#!/usr/bin/env python3
"""One-core modular homogeneous dimension test using frozen guided_gb."""
import importlib.util
import json
from pathlib import Path
import sys

root=Path(__file__).resolve().parent
source=Path('/tmp/jc2-lane.zx9GKm/inputs/guided_gb.py')
spec=importlib.util.spec_from_file_location('frozen_guided_gb',source)
gb=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=gb
spec.loader.exec_module(gb)
pre=(root/'controls_t8_p32003_d31750_raw.sing').read_text()
pre+='''
option(redSB);
proc must(int ok,string msg){if(!ok){print("FAIL "+msg);quit;}}
intvec weights=1,2,3,4,5,6,7,9;
proc hcheck(poly p,int expected){
  poly tmp=p; intvec ee; int ww; int j;
  while(tmp!=0){ee=leadexp(tmp);ww=0;for(j=1;j<=8;j++){ww=ww+ee[j]*weights[j];}
    if(ww!=expected){return(0);}tmp=tmp-lead(tmp);}
  return(1);
}
must(size(rows)==15,"ROW_COUNT");
int i,j;poly atzero;
for(i=1;i<=15;i++){
  must(hcheck(rows[i],33-i),"ROW_HOMOGENEITY");
  atzero=rows[i];for(j=1;j<=8;j++){atzero=subst(atzero,var(j),0);}
  must(atzero==0,"ORIGIN");
}
must(hcheck(Bsol,17) && hcheck(eta,16) && hcheck(target,33),"TARGET_HOMOGENEITY");
must(target==Bsol*eta,"TARGET_PRODUCT");
ideal pos=c1^2,c2^2,c3^2,c4^2,c5^2,c6^2,c7^2,b^2;
ideal posGB=std(pos);must(dim(posGB)==0 && vdim(posGB)==256,"POSITIVE_CONTROL");
ideal neg=c1,c2,c3,c4,c5,c6,c7;ideal negGB=std(neg);
must(dim(negGB)==1 && vdim(negGB)==-1,"NEGATIVE_CONTROL");
print("HOMOGENEITY_ORIGIN_POSITIVE_NEGATIVE_PASS");
'''
system=gb.SingularSystem(
    name='controls_t8_direct_f3',prelude=pre,
    generators=tuple(f'rows[{i}]' for i in range(1,16)),
    characteristic=32003,variables=tuple(f'c{i}' for i in range(1,8))+('b',),
    homogeneous=True,positive_weights=(1,2,3,4,5,6,7,9),
    metadata={'droot':31750,'field_lift':'Q[d]/(3*d^2-9)',
              'map':'identity c_i,b; eliminated w_k and B by nonzero scalar high pivots',
              'construction':'direct F1--F3', 'raw_sha256':gb.sha256_file(root/'controls_t8_p32003_d31750_raw.sing')})
result=gb.guided_groebner(system,
    policy=gb.PromotionPolicy.homogeneous_properness(
      'Only homogeneous dimension-zero may promote; localized modular units are never used.'),
    config=gb.RunConfig(output_dir=root/'controls_t8_guided',timeout_seconds=1800,
      total_cores=1,max_parallel_jobs=1,run_perturbed_control=False))
print(json.dumps(result.to_json(),sort_keys=True),flush=True)
