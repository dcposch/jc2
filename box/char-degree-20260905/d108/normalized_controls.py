#!/usr/bin/env python3
import hashlib,json,subprocess
from pathlib import Path
from normalized_backend import normalized_script
OUT=Path(__file__).resolve().parent
names=sorted(['target_a','target_b','target_c','target_d','target_e','leader63','Z63','c','Zc'])
cases=[('vertex_unit','zz^36+tt^9*zz^27+tt^35','0','0',36,63,'zz^21*(1+zz)^6',True),
       ('attained_nonunit','zz^2','tt^2*zz','(3/8)*tt^5',2,3,'zz',False)]
records=[]
for tag,h,D,C,k,d,face,unit in cases:
    rows=['target_a','target_b','target_c','target_d','target_e','c-1']
    text=normalized_script(h,D,C,rows,names,k,d,face,leader_name='leader63',leader_inverse='Z63')
    path=OUT/f'normalized_control_{tag}.sing';path.write_text(text)
    proc=subprocess.run(['Singular','-q',str(path)],text=True,capture_output=True,timeout=60)
    log=proc.stdout+proc.stderr;(OUT/f'normalized_control_{tag}.out').write_text(log)
    errors=[s for s in log.splitlines() if s.lstrip().startswith('?') or 'error occurred' in s]
    assert not errors,errors
    section=log.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].splitlines()
    assert (section[0]=='0')==unit,log
    controls=log.split('BEGIN_CONTROLS\n',1)[1].split('\nEND_CONTROLS',1)[0].splitlines()
    assert controls==['0','1'],controls
    records.append({'tag':tag,'expected_unit':unit,'reduce_one':section[0],'controls':controls,
                    'script_sha256':hashlib.sha256(text.encode()).hexdigest(),'passed':True})
(OUT/'normalized-controls.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
