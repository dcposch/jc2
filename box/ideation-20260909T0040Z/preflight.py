"""Read-only packet checks. No invocation launches anything or writes authority."""
import argparse, datetime, hashlib, json, pathlib, re, subprocess
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260909T0040Z'
def require(ok,msg):
 if not ok: raise SystemExit('REFUSE: '+msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
a=argparse.ArgumentParser(); a.add_argument('--invitation-ready',action='store_true'); a.add_argument('--deadline-utc'); o=a.parse_args()
for p,h in json.loads((B/'PINS.json').read_text()).items(): require(sha(R/p)==h,'pin '+p)
m=json.loads((B/'MANIFEST.json').read_text()); expected=[e['path'] for e in m['entries']]+[str((B/'MANIFEST.json').relative_to(R))]
require(m['blind_target_utc'] is None and m['invitation_utc'] is None and m['launch_authorized'] is False,'prep scheduling drift')
require(len({pathlib.Path(p).name for p in expected})==len(expected),'duplicate basename')
require([int(x) for x in re.findall(r'^\| (\d+) \|',(B/'snapshots/master46-history.md').read_text(),re.M)]==list(range(1,47)),'full46')
require('BINDING OVERRIDE ROW26' in (B/'packet.md').read_text(),'missing binding override')
require("charged_inputs=$(sed -n 's/^charged_input=//p' \"$prompt_snapshot\")" in (R/'ops/lane.sh').read_text(),'launcher parser drift')
normalized=[]
for seat in ['coordinator','astra','fable5','sol56']:
 p=B/(seat+'.prompt.md'); s=p.read_text(); dest='xmodel/ideation-20260909T0040Z-'+seat+'.md'
 got=subprocess.run(['sed','-n','s/^charged_input=//p',str(p)],capture_output=True,text=True,check=True).stdout.splitlines()
 require(got==expected and '{{LANE_INPUTS}}' in s and s.count(dest)==1,'prompt '+seat)
 bad=s.replace('charged_input=','charged_input_1=')
 got_bad=subprocess.run(['sed','-n','s/^charged_input=//p'],input=bad,capture_output=True,text=True,check=True).stdout.splitlines()
 require(got_bad==[] and got_bad!=expected,'actual indexed-key corruption')
 normalized.append(s.replace(dest,'OUTPUT'))
require(len(set(normalized))==1,'unequal contract')
rootpins=None
if o.invitation_ready:
 require(o.deadline_utc is not None,'explicit fresh invitation deadline missing')
 try: deadline=datetime.datetime.fromisoformat(o.deadline_utc.replace('Z','+00:00'))
 except ValueError: raise SystemExit('REFUSE: invalid deadline')
 require(deadline.tzinfo is not None and deadline>datetime.datetime.now(datetime.timezone.utc),'deadline not future')
 report=R/'xmodel/ideation-20260909T0040Z-coordinator.md'
 require(report.is_file(),'root blind absent')
 r=subprocess.run(['python3','-I','-B',str(R/'ops/artifact_finalize.py'),'verify','--final',str(report)],capture_output=True,text=True)
 require(r.returncode==0,'root blind transaction')
 rootpins=dict(report_sha256=sha(report),transaction_sha256=sha(pathlib.Path(str(report)+'.artifact.json')))
elif o.deadline_utc is not None: raise SystemExit('REFUSE: deadline only at explicit invitation readiness')
print(json.dumps(dict(status='PASS',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),charged_inputs=len(expected),all46=True,equal_contract=True,indexed_key_corruption_rejected=True,root_blind_pins=rootpins,proposed_invitation_deadline=o.deadline_utc,launch_performed=False)))
