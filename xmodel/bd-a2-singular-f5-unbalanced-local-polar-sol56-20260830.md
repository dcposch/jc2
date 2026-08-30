# Singular F5 unbalanced local polar: exact U3, U5, and U6 families

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra sublane `/root/u_rows_full_family`  
Frozen basis: `eb6c6aeea48ab76f61e606e5addc4107a840f9fb`  
Lifecycle: **EXACT PROVISIONAL LOCAL THEOREM / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

In the charged normal, reduced, finite-near-infinity F5 quadratic-incidence
scope, every unbalanced singular row has a coefficient-invariant strict
Cartier-polar factorization.  With the marking conventions in Section 1, the
complete table is

| row | strict `A`-degree partition | exceptional polar coefficients `m` | strict contact vector `n=Cm` | physical polar sites |
|---|---:|---:|---:|---|
| `U_3/A_3` | `4+4` | `(2,2,1)` | `2e1+e2` | smooth `E1`; node `E1 cap E2` |
| `U_5/D_5` | `2+3+3` | `(2,4,5,3,3)` | `e2+e4+e5` | smooth `E2,E4,E5` |
| `U_6/D_6` | `3+5` | `(2,4,5,6,3,3)` | `e2+e4` | smooth `E2,E4` |

Every displayed strict germ is reduced and occurs in the Cartier different
with coefficient one.  The entries of each partition are the orders of the
target boundary function `u` on the normalizations of the strict germs; they
sum to the exact local intersection length eight.

There is no hidden modulus-special degeneration within any named cell.  In
particular, if

```text
delta=b'(0)+c''(0)/2,
```

then `delta!=0` is exactly the `U_5/D_5` cell and separates its two pair
roots, while `delta=0` is exactly the `U_6/D_6` cell and has a forced nonzero
next normal-form coefficient.  The provisional patterns `4+4`, `2+3+3`, and
`3+5` are therefore confirmed, but the conjectured `D_5` vector supported at
only two vertices is false: the correct vector has three distinct sites
`E2,E4,E5`.

This is a local analytic theorem.  It does not assert global effectivity,
that distinct germs belong to distinct global primes without a separate
forest argument, or that any row is realized by a polynomial map.

## 1. Exact hypotheses, equation, and marking

Work over `C` in the completed analytic local ring at the singular F5 point.
Use target coordinates `(u,v)` with infinity `u=0` and source-line coordinate
`z`.  The exact incidence equation and its reduced infinity fibre are

```text
h(v,z)=z(z-v)((1+v)z-v),
f(u,v,z)=h(v,z)+u(a(z)u+b(z)v+c(z)),                 (1.1)
c(0)=0.
```

The surface germ is assumed normal and reduced, and projection to `(u,v)` is
finite near the reduced boundary.  The source Cartier different is the
divisor of

```text
p=f_z                                                       (1.2)
```

on `f=0`, where the derivative is at fixed target coordinates `(u,v)`.  A
strict germ's `A`-degree is `ord(u)` on its normalization.  No exceptional
coefficient, target-discriminant multiplicity, or formal branch flag is being
called an `A`-degree.

The unbalanced cells are

```text
b(0)=0, c'(0)!=0:                 U_3/A_3;
b(0)=c'(0)=0, a(0)!=0:           U_5/D_5 or U_6/D_6. (1.3)
```

Use the standard diagrams

```text
A3:  1--2--3;
D_r: 1--2--...--(r-2), with spins r-1,r at r-2.       (1.4)
```

For `A3`, the two tangent section branches meet `E1` and `L={z=0}` meets
`E2`, so the marked boundary vector is `2e1+e2`.  For `D5`, `L` meets `E1`;
the two section branches use one spin.  If that retained spin is called
`E5`, the boundary vector is `e1+2e5` (spin reversal gives the convention
`e1+2e4` used in earlier packets).  For `D6`, the boundary vector is
`e1+e5+e6`.  The polar vectors below are unchanged by the `D5` spin swap.

## 2. The full U3/A3 family

Write

```text
b(z)=zB(z),       c(z)=zC(z),       C(0)=c'(0)=c1!=0.
```

Normality forces `a0=a(0)!=0`.  Indeed, if `a0=0`, then `a(z)` is divisible
by `z`, and every term of (1.1) is divisible by `z`; the surface is reducible
and is outside the charged normal cell.

The Hessian in `(u,z)` is nondegenerate.  Its critical centre satisfies

```text
u0=-v^2/c1+O(v^3),
z0=2a0*v^2/c1^2+O(v^3),
f(u0,v,z0)=a0*v^4/c1^2+O(v^5).                       (2.1)
```

The parametric Morse lemma therefore gives `XY+unit*v^4=0`, proving the
`A3` tag without specializing any higher coefficient.

Because `p_u(0)=c1`, the polar equation uniquely solves `u=U(v,z)`.  Two
Newton regions exhaust its strict curve.

### 2.1 The cusp region

Give `(v,z,u)` weights `(2,3,4)`.  The leading polar equation is

```text
c1*u+v^2-4vz=0.                                      (2.2)
```

After substituting its solution in `f`, the weight-eight edge is

```text
2v*z^2+(a0/c1^2)*v^4=0.                              (2.3)
```

The nonvertical factor is the reduced irreducible cusp

```text
v=t^2,
z=lambda*t^3+O(t^4),       2lambda^2=-a0/c1^2,
u=-t^4/c1+O(t^5).                                    (2.4)
```

Thus it has `A`-degree four.  Both edge coefficients in (2.3) are forced
nonzero by normality and the definition of the cell.

### 2.2 The tangent-pair midpoint

Put `y=z-v` and give `(z,y,u)` weights `(1,2,4)`.  Since

```text
h=z*y*(y*(1-z)+z^2),
```

the leading polar equation is `z(2y+z^2)=0`.  The strict solution has

```text
y=-z^2/2+O(z^3),
u=z^4/(4c1)+O(z^5).                                  (2.5)
```

It is a unique smooth reduced germ of `A`-degree four.  Equations
(2.3)--(2.5) prove the exact `4+4`; no higher coefficient of `a,B,C` lies on
either controlling edge.

### 2.3 Marked A3 resolution

In the first `v`-chart, put `u=vU,z=vZ`.  The reduced exceptional equation is

```text
U(a0*U+c1*Z)=0.                                      (2.6)
```

Call the component `U=0`, which contains the two section directions `Z=1`,
`E1`; call the other outer component `E3`.  Blowing up their residual `A1`
point inserts `E2`, which is met by `L`.  At the generic points of
`E1,E2,E3`, direct substitution in `p` gives

```text
m=(2,2,1).                                           (2.7)
```

The smooth germ (2.5) meets `E1` at `Z=1`.  The cusp (2.4) approaches the
residual point tangent to `E1`, and after the `A1` blowup passes through the
node `E1 cap E2`.  Hence its two node contacts plus the smooth contact give

```text
n=C_A3*m=2e1+e2.                                     (2.8)
```

The equality of (2.8) with the formal boundary contact vector does not
identify the polar germs with boundary germs: the smooth polar, the two
sections, and the nodal cusp are physically distinct analytic germs.

## 3. Exact square completion for every D cell

Now write

```text
b(z)=zB(z),       c(z)=z^2C(z),       y=z-v,
Delta(z)=B(z)+C(z),
L=b(z)v+c(z)=z(-B(z)y+zDelta(z)).                     (3.1)
```

Since `a0!=0`, set `x=a(z)u+L/2`.  Multiplying `f` by the unit `a(z)` gives

```text
a*f=x^2+a*h-L^2/4.
```

Define the one-variable units/functions

```text
P=a(1-z)-zB^2/4,
Q=a+B*Delta/2,
Y=y+z^2Q/(2P),
K=Delta^2+zQ^2/P.                                    (3.2)
```

A direct completion, with no discarded term, is

```text
a*f=x^2+zP*Y^2-(z^4/4)K.                             (3.3)
```

Put `delta=Delta(0)=b'(0)+c''(0)/2`.  If `delta!=0`, then
`K(0)=delta^2` and (3.3) is `D5`.  If `delta=0`, then

```text
K=z*(a0+O(z)),                                       (3.4)
```

because `Q(0)^2/P(0)=a0`.  Thus (3.3) is exactly `D6`; it cannot jump to
`D7` or higher while `a0!=0`.  Equations (3.2)--(3.4) are the full-family
normal-form and modulus audit.

The square completion is used to identify the singularity and resolution.
The polar calculations below still use `p=f_z` in the original target
coordinates, so no source-coordinate derivative is mistaken for the target
map's Cartier different.

## 4. Strict polar germs in the D5 and D6 cells

At fixed `v`, differentiation in `(z,y=z-v)` is the operator
`partial_z+partial_y`.  There is first a common transverse region.  With
`z=t^2`, its initial polar equation and surface equation are

```text
y(y+2z)=0,
a0*u^2+z*y^2=0.                                      (4.1)
```

The root `y=-2z` gives one reduced irreducible germ

```text
y=-2z+O(z^(3/2)),
u^2=-(4/a0)z^3+higher,
ord_t(u)=3.                                          (4.2)
```

The other root `y=0` is the tangent-pair region.

### 4.1 D5: delta nonzero

Set `z=t`, `y=Y0*z^2`, and initially `u=U*z^2`.  The leading surface and
polar systems are

```text
U(a0*U+delta)=0,
(b'(0)+c''(0))*U+2Y0+1=0.                            (4.3)
```

The two roots `U=0` and `U=-delta/a0` are distinct.  The second is a smooth
germ of `A`-degree two.  For the zero root, `Y0=-1/2`; writing
`u=W*z^3+...` in the next surface equation gives

```text
delta*W-1/4=0,
u=z^3/(4delta)+O(z^4).                               (4.4)
```

This is a second smooth germ, of `A`-degree three.  Together with (4.2) the
partition is exactly `2+3+3`.  The nonzero quantities `a0`, `delta`, and
`1/(4delta)` prevent every possible leading collision or cancellation.

### 4.2 D6: delta zero

The pair polar equation now forces

```text
y=-z^2/2+O(z^3).
```

The leading surface equation is

```text
a0*u^2-z^5/4=0.                                      (4.5)
```

It is one reduced irreducible germ, parametrized by `z=t^2` with
`ord_t(u)=5`.  The odd exponent five prevents analytic splitting, and the
coefficient `1/(4a0)` is forced nonzero.  With (4.2), the exact partition is
`3+5`.

In all three cells, the relevant polar equation has a simple transverse
derivative at the generic point of every listed germ.  Hence each strict
prime has Cartier coefficient one.  Also

```text
length C[[v,z]]/(h,h_z)=8,                            (4.6)
```

and none of the strict germs is contained in `u=0`; the three partitions
independently saturate (4.6).

## 5. Marked D5 and D6 sites and exceptional vectors

The following blowup audit also fixes a subtle normalization trap.  In the
first `z`-chart of (3.3), put `x=zx1,Y=zy1`.  The generic strict surface has

```text
D5: x1^2+z*unit*y1^2-z^2*unit=0;
D6: x1^2+z*unit*y1^2-z^3*unit=0.                     (5.1)
```

The generic exceptional component is `E2`.  On the normalized surface its
local uniformizer is `x1`, and `z` has order two.  Therefore a displayed
factor `z^2` in the raw polar chart contributes exceptional order four, not
two.  The `y`-chart point at infinity is an `A1`; resolving it creates `E1`,
which is met by `L`, and joins it to `E2`.

The transverse germ (4.2) has `y1=-2+...` and meets a smooth point of `E2`.

For `D5`, the point `y1=0` is the residual `A3`.  Its next `z`-chart has two
spin components distinguished by

```text
x/z^2=+delta/2+...,
x/z^2=-delta/2+....                                  (5.2)
```

The degree-three pair germ (4.4) lands on the first and the degree-two pair
germ lands on the second (interchanging the spin names changes nothing).
Thus the three physical sites are `E2,E4,E5`, and

```text
n_D5=e2+e4+e5,
m_D5=C_D5^(-1)n_D5=(2,4,5,3,3).                     (5.3)
```

If the section-retaining spin is named `E5`, the degree-three pair polar is
on `E5` and the degree-two pair polar is on `E4`; spin reversal gives the
opposite sentence.  In either convention, (5.3) is symmetric.  This proves
that the earlier candidate `e1+2e5` for the polar was a confusion with a
two-site boundary marking, not the actual different.

For `D6`, the point `y1=0` is the residual `D4`.  The next `z`-blowup creates
its central component `E4`; the degree-five germ (4.5) meets it transversely.
The transverse degree-three germ remains on `E2`.  Consequently

```text
n_D6=e2+e4,
m_D6=C_D6^(-1)n_D6=(2,4,5,6,3,3).                   (5.4)
```

The two `D6` section branches instead use the spin vertices `E5,E6`; they are
not being conflated with the polar sites in (5.4).

## 6. Exact replay, negative controls, and scope

The standard-library replay

```text
ops/f5_unbalanced_polar_replay.py
SHA-256 ee488fbb19c243815f85254d8c2d3a06ba77991b1cf8e92d70e57b4b0317ac82
```

checks all three partitions, the three Cartan products, the nonzero U3 edge
controls, the separated D5 roots and lift, and the forced D6 coefficient.
It passes identically in ordinary, optimized, and double-optimized Python:

```text
python3 ops/f5_unbalanced_polar_replay.py
python3 -O ops/f5_unbalanced_polar_replay.py
python3 -OO ops/f5_unbalanced_polar_replay.py
```

The replay is arithmetic corroboration, not a replacement for the analytic
Newton and blowup arguments above.

Negative controls are exact:

1. `U3` with `a0=0` factors by `z` and is not a normal-surface degeneration
   inside the named cell.
2. `D5` cannot merge its pair roots while `delta!=0`.
3. `delta=0` does not create a special `D5` polar; it moves to the named
   `D6` cell, where (3.4) forbids a higher-D cancellation.
4. Higher coefficients of `a,b,c` lie above every controlling Newton edge
   and can move attachment points only within the displayed components.

Nothing in this packet proves effectivity of a marked row, globalization of
its local germs, equality or inequality of their global carrier primes,
existence of a finite first-leg algebra, or occurrence in a polynomial map.
It supplies no counterexample and no conclusion about JC2.  Formal lattice
contacts, physical sites, strict analytic germs, global primes, Cartier
coefficients, and target degrees remain separately typed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13147`.
- Body SHA-256:
  `590d3ae673f01711627a5adddec9ce174e345617b7aba5402c82db05487ecc53`.
- Frozen basis: `eb6c6aeea48ab76f61e606e5addc4107a840f9fb`.
