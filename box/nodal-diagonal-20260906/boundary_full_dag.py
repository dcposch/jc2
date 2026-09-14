#!/usr/bin/env python3
"""Complete normalized delta5/2 boundary/characteristic/Jacobian DAG.

R=G^3-F^2+pG+q. The three square/depression target coordinates are factored
by an explicit target automorphism; q is a free factor. Every remainder is
retained. Numeric evaluations are controls, not solutions of the residual
ideal. Only compact circuit hashes are written; the driver regenerates them.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from math import comb
import argparse
import json
import resource
import signal
import time

from boundary_counts import SPECS
from boundary_maps import build, major_face, minor_face


class CpuBound(Exception):
    pass


def cpu_alarm(signum, frame):
    raise CpuBound("840 CPU second bound reached")


class Emit:
    def __init__(self):
        self.groups = []
        self.first_constant_obstruction = None

    def block(self, name, values):
        digest = sha256()
        count = zero_constants = nonzero_constants = 0
        evaluated_nonzero = [0, 0]
        first_nonzero_eval = None
        for value in values:
            digest.update(f"{count}:".encode() + value.digest)
            count += 1
            if value.constant == 0:
                zero_constants += 1
            elif value.constant is not None:
                nonzero_constants += 1
                if self.first_constant_obstruction is None:
                    self.first_constant_obstruction = [name, count-1, str(value.constant)]
            for point in range(2):
                if value.values[point]:
                    evaluated_nonzero[point] += 1
                    if first_nonzero_eval is None:
                        first_nonzero_eval = [count-1, point,
                            sha256(str(value.values[point]).encode()).hexdigest()]
        result = dict(name=name, coefficients=count, literal_zero_constants=zero_constants,
                      literal_nonzero_constants=nonzero_constants,
                      evaluated_nonzero_counts=evaluated_nonzero,
                      coefficient_circuits_sha256=digest.hexdigest(),
                      first_nonzero_evaluation_hash=first_nonzero_eval)
        self.groups.append(result)
        return result


def add_poly(C, terms, size=None):
    if size is None:
        size = max((len(p) for _, p in terms), default=0)
    return [C.add([(scalar, p[i]) for scalar, p in terms if i < len(p)])
            for i in range(size)]


def multiply(C, p, q):
    if not p or not q:
        return []
    rows = [[] for _ in range(len(p)+len(q)-1)]
    for i, a in enumerate(p):
        if a.constant == 0:
            continue
        for j, b in enumerate(q):
            if b.constant != 0:
                rows[i+j].append((1, C.mul(a,b)))
    return [C.add(row) for row in rows]


def bracket(C, p, q, N, M):
    if not p or not q:
        return []
    # The possible coefficient of degree N+M-1 cancels identically.
    rows = [[] for _ in range(max(0,N+M-1))]
    for a, u in enumerate(p):
        if u.constant == 0:
            continue
        for b, v in enumerate(q):
            scalar = N*b-M*a
            if scalar and v.constant != 0:
                rows[a+b-1].append((scalar,C.mul(u,v)))
    return [C.add(row) for row in rows]


def monic_division(C, numerator, denominator):
    """Exact polynomial graph operation; the remainder is always retained."""
    assert denominator[-1] == 1
    degree = len(denominator)-1
    current = numerator[:]
    quotient = [C.const(0)] * max(0,len(current)-degree)
    for i in range(len(current)-1,degree-1,-1):
        leader = current[i]
        quotient[i-degree] = leader
        for j, scalar in enumerate(denominator):
            if scalar:
                current[i-degree+j] = C.add([(1,current[i-degree+j]),(-scalar,leader)])
    return quotient,current[:degree]


def physical_boundary(C, E, name, physical, D, d, h, pole, scale, state, lam):
    major = major_face(C,name,lam)
    minor = minor_face(C,name,lam)
    zero=C.const(0)
    major_rows=[]
    for N in range(D+1):
        p=physical[N]
        # y=(z+x): coefficient at w-1 equals sum_{j>=k}binom(j,k)*p_j.
        for k in range(N+1):
            weight=d*N-(d+1)*k
            if weight>=h:
                value=C.add([(comb(j,k),p[j]) for j in range(k,N+1)])
                if weight==h:
                    target=major[k] if k<len(major) else zero
                    value=C.add([(1,value),(-1,target)])
                major_rows.append(value)
    E.block(name+"_major_full",major_rows)
    minor_rows=[]
    for N in range(D+1):
        residue=0
        while Q(N)-scale*residue>=pole:
            equality=Q(N)-scale*residue==pole
            terms=[]
            for a in range((D-N)//2+1):
                for bb in range((D-N-2*a)//3+1):
                    NN,j=N+2*a+3*bb,residue+a+bb
                    if j<=NN:
                        p=physical[NN][j]
                        if p.constant!=0:
                            terms.append((comb(j,residue)*comb(a+bb,a),
                                          C.mul(state["centre_products"][a,bb],p)))
            if equality and residue<len(minor):
                terms.append((-1,minor[residue]))
            minor_rows.append(C.add(terms))
            residue+=1
    E.block(name+"_minor_full",minor_rows)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--client",choices=["delta52","delta2","108"],default="delta52")
    args=parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(840,900))
    resource.setrlimit(resource.RLIMIT_AS,(1900*1024**2,1900*1024**2))
    signal.signal(signal.SIGXCPU,cpu_alarm)
    started=time.monotonic()
    spec_index={"delta2":0,"delta52":2,"108":4}[args.client]
    fspec,gspec=SPECS[spec_index],SPECS[spec_index+1]
    fname,n,d,hF,poleF,scale=fspec
    gname,m,_,_,_,_=gspec
    rdegree=63 if n==108 else 55
    rname="108_free_mean_R_conditional" if n==108 else "99_"+args.client+"_R_conditional"
    rh,rpole=(7,Q(7)) if n==108 else (5,Q(10) if args.client=="delta2" else Q(5,2))
    E=Emit()
    receipt=dict(client=args.client,status="RUNNING",normalization="R=G^3-F^2+pG+q",
                 target_action_factors=3,q_is_independent_free_factor=True,
                 arbitrary_evaluations_are_not_survivors=True)
    destination=Path(__file__).with_name("boundary_full_dag_"+args.client+".json")
    phase="G boundary"
    try:
        gcheck,state=build(gspec,{},return_state=True)
        C=state["C"]
        zero=C.const(0)
        # F needs more centre products than G's original map.
        up=C.power(state["u"],n//2)
        vp=C.power(state["v"],n//3)
        state["centre_products"]={(a,b):C.mul(up[a],vp[b])
            for a in range(n//2+1) for b in range((n-2*a)//3+1)}
        G=[state["coeff_y"][m-r] for r in range(m+1)]
        pF,qF=(24,84) if n==108 else (27,72)
        ftop=[Q(0)]*(n+1)
        for i in range(qF+1):
            ftop[pF+i]=Q(comb(qF,i)*(-1)**(qF-i))
        F=[[C.const(x) for x in ftop]]
        G2,Rphysical={},{}
        parameter_p=None
        phase="characteristic recursive bands"
        for r in range(2*n+1):
            if r<=2*m:
                pieces=[]
                for i in range(max(0,r-m),min(m,r)+1):
                    j=r-i
                    if i<=j:
                        pieces.append((1 if i==j else 2,multiply(C,G[i],G[j])))
                G2[r]=add_poly(C,pieces,size=2*m-r+1)
            cube=[]
            for i in range(max(0,r-2*m),min(m,r)+1):
                cube.append((1,multiply(C,G[i],G2[r-i])))
            g3=add_poly(C,cube,size=2*n-r+1)
            if r==0:
                continue
            square=[]
            for i in range(max(1 if r<=n else 0,r-n),min(n,r-1 if r<=n else r)+1):
                j=r-i
                if i<=j and i<len(F) and j<len(F):
                    square.append((1 if i==j else 2,multiply(C,F[i],F[j])))
            numerator=add_poly(C,[(1,g3)]+[(-s,p) for s,p in square],size=2*n-r+1)
            if r<=n:
                quotient,remainder=monic_division(C,numerator,ftop)
                F.append(add_poly(C,[(Q(1,2),quotient)],size=n-r+1))
                E.block("characteristic_upper_depth_"+str(r),remainder)
            else:
                if r==2*n-m:
                    parameter_p=C.add([(-1,numerator[-1])])
                if parameter_p is not None:
                    gi=r-(2*n-m)
                    if 0<=gi<=m:
                        numerator=add_poly(C,[(1,numerator),(1,[C.mul(parameter_p,v) for v in G[gi]])],size=2*n-r+1)
                if 2*n-r>rdegree:
                    E.block("characteristic_upper_depth_"+str(r),numerator)
                else:
                    Rphysical[2*n-r]=numerator
            if r%10==0:
                print(json.dumps(dict(phase=phase,depth=r,nodes=C.nodes,
                                      elapsed=round(time.monotonic()-started,1))),flush=True)
        lam=Rphysical[rdegree][-1]
        jacobian_scalar=C.add([(Q(-3315,2048) if n==108 else Q(-455,243),lam)])
        receipt.update(G_boundary_receipt=gcheck,
            coefficient_generators=len(C.free_names),
            retained_centre_generators=4 if n==108 else 3,
            total_generators_including_q=len(C.free_names)+(4 if n==108 else 3)+1,
            p_circuit_sha256=parameter_p.digest.hex(),lambda_circuit_sha256=lam.digest.hex(),
            q_does_not_occur_in_residuals=True)
        phase="F and R complete boundary rows"
        Fphysical={n-r:f for r,f in enumerate(F)}
        physical_boundary(C,E,fname,Fphysical,n,d,hF,poleF,scale,state,C.const(1))
        physical_boundary(C,E,rname,Rphysical,rdegree,d,rh,rpole,scale,state,lam)
        phase="all Jacobian bands"
        for r in range(n+m-1):
            pieces=[]
            for i in range(max(0,r-m),min(n,r)+1):
                j=r-i
                if j<=m:
                    pieces.append((1,bracket(C,F[i],G[j],n-i,m-j)))
            values=add_poly(C,pieces,size=n+m-1-r)
            if r==n+m-2:
                values[0]=C.add([(1,values[0]),(-1,jacobian_scalar)])
            E.block("jacobian_depth_"+str(r),values)
            if r%10==0:
                print(json.dumps(dict(phase=phase,depth=r,nodes=C.nodes,
                                      elapsed=round(time.monotonic()-started,1))),flush=True)
        receipt["status"]="COMPLETE_DAG_RESIDUAL_IDEAL_UNDECIDED"
        receipt["all_residuals_retained"]=True
        receipt["distinguished_element"]="separation * derived lambda"
    except (CpuBound,MemoryError) as exc:
        receipt["status"]="BOUNDED_DAG_INCOMPLETE"
        receipt["bound_reason"]=type(exc).__name__+": "+str(exc)
    finally:
        receipt.update(last_phase=phase,elapsed_seconds=round(time.monotonic()-started,3),
                       maximum_resident_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                       residual_blocks=E.groups,first_literal_constant_obstruction=E.first_constant_obstruction,
                       total_retained_coefficients=sum(g["coefficients"] for g in E.groups))
        if "C" in locals():
            receipt["circuit_nodes_constructed"]=C.nodes
        destination.write_text(json.dumps(receipt,separators=(",", ":"))+"\n")
        print(json.dumps({k:v for k,v in receipt.items() if k not in ("residual_blocks","G_boundary_receipt")}),flush=True)


if __name__=="__main__":
    main()
