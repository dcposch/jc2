#!/usr/bin/env python3
"""Split charged QHy generators and emit a lex-leading-term Singular job."""

from __future__ import annotations

import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
qhy = (HERE / "t6_heuristic_exact_QHy_std.sing").read_text()
match = re.search(r"ideal I=(.*?);\nideal G=", qhy, re.S)
if match is None:
    raise SystemExit("cannot find ideal I in QHy")
parts = [p.strip() for p in match.group(1).split(",\n")]
if len(parts) != 13:
    raise SystemExit("expected H + 12 generators, got %d" % len(parts))
H, gens = parts[0], parts[1:]
(HERE / "t6_heuristic_H.txt").write_text(H + "\n")
(HERE / "t6_heuristic_gens.sing").write_text(
    "ideal I=" + ",\n".join(gens) + ";\n"
)
# Self-contained lex metadata job.  lp = lex in remaining-name order.
lines = [
    "// t=6 heuristic terminal, lex (lp) in remaining-name order over A_6",
    'LIB "elim.lib";',
    "ring RAC=0,(gamma,pi),dp;",
    "poly FAC=pi;",
    "poly GAC=pi-(gamma^2)/2;",
    "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
    'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
    ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
    "ring R=(0,q13_1),(q7_0,q8_1,q9_1,q10_1,q11_1,q12_1),lp;",
    "minpoly=%s;" % H.replace("**", "^"),
    "option(redSB);",
    "ideal I=" + ",\n".join(gens) + ";",
    'print("META_START n=");',
    "size(I);",
    "for (int i=1; i<=size(I); i++)",
    "{",
    '  print("ROW"); i;',
    '  print("DEG"); deg(I[i]);',
    '  print("NTERMS"); size(I[i]);',
    '  print("LM"); leadmonom(I[i]);',
    '  print("LC"); leadcoef(I[i]);',
    "}",
    'print("META_DONE");',
    "quit;",
]
(HERE / "t6_heuristic_lex_meta.sing").write_text("\n".join(lines) + "\n")
print("H", H)
print("n_gens", len(gens))
print("wrote t6_heuristic_lex_meta.sing bytes",
      (HERE / "t6_heuristic_lex_meta.sing").stat().st_size)
