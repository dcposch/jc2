# Hostile different-model review — Fable5 `20260827T1808Z` ideation

Reviewer: Opus 5 (Anthropic), exact model ID `claude-opus-5`, acting as a
hostile mathematical reviewer.
Written: 2026-08-27.
Reviewed producer: `xmodel/ideation-20260827T1808Z-fable5.md`,
SHA-256 `df7a92a1172d4c6857be9e94b62592e4e11dfd438be54c30f2936a141b3dfdbc`
(recomputed, matches).
Common packet: `xmodel/ideation-20260827T1808Z-packet.md`,
SHA-256 `e388864250cdaa7bd23d5eb0babe8929bf0c02d80758ae91d708202ea9e2f6cc`
(recomputed, matches).

Charge: audit three load-bearing bundles — F1 (fixture-gate emptiness by
composition), the endpoint transfer, and the K00 kernel structure — with
desk-scale exact arithmetic only.

---

## 0. Headline

The report's mathematics is largely right and, in the K00 bundle,
verifiably right in a stronger sense than it claims. Three things are wrong
and one is mislabelled:

1. **F1 is correct but not new.** The emptiness conclusion is written
   verbatim inside the *already promoted* R7R1 hostile review
   `7ab758fa…`, which Fable5 lists as consumed evidence. It is a
   promotion-lifecycle gap, not a composition gap. The genuinely new part
   is the R3/R4 containment route and the sharpening that only **626** of
   the 734 generators are needed.
2. **The upper-face rigidity statement is REFUTED**, twice over: the sign
   is inverted, and the polynomial-`Y` form has *no solution at all* on
   exactly the two survivor branches where Card 1 wants to use it. The
   correct closed form is `g22 = v/(8A^5B)` with `Bv' + (3/2)B'v = A`.
3. **The "face uniformity" corollary is REFUTED as stated.** The upper face
   is rigid only because its `G` window is empty at weight 22. The lower
   face's target-weight window is *not* empty (`G_17 = Q[ξ]_{≤7}`, eight
   slots, re-derived here from the frozen D3 bytes), so
   `Dtil_17 = −L̃_17(g̃17)` is false; the correct uniform statement is
   `D_target = L_target(G_target − g_target)`. Card 3's row-17 architecture
   inherits the defect.
4. **`ℓ0·b` cannot be adjoined to `BASE4`.** `BASE4` is a six-variable job;
   `ℓ0·b` involves all 33 ring variables.

Everything else in the three bundles survives, and several sampled claims
are upgraded here to symbolic identities.

---

## 1. Bundle F1 — is the frozen D5G35 gate empty by composition?

### 1.1 What I did rather than trust prose

I did not read AUDIT prose as evidence. I rebuilt the gate. From the frozen
D3 windows (`RAW_INPUT.json` in
`cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/`) I formed
`F = H^2 + Σ_{n=1}^{14} t^n F_n`, `G = H^3 + Σ_{n=1}^{21} t^n G_n` with each
`F_n, G_n` a generic element of its frozen degree window, applied the row
formula, and compared against every entry of the frozen `TARGET_GATE.json`.

```text
all 734 frozen generators reproduced as (row − target):  True
rows computed with no gate generator:                    none
gate generators with an empty computed row:              none
D0 identically empty:  True        D35 identically empty:  True
D34 degrees: [4, 5],   X^4: 2·f_2_0·g_3_1 − 3·f_2_1·g_3_0
                       X^5: 8·f_2_0·g_4_4 − 12·f_3_4·g_3_0
```

Independently, by hand: writing `E = 12F_XG − 8FG_X − t(F_XG_t − F_tG_X)`
and expanding, the `t^n` coefficient is
`Σ_{i+j=n}[(12−j)F_i'G_j + (i−8)F_iG_j']` — the `α`-terms of
`−tF_XR_t + tF_tR_X` cancel. So the D5G35 row convention and the R3
operator are literally the same object, **including the sign of the
target**. Both my hand expansion and the byte-level regeneration agree.

Window census (recomputed, not quoted): `F` weights 0–14, `G` weights 0–21,
400 positive-weight slots, top row `14 + 21 = 35`.

### 1.2 Atom verdicts

| Atom | Verdict |
|---|---|
| F1-A Row formula ⇔ R3 operator, coefficientwise, incl. target sign | **CONFIRMED** |
| F1-B Gate solutions ⊆ R3's excluded set (route 1) | **CONFIRMED** |
| F1-C R3's AUDIT quantifier faithfully reproduces producer + review | **CONFIRMED** (Fable5's fail-closed caveat is now closed; no recheck needed) |
| F1-D Route 2 (R4, every squarefree `deg H ≥ 2`) | **CONFIRMED WITH REPAIR** — it is *not independent* |
| F1-E Route 3 (R7R1 `q0` + superelliptic) | **CONFIRMED WITH REPAIR** — not independent, and its stated premise is unnecessary |
| F1-F "rows above 34 vanish" (`D35 ≡ 0`) | **CONFIRMED** — and load-bearing for *no* route |
| F1-G "This is a composition gap the ledger missed" | **REFUTED** as a novelty claim |
| F1-H Sharpening: 626 generators suffice; emptiness is scheme-theoretic | **CONFIRMED** (new, mine) |
| F1-I "Live work on this fixture should stop" | **CONFIRMED WITH REPAIR** — nothing *live* targets it |

### 1.3 F1-C — I closed the caveat instead of recommending a recheck

Fable5 recommends "a one-hour different-model recheck of R3's quantifier".
Unnecessary. The producer `b1851156…` §0 states verbatim: *"Let `K` be a
characteristic-zero field, put `H=X^8−1`, and suppose `F,G ∈ K[X][[t]]`,
`F_0=H^2`, `G_0=H^3`. There is no such polynomial-`X` formal jet
satisfying `E = t^22 + O(t^23)`."* The Grok review `27fcd256…` states the
identical claim under "Claim under review (narrow)" and returns
**CONFIRMED** on all nineteen items with no REFUTED and no GAP/REPAIR.
AUDIT does not over-quantify.

I also re-derived the proof rather than reading it:

* `E(F, t^nF^α) = (12 − 8α − n)·t^nF^αF_X` — verified by direct
  differentiation; the two `α`-terms cancel exactly.
* At weight `n` with residual vanishing below `n`, the row is
  `2H[(12−n)H'r_n − 4Hr_n'] = 0`, so `r_n'/r_n = ((12−n)/4)(H'/H)`, hence
  `ord_c(r_n) = ((12−n)/4)·ord_c(H)` at every place. For `H` squarefree
  that is integral only at `n ≡ 0 mod 4`; the six modes are complete.
* Pole lemma: at `ord_c(d) = −m ≤ −2`, the weight-22 row has
  `ord_c = 1 − m < 0` with leading factor `(8m − 20) ≠ 0`, contradicting
  regularity. Hence `d = −Y/(2H)`, `Y ∈ K[X]`.
* `M(Y) = 4HY' + 6H'Y` has degree `deg Y + 7` with leading coefficient
  `(4·deg Y + 48)·lc(Y) ≠ 0`, so `M(Y) = 1` is impossible.
* Cross-check of R3(4.6): `M(X/48) = H/12 + X^8 = 1 + (13/12)H`. ✓

Observation the producer did not claim: the proof never uses polynomiality
of `F,G` — the weight-22 equation itself forces `d` to be regular off the
roots of `H` (a pole of order `m` off `H` gives `ord = −m−1`). **R3 is
therefore true for `F,G ∈ K(X)[[t]]` as well.** That only strengthens the
containment.

### 1.4 F1-D / F1-E — "three independent routes" is one obstruction in three costumes

R4 `11cad1db…` opens: *"The reviewed R3 rational-mode proof does not use
`H=X^8−1` until its final degree calculation. It transports verbatim."*
Routes 1 and 2 are the **same proof**, same producer lane, same reviewer
family. Calling route 2 "independent" overstates the evidence.

Route 3 is the same obstruction too. Explicitly:

```text
d/dX (Y·H^{3/2}) = H^{1/2}·(HY' + (3/2)H'Y) = (1/4)·H^{1/2}·M(Y),
```

so `M(Y) = 1` ⟺ `w dX/4` is exact with primitive `Y·H·w` on `w^2 = H`.
The promoted superelliptic fixture `[w dX] = −(4/5)[dX/w] ≠ 0` is that same
statement. I verified the relation by hand: `2w dw = 8X^7dX` gives
`d(Xw) = w dX + 4X^8dX/w = 5w dX + 4dX/w`, and `[dX/w] ≠ 0` because
`dX/w` is a nonzero holomorphic differential on a genus-3 curve.

What *is* independent about route 3 is the reviewer (Fable5 on R7R1 vs Grok
on R3/R4) and the mechanical path (superelliptic reduction vs degree law).
That is corroboration, not a second proof. **Repair:** call routes 2 and 3
*corroborating restatements*, not independent routes.

Route 3 also carries an unnecessary premise. Fable5 writes that "the gate
forces `E=t^22` exactly (weights above 35 vanish …, `D35≡0` promoted)".
R7R1's own promoted licensing schedule is `n + 22 < N` for
`E = t^22 + O(t^N)`; row `q0` needs only `N = 23`, i.e. exactly R3's
hypothesis. **`D35 ≡ 0` and the whole `D23..D34` tail are irrelevant to
every route.**

### 1.5 F1-G — the conclusion is already in promoted bytes

`xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md`
(`7ab758fa…`, promoted at 16:48Z), under "Context notes, recorded for the
successor (no verdict impact)":

> By reviewed R5's degree law (`b=8` excluded; rederived here) plus R7R1's
> `q0` row and trace descent, `q0 dX` is not exact even in `L`, so *no*
> slot values on the current pinned polygons can reach `E=t^22+O(t^23)`.
> The exact-target determinant system on the current artificial fixture is
> infeasible.

That is F1, in a file Fable5 lists as consumed at promoted scope. The
"UNSOLVED" label survived because the note was tagged *no verdict impact*
and the 17:22Z D5G35 promotion did not fold it in. Fable5's own
consequence 1 ("a lifecycle correction, not new mathematics") is the honest
description; the §F1 framing around it ("a composition gap of exactly the
kind the theorem-interface pass exists to catch") is not.

**Novelty adjudication:** emptiness = **KNOWN** (promoted-review context
note). The R3/R4 containment route and §1.6's sharpening = **NEW**.

### 1.6 F1-H — two sharpenings that are mine, not the report's

*Only 626 generators are needed.* Census of `TARGET_GATE.json` by weight:
weights 1–22 carry **626** generators, weights 23–34 carry **108**. R3's
hypothesis is exactly the weights-1–22 subsystem. So the sub-ideal
generated by those 626 is already inconsistent, and the 108 tail generators
plus the structural `D35 ≡ 0` are redundant for emptiness.

*The emptiness is scheme-theoretic, not just field-theoretic.* R3 excludes
solutions over every characteristic-zero field, in particular `Q̄`. By the
Nullstellensatz the gate ideal is the unit ideal in `Q̄[400 slots]`, hence
(faithful flatness) in `Q[400 slots]`. So `1 ∈ I`: there are no solutions
in **any** `Q`-algebra, including dual numbers. This matters because the
upper-cascade review's live repair turns precisely on dual-number tangent
solutions existing where field points do not; here they cannot.

### 1.7 F1-I — what actually stops

The two live AWS jobs (Box02 R2 PID 366878, R5 PID 371365) are K00 exact
jobs, not GGV. **No live process targets this fixture**, so the correct
action is to cancel *registered/queued plans*, not to kill anything.
Specifically: any plan whose deliverable is "solve / decide / search the
734-generator gate" should be cancelled before compute. The D5G35
*compiler* stays promoted and useful — it is the row machinery for other
`H`. The `q1`/`q2` licensing schedule (`n+22 < N`) stays a theorem; only its
instantiation *on this fixture* becomes vacuous, because it now quantifies
over an empty set. Survivor-branch endpoints (`H = A^2`, `H = A^2B`) are
untouched and remain the open objects.

---

## 2. Bundle 2 — the endpoint transfer

### 2.1 The identity itself

I verified `D22 = −L_22(g22)` exactly, on branch P with `A = X^4−1`,
`H = A^2`, a nontrivial `F = H^2 + F_1t + F_2t^2` (`F_1` a degree-6
polynomial, `F_2` quadratic), and a continuation carrying **three** modes
(`c_4, c_6, c_10` nonzero) — not the mode-free fixture the producer used:

```text
E(F, F^{3/2}) rows 0..22 all zero                    : True
prefix rows D_1..D_21 vanish (truncated continuation): True
D_22 + L_22(g22) == 0                                : True
```

and, as a by-product, the branch-P mode schedule:

```text
n = 2,4,6,8,10,12,14,16,18,20  →  exponent (12−n)/2 integral, E(F,Z_n) ≡ 0
n odd                          →  exponent half-integral, no rational mode
```

Ten modes on branch P (not five), five on branch Q (`n ≡ 0 mod 4`). This
reproduces R5's promoted-review δ-trichotomy independently: `δ ≡ 2 mod 4`
(`H = A^2`) gives every even `n`; `δ` odd (`H = A^2B`) gives `n ≡ 0 mod 4`.

`L_22(R) = 2H[−10H'R − 4HR'] = −20HH'R − 8H^2R'` is literally R3(4.1) and
R5's extraction; and because `Δ_j = 0` for `j < 22`, no `F_j` with `j ≥ 1`
enters — which R5's review already states verbatim.

**T-A: CONFIRMED.**

### 2.2 The identity does not need the unproved window-tier completeness

Fable5's §10 conditions §3b on window-tier completeness at weights 7–21,
"executed through weight 6 only". That caveat is over-scoped. The identity
needs exactly three things: (i) `D_1 = … = D_21 = 0`; (ii) the frozen `G`
window is **empty at weight 22** (true — `G` weights run 0–21); (iii)
rational-tier completeness of the mode subtraction, which is R5-review item
3, **CONFIRMED**. Window membership of the intermediate `G_n` is needed to
*enumerate prefix strata* in PS21, not to derive the identity.

**T-B: CONFIRMED WITH REPAIR** (drop the caveat from the identity; keep it
on the compiler).

### 2.3 The exclusion half

`L_22(R) = 2H·[…]`, so `L_22(K[X]) ⊆ (H)`; with `deg H = 8 > 0`,
`D22 = 1` is impossible whenever `g22 ∈ K[X]`. Trivially true once T-A
holds. **T-C: CONFIRMED.**

### 2.4 The rigidity half — REFUTED, with a clean repair

Fable5 states: `D22=1 ⟺ L_22(g22) = −1 ⟺ g22 = −Y/(2H) + κ` with
`M(Y) = 1`.

**Error 1 — sign.** Fable5's own bridge `L_22(N/H) = −2M(N)` (which I
confirm: `L_22(N/H) = −12H'N − 8HN' = −2M(N)`) makes
`g22 = −Y/(2H)` give `L_22(g22) = +M(Y) = 1`, hence
`D22 = −L_22(g22) = −1`, not `+1`. The correct form is `+Y/(2H)`
(equivalently `−Y/(2H)` with `M(Y) = −1`).

**Error 2 — polynomiality, and it is fatal on the branches that matter.**
On branch P, `H = A^2` and `M(Y) = 4A^2Y' + 12AA'Y ∈ (A)` for every
polynomial `Y`, so `M(Y) = 1` has **no** polynomial solution. Fable5's
literal statement therefore declares the branch-P endpoint unreachable —
contradicting the promoted endpoint criterion, and contradicting their own
§6 sentence "the particular `Y` with `M(Y)=1` (exists on survivor branches
by the promoted criterion)". Table of `M(X^d)`, `d = 0..8`, on branch P:
every value has degree `d+7 ≥ 7`.

**The repair, verified exactly on both branches.** Write `H = A^2B` with
`B` squarefree and `N_B(v) := Bv' + (3/2)B'v`. Then

```text
D22 = 1   ⟺   g22 = v/(8·A^5·B)   with   N_B(v) = A ,  v ∈ K[X].
```

Machine-checked in exact arithmetic:

| branch | data | `L_22(g22)` | `D22` | `2Hu' + H'u − 2H`, `u = 8H^2g22` | `Y := 2H·g22`, `M(Y)` |
|---|---|---|---|---|---|
| P | `A = X^4−1`, `v = X^5/5 − X` | `−1` | `+1` | `0` | `v/(4A^3)` (not polynomial), `M(Y) = +1` |
| Q | `B = X^2−1`, `A = X^3−(2/5)X`, `v = X^2/5` | `−1` | `+1` | `0` | `M(Y) = +1` |

The `2Hu' + H'u = 2H` column is the *promoted* endpoint equation, so the
repaired form lands exactly on promoted evidence. Note `M(Y) = +1` with
`g22 = +Y/(2H)`, confirming Error 1 independently.

Does the sign error matter? Over `Q̄` no: `t ↦ μt` with `μ^22 = −1`
preserves the windows and the vanishing prefix while flipping `D22`. Over
`Q` it does: PS21 and Card 1 are specified as **rational-point** searches,
so a compiler hard-coding `−Y/(2H)`, `M(Y)=1` would solve `D22 = −1`.

**T-D: REFUTED** (both the sign and the polynomial-`Y` form).

### 2.5 Kernels on branches P and Q

`L_22(κ) = 0 ⟺ κ'/κ = −(5/2)H'/H ⟺ κ = cH^{−5/2}`. On P (`H = A^2`) this
is `cA^{−5}`; on Q (`H = A^2B`, `B` squarefree nonconstant) the local
exponent `−5/2` at a root of `B` is not integral, so the kernel is `0`.
**T-E: CONFIRMED**, exactly as stated.

Better than the report's Card 1 discriminator: `N_B` has leading
coefficient `lc(B)·lc(v)·(deg v + (3/2)deg B) ≠ 0`, so for `deg B ≥ 1` it is
**injective**, `v` is unique, and on branch Q the endpoint forces `g22` to
equal **one explicit rational function** — not "the finitely many `M(Y)=1`
solutions". For the R5 pair that function is `X^2/(40·A^5·B)`. On branch P,
`B` is constant, `ker N_B = K`, and the constant of integration in `v` *is*
the kernel freedom `κ = cA^{−5}`: `g22 = (X^5/5 − X + c)/(8A^5)`.
**T-F: CONFIRMED WITH REPAIR** (sharper than claimed).

### 2.6 The lower-face analogue — REFUTED as stated

The operator reduction is right. By hand, with `F_0 = aK^2`:

```text
L̃_17(R) = −10aKK'R − 8aK^2R' ,
L̃_17(g/K^2) = −(2a/K)·(4Kg' − 3K'g) ,
```

so `L̃_17(g̃17) = 1` gives `4Kg' − 3K'g = −K/(2a)`, which is the promoted
NU17 ODE `4Kg' − 3K'g = 4K` rescaled by `−1/(8a)` (`a ≠ 0`). That part is
**CONFIRMED**.

What fails is the transfer. The upper face is rigid because `G` has **no**
weight-22 slot. The lower face does have a target-weight window. I
re-derived the entire lower regrading from the frozen `RAW_INPUT.json`
under `ν_F = 8−4i+j`, `ν_G = 12−4i+j`:

```text
F : ν = 0..16          →  F_17 is EMPTY
G : ν = 0..24 ,  G_17  =  ξ-degrees 0..7  =  Q[ξ]_{≤7}   (8 slots)
     28 G-slots at ν = 18..24 ;  determinant ceiling 16+24 = 40
```

matching the promoted AUDIT line exactly. Hence `Δ_17 = G_17 − g̃17` with
`G_17` **free in an 8-dimensional window**, and

```text
Dtil_17 = L̃_17(G_17 − g̃17)   ≠   −L̃_17(g̃17).
```

The exclusion half survives untouched — `L̃_17(polynomial) ∈ (K)`, so
`Dtil_17 = −1` still forces `g̃17 ∉ K[ξ]` — but the rigidity/closed-form
half does not, and Card 3's architecture ("the row-17 target as
`g̃17 ∈ (particular of 4Kg'−3K'g=−K/(2a)) + ker`") is wrong: the ODE
constrains `G_17 − g̃17`, and the residual must additionally satisfy
`Δ_17 + g̃17 ∈ Q[ξ]_{≤7}`.

**T-G: REFUTED as stated; the operator reduction inside it is CONFIRMED.**

**Correct uniform statement:** `D_target = L_target(G_target − g_target)`.
The two faces differ precisely in whether the target-weight window is empty.

### 2.7 Promoted vs unpromoted, precisely

The AUDIT block promoting the superelliptic endpoint criterion says
explicitly: *"No general-`H` rational-mode completeness for the preceding
GGV equations … follows."* R3's completeness is promoted for `H = X^8−1`;
R4's for general **squarefree** `H`. Neither covers `H = A^2` or `A^2B`.
R5's hostile review confirms the general-multiplicity schedule and the
completeness of subtraction as *review items*, and I reproduced the
branch-P instance symbolically above — but at ledger scope this ingredient
is reviewed, not promoted.

**T-H: SCOPE-CONFLICT.** The transfer identity on branches P/Q currently
rests on an unpromoted (though reviewed-CONFIRMED and independently
re-verified here) completeness lemma. The fix is cheap: micro-promote
exactly R5-review item 3 + item 4 at general multiplicity. Until then,
Card 1 and PS21 must carry that tag.

### 2.8 A discriminator with teeth (mine)

The repaired form converts the endpoint into an `A`-adic pole-order
condition: `ord_A(g22) ≥ −5`, with `A^5·g22` a degree-5 polynomial whose
derivative is `A/8`. Measured pole orders of the forced `g22` on branch P
(`A = X^4−1`):

```text
F1 = H,   F2 = 0        →  g22 = const / A^38     ord_A = −38
F1 = H,   F2 = 1/4      →  g22 = 0                ord_A = +∞   (D22 = 0)
F1 = X^3, F2 = 0        →  g22 = (deg 66) / A^82  ord_A = −82
```

The required window is `≥ −5` against a generic `−82`; the constraint is
extremely tight, so Fable5's "denominator profile" discriminator is a good
instinct and now has an exact target. The middle row is the promoted-
provisional `F = U^2, G = U^3` separator, and it reproduces `D22 = 0` — an
independent consistency check of the transfer identity against the cascade.

### 2.9 Endpoint-bundle verdict table

| Atom | Verdict |
|---|---|
| T-A `D22 = −L_22(g22)`, `L_22 = −20HH'R − 8H^2R'` | **CONFIRMED** |
| T-B independence from window-tier completeness | **CONFIRMED WITH REPAIR** |
| T-C `L_22(K[X]) ⊆ (H)`; exclusion on polynomial strata | **CONFIRMED** |
| T-D rigidity `g22 = −Y/(2H)+κ`, `M(Y)=1` | **REFUTED** (sign + polynomiality) |
| T-E `ker L_22 ∩ K(X)` = `K·A^{−5}` / `0` | **CONFIRMED** |
| T-F branch-Q finiteness | **CONFIRMED WITH REPAIR** (unique, not finite) |
| T-G lower-face `Dtil_17 = −L̃_17(g̃17)` | **REFUTED**; operator reduction **CONFIRMED** |
| T-H promoted scope of general-multiplicity completeness | **SCOPE-CONFLICT** |
| T-I `A`-adic pole-order discriminator | **CONFIRMED** (new, mine) |

---

## 3. Bundle 3 — K00 kernel structure

Byte source: `ATLAS_EXACT_POLYNOMIALS.json`, SHA-256
`d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501`, pinned
in `COMPILED_SOURCE.sha256`, `EVIDENCE.sha256` and `RELEASE_V26R1_W0.json`.
*Custody note:* Fable5 cites the source as "inside the reviewed
`f1a6f1fc…` compiler output". `f1a6f1fc…` is the enclosing `RESULT.json`;
the atlas byte hash is never stated in the report. Traceable, but it should
be pinned directly.

### 3.1 What is symbolic and what was only sampled

Fable5 flags items (3) and (4) as "symbolic for `ℓ0,v1,v2` but pointwise
(3–4 random points) for the `w5`-pencil and the `1/384` ratio". **I raise
all four to symbolic.**

| Claim | Fable5 | This review |
|---|---|---|
| `ℓ0·A = 0`, `ℓ0 = (5/1024,0,3/128,0,1/8,0,1)` | symbolic | **symbolic, reproduced** (all 49 entries) |
| `A·v1 = A·v2 = 0`; `2C0+C2+C4 = 0`, `(1/16)C1+(1/2)C3+C5 = 0` | symbolic | **symbolic, reproduced** |
| `ℓ0·b` nonzero, 690 terms, 33 variables | symbolic | **symbolic, reproduced** (sha `0a6b74e0…`) |
| `w = (1,0,16/3,0,128/3,w5,0)` | 3–4 points | **symbolic** (see below) |
| second adjugate has rank 1 | one point | **symbolic**, all 90 compound `2×2` minors vanish |
| `ratio · w5 = 1/384` | 3 points | **symbolic**, for all 9 valid column pairs |
| 90 / 54 / two classes | promoted census | **reproduced** from frozen minors |

The `w`-constancy is symbolic because of two exact polynomial identities I
found in the frozen bytes:

```text
A[5][j] = 0                                              for j = 0..5
A[0][j] + (16/3)·A[2][j] + (128/3)·A[4][j] = 0           for j = 0..5
```

Hence `w0, w2, w4` are forced to constants by the `j ≤ 5` columns alone
(where `w5` cannot appear), and the single `j = 6` column determines

```text
w5 = −( A[0][6] + (16/3)A[2][6] + (128/3)A[4][6] ) / A[5][6],
```

a 9-term numerator over a 12-term denominator. Not sampled — closed form.

### 3.2 The census explanation, completed

The two-form on the left, `u = ℓ0 ∧ w`, and the constant right Plücker
vector `p = v1 ∧ v2`, have these exact supports:

```text
u_{ab} ≠ 0 for  {a,b} ⊂ {0,2,4,6}    (6 pairs, constants)
              u_{02}=1/384  u_{04}=1/12  u_{06}=−1
              u_{24}=1/3    u_{26}=−16/3 u_{46}=−128/3
u_{a5} = ℓ0_a·w5                      (4 pairs, ∝ w5)   u_{56} = −w5
p_{cd} ≠ 0 exactly for c ∈ {0,2,4} = supp v1, d ∈ {1,3,5} = supp v2  (9 pairs)
```

So `90 = 10 × 9` nonzero `5×5` minor positions, splitting as
`54 = 6×9` (dropped-row pairs from `{0,2,4,6}`, `u` constant) and
`36 = 4×9` (dropped-row pairs containing 5, `u ∝ w5`). The frozen minor
file agrees exactly: dropped-row sets `{0,2},{0,4},{0,6},{2,4},{2,6},{4,6}`
in one class and `{0,5},{2,5},{4,5},{5,6}` in the other, with the nine
dropped-column sets `{0,1},{0,3},{0,5},{1,2},{1,4},{2,3},{2,5},{3,4},{4,5}`
in both. The class ratio is `u_{02}/u_{56}`, and

```text
u_{02} = (5/1024)(16/3) − (3/128)(1) = 1/384    exactly,
```

which is where Fable5's sampled `1/384` comes from. I verified
`384·P02·num(w5) − P56·den(w5) = 0` symbolically for all nine column pairs
(zero residual terms), i.e. `(P02/P56)·w5 = 1/384` as an identity.

**New, and it is V27's registered `MAX5CLASS` step 2 done at desk scale:**
`W` is, up to a nonzero scalar, exactly the **226-term class-0
representative** (the `w5` class, 36 occurrences). The other class is the
236-term representative (54 occurrences). So `I5(A) = (W, W')`, and
`B + I5(A)` is the 9-generator system Fable5 names in §5.

*Trap flagged:* `RELEASE_V26R1_W0.json` records
`W_zero_redundant_mod_B_and_P6_by_explicit_syzygy`. That syzygy lives in
the **33-variable** ring (it uses `P6`). `W` itself lies in
`R = Q[d0_1..d5_1]`, but the redundancy does **not** transfer to `R`, so
`W` may not be dropped from the intrinsic six-variable rank-`≤4` ideal
whose dimension 3 is what V26R1F promoted.

### 3.3 A second universal covector — better than Card 2 (iii)

Fable5 proposes obtaining the second compatibility covector "from the two
promoted minor classes by division". No division is needed. Clearing
denominators in `w` gives a **polynomial** covector, and I verified
`ŵ·A = 0` identically in all 49 entries:

```text
ŵ = A[5][6]·(1, 0, 16/3, 0, 128/3, 0, 0)
    − ( A[0][6] + (16/3)A[2][6] + (128/3)A[4][6] )·e_5 .
```

Therefore **two** universal necessary compatibility conditions exist, at
every point, at every rank, with no localization at `W` and no minor choice:

```text
C1 := ℓ0·b     690 terms   sha256 0a6b74e08f6fb6a3aadfd6ace6be06f7081b465ecc44d364e1bd583f844c0a6d
C2 := ŵ·b    6,702 terms   sha256 246162a6120b9d1312686c624e99ca21d83c7d07d0061c758528c999d19e8954
```

against the frozen `Comp6_Comp7` representatives at 110,117 and 83,298
terms: **7,392 vs 193,415, a 26.2× compression.** Neither `C1` nor `C2` is
literally a `P6` generator (the largest `P6` generator has 457 terms, so
`C1` cannot be one); whether `C1` reduces to zero modulo `P6` remains the
open Gröbner question Fable5 correctly identifies, and it is AWS-scale.

*Sufficiency caveat:* `C1 = C2 = 0` is equivalent to rank-5 compatibility
only where the left kernel is exactly `span(ℓ0, w)`, i.e. where
`rank A = 5` and `(A[5][6], num) ≠ (0,0)`. On `A[5][6] = num = 0`,
`C2` degenerates to `0` and carries no information. Necessity is
unconditional.

### 3.4 `BASE4` cannot receive `ℓ0·b` — REFUTED

`BASE4` is specified in the V27 design as *"decide `B+I5(A)+I4(A)` in six
variables"*, and V26R1F's promoted theorem lives in
`R = Q[d0_1,…,d5_1]`. I confirmed that every entry of `A` uses only those
six variables — and that `ℓ0·b` uses **all 33**. Adjoining it to `BASE4` is
either ill-typed or silently converts `BASE4` into a 33-variable problem,
destroying the intrinsic statement whose dimension 3 is the promoted
result. Valid destinations are only the big-ring jobs: `LOW-KILL`, `Kr`,
and the single rank-five chart.

### 3.5 The gauge quotient — safe for grade 7, not for prolongation

`A·v1 = A·v2 = 0` with `v1, v2` constant means the seven newest variables
carry a globally trivial rank-2 gauge, so solvability at grade 7 is
unchanged by passing to the 5-dimensional quotient. But the V27 design's
step 6 is later-grade prolongation, and the grade-8 equations can depend on
the *actual* newest-variable values, not just their gauge class. **Retain
`v1, v2` and the two-parameter solution family; do not discard them at the
quotient step.**

### 3.6 How to amend V27 without invalidating a live run

The two live jobs (Box02 R2, R5) are pre-V27 and consume the frozen V26
manifest; V27 itself is `UNRUN / NOT EVIDENCE`. The amendments are
therefore safe **iff**:

1. **No frozen byte is edited.** Write a new preregistration/case that
   pins `d7ec6d18…` and the V26R1F/review hashes; do not touch the V26
   case directory, whose bytes the live jobs' custody chain references.
2. **`C1`, `C2` go only into big-ring jobs** (`LOW-KILL`, `Kr`, rank-five
   chart), never `BASE4` (§3.4).
3. **Record that adjoining `C1`/`C2` changes what "proper" means.**
   `V(Kr + (C1,C2)) ⊊ V(Kr)`: a rank-`≤ r` point of `V(Kr)` with
   `rank A < rank E` is genuinely incompatible and need not satisfy
   `C1 = 0`. The kill-screen direction is preserved — every *compatible*
   point satisfies `C1 = C2 = 0`, so `Kr + (C1,C2) = (1)` still eliminates
   all compatible ranks `≤ r` — but a proper outcome is no longer
   comparable with a previous `Kr` run's dimension or degree.
4. **Do not carry mutation controls across the amendment boundary.** The
   design's registered mutations (swap a class representative, `b`-sign,
   restored `k6_0`) must be re-run inside the amended system.
5. The `MAX5CLASS` `W`-identification (§3.2) may be banked immediately as a
   desk result; it consumes nothing live.

### 3.7 K00 verdict table

| Atom | Verdict |
|---|---|
| K-A `ℓ0·A = 0` symbolically | **CONFIRMED** |
| K-B `A·v1 = A·v2 = 0`; two column relations; explains `I6(A)=0` | **CONFIRMED** |
| K-C `ℓ0·b` nonzero, 690 terms, 33 variables | **CONFIRMED** |
| K-D universal necessary compatibility, all ranks, no localization | **CONFIRMED** |
| K-E `w` constant but one moving entry `w5` | **CONFIRMED**, upgraded to symbolic |
| K-F second adjugate rank 1; ratio·`w5` = 1/384 | **CONFIRMED**, upgraded to symbolic |
| K-G 90 / 54 / two-class explanation | **CONFIRMED**, and completed (`90 = 10×9`; `W` identified) |
| K-H "adjoin `ℓ0·b` to `BASE4`" | **REFUTED** (ring mismatch) |
| K-I "replace `y`-space by the gauge quotient" | **CONFIRMED WITH REPAIR** (not for prolongation) |
| K-J second covector "by division from the minor classes" | **CONFIRMED WITH REPAIR** — no division needed; `ŵ` is polynomial |
| K-L byte-source custody pin | **CONFIRMED WITH REPAIR** (pin `d7ec6d18…`) |

---

## 4. What may be promoted now

1. **`GATE-EMPTY`.** The frozen D5G35 artificial-fixture gate
   `D0=…=D21=0, D22=1, D23=…=D34=0` on `H = X^8−1`, `F0=H^2`, `G0=H^3`,
   400 D3 slots, is **empty**, and the ideal generated by its 734
   generators in `Q[400 slots]` is the unit ideal. Licensed by promoted R3
   (`b1851156…` / `27fcd256…`) alone; R4 (`11cad1db…` / `5187676b…`)
   covers it as a special case of general squarefree `deg H ≥ 2`.
   Sharpened: the **626** generators of weights 1–22 already suffice; the
   108 tail generators and `D35 ≡ 0` are redundant. Relabel the ledger
   `EMPTY-BY-COMPOSITION (R3; R4)`. Record that the emptiness is
   scheme-theoretic, so no dual-number tangent solution exists either.
   Record also that the conclusion was already written in the promoted
   R7R1 review `7ab758fa…` — this is a lifecycle correction.
2. **`TRANSFER-22`.** On the frozen D3 windows, if `D1=…=D21=0` then
   `D22 = −L_22(g22)` with `L_22(R) = −20HH'R − 8H^2R'`, `g22` the
   weight-22 coefficient of the forced rational continuation, and no `F_j`
   (`j ≥ 1`) contamination. Corollary: `L_22(K[X]) ⊆ (H)`, so `D22 = 1`
   forces `g22 ∉ K[X]`. Promotable at fixture scope now; at branch-P/Q
   scope it needs the T-H micro-promotion.
3. **`ENDPOINT-FORM`** (repaired, replacing Fable5's rigidity): with
   `H = A^2B`, `B` squarefree,
   `D22 = 1 ⟺ g22 = v/(8A^5B)` with `Bv' + (3/2)B'v = A`, `v ∈ K[X]`;
   `v` unique for `deg B ≥ 1`, unique up to the additive constant
   (`= ker L_22 = K·A^{−5}`) when `B` is constant. Verified exactly on both
   named branches, and the promoted equation `2Hu' + H'u = 2H` holds for
   `u = 8H^2g22`.
4. **`K00-PENCIL`.** `ℓ0·A = 0` and `ŵ·A = 0` are exact polynomial
   identities (`ŵ` as in §3.3); `A·v1 = A·v2 = 0` with `v1, v2` constant,
   which structurally forces `I6(A) = 0`; `w5` has the closed form of
   §3.1; the second adjugate factors as `minor_{IJ} = λ·u_I·p_J`, giving
   `90 = 10×9`, the two classes `36`/`54`, and the exact constant
   `u_{02} = 1/384`. `C1 = ℓ0·b` (690 terms) and `C2 = ŵ·b` (6,702 terms)
   are universal necessary compatibility conditions. `W` is the 226-term
   class representative.

Nothing above is a family landing, a fan cover, an arc, a witness,
`G2-PSC`, `G2-BD`, order two, maximum twelve, or JC2.

## 5. What should be cancelled or redirected

* **Cancel** every registered plan whose deliverable is solving, searching,
  or Gröbner-deciding the 734-generator fixture gate. No live process is
  affected; this is a queue action.
* **Redirect** PS21/Card 1 to the repaired endpoint form. As written it
  targets `D22 = −1` over `Q` and hard-codes a polynomial `Y` that does not
  exist on either branch. The corrected target is the `A`-adic pole-order
  condition `ord_A(g22) ≥ −5` with `A^5g22 = v/8`, `v' = A` on P
  (`ord_A(g22) ≥ −5`, `A^5Bg22 = v/8`, `N_B(v) = A` on Q). Measured
  generic pole orders are `−38` and `−82`, so this discriminator should be
  run *first*, before any prefix compilation.
* **Redesign** Card 3's row-17 architecture: the ODE constrains
  `G_17 − g̃17` with `G_17` free in the 8-slot window `Q[ξ]_{≤7}`, not
  `g̃17` alone. The exclusion half needs no change.
* **Re-anchor** the `q1`/`q2` licensing sentences to survivor-`H`
  compilations; on the fixture they now quantify over an empty set. The
  licensing schedule `n + 22 < N` itself remains a theorem.
* **Do not** spend a "one-hour recheck of R3's quantifier" (§1.3), and
  **do not** cite routes 2/3 as independent (§1.4).
* **Micro-promote** R5-review items 3–4 at general multiplicity, which is
  the cheapest way to close T-H and unblock branch-P/Q work.

## 6. Shortest repaired statements

```text
R1  (gate)     The 626 weight-1..22 generators of the frozen D5G35 gate
               generate the unit ideal in Q[400 slots]: a solution over any
               field would be a polynomial-X formal jet with F0=H^2,
               G0=H^3, E = t^22 + O(t^23), excluded by promoted R3 (R4 for
               every squarefree H of degree >= 2).  The 108 weight-23..34
               generators and D35 = 0 are redundant.

R2  (transfer) On the frozen D3 windows G has no weight-22 slot; hence if
               D1 = ... = D21 = 0 then D22 = -L_22(g22),
               L_22(R) = -20 H H' R - 8 H^2 R'.  Since L_22(K[X]) is
               contained in (H), D22 = 1 forces g22 not polynomial.

R3  (endpoint) With H = A^2 B, B squarefree:
               D22 = 1  <=>  g22 = v/(8 A^5 B),  B v' + (3/2) B' v = A,
               v in K[X];  v unique if deg B >= 1, unique up to an additive
               constant (= ker L_22 = K A^-5) if B is constant.

R4  (faces)    D_target = L_target(G_target - g_target).  The upper face is
               rigid because its G window is empty at weight 22; the lower
               face's is not (G_17 = Q[xi]_{<=7}), so
               Dtil_17 = L_17~(G_17 - g~_17) and the ODE constrains the
               difference.  Exclusion half unchanged: L_17~(polynomial) is
               in (K).

R5  (K00)      l0 = (5/1024,0,3/128,0,1/8,0,1) and
               w^ = A56*(1,0,16/3,0,128/3,0,0)
                    - (A06 + (16/3)A26 + (128/3)A46)*e5
               are polynomial left-kernel covectors of the frozen 7x7 A, so
               C1 = l0.b (690 terms) and C2 = w^.b (6702 terms) are
               universal necessary compatibility conditions at every point
               and every rank.  A v1 = A v2 = 0 with v1,v2 constant, so
               I6(A) = 0 structurally, and the second adjugate factors as
               minor_IJ = lambda * u_I * p_J with u = l0 ^ w, p = v1 ^ v2,
               giving 90 = 10 x 9, the classes 36 (u ~ w5) and 54
               (u constant), and the exact ratio u_02 = 1/384.
               C1 and C2 may be adjoined only to big-ring jobs, never to
               the six-variable BASE4.
```

---

## 7. Exact replay

All checks are pure-Python 3 standard library, exact `fractions.Fraction`,
run locally at desk scale (longest 46 s). Scripts in `/tmp/o5hr/`:

```text
bea4ab02d634538c99bab5e67e82129ff58df35fde48d1159f8e0fc0c09ce7cf  rf.py          exact Q(X) arithmetic
9f4b1b022a4012a3fc9f38ccda2468e72c21e6a5dd4fa42b7f37de981a1915a4  regen_gate.py  regenerate all 734 gate generators from D3 windows
0544b036ffb042d6f6c2669e9d9e158078d1e68dd4f30b92242cec7fa0c3a87e  endpoint.py    endpoint operator algebra, both branches
bb586b8ec479d5bb1414e11eefc17f21ea1268576c84df3e049607a85ee4fafb  transfer.py    branch-P mode schedule + transfer identity
bc24d82ae7681b522ec42f71e91e0b75f89d4611f376e7806e3e8c68b790532e  pole2.py       A-adic pole order of the forced g22
59120a8323dfa308de9b69320a0576699231e455ab59bfe771f357bfa93be318  k00.py         l0.A, A.v1, A.v2, column relations, 690-term census
e167195b19687dc449de4f6bed9edbd0074c60ed62f7933d3d871c9da52a4df0  k00b.py        5x5 minor census + sampled kernels
d0e5b5a4721ca85c4d72dfad30e3673159b4d8db1d6071b42946085036e29391  k00c.py        symbolic w-constancy; class supports
97789821cc18ff439f14ec3e3e99c47eff62dc7d63824cdde993304049f5529a  k00d.py        symbolic rank-1 adjugate + 1/384 identity
64fda5083206a060525416035548086e23005c167ab7e881d474ac430669d984  k00e.py        C1/C2 sizes vs Comp6/Comp7; P6 comparison
dc3b6db7f12529aa4f87c2818c9dbf088c5e6c35031f765e43a68345cc506137  k00f.py        W = class-0 representative
3b6f27fbed208e94e729b39948b7285ef3be65d871f0ac3b798c7b716052c123  k00g.py        w^.A = 0 identically; C2 as a polynomial cut
```

Frozen inputs consumed (all recomputed and matched):

```text
df7a92a1172d4c6857be9e94b62592e4e11dfd438be54c30f2936a141b3dfdbc  xmodel/ideation-20260827T1808Z-fable5.md
e388864250cdaa7bd23d5eb0babe8929bf0c02d80758ae91d708202ea9e2f6cc  xmodel/ideation-20260827T1808Z-packet.md
b1851156c83657fa85eb875df7e191a99fd339bfcb79ca1a752742ddff9f70b7  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-sol-20260827.md
27fcd25640f62a92c147863e7a8ef8ca4b7b004f05d54450c8d2d8811c97cdc6  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-hostile-review-grok-20260827.md
11cad1dbdf3d49ffd5f15a84de2969fbb79ac7b134aea18e079061e109322f56  xmodel/ggv-keller-face-general-squarefree-rational-mode-theorem-r4-sol-20260827.md
5187676bdb9b1ea449dde569e426385ad1453b4f15ebc8906886a7cc33c14557  xmodel/ggv-keller-face-general-squarefree-rational-mode-theorem-r4-hostile-review-grok-20260827.md
fd164042... (R5 producer)  48fff5d5... (R5 hostile review, Opus5)
ed0e3460... (R6 producer)  d9e65315... (D5G/R6/K00R6R1 cross-audit)
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md
f0fe0f5d... (D5G35 producer)  ba7162fe... (D5G35 Grok review)  59e9bf2c... (D5G)
72f10ad7... (NU17 narrow core)  d547baa2... (V24 review)
e1ed280ee1f5d7c997fe1ab6fdeaf40b689de71e1682ba8e13b1c4ba5047ae01  cases/.../r3.../verify_r3.py
3d69dfbd6c0e28afafdfc7bbb0cf4ebe57d8522938ddd46b418f71123c1da006  cases/.../r3.../RESULT_R3.json
86742147085332881b3c44ba041172ac5a032d656df3992ceff5da7d0a5b46dc  cases/.../v26.../RESULT_V26R1F_EXACT_PREPASS.md
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501  cases/.../v26.../aws_box02_r2_held_compile/output/ATLAS_EXACT_POLYNOMIALS.json
```

Reproducible derived digests: `sha256(canonical C1) = 0a6b74e08f6f…`,
`sha256(canonical C2) = 246162a6120b…` (canonicalisation: JSON of the
sorted `[monomial, coefficient-string]` list, separators `,` `:`).

## 8. Checks actually run

1. Both frozen report hashes recomputed and matched.
2. Row formula `Σ_{i+j=n}[(12−j)F_i'G_j+(i−8)F_iG_j']` derived by hand from
   R3's operator, including the sign of the target.
3. All **734** frozen gate generators regenerated from the D3 windows;
   `D0 ≡ 0`, `D35 ≡ 0`, `D34` = the two hand-derived generators.
4. Slot census: 400 positive-weight slots; 626 generators at weights ≤ 22,
   108 above.
5. R3's proof re-derived independently (mode identity, log-derivative
   valuation argument, pole lemma `8m−20`, degree law, `M(X/48)` check).
6. R4's boundary `deg H ≥ 2` and the `deg H = 1` escape re-derived.
7. `d(Xw) = 5w dX + 4dX/w` on `w^2 = X^8−1`, giving the promoted
   `[w dX] = −(4/5)[dX/w] ≠ 0`; and the bridge
   `d(YH^{3/2}) = (1/4)H^{1/2}M(Y)` showing route 3 = routes 1/2.
8. Bridges `g = 4HY` and `g = −8H^2d` verified by hand
   (`2Hg'+H'g = 2H·M(Y)`; `L_22(N/H) = −2M(N)`).
9. `E(F,F^{3/2}) ≡ 0` through weight 22 on branch P for a nontrivial `F`.
10. Branch-P mode schedule: modes at every even `n ∈ [2,20]`, none at odd
    `n`; each `E(F,Z_n) ≡ 0` exactly.
11. `D1..D21 = 0` and `D22 = −L_22(g22)` for a truncated continuation with
    three nonzero mode constants.
12. Repaired endpoint form `g22 = v/(8A^5B)` verified on branch P
    (`A=X^4−1`) and branch Q (`B=X^2−1`, `A=X^3−(2/5)X`, `v=X^2/5`);
    `L_22(g22) = −1`, `D22 = +1`, `2Hu'+H'u−2H = 0`, `M(2Hg22) = +1`.
13. `M(X^d) ≠ 1` for `d = 0..8` on branch P (no polynomial `Y` exists).
14. `N_B` leading-coefficient injectivity for `deg B ≥ 1`.
15. Lower-face operator reduction `L̃_17(g/K^2) = −(2a/K)(4Kg'−3K'g)` by
    hand, and the whole lower `(4,−1)` regrading recomputed from the frozen
    `RAW_INPUT.json` (`F_17` empty, `G_17 = Q[ξ]_{≤7}`, 28 slots at
    `ν=18..24`, ceiling 40).
16. `A`-adic pole orders of the forced `g22` for three `F` fixtures.
17. K00: `ℓ0·A = 0`, `A·v1 = A·v2 = 0`, both column relations, `ℓ0·b` = 690
    terms over 33 variables — all symbolic from frozen bytes.
18. K00: `A[5][j] = 0` and `A[0][j]+(16/3)A[2][j]+(128/3)A[4][j] = 0` for
    `j ≤ 5`, symbolic; closed form for `w5`.
19. K00: 441 frozen `5×5` minors → 90 nonzero, 54 distinct, exactly 2
    proportionality classes (36 + 54 occurrences); dropped-row/column
    support structure matched against `u = ℓ0 ∧ w` and `p = v1 ∧ v2`.
20. K00: all 90 compound `2×2` minors of the second adjugate vanish
    symbolically; `(P02/P56)·w5 = 1/384` symbolically for all nine column
    pairs; `u_{02} = 1/384` by hand.
21. K00: `W` identified as the 226-term class representative.
22. K00: `ŵ·A = 0` identically; `C2 = ŵ·b` = 6,702 terms; comparison with
    `Comp6_Comp7` (110,117 / 83,298) and with the 35 `P6` generators
    (max 457 terms).
23. Custody: R3 case freeze lines; all cited evidence hashes resolved to
    real frozen files; V26 atlas byte hash traced through
    `COMPILED_SOURCE.sha256` / `EVIDENCE.sha256` / `RELEASE_V26R1_W0.json`.

**Not checked (out of desk scope):** whether `C1` or `C2` reduces to zero
modulo `P6`; whether `(C1,C2)` generates the same ideal as
`Comp6_Comp7`; any Gröbner/saturation statement; any window-tier
enumeration of prefix strata.

## 9. Scope firewall

This review proves nothing about JC2, `G2-PSC`, `G2-BD`, cofinality,
coverage, any GGV family exclusion, any Keller pair, order two, maximum
twelve, K00 closure, source reachability, a terminal receiver, a compatible
jet, or an arc. It empties one artificial-fixture algebraic gate by
containment in a promoted theorem; it repairs three statements in a
producer-tier ideation report; and it raises four sampled K00 claims to
symbolic identities. A finite fixture is not a family landing, a selected
chart is not a fan cover, a finite jet is not an arc, a proper superlocus is
not a witness, and a model name is not a vote.

No canonical ledger was edited. `jc2-lean` was not entered, listed, read,
built, or status-inspected. No AWS job was launched, inspected, or
disturbed; the two live Box02 processes were neither touched nor signalled.
No heavy algebra ran locally. Exactly one file was written: this report.

Output path: `xmodel/ideation-20260827T1808Z-fable5-hostile-review-opus5.md`
Model identity: Opus 5, exact model ID `claude-opus-5`.
