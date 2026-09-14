#!/usr/bin/env python3
"""Tiny independent controls only. Never construct the D125 support."""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as F
import hashlib
import json
from math import comb
import os
from pathlib import Path
import resource
import re
import signal
import subprocess
import sys
import time
import exporter as e

def check(ok,message):
    if not ok: raise RuntimeError(message)

def must_fail(action,label):
    try: action()
    except (ValueError,FileExistsError,json.JSONDecodeError):
        return label
    raise RuntimeError("mutation survived: "+label)

def direct_support(d,normalized):
    return {(i,j) for i in range(d['degree']+1) for j in range(d['degree']+1)
            if i+j<=d['degree'] and 5*i-j<=d['weight_cap'] and
            (not normalized or (j<=d['vertical_cap'] and
             (j!=d['vertical_cap'] or i==d['guard'][0])))}

def independent_jac(maps):
    out=defaultdict(dict)
    for (i,j),pid in maps['P'].items():
        for (k,s),qid in maps['Q'].items():
            det=i*s-j*k
            if det:
                check(i+k>=1 and j+s>=1,'negative derivative exponent')
                out[i+k-1,j+s-1][(pid,qid)]=F(det)
    out[0,0][()]=F(-1,5)
    return dict(out)

def decoded(rec):
    out={}
    for n,d,ids in rec['terms']:
        key=tuple(ids)
        check(key not in out,'duplicate monomial')
        out[key]=F(int(n),int(d))
    return out

def phi_coeff(maps,side,ell,order):
    # Direct binomial expansion Phi(u^i v^j)=X^(5i)*(Y+X^-1)^j.
    out={}
    for (i,j),idx in maps[side].items():
        for k in range(j+1):
            xpower=5*i-j+k
            if k==order and xpower==ell+order:
                out[(idx,)]=F(comb(j,k))
    return out

def evaluate(rec,values):
    total=F(0)
    for n,d,ids in rec['terms']:
        value=F(int(n),int(d))
        for idx in ids: value*=values.get(idx,F(0))
        total+=value
    return total

def check_singular(text,records,rows):
    names=[r['name'] for r in records]
    lines=text.splitlines()
    check(lines[1]=='ring R=0,('+','.join(names)+'),dp;','Singular ring/order drift')
    body=text.split('ideal I=\n',1)[1].split(';\n',1)[0]
    chunks=body.split(',\n')
    check(len(chunks)==len(rows),'Singular row count')
    for chunk,row in zip(chunks,rows):
        label,poly=chunk.split('\n',1)
        check(label=='// '+row['label'],'Singular row label')
        got={}
        if poly!='0':
            for atom in poly.split('+'):
                match=re.fullmatch(r'\((-?\d+)/(\d+)\)((?:\*[A-Za-z0-9_]+)*)',atom)
                check(match is not None,'Singular literal grammar')
                n,d,factors=match.groups()
                ids=tuple(names.index(s) for s in factors.split('*')[1:])
                check(ids not in got,'Singular duplicate term')
                got[ids]=F(int(n),int(d))
        check(got==decoded(row),'Singular coefficient drift')

def main():
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
    signal.alarm(25)
    start=time.monotonic()
    base=Path(sys.argv[1]);base.mkdir()
    summary={'fixture_results':[],'mutation_rejections':[],'production_runs':0}
    baseline=None
    for mode in ('original','normalized'):
        spec=e.toy_spec(mode)
        records,maps=e.variables(spec)
        for side in ('P','Q'):
            check(set(maps[side])==direct_support(spec['sides'][side],mode=='normalized'),'support mismatch')
            check((0,0) in maps[side],'lost additive constant')
        literal=list(e.rows(spec,records,maps))
        jac=independent_jac(maps)
        physical={tuple(r['output_exponent']):decoded(r) for r in literal if r['kind']=='physical_J'}
        check(set(jac)<=set(physical),'omitted nonzero output')
        for exponent,actual in physical.items():
            check(actual==jac.get(exponent,{}),'independent convolution mismatch')
        for r in literal:
            if r['kind']=='jet':
                check(decoded(r)==phi_coeff(maps,r['side'],r['ell'],r['order']),'jet Phi mismatch')
            if r['kind']=='pin':
                expected=phi_coeff(maps,r['side'],r['ell'],r['t_power']-r['ell'])
                target=F(*map(int,r['target']))
                if target: expected[()]=-target
                check(decoded(r)==expected,'pin Phi mismatch')
        check(sum(r['kind']=='pin' for r in literal)==5,'pin count')
        jets=[r['label'] for r in literal if r['kind']=='jet']
        if baseline is None: baseline=jets
        else: check(jets==baseline,'normalized lost original jets')
        guard=literal[-1]
        expected_ids=[maps[s][tuple(spec['sides'][s]['guard'])] for s in ('P','Q')]+[len(records)-1]
        check(decoded(guard)=={tuple(expected_ids):F(1),():F(-1)},'degree guard drift')
        out=base/mode
        manifest=e.build(spec,out,singular=True)
        footer=e.verify(out/'literal.jsonl',spec)
        check(footer==manifest['footer'],'manifest footer drift')
        singular=(out/'import.sing').read_text()
        check_singular(singular,records,literal)
        check('std(' not in singular and 'slimgb' not in singular,'unexpected solve')
        check(sum(line.startswith('// J_u') for line in singular.splitlines())==len(physical),'Singular physical slot omission')
        summary['fixture_results'].append({'mode':mode,'variable_count':len(records),'footer':footer,
                                           'files':manifest['files']})
        if mode=='original':
            original_lines=(out/'literal.jsonl').read_bytes().splitlines(keepends=True)
            original_spec=spec
    # Positive Keller control with genuine original total-degree endpoints.
    good={'name':'POSITIVE_TOY','mode':'original','target':['1','5'],
          'sides':{'P':{'degree':2,'weight_cap':5,'terminal_h':100,'vertical_cap':2,'guard':[0,2]},
                   'Q':{'degree':1,'weight_cap':1,'terminal_h':100,'vertical_cap':1,'guard':[0,1]}},'pins':[]}
    records,maps=e.variables(good)
    values={maps['P'][1,0]:F(1),maps['P'][0,2]:F(1),maps['Q'][0,1]:F(1,5),len(records)-1:F(5)}
    good_rows=list(e.rows(good,records,maps))
    check(all(evaluate(r,values)==0 for r in good_rows),'positive P=u+v^2,Q=v/5 failed')
    values[len(records)-1]=0
    check(evaluate(good_rows[-1],values)==-1,'guard negative control failed')
    values[len(records)-1]=5
    values[maps['P'][0,2]]=0
    check(evaluate(good_rows[-1],values)==-1,'degree-drop negative control failed')
    # A support with no bilinear constant contribution must still emit -1/5.
    modified_maps={s:{(0,0):maps[s].get((0,0),0)} for s in ('P','Q')}
    modified_maps['P'][0,2]=maps['P'][0,2]
    modified_maps['Q'][0,1]=maps['Q'][0,1]
    target_row=next(r for r in e.rows(good,records,modified_maps) if r['label']=='J_u0_v0')
    check(decoded(target_row)=={():F(-1,5)},'empty LHS lost target obligation')
    # Stream mutations. Semantic changes fail before the old digest is examined.
    def mutation(label,mutate):
        lines=deepcopy(original_lines);mutate(lines)
        path=base/(label+'.jsonl');path.write_bytes(b''.join(lines))
        summary['mutation_rejections'].append(must_fail(lambda:e.verify(path,original_spec),label))
    def change_record(lines,predicate,change):
        for i,line in enumerate(lines):
            obj=json.loads(line)
            if predicate(obj):
                change(obj);lines[i]=e.canonical(obj);return
        raise RuntimeError('mutation target absent')
    mutation('wrong_target_sign',lambda lines:change_record(lines,lambda r:r.get('label')=='J_u0_v0',
                 lambda r:r['terms'].__setitem__(-1,['1','5',[]])))
    mutation('wrong_determinant',lambda lines:change_record(lines,
                 lambda r:r.get('kind')=='physical_J' and any(len(t[2])==2 for t in r['terms']),
                 lambda r:r['terms'][0].__setitem__(0,str(int(r['terms'][0][0])+1))))
    mutation('wrong_pin',lambda lines:change_record(lines,lambda r:r.get('kind')=='pin',
                 lambda r:r['terms'].__setitem__(-1,['7','5',[]])))
    mutation('wrong_variable_map',lambda lines:change_record(lines,lambda r:r.get('type')=='variable',
                 lambda r:r.__setitem__('name','MUTATED')))
    mutation('wrong_field',lambda lines:change_record(lines,lambda r:r.get('type')=='header',
                 lambda r:r.__setitem__('coefficient_field','Fp')))
    mutation('missing_target_row',lambda lines:lines.__delitem__(next(i for i,l in enumerate(lines) if json.loads(l).get('label')=='J_u0_v0')))
    mutation('missing_guard',lambda lines:lines.__delitem__(-2))
    mutation('missing_footer',lambda lines:lines.pop())
    mutation('trailing_bytes',lambda lines:lines.append(b'X'))
    mutation('wrong_footer_digest',lambda lines:change_record(lines,lambda r:r.get('type')=='footer',
                 lambda r:r.__setitem__('prefix_sha256','0'*64)))
    summary['mutation_rejections'].append(must_fail(lambda:e.build(original_spec,base/'original'),'existing_output_directory'))
    summary['mutation_rejections'].append(must_fail(lambda:e.build(original_spec,base/'capped',max_bytes=64),'output_cap'))
    check(not (base/'capped'/'manifest.json').exists(),'capped run has success manifest')
    summary['mutation_rejections'].append(must_fail(lambda:e.verify(base/'capped'/'literal.jsonl',original_spec),'capped_incomplete_stream'))
    for mode in ('original','normalized'):
        path=base/('forbidden_'+mode)
        proc=subprocess.run([sys.executable,str(Path(e.__file__).resolve()),'--mode',mode,'--output',str(path)],capture_output=True,text=True,timeout=3)
        check(proc.returncode!=0 and 'NO_PRODUCTION_AUTHORITY' in proc.stderr and not path.exists(),'production CLI authority failed')
        summary['mutation_rejections'].append('no_authority_cli_'+mode)
        summary['mutation_rejections'].append(must_fail(lambda:e.build(e.production_spec(mode),path),'no_authority_api_'+mode))
    summary['positive_control']='P=u+v^2,Q=v/5,Z=5; degree-drop/Z=0 rejected'
    summary['empty_target_control']='PASS'
    summary['elapsed_seconds']=time.monotonic()-start
    summary['max_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    summary['optimized_python']=not __debug__
    summary['builder_sha256']=e.digest_file(e.__file__)
    summary['test_sha256']=e.digest_file(__file__)
    summary['status']='PASS'
    (base/'summary.json').write_bytes(e.canonical(summary))
    print(json.dumps(summary,sort_keys=True))

if __name__=='__main__': main()
