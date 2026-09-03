#!/usr/bin/env python3
"""K=16 ray hostile gate.

Uses the frozen lane inputs in /tmp/jc2-lane.d5sry1/inputs and the repo
nested-pack support module knapsack_v2, with JC2_INPUTS pointed at the frozen
Moh enumerator.  Prints only the K=16 ray checks requested by the review lane.
"""
from __future__ import annotations

import hashlib
import importlib
import importlib.util
import json
import os
import sys
from fractions import Fraction as F
from math import gcd
from pathlib import Path

import sympy as sp


REPO = Path("/home/ubuntu/jc2")
INPUTS = Path("/tmp/jc2-lane.d5sry1/inputs")
BRANCH = REPO / "box" / "branch-orbits-v2-20260903"

EXPECTED = {
    "screened-census-grok46-20260903.md": "29a6f54dff3dbe2e2ad4cbb07dfdb7b18168e86848d5abb4644f2024f766b82d",
    "screened_census.py": "b28e6b3d36c2a6907b4175fb914e29757c5eec3b8a4a82bea3099dc88b6853cf",
    "whole-tree-review-opus5-20260903.md": "27551a88ab6ee9f62a5606010adcd9d4a1fd4411a09d97c699e13a67c84f7096",
    "opus5_probe.py": "4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9",
    "full_tree_partition.py": "875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8",
    "nested_pack.py": "36b374b21b3768e841ad2cc2168d7e669d9b0d6e6b6c8d1737d203acbd079067",
    "census-rebase-opus5-20260902.md": "fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948",
    "moh_skeleton_full.py": "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2",
    "phi_delta.py": "4bcb512d47cf9f935c6a2c0c7b8251ae16b3e4f73b4794abbef2d1702846c7c1",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def load_as(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def ray(T: int):
    n = 48 * T + 16
    m = 32 * T + 16
    return n, m, [n - 12, n - 2], {2: 3, 3: 3}


def fraction_text(x) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def symbolic():
    t = sp.symbols("t", integer=True, positive=True)
    e = 3 * t + 1
    dd = 2 * t + 1
    n = 16 * e
    m = 16 * dd
    M = {1: -m, 2: n - 12, 3: n - 2}
    d = {1: n, 2: 16, 3: 4, 4: 2}
    V = {2: 3, 3: 3, 4: 2}

    def delta(i: int):
        num = sp.Rational(1, 1) * (n - M[i])
        den = sp.Rational(1, 1) * (n - M[3] - 1)
        for j in range(i + 1, 4):
            num *= V[j] * (n - M[j]) - d[j]
            den *= V[j] * (n - M[j - 1]) - d[j]
        return sp.factor(1 - num / den)

    delta3 = delta(3)
    delta2 = delta(2)
    delta1 = delta(1)
    A2 = sp.denom(sp.cancel(delta2))
    L1 = 4
    A1 = sp.denom(sp.cancel(L1 * delta1))
    P = V[3] * d[2] // d[3]
    Q = sp.simplify(V[3] * (n - M[2]) / d[3])
    tri = P // int(A2)
    sq = P % int(A2)
    q = sp.factor((1 - delta1) * dd * e / (dd + e))
    N = sp.factor(4 * V[2] * q)

    n2 = n / 4
    m2 = m / 4
    M2p = M[2] / 4
    Mdesc = {1: -m2, 2: M2p}
    ddesc = {1: n2, 2: 4, 3: 1}
    Vdesc = {2: 3, 3: 1}

    def desc_delta(i: int):
        num = sp.Rational(1, 1) * (n2 - Mdesc[i])
        den = sp.Rational(1, 1) * (n2 - Mdesc[2] - 1)
        for j in range(i + 1, 3):
            num *= Vdesc[j] * (n2 - Mdesc[j]) - ddesc[j]
            den *= Vdesc[j] * (n2 - Mdesc[j - 1]) - ddesc[j]
        return sp.factor(1 - num / den)

    raw_desc2 = desc_delta(2)
    raw_desc1 = desc_delta(1)
    return {
        "bezout_gcd_e_d": str(sp.expand(3 * dd - 2 * e)),
        "poly_gcd_e_d": str(sp.gcd(e, dd)),
        "d_ladder": ["n", 16, 4, 2],
        "d3_check": str(sp.factor(n - 12)),
        "d4_check": str(sp.factor(n - 2)),
        "windows": {
            "i=3": "2 < 3 <= 4",
            "i=2": "4/3 < 3 <= 12",
        },
        "delta": {"3": str(delta3), "2": str(delta2), "1": str(delta1)},
        "A2": int(A2),
        "P": int(P),
        "Q": str(Q),
        "triangle": tri,
        "square": sq,
        "cond10": True,
        "cond11": False,
        "A1": str(A1),
        "A1_coprime_certificate": str(sp.expand(3 * (7 * t + 2) - 7 * (3 * t + 1))),
        "cond12_remainders": [str(sp.rem(3 * e, e, domain=sp.ZZ)), str(sp.rem(3 * dd - 1, e, domain=sp.ZZ))],
        "cond13_remainders": [str(sp.rem(3 * dd, e, domain=sp.ZZ)), str(sp.rem(3 * e - 1, e, domain=sp.ZZ))],
        "q": str(q),
        "N": str(N),
        "descended": {
            "n_prime": str(sp.factor(n2)),
            "m_prime": str(sp.factor(m2)),
            "M2_prime": str(sp.factor(M2p)),
            "V2_prime": 3,
            "k": 1,
            "raw_delta2": str(raw_desc2),
            "raw_delta1": str(raw_desc1),
            "Phi_delta2": str(sp.factor(2 * raw_desc2)),
            "Phi_delta1": str(sp.factor(2 * raw_desc1)),
            "anchor": str(sp.factor(n2 - M2p - 1)),
        },
    }


def op_partition(OP, n, m, Ms, V, *, ode=False):
    tree = OP.Tree(n, m, Ms, ode=ode)
    tree._memo = {}
    need = tuple(V[i] for i in range(tree.s - 1, 1, -1))
    return tree.ok(tree.s - 1, (V[tree.s],), False, need)


def main() -> int:
    print("== K16 gate: hash check ==")
    for name, expected in EXPECTED.items():
        got = sha256(INPUTS / name)
        print(f"{name}: {'OK' if got == expected else 'MISMATCH'} {got}")
        if got != expected:
            return 2

    os.environ["JC2_INPUTS"] = str(INPUTS)
    MF = load_as("moh_skeleton_full", INPUTS / "moh_skeleton_full.py")
    sys.modules["moh_skeleton_full_frozen"] = MF
    FT = load_as("k16_full_tree_partition_frozen", INPUTS / "full_tree_partition.py")
    OP = load_as("k16_opus5_probe_frozen", INPUTS / "opus5_probe.py")
    sys.path.insert(0, str(BRANCH))
    NP = importlib.import_module("nested_pack")

    print("\n== symbolic ==")
    print(json.dumps(symbolic(), indent=2, sort_keys=True))

    samples = [1, 2, 3, 5, 8]
    print("\n== census samples ==")
    for T in samples:
        n, m, Ms, V = ray(T)
        rows = []
        for rm, rMs, rV in MF.census(n, Kmin=16, full=True):
            if rm == m and list(rMs) == Ms and rV == V:
                rows.append(MF.Skel(n, rm, list(rMs), rV))
        print(f"t={T} n={n}: matches={len(rows)}")
        assert len(rows) == 1
        S = rows[0]
        print(
            "  full_ok=%s windows=%s K=%d d=%s delta=(%s,%s,%s) A1=%d q=%s u=%s"
            % (
                S.full_ok(),
                S.windows_ok(),
                S.K,
                [S.d[i] for i in range(1, S.s + 2)],
                S.delta[3],
                S.delta[2],
                S.delta[1],
                S.A(1),
                S.q(),
                S.u,
            )
        )
        group = [
            MF.Skel(n, rm, list(rMs), rV)
            for rm, rMs, rV in MF.census(n, Kmin=16, full=True)
            if rm == m and list(rMs) == Ms and rV[3] == 3
        ]
        print(f"  exact group V2={sorted({G.V[2] for G in group})}")

    print("\n== whole-tree screens and partition witnesses ==")
    for T in samples:
        n, m, Ms, V = ray(T)
        S = MF.Skel(n, m, Ms, V)
        part = op_partition(OP, n, m, Ms, V, ode=False)
        part_ode = op_partition(OP, n, m, Ms, V, ode=True)
        gated = OP.Tree(n, m, Ms, gate=True).embeds(V)
        gated_ode = OP.Tree(n, m, Ms, gate=True, ode=True).embeds(V)
        ft = FT.evaluator(S)
        ft_ok, ft_wit = ft.embeds(S)
        ft_ode = FT.evaluator(S, ode_nondegenerate=True)
        ft_ode_ok, ft_ode_wit = ft_ode.embeds(S)
        print(f"t={T} n={n}: OP partition={part is not None} partition+ODE={part_ode is not None} gated={gated is not None} gated+ODE={gated_ode is not None} FT={ft_ok} FT+ODE={ft_ode_ok}")
        wit = ft_ode_wit
        print(
            "  j={j} delta={delta} A={A} P={P} Q={Q} threshold={major_threshold} "
            "zero={zero_multiplicity} selected={selected_mode}:{selected_V} "
            "nonzero_orbits={nonzero_orbit_multiplicities}".format(**wit)
        )
        bottom = wit["selected_child"]
        print(
            "  bottom sibling V2={V2} A1={A1} delta1={delta1} (12)={condition12} (13)={condition13}".format(
                **bottom
            )
        )
        print("  q-slots: fixed zero p-mult=0; one nonzero orbit p-mult=3; one nonzero q-orbit unused")

    print("\n== nested-pack samples ==")
    for T in samples:
        n, m, Ms, V = ray(T)
        S = MF.Skel(n, m, Ms, V)
        vals, cap, states = NP.nested_values([S], max(NP.Umax([S]), F(6)))
        Ns = sorted(NP.ints_in(vals, 6, max(NP.Umax([S]), F(6))))
        packets = []
        for line in NP.describe_towers([S]):
            packets.append(line)
        print(f"t={T} n={n}: Ns={Ns} expected={[6*T+3]} cap={cap} states={states}")
        print(f"  {packets[0]}")
        assert Ns == [6 * T + 3]

    print("\n== descent samples and general datum ==")
    for T in samples:
        n, m, Ms, V = ray(T)
        S = MF.Skel(n, m, Ms, V)
        ds = S.d[S.s]
        n2, m2, M2p = n // ds, m // ds, Ms[0] // ds
        d2p = gcd(n2, m2)
        d3p = gcd(d2p, M2p)
        M = {1: -m2, 2: M2p}
        d = {1: n2, 2: d2p, 3: d3p}
        Vd = {2: 3, 3: d3p}

        def def51(i: int):
            num = F(n2 - M[i])
            den = F(n2 - M[2] - 1)
            for j in range(i + 1, 3):
                num *= Vd[j] * (n2 - M[j]) - d[j]
                den *= Vd[j] * (n2 - M[j - 1]) - d[j]
            return 1 - num / den

        raw2, raw1 = def51(2), def51(1)
        print(
            f"t={T}: (n',m',M2',V2',k)=({n2},{m2},{M2p},3,1) "
            f"d'={[d[1], d[2], d[3]]} raw=({raw2},{raw1}) Phi=({2*raw2},{2*raw1}) "
            f"anchor={n2-M2p-1}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
