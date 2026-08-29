# Hostile review — D1 `a=7` load-tie dual-functional wall

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_a7_loadtie_dual_functional_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Earliest missing source monomial | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, validator strings, and finite-field agreement are not authority |
| Method | SHA-256 of every named pin, nested compiled manifest, and evidence file; independent four-summand binomial expansion through each `T` with pad `0,1,2`; hand derivation of the tied numerator, `Delta_C` rank, pole-two reconstruction, moving-root functionals, pairings, and unit ideals. No Singular, Sage, msolve, Lean, or other heavy CAS |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the seven required primary pins match. Every path named in `FREEZE.sha256` (25 rows), `EVIDENCE.sha256` (39 rows), and `PRODUCER_FREEZE.sha256` (5 rows) rehashes to the printed digest. All three nested `compiled.sha256` files rehash to the retrieved `.sing` scripts and `source_inventory.json`. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

After the registered square/D1 gates, over characteristic zero on `D(p*k0)`, the seven literal Faber equations have no point in either strict cell

```text
ord(A)=7, ord(C)=9,  ord(R)>=7,     (d=2),
ord(A)=7, ord(C)=10, ord(R)>=7.     (d=3)
```

The independently expanded source through `T=28` (resp. `T=30`) has five (resp. seven) polar primitives, global pole ceiling two, and sole pole-two column `(3/8)C^2/L^2` at `T`. At the first wall `G=24+d` the grade-`G` column is exactly `(3/4)C(A+k60)/L`. On `D(Delta_C)` that numerator forces `A+k60=0`. The rank-one face `Delta_C=0` is not divided out: both moving-root functionals

```text
Psi_pm = Phi4 +/- lambda*(Phi3+(p/4)Phi1) = N(+/- lambda),
lambda(sigma)^2 = -p(sigma)/2,
```

vanish identically in grades `G,...,T-1` and equal

```text
q_+ = (3/8)(c1*lambda+c0)^2,   q_- = (3/8)(-c1*lambda+c0)^2
```

at `T`. The ideals `(q_+,q_-)` are the unit ideal on both exact-contact charts `D(lambda*c1*k0)` and `D(lambda*c0*k0)`, before taking radicals, including the rank-one chamber. Rows 1, 3, and 4 are target-free through each `T`, so those three full rows cannot vanish. Finite etale descent from the root cover empties the unsplit chart. Leading `R` is uninverted, so these are the closed `ord(R)>=7` tails.

The two named cells are the entire claim. There is no `a=8,9`, target-shadow, other D1 face, square-component, maximum-twelve, or JC2 statement.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Seven primary pins | hashes | all seven match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 25/25, `EVIDENCE` 39/39, `PRODUCER_FREEZE` 5/5, three nested `compiled.sha256` 3/3 each |
| 1. Exact Q vs screens, AWS, failed preflight | rc, diagnostics, archive, swap, parenthesization-only | **holds**; exact Q is the endpoint; `F_65521` and `F_65519` are independent host screens; preflight supplied no imported verdict |
| 2. Primitive inventories | independent expansion through `T=28,30`, pad+1/+2, pole ceiling, sole `C^2` | **holds**; counts five and seven; earliest missing monomial none; earliest later polar is `k2 R` at grade 29 for `d=2` |
| 3. Seven literal rows | delayed loads, moving `p`, jets, `mu20` through 30, rows 1/3/4 target-free, compact/literal bridge, sigma quotients | **holds** |
| 4. First-wall collision | tied column, `r_z`, `r_0`, `Delta_C`, rank-two on `D(Delta_C)`, rank-one face retained | **holds** |
| 5. Pole-two reconstruction | `N=h1 z^3+...`, `Psi_pm=N(+/-lambda)`, signs, moving root, recurrence | **holds** |
| 6. Pairings and unit ideals | pole-one vanish through `T`; `q_pm` exact; unit ideals before radicals; rank-one covered | **holds** |
| 7. Descent and closed `R` | finite etale on `D(p)`; no leading `R` inverted; no equality/positive-order-load face imported | **holds** |
| 8. Firewall | only `a=7`, `d=2,3` after `D(p*k0)` | **holds** |

No mathematical defect, custody/software defect that breaks a numbered claim, or scope wording defect that enlarges the theorem was found.

---

## 0. Custody

Recomputed SHA-256 of the seven required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `69048f6fd2f3ddf78e8328840d0400fe29d523c5258fbd5c154b211559c433aa` | producer report |
| `.../AWS_LAUNCH_METADATA.md` | `7c1d9f1bf8ff636c21a5be7736652b46bb24c6bfa2cb42149714d42be121de65` | AWS metadata |
| `.../FAILED_ATTEMPTS.md` | `7c3e059fc48cde62bbfcca4378e682d3c919071961e7db443061b6ca82fb48b8` | quarantined preflight |
| `.../EVIDENCE.sha256` | `478bee84248b6ee9ccca1a033093a30f5fafdbe091a76b5a0ad8ef89ab0c28f8` | evidence freeze |
| `.../FREEZE.sha256` | `b22a61508cde775693355fbfc4beda71950382c6561ba8ea5ef92a4b0f6b2d0d` | source freeze |
| `.../PRODUCER_FREEZE.sha256` | `bb662b3d25cd12dec712dc2763e1efd6dd09b1dd084babce65bcb9effb0daac0` | producer freeze |
| `.../compile_a7_loadtie.py` | `d77145b5984601e4887f9597f7867e4a1a80929b2aa35607b1447feee61d1149` | compiler |

`FREEZE.sha256` names 25 files, all matching, including the imported low-`a` local-row compiler and producer freeze, the r1/d1 compiler and freeze, the support miner, `compile_cge3_universal.py`, `tails.json` `d72f774c…`, `compile_square_load_ladder.py`, and the five named xmodel pins. `PRODUCER_FREEZE.sha256` repeats the five producer documents and matches. `EVIDENCE.sha256` names the three AWS boxes only (exact Q on Box03, `F_65521` on r6d, `F_65519` on Box02); 39/39 rehash. Nested `compiled.sha256` on all three lanes rehash.

Exact Q is the characteristic-zero endpoint: Box03 compiled rings are `ring A7D*_R=0,...`. The `F_65521` and `F_65519` scripts are characteristic-normalized equal to the Q scripts (the only difference is the ring-characteristic token `0` versus `65521` or `65519`; size gaps 152272 versus 152276 and 185484 versus 185488). Engine stdout streams are byte-identical (`de1f2dd8…`) because they are boolean/census markers, not polynomials. That agreement is a host/software screen, not a characteristic-zero proof. The Q run is the mathematical endpoint.

| Field | exact Q Box03 | `F_65521` r6d | `F_65519` Box02 |
|---|---|---|---|
| host | `ip-172-30-0-249` | `ip-172-30-0-45` | `ip-172-30-0-186` |
| characteristic | 0 | 65521 | 65519 |
| engine rc | 0 | 0 | 0 |
| wall | 1.63 s | 1.00 s | 0.98 s |
| peak RSS KiB | 336972 | 268448 | 268068 |
| swaps | 0 | 0 | 0 |
| compiler stderr | empty `e3b0c442…` | same | same |
| freeze check | 25/25 OK | same | same |
| archive SHA-256 | `96116048…` | same | same |

GNU `time -v` is the only engine-stderr content. No Singular `error occurred` diagnostic appears in stdout or stderr. Compiler Python stdout contains the inventory JSON and no `FAIL`.

The `/tmp` source archive `961160487ad73db79475f37b7d7868733141bc5b65fed3261d08fc54efa86be1` recorded in `AWS_LAUNCH_METADATA.md` was not retrieved. All three hosts record that same archive hash and a passing on-host `FREEZE` check. The repository freeze and the 39 evidence files are the custody used here.

The first Box03 preflight is recorded only in `FAILED_ATTEMPTS.md` and the metadata paragraph. It is not present in `EVIDENCE.sha256`. The described bug is string parenthesization of the moving-root polynomial passed to `sigma_extract`: without outer parentheses, Singular parses `Q - (lam+...)^2 + P/2 == 0` by left-associativity and squares only the last syntactic summand. No mathematical endpoint was reached. The frozen compiler emits `((lam+sigma*rho1+...)^2+(P/2))`, and the compiled Q scripts contain that protected form in both the quotient and the exactness test. No failed bytes are used as theorem evidence.

A passing sentinel is not mathematics. The algebra below is independent of those sentinels.

---

## 1. Exact Q versus screens, AWS, failed preflight

Charge 1 is custody and is closed in §0. The only additional point is that `run_aws.sh` is fail-closed: it refuses non-Linux/non-Amazon hosts, requires the registered tag prefix, accepts only characteristics `0,65519,65521`, checks `FREEZE.sha256` on the host, requires the twelve named census lines to occur exactly once, rejects `=FAIL` / `error occurred`, and rejects nonzero swap. The validator string `PASS_D1_A7_LOADTIE_DUAL_FUNCTIONAL_D2_D3_EMPTY` is a runner flag, not a proof.

---

## 2. Independent primitive inventories

The square source is `f=K^2+sigma^5 D` with `K=L^2+sigma^2 R` and `D=LA+C`. Factoring `f=L^4(1+x)` produces four atoms of costs `(2,4,5,5)` in `sigma` and denominators `(2,4,3,4)`:

```text
2 sigma^2 R/L^2,   sigma^4 R^2/L^4,   sigma^5 A/L^3,   sigma^5 C/L^4,
```

with type-1 `R` scalar `2`. The four load summands are the binomial series of

```text
f^{3/2},   sigma^4 k10 f^{5/4},   sigma^{12} k6 f^{3/4},   sigma^{20} k2 f^{1/4},
```

alphas `3/2, 5/4, 3/4, 1/4` and delayed weights `Lambda^{2,6,10}` after `Lambda=sigma^2`. Pole order is `denominator - 4 alpha`. These alphas and weights are the frozen load-ladder generating function.

For `(a,d,r)=(7,2,>=7)` the atom costs are `(9,18,12,14)` and `T=28`. For `(7,3,>=7)` they are `(9,18,12,15)` and `T=30`. Independent expansion of every atom tuple through each `T`, with bounds `budget//cost` and with one and two extra counts in every atom direction, produces identical polar signatures. Every positive atom cost is at least 9, so a degree-(bound+2) tuple already exceeds `T`. There is no cutoff hole.

Polar primitives, independently:

`d=2`, `T=28`, five columns, max pole 2:

| grade | pole | coeff | load | `(R,A,C)` | fixed |
|---:|---:|---|---|---|---:|
| 26 | 1 | `3/4` | `k6` | `(0,0,1)` | 17 |
| 26 | 1 | `3/4` | unloaded | `(0,1,1)` | 10 |
| 27 | 1 | `5/8` | `k10` | `(1,0,1)` | 11 |
| 28 | 1 | `5/32` | `k10` | `(0,2,0)` | 14 |
| 28 | 2 | `3/8` | unloaded | `(0,0,2)` | 10 |

`d=3`, `T=30`, seven columns, max pole 2:

| grade | pole | coeff | load | `(R,A,C)` | fixed |
|---:|---:|---|---|---|---:|
| 27 | 1 | `3/4` | `k6` | `(0,0,1)` | 17 |
| 27 | 1 | `3/4` | unloaded | `(0,1,1)` | 10 |
| 28 | 1 | `5/32` | `k10` | `(0,2,0)` | 14 |
| 28 | 1 | `5/8` | `k10` | `(1,0,1)` | 11 |
| 29 | 1 | `1/2` | `k2` | `(1,0,0)` | 22 |
| 30 | 1 | `3/8` | `k6` | `(2,0,0)` | 16 |
| 30 | 2 | `3/8` | unloaded | `(0,0,2)` | 10 |

The sole pole-two primitive in each window is unloaded `C^2` at grade `T`, coefficient `3/8`. Binomial checks: unloaded `AC` is `binom(3/2,2)*2=3/4`; unloaded `C^2` is `binom(3/2,2)=3/8`; `k6 C` is `3/4`; `k10 RC` is `binom(5/4,2)*2*2=5/8`; `k10 A^2` is `5/32`; `k2 R` is `(1/4)*2=1/2`. The `k6 R^2` coefficient `3/8` is the aggregate of two type-1 `R` (`-3/8`) plus one type-2 `R` (`3/4`).

For `d=3` there is one cancelled key at grade 30: unloaded `R^2 A`, pole 1, coefficient `0`, from `-3/4+3/4`. That monomial is absent from the source, not hidden by cancellation. No cancelled key reappears with a nonzero coefficient after padding.

Holomorphic (`pole<=0`) terms exist and are discarded, including `k6 A` at grade 24 (pole 0). They are not polar source.

Earliest polar after each ceiling: for `d=2`, `k2 R` at grade 29, then `k6 R^2` at 30. For `d=3`, `k10 R^3` and `k10 AC` at grade 31. None of these enters the registered window. First omitted or misclassified polar through `T`: none.

Jet ceilings derived from `T - first_grade` over primitives carrying each stem match the compiled rings:

| | `d=2` | `d=3` |
|---|---|---|
| `p` | 2 | 3 |
| `A,C` | 2 | 3 |
| `R` | 1 | 2 |
| `k10` | 1 | 2 |
| `k6` | 2 | 3 |
| `k2` | 0 | 1 |
| `mu2` | 0 | 2 |
| `mu4` | 0 | 0 |

`R=sigma^7*(b1_series + t*b0_series)` does not invert `b0` or `b1`.

---

## 3. Seven literal Faber rows

Literal rows are `tail_text` of frozen `tails.json` (seven rows, 36/54/58/81/89/120/131 monomials, canonical digest `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`), with `Lambda -> sigma^2` and coefficient substitution from `source_coefficients` for `K=L^2+sigma^2 R`, `D=LA+C`, moving `P=p+2 sigma ell1+...`. Delayed loads in every compiled `SourcePhi_j` are the frozen weights `(sigma^2)^2 k10`, `(sigma^2)^6 k6`, `(sigma^2)^10 k2`. `SourcePhi` begins with those delayed-load tail monomials, not with a handwritten polar list.

Targets:

```text
row 1,3,5: 0
row 2: sigma^{28} * mu20_series
row 4: sigma^{32} * mu4
row 6: sigma^{36} * mu6
row 7: sigma^{38} * (J/4)
```

which is `sigma^{2(12+j)}` on rows with targets. For `d=2`, `FullPhi2=SourcePhi2-(sigma^28*mu20)` and `mu2max=0`. For `d=3`, `FullPhi2=SourcePhi2-(sigma^28*(mu20+sigma mu20_1+sigma^2 mu20_2))`, so the row-2 target is retained through grade 30. Rows 1 and 3 subtract `0`. Row 4 subtracts `sigma^{32}*mu4`, which lies after both ceilings (`T=28` and `T=30`), so rows 1, 3, and 4 are target-free through each registered `T`. The compiled firewall is `reduce((S1-F1)+(S3-F3)+(S4-F4), (sigma^{T+1}))==0`.

The compact analytic emitter `H` contains exactly the independently enumerated primitives, with the same coefficients, `sigma` prefixes, `t`-powers `1+2q-eR-eA-eC`, and inverse series `(1+(P/2)t^2)^{-q}` through `t^8`. Compiled counts: `d=2` has four `Inv1` factors and one `Inv2`; `d=3` has six `Inv1` and one `Inv2`. The pole-two inverse is

```text
1 - 2(P/2)t^2 + 3(P/2)^2 t^4 - 4(P/2)^3 t^6 + 5(P/2)^4 t^8.
```

Predicted Faber rows from `H` are the standard Chebyshev/Pell images of `L=z^2+P/2`:

```text
Phi1=h1
Phi2=h2
Phi3=h3+(P/4)h1
Phi4=h4+(P/2)h2
Phi5=h5+(3P/4)h3+(3 P^2/32)h1
Phi6=h6+P h4+(P^2/4)h2
Phi7=h7+(5P/4)h5+(15 P^2/32)h3+(5 P^3/128)h1
```

with every powered numerator parenthesized. The client reduces `SourcePhi_j - PredPhi_j` modulo `sigma^{T+1}`. Independently, `H=t*(polar part)` in the coordinate `t=1/z` produces those same `Phi_j` as the connection coefficients, and extra `t^{10}` cannot enter `[t^8]=h7`. Every full row is then extracted from grade `G` through `T` with recursive quotient identities `sigma * Q_{g+1} = Q_g - [sigma^0]Q_g`.

Observation, non-blocking: the pairing extractors compute `Psi_pm_exact` but the endpoint product multiplies `Root_exact` and the coefficient equalities, not `Psi_pm_exact`. Source valuation is independently at least `G`, so this is not a failing identity.

---

## 4. First-wall collision

At grade `G=24+d` the only polar primitives are `k6 C` and unloaded `AC`, both coefficient `3/4`, both pole 1. Write `t=1/z` and `Inv1=(1+(p/2)t^2)^{-1}`.

- `AC` contributes `(3/4) t (a1+t a0)(c1+t c0) Inv1`, so
  `[t^2]=(3/4)(a1 c0+a0 c1)` and `[t^3]=(3/4)(a0 c0-(p/2)a1 c1)`.
- `k6 C` contributes `(3/4) k60 t^2 (c1+t c0) Inv1`, so
  `[t^2]=(3/4)k60 c1` and `[t^3]=(3/4)k60 c0`.

Hence

```text
Nfirst = h1 z + h2
       = (3/4)[ (a1 c0 + (a0+k60)c1) z + ((a0+k60)c0 - (p/2)a1 c1) ]
       = (3/4) C (A+k60)   reduced modulo L=z^2+p/2.
```

Writing `A+k60=u z+v` and `C=x z+y` (so `u=a1`, `v=a0+k60`, `x=c1`, `y=c0`), multiplication by `C` in `Q[z]/(z^2+p/2)` is

```text
(x z+y)(u z+v) = (u y + v x) z + (v y - (p/2) u x),
```

so `r_z=uy+vx`, `r_0=vy-(p/2)ux`. The matrix on the basis `(z,1)` is

```text
[  y      x ]
[-(p/2)x  y ]
```

with determinant `Delta_C=y^2+(p/2)x^2=c0^2+(p/2)c1^2`. On `D(Delta_C)` the matrix is invertible, so `r_z=r_0=0` forces `u=v=0`, i.e. `a1=0` and `a0+k60=0`. That is the compiled rank-two chamber.

The rank-one face `Delta_C=0` is not discarded and is not divided by. If `C` is nonzero and vanishes at exactly one etale root, multiplication by `C` has a one-dimensional kernel, so a nonzero `A+k60` in that kernel survives the first wall. That face is closed by the dual functionals of §6, not by inverting `Delta_C`.

---

## 5. Pole-two reconstruction and moving-root functionals

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

modulo `sigma^{T+1}`. These are the compiled `Rec5,Rec6,Rec7`. Independently, no pole-3 primitive exists through either `T` (earliest pole-3 is `k10 C^2` at grade 32 for `d=2` and 34 for `d=3`).

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

The compiled root is `lam+sigma rho1+...` with outer parentheses around `(root)^2+P/2`, constant term checked as `p/2+lam^2`, and higher coefficients generating `RootIdeal` together with `ilam*lam-1`. `P` is the moving series. After `subst(p,-2*lam^2)` and reduction by `RootIdeal`, the functionals are evaluated on the finite etale cover.

---

## 6. Pairings, first nonzero target pair, unit ideals, rank-one cover

A pole-one column has `H=M/L` with `M` of degree at most 1, so `N=H L^2=M L` vanishes at both roots of the moving `L`. Hence `N(+/- lambda(sigma))=0` identically in `sigma`, including every jet of `A,C,R`, every later load (`k10 RC`, `k10 A^2`, `k2 R`, `k6 R^2`), and every moving-`p` correction of the tied columns. The only pole-two column through `T` is `(3/8)C^2/L^2` at grade `T`.

At exact grade `T` only the leading coefficients of `C` enter. With `Inv2=1-P t^2+O(t^4)`,

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

C-jets, moving-`p` jets, and other primitives contribute only at grade `>T` or are pole-one. Compiled dual-pair tests are exactly these identities: lower coefficients of both `Psi_pm` vanish in `G,...,T-1`, and the grade-`T` coefficients equal `q_pm` after `RootIdeal`.

Unit ideals before radicals. Let `alpha=lambda c1+c0` and `beta=-lambda c1+c0`. Then `q_+=(3/8)alpha^2`, `q_-=(3/8)beta^2`, and `3/8` is a unit in characteristic zero. On `D(lambda c1)`,

```text
alpha - beta = 2 lambda c1
```

is a unit (characteristic not 2, and `lambda`, `c1` inverted). Thus `(alpha,beta)=(1)`, hence `(alpha^2,beta^2)=(1)`. On `D(lambda c0)`, `alpha+beta=2 c0` is a unit, and the same conclusion holds. The compiled check is Groebner membership `reduce(1, UnitC*)==0`, which is the unit ideal, not merely a radical emptiness. Inverting `k0` restricts to the registered ambient chart `D(k0)` and is not used by `q_pm`.

Exact `ord(C)=7+d` is the condition that the two leading coefficients of `C` are not both zero, i.e. `D(c1) union D(c0)`. Together with `D(lambda)` (the etale cover of `D(p)`) this is the pair of charts above.

Rank-one face `Delta_C=0`: `Delta_C=c0^2+(p/2)c1^2=alpha beta` after `lambda^2=-p/2`. Exactly one of `alpha,beta` vanishes when `C` is nonzero and vanishes at one root. Then one of `q_pm` vanishes and the other is `(3/8)(2 lambda c1)^2` or `(3/8)(2 c0)^2`, a unit on `D(lambda c1)` or `D(lambda c0)` respectively. Simultaneous vanishing of both functionals forces `c0=c1=0`, which is not exact contact. The dual functionals therefore cover the rank-one chamber without dividing by `Delta_C`.

---

## 7. Finite etale descent and closed `ord(R)>=7`

The map `p=-2 lambda^2` from `D(lambda)` to `D(p)` is finite etale of degree two in characteristic zero (derivative `-4 lambda != 0`). It is surjective onto `D(p)`. Emptiness of `V(Phi1,Phi3,Phi4)` on the cover, on both exact-contact charts, therefore descends to the unsplit chart `D(p*k0)` with exact `ord(C)=7+d`.

`R` is written `sigma^7*(b1_series + t*b0_series)`. Neither `b0` nor `b1` is inverted in any unit ideal or chart. The claim is the closed tail `ord(R)>=7`, not only the exact-order slice.

No equality face is imported: the unique-`AC` interior `a+3s>d` is already satisfied by `s_min=0` at `a=7`, `d in {2,3}`, and the present cells are the load-tie `k6 C ~ AC` at `a=7`, not an `R^3`/`AC` equality. No positive-order leading load is imported: `k0` is inverted (`D(k0)`), while `k60` remains free inside the `a=7` cell, including the locus `k60=0`, which is still emptied by `C^2` at `T`.

---

## 8. Firewall

A confirmed verdict closes only the two named strict cells `a=7`, `d=2,3`, `ord(R)>=7`, after the cited upstream gates on `D(p*k0)`. It does not cover:

- `a=8,9` (load-first: `k6 C` arrives strictly before `AC` once `a>7`);
- grade-32/34 row-4 target-shadow chambers (`mu4` starts at grade 32, after both `T`);
- another D1 face, an equality face, or a positive-order leading `k10`;
- `p=0`, `k0=0`, a terminal/global chart;
- the whole square component, order two, `(8,12)`, maximum twelve, or JC2.

No timing or emptiness claim may be extrapolated to `a=8,9`.

---

## Defect classification

| Class | Item |
|---|---|
| Mathematical defect | none. Smallest failing identity: none. Earliest missing source monomial: none |
| Custody/software defect | none that breaks a numbered claim. The `/tmp` archive was not retrieved; on-host freeze checks and the repository freeze are the custody. `Psi_pm_exact` is computed and not multiplied into the endpoint product; independent valuation `>=G` closes that hole |
| Scope wording defect | none. The theorem statement, preregistration, and RESULT firewall name only the two `a=7` cells on `D(p*k0)`. Charts `D(c1)` and `D(c0)` in RESULT are the exact-contact condition inside that ambient chart, matching the client inversions of `lambda` and `k0` |

CONFIRMED
