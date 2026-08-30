# Binding integration: ADE-decorated quadratic boundary/different threat map

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen integration basis: `4ad2fe75f074726bf6d64ade07da17ea1ea02771`  
Lifecycle: **PROMOTED NECESSARY-DATA THEOREM / GLOBAL EFFECTIVITY OPEN**

## 0. Verdict, custody, and scope

This integration binds the transactional producer

```text
ab10ea83f443c93bdb87194ad0e42fe2c442984ba821c3ddf8ddf5cc3f796133
  xmodel/bd-a2-ade-decorated-boundary-different-threat-map-sol56-20260830.md
  body 19667 / 5a1985f48f6b61d4f12b288942b3bbb753b45f3e18a6e31b85cbc077ccd8e2ef
  manifest 9404a4f13e60cf4f40ec45b12a3b5cff81b5c431fdfd96a49e604d5f40e717c8
```

to the independent GPT-5.5 xhigh hostile review

```text
2c7059e5a302f7b117723fd2a8486a7fd048e9c5230c03530fdcb3b2fdbff277
  xmodel/bd-a2-ade-decorated-boundary-different-threat-map-hostile-review-gpt55-20260830.md
  verdict CONFIRM_WITH_CORRECTIONS.
```

The producer was sealed on dependency basis
`dca72076aa1615b0b1286fd4428a1acac7b65963`, committed at
`986427df23c30375b6edfd659ba8a6c6139434ab`, and reviewed on exactly that
publication basis.  The review receipt was root-hash-checked and committed
before the present integration basis.  Its properness, carrier, and
effectivity corrections are binding below.

This theorem charges the normal-singular quadratic reduction integration
`17f41e706bcae7556cd99e019263e7fad254201fe51f9a24ed158b2be68560c6`.
Thus `X` is an irreducible normal class-`2A+3B` hypersurface, its minimal Du
Val resolution `r:Xtilde->X` is rational, the exceptional root lattice embeds
in the actual geometric `D9(-1)` complement of `ZA+ZB`, and the total
resolved source different is `R=r^*R_X~2A+B`.

## 1. Promoted connected-type classification

In signed coordinates

```text
R(D9)={+-e_i+-e_j : i!=j}.                            (1.1)
```

For a connected simple-root set, form the graph on used coordinate positions.
After switching coordinate signs along a spanning tree, all tree edges are
differences and generate `A_(s-1)`.  Any additional balanced edge remains in
that lattice; one unbalanced edge enlarges it exactly to

```text
D_s={x in Z^s : sum x_i is even}.                     (1.2)
```

There is no exceptional third case.  Hence every connected exceptional
Dynkin component embedded in `D9` is exactly one of

```text
A1,...,A8,       D4,...,D9.                           (1.3)
```

This excludes `A9,E6,E7,E8` as embedded root subsystems, not merely as a
chosen diagram presentation.  Full-rank disconnected embeddings additionally
obey the necessary determinant square condition
`det Lambda=4[D9:Lambda]^2`; no primitivity is assumed.

## 2. Exact local Cartier semigroups

At one connected ADE tree let `C` be its positive Cartan matrix, write

```text
R=R_str+sum_i m_iE_i,       m_i>=1,
n_i=R_str.E_i>=0.                                      (2.1)
```

Because the total Cartier pullback is orthogonal to every exceptional curve,

```text
n=Cm.                                                   (2.2)
```

The exact numerical classification is

```text
n in Z_(>=0)^r minus {0},       n in C Z^r,
m=C^(-1)n in Z_(>0)^r.                                  (2.3)
```

Strict positivity of `m` follows from the strictly positive inverse Cartan
matrix; it is not an extra nonnegativity hypothesis.

For `A_r` with chain numbering, integrality is exactly

```text
sum_(i=1)^r i n_i = 0 mod (r+1),                       (2.4)
```

and

```text
m_j=((r+1-j) sum_(i<=j) i n_i
     +j sum_(i>j)(r+1-i)n_i)/(r+1).                    (2.5)
```

For `D_r`, number the chain `1--...--(r-2)` with spin vertices `r-1,r`, put
`a=n_(r-1)`, `b=n_r`, and `T_0=sum_(i=1)^(r-2)i n_i`.  Integrality is exactly

```text
a=b mod 2,
2T_0+(r-2)a+r b=0 mod 4,                               (2.6)
```

with

```text
m_j=sum_(i=1)^(r-2) min(i,j)n_i+j(a+b)/2,
m_(r-1)=T_0/2+r a/4+(r-2)b/4,
m_r    =T_0/2+(r-2)a/4+r b/4.                          (2.7)
```

These are necessary Cartier-lattice data, not an analytic or effective
existence theorem.  They kill no type by themselves: for every vertex a
suitable multiple of `e_i` gives an infinite ray.  Indeed every type in
(1.3) has a formal one-physical-germ survivor with `sum n_i<=2`:

```text
A_(2k-1): n=2e_k;
A_(2k):   n=e_k+e_(k+1);
D_r:      n=e_2.                                      (2.8)
```

## 3. Conditional global caps

For a Cartier slice `L` through a singular point, write

```text
r^*L=L_str+ell E,       r^*R=R_str+mE,
n=Cm.                                                     (3.1)
```

Exact expansion leaves one exceptional contribution:

```text
L.R=L_str.R_str+sum_q ell_q^t n_q.                       (3.2)
```

Therefore, only when the named intersections are proper and share no curve
component,

```text
target line: A.R=8  => sum n_i<=8;
B-fibre:    B.R=4  => sum n_i<=4;
infinity:   H.R=8  => sum h^t n<=8,                       (3.3)
```

where `r^*H=H_str+hE` in the last line.  The coefficient vectors of a local
function are componentwise positive; the Du Val fundamental cycle can give a
stronger row weight but eliminates no connected type.  Projective finiteness
permits a target line avoiding different components.  A common
nonexceptional `H/R` carrier, a different component contained in the chosen
`B`-fibre, coefficient basepoints, or other nonfinite behaviour removes the
corresponding cap; it is not a large capped row.

Thus (3.3) produces literal finite local numerical/combinatorial sets in its
declared regimes.  It does not produce finitely many effective divisors,
analytic germs, incidence equations, finite maps, or polynomial maps.

## 4. Physical germs and the forest test

Numerical entries and support of `n` are not boundary edges.  One tangent
branch can contribute `n_i>1`; one branch through an ADE node can contribute
to both adjacent entries.  Both remain one physical joining path after
embedded resolution.

The exact connector rule is graph-theoretic.  Include the ADE tree and every
local contact-resolution vertex in one tree `T_p`.  A connected component of
the outside resolved boundary may attach to `T_p` at at most one edge; two
attachments, joined inside both connected pieces, make a cycle.  Contacts on
different outside carriers connected only through `T_p` form a star and do
not.  Common `H/R` carriers change the graph and must be handled separately.

The formal patterns (2.8) show that neither Cartan positivity, the conditional
caps, nor this correctly typed local forest rule eliminates any connected
type in (1.3).

## 5. Exact finite successor and firewall

The next finite layer in the capped regimes is numerical and combinatorial:

1. enumerate multisets of connected types of total rank at most nine;
2. enumerate simultaneous root-lattice embeddings in `D9` modulo `W(D9)` and
   component diagram automorphisms, applying the full-rank determinant gate;
3. allocate the global cap among the exact local semigroups;
4. where licensed, enumerate positive paired infinity vectors `(h,a=Ch)` with
   total `sum h^t n<=8`;
5. partition each bounded vector into physical contacts and carrier labels,
   then apply the resolved connector graph;
6. only then test strict carrier classes for effectivity in the actual
   nine-blowup ruled marking and ask for analytic incidence realization.

The active local Cartan enumerator is a first sublayer only; its counts are
not charged by this integration.  Even after the numerical rows are finite,
effectivity and local analytic realization are predicates with moduli, not a
finite construction of curves or maps.

Common-carrier, slice-contained-different, projective-basepoint, and other
nonfinite strata remain separate because (3.3) is unavailable there.  This
integration says nothing about nonnormal incidences, arbitrary quadratic
basis coverage, higher coefficient degree, polynomial maps, counterexamples,
or JC2.  It promotes necessary data and a finite capped threat-list protocol,
not occurrence, attainment, or a solution.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8023`.
- Body SHA-256:
  `106b48088d2bba5132b15744a7e8247562453da9299b49663cbb4e3791e97cfb`.
- Frozen basis: `4ad2fe75f074726bf6d64ade07da17ea1ea02771`.
