# Gate: F10 r1 accepted-premise actual-degree scope composition (FIRST Fable5.1 review, hostile manual)

2026-09-10. FIRST review of the UNREVIEWED conditional interface composition f10-r1-degree-scope-astra-20260910.md. First command 12:11:08 UTC; controlling stop 12:26:08 UTC (earlier of first+15 minutes and 12:29:00, never reset); final three minutes reserved. ZERO mathematical subprocesses, CAS, scripts, imports or tests; manual algebra and documentary reading only. Writes: this file and box/f10-r1-degree-scope-gate-fable5-20260910/ only, via apply_patch. Status: UNSEALED until the standalone body-end line is appended.

Verdicts: A CONFIRMED, B CONFIRMED (perimeter only, no missing arrow), C CONFIRMED (duplicate conditional derivation, no new mechanism), D CONFIRMED (all four controls genuine). Promotion wording in F.

## 0. Custody, prior involvement, read scope

Exactly three immutable inputs in /tmp/jc2-lane.cFa39t/inputs were hashed with sha256sum before any read; all three digests matched the charged list (copied into the owned box custody.txt from the sha256sum output, not typed):

- a18055f3088957ce9892e5f1288a3df03f1f00700a71a97b31a31255b200ebef ACCEPTED-INTERFACES.md, 30778 B, 71 lines
- dc4f601ea661c73a23b5f138afbde11f71525dac0ad555e3160e6aea7c439d68 f10-r1-weighted-composition-gate-fable5-20260909.md, 13353 B, 93 lines
- 81ab7f3685e330ffac746fdcef5e911ea27d795c15265ceacc047be05b20be95 f10-r1-degree-scope-astra-20260910.md, 11458 B, 93 lines

Both owned targets were absent at first action (ls returned No such file or directory for each). Read WHOLE: all three files, every line. The ACCEPTED-INTERFACES file is exactly six labeled literal AUDIT excerpts (16m, 16p, 16r, 17b, 17j, 17zze), not the ledger and not any component proof; the two accepted objects are consumed as conditional premises at their excerpted tier, not re-proved. No link, provenance body, original report, code, certificate, current ledger, peer, process, network or external source was followed or inspected.

Prior involvement: this reviewer model authored the charged 17j gate (dc4f601e...) and the earlier Fable gates named inside the excerpts (16m, 16p, 16r, 17b, 17zze). Those are used here only through the six excerpts; no recollection of their bodies is used as a premise. Genuine WHOLE scope is the three files above and nothing else.

## A. Arbitrary 112/196 pair to a point of the zero ring: CONFIRMED

Quantified statement checked: for every characteristic-zero field K and P,Q in K[X,Y] with [P,Q] in K*, (deg P, deg Q) is neither (112,196) nor (196,112), degrees being ACTUAL ordinary total degrees in K[X,Y]. This is 16m's degree notion verbatim ("ordinary ... ACTUAL total degrees"). 16m's hypothesis is a pair of degrees with a nonzero constant Jacobian; [Q,P] = -[P,Q] is again a nonzero constant, so the swapped order is inside the same hypothesis and needs no separate premise.

Index chain: q_col = 2 (16m), printed F10 index j = 0 (16m: "(q-1)(j+1)=1, hence q=2, j=0"), r = 1 (16p/16r: m = 3r+1, n = 5r+2). The identification is pinned by the exponent pair (4,7), which 16m names explicitly ("supplies 16l at increasing exponents (4,7)") and which equals (3r+1, 5r+2) only at r = 1; 16r's 28m/28n endpoint (112/196 at r = 1) and 17b's "Source degrees remain 112/196" at r1 close the loop. The letter q in 16p's "r=q+1" is therefore the F10 index, not q_col. The producer's disambiguation is right and nothing rests on the letter.

Arrow audit; each arrow is either elementary or a quoted sentence of a charged excerpt:

1. K to C. The finitely many coefficients generate a finitely generated field over Q, which embeds in C; an embedding keeps nonzero coefficients, actual degrees and the nonzero constant Jacobian. Elementary, and 16m's own retained transfer sentence. No original-field normalizer is needed because the contradiction is reached over C.
2. C pair to F10(0) representative. 16m "Exact theorem" at q = 2: any such complex pair has an affine-normalized ordinary rectangular representative which, after output swap, has the PRINTED F10(0) profile with degrees 196/112. 16m's "Output swap" paragraph licenses the swap by transferred face multiplicities and horizontal standardness; the swap only negates the Jacobian scalar.
3. Representative to 16k and 16l. 16m "Composition pass": it "supplies the ordinary rectangular actual F10(0) hypotheses of 16k, whose output-swap cover in turn supplies 16l at increasing exponents (4,7)".
4. 16k source to the compressed presentation. 16p "Composition/limits": the 16k->16l/16n->16o chain "supplies every hypothesis for the entire specified ordinary F10 stratum", an all-q NECESSARY compression. At r = 1 its statement reads deg_S A_i <= 4-i, deg_S B_i <= 7-i, leading coefficients C0 S and D0 S^2 with C0 D0 = c, monic S^4, S^7 attained, Jacobian +c Delta including -c S^2 t^7. Producer step 3 quotes these correctly and correctly refuses a constant-Jacobian reading in this chart.
5. Compressed source to L_1. 16r "Composition/decision boundary": "All 16p necessary sources map to L_r". Own checks that this arrow drops nothing: dividing A by C0 and B by D0 gives A_3 = S, B_5 = S^2 and Jacobian Delta; the actual B satisfies the upper rows, so it equals B* plus beta A plus gamma, and the gauge removes beta, gamma without touching the Jacobian; a = [S^4]k = 1/C0 and b = [S^7]B_0* = [S^7]B_0 = 1/D0 (deg k <= 4 < 7, 16r's m < n remark) are nonzero, so omega = 1/(ab) meets the guard. Own check that 16r's A-shape is the A-side inverse-pole condition, not an extra restriction: with t = 1/z, S = z w, w = p z^2 - z + u, one has S t^3 + (S d - u) t^2 + (1 - u d + S v) t + k = p + (p z - 1) d(S) + w v(S) + k(S), polynomial in (p,z); conversely, for a general A with A_3 = S the z^-2 and z^-1 parts vanish exactly when A_2(0) = -u and A_1(0) = 1 - u d(0), which is the displayed shape with deg d <= r, deg v <= 2r. Every actual source is polynomial in (p,z) (16p's u = -h statement), so the shape is necessary. Own check that E1 and E0 are the complete t^1 and t^0 rows of A_S B_t - A_t B_S - Delta with [t^1]Delta = u and [t^0]Delta = 1: [t^1] gives 2k'B_2 + h'B_1 - hB_1' - 2fB_0', [t^0] gives k'B_1 - hB_0', as printed.
6. L_1 point over C to the 17b retained system. 17b "Retained full-source interface": existence preserved in both directions over every characteristic-zero field, all accepted inverse-pole constraints preserved, EVERY [S^0..S^7]E1 and [S^0..S^8]E0 kept. Own check of the inverse formulas: with s = H/a, v = F a/H^2, w = a^2/H^3 one gets w s^2 = 1/H, w s^3 = 1/a, v/(w s) = F, and the guard gives omega = w s^8 f5, all invertible because w, f5 are proved units of B and s is a unit; H != 0 from the guarded leading ODE and a != 0 from the guard. The two top rows [S^8]E1, [S^9]E0 are the f6 = f7 = 0 relations, so the point defines a Q-algebra map from the FULL B = Q[v]/(p) to C; no factor is chosen and no extra root choice is required.
7. 17b system to the eleven-slot quotient. 17j "Exact triangular quotient" and its gate A/C: each band map is a quotient isomorphism with its accepted inverse; all other rows, whole mate, gauges beta = gamma = k(0) = 0, both inverse-pole conditions and omega = w s^8 f5 are transported by substitution, not dropped; the third forcing uses D_i.
8. Eleven-slot quotient to the complete normalized ring. 17j "Normalized polynomial reconstruction" and gate B/C (all-algebra equivalence over the full rank-7 B). Own check of the direction used: z H1 - U H0 = U s^7 - U s^7 = 0 and H0^2 = s^14 = z^7 hold in the eleven-slot ring, so the natural map from R/(z H1 - U H0, H0^2 - z^7) exists and a point of the eleven-slot ring restricts to a point of the normalized ring; z = s^2 and hence H0 are units there, so the guard inverts nothing a point could violate (17zze correction (4)).
9. Zero ring. 17zze: "the complete normalized 17j guarded ring is zero", by accepted 17l/17x transport of the whole-B R_uni certificate through the free faithful rank-3 monic cubic cover, with all B components, unsquared relations and inverse-pole/full-slot data retained. Accepted at its tier as instructed. A unital map from the zero ring to C is impossible.

The composition proves the producer's statement at the named import tier. The two-coordinate slice's field-level equivalence is not separately invoked, as the producer says; the contradiction uses 17zze's assertion about the COMPLETE ring. CONFIRMED.

## B. 17zze's caution is the perimeter of an isolated certificate review: CONFIRMED

17zze's SCOPE sentence lists what its certificate alone is NOT, and in the same breath says the external 16q/classical source-admissibility chain "is not newly re-proved". That is the perimeter of a review conducted without 16m/16p/16r charged; it is not a claim that the composition fails. 16r's decision-boundary sentence ("A unit at r=1 would close the remaining 112/196 entry and the D28 numerical column via 16m") is the accepted announcement of exactly this composition, and 16m's composition pass stops at "does NOT close 112/196" only because the unit was then absent. With 16m/16p/16r/17b/17j charged there is no missing implication; there is no first missing arrow to print. Neither a coordinate-invariant r nor an original-coordinate cofactor is logically required: the argument refutes the existence of a normalized representative that 16m makes necessary. The promotion must restate the caution as true of 17zze in isolation, not delete it and not read it as a campaign-wide prohibition.

## C. Whole D28 column: duplicate conditional derivation, CONFIRMED

16m's exact theorem is stated for every integer q >= 0 with q != 2 on exactly the family (28(q+2), 28(2q+3)). Own check: gcd(q+2, 2q+3) = gcd(q+2, -1) = 1, so the gcd is exactly 28 and the ratio (q+2)/(2q+3) lies in (1/2, 2/3], matching 16m's filter. The swapped column is inside the same theorem because the hypothesis is a pair of degrees with a nonzero constant Jacobian in either order. Section A fills the single q = 2 exception. Hence the displayed column and its swap are conditionally empty. This is a duplicate conditional derivation of the consequence 16r and 16m already announced, not a new mechanism. It says nothing about other gcd-28 pairs, all degrees up to 196, a maximal-degree-196 bound, all-r F10, global source coverage or JC2.

## D. Changed-premise controls: CONFIRMED

- Drop 16m: correct. Without it there is no arrow from an arbitrary 112/196 pair to the F10(0) stratum; that is the first missing implication in the weakened set.
- Replace the whole-algebra endpoint by a chosen factor of B or a generic chart: correct. A point over an omitted factor or on an inverted locus would not map into the unit; 17zze's endpoint is whole-B with only the forced units z, H0 and B's proved units inverted.
- Keep only the leading ODE: correct. 16m records that the cubic/quintic ODE has solutions and 17b gives seven geometric orbits; it excludes nothing alone.
- Omit the original-source cofactor: correct. Existence of a point is refuted directly; 16r's Nullstellensatz sentence yields an existential unit statement, not an explicit cofactor.

Each control removes a load-bearing premise and the conclusion then fails, so the controls are genuine. No omitted control is load-bearing: dropping field transfer, output swap, the gauges, the inverse-pole shape or the retained scale each breaks one of arrows 1-8 above, and the producer names all of them in section 2.

## E. Non-blocking notes

- 16p's h (in z = p^2 - g + ell p + h) and 16r's h (= A_1) are different objects; the producer's "in its notation" is the right guard.
- 17zze's excerpt lists the token "b=0" among retained data. It is undefined in the six excerpts and cannot be the 16r guard coefficient b, which 17b makes a unit (b = 1/(s^5 f5)). Promotion wording should not carry the token.
- The producer's controlling stop 12:17:31 and reserve are documentary; nothing mathematical depends on them.
- No deviation from scope: no Write/Edit tool, no redirection, no helper change, no seal, no charge_basis line (no exit-price assertion is made).

## F. Defensible promotion wording

Conditional theorem, composition at the named accepted import tiers of 16m, 16p, 16r, 17b, 17j and 17zze, no premise re-proved: for every characteristic-zero field K, no P,Q in K[X,Y] with nonzero constant Jacobian has actual ordinary total degrees 112 and 196, in either order. Combined with 16m for q != 2, no such pair has actual degrees 28(q+2) and 28(2q+3) for any integer q >= 0, in either order. Named dependencies: 16m's imports (Division Lemma/ML ordinary normalization through GENERAL15x, GGV5.20 and cited interiors, GGHV2.20 and cited interiors, Prop 3.2 actual MN membership, Def 3.3/(3.20), whole Section 5 M = 35 completeness in both orientations, accepted 16h/16g); the 16k/16l/16n/16o/16q interfaces consumed through 16p and 16r; accepted 17a through 17b; accepted 17l/17m/17x and the executed 17zze certificate with its recorded review and workflow qualifications. Status: KNOWN CONDITIONAL COMPOSITION / DUPLICATE DERIVATION of 16r's announced consequence. Not claimed: any other degree pair, gcd-28 pairs in general, a maximal degree 196, all-r F10, global source coverage, JC2, an explicit original-coordinate cofactor certificate, or coordinate-invariance of r. 17zze's "not every map of degrees 112/196" remains true of that certificate in isolation. No new task, no re-audit of accepted imports, no runtime work follows.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only check: xmodel/f10-r1-degree-scope-gate-fable5-20260910.md and box/f10-r1-degree-scope-gate-fable5-20260910/ were absent at first action (ls errors recorded); apply_patch Add succeeded for both; no corpus scan. A post-write ls of xmodel/ for the stem also lists the harness lease siblings f10-r1-degree-scope-gate-fable5-20260910.run.v2 and .log (both timestamped 12:10:57, before the 12:11:08 first command) and the producer's report plus artifact.json (12:04:09); none is an owned target and none was read or modified. The box/ listing also shows f10-r1-degree-scope-gate-prep-20260910 and f10-r1-degree-scope-prep-20260910, different names, not touched.

<!-- BODY-END -->
