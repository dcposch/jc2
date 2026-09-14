"""Read-only receipt-first terminal custody; no polynomial arithmetic."""
import datetime,hashlib,json,os,pathlib,shutil,subprocess
root=pathlib.Path('/home/ubuntu/d125-defect-order-solver-20260907')
boot=pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip()
if boot!='375d1a40-5988-4999-8cb7-a5427ad3b3a0' or pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()!='i-0da0cebfc97c9fd54':
    raise RuntimeError('host identity drift')
receipt=json.loads((root/'decision.result.json').read_bytes())
telemetry=json.loads((root/'decision.telemetry.json').read_bytes())
identity=json.loads((root/'decision.identity.json').read_bytes())
launch=json.loads((root/'decision.launch.json').read_bytes())
groups=sorted({identity['pgid'],launch['caller_pgid']})
lines=subprocess.check_output(['ps','-eo','pid=,pgid=,stat='],text=True).splitlines()
members=[line.strip() for line in lines if int(line.split()[1]) in groups]
if members:raise RuntimeError('not terminal: '+repr(members))
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()
files={}
for name in ('solver.authority.json','decision.launch.json','decision.identity.json','decision.sing',
             'decision.stdout','decision.stderr','decision.telemetry.json','decision.result.json'):
    path=root/name;files[name]={'bytes':path.stat().st_size,'sha256':sha(path)}
for suffix,pin in receipt['outputs'].items():
    if files['decision.'+suffix]['sha256']!=pin:raise RuntimeError('receipt output pin drift')
for suffix,pin in receipt['artifacts'].items():
    if files['decision.'+suffix]['sha256']!=pin:raise RuntimeError('receipt artifact pin drift')
source=pathlib.Path('/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational')
pins={str(source.with_suffix('.'+s)):sha(source.with_suffix('.'+s)) for s in ('jsonl','sing')}
pins.update({str(root/n):sha(root/n) for n in ('driver.py','exact.py','defect_order.py','run_capped.py')})
pins['/usr/bin/Singular']=sha(pathlib.Path('/usr/bin/Singular'))
ending=b';\nprint("D125_COMPLETE_LITERAL_IMPORT_ONLY");\nprint(size(I));\nquit;\n'
old=source.with_suffix('.sing').read_bytes()
if not old.endswith(ending):raise RuntimeError('original source ending drift')
old_prefix=old[:-len(ending)]+b';\n'
script=(root/'decision.sing').read_bytes()
prefix,separator,footer=script.partition(b'option(redSB); short=0;\n')
if not separator:raise RuntimeError('missing decision footer')
old_line,old_tail=old_prefix.split(b'\n',1);new_line,new_tail=prefix.split(b'\n',1)
if old_tail!=new_tail:raise RuntimeError('original ideal suffix changed')
new_ring_sha=hashlib.sha256(new_line+b'\n').hexdigest()
if new_ring_sha!='d894d6427d39b774c403165c83bffddbe993b96345ee00d652f5af7a06219bca':raise RuntimeError('wrong ring')
mem={k:int(v.split()[0]) for k,v in (line.split(':',1) for line in pathlib.Path('/proc/meminfo').read_text().splitlines())}
print(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'boot':boot,'root':str(root),
      'receipt':receipt,'telemetry':telemetry,'identity':identity,'launch':launch,'groups_absent':groups,
      'files':files,'pins_after':pins,'original_ideal_suffix_equal':True,'ideal_suffix_bytes':len(old_tail),
      'ideal_suffix_sha256':hashlib.sha256(old_tail).hexdigest(),'new_ring_sha256':new_ring_sha,
      'free_disk_bytes':shutil.disk_usage(root).free,'mem_available_kib':mem['MemAvailable'],
      'swap_total_kib':mem['SwapTotal'],'swap_free_kib':mem['SwapFree']},sort_keys=True))
