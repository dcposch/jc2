# Strict-nine final installation: bounded offline flow diagnosis

STATIC DESIGN / UNREVIEWED. First action 2026-09-12 03:20:04.823585713 UTC. Original reserve 03:37 / hard stop 03:40 UTC; no extension. No worker, runtime, installer, candidate or scientific process was executed; no pre-existing source or template was changed. Batch d and its clocks remain closed; this report grants no successor authority.

## 1. Outcome: the alleged missing copy is not a valid repair

**NO_NEW_REPAIR for nine-authority installation.** The existing dispatcher creates each authority after release and before its corresponding child. Installing the staged nine files into the live authority directory beforehand would deterministically stop the accepted runtime. The remaining complete-flow timing/qualification gap is separate and is not closed here.

Batch d closed as `CLOSED_PREALLOCATION_INCOMPLETE_FLOW`, without a worker, holder, phase or science launch. Its PLAN selected **PREFLIGHT_ONLY_9**, not the four scientific phases. Neither the expired batch nor this diagnosis authorizes a successor.

I initially inferred from CLOSEOUT and final-install lines70–71 that a nine-file copy block was missing, because those lines install only the registration and card. That inference was sent as advisory and is **withdrawn** after reading the actual runtime. No such block was implemented.

The controlling source is `box/caprun-closed-scope-implementation-astra-20260911/dispatch.py`, SHA256 `52b3d916f4fc3941bb98c8b4f7698ab940680d09ee4e065de1f167857e3fd436`:

- Line264 requires **all three** live authority/frozen/writer directories empty at initialization.
- `authorize()` lines418–441 constructs each whole policy/authority and calls `emit()`.
- `emit()` lines99–106 canonically serializes, opens with `O_CREAT|O_EXCL`, writes, fsyncs, chmods0444 and hashes the new file.
- `run()` line453 invokes that authorizer; lines496–504 compare the complete registered argv, then revalidate and rehash the actual frozen authority before Popen.

Thus there is no pre-release interval in which externally installing those nine live files is compatible with the unchanged dispatcher. Installation before initialization fails `fresh output children`; installation afterwards would race the sole writer or fail exclusive creation. The preholder-security empty-file check at line30 is an additional, earlier check—not the only obstacle.

## 2. Expected artifacts versus actual runtime authority

The nine labels, in order, are `refuse-status`, `refuse-caps`, `refuse-inventory`, `refuse-source`, `refuse-hash`, `valid`, `startup-produce`, `startup-check`, `dummy`. Successful strict-nine execution creates all nine sequentially. Failure stops without a promise that the remaining authorities were created.

The accepted binder/caller already prepares **expected** authority bytes. Its `validate_prepared()` checks all nine complete objects and all nine full command vectors. Binding fills every actual leaf device/inode; only valid/dummy policy objects require those late values. The other seven objects can be completely authenticated before the holder. `latebind.py` SHA `ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe` lines281–306 serializes the expected objects and binds eight resulting digests into argv. Its final fourteen candidates include nine `authority/*.json` reference files, registration, card, three-entry manifest, installer and SUMMARY.

Manual source comparison gives the matching runtime construction: identical field values and source/control mutations, the same target paths, check-mode all-zero absent-input digest for startup-check, identical valid/dummy leaf/profile values, and sorted compact ASCII JSON plus LF. Binder explicitly requests ASCII; dispatcher uses JSON's ASCII default. No coefficient payload is involved in this comparison.

The runtime does **not read the staged reference files**. It recomputes them, and compares its whole generated command to registered argv. For eight phases that comparison includes the genuine authority digest. `refuse-hash` deliberately supplies 64 zeroes; its real generated authority is nevertheless frozen and rehashed against the digest just emitted. Its staged reference is documentary custody, not an extra runtime external digest check. Changing only an archived refuse-hash reference has no runtime effect; do not claim every staged-reference mutation is detected by runtime.

Registration `.pins` covers static roles/native/contract metadata, not these future authority outputs. The three-entry final manifest binds registration, card and the opaque `native.sha256` digest—not all fourteen candidates. SUMMARY and the caller's complete expected-file map bind the staged candidate set for ROOT's readback. These are distinct commitments; none justifies copying a candidate tree into the live output tree.

## 3. Smallest coherent preparation and late flow

No new dispatcher, binder, installer authority serializer or framework is required to repair the false copy premise. A prospective complete **ROOT-owned recipe**, frozen before a separately authorized holder, should explicitly preserve the following order. This is a documentary recipe, not an executed command sequence or release.

**Before holder:** qualify actual installed source/native/helper/physical/ACL/namespace facts; authenticate the four prepared documents, their pins and all static metadata; prewrite literal candidate/transport/readback command structure; prepare expected seven fixed authorities; arrange the original coordinator retirement receipt and worker absolute timers. Keep stage/reference files outside the live `/run/<batch>/authority`, `/frozen`, `/writer` children. Perform the existing preholder-security check while the entire output tmpfs has no regular files. All batch/host/clocks must be genuinely new ROOT selections, not the historical d literals.

**After admission:** retain actual holder PID/start ticks/invocation, boot/namespaces, outer and nine freshly created leaf identities/emptiness, fresh coordinator receipt, exclusive no-migration/no-entrant facts and elapsed time. ROOT authenticates the observation and makes the explicit metadata-freeze decision. No future same-PID exec observation is demanded before execution.

The already accepted supplied-input command has six arguments after `caller.py`: prepared-directory, prepared-pins, observation, decision, fresh candidate-prefix, `ROOT_ATTESTED_CANDIDATE`. Its interpreter vector is `python3 -I -S -B`. The composed ROOT recipe parses the complete ASCII result, requires `CANDIDATE_NOT_INSTALLED_NOT_RELEASED`, applies its patch only at a fresh documentary prefix, and checks all fourteen returned digests/paths/byte counts. Reuse that transport mechanism; do not invent a new late serializer or interpret its success as host authentication.

**Installation boundary:** transfer/authenticate the final installer, registration, card, three-entry manifest and exact native-list bytes at the trusted stage; reference authority files may remain in the documentary stage. Never map the candidate prefix to the live output mount. Verify the runtime's three child directories remain empty (outer stdout/stderr now legitimately exist at the mount root; do not rerun the stronger preholder whole-mount-empty predicate).

Run only the separately approved, fully bound existing final installer. Its concrete operations are already present: manifest `sha256sum --strict -c`; literal registration/card hash checks; holder/unit/start/invocation/namespaces; exact nine leaf identities/domain/empty/no-subtree checks; whole `.pins` and `native.sha256` checks; `install -o 0 -g 0 -m 0444` for **registration and card only**; `sync -f`, `cmp`, hash/mode and holder/time readback. Preserve its absent-target checks and STOP on partial failure; no deletion, overwrite retry or second holder.

After ROOT independently confirms those results and the still-current holder/deadline/timer facts, a **separate explicit ROOT release** writes the one fixed `RELEASE <token>\n` frame and closes the FIFO writer. The holder's existing bounded grammar/EOF handling and same-PID exec boundary remain unchanged. Following release, the unchanged dispatcher performs the second empty-children check and creates each authority itself before its phase. This is the only compatible meaning of installing all nine after the empty-output precheck under the accepted writer model.

## 4. Genuine remaining gap and strict stop rule

The required correction is to the deployment interpretation/checklist: label the nine candidates **EXPECTED_RUNTIME_OUTPUTS / DO_NOT_PREINSTALL** and remove their copy from any proposed release sequence. No existing bytes were changed here. A demand for nine live files before release is incompatible with the current accepted runtime; satisfying that changed requirement would require a separately reviewed runtime redesign, not a tiny installer patch. There is no demonstrated reason to choose that redesign.

The closed batch still lacked a frozen, qualified complete late-flow recipe. That gap is not eliminated merely by correcting the copy premise. Fresh observations, ROOT attestation, transport, whole readback, final installation and explicit release must all finish before the holder's earlier monotonic120-second ceiling and absolute cutoff. Outer admission itself allows up to60 seconds. The reported **365 ms** measured only historical caller→patch→fourteen-file readback; it measured none of the host observation/authentication/install/release path. Network, hash/fsync and administrative latency remain unmeasured. No deterministic hard-real-time guarantee follows from a finite list of commands.

A complete future selection must freeze the whole remaining recipe and its STOP boundaries **before** holder launch, leaving no model-composed document or command during the live window. It must use elapsed time from the original holder start, not start a fresh120 seconds at admission or installation. If insufficient time remains for authenticated installation and explicit release, STOP; do not skip predicates or extend the cap. This report neither supplies a new executable wrapper nor authorizes testing one.

Strict-nine phase execution is also outside the holder-wait interval but inside its own original admission/batch/task clocks. `run()` rechecks the admission deadline before **each** phase; granting a fresh phase budget at FIFO release is invalid. In historical d the holder cutoff and phase-admission stop were only15 seconds apart. That does not prove failure if admission/release is early, but it rules out claiming worst-case120-second holder usage automatically leaves room for nine phases. All those clocks expired without allocation and remain closed.

Nine control/dummy profiles remain5wall/3CPU each, dummy RSS32MiB and other control RSS8GiB, with original aggregate3000wall/2100CPU/8GiB/128MiB and CPU origin0. No FULL13, positive baseline/science, rank observation, cap sufficiency or mathematical outcome is inferred. Successful strict-nine evidence still requires independent collection and the selected actual-evidence gate before any separately authorized science.

## 5. Controls, read scope and disposition

Manual countercontrols: (a) one preinstalled authority suffices to falsify empty-children initialization; (b) bypassing that initialization would still meet exclusive-create conflict; (c) copying fourteen candidates into the live mount creates additional inventory violations; (d) staging all nine outside that mount is compatible and changes no runtime authority; (e) replacing the genuine refuse-hash digest by zero in the archival expected-byte check confuses actual and deliberately supplied hashes; (f) successful candidate readback does not certify native/holder/ACL facts or timing.

All twenty charged inputs were pinned before their bodies. Nineteen were freshly read WHOLE, including the exact administrative caller and binder; runtime dispatch was a fresh **selected** read of lines1–125,245–280,400–515 plus a textual symbol locator, not a whole-code review. Initial clipped COORDINATION/AUTHORITIES ranges were recovered explicitly. READ-SCOPE and PINS give exact ranges and hashes. No provenance/science algorithm or payload body was followed. No candidate, installer, caller, probe or runtime was executed; only documentary read/hash/publication tools ran.

QUANTITY: nine expected authority objects and nine complete argv bindings; the decisive three runtime predicates are empty initialization, exclusive emission and command equality. CHEAPEST TEST: documentary comparison of those pinned predicates, completed here; an independently budgeted repeat is **60 seconds UNMEASURED planning wall**, not an execution or review invitation. The separate quantity of complete actual late-flow wall remains UNKNOWN and must be less than the original available holder interval; no runtime estimate is offered.

COLLISIONS: no new OPEN identifier, mathematical claim, source change or alternate framework. Candidate transport and late binding are already reviewed mechanisms. This report corrects a concrete false deployment premise and identifies the remaining whole-flow qualification boundary; it does not close that boundary or authorize a successor batch.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13384`.
- Body SHA-256:
  `83b03b08edef583720477e3897740bf4b8c0fdece460f0599406e0ce7846f958`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
