# Hostile review — D1 `a>=10` grade-38 order-three source obstruction

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_age10_j38_odd_recurrence3_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing source monomial | none through grade 38; first polar family outside the window is `k6*R*A/L^2` at grade 39 (still pole 2); first pole-order-four family is `k6*A*C/L^4` at grade 43 |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, validator strings, and finite-field agreement are not authority |
| Method | SHA-256 of every named pin; independent binomial expansion of `f^alpha` at `A=10,C=11,R=10` with product range larger than the compiler's; generating-function derivation of `(R3)`; frozen seven-row Faber tails plus D1 substitutions; compiled-script inspection. No Singular re-execution, Sage, msolve, Lean, or package compiler |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the six required primary pins match. Every path named in `FREEZE.sha256` (13/13) and `EVIDENCE.sha256` (30/30) rehashes to the printed digest, as does `PRODUCER_FREEZE.sha256` (4/4). Nested `compiled.sha256` on both lanes rehashes (3/3 each). Parent `a>=13` freeze 8/8 and evidence 35/35, high-contact freeze 9/9, and V3 parenthesized-load freeze 7/7 rehash. Frozen `tails.json` is `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`; canonical all-tails digest is `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`. Exact Q is the theorem endpoint; `F_65521` is a separate compiled input and a separate engine transcript. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the registered D1 high-contact chart `D(J)`, after the cited square/D1 gates, write

```text
A = sigma^10 theta Abar,   C = sigma^11 theta Cbar,
R = sigma^10 theta eta Rbar,
```

with independent jets of the moving connection `p(sigma)`, of `A,C,R`, of the parenthesized loads `k10,k6,k2`, and of the sparse targets `mu2,mu4,mu6,J/4`. Through absolute grade 38 every source term that enters the seven first-normal rows has pole denominator at most `L^3`. The four odd Faber rows of any such source satisfy the formal identity

```text
Phi7 + (p(sigma)/4) Phi5 + (3 p(sigma)^2/32) Phi3
     + (5 p(sigma)^3/128) Phi1  =  0   mod sigma^39.
```

The only odd-row target is `-sigma^38*(J/4)` in row seven, so the same combination of the full rows is `-sigma^38 J/4` modulo `sigma^39`. Vanishing of the seven source equations therefore forces `J=0`. Adjoining `iJ*J-1` yields the unit ideal before radicals, which is emptiness on the named chart `D(J)`.

The identity is polynomial in the independent variables `theta,eta`. Substituting `theta=sigma^n`, `eta=sigma^s` covers every integer contact `a=10+n`, `c=a+1`, `r=a+s`. After a common ramification the same homogeneous substitution covers every rationally valued arc with `a>=10` and `r>=a`; extra nonnegative powers of the uniformizer only delay walls. Neither `theta` nor `eta` is inverted.

The separately reviewed `a>=13` order-two theorem, and its `a=12` negative control, are untouched. They use a different annihilator (pole order at most two) and are not this claim. The superseded incomplete draft which inherited the `a>=13` handwritten jets `A_3,k10_1` produced no endpoint and has no verdict.

The Chebyshev/Pell identity is a nonempty engine heartbeat and is not an input to the D1 statement. No claim is made about `a<=9`, `V(J)`, other D1 cells, excluded lifecycle charts, the whole square component, order two, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Six primary pins | hashes | all six match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 13/13, `EVIDENCE` 30/30, `PRODUCER_FREEZE` 4/4, both nested `compiled.sha256` 3/3 |
| 0. Ancestry | `a>=13`, high-contact, V3, tails | parent freeze 8/8 and evidence 35/35, high-contact 9/9, V3 7/7, tails `d72f774c…`, canonical `6eed03d4…` |
| 1. Exact Q vs `F_65521` | separate hosts, scripts, transcripts; rc, diagnostics, swap | **holds**; exact Q is characteristic 0; `F_65521` is a software control |
| 2. Four binomial summands | eleven polar families at `A=10,C=11,R=10`; coefficients, grades, poles; product range; first pole four at 43 | **holds**; `product(range(4))` already exhausts grade `<=38`; first omitted polar family is `k6*R*A/L^2` at 39 |
| 3. Derived jet ceilings | `A_7,C_10,R_6,k10_6,k6_10,k2_6,p_10`; `A_7` and `k10_6` at grade 38; no omitted earlier polar source | **holds**; holomorphic `pole<=0` families do not enter the seven polar rows |
| 4. Seven-row reconstruction | frozen Faber, parenthesized `k10,k6,k2`, moving `p(sigma)`, jets, sparse targets | **holds**; 36,54,58,81,89,120,131 monomials; V3 counts 190/72/27; Laurent emitter is independent of the octic tails |
| 5. Laurent-to-Faber `(R3)` | signs, moving `p(sigma)`, `mod sigma^39` | **holds**; combination equals `(S+p/2)^3 h1`; coefficients are those of `(1-s x)^{-1/2}` |
| 6. Full-row combination | exactly `-sigma^38 J/4`; even targets cannot enter; `iJ*J-1` is the unit ideal | **holds** |
| 7. Homogeneous coverage | `theta=sigma^n`, `eta=sigma^s`; ramification; no hidden inversion; exact orders vs closed faces | **holds**; `theta,eta` are free polynomial variables |
| 8. Firewall and `a>=13` | order-two theorem and `a=12` control preserved; incomplete `A_3,k10_1` draft has no verdict; scoped cone only | **holds** |

---

## 0. Custody

Recomputed SHA-256 of the six required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `2ccfdfe9c3deb4d32594d2f5e1237684023d5b75438a02229776436c38456883` | producer report |
| `.../EVIDENCE.sha256` | `25793913c683a2b6ae914a4ab9b0450cb61c82a8c17b92325ca5292a8183cdef` | evidence freeze |
| `.../FREEZE.sha256` | `d5bf43b80b0565b06407b85e6e333381a4015cccbd80a90e6c819fe33a02fa03` | source freeze |
| `.../AWS_LAUNCH_METADATA.md` | `9720c604276f5f293a3ad91d67beff049c1948f6e4f686ab34335d47262220fc` | launch metadata |
| `.../PRODUCER_FREEZE.sha256` | `60b2e1d52156f0648f7f39739f06c139d7d274c28fe4147eaba8d7213dfc2f0b` | producer freeze |
| `.../compile_age10_j38_r3.py` | `9f0184b1007103478381c474ce6e4c1802ed8a53ab23dee79e7dd77518e0168e` | AWS compiler |

`FREEZE.sha256` names thirteen files, all matching, including the frozen `a>=13` compiler/result/evidence, the high-contact parent, `run_aws.sh`, `launch_host.sh`, and `ops/aws_exact_lane.sh`. `EVIDENCE.sha256` names thirty files; all thirty rehash. Nested `compiled.sha256` files rehash to the retrieved `.sing`, `result.json`, and `source_inventory.json` on each lane. The two inventories are byte-identical at

```text
884922fede59bc3540a61aa089a9ed92f65235b269330d63b9195afa69019297.
```

Exact Q and `F_65521` are genuinely separate frozen runs.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `…_q_20260826_box03` | `…_p65521_20260826_r6d` |
| PID | `239036` | `297985` |
| Characteristic | `0` in the unique ring | `65521` in the unique ring |
| Compiled script SHA | `be7c670117bfce6ca30e0d915ee3073e742c9b8efe124f688d15812b8feb667f` | `894909e6fffdca6909ae3e7faf1fda6f0a424c3a99f91c57a3ce40831130c431` |
| Compiler `rc` | `0` | `0` |
| Engine `rc` | `0` | `0` |
| Compiler stderr | empty-file digest `e3b0c442…` | same |
| Stdout SHA | `bb43b3b4a61fd862d77962868e6b272421ca92e992e014eb0eb3cc0e4ce5b0cf` | same boolean transcript |
| Engine stderr SHA | `9280daf598a22be042766e8e5e2f169a803f09a080e7089da47c0c0df7622860` | `fddc6b28ca9024cac99114c10f3b74ce428915f1e87956b39d956ea46b454ad8` |
| Peak RSS / swaps | 46,066,168 KiB / 0 | 41,890,432 KiB / 0 |
| Wall | 13:08.35 | 10:17.05 |
| VM cap | 67,108,864 KiB | 67,108,864 KiB |

Meta `argv` on each host is `timeout 7200 Singular -q` of the frozen compiled input whose SHA is in `result.json` and `compiled.sha256`. Compiler caps were 3600 s compile, 7200 s engine, 64 GiB virtual. Engine stderr is GNU `time -v` only: no `?`, `error occurred`, or `=FAIL`. Each required stdout marker occurs exactly once (18 nonempty lines, all unique). Freeze-check transcripts are byte-identical and list every `FREEZE.sha256` row as `OK`.

The two compiled scripts are byte-identical after replacing the single ring-characteristic token `ring R=0,` versus `ring R=65521,`. Size gap 4 bytes equals `65521` versus `0` once. Substitutions, parenthesized loads, recurrences, unit test, and Pell block are otherwise identical. `65521` does not divide `2`, so no displayed denominator is killed in the software control; that control is still not a coefficient proof. Stdout hashes coincide because both engines print only the boolean/census sentinels; that agreement is not used below. The validator string is not a mathematical verdict.

A passing manifest is not a theorem. What follows is the source.

---

## 1. Distinct frozen executions

Launch registration, PIDs, hosts, ring characteristics, compiled-input SHAs, RSS, wall-clock, and engine-stderr SHAs all differ. The only shared bytes that should be shared are the inventory, the boolean stdout, empty compiler stderr, and the freeze-check transcript. Characteristic `0` on Box03 is the endpoint. Characteristic `65521` on r6d is a second compiled script and a second engine. It is not a substitute for exact Q.

---

## 2. Independent expansion of the four binomial summands

The frozen square octic is `f=K^2+sigma^5 D` with `K=L^2+sigma^2 R`, `D=LA+C`, and `L=z^2+p(sigma)/2`. This is the substitution encoded by `source_coefficients` in the frozen `r1_d1_ac` parent, and it expands as `f=L^4(1+X)` with

```text
X = 2 sigma^2 R/L^2 + sigma^4 R^2/L^4 + sigma^5 A/L^3 + sigma^5 C/L^4.
```

The seven Faber rows are the weight-`12+ell` polar parts of the inverse-Faber source

```text
f^{3/2} + sigma^4 k10 f^{5/4} + sigma^{12} k6 f^{3/4} + sigma^{20} k2 f^{1/4}.
```

Those four exponents are forced by weighted homogeneity (`wt(f)=8`, loads of weights `2,6,10`). They are not taken from a handwritten wall list. Write `f^alpha=L^{4 alpha}(1+X)^alpha`. A multi-index of the four atoms with total `X`-degree `n>=1` contributes pole order `denom-4 alpha` and baseline grade

```text
summand.fixed + 12 n_R + 24 n_{R^2} + 15 n_A + 16 n_C
```

at `A=10,C=11,R=10`. Independently expanding with each atom count in `0..7` (strictly larger than the compiler's `range(6)`) and retaining `pole>0`, `grade<=38`, produces exactly eleven families after like terms are collected. The compiler's `range(6)` is not a hidden truncation: four copies of the cheapest atom already cost grade `48>38`, and `range(4)` versus `range(8)` yields the same eleven signatures.

| first grade | family | coefficient | pole | derivation |
|---:|---|---:|---:|---|
| 28 | `k6 C/L` | `3/4` | 1 | `C(3/4,1)=3/4` |
| 31 | `A C/L` | `3/4` | 1 | `C(3/2,2)*2=3/4` |
| 32 | `k10 R C/L` | `5/8` | 1 | `C(5/4,2)*2*2=5/8` |
| 32 | `k2 R/L` | `1/2` | 1 | `C(1/4,1)*2=1/2` |
| 32 | `C^2/L^2` | `3/8` | 2 | `C(3/2,2)=3/8` |
| 34 | `k10 A^2/L` | `5/32` | 1 | `C(5/4,2)=5/32` |
| 35 | `k10 A C/L^2` | `5/16` | 2 | `C(5/4,2)*2=5/16` |
| 35 | `k2 A/L^2` | `1/4` | 2 | `C(1/4,1)=1/4` |
| 36 | `k10 C^2/L^3` | `5/32` | 3 | `C(5/4,2)=5/32` |
| 36 | `k2 C/L^3` | `1/4` | 3 | `C(1/4,1)=1/4` |
| 36 | `k6 R^2/L` | `3/8` | 1 | `C(3/4,1)` from the `R^2` atom plus `C(3/4,2)*4=-3/8` from two `R` atoms |

The displayed table in RESULT matches this expansion, including the aggregated `k6 R^2` coefficient `3/8`. The parent high-contact C2 block independently carries the unloaded `C^2` leading coefficient `(3/8)c1^2`, so that one displayed constant is not an isolated interpolation.

No polar family with `grade<=38` is omitted. The next polar family is

```text
k6 * R * A / L^2    at grade 12+12+15=39, pole 2.
```

It is outside the window and still of pole order two, so it would remain in the kernel of `(R3)` if the ceiling were raised by one. The first family of pole order four is

```text
k6 * A * C / L^4    at grade 12+15+16=43, coefficient C(3/4,2)*2=-3/16.
```

The next pole-four walls are `k6 C^2/L^5` and unloaded `R C^2/L^4` at grade 44. Increasing `a` or `r` adds a nonnegative power of `sigma` to every listed monomial, so no omitted wall can move earlier.

The holomorphic (`pole<=0`) companions at this baseline begin at grade 12 (`unloaded R`, pole `-4`) and include `k6 A` at grade 27 (pole `0`) and `k10 C` at grade 20 (pole `-1`). They are `z`-holomorphic powers of `L` and do not enter `[F]_-`. They are therefore correctly absent from the eleven polar families. They are not missing source monomials of the seven rows.

---

## 3. Derived jet ceilings

Jet maxima are the leftover grades `38 - first_arrival` on polar families that actually carry the stem:

```text
k6 C at 28  =>  C_10, k6_10, p_10
AC  at 31  =>  A_7
k10 R C at 32  =>  k10_6, R_6
k2 R at 32  =>  k2_6
```

and no later family demands more. This is exactly

```text
A_7, C_10, R_6, k10_6, k6_10, k2_6, p_10,
mu2_10, mu4_6, mu6_2.
```

The `a>=13` handwritten formulae `a_index=38-(25+a)` and `k10` through `k0_1` would have given `A_3,k10_1` at baseline `a=10`. Those are the jets of `k2 A/L^2` and of the `a=13` arrival of `k10 R C`, and they miss the earlier `a=10` walls `AC/L` (needs `A_7`) and `k10 R C/L` (needs `k10_6`). That is the superseded incomplete draft. The mechanical polar remainder repairs it.

`A_7` enters at grade 38 through the unloaded family `(3/4) A C/L` at 31. `k10_6` enters at grade 38 through `(5/8) k10 R C/L` at 32. Both appear in the literal inventory at grade 38 with those leading coefficients, and the reconstructed `SourcePhi` rows contain the full parenthesized series through `a1_7` and `k0_6`.

If holomorphic families were wrongly included in the jet census one would demand `A_23,R_26,k10_22,p_26`. Those extra jets do not enter `[F]_-`. A polar row is linear in each primitive, so a holomorphic `L^{>=0}` term cannot cancel a polar `L^{-q}` term or force a higher polar jet. Moving-`p` jets on a polar family are already bounded by that family's remainder: the earliest polar wall is grade 28, so `p_10` covers every `ell` insertion through grade 38, including the Faber factors `p^n` with `n<=3`. Inverse-series degree `k<=4` in `t^{2k}` is enough for `t`-degrees `2..8` (rows 1 through 7). No earlier polynomial or moving-`p` polar source was found that would require a higher jet on either side of the bridge.

---

## 4. Seven literal rows from frozen tails, and independence of the emitter

The compiler does not emit an eight-term Laurent polynomial as source. It walks the frozen high-contact parent to V3 parenthesized loads to V2 to V1 to `compile_r1_d1_ac.py` to `compile_cge3_universal.py` to `compile_square_load_ladder.py` and `tails.json`. Before any `.sing` is written it rechecks every imported pin and the canonical all-tails digest. Each ordinary coordinate is

```text
tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
```

with target subtractions `-sigma^{2(12+row)}*(mu20-jet | mu4-jet | mu6-jet | J/4)` on rows 2, 4, 6, 7. `tail_text` refuses a monomial whose length is not the frozen name list, whose load exponents are not in `{0,1}` with at most one load, or whose weighted degree is not `12+row`. Load weights in `Lambda` units are `k10:2`, `k6:6`, `k2:10`.

Frozen Faber `tails.json` has seven rows with 36, 54, 58, 81, 89, 120, 131 monomials. Load monomials total `k10` 190, `k6` 72, `k2` 27, matching the V3 distributivity census. The compiled exact-Q rows contain those parenthesized jets at exactly those cardinalities, doubled by the `SourcePhi`/`FullPhi` pair, plus one copy per polar primitive in the Laurent emitter:

```text
(k0+sigma^1*k0_1+...+sigma^6*k0_6)                 190 per seven-row copy, 384 in the script
(k60+sigma^1*k60_1+...+sigma^{10}*k60_10)          72 per copy, 146 in the script
(k20+sigma^1*k20_1+...+sigma^6*k20_6)              27 per copy, 57 in the script
```

with no unparenthesized `k0+sigma`, `k60+sigma`, or `k20+sigma` remnant.

D1 substitutions are the dictionary of `K=L^2+sigma^2 R` and `D=LA+C`:

```text
pp = p + 2 sigma ell1 + ... + 2 sigma^{10} ell10
kc = sigma^2 rz,     kr = pp^2/4 + sigma^2 rc
n3 = sigma^3 az,     n2 = sigma^3 ac
n1 = sigma^3 ((pp az)/2 + cz),   n0 = sigma^3 ((pp ac)/2 + cc)
a6=2 pp, a5=2 kc, a4=pp^2+2 kr, a3=2 pp kc + sigma^2 n3,
a2=kc^2+2 pp kr+sigma^2 n2, a1=2 kc kr+sigma^2 n1, a0=kr^2+sigma^2 n0.
```

The compiled rows substitute

```text
az,ac = sigma^{10} theta (a1-jet through a1_7, a0-jet through a0_7),
cz,cc = sigma^{11} theta (c1-jet through c1_10, c0-jet through c0_10),
rz,rc = sigma^{10} theta eta (b1-jet through b1_6, b0-jet through b0_6).
```

Sparse targets occur once each, only on the licensed full rows:

```text
row 2: -sigma^28*(mu20+...+sigma^{10} mu20_10)     (11 mu20 tokens, only in FullPhi2)
row 4: -sigma^32*(mu4+...+sigma^6 mu4_6)           (7 mu4 tokens, only in FullPhi4)
row 6: -sigma^36*(mu6+sigma mu6_1+sigma^2 mu6_2)   (3 mu6 tokens, only in FullPhi6)
row 7: -sigma^38*(J/4)                             (only in FullPhi7; length delta 17)
```

Odd compiled `SourcePhi` contain no `mu20`, `mu4`, `mu6`, or `J`. `FullPhi1,3,5` are byte-identical to the corresponding `SourcePhi`. `J` is absent from the frozen tails. Byte lengths of `FullPhi7` and `SourcePhi7` differ by exactly the wrapping of `-sigma^38*(J/4)`.

The independent Laurent emitter is the polar binomial `H` built from the eleven families, times `(1+(p/2) t^2)^{-pole}`, from which `h_n=[t^{n+1}]H` and `Phi=T h`. It does not import `tails.json` and does not walk `a0..a6` monomials. A polar family present in the octic tails but omitted from the eleven primitives would appear in `SourcePhi` and not in `PredPhi`, and the seven-row bridge would fail. A shared omission that is absent from the octic tails themselves would not be caught; that would be an omission in the frozen square source, which is a separately reviewed parent and is not this claim. The emitter is therefore independent enough to detect a source omission of this producer. It is not a second copy of the same handwritten wall list: the primitives are enumerated from `(1+X)^alpha`, while the tails are the complete weight-`12+ell` polar monomials of a generic octic.

The inverse-series truncation `k=0..4` and the `t`-degree window `2..8` match rows 1 through 7 and do not drop a polar contribution inside the window. Inverse degree 4 in `t^{8}` already overshoots `h_7` for every family with `base_t>=2`.

---

## 5. Laurent-to-Faber relation `(R3)`, derived

Put `s=p/2`, `Y(x)=sum h_{2m+1} x^m`, and `Phi(x)=sum Phi_{2m+1} x^m`. The frozen Faber matrix is the generating function

```text
Phi(x)=(1-s x)^{-1/2} Y(x/(1-s x)),
```

equivalently the lower-unitriangular block with even gap `i-j=2n`

```text
T_{ij} = ((j/2)_n / n! / 2^n) p^n.
```

Explicitly

```text
Phi1 = h1
Phi3 = h3 + (p/4) h1
Phi5 = h5 + (3p/4) h3 + (3p^2/32) h1
Phi7 = h7 + (5p/4) h5 + (15p^2/32) h3 + (5p^3/128) h1.
```

A pole-`q` source has odd generating function in the proper-polar basis `x^e/(1+s x)^q` with `0<=e<q`. Then

```text
Y(x/(1-s x)) = x^e (1-s x)^{q-e},
Phi(x)       = x^e (1-s x)^{q-e-1/2}.
```

For `q<=3` the product `(1-s x)^{-1/2} Phi(x)` equals `x^e (1-s x)^{q-e-1}`, a polynomial of degree `q-1<=2`. Its coefficient of `x^3` therefore vanishes. The Taylor expansion

```text
(1-s x)^{-1/2} = 1 + (p/4) x + (3 p^2/32) x^2 + (5 p^3/128) x^3 + ...
```

is the binomial series of `(1-u)^{-1/2}` at `u=s x=(p/2)x`. The `x^3` coefficient of the product is exactly

```text
Phi7 + (p/4) Phi5 + (3 p^2/32) Phi3 + (5 p^3/128) Phi1.
```

All four signs are positive. This is not the order-two annihilator, and it is not an interpolation from the `a>=13` calculation. The opposite signs and the coefficients `1,-p/4,-p^2/32,-p^3/128` annihilate pole order at most two; they are a different identity and are not used here.

In the `h`-basis the same combination is

```text
h7 + (3p/2) h5 + (3 p^2/4) h3 + (p^3/8) h1
  = (S + p/2)^3 h1,
```

where `S` shifts odd index by two. That is the order-three recurrence of a proper polar source of order `<=3`. It is not the zero functional on arbitrary `h`.

The compiled rows use one and the same series `pp` as `a6=2 pp` in the octic coefficients, as the Faber factors `pp^n` in the emitter, and as the combination coefficients. Substituting the moving series `p(sigma)` is the same matrix identity in the formal-power-series ring. Reduction modulo `sigma^39` is the truncation of that identity through grade 38; the `p`-jets through `ell_10` are exactly the remainder of the earliest polar wall, so no `p`-tail beyond the window is silently set to zero inside the combination.

---

## 6. Full-row combination, even targets, unit ideal

Even-indexed `h` never enter the odd `Phi`, so the even targets `-sigma^{28} mu2`, `-sigma^{32} mu4`, `-sigma^{36} mu6` cannot appear in a combination of `Phi1,Phi3,Phi5,Phi7`. Direct inspection of the compiled combination confirms it names only those four odd rows. The only target that can appear is the row-seven charge `-sigma^{38}*(J/4)`. Therefore the full-row combination equals the source-only combination plus `-sigma^{38} J/4`. Through grade 38 the source-only combination is `0` modulo `sigma^{39}`, and the full combination is

```text
-sigma^{38} J/4   mod sigma^{39}.
```

If every source row vanishes, this forces `J=0`. Adjoin `iJ*J-1`. The grade-38 coefficient is `-J/4`, and `(-4 iJ)*(-J/4)=iJ J=1`, so `1` lies in the ideal before any radical. `J` is the constant Jacobian of the Keller pair, inserted only as that target; it is not a discardable normal coefficient of the source. The statement is empty on `D(J)` and claims nothing on `V(J)`.

---

## 7. Homogeneous coverage

The identity is a polynomial relation in the free variables `theta,eta` together with the jets of `Abar,Cbar,Rbar`. The compiled substitutions multiply by `theta` and `eta`; they never invert them, and the compiled script contains no `1/theta`, `theta^-`, `1/eta`, or `eta^-`. Substituting `theta=sigma^n` and `eta=sigma^s` with integers `n,s>=0` realises every integer contact `a=10+n`, `c=a+1`, `r=a+s`. If the leading coefficient of `Abar` (resp. `theta`) vanishes, the actual order is strictly larger than 10 (resp. than `10+n`), which remains inside the cone `a>=10`. That is not a hidden unit hypothesis; it is a weaker statement than exact-contact localisation.

The named D1 cell is the exact-order slice `ord(A)=a`, `ord(C)=a+1`, `ord(R)=r`. The homogeneous identity also holds on the closed faces where a leading coefficient vanishes (`a'>a` or `c'>a+1` or `r'>r`). Those closed faces are other D1 cells or higher contacts, and they are not this claim. Exact orders and closed faces are therefore distinguished: the theorem is the exact-order cone `a>=10`, `c=a+1`, `r>=a`; the proof does not invert the leading coefficients, so it does not pretend to localise onto the open cell by a unit.

A rationally valued arc with `v(A)/v(sigma)>=10` and `v(R)>=v(A)` becomes, after a common ramification that makes the uniformizer integral, an integer point of the same cone. Every source monomial acquires a nonnegative extra power of the new uniformizer, so no wall that was at grade `>=39` in the baseline can appear at grade `<=38` after ramification. The compiled `diff(...,theta)` and `diff(...,eta)` reductions modulo `sigma^{39}` are the homogeneous-stability check of this polynomial identity, not a finite sample of contacts.

---

## 8. Preserved `a>=13` order-two theorem, incomplete draft, firewall

The frozen `a>=13` producer and its hostile review are pinned by this case's `FREEZE.sha256`. That theorem uses the pole-order-two annihilator

```text
Phi7 - (p/4) Phi5 - (p^2/32) Phi3 - (p^3/128) Phi1 = 0
```

and its compiled `a=12` block is a method control: at `a=12` the triple pole `k2 C/L^3` arrives at grade 38 and the order-two combination fails linearly in the leading `k2` load. That control is not a survival result for `a=12`, and it is not re-run here. Residual contacts `a=10,11,12` are exactly the order-three window of the present claim, which overlaps `a>=13` without altering it.

The superseded unfrozen draft inherited the `a>=13` handwritten jets and stopped at `A_3,k10_1`. It produced no endpoint. Notes in the campaign ledger record it as no-verdict. This producer supersedes that draft by deriving every jet from the polar census. No verdict is taken from the incomplete run.

The compiled heartbeat is the polynomial identity

```text
Q = z^4 - 1,
P = 16 Q^2 + 20 Q + 5,
A = 16 z^{10} - 20 z^6 + 5 z^2,
A^2 - Q P^2 - 1 = 0.
```

Direct expansion of these three polynomials gives residual zero. The identity is the square-chart Pell relation used as an engine-positive control. It does not enter the D1 source, does not identify a Chebyshev survivor, and does not enlarge the theorem.

The registered claim excludes only the D1 source cone

```text
ord_sigma(A)=a,  ord_sigma(C)=a+1,  ord_sigma(R)=r,
a>=10,  r>=a
```

on the Keller chart `D(J)`, for the seven literal Faber rows, after the cited upstream square/D1 gates. It does not cover `a<=9`, `V(J)`, `p=0` or `k0=0` lifecycle routing, other D1 cells, the whole square component, order two, `(8,12)`, maximum twelve, or JC2. RESULT and REGISTRATION state that firewall in matching language. No charged artifact claims more.

---

## 9. Defect classification

No mathematical defect of the numbered claim was found. The four-atom expansion, the eleven polar families, the order-three annihilator, the target parity, the unit-ideal arithmetic, the homogeneous substitution, and the scoped overlap with the separately confirmed `a>=13` order-two theorem are independent of the AWS boolean transcript.

No custody or software defect was found. All named hashes match; exact Q and `F_65521` are distinct hosts, distinct PIDs, distinct characteristic tokens, distinct RSS and wall-clock, zero swap, empty compiler stderr, and GNU `time` as the only engine stderr.

No scope wording defect was found. Exact orders are the stated cell; closed faces are not inverted onto and are not claimed.

Smallest failing identity: none.

Smallest missing source monomial: none through grade 38. The first polar family outside the window is `k6*R*A/L^2` at grade 39. The first pole-order-four monomial is `k6*A*C/L^4` at grade 43.

CONFIRMED
