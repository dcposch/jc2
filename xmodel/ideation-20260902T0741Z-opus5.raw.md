# Blind ideation — round 20260902T0741Z — Opus 5

Lane: `ideation-20260902T0741Z-opus5`. Date: 2026-09-02. Agent: Opus 5.
Charged input: `xmodel/ideation-20260902T0741Z-packet.md`,
SHA-256 `2646ac692c292c30597f9c830fd145c85e020207d803927825b8a162086055cf`
(verified against the frozen read-only copy before it was read).
Basis `8939320bc8c91a5a7b79eb30537e89e8c4a10333`.

Sources consumed: the packet; `APPROACHES.md`; `notes.md` (LIVE STATE
band 2026-09-01); `xmodel/integration8-coordinator-fable5-20260902.md`;
`xmodel/horn-flagship-opus5-20260902.md`;
`xmodel/ray-kill-opus5-20260902.md`;
`xmodel/cell-32-termination-opus5-20260901.md`;
`xmodel/mprime-alln-h2-opus5-20260902.md`;
`xmodel/companion-curve-alln-opus5-20260902.md`;
`refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf` (own
`pdftotext -layout` extraction, read directly). No round-20260902T0741Z
submission by any other lane was opened; `ls` output listing their
filenames was seen and nothing was read.

No `charge_basis` line: this report asserts no new exit price.

Desk work only. One PDF extraction, no CAS, no AWS, no `jc2-lean`,
no canonical ledger touched.

## 1. Verdict, up front

```text
(1) THE ROUND'S FIND -- an index failure, not a mathematics gap.
    OPEN[DEG-AF-VS-N], named by BOTH H2-branch flagships as the single
    highest-value successor and by MPRIME as "could not find it promoted
    anywhere in the record", is answered -- in the form the delta-budget
    needs -- by Chau Thm 1/Cor 1/Cor 2, banked and machine-corrected on
    the REDUCIBLE branch the same day (COMPANION clauses C6/C7/C8 and its
    derived M <= K).  Under H2: A_F is a polynomial image of bidegree
    (Md,Me) with ONE place at infinity, deg A_F = M max(d,e), and
    deg A_F <= max(deg P, deg Q).  Sec 3.
(2) AND THE SUBSTITUTION WAS NEVER MADE.  At the (9,6) degree pair the
    cap is saturated by D_1 alone (deg D_1 = 9 = max(9,6)), so no
    companion of any degree fits: OPEN[COMPANION-R0-REALISATION] looks
    decided NEGATIVE at (9,6,2) by arithmetic.  CLAIM [D], three named
    checks, Sec 3.3.
(3) STRUCTURAL DIAGNOSIS (gap (e)).  Every H2 closure is the SAME
    inequality  a-1 <= C*(2a-N)  with both sides linear in N; a constant
    decides and the window is an interval.  Bounded-N architecture can
    therefore never finish alone.  I name the one candidate second
    inequality: the counting degrades exactly as a -> N-2, which is
    exactly where the covering instruments (ORBIFOLD-CAGE, CENTRAL-RANK,
    HC-1 r(E)<=a, B3-COMPONENT) get stronger, because E is then a
    high-degree cover of a rational one-place curve inside C^2.
    AVENUE ANTI-MONOTONE, Sec 4.2.
(4) OPEN[A2-U-BOUND] IS THE WRONG TARGET.  RAY-KILL (C5) proves there is
    no Z-scaling covariance, so the symmetry that would bound U is
    provably absent.  What is needed is a DEPTH bound: truncate to the
    top k coefficients and the system's size becomes independent of U
    while its coefficients stay POLYNOMIAL in U (CELL-32 Sec 1's Euler
    eigenvalues are linear in the degree indices).  One Groebner basis
    over Q(U) then decides all but finitely many U.  RETYPE ->
    OPEN[A2-DEPTH-BOUND] + MECHANISM PARAM-U, Sec 5.
(5) GAP (l), ANSWERED: NO.  The full cell system carries ~3 surplus
    equations per order (RAY-KILL Sec 4's own table, excess ~5U/2+5e);
    the observed 4-conditions-on-5-unknowns deficit is a top-of-ladder
    artefact, because equations switch on at staggered depths.  Expect
    the rank jump at depth O(e), not O(U).  Not a family signal.
(6) COUNTEREXAMPLE SIDE REORDERED.  Not the A2 ray, not an N>=6 census:
    the (B3) N=4 survivor, which Chau now makes explicit down to
    DEGREES.  Sec 7.3; both outcomes advance the campaign.
```

## 2. Challenge to the coordinator's framing

**(i) The list is organised by object; the failure mode is organised by
index.** THEOREM PROFILE's own proof enumerates
`a-1 <= (R_max(W)+beta)(2a-N)` under `N/2 < a <= N-2` and reads off
"`beta>=2` for `5..10`, `>=1` for `11..16`, `0` for `N>=17`" — one
linear-vs-linear comparison whose slack grows. `SMOOTH-KILL` and
`CUSP-A-EMPTY` are the only items not of this shape. Gap (e) is
therefore not the fifth proof-side item; it *is* the list. Raised to #1
structural.

**(ii) Gap (k) is mis-posed and should be retired as written.** RAY-KILL
Sec 6 already established that the A2 residual and the `(B3)` group cage
"act on different objects and do not compose", and that a ray kill closes
**zero** `(B3)` windows. The A2 lane is the `A`-degree-two mate problem
(APPROACHES row 29's descendant) — statements about `C[Z]` polynomials
`eta,s,q,r,G` — not a monodromy cage on `pi_1(C^2\A_F)`. The bridge that
actually exists runs COMPANION (Chau data) -> H2 (delta-budget), and
Sec 3 uses it.

**(iii) "One theorem away" miscounts the A2 side.** `U` is unpinned
precisely because `Z`-isobarity fails (RAY-KILL C5: `kappa`'s weight is
forced to be both `2` and `1`). Asking for a `U`-bound is working against
a proven absence of symmetry. Sec 5 goes around it.

What the framing gets right, and I reinforce: "H2 complete at every
degree" is REFUTED/overpromoted. Nothing below weakens that — `(B2)` and
`(B3)` stay open at `5<=N<=16`, `(B1)` at `N>=17`, case `(A)` at `N>=8`.

## 3. NEW CROSS-CONNECTION: the reducible branch already holds the H2 branch's top successor

### 3.1 The collision

`HORN-FLAGSHIP` Sec 5 ranks `OPEN[DEG-AF-VS-N]` first among "what would
compose", because the `(B3)` delta-budget
`delta(p,q) + sum_i t_i + delta_infty = (n-1)(n-2)/2`, `n = deg closure(A_F)`,
"is a budget, not a bound, because `OPEN[DEG-AF-VS-N]` is open"
(`horn-flagship-opus5-20260902.md:369`). `MPRIME-ALLN-H2:682` repeats it
for `(B2)` — "a bound `n <= f(N)` converts directly into a bound on
`beta`" — and adds "I could not find it promoted anywhere in the record".

It is in the record, on the other branch, from the same day and the same
producer model. `COMPANION-CURVE-ALLN` banks from
`refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf`:

```text
 C6  deg a_i = m_i d, deg b_i = m_i e, gcd(d,e)=1, the SAME (d,e) for
     every component, deg D_i = m_i max(d,e), max(d,e) >= 2. [Chau Thm 1]
 C7  one shared leading invariant B^d/A^e for the whole map.
 C8  every component meets L_inf at one point, one place, tangentially.
                                                        [Chau Cor 2]
 :682-687 (derived there)  M <= K = deg P/d,  hence
     sum_i deg D_i <= max(deg P, deg Q).
```

I re-derived `M <= K` independently before finding it (`deg_u Res <= Ke`,
`deg_v Res <= Kd` for `Res_y(P-u,Q-v)`, against the leading form
`(B^d u^e - A^e v^d)^M` of `R_0`), so Sec 3 is a **reproduction with a
transfer**, not a new theorem. The transfer is the point:

```text
 Under H2 (A_F irreducible) the banked clauses read:
   (CHAU-N)  n = M max(d,e);  A_F = image of xi |-> (a,b) of bidegree
             (Md, Me); ONE place at infinity;  n <= max(deg P, deg Q).
```

### 3.2 What that buys, and what it does not

It does **not** bound `n` by the geometric degree `N`: `deg P * deg Q >= N`
runs the wrong way and the surplus hides at infinity. Honest retype:

```text
 OPEN[DEG-AF-VS-N]  RETYPE -> (i) OPEN[DEG-AF-CHAU]: ANSWERED (banked,
   cross-branch) -- n = M max(d,e), bidegree (Md,Me), one place at
   infinity, M <= K.   (ii) OPEN[N-VS-MAPDEG]: is max(deg P,deg Q)
   bounded by N at the reduced representative?  Different question,
   plausibly false, and the delta-budget does NOT need it.
```

The budget needs `n` and `delta_infty`, and `(CHAU-N)` gives both as
functions of `(M,d,e)`: `n` directly, and `delta_infty` because `C8`
makes the branch at infinity a single place with Newton-Puiseux exponent
`d/e`, so its `delta` is the semigroup `delta` of that place. **Computing
`delta_infty(M,d,e)` in closed form is the cheapest promotable item this
round produces** (Card 1). Consequences:

```text
 (B2), 5..16 : sum_Sing delta_q = (n-1)(n-2)/2 - delta_infty(M,d,e) with
   n = M max(d,e).  beta counts singular branches, each costing delta>=1
   above a node, so any (M,d,e) bound gives a beta bound -- exactly the
   implication MPRIME:682 asks for.  Twelve degrees at once.
 (B3), N=4   : the budget confines (p,q) (already congruence-restricted
   by HF Prop 3.2) and k to a FINITE list per (M,d,e).  "Rigid not
   empty" becomes enumerable -- the first time the object can be either
   exhausted or exhibited.
```

### 3.3 A consequence nobody substituted into

Take the campaign's own `(9,6)` row: `deg P = 9`, `deg Q = 6`, so
`K = gcd(9,6) = 3`, `(d,e) = (3,2)`, `max(d,e) = 3`. COMPANION `:371-379`
records, machine-verified, that the realised `(9,6,2)` component `D_1`
has `deg D_1 = 9` and weighted-leading form exactly `(u^2-v^3)^3`,
i.e. `m_1 = 3`. Then

```text
   cap:  sum_i deg D_i <= max(deg P,deg Q) = 9 ;   deg D_1 = 9 already.
   ==>   deg D_2 <= 0 for every companion.  Equivalently M >= 3+1 > 3 = K.
```

```text
CLAIM [D], UNREVIEWED, cheap to check.  At (9,6) the Chau cap is
SATURATED BY D_1 ALONE, so no Keller map of bidegree (9,6) has a
reducible A_F containing the realised (9,6,2) component:
OPEN[COMPANION-R0-REALISATION] is decided NEGATIVE at (9,6,2) by
substitution into a banked inequality.  COMPANION SS7 typed
M = M_1+M_2 <= K as "the exact currency" and did not evaluate it on its
own witness.
```

Three checks before promotion, flagged rather than assumed: **(a)**
additivity — `R_0 = c prod_i f_i^{a_i}`, `a_i >= 1`, and the weighted-
leading form of a product is the product of the forms, so
`M = sum a_i m_i >= sum m_i`; write this out. **(b)** `m_1 = 3` must be a
property of the numerical *type* (`deg D_1 = 9` plus `C6`), not of the
realisation. **(c)** Chau's normalisation (`P,Q` monic in `y`; a generic
linear change alters neither degrees nor `A_F`) and `deg_x Res = N`,
consumed at his typing.

If (a)-(c) hold, this is also a **general reducible-branch razor**:
`sum_i deg D_i <= max(deg P, deg Q)` is checkable on every numerical type
the census emits, as a one-line prefilter in front of the most expensive
instrument the campaign runs.

## 4. The all-degree ceiling (gap (e)), and a candidate second inequality

### 4.1 Why every H2 closure is an interval

Restating `H2` precisely, as the packet asks: `A_F` is Jelonek's
non-properness set of the Keller map `F`, a curve, nonempty iff `F` is
not an automorphism; `(H2)` is "`A_F` irreducible", and its complement is
the reducible branch. The two are not symmetric: under `H2`, Chau
`C7`/`C8` force one place at infinity on one curve, whereas reducibility
forces several components through one point with the same `(d,e)` — which
is why Lemma CONTACT bites there and has no `H2` analogue.

Every `THEOREM PROFILE` bound is `a-1 <= (R_max(W)+beta)(2a-N)` with
`N/2 < a <= N-2`: left side linear in `a`, right side linear with slope
`2C`. For `C >= 1` it is eventually satisfiable; the window closes only
while `C` is too small. So bounded-`N` architecture can only ever produce
intervals `[3, f(C)]`, and `C` is a local invariant with no reason to
shrink. Answering the packet directly: **no**, it cannot finish without a
second inequality of opposite monotonicity in the same variable.

### 4.2 NEW AVENUE — ANTI-MONOTONE: run the covering cage on the same `(N,a)` grid

The counting fails exactly when `a -> N-2`, i.e. `D_gap` large. That is
precisely the regime in which the cusp/homology instruments are
strongest, because they are statements about `E = F^{-1}(A_F)`, a degree-
`a` cover of a rational curve with one place at infinity:

```text
  HC-1        r(E) <= a                    grows with a
  CENTRAL-RANK r = j - 1                   pins j from r
  ORBIFOLD-CAGE s + s' = M + 2 - j         couples j to the local data
  B3-COMPONENT j = orbit count of the (2.5.1) monodromy
  B3-N4        E's genus and place count from the puncture signs
```

and, crucially, `E` is an **affine plane curve**: it embeds in `C^2`, and
by `(CHAU-M)` applied to `F` its degree is capped. A degree-`a` cover of
a rational one-place curve, branched only over the `<= s` singular points
and infinity, has genus growing with `a` by Riemann-Hurwitz; but a curve
of bounded degree in `C^2` has genus bounded by `(deg-1)(deg-2)/2`. Two
bounds on the same `g(E)`, one increasing in `a` and one capped.

```text
AVENUE ANTI-MONOTONE.  For each N, tabulate
   (i)  the counting-admissible a-range from THEOREM PROFILE, and
   (ii) the covering-admissible a-range from Riemann-Hurwitz on
        E -> A_F together with the genus cap from deg E <= (a bound
        via CHAU-M and deg F).
   A crossing at some N would be the campaign's FIRST degree-monotone
   obstruction.  If the ranges never cross, the tabulation says so
   explicitly and the ceiling question is answered NEGATIVELY, which is
   also information the campaign does not have.
```

Cheapest discriminator: a spreadsheet, not a CAS. `N = 4..20`,
`a in (N/2, N-2]`, `W >= 2`, the `(K)`/`(L)`/`[P3]` data from MI. It is
an afternoon of desk work and it either produces the missing invariant
or retires the hope, and either outcome is worth more than another
bounded window.

*Honest limit.* I have not verified that the genus cap on `E` is
effective — the branching data of `E -> A_F` at infinity is exactly
`OPEN[B3-INFINITY-RANK]`, which HF left open, and without it the
Riemann-Hurwitz side is a floor with an unpinned correction. So this is
an avenue with one named dependency, not a proof sketch.

## 5. NEW MECHANISM — PARAM-U: decide the A2 cells for all large `U` at once

### 5.1 The reframing

`OPEN[A2-U-BOUND]` asks for `U <= f(e)`. Two reasons to go around it:
RAY-KILL `(C5)` proves there is **no** `Z`-scaling covariance (the
`kappa`-weight is forced to be both `2` and `1`), so the natural
isobaric argument that would bound `U` is provably unavailable; and a
bound is not what the computation needs.

What the computation needs is a **depth** bound. Write `Lad_k` for the
system obtained by keeping, from each residual equation
(`EQ1..EQ4, E0, T1`), only its top `k+1` coefficient equations in `Z`.
Then:

* `Lad_k` is a **necessary** condition: cell nonempty `=>` `Lad_k`
  solvable. So `Lad_k` unit ideal `=>` cell EMPTY.
* `Lad_k` has `5(k+1) + O(1)` unknowns
  (`eta_{e-i}, s_{sigma-i}, q_{m-i}, r_{n-i}, G_{2e-i}`, `i <= k`) and
  `6(k+1)` equations — **both independent of `U`**, once `k < min(n, m, sigma)`.
* Its coefficients are **polynomial in `U`**. This is not an assumption:
  CELL-32 Sec 1 computes every leader by an Euler-operator eigenvalue
  *linear* in the degree indices (`deg M(Y) = e+k` with leader
  `eta_e Y_k (2k-1-4e)`, etc.), and on the wall `m = U`, `n = U-e`,
  `2 sigma = U+e`.

```text
MECHANISM PARAM-U.  Treat U as a symbolic parameter and compute a
Groebner basis of Lad_k over Q(a,b,U) (or Q(U) after S1,S2).  If it is
the unit ideal, then Lad_k is unit for all but the finitely many U in
the zero set of the product of the pivots' denominators/leading
coefficients -- an explicit finite list, each member decided by the
per-cell CAS the campaign is ALREADY running on box01.
Result: the E1-wall is EMPTY for all U, with NO bound on U.
```

`OPEN[A2-U-BOUND]` is then RETYPED as

```text
OPEN[A2-DEPTH-BOUND].  Find k* = k*(e) with Lad_{k*} unit over Q(U).
```

which is a *finite* search in `k`, bounded below by RAY-KILL's own data
(`k = 1` gives rank `<= 3` on `5` unknowns, `k = 2` adds nothing for
`e <= 5`, so `k* >= 3`).

### 5.2 Why `k*` should exist, and why the ladder's failure so far proves nothing (gap (l))

RAY-KILL Sec 4's own size table is the argument. Per cell,
`equations - unknowns ~ 5U/2 + 5e`, i.e. **~3 surplus equations per
order of `Z`** averaged over the whole polynomial. But the top-of-ladder
count is `4` conditions against `5` unknowns — a *deficit* of 1. Both are
correct: near the top most equations have not yet contributed, because
their own top coefficients sit lower (an equation of total degree
`D_i < D_max` contributes nothing at orders above `D_i`). The deficit
must therefore turn into a surplus after a number of orders set by the
spread of the equations' degrees, which is `O(e)` and `O(1)` in `U`, not
`O(U)`.

**This answers gap (l): NO.** The non-termination of the ladder at
orders `top-1` and `top-2` is the expected behaviour of a system whose
equations switch on at staggered depths. It is not evidence that the
residual is a genuine family and it should not be read as a positive-side
signal. Gap (h) is lowered on the same ground.

### 5.3 The decisive experiment, on data that already exists

`(1,3)`, `(1,5)`, `(1,7)` and `(2,6)` are DECIDED EMPTY. Nobody recorded
*at what depth* they became empty.

```text
EXPERIMENT DEPTH-PROFILE.  For each decided cell, compute the minimal k
with Lad_k the unit ideal.  Cost: k Groebner bases on <= 5(k+1)+2
variables -- seconds to minutes each, far cheaper than the full cell.
READ-OUT:
  k* bounded and equal across cells of the same e   -> PARAM-U applies;
        run it, and OPEN[A2-U-BOUND] is retired without ever being proved.
  k* growing with U                                 -> PARAM-U fails, and
        the growth rate is itself the first quantitative statement about
        the residual anyone has.
  k* undefined (no k gives unit; emptiness only from the full system)
                                                    -> the leading-order
        programme is the wrong instrument; say so and stop the ladder.
```

All three outcomes are worth having, and the experiment costs less than
one cell of the window currently running on box01.

## 6. Disposition vectors

### 6.1 APPROACHES.md master union table — CHANGES ONLY

| Row | Change | Reason |
|---|---|---|
| 6 Abhyankar-Moh one-place | **RETYPE + RAISE** (was "tried on the wrong object", category error) | The category error is repaired by Chau. `A_F` *is* a curve with one place at infinity (Chau Cor 2 + MI Lemma A), and its place data are now pinned (`(Md,Me)`, exponent `d/e`), which is exactly the row's stated blocker ("place data are unpinned"). AM/Suzuki semigroup theory applies to `A_F` directly. |
| 7 Nonproperness / Jelonek `A(F)` | **RAISE to top-3** (was Partial, "`A(F)` never constructed") | The whole H2 branch is now a structure theory of `A(F)`; THEOREM PROFILE classifies its singularities at every `N`; Chau parametrises it. The DISSENT (S:8 "construct asymptotic values" vs G "not cheaper than rebuilding the compactification") resolves in S's favour: it was constructed, twice, and it is cheaper. |
| 25 Fiber monodromy / passports | **RAISE**, status change | S's requested "coupled two-coordinate branch-cycle CSP" (S:7) exists: realisation -> SIROCCO -> ZvK -> `S_N`, validated end-to-end and delivering two curve-level kills. Row status "no kill" is stale. |
| 26 Primitive monodromy / block bound | **RAISE slightly** | `SOURCE-OPEN-U`/`SG-1` is this row's live descendant; `d2=2` successor still exact. |
| 27 Links at infinity / splice | **RAISE** | HF names "a route through the ends" of `E` as successor #2 for the `(B3)` `CUSP-KILL` replacement; that is this row, on a newly pinned object. |
| 29 LND / mate problem | **RETYPE** (no rank change) | The A2/CELL-32 lane is this row's active instance; the row's text does not say so and should. |
| 36 Guided CE search | **RAISE** (was G:2 "worthwhile only as a GGV bug-hunt") | For the first time the CE side has an object with pinned DEGREES (Sec 7.2), so the search is structured, not random. G's objection ("CEs form a thin locus in an enormous space") does not apply to a bidegree-`(Md,Me)` parametrisation search. |
| 19 char-p / Witt | **LOWER** | Packet types it orthogonal at a bounded degree-12 frontier; no Opus seat should be spent while (B2)/(B3) are open. |
| 46 Lean / formal certification | **LOWER** | DC standing: formalization non-blocking. |

No other row changes. Rows 11, 18, 41, 44 stay closed; rows 1-4 stay at
their overlay typings.

### 6.2 Gaps (a)-(l)

| Gap | Disposition | Reason |
|---|---|---|
| (a) `A2-U-BOUND` | **RETYPE** -> `OPEN[A2-DEPTH-BOUND]` + PARAM-U | Sec 5. A `U`-bound is neither necessary nor supported by an available symmetry (`C5` kills `Z`-isobarity). |
| (b) `(B3)` cage 4..16 | **RAISE**, reframe | Sec 3.2: the binding sub-gap is the delta-budget, now closed-form in `(M,d,e)`, not a `CUSP-KILL` replacement. `N=4` becomes an enumerable list. |
| (c) `HOMCOVER-CUSP-A-N8` | **LOWER in priority, unchanged in validity** | Case `(A)` is necessary at `N>=8` but never binding-first: at every `N>=8` where `(A)` is open, `(B3)` and `(B2)` are open too, and they are cheaper. Let the running lane finish; do not reseat. |
| (d) `(B2)` 5..16 | **RAISE to cheapest H2 kill** | MPRIME `:682` states the implication `n<=f(N) => beta` bound explicitly; Sec 3 supplies `n = M max(d,e)` and `delta_infty`. Twelve degrees at once. |
| (e) all-degree ceiling | **RAISE to #1 structural** | Sec 4.1: it is not one gap among five, it is the shape of all of them. New mechanism in Sec 4.2. |
| (f) companion `R0` / degree-cap | **RAISE**, and possibly decidable today | Sec 3.3 CLAIM: the cap is saturated by `D_1` alone at `(9,6)`. The general razor `sum deg D_i <= max(deg P, deg Q)` should be a prefilter on every census type. |
| (g) `N>=6` census | **LOWER as a first move**, keep alive | At `N>=6` the profile does not pin the object; a census there is unguided. Reorder behind (i). |
| (h) A2 infinite-`U` as construction target | **LOWER** | Sec 5.2: the non-termination is a top-of-ladder artefact, not a family signal. |
| (i) `(B3)` `N=4` survivor as construction target | **RAISE to #1 on the CE side** | Sec 7.2. Fully pinned representation + Chau bidegree = a small explicit search. |
| (j) char-p / Witt | **LOWER / park** | As row 19. |
| (k) A2 <-> `(B3)` bridge | **CLOSE AS POSED; REPLACE** | RAY-KILL Sec 6 already proved they do not compose. Replace with COMPANION(Chau) <-> H2(delta-budget), which is real and used in Sec 3. |
| (l) non-termination as positive signal | **ANSWERED: NO** | Sec 5.2, from RAY-KILL's own size table. |

## 7. Reranked bottlenecks, and the two strongest attacks

### 7.1 Proof-side bottlenecks (reranked)

```text
 1. delta-BUDGET CLOSURE.  Compute delta_infty(M,d,e) in closed form and
    substitute into (n-1)(n-2)/2.  Closes: a beta-bound for (B2) at
    5..16; a finite (p,q),k list for (B3) at N=4.  Cost: desk.
    [was: OPEN[DEG-AF-VS-N], ranked #1 by HF -- same slot, now reachable]
 2. THE CEILING.  ANTI-MONOTONE (Sec 4.2).  The only route to an
    unbounded-N obstruction anyone has named.
 3. A2 DEPTH-PROFILE + PARAM-U (Sec 5).  Retires the horn's analytic
    residual without a U-bound.
 4. (B3) CUSP-KILL REPLACEMENT through the ends of E (HF successor 2;
    APPROACHES row 27).  Needs OPEN[B3-INFINITY-RANK].
 5. CASE (A) N >= 8 GATE.  Necessary, not binding-first.
 6. (B1) at N >= 17.  Do not start until 1-3 are done: it is the only
    region where a bounded-N method is provably useless.
```

### 7.2 STRONGEST PROOF ATTACK

**Close `(B2)` for `5 <= N <= 16` by the Chau delta-budget.** It is the
largest single block of degrees any one instrument can take, it needs no
new theory, and every input is banked:

1. `delta_infty(M,d,e)`: the place at infinity of a curve parametrised
   with bidegree `(Md,Me)`, `gcd(d,e)=1`, is a one-place branch whose
   semigroup is generated by `M min(d,e)` and `M max(d,e)` plus the
   Puiseux data; write its `delta` in closed form. Desk, one page.
2. Substitute into `sum_{Sing} delta_q = (n-1)(n-2)/2 - delta_infty`,
   `n = M max(d,e)`.
3. `beta` counts singular branches at multibranch points; each costs
   `delta >= 1` above a node, so `beta <=` the residual budget.
4. Compare with MPRIME Sec 6's enumeration: `beta >= 2` required for
   `5..10`, `beta >= 1` for `11..16`. Any budget bound below those kills
   the window.
5. **Stop condition:** if step 4's budget exceeds `2` for some `(M,d,e)`
   admissible at that `N`, the window survives and the residual is the
   explicit `(M,d,e)` list — still a strict improvement, because the
   list is finite and each entry is a concrete curve-existence question.

### 7.3 STRONGEST COUNTEREXAMPLE / FALSIFICATION ATTACK

**Build the `(B3)` `N=4` object as a Chau parametrisation.** It is now
specified down to degrees:

```text
 seek   xi |-> (a(xi), b(xi)),   deg a = Md, deg b = Me, gcd(d,e)=1,
        max(d,e) >= 2,  M <= K = gcd(deg P, deg Q),
 image  A_F, rational, ONE place at infinity, with
        exactly one quasi-homogeneous cusp (p,q), (2|p,3|q) or (3|p,2|q)
                                                     [HF Prop 3.2]
        plus k double points of contacts t_i,
        delta(p,q) + sum_i t_i + delta_infty = (n-1)(n-2)/2, n = M max(d,e)
 then   rho(G) = S_4 pinned [HF Prop 3.1]; E = F^{-1}(A_F) of genus
        k_odd - 1 with 3 + 4k - 2k_odd places at infinity [THEOREM B3-N4].
```

The smallest admitted cusp is `(p,q) = (2,3)`. With `(d,e) = (3,2)`,
`M = 1`, `n = 3`: a cuspidal cubic has `delta = 1` and the budget is
`(3-1)(3-2)/2 = 1`, so `delta_infty = 0` and `k = 0` — which is case
`(A)`, already EMPTY. So `(B3)` at `N=4` forces `n >= 4` and the search
starts at `M max(d,e) = 4`. **That is a two-parameter family of
polynomial pairs of degree `<= 6` each.** It is exhaustible.

* **Outcome NONEMPTY** (a parametrisation with the right singularities
  exists): hand it straight to the validated realisation -> SIROCCO ->
  ZvK -> `S_N` pipeline, which killed `(9,6,2)` and `(9,6,4)`. Either it
  kills this one too — and `(B3)` `N=4` closes by exhaustion — or it does
  not, and the campaign has its first object that survives past
  representation level, which nothing has ever done.
* **Outcome EMPTY** at every admitted `(M,d,e)`: `(B3)` at `N=4` is EMPTY,
  and with `CUSP-A-EMPTY` and `THEOREM PROFILE` the `N=4` `H2` branch
  closes without any `CUSP-KILL` replacement.
* **Stop condition:** if the budget admits `n` beyond `12`, stop and
  report the list; the search is no longer exhaustive and the value is
  in the list, not the sweep.

**Expected information gain:** high in both directions, and this is the
rare item where EMPTY and NONEMPTY are *both* campaign-advancing.

## 8. Software acceleration / decisive experiment, and a systems UPGRADE

### 8.1 Acceleration: `PARAM-U` as a generic-parameter Groebner driver

The campaign's default stack (`qqideal` + `msolve 0.10.1`) is a
*ground-field* stack: it decides one cell at a time over `Q`. The A2
window on box01 is therefore linear in the number of cells and infinite
in `U`. `PARAM-U` needs one capability the stack does not currently
exercise: **Groebner over `Q(U)`** (or over `Q` with `U` adjoined and the
result saturated at the pivot denominators). Two routes, both cheap:

* `Singular`/`M2` over `QQ(U)` directly on `Lad_k` (tiny systems:
  `<= 5(k+1)+2` variables);
* or, engine-agnostic and safer: compute `Lad_k` over `Q` at `~20`
  integer values of `U` in the admissible congruence class, confirm unit
  ideal at all of them, then run once over `Q(U)` to promote. The
  integer runs are the positive/negative controls FALLACY-v2 requires
  for the parametric run.

Expected speedup: from *unbounded* (one cell per `U`, `U` unbounded) to
*one computation per `e`*. That is the only acceleration on the board
that changes the complexity class of the A2 lane rather than its
constant.

### 8.2 Decisive experiment

`DEPTH-PROFILE` (Sec 5.3). Minutes of CPU on already-decided cells; three
mutually exclusive read-outs; settles whether the A2 lane's whole
leading-order programme can terminate.

### 8.3 Campaign-systems check — **UPGRADE**

Not `NO_CHANGE`. The evidence is Sec 3.3: on **2026-09-02**, two
H2-branch flagships ranked `OPEN[DEG-AF-VS-N]` as their top successor,
one writing "I could not find it promoted anywhere in the record", while
the *same producer model on the same day* derived `M <= K` and
`sum deg D_i <= max(deg P, deg Q)` in the reducible-branch report. The
packet then reprinted the cap under gap (f) as a reducible-branch handle
and under gap (b)/(e) as an open question, in the same document, without
connecting them. This is not a review failure — every item was correctly
typed. It is an **index** failure: `OPEN[...]` tokens and banked lemmas
live in different namespaces and are never matched.

```text
UPGRADE CARD -- OPEN/BANKED COLLISION CHECK
WHAT   Before a report is sealed, extract every OPEN[...] it RAISES,
       and grep the banked corpus (xmodel/*.md, AUDIT.md, notes.md) for
       the OPEN's key nouns plus the quantity it asks to bound.  Emit a
       COLLISIONS section listing candidate matches with file:line.
       Fail-CLOSED: an empty COLLISIONS section must be explicit, never
       absent (per the SECTIONED-OUTPUT repair discipline).
SMALLEST USEFUL TEST
       Run it retroactively over the OPENs raised on 2026-09-02 only.
       PASS iff it surfaces companion-curve-alln:682-687 when fed
       OPEN[DEG-AF-VS-N].  One afternoon; no new infrastructure; the
       corpus is already on disk and already grep-shaped.
IF IT PASSES   make it a seal-time hook, like PREFLIGHT.
IF IT FAILS    the namespaces are genuinely disjoint and the right fix
       is a curated OPEN register with an explicit "quantity bounded"
       field -- more expensive, and now justified by a measurement.
```

This is strictly higher-value than the currently tracked upgrade
(`PREFLIGHT` encoding faithfulness), which guards against a failure mode
that has not yet cost the campaign a flagship successor. `PREFLIGHT`
should continue; this should go in front of it.

## 9. Idea cards (three)

### CARD 1 — `CHAU-DELTA` (proof; cheapest; highest ratio)

```text
GOAL          Closed-form delta_infty(M,d,e); substitute into the
              delta-budget; derive a beta-bound for (B2) 5..16 and a
              finite (p,q),k list for (B3) at N=4.
DEPENDENCIES  Chau Thm 1 / Cor 1 / Cor 2 [refs on disk]; COMPANION C6-C8
              incl. its leading-form correction; MI Lemma A (one place at
              infinity); HF Prop 3.2 and THEOREM B3-N4.  NO new theory.
CHEAPEST      Write delta_infty for the one-place branch of a bidegree-
DISCRIMINATOR (Md,Me) parametrisation at M=1 first (semigroup <d,e>,
              delta = (d-1)(e-1)/2) and check the budget on the realised
              (9,6,2) curve: n=9, delta_infty should reconcile with the
              curve's known singularities.  One page.
OUTCOMES      Budget < 2 at some N in 5..10  -> (B2) window KILLED there.
              Budget finite but >= 2         -> explicit (M,d,e) residual
                                               list; still a strict gain.
              Reconciliation FAILS on (9,6,2)-> one of C6/C8/Lemma A is
                                               mis-typed; that is itself
                                               a high-value find.
STOP          If delta_infty needs the full Puiseux expansion of the
              parametrisation rather than (M,d,e) alone, stop and type
              OPEN[DELTA-INFTY-NOT-NUMERICAL]; the budget is then not a
              closed form and Card 1 is dead.
INFO GAIN     Very high per unit cost: 12 degrees of (B2), plus the
              enumerability of (B3) at N=4.
```

### CARD 2 — `PARAM-U` (proof; changes the A2 lane's complexity class)

```text
GOAL          Decide the A2 E1-wall for all U at fixed e, with no U-bound.
DEPENDENCIES  RAY-KILL Secs 2-4 (the wall, RAY-1/DEP/2, the cell sizes);
              CELL-32 Sec 1 (Euler-eigenvalue leaders, LINEAR in the
              degree indices -- this is the load-bearing fact);
              OPEN[A2-O0-O1] must be resolved first or Lad_k is built
              from an incomplete equation set.
CHEAPEST      DEPTH-PROFILE (Sec 5.3) on the four decided cells.
DISCRIMINATOR
OUTCOMES      k* bounded, uniform in U -> run PARAM-U; horn's analytic
                                          residual retired.
              k* grows with U           -> PARAM-U dead; the growth rate
                                          is the first quantitative fact
                                          about the residual.
              no finite k*              -> the leading-order programme
                                          cannot terminate; STOP the
                                          ladder and say so.
STOP          If Lad_k over Q(U) is non-unit for k up to 3e+3, stop.
INFO GAIN     High.  Also settles gap (l) empirically.
DEPENDENCY    Blocked on OPEN[A2-O0-O1]; do not run Lad_k on six of seven
RISK          equations and read emptiness from it.
```

### CARD 3 — `B3-PARAM-SEARCH` (counterexample AND proof; dual-use)

```text
GOAL          Enumerate bidegree-(Md,Me) polynomial parametrisations whose
              image realises the (B3) N=4 profile (Sec 7.3).
DEPENDENCIES  Card 1 (to bound n); HF Prop 3.1/3.2, THEOREM B3-N4;
              the realisation -> SIROCCO -> ZvK -> S_N pipeline for the
              decision step.
CHEAPEST      n = 4 and n = 5 only, M max(d,e) in {4,5}: solve for
DISCRIMINATOR coefficients making the image have one (p,q) cusp with
              3|pq and 2|pq, plus k double points.  A small polynomial
              system; qqideal/msolve territory, minutes.
OUTCOMES      NONEMPTY -> feed the pipeline.  Kill => (B3) N=4 closes by
                          exhaustion (with Card 1's finite list).
                          Survive => FIRST object past representation
                          level; escalate immediately, all seats.
              EMPTY at every admitted (M,d,e) -> (B3) N=4 EMPTY, and with
                          CUSP-A-EMPTY + PROFILE the N=4 H2 branch closes
                          with no CUSP-KILL replacement needed.
STOP          If Card 1 admits n > 12, stop sweeping and report the list.
INFO GAIN     Highest of the three, and symmetric: both outcomes advance.
```

## 10. Current lanes — continue / redesign / stop

| Lane | Call | Reason |
|---|---|---|
| `a2-ubound-opus5-20260902` | **REDESIGN** | Keep `O0/O1` (a hard dependency for anything downstream) and the negative route. Drop the search for a literal `U`-bound: `C5` removes the symmetry that would supply it. Insert `DEPTH-PROFILE` then `PARAM-U`. The `E0` unit-Wronskian sub-route deserves a sharpened statement: `q r' - p' s = kappa/2` is a *constant* Wronskian-type identity, and the classical fact that `W(f,g) = const != 0` forces `deg <= 1` on a genuine Wronskian is the model to aim at; state precisely which pair `E0` is a Wronskian of before invoking Mason-Stothers. |
| `cusp-a-n8-gate-opus5-20260902` | **CONTINUE to completion, do not reseat** | Necessary but not binding-first (gap (c)). Let the running seat finish; do not renew. |
| `web-sweep-20260902-grok46` | **CONTINUE, retarget** | Add three explicit questions: (1) Jelonek's degree bound for the non-properness set `S_F` in dimension 2 — is `deg S_F` bounded in the geometric degree? This is `OPEN[N-VS-MAPDEG]` and it may be literature-closed; (2) classification of rational plane curves with one place at infinity, one cusp and `k` nodes (Orevkov / Abhyankar-Moh / Coolidge-Nagata) — this is exactly the `(B3)` `N=4` object; (3) `delta` of one-place branches from bidegree-`(Md,Me)` parametrisations. |
| box01 A2 cells window | **CONTINUE, instrument** | Add the `DEPTH-PROFILE` read-out to the existing driver; it is nearly free alongside the runs already queued. |
| Box03 `869` | **CONTINUE to the 12h cap, then stop** | Confirmatory under `N=4-CHECKED-CLOSED`; do not extend past the cap. |

**One lane I would add**, ahead of everything except Card 1: a desk seat
on `ANTI-MONOTONE` (Sec 4.2). It is the only named route to a
degree-monotone obstruction, and it costs a spreadsheet.

## 11. FALLACY-v2 audit

```text
Flag/place/series.        No cv flag, place or cover series is identified
                          anywhere.  Sec 3 keeps deg A_F (a place-count-
                          free degree), the parametrisation bidegree, and
                          the geometric degree N strictly apart, and
                          Sec 3.2 splits OPEN[DEG-AF-VS-N] into two
                          questions precisely to stop the conflation.
Per-ray/exit-set charge.  No exit claim; no charge_basis line emitted.
Carrier/attainment.       Sec 3.3's (9,6,2) datum is REPRESENTATIVE (one
                          realised curve, one degree pair); it is NOT
                          promoted to the numerical row, and the CLAIM is
                          typed [D] UNREVIEWED with three named checks.
Pole/interior.            No pole identity used.
Floor/attainment.         (CHAU-M) is an inequality and is used only as
                          an inequality.  The delta-budget is an IDENTITY
                          and is called a budget, not a bound, until
                          delta_infty is computed (Card 1's stop
                          condition covers the case where it is not a
                          closed form).  Sec 4.2's Riemann-Hurwitz side
                          is explicitly labelled a floor with an unpinned
                          correction (OPEN[B3-INFINITY-RANK]).
sat() wrapping.           No CAS run in this report.
Raw remainder degree.     No normal form taken.
Variable/ring map.        Sec 5's Q(U) proposal DECLARES the ring
                          (Q(a,b,U) after S1,S2), the unknown list, and
                          demands integer positive/negative controls
                          before the parametric run is believed.
Prime label/derivative.   Primes in Sec 5 and Sec 10 are d/dZ, per
                          CELL-32 Sec 1's convention; the E0 remark in
                          Sec 10 says "Wronskian-type" and explicitly
                          asks which pair before Mason-Stothers is
                          invoked, rather than asserting a Wronskian.
Merge-free/M-descent.     Not used.
Target/arrival index.     N (geometric degree), n (deg A_F), M (Chau
                          multiplicity), K (= gcd(deg P,deg Q)), U and e
                          (A2 cell indices) are used with fixed meanings
                          and never substituted for one another.  Note
                          M and K here are Chau's, NOT the (B3) cage's
                          M_tot / kappa -- flagged because the letters
                          collide across the two instruments.
Typed OPEN, never a cap.  OPEN[N-VS-MAPDEG], OPEN[A2-DEPTH-BOUND],
                          OPEN[DELTA-INFTY-NOT-NUMERICAL] raised rather
                          than filled by analogy.
```

## 12. Typed verdict block

```text
LANE            ideation-20260902T0741Z-opus5   (blind full-spectrum)
BASIS           8939320bc8c91a5a7b79eb30537e89e8c4a10333
INDEPENDENCE    No round-20260902T0741Z submission read.  Sources listed
                in the header.  One PDF extracted and read directly.

NEW AVENUE      ANTI-MONOTONE (Sec 4.2) -- the counting inequality and
                the covering cage have opposite monotonicity in a; run
                them on one (N,a) grid.  Only named route to a
                degree-monotone obstruction.  Dependency:
                OPEN[B3-INFINITY-RANK].
NEW MECHANISM   PARAM-U (Sec 5) -- top-k truncation has U-independent
                size and U-polynomial coefficients; one Groebner basis
                over Q(U) decides all but finitely many U.  Retires
                OPEN[A2-U-BOUND] without proving it.
NEW CROSS-CONN. COMPANION (Chau C6/C7/C8, M<=K) -> H2 delta-budget
                (Sec 3).  Answers, cross-branch, the successor both
                H2 flagships ranked first.
CLAIMS RAISED   [D] UNREVIEWED: at (9,6) the Chau degree cap is
                saturated by D_1 alone, so OPEN[COMPANION-R0-REALISATION]
                is negative at (9,6,2).  Three checks named (Sec 3.3).
                [D] Reproduction (not new): M <= K, independently
                derived, already banked at companion:682-687.
OPENS RAISED    OPEN[A2-DEPTH-BOUND]  (replaces OPEN[A2-U-BOUND])
                OPEN[N-VS-MAPDEG]     (residual half of DEG-AF-VS-N)
                OPEN[DELTA-INFTY-NOT-NUMERICAL] (Card 1 stop condition)
OPENS ANSWERED  OPEN[DEG-AF-CHAU] (the half the delta-budget needs);
                gap (l) answered NO.
NOT CLAIMED     any closure of (B2), (B3), (B1) or case (A) at any N;
                any bound of deg A_F in the geometric degree; any
                promotion of CLAIM [D]; any statement about the existence
                of F; the correctness of Chau's Thm 1 beyond its typing.
SYSTEMS         UPGRADE (Sec 8.3): OPEN/BANKED collision check.  Smallest
                useful test named; ranked ahead of PREFLIGHT.
CONTRACT        All contract items delivered.  DEVIATION: 15-25KB target
                overrun (~36KB).  Cause: the contract enumerates 46 rows,
                12 gaps, two rankings, two attacks, an experiment, a
                systems card, three cards and five lanes; Secs 1-3 were
                compressed twice rather than dropping required items.
                Reported, not concealed.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `41198`.
- Body SHA-256:
  `e67b2cd027e0cdbfc249d057d929e72a3e553ca61256f48b9978bedda358e9ce`.
- Frozen basis: `8939320bc8c91a5a7b79eb30537e89e8c4a10333`.
- Charged input SHA-256:
  `2646ac692c292c30597f9c830fd145c85e020207d803927825b8a162086055cf`.
