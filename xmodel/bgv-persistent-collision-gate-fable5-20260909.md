# FIRST gate: persistent collision lemma and exact generic-projection control

Reviewer: Claude Fable 5.1 (different model from producer Astra). First action 2026-09-09T23:00:43.547Z. Controlling stop: earlier of launch+18 min and 23:19:00Z; root TERM 23:17:00Z; final reserve from 23:15:00Z. No clock reset. FIRST different-model review of the producer's new mathematics only; not a campaign scan and not a 175-page external proof review.

## Custody

Three ordered SHA256 in /tmp/jc2-lane.K9rrnz/inputs matched before any body read:

- `e1e06dd66b0576fa467505b52c55fcb3d7c4a0d803d905bbf13f32fdcded7d9a` xmodel/bgv-one-function-discriminator-astra-20260909.md, WHOLE (11632 B; seal body SHA `7ec892b4…` rechecked on the first 11299 bytes, see box READ-SCOPE).
- `a7a2d635f83a53448642f5f9258fec7967d73d4f8c8f6e70e69b7f2f4bdd638e` box/bgv-one-function-discriminator-astra-20260909/READ-SCOPE.md, WHOLE.
- `07465b6c788a469b0d4e77f8ac2cbf7f6ae23025e6c142fcc741bc66716047b2` box/websweep-20260909T2220Z-astra/bgv-v1.txt, SELECTED lines 5984–6075, 7310–7425, 100–210 only.

Root-side facts taken as given, not verified here: producer writers IDLE 22:49:25.321980825Z; expected artifact transaction `bd9fb0e30befdc3c9ab32e466295e50ec03d3bf175c79069625f089cb6f3a908`. Primary URL https://arxiv.org/pdf/2609.05746v1 is provenance only; not fetched.

## Verdict table

| Item | Verdict | Smallest defect found |
|---|---|---|
| A | CONFIRMED | none |
| B | CONFIRMED | precision only: `a^(d-1)` needs the leading-coefficient-normalized `f'` |
| C | CONFIRMED | none; (5) and (6) reproduced by hand |
| D | CONFIRMED | none essential omitted |

## A. Collision divisor is a component of the singular pullback

Setting reviewed: j = (π, e): X → Z, X smooth integral of dimension n, Z the closure of j(X) in A¹ × Y (integral), j quasi-finite and birational. Let U ⊂ Z be the normal locus. U is a nonempty open: Z is reduced over an algebraically closed (perfect) field, so it is generically regular, and regular local rings are normal. The restriction j⁻¹(U) → U is quasi-finite, birational, separated (affine varieties), with normal target, hence an open immersion by the classical Zariski Main Theorem; in particular it is injective on closed points. If x ≠ x' and j(x) = j(x') = z, then z ∉ U (else both x, x' ∈ j⁻¹(U) map to one point of U), so z ∈ Z \ U ⊂ Sing Z. Thus every collision point lies in the closed set j⁻¹(Sing Z), and the closure D of the dense collision subset lies there too. j is dominant onto Z and Sing Z ≠ Z, so j⁻¹(Sing Z) ≠ X. The irreducible closed subsets of X containing the (n−1)-dimensional irreducible D are D and X only; hence D is an irreducible component of j⁻¹(Sing Z) of dimension n−1, exactly the object quantified in Definition 22.2.

Arbitrary dimension: no step used n = 2. Properness of the singular pullback: from dominance alone, as above; the producer's route (birational ⇒ isomorphism on dense opens, target generically smooth) is also valid. Field assumptions actually used: K algebraically closed (closed points, generic regularity; perfect would suffice); characteristic zero is NOT used in A. Source hypotheses used: X normal (smooth suffices), e quasi-finite (so j is), birationality of j. Manual attacks tried: (i) could a non-normal point of Z be nonsingular? No, regular ⇒ normal. (ii) Could D sit strictly inside a larger component? No, by the dimension count. (iii) Does the argument need Z normal? No; only the normal locus is used, as the producer states. Verdict: CONFIRMED.

## B. Base-affine replacement

π' = (a∘e)·π + (b∘e), a, b ∈ K[Y], a ≠ 0 (Y integral, so a ≠ 0 in K(Y); a∘e ≠ 0 since e is dominant).

- Collision persistence is a pointwise identity with no division: e(x') = e(x), π(x') = π(x) give π'(x') = a(e(x))π(x) + b(e(x)) = π'(x). It holds when a(e(x)) = 0; there the whole e-fibre through x collides under π', which only strengthens the witness.
- Quasi-finite: every fibre of j' = (π', e) lies in a fibre of e.
- Birational: K(Z') = K(Y)(π') ⊂ K(X), and π = (π' − b)/a ∈ K(Y)(π') because a ≠ 0 in K(Y); so K(Y)(π') = K(Y)(π) = K(X). Hence π' is primitive; this is a function-field statement, independent of where a vanishes.
- Nonsaturation: e⁻¹(e(D)) ≠ D involves only e and D. By A applied to j', D is again a divisorial component of j'⁻¹(Sing Z'). The set-image versus closure reading of e(D) is immaterial: for quasi-finite e, e⁻¹(e(D)) = D iff e⁻¹(closure e(D)) = D. (Each component W of the latter has dense image in that closure; the constructible sets e(W), e(D) each contain a dense open of it, so a dense subset of W lies in e⁻¹(e(D)) = D and W = D.)
- Constant a ∈ K*: φ(T, U, V) = (aT + b(U, V), U, V) is an automorphism of A¹ × Y with φ∘j = j', so Z' = φ(Z), Sing Z' = φ(Sing Z), j'⁻¹(Sing Z') = j⁻¹(Sing Z). With f'(T, U, V) := a^d·f((T − b)/a, U, V), which keeps the leading T-coefficient, f'_T = a^(d−1)·f_T((T − b)/a, U, V), so f'_T(π', P, Q) = a^(d−1)·f_T(π, P, Q) as the producer writes. With the un-normalized f' := f((T − b)/a, U, V) the factor is a^(−1). Either factor is a unit, so no divisor statement changes; the phrase "compatible defining equations" should be read as "leading-coefficient-compatible". This is the only precision issue found.
- Nonconstant a: the producer asserts only collision persistence and explicitly disclaims an ambient polynomial inverse. Nothing more is needed for the lemma.

Verdict: CONFIRMED (one precision note, no consequence).

## C. Hand derivation of the G_m x A^1 cubic cover

X = Spec K[x, x⁻¹, y], Y = Spec K[U, U⁻¹, y], e = (x³, y), ζ a primitive cube root of 1 (1 + ζ + ζ² = 0, ζ³ = 1). Étale needs 3 invertible; char 0 is given. T = π_λ = x² + λx. Conjugates over K(U): T_i = ζ^(2i)x² + λζ^i x.

- e₁ = x²(1 + ζ² + ζ⁴) + λx(1 + ζ + ζ²) = 0 (ζ⁴ = ζ).
- p₂ = ΣT_i² = Σ(ζ^(4i)x⁴ + 2λζ^(3i)x³ + λ²ζ^(2i)x²) = 0 + 6λx³ + 0 = 6λU, so e₂ = (e₁² − p₂)/2 = −3λU.
- e₃ = Π ζ^i x(ζ^i x + λ) = ζ³x³·Π(λ + ζ^i x) = U(λ³ + x³) = U(U + λ³), from Π(z − ζ^i x) = z³ − x³ at z = −λ.

Minimal equation T³ − e₁T² + e₂T − e₃ = T³ − 3λUT − U(U + λ³): (5) confirmed. Degree 3 = [K(x):K(U)], so it is irreducible and π_λ is primitive for every λ; explicitly x(x² + λx + λ²) = x³ + λ(x² + λx) = U + λT, and T + λ² is not identically zero. Derivatives: f_T = 3T² − 3λU, f_U = −3λT − 2U − λ³. On X: f_T = 3(x² + λx)² − 3λx³ = 3x²((x + λ)² − λx) = 3x²(x² + λx + λ²) = 3x²(x − λζ)(x − λζ²), since (x − λζ)(x − λζ²) = x² − λ(ζ + ζ²)x + λ²ζ³ = x² + λx + λ². e*(U − λ³) = x³ − λ³ = (x − λ)(x − λζ)(x − λζ²). Both lines of (6) confirmed.

Fibre over U = λ³ (λ ≠ 0): x ∈ {λ, λζ, λζ²} with T = 2λ², λ²(ζ² + ζ) = −λ², λ²(ζ⁴ + ζ²) = −λ². Three fibre lines: {x = λ} at T = 2λ²; {x = λζ} and {x = λζ²} both at T = −λ², for all y. Singular point: f_T = 0 ⇔ T² = λU; substituting in f = 0 gives −U(2λT + U + λ³) = 0, U ≠ 0 forces U = −2λT − λ³, then T² = λU gives (T + λ²)² = 0, so (T, U) = (−λ², λ³) is the unique singular point of the curve on U ≠ 0 (check: f = −λ⁶ + 3λ⁶ − 2λ⁶ = 0, f_U = 3λ³ − 2λ³ − λ³ = 0). Sing Z = that point × the y-line. Since x is a unit, j⁻¹(Sing Z) = D₁ ∪ D₂ exactly, and e⁻¹(e(D_i)) = all three lines ≠ D_i. The obstruction is exact.

λ = 0 control: f₀ = T³ − U², f_T = 3x⁴ a unit, f_U = −2U ≠ 0 on U ≠ 0, so j⁻¹(Sing Z) = ∅. Closed embedding: x = T²·U⁻¹ and x⁻¹ = T·U⁻¹ lie in the image of K[T, U, U⁻¹, y]. (The producer's "x = U/T and T invertible" is true but T⁻¹ in the image is T²U⁻²; the T²U⁻¹ witness is the direct one. Not a defect.) Stronger than stated: π = x alone also gives a closed embedding (x⁻¹ = T²U⁻¹, f = T³ − U, f_T = 3x² unit). So x and x² EACH satisfy Definition 22.2 vacuously, while b·x² + a·x = b·π_(a/b) fails for every ab ≠ 0 (T ↦ bT is an ambient scaling, item B). Generic linear combination failure confirmed in the strongest form.

Dropped hypotheses, both named by the producer: (1) source and target are G_m × A¹, not the affine plane; (2) Jac(e) = 3x² is a nonconstant unit on X, and the A² extension has Jacobian vanishing on {x = 0}, so it is not a Keller map. The example is outside D_n(K)/EE_n(K) of Definition 22.2 and is NOT a Keller counterexample; it is a parameter cover, not a source-map extension. Verdict: CONFIRMED.

## D. Comparison with BGV Definition 22.2, Lemma 22.5, Proposition 27.5

Read in the frozen text, all inside lines 5984–6075 and 7310–7425 plus 100–210: Definition 22.2 and Examples 22.3/22.4, WHOLE Lemma 22.5 with proof, WHOLE Proposition 27.5 with proof and footnote 28, Corollary 27.6, and the introduction's characteristic and affine-space framing.

1. Type 1 versus at-most 1. Definition 22.2: "type m" = "type ≤ m and not type ≤ m−1". Proposition 27.5 is stated for "weak type 1"; its proof opens "Let π be a morphism such that the condition for weak type ≤ 1 ... holds" and uses nothing else. Conclusion (1), e ∈ GA_n(K), is weak type 0 by Example 22.3(1), so the literal hypothesis is never met in char 0. Corollary 27.6(1) applies Proposition 27.5 to "weak type ≤ 1", confirming the operative reading. The producer's remark is exact.
2. Individual versus union saturation. Definition 22.2 quantifies "for each irreducible component Y ... of dimension n−1 we have e⁻¹(e(Y)) = Y". The proof of 27.5 needs one h_i per Y_i: f_{x0}(g) = β·Π(h_i∘e)^{q_i}. Union saturation would break the descent whenever two components with the same image carry q₁ ≠ q₂. The producer's "each prime divisor, not merely their union" is the correct reading. Lemma 22.5 uses TWO functions (y, z), obtains a locally closed embedding off a codimension-≥2 set W, hence no divisorial component at all (condition vacuous) and weak type ≤ 2; it never asserts a single combination, and item C shows one cannot be inferred.
3. Base descent versus norm. The step "f_{x0} − βΠh_i^{q_i} divisible by f, then x₀-degree 0" descends f_{x0}(g) ITSELF to K_t[x]. It needs (a) each Y_i saturated, giving e⁻¹(V(h_i)) = Y_i (BGV write "It follows"; the producer's constructible-image argument, rechecked in B, supplies it), and (b) h_i∘e reduced (étale pullback of a reduced divisor), left implicit by BGV and stated by the producer. The norm of f_{x0}(g) lies in K_t[x] automatically and yields nothing. Distinction correct.
4. Omissions. None essential. The producer's interface is exactly weak type ≤ 1: primitive ⇔ birational, quasi-finite from e, plus the individual divisor condition. Its (1), j⁻¹(Sing Z) = V(f_T(π, P, Q)), matches the proof's "both systems define Sing Z ∩ Im" via the invertible Jacobian; rederived: (f_U, f_V)·Jac(e) = −f_T·(π_x, π_y), so f_T = 0 on the image forces f_U = f_V = 0. Pure dimension n−1 holds in char 0 because f_T(π, P, Q) ≠ 0 (T-degree d−1 < d). BGV's "by Definition 2.1" inside the proof is a cross-reference slip for Definition 22.2; immaterial.

Not asserted here: whole-paper verification, any JC2 theorem promotion, or a source-map reading of the item C cover. Verdict: CONFIRMED.

## Scope, manual attacks, and limits of the accepted output

WHOLE: producer report and its READ-SCOPE. SELECTED: bgv-v1.txt line ranges above only. Manual algebra only; no CAS, code, network, AWS/SSH, agents, other reports or ledgers. Writes: this file and box/bgv-persistent-collision-gate-fable5-20260909/READ-SCOPE.md, apply_patch only. Attacks run by hand: non-normal-but-regular point (fails), larger-component containment (fails by dimension), a vanishing on e(D) (persistence is pointwise), set-versus-closure image (equivalent), un-normalized f' scaling (unit only), extra singular points on the cubic curve (none on U ≠ 0), λ = 0 embedding (holds), π = x alone (holds, strengthens C).

What the accepted output does: a dense collision witness on a nonsaturated divisor D rejects π and its entire base-affine class (4). What it cannot do: establish JC2 or a counterexample; absence of collisions is not acceptance, since components of (1) without source collisions must still be checked. Nothing in the producer's §4 claim about the campaign's cubic parameter cover was verifiable from the three inputs; it is not a claim about the lemma. No exit-price assertion is made, so no exit basis line is declared.

## OPEN(S) RAISED

None new. The producer's exact remaining quantity stands: for one licensed actual source and one chosen primitive π, which prime divisors of f_T(π, P, Q) fail full e-saturation.

## COLLISIONS

status: EMPTY — own-only check of the two target paths (absent at lease, created by this lane only); no corpus scan.

<!-- BODY-END -->
