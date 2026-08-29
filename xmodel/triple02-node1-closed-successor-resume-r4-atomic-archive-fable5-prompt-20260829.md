# Fable 5 repair — TRIPLE02 R4 atomic archive authentication

Work from `/Users/dc/code/math/jc2`. Create a fresh packet only at

`cases/ggv_8_28_upper_endpoint_triple02_closed_successor_resume_r4_20260829/`

and write exactly

`xmodel/triple02-node1-closed-successor-resume-r4-atomic-archive-fable5-20260829.md`.

Use R3 as the immutable predecessor and read its producer report plus the
complete Opus hostile review
`xmodel/triple02-node1-closed-successor-resume-r3-hostile-review-opus5-20260829.md`
(full `1110c09d8528b536c231eb48e7fdae7c69869d042d0c292d6221ff9c0153397a`,
body `206ebc55548c7218a4966990050510da38279461a9d9279cc3cc5533f959685c`).
Treat the review's `O2-B1` concurrent path-swap exploit as binding. Preserve
R1/R2/R3 byte-for-byte.

Repair the authority so the charged terminal archive is opened exactly once:

1. Reject symlink/non-regular archive paths without creating a second content
   read. Open a single descriptor with appropriate no-follow/regular-file
   checks; hash the bytes from that descriptor, rewind, and pass that same
   open object to `tarfile.open(fileobj=...)`. No later archive-path reopen is
   allowed anywhere in the authenticated decision path.
2. Keep the descriptor alive until all archive member/manifest/directory
   authentication and retained-member reads are finished. Bind the marker's
   `TERMINAL_ARCHIVE_SHA256` to the digest actually computed from that open
   object, not merely to a CLI string.
3. Add a real concurrent rename/replacement regression reproducing Opus's
   unpatched-thread exploit. It must fail closed under multiple file counts
   and timing windows. Also test in-place mutation/truncation during the read;
   if the platform cannot make this race impossible, detect it with stable
   pre/post `fstat` identity/size/mtime/ctime and fail closed.
4. Preserve and re-run all R3 hostile/positive controls. Exercise the hitherto
   untested `swap_zero` gate. Tighten the fault-latch schema so JSON booleans
   cannot pass as integers. Ensure malformed late CLI inputs always emit the
   custody-no-verdict marker before a nonzero exit. State honestly that
   `FINALIZATION_LATCHES` is an internal consistency sidecar unless it gains
   independent authentication; do not overclaim it.
5. Freeze a fresh source archive/manifests/report binding for R4. Prove by AST
   and hash comparison that mathematical generators, Singular scripts,
   objective, starting ideal, recursion, rank census, and terminal allowlist
   are unchanged from R3. Do not execute Singular or launch AWS.

Return `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW` only if every concurrent race
and inherited hostile fixture fails closed and all positive controls promote.
Include exact counts, commands, archive/member arithmetic, full/body hashes,
and a residual-risk ledger. R4 may at most license another hostile review; it
does not authorize AWS, a rehearsal, a mathematical pilot, or promotion.

Hard boundaries: no web, AWS, commit, push, canonical edits, systemd/root
mutation, Singular, or local heavy computation. Never access/list/search/
build/status or control `jc2-lean`; never run global `git status` or
workspace-wide searches. Modify only the new R4 packet and report; use `/tmp`
for scratch.
