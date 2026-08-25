# Reusable extension-field smooth-point oracle

Date: 2026-08-25  
Status: **PRODUCER-EXACT SOFTWARE PACKAGE; client-neutral**

The new package

```text
cases/reusable_plane_curve_extension_smooth_point_oracle_aws_20260825/
```

turns any pinned sparse plane curve `H(w,v)` over an odd prime field, monic
in `v`, into a sharded exact Singular census over `F_(p^e)`.  It validates the
input hash, prime, sparse support, monicity, and irreducibility of the supplied
extension modulus before emitting any CAS source.  The aggregate checks every
source/output hash, full disjoint field coverage, return code, terminal marker,
and the identity `total=smooth+singular`.

For each `w`, Singular computes

```text
R_w=gcd(H(w,v),v^(p^e)-v),
S_w=gcd(R_w,H_v(w,v),H_w(w,v)).
```

The exact smooth affine count is `sum_w(deg R_w-deg S_w)`.  If a separate
reviewed theorem says the plane curve is geometrically integral, a count above
`p^e+1` proves that its smooth projective normalization has positive genus.
The oracle itself proves neither geometric integrality nor source-component,
specialization, trajectory, maximum-degree, or JC2 statements.

AWS r6a smoke tests over `F_25=F_5[a]/(a^2+2)` passed on both a smooth and a
singular control: `v^2-w` gives `25/25/0`, while `v^2` gives `25/0/25`
for total/smooth/singular affine points.  Q8 remains a regression input whose
mathematical count is separately frozen and reviewed; it is not counted as one
of the two next clients.

Two max-12 client slots remain open by design.  A client becomes eligible only
after an exact sparse plane-curve table and its geometric-integrality premise
are frozen.  This prevents an avenue label or projected root set from being
silently treated as a curve theorem.

