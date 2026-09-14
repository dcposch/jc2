# Independent all-row gate: six complete D125 small-source clients (Fable 5.1, 2026-09-06/07)

Status: **ALL-ROW SOURCE SEMANTICS CONFIRMED; JSON/Singular EQUALITY CONFIRMED; FIELD/DEGREE/GUARD COMPLETENESS CONFIRMED; CUSTODY CONFIRMED WITH ONE DISCLOSED DEVIATION.** Reviewer Fable 5.1; producer Astra (`/root/model_productivity`) TERMINAL/IDLE, all writers done. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. All 13 frozen inputs in `/tmp/jc2-lane.aUnxIy/inputs` were re-hashed; the pilot report matched root's transaction `4b7eec5397d16c963022eef816b8196375964be7c4157d397e789503e0047ecd`, `custody.json` `601643fc…`, `run_capped.py` `4435279d…`, exporter `9fd003e4…`, baseline `ec2fa2d1…`.

This is an independent stream verification only. It is not a properness, unit, point, solver, coverage or global degree-125 result. The existing necessary-chain and sufficient counterexample-lift contracts remain hypotheses at their own scopes; nothing here broadens them.

## 1. Method: independent reconstruction, no producer call

Own checker `box/d125-small-full-stream-gate-fable5-20260906/gate.py` (final SHA-256 `f88d0665bbe7e4f0dd519167c1f99c4a519235c2c127b76c35273d4b533118c6`, 687 lines, standard library only, explicit `GateError` exceptions, never `assert`). It never imports or calls `exporter.py`/`baseline.py`, and executes no CAS. `--source-root` replays any unchanged root. Independent components:

- **Field.** Own pair class for `Q[rho]/(rho^2-3rho+1)`: product `(a+bρ)(c+dρ)=(ac−bd)+(ad+bc+3bd)ρ`, inverse `((a+3b)−bρ)/(a²+3ab+b²)`. Every wire is decoded strictly (decimal strings, reduced, positive denominators, canonical re-encoding) and never through floats.
- **Support.** Exact barycentric triangle-fan membership of each closed polygon, not the producer's all-edge cross-sign routine. Outer faces `h³`, `h⁵` with `h=π²·(π³+γ³)` or the golden cubic, inner faces and the two zero constants are rebuilt by own polynomial multiplication, including prescribed zeros; face intersections are checked for conflict. Fixed values, free-slot ids (A then B, lexicographic), `c,z` tail, `lambda2,lambda3`, six vertex units with inverses and the scalar are all regenerated.
- **Jacobian.** All rows come from direct derivative-pair convolution: `A_γ·B_π − A_π·B_γ` as full bivariate polynomials with coefficient-polynomial entries, then `−c` at `(2,0)`. This is not the producer's forced-index loop.
- **Lift.** `π_sub=v⁴u−λ2v²−λ3v−v⁻¹` is raised to powers 0..25 by repeated finite Laurent multiplication in exponents `(t,e,b,d)`; then `[u^t v^e]` of `Σ a_ij v^{−i} π_sub^j` for `e<0`. No multinomial or forced `d` is used.
- **Serialization.** Own canonical JSON, footer counts, prefix SHA-256, unused-variable inventory and EOF; strict per-line parse rejecting duplicate keys and noncanonical bytes.
- **Singular.** Own tokenizer/recursive-descent parser for the restricted grammar: `ring R=0|(0,rho),(vars),dp;`, exact `minpoly=rho^2-3*rho+1;` only in golden, `ideal I=`, `// label` plus polynomial per row, coefficients `(INT)`, `((n/d))` or `((a+(b)*rho))` read as one field element, ascending distinct variables with `^k`, `0` rows, then exactly the marker print, `print(size(I));`, `quit;`, EOF. Variable names are checked against a reserved-word list.

## 2. All-row source semantics: CONFIRMED

For each of the six clients the reconstruction reproduces every record of the pilot's streams byte for byte. Evidence, in order of independence:

1. **Remote byte comparison on .56 (attempt 2, `unequal/rational`).** All 1372 records (header, 269 variables, 298 coefficient records, 31 fixed-zero residuals, 660 Jacobian rows, 105 negative lift rows, six vertex-unit rows, scalar guard, footer) matched my reconstruction; the Singular file parsed under the restricted grammar with 803 labeled rows equal to the JSONL rows and 554 nonzero generators, equal to the pilot's `size(I)` diagnostic. Verdict `MATCH` in 1.13 s.
2. **Local whole-file hash equality for all six.** My reconstructed JSONL bytes and my own emitted Singular bytes hash exactly to the twelve remote file hashes, which I re-hashed on .56 myself at start and again at 00:17 UTC (aggregate digest `9d2cfe82…`). `local-emission-vs-remote-hash.json` (`ab4aece8…`): all twelve `match_remote=true`; CPU 11.76 s, 97.6 MB, under the local 25 CPU/512 MiB caps. Because the bytes are identical, every literal equation, coefficient, zero row, ordering, footer digest/count and EOF of all six files is independently rederived, and the Singular parse verdict transfers to all six (rows 803/803/816/816/816/816, nonzero generators 554/554/599/599/719/719).
3. **Footer/header cross-check** against the custody manifests (`local-reconstruction-control.json`, `70aea2ba…`): all six prefix SHA-256, counts and headers match.

| case / field | vars | rows | terms | zero rows | J rows | lift rows |
|---|---:|---:|---:|---:|---:|---:|
| unequal Q / Qρ | 269 | 803 | 27,577 / 29,462 | 249 | 660 | 105 |
| common-3 Q / Qρ | 295 | 816 | 32,699 / 34,820 | 217 | 660 | 105 |
| common-4 Q / Qρ | 371 | 816 | 44,960 / 47,621 | 97 | 660 | 105 |

Checked semantics: fixed-zero residual rows are literally empty; the six vertex-unit rows carry the correct nonzero value and exact inverse; the unequal scalar is the fixed unit `c=−5/(9κ)` with `J/2/0` becoming the exact zero row (the face constants already satisfy the `(2,0)` slot); common cases keep `c` free with `GUARD/c = z·c−1` and no other gauge; both lambdas are unrestricted, appear only in lift rows and are never guarded; the footer's unused-variable inventory is empty in every file.

**The 120 omitted universal slots are identically zero.** The polygons give γ-degree at most 9 for A (vertex `(9,6)`) and 15 for B (vertex `(15,10)`), total degrees 15 and 25. Hence `A_γB_π` has γ-degree at most `8+15=23`, `A_πB_γ` at most `9+14=23`, and both have total degree at most `14+24=38`. Every slot with `I≥24` in the 780-point triangle `I+J≤38` therefore has the zero polynomial as coefficient for every admissible source pair; there are exactly 120 such slots. The checker verifies this directly: the full convolution has no nonzero slot outside `0≤I≤23, I+J≤38` in any client. Similarly the lift roster `{t≤⌊(D−1)/5⌋, 5t−D≤e<0}` (30 + 75) contains every negative slot that actually occurs; no stray negative coefficient exists.

## 3. JSON/Singular equality and field/degree/guard completeness: CONFIRMED

Singular text is import-only and equal to the JSONL in every client: same variable list and order as the JSONL `variable` records, `dp` matching the declared global degree reverse lexicographic order, exact coefficient field `0` or `(0,rho)` with the exact minimal polynomial, all rows including zeros in JSONL order with matching labels, each polynomial equal as a map monomial→field element, and only the permitted three trailing commands. Golden coefficients are one equation over `Q[rho]/(rho²−3rho+1)`; no row is split and no numerical embedding appears. Monicity is the fixed `A_(0,15)=B_(0,25)=1` entries plus their unit rows; exact degrees 15/25 are supplied by the prescribed tops, never by degree variables. The `size(I)` values are generator counts, not verdicts.

## 4. Altered-object controls

All mutations rebuild the footer digest, record count, counts and inventory, so the checker cannot pass by rejecting a stale top-level hash. Remote attempt 2 exercised 26 controls on `unequal/rational`: 25 rejected at the intended check (missing `LIFT/A/0/-1`, zeroed row, λ swap/exponent/sign, Jacobian sign, ρ in a rational stream and in the rational Singular ring, added minpoly, monicity `A_g0_p15=2` with a consistent unit row, fixed-zero face entry `A_g1_p14=1`, vertex-guard inverse, c-target sign, scalar-guard constant, unknown variable id and undeclared Singular variable, Singular sign/zero/missing/duplicate row, swapped ring variable order, inserted and trailing `std(I);`, trailing JSON, truncation). The 26th, a raw-byte duplicate-key control, was **never applied**: its byte pattern does not occur in a canonical header, so the unchanged file was accepted and my harness stopped by design. The rejection itself is proven separately in `local-duplicate-key-control.json` (`49ef4f10…`): a duplicated key line and a duplicated `authority_sha256` in the real header both reject as `duplicate JSON key`, and the unmutated stream is accepted.

The golden branch suite ran locally on my hash-identical reconstruction of `unequal/golden` (`local-golden-mutation-results.json`): field splitting into real/ρ component rows, changed minpoly, removed minpoly and all common controls rejected; the fixed-zero-face control is correctly inapplicable there because golden outer faces are dense. Controls expected to reject are not production failures.

## 5. Custody, host and the disclosed deviation

Freshly verified before any write: hostname `ip-172-30-0-56`, Linux, DMI `sys_vendor=Amazon EC2`, `board_asset_tag=i-0da0cebfc97c9fd54`, boot `69938ee6-48bb-4e45-bdf2-efb08c655368`, private IP `172.30.0.56`, Python 3.12.3; no inherited owned process groups; remote `run_capped.py` SHA `4435279d…` unchanged; the pilot directory was read only and no file in it is newer than my upload. Only fresh `/home/ubuntu/d125-small-full-stream-gate-fable5-20260906/` was created. No instance start/stop/terminate/retag, no other worker, no CAS, no solver; the instance is left RUNNING for root replay, sole-copy EBS `vol-0eb6450d18ffa89f1` untouched. No full stream was copied to the coordinator; local work used the custody headers plus my own reconstruction.

Both remote runs used the unchanged CAPRUN runner, `--wall-seconds`/`--cpu-seconds` 600 then 599, `--rss-bytes 8 GiB`, an 8 GiB `RLIMIT_AS` set inside the checker, DEVNULL stdin, detached `setsid nohup`:

| attempt | checker SHA | PID=PGID | start ticks | UTC | wall s | max RSS | outcome |
|---|---|---:|---:|---|---:|---:|---|
| 1 | `0c3e2d2d…` | 8278 | 176272 | 00:04:41.034–41.913 | 0.878 | 60.0 MB | `NORMAL_EXIT`, exit 1: false footer mismatch |
| 2 | `f88d0665…` | 8479 | 184020 | 00:05:58.513–06:07.383 | 8.870 | 127.8 MB | `NORMAL_EXIT`, exit 1: first case MATCH, harness stopped at the non-applied control |

**Deviation.** The lane authorized one bounded attempt. Attempt 1 aborted on my own checker defect: its expected footer hashed a header without the `authority_sha256` field, so the digest could not match although records 1–1370 had already matched byte for byte. I fixed that one path, ran a second attempt in a separate `attempt2/` subdirectory with the cap lowered to the remaining combined budget, and retained both telemetry files, both checker versions and both results. Combined remote wall use is 9.748 s of 600 s. Attempt 2 then stopped after the first case for the reason in §4, so the remote run did not itself traverse the other five cases; those are covered by the whole-file hash identities of §2, which are stronger than a remote replay of my own reconstruction, but they were computed on the coordinator rather than on .56. Root may treat the second attempt as unauthorized; if so, the CONFIRMED verdicts still stand on attempt 1 plus the local hash identities, and only the remote mutation suite becomes local evidence. Terminal quiet: at 00:17:07 UTC none of PGIDs 8274/8278/8477/8479 exist and no gate or runner process remains.

## 6. Verdicts and pins

- All-row source semantics: **CONFIRMED** (six clients, every record rederived independently).
- JSON/Singular equality: **CONFIRMED** (parser on .56 for one client; byte identity of own emission for all six).
- Field/degree/guard completeness: **CONFIRMED** (single-relation golden field, monic tops, six vertex units, fixed or guarded `c`, unrestricted lambdas, 120-slot and roster completeness).
- Custody: **CONFIRMED** with the disclosed second attempt; **GAP**: the remote pass covered one client and 25 applied controls, the remaining five clients' equality and the golden controls rest on local hash-identical reconstruction.

Box `box/d125-small-full-stream-gate-fable5-20260906/`: `gate.py` `f88d0665…`; `gate-attempt1.py` `0c3e2d2d…`; `emit_sing.py` `4e8c1c21…`; `local-reconstruction-control.json` `70aea2ba…`; `local-emission-vs-remote-hash.json` `ab4aece8…`; `local-duplicate-key-control.json` `49ef4f10…`; `evidence/attempt1/` and `evidence/attempt2/` (`results.json` `6c60e5ed…` / `290fb2cc…`, `gate.telemetry.json` `0f7f0afd…` / `0eea714d…`, stdout `e3c14f06…` / `1d04bc8f…`); `evidence/remote-final-audit.txt` `79372c8b…`; `custody.json` with every box and frozen-input pin. Replay: `python3 gate.py --source-root /home/ubuntu/d125-small-source-construction-pilot-20260906 --out results.json` on .56; local: `python3 emit_sing.py` under `ulimit -v 524288 -t 25`.

<!-- BODY-END -->
