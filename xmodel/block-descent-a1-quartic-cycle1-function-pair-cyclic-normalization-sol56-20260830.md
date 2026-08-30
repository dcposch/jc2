# Rank-four `R4-CYCLE-1-FUNCTION-PAIR`: cyclic normalization and the second asymptotic curve

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_cycle1_function_pair` lane)  
Frozen basis: `06a4110854d7ad38525daccfa7895943259a3812`  
Lifecycle: **FINAL+VERIFIED EXACT SUCCESSOR / NEW SAME-FIBRE COLLISION / HORN OPEN**

## 0. Verdict

Charge the `R4-CYCLE-1` pseudo-plane funnel with unique multiple ruling fibre
`mu*Phi`, `mu>=2`.  The arbitrary first leg can be replaced, without
increasing degree, by Miyanishi's canonical cyclic pseudo-cover.  This turns
the proposed function pair into a literal coordinate-power pair:

```text
A2_(x,y) --f_mu--> U --pi--> A2,
H=pi o f_mu,                    deg(H)=4mu,
rho o f_mu=a+c*x^mu,            q=b o H,
H(A2)=A2-{n}.                                           (0.1)
```

Here `x` is a polynomial coordinate, `b=0` is the target branch `B`, and
`n` is its omitted `(2,2)` value.  Thus `H` is itself a noninvertible plane
Keller map.  If the charged strict-block counterexample was chosen with
minimal geometric degree, then the earlier divisibility `mu|d1` improves to

```text
mu=d1.                                                   (0.2)
```

The `d1=1` specialization of this **exact pseudo-plane row** is empty:
`d1=1` is incompatible with `mu>=2` and `mu|d1`.  This does not exclude an
arbitrary canonical rank-four normalization outside the charged row, and
nothing in (0.2) licenses setting `d1=1` in the strict-block horn.

The Orevkov--Chau degree budget first forces the connected target branch
`B` to be irreducible.  The cyclic normalization then forces a second
nonproper-value curve

```text
C0=H({x=0})=pi(Phi).                                    (0.3)
```

It is distinct from `B`, because it is closed and misses `n`.  Chau's
Theorem 4.4 forces every nonproper-value component of a noninvertible Keller
map to be singular.  On the other hand `H|_{x=0}` is everywhere immersive
and is the normalization map of `C0`.  Consequently the required singularity
is a multibranch self-identification:

```text
there exist p!=p' in Phi with pi(p)=pi(p').              (0.4)
```

It is neither the charged cusp `c` nor the omitted node `n`.  This is a new
same-ruling-fibre collision, but it is **not** a second reducible or multiple
fibre of `rho`.

The actual second polynomial gives an exact Euler/orbit identity.  Put

```text
T=U times_(A2) B,          A=T intersect Phi,
N=#A,                      D=V(q)=f_mu^(-1)(T).
```

Then `A` is finite and

```text
e(D)=-3mu-(mu-1)N,              D intersect {x=0}=A.     (0.5)
```

If `nu` is the generic number of points of a vertical fibre of `D`, and one
representative is chosen from every nonzero `mu`-th-root orbit of exceptional
`x`-values, then

```text
sum_representatives (nu-#D_x)=N+3.                       (0.6)
```

Thus a nonzero exceptional companion-incidence value is forced, but all
scheme fibres of the ambient `x`-ruling can remain affine lines.  A uniform
polynomial family in Section 6 realizes (0.5)--(0.6), one cusp orbit, no node,
and no bad ruling fibre.  It blocks a purely polynomial-fibre contradiction.

Indeed, if `r` is the number of irreducible components of `B`, the boundary
over them consumes at least `2mu*r+mu` units (generic length `2mu` on each
component plus the unique cusp increment `mu`), while the `mu-1` deleted
cyclic fibre lines consume at least `mu-1`.  The Orevkov--Chau degree-at-
infinity formula gives

```text
4mu-1 >= 2mu*r+2mu-1.                                   (0.7)
```

Thus `r=1`, and equality holds throughout.  The budget is saturated, not
violated.  The node is budget-free because it is a two-point normalization
identification; the forced singularity of `C0` is budget-free for the same
reason.  Hence the function pair gives a sharp new normalization, target-
irreducibility, and collision theorem, not yet an exclusion of
`R4-CYCLE-1`.

## 1. Frozen inputs and exact scope

```text
7d40e7ee6d5970c51d62f73bafaf11670cb32c06bd51859876ab526f0fdf8bab
  xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-threat-map-sol56-20260830.md
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7
  refs/chau1999_apm71_full.pdf
```

The charged producer supplies

```text
A2 --g1--> U subset Y --pi--> A2,
deg(pi)=4,                   deg(g1)=d1,
rho:U->A1,                  rho^(-1)(a)=mu*Phi,
Pic(U)=Z/mu,                K_U~0,
e(U)=1,                     e(T)=-3,
pi(U)=A2-{n},               mu|d1.                       (1.1)
```

Every reduced ruling fibre is one `A1`; `Phi` itself is `A1`.  The branch is
connected but is **not initially assumed irreducible**.  Put
`r=#Irr(B)>=1`.  Every irreducible component is generically `(2,1,1)`; the
whole connected curve has one `(3,1)` cusp value `c`, one `(2,2)` two-point
value `n`, and `beta1(B)=1`.  The companion fibre cardinalities are `2,1,0`
respectively.  Section 4 will derive `r=1`; no use before that point may
silently assume it.

The cyclic pseudo-cover theorem used below is Miyanishi Lemma 2.5.2, already
source-checked and different-model-reviewed in the cubic funnel.  Chau's
primary Theorem 4.4 and the Orevkov degree formula quoted in Remark 4.9 are
read directly from *Non-zero constant Jacobian polynomial maps of C2*,
Ann. Polon. Math. 71 (1999), 287--310, DOI
`10.4064/ap-71-3-287-310`.  No classification of arbitrary pseudo-planes,
no typed `(d,n,r)` canonical formula, and no unreviewed Jacobian claim is
imported.

## 2. Canonical cyclic replacement of the first leg

Apply Miyanishi Lemma 2.5.2 to `(U,rho)`.  Base-change the ruling by the
degree-`mu` cyclic map

```text
x |-> a+c*x^mu
```

and normalize.  This gives a finite etale cyclic cover

```text
f_tilde:U_tilde->U,             deg(f_tilde)=mu.         (2.1)
```

The inverse image of `Phi` is a disjoint union of `mu` affine lines

```text
L_0 disjoint_union ... disjoint_union L_(mu-1).
```

Each `L_j->Phi` has degree one: their degrees sum to `mu`, the cyclic group
acts transitively, and a connected finite etale cover of `A1` is trivial.
Delete `L_1,...,L_(mu-1)`.  Miyanishi's lemma identifies the resulting open
with `A2` and makes the restriction

```text
f_mu:A2->U
```

surjective, etale, and of generic degree `mu`.

The base-change coordinate `x` restricts to a polynomial on this `A2`.
For `x!=0` its fibre is the base change of an ordinary ruling fibre; for
`x=0` it is the retained line `L_0`.  All scheme fibres are reduced `A1`s.
Equivalently this is a smooth `A1`-bundle over `A1`, hence trivial.  After an
affine change of source and base coordinates, `x` is a coordinate and

```text
rho o f_mu=a+c*x^mu.                                    (2.2)
```

Now put `H=pi o f_mu`.  It is a morphism `A2->A2`, hence a polynomial pair.
Both factors are etale on their displayed domains, so `det JH` is a nowhere-
zero polynomial and therefore a nonzero constant.  The field tower and
surjectivity give

```text
deg_geo(H)=4mu,                 H(A2)=pi(U)=A2-{n}.      (2.3)
```

Thus the conditional rank-four survivor canonically manufactures another
Keller counterexample of degree `4mu`.

For the original first leg, `mu|d1` and `mu>=2`.  If the original map has
minimal geometric degree among all plane Keller counterexamples, (2.3)
cannot have smaller degree than `4d1`.  Hence `mu>=d1`; divisibility gives
`mu=d1`, proving (0.2).  This is a minimal-counterexample reduction, not an
identity for an arbitrary nonminimal factorization.

If a canonical-normalization first leg `d1=1` satisfied this same pseudo-plane
package, (1.1) would say `mu|1`, immediately contradicting `mu>=2`.  The
cyclic replacement is needed only in the strict-block case `d1>=2`; no claim
is made about canonical rank-four configurations outside this package.

## 3. The deleted fibre forces a second singular asymptotic curve

Let `Ubar` be the normalization of `Y` in `C(U_tilde)`.  Excellence makes
`Ubar->Y` finite of degree `mu`; over `U` it restricts to (2.1).  The open
source `A2` has boundary in `Ubar` consisting exactly of

```text
the inverse image of R=Y-U,       and       L_1,...,L_(mu-1). (3.1)
```

The finite extension of `H` maps the first part to `B` and every deleted
line to

```text
C0=pi(Phi)=H(L_0).                                      (3.2)
```

Therefore the nonproper-value set of `H` is exactly `B union C0` set-
theoretically.  At this stage `C0` could still coincide with one irreducible
component of a reducible `B`; this possibility is not discarded by notation.

The map `H|L_0:A1->A2` is polynomial and nonconstant.  Any polynomial map
from `A1` to an affine curve is finite onto its image: a nonconstant
coordinate polynomial makes `C[t]` integral over the image ring.  Hence
`C0` is closed.  Since `L_0 subset A2` and `H(A2)=A2-{n}`, one has
`n notin C0`.  But `n in B`, so `C0` is not the whole connected curve `B`.
After Section 4 proves `B` irreducible, this sharpens to

```text
C0!=B.                                                   (3.3)
```

The full map `pi o f_tilde` is etale along every `L_j`; in particular every
restriction `L_j->C0` is everywhere immersive.  Also each deleted line is a
dicritical boundary line for `H`.  Chau Theorem 4.4 applies to its polynomial
image even if another dicritical has the same image: `C0` must be singular.
The exact degree and type of that singularity will follow from saturation in
Section 4.

## 4. Orevkov--Chau degree budget: irreducibility and saturation

Apply the degree-at-infinity formula quoted by Chau in Remark 4.9 to the
Keller map `H`.  On a regular extension it has the form

```text
deg(H)-1 = sum_L [m_L + sum_p(deg_p(Hbar)-m_L)],         (4.1)
```

where `L` runs over dicritical boundary lines, `m_L` is the generic local
degree, and every displayed correction is nonnegative.  Blowing up the
finite normalization in Section 3 only refines these contributions.

For clarity, a standard normalization fact translates generic missing rank
into a lower bound in (4.1).  If a dicritical line maps with degree `s` to
the normalization of its image curve and has generic transverse degree `m`,
then its bracket is at least `ms`: the finite ramification of the polynomial
map `A1->A1` contributes `m(s-1)` in addition to the initial `m`.  Summing
over all lines above one image component is therefore at least the generic
missing multiplicity along that component.  Self-identifying two distinct
normalization points creates no derivative correction.

Let `r=#Irr(B)`.  At a generic `(2,1,1)` value of every component, the
missing ramified rank of `pi` is two.  After the cyclic degree-`mu` cover,
the generic multiplicity of the part of (3.1) lying over `R` is `2mu` on
each component.  Equivalently, at its generic DVR the valuation identity
`sum_j e_j f_j=mu` for `Ubar->Y`, multiplied by the rank-two local factor of
`pi`, gives `sum_j 2e_j f_j=2mu`.  Thus these ramification-boundary curves
contribute at least `2mu*r`.

At the unique `(3,1)` cusp the missing local rank is three rather than two.
The cusp is unibranch, so this increase cannot be supplied by a second
normalization preimage (unlike the node).  After the cyclic cover it therefore
supplies an additional `mu` in the local-degree corrections; any nonflat
specialization in the finite normalization only increases it.  Consequently
the total ramification-boundary collection over `B` contributes at least

```text
2mu*r+mu.                                               (4.2)
```

The `(2,2)` node does not force another correction: it has two normalization
preimages, each carrying the generic rank-two packet.  This is the same
reason a nodal self-identification is invisible to the derivative of its
normalization parametrization.

Next consider `C0`.  There are exactly `mu-1` deleted lines.  Along each,
the extended map is etale and its image is nonconstant.  Each bracket is at
least one, even if `C0` initially coincides with a component of `B`.  Their
total is at least

```text
mu-1.                                                    (4.3)
```

Equations (4.2)--(4.3) and `deg(H)=4mu` give

```text
4mu-1 >= (2mu*r+mu)+(mu-1)=2mu*r+2mu-1.
```

Since `r>=1`, this forces

```text
r=1,                                                     (4.4)
```

and every inequality is an equality.  This is the promised proof that the
connected target branch is irreducible.  Now `n notin C0` proves
`C0!=B`, so `C0` is a genuine second irreducible component of the nonproper-
value set.

Equality in (4.3) also says that every deleted line contributes exactly one.
Factor `L_j=A1->C0` through the normalization.  That normalization is `A1`:
it is a normal rational affine curve admitting a finite surjection from
`A1`, and it cannot have a puncture because a nonconstant unit would pull
back to a nonconstant unit of `C[t]`.  Contribution one forces the finite
lift `A1->A1` to have degree one.  Since the ambient map is etale along
`L_j`, the normalization parametrization is immersive.  Hence

```text
L_j=A1 -> C0 is the immersive normalization map.        (4.5)
```

Chau Theorem 4.4 forces `C0` to be singular.  Equation (4.5) excludes a cusp
or any other unibranch critical parametrization, so its singularity identifies
at least two distinct normalization points.  Transport through
`L_0 isomorphic to Phi` proves

```text
there exist p!=p' in Phi with pi(p)=pi(p').              (4.6)
```

The collision value cannot be `n`, which has no point in `U`, or `c`, whose
companion fibre in `U` has only one point.  It lies either outside `B`, where
two of the four etale points of a `pi`-fibre lie on `Phi`, or at an ordinary
`(2,1,1)` value of `B`, where both companions lie on `Phi`.  The data do not
choose between these alternatives.  The collision gives `C0` an incidence
cycle but does not add to the ruling defect `Q`.

Finally, equality leaves no spare degree-at-infinity budget for another
unibranch/critical boundary event.  The cusp consumes the sole positive jump
over `B`; the node consumes none; and the singularity of `C0` is the
budget-free immersive self-identification in (4.6).  This is a consistency
theorem, not an exclusion.

It also identifies a precise possible closing move.  Any independent theorem
forcing a critical parametrization on `C0`, an additional positive local-
degree jump above `B`, or a third dicritical contribution would make (4.1)
strict and close the horn.  Mere self-intersection or extra tangency between
distinct immersed branches does not.

## 5. Exact Euler and orbit ledger for `q=b o H`

Let

```text
D=V(q)=f_mu^(-1)(T),       q=b o H.
```

Because `H` is etale and `b` is reduced, `D` is reduced.  Sections 3--4 give
`C0!=B`, so `Phi` is not a component of `T`; set

```text
A=T intersect Phi,            N=#A<infinity.             (5.1)
```

The full finite-etale pullback `T_tilde=f_tilde^(-1)(T)` has

```text
e(T_tilde)=mu*e(T)=-3mu.
```

Every deleted `L_j` meets `T_tilde` in the copy of `A` lying over `Phi`.
Deleting `mu-1` disjoint copies gives

```text
e(D)=-3mu-(mu-1)N,             D intersect L_0=A,        (5.2)
```

which is (0.5).  In particular

```text
e(D)=N mod mu.                                           (5.3)
```

No component of `T` can be a ruling fibre.  If an `A1` ruling fibre were a
component, its polynomial image under the finite `pi` would be a closed
irreducible curve dense in the now irreducible `B`, hence all of `B`.  It
would have to contain `n`, contradicting `n notin pi(U)`.  Thus the
projection

```text
x:D->A1
```

has finite fibres.  Let `nu` be its generic cardinality.  Every special
cardinality is at most `nu`: the finite Zariski-Main completion of each curve
component is torsion-free, hence flat over the smooth affine line, while `D`
is obtained by deleting points.  Away from `x=0`, all cyclic opens coincide
and the deck group sends `x` to `zeta*x`; it preserves `D`.  Hence the
nonzero exceptional values occur in free orbits of size `mu`, with a constant
defect on each orbit.

Constructible Euler integration for a quasi-finite curve map gives

```text
e(D)=nu-sum_s(nu-#D_s).
```

The zero-fibre defect is `nu-N`.  Choose one representative from each
nonzero exceptional orbit and call the sum of its defects `Delta`.  Combining
with (5.2),

```text
-3mu-(mu-1)N = nu-(nu-N)-mu*Delta,
Delta=N+3.                                               (5.4)
```

This proves (0.6).  It also shows exactly why the tempting conclusion
`mu|e(D)` is false: the `mu-1` deleted copies of `A` contribute the residue
`N`.  The only valid divisibility statement is (5.3).

There is an exact cusp dichotomy.  Let `u_c` be the unique point of `T` over
the `(3,1)` cusp value.

```text
u_c notin Phi:   D has mu cusp points in one nonzero deck orbit;
u_c in Phi:      D has one retained cusp at x=0 and mu-1 deleted ones.
```

The node `n` has no point of `D` in either case.  Formula (5.4) forces at
least one nonzero exceptional companion-incidence orbit, but this may be a
tangency, a collision, or a loss at infinity of `T->A1`.  It says nothing
about reducibility or multiplicity of the ambient ruling fibre, all of which
remain reduced affine lines.

The `Pic` and canonical data are fully consumed but add no hidden numerical
term.  The exact order `mu` of `[Phi]` is what selects the cyclic cover and,
for the original leg, proves `mu|d1`.  Also

```text
f_mu^*K_U=K_A2~0.
```

Since `T` is principal, adjunction gives `omega_T~O_T`.  This agrees exactly
with etale pullback from the plane hypersurface `B`, whose dualizing sheaf is
also trivial.  Thus a Riemann--Hurwitz or canonical-class correction cannot
be inserted into (5.4), and `K_U~0` alone imposes no congruence on `N`.

## 6. Sharp polynomial-fibre firewall

The Euler mechanism in Section 5 has a uniform exact control.  Put

```text
G(t)=(t-1)^3(t-2)(t-3)(t-4)(t-5),
Q(t,y)=y^2-G(t),
q_mu(x,y)=Q(x^mu,y).                                    (6.1)
```

The curve `Q=0` has one ordinary cusp at `(1,0)` and no node.  Its
normalization is

```text
z^2=(t-1)(t-2)(t-3)(t-4)(t-5),        z=y/(t-1),
```

a genus-two projective hyperelliptic curve with one point removed.  The cusp
normalization is point-bijective, so

```text
e(Q=0)=2-2*2-1=-3.                                      (6.2)
```

At `t=0` the curve has two points, so `N=2`.  The pullback `q_mu=0` has
exactly `mu` ordinary cusps, one over each root of `x^mu=1`, and no nodes.
Projection to `x` has generic cardinality two and exactly `5mu` deficient
fibres, one over every root of `x^mu in {1,2,3,4,5}`.  Hence

```text
e(q_mu=0)=2-5mu
             =-3mu-(mu-1)*2,
sum_nonzero_orbit_reps(2-#fibre)=5=N+3.                 (6.3)
```

Meanwhile every fibre of the ambient coordinate ruling `x:A2->A1` is a
reduced irreducible `A1`.  Thus a coordinate power, base Euler number `-3`,
one cusp orbit, absence of a source node, and the exact divisibility/orbit
ledger do not force a second bad ruling fibre.

This family is deliberately only a **polynomial-fibre firewall**.  It does
not realize a Keller pair `H`, a quartic finite-flat algebra, the target node
with companion counts `2/1/0`, the pseudo-plane `Pic` and canonical package,
or a counterexample to JC2.  It blocks only arguments that forget those
additional structures.

## 7. Maximum-safe conclusion and next gate

Promote exactly the following conditional statement.

> **`R4-CYCLE-1-FUNCTION-PAIR` cyclic normalization.**  Every strict-block
> survivor in the charged one-cusp rank-four row canonically produces a
> degree-`4mu` plane Keller counterexample `H=pi o f_mu` with image
> `A2-{n}` and coordinate-power first function `rho o f_mu=a+c*x^mu`.
> A minimal-degree survivor has `mu=d1`.  The Orevkov--Chau budget forces
> `B` irreducible.  The nonproper-value set then has a second component
> `C0=pi(Phi)!=B`; `C0` is normalized immersively by the retained line and
> must have a multibranch self-identification.  For `q=b o H`, equations
> (5.2)--(5.4) give the exact Euler and cyclic-orbit deficit.  The infinity
> budget is saturated by `B` and the `mu-1` deleted lines.

Do not promote an exclusion of `R4-CYCLE-1`, a second bad ruling fibre,
`mu|3`, `N=0`, `C0 intersect B!=empty`, finiteness of either pseudo-cover,
or any claim that the node/cusp determines the gluing of the companion
divisor.

The cheapest successor is now narrower than the original function-pair
brief:

1. determine whether the quartic algebra or `K_U=0` forces the immersed
   self-collision of `C0` to lie on `B`; if so both generic companions lie on
   the single fibre `Phi`, an exact divisor-intersection configuration;
2. calculate the based infinity relation for the two components `B` and
   `C0`, using the saturated budget to reject any forced critical jump;
3. use the exact finite number `N=#(T intersect Phi)` and cusp alternative in
   (5.4), rather than the false divisibility `mu|e(T)`.

No replay is attached: the new claims are theorem-level normalization,
Euler additivity, and symbolic all-`mu` identities.  Section 6 is proved
uniformly by its displayed normalization and fibre count; sampling finitely
many `mu` values would not strengthen it.

Nothing here treats `R4-CYCLE-0`, disconnected branch, second-leg degree at
least five, the primitive/no-block horn, constructs an unconditional Keller
counterexample, or proves/disproves JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21468`.
- Body SHA-256:
  `ca809efbfbf2e613e74254d27a2b37fc4cef44610569a03cf7aa69da11b9b78d`.
- Frozen basis: `06a4110854d7ad38525daccfa7895943259a3812`.
