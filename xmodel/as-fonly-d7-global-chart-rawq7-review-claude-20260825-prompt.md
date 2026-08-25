# Hostile review: AS D7 global accepted-chart raw-Q7 exclusion

Act as an independent hostile referee for an exact finite-state algebra and
proof-certificate claim. Read these files in full, following their directly
named source dependencies where necessary:

- `xmodel/as-fonly-d7-global-chart-rawq7-exclusion-20260825.md`
- `cases/as_fonly_d7_global_chart_qfbv_rawq7_20260825/PREREGISTRATION.md`
- `cases/as_fonly_d7_global_chart_qfbv_rawq7_20260825/RESULT_README.md`
- `cases/as_fonly_d7_global_chart_qfbv_rawq7_20260825/solve_global_rawq7.py`
- `cases/as_fonly_d7_global_chart_qfbv_rawq7_20260825/SOURCE_CLOSURE.sha256`
- `cases/as_fonly_d7_global_chart_qfbv_rawq7_20260825/UPSTREAM_SOURCE_CLOSURE.sha256`
- `cases/as_fonly_d7_global_chart_qfbv_rawq7_controls_20260825/generate_preterminal.py`
- `cases/as_fonly_d7_global_chart_qfbv_rawq7_controls_20260825/replay_preterminal_model.py`
- `cases/as_fonly_d7_global_chart_qfbv_20260825/QUARANTINE.md`
- the hash-pinned upstream compiler files directly consumed by the above.

Do not read or unpack the 295 MB custody archive, browse, run shell commands,
or perform any new computation. Use repository Read/Grep/Glob only. You may
write exactly the report requested below.

The narrow claimed result is: over F_3, no assignment in the complete
accepted aligned 13-trit Q9 chart, with all 32 raw Q8 digits and all 18 raw Q7
digits existential, satisfies the explicit 23 Q9, 22 Q8, 19 Q7, and 46
terminal-high source congruences. The V2 formula does not consume a constant
Q7 matrix. Its SMT formula is independently UNSAT in Boolector; Z3 4.16
bit-blasting produced a pinned CNF; CaDiCaL produced a DRAT proof; an
independently built drat-trim returned `s VERIFIED`. Omitting terminal-high
rows is SAT, and that model replays all integer source rows with exactly one
terminal coefficient nonzero.

Try to falsify every load-bearing point:

1. Does the origin/kernel parametrization with 13 trits cover exactly the
   accepted aligned Q9 chart? Are all 23 Q9 source rows also explicitly
   encoded correctly?
2. Compare the symbolic 22 Q8 rows, 19 raw-Q7 rows, and 46 terminal rows
   term-for-term with the independent integer functions `transition_rows`,
   `q7_rows`, `recursive_high`, and `direct_high`. Look for omitted rows,
   degree/order reversals, stale variables, namespace/`exec` mistakes, or
   accidental extra constraints.
3. Confirm that all 18 Q7 digits are genuinely raw existential variables and
   that no sampled/fixed Q7 matrix, pivot solve, or compatibility assumption
   remains in V2. Explain why the quarantined V1 gap is absent.
4. Audit the 32-bit unsigned bit-vector arithmetic: every operand bound,
   absence of wraparound, reduction modulo 729, exact divisibility constraints
   before each `/3`, and why this represents the required integer `/243`
   terminal congruences modulo 3. Flag signed/unsigned or representative
   errors.
5. Audit the SAT omission control and independent integer replay as a
   meaningful overconstraint/compiler negative control. State what it does
   and does not prove.
6. Audit the proof trust boundary: SMT hash -> Z3 simplify/bit-blast/
   tseitin-CNF hash -> CaDiCaL DRAT hash -> independently built drat-trim
   `s VERIFIED`. Distinguish checked CNF UNSAT from the trusted SMT-to-CNF
   translation and source compiler.
7. Enforce scope. This is one accepted aligned D7 chart, not an all-AS,
   all-depth, characteristic-zero, landing, or JC2 theorem unless a separate
   coverage theorem says so.

Write only
`xmodel/as-fonly-d7-global-chart-rawq7-review-claude-20260825.md`.
Give verdict `CONFIRMED`, `CONFIRMED WITH REPAIRS`, or `REJECTED`. Enumerate
all issues, say whether any changes the mathematics, and give the cleanest
repair. Do not edit producer, custody, quarantine, or frozen files.
