# Selected-Q8 generic candidate order race over `F_127(w)`

This AWS-only race attacks the exact missing bridge directly.  It uses the
same pinned original eight generators and the same interpolated monic
degree-190 candidate `H(w,v)` as the canonical candidate-certificate case,
but varies variable permutations, monomial orders, and Singular's `std` /
`slimgb` engines.  Each lane computes a standard basis of the **unseeded**
original ideal `I`, reports `dim` and `vdim`, and reduces `H` modulo that
basis.  The decisive endpoint is

```
generic_dim=0
generic_vdim=190
candidate_remainder=0
```

Unlike candidate-seeded `I+(H)` runs, this endpoint supplies both generic
length and generic ideal membership.  Every substantive run belongs on AWS.

