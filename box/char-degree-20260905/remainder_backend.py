#!/usr/bin/env python3
"""Full characteristic rows without expanded monic quotient substitution.

Use the necessary U=8V/3 graph and enforce v²-UH remainder degree < k.
Retain all remainder and full characteristic coefficient rows. All changes
are polynomial identities or the audited front quotient consequence.
"""
import argparse,hashlib,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'review'))
from active_ring_backend import from_g9966_input

def script_for(h_expr,D_expr,C_expr,residual_strings,names,k,target,face_expr,
               leader_name=None,leader_inverse=None,localizer_rows=('Zc*c-1',),
               predefinitions=()):
    leader_name=leader_name or f'leader{target}'
    leader_inverse=leader_inverse or f'Z{target}'
    ambient=6*k-2;depth=ambient-target
    # The caller's face_expr is the H-adic digit face. Multiply by H0.
    h0='zz^24*(1+zz)^9' if k==33 else 'zz^28*(1+zz)^8'
    lines=[f'ring R=0,(zz,tt,{",".join(names)}),(lp(1),dp({len(names)+1}));',
      'option(redSB);print("BEGIN_REMAINDER_BUILD");',
      *[f'poly {n}={e};' for n,e in predefinitions],
      f'poly h={h_expr};poly D={D_expr};poly C={C_expr};',
      f'poly H=h-(1/6)*target_b*tt^{k};',
      f'poly vv=D+((1/3)*target_a+(1/18)*target_b^2)*tt^{2*k-1};',
      f'poly VV=C-(1/4)*target_b*tt^{k}*D+((1/12)*target_a*target_b+(1/54)*target_b^3-(1/2)*target_c)*tt^{3*k-1};',
      'poly UU=(8/3)*VV/tt;if(tt*UU-(8/3)*VV!=0){ERROR("U monomial shift failed");}',
      'poly aa=target_a+(1/4)*target_b^2;poly dd=target_d+(1/2)*target_b*target_c;',
      'poly pp=dd-(1/3)*aa^2;poly qq=target_e+(1/4)*target_c^2-(1/3)*aa*dd+(2/27)*aa^3;',
      f'intvec tw=0,1,{",".join("0" for _ in names)};',
      f'intvec zw=1,0,{",".join("0" for _ in names)};',
      'ideal I='+(','.join(residual_strings) if residual_strings else '0')+';',
      'print("BEGIN_REMAINDER_PRODUCT");poly Rraw=vv^2-UU*H;print("END_REMAINDER_PRODUCT");',
      'matrix cr=coef(Rraw,tt*zz);poly RR=0;int j;int charRows=0;',
      f'for(j=1;j<=ncols(cr);j++){{if(deg(cr[1,j],zw)<{k}){{RR=RR+cr[1,j]*cr[2,j];}}else{{I[size(I)+1]=cr[2,j];charRows++;}}}}',
      'kill Rraw,cr;print("END_REMAINDER_EXTRACT");',
      'print("BEGIN_CHARACTERISTIC_PRODUCT");poly HH=H^2;',
      f'poly Qrow=jet((3/4)*RR*HH,{depth},tw);print("CHAR_TERM_RH2");',
      f'Qrow=Qrow-jet((1/8)*tt*vv*UU*H,{depth},tw);print("CHAR_TERM_vUH");',
      f'Qrow=Qrow+jet(tt*vv*RR,{depth},tw);print("CHAR_TERM_vR");',
      f'Qrow=Qrow-jet((9/64)*tt^2*UU^2,{depth},tw);',
      f'Qrow=Qrow+jet(pp*tt^{4*k-2}*HH+pp*tt^{4*k-1}*vv+qq*tt^{6*k-2},{depth},tw);',
      f'Qrow=Qrow-{leader_name}*tt^{depth}*({face_expr})*({h0});',
      'print("END_CHARACTERISTIC_PRODUCT");matrix cq=coef(Qrow,tt*zz);',
      'for(j=1;j<=ncols(cq);j++){I[size(I)+1]=cq[2,j];charRows++;}',
      f'I[size(I)+1]={leader_inverse}*{leader_name}-1;',
      *[f'I[size(I)+1]={r};' for r in localizer_rows],
      'print("BEGIN_ROW_COUNTS");print(charRows);print(size(I));print("END_ROW_COUNTS");',
      'kill cq,Qrow,HH,RR,H,h,D,C,vv,VV,UU,aa,dd,pp,qq;',
      'print("BEGIN_GB");ideal SB=std(I);print("END_GB");print("BEGIN_RESULT");print(reduce(1,SB));print(dim(SB));print(size(SB));print("END_RESULT");',
      f'ideal neg={leader_name},{leader_inverse}*{leader_name}-1;ideal pos={leader_name}-1,{leader_inverse}*{leader_name}-1;',
      'print("BEGIN_CONTROLS");print(reduce(1,std(neg)));print(reduce(1,std(pos)));print("END_CONTROLS");quit;']
    return '\n'.join(lines)+'\n'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args()
    args=from_g9966_input(a.input);script=script_for(**args)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(script)
    meta={'input':str(a.input),'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
      'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'script_sha256':hashlib.sha256(script.encode()).hexdigest(),
      'field':'Q','ring_generators':['zz','tt']+args['names'],
      'full_source_rows_retained':True,'all_five_targets_retained':True,
      'added_consequence':'U=8V/3; deg_y(v^2-UH)<k',
      'row_equivalence':'R high coefficients zero; Q identity modulo those rows; full totaldegree/top target subtraction',
      'status':'EMITTED_NOT_DECIDED'}
    a.out.with_suffix('.map.json').write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'script_bytes':len(script),'parameters':len(args['names']),'script_sha256':meta['script_sha256']}))

if __name__=='__main__':main()
