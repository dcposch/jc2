#!/usr/bin/env python3
"""Exact root-free critical-value stratifier for loaded max12 order three.

The script deliberately keeps the norm in quadratic-algebra pair form.  A
fully expanded coefficient resultant has almost two hundred thousand terms;
the pair form is exactly equivalent and preserves the two original critical
points without adjoining either one.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
EXPECTED = {
    "cases/max12_912_order3_fibre_20260824/order3_fibre.py":
        "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf",
    "xmodel/max12-912-order3-nu-belyi-collision-boundary-20260824.md":
        "9b717712e59b70a6b06303f745a9c70b2152e3f624d03162741e3338ef1168b7",
    "xmodel/max12-912-order3-nu-belyi-collision-boundary-review-grok-20260824.md":
        "6d34908cbd2ead9769e4090fcab903ec5d5b7bd9db485db1d681708c5d36946e",
    "xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md":
        "f37376c96ab7e3c6ed7aa554dd04e2c72c9b2f5092ba6df03f524ea44765515d",
    "xmodel/max12-912-order3-nu-parity-genus5-review-grok-20260824.md":
        "903a973ac4975dfdeea77d143ebaa33cdc504d0f75d31dfe5327dad2d9be8528",
}


def load_parent():
    spec = importlib.util.spec_from_file_location("max12_cvnorm_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load order-three parent")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_parent()
M = P.M


def pin_inputs() -> dict[str, str]:
    pinned = {}
    for relative, expected in EXPECTED.items():
        got = sha256((ROOT / relative).read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError(f"input hash mismatch: {relative}: {got}")
        pinned[relative] = got
    # This recursively checks the frozen high-row dependencies of the parent.
    P.pin_inputs()
    return pinned


def cpow(value, exponent, ring):
    out = ring.one
    for _ in range(exponent):
        out = M.cmul(out, value)
    return out


def reduce_quadratic(poly, s, ring):
    """Return (even, odd) for poly modulo z^2=s."""
    even, odd = {}, {}
    powers = [ring.one]
    for _ in range(max(poly) // 2):
        powers.append(M.cmul(powers[-1], s))
    for exponent, coefficient in poly.items():
        term = M.cmul(coefficient, powers[exponent // 2])
        if exponent % 2:
            odd = M.cadd(odd, term)
        else:
            even = M.cadd(even, term)
    return even, odd


def qmul(left, right, s):
    """Multiply pairs a+b*z in the algebra z^2=s."""
    a, b = left
    c, d = right
    return (
        M.cadd(M.cmul(a, c), M.cmul(s, M.cmul(b, d))),
        M.cadd(M.cmul(a, d), M.cmul(b, c)),
    )


def qpow(value, exponent, s, ring):
    out = (ring.one, {})
    for _ in range(exponent):
        out = qmul(out, value, s)
    return out


def norm(value, s):
    a, b = value
    return M.cadd(M.cmul(a, a), M.cscale(-1, M.cmul(s, M.cmul(b, b))))


def abstract_norm_identities() -> None:
    ring = M.Ring(["G0", "G1", "F0", "F1", "s"])
    G0, G1, F0, F1, s = [ring.var(name) for name in ring.names]
    C0 = M.cadd(M.cmul(G0, G0), M.cscale(-1, M.cmul(s, M.cmul(G1, G1))))
    C1 = M.cscale(-2, M.cadd(
        M.cmul(G0, F0), M.cscale(-1, M.cmul(s, M.cmul(G1, F1)))
    ))
    C2 = M.cadd(M.cmul(F0, F0), M.cscale(-1, M.cmul(s, M.cmul(F1, F1))))
    E = M.cadd(M.cmul(G0, F1), M.cscale(-1, M.cmul(G1, F0)))
    discriminant = M.cadd(M.cmul(C1, C1), M.cscale(-4, M.cmul(C0, C2)))
    if discriminant != M.cscale(4, M.cmul(s, M.cmul(E, E))):
        raise RuntimeError("critical-value discriminant identity failed")

    W = (M.cadd(G0, M.cscale(-1, F0)),
         M.cadd(G1, M.cscale(-1, F1)))
    if M.cadd(M.cadd(C0, C1), C2) != norm(W, s):
        raise RuntimeError("C(1)=Norm(W) failed")


def specialize(value, source_names, images, target_ring):
    return P.substitute_coeff(value, images, target_ring)


def main() -> None:
    pins = pin_inputs()
    compiled = P.compile_fibre()

    # Normalize the nonzero constant load nu to one.  In raw coefficient
    # coordinates p=a7/3 and B/54=z^2-s with
    # s=-(a7+10*rho)/9.  The actual fibre separately imposes r8=rho.
    names = [f"a{i}" for i in range(8)] + ["rho"]
    ring = M.Ring(names)
    source = M.Ring([f"a{i}" for i in range(8)] + ["k"])
    images = [ring.var(f"a{i}") for i in range(8)] + [{}]
    f = {9: ring.one, **{i: ring.var(f"a{i}") for i in range(8)}}
    U = {i - 9: source.var(f"a{i}") for i in range(8)}
    g_source = P.faber(source, 9, 12, U)
    g = {exponent: specialize(coefficient, source.names, images, ring)
         for exponent, coefficient in g_source.items()}
    s = M.cscale(Fraction(-1, 9), M.cadd(
        ring.var("a7"), M.cscale(10, ring.var("rho"))
    ))

    f_pair = reduce_quadratic(f, s, ring)
    g_pair = reduce_quadratic(g, s, ring)
    F_pair = qpow(f_pair, 4, s, ring)
    G_pair = qpow(g_pair, 3, s, ring)

    # Positive control: on the parity locus f is odd and g is even, so the
    # unordered critical values agree without choosing a square root.
    parity_ring = M.Ring(["p", "x1", "x3", "x5", "rho"])
    p, x1, x3, x5, rho = [parity_ring.var(name) for name in parity_ring.names]
    zero = {}
    parity_images = [
        zero,
        x1,
        zero,
        M.cadd(cpow(p, 3, parity_ring), x3),
        zero,
        M.cadd(M.cscale(3, cpow(p, 2, parity_ring)), x5),
        zero,
        M.cscale(3, p),
        rho,
    ]
    if specialize(f_pair[0], names, parity_images, parity_ring):
        raise RuntimeError("parity f-even remainder is nonzero")
    if specialize(g_pair[1], names, parity_images, parity_ring):
        raise RuntimeError("parity g-odd remainder is nonzero")

    abstract_norm_identities()

    pair_data = {}
    for label, pair in (("f", f_pair), ("g", g_pair),
                        ("F=f^4", F_pair), ("G=g^3", G_pair)):
        pair_data[label] = {
            "even_terms": len(pair[0]),
            "odd_terms": len(pair[1]),
            "even_sha256": M.coefficient_digest(pair[0]),
            "odd_sha256": M.coefficient_digest(pair[1]),
        }

    payload = {
        "case": "max12_912_order3_critical_value_norm_20260824",
        "input_hashes": pins,
        "normalization": {
            "nu": 1,
            "p": "a7/3",
            "B": "54*(z^2-s)",
            "s": "-(a7+10*rho)/9",
            "actual_fibre_rows":
                "r1=r2=r3=r4=r5=r7=0, r6=1, r8=rho",
        },
        "quadratic_pair_hashes": pair_data,
        "critical_value_norm": {
            "F": "f^4 mod (z^2-s) = F0+F1*z",
            "G": "g^3 mod (z^2-s) = G0+G1*z",
            "C(T)":
                "Norm(G-TF)=C0+C1*T+C2*T^2",
            "C0": "G0^2-s*G1^2",
            "C1": "-2*(G0*F0-s*G1*F1)",
            "C2": "F0^2-s*F1^2",
            "E": "G0*F1-G1*F0",
            "discriminant": "C1^2-4*C0*C2=4*s*E^2",
            "C(1)": "Norm(G-F)",
        },
        "complete_split_on_NormF_times_s_nonzero": [
            "full absorption: W0=W1=0",
            "exactly one absorption: Norm(W)=0 and (W0,W1)!=(0,0)",
            "equal non-1 values: Norm(W)!=0 and E=0",
            "no absorption, unequal values: Norm(W)*E!=0",
        ],
        "separate_strata": [
            "s=0 (double B root; split W0=0 versus W0!=0)",
            "Norm(F)=0 (B meets f; retain until the actual-Keller firewall is applied)",
        ],
        "controls": {
            "parity": "f_even=0 and g_odd=0, hence E=0",
            "abstract_discriminant_identity": "PASS",
            "abstract_C_at_1_identity": "PASS",
        },
        "scope": (
            "exact coefficient-field stratifier only; no leaf is excluded, "
            "no Taylor boundary is dropped, and no max12 or JC2 conclusion follows"
        ),
        "tail_sha256": compiled["payload"]["tail_sha256"],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-MAX12-ORDER3-CRITICAL-VALUE-NORM")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
