# Hostile review: singular F5 local polar and A6/A7 elimination

Date: 2026-08-30 UTC
Reviewer: GPT-5.5 xhigh, independent hostile audit
Charged basis: `2275c1f490517e844572f7b532bde36ecce8cc20`

## 0. Custody

The requested commit object exists.  The working tree HEAD during this audit was
`ed261f7ffb18daa2abb948429c2ebd4148a93622`, not the requested basis, but the
seven charged paths in the working tree and in
`2275c1f490517e844572f7b532bde36ecce8cc20` have exactly the requested
SHA-256 hashes.  I therefore audited the hash-pinned file contents, not the
current HEAD as an authority.

I did not inspect, list, search, stat, build, modify, or control `jc2-lean`.
No Singular or heavy local CAS was used.  The supplied Python replay was read
and run once; it is only an arithmetic check of the Cartan rows.

## 1. Local equation, singularity, and Morse reduction

Verdict: **CONFIRM_WITH_CORRECTIONS**.

The exact local equation is

```text
h=z(z-v)((1+v)z-v),
f=h+u(a(z)u+b(z)v+c(z)).
```

Expanding

```text
h=z^3+vz^3-2vz^2-v^2z^2+v^2z,
h_3=z(z-v)^2.
```

The origin is singular exactly when `c(0)=0`: at the origin,
`f_u=c(0)`, while `f_v=f_z=0`.  If `c(0)=0`, the quadratic tangent part is

```text
u(a(0)u+b(0)v+c'(0)z).
```

For the balanced rows, `b(0)!=0` is precisely the nondegenerate Hessian case in
the target variables:

```text
Hess_(u,v)(f)(0)= [[2a(0), b(0)], [b(0), 0]],
det=-b(0)^2.
```

Multiplying by a unit normalizes `b(0)=1`.  A constant target shear
`v -> v+lambda u` changes the `u^2` coefficient by a nonzero multiple of
`lambda`; because `h` is quadratic in `v`, this keeps the same target-degree-two
form, with changed one-variable coefficients.  Thus `a(0)=0` is a legitimate
normalization.

Solving the critical equations

```text
2a(z)u+b(z)v+c(z)=0,
h_v(v,z)+b(z)u=0
```

gives a unique analytic critical point `(u_0(z),v_0(z))`.  If
`v_0=tau z+O(z^2)`, then the critical value has cubic term

```text
phi(z)=h(v_0,z)+higher = (1-tau)^2 z^3+O(z^4).
```

Hence an `A_(s-1)` tag with `s>=5` forces `tau=1`.  Then
`h_v(z,z)=-z^3`, so `u_0=z^3+O(z^4)` up to the unit `b(z)^{-1}`;
in particular `ord(u_0)>=3`.

Because `f` is exactly quadratic in `(u,v)` for fixed `z`, the parametric Morse
change may be chosen linear in the centered variables.  With `X` the factor
near `v-v_0` and `Y` the complementary factor,

```text
f=XY+phi(z),
v=z+X+O(z^2,zX,zY),
u=u_0(z)-zX+Y+O(z^2X,zY).
```

The correction is interpretive: the displayed inverse-coordinate form is a
principal expansion after the Hessian factor choice.  It is not an arbitrary
target-coordinate change, and its omitted terms are controlled because the
original equation is quadratic in `(u,v)`.

## 2. Cartier different and Newton principal part

Verdict: **CONFIRM_WITH_CORRECTIONS**.

On `XY+phi(z)=0`, use

```text
omega=dX wedge dz / X.
```

Write the inverse Morse transformation in the exact linear form

```text
v=v_0(z)+alpha(z)X+beta(z)Y,
u=u_0(z)+gamma(z)X+delta(z)Y,
```

with

```text
alpha(0),delta(0) units,  beta=O(z),  gamma=-z+O(z^2),
v_0'=1+O(z),              u_0'=O(z^2).
```

On the chart `X!=0`, put `Y=-phi/X`.  If

```text
du wedge dv = r omega,
P=Xr,
```

then `P=X^2 det(partial(u,v)/partial(X,z))`.  Substituting the preceding
expansions gives the lower terms

```text
P = unit*X^3 - unit*zX^2 + unit*phi'(z)X + unit*phi(z) + higher.
```

More explicitly, the `X^3` coefficient is
`gamma alpha' - alpha gamma'`, a unit because `gamma'=-1+O(z)`;
the `zX^2` coefficient is `gamma v_0' - alpha u_0'=-z+O(z^2)`;
the `phi` coefficient is `delta v_0' - beta u_0'`, again a unit.  The
`phi'(z)X` coefficient has unit leading part `alpha delta`.

The correction is that "higher" must be read in the Newton/valuation sense
after using `XY=-phi`.  For a nontriangular Morse factorization some terms are
naturally written as `phi Y` or `phi^2/X` on the `X!=0` chart.  Their weights
are strictly above both lower edges:

```text
edge 1: (3,0)--(2,1),
edge 2: (2,1)--(0,s).
```

For edge 1 the weights are ordinary total degree, and every omitted term has
degree at least four.  For edge 2 use weights
`wt(z)=2`, `wt(X)=s-1`; `zX^2` and `phi` have weight `2s`, while
`phi'X`, `X^3`, and the possible `phi^2/X` terms have weights greater than
`2s` for `s>=5`.

No lower-edge coefficient can vanish while the named ADE tag persists:
the first edge has unit coefficients in `X^3` and `zX^2`, and the second edge
has unit coefficient in `zX^2` and nonzero leading coefficient of `phi`,
because `ord_z(phi)=s`.

The `X=0` factor is not a strict physical different component.  It appears in
`div(P)=div(X)+div(r)` because of the residue chart denominator.  The strict
different is read from `r=0`, equivalently from the nonvertical Newton factors
of `P` with `X!=0` generically.

## 3. Newton/Hensel factorization and A-degrees

Verdict: **CONFIRMED**.

The first lower edge has initial polynomial

```text
X^3-lambda zX^2 = X^2(X-lambda z),
lambda!=0.
```

The nonzero root is simple, hence gives one reduced smooth strict germ

```text
X=lambda z+O(z^2).
```

After removing that factor, the second edge is

```text
X^2=mu z^(s-1),  mu!=0.
```

If `s` is odd, `s-1` is even and Hensel gives two distinct factors in
`C[[z]]`, with

```text
X= +/- sqrt(mu) z^((s-1)/2)+higher.
```

If `s` is even, `s-1` is odd.  The Newton polynomial is squarefree after the
Puiseux substitution `z=t^2`, `X=t^(s-1)*unit`, but the factor is irreducible
over `C[[z]]`: a square root of `z^(s-1)` would have odd valuation.  Thus
there is one reduced irreducible Puiseux germ.

The total local length is exactly eight:

```text
length O_X/(u,r)=length C[[v,z]]/(h,h_z).
```

Along the three branches of `h` this is

```text
z=0:                         ord(h_z)=2,
z=v:                         ord(h_z)=3,
((1+v)z-v)=0, v=z/(1-z):     ord(h_z)=3,
```

so the sum is `2+3+3=8`.

For the first strict polar germ, the inverse coordinate formula gives
`u=-lambda z^2+O(z^3)`, hence exact local `A`-degree `2`.

For odd `s`, the two second-edge germs have `ord(u)>=3`.  For even `s`, the
single Puiseux germ has `z=t^2`, so `ord_t(u)>=6`.  Additivity against the
already exact length eight forces equality and excludes hidden strict polar
components or hidden higher Cartier coefficients:

```text
s odd:   8=2+3+3,
s even:  8=2+6.
```

The edge polynomials are squarefree in characteristic zero.  For even `s`,
the irreducible Puiseux factor has multiplicity one, not coefficient two.
Thus every strict prime has Cartier coefficient one.

## 4. Exceptional vector and attachment sites

Verdict: **CONFIRMED**.

For `A_(s-1)` in standard numbering,

```text
ord_Ei(X)=i,        ord_Ei(Y)=s-i,        ord_Ei(z)=1.
```

Since `r=P/X`, the displayed terms give

```text
ord_Ei(r)=min(2i, i+1, s-1, s-i)=min(i+1,s-i).
```

At the odd middle equality `i+1=s-i`, the initial forms of `zX` and `Y` on
`E_i` are not proportional: in a toric chart they are represented by
`w` and a nonzero multiple of `1/w`.  Therefore no identity-level cancellation
occurs on the exceptional component.

Applying the `A_(s-1)` Cartan matrix gives:

```text
B5/A4:  m=(2,3,2,1),             n=(1,2,0,0)
B6/A5:  m=(2,3,3,2,1),           n=(1,1,1,0,0)
B7/A6:  m=(2,3,4,3,2,1),         n=(1,0,2,0,0,0)
B8/A7:  m=(2,3,4,4,3,2,1),       n=(1,0,1,1,0,0,0)
B9/A8:  m=(2,3,4,5,4,3,2,1),     n=(1,0,0,2,0,0,0,0)
```

The special audited row is correct:

```text
B8/A7:
m=(2,3,4,4,3,2,1),
n=e1+e3+e4.
```

The physical sites follow from the usual `A`-chain resolution:

```text
X=unit*z^j, j integral       -> smooth point of E_j,
X=unit*z^(j+1/2)             -> node E_j cap E_(j+1).
```

Hence `B8/A7` has one strict germ at a smooth point of `E1` and one strict
Puiseux germ through `E3 cap E4`.

## 5. Globalization-cycle lemma

Verdict: **CONFIRM_WITH_CORRECTIONS**.

The lemma is correct, but the proof must be stated on a common embedded
resolution of the reduced full first-leg boundary.

Every `E_i` over the singular F5 point is a boundary component of the resolved
open because the singular point is removed with `Supp(H+R_X)`.  Equivalently,
`r^*H` has positive coefficient on every component of the connected
`A_(s-1)` chain: the attachment vector for `H` is nonzero and
`C_A^{-1}` has strictly positive entries.  The strict polar germs are local
branches of `Supp(R_X)`, so their global closures are also boundary components
of

```text
U=X minus Supp(H+R_X).
```

The rational-forest theorem applies only after resolving the reduced full
boundary to SNC.  In that graph, suppose one irreducible global ramification
prime `C` has two local branches at two distinct physical attachment sites.
Its proper transform is one connected vertex after normalization and embedded
resolution.  It has two distinct incidences with the exceptional tree:

```text
C -- site_1 -- unique exceptional path -- site_2 -- C.
```

If the two sites are distinct points on the same exceptional component, the
dual multigraph has two parallel edges from the `C` vertex to that exceptional
vertex, already a cycle.  If one site is an exceptional node, blowing up the
triple point only subdivides the node by a tree of new exceptional components;
the attachment point moves to this subdivision and remains distinct from the
other site.  Further embedded blowups subdivide edges and cannot remove the
first Betti class.

Thus two distinct physical attachment sites cannot belong to one global
irreducible prime under the charged rational-forest first-leg hypothesis.
This proves

```text
s odd:   k>=3,
s even:  k>=2
```

for the balanced `B_s/A_(s-1)`, `5<=s<=9`, local rows.  The argument does not
say that arbitrary distinct analytic germs always globalize to distinct
primes; it uses distinct physical boundary sites in the full resolved boundary.

## 6. Euler cap consequences

Verdict: **CONFIRMED**.

The charged A1-ruling integration gives, in the reduced F5 scope,

```text
rho+k<=8,
rho=(s-1)+r_aff
```

for `B_s/A_(s-1)`.

Combining with the local lower bounds for `k`:

```text
B5/A4:  rho=4+r_aff, k>=3 -> r_aff+k<=4 and r_aff<=1.
B6/A5:  rho=5+r_aff, k>=2 -> r_aff+k<=3.
B7/A6:  rho=6+r_aff, k>=3 -> rho+k>=9, impossible.
B8/A7:  rho=7+r_aff, k>=2 -> rho+k>=9, impossible.
B9/A8:  rho=8+r_aff, k>=3 -> rho+k>=11, impossible.
```

Thus `B_7/A_6`, `B_8/A_7`, and `B_9/A_8` are eliminated as necessary states in
the charged first-leg scope.  `B_9/A_8` was already dead from `rho>=8,k>=1`.
The new eliminations are `B_7/A_6` and `B_8/A_7`.

The surviving `B_5/A_4` and `B_6/A_5` rows are not effective states.  They are
only necessary local tags satisfying the sharpened residual budgets above.

## 7. The `B3/A2` modulus

Verdict: **CONFIRM_WITH_CORRECTIONS**.

For `B_3/A_2`, write

```text
v_0=tau z+O(z^2),       sigma=1-tau,       sigma!=0.
```

Here

```text
phi=sigma^2 z^3+O(z^4).
```

The same Jacobian calculation, now retaining `u_0=2sigma z^2+O(z^3)` and
`v_0'=tau+O(z)`, gives the degree-three homogeneous polynomial in `T=X/z`:

```text
T^3-(1+3sigma)T^2+3sigma^2T+tau sigma^2
 =(T-sigma)(T^2-(1+2sigma)T+sigma(sigma-1)).
```

The root `T=sigma` is distinct from every quadratic root because `sigma!=0`.
It is the branch for which the order-two term of `u` cancels:

```text
u/z^2 = 2sigma - T - sigma^2/T,
```

and this vanishes exactly at `T=sigma`.

If `tau!=0` and

```text
Delta=1+8sigma=9-8tau !=0,
```

then all three roots are nonzero and distinct.  The two quadratic-root branches
have exact `A`-degree `2`, while the `T=sigma` branch has exact degree `4` by
the total length eight.  The generic partition is therefore

```text
4+2+2.
```

If `Delta=0`, the quadratic block is tangent at a second physical point of
`E1`.  Its total `A`-degree is `4`; higher coefficients decide whether it is
one irreducible branch or two tangent branches.  A nonreduced divisorial prime
is incompatible with the charged coefficient-one fixed-sheet theorem, but this
does not force two distinct physical sites inside the quadratic block.

For `tau!=0`, the exceptional vector is

```text
m=(2,1),       C_A2 m=(3,0)=3e1.
```

If `tau=0`, the cubic has roots `T=1,3,0`.  The two nonzero roots give two
distinct smooth `E1` sites.  The `T=0` residual block is centered at the
opposite endpoint, and its splitting and Cartier multiplicity are
higher-coefficient dependent.  Thus the universal conclusion is only
`k>=2`; in the generic `tau!=0, Delta!=0` subcell one has `k>=3`.

The correction is important: there is no coefficient-independent singular
`3+5` partition for `B_3/A_2`.

## 8. Generic-DVR contracted-carrier decision tree

Verdict: **CONFIRM_WITH_CORRECTIONS**.

At the generic point of an affine contracted carrier `Z={q} times P1`, choose
target parameters `(s,t)` at `q`.  After possibly replacing `(s,t)` by a
constant linear pair, assume the linear coefficient `P` of `s` is nonzero at
the generic point.  Over `K=C(Z)`, divide by `P` and write

```text
F=s+tQ+s^2A+stB+t^2C.
```

Implicitly solving for `s` gives

```text
s=a_1t+a_2t^2+a_3t^3+...
```

and the map `(t,z)->(s,t)` has Jacobian `partial s/partial z`.  In
characteristic zero,

```text
nu_Z=min{j>=1 : a_j is nonconstant in K}.
```

The recurrence is exact.

1. `a_1=-Q`.  If `Q` is nonconstant, `nu=1`.
2. If `Q` is constant, the constant shear `s -> s+Qt` sets `Q=0`; writing
   `s=t^2w` gives `w+At^2w^2+Btw+C=0`, so `a_2=-C`.  If `C` is nonconstant,
   `nu=2`.
3. If `C=c` is constant, then `c!=0`; otherwise `F=s(1+As+Bt)` and the local
   component maps into a target curve, contradicting generic finiteness.  With
   `c!=0`, the coefficient of `t` in `w` is `cB`, so nonconstant `B` gives
   `nu=3`.
4. If `B=b` is also constant, the coefficient of `t^2` in `w` is
   `-cb^2-c^2A`, a nonzero affine function of `A`; nonconstant `A` gives
   `nu=4`.
5. If `A,B,C` are all constant after the preceding normalizations, the local
   equation is independent of the source coordinate up to a unit factor, so the
   map has rank at most one near the carrier.  This contradicts generic
   finiteness.

Therefore the sharp generic range is

```text
1<=nu_Z<=4.
```

The correction is scope: this is the generic Cartier multiplicity of a
particular effective contracted carrier.  It does not prove such carriers
exist, does not prove smoothness away from their generic point, and does not
turn the global class equations into an effectivity theorem.

If `nu_Z>1`, then the first-jet pencil `[P:Q]` is constant.  Globally along the
source line, `P` and `Q` are proportional cubic sections; since they are not
both zero, their common zero scheme has length three on `Z`.  At those points
`F_s=P=0`, `F_t=Q=0`, and `F_z=0` because `s=t=0`, so the hypersurface has a
length-three singular subscheme on `Z`.  This proves a singular-scheme
statement only; it does not by itself give an ADE-rank lower bound, a fixed
local type, or a contradiction.

## 9. Scope firewall

Verdict: **CONFIRMED**.

The firewall is necessary and should be kept verbatim in downstream use:

```text
local analytic germs != formal lattice entries,
exceptional coefficients != strict physical branches,
physical attachment sites != global primes without the forest argument,
Cartier multiplicity != reduced-prime count,
necessary marked tags != effective incidence states,
incidence states != polynomial Keller maps or JC2 conclusions.
```

The unbalanced `U_3`, `U_5`, and `U_6` rows remain provisional.  The balanced
proof above does not transfer to them by analogy because their Hessian rank and
square-completion units change the polar Newton data.

## 10. Maximum safe theorem

Verdict: **CONFIRM_WITH_CORRECTIONS**.

The maximum safe theorem after this hostile review is:

In the charged normal, reduced, finite-near-infinity singular F5 first-leg
scope, for every balanced local tag

```text
B_s/A_(s-1), 5<=s<=9,
```

the strict local source different at the singular F5 point has Cartier
coefficient one on each strict prime and has exact local `A`-degree partition

```text
s odd:   2+3+3 with three reduced strict germs,
s even:  2+6   with two reduced strict germs.
```

The degree-two germ attaches at a smooth point of `E1`.  The odd high-contact
germs attach at two distinct smooth points of `E_((s-1)/2)`.  The even
high-contact germ attaches at the node
`E_((s-2)/2) cap E_(s/2)`.  The exceptional different vector is

```text
m_i=min(i+1,s-i),
Cm = e1+2e_((s-1)/2)              for odd s,
Cm = e1+e_((s-2)/2)+e_(s/2)       for even s.
```

On the charged resolved full first-leg boundary, distinct physical attachment
sites force distinct global reduced ramification primes by the rational-forest
cycle argument.  Therefore

```text
s odd:   k>=3,
s even:  k>=2.
```

Together with the charged `rho+k<=8` Euler cap, this eliminates the necessary
balanced singular F5 rows

```text
B_7/A_6, B_8/A_7, B_9/A_8.
```

The surviving balanced rows are sharpened only to

```text
B_5/A_4: r_aff+k<=4, k>=3, hence r_aff<=1,
B_6/A_5: r_aff+k<=3, k>=2.
```

For `B_3/A_2`, the universal safe statement is modulus-dependent: generic
`tau!=0, Delta!=0` gives `4+2+2` and `k>=3`, while all coefficient-independent
claims reduce to at least two physical/global primes and no universal `3+5`
partition.

For an effective affine contracted carrier, the generic Cartier multiplicity is
exactly determined by the first nonconstant coefficient in the four-stage DVR
expansion and satisfies `1<=nu_Z<=4`; if `nu_Z>1`, the first jet is rank one
and there is a length-three singular subscheme on the carrier.  No unbalanced
row, effectivity assertion, polynomial-map conclusion, or JC2 conclusion is
promoted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17619`.
- Body SHA-256:
  `95f767dcf5bf9c9a45f2da09a16e1744bd4cc49c14dc9c5fb1e1a607e449fb60`.
- Frozen basis: `2275c1f490517e844572f7b532bde36ecce8cc20`.
