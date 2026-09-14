# FIRST: mixed-scalar elimination source

Astra different-model static review of Sol's frozen source. First action
2026-09-12 18:57:00 UTC; own targets absent. Original publication reserve
19:10 UTC / hard19:13 UTC, never reset. No source, CAS, import, syntax,
fixture, native/worker, network or scientific execution occurred.

Six specified inputs were all pinned before fresh WHOLE reads. The corrected
COORDINATION pin is 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597.
Only the unchanged administrative finalizer is an additional instrument.

Verdicts below distinguish the mathematical algorithm from source-level
certificate safety, runtime compatibility, the stipulated source attachment,
and absent execution authorization. No certificate or all-r result exists.

## Verdict summary

| Issue | Verdict at exact scope |
|---|---|
| Power recurrence, convolution and coefficient indices | CONFIRMED, stipulated scalar target |
| Generic std/lift certificate algorithm and orientation check | CONFIRMED mathematically, conditional on installed Singular APIs |
| Denominator clearing and integer-r exception criterion | CONFIRMED mathematically; conservative false negatives allowed |
| Malformed-certificate isolation / checker-only PASS authority | REFUTED — blocking source defect |
| Installed language, conversions, serialization and error/exit behavior | GAP, not observed or primary-documented by these inputs |
| Wrapper guard-before-CAS ordering | CONFIRMED narrowly; complete runtime registration/caps absent by design |
| Full forcing/source attachment or actual all-r conclusion | GAP / NOT ESTABLISHED |

Recommendation: do not accept this checker as the future independent
certificate verifier unchanged. Repair only the executable-certificate
boundary and qualify the selected Singular language/error behavior before
registration. No implementation or execution is selected by this review.

## A. Exact recurrence and target — CONFIRMED

Put phi=1+u+Xu²+Yu³ and a_k(s)=[u^k]phi^s, a_0=1. Comparing u^(k-1)
in phi A'=s phi' A gives

    k a_k = sum_(j=1..min(3,k)) ((s+1)j-k) phi_j a_(k-j),
    (phi_1,phi_2,phi_3)=(1,X,Y).

Thus eliminate.sing20/23 and checker14/16 have the correct coefficient and
one-based offset: a[k+1] stores a_k; D[6],D[7],D[8] are d5,d6,d7.
The initial list element and every referenced earlier element exist in the
intended list semantics; the guard j<=k prevents negative indices.

For phi^-1=sum q_k u^k, q_0=1 and q_k=-sum phi_j q_(k-j), exactly producer
33–46/checker24–32. Therefore [u^k](phi'/phi)=q_k+2Xq_(k-1)+3Yq_(k-2).
Their k=14-i-j and indices q[k+1],q[k],q[k-1], with lower-bound guards,
give exactly [u^14](phi'/phi) T_(2nu-1) T_(4-nu), both T truncated at7.
In the old FIRST notation this is ell_(15-i-j), not ell_(14-i-j).
Computing q through14 suffices for every i,j in0..7. No coefficient is
omitted and there is no off-by-one or extra inverse power in this formula.

The stipulated localized unit problem is precisely
I=(d6,d7,B,zYd5-1) in Q(nu)[X,Y,z]. All components remain; neither a chosen
factor nor a generic point of V(d6,d7) replaces this ideal. This confirms
transcription of the old scalar target only, not its missing forcing bridge.

## B. Generic ideal and denominator proof — CONFIRMED conditionally

Over the stated rational-function coefficient field and global dp order,
an exact standard basis has reduce(1,std(I))=0 iff I is the unit ideal.
The intended lift(I,ONE) convention is four rows, one column, with
sum_i I_i C_(i,1)=1. Producer78–82 explicitly verifies THAT orientation and
identity, rather than accepting rank, a unit-basis header or a lift flag.
Actual API availability/dimensions and successful evaluation are not observed.

Each C_(i,1) has finitely many monomials in X,Y,z and coefficients in Q(nu).
Taking the product of every nonzero coefficient denominator yields a nonzero
N in Q[nu] and A_i=N C_(i,1) in Q[nu,X,Y,z]. f-lead(f) removes one whole
leading term; it does not merely remove its coefficient. The product can
retain redundant factors but cannot miss a denominator of the final witness.
No denominator of a discarded Groebner intermediate must be retained: the
final cleared polynomial identity itself is the specialization authority.
The original d5,d6,d7,B have only nonzero rational constant denominators, so
no additional parameter-denominator exceptional set is omitted.

Producer99–102 and checker61–62 test the full identity. Checker48 rules out
the vacuous zero multiplier, and53/58 require cleared coefficients. If the
installed denominator primitive also returns nonunit rational constants,
requiring literal1 can reject a valid Q-polynomial certificate; that is a
conservative refusal, not an unjustified specialization.

For N!=0 in Q[nu], exact irreducible factorization over Q is sufficient.
Every actual nu=(5r+2)/(3r+1) is rational, so nonlinear irreducible factors
cannot vanish there. A linear root q has inverse r=(2-q)/(3q-5), and the
integer condition denominator(r)=1 together with r>=2 is exact. q=5/3
has no finite inverse r and must be skipped, as the source does. Constant
factors are units. Neither signs on a real interval nor absence of irrational
roots is required. Extra actual-r factors in this particular N cause a
conservative GAP, not a counterexample or proof that no other witness exists.

The old FIRST's cube control forces N(5/3)=0 for any correctly cleared
identity: at its X=1/3,Y=1/27 point d6=d7=B=0 and Yd5 is nonzero, so choose
z=(Yd5)^-1. This is a consistency requirement on a FUTURE N, not a computed
factorization. The checker correctly does not interpret that root as an
actual integer-r exception.

## C. Blocking executable-certificate boundary — REFUTED

check-certificate.sing3 sources certificate.sing as executable Singular
input BEFORE establishing any checker-owned ring, N!=0, denominator check,
identity check or factor census. The certificate controls the ambient ring
and can contain arbitrary statements, not merely the five coefficient values.
The wrapper checks only that the file exists (line20); it neither constrains
its grammar nor authenticates/freezes the future candidate bytes.

Exact source-level negative trace, NOT executed and no fixture written:
replace the whole candidate by the checker's own final PASS-print statement
(line88) followed by its own exit(0) statement (line89). Inclusion at line3
then performs those statements before reaching line5 or any check. If
exit(0) terminates the Singular process from an included file, this produces
the PASS text and normal exit without an identity or even a ring. Its exact
exit code and nested-file behavior remain UNOBSERVED; this is not a replay.
If that exit spelling is rejected or merely returns from the include, this
particular early-exit trace is correspondingly qualified, but the unconditional
input-as-code/ring-ownership defect remains. Additional expected files could likewise be
written by included code, so a presence-only receipt/census rule is no cure.

This is not an assertion that the frozen honest producer emits malicious
text. It refutes the checker's advertised independent malformed-input
boundary and makes its PASS channel insufficient as certificate evidence.
A post-generation hash proves custody, not that sourced bytes were data.
Even a nonmalicious altered ring is not rejected independently by this checker.

Smallest sound repair recommendation: make the ring checker-owned and admit
only a bounded literal coefficient payload for N,A1..A4, with exact names,
types, grammar and EOF. No input statements, ring changes, procedure calls or
early exits may execute. If preserving the present serialization temporarily,
a whole-file rigid grammar gate must precede sourcing and permit ONLY the
exact fixed ring plus five literal algebraic declarations; a substring or
character allowlist is not that grammar. No generic controller is needed.
The actual new parser/source change must receive focused review; none is
implemented or licensed here.

## D. Semantic controls and runtime assumptions

Two further mathematical controls, also unexecuted:

- Given any genuine cleared witness, change A4 to A4+1 and keep N/other
  coefficients unchanged. The residual changes by zYd5-1, nonzero because its
  constant-in-z term is -1. Denominator checks still pass; checker61 must
  select CHECK_FAIL: polynomial identity / intended exit11. This exercises
  the normal mathematical branch, not stale-hash or parse rejection.
- Multiply N and all four A_i by 7nu-12. The cleared identity remains true,
  but the new linear factor q=12/7 gives r=(2/7)/(1/7)=2. Checker82 must mark
  bad and87 select intended exit12. This distinguishes an actual discrete
  exception from the permitted q=5/3 root and from an irrational root.

GAP: these six inputs do not establish installed Singular semantics for
exit(integer), list indexing/extension, lift dimensions, denominator on a
transcendental coefficient field, factorize's factor/multiplicity lists,
constant-polynomial to number conversion at checker78, or number/poly string
round-tripping through certificate.sing and execute at checker70. The
mathematical derivations above are independent of those implementation
observations; no unsupported syntax is asserted definitely broken.

In particular, intended exit codes cannot yet be treated as observed process
codes. Top-level parse/evaluation errors are not caught by a fail-closed
completion protocol here. An installed build which resumes after an error
could reach later text; success requires evidence that all checks actually
completed, with no earlier language/runtime diagnostics. Mere normal exit or
one PASS substring is not enough. The executable-certificate defect remains
blocking even after normal error/exit behavior is qualified.

The checker separately reconstructs polynomials and does not consume the
producer's I/G/lift matrix. However its power and convolution recurrences
duplicate the producer, so their agreement is not independent evidence of
formula transcription. Section A supplies the separate manual coefficient
derivation; no independent native arithmetic backend is claimed.

## E. Runner and source-completeness boundaries

CONFIRMED narrowly: wrapper4–22 checks argv/job, Linux, EC2 vendor, selected
UID, output-directory shape and BOTH source hashes before Singular exec24.
Its unresolved UID placeholder cannot match a numeric installed UID; this
template is not an enabled registration. Direct .sing entry does not have
those guards. A comment saying DISABLED supplies no independent guard.

Future obligations, NOT implemented by this small wrapper: genuine exact ROOT
authority and physical identity; binary/library/startup configuration and
tool/native pins; controlled environment and source search paths; canonical
exclusive output ancestry, candidate regularity/hash/freeze and byte grammar;
fixed wall/CPU/RSS/output quotas for the joint generator/checker job; exact
owned process/cgroup identity, descendant cleanup, durable terminal custody,
and strict all-output/error acceptance. -f follows a candidate symlink and
the final-directory !-L test alone does not qualify its ancestry. The shell
retains its inherited environment. No fresh-output/exclusive-write predicate
is supplied around RESULT/certificate/census publication. These are real
future integration requirements, not purported observations or authority.

The contract's 3600wall/3300CPU/32GiB/256MiB proposal is UNMEASURED and
unenforced here. This review neither chooses it nor schedules a run. There
is no fallback, parameter farm, source outcome or runtime PASS to collect.

The old FIRST explicitly leaves the entire-forcing-to-(4) attachment GAP and
imports the two undisplayed degree assumptions for its later cancellation.
It confirms the normalized scalar presentation and finite B formula, not
the full original forcing. Even a repaired checker and successful all-r
unit certificate would establish only that stipulated localized scalar
statement until a separately accepted source attachment is supplied. No new
ROOT forcing note, potential, REG, source-zero, all-F10 or JC2 consequence is
an input or conclusion of this review.

## Closeout and exact remaining quantity

Own complete readback and six unchanged post-pins are required before seal.
COLLISIONS: own targets absent at first action; this named FIRST is distinct
from the old mathematical scalar gate. No corpus, live peer or linked input
was inspected. All review work was manual text/algebra and administrative
hash/publication; no source was modified, copied into an executable fixture,
parsed by an interpreter, imported, syntax-checked or run.

OPEN[CERTIFICATE_DATA_BOUNDARY]: QUANTITY: prevent an input certificate from
executing any statement or selecting the checker success path, while retaining
the exact identity and discrete exception checks. CHEAPEST TEST: narrowly
repair the input grammar/ring ownership, then one focused different-model
actual-code gate; prospective AWS-only malformed/identity/exception controls
may be bounded to60seconds each as UNMEASURED planning, not authorization or
a forecast. No automatic successor, broad foundation review or worker action
is requested. FINAL VERDICT: blocking source defect; algorithmic mathematics
passes at its stipulated scope, but independent-verifier acceptance is denied.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13435`.
- Body SHA-256:
  `9836e4982c086fff0f6570a22a9357215ffe7e69435bf867dc4dbf3f3eb4ac15`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
