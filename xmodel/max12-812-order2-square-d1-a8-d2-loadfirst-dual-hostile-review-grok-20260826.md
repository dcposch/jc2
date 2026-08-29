# Hostile review — D1 `a=8,d=2` load-first split

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_a8_d2_loadfirst_dual_functional_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Earliest missing source monomial | none through grade 30. First later polar: `k10 AC` at grade 32, pole 2, coefficient `5/16` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, validator strings, and finite-field agreement are not authority |
| Method | SHA-256 of every named pin, nested compiled manifest, and evidence file; independent four-summand binomial expansion through grade 30 with pad `0,1,2` and a grade-40 omitted-term census; hand derivation of the grade-27 `D(k60)` obstruction, the grade-28 tied numerator, `Delta_C` rank, pole-two reconstruction, moving-root functionals, pairings, and unit ideals. No Singular, Sage, msolve, Lean, or other heavy CAS |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the six required primary pins match. Every path named in `FREEZE.sha256` (4 rows), `EVIDENCE.sha256` (36 rows), and `PRODUCER_FREEZE.sha256` (4 rows) rehashes to the printed digest. All three nested `compiled.sha256` files rehash to the retrieved `.sing` scripts and `source_inventory.json`. Compiler ancestry pins (low-`a` local-row compiler and producer freeze, r1/d1 compiler and freeze, support miner, `tails.json`, load-ladder compiler, cge3 compiler) rehash on disk. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

After the registered square/D1 gates, over characteristic zero on `D(p*k0)`, the seven literal Faber equations have no point in the strict contact tail

```text
ord(A)=8, ord(C)=10, ord(R)>=8.
```

The independently expanded source through `T=30` has six polar primitives, global pole ceiling two, unique grade-27 polar column `(3/4)k6 C/L`, and sole pole-two column `(3/8)C^2/L^2` at grade 30. The scheme-theoretic split `D(k60) union V(k60)` is exhaustive.

On `D(k60)` the grade-27 analytic rows are exactly `(3/4)k60 c1` and `(3/4)k60 c0`. After inverting `k60` they generate the unit ideal on either exact-contact chart `D(c1)` or `D(c0)`. No target is present at grade 27: the row-2 target begins at `sigma^{28}`.

On `V(k60)` the first surviving pole-one column is `(3/4)C(A+k60_1)/L` at grade 28. Its two proper-numerator equations have determinant `Delta_C=c0^2+(p/2)c1^2`. Off `Delta_C` they force `a1=0` and `a0+k60_1=0`. The rank-one face is not divided out. Both moving-root functionals

```text
Psi_pm = Phi4 +/- lambda*(Phi3+(p/4)Phi1) = N(+/- lambda),
lambda(sigma)^2 = -P(sigma)/2,
```

vanish identically in grades `28,...,29` and equal

```text
q_+ = (3/8)(c1*lambda+c0)^2,   q_- = (3/8)(-c1*lambda+c0)^2
```

at grade 30. The ideals `(q_+,q_-)` are the unit ideal on both exact-contact charts `D(lambda*c1*k0)` and `D(lambda*c0*k0)`, before taking radicals, including the rank-one chamber. Rows 1, 3, and 4 are target-free through grade 30, so those three full rows cannot vanish. Finite etale descent from the root cover empties the unsplit chart `D(p)`. Leading `R` is uninverted, so this is the closed `ord(R)>=8` tail.

The named cell is the entire claim. There is no `a=8,d=3`, `a=9`, equality/target-shadow face, other D1 chart, square-component, maximum-twelve, or JC2 statement.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Six primary pins | hashes | all six match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 4/4, `EVIDENCE` 36/36, `PRODUCER_FREEZE` 4/4, three nested `compiled.sha256` 2/2 each; imported compiler ancestry rehashes |
| 1. Exact Q vs screens, AWS, ancestry | rc, diagnostics, archive, swap, caps | **holds**; exact Q is the endpoint; `F_65521` and `F_65519` are independent host screens |
| 2. Primitive inventory | independent expansion through `T=30`, pad+1/+2, pole ceiling, sole `C^2`, grade-27 `k6 C` | **holds**; count six; earliest missing monomial none; first later polar is `k10 AC` at grade 32 |
| 3. Seven literal rows | delayed loads, moving `p`, jets, row-2 target through 30, rows 1/3/4 target-free, compact/literal bridge, sigma quotients | **holds** |
| 4. Exhaustive split and `D(k60)` | `D(k60) union V(k60)`, grade-27 unit obstruction, no target | **holds** |
| 5. `V(k60)` first wall | tied column, two numerators, `Delta_C`, rank-two on `D(Delta_C)`, rank-one face retained | **holds** |
| 6. Functionals, pairings, descent | `Psi_pm=N(+/-lambda)`, pole-one vanish through 29, `q_pm` exact, unit ideals before radicals, finite etale on `D(p)` | **holds** |
| 7. Closed `R` and firewall | no leading `R` inverted; only `a=8,d=2,ord(R)>=8` after `D(p*k0)` | **holds** |

No mathematical defect, custody/software defect that breaks a numbered claim, or scope wording defect that enlarges the theorem was found.

---

## 0. Custody

Recomputed SHA-256 of the six required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `919f6e1a296e084ffdf4d569fcf8c184bcf5b2cf263f47b2882bd03f50539021` | producer report |
| `.../AWS_LAUNCH_METADATA.md` | `168cf84173b28c0ba72485b2362ab07a714575f001d7261335c1705c8ceb5e37` | AWS metadata |
| `.../EVIDENCE.sha256` | `d7a2ca512067b48d690fa1510036833ac4368ebc2a9539a0654b690392404cdc` | evidence freeze |
| `.../FREEZE.sha256` | `db71eda0a205b7138d497e5b64c7f86a6cfd691714a64eec027d3cb5be1e2514` | source freeze |
| `.../PRODUCER_FREEZE.sha256` | `9a85f15ea741255ecda04fc787467393d1661a08cd8ed501549d4cacf32d91fd` | producer freeze |
| `.../compile_a8_d2.py` | `7df2b5629b3153bd490e7c38a8d8de38fbde0daace35ba99ce5847e8a47d7095` | compiler |

`FREEZE.sha256` names the four local producer files (`PREREGISTRATION.md`, `compile_a8_d2.py`, `run_aws.sh`, `launch_host.sh`), all matching. `PRODUCER_FREEZE.sha256` repeats the four producer documents and matches. `EVIDENCE.sha256` names the three AWS boxes only (exact Q on Box03, `F_65521` on r6d, `F_65519` on Box02); 36/36 rehash. Nested `compiled.sha256` on all three lanes rehash to the retrieved scripts and inventories.

Imported ancestry is not in the local four-row freeze. It is pinned inside `compile_a8_d2.py` and the frozen low-`a` local-row compiler, and those pins still match on disk:

| Pin | SHA-256 |
|---|---|
| low-`a` `compile_local_row.py` | `b2fe07fdd2f855598dde5c6ef9828909c94496eb5e196756eff504056cde2769` |
| low-`a` `PRODUCER_FREEZE.sha256` | `4d69b97d8c6e24baadc76aba69d3d37158a3aa466cf7e44bc3111008c5a07fd3` |
| r1/d1 `compile_r1_d1_ac.py` | `e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c` |
| r1/d1 `FREEZE.sha256` | `34b0f3254410e39abfc9843febd3c053f965a30dfa948d9e0367c0fb094611a6` |
| support miner `mine_support.py` | `0e94e5408b8a3b5db06c8eff5c759df1c75a2e8bb4563aa4964f42c39952fe9a` |
| `tails.json` file / canonical | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` / `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` |
| load-ladder compiler | `77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc` |
| cge3 compiler | `352ad4f2d10df80e7edcc5179a8c46dfc55b4f7ce07762fb06d2109a9da1da23` |

The r1/d1 freeze itself rehashes 17/17. A pin mismatch would have aborted the AWS compiler before any `.sing` was written.

Exact Q is the characteristic-zero endpoint: Box03 compiled ring is `ring A8D2_R=0,...`. The `F_65521` and `F_65519` scripts are characteristic-normalized equal to the Q script (the only difference is the ring-characteristic token `0` versus `65521` or `65519`; sizes 158369 versus 158373 and 158373). Engine stdout streams are byte-identical (`3c95b429…`) because they are boolean/census markers, not polynomials. That agreement is a host/software screen, not a characteristic-zero proof. The Q run is the mathematical endpoint.

| Field | exact Q Box03 | `F_65521` r6d | `F_65519` Box02 |
|---|---|---|---|
| host | `ip-172-30-0-249` | `ip-172-30-0-45` | `ip-172-30-0-186` |
| launcher PID | 254161 | 318941 | 298666 |
| characteristic | 0 | 65521 | 65519 |
| start/end UTC | 18:28:03 / 18:28:03 | same | same |
| engine rc | 0 | 0 | 0 |
| wall | 0.57 s | 0.33 s | 0.33 s |
| peak RSS KiB | 136780 | 111048 | 111360 |
| swaps | 0 | 0 | 0 |
| compiler stderr | empty `e3b0c442…` | same | same |
| freeze check | 4/4 OK | same | same |
| archive SHA-256 | `95233012…` | same | same |
| inventory SHA-256 | `7c9cdf0a…` | `7a4a765c…` | `613b4453…` |
| stdout SHA-256 | `3c95b429…` | same | same |

GNU `time -v` is the only engine-stderr content. No Singular `error occurred` diagnostic appears in stdout or stderr. Compiler Python stdout contains the inventory JSON and no `FAIL`. Timeout 1800 s and VM cap 33554432 KiB match the launchers.

The `/tmp` source archive `952330121f34f99a4c14bde319766373d14d2da69c47aed2c40071e701231dfb` recorded in `AWS_LAUNCH_METADATA.md` was not retrieved. All three hosts record that same archive hash and a passing on-host `FREEZE` check. The repository freeze and the 36 evidence files are the custody used here.

A passing sentinel is not mathematics. The algebra below is independent of those sentinels.

---

## 1. Exact Q versus screens, AWS, ancestry

Charge 1 is custody and is closed in §0. The only additional point is that `run_aws.sh` is fail-closed: it refuses non-Linux/non-Amazon hosts, requires the registered tag prefix, accepts only characteristics `0,65519,65521`, checks `FREEZE.sha256` on the host, requires nine named census lines to occur exactly once, rejects `=FAIL` / `error occurred`, and rejects nonzero swap. The validator string `PASS_D1_A8_D2_LOADFIRST_DUAL_EMPTY` is a runner flag, not a proof. The remaining census lines (`LITERAL_ANALYTIC_BRIDGE`, `ALL_SEVEN_QUOTIENTS`, `VK60_MOVING_ROOT`, `POLE2_RECURRENCE`, `TARGET_FREE_ROWS134`) are multiplied into the endpoint product, so a zero among them cannot print `A8D2_ENDPOINT=PASS_EMPTY_A8_D2_CLOSED_R_TAIL`.

---

## 2. Independent primitive inventory

The square source is `f=K^2+sigma^5 D` with `K=L^2+sigma^2 R` and `D=LA+C`. Factoring `f=L^4(1+x)` produces four atoms of costs `(2,4,5,5)` in `sigma` and denominators `(2,4,3,4)`:

```text
2 sigma^2 R/L^2,   sigma^4 R^2/L^4,   sigma^5 A/L^3,   sigma^5 C/L^4,
```

with type-1 `R` scalar `2`. The four load summands are the binomial series of

```text
f^{3/2},   sigma^4 k10 f^{5/4},   sigma^{12} k6 f^{3/4},   sigma^{20} k2 f^{1/4},
```

alphas `3/2, 5/4, 3/4, 1/4` and delayed weights `Lambda^{2,6,10}` after `Lambda=sigma^2`. Pole order is `denominator - 4 alpha`. These alphas and weights are the frozen load-ladder generating function.

For `(a,d,r)=(8,2,>=8)` the atom costs are `(10,20,13,15)` and `T=30`. Independent expansion of every atom tuple through `T`, with bounds `budget//cost` and with one and two extra counts in every atom direction, produces identical polar signatures. Every positive atom cost is at least 10, so a degree-(bound+2) tuple already exceeds `T`. There is no cutoff hole. Pad `0`, `1`, and `2` agree.

Polar primitives, independently, six columns, max pole 2:

| grade | pole | coeff | load | `(R,A,C)` | fixed |
|---:|---:|---|---|---|---:|
| 27 | 1 | `3/4` | `k6` | `(0,0,1)` | 17 |
| 28 | 1 | `3/4` | unloaded | `(0,1,1)` | 10 |
| 29 | 1 | `5/8` | `k10` | `(1,0,1)` | 11 |
| 30 | 1 | `5/32` | `k10` | `(0,2,0)` | 14 |
| 30 | 1 | `1/2` | `k2` | `(1,0,0)` | 22 |
| 30 | 2 | `3/8` | unloaded | `(0,0,2)` | 10 |

The unique grade-27 polar is `k6 C`. The sole pole-two primitive in the window is unloaded `C^2` at grade 30, coefficient `3/8`. Binomial checks: unloaded `AC` is `binom(3/2,2)*2=3/4`; unloaded `C^2` is `binom(3/2,2)=3/8`; `k6 C` is `3/4`; `k10 RC` is `binom(5/4,2)*2*2=5/8`; `k10 A^2` is `5/32`; `k2 R` is `(1/4)*2=1/2`.

Holomorphic (`pole<=0`) terms exist and are discarded, including `k6 A` at grade 25 (pole 0) and `k10 RA` at grade 27 (pole 0). They are not polar source. No cancelled (coefficient-zero) polar key exists through grade 30. Through grade 40 the first cancelled keys are unloaded `R^2 A` at 33, unloaded `R^2 C` at 35, and unloaded `R^4` at 40; all lie after `T`.

No polar exists at grade 31 (atom costs plus delays cannot sum to 31). First omitted polar after the ceiling:

| grade | pole | coeff | load | `(R,A,C)` |
|---:|---:|---|---|---|
| 32 | 2 | `5/16` | `k10` | `(0,1,1)` |
| 32 | 1 | `3/8` | `k6` | `(2,0,0)` |

The first omitted primitive, ordered by `(grade, summand, pole, R, A, C)`, is `k10 AC` at grade 32. The `k6 R^2` coefficient `3/8` is the aggregate of two type-1 `R` (`-3/8`) plus one type-2 `R` (`3/4`). Neither enters the registered window. First omitted or misclassified polar through `T`: none.

Jet ceilings derived from `T - first_grade` over primitives carrying each stem match the compiled ring:

| stem | ceiling | compiled jets |
|---|---:|---|
| `p` | 3 | `ell1,ell2,ell3` |
| `A` | 2 | `a1,a1_1,a1_2` and `a0` likewise |
| `C` | 3 | `c1..c1_3`, `c0..c0_3` |
| `R` | 1 | `b1,b1_1`, `b0,b0_1` |
| `k10` | 1 | `k0,k0_1` |
| `k6` | 3 | `k60..k60_3` |
| `k2` | 0 | `k20` |
| `mu2` | 2 | `mu20,mu20_1,mu20_2` |
| `mu4` | 0 | `mu4` |

`R=sigma^8*(b1_series + t*b0_series)` does not invert `b0` or `b1`. Moving `P=p+2 sigma ell1+2 sigma^2 ell2+2 sigma^3 ell3`.

---

## 3. Seven literal Faber rows

Literal rows are `tail_text` of frozen `tails.json` (seven rows, 36/54/58/81/89/120/131 monomials, canonical digest `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`), with `Lambda -> sigma^2` and coefficient substitution from `source_coefficients` for `K=L^2+sigma^2 R`, `D=LA+C`, moving `P=p+2 sigma ell1+...`. Delayed loads in every compiled `SourcePhi_j` are the frozen weights `(sigma^2)^2 k10`, `(sigma^2)^6 k6`, `(sigma^2)^10 k2`. Direct inspection of `SourcePhi1` finds those three delayed weights and no `(sigma^2)^4`. `SourcePhi` begins with those delayed-load tail monomials, not with a handwritten polar list.

Targets:

```text
row 1,3,5: 0
row 2: sigma^{28} * (mu20 + sigma mu20_1 + sigma^2 mu20_2)
row 4: sigma^{32} * mu4
row 6: sigma^{36} * mu6
row 7: sigma^{38} * (J/4)
```

which is `sigma^{2(12+j)}` on rows with targets. `FullPhi2=SourcePhi2-(sigma^{28}*(mu20+sigma mu20_1+sigma^2 mu20_2))`, so the row-2 target is retained through grade 30. Rows 1 and 3 subtract `0`. Row 4 subtracts `sigma^{32}*mu4`, which lies after `T=30`, so rows 1, 3, and 4 are target-free through the registered `T`. Independently, `SourcePhi4-FullPhi4=sigma^{32} mu4` is zero modulo `sigma^{31}`. The compiled firewall is `reduce((S1-F1)+(S3-F3)+(S4-F4), (sigma^{31}))==0`. The row-2 identity is an equality, not a reduction: `FullPhi2-SourcePhi2=-(sigma^{28}*mu20_series)`.

The compact analytic emitter `H` contains exactly the independently enumerated primitives, with the same coefficients, `sigma` prefixes, `t`-powers `1+2q-eR-eA-eC`, and inverse series `(1+(P/2)t^2)^{-q}` through `t^8`. Compiled `H` is the sum of six terms:

```text
(3/4) sigma^{17} k6 t^2 C Inv1
(3/4) sigma^{10} t A C Inv1
(5/8) sigma^{11} k10 t R C Inv1
(5/32) sigma^{14} k10 t A^2 Inv1
(1/2) sigma^{22} k2 t^2 R Inv1
(3/8) sigma^{10} t^3 C^2 Inv2
```

with five `Inv1` factors and one `Inv2`. The pole-two inverse is

```text
1 - 2(P/2)t^2 + 3(P/2)^2 t^4 - 4(P/2)^3 t^6 + 5(P/2)^4 t^8.
```

`A,C,R` are the compiled jets `sigma^8 (a1_series + t a0_series)`, `sigma^{10} (c1_series + t c0_series)`, `sigma^8 (b1_series + t b0_series)`. Predicted Faber rows from `H` are the standard Chebyshev/Pell images of `L=z^2+P/2`:

```text
Phi1=h1
Phi2=h2
Phi3=h3+(P/4)h1
Phi4=h4+(P/2)h2
Phi5=h5+(3P/4)h3+(3 P^2/32)h1
Phi6=h6+P h4+(P^2/4)h2
Phi7=h7+(5P/4)h5+(15 P^2/32)h3+(5 P^3/128)h1
```

with every powered numerator parenthesized. The client reduces `SourcePhi_j - PredPhi_j` modulo `sigma^{31}`. Independently, `H=t*(polar part)` in the coordinate `t=1/z` produces those same `Phi_j` as the connection coefficients, and extra `t^{10}` cannot enter `[t^8]=h7`. The four atoms of `source_coefficients` are the same `x` as in §2, so the literal tails and the compact `H` are two presentations of one generating function. Every full row is then extracted from grade 27 through 30 with recursive quotient identities `sigma * Q_{g+1} = Q_g - [sigma^0]Q_g`.

Observation, non-blocking: the pairing extractors compute `Psi_pm_exact` and the grade-28 `h` extractors compute `GH1_exact`, but the endpoint product multiplies `Root_exact` and the coefficient equalities, not those exactness flags. Source valuation is independently at least 27, and on `V(k60)` the grade-27 column vanishes, so this is not a failing identity.

---

## 4. Exhaustive split and load-open branch `D(k60)`

For any section `k60` of the structure sheaf, `Spec = D(k60) union V(k60)` scheme-theoretically. There is no third chamber.

On `D(k60)` the unique polar primitive at grade 27 is `k6 C`. Write `t=1/z` and `Inv1=(1+(p/2)t^2)^{-1}`. At leading grade, `k6=k60` and `C=sigma^{10}(c1+t c0)`, so

```text
H = (3/4) k60 t^2 (c1 + t c0) + O(t^4) + O(sigma^{28}),
```

hence `[t^2]=(3/4)k60 c1` and `[t^3]=(3/4)k60 c0`. These are `h1` and `h2`, which are `Phi1` and the source part of `Phi2`. The row-2 target is `sigma^{28}*mu20_series`, so it is absent at grade 27. On `D(c1)` the single generator `(3/4)k60 c1` is a unit after inverting `k60` (`3/4` is a unit in characteristic zero). On `D(c0)` the same holds with `c0`. Exact `ord(C)=10` is `D(c1) union D(c0)`. The compiled unit ideals are `std(h1,h2,ik60 k60-1, ic1 c1-1)` and the `c0` twin; `reduce(1)==0` is the unit ideal, not merely a radical emptiness.

No later polar is needed on this branch: the scheme of the seven equations is already empty at grade 27.

---

## 5. Load-closed branch `V(k60)`: tied column, determinant, rank jump

At grade `G=28` the polar primitives are `k6 C` and unloaded `AC`, both coefficient `3/4`, both pole 1. On `V(k60)` one has `k6=sigma k60_1+...`, so both columns sit at grade 28.

- `AC` contributes `(3/4) t (a1+t a0)(c1+t c0) Inv1`, so
  `[t^2]=(3/4)(a1 c0+a0 c1)` and `[t^3]=(3/4)(a0 c0-(p/2)a1 c1)`.
- `k6 C` contributes `(3/4) k60_1 t^2 (c1+t c0) Inv1`, so
  `[t^2]=(3/4)k60_1 c1` and `[t^3]=(3/4)k60_1 c0`.

The leftover `k60 c1_1` in `[sigma^{28}]h1` is killed by `k60=0`. Hence

```text
Nfirst = h1 z + h2
       = (3/4)[ (a1 c0 + (a0+k60_1)c1) z + ((a0+k60_1)c0 - (p/2)a1 c1) ]
       = (3/4) C (A+k60_1)   reduced modulo L=z^2+p/2.
```

Writing `A+k60_1=u z+v` and `C=x z+y` (so `u=a1`, `v=a0+k60_1`, `x=c1`, `y=c0`), multiplication by `C` in `Q[z]/(z^2+p/2)` is

```text
(x z+y)(u z+v) = (u y + v x) z + (v y - (p/2) u x),
```

so `r_z=uy+vx`, `r_0=vy-(p/2)ux`. The matrix on the basis `(z,1)` is

```text
[  y      x ]
[-(p/2)x  y ]
```

with determinant `Delta_C=y^2+(p/2)x^2=c0^2+(p/2)c1^2`. On `D(Delta_C)` the matrix is invertible: `a1=(c0 r_z - c1 r_0)/Delta_C`, and likewise for `a0+k60_1`. Thus `r_z=r_0=0` forces `u=v=0`. That is the compiled rank-two chamber `reduce(a1, Rank2)==0` and `reduce(a0+k60_1, Rank2)==0` after inverting `Delta_C` and setting `k60=0`.

The rank-one face `Delta_C=0` is not discarded and is not divided by. If `C` is nonzero and vanishes at exactly one etale root, multiplication by `C` has a one-dimensional kernel, so a nonzero `A+k60_1` in that kernel survives the first wall. That face is closed by the dual functionals of §6, not by inverting `Delta_C`.

The compiled `first_tie` reduces the grade-28 identity modulo `RootK0`, which is larger than `(k60)` because it also contains the moving-root equations and `ilam*lam-1`. Independently the identity is polynomial after only `k60=0` (no `lambda` enters `h1` or `h2` at this grade: `Inv1` corrections begin at `t^4`). Enlarging the ideal cannot manufacture a false pass of a polynomial that is already zero.

---

## 6. Pole-two reconstruction, moving-root functionals, pairings, unit ideals, descent

In the coordinate `t=1/z`, `L=z^2+P/2=t^{-2}(1+(P/2)t^2)` and a cubic numerator `N=n3 z^3+n2 z^2+n1 z+n0` gives

```text
t * N/L^2 = (n3 t^2 + n2 t^3 + n1 t^4 + n0 t^5) (1+(P/2)t^2)^{-2}.
```

Writing `H=sum_{j>=1} h_j t^{j+1}` and expanding `Inv2=1-P t^2+...` yields `n3=h1`, `n2=h2`, `n1=h3+P h1`, `n0=h4+P h2`, hence

```text
N = h1 z^3 + h2 z^2 + (h3+P h1) z + (h4+P h2).
```

Pole ceiling two is the statement that `H(1+(P/2)t^2)^2` has `t`-degree at most 5, i.e.

```text
h5 + P h3 + (P^2/4) h1 = 0,
h6 + P h4 + (P^2/4) h2 = 0,
h7 + P h5 + (P^2/4) h3 = 0
```

modulo `sigma^{31}`. These are the compiled `Rec5,Rec6,Rec7`. Independently, no pole-3 primitive exists through `T` (earliest pole-3 is `k10 C^2` at grade 34).

The Faber connection on rows 1,3,4 is

```text
Psi_+ = Phi4 + lambda (Phi3 + (P/4) Phi1),
Psi_- = Phi4 - lambda (Phi3 + (P/4) Phi1).
```

Substituting the predicted `Phi_j` gives `Psi_+ = h4+(P/2)h2 + lambda(h3+(P/2)h1)`. Direct subtraction produces the identity

```text
N(lambda) - Psi_+ = (lambda^2 + P/2)(h1 lambda + h2),
```

and likewise `N(-lambda)-Psi_- = (lambda^2+P/2)(-h1 lambda + h2)`. On the moving-root locus `lambda(sigma)^2=-P(sigma)/2` both differences vanish, including every Hensel correction `rho_j`. Signs are therefore `Psi_pm=N(+/- lambda)`, not the swapped pair.

The compiled root is `lam+sigma rho1+sigma^2 rho2+sigma^3 rho3` with outer parentheses around `(root)^2+P/2`, constant term checked as `p/2+lam^2`, and higher coefficients generating `RootK0` together with `k60` and `ilam*lam-1`. `P` is the moving series. After `subst(p,-2*lam^2)` and reduction by `RootK0`, the functionals are evaluated on the finite etale cover. The minus functional uses `(-(root))`, which is the swapped root.

A pole-one column has `H=M/L` with `M` of degree at most 1, so `N=H L^2=M L` vanishes at both roots of the moving `L`. Hence `N(+/- lambda(sigma))=0` identically in `sigma`, including every jet of `A,C,R`, every later load (`k10 RC` at 29, `k10 A^2` and `k2 R` at 30, remaining `k6` jets `k60_1,k60_2,k60_3`), and every moving-`p` correction of the tied columns. The only pole-two column through `T` is `(3/8)C^2/L^2` at grade 30.

At exact grade 30 only the leading coefficients of `C` enter. With `Inv2=1-P t^2+O(t^4)`,

```text
H_{C^2} = (3/8) t^3 (c1 + c0 t)^2 Inv2
        = (3/8)( c1^2 t^3 + 2 c1 c0 t^4 + (c0^2 - P c1^2) t^5 ) + O(t^6),
```

so `h2=(3/8)c1^2`, `h3=(3/4)c1 c0`, `h4=(3/8)(c0^2-P c1^2)`, and

```text
N = (3/8)(c1 z + c0)^2
```

after the `P h2` reconstruction term cancels `-P c1^2`. Therefore

```text
N(lambda)  = (3/8)(c1 lambda + c0)^2,
N(-lambda) = (3/8)(-c1 lambda + c0)^2.
```

C-jets, moving-`p` jets, and other primitives contribute only at grade `>30` or are pole-one. Compiled dual-pair tests are exactly these identities: lower coefficients of both `Psi_pm` vanish in `28,29`, and the grade-`30` coefficients equal `q_pm` after `RootK0`.

Functionals are built from `SourcePhi1,3,4`. Rows 1, 3, and 4 are target-free through grade 30, so `SourcePhi_j=FullPhi_j` in the window and the two functionals are source-exact. Row 2 is retained but does not enter `Psi_pm`. Emptiness of `(Phi1,Phi3,Phi4)` already empties the seven-row scheme.

Unit ideals before radicals. Let `alpha=lambda c1+c0` and `beta=-lambda c1+c0`. Then `q_+=(3/8)alpha^2`, `q_-=(3/8)beta^2`, and `3/8` is a unit in characteristic zero. On `D(lambda c1)`, `alpha-beta=2 lambda c1` is a unit (characteristic not 2, and `lambda`, `c1` inverted). In the quotient by `(alpha^2,beta^2)` one would have `alpha=beta+u` with `u` a unit, hence `0=alpha^2=(beta+u)^2=2u beta+u^2`, so `beta=-u/2` and `beta^2=u^2/4=0`, contradicting that `u` is a unit. Thus `(alpha^2,beta^2)=(1)`. On `D(lambda c0)`, `alpha+beta=2 c0` is a unit, and the same conclusion holds. The compiled check is Groebner membership `reduce(1, UnitC*)==0`, which is the unit ideal, not merely a radical emptiness. Inverting `k0` restricts to the registered ambient chart `D(k0)` and is not used by `q_pm`. Setting `k60=0` restricts to `V(k60)`.

Exact `ord(C)=10` is the condition that the two leading coefficients of `C` are not both zero, i.e. `D(c1) union D(c0)`. Together with `D(lambda)` (the etale cover of `D(p)`) this is the pair of charts above.

Rank-one face `Delta_C=0`: `Delta_C=c0^2+(p/2)c1^2=alpha beta` after `lambda^2=-p/2`. Exactly one of `alpha,beta` vanishes when `C` is nonzero and vanishes at one root. Then one of `q_pm` vanishes and the other is `(3/8)(2 lambda c1)^2` or `(3/8)(2 c0)^2`, a unit on `D(lambda c1)` or `D(lambda c0)` respectively. Simultaneous vanishing of both functionals forces `c0=c1=0`, which is not exact contact. The dual functionals therefore cover the rank-one chamber without dividing by `Delta_C`.

The map `p=-2 lambda^2` from `D(lambda)` to `D(p)` is finite etale of degree two in characteristic zero (derivative `-4 lambda != 0`). It is surjective onto `D(p)`. Emptiness of `V(Phi1,Phi3,Phi4)` on the cover, on both exact-contact charts, therefore descends to the unsplit chart `D(p*k0)` with exact `ord(C)=10`.

`R` is written `sigma^8*(b1_series + t*b0_series)`. Neither `b0` nor `b1` is inverted in any unit ideal or chart (`ib0` and `ib1` are absent). The claim is the closed tail `ord(R)>=8`, not only the exact-order slice.

---

## 7. Firewall

A confirmed verdict closes only the named strict cell `a=8`, `d=2`, `ord(R)>=8`, after the cited upstream gates on `D(p*k0)`. It does not cover:

- `a=8,d=3`, whose first load grade 28 already coincides with the row-2 target (target-shadowed, not load-first);
- `a=9` (further load-first);
- equality faces or other D1 charts;
- grade-32 row-4 target-shadow chambers (`mu4` starts at grade 32, after `T`);
- a positive-order leading `k10`, or `p=0`, or `k0=0`;
- the whole square component, order two, `(8,12)`, maximum twelve, or JC2.

The compiler hardcodes `(a,d,c,r)=(8,2,10,8)`. The inventory scope string is `A8_D2_ONLY_NO_A8D3_A9_OR_GLOBAL_VERDICT`. `RESULT.md` and `PREREGISTRATION.md` name the same exclusions. No timing or emptiness claim may be extrapolated off this cell.

---

## Defect classification

| Class | Item |
|---|---|
| Mathematical defect | none. Smallest failing identity: none. Earliest missing source monomial through grade 30: none. First later polar: `k10 AC` at grade 32, pole 2, coefficient `5/16` |
| Custody/software defect | none that breaks a numbered claim. The `/tmp` archive was not retrieved; on-host freeze checks and the repository freeze are the custody. Local `FREEZE.sha256` is the four producer files; imported ancestry is compiler-pinned and rehashes. `GH1_exact` / `Psi_pm_exact` are computed and not multiplied into the endpoint product; independent valuation `>=27` (and vanishing of grade 27 on `V(k60)`) closes that hole |
| Scope wording defect | none. The theorem statement, preregistration, and RESULT firewall name only the `a=8,d=2,ord(R)>=8` cell on `D(p*k0)`. Charts `D(c1)` and `D(c0)` in RESULT are the exact-contact condition inside that ambient chart, matching the client inversions of `k60` on the load-open branch and of `lambda` and `k0` on the load-closed branch |

CONFIRMED
