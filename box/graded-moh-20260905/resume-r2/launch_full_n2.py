from pathlib import Path
import json,hashlib,subprocess,re
root=Path('/home/ubuntu/jc2/box/graded-moh-20260905');stem='C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6'
dag=json.loads((root/'resume-r2/triangular/77/triangular-dag-custody.json').read_text());a=json.loads((root/'instrument'/f'{stem}_audit.json').read_text());cust=json.loads((root/'instrument'/stem/'custody.json').read_text());old=root/'instrument'/stem/'homogeneous_ideal.sing'
piv=[d['pivot'] for d in dag['pivot_dag']];vv=list(reversed(piv))+[v for v in cust['source_ring']['variables'] if v not in piv]
txt=old.read_text();txt=re.sub(r'ring r=0,.*?;','ring r=0,('+','.join(vv)+'),wp('+','.join(str(a['positive_weights'][v]) for v in vv)+');',txt,count=1)
assert 'ideal I=' in txt and len(vv)==77
work=root/'runs'/'r2_77_full_n2_Q';work.mkdir(exist_ok=True);inp=work/'input.sing'
txt+='''\nprint("FULL_N2_READY field=Q variables=77 generators="+string(size(I))+" weight_bound=78 target_bidegree=4,78");
degBound=78;
ideal G=std(I);
poly target=c^2;
poly nf=reduce(target,G);
print("FULL_N2_STD_DONE basis="+string(size(G))+" c1_nonzero="+string(reduce(c,G)!=0)+" c2_zero="+string(nf==0));
write(":w nf_c2.txt",string(nf));
if(nf==0){
 degBound=0;
 matrix W=lift(I,ideal(target));
 matrix M[1][size(I)]=I;
 matrix C=M*W;
 print("FULL_N2_IDENTITY="+string(C[1,1]==target));
 write(":w witness.txt",string(W));
}
print("FULL_N2_DONE");
quit;
'''
inp.write_text(txt)
spec=dict(input=str(inp),work=str(work),command=['/usr/bin/Singular','--cpus=1','--threads=1','--flint-threads=1','-q','--no-rc',str(inp)],memory_gib=128,timeout_seconds=1200,kind='singular_weighted_std',chart=stem,field=0,order='wp(w), reverse triangular pivots then source free variable order',representation='FULL_original_direct_ideal_no_specialization_no_quotient',target='c^2',target_bidegree=[4,78],positive_weight_bound=78,worker='i-02aaa996f54d2c004',ip='172.30.0.86',source_script=str(old),source_script_sha256=hashlib.sha256(old.read_bytes()).hexdigest(),source_rows_sha256=cust['source_rows_sha256'],variables=vv,positive_weights=[a['positive_weights'][v] for v in vv],original_generator_count=150)
p=work/'spec.json';p.write_text(json.dumps(spec,indent=2)+'\n');subprocess.run(['python3',str(root/'ops/dispatch_lane.py'),'launch',spec['ip'],str(p)],check=True)
