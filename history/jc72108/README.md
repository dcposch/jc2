# Retired (72,108) campaign

The campaign coordinator confirmed that no active or planned research job uses
this standalone campaign or its old replay tools. The top-level `jc72108/`
directory, its generated solver inputs/outputs, and its old plans and launchers
were removed. There are no compatibility symlinks.

These seven documents retain useful mathematical and provenance material,
including the external-certificate cross-check and the limitations of modular
solver verdicts. Their contents are unchanged. Current claim scope and
corrections belong in the root `AUDIT.md`, not in these historical documents.

| Former path | Retained document |
| --- | --- |
| `jc72108/CROSSCHECK.md` | [CROSSCHECK.md](CROSSCHECK.md) |
| `jc72108/CERT-UPGRADE.md` | [CERT-UPGRADE.md](CERT-UPGRADE.md) |
| `jc72108/FACE-ISOLATION.md` | [FACE-ISOLATION.md](FACE-ISOLATION.md) |
| `jc72108/RECON.md` | [RECON.md](RECON.md) |
| `jc72108/REDUCE4-CUT-REVIEW.md` | [REDUCE4-CUT-REVIEW.md](REDUCE4-CUT-REVIEW.md) |
| `jc72108/REDUCE4-REVIEW.md` | [REDUCE4-REVIEW.md](REDUCE4-REVIEW.md) |
| `jc72108/SECTION4-AUTOMATION.md` | [SECTION4-AUTOMATION.md](SECTION4-AUTOMATION.md) |

The documents retain their original path notation. Old references in audit
records can be resolved with this table. Obsolete executable paths need not
exist in the current checkout; original versions remain in Git history.

The external-certificate archive `archive/crosscheck.tgz` in DC’s local checkout
was retained,
including the Helali and Suzuki source/certificate packages. Other existing
certificate artifacts and sealed research records were not moved or rewritten.
Published reproduction archives remain under `dist/`.

The old `lean/` project is now `jc2-lean/cascade-certificate/`. Its original
proof and dependency pins are unchanged; its retired Python exporter and
worked-example probes remain recoverable from Git and release history.
Shared `lib/`, `cases/emit.py`, `cases/farm_driver.py`, and their tests remain
available for other cases.
