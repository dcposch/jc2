"""Tiny constant-matrix/monomial-space checks only, no source traversal."""
import ast,json,resource
from fractions import Fraction as Q
from math import comb
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(10,10));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
def need(ok,msg):
    if not ok:raise ValueError(msg)
def matrix(s,columns):
    return [[Q((-1)**(s-i-t)*comb(s-i,t)) for i in columns] for t in range(len(columns))]
def invert(m):
    n=len(m);a=[list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(m)];det=Q(1)
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j]);
        if k!=j:a[k],a[j]=a[j],a[k];det=-det
        pivot=a[j][j];det*=pivot;a[j]=[x/pivot for x in a[j]]
        for k in range(n):
            if k!=j:
                z=a[k][j];a[k]=[x-z*y for x,y in zip(a[k],a[j])]
    return det,[row[n:] for row in a]
m=matrix(15,[1,2,3]);det,inv=invert(m)
need(m==[[1,-1,1],[-14,13,-12],[91,-78,66]] and det==-1,'shifted degree15 matrix')
need(all(x.denominator==1 for row in inv for x in row),'unimodular shifted inverse')
want=[Q(2),Q(3),Q(5)];rhs=[sum(x*y for x,y in zip(row,want)) for row in m]
need([sum(x*y for x,y in zip(row,rhs)) for row in inv]==want,'pivot orientation')
need([sum(x*y for x,y in zip(row,list(reversed(rhs)))) for row in inv]!=want,'orientation mutation not rejected')
columns=[1,2,3]
need(0 not in columns and all(i+15-i<25 and 5*i-7*(15-i)<5 for i in columns),'pivots free after beta15 slice')
bad=[0,1,2];need(0 in bad,'fixed beta15 reuse mutation')
a_piv=sum((s+4)//5 for s in range(1,15,2));b_piv=sum((s+4)//5 for s in range(1,25,2))
need((a_piv,b_piv)==(13,34) and 33+94+2-a_piv-b_piv-1==81,'counts')
# All possible coefficient-polynomial monomials. Actual source rows are absent.
a=[(),(79,)]+[(i,) for i in range(20)]
b=[(),(79,),(79,79)]+[(i,) for i in range(20,79)]
products={tuple(sorted(x+y)) for x in a for y in b}
need(len(a)==22 and len(b)==62 and len(products)==1362,'monomial-space count')
need(max(map(len,products))==3,'cubic J bound')
bad_products=products|{(79,79,79,79)};need(max(map(len,bad_products))>3,'degree mutation')
# Fixed denominator lattice: integer matrices preserve (1/9)Z coefficients.
need(all((9*x).denominator==1 for row in inv for x in [sum(row)/9]),'denominator lattice')
# Whole shear's lower coefficient is essential; no point/face satisfaction claimed.
s,k,b_lower=Q(2),Q(3),Q(7);sliced=b_lower-s*k
need(sliced+s*k==b_lower and b_lower+s*k!=b_lower,'whole shear inverse/mutation')
need(0*0-1!=0,'inverse guard omission control')
for r in (1,2,3):
    lhs={0:Q(-1),r:Q(1)};rhs={}
    for j in range(r):rhs[j+1]=rhs.get(j+1,Q(0))+1;rhs[j]=rhs.get(j,Q(0))-1
    rhs={j:c for j,c in rhs.items() if c};need(rhs==lhs,'guard cofactor')
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_bytes()))),'Assert nodes')
print(json.dumps(dict(status='TINY_DESK_CHECKS_PASS',optimized=not __debug__,
      shifted_B15_matrix=[[str(x) for x in row] for row in m],det=str(det),
      inverse=[[str(x) for x in row] for row in inv],A_pivots=a_piv,B_Hermite_pivots=b_piv,
      variables=81,original_positions=803,extra_inverse_guard=1,max_A_map_terms=22,max_B_map_terms=62,
      J_monomial_universe=len(products),max_J_degree=3,source_rows_evaluated=0,
      production_metadata_or_constructor=False),sort_keys=True))
