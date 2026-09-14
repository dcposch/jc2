#!/usr/bin/env python3
"""Full characteristic rows in normalized t,z coordinates, exact monic division.

Changing the chart's polynomial coordinates before division avoids expanding
z=y/x-1. The four divisions and output rows are equivalent to the physical
backend. Moh Prop4.5 total-degree/top-form rows are imposed with targets.
"""
from pathlib import Path
import argparse,hashlib,json,subprocess,os,signal,time
import sympy as sp
from char_degree_driver import build,exprS
OUT=Path(__file__).resolve().parent

def normalized_polyS(table):
    return '+'.join(f'({exprS(v)})*tt^{r}*zz^{q}' for (r,q),v in sorted(table.items())) or '0'

def normalized_script(h_expr,D_expr,C_expr,residual_strings,names,k,target,face_expr,
                      leader_name=None,leader_inverse=None,localizer_rows=('Zc*c-1',)):
    assert k < target < 2*k
    leader_name=leader_name or f'leader{target}';leader_inverse=leader_inverse or f'Z{target}'
    vd,cd,rd,ed,ld=2*k-1,3*k-1,4*k-2,5*k-3,6*k-3
    face_depth=ed-(target-k);low_depth=ld-(target-1)
    lines=[f'ring R=0,(zz,tt,{",".join(names)}),(lp(1),dp({len(names)+1}));',
      'option(redSB);print("BEGIN_BUILD_NORMALIZED");',
      f'poly h={h_expr};poly D={D_expr};poly C={C_expr};',
      f'poly H=h-(1/6)*target_b*tt^{k};',
      'poly aa=target_a+(1/4)*target_b^2;poly dd=target_d+(1/2)*target_b*target_c;',
      'poly pp=dd-(1/3)*aa^2;poly qq=target_e+(1/4)*target_c^2-(1/3)*aa*dd+(2/27)*aa^3;',
      f'poly vv=D+((1/3)*target_a+(1/18)*target_b^2)*tt^{vd};',
      f'poly VV=C-(1/4)*target_b*tt^{k}*D+((1/12)*target_a*target_b+(1/54)*target_b^3-(1/2)*target_c)*tt^{cd};',
      'print("BEGIN_DIVIDE_vv2");list L0=division(vv^2,ideal(H));matrix M0=L0[1];ideal N0=L0[2];poly UU=M0[1,1];poly RR=N0[1];',
      'if(vv^2-UU*H-RR!=0){ERROR("division0 identity failed");}print("END_DIVIDE_vv2");print(size(UU));print(size(RR));',
      'print("BEGIN_DIVIDE_vvU");list L1=division(vv*UU,ideal(H));matrix M1=L1[1];ideal N1=L1[2];poly PP=M1[1,1];poly RR1=N1[1];',
      'if(vv*UU-PP*H-RR1!=0){ERROR("division1 identity failed");}print("END_DIVIDE_vvU");print(size(PP));print(size(RR1));',
      'print("BEGIN_DIVIDE_vvR");list L2=division(vv*RR,ideal(H));matrix M2=L2[1];ideal N2=L2[2];poly Qpart=M2[1,1];poly RR2=N2[1];',
      'if(vv*RR-Qpart*H-RR2!=0){ERROR("division2 identity failed");}print("END_DIVIDE_vvR");print(size(Qpart));print(size(RR2));',
      'print("BEGIN_DIVIDE_U2");list L3=division(UU^2,ideal(H));matrix M3=L3[1];ideal N3=L3[2];poly WW=M3[1,1];poly RR3=N3[1];',
      'if(UU^2-WW*H-RR3!=0){ERROR("division3 identity failed");}print("END_DIVIDE_U2");print(size(WW));print(size(RR3));',
      'poly derivedV=VV-(3/8)*tt*UU;',
      f'poly upper=(3/4)*RR+pp*tt^{rd}-(1/8)*tt*PP;',
      'poly digit=Qpart-(1/8)*RR1-(9/64)*tt*WW;',
      f'poly low=RR2-(9/64)*tt*RR3+pp*tt^{rd}*vv+qq*tt^{ld};',
      f'poly digitDifference=digit-{leader_name}*tt^{face_depth}*({face_expr});',
      'print("BEGIN_EXTRACT_CHARACTERISTIC");matrix cv=coef(derivedV,tt*zz);matrix cu=coef(upper,tt*zz);matrix ce=coef(digitDifference,tt*zz);matrix cl=coef(low,tt*zz);',
      'print("END_EXTRACT_CHARACTERISTIC");',
      f'intvec wt=0,1,{",".join("0" for _ in names)};',
      'ideal I='+(','.join(residual_strings) if residual_strings else '0')+';',
      'int j;int charRows=0;',
      'for(j=1;j<=ncols(cv);j++){I[size(I)+1]=cv[2,j];charRows++;}for(j=1;j<=ncols(cu);j++){I[size(I)+1]=cu[2,j];charRows++;}',
      f'for(j=1;j<=ncols(ce);j++){{if(deg(ce[1,j],wt)<={face_depth}){{I[size(I)+1]=ce[2,j];charRows++;}}}}',
      f'for(j=1;j<=ncols(cl);j++){{if(deg(cl[1,j],wt)<{low_depth}){{I[size(I)+1]=cl[2,j];charRows++;}}}}',
      f'I[size(I)+1]={leader_inverse}*{leader_name}-1;'+''.join(f'I[size(I)+1]={row};' for row in localizer_rows),
      'print("BEGIN_ROW_COUNTS");print(charRows+1);print(size(I));print("END_ROW_COUNTS");',
      'print("BEGIN_GB");ideal SB=std(I);print("END_GB");print("BEGIN_RESULT");print(reduce(1,SB));print(dim(SB));print(size(SB));print("END_RESULT");',
      f'ideal neg={leader_name},{leader_inverse}*{leader_name}-1;ideal pos={leader_name}-1,{leader_inverse}*{leader_name}-1;',
      'print("BEGIN_CONTROLS");print(reduce(1,std(neg)));print(reduce(1,std(pos)));print("END_CONTROLS");quit;']
    return '\n'.join(lines)+'\n'

def emit(stage):
    maps,res,meta=build(stage,True,normalized=True)
    vs=set(sp.symbols('target_a target_b target_c target_d target_e leader63 Z63 c Zc'))
    for tab in maps.values():
        for v in tab.values():vs|=v.free_symbols
    for _,v in res:vs|=v.free_symbols
    names=sorted(map(str,vs));tag=f'd108_totalface_stage{stage}'+os.environ.get('CHAR_RUN_SUFFIX','')
    script=normalized_script(*(normalized_polyS(maps[k]) for k in ['h2','B2','A3']),[exprS(v) for _,v in res],names,36,63,'zz^21*(1+zz)^6')
    path=OUT/f'{tag}.sing';path.write_text(script)
    meta.update({'tag':tag,'coefficient_field':'QQ','ring_generator_order':['zz','tt']+names,
      'map':'t=1/x,z=y/x-1; normalized degree h=36,D=71,C=107; four divisions transformed exactly',
      'characteristic_condition':'totaldegree63; top=lambda*y^14*(y-x)^49; lambda unit',
      'equivalent_rows':{'derivedV_degree':107,'upper_degree':142,'digit_degree':177,'digit_face_depth':150,'digit_face':'lambda*z^21*(1+z)^6','low_degree':213,'low_vanish_below':151},
      'script_sha256':hashlib.sha256(script.encode()).hexdigest(),'address_space_limit_kib':os.environ.get('CHAR_MEMORY_KIB'),'verdict':'EMITTED_NOT_DECIDED'})
    (OUT/f'{tag}.json').write_text(json.dumps(meta,indent=2,default=str)+'\n')
    print(f'{tag}: emitted {len(script)} bytes; {len(names)} parameters',flush=True)
    return path,meta

def run(stage,timeout):
    path,meta=emit(stage);tag=meta['tag'];t0=time.monotonic()
    with (OUT/f'{tag}.out').open('w') as f:
        proc=subprocess.Popen(['Singular','-q',str(path)],stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
        timed=False
        try:rc=proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed=True;os.killpg(proc.pid,signal.SIGTERM)
            try:rc=proc.wait(timeout=10)
            except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);rc=proc.wait()
    log=(OUT/f'{tag}.out').read_text();errors=[s for s in log.splitlines() if s.lstrip().startswith('?') or 'error occurred' in s]
    run={'timeout':timed,'returncode':rc,'elapsed_seconds':round(time.monotonic()-t0,3),'parser_or_cas_errors':errors[:30],
         'last_progress_marker':next((s for s in reversed(log.splitlines()) if s.startswith(('BEGIN_','END_'))),None),
         'log_sha256':hashlib.sha256(log.encode()).hexdigest()}
    if not errors and 'BEGIN_RESULT\n' in log and 'END_RESULT' in log:
        vals=log.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].splitlines();run.update({'reduce_one':vals[0],'dimension':vals[1],'gb_size':vals[2]})
        meta['verdict']='UNIT' if vals[0]=='0' else 'NONUNIT_NOT_POINT'
    else:
        memory='no more memory' in log.lower() or 'out of memory' in log.lower()
        meta['verdict']='MEMORY_BOUND_OPEN' if memory else ('CAS_ERROR_OPEN' if errors else ('COMPUTE_BOUND_OPEN' if timed else 'PROCESS_ERROR_OPEN' if rc else 'CAS_ERROR_OPEN'))
    meta['run']=run;(OUT/f'{tag}.json').write_text(json.dumps(meta,indent=2,default=str)+'\n');print(json.dumps({'tag':tag,'verdict':meta['verdict'],'run':run}),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--stage',type=int,required=True,choices=range(9));ap.add_argument('--run',action='store_true');ap.add_argument('--timeout',type=int,default=1800);a=ap.parse_args()
    if a.run:run(a.stage,a.timeout)
    else:emit(a.stage)
