# Active q1 translation gauge: exact formal symmetry, raw-window obstruction

Date: 2026-08-28  
Author: Sol Ultra  
Status: **EXACT NEGATIVE AUDIT / SCRATCH FREEZE**

On the active q1 locus `R0=lambda A`,

```text
V0=3lambda A A',
F1=A^2V0=(3lambda/4)F0',
G1=(3lambda/4)G0'.
```

Thus with `a=3lambda/4`, formal precomposition
`tau_a(P)(X,t)=P(X-at,t)` kills both weight-one coefficients.  It is an
exact symmetry of

```text
E(F,G)=F_X(12-t d_t)G+((t d_t)-8)F G_X,
```

because

```text
t d_t tau_a(P)=tau_a(t d_t P-a t P_X)
```

and the two new `a t F_XG_X` terms cancel.  It fixes `t^22`, `F0`, `G0`,
the branch-P leading factor, and all upper degree bounds.

However, it is **not** an automorphism of the authoritative raw support.
The coefficient formula is

```text
(tau_a P)_n=sum_(k=0)^n (-a)^k P_(n-k)^(k)/k!.
```

The frozen windows contain `F8[X^0..X^8]` but only
`F9[X^1..X^7]`.  Taking the literal allowed mutation `F8=X` gives

```text
(tau_a F)_9[X^0]=-a,
```

which has no raw slot.  Independently, `G12=X` is allowed while G13 begins
at X-degree one, and the shear creates `(tau_a G)_13[X^0]=-a`.

The exact checker uses `A=X^4-1`, `lambda=4/3`, hence `a=1`, verifies the
weight-one identities, and obtains both forbidden constants literally.

Verdict: the differential equation has the proposed translation symmetry,
but the finite Newton-support problem does not.  Therefore lambda cannot be
gauged to zero in the current campaign.  It remains logically possible
that the determinant equations force all forbidden shear tails to cancel
on the solution locus; no such theorem has been proved, and it must not be
assumed.

Packet:
`cases/ggv_8_28_upper_endpoint_q1_translation_gauge_audit_20260828/`.
