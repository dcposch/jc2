#!/usr/bin/env python3
"""Emit the q4_1-normalized t=3 reduced chart over its quadratic field.

The script re-derives the unique positive grading of all 37 residual rows,
checks homogeneity row by row, uses the c-row to prove q4_1 != 0 on the
c != 0 component, normalizes q4_1=1 by the weighted G_m action, and maps
the remaining equations into Q(rho), where
    147*rho^2 - 84*rho + 11 = 0.
Every source-row image is explicitly reduced modulo this polynomial.
"""

import importlib.util
import math
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


def primitive_weights(rows, variables):
    constraints = []
    for row in rows:
        terms = sp.Poly(row.expr, *variables, domain=sp.QQ).terms()
        base = terms[0][0]
        for monomial, _coefficient in terms[1:]:
            constraints.append([a - b for a, b in zip(monomial, base)])
    matrix = sp.Matrix(constraints)
    nullspace = matrix.nullspace()
    assert len(nullspace) == 1
    vector = nullspace[0]
    denominator_lcm = sp.ilcm(*[term.q for term in vector])
    integers = [int(term * denominator_lcm) for term in vector]
    divisor = math.gcd(*[abs(term) for term in integers if term])
    integers = [term // divisor for term in integers]
    if integers[0] < 0:
        integers = [-term for term in integers]
    assert all(term > 0 for term in integers)
    for row in rows:
        weights = {
            sum(exponent * weight for exponent, weight in zip(monomial, integers))
            for monomial, _coefficient in sp.Poly(row.expr, *variables, domain=sp.QQ).terms()
        }
        assert len(weights) == 1
    return integers


def reduce_mod_h(expr, rho, auxiliary_variables, hpoly):
    polynomial = sp.Poly(sp.expand(expr), *auxiliary_variables, domain=sp.QQ[rho])
    image = 0
    for monomial, coefficient in polynomial.terms():
        coefficient_expr = sp.sympify(coefficient)
        remainder = sp.rem(sp.Poly(coefficient_expr, rho, domain=sp.QQ), hpoly).as_expr()
        term = remainder
        for variable, exponent in zip(auxiliary_variables, monomial):
            term *= variable**exponent
        image += term
    image = sp.expand(image)
    # Mechanical quotient check coefficient by coefficient.
    difference = sp.Poly(sp.expand(expr - image), *auxiliary_variables,
                         domain=sp.QQ[rho])
    for _monomial, coefficient in difference.terms():
        remainder = sp.rem(sp.Poly(sp.sympify(coefficient), rho, domain=sp.QQ), hpoly)
        assert remainder.is_zero
    return image


def main():
    prep = load("triangular_preprocess_qfield",
                ROOT / "box/k16t3-20260903/preprocessed/triangular_preprocess.py")
    driver = load("t_order_system_qfield",
                  ROOT / "box/k16t3-20260903/t3/t_order_system.py")
    data = driver.build(t=3, gauged=True)
    reduction = prep.reduce_chart(data, max_pivots=256, max_seconds=300,
                                  max_expression_bytes=2_000_000)
    assert len(reduction.pivots) == 13 and len(reduction.rows) == 37

    c = data["c"]
    x = next(v for v in reduction.remaining_variables if str(v) == "q4_1")
    y = next(v for v in reduction.remaining_variables if str(v) == "q7_1")
    grading_variables = list(reduction.remaining_variables) + [c]
    weights = primitive_weights(reduction.rows, grading_variables)
    weight_map = dict(zip(map(str, grading_variables), weights))
    assert weight_map["q4_1"] == 13
    assert weight_map["q7_1"] == 26
    assert weight_map["c"] == 65

    c_rows = [row for row in reduction.rows if c in row.expr.free_symbols]
    assert len(c_rows) == 1
    c_row = c_rows[0]
    c_rhs = sp.solve(sp.Eq(c_row.expr, 0), c)[0]
    d = 2 * x**2 - 21 * y
    assert sp.expand(c_rhs - 10 * x * y * d / 343) == 0

    xy_rows = [row for row in reduction.rows
               if c not in row.expr.free_symbols and row.expr.free_symbols <= {x, y}]
    assert len(xy_rows) == 1
    h_row = xy_rows[0]
    h_primitive = prep.primitive_integer_polynomial(
        h_row.expr, grading_variables
    )[0].as_expr()
    expected_h = 11 * x**4 - 84 * x**2 * y + 147 * y**2
    assert sp.expand(h_primitive - expected_h) == 0

    rho = sp.Symbol("rho")
    hpoly = sp.Poly(147 * rho**2 - 84 * rho + 11, rho, domain=sp.QQ)
    assert hpoly.is_irreducible
    assert sp.discriminant(hpoly.as_expr(), rho) == 588
    assert sp.gcd(hpoly, sp.Poly(rho, rho, domain=sp.QQ)).degree() == 0
    assert sp.gcd(hpoly, sp.Poly(2 - 21 * rho, rho, domain=sp.QQ)).degree() == 0

    auxiliary_variables = [v for v in reduction.remaining_variables if v not in (x, y)]
    mapped_rows = []
    mapped_sources = []
    all_source_images = []
    for row in reduction.rows:
        primitive = prep.primitive_integer_polynomial(
            row.expr, grading_variables
        )[0].as_expr()
        specialized = sp.expand(primitive.subs(c, c_rhs).subs({x: 1, y: rho}))
        image = reduce_mod_h(specialized, rho, auxiliary_variables, hpoly)
        all_source_images.append((row.source_index, image))
        if image != 0:
            mapped_rows.append(image)
            mapped_sources.append(row.source_index)
    assert dict(all_source_images)[c_row.source_index] == 0
    assert dict(all_source_images)[h_row.source_index] == 0
    assert len(mapped_rows) <= 35
    assert all(x not in row.free_symbols and y not in row.free_symbols and c not in row.free_symbols
               for row in mapped_rows)

    def render(expr):
        return str(sp.expand(expr)).replace("**", "^")

    print("// exact t=3 q4_1-normalized quadratic-field chart")
    print("// 13 audited constant Q* pivots; 37 residual source rows mapped")
    print("// unique primitive positive weights: %s" %
          ",".join("%s:%d" % (name, weight_map[name])
                   for name in map(str, grading_variables)))
    print("// q4_1 weight=13 and c!=0 => q4_1!=0; weighted scaling sets q4_1=1")
    print("// c image=10*rho*(2-21*rho)/343 is nonzero in Q(rho)")
    print("// zero source images: %s" %
          ",".join(str(source) for source, image in all_source_images if image == 0))
    print("// retained source indices: %s" % ",".join(map(str, mapped_sources)))
    print("ring RAC=0,(gamma,pi),dp;")
    print("poly FAC=pi;")
    print("poly GAC=pi-(gamma^2)/2;")
    print("poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);")
    print('if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
          ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }')
    # Genuine Rabinowitsch wrapper controls live in their own declared Q ring;
    # the normalized main ring below has already eliminated c and T.
    print("ring RWRAP=0,(c,T),dp;")
    print("option(redSB);")
    print("ideal CE=c,T*c-1;")
    print("ideal GE=std(CE);")
    print('if (typeof(GE)=="ideal" && nameof(basering)=="RWRAP" && reduce(1,GE)==0)'
          ' { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }')
    print("ideal CN=c-1,T*c-1;")
    print("ideal GN=std(CN);")
    print('if (typeof(GN)=="ideal" && nameof(basering)=="RWRAP" && reduce(1,GN)!=0)'
          ' { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }')
    print("ring R=(0,rho),(%s),dp;" % ",".join(map(str, auxiliary_variables)))
    print("minpoly=147*rho^2-84*rho+11;")
    print("option(redSB);")
    print('if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); }'
          ' else { print("CONTROL_RING_FAIL"); }')
    print("number CIMAGE=10*rho*(2-21*rho)/343;")
    print("number LOCIMAGE=rho*(2-21*rho);")
    print("number INVLOC=1/LOCIMAGE;")
    print('if (CIMAGE!=0 && INVLOC*LOCIMAGE==1)'
          ' { print("CONTROL_FIELD_LOCALIZATION_PASS"); }'
          ' else { print("CONTROL_FIELD_LOCALIZATION_FAIL"); }')
    print('print("MAIN_START original_equations=51 triangular_rows=37 mapped_nonzero_rows=%d variables=%d coefficient_field=Q(rho)");' %
          (len(mapped_rows), len(auxiliary_variables)))
    print("ideal I=%s;" % ",\n".join(render(row) for row in mapped_rows))
    print("ideal G=slimgb(I);")
    print('print("MAIN_DONE basis_size=");')
    print("size(G);")
    print('if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); }'
          ' else { print("MAIN_NONTRIVIAL_SUPERSET_ONLY"); }')
    print("G;")
    print("quit;")


if __name__ == "__main__":
    main()
