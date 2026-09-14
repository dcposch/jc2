from pathlib import Path
import json,random,hashlib
BASE=Path('/home/ubuntu/jc2/box/graded-moh-20260905')
src=BASE/'truncation/C_n24m18_Mm15_14_ell1_s3_V1_9_N1'
m=json.loads((src/'manifest.json').read_text());X,Y=m['target_bidegree'];W=m['weights'];zero=[v for v in m['variables'] if W[v][0]==0];pos=[v for v in m['variables'] if W[v][0]>0];L=Y+1;B=[W[v][0] for v in pos];combined=[W[v][1]+L*W[v][0] for v in pos]+[1]
out=BASE/'resume-r2/truncation'/src.name/'curve-specialization';out.mkdir(parents=True,exist_ok=True)
assignments=[dict.fromkeys(zero,1),{v:int(v.startswith('h_')) for v in zero},{v:int(v.startswith('A1_')) for v in zero}]
rng=random.Random(20260905129)
assignments += [{v:rng.choice([-1,0,1]) for v in zero} for j in range(5)]
s=(src/'input.sing').read_text();s+='\nring S=0,('+','.join(pos+['curve_t'])+'),wp('+','.join(map(str,combined))+');\nintvec CW='+','.join(map(str,combined))+';\nint i,j,good;\npoly lc,sp,nf;\nideal J,G;\noption(redSB);\n'
for a,assignment in enumerate(assignments):
 images=','.join((str(assignment[v])+'*curve_t^'+str(W[v][1])) if v in assignment else v for v in m['variables'])
 s+=f'\nmap phi{a}=R,{images};\nJ=phi{a}(I);\ndegBound={Y+L*X};\nprint("ASSIGNMENT_START={a}");\nG=std(J);\nattrib(G,"isSB",1);\nnf=reduce(c,G);\n'
 s+='good=1;\nfor(i=1;i<=size(J);i++){if(reduce(J[i],G)!=0){good=0;}}\n'
 s+='for(i=1;i<=size(G);i++){for(j=i+1;j<=size(G);j++){lc=lcm(leadmonom(G[i]),leadmonom(G[j]));if(deg(lc,CW)<='+str(Y+L*X)+'){sp=(lc/leadmonom(G[i]))*G[i]/leadcoef(G[i])-(lc/leadmonom(G[j]))*G[j]/leadcoef(G[j]);if(reduce(sp,G)!=0){good=0;}}}}\n'
 s+=f'print("ASSIGNMENT={a} C_NF_NONZERO="+string(nf!=0)+" NF_TERMS="+string(size(nf))+" INPUT_AND_TRUNCATED_SPAIRS_ZERO="+string(good)+" BASIS_SIZE="+string(size(G)));\n'
 s+=f'write(":w {out}/basis-{a}.txt",string(G));\nwrite(":w {out}/normalform-{a}.txt",string(nf));\n'
s+='print("DONE");quit;\n'
(out/'curve-specialization.sing').write_text(s)
spec=dict(ip='172.30.0.86',worker='i-02aaa996f54d2c004',work=str(out),input=str(out/'curve-specialization.sing'),command=['/usr/bin/Singular','-q',str(out/'curve-specialization.sing')],memory_gib=90,timeout_seconds=900)
(out/'spec.json').write_text(json.dumps(spec,indent=2)+'\n')
(out/'custody.json').write_text(json.dumps(dict(original_source_input=str(src/'input.sing'),original_source_input_sha256=hashlib.sha256((src/'input.sing').read_bytes()).hexdigest(),input_sha256=hashlib.sha256(s.encode()).hexdigest(),variables=pos+['curve_t'],weights=combined,combined_degree_bound=Y+L*X,target_bidegree=[X,Y],L=L,source_original_variable_order=m['variables'],assignments=assignments,coefficient_field='Q',completion_requirement='All mapped inputs and all basis S-pairs of combined degree <= cutoff reduce to zero; c normal form nonzero. Any passing candidate proves c not in I, not radical nonmembership.',ring_map='Each B=0 variable v maps to listed rational constant times curve_t^w(v); each positive B variable maps to itself. curve_t has bidegree (0,1).'),indent=2)+'\n')
print(out)
