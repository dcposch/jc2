#!/usr/bin/env python3
"""
PLACE-DICTIONARY CHECK.
Independent (Puiseux / Hamburger-Noether) computation of the places at infinity of
a GENERIC MEMBER of the net of a dominant map F=(P,Q), to test

      r_inf(C_gen) = D - T          and     D = sum_gamma nu_gamma ,
      nu_gamma = I(gamma, L_infty).

T values are taken from the published SAT-MASS sec.3 table (charged input) and from
MINIMAL-KELLER-SHAPE; this driver never computes a blow-up.
"""
import subprocess, sys, random
from sympy import symbols, Poly, expand, factor_list, QQ, total_degree, simplify, Rational

x,y,X,Y,Z = symbols('x y X Y Z')

def homog(g, D):
    g = expand(g)
    p = Poly(g, x, y)
    out = 0
    for (i,j),c in p.terms():
        out += c * X**i * Y**j * Z**(D-i-j)
    return expand(out)

def singular_branches(loc_eq, prec=30):
    """loc_eq: sympy expr in symbols a (transverse) and b (= the L_infty coordinate).
       returns (list of ord_t b(t) per branch, #branches, raw)."""
    s = str(loc_eq).replace('**','^')
    code = """LIB "hnoether.lib";
ring R = 0,(a,b),ds;
poly f = %s;
list L = hnexpansion(f);
if (typeof(L[1])=="ring") { def RR = L[1]; setring RR; list HN = hne; }
else { list HN = L; }
int i;
for (i=1; i<=size(HN); i++) {
   list PR = param(HN[i],1);
   ideal I = PR[1];
   printf("BRANCH %%s %%s", i, ord(I[2]));
   kill PR; kill I;
}
printf("NB %%s", size(HN));
quit;
""" % s
    import tempfile, os
    fh = tempfile.NamedTemporaryFile('w', suffix='.sing', delete=False); fh.write(code); fh.close()
    try:
        r = subprocess.run(['Singular','-q',fh.name], capture_output=True, text=True, timeout=60)
    finally:
        os.unlink(fh.name)
    out = r.stdout + r.stderr
    ords, nb = [], None
    for line in out.splitlines():
        t = line.split()
        if len(t)>=3 and t[0]=='BRANCH': ords.append(int(t[2]))
        if len(t)>=2 and t[0]=='NB': nb = int(t[1])
    return ords, nb, out

def places_at_infinity(g, verbose=False):
    D = total_degree(expand(g), x, y)
    gh = homog(g, D)
    lead = expand(gh.subs(Z,0))
    # roots of the leading form
    pl = Poly(lead, X, Y)
    # factor the binary form
    fl = factor_list(lead)
    pts = []
    for (fac,mult) in fl[1]:
        pf = Poly(fac, X, Y)
        if pf.total_degree() != 1:
            return None, f"non-linear factor over Q: {fac}"
        # fac = c1*X + c2*Y  -> point [X:Y] = [-c2 : c1]  (up to scale)
        c1 = pf.coeff_monomial(X); c2 = pf.coeff_monomial(Y)
        pts.append((-c2, c1))
    tot = []
    for (a0,b0) in pts:
        if b0 != 0:
            al = Rational(a0, b0)
            loc = expand(gh.subs({Y:1, X: X+al}))          # coords (X,Z), L_inf = {Z=0}
            loc = loc.subs({X: symbols('a'), Z: symbols('b')})
        else:
            loc = expand(gh.subs({X:1}))                   # coords (Y,Z)
            loc = loc.subs({Y: symbols('a'), Z: symbols('b')})
        ords, nb, raw = singular_branches(loc)
        if nb is None: return None, "singular failed: "+raw[:300]
        if len(ords)!=nb: return None, f"branch/ord mismatch {len(ords)} {nb}: "+raw[:300]
        tot.extend(ords)
    return (D, tot), None

BATTERY = [
  # (name, P, Q, published T, published D, published N)
  ("(x, y+x^2)",      x, y+x**2,          1, 2, 1),
  ("(x, y+x^3)",      x, y+x**3,          2, 3, 1),
  ("(x, y+x^4)",      x, y+x**4,          3, 4, 1),
  ("(x, y+x^6)",      x, y+x**6,          5, 6, 1),
  ("(x, xy)",         x, x*y,             0, 2, 1),
  ("(x, y^2)",        x, y**2,            1, 2, 2),
  ("(x, xy^2)",       x, x*y**2,          0, 3, 2),
  ("(x, x^2 y)",      x, x**2*y,          1, 3, 1),
  ("(x, x^2 y^2)",    x, x**2*y**2,       1, 4, 2),
  ("(x^2 y, y)",      x**2*y, y,          0, 3, 2),
  ("psi_2 o (x,xy^2)", x+ (x*y**2)**2, x*y**2,   3, 6, 2),
  ("psi_2 o (x,xy^3)", x+ (x*y**3)**2, x*y**3,   5, 8, 3),
  ("psi_3 o (x,xy^3)", x+ (x*y**3)**3, x*y**3,   8,12, 3),
  ("psi_4 o (x,xy^2)", x+ (x*y**2)**4, x*y**2,   7,12, 2),
  ("(x^3, y^2)",      x**3, y**2,         2, 3, 6),
  ("(x^2, y^3)",      x**2, y**3,         2, 3, 6),
]

if __name__ == "__main__":
    random.seed(11)
    print(f"{'map':22} {'D':>3} {'r_inf':>6} {'D-r_inf':>8} {'T(pub)':>7} {'nu list':>22}  ok")
    nfail=0
    for (name,P,Q,Tpub,Dpub,Npub) in BATTERY:
        try:
            pass
        except Exception: pass
        g = 5*P - 3*Q + 7          # generic member of the net
        try:
            res, err = places_at_infinity(g)
        except Exception as ex:
            print(f"{name:22} EXC {type(ex).__name__}", flush=True); nfail+=1; continue
        if res is None:
            print(f"{name:22} SKIP/ERR {err[:120]}", flush=True); nfail+=1; continue
        D, nus = res; D = int(D)
        r = len(nus); T = D - r
        ok = (D==Dpub) and (T==Tpub) and (sum(nus)==D)
        if not ok: nfail+=1
        print(f"{name:22} {D:3d} {r:6d} {T:8d} {Tpub:7d} {str(sorted(nus)):>22}  {'OK' if ok else 'FAIL'}", flush=True)
    print("\nfailures:", nfail)
