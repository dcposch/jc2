# Round 2 W root: minimal odd-prime `W_2` discriminator

**Date:** 2026-08-24  
**Cap:** `AS3-MIN-W2`  
**Verdict:** **`W2-SURVIVOR`** (finite-field / `W_2(F_3)` tier only)  
**Independent replay:** **PASS**

## 1. Decisive result

The preregistered two-value cap stopped at its first survivor.  Over
`F_3`, the map

\[
F=(P,Q)=(x+2x^3,y)=(x-x^3,y)
\]

has Jacobian one, exact generic degree three, and the marked collision

\[
(0,0),(1,0)\longmapsto(0,0).
\]

Its complete unrestricted first Witt obstruction vanishes.  With the
Teichmuller representative `[2]=8` in `W_2(F_3)=Z/9`, take

\[
\widetilde P=x+8x^3,\qquad \widetilde Q=y.
\]

Then

\[
[\widetilde P,\widetilde Q]
 =1+24x^2
 =1+3(8x^2),
\qquad E=2x^2\pmod3.
\]

The top de Rham / Cartier basis in characteristic three consists of the
monomials `x^(3r+2)y^(3s+2) dx wedge dy`.  The `y` exponent of `E` is zero,
so the obstruction class is zero.  The independently recovered correction

\[
A=0,\qquad B=x^2y
\]

satisfies `[A,Q]+[P,B]=x^2=-E` in `F_3[x,y]`.  Hence

\[
P_2=x+8x^3,\qquad Q_2=y+3x^2y
\]

obeys

\[
[P_2,Q_2]=1+27x^2+72x^4\equiv1\pmod9.
\]

The same displayed points `(0,0)` and `(1,0)` remain distinct and both map
to `(0,0)` modulo 9.  Thus no moving-point subtlety is needed for this
witness.

## 2. Deduplication and why this cap was typed

This run did not invent a new finite-field search universe.  The campaign
already records the family

\[
F_{\rm AS}=(x-x^p,y)
\]

as a characteristic-`p` finite-etale, degree-`p` nonautomorphism control in
`xmodel/sol-pcurvature.md`; `xmodel/review-round1-proof-gates-claude.md`
independently checks those properties.  The prior promoted Witt campaign in
`xmodel/sol-witt.md`, with review in `xmodel/grok-witt-review.md`, concerns a
characteristic-two Mondello support slice and its characteristic-two relaxed
controls.  Repository-wide deduplication found no prior `F_3`, `Z/9`, or
`W_2(F_3)` computation on the exact Artin--Schreier support.

Accordingly the preregistration chose the smallest *repository-typed*
odd-prime Artin--Schreier cap: `p=3`,

\[
P_a=x+a x^3,\quad Q=y,\quad a\in\{1,2\},
\]

with exact supports `{x,x^3}` and `{y}` and fixed marked points.  This is not
a claim of global minimality among all polynomial-map supports.  The map was
known; its odd-prime `W_2` status was the genuinely untested discriminator.

The cap, equations, prediction, verdict taxonomy, cost, and stop were frozen
in `cases/round2_witt_oddprime/PREREGISTRATION.md` before either enumerator
ran.  Its header contains a transparent timestamp-only correction; filesystem
creation preceded `results.json` by about four minutes, and no mathematical
or stopping text changed.

## 3. Complete bounded census

The exact-support coefficient order was `a=1,2`.

| `a` | Jacobian over `F_3` | marked images | Witt gate |
|---:|---|---|---|
| 1 | `1` | `(0,0)`, `(2,0)` | rejected at marked collision |
| 2 | `1` | `(0,0)`, `(0,0)` | **`W2-SURVIVOR`** |

For `a=2`, over `K=F_3(U,V)` the generic fibre is

\[
K[x,y]/(2x^3+x-U,\ y-V).
\]

Division by the cubic gives the exact basis `1,x,x^2`, hence generic degree
three.  Its derivative in `x` is one, so this computation is separable and is
not a finite-point count.

The first survivor occurred at the last coefficient value.  The registered
stop fired immediately: no `F_5`, support expansion, or further lifting level
was run.

## 4. Independent replay and provenance

`search.py` uses sparse polynomial dictionaries and constructs the
unrestricted de Rham primitive.  `replay.py` imports none of that code: it
uses a separate term-list determinant implementation, independently enumerates
the two special fibres, proves the triangular generic-fibre basis, recomputes
the Teichmuller lift and Cartier class, row-reduces a separate correction
matrix over `F_3`, and directly checks the producer's determinant and marked
collision over `Z/9`.  The independent solve has rank 10 on its fixed
24-column witness box and also returns `B=x^2y`.

Replay commands:

```text
python3 cases/round2_witt_oddprime/search.py \
  --output cases/round2_witt_oddprime/results.json
python3 cases/round2_witt_oddprime/replay.py \
  --input cases/round2_witt_oddprime/results.json \
  --output cases/round2_witt_oddprime/replay.json
python3 cases/round2_witt_oddprime/verify.py
```

The producer canonical-claim SHA-256 is
`875682b644f367ee8b841d3e433b8706b3f95a25bb1200b6f20395faa8f7dff9`.
The independent-core SHA-256 is
`9ee96b84ac81f36f921235987bcfcf33a71484a5e5a93aba4757f81efcdb834c`.
`MANIFEST.sha256` pins every owned input, executable, result, replay, and this
report; `provenance.json` separately pins the pre-existing campaign sources.

## 5. Exact interpretation boundary

This result proves exactly one bounded statement: a degree-three
characteristic-three Keller collision on the registered support survives the
first unrestricted Witt lifting obstruction and has an explicit polynomial
Keller-collision lift over `Z/9`.

It does **not** provide a bounded-support compatible tower through all Witt
levels, a `W_3` lift, a `Z_3` or integral lift, descent or algebraization in
characteristic zero, a polynomial germ, a JC2 counterexample, or evidence that
any of those objects exists.  Indeed the displayed `W_2` correction already
adds `x^2y` to the second coordinate.  The only campaign-level update licensed
by this cap is that the total characteristic-two obstruction on the promoted
Mondello stratum does not extend as a blanket first-Witt obstruction across
odd primes and other supports.

