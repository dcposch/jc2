# Hostile review — T-cs ordered chart, total row-five grade-14 export V17

Reviewer: independent hostile review (Opus 5), 2026-08-26.
Package: `cases/max12_812_order2_p0_total_rees_t_cs_row5_g14_export_v17_20260826/`.

Method note: no producer PASS string, prose claim, or finite-field agreement is
relied on below. Every quantitative assertion was re-derived here from the
frozen bytes, using an independent parser and an independently written second
implementation of the source. Local recomputation stayed inside the producer's
own measured envelope (producer compiler: 5.05 s, 28.9 MB; this review's
independent rebuild: ~25 s, 22.6 MB peak). No heavy CAS was used and none was
needed.

---

## 0. Summary

Every quantitative claim is true and was independently reproduced:

| Claim | Independent finding |
|---|---|
| Literal total source `p=-2*rho^2+sum_(i=1)^14 2*ell_i*sigma^i` | Confirmed at `export_row5_g14_v17.py:128-137` |
| Grades 10/11/12 bridge exactly to frozen V9 | Confirmed as polynomials over `Q` and mod 65521; `Ref_d` are byte-literal V9 files |
| Grade-14 coefficient has 304 terms | Confirmed: 304 distinct monomials |
| Nonzero | Confirmed |
| Even in `rho` | Confirmed: rho-degree histogram `{0:103, 2:116, 4:74, 6:11}` |
| Odd-sheet specialization `= -(21/320)*b^5*w^2` | Confirmed exactly, by hand and by machine |
| `11/5` is a genuine negative control | Confirmed non-vacuous: yields `-(41/640)*b^5*w^2` |
| F65521 is only an encoding/software control | Confirmed; no modular inference enters the char-0 claim |

Three defects are recorded. None changes the exported mathematics:

- **D1 (attestation, this package).** Two of the eight registered engine flags
  are printed unconditionally; the Singular lane never tests the odd-sheet
  specialization or the negative control.
- **D2 (upstream V9).** `validate_coeffexport_v9.py:128` miscounts
  every leading-minus polynomial by one, including all three coefficients used
  here.
- **D3 (custody).** The evidence manifests are self-attesting and the launcher's
  outer transcripts are never harvested.

---

## 1. Freeze, evidence, return codes, validators, custody gaps

### Verified

`FREEZE.sha256` has ten entries and all ten verify byte-for-byte in the working
tree today: `PREREGISTRATION.md`, `export_row5_g14_v17.py`,
`validate_export_v17.py`, `run_aws.sh`, `launch_host.sh`, the upstream
`replay_row5_grade14.py`, the frozen `tails.json`, both V9 `COEFFICIENTS.json`
manifests, and `ops/aws_exact_lane.sh`. The freeze is transitively tight on the
V9 coefficient files themselves: the raw `Tg{10,11,12}_5.poly` are not in the
freeze list, but `export_row5_g14_v17.py:237` checks each against the
`coefficient_sha256` map inside the frozen `COEFFICIENTS.json`. I re-verified
those three digests (`5c1d7ae3`, `ca08b238`, `9389b34a`) against the files.

Both harvested lanes verify completely. `aws_q/EVIDENCE.sha256` and
`aws_p65521/EVIDENCE.sha256` list 18 files each; all 36 local files match their
recorded digests, and there are no unlisted files in either tree. On-host
`freeze_check.stdout` reproduces the same ten `OK` lines in both lanes and the
two files are byte-identical (`cd40885d…`).

Return codes and resource records are clean and consistent:
`compiler_rc=0`, `engine_rc=0`, `validator_rc=0` in both lanes; `/usr/bin/time -v`
reports `Exit status: 0` for both the compiler and the engine. Exact-Q compiler:
5.05 s wall, 28.9 MB RSS. Engine: 0.00 s, 9.6 MB. Two distinct hosts
(`ip-172-30-0-186` for `q`, `ip-172-30-0-45` for `p65521`), same job stamp
`20260826T214230Z`, both engine lanes starting `21:42:53Z`.

`RESULT.json` in each lane is internally honest: `coefficient_sha256`,
`control_script_sha256`, `compiler_result_sha256`, `stdout_sha256`, and
`resource_stderr_sha256` all match the actual local artifacts, and
`compiler.stdout` parses to exactly the JSON in `compiled/result.json`.

The two lanes share an identical engine `stdout_sha256`
(`0ead117c…`). That is expected rather than suspicious — the Singular stdout is
nine constant flag lines — but it is worth stating plainly that the engine
transcript carries no lane-specific mathematical content whatsoever.

No post-freeze mutation is detectable. `export_row5_g14_v17.py` (mtime
`14:41:54` local) was last edited after the other package files (`14:41:22`)
but before `FREEZE.sha256` (`14:42:25`); every harvested artifact postdates the
freeze (`14:43:24`–`14:43:40`), and the on-host freeze check independently
re-established the same digests at run time.

### Custody gaps (stated as required)

**G1 — the engine does not test two registered controls (defect D1).**
`export_row5_g14_v17.py:268-269` emits

```
print("V17_NORMALIZED_ODD_SPECIALIZATION=1");
print("V17_NEGATIVE_NORMALIZATION_CONTROL=1");
```

as unconditional literals into the generated `.sing`. The generated script
contains no `subst`, no comparison against `-(21/320)*b^5*w^2`, and no `11/5`
evaluation. Preregistration controls 4 and 5 are therefore attested *only* by
the producer's own Python process. `validate_export_v17.py:30-31` does not
repair this: it checks `result["normalized_odd_specialization"]` and
`result["negative_normalization_control"]`, which are literal constants the
compiler writes into its own `result.json` at lines 289-290. The check is not
vacuous (the compiler raises at lines 215 and 220 before reaching that dict),
but it is entirely self-reported. I closed this gap independently in §4.

**G2 — self-attesting manifests.** `run_aws.sh:36` generates `EVIDENCE.sha256`
on the same host, in the same process tree, after the run. Nothing external
notarises or timestamps it, and nothing binds the local copies to the remote job
other than digests carried in the same transfer.

**G3 — unharvested launcher transcripts.** `launch_host.sh:16` redirects
`run_aws.sh` to `$remote_job.outer.stdout` / `.outer.stderr`, which sit *outside*
`$aws_job` and are therefore excluded from `EVIDENCE.sha256` and never
harvested. Any `set -e` failure diagnostics at the wrapper level are
unrecoverable from this package.

**G4 — host alias binding unverifiable.** `launch_host.sh:5` maps `Box02` /
`Box03` / `r6d` to fixed elastic IPs, but the package records only the internal
names `ip-172-30-0-186` and `ip-172-30-0-45`, with no record of which alias was
passed. The alias-to-instance binding cannot be checked from the evidence.

**G5 — the memory cap is decorative.** `cap_kib=524288000` (≈500 GiB) against a
28.9 MB actual peak. Harmless here, but it is not a control.

**G6 — no repository anchor.** The entire case directory is untracked in git, so
`FREEZE.sha256` itself has no immutability anchor beyond the working tree.

**G7 — term count is self-reported.** `RESULT.json`'s
`coefficient_term_count: 304` is copied from the compiler's own telemetry;
neither the validator nor the engine recounts it. (Independently confirmed in §4.)

**G8 — grade 13 is silent.** The source is nonzero at grade 13 (141 terms, see
§4), but grade 13 is neither exported nor bridged nor mentioned. "Through grade
14" is accurate for the *source extension*; the *export* is grades 10, 11, 12,
and 14 only.

---

## 2. Trace to the literal total source

### The source is literal, and matches the frozen replay exactly

`export_row5_g14_v17.py:128-160` builds, with `MAX_DEGREE = 14` inherited from
the frozen replay:

- `p[0] = -2*rho^2`, `p[d] = 2*ell_d` for `d = 1..14` — the literal total source,
  with no normalization and no dropped `rho` or `ell1`.
- `c = sigma^2*(cs + cs1*sigma + … + cs12*sigma^12)`.
- `r = (p^2 + sigma^2*(rs + rs1*sigma + … + rs12*sigma^12))/4`.
- A/C corrections `az, ac, ez, ec` dense in degrees 0..9, with
  `n3 = sigma^3*az`, `n2 = sigma^3*ac`, `n1 = sigma^3*(p*az+ez)/2`,
  `n0 = sigma^3*(p*ac+ec)/2`, each shifted a further `sigma^2` inside
  `coefficients[3], [2], [1], [0]`.
- Loads `sigma^4*(k + k1*sigma + k2c*sigma^2 + k10_3*sigma^3 + … + k10_10*sigma^10)`,
  `sigma^12*(k6 + k6_1*sigma + k6_2*sigma^2)`, `sigma^20*k2`.

Term-by-term this is the frozen replay's construction
(`replay_row5_grade14.py:177-220`) with the seven specialized entries restored
to free variables and the three assigned entries generalized. The
correspondence, which I checked slot by slot, is:

| replay | V17 | meaning |
|---|---|---|
| `p[0], p[1]` absent | `-2*rho^2`, `2*ell1` | `rho = ell1 = 0` restored |
| `rs[0]` absent | `rs` | `rs = 0` restored |
| `ac[0]` absent | `a0` | `a0 = 0` restored |
| `ez[0]` absent | `c1` | `c1 = 0` restored |
| `ec[0], ec[1]` absent | `c0`, `e0` | `c0 = e0 = 0` restored |
| `cs[0] = b` | `cs` | `cs = b` generalized |
| `ez[1] = b^2*w` | `e1` | `e1 = b^2*w` generalized |
| `k10[0] = (12/5)*w^2` | `k` | `k = (12/5)*w^2` generalized |
| `az2, ac2, k10_1, k10_2, k6_0, k2_0` | `aaa1, aaa0, k1, k2c, k6, k2` | renaming only |

So the V17 substitution map at lines 200-211 is exactly the inverse of the
replay's specialization. Nothing else is specialized, and nothing is dropped.

### No omissions, no duplicate conventions

- **Tail contract.** Every one of the 89 row-5 tails is checked for length 10 and
  weight exactly `17 = 12 + row` against `[8,7,6,5,4,3,2 | 2,6,10]`, with the
  three load slots forced linear. All 89 pass; `tail_terms_checked = 89` is
  correct. Only `tails["5"]` is read — no other source row leaks in.
- **Truncation.** Every series is dense and exactly long enough. `az/ac/ez/ec`
  index 9 lands at grade 14 (shift `3+2`); `k10` index 10 lands at grade 14
  (shift 4); `k6` covers 12..14. Nothing needed for grade ≤ 14 is truncated
  away. The `sigma^20` load is identically zero below grade 15, so the four
  slot-9 tails legitimately contribute nothing — their true grade is ≥ 20.
- **The weight-6 load near-miss, checked explicitly.** Eleven row-5 tails use
  the `sigma^12` load. Since 17 is odd, every weight-11 coefficient
  decomposition must contain an odd-weight factor (indices 1, 3, 5), each of
  minimum grade 2 — so those tails *can* reach grade 14 exactly, and `k6`
  should have appeared in the ring. It does not. I computed the grade-2 part of
  all eleven coefficient products in exact rationals: they sum to zero. The
  absence of `k6, k6_1, k6_2` from the 40-variable ring is a genuine
  cancellation, not a truncation omission.

### No stale specialized-source import

`load_replay()` hash-pins both the replay and `tails.json` before importing, and
imports under the module name `odd_row5_replay_frozen`, so `__name__` is never
`"__main__"` and the replay's `main()` never runs. That matters: the replay's
*specialized* source, its hard-coded `b`, `w`, `(12/5)*w^2`, and its own AWS
gate all live inside `main()`. The replay is used strictly as a `Fraction`
polynomial/series library. There is no stale specialized import and no module
level side effect. The `-(21/320)` constant is hard-coded in V17 at line 213
rather than read from a replay artifact, but the identical constant sits in the
hash-pinned replay at line 249, so it is corroborated by frozen bytes.

The generated scripts contain no `qring`, declare `ring R=0,(…),dp` (rationals)
and `ring R=65521,(…),dp`, and both terminate with `quit;`. All 40 ring
variables are used and every symbol appearing in `Mine*`, `Ref*`, and `G14` is
declared — so no symbol could have been silently treated as zero. The exported
`Tg14_5_*.poly` is byte-identical to the `G14` text embedded in the
corresponding `.sing`.

---

## 3. The grade-10/11/12 bridge, and the V8/V9 defect

I re-parsed the generated `.sing` with my own parser and compared as
polynomials, without trusting Singular's `!=0` test:

| grade | `Mine` terms | `Ref` terms | `Mine == Ref` over `Q` | `Ref` is byte-literal V9 file |
|---|---|---|---|---|
| 10 | 5 | 5 | yes | yes |
| 11 | 18 | 18 | yes | yes |
| 12 | 58 | 58 | yes | yes |

The same holds in the F65521 lane modulo 65521 against the separately produced
V9 `aws_p65521_v9` shard files. The bridge is real.

### The registered V8 `TPhi` rebuild defect does **not** affect anything used here

The known defect (recorded as M1 in
`xmodel/max12-812-order2-p0-total-rees-t-rs0-rowshard-v8-hostile-review-grok-20260826.md`)
is that V8's `TPhi=` matcher over-matches the stream-release line and appends a
second full `TPhi` schedule after extraction. In the V9 row-5 program
`aws_q_v9/compiled/t_rs0_row5_q.sing`, the three writes used by V17 occur at

```
1386: write("…/Tg10_5.poly",Tg);
1399: write("…/Tg11_5.poly",Tg);
1412: write("…/Tg12_5.poly",Tg);
```

and the second `TPhi=0;` begins at line **1432**. All three extractions are
strictly before the rebuild. The defect cannot reach any coefficient in this
bridge. Confirmed harmless for V17.

### A second V9 defect (D2), distinct from the registered one — also harmless here

`validate_coeffexport_v9.py:128` computes term counts as
`value.count("+") + value.count("-") + 1`, which counts a *leading* minus sign
as a separator. Consequently every V9 polynomial whose serialization begins with
`-` has `coefficient_term_telemetry` exactly one too high. Fourteen of the 42
entries are affected, including all three used here:

| key | telemetry | actual file terms | Singular's own `size(Tg)` |
|---|---|---|---|
| `Tg10_5` | 6 | 5 | 5 |
| `Tg11_5` | 19 | 18 | 18 |
| `Tg12_5` | 59 | 58 | 58 |

(The other eleven are `Fg11_1..5`, `Fg12_1`, `Fg12_2`, `Fg12_4`, `Fg12_5`,
`Fg12_7`, `Tg12_4`; every affected file and only affected files begin with `-`.)
The row-5 transcript records `T_RS0_TERMS_10_5=5`, `T_RS0_TERMS_11_5=18`, and
`T_RS0_TERMS_12_5=58`, matching
the files and matching V17's `coefficient_term_counts`. This is a display-only
counting bug in a field that enters no hash and no identity, so it does not
touch the bridge — but it should be repaired before that telemetry is cited
anywhere. It is a distinct defect from the registered `TPhi` one and is not
recorded in the V8 hostile review.

---

## 4. Grade 14: count, nonzeroness, parity, specialization, control

### Independent recomputation

To close gap G1, I wrote a second implementation of the source with its own
polynomial and series arithmetic and ran it on the frozen `tails.json`. It
reproduces the producer's output **monomial for monomial**:

| grade | independent | producer | identical |
|---|---|---|---|
| 10 | 5 | 5 | yes |
| 11 | 18 | 18 | yes |
| 12 | 58 | 58 | yes |
| 14 | **304** | 304 | **yes** |

It also reproduces the contributing-tail census `{10: 73, 11: 73, 12: 73,
14: 83}` exactly, and shows the row vanishes identically in grades 0–9 and has
141 terms at grade 13.

Honest limitation: this is independent *code* for the same *specification*. It
does not and cannot validate the specification — `tails.json`, the weight
vector, the `n0..n3` correction shape, and the `sigma^3`/`sigma^2` shifts are
inherited from frozen upstream artifacts outside this package's scope.

### Count, nonzeroness, parity

The exported coefficient has **304 distinct monomials** — confirmed by parsing,
not by trusting the field. (A naive `+`/`-` scan gives 479 because negative
rationals are parenthesized as `(-3/64)*…`; the honest monomial count is 304.)
It is nonzero. Its `rho`-degree histogram is `{0: 103, 2: 116, 4: 74, 6: 11}` —
**no odd `rho` power occurs**, so it is invariant under `rho -> -rho`. All three
claims confirmed.

### The exact odd-sheet specialization

Under `rho=ell1=rs=a0=c1=c0=e0=0, cs=b, e1=b^2*w, k=(12/5)*w^2`, computed here
independently in exact rationals from the exported `.poly`, the result is
**exactly one monomial**:

```
-(21/320)*b^5*w^2
```

Confirmed. The identity is hand-checkable, because exactly **two** of the 304
monomials survive the substitution:

```
(-3/64)*cs*e1^2   ->  (-3/64)*b*(b^2*w)^2   = -(15/320)*b^5*w^2
(-1/128)*cs^5*k   ->  (-1/128)*b^5*(12/5)w^2 = -( 6/320)*b^5*w^2
                                        sum = -(21/320)*b^5*w^2
```

This also independently reproduces the registered upstream identity
`E_(5,14) = -(21/320)b^5w^2 = -(21/320)b*e1^2 = -(7/256)k0*b^5` recorded in
`AUDIT.md:542`.

**Necessary qualification on "with all live correction terms included."** That
phrase is true in the sense that all 304 monomials — including every A/C
correction (`ac3, ac4, az3, az4, ec3, ec4, ez3, ez4`) and every live load term
(`k1, k2c, k10_3, k10_4`) — are present in the export. It must **not** be read
as a nontrivial cancellation of live corrections against each other. Each of the
other 302 monomials contains at least one of the seven zeroed variables and is
*annihilated*, not cancelled. The registered value therefore constrains 2 of the
304 coefficients and says nothing about the remaining 302. As a check on the
export, the specialization is weak; the strong check is the independent
recomputation above and the grade-10/11/12 bridge.

As a free extra control the producer did not run, I confirmed that under the
same substitution the independently recomputed grades 10, 11, 12 **and 13** all
vanish identically, as the frozen replay's own `total[degree] == 0 for degree <
14` requirement demands.

### The `11/5` negative control is genuine, and its reach is limited

Substituting `k = (11/5)*w^2` gives `-(41/640)*b^5*w^2`, which differs from
`-(21/320) = -(42/640)`. The control is **non-vacuous**: it does not reproduce
the registered coefficient, and the producer's assertion
(`export_row5_g14_v17.py:217-220`) is a real test.

Its discriminating power should be stated exactly. Among the surviving
monomials only `k`-degrees 0 and 1 occur, so with `k = t*w^2` the specialized
coefficient is affine:

```
coefficient(t) = -3/64 - t/128 ,   t = 12/5 -> -21/320 ,   t = 11/5 -> -41/640
```

which vanishes only at `t = -6`. So `11/5` also yields a nonzero `b^5*w^2`. The
control confirms sensitivity of the exact rational value to the normalization;
it does **not** show that a wrong normalization would break nonvanishing, or the
downstream "unit on `D(b*w)`" conclusion. Anyone citing it as evidence for the
latter would be overreading it.

---

## 5. The F65521 lane is an encoding/software control only

Confirmed, and confirmed in the strong direction the claim requires: **no
modular inference enters the characteristic-zero claim.**

In `export_row5_g14_v17.py`, `characteristic` enters in exactly two places:
`coefficient_text` (line 109-114, serialization only) and the `V9[characteristic]`
lookup selecting which frozen reference directory to compare against.
`build_total`, the `rho`-parity test at line 193, the odd-sheet specialization at
lines 196-215, and the negative control at lines 216-220 all run in
`fractions.Fraction` in **both** lanes. The exact-Q identity is established
before, and independently of, any reduction.

I verified that `Tg14_5_p65521.poly` is exactly the term-by-term mod-65521
reduction of `Tg14_5_q.poly`: all 304 monomials present in both, no exact-Q
coefficient vanishing mod 65521.

Hostile qualification: because both lanes recompute with identical `Fraction`
arithmetic, the F65521 lane is **not** an independent arithmetic control on the
producer's own computation. What it genuinely controls is (i) a second Singular
engine invocation in a different characteristic on a different host, and (ii) the
bridge against the *separately produced* V9 mod-65521 shard files. Read as
"independent encoding/software control", the claim is accurate. Read as
"independent arithmetic", it would be an overstatement.

---

## 6. Scope enforcement

The valid result is exactly what the preregistration says and no more: a
**source-honest exact-Q export of one coefficient** (grade 14, fifth row, total
moving-`p` source) **plus an exact low-grade bridge** of grades 10–12 to the
frozen, separately reviewed V9 shards.

It does **not**:

- make the T-cs ideal a unit. The exported object is a 304-term polynomial in 40
  free variables; nothing here inverts, localizes, or saturates anything;
- prove `rho` is a unit. `rho` appears only in even degree, and 103 of the 304
  monomials are `rho`-free — this is a parity statement, not a unit statement;
- form the ordered chart `V(rs/cs) intersect D_+(cs)` or any Rees chart;
- close Gate T, order two, `(8,12)`, maximum twelve, or JC2.

The `-(21/320)*b^5*w^2` value is a property of the *specialized* odd sheet
already registered upstream; V17's contribution is to exhibit the unspecialized
grade-14 coefficient that reduces to it. The unit conclusion on `D(b*w)` lives
on the specialized sheet and is not transported to the total chart by anything
in this package.

The preregistration's own scope paragraph states this correctly, and no entry in
`PROGRESS.md`, `AUDIT.md`, `notes.md`, `COORDINATION.md`, or `APPROACHES.md`
cites V17 yet, so there is no in-tree over-claim to correct.

---

## 7. Review gaps

- No local Singular is used or needed; every identity above was re-derived in
  exact rational arithmetic here. No heavy CAS need arose.
- The specification behind the source — `tails.json`, the `[8,7,6,5,4,3,2 |
  2,6,10]` weight vector, the `n0..n3` correction shape, and the `sigma^3` /
  `sigma^2` shift convention — is inherited from frozen upstream and was **not**
  re-derived from the Faber source in this review. My independent implementation
  validates the producer's arithmetic against that specification, not the
  specification itself.
- G3 and G4 above are unrecoverable from the harvested bytes.

## 8. Recommended repairs (software only, no mathematical change)

1. Make the generated `.sing` actually test controls 4 and 5 — emit the
   substitution and the comparison against `-(21/320)*b^5*w^2`, and the `11/5`
   evaluation, as `if (…) { print("FAIL_…"); quit; }` guards rather than as
   unconditional prints (D1).
2. Fix `validate_coeffexport_v9.py:128` to ignore a leading sign, and re-issue
   the V9 telemetry (D2).
3. Harvest `$remote_job.outer.stdout` / `.outer.stderr`, and record the host
   alias passed to `launch_host.sh` in `launch_registration.txt` (G3, G4).
4. Have the validator recount the terms in the coefficient file rather than
   trusting the compiler's telemetry (G7).
5. Export and bridge grade 13, or state explicitly that it is out of scope (G8).

---

## Verdict

Every element of the audited claim was independently reproduced: the source is
literal and faithfully generalizes the frozen replay; the grade-10/11/12 bridge
to V9 is exact and the registered V8 `TPhi` rebuild defect provably cannot reach
any coefficient used in it; the grade-14 coefficient has exactly 304 monomials,
is nonzero, is even in `rho`, and specializes exactly to `-(21/320)*b^5*w^2`; the
`11/5` control is genuine; and the F65521 lane injects no modular inference into
the characteristic-zero claim. The three recorded defects are an attestation gap
that I closed by independent recomputation, an upstream display-only counting
bug, and ordinary self-attestation custody limits — none of which alters the
exported mathematics. The result remains, as preregistered, a coefficient export
with a low-grade bridge, and closes nothing.

VERDICT: CONFIRMED
