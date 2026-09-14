#!/usr/bin/env python3
"""Generate/replay exact target-square -> main/boundary unit circuits.

The verifier checks the source identity over the declared number field,
every coefficient image and b degree, and the universal polynomial
identities implementing denominator clearing and both geometric series.
Final coefficients are recorded as finite arithmetic circuits, avoiding
expansion of large powers of the inhomogeneous polynomials A and Delta.
Optional --expand-main additionally expands the cleared main identity.
No modular or properness argument occurs anywhere in this driver.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

parser=argparse.ArgumentParser()
parser.add_argument('t',type=int)
parser.add_argument('--run',action='store_true')
parser.add_argument('--expand-main',action='store_true')
parser.add_argument('--timeout',type=int,default=900)
parser.add_argument('--lift',type=Path,help='Optional independently replayed coefficient file')
args=parser.parse_args()
t=args.t
assert t in (3,4,5)
root=Path(__file__).resolve().parent
raw=root/f'controls_t{t}_raw.sing'
chart=root/f't{t}_chart_data.txt'
lift=args.lift.resolve() if args.lift else root/f't{t}_target2_lift.sing'
mainprelude=root/f't{t}_main_prelude.sing'
paths=[raw,chart,lift,mainprelude]
for path in paths:
    if not path.is_file():
        raise SystemExit(f'MISSING_INPUT {path.name}')
liftlines=lift.read_text().splitlines()
correct=[line for line in liftlines if re.match(rf'^matrix LL\[{2*t-1}\]\[1\]=',line)]
if correct:
    if len(correct)>1 and any(line!=correct[-1] for line in correct):
        raise SystemExit(f'AMBIGUOUS_CORRECT_LIFT_DECLARATIONS {lift.name}')
    matrixline=correct[-1]
else:
    declarations=[re.fullmatch(rf'matrix ([A-Za-z][A-Za-z0-9_]*)\[{2*t-1}\]\[1\];',line) for line in liftlines]
    declarations=[match for match in declarations if match]
    if len(declarations)!=1:
        raise SystemExit(f'MISSING_OR_AMBIGUOUS_CORRECT_LIFT_DECLARATION {lift.name}')
    oldname=declarations[0].group(1)
    assignments=[]
    for k in range(1,2*t):
        prefix=f'{oldname}[{k},1]='
        matches=[line for line in liftlines if line.startswith(prefix)]
        if len(matches)!=1:
            raise SystemExit(f'MISSING_OR_AMBIGUOUS_LIFT_ENTRY {lift.name} row={k}')
        assignments.append('LL'+matches[0][len(oldname):])
    matrixline=f'matrix LL[{2*t-1}][1];\n'+'\n'.join(assignments)
script=raw.read_text()+chart.read_text()+matrixline+'\n'
script+=r'''
proc must(int ok,string msg){if(!ok){print("FAIL "+msg);quit;}}
proc bdeg(poly f){
 matrix cf=coef(f,b); int j; int dd=0; intvec ex;
 for(j=1;j<=ncols(cf);j++){ex=leadexp(cf[1,j]);if(ex[nvars(basering)]>dd){dd=ex[nvars(basering)];}}
 return(dd);
}
proc bcoeff(poly f,int e){
 matrix cf=coef(f,b); int j; intvec ex;
 for(j=1;j<=ncols(cf);j++){ex=leadexp(cf[1,j]);if(ex[nvars(basering)]==e){return(cf[2,j]);}}
 return(poly(0));
}
proc clearb(poly f,poly a,poly D,int powercap){
 int j; poly answer=0;
 for(j=0;j<=powercap;j++){answer=answer+bcoeff(f,j)*a^j*D^(powercap-j);}
 return(answer);
}
proc homogeneous(poly f,int expected){
 intvec ex; int totalwt; int j; poly rem=f;
 while(rem!=0){
  ex=leadexp(rem); totalwt=0;
  for(j=1;j<nvars(basering);j++){totalwt=totalwt+j*ex[j];}
  totalwt=totalwt+(nvars(basering)+1)*ex[nvars(basering)];
  if(totalwt!=expected){return(0);}
  rem=rem-lead(rem);
 }
 return(1);
}
must(nrows(LL)==size(rows) && ncols(LL)==1,"lift_dimensions");
must(Bsol==MM+b*NN && eta==rho+b*sigma,"affine_reconstruction");
must(diff(NN,b)==0 && diff(sigma,b)==0,"affine_b");
must(Delta==NN-sigma && AA==rho-MM && HH==NN*rho-MM*sigma,"chart_definitions");
must(Bsol-eta==b*Delta-AA,"slice_identity");
must(MM*Delta+NN*AA==HH && rho*Delta+sigma*AA==HH,"main_affine_images");
must(target==Bsol*eta,"target_image");
print("SOURCE_AND_CHART_MAPS_PASS");
poly sourceSum=0; ideal actualCleared; int k,j; intvec edegrees; int m=4; int ek,dk;
for(k=1;k<=size(rows);k++){
 sourceSum=sourceSum+LL[k,1]*rows[k];
 ek=bdeg(LL[k,1]); dk=bdeg(rows[k]); edegrees[k]=ek;
 must(dk==bdegrees[k],"saved_row_bdegree");
 must(dk<=3,"row_cubic_b_bound");
 actualCleared[k]=clearb(rows[k],AA,Delta,dk);
 must(diff(actualCleared[k],b)==0,"cleared_row_independent_b");
 must(homogeneous(rows[k],4*nvars(basering)+1-k),"row_weight");
 must(homogeneous(LL[k,1],4*nvars(basering)+1+k),"homogeneous_lift_weight");
 if(ek+dk>m){m=ek+dk;}
}
must(sourceSum==target^2,"literal_source_target_square_identity");
must(bdeg(target^2)<=4,"target_square_degree");
print("EXACT_SOURCE_SQUARE_IDENTITY_PASS");
// Check all coefficients, including high cancellations in the homogenization.
for(j=0;j<=m;j++){
 must(bcoeff(sourceSum,j)==bcoeff(target^2,j),"homogenized_coefficient_identity");
}
// Degree bookkeeping suffices to distribute the degree-m homogenization.
for(k=1;k<=size(rows);k++){
 must(m-edegrees[k]-bdegrees[k]>=0,"nonnegative_clearing_exponent");
}
int rr=m-4; if(rr<4){rr=4;}
must(m<=7 && rr==4,"homogeneous_square_transport_bound");
must(rr-m+4>=0 && rr-4>=0,"nonnegative_inverse_exponents");
print("B_DEGREES="+string(bdegrees));
print("LIFT_B_DEGREES="+string(edegrees));
print("M="+string(m)); print("R="+string(rr));
print("EXACT_HOMOGENIZED_SOURCE_COEFFICIENTS_PASS");
// Actual boundary polynomial equality, before adding the inverse variable.
must(sourceSum-Bsol^2*(eta+Bsol)*(AA-b*Delta)==Bsol^4,"boundary_lift_identity");
print("EXACT_BOUNDARY_SOURCE_IDENTITY_PASS");
'''
script+=f'< "{mainprelude}";\n'
script+=r'''
// Explicit map c_i -> c_i, d -> d, b -> 0; actualCleared is b independent.
ideal checkActualCleared=imap(rsmall,actualCleared);
must(size(checkActualCleared)==size(cleared),"saved_main_row_count");
for(k=1;k<=size(cleared);k++){
 must(checkActualCleared[k]==cleared[k],"saved_main_generator_image");
}
print("SAVED_MAIN_GENERATOR_IMAGES_PASS");
setring rsmall;
'''
if args.expand_main:
    script+=r'''
poly actualSum=0; poly clearedRow; poly clearedLift;
for(k=1;k<=size(rows);k++){
 clearedRow=clearb(rows[k],AA,Delta,bdegrees[k]);
 clearedLift=clearb(LL[k,1],AA,Delta,edegrees[k]);
 actualSum=actualSum+Delta^(m-edegrees[k]-bdegrees[k])*clearedLift*clearedRow;
 print("EXPANDED_MAIN_ROW="+string(k+1));
}
must(actualSum==Delta^(m-4)*HH^4,"expanded_actual_main_identity");
print("EXACT_EXPANDED_MAIN_IDENTITY_PASS");
'''
script+=r'''
// Independent universal arithmetic-circuit checks over Q.
// Q,Y,Z are formal; evaluate Y=A and Z=Delta after these identities.
ring runiversal=0,(Z,Y,Mm,Nn,Rho,Sig,InvU,Hh,Bb,Eta,Ss),dp;
poly universalTarget=(Mm+Nn*Y)^2*(Rho+Sig*Y)^2;
poly homogeneousTarget=(Mm*Z+Nn*Y)^2*(Rho*Z+Sig*Y)^2;
// Homogenize universalTarget coefficientwise in Y, with degree exactly four.
matrix targetCoeff=coef(universalTarget,Y); poly checkHom=0;
intvec exponents; int exponent;
for(j=1;j<=ncols(targetCoeff);j++){
 exponents=leadexp(targetCoeff[1,j]); exponent=exponents[2];
 checkHom=checkHom+targetCoeff[2,j]*Y^exponent*Z^(4-exponent);
}
must(checkHom==homogeneousTarget,"universal_affine_square_homogenization");
// Each replacement is a ring homomorphism; source checked both images = H.
must(Hh^2*Hh^2==Hh^4,"universal_product_image");
poly Wfactor=InvU^rr*Z^(rr-m+4)*Hh^(rr-4);
poly Ptarget=Z^(m-4)*Hh^4;
poly inverseProduct=InvU*Z*Hh; poly geom=0;
for(j=0;j<rr;j++){geom=geom+inverseProduct^j;}
must(Wfactor*Ptarget+(1-inverseProduct)*geom==1,"main_literal_unit_circuit");
print("MAIN_UNIT_CERTIFICATE_CIRCUIT_PASS");
poly boundaryCorrection=Bb^2*Eta^2-Bb^2*(Eta+Bb)*(Eta-Bb);
must(boundaryCorrection==Bb^4,"universal_boundary_difference_of_squares");
poly boundaryGeom=0; for(j=0;j<4;j++){boundaryGeom=boundaryGeom+(Ss*Bb)^j;}
must(Ss^4*Bb^4+(1-Ss*Bb)*boundaryGeom==1,"boundary_literal_unit_circuit");
print("BOUNDARY_UNIT_CERTIFICATE_CIRCUIT_PASS");
print("TRANSPORT_ALL_EXACT_ASSERTIONS_PASS");
quit;
'''
output=root/f't{t}_transport.sing'
output.write_text(script)
manifest={
    't':t,'field':f'Q[d]/(3*d^2-{t+1})','generator_order':[f'c{i}' for i in range(1,t)]+['b'],
    'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
    'selected_matrix_sha256':hashlib.sha256(matrixline.encode()).hexdigest(),
    'source_identity':'sum_{k=2}^{2t} a_k E_k = (B eta)^2; a_k=LL[k-1,1]',
    'coefficient_operator':'clear(f,e)=sum_{j=0}^e coeff_b(f,j)*A^j*Delta^(e-j)',
    'main':{
        'd_k':'deg_b E_k','e_k':'deg_b a_k','m':'max(4,max_k(e_k+d_k))','r':'max(m-4,4)',
        'F_k':'clear(E_k,d_k)','Q_k':'Delta^(m-e_k-d_k)*clear(a_k,e_k)',
        'cleared_identity':'sum Q_k F_k = Delta^(m-4) H^4',
        'W':'u^r Delta^(r-m+4) H^(r-4)',
        'inverse_coefficient':'sum_{j=0}^{r-1}(u Delta H)^j',
        'literal_unit':'1=sum_k (W Q_k) F_k + (sum_{j=0}^{r-1}(u Delta H)^j)*(1-u Delta H)'},
    'boundary':{
        'E_k_coefficient':'s^4 a_k',
        'A_coefficient':'-s^4 B^2 (eta+B)',
        'Delta_coefficient':'s^4 B^2 (eta+B) b',
        'inverse_coefficient':'1+sB+(sB)^2+(sB)^3',
        'literal_unit':'1=sum_k s^4*a_k*E_k-s^4*B^2*(eta+B)*A+s^4*B^2*(eta+B)*b*Delta+(1+sB+(sB)^2+(sB)^3)*(1-sB)'},
    'verification':'GENERATED_NOT_YET_REPLAYED','expanded_main_requested':args.expand_main}
manifestpath=root/f't{t}_transport_circuit.json'
manifestpath.write_text(json.dumps(manifest,indent=2)+'\n')
print(f'GENERATED {output.name}',flush=True)
if args.run:
    env=os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    logfile=root/f't{t}_transport.log'
    with logfile.open('w') as handle:
        try:
            result=subprocess.run(['stdbuf','-oL','-eL','Singular','-q',str(output)],
                                  stdout=handle,stderr=subprocess.STDOUT,env=env,
                                  timeout=args.timeout,check=False)
        except subprocess.TimeoutExpired:
            manifest['verification']='TIMEOUT'
            manifestpath.write_text(json.dumps(manifest,indent=2)+'\n')
            raise SystemExit('TRANSPORT_TIMEOUT')
    log=logfile.read_text()
    print(log,end='',flush=True)
    good=(result.returncode==0 and 'TRANSPORT_ALL_EXACT_ASSERTIONS_PASS' in log
          and not re.search(r'(^FAIL |^\s*\? )',log,re.M))
    manifest['verification']='ALL_EXACT_ASSERTIONS_PASS' if good else 'FAILED'
    for label,key in [('B_DEGREES','row_b_degrees'),('LIFT_B_DEGREES','lift_b_degrees')]:
        match=re.search(rf'^{label}=([0-9,]+)$',log,re.M)
        if match:manifest[key]=list(map(int,match.group(1).split(',')))
    for label,key in [('M','m'),('R','r')]:
        match=re.search(rf'^{label}=([0-9]+)$',log,re.M)
        if match:manifest[key]=int(match.group(1))
    manifest['expanded_main_verified']='EXACT_EXPANDED_MAIN_IDENTITY_PASS' in log
    manifest['transport_script_sha256']=hashlib.sha256(output.read_bytes()).hexdigest()
    manifest['log_sha256']=hashlib.sha256(logfile.read_bytes()).hexdigest()
    manifestpath.write_text(json.dumps(manifest,indent=2)+'\n')
    if not good:raise SystemExit('TRANSPORT_FAILED')
