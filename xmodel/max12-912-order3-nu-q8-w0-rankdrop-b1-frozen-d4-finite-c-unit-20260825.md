# Selected Q8 `b=1`: frozen-`d4` finite-`c` landing unit

Date: 2026-08-25  
Status: **PRODUCER-EXACT ONE-ENGINE ENDPOINT; MIRROR/REVIEW PENDING**

The exact Box02 `std/dp` computation over the polynomial ring `Q[c,...]`
returns the unit ideal after taking the selected contraction and imposing the
pointed landing centre.  Thus no exceptional finite value of `c` survives in
the **frozen slice `d4=1,d2=2+u` at that landing centre**.

## Exact construction and result

From the pinned six quotient rows `(e1,e3,e5,e7,e2,e4)`, substitute

```text
d4=1,  d2=2+u,  A=x3-2*x5.
```

Over `Q[w,u,x1,x3,x5,c]`, compute

```text
C       = I : (w*x5*A)^infinity,
GC      = std(C),
Landing = GC + (w,u,x1,x3,x5),
GL      = std(Landing).
```

The accepted endpoint prints

```text
landing_empty=1
C_PARAMETER_BASIS_BEGIN
GL[1]=1
C_PARAMETER_BASIS_END
```

and exits rc0.  The run used Singular 4.3.2 on Box02, wall `1:07:11`, user
`4026.60s`, maximum RSS `41820 KiB`, and zero swaps.  Generator stderr is
empty.  Stdout SHA256 is
`98950fa27f11b9a15902a4af17173d60f2b97acfcdb0d4778dc09510c38215ff`;
input SHA256 is
`58c2fa57f7d4511b3df76f74c84759ea88534c6b9ddac0c39ef82b43aa02f946`.

The frozen one-host custody manifest is
`cases/max12_912_order3_nu_q8_w0_rankdrop_b1_loaded_saturation_aws_20260825/PARAM_BOX02_RESULT.manifest.sha256`.

## Exact scope

The theorem is `Landing=(1)`.  The endpoint does **not** print or assert
`GC=(1)`: it does not say that the whole selected contraction is empty away
from the landing centre.  It says only that its closure has no point over

```text
w=u=x1=x3=x5=0
```

for any finite `c`, in the frozen `d4=1` slice.  It upgrades the reviewed
generic-`c` result by removing the finite exceptional-`c` debt in that slice.

Moving `d4`, the pointed drift chart `d4=1+v`, the full rank-drop line/full
`Hsrc`, coefficient infinity, other coordinate projective boundaries,
terminal and both Taylor families, trajectories, the full `(9,12)` cell,
maximum twelve, and JC2 remain open.  The independent Box03 `slimgb/block`
mirror and hostile review are pending, so this report is not yet a promoted
claim.
