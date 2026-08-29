# Closed-successor resume R1: local preflight report

Date: 2026-08-28 (macOS host, pure Python; no Singular/CAS executed).

## What ran locally

1. `python3 -m py_compile` over all eight packet Python files — pass.
2. `prepare_resume.py` against both real frozen archives — pass
   (`R3_SELECTED_EXTRACTED_FILE_COUNT=294`,
   `SETTLED_OPEN_EXTRACTED_FILE_COUNT=3`, open-route members excluded,
   archived timeout revalidated, settled-open verdict revalidated).
   Evidence: `preflight/R1_PREPARE.stdout.txt`,
   `preflight/PREPARED_INPUTS.json`.
3. `build_resume.py` against the prepared tree — pass, including
   byte-identical reconstruction of the archived node-1 `reduce.sing` and
   `rank_size_6.sing` (+ support census JSON) from the pinned frozen r5
   builders, and inherited rank-six provenance replay.  Evidence:
   `preflight/R1_BUILD.stdout.txt`, `preflight/generated/`.
4. `generator_selfcheck.py` — pass: 20 hostile mutations rejected
   (archive hash, traversal member, open-route member selection, witness
   delta literal, saturation injections, route-guard deletion, ring order,
   settled-delta reuse in saturation and chart, ungated power search,
   reverse-marker drop, repivot, count-gate flips, transform-record drop,
   driver-verdict swap, chart-residual tamper, plant-marker drop, `node_001`
   directory) plus dead/survivor classifier positive controls and the
   Singular-diagnostic negative control.  Evidence:
   `preflight/R1_GENERATOR_SELFCHECK.stdout.txt`.
5. `containment_selfcheck.py` — pass, including the new
   foreign-campaign-candidate rejection (the settled-open verdict string is
   not promotable by this packet).  Evidence:
   `preflight/R1_CONTAINMENT_SELFCHECK.stdout.txt`,
   `preflight/containment_selfcheck.json`.
6. `resume_recursor.py` fail-closed dry run (stage runner cannot run on
   macOS): rc 2 with `ADAPTER_FAILURE_NO_VERDICT`, exact cause
   `RuntimeError:STAGE_RESULT_MISSING:witness_replay`, remainder = the three
   node-2 generators at bound 6.  All pre-stage validation (pinned imports,
   RESUME input hashes, source reconstruction, rank provenance, node-2
   determinism, witness-script hash) passed before the deliberate failure.
   Evidence: `preflight/driver_failclosed_dryrun_SUMMARY.json`.
7. Build determinism: prepare+build were run twice into fresh directories;
   the witness-replay script, node-2 reduce script, and
   `RESUME_NODE_INPUT.json` were byte-identical across runs.
8. Source archive replay: sidecar hash verified; the launch-preflight member
   census (23 file-only members, prefix/type/traversal/duplicate gates)
   replayed; fresh extraction verified all 22 `SOURCE_MANIFEST.sha256`
   entries.

## Pinned outputs

- Witness replay script SHA-256
  `27cb85082e8ea56a4a9bc8d0cb38b889edc4e981529d6697b0ff2800e0159d0d`.
- Node-2 reduce script SHA-256
  `d9e79b427dd22718683b2ac3f5f50dbd9839622ee07bf95cb61f02bdd380d8b8`.
- Source archive SHA-256
  `6a4dc35fe31cdbd1ca3eed7064b417e798072d75240e31b60d0e4b70462e6a9f`
  (mode 0444).

## Known local gaps (disclosed)

- No Singular stage was executed locally; the witness replay, all node
  stages, and the two Singular control scripts run for the first time on the
  AWS host.  The worker re-runs every selfcheck on-host before production.
- The containment suite's `/proc`-dependent paths (`cleanup`,
  `validate-worker`, `cgroup-census` live reads, stage-runner containment)
  cannot execute on macOS; they were exercised through the pure-logic
  fixtures and injected readers only, exactly as in the reviewed proper-open
  R5 flow.
- The Singular normalized-version and `elim.lib` pins are inherited from the
  reviewed proper-open R5 host; a different AMI fails closed before
  production.
