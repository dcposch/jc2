# D108 published-case interface gate (Fable 5.1, 2026-09-06)

Independent gate of `xmodel/d108-published-case-interface-astra-20260906.md` (SHA256 `528d745faac9de5a7e80a57e534c1f36377eb99b8576c1cfa72894fa3b110a1e`). All 15 charged inputs were hash-verified against the lane list. Scope: one bounded mathematical review. No solver, AWS action, ledger/tool/source edit, certificate download, live peer report, or jc2-lean inspection. Own scratch only: `/tmp/fable5-gate-scratch/envelope.py` (stdlib+SymPy, well under 30 s / 512 MiB), an explicit-root re-implementation, not the producer's `controls.py`.

**Headline.** Arrows (1) and (2) are CONFIRMED: every characteristic-zero Keller specialization of the frozen source is a standard (3,2)-pair whose complete first edge forces the length-one chain ((8,28),(1,0)) -> (11/4,7) of the [5] §6 row, with no global-minimality hypothesis. Arrow (3) is a GAP: the published proof of GGHV Proposition 4.3 uses, beyond the chain data, one normalization inherited from GGV1 Corollary 5.21(4) (via [5] §2 and [2] §2), and for this source that normalization is a statement about the B-degree of F that the packet does not establish. The composition (4) is therefore conditional on that one antecedent plus the retained external exclusions.

## 1. Verdict table

| Claim | Verdict | Basis |
|---|---|---|
| (1) Keller specialization -> standard (3,2)-pair, A0=(8,28), A0'=(1,0), full (4,-1) edge, no intervening edge, type II.b | CONFIRMED | independent parse of h/D/C; GGV1 Def 4.3, Def 5.5, case list before Remark 5.9 |
| (2) chain -> l1=4, A1=(11/4,7) for every root, type I forced, row (8,28),(11/4,7),(3,2),108 | CONFIRMED (EXTERNAL-THEOREM [5] Thm 2.20, GGV1 Prop 5.19) | Thm 2.20 quantifies over each standard pair; minimality enters only the bound on B |
| (3) published Prop 4.3 antecedent satisfied by every Keller specialization | GAP | proof step "Pred_P(-1,4) in ](0,-1),(1,-1)]" needs (U) below, not supplied by support bounds |
| (4) conditional composition to exclusion | CONDITIONAL on (U) and on the retained Helali/Suzuki exclusions as recorded in CROSSCHECK | CROSSCHECK read whole |

First missing arrow: **(U)** "A^24 B^84 is the unique monomial of F of B-exponent 84 and no monomial has B-exponent above 84" (after the harmless A-translation), for every Keller specialization. Nothing in the packet proves it; see §4.

## 2. Arrow (1): literal source to standard pair and full edge

Independently re-derived from the JSON grammar (x = N - r - w is the X-exponent, w the W-exponent):

- h: 185 slots, max X-exponent 8, max(4x-w)=4, degree 36; D: 191 slots, degree 37; C: 197 slots, degree 38; all three have X-exponent <= 8 and 4x-w <= 4.
- The only x=8 slot of h is (8,28) with coefficient 1. The weight-(4,-1) face of h is exactly `X(XW^4-1)^7` with numeric coefficients (checked slot by slot against binomials).
- Under X=A-B, W=B a monomial X^x W^w expands to A^(x-t) B^(w+t) with A-exponent x-t and (4,-1)-weight 4x-w-5t. Both strictly drop for t>=1, so the highest-A slot and the (4,-1) face transfer verbatim to (A,B). Hence ell_(1,0)(F)=A^24 B^84, ell_(1,0)(G)=A^16 B^56, ell_(4,-1)(F)=[A(AB^4-1)^7]^3, ell_(4,-1)(G)=its square, because the D and C corrections have (4,-1)-weight <= 4 and A-degree <= 8, far below 12/8 and 24/16.
- No intervening edge between (1,0) and (4,-1): every monomial satisfies i<=24 and 4i-j<=12 with both equalities only at (24,84), so every positive combination of the two normals exposes that vertex alone.
- With [F,G] in K^x assumed: v11 ratio 108/72 = v10 ratio 24/16 = 3/2, v_(1,-1)(24,84) = -60 < 0 at both st and en of the (1,0) face, F,G in L. This is GGV1 Definition 4.3 literally; standard. The corner ((8,28),(4,-1)) is regular (28 > 8, (4,-1) in Dir(F)), [ell F, ell G]=0, p(z)=(z^4-1)^21 has four factors, v_(1,-1)(st)=v_(1,-1)(3,0)>0: type II.b, hence by GGV1 Remark 6.3 it is the starting triple and t=0 in Theorem 2.20(13).

All of this is specialization-independent because the load-bearing slots are numeric. It asserts nothing about existence of a Keller point.

## 3. Arrow (2): forced chain and type-I endpoint to the published row

Read in full: [5] Theorem 2.20 statement and proof, Prop 2.5, Defs 2.11/2.12/2.18/2.19/2.25, §2.4, §6 tables and Prop 6.1; GGV1 Def 5.5, Remarks 5.8-5.12, Prop 5.13/5.14 statements, Prop 5.19 with proof, Cor 5.21, Def 6.2/Remark 6.3, Thm 7.6, Props 7.3/Cor 7.4.

- Quantifier: Theorem 2.20 reads "For each standard (m,n)-pair (P,Q)". Its proof uses standardness (to get rho_t > 0) and Prop 2.5, whose l=1 branch imports van den Essen 10.2.1/10.2.6 (a pure x-power in Supp P). Global minimality appears only in [5] §2/§3 to bound the invariant B and in Cor 5.21 to produce some minimal standard pair. CONFIRMED: no minimality hypothesis in the chain theorem.
- Successor: Thm 2.20(8) gives l1 = lcm(4,1) = 4 and A1 = (k/(m l),0) + (m_lambda/m)(-sigma/rho,1) = (1,0) + 7(1/4,1) = (11/4,7). All four roots of z^4-1 are simple (discriminant nonzero) and each has multiplicity 21 = 7m in the F face, so the root choice in Prop 2.5(4) cannot change A1; Prop 2.5(4)'s bound b' < (rho a + sigma b l)/(l(rho+sigma)) = 4/3 <= 7 holds. Changed-object control: multiplicity 20 is not divisible by m=3 and the theorem's item (8) does not apply, my own re-implementation rejects it.
- Endpoint: after removing type-III corners (Thm 2.20 proof, finitely many rho|4), Prop 5.19 says a type-II corner at (a/l,b) = (11/4,7) in L^(4) needs gcd(11,7) > 1; it is 1, so the corner is type I with l - a/b = 17/7 > 1, a final corner (Def 2.18). The chain ((8,28),(1,0)) -> (11/4,7) is complete of length 1 and is literally the row (8,28), (11/4,7), (3,2), 108 of the [5] §6 length-one table; the (7/4,3)/(3,4)/144 row and the length-two (8,32)/(8,40) rows are different chains. CONFIRMED. Note that this direction does not need the tables' exhaustiveness at all; only the row's existence.

## 4. Arrow (3): published Proposition 4.3 to the two literal systems

GGHV Prop 4.3's proof (pp. 10-12, read whole) swaps x,y, applies GGV1 Cor 7.4 at (rho0,sigma0)=(-1,4), l=1, (a/l,b)=(28,8), en(F)=(21,6)=(3/4)(28,8) so q=4, and then asserts: "for (rho,sigma)=Pred_P(-1,4) we have (rho,sigma) in ](0,-1),(1,-1)]". Only after that does [2] Prop 3.12 (whose hypothesis is exactly (rho,sigma) in ](0,-1),(1,-1)[) and [6] Prop 2.5 yield Pred_P(1,0) in {(1,-2),(1,-3)} and the three polygons a), b), c).

That membership is not a chain datum. Unswapped it says (24,84) is the unique maximizer of v_(rho,sigma)(F) for every direction strictly between (4,-1) and (-1,1). I checked what it needs. Given the verified facts (A-exponent <= 24 with unique maximum, (4,-1)-weight <= 12), a monomial (i,j) beats (24,84) in some direction between (0,1) and (-1,4) after the swap only if 4j - i > 12 in swapped coordinates, which is excluded; and [2] Prop 2.1 (a general Jacobian-pair statement, no minimality, read with proof) pushes an edge ending at (84,24) with 84 > 24 > 0 from ](0,-1),(1,0)[ down to below (1,-1). So the whole step reduces to exactly one antecedent:

**(U)** deg_B F = 84, attained only at A^24 B^84 (equivalently, after the swap, (84,24) is the unique max-x point so Pred_P(-1,4) < (1,0)).

In the published context (U) is part of the standing normalization: [2] §2 and [5] §2 take (P,Q) "as in [1, Corollary 5.21]", whose item (4) "(−1,1) < Succ_P(1,0) < (−1,0)" is obtained in GGV1 Prop 4.7 by an automorphism (van den Essen 10.2.21 plus a "well known" step), not derived from the (m,n)-pair definition. For the frozen source, (U) is not a support-bound fact: my (A,B) expansion of h has monomials of B-exponent 29..33 with parametric coefficients (the B^33 one is L = -K2c_3_26 + 8 jet0 jet1 - 8 jet2, and residual 0 equals L^2 exactly, as the prior report noted; the B^29..B^32 slots involve K2c_4_25, K2c_4_26, Hc_5_4 and others). So h, and hence F through h^3, has B-degree above 28/84 on the ambient family, and the packet nowhere shows those coefficients vanish at every Keller point.

Verdict GAP, not REFUTED: (U) may well be true on the Keller locus (Abhyankar subrectangularity would give B-exponent <= 84 if the normalizing map of 10.2.21 is affine, since a monomial top form pins the coordinates up to diagonal affine maps; uniqueness of the B^84 term is a further step), but neither the producer nor this gate has proved it, and it is a hypothesis GGHV consume, not an un-reproved internal step. Everything after that step (root cuts, Prop 8.2 use, vertex attainment, the final inversion with bracket x^2, the two polygons, polynomial membership because all lattice points are nonnegative) is accepted as EXTERNAL-THEOREM with the vertex/normalization hypotheses retained, subject to the same proof-replay debts the producer lists. Given (U), the Cor 7.4 lower limit is discharged for the predecessor by [2] Prop 2.2's route through van den Essen 10.2.6 (a pure x-power term gives v_(rho,sigma)(P) > 0 for every rho > 0), which is the same positivity the producer's negative J=0 control shows is not a consequence of edge data alone.

## 5. Arrow (4): conditional composition with retained external exclusions

CROSSCHECK was read whole. What it retains: exact agreement of both Prop 4.3 polygon systems, bracket x^2 and convention P_x Q_y - P_y Q_x, lattice supports (25+47 and 61+125), subcase numbering; Helali replay PASS with three coverage gaps closed by the auditor; Suzuki static and full regeneration PASS with the F_23-only lower descent covered by an on-paper lifting lemma; both certify both subcases; the internal c1/c2 lanes were still pending (superseded msolve/header claims are not revived here). The Helali README snapshot itself conditions the (72,108) conclusion on the published reduction and faithful transcription. So the usable composition is: D108 Keller point -> standard pair with the row chain [proved] -> (U) [open] -> Prop 4.3 polygon pair [external] -> contradiction [external, retained]. No blanket degree >= 125 theorem, source properness, unit certificate, coefficientwise cut map, or JC2 claim follows, and none is asserted.

## 6. Review of the corrections, controls, and replay debts

- Prop 2.11 uniqueness: CONFIRMED in original coordinates. (4,-1) lies in V0 = {rho+sigma>0, rho>0}, p(z)=(z^4-1)^21 has four factors, so item (5) applies before the swap; (-1,4) is outside V0 and the swapped description must not be used. Transport through the swap is a relabeling.
- Cor 7.4 range: CONFIRMED that positivity on the cone (1,-1),(-1,4) (values 60 and 12) does not reach an unknown predecessor; the J=0 control P=H^3+1 with predecessor (2,-7) of value 0 is genuine and not a Keller pair. The producer correctly files this as proof-replay debt; see §4 for how it is discharged once (U) holds.
- Split/single distinction: CONFIRMED. Published [6] Prop 2.5(4) with a=7, l=1 allows Delta in {2,3} and only Delta=3 satisfies a-2Delta | Delta-l, direction (1,-3); the single-root clause of [2] Prop 3.12(1) with l=1 forces rho=1 and 7+2sigma>0, so sigma in {-3,-2}. The arXiv-v2 1.5/2.5 crosswalk file is not among the charged inputs and was not checked.
- Controls: `controls.py` read before anything ran; it locates the repo from its own path and checks the source hash. The producer's six mutations are genuine. My own explicit-root script reproduces the face, the unique x=8 slot, A1, gcd/final-corner arithmetic, the Delta and sigma lists, and adds the multiplicity-20 rejection and the B-exponent envelope above.
- Not independently reproved: Thm 2.20's dependencies in GGV1 §5-7, Prop 5.19's Prop 5.17 machinery, GGHV's Prop 4.1 vertex analysis and Prop 8.2 use, van den Essen 10.2.6/10.2.21, and the external certificates.

## 7. Cheapest discriminator

For (U): expand h(A,B) symbolically (seconds) and test whether every coefficient with B-exponent > 28 lies in the radical of the ideal of the 14 residuals, or more cheaply whether each vanishes at a few exact points of the residual locus. If they all vanish, (U) holds for h and the same check on D and C closes arrow (3) at the published interface; if one survives, the (8,28) case as proved by GGHV does not cover that stratum and a normalization argument (or a direct proof of Succ_F(1,0) > (-1,1) from the Keller equations) is required before Prop 4.3 can be cited.

<!-- BODY-END -->
