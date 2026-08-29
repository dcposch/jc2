REPAIR

# Hostile review — TD6 V87 total-`(F, all licensed q)` raw-source certificate

| Field | Value |
|---|---|
| Target | V87TFAQ `RESULT.md`, `AWS_LAUNCH.md`, `EVIDENCE.sha256`, `FREEZE.sha256`, `SOURCE.sha256`; two AWS evidence trees |
| Overall verdict | **REPAIR** |
| Smallest failing identity | none found in the represented all-q identity (1) |
| Smallest custody/proof gap | no exact V87→V86 specialization comparison of the represented sources/`h` against frozen V86 total-`(F,q2)` artifacts |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile review. Dual-host PASS banners and byte-identity are custody only |
| Method | Recomputed SHA-256 of every charged pin and every consumed manifest row; flint identities in `Q[C,V,U]`; tablewise V85/V86 inventory comparison; source review of `QPoly`, both live q-paths, 44 FIRST omissions, `decompose_q_residual`, degree-12 CURRENT extraction, and denominator gates. No Singular, Sage, Lean, or `jc2-lean`. The 19-minute AWS client was not re-executed; identity (1) is recovered from polynomiality plus the hash-locked V85 special identity, not from a second producer run |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

No file other than this review was written.

---

## Verdict

**REPAIR.**

On the normalized three-center source chart, with frozen V82QST3 multipliers `a_P,a_i` and with

```text
q(t) = t + sum_{e in E} q_e t^e + t^{25},
E = {2,...,14,16,...,24},
```

the rebuilt raw P12 and 38 packed FIRST maps satisfy the exact identity

```text
U^{12} H^3 B3
  = a_P P12(C,V,U,q)
    + sum_i a_i FIRST_i(C,V,U,q)
    + F h_F + sum_{e in E} q_e h_e                 (1)
```

in `Q[C,V,U,q_e:e in E][X_0,...,X_{131}]_{U H B3}`, where `F=CU-V^2+U^3`, `H=C-3U^2`, and `B3` is the displayed sextic. The coefficient ring in the 22 licensed q jets is an untruncated sparse multivariate polynomial ring. Inversion of any nonconstant q polynomial is a closed failure. Both live paths for every licensed `q_e` are present: affine transport RHS at `('g','X',0,e)`, and receiver `q'` coefficient `e q_e` of `t^{e-1}`. The coordinate `q15` is the lower target-shear of the frozen pair `(p,q)=(t^{15}, q)` and is held at zero; it is not a silently dropped source modulus. Identity (1) does not claim a unit-q chart.

At all q zero, the 39 source digests equal the frozen V85 generic inventory, including the genuine 2,893-term P12 digest `8d5c3550…` and labels `0..131`. At `F=0` the frozen V82QST3 clearer `V^4 U^9 (V^2-4U^3)^3` is the exact specialization of the left side. The q-zero `F` quotient reproduces frozen V85 `h_F` digest `7434b0a7…`.

The producer does **not** contain a sufficient exact comparison of the represented V87 family at `q_e=0` for `e≠2` against the reviewed V86 total-`(F,q2)` artifacts. Shared parent-client text and a V86 SHA-256 pin are not that comparison. That is the charged custody/proof gap. It does not falsify (1). It blocks treating V87 as a checked lift of the reviewed q2 certificate.

**Smallest repair.** After building the live V87 P12, FIRST maps, `h_F`, and `h_2`, evaluate at `q_e=0` for all `e≠2`. Compare the resulting univariate-in-`q2` objects coefficientwise, or under a documented digest encoding, to frozen V86 `TOTAL_F_Q2_SOURCE_INVENTORY.tsv` together with the frozen V86 `h_F` / `h_beta` tables after the same clearing. Fail-close on any mismatch. Pin those V86 artifacts in `SOURCE.sha256`. Do not treat `replay_v86tfq2_total_f_q2.py` hash equality as this gate.

On `D(U H B3)` this excludes DVR arcs in this retained literal source family on which all raw P12/FIRST rows vanish and `F` together with every one of the 22 licensed q coordinates have positive valuation. It does not exclude unit-q fibres, q15, dead stretch, correction, orbit/pole, centering, deck/torsion, other boundary moduli, a total-Rees chart, or any whole fixed A3, TD6, SP-2, or JC2 statement.

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Primary pins | hashes | all seven charged pins match |
| 0. Evidence / freeze / source | every named file | `EVIDENCE.sha256` 30/30, `FREEZE.sha256` 44/44, `SOURCE.sha256` 9/9 at case root and inside `source.tar.gz` |
| 0. Nested compiler pins | shard / V32 / tri / QDUAL / q2-base / two-center | all six hash-pins match |
| 0. Dual AWS | hosts, archive, rc | distinct Box02 / r6d; archive `e80b1cba…`; `rc=0`; math stdout and four output files byte-identical |
| 1. 22-jet scope | `q2..q14,q16..q24` | `Q_EXPONENTS` is that exact 22-tuple; no duplicate; `15` absent; `Q_PRIME[14]` unset |
| 1. q15 | lower target-shear of fixed `p=t^{15}` | f-transport `{15:1}`, g-transport `{1:1,25:1}`; shear `q↦q-λp` moves `t^{15}`; gauge, not omitted modulus |
| 1. Unit q | identity (1) | no unit-q claim; slogans `q15_totalized=false` |
| 2. Transport path | `('g','X',0,e)` | affine `+q_e·E3(1)` on `from_vector(source_vector(key))`; one registered path per licensed e |
| 2. Direct `q'` path | `e q_e t^{e-1}` | `Q_PRIME[e-1]=e q_e`; plus `{0:1,24:25}`; FIRST-omission first key is exactly `('X-2', e-1)` |
| 2. Literal P12 | degree-12 CURRENT | inlined copy of `compile_x_current` at degree 12; no staged CURRENT/PREVIOUS/POLE |
| 2. Square-zero | `QPoly` vs `EJet` | Cauchy product; no degree cap; `qd.Dual=QPoly` and `v86.BPoly=QPoly` |
| 3. 44 omissions | transport and direct per e | 22×2 independent FIRST rebuilds; all changed-row counts positive; no shared mutation |
| 4. `QPoly` / partition | exact augmentation division | ordered prefix split of the augmentation ideal; replay identity; never inverts a q expression |
| 4. Identity (1) | independent of AWS equality | polynomiality + V85 + exact `F`-division + exact partition ⇒ (1) |
| 5. Degree telemetry | total/residual q-degree 1 | live `max_q_degree` walk is 1 on both hosts; H inventory consistent but does not by itself rule out pure squares |
| 6. V85 specialization | all q zero | 39/39 generic/all-q-zero SHA-256 match; P12 2,893 terms; labels `0..131`; special identity and `h_F` hash match |
| 6. V86 specialization | all q except q2 zero | **gap**: no exact comparison to frozen V86 sources/`h`; term counts 3330/2797 agree and are not a comparison |
| 7. Denominators | 312,604 E3 values, LCM `U H` | audited list is complete for the claimed objects; `gcd(F,U H)=gcd(F,B3)=1`; `312604×18=5626872` |
| 7. Row omissions | P12 and FIRST-0 | subtract used terms; index 0 is an active V82QST3 row |
| 8. Dual AWS | math vs host metadata | four outputs + stdout identical; pid/RSS/elapsed/launch.meta/finished_utc differ as they should |
| 9. DVR | `D(U H B3)` | unit left side vs `F h_F+sum q_e h_e` in the maximal ideal; scope is this 22-jet slice only |

---

## 1. Custody

Recomputed SHA-256 of the seven required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `RESULT.md` | `6e22c6ac16f9e164b760367cf65b970649e9235f185e8ec82f8e28dbd6859bda` | producer result |
| `AWS_LAUNCH.md` | `e11b19e69fbe816a49592225e79dbba0a9acc504d9c249ef00c010a51205c19e` | launch record |
| `EVIDENCE.sha256` | `074072f04a88b2e74e1545afdbdd173e8dbc0d68bd2052b6ea37ebad05e754c5` | evidence manifest |
| `FREEZE.sha256` | `ef39fef7983ed3251bc21b3dd4f53db075f816cd95ffb7a38511956d7d9c60b9` | freeze |
| `SOURCE.sha256` | `f82ebe8ef8018542c02d9cbe3654c84b2c6336f442d5e8b83633cdeebbf3e874` | AWS source manifest |
| `source.tar.gz` | `e80b1cba7b4a1749c7f12ecd7b6a8d9418e73b6b01d8f82081dbb76f113669d3` | source archive |
| `replay_v87tfaq_total_f_allq.py` | `7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463` | V87 client |

Every path named in `EVIDENCE.sha256` (30/30) and `FREEZE.sha256` (44/44) rehashes to the printed digest. Every `SOURCE.sha256` row exists at the case root and as `source/<path>` inside the tarball, and both copies match the listed digest.

Nested compiler pins reached from the frozen shard, independently rehashed:

| Pin | SHA-256 |
|---|---|
| V32 q2 dual client | `dcc7003def824c0d2a88998cbf22a66f022a32714f05754c505e8d825bd91742` |
| trivariate adapter | `1fb512643f31b4eda6c0e96ca1adbfe3e79599986c7c095b825605a4145fdaea` |
| two-center `replay.py` | `56df638aaa3ae02cf437a32258a920a8a66afb2781c089e30b1774a5b38e65db` |
| QDUAL `jet_orbit_adjoint` | `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198` |
| q2 base `boundary_q2_deformation` | `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357` |
| generic parent shard | `a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e` |

V86 parent client pin `5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c` and V85 parent pin `ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e` match the freeze. Producer `TD6-V87TFAQ-LITERAL-TOTAL-F-ALLQ-RAW-P12-SOURCE PASS` was not used as algebra.

---

## 2. Charge 1 — exact 22-jet scope and q15

`Q_EXPONENTS = tuple(range(2,15))+tuple(range(16,25))` with `len==22` and `15 not in Q_EXPONENTS`. The printed `q_exponents=` line, the omission-inventory exponent column, and the H-inventory generators `q2..q14,q16..q24` are that same set. There is no duplicate and no hole inside `E`.

Why `q15` is a legitimate quotient coordinate, not a silently omitted source modulus:

- f-transport is built from `{15: 1}` at degree 15: frozen `p=t^{15}`.
- g-transport is built from `{1: 1, 25: 1}` only: frozen `q=t+…+t^{25}`.
- A polynomial target shear of the pair `(p,q)` is `q ↦ q-λ p`. At this frozen F1 that adds a multiple of `t^{15}` to `q`, so the coefficient of `t^{15}` is the lower target-shear coordinate.

V87 holds that coordinate at zero: `source_value` adds a q-variable only for `e in Q_ORDER`, and `Q_PRIME` is initialized `{0:1, 24:25}` then `Q_PRIME[e-1]=e q_e` only for `e in E`. Slot `Q_PRIME[14]` stays unset. The row `('g','X',0,15)` may still occur as an ordinary q-independent transport source; it does not receive a licensed q increment. That is gauge-fixing `q15=0`, not deleting a source modulus from the chart.

Identity (1) writes the leftover as `F h_F + sum_{e in E} q_e h_e`. If some licensed `q_e` is a unit, that term need not lie in a DVR maximal ideal. The producer slogans `q15_totalized=false` and the RESULT firewall match. No unit-q claim is made.

`q1` is the normalized linear leading term of `q` and `q25` is the frozen upper boundary. Neither is in `E`.

---

## 3. Charge 2 — literal source custody

### Transport

`source_value(key)` is `QPoly(from_vector(source_vector(key)))`, plus `QPoly.variable(e)` when `key=('g','X',0,e)` for licensed `e`. The frozen adapter satisfies `from_vector(source_vector(('g','X',0,1)))=E3(1)`, so the increment is `q_e·E3(1)`, the same unit used by the reviewed q2 dual client as `ONE_VECTOR`. It is not a raw 18-vector add after the `from_vector` conversion; both sides are already in `E3`.

`propagate_all_q` counts those keys and fail-closes unless every licensed exponent occurs exactly once. Printed counts are `q2:1,…,q24:1`. Homogeneous transport is the frozen V85 rectangles `(15,60,3,{15:1})` and `(25,100,5,{1:1,25:1})`. Pivot inversion uses `lead.inverse()` of the q-independent trivariate lead, then multiplies a `QPoly`. Rank 3470/3602 with 132 free variables and two chart events is the frozen V85/V82 transport.

### Direct `q'`

```text
Q_PRIME = {0: 1, 24: 25}  and  Q_PRIME[e-1] = e q_e  for e in E, e ≠ omit_direct.
qd.B = q2.
```

Live FIRST is `first_band_polynomials`, which multiplies `f1[i]` by `Q_PRIME.get(degree-i)` and does not read `B`. Live P12 is the degree-12 CURRENT formula, which uses `Q_PRIME` in the `3 f3 q'` term and does not read `B`. After `Q_PRIME` is installed, `B` is the licensed q2 slot, historically inert for this raw FIRST/P12 compiler. `R3/R5` and `POLE_*` are configured and never consumed. Direct-omission first keys in the frozen inventory are exactly `('X-2', e-1)` for every licensed `e`, which is the `t^{e-1}` slot of `q'`. That is independent of producer banners.

### P12 extraction is literal degree 12, not staged

Frozen `compile_x_current` loops `degree in range(40)` and at a generic degree forms

```text
f1*g2' + 2 f2*g1' + 3 f3 q' - 45 g3[degree-14] - 2 f1'*g2 - f2'*g1,
```

with a degree-0 constant correction that does not apply at 12. V87 `compile_current_degree12` is that same block with `degree=12` fixed, using `qd.nr` (`scale_affine` / `multiply_affine` / `add_polynomial` / `affine_polynomial`). V86 takes `compile_current(...)[12]`, which is `compile_x_current` after rebinding `base.Q_PRIME`. There is no cross-degree state in that loop. Family label `('X0_RAW', 12)` is the V85/V86 name of this object. No post-reduction CURRENT, PREVIOUS, or POLE row is read.

### Not square-zero, not truncated

`QPoly` stores monomials as sorted tuples of exponents (with repetition), multiplies by concatenation, and has no degree cutoff. `qd.Dual` is rebound to `QPoly` before FIRST/P12. `v86.BPoly` is rebound to `QPoly` so V86 `restrict_row` / `clean` / `add` / `multiply` resolve the live type at call time. The imported shard `EJet` remains square-zero and is not the live coefficient type for this certificate.

---

## 4. Charge 3 — 44 omission fixtures

The loop is 22 exponents times two FIRST rebuilds. Original `bands` and `total_family` are computed once. `omit_transport_path` returns a new dictionary; it does not mutate `bands`. `remove_q` drops every monomial containing that exponent from already-built affine bands, which for linear transport is exactly the transport-RHS path of that variable. Direct omission calls `configure_qd(omit_direct=e)`, which rebuilds `Q_PRIME` without `Q_PRIME[e-1]` and leaves bands intact. Each `compile_first` starts with `configure_qd`, so global `qd` mutation does not leak across fixtures.

`omission_record` requires a nonempty changed-key set and a nonempty polynomial difference. Frozen inventory:

- every transport `changed_rows` is in `{1,...,12}`;
- every direct `changed_rows` is `15`;
- direct first key is `('X-2', e-1)` for every licensed `e`;
- q2 transport first key is `('X-2', 15)`, distinct from its direct key `('X-2', 1)`.

If either path were dead, one comparison would be equality and the assert would fail. That is a genuine 44-way negative control, not a self-hash. The fixtures do not rebuild P12; the charge asked for raw FIRST comparison, and P12 uses the same two live paths.

No separate `B`-path FIRST omission exists. FIRST/P12 do not consume `B`, so such a fixture would be vacuous. V87 preregistration requires the two live paths, not a third. That matches the reviewed V86 q2 fixture.

---

## 5. Charge 4 — `QPoly` and `decompose_q_residual`

Let `R=E3` and `A=R[q_e:e in E]` with the sorted-tuple monomial basis. Addition merges coefficients; multiplication is the Cauchy product; `__pow__` is binary exponentiation. `inverse` asserts `coefficients ⊆ {()}` and otherwise raises `attempted_q_polynomial_inverse`. Transport leads are q-independent, so that branch is not the pivot inverse. Receiver operations are addition and multiplication. The AWS client completed, so no q-dependent inverse was taken. Independently: FIRST and the degree-12 CURRENT formula never divide in the coefficient ring.

`decompose_q_residual` on a section-polynomial whose every coefficient has zero constant q part:

1. rejects any leftover `()` q-monomial (`q_nondivisible`);
2. assigns each nonempty q-monomial to `exponent = monomial[0]`, the least factor in `Q_ORDER`, with rest `monomial[1:]`;
3. replays `sum_e q_e h_e` and asserts equality.

This is an ordered module splitting of the augmentation ideal `I=(q_e:e in E)`. It is unique for this order and exact for arbitrary cross-q powers, including `q2 q3` and `q3^3`. The assignment `q2 q3 ↦ q2·(q3)` is not the only module splitting of `I`, but replay reconstructs the original polynomial. Coefficients stay in `R`; no q expression is inverted. A toy partition on integer coefficients, including `(2,3)`, `(2,2)`, `(16,24)`, and `(3,3,3)`, replayed exactly.

Identity (1), independently of the AWS equality flag. Write `s=U^{12} H^3 B3` and `f` for the tuple of raw P12/FIRST section-polynomials. `QPoly` plus Dual rebound plus add/mul compilers put every `f_i` in `A_S[X]`. At all q zero the 39 source digests equal frozen V85, so the reviewed V85 identity supplies `s = a·f(0) + F h_F^{V85}`. The q-zero residual is `s-a·f(0)`; V87 divides it by `F` coefficientwise in 50,346 scalar coordinates (`2797×18`) and checks `polynomial_digest(h_F)=7434b0a7…`, the frozen V85 quotient. The positive-q residual is `a·f(0)-a·f(q) ∈ I[X]`. The ordered partition writes it as `sum q_e h_e`. Therefore

```text
a·f(q) + F h_F + sum_e q_e h_e = a·f(q) + (s-a·f(0)) + (a·f(0)-a·f(q)) = s.
```

That is (1). The AWS `assert rhs==target` is this tautology executed, not an independent identity. Dual-host agreement is not the proof.

flint in `Q[C,V,U]` expands `s` to the emitted `target=` polynomial, and `U H = C U-3 U^3`. Also `B3|_{F=0}=V^4` after substituting `C U=V^2-U^3`, so on `D(U)` one has `s|_{F=0}=V^4 U^9 (V^2-4U^3)^3`. Further `gcd(F,U H)=gcd(F,B3)=gcd(F,H)=1`, so localizing at `U H B3` cannot invert `F`.

The frozen V82QST3 certificate has 1,490 nonheader rows (1 P12 + 1,489 FIRST), and every scanned polynomial denominator token is `'1'`. V87 embeds those multipliers as q-degree-zero `QPoly` values and, after substituting `C=(V^2-U^3)/U` on the all-q-zero sources, replays the special clearer.

---

## 6. Charge 5 — degree telemetry

`max_q_degree` is `max len(q_monomial)` over the live P12/FIRST (resp. residual) dictionaries. Dual-host stdout reports `total_q_degree=1` and `residual_q_degree=1`. The H inventory has `parameter_terms=coefficient_terms` for `h_F` and every `h_e`, and `sum_e coefficient_terms(h_e)=46378`, matching `q_partition_coefficient_count`. That is consistent with every quotient being q-degree 0, hence with residual total degree 1.

It does not by itself prove degree 1: a pure square `q_e^2` on a single parameter monomial would still give one coefficient per parameter after the prefix split, with rest `(e,)`. V86 closed this loophole for q2 by emitting a `beta_degree` column that was identically 0. V87 does not emit q-monomials or degrees in the H or source tables. The live walk is the actual computation on the represented polynomials; it is producer telemetry, not a second table.

Degree 1 means every q-monomial in the sources and residual has length 0 or 1, so no `q_e q_f` or `q_e^2` occurs in this family. The partition algorithm does not rely on that: it would have assigned `q2 q3` to `h_2` with rest `(3,)` and still replayed. Linearity is an empirical output, not a coefficient-type assumption. `QPoly` would have kept a Cauchy product of two q-factors.

Structural remark, not a proof: `Q_PRIME[k]` is either constant or a single licensed variable, and products `Q_PRIME[k] f1[i]` become degree 2 only if that f-band already carries q from transport mixing. The walk says those products did not survive in the packed sources. I did not re-expand the 39 source polynomials.

**Packaging repair, not the headline gap:** add a `q_monomial` or `q_degree` column to `TOTAL_F_ALLQ_H_INVENTORY.tsv` (and/or the source inventory), as V86 did for beta.

---

## 7. Charge 6 — V85 specialization holds; V86 specialization is not checked

### V85 / V82QST3, independently compared

Frozen V85 inventory SHA-256 `9a612bb6…` is the V87 case-root copy. For every one of the 39 rows, V87 `all_q_zero_sha256` equals V85 `generic_sha256` and the keys agree: P12 `('X0_RAW', 12)` and FIRST `('X-2', 0)` through `('X-2', 37)`. P12 support is asserted `len==2893`. Every V87 full digest differs from its all-q-zero digest, so some licensed q is live in genuine P12 and in every packed FIRST map. Labels collected from total P12 and FIRST are `set(range(132))`.

The same 39 all-q-zero digests equal the frozen V86 `beta_zero_sha256` column (0 mismatches). That is the common all-zero point of V85, V86, and V87, not the q2-only slice.

`EXPECTED_V85_H_SHA256 = 7434b0a7…` is checked against `polynomial_digest(h_F)` after exact `F`-division. V87 `h_F` has 2,797 parameter terms; `2797×18=50346` matches `F_division_coordinate_count`. V86 cleared `h_F` also has 2,797 terms of `beta_degree=0`. Localized `h_F` full-digest `5f429f95…` differs from V86 `d42fd419…` because `QPoly` serializes `()` where `BPoly` serializes degree `0`; that is encoding, not a different quotient. The V85 digest check is the specialization evidence.

V85 `special_sha256` for P12 is `da0d595e…`. The special-fibre replay is the gate.

### V86 total-`(F,q2)` specialization: custody/proof gap

Required check: set `q_e=0` for all `e≠2` and determine whether the represented V87 sources and identity specialize to the reviewed V86 family. The producer does not do this.

What V87 does instead:

- pins `replay_v86tfq2_total_f_q2.py` at `5b160a2b…` and imports V86 as a helper library;
- rebinds `v86.BPoly=QPoly`;
- reads the V85 inventory through `v86.read_v85_inventory`;
- prints `v86_parent_sha256=` in the exact-result file.

No V86 source inventory, `h_beta` table, or full-digest is loaded. No `q_e=0` (`e≠2`) restriction is computed. The V87 package root contains no V86 `TOTAL_F_Q2_*` artifacts.

Circumstantial numbers that are **not** the comparison:

- V87 `h_2` has 3,330 parameter terms; frozen V86 cleared `h_beta` has 3,330 terms, all `beta_degree=0`;
- V87/V86/V85 `h_F` term counts agree at 2,797;
- all-q-zero / beta-zero / V85 generic hashes agree;
- transport key `('g','X',0,2)`, `Q_PRIME[1]=2 q_2`, `B=q2`, FIRST compiler, and the degree-12 CURRENT formula agree with V86 as source text.

The charge forbids promoting that source-text agreement to a specialization theorem. Full source hashes cannot match even under a true specialization: V87 `full_digest` writes `q_monomial` tuples over 22 variables, V86 writes a beta degree integer, and V87 full polynomials still contain `q3,…,q24`. Without an emitted restriction or a common encoding, the reviewer cannot finish the comparison from the frozen tables. Inferring it from the parent client is exactly the forbidden move.

**Smallest repair** is the gate in the verdict section. Optional strengthening: emit the restricted P12/FIRST/`h_2` digests in the V86 encoding so a later review can check the gate without re-running the 19-minute client.

This gap does not disturb the independent proof of (1) in §5. It disturbs the claim that the represented all-q family is the reviewed q2 family with the other jets restored.

---

## 8. Charge 7 — denominators and clearing

Audited list in source:

```text
q_p12_multiplier, all 38 q_first_multipliers,
total_p12, all 38 total_sources, all used products,
embed(h_F), all 22 h_e.
```

That is multipliers, all sources, all products, `h_F`, and all 22 `h_e`. Residual and target are not separately listed; target is the polynomial `s`, and residual is `s` minus the audited combination. Common denominator is computed by `denominator_for` on those E3 values, required to factor only in `{U,H,B3}`, and required to be coprime to `F`. Printed value is `C*U-3*U^3=U H`, factored `(U,1)·(C-3U^2,1)`. The allowed `B3` factor is not needed for clearing. flint confirms `gcd(F,U H)=1`. `QPoly.inverse` refuses nonconstant q, and the frozen multiplier table has polynomial denominator `1` in every scanned coordinate, so neither `F` nor a q variable is inverted.

`assert_polynomial_after_clear` multiplies each of the 312,604 E3 coefficients by `U H` and checks all 18 scalar denominators become `1`. `312604×18=5,626,872`, matching `cleared_polynomial_scalar_coordinate_count`. One clearing of the already-replayed identity `rhs==target` is then `scale(rhs,U H)==scale(target,U H)`.

P12 and FIRST-0 replay omissions subtract the corresponding used term from `total_identity` and require the identity to fail. FIRST index 0 is `min(used_keys)` of the frozen V82QST3 table, one of the 28 active rows. P12 has a nonzero frozen multiplier. Neither control hashes an object against itself.

---

## 9. Charge 8 — dual AWS custody

| | Box02 | r6d |
|---|---|---|
| hostname | `ip-172-30-0-186` | `ip-172-30-0-45` |
| endpoint (launch record) | `34.203.207.55` | `100.26.198.153` |
| tag | `…_box02_20260826T150610Z` | `…_r6d_20260826T150610Z` |
| archive | `e80b1cba…` | `e80b1cba…` |
| `rc` | `0` | `0` |
| elapsed | 19:26.61 | 19:27.93 |
| max RSS KiB | 3,762,460 | 3,762,384 |
| swaps | 0 | 0 |
| VM cap KiB | 268,435,456 (256 GiB) | same |
| math stdout SHA-256 | `7b741c31…` | `7b741c31…` |

Byte-identical across hosts, as they must be: the four mathematical outputs and stdout. Distinct, as they should be: `pid`, `launch.meta`, `finished_utc`, `fleet_finished_utc`, `fleet_supervisor.pid`, `registration.meta`, and `stderr` (time/RSS lines). Empty `wrapper.log` and `fleet_supervisor.log` are identical empty files. `ulimit -v 268435456` is in `launch_host.sh`. Wrapper requires Linux, Amazon EC2, `AWS_RUN_TAG=td6_v87tfaq_total_f_allq_*`, and `TD6_Q_EXPONENT=2`. The last is a V85 parent import constraint, not a restriction of `Q_EXPONENTS` to `{2}`.

Mathematical equality of two executions is custody that the freeze ran twice. It is not the identity in §5.

---

## 10. Charge 9 — DVR consequence

On `D(U H B3)`, `s` is a unit. Identity (1) writes `s` as a combination of the raw P12/FIRST rows plus `F h_F+sum_{e in E} q_e h_e`, and every coefficient of `h_F` and of each `h_e` lies in the registered localization (denominator `U H`). If a DVR arc in this retained family kills every raw row and puts `F` and all 22 licensed q coordinates in the maximal ideal, the right side has positive valuation and the left side does not.

This uses `F` and every licensed `q_e` together. If some `v(q_e)=0`, the corresponding `q_e h_e` need not lie in the maximal ideal. If `v(F)=0`, positive-`F` is not excluded. `q15` is not a variable of this ring. Dead stretch, correction, F1-orbit/pole, centering, deck/torsion, and other boundary moduli are not variables of this ring. The 132 section coordinates remain free parameters. The identity totalizes only the literal tuple `(F, q_e:e in E)` on one normalized source slice.

RESULT's slogan `positive_F_and_all_licensed_q_arcs_on_this_slice_excluded` matches that DVR statement and no larger one.

Rejected extensions: unit-q chart, q15, omitted correction/orbit/pole/center/deck/torsion/boundary variables, a total-Rees chart, whole fixed A3, TD6, SP-2, JC2.

---

## 11. Failed attacks

- **Silently omitted q15 as a source hole.** q15 is the `t^{15}` coefficient of `q` under target shear of frozen `p=t^{15}`. `Q_PRIME[14]` is unset; `15 not in Q_EXPONENTS`; transport increment is not applied at e=15.
- **Square-zero truncation.** `QPoly` keeps Cauchy products. A residual of degree ≥2 would have been partitioned, not dropped. The live degree walk reported 1; the type did not impose it.
- **Hidden `F` inversion.** `gcd(F,U H)=1`; every scanned V82QST3 denominator is `1`; `divide_polynomial_by_f` checks `divided*F==coordinate` in 50,346 scalars.
- **Hidden q inversion.** `QPoly.inverse` fail-closes on any positive q degree; AWS completed.
- **Inert `B` as a missing live path.** FIRST/P12 read `Q_PRIME`, not `B`. The two live paths are independently omit-controlled on FIRST. Direct first keys are the `q'` slots.
- **Self-referential omissions.** Path omissions rebuild FIRST from altered compiler state. Row omissions subtract used multiplier terms.
- **Staged CURRENT / PREVIOUS / POLE.** P12 is the degree-12 formula of `compile_x_current`. Pole polynomials are configured and unused.
- **V85 identity inherited as a banner.** All-q-zero sources are digest-identical to V85 generic sources; `h_F` digest is the V85 quotient; `F=0` specialization of `s` is the V82QST3 clearer.
- **Dual-host PASS as algebra.** Used only as custody.
- **Unit-q, q15, other moduli, whole TD6.** None of these are licensed by (1) or by the RESULT firewall.

---

## 12. Defects

1. **Headline repair — V86 specialization not compared.** See verdict. Circumstantial term counts and shared compiler text are not a substitute.
2. **Degree tables omit q-monomials.** V86 emitted `beta_degree`. V87 H inventory counts are consistent with degree 1 but do not rule out pure squares without the live walk. Smallest packaging repair: emit `q_degree` or `q_monomial` in the H inventory.
3. **`F_allq_decomposition_exact=true` is printed after the replay assert, which is correct order.** No banner-order defect analogous to V86's special-identity slogan was found here.
4. Producer ring slogan `Q[C,V,U,q_e]_{U H B3}` omits the 132 section coordinates. The identity is in the section-polynomial ring. Prose imprecision only.

Defect 1 is the required custody/proof gap. Defects 2–4 do not break (1).

---

## 13. Firewall

This review confirms a literal total-`(F, q2..q14,q16..q24)` raw P12/FIRST identity on one normalized source slice, subject to the V86-lineage repair above. It does not totalize `q15`, a unit q coordinate, dead stretch, correction, orbit/pole, centering, deck/torsion, or other boundary moduli; supply a full total-Rees chart; or prove a whole fixed A3, TD6, SP-2, or JC2 statement.

---

## Dependency table

| Producer assertion | Independently checked evidence | Verdict | Smallest repair |
|---|---|---|---|
| 22-jet family is `q2..q14,q16..q24` | `Q_EXPONENTS`, omission exponents, H generators, `15 not in` | confirmed | — |
| q15 is lower target-shear of `p=t^{15}`, not an omitted modulus | f-boundary `{15:1}`, g-boundary `{1:1,25:1}`, shear `q↦q-λp`, `Q_PRIME[14]` unset | confirmed | — |
| (1) makes no unit-q claim | leftover `sum q_e h_e`; slogans | confirmed | — |
| Each `q_e` enters transport `('g','X',0,e)` and `e q_e t^{e-1}` in `q'` | `source_value`, `Q_PRIME[e-1]`, omission first keys `('X-2', e-1)`, path counts all 1 | confirmed | — |
| Transport not square-zero / not truncated | `QPoly` Cauchy product; Dual rebound; no degree cap | confirmed | — |
| Raw degree-12 CURRENT, no staged CURRENT/PREVIOUS/POLE | literal `compile_x_current` at degree 12; pole unused | confirmed | — |
| 44 fixtures separately kill transport or direct, FIRST comparison nonvacuous, no shared mutation | 22×2 rebuilds; all changed_rows>0; new band dicts; `configure_qd` reset | confirmed | — |
| `QPoly` exact; `decompose_q_residual` exact on the augmentation ideal, including cross-q; no q-division in `R` | type audit; ordered prefix split; toy replay; fail-closed inverse | confirmed | — |
| Identity (1) in `Q[C,V,U,q_e][X]_{U H B3}` | polynomiality + V85 hashes + exact `F`-division + exact partition; flint `s` and `gcd(F,U H)=1` | confirmed | — |
| `total_q_degree=residual_q_degree=1`; no cross-q here; partition does not assume linearity | dual-host `max_q_degree` walk; H counts consistent; type allows higher degree | confirmed on the live walk; tables incomplete | emit `q_degree`/`q_monomial` in H inventory |
| All-q-zero P12/FIRST = frozen V85; 2,893-term P12; labels `0..131` | 39/39 digest match; `len==2893`; `labels==range(132)` | confirmed | — |
| Frozen V82QST3 special identity | replay `special_identity=={(): SPECIAL_CLEARER}`; `s\|_{F=0}=V^4 U^9 (V^2-4U^3)^3`; cert 1,490 rows, dens `1` | confirmed | — |
| q-zero `F` quotient = frozen V85 `h_F` | `polynomial_digest(h_F)=7434b0a7…`; 2,797 terms; `2797×18=50346` | confirmed | — |
| V87 at `q_e=0` (`e≠2`) is reviewed V86 total-`(F,q2)` | parent-client pin and shared code only; no table comparison; 3330/2797 counts are not enough | **gap** | restrict V87 objects to q2 and compare to frozen V86 inventories/`h` tables under a common encoding; pin those artifacts |
| 312,604-value denominator audit; LCM exactly `U H`; no `F` or q inverted; one clearing of 5,626,872 scalars | audited list; flint gcd; `312604×18=5626872`; multiplier dens `1`; fail-closed q inverse | confirmed | — |
| P12/FIRST omission negatives | subtract used terms; FIRST index 0 active | confirmed | — |
| Dual AWS: same math, different host metadata; zero swap; RSS/elapsed | hashes; `rc=0`; stderr time/RSS; distinct hostnames/pids | confirmed as custody | — |
| No DVR arc on `D(U H B3)` with all P12/FIRST zero and `v(F)>0`, `v(q_e)>0` for all 22 licensed q; every `h` regular there | (1) + unit `s` + denominators `U H` | confirmed on this slice | — |
| No extension to unit-q, q15, omitted moduli, total-Rees, A3, TD6, SP-2, JC2 | firewall slogans and the actual variable set of (1) | confirmed | — |

REPAIR
