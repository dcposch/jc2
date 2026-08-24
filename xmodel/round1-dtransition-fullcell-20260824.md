# D1 child: full-cell band-26 compatibility gate

**Producer:** `/root/dtransition_fullcell`

**Date:** 2026-08-24 UTC

**Premise:** only the different-model-reviewed `FREE-TAIL-SIGNAL` in
`xmodel/review-dtransition-grok.md`

**Object:** the promoted `p=105337`, `a00pp`, cell-0 copy of
`A^14`, with fixed `(W1,W2)=(31931,9457)`, under the source-defined
`X27 -> X25` transition

**Status:** INTERNAL / PRODUCER-CHECKED / MOD-p FULL-CELL GATE

**Preregistered verdict:** `NONEMPTY-SINGULAR-OR-LOWER-RANK`

## Result

The six band-26 compatibility functions have an exact common zero: the
registered `A^14` origin.  Their Jacobian there has rank **five**, witnessed
by the nonzero `5 x 5` minor

```text
function rows       0,1,2,3,4
free columns        x57,x62,x65,x68,x16
determinant mod p   39793
```

Consequently the compatibility zero locus on this modular cell is
**nonempty**, and the generic rank of the six-function map is **at least
five**.  The desired rank-six smooth-codimension-six gate does not occur at
the origin.

At the deterministic same-cell point with the fourteen free coordinates set
to `1,2,...,14` in the registered order, the compatibility values are

```text
(23070, 55420, 82249, 287, 11111, 1237),
```

so that point is outside the `X27 -> X25` image.  Its exact Jacobian again has
rank five, now witnessed by determinant `104469` on the first five function
rows and free columns `x57,x59,x60,x62,x63`.

Both registered Jacobians have the same one-dimensional left dependency,

```text
mu = (104372, 48519, 44983, 31248, 84848, 1),
```

and `mu` also annihilates the six function values at both points.  This is a
strong structural signal that one of the six canonical cokernel equations may
be redundant after the band-24 triangular completion.  It is **not yet an
identity certificate on all of `A^14`**.  Therefore this report does not
upgrade “generic rank at least five” to “generic rank exactly five.”  The
exact upper rank remains the sole unresolved part of the requested generic-
rank discriminator.

Two exact symbolic-source expansion attempts were bounded and stopped before
completion: an unrestricted depth-27 build after 994.8 seconds, and a
source-faithful 64-coordinate build after 893.5 seconds.  Neither emitted an
artifact or a mathematical result.  Their timeouts are representation-growth
limits, not evidence for or against the identity.

This is a decisive stop under the preregistration: a certified zero exists,
but no registered zero has rank six.  No band-28 child is licensed.

## The six functions

On the fixed cell, let `s=(x57,...,x27)` denote the fourteen free coordinates
in the order

```text
x57 x59 x60 x62 x63 x65 x66 x68 x72 x73 x16 x19 x24 x27.
```

The promoted triangular certificate reconstructs the ten dependent cell
coordinates, the 22 pristine D21 pivots, the two level-44 `tg` coordinates,
the four pivot deep tails, and the rank-four band-24 frontier completion.  Let
`E_26(s)` be the resulting ten-vector

```text
Row_26[eta^a],  a=0,3,6,9,12,15,18,21,24,27,
```

before adding the ten new X27 coordinates.  The source-filtration coefficient
matrix `A_26` of those new coordinates is constant on this fixed leading
cell: a first-occurrence band-26 coordinate can pair only with slot-zero
leading factors at this band.  It has rank four.  If
`lambda_1,...,lambda_6` is its canonical left-kernel basis, the six functions
banked here are

```text
C_i(s) = lambda_i . (-E_26(s)),  i=1,...,6.
```

Their simultaneous vanishing is equivalent to exact affine solvability of
the ten band-26 equations.  The straight-line evaluator and the literal
`A_26`, `lambda_i`, values, Jacobians, minors, and completed points are in
`cases/round1_dtransition_fullcell/results.json`.

## Exact differentiation and gates

The Jacobian is not a finite-difference estimate.  The replay differentiates
the complete source/certificate chain over `F_105337`:

1. It differentiates all 34 parked-cell rows and uniquely solves the
   rank-10 dependent-coordinate tangent system.
2. It differentiates all 76 pristine D21 rows plus all ten pristine Row-22
   rows.  The combined system has rank 28 on the 22 pivot coordinates, the
   two level-44 `tg` coordinates, and the four zero-completion deep pivots.
3. It extends the source dual jets to the five varying prefix coordinates
   `uf18,vf1_34,vf1_36,vf2_34,vf2_36`.  In the Newton suborbit block it uses
   the required `1-C_k` derivative for the shared `P-C_kY` prefix slots; an
   earlier `-C_k`-only draft correctly failed the frontier tangent replay and
   was discarded.
4. It differentiates the rank-four band-24 frontier solve with its six kernel
   frees held at the registered zero-completion and replays every band-24
   tangent residual as zero.
5. It contracts the resulting band-26 derivative with the six canonical left
   cokernel rows and certifies the displayed modular minors.

At both registered points the following exact ranks are unchanged:

| gate | rank |
|---|---:|
| 34-row cell dependent block | 10 |
| D21 + Row-22 reconstruction block | 28 |
| band-24 frontier block | 4 |
| band-26 new-coordinate block | 4 |
| six-function Jacobian | 5 |

The origin needs no frontier correction and has function vector zero.  The
sequence point uses exactly four nonzero frontier pivots,

```text
tf1_51=4638, tf1_56=91894, tf2_51=11461, tf2_56=14361,
```

after which every residual through band 24 is zero.

## What is and is not decided

Decided exactly at the declared modular scope:

- the six source-defined compatibility functions exist on the selected full
  `A^14` cell;
- their common zero locus is nonempty;
- their generic differential rank is at least five;
- the origin has rank five, not six;
- a deterministic point of the same cell is cut by compatibility;
- the reviewed pointwise mixed behavior is therefore already present within
  one full promoted cell, not merely across different cells.

Not decided:

- whether the generic rank is five or six.  The repeated constant dependency
  is not promoted to a global polynomial identity without an exact reduction
  through the triangular certificate;
- the dimension, reducedness, or component structure of the full
  compatibility zero locus;
- whether a non-origin compatible point has rank six;
- anything at band 28 or later.

## Perimeter

There is no use of D43, `D43-NF-FID`, D75, B=168, or a characteristic-zero
model.  This report proves no persistence, compatible inverse system, formal
germ, lift to characteristic zero, algebraization, polynomial Keller map, or
Jacobian-conjecture counterexample.

## Reproduction

```sh
/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round1_dtransition_fullcell/fullcell_compat.py --selftest

/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round1_dtransition_fullcell/fullcell_compat.py --run \
  --out cases/round1_dtransition_fullcell/results.json
```

The JSON carries a SHA-256 manifest of every source, promoted cell,
preregistration, producer report, and hostile-review input used by the run.
An independent stdlib replay then rehashed every manifest entry, recomputed
the modular ranks, cokernel equations, both `5 x 5` determinants, the shared
dependency, and a one-unit negative control.  It passed 48 checks; a fresh
source run into a temporary directory was byte-identical to the banked JSON:

```sh
python3 cases/round1_dtransition_fullcell/independent_replay.py \
  --source-rerun --out cases/round1_dtransition_fullcell/replay.json
```

No shared top-level ledger was edited.
