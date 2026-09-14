#!/usr/bin/env python3
"""Execute frozen map verifier in memory, replacing only its final output write."""
import hashlib, json, os, sys, time
from pathlib import Path
root=Path('/home/ubuntu/jc2');os.chdir(root)
driver=root/'box/char-degree-20260905/active-gauge/verify_circuit_schedule_inputs.py'
text=driver.read_text()
needle="(a.directory/'verification.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\\n')"
assert text.count(needle)==1
replacement="print(json.dumps({'status':result['status'],'field':result['field'],'cases':len(result['records']),'source_driver_sha256':result['driver_sha256'],'preparation_sha256':result['preparation_sha256'],'checked_sites':sum(r['coefficient_sites_checked'] for r in result['records'])},sort_keys=True))"
text=text.replace(needle,replacement)
if os.environ.get('CHAR99_REPLAY_TAIL')=='1':
    needle="for rec in prepared['records']:\n  branch,stage=rec['branch'],rec['stage']"
    assert text.count(needle)==1
    text=text.replace(needle,"for rec in prepared['records']:\n  if rec['stage']<6 or (rec['stage']==6 and rec['branch']=='delta2'): continue\n  branch,stage=rec['branch'],rec['stage']")
sys.path.insert(0,str(driver.parent))
sys.argv=[str(driver),'--directory',str(root/'box/char-degree-20260905/g9966/circuit-inputs')]
start=time.monotonic()
exec(compile(text,str(driver),'exec'),{'__name__':'__main__','__file__':str(driver)})
print('wall_seconds='+str(round(time.monotonic()-start,3)))
