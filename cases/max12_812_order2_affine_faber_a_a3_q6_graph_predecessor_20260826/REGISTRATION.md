# Registration: affine-Faber `A`, `a=3,q=6` graph predecessor

Date: 2026-08-26

Status: preregistered exact source client; no theorem before review.

The first remote archive froze an earlier hand-note digest while that note
was concurrently clarified.  It is no-verdict deployment custody.  V2
pinned the clarified note and replaced repeated coefficient extraction by a
single-pass lower-zero scan, but failed closed on both lanes because four
hand-control polynomials put denominators after polynomial monomials (for
example `m^2/8`), which Singular parsed as a nonintegral exponent.  Its
diagnostic evidence is retained under `evidence_v2_failed/` and licenses no
row or predecessor claim.  V3 changed only those literal hand formulas to
coefficient-first syntax.  It then failed the preregistered row control
because the source replay correctly found three additional nonzero but
dependent rows `G2,G5,G7`; its two chart standard bases were nevertheless
units.  That evidence is retained under `evidence_v3_failed/` and licenses
no endpoint.  V4 verified the complete seven-row block, printed all three
exact dependencies as one, and obtained units on both charts, but its
validator accidentally omitted the new dependency marker from the mandatory
marker list.  Its positive evidence is retained under
`evidence_v4_preformal/` but is not the formal endpoint.  The controlling V5
changes only that validator gate and records an explicit terminal status.

## Cell

Use the fixed delayed schedule with normal order 15, center order 3,
kernel order 6, complement order at least 12, and the leading grade-42
affine load graph

```text
K6=(15*E^2/32)K10,
K2=(15*E^4/256)K10,
mu2=-(5*E^6/4096)K10.
```

Graph deviations begin strictly after grade 42.  Reconstruct all seven
literal ordinary-Faber rows and verify that their complete grade-42 block
is exactly the center-independent quadratic kernel block `G1,...,G7` in the
corrected hand note.  Verify explicitly that `G2,G5,G7` are redundant on
`D(E)` and that `G1,G3,G4,G6` generate unit ideals on both kernel charts.

## Mandatory controls

- all coefficients below grade 42 vanish;
- arbitrary positive center, `E`, `M`, kernel, complement, load, and graph-
  deviation successor jets are retained far enough to detect a grade-42
  intrusion;
- every grade-42 row is independent of those successor jets and of `K10`;
- a deliberate mutation of the leading `mu2` graph coefficient is detected;
- all seven exact row identities agree with the frozen hand formulas, and
  the three registered row dependencies vanish coefficientwise;
- both projective kernel charts `D(p*m*x6)` and `D(p*m*y6)` have unit
  standard bases, without inverting `K10`;
- exact Q is evidence and `F_65521` is a software control.

The client proves only the registered grade-42 predecessor.  Composition
with the low-kernel lemma and graph-relative `q>6` support remains a
separate reviewed step.  Run only on AWS.
