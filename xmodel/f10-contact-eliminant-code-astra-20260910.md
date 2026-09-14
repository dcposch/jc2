# Exact contact eliminant producer and independent coefficient checker

2026-09-10. Astra implementation producer, UNREVIEWED. First action
04:09:56 UTC; original fixed stop04:24:00 UTC, reserve04:22:00 UTC.
SOURCE TEXT ONLY. No computation, syntax/AST/import/compile check or test.

## 1. Delivered implementation and exact remaining status

Owned source files are complete bounded candidates:

- produce.sing: one characteristic-zero GLOBAL dp Singular producer for
  the literal accepted17zr four-generator ideal, with membership lift and
  sparse rational-term certificate serialization.
- check_certificate.py: separate exact sparse rational polynomial checker;
  it reconstructs the original ideal independently from BOTH quartics,
  parses nonexecutable term data and verifies the coefficient identity.
- CONTROLS.md: prospective arithmetic, saturation and malformed-input
  controls. NONE were executed and no fixture was emitted.

The files are in box/f10-contact-eliminant-code-astra-20260910/. They were
authored only with apply_patch. No F, cofactor, GB, coefficient artifact,
root list, prescribed exclusion or source/JC2 conclusion exists from this
lane. Source is not runtime-validated, and this report grants no execution.

Exactly three charged science inputs: assigned ROOT-CARD, accepted17zr
interface c1ec52ca and FIRST Fable gate76d25dfe. Card and gate were read
WHOLE anew after pins; the interface's previous exact WHOLE was reused
only after its current matching pin, as permitted. No singleclient packet,
old dimension report, other lane, live solver or linked provenance read.
The sole additional API source was the specifically permitted pinned
official reference.doc; exact read scope and full-byte hash are in PINS.

## 2. Producer algorithm and proof of intended certificate

The source fixes ring contact=Q[z,V,W,X] with global dp, never a quotient
or local ring. option(none) clears inherited optional strategies, then
option(redSB) requests reduced standard bases. The original coefficients,
c,d,e,f,g and A,B,C are literal accepted17zr definitions; I retains all
four rows, in the exact order I1,I2,I3,I4, including I4=z*c*A-1.

The concrete sequence is

    G0=liftstd(I,T);       G=std(G0) with redSB;
    F=1 if reduce(1,G)=0;
    otherwise require dim(G)=0, then F=finduni(G)[4];
    L=lift(G0,ideal(F));   H=T*L.

G0 and T are deliberately kept together. The reduced G is used only to
choose F; the membership lift goes to the UNCHANGED G0, not to a changed
basis while reusing T. The primary API identities give

    matrix(G0)=matrix(I)*T,
    matrix(ideal(F))=matrix(G0)*L,
    F=sum(i=1..4) H[i,1]*I[i].

The second equality has no unrecorded unit matrix because this is a
global polynomial ring. No local-ring lift assumption is transferred.
The source requires H to have four rows and one column, checks F!=0 and
F=subst(F,z,0,V,0,W,0), and recomputes the LAST displayed identity before
serialization. Substitution at zero is an exact univariate test here:
every term involving z,V,W disappears and all other terms are unchanged.
The F=1 branch handles the zero quotient without calling finduni on it.
The nonzero branch calls finduni only on a reduced zero-dimensional GB.

The mathematical correctness of a returned packet does NOT depend on
trusting a GB header or finduni's minimality: the independent checker
validates the final literal identity itself. The accepted17zr finiteness
theorem supports this computation target but supplies no runtime bound.
No actual GB or F has been obtained.

## 3. Primary API verification and serialization contract

The pinned [official Singular reference source](https://raw.githubusercontent.com/Singular/Singular/186962946a86748b0b15bd9e34f02a85e51692c2/doc/reference.doc)
was read by named sections, not WHOLE. Verified interfaces include
liftstd, global lift, redSB/std/finduni, dim, char, subst, leading-term
access, rational numerator/denominator, and ASCII write/open/close.
The reference explicitly specifies newline-separated ASCII conversion,
the :w overwrite mode, and quit without supplying an exit-status promise.
No secondary site or additional library semantics were assumed.

The producer's ONLY output file is contact-eliminant.cert in a future
fresh ROOT-registered isolated working directory. It opens an ASCII :w
link, then writes a whitespace-token format:

    JC2_CONTACT_CERT_V1
    interface <accepted interface SHA256>
    gate <accepted FIRST gate SHA256>
    ring Q z V W X dp
    generators I1 I2 I3 I4
    poly F
    term <numerator> <denominator> <ez> <eV> <eW> <eX>
    ...
    endpoly
    poly H1 ... endpoly
    poly H2 ... endpoly
    poly H3 ... endpoly
    poly H4 ... endpoly
    endcert

ASCII write places separate arguments on separate lines; the grammar
intentionally treats all whitespace equally. The serializer repeatedly
takes leadcoef/leadexp and subtracts lead(poly), emitting exact integer
numerator and denominator fields, never polynomial-expression strings,
floats, JS numbers or integer-truncated coefficients. Zero cofactors have
empty blocks. Block order, variable order, Q characteristic and both
accepted source hashes are mandatory. The checker does not execute data.

The producer prints only compact stage/failure/candidate-written markers,
never an explicit GB dump. Explicit failures print PRODUCER_FAIL and quit.
The candidate-written marker and Singular's exit status are NOT acceptance.
An engine/serialization failure may leave a partial file, which must fail
the independent complete grammar/identity check. Fresh-directory custody
is required to rule out reuse of an old file after an early engine failure;
this tiny producer is not a supervisor or transaction wrapper.

## 4. Independent checker: exactness, binding and refusal behavior

The Python source uses stdlib Fraction and arbitrary-size integers. Its
polynomial representation is a dictionary from four nonnegative exponent
integers in order(z,V,W,X) to nonzero reduced rational coefficients.
Addition merges equal exponents; multiplication convolves exponent tuples
and multiplies rational coefficients; construction removes exact zeros.
Induction on these operations gives their ordinary Q[z,V,W,X] meanings.

The checker imports no producer and trusts no emitted I. Its own literal
a3..a0 and b3..b0 reconstruct c=a3-b3,d=a2-b2,e=a1-b1,f=a0-b0, then the
accepted A,B,C and all four generators. This is a distinct reconstruction
from the producer's explicit d,e,f formulas and keeps every I4 term.
The b_i coefficients were hand-derived from b=a-(cY^3+dY^2+eY+f)
in the charged interface, not obtained from an additional report.
It is source-level independence of reconstruction and arithmetic engine,
not a claim that either implementation has already passed a gate.

The parser checks the exact source/ring/generator header and exactly five
named blocks, canonical decimal integer tokens, positive denominator,
nonzero numerator, reduced rational coefficients, nonnegative exponents,
no duplicate monomials, terminal endcert and no trailing token. It refuses
zero F or an F term with any of its first three exponents nonzero. It then
computes F-sum(Hi*Ii) and accepts only the empty zero dictionary.
This checks the characteristic-zero identity with nilpotents retained;
neither radical membership nor sampled evaluations are substituted.

The CLI accepts one certificate path, reads at most64MiB+1 and refuses
larger input. This byte ceiling is only an operational refusal bound,
not an eliminant size/degree assertion. Decimal digit conversion limits
are disabled where the Python API provides that facility; integers remain
exact. External memory/time limits remain mandatory: sparse multiplication
can still be expensive. ROOT owns those limits, not this source lane.

Any caught exception prints CHECK_FAIL and returns status2; CHECK_OK and
status0 occur only after the coefficient identity, with SHA256 of the
exact accepted file bytes. Uncaught termination is not acceptance. The
hash binds the verdict to data, but source/runtime pins and provenance of
the actual producer run remain external custody obligations. No root
filtering code was added to dilute this primary certificate deliverable.

## 5. Controls, static guarantees and unexecuted gates

The arithmetic mutation controls are substantive. Starting from a valid
packet, changing only F to F+1 makes residual1, while changing only H4 to
H4+1 makes residual-I4. The latter is a nonzero polynomial because
I4 at z=0 is -1. Both MUST be rejected by the displayed exact check, not
just by a changed provenance hash. These are static deductions, not runs.

The omitted-I4 control is separate: at V=W=0, A=B=C=0, so the three other
rows leave a spurious X-line. No nonzero univariate F belongs to that
changed ideal. A future mathematical control must trigger dimension
refusal; merely omitting the serialized H4 block tests the parser instead.
CONTROLS.md distinguishes these and lists prospective zero-F, zero-H,
nonunivariate, malformed, truncated and unit-ideal branch checks.

Executed evidence: NONE. This includes no syntax check, AST, import,
compilation, dummy, test, mathematical subprocess, CAS or native run of
ANY size. Only source text, the permitted official API source, exact hashes,
owned documentary writes and the existing artifact transaction were used.
Thus syntax/engine compatibility, ASCII round trip, complete control
execution, pinned-engine behavior, independent FIRST review and ROOT's
runtime/cap/transport registration are genuinely pending. An explicit
eliminant and prescribed root discrimination also remain GAP. Accepted17zr
still requires source/affine read-back before any broader implication.

## OPEN(S) RAISED

- ASSIGNED GAP ONLY; no new canonical ID: gate the unexecuted source and
  any independently authorized runtime/controls, then obtain an actual
  certificate. No engine execution, further lane, promotion or follow-on
  authority is supplied by this report.

## COLLISIONS

status: EMPTY FOR THIS SOURCE IMPLEMENTATION

- Exact owned report and box were ABSENT at first action04:09:56 UTC.
  Own-only report extraction; no corpus/history or other-lane inspection.
- No source solver, CAPRUN, wrapper, scheduler, runtime registration or
  protected/shared file was inspected, altered or invoked.

Own WHOLE report, both source files, CONTROLS and PINS were reread as TEXT
at04:18:32 UTC, with own-report OPEN/collision extraction. This completion
clarifies the b_i source derivation only. No authored code was executed or
machine-checked. Final custody and independent ROOT/FIRST intake remain
required; all execution and promotion decisions remain outside this lane.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10716`.
- Body SHA-256:
  `6ae23405c20c9abc4c8720fafe261ad07891d4e778d33f00a5ba58ce9ab1d858`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
