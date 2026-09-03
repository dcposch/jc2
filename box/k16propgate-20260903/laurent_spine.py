#!/usr/bin/env python3
"""Emit a Singular replay of the proved Laurent/Euler spine (Sol 17(qqq) sections 5-6).

Usage: laurent_spine.py t [--fibre NUM] [--out FILE]

For irreducible H_t the coefficient field is Q(y)/(H_t) via minpoly.
For split t (t=3s^2-1) pass --fibre with the rational root of H_t; the run then
uses Q with y that rational number (one run per factor of the product algebra).

The script writes terminal rows T_{t,k}=[h^k](-R_h), k=0..2t-1 (the Sol sign
convention -E_t = R_s, i.e. T_{t,k} = [X^k] E_t), the pivot coefficients and
their inverses, as Singular-readable text.
"""
import argparse, sys
from fractions import Fraction

ap = argparse.ArgumentParser()
ap.add_argument("t", type=int)
ap.add_argument("--fibre", default=None, help="rational root of H_t for split t, e.g. 1/5")
ap.add_argument("--out", default=None)
ap.add_argument("--bands-only", action="store_true")
ap.add_argument("--modp", type=int, default=None, help="prime characteristic (needs --fibre)")
a = ap.parse_args()
t = a.t
q, e, N = 2*t+1, 3*t+1, 4*t+1
qv = ",".join("q(%d)" % j for j in range(2, 2*t+1))
cv = ",".join("C(%d)" % j for j in range(1, t)) if t >= 2 else ""
vars_ = "s,b1,b2,b3,b4,B0," + qv + ("," + cv if cv else "")
Hcoef = (12*q*q, -12*q*(t+1), (t+1)*(3*t+2))
L = []
if a.fibre is None:
    L.append('ring R=(0,y),(%s),dp;' % vars_)
    L.append('minpoly = %d*y^2%+d*y%+d;' % Hcoef)
    L.append('number yy = y;')
else:
    fr = Fraction(a.fibre)
    val = Fraction(Hcoef[0])*fr*fr + Fraction(Hcoef[1])*fr + Hcoef[2]
    if a.modp:
        if (val.numerator * pow(val.denominator, -1, a.modp)) % a.modp != 0:
            sys.exit("fibre %s is not a root of H_%d mod %d" % (a.fibre, t, a.modp))
    elif val != 0:
        sys.exit("fibre %s is not a root of H_%d" % (a.fibre, t))
    if a.modp:
        L.append('ring R=%d,(%s),dp;' % (a.modp, vars_))
    else:
        L.append('ring R=0,(%s),dp;' % vars_)
    L.append('number yy = number(%d)/%d;' % (fr.numerator, fr.denominator))
L.append('int t=%d; int q=%d; int e=%d; int N=%d;' % (t, q, e, N))
L.append('number g1 = number(%d)/%d;' % (e, q))
L.append('number g2 = (number(%d)/%d)*yy + number(%d)/%d;' % (e, q, e*t, 2*q*q))
L.append('number g = (number(%d)/%d)*yy - number(%d)/%d;' % (e*t, q*q, e*t*(t+1), 6*q**3))
L.append('number c = -yy*g;')
L.append('poly U = (s+b4)^q;')
for j in range(2, 2*t+1):
    L.append('U = U + q(%d)*(s+b4)^%d;' % (j, q-j))
L.append('poly Cp = (s+b4)^(t-1);')
for j in range(1, t):
    L.append('Cp = Cp + C(%d)*(s+b4)^%d;' % (j, t-1-j))
L.append(r'''
proc binom(int m, int k) { // exact binomial as number
  number r = 1; int i;
  for (i=1; i<=k; i++) { r = r*(m-k+i)/i; }
  return(r);
}
proc coefflist(poly f) { // list of coefficients of f in s: index m+1 -> [s^m]f
  int dg = deg(f, intvec(1,0,0,0,0,0''' + ",0"*(len(vars_.split(","))-6) + r'''));
  matrix M = coeffs(f, s);
  list Lc; int i;
  for (i=1; i<=nrows(M); i++) { Lc[i] = M[i,1]; }
  return(Lc);
}
proc integrate_s(poly f) { // antiderivative with zero constant
  list Lc = coefflist(f); poly r = 0; int i;
  for (i=1; i<=size(Lc); i++) { r = r + Lc[i]*s^i/i; }
  return(r);
}
proc euler_inverse(poly f, number yyv) { // solve yy*(1+2 s d/ds) S = f
  list Lc = coefflist(f); poly r = 0; int i;
  for (i=1; i<=size(Lc); i++) { r = r + (Lc[i]/(yyv*(2*(i-1)+1)))*s^(i-1); }
  return(r);
}
proc hband(poly f, int k) { // [h^k] f(h-b4) = sum_{m>=k} binom(m,k)(-b4)^(m-k)[s^m]f
  list Lc = coefflist(f); poly r = 0; int m;
  for (m=k; m<size(Lc); m++) { r = r + binom(m,k)*(-b4)^(m-k)*Lc[m+1]; }
  return(r);
}
proc affine_solve(poly row, poly v) { // returns list(coef, rhs) with row = coef*v + rem
  poly cf = diff(row, v);
  poly rem = subst(row, v, 0);
  if (row - cf*v - rem != 0) { ERROR("row not affine in variable"); }
  if (cf == 0) { ERROR("zero coefficient"); }
  if (deg(cf) != 0) { ERROR("coefficient not a scalar"); }
  number cn = leadcoef(cf);
  return(list(cn, -rem/cn));
}
''')
L.append('poly A = s*Cp;')
L.append('poly Bp = (g/(2*yy))*(5*Cp + 3*s*diff(Cp, s));')
L.append('poly B = B0 + integrate_s(Bp);')
L.append('if (diff(B,s) - Bp != 0) { ERROR("B recurrence"); }')
L.append('if (leadcoef(coeffs(B,s)[t+1,1]) - g2 != 0) { ERROR("B leading coefficient"); }')
L.append('poly rhsD = 3*g*diff(U,s) + A*B - s*A*diff(B,s) + 2*s*diff(A,s)*B + g*b3*(Cp + (5/2)*diff(A,s));')
L.append('poly D = euler_inverse(rhsD, yy);')
L.append('if (yy*(D + 2*s*diff(D,s)) - rhsD != 0) { ERROR("Euler inverse"); }')
L.append('if (leadcoef(coeffs(D,s)[2*t+1,1]) - g1 != 0) { ERROR("D leading coefficient"); }')
L.append('poly V = s*A - yy*b3;')
L.append('poly Y = s*D - b3*B - g*b2;')
L.append('poly Z = s*B - g*b3;')
L.append('poly num = yy*g*b1 - V*diff(Y,s) + diff(V,s)*Y + 2*diff(U,s)*Z;')
L.append('poly num0 = subst(num, s, 0);')
L.append('list sb1 = affine_solve(num0, b1);')
L.append('number b1coef = sb1[1]; poly b1rhs = sb1[2];')
L.append('num = subst(num, b1, b1rhs);')
L.append('if (subst(num, s, 0) != 0) { ERROR("not divisible by s"); }')
L.append('poly Xp = (num/s)/(2*yy);')
L.append('if (leadcoef(coeffs(Xp,s)[3*t+1,1]) - e != 0) { ERROR("Xp leading"); }')
L.append('poly gauge = hband(Xp, q-1);')
L.append('list sB0 = affine_solve(gauge, B0);')
L.append('number B0coef = sB0[1]; poly B0rhs = sB0[2];')
L.append('B = subst(B, B0, B0rhs); D = subst(D, B0, B0rhs); Y = subst(Y, B0, B0rhs); Z = subst(Z, B0, B0rhs); Xp = subst(Xp, B0, B0rhs); b1rhs = subst(b1rhs, B0, B0rhs);')
L.append('if (hband(Xp, q-1) != 0) { ERROR("gauge"); }')
L.append('poly Rs = V*Xp - diff(U,s)*Y - yy*g;')
L.append('list rows; int k; for (k=0; k<=N; k++) { rows[k+1] = hband(Rs, k); }')
L.append('if (rows[N+1] != 0) { ERROR("top band nonzero"); }')
L.append('list pivots; int j; poly pv; list sol; int band; int i;')
L.append('for (j=1; j<=2*t+1; j++) {')
L.append('  band = N - j;')
L.append('  if (j <= t-1) { pv = C(j); } else { if (j <= 2*t) { pv = q(j); } else { pv = b2; } }')
L.append('  sol = affine_solve(rows[band+1], pv);')
L.append('  pivots[j] = list(band, pv, sol[1], sol[2]);')
L.append('  for (i=1; i<=N+1; i++) { rows[i] = subst(rows[i], pv, sol[2]); }')
L.append('  if (rows[band+1] != 0) { ERROR("pivot substitution"); }')
L.append('  b1rhs = subst(b1rhs, pv, sol[2]); B0rhs = subst(B0rhs, pv, sol[2]);')
L.append('}')
L.append('for (k=2*t; k<=N; k++) { if (rows[k+1] != 0) { ERROR("high band survives"); } }')
L.append('print("SPINE_OK t=" + string(t));')
L.append('list PV; poly Tk; for (j=1; j<=2*t+1; j++) { PV = pivots[j]; print("PIVOT band=" + string(PV[1]) + " var=" + string(PV[2]) + " coef=" + string(PV[3])); }')
L.append('print("B1COEF=" + string(b1coef)); print("B0COEF=" + string(B0coef));')
L.append('for (k=0; k<2*t; k++) { Tk = rows[k+1]; Tk = -Tk; print("TERMINAL band=" + string(k) + " T=" + string(Tk)); }')
if a.out:
    L.append('write(":w %s", "// terminal rows T_{t,k} = -[h^k]R_h, t=%d");' % (a.out, t))
    L.append('for (k=0; k<2*t; k++) { Tk = rows[k+1]; Tk = -Tk; write(":a %s", "T" + string(k) + " = " + string(Tk) + ";"); }' % a.out)
    L.append('write(":a %s", "B1RHS = " + string(b1rhs) + ";");' % a.out)
    L.append('write(":a %s", "B0RHS = " + string(B0rhs) + ";");' % a.out)
    L.append('for (j=1; j<=2*t+1; j++) { PV = pivots[j]; write(":a %s", "PIVOT " + string(PV[1]) + " " + string(PV[2]) + " " + string(PV[3]) + " " + string(PV[4]) + ";"); }' % a.out)
L.append('quit;')
print("\n".join(L))
