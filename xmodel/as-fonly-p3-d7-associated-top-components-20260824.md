# Map-only AS `p=3,D=7`: exact associated top-component gate

**Producer verdict: THE FIRST-DIGIT HIGH CARRY ROWS OF DEGREES 12 AND 11
HAVE THREE REDUCED LAYER-`7/6` COMPONENTS AND ONE LOAD-BEARING EMBEDDED
PRIMARY COMPONENT.  THIS IS A CHECKPOINT, NOT A CLASSIFICATION OF THE FULL
CAP-SEVEN LIFT LOCUS.**

- Date: 2026-08-24
- Field: `F_3`
- Geometry: complete total-degree-simplex first map digit
- Rows covered: divergence in homogeneous degrees 6 and 5; next-carry
  homogeneous degrees 12 and 11
- Engines: deterministic Python row generation and exact Singular
- Hostile different-model review: not yet run

## 1. Exact associated equation

Write the first map digit as

```text
P=x-x^3+3U,     Q=y+3V,
U=sum U_m,      V=sum V_m,
```

where `U_m,V_m` are homogeneous of total degree `m`.  The determinant
equation modulo nine begins with

```text
U_x+V_y=x^2.                                             (1)
```

The next carry is

```text
K=(U_x-x^2)V_y-U_yV_x.                                  (2)
```

A degree-seven next digit has divergence of degree at most six.  Therefore
every homogeneous coefficient of `K` in degrees greater than six must
vanish before any next digit can exist.

For the two highest layers, the fixed term `-x^2 V_y` has degree at most
eight.  Consequently the degree-12 and degree-11 rows of (2) are exactly
the corresponding rows of

```text
det D(U_7+U_6,V_7+V_6).                                  (3)
```

No initial form or generic denominator is used: the gate contains the
literal homogeneous divergence rows and every coefficient of (3) in the
two stated degrees.

## 2. Top degree-seven scheme

With

```text
U_7=sum_(i=0)^7 a_i x^i y^(7-i),
V_7=sum_(i=0)^7 b_i x^i y^(7-i),
```

the exact ideal consists of the nonzero degree-six divergence rows and all
13 coefficients of `det D(U_7,V_7)`.  Singular reports

```text
variables                         16
nonzero equations                 20
reduced Groebner basis size       16
dimension                          4
minimal associated primes          2
dimensions                         4,4
```

Both reduced components contain the common linear spine

```text
b5=b2=a5=a2=0,
a7=-b6,  a4=-b3,  a1=-b0,                         (4)
```

and differ in their remaining determinantal/Frobenius relations.  The
portable replay prints both prime ideals in full.

The top ideal is not radical.  Its complete primary decomposition has two
components: one nonprime primary thickening (Groebner size 18, associated
prime size 22) and one prime component (size 22).  There is no embedded
associated prime at this one-layer stage.

## 3. Attach degree six and carry degree 11

Adjoin all 14 coefficients of `U_6,V_6`, the complete homogeneous
degree-five divergence rows, and all degree-11 coefficients of (3).  This is
the original nonreduced layer scheme, not the intersection of the two top
minimal primes.  Exact output is

```text
variables                         30
nonzero equations                 38
reduced Groebner basis size       59
dimension                         10
minimal associated primes          3
minimal dimensions              10,10,8
complete primary components         4
```

The reduced components have a transparent descending interpretation.

1. The first two ten-dimensional components lie over the two top
   degree-seven components.  Every derivative-visible degree-six
   coefficient vanishes:

   ```text
   u6_1=u6_2=u6_4=u6_5=v6_1=v6_2=v6_4=v6_5=0.
   ```

   The six surviving degree-six coefficients have both exponents divisible
   by three.  They are precisely the Frobenius polynomials in `x^3,y^3` and
   have zero derivative.
2. The eight-dimensional rank-zero component sets the entire degree-seven
   layer to zero and retains the complete divergence-free degree-six layer.
   This is the honest descending branch; it must not be removed by a generic
   top pivot.

The scheme is again nonradical.  Its complete primary decomposition contains
the three minimal components above plus a fourth, embedded primary component
of dimension six (primary Groebner size 329, associated prime size 24).  Its
support is

```text
U_7=V_7=0,
u6_1=u6_2=u6_4=u6_5=v6_1=v6_2=v6_4=v6_5=0.      (5)
```

Thus the embedded support is exactly the intersection where the top layer
vanishes and the degree-six layer is purely Frobenius.  It carries no new
field-valued branch beyond the minimal components, but its nilpotent
thickening is load-bearing for later accepted digits and Fitting ranks.

## 4. Incidence of the frozen triangular point

The independently frozen triangular depth-six map has first digit

```text
U_0=x^3,       V_0=x^2y                              (mod 3).
```

Its homogeneous degree-seven and degree-six layers are both zero.  Hence its
projection to this gate is the origin.  Exact ideal reduction in the replay
shows that the origin lies on both top minimal components, all three
layer-`7/6` minimal components, and all four associated-prime supports,
including (5).

This incidence explains why a reduced generic-component calculation would
not faithfully describe the triangular point's later lift space.  It does
not say that the full lower-degree point belongs to every eventual component;
rows 10 through 7 and the Cartier row have not yet been attached.

## 5. Descending recurrence exposed by the gate

The exact layer-`7/6` decomposition gives the first step of a componentwise
compiler:

```text
nonzero degree-7 derivative layer
    -> one of two four-dimensional top types
    -> degree-6 follower is derivative-zero Frobenius;

rank-zero degree-7 layer
    -> retain the full degree-6 divergence-free problem;

their intersection
    -> retain the embedded Frobenius-supported primary thickening.
```

This recurrence replaces only a monolithic treatment of carry rows 12 and
11.  It does **not** replace or decide:

- carry rows of degrees 10, 9, 8, or 7;
- the bounded Cartier coefficient `[x^2y^2]K`;
- existence of the second accepted digit;
- any depth-seven map-only lift.

The next producer must descend componentwise through the degree-10 row,
keeping the primary component (5), rather than computing the already observed
opaque 42-variable/3,397-row global Groebner basis.

## 6. Refusal scope

This checkpoint is exact associated-scheme structure.  It proves neither
emptiness nor nonemptiness of the complete `D=7` next-depth system.  It makes
no simultaneous-gauge, all-depth, characteristic-zero, no-lift,
counterexample, or JC2 inference.  Minimal primes are used for navigation;
the original nonreduced ideal remains the object passed to subsequent carry
and Fitting gates.

## 7. Replay

From the case directory:

```sh
python3 replay_rows_and_incidence.py
M=7 DO_PRIMARY=1 python3 generate_top_gate.py | Singular -q
TOP=7 LOW=6 DO_PRIMARY=1 python3 generate_layers76_gate.py | Singular -q
shasum -a 256 -c MANIFEST.sha256
```

The Python replay independently reconstructs the exact row counts and the
triangular projection.  The two generated Singular programs recompute the
Groebner bases, radicals, minimal associated primes, complete primary
decompositions, and origin incidence.

