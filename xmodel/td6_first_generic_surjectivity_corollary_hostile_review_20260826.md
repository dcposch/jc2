# Hostile review: TD6 FIRST generic-surjectivity corollary

Inspection only of the charged corollary and the three named
hostile-reviewed inputs.  No producer Python, no Flint, no Singular, no
Sage, no msolve, no Lean, and no other substantive computation.
SHA-256 values below were recomputed from on-disk bytes with
`shasum -a 256` and compared by exact equality.  The only linear
algebra is the square-zero expansion written by hand.

Charged surface (hash matched on disk):

```text
b1352aa1c9e218cf7ee5df7d6c03ff99e603a86f57a24cb391dbba102a2579c1
  xmodel/td6-first-generic-surjectivity-corollary-20260826.md
```

Consumed, not re-proved (hashes matched on disk, and match the pins
inside the corollary):

```text
3f62b23d43e134eedb53ecd6e78511ca10606f46e6c0007d510596d9516bd93b
  xmodel/td6_v82s2_kernel_dead_first_hostile_review_v2_20260826.md
  standalone verdict CONFIRMED

a3599e65f88015f60a3131572716affda748d8dc5963e3648bb35842246a1861
  xmodel/td6_v78bc_all_q_p12_hostile_review_v3_20260826.md
  standalone verdict CONFIRMED

dfac352887f645a9dd1f03a32b4701372b32de3a445bfd496c74109e64381ebb
  xmodel/td6_v81c_dead_transport_rank_hostile_review_20260826.md
  standalone verdict CONFIRMED
```

The seven load-bearing charges are re-audited from those four texts.

---

## Findings

**1. [Confirmed] All four hashes match.  The packed generic FIRST
presentation is 132 variables, exactly 38 nonzero packed equations,
rank 38, and has no dependent FIRST row after original-row transport
replay.  The integer 38 is packed Dual-GE row/pivot count, not a
historical unreduced degree-slot cardinality.**

Independently recomputed SHA-256 values equal the four charged pins
byte-for-byte.  The two V78/V82S2 fences inside the corollary carry a
trailing period after `.md`; the V81C fence does not.  That is citation
punctuation, not a filename, and does not change the hashes.

From the CONFIRMED V82S2 review, after the frozen rank-3470 transport:

```text
transport_rank=3470/3602;free=132
len(pivots) + 132 == nf + ng
parameterize(132, first_rows)     # V82 Dual GE, pack("X-2", ...)
len(first_pivots) == 38 and len(free94) == 94
first_rank=38/132
first_dependent_count=0
```

Pivots are chosen only on nonzero base values.  Every dependent row
and every surviving pivot is reconstructed from original packed
`pack("X-2", first_band_polynomials(f1,g1))` source rows.  With
`first_dependent_count=0`, `dependent_coordinates` is empty.  Hand
arithmetic: `38 + 94 = 132` and `3602 - 3470 = 132`.  The undeformed
first echelon is the same object V78 already recorded as rank
`38/132`, dependent count 0, on the same packed first rows.

Distinction demanded by the charge:

- Historical nominal degree slots are the unreduced `first_band_polynomials`
  degree list (and, in sibling bands, loops such as `range(40)`).
  `pack` omits a degree when the row vanishes.  That slot cardinality
  is not an equation count and is not used as one in V82S2 or V78.
- Packed nonzero equations are the Dual-GE rows of `first_rows`.
  Dual GE on this lineage never selects an `eps`-only pivot.  Zero
  packed rows are not equations.  Nonzero packed rows that fail to
  become pivots are dependents.  The frozen counts are 38 pivots and
  0 dependents, so there are exactly 38 nonzero packed equations,
  they are linearly independent over `K`, and the base map is
  `A0 : K^132 -> K^38` of rank 38.
- A 28-row figure appearing in older P12 original-row identities is
  multiplier support among these 38 rows, not a second equation
  count.  It is not cited by the corollary and is not a FIRST
  presentation.

Transport original-row replay is V82S2 Finding 2: every one of the
3,470 original transport pivot rows is rebuilt as
`A0 x' + A'_LEVEL x0 = 0` and asserted `ZERO_FORM`, with
`replay_count == len(pivots)` and `assert not compatibility`, before
the FIRST pack is formed.  Absence of a dependent FIRST compatibility
row is V82S2 Finding 3 (`first_dependent_count=0`), not a silent
reuse of the transport leftover emptiness.

The corollary’s opening therefore matches the reviewed presentation:
132 unknowns after the 3,470-row transport echelon, 38 packed
nonzero FIRST equations, rank 38, cokernel zero, exact source replay.

**2. [Confirmed] The derivative equation is `A0*x1 = b1 - A1*x0`.
Surjectivity of `A0` solves it for every right-hand side in `K^38`.
That is exactly vanishing FIRST cokernel/conormal and does not use
an axis-specific identity.**

Write, as the corollary does,

```text
A = A0 + eps*A1,     b = b0 + eps*b1,     x = x0 + eps*x1,
eps^2 = 0,           A0*x0 = b0,
```

with `A0, A1` of size `38 x 132` over `K` and `b0, b1, A0*x0` in
`K^38`.  Expand:

```text
A*x = (A0 + eps*A1)(x0 + eps*x1)
    = A0*x0 + eps*(A0*x1 + A1*x0)
```

because `eps^2 = 0`.  The equation `A*x = b` is therefore equivalent
to the given base equation together with

```text
A0*x1 + A1*x0 = b1,
A0*x1         = b1 - A1*x0.
```

This is the same first-order identity V81C/V82S2 write at transport
as `A0 x' + A'_LEVEL x0 = 0` and that Dual GE reduces at FIRST by
the `lambda' A` term.  Omitting `A1*x0` would be a different
linearization; V81C/V82S2 omission controls already refuse that
shortcut on `d10` and `d15`, and V78 lambda-prime support is 14 on
every licensed q-coordinate.  The corollary is right to keep the
term.

`A0 : K^132 -> K^38` has rank 38, hence is surjective, hence
`coker(A0) = 0`.  For every pair `(A1,b1)` of these sizes the
right-hand side `b1 - A1*x0` lies in `K^38`, so a solution `x1`
exists.  No column of `A1` and no particular axis identity enters.
The 22 q-FIRST zeros and the two dead-FIRST zeros are instances, not
premises.

Project language: FIRST conormal is the leftover pairing of a
source column against `coker(A0)`.  That pairing is the zero map
precisely because the cokernel is zero.  This is not a claim that
the geometric conormal sheaf of the 94-dimensional FIRST solution
scheme in the 132-chart vanishes; that sheaf has rank 38.  The
corollary’s own gloss, “no FIRST compatibility functional exists:
`coker(A0)=0`”, is the correct identification.

Existence of some base solution `x0` for the actual undeformed
`b0` is the same surjectivity, not a hidden V76 citation.  The
affine fibre has dimension `132-38 = 94`, matching `free94`.

**3. [Confirmed] “Every well-typed perturbation” is restricted to
square-zero deformations of this same licensed 38-by-132 FIRST
presentation, including direct, transported, and varying-matrix
terms.  The wording does not license a new equation, chart,
unlicensed source modulus, or nonlinear deformation.**

The corollary statement says “every well-typed square-zero
perturbation of this same source presentation”.  The firewall
paragraph then defines that phrase:

- same licensed FIRST row/column presentation;
- all of the direct, transported, and varying-matrix (`A1*x0`) terms;
- not a new chart, not a new equation, not an unlicensed source
  coefficient, not a perturbation that changes the presentation, not
  a nonlinear deformation.

The linear-algebra proof of Finding 2 actually solves the derivative
equation for every `(A1,b1)` of size `38 x 132` / `38`.  “Well-typed”
is a source-scope restriction of that argument, not an enlargement.
In particular it does not add `q15` (target-shear gauge), `q1`/`q25`
(frozen q-boundaries), `d5`/`d17`, zeta-as-a-new-dead-axis, or any
previous/pole/current row.

The nine dead axes `d6..d9,d11..d14,d16` that fail transport are not
perturbations of this 132-chart presentation: V81C leftover on those
columns is nonzero, so they do not remain on the transport-free
FIRST chart at order `eps`.  The corollary does not sneak them in.
It also does not resurrect them at FIRST.

A 24-fold square-zero ring `K[eps_i]/(eps_i eps_j)` is still
first-order and, by the same `A0` surjectivity, would still have
vanishing FIRST leftover.  The corollary never claims to have run
that ring: its displayed perturbation is a single `eps`.

**4. [Confirmed] V78 and V82S2 are ancestry/omission controls for
honest insertion of the q-columns and of `d10,d15`.  Full row rank
is the reason the final FIRST conormal vanishes.  Neither control
is used to infer a stronger source inventory.**

The corollary’s own division of labour is the required one:

- V78 and V82S2 prove the advertised perturbations were inserted,
  that direct/source columns are nonzero where claimed, that
  omission changes those columns, and that the varying echelon was
  replayed.
- They are “not the mathematical reason the final FIRST conormal is
  zero.  The reason is full row rank.”

That matches V82S2 Finding 3 (raw first-source columns 1,108 and 739
entries, omitted digest the empty SHA `e3b0c442…`, rank `38/132`,
dependent count 0) and V78 Finding 5 (direct-q-prime omission, 14
lambda-prime rows on every licensed exponent, `first_all_q_pivot_source_replay=true`).
The axis calculations remain load-bearing as negative controls
against a phantom zero column.  They are not used as a census.

Inventories left untouched:

- V78: licensed q-support is exactly `{q2,...,q14,q16,...,q24}`,
  with `q15` gauge.  The corollary does not add a 23rd q.
- V81C: licensed dead-stretch support is `d6..d16`.  The corollary
  does not add `d5` or `d17`, and does not treat zeta as a twelfth
  dead coordinate.
- Combined licensed source axes remain 33.  The corollary’s
  “every well-typed” class is perturbations of the packed FIRST
  map, not a 34th source modulus and not a claim that FIRST was
  executed on all 33 axes.

Fail-closed test: if the text had inferred, from V78/V82S2 insertion
honesty, a larger FIRST source inventory or a 33-axis FIRST table,
this charge would reject.  It does not.  Rank of `A0` is a property
of the undeformed packed rows (pivots on base values) and does not
need those 24 derivative columns except as Dual passengers.

**5. [Confirmed] Generic FIRST surjectivity plus reviewed V81C
transport rank nine with kernel `Q22+d10+d15` implies that exactly
those 24 directions survive transport plus FIRST.  This is a logical
columnwise composition, not a one-ring 24-axis execution.**

V81C, already CONFIRMED: on the 33 licensed axes, transport leftover
has rank nine and kernel `span(q2..q14,q16..q24,d10,d15)`, dimension
`22+2 = 33-9 = 24`.  Those 24 directions remain on the 132-chart, so
they are well-typed perturbations of the packed FIRST presentation.
Finding 2 therefore gives them zero FIRST leftover: FIRST removes no
vector from that kernel.

The complementary nine dead transport columns are already nonzero at
transport.  FIRST cannot put them back onto the 132-chart.  The
cumulative transport-plus-FIRST gate therefore still has kernel
exactly those 24 directions.

This is strictly stronger than, and consistent with, V82S2 Finding 6,
which obtained the same 24-dimensional FIRST leftover zero by
concatenating V78’s 22 empty q-FIRST columns with V82S2’s two empty
dead-FIRST columns.  The present reason is `coker(A0)=0` on the
whole 38-by-132 map, of which those 24 columns are instances.

The corollary’s wording is “Combining this corollary with the
separately reviewed V81C transport theorem shows…”.  That is logical
composition of two already reviewed maps, the same assembler pattern
V81C and V82S2 already accepted.  It is not a 24-fold one-ring Dual
run, not V82 `cumulative_table` / `configure_qd` with all `Q_PRIME`,
and not a claim that V82S2 recomputed V78’s q-FIRST columns.  The
displayed linearization has a single `eps`.  Mixed q-dead second
derivatives remain square-zero and vanish, so column concatenation
is the first-order composition.

The corollary body does not spell out the one-ring refusal in the
composition paragraph.  The refusal is already present in the
consumed V82S2 theorem and is implied by the single-`eps`
perturbation plus the later “neighborhood or family” firewall.  It
is not a load-bearing hole.  The surviving theorem below records the
distinction explicitly.

**6. [Confirmed] The theorem is over `K = E(C,V,U)`, or on the
source-legal open where a maximal 38-minor of `A0` is nonzero.  It
says nothing on the complement until raw fibres are rebuilt.  It
does not identify that open with `D(U*H*B3)`.**

The corollary never writes `D(U*H*B3)`, `U*H*B3`, `H = C-3U^2`, or
`B3`.  The rank-drop paragraph is:

- generic-field statement over `K = E(C,V,U)`;
- equivalently, the open where the source chart is legal and some
  38-by-38 minor of `A0` is nonzero;
- no surjectivity on the rank-drop divisor, nor after specializing
  a denominator/pivot factor to zero;
- those fibres need raw reconstruction; cokernel can grow.

That is exactly the charged firewall.  A matrix of rank 38 over a
field is equivalent to some maximal minor being a nonzero element
of that field; the corresponding principal open is the correct
constructible locus, and is not named as `D(U*H*B3)`.

Consumed facts that must not be silently collapsed into that open:

- V78 FIRST-conormal denominator is the unit `(1, [])`.  V78’s
  `D(U*H*B3)` is the P12-column LCM locus, inherited only for the
  consumed zero q-columns, and is not a FIRST rank-drop description.
- V82S2 FIRST-axis denominator is the unit `1`; V82S2 already
  refuses to treat the FIRST statement as “merely on `D(U H B3)`”.
- V81C sentinel diagonal has denominator `1`; generic-table
  denominators that occur at transport are `{1, U, C-3U^2}`.  Those
  are transport facts, not a FIRST open.

The corollary does not claim a denominator-cleared atlas, and does
not assert that the 38-minor is a unit in `Q[C,V,U]`.  Specializing
a pivot lead or a transport-chart denominator to zero is exactly
the complement it defers.

**7. [Confirmed] The strongest exact promotion is the charged
corollary as written.  No load-bearing repair.  All required
firewalls hold.**

Previous / pole / current, second order, Kuranishi/Fitting zero
loci, a neighborhood or family, the full TD6 source, SP-2, and JC2
are all refused in the final paragraph.  Operational redundancy of
further isolated FIRST-axis runs is restricted to “the same generic
rank-38 presentation”, with the next information allowed to occur
at previous/pole/current, on a rank-drop fibre, or at higher order.
P12/current remains a different stage: V78’s degree-14 P12 cutoff
is not a FIRST statement and is not declared redundant.

---

## Load-bearing defects

None.

## Custody and prose recommendations (not load-bearing)

These do not disturb the verdict.

1. Two of the three consumed-review fences inside the corollary put
   a period after `.md`; the V81C fence does not.  Drop the periods
   so a later hash pin cannot be misread as a filename.

2. The composition paragraph can afford the one sentence V82S2
   already uses: the 24-direction survival is a logical columnwise
   composition with V81C, not a one-ring 24-fold FIRST run.  Finding
   5 already reads the present text that way.

3. One explicit clause that 38 is packed Dual-GE nonzero rows, not
   an unreduced `first_band_polynomials` degree count, would make
   Finding 1’s distinction visible in the corollary itself.  The
   word “packed” is already there.

4. Status still says review of this formulation is pending.  That
   is expected of the charged file and is not edited here.

---

## Independent discharge

- **Four SHA-256 pins** are discharged by `shasum -a 256` on the
  four on-disk files, equal to the charged strings.
- **132 / 38 / rank 38 / no FIRST dependent** are discharged by
  V82S2 Finding 3 plus V78 Finding 5, together with
  `38+94=132` and `3602-3470=132`.  Packed-versus-slot is discharged
  by Dual GE’s 38 pivots and 0 dependents on `pack("X-2", ...)`,
  not by any degree-loop cardinality.
- **Original-row transport replay** is discharged by V82S2 Finding 2
  (`replay_count == 3470`, `assert not compatibility`), which is
  prior to the FIRST pack.
- **Derivative equation and surjectivity** are discharged by the
  hand expansion in Finding 2, using only `eps^2=0` and rank 38.
- **Well-typed scope** is discharged by the corollary’s own
  firewall paragraph, read against V78/V81C inventories.
- **Ancestry versus rank** is discharged by the corollary’s
  explicit sentence that V78/V82S2 are not the reason the conormal
  vanishes.
- **24-dimensional cumulative kernel** is discharged by V81C’s
  rank-nine kernel plus Finding 2, as columnwise composition, not
  by a 24-axis ring.
- **Rank-drop / non-identification with `D(U*H*B3)`** is discharged
  by the absence of that open from the corollary and by the maximal
  38-minor locus it does name.

---

## Strongest exact theorem that survives

Let `K = E(C,V,U)` be the generic symbolic-center field of the fixed
source-typed A3/F1 TD6 slice.  After the 3,470-row transport
echelon, the packed FIRST presentation
`pack("X-2", first_band_polynomials(f1,g1))` is a linear map

```text
A0 : K^132 -> K^38
```

of rank 38: 132 transport-free unknowns, exactly 38 nonzero packed
equations, 0 dependent FIRST rows, 94-dimensional affine fibre.
The integer 38 is that packed Dual-GE count, not a historical
unreduced degree-slot count.  Equivalently `coker(A0)=0`, so there
is no FIRST compatibility functional.  This is a statement over
`K`, or on the source-legal open where some 38-minor of `A0` is
nonzero.  It is not a statement on the rank-drop complement, and
that open is not `D(U*H*B3)`.

For every square-zero deformation of this same 38-by-132
presentation,

```text
A = A0 + eps*A1,   b = b0 + eps*b1,   x = x0 + eps*x1,
eps^2 = 0,         A0*x0 = b0,
```

the order-`eps` equation is `A0*x1 = b1 - A1*x0`.  Surjectivity of
`A0` solves it for every well-typed `(A1,b1)`, including the
varying-matrix term.  In the project’s leftover language the FIRST
conormal of every such perturbation vanishes.  No axis-specific
identity is used.  The class does not include a new chart, a new
equation, an unlicensed source coefficient, a changed presentation,
or a nonlinear deformation.

Reviewed V78 q-axis and V82S2 `d10,d15` runs remain the ancestry
and omission controls that those columns were honestly inserted.
They are not a larger source inventory and are not the reason the
conormal is zero.

Composing with the separately reviewed V81C theorem that the
33-axis transport leftover has rank nine and kernel
`span(q2..q14,q16..q24,d10,d15)` of dimension 24: FIRST removes no
vector from that kernel, and does not restore the nine nonzero dead
transport columns.  Exactly those 24 directions survive the
cumulative transport-plus-FIRST gate.  This is logical columnwise
composition of two reviewed maps.  It is not a one-ring 24-fold
square-zero FIRST execution.

Nothing is claimed about previous, pole, current, second order,
Kuranishi/Fitting zero loci, a neighborhood or family, the full
TD6 source, SP-2, or JC2.  Further isolated FIRST-axis computations
on this same generic rank-38 presentation are redundant.  The next
information can first occur at previous/pole/current, on a
rank-drop fibre, or at higher order.

---

CONFIRMED
