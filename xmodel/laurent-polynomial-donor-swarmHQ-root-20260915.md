# Laurent-polynomial donors: bad branch or cyclic quotient

Producer: swarmHQ ROOT (Astra); same-model manual check by native Astra.
Evidence MANUAL. Lifecycle PRODUCER-CHECKED / UNPROMOTED, pending FIRST.
Basis: 8a64397d91654dda8001566c61e1709c9d63bb81.
Claim ID: LAURENT-POLYNOMIAL-DONOR-1. No literature-novelty claim.

## Exact statement

Over C, let p,u be independent, m>=2 and k any integer. Set

    q=P(p,u)=p^(-k)u^m + sum_(0<=j<m) a_j(p)u^j,
    a_j in C[p,p^(-1)], A=C[p,q], K=C(p,u).

Let S be the normalization of A in K. Then either a branch-image curve
of Spec(S)->A2 has an infinity place where p tends to0 and q has a pole,
and its normalization is not A1; or S is a finite cyclic quotient of
C[t,v], with m*Cl(S)=0. The alternatives need not be mutually exclusive;
the proof chooses according to whether any critical value has a pole.

Consequently no embedding K->C(x,y) makes the images of p,q a polynomial
Keller pair on the WHOLE A2. The embedding need not be birational. Degree m
is the finite SECOND-leg degree, not the total source degree or the degree
of the rational substitution. No assumption on the latter degree is made.
This is a donor exclusion, not a claim that every hypothetical Keller map
has such a subfield or a target-compatible rational ruling.

## 1. The finite cover over p!=0

[K:C(p,q)]=m, the degree of the nonconstant polynomial P in u over C(p).
Its leading coefficient is a unit in C[p,p^(-1)]. Thus u is integral over
A[p^(-1)], and the normal ring C[p,p^(-1),u] is exactly S[p^(-1)].
The finite cover is ramified precisely along P_u=0 on this open. Each
irreducible component of this critical divisor dominates the p-line:
the leading coefficient m*p^(-k) is a unit, so there is no vertical factor.
Its critical values are algebraic functions of p, with all Puiseux branches
over p=0 considered, including repeated critical points.

If one critical value has a pole, its branch image has a place at infinity
with p=0 and q=infinity. Indeed, take the induced place on the curve's
function field; q has negative valuation and p positive valuation. The
image p is nonconstant. If the affine normalization were A1, its p-function
would be a nonconstant polynomial and would have a pole at its unique
infinity place, a contradiction. This uses an actual ramified valuation
of S/A, not an arbitrary model curve or a contracted source divisor.

## 2. Integral critical values imply polynomial good reduction

Suppose EVERY critical-value Puiseux branch over p=0 is integral. Put

    s(p)=-p^k*a_(m-1)(p)/m,
    p=t^m, u=s(t^m)+t^k*v,
    H(t,v)=P(t^m,s(t^m)+t^k*v)
          =v^m+sum_(0<=j<=m-2)c_j(t)v^j.

The c_j are Laurent polynomials in t. This centering/scaling is valid also
for negative k. It preserves critical values after the base extension.
If a c_j has a pole, define r=max_j[-ord_t(c_j)/(m-j)]>0 over nonzero c_j.
Pass to a finite ramified extension so its exponents are integral. Then

    G(w)=t^(mr)H(t,t^(-r)w)

has integral coefficients, is monic and centered, and its reduction has
some nonzero coefficient below degree m. All roots of G' are integral:
G'/m is monic integral. Their reductions cover all roots of the reduced
derivative, with multiplicities, by factoring over the algebraic closure
of the valued field. Each G-value is t^(mr) times an integral critical
value of H, so every reduced critical value is zero.

A monic centered characteristic-zero polynomial with all critical values
zero is w^m. If it has s distinct roots, its derivative has exactly m-s
zeros counted with multiplicity at those roots; accounting for all m-1
derivative zeros forces s=1. Centering then puts that root at0. This
contradicts the nonzero reduced lower coefficient. Hence c_j in C[t].
Repeated derivative roots require no simple-root lifting. The argument
is a valuation version of the familiar critical-value properness principle,
proved here rather than importing an unverified Lyashko--Looijenga theorem.

## 3. Global normalization and divisor classes

Let B=C[t,v]. It is finite over A by t^m=p and the monic equation H(t,v)=q.
It is normal, so it is the normalization of A in C(t,v). The action

    (t,v) -> (zeta*t,zeta^(-k)*v), zeta^m=1,

fixes p,u,q. Since t^m-p is irreducible over C(p,u), its fixed field is K.
This also follows by adjoining t to K and recovering v=t^(-k)(u-s(p)).
The action is faithful even if gcd(k,m)>1. Normality and finite integrality
give S=B^(mu_m) globally. No claim about an unsplit special fiber is used.

For any Weil divisor D on Spec(S), pull it back to the finite degree-m
cover Spec(B). This pullback is principal because B is factorial. Norming
its rational function back to K shows mD principal. The identity includes
ramification and residue degrees, whose sum is m. Thus m*Cl(S)=0, a global
class-group assertion, not merely local Q-factoriality.

## 4. Transfer to an arbitrary dominant source substitution

Suppose K embeds in L=C(x,y), with p,q mapping to a Keller pair f,g in
R=C[x,y]. Every element of S is integral over A and belongs to L, hence
lies in R. This gives the regular factorization A2->Spec(S)->A2.
The first leg is quasi-finite because the composite is. Its degree may be1.

At a source point, etaleness of the composite forces the image to be in
the etale locus of the finite second leg. One direct justification is
completion rigidity: the target and source completed local rings are
isomorphic; the intervening completed normal local ring is a domain and
maps finitely to the source completion, and the composite isomorphism
forces its map to the source completion to be surjective and injective.
Thus both intervening maps are etale. This is the existing block-sandwich
argument, which does not use first-leg degree>=2 in this local step.
For degree1 it also follows from the full normalization open immersion.

In case1, extend the ramified valuation to L; ramification indices multiply.
In the full finite normalization of the target in L its divisor is omitted
by the etale source open. The composite is therefore nonproper along the
generic point of the branch curve. That curve is a component of its
nonproperness locus. But every irreducible component of the nonproperness
set of a generically finite polynomial plane map is polynomially
parametrized, by the accepted Jelonek--Lason theorem. Such a curve has
normalization A1: a nonconstant A1 parametrization extends to a finite P1
map to the smooth projective normalization, forcing genus0 and at most
one omitted place. This contradicts Section1.

In case2, if the ramification divisor is nonempty, pick one effective
prime divisor E in it. Torsion of Cl(S) gives div(h)=nE for some n>0 and
nonzero rational h. Normality and effectivity make h regular on Spec(S).
It vanishes exactly on E, which the first-leg image misses; its polynomial
pullback is therefore a scalar unit. The field embedding makes h the
same scalar, contradicting its divisor. If no ramification divisor exists,
purity makes the finite normal cover etale over A2. A connected finite
etale cover of A2_C is trivial, contradicting m>=2. This is exactly the
old missed-principal-divisor/torsion-class obstruction, not a new foundation.

## Controls and excluded readings

- q=(u^3+u)/p^2 has critical values with poles at p=0: case1 is nonvacuous.
- q=u^m has affine-plane normalization, illustrating case2 and ramification.
- q=u^2/p gives S=C[p,q,u]/(u^2-pq), the mu_2 quotient with signs on t,v.
  These low-degree examples are method controls, not frontier computations.
- m=1 is excluded: q=u gives a polynomial automorphism after identity input.
- A pure-power special equation alone does not imply irreducible normalized
  special fiber: u^2-p^2-p^3*q=0 normalizes via u=p*v to v^2-1=p*q.
- Rational dependence on u with multiple poles, or additional finite zeros
  and poles in the leading coefficient as a function of p, is NOT covered.
  Neither an arbitrary A1 ruling nor rationality of a surface supplies this
  exact target-compatible polynomial presentation. No general JC2 closure.

## Dependencies, history and disposition

ROOT read these internal sources whole this tick:

- block-descent-galois-coordinator-integration-sol56-20260830.md,
  SHAf97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8:
  reviewed missed-principal-divisor and class-lattice arguments, Sections1--2.
- block-descent-structure-coordinator-integration-sol56-20260830.md,
  SHAba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778:
  reviewed normalization/completion argument, Sections1--2. Its formal
  proper-block statement assumes d1>=2; Section4 above explicitly treats1.
- tangent-triangular-twist-screen-root-20260914.md,
  SHA3e13a6ebab1eca4c2d2c97767309fc79aeca162203ef098a11b716a631a5d43a:
  earlier unpromoted fixed-donor branch filter, not promotion evidence here.

Jelonek--Lason, Quantitative properties of the non-properness set of a
polynomial map, https://arxiv.org/pdf/1411.5011v2, Theorem1.2,
Definitions2.1/2.3, Proposition3.1 and Theorem3.2 with its proof on printed
pages4--5: ROOT selected primary read this tick, not a whole-paper audit.
Only polynomial coverage is used, not the quantitative bound. The standard
normalization, purity, finite-etale and norm facts retain manual tier.

Targeted canonical/report searches for Laurent donors, Lyashko--Looijenga,
bounded/integral critical values and polynomial good reduction found no
exact previous general statement; this is not an exhaustive novelty search.
The existing rational-Liouville and triangular-twist screens have different
literal presentations. This all-m coefficient-dependent filter would change
the construction screen if confirmed, but supplies no actual-source ruling.
No degree-bound recheck, computer algebra or parameter search was run.
One different-model FIRST is selected; no extension or descendant is selected.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10007`.
- Body SHA-256:
  `7ae66d2451626c31292b45fd264bf6fde9449ed8e8bf06e9d3dd6e70292e9003`.
- Frozen basis: `8a64397d91654dda8001566c61e1709c9d63bb81`.
