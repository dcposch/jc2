# No homogeneous Hamiltonian slice on the exact pseudo-plane

INTERNAL / PRODUCER-CHECKED BY MANUAL ALGEBRA / DIFFERENT-MODEL REVIEW REQUIRED.
ROOT, 2026-09-11. This is a scoped new candidate lemma, not a JC2 proof, a
pseudo-plane-to-plane exclusion, or a computation. Publication preparation
first recorded07:42:45UTC; original reserve07:50/HARD07:52, no reset.
The earlier exploratory reading and desk derivation preceded this publication
transaction. No source, mathematical code or candidate search was executed.

## 1. Exact statement and sufficient counterexample interface

Let k be any field of characteristic zero and
```
R = k[A,U,Z]/(U^2-A-A^2 Z),
wt(A)=2, wt(U)=1, wt(Z)=-2,
{A,U}=2A^2, {A,Z}=4U, {U,Z}=2+4AZ.
```
The bracket is a biderivation. It respects the relation and satisfies Jacobi:
the generator Jacobi sum is 16AU+0-16AU=0. The relation is homogeneous
of weight2, and the bracket has weight+1. "Homogeneous" below refers to
this exact integer grading of this exact ring, not to an initial form.

**Candidate theorem.** For every homogeneous H in R and every G in R,
`{H,G}` is not a nonzero scalar. Thus no homogeneous Hamiltonian has
a regular slice, even when its Hamiltonian derivation is not locally finite.

This is broader than just H in k[A]. It includes, in particular, U and Z,
whose Hamiltonians need not be locally finite. It does NOT say that an
arbitrary H can be replaced by its leading homogeneous term in a
constant-bracket equation.

The relevance is literal, without a source-coverage assertion. There is a
polynomial map from the affine plane to Spec R given by
```
A=x^2, U=x+x^3 y, Z=2y+x^2 y^2.
```
Substitution gives U^2=A+A^2Z, and the three ordinary (x,y)-Jacobian
brackets are respectively 2A^2,4U,2+4AZ. Hence any F,G in R with
{F,G}=c in k* would give a polynomial Keller pair after pullback.
The distinct points (1,0) and (-1,-2) have the same triple (1,1,0);
therefore that pair would not be injective. This is a sufficient
counterexample endpoint, but NO such F,G is supplied. The theorem rules
out only endpoints with at least one homogeneous coordinate.

## 2. Homogeneous reduction of a hypothetical slice

R is free as a k[A,Z]-module with basis1,U, by monic division in U.
Every element therefore has a unique normal expression
`P(A,Z)+U Q(A,Z)`. Homogeneity of the defining relation makes the
quotient a direct sum of its integer-weight spaces, and each element has
only finitely many weights.

If H has weight w and {H,G}=c!=0, decompose G by weight. Since the bracket
has weight+1, its weight-zero component gives the exact equation
```
{H,G_(-w-1)}=c.
```
All other components have different weights; they cannot contribute to c.
Thus the mate may be taken homogeneous of weight -w-1. This argument
requires H itself homogeneous; it is not valid for a mixed H.

## 3. The fixed point leaves only two weights

The k-rational point o=(A,U,Z)=(0,0,0) lies on Spec R. In its cotangent
space the relation has linear term -A, so
```
m_o/m_o^2 = k U + k Z
```
with weights1 and-2. At o the bracket on these tangent coordinates is
{U,Z}(o)=2. A scalar nonzero bracket forces the differential of each
coordinate to be nonzero at o. For a homogeneous H its differential
can therefore be nonzero only for w=1 or w=-2. If w=0, its possible
constant term contributes no differential. All other weights fail at o.

Interchanging H and its homogeneous mate changes only the sign of c.
It is consequently enough to consider H of weight1 and G of weight-2.

## 4. Exact weight spaces and the final polynomial obstruction

Put t=AZ. Monic normal form and the weights give exactly
```
R_1=U k[t],       R_(-2)=Z k[t].
```
Indeed a monomial A^i U^epsilon Z^j has weight2(i-j)+epsilon with
epsilon=0 or1. Weight1 forces epsilon=1,i=j; weight-2 forces
epsilon=0,j=i+1. Therefore write
```
H=U f(t),       G=Z g(t),       f,g in k[t].
```
Neither f nor g can be zero in a hypothetical scalar-bracket pair.
The elementary identities
```
{U,t}=2U^2,       {t,Z}=4UZ,       U^2 Z=t(1+t)
```
give, with primes denoting derivatives in t,
```
{U f(t),Z g(t)}
 =2[(1+2t) f g + 2t(1+t) f' g + t(1+t) f g'].
```
For n=deg f,m=deg g, the coefficient of t^(n+m+1) is exactly
```
2(2+2n+m) lc(f) lc(g).
```
It is nonzero in characteristic zero, and n+m+1>=1. Thus the displayed
bracket is nonconstant. Here k[t] embeds into R: k[A,Z] embeds by the
same monic normal form, and AZ is transcendental over k. A positive
t-degree cannot disappear in the quotient. This contradicts c and
proves the candidate theorem.

## 5. Coordinate corollary and explicit firewalls

If F,G in R formed a constant-bracket pair, no coordinate of that pair
could become homogeneous after a polynomial automorphism of the TARGET
affine plane. Such a target change has a nonzero scalar Jacobian and
would produce another constant-bracket pair in R, contradicting the
theorem if its first or second coordinate were homogeneous.

This does not assert that a target change making a coordinate homogeneous
exists. It does not classify mixed/mixed Hamiltonians, arbitrary rational
involutions, any actual Keller map, or the unbounded plane conjecture.

The regularity boundary is essential. In R[A^-1], direct differentiation
gives
```
{A,U/(2A^2)}=1.
```
The second entry is not in R. At the prime P=(A,U), Z is a residue
coordinate, U has order1 and A has order2 (the factor1+AZ is a unit);
hence U/(2A^2) has pole order3. The two Laurent entries are homogeneous
of weights2 and-3. This countercontrol defeats any claimed version
that omits regularity at A=0.

Another check is f=g=1: {U,Z}=2+4t, not2. Evaluation at the fixed point
alone would miss its nonconstant part. No completeness or local-finiteness
claim is inferred from the fixed point; the exact polynomial bracket is
what eliminates its remaining two weights.

## 6. Campaign composition, history and next test

The construction interface is already known in the campaign; this report does
not claim its invention or a literature novelty. The bounded history search
found the exact pseudo-plane, its Poisson bracket, the ruling-aligned
obstruction, locally-finite Hamiltonian theorem and wild/mixed safeguards.
It did not locate the exact all-homogeneous no-slice statement. The following
old reports are CONTEXT, not unchecked proof dependencies of Sections1-5:

- xmodel/block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md
  cd27b7f6687103fae0fc4e5fe19772e0f8e62939d73a655ebf04e57905ddba05.
- xmodel/block-descent-a1-one-cusp-poisson-hostile-review-grok46-20260831.md
  d154a30379335970719b1ea2f2f942118e995ac643feec4aebc9461e1d1ee7fb.
- xmodel/block-descent-a1-quartic-cycle1-ruling-aligned-log-jacobian-obstruction-sol56-20260830.md
  985f66316961ddd8555ae96516cadef0cba26c30854f4bdc99a157a06dc5f045.
- xmodel/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
  2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5.

ROOT read selected ranges/text searches of these BEFORE recording their
current hashes; this was exploratory historical reading, not a fresh frozen
WHOLE intake. No whole-proof re-review of their imported surface theorems
is asserted. The self-contained candidate above needs only the displayed
ring, bracket, elementary normal form and characteristic zero.

Theorem-interface composition: a potential two-function construction on this
exact R is a sufficient disproof route; the candidate forbids its homogeneous
coordinate and all target-coordinate-equivalent versions. It does not rule
out mixed/mixed functions or supply a new source. This is a scoped
construction constraint, not a global route reranking or full ideation round.
No F10 source, guard, coefficient or accepted scope changes.

The immediate open QUANTITY is whether Sections1-5 survive one different-model
hostile review. CHEAPEST TEST: Fable5.1 static manual review of this complete
proof, approximately10minutes UNMEASURED planning time, hard publication cap
to be fixed before launch. Check grading, fixed-point cotangent weights,
both remaining weight spaces, the leading coefficient, exact pullback
collision, and rational-pole countercontrol. REFUTED/GAP narrows or rolls
back only this candidate; CONFIRMED can promote this exact obstruction,
not the mixed case. No symbolic subprocess, local scientific validation,
AWS allocation, uniform mixed theorem, degree farm or code implementation is
authorized here. There is no new canonical OPEN identifier.

## COLLISIONS

Documentary target check: both prospective owned final report and own box
were absent before begin. The bounded canonical/text history search above
found the old related mechanisms and no exact matching statement. This
manual search is not exhaustive novelty certification. All mathematics in
this report is manual; no mathematical artifact or source was executed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8872`.
- Body SHA-256:
  `5b902bf2160b41b52f7dbef72cecd1a1ddfb99daa0d83190151ab4cf6aa690b2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
