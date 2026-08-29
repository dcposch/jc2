#!/usr/bin/env python3
"""Tracked modular unit-certificate producer for the V24 exact-Q fallback."""

from __future__ import annotations

import argparse
import ast
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess


HERE = Path(__file__).resolve().parent
ORIGINAL = HERE / "aws_r6b_pass/output/modular_prior_reduction_v24.sing"
V24_RESULT = HERE / "aws_r6b_pass/output/RESULT.json"
R1_RESULT = HERE / "aws_r6b_r1_unit/output/RESULT.json"
R3_RESULT = HERE / "aws_box02_r3_multiprime/output/RESULT.json"
R4_DESIGN = HERE / "PREREGISTRATION_R4_MODULAR_CERTIFICATE_LIFT.md"
PREREG = HERE / "PREREGISTRATION_R4A_MODULAR_CERTIFICATES.md"
PRIMES = (1000003, 2147483629, 2147483587, 2147483579,
          2147483563, 2147483549, 2147483543, 2147483497)
EXPECTED = {
    ORIGINAL: "6f5e8fac9d8f1d06c5a06a3b3f67b1bce776418d977bf6ea80ca064c9fc5b96a",
    V24_RESULT: "22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b",
    R1_RESULT: "10cfdfea0c20554d6a65bac99a009bad23fee9babcb62c80f11ed86ee8a96ea4",
    R3_RESULT: "413216635dd886a0e5e4893bfa74491a4fe3265cde80603bbf8c641f66b5d16c",
    R4_DESIGN: "92e6b7362b6d60808b53e8fbbbde9a7d949691548b6f4fcc458ff0bf1e6f6e9e",
    PREREG: "d9f60ef1589f864c12aae28d18ee70a86c309976e625c8d93ff453690c960bcf",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V24R4A compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V24R4A compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def add(left: dict[tuple[int, ...], int], right: dict[tuple[int, ...], int],
        prime: int, scale: int = 1) -> dict[tuple[int, ...], int]:
    out = dict(left)
    for key, value in right.items():
        new = (out.get(key, 0) + scale * value) % prime
        if new:
            out[key] = new
        elif key in out:
            del out[key]
    return out


def mul(left: dict[tuple[int, ...], int], right: dict[tuple[int, ...], int],
        prime: int) -> dict[tuple[int, ...], int]:
    out: dict[tuple[int, ...], int] = {}
    for akey, avalue in left.items():
        for bkey, bvalue in right.items():
            key = tuple(a + b for a, b in zip(akey, bkey))
            out[key] = (out.get(key, 0) + avalue * bvalue) % prime
            if not out[key]:
                del out[key]
    return out


def power(poly: dict[tuple[int, ...], int], exponent: int,
          prime: int, zero: tuple[int, ...]) -> dict[tuple[int, ...], int]:
    if exponent < 0:
        fail("negative exponent in certificate")
    out = {zero: 1}
    base = poly
    while exponent:
        if exponent & 1:
            out = mul(out, base, prime)
        exponent >>= 1
        if exponent:
            base = mul(base, base, prime)
    return out


def parse_certificate(text: str, variables: tuple[str, ...],
                      prime: int) -> dict[tuple[int, ...], int]:
    source = "".join(text.split())
    zero = (0,) * len(variables)
    index = {name: i for i, name in enumerate(variables)}
    if source == "0":
        return {}
    if not source or any(char in source for char in ';,"'):
        fail(("malformed certificate polynomial", source[:120]))

    def evaluate(node: ast.AST) -> dict[tuple[int, ...], int]:
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            value = node.value % prime
            return {} if value == 0 else {zero: value}
        if isinstance(node, ast.Name) and node.id in index:
            key = [0] * len(variables)
            key[index[node.id]] = 1
            return {tuple(key): 1}
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = evaluate(node.operand)
            return value if isinstance(node.op, ast.UAdd) else {
                key: (-coefficient) % prime for key, coefficient in value.items()}
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, ast.Add):
                return add(evaluate(node.left), evaluate(node.right), prime)
            if isinstance(node.op, ast.Sub):
                return add(evaluate(node.left), evaluate(node.right), prime, -1)
            if isinstance(node.op, ast.Mult):
                return mul(evaluate(node.left), evaluate(node.right), prime)
            if isinstance(node.op, ast.Pow) and isinstance(node.right, ast.Constant) \
                    and isinstance(node.right.value, int):
                return power(evaluate(node.left), node.right.value, prime, zero)
        fail(("unsupported certificate syntax", ast.dump(node)))

    return evaluate(ast.parse(source.replace("^", "**"), mode="eval").body)


def run_prime(prime: int, lines: list[str], variables: tuple[str, ...],
              output: Path, singular: str) -> dict[str, object]:
    lane = output / f"p{prime}"
    lane.mkdir()
    ring = lines[0].replace("ring R=65521,", f"ring R={prime},", 1)
    if not ring.startswith(f"ring R={prime},"):
        fail(("field conversion failed", prime))
    script = lane / "tracked_unit_certificate.sing"
    certificate_paths = [lane / f"CERT_{i:02d}.txt" for i in range(1, 37)]
    program = [
        ring,
        lines[1],
        lines[2],
        f'if (size(P)!=36) {{ print("V24R4A_P{prime}_FAIL=GENERATOR_CENSUS"); quit; }}',
        "matrix T; ideal G=liftstd(P,T);",
        "matrix BREPLAY=matrix(P)*T-matrix(G);",
        f'if (BREPLAY!=0) {{ print("V24R4A_P{prime}_FAIL=BASIS_REPLAY"); quit; }}',
        "poly N1=reduce(1,G); int D=dim(G);",
        f'if ((N1!=0)||(D!=-1)||(size(G)!=1)||(G[1]!=1)) {{ print("V24R4A_P{prime}_FAIL=NOT_UNIT"); quit; }}',
        "matrix H=lift(G,ideal(1)); matrix C=T*H;",
        "matrix CREPLAY=matrix(P)*C-matrix(ideal(1));",
        f'if (CREPLAY!=0) {{ print("V24R4A_P{prime}_FAIL=CERTIFICATE_REPLAY"); quit; }}',
        "matrix Cbad=C; Cbad[1,1]=Cbad[1,1]+1;",
        f'if (matrix(P)*Cbad-matrix(ideal(1))==0) {{ print("V24R4A_P{prime}_FAIL=COEFFICIENT_MUTATION"); quit; }}',
        "ideal Pbad=P; poly SWAP=Pbad[1]; Pbad[1]=Pbad[2]; Pbad[2]=SWAP;",
        f'if (matrix(Pbad)*C-matrix(ideal(1))==0) {{ print("V24R4A_P{prime}_FAIL=ORDER_MUTATION"); quit; }}',
    ]
    for index_value, path in enumerate(certificate_paths, 1):
        safe = str(path.resolve())
        if '"' in safe or "\n" in safe:
            fail(("unsafe certificate path", safe))
        program.append(f'write("{safe}",C[{index_value},1]);')
    program.extend([
        f'print("V24R4A_P{prime}_BASIS_REPLAY=1");',
        f'print("V24R4A_P{prime}_CERTIFICATE_REPLAY=1");',
        f'print("V24R4A_P{prime}_MUTATIONS=1");',
        "quit;",
    ])
    script.write_text("\n".join(program) + "\n")
    try:
        completed = subprocess.run(
            [singular, "-q", str(script)], cwd=lane, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1200)
    except subprocess.TimeoutExpired as error:
        (lane / "singular.stdout").write_text(error.stdout or "")
        (lane / "singular.stderr").write_text(error.stderr or "")
        return {"prime": prime, "status": "RESOURCE_CAP",
                "script_sha256": digest(script)}
    (lane / "singular.stdout").write_text(completed.stdout)
    (lane / "singular.stderr").write_text(completed.stderr)
    required = (f"V24R4A_P{prime}_BASIS_REPLAY=1",
                f"V24R4A_P{prime}_CERTIFICATE_REPLAY=1",
                f"V24R4A_P{prime}_MUTATIONS=1")
    if completed.returncode != 0 or completed.stderr or \
            any(marker not in completed.stdout for marker in required) or \
            f"V24R4A_P{prime}_FAIL=" in completed.stdout:
        fail(("modular tracked certificate failure", prime,
              completed.returncode, completed.stderr[-1000:],
              completed.stdout[-2000:]))
    if not all(path.is_file() for path in certificate_paths):
        fail(("missing certificate entry", prime))
    parsed = [parse_certificate(path.read_text(), variables, prime)
              for path in certificate_paths]
    canonical = []
    for poly in parsed:
        canonical.append([[list(key), int(value)]
                          for key, value in sorted(poly.items())])
    canonical_path = lane / "CERTIFICATE_CANONICAL.json"
    canonical_path.write_text(json.dumps(canonical, separators=(",", ":")) + "\n")
    support = [[list(key) for key in sorted(poly)] for poly in parsed]
    support_bytes = json.dumps(support, separators=(",", ":")).encode()
    return {
        "prime": prime,
        "status": "UNIT_CERTIFICATE_REPLAYED",
        "script_sha256": digest(script),
        "canonical_certificate_sha256": digest(canonical_path),
        "support_sha256": sha256(support_bytes).hexdigest(),
        "support_term_counts": [len(poly) for poly in parsed],
        "certificate_entry_sha256": [digest(path) for path in certificate_paths],
        "basis_replay": True,
        "certificate_replay": True,
        "coefficient_and_order_mutations": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, wanted in EXPECTED.items():
        got = digest(path)
        if wanted == "TO_BE_FROZEN" or got != wanted:
            fail(("frozen input mismatch", str(path), got, wanted))
    r1 = json.loads(R1_RESULT.read_text())
    if r1.get("status") != "F65521_LOCALIZED_PRIOR_IDEAL_IS_UNIT_NO_MEMBERSHIP_CONCLUSION":
        fail("V24R1 dependency mismatch")
    lines = ORIGINAL.read_text().splitlines()
    if len(lines) != 11 or not lines[0].startswith("ring R=65521,"):
        fail("V24 script shape mismatch")
    match = re.fullmatch(r"ring R=65521,\(([^)]+)\),dp;", lines[0])
    if match is None:
        fail("variable declaration mismatch")
    variables = tuple(match.group(1).split(","))
    if len(variables) != 34 or variables[-1] != "zinv":
        fail(("variable census mismatch", len(variables), variables[-1]))
    denominators = [int(value) for value in re.findall(r"/([0-9]+)", lines[1] + lines[2])]
    if not denominators or any(math.gcd(prime, denominator) != 1
                               for prime in PRIMES for denominator in denominators):
        fail("source denominator is not invertible at a registered prime")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    with ThreadPoolExecutor(max_workers=len(PRIMES)) as pool:
        futures = [pool.submit(run_prime, prime, lines, variables, output, singular)
                   for prime in PRIMES]
        outcomes = [future.result() for future in futures]
    outcomes.sort(key=lambda item: int(item["prime"]))
    if any(item["status"] == "RESOURCE_CAP" for item in outcomes):
        status = "RESOURCE_CAP_NO_VERDICT"
    else:
        support_hashes = {str(item["support_sha256"]) for item in outcomes}
        status = ("PASS_MODULAR_UNIT_CERTIFICATES_STABLE_SUPPORT_READY_FOR_EXACT_LIFT"
                  if len(support_hashes) == 1 else
                  "PASS_MODULAR_UNIT_CERTIFICATES_SUPPORT_VARIES_NO_EXACT_LIFT_YET")
    payload = {
        "status": status,
        "registered_aws_lane": tag,
        "primes": list(PRIMES),
        "outcomes": outcomes,
        "input_sha256": {str(path.relative_to(HERE.parents[1])): digest(path)
                         for path in EXPECTED},
        "scope": "TRACKED_MODULAR_UNIT_CERTIFICATE_SUPPORT_DISCOVERY_ONLY",
        "firewall": "NO_EXACT_Q_NO_CHART_EMPTY_NO_STRATUM_NO_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V24R4A=" + status)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
