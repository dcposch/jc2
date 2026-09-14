# Gate: D108 literal source → GGHV interface (targeted independent, Fable 5.1)

Gate of `xmodel/d108-source-frontier-interface-astra-20260906.md` (SHA `39bbe041…21ce7`). Lifecycle: **GATE-CHECKED / PROVISIONAL**. No mathematical point, properness, source-configuration exclusion, or JC2 claim is made or assumed. No AWS, no heavy CAS, no jc2-lean, no shared-ledger or source write, no live peer report or log read.

## Inputs and replay

All 16 charged inputs hash-match `charged-inputs.list` (source `1c927d83…a10814`, GGHV PDF/txt `ac18e80c…80bd` / `f3eca2a5…2368`, GGV1 txt `e3694dde…e37b1`). Replays ran on my own scratch mirror of the repo layout, each capped at 30 s / 512 MiB:

| Replay | Result |
|---|---|
| `edge_interface.py --verify` | PASS, 0.39 s |
| `map_controls.py --verify` | PASS, 12.0 s, 64.9 MB; all six producer mutations rejected |
| `critical_jet.py` on own copy | regenerated JSON byte-identical to the charged `critical_jet.json` |
| `inspect_source.py --verify` | exit 1 on the mirror; the only differing keys are `source_path` (recorded as the repo absolute path) and the excluded timing keys |

The inspect failure is a harness relocatability defect, not a mathematical one: the recorded `source_path` is compared literally. Root's in-place PASS at 12:59:48 is consistent with this. Fix: exclude `source_path` from the comparison or record it relative to the repo.

## Independent mutations (raw source JSON, not `source_interface.json`)

Own script `gate_mut.py`, 0.94 s, from the frozen input file: h/D/C X-degree max 8 each; weight `4X−W` max exactly 4 each; total degrees 36/37/38; C has no W^36 slot and its degree-36 W exponents are 28…35; the unique X^8 slot of h is (8,28) with coefficient 1; the eight weight-4 rows of h are parameter-free and sum to `X(XW^4−1)^7`; lines `h=η−X`, `D=d1X+d0`, `C=βX+γ` with the producer's β; G line monic quadratic; 14 residuals over 30 names with no C name and no B2c name; γ occurs only in C's (0,0) slot; `h(−B,B)` has ambient B-degree 33 with leading L and residual 0 equals L² exactly.

Euler auxiliary: `J(E,H)=H` and `J(E/3,H³)=H³` recomputed; a perturbed E coefficient and the root α=2 both fail. Map: the explicit five-step composition (A=X+W, B=W; swap; three Laurent shears; inversion x→x^−1, y→x^4 y) equals the producer's T on X, W, XW²; on the non-trivial Keller control `F=X+W³, G=W+(X+W³)²` (j=1) the ordered pair `P=T(G), Q=−T(F)/j` has bracket exactly x². Terminal polygon maps `(i,j)→(4j−i,j)` reproduce both GGHV vertex sets and the case-(c) extras (0,8),(0,12). Δ re-derived as `−J(h,D)(x*,0)` with `x*=η−b/6−d1/2`, monic in `B2c_70_1`, which is absent from all residuals.

## Verdicts per claim

- **Literal source h36/D37/C38, 192 free C, 14 ordered residuals C-independent, rings and exponent normalization: CONFIRMED.**
- **G line monic quadratic; C line image span{1,X} of rank 2: CONFIRMED.**
- **Full-C rank 191 at every characteristic-zero field point: CONFIRMED** as an argument. Re-derived: `J(P,G)=0` with P nonconstant forces `G=φ(R)`; the monic quadratic line gives deg φ ∈ {1,2}; degree 1 needs deg R=72 > 38; degree 2 gives deg R=36, `R_top` a scalar multiple of `(X+W)^8W^28`, whose W^36 term has no slot in V_C. Rank is field-extension invariant, so passing to a closure for the square root is harmless.
- **Abstract W190 constant pivots over any Q-algebra: CONFIRMED.** In the echelon basis of V0 ordered by W-order ascending then X-degree descending, the slot (i+1,r−1) of `J(P,G)` receives contributions only from monomials of P at W-order < r, or at W-order r with X-degree i or i+1; all of these precede the leader `X^iW^r` and vanish except the leader itself, where only the monic X² of G(X,0) contributes, giving −2r. Later columns have no such monomials, and the pivot rows are injective in (i,r). This is a constructed 190-minor with constant diagonal. It is **not** the same object as the Keller-localized pivot of the transverse-critical-unit report (its determinant `det(M)·Δ`, entries over the base, line 40); I did not conflate them, and full-C rank over a nonreduced base is not claimed by either.
- **Rowless γ: CONFIRMED for the raw physical Jacobian plus the 14 residuals only.** J kills constants and γ is absent from the residuals. T2/T3 characteristic rows are out of scope, as the producer states.
- **Standard (3,2)-pair in the literal GGV1 Definition 4.3 sense at every Keller point: CONFIRMED.** In (A,B): `v_{1,1}` ratio 108/72, `v_{1,0}` ratio 24/16, `ℓ_{1,0}(F)=A^24B^84` is a monomial so st=en=(24,84) with `v_{1,−1}=−60<0`; m=3, n=2 coprime and >1; F,G ∈ K[A,B]. Needs only the unique X^8 slot and X-degree ≤ 8 of D, C.
- **Full (4,−1) edge `[A(AB^4−1)^7]^3`, `[…]^2`, and q=4 auxiliary: CONFIRMED.** Weights 12 vs ≤ 8 (Dh) and ≤ 4 (C). E has weight 3 = ρ+σ. Uniqueness of the Theorem 2.6 element follows from GGV1 Proposition 2.11(5) via **s>0** (the face carries y³ resp. y²); the producer's "multiple distinct factors" clause is not the operative one since p=(z−1)^7 has one factor. Wording correction only.
- **Cor 7.4 literal hypotheses at (ρ0,σ0)=(−1,4): CONFIRMED** in GGV1's convention: (−1,4)∈Dir(F), v=12>0; `(1/3)st(F)=(1/2)st(G)=(28,8)∈Z×N` (Notation 1.6/Remark 1.7 cross-product test gives st=(84,24), en=(0,3)); b=8<a=28; `st_{−1,4}(E)=(21,6)=(3/4)(28,8)`, q=4. GGHV's "en=(21,6)" is GGV1's st; GGHV line 166 says it uses the opposite direction order.
- **Partial Laurent map with Jacobian x² and ordered `P=T(G), Q=−T(F)/j`: CONFIRMED** (independent control and explicit composition). The j-inverse is Keller-locus only; not a gauge.
- **Two terminal polygon maps: CONFIRMED as vertex arithmetic. Whole upper/lower support transport and exhaustive cut transport: NOT checked, GAP** as declared. No coefficient function ℓ2/ℓ3 was checked by anyone.
- **Δ formula, `B2c_70_1` linearity and independence; "Δ ∈ (residuals14) iff 1 ∈ (residuals14)": CONFIRMED** (the ring endomorphism fixing all residual generators and sending `B2c_70_1` to `1−(Δ−B2c_70_1)` maps Δ to 1). **Does not prove the 14-ideal proper: CONFIRMED as stated.** The residual-0 = L² square is kept as a square; radical/nilpotent distinction untouched.

## Adversarial scope question: is GGV-CUT-EXHAUSTIVENESS a genuine interface?

Verdict: **typed OPEN, of kind UNREAD-DEPENDENCY, not a new mathematical obstruction and not yet a discharged citation.**

Read exactly: GGHV Proposition 4.3's hypothesis is "a counterexample in the case (8,28)", where the case is a row of the §2 table taken from the family tables of [5, §§5–6] with invariants A0=(8,28), (m,n)=(3,2), max degree 108. The proof then (i) *proves* the corner set {(0,0),(1,0),(8,28),(0,4)}·(m,n) using [1, Cor 7.4] at (−1,4) with q=4, the setting of [2, Prop 3.12], and [6, Prop 2.5] ⇒ Pred_P(1,0)∈{(1,−2),(1,−3)}; (ii) does the x^−2/x^−3 cut case split (one or two linear factors) to reach cases a/b/c; (iii) cuts the fixed edge at α; (iv) analyses the opposite vertex "as in Proposition 4.1" to get Succ=(−2,7); (v) applies [1, Prop 8.2] (hypotheses verifiable: ρ1<0, a=24>b=7, m≠n coprime) to get k=1; (vi) inverts.

What the literal D108 data supply: the row invariants, the Definition 4.3 standard-pair conditions, and the verifiable hypotheses of Cor 7.4 and of Prop 8.2's statement. What they do not supply, and what the charged inputs cannot decide: whether "case (8,28)" as defined in [5] carries the minimal-pair hypothesis (B = gcd over all counterexamples; the D108 pair has gcd 36 and minimality is unknowable) or extra corner/A1 data; the hypotheses of [2, Prop 3.12] and [6, Prop 2.5]; and the lower-side positivity (ρ̃,σ̃) ≤ Pred_P(−1,4) that Cor 7.4 needs to reach the predecessor edge. GGHV Prop 4.3 itself never mentions minimality, so the conditional implication "row invariants ⇒ polygon (1) or (2)" may be exactly published; but confirming it is a reading of [2], [5], [6], which are absent. Hence the producer's naming is right in substance: the interface is a citation-hypothesis check, not a proof obligation for a new theorem. **First missing arrow:** the literal definition of the (8,28) row in [5, §5] (which invariants define membership, and whether minimality is required) together with the statements of [2, Prop 3.12] and [6, Prop 2.5].

Old exact-Q/msolve closures of the two explicit GGHV systems are history in the producer and are not re-promoted here.

## Cheap next tests

1. Reading only, ≤30 min, no CAS: obtain [5] and [2], transcribe the (8,28) row definition and Prop 3.12 / [6] Prop 2.5 hypotheses, and tick each against the CONFIRMED list above.
2. Fix the `source_path` comparison in `inspect_source.py --verify` so the replay is relocatable.

**One bounded follow-up proposal (no point, properness, or case closure assumed):** GGHV's proved corner (0,4)·3=(0,12) forces `deg_B F(0,B) ≤ 12`, hence the coefficients of `h(−B,B)` at B-degrees 13…33 must vanish at any Keller point of the source that is in case (8,28). Test radical membership of each of those 21 coefficients in the 14-residual ideal (30 names) by Rabinowitsch, one coefficient per process, 60 s / 512 MiB each. Any non-member is a literal interface mismatch on the generic residual-locus point; membership of all is consistency only, never attainment.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line, including its terminating newline; this seal is outside the body.
- Body bytes: `9441`.
- Body SHA-256: `e5f09997493d1e71ce862a43e84d464ea9232cb8e10ccdbb32cc2761108857f5`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
- Own scratch: `/tmp/fable-gate-scratch-315399` (gate_mut.py, mirrored replays); no repo file other than this report was written.
