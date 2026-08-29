# Deep lambda-zero tail: the exact `Q=X` mutation first fails at `G13[X^0]`

Date: 2026-08-28

Status: **exact fixed-fixture obstruction; not a universal exclusion theorem**

## Scope and pinned input

Work on the reviewed `lambda=0`, `c2!=0`, exact-tail branch, with

```text
A=X^4-1,  Q=X,  r=e=F8=0,
c2=c6=1, all other displayed modes zero,
f=(2^29/75)(-1+11X^4),
F7=A f,
F9=(2^23/75)(7X-27X^5),
F11=F13=0.
```

The `q7,q9,q11,q13,q15` primitives and the nonzero origin coupling for this
point were frozen in
`xmodel/ggv-upper-endpoint-deep-q1-lambda0-even-subbranch-origin-coupling-independent-sol-ultra-20260828.md`
(SHA256 `c940ba048f5edf60b3018670c8914acc469f55f30101f211a6aedb5d591b6714`)
and its checker (SHA256
`23f46a95170fb77f2f5c340b1c6fb570881062d67102fca6dfdeae2f5ea37c4d`).

This packet asks the next necessary question only: when the complete
characteristic is reconstructed, how far does the point fit the literal raw
`G` receiver windows?

## Exact result

The complete characteristic coefficients `G8,...,G12` are polynomials and
lie in their authoritative lower and upper degree windows.  The first failure
is

```text
G13 = -2^27/25 - (2^17/5)X^2
      + (11*2^27/25)X^4 + (2^20/15)X^6.
```

The literal `G13` window is degrees `1,...,11`.  Thus its only illegal slot is

```text
G13[X^0] = -2^27/25 != 0.                         (1)
```

This is a receiver-window failure, not a determinant recurrence failure:
using the characteristic coefficients literally makes every raw determinant
row `D0,...,D13` vanish exactly.

## Mode decomposition and smallest scalar repair

Holding the displayed raw `F` fixed, independently turn on the base
trajectory and the modes `c2,c4,c6,c8,c10,c12` one at a time.  Their
contributions to `G13[X^0]` are respectively

```text
0, 0, 0, -2^27/25, 0, 0, 0.
```

Later modes have not yet been born.  Therefore, within scalar-mode changes
alone, (1) forces `c6=0`.  This cancellation does repair the complete `G13`
window.  It is not a survivor: with all other raw data unchanged, the next
coefficient `G14` has the genuine normalized pole

```text
A^(-1) * (-5 X^6 / 2^34),                         (2)
```

whose numerator is not divisible by `A=X^4-1`.

Moreover the old endpoint coupling used `c6`; setting `c6=0` destroys that
particular coupling.  A successful continuation therefore needs both an odd
primitive/mode release (for example a `c8` carrier) and an even-tail release
to cure (2).  This is the next search, not a conclusion of the present
packet.

## What is and is not proved

Proved exactly:

- the frozen `Q=X` point passes `G8,...,G12`;
- its earliest literal receiver failure is precisely (1);
- at that fixed raw point, the entire constant load comes from `c6`;
- `c6=0` repairs `G13`, after which (2) is the next failure;
- raw determinant rows through the reconstructed weight vanish, as required
  for a characteristic trajectory.

Not proved:

- that arbitrary `Q,e,F8`, odd primitive choices, or modes cannot repair the
  tail;
- that the `lambda=0` full-system locus is empty;
- any four-root endpoint theorem, Keller-pair statement, or JC2 consequence.

## Replay

```bash
python3 cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_g13_obstruction_20260828/verify_qx_g13_obstruction.py
```

The replay uses only exact rational standard-library arithmetic, pins its
upstream packet, checks both lower and upper receiver windows, reconstructs
the characteristic, verifies `D0,...,D13=0`, and includes the `c6` restoration
and nonzero-pole mutation controls.
