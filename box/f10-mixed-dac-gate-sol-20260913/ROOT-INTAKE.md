# ROOT intake — supervisor DAC correction

2026-09-13. ACCEPTED CONDITIONAL STATIC FIRST for the one named command
delta. No live dummy, scientific execution or new worker is authorized by
this intake. JC2 and the selected all-r scalar remain unresolved.

## Custody and scope

Sol first action 00:08:54.964129538 UTC; final all-writers-idle
00:11:06.603090927 UTC, before original reserve00:18/HARD00:21. ROOT
independently observed terminal agent status before custody-first intake.
Custody0b652a8f6e6495a60104318ef1ce0999816b537181e1e1b221b2bb9b40a20a96,
report695ba0e7a3fd5a2eef187d1a3ae38daaaf27eb2cea48fb3455021096797ef21c,
manifest828eb1d266641acc55965919b1737654d5d1c4301eb9974f329c56b5160cfcde,
PINS71081e6877a080326e9b605465fcffef60064025c0993ac32d1ca3c96bea8ddf.
All four owned bodies WHOLE read; all eight charged source postpins passed
strict SHA verification. Administrative finalizer expected-basis/manifest
verification passed. Reviewer CAPRUN read was SELECTED, not WHOLE.

The original commands5cf94c444a26c1052338518f17051f0a2abd838b2be2cabd001424568320673e
remain unchanged. The new immutable copy at
box/f10-mixed-dac-correction-root-20260913/COMMANDS.md,
SHA7809c8ae3733d5e765cec4d5018e57dc4b90d30422dbef66f1f89882fee8cd70,
changes only the nonexecuting title and adds CAP_DAC_OVERRIDE to the root
supervisor's bounding set. All source programs, scientific caps, dummy
predicates, clocks and one-attempt rule remain unchanged.

## Exact accepted correction

CAPRUN opens new exclusive stream/telemetry files and sets child cwd before
setpriv. Its root supervisor must therefore enter and write the positive
child-UID-owned0700 output directory. The old bounding set lacks the needed
DAC bypass. The dispatcher separately needs that permission to read child
0600 candidates and receipts. The review's phrase "opens/truncates" should
be read as opens NEW EXCLUSIVE files: the charged source does not authorize
truncating an existing file.

CAP_DAC_OVERRIDE addresses those file-access checks. It is not a bypass of
LSM, read-only mounts or unrelated path controls. The unchanged nonroot
setpriv transition is expected to drop effective capabilities; the actual
probe must still report NoNewPrivs=1 and CapEff=0. That fact is not certified
by static source. ROOT checked the relevant [Linux capability semantics](https://man7.org/linux/man-pages/man7/capabilities.7.html),
including bounding sets and root-to-nonroot UID transitions; this was a
targeted technical check, not a JC2 broad sweep.

No EACCES was observed in a running dummy: neither prior worker attempt
reached that stage. The defect and its correction are source-level findings.
The CPU-limit helper explicitly uses soft=cpu and hard=cpu+1, so internal
dummy3/4 remains compatible with a science parent hard limit3300. No new
capability, larger scientific cap, controller or algebra source is selected.
The future science UNIT must separately carry the same root-side DAC
permission; this review does not authenticate an as-yet-unwritten unit.

## Preparation advanced, not declared complete

ROOT separately prepared the unreviewed DATA template
box/f10-mixed-dac-correction-root-20260913/REGISTRATION.disabled.json,
SHA12ffb39e2ffea120ccb1f6c7827de0459614fbfcfcb9347c8ad4079a02d7bdce.
It fills the fixed schema/job, twelve paths, six existing source pins,
private library parent and unchanged caps. Its sixteen top-level fields,
path/pin keysets and caps passed an administrative jq comparison; this is
not execution of the dispatcher or acceptance of a scientific registration.
Enabled remains FALSE; actual host/boot/uid/gid/clocks, interpreter/setpriv
pins, native projection and qualification pins remain NULL. Nothing may
derive live authority from old worker observations.

The selected native projection destination is meta/source-native-manifest.json,
outside both private output and the assembler's0700 result directory. A
future ROOT must copy the complete freshly checked projection0444 there
with traversable root-owned ancestry; a pathname alone proves no copy.
Qualification likewise belongs in root-owned traversable meta, and the
fresh science mount must initially contain only empty admin/output siblings.

This exposes an operator-integration constraint, NOT a second executed
failure: the future science unit cannot blindly copy the dummy's
StandardOutput=file:OUTPUT/runner.stdout convention, because systemd would
create that file before the dispatcher's exact empty-output predicate.
The complete outer capture/whole-job command sequence must resolve this
before allocation, while preserving bounded output and the accepted layout.
No capture solution, source change or third allocation is selected here.

No new mathematical promotion or ranking change; no full/sweep clock reset.
The minimal command correction closes a concrete source doubt, not the
remaining operator preparation or mandatory registered-worker qualification.
There is no basis for calling the mission complete or genuinely blocked.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5031`.
- Body SHA-256:
  `76a51407450ba6d843969da2fb2bac5dded96efa3c20d677cf4d273912ae4d40`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
