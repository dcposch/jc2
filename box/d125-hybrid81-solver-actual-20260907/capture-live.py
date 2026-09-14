"""Read-only exact live decision identity; no source/stdout reads or signals."""
from pathlib import Path
import hashlib,json,os
W=Path('/home/ubuntu/d125-hybrid81-exact-solver-20260907');BOOT='886172be-22d4-42e8-939c-0fc0475346fa'
def need(c,m):
 if not c:raise RuntimeError(m)
def ident(pid):
 p=Path('/proc')/str(pid);s=(p/'stat').read_text().rsplit(') ',1)[1].split()
 return {'pid':pid,'ppid':int(s[1]),'pgid':int(s[2]),'start_ticks':s[19],'argv':[x.decode() for x in (p/'cmdline').read_bytes().split(b'\0')[:-1]],'namespace':os.readlink(p/'ns/pid'),'cgroup':(p/'cgroup').read_text(),'limits':(p/'limits').read_text(),'exe':os.readlink(p/'exe')}
need(Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0da0cebfc97c9fd54','host')
need(Path('/proc/sys/kernel/random/boot_id').read_text().strip()==BOOT,'boot')
i=json.loads((W/'decision.identity.json').read_bytes());l=json.loads((W/'decision.launch.json').read_bytes())
p=ident(i['pid']);runner=ident(p['ppid']);caller=ident(l['caller_pid'])
need(i['phase']=='decision' and i['host']['boot']==BOOT and p['pid']==p['pgid']==i['pgid'] and p['start_ticks']==i['start_ticks'],'payload pin')
need(runner['argv']==l['command'] and runner['ppid']==caller['pid'],'actual registered parent vector')
need(hashlib.sha256((W/'solver.authority.json').read_bytes()).hexdigest()==i['authority_sha256']==l['authority_sha256'],'authority')
print(json.dumps({'scope':'LIVE_METADATA_ONLY','boot':BOOT,'identity':i,'launch':l,'caller':caller,'runner':runner,'payload':p},sort_keys=True))
