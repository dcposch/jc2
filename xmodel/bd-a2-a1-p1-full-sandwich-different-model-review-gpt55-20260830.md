# Different-model hostile review: complete-base controls and cyclic canonical exclusion

Date: 2026-08-30 UTC
Reviewer lane: different-model hostile review for the complete-base `A1` packet
Frozen basis audited: `0f730d0c917b18915b2ef8d9cc80c2a644bf8fbc`

## 0. Verdict

Overall status: **CONFIRM_WITH_CORRECTIONS**.

The main mathematical conclusion is correct and promotion-ready after the
source repairs below:

```text
An etale, almost-surjective first leg A2 -> U of generic degree > 1
does not by itself exclude a complete-base A1-ruling U -> P1.

The named cyclic first-leg controls with multiplicities (2,2) and (2,4)
cannot realize the full etale sandwich, because every such cyclic target has
K_X nontrivial and hence admits no etale map to A2 or to any smooth affine
surface with trivial canonical bundle.
```

Do not apply the cyclic canonical exclusion to complete-base rows with
reducible fibres.  Miyanishi's canonical formula charged here is explicitly
in the all-fibres-irreducible `A1`-fibration setting.

Primary sources checked:

```text
M. Miyanishi, "Affine pseudo-planes and affine pseudo-coverings",
Oberwolfach Reports 2 (2005), Report 19/2005, pp. 1110-1112.
TIB PDF:
https://oa.tib.eu/renate/bitstreams/506cb292-0466-4e6a-9a34-53989f1922e0/download

M. Miyanishi, "Lectures on Geometry and Topology of Polynomials --
Surrounding the Jacobian Conjecture", arXiv:1504.07179, Section 2.5.
https://arxiv.org/pdf/1504.07179
```

The downloaded PDFs match the producer/review receipts:

```text
e35a88d8a33daa64b24b9120bd85aeca0c891869bfa79cdb81ef545a6acfd909
  Oberwolfach Report 19/2005 PDF

ab4eb0cb74e4051e3fb1f702a253d29cb1a658632f11bc6f4b04a8bb9e7daaa4
  arXiv:1504.07179 PDF
```

## 1. First-leg degree obstruction

Status: **CONFIRMED**.

Oberwolfach Definition 2.5 defines a cyclic `A1`-fiber space as a smooth
affine surface with an `A1`-fibration over `P1`, all fibres irreducible, and at
most two multiple fibres.  With two multiple fibres `m_1 F_1`, `m_2 F_2`, the
same definition records that `pi_1(X)` has order `gcd(m_1,m_2)`.

Oberwolfach Lemma 2.6(1)(ii) says that `A2` is a Galois affine
pseudo-covering of a cyclic `A1`-fiber space with two multiple fibres of equal
multiplicity larger than one.  The lemma is conditional on such an `X`; it
does not, by itself, construct the multiplicity row or state an exact degree
for every equal-multiplicity row.

Oberwolfach Lemma 2.7 says that if a cyclic `A1`-fiber space has two multiple
fibres `m_1 F_1`, `m_2 F_2` with `m_1 | m_2` and `m_2/m_1 > 1`, then there is a
non-Galois affine pseudo-covering `A2 -> X` of exact degree `m_2`.

An affine pseudo-covering means: source affine, morphism etale, and image
complement of codimension at least two.  It is not asserted finite, proper, or
closed-point surjective.  Since etale morphisms are open and quasi-finite, and
the image contains all codimension-one target points, these controls match and
exceed the first-leg image strength being tested.  Therefore `d_1 > 1` plus
almost-surjectivity of `A2 -> U` does not exclude a `P1`-base `A1`-ruling.

Source repair: say "Lemma 2.7 gives exact degree `m_2` conditionally on a
cyclic target with those multiplicities"; for the equal row, say "Lemma 2.6
gives a Galois pseudo-covering, and exact degree two in the `(2,2)` case
follows from Lemma 2.2(2) and `pi_1`."

## 2. Non-vacuity custody

Status: **CONFIRMED**.

The non-vacuity issue for the named rows can be pinned by an explicit standard
ruled-boundary construction.

Start with `Sigma_0 = P1_t x P1_z`, projection to `P1_t`, and horizontal
boundary `M = {z = infinity}`.  Choose distinct fibres over two base points
and choose all blow-up centers away from `M`.  Write "outer" for blowing up a
smooth point of one current fibre component, and "inner" for blowing up an
intersection of two current fibre components.

For a double fibre, use the sequence

```text
outer on L,
inner at L-E1,
outer on the resulting coefficient-2 component.
```

The final completed fibre has multiplicity relation

```text
L + E1 + 2E2 + 2F,
```

with self-intersections

```text
L^2 = E1^2 = E2^2 = -2,      F^2 = -1,
```

and edges `L-E2-E1` plus `E2-F`.  Put `L,E1,E2` in the boundary and retain
`F`.  The open special fibre is `2F`, with `F` meeting the boundary once, so
`F minus boundary = A1`.

For a quadruple fibre, use the sequence

```text
outer on L,
inner at L-E1,
outer on the resulting coefficient-2 component,
inner at the two coefficient-2 components,
outer on the resulting coefficient-4 component.
```

The final completed fibre has multiplicity relation

```text
L + E1 + 2E2 + 2A + 4G + 4F,
```

with self-intersections

```text
L^2 = E1^2 = A^2 = G^2 = -2,   E2^2 = -3,   F^2 = -1,
```

and edges `L-E2`, `E1-E2`, `E2-G`, `G-A`, `G-F`.  Put
`L,E1,E2,A,G` in the boundary and retain `F`.  The open special fibre is
`4F`, again an affine line.

Using two double blocks gives a cyclic target with multiplicities `(2,2)`.
Using one double block and one quadruple block gives a cyclic target with
multiplicities `(2,4)`.  General fibres are `P1 minus M = A1`, and the only
special open fibres are the retained `mF` components above, hence all fibres
of the induced `A1`-fibration are irreducible.

Affineness is the same ruled-boundary criterion used in Miyanishi Section 2.5.
Here `n=0`, `T=M`, the vertical blocks are negative definite, and the Schur
complement is `-n + alpha_1 + alpha_2`.  Miyanishi's table gives

```text
double block:     h=3, alpha=3/4;
quadruple block:  h=5, s=3, alpha=11/16.
```

Thus `(2,2)` has `alpha_1+alpha_2=3/2>0`, and `(2,4)` has
`alpha_1+alpha_2=23/16>0`.  The boundary supports an ample divisor, so the
complements are smooth affine cyclic `A1`-fiber spaces.  The named rows are
not vacuous.

## 3. The `(2,2)` exact-degree argument

Status: **CONFIRM_WITH_CORRECTIONS**.

The exact-degree-two conclusion is correct, but purity alone is not the proof.

Let `q:A2 -> X` be Miyanishi's Galois affine pseudo-covering for a cyclic
target with multiplicities `(2,2)`, and let `Xtilde` be the normalization of
`X` in `C(A2)`.  Oberwolfach Lemma 2.2(2) says that `Xtilde -> X` is smooth
and that the Galois group acts freely with quotient `X`; in the arXiv
formulation this is recorded as a finite etale Galois normalization.  The
point is Galois uniformity over height-one points plus almost-surjectivity;
only after divisorial ramification is excluded does purity enter.

Since `pi_1(X)` has order `gcd(2,2)=2`, the connected finite etale Galois
normalization has degree one or two.  Degree one is impossible: then `A2` is an
open subset of `X` with finite complement, and removing finitely many points
from a smooth complex surface does not change the fundamental group.  This
would force `pi_1(X)=pi_1(A2)=1`, contradicting Definition 2.5.  Hence the
degree is exactly two.

Repair the producer prose by replacing "purity makes the finite normalization
etale" with the Lemma 2.2(2) normalization argument above.

## 4. Canonical formula scope and `T != M`

Status: **CONFIRM_WITH_CORRECTIONS**.

The canonical formula is valid in exactly this source setting:

```text
X smooth affine,
rho:X -> P1 an A1-fibration,
all fibres irreducible,
multiple fibres m_i F_i with F_i ~= A1.
```

Miyanishi chooses a smooth completion `V` obtained from `Sigma_n`, lets `T` be
the image of the unique horizontal boundary component, writes
`T ~ M + a ell` with `a=0` or `a>=n`, and writes the canonical divisor as

```text
K_V ~ -2M - (n+2)ell + sum_i(k_i F_i + boundary terms).
```

Then in `Pic(X) tensor Q`,

```text
[K_X] = ((2a-n-2) + sum_i k_i/m_i) [ell|_X],
```

with `k_i > m_i`.

For two cyclic multiple fibres, if `T != M` then one is in the `a>=n` branch
after choosing `M=T` in the `a=0` case on `Sigma_0`.  Therefore

```text
I = 2a-n-2 + k_1/m_1 + k_2/m_2
  > 2a-n
  >= n
  >= 0.
```

Since cyclic spaces have rational Picard rank one, `I != 0` gives a nonzero
free part of `K_X`.  Thus any linearly trivial row must have `T=M`.

For the actual internal block surface, the second leg `U -> A2` already gives
`K_U ~ 0`.  A canonical calculation on a proposed adapted boundary row is
therefore a consistency check for that row, not new information about a
genuine internal `U`.  For the external cyclic controls, by contrast,
`K_X != 0` is a genuine discriminator against the reverse etale leg.

## 5. Picard ledger and parity checks

Status: **CONFIRMED**.

In the `T=M` case, the horizontal boundary kills `M`, and each vertical
boundary block kills all components of the completed special fibre except the
retained `(-1)` component `F_i`.  The remaining integral presentation is

```text
Pic(X) = <ell,F_1,F_2 | ell=m_1 F_1=m_2 F_2>,
K_X = -(n+2)ell + k_1 F_1 + k_2 F_2.
```

Miyanishi's Schur-complement coefficient table gives, for the rows needed
here,

```text
m=2:  k=h,      alpha=h/4.

m=4, one branching vertex and T' adjacent to the (-4)-curve:
      k=h,      alpha=h/16.

m=4, one branching vertex and T' not adjacent to the (-4)-curve:
      k=h+2,    alpha=(h+8)/16.

m=4, more than one branching vertex:
      s>=3, h>=s+2,
      k=h+s-1,
      alpha=((8s-3)(h-s)-(12s-5))/(16(2(h-s)-3)).
```

The arXiv proof contains a doubtful printed divisibility/denominator line in
the later Platonic argument.  It is not needed here; the integral torsion
conditions follow directly from the Picard presentation above.

For `(2,2)`, set `ell=2F_1`, `F_2=F_1+t`, `2t=0`.  Then

```text
K_X = (h_1+h_2-2(n+2))F_1 + h_2 t.
```

If `K_X~0`, then `h_1+h_2=2(n+2)` and `h_2` is even; hence `h_1` is even.
Since `h_i=k_i>2`, both `h_i>=4`, so `n>=2`.  Affineness requires

```text
n < h_1/4 + h_2/4 = (n+2)/2,
```

so `n<2`.  Contradiction.  The boundary case `n=2` gives zero Schur
complement, not an affine positive direction.

For `(2,4)`, set `ell=4F_2`, `F_1=2F_2+t`, `2t=0`.  Then

```text
K_X = (2h_1+k-4(n+2))F_2 + h_1 t.
```

If `K_X~0`, then

```text
h_1 even,
n = h_1/2 + k/4 - 2.
```

Thus `h_1>=4`, `4|k`, and `k>4` gives `k>=8`.  Affineness would require

```text
h_1/4 + alpha > h_1/2 + k/4 - 2.
```

Every `m=4` branch satisfies `alpha <= k/4 - 1`:

```text
alpha=k/16:          holds for k>=8.
alpha=(k+6)/16:      difference is (3k-22)/16 > 0 for k>=8.
```

For the multi-branch row, put `d=h-s>=2`, so `k=d+2s-1`.  Multiplying the
difference `(k/4-1)-alpha` by the positive denominator `16(2d-3)` gives

```text
Q(d,s)=8d^2+8sd-49d-12s+55.
```

At `d=2`, `Q(2,s)=4s-11>0` for `s>=3`, and

```text
Q(d+1,s)-Q(d,s)=16d+8s-41>=15.
```

Hence the estimate is strict throughout the multi-branch family.  Therefore

```text
h_1/4 + alpha <= h_1/4 + k/4 - 1
               <= h_1/2 + k/4 - 2
               = n,
```

contradicting the strict affineness inequality.  The `(2,4)` canonical
exclusion is complete.

## 6. Exact conclusion

Status: **CONFIRMED**.

The correct conclusion is exactly this:

```text
FIRST-LEG-DEGREE-ONLY P1 OBSTRUCTION: false.
CYCLIC (2,2) FULL-SANDWICH TARGET: excluded by K_X != 0.
CYCLIC (2,4) FULL-SANDWICH TARGET: excluded by K_X != 0.
```

The result does not exclude all complete-base internal rows.  In particular,
it does not apply to rows whose `A1`-ruling has reducible fibres, rows not
identified with Miyanishi cyclic spaces, or rows where the adapted completion
and Picard ledger have not been constructed.

## 7. Exact/decomposable volume-form successor

Status: **CONFIRMED**.

If `p:X -> A2` is etale, and `u,v` are coordinates on `A2`, then

```text
df wedge dg = p^*(du wedge dv),      f=p^*u, g=p^*v,
```

is nowhere vanishing and exact, since

```text
df wedge dg = d(f dg).
```

When `O(X)^*=C^*` and `K_X~0`, the global canonical generator is unique up to
scalar, so vanishing of its algebraic de Rham class is a well-defined
necessary condition for a reverse etale map.

This is one-way only.  A linearly trivial canonical class, an exact canonical
form, or even an exact decomposable two-form does not by itself produce
global functions defining an etale map to `A2`.  For the campaign's internal
block, the successor must still impose the actual coordinate pair, rank-two
differential everywhere, and the fixed degree-three finite-flat/F5-different
extension data.

## 8. Promotion-ready maximum theorem

Status: **CONFIRMED**.

Promote the following theorem and no stronger statement:

```text
Theorem.  Over C, there exist smooth affine cyclic A1-fiber spaces
rho:X -> P1 with all fibres irreducible and with two multiple fibres of
multiplicities (2,2), and likewise of multiplicities (2,4).  In the (2,2)
case Miyanishi Lemma 2.6, together with Lemma 2.2(2) and Definition 2.5,
gives a Galois affine pseudo-covering A2 -> X of exact degree 2.  In the
(2,4) case Miyanishi Lemma 2.7 gives a non-Galois affine pseudo-covering
A2 -> X of exact degree 4.  Hence an etale, almost-surjective first leg
from A2 of generic degree greater than one does not exclude the existence of
a complete-base A1-ruling on the target.

For every cyclic A1-fiber space with all fibres irreducible and two multiple
fibres of multiplicities (2,2) or (2,4), the integral Picard presentation

  Pic(X)=<ell,F_1,F_2 | ell=m_1F_1=m_2F_2>,
  K_X=-(n+2)ell+k_1F_1+k_2F_2,

together with Miyanishi's alpha table and the affine Schur inequality
alpha_1+alpha_2>n, implies K_X is not linearly equivalent to zero.  Therefore
none of these named cyclic targets admits an etale morphism to A2, or to any
smooth affine surface with trivial canonical divisor.

No assertion is made for complete-base A1-rulings with reducible fibres, for
unidentified internal boundary rows, for arbitrary multiplicity pairs, or for
the existence of any Keller counterexample.
```

Source repairs required before integration:

```text
1. Attach the ruled-boundary construction above as the non-vacuity pin for
   the named (2,2) and (2,4) rows.
2. State Lemma 2.7's exact degree-four use conditionally on the constructed
   (2,4) cyclic target.
3. State the (2,2) exact degree-two proof via Lemma 2.2(2), Galois uniformity,
   pi_1, and the finite normalization; do not cite purity alone.
4. State the canonical formula only under the all-fibres-irreducible
   hypothesis.
5. Treat internal `K_U~0` as a consistency constraint already forced by the
   second leg, while treating external `K_X!=0` as the discriminator that
   excludes the named cyclic controls from the full sandwich.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14386`.
- Body SHA-256:
  `fd5cfb3608f0ec52bc90717c952e004cf9c018b6eed6ba801586f995d0f88ab9`.
- Frozen basis: `5f285393f481bfb8f8767fa0ad09b1eeeb1d9f91`.
