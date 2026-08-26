# Hostile source review — strict D1 double-root toric blow-up

Act as a hostile algebraic geometer, valuation theorist, and exact-CAS source
auditor.  This review is independent of the live solver result.  Verify this
frozen package and every entry in its manifests before relying on it:

```text
015ed8156197ba4cfac55cbc6d33379d7545739bfe657856febd8e17c8d3913c  cases/max12_912_order3_d1_double_root_toric_blowup_20260825/FREEZE.sha256
7e6cce9beaed80cc4f75d33fddabc9b3a12d619f7831e110d58e4c3241d0a061  cases/max12_912_order3_d1_double_root_toric_blowup_20260825/SOURCE_CLOSURE.sha256
3b200a84f0d7ff3e3b30612e0e10d6792cbf1ebeda0da721ce4eef0103951228  cases/max12_912_order3_d1_double_root_toric_blowup_20260825/CUSTODY_PRELAUNCH.sha256
```

Read `PREREGISTRATION.md`, the charged ordinary reconstruction, the complete
compiler, both hosts' compiler stdout, and all four emitted Singular scripts.
Do not infer a solver verdict: A and B were still running when this prompt was
frozen.

Charge each of the following independently.

1. Re-derive the exact coefficient images for
   `f=K^3+K*x*Qhat+x^2*Rhat`, `K=z^3+pz+c`, including every coefficient
   `a0,...,a7`, and verify `kbar=x*y*k`.  Check that the eight ordinary tails
   have target equations `Lambda^(12+l) gamma_l` with loads precisely at
   15/18 and row 8 exactly `Lambda^20*(1+tau)`, with correct signs.
2. Audit the compiler's hash anchoring, ordinary-weight check, exact sparse
   substitution, common-cubic zero check, `kbar` scaling check, target check,
   and emitted row digests.  Look for Python indexing, multiplication,
   specialization, string-parenthesization, rational-coefficient, or Singular
   parsing errors.  Verify that the factored and expanded rows are identical
   polynomials, not merely similar metadata.
3. Re-prove or reject the claimed chart coverage.  Starting from the complete
   double-root Newton fan, check that every low-valuation case except
   `alpha=2 beta` is excluded and that the sole survivor has
   `Q0=q(z-1)(z+2)` and `R0(1)=q^2/3`.  Then decide whether
   `Q=x Qhat`, `R=x^2 Rhat`, `x*y=Lambda^6`, followed by saturation by
   `x*y`, covers exactly every Puiseux arc with `0<beta<6`.  Charge possible
   ramification, nonintegral beta, amplitude rescaling, coefficients of Q or R
   with unequal valuations, and the `beta=0,6` endpoints.  Identify any
   dependence on a Newton-fan lemma not actually present in the frozen
   package.
4. Verify the simultaneous strict-slope chart
   `Lambda=tau^3*rho`: saturation by `tau*rho` must mean
   `v(Lambda)>3v(tau)>0`.  Check compatibility with the toric chart and exact
   row-8 target.  Say explicitly which strict slopes are and are not covered.
5. Verify the moving axis/cusp equations
   `p=-3a^2,c=2a^3+h`, their etaleness at `(a,h)=(1,0)`, and whether retaining
   `a,h` through interior saturation before imposing `a=1,h=0` includes all
   local cubic motion.  Check that all three coefficients of both Qhat and
   Rhat are present.
6. Derive the boundary equations from the nilpotent survivor:
   `Qhat(1)=Qhat(-2)=0`, `Qhat'(1)!=0`, and
   `27 Rhat(1)=Qhat'(1)^2`.  Audit the numerical factor 27 and verify that the
   other two Rhat directions remain free.  Check whether saturating by QD only
   after taking the boundary is the correct closure operation.
7. Audit scheme operations in encoding A.  Prove that four sequential
   principal saturations by `x,y,tau,rho` equal saturation by their product;
   verify Singular's `sat` list API, ring order, boundary addition, and final
   QD saturation.  Audit both synthetic controls and ensure none accidentally
   exercises a different operation.
8. Audit encoding B independently.  Verify the `(lp(2),dp(18))` syntax and
   that eliminating `u` from `I+(u*x*y*tau*rho-1)` and then `v` from
   `BOUNDARY+(v*QD-1)` computes the same two saturations without retaining an
   auxiliary variable or eliminating a load.  Check the controls and whether
   calling `eliminate` on the displayed standard bases is valid Singular
   semantics.
9. Charge fixed-load semantics.  The equations retain polynomial coordinates
   `k,mu,nu`, so a total-space formal arc may let them vary even though the
   theorem sought concerns constant loads.  Decide whether `H=1` would still
   uniformly exclude every fixed-load arc and why `H!=1` proves neither a
   fixed-load survivor nor a formal lift.  State the exact specialization or
   verticality repair required after any nonunit result.
10. Distinguish this chart from the finite exceptional algebra of VDIM 125.
    Decide whether any unproved finite-determinacy, properness, curve-selection,
    or local-to-global step has been smuggled into the preregistration.

Name the smallest failing identity or missing hypothesis, if any.  Separate a
source bug from a mathematical coverage gap and from a repairable exposition
issue.  Enforce all firewalls: a solver nonunit is not a lift, a solver unit is
only as broad as the proven chart coverage, the Newton-fan classification is a
separate theorem obligation, and no result here alone proves D1 or JC2.

Write exactly one report and make no other repository edits:

`xmodel/max12-912-order3-d1-double-root-toric-blowup-source-review-grok-20260825.md`

The report must state the frozen hashes, include explicit algebra checks, and
end with exactly one verdict token on its own line:
`CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `NOT_CONFIRMED`.
