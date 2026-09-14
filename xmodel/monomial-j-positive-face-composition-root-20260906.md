# Positive-face Euler composition for polynomial monomial-J receivers

2026-09-06, Astra coordinator. PROVISIONAL, external-GGV-theorem dependency.
This is a post-collection composition of the Astra pole-removal proposal and
Fable's face-factor screen, not a blind discovery and not a receiver exclusion.

## Exact statement

Let K have characteristic zero, P,Q in K[g,p], and [P,Q]=c*g^k with c nonzero
and k>=0. Put l=k+1. For any primitive positive integer direction (r,s), let
R=ell_(r,s)(P), assuming its weight d>0. Then there exists E in K[g,p] with

    weight_(r,s)(E)=l*r+s,       [E,R]=g^k*R.

The endpoint alternatives inherited from GGV have exceptional point (l,1),
not (1,1). For a nonmonomial face, write its univariate face factor after
removing its endpoint monomial as p0(z), p0(0)!=0,
z=g^(-s/r)*p (in the needed Puiseux extension). Its distinct nonzero roots
over an algebraic closure number at most floor((l*r+s)/s).
Axes/removed monomial factors are NOT included in that count.

In particular, for source weight (1,l), equivalently weight (1,1) after
t=g^l, the bound is TWO nonzero roots. This does not assert a global support
rectangle, bound actual total degrees, or identify any forced receiver face.

## Proof, with the source/non-source distinction explicit

Use t=g^l, Pbar=P(t^(1/l),p), Qbar analogously in K[t^(+/-1/l),p].
The bracket is c/l. A primitive positive integer multiple of direction
(l*r,s) in (t,p) selects exactly the original (r,s) face.
GGV1 Theorem2.6 supplies its Laurent Euler element F, with [F,Rbar]=Rbar
and weight l*r+s before primitive rescaling. Pull back and divide by l:
E=F(g^l,p)/l lies in K[g^(+/-1),p], has weight l*r+s, and

    [E,R]_g,p = g^(l-1)*R.

This uses GGV's Laurent existence, NOT its ordinary-polynomial clause.
The full original pair licenses that invocation; a truncated face alone
would not. The imported theorem's upstream [8] Lemma2.2 remains external.

Here is the missing polynomiality step. Since r,s>0, any fixed g-exponent
of a homogeneous polynomial has only one possible p-exponent. Let the
least g-exponent of E be u with term a*g^u*p^v. If u<0, its positive weight
forces v>0. Let the least g-exponent of R be h with term b*g^h*p^j.
Because R is an actual polynomial positive-weight face, h,j>=0 and they
are not both zero. The bracket's coefficient at its least possible
g-exponent u+h-1 is

    a*b*(u*j-v*h)*p^(v+j-1),

which is nonzero: u*j-v*h<0, and v+j-1>=0. Only the two least-g terms can
contribute at this exponent, so no other pair cancels it. But the right side
g^k*R starts at exponent k+h>u+h-1. Contradiction. Hence u>=0 and E is
polynomial. This also handles a pure-g monomial face; no unsupported
nonconstant-in-p assumption is needed in that case.

It follows from nonnegative g-exponents that deg_p(E)<=floor((l*r+s)/s).
Return F=l*E(t^(1/l),p); it still has nonnegative t exponents, although not
necessarily integral t exponents. GGV Proposition2.11(1), in its stated
Laurent/Puiseux ring and positive direction, says every irreducible factor
of the nonzero-constant face factor p0 divides the separable univariate
factor f0 of F. The degree of f0 is the difference of endpoint p-exponents,
hence at most deg_p(F)=deg_p(E). This proves the nonzero-root bound.
No polynomial-only clause2.11(4) or minimal-pair assumption is imported.

GGV endpoint alternatives transport under the invertible diagonal exponent
map (a,b)->(l*a,b), which preserves alignment and oriented endpoints; the
exceptional (1,1) becomes (l,1). They belong to the same supplied F/E,
which was proved polynomial without replacement.

## What the blind objection does and does not refute

Fable's count from the Laurent weight line ALONE is false:
t^(2-b)*p^b has weight2 for every integer b>=0 at (1,1).
Astra's pole argument supplies the missing source-polynomial restriction.
Thus the finite bound has a potential repair for the stated polynomial
receivers; it remains false for arbitrary Laurent Euler data.
The monomial count is at most N+1, whereas the relevant univariate degree
bound is N, N=floor((l*r+s)/s). At constantized (1,1), N=2.

Actual changed-ring control at k=0,r=s=1:

    R=g^-3*(p^3-g^3)^2,
    E=(g^-2*p^4-g*p)/3,
    [E,R]=R.

The nonzero face factor (z^3-1)^2 has three distinct roots in char0, and E
has p-degree4. R is NOT polynomial in g. This is an Euler counter-control,
not a claimed Laurent Keller pair or counterexample to JC2.

Positive sharpness at Euler-identity level for k=1,r=1,s=2:

    R=(p-g^2)*(p-2*g^2)^2,
    E=(p-g^2)*(p-2*g^2)/2,
    [E,R]=g*R.

There are two distinct nonzero face roots. Again this is NOT asserted to
extend to a full P,Q pair. The separate actual pair P=g*p,Q=g^2 has
J=-2g^2 and tests constantization/pullback scaling exactly.

## Controls, history and current use

Checker box/monomial-j-positive-face-composition-20260906/check.py
SHA89985fa9800790221eb9fc2d44cf04ca007469af0076e935311001ea62d3483f,
read and run in normal and optimized Python, 15 PASS checks each under
25CPU/512MiB/30wall. It uses explicit exceptions; positive/negative ring
fixtures, omitted1/l and sign mutations were executed. Small sampled
determinants illustrate, not prove, the uniform inequality. No CAS/AWS,
receiver enumeration, cut, or solve was performed.

Whole blind Astra/Fable reports were read only after collection; the
relevant GGV definitions/Theorem2.6 proof and Proposition2.11(1)-(3) proof
were read in primary snapshot core-ggv-layout.txt
SHAe3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1,
especially lines364-397 and422-481. History checks in AUDIT, APPROACHES,
PROGRESS, ladder/REDUCTION and the terminal monomial-J report found the
known constantization and blind proposals, not this explicit composition.
This is NEW COMPOSITION / KNOWN INGREDIENTS within that bounded search,
not a worldwide novelty claim. Unread: upstream[8] proof and any complete
forced-face enumeration of current receivers.

Cheapest next test: different-model hostile review of this entire implication,
then ONE source-licensed receiver-face discriminator. If all forced faces
already have at most two nonzero roots, stop that screen as NO GAIN; do not
pretend the lemma establishes coverage or exclusion. If a forced positive
face violates the bound, recheck source necessity and root distinctness before
a separate exclusion gate. No authority is given to cut live K7 inputs.

This is a scoped repair/composition of unpromoted blind proposals. It changes
no already-promoted source/case scope; carry it as a targeted post-cutoff
delta, not a reason to restart the already delayed1435 blind round.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6654`.
- Body SHA-256:
  `51e3f9a0697cd9421d02e63034cce396febcbd7abebb73430b8104e9cbc90511`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
