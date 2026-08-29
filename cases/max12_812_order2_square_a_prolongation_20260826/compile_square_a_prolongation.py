#!/usr/bin/env python3
"""Compile the generic-square high-contact A-prolongation (AWS only)."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
BASE_COMPILER = ROOT / "cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py"
DESIGN = ROOT / "xmodel/max12-812-order2-square-a-prolongation-design-20260826.md"
HALFWEIGHT_DESIGN = ROOT / "xmodel/max12-812-order2-generic-square-halfweight-kuranishi-design-20260826.md"
HALFWEIGHT_RESULTS = ROOT / "cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.md"
THIRD_TAIL = ROOT / "xmodel/max12-812-order2-square-third-tail-divisibility-theorem-20260826.md"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"

EXPECTED_STATIC = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    BASE_COMPILER: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    DESIGN: "36b8abd0383d901261a4b410c94a0ffb759e3dea37263852af86778e77d5589d",
    HALFWEIGHT_DESIGN: "37a7234cee998a0069f33b7a36bb945123b305acd01485a771d8e6ed7dac65fd",
    HALFWEIGHT_RESULTS: "eb2cd8036a0abf87a1ff7a58c116346b11973efc47f35f9cb76105a6ccd485af",
    THIRD_TAIL: "045b1bdc6c1429451afa34dd2d7d12da4c72d9af716e52228a869f61d0f4a4bb",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only square A-prolongation compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only square A-prolongation compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base_compiler():
    spec = importlib.util.spec_from_file_location("square_ladder_base", BASE_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot load charged base compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_coefficients() -> dict[int, str]:
    p = "p"
    c = "(sigma^4*bs0+sigma^5*bs1)"
    r = "((p^2+sigma^4*br0+sigma^5*br1)/4)"
    n3 = "(sigma^3*(a1+sigma*aa1))"
    n2 = "(sigma^3*(a0+sigma*aa0))"
    n1 = "(sigma^3*(p*(a1+sigma*aa1)+sigma^4*(e1+sigma*ee1))/2)"
    n0 = "(sigma^3*(p*(a0+sigma*aa0)+sigma^4*(e0+sigma*ee0))/2)"
    return {
        6: f"(2*({p}))",
        5: f"(2*({c}))",
        4: f"(({p})^2+2*({r}))",
        3: f"(2*({p})*({c})+sigma^2*({n3}))",
        2: f"(({c})^2+2*({p})*({r})+sigma^2*({n2}))",
        1: f"(2*({c})*({r})+sigma^2*({n1}))",
        0: f"(({r})^2+sigma^2*({n0}))",
    }


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    base = load_base_compiler()
    coeffs = source_coefficients()
    loads = {"k10": "(k0+sigma*k1)", "k6": "k6", "k2": "k2"}
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    variables = (
        "sigma,p,a0,a1,aa0,aa1,bs0,br0,bs1,br1,e0,e1,ee0,ee1,"
        "k0,k1,k6,k2,mu2,mu4,mu6,J"
    )
    lines = [
        'LIB "elim.lib";',
        'LIB "primdec.lib";',
        f"ring Rfull={characteristic},({variables}),dp;",
        "proc idealZero(ideal A, ideal G)",
        "{",
        "  int i;",
        "  for (i=1; i<=size(A); i++) { if (reduce(A[i],G)!=0) { return(0); } }",
        "  return(1);",
        "}",
        'print("SQUARE_APROL_SOURCE_HASHES=PASS");',
        "ideal Sigma14=std(ideal(sigma^14));",
        "int divisible14=1; int identity14=1; int identity15=1;",
        "int forbidden14=1; int forbidden15=1; int cancellation14=1;",
    ]
    for ell in range(1, 8):
        expression = base.tail_text(tails[str(ell)], ell, coeffs, loads)
        expression = expression.replace("Lambda", "(sigma^2)")
        if targets[ell] != "0":
            expression += f"-sigma^{2 * (12 + ell)}*({targets[ell]})"
        lines.extend([
            f"poly Phi{ell}={expression};",
            f"if (reduce(Phi{ell},Sigma14)!=0) {{ divisible14=0; }}",
            f"poly Xi14_{ell}=Phi{ell}/sigma^14;",
            f"if (sigma^14*Xi14_{ell}-Phi{ell}!=0) {{ identity14=0; }}",
            f"poly e14_{ell}=subst(Xi14_{ell},sigma,0);",
            f"poly Rem15_{ell}=Xi14_{ell}-e14_{ell};",
            f"poly Xi15_{ell}=Rem15_{ell}/sigma;",
            f"if (sigma*Xi15_{ell}-Rem15_{ell}!=0) {{ identity15=0; }}",
            f"poly e15_{ell}=subst(Xi15_{ell},sigma,0);",
            f"if (diff(e14_{ell},k6)!=0 || diff(e14_{ell},k2)!=0 || diff(e14_{ell},mu2)!=0 || diff(e14_{ell},mu4)!=0 || diff(e14_{ell},mu6)!=0 || diff(e14_{ell},J)!=0) {{ forbidden14=0; }}",
            f"if (diff(e15_{ell},k6)!=0 || diff(e15_{ell},k2)!=0 || diff(e15_{ell},mu2)!=0 || diff(e15_{ell},mu4)!=0 || diff(e15_{ell},mu6)!=0 || diff(e15_{ell},J)!=0) {{ forbidden15=0; }}",
            f"poly C14_{ell}=subst(subst(subst(subst(e14_{ell},bs0,0),br0,0),e1,-5*k0*a1/12),e0,-5*k0*a0/12);",
            f"if (C14_{ell}!=0) {{ cancellation14=0; print(\"SQUARE_APROL_CANCELLATION_REMAINDER_{ell}\"); print(C14_{ell}); }}",
        ])
    lines.extend([
        'print("SQUARE_APROL_SIGMA14_DIVISIBLE="+string(divisible14));',
        'print("SQUARE_APROL_GRADE14_IDENTITY="+string(identity14));',
        'print("SQUARE_APROL_GRADE15_IDENTITY="+string(identity15));',
        'print("SQUARE_APROL_GRADE14_FORBIDDEN="+string(forbidden14));',
        'print("SQUARE_APROL_GRADE15_FORBIDDEN="+string(forbidden15));',
        'print("SQUARE_APROL_GRADE14_CANCELLATION="+string(cancellation14));',
        'if (divisible14*identity14*identity15*forbidden14*forbidden15*cancellation14!=1) { print("SQUARE_APROL_FAIL=SOURCE_EXTRACTION"); quit; }',
        'print("SQUARE_APROL_GRADE14_ROWS_BEGIN");',
        "print(e14_1); print(e14_2); print(e14_3); print(e14_4); print(e14_5); print(e14_6); print(e14_7);",
        'print("SQUARE_APROL_GRADE14_ROWS_END");',
        'print("SQUARE_APROL_GRADE15_ROWS_BEGIN");',
        "print(e15_1); print(e15_2); print(e15_3); print(e15_4); print(e15_5); print(e15_6); print(e15_7);",
        'print("SQUARE_APROL_GRADE15_ROWS_END");',
        "ideal Efull=e14_1,e14_2,e14_3,e14_4,e14_5,e14_6,e14_7,e15_1,e15_2,e15_3,e15_4,e15_5,e15_6,e15_7;",
        f"ring Rsmall={characteristic},(p,k0,a0,a1,aa0,aa1,bs0,br0,bs1,br1,e0,e1,ee0,ee1,k1),dp;",
        "ideal E=std(imap(Rfull,Efull));",
        "ideal Ep=std(sat(E,ideal(p)));",
        "ideal Epk=std(sat(Ep,ideal(k0)));",
        'print("SQUARE_APROL_SAT_DONE");',
        'print("SQUARE_APROL_SAT_SIZE="+string(size(Epk)));',
        'print("SQUARE_APROL_SAT_DIM="+string(dim(Epk)));',
        "ideal Rad=std(radical(Epk));",
        "int a0zero=(reduce(a0,Rad)==0);",
        "int a1zero=(reduce(a1,Rad)==0);",
        "int endpointunit=(reduce(1,Rad)==0);",
        'print("SQUARE_APROL_RADICAL_BEGIN"); print(Rad); print("SQUARE_APROL_RADICAL_END");',
        'print("SQUARE_APROL_A0_IN_RADICAL="+string(a0zero));',
        'print("SQUARE_APROL_A1_IN_RADICAL="+string(a1zero));',
        'print("SQUARE_APROL_ENDPOINT_UNIT="+string(endpointunit));',
        'if (a0zero*a1zero!=1) { print("SQUARE_APROL_FAIL=A_NOT_KILLED"); quit; }',
        'print("SQUARE_APROL_ENDPOINT=PASS_HIGH_CONTACT_A_KILLED");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED_STATIC.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen source mismatch", str(source), actual, expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"square_a_prolongation_{label}.sing"
    emit(singular, args.characteristic, tails)
    result = {
        "status": "PASS-SQUARE-A-PROLONGATION-COMPILER",
        "scope": "GENERIC_SQUARE_HIGH_CONTACT_R_GE_2_C_GE_4_ONLY_NO_FAN_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "design_sha256": digest(DESIGN),
        "input_sha256": digest(singular),
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
