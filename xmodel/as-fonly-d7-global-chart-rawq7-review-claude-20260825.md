# Hostile review: AS D7 global accepted-chart raw-Q7 exclusion

**Reviewer: hostile different-model session (Claude), 2026-08-25.  All
repository bytes treated as immutable; nothing written except this file.**

**Verdict: CONFIRMED** — as an exclusion of the one displayed 13-trit chart
over the first emitted Q9-compatible corrected-Q10 predecessor, with the
already-frozen scope erratum
`xmodel/as-fonly-d7-global-chart-rawq7-scope-erratum-20260825.md` treated as
an inseparable rider on the exclusion report.  No mathematical, encoding,
splice, or arithmetic defect was found.  All issues enumerated in §8 are
wording, disclosure, or optional-hardening items; none changes the
mathematics.

## 0. Session constraints and evidence basis

This session had no shell: no Bash, no execution, no SHA-256 recomputation
of any file, and the 295 MB custody archive was not opened, per the review
charge.  Every hash statement below is a textual cross-consistency check
over frozen repository bytes; the Box02 stdout/JSON/solver/proof artifacts
are trusted as transported under `FULL_CUSTODY_INPUTS.sha256` and
`manifest_check.stdout` (53 × `OK`).  All load-bearing mathematics — row
counts, term-for-term encoding equality, the staged-division identity, the
divisibility-gate census, and operand bounds — was re-derived by hand from
the frozen sources.

Read in full: the exclusion report
`xmodel/as-fonly-d7-global-chart-rawq7-exclusion-20260825.md` and its scope
erratum; in `cases/as_fonly_d7_global_chart_qfbv_rawq7_20260825/`:
`PREREGISTRATION.md`, `RESULT_README.md`, `solve_global_rawq7.py`,
`SOURCE_CLOSURE.sha256`, `UPSTREAM_SOURCE_CLOSURE.sha256`,
`MANIFEST.sha256`, `FREEZE_RESULT.txt`, `SOURCE_PACKAGE_FILES.txt`, and the
custody sidecars (`FULL_CUSTODY_INPUTS.sha256`, `CUSTODY_FILE_LIST.txt`,
`manifest_check.stdout`); in the controls case: `PREREGISTRATION.md`,
`generate_preterminal.py`, `replay_preterminal_model.py`, both closures; the
V1 quarantine `cases/as_fonly_d7_global_chart_qfbv_20260825/QUARANTINE.md`;
and the entire pinned executable ancestry actually spliced at run time:
`solve_global_chart.py` (V1, `d4d4c17d…`), fullfibre `solve_state.py`
(`d6345f8b…`, with its `WRAPAROUND_CONTROL.md`), `compile_state.py`
(`abfd5cfa…`), `compile_fibre_kuranishi.py` (`cc75c22f…`),
`compile_witness.py` (`fbf327fb…`), and the vertical Q9 state gate
`compile_shard.py` (`54d05ebf…`).  Deeper ancestry (`3837508e…`,
`349ea509…`, …) was inspected only for splice/name integrity; its source
data is reused as previously hand-certified by the confirmed lineage
reviews (e.g. `as-fonly-d7-q7kernel-next-high-review-claude-20260825.md`
§1: `U=0`, `V=x²y`, `A=−x²`, `u_y=0`, `v_x=2xy`, `v_y=x²`, `L1=0`,
`K=−x⁴`, `Cbase=2x⁵`, `Dbase=0` at the frozen predecessor `c5_5=2`).  §4
below shows this reviewer's independent gate census agrees with the frozen
count, which corroborates that data again from a new direction.

Custody tie-out, textual only: SMT2 `46b755e1…`, CNF `19c1551c…`, DRAT
`5b36f877…`, model stdout `6cd687ba…`, replay JSON `877641bb…`, drat-trim
binary `92f0aa95…`, archive `e61d2c3d…`, report `839bbdd0…` appear verbatim
and mutually consistently across the exclusion report, RESULT_README,
FREEZE_RESULT, MANIFEST, FULL_CUSTODY_INPUTS, and the erratum.  Every
in-script pin matches the corresponding frozen closure line: producer↦V1
(`d4d4c17d…` = V1 `SOURCE_CLOSURE` line 2), V1↦`solve_state.py`
(`d6345f8b…` = fullfibre closure line 4), `solve_state.py` and
`replay_preterminal_model.py` both ↦ `compile_state.py` (same `abfd5cfa…`),
`generate_preterminal.py`↦producer (`69b90854…` = raw-Q7 closure line 2),
controls upstream closure ↦ raw-Q7 `SOURCE_CLOSURE` (`8bcd9a41…` =
MANIFEST line 6), and the `compile_state → fibre-kuranishi → witness → Q9
gate` pins recur identically in a dozen sibling frozen closures.

## 1. Chart parametrization and the 23 explicit Q9 rows (charge 1)

**Coverage is exact.**  `q9_origin` is the hard-coded 32-vector of
`compile_witness.py` (single 2 at index 23 = `w7_7`), re-asserted
`source_rows(source_data, q9_vector) == [0]*23` inside the exec'd prefix on
every producer run.  `q9_kernel` is the 19-vector kernel basis of the
affine Q9 system, built by `kernel_basis` in `compile_fibre_kuranishi.py`
with rank asserted 13 and each basis vector verified against the matrix; by
construction each kernel vector carries a 1 in its own free column and 0 in
the other free columns, so the parameter map is injective.  The 23 rows are
affine in the 32 unknowns (the only bilinear source, the bracket
`[Cfull, Dfull]` at degree 9, pairs a variable layer only against the
constant `Cbase/Dbase` layer at that degree; variable×variable bracket
terms top out at degree 6), and `compile_witness`/`compile_shard` both
carry the all-ones nonlinearity control.  Hence the solution set of the 23
rows is exactly `origin + span(kernel)`, and fixing
`t10=t11=t12=t13=t15=0, t17=1` while leaving the 13 coordinates
`(t0..t9,t14,t16,t18)` free sweeps exactly the displayed `3^13` chart:
`solve_global_rawq7.py` builds `q9_parameters` with those six constants and
13 `ULE ≤ 2` bit-vectors and reduces each coordinate `URem(·,3)`, so the
symbolic `xvalues` range over precisely the chart, no more, no less.  The
`forced` dictionary is byte-identical across producer fragment, V1,
`solve_state.py`, `compile_state.py`, and the replay script.

**The 23 rows are explicitly and correctly encoded.**  Lines 78–98 of the
producer transcribe integer `source_rows` term for term: `Cq9 =
Cbase+C2+C4`, `Dq9 = Dbase+D2+D4` (correctly *without* the Q8 layers
`C3/D3`), `Eq9 = L1+K+∂xCq9+∂yDq9` constrained at degrees 1 and 3 (2+4
coefficients); `F6q9 = E1_6 + [Mq9]₆ + ∂xW7 + ∂yZ7` (7); `G9q9 = F1_9 +
[Cq9,Dq9]₉ + [Tq9]₉` with `Tq9 = A·∂yZ7 + ∂xW7·v_y − u_y·∂xZ7 − ∂yW7·v_x`
(10).  Total 2+4+7+10 = 23, matching `assert 2+4+7+10 == 23` in the state
gate.  Consuming the constants `E1_6`, `F1_9` instead of dividing
symbolically is faithful: I checked by degree bookkeeping that `[M]₉` and
`[E]₆` take no contribution from any symbolic layer (the integer source
asserts `[M]₉ = 3·F1_9` on every call), so the divided constants are the
degree parts in question.  These 23 constraints are indeed redundant given
the parametrization — every chart point satisfies them identically — which
is exactly the self-auditing property claimed: a transcription error here
would surface as an UNSAT predecessor block, and the SAT control (§5)
proves the predecessor block is satisfiable.

## 2. Term-for-term audit of the 22 Q8, 19 raw-Q7, and 46 terminal rows (charge 2)

**Splice integrity.**  The producer executes exactly three byte-pinned
fragments of V1 after asserting each of the four split markers occurs once
(independently confirmed by this reviewer's full read of V1: `def
affine_matrix` only at line 66, the `forced` literal only at 135, `def
components` only at 213, `b7_symbolic = q7_residual([bv(0)] * 18)` only at
238).  Prefix = V1 lines 1–65 (which execs `solve_state.py`'s prefix ending
*before* any variable or constraint exists, so the inherited solver is
empty and `division_constraint_count` starts at 0).  Chart fragment = V1
lines 135–211.  Function fragment = V1 lines 213–237.  Everything else in
V1 — `affine_matrix`, the numeric `matrix7`, `EXPECTED_MATRIX_SHA`, the
RREF pivot analysis, `inverse_mod3`, `pivot_inverse`, the `uvars`, the
pivot-column elimination, the nine nonpivot compatibility rows, and V1's
own terminal loop — is never compiled into the V2 process.  Both fragments
are exec'd into the producer's module globals; I audited every free name
each fragment reads (`bv, badd, bmul, padd, pscale, pmul, pderivative,
pbracket, degree_part, lift_poly, homogeneous, divide_three,
constrain_row_zero, source_data, q9_origin, q9_kernel, tvars, yvars, z3`)
and each is bound at exec time to the intended object; no fragment name
shadows a producer name, and the fragment-defined `forced`/`free_q9` are
the ones the SAT branch would read.  No namespace or `exec` defect.

**22 Q8 rows.**  The chart fragment constrains `[E0]₂` (3), `F3` (4), `F5`
(6), `G8` (9) — 22, in the same blocks as integer `transition_rows`:
`row(E,2)+row(F3,3)+row(F5,5)+row(G8,8)`.  Term equality holds because the
degree-restricted symbolic sums coincide with the integer per-layer
derivatives by homogeneity: `[∂xW0+∂yZ0]₃ = ∂xW4+∂yZ4`, `[·]₅ =
∂xW6+∂yZ6`; `G8 = F1_8 + [N0]₈ + [T0]₈` matches `F1_8 + N8 + T8`.  The
integer source's `assert [E]₈ == {}` (no degree-8 E part) has no symbolic
counterpart, but it executes inside every producer run's prefix on the same
frozen source data, so omitting an `E1_8` term in `G8` is faithful.

**19 raw-Q7 rows.**  `restoration = list(rvars)` (18 fresh variables) is
passed to V1's `q7_residual`, whose body is a verbatim transcription of
integer `q7_rows`: `C6/D6` on Frobenius support `{y⁶, x³y³, x⁶}` from
`r0..r5`, `W5 = r6..r11`, `Z5 = r12..r17`; rows `row(F5,5) + row(F4,4) +
row(G7,7)` = 6+5+8 = 19 in the same order, with `F1_7 =
divide_three(E1_7 + [M]₇)` exactly mirroring `divide_exact(F7,3)`,
`F7 = E1_7 + [M]₇`.  All 19 residuals are constrained `≡ 0 mod 3`
directly.  Variable-order agreement with the integer `restored` zip
(`c6_0,c6_3,c6_6,d6_0,d6_3,d6_6,w5_*,z5_*`) was checked index by index.

**46 terminal rows.**  Producer lines 112–121 rebuild `C,D,W,Z =
components(restoration)`, `E,M,N,T,Rmix = core_intermediates(·)` and, for
each degree 9..12, impose `E1 = E_d/3`, `F1 = (E1 + M_d + (∂xW+∂yZ)_d)/3`,
`G1 = (F1 + N_d + T_d)/3`, `row(G1 + Rmix_d, d) ≡ 0` — 10+11+12+13 = 46
rows.  This is the same text as V1 lines 264–270, `solve_state.py` lines
228–235, and a verbatim transcription of integer `recursive_high`,
including the `Rmix = c_x·∂yZ + ∂xW·d_y − c_y·∂xZ − ∂yW·d_x` mixed layer.
No omitted row, no degree/order reversal, no stale variable, and no extra
constraint was found anywhere in the four blocks.  (One structural remark,
not a defect: at this predecessor the degree-12 row is vacuous — `N`, `T`,
`M`, `E` all top out below 12, `Rmix` at 11 — and both the symbolic and the
integer encodings make it identically zero, consistently; see §8 item 3.)

## 3. All 18 Q7 digits are raw; the quarantined V1 gap is absent (charge 3)

`rvars` are 18 independent `BitVec`s bounded only by `ULE ≤ 2`, fed
unmodified into `q7_residual`, with all 19 rows imposed as constraints.
There is no `affine_matrix` call, no `EXPECTED_MATRIX_SHA`, no RREF, no
pivot solve, no 9-parameter `uvars` reduction, and no compatibility-only
row subset anywhere in the executed V2 text — those live exclusively in
V1's skipped byte ranges (§2).  The V1 defect quarantined in
`QUARANTINE.md` was a *premise*: the Q7 restoration matrix used to
eliminate 9 of 18 digits had been audited constant only on 24 sampled
representatives of affine rank 11 < 13, so V1's certificate proves only its
reduced formula.  V2 removes the premise rather than repairing it: the
matrix object does not exist in the formula, so no constancy claim — true
or false — is consumed.  The producer's own metadata
(`uses_constant_q7_matrix: false`, `q7_explicit_source_row_count: 19`) and
the preregistration's "without a fixed-matrix reduction" are accurate.
Note the two formulas constrain the same mathematical solution set only if
the matrix really were globally constant; V2 needs no such fact, which is
precisely why its UNSAT closes the chart while V1's does not.

## 4. Bit-vector arithmetic audit (charge 4)

**Widths, bounds, wraparound.**  Everything is unsigned 32-bit; the only
predicates and operators are `ULE`, `URem`, `UDiv`, `+`, `*` — no signed
operator appears in any executed fragment.  `bv(int)` canonicalizes via
Python `% 729` (nonnegative, ≤ 728, including `pscale(−1,·) ↦ 728`).
`badd` reduces `URem(·,729)` after *every* addition, so intermediate sums
are ≤ 1456; `bmul` multiplies only canonical residues, bounding products by
`728² = 529984 < 2²⁰ < 2³²` — the bound the base compiler hard-asserts
before building the solver, and whose necessity the frozen 5-bit
counterexample (`WRAPAROUND_CONTROL.md`: `26·26` wraps) documents.
Divisors are the constants 3 and 729, never zero, so SMT-LIB division
underspecification is never touched.  Chart coordinates are `URem(·,3)`
≤ 2 before entering coefficients.  Wraparound is impossible in any term.

**Soundness direction.**  For the theorem only one direction is needed: any
F₃ solution of the integer congruence system yields values 0..2 satisfying
every `ULE` bound, and every gate then computes the integer value mod 729
exactly, so the BV formula would be SAT.  Checked-UNSAT therefore excludes
every F₃ assignment.  Since `3 | 729`, `URem(·,3)` of a mod-729 residue
equals the integer value mod 3, so `≡ 0 (mod 3)` rows are represented
exactly.

**Divisions.**  `divide_three` asserts `URem(v,3) = 0` — equivalent over ℤ
to exact divisibility of the represented value — and returns `UDiv(v,3)`.
If `v ≡ V (mod 3^k)` with `3 | V` then `UDiv(v,3) ≡ V/3 (mod 3^(k−1))`;
starting from exact mod-`3⁶` residues, the three nested divisions of the
terminal tower leave quotients exact mod `3³ ⊇` mod 3, so the final row
tests are exact.  Missing-key safety is structural: a monomial absent from
a BV polynomial dict is *identically* zero (not merely ≡ 0), so omitting
its gate loses nothing, while `constrain_row_zero` reads absent
coefficients as literal `bv(0)`.

**The staged /3 tower is the /243 congruence.**  Writing `P = P0 + 3U + 9C
+ 27W`, `Q = Q0 + 3V + 9D + 27Z` and expanding `det J(P,Q) − 1` by hand
gives, with `E = L1 + K + C_x + D_y` (using `L = A + V_y = 3·L1`,
`K = A·V_y − U_y·V_x`, `A = U_x − x²`):

```text
det J − 1 = 9·E + 27·(M + ∂xW + ∂yZ) + 81·(N + T) + 243·Rmix + 729·[W,Z].
```

Restricting to total degree `d` and requiring coefficientwise `243 |
(det J − 1)_d` is equivalent to `27 | E_d + 3(M + divWZ)_d + 9(N + T)_d`,
which (elementary back-substitution, done by hand both directions) is
equivalent to the staged conditions `3 | E_d`, `3 | F`, `3 | G`; the
quotient then satisfies `(det J − 1)_d / 243 ≡ G1 + Rmix_d (mod 3)`, the
`729·[W,Z]` layer dying mod 3.  So the 46 imposed rows are *exactly* the
"determinant−1 divisible by 243 with quotient ≡ 0 mod 3" terminal-high
congruences in degrees 9–12, and integer `direct_high` (literal `P,Q`
determinant with `divide_exact(·,243)`) is the independent literal form of
the same rows.  The producer/replay `recursive == direct` assertion checks
this identity numerically at the control point; the derivation above closes
it for all points.

**Independent gate census.**  Using the previously hand-certified source
data (`L1 = {}`, `K = −x⁴`, `Cbase = 2x⁵`, `Dbase = 0`, `u_y = 0`,
`v_x = 2xy`, `v_y = x²`) and the structural fact that `homogeneous()`
keeps all `d+1` keys, I counted every key passed through `divide_three` in
the V2 formula: Q8 block `E1_3` 4, `E1_5` 0, `F1_8` 0; Q7 block `E1_4` 1,
`E1_5` 6, `E1_7` 0, `F1_7` 7; terminal block `E1/F1` all 0, `G1` at degree
9 = 6 (from `∂xCbase·∂yD6`-type pairings), degree 10 = 11 (full
`∂xC6·∂yD6` spread), degrees 11–12 = 0.  Total **4 + 14 + 17 = 35**,
matching the exclusion report's "35 exact divisibility-by-three gates"
exactly.  This is a nontrivial two-sided corroboration: the frozen count
confirms the reviewer's reconstruction of the deep source supports, and the
reconstruction independently verifies the frozen count.

## 5. The SAT omission control and integer replay (charge 5)

`generate_preterminal.py` re-executes the byte-pinned producer *itself* up
to the unique marker `for degree in range(9, 13):`, so the control formula
is constructed by literally the same code path as the theorem formula with
only the terminal loop absent — not a re-implementation.  Boolector found a
model (stdout `6cd687ba…`, in custody); `replay_preterminal_model.py`
hash-pins the model file, parses the 63 binary assignments fail-closed
(missing variable ⇒ KeyError; value 3 ⇒ assert), rebuilds `xvalues` through
the same `forced/free_q9` map, and pushes everything through the *integer*
compiler (`compile_state.py`, same `abfd5cfa…` pin as the producer chain):
`source_rows == [0]*23`, `transition_rows == [0]*22`, `q7_rows == [0]*19`,
`recursive_high == direct_high`, and `any(high)` — with the attested count
of nonzero terminal coefficients equal to 1.

What this proves: (i) the predecessor block of the *actual* formula is
satisfiable, so the theorem's UNSAT cannot come from a broken chart
parametrization, a miscompiled Q9/Q8/Q7 row, an accidental contradiction
among source rows, or a missing Q7 fibre — any overconstraint that
empties the predecessor set is excluded, and the exhibited model
double-checks compiler↔integer agreement of all 64 predecessor rows at one
point; (ii) the terminal rows are the active gate — the model violates
exactly one terminal coefficient in integer arithmetic, pinning the
orientation (the exclusion bites at the terminal congruences, not before);
(iii) `divide_exact` inside the integer replay hard-asserts every staged
divisibility over ℤ at that point.  Note the control's evidential value is
independent of Boolector's honesty: any assignment with those properties
would do.

What it does not prove: it is a single-point control.  It cannot certify
that the BV predecessor encoding admits *every* mathematical solution
elsewhere on the chart, nor does it numerically exercise the SMT terminal
expressions themselves (the model was found without them; their integer
counterparts are what the replay evaluates).  Those gaps are closed
analytically in §§1–2 and §4 (term-for-term equality plus exact-arithmetic
faithfulness), not experimentally.  See §8 item 2 for an optional
hardening.

## 6. Proof trust boundary (charge 6)

Machine-checked, end to end: **the CNF with SHA-256 `19c1551c…` is
unsatisfiable.**  CaDiCaL 1.7.3 emitted a textual DRAT trace
(`5b36f877…`); an independently built `drat-trim` (source snapshot at
commit `2e3b2dc0…`, binary `92f0aa95…`, both in custody) returned
`s VERIFIED`, with the attested core (39,393 clauses, 7,508 lemmas,
8,815,141 resolution steps, 0 RAT lemmas — a RUP-only core, checkable by
the simplest fragment of the checker).

Trusted, not machine-checked, in decreasing order of exposure: (1) the
Python source compiler chain that builds the z3 AST — mitigated by the
seven-level byte-pinned exec chain, the redundant self-auditing Q9 rows,
the SAT control, and this review's hand audit; (2) z3's `to_smt2`
serialization of that AST into the pinned `46b755e1…` bytes (written before
any solve); (3) z3-solver 4.16.0's `simplify → bit-blast → tseitin-cnf`
equisatisfiability from those bytes to the pinned CNF; (4) the artifact
pairing — that these exact bytes fed Boolector, the bit-blaster, CaDiCaL,
and drat-trim — which rests on the custody archive's pinned scripts, rc
files, and stdouts (hashes in-repo, contents not re-opened here).  Risk (3)
is substantially diversified by Boolector 1.5.118 independently answering
`unsat` on the SMT2 through its own parser/bit-blaster/SAT core: two
unrelated translation-plus-decision pipelines agree, and one of them is
proof-checked.  The producer's own 10-second system-z3 smoke returning
`unknown` is retained and correctly given no evidential weight
(`unsat_is_theorem_without_checked_proof: false`).  What no solver
artifact can certify is the compiler faithfulness in (1)–(2); that burden
is carried by the source audit in this review plus the controls, which is
exactly the division the exclusion report claims.

## 7. Scope (charge 7)

The certified statement is: *the displayed 13-trit chart* —
`t10=t11=t12=t13=t15=0, t17=1` inside the 19-dimensional Q9 affine fibre
*over the single frozen predecessor* (`c5_5=2`, all other 29 coordinates
zero, the first emitted Q9-compatible corrected-Q10 state) — *contains no
point over which any of the `3^32` Q8 and `3^18` Q7 digit assignments
satisfies the 22+19 predecessor rows together with the 46 terminal-high
congruences.*  The scope erratum is load-bearing for reading the exclusion
report: unqualified phrases there ("complete `3^13` accepted chart",
"complete accepted chart … is empty") must be read as this one chart.  The
result does not cover: the other six Q9 kernel directions over the same
predecessor (the 19-dimensional fibre), the other 11,880 Q9-compatible
predecessors across 79 structural bases, the `a`/`g` endpoint families,
other associated-top branches, any Witt/characteristic-zero lift, any
landing statement, or any Jacobian-conjecture inference — and the frozen
report's refusal paragraph plus the erratum say so explicitly.  Within the
chart, however, the statement is genuinely universal (all 13 trits
symbolic, all 50 fibre digits raw); it is not a zero-section or sampled
claim.  The "accepted chart exhausts the relevant boundary components"
question is an open, separately-preregistered coverage obligation and is
not consumed here.

## 8. Findings (all non-mathematical; none changes the theorem)

1. **Headline wording vs. actual scope (repaired by existing erratum).**
   The exclusion report's headline and its JSON `scope` string say
   "complete accepted 13-trit Q9 chart" without naming the predecessor;
   read alone they invite the over-broad reading the erratum forbids
   (one predecessor's chart, not the fibre, not all 11,881 states).  The
   erratum (already frozen, producer bytes unchanged) is the cleanest
   repair; the only residual action is hygienic: every future citation of
   `as-fonly-d7-global-chart-rawq7-exclusion-20260825.md` should cite the
   erratum alongside it.  No frozen file should be edited.

2. **Terminal SMT rows are source-audited, not point-tested (optional
   hardening).**  The single-point control validates the predecessor
   encoding experimentally, but the terminal-block BV expressions are never
   numerically compared against `recursive_high` at any point (§5).  The
   gap is closed analytically here (§2, §4), and the identical block text
   has SAT-branch history upstream (`solve_state.py` asserts
   `not any(high)` against SMT models in fullfibre runs).  Cleanest
   hardening if ever desired: evaluate the 46 BV rows at the control model
   by substitution and compare with the integer `high` vector — a few
   lines, no new trust.

3. **13 of the 46 terminal rows are vacuous at this predecessor
   (cosmetic).**  With `Cbase = 2x⁵`, `Dbase = 0`, all degree-12
   contributors (`E`, `M`, `divWZ`, `N`, `T`, `Rmix`) vanish structurally,
   so the degree-12 row is `0 ≡ 0` in both encodings, and degree 11 binds
   only through `Rmix`.  The count "46" is honest as the number of imposed
   congruences; the mathematical content lives in degrees 9–11.  No
   action.

4. **Attestation reliance (disclosure).**  The SMT2 byte length, solver
   timings and RSS, CNF variable/clause counts, drat-trim core statistics,
   Boolector/CaDiCaL version strings, and the "exactly one nonzero
   terminal coefficient" count are transported facts under pinned hashes in
   the unopened custody archive; this session verified their in-repo hash
   plumbing and internal consistency (including the empty-string SHA for
   `cadical.launcher.stderr`) but did not re-derive them — except the
   35-gate count, which §4 re-derives by hand and confirms.

5. **Upstream closure is one-hop-linked, not flattened (nit).**  The
   raw-Q7 `UPSTREAM_SOURCE_CLOSURE.sha256` pins only V1's closure file;
   deeper pins live hop-by-hop in ancestor closures and, decisively, as
   hard SHA asserts inside every executed script, so no unpinned byte can
   execute.  Sound as-is; a flattened transitive closure in the case
   directory would ease future audits.  No repair required.

## 9. Verdict

**CONFIRMED.**  The four constraint blocks are exact transcriptions of the
independent integer source functions; the 18 Q7 digits are raw existential
variables and the quarantined fixed-matrix premise is structurally absent;
the 32-bit modular circuit is wraparound-free and its staged divisions
encode precisely the `/243` terminal congruences (hand-proved identity);
the SAT omission control and independent integer replay rule out
predecessor-side overconstraint and pin the terminal orientation; the
UNSAT rests on a proof-checked CNF plus a second, independent solver on
the same pinned SMT2, with the trusted compiler layer discharged by source
audit; and the hand-recomputed divisibility-gate census (35) matches the
frozen attestation.  The theorem is exactly the erratum-narrowed statement
in §7: one complete 13-dimensional accepted chart over the first
corrected-Q10 predecessor is empty at the terminal-high gate, with every
Q8/Q7 fibre digit existential.  Nothing wider is certified, and nothing
narrower would account for the artifacts.
