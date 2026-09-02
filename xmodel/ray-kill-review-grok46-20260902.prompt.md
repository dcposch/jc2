# Review lane: RAY-KILL-REVIEW — gate RAY-1/RAY-DEP/RAY-EDGE/RAY-2

The charged ray-kill report proves, one order past the reviewed
THEOREM HORN-A2: RAY-1 (the 4x5 next-order linear system, rho
carried by EQ3, rho != 0 exactly on U = 3e); RAY-DEP (the exact
dependency n(N1)+(n-2)(N3)-(N4) = -(n-2)rho, rank <= 3);
RAY-EDGE (the boundary slice U = 3e is EMPTY — proved e >= 2 via
the rank obstruction with rho = -P(-(2e+1)) b^2 eta_e^4/...;
the degenerate cell n=2,(e,U)=(1,3) via an exact Groebner
decision); RAY-2 (deg E1 <= 2e-2 on survivors); the exact
2-dimensional residual per cell (second-order pins displayed);
per-cell finiteness/overdetermination; NEW OPEN[A2-U-BOUND]
(U unbounded per e); and a LEDGER CORRECTION (a ray kill closes
OPEN[A2-CELL-32] + one OBSTRUCTION[A-DEGREE-TWO] layer, NOT
(B3) windows — the charge premise was wrong per HF §5).
Hostile review, sympy available:
(1) Replay RAY-DEP symbolically (the identity must hold
    coefficient-by-coefficient; state your residuals).
(2) RAY-EDGE e>=2: verify rho != 0 — in particular that
    P(-(2e+1)) != 0 for all e >= 2 (P is HF's chamber-II
    polynomial; check its roots exactly).
(3) The (1,3) Groebner decision: RERUN it yourself (state
    engine + basis); the lane ran it in-sandbox — verify the
    system transcription against the closed form of its §3.1.
(4) RAY-2 and the second-order pins: replay; check the pins'
    derivation does not divide by anything unproven-nonzero
    (eta_e, r_n, s_s nonzero — sourced where?).
(5) The ledger correction: adjudicate against HF §5 — was the
    charge wrong as claimed? State what a full ray kill would
    and would not close.
(6) The five control layers of its §2 (scaling residuals etc.):
    spot-verify two.
Verdict per claim: CONFIRMED / REFUTED / GAP.
Report: xmodel/ray-kill-review-grok46-20260902.md
Seal-at-completion; target 15-25KB.
charged_input=xmodel/ray-kill-opus5-20260902.md
charged_input=xmodel/horn-flagship-opus5-20260902.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
3d08b8996227e292d76e0ba3901cfad16099f347f97129d27b6bf5b3bc253f0a  {{LANE_INPUTS}}/ray-kill-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
```
