#!/usr/bin/env python3
"""Emit and optionally run the Laurent/Euler terminal recurrence in Singular.

The generated calculation is the fixed-integer specialization of the indexed
recurrence in the accompanying report.  It never divides in the rank-two
algebra at a split index: ``--mode split-exact`` and ``--mode mod`` specialize
``y`` first and run one product factor at a time.

The terminal polynomials printed by the frozen discovery driver are ``-E``.
Here ``T[k]`` is defined with the sign in the question, namely ``+E``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import re
import subprocess
import time

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent


def h_polynomial(t: int, yy: sp.Symbol) -> sp.Expr:
    q = 2 * t + 1
    return sp.expand(12 * q * q * yy**2 - 12 * q * (t + 1) * yy
                     + (t + 1) * (3 * t + 2))


def modular_roots(t: int, prime: int) -> list[int]:
    yy = sp.Symbol("yy")
    poly = sp.Poly(h_polynomial(t, yy), yy, modulus=prime)
    roots = sorted({int(root) % prime for root in range(prime)
                    if int(poly.eval(root)) % prime == 0})
    if len(roots) != 2:
        raise ValueError(f"H_{t} has {len(roots)} distinct roots modulo {prime}")
    return roots


def split_roots(t: int) -> list[sp.Rational]:
    quotient, remainder = divmod(t + 1, 3)
    root = math.isqrt(quotient)
    if remainder or root * root != quotient:
        raise ValueError(f"t={t} is not of the form 3*s^2-1")
    q = 2 * t + 1
    return sorted({sp.Rational(t + 1 - root, 2 * q),
                   sp.Rational(t + 1 + root, 2 * q)})


def singular_rational(value: sp.Rational) -> str:
    return f"({int(value.p)}/{int(value.q)})"


def ring_header(t: int, mode: str, prime: int | None,
                branch: int | None, variables: list[str]) -> tuple[list[str], str]:
    yy = sp.Symbol("yy")
    H = h_polynomial(t, yy)
    if mode == "exact":
        if not sp.Poly(H, yy, domain=sp.QQ).is_irreducible:
            raise ValueError("exact algebraic mode requires irreducible H_t")
        lines = [f"ring R=(0,yy),({','.join(variables)}),dp;",
                 f"minpoly={str(H).replace('**', '^')};"]
        return lines, "Q[y]/(H_t)"
    if branch not in (0, 1):
        raise ValueError("a branch index 0 or 1 is required")
    if mode == "split-exact":
        value = split_roots(t)[branch]
        lines = [f"ring R=0,({','.join(variables)}),dp;",
                 f"number yy={singular_rational(value)};"]
        return lines, f"Q, y={value}"
    if mode == "mod":
        if prime is None or prime <= 2:
            raise ValueError("--prime is required in modular mode")
        value = modular_roots(t, prime)[branch]
        lines = [f"ring R={prime},({','.join(variables)}),dp;",
                 f"number yy={value};"]
        return lines, f"F_{prime}, y={value}"
    raise ValueError(mode)


def chart_ring_header(t: int, mode: str, prime: int | None,
                      branch: int | None, variables: list[str]) -> list[str]:
    lines, _description = ring_header(t, mode, prime, branch, variables)
    return [line.replace("ring R=", "ring C=", 1) for line in lines]


def emit(t: int, mode: str, prime: int | None, branch: int | None,
         charts: str, algorithm: str, compare_record: pathlib.Path | None,
         dump_rows: bool, specialize_b4: int | None) -> tuple[str, dict[str, object]]:
    if t < 2:
        raise ValueError("the stable Laurent/Euler recurrence starts at t=2")
    if algorithm not in ("std", "slimgb", "modstd"):
        raise ValueError(algorithm)
    basis = (lambda ideal: f"modStd({ideal},1)" if algorithm == "modstd"
             else f"{algorithm}({ideal})")
    q, e, N = 2 * t + 1, 3 * t + 1, 4 * t + 1
    cvars = [f"C{j}" for j in range(1, t)]
    qvars = [f"q{j}_0" for j in range(2, 2 * t + 1)]
    residual = ["b3"] + [f"q{j}_0" for j in range(2, t)]
    variables = ["h", "s", "b1", "b2", "b3", "b4", "B0"] + cvars + qvars
    header, coefficient_algebra = ring_header(t, mode, prime, branch, variables)
    lines: list[str] = [
        "// Generated Laurent/Euler terminal recurrence.",
        f"// t={t} mode={mode} branch={branch} charts={charts}",
        *header,
        "option(redSB);",
        *( ["LIB \"modstd.lib\";"] if algorithm == "modstd" else [] ),
        "proc hcoef(poly f, int k)",
        "{",
        "  matrix M=coef(f,h);",
        "  int ii;",
        "  for (ii=1; ii<=ncols(M); ii++)",
        "  { if (M[1,ii]==h^k) { return(M[2,ii]); } }",
        "  return(0);",
        "}",
        "proc eulerInverse(poly f)",
        "{",
        "  matrix M=coef(f,s);",
        "  poly answer=0; int ii; int mm;",
        "  for (ii=1; ii<=ncols(M); ii++)",
        "  { mm=deg(M[1,ii]); answer=answer+M[2,ii]*M[1,ii]/((2*mm+1)*yy); }",
        "  return(answer);",
        "}",
        f"number g1={e}/{q};",
        f"number g2=({e}/{q})*yy+({e*t}/{2*q*q});",
        f"number g3=({e*t}/{q*q})*yy-({e*t*(t+1)}/{6*q**3});",
        "number cc=-yy*g3;",
    ]
    b4_image = "b4" if specialize_b4 is None else str(specialize_b4)
    U_terms = [f"h^{q}"] + [f"q{j}_0*h^{q-j}" for j in range(2, 2*t + 1)]
    C_terms = [f"h^{t-1}"] + [f"C{j}*h^{t-1-j}" for j in range(1, t)]
    lines += [
        "poly Uh=" + "+".join(U_terms) + ";",
        "poly Ch=" + "+".join(C_terms) + ";",
        f"poly U=subst(Uh,h,s+{b4_image});",
        f"poly Cp=subst(Ch,h,s+{b4_image});",
        "poly A=s*Cp;",
        "poly Bprime=g3*(5*Cp+3*s*diff(Cp,s))/(2*yy);",
        "matrix MB=coef(Bprime,s);",
        "poly B=B0; int ii; int mm;",
        "for (ii=1; ii<=ncols(MB); ii++)",
        "{ mm=deg(MB[1,ii]); B=B+MB[2,ii]*s*MB[1,ii]/(mm+1); }",
        "if (diff(B,s)-Bprime!=0) { print(\"FAIL B derivative\"); exit(2); }",
        "poly rhsD=3*g3*diff(U,s)+A*B-s*A*diff(B,s)+2*s*diff(A,s)*B",
        "          +g3*b3*(A/s+(5/2)*diff(A,s));",
        "poly D=eulerInverse(rhsD);",
        "if (yy*(D+2*s*diff(D,s))-rhsD!=0) { print(\"FAIL Euler inverse\"); exit(2); }",
        "poly Q1=s*A-yy*b3;",
        "poly Y=s*D-b3*B-g3*b2;",
        "poly Z=s*B-g3*b3;",
        "poly numD1=yy*g3*b1-Q1*diff(Y,s)+diff(Q1,s)*Y+2*diff(U,s)*Z;",
        "poly constantS=subst(numD1,s,0);",
        "poly pb1=diff(constantS,b1);",
        "poly b1rhs=-subst(constantS,b1,0)/pb1;",
        "numD1=subst(numD1,b1,b1rhs);",
        "if (subst(numD1,s,0)!=0) { print(\"FAIL b1 divisibility\"); exit(2); }",
        "poly Xprime=numD1/(2*yy*s);",
        f"poly gauge=hcoef(subst(Xprime,s,h-{b4_image}),{q-1});",
        "poly pB0=diff(gauge,B0);",
        "poly B0rhs=-subst(gauge,B0,0)/pB0;",
        "B=subst(B,B0,B0rhs);",
        "D=subst(D,B0,B0rhs);",
        "Y=subst(Y,B0,B0rhs);",
        "Z=subst(Z,B0,B0rhs);",
        "Xprime=subst(Xprime,B0,B0rhs);",
        "b1rhs=subst(b1rhs,B0,B0rhs);",
        "if (subst(gauge,B0,B0rhs)!=0) { print(\"FAIL B0 gauge\"); exit(2); }",
        "// RR is -E.  The requested terminal row is T[k]=-hcoef(RR,h,k).",
        "poly RR=Q1*Xprime-diff(U,s)*Y-yy*g3;",
        f"poly Rh=subst(RR,s,h-{b4_image});",
    ]
    elimination = cvars + [f"q{j}_0" for j in range(t, 2*t + 1)] + ["b2"]
    pivot_rows: list[dict[str, object]] = []
    for weight, variable in enumerate(elimination, start=1):
        band = N - weight
        lines += [
            f"poly W{weight}=hcoef(Rh,{band});",
            f"poly p{weight}=diff(W{weight},{variable});",
            f"poly v{weight}rhs=-subst(W{weight},{variable},0)/p{weight};",
            f"if (subst(W{weight},{variable},v{weight}rhs)!=0) "
            f"{{ print(\"FAIL pivot {weight}\"); exit(2); }}",
            f"Rh=subst(Rh,{variable},v{weight}rhs);",
            f"print(\"PIVOT weight={weight} band={band} variable={variable}\"); p{weight};",
        ]
        pivot_rows.append({"weight": weight, "band": band, "variable": variable})
    for band in range(2*t, N + 1):
        lines.append(f"if (hcoef(Rh,{band})!=0) {{ print(\"FAIL high band {band}\"); exit(2); }}")
    for band in range(0, 2*t):
        lines.append(f"poly T{band}=-hcoef(Rh,{band});")
        lines.append(f"print(\"TERMINAL band={band}\"); deg(T{band}); size(T{band});")
        if dump_rows:
            lines.append(f"print(\"TROW band={band}\"); T{band};")
    lines.append(f"print(\"RECURRENCE_PASS t={t} rows={2*t}\");")

    comparison_metadata: dict[str, object] | None = None
    if compare_record is not None:
        raw = compare_record.read_bytes()
        record = json.loads(raw)
        if int(record["t"]) != t or len(record["terminal"]) != 2*t:
            raise ValueError("comparison record has the wrong t or row count")
        for item in record["terminal"]:
            band = int(item["band"])
            expression = str(item["expr"]).replace(f"q{q}_1", "yy").replace("**", "^")
            # Singular can parse ``x^2/large_integer`` as a non-integral
            # exponent.  Multiplication by an explicitly parenthesized base
            # coefficient is unambiguous.
            expression = re.sub(r"/(\d+)", r"*(1/\1)", expression)
            lines += [f"poly Bank{band}={expression};",
                      f"if (T{band}+Bank{band}!=0) "
                      f"{{ print(\"FAIL banked row {band}\"); exit(2); }}"]
        lines.append("print(\"BANKED_ROWS_MATCH\");")
        comparison_metadata = {
            "path": str(compare_record),
            "sha256": hashlib.sha256(raw).hexdigest(),
        }

    if charts != "none":
        top = ",".join(f"subst(T{k},b4,1)" for k in range(t, 2*t))
        positive = ",".join(f"subst(T{k},b4,0)" for k in range(1, 2*t))
        fullzero = ",".join(f"subst(T{k},b4,0)" for k in range(0, 2*t))
        lines += [f"ideal Rtop={top};", f"ideal Rpositive={positive};",
                  f"ideal Rfullzero={fullzero};"]
        lines += chart_ring_header(t, mode, prime, branch, residual)
        lines += ["ideal Itop=imap(R,Rtop);", "ideal Ipositive=imap(R,Rpositive);",
                  "ideal Ifullzero=imap(R,Rfullzero);"]
        if charts in ("top", "all"):
            lines += [f"ideal Gtop={basis('Itop')};",
                      "if (reduce(1,Gtop)==0) { print(\"TOP_TAIL_UNIT\"); }"
                      " else { print(\"TOP_TAIL_NONUNIT\"); }",
                      "print(\"TOP_BASIS_SIZE\"); size(Gtop);"]
        if charts in ("residual", "all"):
            lines += [f"ideal Gpositive={basis('Ipositive')};",
                      "print(\"POSITIVE_BASIS_SIZE\"); size(Gpositive);"]
            for variable in residual:
                token = variable.replace("_", "")
                lines += [f"int found{token}=0; int power{token};",
                          f"for (power{token}=1; power{token}<={2*t+4}; power{token}++)",
                          "{",
                          f"  if (reduce({variable}^power{token},Gpositive)==0)",
                          f"  {{ found{token}=power{token}; break; }}",
                          "}",
                          f"print(\"RADICAL_POWER variable={variable}\"); found{token};"]
            lines += [f"ideal Gfullzero={basis('Ifullzero')};",
                      "if (reduce(1,Gfullzero)==0) { print(\"B4ZERO_FULL_UNIT\"); }"
                      " else { print(\"B4ZERO_FULL_NONUNIT\"); }",
                      "print(\"FULLZERO_BASIS_SIZE\"); size(Gfullzero);"]
    lines += ["print(\"DRIVER_DONE\");", "quit;"]
    metadata: dict[str, object] = {
        "t": t,
        "mode": mode,
        "prime": prime,
        "branch": branch,
        "coefficient_algebra": coefficient_algebra,
        "terminal_sign": "T[k]=[X^k]E=-frozen_JSON_expr",
        "residual_variables": residual,
        "pivot_schedule": pivot_rows,
        "charts": charts,
        "algorithm": algorithm,
        "comparison_record": comparison_metadata,
        "dump_rows": dump_rows,
        "specialize_b4_before_expansion": specialize_b4,
    }
    return "\n".join(lines) + "\n", metadata


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int)
    parser.add_argument("--mode", choices=("exact", "split-exact", "mod"),
                        default="exact")
    parser.add_argument("--prime", type=int)
    parser.add_argument("--branch", type=int, choices=(0, 1))
    parser.add_argument("--charts", choices=("none", "top", "residual", "all"),
                        default="none")
    parser.add_argument("--algorithm", choices=("std", "slimgb", "modstd"), default="std")
    parser.add_argument("--compare-record", type=pathlib.Path)
    parser.add_argument("--dump-rows", action="store_true")
    parser.add_argument("--specialize-b4", type=int, choices=(0, 1))
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--timeout", type=int, default=3600)
    args = parser.parse_args()
    source, metadata = emit(args.t, args.mode, args.prime, args.branch,
                            args.charts, args.algorithm, args.compare_record,
                            args.dump_rows, args.specialize_b4)
    suffix = args.mode
    if args.prime is not None:
        suffix += f"_p{args.prime}"
    if args.branch is not None:
        suffix += f"_branch{args.branch}"
    if args.specialize_b4 is not None:
        suffix += f"_b4{args.specialize_b4}"
    stem = f"terminal_t{args.t}_{suffix}_{args.charts}"
    source_path = HERE / f"{stem}.sing"
    meta_path = HERE / f"{stem}.json"
    source_path.write_text(source, encoding="utf-8")
    if args.run:
        started = time.monotonic()
        try:
            result = subprocess.run(
                ["Singular", "-q", str(source_path)], capture_output=True,
                text=True, timeout=args.timeout, check=False,
            )
            has_error = "? error occurred" in result.stdout or "? error occurred" in result.stderr
            status = ("PASS" if result.returncode == 0 and "DRIVER_DONE" in result.stdout
                      and not has_error else "FAIL")
            metadata.update({
                "status": status,
                "returncode": result.returncode,
                "elapsed_seconds": time.monotonic() - started,
                "stdout": f"{stem}.out",
                "stderr": f"{stem}.err",
            })
            (HERE / f"{stem}.out").write_text(result.stdout, encoding="utf-8")
            (HERE / f"{stem}.err").write_text(result.stderr, encoding="utf-8")
        except subprocess.TimeoutExpired as exc:
            metadata.update({
                "status": "INCONCLUSIVE_TIMEOUT",
                "timeout_seconds": args.timeout,
                "elapsed_seconds": time.monotonic() - started,
            })
            stdout = exc.stdout or ""
            stderr = exc.stderr or ""
            if isinstance(stdout, bytes):
                stdout = stdout.decode("utf-8", errors="replace")
            if isinstance(stderr, bytes):
                stderr = stderr.decode("utf-8", errors="replace")
            (HERE / f"{stem}.out").write_text(stdout, encoding="utf-8")
            (HERE / f"{stem}.err").write_text(stderr, encoding="utf-8")
    meta_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n",
                         encoding="utf-8")
    print(json.dumps({"source": str(source_path), "metadata": str(meta_path),
                      "status": metadata.get("status", "EMITTED")}, sort_keys=True))


if __name__ == "__main__":
    main()
