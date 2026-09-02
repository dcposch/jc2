import sympy as sp
t = sp.symbols('t')
x = (149*t**2 - 785*t + 1100)/(t*(t-1)*(t-2))
y = (3*t - 13)/((t-3)*(t-4))

# 1. cusp type at t=5
h = sp.symbols('h')
sx = sp.series(x.subs(t,5+h)-15, h, 0, 6).removeO()
sy = sp.series(y.subs(t,5+h)-1 , h, 0, 6).removeO()
print("x-15 =", sp.nsimplify(sp.expand(sx)))
print("y-1  =", sp.nsimplify(sp.expand(sy)))
ordx = sp.Poly(sp.expand(sx),h).monoms()[-1][0]; ordy = sp.Poly(sp.expand(sy),h).monoms()[-1][0]
print("orders:", ordx, ordy)
# eliminate the tangent direction: combination with order 3
c2x = sp.expand(sx).coeff(h,2); c2y = sp.expand(sy).coeff(h,2)
comb = sp.expand(c2y*sx - c2x*sy)
print("tangent-killed combination order:", sp.Poly(comb,h).monoms()[-1][0])
print(" -> branch semigroup generators (2,3)?", (ordx==2 and ordy==2 and sp.Poly(comb,h).monoms()[-1][0]==3))

# 2. structure at infinity.  chart u=1/x, w=y/x  (point [0:1:0], branches t=0,1,2)
u = sp.simplify(1/x); w = sp.simplify(y/x)
for a in (0,1,2):
    su = sp.series(u.subs(t,a+h),h,0,5).removeO(); sw = sp.series(w.subs(t,a+h),h,0,5).removeO()
    print("t=%d : ord(u)=%s ord(w)=%s  w/u ->"%(a,sp.Poly(sp.expand(su),h).monoms()[-1][0],
          sp.Poly(sp.expand(sw),h).monoms()[-1][0]), sp.nsimplify(sp.limit(w,t,a)))
# pairwise contact of the three branches at [0:1:0]: distinct tangents -> contact 1 each
# 3. chart v=1/y, z=x/y  (point [0:0:1], branches t=3,4)
v = sp.simplify(1/y); z = sp.simplify(x/y)
ser={}
for b in (3,4):
    sv = sp.expand(sp.series(v.subs(t,b+h),h,0,6).removeO()); sz = sp.expand(sp.series(z.subs(t,b+h),h,0,6).removeO())
    print("t=%d : ord(v)=%s ord(z)=%s  z/v ->"%(b,sp.Poly(sv,h).monoms()[-1][0],sp.Poly(sz,h).monoms()[-1][0]), sp.nsimplify(sp.limit(z,t,b)))
    # write branch as z = phi(v): invert v(h) then substitute
    vv = sp.symbols('vv')
    hs = sp.series(sp.solve(sp.series(sv,h,0,6).removeO()-vv,h)[0] if False else 0,)
    ser[b]=(sv,sz)
