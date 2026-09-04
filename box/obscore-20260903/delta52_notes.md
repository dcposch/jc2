# Certificate slice B: `(99,66)`, `delta=5/2`, stage-8 unit

Date: 2026-09-04 UTC

Scope: only the terminal row `stage8_G_local16_coord0`; no claim about the
other two kills, no ledger edit, and no use of the running residue-formula
lane.  All equalities below are exact over `Q`.

## Result

The charged normal form

```text
stage8_G_local16_coord0 = 64
```

has a much smaller causal slice than the phrase "after seven stage-8 pivots"
suggests.  Starting with the terminal pole row before cumulative joint
substitution, its post-outer-`D1` ancestry contains the 35 earlier Jacobian
pivots from stages 1--4, partitioned `9+9+9+8`.  It contains none of the seven
new degree-155 pivots at stage 8.  Solving the filtered 43-by-43 `B1` block
then prunes those 35 rows to six.  The support-minimal certificate within that
filtered post-`D2` core has seven source rows total: one pole row and six
Jacobian rows.  Every outer-`D1` multiplier is exactly zero.

The literal identity is

```text
1 = (1/64) stage8_G_local16_coord0
  - (17371*K2c_5_21*u + 145*K2c_7_19 - 145*K2c_7_20
     + 145*K2c_7_21 - 6525*c + 1433412*u^2*v - 190680*v)
       / 8017920 * stage1_J_d162_k35
  - (29*K2c_5_21*u + 2088*u^2*v - 240*v)
       / 41760 * stage1_J_d162_k36
  + (29*K2c_6_20 - 29*K2c_6_21 + 2436*u^3
     + 27864*u + 6264*v^2)
       / 1553472 * stage2_J_d161_k35
  + (u/174) * stage2_J_d161_k36
  - (K2c_5_21 + 72*u*v)
       / 51840 * stage3_J_d160_k35
  + (1/6264) * stage4_J_d159_k35.
```

The equality is in the declared post-outer-`D2`, common-`h3` branch quotient.
It remains an identity after adjoining the localization row with zero
multiplier:

```text
1 = certificate_above + 0*(Zc*c - 1),       c != 0.
```

There is no symbol or nonvanishing factor named `J0` in the charged
`(99,66),delta=5/2` ring.  Consequently a `J0 != 0` factor cannot honestly be
inserted here.  The certificate does not divide by `c`; its `c != 0` wrapper
also has coefficient zero.

Verdict for this slice:

```text
CERTIFIED[POST-D2, DECLARED-COMMON-h3-BRANCH, 7 ROWS]
OPEN[PRE-D2-MULTIPLIER-LIFT-NOT-SERIALIZED]
OPEN[CHARGED-PRE-MAJOR-INCIDENCE-MULTIPLIERS-NOT-SERIALIZED]
```

## 0. Custody and source boundary

Before analysis, the lane receipt
`xmodel/two-place-obstruction-core-sol56-20260903.run.v2` was parsed
mechanically.  `awk` paired each indexed `charged_input_<i>_sha256` field with
the same indexed `charged_input_<i>_basename`, prefixed the receipt's frozen
input directory, and streamed the resulting 16-entry manifest to
`sha256sum -c`.  All 16 entries returned `OK`; no digest was retyped.

The charged stage-8 report identifies the row and the integer normal form at
`/tmp/jc2-lane.C9HiZU/inputs/g9966-delta52-stage8-sol56-20260903.md:5-13`,
specifies the pole and degree-155 stage-8 bands at `:88-97`, lists the seven
new pivots at `:108-124`, and states the exact localization at `:130-158`.
The completed static JSON independently records 66 cumulative pivots at
`box/g9966s8-20260903/runs/delta52/stage8.json:48-53`, the first two earlier
pivots at `:54-64`, the relevant stage-4 pivot at `:217-220`, the seven new
pivots at `:408-449`, and the residue at `:451-458`.

The replay script is
`box/obscore-20260903/delta52_certificate.py`.  It verifies the static stage-8
JSON and clean-room engine files against their own manifests before importing
them.  No accepted ledger, charged source, or prior report was modified.

## 1. The honest DAG boundaries

The word "touched" has three different meanings here; collapsing them would
overcount the certificate.

| boundary | pole | Jacobian | outer `D1` | incidence | total | status |
|---|---:|---:|---:|---:|---:|---|
| after common-`h3`, outer `D2`, outer `D1` | 1 | 35 | 0 | 0 | 36 | exact quotient ancestry |
| lift through reduced `D1` pivot DAG | 1 | 35 | 2 | 0 | 38 | exact reduced-step DAG |
| lift the `D1` zero fact to original `D1` row support | 1 | 35 | 7 | 0 | 43 | exact raw-row support |
| support-minimal Schur core, post-`D2` | 1 | 6 | 0 | 0 | 7 | exact certificate |
| common-`h3` dependency of the remaining `K2^2` constant part | 1 | 6 | 0 | 11 | 18 | exact dependency count; charged multipliers not serialized |
| literal support-minimal pre-`D2`, pre-major certificate | -- | -- | -- | -- | -- | typed `OPEN` |

The eight weight-93 `B1` `D1` rows were all processed by the chronological
outer eliminator.  They are audited prerequisites, but they are not eight
ancestors.  In the reduced pivot DAG only `B1_D1_s0_k6` and
`B1_D1_s0_k7` are reached.  When the reduced `B1c_3_21=0` fact is expressed
in the original row basis, seven rows have nonzero multipliers.  Finally, in
the seven-row Schur certificate even those seven disappear: the pole/Jacobian
combination cancels `B1c_3_21` before an outer row is needed.

### 1.1 Terminal before the joint substitutions

After the `D2` projector but before outer `D1`, the raw pole row has 136
monomials and 36 `B1` coordinates.  They occupy levels

```text
r=0: q=24..32  (9)
r=1: q=23..31  (9)
r=2: q=22..30  (9)
r=3: q=21..29  (9).
```

Outer `D1` removes `B1c_3_21`, leaving 135 monomials and 35 `B1`
coordinates.  Recursively following precisely the pivot variables present in
that row gives

```text
stage 1: 9 Jacobian pivots, t^1, degree 162
stage 2: 9 Jacobian pivots, t^2, degree 161
stage 3: 9 Jacobian pivots, t^3, degree 160
stage 4: 8 Jacobian pivots, t^4, degree 159.
```

Thus the deepest Jacobian `t`-power in the ancestry is 4.  The pole row itself
is the `s^16` coefficient and its construction can use `t^8`, since `t=s^2`.
These are different filtration depths.

The charged Q-star reducer scans only pure-linear variables with a nonzero
rational coefficient and resolves substitutions exactly; see frozen
`band_engine.py:191-239`.  Its stage convention and cumulative row builder
are at `band_engine.py:666-723`.  The independent engine supplies the same
exact rational reducer at
`box/g9966indep-20260903/indep_engine.py:135-177` and the low-band factored
Jacobian at `:279-293`.  The independent report confirms the joint pivot
sequence `0,9,9,9,8,8,8,8,7` at
`/tmp/jc2-lane.C9HiZU/inputs/g9966-independent-engine-opus5-20260903.md:24-29`
and explains the `B1`-linear mechanism at `:295-314`.

### 1.2 The seven new stage-8 pivots are not causal ancestors

The new rows pivot `B1c_7_19,...,B1c_7_25`, with coefficients

```text
675, 576, 477, 378, 279, 180, 81.
```

Neither the raw terminal row nor any recursively required earlier pivot RHS
contains a level-7 `B1` coordinate.  The script checks all seven variables
against the terminal dependency closure and obtains zero intersections.
Their chronological occurrence before the reported residue therefore does
not make them members of this certificate slice.  This agrees with the
charged table at frozen stage-8 report `:108-124` and the independent
row-for-row table at independent report `:283-293`.

## 2. Exact lift of the `B1` outer-`D1` zero fact

The retained weight-93 positions, ordered here by decreasing `q`, are

```text
(r,q)=(3,21),(7,18),(11,15),(15,12),
      (19,9),(23,6),(27,3),(31,0).
```

In chronological lexicographic elimination, the two reached reduced steps
are exactly

```text
B1_D1_s0_k6:  coefficient 5103 on B1c_3_21,
               B1c_3_21 = -B1c_7_18/7;
B1_D1_s0_k7:  coefficient -2187/7 on B1c_7_18,
               B1c_7_18 = 0.
```

These are the two reduced-pivot nodes.  To avoid treating a reduced row as an
original incidence, the script also solves the transpose of the original
eight-by-eight binomial row matrix.  The literal source-row equality is

```text
B1c_3_21 =
    (374/19683) * B1_D1_s0_k1
  - (20/729)    * B1_D1_s0_k2
  + (166/6561)  * B1_D1_s0_k3
  - (112/6561)  * B1_D1_s0_k4
  + (55/6561)   * B1_D1_s0_k5
  - (2/729)     * B1_D1_s0_k6
  + (1/2187)    * B1_D1_s0_k7.
```

The multiplier of `B1_D1_s0_k0` is exactly zero, hence the raw support count
is seven, not eight.  The source construction of these binomial rows is
`box/g9966indep-20260903/indep_engine.py:198-213`; the charged construction
is frozen `band_engine.py:420-470`.  The global report distinguishes the
retained `D1` rows from the `D2` deletion and gives all raw/rank counts at
`/tmp/jc2-lane.C9HiZU/inputs/g9966-global-band-sol56-20260903.md:110-140`.

## 3. The filtered obstruction map and Schur complement

Let `x` be the 43 `B1` coordinates appearing in the original rows, let `R`
be the column of 43 source equations formed from the eight weight-93 `D1`
rows followed by the 35 stage-1--4 Jacobian rows, and write

```text
R = A*x + r0,
P = ell^T*x + p0,
```

where `P=stage8_G_local16_coord0` before any of these substitutions.  The
script constructs `A` over the coefficient ring, verifies that it is a
43-by-43 invertible matrix, and solves

```text
alpha = A^(-T) ell,
S = P - alpha^T R = 64.
```

This is the Schur complement of the filtered `B1` obstruction block.  The
dual vector is unique.  Its first eight coordinates, belonging to all outer
`D1` rows, vanish.  Among its 35 Jacobian coordinates only these six are
nonzero:

```text
stage1_J_d162_k35, stage1_J_d162_k36,
stage2_J_d161_k35, stage2_J_d161_k36,
stage3_J_d160_k35, stage4_J_d159_k35.
```

This proves support-minimality within the 43-row filtered core: deleting any
row with a nonzero unique dual coefficient destroys this representation.  It
does not claim a globally minimal certificate in an unavailable pre-`D2`
presentation.

The replay includes a discriminating negative control.  It replaces

```text
stage4_J_d159_k35  by  stage4_J_d159_k35 + B1c_3_22
```

while retaining the extracted multipliers.  The purported identity then has
error `B1c_3_22/6264`, so it is not 1.  This establishes that the row content,
not only its label or the final number 64, is being checked.

## 4. Incidence, major-`h2`, outer, and bridge provenance

### 4.1 Why the incidence counts are 17 and 11

These numbers answer different questions.

* The raw terminal pole row before the hard-coded common-`h3` substitution
  contains 17 `Hc` variables.  Recursive closure in the 20-row clean-room
  incidence eliminator reaches 17 pivots.  This is a dependency audit of the
  unpruned pole row.
* After the six Jacobian rows cancel the `B1`-linear part, the surviving
  constant component is the local-coordinate-zero part of `K2^2`.  Before
  common-`h3` reduction it has 230 monomials and ten direct `Hc` variables;
  one RHS adds `Hc_5_6`, so the recursive closure has 11 incidence pivots.
  Exact reduction gives 64.

The 11 row labels are

```text
h3_s2_pi^0,  h3_s9_pi^1,  h3_s16_pi^2,
h3_s4_pi^0,  h3_s11_pi^1, h3_s18_pi^2,
h3_s6_pi^0,  h3_s13_pi^1, h3_s20_pi^2,
h3_s10_pi^0, h3_s17_pi^1.
```

The other six rows in the raw-terminal closure are

```text
h3_s8_pi^0, h3_s15_pi^1, h3_s12_pi^0,
h3_s19_pi^1, h3_s14_pi^0, h3_lead_pi^1.
```

`Hc_11_0` is in neither closure.  The independent report's no-ODE control
states that dropping `Hc_11_0=0` leaves the residue exactly 64 at
`/tmp/jc2-lane.C9HiZU/inputs/g9966-independent-engine-opus5-20260903.md:109-119`
and `:358-366`.  Hence no effective `T2/T3` bridge row is touched.

The clean-room source defines the common-`h3` series and branch substitution
at `box/g9966indep-20260903/indep_engine.py:26-133` and its incidence rows at
`:179-196`.  The charged engine instead hard-codes the branch map at frozen
`band_engine.py:257-280`; it does not serialize row multipliers that lift that
map back to the source incidence rows.  The replay therefore promotes the
counts and the normal form, but marks the literal charged pre-major multiplier
certificate `OPEN` rather than manufacturing it.

### 4.2 The integer 64 depends on common-`h3`, not on the seven `h2-D1` pivots

Before common-`h3` reduction the `K2^2` component is not a constant: it has
the 230 terms just described.  Its reduction through the 11-row incidence
closure is 64.  Thus the numerical constant does depend on the declared
common-`h3` leader substitution.

By contrast, none of the seven major-`h2` pivot variables occurs in the pole
row or the 43-row obstruction core:

```text
K2c_11_16, K2c_15_13, K2c_19_10, K2c_23_7,
K2c_27_4, K2c_10_17, K2c_14_14.
```

Therefore the `h2-D1` row count in this DAG is zero.  Some unpivoted `K2c`
symbols remain in certificate multipliers, as displayed in the identity;
they are coefficient-ring elements and cancel without specialization.  The
charged major builder and its seven chosen pivots are frozen
`band_engine.py:307-389`, and the completed JSON records them at
`box/g9966s8-20260903/runs/delta52/stage8.json:475-530`.

### 4.3 Outer `D2` zero facts and the explicit `A2/A3/B2` test

The exact global `D2` coordinate projector has 5,598 zero rows:

| family | zero-coordinate rows |
|---|---:|
| `A2` | 1,386 |
| `A3` | 2,442 |
| `B1` | 384 |
| `B2` | 1,386 |

The sum and post-projector size are recorded in the static JSON at
`box/g9966s8-20260903/runs/delta52/stage8.json:1096-1104` and in the frozen
global report at `:119-140`.  This is an exact global prerequisite count, not
the size of a support-minimal certificate slice.

After this projector, `A2` and `B2` can start only at coefficient level
`r=21`, and `A3` only at `r=53`; the normalized contributions enter one
`t`-power later.  Every row in this slice is at `t<=8`.  The script enumerates
the free symbols of the pole and all 43 obstruction rows and finds no live
`A2c_*`, `A3c_*`, or `B2c_*` coefficient.  The source-covered low-band
identity and these onsets are stated at independent report `:150-175`; the
charged construction is frozen `band_engine.py:392-512`.

The accepted JSON and charged engine retain the projector and the resulting
rows, but not a row-multiplier map from this certificate back through all
5,598 coordinate deletions.  Accordingly the number of `D2` zero facts in a
support-minimal literal pre-`D2` certificate is

```text
OPEN[PRE-D2-MULTIPLIER-LIFT-NOT-SERIALIZED].
```

It would be a fallacy to report 5,598 as the slice size: that is the whole
projector.  It would also be a fallacy to report zero: absence of live outer
variables in the quotient does not reconstruct pre-projector multipliers.

### 4.4 No bridge row

There is no `T2` or `T3` label in the obstruction rows, no `Hc_11_0` in either
incidence closure, and the no-ODE clean-room control keeps 64 unchanged.
Hence the number of touched bridge rows is exactly zero.  The broader bridge
remains open, as the charged stage-8 report says at
`/tmp/jc2-lane.C9HiZU/inputs/g9966-delta52-stage8-sol56-20260903.md:182-198`.

## 5. Replay

Run from the repository root:

```sh
timeout 1800 python3 box/obscore-20260903/delta52_certificate.py
```

The script performs all of the following in exact sparse arithmetic/SymPy:

1. checks the clean-room and stage-8 artifacts against their manifests;
2. reconstructs the pole, eight original `B1` `D1` rows, and 35 earlier
   Jacobian rows;
3. verifies every earlier pivot label, variable, and rational coefficient
   against the charged stage-8 JSON;
4. verifies that the seven new stage-8 variables are outside the dependency
   closure;
5. derives the seven-row Schur certificate and expands it to the identity 1;
6. lifts `B1c_3_21=0` to the seven original `D1` rows;
7. audits the 17-row raw-pole and 11-row constant-component incidence
   closures, the seven `h2-D1` variables, the outer families, and the bridge;
8. runs the perturbed-row negative control.

Final replay result: exit 0, elapsed 10.85 seconds, peak RSS 83,736 KiB on
this host.  Script SHA-256:

```text
ff457563bad9edd8667999408c9e7e5e610abd6d380cbec7f8dfd965d03788c7
```

The principal machine-readable outputs are:

```text
normal_form                         64
post-D1 quotient DAG               pole 1, Jacobian 35
reduced D1 pivot ancestors          2
original D1 row support             7
minimal post-D2 certificate         pole 1, Jacobian 6
new stage-8 pivots touched          0
h2-D1 rows touched                  0
T2/T3 bridge rows touched           0
live A2/A3/B2 coefficients          false
negative-control error              B1c_3_22/6264
```

## 6. FALLACY-v2 audit

* Flag/place/series: the local `s`-power, Jacobian `t`-power, and outer weight
  are reported separately; stage synchronization is not promoted to an
  identification.
* Strict-below/at-level: the 5,598 `D2` coordinate deletions and the retained
  weight-93 `D1` rows are counted separately.  Deleted-coordinate `D1` labels
  are not counted again.
* Pole/interior: the pole row is used only in the declared charged
  `(99,66),delta=5/2` chart and branch.  No new pole theorem is asserted.
* Floor/attainment and carrier: a unit in this finite necessary quotient is
  not called a representative or an attained polynomial pair.
* Localization: the field, ring, wrapper, and zero wrapper multiplier are
  explicit.  No `c`-division or invented `J0` factor occurs.
* Raw remainder: the row is reduced in the declared quotient; zero and the
  nonzero constant 64 are distinguished.
* Variable/ring map: the computation remains in the declared `K2c` basis.
  The unavailable inverse to original `C2,C3` coordinates is not inferred
  from matching names.
* Missing lifts: the pre-`D2` and charged pre-major multiplier maps are typed
  `OPEN`, in accordance with frozen `FALLACY-v2.md:29-30`.
* No prime-labelled object is read as a derivative; no merge-free descent or
  target/arrival-index statement occurs.
* This is not an exit-price assertion, so no `charge_basis` line is emitted.

The relevant guardrails are frozen `FALLACY-v2.md:5-30`.  The charged report's
parallel audit is at frozen stage-8 report `:200-211`.
