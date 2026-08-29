# D43 essential-source coordinate bridge: hostile review

**Date:** 2026-08-28  
**Reviewer:** GPT-5.6 Sol, independent hostile lane  
**Scope:** fixed `B=84`, residue-A, `a00pp`, D43 source/NF interface  
**Verdict:** **REPAIR**

The source/NF split in
`xmodel/d43-common-integral-emitter-preflight-gpt56-20260828.md` is correct:
a source-defined D43 point does not require a common lift of the 509-element
modular Groebner basis, while equivalence with the banked NF presentation does.
The claimed coordinate obstruction, however, is substantially overstated.

The pristine source evaluator has 190 advertised directions, but eight of them
are causally invisible to every selected D43 row.  They are not unknown
eliminated coordinates and require no reconstruction.  Removing those eight
dummy directions leaves exactly 182 essential source coordinates.  The two
additional banked coordinates `uW1,uW2` are ordinary inverse-chart auxiliaries,
already governed by the exact equations `W1*uW1-1` and `W2*uW2-1`.  Thus there
is a clean exact 182-coordinate source model, or equivalently a 184-coordinate
chart extension with those two inverse equations.  The real source-existence
obstruction is now local generation/formal smoothness of the 184 source rows,
not a 190-to-184 reconstruction and not common provenance for all 34 parked
rows.

No claim below identifies this source model with the banked 218-row NF
presentation.  That stronger equivalence still needs the missing integral
membership traces.

## 1. Facts that pass unchanged

### 1.1 The advertised dimensions are correct

`cases/d43_char0_lift.py:349-383` constructs a `184 x 190` Jacobian: 180 tail
directions, eight fixed directions, and `alpha,beta`.  The same census is
recorded at `cases/d43_char0_lift.py:787-794`.

The banked presentation has 184 variables and 218 rows.  Its blocks are 34
parked, 95 old graph, and 89 late graph rows
(`cases/d43_full_family.py:343-380`, especially `:350-372`).

The existing comparison really does label only 182 of the banked columns and
assigns `None` to `uW1,uW2`
(`cases/d43_char0_lift.py:501-530`).  It then invokes the modular identity
`raw = NF + Q*parked` for its row-space conclusion
(`cases/d43_char0_lift.py:491-500,620-640`).  Therefore that routine is not an
integral presentation-equivalence certificate.  This part of the preflight is
confirmed.

### 1.2 Source existence and NF equivalence remain different tasks

The 509 reducers are prime-specific outputs consumed by
`cases/d43_reduce_modp.py:136-149`; the reducer replaces each raw coefficient
by its modular normal form at `:111-122`.  The banked graph construction then
collects only the variables occurring in those reduced rows
(`cases/d43_full_family.py:287-353`).

Consequently, proving that a common source scheme has a `Z_p` point can be done
without the 509 reducers.  Proving equality with, or transporting local
geometry from, the banked NF scheme still requires:

1. common exact provenance for the parked presentation if that presentation
   is retained;
2. the 509 reducer-to-parked membership identities; and
3. the 184 source-to-NF identities (including the separately handled D43
   x-side contribution).

The preflight's two-tier seal is therefore conceptually correct.

## 2. The eight alleged reconstruction directions are dummy directions

### 2.1 Exact identity of the complement

The omitted set is declared explicitly at
`cases/d43_char0_lift.py:44-46`:

```text
(tf1,39), (tf1,41), (tf2,39), (tf2,41),
(tg1,39), (tg1,41), (tg2,39), (tg2,41).
```

Here the second entry is the source offset `r`, not the absolute coefficient
level.  The source point converts a tail at absolute level `L` to offset
`r=L-32` (`cases/d43_char0_lift.py:149-151`), and the assembled-to-source map
does the same at `cases/d43_char0_lift.py:515-519`.  Hence these are precisely
the eight high coefficients at absolute levels 71 and 73.

A direct registry census using the committed `X2T` table
(`cases/d43_family2.py:56-80`) and either full 184-coordinate certificate gives:

```text
banked variables                                      184
banked variables other than uW1,uW2                  182
distinct source labels represented                   182
advertised source labels                              190
source-label complement                                 8
```

The complement is exactly the list above; there is no collision or additional
unmapped source label.

### 2.2 Exact support proof of invisibility

The eight columns are not merely zero at the displayed point.  The selected
184 source polynomials are independent of them.

The proof follows directly from the exact sparse source evaluator:

1. A tail with offset `r` enters a through-orbit factor in slot `r`
   (`cases/d43_char0_lift.py:137-165`, especially `:149-163`).
2. The same tail could enter an other-orbit factor only in slot `20+r`
   (`cases/d43_char0_lift.py:168-180`).  For `r=39,41`, these are slots 59 and
   61 and are discarded by the `<43` truncation at `:171-173`.
3. Sparse products add nonnegative slots and retain only totals below 43
   (`cases/d43_char0_lift.py:117-125,128-134`).  Apart from slot-zero factors,
   the smallest available positive source slot is 6.  Thus, through D43, a
   monomial containing one of these tails can occur only in its original odd
   slot 39 or 41; adding any positive slot puts it above 42.
4. Theta and eta differentiation do not change the slot, and the two Euler
   products only add slots (`cases/d43_char0_lift.py:253-265`).
5. Every selected row has even slot `S30[a]+6*j <= 42`.  This is the complete
   row registry asserted at `cases/eplus43.py:139-159`.

Therefore no selected D43 polynomial contains any of the eight level-71/73
variables.  Equivalently, the 190-coordinate zero locus is a product of the
essential zero locus with an affine 8-space in these dummy directions.  Setting
them to zero is harmless, but even the language "affine slice" is weaker than
the actual statement: the equations do not see them.

As a diagnostic only, an independently extracted copy of the exact
`source_rows` functions was evaluated at three unrelated coefficient/tail
assignments over `F_105337`; changing each of the eight directions from 0 to 1
or 2 changed zero of 184 rows in all 48 perturbations.  The proof is the support
argument above, not this sample.

This also explains the existing exact result.  Dropping precisely these eight
columns leaves rank 129, augmented rank 129, and a successful direct `p^2`
replay of all 184 source rows
(`cases/d43_char0_lift.py:734-757` and
`cases/d43_char0_lift_p105337.json:361-383`).  The constant name
`MISSING_RECONSTRUCTED_TAILS` is misleading; these are
`D43_INVISIBLE_HIGH_TAILS`.

## 3. The `uW` coordinates already have the clean exact bridge

The pristine source equations depend on `W1,W2`, not on inverse variables, so
returning `None` for `uW1,uW2` in the source-label map
(`cases/d43_char0_lift.py:508-519`) is correct rather than a loss of source
information.

The exact characteristic-zero chart rows are already stated as

```text
uW1*W1 - 1,
uW2*W2 - 1
```

in `cases/directionb_residual32_emit.py:50-54`.  They specialize literally to
parked rows 25 and 26 at both primes:

- `cases/d25fam_p105337_a00pp.ms:27-28`;
- `cases/d25fam_p105673_a00pp.ms:27-28`.

The source-point constructor independently verifies `uWi=Wi^(-1)` at
`cases/valuation_e2.py:257-265`.  Since each displayed `Wi` is a unit, adjoining
`uWi` with `Wi*uWi-1` is an etale graph extension and its lift is unique at
every `p`-adic precision.

Let `A` be the registered `Z_p` coefficient order and let `S` be the polynomial
ring on the 182 essential source coordinates.  A clean common source chart is

```text
T = S[uW1,uW2] / (W1*uW1-1, W2*uW2-1).
```

Pull the 184 pristine D43 rows into `T`; they do not involve either `uW`.
This is an exact 186-row/184-coordinate chart presentation (184 source rows
plus two chart rows), or simply the original 184-row/182-coordinate essential
source presentation before adjoining inverse bookkeeping.

No formula for the eight invisible high tails is required.

## 4. Do the 184 source rows suffice?

### 4.1 Yes, for the finite D43 source-existence question

The 184 pristine equations are the complete selected Euler residuals through
band 42 (`cases/d43_char0_lift.py:240-267` and
`cases/eplus43.py:150-159`).  A `Z_p` solution of these equations in the
registered source ansatz is already a characteristic-zero point of the finite
D43 source scheme.  It need not continue to satisfy an auxiliary modular
normal-form presentation used to find its residue-class seed.

Therefore the other 32 parked rows, the three/five compressed solve-back
blocks, and the 509 reducers are not logically required for **direct finite
D43 source existence**.  They remain useful for identifying the source model
with the banked component and for reusing banked calculations.

There is one implementation caveat.  The current integer `source_rows`
evaluator is the pure-y value path.  It is regression-compared with the full
operator at `alpha=beta=0` (`cases/d43_char0_lift.py:668-695`), and the present
`p^2` correction indeed has zero x-side correction because
`apply_correction` fails closed otherwise (`:422-463`).  A future unrestricted
182-coordinate Newton engine must incorporate the exact alpha/beta value-side
formula from `cases/eplus43.py:243-276`, or explicitly freeze
`alpha=beta=0` and recompute its rank and every lifting gate.  It must not use
the alpha/beta Jacobian columns with a value evaluator that silently discards
nonzero alpha/beta.

### 4.2 No, for the ultimate JC2 conclusion

A characteristic-zero point at finite D43 would settle only stage 2 of the
existing algebraization ladder.  Compatible points at all depths, an inverse
limit, convergence/algebraicity, global gluing, a polynomial Keller pair, and
the unbounded-scale conclusion all remain open.  Nothing here proves or
disproves JC2.

## 5. The true next obstruction is source-local smoothness

The essential 184-by-182 source Jacobian at the displayed point has rank 129.
The restricted first correction has rank equal to augmented rank and replays
modulo `p^2`, but that is only one successful correction.

Adjoining the two inverse variables and their chart equations raises the rank
exactly from 129 to 131: the source Jacobian has zero `uW` columns, while
`d(Wi*uWi-1)/d(uWi)=Wi` is a unit.  Hence the chart has tangent dimension

```text
184 - 131 = 182 - 129 = 53.
```

This already explains the reported rank 131/tangent dimension 53 without the
other 32 parked equations.  The assembled calculation records source rank 129,
combined rank 131, and tangent dimension 53 at
`cases/d43_char0_lift.py:563-640` and in the
`assembled_special_fiber_jacobian` block of
`cases/d43_char0_lift_p105337.json`.

What is still missing is one of the following equivalent-strength local
certificates for the source ideal:

1. choose a unit 129-by-129 source minor and prove that the remaining 55 source
   rows lie in the localization of the ideal generated by those 129 rows; or
2. prove the full source local ring has dimension 53 (the selected-minor local
   ring is regular of dimension 53, so no additional nonzero local equation
   can retain that dimension); or
3. give a direct formal-smoothness/right-inverse theorem that controls every
   higher obstruction.

Without such a certificate, rank 129 and one `p^2` correction do not invoke
Hensel for the overdetermined 184-row system.  Conversely, common provenance
for all 34 parked rows does not by itself address this source-local obstruction.

## 6. Smallest sound next artifact

Build a fail-closed `D43-ESS-SOURCE` certificate before any common-34 emitter
or AWS solve.  It should contain:

1. the exact 190-label registry, the eight-label invisible complement, and the
   182-label bijection to the non-`uW` banked header at both primes;
2. a machine-checked support/weight proof that the eight high tails occur in no
   selected source polynomial (not merely zero Jacobian columns at one point);
3. the two literal common chart rows and their exact two-prime specialization;
4. a serialized source correction and direct all-184 `p^2` replay, followed by
   the uniquely reconstructed `uW` values and an all-186 replay;
5. an exact 129-unit-minor certificate for the essential source Jacobian (and
   the automatic 131-minor after adjoining the chart rows);
6. a source-only obstruction adapter: solve the 129 pivot equations at
   increasing `p`-adic precision and project the remaining 55 residuals to the
   cokernel.  This is a fast discriminator; any nonzero obstruction is real,
   while repeated survival directs the heavy AWS lane toward localized
   syzygy/standard-basis certification.

Items 1-5 are small exact bookkeeping and should close the coordinate question
without heavy computation.  Item 6, and especially a symbolic local-generation
proof, is the actual mathematical frontier.  The common `26+3+5` emitter and
509/184 traces should proceed only as a parallel **NF-equivalence/reuse** lane,
not as a prerequisite for the direct source-existence lane.

## 7. Final hostile verdict

**REPAIR.**  Keep the preflight's source-existence/NF-equivalence separation,
but replace every assertion that an unknown 190-to-184
descent/reconstruction is load-bearing with the exact essential-source fact:

```text
190 advertised source directions
  = 182 essential directions + 8 D43-invisible affine directions,

184 banked coordinates
  = 182 essential source coordinates + 2 inverse-chart auxiliaries.
```

The coordinate bridge is clean.  Direct source existence should now attack
rank-129 local generation/formal smoothness.  Presentation equivalence remains
open and still requires the integral trace package.

## 8. Audited-source hashes

```text
6b873ac1b7bf9cb8513876a13ccf8b5ffe6c845f247b40972c3d023c0a97762a  cases/d43_char0_lift.py
92ea21461ad86274473b984fdbf64c4103f18f320e4e60d0aec430ab29999231  cases/build_tails43.py
e964d2b467f76696f16ccef505f6f66cce7d68e722004bb1a70b6e1cf4f21e7c  cases/d25_eplus.py
c1a858fbe53c291038b0386c124dbfd4bc79400eedc6b9d5d49a4088736d08f8  cases/valuation_e2.py
1ac2f37245fd4f9770cf6172ecde994e5394171712d4dffd25f87029531b4f82  cases/directionb_residual32_emit.py
b846ff241167ee0e065287dff9bd4847d5fd73c3657f7a7db05f52e4ac615596  cases/d43_full_family.py
8c0f7fd3ea1efb54293036e1caa481519682251ec554e8dac4cb254b4f2ca013  cases/d43_family2.py
6e50a00f651b4e6ea0a5666d7507c499ff86e86d7eed9c0c17cd7add247eec7c  cases/d43_full_certificate_p105337.json
81eae319fb02ade7369be0c192162925bf63ebc52edc97a99348acb3524b9f3c  cases/d43_char0_lift_p105337.json
```

No AWS job or heavy local computation was run, and no canonical campaign file
was edited.
