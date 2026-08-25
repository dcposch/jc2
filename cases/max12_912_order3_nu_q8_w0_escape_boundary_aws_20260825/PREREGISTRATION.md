# Preregistration: `w=0` source/projective escape boundary

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS LAUNCH**

## 1. Exact source

Hash-pin the reviewed approximate-cubic quotient compiler and impose exactly

```text
r1/t=r3/t=r5/t=r7/t=r2=r4=0.
```

No Q8 relation, terminal row, Taylor row, or parity-component equation is
added.  Write `A=x3-2*x5`, `e6=r6`, and `e8=r8` from the same compiler.

## 2. Finite affine cover and charged controls

At `w=0`, the excluded source divisor `V(x5*A)` is the disjoint union

```text
X: x5=0, x3!=0;       O: x5=x3=0;       A0: x5!=0, A=0.
```

Every open is represented by a fresh inverse equation.  The `X` lane must
verify mutual ideal containment with the hand-derived model

```text
x5=0, x1=x3=a, d2=d4=0, c*a=1, a!=0,
81*e6=-4*a^3, e8=0.                              (2.1)
```

The `A0` lane is expected to be empty because `e2=-4*x5^3/81` modulo
`A=0`.  These expectations are negative controls: disagreement fails closed
and quarantines every downstream claim.  The overlap `O` is split literally
by `V(e6)` and `D(e6)` and is not assumed empty or reduced.

## 3. Generic transverse formal gate

Over `Q(a)`, substitute the generic point (2.1) into the six-row Jacobian
with respect to `(c,d2,d4,x1,x3,x5)` and into the `w` derivative.  Record the
ranks of `J_y` and `[J_y|F_w]`, all `5 x 5` minors of `J_y`, and all `6 x 6`
minors of the augmented matrix.  This is only a first-order generic
Kuranishi discriminator.  If the augmented rank exceeds the source rank,
generic transverse `w`-arcs are excluded but every zero/pole of the displayed
obstruction in `a` remains charged.  If ranks agree, higher-order lifting is
mandatory.  The earlier parity `x5=0` trajectory theorem may not be imported
to kill a transverse non-parity arc.

## 4. Projective source escape

Let `I` be the six-row ideal over `Q[w]`.  Homogenize every generator in the
six affine source variables `(c,d2,d4,x1,x3,x5)` with a new coordinate `T`,
form the generated homogeneous ideal, and saturate by `T` **over `Q[w]`**.
Only after this saturation specialize `w=0,T=0`.  The six standard projective
charts `c,d2,d4,x1,x3,x5=1` cover the resulting boundary.  Each chart is an
independent fail-closed Singular lane.

Generator homogenization followed by `T`-saturation is used because it is the
homogenization of the full affine ideal; specializing first would not control
branches whose affine coefficients diverge as `w` tends to zero.  A nonempty
chart is only a projective source component/point, not a trajectory.  It must
still be split by `x5/A`, `e6`, terminal `e8`, Taylor polynomiality, and
coprimality before any exclusion.

## 5. Acceptance

Every run must pin the compiler/source hashes, return `rc=0`, contain exactly
one PASS marker, reduce every literal input generator to zero, and contain no
Singular diagnostic.  Empty means a certified unit ideal.  Positive
dimension is retained exactly; no projection factor is dropped.
