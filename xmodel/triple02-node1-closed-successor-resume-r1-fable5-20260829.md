# TRIPLE02 node-1 closed-successor resume R1 — source producer report

Author: Fable 5 (source producer, not reviewer).  Date: 2026-08-28
(packet dated 20260829).  Working directory: `/Users/dc/code/math/jc2`.

Deliverable: the fresh directory
`cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r1_20260829/`
(a source-only, AWS-ready, fail-closed resume packet) and this report.
Nothing was launched, no CAS was run, no existing file was modified, no
ledger was edited, nothing was committed, and `jc2-lean` was not touched.

## Verdict

**`SOURCE_PACKET_READY_FOR_DIFFERENT_MODEL_REVIEW`**

No AWS authorization is claimed.  A hostile source review by a different
model, plus a coordinator `GO`, are mandatory before any launch.

## 1. Mathematical scope

The packet resumes the frozen r5 exact finite Fitting/chart recursion on the
TRIPLE02 node-1 **closed successor**

`V(I_node1 + (Delta_node1)) ⊂ Spec(Q[q0,q2,c4,c6])`, `dp` order,

starting directly at global node 2 with the three literal generators

| generator | SHA-256 of literal |
|---|---|
| g1 = TRIPLE02 branch factor | `2b9d29b706ce5d7e58e2dc5a28799782f5610c5ccb7b71987ebd694fd8b83206` |
| g2 = root chart delta | `fecd1d43f3f55e1c65bec858303b7688c0db83dbe9c3a60f51f70130a4149336` |
| Delta_node1 = archived size-6 witness NF (rows 1,2,4,7,9,11; cols 1,2,3,5,6,7) | `84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02` |

and inherited rank upper bound **6** (provenance: rank archive
`b947a2d3e815…b809`… exact: `b947a2d3e81525902a93500026020c2cf9580f070767757389daadb9a6bbe3b2`,
certificate member
`cc6dc1c4edbceeecf31c17b96ab9a0ac9744720100e7bf3f20ba41c4e4cd99d2`).
The node-1 open saturation is neither recomputed nor depended on.  The four
preregistered terminal classifications (exact dead on finite cover /
ring-level survivor pending nilpotence-radical / bounded no-verdict
remainder / reverse-containment exhausted) are chart-local to the closed
successor; ideal equality, saturation equality, ring-level endpoint
nonvanishing, radical/nonemptiness, and geometric existence are kept
separate, and no whole-component or JC2 inference is possible from any
terminal.

## 2. Frozen sources used (all hash-verified this session)

| artifact | SHA-256 | role |
|---|---|---|
| R3 terminal archive `…endpoint_complements_r3_20260828/custody/terminals/ggv_endpoint_complement_triple02_r3_…i0f089.terminal.tar.gz` | `e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1` | node-1 literals, reduce/rank artifacts, witness, frozen timeout, `work/base` |
| Proper-open r5 terminal archive `…proper_open_resume_r1_20260828/custody/terminals/ggv_triple02_proper_open_resume_r5_…r6d.terminal.tar.gz` | `4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e` | routing provenance only |
| Frozen r5 recursor `…endpoint_complements_r5_20260828/recurse_component.py` | `d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90` | pinned stage-script builders |
| Frozen transcript gate (same dir) | `0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316` | diagnostic-fail-closed parser |

Archived members consumed from the R3 archive (each pinned individually in
`prepare_resume.py`; census 437 members = 374 files + 63 dirs, no
links/devices/traversal/duplicates): `output/INPUT_MANIFEST.json`
(`0025f3ea…`), `output/VERDICT.txt` (`1434d904…`, reads
`ADAPTER_FAILURE_NO_VERDICT`), `output/ADAPTER_FAILURE.txt` (`137d6cd1…`,
reads `RuntimeError:SATURATION_RETURN_CODE:1`), and under
`output/node_001/`: `NODE_INPUT.json` (`b8bf5ec7…`),
`NODE_001_STANDARD_BASIS.txt` (`bd95508c…`), `reduce.sing` (`28385a70…`),
`reduce.result.json` (`6daced55…`), `reduce.stdout.txt` (`85630c0b…`),
`NODE_001_REDUCE_PIVOTS.tsv` (`2edaa006…`), `NODE_001_REDUCE_RESIDUAL.tsv`
(`f24a4a23…`), `rank_size_6.sing` (`9f9e7608…`), `rank_size_6.result.json`
(`ac4a2f1b…`), `rank_size_6.stdout.txt` (`5d181ec4…`),
`rank_size_6.support.json` (`bb8f7ee0…`), `NODE_001_SIZE_6_MINORS.tsv`
(`1c6e57a4…`), `NODE_001_SIZE_6_WITNESS.tsv` (`fa042886…`),
`saturation.result.json` (`4bac1369…`, cap 900 s, rc 1, `timed_out: true` —
the frozen frontier, provenance only), `saturation.stdout.txt`
(`4ee63095…`, six-marker prefix, ends `halt 1`, no completion marker),
plus `custody/Singular.version` (`0d074eb6…`) and the whole `work/base/`
tree (root chart delta file `adaad79c…`, root classification
`ENDPOINT_DEAD_ONLY_ON_D_DELTA`, upstream inputs, rank archives).
**Never extracted:** `NODE_001_OPEN_SAT_STANDARD_BASIS.txt` and
`saturation.sing` — the settled open-route products; the preparer fails if
they appear on disk.

From the proper-open archive (census 565 members, same safety checks), only
`output/VERDICT.txt` (`75645210…`), `output/SUMMARY.json` (`a976536e…`),
`custody/CANDIDATE_MATHEMATICAL_VERDICT.txt` (`75645210…`) are extracted;
all must read `EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY` with scope
`TRIPLE02_NODE1_D_DELTA_ONLY` and
`whole_component_or_closed_successor_inference: false`.

## 3. How the closed successor is reconstructed

Four independent bindings, all exercised locally this session:

1. **Literal hashes.**  g1/g2 from `NODE_INPUT.json` (self-consistent
   `generator_sha256`), Delta_node1 from the witness TSV; all three pinned.
2. **Semantic source replay.**  `build_resume.py` imports the frozen r5
   recursor by hash and re-derives g1, the ring `Q[q0,q2,c4,c6]` (`dp`), the
   zero pattern `(q1,c8)` with token counts `{q1:566, c8:6}`, and the full
   106×105 matrix from the archived `work/base` upstream inputs; it then
   reproduces the archived node-1 `reduce.sing` **and** `rank_size_6.sing`
   (and the support census JSON: 97020 formal / 1100 matchable / 36 support
   entries) **byte-for-byte**.  Verified locally: both reconstructions
   matched the archived hashes exactly.
3. **Witness replay stage (host-side Singular, generated now).**  The
   generated `TRIPLE02_NODE1_WITNESS_REPLAY.sing` (SHA-256
   `27cb85082e8ea56a4a9bc8d0cb38b889edc4e981529d6697b0ff2800e0159d0d`)
   re-runs the exact node-1 reducer (95 rational unit pivots, invariant
   gates), after which the classifier byte-compares the produced pivot log,
   residual, and node standard basis against the archived files; the stage
   recomputes `det` of the archived minor, requires exact equality with the
   Delta_node1 literal, nonzero NF, NF-stability, and then forms
   `SUCCESSOR = (g1, g2, Delta_node1)`, checking `Delta_node1 ∈ SUCCESSOR`
   and recording the successor standard basis and emptiness marker.
4. **Rank-bound provenance.**  `r5.verify_rank_bound(base, "triple02", 6)`
   replays the pinned rank archive and certificate member from inside
   `work/base`; the resume input embeds the provenance block and the driver
   re-verifies it at run time.

Node 2's `NODE_INPUT.json` then has exactly the three generators with
inherited bound 6; the node-2 reduce script is generated deterministically
(SHA-256 `d9e79b427dd22718683b2ac3f5f50dbd9839622ee07bf95cb61f02bdd380d8b8`,
byte-identical across two independent local builds and re-required at run
time), and the recursion continues under the r5 contract: reduce → full
support-matchable minor census from the inherited bound downward (explicit
nonzero witness or per-size all-zero certificate) → saturation with
object-shape/inclusion/stability gates → chart with full right transform,
base change (11135 reductions, 11025 recorded entries), all
106×(10−rank) row kernel identities, denominator-cleared endpoint
coefficients, bordered and two-shift plants → descent
`generators + (delta_n)` at bound = found rank.  Maximum 6 new nodes
(2..7); stage caps 900 s (witness replay) / 3600 s (node stages); whole job
21600 s.

## 4. Why the settled open route cannot be re-entered

- **Algebraically**: Delta_node1 generates every node ideal from node 2 on,
  so every chart lies in `V(Delta_node1)`, disjoint from the settled
  `D(Delta_node1)`.  The adapter selfcheck proves the miniature
  (`J=(x·y, y)`: parent delta in `J`, `J` proper, `sat(J, y)` = unit ideal).
- **Structurally**: node numbering starts at 2; the driver never creates a
  `node_001` stage; the classifier rejects any `node_001` directory; the
  node-1 saturation and its 257-step pure-delta power search are never
  generated; the open-route archive members are never extracted.
- **By guards**: every scanned delta at every node is hash-compared against
  Delta_node1 in the builder validators, the driver, and the classifier
  (three independent layers); the settled-open campaign's verdict string is
  explicitly rejected as a foreign candidate by `containment_contract.py`.
- **Repaired hazard**: the r5 saturation template runs the 257-step pure
  power search unconditionally — on a proper open it always does all 257
  growing-power reductions (this is the exact shape of the node-1 timeout).
  The repaired template gates that loop to the empty-open branch (where it
  remains mandatory for the power-membership certificate) and adds
  per-generator reverse-containment witnesses (`NF(OPEN_SB[i]·delta_n^k)`,
  reduced intermediates, bound 64) on the proper branch, so the computed
  saturation is certified by two containments rather than trusted.
  Exhaustion is a bounded no-verdict, never a claim.

## 5. Packet contents and hashes

Case dir `cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r1_20260829/`:

| file | SHA-256 |
|---|---|
| `prepare_resume.py` | `d06acdd3402f45548975414efe99976997b73443fc29fceaf2f01fc96db8f169` |
| `build_resume.py` | `3763ac7a5ce2915ede7c21c9d9b8dcb3fc1ab12075c998daa646a375b640f780` |
| `resume_recursor.py` | `949846b049fbf1e1388ecb3439d40341529509d609f1c68451d955865a950acc` |
| `classify_resume.py` | `b01b0bd8e224838ae150459635634b95e78d86271de1a5f33a57cff143f9f549` |
| `generator_selfcheck.py` | `a417b2fa1b558c4372bd1a8d7cf6fbcab03880df9272904216b6a7ca8dbbe0f4` |
| `run_singular_stage.py` (verbatim from reviewed R5 packet) | `2a19c0e5d605ea938035b29e0cf790dcedfb01d32d4469696c803666958622bb` |
| `containment_contract.py` | `017e18eca22afbaa22e20da34f9e8cc4df92005131856139723594a729441ecd` |
| `containment_selfcheck.py` | `9780ad910a6d6b1a776bff75d71b2562f46f510d3802533c4197f48edc74733f` |
| `adapter_selfcheck.sing` | `e616b59542a977dd9daa6865dbf18b60feaae06f784d98f72cf8cced27ee4490` |
| `diagnostic_hostile.sing` (verbatim) | `01be817524da040ad97eeb52adc461d6556e2d8cd179c9447c4c5101a2f15e02` |
| `aws_job_worker.sh` | `5a49ea1980fe3059eb5e90cf935c804dc2b61893b09fd0121929d810809efb60` |
| `aws_supervisor.sh` | `2ea637754a26dea21966d5a3cca6557d30f4d9fe9a3136061bb2c6a951fa6f56` |
| `aws_launch_preflight.sh` | `22bfc453d9686395d09077516e3b2d73ce21fa31d978ddaa3c27de96ab208136` |
| `runtime_expectations.env` | `2ccea23e01c1113dc9ca95a5839c63e0ada095db4cbc6f790d66901def9ceb6e` |
| `SOURCE_MANIFEST.sha256` (22 entries) | `9d593d61c74f01df39e5b69a3ec4d0d5538e2fa280f2cf9f7a9d4ebcb4f39655` |
| `AWS_PREREGISTRATION.md` | `f7df8caec8b1b95396af4c48adc9ab1db5df4b0427561616523896f787ab0c94` |
| `PREREGISTRATION.md` | `2b302bcc240c0f600b46b4087c3a54dbd7ae417155f9cf1c04fed752233a42a3` |
| `README.md` | `6ff913fdf85e8ddf5dff8c6fc547049bf6000e5ebc24509bc595e4f20e800cd0` |
| `PREFLIGHT_REPORT.md` | `7325936c40796d1d46cd3a0c2981812dabe026e243e9812116976384ff9376a3` |
| source archive `custody/ggv_triple02_closed_successor_resume_r1_SOURCE.tar.gz` (23 file-only members, mode 0444) | `6a4dc35fe31cdbd1ca3eed7064b417e798072d75240e31b60d0e4b70462e6a9f` |

The custody stack is a deliberate near-copy of the R5-PASS proper-open
packet (diff-review against it is the intended review technique): the
supervisor differs only in the case path and the 21600 s whole-job budget;
the contract differs only in `MATH_TERMINALS` and the scope-marker string;
the containment selfcheck adds a foreign-candidate rejection.  The stage
runner never creates a nested session (the frozen r5's internal
`start_new_session=True` runner is *not* used to run stages; only its
script builders are imported).

## 6. Hostile fixtures and outcomes (all run locally, all pass)

- `generator_selfcheck.py`: 20 mutations rejected — R3 archive hash;
  traversal member; open-route member selection; witness delta literal
  (+1); `sat(` injection into witness/node-2 scripts; route-guard marker
  deletion; ring-order permutation; Delta_node1 reuse as scanned delta in
  saturation *and* chart; ungated 257-step power search; reverse-marker
  deletion; post-base-change repivot; kernel/transform count-gate flips;
  transform-record print deletion; classifier driver-verdict swap; chart
  residual byte tamper; endpoint plant marker drop; `node_001` directory.
  Plus dead and survivor classifier positive controls and the
  Singular-diagnostic negative control.
- `containment_selfcheck.py`: 13 late-failure downgrades, detached stage
  child, wrong recorded PGID, launcher start-time mutation, hung-launcher
  bound, zombie reap, cgroup content parsing (empty/nonempty/malformed/
  missing), sticky swap/whole-timeout, terminal-manifest build/replay/tamper,
  valid-outer-hash-bad-embedded-manifest, unexpected archive member, late
  archive failure, nonzero late worker exit, and the new foreign-campaign
  candidate rejection.
- Driver fail-closed dry run: deliberate stage failure produced rc 2,
  `ADAPTER_FAILURE_NO_VERDICT`, exact cause string, and the bounded
  remainder (3 generators, bound 6) — no partial claim.
- On-host (AWS) controls, wired but not yet run: the invalid-list-slot
  diagnostic; the adapter selfcheck (two-containment, strict overideal
  adversary, empty-power route, reducer adversary, endpoint two-shift with
  innocent `e=-1`, bordered plant, closed-successor separation fixture).

## 7. Remaining risks (for the reviewer)

1. **No Singular ran locally.**  The witness replay and every node stage
   execute for the first time on AWS.  Mitigations: byte-identical local
   reconstruction of both archived node-1 scripts by the same builders; the
   archived node-1 reduce took 4.9 s and rank census 0.2 s under the same
   contract; every stage is capped and fail-closed.
2. **Node-2 saturation cost is unknown.**  `sat` on the 3-generator ideal
   may exhaust the 3600 s cap exactly as node-1's did at 900 s; that
   outcome is preregistered as a bounded no-verdict
   (`STAGE_TIMEOUT:<node>:saturation`), not a failure of custody.
3. **Rank-census script size at lower sizes.**  If a node-2+ residual is
   much denser than node-1's (36 entries), the support-matchable census at
   sizes 5/4 could generate large scripts/runtimes; caps and the file-size
   ulimit bound it; a timeout is again a bounded no-verdict.
4. **Reverse-containment bound 64** may be too small for a legitimate
   saturation at deeper nodes — again a preregistered bounded no-verdict,
   never a wrong claim.
5. **Repaired-template splice risk.**  The saturation/chart repairs are
   textual splices on frozen r5 builder output; every splice anchor is
   count-1-guarded (`replace_once`) and the mutation suite covers the two
   highest-risk deviations (ungated loop, missing reverse markers), but a
   reviewer should re-derive the spliced scripts independently.
6. **Environment pins inherited** from the proper-open R5 host (Singular
   4.3.2 normalized version, `elim.lib`); a different AMI fails closed
   rather than running.
7. **`decide_terminal` publishes bounded no-verdicts** (`NO_VERDICT_OPEN_
   REMAINDER…`, `REVERSE…EXHAUSTED…`) as first-class terminals when all
   custody gates pass; a reviewer should confirm this widening of
   `MATH_TERMINALS` (relative to the proper-open contract) is acceptable —
   they are verified bounded outcomes, not mathematical claims.

## 8. Session evidence

Local preflight evidence (with a second independent byte-identical build)
is preserved under the packet's `preflight/` directory; the frozen source
archive replayed cleanly (sidecar hash, 23-member safety census, embedded
manifest verification from a fresh extraction).  No tracked repository file
was modified; the packet directory and this report are the only additions.
