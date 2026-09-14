# F10 r1: one exact-Q decision-and-certificate design

**DESIGN ONLY; DISABLED.** Choose one Singular default `std` computation over Q, one global degree-reverse-lexicographic order, and one independent exact certificate check. No code was written and no mathematical subprocess, network/CLI probe or worker action occurred. The prior producer engineering result remains PROVISIONAL pending its live independent review, which was not read.

First timestamp: 2026-09-09 13:39:31 UTC. The controlling design deadline is 13:49:31 UTC, earlier than 13:51. This is not allocation, restart, registration or solving authority.

## 1. Immutable question and one engine

The only mathematical input is `box/f10-r1-engineering-v2-execution-20260909/remote/exact.json`, SHA `168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576`. Keep Q[u,ell,d0,d1,v0,v1,v2,k1,k2,k3,k4,omega] in exactly that variable order, with global Singular `dp`, not a block/local/parameter-field order. Keep all twenty ordered slots: E1/S0–S8, E0/S0–S9, GUARD/omega*a*b-1. Preserve literal zero slots and beta=gamma=k0=0. No denominator clearing, variable removal, u=0 specialization, generic localization, maximum-h stratum, new guard or second representation is proposed.

Run default `std(I)` once, without a transformation matrix, modular computation, second engine or alternate order. No `slimgb` branch, reduced-basis optimization, elimination block or unregistered algorithm option is proposed. Exact internal reductions are allowed; the input ideal is unchanged.

If the completed output contains a nonzero constant, request a lift of the single target 1 against the original twenty generators, in the same ring/engine/order and within the same initial solver cap. This extraction may internally repeat basis work; that explicit tradeoff avoids transformation-matrix overhead on the properness branch. If no nonzero constant occurs, export the completed candidate basis G directly. In either case the engine's verdict remains only a candidate until independent verification. If extraction does not finish, the result is INCONCLUSIVE, even after an apparent unit basis.

## 2. Exact read-back before trusting either branch

A small future adapter must validate the artifact SHA/schema, fixed twelve variable names and all twenty IDs, emit each original row under a stable separate name, and ask Singular to read back each of those twenty named polynomials before computation. Do not reconstruct the input only from engine ideal indices, which may drop zero entries. The independent parser must compare normalized sparse rational terms row-by-row to the original wires, including the guard and constant row. Domain Q and exact global order must be bound to the generated script and read-back metadata; a characteristic-zero banner alone is insufficient.

Use the existing wire discipline: twelve nonnegative integer exponents and canonical numerator/positive-denominator decimal STRINGS, reduced rational coefficients, unique sorted monomials, and [] for zero. Never evaluate an engine expression as Python. Witness framing binds artifact SHA, exact variable/order declaration, engine binary/version, input script/read-back hashes and branch. Preserve raw engine bytes; unsupported syntax, floats, duplicate terms, missing rows or noncanonical rationals are rejection, not coercion.

The current checker already verifies the full representation, all eight bracket levels, ten inverse-pole slots, all coefficient envelopes/gauges and restoration; do not reimplement its source mathematics in the solver adapter. Its accepted interface and future runtime promotion are dependencies. The new work is faithful conversion and independent ideal-certificate checking.

## 3. Small unit certificate

Export a 20-entry polynomial vector T, including zero entries, and the actual returned 1-by-1 multiplier U. The independent checker must establish that U is exactly a **nonzero rational constant q**, then verify coefficientwise

`sum(f_i*T_i, i=1..20) = q`.

Division by q then proves 1 belongs to the original I. Alternatively normalize the cofactors by q and check the literal identity 1; storing q avoids unnecessary coefficient rewriting. The witness is only q plus the twenty cofactor wires and custody metadata. No Gröbner-basis certificate is needed for this branch.

Crucially, a zero residual in `target*U = I*T` alone is not a unit certificate. The scalar must have no variable terms and must not be zero. Manual control: for I=(u), target=1, T=(1), U=(u), the residual is zero but I is proper. U=0 and T=0 is also vacuous. Both must be rejected before any conclusion. A nonzero polynomial is not a unit merely because it becomes invertible after an unregistered localization.

Root supplied an official-manual advisory during this task: Singular `reference.doc` lines 4372–4422 states this lift identity and promises identity U over polynomial rings; lines 4425–4479 concerns `liftstd`. URL and read limitations are recorded in READ-SCOPE.md. This author did not obtain those bytes, and the installed version remains untested. The design checks U anyway; it does not turn that API promise into trusted arithmetic evidence.

## 4. Small properness certificate—no transformation matrix

The witness can be just a finite candidate G in the same canonical wires. An independent rational checker, not importing the engine or producer's recurrence, must:

1. Validate the global `dp` comparison, monic nonzero basis entries and their exact leading terms; reject any leading monomial 1.
2. Compute every unordered Buchberger S-pair and deterministically divide by G over Q; require zero remainder. No omitted pairs or undocumented criteria.
3. Divide **each of the twenty original input rows** by G and require zero remainder.

Then G is a Gröbner basis, J=(G) is proper because 1 is not in its leading ideal, and I is contained in J. Therefore I is proper. **Reverse containment G in I and equality I=J are unnecessary for this endpoint.** This inclusion certificate does not license claims about I's dimension, exact Gröbner basis or quotient structure. Nor is it permission to search a substituted or enlarged family: the proposed candidate G is the output of `std` on the same original I.

The independent checker may compute the finite reductions itself; no large quotient matrices or stored S-pair traces are required initially. If it exceeds its cap, classification is INCONCLUSIVE. Manual controls: G=(x²,xy+1) has no constant leading monomial but its S-pair reduces to -x, so the first two conditions matter; G=(x²) is proper but cannot certify I=(x), because the input reduction fails. A mod-p basis, an unfinished basis, an engine success header, or an absence of 1 in a list is not a properness proof.

An exact verified proper ideal over Q has a geometric characteristic-zero point by the usual finite-type algebraic-closure consequence; a rational point is not required. Application to a complete source endpoint retains accepted 16q/r and the complete-artifact interface, including its guard. No point or proper ideal has been produced here.

## 5. Proposed smallest registered initial lane

Before activation: root must accept the pending runtime review, choose an absolute cutoff and exact worker, verify installed Singular binary/hash/version and compatible official documentation, freeze new adapter/certificate-checker bytes, and obtain one focused different-model delta review. The currently stopped worker is **not reassigned** by this design.

Recommend one engine child capped at **60 wall / 50 CPU seconds / 2 GiB sampled descendant RSS / 16 MiB per output file**, including input read-back, `std`, conditional lift and witness serialization. Follow only a normally completed candidate with one independent verifier capped at **30 wall / 25 CPU seconds / 2 GiB / 16 MiB**. No cap increase, retry, second order, prime or alternate engine. These are deliberately bounded initial limits, not predicted adequate resources or speed claims. If no certificate is accepted under them, preserve evidence and stop INCONCLUSIVE for root direction.

Reuse the accepted CAPRUN process-group/namespace/start-identity supervision and exact full argv registration, inherited file limit, sampled-RSS caveat, +15-second admission margin, original stored hard cutoff and post-return deadline check. Do not reuse an old enabled authority or assume the frozen v2 builder dispatcher accepts a solver. A narrowly reviewed new engine-operation binding is necessary; CAPRUN itself needs no change. Engine input-file invocation and its absolute CLI vector must be checked against the installed version before enabling—no executable or syntax probe occurred here. One child at a time, exclusive outputs, pre/post pins and post-run owned-PGID audit remain mandatory. Any cap, parser/mapping mismatch or late return yields no decision.

The two historical shell runners are case-specific and have inner GNU timeout/kill-after=300; neither is reusable authority. Their generators hard-code another nine-variable case and a block order. Only their documented-looking `lift(I,target,U)` call and explicit printing of U/T/residual informed this plan; no historical input, result or generator was executed or imported.

## 6. Minimal delta-review boundary and stop

Only the following new source needs a future Fable delta review: artifact-to-Singular emitter plus exact row read-back/parser; single rational-ring/global-order engine script and certificate export; independent sparse certificate parser/comparator/division/S-pair/unit checker; exact new engine/verifier authority bindings and exclusive-output/cap wiring. Review changed objects: dropped constant/guard, swapped variables or rows, float/rounded rational, U=0 or U=u, bad cofactor, failed S-pair, and an input not reducing to G. These are proposed future controls, not executed tests.

Do not re-review the accepted Euler reconstruction, source/lift mathematics or CAPRUN implementation absent a concrete delta. The pending runtime gate remains separate. Primary compatibility checks still needed are installed-version `std`/`lift`/ring `dp` behavior, exact input-file CLI, and the chosen coefficient/exponent exporter semantics. Root's current manual observation narrows that check but does not erase it. No network retrieval, code, mathematical check or solver execution was performed in this design.

The only honest outcomes of the future lane are VERIFIED UNIT, VERIFIED PROPER, or INCONCLUSIVE. This report selects the plan; it supplies none of those mathematical verdicts and grants no execution or follow-on authority.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10696`.
- Body SHA-256:
  `4375b6115723300b42eda6ca8d72471d26d09e920d0b7d5d01e8e574cdd89844`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
