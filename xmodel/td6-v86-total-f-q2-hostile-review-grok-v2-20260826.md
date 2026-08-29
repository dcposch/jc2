# Hostile review V2 — TD6 V86 literal total-`(F,q2)` raw-source certificate

| Field | Value |
|---|---|
| Target | V86TFQ2 `RESULT.md`, `EVIDENCE.sha256`, `FREEZE.sha256`, `SOURCE.sha256`; V85 source-DAG design note |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest bad coefficient / denominator / omission | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile review. Producer `PASS` banners, dual-host byte identity, and RSS/elapsed lines are custody only |
| Method | SHA-256 of every charged pin and every consumed manifest row; flint identities in `Q[C,V,U]`; tablewise comparison of frozen V85 inventory and cleared `h_F`/`h_beta`; source review of both beta paths, `BPoly`, inverse gates, and omission controls. No Singular, Sage, Lean, or `jc2-lean`. The 17-minute AWS client was not re-executed; the total identity is recovered by exact divided differences from hash-locked V85 sources |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

The V1 review launch is cancelled no-verdict custody: it paired freeze hash `82083dd2…` with path `SOURCE.sha256`. This V2 assignment uses the corrected pairing. Independently recomputed SHA-256 of all five required primary pins match. Every path named in `EVIDENCE.sha256` (30/30) and `FREEZE.sha256` (41/41) rehashes to the printed digest. `SOURCE.sha256` is an AWS working-directory manifest: five rows exist at the case root and match; the remaining three rows exist inside `source.tar.gz` under `source/` and match there. Nested compiler hash pins consumed from that archive also match. Producer `TD6-V86TFQ2-LITERAL-TOTAL-F-Q2-RAW-P12-SOURCE PASS` was not used as algebra. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the normalized three-center source chart, with the frozen V82QST3 multipliers `a_P,a_i` and with `q=t+beta t^2+t^{25}`, the rebuilt raw P12 and 38 packed FIRST maps satisfy

```text
U^12 H^3 B3
  = a_P P12(C,V,U,beta)
    + sum_i a_i FIRST_i(C,V,U,beta)
    + F h_F + beta h_beta
```

in `Q[C,V,U,beta][X_0,…,X_{131}]_{U H B3}`, where `F=CU-V^2+U^3`, `H=C-3U^2`, and `B3` is the displayed sextic. The coefficient ring in `beta` is an untruncated sparse polynomial ring. Both live beta paths are present: affine transport RHS at `('g','X',0,2)`, and receiver `q'=1+2 beta t+25 t^{24}`. The licensed load coordinate is `B=beta`. At `beta=0` the 39 source digests equal the frozen V85 generic inventory, including the genuine 2,893-term P12 digest `8d5c3550…`. At `F=beta=0` the frozen V82QST3 clearer `V^4 U^9 (V^2-4U^3)^3` is the exact specialization of the left side, and the frozen 1,490-row multiplier table has polynomial denominator `1` in every coordinate.

The identity is the V85 total-`F` identity plus the exact divided-difference in `beta`. Independently: `U^12 H^3 B3` expands to the emitted target polynomial; `U H=F+(V^2-4U^3)` and `B3≡V^4 (mod F)` on `D(U)`; `gcd(F,U H)=gcd(F,B3)=1`; the cleared `h_F` table is coefficientwise identical to the frozen V85 cleared `h`; the cleared `h_beta` table is beta-degree zero in all 3,330 terms. No hidden inversion of `F` or `beta`, and no coefficient truncation, is present in the coefficient type or in the emitted tables.

On `D(U H B3)` this excludes DVR arcs in the retained literal `(F,q2)` source family on which all raw P12/FIRST rows vanish and both `F` and `beta` have positive valuation. It does not exclude beta-unit fibres, other `q` jets, dead stretch, correction, orbit/pole, centering, boundary moduli, a full total-Rees chart, or any whole fixed A3, TD6, SP-2, or JC2 statement.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Five primary pins | hashes | all five match the required bytes |
| 0. Evidence / freeze | every named file | `EVIDENCE.sha256` 30/30, `FREEZE.sha256` 41/41 |
| 0. Source manifest | AWS working directory | 5/5 at case root; 3/3 inside `source.tar.gz` |
| 0. Nested compiler pins | shard / V32 / tri / QDUAL / q2-base / V82QST3 cert | all hash-pins match |
| 0. Dual AWS V3 | hosts, archive, rc | distinct Box03 / r6d; V3 archive `a7e3681d…`; `rc=0`; math stdout and four output files byte-identical |
| 1. Genuine P12 | 2,893-term V85 P12 | beta-zero P12 digest `8d5c3550…` equals frozen V85 generic P12 |
| 1. 38 FIRST maps | packed `X-2` rows | inventory keys `('X-2',0)` through `('X-2',37)`; all 38 beta-zero digests equal V85 |
| 1. 132 section coordinates | labels `0..131` | inherited from hash-identical V85 generic sources; total labels asserted not to grow |
| 1. Transport beta path | `('g','X',0,2)` | affine `+beta·1` on the frozen source vector; FIRST-omission control rebuilds without it |
| 1. Direct `q'` path | `1+2 beta t+25 t^{24}` | `Q_PRIME={0:1,1:2 beta,24:25}`; FIRST-omission control drops `Q_PRIME[1]` |
| 1. `B=q2` | licensed load | `qd.B=beta`; live receiver derivative is `Q_PRIME`; `B` is historically inert after that replacement |
| 2. V85 specialization | beta-zero inventory | 39/39 generic/beta-zero SHA-256 and keys match; every full digest differs |
| 2. V82QST3 specialization | `F=beta=0` | special P12 digest `da0d595e…` is the frozen V82QST3 P12; multipliers are the frozen 1,490-row table |
| 2. Omission controls | paths and rows | both FIRST path omissions compare independently rebuilt families; P12 and FIRST-0 replay omissions subtract used terms |
| 3. Left side | `U^{12}H^3 B3` | flint expansion equals the emitted target polynomial |
| 3. Beta degree | exact degree one | cleared `h_F` all degree 0; cleared `h_beta` all degree 0 after `/beta`; `BPoly` has no cutoff |
| 3. Divisions | `F` and `beta` | `h_F` table = V85 cleared `h` (2,797 terms, 50,346 dens `1`); `h_beta` 3,330 terms, 59,940 dens `1` |
| 3. Common denominator | `U H` | `C U-3 U^3`; `gcd(F,U H)=1`; no `F` or `beta` in any scanned denominator |
| 3. Hidden inversion / truncation | `BPoly.inverse`, Dual rebound | nonconstant beta inverse is fail-closed; `qd.Dual=BPoly` rebinds the live compiler class |
| 4. DVR consequence | `D(U H B3)` | unit left side vs `F h_F+beta h_beta` in the maximal ideal; scope is this q2 slice only |
| 5. V1 / V2 | no-verdict custody | V1 harness `rc=1`; V2 redundant replay quarantined; V3 archive is the freeze |
| 6. Firewall | all-q / TD6 / JC2 | RESULT and preregistration keep the charged firewall |

---

## 1. Custody

Recomputed SHA-256 of the five required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `cases/td6_c1_c2_c3_total_f_q2_raw_p12_source_v86tfq2_aws_20260826/RESULT.md` | `22fb1c6c437e26f212a38857157050f68e773dcee8482e3d384da47fffc09c02` | producer result |
| `.../EVIDENCE.sha256` | `492117581f014bdc60bc13262a4d6ae89c478646c9f4a79b1db29206e1bcf94e` | evidence manifest |
| `.../FREEZE.sha256` | `82083dd26b44766779beb2fec64e34f0842769a8f81fe73aee1f105cb8510c79` | freeze |
| `.../SOURCE.sha256` | `d86ec28236b9b97746150d04b3a0891ec05f5bc6eed02e78fc02b0f864d221f6` | AWS source manifest |
| `xmodel/td6-v85-total-source-dag-q-globalization-design-20260826.md` | `245d1f00ab283e71b8db200e4cf51dce13c9703b91715a67295449de32352501` | design/acceleration note only |

`SOURCE.sha256` rows consumed from the case root:

| Path | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `a08b2b3dad3008571473f63fbc3e1f52f646efaa8bb851c5335e9b45a1285adb` |
| `replay_v86tfq2_total_f_q2.py` | `5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c` |
| `run_v86tfq2_total_f_q2.sh` | `080df745476a062894e5199df4d83507cbae4943405ab5a15f5ce20dca16486d` |
| `DEPLOYMENT_ERRATUM.md` | `f61b36922e764ad62bbaacf81b84f52d8fb752920864e41ff16c2f272a069967` |
| `V85_TOTAL_F_SOURCE_INVENTORY.tsv` | `9a612bb64ee974a506a1f3b7fcb471fb8924220ca6d24320af0fc9b8a7de6b7a` |

`SOURCE.sha256` rows consumed from `source.tar.gz` (`a7e3681d…`):

| Path | SHA-256 |
|---|---|
| `source/replay_v85tf1_total_f.py` | `ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e` |
| `source/F_RAW_P12_CLEARED_SOURCE_CERTIFICATE.tsv` | `8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482` |
| `source/payload/jc2/cases/td6_c1_c2_c3_all_q_vector_ad_repaired_20260825/replay_shard.py` | `a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e` |

Nested pins reached from that shard, independently rehashed:

| Pin | SHA-256 |
|---|---|
| V32 q2 dual client | `dcc7003def824c0d2a88998cbf22a66f022a32714f05754c505e8d825bd91742` |
| trivariate adapter | `1fb512643f31b4eda6c0e96ca1adbfe3e79599986c7c095b825605a4145fdaea` |
| two-center `replay.py` | `56df638aaa3ae02cf437a32258a920a8a66afb2781c089e30b1774a5b38e65db` |
| QDUAL `jet_orbit_adjoint` | `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198` |
| q2 base `boundary_q2_deformation` | `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357` |

Case-root copies of the five overlapping source files are byte-identical to the tarball. Box03 and r6d are distinct hosts (`ip-172-30-0-249` / `ip-172-30-0-45`), distinct tags, V3 archive `a7e3681d…` on both, `rc=0`, zero swap. Mathematical stdout SHA-256 `48799b2b…` and the four output files are byte-identical across hosts. That equality is custody, not the identity.

V1 archive `4ab84624…` failed at transport insertion order (`rc=1`, ~13s). V2 archive `9f742734…` is the quarantined redundant replay. Neither hash is the freeze. Dual-host PASS banners do not enter the algebra below.

---

## 2. Charge 1 — rebuilt raw source, both beta paths, `B=q2`

The live FIRST compiler is the hash-pinned `qd.first_band_polynomials` in `td6_jet_orbit_adjoint_20260824/replay.py`. It reads `Q_PRIME`, not `B`, and forms `f1*q'-15 g1`. The live P12 compiler is `qd.compile_current`, which temporarily installs that same `Q_PRIME` on the q2 base. V86 rebinds `qd.Dual` to `BPoly` before either call, so `Dual(…)` inside those functions is `BPoly` at runtime.

Transport is the frozen V85 rectangles `(15,60,3,{15:1})` and `(25,100,5,{1:1,25:1})`. The homogeneous matrix does not contain `q2`. Beta enters the affine RHS only at the original source key `('g','X',0,2)` by

```text
value = BPoly(source_vector(key)) + [beta * 1  if key=('g','X',0,2)].
```

That is the same unit as the reviewed q2 dual client's `ONE_VECTOR`. Pivot inversion uses `lead.inverse()` of the beta-independent trivariate lead, then multiplies a `BPoly`. `BPoly.inverse` refuses any nonconstant beta polynomial.

The receiver is configured as

```text
B      = beta
Q_PRIME = {0: 1, 24: 25}  and, unless omitted,  {1: 2*beta}.
```

This is `q'=1+2 beta t+25 t^{24}` together with the licensed `B=q2` assignment. After `Q_PRIME` is replaced, `B` is the historically inert load slot: it is consumed only by the initial `Q_PRIME` construction that V86 overwrites. The two live paths are therefore the transport RHS and `Q_PRIME[1]`. Setting `B=beta` is the licensed q2 configuration, not a third independent derivative.

Path-omission controls rebuild FIRST twice: once with transport beta stripped from the bands and `Q_PRIME[1]` retained, once with bands intact and `Q_PRIME[1]` dropped. Each is compared by polynomial equality to the theorem FIRST family. If either path were dead, one comparison would be an equality and the assert would fail. That is a genuine two-path negative control, not a self-hash.

Emitted `TOTAL_F_Q2_SOURCE_INVENTORY.tsv` (SHA-256 `450c478c…` on both hosts) has 39 rows: P12 key `('X0_RAW',12)` and FIRST keys `('X-2',0)` through `('X-2',37)`. All 39 full digests differ from their beta-zero digests, so beta is live in genuine P12 and in every packed FIRST map. The beta-zero P12 digest is

```text
8d5c3550fbad393c1e13061d9934ed79e29261db378f1d344c4ea5e587e704da
```

which is the frozen V85 generic 2,893-term P12. The 132 transport-free labels on those V85 generic sources are `0..131`; because V86's beta-zero sources are digest-identical, they carry the same labels. Extra monomials supported only in positive beta cannot drop a label, and the client fail-closes if the total label set grows.

Transport rank 3470/3602 with 132 free variables and two chart events is the frozen V85/V82 transport, not a new elimination.

---

## 3. Charge 2 — V85 / V82QST3 specialization and omission controls

Frozen V85 inventory SHA-256 `9a612bb6…` is byte-identical to V85 Box02 output. For every one of the 39 rows, V86 `beta_zero_sha256` equals V85 `generic_sha256` and the keys agree. That is exact specialization at `beta=0`, not a banner.

V85 `special_sha256` for P12 is `da0d595e…`, which is the V82QST3 specialized genuine-P12 digest. The multiplier table consumed by V86 is the frozen V82QST3 certificate `8e892ffa…`: 1,490 nonheader rows, one P12 monomial plus 1,489 FIRST monomials on the 28 active indices `0..27`. All 26,820 scalar coordinates of that table have polynomial denominator `1`; none contain `F` or `beta`. V86 embeds those multipliers as beta-degree-zero `BPoly` values and, after substituting `C=(V^2-U^3)/U` on the beta-zero sources, replays

```text
a_P P12|_{F=beta=0} + sum a_i FIRST_i|_{F=beta=0}
  = V^4 U^9 (V^2-4U^3)^3.
```

The reporter line `F_beta_zero_raw_source_matches_V82QST3=true` is printed after the V85 generic-inventory match and before that replay. It is a banner-order defect. The replay itself is the gate, and the special P12 digest plus the frozen certificate are the specialization evidence.

P12 and FIRST-0 replay omissions subtract the corresponding used term from the total combination and require the identity to fail. FIRST index 0 is one of the 28 active V82QST3 rows, so the FIRST omission is not an empty-term check. P12 has a nonzero frozen multiplier. Neither control hashes an object against itself.

---

## 4. Charge 3 — the identity, degrees, divisions, denominators

Let `A` be the frozen V85 coefficient ring localized at `U H B3`, and write `s=U^{12} H^3 B3`. Independently in `Q[C,V,U]`, flint expands

```text
s = 4 C^5 U^{14} - 4 C^4 V^2 U^{13} - 12 C^4 U^{16} + C^3 V^4 U^{12}
    + 16 C^3 V^2 U^{15} - 88 C^3 U^{18} - 9 C^2 V^4 U^{14}
    + 72 C^2 V^2 U^{17} + 360 C^2 U^{20} + 27 C V^4 U^{16}
    - 432 C V^2 U^{19} - 108 C U^{22} - 27 V^4 U^{18}
    + 540 V^2 U^{21} - 540 U^{24},
```

which is exactly the emitted `target=` line. The polynomial identities

```text
U H = F + (V^2-4 U^3),
U^2 B3 ≡ U^2 V^4  (mod F)
```

hold, so on `D(U)` one has `s|_{F=0}=V^4 U^9 (V^2-4 U^3)^3`. Spot checks at `(C,V,U)=(0,1,1)`, `(3,2,1)`, `(4,4,2)`, `(-6,3,3)` agree. Further,

```text
gcd(F, U H) = gcd(F, B3) = gcd(F, H) = gcd(U, F) = 1.
```

Localizing at `U H B3` therefore cannot invert `F`.

V86's beta-zero sources are the V85 generic sources (Charge 2). The frozen multipliers are beta-independent. The V85 identity therefore supplies

```text
s = a_P P12(0) + sum a_i FIRST_i(0) + F h_F^{V85}.
```

`BPoly` is sparse `E3[beta]` with no degree cutoff; multiplication is the Cauchy product; inversion of a nonconstant beta polynomial raises `attempted_beta_polynomial_inverse`. Receiver operations on the live `qd` object are addition and multiplication of `BPoly` values. Hence every total source lies in `A[beta]`, and the divided-difference identity

```text
s = a_P P12(beta) + sum a_i FIRST_i(beta) + F h_F^{V85} + beta h_beta
```

holds in `A[beta]` with

```text
h_beta = - sum a (f(beta)-f(0))/beta.
```

This is the exact identity charged, not an AWS equality flag.

Independent table confirmation of the two quotients:

- Cleared `h_F` has 2,797 terms, all `beta_degree=0`. After dropping that extra column, the `(monomial, coefficient)` pairs are equal to the frozen V85 cleared-`h` table (2,797 terms). All 50,346 scalar coordinates have polynomial denominator `1`. That 50,346 is the V85 `F`-division coordinate count. Localized `h_F` digest claimed `d42fd419…`; V85 quotient digest `7434b0a7…` is the beta-zero object the client checks before clearing.
- Cleared `h_beta` has 3,330 terms, all `beta_degree=0`. All 59,940 scalar coordinates have polynomial denominator `1`. If the residual had `beta^2` or higher, `divide_by_beta` would have emitted positive `beta_degree` rows. It did not. Residual beta degree is therefore exactly one, and `h_beta` is beta-independent.

No scanned coefficient string in either cleared table or in the V82QST3 multiplier table contains a polynomial denominator involving `F`, `beta`, or an unregistered factor. Integer contents such as `/4552200` are coefficients in `Q`, not inversions in `Q[C,V,U]`. Common denominator of the family is `C U-3 U^3=U H`; the allowed `B3` factor is not needed for clearing. Multiplying once by `U H` produces the emitted polynomial tables.

The 38 FIRST maps and genuine P12 are not re-emitted as polynomials, only as digests. Expanding `a_P P12(beta)+…` on this host is therefore unnecessary once the V85 identity and polynomiality in `beta` are in hand. That is the design note's telescoping argument, applied to the one-variable q2 fixture, not an all-q theorem.

---

## 5. Charge 4 — DVR consequence and scope

On `D(U H B3)`, `s` is a unit. The identity writes `s` as a combination of the raw P12/FIRST rows plus `F h_F+beta h_beta`, with `h_F` and `h_beta` regular on that open (denominator `U H`). If a DVR arc in this retained family kills every raw row and puts both `F` and `beta` in the maximal ideal, the right side has positive valuation and the left side does not.

This contradiction uses both `F` and `beta`. If `v(beta)=0`, the term `beta h_beta` need not lie in the maximal ideal, so beta-unit fibres are not excluded. If `v(F)=0`, positive-`F` is not excluded. Other `q_e`, dead stretch, correction, F1-orbit/pole, centering, and boundary moduli are not variables of this ring. The identity totalizes only the literal pair `(F,q2=beta)` on one normalized source slice with the 132 section coordinates retained as free parameters.

RESULT's producer-tier slogan `positive_F_and_beta_arcs_on_this_slice_excluded` matches that DVR statement. The charged design note describes a compressed all-q successor and explicitly claims no all-q theorem; V86 is the q2 acceptance fixture of that design, not the successor.

---

## 6. Charge 5 — V1 / V2 / dual-host custody

V1 is a harness failure: unsorted transport-pivot insertion under an ascending policy, identical on both hosts, `rc=1`, before FIRST or P12. It has no denominator, beta-family, or source verdict. V2 is a deliberately redundant, latency-heavy replay of a non-authoritative archive. The freeze pins V3 archive `a7e3681d…` and V3 client `5b160a2b…`. Dual-host byte identity of stdout and of the four mathematical files confirms that V3 executed the same client twice; it does not substitute for the identities in §§3–4.

---

## 7. Failed attacks

- **Wrong-manifest V1 assignment.** Freeze hash `82083dd2…` is `FREEZE.sha256`, not `SOURCE.sha256`. This V2 pairing is the correct one; every freeze row rehashes.
- **Square-zero truncation.** `BPoly` keeps Cauchy products. Residual `h_beta` would show leftover beta degree if `beta^2` survived. The table is purely degree 0.
- **Hidden `F` inversion.** `gcd(F,U H)=1` in `Q[C,V,U]`; every scanned cleared and multiplier denominator is `1`; `BPoly` never inverts `F`.
- **Hidden `beta` inversion.** `BPoly.inverse` fail-closes on any positive beta degree; the AWS client completed, so that branch was not taken.
- **Inert `B` as a missing live path.** After `Q_PRIME` replacement, `B` is the licensed q2 slot, not a third derivative. The two live paths are independently omit-controlled on FIRST.
- **Self-referential omissions.** Path omissions rebuild FIRST from altered compiler state. Row omissions subtract used multiplier terms.
- **Staged CURRENT / PREVIOUS / POLE.** The P12 object is `compile_current(...)[12]` with family `X0_RAW`, the same genuine pre-PREV P12 as V85/V82QST3. No staged CURRENT table is consumed.
- **V85 identity failure inherited silently.** Beta-zero sources are digest-identical to V85 generic sources; cleared `h_F` is coefficientwise the V85 `h`; the `F=0` specialization of `s` is the V82QST3 clearer. The V85 identity is the same computational object, not an unexamined banner.
- **All-q, other moduli, unit-beta, whole TD6.** None of these are licensed by the identity or by the RESULT firewall.

---

## 8. Defects that do not break the charged claims

1. `F_beta_zero_raw_source_matches_V82QST3=true` is printed before the special-fibre replay. Repair is to move the banner under the `special_identity=={(): SPECIAL_CLEARER}` assert. The replay and the frozen special P12 digest remain the evidence.
2. The charged design note's all-q gate 5 lists a separate `B`-path omission. V86 is the q2 fixture of that note, not the all-q certificate; it retain-assigns `B=beta` and omit-controls the two live paths. No V86 claim requires a third omission.
3. Total P12/FIRST polynomials are not emitted, only digests and the two quotient tables. That is an evidence-packaging choice. It does not weaken the divided-difference identity once V85 specialization is hash-locked.

None of these is a bad coefficient, a bad denominator, a source omission, or a scope overclaim.

---

## 9. Firewall

This review confirms a literal total-`(F,q2)` raw P12/FIRST identity on one normalized source slice. It does not totalize the other q jets, dead stretch, correction, orbit/pole, centering, deck/torsion, or boundary moduli; cover unit-beta fibres; supply a full total-Rees chart; or prove a whole fixed A3, TD6, SP-2, or JC2 statement. The charged design note remains a design/acceleration note: no all-q theorem is claimed or confirmed here.

CONFIRMED
