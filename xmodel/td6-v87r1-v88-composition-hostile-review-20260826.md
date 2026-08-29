CONFIRMED

# Hostile review — V87R1 q2-specialization repair plus V88 q15 composition

| Field | Value |
|---|---|
| Target | V87R1 repair package; V88 q15 pullback package and design; original V87 review and controlling repair addendum |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest exact repair | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile review. Producer PASS banners and dual-host byte-identity are custody only |
| Method | Recomputed SHA-256 of every charged pin and every consumed manifest row; flint identities in `Q[C,V,U]`; tablewise comparison of both AWS trees against frozen V87/V86 inventories and cleared `h` tables; serializer audit of V86 `full_digest` versus V87R1 `slice_digest`; source review of `q2_slice`, the triangular shear, FIRST/`compile_current_degree12` extra terms, both omission controls, and the leftover pullback. No Singular, Sage, Lean, or `jc2-lean`. The 9-minute V87R1 client and the 2-minute V88 client were not re-executed; the specialization comparison is recovered from frozen output tables, and the q15 identity is recovered from the triangular map plus exact receiver cancellation |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

No file other than this review was written. V89 was not imported.

---

## Verdict

**CONFIRMED.**

The original V87 review's sole controlling gap is closed by V87R1. On the normalized three-center source chart, with frozen V82QST3 multipliers `a_P,a_i` and with

```text
q_bar(t) = t + sum_{e in E} q_e t^e + t^{25},
E = {2,...,14,16,...,24},
```

the rebuilt raw P12 and 38 packed FIRST maps satisfy

```text
U^{12} H^3 B3
  = a_P P12(C,V,U,q_bar)
    + sum_i a_i FIRST_i(C,V,U,q_bar)
    + F h_F + sum_{e in E} q_e h_e                 (1)
```

in `Q[C,V,U,q_e:e in E][X_0,...,X_{131}]_{U H B3}`. Setting every licensed coordinate except `q2` to zero recovers the promoted, hostile-reviewed V86 total-`(F,q2)` sources and both quotient tables under the documented V86 serializer. That comparison is output-explicit: 39 source rows against frozen V86 hashes, and byte-identical cleared `h_F` / `h_2` tables against frozen V86 `TOTAL_F_Q2_HF_CLEARED.tsv` and `TOTAL_F_Q2_HBETA_CLEARED.tsv`. Shared parent-client text is not the comparison.

V88 then installs the exact two-sided total target-shear

```text
q_raw = q_bar + b p,   f_raw = f_bar,   g_raw = g_bar + b f_bar,     (2.1)
q_bar = q_raw - b p,   f_bar = f_raw,   g_bar = g_raw - b f_raw,     (2.2)
```

with `p=t^{15}` and `b=q15`. These are mutually inverse integral polynomial maps on all 3,602 global section coordinates, triangular of Jacobian determinant one, with no q15 denominator. After both the section shear and `q_raw'=q_bar'+15 b t^{14}` are installed, literal raw P12 and all 38 packed raw FIRST maps equal their V87 normalized counterparts as polynomials over the untruncated 23-variable ring, and have q15-degree zero. Pulling (1) along (2.1) therefore leaves `F,U,H,B3`, the multipliers, the source-row typing, and the 22 transverse q coordinates unchanged, and produces exactly zero q15 remainder:

```text
U^{12} H^3 B3
  = a_P P12_raw + sum_i a_i FIRST_i,raw
    + F h_F + sum_{e=2..14,16..24} q_e h_e.                        (3)
```

On `D(U H B3)` this excludes DVR arcs in this retained literal source family on which all raw P12/FIRST rows vanish and `F` together with every one of the 22 transverse q coordinates have positive valuation. The coordinate `q15` may have arbitrary valuation, including zero. No unit theorem for `q2..q14,q16..q24` is claimed. V87R1 does not silently change V87 and adds no unit-q claim.

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Primary pins | hashes | all 18 charged pins match, including V87R1 client `5227b676…` |
| 0. V87R1 evidence / freeze / source | every named file | `EVIDENCE.sha256` 30/30, `FREEZE.sha256` 62/62, `SOURCE.sha256` 27/27 at case root and inside `source.tar.gz` |
| 0. V88 evidence / freeze / source | every named file | `EVIDENCE.sha256` 30/30, `FREEZE.sha256` 52/52, `SOURCE.sha256` 17/17 at case root and inside `source.tar.gz` |
| 0. V86 lineage consumed by V87R1 | corrected review / promotion | `9e70d6ce…` and `677513a2…` match the frozen V86 V2 review and promotion |
| 1. 39-source comparison | both AWS trees | 1 P12 + 38 FIRST; exact keys; live V87 full hashes = frozen V87; q2-slice hashes = frozen V86 full-beta; beta-zero hashes = frozen V86 beta-zero |
| 1. Serializer | V86 encoding, not shared code | V87R1 recodes q2-only QPoly monomials as `(parameter, beta_degree, E3_exact)` and compares to frozen V86 bytes |
| 2. Actual `h` outputs | byte identity | both hosts' `V87_Q2_HF_CLEARED.tsv` / `V87_Q2_H2_CLEARED.tsv` equal frozen V86 HF / HBETA tables |
| 2. Term / scalar / clearing counts | 2797 / 3330; 50346 / 59940; `U*H` | independently recounted; every E3 slot has printed polynomial denominator `1`; common `C*U-3*U^3` |
| 3. Repair scope | sole original V87 gap | closed; V87 client hash unchanged; no unit-q theorem added; original packaging defects 2–4 remain non-controlling |
| 4. Two-sided map | 3602 coords, 976 shared, det 1 | unipotent triangular shear; 976-slot embedding `(i,j)↦(i,j)`; 1650 unshared g slots identity; inverse is subtraction |
| 4. Transport | original rows + unique q15 RHS | 4743/4743 shared-equals-f; unique extra `('X',0,15)` with f-RHS `1` |
| 5. Receiver invariance | FIRST and degree-12 CURRENT | exact cancellation identities; both omissions change 15 FIRST rows at `('X-2',14)`; 39 hashes = frozen V87; q15 degree 0 |
| 6. Composition | pull (1) through (2.1) | leftover has no b; `F,U,H,B3`, multipliers, 22 transverse q unchanged |
| 7. DVR / firewall | `D(U H B3)` | unit left side vs `(F,q_e:e in E)` in the maximal ideal; q15 may be a unit; no 22-q unit theorem |
| 8. Dual AWS | hosts, rc, math vs metadata | distinct Box02 / r6d; `rc=0`; math outputs byte-identical; stderr is `/usr/bin/time -v` only; zero swap |

---

## 1. Custody

Recomputed SHA-256 of every charged primary pin:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/td6-v87-total-f-allq-hostile-review-20260826.md` | `c4f3ea4a1de7f9675cd46029ba568d58dfe2374540d8e1d99dccc73db51ee1f4` | original V87 review |
| `xmodel/td6-v87-total-f-allq-hostile-review-repair-addendum-20260826.md` | `572c4b4c36f14a234041990cbc25f39621699888184c97b6a343c466d2215419` | controlling addendum |
| V87 `RESULT.md` | `6e22c6ac16f9e164b760367cf65b970649e9235f185e8ec82f8e28dbd6859bda` | V87 producer result |
| V87 `EVIDENCE.sha256` | `074072f04a88b2e74e1545afdbdd173e8dbc0d68bd2052b6ea37ebad05e754c5` | V87 evidence manifest |
| V87 `FREEZE.sha256` | `ef39fef7983ed3251bc21b3dd4f53db075f816cd95ffb7a38511956d7d9c60b9` | V87 freeze |
| V87 `SOURCE.sha256` | `f82ebe8ef8018542c02d9cbe3654c84b2c6336f442d5e8b83633cdeebbf3e874` | V87 source manifest |
| V87R1 `RESULT.md` | `824344bc520e85621bd88455397a6ca2ad9997616055f7187b3cfc9923404089` | repair result |
| V87R1 `AWS_LAUNCH.md` | `2796a9fd3b3e08ba3ba49078e5dc23d09bfe86b2146e57320ba67156cf0bbdf1` | repair launch record |
| V87R1 `EVIDENCE.sha256` | `43d796d9b392c7c94a70af89d2e397bbc9fa7f37a3f286e342a70c6408b34cf7` | repair evidence manifest |
| V87R1 `FREEZE.sha256` | `1caf9fa6bda9f9b0a04573345866b7b9aa6fb505feed78e1df6e0809e7e85393` | repair freeze |
| V87R1 `SOURCE.sha256` | `a0c4421bf52784cd949a649bb09a9045de8bb13f84c22f087245becba7967614` | repair source manifest |
| V87R1 `source.tar.gz` | `c7933417e0d0ad2e69a99a2a982a3a2cf2d670eecf0b018f72ac8ea402675a78` | repair archive |
| V87R1 client | `5227b6763aca6833c8aab117337f74c45b0be89b6112b0c35f0b6580c1143237` | `replay_v87r1_v86_specialization.py` |
| V88 `RESULT.md` | `c34ae948e91b86e51a6030a93ea379e8bc570c457d3619c1e8ff57a33255a3df` | V88 producer result |
| V88 `AWS_LAUNCH.md` | `ca4d382e944c9f3fce70c028e5d9678af318e3eda31f9cf11c21beb5fe6b1616` | V88 launch record |
| V88 `EVIDENCE.sha256` | `e3ffec3f7ca1e26000ef7c5b1e4fd9aefb8fc07099af66a9eb0b4c7841c61317` | V88 evidence manifest |
| V88 `FREEZE.sha256` | `20f9a6caafa3677db0da55a5d729bc7b45639a614b26fac46853d27c9e7445cd` | V88 freeze |
| V88 `SOURCE.sha256` | `146cebda99ee7c4264c5e1e50a3905901cd92a3d8d7005d5b908f5b6953de433` | V88 source manifest |
| V88 design | `eac77fcc8dc019e5e05c4d58c5172040076daa151e16cf87bcc2245040a3f03f` | `td6-v88-q15-target-shear-total-coordinate-design-20260826.md` |

Every path named in the V87R1, V88, and original V87 `EVIDENCE.sha256` / `FREEZE.sha256` / `SOURCE.sha256` files rehashes to the printed digest. Every `SOURCE.sha256` row exists at the case root and as `source/<path>` inside the corresponding tarball, and both copies match.

Mathematical outputs, as opposed to host metadata:

- V87R1 math: four `repair/output/*` files and `repair/stdout`, SHA-256 `e60173b3…`, `89ecec18…`, `590f88a2…`, `64147317…`, `c0104ec0…` on both hosts.
- V88 math: four `q15/output/*` files and `q15/stdout`, SHA-256 `602b3a03…`, `e6adc986…`, `5cb919b9…`, `807a9a65…`, `eb4eede4…` on both hosts.
- Host metadata that correctly differs: `pid`, `stderr`, `launch.meta`, `finished_utc`, `fleet_finished_utc`, `fleet_supervisor.pid`, `registration.meta`.
- Empty `wrapper.log` files are the empty-file digest `e3b0c442…`.

The V87 parent client is byte-identical across the original V87 package, V87R1, and V88, at `7c0890ab…`. V87R1 consumes the corrected V86 hostile review `9e70d6ce…` and promotion `677513a2…`, not an unreviewed producer banner. V88 `V88_DESIGN.md` equals the charged design file. Neither repair package mentions V89. Producer `PASS` banners were not used as algebra.

---

## 2. Charge 2 — exact 39-source comparison

Both AWS copies of `V87_V86_Q2_SOURCE_COMPARISON.tsv` are byte-identical, SHA-256 `e60173b3e8f224d6fab09f0ef3a831c846a27137718ba1d188d08b009453fae4`. The table has a header plus 39 data rows: one P12 row with key `('X0_RAW', 12)` and 38 FIRST rows with keys `('X-2', 0)` through `('X-2', 37)`. Independently compared to the frozen inventories:

- every `v87_full_sha256` equals the corresponding frozen V87 `full_sha256`, including the live V87 evidence-tree inventory `079447d9…`;
- every `v87_q2_slice_sha256` equals the corresponding frozen V86 `full_sha256`, including the live V86 evidence-tree inventory `450c478c…`;
- every `v86_beta_zero_sha256` equals the corresponding frozen V86 `beta_zero_sha256` and the frozen V87 `all_q_zero_sha256`;
- every `match` flag is `true`;
- every V87 full digest differs from its V86 full-beta digest, so some licensed `q_e` with `e≠2` is live in genuine P12 and in every packed FIRST map;
- every V86 full-beta digest differs from its beta-zero digest, so `q2` itself is live.

That is the comparison the original V87 review required. Term counts 3330/2797 are not substituted for it.

### Serializer, independently of shared source

V86 `full_digest` writes, for each parameter monomial and each integer beta degree,

```text
repr(parameter_monomial)  <tab>  degree  <tab>  e3_exact(coefficient)
```

and hashes the joined lines plus a trailing newline. V87 `full_digest` writes q-monomial tuples instead of integer degrees, so a V87 full hash cannot equal a V86 full hash even after a true specialization. V87R1 does not compare those encodings. It first restricts each live V87 polynomial by

```text
keep a q-monomial iff every factor equals 2
```

(`all(exponent == 2 for exponent in q_monomial)` is true for the empty monomial `()` and for pure powers of `q2`, and false as soon as any other licensed exponent appears), records `degree = len(q_monomial)`, and then hashes under the V86 line format. The frozen V86 `full_sha256` column is the hash of that same format, produced by the separate V86 freeze, not by this repair client. Recoding live V87 QPoly objects into the V86 byte format and matching frozen V86 hashes is the comparison. Importing `replay_v86tfq2_total_f_q2.py` as a helper library is not.

The restriction really does set every non-`q2` coordinate to zero: a mixed monomial such as `(2,3)` is dropped, not recoded as beta-degree 2. Residual total q-degree 1, already walked on both V87 hosts and re-asserted by V87R1, implies there are no `q2^2` or `q2 q_e` terms to mis-assign. Independently, V87R1 checks `scale(h_2, q2)` against the residual's pure-`q2` part, which would fail if a higher pure-`q2` power were present.

A SHA-256 collision of two different exact E3 dumps is not a live attack. The quotient comparison below does not rely on source hashes at all.

---

## 3. Charge 3 — actual `h` outputs

Byte comparison, not digest comparison:

| Emitted V87R1 table (both hosts) | Frozen V86 table | SHA-256 |
|---|---|---|
| `V87_Q2_HF_CLEARED.tsv` | V87R1 pin of `V86_TOTAL_F_Q2_HF_CLEARED.tsv` and original V86 evidence `TOTAL_F_Q2_HF_CLEARED.tsv` | `89ecec18cea6547fe465fc4f6088f7f94ec9b6d717eefb33386f5b3fab6d49e0` |
| `V87_Q2_H2_CLEARED.tsv` | V87R1 pin of `V86_TOTAL_F_Q2_HBETA_CLEARED.tsv` and original V86 evidence `TOTAL_F_Q2_HBETA_CLEARED.tsv` | `590f88a20183a4d4363a4e14397084cae347838331abc6df536f60129f2f0384` |

Header is exactly `parameter_monomial<tab>beta_degree<tab>coefficient_exact`. Independently recounted:

- `h_F`: 2,797 terms, every `beta_degree=0`, 2,797×18 = 50,346 scalar coordinates, each E3 slot a pair `(polynomial, '1')`;
- `h_2`: 3,330 terms, every `beta_degree=0`, 3,330×18 = 59,940 scalar coordinates, same denom token `'1'`.

Localized digests under the V86 encoding reproduce the frozen V86 exact-result pins `hF_sha256=d42fd419…` and `hbeta_sha256=ff283ad8…`. Live V87 full digests of the unrestricted quotients reproduce the frozen V87 H inventory: `F ↦ 5f429f95…`, `q2 ↦ fee93555…`. Those two encodings differ because QPoly serializes `()` where BPoly serializes degree `0`; that is the encoding gap the original V87 review already recorded, and it is exactly what V87R1 recodes.

Common clearing is `U*H = C*U-3*U^3`. flint in `Q[C,V,U]` confirms `U H = C U - 3 U^3` and `gcd(F, U H) = 1`. Clearing multiplies by `E3(Rat3(U H))` and requires every scalar coordinate denominator to be `1`. It does not invert `F`, `q2`, or any q polynomial. `QPoly.inverse` fail-closes unless the support is a subset of `{()}`. Printed slash tokens in the TSV are QQ content of polynomial coefficients (for example `/281`, `/1405`), not polynomial division by `F` or by a q variable. No coefficient string contains a q-variable token.

The F-quotient is taken from the q-constant residual, 50,346 coordinates, matching V87R1 stdout `F_division_coordinate_count=50346` and the frozen V85 digest gate `EXPECTED_V85_H_SHA256`. The `h_2` table is the coefficient of the linear monomial `(2,)`, already the quotient by `q2`; V87R1 never divides by `q2`.

---

## 4. Charge 4 — repair scope

The original V87 review named one controlling gap: no exact comparison of the represented V87 family at `q_e=0` for `e≠2` against frozen V86 sources and `h` tables. Circumstantial term counts and shared compiler text were expressly insufficient. V87R1 emits that comparison as frozen output and it holds. That is the smallest repair the original review requested.

V87R1 does not silently change V87:

- the V87 client hash remains `7c0890ab…`;
- live full source hashes equal the frozen V87 inventory;
- live `h_F` / `h_2` full hashes equal the frozen V87 H inventory;
- slogans `new_unit_q_or_chart_claim=false`.

It adds no unit-q theorem, does not totalize q15, and does not claim a whole A3 / TD6 / SP-2 / JC2 statement.

Original V87 packaging items 2–4 survive and remain non-controlling: the V87 H inventory still omits a `q_degree`/`q_monomial` column; identity (1) itself was already recovered independently of the V86 lineage. After V87R1, none of those items is a remaining custody/proof gap in the charged specialization.

---

## 5. Charge 5 — V88 two-sided map

Coordinates of the unnormalized family: 976 f-rectangle slots `(i,j)` for `0≤i≤15`, `0≤j≤60`; 2,626 g-rectangle slots `(i,j)` for `0≤i≤25`, `0≤j≤100`; the 22 transverse q jets; and `b = [t^{15}]q`. That is 3,602 section coefficients plus the q jets. The f-rectangle embeds into the g-rectangle by the monomial map `(i,j)↦(i,j)`, i.e. f-index `i*61+j` to g-index `i*101+j`. The emitted coefficient-map TSV has exactly those 976 shared slots, with `i` in `0..15`, `j` in `0..60`, and both index formulae holding on every row. The remaining 1,650 g slots have no f partner.

On those coordinates (2.1) is

```text
f_raw = f_bar,
g_raw,ij = g_bar,ij + b f_bar,ij    if (i,j) is in the f rectangle,
g_raw,ij = g_bar,ij                 otherwise,
q_raw,e = q_bar,e                   for e in E,
q_raw,15 = b.
```

The inverse (2.2) is the same formulae with the sign of `b` reversed. Composition either way is the identity because `b f - b f = 0` in the commutative coefficient ring and `f` is held fixed. Ordered as `(f, g, q_e (e≠15), b)`, the Jacobian is block-triangular with identity diagonal blocks: `∂f_raw/∂f_bar = I`, `∂g_raw/∂g_bar = I`, `∂q_raw,e/∂q_bar,e = 1`, `∂b/∂b = 1`. Off-diagonal blocks involving `b` and `f` do not meet the diagonal. Determinant one. No localization and no q15 division. `Q23.inverse` fail-closes on any nonconstant q monomial; the AWS client completed.

The 976-row TSV is the shared-slot inventory, not a dump of 3,602 numeric values. The unshared 1,650 g slots are identity by the formula above; they contribute 1 to the determinant. Two-sided exactness on the transported bands (powers 1,2,3) is the computational check: each sheared g-form recovers the bar form after subtracting `b` times the embedded f-form.

### Original transport rows and the unique q15 RHS

Transport is linear in the global section coefficients (frozen V85 affine solve). The V88 audit evaluates every original unsolved g row against the corresponding f row:

- 4,743 g rows, 1,764 f rows;
- on every g row, the coefficients in the f rectangle, reindexed by `(i,j)↦ i*61+j`, equal the f-row of the same key, or are empty when f has no such key;
- `shared_equals_f` is `true` on all 4,743 rows;
- the unique g key with nonzero f-RHS is `('X', 0, 15)`, with f-RHS `1`.

If a g F1 or r9-pole row is not an f key, its shared slot set is empty, so the shear `+b f` does not enter that linear form. If it is an f key, shared equals the f row and the f-RHS is zero except at `('X',0,15)`. Therefore, after (2.1), the only added boundary source is `b` times that unit RHS, i.e. `('g','X',0,15)=b` in the V87 source-key convention. That is an exact evaluation of the sheared residual: original rows are q-independent, the shear is linear in `b`, and the residual is `b` times the recorded f-RHS vector. Omitting that unique source leaves residual `b`, which is the registered negative control. The producer slogan `q15_transport_rhs_omission_negative_control=true` is this uniqueness, not a second rebuild; the TSV is the evidence.

---

## 6. Charge 6 — literal receiver invariance

FIRST at degree `d` is the packed coefficient of

```text
sum_i f1[i] · Q_PRIME[d-i]  −  15 · g1[d-14],
```

i.e. the degree-`d` part of `f q' - p' g` with `p'=15 t^{14}`. After (2.1) and `Q_PRIME[14]=15 b`,

```text
f · (q_bar' + b p') − p' · (g_bar + b f)
  = f q_bar' − p' g_bar.
```

Degree by degree the extra terms are `15 b f1[d-14]` from `Q_PRIME[14]` and `−15 b f1[d-14]` from the sheared g-band, which cancel in the commutative coefficient ring. No division.

Genuine degree-12 CURRENT is the inlined `compile_x_current` block at `degree=12`. The `g3[degree-14]` correction is at index `−2` and is skipped. The extra b coefficient is therefore

```text
f1·(b f2)' + 2 f2·(b f1)' + 3 f3·(b p') − 2 f1'·(b f2) − f2'·(b f1)
  = b ( f1 f2' + 2 f2 f1' + 3 f3 p' − 2 f1' f2 − f2' f1 ).
```

`multiply_affine` multiplies E3 coefficients. Those coefficients commute, so `f1 f2' = f2' f1` and `f2 f1' = f1' f2`, and `3 f3 p' = 3 p' f3`. The parenthesis is identically zero. This is the design identity (2.3), not a tangent or a homogeneity count.

Both omission controls are nonvacuous and distinct:

- omit the section shear, retain `Q_PRIME[14]`: 15 FIRST rows change, first key `('X-2', 14)`, digest `012f0384…`;
- omit `Q_PRIME[14]`, retain the section shear: 15 FIRST rows change, first key `('X-2', 14)`, digest `c6c4df15…`.

Degree 14 is the `t^{14}` slot of `q'` and of `p'`. If either live path were inert, one comparison would be equality and the assert on a nonempty changed-key set would fail.

The 39-row invariance table has `normalized_sha256 = raw_sha256` on every row, and each of those hashes equals the corresponding frozen V87 `full_sha256`. P12 support is asserted `len==2893`. Walking every q-monomial of the raw sources finds no factor `15`. Raw source common denominator of 9,827 E3 coefficients is `C*U-3*U^3=U*H`, factored `(U,1)·(C-3U^2,1)`, coprime to `F`. The shear introduces no denominator.

---

## 7. Charge 7 — composition

Let `f` be the 39-tuple of raw P12/FIRST section-polynomials and `a` the frozen V82QST3 multipliers, embedded as q-degree-zero coefficients. V88 gives `f_raw = f_bar` as polynomials in the 23-variable ring, and the 39 hashes equal frozen V87, so `a·f_raw = a·f_bar`. The target `s = U^{12} H^3 B3` is a polynomial in `C,V,U` only; flint expands it to the emitted V87 `target=` polynomial, and `gcd(F,B3)=gcd(F,H)=gcd(F,U)=1`. The leftover of (1) is therefore the leftover of (3):

```text
s − a·f_raw = s − a·f_bar = F h_F + sum_{e in E} q_e h_e.
```

There is no q15 remainder. The 22 transverse coordinates are the same symbols on both sides of (2.1). Source-row typing is unchanged: P12 remains `('X0_RAW', 12)` and FIRST remains `('X-2', 0..37)`. This is equality of polynomials, not a tangent linearization and not a weighted-degree count.

V88 does not rebuild `h_F` or the 22 `h_e`. It does not need to: source invariance plus unchanged `s` and `a` identify the leftover. V87R1 is not a V88 input because V87R1 does not change V87 algebra; it only compares the q2 slice of that same algebra to V86.

---

## 8. Charge 8 — DVR consequence and firewall

On `D(U H B3)`, `s` is a unit. Identity (3) writes `s` as a combination of the raw P12/FIRST rows plus `F h_F + sum_{e in E} q_e h_e`. Every coefficient of `h_F` and of each `h_e` lies in the registered localization (denominator `U H` on the V87 side; V88 does not alter those polynomials and introduces no new denominator). If a DVR arc in this retained family kills every raw row and puts `F` and all 22 transverse q coordinates in the maximal ideal, the right side has positive valuation and the left side does not.

The valuation of `q15=b` is unconstrained: `b` does not appear in the leftover. In particular `v(q15)=0` is allowed.

Regularity of every `h` coefficient survives the pullback because the leftover polynomial is literally the V87 leftover. The shear is an integral polynomial map, so it cannot create a pole along `U H B3`. Raw source coefficients after the shear still have common denominator `U H`.

Firewall, as charged:

- q15 alone may be a unit;
- a unit among `q2..q14,q16..q24` is not covered;
- no omitted-modulus, total-Rees, whole-A3, TD6, SP-2, or JC2 claim is licensed;
- dead stretch, correction, F1-orbit/pole, centering, deck/torsion, and other boundary moduli are not variables of this ring;
- V89 is outside this charge and was not used.

---

## 9. Charge 9 — dual AWS

| | V87R1 Box02 | V87R1 r6d | V88 Box02 | V88 r6d |
|---|---|---|---|---|
| hostname | `ip-172-30-0-186` | `ip-172-30-0-45` | `ip-172-30-0-186` | `ip-172-30-0-45` |
| endpoint | `34.203.207.55` | `100.26.198.153` | `34.203.207.55` | `100.26.198.153` |
| archive | `c7933417…` | `c7933417…` | `46dee1d1…` | `46dee1d1…` |
| `rc` | `0` | `0` | `0` | `0` |
| elapsed | 9:16.96 | 9:06.28 | 2:15.51 | 2:17.37 |
| max RSS KiB | 1,173,092 | 1,172,144 | 298,324 | 298,044 |
| swaps | 0 | 0 | 0 | 0 |
| math stdout | `c0104ec0…` | `c0104ec0…` | `eb4eede4…` | `eb4eede4…` |

Hosts are distinct. Mathematical outputs and stdout are byte-identical across each pair, as they must be. Host metadata and both `stderr` files differ, as they should. Every nonempty `stderr` consists solely of a successful `/usr/bin/time -v` record (`Command being timed`, RSS, `Swaps: 0`, `Exit status: 0`). Dual-host agreement is custody that each freeze ran twice. It is not the identity (1), the V86 comparison, or the cancellation (2.3).

---

## 10. Failed attacks

- **Shared V87/V86 source as the V87R1 comparison.** The comparison is frozen-hash equality under the V86 serializer plus byte-identical cleared `h` tables from a separate V86 freeze.
- **Serializer collision between QPoly `()` and BPoly degree `0`.** V87R1 recodes; it does not compare the two encodings to each other.
- **`q2_slice` keeping mixed monomials.** `all(exponent==2 for …)` rejects any foreign factor; residual degree 1 leaves none.
- **Hidden `F` or `q2` inversion in the quotients.** Clearing multiplies by `U H`; `h_2` is a coefficient extraction; `gcd(F,U H)=1`; printed E3 denominators are `'1'`.
- **V87R1 silently mutating V87.** Parent-client hash and live full source/`h` hashes match the frozen V87 package.
- **Map not inverted on the 1,650 unshared g slots.** Those slots are identity; inverse is identity.
- **Jacobian not one.** Unipotent triangular, identity diagonal.
- **q15 as a silently omitted source modulus.** It is the lower target-shear coordinate of frozen `p=t^{15}`; V88 makes it a free coordinate of the raw family.
- **Square-zero / truncated ring.** `Q23` is an untruncated Cauchy product, the same type as V87 `QPoly` with `q15` adjoined.
- **FIRST/P12 invariance as a tangent test.** Cancellation is an identity in the polynomial ring; both omission controls change 15 rows.
- **Composition replaced by homogeneity.** Source polynomials are equal, leftover is identical, q15 coefficient is zero.
- **`h` acquiring a q15 pole.** Leftover polynomial unchanged; map integral.
- **Unit theorem for a transverse `q_e`.** Not claimed; leftover still contains that `q_e h_e`.
- **V89 strengthening.** Not present in either package and not used here.
- **Dual-host PASS as algebra.** Used only as custody.

---

## 11. Defects

1. **V88 coefficient-map TSV lists the 976 shared slots, not 3,602 numeric coordinates.** The unshared 1,650 g slots are identity by the displayed formula. Packaging, not a failing identity.
2. **V88 slogans a transport-RHS omission rebuild.** The evidence is uniqueness of the extra original f-RHS, which is the exact sheared residual. Packaging.
3. **Original V87 packaging items 2–4** (no `q_monomial` column in the H inventory; ring slogan omitting the 132 section coordinates) are unchanged and remain non-controlling.

None of these disturbs (1), the V86 comparison, (2.1)–(2.2), the receiver identities, or (3).

---

## 12. Firewall

This review confirms the V87R1 specialization repair and the V88 pullback of the resulting identity to the raw q15 family on one normalized fixed-`p=t^{15}` source slice, localized at `U H B3`. It does not totalize a unit among the other 22 q coordinates, dead stretch, correction, orbit/pole, centering, deck/torsion, or other boundary moduli; supply a full total-Rees chart; or prove a whole fixed A3, TD6, SP-2, or JC2 statement. V89 is a successor design only.

---

## Dependency table

| Producer assertion | Independently checked evidence | Verdict | Smallest repair |
|---|---|---|---|
| All charged pins match | recomputed SHA-256 of 18 pins | confirmed | — |
| V87R1 / V88 / V87 manifests and tarballs | 30/30, 62/62, 27/27; 30/30, 52/52, 17/17; 30/30, 44/44, 9/9 | confirmed | — |
| 39 V87 q2 source slices = frozen V86 | comparison TSV vs both frozen inventories and both live evidence trees; V86 serializer recode | confirmed | — |
| Cleared `h_F` / `h_2` = frozen V86 HF / HBETA | byte identity; 2797/3330 terms; 50346/59940 slots; denom `'1'`; localized digests `d42fd419…` / `ff283ad8…` | confirmed | — |
| Common clearing `U*H`; no F/q inversion | flint `UH=CU-3U^3`, `gcd(F,UH)=1`; multiply-by-UH; fail-closed q inverse | confirmed | — |
| V87R1 closes the sole original V87 gap and does not change V87 or add unit-q | original review gap statement; unchanged V87 client/hashes; slogans | confirmed | — |
| (2.1) and (2.2) mutually inverse, det 1, 3602 coords, 976 shared | triangular unipotent shear; TSV index formulae; band two-sided replay | confirmed | — |
| Unique q15 transport RHS `('g','X',0,15)=b` | 4743 shared-equals-f; unique extra `('X',0,15)` with f-RHS 1; linearity | confirmed | — |
| Raw FIRST/P12 exactly invariant; both omissions live; q15 degree 0; no q15 denom | cancellation identities; 15+15 changed rows at `('X-2',14)`; 39 V87 hashes; monomial walk; common `UH` | confirmed | — |
| Pullback of (1) is (3), zero q15 remainder | `f_raw=f_bar`; `s` and `a` independent of `b`; leftover has no `b` | confirmed | — |
| No DVR arc on `D(U H B3)` killing P12/FIRST with `v(F)>0` and `v(q_e)>0` for all 22 transverse q; q15 arbitrary; every `h` regular | (3) + unit `s` + denominators `UH` + integral map | confirmed on this slice | — |
| No extension to unit-q among the 22, omitted moduli, total-Rees, A3, TD6, SP-2, JC2, V89 | firewall slogans and the actual variable set of (3) | confirmed | — |
| Dual AWS custody | distinct hosts; `rc=0`; identical math; distinct metadata; time-v stderr; zero swap | confirmed as custody | — |

CONFIRMED
