#!/usr/bin/env python3
"""AWS-only compiler for two fixed-load order-one coefficient-curve probes."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SHARED = ROOT / "cases/max12_high_row_probe_20260824/shared_faber_probe.py"
DESIGN = ROOT / "xmodel/max12-812-order1-fixedload-coefficient-curve-probe-design-20260826.md"
SOURCES = {
    SHARED: "69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f",
    ROOT / "xmodel/max12-partial-y-shared-faber-probe-20260824.md":
        "d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036",
    ROOT / "xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md":
        "e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c",
    ROOT / "xmodel/max12-812-terminal-power-belyi-order1-theorem-20260825.md":
        "a4d7d6a1173b5a0b785aa61a4c80ad5f46e4ea83f1d73103917c425608666633",
    ROOT / "xmodel/max12-812-terminal-power-belyi-order1-review-grok-20260825.md":
        "e322d508c2af66aebb408b2794bd017b05e96cf9ca67f0fc74be8407406f67e1",
    DESIGN: "14f872accdeaaa9120924bfbe187cec6092ef27a64af59c8c24a301efefc65e6",
}
CONFIGS = {
    "A": {
        "characteristic": 32003,
        "h": (2, 3, 5, 7, 11, 13, 17, 19, 23),
        "r": (29, 31, 37, 41, 43, 47),
    },
    "B": {
        "characteristic": 65521,
        "h": (53, 59, 61, 67, 71, 73, 79, 83, 89),
        "r": (97, 101, 103, 107, 109, 113),
    },
}
H_INDICES = (1, 2, 3, 5, 6, 7, 9, 10, 11)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only order-one compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only order-one compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_shared():
    spec = importlib.util.spec_from_file_location("reviewed_shared_faber", SHARED)
    if spec is None or spec.loader is None:
        fail("could not load reviewed shared Faber compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def fixed_faber(sf, h_values: tuple[int, ...]):
    names = [f"a{i}" for i in range(7)]
    ring = sf.Ring(names)
    one = ring.one
    f = {8: one}
    u = {}
    for i in range(7):
        ai = ring.var(f"a{i}")
        f[i] = ai
        u[i - 8] = ai

    faber = {}
    for j in range(13):
        fj = {j: one}
        upower = {0: one}
        for k in range(1, j // 2 + 1):
            upower = sf.zmul(upower, u)
            term = {
                exponent + j: coefficient
                for exponent, coefficient in upower.items()
                if exponent + j >= 0
            }
            fj = sf.zadd(
                fj,
                sf.zscale(sf.binomial(Fraction(j, 8), k), term),
            )
        faber[j] = sf.zclean(fj)

    h = {j: Fraction(0) for j in range(13)}
    h[12] = Fraction(1)
    for index, value in zip(H_INDICES, h_values):
        h[index] = Fraction(value)
    if any(h[index] for index in (0, 4, 8)):
        fail("target gauge failure")
    g = {}
    for j in range(13):
        if h[j]:
            g = sf.zadd(g, sf.zscale(h[j], faber[j]))
    if g.get(12) != one or g.get(11) != sf.cscale(h[11], one):
        fail("monic or h11 row failure")

    fz = sf.zderivative(f)
    for i in range(7):
        fi = sf.zpartial(f, i)
        gi = sf.zpartial(g, i)
        jacobian = sf.zadd(sf.zmul(fi, sf.zderivative(g)),
                           sf.zscale(-1, sf.zmul(fz, gi)))
        bad = [exponent for exponent, coefficient in jacobian.items()
               if coefficient and 7 <= exponent <= 17]
        if bad:
            fail(("high-row failure", i, bad))
    return ring, f, g


def inverse_to(sf, ring, max_q: int):
    one = ring.one
    zseries = {1: one}
    for q in range(1, max_q + 1):
        target = 7 - q
        residual = sf.zpower_coefficient(zseries, 8, target, one)
        for i in range(7):
            residual = sf.cadd(
                residual,
                sf.cmul(ring.var(f"a{i}"),
                        sf.zpower_coefficient(zseries, i, target, one)),
            )
        correction = sf.cscale(Fraction(-1, 8), residual)
        if correction:
            zseries[-q] = correction
    for q in range(1, max_q + 1):
        target = 7 - q
        residual = sf.zpower_coefficient(zseries, 8, target, one)
        for i in range(7):
            residual = sf.cadd(
                residual,
                sf.cmul(ring.var(f"a{i}"),
                        sf.zpower_coefficient(zseries, i, target, one)),
            )
        if residual:
            fail(("inverse residual", q, target))
    return zseries


def tails_through_seven(sf, ring, g):
    # In z^12, the coefficient w^-7 first consumes t_18.
    zseries = inverse_to(sf, ring, 18)
    tails = {}
    for ell in range(1, 8):
        coefficient = {}
        for z_exponent, g_coefficient in g.items():
            coefficient = sf.cadd(
                coefficient,
                sf.cmul(
                    g_coefficient,
                    sf.zpower_coefficient(
                        zseries, z_exponent, -ell, ring.one
                    ),
                ),
            )
        # H(w) has no negative powers: r_l=-[w^-l]g(z(w)).
        tails[ell] = sf.cscale(-1, coefficient)
    return tails


def singular_program(sf, config: str, tails: dict[int, object]) -> str:
    data = CONFIGS[config]
    p = data["characteristic"]
    fixed_r = data["r"]
    expressions = {
        ell: sf.coeff_string(tails[ell], [f"a{i}" for i in range(7)])
        for ell in range(1, 8)
    }
    lines = [
        'LIB "elim.lib";',
        'LIB "primdec.lib";',
        f"ring R={p},(a0,a1,a2,a3,a4,a5,a6,rho,s,t),(dp(7),dp(3));",
        'print("ORDER1_SOURCE_HASHES=PASS");',
        'print("ORDER1_SHARED_FABER_REPLAY=PASS");',
        'print("ORDER1_GAUGES=h0,h4,h8");',
        f'print("ORDER1_CONFIG={config}");',
    ]
    for ell in range(1, 8):
        lines.append(f"poly r{ell}={expressions[ell]};")
    equations = [f"r{ell}-{fixed_r[ell - 1]}" for ell in range(1, 7)]
    lines.extend([
        "ideal I=" + ",".join(equations) + ";",
        "I=std(I);",
        'print("ORDER1_STD_DONE");',
        'print("ORDER1_I_SIZE="+string(size(I)));',
        'print("ORDER1_I_DIM="+string(dim(I)));',
        'print("ORDER1_MINASS_START");',
        "list PA=minAssGTZ(I);",
        'print("ORDER1_MINASS_DONE");',
        'print("ORDER1_MINASS_COUNT="+string(size(PA)));',
        "for (int ii=1; ii<=size(PA); ii++) {",
        "  ideal Pi=std(PA[ii]);",
        "  poly r7nf=reduce(r7,Pi);",
        "  int r7der=0;",
        "  if (diff(r7nf,a0)!=0 || diff(r7nf,a1)!=0 || diff(r7nf,a2)!=0 || diff(r7nf,a3)!=0 || diff(r7nf,a4)!=0 || diff(r7nf,a5)!=0 || diff(r7nf,a6)!=0) { r7der=1; }",
        '  print("ORDER1_COMPONENT="+string(ii)+",SIZE="+string(size(Pi))+",DIM="+string(dim(Pi)));',
        '  print("ORDER1_COMPONENT_R7_DERIVATIVE_SIGNAL="+string(ii)+":"+string(r7der));',
        "}",
        'print("ORDER1_CHART_A6_NONZERO_START");',
        "ideal Ia6nz=sat(I,ideal(a6));",
        "Ia6nz=std(Ia6nz);",
        'print("ORDER1_CHART_A6_NONZERO_DONE");',
        'print("ORDER1_CHART_A6_NONZERO_DIM="+string(dim(Ia6nz)));',
        'print("ORDER1_COMPLEMENT_A6_ZERO_START");',
        "ideal Ia6z=I,a6;",
        "Ia6z=std(Ia6z);",
        'print("ORDER1_COMPLEMENT_A6_ZERO_DONE");',
        'print("ORDER1_COMPLEMENT_A6_ZERO_DIM="+string(dim(Ia6z)));',
        "poly Slin=a0+2*a1+3*a2+5*a3+7*a4+11*a5+13*a6;",
        "poly Tlin=17*a0+19*a1+23*a2+29*a3+31*a4+37*a5+41*a6;",
        "ideal graph=I,rho-r7,s-Slin,t-Tlin;",
        'print("ORDER1_R7_GRAPH_ELIM_START");',
        "ideal r7graph=eliminate(graph,a0*a1*a2*a3*a4*a5*a6);",
        "r7graph=std(r7graph);",
        'print("ORDER1_R7_GRAPH_ELIM_DONE");',
        'print("ORDER1_R7_GRAPH_SIZE="+string(size(r7graph)));',
        'print("ORDER1_R7_GRAPH_DIM="+string(dim(r7graph)));',
        'print("ORDER1_PLANE_ELIM_START");',
        "ideal plane=eliminate(graph,a0*a1*a2*a3*a4*a5*a6*rho);",
        "plane=std(plane);",
        'print("ORDER1_PLANE_ELIM_DONE");',
        'print("ORDER1_PLANE_SIZE="+string(size(plane)));',
        'print("ORDER1_PLANE_DIM="+string(dim(plane)));',
        "if (size(plane)==1) {",
        '  print("ORDER1_PLANE_POLY_BEGIN");',
        "  print(plane[1]);",
        '  print("ORDER1_PLANE_POLY_END");',
        "  list PF=factorize(plane[1],1);",
        '  print("ORDER1_PLANE_FACTOR_COUNT="+string(size(PF[1])));',
        "}",
        'print("ORDER1_R7_SATURATION=NOT_PERFORMED");',
        'print("ORDER1_PROBE_ENDPOINT=PASS_NAVIGATION");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--config", choices=sorted(CONFIGS), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in SOURCES.items():
        if digest(source) != expected:
            fail(("frozen source mismatch", source, digest(source), expected))
    sf = load_shared()
    # Execute the reviewed universal (8,12) compiler as an independent source
    # and gauge sentinel before the fixed-load specialization.
    universal = sf.Frontier(8, 12, 4, 2, 3, (4, 2, 1)).compile()
    order_one = [branch for branch in universal["branches"]
                 if branch["Kummer_order"] == 1]
    if len(order_one) != 1:
        fail("missing unique reviewed order-one branch")
    expected_indices = list(H_INDICES)
    if order_one[0]["remaining_constant_indices"] != expected_indices:
        fail(("order-one gauge mismatch", order_one[0]))

    data = CONFIGS[args.config]
    ring, _f, g = fixed_faber(sf, data["h"])
    tails = tails_through_seven(sf, ring, g)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"order1_fixedload_{args.config}_p{data['characteristic']}.sing"
    singular.write_text(singular_program(sf, args.config, tails))
    tail_meta = {
        str(ell): {
            "support": len(tails[ell]),
            "sha256": sf.coefficient_digest(tails[ell]),
        }
        for ell in range(1, 8)
    }
    payload = {
        "status": "PASS-ORDER1-FIXEDLOAD-COMPILER",
        "registered_aws_lane": tag,
        "config": args.config,
        "characteristic": data["characteristic"],
        "h_indices": list(H_INDICES),
        "h_values": list(data["h"]),
        "r1_to_r6": list(data["r"]),
        "shared_faber_sha256": digest(SHARED),
        "design_sha256": digest(DESIGN),
        "tail_metadata": tail_meta,
        "singular_input_sha256": digest(singular),
        "scope": "NAVIGATION_ONLY_NO_COMPONENT_COVERAGE_NO_GENUS_NO_ORDER1_VERDICT",
    }
    (output / "result.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n"
    )
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
