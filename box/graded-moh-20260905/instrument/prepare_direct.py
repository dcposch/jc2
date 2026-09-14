#!/usr/bin/env python3
from pathlib import Path
import re,json
out=Path(__file__).resolve().parent
base=Path('box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes')
for meta in base.glob('*/meta/*json'):
 if '_union' in meta.name:continue
 m=json.loads(meta.read_text())
 if m['parameter_count'] not in (77,136):continue
 stem=meta.stem
 source=Path(m['builder'])
 s=source.read_text(); s=s.split('if (H0 != 0) {')[0]
 assert s.endswith('if (tmpSame != 0) { H0 = H0 + tmpSame; }\n')
 row=out/(stem+'_direct_rows.tsv')
 s=re.sub(r'string rowsfile = "[^"]+";',f'string rowsfile = "{row}";',s)
 maxh=max(map(int,re.findall(r'poly H(\d+) = 0;',s)))
 ell=m['meta']['closed_form']['ell']
 s+='\n// Exact direct coefficient ideal; reconstructed from all native pre-division blocks.\npoly DIRECT=0;\n'
 s+=''.join(f'DIRECT=DIRECT*h+H{i};\n' for i in range(maxh,-1,-1))
 s+=f'DIRECT=DIRECT-c*x^{ell};\nnative_append_coeffs(DIRECT,0,rowsfile,WX,WY);\nprint("DIRECT_DONE equations="+string(source_idx));\nquit;\n'
 p=out/(stem+'_direct_builder.sing');p.write_text(s)
 print(p)
