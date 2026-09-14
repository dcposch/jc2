#!/usr/bin/env python3
"""Exact-Q D108 characteristic-degree augmentation, with immutable old engine.

All source chart rows are retained through rational-pivot maps.  The two
optional derived identities B1=-b/3, A2=(3*B2+a)/2 are necessary when deg_y Q<72;
their proof is recorded separately.  They dramatically reduce the expansion.
Full physical x/y coefficient extraction is used: no zero padding of t-jets.
"""
from __future__ import annotations
import argparse, hashlib, json, os, signal, subprocess, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
import rekill_engine_snapshot as E

OUT = Path(__file__).resolve().parent

def rows_hash(rows):
    return hashlib.sha256(''.join(f'{l}\t{sp.srepr(sp.expand(v))}\n' for l,v in rows).encode()).hexdigest()

def clean(table, subs):
    return {k:v for k,e in table.items() if (v:=E.substitute_map(e,subs)) != 0}

def physical(table, degree):
    """t=1/x,z=y/x-1; t^-degree*K -> Q[x,y], exact finite map."""
    result=defaultdict(lambda:sp.Integer(0))
    for (r,q),v in table.items():
        assert 0 <= q <= degree-r, (degree,r,q)
        for j in range(q+1):
            result[degree-r-j,j] += v*sp.binomial(q,j)*(-1)**(q-j)
    return {k:v for k,e in result.items() if (v:=sp.expand(e)) != 0}

def exprS(e):
    """Unambiguous recursive Singular polynomial serializer (no power/division)."""
    e=sp.sympify(e)
    if e.is_Integer:return str(e)
    if e.is_Rational:return f'({e.p}/{e.q})'
    if e.is_Symbol:return str(e)
    if e.is_Add:return '('+'+'.join(exprS(t) for t in e.args)+')'
    if e.is_Mul:return '('+'*'.join(exprS(t) for t in e.args)+')'
    if e.is_Pow:
        base,power=e.args
        assert power.is_Integer and power>=0,(e,power)
        return f'({exprS(base)})^{power}'
    raise TypeError((e,type(e)))

def polyS(table):
    return '+'.join(f'({exprS(v)})*xx^{i}*yy^{j}' for (i,j),v in sorted(table.items())) or '0'

def build(stage, jet0free=True, normalized=False, early_D=False, strong_front=False):
    t0=time.monotonic(); R=E.SRC
    rows0,hvars,h3=E.minor_incidence(R,R.k3_face,jet0free)
    resid0,subs0,piv0,z0=E.qstar_reduce(rows0,hvars)
    h3r=clean(h3,subs0)
    h2,h2free,h2meta=E.build_major_h2(R,h3r,36,jet0free)
    outer,ofree,ometa=E.outer_state(R,stage)
    a,b,c,d,e,lam,Z=sp.symbols('target_a target_b target_c target_d target_e leader63 Z63')
    # These equations retain the complete source coordinates and are solved
    # only by rational pivots. Constants are independent target coefficients.
    derived=[]
    for pos,v in outer['B1'].items():
        target=-b/3 if pos==(35,0) else 0
        derived.append((f'derived_B1_{pos[0]}_{pos[1]}',sp.expand(v-target)))
    for pos in sorted(set(outer['A2'])|set(outer['B2'])):
        target=sp.Rational(3,2)*outer['B2'].get(pos,0)+(a/2 if pos==(71,0) else 0)
        derived.append((f'derived_A2_{pos[0]}_{pos[1]}',sp.expand(outer['A2'].get(pos,0)-target)))
    dr,ds,dp,dz=E.qstar_reduce(derived,ofree)
    outer={bl:clean(tab,ds) for bl,tab in outer.items()}
    if early_D or strong_front:
        # The first-nonzero-band lemma forces D_r=0 for r<=30. At r31,
        # D31^2=U62*z^28(1+z)^8 and source floors force
        # D31=tau*z^31(1+z)^4, C63=(3/8)*tau^2*z^34. These are
        # field-variety consequences, with tau retained even when zero.
        tau=outer['B2'].get((31,35),sp.Integer(0));pre=[]
        dcut=(32 if stage==0 else 33) if strong_front else 30
        ccut=(66 if stage==0 else 68) if strong_front else 62
        for (r,q),v in outer['B2'].items():
            if r<=dcut:pre.append((f'derived_D_early_{r}_{q}',v))
            elif not strong_front and r==31:pre.append((f'derived_D_firstshape_{q}',sp.expand(v-tau*sp.binomial(4,q-31))))
        for (r,q),v in outer['A3'].items():
            if r<=ccut:pre.append((f'derived_C_early_{r}_{q}',v))
            elif not strong_front and r==63:pre.append((f'derived_C_firstshape_{q}',sp.expand(v-(sp.Rational(3,8)*tau**2 if q==34 else 0))))
        pr,ps,pp,pz=E.qstar_reduce(pre,set(ofree)-set(ds))
        derived+=pre;dr+=pr;ds.update(ps);E.resolve_map(ds);dp+=pp;dz+=pz
        outer={bl:clean(tab,ps) for bl,tab in outer.items()}
    max_t=4+stage
    pure_power_band=not any(r+1<=max_t and value!=0 for tab in outer.values() for (r,q),value in tab.items())
    if pure_power_band:
        # Exact ring-map identity, not a new equation: substitution commutes
        # with multiplication modulo t^(max_t+1). The retained outer series
        # has no coefficient in this band, so F=H^3,G=H^2 here. All scheduled
        # J labels are emitted and equal zero identically.
        hl=E.local_rows(h2,max_t,jet0free)
        gl=E.tz_mul(hl,hl,max_t);fl=E.tz_mul(gl,hl,max_t)
    else:
        KF,KG=E.build_FG(h2,outer,max_t)
        fl=E.local_rows(KF,max_t,jet0free);gl=E.local_rows(KG,max_t,jet0free)
    rows=[(f'h3_incidence_{l}',v) for l,v in resid0]+dr
    for name,tab in [('F',fl),('G',gl)]:
        for n in (1,2,3):
            for k in E.raw_minor_support(name,jet0free).get(n,()):
                rows.append((f'prior_{name}_{n}_{k}',E.pole_coeff(tab,n,k,name)))
    J={} if pure_power_band else E.jacobian_band(KF,KG,1)
    rows += [(f'prior_J_177_{k}',J.get(k,sp.Integer(0))) for k in range(15,25)]
    for cur in range(stage+1):
        sc=E.stage_spec(cur); n=sc['pole_local_power']
        for name,tab in [('F',fl),('G',gl)]:
            for k in E.raw_minor_support(name,jet0free).get(n,()):
                rows.append((f'stage{cur}_{name}_{n}_{k}',E.pole_coeff(tab,n,k,name)))
        js=sc['jacobian']; J={} if pure_power_band else E.jacobian_band(KF,KG,js['t_power'])
        rows += [(f'stage{cur}_J_{js["degree"]}_{k}',J.get(k,sp.Integer(0))) for k in js['w_powers']]
    free=set(h2free)|(set(ofree)-set(ds))|({*hvars}-set(subs0))
    res,subs,pivs,zeros=E.qstar_reduce(rows,free)
    native={'h2':clean(h2,subs),'B2':clean(outer['B2'],subs),'A3':clean(outer['A3'],subs)}
    fullmaps=native if normalized else {key:physical(native[key],degree) for key,degree in [('h2',36),('B2',71),('A3',107)]}
    meta={'stage':stage,'jet0_free':jet0free,'field':'QQ','gauge_ledger':E.GAUGE_LEDGER,
          'char_degree':{'n':108,'m':72,'M1':-72,'M2':81,'d2':36,'q2':153,'lambda2':-2268,'mu2':-63,
                         'degree_y':63,'constant_leader_t_deficit':153},
          'h3_raw_rows':len(rows0),'h3_pivots':len(piv0),'major':h2meta,'outer':ometa,
          'derived_rows':len(derived),'derived_rows_sha256':rows_hash(derived),'early_D_preprocessor':early_D,
          'strong_front_preprocessor':strong_front,
          'strong_front_ledger':({'D_cut_inclusive':dcut,'C_cut_inclusive':ccut,
              'type':'radical consequence over fields, no coordinate gauge',
              'proofs':['../cubic-front-improvement.md','../d108-stage-front-audit.md']} if strong_front else None),
          'derived_pivots':len(dp),'derived_residual':len(dr),
          'source_rows':len(rows),'source_rows_sha256':rows_hash(rows),'pure_power_truncation_identity':pure_power_band,
          'source_pivots':len(pivs),'source_zeros':zeros,'source_residual':len(res),
          'source_residual_rows':{l:str(v) for l,v in res},
          'target_coefficients':list(map(str,[a,b,c,d,e])),
          'physical_map':'t=1/xx, z=yy/xx-1; t^-degree*K; all finite coefficients retained',
          'physical_support_counts':{k:len(v) for k,v in fullmaps.items()},
          'build_seconds':round(time.monotonic()-t0,3),
          'pivot_maps':{'derived':{str(k):str(v) for k,v in ds.items()},'source':{str(k):str(v) for k,v in subs.items()}},
          'pivot_ledger':[{'row':p.label,'variable':str(p.variable),'leader':str(p.coefficient)} for p in dp+pivs]}
    return fullmaps,res,meta

def backend_script(h_expr,D_expr,C_expr,residual_strings,names,digit_degree=27,
                   leader_name='leader63',leader_inverse='Z63',localizer_rows=('Zc*c-1',)):
    """Reusable exact backend; serialized inputs must already be unambiguous.

    Parameters include target_a,...,target_e and named leader/inverse. All
    original source rows and localizations are passed explicitly. The two
    leading identities B1=-b/3,A2=(3D+a)/2 must already be imposed with their
    source coordinate equations retained. H is monic with y-degree k, and
    the desired degree is k+digit_degree strictly between k and 2k.
    """
    lines=[f'ring R=0,(yy,xx,{",".join(names)}),(lp(1),dp({len(names)+1}));',
           'option(redSB);',
           'print("BEGIN_BUILD_PHYSICAL");',
           f'poly h={h_expr};',f'poly D={D_expr};',f'poly C={C_expr};',
           'poly H=h-(1/6)*target_b;',
           'poly aa=target_a+(1/4)*target_b^2;',
           'poly dd=target_d+(1/2)*target_b*target_c;',
           'poly pp=dd-(1/3)*aa^2;',
           'poly qq=target_e+(1/4)*target_c^2-(1/3)*aa*dd+(2/27)*aa^3;',
           'poly vv=D+(1/3)*target_a+(1/18)*target_b^2;',
           'poly VV=C-(1/4)*target_b*D+(1/12)*target_a*target_b+(1/54)*target_b^3-(1/2)*target_c;',
           'print("BEGIN_DIVIDE_vv2");',
           'list L0=division(vv^2,ideal(H));matrix M0=L0[1];ideal N0=L0[2];poly UU=M0[1,1];poly RR=N0[1];',
           'if(vv^2-UU*H-RR!=0){ERROR("division0 identity failed");}',
           'print("END_DIVIDE_vv2");print(size(UU));print(size(RR));',
           'print("BEGIN_DIVIDE_vvU");',
           'list L1=division(vv*UU,ideal(H));matrix M1=L1[1];ideal N1=L1[2];poly PP=M1[1,1];poly RR1=N1[1];',
           'if(vv*UU-PP*H-RR1!=0){ERROR("division1 identity failed");}',
           'print("END_DIVIDE_vvU");print(size(PP));print(size(RR1));',
           'print("BEGIN_DIVIDE_vvR");',
           'list L2=division(vv*RR,ideal(H));matrix M2=L2[1];ideal N2=L2[2];poly Qpart=M2[1,1];poly RR2=N2[1];',
           'if(vv*RR-Qpart*H-RR2!=0){ERROR("division2 identity failed");}',
           'print("END_DIVIDE_vvR");print(size(Qpart));print(size(RR2));',
           # Q = upper*H^2 + Char after coefficientwise VV=3*UU/8.
           # All three divisions are monic in yy over QQ[xx,parameters].
           'poly upper=(3/4)*RR+pp-(1/8)*PP;',
           'poly derivedV=VV-(3/8)*UU;',
           'print("BEGIN_DIVIDE_U2");',
           'list L3=division(UU^2,ideal(H));matrix M3=L3[1];ideal N3=L3[2];poly WW=M3[1,1];poly RR3=N3[1];',
           'if(UU^2-WW*H-RR3!=0){ERROR("division3 identity failed");}',
           'print("END_DIVIDE_U2");print(size(WW));print(size(RR3));',
           # Char=(QQ-RR1/8-9*WW/64)*H + low, deg_y low < 36.
           # Therefore exact degree63/scalar leader is exact degree27/scalar
           # leader of this H-adic digit. e remains a free target constant.
           'poly digit=Qpart-(1/8)*RR1-(9/64)*WW;',
           'print("BEGIN_EXTRACT_CHARACTERISTIC");',
           'matrix cc=coef(digit,xx*yy);matrix cu=coef(upper,xx*yy);matrix cv=coef(derivedV,xx*yy);',
           'print("END_EXTRACT_CHARACTERISTIC");',
           f'intvec wx=0,1,{",".join("0" for _ in names)};',
           f'intvec wy=1,0,{",".join("0" for _ in names)};',
           'ideal I='+(','.join(residual_strings) if residual_strings else '0')+';',
           'int j;int dx;int dy;int charRows=0;poly leader=0;',
           'for(j=1;j<=ncols(cv);j++){I[size(I)+1]=cv[2,j];charRows++;}',
           'for(j=1;j<=ncols(cu);j++){I[size(I)+1]=cu[2,j];charRows++;}',
           f'for(j=1;j<=ncols(cc);j++){{dx=deg(cc[1,j],wx);dy=deg(cc[1,j],wy);if(dy>{digit_degree}||(dy=={digit_degree}&&dx>0)){{I[size(I)+1]=cc[2,j];charRows++;}}if(dy=={digit_degree}&&dx==0){{leader=cc[2,j];}}}}',
           f'I[size(I)+1]=leader-{leader_name};I[size(I)+1]={leader_inverse}*{leader_name}-1;'+''.join(f'I[size(I)+1]={row};' for row in localizer_rows),
           'print("BEGIN_ROW_COUNTS");print(charRows+2);print(size(I));print("END_ROW_COUNTS");',
           'print("BEGIN_GB");ideal SB=std(I);print("END_GB");',
           'print("BEGIN_RESULT");print(reduce(1,SB));print(dim(SB));print(size(SB));print("END_RESULT");',
           f'ideal neg={leader_name},{leader_inverse}*{leader_name}-1;ideal pos={leader_name}-1,{leader_inverse}*{leader_name}-1;',
           'print("BEGIN_CONTROLS");print(reduce(1,std(neg)));print(reduce(1,std(pos)));print("END_CONTROLS");quit;']
    return '\n'.join(lines)+'\n'

def emit(stage,jet0free=True):
    maps,res,meta=build(stage,jet0free)
    variables=set(sp.symbols('target_a target_b target_c target_d target_e leader63 Z63 c Zc'))
    for tab in maps.values():
        for v in tab.values(): variables|=v.free_symbols
    for _,v in res: variables|=v.free_symbols
    names=sorted(map(str,variables))
    script=backend_script(*(polyS(maps[k]) for k in ['h2','B2','A3']),
                          [exprS(v) for _,v in res],names)
    tag=f'd108_char_jet0{"free" if jet0free else "pinned"}_stage{stage}'
    p=OUT/f'{tag}.sing';p.write_text(script)
    meta.update({'tag':tag,'script':p.name,'script_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                 'ring_generator_order':['yy','xx']+names,'coefficient_field':'QQ',
                 'implementation':'full x/y coefficient rows; four exact monic-y divisions, no t-truncation; VV=3U/8 and upper=0 coefficientwise plus exact degree27/scalar-unit H-adic digit (equivalent degree63)',
                 'verdict':'EMITTED_NOT_DECIDED'})
    (OUT/f'{tag}.json').write_text(json.dumps(meta,indent=2,default=str)+'\n')
    print(f'{tag}: emitted {p.stat().st_size} bytes, {len(names)} parameters, source rows {len(res)}',flush=True)
    return p,meta

def emit_maps(maps,res,meta,k,target,tag,out,extra_variables=()):
    """Shared complete-row emitter for a preprocessed source chart.

    maps contains physical exponent maps B2,A3 and either h2 or h3,C2,C3.
    The latter means h2=h3^3+C2*h3+C3. The source caller owns necessity and
    the retained equations for the two leading reductions. No source row is
    discarded here. Unused declared chart variables can be included through
    extra_variables; omitted variables are a free polynomial extension.
    """
    assert k < target < 2*k
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    leader=f'leader{target}';inv=f'Z{target}'
    variables=set(sp.symbols('target_a target_b target_c target_d target_e c Zc'))
    variables|={sp.Symbol(leader),sp.Symbol(inv)}|set(map(sp.Symbol,map(str,extra_variables)))
    for tab in maps.values():
        for v in tab.values():variables|=sp.sympify(v).free_symbols
    for _,v in res:variables|=sp.sympify(v).free_symbols
    names=sorted(map(str,variables));defs=''
    if 'h2' in maps:h_expr=polyS(maps['h2'])
    else:
        defs='\n'.join(f'poly {label}={polyS(maps[key])};' for key,label in [('h3','baseH'),('C2','innerC2'),('C3','innerC3')])+'\n'
        h_expr='baseH^3+innerC2*baseH+innerC3'
    script=backend_script(h_expr,polyS(maps['B2']),polyS(maps['A3']),
                          [exprS(v) for _,v in res],names,target-k,leader,inv)
    script=script.replace('print("BEGIN_BUILD_PHYSICAL");\n','print("BEGIN_BUILD_PHYSICAL");\n'+defs)
    path=out/f'{tag}.sing';path.write_text(script)
    record=dict(meta);record.update({'tag':tag,'script':path.name,'script_sha256':hashlib.sha256(script.encode()).hexdigest(),
                                   'coefficient_field':'QQ','ring_generator_order':['yy','xx']+names,
                                   'h2_degree':k,'characteristic_degree':target,'adic_digit_degree':target-k,
                                   'verdict':'EMITTED_NOT_DECIDED'})
    (out/f'{tag}.json').write_text(json.dumps(record,indent=2,default=str)+'\n')
    return path,record

def run(stage,jet0free,timeout):
    p,meta=emit(stage,jet0free);tag=meta['tag'];t0=time.monotonic()
    with (OUT/f'{tag}.out').open('w') as out:
        proc=subprocess.Popen(['Singular','-q',str(p)],stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
        timed=False
        try: code=proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed=True;os.killpg(proc.pid,signal.SIGTERM)
            try:code=proc.wait(timeout=10)
            except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);code=proc.wait()
    log=(OUT/f'{tag}.out').read_text(); result={'timeout':timed,'returncode':code,'elapsed_seconds':round(time.monotonic()-t0,3)}
    errors=[s for s in log.splitlines() if s.lstrip().startswith('?') or 'error occurred' in s]
    result['parser_or_cas_errors']=errors[:30]
    if not errors and 'BEGIN_RESULT\n' in log and 'END_RESULT' in log:
        vals=log.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].strip().splitlines()
        result.update({'reduce_one':vals[-3],'dimension_including_unused_xy':vals[-2],'gb_size':vals[-1]})
        meta['verdict']='UNIT' if vals[-3]=='0' else 'NONUNIT_NOT_POINT'
    else:meta['verdict']='CAS_ERROR_OPEN' if errors else ('COMPUTE_BOUND_OPEN' if timed else 'CAS_ERROR_OPEN')
    result['last_progress_marker']=next((s for s in reversed(log.splitlines()) if s.startswith(('BEGIN_','END_'))),None)
    result['log_sha256']=hashlib.sha256(log.encode()).hexdigest();meta['run']=result
    (OUT/f'{tag}.json').write_text(json.dumps(meta,indent=2,default=str)+'\n')
    print(json.dumps({'tag':tag,'verdict':meta['verdict'],'run':result}),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--stage',type=int,required=True,choices=range(9));ap.add_argument('--jet0pinned',action='store_true');ap.add_argument('--run',action='store_true');ap.add_argument('--timeout',type=int,default=1800)
    a=ap.parse_args()
    if a.run:run(a.stage,not a.jet0pinned,a.timeout)
    else:emit(a.stage,not a.jet0pinned)
