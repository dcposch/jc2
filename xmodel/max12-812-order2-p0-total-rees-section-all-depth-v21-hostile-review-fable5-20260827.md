# Hostile review (Fable 5): actual-total named sections at all coefficient grades V21

Date: 2026-08-27
Reviewer: Fable 5, acting as equal independent hostile reviewer.
Producer claim under review:
`xmodel/max12-812-order2-p0-total-rees-section-all-depth-v21-producer-sol-20260827.md`
(SHA-256 `172755de690977d90448a6b6c6ac0abf0d9437dfecb46983638919eb241c7ffe`, observed and matching).

## Verdict: CONFIRMED

Every frozen hash matches, the four specializations follow exactly from the
literal V20 emitter formulas by my own hand derivation, my independently
written untruncated evaluator over `Q[sigma,rho]` reproduces the complete
nonzero output on all 569 tails, the frozen replay regenerates `RESULT.json`
byte-for-byte, the V20 grade-13/14 bridges and both modular reductions are
verified (the bridged content independently reproven, not merely pinned),
and the exhaustiveness of "all coefficient grades" holds for the literal
finite-tail source with no hidden truncation.  The producer's scope firewall
is accurate and necessary.  No mathematical defect found.

## 1. Custody: every hash re-verified

All observed with `shasum -a 256` on 2026-08-27:

| artifact | observed SHA-256 | pinned where | match |
|---|---|---|---|
| producer report | `172755de690977d90448a6b6c6ac0abf0d9437dfecb46983638919eb241c7ffe` | review assignment | yes |
| `FREEZE.sha256` | `403451572df3dd1929d873f63a6fe22972e2127c24a24fa5b8ccfbdf18bea38b` | producer report | yes |
| `PREREGISTRATION.md` | `8b0dd8cf035c870b9b5577e187e7b86110d08db41b3241c50b4db3ab0bdeef1b` | FREEZE.sha256 | yes |
| `replay_section_all_depth_v21.py` | `0807540484b93ee12b6d6b7ea2b90a7e80418fd29fa7633bc9a8ab3485269f14` | FREEZE.sha256 | yes |
| `RESULT.json` | `f702630d71ea4b1168ab993848dc334e67fac4f436273e27fc5fb93637bd34ff` | producer report | yes |
| `tails.json` (569 tails) | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | report, prereg, replay | yes |
| V20 emitter `export_allrows_g13_g14_v20.py` | `5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587` | report, prereg, replay | yes |
| V20 `aws_q_v20/RESULT.json` | `b23ffacd1e4e26abccaeb94a5e83f301cd98a9918a3a84e207fc462a880fe68d` | prereg, replay | yes |
| V20 `aws_p65521_v20/RESULT.json` | `266130872a10983724a7f9a080b36fef33981ff52192cbdf6c713a75bb7cd07a` | prereg, replay | yes |

I additionally reran the frozen replay to a scratch output: it printed all
eight PASS banners, ran in 0.07 s locally (consistent with the claimed
0.06 s / 13 MB), and its output is **byte-identical** to the frozen
`RESULT.json` (same SHA-256 `f702630d…`).  So `RESULT.json` is the honest
deterministic output of the frozen program.  This rerun is custody evidence
only; my verification below does not rely on the V21 program or on its
frozen expected-answer assertion.

The frozen sparse-replay module imported by the V20 emitter
(`replay_row5_grade14.py`) hashes to its pin
`2c55284a3fd36e5d9eda26f759353f27d07163d87c30c9f958e84fb32b031258`; I read
its primitives and confirmed `named_series` places name *i* at sigma-degree
*i*, `series_shift(s,n)` multiplies by `sigma^n`, and `MAX_DEGREE = 14`
(truncated convolution, exact per retained grade).  So V20 could never see
grade 15; V21's untruncated ring is the correct instrument for the claim.

## 2. Independent derivation of the four specializations

From the literal formulas in the hash-pinned V20 emitter
(`build_source_series`, lines 147–180), by hand, before reading V21's
`section_coefficients`:

- `p = -2 rho^2 + sum_{d>=1} 2 ell_d sigma^d`; `c = sigma^2(cs + cs1 sigma + …)`;
  `r = (p^2 + sigma^2(rs + …))/4`;
- `az = a1 + aa1 sigma + aaa1 sigma^2 + az3 sigma^3 + …`, `ac = a0 + aa0 sigma + …`,
  `ez = c1 + e1 sigma + …`, `ec = c0 + e0 sigma + …`;
- `n3 = sigma^3 az`, `n2 = sigma^3 ac`, `n1 = sigma^3 (p·az + ez)/2`,
  `n0 = sigma^3 (p·ac + ec)/2` — the shift-by-3;
- row-coefficient tuple `C6..C0 = (2p, 2c, p^2+2r, 2pc + sigma^2 n3,
  c^2+2pr + sigma^2 n2, 2cr + sigma^2 n1, r^2 + sigma^2 n0)` — the further
  shift-by-2, so the `a0`/`a1` perturbations land at `sigma^{3+2} = sigma^5`.

Each named assignment sets every source name except `rho` and the one
distinguished name to zero.  Name census (grep-verified in the emitter):
`cs` occurs only as the degree-0 head of `c0`; `a0` only as the head of
`ac`; `a1` only as the head of `az`; the `ez`/`ec` name lists
(`c1,e1,ee1,ez*` and `c0,e0,ee0,ec*`) contain none of `cs,a0,a1,rho` and
therefore vanish under **all four** assignments (this justifies V21's
`n1`/`n0` formulas dropping `ez`/`ec` — exact, though silently done).
Hence `p → -2rho^2`, `r → p^2/4 = rho^4`, and:

| pos (weight) | Z00 | CS0 (`cs=1`) | A00 (`a0=1`) | A10 (`a1=1`) |
|---|---|---|---|---|
| C0 (8) | `rho^8` | `rho^8` | `rho^8 − rho^2 sigma^5` | `rho^8` |
| C1 (7) | 0 | `2 rho^4 sigma^2` | 0 | `−rho^2 sigma^5` |
| C2 (6) | `−4 rho^6` | `−4 rho^6 + sigma^4` | `−4 rho^6 + sigma^5` | `−4 rho^6` |
| C3 (5) | 0 | `−4 rho^2 sigma^2` | 0 | `sigma^5` |
| C4 (4) | `6 rho^4` | `6 rho^4` | `6 rho^4` | `6 rho^4` |
| C5 (3) | 0 | `2 sigma^2` | 0 | 0 |
| C6 (2) | `−4 rho^2` | `−4 rho^2` | `−4 rho^2` | `−4 rho^2` |

This table agrees exactly with V21's `section_coefficients` (checked
line-by-line after deriving it).  Coefficient-index ordering: both V20
(`build_row`) and V21 pair tail exponent slot *i* (i = 0..6) with the
key-*i* series of the same dict, weights `[8,7,6,5,4,3,2]`; the pairing is
identical, and the weight contract `sum(exp·weight) = 12 + row` was
re-verified by me for all 569 tails.  Rho powers: only `p` and `r` carry
`rho` (`rho^2` and `rho^4`), entering the odd corrections as
`(1/2)p·az = −rho^2` and `(1/2)p·ac = −rho^2` — matching the table.

**Loads.**  The three load series use names
`{k,k1,k2c,k10_3..k10_10} ∪ {k6,k6_1,k6_2} ∪ {k2}`, disjoint from
`{cs,a0,a1,rho}`.  Under every one of the four assignments each load series
is therefore **identically zero** — not low-order zero — so all 289
load-containing tails (of 569; load exponents verified in `{0,1}` for every
tail, matching V20's load-nonlinearity contract) contribute exactly zero at
every sigma grade.  V21's skip of these terms is exact, not a truncation.

## 3. Independent untruncated evaluation of all 569 tails

I wrote a separate evaluator from scratch (staged at
`/tmp/fable5_v21_hostile_check.py`, not in the campaign tree) with
deliberately different internals: my own specialization table above (not
V21's `p/r/c/n` construction), monomial keys transposed to
`(rho_exp, sigma_exp)`, naive repeated multiplication instead of binary
powering, plus a second, polynomial-free evaluation path computing each
row as an exact rational number at 10 integer points `(sigma,rho)` and
comparing the direct tail sum against both my symbolic totals and the
claimed closed forms.  Runtime 0.17 s.

Observed complete nonzero output over all four sections, seven rows, all
sigma grades:

```text
CS0:  every row identically 0 in Q[sigma,rho]
Z00:  every row identically 0 in Q[sigma,rho]
A00:  row 6 = -(1/16) sigma^15;                    rows 1,2,3,4,5,7 = 0
A10:  row 3 = -(1/16) sigma^15
      row 5 = -(3/32) sigma^15 rho^2
      row 7 = -(3/128) sigma^15 rho^4;             rows 1,2,4,6 = 0
```

This is exactly the frozen expected answer, i.e. `Tg15_6(A00) = −1/16` and
`Tg15_3(A10) = −1/16`, `Tg15_5(A10) = −(3/32)rho^2`,
`Tg15_7(A10) = −(3/128)rho^4`, all other row coefficients zero on `A00` and
`A10`, and all seven full row series identically zero on `CS0` and `Z00`.
My per-tail contribution records also match the frozen
`nonzero_tail_contributions` in `RESULT.json` term-for-term (17 tails for
A00 row 6; 12, 17, 25 tails for A10 rows 3, 5, 7).  The ten-point numeric
path agreed with both on all 4×7×10 evaluations.

Hand reductions (independent of both programs):

- **A00 row 6, the sigma^15 witness.**  Homogeneity: under A00 every entry
  is homogeneous with weights `w(rho)=1, w(sigma)=6/5`, so row 6 (weight 18)
  lives on `rho^18, rho^12 sigma^5, rho^6 sigma^10, sigma^15`.  A pure
  `sigma^15` needs three `rho^0 sigma^5` factors, available only from C2,
  and `3·6 = 18` uses the whole weight: the unique candidate tail is
  `[0,0,3,0,0,0,0,0,0,0]`, present with coefficient `−1/16`.  Expanding
  `(−4rho^6 + sigma^5)^3 = −64rho^18 + 48rho^12 sigma^5 − 12rho^6 sigma^10
  + sigma^15` and scaling by `−1/16` gives parts
  `(4, −3, 3/4, −1/16)` — matching the frozen record — so the
  `sigma^15` total is `−1/16`.
- **Cancellation of the other A00 row-6 grades**, summed by hand from the
  17 frozen contributions: `rho^18` parts
  `140 −630 +999 −1269/2 +243/2 +138 −396 +621/2 −81/2 +42 −54 +4 −9 +45/2
  −27/2 −9/2 +9/2 = 234 − 234 = 0`; `rho^12 sigma^5` parts sum to
  `111 − 87/2 − 135/2 = 0`; `rho^6 sigma^10` parts sum to
  `(21−27−9+9)/8 + 3/4 = 0`.  (The `rho^18` cancellation is precisely the
  Z00 row-6 zero.)
- **A10 rows 3/5/7 sigma^15 sums.**  Row 3: sole `sigma^15` source is
  `C3^3` from tail `[0,0,0,3,…]` with `−1/16`.  Row 5:
  `(9/128)·C3^3·C6 + (−3/16)·C1·C3^2 = −9/32 + 3/16 = −3/32` times
  `rho^2 sigma^15`.  Row 7:
  `(−45/2048)·C3^3·C6^2 + (3/128)·C3^3·C4 + (9/128)·C1·C3^2·C6 +
  (−3/32)·C1^2·C3 = (−45 + 18 + 36 − 12)/128 = −3/128` times
  `rho^4 sigma^15`.  All match.

**The zeros are nontrivial cancellations, not vacuous.**  Census of tails
whose individual contribution is nonzero (with the sigma grades they touch):

```text
Z00:  rows 1,3,5,7: 0 tails (parity: odd row weight forces an odd-weight
      position 1/3/5, all zero under Z00);  rows 2/4/6: 11/15/17 pure-rho
      contributions cancelling to 0.
CS0:  rows 1..7: 19/27/30/40/44/57/63 tails, grades up to {0,2,…,12},
      all cancelling to 0 in every grade.
A00:  odd rows: 0 tails (same parity argument); rows 2/4/6: 11/15/17 tails
      at grades {0,5,10(,15)}, everything cancelling except sigma^15 in row 6.
A10:  all rows contribute (8..27 tails); everything cancels except
      sigma^15 in rows 3, 5, 7.
```

## 4. All coefficient grades: no hidden truncation

- **Finiteness is structural, not imposed.**  After any of the four
  assignments each C-entry is a polynomial with sigma-degree ≤ 5, each tail
  is a finite product, and each row total is a polynomial; my evaluator
  (like V21's) has no degree cap anywhere.  "All grades" is therefore a
  complete finite statement about the specialized literal source.
- **Upper grades:** per-tail grade support never exceeds 15 on A00/A10
  (homogeneity caps the number of `sigma^5` factors at three) and never
  exceeds 12 on CS0; so nothing exists above grade 15 either — the
  displayed output is complete in both directions.
- **Omitted higher jet variables:** the frozen emitter's name lists are
  finite and its series stop at `MAX_DEGREE = 14`; but any deeper jet name
  in an extended model would be "another source name" and hence zeroed by
  the very definition of the four assignments.  The four specializations
  are invariant under jet-depth extension of the emitter; only the *scope*
  (literal frozen source) is affected, and the firewall states this.
- **Delayed loads:** loads enter at sigma-shifts 4, 12, 20; a shift-20 load
  is invisible to V20's grade-≤14 window but would act at grade ≥ 20.  It
  cannot survive here: every load name is zeroed under all four assignments,
  so load series are identically zero at every grade.  No named assignment
  sets any load name to 1 (`CS0` sets `cs`, which is not a load name).
- **No tail containing a load can survive any named assignment** (name
  disjointness above), and dropping exact zeros is exact, so the 289
  skipped tails cannot bias the A00/A10 values either.

## 5. V20 grade-13/14 bridges and modular reductions

- Both pinned V20 result files hash-match and carry exactly the fields the
  bridge requires: `status = PASS-TOTAL-REES-ALLROWS-G13-G14-EXPORT-V20`,
  `characteristic ∈ {0, 65521}`, and
  `section_nonzero_residuals_exact_qrho = {"A00":{},"A10":{},"CS0":{},"Z00":{}}`.
- The bridged content is **independently reproven**, not just pinned:
  the V20 grade-g section residual is mathematically the `sigma^g`
  coefficient of my specialized total (specialization by degree-0 constants
  commutes with the sigma-grading), and my untruncated totals contain no
  `sigma^13` or `sigma^14` monomial in any section or row.  V20's four
  empty dictionaries at grades 13/14 are exactly what my computation
  forces.  (The unspecialized V20 exports have their own AWS custody chain
  and are not re-derived here; V21 uses only the four empty section dicts.)
- Modular reductions recomputed independently for both primes and matching
  the frozen `modular_reductions`, each residue also checked by hand:
  `−1/16 ≡ 22002 (mod 32003)` since `22002·16 = 352032 ≡ −1`;
  `−1/16 ≡ 4095 (mod 65521)` since `4095·16 = 65520 ≡ −1`;
  `−3/32 ≡ 1000`, `−3/128 ≡ 250 (mod 32003)` since `32000 ≡ −3`;
  `−3/32 ≡ 38903`, `−3/128 ≡ 26106 (mod 65521)` since
  `38903·32 = 1244896 ≡ −3` and `26106·128 = 3341568 ≡ −3`.
  All displayed coefficients are dyadic, hence nonzero modulo both odd
  control primes, as required.

## 6. Structural reading (interpretation, not load-bearing)

With `Q(x) = x^4 + p x^2 + c x + r`, the C-tuple is the coefficient list of
`Q^2` plus the shifted `n3..n0` corrections.  Under Z00 and CS0 the
specialized datum stays a perfect square (`Q = (x^2−rho^2)^2`, resp.
`(x^2−rho^2)^2 + sigma^2 x`), and every row functional vanishes
identically; A00 adds `sigma^5 (x^2−rho^2)` and A10 adds
`sigma^5 x(x^2−rho^2)`, breaking squareness, and the rows first detect
these at cubic order `(sigma^5)^3 = sigma^15`, the linear and quadratic
orders cancelling (verified).  This is consistent with the rows being
obstructions vanishing on the perfect-square locus, which makes the
all-depth CS0/Z00 zeros structurally expected rather than numerically
accidental — but I have not re-derived the tails' defining property, and
nothing in my verdict depends on this reading.

## 7. Scope judgment (confirming the firewall)

- **Grade 15 kills only the two displayed horizontal points.**  `A00` and
  `A10` are single named prefix sections (one coordinate set to 1, all
  other deformation names 0, `rho` free).  The values `−1/16 · sigma^15`
  are constants in `rho`, so the kills are rho-uniform — no localization
  needed — but they say nothing about sections with other names turned on.
  Nothing here makes `a0` or `a1` radical or empties either `J2` Rees chart.
- **All-depth persistence of CS0/Z00 is exactly what it says:** no
  coefficient grade of the *literal frozen 569-tail source* can kill
  `CS0` or `Z00` under the named assignments; deeper exports of this same
  source family are provably futile for those two residuals.  It is not a
  formal-arc statement, not chart nonemptiness, and not resistance to
  Rees/chart equations, bilinears, routing, or other source families —
  none of which are in the 569-tail source.  `CS0` remains outside the
  named unit-`k10` family on `D(k)`.  Completeness of the 569-tail census
  itself is inherited from the upstream frozen u2_62 strict-Rees compile
  (hash-verified here, not re-derived).
- Nothing here proves Gate T, order two, maximum twelve, or JC2.  The
  producer's firewall states all of this; it is accurate.

## 8. Defect log

No mathematical defect.  Minor observations, none affecting the verdict:

1. V21's `section_coefficients` drops the `ez`/`ec` summands of `n1`/`n0`
   relative to the emitter formulas without comment.  This is exact — those
   name lists are zeroed under all four assignments — but the justification
   lives only in this review and in the name census, not in the code.
2. `FREEZE.sha256` covers only the preregistration and the replay script;
   `RESULT.json` and the report are pinned via the producer report (normal
   campaign convention; verified coherent here, including a byte-exact
   regeneration of `RESULT.json`).
3. The V21 bridge check binds to the top-level V20 status string
   (`…-V20`, not the compiler-level `…-V20-COMPILER`); the pinned files
   carry the former, so the check binds as intended.

## 9. Strongest justified statement

In untruncated `Q[sigma,rho]`, the specialization of the frozen 569
canonical-tail actual-total source (V20 emitter
`5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587`, tails
`d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`) at the
four named assignments is, exhaustively over all rows and all sigma grades:
identically zero in all seven rows for `CS0` and `Z00`; exactly
`−(1/16)sigma^15` in row 6 and zero elsewhere for `A00`; and exactly
`−(1/16)sigma^15`, `−(3/32)rho^2 sigma^15`, `−(3/128)rho^4 sigma^15` in
rows 3, 5, 7 and zero elsewhere for `A10`.  Consequently grade 15 is the
first and only nonzero source grade on either named `J2` prefix point, the
two displayed horizontal witnesses are killed rho-uniformly, and no
coefficient grade of this literal finite-tail source can decide `CS0` or
`Z00`.  Scope strictly as in the firewall above.

## 10. Producer report hash

`172755de690977d90448a6b6c6ac0abf0d9437dfecb46983638919eb241c7ffe`
(observed on the reviewed file; equals the assignment's expected value).
