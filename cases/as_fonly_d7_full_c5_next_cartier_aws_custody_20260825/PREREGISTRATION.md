# Full-C5 / next-Cartier shell-custody closure

The shell-less Claude review
`xmodel/as-fonly-d7-vertical-full-c5-next-cartier-review-claude-20260824.md`
is already `CONFIRMED` at its hand/source-inspection tier, but explicitly
left replay, manifest, and hash execution to a shell-enabled session.

On Box02, from a SHA-verified complete transitive source closure, run in
sequence:

1. the frozen full-C5 `replay_all.sh`;
2. an explicit independent check of its frozen `MANIFEST.sha256`;
3. the frozen next-Cartier `replay_all.sh`;
4. an explicit independent check of its frozen `MANIFEST.sha256`.

Every command is capped at 12 hours and 16 GiB virtual memory.  Preserve
stdout, stderr, `/usr/bin/time -v`, return code, host/tag/UTC metadata, and
all output hashes.  Any source-closure mismatch, nonzero return code,
timeout, OOM, stderr, missing PASS endpoint, or manifest mismatch is no
custody result.  This is execution hygiene only and cannot enlarge either
reviewed theorem.

