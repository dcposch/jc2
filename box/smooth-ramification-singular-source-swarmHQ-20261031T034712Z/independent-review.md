# Smooth ramification support: hostile finite-algebra review

Verdict: PASS
Review completion UTC: 2026-10-31T03:40:24.431388+00:00
Task: smooth-ramification-singular-source-review-sol56-20261031T0330Z
Configured model: gpt-5.6-sol/ultra
Hosted identity: UNVERIFIED
Exact candidate: CANDIDATE.md, SHA-256 34498d1337e1d47a5bbb0e1b2520bcb4f7070559dd5e049ea1e54c2a713f33fb
Frozen public basis: 68e87443925f50914a6cbb858d9d2f061dbda8b3

## Result

No fatal defect was found. The exact candidate proves a finite-flat degree-four map
from a normal singular quadric cone whose entire reduced non-etale support is one
scheme-smooth, non-Cartier affine line. It does not realize the whole polynomial
A2 source and does not resolve any global Keller or JC2 question.

## Independently checkable argument

Let f=T^4-6PT^2+QT-3P^2. The substitutions
a=T, b=P-T^2, c=(Q-12PT+4T^3)/3 give 3(ac-b^2)=f, and substitution
back into P=a^2+b and Q=3c+12ab+8a^3 fixes P,Q,T. Thus
B is exactly C[P,Q,T]/(f). Monicity injects C[P,Q] and makes B free
with basis 1,T,T^2,T^3; h is finite flat of degree four.

The irreducible cone ac-b^2 is a hypersurface domain. Its gradient
(c,-2b,a) vanishes only at the origin. Hypersurface Cohen-Macaulayness
and regularity in codimension one give normality by Serre's criterion.
At the origin, embedding dimension three exceeds dimension two, so X is singular.

For the monogenic presentation,
Omega_(B/C[P,Q])=(B/(f_T))dT and f_T=4a^3-12Pa+Q=3c.
Finite-flat plus unramified iff etale therefore gives etale locus D(c).
Moreover B/(c)=C[a,b]/(b^2), so sqrt((c))=(b,c) and
B/(b,c)=C[a]. Hence E=V(b,c) is the complete reduced non-etale support
and is scheme-smooth. The Fitting/different scheme is V(c), not E;
generically its divisor is 2E. There is no hidden second ramification component
and no conflation of reduced support with the reduced different.

At the generic point of E, a is a unit, b is a DVR parameter, and c=b^2/a.
The image divisor is the irreducible cusp g=Q^2-64P^3=0, and in that DVR
g=b^3(8+9b/a^2). The parenthesized factor is a unit, so the transverse
ramification index is exactly three. Also a=Q/(8P) in the cusp function field,
so the residue degree is one.

With m=(a,b,c), the classes of b,c are independent in
(b,c)/m(b,c). Nakayama therefore rules out a principal ideal at the origin:
E is not Cartier there despite being a smooth curve. Setting P=Q=0 gives
f=T^4, so the finite target-origin fibre is supported only at the source origin.
On E, (P,Q)=(a^2,8a^3); thus a is precisely the cusp-normalization parameter.

Finally, X-E=D(c) and B[c^(-1)]=C[b,c,c^(-1)] via a=b^2/c.
The complement is A1 times G_m, with a nonconstant unit, and is not A2.

Named foundations used: monic-quotient freeness; the Jacobian and Serre
normality criteria; hypersurface Cohen-Macaulayness; monogenic relative
differentials; finite-flat unramified/etale equivalence; DVR ramification;
Nakayama's lemma; and normalization of the plane cusp. No source audit is claimed.

## Exact limitation

This is a local counterexample to inferring ambient source smoothness from
normality, finiteness, and one smooth reduced ramification-support curve.
It neither supplies an actual polynomial Keller pair nor repairs the source to
have whole-A2 complement. The actual-normalization smoothness/Cartier alternative
and the whole-A2 problem remain unresolved. No novelty claim or successor is authorized;
ROOT alone decides promotion.

## Reading and process audit

Startup ACK was written at 2026-10-31T03:36:11.364661+00:00 and made mode 0444.
The required-reading draft was saved at 2026-10-31T03:38:37.071991+00:00;
the findings draft was saved at 2026-10-31T03:39:56.287251+00:00.
The copied reader SHA matched its pin before body access. Preflight verified the
complete packet, including MANIFEST and all three declared canonical seals.

Packet body reading was 1934 unique nonSTATE LF in 44 windows and 185 unique
STATE LF in 10 windows. NonSTATE breakdown: MANIFEST 239; HQ governors
23+112+162+259+519; public governors 22+102+107+36; ADMISSION 52;
CANDIDATE 64; RANK-ZERO 126; GLOBAL-GAP 111. Packet-body repeats: 0 LF.
The prompt duplicated 58 LF of PUBLIC-AGENTS and PUBLIC-FALLACY-v2, giving a
conservative 1992/3000 nonSTATE LF charge. STATE was 185/200 LF.

One sequencing deviation is disclosed: HQ-RESEARCH_POLICY first returned
next_start 95, but an already precomposed call began at 97. Exact lines 95-96
were then recovered through the pinned reader in a separate two-line window.
All required lines were read exactly once before mathematical review; no clipped
line received credit. Observed report/ACK body readbacks or automatic previews:
0 LF—the visible write results contained metadata only. Helper-source reading
credit was 0 LF.

Only the authorized ACK and report were authored. No web, history, repository or
source query, Git action, CAS/scientific computation, secondary model, model probe,
scratch/helper file, automatic retry, extension, protected-tree access, or other
artifact write occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5063`.
- Body SHA-256:
  `05b6e5d3fb204c06807ef81eb7e674417235049ebe4c232ad205ef26ed66bc0a`.
- Frozen basis: `68e87443925f50914a6cbb858d9d2f061dbda8b3`.
