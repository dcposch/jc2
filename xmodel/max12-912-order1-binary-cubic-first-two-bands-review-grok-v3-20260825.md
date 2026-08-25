# Hostile V3 review — fixed-D12 `(9,12)` order-one binary-cubic first bands

| Field | Value |
|---|---|
| Producer | `xmodel/max12-912-order1-binary-cubic-first-two-bands-aws-20260825.md` (SHA-256 `2a185d6dabec5c47c16be2779c45e351f9658abe8fc8140de91c4d83a9407fb7`) |
| Frozen case | `cases/max12_912_order1_binary_cubic_bands_aws_20260825/` |
| Active manifest | `MANIFEST.postrun.v3.sha256` (SHA-256 `38466426e3a0b113a4cbd71b447d9a44b01482bcd3e3acea4879cad96589a8e3`) |
| Active freeze | `FREEZE.v3.sha256` (SHA-256 `b4374cb2395cadb1c4755432dd7087dd19f44e4ac1e21265054a38aa429354d5`) |
| Count correction | `CUSTODY_MANIFEST_COUNT_CORRECTION.md` (SHA-256 `d7c6caa33c6879b321acd838c922ea2f655d01a267912f3ed3190860d4b5c9ec`) |
| Nine-charge prompt | `xmodel/max12-912-order1-binary-cubic-first-two-bands-review-grok-20260825-prompt.md` (SHA-256 `c7fe6dae6e5b79c38751c2a664201557817f78362d27b9ca978b333e96344c5b`) |
| Overall verdict | **CONFIRMED_WITH_REPAIRS** |
| Mathematics | **CONFIRMED** at first-two-band scope |
| Custody | **CONFIRMED** of the V3 fail-closed root; V1 harvest list and V1 freeze are documented fail-open negative controls |
| Wording / scope | **REPAIRED.** The producer still names V1 `MANIFEST.postrun.sha256` as the active post-harvest object. That sentence is false under the V3 root |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Promotion-eligible V3 attempt. V1/V2 review attempts are 72-byte adapter logs only |
| Evidence | source reading of compiler, SAT interface, launcher, preregistration, and all custody notes; independent SHA-256 of named roots and of every V3 record; `LC_ALL=C` `shasum -c` of V1/V2/V3 manifests and freezes; byte comparison of dual-host algebraic artifacts; hand Euler/Wronskian identities, PGL2 normal forms, `K^3`/`K^4` expansions, perturbed-top brackets, and 3-adic term valuations; schoolbook integer discriminant of the literal SAT cubic. No local Singular, Sage, solver, compiler rerun, or rref |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (producer and case uncommitted) |
| Review window | 2026-08-25 |

V1 and V2 review attempts are diagnostics only. Each log is 72 bytes, SHA-256 `ff028592504c7e4cd6f0c06e70f952247a2b0162f98a0c70e570a67d8d5b60d9`, and contains no charge. They are FAILED CLOSED.

## Verdict

**CONFIRMED_WITH_REPAIRS**

The frozen AWS compilation of the three displayed representatives is internally complete for the first two denominator-free homogeneous bands, and the printed Singular dimensions 7/6/6 are the dimensions of those obstruction schemes, not of any Keller branch. The literal mod-`3^11` cubic `(1,119880,40581,0)` has `v_3(Disc)=15` for every integral continuation of that 4-tuple, so any exact continuation is squarefree; that does not produce a continuation. Fixed total degree 12 separately collapses the partial-`y` Kummer class to order one and is a SCOPE-CONFLICT with selected order-three Q8; it does not identify the total-homogeneous cubic `K` with the partial-`y` coefficient `h(x)`.

The only load-bearing repairs are custody wording. V3 is a fully fail-closed, custody-only overlay of an otherwise intact harvest. Promote the mathematics only together with the corrected active-root sentences below.

## Strongest exact claim

Work over an algebraically closed characteristic-zero field, after licensed constant normalization `P9=K^3`, `Q12=K^4`, on the three PGL2 root-multiplicity representatives `K=y^3`, `K=xy^2`, `K=xy(x-y)`. The degree-19 bracket is identically zero. The complete degree-18 map is `19×21` of rank/kernel `11/10`, `12/9`, `12/9`; the complete degree-17 fresh map is `18×19` of rank/kernel/cokernel `10/9/8`, `11/8/7`, `11/8/7`. Projecting `[P8,Q11]` from the full degree-18 kernel onto the full left cokernel yields 6, 6, and 7 nonzero quadrics of `Q`-span rank 6, 6, and 6. Singular, consuming exactly those primitive generators without radicalization, reports dimensions 7, 6, and 6 and returns nonunit nonreduced standard bases.

Separately, for the frozen SAT witness of SHA-256 `a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a` with coefficients `(1,119880,40581,0)`, every integral lift of the last three coefficients by multiples of `3^11` has `v_3(Disc)=15≠∞`, hence type `LMN`, **conditional on an exact continuation existing**. Independently of that cubic, a total-degree-`≤12` pair on the reviewed `(9,12)` partial-`y` route has constant `b12=h^4`, hence constant `h` and Kummer order one after the licensed scalar extension.

## Sharpest non-claim

First-two-band affine geometry on three leading-form representatives, plus a conditional root-type for one finite 4-tuple, plus a partial-`y` Kummer-order statement that does not constrain `K`. Not an all-depth lift, not a composition of lower determinant bands for the SAT witness, not emptiness or survival of any full binary-cubic stratum, not a `PGL2(Z_3)` statement, not a selected-Q8 landing, not maximum twelve, not a counterexample, and not JC2.

---

## Custody — 102 V3 records, 96+7 V1 harvest, fail-closed status

**CONFIRMED** that V3 is fully fail-closed and that the count-correction is custody-only.

`LC_ALL=C LANG=C shasum -a 256 -c MANIFEST.postrun.v3.sha256` reports 102 `OK` lines, zero `FAILED`, zero malformed lines, exit 0. `FREEZE.v3.sha256` reports 5 `OK` lines, exit 0, and pins the V3 manifest, the count-correction, `FREEZE.v2.sha256`, `MANIFEST.postrun.v2.sha256`, and the producer.

V3 line count is exact: 12 case-root records (count-correction, erratum, supplement, V1 freeze, V2 freeze, V1 manifest, V2 manifest, preregistration, README, `compile_bands.py`, `compose_sat_interface.py`, `run_aws.sh`) plus 90 evidence files (14 per triple/double lane on two hosts, 17 per squarefree lane). The only case-root file not in the 102 is `FREEZE.v3.sha256` itself, which is the freeze root and must not be self-included.

Layering:

| object | physical lines | valid SHA-256 records | other lines |
|---|---:|---:|---:|
| `MANIFEST.postrun.sha256` | 103 | 96 | 7 Perl locale warnings |
| `FREEZE.sha256` | 12 | 5 | same 7 warnings |
| `MANIFEST.postrun.v2.sha256` | 99 | 99 | 0 |
| `FREEZE.v2.sha256` | 5 | 5 | 0 |
| `MANIFEST.postrun.v3.sha256` | 102 | 102 | 0 |
| `FREEZE.v3.sha256` | 5 | 5 | 0 |

V2 adds exactly the V1 erratum, V1 freeze, and V1 manifest to the 96 harvest records. V3 adds exactly the count-correction, V2 freeze, and V2 manifest. No evidence, compiler, or result byte is added after harvest. That is custody-only.

V1 `shasum -c` on the old manifest reports `WARNING: 7 lines are improperly formatted`, 96 `OK`, 0 `FAILED`, **exit 0**. The same pattern holds for V1 `FREEZE.sha256`. macOS/`perl` `shasum -c` does not fail-close on leading garbage. The seven warning lines are:

```text
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LC_ALL = "C.UTF-8",
	LC_CTYPE = "C.UTF-8",
	LANG = "C.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
```

`CUSTODY_MANIFEST_ERRATUM.md` correctly quarantines those lines and incorrectly says the old manifest contains 89 valid records. The arithmetic is `96-7=89` (subtracting warnings from the valid count) instead of `103-7=96`. The immutable count-correction repairs the stated count to 96 and changes no mathematics. All 96 V1 records verify.

**Corrected V1-erratum sentence:** `MANIFEST.postrun.sha256` contains 96 valid SHA-256 records plus seven leading Perl locale-warning lines, for 103 physical lines. `shasum -c` warns on the seven lines and still exits 0; it is not fail-closed. All 96 valid records verify. The stated count 89 is false.

**Corrected producer custody sentence:** The remote `OUTPUT.sha256` files are quarantined negative controls (Charge 6). The active byte manifest is `MANIFEST.postrun.v3.sha256`, SHA-256 `38466426e3a0b113a4cbd71b447d9a44b01482bcd3e3acea4879cad96589a8e3`, with custody root `FREEZE.v3.sha256`, SHA-256 `b4374cb2395cadb1c4755432dd7087dd19f44e4ac1e21265054a38aa429354d5`. `MANIFEST.postrun.sha256` and `CUSTODY_SUPPLEMENT.md` remain immutable V1 harvest documents and are not the active root.

---

## Charge 1 — `P9=K^3,Q12=K^4` and three PGL2 representatives

**CONFIRMED**

Over an algebraically closed characteristic-zero field, a nonzero binary cubic is a product of three linear forms. The geometric types are exactly `L^3`, `L^2M`, and `LMN`, separated by whether the discriminant vanishes and whether the cubic is a cube. `PGL2` sends those types to the displayed representatives

```text
triple [1,0,0,0]       K = y^3,
double [0,1,0,0]       K = x y^2,
squarefree [0,-1,1,0]  K = x^2 y - x y^2 = x y (x-y),
```

with coefficient index `i` the `x`-exponent. Frozen `P9`/`Q12` match the hand expansions `y^9`, `x^3 y^6`, `x^3 y^3(x-y)^3` and `y^{12}`, `x^4 y^8`, `x^4 y^4(x-y)^4`.

Euler identity: `[K^n,K^m] = n m K^{n+m-2}[K,K]=0`, so `[P9,Q12]=0` identically. Frozen `top_zero=true` and `top_row_count=20`.

Attacks, and why they are not missing charts inside the claim:

- **Zero cubic / leading-form degree drop.** `K=0` makes `P9=Q12=0` and is excluded by “nonzero binary cubic”. Maps whose actual leading degrees drop below `(9,12)` are a different stratum and are not claimed.
- **Scalar chart.** `K ↦ λK` scales `P9` by `λ^3` and `Q12` by `λ^4`. Independent constant source/target scalings absorb those factors and leave the linear maps equivalent. The package fixes one representative per type.
- **Non-closed fields.** A cubic need not split (e.g. over `R`). Exhaustiveness is claimed only after the stated algebraic closure.
- **Characteristic `p`.** The identity `[K^3,K^4]=0` survives, but `PGL2` classification and later Wronskian arguments do not. The package is characteristic zero.
- **Closure intersections.** The types of a given `K` are disjoint. The closure of `LMN` contains `L^2M` and `L^3`. The package does not classify the degeneration of the `LMN` obstruction scheme to the boundary; it compiles three separate representatives.
- **`PGL2(Z_3)` / B9 residue chart.** Preregistration and the firewall refuse both. Linear source changes preserve total-degree faces, so invariant numerical data (ranks, dimensions) of a type may be read from one representative; the printed generators are representative-dependent and are not claimed `PGL2`-canonical.
- **Opposite affine chart `K=x^3`.** `PGL2`-equivalent to `y^3`. Not a fourth type.

The claim is the leading-form ansatz `P9=K^3`, `Q12=K^4`, not a classification of all `(9,12)` maps.

---

## Charge 2 — degree-19/18/17 bands, counts, sign convention

**CONFIRMED**

Homogeneous `[F,G]` has degree `deg F+deg G-2` and `deg F+deg G-1` coefficients. Direct expansion

```text
[x^i y^{a-i}, x^j y^{b-j}] = (i b - a j) x^{i+j-1} y^{a+b-i-j-1}
```

equals `F_x G_y - F_y G_x`. The identity is denominator-free. Index `i` is the `x`-exponent throughout compiler, matrices, and representatives; the opposite `y`-exponent convention is not used.

| band | form | rows | columns | frozen |
|---|---|---:|---:|---|
| 19 | `[P9,Q12]=0` | 20 | 0 (leading forms fixed) | `top_row_count=20`, identically zero |
| 18 | `[P9,Q11]+[P8,Q12]=0` | 19 | 9+12=21 | `band1` `19×21` |
| 17 fresh | `[P9,Q10]+[P7,Q12]` linear in `(P7,Q10)` | 18 | 8+11=19 | `band2_fresh` `18×19` |

All 9 coefficients of `P8`, 12 of `Q11`, 8 of `P7`, and 11 of `Q10` are assembled. No Q8 divided row, Kummer root, Taylor row, or terminal row is an input. Internal rref uses `fractions.Fraction`; emitted obstruction generators are primitive integers (denominator LCM, content gcd, sign normalized on the least monomial). Boundary bracket indices `i=j=0` and `i=a,j=b` have prefactor zero, so the implementation’s `exponent>=0` guard never drops a nonzero term. The dictionary derivative implementation is checked on every assembled column and on every quadratic source.

The quadratic `[P8,Q11]` is not a fresh linear column at degree 17; it is the bilinear source from the degree-18 kernel, projected in Charge 3. That is completeness of the first two lower bands, not an omitted linear variable.

---

## Charge 3 — ranks, kernels, cokernels, projected quadrics, `equation_span_rank`

**CONFIRMED** from complete source construction plus frozen AWS numbers. Local rref was not rerun.

Rank-nullity on the frozen JSON/stdout:

| type | band1 rank+ker | band2 rank+ker / rank+coker | parameters | nonzero quadrics / span rank |
|---|---|---|---:|---|
| `L^3` | 11+10=21 | 10+9=19 / 10+8=18 | 10 | 6 / 6 |
| `L^2M` | 12+9=21 | 11+8=19 / 11+7=18 | 9 | 6 / 6 |
| `LMN` | 12+9=21 | 11+8=19 / 11+7=18 | 9 | 7 / 6 |

Matrix shapes are `19×21` and `18×19` with kernel vectors of length 21 and left-cokernel vectors of length 18, counts matching the dimensions.

Construction attacks:

- **Kernel orientation.** `nullspace` puts `1` on rref-free columns. The `s_i` are that basis. The printed generators depend on it; Krull dimension does not. The producer treats the standard bases as frozen evidence, not as a normal form.
- **Bilinear expansion.** For `P8=∑ s_i p_i`, `Q11=∑ s_j q_j` the coefficient of `s_i s_j` is `[p_i,q_j]+[p_j,q_i]` (`i≠j`) and `[p_i,q_i]` (`i=j`). The double loop does exactly that. No omitted cross term.
- **Cokernel completeness.** Every left-kernel vector of the fresh matrix is used. Zero projections are dropped (`0=0`), not omitted obstructions. Triple: 8 cokernel vectors, 6 nonzero quadrics. Double: 7 and 6. Squarefree: 7 and 7.
- **Duplication / `equation_span_rank`.** This is the `Q`-rank of the coefficient matrix of the nonzero projected quadrics as vectors of monomial coefficients. It is not Krull dimension, not `INPUT_GENERATORS`, not `GB_GENERATORS`, and not `parameter_count - span_rank`. Squarefree has 7 generators spanning a 6-dimensional space of quadrics (one `Q`-linear relation); Singular still consumes all 7, which does not change the ideal. Naive complete-intersection arithmetic `10-6=4` or `9-6=3` is false and is not what the producer reports. Squarefree `monomial_count=45=binom(9+1,2)` is the full quadratic monomial basis in 9 variables, consistent with span taken in that ambient space.

The origin of `s`-space is always a point (homogeneous linear maps, homogeneous quadrics). That is the zero-lower-face solution, not a missing equation.

---

## Charge 4 — Singular consumes the primitive ideal; dimensions 7/6/6; nonunit is not a Keller branch

**CONFIRMED**

Each `obstruction.sing` is `option(redSB); ring R=0,(s1..s_n),dp; ideal I=<primitive generators>; G=std(I); dim(G)`. No `radical`, `minAssGTZ`, `slimgb` replacement, or component deletion. Input generator counts 6, 6, 7 match `nonzero_cokernel_equations`. Frozen stdout:

| stratum | `INPUT_GENERATORS` | `GB_GENERATORS` | `DIMENSION` | nilpotents in printed GB |
|---|---:|---:|---:|---|
| triple | 6 | 8 | 7 | `s10^2` in `I` and in `G`; `s10` not a generator |
| double | 6 | 7 | 6 | `s1^2`, `s9^2`; `s7^2*s9` in `G` |
| squarefree | 7 | 8 | 6 | `s9^2` in `I` and in `G` |

Generator-by-generator consumption was checked: triple and double match the six primitive triples/pairs including `s5 s10+s6 s9+s7 s8` and `s1^2`; squarefree first generator begins `(∑ s_i)^2` as in `equations_primitive[0]`, and the last two generators are `13 s8 s9-3 s9^2` and `s9^2`. Dual-host `obstruction.sing` and `singular.stdout` are byte-identical. Singular was not rerun locally; the frozen `DIMENSION` lines are the dimension evidence.

A nonunit first-two-band ideal is forced by the origin in `s`-space and by the zero-lower-face solution. It is not a surviving full Keller branch, not a continuation of the SAT witness, and not emptiness of any complementary stratum. The producer states this. Do not promote dim 7/6/6 past degree 17.

---

## Charge 5 — controls at exact strength

**CONFIRMED** at the following strengths, and no higher.

1. **Derivative-bracket agreement.** Two formulas in one script (`bracket` vs `direct_bracket`) are asserted equal on every column and every quadratic source. Frozen `direct_bracket_agreement=true`. This is same-source dual-formula checking, not a second language or CAS.
2. **Zero-lower-face positive control.** The boolean is hardcoded `True` after the maps are built. It is a homogeneity tautology (`A0=0`, `B0=0`, quadrics have no constant term), not an extra stored matrix-vector replay. The independent positive evidence is that Singular does not return the unit ideal and that `I` is homogeneous. That matches the registered control at tautological strength.
3. **Perturbed-`Q12` negative control.** `Q12[12]+=1` adds `x^{12}`. Frozen nonzero supports, checked by hand:
   - triple: `[y^9,x^{12}]=-108 x^{11} y^8`, JSON index 11 coefficient `-108`;
   - double: `[x^3 y^6,x^{12}]=-72 x^{14} y^5`, JSON index 14 coefficient `-72`;
   - squarefree: four nonzero coefficients at indices 14–17.
4. **Same-source dual-host custody.** For every stratum, `compiler.stdout`, `result.json`, `obstruction.sing`, and `singular.stdout` are byte-identical across r6d and Box02; squarefree also has identical `sat_interface.stdout` and `sat_interface_result.json`. Inner `SOURCE.sha256` hashes of the four case sources match the V3 manifest on both hosts; the `SOURCE.sha256` files themselves differ by absolute-path prefixes. All six `/usr/bin/time` stderr pairs differ, so these are two processes of one implementation. The producer’s “custody only” sentence is the correct strength. Both hosts wrote `start_utc=end_utc=2026-08-25T18:02:02Z`; the jobs finished inside one UTC second. That is consistent with 19×21 exact rref and is not dual-host collusion: stderr hashes differ.

---

## Charge 6 — stale `OUTPUT.sha256`

**CONFIRMED** of the stale-entry explanation; **repair** of the active-object sentence.

`run_aws.sh` writes `OUTPUT.sha256` from `$outdir/*` and only afterwards prints `PASS <stratum>` to stdout. With stdout redirected to `launcher.stdout` inside `$outdir`, the hashed `launcher.stdout` is the empty file.

On all six lanes, every `OUTPUT.sha256` record matches the harvested file except `launcher.stdout`, which is recorded as the empty digest `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` while the harvested file is exactly `PASS triple\n` / `PASS double\n` / `PASS squarefree\n` (hashes `635b6fe6…`, `e05eb150…`, `94bded4d…`). No other algebraic or version file is stale. `OUTPUT.sha256` does not list itself (tmp/mv), which is not a second stale hash. The six `OUTPUT.sha256` files are negative controls and must not be used as final manifests.

The producer’s further sentence that the active post-harvest manifest is `MANIFEST.postrun.sha256` is false under V3. Smallest correction is the custody sentence in the custody section above.

---

## Charge 7 — witness discriminant valuations; squarefree continuation

**CONFIRMED** for the literal 4-tuple. Every exact integral continuation of that 4-tuple is forced into the squarefree total-cubic stratum. No continuation is produced.

Witness SHA-256 `a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a` exists at the path consumed by `compose_sat_interface.py` and has `H_coefficients_mod177147=[1,119880,40581,0]`.

Valuations, by successive division by 3:

```text
v3(1)=0,
v3(119880)=4,     119880 = 3^4 · 1480,  1480 ≡ 1 (mod 3),
v3(40581)=5,      40581  = 3^5 · 167,   167 ≡ 2 (mod 3),
v3(0)=∞  so any lift of the last coefficient has valuation >=11.
```

Write `a'=119880+3^{11}A`, `b'=40581+3^{11}B`, `c'=3^{11}C`. Then `v3(a')=4` and `v3(b')=5` exactly. The binary/univariate discriminant

```text
Disc = a^2 b^2 - 4 b^3 - 4 a^3 c - 27 c^2 + 18 a b c
```

is the discriminant of `s^3+a s^2+b s+c` with `s=y/x`, equivalently of the binary form `y^3+a x y^2+b x^2 y+c x^3`. That is the correct chart for leading `y^3`-coefficient 1 and vanishing `x^3`-coefficient. Term valuations:

| term | valuation | exact or bound |
|---|---:|---|
| `a'^2 b'^2` | 2·4+2·5=18 | exact |
| `-4 b'^3` | `v3(4)+3·5=15` | exact |
| `-4 a'^3 c'` | `≥12+11=23` | lower bound |
| `-27 c'^2` | `≥3+22=25` | lower bound |
| `18 a' b' c'` | `v3(18)+4+5+≥11=≥22` | lower bound |

Unique minimum 15, carried by `-4 b'^3` alone. No other term can meet valuation 15, so there is no cancellation. Frozen integer `Disc(119880,40581,0)=23666500928802306636=3^{15}·1649359141348` with `1649359141348 ≢ 0 (mod 3)`, hence `v3=15` on the special fibre as well.

Attacks:

- **Cancellation.** Fails: the minimum is unique and exact.
- **Coefficient-representative.** The monic slice (leading 1 fixed) covers unit-leading lifts: a leading coefficient `1+3^{11}L` remains a unit and can be scaled back into the same `a,b,c` continuation box of valuation `≥11`. A continuation that dropped the leading unit would not reduce to this witness. `PGL2` changes the representative but preserve vanishing of `Disc`; the claim is nonzero discriminant, not invariance of the valuation 15.
- **Finite-witness quantifier.** One frozen 4-tuple, not the ambient `3^{150}` family, not every B9 SAT cubic, and not a characteristic-zero point. Conditional on an exact continuation of this 4-tuple, the total-homogeneous cubic is type `LMN`. The SAT interface does not compose any degree-18/17 band on that continuation.

Root-multiplicity controls `Disc(0,0,0)=0` (`t^3`) and `Disc(1,0,0)=0` (`t^2(t+1)`) are correct and unused for the witness bound.

Precision note, not a defect: calling 18 and 15 “lower bounds” is weakly worded; they are exact. The uniqueness argument only needs the other three terms to be strictly larger, which they are.

---

## Charge 8 — partial-`y` Kummer order one vs total-homogeneous `K`; Q8 SCOPE-CONFLICT

**CONFIRMED**, with one typing repair in the SAT JSON.

The `(9,12)` leading-coefficient identities `a9(x)=h(x)^3`, `b12(x)=h(x)^4` are the licensed partial-`y` Kummer preflight on that cell (Q8 interface V2, SHA-256 `82c701474a9d1605097910f7947deb99d70908934fa93d26a73103b4b2440e40`, already hostile-confirmed). They are not recomputed from this band compiler.

Independent D12 cap, given those identities: `deg_total(Q)≤12` forces the coefficient of `y^{12}` to have `x`-degree 0, so `b12` is a nonzero constant. Then `h^4` is constant, so `h` is constant. After the licensed finite scalar extension, `[h]=1` in `k(x)^*/k(x)^{*3}`. That is Kummer order one, `H=deg_x(h)=0`. Residual divisibility `3|H` remains true and does not make the class nontrivial.

This is distinct from the total-homogeneous cubic `K` in `P9=K^3`, `Q12=K^4`. Frozen squarefree `K=xy(x-y)` is nonconstant as a binary form while `h(x)` is constant. Order-one partial-`y` Kummer does not solve the common-cubic incidence or any lower Jacobian band.

Selected corrected Q8 is an order-three `p=1` divided-row chart that refuses the order-one core. An order-one fixed-D12 object cannot land there. The producer’s “strict SCOPE-CONFLICT … not a landing” is the correct strength. Denominator clearing and the `p=q=0` special fibre do not license a B9 specialization into that chart.

`compose_sat_interface.py` writes `"partial_y_kummer_order_from_fixed_D12": 1` without reading `h` or any Q8 source. The value is a hardcoded D12 identity sitting in the SAT-witness JSON.

**Corrected SAT-interface typing:** `partial_y_kummer_order_from_fixed_D12=1` is not computed from `H_coefficients`. It is the independent total-degree cap on the reviewed `(9,12)` partial-`y` route. It must not be read as a property of the SAT cubic, as a continuation of that cubic, or as a Q8 landing.

The producer prose already says “Separately” and does not conflate `K` with `h`. The JSON mixing is the defect.

---

## Charge 9 — firewalls

**CONFIRMED**

The producer firewall, preregistration refusal list, README, and SAT `refuses` array together block: survival past `3^{11}`, inverse limit, characteristic-zero Keller map, compatibility below degree 17, emptiness of any root-type stratum, preservation of the B9 residue chart under `PGL2`, selected-Q8 landing, all-depth lift, lower-band composition for the finite witness, full fixed-cap exclusion, maximum twelve, a counterexample, and JC2.

No charged sentence exceeds those bounds once the V3 active-root repair and the SAT-JSON Kummer typing repair are applied. Dual-host identity is not a second mathematical implementation. Nonunit obstruction ideals are not surviving branches. Squarefree continuation of the literal 4-tuple is conditional. Partial-`y` order one is not a statement about `K`.

---

## Repairs (smallest corrected statements)

1. **Active custody object (producer §AWS custody, and `CUSTODY_SUPPLEMENT.md`).** Replace the sentence naming `MANIFEST.postrun.sha256` as active by: the remote `OUTPUT.sha256` files are quarantined; the active manifest is `MANIFEST.postrun.v3.sha256` (`38466426e3a0b113a4cbd71b447d9a44b01482bcd3e3acea4879cad96589a8e3`) with freeze root `FREEZE.v3.sha256` (`b4374cb2395cadb1c4755432dd7087dd19f44e4ac1e21265054a38aa429354d5`).
2. **V1 valid-record count (`CUSTODY_MANIFEST_ERRATUM.md`).** Already repaired by the immutable count-correction: 96 valid records plus seven warning lines, 103 physical lines, not 89. Record the further precision that `shasum -c` on V1 warns and exits 0 (fail-open), while V3 is fail-closed.
3. **SAT JSON Kummer field.** `partial_y_kummer_order_from_fixed_D12` is a hardcoded independent D12 identity, not a computation from the SAT cubic.

No mathematical rank, generator, dimension, valuation, or firewall statement requires repair.

---

## Sources read and SHA-256

Active roots (recomputed):

| path | SHA-256 |
|---|---|
| `xmodel/max12-912-order1-binary-cubic-first-two-bands-aws-20260825.md` | `2a185d6dabec5c47c16be2779c45e351f9658abe8fc8140de91c4d83a9407fb7` |
| `cases/…/MANIFEST.postrun.v3.sha256` | `38466426e3a0b113a4cbd71b447d9a44b01482bcd3e3acea4879cad96589a8e3` |
| `cases/…/FREEZE.v3.sha256` | `b4374cb2395cadb1c4755432dd7087dd19f44e4ac1e21265054a38aa429354d5` |
| `cases/…/CUSTODY_MANIFEST_COUNT_CORRECTION.md` | `d7c6caa33c6879b321acd838c922ea2f655d01a267912f3ed3190860d4b5c9ec` |
| `xmodel/max12-912-order1-binary-cubic-first-two-bands-review-grok-20260825-prompt.md` | `c7fe6dae6e5b79c38751c2a664201557817f78362d27b9ca978b333e96344c5b` |
| `xmodel/max12-912-order1-binary-cubic-first-two-bands-review-grok-v3-20260825-prompt.md` | `8d87299b404d8e2ccb9ed4dc3d818fcdde5c92787b96be299515c2d8d808d5eb` |

Case sources and V1/V2 custody (all in the V3 manifest except the V3 freeze root):

| path | SHA-256 |
|---|---|
| `cases/…/PREREGISTRATION.md` | `8225a4dd2a6149c79afed95b72b189cb630c050fc0cafbbbc2d9fef04796fa89` |
| `cases/…/README.md` | `c458ef561293927c8a2f9dee1ffddbf8cac663bf5bfd040ae478090f17955cb7` |
| `cases/…/compile_bands.py` | `b96bf20d0a262d92c31746b666d668f01fcfe820839d29656eed4b09da3a3b0a` |
| `cases/…/compose_sat_interface.py` | `e86adb9909a9b7106094daeed845996deb9803aacf5c8e0515f0612edb0c08f2` |
| `cases/…/run_aws.sh` | `94efc91114cff15adb37fb1c27fb3a295a98abe5b577064d0c64097bca94eb0e` |
| `cases/…/CUSTODY_SUPPLEMENT.md` | `2c642e24776b9adfd5f62ed037fe1a0bffd08803b5e07400c2838e49efbebc90` |
| `cases/…/CUSTODY_MANIFEST_ERRATUM.md` | `82494364dcd4f1d86fa7abb276323251c6cc65f3005c13fb3c4d6da626188c25` |
| `cases/…/MANIFEST.postrun.sha256` | `4409325ec61c8b8f724f94e230d853c1b8ba4651e15ac735a59d43e696f2aac1` |
| `cases/…/MANIFEST.postrun.v2.sha256` | `0f74917eee62e09222f33d74fdbb16e508716e33bdfd0bed88683e2fbb215b1f` |
| `cases/…/FREEZE.sha256` | `6d9622941892bc5a08aa41622e87a670d2418d265c5ddf774225404c93b1ca32` |
| `cases/…/FREEZE.v2.sha256` | `12e44a26f20bea5450e1f4f56b996a83fa2ba290360dec88266e6727471e9bb0` |

Frozen algebraic evidence (r6d; Box02 algebraic bytes identical):

| path | SHA-256 |
|---|---|
| `evidence/r6d/triple/result.json` | `7ac9332c6e8e391d4adb76e6a580dc481296f0b3532488b0fdae71501f8f99e2` |
| `evidence/r6d/double/result.json` | `551231756492097728b0276c28ecbdee3067c218f86e04e85e5aa83bde57afdc` |
| `evidence/r6d/squarefree/result.json` | `6eadc4dc910e87921e39b3f3673c9f8345d32de702796d1012f9525a70348af9` |
| `evidence/r6d/triple/obstruction.sing` | `88f8352f589f5ff897155b7f3f0a4c3cc4c71755a4ff1e71e9820e073770da4a` |
| `evidence/r6d/double/obstruction.sing` | `601d4867d10d1190e87f4aaefd725efbbcaf0069c7981f99c529ad4630701927` |
| `evidence/r6d/squarefree/obstruction.sing` | `d2afbb3ce32ccc5ab36141fcb187268fff6653b254c0fbf4c0ab032dbf34add1` |
| `evidence/r6d/triple/singular.stdout` | `f64277addba6583f8a428aa1c4c55b8af9c6e5538c6ebaa2eaab279186356207` |
| `evidence/r6d/double/singular.stdout` | `2063f63866d6b2abb22753cd9e6c4f3ca56ca12e738fa87dac8d01beb8f8f36b` |
| `evidence/r6d/squarefree/singular.stdout` | `c9a596a199a0ba104ca4b8db45cf13e98155ded74e80e587e678aad35709fb74` |
| `evidence/r6d/squarefree/sat_interface_result.json` | `18a2335297a6629284490e3a3b4485fc7d12e90c36fdf370a3bade3336d08c35` |
| `evidence/r6d/triple/OUTPUT.sha256` | `5226dbf0f9cf12ff292a9fb8b7c136daddc255e8a72b547ca59e5159ee7b17c3` |
| `evidence/r6d/triple/launcher.stdout` | `635b6fe6e53fa50ec74699bf0fd30d1127c0f3109edc40f154e1cac0058d13ce` |

External SAT witness and licensed Kummer/Q8 interface (read, not part of this case freeze):

| path | SHA-256 |
|---|---|
| `cases/as_b9_9_12_common_cubic_hostile_audit_20260825/evidence/box02/independent_witness.json` | `a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a` |
| `xmodel/as-b9-max12-leading-shear-q8-interface-audit-v2-20260825.md` | `82c701474a9d1605097910f7947deb99d70908934fa93d26a73103b4b2440e40` |
| `xmodel/as-b9-max12-leading-shear-q8-interface-audit-v2-review-grok-20260825.md` | `1cb8f1c193203808f97f143f66eed60fc0469f13821497fa1d663dd21ac26b27` |

Diagnostics only (not promotion inputs):

| path | SHA-256 |
|---|---|
| `xmodel/max12-912-order1-binary-cubic-first-two-bands-review-grok-20260825.log` | `ff028592504c7e4cd6f0c06e70f952247a2b0162f98a0c70e570a67d8d5b60d9` |
| `xmodel/max12-912-order1-binary-cubic-first-two-bands-review-grok-v2-20260825.log` | `ff028592504c7e4cd6f0c06e70f952247a2b0162f98a0c70e570a67d8d5b60d9` |
| `xmodel/max12-912-order1-binary-cubic-first-two-bands-review-grok-v2-20260825-prompt.md` | `628fd93591fd13581f911347278bfbdf2b6a122e153c4d4bd4d8843f4c78cd0a` |

All 102 V3 manifest records were verified by `shasum -c` under `LC_ALL=C` and are not repeated here. No case, producer, or prior-review byte was edited.
