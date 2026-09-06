# Disk purge candidates on math-hq (for DC's decision; coordinator will NOT delete lane artifacts unilaterally)
Root 96 GB at 99% (2026-09-06 00:45Z). Non-campaign: /home/ubuntu/lean/verify 50 GB (Lean verify tree), .elan 5.8 GB, .codex 2.6 GB (thread_history_1.sqlite 0.44 GB, grows ~0.4 GB/day).
Campaign, regenerable from committed emitters (hashes are recorded in the lanes' manifests, so deleting the bytes loses re-verifiability-by-hash but not mathematics):
- emitted CAS inputs *.ms / *.sing larger than 20 MB under box/: 12.2 GB (re-emittable by the recorded scripts)
- coefficient extractions *.tsv / *.json larger than 50 MB under box/: 6.2 GB (re-extractable)
- __pycache__ under box/: 10 MB; worker tree/pull copies: 16 MB (already pruned of duplicate msolve binaries)
Recommended durable fix: grow the root volume (aws ec2 modify-volume --size 300 + growpart/resize2fs). Quick fix if acceptable: delete the two regenerable classes above (18.4 GB).
