#!/usr/bin/env python3
"""Emit an exact localized t=3 system after the audited constant pivots.

In the 37-row triangular reduction, the unique c-row is
  20*x^3*y - 210*x*y^2 - 343*c = 0,
where x=q4_1 and y=q7_1.  Thus c=10*x*y*(2*x^2-21*y)/343.  On c != 0,
Rabinowitsch localization is therefore exactly localization at
x*y*(2*x^2-21*y).  We eliminate c using only the constant pivot -343,
remove T, and introduce U with U*x*y*(2*x^2-21*y)-1.  No variable-dependent
coefficient is divided out.
"""

import importlib.util
import pathlib
import sys
import sympy as sp


ROOT = pathlib.Path("/home/ubuntu/jc2")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    prep = load("triangular_preprocess",
                ROOT / "box/k16t3-20260903/preprocessed/triangular_preprocess.py")
    driver = load("t_order_system",
                  ROOT / "box/k16t3-20260903/t3/t_order_system.py")
    data = driver.build(t=3, gauged=True)
    reduction = prep.reduce_chart(data, max_pivots=256, max_seconds=300,
                                  max_expression_bytes=2_000_000)
    assert len(reduction.pivots) == 13
    assert len(reduction.rows) == 37
    x, y, c, U = sp.symbols("q4_1 q7_1 c U")
    d = 2 * x**2 - 21 * y
    c_rows = [row for row in reduction.rows if c in row.expr.free_symbols]
    assert len(c_rows) == 1
    c_row = c_rows[0]
    c_rhs = sp.solve(sp.Eq(c_row.expr, 0), c)[0]
    assert sp.expand(c_rhs - 10 * x * y * d / 343) == 0

    rows = []
    row_sources = []
    variables_for_primitive = list(reduction.remaining_variables) + [U]
    for row in reduction.rows:
        if row.source_index == c_row.source_index:
            continue
        image = sp.expand(row.expr.subs(c, c_rhs))
        if image == 0:
            continue
        primitive, _multiplier, _denominator, _content = \
            prep.primitive_integer_polynomial(image, variables_for_primitive)
        rows.append(primitive.as_expr())
        row_sources.append(row.source_index)
    localization = sp.expand(U * x * y * d - 1)
    assert c not in set().union(*(row.free_symbols for row in rows))
    assert len(rows) == 36

    variables = list(reduction.remaining_variables) + [U]
    print("// exact t=3 localization after 13 audited Q* pivots")
    print("// c-row source=%d; residual rows 37 -> 36; c,T -> U" % c_row.source_index)
    print("// c=10*q4_1*q7_1*(2*q4_1^2-21*q7_1)/343")
    print("// localization equation U*q4_1*q7_1*(2*q4_1^2-21*q7_1)-1")
    print("// retained source indices: %s" % ",".join(map(str, row_sources)))
    print("ring RAC=0,(gamma,pi),dp;")
    print("poly FAC=pi;")
    print("poly GAC=pi-(gamma^2)/2;")
    print("poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);")
    print('if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
          ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }')
    print("ring R=0,(%s),dp;" % ",".join(map(str, variables)))
    print("option(redSB);")
    print('if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); }'
          ' else { print("CONTROL_RING_FAIL"); }')
    print("poly D=q4_1*q7_1*(2*q4_1^2-21*q7_1);")
    print("ideal CE=D,U*D-1;")
    print("ideal GE=std(CE);")
    print('if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); }'
          ' else { print("CONTROL_EMPTY_FAIL"); }')
    print("ideal CN=q4_1-1,q7_1-1,U*D-1;")
    print("ideal GN=std(CN);")
    print('if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); }'
          ' else { print("CONTROL_NONEMPTY_FAIL"); }')
    print('print("MAIN_START original_equations=51 triangular_rows=37 localized_rows=36 chart_variables=22 localization_variables=1 characteristic=0");')
    generators = [prep.singular_polynomial(row, variables) for row in rows]
    generators.append(prep.singular_polynomial(localization, variables))
    print("ideal I=%s;" % ",\n".join(generators))
    print("ideal G=slimgb(I);")
    print('print("MAIN_DONE basis_size=");')
    print("size(G);")
    print('if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); }'
          ' else { print("MAIN_NONTRIVIAL_SUPERSET_ONLY"); }')
    print("G;")
    print("quit;")


if __name__ == "__main__":
    main()
