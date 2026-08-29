# Independent terminal hostile review: TRIPLE02 proper-open resume R5

You are Grok 4.6 acting as an equal-standing, adversarial mathematical and
custody referee.  Review the completed AWS terminal independently.  Do not
trust the coordinator's description, do not launch AWS or any CAS job, and do
not access `jc2-lean` in any way.

## Charged terminal

- Archive:
  `cases/ggv_8_28_upper_endpoint_triple02_proper_open_resume_r1_20260828/custody/terminals/ggv_triple02_proper_open_resume_r5_20260828T233745Z_r6d.terminal.tar.gz`
- Required outer SHA-256:
  `4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e`
- Local replay sidecar: the same archive name plus `.sha256`.
- Remote-custody sidecar: the same archive name plus `.remote.sha256`.
- Passing source review:
  `xmodel/triple02-proper-open-resume-r5-hostile-review-fable5-20260828.md`,
  SHA-256 `b886d8bb516f04f3ca6683b17e8f1502c9b4e40eff55a9aab52dd922d48df10b`.
- Controlling preregistration:
  `cases/ggv_8_28_upper_endpoint_triple02_proper_open_resume_r1_20260828/AWS_PREREGISTRATION.md`.
- Frozen source archive SHA-256:
  `60f83a1d4e2eae0f974027059bc1cb1e6de8c3fc687b6cce4af4072ab18c2310`.
- Frozen generated Singular program SHA-256:
  `f5050f1204f3d990be64f18c5776eb7204f2587273a64a533e6d56d37b49132a`.

## Required attacks

Inventory the tar before extraction.  Reject duplicate, traversal, absolute,
link, device, FIFO, or otherwise unsafe members.  Extract only into a fresh
private temporary directory.  Replay the embedded terminal manifest with
exact regular-file census equality and hashes, and independently replay the
outer/local and remote sidecars.

Then verify from the extracted evidence, rather than prose, all of the
following:

1. the candidate and output classification are exactly
   `EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY`;
2. the only valid scope is TRIPLE02 node 1 on `D(Delta)`, with no inference
   about the closed successor, whole component, geometric ambient locus, or
   JC2;
3. worker and production return codes are zero, production did not time out,
   the exact generated script/source/preregistration/Singular/`elim.lib`
   hashes match, and the classifier consumes the complete expected outputs;
4. the exact mathematical trace really establishes the two-containment
   saturation certificate and makes all ten coefficients of
   `x14*x72+x1*x97` vanish after the full right-transform/adjugate replay;
5. every sticky containment, timeout, swap, launcher-reap, systemd, manifest,
   archive, and resource latch is clean; final PGID/JOB_TAG/cgroup censuses are
   empty under the documented collected-scope route; and no contradictory
   positive-looking evidence survives a failed gate;
6. the archive intentionally contains the candidate but not the externally
   published terminal marker, and this is consistent with the reviewed rule
   that the public terminal rename is the supervisor's last successful action.

Look specifically for ways a stale, partial, mismatched, or post-fault output
could have been promoted despite the source review.  Distinguish harmless
stage-runner wrapper return-code files from the Singular subprocess return
codes recorded in the result JSON.

Return one explicit verdict: `PASS`, `REPAIR`, or `FAIL`.  A PASS authorizes
campaign promotion only at the literal proper-open scope above.  Seal your
report with SHA-256 and write only:

`xmodel/triple02-proper-open-resume-r5-terminal-hostile-review-grok46-20260828.md`

Do not edit any other repository file.
