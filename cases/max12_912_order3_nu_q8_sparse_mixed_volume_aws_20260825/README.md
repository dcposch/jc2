# Selected-Q8 sparse projection-degree bound

This AWS-only producer extracts the exact characteristic-zero monomial
supports of the six divided approximate-cubic source rows in variables

```text
(w,c,d2,d4,x1,x3,x5)
```

and appends the pulled-back support of a generic plane line after eliminating
the ratio coordinate,

```text
a*w*x5 + b*(x3-2*x5) + c*x5.
```

It computes seven-dimensional mixed volumes exactly by polarization.  Each
of the 127 Minkowski-sum normalized volumes is computed by Normaliz 3.10.2;
the polarization sum is divided by `7!`.  Two calculations are kept separate:

- raw Newton supports, which bound torus intersections only;
- every support augmented by the origin, the candidate affine-BKK bound that
  also charges coordinate boundaries.

The Box02 replay gives raw torus mixed volume `519` and origin-augmented
affine mixed volume `658`.  Standard-segment and repeated-simplex controls both
give `1`.  A separately generated Box03 shard reproduces `658` from the same
pinned supports.

The companion proof report audits the intersection-theoretic use of `658`:
the relevant components are one-dimensional and regular at every charged base
point; a generic target line avoids their finite localization/infinity and
component-collision sets; its pullback intersections are therefore isolated;
and the affine sparse theorem counts them even if unrelated positive-
dimensional components exist elsewhere.  The number bounds the total degree of
the pushed-forward relevant cycle.  It does not itself force a component;
finite contact must exceed the bound strictly.

No substantive local execution is licensed.
