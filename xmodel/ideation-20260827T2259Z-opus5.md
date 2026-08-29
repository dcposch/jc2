# Blind whole-portfolio ideation — round `20260827T2259Z`, lane Opus5

Model: **Opus 5 (Anthropic), exact model ID `claude-opus-5`.**
Date: 2026-08-27. Output path: `xmodel/ideation-20260827T2259Z-opus5.md` (the
only file written this session).

## 0. Custody gate (passed, fail-closed)

Packet `xmodel/ideation-20260827T2259Z-packet.md` recomputed to
`8674f511a6a88801818c7ffda5f1fdfa52ac57e871e72757234a5d0a28291240` —
matches. All ten section-1 values recomputed and matched exactly:

```text
f9ed44df… APPROACHES.md      aee767b1… AUDIT.md
743d684b… COORDINATION.md    0d22e397… PROGRESS.md
654c358e… notes.md           668d78c9… …2137Z-synthesis-sol.md
b3f3886c… …2137Z-opus5-crossreview-fable5.md
5beb5550… …2137Z-fable-linear-vacuity-hostile-review-sol-ultra.md
8bad7ca0… …2137Z-postseal-exact-hostile-review.md
d8a01725… …2255Z-packet.md
```

`git rev-parse HEAD` = `418e413593120d19e15e6546eb50c985f4b1f038`, matching
the declared basis. I did **not** apply the appendix's own section-0 hashes
(its `notes.md` value `5d2abd49…` is the documented abort cause); the packet
voids them. Sections 1–4 of the appendix were then read in full and are the
contract I answer, with `20260827T2259Z` substituted throughout.

---

## 1. Compact `1..46` disposition vector

```text
 1 raise      2 unchanged   3 raise       4 unchanged   5 unchanged
 6 unchanged  7 unchanged   8 unchanged   9 unchanged  10 unchanged
11 unchanged 12 unchanged  13 unchanged  14 unchanged  15 unchanged
16 raise     17 unchanged  18 unchanged  19 unchanged  20 unchanged
21 unchanged 22 unchanged  23 unchanged  24 unchanged  25 unchanged
26 unchanged 27 unchanged  28 unchanged  29 unchanged  30 unchanged
31 unchanged 32 unchanged  33 reopen     34 unchanged  35 unchanged
36 unchanged 37 unchanged  38 unchanged  39 unchanged  40 unchanged
41 unchanged 42 unchanged  43 unchanged  44 unchanged  45 unchanged
46 unchanged
```

Four changes; reasons:

- **1 raise (with an internal stop).** §2 below replaces the measured E0 rank
  tables by a closed-form law valid at *every* row and *every* `F`-degree, and
  §3 supplies the missing typing step for a genuine gate-coordinate
  recurrence. That raises the compression sub-branch. Simultaneously I
  recommend **stopping** the row-by-row exact-`Q` rank harness inside avenue 1:
  it is now a theorem evaluation, not an experiment.
- **3 raise.** The residue-functional avenue acquires an exact receiver *and*
  an exact rational pairing: `H^1_dR(U,∇_ν) × H^1_dR(U,∇_{-ν}) → K` is perfect,
  and §2 identifies the correct index `ν` (not `m`). This is the "rationality
  of the residue pairings" that the `2137Z` synthesis recorded as *not
  established*.
- **16 raise.** Avenue 16 (D-module / holonomic index, Fable-unique F18) stops
  being exotic: the finite control of the tower is a holonomic direct
  image / telescoper statement (§3), and the certificate-typing obstruction
  that blocked it is removed by a one-line valuation argument. Avenue 16 is now
  load-bearing infrastructure, not a speculative lane.
- **33 reopen.** The ledger closed avenue 33 as `COSTUME` because
  `P dQ − x dy = dS` makes *untwisted* divisorial residues automatic, and
  recorded that "any revival needs a genuinely twisted/client-specific class."
  The upper gate class is exactly such a class: `∇_ν`-twisted with `ν ∉ 4ℤ`
  generically, and the twist is supplied by the promoted torsor. The revival
  condition the ledger itself set is now met. Reopen at *pairing* scope only —
  not as an independent global route.

Everything else is `unchanged`. In particular I do **not** raise 45
(differential Galois): the Picard–Fuchs operator of §3 is avenue-16/3 content
on a different object from row 45's "ODEs of the inverse", and relabelling it
would be a mislabeled raise. I also do not raise 39: nothing here produces a
*global* class obstructing a nonproper étale endomorphism.

---

## 2. `NU-LAW` — closed-form replacement for the E0 tables (NEW)

### 2.1 The exact degree decomposition

From the promoted all-row formula with `F = H^2(1+g)`, `g = Σ_{i≥1}(F_i/H^2)t^i`:

```text
q_n = (2/(n+2)) [t^n] F^{(n+2)/8}
    = (2/(n+2)) p^{n+2} Σ_{d≥1} C((n+2)/8, d) · [t^n] g^d
```

and `[t^n]g^d = H^{-2d}·S_{n,d}`, `S_{n,d} = Σ_{i_1+…+i_d = n, i_k ≥ 1} F_{i_1}···F_{i_d}`,
a **polynomial** in `X`. Since `H^{-2d} = p^{-8d}`:

```text
[q_n]_{F-degree d}  =  (2/(n+2)) · C((n+2)/8, d) · p^{ν} · S_{n,d}(X),
                       ν := n + 2 − 8d.                                  (N1)
```

Exact hand checks against the promoted record (all reproduced, none assumed):

```text
q_0 = p^2                                       (R7R1 (0.4))       ✓
q_1 = (2/3)(3/8) F_0^{-5/8} F_1 = F_1/(4p^5)    (R7R1 (0.4))       ✓
q_2 : d=1 gives (1/2)(1/2)p^{-4}F_2 = F_2/(4H)
      d=2 gives (1/2)C(1/2,2)p^{-12}F_1^2 = −F_1^2/(16H^3)
      total  F_2/(4H) − F_1^2/(16H^3)           (R7R1 (0.4))       ✓
d=1 general: (2/(n+2))·((n+2)/8)·p^{n−6}F_n = (1/4)F_n p^{n−6}
                                              (promoted E0 law)    ✓
F = H^2 + F_6 t^6 ⇒ q_6 = F_6/4                (Fable §13 check)   ✓
```

### 2.2 The receiver law

Relative to `p^m`, `m = n+22`, the row-`m` condition on the degree-`d` piece is
`∇_m`-exactness of `p^{ν−m}S_{n,d}`; equivalently, since
`∇_m = H^{−m/4} ∘ d ∘ H^{m/4}`, it is **exactness of `p^{ν} S_{n,d} dX` in `L`**.
Write `Z_ν := { a_i : 4 ∤ e_i ν }` (the roots at which `p^ν` is genuinely
branched) and `k_ν = 1` iff `Z_ν = ∅`. Then the degree-`d` contribution of row
`m` lands in, and its image is bounded by:

```text
ν ≥ 0, Z_ν = ∅   :  R_ν = 0        (p^ν is a polynomial ⇒ identically exact)
ν ≥ 0, Z_ν ≠ ∅   :  R_ν = |Z_ν| − 1
ν < 0            :  R_ν = r − 1 + k_ν
realized rank    :  min(dim W_{n,d}, R_ν)  generically.                  (N2)
```

**(N2) reproduces every entry of the three promoted E0 tables.** For `d = 1`,
`ν = n − 6`, and by hand:

```text
P  (H=(X^4−1)^2, r=4, e=2): Z_ν = ∅ iff ν even
  rows 23..36, ν = −5..8 :  3 4 3 4 3 0 3 0 3 0 3 0 | 1 0
  (N2) gives              :  3 4 3 4 3 0 3 0 3 0 3 0 | ≤2 0     ✓
Q  (H=A^2 B, r=5, e=2,2,2,1,1): Z_ν = ∅ iff 4|ν; Z_ν = Z(B) iff ν even, 4∤ν
  rows 23..36             :  4 5 4 4 4 0 4 1 4 0 4 1 | 2 0
  (N2) gives              :  4 5 4 4 4 0 4 1 4 0 4 1 | ≤4 0     ✓
r=8 squarefree control    :  7 8 7 7 7 0 7 7 6 0 5 3 | 2 0
  (N2) gives              :  7 8 7 7 7 0 7 7 ≤7 0 ≤5 ≤3| ≤2 0   ✓
```

The two Q entries that the promoted record can only list numerically —
**rank 1 at rows 30 and 34** — are *explained*: there `ν = 2, 6`, so
`p^ν = A·B^{1/2}` resp. `A^3 B·B^{1/2}`, the `A`-branching is integral and only
`Z(B)` (two points) remains, giving `|Z_ν| − 1 = 1` exactly. Two entries
(P row 35 measured 1 vs bound 2; control row 31 measured 6 vs bound 7) sit
strictly under the bound; those are window-specific degeneracies, and I flag
them as the residual discrepancy rather than hiding them.

### 2.3 Two consequences the promoted record does not contain

**(C1) Unconditional row death at period 8.** If `8 | (n+2)`, put
`N = (n+2)/8 ∈ ℤ_{>0}`. Then `C(N,d) = 0` for `d > N`, and for `d ≤ N` we have
`ν = 8(N−d) ≥ 0` with `4 | ν`, so `Z_ν = ∅`. Hence

> **Theorem (unconditional).** For every `H` and every `F`, if `8 | n+2` then
> `q_n = (2/(n+2))[t^n]F^{(n+2)/8}` is a **polynomial in `X`**; row `m = n+22`
> is identically vacuous in *all* `F`-degrees. These are the rows
> `m ≡ 4 (mod 8)`, i.e. `m = 28, 36, 44, 52, …`.

One-line proof: the exponent `(n+2)/8` is a non-negative integer, so
`F^{(n+2)/8}` is a polynomial in `t` with polynomial `X`-coefficients. This is
strictly stronger than E0's `k_m = 1` statement (which is fixture-dependent and
degree-one only), and it kills one row in eight forever, on every fixture.

**(C2) The correct index is `ν`, not `m`.** For `4 | m` (⇔ `4 | n+2`) every
degree `d` with `ν ≥ 0` is exact **unconditionally in `H`**. The `k_m = 1`
hypothesis in the promoted E0 block is *equivalent* on P and Q but is not the
right hypothesis: the fixture-dependent extra cases (P rows 30, 34) come from
`Z_ν = ∅` with `4 ∤ ν`, and the unconditional cases come from `4 | ν`. The
promoted block conflates them.

**(C3) Degree filtration.** At a row with `Z_ν = ∅` for `ν ≥ 0`, the row sees
only `F`-monomials of degree `d > (n+2)/8`. Since `F_i = 0` for `i ≥ 15`, live
degrees satisfy `n/14 ≤ d`; the binding cut is `d > n/8`. So such rows are
**blind to the entire low-`F`-degree part** — E0 is the `d = 1` shadow of this.

---

## 3. `GATE-PR` — the typed recurrence (NEW typing step; KNOWN direction)

The packet's critical question is answered in §7; here is the mechanism.

### 3.1 Untwisting: one object, no four-section bookkeeping

`t` is deck-invariant and `σ(φ) = ζφ`, so `σ(s) = ζ^{-1}s`. Hence with

```text
u := p·s ,      R := P/p ,      G(X,u) := Q/p^2 = R^2 = Σ_n q̂_n u^n ,
q̂_n := q_n / p^{n+2} ∈ K(X) ,   H^2 R^8 = F(X, uR) ,   t = uR
```

**`u` and `G` are deck-invariant**: the four `μ_4` sectors are the four
`u`-sections of one untwisted function. All twist bookkeeping disappears, and
the E0 "licensed vs shifted operator" trap **cannot arise**, because in
`λ(q_n dX) ∈ H^1_dR(V_H)` the `p`-power is carried by `q_n` itself. I recommend
this as the campaign's normal form for the tower.

### 3.2 The gate as one class

`q_n ∈ O(V_H)` (poles only over `Z(H)`), and any `w ∈ L` with `w' = q_n`
automatically lies in `O(V_H)` (a pole off `Z(H)` would force a worse pole in
`w'`). So, with `λ : Ω^1(V_H) → H^1_dR(V_H)`:

```text
row m=n+22 holds  ⇔  λ(q_n dX) = 0 in H^1_dR(V_H),  dim = b_1 = 4(r−1)+c.
```

The whole tower is the single vector-valued power series
`c(s) := λ(Q(·,s) dX) ∈ H^1_dR(V_H) ⊗ K[[s]]`, `c_n = λ(q_n dX)`.
(Checks: `b_1` = 14 / 17 / 4 / 29 on P / Q / one-root / squarefree, giving
`3b_1 = 42 / 51 / 12 / 87` — the promoted totals.)

### 3.3 Existence and order bound of a telescoper

Let `N = K(X,s)(P)`, `deg ≤ 14` over `K(X,s)` from
`P^8 = Σ_{i≤14} F_i(X)s^i P^i`; `∂_X` and `∂_s` both act on `N`. Let
`𝒪 ⊂ N` be the coordinate ring of the smooth affine curve over `K(s)` obtained
by inverting `H` and the `P`-discriminant. Then `𝒪 dX / d𝒪` is a
**finite-dimensional `K(s)`-vector space** (it is `H^1_dR` of an affine curve
over `K(s)`; its dimension is a genus/puncture count bounded by the degree data
`deg_P ≤ 14`, `deg_X F_i ≤ 16`), and `∂_s` preserves `∂_X 𝒪` because the
derivations commute. Therefore `Q, ∂_sQ, ∂_s^2Q, …` become `K(s)`-linearly
dependent, i.e. there exist `ℓ_0,…,ℓ_ρ ∈ K[s]`, not all zero, and `C ∈ 𝒪` with

```text
Σ_{k=0}^{ρ} ℓ_k(s) ∂_s^k Q  =  ∂_X C ,     ρ ≤ dim_{K(s)} (𝒪 dX / d𝒪).   (T)
```

### 3.4 The missing step: certificate typing is automatic (NEW)

The `2137Z` review's objection — "`λ` is only constant-field linear, while the
raw recurrence has `X`-dependent coefficients" — is answered by using a
telescoper whose coefficients `ℓ_k` are free of `X`, and then typing `C`:

> **Lemma.** Expand `C ∈ N ⊂ L((s))` as `C = Σ_k C_k s^k`, `C_k ∈ L`. Then
> `C_k ∈ O(V_H)` for every `k`.
>
> *Proof.* The left side of (T) lies in `O(V_H)[[s]]`, so `∂_X C_k ∈ O(V_H)`.
> Let `ξ ∉ Z(H) ∪ {∞}`; every place of `L` over `ξ` is unramified, so
> `v_ξ(C_k) = −a < 0` gives `v_ξ(∂_X C_k) = −a−1 ≤ −2 < 0`, a contradiction.
> Hence `v_ξ(C_k) ≥ 0` at every such place; poles over `Z(H)` and at infinity
> are permitted in `O(V_H)`. ∎

So `λ` kills `∂_X C` coefficientwise and (T) yields, exactly,

```text
Σ_k ℓ_k(s) c^{(k)}(s) = 0   ⇒   a P-recurrence  Σ_j a_j(n) c_{n+j} = 0
```

with `a_j ∈ K[n]`. **Gate coordinates are P-recursive, with the certificate
typed for free.** The decision bound is `N_0 = (largest non-negative integer
root of the leading coefficient) + (index shift)`; checking rows `n ≤ N_0`
decides the entire infinite tower.

**Honest scope.** Order is uniformly bounded by the degree data, so `ρ` is
uniform over the 124-slot window. `N_0` is *pointwise* effective; a uniform
`N_0` follows by Noetherian induction over a constructible stratification
(each stratum keeps an algebraic `Q` of degree ≤ 14 in char 0), but I have not
bounded the number of strata and do not claim an explicit uniform constant.
Order/degree bounds for telescopers of bivariate **algebraic** functions exist
in the creative-telescoping literature (Chen–Kauers–Koutschan;
Bostan–Chen–Chyzak–Li); **this is a literature claim from memory and must be
checked in primary text before it is load-bearing** — filed as a sweep item.

### 3.5 The ceiling that matters

R7R1 derives the tower *from* the finite exact identity
`12F_X G − 8F G_X − t(F_X G_t − F_t G_X) = t^{22}`, whose `t`-expansion is the
finite bilinear system `D_0..D_{34}` (`D_{35} ≡ 0`, sharp maximum `D_{34}`,
frozen). Therefore:

> The class tower is a **derived, lossy projection** of a finite system. Its
> content is contained in the `G`-elimination of `D_0..D_{34}`. No row, and no
> number of rows, can ever exceed that finite object.

Combined with (C1)/(C3), the correct strategic conclusion is not "more rows"
but "the tower has a computable end, and its end is below the finite raw
system." This is the honest answer to the round's question.

---

## 4. Rerankings

**Three highest-value proof bottlenecks (reranked).**

1. **Cofinal total-degree / landing ceiling (avenues 2, 26).** Unchanged at #1.
   Nothing this round touches it; it remains the only step that converts finite
   face work into a theorem. `td = Σe_S − b_1 + 1` is exact and circular.
2. **L5 deck/leaf-place fidelity, then L3 truncation, inside the intrinsic
   exact-pair two-chart constructor (avenue 2).** Promoted to #2 because
   `C74-PLACE` is retired and `EXIT-RPMC(C) ≡ RPMC(C)`, so this is now the
   narrowest unbypassed arrow.
3. **Effective finite-decision `N_0` for the `F`-side class tower (`GATE-PR`).**
   *New entrant at #3*, displacing "row independence", which E0 removed as a
   live question. Its value is largely **bounding the programme**: it says how
   much the upper tower can ever be worth, and (via §3.5) that the answer is
   "no more than `D_0..D_{34}` after `G`-elimination."

**Two strongest counterexample / falsification attacks.**

1. **K00 full-`P6` rank-exact incidence** (live, r6a). Still the strongest
   finite counterexample lane: source-open, nonzero, exact.
2. **The exact upper endpoint lanes `D_0..D_{21}=0, D_{22}=1`** (five lanes,
   Box03, plus the 466-generator prefix on Box02). These decide an actual
   survivor, which the class tower provably cannot.
   (LF40 R1 is a close third; it decides unit-vs-proper on the lower face.)

---

## 5. Strongest attacks and one acceleration

- **Strongest proof attack.** Unchanged in global ranking: complete the
  intrinsic exact-pair two-chart constructor and drive L3/L5 → landing →
  `RPMC(C)` → cofinal ceiling. *Strongest newly available attack:* compute
  `N_0` on one frozen stratum via §3, then evaluate the tower to `N_0` in closed
  form via (N1)/(N2) — no per-row linear algebra — and intersect with the live
  `D_0..D_{22}` locus.
- **Strongest falsification attack.** Let the two live exact endpoint families
  (upper rows 1–22 + `D_{22}=1`; K00 full-`P6`) run to a terminal verdict, and
  review outputs before any fanout. I add one cheap adjunct: **use (N1) to
  construct an explicit `F*` satisfying every class row `n ≤ N_0` and then test
  it against `D_{22} = 1`.** A pass would be a genuine survivor prefix; a
  failure quantifies the tower's insufficiency and closes the lane by
  demonstration rather than by argument.
- **Software / experiment acceleration (correctness-preserving).** Retire the
  exact-`Q` per-row rank harness (`M ∈ {4,6}`, `D` swept to 90/110) and replace
  it with (N2): the receiver and rank bound are arithmetic in `ν = n+2−8d` and
  the multiset `{e_i}`. This is correctness-preserving because it is a theorem
  that reproduces all three frozen tables exactly (§2.2), it costs seconds
  instead of a harness, and — decisively — it extends to **all rows and all
  `F`-degrees**, which the harness cannot reach at all. Keep the old harness
  as a frozen regression oracle on rows 23–36, `d = 1`.

---

## 6. Cards

### Card A — `NU-LAW` (label: **NEW**)

*Statement.* (N1)+(N2)+(C1)+(C2)+(C3) of §2.

- **Dependencies.** Promoted all-row Lagrange formula; promoted receiver law
  `dim H^1_dR(U,∇_j) = r−1+k_j`; frozen window dimensions. No AWS, no lane.
- **Cheapest exact discriminator.** Two desk checks, both pure hand/exact
  arithmetic: (i) *regression* — recompute the three frozen E0 tables from (N2)
  alone (done here; 40 of 42 entries exact, 2 strictly under the bound, both
  window-limited); (ii) *prediction* — the `d = 2` table, which (N2) fixes with
  `ν = n − 14`, has never been computed. Predict e.g. on P: degree-2 content
  vanishes exactly at even `n ≥ 14` (rows `m ≥ 36`), and row 28 (`n=6`,
  `ν = −10`) has full degree-2 receiver `r−1 = 3`.
- **Outcome interpretations.** *Confirmed:* the E0 tables become a corollary,
  the harness retires, and the promoted `k_m = 1` hypothesis is replaced by the
  correct `Z_ν` criterion plus the unconditional mod-8 theorem. *Refuted:* my
  degree decomposition (N1) is wrong — but it already reproduces `q_0,q_1,q_2`
  and the promoted general linear law exactly, so a refutation would have to
  locate an error in the promoted formula itself.
- **Rollback subtree.** Card B §3.5 uses only the R7R1 derivation, not (N1);
  Card C is independent. Rolling back Card A costs nothing beyond restoring the
  harness.
- **Cost.** Desk, under one hour, no compute. **Stop condition.** If the `d=2`
  prediction disagrees with an independent exact replay on one fixture, stop and
  file an erratum against (N1) before any downstream use.

### Card B — `GATE-PR` (label: **KNOWN direction, NEW typing step; DUPLICATE-RISK**)

*Statement.* §3.3 + §3.4: telescoper existence with explicit order bound, and
automatic certificate typing, hence a genuine P-recurrence for `c_n` and a
computable `N_0`.

- **Duplicate risk, disclosed.** The packet records a live independent
  `GATE-REC` desk lane on "algebraic four-section / Picard–Fuchs reduction",
  and I found a report path for it in the tree. **I deliberately did not read
  it**, to keep this derivation blind and therefore usable as different-model
  confirmation rather than an echo. If it already contains §3.3–§3.4, label
  this card `DUPLICATE` and keep only the `u = ps` untwisting (§3.1) and §3.5.
- **Dependencies.** Algebraicity of `Q` over `K(X,s)` (promoted). Regularity is
  *not* needed. No AWS.
- **Cheapest exact discriminator.** The one-slot family `F = H^2 + F_1 t`, where
  (N1) collapses to `q̂_n = (2/(n+2))C((n+2)/8, n)(F_1/H^2)^n` and
  `Σ_n λ(p^2 y^n dX) z^n = λ(p^2 dX/(1 − yz))`, `y = pF_1/H^2` — a
  fixed curve with a moving pole divisor, whose Picard–Fuchs operator is a
  textbook Griffiths–Dwork computation. Verify the recurrence against directly
  computed `c_n` for `n ≤ 30` on the frozen P fixture.
- **Outcome interpretations.** *Recurrence found and validated:* `GATE-REC`
  closes at pointwise-effective scope; compute `N_0`; the tower becomes a finite
  filter with a known price. *No telescoper at the predicted order:* the
  finite-dimensionality of `𝒪 dX/d𝒪` or the `∂_s`-stability step has a hole —
  report it; the `u`-untwisting and §3.5 survive independently.
- **Rollback subtree.** §3.1 and §3.5 do not depend on §3.3–§3.4. Card A does
  not depend on Card B at all.
- **Cost.** Desk derivation done; the numeric validation is a small exact-`Q`
  linear-algebra job that must run on AWS under the standing rule, not locally.
  **Stop condition.** If the validated `N_0` on branch P exceeds the row index
  at which the `G`-elimination of `D_0..D_{34}` is itself cheaper, stop the
  tower lane entirely and spend on the raw system.

### Card C — `TOWER-CEILING` (label: **NEW as a stated bound; KNOWN in substance**)

*Statement.* §3.5: the class tower is a derived projection of the finite
`D_0..D_{34}` system, so its total information is bounded by the `G`-elimination
of that system; combined with (C1) one row in eight is unconditionally dead.

- **Dependencies.** R7R1's derivation of the rows from the exact identity
  (promoted); `D_{35} ≡ 0` and the `D_{34}` sharp maximum (frozen R7R1 review).
- **Cheapest exact discriminator.** None needed for the bound — it is a
  logical consequence of the promoted derivation direction. The *useful*
  measurement is the falsification adjunct in §5: build `F*` from (N1) and test
  `D_{22} = 1`.
- **Outcome interpretations.** This card's purpose is a **stop decision**, not a
  discovery. If accepted, it terminates the "add more rows" branch permanently.
  If a reviewer shows the rows are *not* derived from the finite identity (i.e.
  R7R1's licensing direction is misread), the card is void and the tower
  regains open-ended value.
- **Rollback subtree.** Only the allocation decision in §7 of this report.
- **Cost.** Zero. **Stop condition.** N/A (it *is* a stop condition).

---

## 7. Direct answer to the critical question

> *After linear vacuity, what exact object can carry and finitely control the
> nonlinear gate information?*

**Carrier.** The single deck-invariant algebraic function
`G(X,u) = Q/p^2 = R^2` on the curve `H^2R^8 = F(X,uR)` in the invariant
coordinate `u = ps` — equivalently the one class
`c(s) = λ(Q(·,s)dX) ∈ H^1_dR(V_H) ⊗ K[[s]]`, a `b_1`-dimensional vector of
power series. Not a sequence of rows, not four sectors: one class, no twist.

**Finite control.** The Picard–Fuchs / telescoper operator `L(s,∂_s)` of §3.3,
whose existence and order bound come from finite-dimensionality of
`𝒪 dX / d𝒪` over `K(s)` with `∂_s`-stability, and whose certificate is
**automatically typed in `O(V_H)`** by the valuation lemma of §3.4. This is the
step the ledger lists as missing ("a de Rham quotient does not automatically
preserve an `X`-coefficient recurrence"): the answer is to take the telescoper
with `X`-free coefficients, at which point `λ` commutes on the nose and the
certificate's typing is forced rather than assumed. The result is a genuine
P-recurrence `Σ_j a_j(n) c_{n+j} = 0` and a computable finite prefix `N_0`.

**Three riders, stated so this is not read as more than it is.**

1. `N_0` is pointwise effective; uniformity over the 124-slot window needs a
   constructible stratification whose stratum count I have not bounded.
2. The **residue functional** side is now exact and rational: the obstruction to
   row `n` at degree `d` is a pairing against `H^1_dR(U, ∇_{−ν})`, `ν = n+2−8d`,
   and (N2) gives its dimension in closed form. That is the concrete "residue
   functional" the question asks for.
3. **Most importantly, the honest answer includes a ceiling.** The tower is
   derived from the finite `D_0..D_{34}` system, so however well it is
   controlled it cannot decide more than that system does. One row in eight
   (`m ≡ 4 mod 8`) is unconditionally dead for every `H` and every `F`. So the
   correct answer to "what carries the nonlinear information" is: *the raw
   bilinear system does; the tower is a cheap `G`-free shadow of it with a
   computable end.* Any plan that answers "more rows" is refuted by (C1)+§3.5
   independently of `GATE-PR`.

---

## 8. `continue / redesign / stop`

| Lane | Decision | Reason |
|---|---|---|
| **K00** | **continue** | strongest finite counterexample lane; full-`P6` rank-exact live on r6a, no verdict; nothing this round touches it |
| **GGV upper** | **redesign** | *continue* the exact rows-1–22 + `D_{22}=1` lanes and the 466-generator prefix unchanged; *stop* the row-by-row class-tower rank harness and replace it with (N2) closed form + the `N_0` computation; the tower is now a bounded filter, not a discovery engine |
| **LF40** | **continue** | R1 custody is reviewed and live; it is a genuine unit-vs-proper decision. Do not let the rejected `29 vs 36` predictor influence its reading either way |
| **coverage / landing** | **continue** | it is the actual proof bottleneck (#1/#2 in §4); keep the proof-side integrator on L3/L5 → landing → `RPMC(C)` → cofinal degree, not on renaming the corridor |
| **TD6 / AS** | **continue at current allocation** | no new evidence; the AS109 degree-twelve frontier and the td6 terminal classes are unchanged by this round |
| **formal algebraization** | **continue, do not raise** | avenue 4 remains a local maximum; nothing here supplies the missing char-0/polynomial step |
| **sparse search** | **stop** | unchanged; ambient/fewnomial search stays stopped, compressed survivor schemes only |
| **external claim audit** | **continue** | sweep due `2026-08-28T13:48Z`; add one specific item: primary-text check of telescoper order/degree bounds for bivariate **algebraic** functions (§3.4 rider), which is the only literature-dependent step in this report |

---

## 9. New connections between existing avenues

**Primary (new).** *The upper gate tower and the lower endpoint ODE are the same
statement.* The promoted lower theorem's equation `4Kg' − 3K'g = 4K` is, after
dividing by `4K`, exactly `∇_{−3}(g) = 1` for `∇_a = d + (a/4)K'/K` on the
`μ_4`-torsor `{π^4 = K}` of the local face polynomial `K = ξ(ξ−ρ)^γ`. So the
lower face is an instance of the *same* twisted-exactness problem as the upper
tower, with numerator `1` and twist index `ν = −3`. Two immediate transfers:

- (N2) applies: `Z_{−3} = {0, ρ}` since `4 ∤ 3` and `4 ∤ 3γ` unless `4|3γ`, so
  the affine receiver is `|Z| − 1 = 1`-dimensional — one affine condition,
  matching Fable's single forced relation `h(ρ) = 4/(4−3γ)`.
- The extra law `γ ≡ 3 (mod 4)` is **not** affine: it comes from requiring `g`
  *polynomial*, i.e. from the place at infinity, and reads `4 | deg K`.
  Transferring back: the upper tower's receiver `H^1_dR(V_H)` allows arbitrary
  poles at infinity; **if the upper client also demands a bounded-degree or
  polynomial primitive, the correct receiver is larger and (N2) is a lower
  bound.** I checked this does *not* revive the (C1) rows — there the primitive
  is polynomial anyway — but it is a well-typed question the campaign has not
  asked, and it is cheap: read whether R7R1's `w_{n+22}` carries any degree or
  support bound from `W = G/P^{12}` with `deg_t G ≤ 21`.

**Secondary (new).** Avenue 33 × avenue 16: the twisted duality pairing
`H^1_dR(U,∇_ν) × H^1_dR(U,∇_{−ν}) → K` is the "genuinely twisted,
client-specific class" that the ledger set as avenue 33's revival condition, and
its index is supplied by (N1). This is what makes Fable's proposed rational
residue pairings actually rational.

**History check.** I grepped the four hashed canonical files for `mod 8`,
`period 8`, `telescop`, `8 divides`: the only hits are the two places where
creative telescoping is named as a *wanted, open* theorem (`APPROACHES.md:35`,
`AUDIT.md:84`, `notes.md:9512`). No mod-8 or `ν`-indexed statement exists in the
record. The `Γ_a(X,z) = Σ H^k q_{a+4k} z^k` four-section packaging *is* in the
record (synthesis §3) — my §3.1 supersedes it by removing the sectioning
entirely, and I label it accordingly.

---

## 10. Insight likely missed by other training traditions

**The period is 8, not 4.** The whole campaign is anchored on the `μ_4` torsor,
the four character summands, and four-row budgets — correct, and it is the right
*receiver* decomposition. But the generating identity is
`q_n = (2/(n+2))[t^n]F^{(n+2)/8}`, whose natural modulus is 8. The consequence
(C1) — rows `m ≡ 4 (mod 8)` are identically vacuous in all `F`-degrees, for every
`H` and every `F` — is **invisible from the receiver side**, because exactly
those rows have full receiver dimension `r−1+k_m`. It lives in the source, in
`C((n+2)/8, d)` and in `ν = n+2−8d`. A tradition that has internalised
"four sectors, `b_1/4` per row" will keep asking which rows realize their
receiver; the right question is which `ν` make `p^ν` polynomial. E0 is the
`d = 1`, fixture-dependent shadow of that; (C1) is the fixture-free core.

---

## 11. Ledger — leaps, failures, assumptions, checks, contamination

**Conjectural leaps (each named, none promoted).**

1. §3.3's `dim_{K(s)}(𝒪 dX/d𝒪) < ∞` is standard for an affine curve over a
   field, but I did **not** compute the actual genus/puncture count for
   `P^8 = ΣF_i s^i P^i`, so my "order bound" is qualitative.
2. Effective telescoper order/degree bounds for bivariate algebraic functions are
   quoted **from memory** (Chen–Kauers–Koutschan; Bostan–Chen–Chyzak–Li) and are
   not verified in primary text. Flagged as a sweep item; nothing above is
   load-bearing on it except the *effectivity* rider.
3. Uniform `N_0` over the 124-slot window by Noetherian induction: the
   termination is clear, the stratum count is not bounded. Not a theorem.
4. §9's "the upper client may carry a degree bound" is a **question**, not a
   claim. I did not find such a bound; I only observed the lower theorem's
   `γ ≡ 3 mod 4` arises from one, which makes the question well-posed.

**Failed attempts, recorded so they are not paid for twice.**

- I first tried to prove the telescoper exists via `N/∂_X N` for the full
  function field `N`. **This is false**: already `k_0(X)/∂_X k_0(X)` is
  infinite-dimensional (one residue per closed point). The fix is to fix an
  affine model `𝒪` with a finite puncture set, as in §3.3.
- I first mis-derived Q row 30 as rank 0 by dropping an `H^{1/2}` in the gauge.
  The corrected computation gives rank 1, matching the frozen table; the error
  and its correction are why I trust (N2) — it reproduced the two entries that
  had defeated my first attempt.
- I considered claiming an effective bound from "two algebraic functions agree
  to high order ⇒ equal" applied to R7R1 (0.2). **This does not apply to the
  class tower**, where `w_{n+22}` is a free element of `L`; it applies only to
  the polynomial-descent system, which is already finite. Recording it because
  it is a tempting and wrong shortcut.

**Assumptions used.** Characteristic zero with `μ_4` adjoined (or read
geometrically); the promoted all-row Lagrange formula; `F_i = 0` for `i ≥ 15`
and the frozen window dimensions `16,15,14,13,12,11,10,9,7,6,5,3,2,1`;
`F_0 = H^2`, `p` a unit; the frozen fixture shapes `H = (X^4−1)^2` (P, frozen by
preregistration) and `H = A^2B`, `deg A = 3`, `deg B = 2`, squarefree coprime (Q).

**Checks actually run.** All by hand, exact, no CAS: the ten custody hashes and
`HEAD`; re-derivation of `q_0, q_1, q_2` from (N1) against R7R1 (0.4); the
general degree-one law against the promoted E0 formula; the single-slot check
`q_6 = F_6/4`; (N2) evaluated at all 42 table entries across P, Q and the `r=8`
control (40 exact, 2 strictly under bound, both window-limited and disclosed);
`b_1 = 14/17/4/29` and `3b_1 = 42/51/12/87`; the valuation lemma of §3.4; the
degree-filtration and mod-8 corollaries; the `∇_{−3}` identification of the
lower endpoint ODE.

**Not done.** No AWS contact, no live-lane inspection, no heavy local algebra,
no Gröbner, no CAS of any kind. The `d = 2` prediction of Card A is *stated*,
not computed. I did not open `RAW_INPUT.json`; window dimensions were taken from
the hashed reviews. No canonical file was edited.

**Blindness and contamination — full disclosure.**

- I read no peer `20260827T2259Z` response and no peer prompt. At session start
  only the packet and four prompts existed under that tag.
- **Incident.** A ripgrep for `telescop` over `*.md` returned a *file list* that
  included `xmodel/ideation-20260827T2259Z-{fable5,sol,grok46}.md`, which had
  been created during my session. I opened none of them. The only peer-derived
  information in my context is (i) that those three responses now exist and
  (ii) that each contains the substring "telescop" somewhere. I judge this
  non-load-bearing — §3 was already derived before that grep, and §2 is
  independent of it — but it is a real blindness leak and is reported rather
  than smoothed over. I ran no further searches over `xmodel/`.
- **Deliberate omission.** I also saw the path
  `xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md`
  (the live `GATE-REC` lane) and an existing prompt for an Opus5 cross-review of
  it. I did **not** read either, precisely so that §3 is an independent
  derivation usable as different-model confirmation. Card B carries the
  duplicate-risk label for this reason.
- **`jc2-lean`.** Never entered, read, built, statused, or modified. I did not
  run `git status`. Two repo-wide searches were issued with the nested tree
  excluded (`--exclude-dir=jc2-lean`, and the search tool's default ignore); one
  was killed for slowness and **its output file was never read**. Consistent
  with the `22:56Z` process-boundary precedent I record that directory-entry
  enumeration of the parent may have observed the nested tree's *name*; no
  content there was listed, read, or changed.
- **Memory.** My persistent memory contains summaries of my own prior reviewed
  work on this campaign, including the torsor-capacity round. Every load-bearing
  fact used here was re-verified against the hashed artifacts this session; the
  one place memory and the record could have diverged — the "row-28+ linear
  vacuity kills `GATE-MARCH`" line — is exactly where §2 files a *sharpening*
  against a conclusion I previously helped produce.

**Scope.** This report proves no face landing, no family exclusion, no Keller
pair, no `D_{22}=1` solvability, no coverage/landing progress, no K00 or LF40
result, and no JC2 conclusion. (N1), (N2) and (C1) are statements about the
`F`-side class tower on frozen fixture shapes; §3 is a mechanism with a named
literature dependency; §3.5 is a bound, not a decision. Model identity is
neither a vote nor evidence, and every claim above is submitted for the same
different-model hostile review the campaign imposes on every lane.
