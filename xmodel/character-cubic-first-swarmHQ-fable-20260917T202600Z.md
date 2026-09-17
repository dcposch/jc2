# Character-cubic FIRST: preserved independent review

Publication custodian: swarmHQ ROOT (Astra), September17,2026.
Frozen publication basis: 846870e462d1e7bef517852a8a1dbec5e4a25700.
Evidence: MANUAL / independent hostile review of CHARACTER-CUBIC-NONEXACTNESS-1.
This is a publication copy, not a new producer claim or an expanded theorem.

ROOT independently verified termination and the absence of the original
processes/owned descendants before receipt-first collection. The original
terminal review had SHA256
bd15ddce8c7cb92597fa436a4aab871b480526b63df0e06e5c1ae33e8dccbcf2
and 18550 bytes; report/log/receipt were frozen read-only without changing
any hash. The original's completion marker is not a canonical post-body
seal. This separately named copy preserves the entire review below VERBATIM
and adds this provenance and a new canonical publication seal.

The review independently confirms all five exact items. ROOT reconstructed
the residue/continuous-differential/finite-trace proof before accepting its
verdict. Affine singularities, arbitrary finite degree and ramification are
covered. The paper's bibliographic/formula mapping was not re-audited by the
reviewer and is not a proof dependency. Its optional whole-boundary
smoothness observation is not a separate promoted claim. Hosted model
identity remains harness-reported, not independently attested.

The reviewer's COLLISIONS block below was manually supplied; ROOT's
independent publication collision check completed with status EMPTY and
no explicitly raised open entries. Its exact read limits
are preserved, including the partial frontier read. No scientific code,
parameter sample or model agreement is substituted for the written proof.
Promotion, if recorded in AUDIT, concerns ONLY the fixed form and constant
multipliers, not all rational maps, other Painleve phase spaces, a general
Keller-source reduction, or JC2. No successor family is admitted here.

## Verbatim terminal review

# Independent hostile review: character-cubic finite-cover nonexactness

status: COMPLETE (review finished; all five items decided)
kind: MANUAL / review-only. No promotion authority. No seal, no artifact_finalize; the legacy lane parent owns custody.
reviewer: Fable independent reviewer, requested adapter model=fable, effort=max. Harness-reported model id claude-fable-5-1. The exact hosted identity is not independently exposed to this process and is not verified here; different-model status relative to the producer (swarmHQ ROOT, Astra, with a same-model Astra co-check) rests on the harness report only.
reviewed claim: CHARACTER-CUBIC-NONEXACTNESS-1, producer report written at basis 3214fd164b78aaf49a2a6c7b231ad7f2d8c20010 and recorded by the frozen commit below.
started_utc: 2026-09-17T20:14:27Z; draft created 20:19Z; final text written at about 20:24Z.
frozen_basis: 846870e462d1e7bef517852a8a1dbec5e4a25700 (git rev-parse HEAD equal; no submodule recursion; jc2-lean and jc2-web not entered).
startup acknowledgment: /home/ubuntu/swarmHQ/runtime/character-cubic-review-20260917/FABLE-STARTUP.md, mode 0444, sha256 cc563c7698c0eb97595896e618ddb5f015704a3cb456610cb6620c6aaaa4cfd2.
tools: no CAS, no scientific code, no enumeration, no network, no Git mutation. Only date, command -v, readlink, ls, sha256sum, cat, grep, od, printf and apply_patch were used.

## Summary verdict

CONFIRMED on all five items. No REFUTED item. No GAP affecting the stated claim. Every recomputation below is my own, done by hand from the producer's displayed formulas; the Mazzocco-Vidunas paper was not retrieved and no Painleve classification is imported.

## Pins: pre-read and post-read

Pre-read at 20:14Z by sha256sum; post-read re-run by sha256sum -c immediately before this text was written, with the write conditioned on MATCH:
- character-cubic-nonexactness-swarmHQ-root-20260917T200800Z.md 55ca0574e83b51ef84113d65ea93d1d306a0330d8d0dada99d33ef40f15c0548 pre MATCH / post MATCH
- FALLACY-v2.md e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5 pre MATCH / post MATCH
- COORDINATION.md 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e pre MATCH / post MATCH
- APPROACHES.md d5d5e9b3eb8b6ad7379203dd148d7cd6bc8557186458b8750cfef2d1f58dd13b pre MATCH / post MATCH

Producer-cited campaign evidence, hash-checked only (contents not read):
- xmodel/source-volume-residue-integration-root-20260911.md 91ce3ee72fcdf88091806a9c7990f0c0be48006c45b42930272f5bc1a34f5eb8 MATCHES the producer's cited SHA
- xmodel/volume-neutral-torus-quotient-swarmHQ-root-20260915.md 181d7ae11675d27a61da977f143abaf5797415d6c64923e11be336281ce6df80 MATCHES the producer's cited SHA
- xmodel/keller-trace-node-astra-20260911.md: producer cites no SHA; file present with sha256 97c4a0fda9e23bed5f16671abfb4d026a065ae040345240a82ecade3b878af76; not compared, not read

## Actual read limits

- Producer report: read whole (10650 bytes) including its Seal section. Its body-hash claim (10317 bytes, 3c8269195f409abff6af6b156491a3b78d23aec5abcb6fb76e08e546efd00086) was not recomputed; the file-level pin above is what this review verifies.
- FALLACY-v2.md and COORDINATION.md: read whole.
- APPROACHES.md: NOT read whole. Only a case-insensitive grep for character, cubic, painlev, nonexact, symplectic, area form was run (hits at lines 19, 118-135, 198-219, 360). Frontier is scope context only, not a mathematical dependency.
- Not read: the three cited campaign reports, the paper 1011.6036v2, AUDIT.md, PROGRESS.md, and any live lane log, receipt or ledger.

## Item 1. All-parameter integrality of the cubic and the chosen function field: CONFIRMED

Independent recomputation. f = z^2 + (xy - C) z + (x^2 + y^2 - Ax - By - D) is monic of degree 2 in z over R = C[x,y]. Any factorization in C[x,y,z] has z-degrees (0,2) or (1,1). A (0,2) factor is a nonunit of R dividing the leading coefficient 1, impossible. A (1,1) factorization gives a root of f in C(x,y) (Gauss; f is monic hence primitive), i.e. Delta = (xy - C)^2 - 4(x^2 + y^2 - Ax - By - D) is a square in C(x,y).

Polynomial-versus-rational step (attacked as requested): if Delta = (p/q)^2 with p, q in R coprime, then q^2 divides p^2 in the UFD R, so q is a unit; equivalently sqrt(Delta) is a root of the monic T^2 - Delta over the integrally closed domain R. So a square root, if one exists, lies in R. The producer's step is correct.

Square test for all parameters: Delta = x^2 y^2 - 2Cxy + C^2 - 4x^2 - 4y^2 + 4Ax + 4By + 4D. If g^2 = Delta then deg g = 2 and the top form of g squares to x^2 y^2, so g = (+/-)xy + (a x + b y) + c. The degree-3 part of g^2 is (+/-)2(a x^2 y + b x y^2); Delta has no cubic terms, so a = b = 0. Then g^2 = x^2 y^2 (+/-) 2c xy + c^2 has x^2-coefficient 0, while Delta has x^2-coefficient -4. The -4 is parameter-free, so no value of (A,B,C,D) escapes. Hence f is irreducible for ALL parameters, C[x,y,z]/(f) is a domain, S is integral, and K = C(S) = C(x,y)[z]/(f) is a field of degree 2 over C(x,y). The producer's argument matches mine step for step.

Nonvanishing of the denominator: if 2z + xy - C = 0 in K then z = (C - xy)/2 lies in C(x,y) and is a root of f, contradicting irreducibility. So omega is a nonzero element of Omega^2_{K/C}, which is one-dimensional over K with basis dx wedge dy because K/C(x,y) is finite separable (characteristic zero). CONFIRMED.

## Item 2. Uniformly smooth infinity vertex, formula, sign and residue 1: CONFIRMED

Homogenization: G = X^2 W + Y^2 W + Z^2 W + XYZ - AXW^2 - BYW^2 - CZW^2 - DW^3; G(1,0,0,0) = 0, so P = [1:0:0:0] lies on the closure for every parameter. The chart X = 1, r = Y, s = Z, w = W gives exactly the producer's F in (1). F_w = 1 + r^2 + s^2 - 2Aw - 2Brw - 2Csw - 3Dw^2, so F_w(0,0,0) = 1 for ALL parameters: P is a smooth point, r, s are regular parameters, the completed local ring is C[[r,s]] (formal implicit function theorem, F_w a unit), and the unique formal solution w lies in (r,s)^2 because F = wU + rs with U = 1 + r^2 + s^2 - Aw - Brw - Csw - Dw^2 and U(0,0) = 1. The producer's (2) is CONFIRMED.

Boundary at P: on S, w = 0 forces rs = 0 because U is a unit, so the two branches r = 0 and s = 0 are the two triangle edges through P. CONFIRMED.

Formula and sign, recomputed two ways.
(a) Direct: x = 1/w and y = r/w give dx = -dw/w^2 and dy = dr/w - r dw/w^2, so dx wedge dy = dr wedge dw / w^3. Also 2z + xy - C = (2sw + r - Cw^2)/w^2 = F_s/w^2. Wedging dF = 0 with dr gives dr wedge dw = -(F_s/F_w) dr wedge ds. Hence omega = dr wedge dw/(w F_s) = -dr wedge ds/(w F_w). With 1/w = -U/(rs): omega = (U/F_w) (dr/r) wedge (ds/s). The producer's (3) is CONFIRMED including the sign.
(b) Poincare-residue cross-check: the Jacobian determinant of (r,s,w) -> (1/w, r/w, s/w) is -1/w^4 and f = F/w^3, so dx dy dz / f = -dr ds dw / (wF); its residue along F = 0 is -dr wedge ds/(w F_w). Same answer. This independently confirms that the affine form dx wedge dy / f_z and the chart formula are the same rational 2-form.

Residue: U/F_w lies in C[[r,s]] with constant term 1, so the r^-1 s^-1 coefficient of the dr wedge ds coefficient is exactly 1, uniformly in A, B, C, D. With the opposite orientation ds wedge dr the value would be -1; nonvanishing, which is all Item 3 needs, is orientation-independent. CONFIRMED.

Singular parameter cases: nothing in the argument uses affine smoothness. I also checked, beyond what the producer needs, that the closure is smooth along the whole triangle W = 0 for all parameters: at [0:Y:Z:0], G_X = YZ and G_W = Y^2 + Z^2 cannot both vanish, and the other vertices are handled by the same formula by symmetry. The Cayley specialization A = B = C = 0, D = 4 has genuine affine nodes, for example (2,2,-2) where f_x = f_y = f_z = 0, and still has F_w(P) = 1 and residue 1. CONFIRMED.

## Item 3. Chain map to CONTINUOUS coordinate differentials; detection of rational nonexactness: CONFIRMED

Embedding through completion (attacked as requested): O, the local ring of the closure at P, is a regular local ring of dimension 2; O -> C[[r,s]] is injective by Krull's intersection theorem, and C[[r,s]] is a domain, so K = Frac(O) embeds in Frac(C[[r,s]]). Since C[[r,s]] = C[[r]][[s]] sits inside C((r))[[s]] inside the field E = C((r))((s)), K embeds in E. CONFIRMED. The iterated ordering (r inside, s outside) is a choice; the argument is symmetric in the two orders.

Chain map (the point the review was asked not to confuse with abstract Kahler forms of E): define delta: K -> E dr + E ds by h -> d_r(iota h) dr + d_s(iota h) ds, where d_r, d_s are the termwise derivations of E. This is a C-derivation of K into a K-module, so the universal property of Omega^1_{K/C} gives a unique K-linear map Omega^1_{K/C} -> E dr + E ds, and its second exterior power gives Omega^2_{K/C} -> E dr wedge ds. Commutation with d, checked by hand: for eta = sum a_i dh_i, the image of d eta = sum da_i wedge dh_i is sum (d_r a_i d_s h_i - d_s a_i d_r h_i) dr wedge ds, while d of the image (sum a_i d_r h_i) dr + (sum a_i d_s h_i) ds is [d_r(sum a_i d_s h_i) - d_s(sum a_i d_r h_i)] dr wedge ds; the mixed second-derivative terms cancel because d_r d_s = d_s d_r termwise, leaving the same expression. No identification of Omega_{E/C} with the two-dimensional coordinate complex is used or needed. CONFIRMED.

Residue kills exact forms with arbitrary poles: for h = sum_j h_j(r) s^j in E (j bounded below, each h_j a Laurent series in r), the s^-1 coefficient of d_s h is 0 times h_0, which is 0, and the r^-1 coefficient of d_r h_{-1} is 0 because the derivative of a Laurent series has no r^-1 term. So Res(d(a dr + b ds)) = 0 for ALL a, b in E, whatever the pole orders in either coordinate. The producer's (4) is CONFIRMED.

Detection: if omega = d eta with eta in Omega^1_{K/C}, apply the chain map: the image of omega is iota(-1/(w F_w)) dr wedge ds = (U/F_w)/(rs) dr wedge ds, residue 1, while it must equal d(image of eta), residue 0. Contradiction. So omega is not exact in the FUNCTION FIELD K. This is stronger than non-existence of a regular primitive on any affine open, and removing divisors cannot change it. CONFIRMED.

## Item 4. Trace compatibility with d for every finite extension; both construction consequences: CONFIRMED

Let L/K be finite; characteristic zero makes it separable. Standard fact: L tensor_K Omega^1_{K/C} -> Omega^1_{L/C} is an isomorphism for separable algebraic L/K, hence Omega^1_{L/C} = L dr + L ds and Omega^2_{L/C} = L omega. Concretely, the derivations d_r, d_s of K (defined through the finite separable extension K/C(r,s)) extend uniquely to L and are the coefficient derivations of d on L. Tr(a dr + b ds) := Tr(a) dr + Tr(b) ds and Tr(a omega) := Tr(a) omega are well defined and K-linear.

Trace commutes with derivations, non-Galois case included (attacked as requested): let N be a normal closure of L/K and D_N the unique extension to N of D in {d_r, d_s}. For sigma in Gal(N/K), sigma D_N sigma^-1 is a derivation of N extending D, so it equals D_N: D_N commutes with every sigma. Every K-embedding tau: L -> N is the restriction of some sigma, and D_N restricted to L is the unique extension D_L (uniqueness of extension into the L-module N). Hence D_N(tau a) = tau(D_L a), and summing over the n = [L:K] embeddings gives D(Tr a) = Tr(D_L a). No Galois hypothesis on L/K and no ramification hypothesis is used: the trace is a field-theoretic construction on L tensor Omega_K that never looks at a place, so ramification over the boundary at P is irrelevant. Then for eta = a dr + b ds in Omega^1_{L/C}, Tr(d eta) = (Tr d_r b - Tr d_s a) dr wedge ds = (d_r Tr b - d_s Tr a) dr wedge ds = d(Tr eta). CONFIRMED.

Descent: if 1 tensor omega = d eta in L, then n omega = Tr(1 tensor omega) = Tr(d eta) = d(Tr eta) with Tr eta in Omega^1_{K/C}; n is a nonzero element of C (characteristic zero, attacked as requested), so omega = d(Tr eta / n) is exact in K, contradicting Item 3. Nonexact after EVERY finite extension. CONFIRMED.

Dominance supplies a finite extension (attacked as requested): a dominant rational phi: A^2 --> S gives an injective C-algebra map phi^*: K -> L = C(u,v). L is finitely generated over C, hence over K, and trdeg_C L = 2 = trdeg_C K, so L/K is algebraic and finitely generated, hence finite, of degree deg(phi) >= 1 (degree 1, birational, included). Pullback of rational forms is the map Omega_{K/C} -> Omega_{L/C} induced by phi^*. Consequence 1: c du wedge dv = d(c u dv) is exact in Omega^2_{L/C}, while phi^* omega is not; so no such phi exists for any nonzero constant c and any finite source degree. CONFIRMED.

Consequence 2: df wedge dg = d(f dg) is exact in Omega^2_{K/C} already, so df wedge dg = c omega with c a nonzero constant is impossible directly from Item 3; Item 4 is not needed, as the producer says. Poisson translation: Omega^2_{K/C} = K omega, so df wedge dg = P(f,g) omega defines a biderivation P on K with P(x,y) = f_z = 2z + xy - C and, from dz = -(f_x dx + f_y dy)/f_z, P(y,z) = f_x = 2x + yz - A and P(z,x) = f_y = 2y + xz - B. A biderivation of K is determined by its values on the generators x, y, z, so P is the bracket the producer names. Hence no rational pair, a fortiori no regular pair, has nonzero constant bracket. CONFIRMED, with one wording remark: the producer displays only {x,y}; the identity forces the other two generator brackets as above, and a convention with the same {x,y} but different {y,z}, {z,x} would not satisfy df wedge dg = {f,g} omega. This is a remark, not a gap.

## Item 5. Exact scope, controls and absence of a general JC2 conclusion: CONFIRMED

Controls, recomputed:
- Identity of A^2: du wedge dv = d(u dv) is exact and the residue detector returns 0 on it. Correct, though weak as a control: it is a tautology of exactness, not a test of the detector's discriminating power.
- Degree-two rational map (u,v) -> (X,Y) = (u^2, v/(2u)): dX = 2u du and dY = dv/(2u) - v du/(2u^2), so dX wedge dY = du wedge dv exactly. Generic fibre {(u,v), (-u,-v)}, degree 2, dominant, with a pole along u = 0, not a polynomial map, hence not a Keller map. It shows that finite degree greater than one is not by itself the obstruction; nonexactness of the fixed target form is. CONFIRMED.
- Cayley specialization: covered under Item 2; residue 1 with real affine nodes present. No generic-smoothness or generic-parameter assumption appears anywhere in Sections 1-4. CONFIRMED.

Scope statements checked against the proof:
- The obstruction is specific to the FIXED form omega and a CONSTANT multiplier. A pullback equal to h du wedge dv with h nonconstant is untouched, since h du wedge dv need not be exact. A nonconstant rescaling of omega is untouched. Analytic Darboux charts are untouched, not being finite rational extensions of K. Maps between two character surfaces preserving their nonexact forms up to constants are untouched, both sides being nonexact. All four disclaimers are correct and necessary.
- No Keller-source landing theorem, no global properness result, no JC2 proof or counterexample: a Keller map is a polynomial self-map of the plane, not a map to S, and nothing in Sections 1-4 speaks to it. The producer's own text says so. CONFIRMED that no general JC2 conclusion is drawn or implied.
- The paper 1011.6036v2 is used only for the family and bracket display; every step I checked stands on the self-contained algebra. I did not retrieve the paper and did not verify the equation numbers (2.3), (2.5), (2.9)-(2.10) or the parameter dictionary (u1,u2,u3,u0) = (A,B,C,-D). That citation mapping is NOT CHECKED here and affects no verdict.
- The producer's OPENS RAISED is empty; consistent with the report content. No quantifier was silently weakened and no generic smoothness was imposed anywhere in the producer text.

## Attacks attempted and outcome

1. Discriminant square, rational versus polynomial: closed by UFD / integral closure. No loophole.
2. Special parameters making f reducible: impossible; the x^2 coefficient -4 of Delta is parameter-free.
3. P singular or off the closure at special parameters: impossible; G(P) = 0 and F_w(P) = 1 identically.
4. Sign error in (3): rechecked directly and by Poincare residue; consistent.
5. Embedding K into E through completion: Krull injectivity plus C[[r,s]] a domain; valid.
6. Iterated Laurent ordering: either order works; residue extraction well defined; (4) holds in both.
7. Primitive with arbitrary poles, including along r = 0, s = 0, or through P: covered because (4) holds on all of E.
8. Abstract Kahler differentials of E versus the coordinate complex: not conflated; the chain map targets the coordinate complex and is defined through the universal property of Omega_{K/C} only.
9. Characteristic-zero trace: n = [L:K] is invertible in C; separability is automatic.
10. Non-Galois L/K: handled by the normal closure. Ramified L/K: irrelevant to a purely field-theoretic trace.
11. Dominance to finiteness: finitely generated plus equal transcendence degree; valid, degree 1 included.
12. Degree-two Euclidean control: pullback is exactly du wedge dv; valid.
13. Silent quantifier weakening or imposed generic smoothness: none found; every producer step is stated for all parameters.

None of the attacks produced a REFUTED or a GAP.

## Adapter, identity and process limits

- Requested adapter model=fable, effort=max; the harness reports claude-fable-5-1. The hosted identity is not independently exposed; the different-model status relative to the producer is asserted by the harness, not verified by me.
- This is a manual hand recomputation. No CAS, script, enumeration, network, AWS or provider call was made. No Git mutation, no shared edits, no descendants, no new OPEN or successor proposal, no artifact_finalize, no seal.py.
- Supervisor cap 1200 s from launch; startup 20:14:27Z; draft 20:19Z; final text about 20:24Z.
- Outputs written: FABLE-STARTUP.md (0444) and this report only. The 1667-byte draft of this file was replaced by delete-and-add through apply_patch; no other file was touched.

## Recommendation (non-binding)

All five exact claims CONFIRMED at the stated scope. This review is the different-model hostile review the producer's lifecycle line requested; promotion is HQ's decision, not this reviewer's.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — this review raises no `OPEN[...]` entries, so there is nothing to collide. The collision scanner was not executed under the read-only shell constraint; the block is written by hand in the scanner's format.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20520`.
- Body SHA-256:
  `c068bcfb0185d58e0d85f0c431d29d97f84d816f904b538a18104ada39f5a550`.
- Frozen basis: `846870e462d1e7bef517852a8a1dbec5e4a25700`.
