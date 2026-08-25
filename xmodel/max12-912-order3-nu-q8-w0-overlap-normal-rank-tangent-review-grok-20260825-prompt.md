# Hostile review request: raw-overlap normal-rank/Fitting and ordinary tangent package

Act as an independent hostile algebraic-geometry/source-fidelity referee.
Work read-only.  Do **not** run Bash, local CAS, solver, long Python, or any
substantive computation; the accepted computations ran on AWS.  You may read
files and check small identities by hand.  Write exactly

`xmodel/max12-912-order3-nu-q8-w0-overlap-normal-rank-tangent-review-grok-20260825.md`

and no other file.  Read in full:

- `xmodel/max12-912-order3-nu-q8-w0-overlap-normal-rank-fitting-20260825.md`
- `xmodel/max12-912-order3-nu-q8-w0-overlap-horizontal-tangent-20260825.md`
- both corresponding case directories, including preregistrations,
  generators, accepted AWS endpoints, replays, manifests, and freezes
- the pinned quotient compiler/source only as needed to audit source identity.

Attack these points explicitly:

1. The imposed source is exactly `(e1,e3,e5,e7,e2,e4)` and the raw overlap is
   `w=x1=x3=x5=0`, with no hidden load or terminal equation.
2. The matrices `M` and `N=[M|F_w]`, all minor ideals, and the formulas
   `K3=I4(N):I3(M)^infinity`,
   `K2=(I3(M)+I3(N)):I2(M)^infinity`, etc. really represent the ordinary
   `delta w=1` incidence on exact-rank strata.  Challenge closure artifacts
   caused by saturation and say exactly what the computed ideals license.
3. Check the rank-drop polynomial equals `(d2-d4-1)^2`, including the doubled
   scheme structure, and that `K3=(d2,d4)`, `K2=K1=K0=(1)` supports only the
   report's strict first-order conclusion.
4. Independently hand-check the displayed `L2,L4` equations, their two-point
   ideal `(d2-2*d4,d4(d4-2))`, the branch-zero solution, and the branch `(4,2)`
   residual `729*L7=-432`; flag any mismatch of tangent coordinates or row
   ordering.
5. Audit both engine/order endpoints, input/output hashes, replay logic,
   diagnostic firewall, and retained V1/V2 negative controls.  Independence
   is engine/order/host, not independently authored mathematics.
6. Enforce the firewall: these are ordinary first-order/Fitting facts only.
   They do not exclude ramified/weighted arcs, the rank-drop line, global
   horizontal closure, infinity, Taylor/terminal realization, trajectories,
   `(9,12)` generally, maximum twelve, or JC2.

Give a precise verdict `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REFUTED`,
list the smallest exact repair for every defect, and end with the verdict
word alone on its own line.

