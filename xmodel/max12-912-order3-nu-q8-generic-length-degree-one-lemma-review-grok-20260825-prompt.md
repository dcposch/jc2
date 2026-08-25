# Hostile review: generic length 190 implies degree one and all Q8 contacts

Act as an independent hostile algebraic-geometry and computational-algebra
referee.  Work read-only except for the single output file named below.  Do
not browse, use a shell, access the network, or run new heavy computation.
Read these files in full:

- `xmodel/max12-912-order3-nu-q8-generic-length-degree-one-lemma-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-component-reviewed-successor-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-full-contact-jacobian-aws-20260825.md`
- `cases/max12_912_order3_nu_q8_generic_vertical_length_aws_20260825/generate.py`
- `cases/max12_912_order3_nu_q8_generic_vertical_length_orders_aws_20260825/generate_variant.py`

The theorem under review is deliberately **conditional**.  No generic-length
lane has yet supplied its premise.  Assume only for the implication that a
fail-closed exact computation on the displayed generic localized ideal proves

```text
dim=0,  vdim=190,  source_fail=0
```

over `F_127(w)`.  Do not turn that assumption into a claim that an endpoint
already exists.  Try to refute every load-bearing step:

1. Verify that the generic ideal in seven variables really describes the
   same localized source as the full-contact eight-variable presentation.
   Audit `x3=(v+2)x5`, `u=inv*x5`, both localizer equations, and every unit
   needed to make this an isomorphism rather than a one-way substitution.
2. After base change from `F_127(w)` to `Fbar_127(w)`, does algebra length
   remain 190?  Does the reviewed existence of a source component whose plane
   image is `H` genuinely produce a support prime of that exact generic
   algebra?
3. Check the formula `m*[L:Fbar_127(w)]=m*d*190`.  Attack hidden assumptions
   about scheme multiplicity, embedded points, nonreduced Artin factors,
   inseparability, or the distinction between cycle multiplicity and residue
   field degree.
4. Audit the geometric-integrality premise for `H`, including why it remains
   irreducible of `v`-degree 190 over `Fbar_127(w)`.  Could a constant-field
   extension or Frobenius orbit let several source components contribute less
   than 190 each over the original base?
5. If one H-dominant support already consumes all length 190, does it follow
   scheme-theoretically that its multiplicity and source-to-H degree are one
   and that there is no other `w`-dominant localized component?  Distinguish
   uniqueness over `F_127` from geometric uniqueness.
6. Does the full relative `8 x 8` Jacobian unit at each corrected contact
   really give completed local ring `Fbar_127[[w]]` for the same source
   scheme?  Check ambient dimension, equation count, the role of the
   localizer, and whether `w` rather than some ramified parameter is a
   uniformizer.
7. Even if the completed contact branch is reduced and one-dimensional, must
   it survive in the generic localized fibre?  Look for vertical components,
   components contained in a removed denominator, higher-dimensional special
   components, or failure of local-to-global component passage.
8. Determine the exact strongest conclusion.  Degree one should mean equality
   of function fields/birationality, not global regular coordinate functions.
   Enforce the firewall against projective-boundary regularity,
   characteristic-zero no-merger, integral specialization, primitive
   grouping, Taylor data, terminal dynamics, trajectories, maximum twelve,
   or JC2.

If the implication is false, give the smallest explicit algebraic
counterexample.  If it is correct after repairs, state the minimal corrected
hypotheses and exact replacement wording.  Separate a missing computational
premise from a flaw in the conditional mathematics.

Write the complete review only to
`xmodel/max12-912-order3-nu-q8-generic-length-degree-one-lemma-review-grok-20260825.md`.
Do not edit producer files, cases, manifests, or canonical ledgers.  End with
exactly one verdict token on its own line:

```text
CONFIRMED
CONFIRMED_WITH_REPAIRS
INCONCLUSIVE
REFUTED
```
