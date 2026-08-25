# Saturated projective boundary over `w=25`

This AWS-only successor consumes the immutable raw-homogenization generator
by SHA-256.  It computes the true global-family projective closure

```text
(J : t^infinity) = eliminate(J + (z*t-1), z)
```

before specializing to `w=25`.  It then tests all seven standard projective
charts at `t=0`.  Saturation is global in `w`; specializing first would miss
components that escape to infinity as `w` approaches `25`.

An all-empty endpoint, combined with the independently frozen affine fibre
length `190`, gives a proper finite neighbourhood whose generic length is at
most `190`.  Together with the reviewed `H` component, that would trigger the
separate conditional degree-one/all-contact lemma.  A nonempty endpoint is a
real boundary obstruction for this compactification, not a trajectory claim.

