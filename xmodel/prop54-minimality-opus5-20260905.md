# SCOPE lane — Moh Prop 5.4 and minimal-degree counterexamples: does minimality force the two-point configuration?

**Lane:** `prop54-minimality-opus5-20260905` (Opus 5). Source-read + logic; no CAS beyond one
symbolic identity check; no fleet. Drivers: `box/prop54-20260905/`.

**Inputs verified** (manifest generated with `awk` from the receipt's
`charged_input_<i>_sha256=` / `_basename=` lines, checked with `sha256sum -c`; log
`box/prop54-20260905/inputs.check.log`): 5/5 **OK**, no mismatch.

---

## VERDICT — `MINIMALITY-COVERS` (for the one-point/one-place leak only)

**A plane Keller counterexample whose degrees cannot be simultaneously reduced by an
automorphism of `k[x,y]` — in particular any counterexample of minimal total degree —
NECESSARILY has Moh's configuration `M_s = n−2` with the highest homogeneous form of `g`
carrying exactly TWO distinct roots, i.e. two distinct points at infinity.** This is Moh's
Prop. 5.4 "Moreover" clause (p.183) + Lemma 5.3 (p.185), and the dichotomy they straddle is
exhaustive because the logarithmic radius `δ_i` of the smallest disc containing all roots of
`g(y)T₁^ψ(y)` satisfies `δ_i ≥ −1` **always** — proved two independent ways in §2 below, one of
them Moh's own unlabelled identity `δ_i = −1/(n−M_i−1)`, verified symbolically here.

Consequently `OPEN[PROP-5.4-MINIMALITY]` **RESOLVES AFFIRMATIVELY**: there is **no**
`OPEN[ONE-PLACE-GAP]`. The banked scope caveat 17(qqqqq)(5) / 17(eeeeee) listed **four** leaks;
this lane closes **leak (i) only** — "one-place/Abhyankar–Moh is a different program" is
**refuted for minimal counterexamples**. Leaks (ii) U-NEGATIVE, (iii) `s′>2` residual,
(iv) unproved routing maps **stand unchanged**. The scope caveat is therefore **narrowed, not
removed**; see §4.

Two precision corrections to the campaign's framing are recorded in §5 (the excluded
configuration is one **point**, not one **place**; and `[A.1]` is *not* Abhyankar–Moh).

---

## 1. The source, exactly as printed

Journal page `N` = PDF page `N−139` (74pp; `refs/moh1983_jram340_configurations_of_roots.pdf`).
300-dpi renderings of pp. 166, 179, 183, 185, 186, 194 are banked in `box/prop54-20260905/`.

### 1.1 Proposition 5.4 (p.183, PDF p.44) — verbatim

> **Proposition 5. 4.** *Suppose that `g(x, y)` is monic in `y` with `y`-degree `n > 1` and a
> tower of major discs `D_s ⫌ D_{s−1} ⫌ ⋯ ⫌ D_1` is constructed. Then the smallest disc which
> contains all roots of `g(y) T₁^ψ(y)` is the `D_i` with*
>
> > `i = max { r : V_{r+1} d_r / d_{r+1} > V_r }` .
>
> *Moreover if `δ_i > −1` then either `k[x, y] = k[T₁^ψ, g] = k[f, g]` or there exists an
> automorphism of `k[x, y]` which reduces the degrees of `T₁^ψ(f(x, y), g(x, y))`, `g(x, y)`
> and `f(x, y)` simultaneously.*

Proof structure (pp.183–185): the index `i` is where the leading coefficients `g_σ(π)`,
`T₁^ψ_{,σ}(π)` acquire more than one root; then `i = 1` yields `M₁ = −1`, so `T₁^ψ` is monic of
`y`-degree 1, an automorphism sends it to `y`, the Jacobian condition forces
`g ↦ x + polynomial in y`, hence `k[x,y] = k[T₁^ψ,g] = k[f,g]`. For `i > 1` the top weighted
form of `g` (weights `x:l`, `y:1`, `l = n−M_i−1 ≥ 2`) has a factor `aˡx − yˡ`; the automorphism
`x ↦ x + a^{−l} yˡ, y ↦ y` sends it to `aˡx`, so `deg g` drops by ≥ 1, likewise `deg T₁^ψ`, and
by `T₁^ψ = f + polynomial in g` (Prop 2.2) with
`deg T₁^ψ(f,g) = deg_y T₁^ψ = −M₁`, `deg f` drops too.

### 1.2 Definition 5.1 (p.179, PDF p.40) — the two clauses used

> (2) `V_{i+1} d_i / d_{i+1} ≥ V_i > d_i/(n−M_i)` for `i = r+1,…,s`, `V_{s+1} = d_{s+1}`,
>
> (3) `δ_i = 1 − [ (n−M_i) ∏_{j=i+1}^{s} (V_j(n−M_j) − d_j) ] / [ (n−M_s−1) ∏_{j=i+1}^{s} (V_j(n−M_{j−1}) − d_j) ]`.

`d_s = g.c.d.(n, M_1, …, M_{s−1})` (p.194). `M_s` is **defined** as *"the largest `M_i` which is
less than `n − 1`"* (Prop 5.2, p.176) — so `M_i ≤ M_s ≤ n−2` is definitional, and
`n − M_s − 1 > 0` is re-derived inside Lemma 5.2's proof (p.178:
`(n−L) ≥ (n−M_s) > (n−M_s−1) > 0`). Radii increase downward: `δ_s < ⋯ < δ_1` (p.185), distance
`= 2^{−δ}` (p.183).

### 1.3 Lemma 5.3 (p.185, PDF p.46) — verbatim

> **Lemma 5. 3.** *Suppose that `g(x, y)` is monic in `y` with `deg g(x,y) = deg_y g(x,y) = n > 1`.
> Then the smallest disc which contains all roots of `g(y) T₁^ψ(y)` is of logarithmic radius `−1`
> iff `M_s = n−2` and the highest homogeneous form of `g(x, y)` has two roots with one root
> having a multiplicity `(n/d_s) v_s` where `v_s` satisfies `d_s > v_s > d_s/2`.*

Its "Necessary" direction (p.185 foot) opens with exactly the identity of §2:
`−1 = δ_i = 1 − (n−M_i)/(n−M_i−1) = −1/(n−M_i−1)`, hence `n−M_i−1 = 1`, hence `M_s = n−2` (p.186).

### 1.4 The p.194 hypothesis — verbatim (PDF p.55, read from the image; the text layer garbles the exponent)

> *"As pointed out in Proposition 5. 4 and Lemma 5. 3 we shall only consider the case
> `M_s = n−2` and the highest homogeneous form `g(x, y)` equals `[(y − ax)^{v_s} (y − bx)^{u_s}]^{n/d_s}`
> for `a ≠ b` where `u_s = d_s − v_s`."*

Exponent is `n/d_s` (degree check: `(n/d_s)(v_s+u_s) = n`), matching Lemma 5.3's multiplicity
`(n/d_s)v_s`. This is precisely the campaign's two-point `M_s = n−2` stratum.

### 1.5 The complementary configuration — Proposition 4.3 (p.166, PDF p.27) — verbatim

> **Proposition 4. 3.** *Suppose that `deg g(x,y) = deg_y g(x,y) = n > 1`, and `M_i ≠ n−2` for
> `i = 1,…,h`. Then the highest homogeneous forms of `g(x,y)`, `T_i^ψ(f(x,y), g(x,y))` for all `i`
> with `M_i < n−2` are powers of a common linear form (i.e. one point at infinite).*

Its proof fixes the meaning of the complementary branch: with
`δ = min{ord τ : τ root of g(y)∏T_i^ψ(y)}`, *"Let us consider the possibility of `δ > −1` … The
above statement is equivalent to the degree `n` homogeneous form of `g(x, y)` being `yⁿ`"* — and
then *"Let us henceforth assume that `δ ≤ −1`"*, after which Case 1 proves `δ = −1` by
contradiction. So `δ > −1` ⟺ one point at infinity, and `δ < −1` is excluded.

### 1.6 The minimality hypothesis as Moh states it (Theorem, p.200, PDF p.61)

Theorem hypothesis (3): *"the number `M_s` is the largest one `≤ n−2`"*; and in the `≤100` search,
normalization (3): *"`J(x,y)(f(x,y), g(x,y)) = 1` and the degrees of `f(x,y)` and `g(x,y)` can not
be reduced simultaneously"*. Moh already reasons by minimality on p.200:
*"in looking for a possible counter-example for the Jacobian conjecture of the smallest possible
degrees we must assume that `d_s ≥ 3`."*

---

## 2. Exhaustiveness: `δ_i ≥ −1` always (the step Prop 5.4 does not label)

Prop 5.4 covers `δ_i > −1`; Lemma 5.3 characterises `δ_i = −1`. The dichotomy is exhaustive iff
`δ_i < −1` is impossible. Two independent proofs; both are needed only because Moh states
neither as a lemma.

**(a) Moh's own identity, made unconditional.** In Def 5.1(2) the inequality is `≥`. By the
maximality defining `i`, `V_{j+1}d_j/d_{j+1} > V_j` fails for every `j > i`, so
`V_{j+1}d_j = V_j d_{j+1}` there, i.e. `V_j/d_j` is constant on `j = i+1,…,s+1`; with
`V_{s+1} = d_{s+1}` this gives `V_j = d_j` for `j = i+1,…,s`. Substituting into Def 5.1(3), both
products factor as `∏ d_j(n−M_j−1)` and `∏ d_j(n−M_{j−1}−1)` and **telescope**:

> `δ_i = 1 − (n−M_i)/(n−M_i−1) = −1/(n−M_i−1)`.

Verified symbolically for all `1 ≤ i ≤ s ≤ 8` (36 cases, residual identically `0`):
`box/prop54-20260905/delta_identity_check.py` → `.log`, `IDENTITY_UNCONDITIONAL=True`.
**No hypothesis on the sign of `δ_i` enters the derivation** — the `δ_i > −1` supposition on
p.183 sets up the `i = 1` / `i > 1` case split, it is not used for the identity. (Lemma 5.3's
"Necessary" proof quotes the same identity in the `δ_i = −1` case, which is Moh's own
confirmation that it is not conditioned on `δ_i > −1`.) Since `M_i ≤ M_s ≤ n−2` is definitional
(§1.2), `l := n−M_i−1 ≥ 1` is a positive integer, so

> `δ_i ∈ {−1, −1/2, −1/3, …}`, i.e. `δ_i ≥ −1`, with `δ_i = −1 ⟺ l = 1 ⟺ M_i = n−2`.

**(b) Elementary, index-free.** With `g` monic in `y`, `deg g = deg_y g = n`, write
`g = yⁿ + a₁(x)y^{n−1} + ⋯ + a_n(x)`, `deg a_j ≤ j`. The Newton polygon then has all slopes ≤ 1,
so every root satisfies `ord_x τ ≤ 1`, i.e. `ord_t τ ≥ −1` in Moh's parameter (`ord_t x = −1`;
cf. p.194 eq. (8) `y = a t^{−1} + c_j + ⋯`, and p.185 `ord g(t^{−1}, πt^{δ_i}) = nδ_i`). Hence for
any two roots `ord(τ − τ′) ≥ min(ord τ, ord τ′) ≥ −1`, and the smallest disc containing them all
has logarithmic radius `≥ −1`. Equality holds iff two roots have **distinct** leading
coefficients — i.e. iff `g` has at least two distinct points at infinity. This route needs no
tower and no index `i`; it also makes Lemma 5.3's geometric content transparent.

Route (b) is the load-bearing one for the verdict (it is immune to the two bookkeeping caveats
in §5.2); route (a) is Moh's and pins the arithmetic `δ_i = −1/(n−M_i−1)`.

---

## 3. The logical chain — `MINIMALITY-COVERS`

Let `k` be a field of characteristic 0. Suppose plane JC2 fails: some `(f,g) ∈ k[x,y]²` with
`J(f,g) ∈ k*` and `k[f,g] ⊊ k[x,y]`. Choose one with **`deg f + deg g` minimal**.

1. **Minimality is inherited under `Aut k[x,y]`.** For `φ ∈ Aut k[x,y]`,
   `J(f∘φ, g∘φ) = (J(f,g)∘φ)·det Jac(φ) ∈ k*`, and `k[f∘φ, g∘φ] = φ*(k[f,g]) ⊊ k[x,y]`. So the
   image of a counterexample is a counterexample, of the degrees produced by `φ`.
2. **Normalisations are degree-preserving or degree-decreasing.** A generic linear change gives
   `deg g = deg_y g = n` and `g` monic in `y` (degrees unchanged, step 1 applies). `n > 1`:
   `n = 1` makes `g` affine-linear, forcing `k[f,g] = k[x,y]`. Replacing `f` by its first
   approximate root `T₁^ψ = f + polynomial in g` (Prop 2.2, p.185) preserves `J` and `k[f,g]` and
   does not raise `deg f`; at a minimal counterexample it therefore holds with equality, and
   Moh's "nonrestrictive assumption `f = T₁^ψ`" (p.200) is available.
3. **Trichotomy → dichotomy.** Let `δ` be the logarithmic radius of the smallest disc containing
   all roots of `g(y)T₁^ψ(y)`. By §2, `δ ≥ −1`. So either `δ > −1` or `δ = −1`.
4. **Branch `δ > −1` is impossible for this pair.** By Prop 5.4's "Moreover" clause (§1.1),
   either (a) `k[x,y] = k[T₁^ψ, g] = k[f,g]` — contradicting `k[f,g] ⊊ k[x,y]` — or (b) some
   `φ ∈ Aut k[x,y]` reduces `deg T₁^ψ(f,g)`, `deg g` and `deg f` **simultaneously**; then by
   step 1 `(f∘φ, g∘φ)` is a counterexample with strictly smaller `deg f + deg g`, contradicting
   minimality. (Equivalently: minimal total degree ⟹ Moh's p.200 normalisation (3).)
5. **Hence `δ = −1`.** By Lemma 5.3 (§1.3), `M_s = n−2` **and** the highest homogeneous form of
   `g` has exactly two roots, one of multiplicity `(n/d_s)v_s` with `d_s > v_s > d_s/2` — i.e.
   the p.194 configuration `[(y−ax)^{v_s}(y−bx)^{u_s}]^{n/d_s}`, `a ≠ b`, `u_s = d_s − v_s`:
   **two distinct points at infinity.** ∎

**Consequence for the campaign.** Write `P` for the program "(H1) ∧ (H2) + routing maps kills
every two-point `M_s = n−2` Keller skeleton". If `P` is completed, then by 1–5 no
minimal-total-degree counterexample exists; and if any counterexample existed, a
minimal-total-degree one would exist. Therefore **`P` complete ⟹ plane JC2**. The
minimal-counterexample step is the standard one and is valid here because degree is a
well-ordered `ℕ`-valued invariant and step 1 makes the reduction stay inside the
counterexample class.

**Strength note.** The chain uses only the *weak* minimality "degrees not simultaneously
reducible" (Moh p.200 (3)); minimal total degree is one sufficient way to get it. So the
conclusion also applies to every pair already normalised the way Moh's `≤100` search normalises
them — which is why the banked `≤100` work was never actually confined to a stratum it had not
justified.

---

## 4. Reconciliation with the banked SCOPE statements

17(qqqqq)(5) (2026-09-04T12:47Z) recorded: *"(H1)∧(H2) reduces the TWO-POINT `M_s=n−2` stratum
ALONG MOH'S LINE, NOT all of plane JC2 (one-place/Abhyankar–Moh is a different program;
U-NEGATIVE rows `V₂′>d₂′` are a genuine THIRD configuration; `s′>2` residual; the routing maps
are unproved)"*; 17(eeeeee) carries it forward.

| leak | status after this lane |
|---|---|
| (i) "one-place/Abhyankar–Moh is a different program" | **CLOSED for minimal counterexamples.** Refuted by Prop 5.4 + Lemma 5.3 + `δ ≥ −1` (§3). It is not a different program; Moh disposes of it inside this paper, without invoking Abhyankar–Moh. |
| (ii) U-NEGATIVE rows `V₂′ > d₂′` a "third configuration" | **STANDS, unadjudicated here.** Note the packet is internally inconsistent about it: 17(qqqqq) calls it a third configuration *outside* the stratum, whereas `ideation-20260905T0200Z-fable5.md` §4.3 calls it "a per-row chart condition" *inside* the stratum. Out of this lane's scope; flagged. |
| (iii) `s′ > 2` residual | **STANDS.** (Independently confirmed as the binding item by 17(eeeeee) and the `moh100-residue-is-s3-descent` finding.) |
| (iv) routing maps unproved | **STANDS** (`OPEN[ROUTING-MAPS]`). |

So the scope caveat is a **real residual**, but for reasons (ii)–(iv), **not** for reason (i).
The correct replacement wording for the caveat:

> (H1)∧(H2) + routing reduces the two-point `M_s = n−2` stratum. By Moh Prop 5.4 (p.183) +
> Lemma 5.3 (p.185), **every minimal-total-degree plane Keller counterexample lies in that
> stratum**, so completing the program proves plane JC2 — the residual scope items are
> U-NEGATIVE, the `s′ ≥ 3` depth case, and the unproved routing maps, **not** a one-place
> configuration outside Moh's line.

This is what Fable predicted conditionally in `ideation-20260905T0200Z-fable5.md` §4.3 ("if
Moh's p.183 'Moreover' clause holds as printed, a minimal-total-degree counterexample IS
two-point"). It holds as printed. The 20260904T1200Z retyping of the program as "two-point
stratum only, one-place is a separate program" was, on the point-(i) clause, an over-correction.

---

## 5. Precision items (FALLACY-v2 discipline)

### 5.1 Two corrections to campaign wording

- **Point, not place.** The excluded configuration is *one **point** at infinity* — Moh's own
  parenthetical in Prop 4.3, "powers of a common linear form (i.e. one point at infinite)". A
  single point at infinity may carry several **places** (branches). The campaign's leak (i) was
  worded "one-place". This matters because the Abhyankar–Moh epimorphism theorem needs one
  *place* (plus `k[x,y]/(f) ≅ k[t]`), so an AMT-based disposal would have had a gap that Moh's
  Prop 5.4 does not have: **Prop 5.4 handles the whole one-point branch directly**, by the
  weighted-form automorphism, with no place-count hypothesis and no appeal to AMT. Nothing in
  the chain of §3 needs the point/place bridge.
- **`[A.1]` is not Abhyankar–Moh.** In Moh's reference list, `[A.1] = S. S. Abhyankar, "On
  Expansion Techniques in Algebraic Geometry", TATA Institute Bombay 1977`; Abhyankar–Moh
  *"Embeddings of the line in the plane"* is `[A-M.2]`. The p.183 remark *"(cf. [A.1], p. 14)
  'one point at infinite'"* and Lemma 5.3's *"(cf. [A.1], p. 139)"* are terminology/technique
  citations to Abhyankar's TATA notes, **not** to the epimorphism theorem. (The campaign memory
  `moh-prop54-minimal-counterexample-two-point` asserted the one-place branch "ends in
  Abhyankar–Moh [A.1]"; that attribution is wrong and is corrected here. The mathematical
  conclusion of that memory — the "Moreover" clause + Lemma 5.3 force the two-point
  configuration — is confirmed, and is now unconditional rather than conditional.)

### 5.2 Two bookkeeping caveats in the source (typed; neither affects the verdict)

- `CAVEAT[TOWER-INDEX-1]`. Prop 5.4 is stated for a tower reaching `D_1`, while the Theorem
  (p.200) asserts tower construction *"for any `r ≥ 2`"*, and the proof of Prop 5.3 remarks
  *"Note that `r ≥ 2`. Otherwise we have `M_1 = n−2 ≥ 0`"* — impossible since
  `M_1 = μ_1 = −deg_y T₁^ψ < 0`. Prop 5.4's `i = 1` branch is exactly the case where `D_1` is
  reached, and it terminates in `k[x,y] = k[f,g]` with `M_1 = −1`, consistent with `M_1 < 0`. So
  this is a presentation seam, not a hole.
- `CAVEAT[INDEX-FORMULA-EMPTY]`. If `{ r : V_{r+1}d_r/d_{r+1} > V_r }` were empty the index `i`
  of Prop 5.4's first clause would be undefined. The dichotomy of §3 is **index-free** (it is
  stated in terms of the radius of the smallest disc, exactly as Lemma 5.3 is), and route (b) of
  §2 is index-free, so the verdict does not depend on this clause. Recorded so that a later lane
  quoting the `i = max{…}` formula knows where its edge is.

### 5.3 What this lane does *not* claim

- No claim that the **one-point** configuration is impossible for a *non-minimal* Keller pair —
  Prop 5.4's branch (b) says its degrees drop, not that it does not exist. The theorem is about
  minimal / non-simultaneously-reducible pairs only.
- No claim about the literature status of the one-place case *per se*: it is not needed. (For
  the record, the standard disposal in the literature — one place at infinity + Jacobian
  condition ⟹ the fibre is `𝔸¹` ⟹ AMT/Suzuki ⟹ coordinate — is *corroborating context*, typed
  as such, not used in §3.)
- No exit-price assertion is made, so no `charge_basis` line is due under FALLACY-v2.
- No ledger edit, no `jc2-lean` touch, no in-progress lane report read.

---

## 6. Drivers and reproduction

`box/prop54-20260905/`:

- `inputs.manifest.sha256`, `inputs.check.log` — 5/5 OK.
- `delta_identity_check.py`, `delta_identity_check.log` — symbolic proof that Def 5.1(2)+(3)
  give `δ_i = −1/(n−M_i−1)` for all `1 ≤ i ≤ s ≤ 8` with no sign hypothesis on `δ_i`.
- `moh_p166-27.png`, `moh_p179-40.png`, `moh_p183-44.png`, `moh_p185-46.png`, `moh_p186-47.png`,
  `moh_p194_crop-55.png` — 300-dpi renderings of the load-bearing pages (the pdftotext layer
  drops the displayed index in Prop 5.4 and garbles the `n/d_s` exponent on p.194; both were
  read from the images).
- `moh_full.txt` — full text layer, for line-referenced grepping.

## 7. OPENs

- `OPEN[PROP-5.4-MINIMALITY]` → **RESOLVED (affirmative)**: minimality forces two points at
  infinity. Ready for the gate; a hostile replay should re-read p.183 and p.185 from the images
  and re-run `delta_identity_check.py`.
- `OPEN[ONE-PLACE-GAP]` → **NOT RAISED** (no such gap for minimal counterexamples).
- New, small: `CAVEAT[TOWER-INDEX-1]`, `CAVEAT[INDEX-FORMULA-EMPTY]` (§5.2) — both
  non-load-bearing, recorded for citation hygiene.
- Flagged for the coordinator, not adjudicated here: the packet disagrees with itself on whether
  U-NEGATIVE (`V₂′ > d₂′`) is inside or outside the two-point stratum (17(qqqqq)(5) vs
  `ideation-20260905T0200Z-fable5.md` §4.3). That disagreement, not a one-place configuration, is
  now the least-settled part of the scope statement.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19428`.
- Body SHA-256:
  `613a89ce7a2fd9b09409ab5b86dbbb4c09c5bddec9d4b5b14987fe6c8612c00a`.
- Frozen basis: `37589ccbc49aa60575feebff7a5e7bd78e9a4835`.
