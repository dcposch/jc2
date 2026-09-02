# Research lane: A2-CELLS-CODEGEN — the A2-E1WALL-CELLS job as qqideal Python

Transcribe the charged ray-kill report's §4.1 job spec
(A2-E1WALL-CELLS) into runnable Python against qqideal 0.1.0 +
msolveio 0.1.0 (API as used in box/qq_oracle_jobs.py — read it
in place as the style/API reference; msolve 0.10.1 pinned via
binary= parameter).
Deliverables:
(1) box/a2_cells_jobs.py — build_cell(e, U) constructing the
    EXACT generator system: all Z-coefficients of EQ1-EQ4
    (transcribe from the charged CELL-32 report's displayed
    equations — (1.1), the Sec 6 E2eq|_{G=0}+Delta_2, T2's
    eta Z^2 Xi - (3a/b)(Z eta^2 G^2)', (2.2)), T1
    (eta*Phi - s*G), E0 (2(q r' - p' s) - kappa), the wall
    G_g = -(1+2e), normalizations a=b=1, A_e=1, and the
    saturation S_sigma*Q_m*R_n*kappa*tt - 1. Honor the DO-NOTs
    (no S_sigma normalisation; never omit saturation). The
    OPTIONAL accelerator generators behind a flag, off by
    default for the decisive run.
(2) box/a2_cells_run.py — runner: item-0 promotion gate first
    ((1,3) must return EMPTY over Q — this is the SECOND ENGINE
    for the ray-kill lane's sympy decision; a NONEMPTY or
    non-answer there is a P0, print loudly, exit 2), then items
    1-4 (e=1 U=5..13; e=2 U=8..12; e=3 U=11,13; e=4 U=14), each:
    mod-p msolve screen first (EVIDENCE only, typed), then the
    char-0 decisive run; per-cell timeout parameter; verdict
    table with certainty labels and input sha256s.
(3) Derivation section in the report: coefficient-level
    correspondence between your generators and the CELL-32
    displays, line-cited. ANY ambiguity in the displays: STOP,
    type OPEN, encode variants.
(4) Self-checks runnable without msolve (Fraction/sympy):
    (i) generator counts per cell match the ray-kill §4 table
    (22 unknowns/37 equations at (1,3) etc.); (ii) a
    deliberately broken wall value (G_g = +(1+2e)) changes the
    system (nonzero diff); (iii) the saturation variable
    appears in exactly one generator.
PACE report sections as you go. Report:
xmodel/a2-cells-codegen-sol56-20260902.md
Seal-at-completion; target 15-25KB.
charged_input=xmodel/ray-kill-opus5-20260902.md
charged_input=xmodel/cell-32-termination-opus5-20260901.md
charged_input=xmodel/ray-kill-review-gpt55-20260902.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
3d08b8996227e292d76e0ba3901cfad16099f347f97129d27b6bf5b3bc253f0a  {{LANE_INPUTS}}/ray-kill-opus5-20260902.md
d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b  {{LANE_INPUTS}}/cell-32-termination-opus5-20260901.md
df5612152d60496bb81311ee9183d3c580759a2549d6ea8945a487d284976fcf  {{LANE_INPUTS}}/ray-kill-review-gpt55-20260902.md
```
