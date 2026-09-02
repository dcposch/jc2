import sympy as sp
t,h,vv = sp.symbols('t h vv')
x = (149*t**2 - 785*t + 1100)/(t*(t-1)*(t-2)); y = (3*t - 13)/((t-3)*(t-4))
v = 1/y; z = x/y
def branch(b,n=8):
    sv = sp.expand(sp.series(v.subs(t,b+h),h,0,n).removeO())
    sz = sp.expand(sp.series(z.subs(t,b+h),h,0,n).removeO())
    # invert v = sv(h) as power series, h = sum c_k v^k
    c = sp.symbols('c1:%d'%n); H = sum(c[k-1]*vv**k for k in range(1,n))
    eq = sp.expand(sv.subs(h,H) - vv)
    sol={}
    for k in range(1,n):
        co = sp.expand(sp.series(eq.subs(sol),vv,0,k+1).removeO()).coeff(vv,k)
        s = sp.solve(co, c[k-1]); sol[c[k-1]] = sp.nsimplify(s[0].subs(sol) if s else 0)
        sol = {kk:sp.simplify(vvv.subs(sol)) for kk,vvv in sol.items()}
    Hs = sp.expand(H.subs(sol))
    return sp.expand(sp.series(sz.subs(h,Hs),vv,0,n-2).removeO())
p3 = branch(3); p4 = branch(4)
d = sp.expand(sp.nsimplify(p3-p4))
print("phi_3 - phi_4 =", d)
print("contact at [0:0:1] =", sp.Poly(d,vv).monoms()[-1][0] if d!=0 else 'inf')

# birationality: generic fibre of t -> (x,y)
X0,Y0 = sp.Rational(1,7), sp.Rational(2,5)
sols = sp.solve([sp.numer(sp.together(x-X0)), sp.numer(sp.together(y-Y0))], t)
print("fibre over a generic point:", sols)
