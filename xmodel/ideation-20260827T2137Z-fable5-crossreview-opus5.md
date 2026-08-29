# Hostile cross-review of the Fable5 blind submission — round `20260827T2137Z`

Reviewer: Opus 5 (Anthropic), exact model `claude-opus-5`, adapter
`ops/adapters/claude.sh`.
Role: equal-standing hostile mathematical reviewer, plane Jacobian campaign.
Target: `xmodel/ideation-20260827T2137Z-fable5.md`.
Status: **REVIEW ONLY.**  Nothing here is promoted; nothing here is a JC2
result.  I wrote exactly one file (this one) and changed nothing else.

---

## 0. Custody gate (fail-closed) and model identity

Mandatory inputs, hashed by me before reading:

```text
edd383ad33838268cc7e700f2aa913dab73eb6744a60133a131a69eb7ef476bb  xmodel/ideation-20260827T2137Z-fable5.md          [MATCHES mandate]
0e09faeb69480b7594864199fbd061291af490cf8e514d1795784fbf00ad9bee  xmodel/ideation-20260827T2137Z-postseal-truth-delta.md  [recorded at session start]
```

The Fable5 hash matches the mandated value exactly; the gate passes and I
proceeded.  Both files were read in full.

Secondary pins recomputed by me this session (all match the values quoted in
the delta or in the ledgers):

```text
49dd042a15670f082ea4335610150eee3022fc7a37282df200e2ae3a052ea0a0  xmodel/ideation-20260827T2137Z-opus5.md              (my own sealed submission)
968b42ced94bd6c59b33bfdab30677e2ad6ad91a349fc978a271c01083d11e7d  xmodel/g2-c74-place-exit-rpmc-hostile-review-opus5-20260827.md
9147ada2c1704a2df10139d79f4863adee53006a6195b9a893f5bd9c343a8e83  xmodel/g2-pure-sigray-bypass-after-transpose-sol-ultra-20260827.md
1cc41972d5049e68b8464a634c1cfae48ec5e0e1ba995475fa90998f7aad3984  xmodel/ideation-20260827T1808Z-opus5-hostile-review-fable5.md
```

Custody hashes that Fable cites for the ladder (`c66b1396`, `8e25502c`,
`afd9565d`) and for the lower FACEPIN promotion (`94c10fd8`, `681357ce`) all
resolve in `notes.md` / `AUDIT.md`.  No fabricated pin found.

---

## 1. Executive verdict

Fable's report contains **one exactly correct and genuinely useful new piece
of mathematics** (the lower-face endpoint local analysis, §9), **one correct
but already-promoted identity presented as new** (the intertwiner, §3.1.1),
**one mechanism whose load-bearing step is a non-sequitur** (Krull finite
determinacy, §3.1.3), **one count that does not support the direction it is
used in** (`29` vs `36`, §9/card 2), and **one section that must be deleted
rather than repaired** (the `C74-PLACE` → `EXIT-RPMC(C)` corridor).

The single most consequential correction: Fable's compression rests on
replacing the campaign's polynomial/windowed row problem with its
localization at `H`.  That replacement is legitimate for the *upper tower
gate rows* — where the promoted condition really is exactness in
`L = K(X)(p)`, and where I reproduce the promoted codimensions `3,4` (P) /
`4,4` (Q) exactly.  It is **illegitimate at the upper endpoint** (where the
promoted record already says the localized row-22 gate is vacuous) and
**illegitimate on the entire lower face** (whose rows are polynomial slot
identities, and whose per-row polynomial obstruction is `7`, not `1` or `2`).
Fable's only anchor for the transfer, `H = X^8-1`, is precisely the fixture
on which the two notions coincide, so it cannot test the step it is used to
support.

Offsetting this, I supply below the exact closed form Fable's §3.1.2 asks for
— **for all `n` and all four sectors at once**, in one line, verified
symbolically — which removes the `q3` "negative control" entirely and
replaces the Krull/rationality scaffolding with a genuinely effective engine.

---

## 2. Itemized verdict table

| # | Claim / object (Fable §) | Verdict | Basis |
|---|---|---|---|
| 1.1 | `T_m(HY) = H·T_{m+4}(Y)` exact (§3.1.1) | **CONFIRMED** | symbolic, this session |
| 1.2 | Induced map is `coker(T_{m+4}) → coker(T_m)`, `[f]↦[Hf]` | **CONFIRMED** | `μ_H(im T_{m+4}) ⊆ im T_m` |
| 1.3 | Isomorphism over `K[X,1/H]` | **CONFIRMED** | `H·im T_{m+4} = T_m(H·V) = im T_m`, `H·V=V` |
| 1.4 | `k_{m+4} = k_m` | **CONFIRMED** (trivial) | `4 | 4e_i` |
| 1.5 | Label **NEW** | **REFUTED** | it is the promoted `r∘(H·)` diagonal iso; written as `M(Y)/H` under `Y=HR` in Fable's own 18:08Z review (`1cc41972`, line 156) |
| 1.6 | "row cokernels are one module, not an unbounded list" ⇒ compression | **REFUTED as stated** | equal dimensions were already promoted (`r-1+k_m`, `k` 4-periodic); the tower is unboundedly many *targets* in 4 fixed spaces, not unboundedly many spaces |
| 1.7 | Localization preserves the campaign's obstruction problem | **SPLIT: CONFIRMED for tower gate rows, REFUTED for endpoint and for the whole lower face** | table in §3.3 below |
| 2.1 | `[t^2](1/2)√F = q2` (§3.1.2) | **CONFIRMED** | symbolic |
| 2.2 | `q3` not a multiple of `[t^3](1/2)√F` | **CONFIRMED** but mis-diagnosed | the exponent is `(n+2)/8`; `n=2` is the unique `n` giving `1/2` |
| 2.3 | "each sector has its own algebraic assembly" | **REFUTED** | one assembly covers all four: `q_n = (2/(n+2))[t^n]P^{n+2}` |
| 2.4 | "the correct closed forms must be taken from the frozen R7R1 construction" | **REGRESSION** | the `q3` closed form was already derived and verified in Fable's own 18:08Z review, line 169; it matches my formula exactly |
| 3.1 | Krull ⇒ "all rows vanish is finitely many conditions" (§3.1.3) | **NON-SEQUITUR** | Krull gives (all coefficients vanish ⇒ γ=0); the needed direction is (finitely many vanish ⇒ all vanish) |
| 3.2 | Abstract finiteness of the tower's cut locus | **TRUE BUT FREE** | Noetherianity on the frozen 121/124-slot space; no Krull, torsion-freeness or residue pairing needed |
| 3.3 | `M_j` finite-rank coherent, torsion-free on integral strata | **GAP, REPAIRABLE** | rank jumps on multiplicity strata (promoted: codim 3 is exactly the squarefree locus); repair = stratify by multiplicity type of `H` |
| 3.4 | Discriminant localization | **MISLOCALIZED** | the discriminant of `P^8=ΣF_n s^n P^n` vanishes on `Z(H)`, which is exactly where the residue obstruction is supported |
| 3.5 | Residue pairings `c_i(s)` are **rational** in `s` | **UNSUPPORTED, likely false** | these are periods of an algebraic family: holonomic, not rational |
| 3.6 | Effective `N0` exists | **NOT ESTABLISHED as claimed; ESTABLISHABLE by a different route** | see the repair in §5.3 (algebraicity ⇒ P-recursion) |
| 3.7 | "endpoint verdict ⇒ stratum verdict" | **REFUTED twice** | (i) generic-point `N0` ≠ uniform family bound, and the live fixtures sit on degenerate strata; (ii) the tower is `F`-side only and `F=0` always satisfies every gate |
| 5.1 | `23` rows, `6` multiples of 4, `23+6=29`; `8+28=36` | **ARITHMETIC CONFIRMED** | recomputed |
| 5.2 | Lower `k_m = 1 ⟺ 4|m` | **CONFIRMED and upgraded** | holds under both candidate offsets (`c0=12`, `c0=20`); the offsets and the row/T-index shift are all `≡0 mod 4` |
| 5.3 | "every unwindowed lower row obstruction space has dimension 1 or 2" | **REFUTED for the row problem** | polynomial coker per row `= 7` (`8` at the one resonant row); sum over rows 18–40 `= 162`, not `29` |
| 5.4 | `29` is the intrinsic obstruction content "at most" | **REFUTED** | `29` upper-bounds one component (a hypothetical localized gate that the card itself must still derive); it bounds nothing about the compiler's rows |
| 5.5 | "PROPER at least as plausible as unit, on obstruction-budget grounds" (§9b) | **UNLICENSED; both natural repairs point the other way** | `G17` is pinned by row 17 (unique solution, verified), so corrected local unknowns `= 28 < 29`; globally the frozen system is 740 generators in 408 variables |
| 5.6 | "windowing can move conditions in both directions" (§10.2) | **FALSE as stated** | windowed solvability implies gate vanishing, so windowing only adds conditions relative to the gate count |
| 5.7 | A proper LF40 is a "falsification attack" (§2) | **CATEGORY ERROR** | promoted: a char-0 unit gives `108→125` conditionally and "would not prove JC2"; a proper result falsifies the bound route, not JC2 |
| 5.8 | Upper anchor `k_22=0, r=8 ⇒ dim 7` matches D5G | **CONFIRMED but non-discriminating** | this is the unique fixture where polynomial and localized answers agree (`7 = 7`) |
| 6.1 | Prefix-unit monotonicity `1∈I_1 ⇒ 1∈I_2` | **CONFIRMED, sound, one-sided** | trivial; cofactor replay is a real certificate |
| 6.2 | Ladder guards as written | **INCOMPLETE** | must forbid specialization and mod-`p` rungs; this lane already produced misleading *specialized* row-22 units |
| 6.3 | Ladder cost premise ("smallest unit prefix typically far cheaper") | **UNEVIDENCED** | removing generators can make a unit certificate harder; no data offered |
| 6.4 | Refute-only partial-forest budget (§3.2.1) | **CORRECT SHAPE, UNSAFE NOW** | needs leaf→end injectivity = **L5**, verdict OPEN in my C74 review; without it a duplicated place yields a *false refutation* |
| 6.5 | `td`, `b1` "both forest-computable" | **CIRCULARITY RISK** | on a partial forest they must come from sources independent of the decoration under test |
| 6.6 | Passport CSP "strictly stronger derived check" (§3.2.3) | **TRUE IN DIRECTION, WEAK IN PRACTICE** | post-seal 5: marked profiles prune 169→48 and kill none; ordinary passports lose the marking on `e=1` fixed ends |
| 7.1 | `C74-PLACE` → `EXIT-RPMC(C)` as the live corridor (§1 av.2, §2, §4, §5, card 3) | **DELETE** | post-seal 1–3; my own review Q4a/Q6e/Q6f |
| 9.1 | Lower endpoint local analysis: `g(0)=g(ρ)=0`, `h(ρ)=-4/17`, degree dichotomy, `γ≡3 mod 4` | **CONFIRMED EXACTLY, and it is a real upgrade** | verified symbolically; uniform in `γ`, removing the promoted `γ≤11` restriction |

---

## 3. Item 1 — the intertwiner, its direction, and localization

### 3.1 The identity is exact

With `T_m(Y) = 4HY' + (m-12)H'Y`:

```text
T_m(HY) = 4H(H'Y + HY') + (m-12)H'HY = H[4HY' + (m-8)H'Y] = H·T_{m+4}(Y).
```

Verified symbolically (`/tmp/xr`, difference identically `0`).  The induced
map is `coker(T_{m+4}) → coker(T_m)`, `[f] ↦ [Hf]`, exactly as Fable states
(a map `φ` with `φ(S) ⊆ T` induces `A/S → B/T`; the direction is right).
Over `K[X,1/H]` it is an isomorphism because `H·V = V` there, so
`H·im T_{m+4} = T_m(H·V) = im T_m` with equality, and `μ_H` is bijective.
`k_{m+4} = k_m` is immediate.  **All four sub-claims CONFIRMED.**

### 3.2 It is not new, and its promoted reading is the opposite one

The instance `(m, m+4) = (18, 22)` is written in the promoted record as
`M(Y)/H` under `Y = HR` — "the promoted `r∘(H·)` diagonal iso"
(`xmodel/ideation-20260827T1808Z-opus5-hostile-review-fable5.md`, line 156,
Fable's own review).  The source audit that named it states its consequence:

> `r∘(H·): V_6 → V_6` is a diagonal isomorphism.  Without a source-pinned
> raw-to-Morse compiler that fixes the `H`-multiple, the proposed 16
> factorwise types do **not** carry one intrinsic seven-vector each.

That is, the campaign's promoted reading of this exact map is that it
**destroys** the information needed to pin the source, which is why a
provenance compiler is required.  Fable proposes the same map as the engine
of a compression.  Both readings cannot stand; the promoted one is correct,
and §3.3 shows why quantitatively.

Independently: my own blind submission of this round states the same gauge
witness (`H·∇_{m+4} = ∇_m·H`, §3.0) and labels it **KNOWN**, crediting
Fable's 18:08Z representative-independence theorem.  Two blind reviewers
reaching it independently while one of them files it as known is decisive
against the **NEW** label.  The genuine increment over the promoted statement
is only that the isomorphism is *canonical* rather than dimension-level.

### 3.3 Localization does not preserve the decision-relevant problem

Two different obstruction spaces are in play, and the report slides between
them.  For `deg H = 8` the polynomial cokernel of `T_m : K[X] → K[X]` is
`deg H - 1 = 7` for every `H` and every non-resonant `m` (the images of
`X^k` have leading coefficient `4k + 8(m-12)` and pairwise distinct degrees
`k+7`).  The localized cohomological dimension is `r - 1 + k_m`.  Computed
exactly this session (stable in the truncation degree `D = 14…60`):

| fixture | `m` | polynomial coker | localized `r-1+k_m` | agree? |
|---|--:|--:|--:|---|
| `X^8-1` squarefree, `r=8` | 18 / 22 / 23 | 7 / 7 / 7 | 7 / 7 / 7 | **yes** |
| branch P `H=A^2`, `r=4`, `e_i=2` | 18 / 22 / 23 | 7 / 7 / 7 | 4 / 4 / 3 | no |
| `r=1` control `H=(X-1)^8` | 18 / 22 / 23 | 7 / 7 / 7 | 1 / 1 / 1 | no |
| branch P, promoted gate rows | 25 / 26 | 7 / 7 | **3 / 4** | no |
| branch Q `H=A^2B`, `r=5` | 25 / 26 | 7 / 7 | **4 / 4** | no |

Three readings follow, and they must be kept apart.

1. **Upper tower gate rows: localization is legitimate.**  R7R1's condition
   is "`q_n dX` is exact in `L = K(X)(p)`" — a genuinely localized
   condition.  The localized column reproduces the promoted row-25/26
   codimensions `3,4` (P) and `4,4` (Q) on the nose.  Fable's intertwiner
   applies here, and here it is correct.
2. **Upper endpoint: localization is destructive.**  The promoted record
   already states that row 22 on branch P with poles allowed is **vacuous
   (codim 0)**, against `7` for polynomial-only `Y`; "endpoint (R4) death is
   support-side, not class-side."  Localizing does not shrink the endpoint
   obstruction, it annihilates it.
3. **The anchor cannot test the transfer.**  Fable's sole numerical anchor
   (`H = X^8-1`, `k_22=0`, `r=8`, `dim 7`) is the unique row of the table
   where the two notions coincide.  It confirms arithmetic and discriminates
   nothing.

Finally, the frozen `D3` slot windows have `X`-degrees
`max(0,ceil((w-8)/3)) .. 16-w`, with top degree *decreasing* in `w`, while
`μ_H` raises `X`-degree by `8`.  So multiplication by `H` maps no frozen
window into any other frozen window; the isomorphism exists only after
inverting `H`.  **Item-1 verdict: identity CONFIRMED, novelty REFUTED,
preservation of the campaign's problem REFUTED outside the tower gate rows.**

---

## 4. Item 2 — the sector assembly, closed forms supplied

### 4.1 The exact closed form, for all `n` and all four sectors

Fable's §3.1.2 verifies one sample and then concedes that "the correct closed
forms must be taken from the frozen R7R1 construction."  They need not be
taken from anywhere; they follow in one line.  With R7R1's setup
`F_0 = H^2`, `p^4 = H`, `P = F^{1/8}`, `s = t/P`, `Q = P^2 = Σ q_n s^n`, the
defining relation is `t = s·F^{1/8}`.  Lagrange inversion with
`φ = F^{1/8}`, `ψ = F^{1/4}` gives, for `n ≥ 1`,

```text
[s^n] F^{1/4} = (1/n)[t^{n-1}]( (1/4)F^{-3/4}F_t · F^{n/8} )
              = (1/(4n))[t^{n-1}]( F^{(n-6)/8} F_t )
              = (1/(4n))·(8/(n+2))·[t^{n-1}] d/dt F^{(n+2)/8},
```

hence

```text
        q_n = (2/(n+2)) · [t^n] F^{(n+2)/8}  =  (2/(n+2)) · [t^n] P^{n+2}.     (★)
```

**Verification (symbolic, exact, this session).**  In
`Q[F_1..F_8][u, u^{-1}]` with `u = H^{1/4}`, I computed `t(s)` by direct
series reversion of `t = s F^{1/8}`, substituted, expanded `Q = F^{1/4}` to
order `s^8`, and compared with `(★)`:

```text
n = 0,1,2,3,4,5,6,7,8   reversion == Lagrange :  True (all)
q0 - p^2                                     = 0
q1 - F1/(4p^5)                               = 0        [R7R1 (0.4)]
q2 - (F2/(4H) - F1^2/(16H^3))                = 0        [R7R1 (0.4)]
q3 - p^5[F3/(4H^2) - (3/32)F1F2/H^4 + (11/512)F1^3/H^6] = 0   [promoted closed form]
```

Three consequences fall out immediately, all of them things the report either
asks for or gets wrong:

- **The `q3` "negative control" evaporates.**  `q_n` is a multiple of
  `[t^n]F^{(n+2)/8}`; the exponent depends on `n`, and `n = 2` is the unique
  index at which `(n+2)/8 = 1/2`.  The failure of the single-function guess
  is a statement about the exponent, not about sectors having separate
  assemblies.  There is **one** assembly.
- **The `μ_4` character is a corollary, not an input.**  `q_n =
  (2/(n+2))[t^n]P^{n+2}` and `p ↦ ζp` give `q_n ↦ ζ^{n+2} q_n`.  Verified
  directly: every `u`-exponent appearing in `q_n` is `≡ n+2 (mod 4)` for
  `n = 0..5`.
- **Triangularity is a corollary.**  The `F_n`-linear term of `(★)` is
  `(1/4)u^{n-6}F_n = F_n p^{n+2}/(4H^2)`, reproducing the shape already
  derived in Fable's 18:08Z review and used in my §3.4.

### 4.2 Regression finding

The `q3` closed form quoted above is not new to the campaign: it is
`xmodel/ideation-20260827T1808Z-opus5-hostile-review-fable5.md` line 169,
authored by Fable earlier the same day, "verified against six random exact
fixtures," and carried in the promoted gate-law ledger.  The sealed 21:37Z
report files it as an open item.  This is a self-regression against reviewed
work, not a campaign gap, and it is the reason §3.1.2's "documented failed
attempt" reads as a discovery rather than as a step already taken.
`(★)` is the natural completion of the very method §5.1 of that review used
(binomial expansion plus inversion of `t = sP(t)`), carried past the linear
term to closed form at all orders.

---

## 5. Item 3 — Krull, strata, pairings, and `N0`

### 5.1 The Krull step is a non-sequitur

Fable: "If all its `s`-coefficients vanish, then `γ_j` lies in `∩_N s^N M_j`,
which is zero by Krull … **So** 'all rows of sector `j` vanish' is finitely
many conditions."

Krull/Artin–Rees delivers `(all coefficients vanish) ⇒ γ_j = 0`.  The
statement the mechanism needs is `(finitely many coefficients vanish) ⇒ all
vanish`.  These are converse to one another; nothing in the quoted argument
bridges them.  Moreover, if `γ_j` is a *formal* section — an element of
`M_j ⊗ K[[s]]` or of the completion, which is where "assemble the rows into a
section" naturally lands — then `∩_N s^N = 0` merely restates the hypothesis
and the step is vacuous.  It has content only if `γ_j` is a genuine element
of the finitely generated `M_j`, which is an unstated and nontrivial premise.

### 5.2 The abstract finiteness is free; only effectivity is content

The tower's rows are polynomial conditions on the frozen, finite `F`-slot
space (121 slots for `n ≤ 12`, 124 including `F_13, F_14`; the window
`max(0,ceil((n-8)/3))..16-n` is empty for `n ≥ 15`).  The ideals generated by
rows `0..N` form an ascending chain in a Noetherian ring, so they stabilize
and the cut locus is already cut by finitely many rows.  No Krull, no
torsion-freeness, no integral strata, no residue pairing is required for the
qualitative statement.  Card 1's only nontrivial content is therefore the
**effective** `N0` — and that is the part the report sketches rather than
establishes.

Two further defects in the supporting apparatus:

- **Torsion-freeness / integral strata — GAP, repairable.**  `M_j` is not
  locally free over the `H`-parameter space: `dim H^1 = r-1+k_m` jumps on
  multiplicity strata, and the promoted record is explicit that "codim 3 is
  exactly the squarefree locus … `A = C^2` or double root → 2; triple root →
  1."  The repair is available from the promoted law itself: stratify by the
  multiplicity type of `H`; on each such stratum the dimension is constant,
  `M_j` is locally free, and torsion-freeness is then legitimate.  This must
  be done first, not assumed.
- **Discriminant localization — MISLOCALIZED.**  The discriminant of
  `P^8 = Σ F_n s^n P^n` in `P` vanishes where `H` does (at a root of `H`,
  `P = 0` is an eight-fold root).  The gate obstruction is a residue
  supported exactly on `Z(H)`.  Localizing away the discriminant deletes the
  support of the object being measured.

### 5.3 Rationality is the wrong finiteness class — and the right one is available

Fable's effectivity rests on the pairings `c_i(s)` being **rational** in `s`
with a resultant-computable degree bound.  No argument is given, and the
natural object — a residue/period of an algebraic family — is holonomic, not
rational.  I recommend discarding that route and replacing it with the
following, which is exact, already promoted in substance, and desk-scale.

From `P = F^{1/8}` and `t = sP`:

```text
P^8 = F(X, t) = Σ_n F_n(X) t^n = Σ_n F_n(X) s^n P^n .                     (†)
```

I verified `(†)` symbolically to order `s^8` (residual coefficients all
zero); it is the promoted R7R2 relation `P^8 = F(X,sP)`.  Since `F_n = 0` for
`n ≥ 15`, `(†)` is a polynomial equation of degree `≤ 14` in `P` with
coefficients in `K(X)[s]`.  Hence `Q = P^2 = Σ q_n s^n` is **algebraic** over
`K(X,s)` of degree `≤ 14`, therefore holonomic, therefore each gate sequence
`n ↦ λ_{n mod 4}(q_n)` is **P-recursive** with an effectively computable
recursion of order `d` and leading coefficient `L(n)`.  A P-recursive
sequence vanishing on `d` consecutive indices beyond the largest integer root
`n*` of `L` vanishes forever.  So

```text
N0 = n* + d,     both computable from the frozen F-window by
                 algebraic → holonomic → recursion, no new theory.
```

This is a real effective bound, and it is exactly what card 1 wants.

### 5.4 Pointwise/generic determination is not a uniform family bound

The recursion in §5.3 has coefficients depending on the `F_n(X)`, so `d` and
`n*` depend on the point of the stratum.  Fable's own phrasing is careful —
"per stratum, per sector … on the generic point of the stratum" — but the
consequence drawn is not: "upgrading **any** finite endpoint decision into a
stratum decision" silently promotes a generic bound to a uniform one.  A
uniform family `N0` requires `d` and the integer-root bound for `L` to be
constant along the stratum; that is a constructible-stratification statement
nobody has made.  It matters concretely here, because the campaign's live
fixture `H = A^2`, `A = X^4-1` is *not* squarefree: it sits on a degeneracy
stratum, which is exactly where generic bounds fail and where the promoted
record already records the codimension dropping from 3 to 2 to 1.

### 5.5 Even a perfect `N0` does not deliver the advertised consequence

Card 1's value proposition is that a tower-capacity theorem converts endpoint
decisions into family statements.  Per my own (blind, unreviewed) row-budget
analysis this cannot hold: the tower is an `F`-side necessary condition
against a census of `F: 124` / `G: 276` positive-weight slots, and `F = 0`
lies in the gate locus of every row, so emptiness can only ever come from the
inhomogeneous endpoint target `D22 = 1`.  I flag that this counter-argument
is my own same-round submission and carries no more standing than Fable's; it
is a live disagreement, and §11's discriminator 1 settles the shared part.

---

## 6. Item 4 — composition with the `mu_4`-torsor capacity identity

**What composes.**

- *Four fixed character spaces.*  My `V_H = {p^4 = H} → U` is a finite étale
  `μ_4`-torsor with `O_{V_H} = ⊕_j O_U p^j`, the `p^j` summand carrying
  `∇_j`; Fable's intertwiner is the same 4-periodicity realized as a
  canonical isomorphism instead of a decomposition.  They are two
  presentations of one fact, and both reduce to the promoted
  representative-independence.  `(★)` above now gives the character law
  directly, so all three derivations agree.
- *Repeated rows.*  My capacity identity `Σ_j dim H^1(U,∇_j) = b_1(V_H) =
  4(r-1) + c`, `c = Σ_j k_j` (verified against the frozen `42/51/12/87`),
  quantifies what Fable's intertwiner explains structurally: the target space
  repeats with period 4, so the cutting rate is `b_1(V_H)/4` per row forever.
  Complementary, no conflict.
- *Coefficient windows.*  Both of us argue unwindowed-first and both flag it.
  I add the missing direction: for the *polynomial* row problem the
  unwindowed answer is `7`, not `r-1+k_m`, and windowing only increases it.

**What conflicts.**

1. *Finitely many spaces vs finitely many conditions.*  Fable's §3.1.1
   conclusion ("one module, not an unbounded list") suggests bounded content.
   My budget says the opposite: `121/124` `F`-slots require roughly 23 more
   rows on P and 17 on Q, at `3.5`/`4.25` conditions per row.  Four fixed
   target spaces do not bound the number of conditions, because
   `F ↦ [q_n dX]` is a different nonlinear map for each `n` — `(★)` makes the
   nonlinearity explicit (`q_5` already carries `F_1^5`).
2. *Nonlinear gate independence.*  Neither report has it.  My `≥ 79 / ≥ 70`
   residuals and Fable's `29` both assume independence.  This is the shared
   unproven premise of both budgets and should be stated as such in any
   promotion.
3. *Effective family determination.*  Neither report established it.  I
   supplied the schedule (how many rows), Fable supplied the question; §5.3
   supplies the machinery.  None of the three is a uniform family bound.

---

## 7. Item 5 — the lower-face transfer and `29` vs `36`

### 7.1 What is right

The arithmetic checks out: rows `18..40` is 23 rows; multiples of 4 in
`[18,40]` are `20,24,28,32,36,40`, six of them; `23+6 = 29`; and
`8 + 28 = 36` from the promoted census (`F_17` empty, `G_17 = Q[ξ]_{≤7}`, 28
G-slots at weights 18–24).  `K_ρ = ξ(ξ-ρ)^7` gives `r = 2`, `e = (1,7)`, and
`gcd(7,4)=1` makes `4|7m ⟺ 4|m`.  The endpoint twist has residues `-3/4` and
`-21/4 ≡ -1/4 (mod Z)`, both non-integral, so `k = 0` and the localized
cokernel is `r-1 = 1`.  All confirmed.

Better than Fable claims: the `k_m` schedule, flagged in §10.2 as "asserted
by analogy," is in fact **robust**.  The two candidate normalizations are
`c0 = 12` (direct analogy with the upper `T_m`) and `c0 = 20` (forced by the
endpoint coefficient `-3` sitting at compiler row 17).  Both are `≡ 0 mod 4`,
and the row/T-index shift `8` is too, so `k_m = 1 ⟺ 4|m` either way.  I
verified this by computing both schedules; they agree on all 23 rows.  The
genuinely load-bearing unverified assumption is not the offset but the
**slope**: that the twist advances by exactly `1/4` per row.  That is
discriminator 3 in §11.

### 7.2 Why the count is not a budget

**(a) `29` counts the wrong object.**  The lower compiler rows are polynomial
identities in `ξ` on frozen slot windows, not exactness conditions in a
Kummer field; and the lower gate structure (which rows carry which twists) is
precisely what card 2 must still derive (§10.2, leap 2).  Using the localized
dimension before deriving the lower gate assumes the conclusion.  The correct
unwindowed count for the row problem is the polynomial cokernel of
`Y ↦ 4KY' + cK'Y`, which I computed exactly for all 23 rows:

```text
c0 = 20 :  poly coker = 7 for every row except m = 20 (resonant, = 8);  Σ = 162
c0 = 12 :  poly coker = 7 for every row;                                Σ = 161
either   :  localized Σ (Fable's "29")                                  =  29
```

So the "intrinsic obstruction content … at most `23+6 = 29` scalars" is short
by a factor of about `5.6`, and §9's headline that "the lower face is nearly
scalar" is false for the object the LF40 lanes actually solve.

**(b) The inequality runs the wrong way for the inference.**  A window sits
inside `O(U)`, so windowed solvability *implies* class vanishing: the gate
conditions are a subset of the compiler's conditions.  Windowing therefore
only *adds* conditions relative to the gate count, contradicting §10.2's
hedge that it "can move conditions in both directions."  And a gate can
impose *fewer* conditions than its dimension — the promoted row-22 branch-P
vacuity (codim 0 against dimension 4) is the campaign's own witness.  So `29`
is an upper bound on one component only; it bounds nothing above or below on
the decision.

**(c) The `36` double-counts freedom.**  `G_17`'s eight slots are not free.
The row-17 equation is the endpoint ODE, whose homogeneous solutions are
`c·K^{3/4}` — not polynomial — so its polynomial solution is unique.  I
verified this directly: no solution of degree `≤ 5`, a unique solution at
degree `6`,

```text
g = 4ξ - (84/5)ξ^2 + (448/15)ξ^3 - (1792/65)ξ^4 + (14336/1105)ξ^5 - (8192/3315)ξ^6   (ρ = 1),
```

and solving in `Q[ξ]_{≤7}` returns the same vector with zero top coefficient.
So either count row 17 as its conditions *and* `G_17` as unknowns (net zero),
or drop both.  Fable keeps the unknowns and drops the conditions.  Corrected
local unknowns are `28`, against Fable's own `29` — the naive comparison
flips to over-determined.

**(d) The truncation is not neutral.**  Rows 18–40 also involve the 141
`F`-slots and the G-slots below weight 17.  Globally the frozen system is 740
generators in 408 variables after FACEPIN, which points the opposite way from
the local sub-budget.  Neither count decides anything, which is the point.

**Conclusion.**  §9(b) — "a PROPER LF40 outcome is at least as plausible as
the unit … on obstruction-budget grounds" — is unlicensed, and its two most
natural repairs point toward unit.  Card 2 should keep its *windowed* ledger
plan (which is the right object) and drop the unwindowed orientation number
entirely.  Additionally, §2 mislabels a proper LF40 as a falsification
attack: per the promoted verdict, a char-0 unit would raise a conditional
degree bound `108 → 125` and "would not prove JC2", so a proper result
falsifies the bound-improvement route, not the conjecture.  Relabel it a
programme-falsification.

### 7.3 What survives, and is worth promoting

Fable's §9 local analysis is exactly right and I confirm every step
symbolically.  At a root of multiplicity `e`, writing `K = (ξ-ρ)^e w` and
dividing by `(ξ-ρ)^{e-1}` gives `-3e·w(ρ)g(ρ) = 0`, hence `g(ρ) = 0` — **one
evaluation condition per distinct root, independent of multiplicity**.
Setting `g = (ξ-ρ)h` gives `(4 - 3γ)h(ρ) = 4`, i.e. `h(ρ) = 4/(4-3γ)`, which
is `-4/17` at `γ = 7` (confirmed numerically) and is finite for every integer
`γ`, so there is no further local obstruction.  The leading-degree equation
forces `deg g ∈ {1, 3deg K/4}`, and a degree-one `g` with two forced zeros is
zero, so `4 | deg K`, i.e. `γ ≡ 3 (mod 4)`.  **This is uniform in `γ` and so
strictly upgrades the promoted necessity statement, which was verified only
for `γ ≤ 11`.**

---

## 8. Item 6 — the two one-sided tools

### 8.1 Prefix-unit ladder (§6): sound, under-guarded

The mathematics is trivially correct and genuinely one-sided: literal
generator subsets `I_1 ⊆ I_2` give `1 ∈ I_1 ⇒ 1 ∈ I_2`, properness of a
prefix gives nothing, and the exact-`Q` cofactor replay is a real
certificate.  The custody pins resolve.  One structural improvement Fable
does not note: the held 466-generator system is a subset **plus** a replay of
the 47 omitted generators through 697 cofactor entries, so it is
*ideal-equal* to the full system, strictly stronger than a prefix.

Two guards must be added, both from this lane's own history:

1. **No specialization.**  The ledger records that "exact tail cutoffs 11 and
   10 each returned a literal specialized row-22 unit, excluding only those
   positive-search specializations and not the full fixture."  A specialized
   unit is not a subset unit and does not lift.  Every rung must be a literal
   generator subset in the identical ring with identical variables — no
   fixing, no cutoff, no substitution.
2. **No modular or truncated rung may report UNIT.**  `1 ∈ I mod p` does not
   imply `1 ∈ I` over `Q` (`(2x-1)` is proper over `Q`, unit mod 2), and an
   aborted or degree-capped Gröbner run proves no membership.  Fable's
   exact-`Q` replay discipline covers this if stated as a precondition rather
   than as a post-hoc check.

The cost premise ("the smallest unit prefix is typically far cheaper") is an
unevidenced heuristic and can invert: dropping generators often makes a unit
certificate harder to reach, not easier.  Not a mathematical error; it should
not be used to justify capacity allocation without the ten-minute measurement
in §11.6.  Reach is also bounded: a fixture unit kills only the fixture
(Fable says so itself in §4), and a char-0 unit yields `108 → 125`, not JC2.

### 8.2 Finite-end / passport validator (§3.2, card 3): correct shape, unsafe today

The parent identity `Σ_N e_S = td + b_1(C) - 1` is confirmed post-seal, and
refute-only semantics on a partial forest is the right one-sided design.  Its
soundness, however, requires `Σ_{known} e_S` to be a genuine **lower** bound,
which requires the leaf→end map to be injective — no place counted twice
across charts or deck orbits.  That is exactly **L5 (deck / leaf-place
bijection / no duplication)** in my C74 review, verdict **OPEN**.  Without
L5, a duplicated place inflates the partial sum and can trigger a **false
refutation** — the worst possible failure for a fail-closed tool, since it
would discard a correct forest and send the lane hunting a nonexistent bug.
So layer 1 is safe *now* only if leaf→end injectivity is certified per forest,
or if the sum is taken over distinct certified places only.

Second requirement: `td` and `b_1` must come from sources independent of the
decoration under test.  On a partial forest `b_1` of the generic fibre is not
in general forest-computable, and deriving it through the identity being
tested makes the check circular.

Layer 2 (two-pencil equality) inherits both requirements twice and needs
completeness, so it is not available now.  Layer 3 (passport CSP) is correct
in direction — Riemann existence plus transitivity plus product-one is
strictly stronger than the Euler-characteristic shadow — but post-seal fact 5
shows its demonstrated power is low: the marked-profile congruence prunes 169
passports to 48 and kills none of them, ordinary passports lose the marking
on `e=1` fixed ends, and braid orbits act on branch values rather than sheet
blocks.  Fable's step "complete decorations determine the full branch data"
is precisely where the marking is lost.

**Safe now:** layer 1, conditional on a per-forest injectivity certificate and
independent `td`/`b_1`.  **Depends on a complete marked place dictionary:**
layer 2 equality, layer 3, and any completeness certificate.

---

## 9. Item 7 — post-seal corrections applied; the stale corridor is deleted

Per post-seal facts 1–3, and consistently with my own review
(`968b42ce`, verdicts Q4a **REFUTED**, Q6e **CONFIRMED**, Q6f **GAP**), the
following are **deleted, not repaired**:

- **§2 bottleneck 1** in full, including the claim that `EXIT-RPMC(C)` is
  "the only named path to a type-relative degree theorem `d ≤ C·α·β`".  Given
  its own clause 1, `EXIT-RPMC(C) ⟺ RPMC(C)`; it localizes notation and
  removes no proof cost.
- **§1 avenue-2 raise reason.**  The stated justification is "the `C74-PLACE`
  → `EXIT-RPMC(C)` corridor interfaces."  That justification is void.  The
  raise may survive on the pure-Sigray intrinsic two-chart forest plus the
  acceptance tests, but it must be re-based; as written it is unsupported.
- **§4 composition rows 1 and 2** ("intrinsic two-chart forest × `C74-PLACE`:
  composes, guarded"; "`C74-PLACE` × `EXIT-RPMC(C)`: composes, sequential").
  The guard is moot: the corridor cannot supply the missing physical chart at
  all.  L1 face-power custody and L2 multiplicity convention are available
  natively; L4 chart coverage belongs to the exact-pair constructor; L3 and
  L5 remain open.
- **§5 proof attack** as framed ("`C74-PLACE`, stated and proved first for one
  exact generic fibre and one chart").  Refile as native L1/L2 work plus the
  two open clauses, dropping "other chart" throughout.
- **Card 3's dependency line** "VGG Proposition 7.3/Corollary 7.4 (provisional
  corridors)".  Native 7.1/7.2 subsume the transposed packet and are strictly
  stronger for `l > 1`; the exact powers 12 and 8 remain correct but are
  natively supplied.

Post-seal fact 4 additionally forecloses the obvious escape: VGG minimal
re-selection is chart-rigid, so same-orbit re-selection cannot expose the
missing chart.  Surviving from card 3: the acceptance-test layers, which
never used the corridor, subject to §8.2.

Small errata to carry into any G2 reuse (post-seal 6): frozen orientation is
`(m,n) = (β,α) = (3,2)` and `(α,β) = (2,3)`; proximity closure means the full
relation "proximate to," not merely the parent edge; the correct primary
source hashes are VGG TeX `b4908fd5…` and GGV5 TeX `8f5571e5…`.

---

## 10. Narrowest promotable theorems

**T1 (new here; supersedes card 1's §3.1.2).**  In the R7R1 setting
(`F_0 = H^2`, `P = F^{1/8}`, `s = t/P`, `Q = P^2 = Σ q_n s^n`),

```text
q_n = (2/(n+2)) · [t^n] P^{n+2} = (2/(n+2)) · [t^n] F^{(n+2)/8}   for all n ≥ 0,
```

with corollaries: (i) one algebraic assembly serves all four sectors, so the
`q3` mismatch is not evidence of sector-wise assemblies; (ii) `q_n^σ =
ζ^{n+2}q_n` is immediate; (iii) the triangular form `q_n = F_n p^{n+2}/(4H^2)
+ NL(F_1..F_{n-1})` is immediate; (iv) `P^8 = Σ_n F_n s^n P^n` with `F_n = 0`
for `n ≥ 15` makes `Q` algebraic of degree `≤ 14` over `K(X,s)`, hence
`(q_n)` P-recursive with an effectively computable recursion.  Verified
symbolically against direct reversion for `n ≤ 8` and against R7R1 `(0.4)` and
the promoted `q3`.  *Scope: exact identity; no capacity or finiteness claim.*

**T2 (Fable's, verified and generalized).**  For `K = ξ(ξ-ρ)^γ`, `ρ ≠ 0`, any
polynomial solution of `4Kg' - 3K'g = 4K` satisfies `g(0) = g(ρ) = 0` and
`deg g ∈ {1, 3deg K/4}`; the degree-one branch is killed by the two zeros;
hence `4 | deg K`, i.e. `γ ≡ 3 (mod 4)`.  The local coefficient at the
multiple root is `h(ρ) = 4/(4-3γ)` (`= -4/17` at `γ = 7`), so there is no
local obstruction beyond the evaluation.  *This is uniform in `γ` and
supersedes the promoted "proved for `γ ≤ 11`."*

**T3 (new here; corrects card 2's budget).**  For `deg K = D`, the polynomial
cokernel of `Y ↦ 4KY' + cK'Y` on `K[ξ]` is `D - 1` whenever `4k + cD ≠ 0` for
all `k ≥ 0`, and `≥ D-1` always.  On the LF40 face (`D = 8`) this is `7` per
row (`8` at the single resonant row), summing to `161`–`162` over rows 18–40,
against the localized `29`.  Consequently the localized dimension `r-1+k_m`
is not an upper bound on the compiler's per-row conditions, and no
proper/unit direction may be read from `29` vs `36`.

---

## 11. Cheapest discriminator per surviving conjectural step

1. **Card 1 effectivity (replaces the residue-pairing plan).**  Take the
   frozen branch-P `F`-window, form `P^8 - Σ F_n s^n P^n`, run
   algebraic → holonomic to get the ODE for `Q`, convert to the P-recursion
   for `q_n`, and read the order `d` and the largest integer root `n*` of the
   leading coefficient; `N0 = n* + d`.  Degree `≤ 14`, desk-scale, exact.
   *PASS:* the first effective tower bound, with no Krull and no rationality
   hypothesis.  *FAIL:* the leading coefficient admits no integer-root bound
   — report and stop; the Krull route does not rescue it.
2. **Generic vs uniform.**  Run discriminator 1 twice, at a squarefree `H` and
   at the degenerate live fixture `H = A^2`, `A = X^4-1`, and compare `d` and
   `n*`.  If they differ, the "endpoint verdict ⇒ stratum verdict" upgrade is
   dead as stated and must be restricted to the generic locus explicitly.
3. **Lower-face slope (the real load-bearing assumption).**  From the frozen
   lower recurrence (`ν_F = 8-4i+j`, `ν_G = 12-4i+j`), extract the linear part
   of `Dtil_18` in the top `G`-slot and read the coefficient of `K'g`.  One
   row, desk-scale.  It decides whether the twist advances by `1/4` per row
   and therefore whether any `k_m` schedule on this face is real.  (The
   *offset* needs no test: both candidates are `≡ 0 mod 4`.)
4. **Card 2 ledger, corrected.**  Recompute rows 18–24 with the windowed
   polynomial cokernel, not `r-1+k_m`, and compare with the first LF40 lane
   to report early-row elimination ranks.  The prediction under test is `7`
   (or `8` at `m=20`) per row, not `1`–`2`.  A lane rank matching `1`–`2`
   would refute T3's applicability and would itself be the news.
5. **Validator safety (before any live run).**  On the live corner (one deck
   orbit, four roots, known pole tags), certify leaf→end injectivity
   explicitly.  Until then run the budget over *distinct certified places*
   only.  Cost: an afternoon, and it is a precondition, not an afterthought.
6. **Ladder cost premise.**  Before committing Box03 capacity, run the
   smallest rung and the full system side by side for ten minutes and compare
   first degree fall.  If the prefix is not faster, the ladder's entire value
   proposition is void and the held quotient should simply run.

---

## 12. What Fable supplied that is unique relative to Opus

Stated plainly, and credited without discount:

1. **The lower-face endpoint local analysis (§9).**  Every step verified
   exactly.  "One evaluation condition per distinct root, independent of
   multiplicity", `h(ρ) = 4/(4-3γ)`, the degree dichotomy, and the
   observation that the degree-one solution is a leading-order mirage —
   together giving a **uniform-in-`γ`** proof of `γ ≡ 3 (mod 4)` where the
   promoted record had only `γ ≤ 11`.  This is not in my report in any form
   and is the round's cleanest small theorem.  Its negative companion (no
   local obstruction at the multiplicity-7 root) is also genuinely useful: it
   redirects future lower-face mode searches away from local analysis.
2. **The refute-only partial-forest semantics and the two-pencil budget.**  I
   proved the identity's compositions with avenues 7 and 26; I did not state
   a one-sided validator discipline for partially decorated forests.  That
   discipline is the correct shape for a compiler audit and survives the
   corridor deletion.  It is not safe until L5 is certified, but the design
   is Fable's and it is right.
3. **The prefix-unit ladder as an operational design.**  Mathematically
   trivial, but the certificate/replay discipline and the containment of the
   held quotient as the top rung rather than a competitor are good
   engineering that I did not propose.
4. **The explicit lower-face structural reading** (`r = 2`, `e = (1,7)`,
   `gcd(7,4) = 1`) and the residue check on the endpoint twist.  Correct, and
   the `k_m` schedule turns out to be more robust than Fable claimed.

Where I am ahead: the closed form `(★)` and its four corollaries; the
identification of the correct finiteness class (algebraic ⇒ holonomic ⇒
P-recursive) in place of Krull-plus-rationality; the capacity identity
`b_1(V_H) = 4(r-1) + Σ_j k_j` and the row budget; and the polynomial-versus-
localized separation that decides item 1 and corrects item 5.

---

## 13. Errata list (precise, for the record)

| # | Location | Error | Correction |
|---|---|---|---|
| E1 | §3.1.1, §3.1 label | Intertwiner labelled **NEW** | It is the promoted `r∘(H·)` diagonal iso, instance `M(Y)/H` under `Y = HR`, written in Fable's own 18:08Z review line 156 |
| E2 | §3.1.1 | "the row cokernels are one module, not an unbounded list" used as compression | Equal dimensions were already promoted; the tower's unboundedness is in the targets, not the spaces |
| E3 | §3.1.2 | "the correct closed forms must be taken from the frozen R7R1 construction" | `q_n = (2/(n+2))[t^n]P^{n+2}`; and the `q3` case is already in Fable's 18:08Z review line 169 |
| E4 | §3.1.2 | "each sector has its own algebraic assembly" | One assembly; sectors are `n mod 4` of the exponent `(n+2)/8` |
| E5 | §3.1.3 | Krull used to conclude finitely many conditions | Converse direction; the correct engines are Noetherianity (abstract) and P-recursion (effective) |
| E6 | §3.1.3 | "finite-rank coherent module … torsion-freeness … then integrality" | Rank jumps on multiplicity strata; stratify by multiplicity type of `H` first |
| E7 | §3.1.3 | "discriminant-localized locus" | The discriminant vanishes on `Z(H)`, the support of the obstruction |
| E8 | §3.1.3 | pairings "rational in `s` with a resultant-computable degree bound" | Holonomic, not rational; use the P-recursion bound instead |
| E9 | §3.1.3 / card 1 | "generic point of the stratum" used to license stratum decisions | Generic ≠ uniform; the live fixture is on a degenerate stratum |
| E10 | §3.3, §9, card 2 | "every unwindowed lower row obstruction space has dimension 1 or 2"; "at most `23+6=29` scalars" | For the row problem the per-row polynomial cokernel is `7` (`8` at `m=20`); `Σ = 161`–`162` |
| E11 | §9(b) | "PROPER at least as plausible as the unit … on obstruction-budget grounds" | Unlicensed; `G_17` is pinned by row 17 (unique degree-6 solution verified), giving 28 unknowns against ≥29 conditions |
| E12 | §10.2 | "windowing can move conditions in both directions" | Windowed solvability implies gate vanishing, so windowing only adds |
| E13 | §2 (falsification 2) | A proper LF40 framed as a falsification attack | It falsifies the `108→125` bound route, not JC2 |
| E14 | §3.3 anchor | `H = X^8-1` used to validate the transfer | The unique fixture where polynomial and localized answers coincide; non-discriminating |
| E15 | §2 (bottleneck 1), §1 av.2, §4 rows 1–2, §5, card 3 deps | `C74-PLACE` → `EXIT-RPMC(C)` corridor | Deleted per post-seal 1–3; refile natively as L1/L2, with L3/L5 open and L4 owned by the exact-pair constructor |
| E16 | §6 | Ladder guards | Add: no specialization (this lane has produced misleading specialized units), no modular/truncated rung may report UNIT |
| E17 | §3.2.1 | Refute-only budget presented as needing no completeness | It needs leaf→end injectivity (L5, OPEN) and independent `td`/`b_1`, else false refutations |
| E18 | §3.2.3 | "complete decorations determine the full branch data" | Ordinary passports lose the marking on `e=1` fixed ends; post-seal 5 prunes 169→48 and kills none |

Disposition-vector consequences: the avenue-16 raise **survives** but must be
re-targeted onto T1 + discriminator 1; the avenue-3 raise **survives** with
card 2's ledger corrected to the windowed polynomial count; the avenue-25
raise **survives but weakens** under post-seal 5; the avenue-7 raise stands;
the **avenue-2 raise is void as justified** and needs re-basing.

---

## 14. Checks actually run, and the scope/firewall ledger

**Checks run (all desk-scale, exact, local; scripts in `/tmp/xr/` only).**

1. SHA-256 of both mandatory inputs before reading; Fable matches the mandated
   value; the delta hash is recorded in §0.  Four secondary pins recomputed.
2. Fable-cited custody hashes `c66b1396`, `8e25502c`, `afd9565d`, `94c10fd8`,
   `681357ce`, `9147ada2` all resolve in the ledgers.
3. Symbolic verification of `T_m(HY) - H·T_{m+4}(Y) = 0`.
4. Exact multivariate series arithmetic in `Q[F_1..F_8][u,u^{-1}]`,
   `u = H^{1/4}`: direct reversion of `t = sF^{1/8}`, expansion of `Q =
   F^{1/4}` to order `s^8`, and agreement with `(★)` for `n = 0..8`.
5. `q_0..q_3` against R7R1 `(0.4)` and the promoted `q3` closed form:
   differences identically zero.
6. `μ_4` character read directly off the `u`-exponents of `q_0..q_5`: all
   `≡ n+2 (mod 4)`.
7. `P^8 - Σ_n F_n s^n P^n = 0` to order `s^8` (the promoted R7R2 relation).
8. Polynomial cokernels of `T_m` by exact rational elimination for
   `H = X^8-1`, `(X^4-1)^2`, `(X-1)^8`, `A^2B`, at `m = 18,22,23,25,26`;
   stability checked at truncation degrees `D = 14,20,30,40,60`.  Localized
   values recomputed from `r-1+k_m` and cross-checked against the promoted
   row-25/26 codimensions `3,4` (P) and `4,4` (Q) — they match.
9. Lower face: polynomial cokernels for all 23 rows `m = 18..40` under both
   offset conventions; `k_m` schedules under both; sums `162` / `161` vs `29`.
10. Endpoint ODE `4Kg' - 3K'g = 4K` with `K = ξ(ξ-1)^7`: unsolvable at degree
    `≤ 5`, unique degree-6 solution exhibited, `g(0) = g(ρ) = 0`,
    `h(ρ) = -4/17`, uniqueness confirmed by solving in `Q[ξ]_{≤7}`.
11. Counting checks: 23 rows, 6 multiples of 4 in `[18,40]`, `8+28=36`.

**Two errors I made and fixed during this session, disclosed because they are
the same class of bug the review is about:** an off-by-one in the symbolic
`F`-variable index silently specialized `F_1 = 1` (caught by inspecting the
printed `q2`, fixed, re-run — all §4.1 results are post-fix); and a target
degree cap one too large returned `8` instead of `7` for every polynomial
cokernel (the top degree `D + deg H` is unreachable; corrected to
`D + deg H - 1`, results then stable across five truncation levels).  The
second is the identical truncation artifact recorded in my own report §10.2.

**Scope and firewall ledger.**

- `jc2-lean` was never entered, listed, searched, read, built, or modified.
  All greps in this session named explicit files or top-level `*.md` /
  `xmodel/*.md` globs.
- **No AWS action** was taken, planned, inspected, or disturbed.  No lane was
  touched.  No heavy algebra was run; every computation above is exact and
  desk-scale in pure Python (no CAS available in this environment; I wrote
  the series and linear algebra myself).
- **Exactly one file written:** `xmodel/ideation-20260827T2137Z-fable5-crossreview-opus5.md`.
  No canonical ledger, case artifact, or peer report was modified.
- **Peer content:** I read my own sealed submission (`49dd042a…`, mine) and the
  assigned target.  A hash/grep pass surfaced the *filenames*
  `ideation-20260827T2137Z-grok46.md` and `…-sol.md` and the fact that
  `grok46` also cites `c66b1396`/`8e25502c`/`afd9565d`; I read zero bytes of
  either file's content and no conclusion here derives from them.
- **Standing of my own counter-claims:** §5.5 and parts of §6 rest on my own
  blind submission of this round, which is unreviewed and carries no more
  standing than Fable's.  Where I disagree on that basis I have said so and
  named the discriminator (§11.1) rather than asserting priority.
- Nothing in this review is promoted.  T1–T3 are offered as candidates for
  the normal promotion path with hostile review, not as campaign results.

Report path: `xmodel/ideation-20260827T2137Z-fable5-crossreview-opus5.md`.
Model identity: Opus 5 (Anthropic), exact model ID `claude-opus-5`.
SHA-256: emitted to stdout immediately after writing (a file cannot contain
its own hash).
