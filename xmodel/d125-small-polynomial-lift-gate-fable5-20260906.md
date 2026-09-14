# Gate: small receiver plus 105 rows is a sufficient polynomial Keller client (Fable 5.1, 2026-09-06)

Bounded 25-minute independent proof gate of `xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md` (lane copy SHA-256 `433cc2fe…`, body 15284 bytes, body SHA `f4a2aab6…` re-derived and MATCH) and its `check.py` (`77f8ee1b…`). All six frozen inputs in `/tmp/jc2-lane.AYiVyM/inputs` re-hashed; the three charged reports and the checker are byte-identical to the repository copies; frozen basis `0d39df3c` equals HEAD. Whole 181-line proof and 155-line code read. Status: **PROOF GATE ONLY.** No ideal, solve, CAS, AWS, point search, ledger edit or full client expansion. Nothing here is a properness, existence, novelty, global degree-125 or performance claim.

## Verdict table

| item | verdict | basis |
|---|---|---|
| main acceptance theorem: complete receiver J, monicity, c≠0, all 105 negative rows ⇒ polynomial Keller pair of exact degrees 75/125, not an automorphism | **CONFIRMED**, proved independently below, no F2/census necessity used | §1, C1a–d, C2a–b, C4a–b |
| exponent `e=5t+3b+2d−i−j`, sign `(−1)^(j−t)`, multinomial, `λ2^b λ3^d`; slot list 30+75; λ-degree 7/12; no truncation | **CONFIRMED** by a different expansion algorithm | §2, C3a–d |
| golden field as one relation, `ρ^{-1}=3−ρ`, both conjugates retained; c guard only when c is not a fixed unit | **CONFIRMED** | §2, C8a–c |
| optional graph lemma: `D0=162` or `6ρ^6`, rows `[u²v^{−5..−2}]`, graph values, coordinate-ring isomorphism | **CONFIRMED** with the full contribution census in §3 | C6a–i |
| dilation covariance `λ2τ^{−3}, λ3τ^{−2}`, fifth-cut coefficient 1 persists, `c_τ=cτ^{−36}`, constants harmless, `c=−5/(9κ)` fixed, common μ=1 keeps c variable | **CONFIRMED**; sufficiency is inherited by every sub-locus, so it does not depend on the source-normalization theorem | §4, C7a–d |
| necessity for all counterexamples; Roy/Moh/Strinz identification; properness of anything less than the complete guarded ideal | **not claimed by producer, correctly declared GAP / conditional** | §5 |

No claim of the producer failed. The producer's checker passes in normal and `-O` mode and both wrong-sign mutations exit 1 in both modes (own re-run, §6). My own control script, on its first version, was killed at the 25 s CPU cap by a quadratic accumulator of mine; the fixed version runs in 2.4 s. Both artefacts are kept.

## 1. Independent proof of the acceptance theorem

Let k be a field of characteristic zero, `A,B ∈ k[γ,π]` with total degrees at most 15 and 25, `[A,B] := A_γB_π − A_πB_γ = cγ²` with `c ∈ k^×`, `a_{0,15}=b_{0,25}=1`, and `λ2,λ3 ∈ k` arbitrary (zero allowed). Define the k-algebra homomorphism `φ: k[γ,π] → R := k[u,v,v^{−1}]`, `γ ↦ v^{−1}`, `π ↦ v⁴u − λ2v² − λ3v − v^{−1}`, and `P := φ(A)`, `Q := φ(B)`.

**Bracket.** For any k-algebra homomorphism between polynomial or Laurent rings, partial derivatives obey the chain rule, so `[P,Q]_{(u,v)} = φ([A,B]) · det ∂(γ,π)/∂(u,v)`. The determinant is `γ_u π_v − γ_v π_u = 0 − (−v^{−2})(v⁴) = +v²`. Hence `[P,Q] = c·v^{−2}·v² = c` in R (C1a, C1d checks the chain rule on random Laurent pairs with negative γ-powers). The forward determinant `[U,V]_{(γ,π)} = +γ²` and both compositions are identities (C1b, C1c), so φ is injective with the stated inverse and no sign is lost.

**Polynomiality.** Expanding `γ^iπ^j` under φ by repeated multiplication (my algorithm; the producer uses the closed multinomial) gives a finite Laurent polynomial whose monomials are `u^t v^e λ2^b λ3^d`, `t ≥ 0`. Distinct monomials of `k[u,v^{±1}]` are linearly independent, so `P ∈ k[u,v]` iff every coefficient `[u^t v^e]P`, `e<0`, vanishes. These are finitely many literal coefficients of a finite Laurent polynomial, not jets of a series. §2 shows the index set of possibly nonzero negative coefficients is exactly 30 slots for P and 75 for Q. Therefore the 105 rows plus the receiver rows give `P,Q ∈ k[u,v]` with `[P,Q]=c ≠ 0`, a Keller pair.

**Degrees.** A monomial of `φ(γ^iπ^j)` with t factors `v⁴u`, b factors `−λ2v²`, d factors `−λ3v` and `z=j−t−b−d` factors `−v^{−1}` has `t+e = 5t+2b+d−z−i ≤ 5(t+b+d+z)−i = 5j−i ≤ 5D`, with equality iff `b=d=z=0`, `i=0`, `j=D`. So the unique monomial of total degree 5D is `u^D v^{4D}` with coefficient `a_{0,D}=1`; no cancellation is possible and `deg P = 75`, `deg Q = 125` exactly (C4a on random monic fixtures of degree 15 and 25, with numeric λ's). Also `deg_u ≤ D`, `deg_v ≤ 4D`, weight `5t−e ≤ D` (C4b). Monicity therefore replaces any degree guard; none is needed.

**Counterexample.** Neither 75 nor 125 divides the other (C8b). The named external criterion (a characteristic-zero plane polynomial automorphism has one component degree dividing the other, from the Jung–van der Kulk tame-generation theorem) then says `(P,Q)` is not an automorphism. It is a Keller map, hence a JC2 counterexample over k. This criterion is consumed, not re-proved.

**From an ideal to a point.** Let I be the ideal over K=Q or K=Q(ρ) generated by every coefficient of `[A,B]−cγ²` (all 780 slots `r+s ≤ 38`, C2a–b; absent coefficients zero), the two monicity rows, the 105 negative rows, and `z_c·c−1` when c is a variable. If I is proper, it lies in a maximal ideal m; `K[x]/m` is a finitely generated K-algebra field, hence a finite extension of K by Zariski's lemma (weak Nullstellensatz). This gives a point over `Q̄` at which the guard forces `c≠0`, and the theorem above applies with `k=Q̄ ⊂ C`. A proper projection, an omitted-row subsystem, a modular point or a receiver-only point supplies none of the 105 rows over a characteristic-zero field, so none certifies anything. **CONFIRMED.** Nothing in this section uses the F2 reduction, any census, or any identification with Roy, Moh or Strinz objects.

## 2. Row and ring claims

**Formula.** By the multinomial theorem, the coefficient of `u^t v^e λ2^b λ3^d` in `φ(γ^iπ^j)` is `j!/(t!b!d!z!)·(−1)^{b+d+z} = j!/(t!b!d!z!)·(−1)^{j−t}` with `e = 4t+2b+d−z−i = 5t+3b+2d−i−j`. Control C3a expands every `π^j`, `j ≤ 25`, by repeated multiplication and compares each resulting coefficient with this closed form, which does not depend on i; all agree, and the degree/weight bounds of §1 hold for every `(i,j)` with `i+j ≤ 25` after the `v^{−i}` shift. The sign mutation `(−1)^j` is rejected.

**Slot list.** `e<0` forces `5t < i+j ≤ D`, so `t ≤ ⌊(D−1)/5⌋`; at fixed t the minimum is `5t−D` (`b=d=0`, `i+j=D`). Every intermediate `(t,e)` is attained by the π-axis monomial `π^{5t−e}`, which lies in all three closed polygons. Control C3b shows the expanded negative support equals `{t ≤ ⌊(D−1)/5⌋, 5t−D ≤ e ≤ −1}` for D=15 and 25, C3c gives 30 and 75 slots, and C3d recomputes the negative support restricted to each of the six polygon lattices with my own half-plane membership test and finds the same sets. Slots that later specialize to zero stay in the list; that is harmless.

**λ-degree.** `e<0` gives `3b+2d ≤ D−5t−1`, hence `b+d ≤ 7` (D=15) and `≤ 12` (D=25), attained at `(i,j)=(0,D)`, `d=7` or `12`, `e=−1` (C3c). Rows are linear in the receiver coefficients, so total degree at most 8 and 13. These are algebraic bounds only.

**Golden field.** `Q[ρ]/(ρ²−3ρ+1)` is a field because 5 is not a rational square; `ρ(3−ρ)=1` (C8a, computed in my pair representation `a+bρ`, not by monomial reduction). Either work over that field or adjoin ρ as a variable with its quadratic; a proper ideal then has a `Q̄`-point at one of the two conjugates, and a unit certificate over the field conjugates to the other embedding. Splitting a coefficient by a numerical root is the only forbidden move, and the producer does not do it.

**Guard.** In the unequal case `c=−5/(9κ)` is a fixed nonzero element (`−5/9` or `−5/3+(5/9)ρ`, C8c); no guard. In the common cases c is a variable and `z_c·c−1` is required; without it a point with `c=0` would not be excluded, and `[P,Q]=0` is not a Keller pair.

## 3. Optional graph lemma

Write `A(γ,γz) = Σ_k γ^{15−k} a_k(z)`, `a_k(z) = Σ_{i+j=15−k} a_{i,j} z^j`. With `z = π/γ = πv = −1 + w`, `w = v⁵u − λ3v² − λ2v³`, we get `P = Σ_k v^{k−15} a_k(−1+w)`. Control C6a computes P this way (Taylor shift by Horner composition, then substitution of w) on a fixture with the full fixed face `H³` and random coefficients on **every** lattice point with `i+j ≤ 14`, over Q for the squarefree face and over `Q(ρ)` for the golden face, and finds it identical to the direct substitution.

The `u²` part of `w^r` is `C(r,2) v^{10} (−λ3v²−λ2v³)^{r−2}`. So `[u²v^e]P = Σ_{k,r} a_k^{(r)}(−1)/r! · C(r,2) · [v^{e−k+5}](−λ3v²−λ2v³)^{r−2}`. The last factor has v-exponent `≥ 2(r−2)`, and the complete census of contributions with `k + (that exponent) = e+5` is:

| row | contributions (k, r, factor) | value |
|---|---|---|
| `[u²v^{−5}]` | (0,2,1) | `a_0''(−1)/2 = 0`, since `a_0=h³` vanishes to order 3 at −1 |
| `[u²v^{−4}]` | (1,2,1) | `a_1''(−1)/2` |
| `[u²v^{−3}]` | (2,2,1), (0,3,−λ3) | `(a_2''(−1) − λ3 D0)/2` |
| `[u²v^{−2}]` | (3,2,1), (1,3,−λ3), (0,3,−λ2) | `(a_3''(−1) − λ3 a_1'''(−1) − λ2 D0)/2` |

The candidate (0,4,λ3²) has exponent 4 ≠ 3 and does not enter the last row. `D0 = a_0'''(−1) = 6h'(−1)³` because −1 is a simple root of h: `h'(−1)=3` for `z²(z³+1)` and `h'(−1)=ρ²` for `z²(z+1)(z+1−ρ)²`, giving 162 and `6ρ⁶ = −330+864ρ`, both nonzero constants of the coefficient field with `D0^{−1} = (3−ρ)⁶/6` in the golden case (C6b, C6c; the mutation `6ρ⁵` is rejected). C6d–g verify all four rows against the direct expansion for both faces, and C6h shows the graph values `λ3 = a_2''(−1)/D0`, `λ2 = (a_3''(−1) − λ3 a_1'''(−1))/D0` annihilate both rows. Because the two rows are `(unit)·(λ − polynomial in the other unknowns)`, adjoining them and eliminating `λ2,λ3` is an isomorphism of coordinate rings `K[X,λ]/(I', rows) ≅ K[X]/(I'|_{λ=graph})` **only if** every other row, guard and face relation is carried through the substitution; the producer states exactly this. C6i confirms the fixture is not itself polynomial, so nothing here is an existence claim. The lemma needs the fixed face `a_0=h³`; with monicity alone `a_0''(−1)` and `D0` are not constants. **CONFIRMED.**

## 4. Composition with the economical normalizations

For `A_τ = τ^{−15}A(τγ,τπ)`: `P(τ⁵u, τ^{−1}v) = A(τ·v^{−1}, τ·(v⁴u − λ2τ^{−3}v² − λ3τ^{−2}v − v^{−1}))`, so `P_τ(u,v) := φ_{λ_τ}(A_τ) = τ^{−15}P(τ⁵u,τ^{−1}v)` with `λ2_τ = λ2τ^{−3}`, `λ3_τ = λ3τ^{−2}`; the `γ⁵` (fifth-cut) coefficient of the forward map stays 1 because `γ⁴π` and `γ⁵` both scale by `τ⁵`. C7a checks this on a random monic degree-15 fixture with nonzero numeric λ's and rejects the swapped exponents; C7b keeps monicity; C7c gives `[A_τ,B_τ] = cτ^{−36}γ²`. Subtracting receiver constants subtracts the same constants from P,Q and touches no negative row or leader (C7d).

The unequal-face constants `c = −(5/9)a³/κ`, the `a → a/τ^{12}` transport, and the common-case `μ → μ/τ²`, `μ/τ` are consumed from the independent gate `cd69c238…` (re-hashed MATCH), not re-derived. Setting `a=1` gives the fixed unit `c=−5/(9κ)`; imposing `c=1` as well would be inconsistent, and the producer forbids it. Setting `μ=1` exhausts the dilation, so c stays a guarded variable there.

**Sufficiency is normalization-independent.** The theorem of §1 is universally quantified over all `(A,B,c,λ2,λ3)` satisfying its equations. Every economical normalization only adds equations or fixes constants that keep monicity and `c≠0`; the resulting locus is a sub-locus, so any point of it is still a counterexample certificate. Whether the normalized chart is **necessary**, i.e. whether every actual standard-F2 pair lands in it, depends on the earlier normalization theorem and the exact incoming chain; that direction is conditional and is not part of this gate. In particular the producer's "necessary coverage" is correctly restricted to the exact incoming chain, not to all counterexamples.

## 5. Exact sufficient-client boundary

A client certifies a JC2 counterexample **iff** it emits, over Q or `Q[ρ]/(ρ²−3ρ+1)` without numerical splitting, all of: every coefficient of `[A,B]−cγ²` on all 780 slots (zero rows may be dropped only if they are identically zero as polynomials, since the theorem needs the full bracket); `a_{0,15}−1`, `b_{0,25}−1`; all 30+75 negative rows as literal coefficient extractions with `λ2,λ3` free variables (or the two graph substitutions of §3 applied to every remaining row); and `z_c·c−1` unless c is a fixed nonzero constant. Then properness ⇒ counterexample over C. Nothing weaker suffices: a receiver-only ideal (C5a shows `γ, γ²π+γ³` has bracket `γ²` yet lifts to `P=v^{−1}`), a subsystem missing one actual row (C5b–c: dropping the single row `[u⁰v^{−1}]P` makes my verifier accept that nonpolynomial P), a modular point, or a projection. Positive fixtures `u³`, `u²v³`, `u+uv` round-trip (C5d). No conclusion about necessity, about the Roy/Moh/Strinz families, or about any solving cost follows.

## 6. Controls and custody

`box/d125-small-polynomial-lift-gate-fable5-20260906/`: `input_pins.txt` (six SHA-256, all MATCH the repository copies), `body_seal.txt`, `producer_check.py` (byte-identical to the charged `check.py`), `producer_runs.txt` with six `run*.out/.err`: normal and `-O` exit 0 printing `{30,75}×3, total 105, λ-degree {7,12}`; `--mutate-sign` and `--mutate-pivot` exit 1 in both modes with the injected messages; 0.2–0.7 s, peak 39 MB. Own `gate_controls.py` (SHA `ebee1c63…`, 54 checks, standard library only, exact rationals, `Q(ρ)` as pairs): `gate.out` and `gate_O.out` exit 0 in 2.4 s and 42 MB; `--mutate-det`, `--mutate-sign`, `--mutate-omit`, `--mutate-D0`, `--mutate-scale` each exit 1 at the intended check (`own_runs.txt`). All commands ran under `ulimit -t 25 -v 524288` and `timeout 30`. The first version of my script was killed by the CPU cap (`first_version_cpu_timeout.*`); the fix was to my accumulator, not to any claim. Fixtures are small: the largest expansions are a 41-monomial degree-25 receiver and a full-support degree-15 receiver, both with symbolic λ's. No live engineering, positive-face or other review file, ledger, FALLACY, adapter, tool or protected project was read or changed. All writers finished before this publication.
<!-- BODY-END -->
