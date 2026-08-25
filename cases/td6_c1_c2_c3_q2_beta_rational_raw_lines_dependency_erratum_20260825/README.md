# Erratum: rational-line endpoint dependency and B3 debt

Frozen status: **nonmutating dependency/custody repair**.

The frozen V45/V46 D(U) algebra is unchanged.  The old frozen assertion that
V33/V69 supplied the common `U=0` endpoint is withdrawn because V33/V69 ran
only on `U=0,D(C)`.  Reviewed V70 is the replacement authority at the common
origin `C=V=U=0`.

Exact repaired status in the fixed normalized A3 q2-beta section:

- `V=0,C=-U^2` is source-closed as V46 on `D(U)` plus the V70 origin;
- `V=0,C=3U^2` and `V=0,C=-5U^2` retain their genuine-P12 plus abstract-N13
  algebra on `D(U)` and the V70 endpoint, but the staged-N13 original-source
  caveat remains;
- for the B3 boundary route, `C=-U^2` is source-closed and
  `C=-5U^2,D(U)` is the precise remaining staged-N13 source-DAG debt.

The `C=3U^2` line is not a B3 branch on `D(U)`.  No frozen predecessor byte
is modified.  See
`xmodel/td6-c1-c2-c3-q2-beta-rational-raw-lines-dependency-erratum-20260825.md`.

