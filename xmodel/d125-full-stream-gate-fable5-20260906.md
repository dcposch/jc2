# Independent full literal D125 stream gate

2026-09-06. Gate lane (Fable 5.1), bounded 30 minutes, hard delivery 22:25 UTC. Charged producer: `xmodel/d125-physical-export-pilot-astra-20260906.md` (SHA-256 `328431e38fd1acd307a0e217ed46a02ef6db9d4bfffc03b458b70835965620a1`, recomputed here) with its `box/d125-physical-export-pilot-20260906/evidence/` custody set. Status: **INDEPENDENT WHOLE-ROW REPLAY OF ONE LITERAL STREAM; NO PROPERNESS, UNIT, POINT, SOLVER OR GLOBAL-125 CLAIM.**

## 0. Verdicts

| Question | Verdict | Basis / first missing hypothesis |
|---|---|---|
| Complete-source semantics: every row of `complete/literal.jsonl` is exactly the reviewed contract (189 original jets, 5 pins, every ordinary coefficient of `J(P,Q)-1/5` on the full normalized envelope including 55 zero rows, cubic guard), no extra rows, no gauge, no elimination | **CONFIRMED** | own rebuild by a different algorithm matched all 3,987 rows coefficient-for-coefficient; nothing missing. Semantics are literal over `Q`; normalized-to-original equivalence remains root's char-0 field-point licence, not scheme/ideal or mod-p equivalence, and was not re-reviewed |
| Literal JSON / Singular equality: ring, order, every variable, every polynomial, footer, digest, EOF, no hidden command | **CONFIRMED** | own restricted grammar parsed all 7,980 lines; 878,473 atoms equal the JSON terms, same order; only ring/ideal/print/quit lines exist |
| Degree guard: `Z_degree_guard*P_u15_v60*Q_u25_v100-1` present, endpoints on the original total-degree boundary, guard variable otherwise unused | **CONFIRMED** | exact row match; own check that `(15,60)`, `(25,100)` are the unique top-row survivors of the normalized support with `i+j` equal to 75 and 125 |
| Instrument custody: producer stream unchanged, exact host/volume, one CAPRUN run inside cap, terminal quiet, producer files preserved | **CONFIRMED** | pre/post input SHA equal, mode 444 and mtimes unchanged; PGID 3079 group empty after exit; only the fresh gate directory was created |
| Engine-import evidence (Singular parses the file, 15.09 s / 6.72 GiB) | **GAP for this lane, producer-only** | not rerun here by design; my parse shows the file's content, not Singular's runtime behaviour |

## 1. What was read and what ran

Read whole from the immutable lane inputs: `exporter.py` (SHA `a8092908…eca2f9`), `test_exporter.py`, `payload.py`, `manifest.json`, `authority.json`, both telemetries, `custody.json` structure, the pilot, preflight, client-interface, source-contract-gate, normalization producer and normalization-gate reports, and `FALLACY-v2.md`. `run_capped.py` (SHA `4435279d…d196c2`): argument parser, `execute` status branches, `sample_group`, `wait_for_group_quiet`, the `killpg` TERM/KILL cleanup path and `main` were read; the remainder was skimmed. Not read: any live 14:35 cross submission, the separate positive-face Fable gate, other workers, keys, ledgers, launcher or adapter code, `jc2-lean`.

Local work (coordinator): writing `box/d125-full-stream-gate-fable5-20260906/gate_check.py` (SHA `b175ccc7ed339e115c58e30a0893a0e6566a02152d837e4469d4b82d41ce673f`) and one toy shakedown under `ulimit -v 524288` and `timeout 30`: elapsed 0.14 s, resident set under 32 MB. No full input was copied to the coordinator and no full arithmetic ran locally.

Remote work (`172.30.0.56`): one CAPRUN run of the checker. Nothing else was executed there except read-only identity capture, hashing and `ps`.

## 2. Independent algorithm (not the producer's)

The checker imports nothing from `exporter.py` and calls neither `rows()` nor `verify()`. Its expected objects come from the reviewed contract, `(D,U,h)=(75,15,3)` for P and `(125,25,5)` for Q, normalized caps `deg_v P<=60` with `[v^60]P=a*u^15`, `deg_v Q<=100` with `[v^100]Q=b*u^25`, the five pins, target `1/5`, built as follows.

- **Support** by direct rectangular enumeration over all `0<=i,j<=D` with `i+j<=D`, `5i-j<=U`, `j<=V`, and `j==V` only at the guard `i`. Result: 571 P and 1,551 Q exponents, plus `Z`, 2,123 variables. The producer's band parametrization `i` in `[ceil(ell/5), floor((D+ell)/6)]` was not used.
- **Jets and pins** from actual integer powers of `Y+X^-1`, computed by repeated multiplication as exponent dictionaries; the order-`k` Taylor coefficient of band `ell` for `u^i v^j` is the coefficient of `X^(ell+k) Y^k` in `X^(5i)(Y+X^-1)^j`. No `math.comb`. Jet counts `r_ell=max(0,ceil((5ell-h)/12))` are the contract already gated against the public `make_band`; pins use order `t_power-ell` with the constant `-value`.
- **Physical rows** by all-pairs convolution over all `571*1551=885,621` P/Q pairs: multiplier `i*s-j*k`, slot `(i+k-1, j+s-1)`, monomial `(pid,qid)`, with a duplicate-monomial check. This differs from the producer's per-output forced-Q lookup. 3,737 slots carry nonzero polynomials.
- **Envelope** derived from the enumerated support extremes, not copied: `I<=15+25-1=39`, `J<=60+100-1=159`, `I+J<=198`, `5I-J<=36`, giving 3,792 slots; every nonzero convolution slot lies inside it, so 55 slots are provably zero and must appear as literal zero rows.
- **Guard** as the explicit cubic `[1, (id(15,60), id(25,100), id(Z))] + [-1, ()]`.

Comparison is per row: label, kind, metadata, then the decoded term multiset as exact `Fraction`s (reduced literal, positive denominator, nonzero, in-range ids, no duplicate monomial) against the expected multiset. Header equality includes the pinned builder hash, the three source hashes, the spec, `Q`, `dp`, source counts and the canonical authority digest `42781305c771397aabead615c75b01b973e9a2d83430133b249cc140c82d853d`, which I recomputed from `authority.json` (file SHA `9c326201…7827a`). Footer checks recompute counts, zero counts, term counts, unused ids and the prefix SHA-256 over every prior byte, then require EOF. Each line must equal its own canonical re-encoding.

The Singular text is parsed line by line with a restricted grammar: exact banner; `ring R=0,(…),dp;` whose name list must equal the JSON names in order; `ideal I=`; for each JSON row a `// label` line and one polynomial line that is `0` or `+`-joined atoms matching `\((-?int)/(posint)\)(\*name)*`, terminated by `,` or, for the last row, `;`; then `// COMPLETE prefix_sha256=<footer digest>`, `print("D125_IMPORT_ONLY_NO_SOLVE");`, `quit;`, EOF. Names resolve to JSON ids; parsed terms must equal the JSON row exactly, including literal numerator/denominator strings and order. Any other byte or line fails, so hidden commands are excluded by construction rather than by keyword search. No second Singular import was run.

The fixed-Q ideal-equivalence theorem of the source-contract gate is used only to relate these ordinary rows to the transformed public contract; no Laurent convolution was expanded.

## 3. Whole-row result on the full stream

Inputs hashed inside the capped run and again after it: `complete/literal.jsonl` 20,560,987 bytes, SHA `8a059438a525a9cc53bb55163dfe74e4931c4dca10f111a2466672ae99fcaf52`; `complete/import.sing` 23,373,677 bytes, SHA `9b6eb808aee27e08f0ee7b263755cefa7e9463c3d8ebd4b03b0664cb57563f4d`. Both match the pilot and `custody.json`.

| Measured on this exact stream | Value |
|---|---:|
| JSON lines (1 header + 2,123 variables + 3,987 rows + 1 footer) | 6,112 |
| Rows matched coefficient-for-coefficient: jets / pins / physical / guard | 189 / 5 / 3,792 / 1 |
| Terms: jets / pins / physical / guard | 3,266 / 86 / 875,119 / 2 |
| Zero rows (all physical, all present as literal zero) | 55 |
| Unused variable ids | 378 `P_u0_v0`, 1,601 `Q_u0_v0` |
| Prefix SHA-256 recomputed | `da8f3cc8339b67566f3fe5a4e63038fafb5dbb2254202a12e68a7b5be00f4b80` |
| Singular lines / atoms parsed | 7,980 / 878,473 |
| Term order identical between my convolution, JSON and Singular | yes |

Every physical row equals my convolution result; the `J_u0_v0` row carries the bilinear terms plus `-1/5`; the guard row is exact; all 189 jet and 5 pin rows equal the power-table rows. The header's `normalized_equivalence_status` is still `PROVISIONAL_UNLICENSED`, as the pilot states. Producer counts 3,987 / 875,119 / 55 / 378 / 1,601 are therefore reproduced by an independent construction, not only by the producer's self-replay.

## 4. Changed-object controls on the full stream

Each JSON control mutates one object and then **re-synchronises the footer** (counts, zero counts, term counts, unused ids, prefix digest), so a checker that only verified internal consistency or the old hash would accept it. All 17 were rejected with a semantic reason before any digest comparison:

- coefficient sign flip and doubled determinant in `J_u0_v0`: coefficient mismatch;
- guard row removed: footer appeared where the guard was expected; guard constant removed: coefficient mismatch;
- target `-1/5` removed and target sign flipped: coefficient mismatch in `J_u0_v0`;
- pin value `9/5 -> 7/5`: mismatch in `pin_4_Q_ell25_t35`; one binomial changed: mismatch in `jet_P_ell1_order0`;
- variable exponent swapped (id 1) and variable renamed (id 2): variable record drift;
- footer `complete:false`, footer removed, trailing JSON line, trailing partial byte: each caught at its own check;
- first zero row `J_u0_v158` omitted and last physical row `J_u39_v159` omitted: label mismatch;
- header field `Q -> Fp`: header drift.

Twelve Singular controls were rejected likewise: atom sign flip and target atom removal (polynomial differs from JSON), guard rows removed with a repaired terminator (previous row terminator), ring variable renamed and two ring names swapped (ring list differs), `dp -> lp` (grammar), COMPLETE marker removed, `ideal J=std(I);` inserted before `quit;`, `;ideal J=std(I)` appended inside a polynomial (atom grammar), text after `quit;`, zero row `J_u0_v158` omitted (label mismatch at row 352), a polynomial split across two lines (terminator).

These are instrument controls for my checker on real data. They are not mathematical statements.

## 5. Toy shakedown (not independent certification)

Before the remote run, the checker was exercised locally on a toy stream produced by the producer's own `--mode toy --singular` fixture (18 variables; rows 27/5/14/1; zero rows 13 jets, 1 physical; unused ids 3 and 11), solely to test my code paths. Whole-row JSON and Singular checks passed and 28 of 29 controls were rejected; `jet_binomial_changed` could not be constructed on the toy because no toy jet has two terms. On the full stream all 29 controls were constructed and rejected. The producer's `test_exporter.py` was read but not used as evidence.

## 6. Custody, cap and measurements

Identity captured before the run in `identity.pre.json` (SHA `c09c62a1b93abfb975f5ab3413da5293b343122a4a13a8ac8e354ae722eed5cf`): Linux hostname `ip-172-30-0-56`; DMI vendor `Amazon EC2`, asset tag `i-0da0cebfc97c9fd54`; IMDS instance id `i-0da0cebfc97c9fd54`, local IPv4 `172.30.0.56`; boot id `235391e8-e646-4ac8-b319-8e609c031bf4`; cwd `/home/ubuntu/d125-full-stream-gate-fable5-20260906`, real path identical, on `/dev/nvme0n1p1 ext4 /`, EBS serial `vol0eb6450d18ffa89f1`. IMDS tag access returned 404, so the owner tag `coordinator-factored-jacobian-20260906` is taken from the pilot's local `ec2.json` record, not re-read from AWS. Pinned copies rehashed remotely before launch: `run_capped.py` `4435279d…`, `exporter.py` `a8092908…`, `authority.json` `9c326201…`, `complete/manifest.json` `f7e176b4…`, and the uploaded checker `b175ccc7…` equal to the local file.

One CAPRUN run, remote-clock times, argv SHA `907c95e3013bc16026b39fd5d604234c6549078ddd60e976edc86154b9f4ae8a`:

| Item | Value |
|---|---|
| Caps | 600 s wall, 8 GiB sampled group RSS, RLIMIT_AS 8 GiB set by the checker |
| Status | `NORMAL_EXIT`, child 0, stderr empty |
| Wall | 41.659 s (21:59:53.914Z to 22:00:35.574Z) |
| Peak sampled group RSS | 463,618,048 bytes; checker `ru_maxrss` 461,056 KiB |
| Process | PID/PGID 3079, `start_ticks=153555`, same boot id |
| Stage times | expected build 1.07 s, JSON 3.91 s, Singular 6.41 s cumulative, controls to 41.4 s |

Neither cap fired; there was no retry or enlargement. After exit the PGID 3079 member count was 0 and runner PID 3078 was gone; producer inputs rehashed identical, still mode 444 with unchanged mtimes, and nothing under the producer directory was created or altered. Same telemetry caveat as the pilot: `leader_reaped=false` and `cleanup_complete=null` are the normal-branch defaults; my explicit post-run group check is the quiet evidence. Retained remote artifacts: `results.json` SHA `8445ff15739871628470c19b8a03740185fba5916962a9afcb8729426beb3efb`, `gate.telemetry.json` SHA `3e94804618631a4fa2d7409c40231db95d1500d9e75fdaba17c2794e47e260f3`, `gate.stdout` SHA `e5d13a2d…6af3d8a` (`{"status": "PASS", …}`); copies under `box/d125-full-stream-gate-fable5-20260906/remote/`. No instance start/stop/terminate/retag, other worker or key was touched.

Root replay command (from the gate directory on `.56`, cwd pinned):

```
/usr/bin/python3 /home/ubuntu/d125-physical-export-pilot-20260906/run_capped.py --wall-seconds 600 --rss-bytes 8589934592 --stdout-file <dir>/gate.stdout --stderr-file <dir>/gate.stderr --telemetry-file <dir>/gate.telemetry.json --cwd <dir> -- /usr/bin/python3 <dir>/gate_check.py --spec d125 --jsonl /home/ubuntu/d125-physical-export-pilot-20260906/complete/literal.jsonl --sing /home/ubuntu/d125-physical-export-pilot-20260906/complete/import.sing --authority /home/ubuntu/d125-physical-export-pilot-20260906/authority.json --out <dir>/results.json --as-bytes 8589934592
```

with `<dir>=/home/ubuntu/d125-full-stream-gate-fable5-20260906`; a fresh replay must use a fresh output directory.

## 7. Boundaries

- The confirmed object is the literal normalized presentation over `Q`. Its relation to the original chart is root's promoted char-0 field-point/nonemptiness licence; no ideal, scheme or mod-p equivalence is asserted or checked here.
- Row labels, variable order, JSON layout and header strings are the producer's format contract; I verified them as a contract, not as mathematics. Spec constants were taken from the reviewed client-interface and normalization reports, not from `exporter.py`.
- Successful whole-row equality says nothing about rank, dimension, properness, a unit, a point, a counterexample pair, solver behaviour or any degree-125 lower bound.
- Singular runtime parsing remains producer evidence (its 26-byte marker stdout); this lane certifies only the file's content.

All arithmetic writers of this lane are terminal. Root retains every instance and promotion decision.

<!-- BODY-END -->
