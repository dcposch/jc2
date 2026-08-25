# Audit protocol

This protocol records what was actually done; it is not a retroactive
preregistration.

## V2 charge

The charged V2 source and emitted formula were inspected literally.  Solver
agreement was not treated as mathematical evidence.  The exact constructor
calls, variable bounds, remainder divisors, supports, row inventory, and
normalization equations were checked before any rerun.

## Diagnostic corrected emission

`audit_patch.py` makes an audit-only copy of the V2 emitter and changes only
the modulus/bound literal from the residue constructor to raw positive
`177147`.  Its corrected canonical SMT is retained for diagnosis.  No solver
verdict on that corrected formula is used in the final SAT claim.

## Independent reconstruction

`independent_common_core.py` consumes the pinned linear-window parent source,
not V2/V3 SMT.  Starting from the displayed B9 mod-243 pair it introduces at
every digit all 146 coefficient coordinates in the total-degree boxes
`P<=9`, `Q<=12`, plus three coefficients of

```text
H = y^3 + h1*x*y^2 + h2*x^2*y + h3*x^3.
```

It forms 299 exact integer rows: all 276 determinant positions of total
degree `0..22` and all 10+13 top-form coefficients of
`P9-P_(0,9)H^3`, `Q12-Q_(0,12)H^4`.  It reconstructs the complete affine
families through `3^10`, performs the first quadratic Kuranishi transition to
`3^11`, and replays every basis direction over the integers.

It obtained family-coordinate dimensions `55,81,99,116,133` through
moduli `3^6,...,3^10`; at the final transition it found 17 quadratic-active
and 116 linear-spectator predecessor coordinates, fresh rank/kernel/cokernel
`94/55/205`, spectator rank 38, and zero residual equations.  It then solved
for and replayed a literal target-depth witness.

## Independent witness replay

`independent_witness_verify.py` reads only the pinned witness JSON.  It has
its own polynomial arithmetic and hardcodes the displayed integer parent

```text
P=u-u^3+18uy+81(2uy+xy^2),
Q=y+u^4+3u^2y+72y^2+81(y^2+x^4y^2+xy^11),
u=x+y^3.
```

It independently checks reduction to this parent modulo 243, exact total
degrees `(9,12)`, `det J(P,Q)=1 mod 177147`, leading units, and every
common-cubic top coefficient.  It does not import any campaign source or SMT
formula.
