#!/usr/bin/env python3
"""Emit a b4=1, tau-free Laurent recurrence and its TOP-TAIL test.

This is the fixed-t executable form of the indexed recurrence used in the
charged middle-spine report.  It specializes b4=1 before expansion, works in
the L=X-1 basis through all high affine solves, and omits the integration
constant B0: changing B0 adds U'/y to P' and the corresponding change in Y,
which cancels identically in V*P'-U'*Y.  These three choices make larger
fixed-t controls substantially cheaper without changing a terminal row.
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


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def h_poly(t: int, y: sp.Symbol) -> sp.Expr:
    q = 2*t+1
    return sp.expand(12*q*q*y*y-12*q*(t+1)*y+(t+1)*(3*t+2))


def mod_roots(t: int, prime: int) -> list[int]:
    y = sp.Symbol("y")
    poly = sp.Poly(h_poly(t, y), y, modulus=prime)
    roots = [a for a in range(prime) if int(poly.eval(a)) % prime == 0]
    roots = sorted(set(roots))
    if len(roots) != 2:
        raise ValueError(f"H_{t} has {len(roots)} roots modulo {prime}")
    return roots


def split_y_roots(t: int) -> list[sp.Rational]:
    quotient, remainder = divmod(t+1, 3)
    s = math.isqrt(quotient)
    if remainder or s*s != quotient:
        raise ValueError(f"t={t} is not a split index")
    q = 2*t+1
    return [sp.Rational(t+1-s, 2*q), sp.Rational(t+1+s, 2*q)]


def singular_fraction(x: sp.Rational) -> str:
    return f"({int(x.p)}/{int(x.q)})"


def pivot_formula(t: int, weight: int) -> sp.Expr:
    q, e = 2*t+1, 3*t+1
    d = sp.Symbol("d")
    j = weight
    if 1 <= j < t:
        ac = (9*j*j*t+18*j*j-54*j*t*t-81*j*t-26*j
              +72*t**3+144*t*t+88*t+16)
        bc = (-9*j*j*t-10*j*j+24*j*t*t+33*j*t+10*j
              -12*t**3-20*t*t-8*t)
        return sp.Rational(3*t*e, (t+1)*(3*t+2)**3*(4*t-2*j+1))*(ac*d+bc)
    if t <= j <= 2*t:
        aq = 12*t*t+16*t+4-j*(3*t+4)
        bq = 2*(t+1)*(j-t)
        return -sp.Rational(3*t*e*(q-j), (t+1)*q*(3*t+2)**2*(4*t-2*j+1))*(aq*d+bq)
    if j == 2*t+1:
        return sp.Rational(t*e, 6*q*q*(3*t+2))*(3*q*d+t+1)
    raise ValueError(weight)


def emit(t: int, mode: str, prime: int | None, branch: int | None,
         chart: str, compare: pathlib.Path | None,
         audit_subsystems: bool, algorithm: str,
         var_order: str) -> tuple[str, dict]:
    if t < 2:
        raise ValueError("stable recurrence begins at t=2")
    q, e, nweight = 2*t+1, 3*t+1, 4*t+1
    cvars = [f"C{j}" for j in range(1, t)]
    uvars = [f"q{j}_0" for j in range(2, 2*t+1)]
    residual = ["b3", *[f"q{j}_0" for j in range(2, t)]]
    chart_residual = list(reversed(residual)) if var_order == "reverse" else residual
    variables = ["L", "b2", "b3", *cvars, *uvars]

    if mode == "exact":
        if not sp.Poly(3*sp.Symbol("d")**2-(t+1), sp.Symbol("d")).is_irreducible:
            raise ValueError("exact mode is only for nonsplit A_t")
        # The integral associate a=3d keeps the minpoly integral and makes
        # modular rational reconstruction markedly cheaper.
        header = [f"ring R=(0,a),({','.join(variables)}),dp;",
                  f"minpoly=a2-{3*(t+1)};", "number d=a/3;",
                  f"number yy=(d+{t+1})/{2*q};"]
        coefficient_algebra = f"Q[a]/(a^2-{3*(t+1)}), d=a/3"
    elif mode == "split-exact":
        if branch not in (0, 1):
            raise ValueError("split-exact needs --branch 0 or 1")
        yy = split_y_roots(t)[branch]
        header = [f"ring R=0,({','.join(variables)}),dp;",
                  f"number yy={singular_fraction(yy)};",
                  f"number d=2*{q}*yy-{t+1};"]
        coefficient_algebra = f"Q, y={yy}"
    elif mode == "mod":
        if prime is None or branch not in (0, 1):
            raise ValueError("mod mode needs --prime and --branch")
        yy = mod_roots(t, prime)[branch]
        header = [f"ring R={prime},({','.join(variables)}),dp;",
                  f"number yy={yy};", f"number d=2*{q}*yy-{t+1};"]
        coefficient_algebra = f"F_{prime}, y={yy}"
    else:
        raise ValueError(mode)

    lines = [
        "// b4=1 tau-free Laurent/Euler recurrence; RR=-E",
        f"// t={t} mode={mode} branch={branch}",
        *header,
        "option(noredSB);",
        "proc Lcoef(poly f, int k)",
        "{",
        "  matrix M=coef(f,L); int ii;",
        "  for (ii=1; ii<=ncols(M); ii++)",
        "  { if (M[1,ii]==L^k) { return(M[2,ii]); } }",
        "  return(0);",
        "}",
        "proc eulerInverse(poly f)",
        "{",
        "  matrix M=coef(f,L); poly a=0; int ii; int mm;",
        "  for (ii=1; ii<=ncols(M); ii++)",
        "  { mm=deg(M[1,ii]); a=a+M[2,ii]*M[1,ii]/((2*mm+1)*yy); }",
        "  return(a);",
        "}",
        f"number g3=({e*t}/{q*q})*yy-({e*t*(t+1)}/{6*q**3});",
        "if (3*d^2-"+str(t+1)+"!=0) { print(\"FAIL d relation\"); quit; }",
    ]
    u_terms = [f"(L+1)^{q}"] + [f"q{j}_0*(L+1)^{q-j}" for j in range(2, 2*t+1)]
    c_terms = [f"(L+1)^{t-1}"] + [f"C{j}*(L+1)^{t-1-j}" for j in range(1, t)]
    lines += [
        "poly U="+"+".join(u_terms)+";",
        "poly C="+"+".join(c_terms)+";",
        "poly A=L*C;",
        "poly Bprime=g3*(5*C+3*L*diff(C,L))/(2*yy);",
        "matrix MB=coef(Bprime,L); poly B=0; int ii; int mm;",
        "for (ii=1; ii<=ncols(MB); ii++)",
        "{ mm=deg(MB[1,ii]); B=B+MB[2,ii]*L*MB[1,ii]/(mm+1); }",
        "if (diff(B,L)-Bprime!=0) { print(\"FAIL B recurrence\"); quit; }",
        "poly rhsS=3*g3*diff(U,L)+A*B-L*A*diff(B,L)+2*L*diff(A,L)*B",
        "          +g3*b3*(C+(5/2)*diff(A,L));",
        "poly S=eulerInverse(rhsS);",
        "if (yy*(S+2*L*diff(S,L))-rhsS!=0) { print(\"FAIL S recurrence\"); quit; }",
        "poly V=L*A-yy*b3;",
        "poly Y=L*S-b3*B-g3*b2;",
        "poly Z=L*B-g3*b3;",
        "poly NN=-V*diff(Y,L)+diff(V,L)*Y+2*diff(U,L)*Z;",
        "poly N0=subst(NN,L,0);",
        "poly Pprime=(NN-N0)/(2*yy*L);",
        "if (2*yy*L*Pprime-NN+N0!=0) { print(\"FAIL Pprime division\"); quit; }",
        "poly RR=V*Pprime-diff(U,L)*Y-yy*g3;",
    ]

    elimination = cvars + [f"q{j}_0" for j in range(t, 2*t+1)] + ["b2"]
    pivots: list[dict] = []
    for weight, variable in enumerate(elimination, 1):
        band = nweight-weight
        expected = str(pivot_formula(t, weight)).replace("**", "^")
        lines += [
            f"poly W{weight}=Lcoef(RR,{band});",
            f"poly p{weight}=diff(W{weight},{variable});",
            f"poly ep{weight}={expected};",
            f"if (p{weight}-ep{weight}!=0) {{ print(\"FAIL pivot coefficient {weight}\"); quit; }}",
            f"if (p{weight}==0) {{ print(\"FAIL zero pivot {weight}\"); quit; }}",
            f"poly v{weight}rhs=-subst(W{weight},{variable},0)/p{weight};",
            f"if (subst(W{weight},{variable},v{weight}rhs)!=0) {{ print(\"FAIL pivot {weight}\"); quit; }}",
            f"RR=subst(RR,{variable},v{weight}rhs);",
        ]
        pivots.append({"weight": weight, "band": band, "variable": variable,
                       "coefficient": expected})

    for band in range(2*t, nweight):
        lines.append(f"if (Lcoef(RR,{band})!=0) {{ print(\"FAIL high L band {band}\"); quit; }}")
    lines += ["poly Rh=subst(RR,L,L-1);"]
    for band in range(t, 2*t):
        lines += [f"poly T{band}=Lcoef(Rh,{band});",
                  f"print(\"TOP_ROW band={band}\"); deg(T{band}); size(T{band});"]
    lines.append(f"print(\"RECURRENCE_PASS t={t}\");")

    comparison_meta = None
    if compare is not None:
        record = json.loads(compare.read_text(encoding="utf-8"))
        if int(record["t"]) != t:
            raise ValueError("comparison record t mismatch")
        terminal = {int(x["band"]): x["expr"] for x in record["terminal"]}
        for band in range(t, 2*t):
            expr = terminal[band]
            expr = expr.replace(f"q{q}_1", "yy")
            expr = re.sub(r"\bb4\b", "(1)", expr)
            expr = re.sub(r"/(\d+)", r"*(1/\1)", expr).replace("**", "^")
            lines += [f"poly Bank{band}={expr};",
                      f"if (T{band}-Bank{band}!=0) {{ print(\"FAIL banked top row {band}\"); quit; }}"]
        lines.append("print(\"BANKED_TOP_ROWS_MATCH\");")
        comparison_meta = {"path": str(compare), "sha256": sha256(compare)}

    if chart == "top":
        lines += ["ideal Itop="+",".join(f"T{k}" for k in range(t, 2*t))+";"]
        # Move only the residual variables into the chart ring.
        if mode == "exact":
            lines += [f"ring CR=(0,a),({','.join(chart_residual)}),dp;",
                      f"minpoly=a2-{3*(t+1)};"]
        elif mode == "split-exact":
            lines += [f"ring CR=0,({','.join(chart_residual)}),dp;"]
        else:
            lines += [f"ring CR={prime},({','.join(chart_residual)}),dp;"]
        lines += ["ideal I=imap(R,Itop);", "option(redSB);"]
        if audit_subsystems:
            for direction, indices in (
                ("ASC", list(range(1, t+1))),
                ("DESC", list(range(t, 0, -1))),
            ):
                accumulated: list[str] = []
                for step, index in enumerate(indices, 1):
                    accumulated.append(f"I[{index}]")
                    name = f"G{direction}{step}"
                    ideal_name = f"J{direction}{step}"
                    lines += [
                        f"ideal {ideal_name}={','.join(accumulated)};",
                        f"ideal {name}=std({ideal_name});",
                        f"print(\"AUDIT {direction} step={step} band={t+index-1}\");",
                        f"size({name}); dim({name}); vdim({name});",
                    ]
            if mode != "exact":
                for omitted in range(1, t+1):
                    generators = [f"I[{j}]" for j in range(1, t+1) if j != omitted]
                    name = f"GO{omitted}"
                    ideal_name = f"JO{omitted}"
                    lines += [
                        f"ideal {ideal_name}={','.join(generators)};",
                        f"ideal {name}=std({ideal_name});",
                        f"poly NF{omitted}=reduce(I[{omitted}],{name});",
                        f"print(\"AUDIT OMIT band={t+omitted-1}\");",
                        f"size({name}); dim({name}); vdim({name}); size(NF{omitted}); deg(NF{omitted});",
                    ]
        if mode == "exact":
            lines += ['LIB "modstd.lib";', "ideal G=modStd(I,1);"]
        else:
            lines += [f"ideal G={algorithm}(I);"]
        lines += ["if (reduce(1,G)==0) { print(\"TOP_TAIL_UNIT\"); }"
                  " else { print(\"TOP_TAIL_NONUNIT\"); }",
                  "print(\"TOP_BASIS_SIZE\"); size(G);"]
    lines += ["print(\"DRIVER_DONE\");", "quit;", ""]
    return "\n".join(lines), {
        "t": t, "mode": mode, "prime": prime, "branch": branch,
        "coefficient_algebra": coefficient_algebra,
        "chart": chart, "comparison": comparison_meta,
        "algorithm": algorithm,
        "var_order": var_order,
        "audit_subsystems": audit_subsystems,
        "pivot_schedule": pivots, "residual_variables": residual,
        "standard_basis_reduction": "noredSB; unit verdict reduces to [1]",
        "typing": "fixed-t execution of indexed b4=1 tau-free recurrence",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int)
    parser.add_argument("--mode", choices=("exact", "split-exact", "mod"), default="exact")
    parser.add_argument("--prime", type=int)
    parser.add_argument("--branch", type=int, choices=(0, 1))
    parser.add_argument("--chart", choices=("none", "top"), default="top")
    parser.add_argument("--algorithm", choices=("std", "slimgb", "groebner"), default="std")
    parser.add_argument("--var-order", choices=("normal", "reverse"), default="normal")
    parser.add_argument("--compare", type=pathlib.Path)
    parser.add_argument("--audit-subsystems", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--stem")
    args = parser.parse_args()
    source, metadata = emit(args.t, args.mode, args.prime, args.branch,
                            args.chart, args.compare, args.audit_subsystems,
                            args.algorithm, args.var_order)
    stem = args.stem or f"top_tail_fast_t{args.t}_{args.mode}_b{args.branch}_{args.chart}"
    source_path = HERE/f"{stem}.sing"
    metadata_path = HERE/f"{stem}.json"
    source_path.write_text(source, encoding="utf-8")
    metadata.update({
        "emitter": str(pathlib.Path(__file__).resolve()),
        "emitter_sha256": sha256(pathlib.Path(__file__).resolve()),
        "singular_source": str(source_path),
        "singular_source_sha256": sha256(source_path),
    })
    if args.run:
        started = time.monotonic()
        try:
            result = subprocess.run(["Singular", "--cpus=4", "--threads=4",
                                     "--flint-threads=4", "-q", str(source_path)],
                                    capture_output=True, timeout=args.timeout)
            out, err = result.stdout, result.stderr
            status = ("PROVED_UNIT" if result.returncode == 0 and b"FAIL" not in out
                      and b"TOP_TAIL_UNIT" in out and b"DRIVER_DONE" in out
                      else "PASS_RECURRENCE" if result.returncode == 0
                      and b"FAIL" not in out and b"DRIVER_DONE" in out else "FAIL")
            code = result.returncode
        except subprocess.TimeoutExpired as exc:
            out, err = exc.stdout or b"", exc.stderr or b""
            status, code = "INCONCLUSIVE_TIMEOUT", 124
        out_path, err_path = source_path.with_suffix(".out"), source_path.with_suffix(".err")
        out_path.write_bytes(out); err_path.write_bytes(err)
        metadata["run"] = {
            "elapsed_seconds": time.monotonic()-started, "exit": code,
            "status": status, "timeout_seconds": args.timeout,
            "out": str(out_path), "out_sha256": sha256(out_path),
            "err": str(err_path), "err_sha256": sha256(err_path),
        }
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True)+"\n",
                             encoding="utf-8")
    print(json.dumps(metadata, sort_keys=True))


if __name__ == "__main__":
    main()
