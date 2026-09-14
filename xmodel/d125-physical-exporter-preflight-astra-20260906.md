# D125 physical-J exporter: code and tiny controls only

2026-09-06. Producer `/root/model_productivity`. **PREP-ONLY / NO PRODUCTION BUILD / NO MATHEMATICAL PROMOTION.** Root has not authorized a full run. The normalized-support implementation remains **PROVISIONAL_UNLICENSED** pending the separate normalization review, whose live body and logs were not read.

## Deliverable and exact dependency boundary

`box/d125-physical-exporter-20260906/exporter.py` is an inspectable standard-library exact rational exporter with separately labelled original and normalized modes. It exports literal independent original-source coefficient variables, not an h/circuit parameterization. No elimination, residual selection, extra localization, new gauge, or solver call occurs. Optional Singular output is import-only over Q with explicit global `dp` order.

Read whole, with full-file SHA-256:

- `xmodel/d125-client-interface-astra-20260906.md`: `0c5270a432a6336c17c4693034e36cb496f139c3267843e3ac06628ec8c4b255`.
- `xmodel/d125-source-contract-gate-fable5-20260906.md`: `a802587179b6f105bb47555ceb0e6a1d20c94c68a76c6ac4a26bbea1fce7b4e4`.
- Terminal normalization producer `xmodel/d125-triangular-source-normalization-astra-20260906.md`: `8ea55aaf26acbd4992aee9d14cce8712fda1c7590cd876ee974194c76bb3ad9e`.

These provide the complete reviewed source formulas; no additional literature theorem is invoked here. The original-source gate licenses coefficient-ideal equality between every ordinary coefficient of `J(P,Q)-1/5` and the complete transformed bracket contract, retaining all original linear constraints and the degree guard. The normalization producer, if accepted separately, supplies field-point/nonemptiness equivalence, not equality of the two ideals or a scheme isomorphism. This implementation does not supply that review.

## Exact variables and all-row contract

The base ring is `Q[all P coefficients, all Q coefficients, Z_degree_guard]`. For side parameters `(D,U,h)=(75,15,3)` and `(125,25,5)`, retain every original exponent

`i,j>=0, i+j<=D, ell=5i-j<=U`.

Variables are deterministically ordered by side P then Q, increasing ell, then increasing i. JSON IDs are zero-based; `P_u15_v60` has explicit exponent `[15,60]` and public source name `P_15_15`. Q is analogous. Z is last. Both additive constants remain literal ring variables: they occur in none of these D125 rows, so they are a harmless two-dimensional cylinder, but are not silently removed.

Original mode retains the entire support. Normalized mode deletes only source variables outside `j<=60` for P or `j<=100` for Q, and those on the respective top horizontal row except `(15,60)` or `(25,100)`. This is explicitly the proposed normalized subchart, with omitted coefficients specialized to zero. It is not an unlicensed coefficientwise inference from a partially solved Jacobian system.

In **both** modes, enumerate the original bands `ell=-D,...,U`, and for each retain every original jet

`sum_i binom(5i-ell,k) a_(ell,i)=0`,

for `0<=k<max(0,ceil((5ell-h)/12))`. A removed normalized variable contributes literal zero; the row and its label remain even if it becomes the zero polynomial. The five pins are exactly

`[t^4]p_3=1, [t^21]p_15=1, [t]q_1=-1, [t^18]q_13=-3, [t^35]q_25=-9/5`.

Pin rows use Taylor order `t_power-ell`, not `t_power`. The degree guard is the original cubic row

`Z_degree_guard * P_u15_v60 * Q_u25_v100 - 1 = 0`.

No `J0=1` gauge, top-coefficient gauge, row truncation, or discarded degree-drop component is hidden in the exporter.

For each possible ordinary output exponent `(I,J)`, loop only over P support and force the unique possible Q exponent

`(k,s)=(I+1-i,J+1-j)`.

If it belongs to Q support, contribute the exact integer coefficient `i*s-j*k` to the bilinear monomial `P_(i,j) Q_(k,s)`. Zero determinants contribute nothing. At `(I,J)=(0,0)`, append the constant **-1/5**, even if the bilinear left side is empty. This is precisely the coefficient of `P_u Q_v-P_v Q_u-1/5`; source P/Q variables are disjoint, so different P exponents cannot create duplicate parameter monomials in that row.

The original physical envelope is `I,J>=0, I+J<=198, 5I-J<=36, I<=39`. The normalized mode additionally uses `J<=159`. Every slot in the respective envelope is emitted, including zero rows. All possible nonzero outputs are inside: the two derivatives reduce ordinary degree by 2, `(5,-1)` weight by 4, and horizontal exponent by 1; the normalized vertical exponent is at most `60+100-1`. Thus enumeration cannot miss an output outside its envelope. This is a symbolic completeness argument, not a production recount.

Quoted source counts are original `706+1901=2607`, normalized `571+1551=2122`, before the one inverse variable and without eliminating the linear rows. The two full rings would therefore have 2608 and 2123 variables. The source gives 189 original jet slots and 5 pins. The 4572/3792 physical-slot bounds would, **if this all-slot code completes unchanged**, produce 4767/3987 total rows including zeros and guard. None of these is a measured full export or an assertion about nonzero row count, independent equations, dimension, or runtime. The full source support, full pair census and full coefficient generation were not executed here.

## Portable format, completion, and operational guards

`literal.jsonl` consists of one canonical JSON header, every variable record, every labelled literal row, and a complete footer. A row term is `[numerator-string,denominator-string,[variable IDs]]`; the empty list means 1, and repeated IDs mean powers. Integer arithmetic and reduced `Fraction` arithmetic avoid precision or machine-offset assumptions. There are no circuit variables. Rows are streamed individually rather than collecting the giant ideal in memory.

The header charges all three source hashes, the running builder hash, exact spec, field/order, variable map count, mode, zero/constant policy, and a canonical authority digest when supplied. The footer records complete status, SHA-256 of every prior stream byte, per-kind row/zero/term counts, variable count, and unused-variable IDs. The fresh-directory manifest records full JSONL and optional Singular file digests and construction caps. Output paths are exclusive/fresh, never overwritten or resumed. A capped/incomplete run does not receive a successful manifest; footerless JSON is rejected. A complete JSON stream and a complete optional Singular stream remain distinct artifacts; require the successful manifest and verify both full-file hashes when accepting the pair.

`verify()` reconstructs and compares every expected literal row and variable record, checks exact header, prefix digest, counts and strict EOF. **It reuses the export formula and is not an independent mathematical builder.** The tiny controls below provide a separately implemented pair convolution and source expansion. Production replay is full arithmetic and also requires explicit root authority.

CLI production modes and the build/verify API reject absent authority **before source-variable enumeration or output-directory creation**. The authority must have schema `jc2.d125-export-authority/v1`, the exact mode, `root_green:true`, matching builder hash and explicit positive integer output/wall/address-space limits. This is a cooperative accidental-run guard, not an authentication or mathematical-license mechanism. CLI applies the address-space limit; the internal writer checks elapsed time and aggregate JSON/Singular output bytes. A separately reviewed external process-group runner is still required for a robust production wall/RSS cap. No production authority file exists in this packet.

Singular output contains only ring definition, the complete literal ideal with row-label comments including zero rows, an import-only completion marker, and `quit`. No `std`, `slimgb`, `groebner`, msolve adapter or solve is present. Tiny text controls verify its exact restricted grammar, ring/order and each rational literal against JSON rows. **Actual Singular parsing has not been run.**

## Tiny independent checks and charged artifacts

`test_exporter.py` runs only degree-at-most-4 fixtures, with a 25-second alarm and 512MiB address-space limit. Both normal and optimized-Python runs passed, in approximately 0.238/0.235 seconds; reported process `ru_maxrss` was 244848/244856 KiB (not an incremental-memory measurement). No giant arithmetic or external CAS was used.

Checks include direct rectangular support enumeration; independent all-pairs Jacobian convolution on the tiny supports; direct binomial expansion under `Phi(u)=X^5, Phi(v)=Y+X^-1` for every toy jet and pin; identical original jet labels in both modes; original degree endpoints; exact optional Singular literals; retained constants and zero rows; and a positive Keller control `P=u+v^2, Q=v/5, Z=5`. Its guard rejects zero Z and a dropped original top coefficient. A deliberately empty bilinear constant row still imposes `-1/5=0`.

Seventeen actual rejection controls per run cover wrong Jacobian target sign, wrong determinant, wrong pin, variable-map drift, field drift, missing target row, missing degree guard, missing footer, trailing bytes, bad digest, existing output directory, byte-cap interruption, incomplete stream, and both CLI/API production modes without authority. Checks use explicit exceptions, not erasable assertions.

The original toy has 18 variables and rows `(jet,pin,physical,guard)=(27,5,14,1)`; its zero counts are 13 jets and 1 physical row. The normalized toy has 11 variables and `(27,5,11,1)` rows, with 16 zero jets and 3 zero physical rows. These are **toy** measurements, not D125 measurements. Normal and optimized runs produced identical literal/Singular artifact hashes.

Charged files under `box/d125-physical-exporter-20260906/`:

- `exporter.py`: `a8092908c9f4916306e24fdeca622426f8e6be09ab4f3d0d19e7488e05eca2f9`.
- `test_exporter.py`: `5444310d1ebfa8a9c7b55fe40ffaa53c3dc934dd201a0e9a378798a3ed4c11d4`.
- `toy-checks-v3/summary.json`: `322a7d9e84113ab296172e11c7701c2a3d793922ce35979f73012546b8a249b7`.
- `toy-checks-optimized-v3/summary.json`: `ea831f68625f69fdd2c3ede82fae6bb1dc47351702e8dddf640a9d1777f91b6c`.

Each toy manifest supplies the exact artifact hashes and footer; mutation files and capped partial outputs are deliberately retained as negative-control evidence. Earlier v1/v2 draft controls are also preserved but superseded by v3. `custody.json` records source/code hashes and terminal status. Owned artifacts total less than 2MiB at handoff; existing campaign files were not overwritten.

## Proposed measured-run decision, not authority to execute

1. Root reviews this code and obtains the separate normalized-support license if selecting that mode. Charge the exact builder plus gate hashes and create a run-specific authority; leave the other mode unrun. Resume only an explicitly root-owned worker if root independently approves.
2. On a fresh EBS-backed task directory, one capped construction plus complete replay could use an initial combined 600-second/8GiB process cap and 1GiB aggregate output limit, sequentially, no retries or automatic enlargement. These are proposed safety limits, **not runtime predictions**. Keep inputs/authority/source/ring/row maps, explicit process identity, cap result, manifests and hashes. Check the literal footer and strict whole replay, with exact counts discovered from the result rather than assumed from metadata.
3. If complete and root retains authority, a separate exact-Q Singular **import only** can be budgeted at 300 seconds/16GiB, under the reviewed runner, with terminal identity and output capture. Do not run a basis computation. Parser failure, cap, memory failure, dimension output, or successful import says nothing about unit/properness. A completed original-source ideal plus a later separately reviewed certificate would still be needed for any mathematical result.

STOP at preflight. No production generation, full support enumeration, pair census, parser, AWS/SSH operation, solver, live gate/body read, shared-ledger edit, or `jc2-lean` access occurred. All toy subprocesses were synchronously reaped; no background writers/PGIDs remain. Root retains the next-run and promotion decisions.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12293`.
- Body SHA-256:
  `8d62556fd28ec5decf406bce350190bc4fcf7358068c1a0dd83bade96e0b4032`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
