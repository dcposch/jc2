# Fixed-degree source composition and the closed-H source screen

Author: /root (Astra coordinator). Date: 2026-09-09.
Basis: 0d39df3c9fd69c939a8420c54d03228b9077777d.
Lifecycle: PRODUCER-CHECKED candidate, not promoted; different-model hostile
review is required. Derived after the coordinator's 0310 blind was sealed,
without reading any peer blind. This is post-blind research, not a changed
premise of the frozen ideation packet. ZERO mathematical subprocesses.

## 1. Exact candidate conclusions and trust boundary

(A) There is no ordinary polynomial pair P,Q over any characteristic-zero
field with degrees (75,125) and [P,Q] a nonzero constant. This follows by the
new source-normalization argument below, followed by the already accepted
standard-F2 published chain, minimal receiver map, and weight-free exclusion
(AUDIT15q). It is not a proof of JC2, a maximum-degree-125 bound, an explicit
unit/cofactor certificate, or a claim about every object labelled D125.

(B) More generally, suppose m,n>1 are coprime, D>0, deg P=mD, deg Q=nD,
[P,Q] is a nonzero constant, and their homogeneous top forms are H^m,H^n
for a homogeneous degree-D polynomial H. Then H is, over an algebraic
closure, a proper d-th power up to a scalar, for some integer d>2.
Consequently such an actual pair cannot satisfy ker[H,-]=K[H].
This makes the entire closed-H source class of accepted15w empty, not merely
its late-contact subcase. It does not refute the conditional15w theorem.
It gives no result for proper-power H or nonconstant-J receivers.

Both conclusions import published normalization/corner theorems. We are not
claiming to independently reprove all their foundations or replay their
classification programs. Conclusion B is a known-theorem consequence, not a
new all-degree JC2 obstruction. Conclusion A composes imported normalization
with our accepted receiver result; novelty is not asserted.

## 2. Primary theorem interfaces

ML2025: L. Makar-Limanov, "On the shape of a counterexample to the Jacobian
Conjecture", Serdica Math. J.51 (2025),299–314,
https://serdica.math.bas.bg/index.php/serdica/article/download/300/153/862
(DOI10.55630/serdica.2025.51.299-314).
The argument on printed302–305 states that for each complex counterexample,
a polynomial SOURCE automorphism makes the support of its first polynomial
contain its simultaneous coordinate-degree corner (r,s), with r<s after
interchanging coordinates. All support lies in [0,r]x[0,s]. The argument
uses that actual pair, not a counterexample of globally minimal degree.
We consume only this source-automorphism normal form, not the later target
degree-reduction argument. A nonzero constant Jacobian can first be made 1
by a scalar rescaling of P, which changes neither supports nor degrees.

GGV2014v3: Guccione–Guccione–Valqui, "On the shape of possible
counterexamples to the Jacobian conjecture", arXiv:1401.1784v3,
https://arxiv.org/pdf/1401.1784v3 .
Definition4.3 requires coprime m,n>1, a nonzero constant bracket, equal
total-degree and horizontal-degree ratios m/n, and
v_(1,-1)(en_(1,0)P)<0. Proposition5.20 applies to EACH such (m,n)-pair in
L^(1); it produces a standard pair, preserving both total degrees and
en_(1,0)P. Its final sentence permits a polynomial automorphism of ordinary
L=K[x,y] when the input is ordinary. Its additional successor-direction
statement is conditional extra information, NOT a hypothesis for this
standardization. We use neither Proposition4.7's minimal-pair formulation
nor Corollary5.21's minimum B.

GGHV2017v1: Guccione–Guccione–Horruitiner–Valqui, "Some algorithms related
to the Jacobian conjecture", arXiv:1708.07936v1,
https://arxiv.org/pdf/1708.07936v1 .
Theorem2.20 gives a complete chain for EACH standard (m,n)-pair; (6) fixes
A0=(1/m)en_(1,0)P and (13) identifies the starting triple. Section2.4,
Remark2.24 and the paragraph after Definition2.25 show the resulting chain
is admissible. Section5 publishes the exhaustive tables for v_(1,1)(A0)<=35.
The other degree orientation is obtained by swapping m,n. Published
exhaustiveness is an explicit import, not a fresh replay of Algorithms8/9.

For B only, GGV Corollary7.9's FIRST assertion says that for EACH ordinary
standard (m,n)-pair, writing (a,b)=(1/m)en_(1,0)P, one has positive integral
a,b and gcd(a,b)>2. Its subsequent claim about the globally minimal B has
separate hypotheses and is not used.

## 3. A given representative normalizes without changing its reduced ratio

Work first over C. Nondividing degrees mD,nD cannot be those of a polynomial
automorphism, by the plane polynomial-automorphism degree-divisibility
theorem. Hence the given Keller pair is a counterexample to which ML applies.
Write Pbar=phi(P), Qbar=phi(Q), and let (r,s) be the rectangle corner of Pbar,
r<s. Both r,s are positive: if the rectangle had r=0, Pbar would be a
polynomial of y alone; its derivative times Qbar_x being a nonzero constant
would force Pbar linear and Qbar a nonzero linear x term plus a polynomial
of y. The pair would be an automorphism, a contradiction.

For every strictly positive rational weight w=(alpha,beta), Pbar_w is its
single corner monomial lambda*x^r*y^s. The predicted top bracket weight is

w(Pbar)+w(Qbar)-alpha-beta > 0,

since r,s>=1, r<s and Qbar is nonconstant. The actual bracket is a constant.
Thus [x^r*y^s,Qbar_w]=0. A monomial x^i*y^j in Qbar_w contributes coefficient
r*j-s*i at exponent (r+i-1,s+j-1). Distinct terms cannot cancel each other.
Every such exponent (i,j) is proportional to (r,s), and a fixed positive
weight then permits only one monomial. Among proportional nonnegative
support points the largest multiple is the largest for EVERY positive
weight. Calling that point (t,u), every positive-weight leader is (t,u).
Taking either coordinate weight arbitrarily large shows every Qbar support
point satisfies i<=t,j<=u. Thus Qbar has a proportional rectangle too.

Let psi=phi^{-1}, U=psi(x), V=psi(y), M=deg U>=1, N=deg V>=1.
Under inverse substitution, the corner is the UNIQUE support point
maximizing Mi+Nj. Its leading product U_M^r V_N^s is nonzero in a polynomial
domain. Therefore no cancellation, including algebraic dependence of the
leading coordinate forms, can change the exact equalities

deg P=Mr+Ns,  deg Q=Mt+Nu.

Since (r,s) and (t,u) are proportional, their ratio is the original m/n.
Coprimality yields positive integers a<b with
(r,s)=m(a,b), (t,u)=n(a,b), and

D=Ma+Nb >= a+b.

Hence Pbar,Qbar meet the literal GGV Definition4.3 with the ORIGINAL ordered
coprime ratio m/n, en_(1,0)Pbar=(ma,mb), and ordinary polynomial supports.
Proposition5.20 produces an ordinary standard pair Pstd,Qstd with that same
endpoint and total degrees m(a+b),n(a+b). In particular its actual degree
gcd is g=a+b<=D. No global-minimality, inherited-successor, affine-normalizer,
same-coefficient-dictionary, or reverse-lift premise has been introduced.

## 4. Hand filter of the published table for the exact 75/125 source

Set m=3,n=5,D=25. Only rows with a+b<=25 can occur. They are exactly
F1–F8 and F18,F19; all the other published rows have a+b>=28.
The table parameter j is a nonnegative integer. Check both degree
orientations by requiring the unordered pair {m,n}={3,5}:

- F1: (2j+3,3j+4); j=0 gives (3,4), and j>=1 cannot give {3,5}.
- F2: (j+2,2j+3); exactly j=1 gives (3,5).
- F3: (4j+3,3j+2); j=0 gives (3,2), and j>=1 cannot give {3,5}.
- F4: (2j+3,12j+16); its second entry is at least16.
- F5: (7j+9,4j+5); its first entry is at least9.
- F6: (3j+4,8j+10); its second entry is at least10.
- F7 and F18: (j+2,4j+7); their second entry is at least7.
- F8 and F19: (2j+3,5j+7); their second entry is at least7.

This is a finite hand comparison of the printed formulas, NOT execution of
a mathematical program. It does not require the paper's additional
exclusion of F18/F19. The only surviving necessary chain is therefore F2,

A0=(5,20), A0'=(1,0), A1=(7/5,2), k=1, (rho0,sigma0)=(5,-1).

Its a+b is25, so Pstd,Qstd have actual degrees75,125, not merely ratio3/5.
Theorem2.20(8) has l1=5>1, and (13) makes index0 the actual starting
triple of this very standard pair. Thus the premise is the precise
standard-F2 source expected by the accepted chain, not a degree label.

## 5. Literal composition into accepted15q

Incoming accepted interfaces, with their named published dependencies
retained, are:

1. The published-chain discriminator and its Fable gate take an ACTUAL
ordinary standard (3,5)-pair of degrees75,125 with precisely the F2
starting triple above. They produce one of the three ordinary U,V pairs
of degrees30,50, [U,V]=c0*x^3 with c0!=0, and the three specified
quartic-root patterns. This source arrow is existential; no coefficient
dictionary to an unrelated carrier is needed.

2. The accepted minimal monomial map is S(W)(g,p)=W(g,p/g).
The incoming support cone i>=j makes every image monomial
g^(i-j)*p^j ordinary, and makes this coefficient map injective.
The exact chain yields A=S(U),B=S(V), with degrees15,25,
[A,B]=c0*g^2. Their leading forms are lambdaP*H^3,lambdaQ*H^5 for
lambdaP,lambdaQ!=0, where either

H=p^2*(g^3+p^3),

or H=p^2*(p+g)*(p+(1-rho)*g)^2,  rho^2-3rho+1=0,

including both conjugate roots. These are the accepted image forms,
not a newly guessed normalization of an arbitrary coefficient ansatz.

3. Replace A,B by lambdaP^{-1}A,lambdaQ^{-1}B. This is defined over the
current coefficient field, keeps the degrees and ordinary supports, makes
the leading forms exactly H^3,H^5, and changes the target only to
c*g^2 with c=c0/(lambdaP*lambdaQ)!=0.
Accepted15q excludes ALL ordinary pairs with these actual degrees, top
forms and target, without requiring the old weighted polygon, parity,
additional coefficients, or a c=1 gauge.

The antecedent of15q has now been discharged for every hypothetical
degree75/125 pair over C. Contradiction. This composition does not claim
surjectivity of the minimal map or a reverse lift; only the forward
existence implication is needed.

For any characteristic-zero field K, all coefficients of an alleged pair
and its Jacobian constant lie in a finitely generated field F over Q.
Such F embeds in C. The embedding preserves nonzero leading coefficients,
degrees and the nonzero constant Jacobian. The complex contradiction
therefore proves nonexistence over K. No assertion that a selected complex
normalizing automorphism descends to K is needed. Finite-witness algebraic
closure transfer is another possible route, but is not used here.

Interface consequence, conditional on review: any complete guarded
coefficient system whose points reconstruct ordinary degree75/125
constant-J pairs has no geometric points. In particular the COMPLETE
original B0 source has that implication if every original row and
nonzero-degree/Jacobian guard is retained. We produce neither an explicit
unit certificate nor a proof that every loosely named D125 carrier is
this complete system. M2=90 numerical descriptions are not themselves
coefficient families. The argument rules out actual75/125, not all
normalized table entries with maximum degree<=125 or every Moh125 label.

## 6. The entire closed-H source class is already empty

Return to arbitrary coprime m,n>1 and the hypotheses of conclusion B.
All steps of section3 apply. In particular, comparing leading forms after
the inverse substitution gives, in C[x,y],

H^m=lambda*(U_M^a*V_N^b)^m.

Taking an m-th root of the nonzero scalar and using factorization in the
polynomial domain gives H=zeta*U_M^a*V_N^b for zeta!=0.
No assertion that psi is affine or that its leading coordinate forms are
independent is necessary.

Proposition5.20 preserves the endpoint (ma,mb), so Corollary7.9 gives
d=gcd(a,b)>2. Hence

H=zeta*h0^d,  h0=U_M^(a/d)*V_N^(b/d),

where h0 has degree D/d, strictly between0 and D. In particular
[H,h0]=0 while h0 cannot lie in C[H], whose nonconstant elements have
degree at least D. Thus ker[H,-]=C[H] is incompatible with the actual pair.

Here is the field point when the closedness assumption is over arbitrary K.
Choose F finitely generated over Q containing all coefficients of P,Q,H
and the nonzero bracket. The assumed equality over K implies the equality
over F: if q in F[x,y] centralizes H, write q=sum c_i H^i over K.
Homogeneity of positive-degree H separates the degrees iD; comparison
with a fixed nonzero monomial of H^i shows each c_i is in F.
For any extension E/F, take a finite F-linearly independent coefficient
basis e_1,...,e_t for an element q in E[x,y] and write q=sum e_i*q_i.
From [H,q]=0 follows [H,q_i]=0 for every i, hence q_i in F[H].
Therefore ker_E[H,-]=E[H]. Embed F in C and apply this observation:
closedness survives, contradicting the proper-power conclusion above.

The proper-power assertion itself also holds over an algebraic closure of
K. For the integer d supplied over C, absorb zeta into h0 there and write
the finite coefficient equations h^d=H for a homogeneous h of degree D/d.
Their coefficients lie in F and their complex solution makes the ideal
proper. Weak Nullstellensatz gives a solution over an algebraic closure
of F, which embeds over F into an algebraic closure of K. This is a
finite-witness existence argument only; no coefficient system is built or
solved. It is unnecessary for the closed-centralizer contradiction above.

This argument is independent of15w and all finite late-T/contact calculations.
It requires neither McKay–Wang's factor-count theorem nor a two-linear-factor
normal form for the original H. Those were useful screens but are unnecessary.
It excludes the full actual closed-H, coprime-nondividing-degree source class
for every D>0, so a new early-contact theorem within that SAME class would
not acquire a live JC2 client. A useful redesign must change the source
interface, for example allowing the genuine proper-power reference with all
kernel terms retained. That redesign is NOT proved or launched by this report.

## 7. Hostile self-checks and rejected stronger readings

- Cancellation control: without the rectangle's unique positive-weight
corner, degree preservation fails. With psi(x)=x+y^2, psi(y)=y, the two
tied terms of x-y^2 cancel to x. Our argument explicitly excludes that
failure by coordinatewise domination at an actual nonzero corner.
- Minimality control: Definition4.3, Proposition5.20, Theorem2.20 and the
FIRST assertion of Corollary7.9 are read separately from the nearby
minimum-B statements. Substituting Corollary5.21 would not prove the
given-representative assertion and is not done.
- Ratio control: arbitrary automorphisms do not generally preserve total
degree ratios. Here it is proved from TWO proportional rectangles plus
the inverse positive degree functional. Initially only g<=D is obtained;
g=25 follows from the exhaustive table, not an assumption.
- Polynomial-domain control: L^(1) can allow x^{-1}; we specifically invoke
the ordinary-input/ordinary-automorphism sentence of Proposition5.20.
The polynomial cone for S is a separate downstream accepted interface.
- Table control: swapped m,n are checked, and all rows of sum<=25 are
retained before filtering, including F18/F19. No "only small degree
counterexamples are minimal" shortcut is used.
- Centralizer control: if H=R^d for d>1, then R already centralizes H and
has smaller degree. Thus the genuine physical F2 H=u^5*v^20=(u*v^4)^5
falls OUTSIDE the closed-H class. This is consistent with B, not a
counterexample to it. Target c*g^2 receivers also fall outside B's
constant-J hypothesis.
- Automorphism control: triangular polynomial automorphisms with a
degree1 component are not forbidden by B: they fail m,n>1. The proof
cannot drop the nondividing-degree restriction.
- Authority control: the Strinz public manuscript at pinned HEAD
16ae8b263cb8355c0d107138034aa452444390ff already proposes this fixed-degree
standardization architecture. Its notes helped locate the exact question,
but their theorem ledger and checker claims are NOT proof authority here.
The shorter argument above independently bridges the literal primary
statements. No Strinz code, solver or checker was executed.
- No primary proof hidden in a citation is represented as locally
reproved. The source normal form, standard-pair theory, published chain
classification and accepted receiver chain retain their import perimeter.
A primary correction to one of those imports would require reassessment.

## 8. Provenance and read/replay limits

ML PDF SHA256:
455b57cdb9c4e45e04517f78e1b13d6645ccaed3353eaf0daf10f9f3ff092c65.
Root independently re-fetched this PDF and obtained the same hash; curl and
pdftotext were documentary reads, not mathematical computation. Root read
printed301–305 whole, including the used normal-form argument, and earlier
introductory context. No claim to a whole-paper read or replay of its
later reductions is made.

GGV primary local extraction:
box/census-coverage-20260905/core-ggv-layout.txt
SHA256 e3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1.
Root read the complete statements/proofs of Proposition5.20 and
Corollary7.9 and Definition4.3 in this extraction and compared primary
browser text; the full surrounding foundational theory is imported.

GGHV primary local PDF:
box/d108-published-case-interface-20260906/ggvh-algorithms-1708.07936v1.pdf
SHA256 e04e3bfd88c62346c467ec7c32f5bb236cdcb2ee4796525408c0c8d68632fcdb.
Its text extraction SHA256:
49df06d11bbc4556a9b09771cdd60ca40a75b7542d327bbb622e09434e6a467e.
Root read Theorem2.20's whole statement/proof, the section2.4 necessity
discussion/Remark2.24/Definition2.25, and section5's whole table text.
The intermediate Remark2.22 formulas and classification foundations are
named published imports, not a new full-paper proof audit. Browser
screenshot references did not display an image; no visual-table inspection
is claimed. Local primary text and browser table text agreed.

Accepted local mathematical interfaces (full report SHA256):
- xmodel/d125-published-chain-discriminator-astra-20260906.md:
9b439af269c23e349615d3e404e0732c9c7f491a9342d5500e061aab91ad4e88.
- xmodel/d125-published-chain-gate-fable5-20260906.md:
5be50d001d285481233c8de415b2f4d22411a22cb930a0c1db287c0579b3cd7b.
Its old terminal receipt was read FIRST again, then all16 current charged
and report pins passed at03:39:33.320246 before the whole gate read.
- xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md:
7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413.
- xmodel/d125-minimal-receiver-gate-fable5-20260906.md:
cd69c23885de119e4bd910992dad5ef695e7b12013168ec1c401546d8aa6ed8d.
The accepted status of this gate is imported, not a new gate re-audit.
- xmodel/d125-weightfree-client-interface-astra-20260909.md:
dcb3a30a48c5977005083a3ad7bbc5935e1f2f74ade6c3569a4b45751c213276.
- xmodel/d125-weightfree-reference-source-astra-20260909.md:
cbc0330b001faeb8692e45c3be3fdcd3c0727b5734e648143642234da5d63696.
The accepted15q corrected universal prose proof is the receiver premise.
Its earlier gate's prohibited computational controls remain EXCLUDED.
Neither those controls nor any mathematical subprocess was replayed here.

Report-to-report integration: chain, minimal-map and weight-free-client
reports were read whole, with current hashes checked before consumption.
The coefficient-bijective map and scalar rescaling discharge the WF
hypotheses literally. The fresh normal form discharges the previously
unresolved arbitrary75/125 source premise. Conclusion B instead composes
normalization with Corollary7.9, exposing the closed-H scope conflict.
No report is altered by this integration.

## 9. Disposition

Request different-model hostile review of three separate propositions:
the minimum-free fixed-degree standardization; its precise composition
to accepted15q excluding actual75/125; and the all-degree closed-H
source-emptiness consequence. A gap in one must not silently promote
the others. No new solver, large computation, source expansion, fleet
allocation, public release or formalization is authorized by this report.
Existing blind ideation remains frozen and independent. Until review,
both new conclusions stay provisional and JC2 remains unresolved.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20292`.
- Body SHA-256:
  `1cf96990638f584f4abe8d3f752533a25aa71b0112c2ed67293fdbf5e03868a0`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
