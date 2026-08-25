# Hostile review: AS D7 pointwise Q9-witness to Q8 Kuranishi obstruction (V3)

**Reviewer: hostile different-model session (Claude), 2026-08-25.  All
repository bytes treated as immutable; nothing written except this file (a
staged, unexecuted replay script was left outside the repository at
`/tmp/as_q9q8_v3_review_check.py`).**

## 0. Session constraints and evidence basis

This session had no shell: no Bash, no execution, no SHA-256 recomputation of
any file, payload, or archive.  Every hash statement below is a textual
cross-consistency check over frozen bytes; the AWS stdout/stderr/time/meta
are trusted as transported under their manifests.  All mathematics below was
re-derived by hand from the frozen sources — the complete 22×32 system was
rebuilt from first principles in this review, and no PASS string or emitted
number was accepted without that reconstruction.

Read in full: the charged report
`xmodel/as-fonly-d7-q9-witness-q8-kuranishi-pointwise-20260825.md`; every
file of `cases/as_fonly_d7_q9_kuranishi_q8_witness_v3_20260825/` including
the result directory (`replay.stdout/.stderr/.time`, `run.meta`,
`OUTPUTS.sha256`), both freezes, both manifests, `SOURCE_CLOSURE.sha256`,
`SOURCE_PACKAGE_FILES.txt`, `PREREGISTRATION.md`, `README.md`,
`RESULT_README.md`, `run_remote.sh`, `compile_witness_v3.py`; the V2 and V1
cases (`compile_witness_v2.py`, `compile_witness.py`, their freezes,
preregistrations, READMEs); the parent Q9 gate's `compile_shard.py`,
`FREEZE_RESULT.txt`, `shard_00.out`, `aggregate.out`,
`REMOTE_RESULTS_MANIFEST.sha256` (spot-checked), and its confirmed hostile
review; the pinned `generate_degree10_gate.py` elimination block; and the
ledger entry in `notes.md` (2026-08-25 02:02Z live state).

Custody tie-out, textual only: report SHA `0227176c…`, result-manifest SHA
`c68c43d8…`-listed entries, stdout `f40ee012…`, stderr `e3b0c442…`,
matrix/RHS hashes `addcbc1e…`/`f2c3b732…`, and run metadata (Box02 /
`ip-172-30-0-186`, tag `as_q9_q8_kuranishi_v3_20260825T020224Z`, rc 0,
10.81 s, 20,688 KiB peak RSS, window 02:02:55Z–02:03:06Z) appear verbatim
and mutually consistently in `FREEZE_RESULT.txt`, `RESULT_MANIFEST.sha256`,
`OUTPUTS.sha256`, `run.meta`, `replay.time`, the stdout, and the report.
`replay.stderr` is empty on read, and its recorded hash is the canonical
empty-input SHA-256, verifiable without a shell.  The git head `2e6104a…`
matches all three freezes.  The charged result-freeze self-hash `7dde1c07…`
appears nowhere in the repository except the review charge; it cannot be
corroborated here (see finding 2).

## 1. Source/witness identity and the V1/V2/V3 relation

**Identity is verbatim.**  The parent gate freezes
`Q9_first_witness = (state, witness, count)` in both `shard_00.out` (line
18) and `aggregate.out` (`aggregate_Q9_first_witness`, line 40): a 30-list
that is zero except value 2 at index 23, a 32-list that is zero except value
2 at index 23, and count `1162261467 = 3^19`.  V1's hard-coded
`predecessor_vector` and `q9_vector` equal these lists entry-for-entry, and
V1 zips them against the *same* pinned name tuples
(`structural+frob+unknowns`, `new_names`) exported by the exec'd Q9-gate
prefix, so no reordering is possible even in principle.  Under the frozen
name order (structural 7, Frobenius 6, unknowns 17) index 23 is `c5_5`;
under `new_names` (c2,d2,c4,d4,w7,z7) index 23 is `w7_7`.  So the charged
point is: predecessor `c5_5=2`, all other 29 coordinates zero; Q9 assignment
`w7_7=2`, all other 31 restored coordinates zero — exactly the state the
parent hostile review hand-certified, in the `(13,13)` stratum with fibre
`3^19` (count agrees).  Compatibility was re-proven here by hand: at this
predecessor `U=0`, `V=x²y`, `A=−x²`, `u_y=0`, `v_x=2xy`, `v_y=x²`, `L=0`,
`K=−x⁴`, `Cbase=2x⁵`, `Dbase=0` (the `generate_degree10_gate.py`
elimination block was inspected: every eliminated digit is a constant-free
combination of `K`-coefficients and free digits, all zero here, so the
recorded digits vanish except `C5=2x⁵`); the only nontrivial Q9 row is
`F_6`'s `x⁶` coefficient `10+7·w7_7+z7_6≡0`, which at free-coordinates-zero
forces `w7_7=2`; all other 22 rows vanish identically.  The vector is a
canonical assignment licensed by the parent, not a point outside its
convention.

**Hash-pinned chain.**  V3 reads V2's bytes and asserts SHA `01804fe3…`
before exec; V2 reads V1's bytes and asserts `fbf327fb…`; V1 reads the Q9
gate's bytes and asserts `54d05ebf…`; the Q9 gate asserts the corrected-Q10
compiler `3837508e…`, and so on down the 16-entry `SOURCE_CLOSURE.sha256`,
whose entries agree with every in-code pin, with both V-case freezes, and
with the parent `FREEZE_RESULT.txt` (`compiler 54d05ebf…`).  The rc-0 AWS
run therefore attests byte identity of the whole chain on the box; none of
it could be recomputed here.  V1's own source freeze pins the parent result
freeze `97755c63…`, closing that loop textually.

**What V1 and V2 failed, exactly.**  V1 computes the same `A22,b22` and then
executes `assert y_witness is not None` (compile_witness.py line 171).
Because the system is incompatible (§3), `rref` returns `witness=None` and
V1 necessarily dies there with `AssertionError`, before any output: it
"asserted compatibility and correctly failed closed on an incompatibility."
V2 introduces the left-null certificate emitter; its 13-row call
(`rref_certificate(A22[:13], b22[:13])`, line 79) takes the compatible
branch and executes line 74,
`assert transition_rows(q9_vector, witness) == [0] * rows` with `rows=13` —
comparing the unsliced 22-entry residual list to a 13-entry zero list, which
is `False` for shape reasons alone.  V2 therefore necessarily dies inside
the 13-row call, before the 22-row call and before any output.  Both
failures are *forced* by the pinned sources plus the mathematics verified
below, so the two negative controls are sound even though their run bytes
are not in the repository (finding 1); neither is used as mathematical
evidence, exactly as `RESULT_README.md` states.

**V3's delta.**  Line-by-line comparison of `compile_witness_v3.py` against
`compile_witness_v2.py`: the files differ only in the docstring, the
pin block (path/name/SHA of the consumed predecessor, scope `__name__`),
and line 74, which becomes
`assert transition_rows(q9_vector, witness)[:rows] == [0] * rows`.  The
slice `[:13]` is exactly the accepted block (3+4+6=13 rows precede `G_8`),
so the corrected check is the meaningful positive substitution check for
the partial solve.  Everything defining the mathematics —
`transition_rows`, `matrix_and_rhs`, `q9_vector`, `y_names` — is *pulled
from the exec'd, hash-asserted V2→V1 prefix*, so V3 changes no mathematics
besides that one check.  The buggy V2 checker exec'd into the prefix scope
is discarded (V3 pulls only the four names).  The claim "consumes V2's
definition prefix byte-for-byte" is literally enforced by the SHA assert
plus the unique-marker split.

## 2. Independent derivation of the 22 rows

**Master identity.**  Re-derived here by direct expansion of
`P_xQ_y−P_yQ_x−1` with `P=x−x³+3U+9C+27W`, `Q=y+3V+9D+27Z`:

```text
det J−1 = 3L + 9(K+C_x+D_y) + 27(M+W_x+Z_y) + 81(N+T) + 243S + 729{W,Z},
L=A+V_y, A=U_x−x², K=AV_y−U_yV_x,
M=AD_y+C_xV_y−U_yD_x−C_yV_x, N={C,D}, T=AZ_y+W_xV_y−U_yZ_x−W_yV_x,
```

every sign checked termwise.  Successive division by 3 gives the exact
band tower `L≡0`, `E=L/3+K+C_x+D_y≡0`, `F=E/3+M+W_x+Z_y≡0`,
`G=F/3+N+T≡0 (mod 3)`, degree by degree; each imposed row is therefore a
*necessary* condition of `det J=1` under the frozen canonical
representatives, so imposing the subset `{E_2,F_3,F_5,G_8}` is conservative
for an incompatibility verdict (unimposed bands such as `F_4`, which awaits
the `W5/Z5` layer, cannot rescue it).  The report's (1) and the code agree
with this tower exactly, including the carries `E_3/3`, `E_5/3`, `F_8/3`.

**All 22 rows at the charged point, from first principles.**  With
`C=2x⁵+C3`, `D=D3`, `W=W4+W6+2x⁷`, `Z=Z4+Z6`:

- `E = −x⁴+(2x⁵+C3)_x+(D3)_y = 9x⁴+(C3)_x+(D3)_y`, so `E` has only degrees
  4 and 2 — for *every* value of the 32 variables.  Hence `E_3=E_5=E_8={}`
  identically (the degree-8 emptiness is also runtime-asserted), and every
  `E`-carry in the four bands is a division of the empty polynomial.
- `M = −x²(D3)_y+10x⁶+x²(C3)_x−2xy(C3)_y` has only degrees 4 and 6, so
  `M_3=M_5=M_8={}` identically; `F_8=E_8/3+M_8+(W_x+Z_y)_8=0` (the last
  term by typed support: the top W/Z layer is degree 7, so its divergence
  caps at degree 6).
- `N_8={C,D}_8={}` identically: the available bracket pairs are
  `{2x⁵,D3}` (degree 6) and `{C3,D3}` (degree 4); a degree-8 bracket would
  need `{C3,D7}` or `{C7,D3}`, and `Cbase₇=Dbase₇=0` at this predecessor.
- `T_8`: state factors `A,v_y,v_x,u_y` are all pure degree 2 here, so
  degree 8 requires a degree-6 W/Z derivative, i.e. the `W7/Z7` layer of
  the *Q9 assignment*, never the 32 unknowns (whose W/Z derivatives cap at
  degree 5).  With `W7=2x⁷`, `Z7=0`:
  `T_8=(W7)_x·v_y=14x⁶·x²=14x⁸`.

So `G_8=0+0+14x⁸`, i.e. the nine obstruction rows are constant in the 32
variables and equal `(0,…,0,14)≡(0,…,0,2)` on the monomials
`(0,8),…,(8,0)`.  Since `row(P,8)[i]` is the `(i,8−i)` coefficient, the
nonzero entry sits at within-block index 8 = monomial `x⁸`, global row
`13+8=21` in zero-based ordering — exactly the report's "`x⁸` row of
`G_8`", with `b[21]=14 mod 3=2`.

The accepted 13 rows are homogeneous-linear with zero RHS:

```text
row  monomial  equation (mod 3)          row  monomial  equation (mod 3)
 0   y²        c3_1                        7   y⁵        w6_1
 1   xy        2c3_2+2d3_1                 8   xy⁴       2w6_2+2z6_1
 2   x²        d3_2                        9   x²y³      z6_2
 3   y³        w4_1+z4_0                  10   x³y²      w6_4
 4   xy²       2w4_2                      11   x⁴y       2w6_5+2z6_4
 5   x²y       2z4_2                      12   x⁵        z6_5
 6   x³        w4_4+z4_3                  13–21  G_8     all-zero rows, b=(0,…,0,2)
```

(coefficients `4≡1`, `5≡2`, `3≡0`, `6≡0` reduced; each variable appears in
at most one row).  No omitted layer can reach the imposed rows at this
point: `C1/D1` enter `E_0` and (with only degree-2 state factors) `M_2`,
never `E_2/F_3/F_5/G_8`; W/Z layers of degree ∉{4,6,7} enter `F_1/F_2/F_4`
and `T_{3,4,6}` only; a degree-9 W/Z layer would be needed for
`(W_x+Z_y)_8` and does not exist in the D=7 typed support; the six
degree-six Frobenius spectators and all Frobenius variables are zero at
this state, so every single/double-Frobenius divided term of the Q11/Q10
erratum class vanishes — and more strongly, every dividend in these 22 rows
is the empty polynomial, so *no divided summand can be missing*: the
erratum class of error is structurally impossible here.  Representative
dependence exists in principle (a different integer lift of the same mod-3
state can shift `L/3` into `E_2` and carries into `G_8`), but the license
is explicitly internal to the frozen canonical convention ("one canonical
Q9 coefficient assignment"), the same convention-internality the parent
review already recorded; within the convention the rows above are exact.

## 3. The linear/Kuranishi certificate

**Affinity is a theorem here, not just a 34-point check.**  `E,M,N_8,T` are
Z-linear in the layer polynomials, which are Z-affine in the 32 values; the
only potentially bilinear term, the bracket of new layers `{C3,D3}`, has
degree 4 and cannot reach `N_8`.  Because every divided part
(`E_3,E_5,M_8`) is identically empty, no divisibility side condition
perturbs affinity at any of the 3^32 points, so the finite-difference
matrix (`f(e_i)−f(0)`) is exact and the asserted all-ones identity
`f(1)=b+Σ_iA_i` is a genuine negative control for cross terms (it ran, rc
0).

**Ranks.**  Rows 0–12 above have pairwise disjoint supports, so
`rank₁₃=13` and, with zero RHS, the pair is `(13,13)`; the accepted-image
kernel has dimension `32−13=19` (free: `c3_0,c3_3,d3_0,d3_3`, one of
`{c3_2,d3_1}`, `w4_0,w4_3,z4_1,z4_4`, one each of `{w4_1,z4_0}`,
`{w4_4,z4_3}`, `w6_0,w6_3,w6_6,z6_0,z6_3,z6_6`, one each of `{w6_2,z6_1}`,
`{w6_5,z6_4}` — 19).  Rows 13–21 are zero rows, so `rank₂₂=13`; row 21 has
zero coefficients and RHS `2≠0`, so the augmented rank is 14: pair
`(13,14)`.  The Kuranishi map on the 19-dimensional kernel is the G_8 block
restricted to that kernel; its matrix part is identically zero, so its rank
is `rank₂₂−rank₁₃=0` and the cokernel dimension is `9−0=9`.  All five
numbers of the report's (2) are hence re-proven by hand.

**Certificate.**  `λ=e_21` satisfies `λA=0` (row 21 is the zero row) and
`λb=b[21]=2` in `F₃` — re-derived here as `14 mod 3` from `T_8=14x⁸`, with
`14=2·7` (witness value 2, exponent 7 from `∂_x x⁷`) and the `+` sign of
`W_xV_y` in `T` traced to the master identity.  In the producer, the
certificate is not merely read off the RREF transform: lines 63–67 verify
`λA≡0` column-by-column against the original matrix, `λb≠0`, and
consistency with the reduced augmented entry; the emitted support `[21]`
lies in the final nine rows, which the V2 preregistration correctly
interprets as a genuine post-image Q8 obstruction (support in the first 13
would instead have flagged a reconstruction error).  The plus-one control
replaces `b[21]←b[21]+1` and re-pairs directly: `2+1≡0`, which checks
orientation exactly (it would give `1`, not `0`, if `λ₂₁` were 2).  Row 21
is the zero-based `x⁸` coefficient row of `G_8`, as claimed.  Within the
RREF machinery the nine zero rows can only be permuted, never combined, so
`e_21` is also the transform row the algorithm must surface; uniqueness of
the bad row follows from `b[13..20]=0`.

**Emitted values.**  Every stdout quantity matches this derivation:
`source_shapes 23 32 3 4 6 9 32`, rank pair lines, kernel 19, Kuranishi
rank 0, cokernel 9, `left_null_certificate=[0]*21+[1]`, support `[21]`,
residual 2, `plus_one_control (21, 0)`, `q8_witness None`, verdict
INCOMPATIBLE.  (The `source_shapes`/`source_row_identities` lines are
hard-coded labels, not computed checks; the identities behind them are
verified above.)  The matrix/RHS hash preimages are fully pinned by the
table in §2 — `bytes` of the 704 entries row-major and of `(0,…,0,2)` — and
the staged `/tmp` script recomputes both digests against the frozen values;
it was not executed here (no shell).

## 4. Custody, controls, and shell-only residuals

Verified textually: the result manifest's eight entries against the files
read; `OUTPUTS.sha256` (box-side) against `RESULT_MANIFEST.sha256`
(repo-side) — stdout/stderr/time/meta hashes agree pairwise;
`run.meta` rc/UTC window against `replay.time` (`Exit status: 0`,
0:10.81, 20,688 KiB) and the report; the runner manifest's four entries
including the V3 compiler SHA `e662c331…` consistent with
`FREEZE_SOURCE.txt` and `SOURCE_CLOSURE.sha256`; the 16-entry source
closure against every in-code pin; `SOURCE_PACKAGE_FILES.txt` covering the
closure plus case text; the parent-side custody of the witness bytes
(`shard_00.out` hash `c102d768…` in `REMOTE_RESULTS_MANIFEST.sha256`, whose
own hash is pinned in the parent freeze).  The ledger (`notes.md` 02:02Z)
records the same rank pairs, certificate, and "no fibre death" scope.

Shell-only residual conditions, none re-checkable here: (i) every SHA-256
recomputation (closure, manifests, payloads, archives, report,
`FREEZE_RESULT.txt` self-hash `7dde1c07…`); (ii) the actual V3 execution
(rc, stdout bytes) — trusted as transported; (iii) the V1/V2 failure runs,
which exist in the repository only as tags
(`as_q9_q8_kuranishi_20260825T015219Z`, `…_v2_20260825T015608Z`) in freeze
prose — their assertion-failure *modes*, however, are forced by the pinned
sources plus §2–3, so their control value does not rest on transported
bytes; (iv) equality of repo bytes with the AWS source archive
(`5a253765…`).  Textual consistency and independently checked mathematics
were kept distinct throughout: everything in §§1–3 except execution and
hashing is independent hand mathematics.

## 5. Scope

The strongest licensed conclusion is exactly: incompatibility of the first
canonical Q9 coefficient assignment — this one predecessor state, this one
Q9 vector, under the frozen canonical-integer-representative convention.
The report says precisely this and disclaims fibre, predecessor, rank
class, branch, and lift kills.  This review *proves* the disclaimer is
necessary, not merely cautious: over the same predecessor's 19-dimensional
Q9 fibre the transition matrix is unchanged and the nine obstruction values
are `w7_{k−1}+k·z7_{k−2} (mod 3)`, `k=0..8` (hand formula, reproducing
`b[21]=w7_7+2z7_6=2` at the witness).  The explicit fibre point `w7_7=1,
z7_6=1`, all other restored coordinates zero, satisfies all 23 Q9 rows
(`10+7+1=18≡0`) and gives `T_8=(7−1)x⁸=6x⁸≡0`, hence `b=0`: the full
22-row system is compatible there with witness `y=0`.  So any inference
from (2)–(3) to the fibre, the predecessor, its rank class, the D7 branch,
a recurrence, all-depth lifting, characteristic-zero algebraization, a
counterexample, or JC2 would be *false*, and none is made.  Combining the
hand formulas with the seven `F_6` fibre ties, the next gate's Kuranishi
zero locus over this fibre is predicted to be a nonempty affine subspace
(six independent conditions beyond the fibre: `w7_0=z7_0=w7_3=z7_3=w7_6=0`,
`z7_6=1`; dimension 13) — a review-derived, unexecuted prediction recorded
for the preregistered discriminator, not a licensed claim.  The "16–19 free
coordinates" phrasing matches the parent census (fibre dimensions
19/17/16).  No overreach was found in the report, freezes, README,
preregistrations, or ledger.

## 6. Findings

No false identity, missing term, or missing hypothesis was found.  The
smallest findings, none affecting the verdict:

1. (Custody/wording) "V1 and V2 remain frozen assertion-failure controls"
   overstates transported custody: only their *sources* and failure *tags*
   are frozen; no stderr/rc/meta bytes of either failed run are in the
   repository.  Mitigated because both failure modes are mathematically
   forced by the pinned sources (§1), and `RESULT_README.md` correctly
   assigns them no evidential weight.
2. (Custody, disclosed) The charged result-freeze self-hash `7dde1c07…` is
   corroborated only by the review charge; nothing in the repository pins
   it yet (the parent's analogous hash became corroborated when its
   successor pinned it — the same should happen here on the next
   promotion).
3. (Wording, minor) The degree-8 instantiation `F_8=M_8` rests on the
   runtime assert `E_8={}` plus the support theorem `(W_x+Z_y)_8=0` (no
   degree-9 W/Z layer); the latter is carried by the typed support, not by
   a runtime check — proven here by hand, same class as the parent
   review's spectator finding.
4. (Precision, favorable) At this point every division in display (1) is a
   division of the empty polynomial, so "all divisions asserted over the
   integers" is true but vacuous, and the whole obstruction reduces to the
   undivided term `T_8=14x⁸≡2x⁸`; this is why the erratum-class
   missing-divided-term risk is structurally nil here.

## Promotable sentence

For the single frozen first canonical Q9 witness of the AS F-only `D=7`
vertical branch — predecessor `c5_5=2` with all other 29 accepted-digit
coordinates zero, Q9 assignment `w7_7=2` with all other 31 restored
coordinates zero, under the frozen canonical-integer-representative
convention — the 22-row transition system `E_2=0`,
`F_3=E_3/3+M_3+(W_4)_x+(Z_4)_y=0`, `F_5=E_5/3+M_5+(W_6)_x+(Z_6)_y=0`,
`G_8=F_8/3+{C,D}_8+T_8≡0 (mod 3)` in the 32 restored coefficients
`(C_3,D_3,W_4,Z_4,W_6,Z_6)` is incompatible, with accepted/full rank pairs
`(13,13)/(13,14)`, 19-dimensional accepted-image kernel, Kuranishi rank 0
and cokernel dimension 9, certified by the left-null vector `e_21` — the
`x⁸` row of `G_8`, whose entire content is the undivided term
`T_8=14x⁸≡2x⁸` — pairing to `2≠0` with a verified plus-one orientation
control; this licenses nothing beyond that single canonical assignment: in
particular not its 19-dimensional Q9 affine fibre (which provably contains
Q8-unobstructed points, e.g. `w7_7=1, z7_6=1`), not its predecessor or rank
class, and no recurrence, all-depth lifting, characteristic-zero,
counterexample, or JC2 statement.

Next discriminator, as preregistered: the induced Kuranishi zero locus over
the whole Q9 affine fibre (predicted here, by hand, to be a nonempty
13-dimensional affine subspace at this predecessor), together with the
cross-rank Bockstein-retention test.

CONFIRMED
