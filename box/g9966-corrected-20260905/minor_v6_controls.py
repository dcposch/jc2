from pathlib import Path
import argparse,json,sys
import sympy as sp
ap=argparse.ArgumentParser();ap.add_argument('--code',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();sys.path.insert(0,str(a.code))
import minor_exact_parser as P
import minor_flint_map_verify as F
x,y,z,u=sp.symbols('x y z u');local={str(v):v for v in [x,y,z,u]};checks=[]
for expression in [sp.expand((x+y+z)**9/sp.Integer(32768)),sp.expand((3*x-7*y+u)**6/sp.Integer(17)),sp.Integer(0),sp.Rational(-2,7)]:assert P.parse(str(expression),local)==expression
for text in ['x**1.0','1/x','hidden+x','sqrt(2)']:
 try:P.parse(text,local)
 except (AssertionError,ValueError,TypeError):checks.append(text)
 else:raise AssertionError('bad parse accepted')
before={u:sp.expand((x+y)**7/sp.Integer(13))};resolved={x:sp.expand(2*y**2+z/sp.Integer(7))};after={u:sp.expand(before[u].xreplace(resolved)),x:resolved[x]}
r=F.verify(before,resolved,after,{x,y,z},{y,z})
bad=dict(after);bad[u]+=1
try:F.verify(before,resolved,bad,{x,y,z},{y,z})
except AssertionError:checks.append('changed_native_map_image')
else:raise AssertionError('changed map accepted')
a.out.write_text(json.dumps({'status':'PASS','negative_controls':checks,'polynomial_parser_sha256_at_import':P.OWN_SHA256,'native_graph_control':r},indent=2)+'\n');print('PASS')
