# Hostile review V2 — TD6 V89H4 high-q total-F K repair

| Field | Value |
|---|---|
| Target | V89H4 `RESULT.md`, `EVIDENCE.sha256`, `FREEZE.sha256`, `SOURCE.sha256`; two AWS evidence trees |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest bad coefficient / denominator / omission | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile review. Producer `PASS` banners, dual-host byte identity, and RSS/elapsed lines are custody only |
| Method | SHA-256 of every charged pin and every consumed manifest row; flint identities in `Q[C,V,U]`; tablewise replay of the frozen 2,651-row multiplier file against independently expanded `K`, `F`, `G`, `B3`, `H`; DAG nilpotence from the frozen 242-edge graph; source review of V87 reconstruction, `QPoly.inverse`, P12 division, and the K-clearing/F-composition. No Singular, Sage, Lean, or `jc2-lean`. The 22-minute AWS client was not re-executed; the H1 reconstruction is recovered from hash-locked H1 artifacts plus the live client's asserted original-source replay, and the total-F step is recovered from the frozen table plus flint |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Base prompt SHA-256 `86d11059850b2abb66c0c00e903602b41b2f6a09e0748c864ad1125c083b6b99` matched. Independently recomputed SHA-256 of all six required primary pins match. Every path named in `EVIDENCE.sha256` (32/32) and `FREEZE.sha256` (9/9) rehashes to the printed digest. Every `SOURCE.sha256` row exists at the case root and as `source/<path>` inside `source.tar.gz`, and both copies match. Nested compiler hash pins consumed from that archive also match. Producer `TD6-V89H4-HIGH-Q-TOTAL-F-K-REPAIR PASS` was not used as algebra. No file other than this review was written. The base-prompt report path was not created.

---

## Verdict

**CONFIRMED.**

On the retained high-q residue obtained by setting `q2,...,q14=0`, omitting `q15` as the lower target-shear of the frozen pair `(p,q)=(t^{15},q)`, and keeping independent untruncated `q16,...,q24`, the rebuilt raw P12, 38 packed FIRST maps, and literal `F=CU-V^2+U^3` satisfy the exact identity

```text
(1/8) B3^2 U^2 H^2
  = a_P P12
    + sum_i a_i FIRST_i
    + F * (2 A G)                                 (1)
```

in `Q[C,V,U,q16,...,q24][X_0,...,X_{131}]_{U H B3}`, where `H=C-3U^2`, `B3` is the displayed sextic,

```text
K = 2 C V^2 U + 16 C U^4 - V^4 - 14 V^2 U^3 + 16 U^6,
G = 2 C U - V^2 + 2 U^3,
A = (1/8) B3 U^2 H^2,
```

and the 2,651 nonzero multiplier coordinates `(a_P, a_i, 2 A G)` are the frozen table
`HIGH_Q_TOTAL_F_CLEARED_MULTIPLIERS.tsv`. The coefficient ring in the nine high-q jets is an untruncated sparse multivariate polynomial ring. Inversion of any nonconstant q polynomial is a closed failure. No inverse of `K` or `F` is used.

The H1 preclear denominator is exactly `(1/8) K B3 U^2 H^2` with `K` to exponent one. Clearing that relation coefficientwise and consuming the independently expanded identity

```text
B3 = K + 2 F G                                    (2)
```

replaces the unregistered factor `K` by the registered unit `B3` without dividing by `K` or `F`. The final family common denominator is `U H`. On the registered open `D(U H B3)`, every remaining denominator factor and the target of (1) are units, so the literal ideal `(P12, FIRST, F)` is the unit ideal on this high-q residue block. This is a total-F identity: omitting `F`, literal P12, or the charged FIRST row (index 0) breaks (1). It is not a P12/FIRST-only collapse.

On `D(U H B3)` this excludes DVR arcs in the retained high-q source family on which all raw P12/FIRST rows vanish and `F` has positive valuation. It does not cover any low-q unit chart, q15, total-Rees/source lifting, omitted correction or moving-center variables, a source point, or any whole fixed A3, TD6, SP-2, or JC2 statement.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Six primary pins | hashes | all six match the required bytes |
| 0. Evidence / freeze | every named file | `EVIDENCE.sha256` 32/32, `FREEZE.sha256` 9/9 |
| 0. Source manifest | AWS working directory | 23/23 at case root and 23/23 inside `source.tar.gz` |
| 0. Nested compiler pins | shard / V32 / tri / two-center / QDUAL / q2-base / V87 / V86 / V85 | all hash-pins match |
| 0. Dual AWS | hosts, archive, rc | distinct Box02 / r6d; archive `84199204…`; `rc=0`; math stdout and five output files byte-identical |
| 1. High-q scope | `q16..q24` retained | `HIGH=range(16,25)`; projection keeps only those exponents; table q-support is exactly that set |
| 1. Low-q zero | `q2..q14=0` | `LOW=range(2,15)`; mixed high-low monomials drop as in specialization; no low-q exponent in the 2,651-row table |
| 1. q15 | target-shear omission | `15` absent from `Q_EXPONENTS`; f-transport `{15:1}`, g-transport `{1:1,25:1}`; `Q_PRIME[14]` unset |
| 2. V87 rebuild | literal transport / FIRST / P12 | live import of pinned V87 client `7c0890ab…`; 38 packed `X-2` rows; inlined degree-12 CURRENT |
| 2. V85 q-zero | 39 source digests | q-constant P12/FIRST compared to frozen V85 generic inventory `9a612bb6…`; H1 remainder digest `93121eef…` is the same generic remainder |
| 2. 242-edge DAG | acyclicity and `N^2=0` | 242 edges, all from rows 14–36 to columns 0–13; source/dest disjoint so `N^2=0`; printed Kahn order reproduced |
| 2. Two-sided inverse | triangular `I+N` | diagonal ones, strict upper triangular in the printed order; inverse is polynomial (`I-N`); no q inverse |
| 2. Remainder | q-zero unit | one parameter/q monomial `()`; four nonzero dual-Q coordinates; zero positive high-q terms |
| 2. P12/FIRST omission | H1 reconstruction | original-source replay and P12/FIRST-0 controls are live asserts; artifacts byte-identical to frozen H1 |
| 3. Preclear denominator | `(1/8) K B3 U^2 H^2` | flint factorization of the emitted `h1_common` is exactly that, `K` exponent 1, `gcd(K,U)=gcd(K,H)=gcd(K,B3)=gcd(K,F)=1` |
| 4. Identity (2) | `B3=K+2FG` | flint expansion is zero; coefficient-1 negative control is nonzero |
| 4. Composition | target `(1/8) B3^2 U^2 H^2` | `A=(1/8)B3 U^2 H^2` and `A B3` match the emitted polynomials coefficientwise; `K A + 2 A F G = A B3` |
| 4. No `K`/`F`/`q` inverse | emitted identity | K is multiplied through then replaced by (2); F is a generator; `QPoly.inverse` fail-closes on nonconstant q |
| 5. 2,651 multipliers | frozen table vs P12/FIRST/F | 1 P12 + 2,649 FIRST + 1 F; FIRST counts equal the H1 inventory termwise; F slot 0 equals `2 A G`; P12 slot 0 equals `(-133624/21075) A K` |
| 5. Final denominator | `U H` | all 2,651 Rat3 denominators are `1`; remaining LCM `U H` is from the sources; `gcd(F,U H)=gcd(F,B3)=1` |
| 5. Omission controls | P12 / FIRST-0 / F | F omission is (2) with the `2FG` term dropped; P12 and FIRST-0 multipliers are nonzero; unused FIRST 28–37 are the H1 zeros |
| 6. Scope firewall | high-q total-F only | slogans and preregistration keep the charged firewall; no P12/FIRST-only, low-q, source-point, A3, TD6, SP-2, or JC2 claim |

---

## 1. Custody

Recomputed SHA-256 of the six required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `RESULT.md` | `8db237a7c466b420060623576b9d778427392fd827a3af856d276707dd618546` | producer result |
| `EVIDENCE.sha256` | `70625a4460778bab5b14ae736b548c963952f5ce052819f6491928ef1a08340d` | evidence manifest |
| `FREEZE.sha256` | `3406db430e1a23bae2e3755f5dca3135773aced2af032c621ae1bbc0e28c3721` | freeze |
| `source.tar.gz` | `84199204a41f7d26bcc6a1329cd72bedf2c60a0ae9590cf1cd04ee5373230d91` | source archive |
| `HIGH_Q_TOTAL_F_K_REPAIR_EXACT_RESULT.txt` | `d51b6cbc6beb807e8a220c0a097139f4e033d6135caf44c56e89b4493161f098` | exact result |
| `HIGH_Q_TOTAL_F_CLEARED_MULTIPLIERS.tsv` | `e3793a7add52c22a7fff745ce196f5dad8c0cd7e4d5407c0e11295484df3ecf2` | cleared multipliers |

`SOURCE.sha256` itself is `c9f6b7078bfbf8b0bdd3df71e50e54303b36d88c25e748b2802a7cdab48bc842`, matching the freeze row and the copy inside the tarball. The client pin `6e810be852691aa5aa2f60b85a3996c3146ae72e6bae28fed1903c35de05bf61` matches freeze and SOURCE. Byte-identical mathematical stdout is `41df45c84197b5ec44d7d779c24b81e35f1297ed0ea49d7cb66186c887a5d288` on both hosts.

Nested compiler pins reached from the frozen shard, independently rehashed:

| Pin | SHA-256 |
|---|---|
| V87 parent client | `7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463` |
| V86 parent client | `5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c` |
| V85 parent client | `ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e` |
| generic parent shard | `a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e` |
| V32 q2 dual client | `dcc7003def824c0d2a88998cbf22a66f022a32714f05754c505e8d825bd91742` |
| trivariate adapter | `1fb512643f31b4eda6c0e96ca1adbfe3e79599986c7c095b825605a4145fdaea` |
| two-center `replay.py` | `56df638aaa3ae02cf437a32258a920a8a66afb2781c089e30b1774a5b38e65db` |
| QDUAL `jet_orbit_adjoint` | `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198` |
| q2 base `boundary_q2_deformation` | `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357` |
| V85 source inventory | `9a612bb64ee974a506a1f3b7fcb471fb8924220ca6d24320af0fc9b8a7de6b7a` |
| H1 `RESULT.md` | `0fd09839dc0e6ec50bd5d58c23e294af252a6a769499429ea512fb64664f81f0` |
| H1 `K_FORMULA.txt` | `2db6935d74924896248fa192120888d8067004a314e4f8fc41c581a7675c2f87` |
| V89K1 `RESULT.md` | `2c57d8924eba299906b73ba1889eae309fc7baf01d91322561d6be62d5327907` |

Box02 (`ip-172-30-0-186`, pid 291004) and r6d (`ip-172-30-0-45`, pid 306837) are distinct hosts with distinct tags, the same archive `84199204…`, `rc=0`, and zero swap. Mathematical stdout and the five output files are byte-identical. Host stderr differs only in `/usr/bin/time` counters (22:01.07 vs 21:58.13; RSS 777,840 vs 779,072 KiB). `launch.meta`, `registration.meta`, pids, and finish timestamps differ as they should. Dual-host equality is custody, not the identity.

The H1 graph `318e11df…`, P12 remainder `763e0d82…`, and original-source inventory `bd94a903…` are byte-identical to the frozen H1 evidence trees. V89H4 recomputes those objects from the pinned V87 client; it does not copy H1 outputs into the run directory.

---

## 2. Charge 1 — exact high-q residue, q2–q14 zero, q15 shear

`Q_EXPONENTS = tuple(range(2,15))+tuple(range(16,25))` has length 22 and does not contain 15. The V89H4 client splits that set as `HIGH=range(16,25)` and `LOW=range(2,15)` and asserts the union is exactly `Q_EXPONENTS`. Projection of a `QPoly` keeps a monomial if and only if every exponent lies in `HIGH`. Empty monomials (q-constants) are kept. A mixed monomial such as `q2 q16` is dropped, which is the correct specialization `q2=…=q14=0`. No emitted multiplier q-monomial carries an exponent outside `{16,…,24}`.

Why `q15` is a legitimate quotient coordinate, not a silently omitted source modulus:

- f-transport is built from `{15: 1}` at degree 15: frozen `p=t^{15}`.
- g-transport is built from `{1: 1, 25: 1}` only: frozen `q=t+…+t^{25}`.
- `Q_PRIME` is initialized to `{0: 1, 24: 25}` and then `Q_PRIME[e-1]=e q_e` for each licensed `e`. The key `14` is never written, so there is no direct `q15` path.
- A polynomial target shear `q ↦ q-λ p` at this frozen F1 adds a multiple of `t^{15}` to `q`. Holding that coefficient at zero is a gauge, recorded as `q15_absent_target_shear=true`.

Wrapper environment `TD6_Q_SCOPE=high-q16-q24` matches this split. The result does not claim a unit-q chart or any low-q cover (`low_q_unit_charts_covered=false`).

---

## 3. Charge 2 — V87 reconstruction, V85 q-zero, DAG, inverse, remainder

The client imports pinned V87 `replay_v87tfaq_total_f_allq.py`, rebinds `QPoly` as the untruncated sparse E3-coefficient ring, rebuilds transport bands, packs 38 raw FIRST rows, and extracts literal degree-12 CURRENT. `QPoly.inverse` raises unless the support is the empty q-monomial, so no q expression is inverted. `compile_current_degree12` is the inlined raw CURRENT formula, not staged CURRENT/PREVIOUS/POLE.

q-constant P12 and the 38 q-constant FIRST sources are digested with the V85 encoding and compared to the frozen generic column of `V85_TOTAL_F_SOURCE_INVENTORY.tsv`, including genuine P12 digest `8d5c3550…`. The q-zero remainder digest is pinned to `93121eef…`, the same digest the shard records for the generic remainder `{(): -k/50}`. That is a dual-Q unit, not a C,V,U polynomial, and it is the entire P12 remainder file: one row, parameter monomial `()`, q-monomial `()`, four nonzero rational dual coordinates `(-126/25, 171/25, -72/25, 18/25)`, fourteen zeros, no positive high-q term.

The q-zero FIRST pivot block `A0` is inverted over E3 constants. `B=A0^{-1} A = I+N` with every entry of `N` having zero constant term. The frozen graph has 242 edges. Every edge runs from a row in `{14,…,36}` to a column in `{0,…,13}`. Source rows and destination columns are disjoint, so `N^2=0` and the finite inverse is `I-N`. Independently: the printed topological order is the unique sorted Kahn order of that graph, and every edge is forward in that order. The client then checks both matrix products `B (I-N)` and `(I-N) B` as identities in `QPoly`. Normalized FIRST rows are original-source linear combinations via `T=(I-N) A0^{-1}` and replay to the pivot identity. P12 divided by those normalized rows replays to P12. Pushing the quotients through `T` recovers original-source multipliers whose FIRST-0 omission is nonzero. Those live asserts are the H1 reconstruction; their emitted artifacts match frozen H1 byte for byte.

---

## 4. Charge 3 — preclear denominator and K exponent one

The emitted H1 common denominator is the displayed degree-18 polynomial `h1_common`. Independent flint factorization is

```text
(1/8) K B3 U^2 H^2
```

with each of `K`, `B3`, `U`, `H` irreducible in `Q[C,V,U]` and

```text
gcd(K,U)=gcd(K,H)=gcd(K,B3)=gcd(K,F)=1.
```

So the exponent of `K` is exactly one: it cannot hide in `B3`, `U`, or `H`, and a second copy would be visible in the factorization. The stripped allowed part is exactly

```text
A = (1/8) B3 U^2 H^2,
```

matching the emitted `allowed_part` coefficientwise, and `K A = h1_common`. Allowed factors are the registered set `{U,H,B3}` up to the scalar unit `1/8`. `gcd(A,F)=1`.

This is the H1 obstruction, not a licensed inverse of `K`. V89H4 multiplies the rational H1 identity through by `h1_common` and then uses (2).

---

## 5. Charge 4 — identity (2) and coefficientwise composition

Literal V85 formulas, expanded in flint:

```text
F  = C U - V^2 + U^3
B3 = 4 C^2 U^2 - 4 C V^2 U + 24 C U^4 + V^4 - 20 V^2 U^3 + 20 U^6
K  = 2 C V^2 U + 16 C U^4 - V^4 - 14 V^2 U^3 + 16 U^6
G  = 2 C U - V^2 + 2 U^3
```

give `B3 - K - 2 F G = 0` and `B3 - K - F G ≠ 0`. That is the frozen V89K1 identity, checked here from the formulas without the V89K1 runtime. Consequently

```text
K A + 2 A F G = A (K + 2 F G) = A B3 = (1/8) B3^2 U^2 H^2.
```

The emitted `total_target` equals `A B3` coefficientwise, and its factorization is `(1/8) B3^2 U^2 H^2`. No inverse of `K` or `F` appears: `K` is a numerator factor of the cleared H1 target and is rewritten by (2); `F` is introduced as a generator with polynomial multiplier `2 A G`.

---

## 6. Charge 5 — 2,651 multipliers, final denominator `U H`, omissions

The frozen table has exactly 2,651 data rows: 1 P12, 2,649 FIRST, 1 F. FIRST indices present are `0..27`; indices `28..37` are the H1 zero relations (inventory `parameter_terms=0`). Every Rat3 denominator coordinate in the 18-wide E3 encoding is `1`. Q-exponents that occur are exactly `{16,…,24}`.

Independent coefficient checks against literal `F` and the H1 target:

- F multiplier is a single q-constant with E3 slot 0 equal to `2 A G` as flint polynomials, remaining slots zero. That is the literal `F` coordinate of (1).
- P12 multiplier is a single q-constant whose E3 slot 0 equals `(-133624/21075) K A = (-133624/21075) h1_common`, remainder zero on division. The other five nonzero dual slots are the dual companions of that same polynomial, as required by multiplying the dual-Q remainder inverse by `h1_common`.
- FIRST coefficient counts by index equal the H1 original-source inventory `coefficient_terms` with no extra terms and no cancellation. The cleared FIRST table is therefore the H1 original-source multipliers scaled by the q-constant `h1_common * (-unit_inverse)`.

H1 already replayed those original-source multipliers against literal P12 and the 38 FIRST sources, leaving the q-zero unit. V89H4 reproduces that reconstruction (hash-identical graph, remainder, inventory) and then scales. Adding the independently matched F term replaces `K A` by `A B3` via (2). That is the replay of the 2,651 frozen coordinates against literal P12, the 38 original FIRST sources, and literal F.

Final family common denominator of sources, multipliers, F-term, and target is `C U - 3 U^3 = U H`. Multipliers themselves are polynomial (monic LCM of their denominators has degree 0). Remaining `U H` poles sit in the sources. `gcd(F, U H)=gcd(F, B3)=1`, so neither F nor B3 is inverted. On `D(U H B3)` the denominator `U H` and the target `(1/8) B3^2 U^2 H^2` are units.

Omission:

- Dropping F leaves target `K A` instead of `A B3`. Independently `2 A F G ≠ 0`.
- P12 multiplier is a nonzero dual multiple of `K A`, so dropping P12 breaks (1).
- FIRST index 0 has 174 nonzero cleared coordinates and is the charged H1 active row. Dropping it breaks (1). Unused rows 28–37 are not charged.

---

## 7. Charge 6 — scope firewall

The identity is a literal total-F unit-ideal theorem on the high-q residue block, localized at the registered open `D(U H B3)`. It is not:

- a P12/FIRST-only identity (`high_q_P12_FIRST_only_collapse_claim=false`; F is required);
- a low-q unit-chart cover (`q2..q14` are specialized to zero);
- a total-Rees or source lift, a source point, or a statement about omitted correction, orbit/pole, moving-center, deck/torsion, or dead-stretch variables;
- a whole fixed-A3, TD6, SP-2, or JC2 result (`whole_fixed_A3_killed=false`, `whole_TD6_killed=false`, `SP2_killed=false`, `JC2_resolved=false`).

V89K1 is used only as the coefficientwise identity (2). It does not make `K` a unit modulo `(P12, FIRST)` without F. H1's rational collapse on `D(U H B3)` remains withdrawn; this package repairs that collapse by adjoining F, not by licensing K as a chart unit.

---

## 8. Inverse gates

| Gate | What is inverted | Allowed? |
|---|---|---|
| `QPoly.inverse` | q-nonconstant polynomials | no; fail-closed |
| remainder unit | dual-Q E3 constant | yes; scalar unit, no `K`/`F`/`q` |
| `A0` | q-zero E3 pivot block | yes, in the rational H1 identity; cleared by multiplying through by `h1_common` |
| `B=I+N` | polynomial, `N^2=0` | inverse is `I-N`; no division |
| `K` | never | replaced by (2) after clearing |
| `F` | never | generator of the total-F ideal |
| `B3` | never divided | appears in the target; localized as a unit on `D(B3)` |

`factors_allowed` accepts only monic factors in `{U,H,B3}`. It is applied to `A` and to the final common denominator, not to `h1_common` (which still contains `K`).

---

**CONFIRMED**
