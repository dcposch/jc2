# Hand certificate: the loaded relative-order-six `A` face is empty

Date: 2026-08-26

Status: **EXACT SOURCE-ROW CERTIFICATE, INDEPENDENT OF THE STANDARD-BASIS
OUTPUT.**

Work on `D(p*m*kk)` and write

```text
x=x6, y=y6, r1=r112, r0=r012, s0=s012.
```

Here `(x,y)` are the two transverse K2-kernel coordinates at relative
sigma order six.  The exact complete-source compiler emits no row below
absolute grade 42.  At grade 42 its seven rows are

```text
G1 = -3*r1*m^2/8 + 3*s0*m/4,
G2 = -5*kk*p^6/4096 - 3*r0*m^2/8 + 3*y^2/8 - mu20,
G3 = -3*r1*m^2*p/32 - 3*x*y*m/8 + 3*s0*m*p/16,
G4 =  3*x^2*m^2/32 - 3*r0*m^2*p/16 - 3*y^2*p/16,
G5 = -3*r1*m^2*p^2/256 + 3*x*y*m*p/32
       + 3*s0*m*p^2/128,
G6 = -3*r0*m^2*p^2/64 + 3*y^2*p^2/64,
G7 =  3*r1*m^2*p^3/1024 - 3*x*y*m*p^2/256
       - 3*s0*m*p^3/512.
```

All three delayed loads and the only target capable of entering this
grade are retained.  They occur in `G2`; the obstruction below uses odd
rows together with `G4,G6`, so no load or target has been discarded.

The source rows give the exact invariant

```text
G3-(p/4)*G1 = -(3/8)*m*x*y.                       (1)
```

Since `m` is a unit, (1) forces `x*y=0`.  The two charts `D(x)` and `D(y)`
therefore exhaust the nonzero kernel exceptional divisor.

On `D(x)`, equation (1) gives `y=0`; then `G6=0` gives `r0=0`, and

```text
G4 = 3*x^2*m^2/32,
```

which is a unit times `x^2`, a contradiction.

On `D(y)`, equation (1) gives `x=0`; then `G6=0` gives
`r0*m^2=y^2`, and

```text
G4 = -3*y^2*p/8,
```

again a unit times `y^2`, a contradiction.  This proves that the full
relative-order-six kernel face is empty.  The argument is exact over
characteristic zero and uses only the displayed complete-source grade-42
rows.  The independently computed standard bases on both charts are
corroborating scheme-theoretic certificates, not inputs to this hand
derivation.

Scope: fixed delayed-load repeated-root `A`, relative kernel order six,
and `D(p*m*kk)`.  It does not classify the homogeneous intervals, the
ramified `q=15/2` face, the separate `q>15/2` slice, `m=0`, terminal or
Taylor receivers, order two, or JC2.
