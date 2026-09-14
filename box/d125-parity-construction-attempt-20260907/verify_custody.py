"""Tiny captured terminal-custody check, not a row or construction replay."""
import hashlib,json,resource
from pathlib import Path
H=Path(__file__).resolve().parent;E=H/'evidence'
resource.setrlimit(resource.RLIMIT_CPU,(5,5));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
def need(ok,msg):
    if not ok:raise ValueError(msg)
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=read(H/'terminal-custody.json');t=read(E/'pilot.telemetry.json');launch=read(E/'pilot.launch.json')
need(c['status']=='INCONCLUSIVE' and c['remaining']==[] and c['extra_reconstruction_or_replay'] is False,'outcome/group custody')
for name,item in c['files'].items():
    p=E/name;need(p.stat().st_size==item['bytes'] and sha(p)==item['sha256'],'copy hash '+name)
need(t==c['telemetry'] and t['status']=='NORMAL_EXIT' and t['child_returncode']==1 and t['runner_exit_code']==1,'terminal status')
need(t['resource'] is None and t['wall_elapsed_seconds']<300 and t['max_observed_group_rss_bytes']<4294967296,'external caps')
a=read(E/'authority.json');payload=read(E/'pilot.payload-identity.json')['payload']
need(a['schema']=='jc2.d125-parity-construction-authority/v1' and a['mode']=='slice' and a['caps']['polynomial_terms']==100000,'registered source/cap')
need(sha(E/'authority.json')==launch['authority_sha256']==c['terminal']['authority_sha256'],'authority pin')
need(a['expires_unix']==launch['expires_unix'] and launch['expires_unix']-launch['dispatch_unix']==300,'shared deadline')
need(t['pid']==t['pgid']==payload['pid']==payload['pgid'],'payload identity')
need(t['start_identity']=='boot='+payload['boot']+';start_ticks='+payload['start_ticks'],'payload start')
need(sha(E/'REGISTRATION.md')==a['registration_sha256'],'registration')
need(all(item['sha256']==a['code_sha256'][name] for name,item in c['post_code'].items()),'code postpins')
need(c['source_posthash']['sha256']==a['source_sha256'],'source postpin')
failure=json.loads((E/'pilot.stderr').read_bytes().splitlines()[0])
need(failure['status']=='INCOMPLETE' and failure['error']=='polynomial term cap','typed internal stop')
need((E/'construction.jsonl').stat().st_size==(E/'replay-result.json').stat().st_size==0,'partial size')
print(json.dumps(dict(status='TERMINAL_CUSTODY_PASS',optimized=not __debug__,files=len(c['files']),
                      outcome='INCONCLUSIVE',failure=failure,extra_full_arithmetic=False),sort_keys=True))
