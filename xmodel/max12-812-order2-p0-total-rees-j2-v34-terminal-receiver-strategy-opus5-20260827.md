# V34 audit, the grade-19 prolongation design, and the terminal receiver `V(J1+J2)` (Opus 5)

Date: 2026-08-27

Lane: independent co-researcher analysis of the charged V34 result, the
grade-19 fork, and the terminal receiver.  Author: Opus 5.  This file is the
lane's sole repository write.  `jc2-lean` was neither read, entered, built,
nor modified.

Status headline: **V34's arithmetic is CONFIRMED and materially strengthened.
The five points are reduced, form a single Galois orbit with residue field
`Q(2^(1/5))`, and — new — they are exactly one sigma-orbit through an
explicit RATIONAL point.  That rational point kills all 63 literal
ordered-`a1` rows of grades 10--18 by direct exact substitution, with no
Groebner basis anywhere.  Independently: the six grade-18 rows V34 did not
append restrict to zero on this support, so V34's cut is complete at grade 18;
the surviving family sits at `k=0`, hence off the named unit-`k10` family; and
the grade-12 terminal-receiver rows alone force `e0=e1=0` unconditionally.
NO chart, receiver, Gate-T, order-two, maximum-twelve, or JC2 verdict.**

---

## 0. Custody, execution disclosure, and evidence tiers

Basis commit `418e413593120d19e15e6546eb50c985f4b1f038`, dirty campaign wave.
All hashes below observed by me with `shasum -a 256` on 2026-08-27.

```text
V34 PREREGISTRATION.md                 5e83cf25386a2ad9c8ceab0c8909f33c9361bf0b0f6f5806433faf331cf1ec80
V34 compile_grade18_curve_cut_v34.py   01784c72cd3f8d69ed57223a40d299a2d0ae05e8f9d1c33e179615b53d5a9830
V34 validate_grade18_curve_cut_v34.py  5f50aac27be95582c65b72b17891f4ca9b14afd0b3af9f8e85b5a2dbfd1c5576
V34 aws_q/RESULT.json                  7796c99ab5bdc2253754b3ca5f86adb42f2c192c6a2a575dd1f81d9cc69226fe
V34 aws_p65521/RESULT.json             f293aaa2bb005778209e1ecbf9b3e12e9a3c59554f24989737b3d8b031babd46
V34 BASIS_G18_q.txt                    1e81e737cdab19a9a1b3cb2c6253fecc82c266db236af6fcf67aa03dbd419e40
V34 BASIS_G18_p65521.txt               96990faf637dc5f3c4bb5b72881fed8fd0b004361b97151605f30c6be3d82bfa
V32 aws_q/compiled/BASIS.txt           ee4f77808d7e2c36588cfba65f252bcb068dbb360f3e4abb843e2b9215e9819b
V33 aws_q/compiled/Tg18_6_q.poly       fdfb477feb6a97413668f705d9a6bd565501b655f1ab42fc29874121e744a6de
V23 census_j2_typed_v23.py             14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501
V23R1 output_r1/RESULT.json            ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641
Fable5 grade-16 boundary strategy      7e4abb962ca0d0fdc08890b4ce9c5f8f0bcfbc29accf8f38a0813ef844e1cfcd
Round synthesis 20260827T0145Z         cb1b625e056753ae99580d80788534ca20f25040cd0921745c58ce6ad765c90b
T-a0 pure-cubic promotion              3e3aa876dc4fc0a49dd41eb060fedc8c1fa8d64a1d2f0731ac5cb27e233380a6
```

Manifest replays I ran myself:

- `cases/.../v34_.../FREEZE.sha256`: **13/13 OK** (all upstream pins,
  including the V32 basis, the V33 Q and F65521 rows, the V23 parser, and
  `ops/aws_exact_lane.sh`).
- `cases/.../v32_.../FREEZE.sha256`: **10/10 OK**.
- V34 `aws_q/EVIDENCE.sha256` and `aws_p65521/EVIDENCE.sha256`:
  **17/17 OK each**, after stripping the absolute
  `/home/ubuntu/jobs/.../source/cases/.../` prefix.  The absolute-path
  portability defect Fable5 flagged for V28 recurs verbatim in V34; freeze
  relative paths.  This is a custody defect, not a mathematical one.

Execution disclosure: everything I computed is my **own** scanner/AST parser
plus exact `Fraction` arithmetic, and exact arithmetic in `Z[t]/(t^5-2)`,
staged in `/tmp/opus5v34/`.  No CAS, no Groebner engine, no solver, no AWS
mutation, no web.  Every step ran in seconds and far under 1 GiB.  I did
**not** re-run Singular and therefore did not recompute a standard basis; §1.6
states exactly which single V34 claim still rests on the frozen lane.

Evidence tiers used below:

- `EXACT-OPUS`: recomputed by me from frozen bytes with exact rational or
  number-field arithmetic, or proved by hand algebra shown in full.
- `FROZEN-LANE`: asserted by the charged V34/V33/V32 Singular runs, replayed
  by hash only.
- `EMPIRICAL-PATTERN`: true on every exported grade I checked, with no proof.
- `PROMOTED`: already in `AUDIT.md` at its recorded scope.

---

## 1. Task 1 — independent audit of V34

### 1.1 What V34 charged, restated exactly

V34 restricts every literal ordered-`T-a1` (`J1=(rs,cs,c0,c1)=0`, `a0=0`)
actual-total source row to the six-coordinate support
`{ell2,cs1,rs2,aa0,ee1,ec3}` with `a1=48` and every other registered
coordinate — including `rho` and `k` — set to zero, appends the restricted
`Tg18_6` to the 24-element V32 standard basis, and reports over exact `Q` and
over `F_65521`:

```text
V34_DIM=0   V34_STANDARD_BASIS_SIZE=12   V34_UNIT_IDEAL=0   V34_VDIM=5
```

Both lanes ran on distinct hosts (`ip-172-30-0-186` char 0,
`ip-172-30-0-249` char 65521) from the same source archive
`efb8ff98...`, in under one second at ~10.6 MiB RSS.

### 1.2 Byte-level recomputations I performed (all `EXACT-OPUS`)

1. **The restricted row.**  I reparsed the frozen `Tg18_6_q.poly` (140 terms)
   with my own parser, applied the restriction myself, and got a 16-term
   polynomial **identical** to the `poly P18=...` embedded in the frozen
   `grade18_curve_cut_q.sing`.  Term count 16 matches
   `grade18_restricted_term_count`.
2. **Cross-characteristic row shadow.**  The frozen `Tg18_6_p65521.poly`
   restricts to the mod-65521 reduction of the `Q` restriction, term by term.
3. **The preregistered negative control.**  On the `aa0=0` branch
   (`ell2=l, cs1=12/l, rs2=-(20/9)l^2, ee1=32l, ec3=576/l`) the restricted
   `Tg18_6` is the Laurent monomial `41472*l^(-1)` exactly — the value V34
   preregistered.  So `Tg18_6` genuinely is **not** in the V32 ideal, and the
   V34 cut is a real cut.
4. **The V33 obstruction, in closed form.**  Substituting the V33
   sigma-scaled rational point into all 63 rows, exactly 62 vanish and
   `Tg18_6 = 16210220612075905068`.  I also derived that number by hand from
   the sigma covariance law:
   `Tg18_6(sigma_u x) = u^18 * Tg18_6(x)` with `u=l^2`, so the value is
   `41472*l^35 = 41472*(243/2)^7 = 2^2*3^39 = 16210220612075905068`.
   **The V33 dual is exactly `4*3^39`.**  This is a stronger, checkable form
   of a number the ledger currently carries only as 20 digits.
5. **Cross-field basis consistency.**  Each of the 12 `F_65521` basis
   elements is a unit multiple of the mod-65521 reduction of the
   corresponding `Q` basis element (I checked all 12, not a sample).  Note
   what this does and does not buy: the two lanes share a source archive and
   a script generator and produced byte-identical Singular protocol output,
   so they are a *lucky-prime* consistency check, not two independent
   derivations.  The independence in this audit comes from §1.3--§1.5.

### 1.3 The ideal solved in closed form — Kummer / primitive-element presentation

The 12 printed generators impose, in order, `cs1` and `ell2` as linear
functions of `ec3, ee1`, and then rewrite **every** degree-2 monomial in
`{rs2,aa0,ee1,ec3}` down to degree `<= 1`:

```text
ec3^2 = -3750*aa0        ee1*ec3 = 21600        aa0*ec3 = (2880/7)*rs2
rs2*ec3 = -(875/24)*ee1  ee1^2   = -(20736/35)*rs2   aa0*ee1 = -(144/25)*ec3
rs2*ee1 = (105/2)*aa0    aa0^2   = 4*ee1        rs2*aa0 = 210
rs2^2   = (49/96)*ec3    600*cs1 = 11*ec3       192*ell2 = 7*ee1
```

Hence `Q[ell2,cs1,rs2,aa0,ee1,ec3]/I` is spanned by `{1,rs2,aa0,ee1,ec3}`, so
`dim_Q <= 5`.  Eliminating gives one Kummer equation.  Two equivalent clean
forms, both `EXACT-OPUS`:

```text
ec3^5 = 2^9 * 3^5 * 5^10 = 1215000000000
ee1^5 = 2^16 * 3^10      = 3869835264
```

with the primitive element `theta := ee1/72`, `theta^5 = 2`, i.e.
`K = Q(2^(1/5))`.  All six coordinates are `Q`-multiples of powers of
`theta`:

```text
ell2 = (21/8)*theta      cs1 = (11/4)*theta^4     rs2 = -(35/4)*theta^2
aa0  = -12*theta^3       ee1 = 72*theta           ec3 = 150*theta^4
a1   = 48                rho = 0                  all other coordinates 0
```

or, purely in the primitive element `E := ee1`:

```text
ell2 = 7E/192   cs1 = 11E^4/107495424   rs2 = -35E^2/20736
aa0  = -E^3/31104   ec3 = 25E^4/4478976   with  E^5 = 3869835264
```

I verified by exact substitution that **all twelve** printed `Q` generators
vanish identically at this point (they do; the check is one line of algebra
per generator, e.g. `rs2*aa0 = (-35/4)(-12) theta^5 = 105*2 = 210`).

**Reducedness and Galois structure (`EXACT-OPUS`).**  `x^5 - 2^9 3^5 5^10` is
irreducible over `Q` because the 2-adic exponent 9 is not divisible by 5, and
it is separable in characteristic zero.  Therefore:

- over `Qbar` the scheme is **5 distinct reduced points**, each of
  multiplicity 1 (5 points and `dim_Q = 5` force multiplicity 1);
- over `Q` the ideal is **prime**: it is the kernel of the evaluation
  `Q[6 vars] -> Q(2^(1/5))`, a single closed point of residue degree 5;
- the five geometric points are one transitive `Gal(Q(2^(1/5),zeta_5)/Q)`
  orbit.

**Independent confirmation of `VDIM=5` and `STANDARD_BASIS_SIZE=12`
(`EXACT-OPUS`, no Groebner engine).**  With `dp` and
`ell2 > cs1 > rs2 > aa0 > ee1 > ec3`, the twelve leading terms are
`ell2, cs1` and all ten degree-2 monomials in `{rs2,aa0,ee1,ec3}`.  The
standard monomials are exactly `{1, rs2, aa0, ee1, ec3}`, so
`dim Q[x]/L = 5`.  Since `L subset in(I)` gives `5 = dim Q[x]/L >= dim Q[x]/in(I)
= dim Q[x]/I = 5`, the twelve polynomials **are** a Groebner basis, it is
minimal (no leading term divides another) and reduced (every tail lies in the
span of the standard monomials).  So `DIM=0`, `UNIT_IDEAL=0`,
`STANDARD_BASIS_SIZE=12`, `VDIM=5` are all confirmed by hand.

### 1.4 Sigma scaling turns the orbit into a rational representative — YES

The frozen `sigma_weight` table in `census_j2_typed_v23.py` gives

```text
w(ell2)=2  w(cs1)=3  w(rs2)=4  w(a1)=5  w(aa0)=6  w(ee1)=7  w(ec3)=8  w(rho)=0
```

and every exported row `Tg{g}_{r}` is sigma-homogeneous of weight `g` (V23
fails closed on this, and I re-verified it on the restricted rows).  So
`Tg{g}_{r}(sigma_u x) = u^g * Tg{g}_{r}(x)`.

The theta-exponents of the five-point orbit are
`(ell2,cs1,rs2,aa0,ee1,ec3) -> (1,4,2,3,1,4)`, and one checks
`2*w_i + e_i = 0 (mod 5)` for **all six** coordinates — a six-fold
coincidence that is exactly the solvability condition.  Taking `u = theta^2`
clears every root:

> **Theorem (rational representative, `EXACT-OPUS`).**  Put
> ```text
> a1 = 192,  ell2 = 21/4,  cs1 = 11,  rs2 = -35,
> aa0 = -96, ee1 = 576,    ec3 = 2400,  rho = 0,
> ```
> with **every** other registered source coordinate zero.  Then all 63 literal
> ordered-`a1` actual-total rows of grades 10--18 vanish exactly over `Q`.
>
> More generally the whole sigma-orbit is rational and one-parameter:
> ```text
> a1 = 192q^5, ell2 = (21/4)q^2, cs1 = 11q^3, rs2 = -35q^4,
> aa0 = -96q^6, ee1 = 576q^7, ec3 = 2400q^8      (q in Q*)
> ```
> I verified `q in {1, 2, -1, 3, 1/2, -2/7}` against all 63 frozen rows:
> 0 nonzero rows in every case.  `q=2` is integral:
> `a1=6144, ell2=21, cs1=88, rs2=-560, aa0=-6144, ee1=73728, ec3=614400`.

The `a1=48` normalization is a **slice** of the sigma-action whose stabilizer
is `mu_5`, and the `mu_5` action on the six coordinates has exponents
`(2,3,4,1,2,3)`; composing with `m=3` reproduces the Galois action exactly.
**So the "five points" are one point of the sigma-quotient.  The apparent
degree 5 is entirely an artifact of fixing `a1=48`, not arithmetic depth.**
Consistently, every V34 generator is `mu_5`-homogeneous (I checked all 12).

### 1.5 A completeness gap in V34 that I closed, and one weak control

**Gap closed (`EXACT-OPUS`).**  V34 appends only `Tg18_6`.  Its
preregistration never records why the other six grade-18 rows may be dropped.
I restricted **all 63** rows myself.  Exactly six restrict to a nonzero
polynomial on this support:

```text
Tg13_1 (3 terms)  Tg14_2 (5)  Tg15_3 (8)  Tg16_4 (10)  Tg17_5 (16)  Tg18_6 (16)
```

All 57 others restrict to the zero polynomial.  Through grade 17 that is 5
nonzero rows, matching V32's own `nonzero_rows: 5` and its
`newton_nonzero_residuals_q` keys.  **Therefore V34's grade-18 cut is
complete on this support**: appending `Tg18_6` alone loses nothing.  This was
previously unrecorded.

**Zero-jet convention is sound here (`EXACT-OPUS`).**  Fable5 correctly warned
that V28's "set the new jets to zero" convention produces false negatives in
general.  I computed the full Jacobian of all 63 rows at the rational point
and found that the six diagonal rows `Tg{g}_{g-12}` (`g=13..18`) have
**every** nonzero Jacobian column inside the seven-coordinate support
`{a1,ell2,cs1,rs2,aa0,ee1,ec3}`.  They are jet-blind at this point: no jet of
any name moves them to first order.  So V34's convention cannot have hidden a
survivor at grade 18 — and, equally, no jet could have rescued V33's point.

**Weak control.**  The `.sing` guard
`if (reduce(G[1],GS)!=0) { print("FAIL_OLD_BASIS_CONTROL"); quit; }` is
tautological: `G[1]` is a generator of `G` and `GS=std(G)`, so the reduction
is zero unless the engine is broken.  It detects engine malfunction only.
The real negative control in the script is `NF18 != 0`, which did fire
correctly (`NF18 = 384*ell2*aa0 - 3456*cs1 + 144*ec3`, identical text in both
characteristics because Singular prints `Z/p` symmetrically and `reduce` does
not normalize).  Similarly `basis.count(",") != 23` is a census, not a
structural check.

### 1.6 What V34 proves, and the one claim still resting on the frozen lane

| Claim | Tier after this audit |
|---|---|
| `Tg18_6` restricted is the exact 16-term polynomial in the script | `EXACT-OPUS` |
| The `aa0=0` branch control equals `41472/l` | `EXACT-OPUS` |
| The V33 dual is `4*3^39` | `EXACT-OPUS` (new closed form) |
| The five points exist, are reduced, prime over `Q`, residue field `Q(2^(1/5))` | `EXACT-OPUS` |
| Printed basis is the reduced `dp` Groebner basis of its own ideal, `vdim 5` | `EXACT-OPUS` |
| The five points satisfy all 24 V32 generators and `P18` | `EXACT-OPUS` |
| The five points satisfy all 63 literal rows, grades 10--18 | `EXACT-OPUS` (stronger than V34 claimed) |
| The orbit is one sigma-orbit through an explicit rational point | `EXACT-OPUS` (new) |
| **No sixth point**: `J subset (G_V32 + P18)` | `FROZEN-LANE` only |

The single unclosed direction is the *upper* bound.  I proved
`(G_V32 + P18) subset J` by evaluation, giving `V(G_V32+P18) contains` the
five points; the reverse inclusion needs the standard-basis computation I am
not permitted to redo.  This asymmetry is benign: the campaign-relevant
content — "grade-18 survivors exist on this support" — is the direction I
fully verified, and I verified it in a stronger, Groebner-free form.

### 1.7 Two scope facts the ledger should carry with V34

**(a) The surviving family is at `k = 0`, hence off the named unit-`k10`
family.**  `k` is not in the V34 support, so `k=0` at every one of the five
points and along the whole rational sigma-orbit.  By the promoted localizer
ledger (`a09232d6...` / `678a087d...`), `D(k)` is intrinsic to the named
post-`M=0`, unit-`k10` Gate-T family.  **A `k=0` survivor is therefore not an
on-family witness.**  It belongs, at face value, with the separately carried
off-family load-timing fan.

**(b) Certificate-refutation ledger, corrected and extended.**  Because
`a1 = 192 != 0` and `rho = 0` at a point where all 63 rows vanish:

- every typed certificate of shape `a1^N * (1 + rho*W)` built from rows of
  grade `<= 18` is **refuted, for all `N`** (`EXACT-OPUS`) — this extends
  Fable5's grade-`<=16` statement by two grades;
- certificates of shape `a1^N k^M (1 + rho*W)` with `M >= 1` are **not**
  refuted by this witness (`k^M = 0` here).  Fable5's Witness B (`k=1`)
  refutes those only through grade 16.  Do not merge the two ranges.

I also computed the Jacobian of all 63 rows at the rational point: rank 26 of
57 variables, kernel dimension 31, and the `k`-column **is** in the span of
the others.  So the `k != 0` direction is first-order reachable at this
point — an exact statement, but a first-order one, not existence.

---

## 2. Task 2 — the smallest fail-closed grade-19 prolongation (design `V35`)

### 2.1 The structural shortcut: the answer is one rational number

Three facts, all established above, collapse a would-be generic Groebner
computation to a single substitution.

1. **Orbit rigidity.**  The five points are one Galois orbit *and* one
   sigma-orbit through a rational point.  Any `Q`-rational new equation
   therefore vanishes at all five or at none.  There is no partial survival
   and nothing to intersect.
2. **Sigma covariance.**  `Tg19_j(sigma_q P_1) = q^19 * Tg19_j(P_1)`.  One
   evaluation at `q=1` decides the entire one-parameter rational family.
3. **Diagonal jet-blindness.**  On this support exactly one row per grade is
   nonzero, at index `g-12`, and at the rational point its differential is
   supported entirely inside the seven support coordinates.

So the grade-19 verdict is: **evaluate the seven grade-19 rows at one
rational 7-tuple.**  No `std`, no `dim`, no `vdim`, no elimination.  If any
value is nonzero and jet-free the family dies; if all are zero with the new
coordinates set to zero, it survives.  This is a V33-sized job, not a V34- or
V29-sized one.

The residual risk is that the diagonal pattern (`EMPIRICAL-PATTERN`, six
consecutive grades) breaks at 19.  The design below does **not** assume it: it
computes all seven rows and treats the pattern as a preregistered control.

### 2.2 Source-series depth and old-row bridges

Reuse the V33 emitter exactly: the frozen 569-tail canonical source
(`tails.json d72f774c...`, V20 module pin as used by V28/V30/V33), driven to
`t`-order 19 on the ordered chart `J1=0, a0=0`, at `rho=0`.  Grade 19 is one
`t`-order past V33; V33 compiled grade 18 in the same envelope as V28's 73 s
grade-16 compile, so a single dual-lane pair is ample.

Old-row bridges (byte-comparison, fail closed on any mismatch):

```text
grades 10-15  ->  V23R1 output_r1/a1_ordered/Tg{g}_{r}.poly   (ce4d0adb...)
grade 16      ->  V28 aws_q/compiled/Tg16_{r}_q.poly           (7e00fc2c...)
grade 17      ->  V30 aws_q/compiled/Tg17_{r}_q.poly           (6a644c20...)
grade 18      ->  V33 aws_q/compiled/Tg18_{r}_q.poly           (22f64fbb...)
```

### 2.3 Variables — and a naming trap that must not be repeated

There are **no** coordinates of sigma-weight 19 in the inventory (the deepest
through grade 18 is `ec8` at weight 13).  Reading "new weight-19 coordinate"
as "sigma-weight exactly 19" would make the unknown set empty — precisely the
V28 false-negative convention Fable5 flagged.  `V35` must use the honest
reading: **every coordinate whose first occurrence is in a grade-19 row**.
From the frozen first-occurrence census (`grade = weight + offset`, offsets
5--11 by family) the predicted grade-19 newcomers are

```text
ell8 (w=8), cs7 (w=9), rs7 (w=9), k10_6 (w=10),
ac8, az8, ez8 (w=13), ec9 (w=14),  plus any k6_j that first appears
```

but the design must **enumerate them from the emitted rows**, not from this
prediction, and must treat every one as an honest affine unknown.  All old
coordinates, including the ones the V34 support set to zero, are *fixed* by
the point being tested; they are not unknowns.

### 2.4 Mandatory fail-closed controls

Positive controls (must reproduce exactly):

1. `Tg18_6` at the V33 sigma-scaled `aa0=0` point `= 16210220612075905068
   = 4*3^39`, and the other six grade-18 rows `= 0` there.
2. The V34 rational point kills all 63 rows of grades 10--18 (0 nonzero).
3. Restricted-row census through grade 18 reproduces the diagonal
   `Tg13_1, Tg14_2, Tg15_3, Tg16_4, Tg17_5, Tg18_6` with term counts
   `3, 5, 8, 10, 16, 16`, and 57 identically-zero restrictions.
4. Every grade-19 row is sigma-homogeneous of weight 19 and `rho`-even.

Negative controls (must **not** silently pass):

5. Perturb the rational point in one coordinate (e.g. `ee1 -> 577`) and
   require at least one row of grade `<= 18` to become nonzero.
6. Delete one grade-19 row from the emitter and require the manifest/bridge
   check to fail.
7. Emit the grade-19 rows with the new coordinates forced to zero **and**
   with them symbolic, and record both; a discrepancy is the jet-blindness
   signal, not an error.

### 2.5 Exact outputs to emit

```text
Q lane:
  Tg19_j_q.poly                       j=1..7, full literal rows
  Tg19_j_restricted_q.poly            restriction to {ell2,cs1,rs2,aa0,ee1,ec3}, a1=48
  Tg19_j_at_point_q.poly              value at the rational point, new coordinates symbolic
  RESULT.json: per-row  {term_count, restricted_term_count, jet_variables,
                         constant_value_at_point, affine_rank, solvable}
F65521 lane: the same objects, term-by-term shadows of the Q lane.
```

The decisive scalars are the seven rationals `Tg19_j(P_1)`; the campaign
should print them in full, with their integer factorizations (the pattern so
far — `-20736 = -2^8*3^4` at grade 17 on Fable5's `S0` family, `4*3^39` at
grade 18 on the `aa0=0` branch — suggests the factorizations are themselves
informative).

### 2.6 Interpretation table

| Grade-19 outcome | Reading | Next move |
|---|---|---|
| All 7 rows vanish at `P_1` with zero new coordinates | The rational sigma-family survives grade 19 in the full coordinate system | Go to §4 card A2: grade 20, where the diagonal index would be 8 and the seven-row inventory is exhausted |
| Some row nonzero at `P_1` but an emitted new coordinate has a nonzero pivot, and the affine system is solvable | Family survives with a determined jet law | Record the jet law; repeat at grade 20 |
| Some row nonzero at `P_1` and jet-free (diagonal behaviour) | **The whole six-coordinate sparse support dies at grade 19** — not the chart | Enlarge support (`k, aaa1, rs4, ...`) or switch to the Rees/Gate-T comparison |
| Diagonal pattern breaks (two or more nonzero restricted rows) | The empirical pattern was coincidence | Re-run a V34-style symbolic cut, this time appending every nonzero restricted row |

In **every** branch this decides one sigma-orbit on one support.  It cannot
close ordered `T-a1`, and a death here must not be reported as one.

---

## 3. Task 3 — the terminal receiver `V(J1+J2)`

### 3.1 The receiver's literal source rows are already on disk, for free

`V(J1+J2)` is `rs=cs=c0=c1=a0=a1=0`.  The V23R1 `a1_ordered` files are the
literal rows with `J1=0, a0=0`.  **Setting `a1=0` in those very files is the
receiver restriction.**  No new export, no AWS, no emitter run is needed for
grades 10--18.  I did this and the result is startlingly sparse.

Grades 10 and 11 vanish identically.  The **first** receiver rows are at
grade 12 and they are four short quadratics (`EXACT-OPUS`, from frozen
bytes):

```text
Tg12_1 = (3/8)(aa0*e1 + aa1*e0)
Tg12_2 = (3/8) aa0*e0 + (3/8) aa1*e1*rho^2 + (3/32) e1^2
Tg12_3 = (3/16)(aa0*e1 + aa1*e0)*rho^2 + (3/16) e0*e1
Tg12_4 = (3/32)(e0^2 + e1^2*rho^2)
Tg12_5, Tg12_7 are rho-multiples of Tg12_1 plus e0*e1 corrections;  Tg12_6 = 0
```

### 3.2 The first bounded discriminator, proved here

> **Lemma R1 (`EXACT-OPUS`, unconditional).**  On `V(J1+J2)`, the grade-12
> rows alone force `e0 = e1 = 0`, over any field of characteristic `!= 2,3`,
> with `rho` free and no localization whatsoever.
>
> *Proof.*  `Tg12_3 - (rho^2/2)*Tg12_1 = (3/16) e0*e1`, so `e0*e1 = 0`.
> `Tg12_4` gives `e0^2 + e1^2 rho^2 = 0`.  If `e1 = 0` then `e0^2 = 0`.  If
> `e0 = 0` then `e1^2 rho^2 = 0`; when `rho != 0` this gives `e1 = 0`, and
> when `rho = 0` the row `Tg12_2` collapses to `(3/32)e1^2 = 0`.  Either way
> `e0 = e1 = 0`.  Every displayed coefficient is a frozen byte. `QED`

This immediately matters because it is a *closed condition* that the promoted
all-depth `Z00` fact does not supply: `Z00` is the origin and trivially has
`e0=e1=0`, but Lemma R1 says **every** receiver point does.  The receiver is
not "all of the `(J1,J2)=0` affine space minus what the rows cut"; the rows
start cutting at grade 12.

The cascade continues, still by hand:

> **Lemma R2 (`EXACT-OPUS`).**  After `e0=e1=0`, the identity
> `Tg14_3 - (rho^2/2) Tg14_1 = (3/16) ee0*ee1 - (ell1/2) Tg13_1` holds
> exactly on the receiver (I verified it as a polynomial identity).  With
> `Tg14_4 = (3/32)(ee0^2 + ee1^2 rho^2)` this gives `ee0 = 0` always, and
> `ee1*rho = 0`.

> **Lemma R3 (`EXACT-OPUS`, on `D(k)`).**  On the receiver intersected with
> the named unit-`k10` locus `k != 0`:
> - if `rho != 0`: `ee1 = 0`, and the two surviving grade-13 rows factor as
>   `Tg13_1 = (5/256) k*cs1*(3 rs1^2 + 16 cs1^2 rho^2)`,
>   `Tg13_2 = (5/1024) k*rs1*(48 cs1^2 rho^2 + rs1^2)`, whose only common
>   solution is `cs1 = rs1 = 0`;
> - if `rho = 0`: `Tg13_2` collapses to `(5/1024) k*rs1^3`, forcing
>   `rs1 = 0`, and then `Tg13_1` collapses to `(3/8) aa0*ee1`, forcing
>   `aa0*ee1 = 0`.

So four grades of frozen bytes already force, on `D(k)`,
`e0 = e1 = ee0 = rs1 = 0` and a two-branch split, with **no solver at all**.
Continuing the `rho=0`, `D(k)` branch through grade 18 (all frozen) leaves
extremely short equations, e.g.

```text
Tg15_4 = -(3/32) ee1^2*ell1                     Tg16_7 = -(3/128) aa0*ee1*ell1^3
Tg16_4 = (3/32)(ec3^2 - aa0^2*rs2)              Tg18_6 = -(1/64) aa0 (3 ec3*rs2 + 4 aa0^2)
```

after the further branch `ee1 = 0` or `aa0 = 0`.  This is a genuinely small
object — far smaller than `T-a1` — and it has never been censused.

### 3.3 The origin is not the receiver, and it is off-family

The promoted all-depth theorem says all seven literal source series vanish
identically at `CS0` and at the terminal origin `Z00`.  Two consequences must
be kept apart:

1. **No deeper row of this source can empty the receiver by hitting `Z00`.**
   Correct, promoted, and the reason `AUDIT.md` forbids deeper exports aimed
   only at `CS0/Z00`.
2. **`Z00` has `k = 0`.**  It is therefore *outside* `D(k)`, i.e. outside the
   named unit-`k10` Gate-T family — exactly the way `CS0` satisfies the
   honest `T-cs` bilinears and `1-u*cs=0` but cannot satisfy `1-v*k=0`.

So the all-depth zero-section blocks emptiness proofs aimed at the origin but
**does not** block emptiness of the on-family receiver `V(J1+J2) cap D(k)`.
That is the object to attack, and Lemmas R1--R3 show it is already being cut.
Confusing the two would either forbid a live line of attack or over-claim a
witness that cannot be on-family.

### 3.4 Cheapest census/discriminator design (`V36`), kept parallel to `T-a1`

`V36` is desk-scale and needs no AWS:

1. Freeze the receiver restriction: for `g=10..18, r=1..7`, emit
   `Tg{g}_{r}` with `a1 -> 0` from the pinned V23R1/V28/V30/V33 bytes.
   Record term counts (mine: 0,0 at grades 10--11, then
   `2,3,3,2,3,0,3` at grade 12, rising to 2787 terms total).
2. Record the Rabinowitsch generator `1 - v*k` explicitly, so the on-family
   scope is in the artifact rather than in prose.
3. Emit the cascade as a machine-checkable certificate chain: the exact
   cofactor identities of Lemmas R1--R3, each as
   `combination of frozen rows = target monomial`, with zero residual.
4. Branch on `rho = 0` vs `rho != 0` and on `ee1 = 0` vs `aa0 = 0`, and for
   each of the (at most four) leaves emit the reduced row set through grade
   18.  Controls: `Z00` must satisfy every leaf's rows (it does, trivially,
   and it must fail `1 - v*k`); a perturbed point must fail.
5. Only then, if a leaf is still large, hand one leaf to a bounded AWS `std`
   — and only that leaf.

Run this **in parallel** with the `T-a1` grade-19 card, exactly as
`COORDINATION.md` requires; it shares no compute and no premise with `V35`.

The honest ceiling: these are *raw row* equations.  Emptiness derived from
them is valid for the honest receiver (the rows are necessary conditions);
**nonemptiness is not**, because the saturated Rees presentation carries
further equations that are still missing.  Same asymmetry Fable5 recorded for
`T-a1`.

---

## 4. Task 4 — effect on ranking, and three next-action cards

### 4.1 What changes

- **Lower** the "close ordered `T-a1` by a finite-grade typed certificate"
  route again.  There is now an exact **rational** witness surviving all 63
  rows through grade 18, which refutes every `a1^N (1+rho W)` shape from
  grades `<= 18`.  Two consecutive grades (17, 18) have failed to close it.
- **Do not** upgrade this to a threat yet: the witness is at `k = 0`, hence
  off the named unit-`k10` family.  The genuinely rank-changing question is
  no longer "does it survive grade 19" but "**can it be moved onto `D(k)`**".
  I showed `k` is first-order reachable there; that is a lead, not a point.
- **Raise** the terminal receiver.  It was being treated as blocked by the
  `Z00` all-depth theorem.  It is not: `Z00` is off-family, and the grade-12
  rows already cut the receiver unconditionally.  The receiver is now the
  cheapest live object in the landing tree.
- **No change** to the promoted first-stage `J1` closures, `T-a0`, the
  coverage/deck-square obligations, or the classical frontier gate.  Nothing
  here proves or disproves any of them.

### 4.2 Cards

**Card A — `V35`: grade-19 single-scalar prolongation.**
*Dependencies:* the V33 emitter and its 569-tail pins; the rational point in
§1.4.  *Cost:* one dual AWS lane, V33-sized.  *Discriminator:* the seven
rationals `Tg19_j(P_1)`.  *Outcomes:* as §2.6.  *Stop rule:* this card buys
**at most two grades**.  If the family also survives grade 20 — the grade at
which the empirical diagonal index would exceed the seven-row source
inventory — stop grade-chasing entirely and move the burden to the
Rees/Gate-T comparison.  A single jet-free nonzero value ends the card
immediately.  *Expected information:* high and cheap; it is one substitution.

**Card B — `V35k`: the on-family repair.**
*Dependencies:* Card A's row bytes are *not* needed; grades `<= 18` suffice.
*Method:* enlarge the V34 support by `k` plus the pivots that couple to it at
the point — from my Jacobian, `k` appears with nonzero coefficient exactly in
`Tg15_1, Tg16_2, Tg17_3, Tg18_4`, where `aaa1, ac3, cs3..cs6, ec5..ec8,
ez4..ez7, ell3..ell6, rs3..rs6` all have nonzero pivots — and solve exactly
for a point with `k != 0` on the enlarged support, mirroring Fable5's `aaa1`
repair of Witness A into Witness B.  *Discriminator:* an exact rational
on-family point through grade 18, or a rational dual proving `k = 0` is
forced.  *Outcomes:* a point makes the `T-a1` survivor **on-family** and
refutes `a1^N k^M (1+rho W)` for all `(N,M)` through grade 18, which is a
genuine rank change; a dual confines the survivor to the off-family fan and
lets `T-a1` be attacked with `k`-carrying certificates.  *Stop rule:* stop
after the first-order solve plus one exact lift attempt; do not iterate
supports more than once without a new idea.

**Card C — `V36`: terminal receiver cascade census.**
*Dependencies:* none beyond the already-frozen V23R1/V28/V30/V33 bytes;
desk-scale, no AWS.  *Discriminator:* Lemmas R1--R3 as frozen certificates,
plus the reduced row set on each of the at most four `D(k)` leaves.
*Outcomes:* a leaf that becomes the unit ideal closes a component of the
on-family receiver; a leaf with an exact witness exhibits a genuine surviving
receiver family and is the first real evidence against the "all mass lands in
the receiver" plan.  *Stop rule:* if after grade 18 no leaf is either unit or
witnessed, stop the hand cascade and hand exactly one leaf to a bounded
`std`; do not fund a deeper source export for the receiver, which the
promoted all-depth theorem already shows is futile against `Z00`.

Dependency graph: A and C are independent and should run concurrently.  B
depends on nothing but consumes the same rational point as A; if capacity
allows only two, run **B and C**, because B decides whether A's answer is
even on-family.

---

## 5. Scope firewall

Everything above concerns the literal 569-tail actual-total source rows of
grades 10--18, specialized to the ordered stage-two `a1` chart over `V(J1)`
(`J1=(rs,cs,c0,c1)=0`, `a0=0`), on the closed face `rho=0`, in the **raw row
ideal** — and, in §3, the further restriction `a1=0` defining `V(J1+J2)`.
The saturated Rees chart kernel and its Gate-T comparison remain missing;
nothing here supplies them.

Specifically, this report does **not** claim, and its evidence does not
prove:

- that ordered `T-a1` is closed, nonempty as an honest chart, or decided;
- that the terminal receiver `V(J1+J2)` is closed or nonempty as an honest
  chart — Lemmas R1--R3 are necessary conditions from raw rows only;
- anything about grades `>= 19`, which are not exported; the diagonal
  `Tg{g}_{g-12}` pattern and the grade-19/20 predictions are
  `EMPIRICAL-PATTERN`, not theorems;
- that the rational witness is on the named unit-`k10` family — it has
  `k = 0` and is off it, and the first-order `k`-reachability I proved is not
  an existence statement;
- that `V34`'s "no sixth point" upper bound is independently verified — that
  one claim still rests on the frozen Singular run;
- anything about the off-family load-timing fan, source/landing coverage,
  the generic deck/square bridge, `G2-PSC`, any invoked `G2-BD`, cofinal
  degree/type control, Gate T, order two, maximum twelve, or JC2.

No repository file other than this one was written.  `jc2-lean` was not read,
entered, built, or modified.  No AWS state was changed, no web access was
made, and no Groebner/CAS computation was run locally; all local work was
exact `Fraction` and `Z[t]/(t^5-2)` arithmetic in `/tmp/opus5v34/`, seconds of
CPU and far under 1 GiB.
