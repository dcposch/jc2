"""Read-only terminal custody of this exact fresh engineering directory."""
import datetime, hashlib, json, os, pathlib, platform, shutil, subprocess
root=pathlib.Path('/home/ubuntu/d125-defect-order-solver-20260907')
boot=pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip()
instance=pathlib.Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()
if (instance,boot)!=('i-0da0cebfc97c9fd54','375d1a40-5988-4999-8cb7-a5427ad3b3a0'):
    raise RuntimeError('custody identity drift')
batch=json.loads((root/'engineering/batch.result.json').read_bytes())
controller=json.loads((root/'engineering/controller.identity.json').read_bytes())
descendant=json.loads((root/'engineering/rss-descendant.identity.json').read_bytes())
groups=sorted({j['telemetry']['pgid'] for j in batch['jobs']}|{controller['pgid']})
lines=subprocess.check_output(['ps','-eo','pid=,pgid=,stat='],text=True).splitlines()
members=[line.strip() for line in lines if int(line.split()[1]) in groups]
if members:raise RuntimeError('owned groups not absent: '+repr(members))
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for data in iter(lambda:f.read(1024*1024),b''):h.update(data)
    return h.hexdigest()
files={str(p.relative_to(root)):{'bytes':p.stat().st_size,'sha256':sha(p)}
       for p in sorted(root.rglob('*')) if p.is_file()}
source=pathlib.Path('/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational')
sources={suffix:sha(source.with_suffix('.'+suffix)) for suffix in ('jsonl','sing')}
if sources!={'jsonl':'b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac',
             'sing':'c089c33301e3889e0c20527386719f411907cf2957ecfad3d93c65f7be24e718'}:
    raise RuntimeError('source-after pin drift')
mem={k:int(v.split()[0]) for k,v in (line.split(':',1) for line in pathlib.Path('/proc/meminfo').read_text().splitlines())}
print(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'instance':instance,'boot':boot,
      'root':str(root),'serial':subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip(),
      'mount':subprocess.check_output(['findmnt','-n','-o','SOURCE,FSTYPE,TARGET','-T',str(root)],text=True).strip(),
      'groups_absent':groups,'controller':controller,'descendant':descendant,'batch_status':batch['status'],
      'source_after':sources,'files':files,'file_count':len(files),'total_bytes':sum(f['bytes'] for f in files.values()),
      'disk_free_bytes':shutil.disk_usage(root).free,'mem_available_kib':mem['MemAvailable'],
      'swap_total_kib':mem['SwapTotal'],'swap_free_kib':mem['SwapFree'],'no_instance_action':True},sort_keys=True))
