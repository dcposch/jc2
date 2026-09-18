# Fractional-linear donor reduction — independent Fable FIRST

Reviewer: independent Fable, requested model=fable/effort=max; exact hosted
identity is self-reported and not independently attested. Publication editor:
swarmHQ ROOT (Astra), September 18, 2026.
Evidence: MANUAL proof review; accepted product-donor theorem and its named
classical imports retained at their existing tiers.
Verdict: CONFIRMED for FRACTIONAL-LINEAR-DONOR-1 at its exact hypotheses,
subject to the narrow ROOT wording clarification below.

This publication preserves verbatim the terminal review's contiguous
mathematical section from "Read scope" through the end of "Verdicts",
including its presentation notes. It is NOT a byte-identical copy of the
entire original submission. Operational headers, startup paths, logs and
duplicate pin tables are omitted. The original terminal submission is
preserved unchanged at full SHA-256
5c79aa7599ca875de485aa9853109a1e2d20b39187b1025e0e37447eaaeb1469
(15042 bytes); its completed body was externally hash-custodied by the
legacy launcher, not canonically seal-stamped. This publication has its
own author-completion and canonical artifact seal.

The frozen producer commit is abcc42be27cc68562e2561988338252d784d5f02,
[producer](fractional-linear-donor-swarmHQ-root-20260918T011400Z.md).
ROOT independently observed the review supervisor and descendants terminal
before collecting the receipt and reading the whole report. All six charged
input hashes matched before/after review and at ROOT collection. These are
custody facts, not substitutes for the proof below.

## Begin verbatim mathematical review

## Read scope

- Producer `fractional-linear-donor-swarmHQ-root-20260918T011400Z.md`: read WHOLE (statement, Sections 2-7, COLLISIONS, seal). Its claim FRACTIONAL-LINEAR-DONOR-1 is the object under review.
- Dependency `symplectic-target-smooth-branch-swarmHQ-root-20260916T192000Z.md`: read WHOLE; Sections 1 and 5 carry the consumed product-cover client.
- Sol FIRST `symplectic-target-smooth-branch-review-swarmHQ-sol-20260916T192900Z.md`: read WHOLE. Its verdict is CONFIRMED for SYMPLECTIC-TARGET-SMOOTH-BRANCH-1 and the rational-R product-cover client at the producer's hypotheses: target change birational with nonzero CONSTANT Jacobian; every old projective branch component smooth; final pair polynomial Keller on the WHOLE source plane; finite source embedding with no degree bound; degree one explicitly a control (its section D).
- FALLACY-v2.md and COORDINATION.md: read WHOLE. APPROACHES.md: frontier context only (header/current-questions table); no verdict below depends on it.
- AUDIT.md: NOT read (not a charged input, no retrieval authorized). The producer's "binding ledger scope" link is therefore taken at the dependency's own stated scope plus the Sol FIRST, which is exactly what the producer consumes.
- Accepted coverage taken as PREMISE (not re-proved): for rational R of degree m>=2, p=R(s), q=t/R'(s), K=C(s,t), K0=C(p,q), there is no birational (p',q') with C(p',q')=C(p,q) and J_(p,q)(p',q')=c in C*, followed by ANY finite C-field embedding C(s,t)->C(x,y) (equivalently any dominant finite-degree rational source substitution), such that the images of p',q' are polynomials with nonzero constant Jacobian on the whole source A2. Its imports (point-blowup resolution/factorization, purity, finite-etale triviality of complex A2, Jelonek coverage, Chau no-A1) stay at their recorded tiers.

## Reconstruction of the producer's proof (independent)

Hypotheses: P,Q in C(x,y), J_(x,y)(P,Q)=1, Q=(ay+b)/(cy+d) with a,b,c,d in C(x), ad-bc != 0.

(R1) Inversion: y=(dQ-b)/(a-cQ), so C(x,y)=C(x,Q); x,Q are algebraically independent (transcendence degree 2), so partial_x and partial_Q on C(x,Q) are well-defined derivations and constants of partial_x on C(Q)(x) are C(Q) (char 0).

(R2) Chain rule: with P=p(x,Q(x,y)), P_x=p_x+p_Q Q_x, P_y=p_Q Q_y, hence J=P_x Q_y-P_y Q_x=p_x Q_y. J=1 gives p_x=1/Q_y=y_Q (inverse-function rule at fixed x). This agrees with the wedge form dP^dQ=p_x dx^dQ, dx^dy=y_Q dx^dQ.

(R3) Partial fractions of the inverse Mobius map: c=0 gives y=(d/a)Q-b/a with A=d/a != 0 (affine); c != 0 gives y=-d/c-((ad-bc)/c^2)/(Q-a/c), i.e. y=A+B/(Q-r) with B=-(ad-bc)/c^2 != 0 and r=a/c in C(x). Then r in C (constant pole) or r nonconstant (moving pole). Three cases, exhaustive, disjoint.

(R4) Affine: p_x=A(x). Write p=N/D, N,D in C[x,Q]; for q0 in C outside the finite set where (Q-q0)|D, specialization Q=q0 commutes with partial_x, so T(x):=p(x,q0) is in C(x) with T'=A (A has no Q-dependence). p-T is killed by partial_x, so p=T(x)+H(Q), H in C(Q). Shear (P,Q)->(P-H(Q),Q): inverse (u,v)->(u+H(v),v), J=1; output (T(x),Q)=(T(x),(y-B)/A)=(T,(y-B)/T'). T'=A != 0 so T is nonconstant. (1) holds with R=T, B0=B.

(R5) Constant pole: p_x=-B/(Q-c)^2. Specialize at q0 != c (and outside the finite bad set): T(x):=-(q0-c)^2 p(x,q0) has T'=B. Then p+T/(Q-c)^2 is partial_x-constant, so p=-T/(Q-c)^2+H(Q). After (P,Q)->(P-H(Q),Q-c) (J=1) the map (p',q')->(-p'q'^2,1/q') has partials (-q'^2,-2p'q';0,-1/q'^2), determinant (-q'^2)(-1/q'^2)=1, inverse (u,v)->(-uv^2,1/v); it sends (-T/q'^2,q') to (T,1/(Q-c))=(T,(y-A)/B)=(T,(y-A)/T'). (1) holds with R=T, B0=A.

(R6) Moving pole: p_x=-B/(Q-r)^2 with r' != 0. Put C=-B/r' (nonzero). Then (C/(Q-r))_x=C'/(Q-r)+Cr'/(Q-r)^2 and u:=p-C/(Q-r) satisfies u_x=-C'/(Q-r) (2). Let F(x)=Q r2(x)-r1(x) with r=r1/r2 in lowest terms; F is linear and primitive in Q, hence irreducible in C(Q)[x], of x-degree deg r>=1. For any root a of F in an algebraic closure of C(Q): r2(a) != 0 (coprimality), r(a)=Q so a is not in C, and r'(a)=-F'(a)/r2(a); since the zeros of r' in C(x) lie in C, r'(a) != 0, so F'(a) != 0 and every root is simple. Likewise a is not a pole of C'. Near a, Q-r(x)=-r'(a)(x-a)+O((x-a)^2), so the residue of -C'(x)dx/(Q-r(x)) at a is C'(a)/r'(a). The left side of (2) is du/dx for u in C(Q)(x) subset Kbar(x), whose Laurent expansion at a has no (x-a)^(-1) term (the derivative of (x-a)^k has exponent k-1 != -1 unless k=0, where it is 0). Hence C'(a)=0 with a transcendental over C, so C'=0 in C(x) (a nonzero element of C(x) has all zeros in C). So C=lambda in C*, B=-lambda r', (2) gives u in C(Q): p=lambda/(Q-r)+H(Q). After the shear, (p',Q)->(Q-lambda/p',-p') has partials (lambda/p'^2,1;-1,0), determinant 1, inverse (u,v)->(-v,u-lambda/v); with p'=lambda/(Q-r) the outputs are (r(x),-lambda/(Q-r))=(r(x),(y-A)/r'(x)). (1) holds with R=r, B0=A.

(R7) Degree: sigma and tau are birational, so n=[C(x,y):C(P,Q)]=[C(x,Y):C(R(x),Y/R')]; with V=Y/R', C(x,Y)=C(x,V) and C(R,V)=C(R(x))(V); V is transcendental over C(x), so [C(x)(V):C(R(x))(V)]=[C(x):C(R(x))]=deg R (Gauss: the minimal polynomial of x over C(R) stays irreducible over C(R)(V)). So n=deg R.

(R8) Composition: (P,Q)=tau^-1 o D_R o sigma as dominant rational maps. For alpha birational with J=c in C* and phi dominant of finite degree, alpha o (P,Q) o phi=(alpha o tau^-1) o D_R o (sigma o phi). J(alpha o tau^-1)=c*1=c, birational; sigma o phi is dominant of finite degree, i.e. (sigma o phi)^*: C(s,t)->C(x,y) is a finite C-embedding; the components of the composite are the images of the accepted theorem's p',q' under that embedding. If the composite were whole-plane polynomial Keller, the accepted client with deg R=n>=2 is contradicted.

## Verdicts

1. C(x,y)=C(x,Q), p_x=y_Q, exhaustive affine/constant-pole/moving-pole presentations over C(x): **CONFIRMED**. (R1)-(R3). The identity p_x=y_Q is the chain rule J=p_x Q_y with Q_y=1/y_Q, coordinate-free via the two-forms. The three presentations are the complete partial-fraction classification of a degree-one map over the field C(x) (c=0 / c != 0 with r constant / r nonconstant), with A != 0 resp. B != 0 forced by ad-bc != 0. No fourth case exists.

2. Rational specialization producing T in cases 1/2 and constants C(Q): **CONFIRMED**. (R4)-(R5). Specialization at Q=q0 is legitimate exactly when the denominator D(x,q0) is not identically zero, a finite exclusion, and then commutes with partial_x because both are ring operations on C[x,Q]; the right-hand side is Q-free (case 1) or has the constant factor (q0-c)^(-2) (case 2), so a rational primitive of A resp. B exists. The constant field of d/dx on C(Q)(x) is C(Q) in characteristic zero, giving H(Q). Nit, not a gap: Section 4 says the specialization "gives a rational T with T'=B" without writing the trivial rescaling T=-(q0-c)^2 p(x,q0).

3. Generic moving-pole residue forcing C'=0: **CONFIRMED**. (R6). Attacks tried: (a) infinity: the argument is local at each finite root a of Q r2-r1 and never uses a residue sum, so x=infinity plays no role; r(infinity) in C u {infinity} is never the transcendental Q. (b) repeated SPECIAL roots: the argument lives over C(Q) with Q transcendental; roots of the generic fibre are simple because a repeated root would be a zero of r', and all zeros of r' lie in C while every root a satisfies r(a)=Q, so a is not in C. No simple-critical-point or fixed-degree hypothesis on r is used or needed; critical values of r only affect special fibres, which are never consulted. (c) coefficient poles: poles of C' and B lie in C u {infinity}, disjoint from the roots a; C=-B/r' is a well-defined nonzero element of C(x). (d) cancellation: (2) is an exact identity with a single term on the right; the residue of du at a is zero for every u in Kbar(x) (even if u had a pole at a); hence C'(a)/r'(a)=0, so C'(a)=0 for a transcendental over C, forcing C'=0. The irreducibility of Q-r(x) (linear primitive in Q) identifies the generic divisor's function field with C(x), matching the producer's alternative phrasing. Signs in (2) and in the residue C'(a)/r'(a) are correct as printed.

4. Target formulas, inverses, Jacobian signs, source translations, mapping-degree preservation: **CONFIRMED**. (R4)-(R7). Each displayed map was recomputed: shear (J=1, inverse (u+H(v),v)); (p',q')->(-p'q'^2,1/q') (J=1, inverse (-uv^2,1/v)); (p',Q)->(Q-lambda/p',-p') (J=1, inverse (-v,u-lambda/v)); constant shift Q-c (J=1). Outputs (T,(y-B)/T'), (T,(y-A)/T'), (r,(y-A)/r') all verified with B0=B,A,A respectively and R=T,T,r nonconstant. sigma(x,y)=(x,y-B0(x)) is a field automorphism of C(x,y) with inverse (x,Y+B0(x)), Jacobian one; it and tau preserve n, and n=deg R by the transcendental-adjunction degree count. The producer's own control y=-r'/(Q-r), p=1/(Q-r) satisfies p_x=y_Q=r'/(Q-r)^2 and maps to (r,y/r') as stated.

5. Composition retaining EVERY constant-J birational target repair and EVERY finite rational source substitution in the accepted theorem's scope, with no intermediate polynomiality: **CONFIRMED** (with the accepted product-cover client as premise). (R8). alpha o tau^-1 is birational with Jacobian c*1=c, so it is within the accepted target-change class; sigma o phi is a dominant finite-degree rational map, i.e. a finite C-field embedding C(s,t)->C(x,y), which is exactly the accepted theorem's source class (its Section 5 and the Sol FIRST section C/D explicitly waive polynomiality, birationality and constant Jacobian of the source substitution). Neither sigma o phi nor alpha o tau^-1 is assumed polynomial anywhere; only the final composite is assumed whole-plane polynomial Keller. The rearrangement is an identity of dominant rational maps, valid because tau is birational and phi is dominant. The producer's D_R=(R,Y/R') is literally the accepted pair (R(s),t/R'(s)) with rational R and no degree bound. Scope match is exact; nothing outside the accepted coverage is consumed.

6. Degree-one control; no arbitrary-donor generation, nonconstant-J target conclusion, new full source, novelty claim or JC2 resolution: **CONFIRMED**. n=1 is correctly excluded: then (P,Q) is birational and, e.g. for R=x, alpha o (P,Q) o phi is polynomial Keller whenever alpha=phi=id, so the exclusion is false at degree one exactly as the accepted theorem's own control states. The report claims no reduction of general rational (or higher-y-degree) pairs to the Mobius hypothesis, no nonconstant-J target statement, no new source family, no novelty, and no JC2 resolution; the Section 7 bullets and Section 1 disclaimers are consistent with the proof's actual reach.

**Overall: CONFIRMED** for FRACTIONAL-LINEAR-DONOR-1 at the stated hypotheses: J=1 rational pair with Q Mobius in y over C(x), normal form (1) by an elementary rational calculation (no imports), and the n>1 all-source/constant-J-target exclusion by direct consumption of the accepted SYMPLECTIC-TARGET-SMOOTH-BRANCH-1 product-cover client at its recorded import tiers. The normal-form part is unconditional; the exclusion part inherits exactly the dependency's lifecycle and tiers. Nothing beyond the fractional-linear hypothesis is established.

Non-blocking presentational notes: (i) Section 4's implicit rescaling of T (above). (ii) Section 2 could state explicitly that x,Q are algebraically independent, which is what makes the partials well defined; this is immediate from J != 0. (iii) Section 5's phrase "restriction of the rational function C'(x) to it is the same function" is correct but relies on the unstated irreducibility of Q r2-r1, supplied above.

## End verbatim mathematical review

## ROOT binding clarification and integration

The final optional presentation note says independence of x,Q is immediate
from J(P,Q)!=0. Taken alone, that wording is false: P=-y,Q=x has Jacobian
one but x,Q are dependent. In the ACTUAL statement Q is Mobius in y over
C(x), so C(x,y)=C(x,Q) and independence follows. Reconstruction (R1) and
verdict (1) explicitly use that correct hypothesis; no inference or claim
under review depends on the looser optional sentence. Promote only the
Mobius-based reasoning. The producer already states this field equality.

For the constant-pole case, the optional explicit rescaling
T(x)=-(q0-c)^2 p(x,q0) indeed gives T'=B; this clarifies the existing proof
without changing it. In the moving-pole case, the generic root a is
transcendental over C, so C'(a)=0 directly forces C'=0. The optional
irreducibility justification is correct but not needed for that last step.

ROOT manually checked the three normal forms, all inverse/sign formulas,
mapping-degree equality and quantified composition. The accepted product
dependency is consumed, not re-audited. Its earlier binding ledger note
limits a nonconstant-J cusp control to branch-smoothness transport; neither
the present producer nor this review uses that control to infer a broader
donor exclusion. No new primary-source proof audit or literature priority
claim is made.

The resulting construction filter has no degree cap, but requires a
degree-one dependence of Q on the chosen source variable y and generic
mapping degree greater than one. It covers constant-J birational target
repairs and finite rational source substitutions as stated; it does not
exclude degree-one donors, arbitrary rational pairs, nonconstant-J target
maps, other target subfields, or all Keller sources. JC2 is unresolved.
No descendant, control family or general generation theorem is supplied.

## Input pins and execution limits

The six immutable inputs, unchanged at collection:

- Producer: 053e0f962aa6558a894ba408de19e18c05ae868342199feb31cd15e49e626809.
- Accepted product producer: f839a4b8d6734d73e45850ed3253211f946ca192eab99c30d2663e0deaf8a85a.
- Product Sol FIRST: cadbc15edc36fd88ac973f42fcf5d8efcd18a42a00ea74adc60f7f143f7188eb.
- FALLACY-v2: e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
- COORDINATION: 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e.
- APPROACHES: b003c386c869f5ac1d0591510e43848314f43f981821fcc82cb9da134fd8a02c.

The reviewer reports manual proof reconstruction only: no scientific
code/CAS, numerical experiment, enumeration, new sources or descendants.
The original reviewer did not run the collision tool; the block below
will be the publication editor's actual check, not attributed to Fable.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

ROOT publication COMPLETE September18 01:31:29 UTC: the extracted
mathematical section was compared equal to the original contiguous text,
all frozen input hashes matched, and the collision tool returned this block.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16304`.
- Body SHA-256:
  `118bf1729f3a3bcfcda9bb0a150f32b7bd301ca967d930ef66858ef9492724db`.
- Frozen basis: `abcc42be27cc68562e2561988338252d784d5f02`.
