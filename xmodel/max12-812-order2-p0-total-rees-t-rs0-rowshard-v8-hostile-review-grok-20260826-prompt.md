# Different-model hostile review: `T-rs-0` V8 explicit normal form

You are the hostile software/source reviewer.  Write your report to

`xmodel/max12-812-order2-p0-total-rees-t-rs0-rowshard-v8-hostile-review-grok-20260826.md`.

Do not edit producer files, shared ledgers, or `jc2-lean`.  Do not run heavy
CAS locally; all controlling heavy results are already AWS artifacts.

## Read completely

- `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/PREREGISTRATION.md`
- `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/compile_t_rs0_rowshard_v8.py`
- `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/prepare_certificate_v8.py`
- `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/finalize_discovery_v8.py`
- `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/run_aws.sh`
- `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/FREEZE.sha256`
- `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/FAILCLOSED_INITIAL_LAUNCH.md`
- `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/FAILCLOSED_EVIDENCE.sha256`
- `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/RESULTS.md`
- `cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_20260826/RESULTS.sha256`
- the four complete harvested directories `aws_p32003_v8r1`,
  `aws_p65521_v8r1`, `aws_q_v8r1`, and `aws_p1000033_v8r1` under that package;
- frozen predecessors V7, V6, streaming V2, and discovery V0R1 that the V8
  compiler imports, including their freeze files and the original
  implementation audit/review named in those compilers.

## Required adversarial checks

1. Reproduce the reported Singular quotient-ring semantic hazard from the
   evidence/design and decide whether V8 actually eliminates it: there must
   be no `qring` in emitted programs, and every quotient operation that
   matters must be an explicit normal form in the ordinary parent ring.
2. Audit the full transitive import/hash chain.  Verify that V8 reconstructs
   all 569 frozen terms rather than changing the source.  In particular
   inspect `Fraction(str(raw_coefficient))`, coefficient-index orientation,
   cached powers, `k10/k6/k2` load mapping, the `Lambda -> sigma^2` exponent,
   target-row terms, and the exact legacy formula-text comparison.
3. Prove or refute that reduction after each factor multiplication/addition
   computes exactly the image of the frozen formula in
   `R/(sigma^13)`.  Check that normalizing source atoms and cached powers is
   algebraically sound and that no dependency can be lost except one whose
   complete quotient image is zero.
4. Audit the transformation logic and censuses: source-line matching,
   TPhi/FPhi replacement, staging/output path replacement, 83 derivative
   checks per row, explicit-NF canary, invalid numeric-`quit` removal, retained
   coefficients, and formula/update hashes.
5. Audit both validators fail-closed.  Check transcript diagnostics, metadata
   hashes, exact sentinel uniqueness, candidate/inactive custody, term-count
   versus nonzero bits, cross-row OR logic, kept-polynomial safety, and
   ordinary-ring recombination certificate.  Look specifically for a path
   on which a failed row/control could still yield `DISCOVERY.json`.
6. Independently compare the four result payloads.  Verify common order 10,
   the exact 23-name manifest, every inactive zero, and the exact-Q identity

   `Delta/rho^2 = 5120*rho^2*cs^4*k + 2640*cs^2*rs^2*k
                  -4608*cs*a0*c1 -4608*cs*a1*c0`.

   Check modular reductions at all three primes against the exact-Q retained
   polynomials; do not accept mere matching booleans.
7. Enforce scope: this is only complete source discovery modulo `sigma^13`.
   It is not an actual saturated Rees chart, base-change theorem, order-two
   exclusion, maximum-twelve proof, or JC2 verdict.

## Verdict

Start with exactly one of `CONFIRMED`, `REPAIR`, or `REFUTED`.  List every
finding by severity and exact file/line or artifact.  If confirmed, state
the narrow reusable theorem/certificate precisely and identify the next
smallest honest obligation.  If repairable, distinguish software-only
repairs from any mathematical change and forbid promotion until repaired.
