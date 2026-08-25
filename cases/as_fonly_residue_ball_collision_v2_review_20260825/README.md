# Residue-ball collision theorem V2 review custody

The reviewed theorem is the conjunction of the immutable repaired parent and
the nonmutating V2 erratum:

- parent report SHA-256
  `81ab0e5cce46d2ad93968500362275ae4a7dbf2d3cf080c54ace531218135d71`;
- V2 erratum SHA-256
  `d50426b36d2881ed577568c0c256f7f45f8f7154805b0f97512cc3e54be1ee2f`.

The repair-only different-model review returned `CONFIRMED`, SHA-256
`0cd7051300bf3938f6b389b1407a46f9a0c7a2d737e209a44c89c00c49e32a30`.
Its prompt and raw run are pinned in `MANIFEST.sha256`.  The underlying AWS
regression-control case remains immutable at manifest SHA-256
`a1b398cdef54bb9874eb6b403227c6cfcac35cd1ccafffa828f7e1d18d64b2db`.

The theorem says: a complete determinant-one polynomial map over every
`Z/3^n`, on one fixed finite allowed monomial set and reducing to
`(x-x^3,y)`, maps each of the three indicated source residue balls
bijectively onto the target residue ball.  Arbitrarily deep compatible
nodes yield a fixed-support `Z_3` map by compactness/König, whose automatic
moving collision transfers through `Q_3`, `Qbar`, and `C`.

Campaign firewall: a filtered state is not a complete map.  In particular,
the current global Q5 gate retains its displayed rows but still owes Q4
through Q0.  Neither its SAT witness nor the pointwise Q4 obstruction may be
fed into the collision theorem.

