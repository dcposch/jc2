import sympy as sp
from tree import analyse, Skip, x, y
def nu_topform(P,Q):
    dP,dQ = sp.Poly(P,x,y).total_degree(), sp.Poly(Q,x,y).total_degree(); D=max(dP,dQ)
    def lf(R,d):
        R=sp.Poly(R,x,y); return sum(c*x**i*y**j for (i,j),c in R.terms() if i+j==d)
    fs=[sp.Poly(lf(R,d),x,y) for R,d in ((P,dP),(Q,dQ)) if d==D]
    G=fs[0]
    for f in fs[1:]: G=G.gcd(f)
    Tv=sp.Symbol('T'); e=G.as_expr()
    if e.is_number: return 0
    g=sp.Poly(sp.expand(e.subs({x:1,y:Tv})),Tv)
    n=len([f for f,_ in sp.factor_list(g.as_expr(),Tv)[1]]) if g.degree()>0 else 0
    if g.degree()<sp.Poly(e,x,y).total_degree(): n+=1
    return n
chi=(x,y+x**2)
def comp(P,Q,c):
    return (sp.expand(P.subs({x:c[0],y:c[1]},simultaneous=True)),
            sp.expand(Q.subs({x:c[0],y:c[1]},simultaneous=True)))
M=[]
for k in (2,3,4,5,6): M.append(("(x,y+x^%d)"%k, x, y+x**k))
M += [("(x+y^2,y)",x+y**2,y), ("(x+(y+x^2)^3,y+x^2)", x+(y+x**2)**3, y+x**2), ("(y,-x)",y,-x),
      ("(x,y^2)",x,y**2),("(x,y^3)",x,y**3),("(x^2,y^2)",x**2,y**2),("(x^3,y^2)",x**3,y**2),("(x^2,y^3)",x**2,y**3),
      ("(x,xy)",x,x*y),("(xy,y)",x*y,y),("(x,xy^2)",x,x*y**2),("(x,x^2y)",x,x**2*y),
      ("(x,x^2y^2)",x,x**2*y**2),("(x,x^3y^2)",x,x**3*y**2),("(x^2y,y)",x**2*y,y),
      ("(x,x^2y^3)",x,x**2*y**3),("(x,x^3y^3)",x,x**3*y**3),("(x,x^3y^4)",x,x**3*y**4),
      ("(x,x^2y^4)",x,x**2*y**4),("(x,xy^3)",x,x*y**3),("(x,xy^4)",x,x*y**4),
      ("(xy^2,xy)",x*y**2,x*y),("(x^2y,xy)",x**2*y,x*y),("(x,x(x-1)(x-2)y^2)",x,x*(x-1)*(x-2)*y**2),
      ("mock(1,2;2,3)", x**2*y**4+x+y, x**3*y**6+x**2*y+1),
      ("mock(1,2;2,3)b", x**2*y**4+x*y+1, x**3*y**6+x*y**2+x),
      ("mock(2,3;2,3)", x**4*y**6+x*y+1, x**6*y**9+x*y**2+x),
      ("mock(2,3;2,3)b", x**4*y**6+x**2*y**2+x, x**6*y**9+x**3*y**3+y),
      ("mock(1,3;2,3)", x**2*y**6+x*y+1, x**3*y**9+x*y**2+x),
      ("mock(4,12;2,3)", x**8*y**24+x*y+1, x**12*y**36+x*y**2+x),
      ("mock(4,12;3,2)", x**12*y**36+x*y**2+x, x**8*y**24+x*y+1),
      ]
for k in (1,2,3):
    for m in (2,3,4):
        M.append(("psi_%d o (x,xy^%d)"%(k,m), x+(x*y**m)**k, x*y**m))
for k in (1,2,3):
    M.append(("G_%d"%k, x+(x*y**4-y**2)**k, x*y**4-y**2))
for nm,P,Q in [("(x,xy)",x,x*y),("(x,x^2y^2)",x,x**2*y**2),("(x,x^2y^3)",x,x**2*y**3)]:
    Pc,Qc=comp(P,Q,chi); M.append((nm+" o chi",Pc,Qc))
seen=set(); ok=0; skip=0; nu1=0; nu2=0; other=0; fails=[]
tcl_ok=0
for nm,P,Q in M:
    key=(sp.srepr(sp.expand(P)),sp.srepr(sp.expand(Q)))
    if key in seen: continue
    seen.add(key)
    try: r=analyse(P,Q)
    except Skip as e:
        skip+=1; continue
    Tp={l for l,d in r['divs'].items() if d['m']>0}
    dg0=sum(1 for o in r['divs']['E0']['adj'] if o in Tp)
    lev1=[cl for cl in r['cluster'] if cl['prox']==['E0']]
    w=sum(1 for cl in r['cluster'] if 'E0' in cl['prox'])
    nu=nu_topform(P,Q)
    c=[r['Zsq']==r['N'], r['ZK1']==r['ZK2'], r['okc'], r['sa2']==r['D']**2-r['N'],
       r['ZK1']==r['Psi']-r['Lam']-r['kappa'], r['ZK1']==r['Theta']-r['kappa']-r['Sn'],
       r['valE0']==nu, (nu<2) or (dg0==nu), (r['T']==r['Tclass'])==(w==len(lev1))]
    if all(c): ok+=1
    else: fails.append((nm,c))
    if nu==1: nu1+=1
    elif nu==2: nu2+=1
    else: other+=1
    if r['T']==r['Tclass']: tcl_ok+=1
print("distinct maps attempted:",len(seen)+skip, " resolved:",ok+len(fails), " skipped:",skip)
print("all-checks-pass:",ok," failures:",fails)
print("nu=1 rows:",nu1," nu=2 rows:",nu2," nu=0 rows:",other, " T==Tclass rows:",tcl_ok)
