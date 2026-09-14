#!/usr/bin/env python3
"""Exact re-expression: full x,y coefficients versus full monic h-adic coefficients.
The polynomial before native_y_div is sum H_i*h^i=J(Q,P).
For monic h the coefficient ideals of the two bases are equal over the same
parameter ring: y^{r+Ki} and y^r*h^i differ by lower y terms, unitriangular.
"""
from pathlib import Path
import json,re,hashlib,subprocess
BASE=Path('/home/ubuntu/jc2/box/moh14-charts-20260905/hsupport-gate-20260905')
JOBS=json.loads((BASE/'ops/launched-native.json').read_text())
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
results=[]
for job in JOBS:
 stem=job['stem'];cls=stem.rsplit('_V',1)[0];dest=BASE/'classes'/cls
 builder=dest/'builders'/(stem+'_builder.sing');src=builder.read_text();meta=json.loads((dest/'meta'/(stem+'.json')).read_text())
 q=meta['meta']['closed_form']['q'];e=meta['meta']['closed_form']['e'];ell=meta['meta']['row']['k']
 assert 'native_y_div_fast' in src
 split=src.index('if (H0 != 0) {')
 prefix=src[:split]
 levels=[int(x) for x in re.findall(r'^poly H(\d+) = 0;',prefix,re.M)]
 assert levels==list(range(max(levels)+1))
 direct=prefix.replace(stem+'_rows.tsv',stem+'_direct_rows.tsv')
 direct+='\n// Equal coefficient ideal under the monic unitriangular h-adic basis.\npoly DIRECT=0;\n'
 for i in reversed(levels):direct+=f'DIRECT=DIRECT*h+H{i};\n'
 direct+=f'poly target_xk = native_coeff_xy(DIRECT, {ell}, 0, WX, WY);\n'
 direct+='if (target_xk != 0) { print("DIRECT_GATE target_xk_nonzero=1"); } else { print("DIRECT_GATE target_xk_nonzero=0"); }\n'
 direct+=f'DIRECT=DIRECT-c*x^{ell};\n'
 direct+='native_append_coeffs(DIRECT, 0, rowsfile, WX, WY);\nprint("NATIVE_DONE equations="+string(source_idx));\nquit;\n'
 out=dest/'builders'/(stem+'_direct_builder.sing');out.write_text(direct)
 # Exact rational specialization, independent differential Jacobian, two seeds.
 definitions='\n'.join(re.findall(r'^poly (?:h|AA\d+|BB\d+) = .*?;$',prefix,re.M))
 raw=prefix[prefix.index('poly H0 = 0;'):]
 variables=meta['variables']
 records=[]
 for seed in (1,7):
  vals={v:f'({((i+seed)*17)%13-6}/{1+((i+seed)*7)%3})' for i,v in enumerate(variables)}
  numeric=re.sub(r'\b[A-Za-z_][A-Za-z0-9_]*\b',lambda m:vals.get(m.group(),m.group()),definitions)
  ctrl='ring R=0,(y,x),lp;\n'+numeric+'\n'+raw
  ctrl+='poly RECOMPOSED=0;\n'
  for i in reversed(levels):ctrl+=f'RECOMPOSED=RECOMPOSED*h+H{i};\n'
  aa={int(i) for i in re.findall(r'^poly AA(\d+) =',definitions,re.M)}
  bb={int(i) for i in re.findall(r'^poly BB(\d+) =',definitions,re.M)}
  low=f'h^{q}'+''.join(f'+BB{i}*h^{q-i}' for i in sorted(bb))
  high=f'h^{e}'+''.join(f'+AA{i}*h^{e-i}' for i in sorted(aa))
  ctrl+=f'poly Q={low};\npoly P={high};\npoly J=diff(Q,x)*diff(P,y)-diff(Q,y)*diff(P,x);\n'
  ctrl+='if (J-RECOMPOSED==0) { print("DIRECT_CONTROL differential_identity=1"); } else { print("DIRECT_CONTROL differential_identity=0"); }\n'
  ctrl+='if (J-RECOMPOSED-1!=0) { print("DIRECT_CONTROL negative=1"); } else { print("DIRECT_CONTROL negative=0"); }\n'
  # Independent monic division/recomposition with actual numeric h.
  ctrl+='ideal HD=h; poly running=RECOMPOSED; poly rebuilt=0; poly hp=1; list d; int k=0;\nwhile(running!=0) { d=division(running,HD); rebuilt=rebuilt+d[2][1]*hp; hp=hp*h; running=d[1][1,1]; k++; if(k>200){print("DIRECT_CONTROL overflow=1"); break;} }\n'
  ctrl+='if(rebuilt==J){print("DIRECT_CONTROL monic_recomposition=1");}else{print("DIRECT_CONTROL monic_recomposition=0");}\nquit;\n'
  cpath=BASE/'ops'/'direct-controls'/(stem+f'_seed{seed}.sing');cpath.parent.mkdir(exist_ok=True);cpath.write_text(ctrl)
  proc=subprocess.run(['Singular','--cpus=1','--threads=1','--flint-threads=1','-q','--no-rc',str(cpath)],capture_output=True,text=True,timeout=60)
  log=cpath.with_suffix('.log');log.write_text(proc.stdout+proc.stderr)
  passed=proc.returncode==0 and all('DIRECT_CONTROL '+tag+'=1' in proc.stdout for tag in ['differential_identity','negative','monic_recomposition']) and not re.search(r'DIRECT_CONTROL \w+=0|\?',proc.stdout)
  records.append(dict(seed=seed,pass_control=passed,control_sha256=digest(ctrl),log_sha256=digest(log.read_text())))
  assert passed,(stem,seed,proc.stdout)
 results.append(dict(stem=stem,source_builder_sha256=digest(src),direct_builder_sha256=digest(direct),max_formal_h_level=max(levels),q=q,e=e,ell=ell,controls=records))
(BASE/'ops/direct-transform.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
