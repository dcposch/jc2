# K00 V27 R3 exact one-minor chart selection

Date: 2026-08-27

Lifecycle: **PRODUCER-CHECKED SELECTION ONLY / INTERNAL-UNREVIEWED /
NO PRINCIPAL-OPEN ALGEBRA RUN / NOT PROMOTED**.

## Frozen selection

A fresh exact Singular 4.3.2 process on audited AWS r6a reconstructed the
frozen matrix `A`, all seven generators of `B`, and every stored nonzero
minor in `I5(A)`, `I4(A)`, `I3(A)`, and `I2(A)`.  It freshly rederived the
R1/R2 containments and the proper dimension-three ideal

```text
J2base = B+I5(A)+I4(A)+I3(A).
```

In Singular's complete literal-column `I2(A)` object, the first column with
nonzero normal form modulo a fresh standard basis of `J2base` is column 37.
An exhaustive replay over all 441 literal `2 x 2` row/column labels found
exactly one label up to sign:

```text
rows    = (5,7)
columns = (6,7)
m       = A[5,6]*A[7,7] - A[5,7]*A[7,6]
m       = -I2A[37]
NF_J2base(m) != 0.
```

The exact serialized `m` has SHA-256
`51007fc35085e65bd7b19936b492949c9edcd04f4f34716c1ff6fc9e8f6d5616`.
Its serialized nonzero normal form has SHA-256
`8748e6f901332974919b80383deb9a3cca37f84f46da5252e34885485380157c`.

This fixes one deterministic chart representative; it does not establish
that `D(m)` meets `V(J2base)`.  Nonzero normal form does not exclude
nilpotence modulo `J2base`.  The exact discriminator is the separately
preregistered ideal `J2base+(z*m-1)`.

## Custody and controls

The clean R1 selection supersedes an unconsumed manual diagnostic that
emitted Singular redefinition warnings.  The clean process required the full
stored-minor censuses, selected column 37 by a deterministic first-outside
rule, exhaustively recovered the unique literal label and sign, compared the
labelled determinant and its normal form coefficientwise, and returned rc 0
with maximum RSS 32,784 KiB and zero swap.

- AWS evidence manifest:
  `8895592dbf85cbc0cae73db1e448d54281ac686c964248688983eafaa6084336`
- portable harvest manifest:
  `60c9745600c275b8876927f11d2441f5267536dd3e653a667ea884d13d385119`
- source R3 endpoint:
  `bd12daa1e1e6545b8c61bef7dcb18913854146bd9c61e0b04c795fa486b4a228`

No chart, saturation, projectivization, `I1(A)`, full-`P6`, rational-point,
grade-seven, lift, jet, arc, closure, counterexample, or JC2 computation was
performed.  No sampled-pencil claim was consumed.

## Additive `ncols()` clarification

The later hostile R1/R2/R3 review found that the selection diagnostic's
per-slot census inherited the producer's `size()` bound.  The selected
column remains valid: a complete `ncols()` traversal has 291 outside entries
and cannot change the earliest outside column 37, which was already visited;
the exact labelled polynomial and its nonzero normal form were independently
replayed.  References above to column 37 mean a literal minor-object column,
not the 37th nonzero generator.  No successor may consume the obsolete 237
count or use `size()` as a positional loop bound.
