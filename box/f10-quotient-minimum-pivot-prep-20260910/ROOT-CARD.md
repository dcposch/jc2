# ROOT card — bounded minimum-degree quotient-kernel redesign

ROOT request2026-09-10 after one actual quotient run STOPped at CPU550,
wall550.17427131/samplegrouppeak1194852352B with NOcandidate, no checker/control
dispatch, no stage trace. Actual failure report4bd18a01 is an OBSERVED,
not independently reviewed runtime promotion; do not diagnose a bottleneck
from it. Old full217x1638 run17zf also CPUstopped. No unchanged rerun/capraise.

One concrete task: prove or refute that accepted17zg's deterministic
MAXIMUM-degree pivot can be replaced by the MINIMUM degree among NONZERO
projected generators, default-1 only when allninezero. Recompute after both
children of every nonunit-leading-coefficient split. Keep all components.
If sound, implement ONLY that selection rule/comment delta in solver.py
and the corresponding literal solverSHA substitutions in the two accepted
callers (generic54c55be3, actuala7c0cf17). Do not transplant either caller.
No stage instrumentation, other algorithm, supervisor, scope or CLI change.

ROOT motivation (a hypothesis to verify, not accepted new theorem):
for any monic pivot degree1<=d<=5, quotient remainder columns with j<d still
span the ideal; other fi degrees<=5, so deg(hi fi)<=d+4<=9 and deg q^5<=25
still yield raw pivot multiplierdegree<=25-d. Thus maximal degree may be
unnecessary. Minimum-degree selection might reduce rows, but NO actual
positive minimum degree or timing/height improvement is established.
Prove both UNIT and SEPARATOR read-back, allzero/constant cases, split
termination, all1638columns/217target semantics, and olddegree25 bounds.
Countercontrol requiring smaller pivot: f1=T^5,f2=T,others0,q=T; constant
non-first pivot control f1=T^5,f2=1. These are manual changed-choice controls,
not computed source fixtures. Do not assume B a field or C reduced.

Accepted premises17m complete generic contract,17zg quotient design,
17zh currentkernel/harnessstatic,17zk genericcaller,17zm actualcaller.
Current sources are frozen independently reviewed text. The unchanged
generic harness is NOT an input or a new success claim. Existing source
schema degrees<=5 are sufficient for this proof; no coefficientbody needed.
Every other scientific sibling/checker/harness remains BYTEUNCHANGED.
If unable to prove selection sound, no new executable; seal REFUTED/GAP.

Exactly8 charged files are thiscard,17zgproducer/gate,17m gate,
current solver58cdc472, current genericcaller54c55be3, current actualcaller
a7c0cf17 and ROOT actualfailure report4bd18a01. Source acceptance or runtime
authority is NOT delegated. Hashcurrent allbeforeWHOLE; no corpus/ledger reads.
Own ONLY xmodel/f10-quotient-minimum-pivot-astra-20260910.md plus transaction,
box/f10-quotient-minimum-pivot-astra-20260910/. If sound, own newsolver.py,
new generic_dispatch_batch.py and actual_dispatch_batch.py; old snapshots
with distinctnames, regenerated literal diffs, readscope and pins.
Use apply_patch for files/copies. Hash-only metadata calculations allowed.
ZERO mathematical subprocessANYsize/AST/compile/syntax/import/tests/fixtures/
CAS, no network/AWS/SSH/proc/agents/Git/protected/shared/instrument edits.
Existing transactionalpublication tool allowed, no new helper executable.

Original cap earlier first+18minutes and03:24:00UTC, reservefinal2minutes,
NEVERRESET. Target absence beforewrites; begin->close->finalize->verify.
TerminalcustodyFIRST/allcurrent+ownedpins/expectedtransaction/WHOLE,
ALLWRITERSIDLE. Newmathematics/code STATIC-UNREVIEWED until FIRST Fable.
Do not start review, runtime, worker, generic farm or follow-on.
