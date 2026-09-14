#!/usr/bin/env python3
"""Bind the independently replayed t=5 rank proof to literal X unit circuits."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess

root=Path(__file__).resolve().parent
rankpath=root/'t5_rank_independent_result.json'
rank=json.loads(rankpath.read_text())
assert rank['verdict']=='INDEPENDENT_T5_RANK_MODEL_AND_DETERMINANT_PASS'
assert rank['determinant_mod_p']==29155
raw=root/'controls_t5_raw.sing'; chart=root/'t5_chart_data.txt'
main=root/'t5_main_prelude.sing'; boundary=root/'t5_boundary_prelude.sing'
selected=root/'linear_t5_rank_certificate.json'
for path in (raw,selected):
    assert hashlib.sha256(path.read_bytes()).hexdigest()==rank['hashes'][path.name]
script=raw.read_text()+chart.read_text()+r'''
proc must(int ok,string msg){if(!ok){print("FAIL "+msg);quit;}}
proc bdegree(poly f){matrix cf=coef(f,b);int j;int dd=0;intvec ex;
for(j=1;j<=ncols(cf);j++){ex=leadexp(cf[1,j]);if(ex[5]>dd){dd=ex[5];}}return(dd);}
proc clearb(poly f,int powcap){matrix cf=coef(f,b);int j,e;intvec ex;poly out=0;
for(j=1;j<=ncols(cf);j++){ex=leadexp(cf[1,j]);e=ex[5];out=out+cf[2,j]*AA^e*Delta^(powcap-e);}return(out);}
must(size(rows)==9 && target==Bsol*eta,"source_target_and_row_count");
must(Bsol==MM+b*NN && eta==rho+b*sigma,"affine_source_images");
must(diff(NN,b)==0 && diff(sigma,b)==0,"affinity");
must(Delta==NN-sigma && AA==rho-MM && HH==NN*rho-MM*sigma,"chart_definitions");
must(Bsol-eta==b*Delta-AA,"slice_identity");
must(MM*Delta+NN*AA==HH && rho*Delta+sigma*AA==HH,"main_affine_images");
must((Bsol*eta)^2-Bsol^2*(eta+Bsol)*(AA-b*Delta)==Bsol^4,"boundary_source_identity");
ideal recomputedF;int j,dk,ek;intvec ecaps;
for(j=1;j<=9;j++){
 dk=bdegree(rows[j]);must(dk==bdegrees[j] && dk<=3,"row_bdegree");
 ek=(21+j) div 6;ecaps[j]=ek;must(7-dk-ek>=0,"cramer_homogeneous_cofactor_clearance");
 recomputedF[j]=clearb(rows[j],dk);must(diff(recomputedF[j],b)==0,"b_independent_F");
}
print("EXACT_T5_SOURCE_CHART_AND_DEGREE_MAPS_PASS");
print("B_DEGREES="+string(bdegrees));print("COFACTOR_CAPS="+string(ecaps));
'''
script+=f'< "{main}";\n'
script+=r'''
// Explicit coefficient map: c_i -> c_i, d -> d, b -> 0, on b-independent rows.
ideal testF=imap(rsmall,recomputedF);
must(size(testF)==size(cleared),"saved_main_count");
for(j=1;j<=size(cleared);j++){must(testF[j]==cleared[j],"saved_main_row_map");}
print("EXACT_T5_SAVED_MAIN_GENERATORS_PASS");
setring rsmall;
'''
script+=f'< "{boundary}";\n'
script+=r'''
// Explicit coefficient map c_i -> c_i, b -> b, d -> d; s is newly adjoined.
ideal originalRows=imap(rsmall,rows);
poly originalB=imap(rsmall,Bsol);poly originalDelta=imap(rsmall,Delta);poly originalA=imap(rsmall,AA);
must(size(originalRows)==size(rows),"saved_boundary_count");
for(j=1;j<=size(rows);j++){must(originalRows[j]==rows[j],"saved_boundary_row_map");}
must(originalB==Bsol && originalDelta==Delta && originalA==AA,"saved_boundary_coefficient_maps");
print("EXACT_T5_SAVED_BOUNDARY_GENERATORS_PASS");
ring universal=0,(uu,DD,HH,Zdet,ss,BB,ee),dp;
poly pp=uu*DD*HH;poly gg=1+pp+pp^2+pp^3;
must(uu^4*DD*(Zdet*DD^3*HH^4)+Zdet*gg*(1-pp)==Zdet,"main_determinant_unit_circuit");
poly bg=1+ss*BB+(ss*BB)^2+(ss*BB)^3;
must(ss^4*Zdet*((BB*ee)^2-BB^2*(ee+BB)*(ee-BB))+Zdet*bg*(1-ss*BB)==Zdet,"boundary_determinant_unit_circuit");
print("EXACT_T5_MAIN_AND_BOUNDARY_DETERMINANT_CIRCUITS_PASS");
print("T5_RANK_CHART_CERTIFICATE_ALL_ASSERTIONS_PASS");quit;
'''
driver=root/'t5_rank_chart_maps.sing';driver.write_text(script)
logfile=root/'t5_rank_chart_maps.log'
env=os.environ.copy();env.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
with logfile.open('w') as handle:
    result=subprocess.run(['stdbuf','-oL','-eL','Singular','-q',str(driver)],stdout=handle,stderr=subprocess.STDOUT,env=env,timeout=120)
log=logfile.read_text();print(log,end='',flush=True)
assert result.returncode==0 and 'T5_RANK_CHART_CERTIFICATE_ALL_ASSERTIONS_PASS' in log
assert not re.search(r'(^FAIL |^\s*\? )',log,re.M)
circuit={
 'verdict':'EXACT_T5_MAIN_AND_BOUNDARY_UNIT_BY_REPLAYED_RANK_AND_DETERMINANT_CIRCUITS',
 'field':'k=Q(d), d^2=2; integral generator e=3d, e^2=18',
 'source_ring_generator_order':['c1','c2','c3','c4','b'],
 'basis':'linear_t5_rank_certificate.json:row_monomials (complete ordered weight42 basis)',
 'selected_columns':'linear_t5_rank_certificate.json:selected_columns, in stored order',
 'matrix_entry':'A[i,l]=coefficient_of_basis_monomial_i(scale_l * monomial(multiplier_l) * E_(source_row_l)); scaled coefficients lie in Z[e]',
 'source_vector':'v[i]=coefficient_of_basis_monomial_i((Bsol*eta)^2)',
 'delta':'det(A), a scalar in Z[e] with residue29155 at e=7868 mod32009, hence nonzero in k',
 'cramer_h_l':'det(A with column l replaced by v), using the declared row/column order',
 'cofactor_tilde_a_k':'sum_{l:source_row_l=k} h_l*scale_l*monomial(multiplier_l)',
 'exact_source_identity':'sum_k tilde_a_k*E_k = delta*(Bsol*eta)^2, by A*h=det(A)*v',
 'cofactor_degree_caps':[3,3,4,4,4,4,4,4,5],
 'm':7,'r':4,
 'clear_operator':'C_e(f)=sum_{j=0}^e coefficient_b_j(f)*A_slice^j*Delta^(e-j)',
 'main':{
   'ring':'k[c1,c2,c3,c4,u]',
   'Q_k':'Delta^(7-e_k-d_k)*C_(e_k)(tilde_a_k)',
   'cleared_source_identity':'sum Q_k*F_k=delta*Delta^3*H^4',
   'literal_unit':'1=sum_k (u^4*Delta*Q_k/delta)*F_k +(1+P+P^2+P^3)*(1-P), P=u*Delta*H'},
 'boundary':{
   'ring':'k[c1,c2,c3,c4,b,s]',
   'literal_unit':'1=sum_k (s^4*tilde_a_k/delta)*E_k-s^4*B^2*(eta+B)*A_slice+s^4*B^2*(eta+B)*b*Delta +(1+s*B+(s*B)^2+(s*B)^3)*(1-s*B)'},
 'scalar_division':'Only delta, a verified nonzero element of k, is inverted in certificate coefficients; no polynomial chart denominator is assumed invertible beyond the literal inverse generator.',
 'verification':'Fresh coefficient model and independent NumPy determinant replay + fresh exact chart maps/generator images + universal polynomial circuit checks. Cramer identity is the standard polynomial determinant identity; huge minors need not be expanded.',
 'hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [raw,chart,main,boundary,selected,rankpath,driver,logfile]}}
(root/'t5_rank_chart_circuit.json').write_text(json.dumps(circuit,indent=2)+'\n')
