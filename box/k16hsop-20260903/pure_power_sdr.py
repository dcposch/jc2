#!/usr/bin/env python3
"""Deliverable (1), degree half:  is a coprime PURE-POWER leading structure even
combinatorially available for the terminal tail?

A regular sequence f_0..f_{t-1} of weighted degrees 2t+2,...,3t+1 in variables of
weights 1,2,...,t-1,t+1 has pairwise coprime pure-power leading monomials
LM(f_r) = x_{sigma(r)}^{e_r} only if there is a SYSTEM OF DISTINCT REPRESENTATIVES:
an injection sigma from rows to variables with  w_{sigma(r)} | (2t+2+r).
(Then automatically prod e_r = prod deg / prod wt = L_t, the CI length.)

This script decides the bipartite matching for every t and reports:
  * whether an SDR exists;
  * whether b3 (weight t+1) is FORCED onto the degree-(2t+2) row -- i.e. onto the
    row whose b3^2-coefficient is the unit alpha_t.
"""
import sys
from itertools import product

def match(t):
    weights = list(range(1, t)) + [t + 1]         # 1..t-1, t+1
    degs = [2 * t + 2 + r for r in range(t)]
    adj = {r: [w for w in weights if degs[r] % w == 0] for r in range(t)}
    # Hopcroft-Karp-lite (Kuhn)
    matchW = {}
    def try_(r, seen):
        for w in adj[r]:
            if w in seen: continue
            seen.add(w)
            if w not in matchW or try_(matchW[w], seen):
                matchW[w] = r; return True
        return False
    ok = all(try_(r, set()) for r in range(t))
    sdr = {v: k for k, v in matchW.items()} if ok else None
    return ok, sdr, adj, weights, degs

print("  t | SDR exists | rows that weight t+1 can serve | assignment (deg -> weight^exp)")
allok = True
for t in range(3, 41):
    ok, sdr, adj, weights, degs = match(t)
    allok &= ok
    can = [2 * t + 2 + r for r in range(t) if (2 * t + 2 + r) % (t + 1) == 0]
    if t <= 12:
        asg = ", ".join(f"{degs[r]}->w{sdr[r]}^{degs[r]//sdr[r]}" for r in range(t)) if ok else "-"
    else:
        asg = "(ok)" if ok else "-"
    print(f"{t:3d} |   {str(ok):5s}    | {can}  | {asg}")
print()
print("ALL_SDR_EXIST =", allok)
print()
print("Note: 2t+2 = 2(t+1) is the ONLY multiple of t+1 in [2t+2, 3t+1] for every t>=1,")
print("since the next one is 3t+3 > 3t+1.  So weight t+1 (the variable b3) can only")
print("be matched to the TOP tail row T_{t,2t-1}, with exponent 2 -- exactly the row")
print("whose b3^2 coefficient is alpha_t, and exactly the exponent 2.")

# ---------------------------------------------------------------- part 2
print()
print("Obstruction: a PRIME degree D in [2t+3,3t+1] has, among the available")
print("weights {1,..,t-1,t+1}, only the divisor 1 (as D >= 2t+3 > t+1).  Two such")
print("degrees therefore both need weight 1 -> Hall's condition fails.")
print()
from sympy import isprime, primerange
print("  t | #primes in [2t+3,3t+1] | SDR | consistent?")
bad = []
for t in range(3, 401):
    ok, sdr, adj, weights, degs = match(t)
    np_ = sum(1 for D in range(2 * t + 3, 3 * t + 2) if isprime(D))
    consistent = (not ok) if np_ >= 2 else True
    if not consistent: bad.append(t)
    if t <= 20 or not ok and t % 97 == 0:
        print(f"{t:4d} |          {np_}             | {str(ok):5s} | {consistent}")
print("...")
print("t in 3..400 with (>=2 primes) but SDR still existing:", bad)
print("t in 3..400 with an SDR at all:", [t for t in range(3, 401) if match(t)[0]])
print()
print("Nagura (1952): for x >= 25 there is a prime in (x, 1.2x].  Applying it at")
print("x=2t+2 and again at x=floor(1.2(2t+2)) yields two distinct primes in")
print("(2t+2, 2.88t+2.88] subset [2t+3,3t+1] as soon as 2.88t+2.88 <= 3t+1, i.e.")
print("t >= 16.  The range 3 <= t <= 15 is settled by the table above.")
