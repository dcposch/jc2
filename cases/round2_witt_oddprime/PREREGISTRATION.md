# Preregistration: `AS3-MIN-W2`

Timestamp: 2026-08-24T02:47:27Z (filesystem creation, before executing either
enumerator).  Administrative note: the first header mistakenly read
`03:18:00Z`; this timestamp-only correction was made after the initial replay.
No cap, equation, prediction, verdict, cost, or stop text changed.

## Typed source and deduplication

The special-fibre family is not invented for this run.  The campaign already
records the characteristic-`p` negative control

\[
F_{\rm AS}=(x-x^p,y)
\]

in `xmodel/sol-pcurvature.md` and independently checks its Keller, finite
etale, degree-`p`, nonautomorphism properties in
`xmodel/review-round1-proof-gates-claude.md`.  The promoted Witt work
`xmodel/sol-witt.md`, reviewed in `xmodel/grok-witt-review.md`, exhausts a
registered characteristic-two Mondello hull-plus-shell slice and records
relaxed characteristic-two controls.  Repository-wide searches found no
characteristic-three `W_2`, `Z/9`, or obstruction computation for the exact
Artin--Schreier support below.  Thus the map is a pre-existing typed control;
the fixed odd-prime Witt cap and its `W_2(F_3)` test are new.

This is the smallest repository-typed odd-prime Artin--Schreier cap: choose
the least allowed odd prime `p=3` and the exact inherited supports

\[
S_P=\{(1,0),(3,0)\},\qquad S_Q=\{(0,1)\}.
\]

No claim of global minimality among arbitrary polynomial-map supports is part
of the run.

## Frozen cap and equations

Over `k=F_3`, enumerate in the order `a=1,2`

\[
P_a=x+a x^3,\qquad Q=y.
\]

The nonzero condition on `a` makes `S_P` exact; `Q` is fixed.  Fix the two
distinct marked source points and target

\[
r_0=(0,0),\quad r_1=(1,0),\quad c=(0,0).
\]

A datum enters the Witt gate exactly when all coefficient equations in

\[
[P_a,Q]-1=0,\qquad F_a(r_0)-c=0,\qquad F_a(r_1)-c=0
\]

hold in `F_3`.  Its generic degree is computed at the exact generic fibre,
not by finite-point counting.

For an entering datum, lift every coefficient by its Teichmuller
representative in `W_2(F_3)=Z/9` and set

\[
E=([\widetilde P,\widetilde Q]-1)/3\pmod 3.
\]

The unrestricted correction equation is

\[
E+[A,Q]+[P,B]=0\quad\text{in }F_3[x,y].
\]

The complete plane obstruction is the class of `E dx wedge dy` in
`H^2_dR(F_3[x,y])`; its Cartier support consists exactly of terms
`x^i y^j` with `i == j == 2 (mod 3)`.  If the class vanishes, the producer
must emit explicit `A,B`, a determinant-one lift modulo 9, and lifts of both
marked collision points.  The independent replay must recompute all of these
without importing producer code.

## Falsifiable verdicts

- `W2-SURVIVOR`: an entering odd-generic-degree datum has zero unrestricted
  obstruction and an exact `Z/9` determinant-one collision witness.
- `CAP-EXHAUSTED-NO-SURVIVOR`: both values of `a` are tested and none meets
  the preceding condition.
- `INVALID-CAP`: an asserted special-fibre equation, generic-degree
  certificate, divisibility by 3, correction, collision lift, or independent
  replay check fails.  Stop without redesign.

Primary prediction: `W2-SURVIVOR` at `a=2`.  This prediction is frozen and is
not a verdict until both exact implementations agree.

## Cost and stop

- Special-fibre budget: exactly two coefficient values, at most two exact
  Jacobian/collision checks.
- Witt budget: at most one obstruction/correction solve before the predicted
  stop; no Groebner basis or network call.
- Stop at the first `W2-SURVIVOR` in the frozen order.  If none survives,
  stop after `a=2` with complete cap exhaustion.
- Forbidden in this run: support enlargement, `F_5` after an `F_3` survivor,
  `W_3`, an all-level tower, characteristic-zero inference, a germ or JC2
  counterexample claim, network access, and shared-ledger edits.
