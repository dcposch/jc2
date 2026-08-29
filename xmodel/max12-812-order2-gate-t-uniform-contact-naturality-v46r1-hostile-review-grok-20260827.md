# Hostile review: V46R1 additive coordinate-typed shifted-root repair

| Field | Value |
|---|---|
| Charged target | additive V46R1 repair of the mixed shifted-root coordinate witness |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile desk review. Different model family from the R1 producer |
| Method | SHA-256 of the six charged artifacts and of every R1-pinned V46 base file before any producer `PASS` line was read as evidence; independent `Fraction` rederivation of both typed root maps, all six leading 2×2 Jacobians, Hensel through depth 10 on three `rho` sequences, triangular inverses, and raw/D1 commutation in both jet-map directions; independent polar arithmetic at `(7,8,7;T=26)`; live `F_1000003` replay of all seven rows at that contact in both map directions; in-process replay of the R1 verifier with no `--output`. Producer `PASS-UNIFORM-CONTACT-NATURALITY-V46R1-ROOT-REPAIR`, schema status tokens, and the V46 Grok review’s `CONFIRMED`/`GAP` labels were not used as evidence |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` (charged files are untracked relative to that commit; custody is the assignment SHA-256) |
| Date | 2026-08-27 |

Independently recomputed SHA-256 of the six charged files match the review assignment. Every R1 `base` pin rehashes. The R1 verifier was replayed in this session **without** writing into `run_v0_v4_r1/`; its `checks` object is byte-identical to the frozen `result.json` (only `elapsed_seconds` is a wall-clock field and was not used). No file other than this review was written. No frozen producer artifact, canonical ledger, AWS job, heavy CAS, web sweep, or `jc2-lean` tree was entered or modified.

This review does **not** promote the eleven-family union, does **not** promote `(a,d,r)=(8,3,8)`, and does **not** conclude Gate T, order two, maximum twelve, JC2, or a counterexample.

---

## Verdicts

| Item | Verdict |
|---|---|
| Custody / supersession boundary | **CONFIRMED** |
| Raw-total shifted map | **CONFIRMED** |
| Mapped-D1 shifted map | **CONFIRMED** |
| Hensel / triangular inversion / commutation | **CONFIRMED** |
| Mutations / computed Jacobians | **CONFIRMED** |
| `a=7` load-tie coverage | **CONFIRMED** |
| Scope / infrastructure | **CONFIRMED** |

**Smallest counterexample:** none. **Smallest repair:** none.

**Exact V46+R1 interface scope: eligible for narrow infrastructure promotion.** V46 remains the source-naturality freeze. R1 is the unique typed shifted-root interface on `D(rho)`. Serial `ACT-TOT-G22/G24+` exporters stay off the mathematical critical path. Per-endpoint manifests, chamber-compiler semantic checks, generated per-contact alias maps, reviewed D1 endpoints, and the confirmed-but-unpromoted `(8,3,8)` family remain separate obligations.

---

## 0. Custody of the six charged artifacts

Recomputed SHA-256, all matching the assignment:

```text
0f6bec4983bc8d682b64db5ac23f2d1bb64b8613e2812e95f2cab2b041494b44
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46r1_20260827/SCHEMA_R1.json
7c571dcd5c545bba64569fe38f826b3b33cac455540f22cecd1c35b37bc88c85
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46r1_20260827/verify_uniform_naturality_r1.py
60729c65debd9499aa69a7db2d67c38628ca1b078e0e84a05de34c690b54f3f4
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46r1_20260827/RESULT.md
fd50f3d70b0ebdbecf1307891a9b017f264dc22e5e1fc4bc2a8839b5fdbbfe6a
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46r1_20260827/run_v0_v4_r1/result.json
830dbd173b4302c63c53e6d27b49adde856677fc467e8d5e79c34cfc41abf1c7
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46r1_20260827/FREEZE.sha256
13450b727aad5a27f40ba22333b91b03765009a41de8aa36c330a5cd02347e71
  xmodel/max12-812-order2-gate-t-uniform-contact-naturality-v46-hostile-review-grok-20260827.md
```

`FREEZE.sha256` contains exactly the four R1 files (schema, verifier, `RESULT.md`, `result.json`) and matches each recomputed digest. `RESULT.md` lists the first three of those four and does not hash itself or the freeze; that is the correct freeze split.

R1 `base` pins, all matching:

```text
796eb0847e7b0bb7972c2fd7b3db10bd2dcfd2fd85c5bbaa47e3a239f8b02673  V46 SCHEMA.json
8e49fc87ebeffb74e4c33f79ae248846c7de3ce4f4fb2ad07ac85751d8841ec7  V46 verify_uniform_naturality.py
25a5fb3e0a8dff1a0d841823dfe44265775e793431445878ab49193c846d67ce  V46 run_v0_v4/result.json
b39f66e2cb7cac16dd1c940814b44e8aff3cd7c7df1ad9347beb5f558187ae22  V46 FREEZE.sha256
13450b727aad5a27f40ba22333b91b03765009a41de8aa36c330a5cd02347e71  V46 Grok review
```

The V46 review is a charged comparator for the additive boundary, not authority for any R1 verdict.

---

## 1. Custody / supersession — CONFIRMED

### 1.1 Additive boundary

`SCHEMA_R1.json` declares a different `schema_id` (`…-V46R1`) and a `repair_scope` that supersedes only

- V46 `SCHEMA.json` `shifted_root` block,
- V46 result `shifted_root.diagonal_determinants` display,
- V46 verifier `check_shifted_root` mixed-coordinate witness,

and preserves the seven source primitives, the coefficient-ring jet-reindexing theorem, 569-tail custody, load/target schedules, polar tables, and endpoint lifecycle.

That split is implemented, not merely declared.

- V46 `SCHEMA.json` is byte-identical to its freeze pin. Its mixed `shifted_root.C_jet` still reads `(CcD1_n +/- sum lambda_i CzD1_(n-i))/2` with D1 names and a leftover total `/2`. R1 does **not** edit that file. A linker that still reads V46 `shifted_root` would get the mixed formula; the supersession document is `SCHEMA_R1.json`. That is the correct additive pattern: frozen producer files stay frozen.
- The R1 verifier imports the hashed V46 module, calls `v0_pins`, `v1_naturality`, `v3_support`, and `v4_provenance`, and never calls `check_shifted_root` (the name does not occur in the R1 source). The mixed witness is omitted, not re-executed as a PASS.
- R1 does not contain `normative_primitives`, load delays, target grades, polar inventory, or endpoint records. Those remain V46’s.
- Live R1 replay rehashes the five V46 base pins, re-executes V0/V1/V3/V4, and returns the same 11 families, 10 promoted plus one `confirmed_but_unpromoted`, 24 endpoint-artifact hashes, and current G20 maxima `(p,A,C,R,k10,k6,k2)=(3,3,3,1,2,0,0)`.

### 1.2 Tails, scales, types

Independent of the R1 report constant `tail_weight_rows_checked: 569`:

| Check | Independent result |
|---|---|
| tails byte | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |
| tails canonical | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` |
| row census | `[36, 54, 58, 81, 89, 120, 131]`, sum **569** |
| monomials | length 10, load part at most one factor of exponent one, weighted degree `12+ell` under `[8,7,6,5,4,3,2,2,6,10]` |
| denominators | powers of two, `{2^2,…,2^20,2^23}`, max `8388608` |
| target scales | `mu2/mu4/mu6/J = 1,1,1,1/4` |

`1000003` is prime and `2^{-1}≡500002`, so every tail denominator is legal in `F_1000003`. Coordinate types in R1 are exactly `raw_total_shifted_jets` and `mapped_D1_relative_jets`, with `raw_to_D1` the relative-jet restriction of V46 `jet_reindexing_map`.

**Weak pin, not a gap.** `v0_r1_pins` checks the raw C formula, the raw R formula, and both determinant triples against hardcoded strings, but does not pin the raw A formula string or the declared variable/orientation order. Those strings are present and correct in the schema; the coded maps implement them. No counterexample.

**Custody/supersession: CONFIRMED.**

---

## 2. Raw-total shifted map — CONFIRMED

Declared variable order `(z_coefficient, constant_coefficient)`, orientation order `(minus, plus)`. Relative jets at grade `n`:

```text
A^{+/-}_n = ac_{a+n} +/- sum_{i=0}^{n} lambda_i az_{a+n-i}
C^{+/-}_n = (ec_{c+n} +/- sum_{i=0}^{n} lambda_i ez_{c+n-i}) / 2
R^{+/-}_n = rs_{r+n}/4 +/- sum_{i=0}^{n} lambda_i cs_{r+n-i}
```

The `/2` on C divides the whole parenthesis. The `/4` on R divides only `rs`. Those are different placements; they are the forced cancellations against `/2` in `N1,N0` and `/4` in `Rtot`.

Leading 2×2 Jacobians, rows minus-then-plus, columns z-then-constant, independently differentiated and evaluated by `ad-bc` at generic `lambda_0` including `3`, `-3`, `5`, `-7/3`:

```text
J_A = [[-lambda_0, 1], [ lambda_0, 1]],          det = -2 lambda_0
J_C = [[-lambda_0/2, 1/2], [ lambda_0/2, 1/2]],  det = -lambda_0/2
J_R = [[-lambda_0, 1/4], [ lambda_0, 1/4]],      det = -lambda_0/2
```

Swapping orientation or swapping `(z, constant)` flips the sign to `+lambda_0/2` or `+2 lambda_0`. The declared order is the one the verifier matrices use. Frozen `result.json` reports, for `lambda_0 = +/- 3`, the numeric triples `(-6, -3/2, -3/2)` and `(6, 3/2, 3/2)`, which are exactly those determinants.

The coded raw loop is

```text
A: ac +/- conv(lambda, az)
C: ec/2 +/- conv(lambda, ez)/2
R: rs/4 +/- conv(lambda, cs)
```

which is the declared map, not a third convention.

**Raw map: CONFIRMED.**

---

## 3. Mapped-D1 shifted map — CONFIRMED

After the relative jet map

```text
az_{a+n} -> AzD1_n,     ac_{a+n} -> AcD1_n,
ez_{c+n} -> 2 CzD1_n,   ec_{c+n} -> 2 CcD1_n,
cs_{r+n} -> BzD1_n,     rs_{r+n} -> 4 BcD1_n,
```

substitution into the raw maps is an identity of formal series, at every depth, not only through depth 3:

```text
A_raw = ac +/- lambda * az           = AcD1 +/- lambda * AzD1
C_raw = (ec +/- lambda * ez)/2       = CcD1 +/- lambda * CzD1
R_raw = rs/4 +/- lambda * cs         = BcD1 +/- lambda * BzD1
```

The leftover total `/2` on C and `/4` on R are consumed by the factors `2` and `4`. The D1-named maps are therefore unscaled and of identical bilinear shape. Each leading Jacobian is the A-matrix `[[-lambda_0, 1], [lambda_0, 1]]` with determinant `-2 lambda_0`.

The R1 schema writes exactly those three D1 formulas and the triple `[-2*lambda_0, -2*lambda_0, -2*lambda_0]`. The verifier’s D1 loop is `d1_c +/- conv(lambda, d1_z)` for `(Az,Ac)`, `(Cz,Cc)`, and `(Bz,Bc)`. Frozen numeric triple at `lambda_0 = +/- 3` is `(-6,-6,-6)` and `(6,6,6)`.

**Mapped-D1 map: CONFIRMED.**

---

## 4. Hensel / inversion / commutation — CONFIRMED

### 4.1 Hensel on `D(rho)`

On `Z[1/2]`, `P = -2 rho^2 + 2 sum_{n>=1} ell_n sigma^n` and `lambda^2 = -P/2`. Leading term `lambda_0 = epsilon rho`, `epsilon in {+1,-1}`. Grade `n>=1`:

```text
2 lambda_0 lambda_n = -ell_n - sum_{1 <= i < n} lambda_i lambda_{n-i}.
```

Every step divides by `2 lambda_0`, so the branch is unique if and only if `rho ≠ 0` (and `2` is already inverted in the coefficient ring). Localization is exactly `D(rho)`. Source naturality never performs this division.

Re-executed through depth 10 on both decks for three non-special sequences (`rho=3` with the producer `ell`, `rho=5` with a different `ell`, `rho=2/3` with quadratic `ell`): `lambda^2 + P/2 = 0` coefficientwise, and `lambda^{(-)} = -lambda^{(+)}` termwise (deck exchange `rho |-> -rho`).

### 4.2 Commutation through depth 3, both jet-map directions

A throwaway engine, not the producer file, evaluated both maps through relative depth 3 on both decks, on the producer jets and on an independent rational jet.

- D1 jets pushed to raw by `(ez,ec,rs) = (2 Cz, 2 Cc, 4 Bc)`: raw outputs equal D1 outputs at every grade (48 equalities: 2 decks × 3 labels × 2 orientations × 4 grades).
- Raw jets pulled to D1 by `Cz = ez/2`, `Cc = ec/2`, `Bc = rs/4`: the same identity.

Leftover `/2` on mapped-D1 C, or leftover `/4` on mapped-D1 R, breaks commutation already at grade 0 whenever the leading C or R value is nonzero, and breaks it as a Jacobian identity on all of `D(rho)` (§5).

### 4.3 Triangular inverses, both decks

Raw:

```text
ac = (A- + A+)/2,     lambda * az = (A+ - A-)/2,
ec = C- + C+,         lambda * ez = C+ - C-,
rs = 2(R- + R+),      lambda * cs = (R+ - R-)/2,
```

then `az, ez, cs` by the unique triangular deconvolution that divides only by `lambda_0`. D1, all three labels:

```text
constant = (X- + X+)/2,     lambda * z = (X+ - X-)/2,
```

same deconvolution. Independently recovered through depth 3 on both decks, producer jets and generic jets: 96 equalities (2 decks × (6 raw + 6 D1) × 4 grades). No division by `rho` occurs except through `lambda_0`.

**Hensel / inversion / commutation: CONFIRMED.**

---

## 5. Mutations / computed Jacobians — CONFIRMED

### 5.1 The verifier computes determinants of 2×2 matrices

V46 pasted the strings `["-2*lambda0", "-lambda0/2", "-lambda0/2"]` and never formed a Jacobian. R1 does not contain those pasted strings. It builds

```text
raw A:  [[-lam0, 1],    [lam0, 1]]
raw C:  [[-lam0/2, 1/2],[lam0/2, 1/2]]
raw R:  [[-lam0, 1/4],  [lam0, 1/4]]
D1:     [[-lam0, 1],    [lam0, 1]]   (three times)
```

and computes `ad-bc`. Those entries are the partial derivatives of the coded leading maps in the declared order. Finite differences of the coded maps at `lambda_0=3` recover the same six matrices and the same three+three determinants. Frozen `computed_determinants` match.

The D1 triple is the common unscaled 2×2 repeated because the three D1 formulas have identical bilinear shape. That is a computation of the unique D1 Jacobian, not a paste of determinant strings. Commutation plus the leftover-factor mutations would still catch a desync if the coded D1 C or R acquired a leftover scale.

### 5.2 Three factor-conflation mutations fire at the leading block

Required mutations:

1. mapped-D1 C written `(CcD1 +/- lambda CzD1)/2`,
2. mapped-D1 R written `(BcD1 +/- lambda BzD1)/4`,
3. paste of the raw-total determinant triple into the mapped-D1 map.

On `D(rho)`, as Jacobian identities, all three **must** fire at the leading 2×2:

```text
wrong J_C det = -lambda_0/2  ≠  -2 lambda_0
wrong J_R det = -lambda_0/8  ≠  -2 lambda_0
raw (C,R) dets (-lambda_0/2, -lambda_0/2) ≠ D1 (-2 lambda_0, -2 lambda_0)
```

Equality would force `lambda_0=0`, which is excluded. Independently checked at `lambda_0 in {3,-3,5,-7/3}`.

The verifier’s value-level leftover checks (`correct/2` and `correct/4` at `n=0`, both orientations, both decks) plus the pasted-triple check (`raw_dets[1:] == d1_dets[1:]`) fire 12 times: 2 decks × (2 orientations × 2 leftover values + 2 leftover determinant slots). That count is a reporting of leading-block failures, not a third coordinate convention.

**Method note, not a gap.** Leftover-factor *values* are inert on the hypersurface `C^{+/-}_0=0` or `R^{+/-}_0=0`. A minus-orientation example: `Cc_0 = lambda_0 Cz_0` makes `C^-_0 = 0 = (C^-_0)/2`. The Jacobian identity still fires. The verifier uses a non-vanishing jet (`Cz_0=2`, `Cc_0=5`, `Bz_0=7`, `Bc_0=11`, `lambda_0=±3`). Mutation (3) is already Jacobian-level and universal.

**Mutations / Jacobians: CONFIRMED.**

---

## 6. `a=7` load-tie coverage — CONFIRMED

V46’s D1 family `D1_A6_A7` has domain `a=6..7`, `c=a+1`, closed `r>=a`, but its stored representative is only `(6,7,6;T=24)`. R1 adds the actual `a=7` wall `(a,c,r;T)=(7,8,7;26)` over `F_1000003`. `T=12+2a` matches the D1 schedule (`a=2,6,8,9` give `16,24,28,30`).

### 6.1 Polar table, first principles

Ten first grades at `(7,8,7)`:

```text
AC=25, C2=26, RA2=33, A3=36,
k10R3=31, k10RC=26, k10R2A=34, k10A2=28,
k6C=25, k2R=29
```

Arrivals at or before `T=26`: `AC=25`, `C2=26`, `k10RC=26`, `k6C=25`. Family maximum `max(T-w(M))` with leading-only `0`, family active at depth zero iff some licensed polar containing it arrives:

```text
p=1, A=1, C=1, R=0, k10=0, k6=1, k2=0
active:   p, A, C, R, k10, k6
inactive: k2
```

`R=0` and `k10=0` are **active** (`k10RC` hits grade 26). `k2=0` is **inactive** (`k2R=29>26`). That is the required distinction.

`k6` is the load-tie. On D1 contacts `c=a+1`, `T=12+2a`, one has `T - w(k6C) = a-6`. At V46’s ordinary `a=6` representative, `k6C` arrives at `T` so `k6=0` active (leading only). At `a=7`, `k6C` arrives at `25=T-1` so `k6=1`: first D1 wall with an interior `k6` jet. Frozen `derive_support` on the hashed V46 inventory returns the same table.

### 6.2 Seven rows, both map directions

`7(T+1)=189` coefficients. Producer direction (D1 jets random, total filled by the jet map) at `(7,8,7;26)` over `F_1000003`: zero mismatches, seven primitives equal. Opposite direction (total jets random, lower ideal imposed, D1 recovered by `AzD1_n=az_{a+n}`, `CzD1_n=ez_{c+n}/2`, `BcD1_n=rs_{r+n}/4`): seven `F_i` series equal coefficientwise and all 189 row coefficients equal. The ordinary `a=6` representative still equals.

Live R1 V1: 11 base representatives, 2247 base coefficients, plus this cell, total 12 and 2436, matching frozen `result.json`.

**`a=7` coverage: CONFIRMED.**

---

## 7. Scope / infrastructure — CONFIRMED

The V46 mixed `C_jet` plus pasted determinant triple was the obstruction to generating linker duty 4 from a unique formula. R1 removes that obstruction: each coordinate system has one map, the two maps commute with the jet map, and both invert on `D(rho)`. The repaired root block is therefore eligible as the unique common linker input for shifted-root instantiation.

It is unique *per coordinate type*. A linker must read `SCHEMA_R1.json` for roots and must not instantiate V46 `SCHEMA.json` `shifted_root`. That is the supersession boundary, not a remaining uniqueness gap.

No source-naturality defect was found. Serial `ACT-TOT-G22/G24+` exporters are **not** reintroduced. `[sigma^g] Phi_j^{total}` remains a defined polynomial the moment the V46 jet map exists; an exporter only writes layer-3 bytes of it.

Remaining finite obligations, none of them serial grade exporters:

1. **Per-endpoint manifests** — `(a,c,r_floor)`, exact versus closed orders, `d`, `G`, `T`, licensed primitive inventory hash, mechanically derived maxima, load/target policy, localization, theorem type.
2. **Chamber-compiler semantic checks** — V0 tokens remain selected fragments. Each chamber compiler’s coded primitives still have to be compared to the D1 shape, including every load and target that can enter by that chamber’s `T`.
3. **Generated per-contact alias maps** — V46 still generates one map at current `(2,5,3)` maxima as a mutation control. A linker must derive the renaming/scaling map from `(a,c,r)` per endpoint.
4. **Reviewed D1 endpoints** — ten promoted families and mixed theorem types/localizations remain inputs. This repair does not re-prove them.
5. **`(8,3,8)` conditional** — `D23_A8D3` stays `confirmed_but_unpromoted`, authority `null`, literal odd `SourcePhi` rows only. No eleven-family union.

**Scope: CONFIRMED.**

---

## 8. Strongest exact surviving theorem

Over `Z[1/2]`, after V46’s coefficient-ring jet reindexing (lower ideal `az_i=ac_i=0` for `i<a`, `ez_i=ec_i=0` for `i<c`, `cs_i=rs_i=0` for `i<r`, and `ez,ec,rs |-> 2 CzD1, 2 CcD1, 4 BcD1` on relative jets), the following hold on `D(rho)` and nowhere is claimed at `rho=0`.

Let `lambda^2 = -P/2` with `P = -2 rho^2 + 2 sum_{n>=1} ell_n sigma^n` and `lambda_0 = epsilon rho`. The two decks are exchanged by `rho |-> -rho`. The recurrence

```text
2 lambda_0 lambda_n = -ell_n - sum_{1<=i<n} lambda_i lambda_{n-i}
```

determines a unique formal branch on `D(rho)`.

In variable order `(z, constant)` and orientation order `(minus, plus)` there are two typed shifted-root maps, related by the jet map:

```text
raw total:
  A = ac +/- lambda * az,                 det_0 = -2 lambda_0
  C = (ec +/- lambda * ez)/2,             det_0 = -lambda_0/2
  R = rs/4 +/- lambda * cs,               det_0 = -lambda_0/2

mapped D1:
  A = AcD1 +/- lambda * AzD1,             det_0 = -2 lambda_0
  C = CcD1 +/- lambda * CzD1,             det_0 = -2 lambda_0
  R = BcD1 +/- lambda * BzD1,             det_0 = -2 lambda_0
```

The displays commute at every relative jet. Both invert triangularly by dividing only by `lambda_0`. Writing the D1 C or R map with a leftover total `/2` or `/4`, or pasting the raw determinant triple onto the D1 map, is already wrong at the leading 2×2.

Source naturality (seven primitives, free `p0`, 569 tails, load delays `4/12/20`, targets `28/32/36/38` with scales `1,1,1,1/4`) uses no root map and is unchanged. The additional D1 representative `(7,8,7;T=26)` satisfies the same source identity on all seven rows, with exact maxima `p/A/C=1`, `R=k10=0` active at depth zero, `k6=1` active, `k2=0` inactive.

Nothing here is an emptiness theorem, a global G2 statement, or a promotion of the endpoint union.

---

## 9. Eligible promotion, exporters, exclusions

**Eligible for narrow infrastructure promotion, exactly this scope:** the V46 source-naturality schema/verifier together with the R1 typed shifted-root maps — two coordinate systems, commuting displays, computed leading Jacobians, Hensel and triangular inversion on `D(rho)`, factor-conflation mutations at the leading block, and the extra `a=7` load-tie cell. Linker duty 4 can be generated from `SCHEMA_R1.json`.

**Serial actual-total G22/G24+ exporters: not reintroduced.** No source-naturality defect was found. Campaign retirement of any concrete linker still waits on the per-endpoint list in §7.

**Not promoted, and not concluded:**

- the eleven-family union as one emptiness theorem;
- `(a,d,r)=(8,3,8)` / `(8,11,8)`;
- `rho=0` ramified fibre;
- equality faces;
- positive-order leading loads;
- `k=0` / `k10`-leading coefficient zero;
- unlisted contacts;
- staged Rees charts and the terminal/Taylor receiver;
- both global `G2` obligations;
- Gate T;
- order two;
- maximum twelve;
- JC2;
- a counterexample.

---

## 10. Execution record

Desk only. Independent Python `Fraction` arithmetic for maps, Jacobians, Hensel, inverses, commutation, and polar maxima; `F_1000003` truncated-series replay of `(7,8,7;26)` in both jet-map directions; SHA-256 of every charged and base-pinned file; in-process R1 replay with no `--output`, `checks` byte-identical to frozen `result.json`. No Singular, Sage, msolve, Lean, AWS, web, or ledger edit. `jc2-lean` was not entered. The only file written is this review.

**CONFIRMED** as an additive coordinate-typed root-map repair. V46+R1 is eligible for narrow infrastructure promotion at the exact scope above. Promotion of the endpoint union and of `(8,3,8)` withheld.
