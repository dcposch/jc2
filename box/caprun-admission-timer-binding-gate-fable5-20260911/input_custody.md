# Input custody — caprun-admission-timer-binding-gate-fable5-20260911

Lane: Fable 5.1 narrow DELTA, coordinator versus worker timer binding. Frozen input directory `/tmp/jc2-lane.pfjGJu/inputs` (six files, mode 0400) plus automatic FALLACY-v2. Reviewer first action 2026-09-11 09:56:16 UTC; ROOT prep 09:54:22 UTC; latest launch 10:00; original reserve 10:08 / HARD 10:11 UTC, never reset. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d.

Target absence: both owned paths absent at 09:56:16Z and 09:58:38Z (`ls`: No such file or directory) before the first write.

Pre-read pins (verbatim `sha256sum` output at 09:56:16Z; all six equal the assignment's expected values; verified before any body was read):

```
bb00d8dc15208a621dbec8293f3faf54ed3836cfeba6aed1a1622a4d533f4252  caprun-admission-timer-binding-root-20260911.md
9982d5315f5f6920e26d4e863d3c59a6e8fcc7499a38c77a4e52766fc3edcfd2  caprun-admission-timer-binding-root-20260911.md.artifact.json
c8912f2e54cdd207268383abe384fca3e5806743cfd3d17ad0973705c2f9c72d  caprun-closed-scope-admission-gate-fable5-20260911.md
5f0cc7a9146c055b09ca0dd0db79e80cbb38ed64e79d64acfb177bbf0ffce9a4  launch-worker.template.sh
d08e05c66d2c874f00f0485aef929a829217e89488546601c73145b11121fba1  outer-admission.template.sh
99cb19a535c8233143db8a4dc68ac0dd93f1ae9b2e68211af9522fb6145d611c  parent-outer-admission.template.sh
```

Sizes (`wc -c -w -l`, bytes / words / lines):

```
  110   746  6049 caprun-admission-timer-binding-root-20260911.md
    1     1   698 caprun-admission-timer-binding-root-20260911.md.artifact.json
   67  2460 17495 caprun-closed-scope-admission-gate-fable5-20260911.md
   44   233  3389 launch-worker.template.sh
   98   551  6261 outer-admission.template.sh
   95   508  6006 parent-outer-admission.template.sh
  415  4499 39898 total
```

Charged names: `caprun-admission-timer-binding-root-20260911.md` = xmodel/caprun-admission-timer-binding-root-20260911.md and its `.artifact.json`; `outer-admission.template.sh` = the new box/caprun-admission-timer-binding-root-20260911/outer-admission.template.sh; `parent-outer-admission.template.sh` = cmp/hash-identical frozen copy of box/caprun-closed-scope-admission-astra-20260911/outer-admission.template.sh, renamed only to avoid a basename collision (its pin equals the root report's "old outer" pin); `launch-worker.template.sh` = box/caprun-closed-scope-deployment-prep-root-20260911/launch-worker.template.sh; `caprun-closed-scope-admission-gate-fable5-20260911.md` = the collected FIRST.

Read WHOLE: all six through EOF (root report through its Seal, FIRST through its BODY-END, artifact JSON single line, three scripts to their final line). Clipping: none; each read reproduced the wc line count. Root artifact consistency: `head -c 5717 | sha256sum` of the root report reproduces body 4b27f15929204f1ee269909bcd966e4602667e6c611f34263c59649a74398acd; the standalone BODY-END line ends at byte 5717; custody opened 09:52:03Z, closed 09:53:03Z, finalized 09:53:04Z, lease 34e613141d16a2e4f0aba28d2308f1ea, all before this lane's 09:54:22 prep.

Process record: only sha256sum, diff, cmp, grep, sed, head, wc, date, ls, pwd, printf/cat and the mandated apply_patch tool (one no-input usage probe that printed usage and wrote nothing). Nothing executed, imported, syntax-checked, compiled, AST-parsed or tested; no Python, CAS, candidate subprocess of any size, AWS, SSH, network, git, process control, protected access, other agent or new assignment. One grep for the string apply_patch over the prior FIRST lane's custody file was used solely to learn the tool's invocation convention; no content from it entered any verdict. Owned outputs: only this file and xmodel/caprun-admission-timer-binding-gate-fable5-20260911.md, written solely through apply_patch in writes under 1000 words each; no Write/Edit/redirection, no other file, no local transaction, no author Seal, no charge_basis.

Post-write pins (verbatim `sha256sum` output at 10:02:06Z, after both owned files were written and before the final marker; identical to the pre-read pins):

```
bb00d8dc15208a621dbec8293f3faf54ed3836cfeba6aed1a1622a4d533f4252  caprun-admission-timer-binding-root-20260911.md
9982d5315f5f6920e26d4e863d3c59a6e8fcc7499a38c77a4e52766fc3edcfd2  caprun-admission-timer-binding-root-20260911.md.artifact.json
c8912f2e54cdd207268383abe384fca3e5806743cfd3d17ad0973705c2f9c72d  caprun-closed-scope-admission-gate-fable5-20260911.md
5f0cc7a9146c055b09ca0dd0db79e80cbb38ed64e79d64acfb177bbf0ffce9a4  launch-worker.template.sh
d08e05c66d2c874f00f0485aef929a829217e89488546601c73145b11121fba1  outer-admission.template.sh
99cb19a535c8233143db8a4dc68ac0dd93f1ae9b2e68211af9522fb6145d611c  parent-outer-admission.template.sh
```

Owned-file write sizes by `wc -w`: report chunk 1 = 769 words, custody first write = 378 words, report chunk 2 and this custody update each smaller than chunk 1. A whole readback of both owned files precedes the final marker append; no writes afterward.
