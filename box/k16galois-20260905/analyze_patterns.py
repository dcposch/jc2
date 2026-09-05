#!/usr/bin/env python3
"""Parse pattern_t{t}_mod_p{p}_b{b}.out files: per prime ideal, the Frobenius cycle type of the
q2-minpoly of Gamma_t ∩ {b4=1}; check the hypotheses (vdim = expected, deg minpoly = vdim, squarefree,
no FAIL/error markers); intersect subset sums over all good primes."""
import re, glob, sys, itertools, collections
t = int(sys.argv[1]); expected = int(sys.argv[2])
files = sorted(glob.glob(f"pattern_t{t}_mod_p*_b*.out"))
allsums = None; good = 0; rows = []; W = collections.Counter(); types = collections.Counter()
for f in files:
    txt = open(f).read(); err = open(f.replace('.out','.err')).read()
    m = re.search(r"prime=(\d+) branch=(\d+)", txt); p, b = int(m.group(1)), int(m.group(2))
    bad = ("FAIL" in txt) or ("error" in txt) or ("div. by 0" in txt) or ("div. by 0" in err) or ("error" in err)
    vd = re.search(r"MAIN vdim=(\d+) dim=(\d+)", txt)
    mp = re.search(r"MAIN minpoly var=q2_0 ordinary_degree=(\d+) squarefree=(\d)", txt)
    pat = re.search(r"MAIN PATTERN((?: \d+\^\d+)+)", txt)
    cone = re.search(r"CONE I2: dim=(\d+)", txt); sl = re.search(r"SLICE b4=0 cone: dim=(\d+)", txt)
    wnz = re.search(r"MAIN W_NONZERO_AT_POINT=(\d)", txt)
    jr = re.search(r"MAIN JACRANK_FREE=(\d+) expected=(\d+)", txt)
    done = "PATTERN_DONE" in txt
    ok = (not bad) and done and vd and int(vd.group(1)) == expected and int(vd.group(2)) == 0 and mp and int(mp.group(1)) == expected and mp.group(2) == '1' and pat
    if cone and cone.group(1) != '1': ok = False
    cyc = []
    if pat:
        for d, e in re.findall(r"(\d+)\^(\d+)", pat.group(1)):
            cyc += [int(d)] * int(e)
    cyc.sort()
    rows.append((p, b, ok, vd.group(1) if vd else None, mp.groups() if mp else None, cyc, cone.group(1) if cone else '-', sl.group(1) if sl else '-', wnz.group(1) if wnz else '-', jr.groups() if jr else None, bad, done))
    if ok:
        good += 1
        types[tuple(cyc)] += 1
        sums = {0}
        for c in cyc: sums |= {s + c for s in sums}
        allsums = sums if allsums is None else (allsums & sums)
        if wnz: W[wnz.group(1)] += 1
print(f"t={t} expected n={expected}: files={len(files)} good primes={good}")
for r in rows:
    print(f"  p={r[0]} b={r[1]} ok={r[2]} vdim={r[3]} minpoly(deg,sqf)={r[4]} cone_dim={r[6]} slice_dim={r[7]} Wnz={r[8]} jac={r[9]} bad={r[10]} done={r[11]}  cycle={r[5]} sum={sum(r[5])}")
print(f"INTERSECTION of proper subset sums over {good} good primes: {sorted(s for s in (allsums or set()) if 0 < s < expected)}")
print("IRREDUCIBLE over A_t by the degree-pattern argument:", (allsums is not None) and all(not (0 < s < expected) for s in allsums))
print("W nonzero at the found rational point (counts):", dict(W))
print("distinct cycle types:", len(types))
# prime cycles present (for Jordan-type statements)
primes_cycles = set()
for cyc in types:
    L = 1
    for c in cyc: L = L * c // __import__('math').gcd(L, c)
    for c in set(cyc):
        # power of the element that is a pure c-cycle product: sigma^(L/c) restricted... report prime cycle lengths c that appear with multiplicity 1 and coprime to all others
        others = [d for d in cyc if d != c]
        if cyc.count(c) == 1 and all(c % 1 == 0 and __import__('math').gcd(c, d) == 1 or d % c != 0 for d in others):
            pass
    primes_cycles |= {c for c in cyc if __import__('sympy').isprime(c) and cyc.count(c) == 1 and all(d % c != 0 for d in cyc if d != c)}
print("prime lengths c such that some Frobenius power is a pure c-cycle:", sorted(primes_cycles))
# ---- Galois-group bookkeeping: parity and Jordan-type criteria ----
import math
def parity(cyc): return sum(c - 1 for c in cyc) % 2
odd = [cyc for cyc in types if parity(cyc) == 1]
print("odd permutations present:", len(odd) > 0, "(e.g.", (odd[0] if odd else None), ")")
n = expected
jordan = sorted(c for c in primes_cycles if n/2 < c <= n - 3)
print(f"prime cycle lengths c with n/2 < c <= n-3 (=> primitive by the p>n/2 lemma, and G >= A_n by Jordan, given transitivity): {jordan}")
transp = any(2 in cyc and cyc.count(2) == 1 and all(d % 2 != 0 for d in cyc if d != 2) for cyc in types)
print("transposition available as a Frobenius power:", transp)
