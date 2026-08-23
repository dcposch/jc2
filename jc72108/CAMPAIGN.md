# jc72108 — the (72,108) case of the plane Jacobian Conjecture bound

Campaign to settle the last open Newton-polygon family below degree 125
(GGV-Horruitiner, arXiv:2204.14178, Prop 4.3: family A0=(8,28), (m,n)=(3,2),
i.e. (deg P, deg Q) = (108,72), reduced to [P,Q] = x^2 with prescribed polygons).
Plan: ../plan-72-108.md

## Layout
- `lib/jc.py` — exact arithmetic: bivariate polys with symbolic coefficients,
  bracket, convex-hull lattice enumeration, Generator A, msolve/Singular emitters
- `tests/test_jc.py` — property tests + hand-checked lattice counts
- `cases/emit.py` — the 7 reduced cases (5 solved regressions + 2 open subcases)
- `systems/` — emitted .ms (msolve) / .sing (Singular) inputs, .vars.json mappings
- `runs/` — solver outputs

## Semantics
Generator A transcribes a Prop 4.x reduced statement directly: unknowns = all
lattice points of hull(N(P)) and hull(N(Q)); equations = all coefficients of
[P,Q] - x^k; saturation t*prod(listed corners) = 1 forces corners attained.
"nonorigin" mode leaves the (0,0) coefficient unconstrained (conservative
w.r.t. the convention that (0,0) always belongs to the Newton polygon);
"_strict" also constrains (0,0) != 0.
GB = [1] mod p  =>  strong evidence the reduced case is empty (theorem-grade
requires an exact characteristic-zero cofactor or equivalent certificate;
mod-p emptiness for finitely many primes is evidence only).  With msolve 0.10.1,
`-g` on a characteristic-zero input prints the first-machine-prime basis, so a
char-0 header followed by `[1]` is also modular trace evidence, not a Q
certificate.
Bracket sign convention: [P,Q] := P_x Q_y - P_y Q_x; a solution of the opposite
convention corresponds to swapping (P,Q), so emptiness is convention-independent.

## Findings (probe-grade, as of 2026-07-28)
- Pipeline validated: solved case (9,24)-(3) core = EMPTY [1] mod 65521 in 2.3s
  (local + remote builds agree); raw formulations of the same case are
  intractable at <=22GB but run at 600-850GB on the 2TB box (char-0 lane).
- Rank structure: modulo the exact gauge (Q -> Q + const [+ lambda P iff
  supp P inside hull Q]), Q is determined by P; the reduced cases live in
  18 (reg) / 24 (open c2) P-coefficient variables.
- Line probe (lib/lineprobe.py, validated on the solved case): 500 lines x
  {65521, 1048573, 2147483629} give constant obstruction for open_8_28_c2 -->
  its solvability locus has codim >= 2 at all three primes; no codim-1
  solution family exists. Open verdict rests on the lane-2 msolve run.

## Status log
- 2026-07-25: Phase 1 + Generator A built, all tests pass. msolve 
  installed (brew), toy validation OK ([1] detection). 14 systems emitted:
  regression suite reg_9_27 (255 vars), reg_9_24_c1/c2/c3 (189/123/57),
  reg_7_21 (185); open case open_8_28_c1 (187 vars, 303 eqs),
  open_8_28_c2 (73 vars, 93 eqs). E1 probes started (p=65521, 10 threads).
- 2026-07-26: E1 verdict on the DIRECT formulation: too hard. Raw and
  torus-normalized reg_9_24_c3 (57/55 vars, the smallest solved case) both ran
  ~5-6 CPU-hours without finishing and OOMed a 32 GB box -> killed. The single
  degree-7 t-product saturation is suspected as a major culprit.
  Pivot v3/v4: lib/reduce.py cascade (M1 contradiction / M2 monomial forcing /
  M3 unit-linear elimination over exact Q, guarded by MAXTERMS) + per-corner
  inverse variables replacing the t-product. Cascade on reg_9_24_c3: 55 -> 38
  vars in 0.3s but densifies (median eq 131 terms). Racing v3 (cascade core,
  42 vars dense) vs v4 (no cascade, 58 vars sparse, per-corner inverses),
  p=65521, 4 threads each; 10 GB-per-process memory watchdog armed.
  Both v3 and v4 killed by watchdog at ~11 GB, no verdict. Monte Carlo linear
  probe (lib/linprobe.py, linearity of Q -> [P,Q]): 300 random P-samples mod
  65521 give ZERO consistent linear systems for both reg_9_24_c3 and
  open_8_28_c2 -> variety projects into a thin determinantal locus; mod-p
  nonemptiness NOT the explanation for the F4 grind; Monte Carlo cannot decide
  emptiness. Overnight v4 rerun launched, single process, 10 threads, watchdog
  raised to 22 GB. Big machine (r7a.48xlarge, 1.5 TB) requested from user.
  Next algorithmic lever queued: cascade ordered by boundary (rho,sigma)
  grading (GGV's valuation order) to avoid densification; then Generator B.
