#!/usr/bin/env python3
"""Check full production99 leading-target subtraction against source images."""
import argparse,hashlib,json,re
from pathlib import Path
import sympy as s

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--script',type=Path,required=True)
 ap.add_argument('--input',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 text=a.script.read_text();rows=text.split('ideal I=\n',1)[1].split(';',1)[0].split(',\n')
 inp=json.loads(a.input.read_text());assert inp['k']==33 and inp['target']==55
 coordpath=Path(inp['source_coordinate_input']['path']);raw=coordpath.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==inp['source_coordinate_input']['sha256']
 coords=json.loads(raw);z=s.Symbol('zz')
 bands={name:s.expand(sum(s.sympify(v)*z**q for r,q,v in tab if r==0)) for name,tab in coords['maps'].items()}
 H0=s.expand(bands['h3']**3+bands['C2']*bands['h3']+bands['C3'])
 target=s.expand(H0*s.sympify(inp['face_expr'].replace('^','**')))
 assert s.expand(H0-z**24*(1+z)**9)==0 and s.expand(target-z**40*(1+z)**15)==0
 leading=[(i,row) for i,row in enumerate(rows) if 'leader55' in row];assert len(leading)==17
 found=[]
 for _,row in leading[:-1]:
  match=re.search(r'\+\(-1\)\*\(\((\d+)\)\*leader55\)\)$',row)
  assert match,row[-160:];found.append(int(match.group(1)))
 expected=[int(s.Poly(target,z).coeff_monomial(z**q)) for q in range(40,56)]
 assert found==expected
 assert [i for i,_ in leading[:-1]]==list(range(len(rows)-18,len(rows)-2))
 assert leading[-1]==(len(rows)-2,'(Z55*leader55-1)')
 sep='rho' if coords['branch']=='delta2' else 'c';inv='Zrho' if sep=='rho' else 'Zc'
 assert rows[-1]==f'({inv}*{sep}-1)'
 result={'status':'PASS','field':'Q','branch':coords['branch'],'stage':coords['stage'],
  'source_H0':str(s.factor(H0)),'whole_target':str(s.factor(target)),
  'target_depth':141,'target_z_powers':list(range(40,56)),
  'all_16_target_coefficients_subtracted':found,'leader_localizer':'Z55*leader55-1',
  'separation_localizer':f'{inv}*{sep}-1','no_source_or_graph_row_contains_leader':True,
  'leading_row_convention':'actual coefficient minus free scalar target',
  'script_sha256':hashlib.sha256(text.encode()).hexdigest(),
  'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
  'source_coordinate_sha256':hashlib.sha256(raw).hexdigest(),
  'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps(result,sort_keys=True))

if __name__=='__main__':main()
