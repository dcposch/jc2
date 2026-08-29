# Hostile review: three exact horizontal zero sections of the exported total prefix

**CS0 over `Q[rho]`: CONFIRMED**

**A00 over `Q[rho]`: CONFIRMED**

**A10 over `Q[rho]`: CONFIRMED**

**Witness and negative controls: CONFIRMED**

**Unlocalized `T-cs` chart compatibility at `k=0`: CONFIRMED**

**Stage-two chart compatibility of the source prefix: CONFIRMED**

**Prefix cannot empty those loci or put `rho^N` in the ideal: CONFIRMED**

**No contradiction with localized `T-cs` on `D(cs*k)`: CONFIRMED**

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-p0-total-rees-prefix-zero-sections-producer-sol-20260827.md` |
| Charged claim | The 21 frozen exact-Q V9 actual-total rows `Tg10_1..Tg12_7` and the frozen V17 row `Tg14_5` vanish as polynomials in `Q[rho]` at three assignments `CS0`, `A00`, `A10`; `CS0` is a horizontal section of the unlocalized `T-cs,k=0` prefix; `A00`/`A10` are compatible with the two `J2` charts over `A/J1`; this prefix alone cannot empty those fibres or make `rho` nilpotent |
| Producer status | `EXACT SOURCE-PREFIX RESULT, AWAITING DIFFERENT-MODEL HOSTILE REVIEW.` SHA-256 `0ca4647acecbff0181478c98cbbec15c932beeba0a106df1d085958aaebf3fb0` |
| Reviewer / model | Grok 4.6 (xAI). Hostile different-model reread. Producer stdout, the producer AST replay, and AWS output were not trusted |
| Method | Independent SHA-256 of the 22 frozen `.poly` bytes, the preregistration, the replay file, and the two charged promotions; sparse monomial parse of Singular-style terms (bare `a/b` and parenthesized `(a/b)` coefficients, word-boundary identifiers, exponents `var^n`); exact `Fraction` evaluation to sparse `Q[rho]`; monomial-support census; monomial-level `T-cs` chart `rs -> cs*qrs`, `c0 -> cs*qc0`, `c1 -> cs*qc1`. No Groebner basis, no heavy local CAS, no AWS mutation, no `jc2-lean`, no web, no execution of `replay_prefix_zero_sections.py` |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-27 |

The three assignments are genuine zeros of the frozen prefix over the rho-line, not sampled points. One such horizontal section is enough to retire any emptiness or global `rho`-torsion attempt that uses only these 22 rows and the stated chart relations. It licenses nothing about unexported source, the localized `T-cs` fibre on `D(cs*k)`, or either full `J2` chart.

---

## Verdicts

| Claim | Verdict | Residual / reason |
|---|---|---|
| Preregistration / replay SHA pins | **CONFIRMED** | `1c4661ac689443184478333755ace8d1ad28b06449dc65ba66d612df3325a815`, `9eb848f034bb7513e50790e9eb896866454cd439a11ac67fba541bb14c657bc0` |
| All 22 input SHA-256 pins, including `Tg10_2`, `Tg10_4`, `Tg14_5` | **CONFIRMED** | Independent `sha256` of the frozen bytes; matches V9 `COEFFICIENTS.json` and V17 `coefficient_sha256` |
| `CS0`: `cs=1`, `k=0`, other source names `0`, `rho` free | **CONFIRMED** | All 22 residuals are the zero polynomial in `Q[rho]` |
| `A00`: `a0=1`, `J1=(rs,cs,c0,c1)=0`, other names `0`, `rho` free | **CONFIRMED** | All 22 residuals `0` in `Q[rho]` |
| `A10`: `a1=1`, `J1=0`, other names `0`, `rho` free | **CONFIRMED** | All 22 residuals `0` in `Q[rho]` |
| Witness `cs=e1=1`, `k=12/5`, `rho=0` | **CONFIRMED** | `Tg12_2 = 0`, `Tg14_5 = -21/320`; all 21 prefix rows `0` |
| Negative control `cs=k=1`, `e1=rho=0` | **CONFIRMED** | `Tg12_2 = -5/128 ≠ 0` |
| `T-cs` bilinears + `1-u*cs` at `CS0` | **CONFIRMED** | `qrs=qc0=qc1=0`, `u=1` give `rs-cs*qrs=c0-cs*qc0=c1-cs*qc1=1-u*cs=0`; charted rows still `0` |
| `1-v*k` at `CS0` | **CONFIRMED** as impossible | `k=0` forces `1-v*k=1` for every `v` |
| `a0`-chart relation at `A00` | **CONFIRMED** | `a1-a0*qa1=0` at `(a0,qa1)=(1,0)` |
| Ordered `a1`-chart at `A10` | **CONFIRMED** | `(a0,a1)=(0,1)` and `a0-a1*qa0=0` at `qa0=0` |
| Horizontal, not merely special, section | **CONFIRMED** | Residuals vanish as polynomials in `rho`, not at a sample; monomial support in `{cs,rho}`, `{a0,rho}`, `{a1,rho}` is empty |
| These 22 rows + stated chart relations cannot empty the named fibres or put `rho^N` in the prefix ideal | **CONFIRMED** | A `Q[rho]`-point (resp. its `rho=0` slice) is a zero of every generator |
| Compatibility with staged calculus and localized `T-cs` fibre | **CONFIRMED** | `CS0` lies in residual `V(k)`, off `D(cs*k)`; promoted fibre emptiness is untouched |
| Unexported grade-13 / other grade-14 / higher rows vanish | **GAP** | Not in the frozen prefix; producer correctly does not claim it |
| `k=k10` is the registered common localizer / post-`M=0` family | **GAP** | Operational routing hypothesis; not implied by the 22 rows |
| Full `J2` charts empty or nonempty after uncompiled stage-two equations | **GAP** | Source prefix only |
| Every associated prime of the prefix is `rho`-torsion-free | **GAP** | One horizontal section kills only a global `rho^N=0` certificate |

---

## Narrow reusable theorem

Work in the ordinary polynomial ring over `Q` on the 40 names occurring in the frozen bytes

```text
a0 a1 aa0 aa1 aaa0 aaa1 ac3 ac4 az3 az4
c0 c1 cs cs1 cs2 cs3 cs4
e0 e1 ec3 ec4 ee0 ee1 ell1 ell2 ell3 ell4 ez3 ez4
k k1 k10_3 k10_4 k2c rho
rs rs1 rs2 rs3 rs4
```

Let `Tg10_1,...,Tg12_7` be the frozen exact-Q V9 files and `Tg14_5` the frozen exact-Q V17 file (byte hashes below). Chart names `qrs,qc0,qc1,qa0,qa1,u,v` do not occur in those files. Then:

1. **`CS0`.** The assignment that sends `cs` to `1`, `k` to `0`, and every other name except `rho` to `0`, with `rho` an indeterminate, evaluates all 22 polynomials to `0` in `Q[rho]`. After the word-boundary chart `rs=cs*qrs`, `c0=cs*qc0`, `c1=cs*qc1`, the same holds at `qrs=qc0=qc1=0`. The affine localizer `1-u*cs` vanishes at `u=1`. Because `cs=1` is a unit, saturation of the Rees bilinears at `cs` does not cut the point out. Restricting `rho=0` yields a rational point of the special fibre of this unlocalized `k=0` prefix. The structure map to `Spec Q[rho]` therefore has a section, so the prefix ring admits `Q[rho]` as a quotient: it is not the unit ideal after `k=0`, and no power of `rho` lies in the ideal of the 22 rows plus those chart relations.

2. **`A00`.** After the base change `J1=(rs,cs,c0,c1)=0`, the assignment `a0=1` and every other source name except `rho` equal to `0` again sends all 22 rows to `0` in `Q[rho]`. The standard `a0`-chart relation `a1=a0*qa1` holds at `(a0,qa1)=(1,0)`. Saturation at `a0` is vacuous at this unit point.

3. **`A10`.** After the same base change, `a1=1` and every other source name except `rho` equal to `0` sends all 22 rows to `0` in `Q[rho]`. The ordered `a1` chart `V(a0) ∩ D_+(a1)` contains `(a0,a1)=(0,1)`, and `a0=a1*qa0` holds at `qa0=0`.

4. **Controls.** At the independently promoted localized-fibre point `cs=e1=1`, `k=12/5`, `rho=0` (and `u=1`, `v=5/12`, `qrs=qc0=qc1=0`), every grade-10--12 row vanishes and `Tg14_5=-21/320`. At `cs=k=1`, `e1=rho=0`, the same parser returns `Tg12_2=-5/128`. The evaluator is therefore not the zero map, and it recovers the reviewed fibre witness.

Consequently: do not attempt a special-fibre-emptiness or global `rho`-torsion certificate for `k=0` or for either pure `J2` direction from this prefix alone. The localized theorem on `D(cs*k)` is a different object; `CS0` is not a point of it, because `1-v*k` cannot vanish at `k=0`.

---

## 1. Custody and SHA pins

Independently recomputed. Producer pins for the preregistration and replay match. Every V9 `Tg*.poly` named in `COEFFICIENTS.json` rehashes. V17 `coefficient_sha256` matches the file.

| Artifact | SHA-256 |
|---|---|
| preregistration | `1c4661ac689443184478333755ace8d1ad28b06449dc65ba66d612df3325a815` |
| replay script | `9eb848f034bb7513e50790e9eb896866454cd439a11ac67fba541bb14c657bc0` |
| producer report | `0ca4647acecbff0181478c98cbbec15c932beeba0a106df1d085958aaebf3fb0` |
| staged-calculus promotion | `16ec6f54e80a420755a52b8d2068390b65344311a5f84c4d486192513a928867` |
| `T-cs` fibre promotion | `5fd19f3577fbd24e74f2c395ab6fd17f84d75f73e00eeae53267536c33265fd4` |
| fibre-witness hostile review (corroboration of `-21/320` only) | `7fbd9423b6840e4f3017687897e0dad373a04d2683589ccb432682553053c3cf` |
| fibre-witness producer (named, not re-trusted) | `d9e5f43954240eee13311c5f386231f9ed506c4bbe978211cdfa711e3e8c86d9` |
| V9 exact-Q `COEFFICIENTS.json` | `86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e` |
| V17 exact-Q `RESULT.json` | `25d40556618983a350eda99d4fb6aae8d1e5cd2cf328041963b46d61729af543` |
| `Tg14_5_q.poly` | `91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7` |

Exact-Q V9 row files:

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

`Tg10_6.poly` and `Tg11_6.poly` are the literal two-byte file `0\n`. Independent sparse term counts of the 22 files are

```text
4,5,5,2,5,0,5 | 12,14,17,3,18,0,18 | 27,36,47,12,58,9,60 | 304
```

matching the previously reviewed monomial census (empty polynomial counted as `0`, not `1`) and V17 `coefficient_term_counts` for the four row-5 files. V9 `COEFFICIENTS.json` SHA pins match the bytes. Its `coefficient_term_telemetry` field is off-by-one on four nonzero rows (`Tg10_5,Tg11_5,Tg12_4,Tg12_5`); that field is not an input to this claim. `python3 -m py_compile` of the replay file succeeds as a syntax check; the replay was not executed.

---

## 2. Independent parse and `Q[rho]` evaluation

Parser: signed Singular terms; coefficients `num/den` or `(num/den)` / `(-num/den)`; identifiers `[A-Za-z_][A-Za-z0-9_]*`; exponents `var^n`; no `eval`, no Python AST, no producer `Poly` class. Every character of every file was consumed. A second, sign-splitting term count (parenthesized coefficients masked) agrees on all 22 files, including `Tg14_5 = 304`. Forbidden names `{ideal,poly,std,ring,eval,exec}` do not occur. Chart-prefix identifiers `{rs1,rs2,rs3,rs4}` are present and were never rewritten as `rs`.

Unspecified source names default to `0`. `rho` is kept as a polynomial generator except in the two controls, where it is the constant `0`. This is the preregistered arithmetic: 66 residual polynomials, all required to be zero, plus two controls.

Exact residuals, raw evaluation:

| assignment | 21 V9 rows | `Tg14_5` |
|---|---|---|
| `CS0` | `0` in `Q[rho]` | `0` in `Q[rho]` |
| `A00` | `0` in `Q[rho]` | `0` in `Q[rho]` |
| `A10` | `0` in `Q[rho]` | `0` in `Q[rho]` |
| witness | `0` (constants) | `-21/320` |
| negative (`Tg12_2` only) | — | `Tg12_2 = -5/128` |

Charted evaluation of `CS0` (substitute `rs -> cs*qrs` etc. at monomial level, then assign `qrs=qc0=qc1=0`, `cs=1`, `k=0`) agrees with the raw evaluation: all 22 rows `0` in `Q[rho]`. The same for the witness, where `qrs=qc0=qc1=0` forces `rs=c0=c1=0`.

Monomial support, stronger than substitution: no frozen term has variables contained in `{cs,rho}`, `{a0,rho}`, or `{a1,rho}`. There is no pure-`rho` term and no constant term. The origin (everything `0` except `rho`) is also a zero of the 22 rows; it is not a `T-cs` chart point, because `cs=0` leaves `D_+(cs)`.

`k=0` is load-bearing for `CS0`. Terms with support in `{cs,k,rho}` that survive if `k` is left free:

```text
Tg10_1  (5/16) cs^3 k rho^2
Tg10_3  (5/32) cs^3 k rho^4
Tg10_5  (-5/128) cs^3 k rho^6
Tg10_7  (5/256) cs^3 k rho^8
Tg12_2  (-5/128) cs^4 k
Tg12_6  (15/128) cs^4 k rho^4
Tg14_5  (-1/128) cs^5 k
```

All die at `k=0`. `J1=0` is load-bearing for `A00`/`A10`: e.g. `Tg12_4` contains `(-3/32) rs a0^2` and `Tg12_1` contains `(-3/8) cs a1^2`. Those are not `{a0,rho}` or `{a1,rho}` terms.

Hand check of the two controls from surviving monomials of `Tg12_2` and `Tg14_5` with support in `{cs,e1,k}` and no `rho`:

```text
Tg12_2 = (-5/128) cs^4 k + (3/32) e1^2
  witness:  (-5/128)(12/5) + 3/32 = -3/32 + 3/32 = 0
  negative: (-5/128)(1)(1) + 0    = -5/128

Tg14_5 |_{rho=0, only cs,e1,k} = (-3/64) cs e1^2 + (-1/128) cs^5 k
  witness: -3/64 + (-1/128)(12/5) = -3/64 - 3/160 = -15/320 - 6/320 = -21/320
```

These are the same two-term restrictions used in the promoted `T-cs` fibre identity. The producer witness is that point with `e1=0` dropped and `k` set to `0` for `CS0`, or with `J1` and `e1` killed for the `A` sections.

---

## 3. Attack: unexported rows

The frozen consumed set is exactly the 21 V9 `Tg` files at grades 10--12 and V17 `Tg14_5`. V9 also writes even-sheet `Fg*` coefficients and `KeepT*`/`KeepF*` remainders in the same compiled directory; those are not in the preregistration. No `Tg13_*` file exists. No other grade-14 actual-total row is exported (V17 is row 5 only). The V17 different-model review already recorded that grade 13 is present in the literal source (141 terms) and is neither exported nor bridged.

The producer firewall is therefore the correct scope: this result says nothing about other grade-13/14 rows, higher grades, or the full source ideal. That is a GAP on those larger objects, not a defect in the charged claim.

Out of charged scope, the 21 `Fg*` files and the six `Keep*.poly` files in the same V9 directory also evaluate to `0` in `Q[rho]` at `CS0`, `A00`, and `A10`. Adjoining those particular extra V9 artifacts would not save an emptiness attempt. This is not a promotion of a larger prefix: grade-13 source and the other grade-14 rows remain unexported, and were not parsed.

---

## 4. Attack: Rees bilinears and saturation

Staged calculus presents the `i`th standard chart as

```text
A[y_j : j≠i] / ((f_i y_j - f_j : j≠i) : f_i^∞).
```

For `T-cs`, `f_i=cs` and the ratios are `qrs,qc0,qc1`. At `CS0`:

```text
rs - cs*qrs = 0,   c0 - cs*qc0 = 0,   c1 - cs*qc1 = 0,
1 - u*cs    = 0,   cs = 1 ≠ 0.
```

The point lies on the unsaturated bilinear locus with `cs` a unit, hence on the saturation. Ordered-stratum equation `qrs=0` (least-index complement of `T-rs`) holds. Extra zeros `qc0=qc1=0` are an assignment, not extra chart generators; they are compatible.

The V18 localizer `1-v*k` is not among the stated `CS0` relations, and cannot be imposed: `k=0` makes `1-v*k=1` identically. So `CS0` is a point of the unlocalized chart prefix, and is not a point of the localized V18/V18R1 special fibre whose emptiness on `D(cs*k)` is the promoted `T-cs` fibre theorem. Saturation at `cs` does not identify those two objects.

For `J2` over `A/J1`, the `a0` chart is `(a0*qa1-a1):a0^∞` and the ordered `a1` chart is `V(a0) ∩ D_+(a1)`, equivalently `(a1*qa0-a0):a1^∞` with `a0=0`. Both unit points above lie on those presentations. No stage-two source equation beyond the 22 rows is present, so this is chart-relation compatibility of the source prefix, not a theorem about the compiled `J2` charts.

Merely rewriting the same 22 rows in a different standard chart of `J1` or `J2` cannot delete the three sections, because each section was checked against the chart in which it is claimed to live. Changing the blown-up ideal, adding a genuine localizer that vanishes on the section, or adding new source rows can. The producer's sentence “merely changing the Rees chart cannot make the three horizontal source-prefix sections disappear” is accepted only in that narrow reading.

---

## 5. Attack: horizontal versus special section

A special-fibre point is a zero at `rho=0`. A horizontal section is a `Q[rho]`-algebra map from the prefix ring onto `Q[rho]`, i.e. a zero for every value of `rho`. The producer claims the latter, and that is what the bytes give: the 66 residuals are the zero polynomial, not a sample.

`CS0` at `rho=0` is then a special-fibre point of the unlocalized `k=0` prefix, so that fibre is nonempty and no Nullstellensatz certificate can exist from these generators. The same section shows `rho^N` is not in the ideal, so there is no global `rho`-torsion certificate in this prefix ring.

That is strictly weaker than “every associated prime is `rho`-torsion-free” or “there is no component supported at `rho=0`”. A further localization that kills `CS0` could in principle leave a `rho`-torsion piece. The producer does not claim those stronger statements; the ideation language about “no rho-torsion certificate without additional source rows” is the global-identity reading, which is confirmed.

The promoted `T-cs` fibre theorem lives on `qrs=rho=0` and `D(cs*k)`, where the grade-10--12 prefix is a rational 31-fold and `Tg14_5=-(21/320)cs e1^2 ≠ 0`. `CS0` has `k=0` and `e1=0`, so it is excluded by the genuine localizer `k` and is not a counterexample to that theorem. Staged calculus already retains residual `V(s)` strata; here `s` involves `k`. The producer firewall that this neither weakens promoted `T-rs`, `T-c0`, ordered `T-c1`, nor localized `T-cs` is correct.

---

## 6. Attack: overstated consequences

**Consequence 1.** Do not launch a `k=0` emptiness or `rho`-torsion computation using only these 22 rows. Confirmed as a mathematical prohibition: any such computation is deciding a false statement. It does not prohibit a later attempt that adds genuinely new exported rows or a source-selection equation.

**Consequence 2.** Do not expect this prefix to delete either `J2` chart. Confirmed for the source prefix and the stated chart relations. Uncompiled stage-two equations remain a GAP.

**Consequence 3.** Source/coverage audit of a common localizer `k=k10` on a post-`M=0`, unit-`k10` family. This is campaign routing, not a theorem of the 22 rows. The algebra shows `k=0` survives the prefix; it does not identify `k` with `k10` or decide the registered source-family scope. Verdict: **GAP** as a mathematical claim; retained as an operational nonclaim.

**Consequence 4.** “The second-stage successor must first export source rows that can see pure `a0/a1`, or prove a routing/receiver theorem.” Operational, not forced by the algebra beyond the weaker fact that *these* rows do not see the pure directions. The second sentence, narrowly read as in §4, is confirmed.

No consequence claims Gate T, order two, maximum twelve, or JC2. The producer does not treat `PASS` as a point of an uncompiled Rees chart in the sense of a full staged certificate; it treats it as a source-prefix section compatible with the named chart relations. That line is held.

---

## 7. Findings

### High

None that change a verdict.

### Medium

None that change a verdict.

**M1. “Merely changing the Rees chart.”** The broad reading (arbitrary change of blown-up ideal, extra localizers, extra generators) is false and is not licensed. The narrow reading (standard staged `J1`/`J2` presentations of this same prefix) is confirmed in §4. The producer’s surrounding sentences already demand new source rows or a routing theorem; the isolated sentence is sloppy, not load-bearing.

### Low

**L1. V9 term telemetry.** `COEFFICIENTS.json` reports `Tg10_5=6`, `Tg11_5=19`, `Tg12_4=13`, `Tg12_5=59` against actual sparse counts `5,18,12,58`. SHA pins and the V17 row-5 counts match the bytes. Harmless census drift; already visible against the fibre-witness monomial census.

**L2. Witness point vs producer display.** The promoted fibre point also has `u=1`, `v=5/12`. The producer replay assigns only `cs,e1,k,rho` for the control, which is enough because `u,v` do not occur in the source bytes. No algebraic effect.

**L3. `py_compile` is not evidence of the identities.** Syntax of the untrusted replay is fine. The identities were re-proved by an independent monomial parser.

---

## Accepted theorem

On the frozen exact-Q V9 rows `Tg10_1,...,Tg12_7` and the frozen exact-Q V17 row `Tg14_5`:

- `CS0` (`cs=1`, `k=0`, other source names `0`, `rho` free) is a `Q[rho]`-zero of all 22 polynomials, remains a zero after the `T-cs` bilinears with `qrs=qc0=qc1=0` and `1-u*cs=0`, and therefore is a horizontal section of that unlocalized `k=0` prefix. Its special-fibre slice is nonempty, and `rho` is not nilpotent in the prefix ring.
- `A00` and `A10` are `Q[rho]`-zeros of the same 22 polynomials on `V(J1)`, compatible with the standard `a0` chart and the ordered `a1` chart respectively.
- The reviewed controls hold: `Tg12_2=0`, `Tg14_5=-21/320` at `cs=e1=1`, `k=12/5`, `rho=0`; `Tg12_2=-5/128` at `cs=k=1`, `e1=rho=0`.

No emptiness or global `rho`-torsion certificate for those three loci can be written from this prefix and the stated chart relations.

## Nonclaims (not accepted)

- Any unexported source row (grade 13, other grade-14 rows, higher grades, full source ideal, source-family coverage).
- A point of a fully compiled Rees chart including unwritten stage-two equations, saturation identities not checked here, or additional genuine localizers.
- Emptiness or nonemptiness of the localized `T-cs` special fibre on `D(cs*k)` (already a separate promoted theorem; `CS0` is off that open).
- Weakening of promoted `T-rs`, `T-c0`, ordered `T-c1`, or localized `T-cs`.
- Identification of `k` with `k10`, post-`M=0` custody, or any load-timing fan owner.
- Associated-prime / embedded-component analysis of the prefix.
- A formal or algebraic arc, a Keller pair, Gate T, all order two, maximum twelve, JC2, TD6, AS109, or any Lean statement.

`jc2-lean` was not accessed. No AWS state was mutated. No campaign computation was launched. The only repository file written is this review.
