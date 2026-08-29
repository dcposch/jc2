# Adjudication: V24 Opus5 hostile review

Date: 2026-08-27

Review:
`xmodel/max12-812-order2-k00-v24-grade7-cokernel-hostile-review-20260827.md`  
Review SHA256:
`d547baa2f5a56ae7d8551ad115384dc1888e87226e726c1ad5c90b35369882bf`

Status: **PASS ACCEPTED AT THE EXACT CONDITIONAL LINEAR-ALGEBRA SCOPE.**

The review lane exited cleanly.  It independently rebuilt the V20R2
Lambda-grade-seven source with a different parser, monomial encoding,
variable order, matrix extraction, and determinant algorithm.  It matched
coefficientwise the `7 x 7` matrix, all 49 entries, the 226-term witness
minor `W`, all fourteen Cramer-covector entries, all fourteen-by-seven
annihilation checks, the seven inhomogeneous rows, all thirty-five prior
rows, and the two 110,117-/83,298-term compatibility polynomials.  It also
checked all 49 `6 x 6` minors of `A` are zero, proved completeness of the
two-dimensional left kernel on `D(W)`, replayed the V20R2 DAG on additional
fixtures, and independently recovered the forbidden nonzero `k6_0` column.

The source freeze replays 11/11 and the original endpoint evidence replays
14/14.  The exact artifacts and review bytes were rehashed again during this
adjudication.

## Accepted theorem wording

Use `Comp1` and `Comp2` below as unambiguous aliases for the producer's
compatibility-polynomial labels `C6` and `C7`; they are not the normalized
coefficient coordinate `C6(normalization)`.

> In the normalized `C6(normalization)=1`, valuation-one source, after the
> honest restriction `k6_0=0`, let `A` and `b` be the exact literal
> Lambda-grade-seven newest-coefficient system in
> `(d0_6,...,d5_6,k10_3)`.  Let
> `W=det A[rows 0..4; columns 0,1,2,3,6]`.  Over the exact localized
> coefficient ring `Q[prior variables][1/W]`, `A` has rank five, its left
> kernel is free of rank two with the frozen Cramer covectors, and
> `A*y+b=0` is solvable if and only if the two frozen exact contractions
> `Comp1=Comp2=0`.

In the campaign's current constructible branch this is consumed only
conditional on all literal prior coefficients through grade six,
`F10=0`, and `k10_0!=0`.  Those prior equations and `k10_0` are contextual
hypotheses, not ingredients in the exact rank-five theorem itself.

## Material modular repair

The review correctly identifies the original machine field

```text
modular_reduction_status = F65521_C6_ZERO_1_C7_ZERO_1
```

as misleading if read as membership evidence.  The original frozen JSON is
not mutated.  It is superseded by the already frozen V24R1 result

```text
F65521_LOCALIZED_PRIOR_IDEAL_IS_UNIT_NO_MEMBERSHIP_CONCLUSION
```

with result SHA256
`10cfdfea0c20554d6a65bac99a009bad23fee9babcb62c80f11ed86ee8a96ea4`.
The Opus review independently reaches the same endpoint and additional
primes do too.  V24R3 separately records unit fibres at 32003, 65519, and
65537.  These repeated unit fibres are a scheduling signal only.

The review's informal wording that the collapse is “not an artifact of the
prime” is narrowed here to: **it is not isolated to `p=65521` among the
tested primes.**  No finite collection of modular unit fibres proves the
exact-Q ideal unit or rules out arithmetic vertical effects.  The live
tracked exact-Q V24R2 gate remains mandatory.

## Additive custody and hygiene disposition

- C-1 and C-2 are repaired additively by the companion reviewed-custody
  manifest, which covers the original endpoint manifest, the previously
  omitted root telemetry/freeze files, the producer report, this
  adjudication, and the hostile review.  No frozen producer byte changes.
- The hardcoded JSON booleans and narrow producer sign mutation are
  non-material because the producer fail paths and the independent review's
  broader mutation/reconstruction both fired.  Future compilers should emit
  computed flags rather than authored `True` values.
- Future artifacts should use `Comp1/Comp2`, not `C6/C7`, for the
  compatibility labels.
- The duplicated sentence in the review's `k6_0` prose is cosmetic and does
  not affect any artifact, reconstruction, or verdict.

## Firewall

This adjudication does not certify chart nonemptiness, modular or exact-Q
membership of the compatibility polynomials, the locus `W=0`, grades
8--19, a compatible full jet, formal/convergent/algebraic arc, honest
`Jdet`-open source reachability, K00 closure incidence, order two, maximum
twelve, JC2, or a counterexample.  The exact-Q `D(k10_0*W)` gate and the
representation-independent Fitting atlas including `W=0` remain separate
successors.
