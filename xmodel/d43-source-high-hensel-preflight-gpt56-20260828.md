# D43 raw-source high-Hensel repair packet

Date: 2026-08-28  
Status: **schema-v2 and AWS-custody repair complete; independent rereview required; no AWS launch authorized**

## Decision

The D43 high-order runner is now fail closed against the hostile-review
resume attack and against accidental local `p^3+` execution. It can only
follow the registered deterministic correction chain: every root lift,
right-hand side, left-cokernel syndrome, correction, point, row replay, and
history link is recomputed from the registered mod-`p` state on every resume.
The demonstrated `p`-times-kernel shift with stale history is rejected.

This repair did not run `p^3+`, launch AWS, or repeat the 326 MB real-source
reconstruction locally. The already reviewed `p^2` raw-source evidence is
preserved. New tests and the exact `p^2` E/E5/E6 arithmetic are lightweight.
The AWS target-16 pilot remains blocked until an independent hostile rereview
accepts this packet.

## 1. Exact scope

The runner enforces these finite equations at every successful digit:

- the 184 pristine raw Euler/J-source rows;
- `Phi42(zeta)=0`, `r3^2=3`, `A1^3=3+r3`, `A2^3=3-r3`, and `2h^2=3`;
- `HW1=hW1`, `HW2=hW2`, literal `uf30=0`, and the evaluator's named finite
  completion;
- the necessary relation
  `E=(9+5r3)A1W1^4+(9-5r3)A2W2^4=0`, with `W1,W2` units;
- deterministic witnesses for both corrected-`243` E5 rows and for the
  cube-form E6 row, with `HM` and `s1F` units.

It does **not** replay:

- the 34 parked D21/D23/D25 equations;
- the `W1*uW1-1`, `W2*uW2-1` rows as equations in inverse variables;
- the full template and low-order reconstruction equations;
- the source-to-normal-form or reducer-membership identities.

Therefore a finite pass is a raw 184-row source congruence satisfying a
necessary eliminated E5/E6 tie. It is not a full residue-A/template/D25
point and is not evidence that a D43 template branch survives.

## 2. Source ambient and exact evaluator

The nominal source registry is

```text
4 * 36 dense tails + 2 * 18 even tails + 8 fixed + alpha,beta = 190.
```

The eight `r=39,41` columns in `tf1,tf2,tg1,tg2` are structurally absent
from all 184 selected rows. Every selected band is even and at most 42. An
odd slot 39 or 41 needs another odd source slot, whose minimum is the W/HW
slot 5, so its first possible even totals are 44 and 46. Literal Jacobian
replay also gives eight zero columns. The essential ambient is consequently

```text
172 tails + 8 fixed + alpha,beta = 182 coordinates.
```

At `p=105337`, the source Jacobian rank is 129, with tangent-kernel dimension
53 and left-cokernel dimension 55.

The band-42 x-side formula is an exact support law, not only a base-point
tangent. `U_f=1+alpha*t^42` and `U_g=1+beta*t^42` first differ at slot 42.
Thus every cross term contributing to output slot 42 sees only the slot-zero
constants `S_M,G_M`; any positive y slot overshoots, `alpha*beta` begins at
slot 84, and lower rows are unchanged. The preflight includes alpha and
beta basis controls and a simultaneous nonzero `(alpha,beta)` control after
four y/fixed perturbations, replayed against the independent operator path.

## 3. Schema-v2 semantic chain

The state schema is `d43-pristine-source-high-hensel-state-v2`. Its initial
exponent-one state is deterministic. Every transition records and seals:

1. the exact input frame, point, 184 rows, and necessary E/E5/E6 gate;
2. every coefficient-root digit and defining-equation digest;
3. the full `-F/p^n` right-hand side;
4. all 55 left-cokernel pairings and any explicit obstruction vector;
5. the full deterministic correction, with all 53 free digits zero;
6. the corrected point, all 184 zero rows, and the output E/E5/E6 gate;
7. previous-record, record, and prefix-history hashes.

Resume validation reconstructs the initial state and every complete
transition, then exact-compares the full canonical payload. It accepts a
genuine obstruction at the first attempted digit if and only if fresh replay
reproduces it. It rejects altered coordinates, roots, history, status,
scope, policy, claims, invariants, or `p^2` anchor even if a new JSON envelope
hash is supplied.

The registered first transition pins the actual frame, RHS, correction,
point, and E/E5/E6 gate hashes. The kernel-shift hostile fixture remains in
the test suite behind `JC2_D43_HOSTILE_REAL=1`; lightweight schema fixtures
exercise the same stale-history attack by default.

## 4. Exact p2 E/E5/E6 check

For `p^2=11095883569`, the reviewed corrected point has

```text
r3 = 11012141449       A1 = 786496672       A2 = 8038065910
W1 = 10092159227       W2 = 4041263462      gcd(W1,p^2)=gcd(W2,p^2)=1
```

The two terms of E are `4315102731` and `6780780838` modulo `p^2`; their
sum is exactly zero. With the corrected E5 coefficient `243=3^5`, the two
E5 equations independently give the same unit

```text
HM = 5143408652 mod p^2,
```

and both E5 residues are zero. Taking

```text
s1F = 2^8 * HM / 7^16 = 9120266557 mod p^2
```

gives a unit and makes `2^24 HM^3 - 7^48 s1F^3` exactly zero. The complete
gate digest is

```text
39702f29d6e1a0b6f45864eca343b555620b41d8cb747b60bca057b3799804e3.
```

Algebraically, on the registered radical locus with `W1W2 != 0`, the two E5
rows admit a common `HM` exactly when E vanishes: eliminating `HM` gives E
up to a registered unit. `HM` is then a unit. E6 adds no projected
condition because its coefficient ratio is already the literal cube
`(2^8/7^16)^3`, so the displayed `s1F` is an explicit solution.

This is set-theoretically equivalent over `C`. It is also pointwise
equivalent over `Z/(105337^N)` and `Z_105337`, not stronger there, because
`2,3,7,a_i-4` and the registered radical/chart values are units. Over an
unlocalized coefficient ring where those denominators cease to be units,
the existential formulation can be stronger. The cube equation may have
additional root-of-unity choices, but existence and the projection to the
W-coordinates are unchanged. None of this proves that the raw 184 rows
force E at all higher digits; the runner checks it after every correction
and terminates with a distinct template-gate-failure status if it breaks.

## 5. Route-specific AWS custody

`cases/d43_source_high_hensel_aws_supervisor.py` and the exec-only worker
shim enforce the registered route. Direct runner requests above `p^2` are
rejected unless they carry the supervisor's parent-bound authenticated
authorization envelope. The route permits only target 16, followed by
target 64 from an authenticated exact target-16 state.

For each job the supervisor requires and records:

- Linux, Amazon EC2 DMI and IMDSv2 identity, exact hostname, instance ID,
  `c7i.xlarge` type, job ID, lane tag, and target;
- exact preregistration, payload-manifest, runner, worker, supervisor,
  dependency, certificate, and input hashes;
- an isolated Python invocation (`-I`, empty `PYTHONPATH`, no user site) and
  one-thread numerical-library environment;
- exact argv, Python binary/hash/version, NumPy version, host and job hashes,
  source archive hash, and durable paths;
- a 1200-second wall limit, process-group RSS at most 2 GiB, global and
  process swap exactly zero at every 10 Hz sample;
- one payload process only, no escaped descendants, foreign group members,
  or surviving orphans.

Any custody, resource, interruption, child-exit, output, or scope fault kills
the contained processes and atomically emits `NO_VERDICT_CUSTODY_FAULT`.
Success and failure bundles include a terminal manifest, deterministic
source/evidence archives, state snapshot, telemetry, and SHA sidecars.

## 6. Tests and evidence status

The lightweight suite covers exact RREF/cokernel solving, radical lifts,
coordinate census, the dead-tail proof, exact `p^2` E/E5/E6 values, semantic
chain tampering, a forged and a genuine exponent-one obstruction, manifest
tampering, direct-route refusal, process topology, swap parsing, and
deterministic evidence archives.

```text
python3 -m unittest -v \
  cases/test_d43_source_high_hensel.py \
  cases/test_d43_source_high_hensel_aws_supervisor.py

23 tests: 22 PASS, 1 real-D43 hostile replay skipped by default.
```

`py_compile`, worker `bash -n`, and the pure selftest pass. The historical
real `p^2` replay and the hostile review independently found 184/184 rows
zero, rank 129, zero cokernel syndrome, the registered correction hash, and
the registered corrected-point hash. The repair phase deliberately did not
rerun that heavier reconstruction; its provenance is explicit in
`cases/d43_source_high_hensel_p2_replay_20260828.json`.

## 7. Launch status and finite interpretation

The route is implementation-complete but administratively blocked pending
independent hostile rereview. After a PASS, the first authorized experiment
is target 16 on one `c7i.xlarge` (4 vCPU, 8 GiB), effectively one compute
thread, zero swap, 2 GiB RSS cap, and 1200 seconds. Target 64 is a separate
job and is legal only from the exact authenticated target-16 state.

A target-16 or target-64 pass would certify only a finite raw-source
congruence along the deterministic zero-free-digit chain, plus the finite
E/E5/E6 tie gate. It would not certify parked/source equivalence, a full
template/D25 point, indefinite solvability, formal smoothness, a `Z_p` or
characteristic-zero point, a formal germ, an ambient polynomial Keller map,
or a JC2 counterexample.
