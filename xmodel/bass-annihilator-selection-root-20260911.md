# Bass annihilator selection: the exceptional factor cannot be generically avoided

ROOT manual research, September11 2026. Transaction first action21:04:52UTC;
original publication reserve21:22UTC, HARD21:25UTC, no extension.
Evidence INTERNAL/UNREVIEWED, conditional on the named Bass source results.
This is not a JC2 proof, a source realization or a novelty claim.

## Input and scope

Primary Bass1989 PDF, box/bass-resonant-operators-root-20260911/bass-1989.pdf,
SHA25686f642941d2cea0f1d438996d8e81833ac53b6039c4c81e1564adc411f614b1e.
Whole parsed mathematical article read; printed41--43 and49 independently
visually inspected. Source-intake record names exact coverage and limits.
No other live research report is an input. Standard Siegel/Fabry/Luroth
results in Bass are externally trusted, not proved anew here.

Two further frozen primary inputs were added before conclusion: van den
Essen1993, Eulerian operators and the Jacobian conjecture, printed373--378,
box/bass-resonant-operators-root-20260911/vandenessen-1993.pdf,
SHA25607f29ddee54e89cfc38b5b228518347799995c06ad359b952eb952f511253db4;
whole parsed text and visual377--378. Adjamagbo1210.5281v1,
box/bass-resonant-operators-root-20260911/adjamagbo-1210.5281v1.pdf,
SHA2560428a76949b3e469f0186053110831b9d97d2efc23f15ed161fa29275fd2d6ad;
parsed article read, visual construction on p3, original Kulikov result
externally trusted. These later inputs narrow the proposed scope; no
unavailable primary or agent draft is silently imported.

Set A=C[p,q], R an actual plane Keller source, N=R/A,
e_p=p partial_p, e_q=q partial_q, delta=p partial_q, e=e_p+e_q,
U=C[e_p,e_q,delta]. Bass1.1 supplies U-torsion of R and N;1.2 supplies
injectivity of delta on N;1.5 says an annihilator whose diagonal part has
no special-linear factor forces its class in N to vanish. The latter follows
for equations Phi f in A by subtracting the finite homogeneous truncation,
as Bass explains on printed41. Homogeneous pieces of f need not lie in R
as an infinite collection; only their finite sum is subtracted in A.

## 1. Generic annihilator selection cannot avoid resonance

For nonzero z in N set I_z=epsilon(Ann_U(z)), where the algebra map
epsilon:U->C[e_p,e_q] sets delta=0. This is a polynomial-ring ideal.
The commutators [e_p,delta]=delta, [e_q,delta]=-delta show delta is normal
and U is the corresponding skew polynomial ring. Given a nonzero
annihilator, its least delta exponent can be factored on the LEFT:
Phi=delta^k Psi, epsilon(Psi)!=0. Delta acts injectively on N by Bass1.2;
hence Psi z=0. Therefore I_z is nonzero.

Every nonzero member of I_z is divisible by some special-linear polynomial
ell=a e_p-b e_q-c, otherwise Bass1.5 forces z=0. In fact ONE such ell
divides EVERY member of I_z. Choose polynomial-ideal generators h_1,...,h_t.
If no ell divides all of them, for each of the countably many normalized
special-linear ell, the coefficient vectors lambda in C^t satisfying
ell | sum lambda_i h_i form a proper linear subspace. A finite-dimensional
complex vector space cannot be covered by countably many proper linear
subspaces (equivalently choose a polynomial parameter curve avoiding their
countably many finite exceptional sets). Some combination would have no
special-linear factor, a contradiction. Thus 0!=I_z is contained in (ell).

This is conditional on Bass's inputs, not a new properness argument. The
common factor may depend on z; no single resonance is asserted for all N.
It shows why merely choosing generic linear combinations of annihilators
cannot remove the exception. Neither individual-annihilator factorization
nor I_z membership supplies a factorization of operators in U.

## 2. The stronger existing result identifies a coordinate order

The later van den Essen paper changes the relevant boundary. After its
generic translation/normalization, N is p-torsion-free, intersection_k p^k N=0,
and N/pN embeds in C[[q]]/C[q]. These are its nice-map hypotheses and
conclusions, not consequences of arbitrary formal coordinates. Every actual
Keller map admits such a normalization by its Proposition3.1.

For z!=0 let r be its finite p-adic order in N: z=p^r z_0 with z_0 not in pN.
Write Phi=sum_i delta^i Phi_i(e_p,e_q). Since delta commutes with p,

  Phi p^r = p^r sum_i delta^i Phi_i(e_p+r,e_q).

Cancel p^r on N and reduce modulo pN. Every delta^i term with i>0 vanishes,
and e_p=p partial_p acts as zero there. Thus any Phi z=0 gives

  Phi_0(r,e_q) [z_0]=0 in N/pN.

For every nonzero polynomial h, h(q partial_q) has no torsion on
C[[q]]/C[q]: beyond finitely many roots h(n)=0, its coefficient action is
invertible, so h(q partial_q)f polynomial forces f polynomial. Therefore
Phi_0(r,e_q) is the ZERO polynomial. Equivalently, e_p-r divides Phi_0 for
EVERY annihilator of z. This is the proof mechanism of Theorem4.1, not a
new theorem claimed independently of that source.

Consequences for allocation:

- Positive a,b in a e_p-b e_q-c give no coordinate factor e_p-r. Such a
  diagonal is ALREADY excluded for arbitrary higher delta terms by4.1 in
  the normalized actual-Keller setting, not a new source frontier.
- The remaining coordinate-resonant case is real in the method: a factor
  e_p-r in Phi_0 does not imply e_p-r divides Phi on either side. It records
  the p-order of a hypothetical nonzero class, rather than contradicting it.
- Root-controlled weighted leading terms of formal germs cannot be presumed
  to lie in R. The nice-map quotient embeds into formal series; it is not
  known to equal C[q]. Proving generic fibre functions polynomial would be
  an additional source theorem, not a harmless completion step.

Negative control: z=1/(1-q) modulo C[p,q] in
C[p,q,(1-q)^-1]/C[p,q] has p-order0 and is killed by e_p. This module is
p-separated and p-torsion-free, and its p-quotient embeds into
C[[q]]/C[q]. Its rational etale-open source has a nonconstant unit, so it
is not a Keller-plane counterexample. It illustrates that coordinate
resonance and the displayed quotient facts alone are consistent.

## 3. Source category cannot be weakened to Bass's broad hypotheses

Adjamagbo's Theorem1, using Kulikov's original construction, supplies a
nontrivial degree-three etale map from a smooth rational affine factorial
simply connected surface with only constant units to A2. The source is
NOT A2. Thus even these combined generalized-source conditions do not
resolve JC2. No independent reconstruction of the degree-three map or its
fundamental-group theorem is asserted here.

A short topological check makes one missing source condition visible.
In the printed generic construction, blow up P2 at the node of a cubic;
remove its strict transform and the strict transform of a generic conic
through that node. Both strict transforms are P1. Their intersection
number is 3*2-2*1=4, with four distinct transverse points generically.
Hence compact-support Euler characteristic is

  chi_c(S)=chi(P2 blowup)-(2+2-4)=4,

not chi_c(A2)=1. Under the usual affine-surface CW and de Rham comparison
facts, simple connectedness then gives b2(S)=3, not the source H2=0 used
by the campaign trace theorem. This manual check is conditional on the
printed construction and named standard topology, not a primary audit of
Kulikov or a new proof of its general assertions.

## 4. Disposition

NO_CLOSING_IMPLICATION from generic annihilator selection. The stronger
1993 source theorem supersedes the 1989 exception list as the current
allocation boundary. A bounded algebraic-germ test of a coordinate-resonant
family is meaningful only with the explicit missing arrow: no theorem yet
puts an arbitrary Keller annihilator into that family. No new external
degree bound, source realization, global proof or counterexample follows.

This is targeted history/primary integration and manual algebra. No science,
AWS, agent-draft intake, global ranking change, or automatic re-review. The
three retained PDF pins were checked before finalization. No novelty claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7994`.
- Body SHA-256:
  `dbcea0a6883d7992d745384e5dea0211897236e92735a9c24ea548753d85bc2d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
