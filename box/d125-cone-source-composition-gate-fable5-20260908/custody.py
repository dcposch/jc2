#!/usr/bin/python3
"""Final custody writer for the Fable 5.1 cone source-composition gate. Hashes the report and every owned box file; runs last."""
import sys
sys.dont_write_bytecode=True
import hashlib,json,os,datetime
BOX=os.path.dirname(os.path.abspath(__file__))
REPORT='/home/ubuntu/jc2/xmodel/d125-cone-source-composition-gate-fable5-20260908.md'
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
b=open(REPORT,'rb').read(); end=b'<!-- BODY-END -->\n'; i=b.index(end)+len(end)
assert_free=True
entries=[]
for f in sorted(os.listdir(BOX)):
    if f=='custody.json': continue
    p=os.path.join(BOX,f); entries.append({'path':'box/d125-cone-source-composition-gate-fable5-20260908/'+f,'bytes':os.path.getsize(p),'sha256':sha(p)})
entries.append({'path':'xmodel/d125-cone-source-composition-gate-fable5-20260908.md','bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
                'body_bytes':i,'body_sha256':hashlib.sha256(b[:i]).hexdigest(),'body_end_line_unique':b.count(end)==1,'charge_basis_lines':b.count(b'charge_basis'),'seal_section':b'## Seal' in b})
pins={l.split()[1]:l.split()[0] for l in open(os.path.join(BOX,'inputs-sha256.txt'))}
out={'schema':'fable5-gate-custody-v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'owner':'fable5 cone source-composition gate','frozen_basis':'0d39df3c9fd69c939a8420c54d03228b9077777d',
     'verdicts':{'1_exact_source_scope':'CONFIRMED','2_dilation_references':'CONFIRMED','3_first_contact_kernel':'CONFIRMED','4_product_ring_initials':'CONFIRMED','5_B_initials_35':'CONFIRMED','6_composition':'CONFIRMED at stated scope only'},
     'charged_input_pins':pins,'owned':entries,'replays':28,'controls':'fable5_controls.py C1-C9, C8 sampled illustration only','exceptions':['reviewer C4 draft list-order comparison corrected to set comparison; no charged object failed'],
     'no_launch':True,'no_cas_aws_agents':True,'writers':'ALL FINISHED after this file','status':'TERMINAL'}
json.dump(out,open(os.path.join(BOX,'custody.json'),'w'),indent=1,sort_keys=True)
print(json.dumps({k:v for k,v in out.items() if k in ('verdicts','replays','status')},sort_keys=True))
