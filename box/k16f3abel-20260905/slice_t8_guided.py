#!/usr/bin/env python3
"""Bounded homogeneous t=8 b=0 slice, using verified direct F3 rows."""
import importlib.util
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
source = Path('/tmp/jc2-lane.zx9GKm/inputs/guided_gb.py')
spec = importlib.util.spec_from_file_location('frozen_slice_guided_gb', source)
gb = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = gb
spec.loader.exec_module(gb)
raw = root/'controls_t8_p32003_d31750_raw.sing'
pre = raw.read_text()+'''
option(redSB);
proc must(int ok,string msg){if(!ok){print("FAIL "+msg);quit;}}
intvec weights=1,2,3,4,5,6,7,9;
proc hcheck(poly p,int expected){
  poly tmp=p; intvec ee; int ww; int j;
  while(tmp!=0){ee=leadexp(tmp);ww=0;for(j=1;j<=8;j++){ww=ww+ee[j]*weights[j];}
    if(ww!=expected){return(0);}tmp=tmp-lead(tmp);}
  return(1);
}
int i,j;poly atzero;
must(size(rows)==15,"ROW_COUNT");
for(i=1;i<=15;i++){
  must(hcheck(rows[i],33-i),"ROW_HOMOGENEITY");
  atzero=rows[i];for(j=1;j<=8;j++){atzero=subst(atzero,var(j),0);}
  must(atzero==0,"ORIGIN");
}
must(hcheck(b,9),"SLICE_HOMOGENEITY");
ideal pos=c1,c2,c3,c4,c5,c6,c7,b;ideal posGB=std(pos);
must(dim(posGB)==0 && vdim(posGB)==1,"POSITIVE_CONTROL");
ideal neg=c1,c2,c3,c4,c5,c6,c7;ideal negGB=std(neg);
must(dim(negGB)==1,"NEGATIVE_CONTROL");
print("SLICE_HOMOGENEITY_ORIGIN_CONTROLS_PASS");
'''
system = gb.SingularSystem(
    name='slice_t8_bzero',prelude=pre,
    generators=tuple(f'rows[{i}]' for i in range(1,16))+('b',),
    characteristic=32003,variables=tuple(f'c{i}' for i in range(1,8))+('b',),
    homogeneous=True,positive_weights=(1,2,3,4,5,6,7,9),
    metadata={'droot':31750,'field_lift':'Q[d]/(3*d^2-9)',
              'slice':'b=0','raw_sha256':gb.sha256_file(raw),
              'map':'identity on c_i,b; high elimination has verified scalar units'})
result = gb.guided_groebner(system,
    policy=gb.PromotionPolicy.homogeneous_properness(
        'Only the homogeneous b=0 slice dimension may promote, never modular length.'),
    config=gb.RunConfig(output_dir=root/'slice_t8_guided',timeout_seconds=900,
        total_cores=1,max_parallel_jobs=1,run_perturbed_control=False))
print(json.dumps(result.to_json(),sort_keys=True),flush=True)
