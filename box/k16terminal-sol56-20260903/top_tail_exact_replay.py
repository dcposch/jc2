#!/usr/bin/env python3
"""Emit an exact TOP-TAIL job over the quadratic coefficient algebra.

The charged Laurent records store coefficients in
    A_t = Q[y]/(H_t),
where d = 2(2t+1)y-(t+1) satisfies 3*d^2=t+1.  At nonsplit t this
is an algebraic number field, so treating d as a Singular coefficient
parameter with the displayed minpoly avoids adding H_t as a polynomial
generator.  At split t the caller must request one rational d-branch at a
time; this deliberately never inverts a zero divisor in A_t.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import time

import sympy as sp


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primitive_row(expr: sp.Expr, variables: list[sp.Symbol]) -> sp.Expr:
    _denominator, cleared = sp.Poly(
        sp.expand(expr), *variables, domain=sp.QQ
    ).clear_denoms(convert=True)
    return sp.primitive(cleared.as_expr())[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--timeout", type=int, default=1200)
    parser.add_argument("--metadata", type=pathlib.Path)
    parser.add_argument(
        "--d-branch", type=sp.Rational,
        help="rational d value for one factor when 3*d^2=t+1 splits",
    )
    args = parser.parse_args()

    record = json.loads(args.record.read_text(encoding="utf-8"))
    t = int(record["t"])
    q = 2 * t + 1
    y = sp.Symbol(f"q{q}_1")
    d = sp.Symbol("d")
    b4 = sp.Symbol("b4")
    auxiliaries = [sp.Symbol("b3")]
    auxiliaries.extend(sp.Symbol(f"q{i}_0") for i in range(2, t))
    local = {str(v): v for v in [y, b4, *auxiliaries]}

    h_expected = sp.expand(
        12*q*q*y*y - 12*q*(t+1)*y + (t+1)*(3*t+2)
    )
    if sp.expand(sp.sympify(record["H"], locals=local) - h_expected) != 0:
        raise RuntimeError("record H_t does not match t")
    if record["terminal_variables"] != [
        "b3", "b4", *[f"q{i}_0" for i in range(2, t)]
    ]:
        raise RuntimeError("unexpected terminal variable order")

    if args.d_branch is None:
        d_image = d
        coefficient_spec = "(0,d)"
        minpoly = f"minpoly=d2-{sp.Rational(t+1, 3)};"
        coefficient_variables = [d, *auxiliaries]
        branch_text = "quadratic-field"
    else:
        if sp.expand(3*args.d_branch**2-(t+1)) != 0:
            raise RuntimeError("requested d branch is not a factor of H_t")
        d_image = args.d_branch
        coefficient_spec = "0"
        minpoly = ""
        coefficient_variables = auxiliaries
        branch_text = str(args.d_branch)

    rows: list[str] = []
    bands: list[int] = []
    for item in record["terminal"]:
        band = int(item["band"])
        if band < t:
            continue
        expr = sp.sympify(item["expr"], locals=local)
        expr = expr.subs({b4: 1, y: (d_image+t+1)/(2*q)})
        expr = primitive_row(expr, coefficient_variables)
        rows.append(str(expr).replace("**", "^"))
        bands.append(band)

    if bands != list(range(t, 2*t)):
        raise RuntimeError(f"unexpected top-tail bands: {bands}")

    script = "\n".join([
        "// exact fixed-t TOP-TAIL replay; generated from charged Laurent JSON",
        f"// source={args.record} sha256={sha256(args.record)}",
        f"// t={t} bands={bands} d_branch={branch_text}",
        'LIB "modstd.lib";',
        f"ring R={coefficient_spec},({','.join(map(str, auxiliaries))}),dp;",
        minpoly,
        "option(redSB);",
        "ideal I=" + ",\n".join(rows) + ";",
        "ideal G=modStd(I,1);",
        'if (reduce(1,G)==0) { print("TOP_TAIL_UNIT"); }'
        ' else { print("TOP_TAIL_NONUNIT"); }',
        'print("BASIS_SIZE");',
        "size(G);",
        "G;",
        "quit;",
        "",
    ])
    args.output.write_text(script, encoding="utf-8")
    metadata = {
        "bands": bands,
        "coefficient_algebra": (
            f"Q[d]/(d^2-{sp.Rational(t+1, 3)})"
            if args.d_branch is None else "Q"
        ),
        "d_branch": branch_text,
        "emitter": str(pathlib.Path(__file__).resolve()),
        "emitter_sha256": sha256(pathlib.Path(__file__).resolve()),
        "output": str(args.output),
        "output_sha256": hashlib.sha256(script.encode()).hexdigest(),
        "source_record": str(args.record),
        "source_record_sha256": sha256(args.record),
        "t": t,
        "typing": "exact fixed-t TOP-TAIL test; modStd exactness=1",
    }
    if args.run:
        started = time.monotonic()
        try:
            result = subprocess.run(
                ["Singular", "--cpus=4", "--threads=4", "--flint-threads=4",
                 "-q", str(args.output)],
                check=False,
                capture_output=True,
                timeout=args.timeout,
            )
            stdout = result.stdout
            stderr = result.stderr
            returncode = result.returncode
            timed_out = False
        except subprocess.TimeoutExpired as exc:
            stdout = exc.stdout or b""
            stderr = exc.stderr or b""
            returncode = 124
            timed_out = True
        elapsed = time.monotonic() - started
        out_path = args.output.with_suffix(".out")
        err_path = args.output.with_suffix(".err")
        out_path.write_bytes(stdout)
        err_path.write_bytes(stderr)
        metadata["run"] = {
            "elapsed_seconds": elapsed,
            "err_path": str(err_path),
            "err_sha256": sha256(err_path),
            "exit": returncode,
            "out_path": str(out_path),
            "out_sha256": sha256(out_path),
            "status": (
                "PROVED_UNIT"
                if returncode == 0 and b"TOP_TAIL_UNIT" in stdout
                else "INCONCLUSIVE_TIMEOUT" if timed_out
                else "NO_UNIT_CERTIFICATE"
            ),
            "timeout_seconds": args.timeout,
        }
    if args.metadata is not None:
        args.metadata.write_text(
            json.dumps(metadata, indent=2, sort_keys=True)+"\n",
            encoding="utf-8",
        )
    print(json.dumps(metadata, sort_keys=True))


if __name__ == "__main__":
    main()
