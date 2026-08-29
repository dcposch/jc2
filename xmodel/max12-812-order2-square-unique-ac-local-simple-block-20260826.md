# `(8,12)` order-two square fan: unique-`AC` local simple-block reduction

Date: 2026-08-26

Status: **HAND LOCAL TRUNCATED-DIVISIBILITY THEOREM, CONDITIONAL ON COMPLETE
SOURCE/FABER SUPPORT AND COEFFICIENT REPLAY.  NO BRANCH VERDICT.**

## Claim and scope

Work on the unit-load generic-square chart `D(p*k0)` after the reviewed
vertical contact gates.  Put

```text
a=ord_sigma(A)>=1,  r=ord_sigma(R)>=2,
c=ord_sigma(C)>=3.
```

Conditional on the complete source support and moving Laurent/Faber replay,
every integral point of the unique-`AC` lower-hull cell is impossible except

```text
(a,c,r)=(1,4,2).                                   (E)
```

This subsumes the earlier conditional `d=1`, `d=2`, and shifted-`d=3`
designs.  It does not decide (E), a tied first face, or unique `RC`.

## Root allocation and the target pole

Put `d=c-a`.  Exact lower-hull inequalities for a unique `AC` face give

```text
d in {1,2,3}.
```

The first source grade makes `A0*C0/L0` polynomial.  Since `L0` is a
squarefree quadratic on `D(p)`, pass to the etale root algebra and orient

```text
L0=u0*v0,  A0=alpha*u0,  C0=gamma*v0,
alpha*gamma!=0.                                    (1)
```

Hensel lifting gives `L(sigma)=u(sigma)*v(sigma)`, with `v(sigma)` a unit in
the local ring at `u0=0`.  Work only in that local ring.  The first `C2`
term occurs exactly `d` grades after `AC`, and its leading coefficient is

```text
(3/8)*C0^2/L0^2=(3/8)*gamma^2/u0^2.                (2)
```

Thus it has a nonzero double pole at the root where `A0` vanishes.

## Local simple-block lemma

Suppose that, through grade `j`, every charged term other than (2) is either
regular at `u0=0` or can be written in the moving local ring as

```text
S(sigma)/u(sigma)
```

modulo the next power of `sigma`.  If the source equations through grade
`j` have no negative part, truncated division forces the numerator of the
sum of all such simple-pole terms to be divisible by `u(sigma)` through
that order.  Its next coefficient can therefore have at most a simple pole.

This statement applies to the **sum** of the charged simple-pole terms;
they need not vanish or factor individually.  It automatically includes
moving-root connections and cancellations among `AC`, `A2`, `RC`, and
`R3`.  It is a local identity in a truncated DVR, not a radical or
set-theoretic assertion.

## Complete pole audit before `C2`

Relative to the first `AC` grade, the registered gaps are

```text
C2:    d,
A2:    4-d,
RC:    1+s,              s=r-a>=0,
R3:    a+3*s-d,
RA2:   a+s+2-d,
A3:    a+5-d,
kR2A:  a+2*s+3-d,
kAC:   4,
RAC:   2+r,
```

with `RC2` still later.  The terms `AC,A2,RC,R3,kAC` have denominator at
most `L`, so they belong to the simple block at `u0=0`.  The remaining
higher-denominator terms behave as follows through the target grade `d`:

- `A3=A^3/L^3`: whenever it can reach grade `d`, its leading powers of
  `A0` cancel the complete `u0^3` denominator; it has no earlier correction
  capable of a double pole there.
- `kR2A=k*R^2*A/L^2`: whenever it can reach grade `d`, its leading `A0`
  factor leaves at most a simple pole; it has no earlier correction capable
  of a double pole there.
- `RAC` and `RC2` start after grade `d` because `r>=2` and `d<=3`.
- `RA2=R*A^2/L^2` starts at gap
  `g=a+s+2-d`.  Its coefficient `n` grades after first appearance can lose
  at most `n` of the two leading `A0` root factors.  It can contribute a
  double pole at the `C2` target only if

  ```text
  d-g>=2,  equivalently  a+s<=2*d-4.               (3)
  ```

For `d=1,2`, inequality (3) has no solution in the unique-`AC` domain.  For
`d=3`, the `s=0` uniqueness condition is `a>3`; with `s>=1`, (3) has the
single solution `a=s=1`.  This is exactly (E), where `RA2` begins at gap one
and its second correction can contain `R0*A1^2/L0^2` at the grade-three
target.

Away from (E), the local simple-block lemma applies through grade `d-1`.
At grade `d`, every charged competitor has pole order at most one at
`u0=0`, while (2) has nonzero order two.  Polynomiality is impossible.
The deck-conjugate orientation is identical.

## Exact client acceptance test

A symbolic dual-field client should fail closed unless it verifies:

1. all seven complete source rows and the moving lower-unitriangular
   Laurent/Faber bridge through the first `AC` grade plus `d`;
2. the exact unique-`AC` inequalities `d in {1,2,3}` and the complete gap
   table above, without replacing unbounded families by a finite box;
3. Hensel/root localization and the local simple-block truncated-division
   identity for the **sum** of all denominator-`L` terms;
4. every higher-denominator pole bound in the audit, including all
   corrections of `RA2,A3,kR2A` that can reach the target;
5. the exact nonzero coefficient `3/8` in (2), both root orientations, and
   the uniqueness of exception (E);
6. a negative control at (E) showing that the blanket simple-block claim is
   rejected when the second `RA2` correction is retained;
7. exact `Q` as the proof endpoint and one good-prime software control.

## Firewall

Conditional on exact replay, this theorem eliminates only unique-`AC`
horizontal faces outside (E).  It does not eliminate (E), unique `RC`, a
tied first face, positive-order or ramified loads, `p=0`, `k0=0`, the
exact-square zero section, terminal/Taylor conditions, fan exhaustiveness,
order two, maximum twelve, or JC2.
