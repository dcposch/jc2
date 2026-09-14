# Rational-mate obstruction survives every monomial constant-J target change

Producer: swarmHQ ROOT (gpt-6-astra), September14, 2026.
Evidence MANUAL; lifecycle PRODUCER-CHECKED, UNPROMOTED.
Native Astra independently checked the B_n argument and its postcomposition
scope, message-only. The monomial classification below is ROOT's elementary
corollary. Neither is different-model FIRST. No computation or search ran.

## Exact scope

Over C fix Q!=0 in C[t], I'=Q with any integration constant, and

    t=x^3*y, p=x^2*Q(t), q=I(t)/(2*p^2).

This rational pair has J(p,q)=1. Let M be any rational monomial map in p,q
with integer exponents, nonzero constant coefficients and nonzero constant
Jacobian. There is NO dominant rational source map Sigma:A2 --> A2 such
that M composed with (p,q) composed with Sigma is a polynomial Keller pair.
The same is true after a polynomial target automorphism is POSTCOMPOSED.

No source-degree bound or birational-source hypothesis is used. Nonmonomial
rational target maps, target automorphisms placed BEFORE M, and interleaved
target changes are not covered. This closes one changed-target tranche for
the specified old rational pair, not arbitrary rational pairs or JC2. No
further family, degree or target-change successor is selected.

## The determinant-one subgroup

First take any integer n and

    B_n(p,q) = (p*(p*q)^n, q*(p*q)^(-n)).

It preserves p*q, has rational Jacobian1, and inverse B_(-n). Suppose its
source pullback gives U,V in R=C[s,z] with J(U,V)=lambda in C*. In the
injective function-field pullback put X=Sigma*(x), T=Sigma*(t). They remain
nonconstant rational functions in Frac(R). Direct substitution gives

    I(T)=2*U^(2-n)*V^(1-n),
    X^2*Q(T)=U^(1-n)*V^(-n).                              (1)

U and V are nonconstant, squarefree and coprime. A repeated factor of one,
or a factor shared by both, would divide their nonzero constant Jacobian.

For n<=0 let a=2-n and b=1-n, positive consecutive integers. The first
identity makes T integral over R, hence polynomial by normality. Taking
Jacobians with U and V gives

    Q(T) divides U^a*V^(b-1) and U^(a-1)*V^b,

so Q(T) divides U^(a-1)*V^(b-1). If Q(r)=0 but I(r)!=0, a prime factor
of the nonconstant polynomial T-r divides Q(T) and cannot divide UV:
reduce I(T)=2U^a V^b modulo that prime. Contradiction. Thus every critical
point of I lies in its zero fiber. If I has d total roots with multiplicity
and k distinct roots, I' has exactly d-k zeros at these roots. Accounting
for all its d-1 zeros forces k=1. Write I=c(t-r)^d. Valuations at prime
factors of U and V in I(T)=2U^a V^b force d|a and d|b. Hence d=1 and
Q=c is constant.

For n=1, I(T)=2U again makes T polynomial, and

    Q(T)*J(T,V)=2*lambda.

Thus Q(T) is a unit; since T is nonconstant, Q is constant.

For n>=2, 1/I(T)=(1/2)U^(n-2)V^(n-1) is polynomial. Write T=A/B in
lowest terms and let d=deg I. The numerator F(A,B)=B^d I(A/B) is coprime
to B: reducing modulo any prime of B leaves the nonzero leading coefficient
times A^d. Therefore F(A,B) divides B^d and must be a unit. Factoring I
over C makes every A-r_i B a nonzero constant. Two distinct r_i would
force both A and B constant, impossible. Consequently I=c(t-r)^d.
Normality makes W=1/(T-r) polynomial, since

    W^d=(c/2)*U^(n-2)*V^(n-1).

Squarefreeness forces d to divide the consecutive positive exponents when
n>2; at n=2 the exponent1 of V suffices. Again d=1 and Q=c is constant.

In ALL cases the second identity (1) is now

    X^2=c^(-1)*U^(1-n)*V^(-n).

The consecutive integers 1-n and -n cannot both be even. A prime factor
of the corresponding squarefree U or V has odd valuation on the right,
but every rational square has even valuation. This is the contradiction.
The argument handles poles of X and negative exponents without evaluating
rational functions on their pole sets, and uses no surjectivity of (U,V).

## Every integer-exponent monomial target

Write a general monomial target as (c1*p^a*q^b,c2*p^c*q^d). Its nonzero
constant Jacobian requires a+c=1, b+d=1 and k=a-b!=0. If its source
pullback is polynomial Keller U,V, the pulled-back rational p satisfies

    p^k = nonzero_constant * U^(1-b)*V^(-b).

Valuations at a prime of U and a prime of V force k to divide both 1-b
and b. Thus |k|=1. For k=1, a=b+1 and this is B_b up to constant scalings.
For k=-1, swap the outputs; it is then B_(1-b) up to constant scalings.
The previous proof excludes both. This uses only UFD valuations, not an
assumed polynomial factorization or a Galois-closure substitution.

A postcomposed polynomial target automorphism can be inverted polynomially;
its constant nonzero Jacobian preserves the Keller condition. This proves
exactly the postcomposition assertion, not arbitrary interleavings.

## Controls and provenance

The squarefree/Keller condition is essential: for Q=1,I=t,n=0, the dominant
polynomial source substitution (x,y)=(s,2s*z) yields (p,q)=(s^2,z), with
Jacobian2s rather than a unit. Its square factor is exactly the final failure.

The special rational pair is also essential. Starting instead from (p,q)=(x,y),
the dominant rational source B_(-n) cancels B_n and gives the identity for
every n. Thus rational formulas or monomial changes alone are not excluded.

The n=0 proof was already banked in
`xmodel/rational-mate-polynomialization-swarmHQ-astra-20260914.md`, read WHOLE,
SHA256 `16f0e9cfdac2980ff7c8f6975913e96b0019165fcd42532d91e7fa77c5c624cc`.
It expressly left arbitrary rational target changes outside scope. The
present all-monomial check is a scoped extension, not an exhaustive novelty
claim. Manual replay: substitute (1), take the two polynomial Jacobians,
factor the homogeneous numerator, and compare prime valuations. No CAS,
optimized-mode verification, source-data specialization or exit-price claim.

## OPEN(S) RAISED

None. The remaining nonmonomial possibility is not assigned a successor.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6032`.
- Body SHA-256:
  `e8b33509967fe5acae6582af45f971d390de236967abd20c2a02350f63d93f8e`.
- Frozen basis: `9e0ff11eeeecb27879223178f8cc75858780c535`.
