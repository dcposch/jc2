# Binding integration: nonnormal quadratic content-cone dichotomy

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen integration basis: `f6be19af096646b15a309841938d29c192a7c902`  
Lifecycle: **PROMOTED REDUCTION; ONE NONNORMAL BOUNDARY FORM REMAINS**

## 0. Verdict, custody, and maximum theorem

This integration binds the transactional producer

```text
6b324824e0c075b938bd5b7015d4e8d134bad7cb845ac7597212b61d91dfa7a5
  xmodel/bd-a2-nonnormal-quadratic-content-cone-dichotomy-sol56-20260830.md
  body 16427 / 36bb8913697d3ce1bd725beed0e2089b444db425ab038f77530b2020c738d34a
  manifest 95487ead150d2ffba5aedba64974340aaf7695df806355398e0588356140a2cb
```

to the independent GPT-5.5 xhigh hostile review

```text
3b8ba81b06506a76374c434ae8ff0ad44ded84441aa932f2d825a4737b4ab944
  xmodel/bd-a2-nonnormal-quadratic-content-cone-dichotomy-hostile-review-gpt55-20260830.md
  body 13335 / b541732a6ea433de59e91a22a85d19913145bdbc620c5001cf701ac006c73df4
  verdict CONFIRM_WITH_CORRECTIONS
```

The producer was authored and transactionally sealed on dependency basis
`145f96d65021ef364a5189c4ca385fe09d7b4f46`, first committed at
`dca72076aa1615b0b1286fd4428a1acac7b65963`, and reviewed on exactly that
commit.  Its review receipt was root-sealed and committed at the present
integration basis.  The producer described the earlier smooth-degeneracy
packet as promoted before its own later review/integration.  That lifecycle
wording is corrected here: this integration charges the now-reviewed binding
smooth-frontier integration

```text
1b30c798114e7d9d96ac2a882a4ebe6ec670880289be107eba3ddf7053125e9f
  xmodel/bd-a2-smooth-quadratic-frontier-coordinator-integration-sol56-20260830.md
```

for the finite common-zero and affine Stein facts.  It also charges the
promoted proper-block/nonmonogenic structure `ba69b33f...` and `f9720718...`,
the affine-linear closure `c8dee319...`, and the intrinsic discriminant theorem
`410de2f5...`.  No provisional statement is silently upgraded.

Let `B` be the normal finite-flat integral cubic algebra of a proper cubic
intermediate block of a hypothetical noninvertible plane Keller map, with its
promoted dominant first leg and nonmonogenic obstruction.  Suppose a chosen
global trace-zero Miranda basis has coefficient maximum exactly two.  Let
`X_aff` be its affine binary-cubic incidence and `Xbar` its class-`2A+3B`
projective homogenization.  Then:

```text
X_aff is normal;
if Xbar is nonnormal, every generic divisorial nonnormal component is at infinity;
the only surviving repeated infinity type is H=2C+L,
  with C irreducible of bidegree (1,1) and L of bidegree (0,1);
equivalently Phi^h=Q^2 L+T Q S+T^2 R;
the intrinsic affine target discriminant then has total degree at most six.
```

The normal form remains a live nonnormal stratum.  Its blowup, normalization,
conductor, and proposed quartic/genus obstruction are not promoted here.

## 1. Intrinsic content and the affine `R_1` criterion

In a trace-zero basis the Miranda table is

```text
z^2 = 2(a^2-bd)+a z+b w,
z w = -(ad-bc)-d z-a w,
w^2 = 2(d^2-ac)+c z+d w.
```

Define the content ideal `I_B=(a,b,c,d)`.  A global trace-zero basis change
lies in `GL_2(C[u,v])`, whose determinant is a nonzero constant.  The binary-
cubic representation and its inverse therefore have polynomial entries, so
the old and new four coefficients generate the same ideal.  Thus `I_B`, its
local orders, the discriminant ideal/divisor, and the minimum coefficient
degree among trace-zero bases of this fixed algebra are intrinsic.  The
leading cubic, infinity factorization, projective basepoints, first normal
jet, and normality of a particular projective closure are not.

Normality excludes a height-one component of `V(I_B)`: at its generic DVR the
Miranda table would specialize to `kappa direct-sum V`, `dim V=2`, `V^2=0`.
A one-prime normal cubic order has either a cubic residue-field fibre or a
totally ramified length-three fibre whose radical has nonzero square.  A
multi-prime fibre is not local.  Hence `Z=V(I_B)` is finite.

The exact Stein bridge follows by pushing forward

```text
0 -> O(-3) --Phi--> O -> O_Xaff -> 0.
```

It gives a locally free rank-three algebra.  Off `Z`, the incidence is finite
and Miranda identifies that algebra with `B`; both sides are reflexive over
the regular affine plane, so the algebra isomorphism extends uniquely across
`Z`.  Thus `X_aff->Spec(B)` is an isomorphism off `Z` and has exceptional
fibre `E_q={q} times P1` at `q in Z`.

At such a point write the first base jet

```text
Phi=s p(X,Y)+t r(X,Y)+O((s,t)^2).
```

Along `E_q`, the fibre derivatives vanish and the two base derivatives are
`p,r`.  The generic point of the exceptional curve is singular exactly when
both binary cubics vanish identically, equivalently

```text
I_B subset m_q^2.
```

Otherwise its singular points form only a finite scheme.  The integral
hypersurface is Cohen--Macaulay, hence `S_2`, and away from exceptional curves
it is isomorphic to normal `Spec(B)`.  Serre's criterion therefore gives

```text
X_aff is normal iff I_B is not contained in m_q^2 for every q in Z.
```

No other affine codimension-one nonnormal locus is omitted.

## 2. The quadratic content cone is impossible

Assume `I_B subset m_q^2`.  Translate `q` to the origin.  Since all
coefficients have degree at most two, all four are homogeneous quadratics.
Giving `s,t` degree one and `z,w` degree two makes `B` a connected normal
graded domain with

```text
B=C[s,t] direct-sum C[s,t](-2)z direct-sum C[s,t](-2)w.
```

The curve `C_0=Proj(B)` is normal, integral, and finite of degree three over
`P1`, hence smooth.  For `n>=2`,

```text
dim B_n=(n+1)+2(n-1)=3n-1.
```

Since `O_C0(1)` has degree three, Riemann--Roch gives `g(C_0)=2`.  For a
nonzero degree-one element `s`, homogeneous fractions give

```text
Frac(B)=C(C_0)(s).
```

The promoted first leg embeds this field in `C(x,y)`, so `C(C_0)` embeds in
the rational surface function field.  This produces a dominant rational map
from `P2` to the genus-two curve; after resolving indeterminacy it would be a
nonconstant morphism from a smooth rational surface to a positive-genus curve,
which is impossible.  This is a function-field/rational-map contradiction,
not an assertion that an affine map to a cone automatically extends to Proj.

The content-cone case is therefore empty, and the affine `R_1` criterion proves
that every quadratic incidence in this proper-block scope has normal affine
part.

## 3. Complete projective repeated-component threat list

Write

```text
Phi^h=Phi_2(U,V;X,Y)+T Phi_1(U,V;X,Y)+T^2 Phi_0(X,Y).
```

Exact coefficient degree two and absence of an affine height-one content
factor make this homogenized binary cubic primitive.  Generic irreducibility
and Gauss make `Xbar` integral, hence `S_2`.  Since its affine part is normal,
every divisorial `R_1` failure lies in infinity `H={Phi_2=0}`.

At a reduced generic component of `H`, some tangent derivative is nonzero.  If
an integral component `C` is repeated, all tangent derivatives vanish and the
normal derivative is `Phi_1|C`; generic nonnormality is exactly the condition
that this restriction vanish.  The possible repeated integral components and
their residual classes are exactly

```text
2(0,1)+(2,1),
3(0,1)+(2,0),
2(1,0)+(0,3),
2(1,1)+(0,1).
```

This is not claimed to list every further decomposition of the residual
divisor.  The eliminations below are componentwise, so additional residual
splitting creates no escape.  In this convention `(1,0)` is a vertical fibre
over a point of `L_infinity`, while an integral `(a,1)` component is a section.

## 4. Constant and vertical repeated components are impossible

For a repeated constant section with fibre value `[r:s]`, repetition and the
vanishing normal jet give

```text
Phi(r,s)=Phi_0(r,s) in C.
```

For `t=r z+s w`, the trace-zero part of `t^2` satisfies

```text
det((r,s),t^2_E)=Phi(r,s).
```

If the scalar is nonzero, `1,t,t^2` is a global basis and `B` is monogenic,
contrary to the promoted proper-block theorem.  If it is zero, the generic
binary cubic has a fixed rational root and cannot define a cubic field.  This
eliminates both constant-section multiplicities.

For a repeated vertical fibre cut by a base linear form `ell`, repetition and
the normal-jet condition force

```text
Phi_2=ell^2 P,       Phi_1=ell Q.
```

Choose affine target coordinates `p=ell(u,v)` and a complementary `r`.  All
coefficients lie in `C[p]`; the multiplication table descends to a normal
finite free cubic domain `D` over `C[p]`, and

```text
B=D[r].
```

Normality descends because `D[r] cap Frac(D)=D`.  The field identity and the
first-leg inclusion force the smooth completion of `Spec(D)` to have genus
zero.  The promoted structure gives the actual algebra inclusion
`B subset C[x,y]`, so `B^*=C^*` and `D^*=C^*`; dominance alone is not used as
a substitute for this unit statement.  Since `D` is the integral closure of
`C[p]`, its spectrum is `P1` with the points over infinity removed.  Removing
at least two complex points creates a nonconstant unit, so exactly one is
removed.  Hence `D=C[t]`, the degree-three map has `p=P(t)`, and
`B=C[p,r][t]` is monogenic.  The vertical case is impossible.

## 5. Sole nonnormal form and exact discriminant drop

Only a double irreducible `(1,1)` component remains.  Unique factorization and
the vanished normal jet give

```text
H=2C+L,
Phi^h=Q^2 L+T Q S+T^2 R,
```

where `Q` is irreducible of bidegree `(1,1)` and `L,S,R` are base-constant
binary forms of fibre degrees one, two, and three.

To compute the intrinsic target discriminant, restrict to a generic radial
line `(u,v)=lambda(u_0,v_0)` and work over the direction field.  The fibre
linear forms `Q_(u_0,v_0)` and `L` are generically independent, so use
`x=Q_(u_0,v_0)`, `y=L` as fibre coordinates.  Its determinant depends on the
direction but not on `lambda`; the sixth-power discriminant factor therefore
cannot change radial degree.  In the chart `y=1`, the coefficients from
constant through cubic degree in `x` have lambda-degrees

```text
0, 1, 2, 1.
```

Every term in the cubic discriminant has lambda-degree at most six.  Hence the
homogeneous target-discriminant pieces of degrees above six vanish on a generic
direction and are identically zero:

```text
deg Delta <= 6.
```

A denominator or determinant depending only on direction cannot create a
higher power of `lambda`.  This is the intrinsic affine target discriminant,
not source ramification, different, conductor, or normalization index.  The
one-way discriminant inequality does not create an affine-linear basis;
`AL3-CLOSED` already excludes one, so the displayed quadratic basis remains
degree-minimal in the hypothetical proper-block scope.

## 6. Exact successor and firewall

The remaining nonnormal client is local and finite.  It must normalize the
single form above along `C={T=Q=0}`.  Blowing up `(T,Q)` formally gives the
strict-transform equation

```text
W^2 L+W S+R=0
```

over `C`, with candidate double-cover discriminant
`S_C^2-4L_C R_C`, a section of degree four on `C~=P1`.  A successor must prove
when this blowup is the finite normalization, compute the actual conductor,
separate connected, split, square, and degenerate quartics, and identify the
preimage as a component of the resolved first-leg boundary before invoking
the rational-forest theorem.  The generic genus-one calculation is only a
successor heuristic here.

This integration does not close the surviving form, prove a conductor or
genus-one obstruction, classify quadratic basis changes, or prove that every
cubic block has a quadratic basis.  Normal singular incidences are governed
by the separate promoted `D9` reduction.  Higher coefficient or block degree,
primitive extensions, polynomial maps, counterexamples, and JC2 remain
outside.  No heavy CAS or AWS computation is charged; any future heavy or
uncertain computation remains AWS-only after a reviewed source packet.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11990`.
- Body SHA-256:
  `f3f2ecff368a7d60f93ce8bc09e992acaa2cca3fadd0702da3148b7e2b683b59`.
- Frozen basis: `f6be19af096646b15a309841938d29c192a7c902`.
