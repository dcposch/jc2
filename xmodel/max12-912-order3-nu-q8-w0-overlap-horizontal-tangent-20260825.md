# Corrected-Q8 unloaded overlap: exact first-order horizontal tangent screen

Date: 2026-08-25  
Status: **PRODUCER-EXACT; REVIEW PENDING**

## Scope

Use the hash-pinned six divided source rows

```text
I=(e1,e3,e5,e7,e2,e4)
```

in `(w,c,d2,d4,x1,x3,x5)`.  On the raw unloaded overlap

```text
w=x1=x3=x5=0
```

this report classifies ordinary first-order deformations normalized by
`delta w=1`.  It does not classify ramified arcs, higher-order departure,
the selected horizontal saturation, coefficient infinity, Taylor/terminal
realization, or trajectories.

## Exact tangent equations

For each imposed row form

```text
L_i = e_i,w + sum_y e_i,y delta y.
```

The two lower normal equations are exactly

```text
L2 =  2*d2^2/9 - 8*d2*d4/9 + 2*d4^2/3 + 4*d4/9,
L4 = -8*d2^2/27 + 20*d2*d4/27 - 4*d4^2/9
     + 4*d2/9 - 16*d4/27.
```

Mutual ideal containments over `Q` certify their equivalence to the
hand-normalized pair `F2,F4` from the preregistration and to the reduced
two-point scheme

```text
(d2-2*d4, d4^2-2*d4).
```

Thus the only candidates are `(d2,d4)=(0,0)` and `(4,2)`.

At the origin, `e1,e3,e5` force

```text
delta x1=delta x3=delta x5=0,
```

and `L7=0`; this is the tangent to the exact boundary sheet.  At `(4,2)`,
the same three rows force

```text
delta x1 =  8*c + 8/3,
delta x3 = 20*c + 88/9,
delta x5 = 12*c + 16/3,
```

but the remaining row gives

```text
L7=-16/27,       729*L7=-432.
```

Hence no ordinary horizontal tangent exists there.  This is consistent
with, but logically separate from, the exact normal-rank/Fitting successor.

## AWS endpoints and replay

Two independent exact-Q Singular engine/order lanes passed without a banned
diagnostic:

```text
Box02 std/dp:
  input  b31d05c152e5357f80cc3d9c375f53630f37252c0842461421753161d0fb2dff
  stdout 68959c2f918990766a27fcfadfd80f2eea8521ddab2bdbbe02f131e68d3e6e63

Box03 slimgb/block:
  input  83732e0d6d857b687c6bcc650f8da73eed84b0c283fa1ffa2849eef7925b320f
  stdout d58fcf95633bad3fd092fc82f215e7ffefcc93fa6a5d28ff0d1a397603154235
```

The AWS-only replay checks both byte hashes, source pins, all displayed
identities and basis rows, zero return codes, and absence of banned
diagnostics.  It returns

```text
Q8_W0_OVERLAP_HORIZONTAL_TANGENT_V3_REPLAY_PASS
```

with stdout SHA256
`009937d287e92e057b5e2562d510abde2d062cece42c102e68d5000c04b2a65c`.

V1 and V2 are retained only as fail-closed software controls.  V1 had
invalid Singular ideal syntax; V2's mathematics passed but its wrapper
incorrectly required zero-dimensional `vdim` in a ring with free variables.

## Honest consequence

At order one in `w`, the raw overlap has no selected-opening direction:
the sole surviving tangent is contained in the exact boundary sheet.  This
does **not** exclude an arc with `ord(w)>1` or an arc whose first nonzero
normal term occurs later.  The global `I:(w*x5*(x3-2*x5))^infinity`
saturation and the weighted rank-drop analysis remain the arbiters.

