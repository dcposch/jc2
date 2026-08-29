# Adversarial cross-pollination audit — round `20260826T2350Z`

Producer: Opus 5 (`claude-opus-5`), adversarial cross-pollination researcher,
post-blind phase.

Inputs read completely: `xmodel/ideation-20260826T2350Z-fable5.md`,
`xmodel/ideation-20260826T2350Z-root.md`,
`xmodel/ideation-20260826T2350Z-order2.md`,
`xmodel/ideation-20260826T2350Z-td6.md`,
`xmodel/prime-ray-3p-one-edge-family-promotion-sol-20260826.md`.  Charged
files consulted for exact typing: `ladder/REDUCTION.md` (executive verdict,
CRITICAL 1--6, GGV5/GGV6/Chau rows), `AUDIT.md` (the promotion ledger rows
cited inline), `PROGRESS.md` and `APPROACHES.md` (2026-08-26 entries),
`notes.md` (`23:48Z LIVE STATE`).

Compliance: no web access, no AWS mutation, no heavy local computation
(file reads and hand algebra only), no `jc2-lean` access.  I wrote only this
file.

Epistemic labels are literal and match the round's convention: **exact**
= promoted/reviewed at a stated scope; **derived-here** = proved in this
document by hand, *unreviewed*, and not licensed for use until it clears the
normal producer/hostile-review gate; **navigation** = finite exact evidence
without the general conclusion; **speculation** = no discriminator has run.
Nothing in this document proves or disproves JC2, closes a chart, promotes
anything, or changes any lifecycle state.

**Method note, stated once.**  Three of the four blind reports converge on
the AS109/max-12 coupling and three converge on a parametric prime-ray
module.  Convergence of independent lanes on the same *object* is evidence
that the object is salient; it is not evidence that the proposed *mechanism*
works.  In both cases below I find that the converged mechanism is either
free (and therefore not what needs running) or a near-duplicate of a charged
experiment whose recorded outcome was null.  I promote neither on the
strength of agreement.

---

## 0. Verdict summary

| Claim | Verdict | One-line reason |
|---|---|---|
| 1. Deck-parity descent of landing certificates | **RUN NOW (narrowed)** — the parity table and the isotypic *validator*; **REJECT** the receiver-discharge conclusion | The Reynolds lemma is correct and free, but the two evidences Fable adduces (`U` rho-even, inverse rho-odd) are parity-blind to the one variable that decides the invariant ring, and the card conflates two unrelated receivers |
| 2. AS109-at-floor-12 into the max-12 leaves | **HOLD** the pincer; the proof-side direction is **free and recorded now**; the congruence-row direction is **REJECT** | The free direction needs no integrality at all; the paid direction duplicates the charged max-9 -> `(6,9)` integral-routing experiment, whose recorded outcome was "congruence automatically satisfied, no rank gained" |
| 3. `mu_3` / strip module / `3P-ORE3` | **REJECT** `mu_3` as a separate item (it is the same object); **RUN NOW** one merged preflight with a corrected sample; **HOLD** `3P-E31` as a proof target | Both stated cheapest discriminators are executed on samples that cannot contain the structure they test: `p=7,11,19` supply at most one shift step per residue class |

Surviving unique composite: **one isotypic certificate calculus with a
fail-closed non-target-component validator**, serving the `Z/2` deck action
(claim 1) and the `mu_3` exponent-residue action (claim 3) from a single
lemma.  Its value is as a *checker of emitted certificates*, which is the use
no report proposed.  See §4.

Derived-here mathematics produced by the audit: **Lemma AS-TRI** (§2.4) and
the **integral-reduction valuation criterion** (§2.5).

---

## 1. Claim 1 — deck-parity descent of landing membership certificates

### 1.1 Verdict

**RUN NOW, narrowed:** compile the rho-parity table (zero compute, probably
already half-computed inside the frozen discovery compiler `51c294e0...`)
and install the isotypic *validator* on V19's cofactors.

**REJECT as stated:** the inference "if the invariant subring presents the
square-receiver chart then square-receiver membership follows with zero new
saturation."  Its two premises are unsupported and one of its two declared
targets is provably out of reach.

### 1.2 When Reynolds averaging descends the certificate — exact statement

Fable's argument is correct but is stated in a special case that hides its
own failure modes.  The exact form:

> **Lemma (isotypic descent of a cofactor identity).**  Let `G` be a finite
> group acting by ring automorphisms on `R`, with `|G|` invertible in `R`.
> For a character `theta` of `G` write
> `pi_theta(c) = (1/|G|) * sum_{g in G} theta(g)^{-1} * g(c)` for the
> isotypic projector.  Suppose `r_1,...,r_n in R` are semi-invariant,
> `g(r_i) = chi_i(g) * r_i`, and `m in R` is semi-invariant with character
> `psi`.  Then any identity `m = sum_i c_i r_i` implies
>
> ```text
> m = sum_i pi_{psi*chi_i^{-1}}(c_i) * r_i      (the descended certificate)
> 0 = sum_i pi_{theta*chi_i^{-1}}(c_i) * r_i    for every theta != psi
> ```
>
> In particular if `psi` and all `chi_i` are trivial, then
> `m in (r_1,...,r_n) * R^G`.

Proof: apply `g` to the identity, multiply by `theta(g)^{-1}`, average over
`G`; the `r_i` come out by semi-invariance.  Char 0 (and `F_65521`, since
`2` and `3` are invertible there) suffices; a char-2 or char-3 replay of a
`Z/2` or `mu_3` descent is invalid and must be firewalled.

For the charged case `G = <tau>`, `tau: rho -> -rho`, `psi` and `chi_i`
trivial, this is exactly Fable's parity split, and it *is* free.

Three failure modes that Fable's binary (a)/(b) framing loses:

1. **Purely odd rows are not an obstruction.**  If `tau(r_i) = -r_i` the row
   is semi-invariant with `chi_i = sgn`, and the descent still runs: the
   surviving cofactor is `pi_sgn(c_i)`, and `pi_sgn(c_i) * r_i` is even.  In
   `R^tau` the effective generator is `rho * r_i`, not `r_i`.  So the
   descended ideal is `({r_i : even}) + ({rho * r_i : odd})` — a *different*
   ideal from the one the receiver is presumably defined by.  Descent
   succeeds; the receiver identification fails.  Fable calls this case (b)
   and treats it as failure of descent; it is not.
2. **Genuinely mixed parity in one row is a real obstruction, with a
   quantified cost.**  If `r_i = r_i^+ + r_i^-` with both parts nonzero,
   `r_i` is not semi-invariant, and the best available descent is into the
   parity-refined ideal `(r_i^+, r_i^-) ⊇ (r_i)`.  Membership in a *larger*
   ideal proves the conclusion only on the *smaller* locus
   `V(r_i^+, r_i^-) ⊊ V(r_i)`.  The descent therefore buys a coverage debt,
   not a failure — and the debt is exactly the kind of silent scope shrink
   this campaign polices.
3. **A mixed-parity localizer moves the open set.**  If `k` is not of pure
   parity then `tau` does not stabilize `D(k)`; it carries `D(k)` to
   `D(tau(k))`.  The descended certificate then lives on
   `D(k * tau(k)) ⊊ D(k)`, and the promoted `T-rs` scope
   (`D_+(rs) intersect D(k)`, `APPROACHES.md` 2026-08-26 overlay) is not
   preserved.  Fable lists no such outcome.

### 1.3 What happens to odd generators such as `rho`

`rho` is a **source** variable (`pTot = -2*rho^2 + 2*sigma*ell1 + ...`,
`PROGRESS.md` 2026-08-26), not a Rees chart coordinate, and `rho` is odd,
hence `rho ∉ R^tau`.  Three consequences, in decreasing obviousness:

- The promoted `T-rs` conclusion is a statement about an **odd** element:
  `rho` is a unit with inverse `-32*rho*qcs^2*(8*rho^2*qcs^2+3)`, which is
  odd.  Its even shadow "`rho^2` is a unit" is *not* a new theorem obtained
  by descent — it follows from `T-rs` with zero argument, parity or not
  (`rho` invertible ⇒ `rho^2` invertible, inverse `(rho^{-1})^2` even).  So
  the descent's payoff cannot be the square-receiver *statement*; it can
  only be the square-receiver *certificate*.
- The certificate does carry over cleanly, and explicitly.  With
  `S = rho^2`, `U = 1 + 32*S*qcs^2*(8*S*qcs^2 + 3) = 1 + 96*S*qcs^2 +
  256*S^2*qcs^4`, so `U = 0` gives
  `1 = -S*qcs^2*(96 + 256*S*qcs^2)`, i.e. `S` inverted with an explicitly
  even cofactor.  This is a genuine invariant-ring certificate — *if* the
  rows and `k` are semi-invariant.
- `R` is free of rank two over `R^tau` with basis `{1, rho}` **only if
  `rho` is the sole odd generator**.  That is precisely what the table must
  decide, and it is not decided by anything charged.

### 1.4 Is the invariant subring the charged square receiver?  Almost
certainly not — for two independent reasons

**Reason A — the card conflates two unrelated receivers.**  Fable's card 1
declares its target as "deck-equivariant square bridge; part of closed
receiver."  `APPROACHES.md` (2026-08-26 landing overlay) lists these as
*separate* open items: "the actual-total `c0,c1,a0,a1` charts, closed
receiver, scheme-theoretic overlaps, deck-equivariant square bridge, and
`k=0` remain open."  The Gate-T **closed receiver** is the
all-generators-vanish stratum of the iterated Rees blowup — TD6's card A
names it exactly ("separate receivers for all generators identically zero
and for `k=0`"), and root's card A addresses it by the irrelevant-ideal
power containment `B^N ⊆ I + (rho)`.  It has no deck content whatever.
Isotypic descent is *provably orthogonal* to it: averaging over `tau` cannot
produce information about the locus where the Rees generators vanish.  So
one of the card's two declared targets is out of reach by construction, and
the card's cost/benefit is overstated by that factor.

**Reason B — the evidence adduced is parity-blind to the decisive
variable.**  Fable cites two facts as support: the V17 grade-14 coefficient
is rho-even (`PROGRESS.md`: "grade 14 has 304 monomials, is rho-even"), and
`U = 1 + 32*rho^2*qcs^2*(8*rho^2*qcs^2+3)` is rho-even.  But `qcs` occurs in
`U` **only in even powers**, so

```text
tau(U) = U  and  tau(inverse) = -inverse
```

hold identically **whether `qcs` is even or odd**.  Neither displayed object
constrains `tau(qcs)` at all.  Yet `tau(qcs)` is exactly the entry that
decides the shape of `R^tau`:

- `tau(qcs) = +qcs` (and likewise for `qc0, qc1`): `R^tau = k[rho^2, rest]`
  is a polynomial ring, and Fable's "`rho^2 -> R`, others fixed"
  presentation is right.
- `tau(qcs) = -qcs` for even one chart coordinate:
  `R^tau = k[rho^2, rho*qcs, qcs^2, ...]` with the relation
  `(rho*qcs)^2 = rho^2 * qcs^2`.  `Spec R^tau` is then **singular** (an
  `A_1`-type quotient), not a chart, and the "generic shape for a sign
  action" claim is false.

And `qcs = cs/rs` is a *ratio* of two Rees generators, so its parity is the
product of theirs; there is no a-priori reason for it to be even.

Independently, the campaign's charged "square" objects are the
**generic-square first-normal chart** `D(p*k0)` in the order-two/D1 lane and
the **exact-square/Pell receiver** listed open in the delayed-load
exceptional `K` promotion.  Neither is described anywhere as
`Spec` of the rho-invariant subring of a Gate-T Rees chart.  Order two's own
compiler rule — "must never infer a source chart from a normalized
coordinate analogy" — applies verbatim against this step.

### 1.5 Prior art the card does not cite

Isotypic reasoning is **already charged in this campaign**.  The
2026-08-26 14:03Z "NORMALIZED AFFINE-FABER GENERIC `J` EXCLUSION" runs on
exactly this mechanism: "the three odd rows `(R1,R3,R5)` generate the
complete odd-coordinate ideal `(c,u,n3)` ... **Parity then forces
`R7 = 0`**."  So the mechanism is not new; what would be new is applying it
to the **cofactors of an actual-total landing certificate**.  Fable's
novelty claim ("nobody has proposed descending the cofactor identities by
parity") is correct only in that narrower form and should be recorded that
way.

### 1.6 Cheapest discriminator — the exact table, and where to read it

The compiler frozen at `51c294e0...` already "checks the complete special
fibre, deck action, recursive extraction, cusp certificate, omission
sentinel, and wrong-source negative control" (`PROGRESS.md` 2026-08-26).
**Read its existing deck-invariance output first**; compile a fresh table
only for what it does not already report.  The table has fifteen cells:

```text
source:    tau(rho)=-rho;  tau(sigma), tau(ell_j), tau(k0), tau(p)      [5]
generators: parity of rs, cs, c0, c1, a0, a1                            [6]
chart:     parity of qcs=cs/rs, qc0, qc1   (= product of the above)     [3]
localizer: parity of k                                                  [1]
rows:      parity of Tg10_1/rs, Tg10_2/rs, Tg10_3/rs, Tg12_6/rs^2       [4]
```

Each cell is decided by inspecting whether `rho` occurs in even or odd total
degree in the frozen V0R1/V9 files — an exponent-parity scan, not algebra.
The **decisive cells are `tau(qcs)` and `parity(k)`**; everything else is
bookkeeping.

### 1.7 All-outcome interpretation

- **(a) `qcs, qc0, qc1` even, `k` even, all four rows semi-invariant.**
  `R^tau = k[rho^2, rest]`; the descent is free; the explicit invariant
  certificate of §1.3 holds.  This discharges *no charged debt on its own*
  (§1.3, first bullet), but it makes every future chart certificate
  automatically available in the invariant presentation, and it makes the
  validator of §4 non-vacuous for `c0,c1,a0,a1`.  Enqueue a short lemma; do
  **not** report it as closing the deck-equivariant square bridge until
  someone writes the chart map from `Spec R^tau` to the charged receiver.
- **(b) Some chart coordinate odd.**  `R^tau` is not a polynomial ring; the
  "square receiver = invariant subring" identification is refuted.  This is
  a *useful* outcome: it converts a vague open item into a named singular
  quotient with an explicit relation, and it tells the receiver owner that
  a real comparison map must be budgeted.
- **(c) Some row of genuinely mixed parity.**  Descent into
  `(r^+, r^-)` only; record the exact grades where parity breaks and the
  resulting coverage debt `V(r^+,r^-) ⊊ V(r)` (§1.2 item 2).
- **(d) `k` of mixed parity.**  The descended statement holds only on
  `D(k*tau(k))`.  Do not restate it on `D(k)`.
- **(e) `tau` swaps the `rs` and `cs` specializations.**  Fable's retry is
  ill-posed as written (averaging needs a group acting on one ring), but
  the correct reading is far stronger and is an immediate **consistency
  check on the campaign itself**: if `tau` carried the `rs` chart to the
  `cs` chart, then `T-cs` would follow from the promoted `T-rs` by
  transport, and the live V18R1 dual-AWS lanes would be redundant.  Since
  V18R1 is being run as an independent test, either `tau` does not swap the
  charts, or the campaign is duplicating a free result.  Answer this cell
  first; it costs one line and can only save time.

### 1.8 Dependency / claim firewall

```text
ALLOWED to consume: frozen V0R1 archive 05e7fc27...; compiler 51c294e0...
                    deck-invariance report; promoted T-rs 52b59e8d... at its
                    literal D_+(rs) ∩ D(k) scope; V19 cofactors 633e5af2...
                    ONLY after V19 has its own validator + hostile review.
FORBIDDEN:          (i) any statement about the Gate-T closed receiver;
                    (ii) any identification of Spec R^tau with a charged
                         "square" object absent an explicit two-sided chart
                         map;
                    (iii) any char-2 replay of a Z/2 descent;
                    (iv) restating a D(k*tau k) result on D(k);
                    (v) treating "rho^2 is a unit" as new information.
```

### 1.9 Stop rule

One desk pass over the fifteen cells.  If cell `tau(qcs)` returns odd, stop
the receiver line immediately and file outcome (b); the validator of §4 still
runs.  No AWS job is licensed by this claim at any outcome; the descended
identity is verified by re-expanding the same cofactors the producer already
emitted.

---

## 2. Claim 2 — AS109 at floor 12 and max-partial-`y` routing

### 2.1 Verdict

**HOLD** the pincer as designed by Fable (card 2) and TD6 (card C).

Split, because the two directions have completely different prices and the
reports price them identically:

- **Direction A (proof side closes a leaf ⇒ AS floor rises): free, needs no
  integrality, and I record the exact conditional in §2.3 now.**  Both cards
  gate it behind the integrality audit; that gating is a mistake.
- **Direction B (impose AS109 congruence rows on the leaf clients):
  REJECT** at present typing.  It is a near-duplicate of a charged
  experiment one degree tier down whose recorded outcome was null (§2.6),
  and it is ill-typed for an independent reason (§2.7).

### 2.2 The exact theorem interface

Charged components, at their recorded scopes:

```text
T1  (7eda0a46 / d9522acb, different-model confirmed)
    Over EVERY characteristic-zero field, every Keller pair with
    max(deg_y P, deg_y Q) <= 11 is a polynomial automorphism.
    Unbounded x-degree.  Descent from the closure by uniqueness/faithful
    flatness.

T2  (AS109 support-gate CONDITIONAL HENSEL BRIDGE, dual-confirmed)
    Any F in Z_109[x,y]^2 with det J_F = 1 and F = (x - x^109, y) mod 109
    has, for each fixed residue b, all 109 source balls (a,b)+109*Z_109^2
    mapping bijectively onto (0,b)+109*Z_109^2.  Hence F is noninjective
    over Q_109, and adjoining coefficients and two preimages embeds a
    complex Keller counterexample.  ASSUMES a lift; asserts none.

T3  (c76f26a6 / 430ffa3c)   T1 o T2:  conditional on an exact integral
    polynomial AS109 lift, max(deg_y A, deg_y B) >= 12.  Explicitly NOT a
    support bound, lift, marked collision, or degree-exactly-twelve routing.

T4  (30cb45cc / 2951856c, "MAXIMUM-12 KUMMER PREFLIGHT")
    ROUTING: the only primitive maximum-12 cells are (8,12) and (9,12);
    unresolved history classes 4|H and 3|H.  Kummer orders 4,2,1 and 3,1.
    T1's own promotion labels the (8,12)/(9,12) statement
    "a checksum, NOT their exclusion".

T5  (d303bf76 / e2ddc5b5)   (8,12) order four closed; live leaves are
    order two/one on (8,12) and order three/one on (9,12); route widths
    33 vs 26 license allocating (9,12) next.
```

Write an **AS109 lift** for `F = (P,Q)`, `P = x - x^109 + 109A`,
`Q = y + 109B`, `F in Z_109[x,y]^2`, `det J_F = 1`.  Two facts used
throughout, both immediate from `F = (x-x^109, y) mod 109`:

```text
(F1)  v_109(p_j) >= 1  for every j >= 1, where P = sum_j p_j(x) y^j
(F2)  v_109(q_j) >= 1  for every j >= 2, and v_109(q_1) = 0, q_1 = 1 mod 109
```

(`v_109` = the Gauss valuation on `Z_109[x]`; multiplicative by Gauss's
lemma.)  Note the immediate structural consequence: **the reduction drops
`y`-degree from `(deg_y A, max(1,deg_y B))` to `(0,1)`.**  Every bit of the
pair's max-12 structure is concentrated in the 109-divisible part.  This one
sentence drives everything below.

### 2.3 Direction A is free — no integrality is used anywhere

The routing operations (source shears, target `GL_2` and polynomial shears,
scalings, depressions, scalar extension) are **automorphisms over the
ambient field**.  Automorphy of `F` is preserved by pre- and
post-composition with automorphisms, over `Q_109` or any extension, and T1
descends automorphy from an extension.  Therefore:

> **Conditional (recorded here at zero cost).**  Suppose (i) the max-12
> routing is **total**: every characteristic-zero Keller pair with
> `max(deg_y P, deg_y Q) = 12` is source/target-equivalent over some
> characteristic-zero extension field to a pair in cell `(8,12)` or
> `(9,12)`, or reduces to `max <= 11`; and (ii) both cells are excluded at
> full unbounded-`x` scope.  Then every characteristic-zero Keller pair with
> `max(deg_y P, deg_y Q) <= 12` is an automorphism, and composing with T2
> exactly as T3 does raises the conditional AS109 correction floor to
> `max(deg_y A, deg_y B) >= 13`.

TD6's card C states the same endpoint ("Both max12 cells are eventually
source-honestly excluded at full unbounded-x scope: only then does the
conditional AS correction floor rise from twelve to thirteen") but places it
*inside* a card whose stop condition is "Stop the cross-lane version at the
first failed integral/collision interface" — which would abandon the one
direction that the interface never touches.  Fable's outcome (a) likewise
conditions the floor-raise on the integrality audit passing.  Both are
wrong on that point.  **The proof-side pincer is already assembled; it costs
nothing and should be written into the composition ledger as a standing
conditional, so that closing `(9,12)` is automatically credited to the AS
floor.**

### 2.4 The first fail-closed zero-compute audit — and what it returns

Both cards nominate the integrality audit as the first action.  That is the
second action.  The first is a **quantifier audit that can only fail
closed**, and it gates Direction A as well:

> **Audit Z1 (totality of the max-12 routing).**  Read the max-12 Kummer
> preflight `30cb45cc...` and its review `2951856c...` and decide whether
> "the only primitive maximum-12 cells are `(8,12)` and `(9,12)`" is
> (i) a statement that the reduction recursion is **total on max-12
> inputs** — i.e. a transformation of every given pair — or (ii) an
> **enumeration of degree pairs** that fail to reduce under the listed
> rules, with no claim that every max-12 pair enters the recursion.
> Fail-closed default: reading (ii), because T1's own promotion says
> "at maximum twelve the first new primitive pairs are exactly `(8,12)` and
> `(9,12)`; **this is a checksum, not their exclusion**."

If (ii) holds, both directions of the pincer are ill-typed, and the correct
successor is a one-page "max-12 routing totality" lemma — not compute.  This
is precisely the `REDUCTION` CRITICAL-2 failure shape (existential selection
mistaken for a normalization of every object).  Fable names it as fallback
outcome (c); it belongs first.

I ran the second audit by hand.  It returns a small exact theorem:

> **Lemma AS-TRI (derived-here, elementary, unreviewed).**  No exact
> integral AS109 lift has `deg_y Q <= 1`.  Equivalently, every such lift has
> `deg_y B >= 2`.

*Proof.*  `deg_y Q = 0` is impossible since `Q = y mod 109`.  So
`Q = q_1(x) y + q_0(x)` with `v_109(q_1) = 0` by (F2).  Induct on
`m = deg_y P`.

If `m >= 1`: `J = P_x Q_y - P_y Q_x = 1` is constant, so its `y^m`
coefficient vanishes.  Computing it,
`P_x Q_y` contributes `p_m' q_1` and `P_y Q_x` contributes `m p_m q_1'`
(the `q_0'` term lands in `y^{m-1}` and below).  Hence
`p_m' q_1 - m p_m q_1' = 0`, i.e. `(p_m / q_1^m)' = 0`, so
`p_m = c * q_1^m` with `c` a constant of `Q_109` (char 0).  Gauss gives
`v_109(c) = v_109(p_m) - m*v_109(q_1) = v_109(p_m) >= 1` by (F1).  So
`c in 109*Z_109`, the target shear `(u,v) -> (u - c v^m, v)` is integral and
determinant-preserving, `P' = P - c Q^m` lies in `Z_109[x,y]`, its `y^m`
coefficient is `p_m - c q_1^m = 0`, and
`P' = P - 0 = x - x^109 mod 109`.  So `(P', Q)` is again an exact integral
AS109 lift with strictly smaller `deg_y P`.

If `m = 0`: `P = p_0(x)` and `J = p_0'(x) q_1(x) = 1` forces both factors to
be nonzero constants, so `deg_x p_0 <= 1`.  But `p_0 = x - x^109 mod 109`
has `x`-degree 109.  Contradiction. `[]`

AS-TRI is independent of the charged AS109 results, which are all two-sided
("both correction `y`-degrees at most `k`"): quadratic (`k=2`), cubic
(`k=3`), the `y`-degree-`<=5` coupled-section gate, and T3's
`max >= 12`.  AS-TRI is one-sided on the **target** correction.  Combined
with T3, the pair `(deg_y A, deg_y B)` of an AS109 lift satisfies
`max >= 12` and `deg_y B in [2, ...]`; at the floor with `deg_y A = 12`, the
target correction is confined to `[2,12]`, and the branch `(12, <=1)` — one
of the shapes an AS lift at the floor could have taken — is dead.

**Custody note.**  AS-TRI is derived-here and unreviewed.  It must go
through the ordinary producer/hostile-review gate before any composition
consumes it.  Nothing in §2.3 or §2.6 depends on it.

### 2.5 Does routing preserve the marked mod-109 collision?  A precise answer

The reports ask one question; there are three, with different answers.

1. **Noninjectivity over `Q_109` (the thing T2 actually delivers, and the
   thing T3 actually consumes): preserved by *any* source/target
   automorphisms over `Q_109` or an extension.  No integrality is needed.**
   This is why Direction A is free.
2. **The residue-level fibre collapse ("for each `b`, all 109 values of `a`
   collide"): preserved iff the routing consists of automorphisms defined
   over `Z_109` *with integral inverses*, and iff no residue-field growth
   occurs.**  Then `Fbar' = sigmabar o Fbar o taubar^{-1}` with
   `sigmabar, taubar` automorphisms of `A^2_{F_109}`, hence bijective on
   `F_109`-points, hence the collapse survives.  Residue growth matters
   because `x - x^109` annihilates `F_109` and **not** `F_{109^f}` for
   `f > 1`; an unramified degree-`f` extension keeps the polynomial
   congruence but destroys the point-collapse marking.
3. **The marked AS *shape* `Fbar = (x - x^109, y)`: not preserved.**  After
   an integral routing step the reduction becomes
   `sigmabar o (x-x^109, y) o taubar^{-1}`, an AS-*twisted* map.  So the
   "extra finite row system" Fable proposes to impose on the leaf client is
   not the rigid pair of congruences `P = x - x^109`, `Q = y`; it is a
   family parameterized by the reduced routing data.

The exact criterion for a reduction step to stay integral, derived from
(F1)/(F2): the Abhyankar step at `n | m` shears `P -> P - c Q^{m/n}` with
`c = p_m / q_n^{m/n}`, so

```text
step is 109-integral  <=>  v_109(p_m) >= (m/n) * v_109(q_n).
```

For `n = 1` this is automatic (`v(q_1) = 0`, `v(p_m) >= 1`) — that is
exactly AS-TRI.  For `n >= 2` both valuations are `>= 1` and the criterion
is a genuine constraint that can fail; when it fails at `v_109(c) = 0` the
reduction remains defined but the reduced map changes (case 3 above).

And a structural obstruction that neither card states.  The leaf machinery
requires a **monic** model: "for monic depressed `f,g` of degrees `(m,n)`
over a characteristic-zero differential field, put `w = f^(1/m)`"
(`d303bf76...`).  Monicization divides by `lc_y`, and by (F1)/(F2) the
leading `y`-coefficients of an AS109 lift have `v_109 >= 1`.  To make
`lc_y` a 109-unit one needs `deg_y P' = deg_y Pbar'` — the reduction must not
drop `y`-degree.  But `Pbar'` is built from `x - x^109`, whose `y`-degree
under a source substitution `(Xbar, Ybar)` is `109 * deg_y Xbar` by
Frobenius additivity in char 109 — i.e. `0` or `>= 109`.  Staying inside
`max deg_y <= 12` forces the `0` branch and hence forces
`v_109(lc_y) >= 1`.  Target shears can raise the reduced `y`-degree, but
only by raising the char-0 `y`-degree past 12 (`sigma_1(u,v) = u + v^12`
gives `deg_y P' = max(m, 12n)`, which needs `n <= 1`, excluded by AS-TRI).
**Consequently, along every route that keeps the pair at maximum
partial-`y` twelve, the leaf's monic normalization divides by an element of
positive 109-valuation, and the leaf's normalized coordinates have negative
valuation.  There is no `Z_109`-model in which the leaf coordinates and the
AS congruences are simultaneously rows.**

This is exactly the mechanism visible in the charged `(6,9)` work: "the
depression `z = s y + A/6` is over `k(x)(s)`, **not a polynomial source
automorphism**" with `s^3 = h`; for an AS lift `h` has positive valuation,
so `1/s` has negative valuation.

### 2.6 Direction B duplicates a charged experiment whose outcome was null

The decisive citation, which neither Fable nor TD6 mentions:

> **`AUDIT.md`, GCD3 `(6,9)` block:** "AS109 COROLLARY: conditionally on an
> exact lift, maximum actual `y`-degree at most eight is impossible by
> reviewed Hensel noninjectivity.  **Maximum exactly nine reduces, by an
> integral target operation and possible swap, to `(6,9)` with `3|H`.  Its
> first non-top `y^13` row is automatically divisible by `109^2`; an exact
> primitive-core control rules out a universal first-row valuation
> contradiction.**"

Read that carefully.  The campaign has already, one degree tier down,
(i) performed the routing, (ii) found it **integral**, (iii) imposed the
AS congruence on the routed leaf, and (iv) recorded the result: the
congruence row is *automatically satisfied* (`109^2 | row`), and the
obvious valuation contradiction is *ruled out by an exact control*.  The
rank gained was zero — for exactly the reason §2.2 identifies: the AS
congruence says "everything structural is `= 0 mod 109`," which is a
degeneration statement, not a cutting constraint.

Therefore the max-12 version of Direction B has a documented, unfavourable
prior from a strictly easier instance.  Proposing it again without citing
the max-9 outcome would be the campaign re-running a null experiment at
higher cost.  This is the single strongest reason for the HOLD.

### 2.7 Second, independent reason Direction B is ill-typed

The `(8,12)`/`(9,12)` leaf clients are **characteristic-zero differential
algebra**: differential-constant Faber coefficients `h_j`, residues `r_l`
with `r_1' = ... = r_{m-2}' = 0`, Kummer classes on the monic-core divisor
class group, triangular determinant `m^{m-1}`.  Their exclusion arguments
use char-0-specific facts (a differential constant is a constant;
integration; invertibility of `m` and of Kummer orders).  There is no
charged `Z_109`-flat model of any leaf.  "Add the congruence rows to the
live leaf clients as small finite systems" therefore asks to intersect a
char-0 classification with a char-109 coefficient condition inside a scheme
that does not exist.

The campaign has caught precisely this failure mode before and priced it:
avenue 25 was lowered this round by three of four reports because "the
proposed direct use of Lu--Song/Davenport--Zannier weighted-tree counts to
certify Sigray's `td=7` book is a **type mismatch**" (TD6 §2).  Direction B
is the same shape of mismatch, and it was proposed by the same reports that
correctly flagged avenue 25.

### 2.8 All-outcome interpretation (for the audits that remain worth doing)

- **Z1 returns "checksum only" (fail-closed default).**  Both directions are
  ill-typed.  Successor: a max-12 routing totality lemma.  Zero compute
  until it exists.  *This is the most likely outcome and it is the cheapest
  to confirm.*
- **Z1 returns "total transformation".**  Record the §2.3 conditional in the
  composition ledger; credit any future `(9,12)` or `(8,12)` closure to the
  AS floor automatically.  Do **not** unlock Direction B.
- **AS-TRI survives hostile review.**  A small exact narrowing of the AS
  habitat (`deg_y B >= 2`) and, more usefully, a *worked positive control*
  for the integral-shear ladder that any future routing audit can replay.
- **AS-TRI fails review.**  My derivation is wrong somewhere in §2.4; the
  valuation criterion of §2.5 still stands independently, and §2.3 and §2.6
  are untouched.
- **Someone builds a `Z_109`-flat model of a leaf.**  Direction B reopens —
  and should then be run first at `(6,9)`, where the max-9 record gives a
  known-null calibration, before spending anything at max 12.

### 2.9 Dependency / claim firewall

```text
ALLOWED:  T1 at "every characteristic-zero field, unbounded x"; T2 as an
          assumption-conditional bridge; T3 verbatim; T4 read as a checksum
          until Z1 says otherwise; T5's leaf inventory.
FORBIDDEN:
  (i)   citing T4 as "every max-12 pair routes to (8,12)/(9,12)" before Z1;
  (ii)  gating the §2.3 floor-13 conditional on any integrality audit;
  (iii) any claim that the AS congruence adds rank to a leaf client, absent
        a Z_109-flat leaf model AND a re-run of the max-9 calibration;
  (iv)  reading residue growth (F_109 -> F_{109^f}) as harmless for the
        point-collapse marking;
  (v)   using AS-TRI in any composition before its own review;
  (vi)  any AS support enumeration.  Neither card licenses one and this
        audit licenses none.
```

### 2.10 Stop rule

Z1 is one reading pass and terminates the claim if it returns (ii).  If it
returns (i), write the §2.3 conditional into the ledger (one paragraph) and
stop; no AWS job is licensed by claim 2 at any outcome in this audit.  Send
AS-TRI to review as an ordinary small producer artifact.  If anyone
proposes Direction B again, the required precondition is a written
comparison against the max-9 `(6,9)` null result, not a new integrality
audit.

---

## 3. Claim 3 — `mu_3`, the strip module, and `3P-ORE3`

### 3.1 Verdict

**REJECT** root's `mu_3` projector as a separate proposal: it is not an
independent mechanism but the block-decomposition of the very module
order two and TD6 propose, and keeping it as its own card would duplicate.

**RUN NOW**, before the arbitrary-standard-pair bridge is settled: **one**
merged preflight, read-mostly, with the sample corrected per §3.4 and the
scope memo of §3.6 written *first*.

**HOLD** `3P-E31` as a proof target.

### 3.2 The three proposals are one object

```text
order2 §3 / Card B `3P-ORE3`:  regrade the emitted covering systems so the
    boundary operators form a fixed-band family M_gamma over Q[gamma];
    seek a bounded-order left recurrence
    lambda_{gamma+1} S_gamma - lambda_gamma = eta_gamma M_gamma, order <= 3.

TD6 §4 / Card B:  "translation-equivariant strip module"; canonicalize row
    supports after edge-normal regrading; test whether coefficients
    interpolate in Q[p,gamma] at bounded degree.

root §3:  a mu_3 Fourier projector on exponent residues, from the fixed
    denominator three in Corner(gamma+3, 3, gamma).
```

They share one irreducible content: *canonicalize the emitted rows in
edge-normal coordinates and test for a finite shift grammar in `gamma` with
`p` confined to boundary data.*  TD6 supplies the hypothesis
(translation-equivariance), order two supplies the certificate form (a
bounded-order left annihilator), root supplies the grading.  The grading is
not an extra idea: it is forced.

**Why `mu_3` is forced, not optional.**  The promoted arithmetic gives final
one-edge chains for `4 <= gamma <= v = (3p-1)/4` — count `(3p-13)/4` — of
which **exactly those with `3` not dividing `gamma`** carry an MN family —
count `(p-3)/2`.  So the `gamma`-lattice carries a distinguished `3`-periodic
structure: the MN multiplicity is `1` on `gamma != 0 mod 3` and `0` on
`gamma = 0 mod 3`.  Any recurrence in `gamma` valid across the family must
therefore have `3`-periodic coefficients, i.e. must be block-diagonal under
the `Z/3` action on `gamma` — which is exactly the `mu_3` isotypic
decomposition, and the same lemma as §1.2 with `G = mu_3` (`3` invertible in
char 0).  Furthermore the denominator `3` in `Corner(gamma+3,3,gamma)` puts
the same `Z/3` on the Laurent exponent residues, and the two coincide because
the corner's exponent datum is `gamma/3`-graded.  One group, one
decomposition.

**Corollary: order two's ansatz is mis-parameterized as written.**
`lambda_{gamma+1} S_gamma - lambda_gamma = eta_gamma M_gamma` uses the shift
`gamma -> gamma+1`, which carries the admissible set `{3 does not divide
gamma}` off itself (`gamma = 5 -> 6`).  On the MN-viable reading the shift is
literally undefined at one third of the lattice.  The repair is `S^3` within
each residue class — or, on the all-chains reading, an order-`3k` operator in
`S` with `3`-periodic coefficients.  Either way `mu_3` is the normalization,
not a second experiment.

### 3.3 Which index set?  This is the first zero-compute question

The two readings give different minimum samples, so the preflight must first
pin what the emitter actually produces:

- **Per-MN-family** (index set `{4 <= gamma <= v, 3 does not divide
  gamma}`): the natural shift is `S^3` within a residue class.
- **Per-chain** (index set `{4 <= gamma <= v}`): the shift is `S`, but the
  module degenerates on `3 | gamma`, forcing `3`-periodic coefficients.

Cost: read the emitter's own output typing.  Zero compute.

### 3.4 The stated cheapest discriminators cannot execute — sample arithmetic

Both cards nominate `p = 7, 11` for fitting with `p = 19` as holdout.  With
`v = (3p-1)/4` the admissible `gamma` are:

```text
p = 7 : v = 5 ;  gamma in {4,5}                                 (2 = (7-3)/2)
p = 11: v = 8 ;  gamma in {4,5,7,8}                             (4)
p = 19: v = 14;  gamma in {4,5,7,8,10,11,13,14}                 (8)
p = 23: v = 17;  gamma in {4,5,7,8,10,11,13,14,16,17}          (10)
p = 31: v = 23;  gamma in {4,5,7,8,10,11,13,14,16,17,19,20,22,23} (14)
```

Split by residue class `gamma mod 3` — the classes a `S^3` recurrence lives
in:

```text
        class [1] = {4,7,10,...}   class [2] = {5,8,11,...}
p =  7        1 point                    1 point
p = 11        2                          2
p = 19        4                          4
p = 23        5                          5
p = 31        7                          7
```

An order-`r` recurrence in `S^3` needs `r+1` consecutive members to fit and
at least one more to validate.  For `r <= 3` that is **at least five per
class**.  Hence:

- `p = 7` and `p = 11` together supply **at most one shift step per class**.
  They cannot fit, let alone falsify, order two's order-`<= 3` recurrence.
- `p = 19` supplies four per class: enough to *fit* an order-3 recurrence
  with **zero** degrees of freedom left for validation.  It is therefore the
  minimum *fitting* sample, **not a holdout**.
- The minimum viable design is `p = 23` (fit + one validation) with `p = 31`
  (fit + three) as the holdout; `p = 19` is a cheap cross-check and
  `p = 7, 11` are degenerate boundary controls only.

TD6's phrasing is worse still: "canonicalize row supports for `p = 7,11,19`
and **all common final `gamma`**."  The `gamma` common to those three primes
is `{4,5}` — one per residue class, i.e. **zero** shift steps.  As written,
TD6's discriminator tests `p`-interpolation at two fixed `gamma`, which is
not the translation-equivariance hypothesis its own card states.

This correction is the concrete deliverable of claim 3's audit, and it costs
nothing but changes what gets emitted.

On the all-chains reading the numbers are friendlier — five consecutive
`gamma` already at `p = 11` — which is a second reason §3.3 must be answered
before anything is emitted.

### 3.5 Cheapest discriminator (merged, corrected)

One preflight, in this order, stopping at the first failure:

1. Pin the index set (§3.3).  Zero compute.
2. Freeze the edge-normal regrading and confirm it preserves Laurent
   denominators and the direction `(3,-1)` (TD6's dependency list; keep it).
3. Emit the smallest terminal block only, for the corrected sample of §3.4,
   split by `mu_3` class.
4. Canonicalize row/column supports; compare bandwidth across `S^3` within
   each class.
5. Only if bandwidth is stable: interpolate entries in `Q[p, gamma]` at
   bounded degree; only then look for a left annihilator.

Steps 1--2 are desk work.  Steps 3--4 are the smallest terminal block, not
monolithic systems (both cards already say this; keep it).

### 3.6 The scope warning, and what it does and does not forbid

The promotion's own firewall plus `REDUCTION` give the exact ceiling:

- `REDUCTION` CRITICAL 2: GGV minimality is an **existential selection**
  (`exists counterexample => exists GGV-minimal standard counterexample`),
  not a normalization of an arbitrary counterexample; "No argument relates
  the selected pair's `td` to that of an arbitrary original pair."
- `REDUCTION` CRITICAL 3 (`G2-PSC`): there is no theorem translating GGV
  corners/admissible chains into Sigray pole/tree decorations, and the
  per-family §4 reductions pass through Laurent automorphisms and finish
  outside `Aut C[x,y]`.
- The `3p` promotion: "A high triangular source shear that raises a seed gcd
  from `D` to `D*p` is nonminimal by construction, and the GGV5 interface
  cannot be applied to it without a separate arbitrary-standard-pair
  bridge."
- One-way semantics: "Emptiness of every correctly covering terminal system
  is a sufficient route; **nonemptiness of such an over-approximating system
  does not construct a Keller pair and does not falsify `3P-E31`**."

So a complete proof of `3P-E31` for all `(p, gamma)` excludes **one starting
edge direction, one-edge chains only, from `A0 = Corner(3u,1,3v)`, for gcd
values `3p` with `p = 3 mod 4`, `p >= 7`, for the selected globally minimal
pair**.  It leaves multi-edge chains, other starting edges, other gcds,
nonminimal pairs, `G2-PSC`, `G2-BD`, off-axis/post-jump coverage, and the
absent topological-degree ceiling.  Its distance to JC2 is not shortened by
its success.

**What should run before the bridge is settled: the preflight, and nothing
downstream of it.**  My reasons, and I want them held to a lower standard of
enthusiasm than the three reports':

- The preflight's *negative* outcome is the informative one and is the
  cheap one: "bandwidth or rank grows after every legal regrading" kills a
  named Noetherian mechanism for a few emitter runs, and no bridge is needed
  to learn it.
- Its *positive* outcome is a structural fact about the only known cofinal
  necessary-chain family, worth having on the record regardless of what the
  bridge eventually says.
- Order two's Connection 2 ("proof-side and disproof-side growing-state
  problems") and Fable's disproof bottleneck #1 (effectivizing the
  fixed-support finite-death theorem) both want the same *tooling*: affine
  exponent forms, shift maps, sparse row modules, exact recurrence
  certificates.  I record honestly that this transfer is **methodological
  and prior-calibrating, not mathematical**: a growth verdict on the
  prime-ray family implies nothing about AS support growth.  Nobody should
  bank the transfer as evidence.

What must **not** run before the bridge: any attempt to prove `3P-E31` as a
campaign deliverable, any regrading that uses a nonminimal source shear, and
any emission of complete systems rather than the smallest terminal block.

### 3.7 All-outcome interpretation

- **Stable band per `mu_3` class + polynomial interpolation in `Q[p,gamma]`
  + a nonzero terminal residual on the admissible lattice.**  A symbolic
  identity to be *proved* over `Q[p,gamma]`, not interpolated into
  existence.  Then `3P-E31` follows **for this family at this interface
  only**; file it under the §3.6 ceiling in the same commit.
- **Stable band, zero residual.**  Test for a licensed degree reduction
  instead of emptiness (order two's outcome; keep it).
- **Stable band with a finite exceptional factor.**  Route its exact integer
  roots as a finite exceptional list; do not discard congruence strata.
  Note that the `mu_3` split will make some "exceptional" strata artifacts
  of the residue class — check the class before calling a root exceptional.
- **Bandwidth or minimal recurrence order grows across `S^3`.**  The
  bounded-Ore/strip mechanism is dead for this family.  Record the first
  growth invariant.  Do **not** return to literal prime enumeration (the
  promoted arithmetic already retired it) and do **not** buy a larger prime
  farm.
- **Nonempty emitted terminal system.**  Refutes the proposed emptiness
  certificate only.  It neither falsifies `3P-E31` nor constructs a Keller
  pair.  This must be printed in the emitter's own output banner, not left
  to a reader.
- **The `mu_3` classes have genuinely different bandwidth.**  Then the two
  classes are separate families and the "one strip module" framing is
  wrong; report the split rather than averaging over it.

### 3.8 Dependency / claim firewall

```text
ALLOWED:  promoted arithmetic 2f5859cb... / review 7f3fd203... at the
          globally-minimal necessary-chain interface; exact GGV5
          globally-minimal standard-pair hypotheses; source-hashed emitters.
FORBIDDEN:
  (i)   any nonminimal source shear anywhere in the regrading;
  (ii)  reading system nonemptiness as evidence about JC2 in either
        direction;
  (iii) publishing a `3P-E31` result without the §3.6 ceiling attached in
        the same artifact;
  (iv)  a separate `mu_3` card, lane, or budget line;
  (v)   fitting a recurrence on p = 7, 11 (or on "common gamma" across
        7,11,19) and reporting the fit as evidence;
  (vi)  interpolating a symbolic identity and treating the interpolation as
        the proof.
```

### 3.9 Stop rule

Stop at §3.5 step 1 if the emitter's index set is not determinable from its
own output — that is a source-typing defect and outranks the experiment.
Stop at step 4 if bandwidth grows across `S^3` in either class.  Stop after
the `p = 31` holdout if the fitted recurrence does not predict it.  Under no
outcome does this claim license a larger prime farm, a monolithic system
emission, or work on `3P-E31` as a proof deliverable.

---

## 4. The one genuinely unique composite that survives

Everything above that survives audit is the **same lemma used twice, and
used differently than proposed**.

> **Isotypic certificate calculus.**  Let a finite abelian `G` with `|G|`
> invertible act diagonally on the working ring.  For every emitted
> certificate `m = sum_i c_i r_i` with semi-invariant data, the lemma of
> §1.2 yields (a) a **descended certificate** with cofactors in a single
> isotypic component, and (b) for every non-target character `theta`, an
> exact identity `sum_i pi_{theta*chi_i^{-1}}(c_i) * r_i = 0`.

Client 1 is `G = Z/2` acting by `rho -> -rho` on the actual-total landing
charts (claim 1).  Client 2 is `G = mu_3` acting on the exponent residues /
`gamma`-lattice of the prime-ray strip module (claim 3).  One lemma, one
implementation, two lanes — and it also subsumes the already-charged
affine-Faber parity step (`three odd rows (R1,R3,R5) ... Parity then forces
R7 = 0`), which becomes an instance rather than a one-off.

**The part no report proposed, and the part with the best cost/benefit, is
(b): the non-target components as a fail-closed validator.**  Both Fable and
root reach for the isotypic split to *obtain a free theorem*; I have argued
in §1.4 and §3.6 that in both cases the free theorem is either already
implied or capped by an unbuilt bridge.  But (b) costs essentially nothing —
the producer already expands `sum_i c_i r_i`; tracking the isotypic
decomposition of that same expansion is marginal — and it is **sensitive**:
a cofactor solved by a Gröbner/syzygy engine that did not respect the
symmetry will generically violate `sum_i pi_theta(c_i) r_i = 0`, while
satisfying the main identity is exactly what the engine optimized for.  It
is therefore a control of the kind the campaign says it wants: one that can
*fail* and thereby certify that the positive result is not an artifact.

Concretely, and in the campaign's own idiom: add `parity-descend` to Fable's
certificate ledger (§5 of the fable5 report) but **specify its contract as
validate-then-descend, with the validator load-bearing and fail-closed**, and
make it the first consumer of V19's 26 cofactors after V19's own validator
and hostile review.  Marginal cost near zero; it is the cheapest new
negative control available this round.

Two smaller items also survive as unique output of this audit:

- **Lemma AS-TRI** (§2.4), derived-here and unreviewed: no exact integral
  AS109 lift has `deg_y B <= 1`.  Small, exact, independent of the charged
  two-sided no-gos, and it doubles as a worked positive control for the
  integral-shear ladder.
- **The `mu_3` sample arithmetic** (§3.4): `p = 7, 11` supply at most one
  shift step per residue class, `p = 19` is the minimum fitting sample and
  not a holdout, and the viable design is `p in {23, 31}`.  This changes
  what two of the four reports would have emitted.

---

## 5. Items I decline to promote despite multi-report agreement

Recorded explicitly, per the round's instruction.

- **"The floor-12 pincer couples two live programs" (fable5 §3, td6 Card C,
  echoed by root §4 and order2 §4).**  The coupling that is real is free and
  the coupling that is paid duplicates a null experiment (§2.3, §2.6).
  Agreement here reflects that all four lanes noticed the same salient pair
  of numbers, not that anyone checked the max-9 record.
- **"Raise avenue 1 because the `3p` family is a structured cofinal test
  bed" (all four reports).**  The raise is defensible as a *research
  allocation*, and I do not contest it.  But three of four reports state the
  scope firewall in one clause and then describe the family as "the
  campaign's only structured cofinal test bed" (fable5) or "the first known
  cofinal necessary-chain family" (order2) — phrasings that will be read
  later as if cofinality had been established for the *counterexample
  problem* rather than for one edge direction inside a selected-pair
  interface.  §3.6 is the sentence that must travel with the raise.
- **"V19 certificates make Lean packaging near-free" (fable5 avenue 46
  raise).**  Correct in principle and outside this audit's scope; noted only
  to record that I did not verify it and that `jc2-lean` was not accessed.
- **The `PROJ-IRR` / weighted-DVR-selector / one-object-atlas cluster
  (root Card A, td6 Card A, fable5 card 3).**  Not in my assigned scope.  I
  note only that these three are *also* substantially the same object viewed
  three ways — a global homogeneous presentation from which the six charts
  are localizations — and that a future dedup pass should treat them
  together rather than funding three cards.  I make no verdict on them here.

---

## 6. Scope discipline of this submission

- I promoted nothing, closed no chart, and changed no lifecycle state.
- Exact-theorem content is cited at its recorded scope: T1 `7eda0a46...` /
  `d9522acb...`; the AS109 Hensel bridge as a conditional; T3
  `c76f26a6...` / `430ffa3c...`; T4 `30cb45cc...` / `2951856c...` read as
  a checksum pending Z1; T5 `d303bf76...` / `e2ddc5b5...`; `T-rs`
  `52b59e8d...` at `D_+(rs) intersect D(k)` with its explicit V9
  provenance dependency; prime-ray `2f5859cb...` / `7f3fd203...` at the
  globally-minimal necessary-chain interface with its firewall.
- **Lemma AS-TRI and the integral-reduction valuation criterion (§2.4,
  §2.5) are derived here by hand and are unreviewed.**  They are not
  licensed for composition until they clear the ordinary producer/hostile
  review gate.  No other claim in this document depends on them.
- The §2.3 floor-13 conditional is stated as a conditional with both
  hypotheses explicit; hypothesis (i) is currently at checksum tier and
  hypothesis (ii) is open.
- Verdicts, firewalls, discriminators, all-outcome tables, and stop rules
  are given per claim in §§1--3; the unique surviving composite is §4.
- No web access, no AWS mutation, no heavy local computation, no
  `jc2-lean` access.  Only this file was written.
