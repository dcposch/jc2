#!/usr/bin/env python3
"""Emit (never run) a self-contained Singular job for the K=16 terminal cone.

The row construction is the proved Laurent/Euler recurrence used by the frozen
``singular_terminal_driver.py``.  The analysis ring deliberately has the order

    (b4,q2_0,...,q(t-1)_0,b3), wp(1,2,...,t-1,t+1).

Use an external foreground command such as
``timeout 1800 Singular -q JOB.sing >JOB.out 2>JOB.err`` to run the result.
This emitter itself never invokes Singular.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
from fractions import Fraction


OUTDIR = pathlib.Path(__file__).resolve().parent


def h_coefficients(t: int) -> tuple[int, int, int]:
    q = 2 * t + 1
    return 12 * q * q, -12 * q * (t + 1), (t + 1) * (3 * t + 2)


def h_value(t: int, y: int, p: int) -> int:
    a, b, c = h_coefficients(t)
    return (a * y * y + b * y + c) % p


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def modular_roots(t: int, p: int) -> list[int]:
    return [y for y in range(p) if h_value(t, y, p) == 0]


def split_roots(t: int) -> list[Fraction]:
    quotient, remainder = divmod(t + 1, 3)
    root = math.isqrt(quotient)
    if remainder or root * root != quotient:
        raise ValueError(f"t={t} is not a split index t=3*s^2-1")
    q = 2 * t + 1
    return sorted({Fraction(t + 1 - root, 2 * q),
                   Fraction(t + 1 + root, 2 * q)})


def is_split(t: int) -> bool:
    quotient, remainder = divmod(t + 1, 3)
    return remainder == 0 and math.isqrt(quotient) ** 2 == quotient


def inv(a: int, p: int) -> int:
    a %= p
    if a == 0:
        raise ZeroDivisionError("zero modular denominator")
    return pow(a, -1, p)


def divp(a: int, b: int, p: int) -> int:
    return a % p * inv(b, p) % p


def closed_pivot(t: int, j: int, y: int, p: int) -> int:
    """The proved high-spine diagonal p_j, reduced modulo p."""
    q, e = 2 * t + 1, 3 * t + 1
    d = (2 * q * y - (t + 1)) % p
    if j < t:
        aa = (9*j*j*t + 18*j*j - 54*j*t*t - 81*j*t - 26*j
              + 72*t**3 + 144*t*t + 88*t + 16)
        bb = (-9*j*j*t - 10*j*j + 24*j*t*t + 33*j*t + 10*j
              - 12*t**3 - 20*t*t - 8*t)
        return divp(3*t*e*(aa*d+bb),
                    (t+1)*(3*t+2)**3*(4*t-2*j+1), p)
    if j <= 2*t:
        aa = 12*t*t + 16*t + 4 - j*(3*t+4)
        bb = 2*(t+1)*(j-t)
        return divp(-3*t*e*(q-j)*(aa*d+bb),
                    (t+1)*q*(3*t+2)**2*(4*t-2*j+1), p)
    g = (divp(e*t*y, q*q, p) - divp(e*t*(t+1), 6*q**3, p)) % p
    return divp(g*d, 2*y, p)


def checked_modular_fibre(t: int, p: int, branch: int) -> tuple[int, dict[str, object]]:
    if not is_prime(p):
        raise ValueError(f"{p} is not prime")
    if p <= 8*t + 3:
        raise ValueError(f"properness integrality guard requires p > 8*t+3={8*t+3}")
    roots = modular_roots(t, p)
    if len(roots) != 2:
        raise ValueError(f"H_{t} has {len(roots)} distinct roots mod {p}: {roots}")
    y = roots[branch]
    q, e = 2*t+1, 3*t+1
    g = (divp(e*t*y, q*q, p) - divp(e*t*(t+1), 6*q**3, p)) % p
    pivots = [closed_pivot(t, j, y, p) for j in range(1, 2*t+2)]
    if y == 0 or g == 0 or y*g % p == 0 or any(v == 0 for v in pivots):
        raise ValueError("bad modular fibre: y, g, yg, or a high pivot vanishes")
    return y, {"roots": roots, "y": y, "g": g, "yg": y*g % p,
               "pivots": pivots, "p_gt_8t_plus_3": True}


def h_text(t: int, symbol: str = "yy") -> str:
    a, b, c = h_coefficients(t)
    return f"{a}*{symbol}^2{b:+d}*{symbol}{c:+d}"


def ring_header(name: str, variables: list[str], order: str, t: int,
                mode: str, p: int | None, y: int | Fraction | None) -> list[str]:
    if mode == "exact":
        return [f"ring {name}=(0,yy),({','.join(variables)}),{order};",
                f"minpoly={h_text(t)};"]
    if mode == "split-exact":
        assert isinstance(y, Fraction)
        return [f"ring {name}=0,({','.join(variables)}),{order};",
                f"number yy=({y.numerator}/{y.denominator});"]
    assert mode == "mod" and isinstance(p, int) and isinstance(y, int)
    return [f"ring {name}={p},({','.join(variables)}),{order};",
            f"number yy={y};"]


def ci_numerator(degrees: list[int]) -> list[int]:
    ans = [1]
    for degree in degrees:
        old = ans
        ans = old + [0] * degree
        for i, coefficient in enumerate(old):
            ans[i + degree] -= coefficient
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return ans


def parse_subset(spec: str, t: int) -> tuple[str, list[int]]:
    aliases = {
        "highest-t": list(range(1, t+1)),
        "tail-t": list(range(t, 2*t)),
        "highest-t+2": list(range(1, t+3)),
        "stated-t+2": list(range(t-2, 2*t)),
    }
    if spec in aliases:
        rows = aliases[spec]
    else:
        rows = [int(piece) for piece in spec.split(",") if piece]
    if not rows or len(set(rows)) != len(rows):
        raise ValueError("subset must be a nonempty list of distinct row indices")
    if min(rows) < 1 or max(rows) > 2*t-1:
        raise ValueError(f"subset rows must lie in 1..{2*t-1}")
    return spec, rows


def recurrence_lines(t: int, mode: str, p: int | None,
                     y: int | Fraction | None) -> tuple[list[str], list[str]]:
    q, e, top = 2*t+1, 3*t+1, 4*t+1
    cvars = [f"C{j}" for j in range(1, t)]
    qvars = [f"q{j}_0" for j in range(2, 2*t+1)]
    variables = ["h", "s", "b1", "b2", "b3", "b4", "B0"] + cvars + qvars
    lines = ["// Closed Laurent/Euler recurrence; T[k]=[X^k]E.",
             *ring_header("R", variables, "dp", t, mode, p, y),
             "option(noredSB);",
             "proc hcoef(poly f, int k)", "{",
             "  matrix M=coef(f,h); int ii;",
             "  for (ii=1; ii<=ncols(M); ii++)",
             "  { if (M[1,ii]==h^k) { return(M[2,ii]); } }",
             "  return(0);", "}",
             "proc eulerInverse(poly f)", "{",
             "  matrix M=coef(f,s); poly answer=0; int ii; int mm;",
             "  for (ii=1; ii<=ncols(M); ii++)",
             "  { mm=deg(M[1,ii]); answer=answer+M[2,ii]*M[1,ii]/((2*mm+1)*yy); }",
             "  return(answer);", "}",
             f"number g1={e}/{q};",
             f"number g2=({e}/{q})*yy+({e*t}/{2*q*q});",
             f"number g3=({e*t}/{q*q})*yy-({e*t*(t+1)}/{6*q**3});",
             "number cc=-yy*g3;"]
    uterms = [f"h^{q}"] + [f"q{j}_0*h^{q-j}" for j in range(2, 2*t+1)]
    cterms = [f"h^{t-1}"] + [f"C{j}*h^{t-1-j}" for j in range(1, t)]
    lines += ["poly Uh=" + "+".join(uterms) + ";",
              "poly Ch=" + "+".join(cterms) + ";",
              "poly U=subst(Uh,h,s+b4);", "poly Cp=subst(Ch,h,s+b4);",
              "poly A=s*Cp;",
              "poly Bprime=g3*(5*Cp+3*s*diff(Cp,s))/(2*yy);",
              "matrix MB=coef(Bprime,s); poly B=B0; int ii; int mm;",
              "for (ii=1; ii<=ncols(MB); ii++)",
              "{ mm=deg(MB[1,ii]); B=B+MB[2,ii]*s*MB[1,ii]/(mm+1); }",
              "if (diff(B,s)-Bprime!=0) { print(\"FAIL B derivative\"); exit(2); }",
              "poly rhsD=3*g3*diff(U,s)+A*B-s*A*diff(B,s)+2*s*diff(A,s)*B"
              "+g3*b3*(A/s+(5/2)*diff(A,s));",
              "poly D=eulerInverse(rhsD);",
              "if (yy*(D+2*s*diff(D,s))-rhsD!=0) { print(\"FAIL Euler inverse\"); exit(2); }",
              "poly Q1=s*A-yy*b3; poly Y=s*D-b3*B-g3*b2; poly Z=s*B-g3*b3;",
              "poly numD1=yy*g3*b1-Q1*diff(Y,s)+diff(Q1,s)*Y+2*diff(U,s)*Z;",
              "poly constantS=subst(numD1,s,0); poly pb1=diff(constantS,b1);",
              "poly b1rhs=-subst(constantS,b1,0)/pb1;",
              "numD1=subst(numD1,b1,b1rhs);",
              "if (subst(numD1,s,0)!=0) { print(\"FAIL b1 divisibility\"); exit(2); }",
              "poly Xprime=numD1/(2*yy*s);",
              f"poly gauge=hcoef(subst(Xprime,s,h-b4),{q-1});",
              "poly pB0=diff(gauge,B0); poly B0rhs=-subst(gauge,B0,0)/pB0;",
              "B=subst(B,B0,B0rhs); D=subst(D,B0,B0rhs);",
              "Y=subst(Y,B0,B0rhs); Z=subst(Z,B0,B0rhs);",
              "Xprime=subst(Xprime,B0,B0rhs); b1rhs=subst(b1rhs,B0,B0rhs);",
              "if (subst(gauge,B0,B0rhs)!=0) { print(\"FAIL B0 gauge\"); exit(2); }",
              "poly RR=Q1*Xprime-diff(U,s)*Y-yy*g3;",
              "poly Rh=subst(RR,s,h-b4);"]
    elimination = cvars + [f"q{j}_0" for j in range(t, 2*t+1)] + ["b2"]
    for weight, variable in enumerate(elimination, start=1):
        band = top-weight
        lines += [f"poly W{weight}=hcoef(Rh,{band});",
                  f"poly p{weight}=diff(W{weight},{variable});",
                  f"if (p{weight}==0) {{ ERROR(\"zero pivot {weight}\"); }}",
                  f"poly v{weight}rhs=-subst(W{weight},{variable},0)/p{weight};",
                  f"if (subst(W{weight},{variable},v{weight}rhs)!=0)"
                  f" {{ print(\"FAIL pivot {weight}\"); exit(2); }}",
                  f"Rh=subst(Rh,{variable},v{weight}rhs);"]
    for band in range(2*t, top+1):
        lines.append(f"if (hcoef(Rh,{band})!=0)"
                     f" {{ print(\"FAIL high band {band}\"); exit(2); }}")
    for band in range(2*t):
        lines.append(f"poly T{band}=-hcoef(Rh,{band});")
    lines.append("ideal RAW=" + ",".join(f"T{k}" for k in range(2*t)) + ";")
    return lines, variables


def analysis_lines(t: int, mode: str, p: int | None,
                   y: int | Fraction | None, task: str,
                   subset: tuple[str, list[int]] | None,
                   pure_bound: int) -> tuple[list[str], dict[str, object]]:
    residual = ["b4"] + [f"q{j}_0" for j in range(2, t)] + ["b3"]
    weights = [1] + list(range(2, t)) + [t+1]
    lines = [*ring_header("S", residual, f"wp({','.join(map(str, weights))})",
                          t, mode, p, y),
             "ideal TT=imap(R,RAW);",
             "setring R; ideal BACK=imap(S,TT); int jj;",
             "for (jj=1; jj<=size(RAW); jj++)",
             "{ if (BACK[jj]-RAW[jj]!=0)"
             " { print(\"FAIL residual ring map\"); exit(2); } }",
             "setring S; option(noredSB);",
             f"intvec WTS={','.join(map(str, weights))};",
             f'print("META t={t} vars={",".join(residual)} weights={",".join(map(str,weights))}");']
    for k in range(1, 2*t):
        degree = 4*t+1-k
        lines += [f"if (homog(TT[{k+1}])!=1)"
                  f" {{ print(\"FAIL inhomogeneous T{k}\"); exit(2); }}",
                  f"if (deg(TT[{k+1}])!={degree})"
                  f" {{ print(\"FAIL degree T{k}\"); exit(2); }}"]
    if task == "rows":
        lines += [f'print("ROWS_PASS t={t} count={2*t}");', "quit;"]
        return lines, {"analysis_rows": None}
    if task == "full":
        label = "FULL"
        selected = list(range(1, 2*t))
    else:
        assert subset is not None
        label = "SUBSET_" + subset[0].replace("+", "PLUS").replace("-", "_").upper()
        selected = subset[1]
    lines += ["ideal J=" + ",".join(f"TT[{k+1}]" for k in selected) + ";",
              f'print("{label}_ROWS={",".join(map(str,selected))}");',
              "int tm=timer; ideal G=std(J);",
              f'print("{label}_STD_SECONDS="+string(timer-tm));',
              f'print("{label}_GB_SIZE="+string(size(G)));',
              f'print("{label}_DIM="+string(dim(G)));',
              f'print("{label}_HILB_NUMERATOR_BEGIN");',
              "intvec HNUM=hilb(G,1,WTS); HNUM;",
              f'print("{label}_HILB_NUMERATOR_END");',
              f'print("{label}_HILB_REDUCED_BEGIN");',
              "intvec HRED=hilb(G,2,WTS); HRED;",
              f'print("{label}_HILB_REDUCED_END");',
              f'if (dim(G)==0) {{ print("{label}_LENGTH="+string(vdim(G))); }}',
              "ideal LM=minbase(lead(G)); ideal GLM=std(LM);",
              f'print("{label}_INITIAL_MIN_GENS_BEGIN"); LM;',
              "for (jj=1; jj<=size(LM); jj++)",
              f'{{ print("{label}_INITIAL_EXP_"+string(jj)+"="'
              '+string(leadexp(LM[jj]))); }',
              f'print("{label}_INITIAL_MIN_GENS_END");']
    for variable in residual:
        token = variable.replace("_", "")
        lines += [f"int found{token}=0; int pow{token};",
                  f"for (pow{token}=1; pow{token}<={pure_bound}; pow{token}++)",
                  f"{{ if (reduce({variable}^pow{token},GLM)==0)"
                  f" {{ found{token}=pow{token}; break; }} }}",
                  f'print("{label}_PURE_POWER {variable}="+string(found{token}));']
    ci = None
    degrees = [4*t+1-k for k in selected]
    if task == "subset":
        ci = ci_numerator(degrees)
        lines += ["intvec CINU=" + ",".join(map(str, ci)) + ";",
                  f'print("{label}_CI_NUMERATOR_BEGIN"); CINU;',
                  f'print("{label}_CI_NUMERATOR_END");',
                  f'if (HNUM==CINU) {{ print("{label}_CI_HILB_EQUAL=1"); }}'
                  f' else {{ print("{label}_CI_HILB_EQUAL=0"); }}']
    lines += [f'print("JOB_DONE t={t} label={label}");', "quit;"]
    return lines, {"analysis_rows": selected, "row_degrees": degrees,
                   "ci_numerator": ci, "label": label,
                   "regular_sequence_length_possible": len(selected) <= t,
                   "selected_row_count": len(selected)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int)
    ap.add_argument("--mode", choices=("exact", "split-exact", "mod"), default="mod")
    ap.add_argument("--prime", type=int, default=1009)
    ap.add_argument("--branch", type=int, choices=(0, 1), default=0)
    ap.add_argument("--task", choices=("rows", "full", "subset"), default="full")
    ap.add_argument("--subset", default="highest-t",
                    help="highest-t, tail-t, highest-t+2, stated-t+2, or CSV indices")
    ap.add_argument("--pure-bound", type=int, default=128)
    ap.add_argument("--out", type=pathlib.Path)
    args = ap.parse_args()
    t = args.t
    if t < 2:
        raise SystemExit("t must be at least 2")
    modular_audit = None
    p: int | None = None
    y: int | Fraction | None = None
    if args.mode == "mod":
        p = args.prime
        y, modular_audit = checked_modular_fibre(t, p, args.branch)
    elif args.mode == "split-exact":
        y = split_roots(t)[args.branch]
    elif is_split(t):
        raise SystemExit("exact algebraic mode is invalid at a split t; use split-exact per factor")
    subset = parse_subset(args.subset, t) if args.task == "subset" else None
    recurrence, source_variables = recurrence_lines(t, args.mode, p, y)
    analysis, analysis_meta = analysis_lines(t, args.mode, p, y, args.task,
                                              subset, args.pure_bound)
    source = "\n".join(recurrence + analysis) + "\n"
    fibre = (f"p{p}_b{args.branch}_y{y}" if args.mode == "mod"
             else f"b{args.branch}_y{str(y).replace('/', '_')}"
             if args.mode == "split-exact" else "numberfield")
    subset_tag = ("_" + args.subset.replace(",", "_").replace("+", "plus")
                  if args.task == "subset" else "")
    out = args.out or OUTDIR / f"t{t}_{args.mode}_{fibre}_{args.task}{subset_tag}.sing"
    if out.suffix != ".sing":
        raise SystemExit("--out must end in .sing")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(source, encoding="utf-8")
    metadata = {
        "t": t, "mode": args.mode, "prime": p, "branch": args.branch, "y": str(y),
        "task": args.task, "subset": args.subset if subset else None,
        "source_ring_variables": source_variables,
        "analysis_ring_variables": ["b4"] + [f"q{j}_0" for j in range(2,t)] + ["b3"],
        "analysis_weights": [1] + list(range(2,t)) + [t+1],
        "row_weight_formula": "deg_wp(T[t,k])=4*t+1-k for k>=1",
        "ring_dimension": t,
        "modular_integrality_audit": modular_audit,
        "singular_source": str(out),
        "singular_source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "run_command": f"timeout 1800 Singular -q {out} > {out.with_suffix('.out')} 2> {out.with_suffix('.err')}",
        "derived_from_sha256": {
            "singular_terminal_driver.py": "0cc821ff59adc955d2c6c33a572766b01569d578f1034f343c4f3661cebcf8ed",
            "terminal_array_recurrence.py": "8a935838ac01731110efd5f36652cae3d66bd00ffa23ae4450cdadaa41438001",
        },
        **analysis_meta,
    }
    meta = out.with_suffix(".json")
    meta.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"source": str(out), "metadata": str(meta),
                      "sha256": metadata["singular_source_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
