# Mixed-univariate runtime v2 repair

Status: **DISABLED / UNEXECUTED / UNREVIEWED / UNREGISTERED**. First action:
`2026-09-12T19:47:38.969898402Z`. No worker, authority, runtime fact, installed
path, or mathematical result was created. The prior packet remains unchanged.

## Result

The three-file derivative repairs the five specified source-static blockers
without changing CAPRUN, the delivered scientific files, the six phases, or
any cap. `dispatch.py` is the only executable derivative;
`REGISTRATION.disabled.json` remains false/null; `CONTRACT.md` states the
deployment and negative-control obligations.

## Exact old/new changes

1. Registration schema advances v1 to v2. Paths replace ambiguous `tmpfs`
with exact `mount`, `output`, and `admin`, and add `dispatcher`. Pins cover the
dispatcher plus the unchanged CAPRUN/probe/setpriv/interpreter/scientific
files. The dispatcher requires its registered path to equal `__file__.resolve()`.
UID and GID must be exact positive `int` values, so booleans and root are
refused. Authority/producer/checker must share one canonical source directory;
the interpreter path must use canonical spelling. Authority's unchanged
four-item scientific source vector is preserved.

2. The bounded writable mount is canonical, a mountpoint, root-owned exact
0755. Its initially empty exact siblings are root-owned `admin`0755 and
scientific-UID-owned `output`0700. Authorities, negative inputs, frozen
candidate and summary go only under traversable non-science-writable admin;
all stdout/stderr/telemetry/receipts/producer outputs and environment cache/temp
roots go under output. ROOT copies the candidate by O_EXCL/write/fsync/chmod0444/
reread into admin before checking; the UID cannot rename that entry. Physical
tmpfs type/256MiB capacity and final exact census remain qualification facts.

3. Every scientific argv remains exactly `PYTHON -E -s -S -B SCRIPT ...`.
The generated authority holds exactly `sys.argv` from SCRIPT onward and only
the typed authority-SHA slot is replaced. No extra interpreter flags exist.

4. Parser control now uses a duplicate top-level JSON key and requires CAPRUN
NORMAL_EXIT with child1, empty stdout, exact `STOP: duplicate JSON key\n`
stderr, and absent output/receipt. Identity control requires actual changed
bytes/SHA, exact A1+1, exact A1-1 canonical restoration to original WHOLE bytes,
normal child1, exact full-identity failure stderr, and absent output/receipt.
Exception control multiplies all A1/A2/N by 7t-12, requires changed bytes/SHA,
uses an exact Fraction recurrence to divide it back and demands original WHOLE
bytes, then accepts only normal child2 plus complete output bound to the mutated
SHA with sole exceptional value `"2"`. Positive check first requires an empty
exception list. Thus an authorization/parser/cap/runtime refusal cannot count
as either semantic control.

5. Every accepted normal phase records telemetry, stdout and stderr digests;
final summary is written only after all exact predicates. Resource-cap or
abnormal control exits cannot be summarized as success. The descendant dummy
and its identity-matched cleanup predicates are unchanged.

## Manual static controls and remaining boundary

Literal trace against `authority.py` confirms admin0755 permits the nonzero UID
to traverse and read root0444 authority/input/candidate files. Lexical output
names are constructed solely beneath the canonical sibling output directory.
The inverse recurrence uses q_k=7a_(k-1)-12a_k, starting a_-1=0 and separately
checks the top remainder; no floating or CAS arithmetic is used. These are
source-static observations only; no interpreter, syntax, import, test, dummy,
fixture, CAS, AWS, or native command ran.

There is deliberately no worker authorization from a qualification hash.
ROOT must still independently prove installed immutable ancestry, complete
native/import closure, exact environment and full source postpins; one-cgroup
containment/no delegation/no migration; fair-class cpu.max semantics with no
scheduler escape; burst zero; separately armed original deadline; qualified
memory.max temporary-overshoot semantics; actual bounded tmpfs; terminal
cgroup emptiness; exact output census/durable custody/cleanup. These are
deployment predicates, not claims of this source packet. Source-static FIRST
and installed qualification are mandatory. Any missing item is STOP, with no
retry, cap increase, second gcd, farm, or automatic follow-on.

## Pins and read scope

`box/f10-mixed-univariate-runtime-repair-sol-20260912/PINS.json` gives every
input/output SHA. Fresh WHOLE reads covered COORDINATION; prior custody and all
four old runtime files plus old PINS; delivered authority template, producer,
checker, CONTRACT and VALIDATION. No live peer payload, protected tree, public
mirror, scientific dependency, or uncharged source was read. Output WHOLE
readback and all input postpins are required immediately before custody.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4975`.
- Body SHA-256:
  `662b6f149dd41dc57a486fa4539e64f194c3f575fa238c19d4944b33d4f7ae3e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
