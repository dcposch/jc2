import sys
sys.path.insert(0,'/Users/dc/code/math/jc2/box/tfe-drivers-20260902')
from timefun import *
import sympy as sp

# ---------------- CONTROL 1: (f,g) = (y, x + y^k) --- charged control, closed form
print("== CONTROL 1: f = y, g = x + y^k  (charged) ==")
print("   %-3s %-8s %-30s %-22s %-10s" % ("k","J","x^{-1} coeff of J/g_y(tau)","F_i - f(x,tau_i)","interp"))
for k in range(2,8):
    f = y; g = x + y**k
    J = jac(f,g)
    # tau_i = zeta^i (c2 - x)^{1/k}
    zeta = sp.exp(2*sp.pi*sp.I/k)
    taus = [sp.simplify(zeta**i*(c2-x)**sp.Rational(1,k)) for i in range(k)]
    gy = sp.diff(g,y)
    ok_nolog = True; ok_time = True
    for i,tau in enumerate(taus):
        w = sp.simplify(J/gy.subs(y,tau))            # = df/dx along the branch
        # w is a constant times (c2-x)^{(1-k)/k}: exponent never -1 => NO x^{-1} term
        F = sp.simplify(sp.integrate(w, x))
        ok_time &= sp.simplify(sp.expand(F - tau)) == 0
    # exponent check for no-log: (1-k)/k - j = -1 has no integer solution j>=0
    ok_nolog = all((sp.Rational(1-k,k)+1).q != 1 for _ in [0])
    # interpolation: values f(x,tau_i)=tau_i at nodes tau_i -> interpolant is y itself
    L = sum(taus[i]*sp.prod([(y-taus[j])/(taus[i]-taus[j]) for j in range(k) if j!=i])
            for i in range(k))
    ok_int = sp.simplify(sp.expand(sp.simplify(L) - y)) == 0
    check("k=%d Keller"%k, J.free_symbols==set(), str(J))
    check("k=%d no-log"%k, ok_nolog)
    check("k=%d time function reproduces f"%k, ok_time)
    check("k=%d Lagrange interpolant = f = y (deg_y 1 = m < n = k)"%k, ok_int)
    print("   %-3d %-8s %-30s %-22s %-10s" % (k, J, "0 (exponent (1-k)/k is not integral)",
          "0 (a_i = 0)", "= y  OK" if ok_int else "FAIL"))
print("\n%d checks, %d failures" % (NCHK[0], len(FAIL)))
