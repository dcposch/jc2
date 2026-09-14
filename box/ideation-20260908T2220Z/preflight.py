"""Read-only checks; this program cannot launch an invitation."""
import argparse, hashlib, json, pathlib, re, subprocess
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260908T2220Z'
def require(ok,msg):
 if not ok: raise SystemExit('REFUSE: '+msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
a=argparse.ArgumentParser(); a.add_argument('--invitation-ready',action='store_true'); opts=a.parse_args()
pins=json.loads((B/'PINS.json').read_text())
for p,h in pins.items(): require(sha(R/p)==h,'pin '+p)
m=json.loads((B/'MANIFEST.json').read_text()); expected=[e['path'] for e in m['entries']]+[str((B/'MANIFEST.json').relative_to(R))]
require(len({pathlib.Path(p).name for p in expected})==len(expected),'nonunique basenames')
require([int(x) for x in re.findall(r'^\| (\d+) \|',(B/'snapshots/master46-history.md').read_text(),re.M)]==list(range(1,47)),'full46 missing')
require("charged_inputs=$(sed -n 's/^charged_input=//p' \"$prompt_snapshot\")" in (R/'ops/lane.sh').read_text(),'actual launcher parser drift')
norm=[]
for seat in ['coordinator','astra','fable5','sol56']:
 p=B/(seat+'.prompt.md'); s=p.read_text()
 got=subprocess.run(['sed','-n','s/^charged_input=//p',str(p)],capture_output=True,text=True,check=True).stdout.splitlines()
 require(got==expected,'actual sed vector '+seat)
 require('{{LANE_INPUTS}}' in s and 'charged_input_1=' not in s,'contract framing')
 dest='xmodel/ideation-20260908T2220Z-'+seat+'.md'
 require(s.count(dest)==1,'one destination')
 norm.append(s.replace(dest,'OUTPUT'))
 bad=s.replace('charged_input=','charged_input_1=')
 parsed=subprocess.run(['sed','-n','s/^charged_input=//p'],input=bad,capture_output=True,text=True,check=True).stdout.splitlines()
 require(parsed!=expected and parsed==[],'indexed-key negative control')
require(len(set(norm))==1,'asymmetric contracts')
if opts.invitation_ready:
 report=R/'xmodel/ideation-20260908T2220Z-coordinator.md'
 require(report.is_file(),'root blind absent; invitations forbidden')
 t=subprocess.run(['python3','-I','-B',str(R/'ops/artifact_finalize.py'),'verify','--final',str(report)],capture_output=True,text=True)
 require(t.returncode==0,'root blind transaction invalid')
 require('<!-- BODY-END -->' in report.read_text(),'root blind incomplete')
print(json.dumps(dict(status='PASS',charged_inputs=len(expected),all46=True,equal_contracts=True,indexed_keys_rejected=True,root_blind_verified=opts.invitation_ready,launch_performed=False)))
