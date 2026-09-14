# Integral closure and formal-flow coefficient containment

Producer: swarmHQ ROOT (Astra), September14,2026.
Basis: 49d9c0d9bc23f14ffaa5e4b81521498889663591.
Evidence: MANUAL / DOCUMENTARY. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.
Outcome: KNOWN-ENDPOINT / NO_NEW_CLOSING_TEST. JC2 remains unresolved.

## Question and literal rings

For an actual complex polynomial Keller pair, write

    A=C[f,g] subset R=C[x,y], K=Frac(A), L=Frac(R),
    S=the integral closure of A in L.

Here S is finite over A, normal and noetherian, and S is contained in R:
an element integral over A is also integral over the integrally closed R.
The standard finite-normalization factorization identifies the WHOLE source
plane with an open subset of Y=Spec(S). It does not identify R with S.
The lifted target derivations D_f,D_g act on R and on L. The unproved step
is their preservation of S; regularity on the source is not that step.

The proposed formal-flow bypass is to apply exp(TD), where D is one lifted
target partial derivative and T is a NEW formal variable. Since D is
locally nilpotent on A, exp(TD)(A) is contained in A[T]. If s is integral
over A, exp(TD)(s) is integral over A[T] inside R[[T]]. One might hope to
deduce that every coefficient is in S. The following precise obstruction
shows why a blanket integral-series containment is not available for free.

## Manual obstruction to the blanket containment

Let C be the set of elements of R[[T]] integral over A[T], using its literal
inclusion in R[[T]]. Then, in the displayed setting,

    C subset S[[T]]  if and only if  R=S.

This is not a new route to R=S: it says the proposed general coefficient
containment already demands the entire missing integrality conclusion.

Proof. Suppose C is contained in S[[T]], and choose any b in R. Since b is
algebraic over K, there is a nonzero a in A such that ab is integral over A,
hence ab belongs to S. For example, clear the denominators in a monic
equation for b over K, and scale b by their common multiple. Form

    w(T)=a*(1+b*T)^(1/2) in R[[T]].

Its square is a^2+a*(ab)*T in S[T]. The ring S[T] is integral over A[T],
so w is integral over A[T] by transitivity. Thus w belongs to C. All its
coefficients must belong to S. Every binomial coefficient binom(1/2,k)
is a nonzero complex constant, so this gives a*b^k in S for every k>=0.
Consequently S[b] is an S-submodule of the finite S-module (1/a)*S.
Noetherianity makes S[b] finite over S, whence b is integral over S.
Normality of S inside L gives b in S. Since b was arbitrary, R=S.
Conversely R=S makes the containment tautological, since the ambient series
ring itself is S[[T]]. This completes the argument.

Equivalently, at any height-one valuation of S the claimed coefficients
would imply v(a)+k*v(b)>=0 for EVERY k. Any negative v(b) eventually violates
this. Finite coefficient checks alone supply no all-orders containment.

For actual Keller data, R=S makes F finite; the accepted finite-etale
affine-plane endpoint then gives automorphy. No actual Keller source is
shown to satisfy C subset S[[T]]. Nor is exp(TD)(S) shown to stay outside it:
the blanket argument is stopped, not every possible special-flow argument.

## Concrete negative control with a literal area-preserving map

Use the PUNCTURED plane, not the whole plane:

    R0=C[x,x^-1,y], u=x^2, v=y/(2*x), A0=C[u,v].

The displayed map has Jacobian1. Its integral normalization in C(x,y) is
S0=C[x,v], with x^2=u; indeed R0=S0[x^-1]. This S0 is normal and finite
over A0, and has the same fraction field as R0, so it is the full integral
closure. The target derivative extending partial_u satisfies

    D_u=(1/(2*x))*partial_x+(y/(2*x^2))*partial_y,
    D_u(x)=1/(2*x), D_u(u)=1, D_u(v)=0.

It is regular on R0 but does NOT preserve S0. The actual formal orbit

    exp(T*D_u)(x)=(x^2+T)^(1/2)

is integral over A0[T], by Z^2-u-T=0, but its T coefficient 1/(2*x)
is not in S0. This is a failure of finite-extension normalization stability
and of coefficient containment even for an exact lifted translation flow.
It is not a Keller counterexample: x is a nonconstant unit and the map is
not polynomial on the whole source plane. No new family is being proposed.

Positive control: for F=(x,y+x^2), A=R=S, so the normalization and every
series-containment statement above hold. No source-coordinate choice or
constant-Jacobian hypothesis has been erased from this comparison.

## History and precise source-access scope

Canonical searches covered current APPROACHES, AUDIT, PROGRESS, notes,
REDUCTION and targeted report filenames, not every historical report.
APPROACHES section8 and the September12 adjoint-derivation intake already
retain a stronger derivative-loss calculation: a codifferent element can
have valuation1-e, and transverse differentiation can lower it to1-2e.
The present elementary control is not an additional family or a reversal
of that result. The September13 16:10 journal also already stops importing
algebraic-flow classification without its single-valuedness hypothesis.

Targeted web discovery located precisely this formal-series warning in the
indexed text of Bass, *Differential Structure of Etale Extensions of
Polynomial Algebras*, AppendixB, (B.7)--(B.8), printed p96. The indexed
paragraph attributes its square-root observation to a discussion with
Hochster. Canonical publisher metadata was read at
https://link.springer.com/chapter/10.1007/978-1-4612-3660-3_5
and identifies the 1989 chapter, pp69--109, DOI10.1007/978-1-4612-3660-3_5.

IMPORTANT access limit: the full-book URL
https://szemberg.up.krakow.pl/1989_Book_CommutativeAlgebra.pdf
failed in the browser with a fetch timeout; the one direct bounded curl
attempt stopped on certificate verification before obtaining the PDF.
No TLS bypass or access-control bypass was attempted. Therefore ZERO full
pages of that chapter were read, and the indexed excerpt is NOT a whole
primary-text audit. Exact bar notation in the indexed OCR was not trusted;
the A/R/S proof above reconstructs every ring and coefficient independently.
The existing local bass-1989.pdf was checked only at metadata/cover scope:
it is the DISTINCT French 13-page Numdam paper, not this chapter. Neither
it nor the publisher abstract was substituted for AppendixB. The finding
is documentary priority discovery plus a self-contained manual stop,
not a new external theorem import or a literature-novelty claim.

## Integration and stopping condition

The independent Astra boundary-duality report
xmodel/source-boundary-duality-swarmHQ-astra-20260914.md was collected only
after independent COMPLETED status and expected-manifest verification.
ROOT read its entire report and manifest, and manually checked the trace
dual signs, localization, polarization and fixed double-cover control.
Its codifferent M=Hom_A(S,A) sits inside R but is not thereby closed under
multiplication. Requiring Tr(h^2) in A for all h in M forces M=S by trace
biduality; it does not prove that regularity. This is the old trace gap,
not a new two-moment algorithm or a found source. Same-model corroboration
does not provide different-model FIRST. No promotion or descendant selected.

No computation, finite-degree test, source or operator family, AWS action,
paid-model lane, or execution-software change was needed. All formulas in
this report were checked by direct algebra and differentiation; the tools
only performed source discovery, file reading, hashes and publication.
The next research must provide new actual-source compatibility, not assume
the generic formal-series containment, normality stability, codifferent
multiplication, or trace regularity established here only as missing steps.

## COLLISIONS

Manual targeted check: no new OPEN identifier is raised. The mathematical
target collides with the known integral-closure/adjoint and trace gaps;
the exact generic formal-series warning was also located in Bass's indexed
AppendixB. No whole-corpus collision scan or exhaustive priority claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8015`.
- Body SHA-256:
  `9c4762597c49b5deab0df0704bfce401d6fe15696f933301a127584fe07e5839`.
- Frozen basis: `49d9c0d9bc23f14ffaa5e4b81521498889663591`.
