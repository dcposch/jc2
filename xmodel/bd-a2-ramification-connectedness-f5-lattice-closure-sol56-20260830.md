# Quadratic ramification: ample connectedness and the finite F5 lattice closure

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra delegated lattice lane `/root/ramification_component_lattice`  
Frozen basis: `1efd7a76538e3fcdf51b999563262afc40d58947`  
Lifecycle: **EXACT GLOBAL PRODUCER / CHARGES BINDING LOCAL INTEGRATION / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

Let `X` be the smooth irreducible quadratic incidence surface of class
`2A+3B` in `P2 times P1`, let `pi:X->P2` be finite near reduced squarefree
infinity `H`, and impose the promoted dominant-`A2` first-leg hypotheses.
The Cartier source ramification divisor is

```text
R_pi ~ 2A+B.
```

Its class is ample.  Therefore its support is connected.  This removes the
reducibility loophole in the promoted attachment theorem: the two distinct
boundary attachment points forced in `F1,F2,F4,F7` create a cycle even when
the reduced ramification support has several components.  Hence none of
those four types survives.

For `F5`, charge the binding local integration

```text
8fcd071fff6e828879b7926ad9398f3d33f81344e58f6fe04c758a19c326641e
  xmodel/bd-a2-f5-local-different-two-branch-coordinator-integration-sol56-20260830.md
  body 6988 / 2d14c7fa9675d41eaaf208e10c2dc4e72e596fa6fbf9503350dd18295abe0787
```

Its Opus 5 review has sealed full-file SHA-256
`7e335e1a1636d1b4342cf0f163fd7051c33b38b3c16766f8c7d94f92e5beea0c`
and body SHA-256
`5a77b09861b3e53c480715399d777db58290ce60466cb4485f5c25f1c4f5b035`.
The integration gives two reduced transverse source-different germs at the
unique boundary point, of weights `3` and `5`.  A forest forces them onto
distinct global components `D_3,D_5`, each with Cartier multiplicity one.
An exhaustive rank-eleven lattice calculation leaves one numerical orbit:

```text
R_pi = D_3 + D_5 + 2Z,
D_3 + Z = A,
D_3.D_5=1,       D_3.Z=3,       D_5.Z=4.             (0.1)
```

It fails twice.  The equality `D_3+Z=A=sum H_i` is a nonzero relation among
reduced ramification-component classes in `Cl(X minus H)`, contradicting the
promoted unit/localization injection.  Independently, `Z` supplies an
interior path between `D_3,D_5`, while their transverse boundary germs
supply another path, so the resolved boundary has a cycle.

Thus, conditional only on different-model review of this packet,

> the smooth projectively finite quadratic stratum with reduced squarefree
> infinity has no dominant `A2` first leg.

This closes that declared stratum, not all quadratic presentations.

## 1. Intersection and Picard conventions

On `X`, ambient intersection gives

```text
A^2=3,       A.B=2,       B^2=0,
K_X=-A+B,    R_pi=K_X-pi^*K_P2=2A+B.                 (1.1)
```

Projection `q:X->P1` is the nine-singular-fibre conic bundle from the
promoted class-group audit, and `rho(X)=11`.  A curve of infinity bidegree
`(a,b)` has

```text
B.C=a,       A.C=b.                                  (1.2)
```

If `H_i` is an infinity component, then

```text
H_i^2=b_i-sum_(j!=i) H_i.H_j.                        (1.3)
```

Using the exact contacts in the promoted seven-type classification, the
Gram matrices of the in-scope component lattices are

```text
F1: [3],                                             det= 3
F2: [-1 2; 2 0],                                    det=-4
F4: [-2 3; 3 -1],                                   det=-7
F5: [-1 1 1; 1 -2 2; 1 2 -2],                      det= 8
F7: [-1 0 2; 0 -1 2; 2 2 -3],                      det= 5.       (1.4)
```

Every displayed lattice is nondegenerate, so its component classes are
independent in `Pic(X)`.  Consequently localization gives the exact free
ranks

```text
rank Cl(X minus H)=10,9,9,8,8
```

for `F1,F2,F4,F5,F7`, respectively.  These ranks explain why the old raw
rank shortcut failed, but the actual component-class injection remains
decisive in (0.1).

## 2. The ramification support is connected

The line bundle `O_X(2A+B)` is the restriction of the ample ambient bundle
`O(2,1)`.  The Jacobian determinant of the generically finite characteristic-
zero morphism `pi` is a nonzero section of it, so `R_pi` is a nonzero
effective ample Cartier divisor.

An effective ample divisor on a smooth projective surface has connected
support.  Indeed, if

```text
D=D_1+D_2,       Supp(D_1) disjoint Supp(D_2),
```

with both parts nonzero, then ampleness gives

```text
D_1^2=D.D_1>0,       D_2^2=D.D_2>0,       D_1.D_2=0.
```

Their span would contain two orthogonal positive-square directions,
contrary to the Hodge index theorem.  Apply this to `D=R_pi`.  The promoted
no-`H`-component lemma identifies its support with the closure of the
reduced affine ramification support, so no extra projective component is
being added here.

In a forest resolution, the connected total-transform subgraphs belonging
to connected `H` and connected `Supp(R_pi)`—including the exceptional chains
needed to connect each strict transform—are trees.  Two distinct physical
attachment points yield two disjoint local joining paths.  Contracting each
tree and each path gives two parallel edges, hence a graph cycle.  The
promoted attachment calculation supplies at least two distinct physical
points in each of `F1,F2,F4,F7`.  Therefore

```text
F1,F2,F4,F7: no compatible effective decomposition of R_pi.     (2.1)
```

This conclusion does not assume irreducibility or reducedness of the
Cartier divisor.

## 3. The exact F5 conic-bundle lattice

Write the three `F5` components as

```text
L:(0,1),       S:(1,1),       T:(1,1),
```

where `L.S=L.T=1`, `S.T=2`; hence `L^2=-1` and `S^2=T^2=-2`.
Use `S` as a conic-bundle section, put `F=B`, and in each of the nine
singular fibres choose the line `E_i` disjoint from `S`.  Choose `E_1` in
the fibre containing `L`.  Then

```text
S^2=-2,       S.F=1,       E_i^2=-1,
A=2S+5F-sum_(i=1)^9 E_i,
L=F-E_1,
T=S+4F-sum_(i=2)^9 E_i.                              (3.1)
```

All omitted pairings in this basis vanish.  Equations (3.1) recover
`A^2=3`, `A.F=2`, and the entire Gram matrix in (1.4).

There is also an exact classification of components disjoint from `H`.
If an irreducible curve `Z` has `A.Z=0`, then `pi(Z)` is a point and the
embedding in `P2 times P1` forces

```text
Z={target point} times P1,       F.Z=1.
```

It is a smooth section and adjunction gives `Z^2=-3`.  Imposing disjointness
from `L,S,T` in (3.1) gives precisely

```text
Z_I=S+2F-E_1-sum_(i in I)E_i,
I subset {2,...,9},       |I|=4.                     (3.2)
```

Thus there are only `binomial(8,4)=70` numerical candidates; effectivity is
not asserted.  For two candidates

```text
Z_I.Z_J=1-|I intersect J|.                           (3.3)
```

Distinct effective `A`-null curves are literal sections over different
target points and hence disjoint.  Therefore they can coexist only when
`|I intersect J|=1`; inclusion-exclusion also shows that no three such
four-subsets can be pairwise one-intersecting.

The Cartier coefficient of an `A`-null curve is not assumed to be a field-
extension ramification index: it is exceptional for `pi` and could exceed
two.  The total equality `R_pi.F=4` is the coefficient bound used below.

## 4. The forced `3+5` carriers

The binding local calculation gives two reduced transverse different germs.
If they lie on one global prime, they give two distinct points of that
prime's normalization over the connected infinity tree, and the attachment-
cycle lemma already excludes it.  In a survivor they therefore lie on
distinct primes `D_3` and `D_5`.  Reducedness of the local Cartier equation
forces their global Cartier coefficients to be one.  Their contact vectors,
in the order `(L,S,T)`, are

```text
D_3: (1,1,1),       A.D_3=3,
D_5: (1,2,2),       A.D_5=5.                         (4.1)
```

These vectors exhaust `R_pi.(L,S,T)=(2,3,3)`.  Hence every other prime in
`R_pi` is one of the `A`-null curves (3.2).  Put

```text
x=F.D_3,       y=F.D_5,
R_pi=D_3+D_5+sum_k nu_k Z_(I_k),
N=sum_k nu_k=4-x-y.                                  (4.2)
```

Both `x,y` are positive: a curve of `F`-degree zero lies in a conic fibre
and has `A`-degree only one or two, not three or five.  Thus `0<=N<=2`.
The only possible extra multiplicity patterns are no `Z`, one simple `Z`,
two distinct simple `Z`'s, or one doubled `Z`.  This explicitly keeps the
Cartier multiplicities `nu_k` separate from reduced support.

The two local carrier germs are transverse, so their intersection at the
boundary is one.  Any additional intersection would make a second path
between them and violate the forest condition.  Therefore

```text
D_3.D_5=1.                                           (4.3)
```

Write their classes in (3.1) as

```text
D_3=xS+(2x+1)F-(x-1)E_1-sum_(j=2)^9 a_j E_j,
D_5=yS+(2y+2)F-(y-1)E_1-sum_(j=2)^9 b_j E_j.         (4.4)
```

Here

```text
a_j=D_3.E_j>=0,       b_j=D_5.E_j>=0,
```

because the carrier primes are distinct from every `E_j`.  Equivalently
these are their nonnegative multiplicities on the ruled-surface blowdown.
Equation (4.1) gives

```text
sum a_j=4x,       sum b_j=4y.                        (4.5)
```

For

```text
c_j=sum_(k:j in I_k) nu_k,
```

the total class equality is exactly

```text
a_j+b_j+c_j=2       for every j=2,...,9.             (4.6)
```

Adjunction, rational normalization, and (4.3) give the finite tests

```text
D_3^2=x^2+4x-1-sum a_j^2,
delta_3=(D_3^2+x-1)/2 in Z_(>=0),

D_5^2=y^2+6y-1-sum b_j^2,
delta_5=(D_5^2+y-3)/2 in Z_(>=0),

sum a_j*b_j=xy+3x+2y-2.                              (4.7)
```

Since (4.6) forces `0<=a_j,b_j<=2`, this is a literal finite enumeration,
not an effectivity heuristic.

## 5. Exhaustion and the unique failed orbit

Up to permutation of `E_2,...,E_9`, the exhaustive cases and the number of
solutions to (4.5)--(4.7) are

```text
(x,y; Z multiplicities)       lattice orbits
(1,1; 2)                            1
(1,1; 1+1)                          0
(1,2; 1)                            0
(2,1; 1)                            0
(1,3; none)                         0
(2,2; none)                         0
(3,1; none)                         0.               (5.1)
```

For the `1+1` row, (3.3) fixes the unique pair-intersection pattern up to
permutation.  The enumeration requires nonnegative integral
`delta_3,delta_5`; no smoothness or general-position assumption is inserted.

Here is the complete standard-library replay.  The coordinates `0,...,7`
stand for `E_2,...,E_9`; `I,J` are the unique relevant subset patterns up to
permutation.

```python
from itertools import product

I = {0, 1, 2, 3}
J = {0, 4, 5, 6}                 # |I intersect J|=1
cases = [
    (1, 1, [(2, I)]),
    (1, 1, [(1, I), (1, J)]),
    (1, 2, [(1, I)]),
    (2, 1, [(1, I)]),
    (1, 3, []), (2, 2, []), (3, 1, []),
]

for x, y, leaves in cases:
    c = [sum(nu for nu, K in leaves if j in K) for j in range(8)]
    count = 0
    for a in product(range(3), repeat=8):
        b = tuple(2-c[j]-a[j] for j in range(8))
        if min(b, default=0) < 0 or sum(a) != 4*x or sum(b) != 4*y:
            continue
        sq3 = x*x+4*x-1-sum(z*z for z in a)
        sq5 = y*y+6*y-1-sum(z*z for z in b)
        if sq3+x-1 < 0 or (sq3+x-1) % 2:
            continue
        if sq5+y-3 < 0 or (sq5+y-3) % 2:
            continue
        if sum(u*v for u, v in zip(a, b)) != x*y+3*x+2*y-2:
            continue
        count += 1
    print(x, y, tuple(nu for nu, _ in leaves), count)
```

Its counts are exactly `1,0,0,0,0,0,0` in the displayed order.

In the sole orbit, choose a four-subset `I` of `{2,...,9}` and let `J` be
its complement.  Then

```text
D_3=S+3F-sum_(j in J)E_j,       D_3^2=0,  delta_3=0,
D_5=S+4F-sum_(j in J)E_j,       D_5^2=2,  delta_5=0,
Z  =S+2F-E_1-sum_(i in I)E_i,   Z^2=-3,
R_pi=D_3+D_5+2Z.                                    (5.2)
```

Direct intersection gives

```text
D_3.D_5=1,       D_3.Z=3,       D_5.Z=4.             (5.3)
```

The candidate is impossible for either of two independent reasons.

First, (3.1) and (5.2) give the literal Picard relation

```text
D_3+Z=A=L+S+T.                                      (5.4)
```

The dominant block morphism forces `O(U)^*=O(X minus H)^*=C^*`, so
localization injects the free group on the *reduced* ramification primes
`D_3,D_5,Z` into `Cl(X minus H)`.  Relation (5.4) maps
`[D_3]+[Z]` to zero and contradicts that injection.  The coefficient `2` of
`Z` in the Cartier different is irrelevant to this reduced-support map.

Second, the boundary point gives a path from `D_3` to `D_5`, while (5.3)
gives a path through the `H`-disjoint component `Z`.  These are distinct
paths in every embedded resolution, hence a cycle.  Concentrating each
positive intersection at one physical point cannot remove the alternate
path.

Therefore the `F5` compatible lattice set is empty as well.

## 6. Scope, review, and compute disposition

Combining (2.1) and Section 5 eliminates every in-scope reduced rational-
forest type.  Types `F3,F6` remain projective-coefficient-basepoint strata
outside projective finiteness; `F8,F9` have no rational-tree refinement.
Nonreduced infinity, singular incidence closure, affine coefficient common
zeros, fibre/target degree drop, and basis minimization remain separate.

The ample-connectedness and lattice arguments are exact desk mathematics.
The full `F5` conclusion charges the independently reviewed binding local
`3+5` integration.  This global packet itself still requires different-model
hostile review before canonical promotion.  No AWS job is justified: the
complete replay is at most seven cases with eight coordinates in `{0,1,2}`.
If reviewed, the next bounded client is not a larger lattice search but the
adjacent nonreduced-infinity and singular-ambient strata.

No occurrence, compatible jet, formal arc, polynomial map, counterexample,
general quadratic/cubic block closure, primitivity theorem, or JC2 result is
asserted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13850`.
- Body SHA-256:
  `2fa574c72a81e6b736cd6847fcbb9cc9272b60ed34c46ef40c1996a3020d92b6`.
- Frozen basis: `1efd7a76538e3fcdf51b999563262afc40d58947`.
