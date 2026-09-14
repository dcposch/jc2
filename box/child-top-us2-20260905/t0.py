import sys; sys.path.insert(0,'/home/ubuntu/jc2/box/child-top-us2-20260905')
import sympy as sp
from chardata import chardata
x,y = sp.symbols('x y')
# control: (f,g) = (x+y^2, y+(x+y^2)^2), a tame automorphism, hand-computed data (4;-2,1)
f = x+y**2; g = sp.expand(y+(x+y**2)**2)
print('y-side', chardata(f,g,y,x))
print('x-side', chardata(f,g,x,y))
