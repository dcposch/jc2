# V84R nonmutating failed-control erratum

V84R passed source closure, the quadratic preflights, and the symbolic-center
rank-3470 transport reconstruction on both AWS hosts. It then failed the new
assertion `raw.value == scalar(row_rhs)` before producing a K2 table.

That assertion compared the normalized typed `qd` source field with the
legacy scalar row presentation. The reviewed source ancestry treats
`qd.source_rhs(key).value` as authoritative; equality with the legacy row RHS
is required only on the X boundary. V84R therefore carries no mathematical
verdict and is preserved as a failed-control/deployment negative.
