#!/usr/bin/env python3
"""Emit bounded Singular jobs for the t=8 K16 cone probes.

Rows are read from a Fable terminal row file already reduced modulo 32003 at a
declared root of H_8.  The emitted jobs are intentionally small wrappers around
the charged row data:

  b4one : z-type chart <T_1..T_15, T0hom, b4-1>
  b4zero: homogeneous z-slice <T_1..T_15|b4=0, T0hom|b4=0, b4>
  resz  : residual-zero slice <T_1..T_15, b4>
  topt  : top-tail cone <T_8..T_15>

The Singular side writes progress to the requested log before running std().
"""
import re
import sys


def main() -> None:
    if len(sys.argv) < 4:
        raise SystemExit("usage: probe_t8.py MODE ROWS LOG [TIMEOUT_LABEL]")
    t = 8
    mode, rows_path, log = sys.argv[1:4]
    timeout_label = sys.argv[4] if len(sys.argv) > 4 else "0"
    rows = {}
    with open(rows_path) as handle:
        for line in handle:
            match = re.match(r"T(\d+) = (.*);$", line.strip())
            if match:
                rows[int(match.group(1))] = match.group(2)
    if sorted(rows) != list(range(2 * t)):
        raise SystemExit("row file must contain T0..T15")

    vars_ = "b3,b4" + "".join(f",q({j})" for j in range(2, t))
    weights = [t + 1, 1] + list(range(2, t))
    wstr = ",".join(map(str, weights))

    lines = [
        f"ring R=32003,({vars_}),wp({wstr});",
        f"intvec W={wstr};",
        "option(redSB);",
    ]
    for k in range(2 * t):
        lines.append(f"poly T{k} = {rows[k]};")
    zero_subs = "".join(f", q({j}),0" for j in range(2, t))
    lines.append(f"poly T0hom = T0 - subst(T0, b3,0, b4,0{zero_subs});")
    lines.append(f'write(":a {log}", "T0CONST=" + string(T0 - T0hom));')
    for k in range(1, 2 * t):
        lines.append(
            f'write(":a {log}", "ROW k={k} terms=" + string(size(T{k})) '
            f'+ " wdeg=" + string(deg(T{k}, W)) '
            f'+ " b4zero_terms=" + string(size(subst(T{k}, b4, 0))));'
        )
    lines.append(
        f'write(":a {log}", "ROW k=0hom terms=" + string(size(T0hom)) '
        f'+ " wdeg=" + string(deg(T0hom, W)) '
        f'+ " b4zero_terms=" + string(size(subst(T0hom, b4, 0))));'
    )

    if mode == "b4one":
        generators = ",".join(f"subst(T{k}, b4, 1)" for k in range(1, 2 * t))
        lines.append(f"ideal J = {generators}, subst(T0hom, b4, 1), b4-1;")
        lines.append(
            f'write(":a {log}", "ZCHART_B4ONE t=8 generators=" '
            f'+ string(size(J)) + " timeout={timeout_label}");'
        )
        lines.append(
            f'int tt = timer; ideal G = std(J); '
            f'if (reduce(1, G) == 0) {{ '
            f'write(":a {log}", "ZCHART_B4ONE t=8 UNIT time=" + string(timer-tt)); '
            f'}} else {{ '
            f'write(":a {log}", "ZCHART_B4ONE t=8 NONUNIT dim=" + string(dim(G)) '
            f'+ " vdim=" + string(vdim(G)) + " size=" + string(size(G)) '
            f'+ " time=" + string(timer-tt)); '
            f'write(":a {log}", "ZCHART_B4ONE_LEAD=" + string(lead(G))); '
            f'}}'
        )
    elif mode == "b4zero":
        generators = ",".join(f"subst(T{k}, b4, 0)" for k in range(1, 2 * t))
        lines.append(f"ideal J = {generators}, subst(T0hom, b4, 0), b4;")
        lines.append(
            f'write(":a {log}", "ZSLICE_B4ZERO t=8 generators=" '
            f'+ string(size(J)) + " timeout={timeout_label}");'
        )
        lines.append(
            f'int tt = timer; ideal G = std(J); '
            f'write(":a {log}", "ZSYS_B4ZERO t=8 dim=" + string(dim(G)) '
            f'+ " size=" + string(size(G)) + " time=" + string(timer-tt));'
        )
    elif mode == "resz":
        generators = ",".join(f"T{k}" for k in range(1, 2 * t))
        lines.append(f"ideal J = {generators}, b4;")
        lines.append(
            f'write(":a {log}", "RESZ t=8 generators=" + string(size(J)) '
            f'+ " timeout={timeout_label}");'
        )
        lines.append(
            f'int tt = timer; ideal G = std(J); '
            f'write(":a {log}", "RESZ t=8 dim=" + string(dim(G)) '
            f'+ " size=" + string(size(G)) + " time=" + string(timer-tt));'
        )
    elif mode == "topt":
        generators = ",".join(f"T{k}" for k in range(t, 2 * t))
        lines.append(f"ideal J = {generators};")
        lines.append(
            f'write(":a {log}", "TOPT t=8 generators=" + string(size(J)) '
            f'+ " timeout={timeout_label}");'
        )
        lines.append(
            f'int tt = timer; ideal G = std(J); '
            f'write(":a {log}", "TOPT t=8 dim=" + string(dim(G)) '
            f'+ " size=" + string(size(G)) + " time=" + string(timer-tt)); '
            f'write(":a {log}", "TOPT_LEAD=" + string(lead(G)));'
        )
    else:
        raise SystemExit(f"unknown mode: {mode}")

    lines.append("quit;")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
