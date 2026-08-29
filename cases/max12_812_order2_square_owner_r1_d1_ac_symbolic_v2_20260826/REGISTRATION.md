# Registration: `r=1` / symbolic-`d=1` V2 identifier repair

Date: 2026-08-26

V1 compiled and executed every source/Laurent, recurrence, symbolic-shift,
support, and double-pole identity over both exact `Q` and `F_65521`.  Its
validator correctly failed because `primdec.lib`, loaded by the first ring,
already owns the identifier `lam`; in the second ring Singular therefore
interpreted the intended root coordinate with the wrong type.  The resulting
`?` diagnostics prevented promotion.

V2 pins V1 byte-for-byte and changes only the whole identifier `lam` in the
compiled Singular source to the collision-resistant
`rootlambda987654`.  It requires a nonzero and unique replacement count and
otherwise preserves all mathematical rows and validators.  V1 is immutable
and remains a deployment-negative control.

Dual AWS, 24 GiB virtual-memory cap, 600-second compiler and 3600-second
engine caps.  Scope is unchanged: only `r=1` and the symbolic unique-`AC`
subcone `a>=2,c=a+1,r>=a` on `D(p*k0)`; no square-branch or order-two
verdict.

