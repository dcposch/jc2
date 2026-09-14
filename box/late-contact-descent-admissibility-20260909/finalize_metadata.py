"""Metadata/publication only: no mathematical execution or source expansion."""
import datetime, hashlib, json, pathlib, subprocess
ROOT = pathlib.Path('/home/ubuntu/jc2')
OWN = ROOT / 'box/late-contact-descent-admissibility-20260909'
FINAL = 'xmodel/late-contact-descent-admissibility-astra-20260909.md'
TOKEN = 'b46e0f962b5fbe74e2449a21eb8be770a43ca1bda7e563befc1bd138ded00edb'
SOURCES = [
 ('xmodel/source-multiplicity-admissibility-astra-20260909.md', '909ba868b027834a31c6eda37546f17694478cad93d35233d047f1321c0875c0', 'WHOLE after current custody checks'),
 ('xmodel/source-multiplicity-admissibility-astra-20260909.md.artifact.json', '9761dcd855b58153cb2ed50bb73c23459f96ea85ccad2b616880dd0fd07a2520', 'WHOLE metadata before body'),
 ('box/source-multiplicity-admissibility-20260909/custody.json', '3fe496680cafeb7fd35bc148848d0489f091d780cd125f063aac028395e79a93', 'WHOLE metadata before body; all34 current checks retained'),
 ('box/source-multiplicity-admissibility-20260909/source-record.md', '8920d43c1d3e08b71e5d9ada27b8a8b382d820f3110b9fa0f02cd4b9192af17f', 'WHOLE source/access record'),
 ('box/source-multiplicity-admissibility-20260909/mw-web-response.json', 'cce23548508ee5e036fb097b6b7795f1c1ba3bf0c75f08dbb8f38f79ec6617e5', 'WHOLE primary article extracted text; OCR caveat; not PDF-byte custody'),
 ('box/source-multiplicity-admissibility-20260909/ggv-v3.pdf', '8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60', 'Opaque hash of retained exact primary PDF; reading via corresponding layout'),
 ('box/source-multiplicity-admissibility-20260909/ggv-v3.txt', 'e3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1', 'Introduction/B definition;3.1-3.10 excerpts;4.1-4.3;4.7 proof partial;5.19-5.21;6.5/6.6 whole;7.9 whole;7.13 statement/partial proof;8.11/8.12/8.13'),
 ('box/source-multiplicity-admissibility-20260909/moh.txt', 'f203d7892753011ac21e8f01d29d73f5d777cad36310d2c16aa49d4a335072a0', 'Printed142-143 introduction;198-200 Prop6.4/Cor6.1 and surrounding text; no full AppendixII replay'),
 ('xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md', '7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413', 'WHOLE'),
 ('xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md', '433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad', 'WHOLE'),
 ('xmodel/d125-client-interface-astra-20260906.md', '0c5270a432a6336c17c4693034e36cb496f139c3267843e3ac06628ec8c4b255', 'WHOLE'),
 ('xmodel/k16-boundary-product-astra-20260906.md', '1c4a1100cc774932f23da27e11bf828a6fa10d5e256ce1528694d356d9031d9c', 'Scoped keyword metadata/excerpts only; no new mathematical premise'),
 ('xmodel/d125-weightfree-client-interface-astra-20260909.md', 'dcb3a30a48c5977005083a3ad7bbc5935e1f2f74ade6c3569a4b45751c213276', 'Scoped keyword excerpts only; pending weightfree proof not read or consumed'),
 ('xmodel/late-contact-keller-descent-astra-20260909.md', '857b2e2fa93cc14acb24fa590a2ffa76961a0d136113908f12b213e126889672', 'Own sealed full proof known; PROVISIONAL conditional consumer only'),
 ('xmodel/late-contact-keller-descent-astra-20260909.md.artifact.json', 'e922c1a601d9692f1cd21eb20b319e3eb5a5c7dcdb14d0632ecb8ef9a034b37e', 'Hash binding to unchanged original provisional proof'),
]
def pin(p):
    b = p.read_bytes()
    return {'path': str(p.relative_to(ROOT)), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
def write(name, obj):
    with (OWN/name).open('x') as f:
        json.dump(obj, f, indent=2)
        f.write('\n')
rows = []
for name, sha, scope in SOURCES:
    row = pin(ROOT/name)
    if row['sha256'] != sha:
        raise SystemExit('INPUT DRIFT: '+name)
    row['read_scope'] = scope
    rows.append(row)
write('input-pins.json', {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'entries': rows,
                        'primary_urls': ['https://arxiv.org/pdf/1401.1784v3', 'https://www.researchgate.net/profile/Stuart-Wang/publication/243064554_A_Note_on_the_Jacobian_Condition_and_Two_Points_at_Infinity/links/55b5379008ae9289a08a68ce/A-Note-on-the-Jacobian-Condition-and-Two-Points-at-Infinity.pdf'],
                        'queries': ['"Jacobian" "3D" "5D" remainder', '"Jacobian" "late contact" descent', '"Jacobian" "remainder" "smaller" Keller pair', '"Jacobian" "7D/3"', '"Jacobian conjecture" "reduction of degree" Moh', '"Jacobian conjecture" "remainder" "Keller"', '"Jacobian conjecture" "3:5" descent', '"Jacobian conjecture" "late contact"'],
                        'query_result': 'NO_EXACT_HIT; no novelty inference; no result snippet used as mathematical premise',
                        'mathematical_subprocesses': 0})
outcomes=[]
for op in ('close','finalize','verify'):
    argv=['python3','-I','-B','ops/artifact_finalize.py',op,'--final',FINAL]
    if op!='verify': argv += ['--token',TOKEN]
    r=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True,timeout=30)
    outcomes.append({'argv':argv,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
    if r.returncode:
        write('publication-failure.json',outcomes)
        raise SystemExit('publication failure')
for row in rows:
    if pin(ROOT/row['path'])['sha256'] != row['sha256']:
        raise SystemExit('POST INPUT DRIFT: '+row['path'])
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
write('publication.json',{'terminal_utc':utc,'outcomes':outcomes,'post_inputs':'UNCHANGED'})
owned=[p for p in OWN.iterdir() if p.is_file()]+[ROOT/FINAL,ROOT/(FINAL+'.artifact.json')]
write('custody.json',{'terminal_utc':utc,'status':'SOURCE_ADMISSIBILITY_NO_ATTACHED_CLIENT_IN_NAMED_SCOPE',
                     'entries':[pin(p) for p in owned],'inputs':rows,'writers':'IDLE','children':[],
                     'mathematical_subprocesses':0,'no_proof_extension':True,'no_launch':True})
for p in owned+[OWN/'custody.json']: p.chmod(0o444)
print(json.dumps({'terminal_utc':utc,'report':pin(ROOT/FINAL),'transaction':pin(ROOT/(FINAL+'.artifact.json')),
                  'custody':pin(OWN/'custody.json'),'input_pins':pin(OWN/'input-pins.json'),
                  'publication':pin(OWN/'publication.json'),'owned_entries':len(owned),'writers':'IDLE'}))
