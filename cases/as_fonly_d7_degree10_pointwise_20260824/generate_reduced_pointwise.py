#!/usr/bin/env python3
"""Emit the exact linearly reduced D7 degree-10 pointwise rank gate."""
from __future__ import annotations

import contextlib
import io
import os
import runpy

os.environ["MATRIX"] = "1"
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(
        os.path.join(os.path.dirname(__file__), "generate_degree10_gate.py")
    )

eadd = ns["eadd"]
escale = ns["escale"]
esubstitute = ns["esubstitute"]
sexpr = ns["sexpr"]


def var(name: str):
    return {(name,): 1}


repl = {
    # Only h=u3_2 can enter the degree-ten affine term.  The four remaining
    # degree-three free coefficients are derivative-invisible here.
    "u3_1": {},
    "u3_2": var("h"),
    "v3_1": escale(2, var("h")),
    "v3_2": {(): 1},
    # Degree-four divergence normal form.
    "u4_0": var("p"),
    "u4_1": escale(2, var("r")),
    "u4_2": {},
    "u4_3": var("q"),
    "u4_4": escale(2, var("t")),
    "v4_0": var("r"),
    "v4_1": var("s"),
    "v4_2": {},
    "v4_3": var("t"),
    "v4_4": var("w"),
    # Degree-five divergence plus divided-linear Cartier normal form.
    "u5_0": var("a"),
    "u5_1": var("b"),
    "u5_2": var("c"),
    "u5_3": var("d"),
    "u5_4": var("e"),
    "u5_5": var("f"),
    "v5_0": var("b"),
    "v5_1": var("c"),
    "v5_2": escale(2, var("d")),
    "v5_3": var("e"),
    "v5_4": var("f"),
    "v5_5": var("g"),
}

base = [esubstitute(row, repl) for row in ns["base_rows"]]
base = [row for row in base if row]
matrix = [[esubstitute(entry, repl) for entry in row] for row in ns["matrix"]]
rhs = [esubstitute(entry, repl) for entry in ns["rhs"]]

allowed = set("hpqrstwabcdefg")
for expression in base + rhs + [x for row in matrix for x in row]:
    for monomial in expression:
        assert set(monomial) <= allowed, (monomial, set(monomial) - allowed)

print("ring R=3,(h,p,q,r,s,t,w,a,b,c,d,e,f,g),dp;")
print('LIB "primdec.lib"; option(redSB);')
print("ideal H=" + ",".join(sexpr(row) for row in base) + ";")
print("matrix A[8][9]=" + ",".join(
    sexpr(entry) for row in matrix for entry in row
) + ";")
print("matrix bvec[8][1]=" + ",".join(sexpr(entry) for entry in rhs) + ";")
augmented = [row + [rhs[i]] for i, row in enumerate(matrix)]
print("matrix Aug[8][10]=" + ",".join(
    sexpr(entry) for row in augmented for entry in row
) + ";")
print("ideal GH=std(H); ideal RH=std(radical(H));")
print('print("H_size_dim_radical_size_dim");')
print("print(size(GH));print(dim(GH));print(size(RH));print(dim(RH));")
print("ideal Z5=a,b,c,d,e,f,g;ideal GZ5=std(Z5);")
print("ideal A4=minor(A,4);ideal A3=minor(A,3);"
      "ideal A1=std(minor(A,1));ideal Aug4=minor(Aug,4);")
print("ideal A1toZ=reduce(A1,GZ5);ideal ZtoA1=reduce(Z5,A1);")
print('print("rank_zero_equals_degree5_zero");'
      'if(size(A1toZ)==0&&size(ZtoA1)==0){print(1);}else{print(0);}')
print("ideal RA4=reduce(A4,RH);")
print('print("A4_remainders_mod_radical");print(size(RA4));')
print("list SR2=sat(H+A3,Z5);ideal JR2=std(SR2[1]);")
print('print("nonzero_rank_le2_sat_size_dim");print(size(JR2));print(dim(JR2));')
print("list SC=sat(H+Aug4,Z5);ideal JC=std(SC[1]);")
print('print("nonzero_compat_sat_size_dim");print(size(JC));print(dim(JC));')
print("ideal RJC=std(radical(JC));")
print("ideal Ca=b,c,d,e,f,g,s,w;")
print("ideal Cg=a,b,c,d,e,f,p,q;")
print("ideal CC=std(intersect(Ca,Cg));")
print("ideal RtoC=reduce(RJC,CC);ideal CtoR=reduce(CC,RJC);")
print('print("compat_radical_size_dim_endpoint_union_size_dim_equal");'
      'print(size(RJC));print(dim(RJC));print(size(CC));print(dim(CC));'
      'if(size(RtoC)==0&&size(CtoR)==0){print(1);}else{print(0);}')
print("ideal GV=std(H+Z5);ideal RbV=reduce(ideal(bvec),GV);")
print('print("vertical_rhs_remainders");print(size(RbV));')
print('print("compatibility_sat_GB");print(JC);')
print('print("PASS-REDUCED-POINTWISE");')
