# Frozen split/resume preregistration

Frozen at `2026-08-28T10:26:30Z`. This successor separates recovery of the
already emitted `lambda_0_full_qgates` packet from compilation of
`lambda_1_full_qgates`. The predecessor ended with
`NO_VERDICT_Q_COMPILE`; none of its bytes carries a mathematical verdict.

## Immutable inputs and programs

- The six copied lambda=0 files and their exact sizes/hashes are frozen in
  `SOURCE_ORIGIN.json`. The JSON system hash is
  `7c4beff1ec5b6e64fafcf800d965e2ea614bcd5d53d14195551f5322f418ab78`.
- `validate_emitted_qgate.py` SHA-256 is
  `54af9aac42385524951fd5228502fbb55dd64ad0436ebfc8a6091b5edd546c16`.
  It must replay the frozen bytes, canonical JSON encoding, all 263 embedded
  equation hashes, source pins, and byte-for-byte regeneration of all five
  Singular scripts before lambda=0 reduction begins.
- `compile_lambda1_slice.py` SHA-256 is
  `624dbdde607891769c0b692b6cdfc7f8b6c4b967568155186e1c6a3572dae396`.
  It imports frozen `compile_q_gates.py` SHA-256
  `b487d8b532d303421386c66638a6d7953aa5a4dcf74208cd07c6db885c511201`
  and compiles only the literal lambda=1 full q-gate system. It may not
  compile lambda=0 first.
- The exact reducer is unchanged, SHA-256
  `47d644bf803dfc2c3e65b57110aca8e4ae32a878794b9def6787adf21f4128b6`.
- Every shipped dependency and input is pinned by `SOURCE.sha256`; the whole
  extracted source tree is independently frozen at launch.

## Separate jobs

1. `resume_lambda0` runs on audited r6a, hostname `ip-172-30-0-34`, Amazon
   EC2 `r6i.16xlarge`, instance `i-02cb2b4a379ffcc64`, namespace
   `/home/ubuntu/jobs/ggv_q1_fixed_split_lambda0_resume_r1_20260828T102630Z_r6a`.
   It validates the recovered packet, then reduces that exact JSON without
   invoking either q-gate compiler.
2. `compile_lambda1` runs independently on audited r6d, hostname
   `ip-172-30-0-45`, Amazon EC2 `r6i.16xlarge`, instance
   `i-07eeaf8ba6f0bc419`, namespace
   `/home/ubuntu/jobs/ggv_q1_fixed_split_lambda1_compile_r1_20260828T102630Z_r6d`.
   It desk-checks the low-prefix identities and source pins, compiles only
   lambda=1, validates/regenerates the emitted packet, and then reduces it.

Each job has its own 7,200-second hard master cap, one pinned CPU, 64 GiB
address-space cap, 16 GiB output-size cap, fresh PGID/SID registry, 10-second
resource monitor, no-orphan cleanup, Linux/Amazon EC2/job-tag/host/instance
checks, at least 450 GiB available-memory gate, and exact zero-swap gates
before and after every stage. Any active-job conflict is a fail-closed refusal.

The exact launch entry points are:

```text
aws_run_remote.sh /home/ubuntu/jobs/ggv_q1_fixed_split_lambda0_resume_r1_20260828T102630Z_r6a resume_lambda0
aws_run_remote.sh /home/ubuntu/jobs/ggv_q1_fixed_split_lambda1_compile_r1_20260828T102630Z_r6d compile_lambda1
```

## Frozen classifications

- A nonzero exact constant compatibility row produced by the sequential
  rational RREF is `EXACT_Q_TRIANGULAR_CONSTANT_OBSTRUCTION`.
- If all three modular reduced ideals are unit and the exact tracked Singular
  run reports `UNIT=1`, `BASIS_REPLAY_ZERO=1`, and `UNIT_REPLAY_ZERO=1`, the
  classification is `EXACT_Q_UNIT_REDUCED_WITH_REPLAY`.
- Any validation disagreement, source/preregistration drift, timeout, resource
  violation, reducer failure, modular nonunit, or incomplete exact replay is
  `NO_VERDICT` with a specific terminal marker. A modular nonunit is not a
  survivor.

These are necessary q1..q13 de Rham gate systems licensed by the full tail;
they do not contain the raw D0..D22 endpoint equations. Exact emptiness can
exclude the corresponding literal fixed slice, but a nonempty or unfinished
screen produces neither a raw endpoint survivor nor a certificate of
existence. Lambda=1 is explicitly diagnostic: no nonzero-lambda normalization
or raw-window shear is claimed.

## Scope firewall

The jobs do not enter or inspect `jc2-lean`, do not mutate top-level canonical
files, do not consume peer ideation submissions, and do not alter the live
HENS-CT or arbitrary-Q origin namespaces.
