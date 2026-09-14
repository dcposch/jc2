#!/usr/bin/env python3
"""Run the frozen guarded GB engine on an exact, inhomogeneous X chart."""
import argparse, importlib.util, json, sys
from pathlib import Path

root=Path(__file__).resolve().parent
lib=Path('/tmp/jc2-lane.Fz7unY/inputs/guided_gb.py')
spec=importlib.util.spec_from_file_location('k16x_guided',lib)
gg=importlib.util.module_from_spec(spec);sys.modules[spec.name]=gg;spec.loader.exec_module(gg)
p=argparse.ArgumentParser();p.add_argument('label');p.add_argument('chart',choices=['main','boundary']);p.add_argument('--timeout',type=int,default=300)
a=p.parse_args()
prelude=(root/f'{a.label}_{a.chart}_prelude.sing').read_text()
gens=('cleared','1-u*Delta*HH') if a.chart=='main' else ('rows','Delta','AA','1-s*Bsol')
system=gg.SingularSystem(name=f'{a.label}_{a.chart}',prelude=prelude,generators=gens,characteristic=0,homogeneous=False,metadata={'source':'fresh direct F3 reconstruction','inhomogeneous_chart':True})
out=gg.guided_groebner(system,policy=gg.PromotionPolicy.exact_q('Exact algebraic number field, no modular inference.'),config=gg.RunConfig(output_dir=root/f'{a.label}_{a.chart}_exact',timeout_seconds=a.timeout,total_cores=1,max_parallel_jobs=1))
print(json.dumps({'label':a.label,'chart':a.chart,'verdict':out.verdict.value,'runs':[{'seconds':r['elapsed_seconds'],'returncode':r['returncode'],'main':r['main']} for r in out.certificate['runs']]},indent=2),flush=True)
