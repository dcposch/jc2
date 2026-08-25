# Post-round precision erratum: the raw `x5=0` tangent test

Date: 2026-08-25  
Status: **NONMUTATING PRECISION REPAIR TO THE 11:20Z SYNTHESIS**

The synthesis says that the generic raw boundary family has compatible
first-order transverse deformation because

```text
rank(J_y)=rank([J_y|F_w])=5.
```

Here "transverse" can only mean transverse to the special fibre `w=0`.  It
must not be read as transverse to the source boundary `x5=0` or as evidence
that the selected `x5!=0` open approaches the family.

Indeed the exact six displayed source rows vanish on the cylinder

```text
x5=d2=d4=0,  x1=x3=a,  c=1/a,  a!=0,
```

for every `w`, and every entry of `F_w` vanishes there.  Thus the augmented
rank equality is already explained by the tangent vector
`delta_w=1, delta_y=0`, which stays inside `x5=0`.

Moreover the recorded minors give `rank(J_y)=5` for every `a!=0` (for
example a displayed minor is a nonzero rational multiple of `a^6`).  The
derivative of the cylinder in `a` is a nonzero vector in `ker(J_y)`, hence it
spans that one-dimensional kernel and has `delta_x5=0`.  Since `F_w=0`, every
first-order solution with arbitrary `delta_w` has coefficient-variable part
in this kernel and therefore also has `delta_x5=0`.

Consequences:

- the old rank test neither kills nor licenses selected-open landing;
- an unramified selected-open arc, if one exists, can turn on `x5` only at
  higher order;
- ramified/weighted arcs remain possible and require the normal-cone/Rees
  analysis;
- the exact source-horizontal saturation
  `I:(w*x5*(x3-2*x5))^infinity` remains the decisive first gate.

No generated input or frozen output is changed by this wording repair.
