# Gate: exact F2 degree-(15,25) monomial receiver and economical normalizations (Fable 5.1, 2026-09-06)

Bounded 25-minute independent composition gate of `xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md` (lane copy SHA-256 `7dec79af…`) and its `check.py` (`3ff299bc…`). Lane inputs `/tmp/jc2-lane.8Jt5YL/inputs`, all five charged pins re-hashed and MATCH; frozen basis `0d39df3c` equals HEAD. Named dependency accepted, not re-proved: the terminal published-chain gate `5be50d00…` with its hypothesis (actual polynomial standard (3,5) pair of degrees 75/125 with the F2 triple), its three-case necessary implication to the degree-(30,50), `J=x^3` polygons, and its quoted external theorems. Status: **PROOF GATE ONLY.** No ideal, solve, CAS, AWS, ledger edit or primary-chain replay. Nothing here is a counterexample claim or a global degree-125 exclusion.

## Verdict table

| item | verdict | basis |
|---|---|---|
| 1 map S, inverse, T4 = S∘T5, determinants, degree table, six counts | **CONFIRMED** | C1a–d, C3, C3x |
| 2 every nonzero Jacobian row has I−J≥1; full row ideals equal under literal renaming | **CONFIRMED** | elementary proof below; C2 symbolic |
| 3 outer H = π²S3 both patterns, both conjugates, κ∈{1,ρ}; inner faces and scalars transported, not added | **CONFIRMED** (face data consumed from predecessor, re-verified arithmetically) | C4a–e, C5a–h |
| 4 monicity changes c; dilation gives τ^−36, preserves H; μ → μ/τ², μ/τ; c=1 only over K̄; vertices stay nonzero; origin is a translation choice | **CONFIRMED** | C6a–h |
| root candidate: constants 0, a=1 (unequal) / μ=1 (common), c free nonzero in common cases | **CONFIRMED as a necessary client with exact K̄-nonemptiness equivalence**, scope below | C5d–f, C6g–h, C7 |
| reverse polynomial lift, Roy/Strinz attachment, properness ⇒ counterexample | **GAP, correctly declared by producer**, out of scope | — |

No claim of the producer failed. One sub-assertion of my own control script failed on its first run (I applied the identity 1/κ = 3−κ at κ=1, where it is false); I corrected my check, not the claim, and record it here.

## 1. Maps and counts (claim 1)

S sends `x^i y^j` to `γ^{i−j} π^j`. On the cone `i≥j≥0` this is a lattice bijection onto the nonnegative quadrant with inverse `(a,b)→(a+b,b)`, i.e. `U(x,y)=A(x,xy)`, so coefficients are carried literally with no denominators (C1d). All three accepted (30,50) polygons lie in `i≥j`; total degree after S is the old x-exponent, giving 15/25 with the top attained at the transported upper vertices. `Jac S = 1/γ` and `Jac T4 = −γ²` (C1c, symbolic); the chain rules `[SU,SV]=γ^{−1}S([U,V])` and `[T4P,T4Q]=−γ²T4([P,Q])` hold on random Laurent pairs (C1a, C1b), and `T4 = S∘T5` on the same pairs. So `J=x³` becomes `J=γ²` with the same scalar and no sign change, and the T5 minus sign is carried, not lost.

Six counts by explicit half-plane membership and by Pick, independently of the producer's cross-product routine: 83/215, 94/241, 115/296 (C3). S maps the six old lattice sets bijectively onto the six new ones (C3x). So the presentation is smaller in degree and bounding box only; it removes no coefficient slot. CONFIRMED.

## 2. Full-row transport (claim 2)

A bracket contribution from `(i,j),(k,l)` lands at `(I,J)=(i+k−1,j+l−1)` with `I−J=(i−j)+(k−l)≥0`; equality forces `i=j`, `k=l`, whence the determinant `il−jk=0`. Hence every potentially nonzero row has `I−J≥1`, and after the factor `γ^{−1}` the row index `(I−J−1,J)` is nonnegative. C2 does this with symbolic coefficient names on a small `i≥j` polygon: the new row polynomials are identical to the old ones after renaming, the index sets correspond exactly, and `(3,0)→(2,0)`. Because the renaming is a bijection of coefficient variables and each guard `z·coef−1` is carried by name, the full guarded row ideals are equal, not merely their projections. Identically zero rows are the same on both sides. CONFIRMED. This equality is of ideals in the coefficient ring; it is not a statement about any truncated or partial row stream.

## 3. Faces (claim 3)

Consumed from the predecessor and re-verified, not re-derived: `r=(w−1)²h(w)` with `h=w²−3w+3` (pattern (2,1,1)) or `h=(w−ρ)²`, `ρ²−3ρ+1=0` (pattern (2,2)); both satisfy the Euler ODE `4wfr′−5wf′r−fr=r/3` with the predecessor's `f`, checked for both conjugates `(3±√5)/2` (C4a, C4b). The cut face `(y+x^{−5})(x⁵y)²h(1+x⁵y)` under T4 is `π²(π+γ)·γ²h(1+π/γ)`, a homogeneous quintic with no negative powers. Literal substitution gives `π²(π³+γ³)` for the squarefree pattern and `π²(π+γ)(π+(1−ρ)γ)²` for the golden pattern, whose expansion `π³+(3−2ρ)γπ²+(2−ρ)γ²π+ργ³` uses `(1−ρ)²=ρ`; both conjugates checked exactly, not by a labelled slope (C4c, C4d). In general `κ=h(1)`, so κ=1 or ρ, nonzero and ≠1, and the two faces are distinct (C4e).

Outer faces: `A_15=λ_P H³`, `B_25=λ_Q H⁵`, so the shared corners `(9,6)`, `(15,10)` carry `λ_Pκ³`, `λ_Qκ⁵`. Unequal inner face: the `(5,−7)` weight is maximal on both polygons, with value 3 exactly on `{(2,1),(9,6)}` and 5 exactly on `{(1,0),(8,5),(15,10)}`, and the face-bracket weight `3+5+2=10` equals the weight of `γ²` (C5b). Hence the face bracket, computed symbolically as `−ad γ² + (2ae−6bd)γ⁹π⁵ + (5af−3be)γ¹⁶π¹⁰` (C5a, signs audited), must equal `cγ²` exactly: the three equations are necessary and complete for that face. Common faces: `x^{−1}(x³y−μ)²→γ(γπ−μ)²`, `x^{−3}(x⁴y−μ)²→γ³(π−μ)²` (C5g); `G_k³`, `G_k⁵` have supports exactly equal to the full top-weight segments and are monic at the shared corners, so the scalars are forced to `λ_Pκ³`, `λ_Qκ⁵` by the outer face and no scalar is added; their bracket weight exceeds 2, so the faces commute, as they do (C5h). CONFIRMED. The double-root shape of the common faces and the unequal endpoint assignment are the predecessor's derived facts, gated there, and are consumed here.

## 4. Monicity and dilation (claim 4)

Translation by constants leaves the bracket unchanged (C6a). Target scaling by `λ_P^{−1}, λ_Q^{−1}` divides c by `λ_Pλ_Q` (C6b); it needs only the guarded nonzero corners and is same-field. The dilation `A_τ=τ^{−15}A(τγ,τπ)`, `B_τ=τ^{−25}B(τγ,τπ)` satisfies `[A_τ,B_τ]=τ^{−38}([A,B])(τ·)`, hence `cγ²→cτ^{−36}γ²` (C6c); it fixes `H³` and `H⁵` entirely for both patterns (C6d); it sends `a→a/τ¹²`, `e→e/τ¹²`, `d→d/τ²⁴`, fixes b,f, and sends `μ→μ/τ²` (common_3), `μ→μ/τ` (common_4) (C6e). Every coefficient is multiplied by a nonzero τ-power, so nonzero vertices stay nonzero (C6f). `c=1` needs `τ³⁶=c`, which exists over K̄ only; that is a geometric statement, not a same-field scheme isomorphism. CONFIRMED.

## 5. Root candidate: verdict and exact scope

**Unequal.** With monic targets, `b=κ³`, `f=κ⁵` and the three face equations give `e=(5/3)aκ²`, `d=(5/9)a²/κ`, `c=−(5/9)a³/κ` (C5c). Choosing `τ¹²=a` sets `a=1` and yields exactly the root's constants `b=κ³, f=κ⁵, e=5κ²/3, d=5/(9κ), c=−5/(9κ)` (C5d); C6h performs this normalization explicitly on an `a=7` golden face point via `τ=7^{1/12}`, landing on those constants with bracket `−5/(9ρ)γ²`. All constants lie in Q (κ=1) or Q(ρ) (κ=ρ); for the golden branch `1/ρ=3−ρ`, so `c=−5(3−ρ)/9`. c and d are automatically nonzero for κ∈{1,ρ,ρ̄} (C5e), so **no guard on c is needed and none should be added**. Fixing `c=1` as well would be inconsistent for every κ value (C5f) and would falsely empty the system: a future input must not impose it. Both conjugates are covered by working over the field `Q[ρ]/(ρ²−3ρ+1)` (or with ρ as a variable carrying that relation): a certificate `1∈I` over that field conjugates to one for the other embedding, so no nonzero case is discarded, provided no numerical embedding is chosen.

**Common_3 / common_4.** `τ²=μ` or `τ=μ` sets `μ=1` (C6e), fixing `G_3=γ(γπ−1)²`, `G_4=γ³(π−1)²` and the faces `κ³G_k³`, `κ⁵G_k⁵` over Q or Q(ρ). The residual dilation is then `μ_2` or trivial (C6g), so c can no longer be normalized and must remain a free variable with the guard `z·c−1`, exactly as root states. Vertex coefficients `(3,0)`, `(5,0)`, `(9,0)`, `(15,0)` become `κ³`, `κ⁵`, `κ³`, `κ⁵` and need no separate guard.

**Validity as a necessary client.** Every operation used (constant translation, target scaling by the guarded corners, dilation by a root of a guarded nonzero coefficient) is invertible and preserves the polygon supports, the outer faces and the inner-face shapes. Therefore, per polygon case and per κ-branch, over an algebraically closed characteristic-zero field: the normalized guarded system has a point iff the receiver family with forced faces has a point. Direction receiver→normalized uses the K̄ roots `τ¹²=a`, `τ²=μ`, `τ=μ`; direction normalized→receiver is same-field inclusion. Combined with the accepted predecessor implication, an exact exclusion (unit certificate) of all six normalized systems would exclude the hypothesised actual standard F2 pair, conditionally on that chain. CONFIRMED.

**Weaker scope, stated explicitly.**
- The equivalence is of K̄-points. Over Q or Q(ρ) only the inclusion direction is same-field; a Q-receiver point normalizes over `Q(a^{1/12})` or `Q(√μ)`.
- κ∈{1,ρ} is a constraint imported from the source Euler ODE, not derivable from the receiver rows alone. Imposing it keeps the family necessary (it only restricts to the image), but a point of the normalized system says nothing about the source: no reverse polynomial lift, no properness-implies-counterexample.
- The implication remains conditional on the predecessor's hypothesis and external theorems.
- Extra symmetry, optional and not part of the verdict: `N(A)⊆N(B)` in all three cases (C7x), so `B→B+λA` is a further same-field symmetry that could zero one more coefficient of B; it is not needed for validity.

## 6. What a future full input must retain

Counts below are from C7 (lattice minus forced-face points minus origin); they are presentation bookkeeping, not a solving claim.

| case | free A | free B | extra vars | potential rows of `[A,B]−cγ²` |
|---|---|---|---|---|
| unequal | 71 | 196 | 0 | 483 |
| common_3 | 77 | 214 | c, z | 539 |
| common_4 | 98 | 269 | c, z | 659 |

Retain: every lattice point of each closed polygon not on a forced face as an unknown (no monomial dropped); every coefficient row of `[A,B]−cγ²`, all with nonnegative indices and containing `(2,0)` (C7); the full outer faces `H³`, `H⁵` and the full inner faces as explicit substitutions with the constants of §5, for both κ=1 and κ=ρ over `Q[ρ]/(ρ²−3ρ+1)`; origin coefficients set to 0 with the origin nonzero guard **removed**; `z·c−1` in the common cases only; no `c=1` in the unequal case; no irreducibility, no old truncated Moh chart condition. Ring boundary: unknowns in K̄, coefficient field Q or Q(ρ); the maps S, T4, T5 live in `K[x^{±1},y]`, while `U(x,y)=A(x,xy)` is the only polynomial-ring map used.

## 7. Controls and custody

`box/d125-minimal-receiver-gate-fable5-20260906/`: `producer_check.py` (byte-identical to the charged `check.py`), `run_producer.sh`, `producer_runs.txt`, six `.out/.err` pairs; own `gate_controls.py` (SHA `6aac3566…`) and `gate_controls.out` (40 PASS, exit 0). Each command ran under `ulimit -t 25 -v 524288` and `timeout 30`. Producer: normal and `-O` exit 0 with the six counts; `--mutate` and `--mutate-face` exit 1 in both modes; wall 0.03–0.53 s, peak 39 MB. These mutations inject a false expected value into the same verifier and show the equality tests are non-vacuous; they are not data-path mutations of a passing claim. Own script: 4.3 s wall, 60 MB; sympy exact rationals and `√5`, both conjugates explicit; six negative controls (wrong κ, wrong bracket sign, wrong scaling exponent τ^−35, wrong row shift, wrong golden coefficient, T3 for T4) are all rejected (C8). No live positive-face lane, PREP lane, `jc2-lean`, ledger, adapter or FALLACY file was read or edited.
<!-- BODY-END -->
