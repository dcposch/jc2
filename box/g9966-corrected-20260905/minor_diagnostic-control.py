import importlib.util
from pathlib import Path
import sys,json
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
fresh=load('minor_fresh_diag',HERE/'diagnostic_engine.py')
gate=load('minor_gate_diag',HERE.parent/'g9966-repair-gate-20260905/corrected_face_engine.py')
report={}
for branch in ['delta2','delta52']:
    f,ff,fm=fresh.build_major_h2(branch,8)
    g,gf,gm=gate.build_major_h2(branch,8)
    fs={key:sp.expand(value.subs(sp.Symbol('minor_a2'),0)) for key,value in f.items()}
    assert fs==g
    assert ff-({sp.Symbol('minor_a2')} if branch=='delta2' else set())==gf
    fo,ffree,fmeta=fresh.outer_state(7)
    go,gfree,gmeta=gate.outer_state(7)
    assert fo==go and ffree==gfree and fmeta==gmeta
    report[branch]={'K2_a2_zero_specialization_identical':True,'outer_all_offsets_identical':True,
                    'inner_free':len(ff),'gate_inner_free':len(gf),'K2_terms':len(f),'outer_free':len(ffree)}
report['status']='PASS'
(HERE/'minor_diagnostic-control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
