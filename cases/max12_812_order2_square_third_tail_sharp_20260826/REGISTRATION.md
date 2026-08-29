# Registration: sharpened square third-tail source replay

Date: 2026-08-26

This package reconstructs all seven frozen one-parameter source rows in the
matched square chart

```text
K=L^2+Lambda*R,
N=L*M+Lambda*S,
k10=Lambda*kappa.
```

It extracts the exact `Lambda^3` grade over `Q` and independently over
`F_65521`, and compares the ordinary source rows with the lower-unitriangular
Faber transform of

```text
[T*(12*B*L^2-T^2)/(16*L^3)]_-,
T=2*L*R+M, B=R^2+S.
```

Two configurations are mandatory:

- `generic`: arbitrary fixed `p`;
- `p0moving`: `p=Lambda*p1`, so the boundary quartic is `z^4` while its
  tangent along the square center is retained.

The p-zero validator requires the exact sentinels

```text
[z^0]P=-beta^3,
[z^3](P|beta=0)=-alpha^3.
```

No standard basis or radical is needed.  A PASS is a source/analytic identity
and a necessary third-tail theorem only.  It is not a square-component,
order-two, terminal, Taylor, `(8,12)`, maximum-twelve, or JC2 verdict.

Run only on registered AWS hosts with a 16 GiB virtual-memory cap, a
10-minute compiler cap, and a one-hour engine cap.
