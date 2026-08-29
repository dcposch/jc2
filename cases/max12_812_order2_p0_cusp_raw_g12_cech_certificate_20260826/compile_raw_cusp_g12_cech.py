#!/usr/bin/env python3
"""Compile the unparameterized raw p=0 cusp grade-12 certificate (AWS only)."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OWNER = ROOT / "cases/max12_812_order2_p0_cusp_g10_g11_20260826/compile_p0_cusp_g10_g11.py"
OWNER_FREEZE = ROOT / "cases/max12_812_order2_p0_cusp_g10_g11_20260826/FREEZE.sha256"
DESIGN = ROOT / "xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md"
EXPECTED = {
    OWNER: "9d49988213806d42ea4523881595837007fa861369f31fd18d0c83b7adf494d4",
    OWNER_FREEZE: "8fe97cd6972cc1f92d2380bfec4b7a7db6e6b71c1b2a348eb749f3bf71aaaa67",
    DESIGN: "6995a991b1e7803a26bbf5374b10d54a0cda7d17158ad9f1595db76218aadb92",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_owner():
    spec = importlib.util.spec_from_file_location("p0_cusp_g1011_owner", OWNER)
    if spec is None or spec.loader is None:
        fail("cannot load frozen p0 cusp grade-10/11 owner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def append_certificate(script: Path) -> None:
    text = script.read_text()
    anchor = (
        'print("P0_CUSP_G10_G11_ENDPOINT=PASS_EXACT_SOURCE_RAW_CHART_AND_TRIANGULAR_PROLONGATION");\n'
        "quit;\n"
    )
    if text.count(anchor) != 1:
        fail("frozen owner endpoint anchor missing or nonunique")

    lines = [
        'print("P0_CUSP_G10_G11_ENDPOINT=PASS_EXACT_SOURCE_RAW_CHART_AND_TRIANGULAR_PROLONGATION");',
        "int div12=1; int quotient12=1; int lateLoads12=1;",
    ]
    for ell in range(1, 8):
        lines.extend(
            [
                f"poly Rem12_{ell}=Q11_{ell}-g11_{ell};",
                f"if (reduce(Rem12_{ell},Sigma1)!=0) {{ div12=0; }}",
                f"poly Q12_{ell}=Rem12_{ell}/sigma;",
                f"if (sigma*Q12_{ell}-Rem12_{ell}!=0) {{ quotient12=0; }}",
                f"poly g12_{ell}=subst(Q12_{ell},sigma,0);",
                f"if (diff(g12_{ell},k6)!=0 || diff(g12_{ell},k6_1)!=0 || diff(g12_{ell},k2)!=0 || diff(g12_{ell},k2_1)!=0 || diff(g12_{ell},mu2)!=0 || diff(g12_{ell},mu4)!=0 || diff(g12_{ell},mu6)!=0 || diff(g12_{ell},J)!=0) {{ lateLoads12=0; }}",
            ]
        )
    lines.extend(
        [
            'print("P0_CUSP_RAW_G12_DIVISIBLE="+string(div12));',
            'print("P0_CUSP_RAW_G12_QUOTIENT_IDENTITIES="+string(quotient12));',
            'print("P0_CUSP_RAW_G12_LATER_LOADS_TARGETS_ABSENT="+string(lateLoads12));',
            'print("P0_CUSP_RAW_G12_ROW6_BEGIN"); print(g12_6); print("P0_CUSP_RAW_G12_ROW6_END");',
            "poly ExpectedRow6=-(3/128)*rs*c1^2-(3/32)*rs*a0*c0-(3/16)*cs*c0*c1-(5/32768)*k*rs^4;",
            "int literalRow6=(g12_6-ExpectedRow6==0);",
            'print("P0_CUSP_RAW_G12_LITERAL_ROW6="+string(literalRow6));',
            "poly DirectCert=32768*g12_6-35*k*rs^4+8192*rs*g10_2+32768*cs*g10_3;",
            "int directCert=(DirectCert==0);",
            'print("P0_CUSP_RAW_G12_DIRECT_CERTIFICATE="+string(directCert));',
            "poly OmitNilpotentRow=32768*g12_6-35*k*rs^4+8192*rs*g10_2;",
            "int negativeControl=(OmitNilpotentRow==-6144*cs*c0*c1 && OmitNilpotentRow!=0);",
            'print("P0_CUSP_RAW_G12_OMIT_G10_3_NEGATIVE_CONTROL="+string(negativeControl));',
            'print("P0_CUSP_RAW_G12_CERTIFICATE_TEXT=32768*g12_6-35*k*rs^4=-8192*rs*g10_2-32768*cs*g10_3");',
            "if (div12*quotient12*lateLoads12*literalRow6*directCert*negativeControl!=1) { print(\"P0_CUSP_RAW_G12_FAIL=CERTIFICATE_OR_SOURCE_COMPLETENESS\"); quit; }",
            'print("P0_CUSP_RAW_G12_CECH_ENDPOINT=PASS_DIRECT_REGISTERED_UNIT_CERTIFICATE");',
            "quit;",
        ]
    )
    script.write_text(text.replace(anchor, "\n".join(lines) + "\n"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()

    owner = load_owner()
    tag = owner.require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen wrapper source mismatch", str(source), actual, expected))
    for source, expected in owner.EXPECTED_STATIC.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen owner transitive mismatch", str(source), actual, expected))
    tails = json.loads(owner.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != owner.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"p0_cusp_raw_g12_cech_{label}.sing"
    owner.emit(singular, args.characteristic, tails)
    append_certificate(singular)
    source_text = singular.read_text()
    result = {
        "status": "PASS-P0-CUSP-RAW-G12-CECH-COMPILER",
        "scope": "POST_M0_FIXED_P0_D_K0_RS_RAW_CUSP_CHART_ONLY_NO_TOTAL_REES_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "owner_sha256": digest(OWNER),
        "design_sha256": digest(DESIGN),
        "tails_sha256": digest(owner.TAILS),
        "input_sha256": digest(singular),
        "source_occurrences": {
            "k6": source_text.count("k6"),
            "k2": source_text.count("k2"),
            "mu2": source_text.count("mu2"),
            "mu4": source_text.count("mu4"),
            "mu6": source_text.count("mu6"),
            "J": source_text.count("J"),
        },
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
