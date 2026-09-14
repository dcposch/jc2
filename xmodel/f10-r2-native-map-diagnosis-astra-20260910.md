# r2 mapped-native STOP: static diagnosis

DIAGNOSIS ONLY. First action2026-09-10 14:14:10UTC;
fixed reserve14:22, hard stop14:25. All five exact input pins matched before
body reads; own targets were absent. No source fix, execution or reproduction.

The complete terminal custody lists only refuse-status as completed and
refuse-caps prelaunch metadata plus empty runner streams. Its result is
STOP_NONDECISION / mapped native file not pinned. No science outcome.

## Exact failing site

The reason is raised at dispatch.py line299 in check_maps: the canonical resolution of an observed absolute mapped pathname was absent from native['files']. This differs from the subsequent alias test at301, the deleted-mapping rejection in identity(), and the unavailable-identity rejection. It is a membership failure, not a recorded SHA mismatch.

The complete CUSTODY.json records one completed run, refuse-status, with NORMAL_EXIT, null resource, observed runner/Python identities and owned-group quiet. For refuse-caps it records pre.json and two empty runner streams, but no runner-live, Python-live, telemetry or post record. The dispatcher opens the streams at404, starts Popen at405, calls identity(p.pid) at408, then check_maps(runner) at410 BEFORE emitting runner-live at411. Conditional on the supplied complete custody inventory, this localizes the failure to run line410 calling check_maps line299: the immediate outer CAPRUN-runner check for refuse-caps. Prelaunch revalidation precedes creation of these streams; subsequent child-map checks follow runner-live publication.

The offending pathname, resolved name and runner snapshot were not persisted. The STOP string identifies no particular library, loader file, transient data mapping, PID, executable image or permissions. Empty streams and absent telemetry do not establish a typed CPU/RSS/wall cap, the expected second refusal, or a particular instruction reached inside CAPRUN. No mutator/check6/check10 ran according to ROOT's terminal intake. Only the first control is completed evidence, not a complete preflight pass.

ROOT separately attested Main0/Control0, original Main8395 and entire cgroup absence before custody intake, successful postchecks and archived custody. Its final lifecycle message reports worker TERMINATED, retained volume AVAILABLE and timers closed. These are attributed lifecycle facts, not new process observations or worker actions by this author.

## Identity and closure ambiguity

identity() reads stat/start identity, status, maps, then boot/namespace, cmdline, limits and cgroup through separate operations. Maps precedes argv. There is no before/after executable-image consistency test. Exec can retain PID/start identity while changing argv/address space; these identifiers do not make the compound record atomic. The runner argv comparison is recorded only after check_maps. The inner Python observation is argv-filtered, but its maps were also read earlier.

A cross-transition snapshot is therefore a source-level possibility, not an observed cause. A legitimate short-lived startup mapping omitted from a steady-state executable/library inventory is another possibility. This check includes every absolute file-backed mapping, not just executable mappings. A large static Python-file inventory does not prove inclusion of the time-union of every permitted startup mapping.

Fork-inherited mappings must not be promoted to the explanation. The failing site is the outer runner immediately after Popen returns, not the later setpriv-to-Python child check. Under the usual successful POSIX Popen exec handshake, return follows exec success, not full interpreter/loader initialization. Thus claiming this snapshot necessarily captured an unexeced fork child or inherited dispatcher maps would be unwarranted. No saved observation discriminates those alternatives.

Passing source/native hash, alias and inventory postchecks is consistent with this STOP: registered files can remain unchanged while a mapped path is unregistered. A successful first control does not prove every later startup instant has identical maps. Conversely, non-atomic reads do not prove the closure adequate; a stable missing file remains possible.

## Smallest prospective diagnostic and correction boundary

The minimal useful instrument delta is fail-closed evidence capture: persist a bounded explicitly UNVALIDATED map observation before validation discards it, or in the same failure branch. Record label/phase/runner role; PID/PGID/start/boot/namespace; timestamps; observed argv; original and resolved offending path; membership/alias result; and observed mapped-path list. If executable-image/dev/inode or before/after readings are added, preserve their separate times rather than claiming atomicity. Keep STOP and existing caps. Recording an observation never validates it or expands an allowlist.

That dispatcher/evidence-ordering delta requires a FIRST instrument review before a separately registered run. No mathematical-source reproof or CAPRUN redesign is indicated. No patch or execution is supplied here.

After evidence exists, a stable legitimate unlisted mapping could justify a ROOT-frozen native-registration correction with exact canonical file hash and required alias. That is new observed registration, not changed mathematical/checker semantics, and cannot retroactively pass this run. Demonstrated mixed-image observations could instead require bounded coherent sampling or explicitly registered transition-image closure; such changed instrument semantics require FIRST review. Sleeping, retrying until a favorable sample, ignoring data mappings, eager imports, or adding a guessed unrecorded pathname is not an established repair.

## Unresolved item and scope

One diagnostic quantity remains unresolved: the failing mapped-path/image observation at refuse-caps line410. These five inputs cannot recover it. Cheapest discriminating future test: one separately reviewed and registered metadata-only startup observation capturing the first map rejection fail-closed. This report authorizes neither that test nor a semantic retry.

The owned report was reviewed whole before sealing; collision and raised-OPEN review are recorded in READ-SCOPE.md. No new campaign OPEN identifier is raised. Complete scoped diagnosis, explicit missing observation; no repaired instrument, runtime pass or scientific result. All writers IDLE at terminal handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6465`.
- Body SHA-256:
  `32abbf3d0f05f3f74fe87513a51e19b375904ccd6854e62e0172c1f84202c069`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
