CONFIRMED

# Hostile review: direct ordered `T-cs` total-family certificate

**Identity `(*)` with `W=0`, `N=447`, `M=164`: CONFIRMED**

**Generating data without expanded composite cofactors: theorem-grade for membership: CONFIRMED**

**Geometric emptiness on `D(cs*k)`, saturation/`rho` warning, V19 typing/Lemma-0 criticism: CONFIRMED**

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-p0-total-rees-t-cs-direct-total-certificate-opus5-20260827.md` |
| Charged claim | Exact identity `cs^447 k^164 = sum cofactors * (Tg10_1..Tg12_7, Tg14_5, rs-cs*qrs, c0-cs*qc0, c1-cs*qc1, qrs)` over `Q`, hence `W=0` in the requested unit-plus-`rho` certificate |
| Producer status | `DIRECT_CERTIFICATE`. SHA-256 `7af66e58a7262ca05bf140919ed3d6ff4e0357bdb6db3378d494907ff33baa8f` |
| Reviewer / model | Grok 4.6 (xAI). Hostile different-model reread. Producer parsers, rewrite engine, hashes of `X,C,D`, and AWS/V18R1/V19 engine output were not trusted |
| Method | Independent SHA-256 of the report and every charged frozen input; sparse monomial parse of the 22 raw `.poly` bytes; exact `Fraction` staged divided differences (Lemma 0); expansion of the grade-10 chain and of the printed branch-(a) identity in both presentations; exact verification of `B1..B7` and `(5.2)`; independent directed rewriting of `(5.3)` and quotient `(5.4)` with cofactor accumulation; denominator accounting for `(5.5)` and the cube composition. No Groebner, no Singular, no AWS mutation, no `jc2-lean`, no web, no V18R1/V19 engine artifacts |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-27 |

The displayed polynomial membership holds over `Q`. `cs` and `rho` are never inverted in the identity. The only genuine source localizer is `k`, paid by `k^164`. `W=0` is the strongest instance of the requested type. The unprinted enormous composite cofactors of `(*)` are determined by verified generating data; their non-serialization is not a hole in the membership theorem.

---

## Narrow reusable theorem

Work in the ordinary polynomial ring

```text
S# = Q[cs, rs, c0, c1, qrs, qc0, qc1, rho, k, and the remaining frozen V9/V17 names]
```

over the frozen exact-`Q` rows `Tg10_1..Tg12_7` and `Tg14_5`. Let

```text
Bil = (rs - cs*qrs,  c0 - cs*qc0,  c1 - cs*qc1),
K   = (Tg10_1, ..., Tg12_7, Tg14_5, Bil, qrs) subset S#,
E_f = f after rs |-> 0, c0 |-> cs*qc0, c1 |-> cs*qc1,
I   = (E_f : f in T) in the substituted ring S (no `rs,c0,c1`).
```

Then:

1. **Lemma 0.** For each of the 22 rows there are polynomial cofactors `B_rs, B_c0, B_c1, B_qrs` with
   `f = E_f + B_rs*(rs-cs*qrs) + B_c0*(c0-cs*qc0) + B_c1*(c1-cs*qc1) + B_qrs*qrs`.
   No negative exponents. Consequently `P in I` if and only if `P in K`, with bilinear/`qrs` cofactors supplied by these `B`'s. The compiler `chart_expression` (`rs |-> cs*qrs`, word-boundary) composed with `qrs=0` recovers `E_f` as sparse polynomials.

2. **Branch (a).** In both the substituted and the honest ordered presentations,
   ```text
   cs^6 * k^2 * rho^6
     = A1*Tg10_1 + A2*Tg10_2 + A3*Tg10_3 + A4*Tg10_4
       - B_rs*(rs-cs*qrs) - B_c0*(c0-cs*qc0)
       - B_c1*(c1-cs*qc1) - B_qrs*qrs
   ```
   with the printed `A_i` and honest `B_•`. Remainder identically `0`. Only grades 10 and the four named generators are used. No factor of `cs`, `k`, or `rho` is inverted.

3. **Branch (b).** In `S/(rho)`, after the seven printed solved forms `B1..B7` (exact Laurent identities inverting only `cs` and `k`, and the units `2,3,5` of `Q`) and the decisive combination
   ```text
   Tg14_5|_{rho=0} + (cs/2)*Tg12_2|_{rho=0}
     = -(7/256)*cs^5*k + g,     g in (qc0,qc1,e0,a0,ell1), |g|=57,
   ```
   the reductions
   ```text
   1 - X = sum C_i Ebar_i,     |X|=341, |C|=716, denoms X: cs^16 k^6, C: cs^18 k^6,
   phi(X)^3 = sum D_i phi(Ebar_i),
       D on Tg11_1(10), Tg11_2(152), Tg12_3(10), Tg12_4(156),
       |D|=328, denoms cs^36 k^9,
   ```
   hold as identities of Laurent polynomials. `X` is supported on the eleven claimed shapes in `(qc0,qc1,e0,a0)`. Setting `Y := X^3 - sum D_i Ebar_i` gives `Y in (qc0,qc1)` with no extra inverted names. Combined with `U^3 subset J[1/(cs*k)]` from `B2,B3,B4` and with `1-X^9=(1-X)(sum_{j<=8} X^j)`, one has `1 in J[1/(cs*k)]`. Clearing the recorded denominators yields
   ```text
   cs^147 * k^54  in  J = (Ebar_1, ..., Ebar_22).
   ```
   Applying the same (rho-free) cofactors to the rho-carrying rows, using that every `E_i - Ebar_i` is divisible by `rho^2`, gives
   ```text
   cs^147 * k^54 + rho^2 * H  in  I
   ```
   for a polynomial `H`.

4. **Composition.** With `A = cs^147 k^54`, `Bq = rho^2 H`, `Xa = cs^6 k^2 rho^6`,
   ```text
   cs^6 k^2 * A^3
     = cs^6 k^2 (A+Bq)(A^2 - A Bq + Bq^2) - H^3 * Xa
   ```
   is an identity of polynomials in `I`, and the left side is `cs^{447} k^{164}`. Lemma 0 returns this to `K`. Thus
   ```text
   cs^447 * k^164 * (1 + rho*0)  in  K.
   ```
   Equivalently, the localization of `S/I` at `cs*k` is the zero ring: the registered ordered `T-cs` chart stratum is empty on `D(cs*k)`, including the `rho != 0` locus, for a grade-10 reason on that half.

`N` and `M` are sufficient, not claimed minimal. The composite cofactors of `(*)` need not be serialized: they are the explicit ring combination of the verified pieces above.

---

## Verdicts

| Claim | Verdict | Reason |
|---|---|---|
| Report SHA-256 `7af66e58…` | **CONFIRMED** | Independent hash of on-disk bytes |
| All 22 frozen row hashes, V9 `COEFFICIENTS.json`, V17 `RESULT.json`, charged compilers/preregistrations/promotions | **CONFIRMED** | Independent SHA-256; every producer pin matches |
| Lemma 0 for all 22 rows, signs and four bilinear/`qrs` cofactors; no hidden division by `cs`,`k`,`rho` | **CONFIRMED** | Staged `x^n-a^n` expansion; reconstruction remainder `0`; B-counts match the report |
| Full-chart term counts `4,5,5,2,5,0,5 \| 12,14,17,3,18,0,18 \| 27,36,47,12,58,9,60 \| 304` | **CONFIRMED** | Sparse `rs|->cs*qrs` counts; these are *full* chart counts, not `|E_f|` (see L1) |
| Grade-10 core `gam,del,alp,bet` and `Tg10_5` identity | **CONFIRMED** | Direct expansion against charted rows |
| Branch (a) nine-line chain and `cs^6 k^2 rho^6` in substituted `I` | **CONFIRMED** | Remainder `0`; `p kap^2 = (25/36) cs^6 k^2 rho^6` |
| Branch (a) honest ordered identity with printed `B_rs,B_c0,B_c1,B_qrs` | **CONFIRMED** | Remainder `0`; `6/6` random exact rational points |
| `B1..B7` as exact identities modulo `J[1/(cs*k)]` | **CONFIRMED** | Each head-minus-tail equals the displayed row combination; tails of `B2,B3,B4` are `0` |
| `(5.2)` residual `-(7/256)cs^5 k` plus 57-term `g` in `(qc0,qc1,e0,a0,ell1)` | **CONFIRMED** | Free-of-those-five remainder `0`; `|g|=57` |
| `(5.3)` `1-X = sum C_i Ebar_i` with claimed sizes and denoms | **CONFIRMED** | Independent rewrite; remainder `0`; `|X|=341`, `|C_i|` exactly `32,277,87,200,51,1,38,29,1`, sum `716`; denoms `cs^16 k^6` / `cs^18 k^6`; `5/5` random points |
| `(5.4)` `phi(X)^3 = sum D_i phi(Ebar_i)` and `Y in (qc0,qc1)` | **CONFIRMED** | Quotient rewrite, NF `0`; `|phi(X)|=13`; `phi(X)^2` NF has 6 terms; `|D_i|` exactly `10,152,10,156`, sum `328`, denoms `cs^36 k^9`; `phi(Y)=0` with leftover `0` |
| Exponents `cs^147 k^54` for `(5.5)` and cube composition `(447,164)` | **CONFIRMED** | Denom table reproduced from the actual objects: `C*X^8` gives `(146,54)`; `Y` denom `(48,18)` so `Y^3` plus `B4`'s `cs^{-3}` gives `(147,54)`; `147*3+6=447`, `54*3+2=164` |
| Lift `cs^147 k^54 + rho^2 H in I` | **CONFIRMED** | Every `E_i-Ebar_i` has min `rho`-valuation even and at least `2`; branch-(b) cofactors are rho-free |
| No hidden localization, illegal radical, or unproved polynomial quotient | **CONFIRMED** | Only `cs,k` and `Q`-units `{2,3,5,7}` are inverted; all inverted names are paid by the left-hand powers; Prop 3.1 is set-level and is not load-bearing |
| Honest vs substituted presentations | **CONFIRMED** | Lemma 0 is the bridge; branch (a) is printed and checked in both; branch (b) and the composite live in `I` and return to `K` by the same `B`'s |
| Complete generating data without expanded `(*)` cofactors is theorem-grade | **CONFIRMED** | See §4. The unprinted composite is a determined ring combination of verified pieces, not an existence claim from a standard basis |
| `V(I) ∩ D(cs*k) = empty` as schemes, strictly stronger than the special fibre | **CONFIRMED** | `cs^{447} k^{164} in I` makes `(S/I)_{cs k}` the zero ring |
| Interface converse on saturation vs adjoining `rho` is too broad | **CONFIRMED** | `(cs k)^m in I+(rho)` need not be `(cs k)^m(1+rho W) in I` |
| V19 after clearing `u,v` is branch (b), not the total-family type, unless `cs^a k^b | Lam_24`; Lemma 0 is missing from V18/V19 predicates | **CONFIRMED** | Read off the frozen V19 compiler and preregistration; `RawSpecial` has 26 generators including `rho` |

Failure modes examined and refused as defects of the theorem: rational denominators `2,3,5,7` (units of `Q`); inversion of `cs` *inside* §5 (cleared by `cs^{147}` / `cs^{447}`); `W=0` (admissible and strongest); non-minimality of `(447,164)` (disclosed); 774 vs 1880 rewrite steps (same normal form; see L2); unreproducible “canonical” `X,C,D` hashes without a pinned serializer (identities independently expanded; see L3).

---

## 1. Custody and SHA pins

Independently recomputed this session. Producer-quoted hashes of the report, the four charged interface/witness/promotion documents, both V18 compilers and preregistrations, the V19 compiler and preregistration, the V9 exact-`Q` coefficient manifest, the V17 exact-`Q` `RESULT.json`, and all 22 row files all match the on-disk bytes. Git HEAD matches the producer.

| Artifact | SHA-256 |
|---|---|
| producer report | `7af66e58a7262ca05bf140919ed3d6ff4e0357bdb6db3378d494907ff33baa8f` |
| staged-calculus promotion | `16ec6f54e80a420755a52b8d2068390b65344311a5f84c4d486192513a928867` |
| drop-g14 witness | `d9e5f43954240eee13311c5f386231f9ed506c4bbe978211cdfa711e3e8c86d9` |
| drop-g14 hostile review (Grok) | `7fbd9423b6840e4f3017687897e0dad373a04d2683589ccb432682553053c3cf` |
| grade-14 fibre promotion | `5fd19f3577fbd24e74f2c395ab6fd17f84d75f73e00eeae53267536c33265fd4` |
| V18 `PREREGISTRATION.md` | `b07e8e7ca19b9a90618e875c22dd797380cdd315bd9eec3ab5744d2f7b01ed95` |
| `PREREGISTRATION_V18R1.md` | `02be2839a80706511e0a7be8e60220e0dad5b114c6c66d9004f55a2b4a2164b3` |
| `compile_t_cs_rho_unit_v18.py` | `50596db3a7009fa887e1679a8dbbc636afd68af66f923bfe13e7b5c3599548e6` |
| `compile_t_cs_rho_unit_v18r1.py` | `c23c67a7f6f3e3071f384db229fe3ab4ba5578e0166dead85177a6923ef08ef6` |
| V19 `PREREGISTRATION.md` | `60692d787fe0a3e9bec285e038bc3bb69a4bf820413b9e2ba6db514e6b850472` |
| `compile_t_cs_certificate_v19.py` | `132108305f80db09e08572a2d5d623be968cd15612b3afe411f5840dd78ef17a` |
| V9 exact-`Q` `COEFFICIENTS.json` | `86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e` |
| V17 exact-`Q` `RESULT.json` | `25d40556618983a350eda99d4fb6aae8d1e5cd2cf328041963b46d61729af543` |
| `Tg14_5_q.poly` | `91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7` |

Exact-`Q` V9 rows, matching the producer list and the V9 manifest:

```text
9a055c5343e43abef6017f82d7aa0f9405d2152227dbd8d3ac4a0e74bac02fec  Tg10_1.poly
50c88196628dc04407c47c49059849f7f43265ade03afa13c9f27eecc1f928a6  Tg10_2.poly
4913e736b6713433411dc1513e8813968bace256b80e6597367ea9917f8a8cda  Tg10_3.poly
6c33503e153a1adda56810a62db220f74b1dfd8c71158d1f3794f128773c503d  Tg10_4.poly
5c1d7ae3fb821011d5c65bbd2bf81389587bbf82c515a9be03b095dfe095a5ec  Tg10_5.poly
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  Tg10_6.poly
080d52ab67b2d5a28c8a8cc35e912b9e99d4be8a53bfb73d1d9bc6d70b20b440  Tg10_7.poly
11f6bd635957677cb8a0b29cedc847369d68d6b695e844efdf32f683078db469  Tg11_1.poly
fa9c5c109541478fc56a0a4c9564a80cbdd9aeaa2bd8a1c2eabfa5076afb1093  Tg11_2.poly
52e685581979a789b4aa72457d982f269d0f344530fd1fab8af541f2570f1650  Tg11_3.poly
d56bce83a56222c76169b259f55b452be61cb892b55d71d0d34abdcdda5ca050  Tg11_4.poly
ca08b238d9d592e5736a167981857a6af60af908b2402e4ff43633fa6fc71ef2  Tg11_5.poly
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  Tg11_6.poly
3c298d36d1353ae5b7ec7e0ce597d2a2ab85ef6fbfe7eebe086e761343e0b156  Tg11_7.poly
799ccff5e54711c53da6498ac01f8ac3fae2290600fd19664238cb49ed8d6e54  Tg12_1.poly
b66a3e858c41d22b4ce3f4592cdee28664e5ba677f138860f840565625b073e6  Tg12_2.poly
b0d090f9000f6e74bd214a0c443450114994c3fd61a0a577453f8c69acc42f87  Tg12_3.poly
091117b510011acf659038b94b3c872423d7b568cb28b04fb2cf9555fd4da327  Tg12_4.poly
9389b34abad72debf6e621bb0082c2882c3cfcc02cbdcd1a00d03cdff89bf1aa  Tg12_5.poly
d545fc9b104202d5e4db12fbd56433ba7fd714f13669e9a11536dc47c9137ebf  Tg12_6.poly
68b897df93e18da37a237bbdddab4776f947d37bdc2444f4d2e3ea043ee79f75  Tg12_7.poly
```

`Tg10_6.poly` and `Tg11_6.poly` are the two-byte file `0\n`. Raw sparse term counts of the 22 files are `4,5,5,2,5,0,5,12,14,17,3,18,0,18,27,36,47,12,58,9,60,304`. All `rho` exponents in all 22 rows are even.

No V18R1 or V19 engine output, log, artifact, or validator result was read.

---

## 2. Exact replay telemetry

Independent sparse parser (monomial keys, `fractions.Fraction` coefficients). Chart substitution is monomial-level on the names `rs,c0,c1` only, so `rs1, cs1, k1, …` are untouched. This is the compiler's word-boundary `chart_expression`, not a string regex replay of the compiler.

### Lemma 0 and presentations

For each row, `c0` then `c1` then `rs` were eliminated by the telescoping identity `x^n - a^n = (x-a) sum_{j<n} x^{n-1-j} a^j`, with leftover `(cs*qrs)^n` sent to the `qrs` cofactor and `E_f` using `rs |-> 0`. Reconstruction `E + B_rs*Bil_rs + B_c0*Bil_c0 + B_c1*Bil_c1 + B_qrs*qrs` equals the raw row, remainder `0`, all 22 rows. Claimed B-counts

```text
Tg10: (2,1,1,1),(4,1,3,2),(2,2,2,1),(0,2,2,0),(2,2,2,1),(0,0,0,0),(2,2,2,1)
Tg11: (6,2,2,4),(9,2,4,6),(8,4,4,5),(0,1,3,0),(8,5,5,5),(0,0,0,0),(8,5,5,5)
Tg12: (11,3,3,8),(18,3,7,14),(21,7,8,15),(3,2,6,3),(28,12,14,19),(9,3,5,5),(29,14,16,20)
Tg14_5: (131,38,45,97)
```

match exactly. No negative exponents in any `B`. `E_f` equals the full chart with `qrs=0`, as sparse polynomials, all 22. Full-chart (keep `qrs`) term counts match the displayed `4,5,…,304` list. `|E_f|` is strictly smaller on 18 of 22 rows because `rs|->0` kills `qrs`-carrying terms; that is L1, not a failed identity.

Sample `Ebar` rows reproduce the drop-g14 §3.1 display term for term (`Tg10_1..4,5,6,7`, `Tg11_1,2,4,6`, `Tg12_4,6` checked). The five-zero slice of `Tg14_5|_{rho=0}` is exactly `-3/64 cs e1^2 - 1/128 cs^5 k`.

### Grade 10 and branch (a)

```text
(8/3) E(Tg10_1) = a0 w + a1 u + kap
(8/3) E(Tg10_2) = a0 u + (1/4) w^2 + p a1 w
(16/3)(E(Tg10_3)-(p/2)E(Tg10_1)) = u w
(32/3) E(Tg10_4) = u^2 + p w^2
E(Tg10_5) = (p/2) E(Tg10_3) - (3/8) p^2 E(Tg10_1)
```

all remainder `0`, with `u=cs*qc0`, `w=cs*qc1`, `p=rho^2`, `kap=(5/6)cs^3 k p`. All nine chain lines expand to polynomial identities on these generators. The last line is `(25/36) cs^6 k^2 rho^6`. The printed `A1..A4` give `A·(E10_1..E10_4) - cs^6 k^2 rho^6 = 0` (`|A|=(4,2,3,3)`). The printed honest `B_rs,B_c0,B_c1,B_qrs` (`14,9,6,7` terms) give remainder `0` in `S#`. Six random exact rational points, seed `20260827`, all `0`. No negative exponents in any `A_i` or honest `B_•`.

### Branch (b)

`B1..B7` as written, including the displayed signs:

```text
ell1 - B1_rhs = (-16/5) cs^{-3} k^{-1} Ebar(Tg11_1)
qc0 qc1       = (16/3)  cs^{-2}          Ebar(Tg10_3)
qc0^2         = (32/3)  cs^{-2}          Ebar(Tg10_4)
qc1^3         = (32/3)  cs^{-2} qc1      Ebar(Tg10_2)
              + (-64/3) a0 cs^{-3}       Ebar(Tg10_3)
a0 e0 - B5_rhs = (8/3)                   Ebar(Tg11_2)
e0^2  - B6_rhs = (32/3)                  Ebar(Tg12_4)
a0^2  - B7_rhs = (-4/3) cs^{-1} ell1     Ebar(Tg11_1)
              + (-8/3) cs^{-1}           Ebar(Tg12_3)
```

all remainder `0` as Laurent polynomials. The only inverted ring elements are `cs`, `k`. In the quotient `qc0=qc1=0`, `B5` and `B6` become `a0 e0 = (8/3) phi(Tg11_2)` and `e0^2 = (32/3) phi(Tg12_4)`, and `B7` remains exact.

`(5.2)`: `Ebar(Tg14_5)+(cs/2)Ebar(Tg12_2) + (7/256)cs^5 k` has 57 terms, all in `(qc0,qc1,e0,a0,ell1)`, and no leftover constant term.

`(5.3)` independent rewrite of `g_scaled = 256/(7 cs^5 k) * g` under priority `B1..B7`, accumulating cofactors of `1-g_scaled` from the `(5.2)` combination plus each rewrite. **774** one-monomial rewrites (producer: 1880; see L2). Result:

```text
|X| = 341
X denom = (cs^16, k^6)
X extra inverted names: none
X shapes: the eleven claimed (qc1^2, a0 qc1^2, a0 qc1, qc0, e0 qc1,
          a0 qc0, e0 qc1^2, e0 qc0, qc1, e0, a0); a0 e0 does not survive
|C_i| = Tg10_2 32, Tg10_3 277, Tg10_4 87, Tg11_1 200, Tg11_2 51,
        Tg12_2 1, Tg12_3 38, Tg12_4 29, Tg14_5 1     (716 terms)
C max denom = (cs^18, k^6)
1 - X - sum C_i Ebar_i = 0     (expanded; |lhs|=|rhs|=342)
5/5 random exact points with cs,k != 0
coefficient-denominator primes of X,C: {2,3,5,7}
```

`(5.4)` in the quotient `qc0=qc1=0` (the honest reading of `phi`): `phi(X)` already has 13 terms, supported on `{a0, e0}`. Unreduced `phi(X)^2` has 78 terms and reduces in 78 steps to **6** terms, supported on `{e0}`. Unreduced `phi(X)^3` reduces in 318 steps to **0**, with

```text
|D_i| = Tg11_1 10, Tg11_2 152, Tg12_3 10, Tg12_4 156     (328 terms)
D max denom = (cs^36, k^9)
D extra inverted names: none
phi(X)^3 - sum D_i phi(Ebar_i) = 0     (expanded)
```

Lifting those `D_i` against unquotiented `Ebar` and setting `Y = X^3 - W_J`:

```text
|X^3| = 1403096,  |Y| = 1403880,  Y denom = (cs^48, k^18)
phi(Y) = 0, leftover after splitting Y = qc0 Y0 + qc1 Y1 is the zero polynomial
Y extra inverted names: none
Y0 denom (cs^44, k^16), Y1 denom (cs^48, k^18)
```

So `Y in U = (qc0,qc1)` as Laurent polynomials inverting only `cs,k`. `U^3` is generated by monomials each a polynomial multiple of `qc0^2`, `qc0 qc1`, or `qc1^3`, which lie in `J[1/(cs*k)]` by `B2,B3,B4` (extra `cs^{-2}` or `cs^{-3}`, no `k`). Worst-case clearing for the `Y^3` piece is therefore `(48*3+3, 18*3) = (147, 54)`. Independently, `C * X^8` clears at `(18+128, 6+48) = (146, 54)`. The table in §5.5 is therefore a correct sufficient exponent, and `A'=147`, `B'=54` is justified.

Every `E_i - Ebar_i` is either `0` (`Tg10_6, Tg11_6`) or has minimum `rho` exponent even and at least `2`. The branch-(b) cofactors do not involve `rho`. Applying them to the rho-carrying rows yields `cs^{147} k^{54} + rho^2 H in I` for a polynomial `H`.

### Composition

The identity `cs^6 k^2 A^3 = cs^6 k^2 (A+Bq)(A^2-A Bq+Bq^2) - H^3 Xa` is polynomial: `H^3 Xa = cs^6 k^2 (rho^2 H)^3 = cs^6 k^2 Bq^3`. No division by `cs^6 k^2` occurs in the ring. Left side `cs^{6+147*3} k^{2+54*3} = cs^{447} k^{164}`. Lemma 0 supplies the bilinear/`qrs` cofactors from the substituted combination. `W=0`.

---

## 3. Ranked findings

### High

None. The membership, the presentations, the exponents, and the three named scope claims survive.

### Medium

None that change a verdict.

### Low

**L1. `E_f` versus full-chart term counts.** Lemma 0 defines `E_f` by `rs |-> 0`. The sentence that this “is exactly the compiler's `chart_expression` map composed with `qrs=0`” is true as *polynomials*. The displayed list `4,5,…,304` is the full `rs |-> cs*qrs` chart (qrs kept), matching the compiler and the earlier reviews. Sparse `|E_f|` is `3,3,4,2,4,0,4 | 8,8,12,3,13,0,13 | 19,22,32,9,39,4,40 | 207`. Harmless conflation of two checksums; both were recomputed.

**L2. Rewrite-step census.** Producer §5.3 says 1880 rewrites. One-monomial priority `B1..B7` on `g_scaled` terminates in 774 steps at an `X` with the claimed size, shapes, and `C_i` support, and with `1-X = C·Ebar` exactly. The NF is the load-bearing object; the step count is not.

**L3. “Canonical” SHA-256 of `X`, `C`, `D`.** The report does not pin a serializer, and the local scripts named in §9 were not committed. Independent reconstruction matches every published *size, support, and denominator*, and the identities expand to zero. The hashes are therefore unused. Byte-level custody of `C` and `D` is the rewrite itself.

**L4. Composite cofactors of `(*)` are not printed.** Disclosed in §6.2. They are determined by the verified pieces (see §4). Not a membership defect.

**L5. Proposition 3.1 is set-level.** It is the geometric reason `W=0` is available, and it is not used as a polynomial certificate. Certificate (a) is.

---

## 4. Generating data without expanded `(*)` cofactors

The charged theorem is existence of polynomial cofactors over `Q` for `cs^{447} k^{164} in K`. That is established by a finite list of identities, each independently expanded or rewritten with accumulated cofactors:

- Lemma 0 (22 rows);
- the printed branch-(a) combination (substituted and honest);
- `B1..B7` and `(5.2)`;
- the rewrite `(5.3)` producing explicit `C` with `1-X = C·Ebar`;
- the quotient rewrite `(5.4)` producing explicit `D` with `phi(X)^3 = D·phi(Ebar)` and `Y in U`;
- `U^3 subset J[1/(cs*k)]` from `B2,B3,B4`;
- the geometric series `1-X^9 = (1-X) sum_{j<=8} X^j` and the binomial `X^9 = (Y+W_J)^3`;
- clearing of a recorded finite power of `cs*k`;
- the cube identity of §6.1, polynomial in `A, Bq, Xa, H`;
- Lemma 0 again, to return from `I` to `K`.

None of these steps inverts `rho`. The only inverted non-units are `cs` and `k`, and both appear as positive powers on the left of `(*)`. Coefficient denominators factor over `{2,3,5,7}`. There is no radical, no saturation routine, no ideal-quotient black box, and no unproved claim that a Laurent remainder is polynomial.

Expanding `X^8` or `Y^3` (`|Y| ~ 1.4e6`) would produce a huge but determined element of `K`. That expansion is not required for membership once the factors are known to lie in the localized ideal and the denominators are known to be finite of the recorded type. This is a verified constructive Nullstellensatz certificate in the rewriting sense, not a Groebner-harvested matrix. It is theorem-grade for the charged identity. It is not a byte-serialized expansion of `(*)`, and the producer does not claim that it is.

---

## 5. Geometry, saturation/`rho`, and V19

**Geometry.** `cs^{447} k^{164} in I` means `(S/I)_{cs k} = 0`. The registered ordered `T-cs` stratum is empty on `D(cs*k)` as a scheme, not merely set-theoretically and not merely on `rho=0`. The `rho != 0` half is certificate (a) and uses only `Tg10_1..Tg10_4`. The special-fibre promotion (`sol-20260827`) is the other half and is not reused as a cofactor source; branch (b) is re-derived from the frozen rows.

**Saturation versus adjoining `rho`.** The staged-calculus converse — “chart-fibre emptiness has a homogeneous power-containment form after clearing a finite saturation exponent” — yields `(cs k)^m in I+(rho)`, i.e. `(cs k)^m - rho G in I`. This is of type `cs^N k^M (1+rho W) in I` if and only if `(cs k)^m` divides `G`. Those operations do not commute. The interface sentence is too quick, independently of this chart. This report closes the gap by supplying the missing `rho != 0` half, not by repairing the implication. Agreed.

**V19.** Frozen `compile_t_cs_certificate_v19.py` builds `RawSpecial = E + Localizers` with `Localizers = (qrs, rho, 1-u*cs, 1-v*k)` and `E` the 22 substituted rows: 26 generators, `rho` included, `qring` forbidden. A PASS is `c = sum_{i<=22} L_i Ehat_i + L_23 qrs + L_24 rho + L_25(1-u cs) + L_26(1-v k)` with `c in Q^x`. The map `psi: u |-> cs^{-1}, v |-> k^{-1}` produces `c in I+(rho)` after clearing `cs^a k^b`, which is branch (b) with explicit cofactors, *not* the total-family type. The extra condition is that `psi(L_24)` have no negative `cs` or `k` (equivalently `cs^a k^b | Lam_24`). The frozen acceptance predicate tests residual zero, nonzero constant unit, and three artifact writes; it does not test that divisibility. Converting substituted `Ehat` into the honest ordered presentation requires Lemma 0, which is not recorded in the V18/V19 preregistrations. All three points in producer §7 are correct. Repair path (ii) — compose a failing V19 lift with certificate (a) — is the same cube as §6.1 and would only compete on exponent quality. V19 is not needed for the mathematics of `(*)` and is not harvested here.

---

## 6. Scope firewall and nonclaims

Promote, and only this:

> On the frozen V9/V17 exact-`Q` bytes, `cs^{447} k^{164}` lies in
> `(Tg10_1..Tg12_7, Tg14_5, rs-cs*qrs, c0-cs*qc0, c1-cs*qc1, qrs)`
> by an exact polynomial identity that inverts neither `cs` nor `rho` and localizes only at `k`. Equivalently the registered ordered `T-cs` chart stratum is empty over `D(cs*k)`, its `rho != 0` half for a grade-10 reason. `W=0` is admissible. `(447,164)` is sufficient, not minimal.

Do **not** promote, and do not infer from this review:

- minimality of `N` or `M`, or the existence of a branch-(a) element with `rho^2` in place of `rho^6`;
- the `k=0` residual stratum (still live, now carrying weight `k^{164}`);
- Gate `T`, order two, the `(8,12)` frontier, maximum twelve, JC2;
- later ordered charts `T-c0`, `T-c1`, either second-stage `A` chart, overlaps, the terminal receiver, the deck/square bridge, the generic comparison, or any effective bound on the decisive source grade;
- TD6, the prime-ray lane, AS109, or any Lean statement;
- any F65521 reduction of branch (b) (branch (a) inverts only `2,3,5` and would transfer; this session did not run the modular check);
- independence from the frozen V9/V17 bytes, or a re-extraction of those coefficients from the Faber emitter;
- a harvested V18R1 or V19 PASS, or any claim that a raw V19 unit certificate is of total-family type;
- a byte-serialized expansion of the composite cofactors of `(*)`.

`jc2-lean` was not accessed. No AWS state was mutated. No Singular or Groebner basis was run. No V18R1/V19 engine output was read. The only repository file written is this review.
