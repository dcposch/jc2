# Preregistration: selected-Q8 horizontal closure and boundary leaves

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

## Exact source and firewalls

Let `I=(e1,e3,e5,e7,e2,e4)` be the same six divided approximate-cubic
quotient rows over

```text
Q[w,c,d2,d4,x1,x3,x5],       A=x3-2*x5,
```

with `e6=r6` and `e8=r8` retained as outputs.  The generator hash-pins the
reviewed quotient compiler and its transitive order-three fibre source.
Nothing is specialized to `w=0` before the following saturations.

Two different geometric objects are deliberately kept separate:

```text
Hsrc = I : (w*x5*A)^infinity,
Bsrc = (I + (x5*A)) : w^infinity.
```

`Hsrc` is the closure of the selected generic open
`D(w*x5*A)`.  `Bsrc` is the union of source components which are horizontal
over `w` and generically contained in the boundary divisor `V(x5*A)`.
The latter are different trajectory leaves; they are not inferred to be
closures of the selected open.

## Affine special-fibre lanes

After forming `Hsrc` or `Bsrc`, and only then, set `w=0` and use fresh inverse
variables to inspect:

```text
X: x5=0, x3!=0;
A0: A=0, x5!=0;
O: x5=x3=0.
```

The overlap is split by `D(e6)` and `V(e6)`.  Every lane reports the source
and branch dimensions, a reduced basis, the normal forms of `e6,e8`, and
literal remainders of every original row.  Empty means a certified unit
ideal.  The raw specialized results from the predecessor case are controls,
not expected answers: in particular, the raw `X` line may be vertical.

## Relative projective successor

The affine lanes are the first gate.  A separately pinned successor will
homogenize the already-saturated ideals in the six coefficient variables
with `w` of degree zero, saturate by the projective irrelevant coordinate
and again by `w`, and only then take `w=T=0`.  The predecessor's raw
projective charts are negative/routing controls only.

## Acceptance and scope

Each AWS lane must return `rc=0`, exactly one PASS marker, no Singular
diagnostic, and zero original-row remainders.  Standard-basis and `slimgb`
mirrors must agree on unit/nonunit status, dimension, and displayed reduced
normal forms before a claim is frozen.

This case classifies horizontal source incidence only.  A surviving point or
component is not a Taylor-polynomial/rational Keller trajectory; terminal,
true-centre Taylor, coprimality, projective infinity, `p=0`, other `(9,12)`
leaves, maximum twelve, and JC2 remain charged.
