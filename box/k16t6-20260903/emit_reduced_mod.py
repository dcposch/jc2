#!/usr/bin/env python3
"""Reduce charged t=6 heuristic QHy generators modulo the three campaign primes.

Ring map (same as charged emit_qhy): GF(p)[q13_1, q7_0, q8_1, q9_1, q10_1,
q11_1, q12_1, W], dp; generators are H_6 plus the 12 terminal rows, with
integer coefficients reduced in Z before the Singular parse.  W is only used
in wrapper controls.
"""

from __future__ import annotations

import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import k16t56_pipeline as P  # noqa: E402

PRIMES = (32003, 32009, 32027)
VARS = "q13_1,q7_0,q8_1,q9_1,q10_1,q11_1,q12_1,W"


def reduce_integer_tokens(text: str, prime: int) -> str:
    """Replace coefficient-like integers by their residue in 0..p-1.

    Identifiers such as q13_1 are left alone because their digits sit next
    to letters or underscores.
    """
    out = []
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        start_number = ch.isdigit() or (
            ch == "-" and i + 1 < n and text[i + 1].isdigit()
            and (i == 0 or text[i - 1] in "=(,+\n \t")
        )
        if start_number:
            j = i + 1 if ch == "-" else i
            while j < n and text[j].isdigit():
                j += 1
            prev = text[i - 1] if i else ""
            if prev.isalnum() or prev == "_":
                out.append(text[i:j])
            else:
                out.append(str(int(text[i:j]) % prime))
            i = j
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def drop_zero_terms(poly: str) -> str:
    """Drop 0*monomial and lone 0 summands after modular reduction."""
    if not poly.strip():
        return "0"
    parts = re.split(r"(?=[+-])", poly.strip())
    kept = []
    for part in parts:
        token = part.strip()
        if not token:
            continue
        body = token[1:] if token[0] in "+-" else token
        body = body.lstrip()
        if body == "0" or body.startswith("0*"):
            continue
        kept.append(token if token[0] in "+-" else ("+" + token))
    if not kept:
        return "0"
    text = "".join(kept)
    if text[0] == "+":
        text = text[1:]
    return text


def extract_ideal(qhy: str) -> list[str]:
    match = re.search(r"ideal I=(.*?);\nideal G=", qhy, re.S)
    if match is None:
        raise SystemExit("cannot find ideal I in QHy")
    parts = [p.strip() for p in match.group(1).split(",\n")]
    if len(parts) != 13:
        raise SystemExit("expected H + 12 generators, got %d" % len(parts))
    return parts


def emit_mod(prime: int, generators: list[str]) -> str:
    reduced = [drop_zero_terms(reduce_integer_tokens(g, prime)) for g in generators]
    H, gens = reduced[0], reduced[1:]
    lines = [
        "// t=6 terminal + H_t in GF(%d)[y, remaining]; method=std" % prime,
        "// coefficients reduced in Python from charged QHy before parse",
        'LIB "elim.lib";',
        "ring RAC=%d,(gamma,pi),dp;" % prime,
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
        ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        'if (nameof(basering)=="RAC") { print("CONTROL_RAC_RING_PASS"); }'
        ' else { print("CONTROL_RAC_RING_FAIL"); }',
        "ring R=%d,(%s),dp;" % (prime, VARS),
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); }'
        ' else { print("CONTROL_RING_FAIL"); }',
        *P.wrapper_controls("R", "q13_1", "R"),
        'print("MAIN_START t=6 char=%d rows=12 vars=6 plus_H=1 method=std reduced=1");'
        % prime,
        "ideal I=%s;" % ",\n".join([H] + gens),
        "ideal G=std(I);",
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (typeof(G)=="ideal" && nameof(basering)=="R")'
        ' { print("MAIN_EXTRACT_RING_PASS"); }'
        ' else { print("MAIN_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); G; }'
        ' else { print("MAIN_NONTRIVIAL");'
        ' print("BASIS_OUTPUT_TRUNCATED_TO_10");'
        ' int basis_cap=size(G); if (basis_cap>10) { basis_cap=10; }'
        ' for (int basis_i=1; basis_i<=basis_cap; basis_i++)'
        ' { G[basis_i]; } }',
        "quit;",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    qhy = (HERE / "t6_heuristic_exact_QHy_std.sing").read_text()
    parts = extract_ideal(qhy)
    for prime in PRIMES:
        path = HERE / ("t6_heuristic_mod_p%d_reduced_std.sing" % prime)
        text = emit_mod(prime, parts)
        path.write_text(text)
        print(path.name, path.stat().st_size, "nonzero_gens",
              sum(1 for g in text.split("ideal I=")[1].split(";")[0].split(",\n")
                  if g.strip() != "0"))


if __name__ == "__main__":
    main()
