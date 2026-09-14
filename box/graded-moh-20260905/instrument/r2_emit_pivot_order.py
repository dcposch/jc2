#!/usr/bin/env python3
import json,hashlib,re
from pathlib import Path
R=Path('/home/ubuntu/jc2/box/graded-moh-20260905');out=R/'resume-r2'/'triangular'/'136';m=json.loads((out/'custody.json').read_text());d=json.loads((out/'triangular-dag-custody.json').read_text());piv=[p for p in d['pivot_dag'] if p['pivot'] in m['variables']];pv=[p['pivot'] for p in reversed(piv)];vv=pv+[v for v in m['variables'] if v not in pv];wt=m['weights'];order='wp('+','.join(str(wt[v][1]) for v in vv)+')';s=(out/'n1_direct_Q.sing').read_text();s=re.sub(r'ring R=0,\([^;]+;', 'ring R=0,('+','.join(vv)+'),'+order+';',s,count=1);needle='print("N1_INPUT_READY';at=s.index(needle);checks='int fails=0;\n'
for p in piv:
 idx=m['source_generator_order'].index(p['source_index'])+1
 checks+=f'if(leadmonom(I[{idx}])!={p["pivot"]}){{print("BAD_PIVOT_ORDER {p["pivot"]}");fails++;}}\n'
checks+='print("PIVOT_ORDER_CHECKS_FAILED="+string(fails));\nif(fails){quit;}\n';s=s[:at]+checks+s[at:];inp=out/'n1_pivot_order_Q.sing';inp.write_text(s)
meta=dict(m);meta.update(variables=vv,order=order,script_sha256=hashlib.sha256(s.encode()).hexdigest(),pivot_priority_order=pv,extra_check='Each declared constant pivot row has leading monomial exactly its pivot, mechanically checked before std. Variable names/order map is identity except permutation.');(out/'pivot-order-custody.json').write_text(json.dumps(meta,indent=2)+'\n')
work=R/'runs'/'r2_136_pivot_order_n1_Q';work.mkdir(parents=True,exist_ok=True);spec=json.loads((R/'runs'/'r2_136_direct_n1_Q'/'spec.json').read_text());spec.update(input=str(inp),work=str(work),memory_gib=52,order=order,representation='r2_exact_target_component_pivot_priority_N1');spec['command'][-1]=str(inp);(work/'spec.json').write_text(json.dumps(spec,indent=2)+'\n');print(work/'spec.json')
