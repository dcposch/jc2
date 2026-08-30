# Binding integration: smooth quadratic frontier and one-attachment discriminant

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen integration basis: `ce162f50f6068b48527434b8aac1dbf1875bc552`  
Lifecycle: **PROMOTED, EXACT IN THE DECLARED STRATA**

## 0. Verdict, custody, and lifecycle

This integration binds two exact producers to two independent GPT-5.5 xhigh
hostile reviews.  The smooth-degeneracy pair is

```text
ac7ef8f5321f579d5e193b6ae3a9b0f1aa2a64421050bb71426b94258d984ffb
  xmodel/bd-a2-smooth-quadratic-degeneracy-absorption-sol56-20260830.md
  body 19665 / ecff0c0f3b373e00128b10cad561a0738e8db32e60d4c04f475c5e0fa38c25bd
  manifest 1a79d1b59737c1ead02cdc2e099d945ce91f19d2a84ceef4858c450af55f3106
ce494caffa72873ab3003596deafe2cbe698114f28fd5e478f81394b22a0b653
  xmodel/bd-a2-smooth-quadratic-degeneracy-absorption-hostile-review-gpt55-20260830.md
  body 14623 / 7d1a36e66a3d71833ace8eb28f7a4e92030b03fad91d226986e6394e0ba50d24
  verdict CONFIRM_WITH_CORRECTIONS
```

The one-attachment/discriminant pair is

```text
1ddb14b3dcc883e24690825a48a09bef47784c201fee67dec7d222732dc7b0d6
  xmodel/bd-a2-one-attachment-disc-max-producer-sol56-20260830.md
  body 16533 / ba0862b9c08538cfe35499c4d0cfe1c50b2dcf98f930c05c0c882e7552adfc0f
  manifest 9d085bf69e7b7c056ee454949bd32c67eabf21b26760727857180bbf7fbeac48
34b7c50638509e50c308766db4d21051824740c64afb1188bff88b248d27f1a3
  xmodel/bd-a2-one-attachment-disc-max-hostile-review-gpt55-20260830.md
  body 12518 / 0ea337dc8a618d09fc596dce77b00f175e38a367d36be97c6589e863d4373abd
  verdict CONFIRM_WITH_CORRECTIONS
```

Both producers were derived and transactionally sealed against the frozen
dependency basis `5bc4eea1c749045d54b4ee8053be8d85c4f3bc9f`.  They were first
committed at `73a200972954df9799da77bb25a7b76a591e5ec9` and
`145f96d65021ef364a5189c4ca385fe09d7b4f46`, respectively.  Both reviews ran
on exactly `145f96d65021ef364a5189c4ca385fe09d7b4f46`.  The older frozen-basis
fields are authorship/dependency snapshots, not claims that the final files
existed at that commit.  The review receipts were root-sealed and committed at
the present integration basis.  Both reviews independently reconstructed the
new mathematics and found no mathematical gap.  Their wording, graph, and
quantifier corrections are binding below.

The smooth closure charges the promoted integrations

```text
c9871c92ce8748fd934dc57061f667b49952a1aba39aee43eb3af7b0aadbf392
  quadratic ramification/lattice closure, including the first-leg forest/unit package;
c8dee3199ecfaf73b6debedea625346a11babbe42082cff5bff049f8585763c2
  affine-linear cubic-block closure;
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  proper cubic block structure;
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  non-Galois quotient obstruction.
```

The structural discriminant theorem additionally charges
`6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08`
for the rational-forest package and
`410de2f569e2ad5599152fdd9414198f012dbdced7d17c5a51dde0096fe4601e`
for the intrinsic cubic discriminant and normalization-index identities.

## 1. Promoted smooth degree-at-most-two closure

Assume the promoted proper cubic intermediate-block sandwich of a hypothetical
noninvertible plane Keller map.  Thus the normal finite-flat integral cubic
algebra `B_K` over `C[u,v]` and its dominant first leg satisfy the exact
rational-forest, non-etale avoidance, unit, and localization hypotheses
consumed by `c9871c92...`.  Choose a global trace-zero Miranda basis, with
four coefficient polynomials `a,b,c,d`.

Then the following fixed-presentation statement is promoted:

```text
max(deg a,deg b,deg c,deg d) <= 1
    is impossible by AL3-CLOSED;

max(deg a,deg b,deg c,deg d) = 2 and the associated exact-degree-two
projective incidence X subset P2 times P1 is smooth
    is impossible by Sections 2--5 below.
```

Equivalently, no proper cubic intermediate block in the promoted Keller
first-leg setting admits a chosen global trace-zero basis whose coefficients
have maximum degree at most two and whose associated incidence is in the
corresponding smooth stratum.  The exact-degree-two assertion concerns the
same basis before homogenization.  An affine-linear presentation is routed to
`AL3-CLOSED`; it is not rebranded as a smooth quadratic presentation.

This is existential in the fixed presentation: the existence of even one
basis satisfying the displayed conditions gives the contradiction.  It does
not assert that a quadratic basis exists, that smoothness is basis-invariant,
or that every basis of a cubic block has low degree.

## 2. Smooth infinity is automatically reduced

For an exact quadratic incidence

```text
X={Phi^h=0} subset P2 times P1,       [X]=2A+3B,
H=X intersect (L_infinity times P1),  [H]=(2,3),
```

suppose an integral component `C` of bidegree `(alpha,beta)` occurred in `H`
with multiplicity at least two.  All derivatives tangent to the infinity
surface vanish along `C`.  The normal jet is a section of

```text
O_C(A+3B),             deg=beta+3alpha>0.
```

If it vanishes identically, `X` is generically singular along `C`; if not,
its pullback to the normalization of the complete curve has a zero, where all
ambient first derivatives vanish.  Both contradict smoothness.  Thus `H` is
reduced and squarefree.  Vertical, horizontal, and singular components are
included because every nonzero component has `beta+3alpha>0`.

The reviewed intersection check agrees: on the smooth incidence surface,
adjunction gives

```text
C_i^2=2 alpha_i beta_i-3 alpha_i-beta_i,
(m_i-1)(3 alpha_i+beta_i)=0.
```

At intersections of distinct components, smoothness makes the normal
derivative a unit, so the ambient-surface intersection agrees with the one on
the infinity surface.  The normal-jet argument remains the primary proof.

## 3. Every smooth coefficient basepoint creates a forbidden cycle

At any common zero `q` of the four homogenized coefficients, the incidence
contains `E={q} times P1`.  Its first base jet is

```text
Phi^h=s p(X,Y)+t r(X,Y)+O((s,t)^2).
```

Smoothness says that the cubic sections `p,r` have no common zero, so
`rho=[p:r]:E->P1` has degree three.  Chartwise
`(s,t)O_X=I_E=O_X(-E)`, hence `pi` factors through `Bl_q(P2)` and `A-E` is
nef.  Adjunction and the Wronskian calculation give

```text
E^2=-3,
R_pi=E+D,             D~2A+B-E,
D|E=Ram(rho),         D.E=4,
```

with coefficient exactly one on `E`.  A degree-three map has ramification
contribution at most two at a physical point, so `E` meets `Supp(D)` at at
least two distinct physical points.  Moreover

```text
D=(A+B)+(A-E)
```

is ample plus nef, hence ample; its reduced support is connected by Hodge
index.  If that support is not already a rational tree, the forest theorem has
fired.  If it is a tree, the rational curve `E` and this tree have two
distinct attachments.  Embedded resolution only subdivides the two joining
paths or adds pendant vertices, so the full resolved boundary has a cycle.

At a projective basepoint, `E` lies in infinity.  At an affine basepoint, the
boundary assertion uses the Stein bridge in Section 4.  The following reviewer
correction is binding when several affine basepoints occur: every component of
`D` is still boundary, but for three possible reasons.  Components in `H` are
infinity boundary; components meeting the affine no-basepoint locus are
closures of its non-etale support; exceptional curves over other affine
basepoints contract to non-etale points missed by the first leg.  The last
kind must not be called the closure of a divisorial affine non-etale component.

## 4. Exact affine Stein bridge

Let `Z` be the finite affine common-zero scheme.  A divisorial common factor is
already impossible: at its generic DVR, normality makes the localized cubic
order semilocal Dedekind, whereas the specialized Miranda table would be the
local algebra `kappa direct-sum V`, `dim V=2`, `V^2=0`.  The only one-prime
degree-three cases are `(e,f)=(1,3)`, with field fibre, and `(3,1)`, whose
radical has nonzero square.  Neither is the displayed square-zero fibre.  Two
generic linear combinations then bound the remaining quadratic common-zero
scheme by length four.

For the affine incidence `pi_0:X_aff->A2`, relative cohomology of

```text
0 -> O(-3) --Phi--> O -> O_Xaff -> 0
```

gives a locally free rank-three algebra

```text
0 -> C[u,v] -> (pi_0)_*O_Xaff -> C[u,v]^2 -> 0.
```

Over `A2-Z`, Miranda's construction identifies it as an algebra with `B_K`.
Both sides are locally free, hence reflexive, on the regular surface; the
isomorphism and inverse extend uniquely across codimension two, and the
multiplication identities extend from the dense open.  Thus

```text
Spec((pi_0)_*O_Xaff)=Spec(B_K)=Y.
```

The Stein morphism is an isomorphism off `Z` and contracts each exceptional
`E_q` to the unique point of the square-zero specialized Miranda algebra.
That point is non-etale.  The square-zero claim is read on the `B_K` side from
the multiplication table, not from an invalid base-change of global
functions.  The promoted first leg lies in `Y_sm` off the non-etale locus, so
it misses every contracted point and lifts through the isomorphism locus.
Therefore every `E_q`, and the entire residual different described above, is
in the full first-leg boundary.  The cycle obstruction applies to affine as
well as projective coefficient basepoints.

After all basepoints are eliminated, every projective fibre is a nonzero
length-three divisor in `P1`; proper quasi-finiteness makes `pi` finite.  The
smooth-squarefree theorem and the promoted lattice closure `c9871c92...` now
exclude the remaining finite quadratic incidence types.  Literal homogeneous
fibre-degree drop contradicts the generic cubic field.  Source generic degree
one exits the proper-block hypothesis; quotient degree two is Galois and is
excluded by the promoted non-Galois theorem.  No one of these typings is
substituted for another.

## 5. Promoted one-attachment/maximal-discriminant theorem

Independently of the quadratic closure, let `X` be a smooth irreducible
hypersurface of class `dA+3B`, `d>=1`, in `P2 times P1`.  Assume `pi:X->P2`
is generically finite and finite near reduced infinity `H`, and assume the
resolved full boundary containing `H` and the reduced source-critical support
is a rational forest.  Then:

```text
H intersect Supp(R_pi) is one physical source point p;
H is three smooth sections with degrees (b,a,a),  d=2a+b, 0<=b<=a;
Disc(H/L_infinity)=c ell^(4d), c!=0;
the full affine discriminant of the associated global trace-zero Miranda
presentation has exact total degree 4d;
the displayed degree d is minimal among global trace-zero bases of this same
finite locally free rank-three C[u,v]-algebra;
the one-dimensional boundary order has normalization-index length 2d.
```

Here “one physical point” does not mean one branch or one normalization
point.  The graph proof is the connected-subtree lemma: in a forest, the
intersection of two connected subtrees is connected.  The total transforms of
connected `H` and connected `Supp(R_pi)` are subtrees; clusters over two
distinct physical intersections would give a disconnected intersection.
Since `H.R_pi=4d>0` and the supports share no component, exactly one physical
intersection remains.

Riemann--Hurwitz then makes every normalized infinity component degree one
over `L_infinity`; finite birationality to the normal target makes each
component a smooth section.  Three local section graphs through the one point
satisfy the nonarchimedean triangle rule on pairwise contacts, forcing the
degree pattern `(b,a,a)`.

The map `H->L_infinity` is finite because there is no vertical component and
flat because the Cartier curve is Cohen--Macaulay and torsion-free over each
target DVR.  Its rank is three.  Its nonzero discriminant is a section of
`O(4d)` supported at the one target value, hence is `c ell^(4d)`.  Equivalently,
the sum of pairwise contacts is `2d` and the root discriminant doubles it.
This nonzero top homogeneous discriminant proves that the full affine
discriminant has degree exactly `4d`; no top-degree cancellation occurs.

For any other global trace-zero basis of the **same** finite locally free
cubic algebra, the change matrix lies in `GL_2(C[u,v])` and has constant-unit
determinant.  The intrinsic discriminant retains degree `4d`, while a basis of
coefficient maximum `e` gives degree at most `4e`; hence `e>=d`.  No comparison
with another algebra, arbitrary presentation, target automorphism, or
non-trace-zero coordinate system is made.

Finally, normalization splits the boundary curve into three copies of `P1`.
Since `p_a(H)=2d-2`, its normalization exact sequence gives

```text
length(q_*O_Htilde / q_*O_H)=3-(1-p_a(H))=2d.
```

This is the normalization index of the one-dimensional boundary order only.
It is not a conductor length, surface normalization index, slice theorem, or
Tor/base-change assertion.

For `d=1` the section pattern is impossible; `d=2` gives `(0,1,1)` and is
already excluded in the promoted smooth quadratic lattice scope; `d>=3` was
already excluded under the same smooth first-leg package by geometric genus.
Thus this second theorem adds an exact boundary-shape, discriminant, and
basis-minimality certificate, not a new smooth survivor or stronger
higher-degree closure.

## 6. Scope firewall and next allocation

The smooth degree-at-most-two closure does not prove that a low-degree basis
exists or say anything about a singular quadratic incidence.  Neither theorem
covers a nonnormal incidence, higher coefficient degree, another block degree,
a primitive extension, arbitrary polynomial support, a polynomial map,
counterexample, or JC2.  The one-attachment theorem additionally requires
smoothness, reduced infinity, and projective finiteness near infinity; it must
not be transplanted to a singular/nonreduced/basepoint stratum.

The quadratic campaign should now stop work inside the closed smooth cell.
Its exact active successors are normal singular incidence, nonnormal incidence,
and intrinsic basis-coverage/minimization beyond the conditional fixed-algebra
statement.  The reviewed one-place leading discriminant may inform those
successors, but no `A(F)`, one-place curve, conductor, monodromy, or surface-
index conclusion is presently licensed.  No heavy computation is required by
this integration; any future heavy or uncertain CAS remains AWS-only after a
source-reviewed packet.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14511`.
- Body SHA-256:
  `d495e00843942d5d750595b0178c3a90340ac58b8808d285f45c8005cfa34fda`.
- Frozen basis: `ce162f50f6068b48527434b8aac1dbf1875bc552`.
