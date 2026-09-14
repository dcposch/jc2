#!/usr/bin/env python3
"""One worker/cwd-pinned build+replay or a separate guarded import-only exec."""
import hashlib,json,os,platform,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path('/home/ubuntu/d125-physical-export-pilot-20260906')
def need(ok,text):
    if not ok: raise RuntimeError(text)
def digest(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()
def save(name,obj):
    with (ROOT/name).open('x') as f:
        json.dump(obj,f,sort_keys=True,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def identity():
    need(platform.system()=='Linux' and platform.node()=='ip-172-30-0-56','wrong Linux hostname')
    need(Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2','not EC2')
    need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0da0cebfc97c9fd54','wrong instance')
    need(Path.cwd()==ROOT and ROOT.resolve()==ROOT,'wrong cwd/symlink')
    ready=json.loads((ROOT/'readiness.stdout').read_text())
    boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    need(boot==ready['boot_id'],'boot changed after registered audit')
    mount=subprocess.check_output(['findmnt','-T',str(ROOT),'-n','-o','SOURCE,FSTYPE,TARGET'],text=True).split()
    need(mount==['/dev/nvme0n1p1','ext4','/'],'task not on registered EBS filesystem')
    serial=subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip()
    need(serial=='vol0eb6450d18ffa89f1','wrong EBS serial')
    auth=json.loads((ROOT/'authority.json').read_text())
    need(digest(ROOT/'exporter.py')==auth['builder_sha256'],'builder hash drift')
    need(digest(ROOT/'run_capped.py')==auth['runner_sha256'],'runner hash drift')
    for filename,sha in auth['source_hashes'].items():need(digest(ROOT/filename)==sha,'source report drift')
    need(digest(ready['singular_path'])==ready['singular_sha256'],'Singular binary changed')
    raw=Path('/proc/self/stat').read_text();parts=raw[raw.rfind(')')+2:].split()
    return auth,ready,{'pid':os.getpid(),'ppid':os.getppid(),'pgid':os.getpgrp(),'start_ticks':parts[19],
            'boot_id':boot,'cwd':str(Path.cwd()),'cgroup':Path('/proc/self/cgroup').read_text(),
            'pid_namespace':os.readlink('/proc/self/ns/pid'),'argv':sys.argv,'utc':time.time()}

def main():
    start=time.monotonic();mode=sys.argv[1]
    need(mode in ('construct','import'),'unknown payload')
    auth,ready,ident=identity()
    save(mode+'.identity.json',ident)
    limit=auth['max_address_space_bytes'] if mode=='construct' else 16*1024**3
    resource.setrlimit(resource.RLIMIT_AS,(limit,limit))
    if mode=='construct':
        import exporter as e
        spec=e.production_spec('normalized')
        manifest=e.build(spec,ROOT/'complete',auth['max_output_bytes'],auth['max_wall_seconds'],True,auth)
        built=time.monotonic()
        print('CONSTRUCTION_COMPLETE',json.dumps(manifest,sort_keys=True),flush=True)
        footer=e.verify(ROOT/'complete/literal.jsonl',spec,auth)
        need(footer==manifest['footer'],'footer/manifest mismatch')
        for name,sha in manifest['files'].items():need(digest(ROOT/'complete'/name)==sha,'full-file digest mismatch')
        records,maps=e.variables(spec)
        unused=[records[i] for i in footer['unused_variable_ids']]
        result={'status':'COMPLETE_BUILD_AND_SELF_REPLAY','identity':ident,
                'construction_seconds':built-start,'combined_seconds':time.monotonic()-start,
                'authority_sha256':digest(ROOT/'authority.json'),'manifest':manifest,
                'manifest_sha256':digest(ROOT/'complete/manifest.json'),
                'file_bytes':{name:(ROOT/'complete'/name).stat().st_size for name in manifest['files']},
                'source_counts':{s:len(maps[s]) for s in ('P','Q')},'unused_variables':unused,
                'builder_header_license':'PROVISIONAL_UNLICENSED unchanged; authority records later promoted CHAR0-point gate',
                'verification_scope':'Exact same-formula complete stream self-replay, not independent certification'}
        need(result['combined_seconds']<600,'combined wall exceeded')
        save('construction.result.json',result)
        print('BUILD_AND_SELF_REPLAY_COMPLETE',json.dumps(result,sort_keys=True),flush=True)
    else:
        result=json.loads((ROOT/'construction.result.json').read_text())
        telemetry=json.loads((ROOT/'construct.telemetry.json').read_text())
        need(result['status']=='COMPLETE_BUILD_AND_SELF_REPLAY','construction incomplete')
        need(telemetry['status']=='NORMAL_EXIT' and telemetry['child_returncode']==0 and telemetry['error'] is None,'construction cap/failure')
        for name,sha in result['manifest']['files'].items():need(digest(ROOT/'complete'/name)==sha,'input drift before import')
        # Exact immutable generated import stream contains no solver command.
        os.execv(ready['singular_path'],[ready['singular_path'],'-q',str(ROOT/'complete/import.sing')])

if __name__=='__main__':main()
