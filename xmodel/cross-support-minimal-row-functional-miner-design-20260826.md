# Design: support-minimal exact row-functional miner

Date: 2026-08-26

Status: **BOUNDED SOFTWARE/EXPERIMENT DESIGN; NO MATHEMATICAL CLAIM.**

## Goal

Given complete source rows `P_1,...,P_n`, find small exact left
functionals

```text
L=sum_i c_i(base)*P_i
```

which cancel a preregistered nuisance support before any predecessor
specialization.  Verify the functional against the literal source, then
emit its coefficient-stratified residual support and relative Newton cones.
"Support-minimal" always means minimal inside a finite declared ansatz; no
global sparsity claim is allowed.

## Frozen input interface

One JSON manifest should contain:

```text
schema_version
source:
  row_ast_path, row_ast_sha256, row_ids
  source_variable_inventory, load_inventory, target_inventory
base_ring:
  invariant_variables, localized_units, coefficient_characteristic
characters:
  row_character, base_character, desired_functional_character
ansatz:
  coefficient_monomial_basis_by_row
  normalization                     # e.g. coefficient of P5 is 1
nuisance:
  forbidden_monomial_predicate
  permitted_residual_support
valuation:
  variables, symbolic_weight_forms, predecessor_ideal_ids
controls:
  expected_positive_identity, required_negative_mutations
```

Rows and substitutions must be expression-tree objects or canonical sparse
monomial maps.  Generated Singular text is an output, not the source of
truth.  Every row carries its load/target timing and deck character, so a
candidate cannot silently omit a family merely because it cancels in one
specialization.

## Exact algorithm

1. Multiply each row by every allowed coefficient-basis monomial.  Index
   the resulting nuisance monomials in a common sparse dictionary.
2. Form the exact rational cancellation matrix.  Solve its kernel by
   fraction-free elimination, with the declared normalization imposed.
3. If the normalized kernel has dimension greater than one, enumerate its
   exact matroid circuits or use a declared lexicographic support objective;
   report all ties.  Never call one arbitrary kernel basis vector minimal.
4. Reconstruct `L` independently from the pinned literal rows and require
   every forbidden coefficient to be identically zero over Q.
5. Emit the residual as a canonical sparse table, factor its coefficient
   polynomials over the invariant base ring, and attach the exact
   localization needed for every factor stratum.
6. Compute only *relative* Newton cones: reduce each equality-face initial
   form by the registered predecessor initial ideal.  A raw support hull is
   navigation, not a certificate.

The exact-Q solve is evidence.  A good-prime replay checks support and
software behavior only.  All nontrivial algebra runs on AWS.

## Positive control A: affine-Faber `K`

Use rows `P1,...,P5`, invariants `B,E`, normalize the `P5` coefficient to
one, and permit the parity-compatible basis through `B^4,E^2`.  The unique
expected normalized vector is

```text
P5:  1
P4: -B
P3:  E/4 + 21*B^2/32
P2:  B*E/4 - 5*B^3/16
P1:  195*B^4/2048 - 25*B^2*E/128 - 3*E^2/32.
```

The literal-source verifier must reproduce the confirmed intrinsic residual
`-E*lambda^3*M^3/16` on the registered weighted face.  The already frozen
full-support client gives 371 raw monomials and is the first support-table
fixture, not a predecessor-relative fan certificate.

## Positive control B: D1 odd recurrence

Use the four odd rows and a coefficient basis in the moving series `p` of
degree at most three.  Normalize the row-seven coefficient to one.  The
expected functional is

```text
Phi7-(p/4)*Phi5-(p^2/32)*Phi3-(p^3/128)*Phi1.
```

On the registered `a>=13` support ceiling it must cancel every source-only
term through grade 38 and leave exactly `-J/4` in the terminal row.  The
`a=12` triple-pole arrival is a sharpness control: the miner must retain its
nonzero residual rather than expanding the ansatz until it disappears.

## Mandatory negative controls

1. **q6 center truncation:** replace the arbitrary center series by its
   leading coefficient only.  The harness must detect that restoring `a6`
   changes the grade-42 face; a PASS on both sources is a failure of the
   omission census.
2. **Perturbed row:** add a new source monomial of the correct total weight
   but wrong coefficient to one input row.  The known affine and D1
   functionals must fail literal verification.
3. **Target deletion:** remove `mu4` or `J` from the typed inventory without
   changing the row text.  Static inventory comparison must reject before
   algebra.
4. **Bad-prime cancellation:** choose a prime dividing one expected rational
   coefficient.  The finite-field lane must be quarantined and cannot alter
   the exact-Q result.

## First implementation slice

The smallest reusable implementation has three commands:

```text
rowfun matrix SPEC.json MATRIX.json
rowfun solve  MATRIX.json CANDIDATES.json
rowfun verify SPEC.json CANDIDATES.json RESIDUAL.json
```

`matrix` and `verify` use the same sparse AST library but independent code
paths for multiplication/collection.  `solve` is generic exact linear
algebra and contains no JC2-specific substitutions.  A fourth command,
`rowfun cones`, is withheld until the affine and D1 controls pass and the
predecessor-ideal API is supplied.

The existing full-`K` support emitter is a cheap prototype of `verify`: it
already reconstructs all seven rows, checks target derivatives and the
intrinsic cubic coefficient, and emits canonical exponent vectors.  The
next bounded code step is therefore the cancellation-matrix builder for the
five-row affine ansatz, followed by the four-row D1 fixture.

## Endpoints and stop rules

```text
PASS_UNIQUE_FUNCTIONAL
PASS_MULTIPLE_MINIMAL_FUNCTIONALS
NO_FUNCTIONAL_IN_ANSATZ
FAIL_SOURCE_INVENTORY
FAIL_LITERAL_VERIFICATION
FAIL_PREDECESSOR_INTERFACE
```

Stop on any unregistered denominator, coefficient factor, target/load
omission, nonunique normalization, or discrepancy between the two exact
code paths.  A found functional may feed reversible downstream design
immediately, but theorem promotion waits for exact source custody and an
independent hostile review.
