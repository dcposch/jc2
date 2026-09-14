# D125 exact-Q solver caller and certificate checker — code preparation

Status: **IMPLEMENTED_PREP_ONLY / PROVISIONAL / NO SOLVER AUTHORITY.** Author `/root/model_productivity`, 2026-09-07. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.

Implemented the accepted bounded plan `xmodel/d125-small-exact-solver-prep-astra-20260907.md` (SHA `fdcd592734d19bfdc33a206ccf7b21f3b146f73581af0bd3d7be202df81d878c`) in new owned `box/d125-small-exact-solver-code-prep-20260907/`. Only small standard-library controls ran. No production source arithmetic, CAS, AWS/SSH, worker write/control, live peer material or protected project access occurred.

## 1. Executable boundaries

`driver.py` has separate `engineering_control` and `solver` authority modes. Both require explicit root GREEN, a nonempty job, exact local code/source/runner/binary/registration pins, Linux/Amazon EC2 instance `i-0da0cebfc97c9fd54`, exact boot and exact future cwd `/home/ubuntu/d125-small-exact-solver-20260907`, plus a bounded registration deadline. No authority file was created. The local checkout fails the production host/cwd checks.

The control branch emits only the tiny fixed ideal `(0,x,0,x,1-x,0)` and its direct `lift` to1; its generated text contains no `slimgb` or `std`. This deliberately includes leading/interior/trailing zeros and a duplicate. `check_control` can validate its later actual output against all six literal rows. The executed local control of that checker used an explicitly synthetic stream, not Singular.

Solver mode additionally demands an accepted full-stream-gate pin and accepted indexing, output-limit and descendant-control pins. Decision and verification are distinct CLI phases, not an automatic chain. The decision phase copies only the immutable source's ring/ideal prefix and replaces the unique import-only suffix. The full original source files remain untouched. There is no alternate ring, subset, field split, gauge, compression, row deletion or second solver command.

The source JSONL SHA is `b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`; Singular SHA is `c089c33301e3889e0c20527386719f411907cf2957ecfad3d93c65f7be24e718`. Exact269 variables/803 rows and unequal/Q/global-dp labels are checked. The literal803 row labels and polynomial values must match the hash-bound JSONL; every source equation, including249 zeros and all guards, reaches the verifier. No full production file was parsed locally.

CAPRUN remains pinned unchanged at `4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2`; Singular at `90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`. The payload must be its own PGID leader with the exact CAPRUN parent, records PID/PGID/start ticks/boot, applies limits, then `execve`s Singular without creating another session. Caller, argv, source-after hashes, generated-input hashes, output hashes and runner telemetry are retained through exclusive files.

## 2. Certificate and cap implementation

The sole decision footer uses `option(redSB); short=0; ideal G=slimgb(I);`, prints the complete indexed engine-I and G lists, and ends the G block before conditional lifting. It reports both `size(I)` and `ncols(matrix(I))`; neither is presumed to equal803. On a constant basis it attempts `lift(I,ideal(1))` and prints all indexed T entries and a dimension-checked direct product. Conditional lift shares the original300-second cap and may recompute internally; it has no fresh allowance.

Decision300 seconds, verifier120 seconds,16GiB AS and sampled aggregate-group RSS, one requested thread; each phase is bounded by the registration's remaining450-second total deadline. Engineering control is at most10 seconds/512MiB. CAPRUN supplies inherited per-process CPU and wall/group cleanup; its RSS measurement is sampled, not a hard instantaneous aggregate limit.

The payload sets inherited `RLIMIT_FSIZE=64MiB` and core size0. The two registered output streams per phase are thereby individually bounded; the generated input also has an explicit2MiB ceiling. No Singular write/link/system/library calls are emitted. Small caller/identity/receipt/telemetry files are separate, so this is not an externally enforced whole-directory byte quota. Actual FSIZE overflow and descendant behavior remain unexecuted pending AWS authorization.

`exact.py` uses rational sparse polynomials, an explicit recursive-descent parser (no eval), and the displayed-variable global degree-reverse-lexicographic order. Only ordinary nonnegative powers and constant denominators are accepted. The parser intentionally rejects exponents above10000; rejection is inconclusive, never an ideal verdict. Output must have complete ordered I/G/T blocks, exact source/ring digests, no unknown variable or trailing material, empty stderr and a final marker. The verifier also checks normal CAPRUN status, rc, exact recorded child identity and output custody hashes.

For a unit, engine polynomials map by exact equality to their first identical original row; duplicate contributions are added and missing zero positions padded. The checker expands the rational identity against the full803-row original vector and accepts only literal1. It does not trust a `[1]` display or the internal matrix check.

For properness, it verifies Buchberger S-pairs, a nonzero normal form of1, and zero normal form for every original equation. This certifies `I subset (G) != R`, which suffices for I proper; it does not claim reverse inclusion or a reduced basis without checking it. No modular or dimension-based properness rule exists. Partial/capped/invalid streams fail closed and remain raw retained candidates; no timeout or failed lift becomes a verdict.

## 3. Executed tiny controls and immutable pins

Final normal and `-O` batches each passed **17 unittest methods**, including multiple actual altered-object subcontrols. Total batch wall0.510823 seconds, child CPU0.512681 seconds, peak child RSS29,456KiB; local limits were30 wall/25 inherited CPU seconds/512MiB. Earlier small development runs also completed normally and are not production experiments.

Controls cover explicit rational parsing and forbidden syntax, dp order, genuine unit with leading/interior/trailing zeros and duplicates, duplicate-cofactor aggregation, altered cofactors and engine equation omission, genuine proper and strict-superideal certificates, missing original equations, source-coefficient/fixed-zero/label/order drift, resynchronized row omission and golden-coefficient corruption, truncated/reindexed/resynchronized result blocks, wrong source/ring bindings, missing authority/gate/control pins, wrong host/boot/cwd, and control-versus-solver isolation. All enforcement checks use explicit exceptions rather than removable `assert` statements.

The false-proper negative control is `G=I=(x^2,x*y-1)`: raw generator reductions vanish and `NF_G(1)=1`, but the S remainder is x, so the checker rejects it. No claim rests on these two insufficient checks alone. The synthetic engine control also checks a five-column engine list against the six literal rows, demonstrating mapping without pretending its indexing is observed Singular behavior.

- `exact.py`: `ca7630e39cb8c5b4aec671b2a83132502abd716c6826c30a4bbc03014ffdb6b3`.
- `driver.py`: `7f081576ea72005c2509ef2d575aa63b9fd53416987f3535ed520fd79fdc130d`.
- `test_exact.py`: `e1f0d6d0c0a930d8f1a2dc17709c98fd1bb37669564c1d09b2be6251a87dd588`.
- `run_tests.py`: `90f3ae5e24c51a893af232b911d9baafb9b8f60ece1a5349807fa3332b94cd04`.
- `test-results-final.json`: `3a8e9b3bb37d7d5f170859e6de8178f40226539078b16f0c87f406a2e60cdc2e`.

Replay tiny local tests: `python3 -B box/d125-small-exact-solver-code-prep-20260907/run_tests.py`. With a new explicit root authorization and deployment only, future worker commands are `python3 -I -B driver.py launch --phase control --authority control.authority.json`, then separately authorized `--phase decision` or `--phase verify` with the solver authority. These command descriptions do not supply authority or launch anything.

## 4. Remaining gates and terminal custody

Still required: root review of this provisional code; acceptance of the independent complete-stream gate; actual AWS-only Singular zero/duplicate indexing, `ncols/size/I[k]/lift` correspondence and explicit/long polynomial printing controls; actual inherited FSIZE overflow on stdout/stderr; fresh reviewed CAPRUN caller/orphan/descendant controls; fresh machine/boot/Owner/EBS/free-space/process-owner audit; and a distinct explicit solver GREEN. The helpers do not automate AWS readiness/ownership or final all-group-absent audits. These are operator duties under the registered task, not claimed completed by the code.

The source parser, suffix serializer and certificate checker have only tiny synthetic tests, not a full-client or independent certificate replay. Their publication does not promote a mathematical result. No basis, cofactor for this actual client, point or counterexample has been produced.

Read perimeter was the accepted preparation, terminal source exporter/header, terminal pilot/custody/telemetry and the already terminal certificate helper machinery. No live Fable gate output/code/receipt was inspected. Root retains the instance and sole complete streams on EBS; no remote directory was created by this task. All local test children exited, no retained PGID or writer remains after sealing. **STOP/IDLE.** Compact custody and pending controls are recorded in the owned box's `custody.json`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9543`.
- Body SHA-256:
  `488c1b6e70b9250e1bb73d613154b431fa944364e1e1641ca5cb0d69db2f51dc`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
