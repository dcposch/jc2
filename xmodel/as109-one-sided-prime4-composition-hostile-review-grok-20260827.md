# Hostile different-model review — AS109 one-sided prime/4 composition (floor six)

| Field | Value |
|---|---|
| Claim under review | Frozen composition: Moskowicz arXiv:1810.08202v2 Theorem 2.7 plus reviewed AS109 Hensel noninjectivity imply that an exact integral polynomial lift of `(x-x^{109},y)` over `Z_{109}` has `deg_y Q = deg_y B >= 6`; the first residual actual target degree is `n=6` with `6\|deg_x(q_6)`, `deg_y P>=12`, `3\|deg_y P`, and the common-core translations `d=3 => 3\|H`, `d=6 => 6\|H`; the displayed `x`-source translation is a safe preprocessor; `n=2`--`5` Newton rectangles are history duplicates |
| Overall verdict | **CONFIRMED** |
| One-sided floor six | **CONFIRMED** |
| Residual `n=6` classification | **CONFIRMED** |
| Source-gauge statements | **CONFIRMED** |
| Stop decision for `n=2`--`5` | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking precisions: Moskowicz's published first-case citation to Theorem 2.4 is slightly too crude when the distinguished invariant is `4` and `gcd(A,C)=4`; the `4P` subcase of the aligned/constant-leading branch cites Żoładek for total-degree gcd `2w`, already repaired by the charged GGV `2p` theorem; the same composition also fully excludes every prime `n>=7`, which the producer did not need for the floor and did not list as a stop) |
| Evidence tier | independent reading of the hash-pinned 2018 e-print (Theorem 2.7 and the constant-leading branch); independent re-derivation of residue-ball Hensel over `Z_{109}`; desk exhaustion of `C0=gcd(n,deg_x q_n)` for `n=1..6` including `gcd(n,0)=n`; independent common-core translation; independent sparse Jacobian of the `(12,6)` control; unmodified rerun of the registered replay. No CAS, no AWS, no web literature sweep, no `jc2-lean` |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (Sol / OpenAI subagent lane) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` (matches the producer header) |
| Review window (UTC) | 2026-08-27T07:44:57Z |
| Python | 3.14.6; stdlib only (`math.gcd`, `math.comb`, integer dicts) |
| Host | hand algebra plus one unmodified replay and one independent sparse-arithmetic script that does not import the producer replay |

Producer, replay, and charged theorem inputs reread in full before any verdict. Primary source retrieved independently of the producer prose and hash-checked against the prior source audit.

- `xmodel/as109-one-sided-prime4-composition-sol-20260827.md` (SHA-256 `3d6d09fd1c9d1548dc6af78221f74c83276eb89378ee06cecac5fd19b46fcb36`)
- `cases/as109_one_sided_prime4_20260827/replay.py` (SHA-256 `4413482ee6d518d85abaa85c609f1f3421c168496c2d40b6b9a9340a2d4ff73d`)
- `cases/as109_one_sided_prime4_20260827/HISTORY.sha256` (SHA-256 `569ee6510a581d89be3528681abeb48e890c005b52ad6b19c803a34b964fb986`)
- `cases/as109_one_sided_prime4_20260827/INPUTS.sha256` (SHA-256 `41d155803dd1bae23f060be5719152352247afd41b4098183a7b00083681ceb6`)
- Vered Moskowicz, *A variation on Magnus' theorem and its generalizations*, arXiv:1810.08202v2 e-print. SHA-256 `ca974bd7a3603262952c9a5751bc7466c71b2ed47693489e5991096846674419`. Title, characteristic-zero field hypothesis, Notation, Theorems 1.1--1.2, Proposition 2.1, Theorems 2.4, 2.6, 2.7, and the `u=0`/`v=0` branch, all read in the primary TeX.

Conditional inputs, consumed only at the stated hypotheses:

- `xmodel/as109-partial-y-history-stop-20260824.md` / `xmodel/as109-partial-y-history-review-grok-20260824.md` — Theorem 2.7 custody, constant-leading convention, `gcd<=2` source-shear, leading UFD
- `xmodel/as109-support-gate-20260824.md` / `xmodel/as109-support-review-grok-20260824.md` Claim 6, with carry erratum — residue-ball Hensel noninjectivity over `Q_{109}`
- `xmodel/gcd3-69-coverage-composition-20260824.md` / Claude review — maximum actual `y`-degree at most eleven is an automorphism
- `xmodel/as109-max11-floor12-composition-opus5-20260826.md` / Sol review — two-sided floor twelve, used here only to name the `m>=12` arrow at `n=6`
- `xmodel/as109-one-sided-target-degree-tri-promotion-sol-20260827.md` / Grok review — AS-TRI `deg_y Q>=2`, used only as an independent `n>=2` control, not as a load-bearing step of floor six

No producer, canonical, ledger, freeze, or case file was edited. This file is the only write. `jc2-lean` was not entered, read, built, status-inspected, or modified. No AWS call was made. No Singular process was started. The 2024 Moskowicz prime field-extension-degree manuscript was not opened and is not an input.

Write `R=Z_{109}`, `K=Q_{109}`, `p=109`, and `J(P,Q)=P_x Q_y-P_y Q_x`. Actual partial `y`-degrees are used throughout.

---

## Promotion

**Accept `PASS-AS109-ONE-SIDED-TARGET-FLOOR-SIX` at the stated scope.**

Let

```text
P = x - x^{109} + 109 A,     Q = y + 109 B
```

belong to `R[x,y]` with `det J(P,Q)=1`. Then, conditionally on this being an exact integral polynomial lift of the seed `(x-x^{109},y)`,

```text
deg_y(Q) = deg_y(B) >= 6.
```

The equality is the actual-degree identity in the domain `R[x,y]` once the degree is at least two: the seed term `y` cannot contribute to `y^{>=2}`, and `109` is not a zero-divisor. The inequality is Moskowicz Theorem 2.7 plus residue-ball Hensel: every actual target degree `n<=5` forces `(P,Q)` to be a polynomial automorphism of `A^2_K`, which is injective on `K`-points, contradicting the 109-to-1 packing of source balls onto each target ball `(0,b)+109 R^2`.

**Accept the residual `n=6` classification (5.1)--(5.5) as the first honest arithmetic corner of this composition, not as emptiness of `n=6`.** A nonautomorphic exact lift with `deg_y Q=6` must satisfy `6 | deg_x(q_6)` (including the constant-leading case `deg_x(q_6)=0`), `deg_y P>=12`, `3 | deg_y P`, and the two-case common-core translation `d=3 => 3|H`, `d=6 => 6|H`.

**Accept the displayed `x`-source translation as a determinant-preserving, seed-preserving, degree-preserving preprocessor, unused in the proof of the floor.** The unique section `[x^{108} y^0]A=0` is only claimed for `deg_x A<=108`.

**Accept `STOP-AS-HISTORY-DUPLICATE` for every `n=2,3,4,5` support rectangle.** Those actual degrees are already excluded at arbitrary finite `x`-support. An empty bounded system is a strict subset of the unrestricted theorem; a survivor is not an exact lift.

**Eligible for `AUDIT.md` promotion** at exactly this conditional one-sided floor, residual classification, gauge preprocessor, and `n=2`--`5` stop. This review does not edit `AUDIT.md`.

**Do not promote this to:** existence of an AS109 lift; nonexistence of an AS109 lift; a bound on `x`-support; a routing of every `n=6` pair; a claim `deg_y Q>=7`; a theorem in a different source chart; a two-sided strengthening of `max(deg_y A, deg_y B)>=12`; a marked collision; a characteristic-`109` statement; a characteristic-zero counterexample; or a JC2 decision.

---

## Quarantine

No result here proves or disproves JC2. Producer strings `PASS-AS109-ONE-SIDED-TARGET-FLOOR-SIX` and `STOP-AS-HISTORY-DUPLICATE` were not used as evidence. Moskowicz Theorem 2.7, residue-ball Hensel, the finite `C0` table, the common-core identities, the gauge formula, and the `(12,6)` Jacobian were re-derived from the primary e-print, the charged Hensel lemma, and independent integer arithmetic. The registered replay is a custody/routing/gauge/sparse-control checker; it does not re-prove the cited automorphy theorems and was not treated as doing so.

The 2024 manuscript arXiv:2407.13795 remains `REFUTED-AS-PROOF` and is a different paper. It was not consumed.

---

## Scope (not enlarged)

One prime `p=109`, coefficient ring `R=Z_{109}` with fraction field `K=Q_{109}` (characteristic zero), polynomial maps, exact `det J=1`, displayed AS109 coordinates. Arbitrary finite `x`-degree is in scope. Partial `y`-degree is not invariant under arbitrary source automorphisms; the conclusion is for this chart. Existence, nonexistence, support rectangles, other seeds, and JC2 are out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Hash-pinned 2018 e-print is Moskowicz, *A variation on Magnus' theorem and its generalizations*, arXiv:1810.08202v2, SHA-256 `ca974bd7…4419`. Throughout, `k` is an arbitrary characteristic-zero field, so `K=Q_{109}` is directly in scope. This is not the quarantined 2024 prime field-extension-degree paper | **CONFIRMED** | a hash mismatch against the prior source audit; the 2024 manuscript substituted for 2018; a hidden algebraically-closed or `C`-only hypothesis in Theorem 2.7 |
| 2 | Theorem 2.7 (`\ref{my thm}`): if one of `{A,C}` belongs to `{1,4} union primes`, a characteristic-zero Keller pair is a polynomial automorphism. No `uv != 0` or unaligned-leading hypothesis in the statement; those belong to Theorems 2.4 and 2.6. Constant-leading uses `gcd(N,0)=N` and is handled in the second case of the proof. The `gf(x)`/`gf(y)` slip in the final aligned `u=0` display is typographical | **CONFIRMED** | Theorem 2.7 secretly requiring `uv!=0`; `gcd(n,0)` left undefined or set to `0`; the statement using `{1,8} union primes union 2P` instead of `{1,4} union primes` |
| 3 | An exact integral polynomial lift of `(x-x^{109},y)` with `det J=1` is 109-to-1 from the source balls `(a,b)+109 R^2` onto each target ball `(0,b)+109 R^2`, hence noninjective over `K`, hence not a polynomial automorphism of `A^2_K`. The carry erratum does not touch this lemma | **CONFIRMED** | `J(\overline F) != I` as polynomials over `F_{109}`; Hensel uniqueness failing for a unit Jacobian over a complete DVR; the lemma asserting existence of a lift |
| 4 | For `n=deg_y Q` in `{1,2,3,4,5}`, every possible `C0=gcd(n,deg_x q_n)`, including `deg_x q_n=0`, lies in `{1,4} union primes`. Theorem 2.7 plus Hensel exclude those actual degrees at arbitrary finite `x`-support. Seed forces `n>=1`; AS-TRI independently forces `n>=2` and is not load-bearing for the floor | **CONFIRMED** | a divisor of `4` outside `{1,2,4}`; `gcd(5,0)` escaping; `109` annihilating a leading coefficient so that actual `K`-degree drops |
| 5 | First residual actual degree is `n=6`. Possible `C0` are `1,2,3,6`; Theorem 2.7 covers the first three; a nonautomorphic exact lift must have `6 \| deg_x(q_6)`, including constant leading. Max-eleven plus Hensel gives `m=deg_y P>=12`. History-stop source-shear covers `gcd(m,6)<=2`, so a survivor has `3\|m`. Leading UFD translates `C0=6` into `d=3 => 3\|H` and `d=6 => 6\|H`, including `H=0` | **CONFIRMED** | `C0=6` already in `{1,4} union primes`; max-eleven failing to apply at `max(m,6)<=11`; `gcd(m,6)<=2` not implying automorphy after the charged GGV repair; `gcd(6,2H)=6` not equivalent to `3\|H` |
| 6 | Source translation `(x,y)->(x+tau,y)` acts on the lift set by the displayed integral formulae, is additive, free on `R[x,y]`, determinant- and seed-preserving, and preserves both actual `y`-degrees and `deg_x` of each nonzero top `y`-coefficient, hence preserves (5.1). Unique section `phi(A^tau)=phi(A)-tau` for `deg_x A<=108`. Unused in the proof of (1.2) | **CONFIRMED** | binomial `C(109,i)` not `109`-divisible; Fermat quotient leaving `R`; translation changing a top `x`-degree; a claimed section at unbounded `deg_x A` |
| 7 | The elementary automorphism `u=x+y`, `v=y+u^6`, `(P,Q)=(u+v^2,v)` has Jacobian `1`, actual `y`-degrees `(12,6)`, and constant top coefficients. It occupies the numerical residual type and is not an AS109 lift. No claim `deg_y Q>=7` is available from this composition | **CONFIRMED** | Jacobian not `1`; actual degrees not `(12,6)`; the producer treating this map as an AS109 lift or as emptiness of `n=6` |
| 8 | Frozen hashes match. Registered replay reruns unmodified and exits 0 with the displayed payload. Replay checks custody, snippet presence, finite routing, gauge sample, and the `(12,6)` control; it does not re-prove Moskowicz or Hensel. Independent arithmetic recovers the routing table, common-core translation, binomial/Fermat integrality, and the `(12,6)` Jacobian. No AWS, no producer/canonical edit | **CONFIRMED** | a hash mismatch against the launch prompt or `FREEZE.sha256`; replay failing closed; independent exhaustion finding an escaped `C0` for some `n<=5` |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt and `FREEZE.sha256`:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-one-sided-prime4-composition-sol-20260827.md` | `3d6d09fd1c9d1548dc6af78221f74c83276eb89378ee06cecac5fd19b46fcb36` | prompt and `FREEZE.sha256` |
| `cases/as109_one_sided_prime4_20260827/replay.py` | `4413482ee6d518d85abaa85c609f1f3421c168496c2d40b6b9a9340a2d4ff73d` | prompt and `FREEZE.sha256` |
| `cases/as109_one_sided_prime4_20260827/HISTORY.sha256` | `569ee6510a581d89be3528681abeb48e890c005b52ad6b19c803a34b964fb986` | prompt and `FREEZE.sha256` |
| `cases/as109_one_sided_prime4_20260827/INPUTS.sha256` | `41d155803dd1bae23f060be5719152352247afd41b4098183a7b00083681ceb6` | prompt and `FREEZE.sha256` |

`HISTORY.sha256` has 40 nonempty lines; `INPUTS.sha256` has 15. Independently recomputed SHA-256 of every load-bearing theorem/review listed in Section 4--5 of the producer matches the corresponding `INPUTS.sha256` line.

Registered command, rerun unmodified:

```text
python3 cases/as109_one_sided_prime4_20260827/replay.py
```

Exit code 0. Terminal payload (abridged to the producer-advertised fields):

```text
verdict = PASS-AS109-ONE-SIDED-TARGET-FLOOR-SIX
history_reports_pinned = 40
excluded_actual_target_y_degrees = [1,2,3,4,5]
first_not_excluded = 6
newton_n2_job = STOP-AS-HISTORY-DUPLICATE
next_arithmetic_corner = n=6 on the residual invariant stratum
lift_found = false
lift_excluded_in_all_degrees = false
jc2_inference = false
```

What the replay actually checks, versus what the report proves:

- Fail-closed SHA-256 of the 40 history reports and 15 theorem inputs, plus required substrings in four charged reviews (Theorem 2.7 invariant, `gcd(N,0)=N`, e-print hash, char-zero field sentence, Hensel “noninjective over `Q_109`” / “109-to-1 onto balls over `(0,b)`”, and the maximum-eleven headline). Substring presence is custody, not a proof of those theorems.
- Sample gauge: one sparse `A` of `x`-degree 108, one `B`, translations `tau=2`, `upsilon=3`. Checks the degree-108 section formula, preservation of actual `y`-degrees and top `x`-degrees, additivity, and integrality of the Fermat quotient and binomial coefficients at those two integers.
- Exhaustive integer routing: every `gcd(n,q)` for `n=2,3,4,5` and `q=0..12n`; every `gcd(6,q)` for `q=0..144` against `6\|q`; every `gcd(m,6)>2` against `3\|m` for `m=1..240`; common-core `gcd(6,(6/d)H)==6` against the claimed divisibility of `H`, including `H=0`.
- Sparse exact Jacobian of the elementary `(12,6)` automorphism.

The replay does not re-prove Moskowicz, Hensel, max-eleven, or the leading UFD. Those were rechecked below from the primary e-print and the charged reviews. That division of labour is exactly what the replay docstring states.

An independent engine, not imported from `replay.py`, recovered: `gcd(n,0)=n` for `n=1..6`; the complete `C0` sets `{1}`, `{1,2}`, `{1,3}`, `{1,2,4}`, `{1,5}`, `{1,2,3,6}` with uncovered residue only `{6}` at `n=6`; zero failures of the `n=6` residual, `3\|m`, and common-core translations on the same ranges; `C(109,i)` divisible by `109` for every `i=1..108`; `tau-tau^{109}` divisible by `109` on `tau=-20..20`; `C(109,108)/109=1`; and Jacobian `{(0,0):1}` with actual degrees `(12,6)` and constant leadings `{0:1}` for the elementary control.

---

## Independent recheck of the load-bearing interfaces

### 1. Moskowicz 2018 Theorem 2.7 — CONFIRMED

The e-print `https://export.arxiv.org/e-print/1810.08202v2` decompresses to a single TeX file whose gzip wrapper hashes to `ca974bd7a3603262952c9a5751bc7466c71b2ed47693489e5991096846674419`, matching the prior source audit and the producer custody line. Title, author, and abstract match *A variation on Magnus' theorem and its generalizations*. Opening sentence of the body: “Throughout this note, `k` is a field of characteristic zero”. No algebraically-closed restriction is present in Theorem 2.7. `K=Q_{109}` is a characteristic-zero field, so the statement applies verbatim. Descent from `C` is needed only for the older total-degree inputs (Magnus, Nagata, GGV) that Theorem 1.1--1.2 consume; that descent is already in the charged history-stop and is the same faithful-flatness/unique-inverse argument used for max-eleven.

Shared `theorem` counter inside Section 2 “Our results”:

| Number | Label | Statement |
|---|---|---|
| Proposition 2.1 | `prop` | `n=0` or `r=0` implies a triangular automorphism |
| Theorem 2.2 | (Dirichlet) | arithmetic progressions |
| Lemma 2.3 | `number theory lemma` | max of two coprime progressions can be made prime |
| Theorem 2.4 | `my thm improved` | `uv != 0` and unaligned; `gcd(A,C) in {1,8} union P union 2P` |
| Remark 2.5 | `trick` | Noether normalisation |
| Theorem 2.6 | `my thm i yes ii no` | `uv != 0` and aligned; one of `{A,C}` in `{1,4} union P`, or `gcd(A,C) in {1,2}` |
| Theorem 2.7 | `my thm` | **if one of `{A,C}` belongs to `{1,4} union P`, then `f` is an automorphism** |

The producer’s claim that Theorem 2.7 has no auxiliary `uv != 0` or unaligned-leading hypothesis is exactly the difference between 2.7 and 2.4/2.6. Notation: `C = gcd(r, deg_x(c_r))` with `r = deg_y(q)`, which is the producer’s `C0`.

Constant-leading branch, quoted from the second case of the proof of Theorem 2.7: if `u=0`, then `A = gcd(n,u) = gcd(n,0) = n`. The same identity is used for `v=0`. Examples in Section 3 compute `gcd(30,0)=30` and `gcd(2,0)=2` in so many words. Python `math.gcd` agrees: `gcd(n,0)=n` for `n>0`. The convention is the paper’s, not an interpolation.

Typographical slip, aligned `u=0` subcase: after displaying `deg((gf)(y))=Lr=LC`, the next sentence writes `deg((gf)(x))=LC` when applying Theorem 1.2 to the `C`-side. The preceding displayed formula and the invoked degree `LC` identify the `y`-coordinate. The theorem statement is unaffected.

Non-blocking source precision, not a refutation. (i) The first case of the published proof of 2.7 says “apply Theorem 2.4” whenever `uv != 0` and the pair is unaligned. Theorem 2.4 as written requires `gcd(A,C) in {1,8} union P union 2P`, which does not contain `4`. If the distinguished invariant is `C=4` and `gcd(A,C)=4`, that citation is formally too crude. In that unaligned situation the sheared total-degree gcd equals `gcd(A,C)=4`, which is covered by Theorem 1.1’s bullet “`<=8` or belongs to `P`” (Appelgate--Onishi / Nagata), so the implication stands. (ii) In the aligned or constant-leading `C=4` cell, the proof produces a sheared total degree in `4P` and cites Theorem 1.2, whose `2w` subcase cites Żoładek for total-degree gcd `2p`. The campaign already replaced that citation by the peer-reviewed GGV `2p` theorem in the charged history-stop. For the AS109 routing one only needs the `Q`-side invariant `C0`; Dirichlet on that side, or `L` prime in the constant-leading case, reduces to Theorem 1.2 with the GGV repair. None of this touches `n in {1,2,3,5}`, whose possible `C0` values are `1` or prime and use only Magnus / Nagata prime-gcd or `P^2`.

The 2024 paper is a different title and a different arXiv identifier. It is not this e-print.

### 2. Hensel noninjectivity — CONFIRMED

Let `F=(P,Q) in R[x,y]^2` reduce to `\overline F = (x-x^{109}, y)` and satisfy `det J_F = 1` as a polynomial identity. Over `F_{109}`,

```text
d(x^{109}) = 109 x^{108} = 0,     J(\overline F) = I
```

as a matrix of polynomials, and `a^{109}=a` for every residue `a`, so `\overline F(a,b)=(0,b)`.

`R` is a complete DVR. At every integral point the Jacobian determinant is a unit. Multivariate Hensel therefore realises, for each residue `c in F_{109}^2` and each target `t` in the ball `\overline F(c)+109 R^2`, a unique source point of `F^{-1}(t)` in the ball `c+109 R^2`. Thus `F` maps each source residue ball bijectively onto its target residue ball.

Fix `b in F_{109}`. The 109 source balls `(a,b)+109 R^2`, `a in F_{109}`, all map onto the same target ball `(0,b)+109 R^2`. Every integral target in that ball has 109 distinct preimages in `R^2 subset K^2`. So `F` is not injective as a map of `K`-points, and is not a polynomial automorphism of `A^2_K`.

A polynomial automorphism has a polynomial inverse, hence is bijective on `K`-points. That is the whole contradiction used in the floor. The complex embedding recorded in support-review Claim 6 is not consumed here.

The carry erratum overrides only the truncated two-layer digit expansion (original review Claim 2). Claims 3--8 of that review, including Hensel Claim 6, are explicitly unchanged. Packed exact `det J=1` over `R` is independent of base-109 digit bookkeeping.

The producer’s phrase “109 source residue balls above `(a,b)`” is compressed notation for the family of balls parametrised by `a`, at fixed `b`. The target is the single ball above `(0,b)`. The mathematics is the 109-to-1 packing just derived.

### 3. Exhaustion `n=1..5` and first residual `n=6` — CONFIRMED

Let `n=deg_y Q` be actual, with nonzero leading coefficient `q_n in R[x]`, and set `C0=gcd(n, deg_x q_n)`. The seed forces `n>=1`: the coefficient of `y` in `Q` is `1+109 beta_1`, a unit in `R[x]`. Independently, reviewed AS-TRI excludes `n=1` by a polynomial-degree contradiction that does not use Hensel. Floor six does not need AS-TRI: `C0=gcd(1,deg_x q_1)=1` is already Theorem 2.7.

Positive divisors, including the constant-leading value `n=gcd(n,0)`:

| `n` | possible `C0` | in `{1,4} union primes`? |
|---:|---|---|
| `1` | `1` | yes |
| `2` | `1,2` | yes (`2` prime) |
| `3` | `1,3` | yes |
| `4` | `1,2,4` | yes (`2` prime, `4` the extra residue) |
| `5` | `1,5` | yes |
| `6` | `1,2,3,6` | `1,2,3` yes; `6` no |

Checked for every `deg_x q_n` from `0` through `12n`, and for `n=6` through `144`. No escaped cell. Therefore Theorem 2.7 makes every exact Keller pair with `1<=n<=5` an automorphism over `K`, Hensel makes every exact AS109 lift noninjective over `K`, and those actual degrees are empty for exact lifts, at arbitrary finite `x`-degree.

For `n=6`, Theorem 2.7 excludes precisely the cells `C0 in {1,2,3}`. The complement is `C0=6`, i.e. `6 | deg_x(q_6)`. This includes `deg_x(q_6)=0`, because `gcd(6,0)=6`. That is (5.1). It is a necessary condition on a nonautomorphic exact lift, not emptiness of `n=6`.

Non-blocking strengthening, not a gap in the floor. The same argument fully excludes every actual target degree whose positive divisors all lie in `{1,4} union primes`, i.e. every `n in {1,4} union primes`. In particular every prime `n>=7` is excluded by Theorem 2.7 plus Hensel. The producer’s list `[1,2,3,4,5]` is the complete list of fully excluded degrees below the first residual, which is `6`. The floor `>=6` remains the correct one-sided lower bound, because `n=6` is not fully excluded. An `n=7` Newton rectangle would also be a history duplicate; the producer did not advertise one.

### 4. Charged theorems for the `n=6` consequences — CONFIRMED

Write `m=deg_y P`, `d=gcd(m,6)`, `H=deg_x h` for the primitive common leading core.

- **`6 | deg_x(q_6)`.** Moskowicz Theorem 2.7, as just exhausted. Includes `H=0`.
- **`m >= 12`.** Reviewed maximum-eleven theorem (gcd3-69 coverage composition, Claude-confirmed): every characteristic-zero Keller pair with `max(deg_y P, deg_y Q) <= 11` is an automorphism. If `n=6` and `m<=11`, the max is at most eleven, so the pair is an automorphism, contradicting Hensel. The two-sided floor-twelve composition is the same arrow specialised to both corrections at most eleven; at one-sided `n=6` one only needs max-eleven plus Hensel. Seed terms have `y`-degrees `0` and `1`, so they cannot raise the max.
- **`3 | m`.** Reviewed partial-`y` history-stop source-shear: `d=gcd(m,n)<=2` implies automorphy by a large triangular source shear plus the repaired prime-gcd theorem and GGV `2p`, including constant cores. For `n=6` the possible `d` are `1,2,3,6`. The first two are closed. The complement is `d in {3,6}`, equivalently `3|m`. Independently, `gcd(m,6)>2` iff `3|m` holds for every positive integer `m` (checked `m=1..240`, and it is immediate from the divisor lattice of `6`).
- **Common core (5.3)--(5.4).** History-stop (1.1)--(1.2): the top Jacobian identity `n a_m' b_n - m a_m b_n' = 0` and unique factorisation give `p_m = alpha h^{m/d}`, `q_6 = beta h^{6/d}`. Then `deg_x(q_6) = (6/d) H` and

```text
C0 = gcd(6, (6/d) H) = (6/d) gcd(d, H).
```

`C0=6` iff `d | H`. For the residual values of `d`:

```text
d=3  =>  3 | H,     because gcd(6, 2H)=6 iff 3|H,
d=6  =>  6 | H,     because gcd(6, H)=6 iff 6|H.
```

Both include `H=0`. Independently checked on `m=1..240` and `H=0..120` with zero failures. History-stop also closes `d=3` when `3` does not divide `H` (sheared total gcd prime), which is the same cell as `d=3 => 3|H`. For `d=6`, history-stop only forces `gcd(H,6) not in {1,2}`; `6|H` is strictly stronger and comes from Theorem 2.7 plus the UFD, not from the `gcd<=2` shear.

The elementary control `u=x+y`, `v=y+u^6`, `(P,Q)=(u+v^2,v)` is a composition of triangular automorphisms. Independent sparse expansion: Jacobian `{(0,0):1}`, actual `y`-degrees `(12,6)`, both top `x`-degrees `0`. Here `d=6` and `H=0`, so `6|H` holds. The numerical residual type is occupied by a determinant-one automorphism that is not congruent to the AS109 seed. This composition therefore cannot push the floor from six to seven.

Target shears that would lower a divisible pair `(m,6)` with `6|m` destroy the AS109 seed in general and are correctly not used.

### 5. Source gauge — CONFIRMED

Precomposition by `(x,y) |-> (x+tau, y)` with `tau in R` sends

```text
P(x+tau, y) = (x+tau) - (x+tau)^{109} + 109 A(x+tau, y)
```

to the AS109 form `x - x^{109} + 109 A^tau` if and only if

```text
A^tau = A(x+tau, y) + (tau - tau^{109})/109
        - sum_{i=1}^{108} [C(109,i)/109] tau^{109-i} x^i,
```

which is the producer’s (6.1). The binomial theorem gives the identity over `K`; integrality over `R` is `p | C(p,i)` for `1<=i<=p-1` together with `tau^{109} \equiv tau \pmod{109}`. Both were checked at desk scale. `B^tau = B(x+tau,y)` because `Q` has no `x-x^{109}` correction.

Additivity is composition of translations. Freeness on `R[x,y]`: if `A^tau=A` and `B^tau=B` for `tau != 0`, the difference `A(x+tau,y)-A(x,y)` equals a `y`-independent polynomial of `x`-degree `108` whose leading coefficient is `tau`. A polynomial difference of `x`-degree `108` forces `x`-degree `109` on `A`, and the leading coefficient would have to be `1/109`, which is not in `R`. So only `tau=0` fixes an integral polynomial lift.

Leading `x`-coefficients are invariant under `x |-> x+tau`, so actual `y`-degrees and `deg_x` of each nonzero top `y`-coefficient are invariant. In particular (5.1) is invariant. The action preserves `det J=1` and the seed residue.

If `deg_x A <= 108`, the unique `x^{108}` contribution from the correction is `-C(109,108)/109 tau = -tau`, and translation does not change the degree-`108` coefficient of `A`, so `phi(A^tau)=phi(A)-tau`. The unique section is `tau=phi(A)`, i.e. `[x^{108} y^0]A=0`. For `deg_x A>108` higher `x`-terms feed the same coefficient and no automatic section is claimed. The proof of (1.2) does not use the gauge.

The replay’s sample (`A` of `x`-degree 108, `tau=2,3`) confirms the section formula, additivity, and degree invariance on that slice. It is not a symbolic identity proof; the identity is the binomial expansion above.

### 6. Overreads — none of the forbidden promotions is made

- **Equality `deg_y Q = deg_y B`.** Once `n>=2`, the seed `y` has degree one and `109 != 0` in `R`, so the actual degrees agree. Statement (1.2) is a lower bound `>=6`, so the equality clause is in force. At `n=1` the equality can fail (`deg_y B=0`); the producer restricts it to degree at least two.
- **Coordinate / gauge dependence.** Partial `y`-degree is not invariant under a general source automorphism. The triangular shear `(x, y+x^L)` used inside Moskowicz changes the AS109 seed and is used only as an internal automorphy criterion over `K`, after which Hensel is applied to the original lift. The displayed `x`-translation preserves the seed and the degrees, and is not a proof input. The theorem is for the displayed chart, as the producer states.
- **Arbitrary support.** No `x`-rectangle is used. Theorem 2.7 and Hensel are unbounded in `x`. A bounded Newton calculation at `n<=5` cannot create an exact lift and cannot refute the unrestricted exclusion.
- **Existence versus conditional obstruction.** The implication is one-way: if an exact integral polynomial lift exists, then `deg_y Q>=6` and the `n=6` residual constraints hold. Replay flags `lift_found=false`, `lift_excluded_in_all_degrees=false`. No existence or total nonexistence is claimed.
- **JC2 / counterexample.** Replay `jc2_inference=false`. Hensel plus an automorphism of type `(12,6)` over `K` is the opposite of a counterexample: the control is an automorphism, and the AS109 lift, if it existed, would be a nonautomorphism of a different map. The two-sided floor `max(deg_y A, deg_y B)>=12` is not improved. Rank impact is correctly one-sided: every branch `deg_y B<=5` dies even if `deg_y A` is unbounded, and a residual `n=6` lift must have `deg_y A = deg_y P >= 12`.

---

## Separate required verdicts

| Decision | Verdict | Strongest sound statement |
|---|---|---|
| One-sided floor six theorem (1.2) | **CONFIRMED** | Exact integral polynomial AS109 lift `=> deg_y Q = deg_y B >= 6`, in the displayed coordinates, at arbitrary finite `x`-degree |
| Residual `n=6` classification (5.1)--(5.5) | **CONFIRMED** | A nonautomorphic exact lift with `n=6` must have `6\|deg_x(q_6)`, `m>=12`, `3\|m`, and `d=3 => 3\|H`, `d=6 => 6\|H`. Not emptiness of `n=6`, not a floor seven |
| Source-gauge statements (6.1) | **CONFIRMED** | Integral additive free seed-preserving `x`-translation; unique section at `deg_x A<=108`; preserves the residual (5.1); unused in (1.2) |
| Stop decision for `n=2`--`5` | **CONFIRMED** | `STOP-AS-HISTORY-DUPLICATE`. Those actual degrees are already excluded at unrestricted support. Same composition also fully excludes every prime `n>=7`; that is a completeness remark, not a hole in the `n=2`--`5` stop |

No numbered claim failed. No clean correction to (1.2) is required. The only campaign-clean citation footnote is that the published `C=4` cell of Theorem 2.7 is read through Theorem 1.1’s `<=8` bullet (unaligned) or through Theorem 1.2’s `4P` with GGV in place of Żoładek (aligned / constant leading). That footnote is already how the charged history-stop reads Moskowicz, and it does not change the routing table.

---

## `AUDIT.md` eligibility

**Eligible**, at exactly the promoted scope above, as a different-model-confirmed theorem-interface composition of already-reviewed inputs (Moskowicz 2018 Theorem 2.7, residue-ball Hensel, max-eleven, history-stop source-shear and leading UFD). Same promotion class as the one-sided AS-TRI lemma and the two-sided floor-twelve composition.

Not eligible as: an existence theorem, a nonexistence theorem, a support-bounded certificate, a routing of the residual `n=6` stratum, a claim `deg_y Q>=7`, a chart-independent partial-degree bound, a two-sided improvement of floor twelve, a characteristic-zero counterexample, or a JC2 decision.

This review does not edit `AUDIT.md`.
