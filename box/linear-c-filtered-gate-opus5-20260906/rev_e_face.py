#!/usr/bin/env python3
"""Opus review Part E: highest face - supports, ranks, injectivity, radical/nilpotent."""
import json,math
from fractions import Fraction as F
import sympy as S
R=[];P=lambda *a:(R.append(" ".join(map(str,a))),print(*a))
d=json.load(open("/tmp/jc2-lane.1CmqE8/inputs/delta2_stage8.strongest.json"))
x,w,al,be,ga,eps=S.symbols("x w al be ga eps")
H=(x+w)**3*w**8; h3=H**3
jac=lambda f,g:S.diff(f,x)*S.diff(g,w)-S.diff(f,w)*S.diff(g,x)
# supports of the actual top rows
Ds=sorted({(34-int(z),int(z)) for r,z,e in d["maps"]["B2"] if int(r)==31})
Cs=sorted({(35-int(z),int(z)) for r,z,e in d["maps"]["A3"] if int(r)==63})
P("D top support (deg 34):",len(Ds),"X-exp",min(p[0] for p in Ds),"..",max(p[0] for p in Ds),"W-exp",min(p[1] for p in Ds),"..",max(p[1] for p in Ds))
P("C top support (deg 35):",len(Cs),"X-exp",min(p[0] for p in Cs),"..",max(p[0] for p in Cs),"W-exp",min(p[1] for p in Cs),"..",max(p[1] for p in Cs))
P("D top support contiguous:",Ds==[(34-z,z) for z in range(min(p[1] for p in Ds),max(p[1] for p in Ds)+1)])
P("C top support contiguous:",Cs==[(35-z,z) for z in range(min(p[1] for p in Cs),max(p[1] for p in Cs)+1)])
# exact source ranks onto these spaces
Dr=[S.sympify(e) for r,z,e in d["maps"]["B2"] if int(r)==31]
Cr=[S.sympify(e) for r,z,e in d["maps"]["A3"] if int(r)==63]
Dv=sorted(set().union(*(e.free_symbols for e in Dr)),key=str); Cv=sorted(set().union(*(e.free_symbols for e in Cr)),key=str)
rD=S.Matrix([[S.diff(e,n) for n in Dv] for e in Dr]).rank(); rC=S.Matrix([[S.diff(e,n) for n in Cr[0].free_symbols and Cv]] if 0 else [[S.diff(e,n) for n in Cv] for e in Cr]).rank()
P("rank D-top map =",rD,"(target dim",len(Ds),") surjective:",rD==len(Ds),"| params",len(Dv))
P("rank C-top map =",rC,"(target dim",len(Cs),") surjective:",rC==len(Cs),"| params",len(Cv))
P("D/C top parameter sets disjoint:",not set(Dv)&set(Cv))
P("D-top rows linear:",all(all(S.diff(e,n).is_number for n in Dv) for e in Dr),"| C-top rows linear:",all(all(S.diff(e,n).is_number for n in Cv) for e in Cr))
# face identity, degree-99 face from K + J(C,G)
D34,C35=S.symbols("D34 C35")
P("J(H^3,(3/4)d^2-2H^3 c) == (3/2)d J(H^3,d)+2H^3 J(c,H^3) :",
  S.expand(jac(h3,S.Rational(3,4)*S.Function('d')(x,w)**2-2*h3*S.Function('c')(x,w))
           -(S.Rational(3,2)*S.Function('d')(x,w)*jac(h3,S.Function('d')(x,w))+2*h3*jac(S.Function('c')(x,w),h3)))==0)
P("J(c,H^6) == 2H^3 J(c,H^3):",S.expand(jac(S.Function('c')(x,w),H**6)-2*h3*jac(S.Function('c')(x,w),h3))==0)
# injectivity of S_68 -> J(H^3,S): exact rank over Q, my own elimination
rows=[]
for j in range(69):
    p=S.Poly(S.expand(jac(x**(68-j)*w**j,h3)),x,w)
    rows.append([F(str(p.coeff_monomial(x**(99-k)*w**k))) for k in range(100)])
piv={};rk=0
for v in rows:
    v=list(v)
    for r0,pv in piv.items():
        if v[r0]: c=v[r0]; v=[a-c*b for a,b in zip(v,pv)]
    nz=[i for i,a in enumerate(v) if a]
    if nz: r0=nz[0]; piv[r0]=[a/v[r0] for a in v]; rk+=1
P("rank of S_68 -> J(H^3,S) =",rk,"of 69 -> injective:",rk==69,"| 11 divides 68:",68%11==0)
# parametrization
L=al*x*x+be*x*w+ga*w*w
Dp=x**2*(x+w)**5*w**25*L; Cp=S.Rational(3,8)*x**4*(x+w)*w**26*L**2
P("face identity for (Dp,Cp):",S.expand(S.Rational(3,4)*Dp**2-2*h3*Cp)==0)
P("Dp monomials inside D support:",set(S.Poly(S.expand(Dp),x,w).monoms())<=set(Ds))
P("Cp monomials inside C support:",set(S.Poly(S.expand(Cp),x,w).monoms())<=set(Cs))
P("Dp is LINEAR in (al,be,ga):",all(S.Poly(S.expand(Dp),x,w).total_degree()>=0 for _ in [0]) and all(S.degree(S.expand(Dp),g)<=1 for g in (al,be,ga)))
P("Cp is quadratic in (al,be,ga): degrees",[S.degree(S.expand(Cp),g) for g in (al,be,ga)])
# converse over a field: forced divisibility
gen=sum(S.Symbol(f"p{i}")*x**(7-i)*w**i for i in range(8))
Dg=x**2*w**25*gen
P("generic source d = X^2 W^25 * (deg-7 form):",set(S.Poly(S.expand(Dg),x,w).monoms())==set(Ds))
gc=sum(S.Symbol(f"q{i}")*x**(6-i)*w**i for i in range(7))
P("generic source c = X^3 W^26 * (deg-6 form):",set(S.Poly(S.expand(x**3*w**26*gc),x,w).monoms())==set(Cs))
# nilpotent counterexample
bad=x**9*w**25
P("bad d=X^9W^25 IS in the source D top space:",(9,25) in set(Ds))
P("(X+W)^5 does NOT divide X^9W^25:",S.rem(bad,(x+w)**5,x)!=0)
P("eps^2=0 makes (3/4)(eps*bad)^2-2H^3*0 == 0 :",S.expand(S.Rational(3,4)*(bad)**2*0)==0,"(eps^2 kills it)")
P("=> face ideal is NOT radical; parametrization is field-point/reduced only")
open("rev_e.out","w").write("\n".join(R)+"\n")
