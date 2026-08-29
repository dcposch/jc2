CONFIRMED / REFUTED / GAP

# Hostile algebra review: cross-pollination algebraic claims
# (`ideation-20260827T0145Z-crosspollination-opus5.md`)

**`k=0` delayed-load characteristic-zero point, all 22 frozen rows: CONFIRMED**

**No prefix certificate `cs^a k1^b rho^c` (nor rho-torsion on `V(k) ∩ D(cs k1)`) in characteristic zero: CONFIRMED**

**Three modular points alone do not prove that: CONFIRMED as a limitation**

**Torsion-multiplier lemma (commutative-ring identity): CONFIRMED**

**Existence of some `cs^N k^M` in the honest total ideal from the promoted fibre theorem plus honest `cs^6 k^2 rho^6`, without branch `(b)`: CONFIRMED as Nullstellensatz existence, GAP as an explicit certificate**

**Fibre emptiness ⇒ multiplicative `1+rho W`: REFUTED** (the promoted converse-correction stands; the lemma uses only `J+(rho)`)

**Grading lattice rank 2, `deg_s` table, row-degree `g`, impossibility of `g(rho)=g(cs)=0`: CONFIRMED; opus5 `deg_2` / `M>=1`: REFUTED**

**Seven first-jet identities: CONFIRMED**

| Field | Value |
|---|---|
| Target | `xmodel/ideation-20260827T0145Z-crosspollination-opus5.md` |
| Charged SHA-256 | `c16cca5ca7aa72d7bc8eb83bc2ba2d9982bae59e251c35c1fb3ae472c095e65a` |
| On-disk SHA-256 | same (independent `sha256`; match before reading) |
| Reviewer / model | Grok 4.6 (xAI). Different-model hostile algebra reread. Producer `/tmp` scripts, modular samples, and narrative “VERIFIED-HERE” banners were not trusted |
| Method | Independent SHA-256 of the memo and of the 22 frozen exact-`Q` rows; recursive sparse parse (word-boundary identifiers, `^`, exact `Fraction`, parenthesized V17 coefficients); exact evaluation in the tower `Q(i,√2)[a0]/(a0^2-σ)`; modular reconstruction of the three printed cores plus sequential `k2c,rs1,k10_4` fill; integer nullspace of the 641 homogeneity constraints; derivation/`d/dp` expansion of the seven jet identities. No Groebner, no Singular, no AWS, no web, no `jc2-lean`. Short `/tmp/xp0827_grok/` scripts only |
| Already-confirmed, not redone | Direct `T-cs` identity `cs^447 k^164` (Grok `f16e1114…`, Fable5 `c9abdce7…`); `J1=0` census (Grok `bedb8dfe…`) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-27 |

The memo’s two new load-bearing claims split cleanly. The delayed-load witness is a genuine characteristic-zero closed point of the frozen prefix, and it kills every monomial `rho`-torsion / `cs^a k1^b rho^c` certificate on `V(k) ∩ D(cs k1)` from these 22 rows. The torsion-multiplier is a correct ring identity and does convert the promoted *additive* special-fibre containment plus honest `cs^6 k^2 rho^6` into *existence* of some `cs^N k^M` in the honest ideal, without branch `(b)`; it does not produce a replayable identity, and it does not repair the false converse that fibre emptiness yields `1+rho W`.

Nothing here proves or disproves Gate T or JC2.

---

## Verdicts

| Claim (memo locus) | Verdict | Residual / reason |
|---|---|---|
| Memo SHA-256 `c16cca5c…` | **CONFIRMED** | Independent hash of on-disk bytes |
| All 22 frozen exact-`Q` row hashes vs V9 `COEFFICIENTS.json` / V17 `Tg14_5_q.poly` | **CONFIRMED** | Independent `sha256`; term counts `4,5,5,2,5,0,5,12,14,17,3,18,0,18,27,36,47,12,58,9,60,304` |
| Zero-load section `CS0` (`cs=1`, `k=0`, other names `0`, `rho` free) kills all 22 rows in `Q[rho]` | **CONFIRMED** | Exact evaluation at `rho ∈ {0,1,2,3/2}` |
| Delayed-load control: `cs=1,k=0,k1` free, other names `0` does *not* vanish | **CONFIRMED** | `Tg11_1=(5/16)k1 rho^2`, `Tg11_3=(5/32)k1 rho^4`, `Tg11_5=-(5/128)k1 rho^6`, `Tg11_7=(5/256)k1 rho^8` |
| Supplied `S,D,E,F` formulas, minus sign branch, at `(cs,rho,k1)=(1,1,1)` | **CONFIRMED** | `S^2=5/12`, `D^2=-(5/12)i`, `E=-2S`, `F=-2i D` |
| Explicit char-0 point of all 22 rows with `k=0` and `cs k1 rho ≠ 0` | **CONFIRMED** | Tower `Q(i,√2)[a0]/(a0^2-σ)`, `σ=(5/48)(1-i)(1+√2)`; remainder `0` on every row |
| Printed modular triples are reductions of the same algebraic family | **CONFIRMED** | Four sign/branch matches at each of `p=65521,1000033,1000081`; after `k2c,rs1,k10_4` fill, all 22 rows `0` |
| No `cs^a k1^b rho^c ∈ I` (nor in `rad(I)`) from these 22 rows, char 0 | **CONFIRMED** | The point evaluates that monomial to `1` |
| No `rho`-torsion on `V(k) ∩ D(cs k1)` from these 22 rows, char 0 | **CONFIRMED** | `rho=1` is a unit at the point of `V(I+(k))` |
| Three modular points alone prove a char-0 component / exclude all `Q`-certificates | **REFUTED** as a stand-alone inference | They prove properness of the three reductions; lift and denominator-free exclusion require the tower point |
| Torsion-multiplier as a commutative-ring identity | **CONFIRMED** | `f ≡ c rho (mod I)` and `g rho^r ∈ I` ⇒ `g f^r ∈ I` |
| Promoted fibre emptiness + honest `cs^6 k^2 rho^6` ⇒ some `cs^N k^M ∈ K`, no branch `(b)` | **CONFIRMED** existence via weak Nullstellensatz + Rabinowitsch + the lemma; **GAP** as an explicit identity | No exponents, no cofactors; does not replace the already-confirmed `(447,164)` |
| Fibre emptiness ⇒ `cs^N k^M (1+rho W) ∈ J` | **REFUTED** | Promoted correction `593f953b…`: generally only `cs^N k^M ∈ J+(rho)` |
| Honest/substituted translation of the existence conclusion | **CONFIRMED** | Reviewed Lemma 0: `P ∈ I ⇔ P ∈ K` for polynomials of the substituted ring; `cs^N k^M` is such a polynomial |
| All 22 rows even in `rho`; evenness upgrades `I+(rho)` to `I+(rho^2)` for rho-even `f` | **CONFIRMED** | Zero odd-`rho` monomials; generators of `K` are rho-even |
| Grading lattice rank 2; `deg_s` with `deg_s(rho)=0`, `deg_s(cs)=2` extends to 40 names; `deg_s(Tg{g}_j)=g` | **CONFIRMED** | 641 constraints, rank 38, nullity 2; table identical to memo §2.1 |
| A grading with `g(rho)=g(cs)=0` (opus5 `deg_2`); forced `M>=1` | **REFUTED** | `(rho,cs)` pairing on the lattice has det `1/2 ≠ 0` |
| `Tg11_j = D(Tg10_j) - ell1 ∂_p(Tg10_j) + k R_j`, `R_j ∈ (c0,c1)`, all seven `j` | **CONFIRMED** | `R_4=R_6=0`; `R_1=(5/16)c0 cs+(5/64)c1 rs` as displayed |
| Direct `T-cs` `(447,164)` / `J1=0` census | **NOT REDONE** | Independently confirmed at the hashes named by the prompt |

---

## Narrow reusable theorems

Work in the ordinary polynomial ring `R = Q[N]` on the 40 names occurring in the frozen bytes

```text
a0 a1 aa0 aa1 aaa0 aaa1 ac3 ac4 az3 az4
c0 c1 cs cs1 cs2 cs3 cs4
e0 e1 ec3 ec4 ee0 ee1 ell1 ell2 ell3 ell4 ez3 ez4
k k1 k10_3 k10_4 k2c rho
rs rs1 rs2 rs3 rs4
```

Let `Tg10_1,…,Tg12_7` be the frozen exact-`Q` V9 files and `Tg14_5` the frozen exact-`Q` V17 file (hashes in §1). Let `I ⊂ R` be the ideal they generate. Chart names `qrs,qc0,qc1` do not occur in the files.

### T1. Delayed-load prefix point

Let `K = Q(i, √2)[α] / (α^2 − σ)` where `i^2 = -1`, `(√2)^2 = 2`, and

```text
σ = (5/48) (1 - i) (1 + √2) ∈ Q(i, √2).
```

This is a degree-`8` extension of `Q` (`σ` is not a square in `Q(i, √2)`). The `R → K` homomorphism sending

```text
cs ↦ 1,   rho ↦ 1,   k1 ↦ 1,   k ↦ 0,
a0 ↦ α,   a1 ↦ i(√2 - 1) α,
e0 ↦  ((√2 - 2)(1 - i)) α,
e1 ↦  (-√2 (1 + i)) α,
k2c ↦ (1/8)(1 - i)(1 - √2),
rs1 ↦ (1/6)(1 + i)(1 - √2),
k10_4 ↦ (1+i)(275/256 - (827/768)√2)  +  (i/3)(1 - 2√2) α,
```

and every other name to `0`, kills `I`. In particular `k = 0` and `cs k1 rho = 1 ≠ 0` in `K`. Consequently:

1. `V(I) ∩ V(k) ∩ D(cs k1 rho)` is nonempty over `Qbar`. It contains a closed point defined over `K`.
2. No polynomial that is a unit at this point lies in `I` or in `rad(I)`. In particular, for all `a,b,c ≥ 0`,

   ```text
   cs^a k1^b rho^c  ∉  rad(I).
   ```

   The same holds after multiplying by any `1 + rho W`, since `rho ↦ 1`.
3. `rho` is a unit of the local ring of this point of `V(I+(k))`. Hence `rho` is not nilpotent in `(R/(I+(k)))_{cs k1}`: these 22 rows produce **no** `rho`-torsion certificate on the delayed-load open.

The zero-load section `CS0` (`cs=1`, every other name `0` except `rho` free) is a second, disjoint `Q[rho]`-point of `V(I+(k))`. Both sub-fan readings of `V(k)` that the `k10` filing review refused to collapse are nonempty for this prefix.

### T2. Torsion-multiplier, at its true scope

Let `A` be a commutative ring, `J ⊂ A` an ideal, `rho ∈ A`. If `f - c rho ∈ J` and `g rho^r ∈ J`, then `g f^r ∈ J`. Proof: `f ≡ c rho (mod J)`, so `f^r ≡ c^r rho^r`, so `g f^r ≡ c^r (g rho^r) ≡ 0`.

Let `K_hon` be the honest ordered-chart ideal in `S#` generated by the 22 rows and `(rs - cs qrs, c0 - cs qc0, c1 - cs qc1, qrs)`, and let `I_sub` be the substituted ideal (the image of the rows after `rs ↦ 0`, `c0 ↦ cs qc0`, `c1 ↦ cs qc1`). Reviewed Lemma 0 identifies membership of substituted-ring polynomials in `I_sub` with membership in `K_hon`.

The promoted localized special-fibre theorem (hash `5fd19f35…`) says that `V(I_sub + (rho)) ∩ D(cs k)` is empty over `Qbar`. Weak Nullstellensatz in the Rabinowitsch extension `1 - u cs`, `1 - v k`, followed by clearing `u,v`, therefore produces some `N,M` and some polynomial `H` with

```text
cs^N k^M  ∈  I_sub + (rho)     (equivalently in K_hon + (rho)).
```

This is containment in `J+(rho)`, **not** an identity `cs^N k^M (1+rho W) ∈ J`. That stronger multiplicative form is exactly what the promoted converse-correction (`593f953b…`) refuses, and the refusal is correct: `H` need not be divisible by `cs^N k^M`.

Branch `(a)`, already confirmed in both presentations and not re-expanded here, gives `cs^6 k^2 rho^6 ∈ K_hon`. The torsion-multiplier with `f = cs^N k^M`, `g = cs^6 k^2`, `r = 6` then yields

```text
cs^{6N+6} k^{6M+2}  ∈  K_hon.
```

All 22 rows are even in `rho` and the chart equations are rho-free, so `K_hon` is generated by rho-even polynomials. The even element `cs^N k^M` of `K_hon + (rho)` is then automatically in `K_hon + (rho^2)` (odd part of the cofactor is itself a multiple of `rho`). The lemma at `r = 3` against `rho^2` gives the tighter existence bound `cs^{3N+6} k^{3M+2} ∈ K_hon`. Neither bound is an exponent; Nullstellensatz supplies no `N`.

Thus: **existence** of some polynomial `cs^• k^•` in the honest total ideal follows from the promoted fibre theorem plus honest branch `(a)`, without branch `(b)`, saturation beyond the `cs^N` already present, or a `1+rho W` identity. **An explicit, replayable membership matrix with known exponents does not follow.** The already-confirmed identity `cs^447 k^164 ∈ K_hon` remains the certificate. Branch `(b)` is not load-bearing for existence; it is load-bearing for the displayed exponents.

---

## 1. Custody

Independently recomputed this session. The memo hash matches the prompt pin before any mathematical reading. Every V9 exact-`Q` `Tg*.poly` named by `COEFFICIENTS.json` rehashes. V17 `Tg14_5_q.poly` rehashes to the previously reviewed `coefficient_sha256`. Git HEAD matches the memo’s charged value.

| Artifact | SHA-256 |
|---|---|
| target memo | `c16cca5ca7aa72d7bc8eb83bc2ba2d9982bae59e251c35c1fb3ae472c095e65a` |
| V9 exact-`Q` `COEFFICIENTS.json` | `86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e` |
| `Tg14_5_q.poly` | `91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7` |
| `T-cs` hostile review (Grok; not redone) | `f16e1114b24e88dfa60d0e687881817f73055361d450547f40ddc9cd5374a844` |
| `T-cs` hostile review (Fable5; not redone) | `c9abdce769be28cfce6e780caacbcc3b50d75501c2377d5581731e5b118002b7` |
| `J1=0` hostile review (Grok; not redone) | `bedb8dfe0a451fee8082bbd61f5134f1dc43fd9e20e7b23d485f475bfde31a03` |
| grade-14 fibre promotion (cited, not re-proved) | `5fd19f3577fbd24e74f2c395ab6fd17f84d75f73e00eeae53267536c33265fd4` |
| staged-calculus converse correction (cited) | `593f953bd95b18cecbd3acb11a68a7d5cc64adabfc015fb5f4c82b2ca93874e5` |

Exact-`Q` V9 rows:

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

`Tg10_6.poly` and `Tg11_6.poly` are the two-byte file `0\n`. Paths: V9 `cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_q_v9/compiled/`, V17 `cases/max12_812_order2_p0_total_rees_t_cs_row5_g14_export_v17_20260826/aws_q/compiled/Tg14_5_q.poly`. The F65521 copies and the V20 exporter were not consumed.

Replay scripts under `/tmp/xp0827_grok/` (not committed): parser `b510547b…`, reconstruction `904d6753…`, char-0 point `1234fb16…`, secondary `92590f30…`.

---

## 2. Delayed-load witness

### 2.1 Slice of the 22 rows at `k = rs = c0 = c1 = 0` plus unused jets

Killing `{k, rs, c0, c1, ell1..ell4, cs1..cs4, aa*, aaa*, ee*, ec*, ez*, ac*, az*, k10_3, rs2..rs4}` leaves only

```text
Tg11_1 = (5/16) cs^3 k1 rho^2 + (3/8) a0 e1 + (3/8) a1 e0
Tg11_2 = (3/8) a0 e0 + (3/8) a1 e1 rho^2
Tg11_3,5,7 = rho^{2,4,6}-multiples of Tg11_1
Tg12_1 = (5/16) cs^3 k2c rho^2 - (3/8) cs a1^2
Tg12_2 = (15/64) cs^2 k1 rho^2 rs1 - (3/4) cs a0 a1 + (3/32) e1^2
Tg12_4 = (3/32) e0^2 + (3/32) rho^2 e1^2 - (3/4) cs a0 a1 rho^2
Tg12_3,5,7 = k2c-linear, and after the Tg12_1 pivot become
            rho-multiples of  e0 e1 - 2 cs (a0^2 + rho^2 a1^2)
Tg14_5 = (-5/128) cs^3 rho^6 k10_4  +  (terms in a0,a1,e0,e1,k2c,rs1,k1,cs,rho)
```

Grade 10, `Tg11_4`, `Tg11_6`, `Tg12_6` vanish identically on the slice. The independent conditions on `(a0,a1,e0,e1)` are therefore four:

```text
gam:  a0 e1 + a1 e0 + (5/6) cs^3 k1 rho^2 = 0
del:  a0 e0 + rho^2 a1 e1 = 0
bet:  e0^2 + rho^2 e1^2 - 8 rho^2 cs a0 a1 = 0
alp:  e0 e1 - 2 cs (a0^2 + rho^2 a1^2) = 0   (after substituting k2c from Tg12_1)
```

Then `k2c`, `rs1`, `k10_4` are uniquely determined on `D(cs k1 rho)` by the displayed unit pivots. This is the memo’s shifted core, recovered from the bytes, not from the memo’s displays.

### 2.2 Algebraic solution of the core

Set `λ = a1/a0` (the locus `a0=0` is incompatible with `del` and `bet` on `D(rho)` unless the point is zero). Eliminating `(e0,e1)` from `gam,del` and imposing `alp,bet` yields the quadratic

```text
μ^2 + 6μ + 1 = 0,    μ := rho^2 λ^2,
```

so `μ = -3 ± 2√2 = −(√2 ∓ 1)^2` and

```text
λ = ± i (√2 − 1) / rho     or     λ = ± i (√2 + 1) / rho.
```

The branch `λ = i(√2 − 1)` at `(cs,rho,k1)=(1,1,1)` gives `kap1 = 5/6` and

```text
a0^2 = σ = (5/48)(1 − i)(1 + √2),
```

which is not a square in `Q(i,√2)`. Adjoin `α` with `α^2 = σ`. Then `e0,e1` are the unique solution of the `2×2` system `gam,del`, and they lie in `K α`. Direct expansion in the basis `{1,α}` of `K/Q(i,√2)` gives remainder `0` on `gam, del, alp, bet`.

The three linear pivots then produce the coordinates in T1. Direct sparse evaluation of all 22 frozen polynomials at that `K`-point returns remainder `0` on every row, including `Tg12_3,5,7` and the 304-term `Tg14_5`.

### 2.3 The memo’s `S,D,E,F` formulas

At the same point, with `t = rho = 1` and the memo’s definitions
`S = a0 + a1/t`, `D = a0 − a1/t`, `E = e0 + e1/t`, `F = e1/t − e0`:

```text
S^2 =  5/12
D^2 = −(5/12) i
E/S = −2
F/D = −2 i
```

This is exactly the **minus** branch of the displayed system

```text
E = ± 2 sqrt(t cs) S,     F = ± 2 i sqrt(t cs) D,
S^2 = ∓ (5/12) cs^{5/2} k1 t^{5/2},
D^2 = ± i (5/12) cs^{5/2} k1 t^{5/2}.
```

The formulas do **not** fail. They were not, as written, an element of an explicit number field (nested `cs^{5/2}`, `t^{5/2}`, `sqrt(t cs)`, `i`); the tower in T1 is that element, at the specialization `(cs,rho,k1)=(1,1,1)`. Combined with the parametric `λ` of §2.2, they describe a family over `D(cs k1 rho)`, not a single accident. One closed point is what the membership obstruction needs.

### 2.4 Modular samples, and what they are not

The three printed cores are reductions of the same family, after allowing the four sign/λ-branches and the value of `k1`:

| `p` | `k1` | `λ`-branch (first match) | printed `(a0,a1,e0,e1)` | after `k2c,rs1,k10_4` |
|---|---|---|---|---|
| 65521 | 1 | `i(√2+1)` | `(48966, 4891, 3387, 38806)` | all 22 rows `0` |
| 1000033 | 5 | `-i(√2-1)` | `(740566, 154990, 852940, 938172)` | all 22 rows `0` |
| 1000081 | 1 | `-i(√2-1)` | `(18714, 528026, 910186, 183294)` | all 22 rows `0` |

Filled extra coordinates, not printed by the memo:

```text
p=65521:     k2c=60476   rs1=28446   k10_4=17229
p=1000033:   k2c=328895  rs1=610954  k10_4=391951
p=1000081:   k2c=449769  rs1=182618  k10_4=927933
```

All three primes are `1 mod 4`, so `i` exists; that is why the printed samples could exist at all.

What the three `F_p`-points prove, by themselves: the reductions of `I+(k)` at those primes are proper on `D(cs k1 rho)`. Equivalently, they exclude any exact-`Q` membership `f ∈ I` whose reduction at those primes is a unit on the sample (in particular any `cs^a k1^b rho^c` with denominators coprime to `{65521, 1000033, 1000081}`).

What they do **not** prove, and what T1 supplies:

- A characteristic-zero closed point. A smooth `F_p`-point of a reduction need not lift; here it does, but the lift is the tower point, not the samples.
- Exclusion of certificates whose cofactor denominators are divisible by those primes.
- Nonemptiness of a characteristic-zero component, as opposed to three isolated characteristic-`p` coincidences.

The memo’s own modular caveat is therefore correct, and is discharged by T1 rather than by more primes.

### 2.5 What this does to prefix certificates

On `V(k) ∩ D(cs k1)` the frozen prefix is nonempty over `Qbar`, at `rho = 0` (`CS0`) and at `rho ≠ 0` (T1). Root’s M3 (`rho`-torsion as an arc-exclusion certificate) returns negative on both sub-fans. fable5’s slice mechanism `12 e1^2 = 5 cs^4 k ⇒ (k=0 ⇒ e1=0)` is counter-witnessed: T1 has `k=0` and `e1 = −√2(1+i) α ≠ 0`. opus5 Card B’s “restricted fibre empty” branch is false for this prefix; grok Card B’s “some grade `≤ 16` row is a unit on this open” is false for these 22 rows.

Any future `k=0` emptiness or `rho`-torsion job that consumes only the frozen 22 rows is deciding a false statement.

---

## 3. Torsion-multiplier lemma

### 3.1 The identity

Uncontroversial in any commutative ring, and independent of this campaign. The memo’s one-line proof is complete.

### 3.2 What the fibre theorem actually hands the lemma

The promoted grade-14 fibre theorem is a **localized special-fibre** statement: after the `T-cs` substitution, on `qrs = rho = 0` and `D(cs k)`, the grade-10–12 equations force `qc0=qc1=e0=a0=ell1=0` by polynomial identities (already reviewed, not redone), the remaining prefix fibre is the irreducible rational `31`-fold `12 e1^2 = 5 cs^4 k`, and `Tg14_5 = −(7/256) cs^5 k` is a unit there. Hence `V(I_sub + (rho)) ∩ D(cs k) = ∅` over `Qbar`. The promotion itself records that this is a Nullstellensatz / faithful-flatness conclusion and supplies no cofactors.

Weak Nullstellensatz in the Rabinowitsch extension `(I_sub, rho, qrs, 1−u cs, 1−v k)` puts `1` in that extended ideal over `Q`. Clearing `u = 1/cs`, `v = 1/k` (fable5 Lemma A) is elementary and produces some `N, M` with `cs^N k^M ∈ I_sub + (rho)`. This is exactly containment `(C)` of the converse-correction, **not** `cs^N k^M (1+rho W) ∈ I_sub`. Saturation by `cs` and localization at `k` commute with this conclusion in the expected way — both localizers are already paid as left-hand powers — but adjoining `rho` does not: `H` in `cs^N k^M − rho H ∈ I_sub` need not be `cs^N k^M W`.

The memo’s application of the torsion-multiplier is the correct use of `(C)`. It does **not** require, and does not produce, the multiplicative staged type from fibre emptiness alone. That is the whole point of the lemma, and it is why M3 (rho-torsion) upgrades M4 (additive fibre certificate) rather than replacing it.

### 3.3 Honest translation, evenness, radical powers

- **Honest / substituted.** Branch `(a)` is already confirmed in both presentations. Lemma 0 identifies `I_sub` and `K_hon` on polynomials of the substituted ring. `cs^N k^M` and `cs^6 k^2 rho^6` are such polynomials. The existence conclusion lands in `K_hon`.
- **Saturation / localization.** The fibre theorem inverts `cs k`. Rabinowitsch clearing pays those inversions as left-hand powers. No further saturation identity is used. The output `cs^• k^• ∈ K_hon` is already the W=`0` polynomial form that, after saturating by `cs` and localizing at `k`, makes the chart ring zero.
- **Radical powers.** Weak Nullstellensatz gives `1` in the extended ideal, not merely in its radical. Strong Nullstellensatz is not invoked. The “force `qc0=…=0`” step of the fibre theorem is polynomial, not radical, by the drop-`g14` review.
- **Rho-evenness.** Every monomial of every frozen row has even `rho` exponent (zero odd monomials in 22 files). Chart equations are rho-free. For rho-even `f`, `f ∈ J+(rho)` upgrades to `f ∈ J+(rho^2)` by taking even parts (`H_odd = rho H'`). The lemma then applies at `r=3` against `rho^2`-torsion `cs^6 k^2 rho^6`. The memo’s conservative `r=6` against `rho` is still valid and weaker.

### 3.4 Explicitness gap

The memo’s sentence

> “This is the direct total-family certificate, with `W=0`, obtained from the already-promoted fibre theorem plus one hand-checkable four-cofactor identity, with branch `(b)` removed from the argument entirely.”

is true as an **existence** theorem and false as a campaign certificate. Nullstellensatz does not serialize cofactors or `N`. The four-cofactor identity is only branch `(a)`. The object the ledger promotes as `T-cs` is the explicit identity `cs^447 k^164 ∈ K_hon`, which uses branch `(b)` for the displayed exponents and is already independently confirmed. The lemma shows that if branch `(b)` had failed, existence would still stand; it does not make branch `(b)` unwritten.

V19 is mathematically redundant for existence, as the memo says. It is not redundant for a smaller explicit exponent, which the lemma does not compute.

---

## 4. Secondary checks

### 4.1 Grading lattice

The `40 × (sum_rows (t_row − 1))` exponent-difference matrix has `641` homogeneity constraints, rank `38`, nullity `2`. A basis is recorded in the `/tmp` telemetry. The unique-up-to-scale lattice vector with `deg(rho)=0`, normalized by `deg(cs)=2`, is nonnegative on all 40 names and equals the memo’s table:

```text
0: rho
1: ell1
2: cs, ell2, rs
3: cs1, ell3, rs1
4: cs2, ell4, k, rs2
5: a0, a1, c0, c1, cs3, k1, rs3
6: aa0, aa1, cs4, e0, e1, k2c, rs4
7: aaa0, aaa1, ee0, ee1, k10_3
8: ac3, az3, ec3, ez3, k10_4
9: ac4, az4, ec4, ez4
```

Every nonempty frozen row is `deg_s`-homogeneous of degree equal to its grade label (empty `Tg10_6`, `Tg11_6` unconstrained). The `(rho, cs)` pairing of the two-dimensional lattice has determinant `1/2 ≠ 0`, so the only lattice vector with `g(rho)=g(cs)=0` is `0`. Opus5 `deg_2` is not extendable to the frozen row set; the inference `M >= 1` from `deg_2(k)=2` has no replacement in the true lattice and must not be a V19 (or successor) acceptance gate. The surviving `deg_s` inequality for a grade-`14` cofactor, `N + 2M >= 7`, is unconditional and is satisfied by `(447,164)` with slack.

### 4.2 Seven first-jet identities

`D` is the derivation with `D(rho)=0` and `D` shifting each jet tower one step
(`cs↦cs1↦cs2↦cs3↦cs4`, `k↦k1↦k2c↦k10_3↦k10_4`, `c0↦e0↦ee0↦ec3↦ec4`, `c1↦e1↦ee1↦ez3↦ez4`, `a0↦aa0↦aaa0↦ac3↦ac4`, `a1↦aa1↦aaa1↦az3↦az4`, `rs↦rs1↦…`, `ell1↦ell2↦…`). `∂_p` is ordinary differentiation in `p=rho^2` (licensed because every `rho` exponent is even). For `j=1..7`,

```text
Tg11_j − D(Tg10_j) + ell1 ∂_p(Tg10_j)  =  k R_j,    R_j ∈ (c0, c1).
```

```text
R_1 = (5/16) c0 cs + (5/64) c1 rs
R_2 = (5/16) c1 cs rho^2 + (5/64) c0 rs
R_3 = (5/32) c0 cs rho^2 + (5/128) c1 rho^2 rs
R_4 = 0
R_5 = −(5/128) c0 cs rho^4 − (5/512) c1 rho^4 rs
R_6 = 0
R_7 = (5/256) c0 cs rho^6 + (5/1024) c1 rho^6 rs
```

`R_1` and `R_4` match the memo’s displayed residuals. The identities are exact on the frozen bytes. They are navigation plus seven polynomial identities, not a proof engine: they predict where a shifted load term can be a unit, and T1 is the case where it is a unit on `D(cs k1 rho)` and still does not empty the stratum, because one then solves the shifted core rather than obtaining a contradiction.

---

## 5. Smallest sound routing consequence

Do not launch, continue, or re-queue any frozen-prefix job whose success condition is emptiness of `V(k) ∩ D(cs k1 rho)`, or `rho`-torsion on that open, from `Tg10_1..Tg12_7,Tg14_5`. Both sub-fan readings are nonempty in characteristic zero, and T1 is the delayed-load witness.

Do not treat memo §3.1 as a replacement explicit `T-cs` certificate: existence of some `cs^N k^M ∈ K_hon` without branch `(b)` is a Nullstellensatz theorem, already superseded as a certificate by the confirmed identity `cs^447 k^164`. Branch `(b)` is not existence-load-bearing; it remains exponent-load-bearing. Withdraw the `deg_2` / `M>=1` gate before any typing tool consumes it.

No AWS mutation, no campaign launch, no ledger edit, no `jc2-lean` access, no Groebner/Singular. The only repository file written is this one.

---

## Scope firewall

This review does not establish Gate T, either `J2` chart, the terminal receiver, source/landing composition, the off-family `k10=0` sibling as a closed scheme beyond these 22 rows, unexported grade 13 / other grade-14 / higher, V19 exponent quality, AS109, order two, maximum twelve, or JC2. T1 is a statement about the frozen V9/V17 bytes. The torsion-multiplier existence route inherits the fibre theorem’s Nullstellensatz non-constructivity and the frozen rows’ literal-source provenance debt in full.
