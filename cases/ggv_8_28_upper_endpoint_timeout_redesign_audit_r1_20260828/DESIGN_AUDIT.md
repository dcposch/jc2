# Exact redesign audit for the four R3 endpoint timeouts

Date: 2026-08-28

## Outcome

The highest-information successor is a **proper-saturation dichotomy with a
certificate-carrying chart resume**. It must reuse the exact saturated open basis
already emitted by each timeout packet, branch on whether that basis is the unit
ideal, skip the power-membership loop on every proper open, and evaluate the
endpoint chart before doing any closed-successor recursion.

This is not another variable/term-order variant and does not repeat the 900-second
stage. The audit shows that the four jobs did not time out inside their first or
second saturation: both saturations and their two-way stability comparison had
already completed. All four then entered the same unconditional 257-reduction
power loop after the last accepted marker.

No AWS job was launched during this audit.

## Frozen evidence comparison

| Branch | Ring before inert-variable removal | rank | node input SHA | node SB bytes / SHA | selected-minor witness SHA | open SB generators / bytes / SHA | reduce + rank time (s) | timed stage (s) |
|---|---|---:|---|---|---|---|---:|---:|
| P | `Q[q0,q1,q2,c4,c6,c8]` | 9 | `7ecc7bba0a883a197f78da31a1af7fc0fc54d945b3ed17ce3d0be7c3d4b4dc59` | 2,198,148 / `591cdaadb2a88253c3562c27b15ac2d3c4049930d4a309614333a7ff3e545f13` | `f3d3b212ab7bb5e7d7949f526350748300667223bea2d067c2e05f7f95b37ce0` | 17 / 100,316 / `3f8813941bed2f3a4e5aee0ac13d8c70558d451246ea63c4cba89ac91e201e76` | 60.016 + 39.636 | 900.020597 |
| C8P02 | `Q[q0,q1,q2,c4,c6]` | 9 | `3b02b04d8ce0bfbb81f11b8904c8943571cca305ba0292c3cd7d1bc6cee1084a` | 457,638 / `2a9a4ef3358bea2170525a225b30004d075dc72814c6a93721a0f675fbba4039` | `6478dff2a1255c31c8c2bdac22334afc7472068457a0f9c630f749bb3bf47376` | 5 / 591 / `5d378ce7d43f5e102ac66d5878213365f30aa8859049bb22f6e6b13a50429905` | 18.592 + 0.316 | 900.011391 |
| Q1P02 | `Q[q0,q2,c4,c6,c8]` | 6 | `563b75f4535a1e86a6e7badf545bcb6e7e739eae1e980f2e1a7cf91c4b3b64ea` | 51,219 / `4dbbd22464bef1e88d62aa3faa5feda86ce66e1268e4265ce6465ac58e816866` | `2abf6fe32026998c004f0e50b28c0ac353dfee49d5c2cdfcd091d6bfa988dc55` | 4 / 295 / `683ecd71352e15784fa42310642402c7e24b14a432035bcef7bcca7508f0a13d` | 5.973 + 0.316 | 900.019921 |
| TRIPLE02 | `Q[q0,q2,c4,c6]` | 6 | `b8bf5ec7f09f53211b00d5aafcee0d5b1b45c997c254437a3edb0f647376f68f` | 14,883 / `bd95508c3d0441d18d2538810e2c40ac85ccd5da57f09a560d2d9a93a483640d` | `fa0428864a2e15b65b89c0fee2c8f91a557571b0c2c7502f1c9230a6f88d8632` | 2 / 169 / `e2d240e369e516ad8e3fb3ac221061abe465a241ce91ceeef96a4e7c0947493c` | 4.922 + 0.216 | 900.006164 |

The rank-9 branches have the same support census SHA
`74f8eb36283eb49f08b92627aed4af1065711c2b7b5b8d3607b6173cbf571722`
(75 nonzero entries; 172 matchable of 550). The rank-6 branches have support
census SHA
`bb8f7ee0faabbdb8e40be15bd4d6b3df319acbb5d6d6df7643954a65503d8c51`
(36 nonzero entries; 1,100 matchable of 97,020). All four exact 95-pivot files are
byte-identical, SHA
`2edaa006dae3f63e90973d40de5c7cdda00437570283429c69b353023645e7fc`.

Every timeout has the identical partial saturation transcript SHA
`4ee63095327d80572764eb3783d0e77c7a6cf385f47cf93c1cafcea843b29418`.
It records, in order:

- node nonempty and reducer fixtures PASS;
- first saturation object type `list`, size 1, slot 1 type `ideal`;
- node-ideal inclusion failures `0`; and
- second saturation/two-way standard-basis stability failures `0`.

The next archived line is the forced-timeout `halt 1`. No power-certificate,
closed-successor, node-result, or endpoint-chart artifact exists. The four exact
open bases listed in the table are nonunit standard bases, so the opens are
proper.

## Root cause in the frozen adapter

Frozen R3 source SHA
`11761ad7734e88458195c344bddabd740a9c4f73d10ff071ab06baa2811e4d8f`
computes `J=I:Delta^infinity`, writes `J`, proves `I subset J`, recomputes
`J:Delta^infinity`, and proves two-way equality. It then unconditionally performs

`NF_I(1), NF_I(Delta), ..., NF_I(Delta^256)`

before printing the proper/empty dichotomy. Thus a proper open necessarily incurs
all 257 reductions even though the already computed saturated ideal has settled
the question. Increasing the cap or changing a nearby term order would repeat a
logically futile negative membership search.

## Algebraic justification for the redesign

For `J=I:Delta^infinity` in a polynomial ring,

`D(Delta) intersect V(I) = D(Delta) intersect V(J)`.

Moreover,

`1 in J` if and only if `Delta^n in I` for some nonnegative integer `n`.

Therefore:

- if `NF_J(1) != 0`, `J` is proper and no power of `Delta` can belong to `I`;
  a bounded search for such a power is both unnecessary and incapable of proving
  its nonexistence;
- if `NF_J(1) == 0`, the open is empty and an explicit power/colon membership
  witness is required before accepting emptiness.

The successor must branch immediately after the stable saturated basis is known.
On the four frozen packets it must require `NF_J(1) != 0`, `NF_J(Delta) != 0`,
node inclusion failure count zero, and the archived stability prefix exactly. It
then uses `J` directly as the active quotient for the adjugate kernel and endpoint
pullback.

## Exact resume design

1. Verify the whole terminal-archive hash and exact member hashes from this report.
2. Extract the node ideal, selected signed minor, rank witness, 95 pivots, residual
   matrix, partial transcript, and emitted `OPEN_SB` without rewriting them.
3. Rebuild `std(OPEN_SB)` and require two-way normal-form equality with the banked
   basis; require every node generator to reduce to zero, `NF(1)` nonzero, and
   `NF(Delta)` nonzero. Require the archived saturation/stability transcript prefix
   byte for byte. Any disagreement is `REDUCER_DISAGREEMENT_NO_VERDICT`.
4. Emit the proper-open certificate and assert
   `EMPTY_POWER_SEARCH_ENTERED=0`. The generated production source must fail its
   mutation audit if an `ek<=256` loop is reachable from the proper branch.
5. Use the banked rank rows/columns and pivot transform; never repivot after the
   base change. Build the full adjugate right-kernel, verify all next-size-minor
   identities and all 106 residual rows, lift through all 95 rational-unit pivots,
   and pull back `E=x14*x72+x1*x97` with every diagonal and cross coefficient.
6. Require the same planted endpoint controls as R5: at least one actual diagonal
   coefficient `e`, `NF(e+1)` nonzero, and
   `NF(NF(e+1)-NF(e)-1)=0`. Also require a bordered zero identity and that adding
   `Delta` yields a nonzero normal form equal to `NF(Delta)`.
7. Classify the node-1 proper open before computing `I+(Delta)`. Closed-successor
   recursion is a later, independently capped phase and cannot erase or promote
   the open-chart result.

An exact artifact census shows `c4` is absent from both node generators, the
selected minor, all 95 pivot entries, and all 110 residual entries in every lane.
The resume may omit this inert variable during exact computation and state the
result after scalar extension by `Q[c4]`; the source must independently reproduce
the zero-occurrence census before doing so.

## Secondary factor checksum, not the primary proof route

Literal monomial-content scans give:

| Branch | content of node generator 2 | content of selected minor |
|---|---|---|
| P | `q1` | `q1*c8` |
| C8P02 | `q1*q2^2` | `q1` |
| Q1P02 | `q2^4` | `q2^4*c8` |
| TRIPLE02 | `q2^4*c6` | `q2^5*c6` |

These explain the degree explosion in repeated powers and provide an independent
product-recomposition control. A factor-aware sequential localization may be used
only as a cross-check with two-way equality against the frozen `OPEN_SB`; it is not
the selected primary route.

## Strict scope and verdicts

A zero endpoint pullback yields only
`EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY`. A nonzero coefficient yields only
`RING_LEVEL_ENDPOINT_NONZERO_ON_NODE1_PROPER_OPEN_PENDING_NILPOTENCE_RADICAL`.
Neither result covers the closed complement or the whole component. Timeout,
diagnostic, marker, source, reducer, basis, or plant disagreement is explicitly
`NO_VERDICT`. No endpoint claim may be inferred from the four old timeout packets
alone.
