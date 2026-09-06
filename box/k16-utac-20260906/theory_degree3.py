import sympy as s
x,a,B,e,w=s.symbols('x a B e w')
L=-1+a*x**2+x**3
G=s.Rational(3,2)*L*(L+1)-B*x
R=s.Rational(3,16)*L**2*(L*(L+2)-4*B*x)-e*x**2*(L/2+B*x)
for lc in [s.Rational(-1,4),s.Rational(1,12)]:
    P=lc*x**6-s.Rational(1,4)
    params={}
    for k in range(11,6,-1):
        q=s.Symbol('q'+str(k-6)); P=P+q*x**(k-6)
        F=s.Poly(s.expand(x*s.diff(P**2,x)-3*P**2+G*P-R),x)
        sol=s.solve(F.coeff_monomial(x**k),q)[0]
        P=P.subs(q,sol);params[q]=s.factor(sol)
    jet=[P.subs(x,0)+s.Rational(1,4), s.diff(P,x).subs(x,0)+B, s.diff(P,x,2).subs(x,0)/2-e]
    eq=[s.factor(i) for i in jet]
    rem=s.Poly(s.expand(x*s.diff(P**2,x)-3*P**2+G*P-R),x)
    eq +=[s.factor(c) for c in rem.all_coeffs() if c]
    gb=s.groebner(eq,B,e,a,order='lex')
    
    sub=s.solve(jet,[B,e],dict=True)[0]
    univar=[s.factor(c.subs(sub)) for c in rem.all_coeffs() if c and c.subs(sub)!=0]
    print('REDUCED',univar,'gcd',s.factor(s.gcd_list(univar)))
    print('lc',lc,'P',s.factor(P),'coefficients',params,'jet',jet,'GB',list(gb), flush=True)
