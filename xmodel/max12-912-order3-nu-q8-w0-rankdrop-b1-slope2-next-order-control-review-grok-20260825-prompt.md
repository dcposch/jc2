# Hostile review request: b=1 slope-two next-order control

Act as a hostile algebraic-geometry/source-fidelity referee.  Work read-only.
Do not edit the repository.  Do not run Bash, local CAS, solver, network, or
long Python.  You may read/hash files and reason by hand; the two frozen AWS
Singular endpoints are the accepted computations.

Read in full:

- `xmodel/max12-912-order3-nu-q8-w0-rankdrop-b1-slope2-next-order-control-20260825.md`
- every file in
  `cases/max12_912_order3_nu_q8_w0_rankdrop_b1_slope2_next_order_aws_20260825/`
  except no need to repeat large identical source text after byte comparison;
- pinned compiler
  `cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py`;
- raw hostile audit plus both immutable errata:
  `xmodel/max12-912-order3-nu-q8-w0-rankdrop-ramified-arc-audit-claude-20260825.md`,
  `...-provenance-erratum-20260825.md`, and
  `...-scope-erratum-20260825.md`.

Charge and decide explicitly:

1. Verify the six source rows and the substitution/convention
   `c=c+C1*t`, `d4=1+B1*t`, `d2=2+(B1+Q1)t`, `x5=t`,
   `x3=5t/3+X2*t^2`, `x1=U2*t^2`,
   `w=-4t^2/9+W3*t^3`.  Check coefficient extraction uses the correct next
   orders (odd rows at `t^2`, even rows at `t^3`) and that all displayed
   leading coefficients vanish.
2. Under the strict normalization `x5=t` and ordinary power series, decide
   whether `C1,B1,Q1,U2,X2,W3` really include every first jet allowed by the
   chosen ansatz, or identify a missing jet.  Distinguish this from earlier
   base-coordinate drift possible in a ramified/Puiseux arc.
3. Audit the six printed next coefficients, the exact unit basis, and the
   elimination to `Q[c]`.  Explain exactly what `GNext=(1)` proves at finite
   jet depth.
4. Audit two-engine independence: Box02 `std/dp` and Box03 `slimgb/block`,
   same compiler but separate hosts/orders/algorithms.  Check rc, diagnostics,
   source regeneration, hashes, replay, and the v1 permission-failure negative
   controls.
5. Enforce the firewall.  Refuse every inference to arbitrary weighted or
   ramified/Puiseux arcs, mixed orders, full rank-drop/Hsrc, infinity,
   Taylor/terminal realization, trajectories, `(9,12)`, maximum twelve, or
   JC2.  Reconcile this finite-jet unit with the raw audit's surviving leading
   cone and `NOT_CONFIRMED` verdict.

Name the smallest exact next weighted/ramified discriminator.  End with one of
`CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `NOT_CONFIRMED`, and list any repairs.
