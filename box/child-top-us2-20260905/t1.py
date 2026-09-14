import sys; sys.path.insert(0,'/home/ubuntu/jc2/box/child-top-us2-20260905')
from fastchar import chardata_poly
from fractions import Fraction as F
import sympy as sp
x,y=sp.symbols('x y')
def topoly(e):
    p=sp.Poly(sp.expand(e),x,y); return {(m[0],m[1]):F(str(c)) for m,c in zip(p.monoms(),p.coeffs())}
f=topoly(x+y**2); g=topoly(sp.expand(y+(x+y**2)**2))
for x0 in [F(7),F(103,5),F(-31,3)]:
    print('x0',x0,'y-side',chardata_poly(f,g,True,x0)['M'],chardata_poly(f,g,True,x0)['d'])
    print('x0',x0,'x-side',chardata_poly(f,g,False,x0)['M'],chardata_poly(f,g,False,x0)['d'])
