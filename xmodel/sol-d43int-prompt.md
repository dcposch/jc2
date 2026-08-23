You are the implementation lane (own it end-to-end). Repo: /Users/dc/code/math/jc2
(NOTE: renamed from .../jc72108; docs moved: ladder docs in ladder/, but all
cases/ and xmodel/ paths are unchanged). Continue xmodel/sol-clift.md, whose ONLY
blocker was missing artifacts: the d43red band checkpoints are NOW RECOVERED at
cases/d43red/ (40 files, both primes p=105337/105673: d43red_p*_a00pp_band{6..42}.pkl
+ summary jsons, exact copies of box01:cases43/d43red/). Read xmodel/sol-clift.md
IN FULL first, plus xmodel/sol-lift.md sect 1.2-1.3 and sect 3.3. Write to
xmodel/sol-d43int.md; emit engines/certificates under cases/.

TARGET: complete Stage 2 of the algebraization gate -- the first certified
characteristic-zero D43 point -- by finishing the two steps sol-clift could not run:

  1. COMMON INTEGRAL MODEL (sol-lift step 1, now unblocked). From the recovered
     band checkpoints build the integral 218-row model (34 parked + 95 old graph
     bands 6-24 + 89 late graph bands 26-42) over Z[1/N] or Z_p, RETAINING the
     radical variables (W_i^4 = A_i integrally; Hensel-lift the coefficient
     radicals r3, zeta42, A1, A2, h as sol-clift did). Run the full reduction
     audit sol-clift couldn't: row/term/hash regression of the mod-p reductions
     against the banked systems, and the integral NF/parked membership traces
     (R_raw = R_NF + sum Q_i P_i integrally, or the p-adic analogue).
  2. DIMENSION / GENERATION / FLATNESS at the witness (sol-lift step 4). The
     known data: full Jacobian rank 131 at the witness (unit minor det=810),
     tangent dim 53, p^2 correction SOLVABLE. Now certify: local dimension = 53
     (equivalently height 131), the 131 selected equations locally generate all
     218 after localizing at the minor, and p-flatness. CAUTION: at the FREE=0
     parked origin, 9 band-10 rows degenerate to identities and a Singular std
     attempt timed out at 10 CPU-min. If the origin is too degenerate, MOVE to a
     less degenerate point of the same modular component (e.g. generic FREE
     values that still satisfy all 218 rows -- search the A^14 cell) and certify
     there; a smooth-anywhere point suffices for X_43(C) nonempty.
     For the dimension computation consider: exact triangular/pivot structure of
     the recovered checkpoints (the bands are staged eliminations -- use the
     stage structure instead of a blind Groebner basis), or a localized
     complete-intersection argument from the 131 unit minor + a 53-parameter
     local parametrization.

  SUCCESS = standard-smooth certificate => Hensel/formal smoothness (Stacks 02H6)
  => Z_p-point => X_43^full(C) != empty. State it as: FIRST CERTIFIED CHAR-0 D43
  POINT (stage 2 cleared), with full replay instructions.
  If a step genuinely cannot be certified, report exactly which and why (e.g.
  the component is everywhere singular => next move is family-wide, name it).

Honest tiers; never claim what the certificate does not support. No git ops; no
full-file msolve (segfault hazard); exact arithmetic. Terse, technical.
