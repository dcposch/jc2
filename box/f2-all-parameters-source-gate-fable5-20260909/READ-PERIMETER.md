# Read perimeter and custody (Fable 5.1 F2 all-parameter SOURCE gate, 2026-09-09)

- Root actual release 09:05 UTC; lane launch observed 09:05:21 UTC; report written 09:20:31 UTC; hard stop 09:30 UTC.
- Inputs read WHOLE: the eleven files in /tmp/jc2-lane.9dZetY/inputs; SHA-256 and byte sizes in input-pins.sha256 (matches the charged list byte for byte).
- Provenance paths inside those files were not followed. source-input-pins.json used as provenance only.
- Output: xmodel/f2-all-parameters-source-gate-fable5-20260909.md, SHA-256 in output-hash.sha256.
- Commands: date, ls, cat, wc, sha256sum, mkdir, git rev-parse, tail, od, heredoc writes. ZERO mathematical subprocesses.
- Not read: canonical ledgers, protected jc2-lean, peer 0730 bodies/logs/receipts, live F2 local/F10 gates, any uniform local theorem. No AWS/SSH, no agents, no shared/frozen edits, no seal, no charge_basis.
- Frozen basis observed: 0d39df3c9fd69c939a8420c54d03228b9077777d.
