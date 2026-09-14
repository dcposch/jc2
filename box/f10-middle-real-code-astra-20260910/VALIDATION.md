# Static preparation; no observations

No source was compiled, imported, parsed by AST, executed, or tested. No coefficient artifact or fixture exists. All syntax, API behavior, costs and branch outcomes remain unmeasured. This is not runtime-ready authority. The first next action is a different-model static review of these three sources and the exact certificate semantics.

## Representation and certificate

The producer uses sparse `Fraction` polynomials in `(tau,alpha,V)`. The checker uses an independently written four-variable dictionary algebra in `(tau,alpha,V,W)`, reconstructs the accepted literal E and Q equations, divides the Q divided difference by `alpha-nu` through monic synthetic division, and eliminates W independently. It never imports producer.py, its arithmetic, determinant routine, or its source formulas.

The producer divides S by T with the fixed constant leading coefficient 10080. With `d=10080^3` and `C=d*Frem`, the integer matrix columns are `C,V*C,...,V^4*C,T,...,V^3*T`, padded through V^8. For `z=adj(B)e0`, put `Atilde=sum(z_i V^i,i=0..4)` and `Btilde=sum(z_(5+i)V^i,i=0..3)`. Then `R=det(B)=C*Atilde+T*Btilde`, `U=d*Atilde`, `Wcof=Btilde-U*Qdiv`. Thus `R=U*S+Wcof*T`; R is 10080^15 times the unintegerized determinant. No polynomial division is used in computing cofactors. Subset DP uses rows 1 through k and k ordered columns; expansion in its last row has sign `(-1)^(k-1+position)`. At size eight, omitted-column j gains `(-1)^j`. This is the independently checked parent suggestion, not a runtime observation.

Wire schema `f10-middle-real-certificate/v1` contains all five Qdiv/Frem/R/U/Wcof polynomials, exact j/epsilon and the entire dense Bernstein rectangle. Polynomial terms are sorted `[exponent-string-vector,[numerator-string,denominator-string]]`; nonzero, reduced rational coefficients only. Integers are denominators one. JSON numeric values are forbidden in this wire. Duplicate keys/terms, wrong versions/fields/bounds, noncanonical rationals, and missing dense positions are rejected. R/U/Wcof must be integral. Nothing uses eval or pickle.

The checker verifies the whole quotient identity and the whole cofactor identity, including every positive-V coefficient. It does not certify that an accepted identity necessarily used the particular determinant algorithm: an alternative exact bounded nonzero identity proving the same result is sufficient. It then uses nested Horner rectangle substitution, descending synthetic division by t-1 (with quotient sign reversed), and direct Bernstein basis expansion. These differ from the producer's cached substitution, ascending division by 1-t and monomial-to-Bernstein conversion. Only the maximal `(1-t)^j`, j>=1, is removed. The t=0, s=0 and s=1 boundaries remain. All 22 coefficients on the collapsed edge must equal the exact positive absolute endpoint, not just its two corners.

The checker is the only prospective source of `CERTIFIED_NONRESONANCE`. Negative/zero signs give INCONCLUSIVE; malformed identities exit nonzero with INCONCLUSIVE. A producer CANDIDATE flag is not evidence and is not trusted. No program emits REFUTED, JC2, a source point or a scheme consequence.

## Explicit bounds and authority

Internal sparse objects have at most 20,000 terms, exponents at most 100, coefficients at most 12,000 numerator/denominator bits. Decimal strings have at most 4,096 characters and process-local int conversion limits are enabled before reads. Qdiv total/V bounds are 3/2; Frem 8/4; R total/alpha/V bounds 40/21/0; U 32/4 and Wcof 35/6. The rectangle has bidegree (40,21), its reduction (40-j,21). These are fixed conservative bounds, not measured maxima. Any bound hit is NONDECISION, not permission to enlarge it.

The certificate is at most 16 MiB minus 4 KiB; the receipt is at most 4 KiB and certificate+receipt at most 16 MiB. Root's future wrapper must separately enforce the aggregate batch/file/log budget; the entry gate is not a supervisor or a strict real-time limiter. Nested malformed JSON can fail nonzero; no claim of constant-memory hostile-input parsing is made.

`authority.py` is metadata only. Both CLIs require `--job f10-middle-real-certificate-20260910 --registration ABSOLUTE_PATH`. Producer additionally requires `--output`; checker `--input --receipt`. Before importing Fraction/math or allocating polynomial objects, authorization demands Linux, literal EC2 DMI, exact registered instance/hostname/cwd/script argv/interpreter, root-owned mode-0444 registration, source and code hashes, absent outputs, exclusive authority ownership and an unexpired fixed deadline. Environment variables alone cannot authorize. Root must supply and preflight full outer Python flags/argv (sys.argv alone excludes interpreter flags), all native/instrument/source pins, immutable input, UID/GID/cgroup/CAPRUN supervision and five-refusal/valid/descendant cleanup regression. The disabled template is not launchable. No root registration, native compatibility or caps enforcement was supplied or tested here.

The proposed single formation+checker cap is 360 wall / 330 CPU seconds, 2 GiB sampled RSS and 16 MiB aggregate wire, unmeasured. Root alone can issue a separately reviewed initial worker registration. No automatic retry, budget escalation, subdivision, second engine or parameter sweep is implemented. Python stdlib Fraction, math.comb, int conversion guard and ordinary Python execution are assumed API interfaces; installed-version compatibility is pending, with no dependency discovery performed.

## Finite prospective changed-object controls

Use a genuinely produced candidate if one exists; no positive certificate is promised. Every fixture is changed canonically, exclusively written and re-read, hashed, and individually authorized. Do not use stale input pins to manufacture a semantic rejection. No fixture authoring or tests occurred in this task.

1. U -> U+1: expect `positive V cancellation` since S has its nonzero seventh-degree term. This also checks a missing-positive-V-cancellation attack; do not count it twice.
2. R -> R+1: expect `full cofactor identity`.
3. Declared j -> j+1 (or j-1 at 40): expect `wrong maximal excluded-edge factor`.
4. Illicit retained-edge removal, represented by deleting a nonzero t=0 Bernstein row entry: expect complete-row schema or full expansion rejection. This is not a witnessed successful sign-branch test.
5. One interior Bernstein coefficient +1: expect `full Bernstein expansion`.
6. One Bernstein entry replaced by a negative rational, changed from its original value: generally full expansion rejects first. To exercise the negative-sign return itself requires an actual identity-consistent negative candidate; none is assumed.
7. A zero-endpoint counterfeit (R changed to have zero constant, cofactors unchanged) rejects at full identity. The genuine zero-endpoint path requires a consistent candidate and remains unobserved.
8. Duplicate top-level JSON key: `duplicate JSON key`.
9. Duplicate a polynomial term: `duplicate or unsorted polynomial term`.
10. File exceeding certificate byte ceiling: `aggregate wire size limit` (only after valid authority).
11. Numerator string longer than 4096: `canonical decimal string required`; a JSON numeric coefficient separately fails `JSON integer forbidden in wire`. These are parser, not successful large-coefficient semantics.
12. Wrong bounds value or an exponent beyond a literal envelope: `variables or declared bounds` or `polynomial degree envelope` respectively.

This is a finite specification, not an executable test harness. Early binding/schema failures are not late identity/sign coverage. A future authorized batch must preserve terminal units, all source/fixture hashes, telemetry and full receipts before result consumption. No generic controls or registration were emitted.

## Unresolved items

There are two task-local pending quantities, not new canonical OPEN IDs: (1) static implementation correctness (three sources; cheapest test is one different-model whole-code audit); (2) bounded actual formation/check success (zero runs, zero artifacts; cheapest test only after that audit is one separately registered capped producer/checker batch). A failed sign certificate is INCONCLUSIVE for the theorem, not a counterexample. No measured runtime, positivity, term count, resultant coefficient, source exclusion or ideal decision is claimed.
