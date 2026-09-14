# D108 Euler envelope and final case-composition gate (Fable 5.1, 2026-09-06)

Independent gate of `xmodel/d108-upper-envelope-euler-astra-20260906.md` (SHA256 `08d3fa09506b412dcbddeabb24d70da0f266b90174615cf39013a4311ecabd75`, PROVISIONAL) composed with the earlier case producer (`528d745f...`) and my earlier gate (`7c6a045b...`). All 14 charged inputs were hash-verified against the lane list. Scope: one bounded mathematical review of the primary statements plus a tiny exact control run. No CAS, solver, AWS action, ledger/tool/adapter edit, live peer report, external post, giant-certificate replay, or jc2-lean access. Own scratch only: `/tmp/fable5-euler-gate/`.

**Headline.** The new argument is sound at the published-statement interface. Its one external ingredient, GGV1 Theorem 2.6 together with Remark 2.5, is used with every antecedent verified; the elementary steps (max-ratio direction, polynomial Euler support, st-endpoint comparison, the vertical ODE with b > a, the common translation) all check against the primary text. (U) is therefore discharged for every characteristic-zero Keller specialization of the frozen source, after one Jacobian-one translation that preserves all published case data. Composed with the earlier confirmed standard (3,2)-pair and the chain ((8,28),(1,0)) -> (11/4,7), every source-level antecedent of GGHV Proposition 4.3 is now met. What remains is proof-replay debt inside external theorems and the external certificates' reduction/transcription scope, not a missing arrow at the source. The family retirement is CONFIRMED as a conditional result at the externally trusted tier only.

## 1. Verdict table

| Item | Verdict | Basis |
|---|---|---|
| Euler envelope: deg_B F = 84, deg_B G = 56, ell_(0,1)F = (A+s)^24 B^84 | CONFIRMED (EXTERNAL-THEOREM GGV1 Thm 2.6(1),(2) + Remark 2.5) | §2 below; all antecedents of Thm 2.6 verified from its statement |
| Common power normalization: same s for G, tau = (A-s,B) preserves leaders and (4,-1) faces | CONFIRMED | Prop 1.13 top-weight cancellation, elementary; §3 |
| Full case interface: all Prop 4.3 normalization/vertex antecedents | CONFIRMED at the published-statement interface, with (U) discharged | §4; remaining items are internal proof-replay debts, listed |
| Conditional family retirement of the D108 physical-Keller source | CONFIRMED as CONDITIONAL (external theorems + retained Helali/Suzuki exclusions at CROSSCHECK scope) | §5 |

No genuine source-level arrow remains. The precise residual debts are named in §4.3 and §6; none is a hypothesis the source must supply.

## 2. Euler envelope: independent review against GGV1

Read whole: GGV1 §1 (Defs 1.1-1.5, Notation 1.6, Remarks 1.7-1.9, Notation 1.10, Prop 1.13), Lemma 2.2, Props 2.3-2.4, Remark 2.5 with note [4], Theorem 2.6 with proof and note [5], Remark 2.7, Prop 4.7 with note [14], Cor 5.21. K is a field of characteristic zero (p.1); no algebraic closure is needed for Thm 2.6.

- **Direction.** V requires only gcd = 1, and V_{>0} only rho + sigma > 0. Both (0,1) and the max-ratio direction (rho,sigma) with 0 < rho < sigma lie in V_{>0}; rho > 0 is needed only for V_0 (Prop 2.11), which the producer does not use. Note [14] applies Thm 2.6 at (1,0) in the same way. CONFIRMED.
- **Max-ratio exposed normal.** For a support point (i,j) with j > b, unique total leader gives i + j < a + b, so i < a and 0 < (j-b)/(a-i) < 1. With rho/sigma the maximum in lowest terms, I re-derived the three dominance cases: points with i <= a, j <= b trivially; points with i > a have j < b and rho(i-a) < rho(b-j) < sigma(b-j); points with j > b by maximality. So the face is exposed, nonmonomial, contains (a,b), and its other points have smaller i and larger j. CONFIRMED.
- **st rather than en.** By Remark 1.8, for a direction in V_{>0} st is the face point maximizing i - j, so st(P) = (a,b). Remark 1.7's cross-product test agrees: the face vector is a positive multiple of (-sigma,rho) and (rho,sigma) x (-sigma,rho) = rho^2 + sigma^2 > 0. CONFIRMED.
- **Polynomial E support.** Thm 2.6(1) gives F in L = K[x,y] when P,Q are polynomials. A monomial A^u B^v of weight rho + sigma with sigma > rho has v <= 1, giving support in {(1,1),(1+sigma/rho,0)}. If F were a monomial, Remark 2.5 (its note [4] proof is elementary and I checked it) would force ell P monomial since rho + sigma > 0. So both points occur, rho = 1, st(F) = (1+sigma,0) != (1,1), and Thm 2.6(2) forces (a,b) ~ (1+sigma,0), i.e. b = 0. Contradiction. The polynomiality clause (1) is load-bearing: in L^(1) negative u would admit more support. CONFIRMED.
- **b > a coefficient argument.** With E = e(A)B, the GGV1 bracket det J gives b e'p - e p' = p exactly. For deg e = r >= 2 the leading coefficient is lc(e) c (br - a) != 0 because br >= 2b > a, at degree a + r - 1 > a; for r = 0 the left side has degree a - 1 (char 0). So e = alpha A + beta with alpha = 1/(b-a), and (A+s)p' = a p forces p = c(A+s)^a by coefficient comparison over K itself. My own changed object shows the hypothesis is load-bearing: at (a,b) = (4,2) the same ODE has the solution e = A^2 + A, p = A(A+1)^3, which is not a shifted power (§7). Both source applications have b > a (84 > 24, 56 > 16). CONFIRMED.
- **Finite checks.** The producer's twelve controls are arithmetic instances at s = 7/5; they do not prove the lemma and the report does not claim they do. The proof is the theorem-based argument above, valid for every K-valued specialization.

Upstream proof debt, separated from antecedents: the existence of the Euler element and its polynomiality clause rest on [8, Lemma 2.2] as cited in the proof of Thm 2.6; statement (2) follows from Prop 2.4, whose proof I read. None of this is a hypothesis about the source.

## 3. Common power normalization and face preservation

- **Same translation for G.** The lemma applies to G directly (b = 56 > a = 16 > 0), so ell_(0,1)G = q(A)B^56 with deg q = 16 and leader 1. Prop 1.13 gives v_(0,1)([F,G]) = 139 unless [ell_(0,1)F, ell_(0,1)G] = 0; since [F,G] is a nonzero constant of weight 0, the top part vanishes: 56 p'q - 84 p q' = 0. With p = (A+s)^24, cancelling (A+s)^23 in the polynomial ring gives (A+s)q' = 16 q, hence q = (A+s)^16. The root is common, not independently chosen. CONFIRMED.
- **tau(A) = A - s, tau(B) = B.** Jacobian one, so (tau F, tau G) is Keller with the same bracket. Each replacement of A^i B^j has A-exponent k <= i, total degree k + j, and (4,-1)-weight 4k - j, both strictly smaller unless k = i. So the unique total leaders A^24 B^84 / A^16 B^56, the unique highest-A monomials, the complete (4,-1) faces [A(AB^4-1)^7]^3 and its square with all numeric coefficients, and the B-degrees 84/56 are unchanged, while ell_(0,1) becomes the monomials A^24 B^84 and A^16 B^56. This is exactly (U). In source coordinates tau is X -> X - s, W -> W. CONFIRMED.
- **Gauge.** tau need not respect the optional source coefficient gauges (e.g. any fixed low-order X-coefficient); the published case data used downstream are the faces, endpoints, degrees, ratios, and Keller-ness, all preserved. No unit certificate for the ambient ideal is implied and none is claimed.

## 4. Full case interface: composing with the confirmed pair and chain

### 4.1 What the earlier gate established and what (U) adds

The earlier gate confirmed, specialization-independently: (tau F, tau G) is a standard (3,2)-pair in L (GGV1 Def 4.3 literally), the starting corner ((8,28),(4,-1)) is regular of type II.b, there is no edge between (1,0) and (4,-1), and [5] Theorem 2.20 (quantified over every standard pair, no minimality) forces l1 = 4, A1 = (11/4,7), a type I final corner, i.e. the [5] §6 row (8,28),(11/4,7),(3,2),108. All of that uses only faces that tau preserves, so it holds for the translated pair. Cor 5.21(3), st_(1,1) = en_(1,0), is literal.

(U) now gives, in GGHV's swapped coordinates P(x,y) = tau F(y,x): deg_x P = 84 attained only at (84,24), and deg_y P = 24 attained only there (source bound). Consequences I re-derived from the definitions:

- Every direction strictly between (1,0) and (-1,4) is a positive combination alpha(1,0) + beta(-1,4), and alpha i + beta(4j - i) <= 84 alpha + 12 beta with equality only at (84,24), using i <= 84 and 4j - i <= 12 (source (4,-1) bound). So Dir(P) meets [(1,0),(-1,4)[ nowhere, Succ_P(1,0) = (-1,4), and Pred_P(-1,4) = Pred_P(1,0) =: (rho,sigma).
- (rho,sigma) > (0,-1) because (0,3) lies in Supp P below y = 24, so (84,24) is not a y-minimizer; (rho,sigma) < (1,0) because (1,0) lies in the normal cone of the vertex. [2] Prop 2.1 (Jacobian pair in L, edge ending at (a',b') = (84,24) with 84 > 24 > 0, direction in ](0,-1),(1,0)[; proof read, it uses Thm 2.6 and [2] Cor 1.6 "no edge of slope 1") then gives (rho,sigma) < (1,-1). So the membership is in the OPEN interval ](0,-1),(1,-1)[, as [2] Prop 3.12 requires; GGHV's printed "]" is weaker than what holds.
- In original orientation this is exactly Cor 5.21(4), (-1,1) < Succ(1,0) < (-1,0), for both F and G (G by the same argument with (56,16)). So the standing normalization of [2] §2, [5] §2 and GGHV §2 is met without invoking GGV1 Prop 4.7 or van den Essen 10.2.21.

### 4.2 Remaining Proposition 4.3 antecedents, checked one by one

Read: GGV1 Prop 7.3 / Cor 7.4 statements, Thm 7.6 statement, Prop 8.2 statement; [2] Prop 2.1 with proof, Prop 2.2 with proof, Cor 1.6 statement, the §2 standing assumption; [6] (2.1), (2.2), Prop 2.5 statement; GGHV Prop 4.3 whole proof.

| Antecedent in the proof | Status for the translated source pair |
|---|---|
| Cor 7.4: m,n coprime > 1; [P,Q] in K^x; v_(1,1) and v_(0,1) ratios both m/n | (3,2); 108/72 and 24/16 (swapped v_(0,1) = original A-degree) = 3/2. Met. |
| Cor 7.4 (1)-(3) at (rho0,sigma0) = (-1,4): in Dir(P), v(P) = 12 > 0; (1/3)st(P) = (1/2)st(Q) = (28,8) in Z x N; b = 8 < a/l = 28 | Met by the fixed face; st in GGV1's counterclockwise convention is the vertex (84,24). GGHV write "en" for it; a labelling drift, not a hypothesis. |
| st(F) = (p/q)(28,8) with q = 4, i.e. the Euler element at (-1,4) does not start at (1,1) | GGV1 Thm 7.6(3), valid for j = 0 when A0 is type II (confirmed II.b). Then v(F) = 3 forces p/q = 3/4. EXTERNAL-THEOREM, antecedent met. |
| Range: (rho~,sigma~) <= Pred, i.e. v_e(P) > 0 for all e in [Pred,(-1,4)] | Reduces to v_Pred(P) > 0 since the vertex is the whole face in between. [2] Prop 2.2 (standing assumption: (m,n)-pair in L, direction in ](0,-1),(1,-1)[, (a,b) = (28,8) with a > b > 0, all met) gives it via van den Essen Thm 10.2.6 (a pure x-power term). EXTERNAL-THEOREM; the earlier gate's J = 0 control shows edge data alone do not give it. |
| Existence of G with [R,G] = R^i at Pred (Pred has rho + sigma < 0, so Thm 2.6 itself does not apply there) | [2] §2 constructions under the same standing assumption. EXTERNAL-THEOREM, antecedent met. |
| [6] Prop 2.5: a/l = 7 > 2, b = 2, direction in the open interval, (2.1) with d in {0,1} | en(R) = (84,24)/12 = (7,2). d in {0,1}: st(R) = (1/12)st(P) is a lattice point with y = 12d, and the edge's lower endpoint has y < 24 because x0 < 84 (envelope), so d <= 1. The single-root alternative to (2.2) is GGHV's own (1,-2) branch via [2] Prop 3.12. Met. |
| Later steps: Laurent shifts y -> y + lambda x^(-k), "as in Prop 4.1" vertex analysis, GGV1 Prop 8.2 (hypotheses: direction in V_{>0} with rho1 < 0, P,Q in L^(1) Keller, (1/m)en = (1/n)en = (a,b) with a > b, m != n coprime; no minimality), the final inversion to bracket x^2 and the two polygons | Internal to the external proof; no further source-level datum enters. The two literal outcomes (1) five-vertex and (2) four-vertex with [P,Q] = x^2 are the ones transcribed in CROSSCHECK. |

Minimality (Cor 5.21(2)) appears in none of these statements; the degrees 108 and 72 make the pair a counterexample rather than an automorphism (Abhyankar-Moh, external), which is the only sense of "counterexample" the proof uses.

### 4.3 Decision

(U) was the last missing source-level arrow. After it, every antecedent of Prop 4.3 that refers to the source is verified from the preserved faces, the Keller hypothesis, and the envelope. The residual items are proof-replay debts of external results, not hypotheses: [8, Lemma 2.2] behind Thm 2.6(1); Thm 7.6(3); the "mimic" proofs of Prop 7.3 / Cor 7.4; [2] Cor 1.6 and the 10.2.6 / 10.2.1 citations inside Prop 2.2; the [2] §2 G-construction; [2] Prop 3.12 and [6] Prop 2.5; GGHV's Prop 4.1-style vertex analysis and Prop 8.2 use. None was reproved here and none is claimed.

## 5. Conditional family retirement

CROSSCHECK was read whole (SHA256 `70bc10f8...`). It records exact three-way agreement on both Prop 4.3 polygon systems, bracket convention P_x Q_y - P_y Q_x with right side x^2, lattice supports 25+47 and 61+125, and subcase numbering; Helali's replay PASS with three coverage gaps closed by the auditor; Suzuki's static and full regeneration PASS with the F_23-only lower descent covered by an on-paper lifting lemma; both certify both subcases. I accept these only at that historical audited reduction/transcription scope. No archive was fetched or replayed here, and the superseded internal msolve/cCa header claims stay superseded.

The usable chain is now: D108 physical Keller point over a characteristic-zero field -> (tau) standard (3,2)-pair with the row chain [proved, specialization-independent] -> envelope (U) [proved from Thm 2.6] -> Prop 4.3 antecedents all met [§4] -> one of the two literal polygon systems with bracket x^2 [EXTERNAL-THEOREM] -> contradiction [retained external exclusions]. Hence the literal D108 full-physical-Jacobian source family is retired as a characteristic-zero counterexample search, CONDITIONAL on the named external theorems and certificates. Not implied and not asserted: a universal degree >= 125 bound, a subset unit or full internal certificate, source necessity, or an explicit coefficientwise cut map from source parameters to the polygon systems.

## 6. Boundaries

- Not independently reproved: [8, Lemma 2.2]; GGV1 Thm 7.6, Prop 7.3 / Cor 7.4, Prop 8.2 proofs; [2] Thm 1.5 / Cor 1.6, Prop 2.2's van den Essen citations, §2 constructions, Prop 3.12 proof; [6] Prop 2.5 proof; GGHV Prop 4.1 and the interior of Prop 4.3; the Helali/Suzuki certificates and their dependencies. The earlier gate's J = 0 control remains the reason the Cor 7.4 range must go through Prop 2.2 rather than edge data.
- The st/en labelling drift between GGHV's text and GGV1's Notation 1.6 changes no mathematics: the shared vertex is (84,24) either way.
- Nothing here touches the launcher, validator, adapters, FALLACY-v2, ledgers, or any prior artifact. No expensive membership job was commissioned; elementary theorem reasoning sufficed. No exit-price assertion is made, so no basis declaration is due.

## 7. Controls and custody

All runs read-only, stdlib only, under 30 s and 512 MiB address-space caps, in `/tmp/fable5-euler-gate/`.

- Supplied checker, read in full before execution, copied as `check_copy.py` (SHA256 `d169f48554949d6660cb1749725913e5a28adbfadba0ab2fb782b8a5f37789a3`, equal to the charged `check.py`). `python3` and `python3 -O` each printed twelve PASS lines and `ALL_EXACT_CONTROLS_PASS`, exit 0; the two outputs are byte-identical, SHA256 `6f3f68ea6971c95dcc09e20e8267eae77268e8d6a3e942f57e291af465a91d2d`; 0.03 s / 12 MB and 0.09 s / 17 MB peak. Its checks use raised exceptions, so -O does not erase them.
- Own changed-object script `changed_object.py` (SHA256 `8bab78ad329e98fd6926669febafdbbbe408a8c4bd5030f493d6fd3ec6034d6d`), output `co.out` (SHA256 `146418feabaad8e05fcbf67811bb454df291c9abce94334f0f7b6e8a78ad3ac6`), 0.02 s / 12 MB, fifteen PASS lines and `FABLE5_CHANGED_OBJECT_CONTROLS_PASS`. It verifies: the b < a counterobject e = A^2 + A, p = A(A+1)^3 solves the vertical ODE at (a,b) = (4,2) and is not a shifted power; the b > a leading coefficient lc(e) c (br - a) at (24,84) for r = 2, 3; on a changed support with leader (5,7) the max-ratio direction (3,5), exposedness, st = (a,b), and the monomial-E Remark 2.5 kill; on a rho = 1 support the E-support {(1,1),(3,0)}, st(E) = (3,0) and non-alignment with (a,b); and the envelope-derived bound d <= 1 for the predecessor edge.

The lane inputs were read from `/tmp/jc2-lane.UFXBLF/inputs`; their SHA256 values match the charged list, including the source JSONs (`0bc1b54f...`, `1c927d83...`), whose face data were consumed only through the earlier gate's confirmed parse.

<!-- BODY-END -->
