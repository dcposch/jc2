# Focused hostile review: AS D7 first-predecessor complete Q9 fibre

Act as an independent hostile referee for a source-compiled finite algebra
claim.  Work read-only except for writing your final review to exactly:

`xmodel/as-fonly-d7-first-predecessor-full-q9-rawq7-review-grok-20260825.md`

Do not modify any producer, case, custody, ledger, quarantine, or other file.
Do not browse.  Use repository Read/Grep/Glob only: no Bash and no new
computation.  Disclose that hashes and solver runs were not independently
rerun.  Read every charged file in full and follow each directly hash-pinned
source dependency needed to audit the compiler.

## Charged producer and custody

- report:
  `xmodel/as-fonly-d7-first-predecessor-full-q9-rawq7-exclusion-20260825.md`
  SHA-256 `fe32d0bf3a3451546f9bfc77cc0a7e107e82b2bc834a4a6311919e002f2b6530`
- case:
  `cases/as_fonly_d7_first_predecessor_full_q9_rawq7_20260825/`
- patch compiler:
  `cases/as_fonly_d7_first_predecessor_full_q9_rawq7_20260825/solve_full_q9.py`
  SHA-256 `ac6654ab044a948ee4499b47ac346a5911b55b4c886c77c6e25bf90719b4855c`
- manifest SHA-256:
  `827f2d28004feae007bea0a50868755e94f921d05a720df6e21fa543afdeed35`
- freeze-record SHA-256:
  `3864e7883e9edc899cc18be8ad9516eb5bef4a24fdf8876753db2cce3efad8bf`
- source-closure SHA-256:
  `4cb58ff4c49e53f2f7d5d884487a3cf820f91b47fbec89affeab7a8190cbcfcb`
- oversized custody archive SHA-256 (do not open/unpack it):
  `601076db6aa5f27e74315657baf7c5a87c2ad64982011612064ee26c1c3f5649`
- hash-pinned immediate parent:
  `cases/as_fonly_d7_global_chart_qfbv_rawq7_20260825/solve_global_rawq7.py`
  SHA-256 `69b908545775f4df1e10884c867cb767b8d1e997be33e386a730a2eaed585988`
- parent report and preregistration:
  `xmodel/as-fonly-d7-global-chart-rawq7-exclusion-20260825.md` and
  `cases/as_fonly_d7_global_chart_qfbv_rawq7_20260825/PREREGISTRATION.md`
- SAT-control compiler/replay sources named in the charged report and
  manifests, plus every hash-pinned upstream source file they consume.

## Exact provisional claim

Fix the first Q9-compatible corrected-Q10 predecessor in the frozen
30-coordinate order: `c5_5=2` and all other predecessor coordinates zero.
The producer claims that no assignment over `F_3` to all 19 Q9-kernel trits,
all 32 raw Q8 trits, and all 18 raw Q7 trits satisfies 23 explicit Q9 source
rows, 22 explicit Q8 source rows, 19 explicit Q7 source rows, and 46 terminal
rows in degrees 9--12.  This is intended to cover the complete Q9 affine
fibre over that one predecessor, not merely the parent's 13-trit accepted
subchart.

The claim is **producer-exact and independently proof-checked, but
provisional pending this source/compiler review**.  A checked DRAT trace
establishes UNSAT of the emitted CNF; it does not by itself establish that the
Python source emitted the intended mathematics.

## Mandatory hostile charges

1. **Patch anchors and complete-fibre coverage.** Inspect the two
   load-bearing replacements in `solve_full_q9.py` exactly: (a) 13 symbolic
   Q9 trits become 19; (b) the forced 13-trit chart header becomes
   `q9_origin + q9_kernel*t` for all 19 kernel directions.  Confirm the old
   chart fragment is replaced exactly once, no old forced coordinates survive,
   the Q9 matrix really has rank 13 in 32 variables at this predecessor, and
   the 19 displayed vectors really span its full kernel.
2. **Parent raw-Q7 compiler.** Audit the hash-pinned parent from source, not
   prose.  Compare its symbolic 23 Q9, 22 Q8, 19 raw-Q7, and 46 terminal rows
   term-for-term with the independent integer functions `source_rows`,
   `transition_rows_numeric`, `q7_rows_numeric`, `recursive_high_numeric`,
   and `direct_high_numeric`.  Look for omitted divided-Frobenius/carry terms,
   wrong signs or constants, reversed coefficient ordering, stale fixed
   variables, namespace/`exec` mistakes, and accidental extra constraints.
3. **Raw existential variables.** Verify all 32 Q8 and all 18 Q7 digits are
   genuinely independent ternary existential variables.  Confirm no sampled
   representative, fixed RREF section, constant-Q7 matrix, zero-section, or
   compatibility extrapolation remains.
4. **Arithmetic typing.** Audit unsigned 32-bit modulo-729 gates,
   per-operation reductions, maximum unreduced products/sums, and every exact
   divisibility constraint before `/3`.  Check that the recursive three
   divisions encode the required integer `/243` terminal congruence modulo
   three for canonical integer representatives.  Attack signed/unsigned,
   overflow, and representative-change hazards.
5. **SAT/direct-source control.** Verify that the terminal-omission SAT model
   is a literal point of the enlarged 19-trit chart and that the independent
   integer replay checks all 23/22/19 rows, recursive-versus-literal `/243`,
   and exactly one nonzero terminal coefficient.  State precisely which
   overconstraint/compiler failures this catches and which it cannot catch.
6. **Proof/custody boundary.** Trace the recorded SMT SHA
   `0061e1ccd62c849d54db9258247413d8fe80bf8cdf696ef987ea904fae89fd5d`,
   CNF SHA
   `a25c7ed0f48766548fc518f9de2b4c7d4e51e413c085dc30f68d6668f1928369`,
   DRAT SHA
   `b8dbb0649833f5c545190e6b56e0efb4c9721385f08a553fdfd92d25ff956eda`,
   and recorded `drat-trim` `s VERIFIED`.  Distinguish: checked CNF UNSAT;
   trusted SMT-to-CNF translation; and source-to-SMT correctness.  Do not
   call the source compiler independently verified merely because DRAT
   verifies the emitted CNF.
7. **Scope firewall.** At most this kills one of 11,881 Q9-compatible
   corrected-Q10 predecessor states, with its complete Q9/Q8/Q7 fibre.  The
   other 11,880 states within the same 79-base vertical problem, separate
   `a`/`g` endpoints, nonreduced incidence, other associated-top branches,
   all-depth lifting, bounded support, characteristic-zero algebraization,
   a counterexample, and JC2 remain open.

Name the smallest false row, stale assumption, omitted state, missing
hypothesis, certificate gap, or wording defect.  Give verdict `CONFIRMED`,
`CONFIRMED WITH REPAIRS`, `REJECTED`, or `INCONCLUSIVE`.  State separately
(i) the source/compiler verdict, (ii) the proof-certificate verdict based on
recorded custody, and (iii) the exact maximum promotable sentence.  Do not
broaden the scope even if every check passes.
