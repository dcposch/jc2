#!/usr/bin/env python3
"""Emit a self-contained Singular runtime builder for the BNF bridge chart."""

from __future__ import annotations

import argparse
import hashlib
import pathlib


ROOT = pathlib.Path("/home/ubuntu/jc2")
HERE = ROOT / "box/bridgegate-20260903"


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def basis_names(t: int, j: int) -> list[str]:
    if j <= t:
        return ["1"]
    if j <= 2 * t:
        return ["1", "A"]
    if j <= 3 * t:
        return ["1", "A", "B"]
    return ["1", "g", "A", "B", "z"]


def bridge_variables(t: int) -> tuple[list[str], list[int], list[int]]:
    e, q = 3 * t + 1, 2 * t + 1
    variables = ["b1", "b2", "b3", "b4"]
    for j in range(2, q + 1):
        for name in basis_names(t, j):
            variables.append(f"q{j}_{name}")
    zero_a = [t, e - 1, e]
    free_a = []
    for k in range(1, e + 1):
        if k not in zero_a:
            variables.append(f"a{k}")
            free_a.append(k)
    return variables, free_a, zero_a


def emit(t: int, characteristic: int, method: str, output: pathlib.Path, build_only: bool = False) -> None:
    if method not in {"std", "slimgb"}:
        raise ValueError(method)
    e, q = 3 * t + 1, 2 * t + 1
    variables, free_a, zero_a = bridge_variables(t)
    build_vars = ["p", "g"] + variables + ["c", "Tr"]
    final_vars = variables + ["c", "Tr"]
    lo = -(e + 3)
    hi = e + q + 10
    offset = -lo + 5

    def coeff_for_beta(j: int) -> str:
        terms = []
        for name in basis_names(t, j):
            basis = {"1": "1", "A": "A", "B": "B", "g": "g", "z": "z"}[name]
            terms.append(f"q{j}_{name}*({basis})")
        return "+".join(terms) if terms else "0"

    lines: list[str] = [
        f"// runtime BNF bridge builder, t={t}, char={characteristic}, method={method}",
        f"// e={e} q={q}; unknowns including c={len(variables)+1}; zero_a={','.join(map(str, zero_a))}; free_a={','.join(map(str, free_a))}",
        'LIB "resources.lib";',
        "setcores(4);",
        f"ring RB={characteristic},({','.join(build_vars)}),lp;",
        "option(redSB);",
        "poly z=p-g;",
        "poly B=p*z+b1*p+b2;",
        "poly A=p*B+b3;",
        "poly h=p*A+b4;",
        "ideal H=h;",
        "ideal Hstd=std(H);",
        f"int LO={lo};",
        f"int HI={hi};",
        f"int OFFSET={offset};",
        "proc getAt(list S, int power)",
        "{",
        "  int idx=power+OFFSET;",
        "  if (idx<1) { return(0); }",
        "  if (typeof(S[idx])==\"none\") { return(0); }",
        "  return(S[idx]);",
        "}",
        "proc addAt(list S, int power, poly value)",
        "{",
        "  if (value==0) { return(S); }",
        "  int idx=power+OFFSET;",
        "  if (typeof(S[idx])==\"none\") { S[idx]=value; } else { S[idx]=S[idx]+value; }",
        "  return(S);",
        "}",
        "proc hred(poly f)",
        "{",
        "  list S;",
        "  int power=0;",
        "  poly cur=f;",
        "  list D;",
        "  poly quo;",
        "  poly rem;",
        "  while (cur!=0)",
        "  {",
        "    D=division(cur,Hstd);",
        "    quo=D[1][1,1];",
        "    rem=D[2][1];",
        "    if (rem!=0) { S=addAt(S,power,rem); }",
        "    if (quo==0) { return(S); }",
        "    cur=quo;",
        "    power++;",
        "  }",
        "  return(S);",
        "}",
        "proc hadd(list A0, list B0)",
        "{",
        "  list R=A0;",
        "  int i;",
        "  poly v;",
        "  for (i=LO; i<=HI; i++)",
        "  {",
        "    v=getAt(B0,i);",
        "    if (v!=0) { R=addAt(R,i,v); }",
        "  }",
        "  return(R);",
        "}",
        "proc hshift(list A0, int delta)",
        "{",
        "  list R;",
        "  int i;",
        "  poly v;",
        "  for (i=LO; i<=HI; i++)",
        "  {",
        "    v=getAt(A0,i);",
        "    if (v!=0) { R=addAt(R,i+delta,v); }",
        "  }",
        "  return(R);",
        "}",
        "proc hscal(list A0, poly scalar)",
        "{",
        "  list R;",
        "  int i;",
        "  poly v;",
        "  for (i=LO; i<=HI; i++)",
        "  {",
        "    v=getAt(A0,i);",
        "    if (v!=0) { R=addAt(R,i,scalar*v); }",
        "  }",
        "  return(R);",
        "}",
        "proc hmul(list A0, list B0)",
        "{",
        "  list R;",
        "  int i; int j; int d;",
        "  poly ai; poly bj; poly rd;",
        "  list Red;",
        "  for (i=LO; i<=HI; i++)",
        "  {",
        "    ai=getAt(A0,i);",
        "    if (ai!=0)",
        "    {",
        "      for (j=LO; j<=HI; j++)",
        "      {",
        "        bj=getAt(B0,j);",
        "        if ((bj!=0) && (i+j>=LO-1) && (i+j<=HI))",
        "        {",
        "          Red=hred(ai*bj);",
        "          for (d=0; d<=8; d++)",
        "          {",
        "            rd=getAt(Red,d);",
        "            if ((rd!=0) && (i+j+d>=LO) && (i+j+d<=HI)) { R=addAt(R,i+j+d,rd); }",
        "          }",
        "        }",
        "      }",
        "    }",
        "  }",
        "  return(R);",
        "}",
        "proc hpowUnit(list U, number exponent)",
        "{",
        "  list Res; list Term;",
        "  Res=addAt(Res,0,1);",
        "  Term=addAt(Term,0,1);",
        "  number coeffN=1;",
        "  int j;",
        f"  for (j=1; j<={-2 * lo + 4}; j++)",
        "  {",
        "    Term=hmul(Term,U);",
        "    if (size(Term)==0) { return(Res); }",
        "    coeffN=coeffN*(exponent-(j-1))/j;",
        "    Res=hadd(Res,hscal(Term,coeffN));",
        "  }",
        "  return(Res);",
        "}",
        "proc J(poly f, poly gg)",
        "{",
        "  return(diff(f,g)*diff(gg,p)-diff(f,p)*diff(gg,g));",
        "}",
        "list U;",
    ]
    for j in range(2, q + 1):
        lines.append(f"U=addAt(U,-{j},({coeff_for_beta(j)}));")
    lines.extend([
        "list Pser;",
        "list Tk;",
    ])
    for k in range(0, e + 1):
        if k == 0:
            ak = "1"
        elif k in zero_a:
            ak = "0"
        else:
            ak = f"a{k}"
        if ak == "0":
            continue
        lines.extend([
            f"// BNF summand k={k}",
            f"Tk=hpowUnit(U,number({e-k})/number({q}));",
            f"Tk=hshift(Tk,{e-k});",
            f"Tk=hscal(Tk,{ak});",
            "Pser=hadd(Pser,Tk);",
        ])
    lines.extend([
        "list Qser;",
        f"Qser=addAt(Qser,{q},1);",
        f"Qser=hadd(Qser,hshift(U,{q}));",
        "list By;",
        "int rp; int spow; poly aa; poly bb; poly first; poly second;",
        f"for (rp=0; rp<={q}; rp++)",
        "{",
        "  aa=getAt(Qser,rp);",
        "  if (aa!=0)",
        "  {",
        f"    for (spow=0; spow<={e}; spow++)",
        "    {",
        "      bb=getAt(Pser,spow);",
        "      if (bb!=0)",
        "      {",
        "        first=J(aa,bb);",
        "        if (first!=0) { By=addAt(By,rp+spow,first); }",
        "        second=spow*bb*J(aa,h)+rp*aa*J(h,bb);",
        "        if (second!=0) { By=addAt(By,rp+spow-1,second); }",
        "      }",
        "    }",
        "  }",
        "}",
        "int hp; poly expr; poly quo; poly rem; list D;",
        f"for (hp=0; hp<={e+q+20}; hp++)",
        "{",
        "  expr=getAt(By,hp);",
        "  if (expr!=0)",
        "  {",
        "    D=division(expr,Hstd);",
        "    quo=D[1][1,1];",
        "    rem=D[2][1];",
        "    By[hp+OFFSET]=rem;",
        "    if (quo!=0) { By=addAt(By,hp+1,quo); }",
        "  }",
        "}",
        "ideal Icoeff;",
        "int coeff_count=0;",
        "proc addCoeffs(poly f)",
        "{",
        "  if (f==0) { return(); }",
        "  matrix Cp=coef(f,p);",
        "  int i; int j;",
        "  poly cp; poly cg;",
        "  matrix Cg;",
        "  for (i=1; i<=ncols(Cp); i++)",
        "  {",
        "    cp=Cp[2,i];",
        "    Cg=coef(cp,g);",
        "    for (j=1; j<=ncols(Cg); j++)",
        "    {",
        "      cg=Cg[2,j];",
        "      if (cg!=0) { Icoeff[size(Icoeff)+1]=cg; coeff_count++; }",
        "    }",
        "  }",
        "}",
        "for (hp=0; hp<=HI; hp++)",
        "{",
        "  expr=getAt(By,hp);",
        "  if (hp==0) { expr=expr-c*g; }",
        "  addCoeffs(expr);",
        "}",
        "Icoeff[size(Icoeff)+1]=Tr*c-1;",
        f'print("BUILD_DONE t={t} coeff_generators=");',
        "coeff_count;",
    ])
    if build_only:
        lines.extend([
            f'print("BUILD_ONLY total_generators_with_Tr=");',
            "size(Icoeff);",
            f'print("UNKNOWNS_INCLUDING_C {len(variables)+1}");',
            "quit;",
        ])
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return
    lines.extend([
        f"ring R={characteristic},({','.join(final_vars)}),dp;",
        "option(redSB);",
        "ideal I=imap(RB,Icoeff);",
        f'print("MAIN_START t={t} runtime_bridge characteristic={characteristic} method={method} generators=");',
        "size(I);",
        f'print("UNKNOWNS_INCLUDING_C {len(variables)+1}");',
        'print("CONTROL_EMPTY_START");',
        "ideal CE=c,Tr*c-1;",
        "ideal GE=std(CE);",
        'if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        'print("CONTROL_NONEMPTY_START");',
        "ideal CN=c-1,Tr*c-1;",
        "ideal GN=std(CN);",
        'if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        f"ideal G={method}(I);",
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (reduce(1,G)==0) { print("MAIN_UNIT"); G; } else { print("MAIN_NONUNIT"); int cap=size(G); if (cap>20) { cap=20; } for (int i=1; i<=cap; i++) { G[i]; } }',
        "quit;",
    ])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--characteristic", type=int, required=True)
    parser.add_argument("--method", choices=["std", "slimgb"], default="std")
    parser.add_argument("--build-only", action="store_true")
    parser.add_argument("--output", type=pathlib.Path)
    args = parser.parse_args()
    suffix = "Q" if args.characteristic == 0 else f"p{args.characteristic}"
    output = args.output or HERE / f"t{args.t}" / f"bridge_runtime_{suffix}_{args.method}.sing"
    emit(args.t, args.characteristic, args.method, output, build_only=args.build_only)
    print(f"{output.relative_to(ROOT)} bytes={output.stat().st_size} sha256={sha256_file(output)}")


if __name__ == "__main__":
    main()
