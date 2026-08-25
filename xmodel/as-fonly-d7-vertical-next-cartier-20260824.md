# AS F-only `p=3,D=7`: first following Cartier gate

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

## Headline

After the full homogeneous degree-five current digit is restored, the first
following divided carry has exactly one bounded de Rham obstruction.  The
integer source reduces it to the single row

```text
c5_3+d5_2+2h^2=0.                                 (1)
```

Appending (1) to the full-C5 D7 system gives a `20 x 17` affine gate.  Its
exact literal-F3 result is

```text
compatible Frobenius choices   structural bases
0                                  208
3                                  180
9                                 1435
27                                 364,                           (2)

compatible structural+Frobenius states: 23,283 / 1,594,323
visible current-digit solutions: 1,085,103.                       (3)
```

Thus this bounded branch has many one-step finite lifts.  This is not an
all-depth or characteristic-zero lift.

## 1. Integer source of the row

With

```text
E=L/3+K+C_x+D_y=3E1,
F=E1+M,                                             (4)
```

the replay adjoins all homogeneous degree-two and degree-three current
digits before constructing `E` and `M` over the integers.  At the only
Cartier monomial of total degree at most six it obtains

```text
[x^2y^2]E1 = c5_3+d5_2+2h^2,
[x^2y^2]M  = 0.                                    (5)
```

The coefficient of `E` is formally divisible by three; no equation is
cleared, no canonical representative is selected, and no piecewise carry is
used.  Equation (1) is therefore exactly `[x^2y^2]F=0`.

The accepted lower rows that could interact with (5) are

```text
degree 1: c2_1+2d2_0, 2c2_2+d2_1,
degree 2: c3_1, 2c3_2+2d3_1+2h, d3_2.             (6)
```

They are always solvable and share no variable with (1).  Accepted degrees
zero and three are divergence-surjective; degree four was handled by the
full-C5 gate, whose `x^2y^2` row is identically zero.  These facts make (1)
the complete lower Cartier condition, not a chosen slice.

## 2. Sufficiency for one next digit

The charged branch has already passed carry degrees ten through seven.
Hence after (1), `F mod 3` has total degree at most six.  For the divergence
of a cap-seven pair, the only cokernel monomial in that range is `x^2y^2`.
Therefore there are polynomials `W,Z` of total degree at most seven with

```text
F+W_x+Z_y=0 mod 3.                                 (7)
```

Adding `27W,27Z` to the two map coordinates changes the order-27 Jacobian
coefficient by `W_x+Z_y`, because the seed Jacobian is the identity modulo
three.  Equation (7) gives one genuine finite lift through the next digit.
No choices of `W,Z` are counted in (3).

## 3. Exhaustive finite compiler

For every structural base `(P,Q,R,T,s,w,h)`, the replay forms the `20 x 17`
current-digit matrix `A`, the six Frobenius columns `Frob`, and the constant
column.  It applies the exact rank formula and independently enumerates all
729 Frobenius values against the row-reduced cokernel of `A`.  The two
methods agree base-by-base.  The compatible literal-state stream hash is

```text
71ed86c8ed086e46a0b3bba6347a3a7553e5b2a3181b8e938c6a6861fdcf6d79. (8)
```

The full rank-triple histogram is emitted in the portable replay.

## 4. Consumed artifacts and refusal scope

This gate consumes the exact full-C5 producer

```text
xmodel/as-fonly-d7-vertical-full-c5-d7-gate-20260824.md
SHA-256 907dcc72523eb228a7ac6581826460601030e56c996d4df583b2fad274f09a6e
```

and its pinned source ancestors.  Its interpretation is provisional until
the parent and this successor receive hostile review.

The visible count omits derivative-zero degree-six spectators, lower
divergence kernels, and the new next-digit kernel.  It is not a count of
distinct maps.  No subsequent divided carry, recurrence, all-depth
lift/no-lift, characteristic-zero, counterexample, or JC2 result is claimed.
