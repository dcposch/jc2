# Keller nonescape and the dicritical class correction

**Tier:** PROMOTED / MANUAL / CONDITIONAL after independent review. JC2 remains unresolved.
ROOT/Astra co-research; independent configured Sol 5.6 review. No novelty claim or formal verification claim.

## Two scoped results
Let F=(P,Q) be an actual complex polynomial Keller map with det DF=1. Normalize infinity valuations by value -1 on a generic affine linear function.
Write A for Favre–Jonsson thinness, V0 for the normalized valuative tree, and d(F,w)=-min{0,w(P),w(Q)}.

1. For this fixed F, there is c_F>0 such that d(F,w)>=c_F for every w in T={A<=0}.
2. In the [adopted infinitely singular eigenvaluation setting](infinitely-singular-value-group-swarmHQ-root-astra-sol56-20261026.md), choose an actual source boundary divisor E mapping onto an affine curve C={c=0}, with curve degree f_E. On compatible resolved models,

       (F^* Z_nu . E) = -f_E nu(c) > 0.

Every valuation preimage of nu is centred away from this E on those models, so its dual class pairs zero with E. A preimage-only A7 class identity is therefore impossible whenever such an E exists.
The second assertion is conditional on the chosen actual dicritical E. This report proves neither existence nor nonexistence of such a divisor in the general case.

## Foundation tier
The named inputs are the plane-valuative-tree and class framework in [Favre–Jonsson](https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p06-p.pdf): compactness of V0, monotonicity and semicontinuity of thinness/skewness, ancestral divisorial approximation, and the dual-class/L2 operator framework.
The underlying classification/retraction foundations cited there as [28]/[30], and the broader referenced proofs, were not audited. The reviewed claim retains this explicit named-import tier.
The [full proof](../box/keller-nonescape-dicritical-swarmHQ-20261026/nonescape1400-astra.md), [independent review](../box/keller-nonescape-dicritical-swarmHQ-20261026/nonescapereview1430-sol56.md), and [mandatory review qualification](../box/keller-nonescape-dicritical-swarmHQ-20261026/nonescapereview1430-sol56-qualification.json) specify the scope.

## Proof of fixed-F nonescape
Put Omega=dx wedge dy. For algebraically independent rational f,g, define J by df wedge dg=J Omega. Every finite-thinness w satisfies

    A(w) >= w(f)+w(g)-w(J).

For primitive w=ord_D, write f=u^m f0 and g=u^n g0 at the generic point of D, where u cuts out D and f0,g0 are units. Differentiation gives ord_D(df wedge dg)>=m+n-1, while ord_D(Omega)=A(ord_D)-1.
For nondivisorial w, increasing divisorial ancestors converge to w. Monotonicity gives A(w_j)<=A(w), and lower semicontinuity gives the reverse limiting inequality, so A(w_j)->A(w). Rational-function values converge as well. This proves the inequality without assuming a finite-map equality at a limit.
Curve semivaluations have infinite thinness under the formal plane-branch foundation, so T consists of field valuations.
Suppose d(F,w)=0 with w in T. Its raw restriction v(H)=w(H composed F) is nonnegative on the target polynomial ring. It is nontrivial: in a finite algebraic field extension, a valuation trivial on the base is trivial everywhere, by the unique least-valued term in a minimal polynomial.
At a closed affine centre (a,b), use f=P-a,g=Q-b and J=1. Their positive values force A(w)>0. At the generic centre of C={c=0}, choose an affine linear g0 with g0 and J(c,g0) nonzero modulo c, and use f=c(P,Q),g=g0(P,Q). Then w(f)>0 while w(g)=w(J)=0, with the same contradiction.
Thus d has no zero on T. Lower semicontinuity makes T closed in compact V0; continuity of the truncated minimum defining d yields the positive minimum c_F.
This constant concerns one fixed F. No invariance or proper self-map of T, and no bound uniform over iterates, is asserted.

## Why the class comparison still has a correction
First let nu=ord_D/b_D be divisorial on a target compactification Y and resolve F as a morphism g:X->Y. Its dual boundary class satisfies (Z_nu.D')=delta_(D,D')/b_D.
For a source boundary prime E mapping with degree f_E onto the closure of C={c=0}, projection gives

    (g^* Z_nu . E) = f_E (Z_nu . closure(C)) = -f_E nu(c).

The last equality uses closure(C) linearly equivalent to -sum_D' ord_D'(c) D'. This is the coefficient of Z_ordE in the source dual-boundary expansion; it is not a valuation-preimage term.
For the infinitely singular target, first separate its centre from the strict transform of C. Further target blowups along nu miss C, and source resolutions can be chosen away from E. Only in this compatible sequence do the strict and total transforms of E agree.
The ancestral dual classes converge strongly in L2: their line-class pairings are 1, their mutual pairings are given by skewness, and monotonicity plus upper semicontinuity gives convergence of skewness. Bounded pullback and pairing with fixed E pass the finite identity to the displayed formula.
Every actual valuation preimage has its centre over the separated target centre, hence outside E. Its dual class therefore pairs zero with E. This excludes a finite preimage-only sum, or any convergent such sum for which that pairing is defined, if the coefficient is nonzero.
It is strictly positive here. The reviewed infinitely singular nu has residue field C and is nonpositive on every nonzero polynomial. If a nonconstant polynomial had value zero, subtracting its complex residue would give a nonzero polynomial of positive value. Hence nu(c)<0, even without alpha(nu)>0.
The inequality A(E)>0 places E outside T; it does not remove E from the boundary class basis. Nonescape on T therefore cannot delete this term.

## Remaining gap and disposition
The general raw discrepancy equality for other infinitely singular extensions, and thus their membership in T, remains unproved in this report. Even granting it would not erase the dicritical coefficient.
We retire only the inference from compact-T nonescape to an uncorrected, preimage-only A7 identity. A successor needs control of the actual correction or a different global use of nonescape; reproving divisorial conservation or pursuing discrepancy equality alone does not close the argument.
No globally convergent corrected expansion, extension count, degree-one result, or JC2 conclusion is claimed.

## Evidence
[Original evidence and custody](../box/keller-nonescape-dicritical-swarmHQ-20261026/README.md) preserves the producer, independent review and correction byte for byte. The correction fixes an ambiguous negation about existence and the review's incomplete reading-count receipt; it changes no mathematical verdict.
ROOT read the producer64, review89 and qualification37 in full and verified their seals and fixed inputs. ROOT is a coauthor, not an independent reviewer; no separate review of this integration's formatting is claimed.
The producer did not separately timestamp completion of its whole-STATE read, so that precise timing deadline is uncertified. This is retained in the evidence, without an invented timestamp.

## OPENS RAISED
None. The existing actual-source correction and extension gaps remain.

## COLLISIONS
Frozen-public collision output is retained in the evidence package. EMPTY is not novelty evidence.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7290`.
- Body SHA-256:
  `ab72dd4e3a0742463e675da4cbe42ae8bf7cd36b7ba767ca275c101419639fd5`.
- Frozen basis: `3a60479fcfb114451c6e78da554af39707c518a7`.
