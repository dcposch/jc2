#!/usr/bin/env python3
"""Audit hypothesis (H-int): p-integrality of the spine at P=(p, y-r), FROM THE
DENOMINATOR LIST of laurent_spine.py -- not from the absence of a div-by-0 marker.

Denominator list, read off laurent_spine.py line by line:
  (D-a) binom():        i, 1<=i<=k<=deg <= N=4t+1
  (D-b) integrate_s():  i, 1<=i<=deg+1 <= N+1
  (D-c) euler_inverse():yy*(2i-1), 1<=i<=deg+1        -> yy and odd ints <= 2N+1
  (D-d) Bp:             2*yy
  (D-e) Xp:             2*yy
  (D-f) rhsD:           2      (the 5/2)
  (D-g) g1,g2,g:        q, 2q^2, 6q^3
  (D-h) affine_solve(): the 2t+1 high pivots, plus b1coef (=y g) and B0coef (=q/y)
Usage: pintegral_check.py t p r rowsfile outfile
  r may be an integer (root of H_t mod p) or a rational a/b (split fibre).
"""
import re, sys
from fractions import Fraction

t, p = int(sys.argv[1]), int(sys.argv[2])
rspec, rows, outf = sys.argv[3], sys.argv[4], sys.argv[5]
q, e, N = 2*t+1, 3*t+1, 4*t+1
fr = Fraction(rspec)
def red(x):                      # Fraction -> GF(p), None if denominator dies
    if x.denominator % p == 0: return None
    return (x.numerator * pow(x.denominator, -1, p)) % p
r = red(fr)
fail = []
def chk(tag, val):
    if val is None: fail.append(tag + " :: DENOMINATOR DIVISIBLE BY p")
    elif val == 0:  fail.append(tag + " :: VANISHES mod P")

print("PINT t=%d p=%d y=%s (=%s mod p)" % (t, p, rspec, r))
# H_t(r) == 0 mod p
H = Fraction(12*q*q)*fr*fr - Fraction(12*q*(t+1))*fr + Fraction((t+1)*(3*t+2))
hv = red(H)
print("  H_t(y) mod P = %s   (must be 0)" % hv)
if hv != 0: fail.append("H_t(y) != 0 mod P")
# (D-a),(D-b),(D-c),(D-f): integers up to 2N+1
worst = 2*N+1
print("  fixed integer denominators: all i in [1,%d] and odd i in [1,%d]; p=%d > %d -> all units" % (N+1, 2*N+1, p, worst))
if p <= worst: fail.append("p <= 2N+1")
# (D-c),(D-d),(D-e): yy
chk("yy (y itself)", r)
print("  yy = %s" % r)
# (D-g)
for tag, v in (("q", q), ("2q^2", 2*q*q), ("6q^3", 6*q**3), ("2", 2)):
    chk(tag, v % p); print("  %-6s = %d mod p = %d" % (tag, v, v % p))
# g and c=-yg (b1 pivot is yy*g)
g  = Fraction(e*t, q*q)*fr - Fraction(e*t*(t+1), 6*q**3)
g1 = Fraction(e, q)
g2 = Fraction(e, q)*fr + Fraction(e*t, 2*q*q)
for tag, v in (("g1", g1), ("g2", g2), ("g", g), ("c=-y*g", -fr*g), ("b1coef=y*g", fr*g)):
    vv = red(v); chk(tag, vv); print("  %-11s = %-14s -> %s mod P" % (tag, v, vv))
chk("B0coef=q/y", red(Fraction(q)/fr) if fr != 0 else None)
# (D-h) the 2t+1 exact high pivots, reduced at y=r mod p
pat = re.compile(r"^PIVOT (\d+) (\S+) (\(([^()]+)\)|[^ ]+) ")
npv = 0
for line in open(rows):
    m = pat.match(line)
    if not m: continue
    band, var, coef = m.group(1), m.group(2), m.group(4) if m.group(4) else m.group(3)
    # coef is a linear form A*y+B over Q, printed by Singular
    cc = coef.replace("-", "+-").replace("e+-", "e-")
    A = Fraction(0); B = Fraction(0)
    for term in [s for s in cc.split("+") if s]:
        if term.endswith("*y"): A += Fraction(term[:-2])
        elif term == "y":       A += 1
        elif term == "-y":      A -= 1
        else:                   B += Fraction(term)
    val = A*fr + B
    vv = red(val)
    chk("pivot band=%s var=%s" % (band, var), vv)
    npv += 1
    print("  PIVOT band=%-3s var=%-7s exact=%-28s -> %s mod P" % (band, var, str(val), vv))
print("  pivots parsed: %d (expected %d)" % (npv, 2*t+1))
if npv != 2*t+1: fail.append("pivot count %d != %d" % (npv, 2*t+1))
print("PINT_RESULT t=%d p=%d y=%s : %s" % (t, p, rspec, "PASS (all denominators are P-units)" if not fail else "FAIL"))
for f in fail: print("  FAIL: " + f)
open(outf, "a").write("PINT t=%d p=%d y=%s %s\n" % (t, p, rspec, "PASS" if not fail else "FAIL " + "; ".join(fail)))
sys.exit(1 if fail else 0)
