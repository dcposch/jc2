#!/usr/bin/env python3
"""AWS-only exact compiler for the normalized (8,12), e=4, mu4!=0 curve V2."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "cases/max12_high_row_probe_20260824/shared_faber_probe.py"
EXPECTED_SHARED_SHA256 = "69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f"
CLIENT = ROOT / "xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-v2-20260825.md"
EXPECTED_CLIENT_SHA256 = "c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621"


def fail(message: object) -> "None":
    raise RuntimeError(message)


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_registered_aws() -> str:
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text().strip() if vendor_path.exists() else ""
    if platform.system() != "Linux" or vendor != "Amazon EC2" or not tag:
        fail({"aws_only": True, "system": platform.system(), "vendor": vendor,
              "registered_tag": bool(tag)})
    return tag


def load_shared():
    if sha(SHARED) != EXPECTED_SHARED_SHA256:
        fail("shared Faber compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("max12_shared_faber", SHARED)
    if spec is None or spec.loader is None:
        fail("cannot load shared Faber compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def inverse_root_to(module, ring, m: int, last_q: int):
    one = ring.one
    zseries = {1: one}
    for q_index in range(1, last_q + 1):
        target = m - 1 - q_index
        residual = module.zpower_coefficient(zseries, m, target, one)
        for i in range(m - 1):
            residual = module.cadd(
                residual,
                module.cmul(
                    ring.var(f"a{i}"),
                    module.zpower_coefficient(zseries, i, target, one),
                ),
            )
        correction = module.cscale(Fraction(-1, m), residual)
        if correction:
            zseries[-q_index] = correction
    return zseries


def build_order4(module):
    m, n, last_tail = 8, 12, 7
    ring = module.Ring([f"a{i}" for i in range(7)])
    one = ring.one

    f = {m: one}
    u_series = {}
    for i in range(7):
        ai = ring.var(f"a{i}")
        f[i] = ai
        u_series[i - m] = ai

    faber = {}
    for j in range(n + 1):
        fj = {j: one}
        upower = {0: one}
        for power in range(1, j // 2 + 1):
            upower = module.zmul(upower, u_series)
            term = {
                exponent + j: coefficient
                for exponent, coefficient in upower.items()
                if exponent + j >= 0
            }
            fj = module.zadd(
                fj,
                module.zscale(module.binomial(Fraction(j, m), power), term),
            )
        faber[j] = module.zclean(fj)
    g = dict(faber[n])

    if g.get(n) != one or any(exponent > n for exponent in g):
        fail("F_12 monic/degree check failed")

    # A t_q*w^-q correction first enters [w^-ell]z^12 at q=11+ell.
    last_q = n + last_tail - 1
    z_of_w = inverse_root_to(module, ring, m, last_q)
    for q_index in range(1, last_q + 1):
        target = m - 1 - q_index
        residual = module.zpower_coefficient(z_of_w, m, target, one)
        for i in range(7):
            residual = module.cadd(
                residual,
                module.cmul(
                    ring.var(f"a{i}"),
                    module.zpower_coefficient(z_of_w, i, target, one),
                ),
            )
        if residual:
            fail(("inverse-root residual", target, len(residual)))

    tails = {}
    weights = [8 - i for i in range(7)]
    for ell in range(1, last_tail + 1):
        coefficient = {}
        for z_exponent, g_coefficient in g.items():
            coefficient = module.cadd(
                coefficient,
                module.cmul(
                    g_coefficient,
                    module.zpower_coefficient(
                        z_of_w, z_exponent, -ell, one
                    ),
                ),
            )
        tail = module.cscale(-1, coefficient)
        expected_weight = n + ell
        for monomial in tail:
            actual_weight = sum(e * w for e, w in zip(monomial, weights))
            if actual_weight != expected_weight:
                fail(("tail weight", ell, actual_weight, monomial))
        tails[ell] = tail

    vpoly = module.zadd(
        module.zadd(
            module.zmul(g, g),
            module.zscale(-1, module.zpower(f, 3, one)),
        ),
        module.zscale(2, f),
    )
    if any(exponent > 11 for exponent in vpoly):
        fail(("shifted polynomial has unexpected high degree", max(vpoly)))
    return ring, f, g, tails, vpoly


def serialize_coeff(value):
    return [[list(monomial), str(coefficient)]
            for monomial, coefficient in sorted(value.items())]


def singular_expression(module, value, names: list[str]) -> str:
    return module.coeff_string(value, names)


def emit_singular(path: Path, module, ring, tails, vpoly) -> None:
    lines = [
        'LIB "elim.lib";',
        "ring R=0,(a0,a1,a2,a3,a4,a5,a6),dp;",
        "option(redSB);",
        "proc ideal_is_zero(ideal A)",
        "{",
        "  int i;",
        "  for (i=1; i<=size(A); i++)",
        "  {",
        "    if (A[i] != 0) { return(0); }",
        "  }",
        "  return(1);",
        "}",
    ]
    for ell in range(1, 8):
        lines.append(
            f"poly r{ell}={singular_expression(module, tails[ell], ring.names)};"
        )
    for degree in range(5, 12):
        lines.append(
            f"poly v{degree}={singular_expression(module, vpoly.get(degree, {}), ring.names)};"
        )
    lines.extend([
        "ideal Itail=r1,r2,r3,r4-1,r5,r6;",
        "ideal Icoef=v11,v10,v9,v8,v7,v6;",
        "ideal Gtail=std(Itail);",
        "ideal Gcoef=std(Icoef);",
        "int tail_to_coef=ideal_is_zero(reduce(Itail,Gcoef));",
        "int coef_to_tail=ideal_is_zero(reduce(Icoef,Gtail));",
        "int lead_ok=(reduce(v5+2*r7,Gtail)==0);",
        'print("TAIL_TO_COEF="+string(tail_to_coef));',
        'print("COEF_TO_TAIL="+string(coef_to_tail));',
        'print("LEAD_RELATION="+string(lead_ok));',
        "if ((tail_to_coef==0) || (coef_to_tail==0) || (lead_ok==0))",
        "{",
        '  print("SOURCE_EQUIVALENCE=FAIL");',
        "  quit;",
        "}",
        'print("SOURCE_EQUIVALENCE=PASS");',
        "list SS=sat(Itail,ideal(r7));",
        "ideal J=std(SS[1]);",
        "int is_unit=(reduce(1,J)==0);",
        'print("SAT_IS_UNIT="+string(is_unit));',
        'print("SAT_DIM="+string(dim(J)));',
        'print("SAT_BASIS_SIZE="+string(size(J)));',
        'print("SAT_BASIS_BEGIN");',
        "print(J);",
        'print("SAT_BASIS_END");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    tag = require_registered_aws()
    if sha(CLIENT) != EXPECTED_CLIENT_SHA256:
        fail("client theorem hash mismatch or compiler not frozen")
    if len(sys.argv) != 2:
        fail("usage: compile_curve.py OUTPUT_DIRECTORY")
    output = Path(sys.argv[1]).resolve()
    output.mkdir(parents=True, exist_ok=False)
    module = load_shared()
    ring, f, g, tails, vpoly = build_order4(module)

    tail_serial = {
        str(ell): serialize_coeff(tails[ell]) for ell in range(1, 8)
    }
    v_serial = {
        str(degree): serialize_coeff(vpoly.get(degree, {}))
        for degree in range(5, 12)
    }
    emit_singular(output / "coefficient_curve.sing", module, ring, tails, vpoly)
    (output / "tails.json").write_text(
        json.dumps(tail_serial, sort_keys=True) + "\n"
    )
    (output / "shifted_coefficients.json").write_text(
        json.dumps(v_serial, sort_keys=True) + "\n"
    )
    payload = {
        "status": "PASS-MAX12-812-ORDER4-MU4-NONZERO-CURVE-COMPILER-V2",
        "registered_aws_lane": tag,
        "compiler_sha256": sha(Path(__file__)),
        "shared_source_sha256": EXPECTED_SHARED_SHA256,
        "client_source_sha256": EXPECTED_CLIENT_SHA256,
        "tail_supports": {
            str(ell): len(tails[ell]) for ell in range(1, 8)
        },
        "shifted_coefficient_supports": {
            str(degree): len(vpoly.get(degree, {}))
            for degree in range(5, 12)
        },
        "tails_sha256": sha256(
            json.dumps(tail_serial, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "shifted_coefficients_sha256": sha256(
            json.dumps(v_serial, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "scope": {
            "order4_no_lower_load_tail_reconstruction": "EXACT",
            "shifted_ds_polynomial_reconstruction": "EXACT",
            "ideal_equivalence": "EMITTED_NOT_RUN",
            "r7_saturation": "EMITTED_NOT_RUN",
            "source_exactness": "NOT_COMPILED",
            "finite_taylor": "NOT_COMPILED",
            "order4_mu4_nonzero_closed": False,
            "JC2": "NOT_CLAIMED",
        },
    }
    (output / "result.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n"
    )
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

