import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
import json,resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
def mul(a,b):
 out={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():out[i+k,j+l]=out.get((i+k,j+l),F(0))+v*w
 return {k:v for k,v in out.items() if v}
def sub(a,b):
 out=a.copy()
 for k,v in b.items():out[k]=out.get(k,F(0))-v
 return {k:v for k,v in out.items() if v}
def der(a,i):
 out={}
 for k,v in a.items():
  if k[i]:
   l=list(k);l[i]-=1;out[tuple(l)]=v*k[i]
 return out
def bracket(a,b):return sub(mul(der(a,0),der(b,1)),mul(der(a,1),der(b,0)))
mode=sys.argv[1] if len(sys.argv)>1 else 'normal'
a={(3,0):F(1),(0,3):F(1)}; b={(0,1):F(1)}
if mode=='changed-map':b={(0,2):F(1)}
if bracket(a,b)!={(2,0):F(3)}:raise ValueError('changed map fails exact monomial-J projection')
# Separate two projective roots from places: the latter are not computed here.
profiles=[(1,),(1,1),(1,2)]
if any(sum(p)>3 or 1 not in p or len(p)>2 for p in profiles):raise ValueError('profile arithmetic')
# Actual degree-three homogeneous factor identity; no H power is expanded.
h=mul({(0,2):F(1)}, {(0,3):F(1),(1,2):F(-3),(2,1):F(3),(3,0):F(-1)})
if mode=='changed-top':h={(0,5):F(1),(1,4):F(-2),(2,3):F(1)}
expected=mul(mul({(0,2):F(1)}, {(0,1):F(1),(1,0):F(-1)}),mul({(0,1):F(1),(1,0):F(-1)},{(0,1):F(1),(1,0):F(-1)}))
if h!=expected:raise ValueError('changed top is not literal (2,3) profile')
print(json.dumps({'status':'PASS','mode':mode,'jacobian':[{'exponent':[2,0],'coefficient':'3'}],'admissible_two-root_D':[sum(p) for p in profiles],'source_claim':'NO actual receiver or Keller point tested'}))
