# Fail-closed initial V8 launch

The first dual-prime launch used source archive
`1a86551c380cbc224155473628cbd784c07243ddb4a0df3cf2e87e402e110617`
and V8 freeze manifest
`121dbe20ffa72751d77837482fc10d7054f3ec8aecbfd5b61528c69105d338db`.
Both AWS compilers exited `rc=1` before any Singular engine was launched.

The frozen V7 compiler calls `output.mkdir(..., exist_ok=False)`.  V8 passed
the root returned by `TemporaryDirectory`, which already exists, so both
lanes raised the same `FileExistsError`.  The repair passes a nonexistent
child path named `v7_baseline`.  This is packaging/staging only; no emitted
CAS input, mathematical output, discovery manifest, or verdict exists for
the initial launch.
