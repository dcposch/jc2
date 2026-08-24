#!/usr/bin/env python3
"""Deterministic arithmetic controls for the AS109 degree cross-gate."""

p = 109
passed = 0


def check(label, condition):
    global passed
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'}  {label}")
    if not ok:
        raise AssertionError(label)
    passed += 1


# The special fibre sends all p residues a to zero and has derivative one.
check("Fermat collapse on all 109 source residues",
      all((a - pow(a, p, p)) % p == 0 for a in range(p)))
check("special derivative is one", (1 - p) % p == 1)
check("109 source balls per fixed target residue", len(range(p)) == p)
check("ordered local sectors", p * p == 11881)
check("ordered local off sectors", p * (p - 1) == 11772)
check("off sectors over one selected source branch", p - 1 == 108)


# Mechanism control.  For every N>=p,
#   g_N(x)=x-x^p+p*x^N
# has the same reduction and unit derivative on every integral ball, while
# its characteristic-zero generic degree is N.  Thus local Hensel data alone
# impose neither p-divisibility nor a congruence on the global degree.
degrees = [p, p + 1, p + 2, 2 * p, 2 * p + 1]
for n in degrees:
    # Coefficients are represented sparsely; combine when n=p.
    coeff = {1: 1, p: -1}
    coeff[n] = coeff.get(n, 0) + p
    coeff = {e: c for e, c in coeff.items() if c}
    degree = max(coeff)
    check(f"control N={n}: generic degree is N", degree == n)
    # Every nonconstant derivative term is divisible by p, so g_N'=1 mod p.
    deriv_mod_p = {e - 1: (e * c) % p for e, c in coeff.items() if e > 0}
    deriv_mod_p = {e: c for e, c in deriv_mod_p.items() if c}
    check(f"control N={n}: derivative is 1 mod 109", deriv_mod_p == {0: 1})
    check(f"control N={n}: same residue collapse",
          all((a - pow(a, p, p) + p * pow(a, n, p)) % p == 0
              for a in range(p)))

check("controls realize degree 0 mod 109", any(n % p == 0 for n in degrees))
check("controls realize degree 1 mod 109", any(n % p == 1 for n in degrees))
check("controls realize degree 2 mod 109", any(n % p == 2 for n in degrees))


# Rank consequences of a degree d extension after p split formal sections.
for d in (109, 110, 137, 218):
    check(f"degree {d}: residual rank is nonnegative", d - p >= 0)
    check(f"degree {d}: global off rank dominates local off rank",
          d * (d - 1) >= p * (p - 1))

print(f"\n{passed}/{passed} arithmetic checks passed")
