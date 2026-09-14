#!/usr/bin/env python3
"""Certify the numerical output against independent object postconditions."""
import collections,importlib.util,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('m','/tmp/jc2-lane.94eJYj/inputs/moh_skeleton_full.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rows=[json.loads(x) for x in (ROOT/'core-rows-kmin2.jsonl').read_text().splitlines()]
seen=set();bad=collections.Counter();dists=collections.defaultdict(collections.Counter)
for r in rows:
 S=m.Skel(r['n'],r['m'],r['M'],{int(k):v for k,v in r['V'].items()})
 key=(S.n,S.m,tuple(r['M']),tuple(sorted(S.V.items())))
 bad['duplicate_rows']+=key in seen;seen.add(key)
 bad['windows_fail']+=not S.windows_ok()
 bad['full_postfilter_fail']+=not S.full_ok()
 bad['u_noninteger']+=S.u.denominator!=1
 bad['top_asymmetry_fail']+=not(S.K>S.u>S.K/2)
 bad['denominator_bottom_identity_fail']+=((S.e+S.dd)*S.V[2]-1)%S.A(1)!=0
 dists[r['tag']+'_s'][S.s]+=1;dists[r['tag']+'_K'][S.K]+=1
 dists[r['tag']+'_n'][S.n]+=1
 bad['any10_absent_'+r['tag']]+=not S.any10()
result=dict(postcheck_counts=dict(bad),distributions={k:dict(v) for k,v in dists.items()})
(ROOT/'core-audit-rows.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
