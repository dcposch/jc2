from pathlib import Path
import json,hashlib,sys
BASE=Path('/home/ubuntu/jc2/box/graded-moh-20260905')
for src in sorted((BASE/'truncation').glob('*_N1')):
 m=json.loads((src/'manifest.json').read_text());out=BASE/'resume-r2/truncation'/src.name;out.mkdir(parents=True,exist_ok=True)
 # Start with original selected rows, so this witness needs no elimination replay.
 data=(src/'input.sing').read_text()
 zero=[v for v in m['variables'] if m['weights'][v][0]==0]
 s=data+'\nideal Z='+','.join(zero)+';\nideal J=I+Z;\noption(redSB);option(prot);\nideal G=std(J);\noption(noprot);\npoly nf=reduce(c,G);\nprint("FULL_STD_COMPLETE=1");\nprint("C_NF_NONZERO="+string(nf!=0));\nprint("BASIS_SIZE="+string(size(G)));\nprint("NF_TERMS="+string(size(nf)));\n'
 s+='write(":w '+str(out/'specialized-basis.txt')+'",string(G));\nwrite(":w '+str(out/'specialized-normalform.txt')+'",string(nf));\nprint("DONE");quit;\n'
 # no overflow first: if specialization is feasible original c nonmembership rigorous.
 (out/'zero-specialization.sing').write_text(s)
 spec=dict(ip='172.30.0.86',worker='i-02aaa996f54d2c004',work=str(out),input=str(out/'zero-specialization.sing'),command=['/usr/bin/Singular','-q',str(out/'zero-specialization.sing')],memory_gib=100,timeout_seconds=300)
 (out/'spec.json').write_text(json.dumps(spec,indent=2)+'\n')
 (out/'specialization-custody.json').write_text(json.dumps(dict(source_manifest=str(src/'manifest.json'),source_input_sha256=hashlib.sha256((src/'input.sing').read_bytes()).hexdigest(),specialized_to_zero=zero,coefficient_field='Q',ring_map='Each listed B=0 variable maps to zero, all others to themselves. Native selected rows retained in original order. Nonzero c normal form proves nonmembership in selected ideal; bigrading identifies target component with full ideal.',input_sha256=hashlib.sha256(s.encode()).hexdigest()),indent=2)+'\n')
 print(out)
