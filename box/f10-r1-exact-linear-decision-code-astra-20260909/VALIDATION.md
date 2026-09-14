# Disabled exact-linear decision implementation and validation plan

STATIC / UNEXECUTED, including syntax. No matrix, certificate, rank, source
coefficient, fixture or verdict was computed. No worker is assigned. All
profiles and clocks remain null in the disabled registration. No installation,
second engine, factor, prime, representation or automatic retry is implemented.

## Exact mathematical framing

Use the complete accepted finite-etale B=Q[v]/p(v), not a selected field.
The nine row ids are E1/S1,E1/S2,E1/S3,E0/S1,E0/S2,E0/S3,E0/S4,P4,P11.
Their dense envelopes are 3,3,2,4,3,3,2,2,5; all slots remain present, even
when zero or redundant. q has six dense slots through degree5, and its
named factors are exactly r,h0. The independent checker also multiplies
the two dense factors to recheck q directly. No original-source rebuilding
or actual univariate artifact is an input of this preparation.

The sole matrix is 217 by1638: row(k,a) has0<=k<=30,0<=a<=6;
column(i,j,l) has0<=i<=8,0<=j<=25,0<=l<=6. The producer augments it
to [M|q^5|I217], width1856, and calls fmpq_mat.rref() ONCE.
No count of nonzero coefficients, bit length, bytes, time or RSS is known.

## Why extraction is valid, independent of flags

Let E be the invertible rational row-operation matrix represented by the
last217 columns of a correct RREF. Since the identity block is present,
the augmented matrix has rank217. A pivot in zero-based column1638
has all M entries zero and target entry1, so the same row of E is a
separator lambda with lambda*M=0 and lambda*b=1. If column1638 is
not a pivot, set all free M variables to0 and every M-pivot variable
to the corresponding reduced target entry; rows with pivots in the
identity block have M=0 and b=0. This gives Mc=b. An API failure or
incorrect extraction cannot become a verdict: checker.py reconstructs
the complete identity without using the RREF or any matrix supplied
by the producer. It checks all217 coordinates for UNIT or all1638
columns and all217 target coordinates for SEPARATOR.

The certificate is JSON with explicit schema, dimensions, basis orders,
branch, input/receipt/root-acceptance binding, solver hash and rational
witness pairs [numerator-string,positive-denominator-string]. A UNIT
witness has1638 pairs, a SEPARATOR217. Reduced canonical zero is
["0","1"]. Floats, duplicate JSON keys and nonfinite numbers are rejected
at the evidence boundary; independent mathematical parsing rejects
noncanonical rationals as well. No polynomial expression eval occurs.

## Authority and future ROOT-owned acceptance

Every mathematical main calls the unchanged authorize before importing
the arithmetic backend, Fraction or FLINT, or allocating a matrix.
The pure verify/candidate functions are not standalone CLI authority;
a future in-process harness must itself pass authorize first.

ROOT must first issue a fresh, reviewed acceptance file, never generated
by this package. Filename ROOT-UNIVARIATE-ACCEPTANCE.json; its SHA is
univariate_acceptance_sha256, its exact JSON is univariate_acceptance
in the external dispatch registration and every per-operation authority.
Required acceptance fields:

- schema F10-UNIVARIATE-ACCEPTANCE/v1;
- status ROOT-ACCEPTED-GENUINE-UNIVARIATE-CHECKER-RECEIPT;
- univariate_sha256 and receipt_sha256;
- adapter_sha256, checker_sha256, backend_sha256,
  input_evidence_sha256 at the frozen versions in evidence.py;
- input_evidence: the exact five-field normalized/original-source
  provenance dict also present in the genuine artifact and prior fullreceipt.

A correctly spelled receipt does not prove execution. Root-issued
acceptance after independent terminal-custody review is an explicit
cooperative trust boundary. This task does not assume the pending runtime
gate has passed, does not issue acceptance, and does not read its result.

Local staged files for a FUTURE run: solver.py, checker.py, evidence.py,
algebra.py, execution_gate.py, probe.py, dispatch_batch.py,
semantic_controls.py, unchanged run_capped.py, admissibility.md,
frontier.json, univariate.json, univariate.full.receipt.json,
ROOT-UNIVARIATE-ACCEPTANCE.json. Also pin /usr/bin/python3 and every
ROOT-selected installed FLINT/native dependency file. The package does
not discover or certify that closure. No accepted original helper or
CAPRUN byte is changed. The upstream adapter/checker/evidence hashes are
metadata versions; those same-basename source files are not staged here.

## Installed API uncertainty

The sole documentary API premise is root-api-note.md: official python-flint
0.9.0 documentation at https://python-flint.readthedocs.io/en/latest/fmpq_mat.html
describes the rational matrix constructor, fmpq numerator/denominator
construction, entry indexing and rref() -> (matrix,rank). No installed
version, package, extension hash, string formatting or cost was checked.
The code requires ROOT-pinned module path/hash and exact version before
import, checks actual __file__/__version__ after import, then uses the
documented matrix API. Missing/incompatible imports fail closed. Export
accepts only integer or numerator/denominator rational strings, canonicalizes
with Fraction, and refuses unsupported formatting; no general expression
parser/fallback exists. These exact installed calls and formatting need
one separately registered compatibility test, not an invented claim here.
Native dependency completeness is ROOT's documentary preflight obligation.

## Caller and literal sequence

caller.diff is the complete diff from the accepted univariate caller.
run() changes only the two per-authority payloads. The existing physical
identity, full parent/child vectors, source pre/post hashes, exclusive
outputs, immutable authority, no concurrent writer, no new inner PGID,
16MiB inherited file cap,15-second admission margin, stored absolute and
aggregate cutoffs, post-return deadline check and exact dummy cleanup are
retained. CAPRUN sampling/cleanup is not a strict real-time guarantee.

Five actual refusals, valid sentinel, descendant-RSS TERM/KILL dummy;
then one solver.main, one genuine checker.main, one bounded in-process
corruption harness. No repeated positive verification is performed by
the harness. All outcomes must be terminal and hash-bound before reading.
Any cap, missing dependency, refusal, unexpected failure or late return
produces STOP/NONDECISION and no retry/escalation.

Complete Python -I -B vectors (AUTHORITY is argv[1]):

- solver.py AUTH ARTIFACT PRIOR_FULL_RECEIPT ACCEPTANCE CERTIFICATE:
  sys.argv length6, full registered vector9;
- checker.py AUTH ARTIFACT PRIOR_FULL_RECEIPT ACCEPTANCE CERTIFICATE RESULT:
  sys.argv length7, full vector10;
- semantic_controls.py AUTH ARTIFACT PRIOR_FULL_RECEIPT ACCEPTANCE CERTIFICATE RESULT CONTROLS:
  sys.argv length8, full vector11.

The incoming receipt is univariate.full.receipt.json; the new independent
result is decision.receipt.json. Neither input is overwritten. The candidate
alone remains CANDIDATE-ONLY. The checker emits VERIFIED-GENERIC-ZERO-QUOTIENT
or VERIFIED-GENERIC-NONZERO-QUOTIENT at17m's exact scope, never a source
point, multiplicative character, maximal-degree result or JC2 claim.

## Finite designed controls — NOT observed

Every harness fixture is a fresh exclusive JSON pair containing input and
certificate, actually changed, reread and hash-bound. The calls are explicitly
checker.verify IN-PROCESS, not new production entrypoints. Seven common cases:

1. rows216 instead of217 -> certificate dimension/schema;
2. remove the last witness pair -> complete rational witness dimension;
3. floating numerator -> canonical rational strings only;
4. numerator "00" -> canonical reduced rational;
5. add1 to the constant modulus coefficient, still canonical -> literal full modulus not a factor;
6. change first row id -> literal row order/degree envelope;
7. omit h0 from guard factors -> guard and both factors retained.

One branch-specific eighth case: separator multiplied by2 preserves every
zero column and fails dual target normalization; for UNIT, add1 to the
constant multiplier of the first nonzero input row and fail the full
217-coordinate identity. If every input row is zero, that UNIT mutation
is explicitly NOT-APPLICABLE rather than fabricated. Seven common fixture
rejections plus one conditional case do not prove coverage of both branches.
Early metadata-binding failures remain distinct from these semantic controls.

Separate generic verifier tests MUST be explicitly registered before use;
they are not implemented as an automatic second solve or hidden batch step:

- UNIT: f1=1, others0, q=r=h0=1; witness h1=1. Flip that multiplier to2.
- SEPARATOR: all fi=0,q=r=h0=1; lambda extracts the constant T^0v^0
  coefficient. Flip lambda to2lambda and require target-normalization failure.
- HIGH WINDOW/PRECISION: f9=K*T^5, others0,q=T^5,r=T,h0=T^4,
  K=9007199254740993. h9=T^20/K is an exact positive identity. Change
  its T^25 multiplier from0 to1 and require a T^30 failure; change the
  successful coefficient to the rounded-integer-string version and reject
  the exact identity. A float is a parser failure, a rounded canonical
  integer string is an arithmetic-identity failure, not the same evidence.
- ZERO GUARD: all fi=0,q=r=0,h0=1; zero UNIT witness. This is not
  automatically a nonzero quotient and must not be mistaken for one.

These are generic tests over the same literal B, not actual source fixtures
or source points; no ROOT source acceptance may be fabricated for them.
One separately authorized gated harness can invoke the pure verifier with
these toy wires. That harness/registration is not supplied in this packet.

## Remaining quantities and cheapest next tests

No syntax/import/runtime has been tested. One static code/semantic delta
review is needed first. Installed python-flint compatibility, pinned native
closure and positive/negative generic tests are the next finite documentary
and registered validation obligations. Only then can ROOT select actual
caps and a single real candidate/check run. All actual matrix/certificate
bit lengths, nonzero counts, bytes, CPU, wall and RSS remain unmeasured.
No claim of runtime readiness, speedup, ideal outcome or launch authority.
