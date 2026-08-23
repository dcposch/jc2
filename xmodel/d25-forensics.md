# D25 forensic adjudication: Ox calibration run vs the promoted certificate chain

[2026-08-22. FORENSIC, fail-closed. Adjudicates the direct conflict between
`xmodel/ox-calibration.md` + `cases/ox_calibration.py` (verdict: REFUTED, "localized
raw parked systems EMPTY (dim -1)") and the promoted AUDIT.md entry "D25 FAMILY
NONEMPTINESS + CELL STRUCTURE (2026-08-21)" (chain: `xmodel/sol-ideas-0821.md` items
1-2 -> `cases/d25_certificate_replay.json` + SHEET6-DIRECTIONB.md 9.S2 ->
`xmodel/grok-d25cert-review.md`). All numbers below were recomputed with FRESH local
Python (own parser, own exact mod-p arithmetic; scratch scripts `forensic1.py`,
`forensic2.py`, `singular_dim.py`) -- no reuse of Ox's, Sol's, or the replay's code
except where explicitly quoted to demonstrate a bug in it. No git, no network.]

## VERDICT: OX-MISCALIBRATED (completely). The promoted certificate stands unchanged.

Every mathematical finding in `xmodel/ox-calibration.md` that contradicts the
promoted chain is an artifact of three identifiable defects in
`cases/ox_calibration.py`, plus one misreading. Nothing in the promoted AUDIT.md
entry needs retraction or rescoping. Details, in the order of the adjudication
protocol:

---

## 1. FILE IDENTITY: Ox parsed EXACTLY the files the replay certified

`cases/ox_calibration.py` `main()` reads `cases/d25fam_p105337_a00mm.ms` and
`cases/d25fam_p105673_a00mm.ms` (assembly per-fiber emissions, 34 rows x 28 vars).
Fresh sha256 (2026-08-22) vs the hashes recorded in
`cases/d25_certificate_replay.json` `sha256`:

| file | fresh sha256 | replay-recorded | match |
|---|---|---|---|
| d25fam_p105337_a00mm.ms | `0be359aea2f8f496caa9526f5309c6db9f3daa8992261b57d3d7eaa1db747b1a` | same | YES |
| d25fam_p105673_a00mm.ms | `68e901a4382fce39e92751704bb66ba46a31c672d74bbdd7492d3cdc3fa3b178` | same | YES |
| d25fam_p105337.ms (union) | `49dc1f9dad0e68b8d166a78753e77d8637d22e1897cbdae95e82bcd4b2718dfd` | same | YES |
| d25fam_p105673.ms (union) | `c01f2d3d0cde6c5e4a09e8b623c7d19bf7612caa9d5d27540cf51fc95d3a4a15` | same | YES |
| d25fam_p105337_a00pp.ms | `ef6db7e9ad36666537475fabf8238887de0c7e6d8f02c9381eaa7c810cbe4fe2` | same | YES |
| d25fam_p105673_a00pp.ms | `43b81c4ea5f77a5d0d32f433a23e867e9ef4c7228f5d6e7624f43561aa976175` | same | YES |

No local copies of the abandoned 514-row `d25pf` race emissions exist anywhere in
the repo (verified by full-tree find; the only non-d25fam `.ms` files are the old
`systems/open_8_28_*` families). Ox's parser reporting 34 x 28 is consistent:
those ARE the assembly emissions. **File identity is NOT the divergence.** Both
computations ran on byte-identical inputs; the divergence is 100% in Ox's
processing of them.

## 2. THE MINOR: fresh computation gives EXACTLY the certificate's value; Ox's 0 is an extraction artifact

Residual rows are rows 29-33 (0-based; 5 pairwise-DISTINCT rows of 148/148/148/148/144
terms -- see section 4 for Ox's "identical" claim). With a fresh parser and fresh
polynomial arithmetic, the coefficient polynomials of x33 and x38 in R1 = row 29 and
R2 = row 30 of the exact files above are single Laurent monomials:

```text
p=105337:  coeff(R1,x33) = 97484*uW1^2   coeff(R1,x38) = 78826*uW2^2
           coeff(R2,x33) = 12718*uW1^2   coeff(R2,x38) = 69417*uW2^2
           minor = a*e - b*d = 75772*uW1^2*uW2^2

p=105673:  coeff(R1,x33) = 37827*uW1^2   coeff(R1,x38) = 82112*uW2^2
           coeff(R2,x33) = 37989*uW1^2   coeff(R2,x38) = 59604*uW2^2
           minor = a*e - b*d = 9899*uW1^2*uW2^2
```

These are **character-for-character the values claimed in sol-ideas-0821.md item 1**
(75772*uW1^2*uW2^2 and 9899*uW1^2*uW2^2) and verified by the replay
(`Delta_scalar` 75772 / 9899, `Delta_mono` `uW1^2*uW2^2`). Since rows 24, 25 of the
same file are literally `W1*uW1 - 1` and `W2*uW2 - 1`, uW1 and uW2 are units on the
whole variety, so **the minor is a unit. It is NOT zero.**

Why Ox got 0: `affine_coefficient` in `cases/ox_calibration.py` (lines 215-219)
keeps only monomials with `sum(monomial) == 1`, i.e. TOTAL degree 1. The actual
coefficient monomials `x33*uW1^2` have total degree 3, so Ox's extraction returns
0 for all four entries and hence minor = 0 -- by construction, for any pivot whose
coefficient is a Laurent monomial rather than a bare constant. The certificate
explicitly claims a Laurent-monomial minor; Ox's extractor is structurally blind
to exactly that claim.

## 3. THE POINT and the LOCALIZATION: the witness lies INSIDE Ox's chart, and Ox's dim = -1 is a code bug, not a localization effect

**Witness evaluation (fresh).** The banked explicit witness for a00mm (all 24
x-coordinates = 0; W = (31931, 9457), uW = (64754, 22756) at p=105337;
W = (8021, 20111), uW = (13662, 64399) at p=105673) vanishes on **34/34 rows of the
exact files Ox parsed**, at both primes (fresh evaluator, raw rows, no
canonicalization).

**The localization hypothesis is REFUTED.** Ox's `localized_dimension` saturates by
`W1*W2*uW1*uW2` (default `invert` tuple, line 127). The witness has all four of
those coordinates NONZERO; its zero coordinates are the 24 x-variables, none of
which Ox's committed code inverts. So the witness lies inside Ox's own localized
chart, and "empty localized chart, point outside the chart" is NOT the
reconciliation. Ox's chart contains a point; its dim = -1 is simply false.

**The actual cause.** `singular_ideal_string` (lines 119-124) iterates over the
monomials of each polynomial and joins **every monomial as a separate ideal
generator**:

```python
for monomial, coefficient in sorted(system.polys[index].items()):
    terms.append(singular_polynomial(system, {monomial: coefficient}))
return ",".join(terms)
```

Row 18 alone (one polynomial, 567 terms) becomes 567 generators, including the
**bare constant generator `71983`** (its constant term). Any ideal containing a
nonzero constant is (1), so `dim = -1` -- unconditionally, for every index set Ox
tested. Calibration probe: running Ox's own `localized_dimension` on the trivially
nonempty two-equation system {W1*uW1 - 1, W2*uW2 - 1} (true dimension 8 in A^10)
returns **-1**. All three dimension numbers in Ox's report
(`localized_dimension_full_raw_system`, `..._laurent_plus_six_terminal_rows`, and
the "aligned constants" negative control) are -1 for this reason and carry zero
information about the systems. Ox's negative control could never have come out any
other way -- the control validated the bug, not the mathematics. (The heavier
saturation list in ox-calibration.md control 3, inverting x70...x66, is not in the
committed code, and is moot: the generator-splitting poisons every such run; and
in any case the interior points below have ALL of those coordinates nonzero.)

**Honest recomputation.** For the record, an honest Singular run (34 rows as whole
generators, dp order) was attempted locally: std timed out at 560 s per prime, and
a longer slimgb attempt had not completed at report-writing time (fail-closed: NOT
used as evidence either way) -- consistent with the certificate's whole point that
no large GB is needed. The GB-free evidence below settles the question anyway.

## 3b. Ox's "root contradiction" x70 + 52700*x72 = 0 is literally row 28 -- an elimination pivot, not an obstruction

Row 28 of `d25fam_p105337_a00mm.ms` is, in full: `x70 + 52700*x72` (p=105673:
`x70 + 9676*x72`). It is one of the 34 emitted rows and is the FIRST pivot of the
certificate's reconstruction DAG (replay `dagA_pivots`: row base28 solves x70,
pivot unit 1). It forces x70 = -52700*x72, i.e. it eliminates one dependent
variable. It does not force x70 = x72 = 0 and cannot "lead to emptiness" -- except
under Ox's monomial-splitting, which turns this binomial into the two generators
`x70` and `52700*x72`, i.e. exactly the false forcing x70 = x72 = 0.

**Fresh interior points (my own solver: substitute 14 random free values, derive
the 3 lift-free compatibility combinations from rows 29-33 myself, solve the 10
dependent variables by exact linear algebra, then evaluate all 34 PRISTINE rows):**

| prime | cell (W1,W2) | raw rows vanishing | x70 | x72 | x70+c*x72 | nonzero x-coords | Jacobian rank |
|---|---|---|---|---|---|---|---|
| 105337 | (31931,21687) | 34/34 | 86629 | 10626 | 0 | 24/24 | 14/28 |
| 105337 | (43162,83650) | 34/34 | 67655 | 79781 | 0 | 24/24 | 14/28 |
| 105337 | (62175,95880) | 34/34 | 96666 | 77188 | 0 | 24/24 | 14/28 |
| 105673 | (8021,25434)  | 34/34 | 103710 | 97253 | 0 | 24/24 | 14/28 |
| 105673 | (33847,80239) | 34/34 | 15622 | 53927 | 0 | 24/24 | 14/28 |
| 105673 | (71826,85562) | 34/34 | 90924 | 90374 | 0 | 24/24 | 14/28 |

Six distinct cells across both primes. Every point satisfies Ox's "forced relation"
with x70 and x72 both NONZERO (it is row 28; every point of the variety satisfies
it), has all 24 x-coordinates and all four W-units nonzero (deep interior -- far
from the all-x-zero witness, and inside even the heaviest localization Ox
mentioned), and is a SMOOTH point: Jacobian rank exactly 14 = 28 - 14, so each
point sits on a local component of dimension exactly 14. This is a rigorous,
GB-free refutation of "empty at both primes" and an independent confirmation of
NONEMPTY + dimension 14 + smoothness on the cells' interior. (The 288 banked
interior samples in `cases/d25_eplus.json` bank only (fiber, cell, sample, W1, W2)
plus the seed -- not full 28-coordinate vectors -- so the fresh points above are
the independent equivalent; the banked samples' (W1,W2) were verified to be genuine
fourth roots of (c1,c2), i.e. genuine cell labels, and c1 = 57673, c2 = 53212 resp.
c1 = 44399, c2 = 92038 each have exactly 4 fourth roots, brute-force verified.)

## 4. Remaining Ox claims, itemized

- **"The five residual rows are identical"** (ox-calibration.md "Root
  contradiction" section / hardcoded `reason` string): FALSE. The five rows are
  pairwise distinct (5 distinct term-multisets; 148/148/148/148/144 terms). Ox's
  own JSON output says `residual_rows_all_identical = false` -- its prose
  contradicts its own run because both `verdict` ("REFUTED") and `reason` are
  **hardcoded string literals** in `verify()` (lines 269-274 of
  `cases/ox_calibration.py`), emitted regardless of what was computed. A verifier
  whose verdict is a constant is not a verifier.
- **"Six distinct terminal constants => the parked Laurent system is already
  inconsistent"**: a misreading twice over. (i) The certificate never claims the
  raw rows 18-23 are trinomials; they are 525-567-term polynomials that REDUCE to
  (U,V,1)-trinomials only after the DAG substitution. (ii) Six trinomial equations
  in two unknowns with six different constants are not thereby inconsistent:
  fresh rank computation on the 6x3 matrices (which Ox's parser itself reproduced
  correctly) gives rank(A) = rank(A|b) = 2 at both primes -- CONSISTENT, unique
  solution (W1^4, W2^4) = (57673, 53212) resp. (44399, 92038), exactly as promoted.
  The interior points above vanish on rows 18-23, closing the question numerically.
- **What Ox got right**: its .ms parser is correct (34 x 28, matching shapes), and
  its terminal U/V/constant coefficient extraction reproduced the certificate's
  6x3 matrices exactly. The failures are all downstream of parsing.

## 5. Scope of what this adjudication itself certifies

Independently re-verified here, fresh code, both primes, fiber a00mm (+ hashes for
a00pp): the (x33,x38) minor is the claimed Laurent unit; the banked witnesses
vanish 34/34; the terminal 6x3 system is rank-2 consistent with the claimed
(W1^4,W2^4); the raw parked systems contain smooth interior points of local
dimension exactly 14 in six distinct cells. NOT re-derived here (and not contested
by anything in Ox's run): the global closure statement that the 16 cells exhaust
each parked fiber (34/34 rows reduce to zero through the DAG modulo the terminal
quartics) -- that remains covered by the replay (`closure_rows_zero: 34`, 72/72
fibers) and the Grok verdict-tier review (72/72 CONFIRMED), and nothing found
here casts doubt on it. The emission-fidelity caveat and modular-tier scope of the
AUDIT.md entry are untouched.

## 6. Disposition

- `xmodel/ox-calibration.md` verdict "REFUTED": **overturned in full**
  (OX-MISCALIBRATED). The file should be annotated as refuted by this forensics
  report and excluded from evidence; `cases/ox_calibration.py` should not be used
  as a verifier in any lane (constant verdict string, monomial-splitting ideal
  construction, degree-1-only coefficient extraction).
- AUDIT.md "D25 FAMILY NONEMPTINESS + CELL STRUCTURE" entry: **no retraction, no
  rescope**. Every promoted sentence tested here survived; the certificate's two
  most falsifiable numbers (the minor's scalar and monomial parts) were reproduced
  exactly from the raw bytes by a third independent implementation.
- Calibration lesson for scoring Ox: it silently replaced "coefficient in the
  Laurent chart" with "constant coefficient", replaced "ideal generated by the
  rows" with "ideal generated by the rows' monomials", drew "inconsistent" from
  a rank question it never computed, and shipped a hardcoded verdict that its own
  JSON contradicts. Each error is individually detectable by its own negative
  control had the control been sound (e.g. its aligned-constants control returning
  the same -1 as every other run was a red flag, not a confirmation).
