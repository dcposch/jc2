#!/usr/bin/env python3
from pathlib import Path
import json,sys,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import minor_final_verify as m
start=time.monotonic();e=m.load_code(HERE);v=m.Verifier(e,'delta52')
paths=[HERE/f'deep_accelerated_smoke_delta52_phase{i:04d}.json' for i in range(46)]
reports=[];previous=None
for path in paths:
 c=json.loads(path.read_text())
 if previous:
  assert v.equal_map(v.mapping(previous['map_after']),v.mapping(c['map_before']))
  assert v.rows(previous['residual_after'])==v.rows(c['residual_before'])
 reports.append({'file':path.name,'sha256':m.digest(path),**v.replay_phase(c)})
 previous=c
raw=v.regenerate(previous)
out={'status':'PASS','scope':'shortened-prefix implementation control, not branch verdict',
     'phases_checked':len(reports),'QQstar_pivots_checked':sum(r['QQstar_pivots_verified'] for r in reports),
     'radical_memberships_checked':sum(r['radical_power_memberships_verified'] for r in reports),
     'final_free_count':len(previous['free_after']),'terminal_raw_regeneration':raw,
     'phase_checks':reports,'elapsed_seconds':time.monotonic()-start,
     'verifier_sha256':m.digest(HERE/'minor_final_verify.py')}
(HERE/'minor_final-chain-control.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','phases_checked','QQstar_pivots_checked','radical_memberships_checked','elapsed_seconds']},indent=2))
