# Hostile review request: generic-`c`, frozen-`b=1` selected-localizer unit

Act as an independent hostile algebraic-geometry/source-fidelity referee.
Work read-only and return the report only on stdout.  Do not edit repository
files.  Do not run Bash, local CAS, a solver, long Python, or the network.
The accepted computations ran on AWS.  Read in full:

- `xmodel/max12-912-order3-nu-q8-w0-rankdrop-b1-generic-c-localizer-unit-20260825.md`;
- `cases/max12_912_order3_nu_q8_w0_rankdrop_b1_loaded_saturation_aws_20260825/ELIM_PREREGISTRATION.md`;
- the frozen elimination generator, runner, both `aws_r6d_elim_*` endpoints,
  replay, `ELIM_PASS.manifest.sha256`, and `ELIM_PASS.freeze.sha256` in that
  case;
- the pinned quotient compiler only as needed to check source identity; and
- `xmodel/max12-912-order3-nu-q8-w0-rankdrop-ramified-arc-audit-claude-20260825.md`
  together with
  `xmodel/max12-912-order3-nu-q8-w0-rankdrop-ramified-arc-audit-provenance-erratum-20260825.md`.

Attack every point below explicitly:

1. The imposed source is exactly `(e1,e3,e5,e7,e2,e4)`; the substitution is
   exactly `d4=1,d2=2+u`; no terminal, Taylor, or extra source row is hidden.
2. The coefficient ring is exactly `Q(c)`, the localizer equation is
   `inv*w*x5*(x3-2*x5)-1`, and block elimination of `inv` is semantically the
   contraction of this selected open.
3. Decide whether independently reconstructed `std` and `slimgb` bases
   `GC=(1)` really license `J=(1)` over `Q(c)`, and identify any missing
   cofactor/membership trust debt.  Audit hashes, regeneration, diagnostics,
   timings, and the replay.
4. Enforce both losses caused by the slice: `Q(c)` erases a finite exceptional
   denominator locus in `c`, and freezing `d4=1` does not cover an arc landing
   at `d4=1` with nonconstant `d4` drift.  The report must not be read as an
   arbitrary-ramification, whole-rank-drop, or full-Hsrc theorem.
5. Reconcile the result with the hostile ramified audit: the surviving b=1
   slope-two cone is not contradicted unless an actual continuation remains
   in the frozen `d4=1` slice at generic `c`; mixed-order and exceptional
   strata remain charged.
6. Check the firewall: no conclusion about exceptional finite `c`, other
   rank-drop values, coefficient infinity, Taylor/terminal realization,
   trajectories, general `(9,12)`, maximum twelve, or JC2.

Give a precise verdict `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REFUTED`.
Name the smallest exact missing certificate and the exact next exceptional
locus.  End with the verdict word alone.
