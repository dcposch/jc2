# Rejected V11 producer: tracked local basis did not replay

The frozen exact-Q AWS producer on `r6d` passed all four local-order toy
controls and computed a proper 12-element `ds` standard basis, but the
mandatory identity

```text
G = I*T
```

returned false.  The fail-closed sentinel fired before reducing `r7`, the
external validator rejected the run, and V11 therefore proves **no
membership or nonmembership statement**.

The implementation had enabled Singular's `option(redSB)` before calling
`liftstd(I,T)`.  V12 preregisters the smallest diagnostic repair: replay the
identical frozen source and local semantics with that post-reduction option
absent, so the transformation returned by `liftstd` is checked against the
unmodified tracked basis.  V11 is retained unchanged as negative provenance.

Rejected evidence is under `aws_q_r6d_failed_basis_replay/`.

