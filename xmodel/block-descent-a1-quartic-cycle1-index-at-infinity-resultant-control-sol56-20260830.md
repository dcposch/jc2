# Rank-four `R4-CYCLE-1`: index at infinity and companion-resultant control

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_cycle1_function_pair` lane)  
Frozen basis: `b3d98d87e9bb9664da7b175b76204bb7eadf1e5d`  
Lifecycle: **FINAL+VERIFIED EXACT CONDITIONAL SUCCESSOR / INDEX IMPLICATION NEGATIVE / HORN OPEN**

## 0. Verdict

Take the inverse-Kummer/primitive-quartic theorem provisionally while its
hostile review runs.  Its forced monogenic coincidence divisor

```text
J_t: u^mu-v^mu=0
```

does **not** necessarily contribute a positive Orevkov--Chau boundary term.
The two quantities measure different maps.

At a height-one prime `q` of `V=A2-B`, with `A=O(V)`, finite-etale
normalization `S`, and quartic order `O=A[t]`, the exact lattice formula is

```text
v_q(Disc(P_t))
  =2 length_(A_q)(S_q/O_q),       v_q(Disc(S/A))=0.      (0.1)
```

Thus `J_t` is an **index divisor**: the chosen primitive element fails to
separate distinct etale sheets.  It is the image of an off-diagonal
coincidence in `S times_A S`.

Orevkov's primary Lemma 4.2, as restated by Chau Remark 4.9, instead says

```text
deg_geo(H)-1
 =sum_(dicritical l)[mu_l
      +sum_(x in l finite)(mu_x-mu_l)].                 (0.2)
```

Here `mu_x` is the **local multiplicity of the actual regularized map at the
single boundary point `x`** and `mu_l` is its generic value.  Formula (0.2)
does not contain the discriminant of an auxiliary field generator.

In the charged horn every deleted cyclic line is already charged its base
term `mu_l=1`.  At the self-identification, the ambient completion is etale
at each of the two distinct boundary points, so `mu_x=1` at each.  Their
common image creates no correction.  If the collision lies on an ordinary
point of `B`, it occurs on the two interior companion sheets; the ramified
boundary point is a third, distinct point and receives no forced jump.
Hence the saturated budget stays saturated.

Two exact controls make the distinction sharp.

1. A connected rank-four finite-etale algebra admits primitive generators
   whose monogenic index along a chosen divisor is arbitrarily large while
   its normalized discriminant remains a unit.
2. A formal tubular map around an immersed nodal boundary line is etale at
   both points identified by the node.  Its Orevkov bracket is exactly one,
   while the two ruling values have coincidence equation `u^mu-v^mu`.

The companion-resultant alternative also does not close.  At an ordinary
`(2,1,1)` point there is an exact local quartic algebra with

```text
P_t(0)=-b^(-1)c_0^mu,
b=u+v,                    c_0=uv,                       (0.3)
```

and the two companion roots `u^mu,v^mu` collide at the smooth point of
`B`.  Clearing the pole makes the quartic relation drop to degree two on
`b=0`; it does not force the cusp or node packet.

Finally, Section 7 gives a global one-place curve-pair firewall.  The curve

```text
B:  Y^2=X^3(X-1)^2
```

has exactly one cusp and one node and Euler characteristic zero.  A second
immersively normalized nodal curve `C_0` has its node at an ordinary point
of `B` and misses both special points.  Thus target curve geometry and raw
resultants alone cannot select the cusp or node.

The minimum missing lemma is genuinely global: it must use the special
Keller/pseudo-plane/link-at-infinity structure to turn an off-diagonal
coincidence into a local-degree jump on an actual dicritical, or to control
the pole exponent of `t` along `B`.  Neither follows from index theory,
`K_U=0`, or the companion census.

## 1. Frozen inputs and exact scope

```text
bcc5148aba1a6cb095401ae8871e184ba6bb3e540395a23c40edc16cb0e363a8
  xmodel/block-descent-a1-quartic-cycle1-kummer-inverse-collision-control-sol56-20260830.md
2e8e73514d1743cdc90934f099eccffc75ef2c4d5a07a5956bbb71cf8dc08aa5
  xmodel/block-descent-a1-quartic-cycle1-kummer-inverse-collision-control-sol56-20260830.md.artifact.json
32780967e3567ae1acc325e70798d78157d86127b7304f52079fef798009b6f1
  xmodel/block-descent-a1-quartic-cycle1-function-pair-hostile-review-gpt55-20260830.md
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7
  refs/chau1999_apm71_full.pdf
```

The hostile review confirms the cyclic replacement and the saturated
Orevkov--Chau budget, with all pseudo-plane hypotheses explicit.  The newer
inverse-Kummer artifact is used provisionally and is not promoted here
beyond its exact conditional assumptions.

We use

```text
A2_(x,y) --f_mu--> U --pi--> A2,       H=pi o f_mu,
t=rho,          t o f_mu=a+c*x^mu,     deg_geo(H)=4mu,
C_0=pi(Phi),    A(H)=B union C_0,       B irreducible.   (1.1)
```

The boundary of the canonical finite completion of `H` consists of the
part over the ramification boundary `R` and the `mu-1` deleted cyclic lines.
The reviewed budget is

```text
4mu-1=(2mu+mu)+(mu-1),                                 (1.2)
```

where the first parentheses are the generic `(2,1,1)` boundary plus the
unique cusp jump, and the second is one base unit for each deleted line.

Primary-source reconstruction uses:

- S. Yu. Orevkov, *On three-sheeted polynomial mappings of C2*, Math.
  USSR-Izv. 29 (1987), 587--596, Lemma 4.2, DOI
  `10.1070/IM1987v029n03ABEH000984`; official English PDF and metadata at
  `https://www.mathnet.ru/eng/im1571`;
- Nguyen Van Chau, *Non-zero constant Jacobian polynomial maps of C2*, Ann.
  Polon. Math. 71 (1999), 287--310, Lemma 4.3, Theorem 4.4, and Remark 4.9,
  in the frozen PDF above.

No source identifies a monogenic index divisor with an Orevkov boundary
correction.  Nothing here constructs a Keller counterexample, a global
quartic cover realizing the controls, or a proof/disproof of JC2.

## 2. What Orevkov--Chau actually counts

Orevkov starts with a smooth compactification of the polynomial source and
regularizes the polynomial map by blowups at infinity.  Write `L_F` for the
irreducible boundary components on which the regular extension is
nonconstant.  Constant boundary trees and the polar boundary are collapsed,
producing a continuous constant-multiplicity map

```text
H*:X*->one-point compactification of A2.
```

Orevkov defines the multiplicity at a source point `x` as the largest `k`
such that every neighborhood of `x` contains `k` points with one common
image.  For a local biholomorphism it is one, even if a distant second
source point has the same image.  For each `l subset L_F`, let `mu_l` be the
generic local multiplicity on its affine image after the collapse.  Lemma
4.2 is exactly

```text
N-1=sum_(l subset L_F)
       [mu_l+sum_(x in l-{infinity})(mu_x-mu_l)],       (2.1)
```

where `N=deg_geo(H)`.  Semicontinuity makes every correction nonnegative.

Chau Remark 4.9 restates (2.1) as formula (4.9).  Its formula (4.10) rewrites
the same terms in Newton--Puiseux charts: the positive corrections occur
where the local degree of a boundary chart exceeds its generic value.
Chau Lemma 4.3 identifies those events with critical/singular
parametrization values.  A node obtained by identifying two distinct
immersed parameter values is not such an event at either parameter.

Three consequences are important here.

1. The outer sum is over actual nonconstant **source boundary components**,
   not target curves and not divisors of an auxiliary discriminant.
2. Two boundary components with the same image are both charged their base
   terms; there is neither cancellation nor an extra term merely because
   their images agree.
3. Two distinct points of one immersed boundary line with the same image
   still have `mu_x=1` when the ambient extension is etale at both.  The
   self-identification is budget-free beyond the line's already charged base
   term.

For the deleted cyclic lines, conclusion 3 gives precisely the `mu-1` in
(1.2).  The index collision cannot be charged a second time without proving
that it creates a new boundary component or a local-degree jump.

## 3. Index discriminant versus normalized ramification

Let

```text
A=O(V),             V=A2-B,
S=O(pi^(-1)(V)),    K=Frac(A),
M=Frac(S)=K(t),     O=A[t]=A[Z]/(P_t).                  (3.1)
```

The algebra `S` is finite etale of rank four over `A`; `O` is a free
rank-four order with normalization `S`.

Localize at a height-one prime `q` of `A`.  The DVR lattice `S_q/O_q` has
Smith exponents `a_1,...,a_4>=0`.  If `C` is the change-of-basis matrix from
an `A_q`-basis of `S_q` to the power basis of `O_q`, then

```text
v_q(det C)=sum_i a_i=length_(A_q)(S_q/O_q).
```

The trace Gram matrices satisfy

```text
Gram(O_q)=C^T Gram(S_q) C.
```

Taking determinants gives the exact discriminant-index formula

```text
v_q(Disc(P_t))
 =v_q(Disc(S_q/A_q))+2 length_(A_q)(S_q/O_q)
 =2 length_(A_q)(S_q/O_q).                              (3.2)
```

The last equality is etaleness.  In differential language,
`Omega_(S/A)=0` and the different of the normalization is the unit ideal.
The nonunit discriminant in (3.2) belongs only to the nonnormal suborder
`O`.

Over a strict henselization, write the four values of `t` as
`t_1,...,t_4`.  Then

```text
Disc(P_t)=product_(i<j)(t_i-t_j)^2.                     (3.3)
```

At the same-fibre collision, two selected values have

```text
t_1-a=u^mu,              t_2-a=v^mu,
t_1-t_2=u^mu-v^mu.                                      (3.4)
```

This is an off-diagonal equality of two etale sections.  Ramification would
instead be failure of one section to be etale along the diagonal.  Equations
(3.2)--(3.4) make the distinction exact.

## 4. Applying the distinction to the saturated horn

### 4.1 Collision outside `B`

At a point outside `B`, `pi` is finite etale and the quartic cover splits
strict-henselian locally into four sections.  The two points with equal
ruling value are interior points of `U`; no source boundary component is
created.  Their equality divisor in the target is not in the outer sum of
(2.1).

Each deleted cyclic line contains corresponding copies of the two
normalization points of `C_0`.  The finite completion is etale along those
lines.  At each point separately, the local multiplicity in Orevkov's sense
is one.  Thus the line's bracket remains

```text
mu_l+sum_x(mu_x-mu_l)=1+0.                              (4.1)
```

The node is a global failure of injectivity of the line parametrization,
not a local failure of etaleness.

### 4.2 Collision at an ordinary point of `B`

The completed quartic algebra has one rank-two ramified factor and two
unramified companion factors.  The collision occurs on the two companion
points in `U`.  The point on the ramification boundary `R` is distinct.
Equality of the two companion values gives no condition on the value or
pole order of `t` at that third point.  Hence the generic boundary term two
over `B` does not jump to three.

The unique `(3,1)` cusp jump is already charged in (1.2), and the omitted
`(2,2)` point is not on `C_0`.  Nothing in (3.4) moves the ordinary collision
to either special value.

### 4.3 Meeting infinity is not enough

The projective closure of the affine index curve must meet the line at
infinity, but (2.1) does not count target intersection with infinity.  It
counts local multiplicity of the regularized source map.  A transversal
meeting of the index curve with an existing boundary image can occur while
the source map remains a local biholomorphism.  A positive correction needs
the additional implication

```text
closure(J_t) meets boundary  =>  mu_x>mu_l,             (4.2)
```

and (4.2) is false for general etale orders and formal boundary maps.

## 5. Two exact index countercontrols

### 5.1 A formal nodal dicritical with bracket one

The immersive polynomial normalization

```text
gamma(s)=(s^2, s(s^2-1))
```

has image `Y^2=X(X-1)^2` and identifies `s=1` with `s=-1` at an ordinary
node.  The derivative never vanishes.  A polynomial tubular extension is

```text
Hbar(s,z)=(s^2+z,
           s(s^2-1)+(3/2)s*z).                          (5.1)
```

Direct differentiation gives

```text
det D(Hbar)=1-(3/2)z.                                   (5.2)
```

Therefore `Hbar` is etale along the line `l={z=0}`.  If that line is deleted
from the source and retained in a completion, its restriction is the
immersive nodal normalization `gamma`.  Both points `s=1,-1` have local
multiplicity one, so its Orevkov bracket is exactly one.

Set locally `t-a=z^mu`.  In the two inverse target charts at the node, the
two transverse boundary equations are `u` and `v`, and equality of the two
values is `u^mu-v^mu=0`.  Thus the exact coincidence divisor coexists with
zero Orevkov correction.  This is a formal-neighborhood control, not a
global Keller map.

### 5.2 A connected rank-four etale algebra with arbitrary index

Let

```text
A=C[u,u^(-1),v],
S=A[z]/(z^4-u)=C[z,z^(-1),v],
h=v+1,                 tau=h^r*z,       r>=1.           (5.3)
```

The algebra `S/A` is connected, finite etale, normal, and rank four.  The
element `tau` is primitive over `Frac(A)`, with minimal polynomial

```text
P_tau(T)=T^4-u*h^(4r).                                  (5.4)
```

At the height-one prime `(h)`, the power basis
`1,tau,tau^2,tau^3` differs from `1,z,z^2,z^3` by determinant

```text
h^(r(1+2+3))=h^(6r).
```

Consequently

```text
length(S_(h)/A_(h)[tau])=6r,
v_h(Disc(P_tau))=12r,
v_h(Disc(S/A))=0.                                      (5.5)
```

The index can be made arbitrarily large without changing the finite-etale
normalization at all.  More generally, multiplying a primitive generator by
a base function changes its order discriminant but not the underlying map.
Orevkov's budget is an invariant of the map; a raw monogenic index is not.

Control (5.3)--(5.5) is a global affine algebra, not a pseudo-plane or a
Keller map.  It proves that any valid implication from `J_t` to (2.1) must
use the special ruling divisor and infinity geometry, not discriminant/index
theory alone.

## 6. Companion norm and resultant: the ordinary-point control

The primitive-quartic artifact gives

```text
P_t(a)=lambda*b^k*c_0^mu in C[X,Y,b^(-1)],             (6.1)
```

where `k` is the valuation of `a-t` at the generic ramification prime over
`B`.  The partition `(2,1,1)` fixes ramification index two but does not fix
`k`.  In particular, (6.1) cannot be specialized to `b=0` before clearing
the unknown poles of every coefficient of `P_t`.

The exact local model displays the failure.  Put

```text
R=C[[u,v]],                  b=u+v,
S=R[z]/(z^2-b) times R times R.                         (6.2)
```

This is rank four finite flat, with fibre `(2,1,1)` at the origin.  Over
`b!=0` it is etale.  On its rank-two factor and two companion factors choose

```text
t-a=(z^(-1), u^mu, v^mu).                              (6.3)
```

The degree-four monogenic polynomial of this local semisimple algebra over
`Frac(R)` is

```text
P_t(Z)=(Z^2-b^(-1))(Z-u^mu)(Z-v^mu),
P_t(0)=-b^(-1)(uv)^mu.                                 (6.4)
```

Thus (6.1) holds with `c_0=uv` and `k=-1`.  Clearing the pole gives

```text
Ptilde(Z)=(bZ^2-1)(Z-u^mu)(Z-v^mu),
Ptilde(0)=-(uv)^mu.                                    (6.5)
```

Modulo `b`, the leading quartic coefficient vanishes and only the two
companion factors remain.  At the origin they both have value `a`, while
`B:{u+v=0}` is smooth.  The target intersection resultant is simply

```text
Res_v(u+v,uv)=-u^2.                                    (6.6)
```

Its double zero records the two branches of `C_0`; it does not make `B`
singular and does not create a `(3,1)` or `(2,2)` packet.

On the actual cyclic source, clearing denominators similarly produces a
polynomial relation whose leading coefficient can be a power of
`q_H=b(H)`.  Restricting that relation to `q_H=0` can drop degree and retain
only the companion roots, exactly as in (6.5).  A resultant proof therefore
needs an independent bound on the `b`-adic coefficient valuations or a
flat monogenic model across `B`; neither is in the frozen package.

## 7. Global one-place curve-pair firewall

Raw target geometry permits the collision at an ordinary point while
realizing the exact cusp/node census.  Define

```text
B:   Y^2=X^3(X-1)^2,
beta(t)=(t^2, t^3(t^2-1)).                              (7.1)
```

The parametrization is birational.  Its derivative vanishes only at `t=0`,
where the local form is an ordinary cusp.  Equality
`beta(t)=beta(-t)` occurs away from zero only at `t=+-1`, producing one
ordinary node at `(1,0)`.  There are no other affine singularities.  The
normalization is `A1`, the cusp is point-bijective, and the node identifies
two points, so

```text
e(B)=0.                                                 (7.2)
```

Now put

```text
C_0: (Y-24)^2=(X-3)(X-4)^2,
gamma(s)=(s^2+3, s(s^2-1)+24).                          (7.3)
```

This normalization is immersive everywhere and identifies `s=1,-1` at the
ordinary node

```text
z_0=(4,24).                                             (7.4)
```

But `z_0=beta(2)` is a smooth point of `B`; for example
`partial(Y^2-X^3(X-1)^2)/partial Y=48` there.  Moreover `C_0` misses both
the cusp `(0,0)` and the node `(1,0)` of `B`.  Both curves have polynomial
normalization `A1` and one place at infinity.

At `z_0`, `B` is transverse to both branches of the node of `C_0` (their
parametric tangent slopes are `17`, `1`, and `-1`).  Hence their completed
local curve pair is analytically the exact form `b=u+v`, `c_0=uv` used in
Section 6.

This is a global **curve-pair/resultant firewall only**.  It does not supply
the quartic cover, companion fibre cardinalities, `S_4` monodromy,
`Pic(U)=Z/mu`, a cyclic pseudo-cover, or a Keller map.  It proves that the
one-cusp/one-node topology and one-place property alone do not force the
new self-identification to occur at either special point.

## 8. Maximum-safe conclusion and minimum missing lemma

Promote, conditional on the inverse-Kummer producer, exactly the following.

> **Index-at-infinity negative gate.**  The divisor
> `u^mu-v^mu=0` is the index divisor of the monogenic quartic order and has
> even polynomial discriminant valuation while the normalized quartic cover
> remains etale.  Orevkov--Chau counts local multiplicities on actual source
> dicriticals.  At the immersed self-identification every deleted-line point
> has the generic local multiplicity one, and at an ordinary point of `B`
> the colliding companions are disjoint from the ramified boundary point.
> Hence the index divisor supplies no necessary positive term beyond the
> already charged base terms.  The norm/resultant identity permits an
> ordinary collision after a degree-dropping `b`-adic specialization.

Do not promote:

1. `Disc(P_t)` is the branch discriminant of `pi`;
2. every component or point of `J_t` is a dicritical component or critical
   boundary value of `H`;
3. projective intersection of `J_t` with infinity implies
   `mu_x>mu_l`;
4. the exponent `k` in (6.1) is zero, nonnegative, or determined by the
   `(2,1,1)/(3,1)/(2,2)` census;
5. clearing the quartic relation preserves degree on `b=0`;
6. a double resultant root makes `B` singular;
7. either countercontrol is a global charged cover or Keller map.

The exact missing lemma must have one of the following genuinely global
forms.

1. **Dicritical-index coupling.**  For this special cyclic pseudo-plane
   completion, prove that every off-diagonal component of `J_t` has closure
   through a point of an actual dicritical where the local degree jumps.
   Controls (5.1)--(5.5) show that no general local or order-theoretic version
   can hold.
2. **Based link-at-infinity coupling.**  Use the saturated two-component
   infinity link, not merely affine intersection, to force the coincidence
   curve to create a critical boundary parameter.  The required input is a
   relation among the links of `B`, `C_0`, and `J_t`.
3. **`b`-adic integral-generator coupling.**  Control the pole valuation of
   `t` and all coefficients of `P_t` at the rank-two boundary factor strongly
   enough that the quartic order stays flat after specialization.  Only then
   could the companion resultant be evaluated at the cusp/node packets.

For the strict-block horn, `d_1>=2` and the conditional minimal-degree
replacement gives `mu=d_1`.  The `d_1=1` pseudo-plane row remains empty from
`mu>=2` and `mu|d_1`; no statement is made about arbitrary canonical
rank-four configurations outside this row.

No replay is attached.  The countercontrols are exact symbolic identities
for all `mu,r>=1`; finite sampling would not verify the boundary implication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20478`.
- Body SHA-256:
  `f2906d4bf6493d8aca2e415c717225dd50eba8c2a44594feecaa2260befa1746`.
- Frozen basis: `b3d98d87e9bb9664da7b175b76204bb7eadf1e5d`.
