#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V23 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827"
RESULT = V23 / "output_r1/RESULT.json"
RESULT_SHA = "ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641"
PARSER = V23 / "census_j2_typed_v23.py"
PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(x: object) -> "None":
    raise RuntimeError(x)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: compile_a1_rho0_v26.py OUTPUT")
    if platform.system() != "Linux" or not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        fail("registered AWS lane required")
    if Path("/sys/class/dmi/id/sys_vendor").read_text().strip() != "Amazon EC2":
        fail("Amazon EC2 required")
    out = Path(sys.argv[1]).resolve()
    if out.exists():
        fail(("refuse overwrite", str(out)))
    out.mkdir(parents=True)
    if digest(RESULT) != RESULT_SHA or digest(PARSER) != PARSER_SHA:
        fail("upstream hash")
    spec = importlib.util.spec_from_file_location("v26_parser", PARSER)
    if spec is None or spec.loader is None:
        fail("parser import")
    v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
    result = json.loads(RESULT.read_text())
    rows = []
    variables = {"a1"}
    zero10 = 0
    hashes = {}
    for name, rec in sorted(result["records"].items(), key=lambda x: (x[1]["grade"], x[1]["row"])):
        cr = rec["charts"]["a1_ordered"]
        path = V23 / "output_r1" / cr["output"]
        if digest(path) != cr["output_sha256"]:
            fail(("row hash", name))
        p = v.specialize(v.parse(path), frozenset({"rho"}), {})
        grade = int(rec["grade"])
        if grade == 10 and not p:
            zero10 += 1
        for monomial in p:
            if sum(v.sigma_weight(x)*e for x,e in monomial) != grade:
                fail(("weight", name))
            variables.update(x for x,_ in monomial)
        rows.append((name, grade, v.polynomial_text(p), bool(p)))
        hashes[str(path.relative_to(ROOT))] = cr["output_sha256"]
    if zero10 != 7:
        fail(("grade10", zero10))
    ordered = sorted(variables, key=lambda x: (v.sigma_weight(x),x))
    weights = [v.sigma_weight(x) for x in ordered]
    nonzero = [(n,g,t) for n,g,t,b in rows if b]
    positive = next(n for n,g,_ in nonzero if g == 11)
    lines = [
        "ring R=0,("+",".join(ordered)+"),wp("+",".join(map(str,weights))+");",
        "option(redSB);",
    ]
    for n,_,t in nonzero:
        lines.append(f"poly P_{n}={t};")
    lines += [
        "ideal I="+",".join("P_"+n for n,_,_ in nonzero)+";",
        "degBound=15;",
        "ideal G=std(I);",
        "poly neg=a1^2;",
        "if (reduce(neg,G)!=neg) { print(\"FAIL_NEG\"); quit; }",
        f"if (reduce(P_{positive},G)!=0) {{ print(\"FAIL_POS\"); quit; }}",
        "poly target=a1^3;",
        "poly nf=reduce(target,G);",
        "print(\"V26_CONTROLS=1\");",
        "if (nf==0)",
        "{",
        " matrix L=lift(I,ideal(target)); poly replay=-target; int j;",
        " for (j=1;j<=size(I);j=j+1) { replay=replay+L[j,1]*I[j]; }",
        " if (replay!=0) { print(\"FAIL_REPLAY\"); quit; }",
        f" write(\":w {out/'LIFT.txt'}\",string(L));",
        " print(\"V26_A1_CUBIC_RHO0_MEMBERSHIP=1\");",
        "}",
        "else",
        "{",
        f" write(\":w {out/'NF.txt'}\",string(nf));",
        " print(\"V26_A1_CUBIC_RHO0_MEMBERSHIP=0\");",
        "}",
        "print(\"PASS_A1_RHO0_SCREEN_V26\"); quit;",
    ]
    script = out / "screen.sing"; script.write_text("\n".join(lines)+"\n")
    compiled = {
        "status":"PASS-A1-RHO0-V26-COMPILER", "input_rows":42,
        "nonzero_rows":len(nonzero), "row_sha256":hashes,
        "variables":ordered, "weights":weights, "script":str(script),
        "script_sha256":digest(script), "target":"a1^3", "degree_bound":15,
    }
    (out/"compile_result.json").write_text(json.dumps(compiled,sort_keys=True,indent=2)+"\n")
    print("PASS-A1-RHO0-V26-COMPILER")


if __name__ == "__main__": main()
