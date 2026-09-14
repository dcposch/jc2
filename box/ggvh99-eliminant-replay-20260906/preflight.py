import sympy as S
from collections import defaultdict
a,b,c,u,v,w,z,t,k,l,m,T=S.symbols('a b c u v w z t k l m T')
D={3:S.Integer(1),1:a,0:b,-1:c,-2:u,-3:v,-4:w,-5:z,-6:t,-7:k,-8:l,-10:m}
def conv(A,B):
    out=defaultdict(lambda:S.Integer(0))
    for i,x in A.items():
        for j,y in B.items():out[i+j]+=x*y
    return {i:S.expand(x) for i,x in out.items()}
D2=conv(D,D);D3=conv(D2,D)
E=[D2[-i] for i in [1,2,3,4,5,7]]+[D3[-1],D3[-2],D3[-4]+T]
subs={}
for row,var in zip(E,[w,z,t,k,l,m]):
    r=S.expand(row.subs(subs))
    assert r.coeff(var)==2
    subs[var]=S.expand(-(r-2*var)/2)
for var,val in subs.items():print(var,'=',val)
R=[S.factor(x.subs(subs)) for x in E[6:]]
for i,r in enumerate(R):print('R',i,'=',r)
print('Resultant02',S.factor(S.resultant(R[0],R[2],v)))
print('Resultant01',S.factor(S.resultant(R[0],R[1],v)))
print('Resultant12',S.factor(S.resultant(R[1],R[2],v)))
