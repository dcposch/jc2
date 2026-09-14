# Ubuntu CPython refusal-path compatibility

STATIC documentary compatibility result; no interpreter execution or observed failure bytes. This is not registration or launch authority.

First action 2026-09-11 04:20:57 UTC. Publication reserve 04:38; hard stop 04:41, unchanged. Scope is the six pinned local documentary inputs plus narrowly selected primary Ubuntu/CPython package/source evidence. The prior worker is not a newly selected worker.

## Result

The nominated Ubuntu amd64 package preserves the seven refusal outputs derived from CPython v3.12.0, subject to the original exact-source, healthy-stream, ordinary-interpreter and installation conditions. This conclusion concerns the specific CALL/RAISE positions, ordinary traceback formatter and string-valued SystemExit paths, not every CPython behavior.

An independently streamed official Ubuntu package payload has `/usr/bin/python3.12` SHA256 `a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223`, exactly the prior worker's recorded binary. No newly selected worker was inspected. AMI identity and unchanged userdata are ROOT-provided administrative expectations, not observations made here.

## Selected source comparison

The [Ubuntu source descriptor](https://archive.ubuntu.com/ubuntu/pool/main/p/python3.12/python3.12_3.12.3-1ubuntu0.16.dsc) names version `3.12.3-1ubuntu0.16`, format `3.0 (quilt)`, and the orig/debian archive SHA256s recorded in EVIDENCE.json. Both streamed archive hashes match. Four relevant files from the orig archive have the same full-file hashes as upstream v3.12.3: `Python/compile.c`, `Python/traceback.c`, `Python/pythonrun.c`, and `Parser/pegen.c`. Those are HASHONLY full-file comparisons plus the exact selected body intervals below, not whole-file human reviews.

The complete packaged patch series was read. A text search across all `debian/patches/*` members found no mention of those four paths or the selected formatter/location symbols. The curl/tar/rg pipeline statuses were `0 0 1`, meaning successful acquisition/extraction and no matches. A positive changed-query control found `+++ b/Lib/compileall.py` with statuses `0 0 0`. This is a bounded patch-path audit, not a whole human review of all patch bodies. The selected packaging rules show the build's patch stamp and reported series; none modifies the four selected files in that block.

1. `compile.c` lines 3948–3972, 4911–4930, 5070–5117 are byte-identical to the saved v3.12.0 excerpt. RAISE_VARARGS retains `LOC(s)`; ordinary CALL receives `LOC(e)`, passed through the helper even after argument expressions are visited. Thus the final raises and the actual failing plain calls retain the previously derived statement/call spans.

2. `pythonrun.c` lines 688–833, 887–916, 1524–1599 are byte-identical to the saved v3.12.0 intervals 688–833, 887–916, 1495–1570. String-valued SystemExit is printed raw with LF and status 1 before ordinary traceback handling. The normal exception path still uses the ordinary excepthook/traceback display routes. Integer-SystemExit overflow behavior is not needed for these controls.

3. `traceback.c` lines 490–596 and 619–966 differ from the saved v3.12.0 intervals only by the saved selected diff: the new formatter converts character offsets to display widths before printing carets. Indentation stripping, four-space display indent, CALL/RAISE lack of secondary anchors, default `^`, and whole-stripped-line suppression are unchanged. The new `Parser/pegen.c` lines 37–52 explicitly return the original character offset for ASCII segments. Every relevant source line in the charged derivation is ASCII, so the new conversion is the identity here. No unicodedata import is reached on this ASCII fast path.

Consequently, within the charged derivation's exact source conditions, `main()` and final whole-line raises still have no caret line; the producer authorization CALL retains nine spaces/twenty carets, and the nested load_pinned CALL retains eleven spaces/thirty-seven carets. The two string-SystemExit controls retain one message line and no traceback. All seven retain status 1 and empty stdout under healthy normal startup/output conditions. The seven branch/line/path derivations themselves were not reopened; no source or runtime bodies outside the charged documents were read.

## Evidence and scope

The official [Ubuntu minimal amd64 package](https://archive.ubuntu.com/ubuntu/pool/main/p/python3.12/python3.12-minimal_3.12.3-1ubuntu0.16_amd64.deb) has SHA256 `3535ddab53a2f39f8cda32250bbf5bb066616f5902b642d15ef56047f83911d3`. Its control metadata identifies Package `python3.12-minimal`, Version `3.12.3-1ubuntu0.16`, Source `python3.12`, Architecture `amd64`. The executable was streamed from the archive directly into SHA256; it was neither installed, saved, nor executed. This ties the prior-worker binary bytes to the published payload without requesting a reproducibility build.

The trust tier is ordinary Ubuntu-distribution trust: authentic HTTPS archive content, faithful binary/source package correspondence and build toolchain, intact standard native/library closure, and unmodified ordinary execution. The embedded source-descriptor PGP signature was retained but NOT independently cryptographically verified. Whole binary equality does not authenticate a future host, source installation, runtime hooks or shared/native closure. No claim is made that package identity alone supplies them.

Preserved prerequisites include the exact administrative source paths/ASCII bytes, flags `-E -s -S -B` without `-X no_debug_ranges`, ordinary available position tables, readable source, normal sys.excepthook without embedded audit/tracing customization, no exception notes, correct invocation/control preconditions and healthy stderr/flush. Flags suppress environment/site influences but do not replace build/native custody. Stream/import/DMI/ACL/resource failures remain STOP, not alternate acceptable output.

## Remaining boundary and controls

No selected-path discrepancy remains for this nominated published package on those assumptions. The remaining GAP is operational identification: a future independently selected worker must be bound to the qualified executable/package/native closure and unchanged installation/invocation. The cheapest remaining check is the already-required read-only native/package/source pin comparison at registration, not an interpreter trial or failure-byte calibration. This task does not perform or authorize that check.

Changed-object control: replacing an ASCII source prefix by wide Unicode can make the newly added display-width function change offsets; this is why the result is not a byte-identical-formatter or all-Python-3.12 claim. The actual diff and ASCII fast path are load-bearing. The patch-audit positive control checks the negative path search is not an empty stream.

No mathematical source/result, resource feasibility, package update, scientific/dummy execution, optional hardening or policy mutation is claimed. Only the existing documentary artifact transaction ran under Python; CPython source was treated as inert text.

## Read and publication scope

All six local inputs were pinned before their body reads; PINS, DERIVATION and all three saved excerpts were fresh WHOLE reads. The first combined display was clipped after the traceback portion; pythonrun and compile were immediately reread untruncated, with no missing excerpt portion counted as read. `native.stdout` was hashed whole but read ONLY lines 1–15. No source/runtime entries merely listed in PINS were followed. External full-source files and archives were streamed for hashes or selected text only; none was unpacked wholesale. EVIDENCE.json gives exact URLs, pins and selected intervals, and custody.json gives every current local input and owned pin.

Own report and all eight documentary files received untruncated WHOLE readback by 04:30:49 UTC. All six local input pins and all owned documentary pins matched; external archive and four source-file pins were rechecked unchanged. OPEN review found only the explicitly typed future-worker identification GAP with its cheapest check, not an unfinished compatibility argument. Report/manifest destinations remained absent before finalization; collision NONE. Authored scope is confined to this report transaction and its same-tag box; no shared or prior frozen file was edited. Expected transaction verification and custody are recorded at terminal handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8524`.
- Body SHA-256:
  `0c310d325f898f7003155149c7aff403714d8da0141490e804c1a1974172c306`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
