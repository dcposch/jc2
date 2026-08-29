# Hostile review — tied square/D1 `(a,c,r)=(3,3,2)` C2 maximal-pole producer

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_tied_a3c3r2_c2_maxpole2_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Earliest missing source family | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers and compile-time print strings are not authority |
| Method | SHA-256 of every named pin and evidence file; compiled-script inspection; independent four-summand atom census with padded replay through grade 24; independent `[σ^{16}]` extraction of all seven frozen tail rows at `(A,C,R)=(3,3,2)`; hand reconstruction of `N2_full`, the remainder modulo `L^2`, the ordinary quotient, both root Faber functionals, both localized unit ideals, and the omit-`C2` control. No Singular, Sage, msolve, Lean, or package compiler was executed by the reviewer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of every required primary pin matches. Every path named in `PRODUCER_FREEZE.sha256` (4 rows), source `FREEZE.sha256` (20 rows), and `EVIDENCE.sha256` (51 rows) rehashes to the printed digest. All three nested `compiled.sha256` files rehash to the retrieved local compiled scripts and inventories once the AWS absolute prefixes are stripped. The `/tmp` source archive rehashes to the claimed digest on all three hosts. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the frozen generic square/D1 unit-load chart `D(p*k0)`, the exact contact cell

```text
ord(A)=3,  ord(C)=3,  ord(R)=2
```

is scheme-theoretically empty at absolute grade 16. The complete polar source through that grade is exactly four primitives, all first occurring in grade 16, with unique pole-two family `C2`. After clearing `L^2`, the Laurent/Faber tail is the remainder of the displayed rational numerator modulo `L^2`, not the full cleared polynomial. On the finite étale splitting cover `p=-2λ^2`, both root functionals collapse to `(3/8)C(±λ)^2`. The two coefficient charts `D(c1)` and `D(c0)` exhaust nonzero linear `C`, and both localized ideals contain `1` before radicals. Omitting `C2` makes both root terminals identically zero. Faithfully flat descent from the splitting cover of `L` on `D(p)` gives emptiness on the base chart.

The statement does not cover another face, a generic all-`C2` theorem, a positive-order leading load, `p=0`, `k0=0`, the exact-square zero section, a terminal/global chart, fan exhaustiveness, order two, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Primary pins | five claimed SHA-256 | **holds** |
| 0. Named manifests | `PRODUCER_FREEZE` 4/4, `FREEZE` 20/20, `EVIDENCE` 51/51 | **holds** |
| 0. Nested compiled manifests | three hosts, two rows each | **holds** against retrieved local files |
| 1. Exact `Q` vs two good primes; zero swap; validator; ordinary `ring` | separate hosts/rings; fail-closed; no `qring` | **holds**; exact `Q` is the endpoint |
| 2. Polar census through grade 16 | independently from four binomials | exactly `AC, C2, R3, RC`; all start at 16; unique pole-two is `C2`; padded identical through `pad=2` |
| 3. Seven literal rows, extraction, analytic `H`, Faber bridge | first grade equals ceiling | **holds**; no normal/connection jet, no lower polar load, no target, no omitted in-window column |
| 4. `N2_full` vs remainder vs ordinary quotient | identities; pole-two recurrence; both Faber signs | **holds**; ordinary quotient is retained and nonzero |
| 5. Two exact-`C` charts on `p=-2λ^2` | `2λ`; `D(c1)∪D(c0)`; unit ideals before radicals | **holds**; no omitted chart, no radical, no extra inverse, no `A`/`R` inverse |
| 6. Omit-`C2` control; firewall | both roots vanish without `C2` | **holds**; adjacent faces and generic maximal-pole claims stay out |

---

## 0. Custody

Recomputed SHA-256 of the required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `b0ae59bfe59705c95114eebebcf639a0a27832710ddbe89a1bf1646e69e40c9b` | producer report |
| `.../PRODUCER_FREEZE.sha256` | `41fdc7c3e3abd7b16159467484f2f4610337709d13dc7a0dbdbe4277a3407cc5` | producer-level freeze |
| `.../EVIDENCE.sha256` | `2bff9bc7358a5fd05a9a6dfa3efd11629ba24381359eb4c94dec134ae419299e` | evidence freeze |
| `.../FREEZE.sha256` | `30673eead795eb94dfc1f1b46fe39327bfe58ed3d5acac773d717ec5421488e8` | source freeze |
| `/tmp/jc2_d1_tied_a3c3r2_c2_maxpole2_20260826_v1.tgz` | `a5380e75cdc897e61d1ce88f508d7f343a90ca43b4e917b9304c2744a9b325c1` | source archive on all three hosts |

`PRODUCER_FREEZE.sha256` names four files, all matching: source `FREEZE.sha256`, `RESULT.md`, `AWS_LAUNCH_METADATA.md` `aa7c0454…`, and `EVIDENCE.sha256`.

Source `FREEZE.sha256` names twenty files, all matching. Ancestry consumed by that chain also rehashes: r1/d1 `compile_r1_d1_ac.py` `e024a13d…` and freeze `34b0f325…`; CGE3 `compile_cge3_universal.py` `352ad4f2…` and freeze `a5efc70c…`; frozen tails `d72f774c…`; canonical all-tails `6eed03d4…`; miner specification `c4eba2d7…`; `ops/aws_exact_lane.sh` `ebe06a10…`. The seven rows have 36/54/58/81/89/120/131 monomials.

`EVIDENCE.sha256` names 51 digest rows; all 51 rehash. Nested `compiled.sha256` rows, which record AWS absolute paths, match the retrieved local compiled objects:

| Lane | `source_inventory.json` | `.sing` |
|---|---|---|
| exact `Q` / Box02 | `b7b7d085…` | `88ff1e99…` |
| `F_65519` / Box03 | `d30cdcf6…` | `baf3dab4…` |
| `F_65521` / r6d | `9163d3f3…` | `e7330707…` |

The three compiled scripts differ by exactly the ring-characteristic token (`R433=0` / `65519` / `65521`). Substitutions, recurrences, charts, and sentinels are otherwise byte-identical. All three inventories report `primitive_count=4`, `target_jet_count=0`, and unique maximal pole `3/8*C^2/L^2`. All three host `archive.sha256` files record the same source-archive digest `a5380e75…`. Nested copies of `FREEZE.sha256` and the compiler on all three extracted trees rehash to the local pins.

A passing manifest is not a mathematical verdict. The algebra below is independent of those sentinels.

---

## 1. Exact `Q`, two good-prime controls, swap, validator, ordinary rings

Exact `Q` is the theorem endpoint. `F_65519` and `F_65521` are software/support controls only. They are genuinely separate frozen runs.

| Charge | Exact `Q` (Box02) | `F_65519` (Box03) | `F_65521` (r6d) |
|---|---|---|---|
| Host | `ip-172-30-0-186` | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `…_q_box02_20260826T201345Z` | `…_p65519_box03_20260826T201345Z` | `…_p65521_r6d_20260826T201345Z` |
| Characteristic | `0` | `65519` | `65521` |
| Compiled script SHA | `88ff1e99…` | `baf3dab4…` | `e7330707…` |
| Engine `rc` | `0` | `0` | `0` |
| Validator | `PASS_D1_TIED_A3C3R2_C2_MAXPOLE2_EMPTY` | same | same |
| Stdout SHA | `79163938…` | same structural payload | same |
| Peak RSS / swaps | 19,712 KiB / 0 | 20,064 KiB / 0 | 20,076 KiB / 0 |
| Source archive in registration | `a5380e75…` | same | same |
| Launcher PID | 321837 | 268065 | 338016 |

Both control primes are prime. Neither divides `2,3,5,8,16`, and both are odd, so the denominators `2,4,8,16` and the numerator `5` remain units. The three validation files are byte-identical (`engine_rc=0` plus the same validator line), hash `aa1b78d3…`; that common payload is not evidence that the runs were copied. Identical stdout is expected: on success the script prints only `0/1` markers and fixed diagnostic strings. All three `freeze_check.stdout` records are byte-identical to the corresponding `prelaunch_freeze.stdout` and report every `FREEZE` row OK. All three metas record `argv` as `timeout 1800` wrapping the lane-local compiler then `Singular -q` on the emitted script, return code 0, and stdout hashes matching `EVIDENCE.sha256`. Compiler stderr is the empty-file digest `e3b0c442…` on all three lanes. Caps were 16 GiB virtual (`16777216` KiB) and 1800 s engine.

Each generated program begins `ring R433=<char>,(z,t,sigma,p,a1,a0,c1,c0,b1,b0,…),dp;`. There is no `qring`, no `sat(`, no `radical`, and no `primdec`. Reduction ideals are explicit `std(ideal(…))` in the ordinary polynomial ring. The ring does not declare `ell1`. The unused inverse `ik0` occurs only in the variable list. Singular 4.3.2 quotient-ring assignments are therefore not in play: every `==0`, `subst`, and `diff` in the generated program is on an ordinary polynomial ring.

The fail-closed validator requires each listed marker exactly once, including `F433_COMMON_N2=1` and `F433_ENDPOINT=PASS_EMPTY_A3_C3_R2_ON_D_P_K0`, and rejects `=FAIL`, `// **`, a leading `?`, `error occurred`, and `Swaps: [1-9]`. Neither stdout nor stderr contains the rejected patterns. Zero swap is recorded on every stderr.

The printed strings `F433_PRIMITIVE_COUNT=4`, `F433_UNIQUE_MAX_POLE=C2_POLE2`, and `F433_PADDED_CUTOFF_IDENTICAL=1` are compile-time constants. The corresponding identities live in the census and in `F433_endpoint`. Those strings are not mathematical evidence; the identities are reconstructed below.

---

## 2. Independent polar census

The frozen square source is `f=K^2+σ^5 D` with `K=L^2+σ^2 R` and `D=LA+C`. Factoring `f=L^4(1+x)` gives the four atoms

```text
x = 2 σ^2 R/L^2 + σ^4 R^2/L^4 + σ^5 A/L^3 + σ^5 C/L^4
```

of `σ`-costs `(2,4,5,5)` and denominators `(2,4,3,4)`, with scalars `(2,1,1,1)`. The four binomial summands are

```text
f^{3/2},   σ^4 k10 f^{5/4},   σ^{12} k6 f^{3/4},   σ^{20} k2 f^{1/4},
```

i.e. alphas `3/2, 5/4, 3/4, 1/4`. Pole order is `denominator - 4α`. Contact costs on this cell are `ord(A)=3`, `ord(C)=3`, `ord(R)=2`, so atom costs become `(4,8,8,8)`. Every atom cost is even, every summand weight is even, and every in-window grade is even: there is no grade-17 hole. The unit-load chart names `k10` as `k0`.

Independent expansion through grade 16, with atom bounds `budget // cost` and with one and two extra counts in every atom direction, produces identical retained signatures. Every positive atom cost is at least 4 on this baseline, so a degree-`(bound+2)` tuple already exceeds the ceiling. There is no cutoff hole.

Aggregation by `(summand, load, fixed, eR, eA, eC, pole)` produces three genuine zeros, all at grade 16:

```text
unloaded R^4 / L^2 :  (4 r1) + (2 r1 + 1 r2) + (2 r2)
                       3/8   +      -3/4      +  3/8  = 0
unloaded R^2 A / L :  (1 r2 + 1 a) + (2 r1 + 1 a)
                       3/4          + -3/4           = 0
unloaded R^2 C / L^2: (1 r2 + 1 c) + (2 r1 + 1 c)
                       3/4          + -3/4           = 0
```

Those monomials are absent from the source, not hidden by a leftover coefficient. The cancelled pole-two key `R^2 C` is the hostile candidate for a second maximal pole; it does not survive. No cancelled key reappears after padding.

The nonzero polar inventory is exactly four families, all of first grade 16:

| Family | Summand | Coefficient | Pole | First grade |
|---|---|---|---|---|
| `AC` | unloaded | `3/4` | 1 | 16 |
| `C2` | unloaded | `3/8` | 2 | 16 |
| `R3` | `k10` | `5/16` | 1 | 16 |
| `RC` | `k10` | `5/8` | 1 | 16 |

The `AC` coefficient is `binom(3/2,2)·2=3/4`. The `C2` coefficient is `binom(3/2,2)=3/8`. The `RC` coefficient is `binom(5/4,2)·2·2=5/8`. The `R3` coefficient is itself an aggregation: three type-1 `R` contributes `-5/16` and one type-1 plus one type-2 contributes `+5/8`, summing to `+5/16`. The unique pole-two family is `C2`. There is no fifth polar primitive and no polar k6 or k2 through grade 16. The only in-window k6 monomial is ordinary `k6 R` at grade 16 (pole `-1`). k2 starts at weight 20. Ordinary (pole `≤ 0`) monomials at grade 16 include unloaded `A^2` and `k10 RA`; they are holomorphic and do not enter the polar tail.

Raising the ceiling to 24, the next polar families all start at grade 20 (`RA2`, `k10 A^2`, `k10 C^2`, `k6 C`, `k6 R^2`, …). Completeness of the grade-16 polar source is this census, not an extra hypothesis, and not the support miner.

---

## 3. Seven rows, extraction, bridge, and first-grade ceilings

The compiled source rows are `tail_text` of the frozen seven-row tails, with `Lambda → σ^2` and the target subtractions

```text
row 1,3,5: 0
row 2: σ^{28} μ2
row 4: σ^{32} μ4
row 6: σ^{36} μ6
row 7: σ^{38} (J/4)
```

which is the same `2(12+row)` timing as the frozen CGE3 emitter. The coefficient substitution is the r1/d1 emitter with direct polynomial `C` and `R` (factors `2` and `4` inserted in `source_coefficients`), at exact orders `σ^3, σ^3, σ^2`. Extraction divides by `σ^{16}`, substitutes `σ=0`, and forbids residual dependence on `k6`, `k2load`, `μ2`, `μ4`, `μ6`, and `J`. Recursive quotients check exact division at each `σ`-step. Because the ceiling equals the first polar grade, there is no further jet to peel: the seven leading coefficients are the entire in-window source.

Independent `[σ^{16}]` extraction of all seven frozen rows at this contact, truncating every coefficient polynomial at `σ^{16}`, yields: every row is divisible by `σ^{16}` (row 6 is identically `0`, hence divisible); no extracted coefficient depends on `k6` or `k2load`; and the seven leading polynomials are

```text
g1 = (3/4)(a0 c1 + a1 c0) + (5/8) k0 (c0 b1 + c1 b0)
     + (15/16) k0 b1 b0^2 - (5/32) p k0 b1^3
g2 = (3/4) a0 c0 + (3/8) c1^2 + (5/8) k0 c0 b0 + (5/16) k0 b0^3
     - (15/32) p k0 b1^2 b0 - (5/16) p k0 c1 b1 - (3/8) p a1 c1
g3 = (3/4) c1 c0 - (3/16) p (a0 c1 + a1 c0)
     - (5/32) p k0 (c0 b1 + c1 b0) - (15/64) p k0 b1 b0^2 + (5/128) p^2 k0 b1^3
g4 = (3/8) c0^2 - (3/16) p c1^2
g5 = - (3/16) p c1 c0 - (3/128) p^2 (a0 c1 + a1 c0)
     - (5/256) p^2 k0 (c0 b1 + c1 b0) - (15/512) p^2 k0 b1 b0^2 + (5/1024) p^3 k0 b1^3
g6 = 0
g7 = - (3/128) p^2 c1 c0 - (3/512) p^3 (a0 c1 + a1 c0)
     - (5/1024) p^3 k0 (c0 b1 + c1 b0) - (15/2048) p^3 k0 b1 b0^2 + (5/4096) p^4 k0 b1^3.
```

Row 6 vanishing is the even pole-two recurrence written in Faber coordinates, not an omitted source column.

No target can occur at grade 16: the earliest target is `μ2` at grade 28. After dividing `Φ_2` by `σ^{16}` the target remainder is still `σ^{12} μ2`, which vanishes at `σ=0`. The forbidden-derivative check would additionally catch any illicit in-window target monomial.

No delayed load other than unit `k0` can occur as a polar family: k6 polar requires remaining budget 4 and denominator at least 4, which cannot buy a polar atom; the only in-window k6 monomial is ordinary `k6 R`. k2 starts at weight 20. The extracted grade-16 rows are therefore unit-load by support, not by setting `k6=k2=0` by hand.

No normal jet can occur at the first grade. The compiled ring carries only the leading two coefficients of each of `A,C,R`, at exact orders `σ^3`, `σ^3`, `σ^2`. The next `σ`-jet of any of those forms raises the grade by 1 and would be a grade-17 family, which is empty by the even-cost parity of §2.

No connection jet can occur at the first grade. The Faber bridge is the frozen lower-unitriangular transform `T_{ij}(p)` at the same grade. Independently, `T_{ij}` is zero unless `i-j` is a nonnegative even integer `2n`, with leading coefficient

```text
(∏_{k=0}^{n-1} (j/2 + k)) / (n!  2^n)  p^n.
```

This reproduces the compiled same-grade identities

```text
g1 = h1
g2 = h2
g3 = (p/4) h1 + h3
g4 = (p/2) h2 + h4
g5 = (3/32) p^2 h1 + (3/4) p h3 + h5
g6 = (1/4) p^2 h2 + p h4 + h6
g7 = (5/128) p^3 h1 + (15/32) p^2 h3 + (5/4) p h5 + h7.
```

The `σ^1` and `σ^2` columns of `T_{ij}` involve `ell1` and `ell2`. The compiled `row_checks` include those columns only when the grade offset is at least 1 or 2. Here minimum = maximum = 16, so the offset is 0 and the connection columns are absent. The ring does not even declare `ell1`. The analytic receiver likewise uses undeformed `L=z^2+p/2`. That is the mechanical reason the first-grade source cannot see a moving connection.

The analytic generating function at this contact, after extracting `σ^{16}`, retains only the four polar families of §2:

```text
H = (3/4) t A C inv1  + (3/8) t^3 C^2 inv2
  + (5/16) k0 R^3 inv1 + (5/8) t k0 R C inv1,
```

with `A=a1+a0 t`, `C=c1+c0 t`, `R=b1+b0 t`, and `inv_q = (1+(p/2)t^2)^{-q}` through `t^8`. The later primitives `RA2`, `A^3`, `k0 R^2 A`, `k0 A^2` start at grades 20, 24, 20, 20 and are absent after the substitution. Independently, `h_j=[t^{j+1}]H` pushed through `T_{ij}` reproduces the seven extracted `g_i` coefficientwise, including `g6=0`. Completeness of this truncated `H` at grade 16 is the census of §2. The CGE3 analytic omitted `C^2` because that family is out of the CGE3 window (grades 13–15); at this contact it is the unique pole-two family and is present both in the r1/d1 `universal_hshift` and in the frozen tails.

---

## 4. Pole-two numerator, ordinary quotient, recurrences, Faber signs

Let `L=z^2+p/2`. The four polar families clear against `L^2` to

```text
N2_full = (3/4) A C L + (3/8) C^2
        + (5/16) k0 R^3 L + (5/8) k0 R C L.             (1)
```

This is a polynomial of degree 5. The Laurent/Faber tail discards the ordinary part, so the reconstructed numerator `N2` is the unique remainder of (1) modulo `L^2`, of degree at most 3. Polynomial division gives the exact ordinary quotient

```text
Q_ord = (3/4) a1 c1 + (5/8) k0 b1 c1
      + (5/16) k0 (b1^3 z + 3 b1^2 b0),                 (*)
```

and the identity `N2_full = N2 + L^2 Q_ord` holds with no remainder. In particular `Q_ord` is not zero, so `N2 ≠ N2_full` as polynomials. The compiled test is the congruence `N2 ≡ N2_full (mod L^2)` together with the reconstruction identity against `(*)`; it is not the false Laurent-versus-ordinary equality `N2 = N2_full`.

The analytic reconstruction with `h_j = [t^{j+1}] H` and

```text
N2 = h1 z^3 + h2 z^2 + (h3 + p h1) z + (h4 + p h2)
```

equals that remainder identically. The denominator recurrences

```text
h5 + p h3 + (p^2/4) h1 = 0,
h6 + p h4 + (p^2/4) h2 = 0,
h7 + p h5 + (p^2/4) h3 = 0
```

hold identically; the signs are those of `L^2 = z^4 + p z^2 + p^2/4` and of `inv_2 = (1+(p/2)t^2)^{-2}`. The identity `g6=0` is the middle recurrence written in Faber coordinates.

After `p = -2λ^2`, the Faber combinations

```text
Ψ± = g4 ± λ (g3 + (p/4) g1)
```

are tautologically `N2(±λ)` given the same-grade transform of §3. Independently of the transform, evaluation of the remainder at a root of `L` agrees with evaluation of (1), because `L^2 Q_ord` vanishes there:

```text
N2(±λ) = (3/8) C(±λ)^2.                                 (2)
```

Every sign is `+`. The simple-pole families `AC`, `R3`, and `RC` each still contain a factor of `L` after clearing `L^2`, so they vanish at both roots. That is the first pole functional, derived from the source rather than imposed.

---

## 5. Two exact-`C` charts, determinant, no radical, no hidden inverse

Work on the finite étale splitting cover `L=(z-λ)(z+λ)` of `D(p)`, with `λ` inverted. For linear forms the two-root evaluation map `(c1,c0) ↦ (C(λ),C(-λ))` has matrix `[[λ,1],[ -λ,1]]` and determinant `2λ`. The compiled check `std(2λ, ilam·λ-1)` being the unit ideal is the statement that `2` is a unit once `λ` is a unit, which holds in every registered characteristic. Consequently every nonzero linear `C` is nonzero at at least one root, and the two opens

```text
D(c1),  D(c0)
```

cover every nonzero linear `C`. There is no third chart: a linear form with both coefficients zero is identically zero, which is outside the contact. No leading coefficient of `A` or of `R` is inverted. `k0` is not inverted; emptiness without inverting `k0` is stronger than the claimed chart `D(p*k0)`.

On `D(c1)` the identity (2) reads `(3/8) C(λ)^2 = (3/8) C(-λ)^2 = 0`. Write `x=λ c1+c0` and `y=-λ c1+c0`. The compiled ideal is

```text
I_{c1} = ( x^2, y^2, ic1·c1-1, ilam·λ-1 )
```

in the ordinary polynomial ring, with no radical and no saturation. Then `x^2-y^2 = 4 λ c1 c0 ∈ I_{c1}`, so

```text
(x^2-y^2) ic1 ilam = 4 c0 (1+U)(1+V),   U=ic1 c1-1,  V=ilam λ-1.
```

Hence `4 c0 ∈ I_{c1}`. In every registered characteristic `4` is a unit, so `c0 ∈ I_{c1}`. Then `x^2 ∈ I_{c1}` forces `(λ c1)^2 ∈ I_{c1}`, and

```text
(λ c1)^2 ilam^2 ic1^2 = (1+V)^2 (1+U)^2 ≡ 1  (mod I_{c1}).
```

Thus `1 ∈ I_{c1}` before taking radicals. The same argument on `D(c0)`, using `x^2-y^2 = 4 λ c1 c0` to place `λ c1` in the ideal and then `y^2` to place `c0^2` in the ideal, yields `1 ∈ I_{c0}`. Because `reduce(1)=0` on `std` of those ideals, there are no residual nilpotent or embedded points on these charts. The cover of nonzero linear `C` is scheme-theoretically empty.

The only inverted quantities are `λ` and a named nonzero coefficient of `C`. There is no inverse of `L`, no inverse of a connection, no inverse of a higher jet, and no inverse of a leading `A` or `R` coefficient. The compiled `ik0` is unused.

---

## 6. Omit-`C2` control, descent, firewall

Omitting `C2` from (1) leaves

```text
N2_full - (3/8) C^2 = L · ( (3/4) A C + (5/16) k0 R^3 + (5/8) k0 R C ),
```

which vanishes at both roots of `L`. That is the compiled omitted-`C2` control, and it is the same identity obtained by deleting the only surviving summand of (2). The decisive column is therefore source-required rather than supplied by `AC`, `R3`, or `RC`.

Descent is from the finite étale cover `Z[λ,λ^{-1}] → Z[p,p^{-1}]` adjoining a root of `λ^2+p/2`, whose discriminant is a unit times `p` on `D(p)` in the registered characteristics. Emptiness after a faithfully flat cover is emptiness on the base. The inverted elements on every chart of the cover are among `{λ, c1, c0}`, all already units on `D(p)` with nonzero linear `C`.

Firewall, as claimed: the result eliminates only this equality vector on `D(p*k0)` at grade 16. It does not treat another lower-hull face, a generic all-`C2` theorem, a positive-order or ramified load, `p=0`, `k0=0`, the exact-square zero section, a terminal or global chart, fan exhaustiveness, order two, `(8,12)`, maximum twelve, or JC2. The support miner and any hand triage are not imported as proof.

---

## Scope reminder

This confirmation is the emptiness of the unit-load D1 cell `ord(A)=3`, `ord(C)=3`, `ord(R)=2` on `D(p*k0)` through absolute grade 16, and nothing else.

CONFIRMED
