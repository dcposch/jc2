# FIRST Fable5.1: necessary-row combined source/runtime DELTA gate

charged_input=box/f10-necessary-rows-delta-gate-prep-root-20260911/old-produce.py
charged_input=box/f10-necessary-rows-producer-astra-20260911/produce.py
charged_input=box/f10-necessary-rows-producer-astra-20260911/produce.diff
charged_input=box/f10-necessary-rows-delta-gate-prep-root-20260911/old-authority.py
charged_input=box/f10-necessary-rows-producer-astra-20260911/authority.py
charged_input=box/f10-necessary-rows-producer-astra-20260911/authority.diff
charged_input=box/f10-necessary-rows-delta-gate-prep-root-20260911/old-check.py
charged_input=box/f10-necessary-rows-checker-astra-20260911/check.py
charged_input=box/f10-necessary-rows-checker-astra-20260911/check.diff
charged_input=box/f10-necessary-rows-delta-gate-prep-root-20260911/old-dispatch.py
charged_input=box/f10-necessary-rows-runtime-astra-20260911/dispatch.py
charged_input=box/f10-necessary-rows-runtime-astra-20260911/dispatch.py.diff
charged_input=box/f10-necessary-rows-delta-gate-prep-root-20260911/old-probe.py
charged_input=box/f10-necessary-rows-runtime-astra-20260911/probe.py
charged_input=box/f10-necessary-rows-runtime-astra-20260911/probe.py.diff
charged_input=box/f10-necessary-rows-delta-gate-prep-root-20260911/old-mutate.py
charged_input=box/f10-necessary-rows-runtime-astra-20260911/mutate.py
charged_input=box/f10-necessary-rows-runtime-astra-20260911/mutate.py.diff
charged_input=box/f10-direct-rows-powerfix-astra-20260911/arithmetic.py
charged_input=box/f10-direct-rows-checker-astra-20260911/check_arithmetic.py
charged_input=box/f10-necessary-rows-root-20260911/ROOT-ADOPTED-NECESSARY-ROWS.md
charged_input=xmodel/f10-necessary-rows-design-gate-fable5-20260911.md
charged_input=box/f10-direct-rows-deployment-prep-root-20260911/ROOT-SOURCE-CONTRACT.json
charged_input=xmodel/f10-direct-rows-code-gate-fable5-20260911.md
charged_input=xmodel/f10-direct-rows-runtime-gate-fable5-20260911.md
charged_input=box/f10-necessary-rows-delta-gate-prep-root-20260911/ROOT-NECESSARY-ROWS-CANDIDATE.json

EXACT26 immutable inputs at {{LANE_INPUTS}}, unique basenames. Hash ALL26
before ANY body. The six old-*.py files are byte-identical aliases of the
predecessors, created only to avoid adapter basename collisions. Match:
8a7bd82ea589744a9de22b54877156a329d724185948538958801475f983760e  old-produce.py
5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a  produce.py
592df59a401a2bf292b36214496b748cf6370c17f6bf65319db67e6245a210c4  produce.diff
5629db5df0a37fdaecaa66f5ad0cde47006cb0c3047b37243b045daedef2ac29  old-authority.py
804c7aff56538fc332bf68638b03b7167eccdb49f73337f1a5f1823348b522a4  authority.py
6d74b9d7c879ad921a0c72f71d1a67d13fce933daa0b796653077487662f5c47  authority.diff
5052884779d781e55693115c3065db1207667ce224a5914bbb95721d0abe9f7b  old-check.py
1d2d5b5408bfbf13b96f09453b1f14dfe884d261e702843bc31e5a043ffa53d1  check.py
7ba8b176f40c37c9643856135f4d8a17fbe9d3f08b148f39c685c8158fc07044  check.diff
f5b6e6c43da4574c1dd9fc241d2f0596071ab505d561e67579eb28d382814480  old-dispatch.py
073e22dbcfa3a11a2afaf6fd9c845ca6ad1d0038ccd3fddc22db21e9f5beeb24  dispatch.py
f3c61b9a40d16e953950e3ff6a65401475a719fae6dbe3e1386cd05c49ef515f  dispatch.py.diff
09845fabff9a8b7f997e3b2d01160e5ff51d728124b9f5cd0b7176f8c19ea063  old-probe.py
5f1211e1a77b5ce2bb4cc496deabc533e3c41cdea88ea750149dac886cc09c69  probe.py
6fccfd82949cc678b4c423690e098e02f902e0a62f89d9efed5c2c6dee386432  probe.py.diff
cc0621aa44d17b1dac346e87d20a53f69ce950b343d68c8ed0d3791d42120af0  old-mutate.py
12eac7bbe5566ac0372c51b36617409e0501595024d948d6086a767f90d84eec  mutate.py
f5e3967d1603fb3e02ed0cb4a21ab306c866227f4e892a2f5c79414f2e19ed73  mutate.py.diff
acd07f800707c379aba60bd06f239d38cd83c86867729561367abd2bcc04ce73  arithmetic.py
9d2aac637dbdeaa192cc3fe531e83694f9853b6573556ad5d49362f754b1163e  check_arithmetic.py
176363939a8aa6861995cd72a99c61f7d04bfeab5a9634f6d3143dcd3d3bd098  ROOT-ADOPTED-NECESSARY-ROWS.md
8e07e419d321b09ecd13c61a1c5fdc3dbaf9a099c1a1ebedf9b9fe6ef280073b  f10-necessary-rows-design-gate-fable5-20260911.md
feef0643e84fbd28307c3bd3469fba974fa6b7f58ed0ef42bc2f92aa3c597aa3  ROOT-SOURCE-CONTRACT.json
0d6cb121ebdd769fb909608043b38e6ef08923d6e6a0411ca5ec057325169784  f10-direct-rows-code-gate-fable5-20260911.md
a02f120acda2439197a9fc173ec068ec0a5a208ec8d15f6b96cc9dfe65ee6ff9  f10-direct-rows-runtime-gate-fable5-20260911.md
7beffe39c68b19e2998edc02949f8d24b3fe55a925d53139dff1c27a6690a482  ROOT-NECESSARY-ROWS-CANDIDATE.json

READ SCOPE IS EXPLICITLY DELTA, not a new full-code/foundation review.
Read all SIX .diff files and all SIX documents/JSON FRESH_WHOLE through
EOF/Seal, recovering any clipped ranges. Both old/new versions of each of
the SIX changed source files are complete pinned objects: independently run
TEXT diff on each pair, compare EVERY hunk with the retained diff (only the
first two filename/mtime header lines differ under snapshot aliases), and
read the changed contexts and any additional portions necessary to test
composition. Record actual ranges. Do not call DIFF/CONTEXT/HASH_ONLY a fresh
WHOLE source read. arithmetic.py and check_arithmetic.py are HASH_ONLY at their
unchanged accepted pins; no repeat arithmetic review. You may expand a source
context read if a specific doubt requires it, recording the scope honestly.
No linked provenance or mutable/live/uncharged inputs. Accept unchanged
predecessor semantics only at the exact imported FIRST scopes below.

Own ONLY xmodel/f10-necessary-rows-delta-gate-fable5-20260911.md and
box/f10-necessary-rows-delta-gate-fable5-20260911/input_custody.md.
First action: actual UTC, own-target absence, skeleton WITHOUT marker.
ORIGINAL reserve2026-09-11 06:39UTC/HARD06:42UTC NEVER RESET; ROOT latestlaunch
06:21. Absolute TERM/KILL+5sec armed before launch. apply_patch only via
/home/ubuntu/.codex/tmp/arg0/codex-arg0KG6wa7/apply_patch, bounded writes
under1500words. Finalize both owned files, all26 postpins and own WHOLE readback,
remaining quantity/cheapest test/numeric UNMEASURED planning wall and own-only
collision statement. Append unique standalone <!-- BODY-END --> LAST.
Adapter seals; author no Seal, charge_basis, transaction or other artifact.
No Write/Edit/redirection into owned files; ALL WRITERS IDLE after marker.
At reserve seal honest PARTIAL/GAP, never extend clocks. No retry authority.

STATIC SOURCE TEXT AND MANUAL REASONING ONLY. Zero scientific subprocess/
import/AST/syntax/compile/test/CAS/dummy ANYSIZE, coefficient/candidate/fixture
generation, prime/place computation, network/AWS/SSH/process control/Git/
agents/protected access. Metadata hashes, date, bounded text reads/diff/awk/
sed and apply_patch are allowed. Do not implement or edit any source. Ordinary
text diff is not source execution. No new whole-foundation audit.

ROOT custody context: all three Astra owners independently COMPLETED before
custody-FIRST, all input/output pins and expected report transactions verified,
reports/diffs read WHOLE. Producer/authority and checker complete old/new text
equals only the prescribed deletion/literals; runtime complete old/new text
equals two replacements only; every actual diff equals retained bytes. These
are ROOT assertions to CHECK independently, not substitute for the delta gate.
All scientific source remains UNEXECUTED. No model or AWS worker is held idle.

Charged imports:
- ROOT-SOURCE-CONTRACT.json binds accepted26z: old code FIRST A-E plus its ONE
  exact prescribed power correction already reflected by arithmetic.py pin
  acd07f80. The report's generic support, cap-sufficiency and speed estimates
  are NOT accepted and must not be repeated. No foundation rereview.
- Old runtime FIRST accepted27z: A-F at static source/runtime interface scope,
  conditional on exact source, seven text-derived refusal triples and genuinely
  new ROOT registration. Its optional inverse-restoration hardening is OFF:
  saved-slot restoration proves only outside-slot and serialization fidelity,
  not arithmetic inversion. Inherited ESRCH false-STOP and cap uncertainties
  remain, not a new repair task.
- New design FIRST28z accepts dead-branch dependency and the SAME25row/guard
  source-exclusion chain at banked23z/19z scopes. It requires authority TAG/hash
  rebinding. ROOT-ADOPTED-NECESSARY-ROWS fixes the exact minimum source/runtime
  edit boundary and spares the direct-source T error.
- ROOT-NECESSARY-ROWS-CANDIDATE.json binds the exact five-source/three-runtime
  vector and NEW scope. It is disabled/pending this review, not a registration.
  Inspect those bindings and the new contract, do not invent missing live facts.

Give separate CONFIRMED/REFUTED/GAP A-E, precise old/new lines and smallest
blocking correction; distinguish actual defects from explicitly pending ROOT
release obligations. Task is exactly one combined focused source/runtime gate:

A. Exact scientific delta. Independently verify old produce.py265-277 deleted,
only two obsolete length conjuncts removed at old332, len(scale_record)!=13
and raise retained; schema/job/success only at prescribed sites. Checker
old390-404 deleted including comment and two lengths; schema/job/success
literals only. Authority only TAG changed. All other bytes unchanged,
including old internal .direct-rows- mkstemp prefix and comments; independent
arithmetic hashes unchanged. Match new sourcevector in candidate contract.
No copied/dummy inverse list or new wire record. Under accepted28z this
exactness should preserve retained graph/diagnostics; identify any additional
dependency the delta actually changes, not a re-review of the accepted lemma.

B. Runtime delta and literal closure. Independently compare the three pairs:
ONLY global direct-rows->necessary-rows and DIRECT_ROWS->NECESSARY_ROWS.
No direct-source/generic direct/native-closure/CAPRUN rename, no algorithm,
cap/profile/order/predicate/argv change. Trace new job, runtime/phase/policy/
preflight/mutation/custody schemas, positive stdout hash, dispatcher positive
and final status, wrapper expectations and checker entry tags. The EXACT T
rejection remains stderr "CHECK FAILED: direct-source graph slot T\n",
normalexit2, emptyout. It must still be the individual slot comparison,
not aggregate/parser/hash/authority/traceback or generic nonzero rejection.

C. Source-authority-runtime composition. New authority TAG and five-file
files vector + absolute source_pins include authority itself; same four-key
metadata-only API / eleven-key authorization / actual absolute entry argv.
New producer/checker wire schema/job and contract/source vector equality
compose with new dispatcher and mutator. The mutator still requires an actual
new positive checker record, reconstructs the check-positive authorization,
and receives a fresh fixture artifact digest before negative checker. No old
ROOT receipt or source hash may substitute. The candidate's five and three
pins must match charged actual bytes. Seven exact refusal triples and actual
physical/native/absolute-path registration are explicitly pending; do not
mistake disabled metadata for a ready release. The old source frame numbers
are changed by deletions and must be rebound, not inherited as live policy.

D. Full-source implication and honest service. At accepted23z/19z/28z scopes,
same alternative25rows vanish in canonical LOCALIZED A=(B[X]/I)[g^-1], B the
entire degree7 field, and g' maps to its original unit. A genuine place-bound
nonzero297minor implies rank297 over B, g' in the row ideal and A=0. Canonical
inverse polynomiality stays a SOURCE HYPOTHESIS, not a numerical property of
the alternative. Omitted alternative Laurent-q inverse/pole coefficients are
NOT_COMPUTED, not zero/ordinary/checked. Old acceptance-domain equality is
not claimed; deleting branch-local cap/envelope/list stops is explicit.
All125denominators/15scalar nodes, forcing/bands/matrix products/installation/
Euler gauges,108/45/63,22readbacks,150diagnostics111/39, Laurent-S auxiliaries,
SCALE13/sixgroups and SAME25rows/guard remain. No canonical matrix-rank,
unsaturated-ideal equality, source point, all-r or JC2 conclusion.

E. Readiness at the exact gate boundary. Is this candidate vector statically
ready for the remaining exact-refusal/ROOT-registration binding and then ONE
capped13phase AWS observation? No current registration or execution approval
is assumed. Name source/runtime defect versus missing deployment field.
No rank client before actual independently checked graph plus fresh exact T
negative. Remaining SCALE/graph/diagnostics cost is UNMEASURED; unchanged
caps are refusal ceilings, not measured feasibility. Badplace/anomaly/cap/
noncompletion => NONDECISION. No optional inverse hardening, capraise,
streaming framework or repeat foundation task.

Target1400-2200 substantive words. Planning15-20minutes UNMEASURED within the
ORIGINAL06:39/42 clocks. No new canonical OPEN ID. All26 postpins and honest
read scope before own WHOLE+marker. One report only.
