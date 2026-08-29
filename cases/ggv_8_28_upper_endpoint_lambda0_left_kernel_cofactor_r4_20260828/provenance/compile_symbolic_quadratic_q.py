#!/usr/bin/env python3
"""Compile the arbitrary-quadratic-Q odd receiver ideal over Q(Q,c-modes)."""

from __future__ import annotations

from fractions import Fraction as QF
import hashlib
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py"
BASE_SHA256 = "7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1"
Q15 = ROOT / "cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_q15_20260828/verify_lambda0_q15.py"
Q15_SHA256 = "6c63fe47ebf35dd56e286ab358b0932f1dad9143875fde30c216a425119e442a"
OUT = HERE / "symbolic_quadratic_q.sing"
SCREEN = HERE / "symbolic_quadratic_q_screen.sing"
GAUSS = HERE / "symbolic_quadratic_q_gauss.sing"
RANKDROP = HERE / "symbolic_quadratic_q_rankdrop.sing"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    assert sha256(BASE) == BASE_SHA256
    assert sha256(Q15) == Q15_SHA256
    ce = load("symbolic_q_base", BASE)
    MV = ce.MV
    zero = MV.zero()
    one = (MV.const(1),)
    A = (MV.const(-1), zero, zero, zero, MV.const(1))
    Aprime = ce.xder(A)
    q = tuple(MV.var(f"q{degree}") for degree in range(3))
    f = tuple(MV.var(f"f_{degree}") for degree in range(6))

    def window_poly(prefix, degrees):
        out = [zero] * (max(degrees) + 1)
        for degree in degrees:
            out[degree] = MV.var(f"{prefix}_{degree}")
        return ce.xtrim(out)

    F9 = window_poly("f9", range(1, 8))
    F11 = window_poly("f11", range(1, 6))
    F13 = window_poly("f13", range(2, 4))
    primitives = {
        7: window_poly("d7", range(3)),
        9: window_poly("d9", range(5)),
        11: window_poly("d11", range(7)),
        13: window_poly("d13", range(9)),
        15: window_poly("d15", range(11)),
    }

    def xsum(*items):
        out = ()
        for item in items:
            out = ce.xadd(out, item)
        return out

    def product(*items):
        out = one
        for item in items:
            out = ce.xmul(out, item)
        return out

    def t5(d):
        return ce.xscale(xsum(
            ce.xscale(ce.xmul(Aprime, d), 5),
            ce.xscale(ce.xmul(A, ce.xder(d)), 2),
        ), QF(1, 2))

    q2 = ce.xmul(q, q)
    q3 = ce.xmul(q2, q)
    q4 = ce.xmul(q2, q2)
    gates = {
        7: ce.xscale(f, QF(1, 4)),
        9: xsum(ce.xscale(F9, QF(1, 4)),
                ce.xscale(ce.xmul(q, f), QF(-3, 256))),
        11: xsum(ce.xscale(ce.xmul(A, F11), QF(1, 4)),
                 ce.xscale(ce.xmul(q, F9), QF(-5, 256)),
                 ce.xscale(ce.xmul(q2, f), QF(5, 2**15))),
        13: xsum(ce.xscale(ce.xmul(ce.xpow(A, 2), F13), QF(1, 4)),
                 ce.xscale(product(A, q, F11), QF(-7, 256)),
                 ce.xscale(ce.xmul(q2, F9), QF(21, 2**15)),
                 ce.xscale(ce.xmul(q3, f), QF(7, 2**21))),
        15: xsum(ce.xscale(product(ce.xpow(A, 2), q, F13), QF(-9, 256)),
                 ce.xscale(product(A, q2, F11), QF(45, 2**15)),
                 ce.xscale(ce.xmul(q3, F9), QF(-15, 2**21)),
                 ce.xscale(ce.xmul(q4, f), QF(-45, 2**29))),
    }
    equations = []
    equation_names = []
    for weight in (7, 9, 11, 13, 15):
        residual = ce.xadd(gates[weight], ce.xscale(t5(primitives[weight]), -1))
        for degree, coefficient in enumerate(residual):
            if coefficient.terms:
                equations.append(coefficient)
                equation_names.append(f"q{weight}_x{degree}")

    def la_add(*items):
        out = {}
        for item in items:
            for exponent, poly in item.items():
                out[exponent] = ce.xadd(out.get(exponent, ()), poly)
                if not out[exponent]:
                    del out[exponent]
        return out

    def la_scale(item, scalar):
        return {exponent: ce.xscale(poly, scalar)
                for exponent, poly in item.items() if ce.xscale(poly, scalar)}

    def la_mul(left, right):
        out = {}
        for exponent1, poly1 in left.items():
            for exponent2, poly2 in right.items():
                exponent = exponent1 + exponent2
                out[exponent] = ce.xadd(
                    out.get(exponent, ()), ce.xmul(poly1, poly2)
                )
                if not out[exponent]:
                    del out[exponent]
        return out

    def series_mul(left, right, maximum):
        out = [{} for _ in range(maximum + 1)]
        for i, first in enumerate(left):
            for j, second in enumerate(right):
                if i + j <= maximum:
                    out[i + j] = la_add(out[i + j], la_mul(first, second))
        return out

    def series_power_one(base, exponent, maximum):
        assert base[0] == {0: one}
        u = list(base[:maximum + 1])
        u.extend({} for _ in range(maximum + 1 - len(u)))
        u[0] = {}
        term = [{} for _ in range(maximum + 1)]
        term[0] = {0: one}
        out = [{} for _ in range(maximum + 1)]
        choose = QF(1)
        for count in range(maximum + 1):
            if count:
                term = series_mul(term, u, maximum)
                choose *= (exponent - (count - 1)) / count
            for degree in range(maximum + 1):
                out[degree] = la_add(out[degree], la_scale(term[degree], choose))
        return out

    normalized = [{} for _ in range(16)]
    normalized[0] = {0: one}
    normalized[2] = {-1: ce.xscale(q, QF(-1, 8))}
    normalized[4] = {-2: ce.xscale(q2, QF(1, 256))}
    normalized[7] = {-3: f}
    normalized[9] = {-4: F9}
    normalized[11] = {-4: F11}
    normalized[13] = {-4: F13}
    characteristic = [{} for _ in range(16)]
    trajectories = (
        (0, 6, QF(3, 2), MV.const(1)),
        (2, 5, QF(5, 4), MV.const(1)),
        (4, 4, QF(1), MV.var("c4")),
        (6, 3, QF(3, 4), MV.var("c6")),
        (8, 2, QF(1, 2), MV.var("c8")),
    )
    for shift, a_power, exponent, scalar in trajectories:
        powered = series_power_one(normalized, exponent, 15 - shift)
        prefactor = {a_power: (scalar,)}
        for degree, value in enumerate(powered):
            characteristic[degree + shift] = la_add(
                characteristic[degree + shift], la_mul(prefactor, value)
            )

    receiver_windows = {
        9: range(0, 16), 11: range(0, 14),
        13: range(1, 12), 15: range(1, 10),
    }
    receivers = {}
    for weight, degrees in receiver_windows.items():
        receiver = window_poly(f"g{weight}", degrees)
        receivers[weight] = receiver
        denominator_power = max(0, -min(characteristic[weight]))
        numerator = ()
        for a_exponent, poly in characteristic[weight].items():
            numerator = ce.xadd(
                numerator,
                ce.xmul(ce.xpow(A, a_exponent + denominator_power), poly),
            )
        residual = ce.xadd(
            numerator,
            ce.xscale(ce.xmul(ce.xpow(A, denominator_power), receiver), -1),
        )
        for degree, coefficient in enumerate(residual):
            if coefficient.terms:
                equations.append(coefficient)
                equation_names.append(f"G{weight}_x{degree}")

    endpoint = (
        MV.var("f11_1") * MV.var("g11_0")
        + MV.var("f_0") * MV.var("g15_1")
    )
    variables = []
    for prefix, degrees in (
        ("f", range(6)), ("f9", range(1, 8)),
        ("f11", range(1, 6)), ("f13", range(2, 4)),
        ("d7", range(3)), ("d9", range(5)), ("d11", range(7)),
        ("d13", range(9)), ("d15", range(11)),
        ("g9", range(16)), ("g11", range(14)),
        ("g13", range(1, 12)), ("g15", range(1, 10)),
    ):
        variables.extend(f"{prefix}_{degree}" for degree in degrees)
    assert len(variables) == len(set(variables)) == 105
    assert len(equations) == len(equation_names)
    used = {name for equation in equations + [endpoint]
            for monomial in equation.terms for name in monomial}
    assert used <= set(variables) | {"q0", "q1", "q2", "c4", "c6", "c8"}

    lines = [
        "// Generic arbitrary-quadratic-Q odd receiver ideal.",
        "ring r=(0,q0,q1,q2,c4,c6,c8),(" + ",".join(variables) + "),lp;",
        "option(redSB);",
        "ideal I=",
        ",\n".join(equation.expression() for equation in equations) + ";",
        f'print("VARIABLES={len(variables)} EQUATIONS={len(equations)}");',
        "int start=timer;",
        "matrix T; ideal J=liftstd(I,T);",
        'print("LIFTSTD_SECONDS="+string(timer-start));',
        "poly E=" + endpoint.expression() + ";",
        "poly R=reduce(E,J);",
        'print("ENDPOINT_NORMAL_FORM="+string(R));',
        "matrix H=lift(J,ideal(E));",
        "matrix C=T*H;",
        "matrix replay=matrix(I)*C-matrix(ideal(E));",
        'print("ENDPOINT_IDEAL_MEMBER="+string(R==0));',
        'print("CERTIFICATE_REPLAY_ZERO="+string(size(module(replay))==0));',
        'write("endpoint_certificate.txt",C);',
        "quit;",
        "",
    ]
    full_text = "\n".join(lines)
    OUT.write_text(full_text)
    screen_text = full_text.replace(
        "matrix T; ideal J=liftstd(I,T);",
        "ideal J=std(I);",
    ).replace(
        "matrix H=lift(J,ideal(E));\nmatrix C=T*H;\nmatrix replay=matrix(I)*C-matrix(ideal(E));\n",
        "",
    ).replace(
        'print("CERTIFICATE_REPLAY_ZERO="+string(size(module(replay))==0));\nwrite("endpoint_certificate.txt",C);\n',
        "",
    )
    SCREEN.write_text(screen_text)
    variable_set = set(variables)
    matrix_entries = []
    for equation in equations:
        coefficients = [MV.zero() for _ in variables]
        for monomial, coefficient in equation.terms.items():
            main_variables = [name for name in monomial if name in variable_set]
            assert len(main_variables) == 1, (monomial, main_variables)
            main_variable = main_variables[0]
            parameter_monomial = tuple(
                name for name in monomial if name != main_variable
            )
            position = variables.index(main_variable)
            coefficients[position] = coefficients[position] + MV({
                parameter_monomial: coefficient
            })
        matrix_entries.extend(coefficient.expression() for coefficient in coefficients)
    gauss_lines = [
        "// Coefficient-field Gaussian version of the symbolic receiver ideal.",
        "LIB \"matrix.lib\";",
        "ring r=(0,q0,q1,q2,c4,c6,c8),(" + ",".join(variables) + "),lp;",
        f"matrix M[{len(equations)}][{len(variables)}]=",
        ",\n".join(matrix_entries) + ";",
        f'print("VARIABLES={len(variables)} EQUATIONS={len(equations)}");',
        "int start=timer;",
        "matrix RR=gauss_row(M);",
        'print("GAUSS_SECONDS="+string(timer-start));',
        "ideal J; int i; int j; poly rowpoly;",
        f"for(i=1;i<={len(equations)};i=i+1){{",
        "  rowpoly=0;",
        f"  for(j=1;j<={len(variables)};j=j+1){{ rowpoly=rowpoly+RR[i,j]*var(j); }}",
        "  if(rowpoly!=0){ J[size(J)+1]=rowpoly; }",
        "}",
        'print("ROW_RANK="+string(size(J)));',
        "ideal K=std(J);",
        "poly E=" + endpoint.expression() + ";",
        "poly R=reduce(E,K);",
        'print("ENDPOINT_NORMAL_FORM="+string(R));',
        'print("ENDPOINT_IDEAL_MEMBER="+string(R==0));',
        'write("row_reduced_ideal.txt",J);',
        "quit;",
        "",
    ]
    GAUSS.write_text("\n".join(gauss_lines))
    rankdrop_lines = [
        "// Maximal-minor rank-drop ideal in the six parameter variables.",
        "ring p=0,(q0,q1,q2,c4,c6,c8),dp;",
        f"matrix M[{len(equations)}][{len(variables)}]=",
        ",\n".join(matrix_entries) + ";",
        f'print("MATRIX={len(equations)}x{len(variables)}");',
        "int start=timer; ideal D=minor(M,105);",
        'print("MINORS_SECONDS="+string(timer-start)+" COUNT="+string(size(D)));',
        "ideal J=std(D);",
        'print("RANKDROP_BASIS_SIZE="+string(size(J)));',
        'write("rankdrop_basis.txt",J);',
        "quit;",
        "",
    ]
    RANKDROP.write_text("\n".join(rankdrop_lines))

    def substitute(poly, mapping):
        out = MV.zero()
        for monomial, coefficient in poly.terms.items():
            term = MV.const(coefficient)
            for name in monomial:
                term = term * mapping.get(name, MV.var(name))
            out = out + term
        return out

    def write_gauss_variant(filename, parameters, mapping):
        specialized = [substitute(equation, mapping) for equation in equations]
        entries = []
        for equation in specialized:
            coefficients = [MV.zero() for _ in variables]
            for monomial, coefficient in equation.terms.items():
                main_variables = [name for name in monomial if name in variable_set]
                assert len(main_variables) == 1, (filename, monomial, main_variables)
                main_variable = main_variables[0]
                parameter_monomial = tuple(
                    name for name in monomial if name != main_variable
                )
                position = variables.index(main_variable)
                coefficients[position] = coefficients[position] + MV({
                    parameter_monomial: coefficient
                })
            entries.extend(coefficient.expression() for coefficient in coefficients)
        variant_lines = [
            "// Coefficient-field Gaussian specialized receiver ideal.",
            "LIB \"matrix.lib\";",
            "ring r=(0," + ",".join(parameters) + "),(" + ",".join(variables) + "),lp;",
            f"matrix M[{len(specialized)}][{len(variables)}]=",
            ",\n".join(entries) + ";",
            f'print("VARIANT={filename} VARIABLES={len(variables)} EQUATIONS={len(specialized)}");',
            "int start=timer; matrix RR=gauss_row(M);",
            'print("GAUSS_SECONDS="+string(timer-start));',
            "ideal J; int i; int j; poly rowpoly;",
            f"for(i=1;i<={len(specialized)};i=i+1){{",
            "  rowpoly=0;",
            f"  for(j=1;j<={len(variables)};j=j+1){{ rowpoly=rowpoly+RR[i,j]*var(j); }}",
            "  if(rowpoly!=0){ J[size(J)+1]=rowpoly; }",
            "}",
            'print("ROW_RANK="+string(size(J)));',
            "ideal K=std(J);",
            "poly E=" + substitute(endpoint, mapping).expression() + ";",
            "poly R=reduce(E,K);",
            'print("ENDPOINT_NORMAL_FORM="+string(R));',
            'print("ENDPOINT_IDEAL_MEMBER="+string(R==0));',
            'write("row_reduced_variant.txt",J);',
            "quit;",
            "",
        ]
        path = HERE / filename
        path.write_text("\n".join(variant_lines))
        return path

    variants = [
        write_gauss_variant(
            "symbolic_quadratic_q_c6zero_gauss.sing",
            ("q0", "q1", "q2", "c4", "c8"),
            {"c6": MV.zero()},
        ),
        write_gauss_variant(
            "symbolic_quadratic_q_q1zero_gauss.sing",
            ("q0", "q2", "c4", "c6", "c8"),
            {"q1": MV.zero()},
        ),
        write_gauss_variant(
            "symbolic_quadratic_q_q0plusq2zero_gauss.sing",
            ("q0", "q1", "c4", "c6", "c8"),
            {"q2": MV.var("q0").scale(-1)},
        ),
        write_gauss_variant(
            "symbolic_quadratic_q_c8zero_gauss.sing",
            ("q0", "q1", "q2", "c4", "c6"),
            {"c8": MV.zero()},
        ),
        write_gauss_variant(
            "symbolic_quadratic_q_q0q2zero_gauss.sing",
            ("q1", "c4", "c6", "c8"),
            {"q0": MV.zero(), "q2": MV.zero()},
        ),
        write_gauss_variant(
            "symbolic_quadratic_q_q0q1zero_gauss.sing",
            ("q2", "c4", "c6", "c8"),
            {"q0": MV.zero(), "q1": MV.zero()},
        ),
        write_gauss_variant(
            "symbolic_quadratic_q_q1q2zero_gauss.sing",
            ("q0", "c4", "c6", "c8"),
            {"q1": MV.zero(), "q2": MV.zero()},
        ),
        write_gauss_variant(
            "symbolic_quadratic_q_q1zero_resonance_plus_gauss.sing",
            ("q0", "q2", "c4", "c8"),
            {
                "q1": MV.zero(),
                "c6": (
                    (MV.var("q0") + MV.var("q2"))
                    * (MV.var("q0") + MV.var("q2"))
                ).scale(QF(5, 6144)),
            },
        ),
        write_gauss_variant(
            "symbolic_quadratic_q_q1zero_resonance_minus_gauss.sing",
            ("q0", "q2", "c4", "c8"),
            {
                "q1": MV.zero(),
                "c6": (
                    (MV.var("q0") - MV.var("q2"))
                    * (MV.var("q0") - MV.var("q2"))
                ).scale(QF(5, 6144)),
            },
        ),
    ]
    (HERE / "equation_names.txt").write_text("\n".join(
        f"{index + 1} {name}" for index, name in enumerate(equation_names)
    ) + "\n")
    print(f"variables={len(variables)} equations={len(equations)}")
    print(f"wrote={OUT}")
    print(f"wrote={SCREEN}")
    print(f"wrote={GAUSS}")
    print(f"wrote={RANKDROP}")
    for variant in variants:
        print(f"wrote={variant}")


if __name__ == "__main__":
    main()
