#!/usr/bin/env python3
"""Byte-preserving export of an unchanged exact checker; exclusive outputs only."""
import copy
from fractions import Fraction
import hashlib
import json
from math import gcd, factorial
from pathlib import Path
import subprocess
import sys
import os

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'box/d125-minimal-receiver-b-reconstruction-20260906/check.py'
OLD=ROOT/'box/d125-minimal-receiver-b-reconstruction-20260906/exact-witnesses.json'
OUT=Path(__file__).resolve().parent/'exact-witnesses-v2.json'
RECEIPT=Path(__file__).resolve().parent/'repair-receipt.json'
SOURCE_SHA='5a3cc2853c04b74faa7b256122a445c5435412c905966fd55ebfc2965e8c67d5'
OLD_SHA='9551e7205d6918e5bf913b70b1ea9e5921b8e8eadeb2d9591b610a78cdc24f77'
RUNTIME_SHA='07b4ce881b4f90f9a41a3f8cb01fcd3a120ff64a4f04969e60126dbdb6e7f246'
def req(ok,why):
    if not ok: raise ValueError(why)
def sha(b): return hashlib.sha256(b).hexdigest()
def forbid_float(s): raise ValueError('floating JSON numeral rejected: '+s)
def rational(pair):
    req(type(pair)==list and len(pair)==2,'rational pair shape')
    n,d=pair
    req(type(n)==int and type(d)==int,'rational pair must contain exact integer types')
    req(d>0 and gcd(n,d)==1,'canonical reduced rational required')
    return Fraction(n,d)
def field(pair):
    req(type(pair)==list and len(pair)==2,'field-pair shape')
    return tuple(rational(v) for v in pair)
def no_floats(obj):
    if isinstance(obj,float): raise ValueError('float object rejected')
    if isinstance(obj,dict):
        for v in obj.values(): no_floats(v)
    if isinstance(obj,list):
        for v in obj: no_floats(v)
def validate(data):
    no_floats(data)
    req(data.get('status')=='PASS','checker status')
    req(set(data['witnesses'])=={'unequal','common3','common4'},'case coverage')
    count=0; kernels=0
    for case,branches in data['witnesses'].items():
        req(set(branches)=={'rational','golden'},'field coverage')
        for branch,ws in branches.items():
            req(len(ws)==24,'degree coverage')
            for d,w in enumerate(ws,1):
                req(w['d']==d,'ordered degree')
                q=w['columns']-1
                req(w['triangular_rows']==list(range(q)),'literal triangular rows')
                S=field(w['schur']); M=field(w['nonzero_minor'])
                t=(-15)**q*factorial(q)
                if d%5==0:
                    req(w['extra_row'] is None and S==(0,0),'kernel witness')
                    req(w['rank']==q,'kernel rank')
                    expected=(Fraction(t),Fraction(0)); kernels+=1
                else:
                    req(type(w['extra_row'])==int and w['extra_row']>=q,'extra row')
                    req(w['rank']==q+1,'full rank')
                    expected=(t*S[0],t*S[1])
                req(M==expected,'exact minor versus exact Schur relation')
                req(M[0]*M[0]+3*M[0]*M[1]+M[1]*M[1]!=0,'minor must be a field unit')
                count+=1
    req((count,kernels)==(144,24),'complete exact witness census')
    return count
def rejected(fn):
    try: fn()
    except (ValueError,TypeError): return True
    return False
def negative_controls(data):
    chosen=None
    for case,branches in data['witnesses'].items():
        for branch,ws in branches.items():
            for idx,w in enumerate(ws):
                for component in range(2):
                    n=w['nonzero_minor'][component][0]
                    if abs(n)>2**53 and int(float(n))!=n:
                        chosen=(case,branch,idx,component,n); break
                if chosen: break
            if chosen: break
        if chosen: break
    req(chosen is not None,'a real precision-loss datum must exist')
    case,branch,idx,comp,n=chosen
    bad=copy.deepcopy(data)
    bad['witnesses'][case][branch][idx]['nonzero_minor'][comp][0]=float(n)
    req(rejected(lambda:validate(bad)),'actual float mutation must fail')
    rawbad=json.dumps(bad).encode()
    req(rejected(lambda:json.loads(rawbad,parse_float=forbid_float)),'float JSON bytes must fail')
    rounded=int(float(n)); bad['witnesses'][case][branch][idx]['nonzero_minor'][comp][0]=rounded
    req(rejected(lambda:validate(json.loads(json.dumps(bad)))),'rounded integer mutation must fail exact relation')
    return {'actual_path':[case,branch,idx,comp],'original_integer':str(n),'float_then_integer':str(rounded),'integer_error':str(rounded-n),'float_rejected':True,'rounded_integer_rejected':True}
def exclusive(path,raw):
    with path.open('xb') as f:
        f.write(raw); f.flush(); os.fsync(f.fileno())

verify_only='--verify-only' in sys.argv
req(sha(SOURCE.read_bytes())==SOURCE_SHA,'unchanged producer checker pin')
req(sha(OLD.read_bytes())==OLD_SHA,'frozen old witness pin')
if not verify_only: req(not OUT.exists() and not RECEIPT.exists(),'refuse overwrite')
proc=subprocess.run([sys.executable,str(SOURCE)],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=25)
req(proc.returncode==0 and not proc.stderr,'producer runtime must pass cleanly')
raw=proc.stdout
req(sha(raw)==RUNTIME_SHA,'runtime bytes must match Fable exact pin')
data=json.loads(raw,parse_float=forbid_float)
count=validate(data); negative=negative_controls(data)
old=json.loads(OLD.read_bytes())
wrong=0; float_witnesses=0; wrong_integer_only=0; examples=[]
for case,branches in data['witnesses'].items():
    for branch,ws in branches.items():
        for idx,w in enumerate(ws):
            prior=old['witnesses'][case][branch][idx]
            isfloat=any(isinstance(x,float) for pair in prior['nonzero_minor'] for x in pair)
            float_witnesses+=int(isfloat)
            # Python compares integer/float exactly; never coerce exact integers to float here.
            bad=prior['nonzero_minor']!=w['nonzero_minor']
            wrong+=int(bad); wrong_integer_only+=int(bad and not isfloat)
            req(all(prior[k]==w[k] for k in ('schur','rank','extra_row','triangular_rows','columns','d')),'unexpected non-minor drift')
            if bad and len(examples)<3:
                examples.append({'case':case,'branch':branch,'d':idx+1,'old_repr':repr(prior['nonzero_minor']),'exact_repr':repr(w['nonzero_minor'])})
result={'schema':'jc2.exact-export-repair/v1','status':'VERIFIED' if verify_only else 'EXPORTED','source_sha256':SOURCE_SHA,'old_sha256':OLD_SHA,'output_sha256':sha(raw),'output_bytes':len(raw),'validated_minors':count,'no_float_types':True,'exact_minor_relations':144,'kernel_minors':24,'nonkernel_minors':120,'old_float_witnesses':float_witnesses,'old_wrong_minors':wrong,'old_wrong_integer_only_minors':wrong_integer_only,'negative_control':negative,'old_examples_as_strings':examples,'numeric_JS_roundtrip':False,'writers_done_on_return':True}
if verify_only:
    req(OUT.read_bytes()==raw,'v2 bytes must match unchanged producer stdout byte for byte')
    validate(json.loads(OUT.read_bytes(),parse_float=forbid_float))
else:
    exclusive(OUT,raw)
    req(OUT.read_bytes()==raw,'exclusive exported bytes')
    validate(json.loads(OUT.read_bytes(),parse_float=forbid_float))
    exclusive(RECEIPT,(json.dumps(result,sort_keys=True,indent=2)+'\n').encode())
# Only hashes and small counts cross the tool boundary, never the witness payload.
print(json.dumps({k:result[k] for k in ('status','output_sha256','output_bytes','validated_minors','old_float_witnesses','old_wrong_minors','old_wrong_integer_only_minors','no_float_types')},sort_keys=True))
