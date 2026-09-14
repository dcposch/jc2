# Frozen static producer/test interface — 2026-09-10

Accepted mathematics:17zg (producer6135ca13, FIRST Fable gate718df083),
under17m. No code or execution is accepted by this contract. One new producer
and an independently authored finite generic harness are prepared in parallel.
Neither author may read the other's live artifacts; this is their shared API.

## Candidate module

solver.py preserves the existing candidate(data, flint) and main CLI/wire
contract. Its new internal generic_candidate(p, fs, q, flint) returns the same
generic certificate dict, including full217/1638 sizes/orders and rational
string witness pairs, without runtime/source binding fields. p is a dense
list of8 Fraction coefficients, monic and squarefree of degree7. fs is a
list of9 dense T-polynomials, each of length1..6, and q is another such
polynomial. Each T coefficient is a dense list of exactly7 Fractions in the
v basis. Zero polynomials are represented by at least one zero coefficient.
No floating conversion. This internal API is callable only inside a separately
authorized AWS entrypoint, not by a local import or test. Validate the bounds,
monicity and squarefreeness; refuse a nonreduced coefficient algebra.

The actual candidate(data,flint) parses the ORIGINAL literal modulus, row ids,
envelopes and guard using the old schema before passing exact values to this
kernel. Generic synthetic moduli are changed-object controls only, never
permitted as actual source inputs. Use exactly17zg's maximal-degree pivot,
both CRT children, possibly nonreduced remainder algebra and raw read-back.
There is at most ONE nonempty direct-sum rational RREF in a candidate call;
exceptional immediate branches may need none. Keep its complete row-operation
tracking for the separator; do not produce the old full search matrix.

checker.py, evidence.py, algebra.py and execution_gate.py are retained
BYTE-IDENTICAL to17z, with the same sibling filenames in the new package.
The new solver is the only changed production module. No new required
production helper module, caller, authority schema, supervisor or engine API.
Use accepted rational matrix construction/indexing/fmpq/rref API only.
The existing Fraction/Q-polynomial helpers may be reused; no new native
polynomial API without a separately named need. Main must still authorize
before importing arithmetic/FLINT or allocating mathematical objects.

A small construction_trace in the candidate may record exact split moduli,
CRT maps, raw pivot units, leaf basis dimensions and local solution/functional
needed to audit read-back. It is not a proof premise for the unchanged checker.
Do not serialize a second full matrix. Optional bounded phase labels in the
future child's stdout are diagnostic only, not a new supervisor or speed claim.

## Independent generic harness

generic_controls.py is a separately authorized metadata-gated entrypoint,
AUTHORITY OUTPUT. Its future flat runtime package contains the new solver,
unchanged checker/evidence/algebra/execution_gate and this harness, all
explicitly pinned. Its authority operation is build. Before any arithmetic
import, authorize its own exact argv/registered host/capped parent. Pin the
candidate and all used modules, and bind the already installed FLINT version,
module/interpreter and declared native files before importing FLINT. No actual
source data, incoming source receipt or ROOT source acceptance is used, minted
or simulated by generic controls. All future worker/cap/clock fields remain
disabled/null; the present task runs NOTHING.

The harness calls generic_candidate on finite hand-specified rank7 inputs and
checks the returned full certificate using its OWN dense Fraction arithmetic
with the fixture modulus, never the producer's helpers or precomputed matrix.
This fixture verifier is NOT an alternative actual-source checker. The actual
checker remains byte-identical and is used later on the genuine source.

Use one synthetic squarefree p=product_(j=0..6)(v-j), computed only in a future
authorized run. Let e0=product_(j=1..6)(v-j)/720, the v=0 idempotent.
At most8 positive finite cases: allzero/q0 UNIT; allzero/q1 SEPARATOR;
constant f1=1,q=T5 UNIT (degree25 multiplier); raw f1=2T,q=T UNIT;
f1=T2,f2=1+T,q1 UNIT with nonreduced remainder; lost-component
f1=e0+(1-e0)T,q=1-e0 SEPARATOR; varying-pivot f1=e0*T,
f2=(1-e0)*T2,q=T UNIT; f1=T,f2=T-1,q1 UNIT (all generators matter).
Every unspecified fi is zero. Pure rational arithmetic, canonical wires.

At most4 changed-certificate/input negatives: scale the positive separator
by2; add1 to the raw2T UNIT constant multiplier; truncate one full witness;
and replace coefficient p by v7 to require a precondition refusal. Require
actual object change and exact failure reason, retain frozen inputs/outcomes;
do not label an unexecuted test PASS. No random/farm/actual-source point work.
All217 coordinates or all1638 column pairings remain in each full identity
test. Cases exercise nonconstant coefficient algebra and actual splitting;
constant-v tests alone would not cover this new algorithm.

If the two static packages disagree with this API, report a concrete GAP;
neither author may silently edit the other's code. Root collects both terminal
packets and sends ONE joint FIRST static review. Later finite runtime testing
and actual-source execution require separate root registrations/authority.
