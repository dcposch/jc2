# Hostile review: V24 exact grade-seven two-cokernel compatibility block

Date: 2026-08-27
Reviewer: Claude Opus 5, adversarial algebra and custody lane, fail-closed
Charged object:

- report `cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/RESULT_V24.md`
- preregistration, compiler and runner in the same case directory
- frozen harvest `.../aws_r6b_pass/`
- exact compatibility artifact
  `4f4c2bac49270fdd220e2333fbf82ba8bd4cc507cff90ea3eb8c2bf8c614ddd2`
- exact left-basis
  `6c857c91220965ee25d4483b122277c174a0dc0b9f740311fce02390b92893e1`
- exact inhomogeneous vector
  `dc7696e1c1552533418eba1f91e14227ef8663aeded38b111d3295d1afb3f289`
- RESULT JSON
  `22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b`
- evidence manifest
  `8fedd7c3ea3c693679b1fa96a9ebce849c0455c44021cb86ad699bc8592b7c60`

## Verdict

**PASS at exactly the allowed narrow scope, with one material finding
against the modular diagnostic, two custody defects and three hygiene
defects.**

Everything in the exact block was rebuilt from the frozen sources by an
independent implementation on AWS and agrees with the producer
coefficientwise: the `7 x 7` newest-coefficient matrix, the 226-term
witness minor, all fourteen left-cokernel entries, all seven
column-annihilation identities per covector, the seven inhomogeneous
rows, all thirty-five prior grade-2..6 rows, and both compatibility
polynomials at 110,117 and 83,298 terms. The confirmed statement is:

> Let `A(x)` be the literal grade-seven newest-coefficient matrix of the
> seven normalized rows plus `Lambda^2`-weighted `K10` loads, in the
> newest variables `(d0_6,...,d5_6,k10_3)`, after the honest boundary
> `k6_0=0`, with `C6` normalized to `1` and valuation-one source
> `d_i = sum_{n>=1} d_i_n Lambda^n`. Let `W = det A[0..4; 0,1,2,3,6]`
> (226 terms, nonzero) and let `b` be the grade-seven inhomogeneous
> vector. Over `Q[x][1/W]`, and hence at every point of `D(W)` and a
> fortiori of `D(k10_0*W)`, the left kernel of `A` is free of rank two
> with the two frozen Cramer covectors `L1,L2` as a basis, and
> `A y + b = 0` is solvable if and only if `C6 = L1.b = 0` and
> `C7 = L2.b = 0`.

**Material finding, against the producer.** The producer left open
whether the localized prior ideal used for its modular normal forms is
proper. It is not. I recomputed the standard basis of the producer's own
frozen ideal and obtained the **unit ideal** over `F_65521`:
`size(G)=1`, `G[1]=1`, `reduce(1,G)=0`, `dim(G)=-1`. The two zero normal
forms are therefore **vacuous** and carry no information: modulo the unit
ideal every polynomial reduces to zero. The collapse is not an artifact
of the prime — it reproduces identically at `32003`, `1000003` and
`2147483629`. This does not break the PASS, because
the allowed adjudication excludes modular membership and chart
nonemptiness, but every downstream consumer must treat
`modular_reduction_status: F65521_C6_ZERO_1_C7_ZERO_1` in the charged
`RESULT.json` as **withdrawn**.

The PASS certifies nothing about `W=0`, chart nonemptiness, modular or
exact ideal membership, grades eight through nineteen, a full jet or arc,
K00 closure incidence, order two, maximum twelve, or JC2.

---

## 1. Custody: rehash of every charged input and evidence entry

All six charged SHA-256 values reproduce byte-for-byte from the working
tree. The producer's own preregistration, compiler and runner hashes
quoted in `RESULT_V24.md` also reproduce.

| object | SHA-256 (charged and recomputed) | verdict |
| --- | --- | --- |
| `aws_r6b_pass/output/GRADE7_COMPATIBILITY_C6_C7.txt` | `4f4c2bac49270fdd220e2333fbf82ba8bd4cc507cff90ea3eb8c2bf8c614ddd2` | recomputed identical |
| `aws_r6b_pass/output/LEFT_COKERNEL_BASIS.txt` | `6c857c91220965ee25d4483b122277c174a0dc0b9f740311fce02390b92893e1` | recomputed identical |
| `aws_r6b_pass/output/GRADE7_INHOMOGENEOUS_B.txt` | `dc7696e1c1552533418eba1f91e14227ef8663aeded38b111d3295d1afb3f289` | recomputed identical |
| `aws_r6b_pass/output/RESULT.json` | `22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b` | recomputed identical |
| `aws_r6b_pass/EVIDENCE.sha256` | `8fedd7c3ea3c693679b1fa96a9ebce849c0455c44021cb86ad699bc8592b7c60` | recomputed identical |
| `PREREGISTRATION.md` | `3e48bb009c82a1a988aca5f17a65f290f916e83a3fc1773252ef9b5b59227e0c` | recomputed identical |
| `compile_grade7_cokernel_v24.py` | `1652cf3f2cefff9490062aade6e4c5be1c20b82cbefa01a7ef8a039530c39022` | recomputed identical |
| `run_grade7_cokernel_v24_aws.sh` | `5fbcb8ebe22fb11701000b367e84c22777feb2536bf7c16a6a7573bc538a7829` | recomputed identical |
| `SOURCE_FREEZE.sha256` | `48e38dfb3ace6301af078b1e2ccd7c3d59a898fbe091c13567f371d0884eb3f9` | recomputed identical |

**Source freeze: 11 entries, 11 verified.** Contents are the case's own
preregistration, compiler and runner, plus V21 `prelude_Q.sing` and
`load_K10.txt`, V20R2 `LITERAL_140_EQUATION_DAG.json` and
`SOURCE_COLUMNS.json`, V23 `GRADE7_NEWEST_MATRIX.txt`,
`GENERIC_RANK_WITNESS_MINOR.txt` and `RESULT.json`, and V22
`F10_QUARTIC.txt`. The manifest does not list itself, so there is no
self-listing paradox; the runner independently `sha256sum -c`s it before
export and `freeze_check.stdout` shows eleven `OK` lines. The compiler
separately pins nine of those eleven by literal hash in `EXPECTED` and
raises on mismatch. The two not pinned inside the compiler (the runner
itself and `SOURCE_FREEZE.sha256`) are covered by the runner's own check.

**Endpoint evidence: 14 entries, 14 verified** after remapping the
AWS-absolute prefix `/home/ubuntu/jobs/<tag>/` onto the local harvest.
The producer's claim of "14/14" is correct. The manifest does not list
itself. It covers `output/` (11 files) and `run/` (3 files) exhaustively:
no file in either directory is unlisted, and no listed file is missing.

**Custody defect C-1 (minor).** The manifest is generated by
`find "$aws_job/output" "$aws_job/run"`, so four harvest-root files are
outside it and are not tamper-evident within the sealed set:
`freeze_check.stdout` (`3429fe88...c1e7`), `launch_registration.txt`
(`b802a2d3...b035d`), and the two empty `outer.stdout`/`outer.stderr`
(`e3b0c442...b855`). `freeze_check.stdout` is the transcript proving the
inputs were frozen, and `launch_registration.txt` carries host, start/end
UTC and `rc`; both belong inside the manifest. Recorded, not blocking:
their contents are consistent with `run/compiler.stderr` and I re-derived
the freeze independently.

**Custody defect C-2 (minor).** `RESULT_V24.md` itself
(`6ed1163e56518e317d7fbb49eb9d107dc5b67e626830427a0a5d336d05f71df9`) is
pinned nowhere: it is not in the source freeze, not in the evidence
manifest, and not hashed inside `RESULT.json`. The report is the object a
reader consumes, so it should be hash-pinned by whatever ledger cites it.

Runner and telemetry are consistent: `/usr/bin/time -v` reports
5:01.33 wall, 300.34 user + 0.94 system seconds, 1,840,916 KiB maximum
RSS, `Swaps: 0`, `Exit status: 0`; `launch_registration.txt` gives
`start_utc=13:29:06Z`, `end_utc=13:34:08Z`, `rc=0`; `FINAL.validation`
gives `engine_rc=0` and the validator string. The report's quoted runtime
matches exactly.

The runner's `grep -Fqx 'K00_V24_PRODUCER=PASS'` gate is a
producer-authored banner, so I checked the failure paths rather than
trusting it: every substantive check in `main()` calls `fail()`, which
raises `RuntimeError`, which makes `python3` exit nonzero, which makes
the runner `exit "$rc"` before the grep. The only swallowed exception is
`subprocess.TimeoutExpired` around the modular reduction, which is
diagnostic by design. So the banner is not reachable with a failed exact
check. See defect H-1 for the residual hygiene problem.

## 2. Independent reconstruction of the rows, loads and grade-seven system

I did not call, import, or re-run the producer's compiler. I wrote a
separate program with a different tokenizer and recursive-descent parser
(no `python ast`), a different monomial encoding (packed 10-bit integer
fields), a different variable ordering (grade-major, not source-major),
and a different derivation of the matrix. Run on AWS EC2 box01
(`ip-172-30-0-237`, `sys_vendor = Amazon EC2`, 64 vCPU, 991 GiB),
job `~/jobs/v24_grade7_cokernel_hostile_review_20260827T135606Z_box01`,
script SHA-256
`3d71bdee1244233bd4de5e3cdf8639876052d798546dc1139ccb860826bad1fa`,
19.13 user seconds, 270,632 KiB RSS, exit 0. Upload integrity was
confirmed by rehashing all nine inputs and five producer artifacts on the
remote host against the charged values.

Normalized rows `r1..r7` were read from the frozen `prelude_Q.sing`,
which carries `C6` already normalized to the literal `(1)` and the
coordinate map `C0=(1+d0)/256`, `C1=d1`, `C2=(1+d2)/16`, `C3=d3`,
`C4=(3+d4)/8`, `C5=d5` (confirmed against the DAG's
`normalized_coordinate_map`). Loads came from the frozen `load_K10.txt`.
No raw tail row or literal K00 evaluation was substituted.

**Matrix derivation (different route).** Instead of expanding a
40-variable series and extracting an affine part, I substituted
`d_j -> x_j*Lambda + y_j*Lambda^6` into the row expression trees,
truncated at `Lambda^8`, took the `Lambda^7` coefficient, and verified it
is exactly linear in `y`; the coefficient of `y_j` is column `j`. Column
6 was obtained as `[Lambda^2] L_i(d -> x*Lambda)`, i.e. the degree-two
part of the K10 load. This yields a `7 x 7` matrix of linear forms in
columns 0..5 and quadratic forms in column 6.

- **Result: byte-equivalent to V23.** `A(x)` agrees with the frozen
  `GRADE7_NEWEST_MATRIX.txt` coefficientwise in all 49 entries.
  Term counts per entry:

  ```text
  [[2, 2, 3, 3, 3, 3,  6],
   [2, 3, 3, 3, 3, 3,  9],
   [3, 3, 3, 3, 3, 3,  8],
   [3, 3, 3, 3, 3, 3, 11],
   [3, 3, 3, 3, 2, 2,  9],
   [0, 0, 0, 0, 0, 0, 12],
   [2, 2, 2, 2, 2, 2,  9]]
  ```

  Row index 5 is supported on column 6 alone. This sparsity is load
  bearing later and is not remarked on anywhere in the charged material.

**Inhomogeneous vector and prior rows.** With
`d_j = sum_{n=1..5} d_{j,n} Lambda^n` and
`k10 = k10_0 + k10_1 Lambda + k10_2 Lambda^2` weighted by `Lambda^2`
(the newest variables set to zero), I evaluated
`E_i = r_i(d) + Lambda^2 k10 L_i(d)` truncated at `Lambda^8`.

- `b_i = [Lambda^7] E_i` has term counts
  `[175, 241, 327, 424, 538, 634, 795]`, matching
  `grade7_b_term_counts`, and all seven rows equal the frozen
  `GRADE7_INHOMOGENEOUS_B.txt` coefficientwise.
- A second, independent consistency check: `b` restricted to
  `d_{j,n}=0` for `n>=2` equals the `y`-free part of the `(x,y)` route
  above. Two different computations, same answer.
- All 35 grade-2..6 rows equal the frozen
  `PRIOR_GRADE2_TO6_EQUATIONS.txt`; exactly 34 are nonzero, matching
  `prior_nonzero_equations`. The single identically-zero row is
  `P_r6_g2`, which the charged material does not name.
- Grades 0 and 1 vanish identically for all seven rows, so restricting to
  grades 2..7 loses nothing.

**Independent replay of the frozen V20R2 literal DAG.** I wrote my own
DAG evaluator over the 309,343-node frozen graph and checked, for every
row and every grade 2..6, that my prior row equals the DAG root, and for
grade 7 that `A(x)*(d_*_6, k10_3) + b` equals the DAG root. Tested at
seven fixtures (the producer's four seeds plus three of my own, drawn
from a different hash namespace and using full-range residues rather than
`{-5..5}`) times three primes (`65521`, `2^31-1`, `2^61-1`), plus exact
rational arithmetic at the producer's two `Q` fixtures. All 7 x 6 = 42
coefficients match in every case. This confirms the producer's
`LITERAL_DAG_REPLAY.json` claim of 42 coefficients x 4 fixtures and
extends it.

**Sensitivity census: the 40-variable truncation is a theorem, not an
assumption.** This is the check I expected to break the producer. The
honest V20R2 source has 169 columns, including `d_*_7 .. d_*_19`,
`k10_4..k10_17`, `k6_1..k6_13`, `k2_1..k2_9`, `mu2_*`, `mu4_*`, `mu6_1`
and `Jdet_0`, all marked `FREE`. If any of those reached grade seven, the
producer's newest-variable list would be wrong and the whole compatibility
block would describe the wrong system. I perturbed each of the 169
columns one at a time and recorded which grade-0..7 roots move. Exactly

```text
d0_1..d5_1, ..., d0_6..d5_6, k10_0, k10_1, k10_2, k10_3
```

move anything at grades 0..7, and nothing else does. In particular
`d_*_7` are inert at grade seven because every `r_i` has identically
vanishing degree-one part (verified symbolically: grades 0 and 1 are
zero), and `k10_4`, `k10_5` are inert because the K10 loads have minimal
`d`-degree two, so `k10_n` cannot reach below grade `n+4`. The producer's
`NEW_VARS` choice is correct.

**The `k6_0=0` boundary is real and correctly imposed.** `k6_0` is one of
the five `FIXED_ZERO_BEFORE_SOLVE` columns and is not even a node of the
frozen DAG (`boundary_restriction_order` substitutes the five zero
constants before anything else), so it cannot be probed by perturbation.
I therefore rebuilt its grade-seven column independently from the frozen
`load_K6.txt`: the K6 multiplier carries weight `Lambda^6`, the K6 loads
have minimal `d`-degrees `[1,1,1,2,1,2,1]`, so `k6_0` contributes exactly
`[Lambda^1] L^{K6}_i` at grade seven and `k6_1` cannot reach below grade
eight. The resulting column reproduces V23's
`FORBIDDEN_K6_0_COLUMN.txt` (`3e5717ae...c7200`) exactly, with five
nonzero rows and zero-based rows 3 and 5 vanishing. **The column is nonzero**, so
`k6_0=0` is a load-bearing boundary condition and not a cosmetic one, and
V24's omission of the entire K6 block from `phi` is exactly its
imposition. Nothing else in the K6, K2, `mu` or `Jdet` families can reach
grade seven.

## 3. The rank-five witness, verified without trusting a displayed determinant

`W = det A[rows 0,1,2,3,4; columns 0,1,2,3,6]` was recomputed by Laplace
expansion with recursive complementary minors, **not** by the producer's
`5! = 120`-term Leibniz permutation sum, and then a second time by
expansion along the opposite row. The two expansions agree, the result
equals the frozen `GENERIC_RANK_WITNESS_MINOR.txt` coefficientwise, it has
226 terms as reported, and it is nonzero.

Invertibility of the chosen `5 x 5` block on `D(W)` is immediate: `W` is
its determinant and `W` is a unit there. That gives `rank A >= 5` at every
point of `D(W)`.

The upper bound was **not** taken from a displayed determinant. V23's
`GRADE7_DETERMINANT.txt` reads `0`, and I confirm `det A = 0` identically
by my own expansion, but a vanishing `7 x 7` determinant only gives
`rank <= 6`. I therefore computed **all 49 six-by-six minors of `A` over
`Q[x]` and every one vanishes identically.** That gives `rank A <= 5` at
every point of affine space, independently of `W`. Combined with the
lower bound, `rank A = 5` exactly on `D(W)`.

Independently, the two exact left-kernel identities of section 4 give the
same upper bound on `D(W)`: `L1, L2` are polynomial left-kernel vectors
whose `(5,6)` coordinate block is `W*I_2`, hence independent wherever
`W != 0`, hence the left kernel has dimension `>= 2` and the rank is
`<= 5`. Both routes were checked; neither depends on the other.

Minor census, recorded because the pivot choice is load bearing: 90 of
the 441 `5 x 5` minors of `A` are nonzero. Of the seven column sets I
probed on rows `0..4`, four are identically zero (`(0,1,2,3,4)`,
`(0,1,2,3,5)`, `(0,1,2,4,6)`, `(0,2,3,4,6)`) and three are nonzero with
226 terms each (`(0,1,2,3,6)`, `(0,1,3,4,6)`, `(1,2,3,4,6)`). The
producer's pivot set is a valid choice and several nearby ones are not,
which is why the mutation analysis in section 4 needed care.

## 4. The two Cramer covectors, verified entry by entry

I re-derived the covectors from scratch, using Laplace expansion along
the replaced row rather than the producer's determinant routine. For
`e in {5,6}`, with `u = A[e; 0,1,2,3,6]` and `P = A[0..4; 0,1,2,3,6]`:

```text
L_e[e]  = W
L_e[p]  = -det(P with row p replaced by u),  p = 0,1,2,3,4
L_e[f]  = 0  for the other extra row f
```

- All fourteen entries reproduce `LEFT_COKERNEL_BASIS.txt`
  coefficientwise. Term counts:
  `L1 = [236, 0, 236, 0, 236, 226, 0]`, `L2 = [226, 0, 226, 0, 226, 0, 226]`.
  Zero-based entries 1 and 3 vanish in both covectors, a structural fact
  the charged material does not record. (Indices throughout this review
  are zero-based, matching `pivot_rows_zero_based` in the charged JSON.)
- All seven column-annihilation identities were verified **coefficientwise
  over `Q[x]`** for each covector: `sum_r L_e[r] * A[r][c]` is the empty
  polynomial for every `c = 0..6`, not merely numerically small. The two
  nontrivial ones are `c = 4` and `c = 5`, the columns outside the pivot
  set; those are the identities that actually encode `rank <= 5`, and
  they hold exactly.
- The `(5,6)` coordinate block is exactly `W*I_2`.

**Why they span the complete left kernel after localizing at `W`.** Work
over `R_W = Q[x][1/W]`. Let `lambda` be any left-kernel vector in
`R_W^7`. Set `lambda' = lambda - (lambda_5/W) L1 - (lambda_6/W) L2`,
which is legitimate because `1/W in R_W`. By the `W*I_2` block, `lambda'`
has vanishing coordinates 5 and 6, so it is supported on rows `0..4`, and
`lambda' A[:, {0,1,2,3,6}] = 0` reads `lambda'|_{0..4} P = 0` with `P`
invertible over `R_W`; hence `lambda'|_{0..4} = 0` and
`lambda = (lambda_5/W) L1 + (lambda_6/W) L2`. Independence is again the
`W*I_2` block. So the left kernel is free of rank two with basis
`{L1, L2}`, and the same argument at any point of `D(W)` over any field
gives a two-dimensional left null space. I confirmed this numerically as
well: at sampled points of `D(W)` over `F_{2^61-1}`, `rank A = 5`, the
left null space has dimension 2, and `L1, L2` evaluate to an independent
spanning pair.

**Mutation controls.** I ran seventeen live mutations. All eight
single-entry sign flips on nonzero entries break at least one column
identity; so do a transposition of two Cramer entries of `L1`, doubling
one entry of `L2`, and replacing one Cramer entry by another. Of six
alternate pivot-column-set constructions, three break the identities and
three do not. I ran the three down rather than reporting them as
failures: because row 5 is supported on column 6 alone, the Cramer
construction for `L1` uses only the `4 x 4` minors on columns
`{0,1,2,3}`, so pivot sets differing from `(0,1,2,3,6)` only in the last
slot **provably regenerate `L1` itself** — I verified the reconstructed
covectors are equal to `L1` entry by entry. They are therefore not
falsification controls at all, not counterexamples. The producer's own
mutation control is weaker than any of these: it flips the sign of the
first nonzero entry of `L1` only, and hardcodes
`left_kernel_sign_mutation_detected: true` rather than emitting the
computed flag (defect H-1).

## 5. Reconstruction of `b`, re-contraction, and the solvability criterion

Both compatibility polynomials were recomputed as `C = sum_r L_r b_r`
from my own `L` and my own `b`, then compared with the charged file.

- Term counts `110117` and `83298`, matching `compatibility_term_counts`.
- Coefficientwise equality with `GRADE7_COMPATIBILITY_C6_C7.txt`.
- Serialization-independent canonical hashes over sorted
  `(monomial, numerator/denominator)` triples, computed the same way from
  my reconstruction and from a separate deserialization of the charged
  file, agree:

  ```text
  C6  b847e57ead7eedaa57a2fbdc0a6d7911b9d1838c8968997a1a8126f8a03ff60c
  C7  f00ec12c3246fb6599ed754f040550396be0cc92656169797f31c1dba97d0cf7
  ```

  These are hashes of the mathematical content, not of the producer's
  byte layout, and are the right object to cite downstream.
- Both are nonzero, of total degree 12, and involve all 33 prior
  variables, including `k10_0`, `k10_1` and `k10_2`.

**Proof that vanishing is necessary and sufficient on `D(W)`, not an
assertion.** Fix a point `x` of `D(W)` over a field `k` and consider
`A(x) y = -b`.

*Necessity.* `L1, L2` are polynomial identities, so they evaluate to
left-kernel vectors at `x`. If `y` solves the system then
`C6 = L1.b = -L1.(A y) = 0` and likewise `C7 = 0`.

*Sufficiency.* Suppose `C6 = C7 = 0`. Put `y_4 = y_5 = 0` on the two
non-pivot columns and solve
`P (y_0,y_1,y_2,y_3,y_6)^T = -(b_0,...,b_4)^T`, which is possible because
`P` is invertible at `x`. Rows 0..4 are then satisfied. For row 5, the
`L1` identity rearranges to
`A[5,:] = sum_p (det_p / W) A[p,:]` with `det_p = -L1[p]`, so

```text
(A y + b)_5 = sum_p (det_p/W)(A y)_p + b_5
            = (1/W)( W b_5 - sum_p det_p b_p )
            = (L1.b)/W = C6/W = 0,
```

and symmetrically `(A y + b)_6 = C7/W = 0`. The same computation with
coefficients in `R_W` gives the module-level statement over `Q[x][1/W]`.
This is the Fredholm alternative, and it is exact here precisely because
the left kernel was shown to be *exactly* two-dimensional, which is where
`rank <= 5` (section 3) and completeness (section 4) are consumed.

**Two-sided numerical confirmation.** At sampled points of `D(W)` over
`F_{2^61-1}`: with the literal `b`, `(C6,C7) != 0` and the augmented
matrix `[A | -b]` has rank 6, so the system is genuinely unsolvable
there; and with a forced-solvable control `b' = -A y` for random `y`,
both contractions vanish and the augmented rank drops to 5. The criterion
fires in both directions, so it is not a one-sided tautology.

## 6. Modular normal forms: replayed, and the properness hole closed negatively

The producer correctly refused to consume its own modular result and
wrote that "it may be genuine membership or a vacuous reduction modulo
the unit ideal". I resolved it.

First I confirmed what the modular script actually consumes, since the
`.sing` file is generated text and not itself charged as mathematics.
Parsing its 12.6 MB `ideal P=` declaration: it has exactly 35 generators,
the first 34 are exactly my 34 nonzero prior grade-2..6 equations, the
35th is exactly the frozen V22 `F10` quartic at `d_*_1`, the localization
line is `zinv*k10_0*(W)-1` with exactly my independently computed 226-term
`W`, and the embedded `C6` and `C7` are exactly the frozen exact
polynomials. So the script is faithful to the charged algebra.

Then I re-ran it. Two runs, on AWS box01 with Singular 4.3.2:

**(a) Verbatim replay of the producer's frozen script.** Reproduces
`K00_V24_MOD_C6_ZERO=1`, `K00_V24_MOD_C7_ZERO=1`,
`K00_V24_MODULAR_REDUCTION=PASS`; the emitted `stdout` hashes to
`5de0fa4a4423cffa711808b5eb8f70ec6606d6c6bdb152ce72ae44d3e9cdaf94`,
which is **the charged `modular.stdout` evidence hash**, and both normal
form files hash to `9a271f2a...86aa`, the charged normal-form hash.
311.81 user seconds, 5:12 wall, 1,841,008 KiB RSS. The producer's modular
run is exactly reproducible.

**(b) Properness probe on the producer's own ring, ideal and
localization lines** (extracted after verifying the frozen script's
SHA-256, its 11-line census, and the exact form of lines 0..4):

```text
HR_ONE_NORMAL=0          reduce(1,G) = 0, so 1 is in G
HR_DIM=-1
HR_GB_SIZE=1
HR_GB_FIRST=1            G = (1)
HR_C6_NF_ZERO=1
HR_C7_NF_ZERO=1
HR_UNIT_CONTROL_ZERO=1   negative control fires as designed
HR_PROPER=0
```

295.70 user seconds, 4:56 wall, 1,841,332 KiB RSS.

**The localized prior ideal is the unit ideal over `F_65521`.** Hence
every polynomial whatsoever reduces to zero modulo it, and the producer's
two zero normal forms are vacuous. Concretely, over `F-bar_65521` there is
no point at which the 34 prior grade-2..6 equations and `F10` all vanish
while `k10_0 * W != 0`: the `F_65521` fibre of the charged chart is
empty. This is exactly the branch the producer's own registered but
unharvested V24R1 repair enumerates as
`F65521_LOCALIZED_PRIOR_IDEAL_IS_UNIT_NO_MEMBERSHIP_CONCLUSION`; the
repair's design is sound and this run establishes its outcome in advance.

**The collapse is not prime-specific.** I re-ran the same probe on the
producer's own ideal and localization at three further characteristics.
All four agree:

```text
p = 65521       reduce(1,G)=0   dim(G)=-1   size(G)=1   G[1]=1
p = 32003       reduce(1,G)=0   dim(G)=-1   size(G)=1
p = 1000003     reduce(1,G)=0   dim(G)=-1   size(G)=1
p = 2147483629  reduce(1,G)=0   dim(G)=-1   size(G)=1
```

Four independent good primes make bad reduction an implausible
explanation. This is still a modular statement, not a theorem over `Q`:
turning it into one needs an exact-`Q` standard basis or an explicit
certificate `1 = sum_i h_i g_i` over `Q`. No exact-`Q` membership or
emptiness is claimed here. But the evidence that the charged chart is
empty is now strong enough to reprioritize the campaign, see section 10.

**Consequence, and defect R-1.** The charged `RESULT.json` field
`"modular_reduction_status": "F65521_C6_ZERO_1_C7_ZERO_1"` reads, out of
context, as a positive modular result. The accompanying
`"modular_reduction_scope": "DIAGNOSTIC_ONLY_NO_Q_MEMBERSHIP_INFERENCE"`
warns against lifting it to `Q` but does not warn that it is vacuous even
over `F_65521`. `RESULT_V24.md` does carry the correct caveat. The JSON,
which is the machine-readable artifact, must be corrected or superseded
before anything downstream reads that field.

## 7. Type boundaries

- **`C6 = 1` normalization.** The frozen `prelude_Q.sing` carries the
  literal `(1)` in every slot where `C6` would appear, and the DAG's
  `normalized_coordinate_map` records `"C6": "1"`. Confirmed consistent.
  **Name collision, defect H-2:** the charged evidence file labels its
  two compatibility polynomials `C6` and `C7`, which collide with the
  normalized *coordinate* names `C0..C6`. In this review, `C6` and `C7`
  always mean the compatibility polynomials, and the normalized seventh
  coordinate is written `C6(normalization)`. The producer's report notes
  the labels but does not flag the collision. Downstream files should
  rename them, for instance to `Comp1`/`Comp2`.
- **Valuation-one source.** `d_i = sum_{n>=1} d_i_n Lambda^n` with no
  constant term; `SOURCE_COLUMNS.json` confirms `first_Lambda_grade =
  series_index` for every `d` column. My reconstruction uses exactly this
  and reproduces the DAG.
- **`k10_0 != 0`.** Inherited from V23's `unit_condition`. Recorded, but
  worth stating plainly: the exact linear-algebra theorem needs only
  `W != 0`. `k10_0` enters only the Rabinowitsch localization of the
  modular diagnostic. `D(k10_0*W)` is contained in `D(W)`, so certifying
  on the smaller chart is sound but weaker than what was proved.
- **`W != 0`.** Load bearing in both directions, as shown in sections 3-5.
  Nothing is claimed on `W = 0`, where the rank can drop below five and
  the two-covector basis degenerates.
- **Prior rows and grades 2..6, and `F10 = 0`.** These are hypotheses,
  not results. They enter the exact statement only as the conditional
  "complete honest prefix" and enter the modular script as ideal
  generators. All 35 rows and the `F10` quartic were reproduced
  independently. `F10` plays no role in the exact grade-seven claim.
- **Grades 0 and 1** vanish identically, so the prefix genuinely starts
  at grade 2.
- **Newest variables.** Exactly `(d0_6,...,d5_6,k10_3)`, established by
  the sensitivity census of section 2 rather than assumed.

## 8. Defects

| id | severity | defect |
| --- | --- | --- |
| R-1 | **material** | `RESULT.json`'s `modular_reduction_status` records a modular zero without recording that the localized ideal is the unit ideal, making the field misleading in isolation. The producer knew the check was missing and said so in prose; the machine-readable field does not. Must be corrected or superseded. |
| C-1 | minor | `EVIDENCE.sha256` omits `freeze_check.stdout`, `launch_registration.txt` and the two `outer.*` files, so the freeze transcript and launch telemetry are outside the sealed manifest. |
| C-2 | minor | `RESULT_V24.md` is hash-pinned nowhere. |
| H-1 | hygiene | `left_kernel_exact` and `left_kernel_sign_mutation_detected` are hardcoded `True` literals in the `RESULT.json` payload rather than the computed flags, and `literal_dag_replay` is a hardcoded description string. The corresponding `fail()` guards do run and do raise, so the values happen to be honest, but the pattern is the "producer-authored PASS banner" antipattern and should emit the computed values. |
| H-2 | hygiene | The compatibility polynomials are named `C6`/`C7`, colliding with the normalized coordinate names `C0..C6`. |
| H-3 | hygiene | The producer's sign mutation perturbs only the first nonzero entry of `L1`. Eight single-entry flips, a transposition, a scaling and an entry replacement are all cheap and all fire; the control should be broadened. |

None of C-1, C-2, H-1, H-2, H-3 affects the mathematics, all of which I
rebuilt independently. R-1 does not affect the PASS statement either,
because modular membership is outside the allowed adjudication, but it
does invalidate a field that a downstream reader would otherwise consume.

## 9. Additional diagnostics

Beyond the three primes reported in section 6, I launched a probe of the
**un-localized** prior ideal (the same 35 generators without the
Rabinowitsch generator `zinv*k10_0*W - 1`) to separate two possibilities:
that the prior stratum is empty outright, or that it is nonempty but
contained entirely in `k10_0 * W = 0`. That distinction matters for
choosing the next gate but cannot change this verdict either way, since
the PASS is exact linear algebra over `Q[x][1/W]` and is independent of
any characteristic. That standard basis was still running when this
review was written; unlike the localized ideal, it does not collapse
quickly, which is itself weak evidence that the un-localized prior ideal
is proper and therefore that the stratum lives inside `k10_0*W = 0`. It
is recorded as an open diagnostic, not as a finding.

## 10. What this PASS does and does not certify

Certified, and nothing more:

> Conditional on the complete honest prefix (normalized `C6 = 1`,
> valuation-one source, `k6_0 = 0`, `Phi[row,grade] = 0` for rows 1..7
> and grades 2..6, `F10 = 0`) and on the chart `D(k10_0 * W)`, the exact
> literal grade-seven newest-coefficient system
> `A(x) (d0_6,...,d5_6,k10_3)^T + b = 0` is solvable if and only if the
> two frozen exact compatibility polynomials `C6` (110,117 terms) and
> `C7` (83,298 terms) both vanish.

Explicitly not certified: chart nonemptiness over `Q` or any finite
field; modular ideal membership (**refuted as informative** at all four
primes tested); exact-`Q` ideal membership; anything on `W = 0`; grades eight
through nineteen; existence of a compatible prefix; a full jet or arc;
K00 closure incidence; order two; maximum twelve; JC2.

**Recommended next gate.** Not grade eight. The charged chart has no
points over `F-bar_p` for `p in {65521, 32003, 1000003, 2147483629}`, so
the highest-value next step is deciding nonemptiness of the prior stratum
on `D(k10_0*W)` over `Q` — either an exact-`Q` standard basis of the same
35 generators plus the Rabinowitsch generator, or an explicit
`1 = sum_i h_i g_i` certificate. Computing further grades of a
compatibility ladder over a chart that is empty at four primes would be
wasted work. If the chart is in fact empty over `Q`, then V22/V23/V24 are
all true and all vacuous, and the campaign needs a different stratum, not
a longer ladder.

## 11. Reproduction record

```text
host        AWS EC2 box01, ip-172-30-0-237, 64 vCPU, 991 GiB, sys_vendor=Amazon EC2
job         ~/jobs/v24_grade7_cokernel_hostile_review_20260827T135606Z_box01
engine      python3 3.12.3; Singular 4.3.2 (4330, 64 bit)
replay      independent_v24_replay.py
            sha256 3d71bdee1244233bd4de5e3cdf8639876052d798546dc1139ccb860826bad1fa
            19.13s user, 270,632 KiB RSS, exit 0
followup    followup_v24.py  (rank census, k6_0 column, Fredholm two-sided)
properness  hostile_properness.sing (frozen lines 0-2 of the producer's script)
            sha256 89fd59562c877abea08085668638172b52c63c64af822ec6f6bf5a39ff2effd9
            295.70s user, 4:56 wall, 1,841,332 KiB RSS
verbatim    producer's frozen modular script, unmodified
            311.81s user, 5:12 wall, 1,841,008 KiB RSS
            reproduced modular.stdout 5de0fa4a...daf94 and normal forms 9a271f2a...86aa
primes      same ideal and localization at p = 32003, 1000003, 2147483629
            all three: reduce(1,G)=0, dim(G)=-1, size(G)=1
unlocalized prior ideal without the Rabinowitsch generator: still running
            at 23 minutes and 4.5 GiB when this review was written; open
```

All heavy algebra ran on AWS. No canonical ledger was edited and
`jc2-lean` was not touched.
