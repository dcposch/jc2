#!/usr/bin/env python3
"""Independent exact expanded-polynomial map checks and Singular cover identities."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import json,subprocess,time,re
root=Path('box/graded-moh-20260905/proof/torus_branches');summ=json.loads((root/'summary.json').read_text());results=[]
# Separate implementation from emitter, canonical monomials sorted by variable name.
def canonical(expr,ones=()):
 answer=defaultdict(Fraction)
 for raw in re.split(r'(?=[+-])',expr):
  if not raw:continue
  coeff=Fraction(-1 if raw.startswith('-')else 1);powers=defaultdict(int)
  for factor in raw.lstrip('+-').split('*'):
   if factor[0].isdigit():coeff*=Fraction(factor)
   else:
    part=factor.split('^');assert len(part)<=2
    name=part[0];assert re.fullmatch('[A-Za-z][A-Za-z_0-9]*',name)
    if name not in ones:powers[name]+=int(part[1])if len(part)==2 else 1
  answer[tuple(sorted(powers.items()))]+=coeff
 return {m:c for m,c in answer.items()if c}
for entry in summ:
 dest=root/entry['stem'];cover=dest/'check_cover.sing';p=subprocess.run(['Singular','-q',str(cover)],text=True,capture_output=True);(dest/'check_cover.log').write_text(p.stdout+p.stderr);assert p.returncode==0 and 'COVER_IDENTITY=1'in p.stdout and '?'not in p.stdout
 for branch in entry['branches']:
  started=time.monotonic();bd=Path(branch);cu=json.loads((bd/'custody.json').read_text());source=Path(cu['source_rows']);sourceexpr=[ln.split('|',4)[4].strip()for ln in source.read_text().splitlines()[1:]]
  btext=(bd/'branch_ideal.sing').read_text();gen=btext.split('ideal I=\n',1)[1].rsplit(';',1)[0];targetexpr=gen.split(',\n');assert len(targetexpr)==len(sourceexpr)==cu['source_generator_count']
  onevars={v for v,t in cu['branch_map'].items()if t=='1'};assert onevars=={'c',cu['coordinate']}
  for src,dst in zip(sourceexpr,targetexpr):assert canonical(src,onevars)==canonical(dst)
  inverse={v:k for k,v in cu['msolve_map'].items()}
  for prime in(0,1073741827):
   lines=(bd/f'branch_p{prime}.ms').read_text().splitlines();assert lines[0].split(',')==list(cu['msolve_map'].values());assert lines[1]==str(prime)
   body='\n'.join(lines[2:]);restored=re.sub(r'\bv\d+\b',lambda m:inverse[m.group()],body);assert restored==gen
  item=dict(branch=str(bd),map_check='EXACT_Q_POLYNOMIAL_IMAGE_PASS',msolve_inverse_rename='PASS',generator_count=cu['source_generator_count'],remaining_variables=len(cu['branch_variables']),seconds=round(time.monotonic()-started,3));results.append(item);(bd/'map-verification.json').write_text(json.dumps(item,indent=2)+'\n');print(json.dumps(item),flush=True)
(root/'verification.json').write_text(json.dumps(results,indent=2)+'\n')
