# Q6 local contact audit: full `B3/A2` modulus and `U3/A3`

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra sublane `/root/u_rows_full_family`  
Frozen basis: `54df5b64b5ea8355cd8c13aa790dcf0f703c5bb7`  
Lifecycle: **EXACT PRODUCER AUDIT / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

On the exact completed incidence

```text
h=z(z-v)((1+v)z-v),
f=h+u(a(z)u+b(z)v+c(z)),                 c(0)=0,
p=f_z|_(u,v fixed),
```

the proposed q=6 local input is correct for `U3/A3` and for the
coefficient-controlled part of `B3/A2`, but it is not uniform across the
balanced modulus.

1. `U3/A3` has two reduced coefficient-one strict polar germs of
   `A`-degrees `4+4`, exceptional vector
   `m=(2,2,1)`, and contact vector `n=2e1+e2`.  Their sites are the smooth
   `S,T` point on `E1` and the node `E1 cap E2`.
2. Normalize `B3/A2` by `b(0)=1,a(0)=0`, and write
   `c(z)=-tau*z+c2*z^2+...`.  The tag is exactly `tau!=1`.
   For `tau!=0`, `m=(2,1)` and `n=3e1`.  If
   `Delta=9-8tau!=0`, the strict partition is `4+2+2`, with three
   coefficient-one germs at distinct smooth points of `E1`.  At
   `Delta=0`, the degree-four quadratic block can split, remain irreducible,
   or become a doubled Cartier prime, according to its exact analytic
   Weierstrass discriminant.
3. For `tau=0`, the ordinary blowup calculation instead forces

   ```text
   m=(2,2),                 n=(2,2).                  (0.1)
   ```

   There are two fixed coefficient-one germs of degrees `4` and `2` on
   `E1`.  A residual Cartier block of total `A`-degree two lies on `E2`.
   Its first site polynomial is the projective quadratic

   ```text
   a1*X^2+2*c2*X*W+3*W^2,       a(z)=a1*z+... .      (0.2)
   ```

   Distinct roots give two coefficient-one degree-one germs.  At a double
   root the exact analytic discriminant decides between two degree-one
   germs, one degree-two irreducible germ, and one degree-one prime with
   Cartier coefficient two.  The simple family `f=h+uv` realizes the last
   case: its vertical prime `{v=z=0}` has coefficient two.
4. Consequently the advertised global strict total

   ```text
   c=(0,1,1,2,2,2,2,2,2)                            (0.3)
   ```

   is correct for `U3` and `B3,tau!=0`, but false for `B3,tau=0`.  In the
   standard chronological `B3` marking the corrected vector is

   ```text
   c_tau0=(0,2,0,2,2,2,2,2,2),                      (0.4)
   ```

   up to exchanging the two named outside coordinates together with the
   chronology.  A q=6 contracted carrier can be subtracted once from (0.3),
   but none can be subtracted from (0.4) without a negative centre
   multiplicity.
5. A positive intersection of strict global primes is a forest
   contradiction only after subtracting the intersection already consumed
   by their common local embedded-resolution centres.  For germs at distinct
   sites on the minimal ADE resolution that correction is zero.  For two
   branches born from one double polar site it can be positive and arbitrarily
   deep; raw positivity then need not be a second path.

These are statements about the source Cartier different on a necessary local
incidence configuration.  They do not prove effectivity, occurrence, a
finite cubic algebra, a polynomial map, or JC2.

## 1. Custody, inputs, and object types

I first read the frozen `COORDINATION.md` and `AUDIT.md`.  Their SHA-256
hashes are respectively

```text
1c0c20fa4798f429cf00325fd19aa8605f0050a32f28e2885dedfb14a03510cc
ab1865c8b4b1022ec3dfb206ada07d2b698bb4a713437aa5e1d6a6e0420398e1.
```

The exact charged mathematical sources, all recomputed from the frozen
commit, are

```text
413489b037be9533337f53e6bd104549c2ef663c4afd27927230d469ac1b1128
  xmodel/bd-a2-normal-singular-reduced-finite-f5-bridge-sol56-20260830.md
a5bf78c8ab8704884e9bb3c084c88059e01ec7690c1d6f645a9e87a0aa70a884
  xmodel/bd-a2-normal-f5-decorated-carrier-effectivity-reduction-coordinator-integration-sol56-20260830.md
fdf8f476acc86e2c07fbc472771ee49358d02c87d2667f15e6b762800eed7bc6
  xmodel/bd-a2-singular-f5-local-polar-and-a6-a7-elimination-coordinator-integration-sol56-20260830.md
6a7dc7bec108d867fe9215a85fdc09c2d2790db73d36c4123e96f7419f9511f3
  xmodel/bd-a2-singular-f5-unbalanced-local-polar-sol56-20260830.md
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md.
```

The unbalanced packet is used as a charged formula source, not as authority
for its conclusion: the U3 charts below were recomputed.  No sibling q6
report or provisional q6 elimination conclusion was assumed.  No **active**
external log/report, excluded formalization, web source, or heavy CAS was
read or run.

The following distinctions are load-bearing.

- A **formal vector** `m` is the valuation of the Cartier function `p` on
  ADE exceptional components; `n=Cm` is its formal strict-contact vector.
- A **configuration** is a marked numerical fibre/root class in the
  nine-blowup `F2` lattice.  It is not an effective blowup history.
- A **physical site** is a point or node met by a strict analytic germ on an
  actual ordinary/embedded resolution.
- A **strict germ** is a reduced analytic branch; its Cartier coefficient may
  exceed one.  A **global prime** is an irreducible global reduced boundary
  curve.  Distinct germs become distinct global primes only after the forest
  incidence argument.

For every strict germ `C`, its displayed `A`-degree is
`ord_(C normalization)(u)`.  The total weighted local degree is always

```text
length C[[v,z]]/(h,h_z)=8.                            (1.1)
```

## 2. Full ordinary blowup audit for `B3/A2`

### 2.1 Normalization and the first exceptional line

The balanced Hessian condition is `b(0)!=0`.  A unit and a constant target
shear preserving `u=0` put

```text
b(z)=1+b1*z+...,
a(z)=a1*z+...,
c(z)=-tau*z+c2*z^2+... .                             (2.1)
```

Solving the target critical equations gives
`v0=tau*z+O(z^2)`.  The critical value begins
`(1-tau)^2*z^3`, so the surface is `A2` exactly when `tau!=1` in this
balanced cell.

Blow up the origin.  In the `v`-chart

```text
u=vU,                  z=vZ,
f/v^2=U(1-tau*Z)+v*Z(Z-1)^2+O(vU,v^2).               (2.2)
```

The exceptional component `E1` is `U=0`; it contains

```text
q_L:  Z=0,                q_ST: Z=1.                 (2.3)
```

Here `L` meets `q_L`, while the two section branches `S,T` meet each other
and `E1` at `q_ST`.  The other exceptional component `E2` meets `E1` at
`Z=1/tau` if `tau!=0`; for `tau=0` that node is the point `Z=infinity`.
This single ordinary blowup resolves the `A2` surface.

On the surface, away from the exceptional node, (2.2) gives

```text
U=-v*Z(Z-1)^2/(1-tau*Z)+O(v^2).
```

Substitution in the target-coordinate polar gives the exact exceptional
initial equation

```text
p/v^2 = unit *
 (Z-1)(-2*tau*Z^2+3Z-1)/(1-tau*Z)+O(v).              (2.4)
```

The root `Z=1` is simple because `tau!=1`.  Writing `Z=1+k v+...` in the
full surface and polar equations gives

```text
k=-1/2,          u=v^4/(4(1-tau))+O(v^5).             (2.5)
```

Thus this is a coefficient-one degree-four polar germ.  Its slope is
strictly between the section slopes `0` and `-1`; after one embedded blowup
of `q_ST`, `S,T`, and this germ meet three different points of the new
exceptional component.

### 2.2 The nonzero-modulus strata

Assume `tau!=0`.  At the generic points of `E1,E2`, direct orders in `p`
are

```text
m=(2,1),             n=C_A2*m=(3,0).                 (2.6)
```

The second value is one because the term `-tau*u` occurs in `p`; it is the
term that disappears at `tau=0`.  The remaining two first-order sites solve

```text
-2*tau*Z^2+3Z-1=0,          Delta=9-8tau.             (2.7)
```

Neither site is `q_L`, `q_ST`, or the exceptional node while `tau!=1`.

If `Delta!=0`, both roots are simple.  At either root `u=unit*v^2+...`, so
the exact strict divisor is

```text
degree 4 at q_ST; degree 2 at q_+; degree 2 at q_-;
all three Cartier coefficients are one.              (2.8)
```

If `Delta=0`, necessarily `tau=9/8`, and the quadratic block has one double
site `Z=2/3`, distinct from all boundary sites.  Remove the simple
degree-four factor and use local coordinates `r=v`, `W=Z-2/3`.  Weierstrass
preparation gives, up to a unit,

```text
Q_Delta=W^2+A(r)W+B(r),
d_Delta(r)=A(r)^2-4B(r),       d_Delta(0)=0.           (2.9)
```

This is an exact exhaustive classification over `C[[r]]`:

| analytic discriminant | strict quadratic block | Cartier coefficient / weighted `A`-degree |
|---|---|---|
| `ord d_Delta=2k<infinity` | two branches at one initial site, local mutual intersection `k` | each coefficient `1`, degree `2+2` |
| `ord d_Delta` odd | one irreducible ramified branch | coefficient `1`, degree `4` |
| `d_Delta=0` | one doubled prime | coefficient `2`, underlying degree `2` |

The first line follows because `sqrt(d_Delta)` is analytic; the second
because an odd-order discriminant is nonsquare and has parameter
`r=t^2`; the third is the literal square of a linear Weierstrass factor.
Thus a blanket coefficient-one assertion at `Delta=0` needs the additional
hypothesis `d_Delta!=0`.  No promoted common normal-F5 hypothesis in the
charged sources supplies that condition.

### 2.3 The `tau=0` stratum

Now `c'(0)=0`.  Use the `z`-chart of the same ordinary blowup:

```text
u=zx,                    v=zy.
```

The strict surface and polar are

```text
f/z^2
 =xy+z[(1-y)^2+x(a1*x+b1*y+c2)]+O(z^2),             (2.10)

p
 =z^2[(y-1)(y-3)+a1*x^2+b1*x*y+2c2*x+O(z)].         (2.11)
```

At the node `x=y=z=0`, the coefficient of `z` in (2.10) is one, so the
blown-up surface is smooth.  The two exceptional components are

```text
E1: x=0,             E2: y=0,
E1 cap E2: x=y=0.                                      (2.12)
```

Since `div(z)=E1+E2` and the bracket in (2.11) is not identically zero on
either component,

```text
ord_E1(p)=ord_E2(p)=2,
m=(2,2),             n=C_A2*m=(2,2).                 (2.13)
```

This is coefficient-family invariant throughout `tau=0`; higher terms
cannot restore `(2,1)` or increase either generic exceptional valuation.

On `E1`, (2.11) has the two forced simple sites `y=1,3`, equivalently
`Z=1,1/3`.  They give the degree-four midpoint germ and one degree-two germ,
both with coefficient one.  On `E2`, the residual first-site divisor is the
binary quadratic

```text
Q_E2(X,W)=a1*X^2+2*c2*X*W+3*W^2.                    (2.14)
```

Here `x=X/W` on the finite chart, while `W/X=z/u` is the chart at the free
endpoint of `E2`.  The node `E1 cap E2` is `x=0`, where (2.14) equals three;
the residual block never collides with that node.  Put

```text
D0=c2^2-3a1.                                         (2.15)
```

If `D0!=0`, (2.14) has two distinct projective roots.  Each produces a
smooth coefficient-one polar germ transverse to `E2`, with `A`-degree one.
This remains true when one root is the free endpoint (`a1=0,c2!=0`).

If `D0=0`, let `q_R` be its double projective root.  In a smooth chart at
`q_R`, let `r` be transverse to `E2`, remove the two fixed factors, and write

```text
Q_R=W_R^2+A_R(r)W_R+B_R(r),
d_R=A_R^2-4B_R.                                      (2.16)
```

The exhaustive residual classification is

| analytic discriminant | residual strict block | Cartier coefficient / weighted `A`-degree |
|---|---|---|
| `ord d_R=2k<infinity` | two branches, local mutual intersection `k` | each coefficient `1`, degree `1+1` |
| `ord d_R` odd | one irreducible ramified branch | coefficient `1`, degree `2` |
| `d_R=0` | one doubled prime | coefficient `2`, underlying degree `1` |

Together with the fixed germs, the three possible scheme partitions are

```text
4+2+1+1;       4+2+2;       4+2+(2 times 1),         (2.17)
```

and every line sums to the length eight in (1.1).  The last possibility is
not hypothetical: for `a=c=0,b=1`, one has `f=h+uv`, and `p=h_z`; the
vertical prime `{v=z=0}` is a Cartier factor of coefficient two and has
`A`-degree one.  The rational-forest theorem uses the reduced support and
does not by itself exclude this multiplicity-two case.

## 3. Independent ordinary blowup audit for `U3/A3`

Write

```text
b=zB,             c=zC,             C(0)=c1!=0.
```

Normality forces `a0=a(0)!=0`: otherwise every term of `f` is divisible by
`z`.  The target Hessian in `(u,z)` is nondegenerate.  Its critical value is
`unit*v^4`, hence the surface tag is `A3` for every higher coefficient in
the named cell.

In the first `v`-chart, `u=vU,z=vZ`,

```text
f/v^2=U(a0*U+c1*Z)+v*Z(Z-1)^2+O(vU,v^2).             (3.1)
```

The first exceptional components are `E1:{U=0}` and
`E3:{a0U+c1Z=0}`.  Their intersection is a residual `A1` singularity at
`U=Z=v=0`.  Blowing up that point inserts `E2` and gives the standard chain

```text
E1 -- E2 -- E3.                                      (3.2)
```

The section branches `S,T` share the smooth point `Z=1` of `E1`; `L` meets
a smooth point of `E2`.  The other spin `E3` has no strict H attachment.

The polar has two forced Newton regions.  With weights
`(v,z,u)=(2,3,4)`, the leading polar and nonvertical surface equations are

```text
c1*u+v^2-4vz=0,
2v*z^2+(a0/c1^2)*v^4=0.                              (3.3)
```

Their cusp is

```text
v=t^2,
z=lambda*t^3+O(t^4),       2lambda^2=-a0/c1^2,
u=-t^4/c1+O(t^5).                                   (3.4)
```

It is one reduced coefficient-one degree-four germ.  It passes through the
residual point in the first blowup; after resolving the `A1`, its strict
transform passes through the node `E1 cap E2`.

In the tangent-pair coordinates `y=z-v`, the other germ is

```text
y=-z^2/2+O(z^3),       u=z^4/(4c1)+O(z^5).           (3.5)
```

It is smooth, reduced, coefficient one, degree four, and meets `E1` at the
shared `S,T` point with midpoint slope `-1/2`.  The controlling coefficients
in (3.3)--(3.5) are nonzero functions of `a0,c1`; there is no additional
modulus-special cell.

At generic points of the three exceptional components, direct substitution
in `p` gives

```text
m=(2,2,1),              n=C_A3*m=(2,1,0).            (3.6)
```

The smooth germ contributes one contact to `E1`; the nodal cusp contributes
one to each of `E1,E2`.  This reconstructs exactly `n=2e1+e2` without
identifying it with the boundary vector merely because the two vectors
happen to agree.

## 4. Contact-labelled local trees and `S0/T` ownership

Use the charged q=6 global marking

```text
S=S0,
L=P_l,
T=S0+3F-sum_(i in I)P_i,       |I|=6,
O={o1,o2}={1,...,9} minus ({l} union I).              (4.1)
```

For `B3`, with `R1` the `A2` endpoint met by `L,S,T`, the standard
chronology is

```text
R1=F-P_l-P_o1,          R2=P_o1-P_o2,          L=P_l.
                                                               (4.2)
```

`L` meets `R1` at `q_L`; `S0,T` meet `R1` at the distinct point `q_ST`.
The minimal local tree is `L--R1--R2`, with the `S,T` flags both at
`q_ST`.  Blowing up `q_ST` for the reduced boundary introduces a star
component `G_ST` whose distinct leaves are `S0,T`, and the fixed degree-four
polar germ.  The remaining nonzero-`tau` polar sites lie on `R1`; the
`tau=0` residual twig lies on `R2`.  A double-site block is replaced by its
own embedded-resolution twig, with one leaf for an irreducible/doubled
reduced prime and two leaves for a split block.

```text
       S0
        \
         G_ST--R1--R2--R_tau0
        /  |    | \
       T   P_4  L  P_R1
```

Here `P_R1` denotes the simple non-midpoint sites (two in the generic
nonzero-modulus cell and one fixed site when `tau=0`), while `R_tau0` denotes
the residual twig and is absent for `tau!=0`.  Coincident-block twigs replace,
rather than add to, the corresponding shorthand leaf.

For `U3`, a compatible standard chronology is

```text
E1=F-P_o1-P_o2,             retained spin met by S0,T,
E2=P_o2-P_l,                central component met by L,
E3=P_o1-P_o2,               other spin,
L=P_l.                                                     (4.3)
```

After embedded resolution the contact-labelled local tree is schematically

```text
       S0
        \
         G_ST--E1--G_12--E2--E3
        /  |          |    |
       T   P_mid      P_cusp L
```

where `G_ST` resolves the shared section/midpoint site and `G_12` subdivides
the old `E1 cap E2` node met by the cusp.  All displayed objects are reduced
support vertices; Cartier multiplicities remain labels, not repeated graph
vertices.

After applying the forest argument to distinct resolved leaves, the exact
local reduced-prime census is:

| cell | reduced strict germs over `p0` | forced distinct global primes meeting this local tree |
|---|---:|---:|
| `U3` | `2` | `2` |
| `B3`, `tau!=0,Delta!=0` | `3` | `3` |
| `B3`, `tau!=0,Delta=0`, split block | `3` | `3` |
| same, irreducible or doubled block | `2` | `2` |
| `B3`, `tau=0`, split residual | `4` | `4` |
| same, irreducible or doubled residual | `3` | `3` |

These are lower bounds on distinct reduced global ramification primes forced
by this one local tree.  A doubled Cartier coefficient counts once, and
additional affine or contracted primes are not included.

## 5. Exact global strict totals and contracted carriers

In the orthogonal total-transform basis,

```text
r^*R_X=4S0+11F-2*sum_(i=1)^9 P_i.                    (5.1)
```

For `B3,tau!=0`,

```text
M_R=2R1+R2=2F-2P_l-P_o1-P_o2.                        (5.2)
```

For `U3`, (4.3) gives the same class:

```text
M_R=2E1+2E2+E3=2F-2P_l-P_o1-P_o2.                   (5.3)
```

Thus in both cases

```text
C_str=r^*R_X-M_R
 =4S0+9F-P_o1-P_o2-2*sum_(i in I)P_i,
c=(0,1,1,2,2,2,2,2,2),
sum c_i=14,             sum c_i^2=26.                (5.4)
```

This is a total Cartier class.  In a doubled-block cell it is a weighted
sum of reduced prime classes, not their unweighted sum.

For `B3,tau=0`, (2.13) instead gives

```text
M_R=2R1+2R2=2F-2P_l-2P_o2,
C_str=4S0+9F-2P_o1-2*sum_(i in I)P_i,
c_tau0=(0,2,0,2,2,2,2,2,2),
sum c_i=14,             sum c_i^2=28.                (5.5)
```

The orientation is fixed by (4.2); reversing the named outside chronology
reverses the two outside entries.  Equations (5.4)--(5.5) both have
`A.C_str=8`, `B.C_str=4`, and `S0.C_str=1`, as required.

Every charged q=6 contracted carrier disjoint from H has

```text
Z_J=S0+2F-sum_(j in J)P_j,
J={o1,o2} union K,             K subset I, |K|=3.     (5.6)
```

Subtracting one from (5.4) gives

```text
C_str-Z_J
 =3S0+7F-sum_(i in K)P_i-2*sum_(i in I minus K)P_i,
multiset(c^Z)=(0,0,0,1,1,1,2,2,2),
sum c_i^Z=9,             sum (c_i^Z)^2=15.           (5.7)
```

A second carrier or coefficient two is impossible because every `J`
contains both outside coordinates, initially of value one.  In the
`tau=0` class (5.5), every `J` contains `o2`, initially of value zero, so
even one subtraction produces `c_o2=-1`.  Hence no effective charged
contracted carrier coexists with the `tau=0` strict total.  This is a
numerical necessary statement, not proof that any remaining class is
effective.

## 6. Exact forest/second-path criterion

Let `W_min` be the surface with the ADE singularity minimally resolved.
First blow up only the common infinitely-near centres needed to separate the
two prescribed germs over the charged F5 point; call the result `W_loc`.
For distinct reduced global primes `C_i,C_j`, define

```text
lambda_ij
 =sum_(q over the charged local cluster)
    mult_q(C_i)*mult_q(C_j),                          (6.1)
```

where the sum includes every common infinitely-near centre blown up while
separating their local germs.  The blowup intersection formula is

```text
C_i^(W_loc).C_j^(W_loc)
 =C_i^(W_min).C_j^(W_min)-lambda_ij.                  (6.2)
```

Both primes now attach to the same connected local resolution tree.  If the
right side of (6.2) were positive, they would meet in at least one additional
cluster away from that prescribed tree.  Resolving the full **reduced**
boundary would turn that cluster into an edge or a second exceptional path,
in either case making a cycle.  The rational-forest theorem therefore
requires

```text
C_i^(W_loc).C_j^(W_loc)=0.                           (6.3)
```

Consequently:

- if the germs meet distinct physical sites on `W_min`, then
  `lambda_ij=0`, and **any positive** intersection in the `W_min` class is a
  forbidden second path;
- if two branches split from one double site, a positive value
  `C_i.C_j=lambda_ij` merely records the local contact that (6.1) resolves
  into the existing tree and is allowed; only `C_i.C_j>lambda_ij` forces a
  second path;
- in the even-discriminant rows of (2.9) or (2.16),
  `lambda_ij=k=ord(d)/2`; this contact can be arbitrarily deep, so raw
  positivity has no uniform force there;
- if one global irreducible prime carried two distinct local branches, its
  single global vertex would attach to two resolved leaves of the local tree
  and itself make a cycle.  The forest therefore forces those branches onto
  distinct global primes.  A doubled Cartier coefficient on one reduced
  branch creates no second vertex and no cycle by multiplicity alone.

Thus the uncorrected pairwise-zero gate is valid for `U3`, for
`B3,tau!=0,Delta!=0`, for a one-branch `Delta=0` block against the fixed
branch, and for the distinct-root `tau=0` sites.  It is not a licensed raw
class gate for the two members of a split double-site block until the local
number `lambda_ij` is subtracted.  Likewise, any global energy identity that
decomposes the total into coefficient-one primes must branch separately on
the doubled-prime cases in Sections 2.2 and 2.3.

## 7. Scope and downstream disposition

The exact local conclusions are:

```text
U3/A3: always 4+4, coefficient one, m=(2,2,1), n=2e1+e2;

B3/A2, tau!=0, Delta!=0:
  4+2+2, coefficient one, m=(2,1), n=3e1;

B3/A2, tau!=0, Delta=0:
  4 plus a discriminant-classified weighted degree-four block,
  m=(2,1), n=3e1;

B3/A2, tau=0:
  4+2 plus a discriminant-classified weighted degree-two block,
  m=(2,2), n=(2,2).
```

Safe provisional descendants are: rerun the q6 lattice energy separately
on (5.4) and (5.5); subtract the exact local `lambda` in every split
double-site cell; and use weighted prime decompositions in the doubled
cells.  Do not promote a blanket q6 no-affine elimination from an unweighted
positive total until those branches are checked.

Nothing here establishes chronological effectivity, analytic realization of
a marked global fibre, existence of the quadratic frame, occurrence from a
minimal Keller map, a counterexample, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22514`.
- Body SHA-256:
  `941d4e27b95bee2483b98fa62c4e1b9c9b94e7dff7aa200848ab03977461522d`.
- Frozen basis: `54df5b64b5ea8355cd8c13aa790dcf0f703c5bb7`.
