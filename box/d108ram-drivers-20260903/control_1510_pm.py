#!/usr/bin/env python3
"""Small exact saturation regression for the corrected Moh (15,10) branch."""
from __future__ import annotations

import sympy as sp


a1, a2, a9, a10, a11, a12, T = sp.symbols("a1 a2 a9 a10 a11 a12 T")
main = [
    -3*a11**2-a9**3,
    -6*a10*a11,
    -6*a11*a12+a2*a9**3,
    -3*a10**2+a9**3,
    a1*a9**3-6*a10*a12,
]
G0 = sp.groebner(main, a1, a2, a9, a10, a11, a12, T, order="lex")
G = sp.groebner(main+[T*a9-1], a1, a2, a9, a10, a11, a12, T, order="lex")
negative = sp.groebner([a9-1, a10-2, a11-3, T*a9-1],
                       a1, a2, a9, a10, a11, a12, T, order="lex")
print("RING QQ[a1,a2,a9,a10,a11,a12,T], lex")
print("MAIN_GENERATORS", len(main), "UNSAT_BASIS_SIZE", len(list(G0)),
      "UNSAT_CONTAINS_ONE", list(G0) == [1])
print("SAT_GENERATOR", T*a9-1, "SAT_BASIS_SIZE", len(list(G)),
      "SAT_CONTAINS_ONE", list(G) == [1], "BASIS", list(G))
print("NEGATIVE_BASIS_SIZE", len(list(negative)),
      "NEGATIVE_CONTAINS_ONE", list(negative) == [1])
