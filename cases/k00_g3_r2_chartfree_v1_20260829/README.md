# `K00-G3-R2-CHARTFREE/v1`

Date: 2026-08-29

Lifecycle: **EXACT PRODUCER + SAME-CODE-FAMILY REPLAY PASS / PROVISIONAL /
INDEPENDENT HOSTILE REVIEW REQUIRED / NOT A COUNTEREXAMPLE OR JC2 RESULT**.

This is the bounded, chart-free successor to the selected full-`P6`
rank-two chart that ended `RESOURCE_CAP_NO_VERDICT`.  It does not rerun that
chart.  It proves a stronger grade-three obstruction by exact labelled ideal
membership certificates, subject to independent review.

## Frozen source

The producer is based on campaign commit
`92ebe92ad5986a47f01af9ed901260595dfed869` and pins these exact bytes:

- V26 exact atlas: `d7ec6d18...6501`;
- V27 BASE3/R2 standard basis: `c8aa23e4...14c0`;
- Fable V27 hostile review: `738f4603...647a`;
- chart-free discovery note: `ac843e4c...5d76`.

`SOURCE_FREEZE.sha256` gives the complete paths and hashes.  The V27 basis is
a custody dependency only: the producer reconstructs the ideal used here
from the raw V26 atlas rather than importing that basis.

## Exact construction

Work over

```text
S = Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1].
```

The compiler selects the seven literal `Lambda_grade=3` rows from the frozen
atlas by their source labels.  With

```text
x = (d0_1,...,d5_1),  u = (d0_2,...,d5_2),
```

it checks in the prior 33-variable ring that every second derivative with
respect to `u` vanishes and that

```text
P3(x,u) = C(x) u + c3(x).
```

It then maps to `S` and checks all 42 entries of

```text
C = A[:,1..6].
```

Set

```text
J2 = B + I3(A),
E3 = [ C | c3 ],
H  = J2 + I3(E3).
```

The raw ideal `Hraw` retains 2,457 literal positions: seven labelled `B`
rows, all 1,225 labelled `3 x 3` determinant slots of `A`, and all 1,225
labelled slots of `E3`.  Zero slots are not discarded from the label map.
Each labelled `I3` family has `ncols=1,225`, 412 zero slots, and
`nonzero/size=813`; together with the seven `B` rows, `Hraw` has 1,633
nonzero entries.  Likewise all 441 literal `2 x 2` labels of `A` are
retained; 351 are nonzero and 90 are zero.

The producer emits a 20-element basis `GH` and exact coefficient matrices
`TH` and `CQ` satisfying entrywise

```text
matrix(Hraw) * TH = matrix(GH),       TH: 2457 x 20
matrix(GH)   * CQ = matrix(Q4),       CQ:   20 x 351,
```

where column `j` of `Q4` is the fourth power of the nonzero literal
`2 x 2` minor identified by the `j`th nonzero label in
`SOURCE_LABELS.json`.  These are full explicit rational-polynomial
certificates, not a fresh-reduction-only fallback.  The replay independently
reconstructs `Hraw` from the frozen labelled generators, checks both matrix
identities entrywise, recomputes standard bases, and checks mutual ideal
containment.

The exact unresolved normal-form profile for the 351 nonzero literal minors
is

```text
power 1: 291
power 2:  60
power 3:  36
power 4:   0.
```

Thus every literal generator of `I2(A)` has fourth power in `H`, so

```text
I2(A) subset sqrt(H).
```

## Mathematical consequence

Suppose a leading point has `B=0` and `rank(A)=2` and lifts through the seven
grade-three rows.  Since `P3=C u+c3=0`, the column `c3` belongs to the column
span of `C`; since `C` consists of six columns of `A`,

```text
rank(E3) = rank(C) <= rank(A) = 2.
```

Hence the point lies in `V(H)`.  The certified radical containment then makes
every `2 x 2` minor of `A` vanish, contradicting `rank(A)=2`.  Therefore no
rank-exactly-two leading point lifts through literal grade three.

Set-theoretically, every rank-two minor chart in the full-`P6` problem is
empty for this reason.  The earlier selected-chart computation remains an
honest historical `RESOURCE_CAP_NO_VERDICT`; this packet does not relabel its
engine outcome.  It instead makes that chart unnecessary after independent
promotion review.

## Reproduction and validation

From the repository root:

```text
python3 -B cases/k00_g3_r2_chartfree_v1_20260829/compile_k00_g3_r2_chartfree.py /tmp/k00-g3-r2-output
python3 -B cases/k00_g3_r2_chartfree_v1_20260829/validate_k00_g3_r2_chartfree.py
```

The compiler refuses an existing output path and fails on source-hash drift,
missing/duplicate labels, a `size`/`ncols` census mismatch, Singular warnings,
nonempty stderr, failed identities, changed power profile, or failed
mutations.  `MANIFEST.sha256` seals every output byte.  The validator checks
the source freeze, output manifest, complete literal label order, artifact
metadata, stored producer sections, and a fresh second-process replay.

The canonical build was also repeated under ordinary Python and `python3
-O`; recursive byte comparison was identical.  This is an implementation
identity control, not independent mathematical review.  The whole build is a
desk-scale exact job (tens of seconds, less than 1 GiB maximum RSS, zero swap
in the sealed run), so AWS was neither needed nor used.

## Mutations and firewall

The producer/replay require nontrivial failure after mutating a `C` entry, a
`c3` entry, a nonzero `TH` coefficient, a nonzero `CQ` coefficient, and a
`Q4` target.  Adjoining `1` must force the unit ideal, while `(d0_1)` must
remain proper.

This packet eliminates only the rank-exactly-two leading locus at literal
grade three.  It says nothing about the surviving rank-at-most-one locus,
the rank-five `MAX5CLASS` route, later-grade compatibility on other strata,
formal/source reachability, a counterexample, or JC2.  The replay shares the
producer's construction code and is expressly **not** an independent review.
