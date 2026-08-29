# Hostile review — exceptional D1 `E` opposite-root pole-three obstruction

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_e_a1d3_opposite_root_pole3_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Earliest missing source monomial | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, validator tokens, finite-field agreement, the support-miner navigation verdict, and the producer theorem prose are not authority |
| Method | SHA-256 of every named pin, nested compiled manifest, and evidence file; independent four-summand binomial census through grade 18 with pad 0/1/2; hand reconstruction of the `L^3` numerator, recurrence, both Faber root identities, opposite-root terminals, and unit ideals; compiled-script inspection of every `H` primitive, inverse series, seven-row bridge, moving recurrence, Hensel cover, orientation, `RA^2` correction, and AWS record. No Singular, Sage, msolve, or Lean replay |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the six required primary pins match. Every path named in `FREEZE.sha256` (9 rows), `EVIDENCE.sha256` (36 rows), and `PRODUCER_FREEZE.sha256` (4 rows) rehashes to the printed digest. All three nested `compiled.sha256` files rehash to the retrieved `.sing` and `result.json`. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the registered square/D1 chart `D(p*k0)`, after the frozen unique-first-`AC` gates, the exceptional strict-contact block

```text
ord(A)=1, ord(C)=4, ord(R)>=2
```

has complete seven-row source of global pole order three through grade 18, with exactly eight polar primitives. The unique pole-three family is unloaded `-(1/16) A^3/L^3`, first at grade 18. Every pole-at-most-two family, including the retained `C^2/RA^2` collision, becomes `L`-divisible in the proper `L^3` numerator and vanishes at either moving root of `L=z^2+P/2`.

The first `AC/L` equations allocate the nonzero leading linear forms to opposite roots. In the orientation `A0=au(z-lambda)`, `C0=cv(z+lambda)`, the pole-three numerator at the `C`-root `z=-lambda` is identically zero in grades 15, 16, 17 and equals `+(1/2) au^3 lambda^3` at grade 18. The deck-swapped orientation gives `-(1/2) au^3 lambda^3`. Rows 1, 3, 5, and 6 are target-free through grade 18, so the functional contains no target. After inverting only `lambda`, `au`, `cv`, and `k0`, each terminal generates the unit ideal before radicals. No coefficient of `R` is inverted, so this is the entire closed `ord(R)>=2` tail. The moving-root cover is finite etale over `D(p)`, and emptiness descends.

This closes only the routed block `E` on `D(p*k0)`. It does not decide a neighboring strict cell, an equality or positive-order-load face, another D1 chart, the square component, order two, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Class | Finding |
|---|---|---|
| 1. Six primary pins and named manifests | custody/software | all six match; `FREEZE` 9/9, `EVIDENCE` 36/36, `PRODUCER_FREEZE` 4/4, three nested `compiled.sha256` 2/2 each |
| 1. Exact Q versus finite screens | custody/software | exact Q is the characteristic-zero endpoint; `F_65519` and `F_65521` are independent screens only; stdout byte-identical; `.sing` files equal after the single ring-characteristic token |
| 1. Archive, rc, diagnostics, caps, zero swap | custody/software | on-host freeze OK; engine rc 0; empty compiler stderr; GNU `time -v` only in engine stderr; no `error occurred`, no `=FAIL`; swaps 0; timeout 1800 s / 16,777,216 KiB. The `/tmp` source archive was not retrieved locally |
| 2. Independent polar census through grade 18 | mathematical | **holds**; eight primitives, global pole three, sole pole-three `-(1/16)A^3/L^3` at grade 18; earliest omitted polar monomial: none |
| 3. Seven Faber rows versus analytic emitter | mathematical | **holds**; moving `P`, delayed loads, mechanical jets, recursive quotients, exact `RA^2` second correction; rows 1, 3, 5, 6 target-free through 18 |
| 4. `L^3` numerator and recurrence | mathematical | **holds**; every coefficient and sign independently rederived from `Inv3` |
| 5. Both Faber identities on `p=-2 lambda^2` | mathematical | **holds**; moving-root form of `lambda^2=-P/2`; rows 1, 3, 5, 6 introduce no target |
| 6. First-`AC/L` opposite-root allocation | mathematical | **holds**; two deck orientations exhaust the moving-root cover on `D(p)`; no proportional/equal-root chamber discarded |
| 7. Opposite-root terminals | mathematical | **holds**; pole `<=2` is `L`-divisible in `N3`; `+(1/2) au^3 lambda^3` and deck-swapped `-(1/2) au^3 lambda^3`; grades 15–17 vanish |
| 8. Localized unit ideals, closed `R`, etale descent | mathematical | **holds**; inverted `lambda, au, cv, k0` only; no leading `R`; entire `ord(R)>=2` tail; finite etale over `D(p)` |
| 9. Firewall | scope wording | **holds**; only routed `E` on `D(p*k0)` after the cited gates |

---

## 1. Custody

Recomputed SHA-256 of the six required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `f2b947ddb2b251069666bb8287800127253ca3f118f5fb22587b3b0032bba1f5` | producer report |
| `.../AWS_LAUNCH_METADATA.md` | `00d9e48cb646372b3cd4306c517c4cbd04fae439c963119e3d547f5ae972f826` | AWS metadata |
| `.../EVIDENCE.sha256` | `31050d988c6246a48610847a7e7498bc55922a8ea0c9a4e87a1db7a30808e382` | evidence freeze |
| `.../FREEZE.sha256` | `65f09d0a5b461e5b82e4c776722990d7d5684e6307ba2484af8bd4814349b4cd` | source freeze |
| `.../PRODUCER_FREEZE.sha256` | `65a40079b7b52964a775d01ef651f24ee04dcce05650147ed11327ace5913237` | producer freeze |
| `.../compile_e_pole3.py` | `3678b0072ce5c4ac24681239f00e38bbecc196c4e9bf2f43ef1ab3a04915e1af` | compiler |

`FREEZE.sha256` names 9 files, all matching, including the parent unique-`AC` compiler and producer freeze, that block's hostile review and promotion, `PREREGISTRATION.md`, `run_aws.sh`, `launch_host.sh`, and `ops/aws_exact_lane.sh`. `PRODUCER_FREEZE.sha256` repeats the four producer documents and matches. `EVIDENCE.sha256` names 36 files across the three AWS lanes; all 36 rehash.

Nested `compiled.sha256` on all three lanes rehash. Exact-Q, `F_65519`, and `F_65521` stdout are byte-identical (`0eaede5fda…`). Compiled scripts are characteristic-normalized equal: the only difference is the ring-characteristic token `0` versus `65519` versus `65521` (4-byte size gap 182717 versus 182721). Compiler stderr is the empty digest `e3b0c442…` on every lane.

| | exact Q | `F_65519` screen | `F_65521` screen |
|---|---|---|---|
| host | Box02, `ip-172-30-0-186` | Box03, `ip-172-30-0-249` | r6d, `ip-172-30-0-45` |
| tag | `..._q_box02_20260826T1855Z` | `..._p65519_box03_20260826T1855Z` | `..._p65521_r6d_20260826T1855Z` |
| launcher PID | 303084 | 257871 | 323913 |
| characteristic | 0 | 65519 | 65521 |
| start / engine end UTC | 18:55:16 / 18:58:29 | 18:55:16 / 18:58:16 | 18:55:16 / 18:58:26 |
| timeout / VM cap | 1,800 s / 16,777,216 KiB | same | same |
| engine rc | 0 | 0 | 0 |
| wall / peak RSS | 3:13.26 / 783,392 KiB | 3:00.48 / 618,052 KiB | 3:09.87 / 617,032 KiB |
| swaps | 0 | 0 | 0 |
| compiled SHA-256 | `577dd40a9de6…` | `cb1e9b44e623…` | `d4b8aa28b06d…` |
| stdout SHA-256 | `0eaede5fdaa3…` | same | same |
| compiler stderr | empty | empty | empty |

GNU `time -v` is the only engine-stderr content. No `error occurred`, no `=FAIL`, no Singular `// **` or `? ` diagnostic, no nonzero swap. Distinct hosts, distinct PIDs, same recorded archive hash `d516f23b4800…`. Exact Q is the characteristic-zero endpoint; the two finite fields are software/host screens (`2` and `3` are units there). They are not a characteristic-zero proof.

The `/tmp` source archive `d516f23b…` recorded in `AWS_LAUNCH_METADATA.md` was not retrieved. All three hosts record that same archive hash and a passing on-host `FREEZE` check of the nine named rows. The repository freeze and the 36 evidence files are the custody used here.

A passing sentinel is not mathematics. The algebra below is independent of those sentinels.

---

## 2. Independent polar census through grade 18

The licensed square source is `f=K^2+sigma^5 D` with `K=L^2+sigma^2 R` and `D=L A+C`. Factoring `f=L^4(1+x)` produces four atoms

```text
(fixed, den, R, A, C, scalar) =
  (2, 2, 1, 0, 0, 2),   # 2 sigma^2 R / L^2
  (4, 4, 2, 0, 0, 1),   # sigma^4 R^2 / L^4
  (5, 3, 0, 1, 0, 1),   # sigma^5 A / L^3
  (5, 4, 0, 0, 1, 1).   # sigma^5 C / L^4
```

The four load summands are the binomial series of

```text
f^{3/2},   sigma^4 k10 f^{5/4},   sigma^{12} k6 f^{3/4},   sigma^{20} k2 f^{1/4},
```

i.e. alphas `3/2, 5/4, 3/4, 1/4` with delayed weights `Lambda^{2,6,10}` after `Lambda=sigma^2`. Pole order is `denominator - 4 alpha`. These alphas and weights are the frozen load-ladder generating function, not a miner-only convention. Polar primitives are those with pole `>0`.

On `ord(A)=1`, `ord(C)=4`, `ord(R)>=2` the grade of a multi-index is

```text
summand_fixed + 4 n_{R,type1} + 8 n_{R,type2} + 6 n_A + 9 n_C.
```

Every atom cost is at least 4, so a degree-(bound+2) tuple already exceeds `T=18`. Independent expansion through grade 18, with atom bounds `budget // cost` and with one and two extra counts in every atom direction, produces the same eight nonzero polar signatures:

| grade | summand | fixed | `R` | `A` | `C` | pole | coefficient | `t`-power |
|---:|---|---:|---:|---:|---:|---:|---|---:|
| 15 | unloaded | 10 | 0 | 1 | 1 | 1 | `3/4` | 1 |
| 16 | k10 | 10 | 3 | 0 | 0 | 1 | `5/16` | 0 |
| 16 | k10 | 14 | 0 | 2 | 0 | 1 | `5/32` | 1 |
| 16 | unloaded | 12 | 1 | 2 | 0 | 2 | `-3/8` | 2 |
| 17 | k10 | 11 | 1 | 0 | 1 | 1 | `5/8` | 1 |
| 18 | k10 | 13 | 2 | 1 | 0 | 2 | `-5/32` | 2 |
| 18 | unloaded | 10 | 0 | 0 | 2 | 2 | `3/8` | 3 |
| 18 | unloaded | 15 | 0 | 3 | 0 | 3 | `-1/16` | 4 |

Hand coefficients, not miner output:

- `AC`: `C(3/2,2)*2 = 3/4`. Unique first polar, grade `10+2+3=15`.
- `k10 A^2`: `C(5/4,2)=5/32`.
- `k10 R^3`: three type-1 `R` gives `-5/16`; one type-1 plus one type-2 gives `+5/8`; aggregate `+5/16`.
- `RA^2`: `C(3/2,3)*3*2 = -3/8`.
- `k10 RC`: `C(5/4,2)*2*2 = 5/8`.
- `k10 R^2 A`: two type-1 `R` plus `A` gives `-15/32`; type-2 `R` plus `A` gives `+5/16`; aggregate `-5/32`.
- `C^2`: `C(3/2,2)=3/8`.
- `A^3`: `C(3/2,3)=-1/16`. Sole pole-three family, first grade `15+3=18`.

Four aggregated keys cancel identically (pad-stable zeros, not hidden monomials):

```text
(unloaded, fixed=9, R=2, A=1, pole=1, grade 14)     # type-2 R plus A versus two type-1 R plus A
(unloaded, fixed=8, R=4, pole=2, grade 16)          # four type-1 R versus mixed type-2
(unloaded, fixed=9, R=2, C=1, pole=2, grade 17)
(unloaded, fixed=11, R=3, A=1, pole=3, grade 18)
```

The earliest cancelled key is the grade-14 unloaded `R^2 A`. It is a genuine zero, and in any case sits before the first polar grade 15.

Holomorphic (pole `<=0`) summands exist — the earliest is unloaded type-1 `R` at grade 4 with pole `-4` — and are not polar source. They belong to the regular part of `f^alpha` and are already present in the literal tails; they are not omitted polar monomials.

Load delay: `k6` first polar is type-2 `R` at grade 20 or `C` at grade 21, both after 18 (`k6` plus type-1 `R` has pole `-1`; `k6` plus `A` has pole 0). `k2` first polar is type-1 `R` at grade 24. Neither load contributes a polar family in-window.

Global pole ceiling 3, primitive count 8, sole pole-three family `-(1/16)A^3/L^3` at grade 18. Earliest omitted polar monomial: none. The miner's `local_pole_upper_at_A_root` navigation is not used.

Compiled `H` contains exactly these eight terms, with matching coefficients, `sigma` prefixes, and `t`-powers `1+2q-eR-eA-eC` (all nonnegative, so every primitive is proper). Inverse series are `(1+(P/2)t^2)^{-q}` through `t^8`:

```text
Inv1 = 1 - (P/2) t^2 + (P/2)^2 t^4 - (P/2)^3 t^6 + (P/2)^4 t^8
Inv2 = 1 - 2(P/2) t^2 + 3(P/2)^2 t^4 - 4(P/2)^3 t^6 + 5(P/2)^4 t^8
Inv3 = 1 - 3(P/2) t^2 + 6(P/2)^2 t^4 - 10(P/2)^3 t^6 + 15(P/2)^4 t^8
```

Compiled `H` has four `Inv1`, three `Inv2`, and one `Inv3`, matching the four pole-1, three pole-2, and one pole-3 families. Extra `t^{10}` cannot enter `[t^8]=h7`.

Jet ceilings are `T - first_grade` over primitives carrying that stem: `p:3`, `A:3`, `C:3`, `R:2`, `k10:2`, `k6:0`, `k2:0`, `mu2:0`, `mu4:0`. The compiled ring is exactly those jets plus `mu6,J,lam,rho1..3,au,cv,ilam,icv,iau,ik0`.

---

## 3. Seven literal Faber rows versus the analytic emitter

Literal rows are `tail_text` of frozen `tails.json` with `Lambda -> (sigma^2)` and coefficient substitution from `source_coefficients` for `K=L^2+sigma^2 R`, `D=LA+C`, moving

```text
P = p + 2 sigma ell1 + 2 sigma^2 ell2 + 2 sigma^3 ell3.
```

Delayed loads in every compiled `SourcePhi_j` are the frozen weights `(sigma^2)^2 k10`, `(sigma^2)^6 k6`, `(sigma^2)^10 k2`. Direct inspection finds those three delayed weights in all seven rows and no `(sigma^2)^4`. `k10` carries jets through `k0_2`; `k6` and `k2` are leading only, matching the mechanical ceilings. `SourcePhi` begins with those delayed-load tail monomials, not with a handwritten polar list.

Target subtractions, compiled:

```text
row 1: 0
row 2: sigma^{28} mu20
row 3: 0
row 4: sigma^{32} mu4
row 5: 0
row 6: sigma^{36} mu6
row 7: sigma^{38} (J/4)
```

The analytic-Laurent/literal bridge is coefficientwise `SourcePhi_j - T_{j*}(P) h` modulo `sigma^{19}`, with the frozen connection

```text
Phi1 = h1
Phi2 = h2
Phi3 = h3 + (P/4) h1
Phi4 = h4 + (P/2) h2
Phi5 = h5 + (3P/4) h3 + (3 P^2/32) h1
Phi6 = h6 + P h4 + (P^2/4) h2
Phi7 = h7 + (5P/4) h5 + (15 P^2/32) h3 + (5 P^3/128) h1.
```

Every powered numerator is parenthesized. Compiled `h_j = [t^{j+1}] H` uses divisors `2!,3!,...,8!`. Recursive sigma quotients divide each `FullPhi_j` by `sigma^{15}`, then peel one `sigma` at a time through 18, requiring each remainder to lie in `(sigma)` and the reconstruction `sigma^{15} Q_{15} = FullPhi`. Those are the exactness flags.

If a polar monomial were missing from `H` but present in the tails, the bridge would fail. If a jet ceiling were too small, the tails (which substitute the same truncated series) could agree with `H` while both were incomplete; pad+2 plus strictly positive atom costs close that cut. No in-window polar monomial is missing from compiled `H`.

Isolated `H_RA2 = -(3/8) sigma^{12} t^2 R A^2 Inv2`. After the plus allocation `a1=au`, `a0=-au lam` and evaluation of the `L^2` numerator at the moving `A`-root,

```text
A(root) = sigma^2 (lam a1_1 + a0_1 + au rho1) + O(sigma^3),
R(root) = sigma^2 (b1 lam + b0) + O(sigma^3).
```

The naive grade-16 term is leading `R A0^2` and vanishes at the `A`-root. Grade 17 has odd extra order and vanishes. Grade 18 is

```text
-(3/8)(b1 lambda + b0)(lambda a1_1 + a0_1 + au rho1)^2
```

modulo the Hensel ideal. Compiled `RA2ExpectedRed` is this polynomial. This reconstructs the second correction of `-(3/8) R A^2/L^2`. The family is retained in `H`; it is not deleted and not assumed to cancel with `C^2`.

Rows 1, 3, 5 have target `0` identically. Row 6 subtracts `sigma^{36} mu6`. Through grade 18, `FullPhi_j = SourcePhi_j` on rows 1, 3, 5, 6. The first target term among these four rows is `sigma^{36} mu6` in row 6, which is outside the window. Compiled `E_targetfree` is exactly those four differences modulo `sigma^{19}`.

The inherited parent print `PASS_ROUTE_DEDICATED_E_SUCCESSOR_NO_EMPTY_VERDICT` is the `L^2` negative-control refusal inside `block()`. It does not decide emptiness. The successor then runs the `L^3` opposite-root argument. Those two strings are sequential, not contradictory.

---

## 4. `L^3` proper-numerator reconstruction and recurrence

Write `H_analytic = N3/L^3` with `L=z^2+P/2` and `deg N3 <= 5`,

```text
N3 = n5 z^5 + n4 z^4 + n3 z^3 + n2 z^2 + n1 z + n0.
```

The extra-`t` packing used by the emitter is

```text
H_t = t^2 * (n5 + n4 t + n3 t^2 + n2 t^3 + n1 t^4 + n0 t^5) * Inv3,
```

with `h_j = [t^{j+1}] H_t`, so `h_j = [t^{j-1}](E * Inv3)`. The expansion

```text
Inv3 = 1 - (3P/2) t^2 + (3 P^2/2) t^4 - (5 P^3/4) t^6 + ...
```

inverts to

```text
n5 = h1,
n4 = h2,
n3 = h3 + (3P/2) h1,
n2 = h4 + (3P/2) h2,
n1 = h5 + (3P/2) h3 + (3 P^2/4) h1,
n0 = h6 + (3P/2) h4 + (3 P^2/4) h2.
```

This is the displayed reconstruction, coefficient by coefficient, including every sign. Mixed pole-`q<=3` generating functions are compatible with this formula because `encoding(L^{3-q}) * Inv3 = Inv_q`.

The next coefficient with `n_{-1}=0` is

```text
h7 = (-3P/2) n1 + (3 P^2/2) n3 + (-5 P^3/4) n5.
```

Substituting the inverted `n_i` yields the identity

```text
h7 + (3P/2) h5 + (3 P^2/4) h3 + (P^3/8) h1 = 0
```

as a polynomial in the `n_i` and `P` (the `n1`, `n3`, and `n5` coefficients each cancel). This is the pole-three certification: `L^3 H` is a polynomial of degree at most five. Compiled `E_Rec7` is this combination, reduced modulo `sigma^{19}`.

---

## 5. Faber identities on `p=-2 lambda^2`

On the cover, `lambda^2 = -P/2`, so

```text
lambda^2 = -P/2,   lambda^3 = -(P/2) lambda,   lambda^4 = P^2/4,   lambda^5 = (P^2/4) lambda.
```

Substitute into `N3(+lambda)` and split even/odd parts. The even part collapses to

```text
h6 + P h4 + (P^2/4) h2 = Phi6.
```

The coefficient of `lambda` collapses to

```text
h5 + P h3 + (P^2/4) h1.
```

The frozen connection gives

```text
Phi5 + (P/4) Phi3 + (3 P^2/32) Phi1
  = h5 + (3P/4) h3 + (3 P^2/32) h1
    + (P/4) h3 + (P^2/16) h1
    + (3 P^2/32) h1
  = h5 + P h3 + (8/32) P^2 h1
  = h5 + P h3 + (P^2/4) h1.
```

Hence

```text
N3(+lambda) = Phi6 + lambda (Phi5 + (P/4) Phi3 + (3 P^2/32) Phi1),
N3(-lambda) = Phi6 - lambda (Phi5 + (P/4) Phi3 + (3 P^2/32) Phi1).
```

This is an identity of power series whenever `lambda^2 + P/2 = 0`, not a grade-by-grade approximation. Compiled `Psi` uses moving `lambda(sigma)=lam+sigma rho1+sigma^2 rho2+sigma^3 rho3` and moving `P`. The constant Hensel coefficient is `lam^2+p/2`, imposed by `subst(p,-2*lam^2)`. Higher coefficients `2 lam rho1 + ell1`, `rho1^2 + 2 lam rho2 + ell2`, … do not contain `p` and generate `RootIdeal` together with `ilam*lam-1`. Both evaluations substitute `z = ± lambda(sigma)` and reduce by that ideal.

The identity uses only rows 1, 3, 5, 6. Those rows are target-free through grade 18, so replacing `SourcePhi` by `FullPhi` introduces no target. Rows 2, 4, 7 are absent from the functional.

---

## 6. First-`AC/L` allocation, scheme-theoretically

At grade `G=15` the unique polar primitive is unloaded `AC` with coefficient `3/4`. The grade-15 numerator is the remainder of `(3/4) A0 C0` modulo `L=z^2+p/2`:

```text
Nfirst = (3/4) ((a1 c0 + a0 c1) z + a0 c0 - (p/2) a1 c1).
```

Compiled `NfirstExpected` is this polynomial, compared at the extracted grade-15 coefficients (moving `ell` first appears at grade 16, so `p` versus `P` is correct here). Thus `Nfirst=0` if and only if `L` divides `A0 C0`.

On `D(p)`, the discriminant of `L` is a unit times `p`, so `L` is squarefree with two distinct roots on the cover `lambda^2=-p/2`. Exact `ord(A)=1` forbids `A0=0`; exact `ord(C)=4` forbids `C0=0`. A nonzero constant cannot be a complementary factor of a quadratic, so both forms have degree exactly one. A degree-`<=2` polynomial divisible by a squarefree quadratic is a unit times `L`, so the two linear forms vanish at complementary roots.

They cannot share a root: that would square `L` and force `p=0`, which is off `D(p)`. If `A0` were proportional to `C0` they would vanish at the same point, again the equal-root chamber, excluded by `D(p)` rather than silently dropped. The remaining possibilities are exactly the two deck orientations

```text
plus:  A0 = au (z - lambda),  C0 = cv (z + lambda),
minus: A0 = au (z + lambda),  C0 = cv (z - lambda).
```

These exhaust the moving-root cover. The `S_2` action swapping the two roots of `L` swaps the two maps. Compiled substitutions are

```text
OriMinus: a1=au, a0=-au lam, c1=cv, c0= cv lam,   evaluate at z = -lambda,
OriPlus:  a1=au, a0= au lam, c1=cv, c0=-cv lam,   evaluate at z = +lambda,
```

which are evaluation at the `C`-allocated root in each orientation.

---

## 7. Opposite-root evaluation

For a pole-`q<=2` family, `H = N_q / L^q = (N_q L^{3-q}) / L^3` with `3-q >= 1`. Its contribution to `N3` is divisible by `L`, hence vanishes at either moving root after reduction by `RootIdeal`. This is linear in families and includes jets. In particular the full `C^2/RA^2` collision, including the retained grade-18 `RA^2` second correction, is `L`-divisible in `N3` and vanishes at the `C`-root. (At the `A`-root that collision does not vanish, which is why the parent `L^2` endpoint is correctly refused.)

The only surviving contribution is pole three. Through grade 18 the unique pole-three family is leading `A^3`. Higher `A` jets first meet grade 19. In the orientation `A0=au(z-lambda)`,

```text
A0(-lambda) = au(-lambda - lambda) = -2 au lambda,
-(1/16) A0(-lambda)^3 = -(1/16) (-8) au^3 lambda^3 = +(1/2) au^3 lambda^3.
```

Deck-swapped, `A0(+lambda)=2 au lambda` and `-(1/16)(8 au^3 lambda^3)=-(1/2) au^3 lambda^3`.

Grades 15, 16, 17 contain only pole-`<=2` primitives, so those coefficients of `N3` vanish at either root as polynomials. Grade 18 is exactly the displayed leading `A^3` value. Characteristic zero supplies the `2` in `1/2`. Compiled terminals compare

```text
OriMinus_g15 = OriMinus_g16 = OriMinus_g17 = 0,
OriMinus_g18 - (1/2) au^3 lam^3 = 0,
```

and the opposite signs on the plus deck.

---

## 8. Localized unit ideals, closed `R`, descent

Compiled unit ideals, before radicals:

```text
std(ideal(OriMinus_g18, ilam*lam-1, iau*au-1, icv*cv-1, ik0*k0-1)),
std(ideal(OriPlus_g18,  ilam*lam-1, iau*au-1, icv*cv-1, ik0*k0-1)).
```

`OriMinus_g18 = (1/2) au^3 lam^3` and `OriPlus_g18 = -(1/2) au^3 lam^3`. After inverting `lam` and `au`, these are units in characteristic zero (`2` is a unit). Hence `1` lies in each ideal. Inverted coefficients are exactly the exact-contact leading forms `au,cv`, the root `lambda`, and the D1 chart unit `k0`. The extra inverse of `cv` is legitimate on the exact `ord(C)=4` chart; it is not required by the terminal and does not weaken the unit claim.

Not inverted: leading `b0,b1` of `R`, the Hensel corrections `rho, ell`, delayed `k6,k2`, and every target. The compiled source writes `R=sigma^2 (b1 + t b0 + jets)` and does not invert `b0,b1`. Raising `ord(R)` delays every `R`-family and cannot create an earlier pole-three term: the obstruction `±(1/2) au^3 lambda^3` is independent of `R`. The compiled floor is the entire closed tail `ord(R)>=2`, not only the exact-order slice.

The cover `lambda^2 + p/2 = 0` is finite etale of degree two on `D(p)`: the discriminant is a unit times `p`, and `2` is a unit in characteristic zero. Emptiness on both sheets therefore descends to the unsplit exact-contact chart on `D(p*k0)`. This is emptiness of that localized `T=18` jet/formal chart. The lowest term of the functional is a unit, so there is no formal arc.

---

## 9. Firewall

A confirmed verdict closes only the routed block `E` after the cited unique-first-`AC` and square/D1 gates, on `D(p*k0)`. Independently:

- The eleven other `a<=6` unique-`AC` `d=2,3` tails are the parent producer, already hostile-review confirmed empty; they are gates, not this claim.
- Equality faces (`a+3s=d`) and positive-order leading load (`a>=7` for `k6 C`) are off the unique-`AC` interior.
- `p=0` and `k0=0` are off the chart.
- Another D1 face, a terminal/global chart, the square component, order two, `(8,12)`, maximum twelve, and JC2 are not this claim.

Compiled scope is `A1_C4_R_GE_2_D1_ON_D_P_K0_ONLY`. Nothing here may be imported through a neighboring cell or to JC2.

---

## Issues

No mathematical identity failed. No polar source monomial is missing through grade 18. The only custody reservation is that the `/tmp` launch archive was not retrieved locally; the on-host freeze of the nine named rows and the 36 retrieved evidence files are the bytes used. Finite-field agreement is not a characteristic-zero proof and was not treated as one. Producer PASS strings, validator tokens, and the support-miner navigation verdict were not used as mathematics.

Smallest failing identity: none.

Earliest missing source monomial: none.

CONFIRMED
