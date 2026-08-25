#!/usr/bin/env python3
"""Compile the exact p=1 parity-involution quotient of the loaded fibre."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"
DESCENT_REPLAY = ROOT / "cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.py"
DESCENT_REPLAY_SHA256 = "5dcb0a67d79859c04d83d2c20ff8518a148a78c1229f42b00169c5842d5e7256"


def load_parent():
    for path, expected in (
        (PARENT, PARENT_SHA256),
        (DESCENT_REPLAY, DESCENT_REPLAY_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError(f"dependency hash mismatch: {path}: {got}")
    spec = importlib.util.spec_from_file_location("q8_quotient_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(PARENT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_parent()
M = P.M
RAW_NAMES = ["w", "b2", "b4", "b6", "x1", "x3", "x5"]
APPROX_NAMES = ["w", "c", "d2", "d4", "x1", "x3", "x5"]


def power(value, exponent, ring):
    out = ring.one
    for _ in range(exponent):
        out = M.cmul(out, value)
    return out


def quotient_polynomial(value, parity, ring):
    """Substitute a_(2i)=t*b_(2i), w=t^2, p=a7/3=1.

    For odd rows, parity=1 also divides the result by t.  Character purity
    makes every remaining t exponent even; failure is fatal.
    """
    w, b2, b4, b6, x1, x3, x5 = [ring.var(name) for name in RAW_NAMES]
    one = ring.one
    out = {}
    for monomial, scalar in value.items():
        e0, e1, e2, e3, e4, e5, e6, e7, ek = monomial
        if ek:
            continue  # k=0
        normal_degree = e0 + e2 + e4 + e6
        if normal_degree % 2 != parity:
            raise RuntimeError(("character failure", monomial, parity))
        term = M.cscale(scalar, one)
        images = (
            (w, (normal_degree - parity) // 2),
            (b2, e2),
            (b4, e4),
            (b6, e6),
            (x1, e1),
            (M.cadd(one, x3), e3),
            (M.cadd(M.cscale(3, one), x5), e5),
        )
        for image, exponent in images:
            term = M.cmul(term, power(image, exponent, ring))
        term = M.cscale(3 ** e7, term)
        out = M.cadd(out, term)
    return out


def approximate_quotient_polynomial(value, parity, ring):
    """Use K=z^3+z+q and the punctured chart t=x0, q=t*c.

    Approximate-cubic residuals are x0=t, x2=t*d2, x4=t*d4 and
    w=t^2.  Raw depressed coefficients are reconstructed exactly before
    the odd rows are divided by t.
    """
    w, c, d2, d4, x1, x3, x5 = [ring.var(name) for name in APPROX_NAMES]
    one = ring.one
    c2 = power(c, 2, ring)
    normal_images = {
        0: M.cadd(one, M.cmul(w, power(c, 3, ring))),
        2: M.cadd(M.cscale(3, c), d2),
        4: M.cadd(M.cscale(6, c), d4),
        6: M.cscale(3, c),
    }
    invariant_images = {
        1: M.cadd(x1, M.cscale(3, M.cmul(w, c2))),
        3: M.cadd(M.cadd(one, x3), M.cscale(3, M.cmul(w, c2))),
        5: M.cadd(M.cscale(3, one), x5),
    }
    out = {}
    for monomial, scalar in value.items():
        e0, e1, e2, e3, e4, e5, e6, e7, ek = monomial
        if ek:
            continue
        normal_degree = e0 + e2 + e4 + e6
        if normal_degree % 2 != parity:
            raise RuntimeError(("character failure", monomial, parity))
        term = M.cscale(scalar, one)
        term = M.cmul(
            term, power(w, (normal_degree - parity) // 2, ring)
        )
        for index, exponent in ((0, e0), (2, e2), (4, e4), (6, e6)):
            term = M.cmul(term, power(normal_images[index], exponent, ring))
        for index, exponent in ((1, e1), (3, e3), (5, e5)):
            term = M.cmul(term, power(invariant_images[index], exponent, ring))
        term = M.cscale(3 ** e7, term)
        out = M.cadd(out, term)
    return out


def compile_quotient(coordinates="approx"):
    source = P.compile_fibre()
    names = APPROX_NAMES if coordinates == "approx" else RAW_NAMES
    ring = M.Ring(names)
    converter = (
        approximate_quotient_polynomial
        if coordinates == "approx"
        else quotient_polynomial
    )
    quotient = {
        ell: converter(source["tails"][ell], ell % 2, ring)
        for ell in range(1, 9)
    }
    imposed = (1, 3, 5, 7, 2, 4)
    return ring, quotient, imposed, names


def stats_payload(coordinates):
    ring, quotient, imposed, names = compile_quotient(coordinates)
    rows = {}
    for ell in range(1, 9):
        value = quotient[ell]
        rows[f"r{ell}{'_over_t' if ell % 2 else ''}"] = {
            "terms": len(value),
            "total_degree": max((sum(monomial) for monomial in value), default=0),
            "w_degree": max((monomial[0] for monomial in value), default=0),
            "sha256": M.coefficient_digest(value),
            "imposed": ell in imposed,
        }
    return {
        "case": "max12_912_order3_nu_q8_global_quotient_probe_20260824",
        "chart": ({
            "p": 1,
            "a0": "t",
            "a2": "t*b2",
            "a4": "t*b4",
            "a6": "t*b6",
            "w": "t^2",
            "a1": "x1",
            "a3": "1+x3",
            "a5": "3+x5",
            "a7": 3,
            "k": 0,
        } if coordinates == "raw" else {
            "p": 1,
            "approximate_cubic": "K=z^3+z+q",
            "parameter": "t=x0",
            "q": "t*c",
            "x0": "t",
            "x2": "t*d2",
            "x4": "t*d4",
            "w": "t^2",
            "k": 0,
        }),
        "coordinates": coordinates,
        "variables": names,
        "equations": ["r1/t", "r3/t", "r5/t", "r7/t", "r2", "r4"],
        "outputs": ["r6", "r8"],
        "rows": rows,
        "scope": (
            "exact quotient compiler and bounded CAS probe only; no component, "
            "global relation, trajectory, max12, or JC2 conclusion"
        ),
    }


def singular_source(prime, include_rho, include_nu, order, saturate,
                    localize, coordinates, print_basis, eliminate_outputs):
    ring, quotient, imposed, names = compile_quotient(coordinates)
    outputs = ([] if not include_rho else ["rho"]) + ([] if not include_nu else ["nu"])
    variables = names + outputs + ([] if not localize else ["inv"])
    if order == "dp":
        ordering = "dp"
    else:
        internal = len(names) - 1  # internal variables; keep w with outputs
        tail = 1 + len(outputs)
        variables = names[1:] + ([] if not localize else ["inv"]) + [names[0]] + outputs
        internal += int(localize)
        ordering = f"(dp({internal}),dp({tail}))"
    lines = [
        'LIB "primdec.lib";',
        f"ring R={prime},({','.join(variables)}),{ordering};",
        "option(redSB);",
    ]
    for ell in imposed:
        lines.append(
            f"poly e{ell}={M.coeff_string(quotient[ell], names)};"
        )
    generators = [f"e{ell}" for ell in imposed]
    if include_rho:
        lines.append(f"poly erho=rho-({M.coeff_string(quotient[8], names)});")
        generators.append("erho")
    if include_nu:
        lines.append(f"poly enu=nu-({M.coeff_string(quotient[6], names)});")
        generators.append("enu")
    if localize:
        lines.append("poly einv=inv*w*x5*(x3-2*x5)-1;")
        generators.append("einv")
    lines.extend([
        f"ideal I={','.join(generators)};",
    ])
    if saturate:
        lines.extend([
            "ideal Q=w*x5*(x3-2*x5);",
            "ideal Isat=sat(I,Q);",
        ])
    lines.extend([
        f"ideal G=slimgb({'Isat' if saturate else 'I'});",
        'print("Q8-QUOTIENT-STATS");',
        'print("dim="+string(dim(G)));',
        'print("size="+string(size(G)));',
        'print("vdim="+string(vdim(G)));',
    ])
    if print_basis:
        lines.append("G;")
    if eliminate_outputs:
        if not outputs:
            raise RuntimeError("--eliminate-outputs requires --rho or --nu")
        internal_names = names[1:] + ([] if not localize else ["inv"])
        lines.extend([
            f"ideal E=eliminate(G,{'*'.join(internal_names)});",
            'print("elimination_size="+string(size(E)));',
            "E;",
        ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--singular", action="store_true")
    parser.add_argument("--prime", type=int, default=32003)
    parser.add_argument("--rho", action="store_true")
    parser.add_argument("--nu", action="store_true")
    parser.add_argument("--order", choices=("dp", "block"), default="dp")
    parser.add_argument("--saturate", action="store_true")
    parser.add_argument("--localize", action="store_true")
    parser.add_argument(
        "--coordinates", choices=("approx", "raw"), default="approx"
    )
    parser.add_argument("--print-basis", action="store_true")
    parser.add_argument("--eliminate-outputs", action="store_true")
    args = parser.parse_args()
    if args.singular:
        print(singular_source(
            args.prime, args.rho, args.nu, args.order, args.saturate,
            args.localize, args.coordinates, args.print_basis,
            args.eliminate_outputs,
        ))
    else:
        print(json.dumps(stats_payload(args.coordinates), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
