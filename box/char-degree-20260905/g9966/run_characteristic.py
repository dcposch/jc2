#!/usr/bin/env python3
"""Full y-degree characteristic block over Q on the corrected source chart.

All source coordinates exist before the two proved degree eliminations.
No t truncation is used in the characteristic block.  The historical rows
are emitted separately at their exact finite caps.  Expansion/GB timeout is
COMPUTE-BOUND, never a unit or point.
"""
import argparse, hashlib, json, os, subprocess, sys, time
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'source'))
import engine as E
from source_data import SOURCE as S, jsonable

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--branch',choices=['delta2','delta52'],required=True)
    ap.add_argument('--stage',type=int,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--gb-seconds',type=int,default=600);ap.add_argument('--term-cap',type=int,default=3000000)
    ap.add_argument('--method',choices=['expand','hadic'],default='hadic')
    args=ap.parse_args();assert 0<=args.stage<=8
    args.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    status={'branch':args.branch,'stage':args.stage,'field':'Q','status':'INITIALIZING',
            'all_five_target_coefficients_retained':True,'characteristic_y_degree':55,
            'characteristic_t_defect':143,'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'checkpoints':[]}
    def save(state,**extra):
        status.update(status=state,elapsed_seconds=time.monotonic()-start,**extra)
        (args.out/'result.json').write_text(json.dumps(status,indent=2,sort_keys=True)+'\n')
        print(state,{k:v for k,v in extra.items() if k in ('last_polynomial','last_terms','row_count','script_bytes','unit','pending')},flush=True)
    h,c2,c3,inner,imeta=E.inner_state(args.branch)
    outer,ofree,ometa=E.outer_state(min(args.stage,7))
    a,b,c,d,e,lam,Z=sp.symbols('ta tb tc td te lambda55 Z55')
    # A2 and B2 have identical homogeneous source blocks and pivot maps.
    # The constants have no strict valuation/source equations.
    degree=S['outer_specs']['B1'][0]
    pre={v:sp.Integer(0) for v in ofree if str(v).startswith('B1c_')}
    pre[sp.Symbol(f'B1c_{degree}_0')]=-b/3
    for v in ofree:
        if str(v).startswith('A2c_'):
            pre[v]=sp.Rational(3,2)*sp.Symbol(str(v).replace('A2c_','B2c_'))
    pre[sp.Symbol('A2c_65_0')]+=a/2
    changed={name:{p:E.substitute_map(v,pre) for p,v in poly.items()} for name,poly in outer.items()}
    A,B,C,D=(changed[n] for n in ('A2','A3','B1','B2'))
    assert all(sp.expand(A.get(p,0)-sp.Rational(3,2)*D.get(p,0)-(a/2 if p==(65,0) else 0))==0 for p in set(A)|set(D))
    assert all(sp.expand(v-(-b/3 if p==(32,0) else 0))==0 for p,v in C.items())
    save('PROVED_DEGREE_ELIMINATIONS_READY',source_inner_dimension=len(inner),source_outer_dimension=len(ofree),
         degree_eliminated_coordinates=len(pre),source_gauge='all source centres free; no new gauge',
         premap={str(k):str(v) for k,v in pre.items()},outer_source=ometa)
    cap=max(args.stage if args.stage>=2 else 1,(E.stage_spec(args.branch,args.stage)['pole_local_power']+S['minor'][args.branch]['cover']-1)//S['minor'][args.branch]['cover'],4)
    Hlow,_,_=E.build_major_h2(args.branch,cap);F,G=E.build_FG(Hlow,changed,cap)
    finite,counts=E.cumulative_rows(args.branch,args.stage,F,G)
    finite=list(imeta['additional_rows'])+finite
    (args.out/'finite-rows.json').write_text(json.dumps({'cap':cap,'rows':[(l,str(v)) for l,v in finite],'counts':counts},indent=2)+'\n')
    free=(inner|ofree)-set(pre)|{a,b,c,d,e,lam,Z}
    # FLINT ring includes physical y,x first, then the full remaining chart
    # coordinates.  lex ensures division by a y-monic polynomial is y-division.
    from flint import fmpq, fmpq_mpoly_ctx
    variables=[sp.Symbol('y'),sp.Symbol('x')]+sorted(free,key=str)
    ctx=fmpq_mpoly_ctx.get(tuple(map(str,variables)),'lex');generators=ctx.gens()
    index={v:i for i,v in enumerate(variables)};yy,xx=generators[:2];zz=yy-xx
    zero=ctx.constant(0)
    def expr(v):
        terms={}
        for mon,coef in sp.expand(v).as_coefficients_dict().items():
            assert coef.is_Rational
            ex=[0]*len(variables)
            for v,power in mon.as_powers_dict().items():
                if v==1:continue
                assert v in index and power.is_Integer and power>=0,(v,power)
                ex[index[v]]=int(power)
            terms[tuple(ex)]=fmpq(int(coef.p),int(coef.q))
        return ctx.from_dict(terms)
    def physical(poly,degree):
        ans=zero
        for (r,q),v in poly.items():
            assert degree-r-q>=0
            if v!=0:ans+=expr(v)*xx**(degree-r-q)*zz**q
        return ans
    def checkpoint(name,p):
        count=len(p.to_dict());status['checkpoints'].append({'name':name,'terms':count,'seconds':time.monotonic()-start})
        save('EXPANDING_FULL_CHARACTERISTIC',last_polynomial=name,last_terms=count)
        if count>args.term_cap:
            save('COMPUTE-BOUND-EXACT-EXPANSION-TERM-CAP',pending='full characteristic coefficients and Groebner basis');sys.exit(0)
        return p
    hp=checkpoint('h3',physical(h,11));c2p=physical(c2,22);c3p=physical(c3,33)
    H=checkpoint('h2',hp**3+c2p*hp+c3p)
    Bp=checkpoint('A3',physical(B,98));Dp=checkpoint('B2',physical(D,65))
    aa,bb,cc,dd,ee,ll,zzl=[generators[index[v]] for v in (a,b,c,d,e,lam,Z)]
    Cp=-bb/3
    # This coefficient identity is independently checked in controls.py.
    L3=-2*Bp+Cp**3-3*Cp*Dp/2+Cp*aa/2+cc
    L2=-3*Bp*Cp-3*Cp**2*Dp/2-Cp**2*aa/2+3*Dp**2/4+Dp*aa/2-aa**2/4+dd
    L1=-3*Bp*Cp**2-3*Bp*Dp-Bp*aa-3*Cp*Dp**2/2+Cp*Dp*aa/2+Cp*dd+3*Dp*cc/2+aa*cc/2
    L0=-Bp**2-3*Bp*Cp*Dp+Bp*cc+Dp**3+Dp**2*aa+Dp*dd+ee
    if args.method=='hadic':
        # Monic h-adic digits are unique over Q[x,chart].  Since 33<55<66,
        # the h^3 and h^2 digits must vanish, and the h digit has degree22
        # with scalar leader. The h^0 digit has degree<33 and is free.
        u2,v2=divmod(L2,H);checkpoint('L2_quotient',u2);checkpoint('L2_remainder',v2)
        u1,v1=divmod(L1,H);checkpoint('L1_quotient',u1);checkpoint('L1_remainder',v1)
        u0,v0=divmod(L0,H);checkpoint('L0_quotient',u0)
        u00,v00=divmod(u0,H);checkpoint('L0_second_quotient',u00)
        R3=checkpoint('R3',L3+u2);R2=checkpoint('R2',v2+u1+u00);R1=checkpoint('R1',v1+v00)
        assert all(max((ex[0] for ex in p.to_dict()),default=-1)<33 for p in (R3,R2,R1))
        specifications=[('hadic_R3',R3,0,None),('hadic_R2',R2,0,None),('hadic_R1',R1,22,22)]
    else:
        H2=checkpoint('h2_squared',H*H)
        Q=checkpoint('Q',checkpoint('H_L3_plus_L2',H*L3+L2)*H2+H*L1+L0)
        specifications=[('char',Q,55,55)]
    # y-degree criterion only.  q<55 is deliberately unconstrained, even
    # when its total degree exceeds 55.  Equality subtracts the free scalar.
    rows=[];group_count=0
    for label,polynomial,minq,leaderq in specifications:
        groups={}
        for ex,co in polynomial.to_dict().items():
            q,p=ex[:2]
            if q<minq:continue
            key=(p,q);ex0=(0,0)+ex[2:]
            groups.setdefault(key,{})[ex0]=co
        if leaderq is not None:groups.setdefault((0,leaderq),{})
        group_count+=len(groups)
        rows.extend((f'{label}_x{p}_y{q}',ctx.from_dict(poly)-(ll if leaderq is not None and (p,q)==(0,leaderq) else zero)) for (p,q),poly in sorted(groups.items(),key=lambda it:(-it[0][1],-it[0][0])))
    rows.append(('char_leader_unit',zzl*ll-1))
    rows += [(label,expr(v)) for label,v in finite if v!=0]
    localizer=generators[index[sp.Symbol('rho' if args.branch=='delta2' else 'c')]]
    # Extra wrapper variable is declared only in the Singular ambient ring.
    names=list(map(str,variables[2:]));assert 'Zsep' not in names
    script='ring R=0,('+','.join(names+['Zsep'])+'),dp;\n'
    script+='ideal I='+',\n'.join(str(p) for _,p in rows)+',\nZsep*'+str(localizer)+'-1;\n'
    script+='print("ROWS_READY");ideal G=std(I);print("BEGIN_UNIT");print(reduce(1,G));print("END_UNIT");print("BEGIN_DIM");print(dim(G));print("END_DIM");quit;\n'
    (args.out/'augmented.sing').write_text(script)
    (args.out/'row-index.json').write_text(json.dumps({'ring':names+['Zsep'],'rows':[l for l,p in rows],
        'characteristic_coefficient_row_count':group_count,'full_y_triangle_bound':198,'method':args.method,
        'leader_target_subtracted':True,'script_sha256':hashlib.sha256(script.encode()).hexdigest()},indent=2)+'\n')
    save('ALL-AUGMENTED-ROWS-EMITTED',row_count=len(rows)+1,script_bytes=len(script),
         finite_nonzero_rows=sum(v!=0 for _,v in finite),characteristic_rows=group_count+1)
    try:
        run=subprocess.run(['Singular','-q',str(args.out/'augmented.sing')],capture_output=True,text=True,timeout=args.gb_seconds)
    except subprocess.TimeoutExpired as err:
        (args.out/'singular.out').write_bytes((err.stdout or b'')+(err.stderr or b''))
        save('COMPUTE-BOUND-GROEBNER',gb_seconds=args.gb_seconds);return
    output=run.stdout+run.stderr;(args.out/'singular.out').write_text(output)
    assert run.returncode==0 and not any(line.lstrip().startswith('?') for line in output.splitlines()),output[-4000:]
    unit=output.split('BEGIN_UNIT\n')[1].split('\nEND_UNIT')[0].strip()=='0'
    save('UNIT-CANDIDATE-REQUIRES-INDEPENDENT-GATE-REPLAY' if unit else 'EXACT-Q-NONUNIT-NO-POINT',unit=unit)

if __name__=='__main__':main()
