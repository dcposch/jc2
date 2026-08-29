# Hostile review: order-two `p=0`, `D(rs*k0)` cusp grade-12 unit

You are the independent hostile reviewer.  Work read-only except for the
single report named below.  Do not run Singular, Sage, msolve, Lean, or any
heavy/exhaustive computation.  Do not touch `jc2-lean` or any shared top-level
ledger.  Inspect only the frozen files named here and the explicitly pinned
transitive source needed to audit them.  Stored PASS strings are evidence,
never authority.

Write exactly one report:

`xmodel/max12-812-order2-p0-cusp-grade12-unit-hostile-review-grok-20260826.md`

## Frozen target

- producer report
  `cases/max12_812_order2_p0_cusp_grade12_unit_replay_20260826/RESULT.md`,
  SHA-256 `fadb2794e395bfbc037aac4cd68b88eb1304ce8e58883d391f847e8a09aa4526`;
- evidence manifest
  `cases/max12_812_order2_p0_cusp_grade12_unit_replay_20260826/RESULTS.sha256`,
  SHA-256 `9008a545ec71f0f67719c0f37c2c58ac0d3e8e9e7a4de7b20a9b2c8661c766d7`;
- frozen-source manifest
  `cases/max12_812_order2_p0_cusp_grade12_unit_replay_20260826/FREEZE.sha256`,
  SHA-256 `0fc1d6f4a52d54df98d5c650611421a2e82657038840be54a6f60f95641145a2`;
- independent exact collector
  `cases/max12_812_order2_p0_cusp_grade12_unit_replay_20260826/replay_p0_cusp_grade12_unit.py`,
  SHA-256 `31f21bce95686110fbb90dc24eb94eb9a38bd8cc5341519b795f6f1dbd7c6244`;
- final preregistered design
  `xmodel/max12-812-order2-p0-cusp-grade12-unit-successor-design-20260826.md`,
  SHA-256 `b426aa9e516b9c1a01e3b8510ddd5ad6415e5125523fbe3e7d409ef3e657c220`;
- companion raw-chart design
  `xmodel/max12-812-order2-p0-cusp-successor-design-20260826.md`,
  SHA-256 `04ca7018ad1609dfd11839914ecbe214cf896ad78edd661cbeecc07f18614622`;
- AWS metadata
  `cases/max12_812_order2_p0_cusp_grade12_unit_replay_20260826/AWS_LAUNCH_METADATA.md`,
  SHA-256 `3643549ac96ed7324eed354f90f3f217348d4442a58dd3b84fda3b5ee7c0e421`.

First verify the target hashes and every entry of `RESULTS.sha256`.  Read the
actual collector, both result JSON files, both exact stdout/validation/meta
records, the frozen tails identified by `FREEZE.sha256`, and only the source
compiler routines actually imported or reproduced by the collector.

## Load-bearing questions

Give an explicit verdict on every item.

1. Verify the raw localized grade-ten algebra.  From the four displayed raw
   rows on `D(rs*k0)`, does one obtain `c0=0` in the raw quotient, then
   `5*k0*rs^3+96*c1^2=0` and
   `15*k0*cs*rs^2+96*a0*c1=0` without silently radicalizing?  Check that the
   `(k,tau,d)` parametrization is an actual Laurent-chart isomorphism and that
   `D(k*tau)=D(rs*k0)` there.
2. Audit independence and completeness of the collector.  Does it really
   reconstruct the complete normalized primitive coefficient series and all
   seven canonical tail rows through absolute grade twelve from the frozen
   tails, rather than importing the earlier Singular answers or hardcoding
   the claimed row?  Check `p`, all `R,A,C,k10` corrections through required
   order, lower loads `k6,k2`, and all terminal targets at their exact source
   grades.
3. Verify the absolute/half-weight convention and the ordinary-to-Faber
   transform, including every moving-centre connection term that can enter
   grades ten through twelve.  Check the claimed zero rows below grade ten and
   normalized grade-ten identities from actual collected expressions.
4. Independently recompute the exact grade-eleven fourth and third pivots
   `-(864/25)k^4 tau^6 ell1` and `(18/5)k^2 tau^3 e0` after the allowed prior
   reduction.  Check that their coefficients are units on the stated open.
5. Independently audit the decisive raw grade-twelve sixth row.  Before any
   grade-eleven pivot substitution, is it exactly
   `(18144/125)k^5 tau^8=-(21/1024)rs^3u^2`?  Identify every frozen-tail
   monomial and every second correction, moving-`p`/Faber connection, moving
   load, and lower-load term that can reach this row.  A missing term or a
   cancellation that requires an uncharged equation is fatal.
6. Verify that row six has no target at grade twelve and that the first target
   grades 28, 32, 36, 38 use the correct convention.  Check that the displayed
   coefficient is genuinely a Laurent unit on `D(rs*k0)` and that this kills
   the raw cusp open without needing a radical, Gate A, terminal row, or Taylor
   pullback.
7. Recompute the focused specialization.  Confirm that exactly four frozen
   tail monomials contribute `-9/1024,-3/256,+3/256,-3/256`, with sum
   `-21/1024`; ensure this is an independent sign/row control rather than a
   second copy of the asserted formula.
8. Audit both AWS records and negative controls.  Exact Q, not the modular
   residues or stored PASS tokens, must carry the characteristic-zero claim;
   `21/1024` must remain nonzero in both control primes.
9. Enforce scope.  A confirmation licenses only raw localized exclusion of
   the post-`M=0`, `p=0`, `D(rs*k0)` cusp open.  It does not cover the odd
   chart, the residual `R=C=0` zero section, moving or ramified `p`, `k0=0`,
   finite Taylor/global overlap, all square/order-two strata, maximum twelve,
   or JC2.

Search for the smallest failing coefficient, missing source term, illegal
reduction, hash mismatch, or scope leak.  If any load-bearing point fails,
issue `REPAIR` or `REFUTED` and quote the exact smallest obstruction.  Do not
rescue a gap with an unstated theorem or an analogous chart.

End the report with exactly one final token:

- `ORDER2_P0_CUSP_GRADE12_UNIT_CONFIRMED`
- `ORDER2_P0_CUSP_GRADE12_UNIT_REPAIR`
- `ORDER2_P0_CUSP_GRADE12_UNIT_REFUTED`
