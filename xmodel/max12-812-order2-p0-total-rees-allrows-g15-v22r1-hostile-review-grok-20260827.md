# Hostile different-model review: actual-total all-row grade-15 export V22R1

Date: 2026-08-27
Reviewer: Grok 4.6, independent hostile mathematical and software reviewer.
Producer is not trusted. No PASS token or producer JSON is treated as evidence.
Case: `cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/`

## Verdict: CONFIRMED WITH REPAIRS

The seven harvested grade-15 polynomials are exactly the cutoff-15 actual-total
rows of the frozen 569-tail source. A clean-room reimplementation, using the
reviewed V20 source formulas extended by one jet coefficient and
`MAX_DEGREE = 15` set before any series is built, reproduces all fourteen
exported files **byte-for-byte in both serializations** and reproduces all
thirty-five historical V9/V20 polynomials as exact polynomial identities (Q)
and as exact identities after reduction (F65521). Named-section residuals
computed from the full polynomial bytes match the reviewed V21 theorem.

V1 failed closed solely because it demanded byte-identical text for
semantically equal polynomials. R1's monkey-patch can defer only that named
serialization tag; a duplicate or empty deferral census fails; a
mathematically unequal historical pair cannot PASS, because the ordinary
Singular script still guards all 35 equalities before the PASS banner, and
those equalities hold independently of Singular.

Five repairs are required of claims and evidence architecture. None changes
a coefficient, a term count, a section residual, or a historical identity.

This is an exported-prefix statement inside a frozen seven-row, degree-15
truncated model. It does not certify a J2 chart, a formal arc, the Rees
equations, Gate T, order two, maximum twelve, or JC2.

## 1. Custody: hashes, freezes, evidence completeness, two executions

All hashes below are observed locally.

Observed top-level hashes, all matching the assignment:

```text
PREREGISTRATION.md                         0c114f5990834b3ccdaa693d00a6265fd22dc72be7f7e501710b807def44b83c
PREREGISTRATION_R1.md                      34a087abdfc57efd6d1f898a6503a9129a8b93847d941bf5621f964234106eaf
V22_V1_SERIALIZATION_BRIDGE_ERRATUM.md     caf6261223c8b196d43806112d4d3534e05269c5911a60f92e74921095015d13
export_allrows_g15_v22.py                  c965726d2308358bf01c533fe89f2e28551abd9e3549fc699cd3e36d40ac82a6
export_allrows_g15_v22r1.py                d9f23a279b39b45ca27717a00493a6e928d1042007bc2c3c183eb2d239882768
validate_export_v22r1.py                   763f31fdc6d01e016e74e12eeac8be84ec79cd78e35c6fc589bef1c5ab848b7e
aws_q_r1/RESULT.json                       829239c93c9a8bcb34a0428391c378ddd662dbc70cfdd27a6b2cc3b6cdcf00b8
aws_p65521_r1/RESULT.json                  04c777e97b9113da9848c2c47fcfb3d880cc7b11319b74a0030dcc92aa92c94c
aws_q_r1/EVIDENCE.sha256                   f213026a454c8f3171c0ce3c8b6cdfb6fe1a22e663caec08d47d08666309def9
aws_p65521_r1/EVIDENCE.sha256              7e862a38d91ee12913ab35af62ab1ed229f3335a2a375604b03e5ab47dc64d40
aws_q_r1/compiled/result.json              ba9cb4f2e30bd570e4231a262fad0a616111f9602ecdd00d61cb19427496c4f0
aws_p65521_r1/compiled/result.json         8e6a66100af7fe5a6981fbd396eeff6d0548c57a368d5c78395fa1143e023ec6
```

Freeze manifests, every listed path rehashed:

```text
FREEZE.sha256     e48ee6d8f82a758db0f9033cdb91acd986a173d7124627a700bcc688826c822e   14/14 OK
FREEZE_R1.sha256  f58db2ff91c83bf3b52357889bb91d01f90dde2770eb0516fc89937f9db6ffb2   17/17 OK
```

`FREEZE_R1.sha256` includes the V1 freeze file, the frozen V1 exporter, the
erratum, the R1 wrapper/validator/launchers, and every upstream pin V22
needs (V20 emitter, replay, tails, both V9 manifests, both V20 compiled
results, V21 `RESULT.json`, `ops/aws_exact_lane.sh`). On-host
`sha256sum -c FREEZE_R1.sha256` is recorded as 17/17 `OK` in both harvested
`freeze_check.stdout` files, which are byte-identical
(`b98a65d2633b28ca18fe4bc88f7ac790b57233d453a42dc85d593c72e561b472`).

Evidence completeness, remote prefix remapped onto the harvested local
roots:

```text
Q prefix:
  /home/ubuntu/jobs/max12_812_order2_p0_total_rees_allrows_g15_export_v22_r1_20260827T031729Z_q/source/cases/.../aws_q_r1/
F65521 prefix:
  /home/ubuntu/jobs/max12_812_order2_p0_total_rees_allrows_g15_export_v22_r1_20260827T031729Z_p65521/source/cases/.../aws_p65521_r1/

aws_q_r1       listed=24  rehashed=24  unlisted local files=0
aws_p65521_r1  listed=24  rehashed=24  unlisted local files=0
```

Each root contains exactly those 24 files plus `EVIDENCE.sha256`. There is
no hidden harvested file.

Two distinct AWS executions, from launch registrations, compiler/engine
resource logs, and process metadata:

```text
Q:      host ip-172-30-0-186  pid 350975  char 0
        tag ...v22_r1_20260827T031729Z_q
        compiler 49.95 s, 43732 KiB, rc=0
        Singular 0.03 s, 11544 KiB, rc=0, ring R=0
F65521: host ip-172-30-0-45   pid 362464  char 65521
        tag ...v22_r1_20260827T031729Z_p65521
        compiler 49.91 s, 44604 KiB, rc=0
        Singular 0.02 s, 11256 KiB, rc=0, ring R=65521
shared source_archive_sha256  4f56f8cf355c54195e452d43826f5693a1e22e1ff6b03d679e2fbfb43a24f54e
```

Distinct machines, distinct pids, distinct compiled polynomials and control
scripts. Identical Singular stdout
(`a8855a31ad58820ccdd53ca71ded4f18d82f4d5c9113ab0c57b9ed6cb7f6698a`) is
expected: both scripts print the same banner strings and no polynomial
values. The tarball itself is not retained locally; that is a residual
custody gap of no mathematical effect, because the on-host freeze check
pins extracted inputs by content.

Post-harvest producer files `HARVEST_CUSTODY.md`,
`verify_harvest_v22r1.py`, and `INDEPENDENT_HARVEST_VERIFICATION.json` are
**not** in either freeze. They are untrusted prose/JSON. Every numerical
claim I use below is re-derived from the frozen exporter, the frozen
upstreams, and the harvested `.poly` / `.sing` bytes.

**Gap (D2).** The two failed V1 trees named in the erratum are not in this
case directory. The erratum's `compiler.stderr` hashes
`82a2e39d…` and `90773104…` cannot be rehashed here. What *can* be
established independently is the mathematical content of the erratum
(§2).

## 2. V1 failure mode and the R1 monkey-patch

V1 compares reconstructed text to historical text:

```python
if v20.singular_text(totals[row][grade], characteristic) != reference:
    fail(("old coefficient byte bridge", grade, row))
```

That `fail` aborts before any grade-15 file is written. The first pair in
insertion order is `(10, 1)`. Independently parsed:

```text
V22 Mine_Tg10_1 =
  (3/8)*a0*c1+(3/8)*a1*c0+(15/256)*cs*k*rs^2+(5/16)*cs^3*k*rho^2
V9  Ref_Tg10_1  =
  5/16*rho^2*cs^3*k+15/256*cs*rs^2*k+3/8*a0*c1+3/8*a1*c0
strings equal?  no
polynomials equal over Q?  yes
```

These are exactly the two strings in the erratum. So V1's first gate is a
term/factor-order and parenthesis-format comparison of one polynomial.

Across all 35 historical pairs, from the harvested `.sing` files, with
`Ref_*` checked against the hash-pinned V9 `.poly` files / V20 exports:

```text
                Q                F65521
Mine == Ref as strings          16/35              16/35
Mine == Ref as polynomials      35/35              35/35  (F65521 after reduction)
Ref == historical file          35/35              35/35
historical file hash            35/35              35/35
```

Byte matches are exactly `(10,6)`, `(11,6)` (both sides the token `0`) and
all fourteen V20 grade-13/14 files. Byte mismatches are exactly the
nineteen V9 files whose serializer differs from V20/V22 `singular_text`.
R1 records those same 19 pairs as `serialization_only_bridge_deferrals` in
both lanes. There is no mathematical discrepancy among the 35.

R1 loads the frozen V1 exporter under a hash gate
(`c965726d2308358bf01c533fe89f2e28551abd9e3549fc699cd3e36d40ac82a6`) and
replaces `v1.fail` by a wrapper that:

1. defers if and only if the message is a 3-tuple whose first entry is
   the exact string `old coefficient byte bridge` and whose other two
   entries are `int`;
2. otherwise calls the original `fail`, which raises.

V1 has 21 `fail(...)` sites. Only one uses that tag. Every other
fail-closed check (AWS lane, V20/V21/V9 hashes, tail contract, zero tail
coefficient, load nonlinearity, missing sensitivity delta, unknown sigma
weight, unexpected zero grade-15 row, rho parity, sigma homogeneity, V21
section mismatch, `qring` sentinel) remains fatal.

After `compile_export` returns, R1 requires `1 <= len(deferred) <= 35` and
uniqueness of `(grade, row)` pairs, pops the hardcoded V1 field
`old_coefficient_byte_bridges == 35`, and writes
`old_coefficient_exact_polynomial_bridges = 35`. It does **not** count
Singular successes; that 35 is a contract that the validator then
cross-checks against 35 `V22_OLD_BRIDGE_Tg{g}_{r}=1` banners, each of
which in the harvested `.sing` is preceded by

```text
if (Mine_Tg{g}_{r}-Ref_Tg{g}_{r}!=0) { print("FAIL_OLD_BRIDGE_..."); quit; }
```

A duplicate deferral fails the uniqueness census. Zero deferrals fails the
lower bound (so a hypothetical V1 that became byte-identical would not
silently skip the R1 repair). A missing historical pair cannot arise from
hash-pinned V1: `refs` is built from all 35 files before the comparison
loop, and the `.sing` emitter walks that same dict. Independently, both
harvested scripts contain all 35 `Mine_*`/`Ref_*` assignments and all 35
equality guards.

A mathematically unequal pair that was wrongly deferred would print
`FAIL_OLD_BRIDGE_*` and `quit` before `PASS`. The validator rejects any
`FAIL_` token and requires each of the 35 success banners exactly once.
Independently, all 35 pairs are equal as polynomials, so the banners are
justified rather than hollow.

**Conclusion of this item.** V1 failed only on byte identity of
semantically equal polynomials. R1 cannot suppress any other V1 failure.
A duplicate or empty deferral cannot PASS. All 35 semantic equalities are
present as ordinary-Singular guards before PASS, and they hold.

## 3. Grade-15 emitter versus reviewed V20

`build_source_series` in V22 is the V20 function with the cutoff and the
name-list endpoints raised by one, and with no other formula change.
After replacing the nine range/list endpoints by common placeholders the
two function bodies are **byte-identical**. Observed extension, matching
the preregistration:

```text
                    V20                         V22
p / ell             range(1, 15)                range(1, 16)     + ell15
c0 / cs             range(1, 13)                range(1, 14)     + cs13
r0 / rs             range(1, 13)                range(1, 14)     + rs13
az, ac, ez, ec      range(3, 10)                range(3, 11)     + az10,ac10,ez10,ec10
k10                 range(3, 11)                range(3, 12)     + k10_11
k6                  [k6, k6_1, k6_2]            [k6, k6_1, k6_2, k6_3]  + k6_3
MAX_DEGREE          14 (replay default)         15, assigned before build_source_series
```

The C-tuple and load shifts are unchanged: `C6..C0 = (2p, 2c, p^2+2r,
2pc+σ^2 n3, c^2+2pr+σ^2 n2, 2cr+σ^2 n1, r^2+σ^2 n0)` with `n3=σ^3 az`,
`n2=σ^3 ac`, `n1=σ^3(p·az+ez)/2`, `n0=σ^3(p·ac+ec)/2`; loads
`σ^4 k10`, `σ^{12} k6`, `σ^{20} k2`. Index-to-weight pairing remains
`(8,7,6,5,4,3,2 | 2,6,10)`. Rational scales `1/2` and `1/4` are unchanged.

`base.MAX_DEGREE = 15` is executed after `load_replay()` and before
`build_source_series`. Replay's `series_zero` / `series_mul` /
`series_shift` read `MAX_DEGREE` at call time, so the assignment is live.
Replay `main()` is behind `if __name__ == "__main__"` and is the only
AWS-gated, file-hashing entry; importing the module constructs nothing
and reads no tails. There is no accidental import side effect.

Truncation sufficiency of the extended heads, from the clean-room series
(occupied degree of each head at cutoff 15):

```text
C6 = 2p          last occupied 15     (need <=15; ell15 lives here)
C5 = 2c          last occupied 15     (c0[13] -> c[15])
k10 shifted      last occupied 15     (k10_11 at degree 11, +4)
k6  shifted      last occupied 15     (k6_3 at degree 3, +12)
k2  shifted      last occupied None   (shift 20; invisible below 20, correctly)
```

No head is short. Convolution at degree `d` uses only pairs summing to
`d`, so raising `MAX_DEGREE` from 14 to 15 cannot change grades `<= 14`.
That is independently confirmed by the historical 35-polynomial match.

Tails: `tails.json` hash `d72f774c…`, canonical
`6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`
(the value the reviewed replay module demands). Census:

```text
row     1   2   3   4   5   6   7    total
n      36  54  58  81  89 120 131     569
weight violations 0, zero coefficients 0, load nonlinearity 0, duplicate monomials 0
every tail coefficient denominator is a power of 2
(so inversion mod 65521 is defined for every tail coefficient)
every row-j monomial satisfies m·(8,7,6,5,4,3,2|2,6,10) = 12+j
```

All 569 entries are consumed. V22 `compile_export` fail-closes unless
`sorted(tails) == ["1",...,"7"]`.

Sigma weights used by the homogeneity guard were re-derived from the
emitter shifts, not copied from producer JSON: `rho` weight 0; `ell_d`
weight `d`; `cs_i` / `rs_i` weight `2+i`; `az_d` / `ac_d` / `ez_d` /
`ec_d` weight `5+d` (shift-by-3 then shift-by-2); `k10_i` weight `4+i`;
`k6_i` weight `12+i`; `k2` weight 20. The fixed names
`a0,a1,c0,c1,aa*,aaa*,e*,ee*,k,k1,k2c,k6` match the degree-0..2 slots of
those series.

Observation, not a defect: the nine new head names
`ell15, cs13, rs13, az10, ac10, ez10, ec10, k10_11, k6_3` do not occur in
any of the seven grade-15 supports. Grade 15 is populated by cutoff-15
products of already-present jets. Including the new heads is the
preregistered exactness contract; omitting them would not have changed
these seven polynomials, and including them did not inject an extra term.

## 4. Independent reconstruction of grades 0--15, and the 35 historical equalities

Clean-room series arithmetic (own sparse monomials, own convolution, own
binary `series_pow`) with the V20+1 source formulas and cutoff 15,
consuming the frozen 569 tails. Wall clock 27 s locally.

Per-row term counts by grade (mine):

```text
row 1: g0..g9 = 0,  g10=4,  g11=12, g12=27, g13=50,  g14=85,  g15=133
row 2: g0..g9 = 0,  g10=5,  g11=14, g12=36, g13=72,  g14=134, g15=224
row 3: g0..g9 = 0,  g10=5,  g11=17, g12=47, g13=103, g14=201, g15=355
row 4: g0..g9 = 0,  g10=2,  g11=3,  g12=12, g13=30,  g14=71,  g15=140
row 5: g0..g9 = 0,  g10=5,  g11=18, g12=58, g13=141, g14=304, g15=585
row 6: g0..g11= 0,                  g12=9,  g13=32,  g14=90,  g15=200
row 7: g0..g9 = 0,  g10=5,  g11=18, g12=60, g13=156, g14=364, g15=759
```

Grades 13/14 match the reviewed V20 counts. Grade 15 matches the harvested
counts `133,224,355,140,585,200,759`. Contributing-tail counts at grade 15
match the compiler: `35,50,55,72,83,104,119`.

Re-serialising with the V20 `singular_text` convention reproduces the
harvested files byte-for-byte:

```text
Tg15_1_q         4d237049cdd6fbaf05a14dcda0710fdb1660058241b0b3a72e1c0c473e7a40ba  MATCH
Tg15_2_q         5a438032b3d558131246d3022006b68cc424f4c09bfcef0215e8ce8ea76e0e69  MATCH
Tg15_3_q         53d513df5003c5b0e60a50aff59779d9c921374e8878dea8e7ba9f3152d294d4  MATCH
Tg15_4_q         2cf0b1d34df224ba0df2b60bdd7b8144fd733d35133edd851c91d27a9b830748  MATCH
Tg15_5_q         26e2f4ef586955dddd1d694343f1bf29f28f050e4da61f386b2e11fb44a08f08  MATCH
Tg15_6_q         786c6bb976305614cc0945b2ebf0d78600fb9a96aefa1553248ff8f473b5c51e  MATCH
Tg15_7_q         1b3eb2ae0963ee0044a209d91f8dc3ca9ef4d11c3dd47633d799219449bfcddd  MATCH
Tg15_*_p65521    3ac69f1e…, 14132ad9…, c258b291…, 9a1e84f1…, c6b99348…,
                 87fe41d1…, 4ce53890…                                               MATCH 7/7
byte-identical: 14/14 in both serializations
```

The same reconstruction, compared as polynomials to the hash-pinned V9
files (grades 10--12) and V20 files (grades 13--14):

```text
clean-room == historical   35/35 over Q
clean-room == historical   35/35 after reduction mod 65521
```

Separately, `Mine_*` inside both `.sing` scripts equals the reconstructed
polynomial and `Ref_*` equals the historical file (35/35, both lanes). The
object Singular tested is the object reconstructed here.

This is exact-Q computation. Characteristic is used only in
`singular_text` (and in which historical file is loaded). See §5 for what
the F65521 lane does and does not corroborate.

## 5. Exact Q versus characteristic 65521

Both compilers run identical `Fraction` arithmetic. Diff of the two
`compiled/result.json` objects: characteristic, lane tag, paths, hashes,
and the two serialized control scripts. Identical fields include term
counts, contributing-tail counts, supports, sensitivity monomials,
deferral list, and the exact-Q section residuals.

What the F65521 lane **does** corroborate, independently of producer JSON:

- Every Q coefficient of every grade-15 polynomial has denominator
  invertible mod 65521 and numerator not divisible by 65521. Parsed
  F65521 term counts equal Q term counts; no `0*` term appears in any
  F65521 file; reducing Q coefficientwise reproduces each F65521 file
  on the nose (support and coefficients, 7/7).
- V9's F65521 files use mixed-sign representatives (e.g. `40951 ≡ -24570
  (mod 65521)` for `3/8`). Ordinary Singular in ring `R=65521` still
  reports `Mine-Ref==0` for all 35 historical pairs, and an independent
  reduction of both sides agrees.
- Source-sensitivity deltas are nonzero after reduction, so the
  non-degeneracy check is live in that ring.
- The harvested F65521 `.poly` files are exactly the V20-style
  serialization of the same Q polynomials.

What it **does not** corroborate:

- An independent reconstruction in characteristic 65521. There is no
  wrap-around, no distinct cancellation pattern, no second arithmetic
  kernel. A bug in the Q `Fraction` convolution would appear in both
  lanes.
- Named-section identities computed in F65521 by a second source
  evaluation. Sections are evaluated over Q in Python even on the
  F65521 job (`singular_text(..., 0)`), then recorded in both results.

This is the V20 dual-lane architecture, and `HARVEST_CUSTODY.md` already
states it. The V1 preregistration's phrase "independently over `F_65521`"
overstates the independence. Repair of the claim, not of the polynomials.

The same latent term-count construction as V20 remains: `len(polynomial)`
is taken on the Q dict regardless of characteristic. Untriggered here
(no coefficient vanishes mod 65521).

## 6. Fourteen grade-15 files, parsed independently

Restricted-AST walker (integers promoted to `Fraction`; `^` as power; no
`eval`). Hashes match `RESULT.json`. Term counts
`133,224,355,140,585,200,759` in both serializations. Declared variable
supports match observed supports (rho first, then sorted), including the
smaller supports of rows 4 (37 names) and 6 (32 names).

Every monomial of every Q polynomial:

- has even `rho` exponent;
- has literal sigma-weight 15 under the emitter-induced weights.

Q-to-F65521: support and every reduced coefficient match; zero modular
vanishing events; no serialized `0*` coefficients.

Highest jets that actually appear are `ell5, cs5, rs5, az5, ac5, ez5,
ec5, k10_5`. No `k6*` name appears in any grade-15 support.

## 7. Named sections, from the full polynomial bytes, versus V21

Not from compiler JSON. For each of the seven Q polynomials, substitute
`rho` free and every other name 0 except the distinguished name (or none,
for Z00):

```text
CS0 (cs=1):  all seven rows 0
Z00 (none):  all seven rows 0
A00 (a0=1):  row 6 = -1/16 ; rows 1,2,3,4,5,7 = 0
A10 (a1=1):  row 3 = -1/16
             row 5 = -(3/32) rho^2
             row 7 = -(3/128) rho^4
             rows 1,2,4,6 = 0
```

These are the unique one-name survivors: among every source name that
occurs in any grade-15 polynomial, the only nonzero one-name sections are
`a0` and `a1`, with exactly those residuals. In particular the same-weight
names `c0` and `c1` (weight 5) give the zero polynomial, so the evaluator
distinguishes `A00`/`A10` from a same-weight unrelated section.

The four nonzero values are literally the coefficients of `a0^3`,
`a1^3`, `a1^3 rho^2`, and `a1^3 rho^4`. Mutation: replacing the `a0^3`
coefficient of `Tg15_6` by `-1/16 + 1` changes the A00 residual from
`-1/16` to `15/16`. The evaluator is discriminating.

Homogeneity remark: `cs` has weight 2 and `rho` has weight 0, so no
`cs^a rho^b` monomial can have weight 15; CS0 at grade 15 is implied by
sigma-weight 15. Z00 is implied because a pure-`rho` monomial has weight
0. Those two zeros are still true of the exported bytes, but they are
not an independent reconstruction test at this grade. V21's all-depth
statement is the right instrument for CS0/Z00; this export's load-bearing
section content is A00/A10.

The same section scan on the hash-pinned V9 (grades 10--12) and V20
(grades 13--14) Q files finds **no** nonzero named-section residual in
any of the 4×7×5 evaluations. Combined with reconstructed grades 0--9
being identically the zero polynomial, the first nonzero named-section
grade of this model is 15 for A00 and A10, and CS0/Z00 remain zero on
the exported prefix. That is V21's `first_nonzero_grade` field, now
seen from the polynomials themselves rather than from V21's specialized
evaluator.

V21 modular reductions of the four constants, recomputed:

```text
-1/16  ≡ 4095  (mod 65521)  ≡ 22002 (mod 32003)
-3/32  ≡ 38903 (mod 65521)  ≡ 1000  (mod 32003)
-3/128 ≡ 26106 (mod 65521)  ≡ 250   (mod 32003)
```

These match the frozen V21 `modular_reductions`. V21 itself was reviewed
CONFIRMED (Fable 5) as an all-depth specialized evaluation of the same
emitter on the same 569 tails; this export agrees with that theorem at
grade 15 and does not re-prove the all-depth identity by an untruncated
specialized sum. The two methods (specialize-then-sum in V21;
export-then-specialize here) agree on the grade-15 named residuals.

## 8. Source-sensitivity, Singular hazards, PASS-after-fail

Seven controls, one per row, recorded identically in both compiled
results. Each monomial exists in `tails.json` (odd rows: index 2, load
`k10`; even rows: index 1, load `k6`), satisfies the row weight, and has
a power-of-two tail coefficient. Harvested `.sing` content:

```text
Wrong_Tg{g}_{r} = Mine_Tg{g}_{r} + delta
if (Wrong - Ref == 0) { FAIL_SOURCE_SENSITIVITY; quit; }
```

Independently parsed, every `delta` is nonzero over Q and nonzero mod
65521, and `Mine+delta != Ref`. Given `Mine == Ref`, this is equivalent
to `delta != 0` in the engine ring: a non-degeneracy check that one
frozen tail's unit contribution at a V9 grade is visible. It is **not**
a re-emission of the row with that tail coefficient incremented. It does
exercise the historical `Mine`/`Ref` pair (the mutated polynomial is
compared to the historical reference), and it would catch a totally dead
reconstruction. It would not catch a wrong reconstruction that happened
to have some nonzero tail contribution at that grade. Limitation, not a
false PASS.

Singular scripts, both lanes:

- no `qring`, `execute`, `random`, `system(`, `LIB `, `proc `;
- ring `R={0|65521},(49 vars),dp` whose variable set equals the names
  used in `Mine`, `Ref`, and `Wrong` (no missing name, no extra name);
- 56 `FAIL_*` / `quit` guards (35 old-bridge, 7 nonzero, 7 rho-parity, 7
  sensitivity) plus a final `quit`;
- `PASS_TOTAL_REES_ALLROWS_G15_EXPORT_V22` is the last print, after every
  guard;
- `V22_QRING_DISABLED=1` is an unguarded echo; the actual qring check is
  the Python `"qring " in control.read_text()` fail-closed test, which
  the harvested scripts pass.

The validator does not parse polynomials. It checks compiler-result
fields, rehashes coefficient files along the AWS absolute paths (valid
on the host), demands the resource-stderr shape (`Command being timed:`
once, `Exit status: 0` once), rejects `FAIL_/?/error occurred/Killed/out
of memory`, and requires each listed banner exactly once. A producer who
printed banners without performing the algebra could satisfy the
validator; the frozen V1 emitter, the harvested `.sing` text, and the
independent reconstruction close that hole. PASS cannot appear after a
failed mathematical guard in the harvested scripts: failure prints
`FAIL_*` and quits, and the validator would reject `FAIL_` even if
`quit` were removed.

No local Singular run was performed (AWS-only lane, and the instruction
is to leave heavy algebra on AWS). Equality of the two sides of every
guard was established by an independent parser, and the reconstruction
supplies the left-hand sides from the tails.

## 9. Convention drift; what this export certifies

Searched: emitter index-to-name maps, load nonlinearity `{0,1}`, tail
weights `12+j`, `p[0] = -2 rho^2`, scales `1/2` and `1/4`, C-tuple
ordering, load shifts 4/12/20, rho-evenness, sigma-weight 15, no
`jc2-lean` access, no qring. No drift relative to reviewed V20. No
missing Rees tail: 569/569 consumed, same census as V20/V21. No missing
source-series term relative to the V20+1 contract; the new heads happen
not to appear in the grade-15 supports (§3).

The export certifies, inside the frozen seven-row actual-total source
model with sparse cutoff 15:

- the seven full literal grade-15 polynomials over Q, and their F65521
  serializations;
- that this model's grades 10--14 equal the reviewed V9 and V20
  polynomials;
- that this model's grades 0--9 are the zero polynomial;
- that the four named point-sections of the grade-15 rows are the V21
  values, and that those named sections of grades 10--14 of the
  exported historical files are zero.

It cannot certify: emptiness or nonemptiness of a J2 chart; any formal
arc; the geometric Rees equations (the 569 tails are a frozen compile,
not re-derived here); Gate T; order two; maximum twelve; JC2. A nonzero
constant at A00 or A10 kills that named point of this source model only.

## Defects and their actual mathematical effect

**D1 — dual-lane independence is overstated.** Both jobs compute the same
Q polynomials. F65521 is serialization plus an ordinary-Singular check
in characteristic 65521, plus coefficientwise reduction of the Q files.
**Effect:** none on correctness. The genuine modular content is the
reduction match and the char-65521 historical equalities, both of which
hold. The preregistration should not say the F65521 export is an
independent algebraic derivation.

**D2 — V1 failed trees are not harvested.** Erratum stderr hashes are
unreproducible from this case directory. **Effect:** none on the R1
polynomials. The erratum's two strings are independently equal as
polynomials and are exactly `Mine_Tg10_1` / `Ref_Tg10_1`. That V1 died
at the first byte comparison is the only behaviour hash-pinned V1 can
have, given the 19 mismatches.

**D3 — source-sensitivity is non-degeneracy, not a +1 re-emit.**
`Wrong = Mine + unit_term` tests `delta != 0` once `Mine = Ref`.
**Effect:** none on the exported polynomials. The historical bridges
and the clean-room reconstruction already pin the tails.

**D4 — latent F65521 term-count construction.** `len(Q-dict)` is reported
even for the F65521 result. **Effect:** none here; no coefficient
vanishes mod 65521 and no `0*` term is serialized. Same untriggered V20
defect.

**D5 — CS0/Z00 at grade 15 follow from sigma-weight 15.** They are true
of the bytes and of V21, but they are not an independent reconstruction
test at this grade. **Effect:** none; A00/A10 are the discriminating
section content, and they were checked by substitution, by generator
coefficient, by mutation, and by a same-weight unrelated name (`c0`).

**Not a defect.** `V22_QRING_DISABLED=1` is an unguarded echo; qring
absence is still fail-closed in Python and by inspection of the
harvested scripts. R1 freeze does not recursively re-check V1-only
paths (`PREREGISTRATION.md`, unused V1 launchers); those paths are not
on the live R1 compile. Extra named jets unused in grade-15 support:
cutoff-15 products of old jets populate the export; the new heads are
provisioned and idle.

## Strongest precisely scoped theorem justified by the evidence

Let `S` be the frozen actual-total source determined by:

- the 569 tails of
  `cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json`
  (SHA-256 `d72f774c…`), seven rows, tail weights `12+j`, load exponents
  in `{0,1}`;
- the reviewed V20 generic emitter
  (`export_allrows_g13_g14_v20.py`, SHA-256 `5c233e0f…`) with sparse
  cutoff raised to 15 before construction and with the nine name-list
  endpoints extended by one coefficient
  (`ell15, cs13, rs13, az10, ac10, ez10, ec10, k10_11, k6_3`);
- exact rational arithmetic.

Then, writing `Tg_{g,j}` for the sigma-degree `g` piece of row `j`:

1. `Tg_{g,j} = 0` for all `j=1..7` and all `g <= 9`, and also
   `Tg_{10,6} = Tg_{11,6} = 0`.
2. For `g=10,11,12`, `Tg_{g,j}` equals the corresponding V9 polynomial
   (hash-pinned by `COEFFICIENTS.json` `86c535a3…` / `dc775709…`) as an
   element of `Q[names]` and, after coefficient reduction, as an
   element of `F_{65521}[names]`.
3. For `g=13,14`, `Tg_{g,j}` equals the corresponding reviewed V20
   polynomial (hash-pinned by compiled `result.json` `b37b9564…` /
   `3e763bd4…`) in both serializations.
4. The seven polynomials `Tg_{15,1},…,Tg_{15,7}` are nonzero, rho-even,
   and sigma-homogeneous of weight 15, with term counts
   `133, 224, 355, 140, 585, 200, 759`. They are the harvested files
   `aws_q_r1/compiled/Tg15_*_q.poly` and
   `aws_p65521_r1/compiled/Tg15_*_p65521.poly` (hashes in §1 and §4).
   Reducing the Q files modulo 65521 recovers the F65521 files with
   identical support and no vanishing coefficient.
5. Named point-sections of `Tg_{15,•}` with `rho` free:
   `CS0 = Z00 = 0`;
   `A00` is `-1/16` in row 6 and 0 in the other six rows;
   `A10` is `-1/16` in row 3, `-(3/32)rho^2` in row 5,
   `-(3/128)rho^4` in row 7, and 0 in rows 1, 2, 4, 6.
   The same named sections of the historical files at grades 10--14 are
   all zero. This agrees with the reviewed V21 all-depth theorem at
   grade 15.

Nothing in (1)--(5) implies a J2-chart statement, a formal-arc
statement, a Gate T / order-two / maximum-twelve / JC2 statement, or
emptiness of any chart other than the four named prefix points of this
finite source.

## Reproduction commands

From `/Users/dc/code/math/jc2`. No campaign file is written.

```bash
# 1. Observed hashes and both freezes
python3 - << 'PY'
from hashlib import sha256
from pathlib import Path
base = Path("cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827")
obs = {
"PREREGISTRATION.md": "0c114f5990834b3ccdaa693d00a6265fd22dc72be7f7e501710b807def44b83c",
"PREREGISTRATION_R1.md": "34a087abdfc57efd6d1f898a6503a9129a8b93847d941bf5621f964234106eaf",
"V22_V1_SERIALIZATION_BRIDGE_ERRATUM.md": "caf6261223c8b196d43806112d4d3534e05269c5911a60f92e74921095015d13",
"export_allrows_g15_v22.py": "c965726d2308358bf01c533fe89f2e28551abd9e3549fc699cd3e36d40ac82a6",
"export_allrows_g15_v22r1.py": "d9f23a279b39b45ca27717a00493a6e928d1042007bc2c3c183eb2d239882768",
"validate_export_v22r1.py": "763f31fdc6d01e016e74e12eeac8be84ec79cd78e35c6fc589bef1c5ab848b7e",
"aws_q_r1/RESULT.json": "829239c93c9a8bcb34a0428391c378ddd662dbc70cfdd27a6b2cc3b6cdcf00b8",
"aws_p65521_r1/RESULT.json": "04c777e97b9113da9848c2c47fcfb3d880cc7b11319b74a0030dcc92aa92c94c",
"aws_q_r1/EVIDENCE.sha256": "f213026a454c8f3171c0ce3c8b6cdfb6fe1a22e663caec08d47d08666309def9",
"aws_p65521_r1/EVIDENCE.sha256": "7e862a38d91ee12913ab35af62ab1ed229f3335a2a375604b03e5ab47dc64d40",
"aws_q_r1/compiled/result.json": "ba9cb4f2e30bd570e4231a262fad0a616111f9602ecdd00d61cb19427496c4f0",
"aws_p65521_r1/compiled/result.json": "8e6a66100af7fe5a6981fbd396eeff6d0548c57a368d5c78395fa1143e023ec6",
}
for rel, exp in obs.items():
    got = sha256((base/rel).read_bytes()).hexdigest()
    print(("OK" if got==exp else "BAD"), rel)
for man in ("FREEZE.sha256","FREEZE_R1.sha256"):
    ok = 0
    for line in (base/man).read_text().splitlines():
        h, f = line.split(None, 1)
        assert sha256(Path(f).read_bytes()).hexdigest() == h, f
        ok += 1
    print(man, ok, "OK")
PY

# 2. Evidence completeness with remote-prefix remap
python3 - << 'PY'
from hashlib import sha256
from pathlib import Path
base = Path("cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827")
for lane, prefix in [
    ("aws_q_r1", "/home/ubuntu/jobs/max12_812_order2_p0_total_rees_allrows_g15_export_v22_r1_20260827T031729Z_q/source/cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/"),
    ("aws_p65521_r1", "/home/ubuntu/jobs/max12_812_order2_p0_total_rees_allrows_g15_export_v22_r1_20260827T031729Z_p65521/source/cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_p65521_r1/"),
]:
    root = base/lane
    listed=set(); bad=0
    for line in (root/"EVIDENCE.sha256").read_text().splitlines():
        h, remote = line.split(None, 1)
        rel = remote[len(prefix):]
        listed.add(rel)
        got = sha256((root/rel).read_bytes()).hexdigest()
        bad += got != h
    actual={str(p.relative_to(root)) for p in root.rglob("*") if p.is_file() and p.name!="EVIDENCE.sha256"}
    print(lane, "listed", len(listed), "bad", bad, "unlisted", sorted(actual-listed), "missing", sorted(listed-actual))
PY

# 3. Clean-room reconstruction and historical/section checks
#    (scripts used in this review; re-run from /tmp copies or re-author)
#    python3 /tmp/v22r1_hostile_rebuild.py     # ~30s; expects byte-identical 14/14 and historical 35/35
#    python3 /tmp/v22r1_hostile_audit.py       # parse 14 files, Q->F65521, sections, Mine/Ref, sensitivity
#    python3 /tmp/v22r1_hostile_sections_hist.py
#
# Minimal inline Q->F65521 and A00/A10 check of the harvested bytes:
python3 - << 'PY'
import ast
from fractions import Fraction
from pathlib import Path
CASE=Path("cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827")
PRIME=65521
def parse(text):
    text=text.strip()
    if text=="0": return {}
    t=ast.parse(text.replace("^","**"), mode="eval")
    def pn(n):
        if isinstance(n, ast.Expression): return pn(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, int):
            v=Fraction(n.value); return {} if not v else {(): v}
        if isinstance(n, ast.Name): return {((n.id,1),): Fraction(1)}
        if isinstance(n, ast.UnaryOp):
            x=pn(n.operand)
            return x if isinstance(n.op, ast.UAdd) else {m:-c for m,c in x.items()}
        if isinstance(n, ast.BinOp):
            L,R=pn(n.left), pn(n.right)
            if isinstance(n.op, ast.Add):
                o=dict(L)
                for m,c in R.items(): o[m]=o.get(m,0)+c
                return {m:c for m,c in o.items() if c}
            if isinstance(n.op, ast.Sub):
                o=dict(L)
                for m,c in R.items(): o[m]=o.get(m,0)-c
                return {m:c for m,c in o.items() if c}
            if isinstance(n.op, ast.Mult):
                o={}
                for ma,ca in L.items():
                    da=dict(ma)
                    for mb,cb in R.items():
                        d=dict(da)
                        for k,e in mb: d[k]=d.get(k,0)+e
                        m=tuple(sorted((k,e) for k,e in d.items() if e))
                        o[m]=o.get(m,0)+ca*cb
                return {m:c for m,c in o.items() if c}
            if isinstance(n.op, ast.Div):
                den=next(iter(R.values())); return {m:c/den for m,c in L.items()}
            if isinstance(n.op, ast.Pow):
                e=int(next(iter(R.values()))); ans={():Fraction(1)}; base=L
                while e:
                    if e&1:
                        tmp={}
                        for ma,ca in ans.items():
                            da=dict(ma)
                            for mb,cb in base.items():
                                d=dict(da)
                                for k,ex in mb: d[k]=d.get(k,0)+ex
                                m=tuple(sorted((k,ex) for k,ex in d.items() if ex))
                                tmp[m]=tmp.get(m,0)+ca*cb
                        ans={m:c for m,c in tmp.items() if c}
                    e//=2
                    if e:
                        tmp={}
                        for ma,ca in base.items():
                            da=dict(ma)
                            for mb,cb in base.items():
                                d=dict(da)
                                for k,ex in mb: d[k]=d.get(k,0)+ex
                                m=tuple(sorted((k,ex) for k,ex in d.items() if ex))
                                tmp[m]=tmp.get(m,0)+ca*cb
                        base={m:c for m,c in tmp.items() if c}
                return ans
        raise RuntimeError(ast.dump(n))
    return pn(t)
def red(p):
    o={}
    for m,c in p.items():
        r=(c.numerator*pow(c.denominator,-1,PRIME))%PRIME
        if r: o[m]=r
    return o
def section(p, one):
    o={}
    for m,c in p.items():
        rho=0; ok=True
        for n,e in m:
            if n=="rho": rho+=e
            elif n!=one: ok=False; break
        if ok: o[rho]=o.get(rho,0)+c
    return {k:v for k,v in o.items() if v}
for row,n in zip(range(1,8),[133,224,355,140,585,200,759]):
    q=parse((CASE/f"aws_q_r1/compiled/Tg15_{row}_q.poly").read_text())
    p=parse((CASE/f"aws_p65521_r1/compiled/Tg15_{row}_p65521.poly").read_text())
    assert len(q)==len(p)==n and red(q)==red(p)
print("Q->F65521 7/7, counts", [133,224,355,140,585,200,759])
q={r: parse((CASE/f"aws_q_r1/compiled/Tg15_{r}_q.poly").read_text()) for r in range(1,8)}
assert all(not section(q[r],"cs") and not section(q[r], None) for r in range(1,8))
assert section(q[6],"a0")=={0:Fraction(-1,16)}
assert section(q[3],"a1")=={0:Fraction(-1,16)}
assert section(q[5],"a1")=={2:Fraction(-3,32)}
assert section(q[7],"a1")=={4:Fraction(-3,128)}
print("named sections OK")
PY
```

Local Singular was not run. Historical `Mine-Ref` equalities were checked
by parsing both sides of the harvested `.sing` files and by reconstructing
the left-hand sides from the tails. The AWS engine logs show `engine_rc=0`,
`Exit status: 0`, no `FAIL_` token, and all 35 `V22_OLD_BRIDGE_*` banners
once each.
