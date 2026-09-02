# Research lane: A2-DEV-PROJECTION — reissue the corrected A2 system and pin the wall parameter c

Two P0s on the A2/CELL-32 record are now gated (charged gate report): the
SPEC's displayed EQ2_even omits -2 q E1 ([A^2]Even = SPEC_E2 - 2qE1), and
C32's THEOREM T2 derivative display has a G' sign error (corrected
bracket eta G^2 + 2Z eta' G^2 - 2Z eta G G'). HORN-A2's E1-wall is
retracted, RAY-2 refuted, T4 open, and every A2 cell certificate void.
Surviving: C32 T1, T3 (repaired), RAY-DEP, RAY-EDGE (e >= 2, corrected
rho), the ray as the universal corrected top kernel, THEOREM DEV-FREE and
A2-DEV-BOUND in their scopes (charged A2-U-BOUND report). Naming rule for
everything you write: the EQUATION is EQ2_even; E2 is the coefficient
polynomial b Z eta^2.

Tasks, in order, all on the fully corrected, WALL-FREE system:
(1) REISSUE. Rebuild all seven residual equations (O0, O1, O2, E0,
    EQ1_even, EQ2_even, EQ3_even) from SPEC's own Even/Odd definitions with
    P = p + A C1 + A^2 C2, Q = q + A D1 + A^2 D2, R0 = r + A E1 + A^2 E2,
    S0 = s; re-derive T1 and the corrected T2 identity (Z^2 Xi form) and
    the p'-free O1s of the charged report; publish the corrected system
    as a canonical display block with every symbol defined, and a
    machine-readable generator file (python, sympy) that emits it, with
    an exact-diff control against Even/Odd. This block replaces the
    SPEC's section 1 for all future consumers.
(2) DEV-PROJECTION / WALL-PIN (Sol's round-0741Z Card 1, charged). In the
    deviation variables X = 4b eta^2 r - s^2, Y = 4b^2 eta q - 3a s^2 the
    corrected EQ1, EQ2, EQ3 are s-free (DEV-FREE); on branch (A)
    deg X, deg Y <= 4e - 1 (Ch. III; Ch. II with c != -2e). For e = 1, 2
    (and 3 if it fits the budget) form the coefficient ideal I_e in the
    declared ring Q[eta_0..eta_{e-1}, G_0..G_{2e-1}, X_0..X_{4e-1},
    Y_0..Y_{4e-1}, kappa, tt, c] with a = b = eta_e = 1 (S1/S2), c5 = 0,
    G_{2e} = c, saturation kappa*c*(c+2e)*tt - 1 = 0, block elimination
    order with c last, and compute J_e = I_e ∩ Q[c]. Read out: 1 ∈ I_e
    (branch empty); J_e nonconstant (finitely many c: list them, then
    with the charged finite-U dichotomy give the finite box per e);
    J_e = 0 (c unpinned: hand the locus to the s-dependent stage EQ4/O1s).
    Use the DET-EO identity of the same card as a checksum. Treat c = 0,
    c = -2e, c = -(2e+1), Wall A 3c + 6e + 2 = 0, the k = 2e stratum
    (OPEN[A2-K2E]) and Chamber I as separate declared branches; never
    impose the retracted wall.
(3) T4 REPAIR ATTEMPT. C32 T4 (deg eta = 0 impossible on the live section)
    is OPEN because its proof used the old EQ2_even. Re-run the e = 0
    section on the corrected system (it is a finite computation) and
    either restore T4 with a corrected proof or exhibit the surviving
    locus.
(4) STATE LADDER. Any nonempty locus is a SUBSYSTEM_POINT at most; label
    by the two-field typing (artifact / attainment) of the charged Sol
    submission; do not call anything a curve, a map, or a (B3) object.
    Reconstruction of (r, q, p) from (X, Y, s) requires the three exact
    divisibilities eta^2 | (s^2 + X), eta | (3a s^2 + Y),
    s | (q r' - kappa/2) — check them pointwise if a locus appears.
Engines: qqideal 0.2.0 + msolveio 0.2.1 (msolve 0.10.1) as the default,
sympy as the second engine for anything called EMPTY; explicit
Rabinowitsch variables, no sat() wrappers; positive control = a planted
point on the corrected system. Desk-scale (< 15 min, < 4 GB per job);
anything larger is a job spec for the coordinator (box01 is free).
Do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/a2-dev-projection-sol56-20260902.md
Seal-at-completion; bounded writes; target 20-30KB.
charged_input=xmodel/a2-ubound-opus5-20260902.md
charged_input=xmodel/a2-e2-p0-gate-gpt55-20260902.md
charged_input=xmodel/cell-32-spec-sol56-20260901.md
charged_input=xmodel/cell-32-termination-opus5-20260901.md
charged_input=xmodel/ideation-20260902T0741Z-sol56.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
e8eb9d77d82b89405b052b703fab2f74de57b9775d3a8376be96a35c95a48345  {{LANE_INPUTS}}/a2-ubound-opus5-20260902.md
68c4802f4c4909389eea13bae09c75f744a5c4cbde0a9db76b7237c3b03f20b5  {{LANE_INPUTS}}/a2-e2-p0-gate-gpt55-20260902.md
86caf003268ddc40143daa68d439079dbd82d1dac41e1da93f33a661d52f96ac  {{LANE_INPUTS}}/cell-32-spec-sol56-20260901.md
d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b  {{LANE_INPUTS}}/cell-32-termination-opus5-20260901.md
717134c733adc17b3b70409b018858fb1311c37608a24f0eebe65ae79aec8b11  {{LANE_INPUTS}}/ideation-20260902T0741Z-sol56.md
```
