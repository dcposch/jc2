# Desk lane: SING-WITNESS — does a fixed-N family with unbounded pencil genus exist with SINGULAR A_F?

Reviewed (charged review of KELLER-PENCIL-GENUS): THEOREM NEG-GENUS —
at every fixed N >= 2 the genus g_L of the generic member of the pencil
<P, Q> is unbounded in the class of dominant polynomial maps
(psi_k∘(x, x y^m)); THEOREM PROFILE-WITNESS — at N = 4 the non-Keller
family psi_k∘(x, x y^4 − y^2) (Jac = 2y(2xy^2 − 1)) matches [P3], (C1),
7.B', (K), the meridian cycle type 1^2·2 and an irreducible one-place
A_F, with g_L = 0, 3, 4 at k = 1, 2, 3 — but its A_F is SMOOTH, which
SMOOTH-KILL forbids for a Keller map. The reviewer raised
OPEN[SING-WITNESS]: is there a fixed-N family of dominant maps with
g_L → ∞ whose A_F is SINGULAR (a cusp, or the (B3) profile: one cusp
plus double points), matching the same ledger? Bounded quantity: the
pair (n, delta_aff) along the family. "A second door, not hygiene": if
NO such family exists, the singularity structure of A_F is the datum
that bounds the genus — the campaign's missing ceiling would then be a
statement about how the affine singularities of A_F cap the fork mass;
if one exists, the profile ledger is provably blind to the genus even
with singular A_F and the ceiling must use Jac F ∈ C^* in a way no
ledger sees.
Task, exact and computational (sympy / Singular-free preferred; refs/
only): (1) Construct candidates: compose the NEG-GENUS families with
target automorphisms that make A_F singular (a target automorphism
does not change A_F's type — so instead vary the SOURCE map:
(x, x^c y^m + h(x, y)) with h chosen so that the non-properness curve
acquires a cusp; use Chau's description of A_F for maps of the form
(x, g(x,y)) and the dicritical parametrisation to force a (2,3) cusp
or a node; verify A_F, its singularities, N, n, delta_aff, the meridian
cycle type, W, a, and g_L for k = 1..4 by CAS. (2) If a family with
g_L → ∞ and A_F singular exists at some fixed N (try N = 3, 4, 6):
exhibit it with all data, and state which banked profile constraints
it matches ([P3], (C1)–(C3), 7.B', (K), the cusp cage) and which it
violates. (3) If your candidates all fail (e.g. making A_F singular
forces the genus to stabilise or the map to lose the profile), extract
the reason and state it as a candidate theorem with its exact
hypotheses (the "door"): what about a singular A_F bounds the fork
mass Psi of the polar tree? (4) Controls: the automorphism family
(g_L = 0 always) and the PROFILE-WITNESS family reproduced. Discipline:
consume NEG-GENUS, PROFILE-WITNESS, FORK-GENUS, ESCAPE-KAPPA at the
review's CONFIRMED typing; MPRIME and DEG-AF at reviewed typing; case
(A) EMPTY; no Z(G) = 1; no A2. Desk-scale CAS (< 15 min, < 4 GB); state
the bounded quantity of every OPEN you raise; do not edit canonical
ledgers; do not inspect jc2-lean.
Report: xmodel/sing-witness-gpt55-20260902.md
Seal-at-completion; bounded writes; target 12-20KB; 75 minutes.
charged_input=xmodel/keller-pencil-genus-opus5-20260902.md
charged_input=xmodel/keller-pencil-genus-review-grok46-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/deg-af-vs-n-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1  {{LANE_INPUTS}}/keller-pencil-genus-opus5-20260902.md
d57d17f8eb6e776013d283e6796bef0db256088011dae2b73d1383c1e40cc56a  {{LANE_INPUTS}}/keller-pencil-genus-review-grok46-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  {{LANE_INPUTS}}/deg-af-vs-n-opus5-20260902.md
```
