#!/usr/bin/env python3
import importlib.util
from pathlib import Path
import sys
import json
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import minor_maps as d

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
    return m
old=load('minor_frozen_old','/tmp/jc2-lane.qdzvDy/inputs/band_engine.py')
corrected=load('minor_gate_corrected',HERE.parent/'g9966-repair-gate-20260905/corrected_face_engine.py')
report={}
for mode,mod in [('old',old),('corrected',corrected)]:
  h,vs=mod.h3_template()
  for branch in ['delta2','delta52']:
    mapping,free,meta=d.derive_minor_map(branch,h,vs,mode)
    hm={key:sp.expand(v.xreplace(mapping)) for key,v in h.items()}
    if mode == 'old':
      original_map,original_free,original_meta=old.h3_branch_map(branch)
      original={key:sp.expand(v.xreplace(original_map)) for key,v in h.items()}
      assert hm == original
      assert set(free)==set(original_free)
      raw=d.local_rows(h,branch,9 if branch=='delta2' else 21,mode='old')
      reference=old.local_rows(h,branch,9 if branch=='delta2' else 21)
      assert raw==reference
      meta['frozen_h3_map_image_exact_match']=True
      meta['frozen_local_row_exact_match']=True
    else:
      gate_map,gate_free,gate_meta=corrected.h3_branch_map(branch)
      original={key:sp.expand(v.xreplace(gate_map)) for key,v in h.items()}
      specialization={key:sp.expand(v.subs(sp.Symbol('minor_a2'),0)) for key,v in hm.items()}
      assert specialization == original
      meta['a2_zero_specialization_matches_gate']=True
    meta['mapping']={str(k):str(sp.factor(v)) for k,v in mapping.items()}
    report[mode+'_'+branch]=meta
report['status']='PASS'
(HERE/'minor_maps-controls.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:{'pivots':len(v['pivots']),'free_generators':v['free_generators']} for k,v in report.items() if isinstance(v,dict)},indent=2))
