#!/usr/bin/env python3
"""Compile the exact-square affine-mu2 simultaneous-load receiver.

The payload is AWS-only.  It imports the frozen recurrence implementation
from the seven-zero-tail Pell client, retains E2=mu2 rather than E2=0, and
asks Singular for the exact reduced support and informative strata.
"""

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
PELL_COMPILER = ROOT / "cases/max12_812_order2_exact_square_pell_20260826/compile_exact_square_pell.py"
PELL_RESULT = ROOT / "cases/max12_812_order2_exact_square_pell_20260826/RESULT.md"
SUCCESSOR = ROOT / "xmodel/max12-812-order2-p0-cech-lowcontact-pell-total-rees-successor-design-20260826.md"

EXPECTED = {
    PELL_COMPILER: "b3a1aba11d181b230bf03a6ca46fd9355753c45758706d8887a8aeb7a0bbf1cd",
    PELL_RESULT: "2b42cf9f0f28818341ccb63de5af3accf72c5dc3026f4ebe6aec17898f1d2f85",
    SUCCESSOR: "99e45e341925ceb9a01843b4dd36ab99218f97055449c203e792e91e38244434",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only affine-mu2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only affine-mu2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_pell_module():
    spec = importlib.util.spec_from_file_location("frozen_exact_square_pell", PELL_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot load frozen Pell compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, characteristic: int, pell) -> list[int]:
    equations = pell.tail_equations()
    texts = [pell.singular_text(poly) for _, poly in equations]
    denominators = [denominator for denominator, _ in equations]
    lines = [
        'LIB "primdec.lib";',
        f"ring R={characteristic},(mu2,gamma,beta,r,c,p),dp;",
        "proc idealZero(ideal A, ideal G)",
        "{",
        "  int i;",
        "  for (i=1; i<=size(A); i++) { if (reduce(A[i],G)!=0) { return(0); } }",
        "  return(1);",
        "}",
    ]
    for ell, (denominator, text) in enumerate(zip(denominators, texts), start=1):
        lines.append(f"poly E{ell}={text};")
        lines.append(f'print("AFFINE_MU2_E{ell}_DENOMINATOR={denominator}");')
    lines.extend(
        [
            "ideal I=E1,E2-1024*mu2,E3,E4,E5,E6,E7;",
            "ideal Raw=std(I);",
            "ideal Rad=std(radical(Raw));",
            "poly Delta=p^2-4*r;",
            "ideal Square=std(ideal(c,Delta,mu2));",
            "ideal Chebyshev=std(ideal(c,16*beta-5*Delta,256*gamma-5*Delta^2,mu2));",
            "ideal P0Target=std(ideal(c,p,5*r^2+8*r*beta+16*gamma,32*mu2-r^2*(5*r+4*beta)));",
            "ideal Expected=std(intersect(intersect(Square,Chebyshev),P0Target));",
            "int expectedSolutions=idealZero(I,Expected);",
            "int radInExpected=idealZero(Rad,Expected);",
            "int expectedInRad=idealZero(Expected,Rad);",
            "ideal OffC=std(sat(Raw,ideal(c)));",
            "ideal C0=std(Raw+ideal(c));",
            "ideal C0PNonzero=std(sat(C0,ideal(p)));",
            "ideal C0P0=std(C0+ideal(p));",
            "ideal C0P0RNonzero=std(sat(C0P0,ideal(r)));",
            'print("AFFINE_MU2_RAW_BEGIN"); print(Raw); print("AFFINE_MU2_RAW_END");',
            'print("AFFINE_MU2_RADICAL_BEGIN"); print(Rad); print("AFFINE_MU2_RADICAL_END");',
            'print("AFFINE_MU2_EXPECTED_BEGIN"); print(Expected); print("AFFINE_MU2_EXPECTED_END");',
            'print("AFFINE_MU2_OFF_C_BEGIN"); print(OffC); print("AFFINE_MU2_OFF_C_END");',
            'print("AFFINE_MU2_C0_PNONZERO_BEGIN"); print(C0PNonzero); print("AFFINE_MU2_C0_PNONZERO_END");',
            'print("AFFINE_MU2_C0_P0_BEGIN"); print(C0P0); print("AFFINE_MU2_C0_P0_END");',
            'print("AFFINE_MU2_C0_P0_RNONZERO_BEGIN"); print(C0P0RNonzero); print("AFFINE_MU2_C0_P0_RNONZERO_END");',
            'print("AFFINE_MU2_RAW_DIM="+string(dim(Raw)));',
            'print("AFFINE_MU2_RADICAL_SIZE="+string(size(Rad)));',
            'print("AFFINE_MU2_EXPECTED_SOLUTIONS="+string(expectedSolutions));',
            'print("AFFINE_MU2_RAD_IN_EXPECTED="+string(radInExpected));',
            'print("AFFINE_MU2_EXPECTED_IN_RAD="+string(expectedInRad));',
            "list Ass=minAssGTZ(Raw);",
            'print("AFFINE_MU2_MINASS_COUNT="+string(size(Ass)));',
            "int ai;",
            "for (ai=1; ai<=size(Ass); ai++) {",
            '  print("AFFINE_MU2_MINASS_"+string(ai)+"_BEGIN");',
            "  print(std(Ass[ai]));",
            '  print("AFFINE_MU2_MINASS_"+string(ai)+"_END");',
            "}",
            'if (expectedSolutions*radInExpected*expectedInRad==1) { print("AFFINE_MU2_ENDPOINT=PROPOSED_THREE_COMPONENT_UNION"); }',
            'else { print("AFFINE_MU2_ENDPOINT=EXTRA_OR_MISSING_COMPONENT"); }',
            'print("AFFINE_MU2_PROBE_DONE=1");',
            'print("AFFINE_MU2_SCOPE=EXACT_SQUARE_AFFINE_TARGET_SUPPORT_ONLY_NO_REES_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
            "quit;",
        ]
    )
    path.write_text("\n".join(lines) + "\n")
    return denominators


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen source mismatch", str(source), actual, expected))
    pell = load_pell_module()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"affine_mu2_{label}.sing"
    denominators = emit(singular, args.characteristic, pell)
    result = {
        "status": "PASS-AFFINE-MU2-COMPILER",
        "scope": "EXACT_SQUARE_AFFINE_MU2_SUPPORT_PROBE_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "equation_denominators": denominators,
        "charged_sha256": {str(path.relative_to(ROOT)): digest(path) for path in EXPECTED},
        "input_sha256": digest(singular),
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
