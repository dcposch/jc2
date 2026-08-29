# Preregistration: exact weight-10 square-tail witness discovery

Date: 2026-08-27

This is the next positive-discovery specialization after the exact weight-11
tail returned the unit ideal.  It remains subordinate to the authoritative
literal raw ideal with SHA-256
`ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`.

Set every raw parameter of weight below 10 to zero and retain every raw slot
of weight at least 10.  Products of two retained perturbations begin at
weight 20, so solve every literal coefficient equation through `D19=0` as
one complete exact rational linear system.  Serialize its full nullspace and
substitute it, without further specialization, into every coefficient of
`D20,D21`, and the affine `D22=1` target.  The resulting exact quadratic
ideal is the charged object of this lane.

Run on audited Box03 in a fresh immutable namespace with a one-hour wall
cap, 24-GiB VM cap, one core, `/usr/bin/time -v`, and zero swap.  A rational
point is promotable only after expansion to all 303 raw coordinates and a
PASS from `verify_endpoint.py --witness`.  A unit result excludes only this
weight-10 square-tail specialization and is non-evidence for the full fixed
fixture.
