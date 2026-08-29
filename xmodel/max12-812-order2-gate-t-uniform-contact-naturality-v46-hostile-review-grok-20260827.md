# Hostile review: V46 uniform strict-unique-AC source-transport schema/verifier

| Field | Value |
|---|---|
| Charged target | frozen V46 implementation of the uniform strict-unique-AC source-transport interface |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile desk review. Different model family from the formula-theorem producer and from Fable 5 |
| Method | SHA-256 of every charged pin, every schema-pinned witness, `tails.json` (byte and canonical), and all 24 endpoint artifacts before any producer `PASS` line was read as evidence; independent `Fraction` / `F_1000003` truncated-series replay in **both** map directions; independent first-mismatch grades; independent Hensel recurrence, deck exchange, and 2×2 Jacobians; independent polar arithmetic at eleven representatives plus the receding-`AC` sentinel; byte read of the three pinned compilers. Producer `PASS-UNIFORM-CONTACT-NATURALITY-V46-V0-V4`, schema status tokens, and Fable 5 `CONFIRMED` labels were not used as evidence |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-27 |

Independently recomputed SHA-256 of the six charged files match the review assignment. Every schema-pinned external input rehashes. The producer verifier was rerun in this session **without** writing into `run_v0_v4/`; its `checks` object is byte-identical to the frozen `result.json` (only `elapsed_seconds` differs: live `2.023` vs frozen `4.795`). No file other than this review was written. No frozen producer artifact, canonical ledger, AWS job, heavy CAS, web sweep, or `jc2-lean` tree was entered or modified.

This review does **not** promote the eleven-family union, does **not** promote `(a,d,r)=(8,3,8)`, and does **not** conclude Gate T, order two, maximum twelve, JC2, or a counterexample.

---

## Verdicts

| Item | Verdict |
|---|---|
| V0 / schema custody | **CONFIRMED** |
| V1 naturality | **CONFIRMED** |
| V2 mutations / root maps | **GAP** |
| V3 support | **CONFIRMED** |
| V4 provenance / lifecycle | **CONFIRMED** |
| Infrastructure sufficiency (serial `ACT-TOT-G22/G24+` exporters) | **CONFIRMED** |

**Exact V46 schema/interface scope: eligible for promotion as the common source-naturality freeze.** The seven primitives, the coefficient-ring jet-reindexing map, free `p0`, the 569-tail custody, load delays `4/12/20`, target schedule `28/32/36/38` with scales `1,1,1,1/4`, aliases, polar inventory, and eleven lifecycle records are fit to freeze.

**The shifted-root block is not yet a unique linker input.** Schema `shifted_root.C_jet` writes D1 names with a leftover total-coordinate `/2`, and V2 pastes the total-coordinate triple of determinants rather than computing the Jacobians of the maps it actually inverts. That is an additive one-block repair, not a failure of `(1.5)`.

**Serial actual-total `G22/G24+` exporters can leave the mathematical critical path.** One coefficientwise identity, now pinned by a hostile-reviewed schema, supplies every truncation. Remaining finite obligations are per-endpoint manifests, compiler-semantic checks, generated alias maps, the reviewed D1 endpoints themselves, and the `(8,3,8)` conditional — plus the additive root-map uniqueness repair for linker duty 4.

---

## 0. Custody of the six charged artifacts

Recomputed SHA-256, all matching the assignment:

```text
796eb0847e7b0bb7972c2fd7b3db10bd2dcfd2fd85c5bbaa47e3a239f8b02673
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/SCHEMA.json
8e49fc87ebeffb74e4c33f79ae248846c7de3ce4f4fb2ad07ac85751d8841ec7
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/verify_uniform_naturality.py
25a5fb3e0a8dff1a0d841823dfe44265775e793431445878ab49193c846d67ce
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/run_v0_v4/result.json
c2efa158bbc494b0d89d556c747e229cca069133fc7b3f30e5cbba3b19e5617c
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/RESULT.md
b39f66e2cb7cac16dd1c940814b44e8aff3cd7c7df1ad9347beb5f558187ae22
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/FREEZE.sha256
a1f18d28e2f2edf556f91a77f6e80fbbe210e3cc801b0d54ec9b972dcbb906e2
  xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-review-repair-v2-sol-20260827.md
```

`FREEZE.sha256` contains exactly those four V46 files (schema, verifier, `RESULT.md`, `result.json`) and matches each recomputed digest. The repair note is additive and is not inside the freeze; that is the correct split.

The formula theorem and its Fable 5 review are schema-pinned witnesses. They were rehashed and then used only as comparators for implementation semantics, never as authority for a V46 `PASS`:

```text
1cfa10b45d83ba4ecd98861c1f82e9bd41056d1cef7eaa43ad2802aa73aada5d
  xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-sol-20260827.md
b66f8c0cf342e497e9117306de3d4aaa5d8b537c5929f99d2b32765ed855f164
  xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-hostile-review-fable5-20260827.md
```

---

## 1. V0 / schema custody — CONFIRMED

### 1.1 External pins

| Input | Role | Recomputed | Match |
|---|---|---|---|
| `tails.json` byte | 569 frozen tails | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | yes |
| `tails.json` canonical | sorted JSON | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` | yes |
| row census | `36+54+58+81+89+120+131` | `569` | yes |
| `compile_t_rs0_discovery.py` | total `source_block` | `3aa6bbbb…f45938` | yes |
| `compile_r1_d1_ac.py` | D1 `source_coefficients` | `e024a13d…c8ecb7c` | yes |
| `compile_square_load_ladder.py` | tail/load/target emitter | `77f25216…90dcdc` | yes |

All 569 monomials have length 10, load part at most one factor of exponent one, and weighted degree `12+ell` under `[8,7,6,5,4,3,2,2,6,10]`. Every tail coefficient denominator is a power of two; the set is `{2^2,…,2^20,2^23}` with maximum `2^23=8388608`. Prime `1000003` is prime and `2^{-1}≡500002`, so every denominator is legal in `F_1000003`.

### 1.2 Normative formulas, free `p0`, localization split, jet map

Schema `coefficient_base` is `Z[1/2]`. The seven primitives are written as

```text
Ctot = sigma^2 S,     Rtot = (P^2 + sigma^2 Q)/4,
N3 = sigma^3 Az,      N2 = sigma^3 Ac,
N1 = sigma^3 (P Az + Ez)/2,   N0 = sigma^3 (P Ac + Ec)/2,
F6 = 2P,  F5 = 2 Ctot,  F4 = P^2 + 2 Rtot,
F3 = 2 P Ctot + sigma^2 N3,  F2 = Ctot^2 + 2 P Rtot + sigma^2 N2,
F1 = 2 Ctot Rtot + sigma^2 N1,  F0 = Rtot^2 + sigma^2 N0,
```

with `P = p0 + 2 sum_{i>=1} ell_i sigma^i` and `p0` retained as a free jet (`jet_reindexing_map.p0 = p`, identity on every `ell_i`, all three loads, and every target). No Kummer substitution occurs in the naturality map. Localization is stated as: source naturality uses none; shifted-root maps use `D(rho)`. That split is implemented: V1 feeds a free random `P` including a free degree-zero term; only `check_shifted_root` sets `p0 = -2 rho^2`.

The jet map is the coefficient-ring reindexing required by the reviewed repair, not a bare continuity claim:

```text
az_i, ac_i -> 0 (i < a);   az_{a+n}, ac_{a+n} -> AzD1_n, AcD1_n,
ez_i, ec_i -> 0 (i < c);   ez_{c+n}, ec_{c+n} -> 2 CzD1_n, 2 CcD1_n,
cs_i, rs_i -> 0 (i < r);   cs_{r+n}, rs_{r+n} -> BzD1_n, 4 BcD1_n,
```

`proof_note` explicitly refuses “bare sigma-adic continuity”. Factors `2` on `C` and `4` on `R` are the forced cancellations against `/2` in `N1,N0` and `/4` in `Rtot`.

Load delays are `{k10: 4, k6: 12, k2: 20}`. Target schedule is `mu2@28 scale 1`, `mu4@32 scale 1`, `mu6@36 scale 1`, `J@38 scale 1/4`. Aliases include the three naming hazards (`k2c` vs `k2load`; D1 reuse of `a1,a0,c1,c0`; stage-zero vs shifted leading). Eleven `endpoint_families` records exist, with lifecycle as in §5.

### 1.3 Compiler-token tests prove exactly the fragments claimed, and no more

V0 searches nine substrings. All nine are present. Independently reading the three compilers shows what those tokens actually witness:

- Total `source_block` is literally the seven formulas after the **Kummer** substitution `p_total = -2 rho^2 + 2 sum_{i=1}^{12} sigma^i ell_i`, inside `qring` modulo `sigma^13`. The three V0 tokens are the Kummer prefix, the `Rtot` template, and the `N1` template. They do **not** prove free-`p0` naturality, and they cannot, because that compiler does not implement free `p0`. The schema role string already says “Kummer-specialized and only modulo `sigma^13`”.
- D1 `source_coefficients` is the (1.4) **shape** `kc = sigma^2 rz`, `kr = P^2/4 + sigma^2 rc`, `n1 = sigma^3 ((P az)/2 + cz)`, with the seven `F_i` written from those auxiliaries. The `r1_section` instantiates the specific contact `az = sigma a1`, `cz = sigma^3 c1`, `rz = sigma b1` (i.e. `(a,c,r)=(1,3,1)`), not a generic triple. The three V0 tokens prove shape, not generic reindexing.
- Tail emitter has `LOAD_WEIGHTS = [2,6,10]`, `Lambda^{lambda_power}`, homogeneous weight `12+ell` under `[8,7,6,5,4,3,2,2,6,10]`, and target subtraction `-Lambda^{12+ell}*(0, mu2, 0, mu4, 0, mu6, J/4)`. With `Lambda |-> sigma^2` this is delays `4/12/20` and grades `28/32/36/38` with `J` scale `1/4`. V0 checks the three load/Lambda tokens and **does not** check the target dictionary or the F-weight list. Both are present in the emitter; both are pinned in the schema object itself.

This is the correct strength: selected literal tokens as custody that the named compilers have not been swapped for unrelated files. They are not a recorded lemma that `source_block = (1.1)` in all grades, nor that every chamber compiler implements (1.4). Those remain the compiler-semantic checks listed in §6. V0 does not claim more than that, and `RESULT.md` calls them “selected literal compiler-semantics tokens”.

V0 compares target **names and grades** to a hardcoded table and does not read schema `scale`. The scales nevertheless agree across schema, verifier `row_series`, and the tail emitter (`J/4`). Not a custody failure; the scale field is still pinned by the schema hash.

**V0: CONFIRMED.**

---

## 2. V1 naturality — CONFIRMED

### 2.1 Separate formula paths

Total auxiliaries are built as

```text
S = sigma^r Bz,           Q = 4 sigma^r Bc,
Ctot = sigma^2 S,         Rtot = (P^2 + sigma^2 Q)/4,
N3 = sigma^3 (sigma^a AzD1),   N1 = sigma^3 (P · sigma^a AzD1 + 2 sigma^c CzD1)/2,
```

and likewise `N2,N0`. The D1 path never reuses those total auxiliaries. It writes

```text
Kc = sigma^{r+2} Bz,      Kr = P^2/4 + sigma^{r+2} Bc,
N3 = sigma^{a+3} AzD1,    N1 = sigma^{a+3} (P AzD1)/2 + sigma^{c+3} CzD1.
```

`P` is copied (`p_total = list(p_d1)` except under the `drop_ell1` mutation). `assemble_f` is shared, so the seven `F_i` identities given matching auxiliaries are tautological. The content of the identity is the six auxiliary series plus `P`. That is the correct reduction of (1.1) versus (1.4).

### 2.2 Independent replay, both map directions

A throwaway engine, not the producer file, rebuilt both sides at every schema representative.

- **Producer direction** (D1 jets random; total filled by the jet map). Zero mismatches.
- **Map direction of the theorem** (total jets random, lower ideal (1.2) imposed, D1 jets recovered by `AzD1_n = az_{a+n}`, `CzD1_n = ez_{c+n}/2`, `BcD1_n = rs_{r+n}/4`). Zero mismatches, and the six auxiliaries matched coefficientwise.

Contacts, fields, and compared counts:

| Family | `(a,c,r)` | `T` | Field | `7(T+1)` |
|---|---|---|---|---|
| `D1_A2_A5` | `(2,3,2)` | 16 | `Q` | 119 |
| `D1_A6_A7` | `(6,7,6)` | 24 | `F_1000003` | 175 |
| `D1_A8` | `(8,9,8)` | 28 | `F_1000003` | 203 |
| `D1_A9` | `(9,10,9)` | 30 | `F_1000003` | 217 |
| `D23_LOW_A6` | `(2,5,3)` | 20 | `Q` | 147 |
| `D23_E` | `(1,4,2)` | 18 | `Q` | 133 |
| `D23_A7` | `(7,10,7)` | 30 | `F_1000003` | 217 |
| `D23_A8D2` | `(8,10,8)` | 30 | `F_1000003` | 217 |
| `D23_A8D3` | `(8,11,8)` | 38 | `F_1000003` | 273 |
| `D23_A9` | `(9,12,9)` | 38 | `F_1000003` | 273 |
| `AGE10_CEILING` | `(10,11,10)` | 38 | `F_1000003` | 273 |

Sum `2247`. The three exact-`Q` windows are the shallow representatives; the eight deeper windows are `F_1000003`. Monomials are consumed in order `F0..F6, k10, k6, k2`. Load delays in `row_series` are `(4,12,20)`, i.e. Lambda-weights `(2,6,10)` after `Lambda = sigma^2`. Targets are **subtracted**, at grades `28,32,36,38`, with scales `1,1,1,1/4`. Signs and scales match the tail emitter.

### 2.3 Vacuous layer, not a circular identity

Once the seven `F_i` series are equal and loads/targets are the identity map, evaluating the same 569-tail polynomial on both sides is functoriality of polynomial evaluation. The `2,247` row-coefficient comparisons therefore add **no independent information** beyond the auxiliary identity, except that they parse every frozen monomial and exercise load/target machinery (and so can detect the `omit_J` mutation). The producer docstring already treats the finite expansions as mutation controls and compiler-interface defense, not as the all-grade proof. The all-grade statement is the jet map in `SCHEMA.json`. That reading is correct, and the opposite-direction auxiliary match is the actual identity check.

The identity is not circular: a wrong factor `4` or `2`, or deleting `ell_1` on one side only, breaks it (next section). `p0` is free in this check, so the identity is not secretly a Kummer identity.

**V1: CONFIRMED.** Smallest failing coefficient: none.

---

## 3. V2 mutations / root maps — GAP

### 3.1 Mutations — confirmed at the stated first grades

Independent first mismatches at `(a,c,r;T)=(2,3,2;16)` over `F_1000003`, except `omit_J` at `(8,11,8;38)`:

| Mutation | First `(row, grade)` | Primitives still equal? |
|---|---|---|
| `R` scaling `4 -> 1` | `(1, 16)` | no |
| `C` scaling `2 -> 1` | `(1, 15)` | no |
| delete moving `2 sigma ell_1` on the total side | `(2, 16)` | no |
| omit total-side `J` target | `(7, 38)` | yes (targets are not primitives) |

First **primitive** mismatches for the factor mutations, independent of tails: `R_factor_1` hits `F0,F2,F4` at grade `r+2 = 4`; `C_factor_1` hits `F0,F1` at grade `c+5 = 8`. Grade 15 is R-free in the rows at `(2,3,2)`, so the `R` mutation is invisible there and first appears at 16, matching the algebra.

Generated alias map at current maxima `(a,c,r)=(2,5,3)` with `p/A/C=3,R=1,k10=2,k6=k2=0` has 48 entries. Stage-zero names `a1,a0,c1,c0,cs,rs` all map to `0`. `k2c -> k10_2` and `k2 -> k2load` are distinct, so the syntactic collision firewall holds. (A row replay cannot catch `k2c -> k2load` through grade 16; the syntactic check is the one that is necessary, and it is present.)

Wrong universal `T = 10+2c` is rejected at `D23_A8D3` (`38 vs 32`), `D23_A9` (`38 vs 34`), and `AGE10_CEILING` (`38 vs 32`). At `E` and the `a=7,8` walls, `T` numerically equals `10+2c`; those cells are distinguished by polar content (next section), not by the `T`-number test. Analytic-only `(8,3,8)` is rejected by a null authority plus the literal-row policy string. `rho=0` is an explicit exclusion, not a relabelled general-`rho` row.

### 3.2 Hensel recurrence — confirmed

On `D(rho)`, `lambda_0 = epsilon rho` and `P = -2 rho^2 + 2 sum ell_n sigma^n` give, at grade `n >= 1`,

```text
2 lambda_0 lambda_n = -ell_n - sum_{1 <= i < n} lambda_i lambda_{n-i}.
```

Re-executed through depth 10 on both decks with `rho = 3` and a non-special `ell` sequence: `lambda^2 + P/2 = 0` coefficientwise, and `lambda^{(-)} = -lambda^{(+)}` termwise (deck exchange `rho |-> -rho`). Every step divides by `2 lambda_0`, so the recurrence exists and is unique **only** on `D(rho)`. Source naturality never performs this division.

### 3.3 Displayed determinants versus inverted maps — the gap

The formula-level total-coordinate maps (minus-then-plus, new jets `(az_n, ac_n)`, `(ez_n, ec_n)`, `(cs_n, rs_n)`) have leading 2×2 Jacobians

```text
det A = -2 lambda_0,
det C = -lambda_0 / 2,     C^{+/-} = (ec +/- lambda ez)/2,
det R = -lambda_0 / 2,     R^{+/-} = rs/4 +/- lambda cs.
```

After the jet map, the D1-named maps are

```text
A^{+/-} = AcD1 +/- lambda AzD1,           det = -2 lambda_0,
C^{+/-} = CcD1 +/- lambda CzD1,           det = -2 lambda_0,
R^{+/-} = BcD1 +/- lambda BzD1,           det = -2 lambda_0.
```

The extra `/2` on `C` and `/4` on `R` are already consumed by `ez -> 2 CzD1` and `rs -> 4 BcD1`.

Schema `shifted_root` writes

```text
A_jet:  AcD1_n +/- sum lambda_i AzD1_{n-i}
C_jet:  (CcD1_n +/- sum lambda_i CzD1_{n-i}) / 2
R_jet:  BcD1_n +/- sum lambda_i BzD1_{n-i}
diagonal_determinants: ["-2*lambda0", "-lambda0/2", "-lambda0/2"]
```

`C_jet` keeps the **total** `/2` while using **D1** names. `R_jet` is the D1 form. The displayed determinants are the **total** triple. A linker that implements `C_jet` against `d1_primitives` `CzD1,CcD1` halves the C root values.

The verifier inverts A in D1 form, C in total form, R in D1 form, then **pastes** the total-coordinate determinant strings. It never computes a Jacobian. Direct evaluation of the inverted blocks with `lambda_0 = 3`:

```text
Python (A, C, R) dets = (-6, -3/2, -6) = (-2 lambda_0, -lambda_0/2, -2 lambda_0)
displayed third       = -lambda_0/2 = -3/2
```

**Smallest counterexample.** The leading Jacobian of the R map actually inverted,

```text
(R^-, R^+) = (bc - lambda_0 bz,  bc + lambda_0 bz),
```

has determinant `-2 lambda_0`. Frozen `result.json` reports `"-lambda0/2"` as the third displayed determinant.

The triangular inversions themselves succeed through depth 3 on both decks, in **both** C conventions, because each convention is inverted against itself. That is a genuine invertibility check on `D(rho)` and a vacuous check that the coded `C_jet` equals the D1 substitution of (2.5).

### 3.4 Strongest surviving V2 statement, smallest repair

**Surviving.** Factor-`4`, factor-`2`, moving-`ell_1`, and omitted-`J` mutations fire at the stated first row-grades. Stage-zero names are annihilated by the generated lower ideal. `k2c` is not `k2load`. Hensel (2.2) holds on both decks through depth 10, and both plus/minus orientations of a bilinear shifted-pair map invert triangularly on `D(rho)` by dividing only by `lambda_0`. Localization is exactly `D(rho)`.

**Not surviving as a unique interface formula.** `shifted_root.C_jet` together with the pasted determinant triple.

**Smallest additive repair.** Choose one coordinate system and make `C_jet`, `R_jet`, and the three determinants agree with it; compute the three 2×2 Jacobians in the verifier. Concretely, either

- D1 names after (1.3): drop the `/2` on `C_jet`, set determinants `[-2 lambda_0, -2 lambda_0, -2 lambda_0]`; or
- total names as in (2.5): write `az,ac,ez,ec,cs,rs`, keep `/2` on C and `/4` on R, keep `[-2 lambda_0, -lambda_0/2, -lambda_0/2]`, and invert R as `rs/4 +/- lambda cs`.

This repair is local to the shifted-root block. It does not touch (1.1), the jet map, the tails, or V1.

**V2/root: GAP.** Mutations and Hensel/invertibility on `D(rho)` stand; the displayed-determinant witness and `C_jet` naming do not.

---

## 4. V3 support — CONFIRMED

### 4.1 Ten polar first grades, re-derived

```text
w(AC)     = 10 + a + c
w(C2)     = 10 + 2c
w(RA2)    = 12 + r + 2a
w(A3)     = 15 + 3a
w(k10R3)  = 10 + 3r
w(k10RC)  = 11 + r + c
w(k10R2A) = 13 + 2r + a
w(k10A2)  = 14 + 2a
w(k6C)    = 17 + c
w(k2R)    = 22 + r
```

The first eight delays are the eight `universal_hshift` summands in the pinned D1 compiler (`sigma^{10} t AC`, `sigma^{10} t^3 C^2`, `sigma^{12} t^2 B A^2`, `sigma^{15} t^4 A^3`, `sigma^{10} k B^3`, `sigma^{11} t k B C`, `sigma^{13} t^2 k B^2 A`, `sigma^{14} t k A^2`). The last two are the delayed-load polars, pinned in the schema and used as the reviewed inventory. Completeness of that inventory is a chamber-review input, not a V46 theorem; V3’s job is to consume it.

Family maximum `max_f(T) = max(T - w(M) : M contains f, w(M) <= T)`, with the leading-only convention `0`. Family `f` is **active at depth zero** when some licensed polar containing `f` arrives at or before `T`, even if `max_f = 0`. It is **inactive** when no such polar arrives. `P` is bounded from every polar that arrives (the only non-vacuous `P` bound: raw `F6 = 2P` has valuation 0).

### 4.2 Stored maxima, all eleven plus the sentinel

Every stored table recomputes exactly. Current grade-20 contact:

```text
(a,c,r;T) = (2,5,3;20)
arrivals: AC=17, C2=20, RA2=19, A3=21, k10R3=19, k10RC=19,
          k10R2A=21, k10A2=18, k6C=22, k2R=25
maxima:   p=3, A=3, C=3, R=1, k10=2, k6=0, k2=0
active:   p, A, C, R, k10
inactive: k6, k2
```

`k6=k2=0` here means **inactive**, not “leading jet present”. Contrast `D1_A2_A5` at `(2,3,2;16)`: `R=k10=0` but **active** (k10R3 and k10RC arrive at 16); `k6,k2` inactive. Contrast the sentinel `(20,21,20;38)`:

```text
arrivals: AC=51, C2=52, k10RC=52, k6C=38, k2R=42, others larger
maxima:   all 0
active:   p, C, k6          (k6C hits grade 38; AC and C2 are outside)
inactive: A, R, k10, k2
```

`p` active at relative depth zero on the sentinel is the stated over-retention: `k6C` does not display a `P` factor, but the `P` bound takes every arriving polar as a possible first grade. That is conservative, matches the stored sentinel, and is the policy V3 records.

### 4.3 Cancellation, useful `P` bound, wrong `C^2` ceilings

Cancellation in a frozen polynomial can only raise `sigma`-adic valuation. A raw census of unreduced `F_i` therefore cannot omit a jet that really occurs through `T`; it can only over-retain. For `P`, the raw bound is vacuous (`F6 = 2P` has valuation 0), so a useful `P` ceiling **requires** the reviewed first polar grade. That is a statement about valuations, not a V46 tagging experiment, and it stands.

`T` is the chamber terminal grade, not `10+2c`:

| Cell | `T` | `10+2c` | Distinguisher |
|---|---|---|---|
| `D23_E` `(1,4,2)` | 18 | 18 | same number; polar content is `A^3` at 18 and `R=2,k10=2`, not a C2-only table |
| `D23_A7` `(7,10,7)` | 30 | 30 | `k6=3, k2=1` active (load wall) |
| `D23_A8D2` `(8,10,8)` | 30 | 30 | `k6=3`, `k2` active at depth 0 |
| `D23_A8D3` `(8,11,8)` | 38 | 32 | `T ≠ C2` |
| `D23_A9` `(9,12,9)` | 38 | 34 | `T ≠ C2` |
| `AGE10` `(10,11,10)` | 38 | 32 | `T ≠ C2` |
| sentinel `(20,21,20)` | 38 | 52 | `C2` recedes to 52; only `k6C` hits 38 |

The V2 `T == 10+2c` mutation cannot fire at `E` or the `a=7,8` walls because the numbers coincide; V3 maxima are the control that actually distinguishes those theorems from a universal C2 ceiling. That is sufficient.

**V3: CONFIRMED.**

---

## 5. V4 provenance / lifecycle — CONFIRMED

All 24 endpoint artifacts rehash to the schema-pinned digests. Census: **ten** `status=promoted` families, each with a pinned authority whose status line is a genuine emptiness/composition promotion (`PROMOTED AFTER …` / `PROMOTED EXACT THEOREM …` / `PROMOTED — HOSTILE REVIEW CONFIRMED`), plus **exactly one** `confirmed_but_unpromoted` family.

`(a,c,r)=(8,11,8)` i.e. `(a,d,r)=(8,3,8)`:

- `authority` is JSON `null`. Filename inference is forbidden.
- Pinned review `02cbae00…` is the target-shadow chamber hostile review. Its overall verdict is `CONFIRMED`. The body is the four literal odd `SourcePhi` rows over exact `Q` (`[sigma^{28}] Phi1 = (3/4) k60 c1`, moving odd combination `S` with `[sigma^{38}] S = -(3/32) p eta k60 c1 b0`, difference from full odd rows exactly `-sigma^{38} J/4`). It is not an analytic-only bridge.
- Pinned `rejected_route` `451dd9eb…` opens `Status: **PROMOTED ROUTE FALSIFICATION ONLY.**` The firewall paragraph states it is a promoted impossibility for one proof route, not an emptiness statement. Two-column determinant `9p/512` on `k6 A^2` versus `k6 R C` is the negative. Schema `literal_row_policy` is `four reviewed odd SourcePhi rows only; reject analytic-only bridge`.

A linker that grepped `a8d3…promotion` and imported `451dd9eb…` as an emptiness authority would be wrong. V46 cannot do that: the family has no authority object, and V4 demands the falsification phrase on that artifact. The similarly named file is pinned **as** the trap, not as a theorem.

AGE10 additionally pins parent authority `d4aceedb…` and parent review `a4eff964…` (exact-contact parent of the closed ceiling). Those are two of the 24 hashes; they do not create an eleventh promoted family.

V4’s substring tests (`"PROMOTED"` in the first 1200 bytes of an authority, `"CONFIRMED"` in the first 2000 of the `(8,3,8)` review) are weak as parsers. The actual files’ status lines were read in this review and match the intended lifecycle. Combined with exact hashes and a null `(8,3,8)` authority, the census stands.

**V4: CONFIRMED.** The eleven-family union remains conditional. `(8,3,8)` is not promoted here.

---

## 6. Infrastructure sufficiency — CONFIRMED

Fable 5’s remaining common items were: freeze the schema with (1.1) normative; record compiler-agreement lemmas; per-manifest primitive comparison; generated renaming maps; a frozen V0–V4 verifier with one hostile review; and the `(8,3,8)` label. This review discharges the schema freeze and the V0–V4 hostile review for the source-naturality interface.

**Serial `ACT-TOT-G22`, `ACT-TOT-G24`, and later per-grade actual-total exporters are not mathematical proof obligations** once the jet-reindexing identity is the theorem. `[sigma^g] Phi_j^{total}` at `g = 22, 24, …` is a defined polynomial the moment the schema exists; an exporter only writes layer-3 bytes of it. Hostile-reviewed V46 is the last **common** artifact needed to remove those exporters from the mathematical critical path.

Remaining finite obligations, none of them serial grade exporters:

1. **Per-endpoint manifests** — `(a,c,r_floor)`, exact versus closed orders, `d`, `G`, `T`, licensed primitive inventory hash, mechanically derived maxima, load/target policy, localization, theorem type. V46 stores one test representative per family, not those manifests.
2. **Compiler-semantic checks** — V0 tokens are selected fragments. Each chamber compiler’s coded primitives still have to be compared to (1.4), including every load and target that can enter by that chamber’s `T`. The shared `r1_d1_ac` shape was byte-read here; that does not discharge other chamber emitters.
3. **Generated alias maps** — V46 generates one map at the current `(2,5,3)` maxima as a mutation control. A linker must still derive the renaming/scaling map from `(a,c,r)` and (3.2) per endpoint, never accept a handwritten map.
4. **Reviewed D1 endpoints** — ten promoted families and the mixed theorem types/localizations remain inputs. This interface does not re-prove them and does not reconcile them.
5. **`(8,3,8)` conditional** — confirmed-but-unpromoted; literal odd rows only. Union-level use stays conditional until a narrow promotion exists.

**Flagged additive V46 repair, not an exporter blocker.** Unique shifted-root coordinates (`C_jet` and the three Jacobians), as in §3.4. Linker duty 4 (“instantiate (2.2)–(2.5) through the required depth for both signs”) cannot be generated from the present schema without a coordinate convention. That is a common-interface gap in the **root-map** half. It does not re-open (1.5) and does not restore serial actual-total exporters as mathematical obligations.

---

## 7. Eligible promotion, exporters, exclusions

**Eligible for promotion, exactly this scope:** the V46 source-naturality schema and desk verifier — seven primitives over `Z[1/2]`, free `p0`, coefficient-ring jet reindexing, 569-tail byte/canonical custody, aliases, delays `4/12/20`, targets `28/32/36/38` with scales `1,1,1,1/4`, polar inventory, eleven lifecycle records with `(8,3,8)` held `confirmed_but_unpromoted`, and the V0–V1–V3–V4 checks that survived this review.

**Not eligible as a unique root-map formula, until the additive repair:** `shifted_root.C_jet` and the pasted determinant triple.

**Serial actual-total G22/G24+ exporters: yes, they can be removed from the mathematical critical path.** Campaign retirement of any concrete linker still waits on the per-endpoint list in §6. Grade-20 custody already banked remains defense in depth; nothing here re-validates its producer labels.

**Not promoted, and not concluded:**

- the eleven-family union as one emptiness theorem;
- `(a,d,r)=(8,3,8)` / `(8,11,8)`;
- `rho=0` ramified fibre;
- equality faces;
- positive-order leading loads;
- `k=0` / `k10`-leading coefficient zero;
- unlisted contacts;
- six staged Rees charts and the terminal/Taylor receiver;
- both global `G2` obligations;
- Gate T;
- order two;
- maximum twelve;
- JC2;
- a counterexample.

---

## 8. Execution record

Desk only. Independent Python `Fraction` and `F_1000003` truncated-series arithmetic; SHA-256; byte reads of the three pinned compilers and the `(8,3,8)` review/route pair. Producer verifier rerun with no `--output`. No Singular, Sage, msolve, Lean, AWS, web, or ledger edit. `jc2-lean` was not entered.

**CONFIRMED** as a provisional source-naturality schema/verifier, with one additive root-map uniqueness repair, promotion of the endpoint union and of `(8,3,8)` withheld.
