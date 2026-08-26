# Text-only hostile follow-up — D1 double-root correction rays

Act as a hostile valuation-theory referee.  This is a **text-only algebra
review**.  HARD RULE: do not execute Python, Singular, Sage, msolve, Lean, any
solver, or any substantive symbolic computation on the local Mac.  You may
read files, inspect already-emitted AWS text, and check hashes with lightweight
shell tools.  The charged exact replay has already run on AWS; reason through
the displayed identities by hand.

Verify these frozen artifacts:

```text
466736cdd1a76607e6475c98d9da4b55096e88813d911722954549bdcba702c0  xmodel/max12-912-order3-d1-double-root-newton-fan-correction-firewall-20260825.md
bbbd7aec20d5a987ae619f7530ea08a3267e32be035ab3534f615543df70b2d0  cases/max12_912_order3_d1_double_root_correction_recurrence_20260825/FREEZE.sha256
2f718839bb063f3f889d5bbca2688d3fac5d5ba1a19ae7a5ca3634324a5eed40  cases/max12_912_order3_d1_double_root_correction_recurrence_20260825/aws_box02/stdout
015ed8156197ba4cfac55cbc6d33379d7545739bfe657856febd8e17c8d3913c  cases/max12_912_order3_d1_double_root_toric_blowup_20260825/FREEZE.sha256
```

Also read `SCOPE_ERRATUM.md`, `SOURCE_REVIEW_ERRATUM.md`, and the recurrence
`DESIGN.md`.  Charge every item below explicitly.

1. Starting from
   `(4/9)QR/K+(2/9)R^2/K^2-(4/81)Q^3/K^2`, verify by hand that for
   `K=L^2U,N=LU`,

   ```text
   Q=t^beta N,
   R=t^alpha L+t^(2beta)U/9,
   3beta/2<alpha<2beta,
   ```

   the lower QR term is polynomial and the complete weight-`3beta` tail
   cancels.  Check all inequalities and omitted-term weights.
2. Verify by hand that with

   ```text
   alpha=15/2, 5<beta<6,
   Q=t^beta L,
   R=t^alpha N-(1/2)t^(15-beta),
   ```

   the lower QR term is polynomial and the weight-15 expression is exactly
   `(2/3)/K`, hence only row 3.  Check signs, exponent `15-beta`, and fixed
   load `mu=2/3`.
3. Audit the already-emitted AWS replay: source hash, rc, empty stderr, terminal
   marker, the two deletion controls, and its firewall.  Do not rerun it.
4. Decide whether Puiseux ramification or the strict chart
   `Lambda=t^4,tau=t,rho=t` forbids either example.
5. State precisely whether these finite successors disprove the proposed
   whole low-fan classification while proving neither a formal lift nor D1.
6. Separately decide whether the frozen compiler remains exact for the tied
   `alpha=2beta` boundary it actually encodes.  Distinguish a source-equation
   bug from the withdrawn fan-completeness sentence.
7. Audit the recurrence design.  Does individual coefficient-series
   convolution retain all earlier layers?  Is certified traversal of every
   coordinate-support and Groebner/tropical cone a plausible completeness
   route?  Enforce that bounded `(M,N)` runs are fixed-slope screening until a
   finite fan certificate exists and that load coordinates must be constant.
8. Explain exactly why the earlier hostile report's “higher corrections sit
   in free Qhat,Rhat” sentence does not justify imposing pure `K^2`
   divisibility before those corrections are included at the same weight.

Write exactly one report and make no other repository edits:

`xmodel/max12-912-order3-d1-double-root-newton-correction-review-grok-v2-20260825.md`

State that no local substantive computation was run.  End with exactly one
token on its own line:
`CORRECTION_CONFIRMED`, `CORRECTION_REPAIRED`, or `CORRECTION_REJECTED`.
