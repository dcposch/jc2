# Independent review and sharpening: exact-pair L5 by reduced denominator

**Date:** 2026-08-28  
**Lane:** independent Sol Ultra sibling audit  
**Target:** `g2-intrinsic-exact-pair-l3-l5-newton-puiseux-sol-ultra-20260828.md`  
**Verdict:** **PASS for the intrinsic exact-pair theorem; operational REPAIR
required for the meaning of a finite terminal leaf**

This is an independent local-field derivation, not a different-model review.
An attempted Fable 5 cross-check stopped before inference because the account
usage limit had been reached.  No producer `PASS` token is evidence below.

## 0. Frozen inputs and headline

Hashes recomputed before the audit:

```text
841c848eb98aa234fe6429006b3f84958c042869db395d61f2394a6c6c7c81d0
  xmodel/g2-intrinsic-exact-pair-l3-l5-newton-puiseux-sol-ultra-20260828.md
968b42ced94bd6c59b33bfdab30677e2ad6ad91a349fc978a271c01083d11e7d
  xmodel/g2-c74-place-exit-rpmc-hostile-review-opus5-20260827.md
f7de3ae12918c9103d595e81ddc7fcb9082ba950698f70966ade3ea576cc79a1
  xmodel/g2-psc-typed-source-to-pole-tree-interface-hostile-review-opus5-20260827.md
99db1854d03e78ce8e1a57b3ff79ebcd9b12bf7a4a60359be8504a2ffe2d2153
  ladder/REDUCTION.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
```

The target's three numerical assertions are correct.  If `u=t^kappa` and a
complete leaf is

```text
phi(t)=sum_m c_m t^m,
g=gcd(kappa,{m:c_m!=0}),
```

with `g=kappa` for the zero/constant-support case, then

```text
least denominator = ramification e = kappa/g,
|Stab_mu_kappa(phi)| = g,
|Orb_mu_kappa(phi)| = e.
```

Complete leaf orbits in one chart biject the normalized places in that chart.
Applying the result to both disjoint charts of Sigray Statement 3.1 closes
**intrinsic exact-pair L5**.  It does not show that any finite VGG corridor
leaf is complete, terminal, or even an actual fibre truncation.

The older L5 wording in the Opus C74 review needs correction: the reduced
branch denominator need not equal the ambient/cumulative Kummer index `l'`.
It divides `l'`, and equality holds exactly when the leaf stabilizer is
trivial.  Quotienting by that stabilizer is the point of the theorem.

## 1. One-chart theorem, in its narrowest form

Let `K` be algebraically closed of characteristic zero.  Let `C` be a reduced
plane curve and let `C_i` range over its irreducible components.  Normalize
the projective closures.  Put `u=1/x`, and let `B_x` be the normalized points
`S` at which `u` has a zero and `y` is regular.  Write

```text
e_S=ord_S(u)>0.
```

Choose `kappa` divisible by all `e_S`, put `u=t^kappa`, and take **all**
bounded Puiseux roots of the nonvertical factors, with their component and
ancestor labels.  Then:

1. every complete root has reduced denominator `e_S` for a unique `S`;
2. its `mu_kappa` stabilizer has order `kappa/e_S` and its orbit has order
   `e_S`;
3. the orbit-to-`S` map is a bijection, component by component; and
4. the same statement holds after swapping `x` and `y`.

For finite data, “complete root” may be replaced by an exact local factor
plus a prefix that separates it from every other root, including its deck
conjugates.  An arbitrary finite prefix is only an ancestor and is not in the
domain of the leaf/place bijection.

## 2. Local primitive-element and denominator audit

Fix `S in B_x` on a component `C_i`.  The rational function `x` is
nonconstant on `C_i`, so the normalized projective map

```text
x : C_i^nu -> P^1
```

is finite.  Put `F=K((u))`.  Since the plane coordinates generate the
component field,

```text
K(C_i)=K(x)(y).
```

If `m_i(Y)` is the minimal polynomial of `y` over `K(x)`, completion at
`u=0` gives the standard separable product

```text
F[Y]/(m_i) = product_(T over x=infinity) K((z_T)).
```

Projection to the `S` factor sends `Y` to the local series `phi_S(z_S)`.
It follows, rather than being assumed, that

```text
F(phi_S)=K((z_S)).
```

This closes the possible local-primitive-element gap in the producer's
Section 2.1.

Because `K` is algebraically closed, the residue degree is one.  After taking
an `e_S`-th root of the local unit, a uniformizer can be chosen with

```text
u=z_S^e_S,
[K((z_S)):F]=e_S.
```

Write `phi_S(z)=sum_n b_n z^n`.  If
`d=gcd(e_S,{n:b_n!=0})>1`, then `phi_S` lies in the proper fixed field
`K((z_S^d))`, contradicting `F(phi_S)=K((z_S))`.  Hence that gcd is one.
Equivalently, the least common denominator of the exponents `n/e_S` is
exactly `e_S`.  This proves both the denominator assertion and its
load-bearing hypothesis: it uses the actual plane coordinate `y`, not an
arbitrary function on the branch.

## 3. Kummer orbit and stabilizer audit

Write `kappa=e_S q`.  The normalized base change of the local equation is

```text
z_S^e_S=t^(e_S q),
z_S=xi*t^q,                  xi in mu_e_S.
```

Thus the `e_S` presentations above `S` are

```text
phi_(S,xi)(t)=sum_n b_n xi^n t^(qn).
```

The map `mu_kappa -> mu_e_S`, `zeta -> zeta^q`, is onto with kernel of
order `q`.  It acts transitively on these presentations.  The gcd-one result
in Section 2 says no larger subgroup fixes a presentation.  Therefore

```text
orbit size=e_S,  stabilizer size=q=kappa/e_S.
```

For an arbitrary displayed support in the common `t` coordinate this is the
equivalent formula

```text
g=gcd(kappa,{m:c_m!=0}),
Stab={zeta:zeta^m=1 for every supported m},
|Stab|=g,  |Orb|=kappa/g.
```

Galois correspondence also gives the useful exact field identity

```text
K((u))(phi)=K((t^g)).
```

So the cumulative Kummer index is presentation capacity, not automatically
ramification.  The intrinsic index is the orbit size after stabilizer
quotient.

## 4. No collisions, reducible fibres, vertical components, and charts

The normalized base change projects back to the original normalization.
Deck transformations act over `u` and leave this projection fixed.  Hence an
orbit cannot move between two original normalized points.  Conversely,
Section 3 proves transitivity on all presentations above one point.  This is
the claimed bijection.

For reducible squarefree `h`, apply the argument to every irreducible factor.
Each factor is deck-invariant after substituting `u=t^kappa`; coprime factors
have no common complete root.  Thus neither a deck transformation nor an
accidental equality of series can cross component labels.

An irreducible component on which `x` is constant is the vertical line
`x=c`.  After `x=t^-kappa`, its factor is a unit in the `y`-polynomial over
`K((t))`, so it contributes no `x=infinity,y=finite` root.  Its boundary
point has `y=infinity,x=c` and is recovered in the swapped chart.  Horizontal
lines have `x` nonconstant and are included here with `e_S=1`; the analogous
statement after swapping handles the opposite orientation.  For the
normalized Keller fibre, the two
chart sets are disjoint by the “exactly one” in Sigray Statement 3.1, so
their union creates no cross-chart duplication.

Squarefreeness is essential for the literal multiplicity count.  A
nonreduced equation such as `(Y^2-u)^2` has the same normalization places but
doubles polynomial multiplicities.  Keller fibres meet the hypothesis:
`df wedge dg` constant implies `df` is nowhere zero, so every fibre is smooth
and reduced, even if it is disconnected.

## 5. Prefixes, terminal precision, and ancestor custody

Sigray Proposition 3.1 counts **base-changed Puiseux presentations**, not
original normalized places.  On a common `kappa` grid it says:

```text
degree of the residual = number of roots extending the old prefix,
root multiplicity      = number of roots extending the new prefix.
```

This validates all-root recursion and strict truncation for the intrinsic
algorithm.  The Kummer quotient in Sections 2--4 is still required to turn
those presentations into places.

There is a finite, exact operational terminal condition.  If `R` is the
finite set of distinct complete roots, choose `N` strictly greater than every
finite contact order

```text
ord_t(phi-psi),          phi!=psi in R.
```

Then truncation below `N` separates all roots.  In particular, a deck element
fixes a truncated root if and only if it fixes the full root, so the support
gcd and orbit size are already final.  One may store the original exact
factor together with this isolating prefix instead of printing infinitely
many coefficients.

Before that condition, a node is an ancestor cluster.  Its prefix stabilizer
can be strictly larger than its leaf stabilizer and its reduced denominator
can be strictly smaller.  Several eventual place orbits may share the node.
Therefore:

- retain every residual root, zero roots included;
- retain the component, chart, parent, and full ancestor path of each child;
- let `mu_kappa` act on the decorated path, not on a detached root token;
- quotient/count only complete or separating terminal records; and
- never use an unfinished VGG leaf in a lower-bound place sum.

This is the exact guard needed by the finite-end/passport validator.

## 6. Two controls

### 6.1 Oversized Kummer cover

Over `K((u))`, `Y^2-u` has one normalized place of ramification two.  On the
ambient cover `u=t^4` its presentations are `t^2` and `-t^2`.  They form one
`mu_4` orbit of size two with stabilizer size two:

```text
kappa=4, support={2}, gcd=2, reduced denominator=2.
```

Thus “reduced denominator equals ambient `l'`” is false; the corrected
orbit/stabilizer theorem is exact.

### 6.2 Premature truncation

For any `N>=2`, the squarefree polynomial

```text
(xy-1)(x^N*y-x^(N-1)-1)
```

has two `x=infinity,y=finite` normalized places with local roots

```text
y=u,       y=u+u^N,       u=1/x.
```

Their prefixes below exponent `N` coincide, but `kappa=1`, so they are two
distinct singleton deck orbits.  Treating the common prefix as a terminal
leaf merges two places.  This is a control against assuming that the VGG
corridor has reached a terminal place.

## 7. Verdict on the frozen producer

| Charge | Verdict | Reason |
|---|---|---|
| least denominator `=e_S` | **PASS** | completion product proves the plane `y` generates the local factor |
| stabilizer `kappa/e_S`, orbit `e_S` | **PASS** | explicit tame base change and support-gcd calculation |
| distinct-place collision | **PASS** | deck action is over the original normalization; component factors stay tagged |
| reducible/vertical scope | **PASS** | componentwise normalization; vertical factor absent in this chart and present after swap |
| Proposition 3.1 use | **PASS with scope precision** | it counts presentations on a common cover, exactly as the producer says before quotienting |
| finite stored leaf | **REPAIR** | require an exact local factor plus an isolating/separating prefix, not merely an unspecified finite prefix |
| intrinsic/hybrid firewall | **PASS** | producer explicitly leaves VGG `H-TRUNC` and source coverage open |

The first sentence needing operational precision is in Section 2.3:

> “Once distinct leaves separate, Hensel lifting supplies their unique
> algebraic continuations; the finite leaf may store that exact factor rather
> than an infinite coefficient list.”

Smallest repair: define the stored record as `(exact local factor, prefix
cutoff N)` and require `N` to exceed every contact with every other complete
root, including deck conjugates.  The theorem as stated for **complete
Puiseux leaves** is already correct; no formula changes.

## 8. Campaign status and firewall

The clean ledger split is:

```text
L3-exact  all-root prefixes are actual fibre truncations       AVAILABLE
L4-exact  both intrinsic charts cover all boundary places      AVAILABLE
L5-exact  terminal deck orbits biject normalized places        AVAILABLE

L3-hybrid VGG selected translations equal fibre truncations    OPEN
L4-hybrid VGG/source leaves cover both charts                   OPEN
L5-hybrid an uncertified source leaf is a terminal place        OPEN/ILL-TYPED
```

Accordingly, exact-pair leaves carrying the terminal certificate above may
now be deduplicated safely in place budgets.  Provisional research can run in
parallel with ancestor construction, but a node may enter a refutation-grade
place sum only after terminal certification.

Nothing here proves repaired Sigray ancestor decorations, Proposition 4.2's
constant-leading-part existence, landing, `RPMC(C)`, a degree ceiling, a
Keller contradiction, or JC2.

## 9. Desk replay

Artifact:

```text
cases/g2_intrinsic_exact_pair_l5_reduced_denominator_20260828/verify.py
```

Run:

```text
python3 -B cases/g2_intrinsic_exact_pair_l5_reduced_denominator_20260828/verify.py
```

The standard-library checker exhausts all `8190` support subsets modulo
ambient indices `1..12`, then checks both controls above.  It tests only the
finite cyclic-group arithmetic; Sections 2--5 are the mathematical proof.

No heavy computation was run, and no canonical ledger or frozen producer
byte was modified.
