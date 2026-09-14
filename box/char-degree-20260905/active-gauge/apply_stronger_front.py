#!/usr/bin/env python3
"""Apply a separately proved stronger front cut to actual input images."""
import argparse,hashlib,json,sys,time
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'g9966'/'source'));import engine as E

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True)
 ap.add_argument('--output',type=Path,required=True);ap.add_argument('--Dcut',type=int,required=True)
 ap.add_argument('--Ccut',type=int,required=True);ap.add_argument('--proof',type=Path,action='append',required=True)
 ap.add_argument('--minimum-stage',type=int,default=0);a=ap.parse_args();started=time.monotonic()
 assert (a.Dcut,a.Ccut) in [(29,60),(30,62)]
 if a.Dcut==30:assert a.minimum_stage>=1
 data=json.loads(a.input.read_text());assert data['stage']>=a.minimum_stage
 maps={name:{(r,q):sp.sympify(v) for r,q,v in tab} for name,tab in data['maps'].items()}
 rows=[]
 for name,cut in [('B2',a.Dcut),('A3',a.Ccut)]:
  rows.extend((f'proved_stronger_char_front_{name}_{r}_{q}',v) for (r,q),v in maps[name].items() if r<=cut)
 protected=set(sp.symbols('target_a target_b target_c target_d target_e leader55 Z55 rho c'))
 eligible=set(sp.symbols(' '.join(data['full_free_coordinates'])))-protected
 residue,mapping,pivots,zero=E.qstar_reduce(rows,eligible);mapping=E.resolve_map(mapping)
 res=[(l,E.substitute_map(sp.sympify(v),mapping)) for l,v in data['residual_rows']]+residue
 data['maps']={name:[[r,q,str(image)] for (r,q),v in sorted(tab.items()) if (image:=E.substitute_map(v,mapping))!=0] for name,tab in maps.items()}
 data['residual_rows']=[(l,str(v)) for l,v in res if v!=0]
 data['full_free_coordinates']=sorted(set(data['full_free_coordinates'])-set(map(str,mapping)))
 for name,cut in [('B2',a.Dcut),('A3',a.Ccut)]:assert all(r>cut for r,q,v in data['maps'][name])
 data['stronger_characteristic_front']={
  'type':'proved radical consequence; original full characteristic equations retained',
  'parent_input':str(a.input),'parent_input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
  'D_cut_inclusive':a.Dcut,'C_cut_inclusive':a.Ccut,'minimum_source_stage':a.minimum_stage,
  'proofs':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in a.proof],
  'raw_rows':[(l,str(v)) for l,v in rows],
  'Qstar_pivots':[{'row':p.label,'variable':str(p.variable),'leader':str(p.coefficient)} for p in pivots],
  'map':{str(k):str(v) for k,v in mapping.items()},'dependent_zero_rows':zero,
  'residual_rows':[(l,str(v)) for l,v in residue],
  'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'elapsed_seconds':round(time.monotonic()-started,3),
 }
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
 print(data['branch'],data['stage'],'STRONG_FRONT',a.Dcut,a.Ccut,len(rows),len(pivots),len(residue))

if __name__=='__main__':main()
