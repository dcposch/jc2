# lib/families.py — GGV5 family enumeration (Phase 1 of SECTION4-AUTOMATION.md)

Faithful pure-integer port of the generation pipeline of GGV5 =
arXiv:1708.07936 (PLLC / starting edges / generated corners / children /
complete chains / divisibility-admissibility / `GetmnFamilies`, plus the
`(q_k)` machinery of Remark 2.29). No coefficient arithmetic, no `JC_BACKEND`
dependence; exact `int`/`Fraction` lattice arithmetic only.

## Usage

```python
from families import *

get_pllc(25)                  # Algorithm 1: possible last lower corners
admissible_complete_chains(35)         # all admissible complete chains, v11(A0) <= M
enumerate_families(35)        # [(chain, Family)]  -> the 24 rows F1..F24 of GGV5 S5
case_rows(150)                # {(corner path, (m,n), maxdeg)} -> the 34 GGV5 S6 cases
section4_families()           # {'9_27','9_24','8_28','7_21'} -> CornerData (gate B)
```

Corners are `Corner(a, l, b)` = the GGV5 corner `(a %% l, b)`, geometric point
`(a/l, b)`; chains are `Chain(edges=(Edge(A, A'), ...), final=Corner)`;
families are `Family(k, i, m0, n0, d1, d2)` with coprime members
`(m0 + j*d1, n0 + j*d2)`, `j >= 0` (GGV5 orientation, eq. (3.1); `(n,m)` swaps
implicit). Tests: `python3 tests/test_families.py` — gate A (10-case table of
arXiv:2204.14178 S2, nothing else below maxdeg 125), gate B (S4 corner data),
plus the full GGV5 S5 (24 families) and S6 (34 cases) tables.

## What Phase 2 (the reduction engine) consumes

`CornerData` (from `corner_data(chain, fam, j)` / `section4_families()`):

- `A0, A0p, chain, final` — the admissible complete chain, verbatim GGV5 data;
- `steps` — per edge `h`: `(rho_h, sigma_h, p_h, q_h)` with
  `(rho,sigma) = dir(A_h - A_h')` and `p/q = (rho+sigma)/v_{rho,sigma}(A_h)`
  reduced — the certificate exponents for rule R1/R2 (Cor 7.4 edge powers);
- `k, family, mn, j, degP, degQ` — instantiation bookkeeping
  (`deg P = m*(a0+b0)` etc.);
- `S, c, upper_dir` — start polygon in 1/m units:
  `conv({(0,0)} + integral chain corners + {(0,c)})`,
  `c = v_{upper_dir}(A0)`, `upper_dir = (1 - ceil(b0/a0), 1)`. Phase 2 must
  RE-DERIVE `(0,c)` via R1–R3 (design S2 note) and may use `S` only as the
  expected answer; `supports(cd)` gives the unreduced `SuppP = m*S`,
  `SuppQ = n*S`;
- `rhs_exp = ceil(b0/a0) - 2` — the bracket RHS is `x^rhs_exp` after
  finalization (R10); pure lattice data, fixed before any branching.

Regression values (gate B): `(9,27)`: steps `((1,0,1,9),(3,-1,2,3))` — the
q=9 certificate GGV22 uses on the flipped `(-2,1)` edge — final `(11/3,8)`;
`(9,24)`: `((3,-1,2,3),)`; `(8,28)`: `((4,-1,3,4),)`, RHS `x^2`;
`(7,21)`: `((7,-2,5,7),)`.

## Divergences from the printed paper (flagged, none hidden)

1. **II.b) (1,0)-direction guard.** `GetStartingEdges` as printed admits
   vertical first edges `(A0, (a0, b'))` with `v_{1,-1}(A') > 0` (e.g.
   `((6,18),(6,0))`, `((9,27),(9,0))`, `((9,27),(9,3))`); these pass
   `GetIsAdmissible` and would add 4 spurious S5 families and duplicate
   `(9,27)`-path chains, contradicting the paper's own tables. GGV5's proof of
   Theorem 2.19 shows a type II.b) corner of a *standard* pair cannot have
   direction `(1,0)` ("because (P,Q) is standard"); since `rho = 1` in `I`
   forces `(1,0)`, the guard `(rho,sigma) != (1,0)` when `v_{1,-1}(A') > 0`
   is added. With it, all published tables are reproduced exactly.
2. **F6 presentation.** The S5 table prints `F6 = (3j+4, 8j+10)`, which is not
   coprime at even `j` (and the claim "in all cases except F4 we have
   k/e_k = 1" misses F6, where `k/e_k = 2`). `GetmnFamilies` (paper's own
   Algorithm 9, with its `(kbar*D1, kbar*D1)` typo corrected to
   `(kbar*D1, kbar*D2)`) yields `(7+6j, 18+16j)` — exactly the coprime members
   of the printed progression. Tested as set equality.
3. **Prose count.** GGV5 S5 says "14 admissible complete chains of length 1
   and 2 of length 2"; its own table lists 7 length-2 families from 7 chains.
   This port: 14 length-1 and 7 length-2 chains carrying families at M = 35.
   The tables, not the sentence, are the regression target.
