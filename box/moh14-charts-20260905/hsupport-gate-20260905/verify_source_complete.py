#!/usr/bin/env python3
"""Audit D1_i union outer-disc G_i in the final 18 emitted chart stems.

The arithmetic and builder checks are independent of the compiler. This script
does not prove the supplied source-to-outer-disc theorem and makes no UNIT claim.
"""
from fractions import Fraction as F
from math import floor
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
OLD = HERE.parent
FINAL = HERE / 'source-complete'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inventory(K, d1, B, ds, i):
    raw = {(b,a) for a in range(K) for b in range(floor(d1*a-i*B)+1)}
    outer = {(b,a) for a in range(K) for b in range(floor(-ds*(i*K-a))+1)}
    return raw | outer, raw, outer


def setup(text):
    return dict(re.findall(r'^poly (h|AA\d+|BB\d+) = (.*);$', text, re.M))


def terms(expr):
    return {tuple(sorted(t.strip().split('*'))) for t in expr.split('+')}


def expected_terms(mons, prefix, monic=0):
    out = {('y^%d' % monic,)} if monic else set()
    for b,a in mons:
        factors = ['%s_%d_%d' % (prefix,b,a)]
        if b: factors.append('x' if b==1 else 'x^%d' % b)
        if a: factors.append('y' if a==1 else 'y^%d' % a)
        out.add(tuple(sorted(factors)))
    return out or {('0',)}


def main():
    original = json.loads((OLD/'classes_manifest.json').read_text())
    final = {c['class_id']:c for c in json.loads((FINAL/'classes_manifest.json').read_text())}
    completion = {r['stem']:r for r in json.loads((FINAL/'support-completion.json').read_text())}
    results = []
    for cls in original:
        cid = cls['class_id']
        computed = []
        U = {'h':set(), 'alpha':{}, 'beta':{}}
        for row in cls['rows']:
            K,e,q = row['K'],row['e'],row['q']
            d1,B,ds = F(row['delta_prime']['1']),F(row['B_safe']),F(row['delta_prime'][str(row['s_prime'])])
            expected = {'h':inventory(K,d1,B,ds,1)[0],
                        'alpha':{i:inventory(K,d1,B,ds,i)[0] for i in range(1,e+1)},
                        'beta':{i:inventory(K,d1,B,ds,i)[0] for i in range(2,q+1)}}
            expected['alpha'][e] -= {(0,0)}
            expected['beta'][q] -= {(0,0)}
            assert expected['alpha'][e-q] != {(0,0)}, 'No scalar shear permitted'
            U['h'] |= expected['h']
            for block in ('alpha','beta'):
                for i,m in expected[block].items(): U[block].setdefault(i,set()).update(m)
            report = completion[row['stem']]
            assert F(report['delta_s']) == ds
            assert set(map(tuple,report['outer_h_support'])) == inventory(K,d1,B,ds,1)[2]
            assert set(map(tuple,report['h_added_beyond_raw'])) == (
                expected['h'] - inventory(K,d1,B,ds,1)[1])
            for block in ('alpha','beta'):
                for i in expected[block]:
                    entire,raw,outer = inventory(K,d1,B,ds,i)
                    assert set(map(tuple,report[block+'_added_beyond_raw'][str(i)])) == entire-raw
            computed.append((row['stem'],expected,row))
        computed.append((cid+'_union',U,None))
        for stem, expected, row in computed:
            oldbase, newbase = OLD/'classes'/cid, FINAL/'classes'/cid
            opath,npath = oldbase/'meta'/(stem+'.json'),newbase/'meta'/(stem+'.json')
            op,np = json.loads(opath.read_text()),json.loads(npath.read_text())
            om,nm = op['meta'],np['meta']
            actual = {'h':set(map(tuple,nm['h_inventory'])),
                      'alpha':{int(i):set(map(tuple,m)) for i,m in nm['alpha_inventories'].items()},
                      'beta':{int(i):set(map(tuple,m)) for i,m in nm['beta_inventories'].items()}}
            assert actual == expected, (stem,'final support mismatch')
            assert nm['gauges'] == om['gauges'], stem
            assert np['sat'] == op['sat'] == nm['saturation_factor'] == 'c', stem
            oldvars,newvars = set(op['variables']),set(np['variables'])
            assert oldvars <= newvars
            added = newvars-oldvars
            count = len(actual['h']) + sum(map(len,actual['alpha'].values())) + sum(map(len,actual['beta'].values())) + 1
            assert count == np['parameter_count'] == len(np['variables']) == len(newvars), stem
            ob,nb = oldbase/'builders'/(stem+'_builder.sing'),newbase/'builders'/(stem+'_builder.sing')
            ot,nt=ob.read_text(),nb.read_text()
            os,ns=setup(ot),setup(nt)
            assert set(os)==set(ns)
            assert terms(ns['h']) == expected_terms(expected['h'],'h',K)
            for i,m in expected['alpha'].items(): assert terms(ns['AA%d'%i]) == expected_terms(m,'A%d'%i)
            for i,m in expected['beta'].items(): assert terms(ns['BB%d'%i]) == expected_terms(m,'B%d'%i)
            for key,expr in ns.items():
                specialized = {t for t in terms(expr) if not set(t)&added}
                assert specialized == terms(os[key]), (stem,key,'old setup specialization')
            ring=re.search(r'^ring R=0,\(y,x,(.*)\),\(lp\(1\),dp\((\d+)\)\);$',nt,re.M)
            assert ring and ring.group(1).split(',') == np['variables']
            assert int(ring.group(2)) == count+1
            assert 'native_y_div_fast' in nt and 'if (lead(h) == y^%d)'%K in nt
            # Manifest values must describe the actual post-gauge ring.
            if row is None:
                assert final[cid]['union_parameter_count'] == count, (stem,'union count')
                assert final[cid]['union_h_count'] == len(actual['h'])
                assert final[cid]['union_alpha_dims'] == nm['alpha_dims']
                assert final[cid]['union_beta_dims'] == nm['beta_dims']
            else:
                fr = next(r for r in final[cid]['rows'] if r['stem']==stem)
                assert fr['parameter_count'] == fr['nunk'] == count
                assert completion[stem]['source_complete_unknowns'] == count
            results.append(dict(stem=stem,union=row is None,status='PASS',K=K,
                old_unknowns=op['parameter_count'],final_unknowns=count,
                added_parameter_count=len(added),old_h_count=len(om['h_inventory']),
                final_h_count=len(actual['h']),
                exact_D1_union_outer_support=True,actual_setup_matches_metadata=True,
                monic_and_fixed_ring=True,c_saturation=True,gauges_unchanged=True,
                old_setup_recovered_by_zero_specialization=True,
                final_meta_sha256=sha(npath),final_builder_sha256=sha(nb),
                builder_byte_identical_to_old=ot==nt))
    assert len(results)==18 and len(completion)==12
    s4=next(r for r in results if r['stem']=='C_n24m16_Mm12_m2_5_ell1_s4_union')
    assert s4['old_unknowns']==s4['final_unknowns']==77
    assert s4['old_h_count']==s4['final_h_count']==11
    # A changed support-label comment need not alter any generator; setup and
    # the full executable body from ring onward are compared separately.
    cid='C_n24m16_Mm12_m2_5_ell1_s4';stem=cid+'_union'
    ob=OLD/'classes'/cid/'builders'/(stem+'_builder.sing')
    nb=FINAL/'classes'/cid/'builders'/(stem+'_builder.sing')
    ot,nt=ob.read_text(),nb.read_text()
    same_s4_body = ot[ot.index('ring R='):]==nt[nt.index('ring R='):]
    assert same_s4_body
    payload=dict(status='PASS',scope='Independent exact support/builders audit; source theorem is a separate dependency',
        stems=18,fibres=12,original_classes_manifest_sha256=sha(OLD/'classes_manifest.json'),
        final_classes_manifest_sha256=sha(FINAL/'classes_manifest.json'),
        completion_receipt_sha256=sha(FINAL/'support-completion.json'),
        compiler_source_sha256=sha(OLD/'sprime3_compiler.py'),
        script_sha256=sha(Path(__file__)),
        true_425_s4_control_executable_body_unchanged=same_s4_body,results=results)
    (FINAL/'verification.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k!='results'},indent=2))
    for r in results: print(r['stem'],r['old_unknowns'],'->',r['final_unknowns'])


if __name__=='__main__': main()
