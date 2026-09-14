#!/usr/bin/env python3
"""On the degenerate locus Lpivot = 4 eta + 3 b l_2 = 0 (eta = -(3/4) b l_2): which l_j is the leading unknown of
row k, and with what coefficient?  Also: the exceptional t=2 family P = -L^2/4 (B=eta=0, L+b = x^3/y) and (UF)."""
import sympy as sp, json, sys
K=10
x,b,B,eta,w2 = sp.symbols('x b B eta w2')
ls = {j: sp.Symbol(f'l{j}') for j in range(2,K+1)}
L = -b + sum(ls[j]*x**j for j in range(2,K+1))
G = sp.expand(sp.Rational(3,2)*L*(L+b) - B*x)
R = sp.expand(sp.Rational(3,16)*L**2*(L*(L+2*b)-4*B*x) - eta*x**2*(b*L/2+B*x))
Gc={k: G.coeff(x,k) for k in range(K+1)}; Rc={k: R.coeff(x,k) for k in range(K+1)}
P={0:-b**2/4,1:-B,2:eta,3:w2}
out={}
for k in range(4,K+1):
    br=(k-3)*sum(P[i]*P[k-i] for i in range(1,k))+sum(Gc[i]*P[k-i] for i in range(1,k+1))-Rc[k]
    P[k]=sp.cancel(br*2/((k-3)*b**2))
deg_sub={eta: -sp.Rational(3,4)*b*ls[2]}
for k in range(5,K+1):
    Pk=sp.cancel(P[k].subs(deg_sub))
    present=[j for j in range(2,K+1) if Pk.has(ls[j])]
    top=max(present)
    c=sp.factor(sp.diff(Pk, ls[top]))
    lin=sp.Poly(sp.numer(sp.together(Pk)), ls[top]).degree()
    out[f'k={k}']={'l_present':present,'top':top,'deg_in_top':lin,'coeff_of_top':str(c)}
# second-order pivot law guess: coefficient of l_{k-3} in Phi_k on the degenerate locus
print(json.dumps(out,indent=1))
# exceptional family check: t=2, N=3, y=1/5 (d=-1): L=-b+5x^3, B=eta=0, P=-L^2/4  satisfies (UF)?
Lx=-b+5*x**3; Px=-Lx**2/4
Gx=sp.Rational(3,2)*Lx*(Lx+b); Rx=sp.Rational(3,16)*Lx**2*(Lx*(Lx+2*b))
UF=sp.expand(x*sp.diff(Px**2,x)-3*Px**2+Gx*Px-Rx)
print('exceptional family (t=2,d=-1) P=-L^2/4 satisfies (UF):', UF==0)
# and P=-L^2/4 in general: (UF) reduces to L*(x L' - 3(L+b)) * (poly) ?
Lg=sp.Function('L')(x)
Pg=-Lg**2/4
Gg=sp.Rational(3,2)*Lg*(Lg+b); Rg=sp.Rational(3,16)*Lg**2*(Lg*(Lg+2*b))
UFg=sp.simplify(x*sp.diff(Pg**2,x)-3*Pg**2+Gg*Pg-Rg)
print('P=-L^2/4, B=eta=0: (UF) reduces to', sp.factor(UFg))
json.dump({'degenerate_locus':out,'exceptional_family_UF_zero':bool(UF==0),'P_eq_-L2/4_reduces_to':str(sp.factor(UFg))}, open('degenerate_pivot.json','w'), indent=1)
