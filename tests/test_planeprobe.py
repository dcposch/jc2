"""Tests for planeprobe: bivariate helpers, residual extraction, and gate A."""
import os, random, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "lib"))
sys.path.insert(0, os.path.join(BASE, "cases"))

import planeprobe as PP


def _randpoly(rng, p, nterms=6, dmax=4):
    f = {}
    for _ in range(nterms):
        f[(rng.randrange(dmax), rng.randrange(dmax))] = rng.randrange(1, p)
    return PP.btrim(f)


def test_bivariate_arith():
    p = 65521
    rng = random.Random(5)
    for _ in range(20):
        f, g = _randpoly(rng, p), _randpoly(rng, p)
        s, t = rng.randrange(p), rng.randrange(p)
        fg = PP.bmul(f, g, p)
        assert PP.beval(fg, s, t, p) == PP.beval(f, s, t, p) * PP.beval(g, s, t, p) % p
        assert PP.beval(PP.badd(f, g, p), s, t, p) == \
            (PP.beval(f, s, t, p) + PP.beval(g, s, t, p)) % p
        assert PP.beval(PP.bsub(f, g, p), s, t, p) == \
            (PP.beval(f, s, t, p) - PP.beval(g, s, t, p)) % p
        # t-major form evaluates consistently
        ct = PP.eval_s(PP.to_ts(f), s, p)
        from lineprobe import peval
        assert peval(ct, t, p) == PP.beval(f, s, t, p)


def test_residuals_consistent_system_vanish():
    """rhs = M * b_const  =>  system consistent everywhere  =>  all h_j == 0."""
    p = 65521
    rng = random.Random(9)
    m, n = 7, 4
    bstar = [rng.randrange(p) for _ in range(n)]
    rows = []
    for _ in range(m):
        ent = [(j, (rng.randrange(p), rng.randrange(p), rng.randrange(p)))
               for j in range(n)]
        r0 = sum(c[1][0] * bstar[j] for j, c in zip(range(n), ent)) % p
        r1 = sum(c[1][1] * bstar[j] for j, c in zip(range(n), ent)) % p
        r2 = sum(c[1][2] * bstar[j] for j, c in zip(range(n), ent)) % p
        rows.append(ent + [(n, (r0, r1, r2))])
    status, hs, rank = PP.residual_polys(rows, n, p, rng)
    assert status == "ok" and rank == n and hs == []


def test_residuals_detect_inconsistency():
    """generic rhs: residuals are nonzero; h_j(pt)=0 iff numerically consistent
    (checked at points where the pivot block is invertible)."""
    p = 65521
    rng = random.Random(10)
    m, n = 7, 4
    rows = []
    for _ in range(m):
        rows.append([(j, (rng.randrange(p), rng.randrange(p), rng.randrange(p)))
                     for j in range(n + 1)])
    status, hs, rank = PP.residual_polys(rows, n, p, rng)
    assert status == "ok" and rank == n and len(hs) == m - n
    for _ in range(20):
        s, t = rng.randrange(p), rng.randrange(p)
        M = PP._num_aug(rows, n, s, t, p)
        # numeric consistency: rank of M-part vs augmented
        Mc = [row[:n] for row in M]
        Ac = [row[:] for row in M]
        rM = _rank(Mc, p)
        rA = _rank(Ac, p)
        vals = [PP.beval(h, s, t, p) for h in hs]
        if rA > rM:                       # inconsistent -> some h nonzero
            assert any(vals)
        else:                             # consistent -> all bordered minors 0
            assert not any(vals)


def _rank(M, p):
    m = len(M)
    n = len(M[0]) if m else 0
    r = 0
    for col in range(n):
        sel = next((i for i in range(r, m) if M[i][col]), None)
        if sel is None:
            continue
        M[r], M[sel] = M[sel], M[r]
        inv = pow(M[r][col], p - 2, p)
        M[r] = [x * inv % p for x in M[r]]
        for i in range(m):
            if i != r and M[i][col]:
                f = M[i][col]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1
    return r


def test_planted_point_is_found():
    """rhs = M b* + random multiples of (s - s*) and (t - t*): the system is
    consistent exactly (generically) at (s*, t*); the probe must find it."""
    p = 65521
    rng = random.Random(21)
    m, n = 8, 4
    ss, ts = 12345, 54321
    bstar = [rng.randrange(p) for _ in range(n)]
    rows = []
    for _ in range(m):
        ent = [(j, (rng.randrange(p), rng.randrange(p), rng.randrange(p)))
               for j in range(n)]
        r0 = sum(ent[j][1][0] * bstar[j] for j in range(n)) % p
        r1 = sum(ent[j][1][1] * bstar[j] for j in range(n)) % p
        r2 = sum(ent[j][1][2] * bstar[j] for j in range(n)) % p
        al, be = rng.randrange(p), rng.randrange(p)
        # + al*(s - ss) + be*(t - ts), kept degree <= 1
        rows.append(ent + [(n, ((r0 - al * ss - be * ts) % p,
                                (r1 + al) % p, (r2 + be) % p))])
    info = PP.plane_candidates(rows, n, p, rng)
    assert info["status"] == "ok"
    assert (ss, ts) in info["cands"]
    assert PP._consistent_at(rows, n, ss, ts, p)


def test_gate_a_two_planes():
    """gate A: reg_9_24_c3 is proven empty at p=65521 -> zero verified hits,
    and no CURVE (a CURVE here would mean the probe is broken)."""
    p = 65521
    S = PP.build_system("reg_9_24_c3")
    out = os.path.join(BASE, "runs", "planeprobe_results.txt")
    res = PP.run_planes(S, p, 2, seed=11, out_path=out,
                        label="test:reg_9_24_c3", timeout_s=900)
    assert len(res) == 2
    for r in res:
        assert r["status"] != "CURVE"
        assert r["n_hits"] == 0


if __name__ == "__main__":
    test_bivariate_arith()
    test_residuals_consistent_system_vanish()
    test_residuals_detect_inconsistency()
    test_planted_point_is_found()
    test_gate_a_two_planes()
    print("test_planeprobe: all ok")
