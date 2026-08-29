# Hostile review: actual-total all-row grade-13/14 export V20

Reviewer: Opus 5, independent hostile reviewer.
Date: 2026-08-27.

Producer report reviewed:
`xmodel/max12-812-order2-p0-total-rees-allrows-g13-g14-export-v20-producer-sol-20260827.md`

```text
producer report SHA-256   bce475bb0e040380ac0ab0b186b50b8eaa60d745b0b3376c707eab2797b96c25
```

## Verdict

**CONFIRMED WITH REPAIRS.**

Every numerical assertion in the producer report is exactly true. I reproduced
all fourteen exported coefficients **byte-for-byte in both characteristics**
from a clean-room re-implementation of the arithmetic, re-derived all 21 V9
bridges and the V17 byte bridge, re-derived all seven `+1` controls, and
re-evaluated the section tests with my own parser and my own evaluator. I found
no error in the mathematics and no error in any reported number.

Five repairs are required to the *report and evidence architecture*, none of
which changes a number:

* **R1.** The two AWS jobs are not two computations. Both run the identical
  exact-`Q` `Fraction` arithmetic; the characteristic affects only text
  serialisation, which reference set is compared, and the Singular ring. The
  producer's "In both characteristics it: 1...5" overstates independence.
* **R2.** The four `V20_SECTION_*_NONZERO=0` flags are unguarded `print`
  echoes of a Python number. Singular verifies nothing about the decisive
  section claim.
* **R3.** The "separate restricted-AST replay" asserted in the producer report
  and in `HARVEST_CUSTODY.md` (`V20_INDEPENDENT_Q_TO_F65521_MATCH=14`,
  `V20_INDEPENDENT_QRHO_ZERO_SECTION_CHECKS=56`) has **no script, log, hash or
  artefact anywhere in the frozen or harvested trees**. It must be struck as
  evidence or frozen as a tool.
* **R4.** The headline inference needs grades 0--9, which this case never
  checked. I supplied the missing link (all seven rows vanish identically at
  grades 0--9; row 6 also at 10 and 11), so the inference stands.
* **R5.** Latent, untriggered defect in `coefficient_term_counts`
  (see "Defects").

The strongest justified theorem is stated at the end. It is an
**exported-prefix section statement inside a frozen seven-row, degree-14
truncated model**, not a full formal source arc, and it proves nothing about
Gate T, order two, maximum twelve, or JC2.

## 1. Custody: freeze, results, manifests, evidence

All hashes below are observed locally, not copied from the producer.

`FREEZE.sha256`: 12/12 entries verified `OK` by `shasum -a 256 -c`; self-hash

```text
9c72580ca4be922bcd746e87cb22eba713319813f9f960e8cac4cce8af0220b7   (matches claim)
```

Top-level artefacts, rehashed:

```text
aws_q_v20/RESULT.json               b23ffacd1e4e26abccaeb94a5e83f301cd98a9918a3a84e207fc462a880fe68d  MATCH
aws_p65521_v20/RESULT.json          266130872a10983724a7f9a080b36fef33981ff52192cbdf6c713a75bb7cd07a  MATCH
aws_q_v20/EVIDENCE.sha256           4c945846a5e6cd0a901bd44b21b2800f46ef8a3ea22dab7413f8093253a55ac4  MATCH
aws_p65521_v20/EVIDENCE.sha256      8e6562bd78f372d4cac91ee130d60d70fae04c50d54dd70f8fe49d479c615c3b  MATCH
aws_q_v20/compiled/result.json      b37b95646e5deb381de1edfd3a15a336065855402267c3044f111ca63c3b0f9e  MATCH
aws_p65521_v20/compiled/result.json 3e763bd4ae482494e11ca351b11619aa5d734c4c35e6f55b61146fa7021830ce  MATCH
```

Evidence manifests, with the remote absolute prefixes
`/home/ubuntu/jobs/<tag>/source/cases/.../aws_{q,p65521}/` remapped onto the
local harvested roots `aws_q_v20/` and `aws_p65521_v20/`:

```text
aws_q_v20       entries=31  verified=31  bad=0  missing=0
aws_p65521_v20  entries=31  verified=31  bad=0  missing=0
local files present but absent from the manifest: none (in either tree)
```

So the manifests are both sound **and** complete: 62/62 evidence entries
rehash, and there is no unlisted local file that could carry hidden state.

Internal chain: both `compiled/result.json` carry
`preregistration_sha256 = a854a4e2...`, `replay_sha256 = 2c55284a...`,
`tails_sha256 = d72f774c...`, `v9_manifest_sha256 = 86c535a3.../dc775709...`,
`v17_reference_sha256 = 91d96924.../760d4f3b...`; all five agree with the
locally recomputed values and with `FREEZE.sha256`. Both hosts' on-box
`freeze_check.stdout` show `sha256sum -c FREEZE.sha256` `OK` on all twelve
frozen paths, so the remote inputs were bit-identical to the local ones. The
V9 individual `.poly` files are not in `FREEZE.sha256`, but the exporter
hash-checks each one against the frozen `COEFFICIENTS.json`; I verified those
42 file hashes myself, so the chain closes.

Resources, cross-checked against `HARVEST_CUSTODY.md`: compiler `rc=0`,
33.65 s / 35,068 KiB (Q, `ip-172-30-0-186`, pid 349790) and 33.26 s /
35,244 KiB (F65521, `ip-172-30-0-45`, pid 361495); Singular `rc=0`, 0.01 s /
10,580 KiB and 10,664 KiB; 99--100 % CPU (one core); identical
`source_archive_sha256=60af9593...`. Distinct hosts, distinct pids. The
tarball itself is gone, so `60af9593...` is unverifiable locally; it does not
matter, because the on-host freeze check pins the inputs by content.

## 2. Source reconstruction: code path, conventions, arithmetic

`export_allrows_g13_g14_v20.py` imports `replay_row5_grade14.py` under a
hash gate and uses **only** its sparse primitives. `main()` there is guarded
by `if __name__ == "__main__"`, so the import executes no unpinned work and
trips no AWS gate — the failure mode recorded for `shared_faber_probe` is not
present here.

**Tail census.** `tails.json` (`d72f774c...`, 25,383 bytes) canonicalises to
`6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`, the exact
value the reviewed replay module expects. Independent census:

```text
row   1    2    3    4    5    6    7   total
n    36   54   58   81   89  120  131    569
weight violations 0, zero coefficients 0, load nonlinearity 0, duplicate monomials 0
all tail coefficient denominators are powers of two (65521 inversion always defined)
```

Every entry of row `j` satisfies `m . (8,7,6,5,4,3,2 | 2,6,10) = 12+j`, i.e.
the contracts `13,14,15,16,17,18,19`. `build_row` enforces this per entry and
`fail`s otherwise, and `compile_export` enforces `sorted(tails) == 1..7`, so
no tail can be silently dropped: all 569 are consumed in all seven rows.

**Truncation audit.** `MAX_DEGREE = 14`. I checked every series head for
under-provisioning, since a short name list would silently zero real terms:

```text
c0[d] -> degree d+2   provided d=0..12   need d<=12   exact
r0[d] -> degree d+2   provided d=0..12   need d<=12   exact
az,ac,ez,ec[d] -> degree d+5  provided d=0..9  need d<=9   exact
k10[d] -> degree d+4  provided d=0..10  need d<=10  exact
k6[d]  -> degree d+12 provided d=0..2   need d<=2   exact
k2[d]  -> degree d+20 provided d=0      invisible below 15 (correctly zero)
p[d]   -> provided d=0..14 (p[0] = -2*rho^2)
```

Every head is provisioned exactly to the truncation, none short. `series_mul`
and `series_shift` only ever discard degrees `> 14`, so grades 13 and 14 are
exact, not truncation artefacts.

**Convention drift vs the reviewed replay.** V20's `build_source_series` is
the generic form of the replay's row-5 specialisation, with
`rho=0, ell1=0, rs=0, cs->b, az2->aaa1, ac0=0, ez0=b^2*w, ...`. The
index-to-name maps agree wherever both define a slot. No exponent, sign, or
`1/2`, `1/4` scale differs. The V9 and V17 bridges below pin this.

**Coefficient arithmetic.** `coefficient_text` inverts the denominator mod
65521; all denominators are powers of two, so inversion never fails and no
coefficient can vanish through the denominator. I confirmed separately that
no *numerator* is divisible by 65521 either (see 4).

## 3. Independent replication (clean room)

I re-implemented the whole computation with different data structures
(monomials as index-sorted tuples merged by linear merge; cached series
powers; series as plain lists) and recomputed **all seven rows at all
grades 0--14**, then re-serialised in the producer's normal form.

```text
clean-room replay   15.53 s wall, 35,487,744 B peak RSS  (bounded: timeout 500, ulimit -v)
```

Per-row term counts by grade (mine):

```text
row 1:  g0..g9 = 0,  g10=4,  g11=12, g12=27, g13=50,  g14=85
row 2:  g0..g9 = 0,  g10=5,  g11=14, g12=36, g13=72,  g14=134
row 3:  g0..g9 = 0,  g10=5,  g11=17, g12=47, g13=103, g14=201
row 4:  g0..g9 = 0,  g10=2,  g11=3,  g12=12, g13=30,  g14=71
row 5:  g0..g9 = 0,  g10=5,  g11=18, g12=58, g13=141, g14=304
row 6:  g0..g11= 0,                  g12=9,  g13=32,  g14=90
row 7:  g0..g9 = 0,  g10=5,  g11=18, g12=60, g13=156, g14=364
```

Grade 13 `50, 72, 103, 30, 141, 32, 156` and grade 14
`85, 134, 201, 71, 304, 90, 364` — exactly the producer's counts.

**Byte-level reproduction.** Re-serialising my own polynomials reproduces all
fourteen exported files byte-for-byte in **both** characteristics:

```text
Tg13_1 3bcb17b0eeefacffba3071254d9d65781fa7a65e9fd84540234948a922e1dc70  MATCH (F65521 MATCH)
Tg13_2 00dcbf286799f9c6c6bae8ef884d40c702d5f4b9457c2d271bb3482211916f37  MATCH (F65521 MATCH)
Tg13_3 df5953cab0bb31736b770b7d977897e67aa6ab3224b41b315772c1d87a82ee64  MATCH (F65521 MATCH)
Tg13_4 a4df324fb80d3ad7587848e9bad166d6b65d4e1dfc4e4fc49765d6bcf8af1740  MATCH (F65521 MATCH)
Tg13_5 61fd4b8b8c60cab1497ef26f2bb415c477ecb6cba35a36a7d830b8d839073e46  MATCH (F65521 MATCH)
Tg13_6 1544f802c29de6235764a349bda23b080b4d290b1a9f0ae503f2e3f3ad499345  MATCH (F65521 MATCH)
Tg13_7 7ec47572e483aa2391444aa96db27ce7c4108fc5cd2baf12886575c985c0963f  MATCH (F65521 MATCH)
Tg14_1 8e74526447eed121b8b522340e0eb850f1ed7ac0ee3a908de960b0a0bd198c8b  MATCH (F65521 MATCH)
Tg14_2 d852675256d250fdad784f36deccc58b16f2991da7447ed4235f7f702908657c  MATCH (F65521 MATCH)
Tg14_3 dc70e191282de4325b06fb3657d81c7da5c656b27de544309362c582cd686677  MATCH (F65521 MATCH)
Tg14_4 0ff7496523bd43054ab0f512169d0ef1e1eb2cc239a2b42780be0706c7cace7f  MATCH (F65521 MATCH)
Tg14_5 91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7  MATCH (F65521 MATCH)
Tg14_6 b05ece17b0b0f61bbb324236f51c8ce8cf9caaeaacd15858494b4a1818d296cf  MATCH (F65521 MATCH)
Tg14_7 635c6546d7ade73bd9a300ffc1b11a88668125c141a93cdb1d7e7a28d237a9f8  MATCH (F65521 MATCH)
byte-identical: 14/14 in both characteristics
```

The exported `.poly` texts are also byte-identical to the `Mine_*` right-hand
sides inside both frozen `.sing` control scripts (14/14, both characteristics),
so the file the reviewer reads is the object the engine tested.

## 4. Bridges, established independently

**V9, grades 10--12, all seven rows.** I extracted `Mine_*` and `Ref_*` from
the `.sing` files, parsed both with my own restricted-grammar parser, checked
each `Ref_*` text against the hash-bound V9 `.poly` file, and separately
compared **my own clean-room polynomials** against the V9 files.

```text
Ref_ text == V9 .poly file           21/21 (Q)   21/21 (F65521)
V9 .poly hash == COEFFICIENTS.json   21/21 (Q)   21/21 (F65521)
Mine_ == Ref_ as polynomials         21/21 (Q)   21/21 (F65521)
clean-room recomputation == V9       42/42 comparisons, 0 mismatches
```

Corroborating detail: my exact term counts differ from the V9
`coefficient_term_telemetry` by exactly `+1` on `Tg10_5, Tg11_5, Tg12_4,
Tg12_5` and agree elsewhere — the known sign-count telemetry artefact on
negative-leading polynomials. The hash-bound `.poly` files, which is what the
bridge uses, are correct.

**V17, `Tg14_5`.** The exported `Tg14_5_q.poly` and `Tg14_5_p65521.poly` are
`cmp`-identical to the reviewed V17 files, and my clean-room re-serialisation
also reproduces them byte-for-byte:

```text
V17 Q  91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7   identical
V17 F  760d4f3b155decdf0e847a587254ae701f2b5948d8dd6135c52f5f213c10835b   identical
```

## 5. Exact-Q versus F65521, all fourteen coefficients

For each of the fourteen names I parsed the `Q` file and the `F65521` file
independently, reduced the exact rational coefficients myself, and compared
monomial supports and reduced coefficients:

```text
support and coefficient agreement Q -> F65521 : 14/14
term counts (Q) == term counts (F65521) == declared : 14/14
coefficients that vanish mod 65521 : 0  (no "0*..." term in any F65521 file)
declared coefficient_variable_supports == observed supports : 14/14
exponents occurring : {2,3,4,5,6,8}; no negative exponent, no unsupported token
```

Because no coefficient vanishes mod 65521, the equality of the two term-count
tables is genuine here (see defect **R5** for why it is not guaranteed by
construction).

## 6. All 56 section evaluations, and 364 more

I did **not** trust `RESULT.json` or the `V20_SECTION_*` prints. I evaluated
the sections myself, by full substitution into my own parsed polynomials, and
independently again on my clean-room recomputation:

```text
CS0 : cs=1, every other non-rho source name 0, rho retained
A00 : a0=1,      "                              "
A10 : a1=1,      "                              "
Z00 : every non-rho source name 0,        rho retained
```

Results:

```text
grades 13,14 x 7 rows x 4 sections  =  56 evaluations   all zero in Q[rho]   (the producer's claim)
grades 10..14 x 7 rows x 4 sections = 140 evaluations   all zero in Q[rho]
grades  0..14 x 7 rows x 4 sections = 420 evaluations   all zero in Q[rho]
```

Vanishing is **termwise**: not one monomial of any of the 35 coefficients at
grades 10--14 is supported inside `{rho, cs}`, `{rho, a0}`, `{rho, a1}` or
`{rho}`. There is no cancellation to be suspicious of.

**Parser audit.** My parser is an independent recursive-descent implementation
over the grammar `sum of signed products of powers`, with a strict tokeniser
that rejects any character outside `[A-Za-z0-9_+-*/^() ]`, rejects negative
exponents, rejects division by a non-constant, and (where a ring is known)
rejects any identifier not declared in the ring. No file tripped any of these.
Identifier tokenisation is greedy, so `k`/`k1`/`k10_3` and `k2c`/`k6` cannot
collide; the 41 ring names are pairwise distinct and none shadows a Singular
keyword. The `Q` files use parenthesised fractions, so no `+-` sequence occurs
in any exported `.poly`.

**The test is not vacuous.** The same evaluator, run over every one-name
section, finds six that *are* broken — a positive control the producer did not
supply:

```text
c0 =1  nonzero on Tg10_4 : (3/32)*rho^0
c1 =1  nonzero on Tg10_2 : (3/32),   Tg10_4 : (3/32)*rho^2
e0 =1  nonzero on Tg12_4 : (3/32)
e1 =1  nonzero on Tg12_2 : (3/32),   Tg12_4 : (3/32)*rho^2
ee0=1  nonzero on Tg14_4 : (3/32)
ee1=1  nonzero on Tg14_2 : (3/32),   Tg14_4 : (3/32)*rho^2
```

So the machinery does return nonzero residuals when a section really is
broken, including at grade 14. `cs`, `a0`, `a1` and the origin are genuinely
special among the 40 candidate one-name sections.

**Robustness stratification (new).** Expanding all 569 tails separately and
counting monomials that survive each section *before* summing:

```text
grade   0 : CS0 43  A00 43  A10 43  Z00 43
grade   2 : CS0 94
grade   4 : CS0 84
grade   5 :          A00 29  A10 54
grade   6 : CS0 88
grade   8 : CS0 37
grade  10 : CS0 23  A00 11  A10 20
grade  12 : CS0  4
grade  13 : none
grade  14 : none
(713,962 unit-term monomials inspected; every surviving family sums to exactly zero)
```

This sharpens the result in two directions at once. At grades `<= 12` the four
sections vanish only after exact cancellation among the 569 frozen rational
tail coefficients — a real arithmetic coincidence. At grades **13 and 14 no
single tail expansion produces even one surviving monomial**, so the section
verdict there holds for *arbitrary* tail coefficients and is a combinatorial
consequence of the tail exponent vectors plus the shape of the source series.
That makes the new result more robust than claimed, and simultaneously means
the `+1` coefficient controls could never have broken it.

## 7. Evenness, nonzeroness, counts, and the seven controls

```text
rho exponents occurring across all 35 coefficients : {0,2,4,6,8}   all even
all fourteen new coefficients nonzero               : verified independently
term counts                                         : reproduced exactly (section 3)
```

I reproduced the producer's control-selection rule (first tail of the row
whose unit term has a grade-10/11/12 part nonzero mod 65521) from scratch:

```text
row grade tail monomial                 |delta|  recorded  in Q .sing  in F .sing  nonzero mod p
 1   10   [0,0,0,0,0,1,4,1,0,0]            26       26        yes         yes          yes
 2   12   [0,0,0,0,0,0,4,0,1,0]             1        1        yes         yes          yes
 3   10   [0,0,0,0,0,1,5,1,0,0]            26       26        yes         yes          yes
 4   12   [0,0,0,0,0,0,5,0,1,0]             1        1        yes         yes          yes
 5   10   [0,0,0,0,0,1,6,1,0,0]            26       26        yes         yes          yes
 6   12   [0,0,0,0,0,0,6,0,1,0]             1        1        yes         yes          yes
 7   10   [0,0,0,0,0,1,7,1,0,0]            26       26        yes         yes          yes
```

All seven weights check (`13,14,15,16,17,18,19`), all seven delta texts are
byte-exact in both `.sing` files, and each names a *distinct* coefficient
(`Tg10_1, Tg12_2, Tg10_3, Tg12_4, Tg10_5, Tg12_6, Tg10_7`), all in grades that
have a `Ref_` — so no control references an undefined symbol.

Honest weight of these controls: `Wrong - Ref` reduces to `delta`, so each
control asserts only that a `+1` perturbation of a real contributing tail is
visible in the V9 bridge. Three of the seven (`rows 2,4,6`) are single-term
`+-2^a * k6 * rho^{10,12}` perturbations. **No control perturbs a grade-13 or
grade-14 output.** The prereg asked for exactly this, so it is a scope limit,
not a violation; the gap is closed instead by my byte-level clean-room
reproduction of all fourteen new coefficients.

## 8. Engine audit and local Singular replay

Both control scripts are structurally identical: 185 lines, 1 `ring`, 63
`poly`, 57 well-formed `if (...) { print("FAIL_..."); quit; }` guards, 63
`print`, 1 `quit`, no `qring`, no `random`, no `read(`, `system(`, `execute`,
exactly one `PASS_` token. `63 = 21 Mine + 21 Ref + 14 Mine + 7 Wrong` and
`57 = 21 + 14 + 14 + 1 + 7`.

Six prints are **unguarded** — nothing in Singular verifies them:

```text
V20_QRING_DISABLED=1
V20_SECTION_CS0_NONZERO=0
V20_SECTION_A00_NONZERO=0
V20_SECTION_A10_NONZERO=0
V20_SECTION_Z00_NONZERO=0
PASS_TOTAL_REES_ALLROWS_G13_G14_EXPORT_V20
```

`validate_export_v20.py` then *derives* its required `V20_SECTION_*` tokens
from the same compiler JSON, so that loop is circular. This is **R2**: the
decisive claim of the case has no engine-side check at all. It is repaired
only by section 6 of this review.

Singular is installed locally, so I replayed both frozen scripts under
`timeout 120` / `ulimit -v`:

```text
q.sing  rc=0  stdout sha256 9765b765915625f637d0279ccdca0a67bdf7e3ef100af4f9bf06a7e8045ed632  stderr 0 bytes
p.sing  rc=0  stdout sha256 9765b765915625f637d0279ccdca0a67bdf7e3ef100af4f9bf06a7e8045ed632  stderr 0 bytes
AWS-recorded stdout sha256                9765b765915625f637d0279ccdca0a67bdf7e3ef100af4f9bf06a7e8045ed632
```

Byte-identical to the AWS record on both hosts, no Singular diagnostics. The
two jobs share a stdout hash because the flag strings do not depend on the
characteristic; that is expected, not a duplication.

I also checked the char-0 integer-division hazard that would have silently
zeroed every rational coefficient: `poly f=(3/4)*x; poly g=3/4*x;` both give
`3/4x` and `f-g==0`. Independently, the run cannot have been affected —
`Tg13_4` has all thirty coefficients fractional, so a zeroing parse would have
tripped `FAIL_NONZERO_Tg13_4`.

Finally, five mutation probes confirm the guards that do exist actually fire
and abort before `PASS`:

```text
perturb Mine_Tg10_1  -> FAIL_V9_BRIDGE_Tg10_1
zero    Mine_Tg13_1  -> FAIL_NONZERO_Tg13_1
rho-odd Mine_Tg13_1  -> FAIL_RHO_PARITY_Tg13_1
perturb Mine_Tg14_5  -> FAIL_V17_BRIDGE_Tg14_5
neutral Wrong_Tg12_4 -> FAIL_SOURCE_SENSITIVITY_Tg12_4
```

## Defects and their mathematical effect

**D1 (R1) — "both characteristics" is one computation.** `load_replay()` takes
no characteristic; every series and polynomial is exact `Fraction` arithmetic.
Confirmed structurally by diffing the two `compiled/result.json`: only
`characteristic`, the lane tag, the control-script path/hash, and the two
reference hashes differ. `coefficient_term_counts`,
`contributing_tail_counts`, `coefficient_variable_supports`,
`source_sensitivity_controls` and `section_nonzero_residuals_exact_qrho` are
*identical*. **Effect:** none on correctness; the genuine mod-65521 content is
the comparison of the reduction against the separately produced V9/V17
mod-65521 artefacts, which does hold. The producer's phrasing should say so.

**D2 (R2) — the decisive test is unverified by the engine.** See section 8.
**Effect:** none on the answer (independently re-derived here); the case as
shipped would have passed unchanged even if `poly_substitute` were broken.

**D3 (R3) — an unevidenced custody claim.** The "separate restricted-AST
replay" producing `V20_INDEPENDENT_Q_TO_F65521_MATCH=14` and
`V20_INDEPENDENT_QRHO_ZERO_SECTION_CHECKS=56` leaves no trace: no file in
`FREEZE.sha256`, none in either `EVIDENCE.sha256`, none on disk.
**Effect:** those two counters carry no evidentiary weight. Their content is
now separately established by sections 5 and 6 of this review.

**D4 (R4) — grades 0--9 were never checked.** "The first possible
section-breaking source grade is at least 15" requires *every* grade below 15
to be non-breaking, but this case tests only 10--14 (V9 bridge plus new
export). **Effect:** an evidence gap in the inference, now closed: I computed
grades 0--9 for all seven rows and they are **identically zero** (row 6 is
also zero at grades 10 and 11). The inference stands.

**D5 (R5) — latent term-count defect.** `coefficient_counts[name] =
len(polynomial)` is taken on the exact-`Q` polynomial regardless of
characteristic. In the F65521 `RESULT.json` this is therefore the `Q` term
count, not the mod-`p` support size, and `validate_export_v20.py` derives its
required `NONZERO`/`ZERO` token from it. Had any numerator been divisible by
65521, the `.poly` file would have carried a `0*...` term while the reported
count overstated the mod-`p` support, and only *total* vanishing would have
been caught by the Singular guard. **Effect: none here** — I verified that no
coefficient of any of the fourteen vanishes mod 65521, and no `0*` term occurs
in any F65521 file. The defect is untriggered but should be fixed before the
prime is changed.

**Not a defect, but a limit worth recording.** The seven `+1` controls are
controls on the V9 bridge only, and (section 6) at grades 13--14 the section
verdict does not depend on tail coefficients at all, so no coefficient
perturbation could ever have tested it.

## Judgement on the inference

The producer's inference is **valid**, with the D4 repair, inside its model.
Precisely:

*If* the seven rows of `tails.json` are the complete actual-total source rows,
*and* `build_source_series` is the correct generic emitter, then every source
row at every grade `<= 14` vanishes at each of `CS0`, `A00`, `A10`, `Z00` with
`rho` free. Hence the ideal generated by the source rows through grade 14 is
contained in the maximal ideal of each of those four points; it is not the
unit ideal in any localisation where the point is visible; and a stage-two
solver fed only rows through grade 14 would be asked to certify emptiness
statements that are false at those points. Consequently the first grade at
which this source could break any of the four sections is `>= 15`. Nothing
here says grade 15 does break one.

Dependencies and scope limits, stated exactly:

1. **Tail completeness is inherited, not proved.** That these 569 tails are
   the whole emitter for rows 1--7 comes from the `u2_62_strict_rees` case.
   V20 verifies only the weight contracts and that all 569 are consumed.
2. **External anchoring is partial.** Every *variable* occurring at grades
   13--14 also occurs in a V9- or V17-anchored coefficient, but 1,036 of the
   1,833 grade-13/14 monomials have a variable-set occurring in no anchored
   coefficient. A model error confined to degrees 13--14 and invisible in row
   5 would not be caught by any bridge. It is excluded only by shared code
   path plus my byte-level clean-room re-derivation of the exporter's own
   definition — which certifies the *implementation*, not the *choice* of the
   source model.
3. **Grade 15 is not merely untested, it is out of model.** `MAX_DEGREE = 14`
   is baked into the frozen replay module; any grade-15 work needs a new,
   separately reviewed module. Consistently, only jet indices `<= 4` (plus
   `k6`, which appears solely in the control deltas) occur at all in the
   41-variable ring: `ell5..ell14`, `cs5..cs12`, `rs5..rs12`, `az5..az9`,
   `ac/ez/ec5..9`, `k10_5..k10_10`, `k6_1`, `k6_2`, `k2` are invisible below
   grade 15.
4. **This is an exported-prefix section, not a formal source arc.** The four
   assignments are points in the coefficient space of a degree-14 truncated
   jet. Nothing shows they extend to full formal arcs: extension would require
   every grade `>= 15`, the unwritten Rees equations, additional genuine
   localizers, even-sheet rows, Keep remainders, and full source coverage,
   none of which is touched.
5. **A point test, not ideal membership.** As the prereg insists, vanishing at
   a point is not radical membership and does not empty or fill a Rees chart
   as a scheme. The identification of `CS0`, `A00`, `A10`, `Z00` with points
   of the two standard `J2` charts, the terminal receiver and the off-family
   point is upstream geometry, not re-derivable from this case's artefacts.
6. `CS0` sets `k=0`, so it lies off the unit-`k10` family on `D(k)` and does
   not bear on the promoted direct `T-cs` theorem. The producer's firewall on
   Gate T, order two, maximum twelve and JC2 is accurate and I endorse it.

### Strongest justified theorem

Let `T` be the frozen 569-entry canonical tail table
(`sha256 d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`,
seven rows, row `j` of tail-weight `12+j` for the weight vector
`(8,7,6,5,4,3,2 | 2,6,10)`), and let `S` be the generic total moving-`p`
source series over `Q` truncated at degree 14 as defined by
`build_source_series` in `export_allrows_g13_g14_v20.py`
(`5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587`), built
on the reviewed sparse primitives of
`replay_row5_grade14.py`
(`2c55284a3fd36e5d9eda26f759353f27d07163d87c30c9f958e84fb32b031258`). Write
`T(d,j)` for the degree-`d` coefficient of row `j`. Then, verified exactly and
independently:

1. `T(d,j) = 0` for all `0 <= d <= 9` and all `j`; also `T(10,6) = T(11,6) = 0`.
2. The 21 polynomials `T(d,j)`, `10 <= d <= 12`, equal the reviewed V9 exports
   over `Q` and over `F_65521`; `T(14,5)` equals the reviewed V17 export
   byte-for-byte in both characteristics.
3. The fourteen `T(13,j)`, `T(14,j)` are exactly the fourteen exported files
   with the hashes and term counts listed in section 3; each is nonzero, even
   in `rho` (exponents in `{0,2,4,6,8}`), and no coefficient vanishes mod
   65521, so the `Q` and `F_65521` supports coincide.
4. For every `0 <= d <= 14`, every `j`, and each of `CS0` (`cs=1`), `A00`
   (`a0=1`), `A10` (`a1=1`), `Z00` (all zero), substituting `1` for the named
   source variable, `0` for every other non-`rho` source variable, and keeping
   `rho` an indeterminate, yields the zero polynomial of `Q[rho]`. All 420
   such evaluations vanish, and vanish termwise.
5. At `d = 13` and `d = 14` no single one of the 569 tail expansions
   contributes even one monomial surviving any of the four sections; hence
   statement 4 at those two grades holds for **arbitrary** rational tail
   coefficients. At `d <= 12` it holds only after exact cancellation among the
   frozen coefficients.
6. The evaluator is discriminating: among the 40 candidate one-name sections,
   `c0`, `c1`, `e0`, `e1`, `ee0`, `ee1` each yield a nonzero `Q[rho]`
   residual (`3/32 * rho^0` or `3/32 * rho^2`), at grades 10, 12 and 14
   respectively.

**Corollary.** Within this frozen model, the four assignments `CS0`, `A00`,
`A10`, `Z00` (with `rho` free) are common zeros of the entire actual-total
source through grade 14. The first grade at which this source could break any
of those four sections is therefore at least 15. This is an exported-prefix
statement about a degree-14 truncation of seven rows; it is not a statement
about full formal source arcs, about grades `>= 15`, about the unwritten Rees
equations, additional localizers, even-sheet rows, Keep remainders, full
source coverage, Gate T, order two, maximum twelve, or JC2.

## Reproduction

Read-only shell work only. No AWS access, no `jc2-lean` access, no campaign
file edited other than this report. All local scratch under `/tmp/v20rev/`.

```text
shasum -a 256 -c cases/.../FREEZE.sha256                      12/12 OK
evidence rehash with remote->local path remap                 62/62 OK, 0 unlisted files
clean-room replay (all rows, grades 0..14)  timeout 500, ulimit -v 6 GiB  15.53 s / 35.5 MB
tail-expansion survivor census              timeout 500, ulimit -v 6 GiB  14.60 s / 25.1 MB
local Singular replay of both frozen .sing  timeout 120, ulimit -v 4 GiB  stdout 9765b765... x2
five mutation probes of the .sing guards    all five FAIL_ tokens fired before PASS
```

Producer report reviewed:

```text
xmodel/max12-812-order2-p0-total-rees-allrows-g13-g14-export-v20-producer-sol-20260827.md
SHA-256  bce475bb0e040380ac0ab0b186b50b8eaa60d745b0b3376c707eab2797b96c25
```
