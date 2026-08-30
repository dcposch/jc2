# Binding integration: complete-base cyclic controls and the full etale sandwich

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `37a6f36bdb7a329d39cc5cc3fa10bd2750bbc748`  
Lifecycle: **BINDING INTEGRATION / ALL-FIBRES-IRREDUCIBLE CYCLIC SCOPE**

## 0. Disposition and custody

The different-model GPT-5.5/xhigh review returned
`CONFIRM_WITH_CORRECTIONS`.  Its receipt pins the dedicated adapter to the
exact model slug `gpt-5.5` and reasoning effort `xhigh`; all declared hashes
were independently reproduced before the report was read.  The sealed review
custody is

```text
b587d728c9f0acf8ef7509cf866ec05acef6a01ae7cc27a5aea5a6b3f19461c9
  xmodel/bd-a2-a1-p1-full-sandwich-different-model-review-gpt55-20260830.md
  raw body fd5cfb3608f0ec52bc90717c952e004cf9c018b6eed6ba801586f995d0f88ab9
ca91eaf55e5596831a100cc172ad58ca9b0261222996a314abfae6b1c516a28d
  xmodel/bd-a2-a1-p1-full-sandwich-different-model-review-gpt55-20260830.run.v2
ddd93c028a3c844cfbf37eda449b55a080abb2d0cea322100d87d6c0965a64cb
  xmodel/bd-a2-a1-p1-full-sandwich-different-model-review-gpt55-20260830.log
```

The review confirms the producer, the same-model hostile review, and the
cyclic canonical exclusion, while repairing three custody points: it gives
explicit nonvacuity constructions for `(2,2)` and `(2,4)`, uses Miyanishi
Lemma 2.2(2) rather than purity alone in the exact degree-two argument, and
keeps the canonical calculation inside its all-fibres-irreducible scope.

## 1. Binding maximum theorem

Over `C`, there are smooth affine cyclic `A1`-fibre spaces

```text
rho:X -> P1
```

with every fibre irreducible and with exactly two multiple fibres of
multiplicities `(2,2)`; there are likewise such spaces of type `(2,4)`.
For a `(2,2)` target, Miyanishi Definition 2.5 and Lemmas 2.2(2), 2.6 give a
Galois affine pseudo-covering

```text
A2 -> X
```

of exact generic degree two.  For a `(2,4)` target, Lemma 2.7 gives a
non-Galois affine pseudo-covering of exact generic degree four.  Here an
affine pseudo-covering is an etale morphism whose image contains every
codimension-one target point; it is not asserted finite, proper, or
surjective on all closed points.

Consequently the actual first-leg facts

```text
g_1:A2 -> U etale and almost surjective,   degree(g_1)>1
```

do **not** by themselves exclude a complete-base `A1` ruling on `U`.

On the other hand, every all-fibres-irreducible cyclic `A1`-space with
multiple-fibre pair `(2,2)` or `(2,4)` has

```text
K_X not linearly equivalent to zero.
```

It therefore admits no etale morphism to `A2`, nor to any smooth surface
with linearly trivial canonical class.  The two named controls disprove a
first-leg-only obstruction, but they cannot realize the full sandwich

```text
A2 -> U -> A2.
```

No part of this theorem applies to a complete-base ruling with a reducible
fibre or to an internal row not proved to be a cyclic `A1`-space.

## 2. Nonvacuity of the two named controls

Start with `Sigma_0=P1_t x P1_z`, its projection to `P1_t`, and the horizontal
boundary `M={z=infinity}`.  Choose two distinct fibres and take all blow-up
centres away from `M`.  An outer blow-up is at a smooth point of one current
fibre component; an inner blow-up is at a node of two current fibre
components.  Fibre coefficients transform by copying at an outer blow-up
and by addition at an inner blow-up.

For a double block use

```text
outer on L; inner at L-E1;
outer on the resulting coefficient-two component.
```

The completed fibre has

```text
L+E1+2E2+2F,
L^2=E1^2=E2^2=-2,   F^2=-1,
edges L-E2-E1 and E2-F.
```

Delete `L,E1,E2` and retain `F`.  The open fibre is the irreducible fibre
`2(F minus boundary) ~= 2A1`.

For a quadruple block use

```text
outer on L; inner at L-E1;
outer on the coefficient-two component;
inner at the node of the two coefficient-two components;
outer on the resulting coefficient-four component.
```

The completed fibre has

```text
L+E1+2E2+2A+4G+4F,
L^2=E1^2=A^2=G^2=-2,   E2^2=-3,   F^2=-1,
edges L-E2, E1-E2, E2-G, G-A, G-F.
```

Delete every displayed component except `F`.  The open special fibre is
`4A1`.  Two double blocks give `(2,2)`; a double and a quadruple block give
`(2,4)`.  General fibres are `P1 minus M ~= A1`, so every fibre is
irreducible.

The vertical boundary blocks are negative definite.  In Miyanishi's
ruled-boundary Schur calculation, `n=0,T=M`; the double block has
`(h,alpha)=(3,3/4)`, and the quadruple block has
`(h,s,alpha)=(5,3,11/16)`.  Thus

```text
(2,2): alpha_1+alpha_2=3/2>0,
(2,4): alpha_1+alpha_2=23/16>0.
```

The boundary supports an ample divisor.  Both complements are therefore
smooth affine cyclic `A1`-fibre spaces, closing the former nonvacuity gap.

## 3. Exact degree two

Let `q:A2->X` be the Galois pseudo-covering of a `(2,2)` target, and normalize
`X` in `C(A2)`.  Miyanishi Lemma 2.2(2) gives a connected finite etale Galois
normalization; the input is Galois uniformity over height-one points together
with almost-surjectivity, not purity alone.  Definition 2.5 gives

```text
pi_1(X)=Z/2.
```

Hence the finite etale degree is one or two.  Degree one would make `A2` an
open subset of `X` with finite complement.  Removing finitely many points
from a smooth complex surface does not change its fundamental group, which
would contradict `pi_1(A2)=1` and `pi_1(X)=Z/2`.  The degree is exactly two.

## 4. Canonical exclusion

For an all-fibres-irreducible `A1` ruling over `P1`, Miyanishi's adapted
completion gives

```text
T~M+a*ell,   a=0 or a>=n,
[K_X]=((2a-n-2)+sum_i k_i/m_i)[ell] in Pic(X) tensor Q,
k_i>m_i.
```

If `T!=M`, its free coefficient is strictly positive, so `K_X` cannot be
trivial.  If `T=M`, the exact integral presentation is

```text
Pic(X)=<ell,F_1,F_2 | ell=m_1F_1=m_2F_2>,
K_X=-(n+2)ell+k_1F_1+k_2F_2.                 (4.1)
```

For `(2,2)`, put `ell=2F_1`, `F_2=F_1+t`, `2t=0`.  Triviality would force

```text
h_1+h_2=2(n+2),   h_1,h_2 even and at least four.
```

Thus `n>=2`, whereas the strict affine Schur inequality gives

```text
n<(h_1+h_2)/4=(n+2)/2,
```

hence `n<2`, a contradiction.

For `(2,4)`, put `ell=4F_2`, `F_1=2F_2+t`, `2t=0`.  Triviality would force

```text
h_1 even,   n=h_1/2+k/4-2,   h_1>=4,   k>=8 and 4|k.
```

Every multiplicity-four fibre row in Miyanishi's table satisfies

```text
alpha<=k/4-1.
```

For the multi-branch row this is the positive polynomial check

```text
Q(d,s)=8d^2+8sd-49d-12s+55>0,
d=h-s>=2, s>=3;
Q(2,s)=4s-11,   Q(d+1,s)-Q(d,s)=16d+8s-41.
```

Therefore

```text
h_1/4+alpha <= h_1/2+k/4-2=n,
```

contradicting the strict affine Schur inequality.  This proves the two
canonical exclusions without charging the doubtful printed divisibility
line in the source's later Platonic argument.

## 5. Campaign consequence and successor

The complete-base strategy must use the second leg.  On the actual block
open, `K_U~0` is already forced by `U->A2`; the calculation above is a
consistency filter on a proposed adapted row, not new information about a
genuine `U`.  After canonical triviality, the next cheap necessary condition
is that its nowhere-zero canonical form be exact and decomposable:

```text
f=p^*u, g=p^*v  =>  df wedge dg=d(f dg).
```

This remains one-way.  Exactness does not manufacture `f,g`, and even an
etale pair must still satisfy the fixed rank-three finite-flat cubic algebra
and the F5/different boundary data.

Promoted:

```text
first-leg-degree-only P1 obstruction is false;
(2,2) and (2,4) controls are nonvacuous;
their pseudo-cover degrees are exactly two and four;
both fail the full-sandwich canonical test.
```

Not promoted: exclusion of a reducible-fibre complete-base row, a general
multiplicity classification, existence of an internal block, a polynomial
map, a counterexample, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7787`.
- Body SHA-256:
  `790dd5936a2745380a36d8dbf4789ec64318fd444387ea4ff36fa97a105700b4`.
- Frozen basis: `37a6f36bdb7a329d39cc5cc3fa10bd2750bbc748`.
