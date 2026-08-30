# One attachment forces maximal discriminant degree

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra delegated lane `/root/whole_portfolio_ideation`  
Frozen basis: `5bc4eea1c749045d54b4ee8053be8d85c4f3bc9f`  
Lifecycle: **EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint and exact scope

Let

```text
X subset P2 times P1,             [X]=dA+3B,          d>=1,
```

be a smooth irreducible hypersurface of literal degree three in the second
factor.  Let `pi:X->P2` be generically finite and finite on a neighborhood of

```text
H=pi^*(L_infinity)=X intersect (L_infinity times P1),
```

and assume `H` is reduced.  Assume the promoted dominant-`A2` first-leg
package: after resolving the full boundary containing `H` and the reduced
source-critical support of `pi`, every boundary component is rational and the
dual multigraph is a forest.  The exact inputs are the promoted rational-
forest integration

```text
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md
  body 6810 / 9c6501222049980161f209d57e1a575ebe80c4de1b8018aedf303f692e1dae46
```

and, for the connected-ramification mechanism in degree two, its promoted
binding use in

```text
c9871c92ce8748fd934dc57061f667b49952a1aba39aee43eb3af7b0aadbf392
  xmodel/bd-a2-ramification-lattice-closure-coordinator-integration-sol56-20260830.md
  body 8709 / 919a024751d6b28b02908f384297a59b791d1a0d52abb931f9fe5840a486df1a
```

The argument below proves the mechanism directly for every `d>=1`; it does
not charge the degree-two lattice enumeration.

Then there is exactly one **physical source point**

```text
p in H intersect Supp(R_pi).
```

This does not say that there is one analytic branch or one normalization
point over `p`.  In fact, the following stronger boundary conclusions hold.

1. `H` has exactly three irreducible components, each a smooth section of
   `H->L_infinity`.
2. Writing their bidegrees as `(a_i,1)` and ordering
   `a_1<=a_2<=a_3`, there are integers `0<=b<=a` with

   ```text
   (a_1,a_2,a_3)=(b,a,a),             d=2a+b.         (0.1)
   ```

3. If `ell` is a linear form vanishing at `pi(p)` on `L_infinity`, the
   target discriminant of the finite boundary cubic is

   ```text
   Disc(H/L_infinity)=c*ell^(4d),      c in C^*.       (0.2)
   ```

4. For a global trace-zero Miranda presentation of the associated finite
   locally free rank-three `C[u,v]`-algebra, the full affine target
   discriminant has exact total degree `4d`.  Consequently the presentation
   realizes the minimum possible coefficient degree among all global
   trace-zero bases:

   ```text
   deg(Delta)=4d,                       d_min=d.        (0.3)
   ```

5. The **one-dimensional boundary order** has normalization-index length
   `2d`, supported over `pi(p)`.  This is not the surface normalization-index
   divisor and is not a conductor assertion.

For `d=2`, (0.1) is the `F5` degree pattern `(0,1,1)`.  The theorem does not
assert that this pattern is realizable; the promoted quadratic lattice
theorem proves that it is not realizable in its declared block scope.
For `d>=3`, the promoted formula `p_g(X)=(d-1)(d-2)>0` already contradicts
the same dominant-first-leg package.  Thus the higher-degree implications
below are exact structural consequences of the stated hypotheses, but they
do not create new smooth survivors or a stronger closure at those degrees.

## 1. Relative canonical class and connected source ramification

In the Chow ring of `P2 times P1`, adjunction gives on `X`

```text
A^2=3,          A.B=d,          B^2=0,
K_X=(d-3)A+B.
```

Since `pi^*K_P2=-3A`, the relative canonical class is

```text
R_pi=K_X-pi^*K_P2=dA+B.                               (1.1)
```

Characteristic zero and generic finiteness make the determinant of `d pi`
a nonzero section of `O_X(dA+B)`.  The restriction of the ambient bundle
`O(d,1)` is ample for `d>=1`, so this section has a nonempty effective ample
Cartier zero divisor `R_pi`.

Its reduced support is connected.  Indeed, if the Cartier multiplicities
could be partitioned as

```text
R_pi=D_1+D_2,       Supp(D_1) disjoint Supp(D_2),
```

with both parts nonzero, ampleness would give

```text
D_i^2=R_pi.D_i>0,             D_1.D_2=0.
```

The two numerical classes are independent (proportional positive-square
classes cannot be orthogonal), contradicting the Hodge index theorem.  This
uses neither reducedness nor irreducibility of the Cartier divisor.

There is no ramification component contained in reduced `H`.  Locally choose
coordinates `(u,v)` on the target with `u=0` the infinity line and a fibre
coordinate `z`, so

```text
X: f(u,v,z)=0,                 H: h(v,z)=f(0,v,z)=0.
```

The critical section is represented by `f_z|X`.  If a reduced factor `c` of
the squarefree `h=cq` also divided `h_z`, then at the generic point of `c`

```text
c | c_z*q.
```

Coprimality gives `c|c_z`.  In characteristic zero this forces `c_z=0`, so
`c` is pulled back from a point of `L_infinity`; it is a vertical fibre of
`H->L_infinity`, contradicting finiteness near `H`.  Hence

```text
H and Supp(R_pi) have no common irreducible component.                (1.2)
```

The same chart gives the exact support bridge.  At a smooth point of `H`,
`h_z=0` exactly when the map `H->L_infinity`, `(v,z)|->v`, is critical.  At
a singular point both first derivatives of `h` vanish.  Therefore

```text
H intersect Supp(R_pi)
 = {singular points of H or projection-critical points of H}.        (1.3)
```

This equality concerns source points.  It is not an equality of the source
different with a target discriminant divisor.

Finally,

```text
H.R_pi=A.(dA+B)=4d>0.                                  (1.4)
```

Thus the two connected supports meet.

## 2. A forest permits exactly one physical attachment

The curve `H` is connected independently of the first-leg theorem.  On
`L_infinity times P1=P1 times P1`, it is a divisor of bidegree `(d,3)`, and

```text
H^1(P1 times P1,O(-d,-3))=0                           (2.1)
```

by Kunneth for every `d>=1`.  The divisor sequence therefore gives
`H^0(O_H)=C`; reducedness turns scheme-connectedness into connected support.

Resolve the reduced union `H union Supp(R_pi)`.  The reduced total transform
of each of the two connected curves is connected.  In the assumed full
boundary forest each is consequently a tree after retaining the exceptional
chains needed to resolve its own singularities.

If the original supports met at two distinct physical points, the exceptional
connector over each point would give a distinct path between these two
connected trees.  Contracting a spanning tree on each side and the interiors
of the two connector paths produces two parallel edges.  This is a graph
minor with first Betti number one, impossible in a forest.  Conversely (1.4)
guarantees at least one point.  Hence

```text
Supp(H) intersect Supp(R_pi)={p}                       (2.2)
```

as a set of physical source points.  The scheme-theoretic intersection has
total length `4d`; (2.2) says only that this length is concentrated at `p`.
It permits several branches of either curve and several points of the
normalization above `p`.

## 3. Riemann--Hurwitz forces three sections

Let `H_i` be an irreducible component, let `Htilde_i` be its normalization,
and let

```text
q_i:Htilde_i -> L_infinity
```

have degree `b_i`.  Finiteness near `H` gives `b_i>=1`.  Every ramification
point of `q_i` maps, by (1.3), to the single physical point `p`, hence lies
over the one target value `t_0=pi(p)`.  There may be several normalization
points above `p`, but all are in the same fibre `q_i^(-1)(t_0)`.

For a degree-`b_i` map, the total ramification contribution in one fibre is
at most `b_i-1`.  Riemann--Hurwitz therefore gives

```text
2g(Htilde_i)+2b_i-2 <= b_i-1,
```

or `2g(Htilde_i)+b_i<=1`.  Thus

```text
g(Htilde_i)=0,                    b_i=1.               (3.1)
```

The finite degree-one morphism `H_i->P1` is an isomorphism because the target
is normal.  So every component is a smooth section, not merely a rational
curve with a degree-one normalization map.  Since the total degree over
`L_infinity` is three, `H` has exactly three components.

Write their bidegrees as

```text
H_i:(a_i,1),              a_i>=0,       sum a_i=d.     (3.2)
```

Every intersection of two components is a singular point of `H`, so (1.3)
and (2.2) put it at `p`.  A disjoint pair would have
`H_i.H_j=a_i+a_j=0`, hence would be two distinct constant sections.  Since
`H` is connected, the third section would have to meet both at the sole
physical point `p`, impossible because the two constant sections have
different fibre coordinates.  Consequently all three sections pass through
`p`, and

```text
I_p(H_i,H_j)=H_i.H_j=a_i+a_j.                          (3.3)
```

Order `a_1<=a_2<=a_3`.  In completed local coordinates at `p`, with `t` a
uniformizer on the base, write the sections as `z=phi_i(t)`.  For three
distinct power series, the minimum among

```text
ord_t(phi_1-phi_2), ord_t(phi_1-phi_3),
ord_t(phi_2-phi_3)
```

is attained at least twice.  By (3.3) these orders are

```text
a_1+a_2,        a_1+a_3,        a_2+a_3.
```

If `a_2<a_3`, the first is the unique minimum, a contradiction.  Hence
`a_2=a_3=a`; putting `a_1=b` proves (0.1).  This argument also shows that no
such first-leg boundary exists for `d=1`, while `d=2` forces `(0,1,1)`.

## 4. The boundary target discriminant is one pure power

Let `q:H->L_infinity`.  Because `H` is a Cartier curve on the smooth ruled
surface and `q` is finite with no vertical component, `q` is finite flat of
rank three.  Its algebra is generically separable: `H` is reduced in
characteristic zero, and the three distinct sections are disjoint away from
`p`.  Thus its trace discriminant is a nonzero section.

In the given binary-cubic presentation the four leading coefficients are
sections of `O_P1(d)`.  The classical cubic discriminant is homogeneous of
coefficient-degree four, so it is a section of `O_P1(4d)`.  Its zero set is
the target non-etale locus of `q`.  By (1.3) and (2.2), that locus is supported
only at `t_0`; it is nonempty because all three sections meet there.  A
nonzero section of `O_P1(4d)` has a zero divisor of degree `4d`.  Therefore

```text
div(Disc(q))=4d*[t_0],
Disc(q)=c*ell^(4d),                  c in C^*.          (4.1)
```

This is a **target** discriminant on `L_infinity`.  It is not the source
ramification divisor `R_pi`, although (1.3) relates their supports.  It is
also not obtained by slicing the affine surface normalization sequence.

As an independent multiplicity check, the normalization is the disjoint
union of the three sections.  The pairwise contact sum is

```text
sum_(i<j) I_p(H_i,H_j)
 =2(a_1+a_2+a_3)=2d.
```

The discriminant of three generically distinct roots is the square of their
pairwise differences, giving total order `4d`, in agreement with (4.1).

## 5. No top-degree cancellation; the basis is degree-minimal

Now assume the incidence comes from a global trace-zero Miranda basis of a
finite locally free, generically separable rank-three algebra over
`C[u,v]`.  Denote the four affine coefficients by `alpha,beta,gamma,delta`,
each of total degree at most `d`, and write their degree-`d` homogeneous parts
with a subscript `d`.  They define the boundary cubic `H`.

The promoted intrinsic-discriminant integration

```text
410de2f569e2ad5599152fdd9414198f012dbdced7d17c5a51dde0096fe4601e
  xmodel/bd-fix3-quadratic-discriminant-conductor-coordinator-integration-sol56-20260830.md
  body 7828 / 722d21d844f08c7a49b6231263b2a5a2e5d744e369192c39d71ac4c5ab3cb5a1
```

identifies the trace discriminant exactly with the classical binary-cubic
formula and proves basis invariance up to a nonzero constant.  Since that
formula is quartic in the coefficients, the homogeneous degree-`4d` part of
the full affine polynomial `Delta(u,v)` is literally

```text
Disc(alpha_d,beta_d,gamma_d,delta_d).
```

Equation (4.1) says this polynomial is `c*ell^(4d)`, not zero.  Therefore no
cross-term cancellation can lower the full degree:

```text
deg(Delta)=4d.                                         (5.1)
```

This also proves that the current coefficient maximum is exactly `d`, not
merely at most `d`.

For any other global trace-zero basis with coefficient maximum `e`, the same
promoted theorem gives

```text
deg(Delta)<=4e.
```

A change matrix lies in `GL_2(C[u,v])`, whose determinant is a nonzero
constant, so the trace discriminant changes only by a scalar and its degree
remains `4d`.  Hence every such `e` satisfies `e>=d`.  The displayed basis
realizes `e=d`, proving

```text
d_min=d.                                               (5.2)
```

No reverse form of the general `DISC8-INDEX` inequality is used.  Equality
comes from the nonzero boundary discriminant plus the already existing
degree-`d` basis.

## 6. Boundary normalization-index length

This section concerns only the finite flat **curve algebra**

```text
C=q_*O_H over O_P1.
```

Its normalization is

```text
Ctilde=q_*O_(Htilde)=O_P1^3,
```

because the three normalized components map isomorphically to the base.  The
quotient `Ctilde/C` is supported at `t_0`.  The arithmetic genus of a
bidegree-`(d,3)` curve is

```text
p_a(H)=(d-1)(3-1)=2d-2.
```

The normalization has three genus-zero components.  The normalization exact
sequence, or equivalently Euler characteristics, gives

```text
length(Ctilde/C)
 =3*chi(O_P1)-chi(O_H)
 =3-(1-p_a(H))
 =2d.                                                  (6.1)
```

Localizing at `t_0`, both orders are free of rank three over the DVR, so the
determinant/Fitting index has order `2d`.  Since the normalized split algebra
has unit discriminant, the lattice identity gives boundary discriminant
order `2*(2d)=4d`, a third check on (4.1).

The qualifications are load-bearing:

* `C` is reduced but generally nonnormal; (6.1) explicitly measures that
  nonnormality.
* The three points of `Htilde` over the triple physical point remain three
  distinct normalization points.  They merely lie over the same base value.
* This index is not the normalization-index divisor of the two-dimensional
  affine algebra, and no base-change or Tor assertion connects them here.
* The Fitting index is not called the conductor.  Although the boundary
  curve is Gorenstein as a Cartier divisor, no conductor-length identity is
  needed or promoted.

## 7. Attack ledger and maximum safe conclusion

The requested failure modes have the following dispositions.

```text
top-degree cancellation:       impossible by nonzero (4.1);
source/target conflation:       separated in Sections 1, 4, and 6;
nonnormal boundary order:       allowed and measured by length 2d;
multiple normalization points: allowed; RH uses one target fibre, not one point;
nonconstant basis determinant: impossible in GL_2(C[u,v]);
basis-degree reduction:         impossible because deg(Delta)=4d;
surface-index/curve-index swap: explicitly not made.
```

The maximum safe theorem is exactly Sections 0--6 under smoothness,
reducedness, projective finiteness near infinity, and the dominant-first-leg
rational-forest package.  It does not extend automatically to nonreduced
infinity, a singular incidence surface, a vertical/projective coefficient
basepoint, fibre-degree drop, or a presentation not arising from the stated
finite locally free cubic algebra.  In those strata the critical Cartier
divisor, connectedness, flat boundary algebra, or nonzero leading
discriminant can fail.

Within the already promoted smooth theory, the result is logically
redundant as an exclusion: `d>=3` is already impossible by geometric genus,
`d=2` is closed by the reviewed lattice theorem, and (0.1) has no solution
for `d=1`.  Its new content is the exact conditional boundary shape,
maximal-discriminant statement, and basis-minimality certificate; using those
features on a singular compactification would require a separate theorem.

The pure-power leading discriminant implies that the projective closure of
the full affine target discriminant has one point at infinity.  Coupling that
fact to `A(F)`, one-place curve theorems, complement fundamental groups, or
cubic monodromy is promising **future work only**.  No such theorem is
charged here.

No general cubic-block closure, higher-block obstruction, occurrence or
coverage theorem, primitive-monodromy conclusion, polynomial map,
counterexample, or JC2 conclusion follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16533`.
- Body SHA-256:
  `ba0862b9c08538cfe35499c4d0cfe1c50b2dcf98f930c05c0c882e7552adfc0f`.
- Frozen basis: `5bc4eea1c749045d54b4ee8053be8d85c4f3bc9f`.
