You are the hostile independent reviewer of a proposed slope-uniform tropical
obstruction in the plane Jacobian-conjecture campaign.  Work from exact files
and rederive the argument; do not inherit the producer verdict.  A prior
Claude lane failed before reading the target because its API quota was
exhausted; it produced no mathematical verdict.

Target:
`xmodel/max12-912-order3-d1-double-root-control2-slope-uniform-obstruction-20260826.md`

Required target SHA-256:
`b6349549a115a44ac8534d7801a15fa7e3f8c7a8211cce69ce723cd019301a49`

Required evidence freezes:

```text
04cd09886ed78e1af48a6387ee2c67996856d2b6f59791963450e7e4380e32a3
  cases/max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826/WITNESS_FREEZE.sha256
616628e959c6b458948bcf72102c46118e5e6c4c95165f0133e5324579a120ee
  cases/max12_912_order3_d1_double_root_control2_la20_witness_replay_v1_20260826/FREEZE.sha256
e4cc300ad4317a7a3807a67cf3d2e671ff9eefaf11a5cecd98b0b5e1f9f1abf5
  cases/max12_912_order3_d1_double_root_control2_la20_witness_replay_v1_20260826/RESULT.md
1fdddc051d8a7cdad2b6e250e4d9332897568cb9da436bfcb3c954dd2f35b297
  cases/max12_912_order3_d1_double_root_control2_la20_witness_replay_v1_20260826/aws_r6d/singular.stdout
```

Independently attack:

1. Verify from the literal replay and charged generators that the displayed
   `W` is in the exact unhomogenized ideal `J`, with the coefficients and
   `Lambda^20` exponent stated.  Distinguish certificate replay from a new
   independent derivation.
2. Recompute every term weight under
   `L=3T+H`, `w(q_i)=beta L`, `w(r_i)=15L/2`, and check that the unique
   least-weight term is `Lambda^20` exactly when the claimed strict
   inequalities hold.  Audit least-versus-greatest convention and rational
   rescaling.
3. Check `W in J => Lambda^20 in in_w(J)` and the torus-localization
   consequence.  State the exact valued-arc/leading-coefficient lemma needed
   to turn this into exclusion of a control-2 arc.
4. Audit whether setting Rees parameter `s=1` permits reweighting at every
   rational slope in the fixed-source ideal, or whether saturation,
   homogenization, a denominator, or discovery-order artifact is missing.
5. Trace the control-2 mapping: why `alpha=15/2`, `5<beta<6`, positivity of
   `T,H`, and `Lambda=tau^3 rho` cover the entire charged interval.  Look for
   a coefficient/layer allowed by the prior correction firewall but absent
   from this fixed support.
6. Check the equality face `beta=5`, endpoints, `beta>6`, moving-axis,
   nonzero-q2, load, support, and whole-D1 firewalls.  Reject any inference
   broader than the exact fixed cubic/load/support theorem.

The Mac is coordination-only.  Do not run Singular, Lean, Sage, Python
algebra, or another computational replay locally.  This is a text/source
audit; request AWS if a substantive computation is needed.

Write the review only to
`xmodel/max12-912-order3-d1-control2-slope-uniform-review-grok-20260826.md`.
Include recomputed hashes, the exact strongest licensed theorem, the smallest
repair/counterexample if any, and end with exactly one of `CONFIRMED`,
`REPAIR`, or `REJECTED`.  Do not edit target, evidence, or top-level files.
