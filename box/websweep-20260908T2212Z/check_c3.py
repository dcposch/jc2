import sys
sys.dont_write_bytecode=True
from fractions import Fraction as Q
from itertools import permutations
import json,resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
def add(*args):
 r={}
 for a in args:
  for k,v in a.items():r[k]=r.get(k,0)+v
 return {k:v for k,v in r.items() if v}
def scale(a,c):return {k:v*c for k,v in a.items() if v*c}
def mul(a,b):
 r={}
 for k,v in a.items():
  for l,w in b.items():
   t=tuple(i+j for i,j in zip(k,l));r[t]=r.get(t,0)+v*w
 return {k:v for k,v in r.items() if v}
def pw(a,n):
 r={(0,0,0):1}
 for _ in range(n):r=mul(r,a)
 return r
def der(a,i):
 r={}
 for k,v in a.items():
  if k[i]:l=list(k);l[i]-=1;r[tuple(l)]=v*k[i]
 return r
def val(a,x):return sum(v*x[0]**k[0]*x[1]**k[1]*x[2]**k[2] for k,v in a.items())
def require(c,m):
 if not c:raise ValueError(m)
def check(mode):
 one={(0,0,0):1};x={(1,0,0):1};y={(0,1,0):1};z={(0,0,1):1};xy=mul(x,y);u=add(one,xy);a=add(scale(one,4),scale(xy,3))
 F=[add(mul(pw(u,3),z),mul(mul(pw(y,2),u),a)),add(y,scale(mul(mul(x,pw(u,2)),z),3),scale(mul(mul(x,pw(y,2)),a),3)),add(scale(x,3 if mode=='changed-map' else 2),scale(mul(pw(x,2),y),-3),scale(mul(pw(x,3),z),-1))]
 determinant={}
 for p in permutations(range(3)):
  sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3));term=one
  for i in range(3):term=mul(term,der(F[i],p[i]))
  determinant=add(determinant,scale(term,sign))
 require(determinant==scale(one,-2),'determinant is not the constant -2')
 points=[(Q(0),Q(0),Q(-1,4)),(Q(1),Q(-3,2),Q(11 if mode=='changed-collision' else 13,2)),(Q(-1),Q(3,2),Q(13,2))]
 image=(Q(-1,4),Q(0),Q(0))
 require(len(set(points))==3,'collision points must be distinct')
 for p in points:require(tuple(val(f,p) for f in F)==image,'actual point fails collision')
 return {'status':'PASS','mode':mode,'degrees':[max(map(sum,f)) for f in F],'terms':[len(f) for f in F],'jacobian':'-2','distinct_collision_points':3,'image':['-1/4','0','0']}
if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'normal'
 if mode not in ('normal','changed-map','changed-collision'):raise ValueError('unknown mode')
 print(json.dumps(check(mode),sort_keys=True))
