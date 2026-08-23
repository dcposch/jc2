#!/usr/bin/env python3
"""Exact Q2-l12/J-window coefficient-map audit.

This is a support/composition checker, not a Groebner solver.  It never calls
msolve.  The two exact elimination ledgers used by q2_backmap normally live in
/tmp/r1red and /tmp/r1dec.  Pass --rebuild-state to replay them from the
banked repository emissions when those transient files are absent.

The important convention is equation-level transport: substitute the complete
Q2 back-map, impose a leaf's zero prefix, sum the whole J equation, and only
then inspect support.  Looking at each coefficient separately misses exact
cancellations and gives the wrong answer for this lane.
"""

from __future__ import annotations

import argparse
import hashlib
import pickle
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"
SYS = ROOT / "systems" / "r1"
PRIMES = (105337, 105673)
BRANCHES = ((1, 1), (1, -1), (-1, 1), (-1, -1))
LEAVES = (11, 12, 13)
W0 = (0, 0, 0, 0)

sys.path.insert(0, str(CASES))
import r1_experiment as R1  # noqa: E402
import r1_fullcore as FC  # noqa: E402
import r1_minimal_ext as ME  # noqa: E402
import r1_q2_screen as Q2  # noqa: E402

# Keep the default checker output to its registered five-line summary.  Every
# q2_backmap regression is still executed; only its timestamped chatter is
# suppressed (the detailed audit is available with --verbose below).
Q2.log = lambda _msg: None


def die(msg: str) -> None:
    raise AssertionError(msg)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def parse_ms(path: Path):
    lines = path.read_text().splitlines()
    hdr = [x.strip() for x in lines[0].split(",")]
    p = int(lines[1])
    eqs = "\n".join(lines[2:]).strip().rstrip(",").split(",\n")
    return hdr, p, eqs


def canonical_eq(eq: str, p: int, zero_names=()):
    """Expanded .ms polynomial -> sparse monomial dict, with zeros applied."""
    zeros = set(zero_names)
    out = {}
    for sign, text in re.findall(r"([+-]?)([^+-]+)", eq.replace(" ", "")):
        c = -1 if sign == "-" else 1
        powers = {}
        killed = False
        for factor in text.split("*"):
            if factor.isdigit():
                c = c * int(factor) % p
                continue
            name, _, exponent = factor.partition("^")
            if name in zeros:
                killed = True
                break
            powers[name] = powers.get(name, 0) + int(exponent or 1)
        if killed:
            continue
        key = tuple(sorted(powers.items()))
        nc = (out.get(key, 0) + c) % p
        if nc:
            out[key] = nc
        elif key in out:
            del out[key]
    return out


def load_pickle(path: Path):
    with path.open("rb") as fh:
        return pickle.load(fh)


def ensure_backmap_state(rebuild: bool) -> None:
    red = Path("/tmp/r1red/reduced.pkl")
    dec = Path("/tmp/r1dec/leaves.pkl")
    if red.exists() and dec.exists():
        return
    if not rebuild:
        raise SystemExit(
            "q2_backmap needs /tmp/r1red/reduced.pkl and "
            "/tmp/r1dec/leaves.pkl; rerun with --rebuild-state"
        )

    # The current systems tree banks the reduced emission but not the original
    # 18 MB full-core .ms.  Replay from the archived prebuild snapshot; the
    # downstream all-119 q2 witness regression guards the resulting map.
    import r1_reduce as RR
    import r1_decompose as RD

    archive = ROOT / "runs" / "r1chain_prebuild_snapshot"
    need = archive / "r1_full_core.ms"
    assert need.exists(), need
    RR.SYS = str(archive)
    RR.COSTBLACK.clear()
    RR.phase_eliminate()
    assert red.exists()
    RD.phase_build()
    assert dec.exists()


def fresh(depth: int):
    R1.reset_vars()
    orbs = R1.build_generators(depth)
    vm = [dict(x) for x in R1.VARS]
    return orbs, vm


def normalize_orbits(orbs, vm, max_level: int):
    """Replace volatile registry ids by names, retaining exact ring values."""
    out = {}
    for on, orb in orbs.items():
        ser = {}
        for level, vex in orb["series"].items():
            # build_generators(D) registers free tails strictly below D.
            if level >= max_level:
                continue
            nv = {}
            for vk, ring in vex.items():
                nk = tuple(vm[i]["name"] for i in vk)
                nv[nk] = ring
            ser[level] = nv
        out[on] = (orb["size"], ser)
    return out


def core_map():
    """Ground-truth xN/name map without depending on /tmp/r1full."""
    _, vm54 = fresh(54)
    byname = {m["name"]: i for i, m in enumerate(vm54)}
    names = {}
    pat = re.compile(r"(x\d+) = (\S+) \(level (\d+)\)")
    for line in (SYS / "r1_full_core.rows.txt").read_text().splitlines():
        m = pat.fullmatch(line)
        if m:
            vid = byname[m.group(2)]
            assert vm54[vid]["level"] == int(m.group(3))
            names[vid] = m.group(1)
    assert len(names) == 119
    return names, vm54


def x_maps(names54, vm54):
    by_x = {int(xn[1:]): vm54[vid]["name"] for vid, xn in names54.items()}
    by_name = {nm: x for x, nm in by_x.items()}
    return by_x, by_name


def zfilter(vex, zero_vids):
    return {
        key: c for key, c in vex.items()
        if not (set(key[1]) & zero_vids)
    }


def vex_support(vex, vm84):
    return {vm84[v]["name"] for _, vk in vex for v in vk}


def vscale(vex, c, p):
    c %= p
    return {k: a * c % p for k, a in vex.items() if a * c % p}


def wshift(vex, p1, p2):
    return {
        ((w[0] + p1, w[1], w[2] + p2, w[3]), vk): c
        for (w, vk), c in vex.items()
    }


def branch_normalize(vex, s1, s2, mu, p):
    """HW_i = s_i*mu*W_i, in the same branch convention as J's bank."""
    out = {}
    for ((a, h, b, k), vk), c in vex.items():
        assert h in (0, 1) and k in (0, 1)
        cc = c * pow(s1 * mu % p, h, p) * pow(s2 * mu % p, k, p) % p
        key = ((a + h, 0, b + k, 0), vk)
        nc = (out.get(key, 0) + cc) % p
        if nc:
            out[key] = nc
        elif key in out:
            del out[key]
    return out


def eval_e(e, pt, mu, p):
    """Specialize an E=K3[a1,a2,mu] coefficient at a banked prime."""
    out = 0
    for (i, j, k), c in e.items():
        cc = (FC.frmod(c[0], p) + FC.frmod(c[1], p) * pt["r3"]) % p
        out += (cc * pow(pt["A1"], i, p) * pow(pt["A2"], j, p)
                * pow(mu, k, p))
    return out % p


def proportional(a, b, p):
    """Exact projective equality of two sparse vectors over F_p."""
    keys = sorted(set(a) | set(b))
    if not keys:
        return True
    pivot = next((k for k in keys if b.get(k, 0)), None)
    if pivot is None:
        return False
    aa, bb = a.get(pivot, 0), b[pivot]
    if aa == 0:
        return False
    return all(a.get(k, 0) * bb % p == b.get(k, 0) * aa % p
               for k in keys)


def compose_e_condition(st, row, cmap, pt, mu, p):
    out = {}
    cache = {"1": {(W0, ()): 1}}
    for col, ecoeff in row.items():
        mono, (p1, p2) = st["cols"][col]
        if mono not in cache:
            term = {(W0, ()): 1}
            for name in mono.split("*"):
                term = Q2.vmulp(term, cmap[name], p)
            cache[mono] = term
        c = eval_e(ecoeff, pt, mu, p)
        term = wshift(vscale(cache[mono], c, p), p1, p2)
        out = Q2.vaddp(out, term, p)
    return out


def compose_raw_row(row, jvars, cmap, pt, p, product_cache):
    out = {}
    for vk, ring in row.items():
        if vk not in product_cache:
            term = {(W0, ()): 1}
            for i in vk:
                term = Q2.vmulp(term, cmap[jvars[i]], p)
            product_cache[vk] = term
        term = Q2.vmulp(Q2.ring2vex(ring, pt, p), product_cache[vk], p)
        out = Q2.vaddp(out, term, p)
    return out


def coeff(vex, w):
    return vex.get((w, ()), 0)


def fourth_root(a, p):
    return next(x for x in range(1, p) if pow(x, 4, p) == a)


def nth_root(a, n, p):
    return next((x for x in range(p) if pow(x, n, p) == a), None)


def solve_scale(e1, e2, a1, a2, p):
    """Solve e1*X+e2*Y=0, a1*X+a2*Y+42=0."""
    det = (e1 * a2 - e2 * a1) % p
    assert det
    di = pow(det, p - 2, p)
    x = (42 * e2) * di % p
    y = (-42 * e1) * di % p
    return det, x, y


def leading_scaffold_check(p, x4, y4):
    """Check the 13 non-quotient leaf11 rows at the candidate scale."""
    hdr, pp, eqs = parse_ms(CASES / f"r1_q2_l8_leaf11_p{p}.ms")
    assert pp == p and len(eqs) == 20
    w1, w2 = fourth_root(x4, p), fourth_root(y4, p)
    pt = FC.radical_point(p)
    mu = pt["HW1"] * pow(pt["W1"], p - 2, p) % p
    val = {name: 0 for name in hdr}
    val.update(W1=w1, W2=w2, HW1=mu * w1 % p, HW2=mu * w2 % p,
               uW1=pow(w1, p - 2, p), uW2=pow(w2, p - 2, p),
               uf24=1, uuf24=1)

    val["HM"] = 0
    base = FC.parse_eval([eqs[15]], val, p)[0]
    val["HM"] = 1
    slope = (FC.parse_eval([eqs[15]], val, p)[0] - base) % p
    val["HM"] = -base * pow(slope, p - 2, p) % p

    val["s1F"] = 0
    base = FC.parse_eval([eqs[17]], val, p)[0]
    val["s1F"] = 1
    slope = (FC.parse_eval([eqs[17]], val, p)[0] - base) % p
    cube = -base * pow(slope, p - 2, p) % p
    val["s1F"] = nth_root(cube, 3, p)
    assert val["s1F"] not in (None, 0)
    val["tSAT"] = pow(val["s1F"], p - 2, p)
    got = FC.parse_eval(eqs, val, p)
    checked = tuple(range(8)) + tuple(range(15, 20))
    assert all(got[i] == 0 for i in checked), (p, checked, got)
    return w1, w2, val["HM"], val["s1F"]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rebuild-state", action="store_true",
                    help="replay exact reduction/UU ledgers into /tmp")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    ensure_backmap_state(args.rebuild_state)

    tails_path = ROOT / "directionb_tails_D21.pkl"
    cond_path = ROOT / "directionb_window_conditions.pkl"
    for repo_path, tmp_path in (
            (tails_path, Path("/tmp/directionb_tails_D21.pkl")),
            (cond_path, Path("/tmp/directionb_window_conditions.pkl"))):
        if tmp_path.exists():
            assert sha256(repo_path) == sha256(tmp_path)
    tails = load_pickle(tails_path)
    conditions = load_pickle(cond_path)
    assert tails["D"] == 21

    # Common template object: registry and orbit tower agree exactly by name.
    orbs53, vm53 = fresh(53)
    assert [m["name"] for m in vm53] == tails["vars"]
    orbs84, vm84 = fresh(84)
    assert normalize_orbits(orbs53, vm53, 53) == \
        normalize_orbits(orbs84, vm84, 53)
    assert len(vm53) == 183 and len(vm84) == 414

    names54, vm54 = core_map()
    by_x, by_name = x_maps(names54, vm54)
    # Make the repository's exact q2_backmap independent of a transient
    # /tmp/r1full/blocks.pkl: this is the same banked name map it expects.
    ME.core_name_map = lambda: (names54, vm54)
    name2vid84 = {m["name"]: i for i, m in enumerate(vm84)}
    vmap = {x: name2vid84[name] for x, name in by_x.items()}

    # Artifact equality and the exact l13 -> l12 delta.
    expected_delta = {
        "uf24", "bg42_24", "bg21_24", "tg1_60", "tg2_60",
        "tg01_60", "tg02_60", "bg42_60", "bg21_60",
    }
    expected_delta_vids = {
        "uf24": 1, "tg1_60": 192, "tg2_60": 238,
        "tg01_60": 273, "tg02_60": 296, "bg42_24": 319,
        "bg42_60": 355, "bg21_24": 384, "bg21_60": 402,
    }
    assert {n: name2vid84[n] for n in expected_delta} == expected_delta_vids
    emit_hdr = {}
    emit_eqs = {}
    leaf_hdr = {}
    missing_emit_pickles = []
    for p in PRIMES:
        for cut in (12, 13):
            emit_pickle = Path(f"/tmp/r1q2/emit_p{p}_l{cut}.pkl")
            hdr, pp, eqs = parse_ms(SYS / f"r1_q2_l{cut}_p{p}.ms")
            assert pp == p
            labels = []
            for line in (SYS / f"r1_q2_l{cut}_p{p}.rows.txt").read_text().splitlines():
                m = re.match(r"eq\d+ = (.*)", line)
                if m:
                    labels.append(m.group(1))
            if emit_pickle.exists():
                bank = load_pickle(emit_pickle)
                assert bank["hdr"] == hdr and bank["eqs"] == eqs
                assert bank["labels"] == labels
            else:
                missing_emit_pickles.append(str(emit_pickle))
            emit_hdr[p, cut] = hdr
            emit_eqs[p, cut] = eqs
        assert set(emit_hdr[p, 12]) - set(emit_hdr[p, 13]) == expected_delta
        assert not (set(emit_hdr[p, 13]) - set(emit_hdr[p, 12]))
        for leaf in LEAVES:
            leaf_hdr[p, leaf] = parse_ms(
                CASES / f"r1_q2_l8_leaf{leaf}_p{p}.ms")[0]
        for leaf, zeros, pivot in (
                (11, (), "uf24"),
                (12, ("uf24",), "bg42_24"),
                (13, ("uf24", "bg42_24"), "bg21_24")):
            _, pp, leqs = parse_ms(CASES / f"r1_q2_l8_leaf{leaf}_p{p}.ms")
            assert pp == p and len(leqs) == 20 and len(emit_eqs[p, 12]) == 19
            assert [canonical_eq(e, p) for e in leqs[:19]] == \
                [canonical_eq(e, p, zeros) for e in emit_eqs[p, 12]]
            want_sat = canonical_eq(f"u{pivot}*{pivot}+{p - 1}", p)
            assert canonical_eq(leqs[19], p) == want_sat
    assert emit_hdr[PRIMES[0], 12] == emit_hdr[PRIMES[1], 12]

    # J support census and the full coefficient dictionary.
    occurring_ids = sorted({i for band in tails["byk"].values()
                            for row in band.values() for vk in row for i in vk})
    occurring = [tails["vars"][i] for i in occurring_ids]
    bnames53 = {m["name"] for m in vm53
                if m["name"].startswith(("bf_", "bg42_", "bg21_"))}
    assert len(bnames53) == 100
    assert not (bnames53 & set(occurring))
    assert len(occurring) == 74 and set(occurring) <= set(by_name)

    backmaps = {}
    map_classes = {}
    term_counts = {}
    for p in PRIMES:
        xv, defs = Q2.q2_backmap(p, 12, vmap)
        assert set(defs) == {37, 43, 49}
        backmaps[p] = xv
        classes = {}
        counts = {}
        for name in occurring:
            x = by_name[name]
            vex = xv[x]
            own = {(W0, (name2vid84[name],)): 1}
            classes[name] = "zero" if not vex else \
                "identity" if vex == own else "polynomial"
            counts[name] = len(vex)
        map_classes[p] = classes
        term_counts[p] = counts
    assert map_classes[PRIMES[0]] == map_classes[PRIMES[1]]
    assert term_counts[PRIMES[0]] == term_counts[PRIMES[1]]
    mc = map_classes[PRIMES[0]]
    assert {k: list(mc.values()).count(k) for k in set(mc.values())} == \
        {"zero": 1, "identity": 41, "polynomial": 32}
    expected_poly_counts = {
        **{f"tf1_{level}": count for level, count in zip(
            (38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 52),
            (1, 1, 1, 1, 3, 1, 2, 1, 9, 4, 16, 56, 121))},
        **{f"tf2_{level}": count for level, count in zip(
            (38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 52),
            (1, 1, 1, 1, 3, 1, 2, 1, 2, 4, 2, 2, 104))},
        **{f"tg{side}_{level}": count for side in (1, 2)
           for level, count in ((38, 1), (40, 1), (42, 3))},
    }
    assert set(expected_poly_counts) == {n for n, k in mc.items()
                                         if k == "polynomial"}
    assert {n: term_counts[PRIMES[0]][n] for n in expected_poly_counts} == \
        expected_poly_counts

    # Literal B=0 is a well-defined coefficient condition on the Q2 chart.
    # Every B coefficient is zero, its own coordinate, or a noncore direct
    # coordinate; none carries a nontrivial polynomial back-map.
    bclass = {"zero": 0, "core_identity": 0, "fresh_identity": 0}
    bsets = {k: set() for k in bclass}
    xv0 = backmaps[PRIMES[0]]
    for name in sorted(bnames53):
        if name not in by_name:
            assert name in name2vid84
            bclass["fresh_identity"] += 1
            bsets["fresh_identity"].add(name)
            continue
        vex = xv0[by_name[name]]
        if not vex:
            bclass["zero"] += 1
            bsets["zero"].add(name)
        else:
            assert vex == {(W0, (name2vid84[name],)): 1}, name
            bclass["core_identity"] += 1
            bsets["core_identity"].add(name)
    assert bclass == {"zero": 26, "core_identity": 19,
                      "fresh_identity": 55}
    live_b = bsets["core_identity"] | bsets["fresh_identity"]
    for p in PRIMES:
        assert bnames53 & set(emit_hdr[p, 12]) == live_b
        assert bnames53 & set(leaf_hdr[p, 11]) == live_b
        assert bnames53 & set(leaf_hdr[p, 12]) == live_b
        assert bnames53 & set(leaf_hdr[p, 13]) == live_b - {"bg42_24"}

    band_labels = []
    for k in (6, 8, 10, 12, 14, 16, 18):
        rank = conditions[(k, 1, 1)]["rank"]
        band_labels += [f"C{k}.{i}" for i in range(1, rank + 1)]
    assert len(band_labels) == 47
    zero_labels = {
        "C6.1", *(f"C8.{i}" for i in range(1, 5)),
        *(f"C10.{i}" for i in range(1, 7)),
        *(f"C12.{i}" for i in range(1, 8)),
        *(f"C14.{i}" for i in range(7, 11)),
        *(f"C16.{i}" for i in range(7, 10)), "C18.8",
    }
    assert len(zero_labels) == 26

    # Whole-equation transport for the 47 branch-echelon conditions.
    condition_result = {}
    individual_local = {}
    for p in PRIMES:
        pt = FC.radical_point(p)
        mu = pt["HW1"] * pow(pt["W1"], p - 2, p) % p
        for leaf, zero_names in (
                (11, ()), (12, ("uf24",)),
                (13, ("uf24", "bg42_24"))):
            zero_vids = {name2vid84[n] for n in zero_names}
            raw_cmap = {name: zfilter(backmaps[p][by_name[name]], zero_vids)
                        for name in occurring}
            local = {name for name, vex in raw_cmap.items()
                     if vex_support(vex, vm84) <= set(leaf_hdr[p, leaf])}
            individual_local[p, leaf] = local
            assert len(local) == 50
            for branch in BRANCHES:
                cmap = {name: branch_normalize(vex, *branch, mu, p)
                        for name, vex in raw_cmap.items()}
                zeros, nonzeros = [], []
                for k in (6, 8, 10, 12, 14, 16, 18):
                    st = conditions[(k, *branch)]
                    assert st["rank"] == len(st["echelon"])
                    assert not st["leftover"]
                    for i, row in enumerate(st["echelon"], 1):
                        out = compose_e_condition(st, row, cmap, pt, mu, p)
                        assert vex_support(out, vm84) <= set(leaf_hdr[p, leaf])
                        (nonzeros if out else zeros).append(f"C{k}.{i}")
                assert set(zeros) == zero_labels
                assert len(nonzeros) == 21
                condition_result[p, leaf, branch] = (zeros, nonzeros)

    # Raw 77 eta rows, including slot20's +42, transport after the same
    # complete composition.  This independently checks the slot20 claim.
    raw_result = {}
    bzero_forms = {}
    bvids84 = {name2vid84[n] for n in bnames53}
    for p in PRIMES:
        pt = FC.radical_point(p)
        for leaf, zero_names in (
                (11, ()), (12, ("uf24",)),
                (13, ("uf24", "bg42_24"))):
            zero_vids = {name2vid84[n] for n in zero_names}
            cmap = {name: zfilter(backmaps[p][by_name[name]], zero_vids)
                    for name in occurring}
            cache = {}
            nonzero_by_band = {}
            bforms = {}
            nrows = 0
            for k in sorted(tails["byk"]):
                for eta, row in tails["byk"][k].items():
                    out = compose_raw_row(row, tails["vars"], cmap, pt, p,
                                          cache)
                    if k == 20 and eta == 0:
                        out = Q2.vaddp(out, {(W0, ()): 42}, p)
                    assert vex_support(out, vm84) <= set(leaf_hdr[p, leaf])
                    nrows += 1
                    if out:
                        nonzero_by_band.setdefault(k, []).append(eta)
                    bo = zfilter(out, bvids84)
                    if bo:
                        bforms[k, eta] = bo
            assert nrows == 77
            assert {k: len(v) for k, v in nonzero_by_band.items()} == \
                {14: 10, 16: 10, 18: 9, 20: 10}
            assert set(bforms) == {(20, 0), (20, 3), (20, 6)}
            assert all(not vex_support(v, vm84) for v in bforms.values())
            raw_result[p, leaf] = nonzero_by_band
            bzero_forms[p, leaf] = bforms
        assert bzero_forms[p, 11] == bzero_forms[p, 12] == \
            bzero_forms[p, 13]

    # On the only domain-compatible chart, Q2 pullback followed by the D21
    # B-zero specialization leaves one affine candidate pole-scale row.  The
    # other two surviving slot components are Q2 E.
    scale_data = {}
    for p in PRIMES:
        forms = bzero_forms[p, 11]
        e_eq = parse_ms(CASES / f"r1_q2_l8_leaf11_p{p}.ms")[2][4]
        m = re.fullmatch(r"(\d+)\*W1\^4\+(\d+)\*W2\^4", e_eq)
        assert m
        e1, e2 = map(int, m.groups())
        eta0, eta3, eta6 = forms[20, 0], forms[20, 3], forms[20, 6]
        wone = (W0, ())
        wx = ((4, 0, 0, 0), ())
        wy = ((0, 0, 4, 0), ())
        assert set(eta0) == {wone, wx, wy}
        assert set(eta3) == {wx, wy} and set(eta6) == {wx, wy}
        a1, a2 = coeff(eta0, (4, 0, 0, 0)), coeff(eta0, (0, 0, 4, 0))
        assert coeff(eta0, W0) == 42
        h3 = {"W1": coeff(eta3, (4, 0, 0, 0)),
              "W2": coeff(eta3, (0, 0, 4, 0))}
        h6 = {"W1": coeff(eta6, (4, 0, 0, 0)),
              "W2": coeff(eta6, (0, 0, 4, 0))}
        evec = {"W1": e1, "W2": e2}
        assert proportional(h3, evec, p) and proportional(h6, evec, p)
        det, x4, y4 = solve_scale(e1, e2, a1, a2, p)
        assert pow(x4, (p - 1) // 4, p) == 1
        assert pow(y4, (p - 1) // 4, p) == 1
        scaffold = leading_scaffold_check(p, x4, y4)
        scale_data[p] = (e1, e2, a1, a2, det, x4, y4, scaffold)

    # The six live no-log pins all map.  After the two direct tg0 pins,
    # the remaining four are Laurent-unit multiples of relation E.
    pins = ("tf1_42", "tf2_42", "tg1_42", "tg2_42",
            "tg01_42", "tg02_42")
    for p in PRIMES:
        pt = FC.radical_point(p)
        mu = pt["HW1"] * pow(pt["W1"], p - 2, p) % p
        hdr = set(leaf_hdr[p, 11])
        assert all(vex_support(backmaps[p][by_name[n]], vm84) <= hdr
                   for n in pins)
        direct_vids = {name2vid84["tg01_42"], name2vid84["tg02_42"]}
        cmap = {n: branch_normalize(zfilter(backmaps[p][by_name[n]],
                                            direct_vids), 1, 1, mu, p)
                for n in pins}
        assert not cmap["tg01_42"] and not cmap["tg02_42"]
        e_eq = parse_ms(CASES / f"r1_q2_l8_leaf11_p{p}.ms")[2][4]
        m = re.fullmatch(r"(\d+)\*W1\^4\+(\d+)\*W2\^4", e_eq)
        e1, e2 = map(int, m.groups())
        e = {((4, 0, 0, 0), ()): e1, ((0, 0, 4, 0), ()): e2}
        e_u1 = wshift(e, -2, 0)
        e_u2 = wshift(e, 0, -2)
        for n in ("tf1_42", "tg1_42"):
            assert proportional(cmap[n], e_u1, p), (p, n, cmap[n])
        for n in ("tf2_42", "tg2_42"):
            assert proportional(cmap[n], e_u2, p), (p, n, cmap[n])

    if args.verbose:
        print("J bank sha256:")
        print(" ", tails_path.name, sha256(tails_path))
        print(" ", cond_path.name, sha256(cond_path))
        print("occurring map classes:",
              {k: list(mc.values()).count(k) for k in sorted(set(mc.values()))})
        print("individual coefficient-local count:",
              {f"p{p}/leaf{leaf}": len(v)
               for (p, leaf), v in individual_local.items()})
        print("optional emit pickles absent:", missing_emit_pickles or "none")
        print("zero band pullbacks:", ", ".join(sorted(zero_labels)))
        for p, data in scale_data.items():
            e1, e2, a1, a2, det, x4, y4, scaffold = data
            print(f"p={p}: E=({e1},{e2}), eta0=42+{a1}X+{a2}Y, "
                  f"det={det}, (X,Y)=({x4},{y4}), "
                  f"roots/HM/s1F={scaffold}")

    # Five deliberately stable summary lines for logs and review diffs.
    print("PASS 1/5 common tower: D21 registry=depth53 exactly; "
          "depth53 orbit data=depth84 overlap exactly")
    print("PASS 2/5 l12 map: 74 occurring J coefficients -> "
          "1 zero + 41 identity + 32 polynomial backmaps; delta=9 exact")
    print("PASS 3/5 formal transport: each leaf gets 47/47 band + 10/10 "
          "slot20; 26 pullbacks zero and 21 nonzero before the B-domain tag")
    print("PASS 4/5 literal V is D21-B=0: leaf12/13 pivots conflict; "
          "Q2+B0 pullback on leaf11 leaves only slot20 eta0,eta3,eta6")
    print("PASS 5/5 payoff: eta3/eta6=Q2 E; eta0 is affine/nonproportional "
          "to E and quartic-compatible at both primes; no full-ideal cut or kill")


if __name__ == "__main__":
    main()
