# F10 r1 quotient–remainder producer — static code preparation

Status: COMPLETE STATIC IMPLEMENTATION; INTERNAL UNREVIEWED / DISABLED /
UNEXECUTED. This is not a certificate, a runtime pass, a source-point result,
or an execution invitation. Accepted 17zg supplies the generic design; the
replacement implementation still requires independent review and validation.

First action was 2026-09-10 00:16:56 UTC, after confirming both new targets
absent. The controlling deadline is 00:39:00 UTC, with 00:36 publication
reserve; it was not reset. Output ownership is this report and
box/f10-r1-quotient-remainder-code-astra-20260910 only. Basis is
0d39df3c9fd69c939a8420c54d03228b9077777d, provenance rather than an exit price.

## Delivered source and exact delta

The package contains exactly five production modules. Only solver.py changes:

| Module | SHA-256 | Relation to frozen 17z source |
|---|---|---|
| solver.py | 58cdc4721143ec2be93cc720831c2235a9221b567f1903d2ffd6025b4f54b665 | replacement candidate algorithm |
| checker.py | 122842e5cf38a0eab2585c7e894c1ca9d9758dd643830d5447800642554fdf69 | byte-identical |
| evidence.py | cbe5a9e05c1718cd7911e68302611e0131774e10c501ca0fa890510d0ccb7767 | byte-identical |
| algebra.py | 7d565299faba1a8921fdb36f345af2cae49254fa59730e0e3c7a1f98e587d9dc | byte-identical |
| execution_gate.py | cbfe55ff11503cee094dc49e54b656d209806aa37ee30cc281902902152049c6 | byte-identical |

solver.diff is the literal text delta. Metadata comparison also establishes
that the complete main() tail, including its CLI and authorization-before-
imports sequence, is byte-identical. No helper, caller, supervisor, authority
schema, engine API, fixture or duplicate harness was added. All original
files remain untouched. Documentation is PINS.json, READ-SCOPE.md,
STATIC-REVIEW.md and the explicitly disabled VALIDATION.md plan.

## Implementation scope

generic_candidate(p, fs, q, flint) implements the exact shared dense Fraction
API. It checks rank-seven monicity, squarefreeness, all nine polynomials,
T-degree bounds and seven-coordinate shapes. The separately pinned additive
API-DELTA is implemented literally: a non-squarefree coefficient modulus
raises ValueError whose message is `generic modulus must be squarefree`.
The actual candidate(data, flint) still requires the original fixed modulus,
row IDs, dense slots, envelopes and both guard factors before converting to
the internal monic modulus. It cannot substitute a synthetic test modulus
for an actual source input. main() requires the existing root-issued genuine
source acceptance and exact source/environment pins; none is minted here.

Each split node projects and rescans all nine whole generators, selecting a
maximal-degree pivot with the first index breaking ties. A nonunit leading
coefficient causes a rational gcd split, retaining both coprime children.
Only that leading coefficient vanishes on the corresponding child; the code
does not assume that the whole generator vanishes. It bounds visits/splits,
checks the full leaf product, and retains every coefficient component.

All-zero and constant-unit leaves are handled directly. Positive-degree
leaves use monic T division over their finite coefficient algebra, without
assuming that the T-remainder algebra is reduced. Only exact rational gcd
identities certify inverses. All eight other generators contribute their
complete remainder multiplication maps, including zero and duplicate rows.
The one direct-sum coefficient matrix has at most 35 rows and 280 columns.
Appending the target and full identity gives at most 35 by 316 for its sole
RREF call. Immediate branches require none. These are design bounds, not
observed sizes or a speed claim. No full 217-by-1638 search matrix is built.

For UNIT, exact monic division reconstructs N/fhat and then divides by the
certified RAW leading coefficient. CRT recombines all nine multipliers and
checks each idempotent on every leaf. All original 1638 slots, through
degree 25, are padded and serialized as canonical rational-string pairs.
For SEPARATOR, the appended full identity gives a functional on all of C,
not just the image span. Its pullback is evaluated on all 217 old basis
coordinates. The all-zero component branch similarly pulls back an exactly
normalized rational coordinate. The unchanged independent checker remains
responsible for the full identity or every one of the 1638 annihilations
and target value one. A rank flag, trace or CANDIDATE-ONLY status proves
nothing without that check. No field selection or discarded component occurs.

## Custody and manual review

Fifteen inputs are charged: the twelve objects in root PINS, that PINS itself,
INTERFACE and the additive API-DELTA. Hash checks preceded bodies or explicit
same-byte prior-WHOLE reuse. READ-SCOPE lists the exact fresh and reused
whole reads. All fifteen matched again at 00:24:27 UTC; final current pins
are included with custody. No provenance link, current peer/harness body,
actual coefficient artifact, receipt, mutable ledger or uncharged science
was read. The root qualification about completing mu to all of C and the
leading-coefficient-only child statement are adopted, not the incidental
overbroad wording in the gate.

Whole own solver and sibling sources were reviewed as text; STATIC-REVIEW
records the paths checked. The four sibling and main-tail comparisons are
documentary byte comparisons, not syntax or runtime tests. Inline metadata
commands only read/hash/compare text and serialize custody. The existing
transaction tool handles begin/close/finalize/verify. All authored edits and
copies use apply_patch. No mathematical subprocess, syntax/AST check,
compile/import/test, polynomial or matrix emission, network/AWS/SSH/process
inspection, package probe, allocation, agent or protected/shared edit occurred.

## Remaining checks and scope stop

OPEN quantities: zero identified missing implementation paths from this
manual review; one independent joint static review and one finite generic
validation batch remain unperformed. The cheapest next check is root's
single different-model review with the separately frozen harness against
INTERFACE/API-DELTA. Any runtime needs a new root registration. All worker,
cwd, acceptance, authority, profiles, environment and deadline fields in
the prospective plan are disabled/null. No cap recommendation is a measured
performance result. Failed/unsupported execution must remain nondecision;
there is no fallback, automatic retry or second solver call.

No new mathematical OPEN ID is raised. COLLISIONS: EMPTY within the two
owned output targets; originals are unchanged. The own whole/read-scope,
quantity-and-cheapest-test and collision checks precede the completion
marker. Terminal custody and expected transaction will be handed off first,
after publication verification; all writers then IDLE. No follow-on or
execution authority is assumed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6942`.
- Body SHA-256:
  `e8bf4395d613085bee43af9a635da2f9171838e9ffd02b69d70ad5a22dd67601`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
