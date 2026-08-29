You are Opus 5 acting as a hostile mathematical reviewer for the plane
Jacobian conjecture campaign. Work in `/Users/dc/code/math/jc2`.

Review the frozen producer report

`xmodel/sigray-later-m-package-source-audit-sol-ultra-20260828.md`

whose required SHA-256 is

`5fc6b1634dc1ef0a0abe578411644fa166ffbfa16b8608cbce2a7b7b61465cd5`.

Audit it independently against `refs/sigray_full.pdf`, especially printed
pp. 39--45 and every earlier statement it actually consumes. Do not merely
check the root endpoint: adjudicate the full repaired package.

Required checks:

1. Verify or refute the local root-order lemma `(L6-root)` and its claimed
   repair of Corollary 6.1. Track every integrality and strict inequality.
2. Verify Proposition 8.1's UFD/perfect-power argument, handling negative
   Bezout exponents, polynomiality of `q`, and the exact `M_F` gcd formula.
3. Verify the orientation and adjacent tower transport in Statements
   8.3--8.5. In particular test whether every tower member used in the
   proposed direct proof of Statement 8.4 is genuinely nonterminal at the
   lower vertex and a positive integral power of the same reduced pattern.
4. Verify Proposition 8.2/Corollary 8.1 after restoring the omitted `h_0`
   factor. A positive valuation at one root is not enough unless the report
   correctly proves all other valuations are nonnegative.
5. Adjudicate the proposed unique-down-child repair `(Reg)` of Proposition
   8.3 and its use of repaired Propositions 6.7/6.8. Check sibling exclusion,
   rootward preservation, and all hidden existence/branch hypotheses.
6. Reprove the corrected nonroot Proposition 8.4 axis contradiction, or give
   the earliest precise failure. Separately adjudicate the root clause as
   proved, false with a fully typed polynomial-tower countermodel, or an open
   proof gap. Do not count a bare ODE/leading-form packet as a countermodel.
7. Check the producer's canonical-consumer blast radius: pole-entry uses are
   nonroot; root-only and root-inclusive suffix claims are unsupported if the
   root clause remains open.

Use explicit equations and dependency typing. Distinguish source gaps,
repairable errata, campaign replacement theorems, and false statements.
Report a verdict for every promoted recommendation in producer Section 15.
Flag any claim whose proof needs a theorem not actually established in the
audited package.

Write exactly:

`xmodel/sigray-section8-full-hostile-review-opus5-20260828.md`

Keep the report below 5,000 words and the final CLI response below 150 words.
Do not edit any existing artifact or canonical/top-level file. Never enter,
list, search, read, build, status, or modify `jc2-lean`. Preserve the dirty
worktree. Your only write may be the required report. No AWS, web, or heavy
local CAS; light exact symbolic checks are allowed.
