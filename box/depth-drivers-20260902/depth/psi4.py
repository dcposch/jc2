import sys; sys.path.insert(0,'/tmp/dc/depth')
import places
from sympy import symbols
places.singular_branches.__globals__['__doc__']=None
x,y=symbols('x y')
# raise the Singular timeout
import re
src=open('/tmp/dc/depth/places.py').read().replace("timeout=60","timeout=900")
ns={}
exec(compile(src.split('BATTERY = [')[0],'p','exec'),ns)
P=x; Q=x*y**2
g=5*(x+(x*y**2)**4)-3*(x*y**2)+7
r,e=ns['places_at_infinity'](g)
print("psi_4 o (x,xy^2):", r, e)
if r: 
    D,nus=r; print(" D=",int(D)," r_inf=",len(nus)," D-r_inf=",int(D)-len(nus)," (published T=7, kappa=1, Lam=4)"," nu=",sorted(nus))
