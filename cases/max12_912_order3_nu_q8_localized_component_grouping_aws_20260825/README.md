# Q8 localized-minimal-prime grouping (AWS-only)

This route decomposes the punctured localized scheme first, where the frozen
gate already found a 607-element modular standard basis, and contracts each
localized prime separately by eliminating `inv`.  Algebraically, minimal
primes of the localization are exactly the primes of the original quotient
that avoid `f=w*x5*(x3-2*x5)`; their contractions are the desired punctured
component closures.

It is an exact finite-field implementation but remains support-only for
characteristic-zero geometry.  It is a distinct algorithmic discriminator,
not an independent theorem.  Run only on AWS under the 12-hour / 256-GiB
guard.  No result is claimed until output is harvested, frozen, and reviewed.
