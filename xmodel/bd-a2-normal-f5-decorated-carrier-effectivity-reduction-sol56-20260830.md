# The normal F5-decorated carrier reduction in the nine-blowup marking

Date: 2026-08-30 UTC  
Producer: Sol 5.6 delegated lane `/root/quadratic_degeneracy_frontier`  
Frozen basis: `fb66748d370da321d6e914521ecfb453465ffa2e`  
Lifecycle: **EXACT PROVISIONAL NECESSARY-STATE THEOREM / RAMIFICATION EFFECTIVITY OPEN**

## 0. Verdict, charged inputs, and scope

This packet charges, provisionally where indicated,

```text
413489b037be9533337f53e6bd104549c2ef663c4afd27927230d469ac1b1128
  xmodel/bd-a2-normal-singular-reduced-finite-f5-bridge-sol56-20260830.md
  (sealed provisional F5 bridge);

9a02c626267b1cd9fa31d241119f096d0915afa5f418a592589a6bdf68d9b037
  xmodel/bd-a2-d9-global-fibre-orbit-cap-ledger-sol56-20260830.md;

f7d1c8cb42d5afd29474eb0975ffae518b0c82620f598649c2ac3d5d59064f94
  xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-sol56-20260830.md;

8fcd071fff6e828879b7926ad9398f3d33f81344e58f6fe04c758a19c326641e
  xmodel/bd-a2-f5-local-different-two-branch-coordinator-integration-sol56-20260830.md
  (only when the F5 point is smooth);

255bd0ba04e1c0a428a18caa70e73bc35895026c5857f629ed855cee79a8f803
  xmodel/bd-a2-quadratic-ramification-attachment-coordinator-integration-sol56-20260830.md
  (localization and rational-forest connector lemmas).
```

Thus `X` is a normal irreducible class-`2A+3B` incidence surface with only
Du Val singularities, `pi:X->P2` is generically finite and finite on a
neighbourhood of the reduced infinity curve `H`, and the charged dominant
first-leg/rational-forest hypotheses hold.  On the minimal resolution

```text
r:Xtilde->X,
A^2=3,       A.B=2,       B^2=0,       K_Xtilde=-A+B.       (0.1)
```

The provisional bridge forces

```text
H=L+S+T of type F5=(0,1)+(1,1)+(1,1),                     (0.2)
```

with its full length-eight intersection with the ramification Cartier
divisor `R_X~2A+B` at the unique F5 point `p_0`.

The finiteness assumption is deliberately only **near `H`**.  It does not
remove affine coefficient-basepoint curves contracted by `pi`, and it does
not remove affine ADE trees.  In particular this packet does not silently
replace the charged scope by global projective finiteness.

> **F5 carrier/fibre theorem.**  Choose one of the two section branches and
> call it `S`.  There is an `S`-adapted contraction to `F_2` and an orthogonal
> total-transform basis
>
> ```text
> S=S_0,       B=F,
> A=2S_0+5F-sum_(i=1)^9 E_i.                            (0.3)
> ```
>
> If `p_0` is smooth, its fibre is `B_1` and, after relabelling,
>
> ```text
> L=F-E_l,
> T=S_0+4F-sum_(i!=l)E_i.                              (0.4)
> ```
>
> If `p_0` is Du Val, then `L=E_l`.  The local Cartan list and the actual
> weighted fibre tree reduce to exactly nine **necessary marked carrier
> tags**:
>
> ```text
> q=6:  B_3/A_2, U_3/A_3;
> q=8:  B_5/A_4, B_6/A_5, B_7/A_6, B_8/A_7, B_9/A_8,
>       U_5/D_5, U_6/D_6.                              (0.5)
> ```
>
> Here `q=h^t a`; `B_s` and `U_s` retain their actual fibre marking and are
> not identified by an abstract root-system isomorphism.  Every tag in
> (0.5) is necessary, not asserted effective.  The balanced `B_4/A_3` and
> `U_4/D_4` rows die, while the alternate `U_3/A_3` row survives.
>
> All ADE points away from `p_0` remain in the state.  The packet gives an
> exact class/proximity system for their ramification carriers, an exact
> list of possible affine `A`-null carriers, and proper residual fibre
> identities.  It does **not** solve the singular-`p_0` local different or
> prove multiplicity one for an affine curve contracted to a coefficient
> basepoint.

Sections 1--5 prove the finite carrier theorem.  Sections 6--9 give the
global effectivity system and state its exact endpoint.

## 1. The three F5 carriers and their fibre degrees

The class labels in (0.2) record degrees to the two factors of
`H subset L_infinity times P1`.  Since `B` is a source-fibre class,

```text
B.L=0,       B.S=B.T=1.                                (1.1)
```

Thus `L` is a component of one actual fibre of `Xtilde->P1`, while `S` and
`T` are sections.  The three components split `A.H=A^2=3`, and each has
positive target degree, so

```text
A.L=A.S=A.T=1.                                        (1.2)
```

The proper transforms are smooth rational curves.  Adjunction with (0.1)
then gives

```text
L^2=-1,              S^2=T^2=-2.                      (1.3)
```

Suppose `p_0` is singular.  The saturated target-line cap in the F5 bridge
says that each of the three analytic boundary branches has one transverse
unit contact with a smooth point of the exceptional divisor.  Write the
scheme fibre through `L` as `F_0=sum beta_v C_v`.  Since a section has
fibre degree one,

```text
1=F_0.S=sum beta_v(C_v.S),                             (1.4)
```

and all summands are nonnegative.  The exceptional contact of `S` already
contributes one, so it is on a `beta=1` component and every other summand is
zero.  In particular `L.S=0`.  The same argument gives

```text
L.S=L.T=0                                             (1.5)
```

in the singular case.  This is stronger than merely knowing that the three
branches have distinct normalization points.

The F5 curve has `delta_p0(H)=4`.  If

```text
r^*H=H'+sum h_iE_i,       a_i=H'.E_i,       a=Ch,
q=h^t a,
```

the crepant genus formula gives residual strict-transform delta

```text
delta(H' over p_0)=4-q/2.                              (1.6)
```

Every strict branch remains smooth.  By (1.5), the only possible residual
pairwise intersection is between `S` and `T`.  Hence

```text
S.T=1 for q=6,            S.T=0 for q=8.               (1.7)
```

The first equality is one physical common attachment of `S` and `T`; it is
not two graph vertices or the formal coefficient two in `a`.

## 2. The `S`-adapted contraction and the `F_2` marking

The weighted fibre blocks from the charged global theorem are as follows.
Subscripts are scheme-fibre multiplicities `beta`.

```text
B_s:  o(-1)_1--E_1(-2)_1--...--E_(s-1)(-2)_1--o(-1)_1
      exceptional root tree A_(s-1).

U_2:  E_1(-2)_1--o(-1)_2--E_2(-2)_1
      exceptional root tree A_1 + A_1.

U_s, s>=3:
                                      E_(s-1)(-2)_1
                                     /
 o(-1)_2--E_1(-2)_2--...--E_(s-2)(-2)_2
                                     \
                                      E_s(-2)_1
      exceptional root tree A_3 for s=3, D_s for s>=4. (2.1)
```

In `U_s` the nonexceptional `(-1)` vertex is attached to standard `D_s`
vertex `1`; for `U_3` it is attached to the central vertex of the root
`A_3`.  When `U_3` is written in `A_3` notation below, its path is relabeled
spin--central--spin as vertices `1--2--3`; thus the central vertex is `2`
even though it is `E_1` in the displayed low-rank `D`-style diagram.  The
two spin vertices are the only root vertices of weight one.

A section must meet a weight-one fibre component.  In either diagram, one
can contract a vertical `(-1)` curve disjoint from `S`, then repeat on the
new weighted tree.  For `B_s`, peel from an endpoint not retained by `S`,
and then from the other side if needed.  For `U_s`, first contract the
weight-two `(-1)` vertex and peel toward the weight-one component met by
`S`; the special `U_2` diagram is the same two-step operation.  At every
stage the contracted curve is disjoint from the current transform of `S`.
Doing this in every affected fibre leaves a relatively minimal ruled
surface, and preserves `S^2=-2`.

On a Hirzebruch surface, an irreducible section of negative square is the
minimal section: a class `S_e+kF` with `0<k<e` contains `S_e` as a fixed
component.  Therefore the ruled endpoint is exactly `F_2` and `S=S_0`.
The contractions are inverse to nine blowups whose centres are disjoint
from `S_0`; the charged coefficient comparison then becomes (0.3).

This also handles infinitely-near centres.  In the singular case (1.5)
allows `L`, already a `(-1)` curve, to be chosen as the first contraction.
In the inverse sequence it is the last-created exceptional curve and has
no descendant.  Its orthogonal total-transform class can therefore be
relabeled

```text
L=E_l.                                                (2.2)
```

No assertion that `L` is exceptional for `r:Xtilde->X` is being made: it is
exceptional only for this chosen contraction to `F_2`.  In the smooth case
`S` meets `L`, so the other `(-1)` component of the `B_1` fibre is contracted
and

```text
L=F-E_l.                                              (2.3)
```

Thus (2.2)--(2.3) remain exact even when other blowups are infinitely near.

## 3. Exact ruled classes and proximity constraints

Because `T` is a smooth section and every inverse blowup centre has
multiplicity zero or one on its successive transform, write

```text
T=S_0+bF-sum_(i in I)E_i.                             (3.1)
```

For completeness, the binary multiplicities do not assume that the nine
centres were initially distinct.  At every stage a section meets a scheme
fibre once, at a smooth point of a weight-one component.  Blowing down a
vertical `(-1)` curve therefore either misses the section or sends it
isomorphically to another smooth section.  In the inverse sequence a centre
on `T` consequently has multiplicity exactly one, including when it is
infinitely near to an earlier centre.

Its square `-2` gives

```text
|I|=2b.                                               (3.2)
```

### 3.1 Smooth `p_0`

Here `L.S=L.T=1` and `S.T=2`.  Equations (2.3) and (3.1) give

```text
b=4,       l notin I,       |I|=8.
```

This is exactly (0.4).  Any root adjacent to `L` would contract to an ADE
point somewhere on `L`.  The F5 curve is smooth away from `p_0`, Section 5
excludes an ADE point there, and `p_0` is smooth in the present case.  Hence
the actual fibre is `B_1`, not a larger fibre carrying a hidden root tree.

### 3.2 Singular `p_0`

Retain, during the contraction of Section 2, the weight-one exceptional
component `C_S` met by `S`.  Let `h_S` be its coefficient in the exceptional
cycle of `r^*H`.  All other exceptional components contract to points on
the `F_2` endpoint, while `C_S` pushes to the fibre `F`; hence that cycle
pushes forward to `h_S F`.  Comparing

```text
A=L+S+T+Z_H
```

with (0.3), (2.2), and (3.1) yields

```text
b=5-h_S,
T=S_0+(5-h_S)F-sum_(i in I)E_i,
l notin I,       |I|=2(5-h_S),                        (3.3)

Z_H=h_S F-2E_l-sum_(i notin I, i!=l)E_i.              (3.4)
```

The expression (3.4) is in the orthogonal total-transform basis; it is not
a claim that the actual exceptional cycle is supported on the displayed
individual `E_i`.

Since the blowup centres avoid `S_0`, (3.1) also gives

```text
S.T=3-h_S.                                            (3.5)
```

Combining (1.7) and (3.5),

```text
q=6: h_S=2,  T=S_0+3F-sum_(i in I_6)E_i, |I_6|=6;
q=8: h_S=3,  T=S_0+2F-sum_(i in I_4)E_i, |I_4|=4.      (3.6)
```

Equivalently, the two residual exceptional-cycle classes are

```text
q=6: Z_H=2F-2E_l-E_j-E_k;
q=8: Z_H=3F-2E_l-E_j-E_k-E_u-E_v,                     (3.7)
```

where the displayed indices are the complements of `I` and `l`.  Their
squares are respectively `-6` and `-8`, as required by `Z_H^2=-q`.

The retained root has class

```text
C_S=F-E_i-E_j.                                       (3.8)
```

for the two (possibly successive infinitely-near) centres lying on its
transform.  Positivity of `T.C_S=1-1_(i in I)-1_(j in I)` gives the exact
proximity test

```text
T meets C_S:          i,j notin I;
T misses C_S:         exactly one of i,j lies in I.   (3.9)
```

The impossible alternative with both indices in `I` would give negative
intersection.  Likewise the root adjacent to `L=E_l` has coefficient `-1`
in coordinate `l`; this is the total-basis version of its physical edge to
`L`.  Equations (3.3), (3.8), and (3.9), together with the chronological
proximity inequalities for the nine blowups, are binding.  Merely choosing
subsets `I` does not prove effectivity.

## 4. Physical carrier classification at a singular F5 point

Fix the standard root numbering displayed in (2.1), and fix `L` rather than
quotienting it by an abstract diagram automorphism.  Each F5 branch has one
unit transverse exceptional contact.  For `q=6`, (1.7) says that `S` and
`T` use the same physical smooth point of one exceptional component; the
`L` contact is a different physical point.  For `q=8`, all three contacts
are physically distinct.  This converts the provisional local Cartan rows
into the following exact marked-fibre table.

| `q` | local row and actual fibre | physical carrier assignment | rank at `p_0` | verdict |
|---:|---|---|---:|---|
| 6 | `A_2`, `B_3`, `a=3e_1` | `L` meets `E_1`; `S,T` share another point of `E_1` | 2 | necessary survivor |
| 6 | `A_r`, `B_(r+1)`, `3<=r<=8` | the singleton in `2e_1+e_(r-1)` is not the endpoint forced by `L` | `r` | killed; in particular `B_4/A_3` dies |
| 6 | `A_3`, `U_3`, `a=2e_1+e_2` | `L` meets central vertex `2`; `S,T` share a point on spin `1` | 3 | necessary survivor |
| 6 | `D_4`, `U_4`, `a=e_1+e_3+e_4` | `L` meets `1`; `S,T` meet the two distinct spins `3,4` | 4 | killed because `S.T=0`, not `1` |
| 8 | `A_r`, `B_(r+1)`, `4<=r<=8`, `a=e_1+e_2+e_(r-2)` | `L` meets endpoint `1`; `S,T` meet `2,r-2` at distinct points | `r` | necessary survivors `B_5` through `B_9` |
| 8 | `D_5`, `U_5`, `a=e_1+2e_4` | `L` meets `1`; `S,T` use distinct points of one spin | 5 | necessary survivor |
| 8 | `D_6`, `U_6`, `a=e_1+e_5+e_6` | `L` meets `1`; `S,T` use the two spin vertices | 6 | necessary survivor |

For `A_4`, the two section contacts in the fifth row are distinct physical
points on the same vertex `2`.  A formal coefficient two is not itself a
single germ.  The reason `B_4/A_3` and `U_3/A_3` differ is precisely the
marked nonexceptional carrier: `L` is forced to an endpoint in `B_4` but to
the central vertex in `U_3`.  The reason `D_4` dies is the residual physical
intersection (1.7), not a Cartan congruence.

The table proves (0.5).  It is not an analytic realization theorem.  In
particular, the three prescribed smooth attachment points, the total-basis
proximity history, and an incidence equation still have to coexist.

At `p_0`, finiteness near `H` rules out an additional nonexceptional
`A`-null `(-2)` component in the same connected fibre tree: its image would
be a positive-dimensional `pi`-fibre passing through `H`.  Thus the root
tree used in the table is the whole `B_s/U_s` root block.  Away from `p_0`,
the present hypotheses are not globally projectively finite.  Abstract
`D9` roots must therefore still be separated from actual effective
exceptional curves and possible nonfinite fibre carriers.

One useful exact subfilter survives.  If every `(-2)` vertex of a `U_s`
block away from `p_0` is known to be `r`-exceptional, a section must meet a
weight-one spin vertex and hence would pass through an ADE point on the
otherwise smooth F5 boundary.  That is impossible.  Therefore there is no
additional **all-exceptional** `U_s` block away from `p_0`.  This does not
discard an incompletely identified/nonfinite fibre merely because its
abstract root signature is tagged `U_s`.

## 5. The unconditional reduced-infinity energy

There is no ADE point of `X` on `H` away from `p_0`.  Indeed the local
crepant genus identity at a point of reduced `H` is

```text
delta_p(H)=h^t a/2+sum_(q over p)delta_q(H').          (5.1)
```

Its right side is positive at an ADE point, whereas every point of the F5
curve away from `p_0` is smooth.

Globally put

```text
D_H=Supp(r^*H)=H'+sum E,
W_H=r^*H-D_H=sum(h_i-1)E_i.                            (5.2)
```

The reduced divisor `D_H` is connected.  Since `A` and `K_Xtilde` are
orthogonal to every Du Val exceptional curve and `p_a(A)=2`, adjunction
gives

```text
p_a(D_H)
 =2-(1/2)sum_trees (h-1)^t C(h-1)>=0,

sum_trees (h-1)^t C(h-1)<=4.                          (5.3)
```

This cap is unconditional in the present reduced-`H` scope.  At a connected
F5 tree, `sum a_i=3` and `1^tC1=2`, so its energy is

```text
(h-1)^tC(h-1)=h^t a-2sum a_i+2=q-4.                   (5.4)
```

Thus a `q=6` tag consumes two units and a `q=8` tag consumes all four.  Since
there is no other ADE point on `H`, these are the full global `H` energies,
not per-point budgets.

## 6. Affine `A`-null carriers

Let `Z` be a nonexceptional curve contracted by `pi` to an affine
coefficient basepoint.  In the incidence it is the full source line over
that target point, so

```text
A.Z=0,       B.Z=1.
```

Its strict transform is a smooth rational curve.  Adjunction gives
`Z^2=-3`, and finiteness near `H` makes it disjoint from `H`, hence from
`S_0`.  In the marking (0.3) every such curve has the necessary class

```text
Z_J=S_0+2F-sum_(j in J)E_j,       |J|=5.              (6.1)
```

The entries are zero or one because the successive transforms of a smooth
curve have multiplicity one at every centre they contain.

For a fixed marked F5 state, disjointness from `L` and `T` gives:

| state | exact subset equations | raw coordinate candidates |
|---|---|---:|
| smooth `p_0` | `l in J`; equivalently choose four of the other eight | 70 |
| singular `q=6` | `l notin J`, `|J cap I_6|=3` | 20 |
| singular `q=8` | `l notin J`, `|J cap I_4|=2` | 24 |

These counts precede chronological proximity and effectivity.  Distinct
contracted curves lie over distinct target points and hence are disjoint.
But

```text
Z_J.Z_K=2-|J cap K|,                                  (6.2)
```

so coexistence requires `|J cap K|=2`; three such five-subsets cannot coexist
by inclusion-exclusion.  In the singular rows there are respectively `10`
and `36` raw compatible unordered pairs.  Again these are numerical
signatures, not constructed coefficient basepoints.

Every such `Z_J` is a component of ramification because the differential of
`pi` drops rank generically along a contracted curve.  Its Cartier
multiplicity is **not** controlled by height-one inertia in the target: its
image has codimension two.  This is the central scope firewall for the
global different.

## 7. Exact global ramification class system

In the `F_2` marking,

```text
r^*R_X=2A+B=4S_0+11F-2sum_iE_i.                       (7.1)
```

Separate the strict nonexceptional ramification carriers into:

```text
C_j:   A.C_j>0, mapping generically to a target divisor;
Z_k:   A.Z_k=0, contracted to an affine target point;
M:     sum m_alpha E_alpha, the actual Du Val exceptional cycle.
```

At the generic point of a `C_j`, the charged fixed-sheet cubic theorem gives
tame inertia `(2,1)`, so its different coefficient is one.  This applies to
every noncontracted prime: no projective prime can hide wholly at infinity,
because `pi^*(L_infinity)=H` and `H` shares no component with `R_X`.
Write the uncontrolled coefficient of `Z_k` as `nu_k>=1`.  Then the binding
class and degree equations are

```text
sum_j C_j+sum_k nu_k Z_k+M
     =4S_0+11F-2sum_iE_i,                              (7.2)

sum_j A.C_j=8,
sum_j B.C_j+sum_k nu_k=4.                              (7.3)
```

At every ADE tree, `M` has positive integral coefficient vector `m` and
strict-transform intersection vector `n=Cm>=0`.  The total-basis expansion
of `M` may contain an `F` term; it must not be replaced by a sum of the
orthogonal symbols `E_i` with the same coefficients.

For a horizontal rational carrier, write

```text
C=dS_0+bF-sum_i mu_iE_i,       d=B.C>=1.               (7.4)
```

The multiplicities are nonnegative and obey the chronological proximity
inequalities.  If `a=A.C`, then

```text
a=d+2b-sum_i mu_i,
C^2=-2d^2+2db-sum_i mu_i^2,
delta(C)=1+(C^2-a+d)/2 in Z_(>=0).                     (7.5)
```

The last equality uses the rational-forest theorem, which makes the
normalization of every reduced boundary carrier rational.  Nonexceptional
vertical fibre carriers have `d=0` and must instead be read directly from
the marked `B_s/U_s` diagrams.

If `p_0` is smooth, the charged local calculation gives two distinct
nonexceptional ramification primes `C_3,C_5` with

```text
A.C_3=3,       A.C_5=5.                               (7.6)
```

They are distinct because placing the two local normalization branches on
one global prime creates a rational-forest cycle.  Equation (7.3) then says
that every other nonexceptional ramification prime is one of the contracted
`Z_k`.  Hence the exact smooth-`p_0` decomposition is

```text
r^*R_X=C_3+C_5+sum_k nu_k Z_k+M.                      (7.7)
```

This does not import the old smooth-surface lattice closure: `X` may still
have affine ADE points and affine coefficient basepoints.

If `p_0` is singular, the strict local different has not yet been factored.
The positive integers `A.C_j` form a partition of eight, all their boundary
contact is over `p_0`, and (7.2)--(7.5) are the exact finite threat system.
No analogue of the smooth `3+5` split is asserted.

## 8. Proper residual fibre identities, localization, and support genus

The raw `B.R_X=4` cap cannot be charged against a fibre that is itself a
strict carrier.  Let an actual scheme fibre be

```text
F_t=Gamma+sum_i beta_iE_i,                             (8.1)
```

where `Gamma` is its scheme-weighted nonexceptional part.  Let `V` be the
sum of all nonexceptional fibre components common with the strict
ramification, put `v_i=V.E_i`, and write `R_o=R_str-V`.  Total-fibre
orthogonality gives `F_t.V=F_t.M=0`, and properness after removing every
common carrier gives the exact identity

```text
4=F_t.r^*R_X=Gamma.R_o+beta^t(n-v),
beta^t(n-v)<=4.                                       (8.2)
```

All terms in the displayed decomposition are nonnegative.  It is
`n-v`, not the formal `n`, that consumes the residual fibre budget.

At the F5 fibre, put `ell_i=L.E_i`.  Since `L` is the unique common
nonexceptional fibre component of `r^*H`, the parallel identity is

```text
2=F_0.r^*H=Gamma.(S+T)+beta^t(a-ell).                 (8.3)
```

For singular `p_0`, the first term is zero and the two section contacts have
weight one, so (8.3) is saturated as `2=0+2`.  For smooth `p_0`, there is no
exceptional term and the two intersections with `L` give `2=2+0`.  These
are shared budgets on the actual fibre, not independent per-singularity
caps.

There is a separate proper target-image budget.  For a target point `q`,
choose a generic target line through `q` which is not the image of a strict
ramification carrier.  If `ell^(p)` is its positive exceptional valuation
vector at each singular point `p` over `q`, total-pullback orthogonality
leaves exactly

```text
8=r^*M_q.r^*R_X
 =M_q'.R_str+sum_(p over q) (ell^(p))^t n^(p).         (8.4)
```

The proper strict term is nonnegative and every entry of every `ell^(p)` is
at least one.  Consequently

```text
sum_(p over q) sum_i n_i^(p)<=8.                       (8.5)
```

This is shared by singularities with the same target image.  It is neither
a per-point copy of eight nor the fibre budget (8.2).  Common target-image
carriers have been excluded by the generic choice of line.

Let `Y=X minus H` and `U=Y minus Supp(R_X)`.  Dominance by the affine source
gives

```text
O(Y)^*=O(U)^*=C^*.
```

The divisor localization sequence therefore injects the free group on all
reduced nonexceptional ramification primes into `Cl(Y)`.  Consequently any
relation on `Xtilde`

```text
sum_j q_j C_j+sum_k q_k Z_k ~lin cA+(exceptional divisor) (8.6)
```

with a nonzero vector of coefficients is impossible after pushdown and
restriction to `Y`.  Cartier multiplicities in (7.2) are irrelevant to this
reduced-prime independence test.

There is also an exact connected-support formula.  Put

```text
D_R=Supp(r^*R_X),
W_R=r^*R_X-D_R
   =sum_k(nu_k-1)Z_k+sum_alpha(m_alpha-1)E_alpha.       (8.7)
```

The reduced support `D_R` is connected and `p_a(r^*R_X)=9`.  Since

```text
r^*R_X.Z_k=K_Xtilde.Z_k=1,
r^*R_X.E_alpha=K_Xtilde.E_alpha=0,
```

adjunction gives the unconditional equality

```text
p_a(D_R)
 =9+(W_R^2-3sum_k(nu_k-1))/2>=0.                      (8.8)
```

Only in the additional subcell `nu_k=1` for every contracted carrier does
(8.8) reduce to

```text
sum_trees (m-1)^t C(m-1)<=18.                         (8.9)
```

There is no theorem in the charged scope forcing that subcell.  In
particular, fixed-sheet divisorial inertia does not control a curve mapped
to a target point, so (8.9) is **conditional**.

Finally, the reduced resolved first-leg boundary is a rational forest.
Connected total transforms of `H` and `Supp(R_X)` may have only one joining
cluster.  Within `Supp(R_X)`, an affine ADE tree or an `A`-null carrier cannot
give a second path between already-connected carrier subgraphs.  Physical
attachment points must first be grouped into clusters; a formal vector
entry, a root vertex, and a physical germ are three different objects.
This connector test and the class-group test (8.6) are exact eliminators,
but neither is a converse effectivity criterion.

## 9. Global finite state and exact remaining gap

A global necessary state is now specified by the following finite data.

1. Choose the smooth `B_1` state (0.4), or one of the nine marked singular
   tags (0.5), including its subset `I`, total-basis root classes, physical
   attachment partition, and proximity history.
2. Allocate the remaining blowup coordinates among actual affine fibre
   blocks.  Retain their source-fibre labels, target-image labels, effective
   exceptional curves, and local pairs `(m,n)`; do not replace this layer by
   an unmarked `W(D9)` root orbit.
3. Add zero, one, or two candidates (6.1), with their multiplicities `nu`
   and proximity histories.
4. Solve (7.2)--(7.5), the proper residual identities (8.2)--(8.5), the
   localization test (8.6), support genus (8.8), and the physical
   rational-forest connector test.

The state space is finite.  There are nine blowups; (8.5) bounds every local
`n` and hence every `m=C^(-1)n`; (7.3) bounds the horizontal and contracted
carrier degrees; and pushing (7.2) to `F_2` bounds every nonnegative fibre
coefficient by eleven.  Equations (7.3)--(7.5) then bound all centre
multiplicities.  No heavy enumeration is justified yet: the
singular-`p_0` local different partition and the multiplicities `nu_k` are
the two missing geometric inputs, and enumerating before they are known
would only multiply nonrealizable lattice signatures.

For later filters, expose the two coarse invariants

```text
rho = total rank of every Du Val tree on X, including affine trees;
k   = number of distinct reduced nonexceptional ramification primes,
      including every affine contracted Z_k regardless of nu_k. (9.1)
```

The present theorem gives `k>=2` in the smooth-`p_0` state and `k>=1` in
every singular state.  The local contribution to `rho` is respectively

```text
state:       smooth A2 A3 A4 A5 A6 A7 A8 D5 D6
rho_p0:        0    2  3  4  5  6  7  8  5  6.        (9.2)
```

### Review-gated out-of-basis successor

A later producer announced under prefix `b0f4d09c`, not present on the
frozen basis and still under review, proposes an Euler/`A^1`-ruling cap

```text
rho+s+k<=11,
```

where `s=3` for F5, hence `rho+k<=8`; its additional `P1`-base branch would
give `rho+k<=7`.  This packet does not charge either inequality.  If the
review promotes them, (9.2) makes the interface immediate: `A8` dies because
`k>=1`, and every rank-at-least-seven state dies when `k>=2`.  Equality has
the extra irreducible-reduced-fibre condition in that new `A^1` ruling, not in
the conic `B`-fibration used here.

The exact remaining gap is therefore not an abstract `D9` orbit count.  It
is the singular-F5 local different together with effectivity/proximity and
the possible higher multiplicity of affine Stein-contracted carriers.  This
packet proves no realization or exclusion of the nine tags, no global
projective finiteness, no unconditional ramification-energy cap, no
quadratic basis-minimization theorem, no higher-degree block result, no map
or counterexample, and no JC2 conclusion.  Normal ADE triage outside this
declared reduced F5 cell remains separate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `28064`.
- Body SHA-256:
  `e4823537bbaa3bb6142790456c11814d9be32c8b3f4c93f2563a2a13eb2a641d`.
- Frozen basis: `fb66748d370da321d6e914521ecfb453465ffa2e`.
