# Research lane: CUSP-A-N8-GATE — a NEW gate for the case-(A) survivors at N = 8 (flagship effort)

Under H2, MPRIME case (A) — A_F topologically A^1 with one (p,q) cusp,
hence by Lin–Zaidenberg A_F is equivalent to the curve x^p = y^q and
G = pi_1(C^2 minus A_F) = <alpha, beta | alpha^p = beta^q> — is EMPTY
for 4 <= N <= 7 (THEOREM CUSP-A-EMPTY, reviewed) and NONEMPTY at N = 8
under the full promoted arsenal. The charged CASE-A-SWEEP leaves, at
N = 8: the trefoil cell (2,3)/(3,2) — 16 representations, dicritical
(s,mu) = (2,3), a = 2, j = 2, M = 4, kappa = 2, image of order 24,
H_1 of the cover rank 2 torsion-free — and the (3,4D)/(4D,3) family —
6 + 4 representations, dicritical (1,4), a = 4, j = 3, M = 4,
kappa = 2, image of order 192. All REPRESENTATIVE (group data, not
realized curves). OPEN[HOMCOVER-CUSP-A-N8]. Every gate in the arsenal
(numerical cage, CUSP-PARITY, meridian cycle type, HOM-COVER rank and
torsion, 7.B, Lemma A, the (K) excess ledger) has been applied and
passed. Your task, flagship effort: find and apply a NEW gate that
decides these survivors — kill them, or show exactly why they survive
every homological gate and name the geometric datum that is missing.
Creativity and directness are wanted.

The lever I would try first. Over C^2 minus A_F the Keller map F is
proper (A_F is by definition the non-properness set), so
Y = C^2 minus E, with E = F^{-1}(A_F), is the FINITE unbranched degree-N
cover classified by rho, and pi_1(Y) = H = the stabiliser subgroup of
rho, an explicit index-N subgroup of the torus-knot group
(Reidemeister–Schreier). F is étale, so E has exactly a singular
points, each ANALYTICALLY a (p,q) cusp, j components, and behaviour at
infinity pinned (to the extent the charged record pins it) by the
dicritical data. Everything a plane-curve complement must satisfy is a
gate on H:

(G-A) ALEXANDER / LIBGOBER DIVISIBILITY. Compute the single- and
   multi-variable Alexander polynomials of H by Fox calculus on its
   Reidemeister–Schreier presentation. Libgober: the Alexander
   polynomial of an affine plane curve complement divides the product
   of the local Alexander polynomials at the singular points and the
   Alexander polynomial of the link at infinity. The local factor of a
   (p,q) cusp is (t^(pq) - 1)(t - 1)/((t^p - 1)(t^q - 1)), a copies.
   Write down what the charged record pins about the link at infinity
   of E (places, multiplicities, the dicritical data) and what it does
   not. Decide whether each survivor's Alexander polynomial divides the
   allowed product. This is OPEN[HOMCOVER-MODP-DIVISIBILITY] of the
   charged homcover-transfer, made concrete.
(G-B) CHARACTERISTIC VARIETIES AND MOD-p BETTI JUMPS. For each survivor
   compute dim H^1(H; F_p) for small p and the first characteristic
   variety of H; compare with the Libgober–Arapura constraints for
   complements of curves with only cusps and the pinned infinity.
(G-C) EULER AND H_2. A_F is contractible, so chi(C^2 minus A_F) = 0 and
   chi(Y) = 0, i.e. chi(E) = 1. Combine with b_1(Y) = j (HOM-COVER) and
   Alexander duality to get b_2(Y) and the exact identity that
   (a, j, genera, places at infinity, cusps) of E must satisfy; test it
   on each survivor. State exactly which of these numbers the charged
   record pins; a mismatch is a kill, a free parameter is a typed gap.
(G-D) THE SMALL CASE BY HAND. In the trefoil cell the image has order 24
   acting transitively on 8 points (point stabiliser of order 3): the
   cover Y is pulled back from a finite cover of the trefoil complement
   in C^2. Identify Y explicitly and decide directly whether it can be
   a plane-curve complement with two (2,3)-cusps and two components.

(2) CUSP-A-KAPPA. The charged sweep conjectures that every kappa = 1
   cage cell dies at the meridian cycle-type gate at every N. Prove it
   (a statement about cycle types of rho(m) against transitivity in the
   torus-knot group) or give the exact obstruction; a proof
   reorganises the all-N problem into the kappa >= 2 cells.

(3) Typed ledger: for each of the 26 survivors, which gate kills it or
   none, with the computation shown or scripted. box/cover_h1.py is the
   banked HOM-COVER instrument you may reuse — copy it, do not modify
   it in place; box/covergeo.py is adjacent. Pure python/sympy
   preferred; no sage assumed.

Discipline: consume CUSP-A-EMPTY, CENTRAL-RANK, ORBIFOLD-CAGE,
CUSP-PARITY, NO-PUSHFORWARD, the MPRIME theorems and the sweep's
counts at their reviewed typings (the sweep's N=9 spot data and family
collapse are MEASURED). The survivors are REPRESENTATIVE group data —
do not claim realization or non-realization beyond what a gate proves.
Do not consume any (B3) transfer or Z(G) = 1. Exact desk-scale
computation only: no single job over about 15 minutes or 4 GB on this
machine; larger enumerations are a job spec for the coordinator.
Report: xmodel/cusp-a-n8-gate-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/case-a-sweep-grok46-20260902.md
charged_input=xmodel/homcover-transfer-opus5-20260902.md
charged_input=xmodel/homcover-transfer-review-gpt55-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
6fa3447c0bdbc28347f287820bd95ea11c2fec37b3310d20adc8da3a75c87ea1  {{LANE_INPUTS}}/case-a-sweep-grok46-20260902.md
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  {{LANE_INPUTS}}/homcover-transfer-opus5-20260902.md
fadc17c809e72d64a493fc1fb16a739d441474b401f191081303de3b003d7d62  {{LANE_INPUTS}}/homcover-transfer-review-gpt55-20260902.md
```
