# Hostile review prompt: D1 slope-uniform strict-boundary saturation

You are a hostile mathematical/source reviewer.  Audit the frozen
slope-uniform D1 source/compiler and the exact logical meaning of its unit
ideal test.  Do not infer anything from the still-running AWS jobs.  Do not
run local Bash, Python, Singular, Sage, msolve, or another CAS/solver; if an
independent computation is needed, specify a fail-closed AWS replay plan.

Write exactly one new report, refusing to overwrite an existing file:

```text
xmodel/max12-912-order3-d1-slope-uniform-saturation-review-grok-20260825.md
```

## Exact charged bytes

```text
2824cca5d49a3992f65ea34a1c55884ea1a0e132eaf4a919a9f5153879181f6f  cases/max12_912_order3_d1_weighted_infinity_20260825/FREEZE_SLOPE_UNIFORM.sha256
39f43b1a078a1e07c18a3bd369a7d8f1b63a7d35a3e5015016d798b7743fd885  cases/max12_912_order3_d1_weighted_infinity_20260825/SOURCE_CLOSURE_SLOPE_UNIFORM.sha256
1acb149bc997d4dae1e29b97b0683b99ca38e9d8dd7543b0da03cf64cc152cb7  cases/max12_912_order3_d1_weighted_infinity_20260825/compile_slope_uniform.py
4aa066bad83407eae9383597aba1fc7e3a7e828be28fd77610d4076cef02b1b7  cases/max12_912_order3_d1_weighted_infinity_20260825/PREREGISTRATION_SLOPE_UNIFORM.md
d77bd3ae91113e09b90109842a93e18b84fd129e47b951d45b1d0e953473d809  cases/max12_912_order3_d1_weighted_infinity_20260825/run_slope_uniform_aws.sh
c25092a17cc8db8d70019018e97120776ca374c8c00d20f981bc7cde7436b9b5  cases/max12_912_order3_d1_weighted_infinity_20260825/SLOPE_UNIFORM_SMOKE_V2_CUSTODY.md
b9df8e900f4f07017a8d04bb30888356a4dbf0fc68ec0ad966a0bd7985f2080c  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/compile_gate_v2.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
de7dd223d472508e057db72a5ec466c6362b762b4ba9a50f4ff823f585e774c7  xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-20260825.md
a274c8d8e0883ce7606f31f69803a293afb15ad48fe9d401191cac1cdbe1daee  xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-review-grok-20260825.md
bdb369f187284df82935488288d3752c4781e527eec1c38da80b757a26f50c38  xmodel/max12-912-order3-d1-isotrivial-strict-rees-saturation-20260825.md
```

The original exceptional-support producer `de7dd223...` is a fixed review
target and was not changed by the later nonmutating compiler successors.

## Required hostile charges

1. **Raw versus shifted rows.**  Verify that the consumed compiler has
   `R_l=D_l-delta_l`, with `delta_3=mu`, `delta_6=nu`, `delta_8=1`, and that
   `raw_tail_rows` undoes exactly these three shifts before the Rees
   homogenization.  Look specifically for double-counted or unscaled loads.
2. **Every monomial weight.**  Check that the runtime assertion
   `sum_i(9-i)e_i+6e_k=12+l` is the needed and sufficient source identity,
   with powers of `s` weight zero.  Verify target exponents and indices.
3. **Isotrivial twist.**  Independently audit
   `a_i=t^(i mod 3)A_i`,
   `r_l=t^(2l mod 3)D_l`, the ordinary target
   `(0,0,mu,0,0,nu,0,t)`, and the exact etale/unit change from
   `q=t^3-1` to `tau=t-1`, including `gamma_8=1+tau`.  Check that the
   runtime ordinary-tail reconstruction really compares all eight rows.
4. **Strict-slope bridge.**  Prove or refute that
   `Lambda=q^3*rho`, with `q,rho` nonzero generically and both zero at the
   centre, represents exactly slopes `ord Lambda>3 ord q`.  For a rational
   slope `m/n>3`, check `q=eps^n`, `rho=eps^(m-3n)`, the coefficient
   normalization, and existence of a nonzero projective `B` centre.
5. **Exact ideals and saturation order.**  Audit

   ```text
   I=(Psi_1,...,Psi_8),
   K=I:(q*rho)^infinity,
   H=((K+(q,rho)):m_B^infinity).
   ```

   Verify that adding the boundary only after interior saturation is
   essential and implemented.  Check saturation by the full irrelevant
   ideal versus the invalid coordinate-product shortcut.  Audit the actual
   product-vs-sequential (`q`, then `rho`) two-containment control.
6. **Constant field and load strata.**  Confirm the emitted ring is a
   polynomial ring over `Q` in `k,mu,nu`, not the rational-function field
   `Q(k,mu,nu)`, so no load stratum is silently inverted.
7. **Common-cubic coordinates and coverage.**  Check that
   `B7=3p`, `B6=3c`, `B_i=C_i(p,c)+X_i` for `i<=5` is a polynomial
   automorphism over `Q`, and that the pulled-back irrelevant ideal is
   `(p,c,X0,...,X5)`.  Given the independently reviewed common-cubic
   boundary radical, verify that `B7!=0` and `B6!=0` cover the projective
   radical if the global job is inconclusive.  Explicitly retain the
   symbolic invariant `c^2/p^3` and the non-axis discriminant locus
   `Delta=-4p^3-27c^2=0`; no pivot may divide `Delta` without a separate
   `Delta=0` stratum.
8. **Controls and custody.**  Audit the synthetic strict-arc, pure-boundary,
   rho-unit slope-three, and projective-axis/product negative controls.  The
   clean smoke used a synthetic source ideal (`CONTROL_ONLY=1`); confirm it
   is syntax/source/control evidence only.  Confirm the prior `sat` list
   out-of-range run is quarantined and the successor rejects nonempty
   Singular stderr.
9. **Exact theorem firewall.**  Prove or refute:
   - `H=(1)` excludes every strict rational/formal/Puiseux coefficient-
     infinity arc by cancellation in the formal-series domain (or curve
     selection after finite extension).
   - `H!=1` is only a finite-type boundary survivor/Puiseux-accessibility
     condition.  It does not give a rational constant-field section,
     monodromy, Taylor polynomiality, a D1 solution, or a JC2 conclusion.
   - Neither a running/timeout endpoint nor agreement of two coordinate
     presentations can replace source review and exact final markers.

## Required report form

Return one of `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REFUTED`.  List
every mathematical, source, deployment, and scope defect separately.  State
the strongest exact implication licensed if the eventual source run reports
`H=(1)`, and separately if it reports `H!=1`.  Include the reviewed target
hashes and the output report SHA-256.
