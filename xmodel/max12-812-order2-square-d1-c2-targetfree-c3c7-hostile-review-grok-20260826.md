# Hostile review — D1 target-free primary-C2 closed cell, `3<=c<=7`

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_c2_targetfree_c3c7_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Earliest missing source family | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, compile-time print strings, and the support miner are not authority |
| Method | SHA-256 of every named pin and evidence file; compiled-script inspection; independent four-summand atom census with padded replay and contact-raising replay; hand reconstruction of the five canonical numerators modulo `L^2`, the ordinary quotients, both root Faber signs, both coefficient charts, and the `c=8` moving-connection wall. No Singular, Sage, msolve, Lean, or package compiler was executed by the reviewer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of every required primary pin matches. Every path named in `PRODUCER_FREEZE.sha256` (4 rows), source `FREEZE.sha256` (20 rows), and the 51 digest rows of `EVIDENCE.sha256` rehashes to the printed digest. All three nested `compiled.sha256` files rehash to the retrieved local compiled scripts and inventories once the AWS absolute prefixes are stripped. The `/tmp` source archive rehashes to the claimed digest. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the frozen generic-square/D1 unit-load chart `D(p*k0)`, the closed primary-C2 cell

```text
ord(C)=c,  3<=c<=7,  ord(A)>=c,  ord(R)>=c-1
```

is scheme-theoretically empty at the five first-grade ceilings `T=10+2c=16,18,20,22,24`. For each integer `c=3,...,7`, an independent cost-bounded census of all four frozen binomial summands through that ceiling, repeated with one and two extra atom counts, gives the complete polar source at the exact-contact boundary `(A,C,R)=(c,c,c-1)`:

```text
c=3:     AC (3/4), C2 (3/8), R3 (5/16), RC (5/8), all at grade 16;
c=4,5,6: AC (3/4), C2 (3/8), RC (5/8), all at grades 18,20,22;
c=7:     AC (3/4), C2 (3/8), RC (5/8), k6*C (3/4), all at grade 24.
```

In every threshold the unique pole-two family is unloaded `C2=(3/8)C^2/L^2`. Every other displayed family has pole one. `k2` is absent through all five ceilings (first polar `k2` family is `k2*R` at grade `21+c`). Every target begins at grade 28. Raising `ord(A)` or `ord(R)` can only delay a family with positive `A` or `R` exponent; it cannot add a lower-grade family, change the pole ceiling, or change target timing, and no chart inverts an `A` or `R` coefficient.

After clearing `L^2`, the Laurent/Faber tail is the remainder of the displayed rational numerator modulo `L^2`. On the finite étale root cover `p=-2λ^2` the only root terminals are `(3/8)C(+λ)^2` and `(3/8)C(-λ)^2`. The coefficient charts `D(c1)` and `D(c0)` cover exact nonzero linear `C`. Both localized ideals contain `1` before radicals. Omitting `C2` makes both root terminals zero.

The excluded `c=8` boundary is a genuine source-timing wall: `k6*C/L` first occurs at grade 25, and the grade-26 moving-connection prolongation contributes a nonzero pole-two term proportional to `-ell1*k6*C/L^2`. The pure-square functional cannot be extrapolated.

The statement does not cover `c>=8`, another primary or tied face, a positive-order leading load, `p=0`, `k0=0`, the exact-square zero section, a terminal/global chart, fan exhaustiveness, order two, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Primary pins | five claimed SHA-256 | **holds** |
| 0. Named manifests | `PRODUCER_FREEZE` 4/4, `FREEZE` 20/20, `EVIDENCE` 51/51 digest rows | **holds**; no locale-warning prefix |
| 0. Nested compiled manifests | three hosts, two rows each | **holds** against retrieved local files |
| 1. Exact `Q` vs two good primes; zero swap; validator; ordinary rings | separate hosts/rings; fail-closed; ordinary `ring`, no `qring` | **holds**; exact `Q` is the endpoint |
| 2. Polar census at five boundary contacts | independently from four binomials, padded | exactly the displayed families; unique pole-two is `C2`; padded identical |
| 3. Seven literal rows, analytic `H`, Faber bridge, `k2`/targets | first grade equals ceiling; no omitted jet | **holds**; `k2` absent; targets start at 28 |
| 4. Closed-tail widening `ord(A)>=c`, `ord(R)>=c-1` | exponent/cost, not density | **holds**; no `A`/`R` inverse; pole ceiling and target timing unaltered |
| 5. `N2` modulo `L^2`; ordinary quotient; both Faber signs; `D(c1),D(c0)`; omit-`C2` | identities; unit ideals before radicals | **holds**; ordinary quotient retained; no hidden inversion |
| 6. Required `c=8` negative control | `k6*C/L` at 25; pole-two `-ell1 k6 C/L^2` at 26 | **holds**; pure square does not extrapolate |
| 7. Firewall | `c>=8`, other faces, loads, `p=0`, `k0=0`, zero section, charts, fan, order two, max twelve, JC2 | **holds**; kept out of the verdict |

---

## 0. Custody

Recomputed SHA-256 of the required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `ed61c925e91f96af4caa62dc03c9c3c4c730a36196e0e5199db8ce877ab2dbd4` | producer report |
| `.../PRODUCER_FREEZE.sha256` | `b9ca9fa21a94b167e451490eef8a1c7fdf7c01c3e989c606cc367a8ac8197087` | producer-level freeze |
| `.../EVIDENCE.sha256` | `0e00de55745e4f004847cd50f8a951551b3b62f98d4285a1c4b0e3ee3aebf682` | evidence freeze |
| `.../FREEZE.sha256` | `331eabdc06e6e1507a1b25a5bef0920f5a4fe908491988fee82bca08065dd4c7` | source freeze |
| `/tmp/jc2_d1_c2_targetfree_c3c7_20260826_v1.tgz` | `74f830bfce1546d415244a7bb646c6a288e6c63114200aba1c9db3a0d2b19bce` | source archive on all three hosts |

`PRODUCER_FREEZE.sha256` names four files, all matching: source `FREEZE.sha256`, `RESULT.md`, `AWS_LAUNCH_METADATA.md` `40dd62a9…`, and `EVIDENCE.sha256`.

Source `FREEZE.sha256` names twenty files, all matching. Direct producer pins: preregistration `12939b0b…`, compiler `fdd28139…`, `run_aws.sh` `59c50d54…`, `launch_host.sh` `e9c928e1…`. Ancestry consumed by that chain also rehashes: r1/d1 freeze `34b0f325…` and compiler `e024a13d…`; CGE3 freeze `a5efc70c…` and compiler `352ad4f2…`; frozen tails `d72f774c…`; load-ladder compiler `77f25216…`; first-normal Padé promotion `40790378…`; halfweight results `eb2cd803…` and hostile review `49744ab9…`; `A`-prolongation validator result `74551fe8…`; low-contact v4 result `b8ae74e5…`; small-AC residue lemma `3a81fe72…`; fan lower-hull reduction `c9ecfe40…`; contact-raising closure criterion `3c0a33ce…`; maximal-pole miner specification `c4eba2d7…`; `ops/aws_exact_lane.sh` `ebe06a10…`. Canonical all-tails digest of the seven-row `tails.json` is independently `6eed03d4…`, matching the frozen CGE3 pin. The seven rows have 36/54/58/81/89/120/131 monomials.

`EVIDENCE.sha256` is 51 digest rows with no locale-warning prefix. All 51 rehash. Nested `compiled.sha256` rows, which record AWS absolute paths, match the retrieved local compiled objects:

| Lane | `source_inventory.json` | `.sing` |
|---|---|---|
| exact `Q` / Box02 | `bed03fb0…` | `cd09d238…` |
| `F_65519` / Box03 | `22c00138…` | `74211550…` |
| `F_65521` / r6d | `9fba157b…` | `a39dd17d…` |

The three compiled scripts differ by exactly the ring-characteristic token (`RC2=0` / `65519` / `65521`). Substitutions, recurrences, charts, terminals, and sentinels are otherwise byte-identical. All three inventories report the same five contact lists, `contact_count=5`, and scope `C_EQ_3_TO_7_A_GE_C_R_GE_C_MINUS_1_ON_D_P_K0_ONLY`. Host copies of the compiler rehash to the workspace pin `fdd28139…`.

All three host `archive.sha256` files record the same source-archive digest `74f830bf…`. The local tarball rehashes to that digest and contains the producer, its freeze, the r1/d1 and CGE3 ancestry, the seven-row tails, the load-ladder compiler, the miner specification, and `ops/aws_exact_lane.sh`. A passing manifest is not a mathematical verdict. The algebra below is independent of those sentinels.

---

## 1. Exact `Q`, two good-prime controls, swap, validator, ordinary rings

Exact `Q` is the theorem endpoint. `F_65519` and `F_65521` are software/support controls only. They are genuinely separate frozen runs.

| Charge | Exact `Q` (Box02) | `F_65519` (Box03) | `F_65521` (r6d) |
|---|---|---|---|
| Host | `ip-172-30-0-186` | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `…_q_box02_20260826T203500Z` | `…_p65519_box03_20260826T203500Z` | `…_p65521_r6d_20260826T203500Z` |
| Characteristic | `0` | `65519` | `65521` |
| Compiled script SHA | `cd09d238…` | `74211550…` | `a39dd17d…` |
| Engine `rc` | `0` | `0` | `0` |
| Validator | `PASS_D1_C2_TARGETFREE_C3C7_CLOSED_TAILS` | same | same |
| Stdout SHA | `0567178e…` | same | same |
| Peak RSS / swaps | 21,760 KiB / 0 | 21,908 KiB / 0 | 21,984 KiB / 0 |
| Wall | 0.21 s | 0.19 s | 0.20 s |
| Source archive in registration | `74f830bf…` | same | same |
| Launcher PID | 325142 | 269674 | 340721 |

Both control primes are prime. Neither divides `2,3,5,8`, and both are odd, so the denominators `2,4,8,16` and the numerators `3,5` remain units. The three validation files are byte-identical (`engine_rc=0` plus the same validator line), hash `eef09076…`; that common payload is not evidence that the runs were copied. Identical stdout is expected: on success the script prints only `0/1` markers and fixed diagnostic strings. All three `freeze_check.stdout` records are byte-identical (`6e369f7f…`) and report every `FREEZE` row OK. All three metas record `argv` as `timeout 1800` wrapping the lane-local compiler then `Singular -q` on the emitted script, return code 0, and stdout hashes matching `EVIDENCE.sha256`. Compiler stderr is the empty-file digest `e3b0c442…` on all three lanes. Caps were 32 GiB virtual (`33554432` KiB) and 1800 s engine. Launcher PIDs match `AWS_LAUNCH_METADATA.md`.

Each generated program begins `ring RC2=<char>,(z,t,sigma,p,a1,a0,c1,c0,b1,b0,k0,k60,k20,mu2,mu4,mu6,J,lam,ic1,ic0,ilam),dp;`. There is no `qring`, no `sat(`, no `radical`, no `primdec`, and no `LIB`. Reduction ideals are explicit `std(ideal(…))` in the ordinary polynomial ring. Raw `==0`, `subst`, and `diff` therefore run on canonically represented polynomials, not on Singular 4.3.2 quotient-ring assignments.

The fail-closed validator requires each listed marker exactly once, including `C2C3C7_C{3..7}_PRIMITIVE_COUNT` equal to `4,3,3,3,4` and `C2C3C7_ENDPOINT=PASS_EMPTY_PRIMARY_C2_C3_TO_C7_CLOSED_A_R_TAILS`, and rejects `=FAIL`, `// **`, a leading `?`, `error occurred`, and `Swaps: [1-9]`. Neither stdout nor stderr contains the rejected patterns. Zero swap is recorded on every stderr.

The printed strings `C2C3C7_MONOTONE_A_R_CLOSED_TAIL=1` and `C2C3C7_C8_MOVING_K6C_WALL_EXCLUDED=1` are compile-time constants. They are not mathematical evidence. The corresponding identities are reconstructed in §§4 and 6.

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

i.e. alphas `3/2, 5/4, 3/4, 1/4`. Pole order is `denominator - 4α`. The unit-load chart names `k10` as `k0`. At the boundary contacts `(ord(A),ord(C),ord(R))=(c,c,c-1)` the atom costs are `(c+1, 2c+2, 5+c, 5+c)`, all at least 4.

Independent expansion through grade `T=10+2c`, with atom bounds `budget // cost` and with one and two extra counts in every atom direction, produces identical retained signatures for every `c=3,...,7`. Every positive atom cost is at least 4, so a count exceeding `budget // cost` already overshoots the ceiling by itself. There is no cutoff hole.

Aggregation by `(summand, load, fixed, eR, eA, eC, pole, grade)` produces three genuine zeros, all at `c=3` grade 16, and none at `c=4,...,7` through the respective ceilings:

```text
unloaded R^2 A / L   at grade 16:  (1 r2 + 1 a) + (2 r1 + 1 a)
                                    3/4           + -3/4            = 0
unloaded R^2 C / L^2 at grade 16:  (1 r2 + 1 c) + (2 r1 + 1 c)
                                    3/4           + -3/4            = 0
unloaded R^4 / L^2   at grade 16:  (2 r2) + (2 r1 + 1 r2) + (4 r1)
                                    3/8   +     -3/4      +  3/8    = 0
```

Those monomials are absent from the source, not hidden by a leftover coefficient. The middle cancellation is the would-be second pole-two family at `c=3`; after summing it is identically zero. No cancelled key reappears after padding. For `c>=4` the same monomials sit at grade `7+3c > T` and are out of window.

The nonzero polar inventory at the five boundaries is exactly the claimed list:

| `c` | `T` | Family | Summand | Coefficient | Pole | First grade |
|---:|---:|---|---|---|---:|---:|
| 3 | 16 | `RC` | `k10` | `5/8` | 1 | 16 |
| 3 | 16 | `R3` | `k10` | `5/16` | 1 | 16 |
| 3 | 16 | `AC` | unloaded | `3/4` | 1 | 16 |
| 3 | 16 | `C2` | unloaded | `3/8` | 2 | 16 |
| 4 | 18 | `RC`,`AC`,`C2` | as above | as above | 1,1,2 | 18 |
| 5 | 20 | `RC`,`AC`,`C2` | as above | as above | 1,1,2 | 20 |
| 6 | 22 | `RC`,`AC`,`C2` | as above | as above | 1,1,2 | 22 |
| 7 | 24 | `RC` | `k10` | `5/8` | 1 | 24 |
| 7 | 24 | `k6*C` | `k6` | `3/4` | 1 | 24 |
| 7 | 24 | `AC` | unloaded | `3/4` | 1 | 24 |
| 7 | 24 | `C2` | unloaded | `3/8` | 2 | 24 |

Coefficients reconstruct from binomials. Unloaded `AC` is `binom(3/2,2)·2=3/4`. Unloaded `C2` is `binom(3/2,2)=3/8`. Loaded `RC` is `binom(5/4,2)·2·2=5/8`. Loaded `k6*C` is `binom(3/4,1)=3/4`. Loaded `R3` is itself an aggregation: three type-1 `R` contributes `binom(5/4,3)·8=-5/16` and one type-1 plus one type-2 contributes `binom(5/4,2)·2·2=5/8`, summing to `+5/16`.

The unique pole-two family in every in-window list is `C2`. There is no polar `k2` through any of the five ceilings: the cheapest polar `k2` monomial is `k2*R` at grade `21+c`, which is `24,25,26,27,28` against ceilings `16,18,20,22,24`. Bare `k2` is ordinary (pole `-1`) at weight 20 and is not a polar family. `k6*C` first enters the window at `c=7`, grade `17+7=24`; for `c<=6` it sits at `17+c > T`.

This census is taken from the frozen generating function. It does not import a support-miner emptiness claim.

---

## 3. Seven rows, analytic `H`, Faber bridge, `k2`, and targets

The compiled source rows are `tail_text` of the frozen seven-row tails, with `Lambda → σ^2` and the coefficient substitution of exact orders

```text
A  ↦  σ^c (a1 z + a0),
C  ↦  σ^c (c1 z + c0),
R  ↦  σ^{c-1} (b1 z + b0),
```

together with the target subtractions

```text
row 1,3,5: 0
row 2: σ^{28} μ2
row 4: σ^{32} μ4
row 6: σ^{36} μ6
row 7: σ^{38} (J/4)
```

which is the same `2(12+row)` timing as the frozen CGE3 emitter. The compiled `FullPhi` rows contain the five copies of each of `-sigma^28*(mu2)`, `-sigma^32*(mu4)`, `-sigma^36*(mu6)`, `-sigma^38*(J/4)` and no earlier target. Extraction divides by `σ^T`, substitutes `σ=0`, and forbids residual dependence on `k20`, `μ2`, `μ4`, `μ6`, and `J`. Exact division `σ^T·Q=SourcePhi` is checked in the ordinary ring. Because the ceiling equals the first polar grade, there is no further jet to peel: the seven leading coefficients are the entire in-window polar source.

No target can occur at grade `T<=24`: the earliest target is `μ2` at grade 28. After dividing `Φ_2` by `σ^T` the target remainder is still `σ^{28-T} μ2` with `28-T>=4`, which vanishes at `σ=0`. The compiled `FullPhi-SourcePhi` reduction modulo `σ^{T+1}` is the same statement (`28>=T+1` holds with room). The forbidden-derivative check would additionally catch any illicit in-window target monomial.

No delayed load other than unit `k0` and the declared `c=7` family `k6*C` can occur as a polar family through the ceilings. Polar `k6` other than `k6*C` starts at grade `>=24` with leftover strictly above `T` for `c<=7` (`k6*R` is ordinary; `k6*A` has pole 0; `k6*C*R` starts at `18+2c`). Polar `k2` starts at `21+c` as above. The extracted leading rows are therefore unit-load for `c=3,...,6` and unit-load plus `k6*C` at `c=7` by support, not by setting `k6=k2=0` by hand. The compiled `targetfree` sentinel correctly does not differentiate with respect to `k60`: at `c=7` that variable is a source column.

No normal jet can occur at the first grade. The compiled ring carries only the leading two coefficients of each of `A,C,R`, at exact orders `σ^c`, `σ^c`, `σ^{c-1}`. The next `σ`-jet of any of those forms raises the grade by 1 and would be a grade-`T+1` family.

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

The `σ^1` and `σ^2` columns of `T_{ij}` involve `ell1` and `ell2`. The compiled `row_checks` include those columns only when the grade offset is at least 1 or 2. Here minimum = maximum = `T`, so the offset is 0 and the connection columns are absent. The ring does not even declare `ell1`. The analytic receiver likewise uses undeformed `L=z^2+p/2`. That is the mechanical reason the first-grade source cannot see a moving connection.

The independent analytic generating function is the frozen truncated `H` with the same contacts, plus the `k6*C` column

```text
(3/4) σ^{17} t^2 k60 C inv_1
```

which is the `t`-dilated form of `(3/4) k6 C/L` (`C` already includes the factor `t C(z)`, so the extra `t^2` is the correct companion of the `t` in `AC` and `RC`). After extracting `σ^T`, leftover exponents of the truncated extras are

```text
RA2: c+1,   A3: 5+c,   R2A: c+1,   A2: 4,
R3:  c-3,   k6*C: 7-c.
```

Thus `R3` survives only at `c=3` and `k6*C` only at `c=7`; every other extra retains a positive power of `σ` and vanishes at `σ=0`. Completeness of this truncated `H` at grade `T` is the census of §2, not an extra hypothesis. Independently expanding `H`, reading `h_j=[t^{j+1}]H`, and applying the same-grade transform reproduces the seven analytic rows used below. The compiled coefficientwise identities `g=T h` are those rows against the seven literal leading coefficients.

---

## 4. Closed-tail widening

The printed monotone flag is a compile-time constant. The compiler's only runtime check is that every retained primitive has nonnegative `A` and `R` exponents, which is true by construction of atom counts and is not a widening proof. The exponent/cost argument is as follows, uniformly in both inequalities.

A polar monomial with exponents `(eR,eA,eC)` at contacts `(a,c,r)` has grade

```text
fixed + a eA + c eC + r eR.
```

Pole order `denominator-4α` is independent of contacts. Coefficients are independent of contacts: cancellations are by exponent key, so a cancelled block stays cancelled as a block. All exponents are nonnegative.

At the boundary `(a,r)=(c,c-1)` the in-window polar source is the list of §2, every family of first grade exactly `T`. Raising to `(a,r)=(c+n,c-1+s)` with `n,s>=0` shifts each grade by `n eA + s eR >= 0`. Consequently:

- no family can drop into the window from above;
- no formerly excluded family can appear at or below `T`;
- a family with `eA>0` is delayed as soon as `n>0`;
- a family with `eR>0` is delayed as soon as `s>0`;
- a family with `eA=eR=0` is invariant under both inequalities.

The invariant families are exactly `C2` (all five thresholds) and `k6*C` (only `c=7`). Independent replay of the enumerator at `(n,s)∈{(1,0),(0,1),(1,1),(2,3)}` returns precisely those predictions: the interior of the closed cell is a sub-source of the boundary source, never a larger one, and the unique pole-two family remains `C2` at the same grade. Target monomials are independent of `(A,C,R)` and sit at grades `>=28>T`, so raising `A` or `R` cannot create, cancel, or advance a target.

No chart inverts an `A` or `R` coefficient (§5). Emptiness of the root charts is therefore a statement about the `C2` square on `D(c1)∪D(c0)`, which is the same ideal on every point of the closed cell. The extra boundary columns `AC`, `RC`, and `R3` carry a factor of `L` in the cleared numerator and vanish at both roots; omitting them (as happens when `A` or `R` is raised) does not change the terminals. This is a closed `A`/`R`-order tail, not an inference from a dense exact-contact subset.

---

## 5. Pole-two numerator, ordinary quotient, recurrences, Faber signs, charts, omit-`C2`

Let `L=z^2+p/2`. Clearing the in-window polar source against `L^2` produces, at each threshold, the polynomial

```text
N2_full = (3/8) C^2
        + (3/4) A C L
        + (5/8) k0 R C L
        + 1_{c=3} (5/16) k0 R^3 L
        + 1_{c=7} (3/4) k60 C L.                                 (1)
```

The Laurent/Faber tail discards the ordinary part, so the reconstructed numerator `N2` is the unique remainder of (1) modulo `L^2`, of degree at most 3. Independent expansion of the analytic `H` of §3, extraction of `h_1,...,h_7`, and the combination

```text
N2 = h1 z^3 + h2 z^2 + (h3 + p h1) z + (h4 + p h2)
```

equals that remainder identically at every `c=3,...,7`. The identity `N2_full = N2 + L^2 Q_ord` holds with no remainder; `Q_ord` is retained and checked, not discarded. It is not the zero polynomial: the `z^4` part of `L·((3/4)AC+(5/8)k0 RC)` is `(3/4)a1 c1+(5/8)k0 b1 c1`, and at `c=3` the `z^5,z^4` parts of `k0 R^3 L` contribute as well. Reduction of (1) by `z^4 ↦ -p z^2 - p^2/4` independently reproduces the same cubic remainder.

The denominator recurrences

```text
h5 + p h3 + (p^2/4) h1 = 0,
h6 + p h4 + (p^2/4) h2 = 0,
h7 + p h5 + (p^2/4) h3 = 0
```

hold identically at every threshold; the signs are those of `L^2=z^4+p z^2+p^2/4` and of `inv_2=(1+(p/2)t^2)^{-2}`. The truncated geometric series for `inv_1,inv_2,inv_3` through `t^8` match the compiled coefficients and are exactly enough for `h_7=[t^8]H`.

After `p=-2λ^2`, the Faber combinations

```text
Ψ± = g4 ± λ (g3 + (p/4) g1)
```

are tautologically `N2(±λ)` given the same-grade transform of §3. Direct expansion: with `p=-2λ^2`,

```text
Ψ+ = h4 + (p/2) h2 + λ h3 + (λ p/2) h1
   = h4 + p h2 + λ h3 + p λ h1 + h2 λ^2 + h1 λ^3
   = N2(λ),
```

because the difference is `(h2 + λ h1)(p/2+λ^2)=0`, and likewise at `-λ` with the displayed minus signs. Independently of the transform, evaluation of the remainder at a root of `L` agrees with evaluation of (1), because `L^2 Q_ord` vanishes there to order two:

```text
N2(±λ) = (3/8) C(±λ)^2.                                          (2)
```

Every pole-one summand of (1) carries a factor of `L` and dies at the roots. That is the first pole functional, derived from the source rather than imposed. Both identities were checked by substituting into the remainder `N2`, not only into `N2_full`.

Work on the finite étale splitting cover `L=(z-λ)(z+λ)` of `D(p)`, with `λ` inverted. For linear forms the two-root evaluation map has matrix `[[λ,1],[ -λ,1]]` and determinant `-2λ`. The compiled check `std(2λ, ilam·λ-1)` being the unit ideal is the statement that `2` is a unit once `λ` is a unit, which holds in every registered characteristic. Consequently every nonzero linear `C` is nonzero at at least one root, and the two opens `D(c1)` and `D(c0)` cover every nonzero linear `C`. There is no third chart: a linear form with both coefficients zero is identically zero, which is outside the exact-order-`c` contact. The charts invert a leading coefficient of `C` and `λ`; they do not invert `A`, `R`, `L`, a connection, or a higher jet. `k0` is already a unit on `D(p*k0)` and is not needed for the root equations.

On `D(c1)` the pair (2) reads `(3/8)C(λ)^2=(3/8)C(-λ)^2=0` with `c1` a unit. Write `u=C(λ)`, `v=C(-λ)`, so `u-v=2λ c1`. After inverting `λ` and `c1`, `u-v` is a unit. In the quotient by `(u^2,v^2)` one has `(u-v)^2=-2uv`, hence `uv` is a unit, hence `u=u·(uv)·(uv)^{-1}=u^2 v·(uv)^{-1}=0`, hence `v` is a unit with `v^2=0`, hence `1=0`. The localized ideal is already `(1)` before radicals. The same holds on `D(c0)`. These are scheme-theoretic unit ideals: the compiler takes `std` of the pole equation plus the named inverse and `ilam·λ-1`, and tests `reduce(1)=0`. No radical and no saturation are used. No extra inverse is hidden in that combination.

Omitting `C2` from (1) leaves a numerator divisible by `L`, so both root terminals are identically zero. That is the compiled omitted-`C2` control. The required source column is not silently supplied by `AC`, `RC`, `R3`, or `k6*C`.

Descent is from the finite étale cover adjoining a root of `λ^2+p/2`, whose discriminant is a unit times `p` on `D(p)` in the registered characteristics. Emptiness after a faithfully flat cover is emptiness on the base.

---

## 6. Required `c=8` negative control

Replay of the same enumerator at `c=8` through the would-be ceiling `T=26` returns four polar families:

```text
k6*C  at grade 25, pole 1, coefficient 3/4;
AC, RC, C2 at grade 26.
```

So `k6*C/L` first appears at grade 25, one below the extrapolated square ceiling. At that order the moving connection is visible. Independently of Faber `T_{ij}`,

```text
L_moving = z^2 + p/2 + σ ell1 + O(σ^2),
(3/4) k6 C / L_moving
  = (3/4) k6 C / L  - σ (3/4) ell1 k6 C / L^2  + O(σ^2).
```

The second summand is a nonzero pole-two term at grade 26, proportional to `-ell1*k6*C/L^2`. Separately, the `σ^1` column of `T_{ij}` at offset 1 (grade 26 measured from first polar `k6*C` at 25) mixes the grade-25 pole-one row by `ell1`. Either contamination destroys the pure `(3/8)C^2` square used on `3<=c<=7`. The printed `C8` flag is a compile-time constant; the wall is this source-timing identity, not a missing threshold in this producer.

---

## 7. Firewall

The result eliminates only the displayed target-free primary-C2 cell on `D(p*k0)` through the five first-grade ceilings. It does not cover `c>=8`, another primary or tied face, a positive-order leading load, `p=0`, `k0=0`, the exact-square zero section, a terminal/global chart, fan exhaustiveness, order two, maximum twelve, or JC2. The support miner and any hand triage are not used as proof.

---

## Scope reminder

This confirmation is the emptiness of the unit-load D1 tail `ord(C)=c` for integers `3<=c<=7`, `ord(A)>=c`, `ord(R)>=c-1`, on `D(p*k0)` through absolute grade `T=10+2c`, and nothing else.

CONFIRMED
