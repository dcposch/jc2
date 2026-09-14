# Root full-stream replay, 2026-09-06

Independent Fable checker b175ccc7ed339e115c58e30a0893a0e6566a02152d837e4469d4b82d41ce673f was read whole (544 lines) and replayed on the full remote inputs. No full arithmetic ran locally. Root's one capped run used fresh remote directory `/home/ubuntu/d125-full-stream-root-replay-20260906T2210Z` on i-0da0cebfc97c9fd54; the directory tag is not the actual launch timestamp.

Actual run22:12:05.555062–22:12:47.201907UTC, PID/PGID4619, start_ticks226719, boot235391e8-e646-4ac8-b319-8e609c031bf4. CAPRUN4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2 enforced600wall/8GiB sampledRSS; checker set8GiB RLIMIT_AS. NORMAL_EXIT0,41.646852461s,471535616B sampled peak, empty stderr. All3987 rows and878473 Singular atoms match; all29 changed objects rejected semantically, none skipped or unconstructed. This is full-stream instrument verification, not a solve, properness, unit or point.

Four exact copied evidence files:

- results.json:319034e7c794cc452b5745ba30aeab3571fc4e7ed7d2c12479b2fb3cf1d8d5de
- gate.telemetry.json:e1332c19aac55621411dbee37d64e92f6360463fc6b176557098adbb6dc1a31b
- gate.stdout:ac3416d0c028efadc603b0b6266396b8f8e7855c8c2e2040782f3afc6d32726f
- gate.stderr:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Remote/local hashes match. Original literal.jsonl8a059438a525a9cc53bb55163dfe74e4931c4dca10f111a2466672ae99fcaf52 and import.sing9b6eb808aee27e08f0ee7b263755cefa7e9463c3d8ebd4b03b0664cb57563f4d were rehashed unchanged after replay22:13:31. Exact producer/reviewer/root groups1846/2070/3079/4619 were absent before idle STOP. EC2 confirmed STOPPED22:15:42, EBSvol-0eb6450d18ffa89f1 retained, no termination.

Custody corrections: the Fable prose calls the DMI instance identifier a chassis asset tag, but its actual identity JSON uses `board_asset_tag`; `chassis_asset_tag` on this worker is `Amazon EC2`. Root's initial mistaken chassis assertion failed BEFORE directory creation or arithmetic, then root read the actual fields and corrected the assertion to board. This was not a computation retry. Fable's identity.pre.json records an earlier checker hash9b9a0fec..., not the final b175ccc7...; do not claim that early identity record pins the final script. Root independently rehashed b175ccc7... on the remote host before its run, whose result self-hash matches. The full source inputs remain identical throughout. The normal-branch telemetry's leader_reaped=false/cleanup_complete=null are defaults, not proof of an orphan; explicit group absence is retained separately.

Replay uses the exact command in the Fable report, changing ONLY cwd/output paths to a fresh directory. Do not overwrite these terminal outputs. Singular runtime import remains the producer's measured evidence; this replay certifies text/equation equality without invoking Singular.
