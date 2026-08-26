#!/usr/bin/env python3
"""AWS-only compiler for the strict D1 double-root toric chart.

This consumes the frozen independently reconstructed *ordinary* D1 tails and
substitutes, without a deformation-order truncation,

    K = z^3+p*z+c,
    f = K^3 + K*x*Qhat + x^2*Rhat,
    kbar = x*y*k,
    x*y = Lambda^6,
    Lambda = tau^3*rho.

It emits two deliberately different characteristic-zero encodings.  Encoding
A keeps the substituted tail rows factored and uses Singular's sequential
``sat`` API in a degree order.  Encoding B expands the same rows over Q and
uses two auxiliary inverses plus block elimination in a lex/degree order.
The compiler does not run Singular and makes no arc/exclusion claim.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CHARGED_SOURCE = (
    ROOT / "cases" /
    "max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825" /
    "independent_reconstruct.py"
)
CHARGED_SOURCE_SHA256 = (
    "67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623"
)

NAMES = (
    "p", "c", "a", "h", "x", "y", "la", "tau", "rho",
    "q2", "q1", "q0", "r2", "r1", "r0", "k", "mu", "nu",
)
INDEX = {name: position for position, name in enumerate(NAMES)}
ZERO = (0,) * len(NAMES)

# Coefficients a0,...,a7 of K^3+K*x*Qhat+x^2*Rhat.  Parentheses are
# intentional: encoding A retains this representation rather than asking the
# Python compiler to expand it.
COEFFICIENT_STRINGS = (
    "(c^3+x*c*q0+x^2*r0)",
    "(3*p*c^2+x*(p*q0+c*q1)+x^2*r1)",
    "(3*p^2*c+x*(p*q1+c*q2)+x^2*r2)",
    "(p^3+3*c^2+x*(q0+p*q2))",
    "(6*p*c+x*q1)",
    "(3*p^2+x*q2)",
    "(3*c)",
    "(3*p)",
    "(x*y*k)",
)


class ToricCompileFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_double_root_toric_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_charged_source():
    got = sha256(CHARGED_SOURCE.read_bytes()).hexdigest()
    if got != CHARGED_SOURCE_SHA256:
        raise ToricCompileFailure(
            ("charged source hash", got, CHARGED_SOURCE_SHA256)
        )
    spec = importlib.util.spec_from_file_location(
        "d1_double_root_toric_charged_source", CHARGED_SOURCE
    )
    if spec is None or spec.loader is None:
        raise ToricCompileFailure("cannot load charged source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def clean(poly):
    return {monomial: scalar for monomial, scalar in poly.items() if scalar}


def add(left, right):
    out = dict(left)
    for monomial, scalar in right.items():
        out[monomial] = out.get(monomial, Fraction(0)) + scalar
    return clean(out)


def scale(scalar, poly):
    scalar = Fraction(scalar)
    return clean({monomial: scalar * value
                  for monomial, value in poly.items()})


def multiply(left, right):
    out = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            out[monomial] = out.get(monomial, Fraction(0)) + lv * rv
    return clean(out)


def constant(value):
    value = Fraction(value)
    return {} if not value else {ZERO: value}


def monomial(scalar=1, **powers):
    exponent = [0] * len(NAMES)
    for name, power in powers.items():
        if name not in INDEX or not isinstance(power, int) or power < 0:
            raise ToricCompileFailure(("bad monomial", name, power))
        exponent[INDEX[name]] = power
    scalar = Fraction(scalar)
    return {} if not scalar else {tuple(exponent): scalar}


def power(poly, exponent):
    out = constant(1)
    base = poly
    while exponent:
        if exponent & 1:
            out = multiply(out, base)
        exponent //= 2
        if exponent:
            base = multiply(base, base)
    return out


def coefficient_images():
    p = monomial(p=1)
    c = monomial(c=1)
    x = monomial(x=1)
    y = monomial(y=1)
    q2 = monomial(q2=1)
    q1 = monomial(q1=1)
    q0 = monomial(q0=1)
    r2 = monomial(r2=1)
    r1 = monomial(r1=1)
    r0 = monomial(r0=1)
    kval = monomial(k=1)
    x2 = power(x, 2)
    return (
        add(add(power(c, 3), multiply(multiply(x, c), q0)),
            multiply(x2, r0)),
        add(add(scale(3, multiply(p, power(c, 2))),
                multiply(x, add(multiply(p, q0), multiply(c, q1)))),
            multiply(x2, r1)),
        add(add(scale(3, multiply(power(p, 2), c)),
                multiply(x, add(multiply(p, q1), multiply(c, q2)))),
            multiply(x2, r2)),
        add(add(power(p, 3), scale(3, power(c, 2))),
            multiply(x, add(q0, multiply(p, q2)))),
        add(scale(6, multiply(p, c)), multiply(x, q1)),
        add(scale(3, power(p, 2)), multiply(x, q2)),
        scale(3, c),
        scale(3, p),
        multiply(multiply(x, y), kval),
    )


def source_power_table(images, tails):
    maxima = [0] * len(images)
    for row in tails.values():
        for source_monomial in row:
            for index, exponent in enumerate(source_monomial):
                maxima[index] = max(maxima[index], exponent)
    table = []
    for image, maximum in zip(images, maxima):
        entries = [constant(1)]
        for _ in range(maximum):
            entries.append(multiply(entries[-1], image))
        table.append(entries)
    return table


def substitute(source_poly, table):
    out = {}
    for source_monomial, scalar in source_poly.items():
        term = constant(scalar)
        for index, exponent in enumerate(source_monomial):
            term = multiply(term, table[index][exponent])
            if not term:
                break
        out = add(out, term)
    return clean(out)


def target(ell):
    if ell == 3:
        return monomial(la=15, mu=1)
    if ell == 6:
        return monomial(la=18, nu=1)
    if ell == 8:
        return add(monomial(la=20), monomial(la=20, tau=1))
    return {}


def fraction_string(value):
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def expanded_poly_string(poly, prefix=()):
    chunks = []
    for exponents, scalar in sorted(poly.items(), reverse=True):
        factors = []
        for name, exponent in zip(NAMES, exponents):
            if exponent == 1:
                factors.append(name)
            elif exponent:
                factors.append(f"{name}^{exponent}")
        body = "*".join(factors)
        coefficient = fraction_string(scalar)
        chunks.append(f"{coefficient}*{body}" if body else coefficient)
    return "+".join(chunks).replace("+-", "-") or "0"


def compact_source_string(source_poly):
    chunks = []
    for exponents, scalar in sorted(source_poly.items(), reverse=True):
        factors = []
        for atom, exponent in zip(COEFFICIENT_STRINGS, exponents):
            if exponent == 1:
                factors.append(atom)
            elif exponent:
                factors.append(f"{atom}^{exponent}")
        body = "*".join(factors)
        coefficient = fraction_string(scalar)
        chunks.append(f"{coefficient}*{body}" if body else coefficient)
    return "+".join(chunks).replace("+-", "-") or "0"


def compact_row_string(source_poly, ell):
    raw = compact_source_string(source_poly)
    if ell == 3:
        return f"({raw})-la^15*mu"
    if ell == 6:
        return f"({raw})-la^18*nu"
    if ell == 8:
        return f"({raw})-la^20*(1+tau)"
    return raw


def canonical(poly):
    return [
        [list(monomial), scalar.numerator, scalar.denominator]
        for monomial, scalar in sorted(poly.items())
    ]


def digest(poly):
    payload = json.dumps(canonical(poly), separators=(",", ":"))
    return sha256(payload.encode()).hexdigest()


def specialize_zero(poly, names):
    positions = {INDEX[name] for name in names}
    return clean({
        monomial: scalar for monomial, scalar in poly.items()
        if all(monomial[position] == 0 for position in positions)
    })


def verify_source_weights(tails):
    report = {}
    for ell in range(1, 9):
        expected = 12 + ell
        for source_monomial, scalar in tails[ell].items():
            if not scalar:
                continue
            weight = sum((9 - index) * source_monomial[index]
                         for index in range(8)) + 6 * source_monomial[8]
            if weight != expected:
                raise ToricCompileFailure(
                    ("ordinary weight", ell, source_monomial, weight, expected)
                )
        report[str(ell)] = {
            "weight": expected,
            "support": len(tails[ell]),
        }
    return report


def common_header(rows, compact, ring_line):
    lines = [
        '// Frozen exact D1 double-root toric blow-up chart.',
        'LIB "elim.lib";',
        ring_line,
        'option(redSB);',
    ]
    for ell in range(1, 9):
        expression = (compact_row_string(rows["tails"][ell], ell)
                      if compact else expanded_poly_string(rows["rows"][ell]))
        lines.append(f"poly E{ell}={expression};")
    lines.extend([
        'poly AX=p+3*a^2;',
        'poly CU=c-2*a^3-h;',
        'poly LT=la-tau^3*rho;',
        'poly XY=x*y-la^6;',
        'poly QA=q2+q1+q0;',
        'poly QB=4*q2-2*q1+q0;',
        'poly QD=2*q2+q1;',
        'poly RA=r2+r1+r0;',
        'poly LC=27*RA-QD^2;',
        'poly INTERIOR=x*y*tau*rho;',
        'ideal I=E1,E2,E3,E4,E5,E6,E7,E8,AX,CU,LT,XY;',
    ])
    return lines


def encoding_a(rows, tag):
    ring_line = f"ring R=0,({','.join(NAMES)}),dp;"
    lines = common_header(rows, True, ring_line)
    lines.extend([
        '// Negative controls for saturation order and boundary closure.',
        'ideal CX=x;',
        'ideal CY=y;',
        'ideal CT=tau;',
        'ideal CR=rho;',
        'ideal TOY_PURE=x,y,tau,rho;',
        'list TCPX=sat(TOY_PURE,CX);',
        'ideal GTP=std(TCPX[1]);',
        'if (reduce(1,GTP)!=0) { print("FAIL_A_PURE_BOUNDARY_CONTROL"); quit; }',
        'ideal TOY_ARC=rho-tau,la-tau^4,x-tau^8,y-tau^16;',
        'list TAX=sat(TOY_ARC,CX);',
        'list TAY=sat(TAX[1],CY);',
        'list TAT=sat(TAY[1],CT);',
        'list TAR=sat(TAT[1],CR);',
        'ideal TOY_ARC_BOUNDARY=TAR[1],x,y,la,tau,rho;',
        'ideal GTAB=std(TOY_ARC_BOUNDARY);',
        'if (reduce(1,GTAB)==0) { print("FAIL_A_STRICT_ARC_CONTROL"); quit; }',
        'print("PASS_A_SYNTHETIC_CONTROLS");',
        f'print("AWS_TAG={tag}");',
        'print("ENCODING=A_FACTORED_SEQUENTIAL_SAT_DP");',
        'print("SOURCE_ROWS=EIGHT_CHARGED_ORDINARY_TAILS_NO_TRUNCATION");',
        'print("LOADS=k_mu_nu_POLYNOMIAL_COORDINATES_NOT_INVERTED");',
        'print("START_A_SAT_X");',
        'list SX=sat(I,CX);',
        'ideal S1=SX[1];',
        'print("A_AFTER_X="+string(size(S1)));',
        'print("START_A_SAT_Y");',
        'list SY=sat(S1,CY);',
        'ideal S2=SY[1];',
        'print("A_AFTER_Y="+string(size(S2)));',
        'print("START_A_SAT_TAU");',
        'list ST=sat(S2,CT);',
        'ideal S3=ST[1];',
        'print("A_AFTER_TAU="+string(size(S3)));',
        'print("START_A_SAT_RHO");',
        'list SR=sat(S3,CR);',
        'ideal S4=SR[1];',
        'print("A_AFTER_RHO="+string(size(S4)));',
        'ideal BOUNDARY=S4,x,y,la,tau,rho,a-1,h,QA,QB,LC;',
        'ideal QDI=QD;',
        'print("START_A_BOUNDARY_QD_SAT");',
        'list HQ=sat(BOUNDARY,QDI);',
        'ideal H=std(HQ[1]);',
        'print("A_H_GENERATORS="+string(size(H)));',
        'if (reduce(1,H)==0)',
        '{',
        '  print("D1_DOUBLE_ROOT_TORIC_H_IS_UNIT=1");',
        '}',
        'else',
        '{',
        '  print("D1_DOUBLE_ROOT_TORIC_H_IS_UNIT=0");',
        '  print("H_BASIS_BEGIN");',
        '  H;',
        '  print("H_BASIS_END");',
        '}',
        'print("FIREWALL=UNIT_EXCLUDES_THIS_CHART;NONUNIT_IS_ONLY_A_TOTAL_LOAD_SPACE_SURVIVOR");',
        'print("PASS_D1_DOUBLE_ROOT_TORIC_A");',
        'quit;',
    ])
    return "\n".join(lines) + "\n"


def encoding_b(rows, tag):
    variables = "u,v," + ",".join(NAMES)
    ring_line = f"ring R=0,({variables}),(lp(2),dp({len(NAMES)}));"
    lines = common_header(rows, False, ring_line)
    lines.extend([
        '// Independent inverse-variable controls.',
        'ideal TOY_PURE=x,y,tau,rho,u*INTERIOR-1;',
        'ideal GTP0=std(TOY_PURE);',
        'ideal GTP=std(eliminate(GTP0,u));',
        'if (reduce(1,GTP)!=0) { print("FAIL_B_PURE_BOUNDARY_CONTROL"); quit; }',
        'ideal TOY_ARC=rho-tau,la-tau^4,x-tau^8,y-tau^16,u*INTERIOR-1;',
        'ideal GTA0=std(TOY_ARC);',
        'ideal GTA=eliminate(GTA0,u);',
        'ideal TOY_ARC_BOUNDARY=GTA,x,y,la,tau,rho;',
        'ideal GTAB=std(TOY_ARC_BOUNDARY);',
        'if (reduce(1,GTAB)==0) { print("FAIL_B_STRICT_ARC_CONTROL"); quit; }',
        'print("PASS_B_SYNTHETIC_CONTROLS");',
        f'print("AWS_TAG={tag}");',
        'print("ENCODING=B_EXPANDED_INVERSE_ELIM_LP_DP");',
        'print("SOURCE_ROWS=EIGHT_CHARGED_ORDINARY_TAILS_NO_TRUNCATION");',
        'print("LOADS=k_mu_nu_POLYNOMIAL_COORDINATES_NOT_INVERTED");',
        'print("START_B_INTERIOR_INVERSE_ELIMINATION");',
        'ideal JU=I,u*INTERIOR-1;',
        'ideal GU=std(JU);',
        'ideal S=eliminate(GU,u);',
        'ideal GS=std(S);',
        'print("B_AFTER_INTERIOR_ELIM="+string(size(GS)));',
        'ideal BOUNDARY=GS,x,y,la,tau,rho,a-1,h,QA,QB,LC;',
        'print("START_B_BOUNDARY_QD_INVERSE_ELIMINATION");',
        'ideal JV=BOUNDARY,v*QD-1;',
        'ideal GV=std(JV);',
        'ideal H0=eliminate(GV,v);',
        'ideal H=std(H0);',
        'print("B_H_GENERATORS="+string(size(H)));',
        'if (reduce(1,H)==0)',
        '{',
        '  print("D1_DOUBLE_ROOT_TORIC_H_IS_UNIT=1");',
        '}',
        'else',
        '{',
        '  print("D1_DOUBLE_ROOT_TORIC_H_IS_UNIT=0");',
        '  print("H_BASIS_BEGIN");',
        '  H;',
        '  print("H_BASIS_END");',
        '}',
        'print("FIREWALL=UNIT_EXCLUDES_THIS_CHART;NONUNIT_IS_ONLY_A_TOTAL_LOAD_SPACE_SURVIVOR");',
        'print("PASS_D1_DOUBLE_ROOT_TORIC_B");',
        'quit;',
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    tag = require_aws()
    charged = load_charged_source()
    built = charged.build()
    if tuple(built["names"]) != tuple([f"a{i}" for i in range(8)] + ["k"]):
        raise ToricCompileFailure(("charged names", built["names"]))
    tails = built["tails"]
    if set(tails) != set(range(1, 9)):
        raise ToricCompileFailure(("charged rows", sorted(tails)))
    weight_report = verify_source_weights(tails)

    images = coefficient_images()
    table = source_power_table(images, tails)
    raw_rows = {ell: substitute(tails[ell], table) for ell in range(1, 9)}
    for ell, row in raw_rows.items():
        if specialize_zero(row, {"x"}):
            raise ToricCompileFailure(("common cubic did not vanish", ell))
        for exponent in row:
            kpower = exponent[INDEX["k"]]
            if (exponent[INDEX["x"]] < kpower or
                    exponent[INDEX["y"]] < kpower):
                raise ToricCompileFailure(("kbar scaling", ell, exponent))
    rows = {ell: add(raw_rows[ell], scale(-1, target(ell)))
            for ell in range(1, 9)}
    if any(not rows[ell] for ell in rows):
        raise ToricCompileFailure("zero charged row")
    for ell in range(1, 9):
        if add(raw_rows[ell], scale(-1, rows[ell])) != target(ell):
            raise ToricCompileFailure(("target mismatch", ell))

    payload_rows = {"tails": tails, "rows": rows}
    source_a = encoding_a(payload_rows, tag)
    source_b = encoding_b(payload_rows, tag)
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    path_a = output / "toric_A_factored_sat_dp.sing"
    path_b = output / "toric_B_expanded_inverse_lpdp.sing"
    path_a.write_text(source_a, encoding="utf-8")
    path_b.write_text(source_b, encoding="utf-8")

    payload = {
        "aws_tag": tag,
        "charged_source_sha256": CHARGED_SOURCE_SHA256,
        "ordinary_weight_report": weight_report,
        "chart": {
            "K": "z^3+p*z+c",
            "f": "K^3+K*x*Qhat+x^2*Rhat",
            "Qhat": "q2*z^2+q1*z+q0",
            "Rhat": "r2*z^2+r1*z+r0",
            "axis_cusp": ["p=-3*a^2", "c=2*a^3+h"],
            "toric": ["x*y=la^6", "la=tau^3*rho"],
            "kbar": "x*y*k",
            "targets": {
                "3": "la^15*mu",
                "6": "la^18*nu",
                "8": "la^20*(1+tau)",
            },
            "interior_saturation": "x*y*tau*rho",
            "boundary": "x=y=la=tau=rho=0,a=1,h=0",
            "leading_Q": ["Qhat(1)=0", "Qhat(-2)=0", "Qhat'(1)!=0"],
            "leading_R": "27*Rhat(1)=Qhat'(1)^2",
            "retained_Rhat_directions": 3,
        },
        "rows": {},
        "outputs": {
            path_a.name: sha256(path_a.read_bytes()).hexdigest(),
            path_b.name: sha256(path_b.read_bytes()).hexdigest(),
        },
        "firewall": (
            "unit excludes the preregistered chart; nonunit is only a "
            "total-load-space survivor and does not prove a fixed-load lift"
        ),
    }
    for ell in range(1, 9):
        payload["rows"][str(ell)] = {
            "raw_support": len(raw_rows[ell]),
            "charged_support": len(rows[ell]),
            "raw_sha256": digest(raw_rows[ell]),
            "charged_sha256": digest(rows[ell]),
        }
    canonical_payload = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print(f"payload_sha256={sha256(canonical_payload.encode()).hexdigest()}")
    print("PASS_D1_DOUBLE_ROOT_TORIC_COMPILER")


if __name__ == "__main__":
    main()
