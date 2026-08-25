#!/usr/bin/env python3
"""AWS-only exact compiler for the (8,12), e=2, U=2, [6,2] Rees client."""

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
CLIENT = ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md"
EXPECTED_CLIENT_SHA256 = "e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7"


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


def build_faber_and_tails(module):
    m, n, last_tail = 8, 12, 7
    names = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
    ring = module.Ring(names)
    one = ring.one
    U = {}
    for i in range(7):
        U[i - m] = ring.var(f"a{i}")

    faber = {}
    for j in range(n + 1):
        Fj = {j: one}
        Upower = {0: one}
        for power in range(1, j // 2 + 1):
            Upower = module.zmul(Upower, U)
            term = {exponent + j: coefficient
                    for exponent, coefficient in Upower.items()
                    if exponent + j >= 0}
            Fj = module.zadd(
                Fj,
                module.zscale(module.binomial(Fraction(j, m), power), term),
            )
        faber[j] = module.zclean(Fj)

    g = dict(faber[12])
    for index in (10, 6, 2):
        kvar = ring.var(f"k{index}")
        g = module.zadd(
            g,
            {exponent: module.cmul(kvar, coefficient)
             for exponent, coefficient in faber[index].items()},
        )

    # A t_q w^-q correction can first enter [w^-ell] z^12 at q=11+ell.
    last_q = n + last_tail - 1
    z_of_w = inverse_root_to(module, ring, m, last_q)

    # Verify every solved inverse-root coefficient through the charged order.
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
    weights = [8 - i for i in range(7)] + [2, 6, 10]
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
        expected_weight = 12 + ell
        for monomial in tail:
            actual_weight = sum(e * w for e, w in zip(monomial, weights))
            if actual_weight != expected_weight:
                fail(("tail weight", ell, actual_weight, monomial))
        tails[ell] = tail
    return ring, tails


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def singular_rees_expression(tail, names: list[str]) -> str:
    terms = []
    for monomial, coefficient in sorted(tail.items(), reverse=True):
        factors = []
        odd_power = sum(monomial[names.index(f"a{i}")] for i in (1, 3, 5))
        if odd_power:
            factors.append("(1+tau)" if odd_power == 1 else f"(1+tau)^{odd_power}")
        for i in range(7):
            exponent = monomial[names.index(f"a{i}")]
            if exponent:
                factors.append(f"B{i}" if exponent == 1 else f"B{i}^{exponent}")
        tau_power = 0
        rho_power = 0
        for name, tau_weight, rho_weight in (
            ("k10", 6, 2), ("k6", 18, 6), ("k2", 30, 10)
        ):
            exponent = monomial[names.index(name)]
            tau_power += tau_weight * exponent
            rho_power += rho_weight * exponent
            if exponent:
                factors.append(name if exponent == 1 else f"{name}^{exponent}")
        if tau_power:
            factors.append(f"tau^{tau_power}")
        if rho_power:
            factors.append(f"rho^{rho_power}")
        body = "*".join(factors) or "1"
        if coefficient == 1 and factors:
            term = body
        elif coefficient == -1 and factors:
            term = "-" + body
        else:
            term = f"{rational_text(coefficient)}*{body}" if factors else rational_text(coefficient)
        terms.append(term)
    return "+".join(terms).replace("+-", "-") if terms else "0"


def serialize_tail(tail):
    return [[list(monomial), str(coefficient)]
            for monomial, coefficient in sorted(tail.items())]


def emit_singular(path: Path, ring, tails) -> None:
    variables = (
        "tau,rho,B0,B1,B2,B3,B4,B5,B6,k10,k6,k2,"
        "mu2,mu4,mu6,j"
    )
    lines = [
        'LIB "elim.lib";',
        f"ring R=0,({variables}),dp;",
    ]
    targets = {
        1: "0", 2: "mu2", 3: "0", 4: "mu4",
        5: "0", 6: "mu6", 7: "(j/4)*(1+tau)",
    }
    for ell in range(1, 8):
        lhs = singular_rees_expression(tails[ell], ring.names)
        target = targets[ell]
        if target != "0":
            lhs += f"-tau^{3 * (12 + ell)}*rho^{12 + ell}*({target})"
        lines.append(f"poly Psi{ell}={lhs};")
    lines.extend([
        "ideal I=Psi1,Psi2,Psi3,Psi4,Psi5,Psi6,Psi7;",
        "list ST=sat(I,ideal(tau)); ideal KT=ST[1];",
        "list SR=sat(KT,ideal(rho)); ideal K=SR[1];",
        "ideal boundary=K,tau,rho;",
        "ideal irrelevant=B0,B1,B2,B3,B4,B5,B6;",
        "list SH=sat(boundary,irrelevant); ideal H=std(SH[1]);",
        'print("STRICT_REES_H_SIZE="+string(size(H)));',
        'print("STRICT_REES_H_IS_UNIT="+string(reduce(1,H)==0));',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    tag = require_registered_aws()
    if sha(CLIENT) != EXPECTED_CLIENT_SHA256:
        fail("client theorem hash mismatch or compiler not frozen")
    if len(sys.argv) != 2:
        fail("usage: compile_rees.py OUTPUT_DIRECTORY")
    output = Path(sys.argv[1]).resolve()
    output.mkdir(parents=True, exist_ok=False)
    module = load_shared()
    ring, tails = build_faber_and_tails(module)
    serialized = {str(ell): serialize_tail(tails[ell]) for ell in range(1, 8)}
    canonical = json.dumps(serialized, sort_keys=True, separators=(",", ":"))
    payload = {
        "status": "PASS-MAX12-812-ORDER2-U2-62-TAIL-COMPILER",
        "registered_aws_lane": tag,
        "shared_source_sha256": EXPECTED_SHARED_SHA256,
        "client_source_sha256": EXPECTED_CLIENT_SHA256,
        "tail_supports": {str(ell): len(tails[ell]) for ell in range(1, 8)},
        "tail_sha256": {
            str(ell): sha256(json.dumps(serialize_tail(tails[ell]), separators=(",", ":")).encode()).hexdigest()
            for ell in range(1, 8)
        },
        "all_tails_sha256": sha256(canonical.encode()).hexdigest(),
        "scope": {
            "tail_reconstruction": "EXACT",
            "strict_saturation": "EMITTED_NOT_RUN",
            "taylor_x0": "CHARGED_NOT_COMPILED",
            "taylor_x1": "CHARGED_NOT_COMPILED",
            "order2_closed": False,
            "JC2": "NOT_CLAIMED",
        },
    }
    (output / "tails.json").write_text(json.dumps(serialized, sort_keys=True) + "\n")
    emit_singular(output / "strict_rees.sing", ring, tails)
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
