# Binomial pencils of a Keller pair: provisional primitivity proof

Status: ROOT candidate, MANUAL / UNPROMOTED, pending independent hostile FIRST.
Basis: 63fb2ef8a23b01af4cf5ea24379d90da6df503a0.
JC2 remains open. External novelty is UNKNOWN.

## Claim and conventions

Let P,Q in C[x,y] satisfy J(P,Q)=c in C*. For coprime positive integers m,n,
put r=P^m/Q^n in L=C(x,y). Then C(r) is algebraically closed in L.
Equivalently, r has geometrically integral generic fiber as a rational pencil.
This is primitivity of a one-variable subfield, NOT the assertion
C(P,Q)=C(x,y), nor a primitive element for that finite two-variable extension.

The same assertion applies after translating the target coordinates or any
invertible affine change of the pair: the changed pair is again Keller.
There is no claim that every special binomial fiber is irreducible, that its
generic compact genus is zero, or that arbitrary rational target pencils work.

## Elementary Keller facts

P,Q are nonconstant and algebraically independent. They are coprime, since a
common prime factor would divide dP wedge dQ and hence the constant Jacobian.
Each is squarefree: a repeated prime factor of P divides both its partial
derivatives and hence J(P,Q); likewise for Q.
On the open set PQ!=0,

    dr = P^(m-1)/Q^(n+1) * (m Q dP - n P dQ).

Since dP,dQ are a basis of the regular cotangent module, dr is nowhere zero
there. In particular no prime divisor meeting that open set is a zero divisor
of dr. These facts also hold for each translated pair.

## Choose a primitive rational generator

Let E be the relative algebraic closure of C(r) in L. It is a finite extension
of C(r). The associated smooth projective curve is dominated rationally by
A2; restriction to a suitable line gives a nonconstant map P1 to that curve.
Riemann--Hurwitz in characteristic zero gives genus zero. Thus E=C(H) for a
nonconstant rational H, and r=R(H) for R in C(z).
The field C(H) is algebraically closed in L by construction.
We must show d=deg R=1.

Write H=A/B with coprime A,B in C[x,y]. A fiber value alpha in P1 is
omitted at divisor level if A-alpha B (finite alpha), or B (alpha=infinity),
has no prime factor, hence is a nonzero constant. At most one value is omitted:
two distinct omitted values give two independent linear combinations of A,B
which are constants, forcing A,B and H to be constant.
If one value is omitted, a Mobius change of H sending that value to infinity
makes H polynomial: its new denominator is the indicated nonzero constant.
The new generator remains primitive.

## Ramification away from zero and infinity

Let alpha be a ramification point of R with R(alpha) not in {0,infinity}.
If a prime divisor C occurs in the alpha fiber of H, a local parameter z at
alpha has H*(z) vanishing along C. If R has local degree e>1 at alpha,
the differential d(R(H)) vanishes along C to order at least e-1.
At the generic point of C, r is a nonzero finite value. Coprimality of P,Q
then implies that P and Q are both units there. This contradicts the preceding
nonvanishing of dr. The statement includes alpha=infinity via its local parameter.
Therefore every ramification point of R over a value other than0,infinity
must be an omitted value of H.

Suppose at least one such point exists. Move its omitted H-value to infinity,
so H is a primitive polynomial. For every a in C, the gcd of multiplicities
of H-a is one: a larger gcd k would give H-a=c G^k in the polynomial UFD,
and G would be algebraic over C(H) without belonging to C(H), contrary to
primitivity. Every H-a is nonconstant and has prime factors.

For any finite zero a of R of order e, the divisor of r along the H=a fiber
has multiplicities e times those of H-a. These are all divisible by m, since
P and Q are coprime and r=P^m/Q^n. Their gcd is e, so m divides e.
Similarly every finite pole of R has order divisible by n.
Factor numerator and denominator of R over C. There are coprime polynomials
U,V in C[z] with

    R(z)=c0 U(z)^m/V(z)^n.

Hence P^m/Q^n=c0 U(H)^m/V(H)^n.
The two fractions are reduced, and U(H),V(H) are coprime by a univariate
Bezout identity. Uniqueness of reduced fractions in C[x,y] and extraction
of constant roots give P=c1 U(H), Q=c2 V(H).
This contradicts algebraic independence of P,Q. Thus this case is impossible.

## The remaining two-branch-value case

All ramification of R now lies over0,infinity. Let k0,kInf be the numbers
of distinct points above those two values. Riemann--Hurwitz gives

    2d-2 = (d-k0)+(d-kInf),

so k0=kInf=1. Therefore R is c0 times the d-th power of a Mobius function.
Consequently r is a d-th power in L up to a nonzero constant.
An irreducible factor of the squarefree P gives valuation m of r, so d divides m;
an irreducible factor of the squarefree Q gives valuation -n, so d divides n.
Since gcd(m,n)=1, d=1. This proves the proposed claim.

## Clients, controls and boundaries of the claim

A dominant rational donor (p,q) with p^m/q^n=R(H), deg R>1, for coprime
positive m,n cannot become a polynomial Keller pair by a dominant rational
SOURCE substitution retaining these fixed target functions. The field embedding
retains the proper finite C(H)/C(R(H)), contradicting the claim. This includes
finite source-field enlargements when the resulting source is a rational plane.
It does not exclude arbitrary birational TARGET changes.

The hypotheses matter: for F=id and gcd(m,n)>1 the pencil is a proper power;
for the NON-KELLER pair (x^2,y^2), even coprime m,n give a proper square.
No computational verification or new control-family search was used.

Nearest retained result: [one-bad-fiber FIRST](one-bad-fiber-review-swarmHQ-sol56-root-20261018T211903Z.md).
The pencil u^m/v^n has two nonreduced affine fibers when m,n>1, so that theorem
does not directly apply. The present proof reuses its rational-generator and
omitted-value principles but adds the primitive-polynomial/reduced-fraction step.
Standard curve rationality, characteristic-zero Riemann--Hurwitz, and UFD facts
are explicit classical imports, not a new external-source audit.

The retained October18 nonlinear-curve genus calculation has an independent
infinity-bound gap and gives only a Bezout bound. Generic primitivity alone
does not remove that gap. No finite-normalization equality, suitable rational
generic-fiber existence, degree bound, global counterexample, or JC2 proof follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6407`.
- Body SHA-256:
  `db8d3ec0913512d3190410230e838b90af18c92519b3fe7de0d3016b3ab14239`.
- Frozen basis: `63fb2ef8a23b01af4cf5ea24379d90da6df503a0`.
