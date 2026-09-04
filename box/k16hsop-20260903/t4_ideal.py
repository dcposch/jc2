import json, sys, itertools, sympy as sp
y,b4,u2,u3,b3 = sp.symbols('y b4 u2 u3 b3')
t=4; q=2*t+1; p=1009
H = 12*q**2*y**2 - 12*q*(t+1)*y + (t+1)*(3*t+2)
roots=[r for r in range(p) if int(sp.Poly(H,y).eval(r))%p==0]
print("H_4 roots mod 1009:",roots,"(charged: 468, 990)",flush=True)
D=json.load(open('/home/ubuntu/jc2/box/k16hsop-20260903/tail_t4_rows.json'))
T={int(k):sp.sympify(v) for k,v in D['rows'].items()}
a={int(k):sp.sympify(v) for k,v in D['a'].items()}
a0=sp.sympify(D['a0'])
gens=(b4,u2,u3,b3)
def modp(e,yv):
    e=sp.together(sp.expand(e)); n,dd=sp.fraction(e)
    n=sp.Poly(sp.expand(n),*gens,y); dd=sp.expand(dd)
    dn=int(sp.Poly(dd,y).eval(yv))%p if dd.has(y) else int(dd)%p
    inv=pow(dn,p-2,p); out=0
    for mo,co in zip(n.monoms(),n.coeffs()):
        co=sp.Rational(co); cc=int(co.p)%p*pow(int(co.q)%p,p-2,p)%p
        cc=cc*pow(yv,mo[4],p)%p
        out+=cc*b4**mo[0]*u2**mo[1]*u3**mo[2]*b3**mo[3]
    return sp.expand(out*inv)
def vdim(polys,gens,yv,tag):
    ps=[f for f in (modp(g,yv) for g in polys) if f!=0]
    G=sp.groebner(ps,*gens,order='grevlex',modulus=p)
    lms=[sp.Poly(g,*gens,modulus=p).monoms(order='grevlex')[0] for g in G.exprs]
    n=len(gens); bnd=[]
    for i in range(n):
        c=[m[i] for m in lms if all(m[j]==0 for j in range(n) if j!=i) and m[i]>0]
        if not c: print(f"   [{tag}] NOT dim 0 (no pure power of {gens[i]})",flush=True); return None
        bnd.append(min(c))
    cnt=0
    for ex in itertools.product(*[range(b) for b in bnd]):
        if not any(all(ex[j]>=m[j] for j in range(n)) for m in lms): cnt+=1
    print(f"   [{tag}] dim=0 bounds={dict(zip([str(g) for g in gens],bnd))} vdim={cnt}",flush=True)
    return cnt
print("\ntail J=(T_4..T_7), predicted L_4 = 572",flush=True)
for yv in roots: vdim([T[4],T[5],T[6],T[7]],gens,yv,f"y={yv}")
print("\nJ == (Q_0,G_1,G_2,G_3) ?",flush=True)
Q0=T[7]; Gs=[sp.expand(a0*T[7-r]-a[r]*T[7]) for r in (1,2,3)]
for yv in roots[:1]:
    A=sp.groebner([modp(f,yv) for f in [T[4],T[5],T[6],T[7]]],*gens,order='grevlex',modulus=p)
    B=sp.groebner([modp(f,yv) for f in [Q0]+Gs],*gens,order='grevlex',modulus=p)
    print(f"   y={yv}: equal GB:",set(A.exprs)==set(B.exprs),
          " deg_b3(G_r):",[sp.Poly(g,b3).degree() for g in Gs],flush=True)
