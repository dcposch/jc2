# Publication copy of the independent D4 review

Published by swarmHQ ROOT from the completed Fable review; September 17, 2026.
Evidence tier: MANUAL. Lifecycle: completed independent review, not itself a
grant of promotion authority. Reviewed producer commit:
1cd8e47f7e28cb6311a3100e9c7644e9f5503239.

The entire original reviewer body below is preserved verbatim. Original body:
14766 bytes, SHA256
62cb3dbc8b1d4ab0bbe9bbc1ada1bff9e075c5821114dc3d5b80af1bd29c7e7e.
ROOT verified the supervisor terminal and the original processes absent before
receipt-first collection; exit0/DONE and all four charged inputs unchanged.
Original report, receipt and log are retained unchanged and read-only. The
legacy BODY_SEALED label denotes the completion-marker boundary, not the
canonical post-body seal added to this separately named publication copy.

ROOT accepts the independent checks of the precise producer statement:
the displayed D4 curve/module violates the representation-only rational-base
criterion. The direct rational compact-support argument suffices; the
reviewer's optional Chevalley--Weil route and other Weyl-type comparisons
are not additional campaign theorem imports or family promotions. The phrase
"no simpler failure exists" supplies no mathematical minimality claim.
No actual Keller source or geometric-unit realization is provided.

ROOT ran the trusted collision checker on this publication copy before
canonical finalization. Its complete output follows; the reviewer's own
manual block remains unchanged within the original body below.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

---

# Independent hostile review: D4 rational-base counterexample

STATUS: COMPLETE (exact audit finished; no minimum occupancy used)

Reviewer: swarmHQ Fable independent reviewer. Adapter request: model=fable, effort=max. The exact hosted model identity is not independently exposed to this reviewer; the runtime self-reports claude-fable-5-1, which is a self-report, not a verification.
Lane: d4-rational-base-review-20260917. Evidence tier: MANUAL. Lifecycle: review-only; this reviewer has no promotion authority, does not seal, and does not call artifact_finalize. The legacy lane parent owns custody.
Producer under review: xmodel/d4-rational-base-counterexample-swarmHQ-root-20260917T191600Z.md (swarmHQ ROOT/Astra, producer basis c06af4b3), read completely from the immutable snapshot /tmp/jc2-lane.0diQ0X/inputs.
Frozen public basis: 1cd8e47f7e28cb6311a3100e9c7644e9f5503239; git rev-parse HEAD returned the same value, and the producer file recorded at HEAD hashes to the pinned value below.

## Summary verdicts

1. Finite group, generators, inertia orders, Riemann-existence realization: CONFIRMED.
2. Rational equivariant H^1 computation, duality, zero Hom dimension: CONFIRMED.
3. Orbit-index lower bound and one-infinity quotient contradiction: CONFIRMED.
4. Claimed scope and positive/negative controls: CONFIRMED.

Exact question answered: YES, the witness refutes the universal implication "for every smooth affine G-curve C with C/G = A1 and nonzero rational G-module M with M^G = 0 and Hom_G(M,H^1(C,Q)) = 0, some H <= G has C/H = A1 and M^H != 0". A universal statement is refuted by one (C,G,M) meeting the hypotheses and violating the conclusion; the witness G = W(D4), M = Q^4, C = RET curve minus its infinity fibre does exactly that. No hypothesis needed silent repair. No simpler failure of the producer's claim exists because the claim is correct.

## Pins and read limits

Pre-read sha256sum of the snapshot, all matching the charged pins:

- d4-rational-base-counterexample-swarmHQ-root-20260917T191600Z.md 65906bbadc41f8107df0a2d76f7c8966b77b07e52289c689a2a5867f86d4a29a
- FALLACY-v2.md e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
- COORDINATION.md 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e
- APPROACHES.md 485b88d7a990268b438e4110f3bdc32d31925efa2a6cd2bc2f0fa90f7bdcd05f

Post-read: the same four values were rechecked with sha256sum -c immediately before this final write, and the write was gated on that check passing. Producer seal reproduced: first 8965 bytes hash to 99b369f08791bb2ff11580e8372c8c22ba0926bd2e9ed634b17f978ed29be86f and end with the unique standalone BODY-END line plus newline.

Read limits: producer read completely (9297 bytes); FALLACY-v2 and COORDINATION read completely; APPROACHES consulted only as scope context (the globalization-bridge paragraph). No other live report, log or receipt consumed. No new source retrieval, no CAS, no scientific Python, no network, no descendants, no Git mutation, no edit to any input. Read-only shell used for date, command -v, ls, sha256sum, git rev-parse and git show, cat, grep, sed, head, od. Integrity evidence is not mathematical proof. Startup acknowledgment written once to the runtime directory and set to mode 444.

## Verdict 1: group, generators, inertia orders, RET realization — CONFIRMED

Independent reconstruction.

- W(D4) is the group of even signed permutation matrices on Q^4: order 4!*2^3 = 192.
- s1 = (12), s2 = (23), s3 = (34) are coordinate transpositions. s4 is the reflection in the root e3+e4, s4(v) = v - (v.(e3+e4))(e3+e4), so s4 e3 = -e4, s4 e4 = -e3, e1 and e2 fixed. Each s_i has order 2 and a 3-dimensional fixed hyperplane (v1=v2, v2=v3, v3=v4, v3=-v4 respectively).
- s3 s4 = diag(1,1,-1,-1): e3 -> -e4 -> -e3 and e4 -> -e3 -> -e4. Its S4-conjugates are all pair sign flips, which generate the even sign group of order 8; with S4 = <s1,s2,s3> this is all of G. Generation confirmed.
- c = s1 s2 s3 s4, rightmost first, recomputed coordinatewise: e1 -> e2 (only s1 moves it); e2 -> e3 (s2 moves it to e3, s1 fixes e3); e3 -> -e4 -> -e3 -> -e2 -> -e1; e4 -> -e3 -> -e4 -> -e4 -> -e4. So c: e1 -> e2 -> e3 -> -e1, e4 -> -e4. The signed permutation has two minus signs, so c lies in G. c^3 = -I, hence ord c = 6 exactly (a Coxeter element; the Coxeter number of D4 is 6, consistent). The producer's remark that c is not of order 2 is right.
- (s1,s2,s3,s4,c^{-1}) has product s1 s2 s3 s4 c^{-1} = 1 and generates G. Inertia orders 2,2,2,2,6.
- Named standard imports, used as imports and not freshly primary-proof-audited: Riemann existence (for distinct points p1..p4, infinity on P1 and a generating product-one tuple there is a connected Galois cover X -> P1 with group G whose local monodromy at p_i is conjugate to s_i and at infinity conjugate to c^{-1}) and GAGA algebraization (X is a smooth connected projective complex curve and the cover a finite algebraic map). Every tuple entry is nontrivial, so the branch locus is exactly these five points. G acts faithfully as the deck group. The fibre over infinity is the G-set G/I, I = <c> cyclic of order 6 up to conjugacy, with 192/6 = 32 points. C := X minus that fibre is smooth, connected, affine (nonempty finite set removed from a projective curve), G-stable, and C/G = (X/G) minus {infinity} = A1. These are exactly the removed points claimed.
- RET fixes the inertia generator over a given branch point only up to conjugacy; nothing below uses more than the conjugacy class and its order, so this is not a gap.

Riemann-Hurwitz recomputed: 2g-2 = 192*(-2 + 4*(1-1/2) + (1-1/6)) = 192*(5/6) = 160, so g(X) = 81; 32 punctures; b1(C) = 2*81 + 32 - 1 = 193. All three producer numbers confirmed.

## Verdict 2: rational equivariant H^1, duality, Hom dimension — CONFIRMED

Recomputed by two independent routes.

Route A (the producer's compact-support route, checked step by step).

- The Grothendieck group of rational G-modules injects into class functions via the character (characteristic 0), so every identity may be checked on characters.
- Free part: let U = A1 minus the four finite branch points, chi_c(U) = 2 - 5 = -3, and C_U its preimage, on which G acts freely. For g != 1 the Lefschetz number of g on H_c^*(C_U) is chi_c of the fixed locus, which is empty, hence 0; for g = 1 it is chi_c(C_U) = 192*(-3). That is exactly -3 times the regular character, so chi_{c,G}(C_U) = -3[Q[G]]. The producer's cell-lifting sentence is an equivalent argument. Either way this is an Euler-characteristic identity and does not claim the local system is trivial.
- Each finite branch fibre is the G-set G/<s_i> (stabiliser = inertia of order 2, 96 points), contributing +[Q[G/<s_i>]]. Additivity along the G-stable open/closed decomposition is the equivariant compact-support long exact sequence.
- Whole-curve cross-check: chi_c(C) = 2 - 162 - 32 = -192 = -3*192 + 4*96. For g != 1 the number of fixed points of g on C is its number of fixed points on the four branch fibres, i.e. the permutation character of the sum of the Q[G/<s_i>], as the formula requires.
- H_c^0(C) = 0 (connected and noncompact), H_c^2(C) = Q with trivial action (holomorphic automorphisms preserve orientation). Hence [H_c^1] = [Q] + 3[Q[G]] - sum_i [Q[G/<s_i>]].
- Poincare duality H^1(C,Q) = H_c^1(C,Q)^* is G-equivariant because the cup-product pairing into H_c^2 = Q is G-invariant. Q and every permutation module are self-dual. Therefore (1) holds with the printed sign: [H^1(C,Q)] = [Q] + 3[Q[G]] - sum_i [Q[G/<s_i>]], of dimension 1 + 576 - 384 = 193 = b1. Independent sign check: (1) predicts tr(g | H^1) = 1 - #Fix_C(g) for g != 1, which is the ordinary Lefschetz formula for a finite-order automorphism with isolated fixed points. The Tate twist is irrelevant over Q with no Galois action.
- Hom dimension: dim_Q Hom_{QG}(M,N) equals the character inner product and is additive in N (Maschke). M^G = 0 since diag(-1,-1,1,1) and diag(1,1,-1,-1) kill all coordinates. M is self-dual via the dot product, so dim Hom_G(M,Q) = dim M^G = 0. dim Hom_G(M,Q[G]) = dim M = 4. By Frobenius reciprocity dim Hom_G(M,Q[G/<s_i>]) = dim M^{s_i} = 3 for each reflection. Total 0 + 12 - 12 = 0.

Route B (Chevalley-Weil on the closed curve plus the puncture sequence).

- For X -> P1 with five branch points, the multiplicity of the irreducible M in H^1(X,Q) is 2*dim M*(0-1) + sum over branch points of (dim M - dim M^{inertia}) = -8 + 4*(4-3) + (4 - dim M^c). Since c^3 = -I, c has no eigenvalue 1 and M^c = 0. Total -8 + 4 + 4 = 0.
- The sequence 0 -> H^1(X) -> H^1(C) -> Q[G/I] -> Q -> 0 gives [H^1(C)] = [H^1(X)] + [Q[G/I]] - [Q], and the multiplicity of M in Q[G/I] is dim M^I = 0. So M has multiplicity 0 in H^1(C,Q), and the dimension is 162 + 32 - 1 = 193. Agrees with Route A.

Rational versus complex multiplicities: M tensor C is irreducible (its restriction to the even sign group has four pairwise distinct coordinate characters, e.g. diag(-1,1,-1,1) separates the first two, and S4 permutes the four lines transitively), so the Schur index is 1 and rational and complex multiplicities agree. This is not needed: the dimension identity is a character inner product valid over Q directly, and the producer does not pass from missing complex characters to missing rational constituents.

## Verdict 3: orbit-index lower bound and one-infinity contradiction — CONFIRMED

Orbit bound, rechecked with repeated and negative coordinates.

- Let v != 0 have support S of size k. For k <= 3: for every k-subset T and every sign pattern sigma on T some element of G sends v to a vector with support exactly T and signs exactly sigma (permute S onto T, then impose the signs on T and fix the parity on a zero coordinate, which exists since k <= 3). These images are pairwise distinct: different supports differ, and equal supports with different sigma differ at a coordinate where both entries are nonzero with opposite signs. Repeated absolute values or negative entries of v play no role because only support and sign pattern are compared. Counts 4*2 = 8, 6*4 = 24, 4*8 = 32.
- For k = 4 the even sign group N acts freely on v (epsilon v = v forces every epsilon_j = 1 because every v_j != 0), so |Gv| >= |N| = 8.
- Hence |Gv| >= 8 for all v != 0, attained at v = e1 (orbit the eight vectors +-e_i). If M^H != 0 choose v != 0 fixed by H; then H <= Stab_G(v) and [G:H] >= [G:Stab_G(v)] = |Gv| >= 8.

Geometric side, rechecked for nonnormal H and for an abstractly given A1.

- C/H is a smooth affine curve (a normal curve, and a finite quotient of an affine variety is affine). X/H is a smooth projective curve containing C/H as a dense open subset; the smooth completion of a smooth curve is unique, so if C/H is isomorphic to A1 as an abstract variety then X/H is P1 and X/H minus C/H is exactly one point. No normality of H and no property of the map C/H -> C/G is used.
- X/H minus C/H is the image of the infinity fibre X_inf = G/I under the orbit map X -> X/H, so its cardinality is the number of double cosets |H\G/I|. Inversion g -> g^{-1} gives |H\G/I| = |I\G/H|, the number of I-orbits on G/H. One point at infinity is therefore equivalent to I = <c> acting transitively on G/H, which by orbit-stabiliser for a cyclic group with one orbit forces [G:H] to divide |I| = 6. Replacing I by a conjugate (another point of X_inf) changes nothing.
- 8 <= [G:H] <= 6 is impossible. So no subgroup H with M^H != 0 has C/H isomorphic to A1. This includes H = {1}: C itself has genus 81 and 32 punctures.

## Verdict 4: scope and controls — CONFIRMED

- Refutation logic: the target implication is universal over (C,G,M); the witness satisfies every hypothesis (Verdicts 1 and 2) and violates the conclusion (Verdict 3). It refutes exactly the bare representation-only criterion of the producer's Section 1 and nothing stronger.
- Positive control (C2 on A1 by z -> -z, M the sign module): C/G = A1 via z -> z^2; M^G = 0; H^1(A1,Q) = 0 so the Hom vanishes; H = {1} gives C/H = A1 and M^H = M. Correct, so the hypotheses are nonvacuous. There the infinity inertia has order 2 and the minimal nonzero orbit is 2, so the necessary condition [G:H] <= |I| from Verdict 3 holds with equality; the D4 witness relies on minimal orbit 8 exceeding |I| = 6. Correct and informative. As context only: for Weyl groups of type A_n and B_n the minimal orbit of the reflection representation equals the Coxeter number, so the mechanism first bites at D4; for S3 with its 2-dimensional standard module the vector (2,-1,-1) has orbit size 3 = |<(123)>| and H = <(23)> gives one point at infinity, so that smaller candidate is not a witness. No census or descendant is proposed.
- Negative-scope control: agreed and independently affirmed. No Keller source, no geometric-unit realisation of M, and no map from a base-changed source to a unit torus is constructed. The witness does not refute geometric-unit vanishing, does not exclude a geometry-enhanced reduction, is not a JC2 counterexample, and does not depend on any unproved log-trace pairing calculation. The producer states each of these limits explicitly and preserves the failed stronger readings.
- Basis consistency: the producer basis c06af4b3 precedes the recording commit 1cd8e47f, which is the frozen public basis here; the recorded file at HEAD hashes to the pinned value.
- The producer's disclosure that ROOT plus a same-model Astra instance co-checked is correctly labelled as not the required different-model review; this report is that different-model hostile review.

## FALLACY-v2 pass

No exit claim is made, so no charge_basis line is needed. Floor/attainment: the orbit bound is used only as a floor (at least 8) against a ceiling (at most 6), so no attainment claim is required; the sole equality used, ord c = 6, is computed exactly. Variable/ring map: the only coefficient change is Q to C for the irreducibility remark, declared and not load-bearing. Prime label: c^{-1} is a group inverse, not a derivative. No gap was filled by cap or analogy.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — this review raises no `OPEN[...]` entries. Comparison with the producer: its block is also `status: EMPTY` with no raised OPENs; the two are consistent. This block was written manually because the collision script was not executed under this lane's read-only restriction; no automatic OPEN or successor is created.

## Custody notes

Outputs of this lane: /home/ubuntu/swarmHQ/runtime/d4-rational-base-review-20260917/FABLE-STARTUP.md (mode 444) and this report. Nothing else was written or modified. No artifact_finalize, no seal.py, no Git mutation, no shared-ledger edit; the legacy lane parent owns custody and collects receipt-first after independent termination.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16436`.
- Body SHA-256:
  `7533ca4648caf31e4b95a316e025519d901ca82f26600a9ea4c7155eddd7964e`.
- Frozen basis: `1cd8e47f7e28cb6311a3100e9c7644e9f5503239`.
