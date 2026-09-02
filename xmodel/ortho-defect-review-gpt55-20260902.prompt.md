# Hostile review lane: ORTHO-DEFECT, ORTHO-FLOOR, ORTHO-DIV, ORTHO-SPLIT, DESCENT-DEGREE, and the retyping NO-CEILING -> NO-CEILING[SINGLE-CLASS]

The charged Opus round submission (ideation 1608Z, sec.1-4) claims, for
a dominant polynomial map F = (P, Q) with p = deg P = Kd, q = deg Q = Ke,
gcd(d,e) = 1, and m_nu, m'_nu the multiplicities of the generic members
of the pencils {P = c}, {Q = c'} at the common infinitely-near base
points nu at infinity (total-transform basis): (1) THEOREM ORTHO-DEFECT:
sum_nu (e m_nu - d m'_nu)^2 = (ep - dq)^2 + 2 d e N, = 2deN under
ep = dq; needs NO Keller, NO H2, NO gauge; (2) COROLLARY ORTHO-FLOOR:
N >= (1/2de) sum_{nu in S}(e m_nu - d m'_nu)^2 for EVERY subset S of
the cluster; (3) COROLLARY ORTHO-DIV: #{nu : d does not divide m_nu}
<= 2deN (uses gcd(d,e) = 1, d >= 2); (4) ORTHO-SPLIT: the two base
clusters coincide except at O(N) points; (5) LEMMA DESCENT-DEGREE:
N(P, beta^d P^e - alpha^e Q^d) = d N; (6) the retyping of THEOREM
NO-CEILING (n-vs-mapdeg-opus5, sec.3.7, charged) to NO-CEILING[SINGLE-
CLASS]: its proof concerns one class Z = DH - sum a_i E_i and does not
cover the pair (C_u, C_v) with C_u^2 = C_v^2 = 0, C_u.C_v = N and
H-components in ratio d:e, whose difference Delta = eC_u - dC_v has
Delta.H = 0 and Delta^2 = -2deN < 0; (7) NOETHER-K is the p = q
one-vector specialisation. The coordinator's blind submission (charged)
stated the same identity as (LATTICE) from A^2 = B^2 = 0, A.B = N.
Integration #17 (charged) binds D1-PIN/D1-STAR, which give an exact
formula for N; ORTHO must be consistent with it term by term
(the vanishing terms are the proportional discs; the nonzero terms live
at the star separation below delta_1).
Your task, hostile and computational: CONFIRMED / GAP / REFUTED per
item with the exact line and repair. Mandatory: (a) reprove ORTHO-DEFECT
from the intersection theory of a common resolution (state exactly what
"the generic member's multiplicity at an infinitely-near point" means
when the two pencils' base loci differ, and whether the total-transform
basis is orthonormal after the union of the two clusters); (b) the
three desk controls ((x,y), (x,y^2), (y^2+x, y^3+3/2 xy)): rerun with
your own hand resolution and sympy resultant; add ONE control with
d != e and N >= 2 that is not an automorphism (e.g. a non-Keller pair)
and one Keller automorphism in Moh's gauge; (c) ORTHO-FLOOR: is the
subset inequality valid when the term (ep - dq)^2 is nonzero (the
producer's gauge normalisation) — state the exact hypothesis; (d)
ORTHO-DIV and ORTHO-SPLIT: reprove; (e) DESCENT-DEGREE: reprove
(Moh's G_1 = beta^d P^e - alpha^e Q^d); (f) the NO-CEILING retyping:
read n-vs-mapdeg sec.3.7 and say whether its single-class scope is as
claimed and whether the pair negativity Delta^2 = -2deN is new
information beyond A.B = N (it is an identity, so decide whether the
"retyping" changes any bound the record has drawn from NO-CEILING —
integration #14 sec.C and #16 sec.C); (g) consistency with D1-PIN: on
Moh's (64,48) row (charged in D1-SUBTREE), evaluate both sides of ORTHO
using the star bottom and confirm 2deN = 24N with N = 9; (h) the
producer's sec.3 satisfiable arithmetic solution at (64,48), N = 4
(40 points (1,1), 14 points (1,2)) — is it consistent with the
Enriques proximity inequalities, and does D1-STAR now exclude it?
Deliver a typed verdict block with a promotion recommendation per item,
what ORTHO CAN and CANNOT decide, and the bounded quantity of any OPEN
you raise. Desk-scale CAS only; do not edit canonical ledgers; do not
inspect jc2-lean.
Report: xmodel/ortho-defect-review-gpt55-20260902.md
Seal-at-completion (seal with the standard <!-- BODY-END --> marker);
bounded writes; target 20-30KB; 75 minutes.
charged_input=xmodel/ideation-20260902T1608Z-opus5.md
charged_input=xmodel/n-vs-mapdeg-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/ideation-20260902T1608Z-fable51-coordinator.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
0916a85a7a8090d04461fa356518fb2ffd877374d1b8452a2b808d6f77156934  {{LANE_INPUTS}}/ideation-20260902T1608Z-opus5.md
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  {{LANE_INPUTS}}/n-vs-mapdeg-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
b404282f3c366a98dbcc745bcfb88cf64293cb17c6004ae784ce00f920c15bd2  {{LANE_INPUTS}}/ideation-20260902T1608Z-fable51-coordinator.md
```
