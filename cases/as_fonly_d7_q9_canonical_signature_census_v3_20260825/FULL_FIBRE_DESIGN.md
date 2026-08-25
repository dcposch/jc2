# Honest full-19D fibre design after the Q9 signature census

Status: **PREREGISTERED SUCCESSOR DESIGN / NOT YET EXECUTED**  
Scope: the corrected fixed-cap F-only D7 source only.

## 1. Why the zero-section signature is preliminary

The V3 census hashes exact integer source/carry rows and deterministic RREF
data at each canonical Q8 affine particular.  Equality of this signature is
an exact zero-section fact, but it does not prove equality of the transition
on all `3^19` points of the Q8 fibre.  In particular:

- `s=0` is an RREF fibre coordinate, not the 32-vector `y=0`;
- an augmented-rank `(9,10)` at `s=0` does not kill the fibre; and
- canonical digit reduction before `/3` can distinguish representatives that
  agree in an unreduced affine chart.

Therefore one representative may stand for a class only after the **whole
carry circuit**, not merely its zero-section evaluation, is byte-identical on
that class.

## 2. Exact circuit, with no polynomial-degree fit

For one Q9 state write its canonical Q8 fibre as

```text
y_j(s) = digit_3(y0_j + sum_i K_ij s_i),    s_i in {0,1,2}, i=0,...,18.
```

Introduce the 18 Q7 restoration digits `r`.  Rebuild the exact Q7 source rows
from the integer formulas, but represent every coefficient modulo `27` by
three base-three digits.  Low-arity full-adder and multiplier gates propagate
those digits.

Modulus `27` is sufficient for the displayed Q7 gate:

1. `F4,F5 mod 3` need `E mod 9` before the first division;
2. `F1_7 mod 3` needs `F7 mod 9`, hence `E mod 27` before the nested
   division; and
3. `N7,T7` are then needed only modulo three.

Every `/3` is a digit shift after an explicit assertion that the low digit is
zero.  There is no rational division, no reduction before divisibility, and
no fitted total-degree bound.

Each ternary gate can be emitted in either of two checkable forms:

- its unique reduced truth-table polynomial over `F_3`, with a field equation
  `u^3-u=0` for every digit variable; or
- a one-hot Boolean encoding with a proof-logging SAT solver.

The final existential system asks whether there exist `s`, `r`, and the
deterministic gate outputs for which all 19 Q7 rows vanish.  Auxiliary gate
variables introduce no branches because every gate table is functional.

## 3. Exact class refinement

For every V3 zero-section class:

1. reconstruct at least its first and last state index;
2. emit the canonical whole-fibre gate list in a fixed topological order;
3. hash the serialized gate types, constants, source-row outputs, Q8 affine
   particular/kernel, and all divisibility assertions;
4. split the class at the first unequal full-circuit hash; and
5. repeat until every final block has byte-identical circuits.

A same-zero-signature/different-circuit pair is a proof that the proposed
state was insufficient.  It is preserved as a separating-word witness, not
smoothed by a larger interpolation model.

Only after this refinement is **one exact solve per distinct full-circuit
class** licensed.

## 4. Acceptance surface

For each final class representative:

- **SAT / compatible:** emit `s`, `r`, every carry digit, and the reconstructed
  integer `x,y,q7` state.  Directly substitute it into the original source
  rows.  A verified witness proves survival of that representative fibre; it
  proves class-wide survival only after circuit identity is established.
- **UNSAT / incompatible:** require a replayable Nullstellensatz/Groebner
  certificate or a proof-checked DRAT/LRAT trace from the exact gate encoding.
  A solver verdict or timeout is not evidence.
- **CIRCUIT SPLIT:** freeze both state indices, both circuit hashes, and the
  first differing gate.  Add exactly that carry datum to the state and rerun
  partition refinement.
- **UNKNOWN/RESOURCE:** retain the class as unresolved.  Do not replace it by
  zero-section counts or random samples.

## 5. Controls

1. State index `0` must reproduce the known Q7-compatible zero section.
2. State index `729` must reproduce Q8 rank `(13,13)` and Q7 zero-section rank
   `(9,10)`; the full solver must decide the remaining 19D fibre rather than
   inherit that pointwise obstruction.
3. The reviewed fixed `Q9=e17,Q8=0` branch remains the next-high terminal
   negative control after Q7 compatibility; this experiment must not confuse
   the two levels.
4. Replacing an actual affine particular by the 32-vector zero is a mandatory
   old-pass/new-fail deployment control.
5. Omitting the divided Frobenius contribution must change a pinned circuit
   hash and fail the source replay.

## 6. AWS execution and stop rules

- Source-freeze the compiler and gate tables before inspecting solver output.
- Shard independently by final circuit hash on Box02/r6d/Box03; cap memory and
  preserve stdout, stderr, time, engine version, source closure, and proof
  artifacts.
- Aggregate with a deterministic class order and Merkle stream.  Independently
  replay every positive witness and every consumed negative certificate.
- If more than 10% of a 100,000-state prefix has a distinct full-circuit hash,
  stop per-class solving and first derive a smaller sufficient carry quotient.
- If one zero-section class splits at two successive depths with no stabilizing
  invariant, record conductor growth and stop finite-state claims at D7.

This design can prove a full fibre compatible or incompatible at the displayed
transition.  It cannot by itself prove a time-homogeneous recurrence, an
all-depth Witt lift, bounded support, characteristic-zero algebraization,
collision, or JC2.

