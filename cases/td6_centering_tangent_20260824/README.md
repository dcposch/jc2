# TD6 common-centering tangent gate

This case differentiates the frozen normalized TD6 transport and all staged
Jacobian systems simultaneously in the three common center coefficients at
`(c1,c2,c3)=(1,1,1)`.  Arithmetic is exact over the frozen degree-18 field
`E`; no numerical embedding or interpolation is used.

Files:

- `orbit_audit.py`: exact quotient/source-typing audit in the registered
  normalized section.
- `orbit_audit.stdout`: canonical audit output.
- `replay.py`: exact three-direction matrix-aware differentiated elimination.
- `replay.stdout`: canonical replay output.

Run from the repository root:

```sh
python3 cases/td6_centering_tangent_20260824/orbit_audit.py
python3 cases/td6_centering_tangent_20260824/replay.py
```

The heavy replay takes roughly 15--20 minutes on the producing machine.  It
must match `replay.stdout` byte for byte.  `MANIFEST.sha256` and
`FREEZE.sha256` are identical manifests over the four payload files above.

Scope: the result is a first-order sensitivity/rank gate at one already
inconsistent normalized control.  It does not kill the center family, SP-2,
any terminal class, or JC2.
