# Minimum nonzero projected pivot: exact read-back and static delta

Status: NEW UNREVIEWED manual theorem/code delta; STATIC ONLY. No executed
mathematics, syntax/import/AST/compile check, fixture, candidate, certificate,
worker action, runtime registration, review invitation, or source decision.

First action: 2026-09-10T03:08:04.045058959Z. Owned report and box were absent.
Controlling stop: 03:24:00 UTC, earlier than first action plus 18 minutes;
publication reserve begins 03:22. Basis
0d39df3c9fd69c939a8420c54d03228b9077777d is provenance, not a price.

## 1. Conclusion and exact scope

The proposed change is sound at the accepted generic certificate interface.
At every coefficient-algebra node, select the least degree among NONZERO
projected generators, including constants, breaking ties by the original
input index. Use -1 only when all nine projections vanish. Split a nonunit
leading coefficient exactly as before and rescan all nine on BOTH children.

The essential changed estimate is not 2d-1: other generators can now have
degree greater than the pivot. Instead, for 1 <= d <= 5,

    deg(h_i f_i) <= (d-1)+5 = d+4 <= 9 <= 25.

This proves the same degree-25 raw-generator reconstruction and the same
complete 217-coordinate / 1638-column certificate alternatives. The
unchanged code already divides arbitrary-degree dividend polynomials by a
monic pivot and checks the resulting degree bound. No reconstruction,
matrix, RREF, CRT, separator, parser, checker, supervisor or schema change
is needed. The two separate callers change only their literal solver SHA.

This is neither a runtime improvement measurement nor an actual-source
result. The prior observed run stopped at CPU550, wall550.17427131 seconds,
sample RSS1194852352 bytes, without candidate/checker/stage trace. Those
observations do not identify an RREF, coefficient-height, memory, or parsing
bottleneck. No actual projected degrees were read or computed here.

## 2. Charged inputs and trust boundary

Exactly eight objects were current-hashed before WHOLE reads: the ROOT-CARD,
17zg design and its gate, generic linear-decision gate, old solver, separate
old generic and actual callers, and the observed execution report. Paths,
all current SHA256 values and byte counts are in owned input-pins.json.
All were read WHOLE in this task, not by following their provenance.
No other scientific report, source coefficient data, helper, runtime
receipt, plan body, current ledger, live producer, corpus or protected tree
was read. Documentary transaction machinery is not a mathematical input.

Accepted parents supply the following interface only. Let
B=Q[v]/P(v), where P is monic squarefree of degree seven. The nine f_i(T)
and guard q(T) have degree at most five in B[T]; zero polynomials are
allowed. Put b=q^5, so deg b <=25. The original rational matrix M has
217 rows (T^k v^ell, 0<=k<=30, 0<=ell<=6) and 1638 columns
(f_i T^j v^ell, 1<=i<=9, 0<=j<=25, 0<=ell<=6).
Its alternatives are a full raw-generator UNIT identity or a rational
SEPARATOR annihilating every column and taking value one on b. The
accepted saturation theorem relates these alternatives to the full guarded
quotient. This note changes only how the same candidate is constructed.

Two qualifications remain explicit: a separator functional must be defined
on the COMPLETE remainder-module basis, and on a split child defined by
g=gcd(lc,P_a), only the chosen leading coefficient is necessarily zero.
The entire positive-degree generator need not vanish there.

## 3. Selection, splitting and the zero/constant leaves

At a node A_a=Q[v]/P_a, project and trim all nine polynomials. If any is
nonzero, let d be their minimum nonnegative degree and choose the first
original index with that degree. Its leading coefficient c is nonzero in
A_a. A rational polynomial gcd gives g=gcd(c,P_a). If g=1, extended gcd
certifies c inverse in A_a. If not, g is a proper nonconstant divisor:
c is a nonzero reduced representative of degree less than deg P_a, so
g cannot equal P_a. The squarefreeness of P makes g and P_a/g coprime.
Keep both children and reproject/rescan all nine on each. No selected
irreducible component or assumed field is introduced.

Each proper split lowers positive coefficient-algebra ranks, their sum
remains seven, and the original bounds of six splits, seven leaves and
thirteen visits remain valid. A selected positive-degree generator may
lose only its leading term on the g child, or become zero; the new scan
handles both, together with possible different minimum indices/degrees.

On a leaf where all f_i vanish, inspect b. If b=0, all nine zero cofactors
give the UNIT identity. If b!=0, a nonzero rational coordinate of b supplies
a normalized coordinate functional; compose it with the leaf projection
and extend by zero on other leaves to obtain the full SEPARATOR. Since
A_a[T] is reduced, q!=0 implies q^5!=0. Thus zero and nonzero guards are
handled without pretending the guarded affine line is finite dimensional.

On a d=0 leaf, the chosen raw constant c is a unit. Set its cofactor to
c^-1 b and the other eight to zero. Its degree is at most25. Unlike the
old maximum-degree choice, other generators on this leaf MAY be
nonconstant. They are irrelevant to this valid identity; the unchanged
constant branch never uses an all-generators-constant assumption.

## 4. Positive-degree quotient and the UNIT read-back

Fix a positive-degree leaf, 1<=d<=5. Normalize only the chosen raw pivot
f_p=c fhat, with fhat monic of degree d. Do not replace the raw input in
the final certificate. The algebra

    C_a=A_a[T]/(fhat)

is free of rank d over A_a, with the full basis 1,T,...,T^(d-1). It need
not be reduced. With e=deg P_a it has rational basis v^ell T^j for
0<=ell<e, 0<=j<d. The ideal generated by the other eight images is
EXACTLY the rational span of their products with every vector of this
basis: arbitrary multipliers reduce uniquely modulo fhat. This argument
does not bound the degrees of the other generators by d.

Take the direct sum over all positive leaves. Its rank R is at most35;
there are exactly 8R multiplier columns, at most280. Zero columns and
zero ideals are retained. This is the same matrix envelope as before;
no actual rank, coefficient height, independence or elapsed time follows.

A small solution chooses h_i of degree less than d for i!=p with
b-sum h_i f_i divisible by fhat. In the unquotiented A_a[T], put

    N=b-sum_(i!=p) h_i f_i.

Every actual f_i still has degree at most5, whether or not it exceeds d.
Consequently deg N <= max(25,d+4)=25. Monic division is valid over A_a,
including its zero divisors, and yields N/fhat of degree at most25-d.
Define h_p=c^-1(N/fhat). Then sum h_i f_i=b for the RAW generators;
deg h_p<=25-d and all other cofactors have degree <=d-1<=4. The bound
used by the retained solver, len(h_p)<=26-d, is therefore unchanged.

Combine these identities and the zero/constant-leaf identities by CRT
in v only. CRT does not increase T degree, so all nine global cofactors
have degree at most25. Padding gives exactly the old 1638 rational
coordinates, and the identity has degree at most30, checked in ALL217
old rows. No substitution of a short quotient identity for that full
identity is permitted.

Conversely, any old degree-25 certificate projects to each leaf and,
after reduction modulo fhat, gives a small solution using the complete
short multiplier basis. Thus the UNIT construction is both sufficient
and necessary for the old target-specific certificate problem.

## 5. Full SEPARATOR, not a functional on only a column span

If b's image is outside the small column span, exact rational linear
algebra gives mu on the COMPLETE direct sum of C_a satisfying
mu(column)=0 and mu(rho(b))=1. For 0<=k<=30, 0<=ell<=6 set

    lambda_(k,ell)=mu(rho(v^ell T^k)).

For any old column v^ell T^j f_i, the pivot image vanishes on its leaf;
otherwise the multiplier v^ell T^j reduces to a combination of the full
short basis. Hence its image is in the small column span, regardless
of deg f_i relative to d. Therefore lambda annihilates ALL1638 old
columns, and lambda(b)=1. No nilpotent direction in C_a is discarded.

For completeness, every individual short leaf-supported column lifts to
an old column combination using its CRT idempotent in B and T^j with
j<d<=5. Thus the small span is exactly the image of the old column
span. This is not the stronger generally false assertion ker rho is
contained in the old degree-truncated image; UNIT read-back used the
specific bound deg b<=25 separately. The existing identity-augmented
RREF and complete-basis mu extraction can therefore remain verbatim.

## 6. Manual changed-object controls (NOT executed fixtures)

These polynomial identities are hand controls over Q, hence also over
the full rank-seven coefficient algebra by scalar inclusion. Unlisted
generators are zero. They are not runtime PASS records or source points.

1. Change f_1=T^5, f_2=T, q=T. Minimum chooses pivot2 with d=1; maximum
   chose d=5. The short target is zero and the raw identity is
   T^4 f_2=T^5=q^5. Here another generator has degree5>d. The obsolete
   maximum-choice estimate 2d-1=1 is false for that generator; d+4=5
   supplies exactly the required new envelope.
2. Change f_2 to1 and q toT^5, retaining f_1=T^5. A NON-FIRST constant
   pivot has d=0 although another generator has degree5. The direct
   identity uses h_2=T^25, attaining the allowed cofactor bound. Excluding
   constants from the minimum would miss this cheap branch.
3. Raw normalization: f_1=2T, f_2=T^5, q=T. The raw pivot cofactor is
   T^4/2, not T^4. Omitting the certified leading-coefficient inverse
   changes the target to2T^5 and must fail full checking.
4. Nonreduced quotient remains essential under the NEW selection:
   f_1=T^2, f_2=1+T+T^3, q=1. Minimum gives d=2 and C=Q[T]/T^2.
   The identity is
   (1-T+T^2)f_1+(1-T)f_2=1.
   Reducing instead modulo T suggests h_2=1; then 1-f_2=-T-T^3 is not
   divisible by T^2. This actually changed quotient loses the required
   tangent direction and fails the retained full read-back.
5. Split/rescan control: use coefficient algebra Q x Q, pivot candidates
   f_1=(T,T^2), f_2=(T^3,1). Initially the minimum projected degree is2,
   selecting f_1 with leading coefficient(0,1). On its g child the
   polynomial is T, not zero; f_2 is T^3 there, so rescan selects degree1.
   On the other child f_2=1 becomes the degree0 minimum. Discarding g,
   declaring the entire pivot zero there, or retaining the old pivot
   degree fails this explicit changed-coefficient control. Such a product
   is also a direct summand of a split rank-seven synthetic algebra.
6. All generators zero: q=0 yields the zero UNIT identity; changing
   only q to1 makes the target nonzero and yields a coordinate SEPARATOR.
   Taking min over unfiltered zero degrees would confuse a nonzero list
   with this case. The filter f is sound because project() trims exactly.

No selected control is a performance claim. The existing generic harness
and actual checker are not copied, modified, rerun or presumed to have
passed this delta.

## 7. Exact code and separate caller deltas

Owned old snapshots are byte-identical to the three charged code sources.
All authored code was created as text with apply_patch, never executed.

newsolver.py SHA256
961e22e64ec768da6d78a886aa987f7ebaf0325b21b87c68e04db88e91778589
changes one expression plus its two explanatory comment lines:

    degree = min((len(f)-1 for f in local if f), default=-1)

Spacing in the actual file follows the retained source. The unchanged
next(i...) tie-break retains the original first index. The projection,
zero/constant handling, nonunit splits, raw normalization, RREF, full
functional, all217/1638 dimensions, certificate wire/schema and every
actual-source input check remain identical. The exact hunk is solver.diff.

generic_dispatch_batch.py SHA256
e62e5dc4376e83c8dbd8be0146eee13d36fd8ad34fe46dc7b84ab3ff64ac15f3
is the charged GENERIC caller with only its solver SHA literal replaced.
actual_dispatch_batch.py SHA256
ae3df9a9320e1341b94108e1f8b2349e50dd39b8c77d0384309e2d04c8634def
is the distinct charged ACTUAL caller with only that same replacement.
Their diffs are generic-caller.diff and actual-caller.diff. No caller
transplant occurred. In particular the actual caller does not acquire
the generic caller's API, registration schema or newer authority barrier
through this task. Both retain their own original caps, receipts,
operation order, source/generic distinction and STOP semantics.

The generic plan's old literal digest stays unchanged by instruction;
its body was not a charged input and was not read. This caller reads
that pinned plan for case inventories and uses the changed explicit
solver pin for runtime/certificate binding. This is not an audit of
uncharged harness/plan compatibility. All deployment-package and caller
digest updates beyond these two literals belong to a future separately
reviewed registration, not to an authority minted here. Owned names
distinguish the two future dispatch_batch.py alternatives; neither is
installed, enabled or transplanted into a runtime directory.

## 8. Static verification, limits and handoff

Verification performed here is documentary: current eight hashes before
WHOLE reads and at final custody; exact old-snapshot hash equality;
literal diff inspection; one solver selection change and two comments;
one solver-hash substitution in each distinct caller; full own report
read before completion; own-only raised-OPEN/collision check; normal
transaction close/finalize/expected-manifest verification. This is not
a Python parse, compilation, API test, mathematical run or certificate
check. No source or actual projected coefficient was generated/read.

The minimum rule can choose a smaller local remainder envelope, but this
report neither measures actual degrees nor forecasts runtime, coefficient
height, memory use, RREF rank or benefit after possibly different splits.
It does not justify repeating a timed-out run, increasing a cap, skipping
the complete old checker, or treating a candidate as an accepted decision.

New canonical OPEN IDs: zero. Remaining operational question: whether
this exact static delta passes a first independent review and later
separately authorized generic controls. Cheapest next evidence is that
targeted review of this proof and the three literal diffs; no execution
or review is launched here. Actual-source time or degree measurements
would require separate root authority. No dependent work is authorized.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14621`.
- Body SHA-256:
  `49b35e985342969cf81fea64ebb267b7fbe1717bc273cf83b8b84b88a08e2e2d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
