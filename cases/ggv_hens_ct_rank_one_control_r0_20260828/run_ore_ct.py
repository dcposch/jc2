#!/usr/bin/env python3
"""Emit an algebraic CT operator/certificate using ore_algebra.

This program is intended for the preregistered AWS lane only.
"""

import hashlib
import json
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

# PassageMath is modular and intentionally has no monolithic ``sage.all``.
# This installed aggregate initializes all Sage components required here.
from sage.all__sagemath_symbolics import ZZ, PolynomialRing
from ore_algebra import OreAlgebra


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fail(label, detail):
    Path("TERMINAL").write_text(label + "\n", encoding="ascii")
    Path("failure.txt").write_text(str(detail) + "\n", encoding="utf-8")
    print(label, detail, flush=True)
    raise SystemExit(2)


def main():
    print("START_UTC", utc(), flush=True)
    print("HOST", platform.node(), flush=True)
    print("PYTHON", sys.version.replace("\n", " "), flush=True)
    print("ORE_COMMIT_EXPECTED", os.environ.get("ORE_COMMIT", ""), flush=True)

    # Outer monomial f(ss,xx,yy)=xx^2 yy^2.
    outer, outer_gens = PolynomialRing(ZZ, names=("ss", "xx", "yy")).objgens()
    ss0, xx0, yy0 = outer_gens
    OA, ops = OreAlgebra(outer, "Dss", "Dxx", "Dyy").objgens()
    Dss0, Dxx0, Dyy0 = ops
    monomial_ideal = OA.ideal([Dss0, xx0 * Dxx0 - 2, yy0 * Dyy0 - 2])

    # Inner algebraic field E=Q(ss,xx)[ya]/(ya^8-1-ss*h*ya).
    base, base_gens = PolynomialRing(ZZ, names=("ss", "xx")).objgens()
    ss, xx = base_gens
    k0 = base.fraction_field()
    yp = PolynomialRing(k0, names=("ya",))
    ya0 = yp.gen()
    h = 1 + xx ** (-3) + xx ** (-7)
    modulus = ya0 ** 8 - 1 - ss * h * ya0
    E = k0.extension(modulus, names=("ya",))
    ya = E.gen()
    print("MODULUS", modulus, flush=True)
    print("BRANCH_SEED ya(ss=0)=1", flush=True)

    print("ANNIHILATOR_BEGIN", utc(), flush=True)
    J = monomial_ideal.annihilator_of_composition(
        ss=E(ss), xx=E(xx), yy=ya, infolevel=2
    )
    print("ANNIHILATOR_END", utc(), flush=True)
    print("J_DIM", J.dimension(), flush=True)
    print("J_VDIM", J.vector_space_dimension(), flush=True)
    print("J", repr(J), flush=True)

    jops = J.ring().gens()
    by_name = {str(op): op for op in jops}
    if "Dxx" not in by_name:
        fail("FAIL_NO_DXX", list(map(str, jops)))
    Dxx = by_name["Dxx"]

    print("CT_BEGIN", utc(), flush=True)
    try:
        T, certs = J.ct(
            Dxx,
            certificates=True,
            early_termination=True,
            iteration_limit=int(os.environ.get("CT_ITERATION_LIMIT", "96")),
            infolevel=2,
        )
    except Exception as exc:
        fail("FAIL_CT_EXCEPTION", repr(exc))
    print("CT_END", utc(), flush=True)
    if not T.gens() or not certs:
        fail("FAIL_EMPTY_CT", (T, certs))

    L = T.gens()[0]
    C = certs[0]
    if L.is_zero() or C is None or C.is_zero():
        fail("FAIL_ZERO_OPERATOR_OR_CERT", (L, C))

    remainder = (J.ring()(L) - Dxx * C).reduce(J)
    print("L", repr(L), flush=True)
    print("C", repr(C), flush=True)
    print("ORE_MEMBERSHIP_REMAINDER", repr(remainder), flush=True)
    if not remainder.is_zero():
        fail("FAIL_ORE_MEMBERSHIP", remainder)

    # Preserve exact machine-readable sparse forms.  Coefficients are repr
    # strings; the direct field replay is a separate follow-up stage.
    payload = {
        "schema": "ggv-hens-ct-rank-one-r0",
        "utc": utc(),
        "host": platform.node(),
        "modulus": str(modulus),
        "branch_seed": "ya(ss=0)=1",
        "L": repr(L),
        "C": repr(C),
        "L_terms": [[list(exp), str(coef)] for exp, coef in sorted(L.dict().items())],
        "C_terms": [[list(exp), str(coef)] for exp, coef in sorted(C.dict().items())],
        "ore_membership_remainder": repr(remainder),
    }
    Path("ct_output.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    print("CT_OUTPUT_SHA256", sha("ct_output.json"), flush=True)
    # Direct algebraic action/replay is deliberately mandatory and performed
    # by replay_ore_certificate.py after this emitter freezes its result.
    Path("TERMINAL").write_text("EMITTED_NEEDS_DIRECT_REPLAY\n", encoding="ascii")
    print("EMITTED_NEEDS_DIRECT_REPLAY", flush=True)


if __name__ == "__main__":
    main()
