"""Compact terminal receipt/hash replay only; no source/system arithmetic."""
from pathlib import Path
import ast,hashlib,json
B=Path(__file__).resolve().parent;E=B/'production-evidence'
def need(ok,msg):
    if not ok:raise ValueError(msg)
def read(name):return json.loads((E/name).read_bytes())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
d=json.loads((B/'production-custody.json').read_bytes())
for name,v in d['files'].items():
    p=E/name;need(p.stat().st_size==v['bytes'] and sha(p)==v['sha256'],'copied file '+name)
t=read('pilot.telemetry.json');r=read('production.receipt.json');a=read('authority.json');l=read('production.launch.json');replay=read('replay-result.json');s=d['summary'];f=s['footer'];h=s['header']
need(d['ids_absent']==[1764,1765,1766] and d['groups_absent']==[1764,1766] and d['source_rows_replayed_again'] is False,'custody scope')
need(t['status']=='NORMAL_EXIT' and t['child_returncode']==t['runner_exit_code']==r['runner_rc']==0 and t['error'] is None,'terminal status')
need(r['runner_stderr']=='' and r['runner_absent'] is True and not r['group_members_after'] and not t['termination']['group_live_before_reap'],'terminal cleanup')
need(t['pid']==t['pgid']==l['payload']['pid']==l['payload']['pgid']==1766 and 'start_ticks=142914' in t['start_identity'],'payload identity')
need(a['root_green'] is True and a['construction_only'] is True and a['engineering_control_only'] is False and a['mode']=='normalized-hermite-only-slice','production authority')
need(a['boot_id']==d['boot']==l['payload']['boot']=='bef732b9-38e5-4a9a-8f93-77203426d2b8','boot')
need(a['root_green_sha256']==sha(E/'ROOT-GREEN.md')=='cdc48d29ec0037cceca2c75ab0712a40d49cf1004ec80b2a7ea513392d60567e','physical GREEN')
need(a['registration_sha256']==sha(E/'REGISTRATION.md')=='1ef0444a0778d13c2bf79fe1df51a82643478532716dd94434a04a412e0f12e6','registration')
need(l['authority_sha256']==h['authority_sha256']==sha(E/'authority.json'),'authority digest')
need(l['spawn_unix']<1788760260 and 0<l['remaining_at_spawn']<299.5 and l['expires_unix']==a['expires_unix'] and r['utc']<a['expires_unix'],'window/shared expiry')
need(a['caps']==dict(wall_seconds=300,cpu_seconds=300,address_bytes=4294967296,file_bytes=134217728,polynomial_terms=100000,multiply_pairs=1000000,retained_terms=1000000,coefficient_bits=4096),'payload caps')
need(t['caps']['wall_seconds']==t['caps']['cpu_seconds']==300 and t['caps']['rss_bytes']==4294967296 and t['caps']['rss_sample_seconds']==.05 and t['caps']['term_grace_seconds']==.25,'CAPRUN caps')
need(l['argv'][-7:]==['--','/usr/bin/python3','-E','-s','-B',str(Path(d['cwd'])/'construct.py'),str(Path(d['cwd'])/'authority.json')],'payload argv')
need(a['code_sha256']==r['post_pins'] and all(d['payload_pins'][k]==v for k,v in a['code_sha256'].items()),'payload code pins')
need(a['source_sha256']==d['source']['sha256']==r['source_post_sha256']==h['source_sha256']=='b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac','source pins')
need(sha(E/'engineering/rss.authority.json')=='d3a16840b13b51bb503c26416cab1fa79c316599acf1e0d4b9fb9ffb8e0e1f17' and sha(E/'engineering/ROOT-GREEN.md')=='12ef766b820b4ef486b4b3286eb0d46f2b41e5630488477f67170874cc2d8a36','retained spent files')
for stream in ('stdout','stderr'):
    need(t[stream]['bytes']==d['files']['pilot.'+stream]['bytes'] and t[stream]['sha256']==d['files']['pilot.'+stream]['sha256'],'telemetry stream pin')
need(replay==read('pilot.stdout') and replay['status']=='ALL_803_ORIGINAL_ROWS_COVER_TRANSPORTED','replay/stdout status')
need(f['complete'] is True and s['canonical_prefix_verified'] is True and len(h['variables'])==81 and len(h['original_variables'])==269 and h['field']=='Q' and h['order']=='dp' and h['target']=='J+5*k^3*g^2/9','stream scope')
need(all(replay[k]==f[k]==v for k,v in dict(rows=804,original_rows=803,terms=58684,zero_original_rows=578).items()),'complete counts')
need(s['row_groups']=={'FIX':{'rows':31,'nonzero':0,'terms':0,'max_degree':0},'J':{'rows':660,'nonzero':222,'terms':58676,'max_degree':3},'LIFT':{'rows':105,'nonzero':0,'terms':0,'max_degree':0},'GUARD':{'rows':7,'nonzero':3,'terms':6,'max_degree':6},'UNIT':{'rows':1,'nonzero':1,'terms':2,'max_degree':2}},'row census')
stages=[json.loads(line) for line in (E/'pilot.stderr').read_bytes().splitlines()]
need(all(x.get('type')=='stage' and 'error' not in x for x in stages),'unexpected stderr')
need([x['row'] for x in stages if x['stage']=='literal_cover_replay']==list(range(803)),'complete replay stage trace')
need(len([x for x in stages if x['stage']=='coefficient_cover'])==298,'coefficient cover trace')
need(d['construction']['sha256']==r['files']['construction.jsonl']['sha256']=='4ea526b2680ef41154332be3059ae5543c2678fdf8fb6a95d02176e8eb929272','construction pin')
need(d['construction']['bytes']==2244493 and d['ebs_serial']=='vol0eb6450d18ffa89f1','retained storage')
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'assert gate')
print(json.dumps(dict(status='PRODUCTION_COMPACT_REPLAY_PASS',copied_files=len(d['files']),original_rows=803,full_arithmetic=False,worker_access=False),sort_keys=True))
