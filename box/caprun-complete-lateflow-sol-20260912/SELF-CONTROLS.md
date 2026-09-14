# Documentary self-controls

No source, template, caller, helper, installer, runtime, syntax checker, AST checker, test, CAS, dummy, SSH, AWS, worker, holder, FIFO, or scientific command was executed. These are manual source controls only.

- Disabled control: `FROZEN-CONSTANTS.template.json` has `armed:false`, `UNREVIEWED_UNBOUND`, and unresolved tokens; `RECIPE.js` requires a separately created bound file and a different-model-reviewed state.
- Attestation separation: invocation one stops after writing observation bytes. `attest.template.sh` is not invoked by `RECIPE.js`; invocation two requires the separately created decision and matches its observation hash, four prepared pins, flags, context, and freeze token.
- Release separation: `RECIPE.js` ends at `INSTALLED_NOT_RELEASED`; it contains no FIFO write. Only `release.template.sh` contains the fixed one-frame write and it rechecks PID/start/invocation, registration hash/mode, FIFO identity, the original absolute stops, and elapsed monotonic time from the original holder start.
- Fourteen-file census: nine expected authority references plus registration, card, three-entry manifest, installer, and summary. Candidate patch/readback requires all fourteen exact hashes.
- Installation census: staging contains registration, card, manifest, installer, and the exact native-list bytes only. The unchanged final installer copies registration and card only. Nine authority references and SUMMARY remain documentary and never enter the live output mount.
- Freshness/no retry: observation and decision use add/no-clobber publication; remote stage requires all five targets absent; failures preserve evidence and provide no retry, replacement, second holder, cap increase, or cleanup.
- Empty-child control: observation explicitly requires `authority`, `frozen`, and `writer` empty and each of nine cgroup leaves empty/domain/unpopulated. It does not rerun the stronger whole-mount-empty predicate after outer stdout/stderr exist.
- Clock control: observation, recipe, attestation, installer source, and release each preserve original absolute admission/holder stops; observation and release measure elapsed time from the observed original `/proc` start tick against 120 seconds. No phase clock is rebased at release.
- Authority-writer control: runtime dispatcher remains sole O_EXCL authority creator. Preinstalling any one authority remains a deterministic STOP, never a repair.

GAP[BOUND-PACKET-REVIEW]: no batch, worker, host, clocks, paths, receipt, native bytes, holder token, or bound descendant is selected here. Quantity: one complete bound administrative packet and five commands/scripts. Cheapest test: different-model source review plus documentary full-byte substitution/pin comparison, estimated 20 minutes; no live execution.

GAP[LIVE-LATENCY]: the complete observe/attest/caller/readback/stage/install/release wall is unmeasured and must fit both the remaining original 120-second monotonic interval and original absolute stops. The historical 365 ms is charged only to caller/patch/readback. Quantity: end-to-end remaining milliseconds. Cheapest test: a separately authorized no-science exact live attempt under existing caps, estimated under 120 seconds; not authorized here.
