# Independent implementation audit: total-Rees `T-rs` chart

You are an independent senior computational algebraist reviewing a live plane
Jacobian conjecture campaign.  Work in `/Users/dc/code/math/jc2`.  Read
`AGENTS.md` and the relevant local instructions first.

Your task is nonmutating analysis.  Create exactly one report:

```text
xmodel/max12-812-order2-p0-total-rees-t-rs-implementation-audit-codex-20260826.md
```

Do not edit any other file.  Do not edit, build, stage, reset, or clean
`jc2-lean`.  Do not run Singular, Sage, Macaulay2, or substantial symbolic
Python locally.  Read-only inspection and tiny hand/check scripts are allowed;
all eventual heavy algebra must be specified for AWS.

Read completely:

```text
xmodel/max12-812-order2-p0-total-rees-gate-t-obligation-table-20260826.md
xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md
xmodel/cross-empty-special-fibre-valuative-propagation-20260826.md
xmodel/max12-812-order2-p0-cech-lowcontact-pell-total-rees-successor-design-20260826.md
xmodel/max12-812-order2-p0-cusp-raw-g12-cech-certificate-v2-hostile-review-grok-20260826.md
cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_v2_20260826/RESULT.md
cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_v2_20260826/compile_raw_cusp_g12_cech_v2.py
cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_20260826/compile_raw_cusp_g12_cech.py
cases/max12_812_order2_p0_cusp_g10_g11_20260826/compile_p0_cusp_g10_g11.py
```

Follow every charged hash transitively where needed to understand the literal
source.  Then answer, with maximal skepticism:

1. Prove or refute the standard-chart formula
   `A[y_j]/((f_i y_j-f_j):f_i^infinity)` and the claimed finite-prefix
   surjection.  State all hypotheses and any base-change caveat.
2. Reconstruct the exact intended unspecialized Kummer substitution.  Decide
   whether the total source should use
   `p=-2*rho^2+2*sigma*ell1+...`, another expression, or additional root-
   value variables.  Trace conventions from source, not analogy.
3. Determine whether the existing `sigma^10`--`sigma^12` extractor remains a
   valid polynomial family over independent `rho`, or whether a bivariate
   Rees homogenization is required before coefficient extraction.  Give the
   smallest correct ring and grading.
4. Specify the exact `D_+(rs)` chart variables, actual Rees-kernel computation,
   `rho=0` base-change comparison, two-sided map to the frozen raw cusp
   algebra, and the lifted identity
   `s=sum H_i Phi_i+rho H`.  If the special-fibre difference is forced to be
   divisible by `rho^2`, prove it; otherwise reject that sentinel.
5. Give compiler-level pseudocode and a fail-closed validator contract,
   including negative controls for the nilpotent `g10_3` row, naive symmetric
   presentation, specialize-before-chart error, missing source jets, and
   forbidden denominators.
6. Identify the earliest likely mathematical or software failure.  If the
   proposed `T-rs` client is malformed, replace it with the smallest exact
   discriminator rather than repairing the desired conclusion by assumption.

Classify every assertion as theorem, exact deduction from frozen sources,
implementation proposal, or unresolved.  Do not promote a total-Rees or
moving-`p` result.  End with a binary launch recommendation and, if `GO`, an
AWS resource estimate and exact prerequisites.
