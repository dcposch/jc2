# Nonnormal quadratic incidences reduce to one moving-double-section normal form

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra delegated lane `/root/whole_portfolio_ideation`  
Frozen basis: `145f96d65021ef364a5189c4ca385fe09d7b4f46`  
Lifecycle: **EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint and epistemic scope

Let `A=C[u,v]` and let

```text
B=A*1 direct-sum A*z direct-sum A*w
```

be the normal finite-flat integral cubic algebra of a hypothetical proper
cubic block of a noninvertible plane Keller map.  Charge the promoted proper
block sandwich, the binding nonmonogenicity theorem, and the dominant first
leg

```text
g:A2 -> Y=Spec(B).
```

Suppose that in one global trace-zero basis the Miranda coefficients
`a,b,c,d` have total degree at most two and at least one has degree two.  Let

```text
Phi=bX^3-3aX^2Y+3dXY^2-cY^3,
X_aff=V(Phi) subset A2 times P1,
Xbar=V(Phi^h) subset P2 times P1,       [Xbar]=2A+3B,
H=Xbar intersect (L_infinity times P1).
```

Then the following is the maximum exact conclusion of this packet.

> **NONNORMAL-Q2-DICHOTOMY.**  The affine incidence `X_aff` is normal.  If
> the projective quadratic incidence `Xbar` is nonnormal, then, after
> constant linear coordinate changes on `L_infinity` and the fibre, its
> unique generic nonnormal boundary type is
>
> ```text
> H=2C+L,             [C]=(1,1),        [L]=(0,1),      (0.1)
> ```
>
> and its homogenized binary cubic has the exact form
>
> ```text
> Phi^h=Q^2 L + T Q S + T^2 R,                         (0.2)
> ```
>
> where `T=0` is target infinity, `Q` is an irreducible bilinear form of
> bidegree `(1,1)`, and `L,S,R` are constant binary forms of fibre degrees
> `1,2,3`.  The target discriminant of `B/A` consequently has total degree
> at most six.

Thus all affine exceptional-curve nonnormality, all repeated constant
sections at infinity, and all repeated vertical infinity fibres are
excluded.  Only the moving double section (0.1) remains in the nonnormal
quadratic frontier.

This is a theorem about the normal cubic algebra plus a chosen quadratic
compactification.  It is not a polynomial-map construction and does not
close the normal-singular quadratic lane.  It also does not say that every
degree-minimal basis has the same infinity divisor.

The exact promoted clients used here are

```text
c8dee3199ecfaf73b6debedea625346a11babbe42082cff5bff049f8585763c2
  xmodel/bd-fix3-affine-linear-log-closure-coordinator-integration-sol56-20260830.md
410de2f569e2ad5599152fdd9414198f012dbdced7d17c5a51dde0096fe4601e
  xmodel/bd-fix3-quadratic-discriminant-conductor-coordinator-integration-sol56-20260830.md
ac7ef8f5321f579d5e193b6ae3a9b0f1aa2a64421050bb71426b94258d984ffb
  xmodel/bd-a2-smooth-quadratic-degeneracy-absorption-sol56-20260830.md
```

The smooth absorption packet supplies the finite common-zero and affine
Stein bridges.  Its smooth exclusion is not charged in the proof below.

## 1. The intrinsic content ideal and what a basis can change

In a trace-zero basis the multiplication table is

```text
z^2 = 2(a^2-bd) + a*z + b*w,
z*w = -(ad-bc) - d*z - a*w,
w^2 = 2(d^2-ac) + c*z + d*w.                         (1.1)
```

Define the coefficient-content ideal

```text
I_B=(a,b,c,d) subset A.                               (1.2)
```

This ideal is intrinsic to `B/A`.  Indeed, a change of global trace-zero
basis is an element of `GL_2(A)`.  The associated binary cubic transforms
through the rank-four binary-cubic representation, with only a determinant
twist.  Both the matrix of that representation and its inverse have entries
in `A`, because the determinant of the basis change is a unit of `A`, hence
a nonzero complex constant.  Therefore the old and new coefficient vectors
generate the same ideal.

Consequently the following data are basis invariant:

```text
I_B and every local order ord_q(I_B);
the trace discriminant Delta, up to C^*;
the branch divisor V(Delta);
the minimum coefficient degree d_min over trace-zero bases.
```

By contrast, the leading homogeneous cubic, the factorization and
multiplicities of `H`, projective coefficient basepoints, the first normal
jet at infinity, and normality of this particular projective closure can
change under a polynomial `GL_2(A)` basis change.  Such a change is an
automorphism of the affine `P^1`-bundle but need not extend regularly over
target infinity.  These boundary features are presentation data, not
invariants of the cubic algebra.

The intrinsic ideal gives the elementary lower bound

```text
d_min >= max_q ord_q(I_B).                            (1.3)
```

Indeed a nonzero polynomial of degree at most `e` cannot vanish to order
greater than `e` at an affine point.  In the hypothetical block scope,
existence of the displayed quadratic basis and the binding theorem
`AL3-CLOSED` already give the exact value `d_min=2`: a basis of degree at
most one is impossible.  This basis-minimality statement does **not** give a
coverage theorem for smooth or normal compactifications.

Normality also forbids a height-one component of `V(I_B)`: at its generic
DVR the special fibre of (1.1) would be `kappa direct-sum V`, `V^2=0`,
which is incompatible with a rank-three normal order.  Hence

```text
Z=V(I_B) subset A2
```

is finite.

## 2. Exact affine `R_1` test

The generic binary cubic is irreducible because `Frac(B)` is a cubic field.
Thus `X_aff` is an integral hypersurface and is Cohen--Macaulay, hence
`S_2`.  The direct-image/Stein bridge identifies `X_aff` with `Y=Spec(B)`
away from `Z`; over `q in Z`, the incidence has the exceptional fibre

```text
E_q={q} times P1.
```

Translate `q` to the origin and write the first Taylor part of `Phi` as

```text
Phi=s*p(X,Y)+t*r(X,Y)+terms of base order at least two.
```

Along `E_q`, all fibre derivatives vanish and the two remaining gradient
entries are `p` and `r`.  Therefore the singular locus contains the whole
curve `E_q` if and only if `p=r=0`, equivalently

```text
I_B subset m_q^2.                                    (2.1)
```

If (2.1) fails, the singular points on `E_q` are only the finite common-zero
scheme of the two binary cubics `p,r`; the generic point of `E_q` is regular.
As `Y` is normal off these exceptional fibres, Serre's criterion gives

```text
X_aff is normal iff I_B is not-subset m_q^2 for every q in Z.   (2.2)
```

This separates two often conflated statements.  The exceptional `P^1` is a
feature of the incidence model and is contracted by the Stein map.  The
condition that makes it a divisorial singular locus is nevertheless the
intrinsic first-order content condition (2.1).

## 3. The quadratic content cone is impossible

Assume (2.1) in a quadratic basis.  Since every coefficient has degree at
most two, after translating `q` all four are homogeneous quadratics.  Give

```text
deg(s)=deg(t)=1,             deg(z)=deg(w)=2.
```

Every equality in (1.1) is homogeneous of degree four.  Thus `B` is a
connected positively graded normal domain with graded `C[s,t]`-module

```text
B=C[s,t] direct-sum C[s,t](-2)z direct-sum C[s,t](-2)w.          (3.1)
```

Put `C0=Proj(B)`.  Because `B` is finite over the standard graded ring
`C[s,t]`, `C0->P1` is finite of degree three and `O_C0(1)` is the pullback
of `O_P1(1)`.  Normality of the graded domain makes `C0` a normal integral
projective curve, hence a smooth curve.  From (3.1), for `n>=2`,

```text
dim_C B_n=(n+1)+2(n-1)=3n-1.
```

Its Hilbert polynomial is also

```text
deg(O_C0(1))*n+1-g(C0)=3n+1-g(C0),
```

so

```text
g(C0)=2.                                               (3.2)
```

Choose a nonzero degree-one element `s`.  The degree-zero homogeneous
fraction field is `C(C0)`, and every homogeneous `b_n` satisfies

```text
b_n=(b_n/s^n)*s^n.
```

It follows that

```text
Frac(B)=C(C0)(s).                                     (3.3)
```

The dominant first leg `A2->Y` is generically finite.  After completing and
resolving indeterminacy, (3.3) would give a dominant map from a rational
surface to the genus-two curve `C0`.  Such a map is impossible: every
morphism from a smooth rational surface to a positive-genus curve is
constant (equivalently use the Albanese/Jacobian).  This contradicts
dominance.

Hence (2.1) never occurs in the proper-block scope.  Equation (2.2) now
proves that `X_aff` is normal.  Notice that the contradiction used exact
algebra and a dominant map.  The Hilbert series alone is formal algebraic
data; interpreting it as a plane Keller map would have been invalid without
the first-leg bridge.

As a consistency check only, in this killed stratum the intrinsic target
discriminant is a nonzero homogeneous octic about `q`, so `DISC8-INDEX`
also certifies `d_min=2`.  This discriminant statement is not the source
ramification divisor and is not a normalization-index or conductor claim.

## 4. Projective `R_1` test and the finite repeated-type list

Write

```text
Phi^h=Phi_2(U,V;X,Y)+T*Phi_1(U,V;X,Y)+T^2*Phi_0(X,Y), (4.1)
```

where `Phi_i` has base degree `i` and fibre degree three.  Since `X_aff` is
normal, a divisorial nonnormal locus of `Xbar` lies in `H={Phi_2=0}`.  The
homogenized cubic is primitive: a projective common coefficient divisor
other than `T=0` would give a forbidden affine height-one component of
`V(I_B)`, while divisibility by `T` would contradict exact coefficient
degree two.  Generic irreducibility and Gauss's lemma therefore make `Xbar`
an integral hypersurface, hence `S_2`; its nonnormality is exactly an `R_1`
failure.

At the generic point of a reduced component of `H`, a tangent derivative
inside `L_infinity times P1` is nonzero, so `Xbar` is regular there.  If an
integral component `C` occurs with multiplicity at least two, all tangent
derivatives vanish along it; `Xbar` is singular generically along `C` if
and only if the first normal jet also vanishes:

```text
Phi_1|C=0.                                             (4.2)
```

Because an integral component of bidegree `(alpha,beta)` repeated `m>=2`
must satisfy `m*alpha<=2` and `m*beta<=3`, the complete list of maximal
repeated patterns in class `(2,3)` is

```text
2(0,1)+(2,1),
3(0,1)+(2,0),
2(1,0)+(0,3),
2(1,1)+(0,1).                                         (4.3)
```

Here the second bidegree is the degree over `L_infinity`; `(1,0)` is a
vertical fibre and `(a,1)` is a section.  Conditions (4.2)--(4.3) are an
exact `R_1` threat map, not merely a list of possible nonreduced divisors.

## 5. Constant repeated sections are impossible

Let the repeated component have class `(0,1)`.  It is the constant section
with fibre value `q0=[r:s]`.  Repetition gives

```text
Phi_2(r,s)=0,
```

and the nonnormality condition (4.2) gives `Phi_1(r,s)=0`.  Therefore

```text
Phi(r,s)=Phi_0(r,s) in C.                             (5.1)
```

If this scalar is nonzero, the determinant criterion

```text
det(t,t^2)=Phi(r,s),          t=r*z+s*w,
```

makes `B/A` monogenic, contradicting the binding proper-block theorem.  If
the scalar is zero, the generic binary cubic has the fixed root `[r:s]` and
is reducible over `C(u,v)`, contradicting that `Frac(B)` is a field.  This
eliminates both constant-section rows in (4.3).

## 6. A repeated vertical fibre is impossible

Let `C` have class `(1,0)`, defined on `L_infinity` by a linear form
`ell(U,V)`.  Repetition and the total base degree two force

```text
Phi_2=ell^2*P(X,Y).
```

Condition (4.2), and the fact that `Phi_1` has base degree one, force

```text
Phi_1=ell*Q(X,Y).
```

Choose a complementary affine target coordinate `r` and put
`p=ell(u,v)`.  Then

```text
Phi=p^2 P+p Q+R
```

is independent of `r`.  Its multiplication table descends to a finite free
rank-three `C[p]`-algebra `D`, and

```text
B=D[r].                                                (6.1)
```

Since `B` is a normal domain, so is `D`.  Let `C1=Spec(D)` and let
`Cbar1` be its smooth projective completion.  The field identity

```text
Frac(B)=C(Cbar1)(r)
```

and the dominant first leg imply `g(Cbar1)=0`, by the same rational-surface
argument as in Section 3.  Dominance also injects units

```text
B^* -> C[x,y]^*=C^*,
```

so `D^*=C^*`.

Because `D` is normal and finite over `C[p]`, it is the integral closure of
`C[p]` in its fraction field; `C1` is `Cbar1` with precisely the points over
`p=infinity` removed.  On `Cbar1=P1`, removal of two or more points produces
a nonconstant unit.  Thus exactly one point is removed, and

```text
D=C[t],             p=P(t) with deg(P)=3.
```

Equation (6.1) becomes

```text
B=C[p,r][t],
```

so `B/A` is monogenic, again contradicting the binding proper-block theorem.
This eliminates the vertical row of (4.3).

## 7. The sole survivor and its discriminant drop

Only `2(1,1)+(0,1)` remains.  An integral `(1,1)` component is cut out by
an irreducible bilinear form `Q`.  Unique factorization on
`P1 times P1`, (4.1), and (4.2) give

```text
Phi_2=Q^2 L,          Phi_1=Q S,          Phi_0=R,
```

with the bidegrees stated in (0.2).  This proves the asserted normal form.

It also forces two top discriminant cancellations.  Scale a generic affine
target direction by `(u,v)->(lambda*u,lambda*v)`.  Over `C(u:v)`, use `Q`
and `L` as fibre coordinates `x,y`.  The cubic is

```text
lambda^2*x^2*y
 +lambda*x*(s0*y^2+s1*x*y+s2*x^2)
 +(r0*y^3+r1*x*y^2+r2*x^2*y+r3*x^3).                 (7.1)
```

On `y=1`, its coefficients from constant through cubic degree have
`lambda`-degrees at most

```text
0, 1, 2, 1.
```

Every term in the cubic discriminant

```text
c1^2*c2^2 -4*c0*c2^3 -4*c1^3*c3
 -27*c0^2*c3^2 +18*c0*c1*c2*c3
```

therefore has `lambda`-degree at most six.  A generic fibre-coordinate
change multiplies the discriminant only by a nonzero factor independent of
`lambda`.  Hence the intrinsic full affine target discriminant satisfies

```text
deg(Delta)<=6.                                         (7.2)
```

The degree-eight leading discriminant and its degree-seven first variation
both vanish.  This is a target-discriminant statement only.  It does not
make the cubic Galois, identify source ramification, or compute a different,
normalization index, or conductor.

`DISC8-INDEX` remains one-way: (7.2) does not imply that an affine-linear
basis exists.  In fact `AL3-CLOSED` forbids such a basis in the hypothetical
proper-block scope, so the given quadratic basis is still degree-minimal.

## 8. Coverage boundary and actionable successor

The exact disposition is

```text
affine exceptional divisorial nonnormality: killed by genus-two content cone;
constant repeated infinity section:          killed by unit/fixed-root split;
repeated vertical infinity fibre:            killed by ruled curve + units;
moving repeated (1,1) section:                survives in form (0.2);
normal singular quadratic incidence:         outside this packet;
change to a good quadratic basis:             no coverage theorem yet.
```

The clean successor is now local and finite rather than a search over all
nonnormal hypersurfaces: normalize (0.2) along the double curve
`C={T=Q=0}` and compute its conductor boundary.  Blowing up the ideal
`(T,Q)` formally replaces `Q=T*W` by

```text
W^2 L+W S+R=0.                                        (8.1)
```

On `C isomorphic to P1`, the prospective conductor cover has quadratic
discriminant

```text
(S|_C)^2-4*(L|_C)*(R|_C),
```

a binary quartic.  Generically its connected double cover has genus one,
which would conflict with the promoted rational-boundary forest.  The next
packet should prove the normalization/blowup bridge, separate split,
two-branch, and square quartics, and feed the resulting attachments into
the forest theorem.  The genus-one observation is a **rigorous calculation
of the candidate local model but only a successor heuristic** until that
bridge and the identification with the resolved map boundary are proved.

A parallel basis-coverage successor should classify degree-two
`GL_2(C[u,v])` orbit moves that preserve the coefficient cap and ask whether
one can leave (0.2) for a smooth or normal-singular compactification.  It
must retain the distinction between intrinsic `I_B,Delta,d_min` and the
presentation-dependent infinity divisor.  A small symbolic factor-stratum
calculation can discriminate cases, but finite-prefix or sampled data would
not prove orbit coverage.

No finite-prefix evidence, formal arc data, heavy CAS output, map-level
construction, counterexample, or JC2 conclusion is claimed in this report.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16427`.
- Body SHA-256:
  `36bb8913697d3ce1bd725beed0e2089b444db425ab038f77530b2020c738d34a`.
- Frozen basis: `145f96d65021ef364a5189c4ca385fe09d7b4f46`.
