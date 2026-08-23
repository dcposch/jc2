#!/usr/bin/env python3
"""Exact Q2/B-zero certificate for the residue-A algebraization lane.

The meaningful orientation of the l12/J question is not
``eta0 in I_J``: eta0 is itself Row_20[eta^0]+42, hence that membership
is tautological.  This checker proves the stronger statement that the
Q2 leaf-11 quotient system has no point after imposing the literal D21
B=0 slice used by the banked J-window.

Write Q_n = W_F(n,60) - s1F*c_n for n = 2,9,16,23, where

    sum c_(7m+2) T^m = (T-1)^16 (T-3/2)^8.

In characteristic zero the exact orbit fold proves

    148342 W_F(2,60) + 9435 W_F(9,60)
      + 408 W_F(16,60) + 9 W_F(23,60) = 0                 (A)

after the 100 D21 B coordinates are set to zero.  Consequently

    148342 Q_2 + 9435 Q_9 + 408 Q_16 + 9 Q_23
      = -(76022307/128) s1F.                              (B)

Together with s1F*tSAT-1 this makes the localized/saturated ordinary
ideal the unit ideal; radical membership is therefore automatic too.

The exact phase reconstructs the lcut=12 back-map over the repository's
Q(sqrt(3))/radical ring, applies B=0 before the fold, and retains every
coefficient capable of entering slot 60.  Fresh tails have relative slot
at least 41, so at most one can occur.  Its complementary slot is at most
19; on this stratum the only possibilities are 0, 12 (uf24), and 18
(uf30).  Thus only fresh levels 72, 60, and 54 can occur.  All lower/core
directions remain symbolic.  VDEG_CAP=5 is exact because every free
coefficient has relative slot at least 12.

Usage:
    python3 cases/sol_algkill_q2.py             # modular + char-0 (slow)
    python3 cases/sol_algkill_q2.py --mod-only  # fast two-prime guard
    python3 cases/sol_algkill_q2.py --rebuild-state

State prerequisites are /tmp/r1red/reduced.pkl and /tmp/r1dec/leaves.pkl;
--rebuild-state recreates them through q2j_map's guarded replay.
On the development machine the exact folds take about five minutes after
generator construction; a cold complete run takes roughly 15--20 minutes.
"""

from __future__ import annotations

import argparse
import hashlib
import pickle
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"
sys.path.insert(0, str(CASES))

import q2j_map as J  # noqa: E402
import r1_experiment as R1  # noqa: E402
import r1_fullcore as FC  # noqa: E402
import r1_q2_screen as Q2  # noqa: E402
from r1_reduce import IR3  # noqa: E402


PRIMES = (105337, 105673)
NS = (2, 9, 16, 23)
LAM = (148342, 9435, 408, 9)
C = Fr(76022307, 128)
SCAP = 61
NMAX = 23
HIGH_LEVELS = {54, 60, 72}
PREFIX_B = ("bf_", "bg42_", "bg21_")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def is_d21_b(name: str, level: int) -> bool:
    return name.startswith(PREFIX_B) and level < 53


def pattern_coefficients():
    p21, pmul = R1.k3poly_pow_pattern()
    p8 = [R1.K1]
    for _ in range(8):
        p8 = pmul(p8, p21)
    cn = {7 * m + 2: c for m, c in enumerate(p8)}
    got = sum((R1.mk(a) * cn[n] for n, a in zip(NS, LAM)), R1.K0)
    assert got == R1.mk(C), (got, C)
    return cn


def modular_guard(cn) -> None:
    """Exact finite-field identity on the shipped full leaf equations."""
    for p in PRIMES:
        path = CASES / f"r1_q2_l8_leaf11_p{p}.ms"
        hdr, pp, eqs = J.parse_ms(path)
        assert pp == p and len(eqs) == 20
        zeros = {
            name for name in hdr
            if name.startswith(PREFIX_B)
            and int(name.rsplit("_", 1)[1]) < 53
        }
        # The header contains only the 74 live members of the 100-coordinate
        # D21 B block; the other 26 were already zero before emission.
        assert len(zeros) == 74
        rows = [J.canonical_eq(eqs[8 + i], p, zeros) for i in range(4)]
        combo = {}
        for a, row in zip(LAM, rows):
            for mon, coeff in row.items():
                new = (combo.get(mon, 0) + a * coeff) % p
                if new:
                    combo[mon] = new
                elif mon in combo:
                    del combo[mon]
        cp = C.numerator % p * pow(C.denominator, p - 2, p) % p
        assert combo == {(('s1F', 1),): (-cp) % p}, combo

        # Full specialized support guard: among fresh coefficients, only
        # levels 54/60/72 occur.  This independently audits the exact
        # slot-complement pruning used below.
        allq = [J.canonical_eq(eqs[i], p, zeros) for i in range(8, 15)]
        tail_names = {
            name for row in allq for mon in row for name, _ in mon
            if name.startswith(("tf", "tg", "bf_", "bg42_", "bg21_"))
        }
        assert {int(name.rsplit("_", 1)[1]) for name in tail_names} \
            <= HIGH_LEVELS
        print(
            f"PASS mod {p}: 148342Q2+9435Q9+408Q16+9Q23 "
            f"= {-cp % p}*s1F; full B-zero quotient support levels "
            f"{sorted({int(x.rsplit('_', 1)[1]) for x in tail_names})}",
            flush=True,
        )


def vmul_unbounded(x, y):
    """VExpr product without the global development cap (back-map only)."""
    out = {}
    for kx, rx in x.items():
        for ky, ry in y.items():
            key = tuple(sorted(kx + ky))
            prod = R1.rmul(rx, ry)
            if not prod:
                continue
            out[key] = prod if key not in out else R1.radd(out[key], prod)
            if not out[key]:
                del out[key]
    return out


def exact_bzero_backmap(vm84, corexn, vm54, name2vid):
    """Exact lcut=12 Q2 back-map with the D21 B slice imposed early."""
    with Path("/tmp/r1dec/leaves.pkl").open("rb") as fh:
        uu = pickle.load(fh)["UU"]["subs"]
    with Path("/tmp/r1red/reduced.pkl").open("rb") as fh:
        red = pickle.load(fh)["subs"]

    assigned = {v for v, _, _, _ in uu} | {v for v, _, _, _ in red}
    levels = {v: vm84[name2vid[name]]["level"]
              for v, name in corexn.items()}
    xv = {}
    for v in range(119):
        if v in assigned:
            continue
        name = corexn[v]
        level = levels[v]
        if level - 12 < 12 or is_d21_b(name, level):
            xv[v] = {}
        else:
            xv[v] = {(name2vid[name],): R1.RONE}

    def radkey_to_ring(rk, coeff):
        e3 = rk[IR3]
        kc = R1.mk(Fr(coeff) * Fr(3) ** (e3 // 2)) * \
            (R1.SQ3 if e3 % 2 else R1.K1)
        return R1.rmono(
            za=rk[1], a1=rk[2], a2=rk[3], w1=rk[4], h1=rk[5],
            w2=rk[6], h2=rk[7], B=rk[8], c=kc,
        )

    def evaluate(poly):
        acc = {}
        for (rk, xkey), coeff in poly.items():
            term = {(): radkey_to_ring(rk, coeff)}
            for v, exponent in xkey:
                for _ in range(exponent):
                    term = vmul_unbounded(term, xv[v])
                    if not term:
                        break
                if not term:
                    break
            acc = R1.vadd(acc, term)
        return acc

    defs = {}
    for v, _, poly, _ in list(reversed(uu)) + list(reversed(red)):
        value = evaluate(poly)
        name = corexn[v]
        level = levels[v]
        if v in Q2.KEEPX:
            defs[v] = value
            xv[v] = {} if is_d21_b(name, level) else \
                {(name2vid[name],): R1.RONE}
        else:
            xv[v] = value

    # l12map's B-coordinate claim, now checked in the exact ring: every
    # assigned kept B value also vanishes on B=0.
    assert all(not defs[v] for v in Q2.KEEPX)
    for v, name in corexn.items():
        if is_d21_b(name, levels[v]):
            assert not xv[v], (v, name, xv[v])
    assert not any(key and key[-1] == R1.HIVAR
                   for value in xv.values() for key in value)
    return xv, defs


def no_sentinel(jet) -> bool:
    return all(not (key and key[-1] == R1.HIVAR)
               for vex in jet.values() for key in vex)


def exact_to_mod_named(vex, vm84, point, p):
    out = {}
    for vkey, ring in vex.items():
        for (wvec, empty), coeff in Q2.ring2vex(ring, point, p).items():
            assert not empty
            powers = Counter(vm84[v]["name"] for v in vkey)
            for name, exponent in zip(("W1", "HW1", "W2", "HW2"),
                                      wvec):
                if exponent >= 0:
                    if exponent:
                        powers[name] += exponent
                else:
                    assert name in ("W1", "W2")
                    powers["u" + name] += -exponent
            mon = tuple(sorted(powers.items()))
            new = (out.get(mon, 0) + coeff) % p
            if new:
                out[mon] = new
            elif mon in out:
                del out[mon]
    return out


def exact_guard(cn, rebuild_state: bool) -> None:
    J.ensure_backmap_state(rebuild_state)
    names54, vm54 = J.core_map()

    R1.reset_vars()
    orbits = R1.build_generators(84)
    vm84 = [dict(meta) for meta in R1.VARS]
    name2vid = {meta["name"]: i for i, meta in enumerate(vm84)}
    corexn = {int(xname[1:]): vm54[vid]["name"]
              for vid, xname in names54.items()}

    bnames = {
        meta["name"] for meta in vm84
        if is_d21_b(meta["name"], meta["level"])
    }
    assert len(bnames) == 100
    xv, defs = exact_bzero_backmap(vm84, corexn, vm54, name2vid)
    xbyname = {corexn[v]: xv[v] for v in range(119)}

    # Construct the faithful B-zero series.  All core directions remain
    # symbolic.  For noncore/fresh tails, the slot-complement lemma above
    # leaves exactly levels 54, 60, 72.
    for orbit in orbits.values():
        for level, vex in list(orbit["series"].items()):
            if level - 12 >= SCAP:
                del orbit["series"][level]
                continue
            (vkey, ring), = vex.items()
            if not vkey:
                value = {(): ring}
            else:
                (vid,) = vkey
                name = vm84[vid]["name"]
                if name in xbyname:
                    value = xbyname[name]
                elif is_d21_b(name, level):
                    value = {}
                elif level < 53:
                    # Noncore extension coordinates (notably uf30 and the
                    # odd 49/51 tails) are genuinely open on lcut=12.
                    value = {(vid,): R1.RONE}
                elif level in HIGH_LEVELS:
                    value = {(vid,): R1.RONE}
                else:
                    value = {}
            if value:
                orbit["series"][level] = value
            else:
                del orbit["series"][level]
    # Every free variable has relative slot >= 12, so degree 5 is the exact
    # maximum below SCAP=61.  A sentinel assertion below guards this bound.
    R1.VDEG_CAP = 5
    t0 = time.time()
    folds = {}
    for name in R1.FORB + R1.GORB:
        folds[name] = R1.fs_block(orbits[name], SCAP)
        print(
            f"  exact fold {name}: {len(folds[name])} keys, "
            f"{sum(len(v) for v in folds[name].values())} terms "
            f"({time.time() - t0:.1f}s)", flush=True,
        )
        assert no_sentinel(folds[name])

    jf = R1.JONE
    for name in R1.FORB:
        jf = R1.jmul(jf, folds[name], SCAP, ndeg=NMAX)
    jg = R1.JONE
    for name in R1.GORB:
        jg = R1.jmul(jg, folds[name], SCAP, ndeg=NMAX)
    assert no_sentinel(jf) and no_sentinel(jg)
    f2 = R1.jmul(jf, jf, SCAP, ndeg=NMAX)
    f3 = R1.jmul(f2, jf, SCAP, ndeg=NMAX)
    g2 = R1.jmul(jg, jg, SCAP, ndeg=NMAX)
    wf = R1.jadd(g2, R1.jscal(f3, -1))
    assert no_sentinel(wf)

    lhs = {}
    for n, coeff in zip(NS, LAM):
        lhs = R1.vadd(lhs, R1.vscal(wf.get((n, 60), {}), coeff))
    assert not lhs, R1.emit_expanded(lhs, {
        i: meta["name"] for i, meta in enumerate(vm84)
    })[:2000]

    # Cross-engine regression of the four exact rows against both shipped
    # modular leaf equations after precisely the same 100-coordinate B cut.
    for p in PRIMES:
        point = FC.radical_point(p)
        hdr, _, eqs = J.parse_ms(CASES / f"r1_q2_l8_leaf11_p{p}.ms")
        zeros = {
            name for name in hdr
            if name.startswith(PREFIX_B)
            and int(name.rsplit("_", 1)[1]) < 53
        }
        for i, n in enumerate(NS):
            got = exact_to_mod_named(wf[(n, 60)], vm84, point, p)
            rhs = FC.ring_modp(R1.rC(-cn[n]), point, p)
            smon = (('s1F', 1),)
            got[smon] = (got.get(smon, 0) + rhs) % p
            if not got[smon]:
                del got[smon]
            want = J.canonical_eq(eqs[8 + i], p, zeros)
            assert got == want, (p, n, len(got), len(want))
        print(f"PASS exact->mod cross-engine regression p={p}", flush=True)

    print(
        "PASS char 0: 148342*WF_2 + 9435*WF_9 + 408*WF_16 "
        "+ 9*WF_23 = 0 on Q2(l12)+B_D21=0",
        flush=True,
    )
    print(
        "PASS ordinary-ideal certificate: the quotient combination is "
        "-(76022307/128)*s1F; with s1F*tSAT-1 the saturated ideal is [1]",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mod-only", action="store_true")
    parser.add_argument("--rebuild-state", action="store_true")
    args = parser.parse_args()

    cn = pattern_coefficients()
    modular_guard(cn)
    print(
        "source hashes:",
        *(f"{path.name}={sha256(path)}" for path in
          (CASES / "r1_q2_l8_leaf11_p105337.ms",
           CASES / "r1_q2_l8_leaf11_p105673.ms")),
        sep="\n  ", flush=True,
    )
    if not args.mod_only:
        exact_guard(cn, args.rebuild_state)


if __name__ == "__main__":
    main()
