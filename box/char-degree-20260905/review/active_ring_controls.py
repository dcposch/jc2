#!/usr/bin/env python3
"""Injective ring extension and original-backend equivalence controls."""
from pathlib import Path
import hashlib,json,subprocess
from active_ring_backend import active_normalized_script
from normalized_backend import normalized_script

HERE=Path(__file__).resolve().parent
names=sorted(['target_a','target_b','target_c','target_d','target_e','leader3','Z3','c','Zc','unused'])
common={'D_expr':'tt^2*(1+zz)','C_expr':'(3/8)*tt^5','residual_strings':['target_a','target_b','target_c','target_d','target_e','c-1'],
        'names':names,'k':2,'target':3,'face_expr':'1+zz'}
records=[]
for tag,hexpr,defs,unit in [('attained','(1+zz)^2',[],False),
                            ('tower_definition','baseH^2',[('baseH','1+zz')],False),
                            ('vertex','(1+zz)^2',[],True)]:
    kwargs=dict(common,h_expr=hexpr)
    if tag=='vertex':kwargs.update(D_expr='0',C_expr='0')
    active,metadata=active_normalized_script(**kwargs,predefinitions=defs)
    original=normalized_script(**kwargs)
    if defs:
        token='print("BEGIN_BUILD_NORMALIZED");'
        original=original.replace(token,token+'\n'+'\n'.join(f'poly {n}={p};' for n,p in defs))
    outcomes=[]
    for mode,script in [('active',active),('original',original)]:
        path=HERE/f'active_control_{tag}_{mode}.sing';path.write_text(script)
        run=subprocess.run(['Singular','-q',str(path)],capture_output=True,text=True,timeout=60)
        output=run.stdout+run.stderr;path.with_suffix('.out').write_text(output)
        assert run.returncode==0 and not any(l.lstrip().startswith('?') for l in output.splitlines()),output
        result=output.split('BEGIN_RESULT\n',1)[1].split('\nEND_RESULT',1)[0].splitlines()
        assert (result[0]=='0')==unit,result
        if mode=='active':assert 'END_EMBED_FULL_RING' in output
        outcomes.append(result)
    assert outcomes[0]==outcomes[1],outcomes
    records.append({'tag':tag,'unit':unit,'same_full_ring_result':outcomes[0],
                    'active_generators':len(metadata['active_generator_order']),
                    'full_generators':len(metadata['full_generator_order']),
                    'all_generator_and_source_image_checks_passed':True,
                    'script_sha256':metadata['script_sha256']})

# A wrong image is detected mechanically before any interpreted outcome.
corrupt=active.replace('injectedGenerators[1]-zz','injectedGenerators[1]-tt',1)
run=subprocess.run(['Singular','-q'],input=corrupt,capture_output=True,text=True,timeout=60)
assert 'generator image 0 failed' in run.stdout
(HERE/'active_generator_map_negative.out').write_text(run.stdout+run.stderr)
record={'field':'Q','controls':records,'wrong_generator_image_rejected':True,
        'driver_sha256':hashlib.sha256((HERE/'active_ring_backend.py').read_bytes()).hexdigest()}
(HERE/'active-ring-controls.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
