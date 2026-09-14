# Gate: c lies in (λ2,λ3) for ordinary φ-lifts (Fable 5.1, 2026-09-07)

Bounded 15-minute independent proof gate of `xmodel/d125-zero-lambda-obstruction-astra-20260907.md` (lane copy SHA-256 `a878a87b…`, body 3749 bytes, body SHA `cbd40191…` re-derived, MATCH) and its `check.py` (`f0c9acb2…`). All five frozen inputs in `/tmp/jc2-lane.WtgJza/inputs` re-hashed and byte-identical to the repository copies; frozen basis `0d39df3c` equals HEAD. Status: **PROVISIONAL PROOF GATE, not a baseline dependency.** No CAS, AWS, solve, production expansion, sublane, shared/adapter/FALLACY/ledger edit or live peer read. Verdict: **CONFIRMED.**

## Verdict table

| item | verdict |
|---|---|
| lemma: R any commutative K-algebra (nilpotents allowed), A,B ∈ R[g,p] finite of arbitrary degree, [A,B]=c·g², P=φ(A), Q=φ(B) ∈ R[u,v] ⇒ c ∈ (λ2,λ3)R | **CONFIRMED**, two independent proofs, §1 |
| [u⁰v¹] formula: sign (−1)^j, multinomial j!/(b!d!(j−b−d)!), constraint 3b+2d=i+j+1, every term has b+d>0 | **CONFIRMED** (C1, 55 monomials, plus the mod-λ weight argument) |
| witnesses U_C,V_C,M2,M3 and the quotient witness 1=λ2·z·M2+λ3·z·M3 | **CONFIRMED** (C3) |
| chain rule with det +v², localization injection, origin evaluation with no domain/point assumption | **CONFIRMED** (C2, C4, C5) |
| ordinariness essential; toy A=g, B=g²p+g³ reused, not novel | **CONFIRMED**, failure mechanism in §3 (C6, C7) |
| consequence I+(λ2,λ3)=S, Spec(S/I)=D(λ2)∪D(λ3); no individual λ unit, no λ=1 normalization, no benefit, no JC2 claim | **CONFIRMED** as stated, §4 |
| 30+75 rows are all negative rows of the actual client | accepted from gate `4295593a…`, not reproved here |

## 1. Independent proof

**Ring map.** φ: R[g,p] → L := R[u,v,v⁻¹], g ↦ v⁻¹, p ↦ v⁴u − λ2v² − λ3v − v⁻¹, with λ2,λ3 ∈ R fixed elements, generator order (u,v), coefficient ring R. Image checks are C1/C6.

**Step 1, bracket.** ∂_u and ∂_v are R-derivations of L, and for every F ∈ R[g,p] the identity ∂(φF) = φ(F_g)·∂(φg) + φ(F_p)·∂(φp) holds by the Leibniz rule on monomials and R-linearity; it is a formal identity over Z. Hence [P,Q] = φ([A,B])·(φg_u·φp_v − φg_v·φp_u) = c·v⁻²·(0 − (−v⁻²)·v⁴) = c in L. No field, domain or characteristic assumption enters.

**Step 2, injection.** L is a free R-module on u^t v^e (t ≥ 0, e ∈ Z) and R[u,v] is the free submodule spanned by e ≥ 0; the derivations restrict. So the bracket computed in R[u,v] equals c there. Nilpotents of R are irrelevant: the inclusion is a direct summand of free modules, not a statement about zero-divisors of R. (Equivalently v is a nonzerodivisor on R[u,v] for every R, C5.)

**Step 3, origin.** Apply the R-algebra map R[u,v] → R, u,v ↦ 0, which extracts constant coefficients. With p1 = [u¹v⁰]P, f_A = [u⁰v¹]P, q1 = [u¹v⁰]Q, f_B = [u⁰v¹]Q this gives the coefficient identity c = p1·f_B − q1·f_A (C4). No point of Spec R is chosen.

**Step 4, membership, proof A (weight).** Reduce modulo J = (λ2,λ3)R. Then φ̄(g) = v⁻¹ and φ̄(p) = v⁴u − v⁻¹ are homogeneous of weight 1 for w(u)=5, w(v)=−1, so φ̄(g^i p^j) is a combination of u^t v^{5t−i−j}. The monomial u⁰v¹ has weight −1 < 0 ≤ i+j and cannot occur (C1). Hence f_A, f_B ∈ J and c ∈ J.

**Step 4, proof B (explicit certificate).** Expanding v⁻ⁱ(v⁴u − λ2v² − λ3v − v⁻¹)^j with t,b,d,z factors gives j!/(t!b!d!z!)·(−1)^{b+d+z}·λ2^b λ3^d u^t v^{4t+2b+d−z−i}. At t=0 and exponent 1 this is 3b+2d = i+j+1 ≥ 1 with sign (−1)^j, so (b,d) ≠ (0,0) in every term. Splitting b ≥ 1 from (b=0, d ≥ 1) yields f_C = λ2·U_C + λ3·V_C with U_C, V_C ∈ Z[c_ij, λ2, λ3] evaluated in R and no division. Therefore c = λ2·(p1U_B − q1U_A) + λ3·(p1V_B − q1V_A), and with z·c = 1 in R, 1 = λ2·z·M2 + λ3·z·M3 (C3). The producer's exponent, sign, partition and witnesses are exactly these. The identity persists under every further quotient of R.

**Scope.** Degree, monicity, faces and the specific field never enter; integer multinomials do not even need Q. Read literally at arbitrary degree. No converse is claimed: c ∈ (λ2,λ3) does not imply ordinariness, and nothing about a single λ follows.

## 2. Producer text against the proof

- "Reviewed 30+75 rows supply ALL negative rows": consumed from gate `4295593a…`; used only to identify "ordinary" with "the 105 rows vanish" for the actual client.
- "Exact ideal equality I+(λ2,λ3)=S, not merely radical": correct, since 1 − z(λ2M2+λ3M3) ∈ I literally.
- "Injective even with nilpotents": correct, by Step 2.
- "Origin evaluation of the Laurent derivatives is invalid" for the toy: correct, §3.
- Golden field: K = Q[ρ]/(ρ²−3ρ+1) is only the base of R; nothing is split numerically.
- Novelty: the toy is credited to contract §7 and gate §5; no wider claim is made. Agreed.

No producer claim failed.

## 3. Essential ordinariness

At λ2=λ3=0, A=g, B=g²p+g³: [A,B] = g², P = v⁻¹, Q = v²u, [P,Q] = 1 = c, yet (λ2,λ3) = 0 in R = K. Step 2 is what fails: P ∉ R[u,v], P_v = −v⁻² has no constant term, and the origin formula returns p1f_B − q1f_A = 0 ≠ 1. Exactly one negative row fails, [u⁰v⁻¹]P = 1 (C6). A second illustration (C7): W = g²p + λ2 + λ3g + g³ and B = g²p + g³ satisfy [W,B] = λ3·g², φ(W) = uv², φ(B) = v²u − λ2 − λ3v⁻¹; the single negative row −λ3v⁻¹ forces λ3 = 0 and hence c = 0, consistent with the lemma and showing that the row, not c, carries the obstruction. Neither pair is a counterexample fixture.

## 4. Precise two-open-cover consequence

Let S be the guarded source ring (receiver coefficients, c, z_c where c is not a fixed unit, λ2, λ3, ρ if golden) and I the complete guarded ideal: all 780 Jacobian slots, monicity, the 105 negative rows, and z_c·c − 1. Then I + (λ2,λ3) = S. Equivalent forms: V(I) ∩ V(λ2,λ3) = ∅; Spec(S/I) = D(λ2) ∪ D(λ3); I is proper if and only if I + (z2λ2 − 1) is proper or I + (z3λ3 − 1) is proper; the both-zero specialization S/(I+(λ2,λ3)) is the zero ring. Which chart is nonempty, whether both are, and whether λ2λ3 vanishes somewhere remain undetermined. Not licensed: λ2 or λ3 a unit of S/I; a normalization λ2 = 1 or λ3 = 1 (the dilation τ is already spent on a = 1 or μ = 1, and λ2 ↦ λ2τ⁻³ would need a unit anyway); any added global equation; a point; properness of I; any solving-cost or runtime statement; any JC2 resolution. (x, 1−x) = K[x] with neither generator a unit is the right analogy.

## 5. Controls and custody

Producer `check.py` replayed byte-identical: normal and `-O` exit 0 (36 jets, 2 fixtures, toy rejected); `--mutate-map` and `--mutate-drop-negative` exit 1 in both modes with the intended messages; at most 0.53 s and 39 MB (`producer_runs.txt`, six `run*.out/.err`). Own `gate_controls.py` (SHA `51644061…`, standard library, coefficient ring Z[λ2,λ3,ε]/(ε²) so every control runs with a nilpotent): C1 closed form versus repeated multiplication versus the mod-λ line on 55 monomials i+j ≤ 9; C2 det = +v² and the chain rule on six random nilpotent-coefficient pairs of degrees 4 and 3; C3 witnesses on six random degree-5 sources; C4 origin identity on six random ordinary pairs; C5 v-shift; C6 toy; C7 W-example. Normal and `-O` exit 0 in at most 0.17 s and 15 MB; `--mutate-sign`, `--mutate-map`, `--mutate-det`, `--mutate-drop` each exit 1 in both modes at the intended check (`own_runs.txt`). All commands ran under `ulimit -t 25 -v 524288` and `timeout 30`. My script's first version failed at my own C3 through a key-shape mismatch in the comparison; the fix touched only that comparison, no claim. Input pins and the producer body-seal re-derivation are in `input_pins.txt`. Evidence only in `box/d125-zero-lambda-gate-fable5-20260907/`. All writers finished before publication.
<!-- BODY-END -->
