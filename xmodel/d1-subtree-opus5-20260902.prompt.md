# Research lane: D1-SUBTREE — the Jacobian condition below the last major disc (flagship effort; the one place no "next pair" argument has been run)

The N-ON-THE-TREE report (charged as a PROPOSAL — its review runs in
parallel; re-derive what you use) built the geometric degree N of a
Jacobian pair (f, g) onto Moh's tree: with t = x^{-1}, the roots
phi_j of f − c_1 and tau_i of g − c_2 in the Puiseux field, N = − sum_{i,j}
ord_t(tau_i − phi_j) (CONTACT-DEFICIENCY, monic GEN gauge; reviewed at
integration #15), equivalently (FRONTIER-N) N = sum over the g-frontier
of the positive parts of −lambda_f. It found: LEMMA DETECTOR-NULL — by
Moh Prop 6.1(2) / Theorem (5), every root of a MINOR disc with
ord g < 0 is a distribution detector (lambda_f = (m/n) lambda_g there),
so minor discs contribute exactly zero to N; THEOREM N-CEILING — the
major tower (Moh's Definition 5.1 data through the LAST major disc D_1,
of radius delta_1) gives N <= U = u d e (1 − delta_1)/(d + e), with NO
lower bound: the sub-tree of D_1 — the a_1 = e V_2 roots of g and
b_1 = d V_2 roots of f below radius delta_1 — is unconstrained by any
published condition (Moh's own minor criterion degenerates there: at
r = 1 it reads #roots <= n/(n + m) < 1, and there is no M_0), and it can
only ADD contact, i.e. LOWER N toward 0. OPEN[D1-SUBTREE] (bounded
quantity: N|_{D_1} = sum_{rho in D_1} (−lambda_f(delta^0_rho))^+ in
[0, a_1 (−lambda_f(delta_1))]). Every other instrument of the record
bounds N ABOVE or D BELOW; a ceiling D <= C(N) needs N bounded BELOW
by D — OPEN[UPPER-TO-FLOOR] — and the sub-tree of D_1 is the only
place the Jacobian condition has never been imposed.
Your task, flagship effort, creativity and directness: run the
Jacobian condition below D_1.
(1) SET UP the sub-tree exactly: the roots of f − c_1 and g − c_2 below
    radius delta_1 (after the major tower is fixed: n, m, M_1..M_s,
    d_1..d_s, V_1..V_s, delta_1..delta_s with delta_1 the last), their
    Puiseux expansions beyond the last characteristic exponent, and the
    contact orders ord_t(tau − phi) among them; write N|_{D_1} in terms
    of that data (re-derive FRONTIER-N restricted to D_1).
(2) IMPOSE [f, g] = 1 THERE. Moh's Lemma 2.1 (the Jacobian condition
    on the T_i / on the exponent tower) stops at the last characteristic
    pair; below it the two root families are "free" only in the sense
    that no CHARACTERISTIC exponent remains — but the Jacobian identity
    is an identity of power series in t, y and constrains every
    coefficient: expand [f, g] = 1 in the local coordinates of D_1 (the
    branch of f − c_1 at a root, the g-roots nearby) and derive the
    conditions on the sub-tree's contact orders. Is the deficiency at
    the bottom forced to be positive? Is there a MINIMUM of
    sum_{rho in D_1} (−lambda_f)^+ implied by [f, g] = 1 — i.e. can the
    sub-tree really drive N|_{D_1} to 0 while the pair stays Jacobian?
    Controls: for an AUTOMORPHISM (x, y + x^k) the whole tree is one
    tower with N = 1 — compute N|_{D_1} there; for the non-Keller
    two-tower controls of the charged report the value is known; the
    Jacobian identity must distinguish them.
(3) THE OTHER DIRECTION, HONESTLY: if the Jacobian condition below D_1
    is compatible with N|_{D_1} → 0 (contact unbounded), then exhibit
    the mechanism (which coefficients are free, and why [f, g] = 1 does
    not see them — e.g. because the Jacobian identity at that depth is
    an identity in the wrong variable), state THEOREM UPPER-ONLY (no
    boundary instrument bounds N below by D) with its exact hypotheses,
    and say what that means: the ceiling D <= C(N) is unreachable from
    the boundary; the all-degree program must use a global invariant
    (name candidates: the cofinal-invariant question of the 0741Z
    round; the affine ramification / Chevalley–Weil data on the Galois
    closure; the source-side étale structure of E = F^{-1}(A_F)).
(4) If a floor exists: price it — N >= L(skeleton) makes the filter
    two-sided; run it on the charged skeleton census (D <= 400, the
    delivered box/moh_skeleton_N.py can be extended) and report which
    (N, D) cells die, against MOH-SHARP-2 (D_min >= 105) and the cells
    (B2)/(B3) at 4 <= N <= 16.
Discipline: the N-ON-THE-TREE report is a PROPOSAL (re-derive
FRONTIER-N, DETECTOR-NULL, N-CEILING before use); DEPTH-CEILING's
reviewed items at their scopes (DEPTH-LOG, PLACE-LEDGER, CONTACT-
DEFICIENCY monic GEN, NU-TWO, MOH-SHARP-2); Moh 1983 from refs/ (hash);
no case (A), no A2, no Z(G) = 1. Desk-scale CAS (< 15 min, < 4 GB); state
the bounded quantity of every OPEN you raise; do not edit canonical
ledgers; do not inspect jc2-lean.
Report: xmodel/d1-subtree-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/n-on-the-tree-opus5-20260902.md
charged_input=xmodel/depth-ceiling-opus5-20260902.md
charged_input=xmodel/depth-ceiling-review-gpt55-20260902.md
charged_input=xmodel/integration15-coordinator-fable51-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
44223b324641e75be374f09c4b6daead796937d3176d8841844551e2d19c3967  {{LANE_INPUTS}}/n-on-the-tree-opus5-20260902.md
863b05dbbd425035a09265cacdf6c418a2a3a1a7fadbeb303571bb5ccba618d6  {{LANE_INPUTS}}/depth-ceiling-opus5-20260902.md
4a171d910e8e7308ed958a539f97c53e01abcee62239581564ef03fca0031421  {{LANE_INPUTS}}/depth-ceiling-review-gpt55-20260902.md
8116bc656f46647a111675f49051f363030fe9f852be66ddaf77d86b97de9e4c  {{LANE_INPUTS}}/integration15-coordinator-fable51-20260902.md
```
