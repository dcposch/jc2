# SOCLE-GATE check — grok46 — 2026-09-06

**Disposition: the dilation-graded quotient of each of the three augmented characteristic-degree charts is not Artinian, so SOCLE-GATE does not fire.** All three 17(uuuuuuuuu) cells stay **compute-bound OPEN**. Opus's implication “top weight < wt(λ) ⇒ no unit at any truncation” inverts the K16 socle law and is not used. No Hilbert number is claimed for these rings. No new exit-price assertion, so no `charge_basis=` line.

## 0. Custody

Receipt `xmodel/socle-gate-grok46-20260906.run.v2`. Frozen copies in `/tmp/jc2-lane.pHlSOq/inputs`. Manifest built with `awk -F=` pairing numbered `charged_input_<i>_sha256=` and `_basename=`; `sha256sum -c` returned five OK, exit 0, before any input was opened. Digests were not retyped. No other `ideation-*` file was read. No ledger, `jc2-lean`, or fleet. Root had 2.8 GiB free at wake; writes are this report and `xmodel/socle-gate-grok46-20260906.json` only.

## 1. Two gradings (do not mix)

**A. Moh completed-chart bidegree (B,Y) — 17(ppppppp), charged graded-Macaulay.** On the four completed fibres (77/111/129/136 parameters), `deg z=(b,iK−a)`, `deg c=(ℓ+1,D)` with D = n+m−1 ∈ {39,29,41,29}. Exact support theorem:

```text
I_(B,Y)=0  ⇔  B=0  or  Y<λ(B),
λ_77(B)=B,  λ_111(B)=2B,  λ_129(B)=⌈13B/3⌉,  λ_136(B)=⌈B/3⌉.
```

Every generator has B≥1, so I_(0,Y)=0 for all Y. The charge-zero subring of R/I is the ambient polynomial ring on the B=0 coordinates; H_(R/I)(0,D) is 6,734,854 / 411,455 / 11,406,589 / 411,455. **This grading has no finite top weight.** Graded-Moh: setting b>0 and c=0 leaves an affine subspace of dimension D−1. The c-weight is D (second component). These are **not** the three char-degree rings; λ is not a coordinate of them.

**B. Residual dilation of the three augmented charts, where λ is homogeneous.** Action F_α=α^(−n)F(αx,αy), G_α=α^(−m)G(αx,αy), equivalently K(t,z)↦K(t/α,z). Weight of a t^r coefficient is r. Physical leader depth L−D₂ = **143** at (99,66) (L=198, D₂=55) and **153** at D=108 (L=216, D₂=63). Circuit normalizer 6k−2 puts the same rows at 141 / 151. Target scalars a,b,c,d,e₀ at 66,33,99,132,198 for (99,66) and 72,36,108,144,216 for D=108. Jacobian-constant (c-weight analog) sits at n+m−2 = 163 / 178, i.e. 20 / 25 above the leader, matching the T₂ Jacobian-degree bound. Beta=1 spends the residual dilation once.

## 2. Actual generator lists (resume-r2)

Production rings are Q, Singular order **dp** (not a weighted block). I_gr := all emitted rows except the two localizers.

| Chart | stage-0 ring | Q rows | localizers | source residual |
|---|---:|---:|---|---:|
| (99,66) δ=2 | 2912 | 1389 | Z55·leader55−1, Zρ·ρ−1 | 0 |
| (99,66) δ=5/2 | 2910 | 1389 | Z55·leader55−1, Zc·c−1 | 0 |
| D=108 free-mean | 2931 | 1256 | Z63·leader63−1, Zc·c−1 | 0 |

Indexed names A3c_r_p, B2c_r_p, C2c_r_p, C3c_r_p, Hc_r_p, K2c_r_p and graph variables cxH_r_p, … have weight r. **No free t-index-0 coordinate** (t^0 faces are numerical constants after beta=1; the circuit lift skips constants). First t-indices of remaining specials, read off the charged input expressions: (99,66) δ=2: u↦2, ρ and minor_a2↦3, E82↦8; δ=5/2: u↦2, v↦3, c↦7, E82↦8; D=108 free-mean: jet0↦1, jet1↦2, jet2↦3, minor_mean↦4, c↦8. The dilation grading on the residual chart is **positive**. That is the opposite of Moh charge-zero, and it is not a finite-socle statement.

Circuit v2 (`box/char-degree-20260905/d108/coefficient_circuit_backend_v2.py`, SHA-256 `17a825098e24dcbeb973d7fe6f254c6f5884f2aad9bed196e12166db0520ce35`) builds Q by `merge(·,·,shift)` retaining only r+shift ≤ depth with depth=6k−2−D₂. The depressed constant is `q=target_e+…`, merged at shift 6k−2 (196 / 214). 196≰141 and 214≰151, so the q-term is **not a row**. Math-audit: “the positive-degree rows do not determine e0; it is an unused free coordinate, not a missing equation.” Residual strings are empty. Therefore no generator of I_gr involves `target_e`, so k[target_e] injects into R/I_gr. Powers of target_e have weights 198N / 216N, unbounded.

## 3. Hilbert: what was computed, what was not

Singular 4.3.2 is present. A weighted Hilbert series of the production ideals is the same `std` that timed out at 600–1800 s on 2495–2931 generators (17(uuuuuuuuu)); it was not rerun. A Hilbert function is exact only in the declared grading: production scripts use `dp`, which is **not** the dilation `wp` vector on the actual name lists, so even a completed dp basis would not be the dilation socle (FALLACY-v2).

Typed toys, p=32003, `wp`:

- Artinian: R=k[x,y], wt(1,1), I=(x²,xy,y²). dim=0, vdim=3, kbase={1,x,y}, max weight 1. `reduce(y²)=0`, so y²∈I. Weight 2 exceeds the socle ⇒ **membership is forced**.
- Free: R=k[λ,e0], wt(3,5), I=(0). dim=2, vdim=−1. No top weight.

The second toy is the model of I_gr: a free positive-weight coordinate.

## 4. Comparison

| Quantity | (99,66) | D=108 |
|---|---:|---:|
| wt(λ), physical / circuit | 143 / 141 | 153 / 151 |
| wt(target_e), unused | 198 / 196 | 216 / 214 |
| Jacobian-constant depth n+m−2 | 163 | 178 |
| Moh-fibre c-weight D (different rings) | 39, 29, 41, 29 | same four fibres |

wt(λ) < wt(target_e) and wt(λ) < Jacobian depth. There is no finite top weight in grading B to compare with 143/153. In grading A the charge-zero Hilbert is infinite and c has weight D, not 143.

## 5. FALLACY-v2

**A Hilbert bound is exact only for the declared grading.** Transferring 17(ppppppp) support numbers, a dp kbase, or a K16 socle table onto these dilation charts is not a bound.

K16 (17(oooooo)): if wt(f) exceeds the socle of an Artinian quotient, then f already lies in the ideal (degree-forced membership). Opus wrote the opposite: top < wt(λ) ⇒ λ^N∉I for all N. The toy of §3 falsifies that. Had the dilation quotient been Artinian with socle < 143, the correct reading would be λ∈I, hence **UNIT at N=1**, not “no unit”. Setting target_e=0 is a specialization, not a chart isomorphism (graded-Moh). Homogeneity of I_gr was checked on the emitter's merge/jet, not by expanding 10 MB scripts. The two dropped localizers are inhomogeneous (ρ has weight 3, c has weight 7 or 8; Zλ−1 mixes weight 143 with 0).

## 6. Verdict per chart

I_gr = graded chart (localizers dropped). Top weight = max degree of R/I_gr in the dilation grading.

| Chart | Finite top weight in the λ-grading? | vs 143/153 | vs c-weight | Verdict |
|---|---|---|---|---|
| (99,66) δ=2 | No: k[target_e]⊂R/I_gr, wt(e₀)=198 | ∞ > 143 | ∞ vs 163 / vs Moh D | **not decidable this way** |
| (99,66) δ=5/2 | No: same, wt(e₀)=198 | ∞ > 143 | same | **not decidable this way** |
| D=108 repaired free-mean | No: k[target_e]⊂R/I_gr, wt(e₀)=216 | ∞ > 153 | ∞ vs 178 / vs Moh D | **not decidable this way** |

Why not Artinian: the dilation grading is positive (no t=0 free coordinate after beta=1) **and** still has an unused polynomial direction of weight 198/216. That is not the Moh charge-zero subring, which is a different grading on different rings and is likewise non-Artinian. Neither grading supplies a socle to cut off λ-powers.

The three compute-bound verdicts of 17(uuuuuuuuu) are **not** converted to “no unit at any truncation”. A unit remains possible at weight N·143 / N·153 for some N; this lane does not produce one and does not forbid one. The first weight at which λ^N could lie in I_gr is 143 / 153 (N=1), but that is the tautological degree of the leader row, not a computed w₀ from a finite socle, so it is not typed UNIT-POSSIBLE-FROM-WEIGHT.

```text
OPEN[SOCLE-GATE-NON-ARTINIAN]
  QUANTITY: dilation-graded R/I_gr for the three augmented charts.
  STATUS: not Artinian (target_e unused, weight 198/216); SOCLE-GATE does not
    decide 17(uuuuuuuuu). Opus's “top<wt(λ) ⇒ no unit” is the K16 implication
    run backwards.
  CHEAPEST TEST: replay merge(qt,'1',6*k-2) against depth=6k-2-D2
    (196>141, 214>151); Singular vdim on k[e0] with I=0 is -1.
  BLAST RADIUS: stops a false “all truncations vacuous” closeout; 0 row kills.
```

<!-- BODY-END -->
