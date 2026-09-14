from pathlib import Path
import argparse,json,sys
import sympy as sp
ap=argparse.ArgumentParser();ap.add_argument('--code',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();sys.path.insert(0,str(a.code))
import minor_flint_corner_direct as C
x,y,d,e,b,j=sp.symbols('x y d e b Jc');q=d*d+sp.Rational(2,3)*e*d+sp.Rational(5,7)*b;S={'inner_power':3,'outer_power_F':3,'outer_power_G':2};checks=[]
for high in [False,True]:
 jets={'h3':(d**3 if high else d,e,1),'C2':(b,d,1),'C3':(e,1,b),'A2':(1,d,2),'A3':(e,1,d),'B1':(b,2,3),'B2':(e,b,1)}
 def expression(name):v=jets[name];return v[0]+v[1]*x+v[2]*y
 h=expression('h3');H=h**3+expression('C2')*h+expression('C3');F=H**3+expression('A2')*H+expression('A3');G=H**2+expression('B1')*H+expression('B2');at={x:0,y:0}
 expected=sp.rem(sp.expand(sp.diff(F,x).xreplace(at)*sp.diff(G,y).xreplace(at)-sp.diff(F,y).xreplace(at)*sp.diff(G,x).xreplace(at)-j),q,d)
 actual,meta=C.corner(jets,S,q,d,j);assert sp.expand(expected-actual)==0
 checks.append({'higher_d_input':high,'metadata':meta})
a.out.write_text(json.dumps({'status':'PASS','checks':checks,'driver_hash':C.OWN_SHA256},indent=2)+'\n');print('PASS')
