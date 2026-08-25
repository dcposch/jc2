# AS F-only `p=3,D=7`: full degree-five current-digit D7 gate

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

## Headline

The zero-`C5,D5` cap-boundary scheme is a useful slice, but it is not the
full vertical D7 compatibility gate.  Homogeneous degree-five current digits
cross the degree-four first digit in the mixed carry and contribute at total
degree seven.  Attaching all twelve of them gives an exact affine system

```text
7 reviewed D8 rows
+ 4 nonzero accepted-degree-4 rows
+ 8 full D7 rows
= 19 equations in 17 visible current-digit unknowns.             (1)
```

Over all `3^7=2187` structural bases, an exact rank compiler and an
independent enumeration of all `3^6` first-digit Frobenius values agree:

```text
compatible Frobenius choices   structural bases
0                                  172
3                                  100
9                                 1539
27                                 376.                            (2)

compatible structural+Frobenius states: 24,303 / 1,594,323
visible current-digit solutions over them: 3,253,689.             (3)
```

Thus this successor is nonempty, but it does not yet cross the following
Cartier/divided-carry gate.

## 1. Exact source

The frozen full-`E1` source license proves that in the charged vertical
normal form

```text
[E1+M]_7=[single-Frobenius K/3+M]_7.              (4)
```

This producer independently rebuilds (4) over the integers after adjoining

```text
C5=sum(c5_i*x^i*y^(5-i)),
D5=sum(d5_i*x^i*y^(5-i)).                          (5)
```

It constructs `M` with the full six-direction Frobenius first digit and
`C=C5+C6+C7,D=D5+D6+D7`, reduces modulo three only afterward, and then
applies the registered accepted-D5/D6, D8-unit-pivot, and triangular
coordinate substitutions.  The eight-row hash is

```text
b4a522561ba435cc6797384bcb9ab81731193ab7ea7d36151a1b13af56f50128. (6)
```

Setting all `C5,D5` variables to zero recovers the eight-row frozen slice.
Rows `0,1,3,4,6,7` change; the two invariant rows remain

```text
fc=0, fd=0.                                        (7)
```

This is the negative control showing why the full layer is load-bearing.

## 2. Accepted degree-four block and lower completion

At degree four, `L/3` is absent, so the exact accepted row is
`K_4+div(C5,D5)`.  Its five coefficients are

```text
c5_1+2d5_0,
2c5_2+d5_1,
0,
c5_4+2d5_3+2h,
2+2c5_5+d5_4.                                     (8)
```

The `x^2y^2` coefficient is identically zero: the universal first-carry
Cartier class vanishes source-honestly.  Hence (8) has four nonzero rows.

For target homogeneous degrees `0,1,2,3,4`, the divergence ranks and
Cartier-cokernel dimensions are

```text
(rank,cokernel)=(1,0),(2,0),(3,0),(4,0),(4,1).    (9)
```

The unique low cokernel is `x^2y^2`, already zero in (8).  Current digits of
degree at most four can affect the mixed carry only through degree six, so
they cannot change the D7 rows.  Therefore they can be completed after (1)
without altering this gate.  The already registered degree-six and
degree-seven current-digit pivots cover the two higher accepted blocks.

Six derivative-zero homogeneous degree-six current directions are invisible
spectators.  They, and the lower divergence kernels, are not included in the
visible solution count (3); (3) is not a count of distinct full maps.

## 3. Exact finite compiler

For a structural base

```text
(P,Q,R,T,s,w,h) in F3^7,
```

let `A` be the `19 x 17` current-digit matrix, `F` the six Frobenius columns,
and `b0` the constant column.  With

```text
r=rank(A), c=rank([A F]), d=rank([A F b0]),        (10)
```

the compatible Frobenius fibre is empty if `c<d` and otherwise has
`3^(6+r-c)` points.  Summing `3^(23-c)` gives the visible current-digit total
in (3).

The replay also row-reduces `A` separately at every structural base and
tests all 729 Frobenius values against the resulting cokernel rows.  It
matches (2) base-by-base.  The compatible literal-state stream hash is

```text
2a4857f137938d56e4edea7988f0404fe4ff5bd954440b27870a811865fb8c7b. (11)
```

The full rank-triple histogram is emitted by the portable replay.

## 4. Consumed artifacts and scope

This gate consumes:

```text
xmodel/as-fonly-d7-postd10-d98-f3-corrected-source-review-grok-20260824.md
SHA-256 156053c538c4c826bc0feb345d25d91f015543464e0ab9d7734ab190cd7842c4

xmodel/as-fonly-d7-vertical-d7-source-license-20260824.md
SHA-256 772d3627965037846f291ca5289c3cab26375e7bcea9edb095a95381fed84b27

xmodel/as-fonly-d7-vertical-state-sufficiency-review-grok-20260824.md
SHA-256 6ab373bf9214c54f506cd368473aff02ed472a20e9797037f83a9745c384bc17
```

The 13-component result for the zero-`C5,D5` scheme remains an exact slice
theorem; none of its components is promoted to a component of (1).

No following lower residual or divided Cartier carry is computed here.  No
all-depth lift/no-lift, characteristic-zero, counterexample, or JC2 claim is
made.
