# Live process-tree audit for aborted cutoff-three modular r1

The following process census was read directly from r6d while all six
charts were live.  RSS is in KiB.  The immutable namespace path occurred in
every worker command and in the inherited `TAIL3_RUN_ROOT` environment.

| Chart | Role | PID | PPID | PGID | SID | RSS |
|---:|---|---:|---:|---:|---:|---:|
| 0 | worker bash | 381080 | 380865 | 381080 | 381080 | 3644 |
| 0 | GNU time | 381082 | 381080 | 381080 | 381080 | 1552 |
| 0 | timeout | 381083 | 381082 | 381083 | 381080 | 2100 |
| 0 | Singular | 381087 | 381083 | 381083 | 381080 | 3641780 |
| 1 | worker bash | 381098 | 380865 | 381098 | 381098 | 3580 |
| 1 | GNU time | 381103 | 381098 | 381098 | 381098 | 1560 |
| 1 | timeout | 381104 | 381103 | 381104 | 381098 | 2104 |
| 1 | Singular | 381105 | 381104 | 381104 | 381098 | 3758616 |
| 2 | worker bash | 381116 | 380865 | 381116 | 381116 | 3572 |
| 2 | GNU time | 381121 | 381116 | 381116 | 381116 | 1560 |
| 2 | timeout | 381122 | 381121 | 381122 | 381116 | 2100 |
| 2 | Singular | 381123 | 381122 | 381122 | 381116 | 3699236 |
| 3 | worker bash | 381134 | 380865 | 381134 | 381134 | 3596 |
| 3 | GNU time | 381139 | 381134 | 381134 | 381134 | 1556 |
| 3 | timeout | 381140 | 381139 | 381140 | 381134 | 2108 |
| 3 | Singular | 381141 | 381140 | 381140 | 381134 | 3576472 |
| 4 | worker bash | 381152 | 380865 | 381152 | 381152 | 3624 |
| 4 | GNU time | 381157 | 381152 | 381152 | 381152 | 1556 |
| 4 | timeout | 381158 | 381157 | 381158 | 381152 | 2100 |
| 4 | Singular | 381159 | 381158 | 381158 | 381152 | 3546612 |
| 5 | worker bash | 381170 | 380865 | 381170 | 381170 | 3600 |
| 5 | GNU time | 381175 | 381170 | 381170 | 381170 | 1560 |
| 5 | timeout | 381176 | 381175 | 381176 | 381170 | 2104 |
| 5 | Singular | 381177 | 381176 | 381176 | 381170 | 3400220 |

The runner recorded only the six worker-shell PGIDs.  GNU `timeout` created
the distinct inner PGIDs shown above, containing the actual Singular
processes.  Consequently the built-in telemetry saw roughly 5 MiB per
recorded group while the direct six-Singular census already totaled
21,622,936 KiB in this snapshot and later reached 34,415,340 KiB.

The coordinator validated and TERM-signalled inner PGIDs
`381083,381104,381122,381140,381158,381176`.  By the start of the delegated
stop at `04:44:45Z`, those groups and their worker shells were gone.  The
only remaining session-380865 members were runner `380865`, guard bash
`381051`, and guard sleep `381592`; each was revalidated by SID and exact
namespace environment.  TERM to outer PGID `380865` reduced the live count
from three to zero in two seconds.  No KILL was issued.  The final census
contained no namespace or Singular process.

This is containment evidence only, not algebraic evidence.

