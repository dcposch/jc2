# D43 pristine-source high-Hensel hostile review — Fable 5

UTC: 2026-08-28T19:31Z  
Mode: independent read-only review through authenticated `claude` CLI  
Verdict returned by reviewer: **PASS, conditional on an external AWS harness
enforcing the preregistered caps**

## Confirmed mathematical core

Fable independently verified all five hashes in the packet manifest and all
eight preregistered input hashes.  Its bounded replay reproduced the sealed
`p^2` state payload digest beginning `ce3a145e` and the committed essential-182
correction digest beginning `e3a15fa6`.

- The source census is exact: 180 nominal tails, eight fixed coordinates and
  two x-side coordinates give 190; the eight dense-family `r=39,41` labels are
  structurally absent, leaving `172+8+2=182` essential coordinates.
- The eight removed columns are both literally zero in the recovered
  `184 x 190` Jacobian and unreachable by the parity/cutoff support argument.
- The alpha/beta value term is exact, not merely tangent-level.  Writing the
  full Euler expression after multiplying by
  `U_f=1+alpha*t^42`, `U_g=1+beta*t^42`, the apparent `(alpha+beta) B_y`
  contribution cancels at slot zero.  The surviving term is
  `42*S_M*G_M*(3*alpha-2*beta)*[eta^a](p^4 p')`; quadratic x-side terms begin
  at slot 84.  Basis and perturbed-y comparisons with the independent
  `eplus43` operator passed.
- The radical lift uses literal `Phi_42`, lifts `r3` before the dependent
  `A1,A2`, and rechecks the five defining equations and unit denominators.
- The frozen Jacobian modulo `p` is valid along the residue branch.  The
  stored row transform gives a genuine 55-dimensional left cokernel, and the
  pivot-only solution correctly sets all 53 free digits to zero.
- A finite `p^16` survival would be strong order-by-order evidence for this
  one branch, while still implying no smoothness, `Z_p`, characteristic-zero,
  Keller-map, or JC2 conclusion.

## Defects reported by Fable

1. A first-digit obstruction seals exponent 1, but the resume validator only
   accepts exponent at least 2; this is fail-closed but operationally awkward.
2. The obstructed-resume guard contains a no-op `pass`.
3. The 1200-second, 2-GiB, no-swap, and AWS-identity gates are not enforced by
   the runner; Fable's PASS is explicitly conditional on a route harness
   enforcing them.
4. The design note should call `S_M*p^2` and `G_M*p^3` slot-zero eta
   polynomials, not merely slot-zero constants.

## Coordinator adjudication

This different-model review confirms the mathematical evaluator and Newton
core, but it is **not launch authority**.  The independent Sol hostile review
`xmodel/d43-source-high-hensel-hostile-review-gpt56-20260828.md` found an
additional semantic-chain defect: a kernel-shifted valid `p^2` point can be
accepted with stale deterministic history.  It also treats the missing AWS
harness as launch-blocking under campaign policy.  Therefore the operative
status is `REPAIR_LAUNCH_BLOCKED` until schema-v2 chain replay, a dedicated
AWS harness, a synchronized claim firewall, resealing, and hostile rereview.
