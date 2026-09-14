# F10 r1 engine compatibility: exact one-line correction

Basis 0d39df3c9fd69c939a8420c54d03228b9077777d. First action 2026-09-09 14:41:59 UTC; controlling stop 14:49:59 UTC. The requested implementation is COMPLETE; no execution or dispatch is authorized or claimed.

New source: box/f10-r1-engine-compatibility-astra-20260909/engine.py, SHA256 **81e52951192afbbcbfcd7c11ef604ec45a470ca35a93afec2c8416dac985a5d1**. Original source remains unchanged at SHA256 1cd210424747b1c03220b8d2a8dea1ac1350d8259e81a9338f63c508681b675d.

The sole change deletes old line 40, the emitted `option(nostdhilb,noprobabilistic);` statement. Byte comparison against the original with exactly line 40 removed passed. The literal git diff, independently byte-compared with the retained engine.diff, contains exactly that deletion; diff SHA256 90f307d04c0c2b730b1a67d489875fb8e3ee5dcd3e89d4fd062000bc4a0211d1. The header, flags, receipt, parsing, integer-limit behavior and every remaining source byte are unchanged. No helper, caller, checker, registration or frozen file was edited.

The terminal Fable gate 2ee02c1a4494ef086ef75c2943c98b46733302fc52e5866ef68eb479014d254b was read WHOLE after hashing. Its section A explicitly prescribes this deletion if the installed version lacks those options. Root's api-metadata.stdout, SHA256 693a7ad78c8fd44216d6d1cecc85477160d130586038fde80314c0e2f800fc10, was then hashed and read WHOLE. Its 2026-09-09T14:35:08Z output reports both option names unknown. Root identifies the installed version as Singular 4.3.2; this small stdout alone does not independently show the version. No other API inference is made.

The accepted 16x review is retained only for this exact conditional correction. There was no compilation, import, engine invocation, mathematical subprocess, test, AWS/SSH action, worker action or decision. All actual operations were source editing, documentary reads/diffs, hashing and transactional publication. The new source and complete own report were read WHOLE statically. Current input and owned hashes are in the custody manifest; old files are preserved. All writers are idle at terminal handoff.

OPEN — carried runtime validation, outside this completed implementation task: corrected-engine executions = 0. Cheapest next check is one separately root-authorized, capped registered validation using this exact new source hash and the unchanged caller/checker; no permission is supplied here. Installed mathematical/API-wide compatibility, a unit/proper ideal verdict and runtime success remain unclaimed. No new mathematical open problem or follow-on task is raised.

Own-only raised-item check: the preceding carried runtime item is the only OPEN entry; no corpus scan or unrelated work was performed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `2771`.
- Body SHA-256:
  `0c7725d5070126d72d76ae374b72974b687e6dd9da29525ba6db001a155d0ad2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
