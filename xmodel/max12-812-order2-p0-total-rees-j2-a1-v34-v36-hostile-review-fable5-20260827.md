# Hostile review: V34--V36 grade-19 orbit obstruction (ordered `T-a1`, `rho=0`, V32 six-coordinate support)

Reviewer: Fable 5 (independent), 2026-08-27.
Working tree: `/Users/dc/code/math/jc2` (branch `master`, HEAD `418e413` at review time).
Cases under review:

- `cases/max12_812_order2_p0_total_rees_j2_a1_grade18_curve_cut_v34_20260827/`
- `cases/max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_20260827/`
- `cases/max12_812_order2_p0_total_rees_j2_a1_grade19_orbit_unit_v36_20260827/`

Upstream artifacts audited only as referenced: V32 (grade-17 sparse support),
V33 (grade-18 prolong), V30/V28 (grades 17/16), V23 census + parser, V20
export module, the pinned replay engine, and the frozen tails. No network, no
AWS, no heavy CAS; all local checks were exact rational arithmetic, hashing,
and file reads. `jc2-lean` untouched.

## Verdict

**PASS WITH AMENDMENT** for the narrow conclusion:

> The normalized V34 degree-five scheme inside the V32 six-coordinate
> ordered-`a1`, `rho=0` support has no grade-19 prolongation. This says
> nothing about the rest of the ordered `T-a1` chart.

No computational defect was found anywhere in the chain. Every load-bearing
number was independently re-derived locally, and the decisive unit-ideal
inference was re-proved by exact field arithmetic without trusting Singular.
The amendments (Section 8) are scope-language and provenance clarifications,
not corrections: (a) "prolongation" must be read as simultaneous vanishing of
the seven literal actual-total rows `Tg19_1..Tg19_7` of the frozen row model
(row 7 alone obstructs); (b) the grade-19 rows themselves exist only as
V35's single-implementation reconstruction (the p65521 lane is a mod-p
serialization of the same exact-Q build), anchored to independent exports
only through grade 18; (c) the V35/V36 validators are not replayable
verbatim off the original AWS host because their `result.json` files store
absolute AWS paths (their full logic was replayed here with path remapping).

## 1. Freeze, evidence, and pin integrity

All verified against current bytes:

- `FREEZE.sha256`: V34 13/13, V35 19/19, V36 11/11 lines OK (`shasum -a 256 -c`).
- `EVIDENCE.sha256` (six lanes, AWS-absolute paths remapped via
  `/source/cases/...` -> repo): **104/104** hashes match local bytes.
- Cross-case pins all hold and are frozen redundantly:
  - V34 pins parser `14f2de22`, V32 `BASIS.txt` `ee4f7780`, V32
    `compile_result.json` `cdbb884e`, V33 rows `fdfb477f`/`252175cd` and
    results `22f64fbb`/`9f5fd6e4`.
  - V35 pins V33 module `5941bf87` (which pins V28 `6c76dc54`, V20
    `5c233e0f`, parser, V23/V28/V30 results), V34 `RESULT.json`s
    `7796c99a`/`f293aaa2`, V34 Q basis `1e81e737`.
  - V36 pins V34 bases `1e81e737`/`96990faf` and both V35 `result.json`s
    `074c7b81`/`1b61cee0`.
- Preregistration hashes embedded in every compile/evaluate result match the
  frozen `PREREGISTRATION.md` files (checked all three cases, both lanes).
- Lane hygiene: `launch_registration.txt`, `freeze_check.stdout` (all OK
  lines), `lanes.log` rc=0 for every lane, `/usr/bin/time -v` stderr with
  `Exit status: 0`, meta files with stdout/stderr hashes that match the
  hashed files. V34/V36 Singular jobs ran in ~0.00 s / ~10.6 MB; the V35
  compiler (series build to grade 19 + 63 bridges) ran 3:53 wall / ~140 MB.
- Validator replays: the V34 validator re-run locally on the frozen inputs
  reproduces both lane `RESULT.json` files **byte-identically**. The V35 and
  V36 validators dereference AWS-absolute paths stored in `result.json`
  (see amendment c); their complete check logic was replayed locally with
  path remapping and reproduces every field of all four frozen
  `RESULT.json` files exactly.

## 2. V34: the degree-five scheme (audit item 1)

V34 appends the six-coordinate restriction of `Tg18_6` (a1=48; keep
`ell2,cs1,rs2,aa0,ee1,ec3`; kill all else) to the complete V32 grade-17
standard basis (24 generators; `V32_DIM=1` is attested in the frozen V32
Singular stdout, so "proper dimension-one ideal" in the prereg is
supported). Outcome in both characteristics: `dim 0`, `vdim 5`,
`unit_ideal 0`, 12-generator basis; identical NF file
`384*ell2*aa0-3456*cs1+144*ec3` (hash `77ea74d9`, same bytes both lanes).

Local exact verification (beyond the engine):

- **Restriction replay.** `restrict(parse(Tg18_6_q.poly))` has 16 terms,
  matches the `P18` line of the frozen `grade18_curve_cut_q.sing`
  byte-for-byte, and its mod-65521 shadow equals the restriction of the
  frozen p-row. The aa0=0 Laurent control replays exactly:
  branch value `{l^-1: 41472}`.
- **Kummer structure is forced by the basis, engine-free.** From the 12
  generators alone: `ee1*ec3=21600` makes `t:=ec3` a unit in the quotient;
  `600cs1=11ec3`, `192ell2=7ee1`, `ec3^2=-3750aa0`, `7aa0*ec3=2880rs2`
  express every coordinate as a rational multiple of a power of `t`; and
  `rs2*aa0=210` then forces `t^5 = 210*2880*3750^2/7 = 1215000000000 = N`.
  So the quotient is a homomorphic image of `Q[t]/(t^5-N)`; conversely all
  12 generators vanish identically under the parametrization
  `ell2=1575/(2t), cs1=11t/600, rs2=-7t^3/10800000, aa0=-t^2/3750,
  ee1=21600/t, ec3=t` in `Q[t]/(t^5-N)` (verified exactly). Since
  `N = 2^9*3^5*5^10` is not a rational fifth power, `t^5-N` is irreducible
  and `Q[t]/(t^5-N)` is a **field** of degree 5. Hence the V34 scheme is
  irreducible, **reduced**, of degree 5 — exactly the claimed Kummer
  scheme — independently of Singular's `vdim` (which agrees: 5). The
  displayed V35 presentation (`t^5=1215000000000` and the coordinate
  formulas) is byte-consistent with this derivation.
- **All 24 V32 generators also vanish** on the parametrization (exact), so
  the quintet lies on the V32 curve as required.
- **p-basis shadow.** Each of the 12 p65521 generators equals a unit
  multiple of the mod-p reduction of a Q generator, 12/12 matched.
- **The aa0=0 companion branch.** The free Laurent line
  `(aa0,ell2,cs1,rs2,ee1,ec3) = (0, l, 12/l, -20l^2/9, 32l, 576/l)` does
  *not* lie on V(V32) (13/24 generators fail as Laurent polynomials), but
  after imposing `l^5 = 243/2` every failing value collapses to 0: the
  "known aa0=0 branch" is the quintet of points with `l^5=243/2`, precisely
  as the V34 prereg words it. `Tg18_6` restricted evaluates to `41472/l`
  there, never zero, so that quintet is killed at grade 18. Independent
  cross-check: V33's frozen dual constant for its sigma-scaled rational
  representative (`a1=708588`, `ell2=243/2`, `aa0=0`) is
  `16210220612075905068 = 4*3^39`, and the hand-scaled value
  `(82944/243)*(708588/48)^4` of `41472/l` reproduces it exactly. V33's
  normalization also gives `l^5 = (243/2)^5/(3^10/4)^2 = 243/2` exactly.
  This locks V33 <-> V34-prereg <-> V34-output together and explains
  `vdim=5`: of V32's dim-1 locus, `Tg18_6` removes the one-dimensional
  part and the aa0=0 quintet, leaving only the aa0!=0 Kummer quintet.

Observation (not a defect): the V34 Q and p65521 Singular stdouts are
byte-identical (hash `9797797c`) *including* `option(prot)` traces and
criterion counts (112/82, 236/155). For this tiny ideal that is plausible —
the p-basis is the unit-scaled shadow of the Q basis, so the dp pair
trajectory can coincide — and it is immaterial here because the decisive
artifacts (the bases) differ per lane, are mutually consistent, and the Q
conclusion is re-derived engine-free above. A future case wanting
independent-looking lanes could add a lane-distinguishing print.

## 3. V35: source depth, 63-row bridge, sigma scaling (audit items 1, 2)

- **Series depth endpoints.** `build_source_series_19` is the V33 grade-18
  builder extended by exactly one entry per family and nothing else:
  `ell1..ell19`; `cs,cs1..cs17` (shift 2 -> degree 19); `rs,rs1..rs17`;
  `az/ac/ez/ec` index 0..14 (effective shift 5 -> weight 19 at index 14);
  `k10` index 0..15 (shift 4 -> 19); `k6` index 0..7 (shift 12 -> 19);
  `k2` at shift 20 (inert through grade 19, same convention as V28/V33).
  `n1`/`n0` internal products need `az/ez` (`ac/ec`) only through index 14
  with `p` through 13 — covered. The pinned replay engine resolves
  `MAX_DEGREE` from module globals at call time, so `base.MAX_DEGREE = 19`
  set before any series construction genuinely extends all series; no
  stale-length hazard (`load_replay()` builds nothing at import).
- **Row builder.** V35 reuses frozen `v28.build_row`: 10-slot tails,
  weighted census `= 12 + row` with weights `[8,7,6,5,4,3,2,2,6,10]`,
  loads forced linear, zero tail coefficients forbidden. Tails are the
  frozen `tails.json` `d72f774c` pinned inside the pinned V20 module.
- **63-row bridge.** 42 V23 rows (grades 10–15, `a1_ordered` chart outputs,
  additionally rho-killed) + 21 rows from V28 (g16), V30 (g17), V33 (g18),
  every file hash-pinned through the respective frozen result manifests;
  bridge count enforced `== 63`. Grades 10–12 descend from the independent
  V9 exporter and grade-14 row 5 is byte-bridged to V17 inside the frozen
  V20 job, so the reconstruction is anchored to genuinely independent
  pipelines through grade 18.
- **Local endpoint replay (this review).** Loading all 63 frozen row files
  (each digest re-verified) and evaluating exactly: all 63 vanish at the
  rational point `a1=192, ell2=21/4, cs1=11, rs2=-35, aa0=-96, ee1=576,
  ec3=2400` (absent variables = 0), and the registered mutation
  `rs2 -> -34` flips exactly 5 rows nonzero — `Tg14_2, Tg15_3, Tg16_4,
  Tg17_5, Tg18_6` — matching `mutation_nonzero_rows = 5`.
- **Grade-19 values.** Evaluating the seven frozen `Tg19_*_q.poly` files
  (term counts 222/375/533/298/667/282/552, matching `result.json`; hashes
  match; parse->serialize round-trips byte-identically): rows 1–6 give 0,
  `Tg19_7 = -7077888`. This replays V35's headline claim from frozen
  artifacts without the series build.
- **Sigma scaling to the rational representative.** With the frozen parser
  weights (`a1,ell2,cs1,rs2,aa0,ee1,ec3` -> `5,2,3,4,6,7,8`) and
  `lambda = t^3/13500000` in `K = Q[t]/(t^5-N)`: `lambda^5 = 4` exactly,
  and coordinate-wise `x * lambda^{w(x)}` maps the `a1=48` Kummer point to
  the rational point exactly (all seven coordinates, verified in `K`).
  The five geometric points (five embeddings of `K`) all map to the same
  rational representative under their respective `lambda` choices, so, by
  sigma-homogeneity of the rows (verified: all seven grade-19 rows are
  weight-19 homogeneous), a nonzero row value at the rational
  representative kills the entire normalized quintet. The orbit logic the
  V35 prereg flags for independent review is hereby confirmed.

## 4. The known V35 weakness (audit item 3) — confirmed, correctly declared

Code-verified: `--characteristic` changes only (i) the `.poly`
serialization (`singular_text(..., 65521)`) and (ii) the
`lane_nonzero_rows` filter `modular(value)`. The entire reconstruction,
bridging, and evaluation runs over exact Q in both lanes; the two frozen
`result.json`s differ **only** in `characteristic`, `coefficient_paths`,
`coefficient_sha256`, and `registered_aws_lane`, with `grade19_values_q`
identical. So the V35 p-lane replicates determinism of one code path, not
modular independence. The V35 validator performs token/contract/hash checks
only and recomputes nothing. Both facts match the review brief's
characterization: V35 alone is not promotion grade. It is the discovery
and freezing step; the proof burden falls on V36.

## 5. V36: does it repair the gap? (audit item 4) — yes, with one inherent residue

Verified in code and by local replay:

- **Pins and contract.** V36 hash-pins the V34 bases and both V35
  `result.json`s and hard-fails unless both lanes report
  `outcome=killed`, `grade19_values_q = {Tg19_7: -7077888, others: 0}`,
  `lane_nonzero_rows = ["Tg19_7"]`.
- **Q/p row shadow.** All seven frozen Q rows against all seven frozen p
  rows, monomial-by-monomial modular shadow — replayed locally, 7/7 PASS.
- **Homogeneity.** All seven Q rows sigma-weight-19 homogeneous — replayed,
  PASS.
- **Receiver absence.** No variable of sigma weight 19 occurs in any of
  the seven rows — replayed, PASS; in fact the maximum variable weight
  present is **14**. Crucially the check runs on the *unrestricted* faces
  before the six-coordinate restriction (which would have hidden
  receivers), and the kill set `J1 ∪ {a0, rho} = {rs,cs,c0,c1,a0,rho}`
  contains no weight-19 variable (weights 2,2,5,5,5,0), so the check is
  not vacuous. Moreover receiver absence is structurally forced, not
  accidental: every coefficient/load series in the row construction has
  degree-0 part either zero or a multiple of `rho^2`, and every tail
  monomial has at least two factors (the largest single slot weight is
  10 < 13 <= 12+row), so a weight-19 variable can enter a grade-19
  component only multiplied by a rho-positive cofactor, which the
  `rho=0` chart kills. The empirical check confirms a theorem of the
  construction.
- **Restriction replay.** `restrict(Tg19_7)` (a1=48, six coordinates) has
  28 terms; regenerated `P19` text matches the frozen Q and p65521 `.sing`
  scripts byte-for-byte; the p-face equals the mod-p shadow of the Q-face;
  the `ideal G` lines in both scripts equal the frozen V34 basis files
  byte-for-byte.
- **Independent Singular reductions.** Fresh `std`/`reduce` in each
  characteristic on AWS (engine logs clean, `Exit status: 0`): NF nonzero
  (`FAIL_ZERO_NORMAL_FORM` guard), then unit ideal
  (`FAIL_NOT_UNIT_IDEAL` guard), final bases `1` in both fields.
  Outputs: `Tg19_7_mod_grade18_q.txt = 110592/35*rs2`,
  `Tg19_7_mod_grade18_p65521.txt = 18136*rs2` with
  `18136 = 110592 * 35^{-1} mod 65521` (verified), i.e. the exact modular
  shadow of the Q normal form.
- **Validators / freezes / evidence.** Both lane validators PASS with all
  token, resource, and diagnostic-token checks; `RESULT.json` fields
  reproduced exactly by local logic replay; FREEZE and EVIDENCE fully
  verified (Section 1).

Inherent residue (not repairable by V36's design and correctly outside its
claims): both V36 lanes consume rows descending from V35's single
Q-implementation (two separate AWS executions of the same pinned
deterministic code). Characteristic-independence in V36 therefore checks
the Singular/Groebner layer, and the Q/p shadow checks catch corruption or
nondeterminism, but a systematic bug in the shared V35 series builder
would propagate to both lanes. The compensating evidence is the 63-row
byte-exact anchoring through grade 18 to three older independent export
pipelines, the minimal one-entry-per-series code delta from the bridged
V33 builder (diffed in this review), and the structural receiver argument
above. I consider this adequate for the narrow claim, flagged as
amendment (b).

## 6. The mathematical inference (audit items 5, 6)

The inference is airtight and was re-proved here without the engine:

1. In the V34 coordinate ring `A` (≅ the degree-5 field
   `K = Q[t]/(t^5 - 1215000000000)` by Section 2), the basis relation
   `rs2*aa0 = 210` makes `rs2` a unit with inverse `aa0/210`.
2. Therefore `NF(Tg19_7) = (110592/35)*rs2` is a unit of `A`; adjoining
   `Tg19_7` yields the unit ideal. Singular's `V36_UNIT_IDEAL=1` in both
   characteristics is thereby *forced*, and was independently confirmed:
   evaluating the 28-term restricted `P19` on the Kummer parametrization in
   `K` gives exactly `-(32/15625) t^3 = (110592/35) * rs2(t)`, a nonzero
   element of a field (exact computation, bypassing NF entirely).
3. Numerical lock: `lambda^19 * (-(32/15625) t^3) = -7077888` exactly in
   `K`, and by weights alone `-7077888 = -110592 * 4^3` (weight 19 = 4+15,
   `mu^5 = 1/4`), so the V35 point value, the V36 normal form, and the
   `a1: 48 -> 192` normalization are mutually consistent frozen numbers.
4. Because the unit-ideal statement is scheme-theoretic over Q, it covers
   all five geometric points at once (and any non-reduced structure, which
   Section 2 rules out anyway); the orbit argument of V35 is subsumed.
5. No escape routes inside the stated scope: (i) a *new* grade-19 jet
   cannot absorb the obstruction — no weight-19 receiver occurs in any of
   the seven grade-19 rows (checked pre-restriction; structurally forced);
   (ii) a *previously zero* weight-<=18 source jet turning nonzero leaves
   the six-coordinate support and hence the precise V34 scheme — expressly
   outside the claim; (iii) rows `Tg19_1..Tg19_6` could only cut further;
   row 7 obstructs alone; (iv) the residual `Z/5` sigma freedom of the
   `a1=48` slice permutes the quintet and changes nothing (all displayed
   relations are weight-homogeneous mod 5 — spot-checked).

## 7. Defects versus scope limitations

Defects found: **none** that affect soundness. Minor engineering
observations (no action strictly required):

- O1. V35/V36 `result.json` store AWS-absolute `coefficient_paths` /
  `script` / `nf_path`, so their validators cannot be re-run verbatim
  off-host (V34's validator, taking paths as CLI arguments, replays
  byte-identically). Logic replay with remapping succeeds and reproduces
  every field. Recommend relative paths in future cases.
- O2. V34's compiler accepts any nonempty `JC2_REGISTERED_AWS_LANE`
  (V35/V36 pin their case-specific tag prefixes). Cosmetic.
- O3. V34's q/p Singular protocol stdouts are byte-identical (explained and
  defused in Section 2); V36's engine stdouts are identical trivially
  (token-only output).

Scope limitations (inherent, correctly declared in the frozen preregs and
result `scope` fields):

- S1. The conclusion is confined to the V32/V34 six-coordinate normalized
  support. The rest of the ordered `T-a1` chart — any solution with a
  source coordinate outside `{ell2,cs1,rs2,aa0,ee1,ec3}` nonzero, or off
  the `rho=0`, `J1=0`, `a0=0` stratum — is untouched.
- S2. "Rows" means the seven literal actual-total rows of the frozen tails
  model (`tails.json` `d72f774c`); grade-19 components exist only as V35's
  reconstruction (single implementation; see Section 5 residue).
- S3. Characteristic-65521 artifacts are replication/shadow evidence; the
  operative statement is the characteristic-0 one (which is the claim).

## 8. Required amendments to the promotion language

1. State the obstruction concretely: *"the seven actual-total rows at
   grade 19 (of which `Tg19_7` alone suffices) have no common zero on the
   V34 scheme; `Tg19_7` restricts to the unit `(110592/35)*rs2` of its
   degree-five coordinate field."*
2. Record the provenance qualifier: *"grade-19 rows are the frozen V35
   reconstruction (exact-Q, single implementation, two concordant AWS
   executions); independent-pipeline bridging covers grades 10–18 only."*
3. Note O1 (absolute paths) for successor reviews so nobody mistakes a
   failed verbatim validator re-run for an artifact defect.

With these clarifications the proposed narrow conclusion is exactly right,
including its final sentence. The V34 five-point Kummer scheme — the last
surviving locus of the V32 six-coordinate support after grade 18 — is dead
at grade 19.

## Appendix A: key hashes

| Artifact | SHA-256 |
| --- | --- |
| V34 `aws_q/RESULT.json` | `7796c99ab5bdc2253754b3ca5f86adb42f2c192c6a2a575dd1f81d9cc69226fe` |
| V34 `aws_p65521/RESULT.json` | `f293aaa2bb005778209e1ecbf9b3e12e9a3c59554f24989737b3d8b031babd46` |
| V34 `BASIS_G18_q.txt` (12 gens) | `1e81e737cdab19a9a1b3cb2c6253fecc82c266db236af6fcf67aa03dbd419e40` |
| V34 `BASIS_G18_p65521.txt` | `96990faf637dc5f3c4bb5b72881fed8fd0b004361b97151605f30c6be3d82bfa` |
| V35 `aws_q/compiled/result.json` | `074c7b817d115805ea6e784225fc1dad64d54769ae89421a78ba65769903e256` |
| V35 `aws_p65521/compiled/result.json` | `1b61cee08b92feeff059ac3a961a4fe8f1f8d355c022a9f1f7eb8dd97726c3f2` |
| V35 `Tg19_7_q.poly` (552 terms) | `6049a9362d101e821759eb6f394b0bce2b20ea2e801e50183671454677a3a356` |
| V36 `Tg19_7_mod_grade18_q.txt` (`110592/35*rs2`) | `543d2b81e46806b7eea239713c5bbdcf9140da92124e4ec7e819c2aefef8aa8e` |
| V36 `Tg19_7_mod_grade18_p65521.txt` (`18136*rs2`) | `3e752b3a7010f1719e746a1a53c07313f2956294f847f3f2fa81c276c432590c` |
| V36 final bases (`1`) | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` |
| Parser `census_j2_typed_v23.py` | `14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501` |
| Frozen tails `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |

## Appendix B: local exact checks performed (all PASS unless noted)

1. 12/12 V34 Q generators vanish on the Kummer parametrization in
   `Q[t]/(t^5-N)`; `rs2*aa0-210` present verbatim.
2. `t^5 = N` forced by generator elimination; `N = 2^9*3^5*5^10` is not a
   fifth power (field/reducedness).
3. 12/12 p-basis generators are unit-scaled mod-p shadows of Q generators.
4. 24/24 V32 generators vanish on the parametrization; the free aa0=0
   Laurent line fails 13/24 but the `l^5=243/2` quintet satisfies 24/24;
   V33's dual constant `= 4*3^39` reproduced by hand-scaling `41472/l`.
5. Restricted `Tg18_6`: 16 terms, Laurent `{-1:41472}`, vanishes on the
   quintet, mod-p shadow exact, byte-equal to the frozen `.sing` `P18`.
6. Seven grade-19 rows: manifest hashes, term counts, weight-19
   homogeneity, **no weight-19 receivers (max weight 14)**, 7/7 Q->p
   shadows, values `(0,0,0,0,0,0,-7077888)` at the rational point,
   serialize/parse round-trip byte-exact.
7. 63 frozen rows through grade 18: all vanish at the rational point;
   `rs2+1` mutation flips exactly `{Tg14_2,Tg15_3,Tg16_4,Tg17_5,Tg18_6}`.
8. Restricted `P19`: 28 terms, byte-equal to both frozen `.sing` scripts;
   embedded `ideal G` byte-equal to the frozen bases.
9. `P19` on the scheme `= (110592/35)*rs2 = -(32/15625) t^3 != 0` in the
   field; p-NF `18136*rs2` is its exact shadow.
10. `lambda = t^3/13500000`: `lambda^5 = 4`; all seven coordinates scale
    `a1=48` point -> rational point; `lambda^19 * value = -7077888 =
    -110592 * 4^3`.
11. Kill set `{rs,cs,c0,c1,a0,rho}` contains no weight-19 variable;
    parser weight table spot-checked on 17 names.
12. V34 validator: byte-identical `RESULT.json` reproduction (both lanes).
    V35/V36 validators: full logic replay with path remapping, all fields
    reproduced (both lanes). FREEZE 43/43 lines, EVIDENCE 104/104 entries.

-- end of report --
