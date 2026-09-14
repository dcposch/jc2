"""Own tiny exact controls for the 81-coordinate design. No source rows, no CAS."""
import ast,sys,json,resource
from fractions import Fraction as Q
from math import comb
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
MUT=sys.argv[1] if len(sys.argv)>1 else ''
def gate(ok,name):
    if not ok:print('FIRST_FAILING_GATE',name);sys.exit(1)
CLIENT=Path('/tmp/jc2-lane.pPWk5L/inputs/client.py')
tree=ast.parse(CLIENT.read_bytes())
VERT=ast.literal_eval(next(n.value for n in ast.walk(tree) if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='VERTICES'))
vA,vB=VERT['unequal']
def inside(v,i,j):  # own cross-product convex test, all edges counterclockwise
    e=list(zip(v,v[1:]+v[:1]));c=[(x2-x1)*(j-y1)-(y2-y1)*(i-x1) for (x1,y1),(x2,y2) in e]
    return all(x>=0 for x in c) or all(x<=0 for x in c)  # orientation-agnostic
def latt(v):
    return [(i,j) for i in range(30) for j in range(30) if inside(v,i,j)]
LA,LB=latt(vA),latt(vB)
gate((len(LA),len(LB))==(83,215),'raw lattice 83/215')
outerA=lambda i,j:i+j==15; innerA=lambda i,j:5*i-7*j==3
outerB=lambda i,j:i+j==25; innerB=lambda i,j:5*i-7*j==5
fixA=[p for p in LA if outerA(*p) or innerA(*p) or p==(0,0)]
fixB=[p for p in LB if outerB(*p) or innerB(*p) or p==(0,0)]
gate((len(fixA),len(fixB))==(12,19) and len(fixA)+len(fixB)==31,'31 fixed-map obligations')
freeA=[p for p in LA if p not in fixA]; freeB=[p for p in LB if p not in fixB]
oddA=[p for p in freeA if sum(p)%2]; oddB=[p for p in freeB if sum(p)%2]
gate((len(freeA),len(freeB),len(oddA),len(oddB))==(71,196,33,94),'free 71/196 odd 33/94')
gate(660+31+7+105==803,'803 literal contract')
# Hermite pivots: odd levels s<D, columns i<ceil(s/5); shifted at B level 15
def cols(s,D):
    c=list(range((s+4)//5))
    if D==25 and s==15:
        c=[0,1,2] if MUT=='pivot' else [1,2,3]
    return c
pivA=[(i,s-i) for s in range(1,15,2) for i in cols(s,15)]
pivB=[(i,s-i) for s in range(1,25,2) for i in cols(s,25)]
if MUT=='face':pivB[0]=(1,0)
gate((len(pivA),len(pivB))==(13,34),'pivot counts 13/34')
sheared=(0,15)  # [p^15]B, fixed 0 by the whole shear B->B-sA
gate(sheared in oddB and sheared not in pivB,'sheared slot free but not a pivot')
gate(all(p in oddA and not outerA(*p) and not innerA(*p) for p in pivA),'A pivots free, off both faces')
gate(all(p in oddB and not outerB(*p) and not innerB(*p) and p[0]+p[1]<25 and 5*p[0]-7*p[1]<5 for p in pivB),'B pivots free, off both faces')
gate(len(set(pivA))==13 and len(set(pivB))==34,'pivots distinct')
gate(33+94+2-13-34-1==81 and 20+59+2==81,'81 count')
# shifted level-15 matrix from the accepted diagonal law, own cofactor inverse
M=[[Q((-1)**(15-i-t)*comb(15-i,t)) for i in (1,2,3)] for t in range(3)]
gate(M==[[1,-1,1],[-14,13,-12],[91,-78,66]],'literal shifted matrix')
def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
d=det3(M);gate(d==-1,'det -1')
minor=lambda m,r,c:[[m[i][j] for j in range(3) if j!=c] for i in range(3) if i!=r]
det2=lambda m:m[0][0]*m[1][1]-m[0][1]*m[1][0]
adj=[[(-1)**(r+c)*det2(minor(M,c,r))/d for c in range(3)] for r in range(3)]
claimed=[[78,12,1],[168,25,2],[91,13,1]]
if MUT=='inverse':claimed[0][0]=79
gate(adj==claimed,'literal inverse equals own adjugate')
I=[[sum(M[r][k]*adj[k][c] for k in range(3)) for c in range(3)] for r in range(3)]
gate(I==[[1,0,0],[0,1,0],[0,0,1]] and all(x.denominator==1 for row in adj for x in row),'M*Minv=I integral')
M0=[[Q((-1)**(15-i-t)*comb(15-i,t)) for i in (0,1,2)] for t in range(3)]
gate(abs(det3(M0))==1,'accepted unshifted level-15 unimodular')
# 105 negative rows: 47 solved odd + 8 top + 50 wrong parity
rows=lambda D:[(D,s,t) for s in range(1,D+1) for t in range((s-1)//5+1)]
rA,rB=rows(15),rows(25);gate(len(rA)+len(rB)==105,'105 rows')
top=[r for r in rA+rB if r[1]==r[0]]
oddlow=[r for r in rA+rB if r[1]%2 and r[1]<r[0]]
even=[r for r in rA+rB if r[1]%2==0]
gate((len(top),len(oddlow),len(even))==(8,47,50),'105 = 8 top + 47 solved + 50 wrong parity')
gate(len(oddlow)==len(pivA)+len(pivB),'one pivot per solved odd row')
# affine maps and J monomial universe (k encoded as 99); degree bound
Amap=[(),(99,)]+[(i,) for i in range(20)]
Bmap=[(),(99,),(99,99)]+[(j,) for j in range(20,79)]
if MUT=='mapdegree':Amap[-1]=(0,1)   # a nonlinear (product) elimination term replaces a_19
gate(len(Amap)==22 and len(Bmap)==62,'affine supports 22/62')
U={tuple(sorted(x+y)) for x in Amap for y in Bmap}
gate(max(map(len,U))==3,'J degree <= 3')
gate(len(U)==1362 and 20*59+3*20+2*59+4==1362,'J universe 1362')
gate(not any(u.count(99)==2 and any(20<=v<99 for v in u) for u in U),'no k^2*b_j monomial')
dens=[Q(5,3),Q(5,9),Q(-5,9)]  # moving faces 5k/3, 5k^2/9 and target -5k^3/9
from math import lcm
gate(lcm(*[x.denominator for x in dens])==9 and all(x.denominator==1 for row in adj for x in row),'denominators divide 9')
# guard cofactors: (w-1)*(1+w+...+w^(r-1)) = w^r-1, w=kz, bidegree 2r
def pmul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():c[i+j]=c.get(i+j,0)+x*y
    return {i:x for i,x in c.items() if x}
for r in (1,2,3):
    series={j:1 for j in range(r)}
    if MUT=='guard' and r==3:series={0:1,1:1}
    gate(pmul({0:-1,1:1},series)=={0:-1,r:1},'guard cofactor r=%d'%r)
    gate(2*r in (2,4,6),'guard degree 2r')
gate(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_bytes()))),'zero Assert nodes')
print(json.dumps(dict(status='GATE_CONTROLS_PASS',optimized=not __debug__,mutation=MUT or None,
  lattice=[83,215],fixed=[12,19],free=[71,196],odd_free=[33,94],pivots=[13,34],variables=81,
  det=str(d),inverse=[[str(x) for x in r] for r in adj],rows105=[8,47,50],J_universe=1362,
  J_degree=3,positions=803,plus_unit=804,source_rows_evaluated=0),sort_keys=True))
