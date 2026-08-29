# V43 compiler custody addendum: reviewed c7ed7309 to launched 0de6a2b2

Date: 2026-08-27  
Scope: additive custody record only; this does not amend the frozen question or report a V43 result.

## Immutable identities

- Fable's correction review consumed and names
  `compile_total_dvr_w30_v43.py` at SHA-256
  `c7ed730905592b571ef6746ad369297916810c671e4c6f2e6f1af0995caeade0`.
- The later AWS preflight, total-dehom sources, and rho-zero LinBox source
  pin a post-review producer at SHA-256
  `0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00`.
- Therefore `0de6a2b2...` is **not** described as reviewed by the Fable
  report.  The Fable claim about `c7ed7309...` remains untouched.

The exact post-review mutation was recovered from the append-only Codex
turn transcript and independently checked by reversing it in memory from
`0de6a2b2...`: the reconstructed bytes hash to `c7ed7309...` exactly.

## Exact unified diff

```diff
--- compile_total_dvr_w30_v43.py.reviewed-c7ed7309
+++ compile_total_dvr_w30_v43.py.launched-0de6a2b2
@@
     core_equations = [index for index, live in enumerate(active) if live]
     core_variables = sorted({variable for equation_index in core_equations
                              for variable in equations[equation_index]})
+    forced_core_equations = [index for index in core_equations
+                             if right_hand_sides[index]]
@@
         "core_nnz": sum(len(equations[index]) for index in core_equations),
+        "forced_core_equations": len(forced_core_equations),
     }
-    if core_equations:
+    if forced_core_equations:
         return {"outcome": "core", "census": census,
                 "core_equation_indices": core_equations,
                 "core_variable_indices": core_variables}
 
+    # A homogeneous cyclic core is solved by zero.  Only the component of
+    # the affine target condition needs back-substitution through the peel.
     values = {target_index: Fraction(1)}
```

There are no other byte differences.

## Meaning and soundness

The reviewed version failed closed whenever leaf peeling left any cyclic
core.  The launched version fails closed only if a surviving core equation
has nonzero affine right-hand side.  If every surviving core right-hand
side is zero, assigning all core variables zero is an exact solution of the
core; reverse substitution through the peeled equations then supplies the
same rational dual functional, which is still replayed against every
rho-zero product by `v37.replay_certificate`.  Thus the change enlarges the
set of instances on which the leaf solver can return a certificate, but it
does not weaken the exact replay gate.

For the actual weight-30 instance the new telemetry is
`core_equations=23477`, `core_variables=47089`, and
`forced_core_equations=1`.  Hence both versions fail closed on this input;
the post-review semantic branch is not exercised.  The separate LinBox
route is being used for the forced affine core.

The total-dehom and LinBox producers import `reconstruct_rows`,
`build_products`, and specialization helpers from `0de6a2b2...`; they do
not call `leaf_peel_dual`.  Consequently this delta does not alter their
literal-row reconstruction or their algebraic questions.  Their remote
source trees carry immutable `0de6a2b2...` bytes and source-manifest hashes.

## Firewall

This addendum establishes custody and explains a post-review semantic
change.  It does not assert `a1^6` membership or nonmembership, a total-rho
certificate, chart closure, Gate T, or JC2.
