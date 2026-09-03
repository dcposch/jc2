#!/usr/bin/env python3
"""Exact CRT/component audit for the branch-B band-5 compatibility locus.

The coefficient field is K=Q(a).  Since a is a unit in K, z=a*x,
Fhat(x)=a^4 F(a*x), and bhat=a^5*b identify the original system with the
a=1 system used by the accompanying Singular calculation.  The one costly
operation is bounded by SINGULAR_TIMEOUT_SECONDS.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
SINGULAR_INPUT = HERE / "band5_component_controls.sing"
SINGULAR_LOG = HERE / "band5_component_controls.log"
RESULT = HERE / "band5_component_audit.json"
SINGULAR_TIMEOUT_SECONDS = 240


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    x, z, t, a, b = sp.symbols("x z t a b")
    uu, vv, ff = sp.symbols("UU VV FF")

    # The fixed high part of f3 in local_band_audit.py is invisible modulo M5.
    H = z**2 * (z + 3 * a)
    M = z**6 * (z + 3 * a) ** 2
    fixed_f3 = 6 * H**5 * (-8 * z**4 - 18 * a * z**3)
    assert sp.rem(fixed_f3, M, domain=sp.QQ.frac_field(a)) == 0

    # Exact invertible normalization over Q(a).
    original_after_z_ax = (
        243 * uu * vv**2
        - 3888 * a**4 * x**3 * (x + 3) * vv * ff
        + 640 * b * a**5 * x**4 * (x + 3) * uu**3
    )
    normalized_with_hats = (
        243 * uu * vv**2
        - 3888 * x**3 * (x + 3) * vv * (a**4 * ff)
        + 640 * (a**5 * b) * x**4 * (x + 3) * uu**3
    )
    assert sp.expand(original_after_z_ax - normalized_with_hats) == 0

    # CRT coordinates p |-> ([p] mod x^6, p(-3),p'(-3)).
    crt = sp.Matrix(
        8,
        8,
        lambda row, col: (
            (1 if row == col else 0)
            if row < 6
            else ((-3) ** col if row == 6 else (0 if col == 0 else col * (-3) ** (col - 1)))
        ),
    )
    crt_det = sp.factor(crt.det())
    assert crt_det == 3**12

    # The degree-bounded images and their free kernels.
    modulus_x = x**6 * (x + 3) ** 2
    vc = sp.symbols("V0:11")
    fc = sp.symbols("F0:15")
    V = sum(vc[i] * x**i for i in range(11))
    F = sum(fc[i] * x**i for i in range(15))
    qv, rv = sp.div(V, modulus_x, x)
    qf, rf = sp.div(F, modulus_x, x)
    assert sp.expand(V - qv * modulus_x - rv) == 0 and sp.degree(qv, x) == 2
    assert sp.expand(F - qf * modulus_x - rf) == 0 and sp.degree(qf, x) == 6

    # Check that the eight equations used in Singular are precisely the two
    # CRT images of the normalized congruence.
    uc0 = sp.symbols("u0:6")
    vc0 = sp.symbols("v0:6")
    fc0 = sp.symbols("f0:6")
    U0 = sum(uc0[i] * x**i for i in range(6))
    V0 = sum(vc0[i] * x**i for i in range(6))
    F0 = sum(fc0[i] * x**i for i in range(6))
    N0 = sp.expand(
        243 * U0 * V0**2
        - 3888 * x**3 * (x + 3) * V0 * F0
        + 640 * b * x**4 * (x + 3) * U0**3
    )
    z_equations = [sp.expand(N0).coeff(x, i) for i in range(6)]
    assert len(z_equations) == 6

    x0, x1, y0, y1, g0, g1 = sp.symbols("x0 x1 y0 y1 g0 g1")
    Ut, Vt, Ft = x0 + x1 * t, y0 + y1 * t, g0 + g1 * t
    Nt = sp.expand(
        243 * Ut * Vt**2
        - 3888 * (t - 3) ** 3 * t * Vt * Ft
        + 640 * b * (t - 3) ** 4 * t * Ut**3
    )
    t_equations = [sp.expand(Nt).coeff(t, i) for i in range(2)]
    assert t_equations == [
        243 * x0 * y0**2,
        81 * (640 * b * x0**3 + 1296 * g0 * y0 + 6 * x0 * y0 * y1 + 3 * x1 * y0**2),
    ]

    # Direct certificate for the unique top component.
    wc = sp.symbols("W0:7")
    W = sum(wc[i] * x**i for i in range(7))
    utop = sum(sp.symbols("T0:8")[i] * x**i for i in range(8))
    ftop = sum(sp.symbols("S0:15")[i] * x**i for i in range(15))
    vtop = x**3 * (x + 3) * W
    ntop = 243 * utop * vtop**2 - 3888 * x**3 * (x + 3) * vtop * ftop
    assert sp.rem(ntop, modulus_x, domain=sp.QQ.frac_field(*wc, *sp.symbols("T0:8"), *sp.symbols("S0:15"))) == 0

    proc = subprocess.run(
        ["Singular", "-q", str(SINGULAR_INPUT)],
        cwd=HERE,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=SINGULAR_TIMEOUT_SECONDS,
        check=True,
    )
    SINGULAR_LOG.write_text(proc.stdout, encoding="utf-8")
    required = [
        "CONTROL_RING_PASS",
        "CONTROL_WRAPPER_NEGATIVE_PASS",
        "CONTROL_WRAPPER_POSITIVE_PASS",
        "MAIN_EXTRACT_RING_PASS",
        "MAIN_IDEAL_CONTAINMENT_PASS",
        "MAIN_MINASS_COUNT=15",
        "MAIN_LOCAL_JET_DIM=20",
        "MAIN_HISTOGRAM_17=3",
        "MAIN_HISTOGRAM_18=3",
        "MAIN_HISTOGRAM_19=8",
        "MAIN_HISTOGRAM_20=1",
        "MAIN_TOP_COMPONENT_UNIQUE_PASS",
    ]
    assert "FAIL" not in proc.stdout
    assert all(marker in proc.stdout for marker in required)

    combinations = [
        ["Z21|b=0", "Lb", 29],
        ["Z3b", "Lb", 30],
        ["Z20", "Luv", 29],
        ["Z3u", "Luv", 29],
        ["Z21", "Luv", 29],
        ["Z1|b=0", "Lb", 28],
        ["Z1", "Luv", 28],
        ["Z0|b=0", "Lb", 27],
        ["Z0", "Luv", 27],
        ["Z20", "Lu", 29],
        ["Z3b", "Lu", 29],
        ["Z3u", "Lu", 29],
        ["Z21", "Lu", 29],
        ["Z1", "Lu", 28],
        ["Z0", "Lu", 27],
    ]
    result = {
        "status": "PASS",
        "scope": "exact reduced band-5 compatibility variety; not a full Keller-pair existence claim",
        "field": "Q(a)",
        "a_localization": {
            "assumption": "a is a unit in Q(a)",
            "normalization": "z=a*x, Fhat(x)=a^4*F(a*x), bhat=a^5*b",
            "normalized_modulus": "x^6*(x+3)^2",
        },
        "degree_bounds": {"U": 7, "V": 10, "f3new": 14},
        "ambient_dimension": 35,
        "fixed_f3_shift_remainder_zero": True,
        "crt": {
            "map": "p -> (coefficients x^0..x^5, p(-3), p'(-3))",
            "matrix_determinant": str(crt_det),
            "isomorphism": True,
            "free_kernel_dimensions": {"U": 0, "V": 3, "f3new": 7, "total": 10},
            "local_equation_counts": {"at_x_0": 6, "at_x_minus_3": 2},
        },
        "singular": {
            "ring": "Q[u0..u5,v0..v5,f0..f5,x0,x1,y0,y1,g0,g1,b]",
            "order": "dp (degree reverse lexicographic)",
            "timeout_seconds": SINGULAR_TIMEOUT_SECONDS,
            "input": SINGULAR_INPUT.name,
            "log": SINGULAR_LOG.name,
            "input_sha256": sha256(SINGULAR_INPUT),
            "log_sha256": sha256(SINGULAR_LOG),
            "controls": required,
            "residue_ambient_dimension": 25,
            "residue_krull_dimension": 20,
            "minimal_prime_count": 15,
            "residue_dimension_histogram": {"17": 3, "18": 3, "19": 8, "20": 1},
        },
        "components": {
            "count": 15,
            "dimension_histogram": {"27": 3, "28": 3, "29": 8, "30": 1},
            "krull_dimension": 30,
            "unique_top_component": {
                "ideal_description": "b2=0 and z^3*(z+3*a) divides V",
                "parameterization": "V=z^3*(z+3*a)*W, deg(W)<=6; U and f3new arbitrary",
                "dimension_count": "b fixed; dim(U)+dim(W)+dim(f3new)=8+7+15=30",
            },
            "minimal_pairings": combinations,
        },
        "band_dimension_consequence": {
            "band4_parameter_locus_after_band5": 30,
            "unaffected_f4new_and_b4": 15,
            "band5_linear_kernel": 13,
            "cumulative_fiber_dimension_over_Q(a)": 58,
            "including_a": 59,
        },
        "inputs": {
            "local_band_audit.py": sha256(HERE / "local_band_audit.py"),
            "local_band_audit.json": sha256(HERE / "local_band_audit.json"),
        },
    }
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
