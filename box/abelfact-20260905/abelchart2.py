"""Reduced (F3') chart, dehomogenised at b=1 (legitimate: the identity is
weighted-homogeneous with wt(b)=t+1, wt(B)=2t+1, wt(eta)=2t, wt(phi_3)=2t-1,
wt(c_i)=t-1-i  -- exactly the frozen grading wt(b4,u2..u_{t-1},b3)=(1,2,..,t-1,t+1)
with c_{t-1-j}=u_j, c_{t-2}=b4, b=b3).  b=0 is a separate branch.
Field: A_t = Q(d), d^2=(t+1)/3,  y=(d+t+1)/(2q), q=2t+1.
Emits a Singular file with the residual system + Rabinowitsch on B*eta.
"""
import sys, sympy as sp

t = int(sys.argv[1]); q = 2*t+1; N = 4*t+4
x, d = sp.symbols('x w')
D2 = sp.Integer(3*(t+1))                       # w^2 = 3(t+1),  w = 3d

def red(e):
    """reduce a polynomial in d modulo d^2 - (t+1)/3"""
    p = sp.Poly(sp.expand(e), d)
    a = sp.Rational(0); c = sp.Rational(0)
    for (k,), co in p.terms():
        if k % 2 == 0: a += co*D2**(k//2)
        else:          c += co*D2**((k-1)//2)
    return sp.nsimplify(a) + sp.nsimplify(c)*d

def finv(e):
    """inverse in Q(d)"""
    e = red(e); a = e.coeff(d, 0); c = e.coeff(d, 1)
    nrm = sp.nsimplify(a**2 - c**2*D2)
    assert nrm != 0, "zero divisor in A_t"
    return red((a - c*d)/nrm)

y  = red((d + 3*(t+1))/(6*q))   # y = (d_alg+t+1)/(2q) with d_alg=w/3
iy = finv(y); iy2 = red(iy*iy); iy4 = red(iy2*iy2)
B, eta, f3 = sp.symbols('B eta f3')
c = sp.symbols('c0:%d' % max(t-1, 1))
C = sum(c[i]*x**i for i in range(t-1)) + x**(t-1)
K = sp.expand(x**2*C - y)          # b = 1
M = sp.expand(x**2*C)
KM = sp.expand(K*M)
Gee = sp.expand(sp.Rational(3,16)*iy4*K**3*(K+2*y)
                - sp.Rational(3,4)*iy2*B*x*K**2
                - sp.Rational(1,2)*iy*eta*x**2*K
                - B*eta*x**3)

def redall(p):
    p = sp.expand(p)
    out = 0
    for mono, co in sp.Poly(p, *( (x, B, eta, f3) + tuple(c) )).terms():
        m = x**mono[0]*B**mono[1]*eta**mono[2]*f3**mono[3]
        for i, e in enumerate(mono[4:]): m *= c[i]**e
        out += red(co)*m
    return sp.expand(out)

Gee = redall(Gee)
gc  = [sp.expand(Gee.coeff(x, n)) for n in range(N+1)]
kmc = [sp.expand(KM.coeff(x, n)) for n in range(N+1)]
c32 = red(sp.Rational(3,2)*iy2)

phi = {0: sp.Rational(-1,4), 1: -B, 2: eta, 3: f3}
for n in range(4, N+1):
    known = sp.expand(sum(phi[i]*phi[n-i] for i in range(1, n)))
    rhs = gc[n] + B*phi[n-1] - c32*sum(kmc[j]*phi[n-j] for j in range(2, min(n, len(kmc)-1)+1))
    phi[n] = redall(sp.expand((sp.expand(rhs)/sp.Integer(n-3) - known)/(2*phi[0])))

eqs = [phi[n] for n in range(2*t+3, N+1)]
nz  = [e for e in eqs if e != 0]
print("t=%d  unknowns=%d (B,eta,f3,%s)  equations=%d (nonzero %d)"
      % (t, t+2, ','.join(map(str, c[:t-1])), len(eqs), len(nz)))
for i, e in enumerate(eqs):
    print("   n=%2d  terms=%4d  totdeg=%s" % (2*t+3+i, len(sp.Poly(e, *((B,eta,f3)+tuple(c))).terms()) if e!=0 else 0,
          sp.Poly(e, *((B,eta,f3)+tuple(c))).total_degree() if e!=0 else '-'))

def sing_terms(e, gens):
    """print with integer coefficients: clear denominators, coeffs are a+b*d."""
    pe = sp.Poly(sp.expand(e), *gens)
    dens = []
    for _, co in pe.terms():
        co = sp.expand(co)
        for part in (co.coeff(d,0), co.coeff(d,1)):
            dens.append(sp.denom(sp.nsimplify(part)))
    L = sp.ilcm(*[int(x) for x in dens]) if dens else 1
    out = []
    for mono, co in pe.terms():
        co = sp.expand(co*L)
        a = sp.nsimplify(co.coeff(d,0)); c1_ = sp.nsimplify(co.coeff(d,1))
        cs = "(%s+(%s)*w)" % (a, c1_)
        m = "*".join("%s^%d" % (g, k) for g, k in zip(gens, mono) if k)
        out.append(cs + ("*"+m if m else ""))
    return "+".join(out).replace("+-", "-")

gens = (B, eta, f3) + tuple(c[:t-1])
vs = [str(g) for g in gens]
with open('/home/ubuntu/jc2/box/abelfact-20260905/t%d.sing' % t, 'w') as fh:
    fh.write('ring R=(0,w),(%s,zz),dp;\nminpoly=w^2-%d;\n' % (','.join(vs), 3*(t+1)))
    fh.write('ideal I=' + ',\n'.join(sing_terms(e, gens) for e in nz) + ';\n')
    fh.write('ideal J=I, 1-zz*%s*%s;\n' % ('B','eta'))
    fh.write('option(redSB); int tm=timer;\n')
    fh.write('ideal g=groebner(J);\n')
    fh.write('"RABINOWITSCH(B*eta): size="+string(size(g))+"  isunit="+string(size(g)==1 && g[1]==1)+"  ms="+string(timer-tm);\n')
    fh.write('tm=timer; ideal g2=groebner(I);\n')
    fh.write('"RAW: dim="+string(dim(std(g2)))+"  size="+string(size(g2))+"  ms="+string(timer-tm);\n')
    fh.write('quit;\n')
print("wrote t%d.sing" % t)
