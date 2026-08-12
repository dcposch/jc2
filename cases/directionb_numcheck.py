#!/usr/bin/env python3
"""Independent mod-p verification of the directionb J-jet Row_20 system.

Direct product of all 315 branch factors over F_p[eta, t]/(t^21), plain
int arithmetic (NO shared code with r1_experiment: no radical ring, no
suborbit Newton, no VExpr).  Frozen stratum (all tails/B-frees 0), w1,
w2 arbitrary nonzero field elements.  Verifies:
  (a) rows k = 0..19 of (t Phi_t - 12 Phi) Gamma_eta - Phi_eta
      (t Gamma_t - 18 Gamma) vanish exactly;
  (b) Row_20(eta) == sum_n eta^n [c1[n] al1 w1^4 + c2[n] al2 w2^4]
      with c1, c2 the exact K3 constants banked in
      /tmp/directionb_dsys.pkl (mapped via sqrt3 -> s mod p).
Run: python3 directionb_numcheck.py [p_start]
"""
import sys, pickle

D = 21

def find_setup(p0):
    """prime p = 1 mod 42 with sqrt3, cube roots of 3+-sqrt3, sqrt(3/2),
    7th root of 3/2 all in F_p; returns the full embedding."""
    def isprime(n):
        if n < 2 or n % 2 == 0: return n == 2
        d, s = n - 1, 0
        while d % 2 == 0: d //= 2; s += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            x = pow(a % n, d, n)
            if x in (0, 1, n - 1): continue
            for _ in range(s - 1):
                x = x * x % n
                if x == n - 1: break
            else: return False
        return True
    p = p0 + (1 - p0) % 42
    while True:
        while not isprime(p): p += 42
        try:
            def root(a, r):
                """some x with x^r = a (F_p), via g^k trick."""
                a %= p
                if a == 0: return 0
                g = 2
                while pow(g, (p - 1) // q, p) == 1 or not isgen(g):
                    g += 1
                # brute via discrete log is slow; use a^(inv) when
                # gcd(r, (p-1)/r^v)… simpler: try x = a^e with
                # e*r = 1 mod ord components; fallback scan small.
                raise RuntimeError
            # simpler: precompute generator and dlogs once (p ~ 1e5 ok)
            def isgen(g):
                for q in facs:
                    if pow(g, (p - 1) // q, p) == 1: return False
                return True
            facs = set()
            n = p - 1
            d = 2
            while d * d <= n:
                while n % d == 0: facs.add(d); n //= d
                d += 1
            if n > 1: facs.add(n)
            g = 2
            while not isgen(g): g += 1
            dlog = {}
            x = 1
            for e in range(p - 1):
                dlog[x] = e; x = x * g % p
            def rt(a, r):
                a %= p
                e = dlog[a]
                if e % r: return None
                # any r-th root; pick g^(e/r)
                return pow(g, e // r, p)
            s3 = rt(3, 2)
            if s3 is None: raise ValueError
            a1, a2 = (3 + s3) % p, (3 - s3) % p
            al1, al2 = rt(a1, 3), rt(a2, 3)
            BB = 3 * pow(2, p - 2, p) % p
            eB = rt(BB, 7)
            sq32 = rt(BB, 2)
            z = pow(g, (p - 1) // 42, p)
            if None in (al1, al2, eB, sq32): raise ValueError
            return p, s3, al1, al2, eB, sq32, z
        except ValueError:
            p += 42

def main():
    p0 = int(sys.argv[1]) if len(sys.argv) > 1 else 100003
    p, s3, al1, al2, eB, sq32, z = find_setup(p0)
    a1, a2 = (3 + s3) % p, (3 - s3) % p
    print("p = %d, sqrt3 = %d, al1 = %d, al2 = %d, eB = %d, z = %d"
          % (p, s3, al1, al2, eB, z))
    assert pow(al1, 3, p) == a1 and pow(al2, 3, p) == a2
    assert pow(eB, 7, p) == 3 * pow(2, p - 2, p) % p
    assert pow(z, 42, p) == 1 and pow(z, 21, p) != 1 and pow(z, 14, p) != 1 \
        and pow(z, 6, p) != 1
    w1, w2 = 12345 % p, 6789 % p
    hw1, hw2 = sq32 * w1 % p, sq32 * w2 % p
    NE = 40                      # eta-degree cap in arrays

    def pmulTE(A, B):
        """(t,eta)-poly product, truncate t-slot < D."""
        C = [[0] * NE for _ in range(D)]
        for s1, r1 in enumerate(A):
            if not any(r1): continue
            for s2, r2 in enumerate(B):
                if s1 + s2 >= D: break
                if not any(r2): continue
                row = C[s1 + s2]
                for n1, v1 in enumerate(r1):
                    if v1:
                        for n2, v2 in enumerate(r2):
                            if v2:
                                row[n1 + n2] = (row[n1 + n2] + v1 * v2) % p
        return C

    def unit():
        C = [[0] * NE for _ in range(D)]
        C[0][0] = 1
        return C

    def zp(e): return pow(z, e % 42, p)

    # ---- Phi: f-branches ----------------------------------------------
    Phi = unit()
    nthrough = 0
    for orb, alv, wv in (("P1", al1, w1), ("P2", al2, w2)):
        for c in range(42):
            if (12 * c) % 42 == 0:               # through: eta - z^32c al - z^37c w t^5
                f = [[0] * NE for _ in range(D)]
                f[0][1] = 1
                f[0][0] = (-zp(32 * c) * alv) % p
                f[5][0] = (-zp(37 * c) * wv) % p
                nthrough += 1
            else:                                 # t^12[(1 - z^12c) + (eta - z^32c al) t^20]
                f = [[0] * NE for _ in range(D)]
                f[0][0] = (1 - zp(12 * c)) % p
                f[20][1] = 1
                f[20][0] = (-zp(32 * c) * alv) % p
            Phi = pmulTE(Phi, f)
    for c in range(42):                           # B orbit: (1 - z^12c eB) + eta t^20
        f = [[0] * NE for _ in range(D)]
        f[0][0] = (1 - zp(12 * c) * eB) % p
        assert f[0][0] % p != 0, "degenerate B-direction"
        f[20][1] = 1
        Phi = pmulTE(Phi, f)
    assert nthrough == 12
    # ---- Gamma: g-branches --------------------------------------------
    Gam = unit()
    for orb, alv, wv in (("Gp1", al1, hw1), ("Gp2", al2, hw2)):
        for c in range(42):
            if (12 * c) % 42 == 0:
                f = [[0] * NE for _ in range(D)]
                f[0][1] = 1
                f[0][0] = (-zp(32 * c) * alv) % p
                f[5][0] = (-zp(37 * c) * wv) % p
            else:
                f = [[0] * NE for _ in range(D)]
                f[0][0] = (1 - zp(12 * c)) % p
                f[20][1] = 1
                f[20][0] = (-zp(32 * c) * alv) % p
            Gam = pmulTE(Gam, f)
    for alv in (al1, al2):                        # G0p orbits (21, even)
        for c in range(21):
            if (12 * c) % 42 == 0:                # c = 0, 7, 14
                f = [[0] * NE for _ in range(D)]
                f[0][1] = 1
                f[0][0] = (-zp(32 * c) * alv) % p
            else:
                f = [[0] * NE for _ in range(D)]
                f[0][0] = (1 - zp(12 * c)) % p
                f[20][1] = 1
                f[20][0] = (-zp(32 * c) * alv) % p
            Gam = pmulTE(Gam, f)
    for rng in (42, 21):                          # GB42, GB21
        for c in range(rng):
            f = [[0] * NE for _ in range(D)]
            f[0][0] = (1 - zp(12 * c) * eB) % p
            assert f[0][0] % p != 0
            f[20][1] = 1
            Gam = pmulTE(Gam, f)

    # ---- rows ----------------------------------------------------------
    def deta(A):
        return [[(r[n + 1] * (n + 1)) % p for n in range(NE - 1)] + [0]
                for r in A]
    A1 = [[(v * (s - 12)) % p for v in Phi[s]] for s in range(D)]
    B1 = deta(Gam)
    A2 = deta(Phi)
    B2 = [[(v * (s - 18)) % p for v in Gam[s]] for s in range(D)]
    T1 = pmulTE(A1, B1); T2 = pmulTE(A2, B2)
    L = [[(a - b) % p for a, b in zip(r1, r2)] for r1, r2 in zip(T1, T2)]
    ok = True
    for k in range(20):
        if any(L[k]):
            print("FAIL row %d nonzero: %s" % (k, L[k])); ok = False
    print(("PASS" if ok else "FAIL") + " rows 0..19 vanish exactly mod p")

    # ---- compare Row_20 against the banked exact constants -------------
    st = pickle.load(open("/tmp/directionb_dsys.pkl", "rb"))
    r20 = st["byk"][20]
    K1M = (0, 1, 0, 4, 0, 0, 0, 0); K2M = (0, 0, 1, 0, 0, 4, 0, 0)
    X1 = al1 * pow(w1, 4, p) % p
    X2 = al2 * pow(w2, 4, p) % p
    def k3mod(c):
        u, v = c
        return (u.numerator * pow(u.denominator, p - 2, p)
                + s3 * v.numerator * pow(v.denominator, p - 2, p)) % p
    want = [0] * NE
    for n, vex in r20.items():
        c = vex.get((), {})
        c1 = c.get(K1M); c2 = c.get(K2M)
        acc = 0
        if c1: acc += k3mod(c1) * X1
        if c2: acc += k3mod(c2) * X2
        want[n] = acc % p
    got = L[20]
    match = all(got[n] == want[n] for n in range(NE))
    print(("PASS" if match else "FAIL")
          + " Row_20(eta) == banked exact constants (all %d eta-coeffs)"
          % NE)
    if not match:
        for n in range(NE):
            if got[n] != want[n]:
                print("   eta^%d: got %d want %d" % (n, got[n], want[n]))

if __name__ == "__main__":
    main()
