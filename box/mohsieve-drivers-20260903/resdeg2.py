import sympy as sp
x,y,c,T=sp.symbols('x y c T')
def check(f,g,name,kmax=4):
    gp=sp.Poly(sp.expand(g-c),y); n=gp.degree(); m=sp.Poly(f,y).degree()
    J=sp.simplify(sp.diff(f,x)*sp.diff(g,y)-sp.diff(f,y)*sp.diff(g,x))
    R=sp.Poly(sp.resultant(sp.expand(g-c),f,y),x)
    cp=sp.Poly(sp.resultant(sp.expand(g-c),T-f,y),T)
    co=cp.all_coeffs(); co=[sp.simplify(a/co[0]) for a in co]      # monic: T^n + co1 T^{n-1}+...
    e=[sp.Integer(1)]+[sp.simplify((-1)**i*co[i]) for i in range(1,n+1)]+[sp.Integer(0)]*(kmax+2)
    P=[sp.Integer(n)]
    for k in range(1,kmax+1):
        s=sum((-1)**(i-1)*e[i]*P[k-i] for i in range(1,k))
        P.append(sp.simplify(s+((-1)**(k-1))*k*e[k]))
    print(f"{name}: n={n} m={m} J={J}  deg_x Res_y(g-c,f)={R.degree()}  Tr(f)=P_1={sp.simplify(P[1])}")
    for k in range(2,kmax+1):
        red=sp.rem(sp.Poly(sp.expand(f**(k-1)),y),gp)
        rhs=sp.simplify(k*red.coeff_monomial(y**(n-1)))
        lhs=sp.simplify(sp.diff(P[k],x))
        agree = sp.simplify(lhs-J*rhs)==0
        print(f"   k={k}: dP_k/dx={lhs}  |  k*[y^{n-1}](f^(k-1) mod g-c)={rhs}  | dP_k/dx = J*rhs : {agree}")
check(y, x+y**2, "AUT f=y, g=x+y^2")
check(y+x**3, x + (y+x**3)**2, "AUT f=y+x^3, g=x+f^2", kmax=3)
check(y, x+y**3+y**2, "AUT f=y, g=x+y^3+y^2", kmax=4)
