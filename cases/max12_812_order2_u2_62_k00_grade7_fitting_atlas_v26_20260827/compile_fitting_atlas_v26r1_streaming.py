#!/usr/bin/env python3
"""Run the unchanged V26 compiler with a streaming flat-sum parser."""

from __future__ import annotations

import ast
from fractions import Fraction

import compile_fitting_atlas_v26 as base


def top_level_terms(source: str) -> list[str]:
    terms: list[str] = []
    depth = 0
    start = 0
    for index, character in enumerate(source):
        if character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
            if depth < 0:
                base.fail(("streaming parser unmatched close", index))
        elif character in "+-" and depth == 0 and index > start:
            term = source[start:index]
            if not term or term in ("+", "-"):
                base.fail(("streaming parser empty term", index))
            terms.append(term)
            start = index
    if depth != 0:
        base.fail(("streaming parser unclosed parentheses", depth))
    tail = source[start:]
    if not tail or tail in ("+", "-"):
        base.fail("streaming parser empty tail")
    terms.append(tail)
    return terms


def streaming_parse_poly(text: str,
                         aliases: dict[str, str] | None = None) -> base.Poly:
    source = "".join(text.split())
    if not source or any(character in source for character in ';,"'):
        base.fail(("malformed exact polynomial", source[:120]))
    out: base.Poly = {}
    mapping = aliases or {}
    for term in top_level_terms(source):
        piece = base.parse_ast_poly(
            ast.parse(term.replace("^", "**"), mode="eval").body, mapping)
        for monomial, coefficient in piece.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
            if out[monomial] == 0:
                del out[monomial]
    return out


def adapter_controls() -> None:
    aliases = {"x": "d0_1", "y": "d1_1"}
    toys = (
        "(1/2)*x^2-3*x*y+5",
        "-x+(y-(x-y))*((3/7)+2)",
        "x-x+y-y+((x+y)-(x+y))",
        "((x+y)^2)-(x^2+2*x*y+y^2)",
        "-(3/5)*x^3+(7/11)*y^4-(-2)*x",
    )
    for source in toys:
        old = base.parse_poly(source, aliases)
        new = streaming_parse_poly(source, aliases)
        if old != new:
            base.fail(("streaming/original parser toy mismatch", source))
    signed = streaming_parse_poly("x-y+2", aliases)
    mutated = streaming_parse_poly("x+y+2", aliases)
    if signed == mutated:
        base.fail("streaming sign-deletion mutation survived")
    long_source = "+".join(f"{index}*x" for index in range(1, 5001))
    long_value = streaming_parse_poly(long_source, aliases)
    expected = base.p_scale(base.p_var("d0_1"), Fraction(5000 * 5001, 2))
    if long_value != expected:
        base.fail("streaming long-flat-sum control")
    for malformed in ("x+", "x+(y", "x+y)"):
        try:
            streaming_parse_poly(malformed, aliases)
        except Exception:
            pass
        else:
            base.fail(("streaming malformed control accepted", malformed))


def main() -> None:
    adapter_controls()
    base.parse_poly = streaming_parse_poly
    base.main()


if __name__ == "__main__":
    main()
