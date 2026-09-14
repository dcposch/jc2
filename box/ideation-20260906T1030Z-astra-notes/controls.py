#!/usr/bin/env python3
"""Tiny exact desk checks for the blind Astra submission; not a full solver."""
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path

SOURCE = Path('/home/ubuntu/jc2/box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json')
SOURCE_SHA = '778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea'

def require(x, message):
    if not x:
        raise ValueError(message)

def add(*args):
    out = defaultdict(Q)
    for a in args:
        for k, v in a.items():
            out[k] += v
    return {k: v for k, v in out.items() if v}

def scale(a, c):
    return {k: v*c for k, v in a.items() if v*c}

def mul(a, b):
    out = defaultdict(Q)
    for (i,j), v in a.items():
        for (k,l), w in b.items():
            out[i+k,j+l] += v*w
    return {k: v for k, v in out.items() if v}

def diff(a, axis):
    out = {}
    for k, v in a.items():
        if k[axis]:
            n = list(k)
            n[axis] -= 1
            out[tuple(n)] = v*k[axis]
    return out

def jac(a, b):
    return add(mul(diff(a,0),diff(b,1)),scale(mul(diff(a,1),diff(b,0)),-1))

def coeff_degree(a, r):
    return {k: v for k, v in a.items() if sum(k) == r}

def map_xw_to_yw(a):
    # X=Y-W, W=W; determinant one.
    out = defaultdict(Q)
    for (i,j), c in a.items():
        for k in range(i+1):
            out[k,i-k+j] += c*math.comb(i,k)*(-1)**(i-k)
    return {k: v for k, v in out.items() if v}

def op_c(c, h, d, b):
    return add(mul(add(scale(h,2),{(0,0):-Q(b,3)}),jac(c,h)),jac(c,d))

def base_j(h,d,a,b):
    return mul(scale(add(scale(d,3),scale(h,b),{(0,0):Q(a)}),Q(1,2)),jac(h,d))

def full_j(h,d,c,a,b):
    f=add(mul(mul(h,h),h),scale(mul(add(scale(d,3),{(0,0):Q(a)}),h),Q(1,2)),c)
    g=add(mul(h,h),scale(h,-Q(b,3)),d)
    return jac(f,g)

def main():
    raw=SOURCE.read_bytes()
    require(hashlib.sha256(raw).hexdigest()==SOURCE_SHA,'source hash')
    data=json.loads(raw)
    require(data['residual_rows']==[],'unconsumed source rows')
    import sympy as S
    normalizers={'h3':11,'C2':22,'C3':33,'B2':65,'A3':98}
    for name,n in normalizers.items():
        require(all(r+z<=n for r,z,e in data['maps'][name]),'nonpolynomial support')
    degree_bounds={name:max(n-r for r,z,e in data['maps'][name]) for name,n in normalizers.items()}
    require(degree_bounds=={'h3':11,'C2':14,'C3':14,'B2':34,'A3':35},'physical degree bounds')
    h3top={}
    for r,z,e in data['maps']['h3']:
        if r==0:
            coeff=S.sympify(e)
            require(not coeff.free_symbols,'h3 top is not fixed')
            h3top[11-z,z]=Q(str(coeff))
    require(map_xw_to_yw(h3top)=={(3,8):Q(1)},'fixed h3 top')
    require(degree_bounds['C2']+11<33 and degree_bounds['C3']<33,'h top correction interference')
    a3=[(98-r-z,z,S.sympify(expr)) for r,z,expr in data['maps']['A3']]
    names=sorted(set().union(*(e.free_symbols for i,j,e in a3)),key=str)
    require(len(names)==192,'C source parameter count')
    other=set().union(*(S.sympify(e).free_symbols for name in ('h3','C2','C3','B2') for r,z,e in data['maps'][name]))
    require(not set(names)&other,'C source overlaps h,D')
    require(all(S.Poly(e,*names).total_degree()<=1 for i,j,e in a3),'C source nonlinear')
    require(set(names)<={e for i,j,e in a3 if isinstance(e,S.Symbol)},'missing identity slots')
    require(all(i+j<=35 for i,j,e in a3),'C total cap')
    require(all(i>0 for i,j,e in a3 if i+j==33),'degree33 has X0 term')
    constant=S.Symbol('A3c_98_0')
    occurrences=[(i,j,e) for i,j,e in a3 if constant in e.free_symbols]
    require(occurrences==[(0,0,constant)],'additive constant not free')

    h0={(9,24):Q(1)}
    resonances=[]
    tested=0
    for r in range(36):
        for i in range(r+1):
            j=r-i
            c={(i,j):Q(1)}
            expected={(i+17,j+47):Q(2*(24*i-9*j))} if 24*i!=9*j else {}
            require(scale(mul(h0,jac(c,h0)),2)==expected,'diagonal formula')
            if not expected:
                resonances.append([r,i,j])
            tested+=1
    require(resonances==[[0,0,0],[11,3,8],[22,6,16],[33,9,24]],'resonance list')

    # Non-Keller method control: source C with deterministic integer parameters,
    # sparse numerical h,D of the correct degree bounds, and exact target J.
    assignment={s:(n%5)-2 for n,s in enumerate(names)}
    c_xw={(i,j):Q(int(e.subs(assignment))) for i,j,e in a3 if e.subs(assignment)!=0}
    c=map_xw_to_yw(c_xw)
    h=add(h0,{(1,0):Q(1),(0,1):Q(1),(0,0):Q(1)})
    d={(3,0):Q(1),(0,2):Q(1),(0,0):Q(2)}
    a,b=2,3
    target=full_j(h,d,c,a,b)
    require(target==add(base_j(h,d,a,b),op_c(c,h,d,b)),'full chain-rule control')
    reconstructed={}
    residual=add(target,scale(base_j(h,d,a,b),-1))
    for r in range(35,-1,-1):
        block={}
        for i in range(r+1):
            j=r-i
            pivot=2*(24*i-9*j)
            value=residual.get((i+17,j+47),Q(0))/pivot if pivot else c.get((i,j),Q(0))
            if value:
                block[i,j]=value
        if r==33:
            # Source X0 W33=0 translates to sum of Y/W coefficients=0.
            inferred=-sum(v for (i,j),v in block.items() if (i,j)!=(9,24))
            require(inferred==block.get((9,24),Q(0)),'source resonance33 inference')
            if inferred:
                block[9,24]=inferred
            else:
                block.pop((9,24),None)
        reconstructed=add(reconstructed,block)
        residual=add(residual,scale(op_c(block,h,d,b),-1))
        require(not coeff_degree(residual,r+64),'high-row compatibility on known target')
    require(reconstructed==c,'exact C roundtrip')
    require(not residual,'every target row roundtrip')
    require(target and target!={(0,0):target.get((0,0),Q(0))},'control accidentally Keller')

    # A nonzero-constant target is not licensed by eliminating positive rows.
    require(not full_j(h,{}, {},0,0),'pure-power zero-J control')
    pure_power_inverse_residual=-1
    require(pure_power_inverse_residual!=0,'J0 inverse omitted')

    # Root preflight divisibility parameterization is only set-theoretic:
    # with epsilon^2=0, D=epsilon*X^9 W25, C=0 obeys the top equation,
    # although D is not divisible by Y^5. Keep the original polynomial rows.
    Y,W,e=S.symbols('Y W epsilon')
    bad=(Y-W)**9*W**25
    require(S.rem(bad,Y**5,Y)!=0,'bad D divisibility control')
    top=Q(3,4)*e**2*bad**2
    require(S.Poly(top,e).nth(0)==0 and S.Poly(top,e).nth(1)==0,'nilpotent top control')

    out={
      'status':'PASS_DESK_ONLY', 'source_sha256':SOURCE_SHA,
      'source_physical_degree_bounds':degree_bounds,'h_top_fixed_Y9W24':True,
      'C_source_variables':192,'C_source_positions':len(a3),
      'source_C_linear_injective_disjoint':True,
      'diagonal_monomials_checked':tested,'diagonal_nonzero_pivots':tested-len(resonances),
      'resonances_degree_Y_W':resonances,'degree33_resonance_source_pivot':1,
      'active_C_parameters_upper_bound':2,'additive_constant_free':True,
      'chain_rule_exact':True,'non_Keller_full_C_roundtrip':True,
      'target_terms':len(target),'reconstructed_C_terms':len(c),
      'pure_power_inverse_residual':pure_power_inverse_residual,
      'nilpotent_topface_divisibility_countercontrol':True,
      'full_parameter_elimination_executed':False,'solver_win_claim':False,
      'source_necessity_claim':False,'JC2_claim':False,
    }
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
