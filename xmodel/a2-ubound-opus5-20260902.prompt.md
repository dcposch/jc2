# Research lane: A2-U-BOUND — the one-cusp horn's missing finisher (flagship effort)

The reviewed RAY theorem set (charged: ray-kill + its GPT-5.5 review +
the N2 derivation) leaves the one-cusp A2 horn as an explicit residual:
on the E1-wall (g = 2e, G_{2e} = -b(1+2e) eta_e^2, HORN-A2) with
deg E1 <= 2e-2 (RAY-2), the cells (e,U) with U == e (mod 2),
U >= 3e+2, m = U, n = U-e, 2 sigma = U+e, are each finite and
decidable — box01 is emptying them one at a time ((1,3),(1,5),(1,7)
EMPTY so far, MODULAR certainty; (1,3) two-engine) — but NOTHING bounds
U in terms of e (OPEN[A2-U-BOUND]), so no finite computation decides
even one value of e. Your task, flagship effort: PROVE a bound
U <= B(e) on the live section — or, better, prove the residual empty
uniformly in U — or exhibit the exact structural reason no bound
exists. Creativity and directness are wanted; a partial uniform
theorem with a named gap beats a survey.

Leads, in the order I would try them (reorder or add freely):

(L1) THE TWO MISSING EQUATIONS. Ray-kill records OPEN[A2-O0-O1]: of the
   seven residual equations O0,O1,O2,E0,E1,E2,E3 of the spec (charged,
   spec:76-114), O1 is ABSENT from the reviewed record and O0 is
   present only through its consequence (2.2). The order-by-order
   ladder fails to terminate because each order gives FOUR linear
   conditions on FIVE new coefficients. Two more independent equations
   per order make it SIX on FIVE. Transcribe O0 and O1 in full from the
   spec, put them on the wall in ray-kill's closed form (sec 3.1: E1 as
   the free object, Theta = s E1/eta, D1, Phi, C1 as displayed), and
   redo the order-(top-1) and order-(top-2) analysis with all six.
   First decide whether O1 is independent of the other six on the
   wall; if it is a consequence, say so exactly and move on.
(L2) THE ORDER-SIDE LADDER AT Z = 0. C32 sec 1 proves the degree (Z at
   infinity) and order (Z = 0) calculi are formally identical, and Z=0
   is special in the system (explicit Z factors in E2, D2, C2, and the
   2 kappa Z term). Every pass so far (HORN-A2, RAY-*) worked only at
   infinity. Run the dual analysis at Z = 0: dual chambers in
   (epsilon = ord eta, nu = ord G), dual wall nu = 2 epsilon,
   G_{2 epsilon} = -b(1+2 epsilon) eta_epsilon^2, i.e.
   ord E1 >= 2 epsilon + 1. Against deg E1 <= 2e-2 this squeezes E1
   from both ends; if eta is a monomial (epsilon = e) it forces E1 = 0
   outright. Note that at (1,3) the order-(top-2) condition forced
   eta = eta_1 Z, a monomial. Decide whether eta is forced monomial in
   general, and what E1 = 0 does to the whole system (C32 sec 6 did
   E1 = 0 only under r' = 0).
(L3) THE UNIT WRONSKIAN. E0 is 2(q r' - p' s) = kappa, a nonzero
   constant: gcd(q,s) = gcd(r',p') = 1 and the four polynomials are
   tied by a unit Wronskian. Combine with T1 (eta divides s E1) and
   Mason-Stothers / abc for polynomials to bound U by root counts; hunt
   a first integral or a second exact identity among q, r, s, p' that
   makes the count bite. The ray pins r_n = s_sigma^2/(4 b eta_e^2) and
   q_m = 3a s_sigma^2/(4 b^2 eta_e): test the ansatz that q and r are
   s^2/eta-type expressions up to lower order and see how far the
   equations force it.
(L4) THE GLOBAL COUNT. Per cell, equations minus unknowns grows like
   5U/2 + 5e, yet the per-order ladder sees only 4 against 5. The
   excess lives in the middle coefficients. Eliminate q, r, p' (or
   whichever family is easiest) to get a single differential-resultant
   condition on (eta, s, E1) and read a degree bound off it.
(L5) THE NEGATIVE ROUTE. If no bound exists, construct the obstruction:
   a formal-series or infinite-U family satisfying every equation on
   the wall. A positive-dimensional solution as U grows would be a
   counterexample-level object for this horn — report it as such with
   the exact residual, never as a kill.

Discipline: consume C32 T1-T5, HORN-A2, RAY-1/RAY-DEP/RAY-EDGE/RAY-2
and the N2 derivation at their reviewed typings; the box01 cell
EMPTYs are MODULAR-certainty evidence, not theorems — do not consume
them as theorems. Exact CAS (sympy, rational arithmetic) is allowed at
desk scale only: no single job over about 15 minutes on this machine
and no job over about 4 GB; anything bigger is a job spec for the
coordinator (msolve 0.10.1 + qqideal are live on box01). Do NOT
normalise s_sigma (ray-kill (C5)); a = b = eta_e = 1 are legal.
Do not consume Z(G) = 1 or any (B3) transfer — the A2 horn and the
(B3) cage are separate fronts acting on different objects.
Report: xmodel/a2-ubound-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/ray-kill-opus5-20260902.md
charged_input=xmodel/ray-kill-review-gpt55-20260902.md
charged_input=xmodel/n2-derive-gpt55-20260902.md
charged_input=xmodel/cell-32-spec-sol56-20260901.md
charged_input=xmodel/cell-32-termination-opus5-20260901.md
charged_input=xmodel/horn-flagship-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
3d08b8996227e292d76e0ba3901cfad16099f347f97129d27b6bf5b3bc253f0a  {{LANE_INPUTS}}/ray-kill-opus5-20260902.md
df5612152d60496bb81311ee9183d3c580759a2549d6ea8945a487d284976fcf  {{LANE_INPUTS}}/ray-kill-review-gpt55-20260902.md
4116a4e2fbd89a7c041f7eaea48d5199709f3f457ebcbf5397770391e8bd0c66  {{LANE_INPUTS}}/n2-derive-gpt55-20260902.md
86caf003268ddc40143daa68d439079dbd82d1dac41e1da93f33a661d52f96ac  {{LANE_INPUTS}}/cell-32-spec-sol56-20260901.md
d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b  {{LANE_INPUTS}}/cell-32-termination-opus5-20260901.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
```
