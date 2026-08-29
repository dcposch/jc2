# V2 dual-AWS negative control: overstrict replacement-count assertion

Date: 2026-08-26

Status: **NO MATHEMATICAL VERDICT.**  Preserve V2 immutably as a fail-closed
compiler control.

V2 correctly found and replaced the six omitted-`k60` strings in the frozen
V1 positive-valuation ring/map declarations.  Its postcondition then required
the repaired string to occur exactly six times globally.  Frozen V1 already
contains one legitimate occurrence in the separate `D(k60)` ring, so the
correct global count after repair is seven.  Both AWS compilers therefore
raised

```text
RuntimeError: V2 formal-k60 replacement failed
```

with compiler rc 1, before Singular was launched.  This is only a wrapper
assertion error.  V3 may replace that postcondition by the exact three-part
check `old_before=6`, `new_before=1`, `old_after=0`, `new_after=7`; it must
change nothing in the generated input.

## Custody

Exact-Q compiler stderr SHA-256:
`e1c2a4659f0cbe958f5bb8e880c4caef48170192d0d209cc25c1590c031df355`.

`F_65521` compiler stderr SHA-256:
`7a0a2c2546a57ba3b1f144992a61c067db0ca810dc8c4d443c0fe592ab4d6f95`.

Both compiler validation files have SHA-256
`f5d6f1d5867d96de551eeca6feb09358a077239f2bf5eab3cfd4b34646e1ad33`
and contain `compiler_rc=1`.

Both freeze-check files have SHA-256
`def11f8b6ac9c82aff5a1d7d061955cc0c03b20472893485e9debd67cd483ac3`.

V2 source freeze manifest SHA-256:
`297a9bb5ceb76e0dda740a0b498902e497af9f7c74af96dd3b757ceb209ae9a1`.

## Firewall

V2 ran no CAS and proves no branch.  The V1 dual-field `D(k60)` partial
endpoint remains the only a=8 evidence until a corrected two-section replay
passes.
