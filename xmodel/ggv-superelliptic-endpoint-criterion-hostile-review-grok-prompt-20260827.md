# Hostile different-model review — GGV superelliptic endpoint criterion

You are Grok acting as an independent hostile mathematical referee.  Work in
`/Users/dc/code/math/jc2`.  Read:

- `xmodel/ideation-20260827T1349Z-opus5.md`, especially sections 0.2, 3,
  4, 5, and Card A;
- the frozen R1/R2/R3 producer and hostile-review artifacts named there;
- `xmodel/ggv-8_28-M-cokernel-seven-vector-hostile-audit-sol2-20260827.md`
  only to distinguish the polynomial-cokernel result from this rational ODE.

Do not read or edit `jc2-lean`.  Do not edit canonical files, cases, or any
ideation submission.  Desk-scale exact algebra only; no heavy local CAS and no
AWS.  Write exactly one report:

`xmodel/ggv-superelliptic-endpoint-criterion-hostile-review-grok-20260827.md`

Independently verify or refute, with the smallest failing example or repair:

1. For nonzero `H` in characteristic zero, rational solutions of
   `2 H g' + H' g = 2 H`.  With `H=A^2 B`, `B` squarefree, prove or refute
   the equivalence with a polynomial `v` satisfying
   `A=B v' + (3/2)B'v`.  Check finite-pole and infinity valuations,
   cancellation, uniqueness/homogeneous solutions, and correct denominator
   wording.
2. The exact integrating-factor and de Rham reformulation on `w^2=H`, the
   computation `[w dX]=-(4/5)[dX/w]` for `H=X^8-1`, and nonexactness.
3. The degree bound and all displayed examples (`X^8-1`, `X^16-1`, a square,
   a single-root power, and `X^2(X^2-1)`).  Rebuild at least one independent
   exact checker or explicit substitution; producer verdict strings are not
   evidence.
4. The general `(alpha,beta,N)` endpoint formula and its superelliptic-cover
   interpretation.  State necessary field/root choices precisely.
5. The firewall: decide exactly what is an endpoint theorem versus what still
   needs general-`H` rational-mode completeness, raw `2S/3S` provenance,
   polynomial cleanup, GGV landing, `G2-PSC`, `G2-BD`, or a cofinal theorem.
   In particular, determine whether the proposed `deg A < deg B-1`
   exclusion is presently licensed for any object beyond the artificial R3
   endpoint.
6. Novelty/custody: account for Opus5's disclosed one-line contamination.
   Treat the integrating factor as convergent, not solely novel; decide
   whether the closed-form rational criterion, certified degree bound, and
   Pell/de-Rham distinction are nonduplicate relative to pre-round history.

Return separate `CONFIRMED`, `REFUTED`, or `GAP/REPAIR` verdicts for the
rational criterion, denominator statement, de Rham computation, examples,
general formula, mode-completeness bridge, claimed degree-uniform GGV use,
history/novelty, and final scope.  A correct endpoint solver is not a GGV
family exclusion without the bridge.
