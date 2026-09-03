import sympy as sp
x,y,c=sp.symbols('x y c')
def check(f,g,name):
    n=sp.degree(sp.Poly(g,y),y); m=sp.degree(sp.Poly(f,y),y)
    J=sp.simplify(sp.diff(f,x)*sp.diff(g,y)-sp.diff(f,y)*sp.diff(g,x))
    R=sp.Poly(sp.resultant(sp.expand(g-c),f,y),x)
    # branch orders: Puiseux exponents of f(x,tau_i(x)) via Newton polygon of Res in 1/x
    print(f"{name}: n={n} m={m} J={J}  deg_x Res_y(g-c,f) = {R.degree()}")
    # trace control: P_1 = Tr(f) must be constant in x (Sum_i 1/g_y(tau_i)=0 for n>=2)
    P1=sp.simplify(sp.expand(-sp.Poly(sp.resultant(sp.expand(g-c),sp.Symbol('T')-f,y),sp.Symbol('T')).coeffs()[1]))
    print(f"   Tr(f) = {sp.simplify(P1)}   -> d/dx = {sp.simplify(sp.diff(P1,x))}")
    for k in (2,3,4):
        # d/dx P_k  vs  k*[y^{n-1}](f^{k-1} mod (g-c))
        red=sp.rem(sp.Poly(sp.expand(f**(k-1)),y),sp.Poly(sp.expand(g-c),y))
        rhs=sp.simplify(k*red.coeff_monomial(y**(n-1)))
        T=sp.Symbol('T')
        cp=sp.Poly(sp.resultant(sp.expand(g-c),T-f,y),T)
        roots_pow=sp.simplify(sp.expand(sum(sp.Poly(cp).all_coeffs()[0]*0 for _ in [0])))
        # P_k by Newton's identity from char poly coefficients
        co=[sp.simplify(cc) for cc in cp.all_coeffs()]; co=[sp.simplify(cc/co[0]) for cc in co]
        e=[(-1)**i*co[i] for i in range(len(co))]   # e_0..e_n  (e_i = elementary symm)
        P=[sp.Integer(n)]
        for kk in range(1,k+1):
            s=sum((-1)**(i-1)*e[i]*P[kk-i] for i in range(1,kk))
            P.append(sp.simplify(s+(-1)**(kk-1)*kk*e[kk]))
        lhs=sp.simplify(sp.diff(P[k],x))
        print(f"   k={k}: d/dx P_k = {lhs} ;  k*[y^(n-1)](f^(k-1) mod g-c) = {rhs} ; equal up to sign: {sp.simplify(lhs-rhs)==0 or sp.simplify(lhs+rhs)==0}")
check(y, x+y**2, "AUT f=y,g=x+y^2")
check(y+x**2, x+ (y+x**2)**2 + y, "AUT-2")
