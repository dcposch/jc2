# Characteristic-degree lane, 2026-09-05

The report is `xmodel/char-degree-instrument-astra-20260905.md`. This folder
contains the exact source audits, immutable inputs, derived equations,
finite schedules, controls, and fleet receipts used by that report.

## Mathematical entry points

- `source-audit.md`: Moh printed pp150–159,169–174; attained characteristic
  degrees 55/63, complete five-target family, scalar-unit and total-top rows.
- `nondegeneracy-theorem.md`: full source D2 faces plus attained degree
  exclude every identically zero Jacobian point, not only the cone vertex.
- `full-characteristic-keller-theorem.md`: the full compatible effective
  sequence, with actual total degrees, forces Keller for unequal two-point
  tops. The finite drivers impose T2 only.
- `front-band-lemma.md`, `cubic-front-improvement.md`,
  `review/quartic-front-improvement.md`, `stage-specific-front-audit.md`, and
  `d108-stage-front-audit.md`: proved radical preprocessing with all original
  rows retained. No new gauge or variable inversion is introduced.
- `remainder-backend-audit.md`, `coefficient-circuit-audit.md`,
  `review/circuit-review.md`: exact row-ideal and coefficient-graph proofs.
- `d108-mean-coverage-audit.md`: a missing mean in the frozen chart, and the
  supplementary arbitrary-quadratic repair. This is independent of the
  safe algebra-only translation described in `d108-algebra-translation-audit.md`.
- `family-c/instrument-manifest.json`: the receipt-bound supplementary
  roster has 20 parents/36 typed leaves. It supplies no automatic leaf kills.

Each proof has adjacent exact-Q controls and source digests. The initial
seven charged inputs were mechanically checked before use (`inputs.sha256`,
`hash-check.txt`). The 99 engine snapshots are also bound mechanically to
the artifact manifest named by the frozen report (`g9966/source-parent-binding.*`).

## Full explicit coefficient systems

`d108/coefficient_circuit_backend_v2.py` is a self-contained exact-Q emitter.
Its input declares the original coefficient ring, all original residual
rows, normalized H/D/C source expressions, all five target scalars, and
leader/separation localizers. New coefficients have monic acyclic graph
equations. Every high remainder coefficient and every total-degree/whole
leading-target coefficient is retained. The final ring consists solely of
coefficient variables; physical t,z are extraction indices, not generators.

An emitted input can be replayed on a host with Python, SymPy, python-flint,
and Singular using, for example:

```
python3 box/char-degree-20260905/d108/coefficient_circuit_backend_v2.py \
  --input box/char-degree-20260905/g9966/circuit-inputs/delta2_stage8.input.json \
  --out /tmp/char-degree-replay.sing --timeout 600
```

The lane used exact Q throughout. Algorithm controls include a proper
attained-degree case, a wrong-target unit case, graph elimination compared
with direct expansion, localization controls, and 64 support-bound cases.
The controls deliberately do not claim that their simple example satisfies
the actual D2 source faces.

`g9966/run_circuit_schedule.py` executes all 18 requested 99 branch/stage
combinations with three concurrent 16-GiB processes and a 600-second CAS
limit. `g9966/circuit-inputs/verification.json` independently replays all
gauge and rational graph maps. `g9966/collect_circuits.py` checks input and
script hashes, rings, target variables, exact parsed row counts, and controls.

For D108, `d108/run_circuit_schedule.sh` records the original centered
chart's stages 0–8. `d108/meanfree_stage.py` and
`d108/run_meanfree_schedule.sh` retain the missing quadratic mean and run
the supplementary full-mean chart. `d108/collect_schedule.py` reports both
with explicit scope. The frozen source engine is never overwritten.

Earlier normalized-division and direct-product attempts are retained as
diagnostics. They frequently exhausted memory before full equations existed.
Singular can restart after an allocation failure and then operate on an
incomplete ideal. Every such continuation is rejected; a later printed
dimension or basis message does not repair missing equations. Only complete
hash-bound, error-free, controlled results could prove unit/properness.

## Custody and closeout

All fleet work belongs to instance `i-02703754668abed88`, the single
authorized r7i.8xlarge. Final result summaries and the termination receipt
must be read before interpreting the lane as closed. The final artifact
manifest excludes itself and transient Python bytecode; it includes the
drivers, inputs, proofs, finite-system scripts, logs, and execution receipts.
No mathematical campaign ledger or Lean file is modified by this lane.
