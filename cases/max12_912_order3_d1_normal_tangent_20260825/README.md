# D1 common-cubic normal deformation packet

This packet supports the producer theorem
`xmodel/max12-912-order3-d1-squarefree-common-cubic-order20-obstruction-20260825.md`.
It reconstructs the complete quadratic normal tail, the constant-composition
Jacobian, the exact weight-20 normal system, and the squarefree-firewall
controls.  The theorem is stronger than the computational samples: its
valuation proof is in the xmodel artifact and must be reviewed independently.

Every substantive program here is AWS-only and fails closed away from a
registered Amazon EC2 lane.  `PREREGISTRATION.md` records the Box03 job
directories, worker PIDs, and caps.  The local Mac was used only to edit,
transfer, hash, and inspect emitted text.

The decisive control run used source
`verify_firewall_controls.py` at SHA-256
`202cc9895216ca8c3dd741de6339bded1413939d4c0b62e8707a19428757db8c`
and the charged independent reconstruction at SHA-256
`67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623`.
Its stdout ends in
`PASS-D1-SQUAREFREE-ORDER20-FIREWALL-CONTROLS`; stderr is empty.

The preserved `firewall_controls_orientation_failed.stderr` is an explicit
harness negative control.  The first algebra-reaching run rejected a test
that mislabeled a lower-triangular matrix as upper-triangular.  Correcting
only that orientation assertion produced the passing source above.  This
incident changes no theorem identity and is retained rather than hidden.

`SOURCE_CLOSURE.sha256` is the immutable byte manifest.  `FREEZE.sha256`
hashes that manifest; files charged there must not be edited in place.
