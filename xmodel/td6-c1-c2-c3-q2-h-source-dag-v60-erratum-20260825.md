# Nonmutating erratum: TD6 `H=0` V60 ancestry labels

This erratum does not alter the frozen V60 case or report.  It is prompted by
the hostile review
`xmodel/td6-c1-c2-c3-q2-h-source-dag-v60-review-grok-20260825.md`
(SHA256
`c99895806fbf7cbae8baea451856a86949c0b4049185dc5d0227425938a5d89e`).

## Exact correction

The V60 xmodel sentence

> through current row 13, previous rows 0 and 14, and original first rows

and the V60 README sentence

> the unique current N13 row 13 is reduced through exactly the previous rows
> `('X-1',0)` and `('X-1',14)`

are false as ancestry descriptions.  The exact source trace is:

```text
current ('X0',13)
  -> previous ('X-1',14)
  -> original first rows.
```

Previous row `('X-1',0)` is an independently replayed genuinely quadratic
positive control.  It is inserted into the lift cache before the N13 lift and
is not an N13 previous edge.  Consequently the old stdout marker

```text
previous_rows_source_lifted_keys=[('X-1', 0), ('X-1', 14)]
```

describes the cache union, not the N13 support.  Likewise
`N13_one_required_edge_omission_negative_control=true` omits the singleton
current left-null row; it should be read as a current-row omission, not as an
omission of either cached previous row.

## What survives

The review confirms, from the producer source:

- the raw center typing `H=C-3U^2=0` over `Q(V,U)`;
- arbitrary-degree original-row replay;
- N13 row 13 through previous row 14 and original first rows;
- genuine direct-first P12 with 2,885 terms, 28 first rows, and 1,640
  multiplier terms;
- the exact scalar glue and residual `-k/50`, with `k` a frozen residue-field
  unit rather than a center divisor;
- the 16-line coefficient-leaf radical `{U,V,P3,QH}`.

Thus the mathematical scope remains the exact post-transport fraction-field
obstruction on

```text
H=0, D(U*V*P3*QH),
P3=V^4-32*V^2*U^3+128*U^6,
QH=V^4+8*V^2*U^3-64*U^6.
```

It is not a whole-`H`, full-A3, TD6, SP-2, landing, or JC2 theorem.  The
ledger is a coefficient-leaf support ledger plus the pinned P12 termwise
clear, not a fully expanded N13 termwise-product LCM, and it does not prove
that `QH` is essential after cancellation.

## Custody and successor

The immutable V60 report, README, verifier, and hostile review have SHA256:

```text
bd923e4bad92e14abac9502f211821e01b1ff2b4fa08ae7aeb41fc49238e093b  xmodel report
eb6dc3a82b630f67ef37322165708f41deef7093ce86eeff3ea0c706905025e7  README
a2b48cfcdaf84dc9ccd2c2b433768688d8fb5bd5250209d05ed24ad47e0906f5  verifier
c99895806fbf7cbae8baea451856a86949c0b4049185dc5d0227425938a5d89e  hostile review
```

The V60 verifier is a marker/custody gate, not an algebraic replay.  Its old
two-key cache marker must not be cited as N13 ancestry.  The V64 successor
separates `N13_previous_edge_keys=[('X-1',14)]` from the row-0 quadratic
control, moves the arbitrary-degree marker after the replay assertion, adds
the previous-row-14 omission, live P12-without-N13 check, `k` typing markers,
and a clean V64 extraction path.  V64 is promoted only after a clean exact
AWS replay and frozen custody package.
