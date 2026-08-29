# Uniform full-fixture D18--D22 endpoint collapse (independent Sol Ultra desk)

## Verdict

The proposed endpoint collapse is correct after one important repair.  The
full characteristic coefficient `g22` is **not** only an `A^-2` polar term.
Its exact `A`-exponents are

```text
-2, 0, 2, 4, 6, 8.
```

This does not weaken the obstruction.  The complete raw determinant row is
still divisible by `A=X^4-1`, whereas the authoritative endpoint equations
require that complete polynomial to equal `1`.  Hence the uniform
field-valued upper-endpoint stratum is empty.

## Exact continuation

Retain the D16/D17 notation

```text
B = F8-Y/2-T*Z/8-Q*V/16-R^2/4,
D = F9-Q*R/2-T*V/16-Y*Z/8,
```

and their exact quotients `M,N`.  No gauge, sign, carrier, or unit is
normalized.

At D18 define

```text
E = F10-D*Z/4-Q^2/4-R*T/2-V*Y/16.
```

The independently reconstructed negative part is

```text
g18^- = c18/A^3 + P18/A^2,
P18   = (3*B/4+c8/2)*E + 3*D^2/8 - N/2.
```

For a polynomial raw `G18`, `c18+A*P18` is divisible by `A^3`.  Reduction
modulo `A` gives `c18=0`; cancellation of `A` then gives `P18 in (A^2)`.
Write `P18=A^2*P`.

At D19 put

```text
H = F11-E*Z/2-D*V/8-Q*T/2-R*Y/2.
```

Then

```text
g19^- = P19/A^2,
P19   = (3*B/4+c8/2)*H + 3*D*E/4 - P/2,
```

so `P19=A^2*S`.

At D20 put

```text
K = F12-D*R-E*V/4-E*Z^2/16-3*H*Z/4-Q*Y/2-T^2/4.
```

The exact negative part is

```text
g20^- = c20/A^4 + P20/A^2,
P20   = (3*B/4+c8/2)*K + 3*D*H/4 + 3*E^2/8 - S/2.
```

Now `c20+A^2*P20` must be divisible by `A^4`; hence `c20=0` and
`P20=A^2*U`.

At D21 define

```text
L = F13-D*Q-2*E*R-E*V*Z/16-3*H*V/8
    -3*H*Z^2/16-K*Z-T*Y/2.
```

Then

```text
g21^- = P21/A^2,
P21   = (3*B/4+c8/2)*L + 3*D*K/4 + 3*E*H/4 - U/2,
```

and therefore `P21=A^2*W`.

Every statement above is obtained by reconstructing the complete
`F^(3/2)` recurrence together with all nine characteristic modes.  In
particular, `c4,c8,c12,c16` and every regular contribution are retained.

## Endpoint row

Complete the F14 cross terms by writing

```text
J = F14-D*T-2*E*Q-E*R*Z/2-E*V^2/64
    -3*H*R-3*H*V*Z/16-H*Z^3/64
    -K*V/2-3*K*Z^2/8-5*L*Z/4-Y^2/4.
```

The polar numerator is

```text
P22 = (3*B/4+c8/2)*J + 3*D*L/4 + 3*E*K/4 + 3*H^2/8 - W/2.
```

Exact expansion gives

```text
g22 = P22/A^2 + H22,
```

where `H22` is polynomial and has `A`-exponents `0,2,4,6,8`.  Thus the
provisional phrase “g22 has only an A^-2 polar part” is valid only if “polar
part” is read literally; it is false as a statement about the whole `g22`.

For

```text
L_n(R)=4*(12-n)*A^3*A'*R-8*A^4*R',
```

one has the exact identity

```text
-L22(P22/A^2) = 24*A*A'*P22 + 8*A^2*P22' in (A).
```

The regular `H22` contribution lands in `(A^3)`.  Therefore
`-L22(g22) in (A)`.

There is no raw `G22` slot.  Once D4--D21 vanish, the raw D22 determinant is
exactly `-L22(g22)`.  The source has eighteen D22 generators, one for every
degree `0..17`; their common target is the polynomial identity `D22(X)=1`.
This is crucial: the contradiction is not an evaluation at `X=0` or at
`A=0`.  It is simply

```text
D22 in (X^4-1)  and  D22=1,
```

which is impossible over a field.

## Mode and raw-window firewalls

The linked successor pieces of the newly born modes were checked separately:

```text
c18 at D19:  +9*c18*A'/A^2  plus  -9*c18*A'/A^2 = 0,
c20 at D21: +12*c20*A'/A^3 plus -12*c20*A'/A^3 = 0.
```

So D19 and D21 do not kill free predecessor modes.  `c18` and `c20` are
forced to zero only by their own birth-row polynomiality, exactly as required
by causal bookkeeping.

The literal G windows are pinned as

```text
G18: degrees 2..6, rank 5, nullity 0
G19: degrees 3..5, rank 3, nullity 0
G20: degrees 3..4, rank 2, nullity 0
G21: degree 3,     rank 1, nullity 0
G22: absent.
```

Their omitted lower and upper coefficients are not dropped.  At a
hypothetical raw solution they are mandatory additional equations, while the
full-rank maps identify the legal characteristic coefficient uniquely with
the raw window.  No solution of those additional equations can evade the
endpoint ideal containment.

## Literal 513-row replay

Five deterministic mutations solve each allowed raw `G` window canonically
through the preceding row and then stop.  Their first residuals are

```text
D18 =  6 - 36*X^4 + 30*X^8,
D19 =  6 - 48*X^4 + 42*X^8,
D20 = 12*X - 72*X^5 + 60*X^9,
D21 = 12*X - 84*X^5 + 72*X^9,
D22 = 12*X - 96*X^5 + 84*X^9.
```

The endpoint mutation satisfies every literal D4--D21 row and factors as

```text
D22=(X^4-1)*(-12*X+84*X^5).
```

Each fixture is replayed against all 513 serialized generators, records
per-generator source hashes for its first residual, and has live `-1` and
`2` scaling regressions.  Separately, the zero determinant row makes exactly
literal generator 495 equal `-1`, pinning the endpoint fold without relying
on a derived indexing convention.

## Scope

This is an exact field-point emptiness result for the pinned uniform
full-fixture branch-P system, conditional on the recursively pinned D8--D17
producer chain until hostile review.  It is not yet a scheme-theoretic unit
certificate and is not, by itself, a proof of the plane Jacobian conjecture.
No CAS, AWS, or Lean state was used.
