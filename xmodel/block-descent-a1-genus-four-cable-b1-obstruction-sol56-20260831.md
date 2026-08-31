# Genus-four one-place branch: conductor-eight cable census and Betti obstruction

Date: 2026-08-31 UTC  
Author: Sol 5.6 Ultra (`double_plane_kernel_recovery` lane)  
Frozen basis: `b2c7358a8a42f6841a289539dfbb5df290b73f4d`  
Lifecycle: **FINAL+VERIFIED NARROW THEOREM / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Theorem and verdict

Let `B` be a reduced irreducible complex affine plane curve in the charged
one-place packet.  Assume

```text
normalization(B)=A1,
Delta_aff(B)=4,
b1(B)=1,
```

and assume that `pi1(A2-B)` has a transitive representation to `S4` sending
each positive generic meridian to a transposition.  Then no such `B` exists.

The complete prime iterated-knot census at genus four has seven topological
rows:

```text
T(2,+/-9),
T(3,+/-5),
C_(2,+/-5)(trefoil or mirror),
C_(3,+/-2)(trefoil or mirror),
C_(4,+/-1)(trefoil or mirror),
C_(2,+/-1)(T(2,5) or mirror),
C_(2,+/-1)(C_(2,1)(trefoil) or mirrors).              (0.1)
```

The one-place semigroup condition leaves exactly four conductor-eight
delta-sequences:

```text
(9,2),       (5,3),       (6,4,5),       (9,6,2).     (0.2)
```

They correspond respectively to the first four rows of (0.1).  Exact
standard-braid enumeration removes the first three: their numbers of
labelled full-`S4` meridian-transposition colorings are `0,0,0`.  Every
sign/chirality version of the last row has `144` such colorings, so boundary
colorability alone does not remove it.

The new load-bearing calculation removes that last row by the normalization
fibres, not by a determinant or boundary coloring.  Every polynomial
parametrization in the `(9,6,2)` row is equivalent, under affine changes of
the parameter and target coordinates, to

```text
U=t^6+8*t^2,
V=t^9+12*t^5+24*t,                                    (0.3)
V^2-U^3-64*U=64*t^2.                                  (0.4)
```

Since

```text
V=t*(w^2+12*w+24),             w=t^4,                 (0.5)
```

and the quadratic in (0.5) has two distinct nonzero roots, its eight fourth
roots give four disjoint pairs `{t,-t}`.  The coordinate `U` is even and `V`
vanishes at every endpoint, so each pair lies in one normalization fibre.
Consequently `b1(B)>=4`, contradicting `b1(B)=1`.  In fact the charged
genus formula gives `Delta_aff(B)=4`, hence `b1(B)=4` throughout this row.

This closes the irreducible one-place charged genus-four row before any
affine Fox or singular-link localization is needed.  It is independent of
the `m=0` assumption and therefore includes the requested `m=0` horn.  It
does not treat genus at least five, reducible branch curves, source forests,
nonminimal rank-four packets, higher-rank blocks, or JC2 itself.

## 1. Exact charged inputs and scope

The charged topology and one-place interfaces are:

```text
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa
  xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md

03b16c2deba48605482963ae7f98f5e74aca26ce0e1761bbeab653a164bec4b4
  xmodel/block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md

5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
```

They supply the already-reviewed statements

```text
g_3(K_infinity)=Delta_aff(B),
K_infinity is prime (or trivial) and iterated-cabled,
pi1(S3-K_infinity) ->> pi1(A2-B), preserving meridians,
b1(B)=sum_z (#nu^(-1)(z)-1),                          (1.1)
```

and the Assi--Garcia-Sanchez one-place delta-sequence, freeness, conductor,
and approximate-root interfaces.  The present artifact extends the same
fixed-genus calculation from conductor six to conductor eight.  It does not
assert that every abstract iterated knot is polynomially realizable.

The predecessor desk replay whose braid conventions are reused is

```text
838898b13769b073913caf5c18a72a51387bb6e338573efea5d4f6e206b1c5c8
  ops/block_descent_a1_genus_three_cable_b1_replay.py.
```

All sign and companion-chirality variants are retained in the finite group
enumeration.  A complex one-place branch has the positive algebraic
orientation; keeping the extra variants only strengthens the boundary
screen and does not manufacture additional semigroup rows.

## 2. Complete genus-four prime iterated-knot census

For a nontrivial cable of a knot `J`, Schubert's formula is

```text
g(C_(p,q)(J))=p*g(J)+(p-1)(|q|-1)/2,
p>=2, gcd(p,q)=1.                                      (2.1)
```

For the unknot companion, genus four gives

```text
(p-1)(|q|-1)=8.
```

After exchanging torus coordinates and imposing coprimality, this gives
exactly `T(2,9)` and `T(3,5)`.

Now let `J` be nontrivial.  Equation (2.1) gives `p*g(J)<=4`.

* If `g(J)=1`, then `J` is a trefoil or mirror.  The exact solutions are
  `(p,|q|)=(2,5),(3,2),(4,1)`.
* If `g(J)=2`, then `(p,|q|)=(2,1)`.  Applying (2.1) once more shows that
  the prime iterated genus-two companions are `T(2,5)` and
  `C_(2,1)(trefoil)`, with mirrors retained.
* A companion of genus at least three is impossible.

This proves the seven-row list (0.1), including the only possible
three-stage tower.

## 3. Complete conductor-eight delta-sequence census

For a delta-sequence `(r0,...,rh)`, put

```text
d1=r0,       d_(i+1)=gcd(r0,...,ri),       e_i=d_i/d_(i+1).
```

The conductor formula is

```text
mu=sum_(i=1)^h (e_i-1)r_i-r0+1.                       (3.1)
```

Here `mu=2g=8`, and the fixed-genus bound gives

```text
h<=floor(log_2(g+1))=2.                               (3.2)
```

For `h=1`, (3.1) becomes

```text
(r0-1)(r1-1)=8.
```

With `r0>r1` and coprimality, its exact solutions are

```text
(r0,r1)=(9,2),(5,3).                                  (3.3)
```

For `h=2`, write

```text
r0=a*d,       r1=b*d,
a>b>=2,       gcd(a,b)=1,       d>=2.                 (3.4)
```

Primitivity gives `gcd(d,r2)=1`.  Freeness at the last step is

```text
d*r2 in <r0,r1>,       equivalently r2 in <a,b>.      (3.5)
```

In particular `r2>=b>=2`.  Formula (3.1) is exactly

```text
7=d*((a-1)*b-a)+(d-1)*r2.                             (3.6)
```

Since `((a-1)*b-a)=(a-1)(b-1)-1>=1`, equations
(3.5)--(3.6) imply

```text
3*d-2<=7,       hence d<=3.                           (3.7)
```

If `d=2`, then `7=2*((a-1)*b-a)+r2`; the only solution is

```text
(a,b,r2)=(3,2,5),       (r0,r1,r2)=(6,4,5).           (3.8)
```

If `d=3`, then `7=3*((a-1)*b-a)+2*r2`; the only solution is

```text
(a,b,r2)=(3,2,2),       (r0,r1,r2)=(9,6,2).           (3.9)
```

This proves (0.2).  Under the standard Puiseux/cabling dictionary,
`(6,4,5)` and `(9,6,2)` are respectively the winding-two and winding-three
trefoil cables in (0.1).  The remaining topological rows would require
`(12,8,1)`, `(10,4,1)`, or a length-four characteristic sequence.  The
first two violate (3.5), since `1` is not in `<3,2>` or `<5,2>`; the last
violates (3.2).

## 4. Determinant, sign-Fox, and full-`S4` boundary screens

The exact finite enumeration gives the following table.  Fox counts include
the three constant colorings; full-`S4` counts are labelled and are not
quotiented by simultaneous conjugacy.

| one-place row | delta-sequence | determinant | Fox-3 count | full-`S4` count |
|---|---:|---:|---:|---:|
| `T(2,9)` | `(9,2)` | 9 | 9 | 0 |
| `T(3,5)` | `(5,3)` | 1 | 3 | 0 |
| `C_(2,5)(trefoil)` | `(6,4,5)` | 5 | 3 | 0 |
| `C_(3,2)(trefoil)` | `(9,6,2)` | 9 | 27 | 144 |

Every sign/chirality variant has the same entry in its row.  The cable
determinants also follow independently from

```text
Delta_C(p,q)(J)(t)=Delta_T(p,q)(t)*Delta_J(t^p).       (4.1)
```

Thus the last row has a two-dimensional reduced sign-Fox space and many
full-`S4` boundary colorings.  It is a genuine group-level survivor.  No
determinant or colorability claim is used to eliminate it below.

## 5. Full `(9,6,2)` approximate-root normal form

Let `C[U(t),V(t)]` be a rational polynomial one-place row with delta-sequence
`(9,6,2)`.  The coordinate degrees are

```text
deg U=6,       deg V=9.                               (5.1)
```

The last approximate root has parameter degree exactly two.  Its weighted
leading part is `V^2-U^3`.  The monomials below weighted degree eighteen are
`1,U,U^2,V,U*V`; completing the square in `V`, depressing the cubic in `U`,
and scaling therefore put the exact approximate root in Weierstrass form

```text
H(t)=V(t)^2-U(t)^3+A*U(t)+B,
deg_t H=2.                                             (5.2)
```

These are affine triangular target changes.  They preserve normalization
fibres and `b1`.

There is a unique monic cubic `Z` such that

```text
U=Z^2+R,       deg R<=2.                               (5.3)
```

Translate the parameter to depress `Z` and write

```text
Z=t^3+p*t+q,
R=a*t^2+b*t+c.                                        (5.4)
```

Divide

```text
R^2=Z*Q+S,       deg Q<=1,       deg S<=2.             (5.5)
```

The polynomial part at infinity of `U^(3/2)` is

```text
W=Z^3+(3/2)*Z*R+(3/8)*Q.                              (5.6)
```

Equation (5.2) forces `V=W`.  Indeed, direct expansion of (5.6) gives
`deg(W^2-U^3)<=8`; if nonzero `V-W` had degree `d>=0`, the term
`2*W*(V-W)` would have degree `9+d`, strictly above every term that can be
cancelled by `A*U+B`.

The same direct expansion gives the useful identity

```text
W^2-U^3
 =-(3/4)*Z^2*S+(9/8)*Z*R*Q-R^3+(9/64)*Q^2.            (5.7)
```

If `a=0` but `b!=0`, the degree-eight coefficient in (5.7) is
`-3*b^2/4`, which `A*U+B` cannot cancel.  If `a=b=0`, then `R=c` and
choosing `A,B` reduces (5.7) to zero, of parameter degree zero rather than
two.  Hence

```text
a!=0.                                                  (5.8)
```

Now polynomial division in (5.5) gives

```text
Q=a^2*t+2*a*b,
S=(b^2+2*a*c-a^2*p)*t^2
 +(2*b*c-a^2*q-2*a*b*p)*t
 +(c^2-2*a*b*q).                                      (5.9)
```

The degree-eight and degree-seven terms in (5.7) cannot be cancelled by
`A*U+B`, so `S` is constant.  Therefore

```text
a^2*p=b^2+2*a*c,
a^2*q=2*b*c-2*a*b*p.                                  (5.10)
```

After (5.10), (5.7) has degree at most six.  There is a unique `A` cancelling
its degree-six coefficient.  Exact coefficient comparison then gives

```text
[t^5](W^2-U^3+A*U)=3*a^2*b/8,
[t^4](W^2-U^3+A*U)=-a*(a*c-b^2)/8.                   (5.11)
```

Equation (5.2), characteristic zero, and (5.8) force first `b=0` and then
`c=0`.  Equations (5.10) give `p=q=0`.  Thus the complete normalized family
is

```text
U=t^6+a*t^2,
V=t^9+(3/2)*a*t^5+(3/8)*a^2*t,       a!=0,            (5.12)
V^2-U^3-(a^3/8)*U=(a^4/64)*t^2.                       (5.13)
```

Conversely (5.13) has exact parameter degree two, so it realizes the final
delta entry.  It is birational: (5.13) puts `t^2` in `C(U,V)`, while

```text
t=V/(t^8+(3/2)*a*t^4+(3/8)*a^2)                       (5.14)
```

in the function field.  Scaling the parameter and the two target coordinates
over `C` sends every `a!=0` to `a=8`, yielding (0.3)--(0.4).

## 6. Exact normalization-pair obstruction

For (0.3), equation (0.5) applies.  The quadratic

```text
q(w)=w^2+12*w+24                                      (6.1)
```

has discriminant `48` and constant term `24`.  It therefore has two
distinct nonzero roots `w1,w2`.  Each equation `t^4=wi` has four distinct
solutions.  The eight solutions are disjoint and are partitioned into four
disjoint unordered pairs `{t,-t}`.

For every such endpoint,

```text
U(t)=U(-t),       V(t)=V(-t)=0.                        (6.2)
```

Let the normalization fibres containing these eight endpoints have sizes
`k1,...,kr`.  Each of the four pairs is contained in one fibre, hence
`r<=4`, while `sum_i ki>=8`.  Formula (1.1) gives

```text
b1(B)>=sum_i(ki-1)>=8-4=4.                             (6.3)
```

This argument remains valid if several displayed pairs have the same image:
merging their fibres only increases the right side.  Since every reduced
plane-curve singularity satisfies `delta_z>=#nu^(-1)(z)-1`, the charged
identity `Delta_aff(B)=4` combines with (6.3) to give `b1(B)=4` exactly.
In particular the row cannot meet `b1(B)=1`.

## 7. Replay, mutations, and next computation

The desk-small exact replay is

```text
c79b7197d9c84e8a9a161cf153430849ad730b35d950a51afc32d1cd73ffa707
  ops/block_descent_a1_genus_four_cable_b1_replay.py.
```

It uses only the Python standard library.  Ordinary, `python3 -O`, and
`python3 -OO` executions have byte-identical stdout with SHA-256

```text
1fbb987b3b3a12aef716f5526fea3f539d02843797ded68e4d70eeea66c8438c.
```

The replay checks the exhaustive conductor-eight arithmetic, all standard
braid sign/chirality rows, determinant and Fox-3 controls, exact coefficient
identities on an interpolation grid large enough for their proved bidegree
bounds, the lower-degree `R` cases, the integer-scaled approximate-root
identity, and the four-pair lower bound.  Each mutation

```text
--mutate-drop-freeness
--mutate-allow-c32-b1-one
--mutate-promote-zero-s4
```

exits nonzero at its intended gate.  No CAS, numerical root finder, or heavy
local computation was used.

There is no honest genus-four affine Fox/local-link client left in the
charged `b1=1` horn: the only boundary survivor fails before localization.
The smallest direct successor is therefore the conductor-ten/genus-five
delta-sequence and cable census.  For each full-`S4` survivor, the correct
order is (i) approximate-root normal form, (ii) normalization-pair count,
and only then (iii) affine sign-Fox plus local singular-link kernel.  A
symbolic normal-form elimination that grows beyond this triangular desk
calculation should be compiled as a bounded exact AWS job; no broad local
Groebner search is licensed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13673`.
- Body SHA-256:
  `12695be8e804252aa9c06b737a428e861af15ff59dc657fa1e5dd5b2c626de66`.
- Frozen basis: `b2c7358a8a42f6841a289539dfbb5df290b73f4d`.
