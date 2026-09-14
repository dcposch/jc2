#!/usr/bin/env python3
"""Apply proved leading-band consequences without any parameter division.

The proof in front-band-lemma.md gives B2[r<=27]=0 and A3[r<=56]=0
on the full characteristic locus.  These are radical consequences, not
invented source support bounds. All defining characteristic rows remain.
"""
import argparse,hashlib,json,sys,time
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'source'));import engine as E

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    start=time.monotonic();data=json.loads(a.input.read_text())
    maps={name:{(r,q):sp.sympify(v) for r,q,v in tab} for name,tab in data['maps'].items()}
    rows=[]
    for name,cut in [('B2',27),('A3',56)]:
        rows.extend((f'proved_char_front_{name}_{r}_{q}',v) for (r,q),v in maps[name].items() if r<=cut)
    eligible=set(sp.symbols(' '.join(data['full_free_coordinates'])))-set(sp.symbols('target_a target_b target_c target_d target_e leader55 Z55 rho c'))
    residue,mapping,pivots,zero=E.qstar_reduce(rows,eligible);mapping=E.resolve_map(mapping)
    res=[(l,E.substitute_map(sp.sympify(v),mapping)) for l,v in data['residual_rows']]+residue
    data['maps']={name:[[r,q,str(image)] for (r,q),v in sorted(tab.items()) if (image:=E.substitute_map(v,mapping))!=0] for name,tab in maps.items()}
    data['residual_rows']=[(l,str(v)) for l,v in res if v!=0]
    data['full_free_coordinates']=sorted(set(data['full_free_coordinates'])-set(map(str,mapping)))
    data['characteristic_front_preprocessing']={'type':'proved radical consequence; all full original characteristic equations still emitted',
      'parent_input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),'parent_input':str(a.input),
      'source_proof':'box/char-degree-20260905/front-band-lemma.md',
      'B2_cut_inclusive':27,'A3_cut_inclusive':56,'raw_rows':[(l,str(v)) for l,v in rows],
      'Qstar_pivots':[{'row':p.label,'variable':str(p.variable),'leader':str(p.coefficient)} for p in pivots],
      'map':{str(k):str(v) for k,v in mapping.items()},'dependent_zero_rows':zero,'residual_rows':[(l,str(v)) for l,v in residue],
      'elapsed_seconds':round(time.monotonic()-start,3)}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(data['branch'],data['stage'],'FRONT',len(rows),len(pivots),len(residue),flush=True)

if __name__=='__main__':main()
