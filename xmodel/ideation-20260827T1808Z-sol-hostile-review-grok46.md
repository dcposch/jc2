# Hostile review: Sol q-compressions and contracting-`G_m` lemma

Reviewer: Grok 4.6 (different-model hostile referee)
Date: 2026-08-27
Pinned model ID: `grok-4.6`
CLI/version: `grok 1.0.5 (5115b46bc909)` (`/Users/dc/.grok/bin/grok`)
Host: Python 3.14.6, Darwin arm64
Charged source:
`xmodel/ideation-20260827T1808Z-sol.md`
Common packet:
`xmodel/ideation-20260827T1808Z-packet.md`

Status: **IDEATION AUDIT / NOT A PROMOTION DOCUMENT.**  Nothing in the
charged source is promoted by this review.

## Overall verdict

The `q2=Z/16` identity and the two displayed `q1` parametrizations are
desk-correct on the **reduced, squarefree (coprime) field-point cascade**,
with one load-bearing wording repair on branch P, one novelty repair, and
the `c2`/`A|V` collapse standing only under squarefree `A`.  They do **not**
cut `F1` beyond the already-promoted gates, and they do **not** reduce the
affine endpoint to four or five parameters.

The contracting-`G_m` mechanism is a legitimate finite-type client at
**fixed** `H`, once `D22=1` is homogenized to `D22=lambda` and one saturates
by `lambda` (not by the irrelevant ideal).  The written chain

```text
J proper  iff  J localized at the zero section is proper
          iff  its completed local extension is proper
```

is **false** as soon as weight-zero parameters remain, and it is the wrong
lemma if applied to the unsaturated ideal `I`.  The exact repaired lemma
and its scope are in §3.  No charged atom assumes GGV landing, a general
algebraization theorem, or coverage; the sentence in §8 that a local
Kuranishi calculation is “globally decisive” is a scope hazard, not a
hidden landing hypothesis.

| # | Charged atom | Verdict |
|--:|---|---|
| 1 | `F1=HV`, `F2=(V^2+HZ)/4` `=>` `q2=Z/16` on the reduced cascade | **CONFIRMED** as a rational identity in char `≠2`, on both branches, with polynomial exactness of `q2 dX`. Conditional on the reduced field-point cascade, not on the nonreduced scheme |
| 2 | This supplies a section of the promoted affine-surjective `q2` residue map, so `q2` is redundant on the cascade | **CONFIRMED** as an explicit particular on the reduced cascade locus, **not** as a section over all `F1`. Adds no `F1` cut. Does **not** imply `D24=0` |
| 3 | Branch-P `V=A'R+2AR'`, `deg R<=4`, five parameters | **CONFIRMED** as the `V`-coordinate form of the already-promoted `im T_A ∩ A^2` intersection. **NOVELTY REPAIR:** this is not a new composition with the `D6` cascade |
| 4 | Branch-P `c2≠0` / `A|V` collapses to `R=cA`, `V=3cAA'` | **CONFIRMED** on squarefree `A`. **GAP/REPAIR:** squarefreeness is load-bearing; Card A’s discriminator does not shard `c2=0` vs `A|V` |
| 5 | Branch-Q `Q=A^2BR`, `V=2A'BR+3AB'R+4ABR'`, `deg R<=3`, four parameters | **CONFIRMED** on squarefree coprime `(A,B)` in char `0`. Coprimeness and both squarefree hypotheses are load-bearing |
| 6 | Four/five-parameter “endpoint reduction” | **REFUTED** as an endpoint statement. The counts are the dimensions of the simultaneous cascade-`F1` plus `q1` loci, not of `D22=1` |
| 7 | Weights `wt(F_n)=wt(G_n)=n`, `wt(lambda)=22`; `D_n` weighted homogeneous; `D22-lambda` homogeneous of weight 22 | **CONFIRMED** |
| 8 | Nonempty `V(I)∩D(lambda)` iff `J=I:lambda^∞` proper; nonzero `lambda` normalizes to `1` after a 22nd root | **CONFIRMED** scheme-theoretically for (8a); **CONFIRMED** for geometric points over an alg. closed field of char `∤22` for (8b). Not a `k`-point statement |
| 9 | `J` proper iff `J` localized at the contracted zero section is proper iff the completed local extension is proper | **CONFIRMED** at **fixed** `H` (`S_0=k`) for the **lambda-saturated** ideal. **REFUTED** in the parenthetical relative form, and **REFUTED** if applied to unsaturated `I` or to the origin of a parameter space |
| 10 | Novelty of `q2=Z/16`, Q four-parameter form, `c2` collapse, and `D22=lambda` client | **CONFIRMED** as `NEW CONNECTION` / `NEW MECHANISM AT D5G SCOPE` after the P five-parameter novelty repair |
| 11 | Global JC2 / landing / algebraization / coverage | **CONFIRMED** that the source does not treat those as theorems. **SCOPE-RISK** on “globally decisive without a separate algebraization theorem” |

---

## Custody and execution disclosure

Live SHA-256 of the charged bytes:

```text
79d32289ece2010929197d0bb189582395b4bca39dd6a4b9fb4b68233e17ed78  xmodel/ideation-20260827T1808Z-sol.md
e388864250cdaa7bd23d5eb0babe8929bf0c02d80758ae91d708202ea9e2f6cc  xmodel/ideation-20260827T1808Z-packet.md
```

Both match the freeze pins exactly.

Supporting sources used only as named inputs, independently rehashed:

```text
6e3d9104effe39c0dd0e34377bb7bdc6ede4f25f472f9f9c0098706aceffb60a  xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md
7358e6623a84ddd6b1aaad1a9b07a1c0c8966f74f75203977c0314bf3588e7ec  xmodel/ggv-8_28-upper-cascade-w3-w6-hostile-review-fable5-20260827.md
56a4b940fb415a1c98aef675ff6f5625fd646341f4fa4e30bdab12e3f59e5387  xmodel/ggv-qgate-opus-new-claims-hostile-review-grok46-20260827.md
46736edc8aa391e50d3c6a1604937bcad85361c25c25f9e3b4c184e19f8afed1  xmodel/ggv-survivor-q1-q2-de-rham-gates-fable5-hostile-review-opus5-20260827.md
```

The packet at `18:08Z` still called the cascade review unfinished.  The
Fable5 file now present confirms the **reduced field-point** formulas
`F1=HV`, `F2=(V^2+HZ)/4` through `D6` and rejects the producer’s
“full solution scheme” wording.  I treated that confirmation as the meaning
of “reviewed reduced upper cascade,” and I rederived every identity charged
below from the D5G row, the promoted `T_A`/`T_Q`/`q2` formulas, and exact
`fractions.Fraction` polynomial arithmetic.  Producer `PASS` strings and
Fable5’s own replay were not used as evidence.

This session had a shell.  I wrote only desk-scale exact Python in
`/tmp/g46sol` (no `sympy`/`flint`/Gröbner, no AWS, no producer import).  I
did not enter, read, build, status-inspect, or touch `jc2-lean`.  I did not
edit any canonical ledger, case freeze, or any file other than this report.
I did not read the peer `18:08Z` ideations `fable5`/`opus5`/`grok46`.

Consumed, not trusted: D5G
`D_n=sum_{i+j=n}((12-j)F_i'G_j+(i-8)F_i G_j')` with `F_0=H^2`, `G_0=H^3`;
R7R1 `q2=F2/(4H)-F1^2/(16H^3)` (PROVISIONAL as a de Rham gate, licensed
through `D24=0`); promoted
`T_A(Q)=2AQ'-3A'Q`, `deg Q<=12` and
`T_Q(Q)=4ABQ'-(6A'B+AB')Q`, `deg Q<=11`.

---

## Item 1 — `q2=Z/16` on the reduced cascade

**Verdict: CONFIRMED** as an identity of rational functions, on both
squarefree degree-eight branches, in characteristic not `2`.  Polynomial
exactness of `q2 dX` on `K(X)` is then immediate.  This is a statement
about reduced field points with `F1=HV` and `F2=(V^2+HZ)/4`.  It is not a
statement about the nonreduced coefficient scheme, and it is not `D24=0`.

### 1.1 The identity

The reviewed reduced cascade (producer `6e3d9104...`, Fable5 atoms 4, 8, 9)
gives, on both P (`H=A^2`) and Q (`H=A^2B`),

```text
F1 = H V,                 deg V <= 7,
F2 = (V^2 + H Z)/4,       deg Z <= 6.
```

Substitute the promoted R7R1 formula

```text
q2 = F2/(4H) - F1^2/(16 H^3).
```

Then, in `K(X)`,

```text
4 H^2 F2 - F1^2
  = 4 H^2 · (V^2 + H Z)/4  -  (H V)^2
  = H^2 V^2 + H^3 Z        -  H^2 V^2
  = H^3 Z,
```

hence `q2=Z/16`.  Every cancellation is polynomial after clearing the
common denominator `16 H^3`: the identity
`4 H^2 F2 - F1^2 = H^3 Z` holds in `K[X]` as soon as
`F2=(V^2+HZ)/4` and `F1=HV`.

Independently replayed on `A=X^4-1` (branch P), on the R5 pair
`A=X^3-(2/5)X`, `B=X^2-1` (branch Q), and on a generic degree-eight `H`.
All three returned identical polynomials.  The identity does **not** use
squarefreeness, coprimeness, or the degree bounds; those enter only to
place `(V,Z)` on the reviewed cascade.

### 1.2 Denominators, windows, characteristic

- The `4` in `F2` and the `4,16` in `q2` require `char K ≠ 2`.  The
  campaign default `char 0` is enough.  Over `Q` the division
  `(V^2+HZ)/4` is automatic in `Q[X]`; there is no extra integrality
  condition.
- `deg V<=7` and `deg H=8` put `deg F1<=15`, the frozen `F1` window.
  `deg V^2<=14` and `deg HZ<=14` put `deg F2<=14`, the frozen `F2`
  window.  `deg Z<=6` is forced by `H|(4F2-V^2)` inside that window,
  matching cascade `(6.4)`.
- After cancellation, `q2=Z/16` has **no poles at the roots of `H`**.
  The original presentation `F2/(4H)-F1^2/(16H^3)` is therefore regular
  at those roots on every reduced cascade point.

### 1.3 Polynomial exactness

On `P^1`, a polynomial differential `f dX` has no finite poles.  In the
chart `X=1/t`, `dX=-dt/t^2`, so
`f(1/t)(-dt/t^2)` has terms `t^{-d-2}` for `deg f=d>=0`.  The residue
(`t^{-1}` coefficient) would require `d=-1`, which never occurs.  Hence
every polynomial is exact on `K(X)`, with polynomial primitive
`(1/16) integral Z dX`.  Trace descent of the promoted `q2` row is not
needed on this locus: `q2` already lies in `K[X]`.

R7R1 remains PROVISIONAL as a **gate**: the named rational function is
the de Rham coordinate only through `D24=0`.  The identity that this
rational function equals `Z/16` does not use that license.

### 1.4 What this does and does not add beyond affine-surjectivity

Promoted `q2` (Grok46 `56a4b940...`, item 4): the residue map on the
15-dimensional `F2` window is surjective, so **every** `F1` admits some
`F2` making `q2 dX` exact.  Linear-image codimension is `4` on P and `5`
on Q.  There is no induced `F1` cut.

The cascade statement is strictly narrower and strictly more explicit:

- It does **not** section the residue map over the whole `F1` window.
  Cascade `F1` are those with `H|F1` (and the later reduced constraints).
  Calling this “an explicit section” of the promoted surjection is
  overstated.  Repair: *the reduced cascade locus lies in the exact-`q2`
  set, via the explicit particular `F2=(V^2+HZ)/4`*.
- It **does** show that, on that locus, one need not search for an `F2`:
  every cascade `F2`, for every polynomial `Z` of degree `<=6`, is already
  exact.  That is stronger than mere existence of some `F2` for those
  `F1`.
- It adds **no** `F1` obstruction.  It deletes a de Rham cut on the
  reduced cascade, rather than creating one.
- It does **not** imply the coefficient row `D24=0`.  Skipping a separate
  **de Rham** `q2` cut on reduced cascade points is legitimate; omitting
  `D24` from the determinant target is not.
- It does **not** apply to the dual-number thickening
  `F1=epsilon f` with `H` not dividing `f`.  That `R`-point fails
  `F1=HV` (Fable5 atom 10).  First-order exactness of `q2` along those
  tangents is a linearized residue condition, not `Z/16`.

Maximum licensed claim: on reduced field points of the reviewed cascade,
the R7R1 rational function `q2` is the polynomial `Z/16`, hence exact as
a differential on `K(X)`, identically in the remaining cascade parameters.
Computation on that reduced locus may skip a residue-vanishing `q2` gate.
It may not skip `D24`, and it may not replace the uncompressed scheme.

---

## Item 2 — Branch-P and branch-Q `q1` parametrizations by `R`

### 2.1 Branch P, five parameters

**Verdict: CONFIRMED** as a coordinate rewrite of the promoted intersection
`im T_A ∩ A^2 K[X]_{<=7}`, dimension `5`, on squarefree `A`.  **NOVELTY
REPAIR:** this is not a new composition with the `D6` cascade.  It is the
promoted weight-3 gate `A^2|F1` (already `F1=A^2 V`) intersected with
promoted `q1`.

Promoted `T_A(Q)=2AQ'-3A'Q`, injective on `deg Q<=12` for squarefree
quartic `A`.  Direct expansion (hand, and replayed):

```text
T_A(A^2 R) = 2A(A^2 R)' - 3A'(A^2 R)
           = 4 A^2 A' R + 2 A^3 R' - 3 A^2 A' R
           = A^2 (A' R + 2 A R').
```

On the cascade, `F1=H V=A^2 V`.  Membership in `im T_A` is therefore
`A^2 V = T_A(A^2 R)` for a unique `R`, i.e.

```text
V = A' R + 2 A R',       deg R <= 4.
```

The degree bound is forced: `deg Q=deg(A^2 R)=8+deg R` with no leading
cancellation, `deg T_A=deg Q+3` off the `deg Q=6` resonance (here
`deg Q>=8`), and `deg F1<=15` forces `deg R<=4`.  Replayed:
`deg T_A(A^2)=11`, `deg T_A(A^2 X^4)=15`, `deg T_A(A^2 X^5)=16`.
The map `R |-> V` is injective because `T_A` is.  Domain dimension `5`.

Sol’s sentence “`F1` is in `im T_A` exactly when the preimage has the form
`Q=A^2 R`” is **false** as a statement about all of `im T_A`.  It is true
on the cascade (equivalently, on `A^2|F1`).  Repair: restrict the
quantifier to `F1` already divisible by `A^2`.

Nit, not a defect of the `V`-locus: the ODE derivation of `q1` produces
`F1=2 T_A(Q)` rather than `F1=T_A(Q)`.  In `char ≠ 2` these are the same
subspace.  Using `F1=2 T_A(A^2 R)` only rescales `R` and replaces
`V=3c AA'` below by `V=6c AA'`.  The geometric line is `⟨AA'⟩` either way.
A later certificate freeze should carry the factor `2`; the parametrized
locus need not.

**Novelty.**  The charged source itself records the promoted dimensions
`9,5,7`.  The displayed basis
`T_A(A^2 R)=A^2(2AR'+A'R)`, `deg R<=4`, **is** that dimension-`5`
intersection.  Writing it as `V=A'R+2AR'` is a change of coordinates on
an already-banked linear space, not a new interface with rows `4--6`.
Closest hit: boxed transversality theorem in
`xmodel/ggv-qgate-opus-new-claims-hostile-review-grok46-20260827.md`.
Verdict on this atom: `KNOWN`, rephrased.

### 2.2 Branch P, `c2` / `A|V` special branch

**Verdict: CONFIRMED** on squarefree `A`.  **GAP/REPAIR:** squarefreeness
is the entire implication `A|V => A|R`, and Card A does not shard the two
P components.

Reviewed cascade row five: polynomial solutions through `D5` on P are the
union of `{c2=0}` and `{A|V}` (arbitrary `c2`).  On the second component,
`V=A'R+2AR'` and `A|V` give `A|(A'R)` because `2AR'` is already `0 mod A`.
Squarefree `A` means `gcd(A,A')=1`, so `A|R`.  Then `deg R<=deg A=4` forces
`R=cA` with `c in K`, and

```text
V = A'(cA) + 2A(c A') = 3c A A'.
```

Replayed on `A=X^4-1`: among all `3125` polynomials `R` of degree `<=4`
with coefficients in `{-2,...,2}`, `A|V` if and only if `A|R`; and
`R=5A` produces `V=15 A A'`.  The degree coincidence `deg R<=deg A` is
load-bearing for “one parameter.”

**Counterexample if squarefree is dropped.**  Take
`A=X^2(X-1)^2=X^4-2X^3+X^2` and `R=X(X-1)`.  Then `deg R=2<=4`, `A` does
not divide `R`, but `A` **does** divide `V=A'R+2AR'`.  The collapse
`R=cA` is false.  This `A` is a degree-four non-squarefree P-shape.  The
same degeneration already drops the `q1` and weight-3 codimensions; the
special branch cannot be quoted off the squarefree locus.

Card A’s cheapest discriminator substitutes `V=A'R+2AR'` with
`deg R<=4` and “the cascade `F2,F3`” without splitting `c2=0` (five
`R`-parameters, `c2` set to `0`) from `A|V` (`R=cA`, `c2` free).  Running
the five-parameter `V` with free `c2` includes points that fail row five.
Repair: shard exactly as the software paragraph already proposes
(`c2=0` versus `c2≠0`).

This collapse **is** a new composition: it uses the `D5` mode gate
`A|V`, which is not in the promoted `q1`/`weight-3` package.  Novelty:
`NEW CONNECTION` at that interface.

### 2.3 Branch Q, four parameters

**Verdict: CONFIRMED** in characteristic zero, `deg(A,B)=(3,2)`, **both
squarefree**, `gcd(A,B)=1`.  The extra `A` beyond the promoted `AB`
intersection is load-bearing, and both squarefree and coprime are
load-bearing for that extra `A`.

Promoted: if `AB | T_Q(Q)` then `Q=AB S` with `deg S<=6`, and

```text
T_Q(AB S) = AB ( 4 AB S' + (-2 A' B + 3 A B') S ).
```

Cascade `F1=H V=A^2 B V` asks for the stronger divisibility `A^2 B | T_Q(Q)`.
After the `AB` step one needs `A` to divide the inner factor.  Reducing
modulo `A`,

```text
inner ≡ -2 A' B S   (mod A).
```

Squarefree coprime and `char ≠ 2` make `A'` and `B` units modulo `A`, so
`A|S`.  Thus `Q=A^2 B R` with `S=AR`.  The `q1` window `deg Q<=11` and
`deg(A^2 B)=8` force `deg R<=3` (no resonance: `deg Q=8+r >=8 >5`).
Replayed: `deg T_Q(A^2 B)=12`, `deg T_Q(A^2 B X^3)=15`,
`deg T_Q(A^2 B X^4)=16`.  Direct expansion (hand and replayed)

```text
T_Q(A^2 B R) = A^2 B ( 2 A' B R + 3 A B' R + 4 A B R' ),
```

so

```text
V = 2 A' B R + 3 A B' R + 4 A B R',       deg R <= 3.
```

Four coefficients.  The map `R |-> V` has trivial kernel on the R5-style
coprime pair `A=X^3+X+1`, `B=X^2-1` (grid of coefficients in `{-1,0,1}`).
Degrees saturate the cascade window: `deg V=4,5,6,7` for `deg R=0,1,2,3`.

The extra `A` is three independent conditions on the promoted
7-dimensional `AB` intersection (`S` unrestricted of degree `<=6`, `A`
squarefree of degree `3`), giving `7-3=4`.  This is genuinely stronger
than the banked dimension-`7` statement.  Novelty: `NEW CONNECTION`.

**Counterexample, coprimeness dropped.**  `A=X^3+1`, `B=X^2-1` share the
root `-1`.  For `S=-X^2+X-1`, `A` does not divide `S` but `A` **does**
divide the inner factor of `T_Q(AB S)`.  The step “reduce modulo `A`,
hence `A|S`” is false.

**Counterexample, `A` not squarefree.**  `A=X^2(X-1)=X^3-X^2`, `B=X^2-2`.
For `S=X^2-X`, `A` does not divide `S` but `A` divides the inner factor.
The boxed Q statement must keep **both** squarefree and `gcd(A,B)=1`,
matching the already-required repair of the branch-Q `q1` theorem.

Characteristic `3` also kills the first (`AB`) step: `6=0` removes the
`A|Q` implication from `AB|T_Q`.  The campaign is `char 0`; it should
remain listed.

Q has no weight-two kernel through `D6`, so there is no Q analogue of
the `c2`/`A|V` collapse.  Sol does not invent one.

### 2.4 The “four/five-parameter endpoint” claim

**Verdict: REFUTED.**

The five P parameters and four Q parameters parametrize **only** the
simultaneous reduced-cascade `F1` plus `q1` locus (and, on P, the `c2≠0`
component collapses further to one parameter).  After that one still has,
through `D6` alone, `Z`, `T`, `F4,F5,F6`, and the free modes — dimensions
`63/60/61` on the reduced supports before any `q1` cut, still dozens of
parameters after it — and then `F7,...,F14` and `G_n` through the affine
target.  Section 1.36 (“compressed to four or five `q1` parameters before
exact solving”) and the novelty line “four/five-parameter endpoint
reduction” are false as endpoint statements.

Repair: *Card A reduces the `F1`/`q1` handle to five P parameters (or one
on `{A|V}`) and four Q parameters, and may delete a separate de Rham `q2`
gate on the reduced cascade.  It does not reduce the `D22=1` scheme to
four or five variables.*

The software paragraph is already the correct weaker claim (“reduces `F1`
to five P parameters/four Q parameters and deletes `q2` as a separate
gate”).  Promote that wording; discard the endpoint wording.

---

## Item 3 — Fixed-`H` `G_m` contraction

### 3.1 Weights and homogenization

**Verdict: CONFIRMED.**

The affine target is the frozen 734-generator system
`D0=...=D21=0`, `D22=1`, `D23=...=D34=0` (D5G35; `D35` is the zero row).
Replace `D22=1` by `D22=lambda`.  Assign every coefficient of `F_n` and of
`G_n` (`n>=1`) weight `n`, and assign `lambda` weight `22`.  `F_0=H^2` and
`G_0=H^3` are constants of weight `0` because `H` is fixed.

Each summand `(12-j)F_i' G_j` and `(i-8)F_i G_j'` of `D_n` has weight
`i+j=n`: differentiation in `X` does not change the jet weight.  Hence
every `D_n=0` is weighted homogeneous of weight `n`, and `D22-lambda` is
weighted homogeneous of weight `22`.  The scaling

```text
F_n |-> c^n F_n,    G_n |-> c^n G_n,    lambda |-> c^{22} lambda
```

preserves `I`.  Nonnegative weights make `c |-> 0` a morphism `A^1 ->`
ambient space, sending every point to the common-power origin
`(F_{>=1},G_{>=1},lambda)=0`.

Independently checked: for a numeric jet through weight `3` in `H=X^8-1`,
scaling by `c=3` multiplies each `D_n` by `3^n` for `n=0,...,6`.  `D0` is
identically zero on `(H^2,H^3)`, as it must be.

All weights are nonnegative.  There is no escaping to infinity along a
negative-weight coordinate; the action really does contract.

Presentation inconsistency, not a weight error: §4 of the charged source
puts `D23=...=D34=0` into `I`, while Card A first decides the endpoint
**before** `D23`.  Both ideals are weighted homogeneous, so the lemma
applies to either.  They are not the same test.  A coarse-`I` unit
certificate (through `D22` only) is a stronger exclusion than emptiness
of the 734-generator target; a coarse-`I` properness certificate is a
weaker existence claim and must still meet `D23`/`q1` and later rows.

### 3.2 Saturation and the `lambda=1` slice

**Verdict: CONFIRMED** with the field hypotheses named.

Let `S` be the polynomial ring in the positive-weight coefficients and
`lambda`, `I` the homogeneous ideal of the homogenized rows, and
`J=I:lambda^∞`.

**(a) `V(I)∩D(lambda)` nonempty as a scheme iff `J≠(1)`.**
`1 ∈ J` iff `lambda^N ∈ I` iff `lambda` is nilpotent in `S/I` iff
`(S/I)_lambda=0`.  No algebraic closure is required.  Sol lists an
algebraically closed characteristic-zero field; that is surplus for this
step (harmless).

**(b) Geometric points of `V(I)∩D(lambda)` vs the slice `lambda=1`.**
If `k` is algebraically closed and `char k` does not divide `22`, every
nonzero value of `lambda` is a 22nd power.  Scaling by a 22nd root of
`1/lambda` sends a geometric point with `lambda≠0` to a geometric point
of `D22=1`, and conversely every `D22=1` point is already such a point
with `lambda=1`.  Residual ambiguity is `μ_{22}` acting by
`F_n |-> ζ^n F_n` on the slice.  Existence over `k` is therefore
equivalent.  “Equality of the nonzero-lambda fiber with the target” is
slightly too strong (it is a `μ_{22}`-identification after a finite
étale base change), but the existence claim is correct.

Over `Q`, a proper `J` does **not** give a `Q`-point of `D22=1`.  Example
of the obstruction, even before Nullstellensatz: a `Q`-point with
`lambda=2` cannot be scaled to `lambda=1` over `Q`, because `2` is not a
22nd power in `Q`.  Card A’s PASS meaning correctly says “over an
algebraic closure.”

Saturating by `lambda`, not by the irrelevant ideal, is load-bearing.  The
homogeneous family `U=H+(V/2)t`, `F=U^2`, `G=U^3` has all `D_n=0` and
`D22=0`.  It makes **unsaturated** `I` proper whether or not the affine
target is empty.  `I:m^∞` keeps that `D22=0` cone.  `I:lambda^∞` kills
it unless it lies in the closure of `D(lambda)`.  A local standard basis
of `I` at the origin that is not `lambda`-saturated will PASS Card A
whenever the `D22=0` cone is present, which it always is.  That is the
practical form of the common error.

### 3.3 Localization and completion: the common error

**Verdict: CONFIRMED at fixed `H` for `J`.  REFUTED for the relative
parenthetical, for unsaturated `I`, and for completion at the origin of
a parameter space.**

Write `m=S_+`, the ideal of the common-power origin.

**Fixed `H`, so `S_0=k` a field, `J` homogeneous.**  A homogeneous ideal
of a positively graded `k`-algebra with `S_0=k` is the unit ideal iff it
contains `1` iff it is not contained in `m`.  Thus

```text
J ≠ (1)  iff  J ⊂ m  iff  J_m ≠ S_m.
```

For `(S_m, m S_m)` Noetherian local, completion is faithfully flat, so
`J_m = S_m` iff `Ĵ = Ŝ`.  Equivalently, the completed local ring of
`S/J` at `m` is the zero ring iff `J=(1)`.  Homogeneity also puts every
irreducible component of `V(J)` (over an algebraic closure) through the
origin, so the germ at `m` sees every component of the cone.  Combined
with §3.2(a), Sol’s three-line chain is **correct at fixed `H` for `J`**.

The parenthetical “or work relatively over its squarefree parameter
locus” drops `S_0=k`.  That is exactly the common error named in the
charge.

**Counterexample A (weight-zero parameter; completion at the total
origin).**
Let `k` be a field, `S=k[t,x,lambda]` with `deg t=0`, `deg x=1`,
`deg lambda=22`.  Let `I=(t-1)` (already `lambda`-saturated; homogeneous
of degree `0`).  Then `J=I` is proper, and `V(I)∩D(lambda)` is nonempty
(e.g. `(t,x,lambda)=(1,0,1)`).  Let `n=(t,x,lambda)` be the origin of
the **total** space.  Then `t-1 ∉ n`, so `J ⊄ n`, `J_n=S_n`, and the
`n`-adic completed extension is the unit ideal.  A proper homogeneous
`lambda`-saturated ideal has unit completion at that origin.

This is the relative situation: coefficients of `A` (or of `(A,B)`) are
weight zero.  Completing at the closed point where those coefficients
and all positive-weight variables vanish is completing at a degenerate
`H` (for monic `A=X^4+a_3 X^3+...+a_0`, the origin is `A=X^4`,
`H=X^8`), which is not even on the squarefree locus.  Components
supported on `A=X^4-1` are invisible there.

**Counterexample B (completion at one closed point of the zero section
misses other fibres).**
Same `I=(t-1)`.  The zero section of the grading is `V(x,lambda) ≅ Spec k[t]`.
The germ at the closed point `t=0` of that section is zero; the germ at
`t=1` is not.  Completing at a single closed point of the zero section
tests one fibre.

**Counterexample C (unsaturated `I`; the D5G client).**
Let `I` be the homogenization including `D22-lambda`.  The origin always
lies on `V(I)` (`lambda=0` and all positive coefficients zero; every
`D_n` vanishes there).  So `I` is always proper, and `Î_m` is always
proper, whether or not a `lambda≠0` point exists.  The homogeneous
`D22=0` family of §1.7 of the cascade producer is a concrete nonempty
subset of `V(I)∩V(lambda)`.  Testing properness of `I` or of `Î_m` cannot
decide the affine target.  One must saturate by `lambda` first.

The charged source writes `J=I:lambda^∞` and “`lambda`-saturated local
standard basis,” so it avoids Counterexample C in the lemma statement.
It invites Counterexample A by the relative parenthetical, and it invites
C in any implementation that completes `I` rather than `J`.

Sol’s converse phrase “a proper `lambda`-saturated ideal cannot have
`lambda` in its radical” is correct and is the reason `V(J)` cannot be
only the origin: if `rad(J)=m` then `lambda ∈ rad(J)`, hence `J=(1)` by
saturation.  That argument still needs `S_0=k` (or, relatively, that the
degree-zero piece of `J` is proper in `S_0`) to pass from “origin on
`V(J)`” back to “`J` proper.”

### 3.4 Exact corrected lemma and scope

**Lemma (positively graded, no parameters).**
Let `k` be a field and `S=k[x_1,...,x_n,lambda]` a positively graded
polynomial ring with `deg x_i >= 1`, `deg lambda=22`, and `S_0=k`.  Let
`m=S_+`.  Let `I ⊂ S` be homogeneous and `J=I:lambda^∞`.  Then the
following are equivalent:

1. `(S/I)_lambda ≠ 0` (i.e. `V(I)∩D(lambda)` is nonempty as a scheme).
2. `J ≠ (1)`.
3. `J ⊂ m`.
4. `J_m ≠ S_m`.
5. The `m`-adic completion satisfies `Ĵ ≠ Ŝ` (equivalently, the
   completed local ring of `S/J` at `m` is nonzero).

If `k` is algebraically closed and `char k` does not divide `22`, these
are also equivalent to:

6. `I+(lambda-1)` is a proper ideal of `S`.
7. `V(I)∩V(lambda-1)` is nonempty over `k`.

The implication `(2)<=> (3)` is elementary graded algebra (`S_0=k`), not
Nullstellensatz.  `(4)<=> (5)` is faithful flatness of completion of a
Noetherian local ring.  Geometric identification of (1) with the original
affine target `D22=1` uses a 22nd root of `lambda` and the residual
`μ_{22}`-action.

**Relative form (weight-zero parameters present).**
If `S_0=A` is not a field, replace (3)--(5) by: `J∩A` is a proper ideal
of `A`; equivalently `(J+S_+)/S_+` is proper in `A`; equivalently the
`S_+`-adic completion of `S/J` is a nonzero `A`-algebra.  Completing at a
**maximal** ideal of a closed point of the zero section `V(S_+)` tests
only the fibre over that point and is not equivalent to `J≠(1)`.

**Scope for the D5G client.**
The lemma decides nonemptiness of the **finite-type** homogenized raw
coefficient scheme at a **fixed** polynomial `H`, after `lambda`-saturation.
It does not:

- algebraize an arbitrary formal GGV germ to a polynomial map;
- detect a family of `H` if one completes at a single (in particular,
  degenerate) origin;
- decide `D22=1` from a local calculation of unsaturated `I`;
- supply GGV landing, a cofinal degree bound, coverage, a Keller pair,
  or JC2;
- by itself include or exclude `D23,...,D34`, which must be placed in
  `I` or imposed later, consistently.

Card A PASS/FAIL, read with this lemma at fixed `A=X^4-1` and with
`J` rather than `I`, are correctly stated as geometric existence /
unit-exclusion over an algebraic closure.  The dual-number thickening at
the cone is extra nonreduced structure through `D6`; every geometric
point of the full target still restricts to a reduced cascade point
through `D6`, so compression of `F1,F2,F3` does not change the binary
proper/unit test over an algebraically closed field.  It **does** change
the local ring, so a Kuranishi description of the germ after compression
is not the germ of the uncompressed scheme.  Section 8 argues for the
uncompressed germ, then Card A cheapens it by the reduced substitution.
Repair: use compression for the binary test and for reduced-point search;
do not advertise the compressed local ring as the scheme-theoretic
obstruction ring.

---

## Item 4 — Novelty and global consequences

### 4.1 Novelty

Repository searches (this session, excluding the `18:08Z` peer ideations)
for `q2=Z/16` and `D22=lambda` hit the charged source and the present
review prompt, plus an unrelated “`Z/16`” string in
`xmodel/ideation-20260824T1820Z-claude.md` that is not this identity.
The displayed `V=A'R+2AR'` form already occurs as the promoted
intersection basis `T_A(A^2 R)=A^2(2AR'+A'R)`.

| Claim | Adjudication | Closest hit |
|---|---|---|
| `q2=Z/16` on the cascade | `NEW CONNECTION` | Promoted `q2` formula; cascade `F2=(V^2+HZ)/4` |
| P five-parameter `V=A'R+2AR'` | `KNOWN` | Promoted `im T_A ∩ A^2`, dimension `5` |
| P `c2`/`A|V` collapse `R=cA`, `V=3cAA'` | `NEW CONNECTION` | Cascade row-five mode gate plus `q1` |
| Q four-parameter `Q=A^2BR` | `NEW CONNECTION` | Promoted `AB` intersection (dimension `7`), strengthened by cascade `H|F1` |
| Four/five-parameter endpoint | `SCOPE-CONFLICT` / false | The `63/60/61` reduced cascade dimensions |
| `D22=lambda` contraction client | `NEW MECHANISM AT D5G SCOPE` | Standard graded properness; AS/TD6 affine-Kuranishi work is a different client |
| General algebraic lemma as written, including the relative parenthetical | `KNOWN` mechanism, **incorrectly stated** relatively | Elementary graded algebra; Counterexamples A--C |

Sol’s own novelty paragraph already lists the `9,5,7` intersections as
found.  It should have classified the P five-parameter form as a rewrite
of that hit.  The Q four-parameter form, the `c2` collapse, `q2=Z/16`,
and the fixed-`H` `D22=lambda` client survive as new interfaces.

### 4.2 Landing, algebraization, coverage

The source does **not** treat a proper saturated germ as a GGV landing, a
family exclusion, a Keller pair, or JC2.  Bottleneck 1 remains universal
landing/coverage; Card A PASS still “then impose `D23`/`q1` and all later
rows”; the contraction paragraph explicitly denies that an arbitrary
formal GGV germ algebraizes to a global Keller map; K00 is scoped to
rank purity plus one compatibility ideal; lower FACEPIN is under
rollback.  Those firewalls are intact.

Two sentences are the residual hazard, not hidden hypotheses:

- §1, avenue 4: “At a **fixed face**, nonemptiness of the affine target
  is equivalent to nontriviality of a local saturated germ.”  Here
  “face” means the fixed-`H` D5G fixture, not a landed GGV family.  The
  word is unlucky in this campaign and should be replaced by “fixed `H`”
  / “fixed squarefree branch.”
- §8: “a local Kuranishi calculation can be globally decisive without a
  separate algebraization theorem.”  True only as: *for this finite-type
  homogeneous scheme at fixed `H`, the `lambda`-saturated germ at the
  origin decides geometric nonemptiness of `D22=1`*.  It is not a
  substitute for algebraization of unbounded series, and it is not
  global in the GGV/coverage sense.

No charged existence or exclusion accidentally consumes GGV landing,
algebraization of infinite jets, or a coverage theorem.  The q-compressions
are conditional on the reduced cascade and on the promoted `q1`/`q2`
formulas (themselves conditional on R7R1 and on `D23`/`D24` as gates).
That dependency tree is written down and is not a landing assumption.

---

## Maximum licensed claim

After this review, the following may be used as ideation, still not as
promoted theorems:

1. On reduced field points of the reviewed squarefree (coprime) cascade,
   `q2=Z/16` identically, hence the de Rham `q2` gate is automatic there.
   Characteristic not `2`.  No `D24` implication.  No nonreduced-scheme
   implication.
2. On that same reduced P locus, `q1` is `V=A'R+2AR'`, `deg R<=4`.  This
   is the promoted dimension-`5` intersection in cascade coordinates.  On
   the `A|V` component, with squarefree `A`, it collapses to
   `V=3c AA'`.
3. On the reduced Q locus, with both squarefree and coprime, `q1` is
   `V=2A'BR+3AB'R+4ABR'`, `deg R<=3`.
4. At **fixed** `H`, the homogenized `D22=lambda` scheme, after
   `lambda`-saturation, has geometric points over an algebraic closure of
   characteristic not dividing `22` if and only if the completed local
   ring of `J` at the common-power origin is nonzero.  This is a
   finite-type graded fact.  It is not relative in `H` if one completes
   at a single origin, and it is not a GGV/algebraization/coverage
   theorem.

Explicitly not licensed: any four/five-parameter description of the
affine endpoint; any `q2` cut of `F1`; any unit/properness certificate
taken from unsaturated `I` or from a relative completion at `H=0`; any
Card A run that mixes free `c2` with all five `R` parameters; any
inference of landing, a Keller pair, or JC2.

---

## Ledger

*What I proved by hand:* the identity `4H^2 F2-F1^2=H^3 Z`; residue of a
polynomial differential at infinity; `T_A(A^2 R)` and `T_Q(A^2 B R)`
expansions; forced degree bounds `deg R<=4` (P) and `deg R<=3` (Q); the
squarefree implication `A|V => A|R`; the extra-`A` reduction of `T_Q`
modulo `A`; weighted homogeneity of `D_n` and of `D22-lambda`; scheme-
theoretic saturation `(S/I)_lambda=0 iff J=(1)`; elementary equivalence
of proper homogeneous ideals with `J ⊂ m` when `S_0=k`; Counterexamples
A--C; `μ_{22}` versus 22nd-root normalization.

*What is script-only (exact rational arithmetic, no CAS):* `q2` identity
on three `H`; `T_A`/`T_Q` expansions; P grid `A|V iff A|R` on `A=X^4-1`
(`3125` polynomials); special-branch `V=3c AA'`; Q coprime grid
`A|inner iff A|S` (`625` polynomials) and injectivity of `R |-> V`;
degree table `deg T_A(A^2 X^d)`, `deg T_Q(A^2 B X^d)`; `D_n` scaling by
`c=3` through weight `6`; the two degeneration counterexamples
`A=X^2(X-1)^2` and `(A,B)=(X^3+1,X^2-1)`.

*What I did not do:* compute any saturated local standard basis; inspect
`jc2-lean`; read peer `18:08Z` ideations; launch AWS; edit any other
campaign file.

Firewall: no face exclusion, landing, Keller pair, counterexample, or JC2
conclusion is inferred.

---

**Review verdict:** `q2=Z/16` and the Q four-parameter `q1` form, plus the
P `c2` collapse, are desk-correct on the reduced squarefree (coprime)
cascade and are new as interfaces; the P five-parameter form is the
promoted dimension-`5` intersection rewritten; the “four/five-parameter
endpoint” is false.  The contracting-`G_m` lemma is correct at fixed `H`
for the **lambda-saturated** homogeneous ideal, and false as soon as
weight-zero parameters remain or one completes unsaturated `I`.  No
global landing/algebraization/coverage theorem is smuggled in.

---

## Report SHA-256

Self-referential stamps cannot hash themselves, so this is the SHA-256 of the
report **body**: the first 729 lines (through the review-verdict paragraph),
i.e. the file as written before this stamp block was appended.

```text
6826e3522692415db3eb712c9b7d47b19ce1b6ed0a45cfe0f68f24dc88bb6c5a
```

Reproduce with:

```bash
head -n 729 xmodel/ideation-20260827T1808Z-sol-hostile-review-grok46.md \
  | shasum -a 256
```

Exact model identity: Grok 4.6, CLI `grok 1.0.5 (5115b46bc909)`,
Python 3.14.6, Darwin arm64.

Checks run: live SHA-256 of the charged Sol writeup and packet (both matched
the freeze pins); rehash of the cascade producer, Fable5 cascade review,
and the two promoted `q`-gate reviews; hand expansion of `q2`, `T_A(A^2 R)`,
`T_Q(A^2 B R)`, the extra-`A` reduction, the `c2`/`A|V` collapse, `D_n`
weights, saturation, and the graded completion lemma; exact
`fractions.Fraction` polynomial grids for those identities and for the
squarefree/coprime counterexamples; novelty `rg` for `q2=Z/16` and
`D22=lambda`.  No Gröbner computation, no AWS, no heavy local algebra.

Scope firewall: this report is the only campaign file written.  `jc2-lean`
was not entered, read, built, status-inspected, or touched.  Peer
`18:08Z` ideations were not read.  No face exclusion, landing, Keller pair,
counterexample, or JC2 conclusion is inferred.
