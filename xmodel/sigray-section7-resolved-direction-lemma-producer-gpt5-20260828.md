# Sigray Section 7: resolved-direction and no-duplication lemma

Date: 2026-08-28  
Producer: GPT-5 / Codex  
Purpose: discharge the global geometric lemma isolated by the hostile review
of the repaired Section 7 Euler ledger.

## 0. Verdict

**PROVED UNDER THE CORRECTED EGGERS--WALL PACKAGE, WITH THREE STANDARD
GEOMETRIC INPUTS STATED EXPLICITLY.**

For every critical-value flag on one reference fibre there is one geometric
direction parameter line `U_i ~= A^1`. The cyclic ambiguity of the Puiseux
coefficient is exactly a finite cyclic quotient of an affine line, hence is
again an affine line. The zero-order residual functions of `f` and `g`
descend to polynomials on `U_i`. Across all fibres, points of the disjoint
union of these lines are in bijection with direction clusters, not with
individual normalized punctures. The value map on each line therefore has
constructible fibre-count pushforward of Euler integral one.

There is no remaining no-duplication obstruction. The proof does not assert
that a value curve is embedded or that its parametrization is injective.

The three external inputs are only:

1. elimination of indeterminacy of a rational map from a smooth projective
   surface by finitely many point blowups;
2. realization of a rational rank-one divisorial valuation of a smooth
   surface on a common point-blowup model (equivalently, the elementary
   Euclidean-algorithm resolution of a rational monomial valuation);
3. Euler-Fubini for complex algebraic constructible functions.

All three are stated in the exact form used below. No classification or
unproved algebraization assertion is used.

## 1. Custody and hypotheses

Primary source:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  jc2/refs/sigray_full.pdf
```

Reviewed Section 7 audit:

```text
0159cdf18f9ad1c986677d4631916dbbef0b5310829958f6dac192eab2795a31
  jc2/xmodel/sigray-section7-full-independent-audit-sol-ultra-20260828.md
```

Hostile review which isolated this obligation:

```text
af1ce600bff775bacee122bea3cd5a098ef6a457616273d8a0147c16438a0afe
  jc2/xmodel/sigray-section7-full-independent-audit-hostile-review-gpt5-20260828.md
```

No canonical file was edited. No file under `jc2-lean` was accessed, listed,
searched, built, or modified.

Let `Phi=(f,g):A^2->A^2` be the polynomial Keller map considered in the
paper. Fix a reference value `a_0`. We use the following already-corrected
tree facts.

### EW1. Centred zero-order flag

On the fibre `f=a`, use `A=f-a`. Every normalized puncture at which `g` has
a finite value has a unique flag

```text
Fhat_P in T_(a,cv),    d_(A,Fhat_P)=d_(g,Fhat_P)=0.
```

The flag is unique on its puncture ray (corrected Statement 3.13 and
Proposition 7.2).

### EW2. Direction realization and clustering

At such a flag, a root of the centred first residual pattern determines one
geometric outgoing direction, modulo the finite root-of-unity ambiguity of
the residual coordinate. Every root orbit is realized, and all normalized
punctures with the same flag and outgoing direction form exactly the set
`R^*_(F,c)` of Proposition 7.3. This is Proposition 3.1 and corrected
Statements 3.9, 3.18.

### EW3. Twisted transport

Corrected Statement 3.14 transports the positive/zero truncation tree from
`a_0` to every `a`. It preserves height, contact indices, and zero orders.
The residual patterns of all fixed polynomials are transported after one
common root-of-unity change of residual coordinate. Two choices differ by
the stabilizer of the same geometric direction.

### EW4. Local value and weight

For a direction represented by `c`, the fibre and `g` values are the
evaluations of the bare first residual pattern and the `g` residual pattern.
The direction-cluster weight

```text
b_F=kappa_F(pi(F)-1)
```

is preserved by transport. Proposition 7.3 gives `L_C>=b_F` for the whole
cluster.

These are precisely the corrected facts already used by the Section 7
audit. The present report proves the missing global organization of them.

## 2. The three external geometric inputs

### G1. Common surface resolution

If `X_0` is a smooth projective compactification of `A^2` and
`Phi:X_0 ---> P^1 x P^1` is rational, there is a composition of finitely
many point blowups `rho:X->X_0`, with `X` smooth, such that

```text
Phi_bar:X -> P^1 x P^1
```

is a morphism. A finite collection of divisorial valuations over the
boundary can be realized simultaneously on a further common point-blowup
model. Further blowups do not identify two distinct divisorial valuations.

This is the surface form of elimination of indeterminacy.

### G2. Rational flags are divisorial

A rational Eggers--Wall flag is locally a rational monomial valuation after
subtracting its finite Puiseux truncation. After multiplying the two weights
to make them coprime positive integers, the Euclidean algorithm realizes
that valuation by a finite sequence of ordinary point blowups. Its residue
field has transcendence degree one. The resulting exceptional component is
`P^1`; the residual coefficient supplies an affine chart, possibly only
after a finite cyclic cover.

This gives a boundary component for every `F_i in T_(a0,cv)`, even when
`F_i` is not already a vertex on the initially chosen resolution.

### G3. Euler pushforward

For a complex algebraic map `h:X->Y` and a constructible function `alpha`,
the pushforward

```text
(h_! alpha)(y)=integral_(h^(-1)(y)) alpha dchi_c
```

is constructible and satisfies

```text
integral_Y h_!alpha dchi_c = integral_X alpha dchi_c.
```

For a finite-fibre map and `alpha=1`, the pushforward is the geometric fibre
cardinality.

## 3. One boundary component and its affine direction line

Enumerate

```text
T_(a0,cv)={F_1,...,F_s}.
```

The set is finite because the reference fibre has finitely many punctures
and every puncture ray has at most one centred zero-order flag.

By G1--G2, choose one smooth projective `X` which resolves the graph of
`Phi` and realizes every valuation `F_i` as a distinct boundary component
`E_i`. Each `E_i` is `P^1`.

Fix `i`. On a suitable cyclic Puiseux cover, choose the residual coefficient
`eta`. The finite group of deck changes preserving the truncation `F_i` is
an effective cyclic group

```text
Gamma_i=mu_(m_i),    eta |-> zeta eta.
```

The covered coefficient chart is `A^1_eta`. The geometric component chart
is its quotient:

```text
U_i := A^1_eta/Gamma_i
     = Spec C[eta]^(Gamma_i)
     = Spec C[eta^(m_i)]
     ~= A^1_z,                 z=eta^(m_i).              (3.1)
```

This also covers the trivial case `m_i=1`. The fixed coefficient `eta=0`
gives one quotient point, not `m_i` directions.

The missing point of `E_i=P^1` is the coefficient `eta=infinity`, namely the
incoming direction toward the lower truncation. Thus

```text
U_i=E_i\{infinity_i} ~= A^1.                            (3.2)
```

All outgoing finite Puiseux coefficients, including zero, lie in `U_i`.
The point `infinity_i` is not an additional outgoing direction; any branch
seen there has a different zero-order flag and is assigned by EW1 to that
other family.

Importantly, `U_i` is **not** the open boundary stratum obtained by deleting
every intersection with other boundary components. Finite intersection or
infinitely-near points encode collision directions and remain points of the
coefficient line (via the strict-transform identification after a blowup).
Only the single coefficient-infinity point is removed. This is why the
relevant Euler characteristic is `chi_c(A^1)=1`, not that of a multiply
punctured rational curve.

## 4. Descent of the two residual value functions

On the cyclic cover, a polynomial `h` has leading expression

```text
rho^(-N d_(h,F_i)) p_(h,F_i)(eta)
```

for a local root parameter `rho`. A deck change acts both on `rho` and on
`eta`. Since `h` itself is invariant, its residual polynomial can acquire a
character only from the prefactor. For

```text
h=f-a_0  and h=g,
```

the exponent is zero at a critical-value flag. Therefore no character is
present and

```text
p_(f-a0,F_i)(zeta eta)=p_(f-a0,F_i)(eta),
p_(g,F_i)(zeta eta)=p_(g,F_i)(eta)                      (4.1)
```

for every `zeta in Gamma_i`.

By (3.1), there are unique polynomials `A_i,Q_i in C[z]` such that

```text
p_(f-a0,F_i)(eta)=A_i(eta^(m_i)),
p_(g,F_i)(eta)=Q_i(eta^(m_i)).                          (4.2)
```

Set

```text
P_i(z):=A_i(z)+a_0.
```

Then on `U_i`

```text
Phi_bar|_(U_i)=phi_i: z |-> (P_i(z),Q_i(z)).            (4.3)
```

In particular, `(f,g)` restricts to a polynomial map on the geometric
direction line. Formula (4.3) proves descent; it does not assume exact
alignment of a named `eta` coordinate between fibres.

The polynomial `P_i` is nonconstant. Indeed, `F_i` lies on an actual branch
of `f=a_0`, so the centred residual polynomial has a realized zero. It cannot
be a nonzero constant, and it cannot be the zero polynomial because it is a
leading residual pattern. Hence `deg A_i>0`.

Consequently `P_i:A^1->A^1` is surjective and has finite fibres.

## 5. One parameter point equals one direction cluster

Let `z in U_i` and put

```text
(a,b)=phi_i(z)=(P_i(z),Q_i(z)).
```

Choose any lift `c in A^1_eta` with `c^(m_i)=z`. Equation (4.2) gives

```text
p_(f-a,F_i)(c)=P_i(z)-a=0.                              (5.1)
```

Under twisted transport EW3, the same equation holds at the transported
flag `F_i(a)` after the common residual-coordinate twist. By EW2, the root
orbit in (5.1) realizes one and only one **geometric** outgoing direction
`D(i,z)`. All normalized punctures above that direction form a nonempty
cluster

```text
C(i,z)=(F_i(a),D(i,z)).                                 (5.2)
```

EW4 gives `g(P)=Q_i(z)=b` for every puncture in this cluster.

The construction is independent of the chosen lift. Replacing `c` by an
element of its `Gamma_i` orbit does not change `z`, the descended values, or
the geometric outgoing direction. At `z=0` there is only the one fixed
orbit. This removes cyclic overcounting exactly.

### Injectivity on clusters

Suppose `C(i,z)=C(j,w)`. Pick a puncture `P` in the common nonempty cluster.
Its unique critical-value flag from EW1 is both `F_i(a)` and `F_j(a)`.
Twisted transport is an isomorphism, so `F_i=F_j` and `i=j`. With the flag
fixed, its geometric outgoing direction has one residue point on `U_i`;
hence `z=w`.

Thus different reference vertices cannot duplicate a cluster, and neither
can two cyclic representatives or two parameter points on one line.

### Surjectivity onto clusters

Conversely, let `C` be any finite-value direction cluster on any fibre
`f=a`, and choose `P in C`. EW1 gives its unique flag `Fhat_P`. Transport
back to `a_0` gives a unique `F_i`. The outgoing direction of `P` supplies a
residual coefficient orbit, hence a unique quotient point `z in U_i`.
The centred first residual equation says `P_i(z)=a`, and EW4 says
`Q_i(z)=g(P)`. Therefore `C=C(i,z)`.

We have proved the promised bijection

```text
disjoint_union_(i=1)^s U_i(C)
  <--> {finite-value direction clusters in all fibres},
z in U_i |-> C(i,z).                                    (5.3)
```

It is intentionally not a bijection with punctures: one cluster may contain
several normalized punctures.

## 6. Coverage of all fibres and constancy of the weight

Because every `P_i` is a nonconstant complex polynomial, for every
`a in C` the finite set `P_i^(-1)(a)` is nonempty. By (5.1)--(5.2), its
points are exactly the directions of the transported family `F_i(a)`.

Conversely EW3 sends every critical-value flag in `T_(a,cv)` back to a
unique member of `T_(a0,cv)`. Thus the reference list has neither a missing
family nor a duplicate family.

The component `E_i` on the one global surface is independent of the fibre,
so its geometric points give the fixed identification across all `a`.
The common twist in EW3 changes only a covered coordinate presentation,
`eta |-> omega eta`. On the quotient it may precompose the chosen affine
coordinate `z` by an automorphism, but it precomposes **both** residual
functions by that same automorphism. Fixing the geometric coordinate on
`U_i` once absorbs this precomposition. Thus the point of `E_i` and the
ordered value pair `(P_i(z),Q_i(z))` are independent of the named Puiseux
coordinate; no assertion of literal `eta` alignment is used.

Height and the characteristic contact index depend only on the valuation
`E_i`, not on `a` or `z`. Therefore

```text
b_i:=kappa_(F_i)(pi(F_i)-1)
```

is the weight of every cluster represented by `U_i`.

## 7. Constructible pushforward and Euler integral

Define

```text
n_i(a,b):=#phi_i^(-1)(a,b),
B(a,b):=sum_i b_i n_i(a,b).                             (7.1)
```

The count in (7.1) is of geometric parameter points. It counts two distinct
directions mapping to the same value twice, counts one ramified parameter
point once, and counts different `i` separately. By (5.3), this is exactly
one baseline for every direction cluster and no baseline for an individual
puncture inside a cluster.

The map `phi_i` has finite fibres because its first coordinate `P_i` is
nonconstant. It is in fact finite onto its affine image: if
`R_i=C[P_i(z),Q_i(z)] subset C[z]` and `n=deg P_i`, then `z` satisfies a
monic degree-`n` equation with coefficients in `C[P_i(z)] subset R_i`.
Thus `C[z]` is integral, hence finite, over `R_i`.

It follows either directly from a finite stratification, or from G3, that
`n_i` is constructible. Euler-Fubini gives

```text
integral_(A^2) n_i(a,b) dchi_c
 = chi_c(U_i)
 = chi_c(A^1)
 = 1.                                                   (7.2)
```

Therefore

```text
integral_(A^2) B(a,b) dchi_c = sum_i b_i.               (7.3)
```

Self-intersections or singularities of the value curve `phi_i(U_i)`, a
common image component for two different `i`, and ramification of `phi_i`
do not alter (7.2). All are handled by geometric fibre cardinality.

## 8. Consequence for the repaired Section 7 ledger

Let `d=td(f,g)` and `N(a,b)=#Phi^(-1)(a,b)`. On the normalized fibre
`f=a`, the divisor of `g-b` gives

```text
d-N(a,b)
 = sum_(P finite puncture, g(P)=b) Lambda(P).            (8.1)
```

Use (5.3) to group the right side into clusters. Proposition 7.3 gives

```text
d-N(a,b)=B(a,b)+E(a,b),    E(a,b)>=0,                   (8.2)
```

where `E(a,b)` is the sum of `L_C-b_i` for the clusters over `(a,b)`.
For fixed `a`,

```text
sum_b E(a,b)=delta_a^cl.                                (8.3)
```

For generic `a`, every root of every `P_i(z)-a` is simple. Generic `a` also
avoids `P_i(0)` when a cyclic cover is nontrivial, so simplicity on the
quotient is simplicity in the covered residual coordinate. The simple case
of Proposition 7.3 gives `E(a,b)=0`. Hence `delta_a^cl` is supported on a
finite set.

The function `E=d-N-B` is constructible. Euler-Fubini and (8.3) therefore
give

```text
integral_(A^2) E dchi_c
 = integral_(a in A^1) delta_a^cl dchi_c
 = sum_(a in C) delta_a^cl,                              (8.4)
```

where the last sum is an ordinary finite sum.

Finally, Keller etaleness makes `Phi` quasi-finite and every affine
preimage simple. By G3,

```text
integral_(A^2) N dchi_c=chi_c(A^2)=1.
```

Integrating (8.2), using (7.3) and (8.3), gives

```text
td(f,g)
 = 1 + sum_i kappa_(F_i)(pi(F_i)-1)
     + sum_(a in C) delta_a^cl.                         (22-cl)
```

Thus the resolved-direction lemma supplies exactly the missing global step
in the producer audit. No injectivity claim and no per-puncture baseline is
used.

## 9. Clause-by-clause discharge

| required clause | status | proof location |
|---|---|---|
| geometric parameter for each transported cv vertex is `A^1` | **proved** | Sections 3--4 |
| cyclic quotient is handled without duplication | **proved** | (3.1), Sections 4--5 |
| `(f,g)` restricts to a polynomial value map | **proved** | (4.1)--(4.3) |
| finite punctures partition into direction clusters | **proved** | EW1--EW2, Section 5 |
| no cross-vertex duplication | **proved** | injectivity after (5.2) |
| one reference fibre covers all `a` | **proved** | EW3 and Section 6 |
| weights are constant along a family | **proved** | EW3--EW4, Section 6 |
| constructible pushforward has Euler integral one | **proved** | Section 7 |

## 10. Boundary of the result

The proof depends on the corrected centred and twisted Eggers--Wall facts
EW1--EW4. It does not repair those inputs independently. In particular, if
root realization in EW2 or common-twist transport in EW3 were withdrawn,
surjectivity in (5.3) would become an actual gap.

Subject to those promoted inputs, no further algebraization theorem is
needed: the direction lines are actual divisorial boundary components of
the given global polynomial map, not arbitrary local analytic models.

## 11. Final verdict

```text
RESOLVED-DIRECTION / NO-DUPLICATION LEMMA: PROVED
CONSTRUCTIBLE BASELINE PUSHFORWARD:          PROVED
EULER INTEGRAL PER CV FAMILY:                1
MISSING CLUSTERS:                            NONE
CYCLIC OR CROSS-VERTEX DUPLICATION:          NONE
REPAIRED EQUATION (22-cl):                   PROVED FROM EW1--EW4 + G1--G3
```

This closes the mandatory formalization identified by the hostile review.
