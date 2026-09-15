# <Exact claim or research question>

Producer: <swarm or human; exact model ID>
Date: <UTC>
Basis: <campaign commit>
Evidence tier: <what the evidence supports>
Lifecycle: <DRAFT / PRODUCER-CHECKED / PROVISIONAL>

## Statement and scope

State the claim, ambient objects/rings, assumptions, and excluded stronger readings.

## Dependencies and prior work

Link accepted claims, source theorems, and relevant earlier attempts. Explain novelty
or label independent replication. Specify all unreviewed dependencies.

## Argument or computation

Give the proof or exact computation. Distinguish necessary conditions from source
realization, imported claims from internal proof, and finite tests from uniform claims.

## Replay and negative controls

Commands from the repository root, engine versions, input hashes, seeds/primes,
execution environment, UTC times, expected results, and meaningful negative controls.
Write `desk-only` if no computation is needed. Link the artifact README and manifest.

## Limitations and next test

What remains unproved? What would change the next research decision?

## OPENS RAISED

None, or each `OPEN[NAME]` with an explicit bounded quantity and its cheapest test:
instrument, prerequisite gate, and estimated time.

## COLLISIONS

Replace this section with the complete output of:
`python3 ops/open_collision.py <this-report> --root .`

Append the literal closing marker described in COORDINATION.md only when the report
is finished. This template deliberately does not include a premature closing marker.
