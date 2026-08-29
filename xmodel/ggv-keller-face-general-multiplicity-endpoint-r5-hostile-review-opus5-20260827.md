# Hostile review: R5 general-multiplicity rational modes and endpoint criterion

**Reviewer:** Opus5 (independent hostile referee).
**Date:** 2026-08-27.
**Target:** the six charged R5 artifacts listed below.

**Method.** Rehashed all charged and pinned files. Read the R5 producer document,
`RESULT.json`, `PREREGISTRATION.md`, `README.md`, and `verify_r5.py`, then discarded every
producer `PASS`, every producer narrative, R4, and both prior endpoint audits as evidence and
reproved the mathematics from the definition of `E` upward. Built an independent exact
`Q[X]` / `Q(X)` / `Q(X)[[t]]` arithmetic layer in `/tmp` (no CAS, no sympy available; pure
`fractions.Fraction`) and ran desk-scale exact checks and live mutations. Ran the producer
verifier once, read-only, with `-B`. No AWS, no heavy CAS, no browsing, no producer-artifact or
ledger edits, no `jc2-lean` access of any kind. Only this review file was written.

---

## Verdict table

| # | Charged item | Verdict |
|---|---|---|
| 1 | Custody, preregistration, additive history, dependency scope | **CONFIRMED** |
| 2 | Rational homogeneous-kernel criterion `q_n e_i in Z` ⟺ `4 \| δ(12-n)` | **CONFIRMED** |
| 3 | Exact lift `t^n R_q (F/H^2)^((12-n)/8)`; completeness of subtraction | **CONFIRMED** |
| 4 | Mode schedules through weight 22; weight-22 kernel | **CONFIRMED** |
| 5 | Endpoint `-20HH'd-8H^2d'=1` and `g=-8H^2d` ⟹ `2Hg'+H'g=2H` | **CONFIRMED** |
| 6 | `g=Bz/A`, `Bz'+(3/2)B'z=A`, every rational `z` is polynomial | **CONFIRMED** |
| 7 | Degree law; `b∈{0,2,4,6,8}`; `b=4,6,8` excluded; `b=0,2` survive | **CONFIRMED** |
| 8 | Normalized quadratic branch `4a0+D a2=0` | **CONFIRMED** (+ field caveat, + invariant) |
| 9 | Verifier: hard-coded conclusions, missing partitions, weak mutations | **GAP/REPAIR** |
| 10 | Scope firewall | **CONFIRMED** |

**Nothing in the R5 solution document is refuted.** Every mathematical claim survived
independent reproof and live falsification. The single failure is the regression harness:
`verify_r5.py` contains a dead branch, a tautological "endpoint identity" that can be deleted
without changing the result, and a degree-rule mutation that escapes. That is a harness defect,
not a theorem defect, and the repair is additive.

---

## 0. Custody

All six charged artifacts rehash byte-for-byte:

```text
fd1640420ac389b1b6c3a0ea21243f5d72488bba5d39e4cc2293ab9e7c494681  xmodel/ggv-keller-face-general-multiplicity-endpoint-r5-sol-20260827.md
3d8ba26743a5c77bf37694ec0118a221a9c5fa1faff6fffb426659010a51c419  .../FREEZE.sha256
5c26a518c36228d9827ba9126427e48c0d35f8fc08492f9dfb3c8831157a3752  .../PREREGISTRATION.md
4f27380015864a4e68f91cf99555d35bdc5929959ca9d59165325d7241c5ca61  .../RESULT.json
a5545867ac089b98b592987e0cde8b0bb0595e0c8740e2f109ac3d8dc2ae163d  .../verify_r5.py
b3d4b59723cd13efe21246fdd4b93830b47678960c00a950b43167634029aa1e  .../README.md
```

`shasum -a 256 -c FREEZE.sha256` from the case directory: **9/9 OK** (4 case files, the sol
document, R4's `FREEZE.sha256`, the R4 sol document, and both superelliptic endpoint audits).
The R4 freeze chain is itself internally consistent: `shasum -c` inside
`cases/ggv_keller_face_general_squarefree_modes_r4_20260827/` returns **4/4 OK**.

`git ls-tree -r HEAD` contains none of the R5 or pinned-dependency paths; `git status --porcelain`
reports every one of them as `??`. The case is **purely additive** — no tracked file is modified,
no canonical ledger is touched.

---

## 1. Custody, preregistration, additive history, dependency scope — CONFIRMED

**Preregistration integrity.** `PREREGISTRATION.md` states five checks and four stop rules. Each
of the five preregistered checks appears in the sol document in the preregistered form, with no
silent widening. Check 5's "only `b=0,2` survive the degree-only filter" is preregistered as a
*degree-only* filter, and the sol document keeps that qualification (`b=2` then carries the extra
condition (0.3)). The stop rule "Keep perfect-square `B=1` as endpoint-silent, not excluded" is
honoured at sol lines 172–176 and in `RESULT.json`
(`"perfect_square_endpoint": "RATIONAL_ENDPOINT_ALWAYS_SOLVABLE_NOT_A_JET"`). The stop rule "Do
not consume the provisional R4 producer as promoted evidence" is honoured — see below.

**Dependency scope is exactly as declared.** R4 is pinned and *not used*. I reproved every R5
claim without reading a single R4 statement as input. Independently, R5's general formula
specializes to R4's squarefree list: for squarefree `H` (`e_i=1`, so `R_q=(H/h_0)^q`),
`Ψ_n = t^n R_q U^{γ_n}` gives `F^{3/2}, t^4F, t^8F^{1/2}, t^{12}, t^{16}F^{-1/2}, t^{20}F^{-1}` at
`n=0,4,8,12,16,20` and no weight-22 mode — exactly R4 (0.3), up to the harmless scalars `h_0^{-q}`.
That is a *consistency cross-check computed downward from R5*, not a dependency. **A Grok
refutation of R4 would not touch any R5 verdict in this review.**

**The prior audits' REFUTED item is correctly not inherited.** Both pinned endpoint audits refute
the wording "denominator exactly `A0`". R5 line 170–171 explicitly says the derivation works
"without assuming that the reduced denominator equals `A`", and my reproof confirms that no step
uses it: `g = Bz/A` is a bijection of `K(X)` for any nonzero `A,B`, coprime or not. Likewise the
audits' constant-`B` exception (`N_B` not injective, degree law failing) is correctly carried:
sol line 180 states the degree law only "For `b>=1`", and the exclusion rule is guarded by `b>=1`.

**One inherited hypothesis, correctly labelled but worth naming.** The target
`E = t^22 + O(t^23)` — in particular that the weight-22 coefficient is a *nonzero constant* — is
an input from the upstream Keller/Jacobian normalization, not something R5 derives. R5 says
"a prospective target", which is honest. I checked the sensitivity: any nonzero constant `c`
rescales to `1` via `d ↦ d/c`, so solvability is normalization-independent *within constants*;
a nonconstant right-hand side is a genuinely different problem (for `H=X^6(X-1)(X+1)`,
`N_B(v)=A` is solvable but `N_B(v)=A·X` is not). Recommend recording this explicitly.

---

## 2. The rational homogeneous-kernel criterion — CONFIRMED

**Independent derivation.** `E` is `K`-linear in `G`. Expanding both arguments,

```text
[t^N] E = Σ_{j+k=N} [ (12-k) F_j' G_k - (8-j) F_j G_k' ].
```

The `j=0, k=N` term is `(12-N)·2HH'·G_N - 8H^2 G_N' = 2H[(12-N)H' G_N - 4H G_N']`, which is sol
line 88 verbatim, hence `r_n'/r_n = q_n H'/H` with `q_n=(12-n)/4`. Confirmed.

**Necessity.** For `r ∈ K(X)^*`, write `r = p_i^{m_i} u` with `u` a unit at `p_i`. Then
`r'/r - m_i p_i'/p_i` is regular at `p_i`, while `q_n H'/H - q_n e_i p_i'/p_i` is regular at `p_i`.
Since char `K = 0` and `deg p_i' < deg p_i` with `p_i` irreducible, `p_i' ≢ 0 mod p_i`, so
`m_i = q_n e_i` in `K` and hence in `Q`. Therefore `q_n e_i ∈ Z` is necessary. Confirmed.

**Sufficiency and uniqueness.** `R_q = ∏ p_i^{q_n e_i}` satisfies `R_q'/R_q = Σ q_n e_i p_i'/p_i =
q_n H'/H`. Any two solutions have quotient with vanishing derivative, hence lie in the constant
field of `K(X)`, which is `K` — this step is where char 0 is *necessary*, not merely convenient
(in char `p`, `(X^p)' = 0`). Confirmed.

**Equivalence to `4 | δ(12-n)`.** `4 | (12-n)e_i` for all `i` ⟺ `4 | (12-n)·gcd_i(e_i)`: (⟸) by
divisibility; (⟹) by Bezout, `(12-n)·gcd = Σ c_i (12-n) e_i`. Verified live on 4000 random signed
exponent sets and weights `n ∈ [0,40]`: **0 mismatches**, so the equivalence also survives the
negative-exponent extension (`H` rational, outside the charged `H ∈ K[X]` scope, with `δ=gcd|e_i|`).

### Attacks

**Irreducible versus geometric factors — no gap.** In char 0 every irreducible `p_i` is
separable, so `p_i^{e_i}` contributes `deg p_i` distinct `K̄`-roots each of multiplicity exactly
`e_i`, and distinct irreducibles have disjoint root sets. The multiset of root multiplicities over
`K̄` is therefore `{e_i, with multiplicity deg p_i}`, and `δ` is **field-independent**. Verified
via `gcd`-only squarefree decomposition (Yun), which is by construction invariant under field
extension, on `(X^2+1)^2`, `2(X^2+1)(X^3+X+1)^3`, `(X^2-2)^6`. Moreover `R_q = ∏ p_i^{q e_i}`
already lies in `K(X)`, so a `K̄(X)` mode forces a `K(X)` mode. **Geometric = arithmetic.**

**Constants without rational fractional roots — correctly handled, and this is a real trap.**
Sol line 106 ("No root of the leading scalar `h_0` is required") is correct and load-bearing.
`H'/H` is blind to `h_0`, so `R_q` omits it. Writing the mode as `H^{q}` instead would require
`h_0^{q}`, which fails: for `H = 2X^2`, `n=10`, `q=1/2`, one would need `√2 ∉ Q`, while
`R_q = X` works. Verified live: `E(F,Ψ_n) = 0` exactly for `H = 2X^2` (δ=2, all even `n`),
`H = 3X^4` (δ=4, all `n∈[0,22]`), `H = 5(X^2+1)^2(X^3+X+1)^2`, `H = 2(X^2+1)` — every case with
`h_0` not a square or fourth power in `Q`.

**Infinity — no extra condition, and none is missed.** Residues of `dr/r` on `P^1` sum to zero,
so `res_∞ = -deg r`; matching `res_∞(q dH/H) = -q·deg H` forces `deg r = q·deg H`, which
`R_q` satisfies automatically (`deg R_q = Σ q e_i deg p_i = q deg H`). Verified at `n=10,13,22`
including the negative-degree cases. Infinity is **automatically consistent**: it adds nothing
and blocks nothing.

**Constant field of `K(X)`.** It is `K` (`K` is relatively algebraically closed in `K(X)`); `K` is
not required to be algebraically closed anywhere in this item.

### Live falsification

For each of six `H` shapes I solved the *linear* system for `r = N/D` over wide denominator
families — `D = ∏ p_i^{c_i}` times extraneous factors `(X-5)`, `(X-5)^3`, `(X-5)^2+1` (poles away
from `H`) — with `deg N ≤ deg D + deg H + extra`:

| `H` | δ | off-schedule `n` | result |
|---|---|---|---|
| `X^2(X-1)^2` | 2 | all odd 1..21 | nothing, 100 denominators, `deg N ≤ 18` |
| `2(X^2+1)` | 1 | 17 weights | nothing, 20 denominators, `deg N ≤ 16` |
| `3X^4` | 4 | none | (schedule is all of 0..22) |
| `X^3(X-2)^6` | 3 | 17 weights | nothing, 64 denominators, `deg N ≤ 20` |
| `X(X-1)^2(X+1)^8` | 1 | 17 weights | nothing, 108 denominators, `deg N ≤ 22` |
| `5(X^2+1)^2(X^3+X+1)^2` | 2 | all odd 1..21 | nothing, 36 denominators, `deg N ≤ 25` |

and on-schedule, `R_q` solves `4Hr' - (12-n)H'r = 0` exactly in every case. A separate wide run on
`X^2(X-1)^2` with denominators up to `p_i^6` recovered the kernel at *every* on-schedule weight
including `n=22` (`R_q = 1/(X^5(X-1)^5)`) and confirmed **all** found solutions are `K`-scalar
multiples of `R_q`, i.e. the kernel is exactly one-dimensional.

---

## 3. The exact lift `t^n R_q (F/H^2)^((12-n)/8)` — CONFIRMED

**Existence in `K(X)[[t]]` without a forbidden root.** `U = F/H^2 ∈ 1 + tK(X)[[t]]` has constant
term exactly `1`, so `U^{γ}` is the binomial series `Σ_k C(γ,k)(U-1)^k`, convergent `t`-adically
and lying in `1 + tK(X)[[t]]` for *any* `γ ∈ Q`. No square root, eighth root, or root of any
scalar is ever selected: the only scalar in sight is `h_0`, and `R_q` does not contain it.
`Ψ_n ∈ t^n R_q(1+tK(X)[[t]]) ⊂ K(X)[[t]]`. Confirmed.

**Independent differentiation, route A (reproducing the producer's).**
`(Ψ_n)_X/Ψ_n = R_q'/R_q + γ_n(F_X/F - 2H'/H) = γ_n F_X/F` precisely because `R_q'/R_q = 2γ_n H'/H
= q_n H'/H`; and `(Ψ_n)_t/Ψ_n = n/t + γ_n F_t/F`. Substituting, the `F_XF_t/F` terms cancel and

```text
E(F,Ψ_n) = Ψ_n F_X (12 - 8γ_n - n) = Ψ_n F_X (12 - (12-n) - n) = 0.
```

Sol (1.3) confirmed. Note the identity `(Ψ_n)_X/Ψ_n = γ_n F_X/F` silently *encodes* the `R_q`
integrality condition; that is legitimate but compressed.

**Independent differentiation, route B (does not reuse the producer's ansatz).** Put `S=F^{3/2}`.
Then the `W`-coefficient of `E(F,SW)` is `12F_X F^{3/2} - 8F·(3/2)F^{1/2}F_X - t·0 = 0`, so

```text
E(F, F^{3/2} W) = F^{3/2} [ -(8F - tF_t) W_X - t F_X W_t ].
```

The vector field `V = -(8F-tF_t)∂_X - tF_X∂_t` is nonvanishing at `t=0` (`V|_{t=0} = -8H^2∂_X`) and
has first integral `Φ = t^8/F`; I verified `V(Φ)=0` identically. Hence
`ker E(F,·) = F^{3/2}·{series in Φ}`, and `Ψ_n ∝ F^{3/2}Φ^{n/8}` — since
`R_q H^{n/4} ∝ (H/h_0)^3` and `t^n F^{-n/8} = Φ^{n/8}`. Membership in `K(X)[[t]]` requires
`H^{-n/4} ∈ K(X)` up to a constant, which is again exactly `4 | δ(12-n)`. **The two routes agree
and the second re-derives the classification from scratch.**

**Iterative subtraction is complete and non-corrupting.** `Ψ_n = t^n R_q(1 + O(t))`, so subtracting
a multiple of `Ψ_n` changes no coefficient at weight `< n` — no earlier weight is corrupted. And
because `E(F,Ψ_n) = 0` exactly, `E(F,G)` is left **bit-identical** by every subtraction; verified
computationally (`E(F, F^{3/2}+Σc_nΨ_n+t^{22}d).c == E(F, F^{3/2}+t^{22}d).c`). Completeness: if
`Δ = G - F^{3/2}` first appears at weight `n < 22`, then `[t^n]E(F,Δ)` is purely homogeneous
(every `j≥1` cross term multiplies a vanishing `Δ_k`), so either `r_n = cR_q` and `cΨ_n` removes
it, or the integrality fails and `r_n = 0` is forced. Either way the induction reaches weight 22.

**Live.** `E(F,Ψ_n) = 0` exactly to `t`-order 30, for **every** on-schedule `n ∈ [0,22]**, across
seven `H` shapes (δ = 1,2,3,4; `h_0` = 1,2,3,5; irreducible factors of degree 1,2,3), with `F` a
*generic* polynomial series with `F_0=H^2` — not `F=H^2`. This includes all `n>12`, where `R_q`
carries negative exponents and `Ψ_n` genuinely has poles; those are legitimate for a *necessary*
criterion because `K[X] ⊂ K(X)`.

---

## 4. Mode schedules through weight 22 — CONFIRMED

`4 | δ(12-n)` on `0 ≤ n ≤ 22`:

| case | schedule | matches `RESULT.json` |
|---|---|---|
| δ odd | `0,4,8,12,16,20` | `squarefree_gcd1` ✓ |
| δ ≡ 2 mod 4 | `0,2,4,…,20,22` | `perfect_square_gcd2` ✓ |
| 4 \| δ | every `n = 0,…,22` | `fourth_power_gcd4` ✓ |

Derivations: δ odd ⟹ `4 | (12-n)` ⟺ `n ≡ 0 mod 4`; `δ=2u` with `u` odd ⟹ `2 | (12-n)` ⟺ `n` even;
`4 | δ` ⟹ vacuous. The trichotomy is exhaustive over `δ ≥ 1`. Endpoints check out: `n=12` gives
`Ψ_12 = t^{12}` with `E(F,t^{12}) = 12F_Xt^{12} - 12F_Xt^{12} = 0` for *every* `H`, and `n=0` gives
`F^{3/2}/h_0^3`.

**Weight 22 in the inhomogeneous problem.** `q_{22} = -5/2`, so a weight-22 kernel exists iff
`4 | 10δ` ⟺ **δ even** ⟺ `H` is a square times a constant. When it exists, the solution set of
(2.1) is a torsor under `K·R_{-5/2}`, so it changes the *affine space* of solutions and not their
*existence*. Sol lines 136–138 state exactly this, and it is correct. Verified: for `δ=4`
(`H=X^4(X-1)^4`) the weight-22 kernel exists and the endpoint is solvable; for `δ=1`
(`H=X^6(X-1)(X+1)`) there is no weight-22 kernel and the endpoint is still solvable.

Independent cross-check against the pinned Grok audit's §5 remark (used as a *coincidence check*,
not evidence): its `-20e - 8s_d` vanishing at `s_d = -5e/2` is the same `q_{22} = -5/2` I derived.

*Minor wording:* sol line 128 says the subtraction removes kernel coefficients "below weight 22",
while the schedules at lines 130–133 list `n=22`. Harmless — the `n=22` entry is the endpoint
kernel discussed immediately after — but the two sentences read as if in tension.

---

## 5. The endpoint — CONFIRMED, with a strengthening

**Extraction.** From `[t^N]E = Σ_{j+k=N}[(12-k)F_j'G_k - (8-j)F_jG_k']`, the `j=0, k=22` term is

```text
(12-22)·2HH'·d - 8H^2 d' = -20HH'd - 8H^2 d',
```

which is (2.1). **Stronger than the document states:** the sol says "direct coefficient
extraction", which reads as if it needs `F = H^2`. It does not. Because `E(F,Ψ_n)=0`, the reduced
residual `Δ = G - F^{3/2} - Σ c_nΨ_n` satisfies `E(F,G) = E(F,Δ)` with `Δ = t^{22}d + O(t^{23})`,
so every `j ≥ 1` term multiplies a vanishing `Δ_k` and **no `F_j` with `j≥1` can contaminate the
weight-22 coefficient**. Verified live on three `H` with *generic* polynomial `F`: `[t^k]E = 0`
for all `k<22` and `[t^{22}]E = -20HH'd - 8H^2d'` exactly.

**`g = -8H^2 d`.** Direct computation:

```text
2Hg' + H'g = -40H^2H'd - 16H^3d' = 2H·(-20HH'd - 8H^2d'),
```

so (2.1)`=1` ⟺ (0.1)`=2H`. Verified on 300 random `(H, d)` with `d` rational and `H` of degree
1..4: **0 failures**. The map `d ↦ -8H^2d` is a bijection of `K(X)` since `H ≠ 0`, so the two
equations are equivalent, not merely related. Sol line 155 is correct: **no squarefreeness and no
uniqueness at weight 22 are used** — I used neither.

**Caveat (inherited, not an error).** The right-hand side `1` is the weight-22 normalization
`[t^{22}]E = 1`. Any nonzero *constant* rescales to `1` (verified for `c = 7, -3, 2/5`). A
nonconstant right-hand side is a different problem (verified above). This should be stated as a
hypothesis rather than left implicit in "a prospective target".

---

## 6. `H=A^2B`, `g=Bz/A`, and polynomiality — CONFIRMED

**The substitution.** With `H=A^2B`, `H' = 2AA'B + A^2B'`, and `g=Bz/A`:

```text
2Hg' + H'g = 2AB[ Bz' + (3/2)B'z ],      2H = 2A^2B,
```

so dividing by `2AB ≠ 0` gives (2.2) exactly. Verified on 400 random `(A,B,z)` with `z` **rational
and carrying poles**: 0 failures. `g ↦ z = gA/B` is a bijection of `K(X)`, so (0.1) and (2.2) are
equivalent as stated.

**Every rational `z` is polynomial.** Over `K̄`, let `α` be a pole of `z` of order `m ≥ 1`.

- *Pole away from `B`* (`B(α)≠0`): `z'` has pole order exactly `m+1` (char 0 keeps `-mc ≠ 0`), so
  `Bz'` has order `m+1` while `(3/2)B'z` has order `≤ m`. Nothing cancels; the left side has a
  pole but `A` does not. Verified for `m=1,2,3,5`: the left-side denominator has degree exactly
  `m+1`.
- *Pole at a simple root of `B`*: `B` squarefree ⟹ `ord_α B = 1`, `ord_α B' = 0`. Both terms have
  pole order exactly `m` with combined leading coefficient `c·B'(α)·(3/2 - m)`, which is never
  zero for integer `m ≥ 1`. Verified for `m=1,2,3,4,7`, with exact leading coefficients
  `1, -1, -3, -5, -11` matching `B'(1)(3/2-m) = 2(3/2-m)`.

Hence `z` has no finite pole and is polynomial. Sol lines 165–169 confirmed.

**The `3/2` is load-bearing — live mutation.** Replacing `3/2` by `κ`, the leading coefficient is
`κ - m`. For every **integer** `κ ≥ 1` the lemma **breaks** at `m = κ` (a rational non-polynomial
solution appears); I confirmed breakage at `κ = 1, 2, 3` and survival at `κ = 3/2, 5/2`. The
content of the argument is that `3/2 ∉ Z`, and `3/2` arises precisely from `H = A^2B`.

### Attacks

- **Non-coprime `A,B`:** never used. Verified with `H = X^5(X-1)^3`, where `A = X^2(X-1)`,
  `B = X(X-1)` and `gcd(A,B)=B`. The reduction and the criterion both apply, and this `H` is
  correctly **excluded**.
- **Constant `B`:** `N_B = B·d/dX`, surjective on `K[X]` in char 0, so the rational endpoint always
  solves. `N_B` is *not* injective there (kernel = constants) and the degree law fails at
  `(b,r)=(0,0)`; R5 restricts the degree law to `b≥1` and guards the exclusion with `b≥1`, so the
  exception is correctly carried, not inherited as a bug.
- **Infinity:** not a pole constraint here — a polynomial `z` is allowed a pole at `∞`. Infinity
  enters only through the degree law of §3, which is where R5 puts it. Correct treatment.
- **Unit choices in the squarefree decomposition:** `(A,B) ↦ (λA, λ^{-2}B)` sends a solution `v` to
  `λ^3 v`, so (0.2) is invariant. Verified live on 500 random cases. `B` is the odd part of `H` and
  `A` the rest, each unique up to scalars, so `b = deg B` is well defined.

---

## 7. Degree law and the degree-eight conclusion — CONFIRMED

**Degree law (3.1).** For `b ≥ 1` and `v ≠ 0` of degree `r`, `deg(Bv' + (3/2)B'v) = r+b-1` with
leading coefficient `(r + (3/2)b)·lc(B)·lc(v)`, nonzero because `r + (3/2)b ≥ 3/2 > 0` in char 0.
Verified on 500 random `(B,v)` with `b∈1..5`, `r∈0..6`: **0 failures**.

**`b ∈ {0,2,4,6,8}`.** `2a+b=8` forces `b` even. Enumerating all `p(8)=22` partitions of 8 and
counting odd parts (the `K̄` picture, and `b` is field-independent) gives exactly `{0,2,4,6,8}`,
each realized: `b=0` by 5 partitions, `b=2` by 9, `b=4` by 5, `b=6` by 2, `b=8` by 1. The number
of odd parts of a partition of `n` has the parity of `n` — verified on all 22.

**Exclusions.** Solvability needs `a = r+b-1` with `r ≥ 0`, i.e. `a ≥ b-1`; with `a=(8-b)/2` this
fails exactly for `b ≥ 4`. I did **not** stop at counting: I solved `N_B(v)=A` exactly for
`deg v ≤ 12` on concrete degree-8 `H`:

| `H` | `a`,`b` | linear algebra |
|---|---|---|
| squarefree deg 8 | 0, 8 | **no solution** → excluded |
| `X^3(X-1)(X+1)(X-2)(X+2)(X-3)` | 1, 6 | **no solution** → excluded |
| `X^3(X-1)^3(X+1)(X-2)` | 2, 4 | **no solution** → excluded |
| `X^5(X-1)(X+1)(X-2)` | 2, 4 | **no solution** → excluded |
| `X^5(X-1)^3` (`A,B` not coprime) | 3, 2 | **no solution** → excluded by (0.3) |
| `X^6(X-1)(X+1)` | 3, 2 | `v = X^2/5 + 2/15` → **survivor** |
| `X^8`, `(X^2(X-1)^2)^2` | 4, 0 | solvable → **survivor** |

So `b=4,6,8` are excluded, `b=0,2` are the only degree-only survivors, and `b=2` genuinely splits
under (0.3). `RESULT.json`'s `[4,6,8]` / `[0,2]` confirmed.

---

## 8. The normalized quadratic branch — CONFIRMED, with a field caveat and an invariant

**Formula (3.2).** With `B=z^2-D`, `v=v_2z^2+v_1z+v_0`:

```text
Bv' + (3/2)B'v = 5v_2 z^3 + 4v_1 z^2 + (3v_0 - 2D v_2) z - D v_1.
```

Reproduced exactly. Matching `A = a_3z^3+a_2z^2+a_1z+a_0` gives `v_2=a_3/5`, `v_1=a_2/4`,
`v_0=(a_1+2Da_3/5)/3`, and the one leftover condition `a_0 = -Da_2/4`, i.e.

```text
4 a_0 + D a_2 = 0.
```

Since `deg A = 3` forces `deg v = 2` exactly by the degree law, restricting `v` to degree ≤ 2 is
without loss. Confirmed.

**Live validation against true solvability.** On **3507** random `(A of degree 3, B squarefree of
degree 2)` over `Q`, the criterion `4a_0 + Da_2 = 0` agreed with exact linear-algebra solvability
in **every single case (0 mismatches)**. Six competing functionals were tested on 2629 cases and
all failed:

| functional | disagreements |
|---|---|
| `4a0 + D a2` (charged) | **0** |
| `4a0 + D^2 a2` | 16 |
| `4a0 - D a2` | 21 |
| `5a0 + D a2` | 21 |
| `4a0 + D a1` | 23 |
| `3a0 + D a2` | 26 |
| `a0 + D a2` | 33 |

**Field caveat — in R5's favour.** Sol line 191 says "translate and scale **after base extension**".
Base extension is **not required**, and the criterion is better stated over `K`: completing the
square needs only char ≠ 2, and one divides the *whole equation* by `lc(B)` (using
`N_{βB_0}(v) = β N_{B_0}(v)`) rather than rescaling `B` by a unit, which would demand `√lc(B)`.
So `D ∈ K` always. Verified with `B=X^2+1` (irreducible over `Q`, `D=-1`) and `B=3X^2-2`
(irreducible, `D=2/3`), where the criterion over `Q` matches solvability over `Q` exactly.
Independently, solvability of a linear system is insensitive to base extension, so the sol
document's stronger phrasing is harmless — but it invites the false impression that `4a_0+Da_2=0`
is only a `K̄`-statement. **Recommended one-line repair:** replace "after base extension" with
"over `K` itself (char ≠ 2), dividing the equation by `lc(B)`".

**Coordinate caveat and the invariant that removes it.** `4a_0 + D a_2` is written in the
normalized coordinate. It is invariant under unit rescaling, translation, and dilation (verified
on 500 random cases), and I identify its coordinate-free meaning. Expanding
`√(z^2-D) = z - D/(2z) - D^2/(8z^3) - …`, the coefficient of `z^{-1}` in `A·√B` is

```text
res_∞( A √B  dz ) = -(D/8)·(4 a_0 + D a_2),
```

verified exactly on six random `(D,A)`. Since `D ≠ 0`, **(0.3) ⟺ `res_∞(A√B dz) = 0`** — the
statement that `A√B dz` has vanishing residue at the two points over `∞` on `y^2=B`. This is the
invariant formulation the charge asked for; recommend recording it.

---

## 9. Verifier audit — GAP/REPAIR

`verify_r5.py` prints `PASS` and writes no files under `-B`. It is nonetheless materially weaker
than the theorem it claims to regress. Findings, all reproduced on an instrumented **copy** in
`/tmp` (the charged file was never modified):

**G1 — dead branch.** At line 120, `if NBv == A_poly:` is never true:
`N_B(v) = 20X^3-4X^2-2X+1` while `A_poly = 3X^3-2X+1`. The guarded assert never executes.

**G2 — the "cross-multiplied endpoint identity" is vacuous.** After `A_pos = NBv`, the surviving
assert (lines 124–126) is `2·A_pos·B·NBv == 2·A_pos·A_pos·B` with `NBv = A_pos` — i.e.
`2·X·B·X == 2·X·X·B`, commutativity of polynomial multiplication, true for *any* `X` and `B`
(demonstrated with unrelated inputs). **`g'` is never computed anywhere in the file; `2Hg'+H'g` is
never assembled.** Deleting the entire 15-line block still yields `PASS R5 exact
general-multiplicity endpoint checks`. So (0.1), (2.1), and `g = -8H^2 d` are **completely
untested**.

**G3 — tautological assertions in place of the core claim.** Lines 84–86 assert
`Q(12-n,4) == 2*Q(12-n,8)` and `12 - 8·(12-n)/8 - n == 0`. Both are arithmetic identities with no
content about `E`. The single most important claim of R5 — that `Ψ_n` annihilates `E` **to all
orders**, not just to leading order — is never exercised: no series, no `F`, no `E` appears in the
file at all.

**G4 — an escaping mutation.** Changing the exclusion rule `a < b - 1` to `a < b` still yields
`PASS`. The two rules agree at every `b` when `deg H = 8`, so the hard-coded degree-8 census cannot
see the difference. The smallest discriminating instance is **`deg H = 4`, `b = 2`, `a = 1`**
(i.e. `a = b-1` exactly): for `H = X^2(X-1)(X+1)` the charged rule correctly reports a survivor
(`v = 1/3`, `g = (X^2-1)/(3X)`, and `2Hg'+H'g = 2H` verified), while the mutant wrongly excludes.
The next discriminator is `deg H = 10`, `b = 4`, `a = 3`. So the verifier does not pin the general
degree law, only its degree-8 shadow.

**G5 — one-sided quadratic test, circular mutation.** Lines 103–111 test only *image ⟹ condition*.
The converse (*condition ⟹ solvable*), which is what makes (0.3) a criterion rather than a
necessary condition, is untested. The mutation `mutated[0] += 1` only rechecks the same formula
rather than demonstrating that the mutated `A` is outside `im(N_B)`. Only `D = 7` is used.

**G6 — regression against producer-authored expectations.** `assert schedules ==
expected["mode_schedules"]` and the two `RESULT.json` degree assertions compare code output to a
file the same producer wrote. That is a consistency check, not evidence.

**Mutations that do bite** (so the harness is not worthless): `n_operator` `3/2 → 5/2`,
`mode_weights` `%4 → %2`, and `4a0+Da2 → 4a0-Da2` all raise `AssertionError`.

**None of G1–G6 is a mathematical error.** Every claim the harness fails to test, I tested
independently and confirmed. The repair is additive.

### Minimal additive repair (verifier only)

Add to the case directory a `verify_r5_strong.py` (do not edit the frozen `verify_r5.py`) that:

1. builds a truncated `K(X)[[t]]` and asserts `E(F, t^n R_q U^{γ_n}) == 0` to `t`-order ≥ 24 for
   every on-schedule `n ∈ [0,22]`, for at least one `H` per `δ`-class and at least one `h_0` that
   is not a square (e.g. `H = 2X^2`);
2. asserts the full reduction `[t^k]E = 0` for `k<22` and `[t^{22}]E = -20HH'd - 8H^2d'` with a
   *generic* polynomial `F`, not `F = H^2`;
3. computes `g'` and asserts `2Hg' + H'g == 2H` for `g = -8H^2 d` and for `g = Bv/A`;
4. adds `deg H = 4` with `(b,a) = (2,1)` and `deg H = 10` with `(b,a) = (4,3)` to pin `a ≥ b-1`
   against `a ≥ b`;
5. tests the converse direction of (0.3): for random `A` with `4a_0 + Da_2 = 0`, exhibit `v`; for
   random `A` with `4a_0 + Da_2 ≠ 0`, assert the linear system is inconsistent — over several `D`
   including `D` negative and non-square;
6. deletes the dead `if` and replaces the tautological block with (3).

---

## 10. Scope — CONFIRMED

Sol §4 disclaims raw `2S/3S` support, GGV landing, family exclusion, global automorphism,
`G2-PSC`, `G2-BD`, cofinality, counterexample, and JC2. `RESULT.json` carries
`"theorem_scope": "NECESSARY_RATIONAL_ENDPOINT_OBSTRUCTION_FOR_FORMAL_H2_H3_EDGE"` and
`"status": "PRODUCER_PASS_PENDING_HOSTILE_REVIEW"`. All accurate; I found no overreach anywhere in
the document, and no claim in it requires more than the stated hypotheses.

The relaxation direction is right: `K[X] ⊂ K(X)`, and the argument runs *polynomial `G` ⟹ rational
`d` exists*, so failure of (0.2) excludes. The positive direction constructs nothing, and I can
make that concrete rather than rhetorical: from `d = -g/(8H^2)` and `g = Bv/A` one gets

```text
d = -v / (8 A^5 B),      deg(A^5 B) = 5a+b  >  a-b+1 = deg v   whenever deg H ≥ 1,
```

so **`d` is never a polynomial**. Verified on both survivor branches:
`H=X^8` gives `d = -1/(40X^{15})`, and `H=X^6(X-1)(X+1)` gives
`d = (-X^2/40 - 1/60)/(X^{17}-X^{15})` — both with genuine poles, both satisfying
`-20HH'd-8H^2d' = 1` exactly. A rational endpoint survivor is endpoint silence and nothing more.

**Maximum promotion supported by this review:** R5 is a *necessary rational-endpoint filter* for
formal polynomial-`X` `F_0=H^2, G_0=H^3` edges, conditional on the inherited weight-22
normalization `[t^{22}]E = 1`. Nothing more.

---

## 11. Smallest failing objects

No mathematical failure was found, so these are the sharpest *sensitivity* points rather than
defects — the places where a small perturbation would break the theorem, and the one place the
harness actually fails:

| object | smallest failing instance |
|---|---|
| Coefficient `3/2` in `Bz'+(3/2)B'z` | any **integer** `κ ≥ 1` breaks polynomiality at pole order `m=κ`; smallest is `κ=1, m=1` |
| Constants `(12,8)` in `E` | `(12,4)`, `(12,9)`, `(10,8)`, `(8,12)` all destroy the entire mode family at `n=0` already |
| Cokernel functional | `a_0 + D a_2` first disagrees with solvability at 33/2629 random `(A,B)`; every tested variant fails |
| Weight-22 kernel | exists iff `δ` even; smallest witness `H = X^2` (`δ=2`) — and it does **not** affect endpoint existence |
| **Verifier degree rule** | **`deg H = 4`, `b=2`, `a=1`, `H = X^2(X-1)(X+1)`** — the mutant `a<b` wrongly excludes a true survivor and the harness cannot see it |
| Characteristic | 2, 3, 5 must be invertible (`γ_n`, `3/2`, `a_3/5`, `a_2/4`, `(a_1+2Dv_2)/3`); char 0 is *necessary* for "mode unique up to scalar", since `(X^p)'=0` in char `p` |
| RHS normalization | constants are harmless; a nonconstant RHS changes the answer (`N_B(v)=A` solvable, `N_B(v)=A·X` not, for `H=X^6(X-1)(X+1)`) |

---

## 12. Recommended additive repairs

None is required for correctness of the theorem; (R1) is required before the harness should be
treated as protecting the result.

- **R1 (verifier, required).** Add `verify_r5_strong.py` per §9. Do not edit the frozen file.
- **R2 (presentation).** Sol line 191: drop "after base extension"; state that `D ∈ K` and that
  dividing by `lc(B)` avoids `√lc(B)`.
- **R3 (presentation).** State `[t^{22}]E = 1` as an inherited hypothesis of the reduction, and
  record that any nonzero constant is equivalent while a nonconstant RHS is not.
- **R4 (optional, strengthening).** Record the invariant reading `res_∞(A√B dz) = 0` for (0.3), and
  record that `d = -v/(8A^5B)` is never polynomial — this makes the "not a jet" firewall an
  identity rather than a caution.
- **R5 (optional, wording).** Reconcile sol line 128 ("below weight 22") with the schedules at
  lines 130–133 that list `n=22`.

---

## 13. Reproduction

Independent checks were staged in `/tmp` (exact `Fraction` arithmetic; no CAS, no network, no
repo writes). Producer verifier run once, read-only:

```text
cd cases/ggv_keller_face_general_multiplicity_endpoint_r5_20260827
PYTHONDONTWRITEBYTECODE=1 python3 -B verify_r5.py     # PASS, no files written
shasum -a 256 -c FREEZE.sha256                        # 9/9 OK
cd ../ggv_keller_face_general_squarefree_modes_r4_20260827
shasum -a 256 -c FREEZE.sha256                        # 4/4 OK
```

Independent checks performed: exact mode lift to `t`-order 30 across 7 `H` shapes; bounded
off-schedule falsification over up to 108 denominator families; full weight-22 reduction with
generic `F`; 300 + 400 random substitution identities; pole-order and leading-coefficient lemma at
`m = 1,2,3,4,5,7`; degree law on 500 random `(B,v)`; explicit `N_B(v)=A` linear algebra on 8
degree-8 `H`; 3507-case criterion-vs-solvability comparison and a 7-way functional discrimination;
residue-at-infinity identity; invariance under unit/translation/dilation; and 4 live mutations of
the producer verifier plus one block deletion.

**Bottom line: the R5 mathematics is confirmed in full. The regression harness is not, and should
be strengthened before it is relied on. R5's promotion ceiling is the necessary rational-endpoint
filter it claims — no more, and R4's separate fate does not disturb it.**
