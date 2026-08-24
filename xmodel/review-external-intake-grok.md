# Hostile review: `xmodel/intake-supermind-guo-20260824.md`

| Field | Value |
|---|---|
| Claim | Frozen bounded SuperMind/Guo intake: exact terminals, same two Prop-4.3 systems, no msolve `-g`, no unconditional `(72,108)` / 125 / JC2 |
| Overall verdict | **CONFIRMED WITH GAPS** |
| Reviewer | Grok 4.6 (adversarial different-model verifier) |
| CLI | `grok 1.0.5 (5115b46bc909) [stable]` |
| Python | 3.14.6 (`/opt/homebrew/opt/python@3.14/bin/python3.14`); scratch venv SymPy 1.14.0 |
| Singular | 4.4.1 (44105, 64-bit, 2025-11-11); GMP 6.3.0, NTL 11.6.0, FLINT 3.6.0 |
| Sage / Docker | absent |
| Host | Darwin 23.6.0 arm64 |
| UTC | 2026-08-24T02:03:47Z |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4` |
| Scratch | `/tmp/jc2-intake-review-grok-95XRei` (fresh `mktemp -d /tmp/jc2-intake-review-grok-XXXXXX`) |

**Promotion.** The SuperMind first-layer / Case-II exact Python replay, the pinned Case-I Singular good-specialization full-rank terminal (with the Python regeneration edge kept explicit), Guo’s 790-file authoritative manifest, the degree-21 independent verifier at its stated mixed exact/frozen tier, the characteristic-zero FGLM *program* replay, the two row-split polynomial identities, the lossless Laurent rename, and the Helali/Suzuki degree-five remainder identities may be promoted off producer-checked provisional. Nothing else may.

**Quarantine if this review is treated as a failure.** Do not promote Guo Sage-only lift / `V(c)` / `D!=0` / `D=E=0` expansions. Do not treat correctness or coordinate equivalence as social or derivational independence. Do not treat either artifact, or both together, as an unconditional exclusion of every `(72,108)` counterexample, as an unconditional degree-125 theorem, or as a proof of JC2.

---

## Claim under review (not enlarged)

The intake’s five clauses, adjudicated separately against pinned bytes and local exact arithmetic, not against author prestige or prose tone.

---

## Verdict table

| Clause | Verdict | What would have flipped it |
|---|---|---|
| 1. SuperMind manifest + first-layer/Case-II exact pass; pinned Case-I Singular input is a char-0 52-dim/good-specialization full-rank terminal; Python regeneration remains capped | **CONFIRMED WITH GAPS** | checksum mismatch; Case-II Bézout remainder nonzero; Singular FAIL/exit≠0; printed qbase ≠ 52 distinct monomials; rank ≠ 52; missing good-specialization gates; silent claim that Python regenerated the `.sing` file here |
| 2. Guo 790-file manifest, logical/global audits, degree-21 verifier, char-0 FGLM, row-split identities at stated exact/regression tiers; Sage-only terminals remain GAP | **CONFIRMED WITH GAPS** | MATCH≠790; false row-split identity; FGLM markers missing; Sage path silently executed or labelled EXACT REPLAY; frozen `['1']` promoted to a local unit-identity expansion |
| 3. Same two Prop-4.3 Laurent systems via the stated lossless rename; Helali/Suzuki degree-five maps remainder 0 | **CONFIRMED** | polygon/count mismatch; rename not term-for-term; Helali or Suzuki remainder nonzero |
| 4. Neither path uses msolve `-g` | **CONFIRMED** | `msolve` / `libmsolve` / `-g 2` in a proof path |
| 5. Correctness/equivalence ≠ independence; no unconditional `(72,108)`, degree-125, or JC2 without the GGV reduction/transcription bridge | **CONFIRMED** | intake treating the two repos as independent votes; intake stating an unconditional 125 or JC2 theorem |

---

## Pins, hashes, and workspace

Fresh directory `/tmp/jc2-intake-review-grok-95XRei`, outside the campaign repository. Public clones only (`GIT_TERMINAL_PROMPT=0`, no credentials). Guo ZIP downloaded independently from the GitHub release, not copied from the producer tree.

| Artifact | Pin | Local check |
|---|---|---|
| SuperMind repo | `https://github.com/SuperMindAI/Jacobian-Conjecture.git` | commit `8b376296bb8ffeb9a6112d482b9f6b1760d8d1ef`, tree `c82d3c05bca2114435ef05023a73ce8dcbfa6684`, `2026-08-05T13:00:02+08:00`, xingchengxu |
| Guo public | `https://github.com/Kakarottoooo/jacobian-2d-research.git` tag `public-preprint-v1-2026-08-10` | commit `624a34a774276bef72b6093af8dd774713f27314`, tree `fbca91c8b11f5691d3f93014f4054c721065442b`, `2026-08-10T15:52:50-07:00` |
| Guo theorem-core | tag `larger-polygon-logical-proof-2026-08-09` | commit `7639822e66de9464e141e748088b62d73c388169`, tree `8cd8f3fde499f0f58f4a2da5b3df54c7aa585ab6` |
| SuperMind `README.md` | `6aaf773a760dc8ef91ea8ce049cfec93d6e36d959895ac76a02161e65fd2626d` | match |
| SuperMind `main.tex` | `9d757f2461f2b6c88292bd76e82131b493b22a2a6061054a609e032824d5a1a2` | match |
| SuperMind `CHECKSUMS.sha256` | `b7265df86a22030edab92d9a63a795a52b94e79bc11dc6571306d4e802485e01` | match; 26/26 `shasum -a 256 -c` OK |
| SuperMind `supplement/code/verify.py` | `2a88f31056363a385790339f72c69d6c9d8b43cc1318d305a7a3aa79b9cd6adc` | match (intake’s `code/verify.py` path is the supplement path) |
| SuperMind `case_ii.py` | `3dcf5e29e98149d5aa4ceb3ea11daa90f3ad4243b64d3e29ce026b0d3e5990d8` | match |
| SuperMind Case-I `.sing` | `6722623b82dd61bad90e53c55881a353727a51d3d1c6263d59c78fc2bd82ebae` | match |
| Archived SuperMind transcripts | `620da511…164f7` / `03e46255…c497` | match; archived only, not used as authority |
| Guo release `SHA256SUMS.txt` | `1da82c88a7d03361a174adf64b52a9f240d13b58bab175f813609fe22ba8b437` | match |
| Guo flat ZIP | `1bb8228640505e40b1b8813f78df7d7290df6baccb994a1fd92bfdf4acc14448` | match (independent download, 101170006 bytes) |
| Inner wrapper README / tar | `f187a3b0…2091` / `bafe2921…d7a8` | match after CRLF strip of inner checksum file |
| Authoritative 790-file manifest | `0d4abab2ddeb44af6771c28f689113beb4b6bb2ef55de56a190eaa7c750db6ba` | match |
| Guo manifest verifier | `059d6cccdd3b8762bd72b70d2e1877d95af6f4fcb745bebbdda73a2176fc1455` | match |
| Logical / global audits | `b4f0f194…bc0d` / `a6cad997…fa34` | match |
| Breakthrough independent verifier | `8b468f4c4b35ef076801769bc83178756c60de5a9959e5d811639c135ea54421` | match |
| Small terminal JSON (primary / independent) | `a00400fc…9bb7` / `af3cfe5c…4135` | match |
| Degree-35 lex basis | `cddb0a735a65fc39c0b6431a6edc7929274d36e5322cd7976582077991414d9e` | match |
| Row-split Singular object | `1fa46d12281933d51bb0152fdaf740e1ad10a514bdcf2ece06f5fa3a3c556f3e` | match |
| Exceptional unit-certificate JSON | `481efe2c46455cda4e4939ad36cd1650c7a8163d8c332b546e7dbcae946f7fe8` | match (72672850 bytes) |

ZIP member check: 3 names, no `..`, no absolute path. Inner tar: 828 members, types file/dir only, no links, no traversal. Extraction used Python `filter="data"` into the scratch tree. Inner `SHA256SUMS.txt` is CRLF; raw macOS `shasum -c` fails on CR-suffixed names; `tr -d '\r'` makes both inner entries OK. Portability defect, not an integrity failure, as the intake said.

PDF hashes in the *outer* checksum file were not independently downloaded here. Same perimeter as the intake: they are recorded from the hashed checksum file, not from local PDF bytes.

Producer workspace `/tmp/jc2-external-intake-20260824.iNiGQL` was listed only to learn the ZIP filename; pins, clones, hashes, and runs below are from this scratch directory.

---

## What was rerun, independently inspected, and not

Inspected before execution: SuperMind `verify.py` / `case_ii.py` / Case-I `.sing` control flow; Guo manifest verifier, logical/global audits, `independent_verifier.py`, FGLM `.sing`, row-split object. SuperMind’s only process launch is local `Singular -q`. Guo `global_degree_bound_audit.py` launches Sage only if `--skip-small-recompute` is omitted; it was not omitted. `independent_verifier.main()` would write `results/breakthrough_independent.json`; this review called `run()` and did not write. Row-split harness written only under scratch. No credentials, no repo writes, no author contact, no optional discovery jobs.

```bash
SCRATCH=/tmp/jc2-intake-review-grok-95XRei
# SuperMind first-layer + Case II, then stop (no Case-I Python regeneration)
# SuperMind Singular:
env -i PATH=/opt/homebrew/bin:/usr/bin:/bin Singular -q case_i_structural_good_reduction.sing
# Guo:
python tools/verify_supplement_manifest.py .
python tests/test_larger_polygon_logical_closure.py   # three functions, no pytest
PYTHONPATH=src:experiments python experiments/larger_polygon_program/logical_coverage_audit.py
PYTHONPATH=src:experiments python experiments/larger_polygon_program/global_degree_bound_audit.py --skip-small-recompute
# independent_verifier.run() with no JSON write
Singular -q results/belyi_edge_Q_fglm.sing
# scratch harness loading row_split_branches_exact.sing
```

Independent work, **not** PASS-string authority:

- Case-I `.sing` control flow read line-by-line (118 lines; giant coefficient payloads truncated). Closed-chart `lift(I_closed,ideal(1))` identity; char-0 `std(J1,J2,J3)` with `size=23` and `vdim=52`; `qbase`; string-map into `ring Rp=(67,theta)`; leading-ideal and specialized-`std` monomial comparison against the mapped char-0 basis; `matmult` rank 52. This is a good-specialization nonvanishing argument, not a finite-field unit-ideal inference.
- Printed `quotient_basis` counted here: **52 distinct** monomials.
- Case-II Bézout independently multiplied: `bezout_s*h12 + bezout_t*h13 == 1` over the quintic field.
- Row-split identities independently substituted in a scratch Singular harness.
- Helali map `T -> (w^4+3w^2-2w+6)/8` remainder 0; compact JSON hash `db0309143fe13954dcf41d30d5bb0e5a562b6ad1ac459516a88573d3109750b1`.
- Suzuki claimed degree-four image remainder 0; compact JSON hash `488e93978579cb4b1050cf491dc7dcef07bcf75159aca946733e4014550273b2`.
- Laurent rename checked term-for-term against SuperMind `sections/03-layer-equations.tex:40-68` and Guo `paper/raising_degree_bound_125.tex:205-255`.
- Independent lattice enumeration of the four closed polygons: 61+125 and 25+47.
- Recursive search of both pinned trees and the extracted Guo archive: no `msolve`, no `libmsolve`, no `-g 2` proof invocation (compiler `-g` debug flags in Sage-image logs are not msolve).

Not done, and not required by the scoped claim:

- SuperMind Python regeneration of the Case-I `.sing` from the universal layer recurrence (capped; `verify.py` continues into `exact_case_i_probe` after Case II).
- Guo Sage lifts, 72 MB exceptional-chart unit expansion, `D!=0` degree-18 / Sylvester checks, `D=E=0` factorwise terminals.
- Optional SuperMind `direct_std` / open-chart lift terminals.
- Optional Guo resultant rediscovery.
- Helali/Suzuki campaign replays (already in `jc72108/CROSSCHECK.md`; not re-executed here).
- GGV Proposition 4.3 itself.

---

## Clause 1 — SuperMind terminals

**CONFIRMED WITH GAPS.**

Supplement checksums: 26/26 OK. First-layer quintic reconstructed here as

```text
theta^5 - theta^4 - 9*theta^3 + theta^2 + 24*theta - 18
```

which matches `sections/04-first-layer-quintic.tex:207` and Guo’s working minpoly. Local unbuffered Python 3.14.6 / SymPy 1.14.0 printed:

```text
PASS quintic: displayed mod-5 and mod-23 irreducibility certificate
PASS first layer Hurwitz count: exact weighted orbit count = 5
PASS first layer: 18 exact coefficients and nonzero endpoints
INDEPENDENT_BEZOUT_SUBSTITUTION_ZERO_ERROR True
PASS Case II: ranks 16,17,11; seven conditions; quartic Bezout identity
PASS archived first-layer/Case-II data match
STOPPED_BEFORE_CASE_I_PYTHON_REGENERATION
```

The Bézout identity is a multiplied polynomial identity in this reviewer’s driver, not a borrowed PASS line.

Pinned Case-I input, after static inspection, rerun:

```text
env -i PATH=/opt/homebrew/bin:/usr/bin:/bin Singular -q case_i_structural_good_reduction.sing
# 271.18 s real / 268.19 s user / 522780672 max RSS; exit 0
PASS Case I A1=0 chart: direct characteristic-zero lift identity
PASS Case I structural core: basis=23 quotient=52
PASS Case I lucky reduction: mapped core and specialized ideal have the same 52 standard monomials
PASS Case I multiplication matrix: shape 52 by 52
multiplication_rank_mod_67=52
PASS Case I structural lucky-reduction full-rank witness
```

Rings are `(0,theta)` then `(67,theta)`, minpoly the common quintic. Closed-chart check is `check_closed = -1 + sum I_closed[i]*T_closed[i,1]` vanishing. Open core is `std` of three generators over `K=QQ(theta)`. Specialization maps the char-0 Gröbner basis by `execute(string(...))` into characteristic 67, requires the 52 standard monomials of `lead(corep)` and of `std(corep)` to equal the mapped char-0 `qbase`, then computes the multiplication matrix of `J4` and requires rank 52. A nonzero reduction therefore certifies nonvanishing of a specified characteristic-zero determinant. That is the argument SuperMind writes in `supplement/README.md:36-40` and `sections/07-certification-and-scope.tex:40-50`. It is **not** “the specialized ideal is `(1)` over `F_67`, hence the rational ideal is `(1)`.”

Gap, explicit: this review did not regenerate `case_i_structural_good_reduction.sing` from the universal layer recurrence. The file is hash-bound and its structural terminal passes. The regeneration edge remains a performance/replay gap, not a failed identity. Do not delete that sentence in any promotion note.

---

## Clause 2 — Guo audits and the Sage GAP

**CONFIRMED WITH GAPS.**

Fresh extraction of the inner tar:

```text
MATCH=790 MISMATCH=0 MISSING=0 UNLISTED=0 MALFORMED=0
```

791 files on disk = 790 manifest entries + `SHA256SUMS.txt`. Reverse coverage is in the verifier (unlisted counter was zero). Historical overlay manifests were not treated as release corruption.

Three regression tests, executed as plain function calls without pytest: all three assertions passed. These compare frozen JSON hashes/status fields. **REGRESSION PASS only.**

`logical_coverage_audit.py` reran. It does some exact work: `exact_support.py` enumerates the larger polygons and asserts 61/125 with lattice-map determinant `-1`; `jacobian_layers.py` rebuilds 302 coefficient equations and, with `run_symbolic_cross_check=True`, checks them against an independent SymPy expansion. The *terminal emptiness* of `V(c)` and of the `D!=0` / `D=E=0` branches is then read from frozen JSON (`exceptional_*`, `degree18_*`, `d0_*`) plus hash equality to the 72 MB certificate file. Status printed:

```text
LARGE_POLYGON_EXCLUDED_BY_LOGICAL_BRANCH_CERTIFICATES
```

That is an exact logical/hash composition of frozen terminal records, not an expansion of those terminals.

`global_degree_bound_audit.py --skip-small-recompute` reran. It did **not** launch Sage (`recomputed_during_this_run=false`). It asserted frozen small-lift invariants, including `third_compatibility_groebner_basis == ['1']` and lex-basis SHA `cddb0a73…`, hashed the five pinned arXiv source tarballs, and printed `GLOBAL_DEGREE_BOUND_125` with the reduction named as a preprint dependency. Conditional composition audit, as labelled.

`breakthrough_program.independent_verifier.run()`: five degree-21 passport orbits (`adjacent_hubs=4`, `separated_hubs=1`, `total=5`), witness cycle type `((2^10,1),(3^7),(17,1^4))`, monodromy `A_21` of order `25545471085854720000`, Newton-vertex Gröbner `('1',)`. It then **reads** frozen `results/belyi_lift_independent.json` and asserts `third_compatibility_groebner_basis == ['1']`. Independent enumeration for the passport; frozen input for the smaller-terminal unit string. Do not promote that string to a Sage lift replay.

FGLM program, `ring r=0,(a1..a6),dp`, `modStd(I,1)`, then `fglm` to lex:

```text
INPUT_GENERATORS=7
GB_SIZE=56
DIMENSION=0
VECTOR_SPACE_DIMENSION=35
LEX_GB_SIZE=6
UNIVARIATE_{1..6}_DEGREE=35
FACTOR_DEGREE=35,MULTIPLICITY=1
```

Exit 0 in 5.94 s real. Harmless `// ** redefining Factors/factor_index` warnings, as the intake said. Archived lex univariate is exactly `H(a6^7)` with no other degrees (checked here). Engine-trust note, **not** a silent Sage promotion: Singular’s `modStd` manual says exactness=1 verifies that the result is a standard basis *and contains I*; for non-homogeneous generators and a global ordering, it still calls the reverse inclusion a standard basis of I “with high probability.” The generators here are not homogeneous and the order is `dp`. The advertised program passed. Do not describe this FGLM run as a fully rational `std` over `Q`. It is also not msolve `-g`.

Row-split object `ring branch_ring=(0,gamma),(X,Y,Z),dp` with the common quintic minpoly. Scratch harness, after loading the serialized polynomials:

```text
b2*p0-a2*r7-(D*Y+E) == 0       PASS
b2*Q0-a2*Q7 == 0               PASS
```

Exit 0 in 1.65 s. This independently closes the two advertised identities, including the exhaustive split used in `REPRODUCE_LARGER_POLYGON.md:105-127`. It does **not** expand later branch certificates.

Sage-only files are present in the passing 790-file manifest. `sage` and `docker` are absent. Stale wrapper `verify_exceptional_unit_certificate.sing` still `execute`s the non-distributed `exceptional_subresultant_unit_certificate.sing`. Wrapper `verify_row_split_branch_identities.sing` is absent. Packaging defects, not identity failures.

Theorem-core `7639822e` → public `624a34a` touches seven executables (six proof/audit scripts plus `tools/verify_supplement_manifest.py`), not byte identity of every script. The intake’s reading — “unchanged” means formulas/conclusion, not every executable at public HEAD — is the safe one.

**Sage-only terminals remain GAP.** They were not silently promoted.

---

## Clause 3 — Same systems, exact field maps

**CONFIRMED.**

Polygons, from SuperMind `sections/02-small-degree-reduction.tex:53-67` and Guo `paper/raising_degree_bound_125.tex:150-157`, are literal matches of `jc72108/CROSSCHECK.md:10-16`:

| Configuration | `N(P)` | `N(Q)` | lattice (this review) |
|---|---|---|---|
| larger / Case I | `(0,0),(1,0),(8,14),(8,16),(0,8)` | `(0,0),(2,1),(12,21),(12,24),(0,12)` | 61 + 125 |
| smaller / Case II | drop `(0,8),(0,12)` | drop `(0,12)` | 25 + 47 |

Both use `[P,Q]=P_x Q_y-P_y Q_x=x^2` and require displayed vertices nonzero.

Rename, from the source formulas, not from the intake paraphrase.

SuperMind (`eq:case-II-slices`): `t_SM=x y^2`,

```text
P = y^{-2} A(t) + y^{-1} C(t) + D(t)
Q = y^{-3} B(t) + y^{-2} E(t) + y^{-1} F(t) + G(t)
```

with `(E0)--(E4)` as in `eq:E0`--`eq:E4`.

Guo (`eq:laurent-change`, `eq:small-slices`): `z_G=x y^2`, `t_G=y^{-1}`,

```text
P = A(z) t^2 + B(z) t + C(z)
Q = D(z) t^3 + E(z) t^2 + F(z) t + G(z)
```

The map `t_SM=z_G`, `y^{-1}=t_G`, `(A,C,D,B,E,F,G)_SM=(A,B,C,D,E,F,G)_Guo` sends SuperMind `(E0)--(E4)` to Guo’s five displayed identities term for term. The monomial map `(i,j) -> (i, 2i-j)` has matrix `[[1,0],[2,-1]]` and determinant `-1`. Lossless lattice automorphism, not a projection.

Common quintic, displayed identically:

```text
f(T) = T^5 - T^4 - 9 T^3 + T^2 + 24 T - 18
```

Helali `h(w)=w^5-w^4+3w^3+3w^2+26`, claimed image `T=(w^4+3w^2-2w+6)/8`: numerator of `f(T)` is exactly divisible by `h` over `QQ` (**remainder 0**). Compact JSON `["1/8","0","3/8","-1/4","3/4"]` SHA-256 `db0309143fe13954dcf41d30d5bb0e5a562b6ad1ac459516a88573d3109750b1`.

Suzuki `M(X)` as in `jc72108/CROSSCHECK.md:79-88` / the intake vector: claimed degree-four image, numerator of `f(T)` exactly divisible by `M` over `QQ` (**remainder 0**). Compact JSON of the five rational strings SHA-256 `488e93978579cb4b1050cf491dc7dcef07bcf75159aca946733e4014550273b2`. Denominator is a nonzero constant in `QQ`.

All three of `f`, `h`, `M` are irreducible of degree 5 here. Discriminant square-free kernels of `f`, of Helali `h`, and of Guo’s non-monic edge quintic `H` (the `T^5` factor of the degree-35 lex univariate) are all `663=3·13·17`. Guo’s working minpoly in the row-split object and in `eq:degree5field` is `f`, not `H`. `H(T^7)` is the archived lex univariate; Sage `optimized_representation` is the documented bridge from `H` to `f`. This review obtained a non-`None` `field_isomorphism(CRootOf(f), CRootOf(H))` and matching square-free discriminants; it did **not** close a second remainder identity for that particular coefficient list (CRootOf bookkeeping in the driver). The load-bearing Helali/Suzuki maps are to `f`, and those remainders are zero.

Field isomorphism of the first-layer quintics is not coefficient-level identification of every terminal ideal.

---

## Clause 4 — No msolve `-g`

**CONFIRMED.**

Recursive searches of the pinned SuperMind tree, the Guo git pin, and the extracted 790-file archive found no `msolve` executable, no `libmsolve` binding, and no `-g 2` command. Hits on `-g` were compiler debug flags in Sage-image version logs. SuperMind’s only subprocess is local Singular. Guo’s finite-field step, where present, is described as a guarded homomorphic image of a fixed characteristic-zero determinant (`REPRODUCE_LARGER_POLYGON.md:115-127`); the two identities this review expanded are characteristic-zero polynomial equalities.

These artifacts are not affected by the campaign msolve `-g` unit-basis erratum. They also do not repair any campaign-internal msolve `[1]` claim.

---

## Clause 5 — Independence and GGV perimeter

**CONFIRMED.**

SuperMind authorship disclosure (`README.md:62-67`): displayed author SuperMind, work attributed to GPT-5.6-Sol Max, human involvement limited feedback. Guo `PUBLIC_RELEASE_NOTES.md`: Codex used for exploration/CAS/drafting/packaging; Ziwei Guo takes responsibility; unverified generative output is not a theorem premise. Dates: SuperMind pin 2026-08-05, Guo theorem-core 2026-08-09, public 2026-08-10. SuperMind `references.bib:88-96` still points ratto3423 to MathOverflow answer `513458` (Eremenko); ratto3423 is `513493`. Citation defect, not a polynomial defect.

Correctness of two terminals plus a lossless rename does not decide social or derivational independence from the Suzuki–Roy–Helali line, or from each other. Shared GGV reduction, shared degree-21/five-dessin core, shared exact quintic, shared publication neighbourhood, and same-family model assistance remain. No independent-vote count follows from repository count.

SuperMind `supplement/README.md:6-12` and `sections/07-certification-and-scope.tex:79-89`, and Guo `README.md:22-28` / `PUBLIC_RELEASE_NOTES.md`, already refuse JC2 and refuse an unconditional degree-125 theorem. SuperMind’s phrase “unconditional once the cited reduction … [is] accepted” is **conditional on that reduction and the transcription/normalization bridge**. This review does not enlarge that perimeter.

No `(72,108)` exclusion, degree-125 lower bound, or JC2 claim is promoted from this intake without the GGV Proposition-4.3 reduction/transcription bridge. Degrees 125 and above remain open.

---

## What may be promoted, and what stays trusted-external

**May be promoted (this reviewer’s exact replay / inspection):**

- SuperMind supplement hash integrity; first-layer and Case-II exact Python identities, including an independently multiplied Bézout identity.
- SuperMind pinned Case-I Singular good-specialization full-rank terminal, with the Python regeneration edge disclosed.
- Guo 790-file bidirectional manifest; inner tar integrity after CRLF normalization.
- Guo logical/global audits at the stated hash/regression/conditional-composition tiers.
- Guo degree-21 passport enumeration in `independent_verifier` (not its frozen `['1']` payload).
- Guo FGLM *program* replay (markers above), subject to Singular `modStd`’s documented verification contract.
- Guo row-split identities `b2*p0-a2*r7=D*Y+E` and `b2*Q0-a2*Q7`.
- Literal Laurent equivalence of the two Prop-4.3 systems via the stated rename.
- Exact Helali and Suzuki remainder identities onto the common quintic, with the two compact JSON hashes above.

**Remains trusted-external / producer-checked / GAP:**

- SuperMind regeneration of the Case-I Singular input from the universal layer recurrence.
- Guo Sage lift of the smaller configuration; Sage reconstruction of the 61/125 system through 302 equations onto six row-split generators; both 72 MB exceptional-chart unit verifiers; `D!=0` degree-18 denominator/divisibility/determinant checks; `D=E=0` factorwise terminals.
- Frozen JSON status fields consumed by the logical/global audits, including `third_compatibility_groebner_basis == ['1']`.
- GGV Proposition 4.3, the small-degree theorem, and the transcription/normalization bridge.
- Pre-existing Helali and Suzuki campaign replays (`jc72108/CROSSCHECK.md`); not re-executed in this review.
- Social or derivational independence of SuperMind, Guo, Helali, Suzuki, or Roy.

---

## Hard perimeter

| Claim | This review | Hard perimeter |
|---|---|---|
| Both artifacts target the campaign’s two systems | **EXACT PASS** | polygons, bracket, lattice counts, term-for-term rename |
| SuperMind smaller terminal | **EXACT REPLAY PASS** | SymPy exact arithmetic / pinned source |
| SuperMind larger terminal | **EXACT REPLAY PASS** | Singular exact arithmetic / pinned `.sing`; Python regeneration capped |
| Guo archive completeness | **HASH PASS** | authoritative 790-file v2.1 manifest |
| Guo degree-21 edge / FGLM program | **EXACT PROGRAM REPLAY** | Singular `modStd(I,1)` + `fglm`; not a rational `std`; Sage lift not run |
| Guo full smaller / larger exclusion | **PARTIAL / GAP** | frozen outputs hash-bound; Sage expansions not run |
| Common degree-five field vs Helali/Suzuki | **EXACT PASS** | remainder identities; does not identify every terminal ideal |
| Social/derivational independence | **UNRESOLVED** | different bytes/methods are insufficient |
| Both residual supports empty | **STRONGLY SUPPORTED, not re-closed here for Guo Sage charts** | SuperMind replay + pre-existing Helali/Suzuki; Guo Sage GAP remains |
| Every `(72,108)` counterexample excluded | **CONDITIONAL** | GGV Prop 4.3 + transcription bridge |
| Every counterexample has max degree ≥ 125 | **CONDITIONAL** | also the cited GGV small-degree theorem |
| Plane Jacobian conjecture | **NO IMPLICATION** | degrees ≥ 125 remain open |

---

## Overall verdict

**CONFIRMED WITH GAPS.**

The intake’s five clauses survive a different-model replay of the named evidence perimeter. No false identity and no unrecoverable manifest was found. The gaps it declared are real: SuperMind’s Python Case-I regeneration, Guo’s Sage-only terminals, unresolved lineage, and the GGV bridge. They were not silently promoted. Promote only the exact items listed above. Keep the public theorem sentence unchanged: exact external certificates exclude both transcribed Proposition-4.3 residual systems **conditional** on the cited GGV reduction/transcription bridge; they do not prove JC2.
