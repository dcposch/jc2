# Gate: mixed-order finite boundary jet is a counter-control, not a survivor (Fable 5.1, 2026-09-07)

Bounded 10-minute hostile gate of `xmodel/d125-generic-ramification-discriminator-astra-20260907.md` (frozen SHA `a7b37d6e…`, whole text read) with its `check.py` (`77e94ad9…`) and `witness.json` (`24a90700…`, matching the report's quoted digest), read from `/tmp/jc2-lane.WTIwVE/inputs` only, beside the five charged prior gates and `FALLACY-v2.md`. The producer's helper-dependent checker was not executed; every number below comes from own stdlib controls in `box/d125-mixed-order-countercontrol-gate-fable5-20260907/`.

| Claim | Verdict |
|---|---|
| 1. Identities `[A,B]=sʲR²[R,Z]+s²ʲ[U,V]` and the corrected second identity; centralizer, low e and whole shear give only `U²∈(R,sʲ)`, hence `s^⌈j/2⌉` divisibility mod the squarefree special R, not `U∈(R,sʲ)`; moving `R_{t(s)}` is a reference, not an automorphism | **CONFIRMED** (centralizer lifting is the already-charged external trust) |
| 2. Independent toy `A*=R³+9s²RS²+9s³S³`, `B*=R⁵+15s²R³S²+15s³R²S³+45s⁴RS⁴+90s⁵S⁵` has exact bracket `2835s⁷S⁶` | **CONFIRMED** |
| 3. Substituting the actual degree-5 `R_t` and degree-3 `S=∂ₜR_t` gives a genuine whole unguarded k=0 source jet mod s⁷ by factored degrees/weights, never expanding `R³`,`R⁵` | **CONFIRMED** for every row family the charged classification gate inventories; t=−3 is inside the jet's scope but outside the recentering (§3) |
| 4. Recentering leaves `F₂=9RS²−(9/h)R²S`, not boundary-tangent; `x=[gp²]A≡0`, so no k=s⁴ saturated survivor and no guarded point; exact nonzero order-7 obstruction; no full arc, no all-m exclusion | **CONFIRMED** |

## 1. Identities and what they leave free (claim 1)

Own C1 checks identity (1) with four random 4-term polynomials R,U,V in (x,y,s) at j=2, and identity (2) after setting `V=(sʲW+5R²U)/3`, which is the corrected form: `[R,R²W−(5/3)RU²]+(sʲ/3)[U,W]=s⁻²ʲ[A,B]`. Both hold exactly. The producer's route to `U²∈(R,sʲ)` uses the imported centralizer `K[R_{t₀}]` and coefficientwise lifting, the same external trust charged in the two-jet packet; nothing new is imported. The reduced-special-fibre step is sound: if `Ū=s^aŪ_a+…` with `Ū_a≠0` mod (R,s), then `Ū_a²≠0` in the reduced ring `K[g,p]/(R₀)`, so `2a≥j`. That is exactly `⌈j/2⌉`, and it is sharp at j=2: on the toy, own C2 finds `U mod R = 9sS³`, divisible by `s¹` only, while `U² mod R = 81s²S⁶ ∈ (R,s²)`. So `U∈(R,sʲ)` is false and the m=2 tangent argument cannot be transported by `s↦sʲ`.

`R_t` is affine-linear in t, so `R_{t(s)}=R_t+(t(s)−t)·S` exactly; writing A against it is a change of reference. The same-field `t(s)` exists uniquely only for `h=t+3≠0`, since each step divides by `3h²`.

## 2. Toy bracket (claim 2)

Own C2, independent variables R,S,s, Fractions, no helper: `[A*,B*]_{(R,S)}={(0,6,7):2835}` exactly, nothing below order 7. `Z=3V−5R²U=s²(135RS⁴+270sS⁵)` vanishes mod s² as claimed, and identity (2) reproduces the same bracket on the toy. `(5/9)D²−(5/81)C³=0` at `C=9S²`, `D=9S³`. Mutation `--mutate-drop-mixed-orders` (delete the s³ and s⁵ terms) fails first at "bracket nonzero below order seven", as the producer says.

## 3. Whole-source membership without expansion (claim 3)

Own C3 on the literal generators in (g,p,h), t=h−3: `S=∂ₜR_t` exactly; support statistics (degree, max 5i−7j, max i−2j, min p-power, odd) are `(5,1,−1,1,odd)` for R and `(3,−7,−2,1,odd)` for S; the degree-5 part of R is exactly H and its weight-1 part is exactly `g³p²`, so the fixed faces `A₁₅=H³`, `B₂₅=H⁵`, `[g⁹p⁶]A=1`, `[g¹⁵p¹⁰]B=1` come from the pure powers alone. Under `g↦v⁻¹`, `p↦v⁴u−v−v⁻¹` both generators have minimum v-exponent ≥0, so every product term lifts ordinarily. The factored table (R-power, S-power, s-order, degree, weight, lower bound, p-valuation) reproduces the producer's witness: A corrections have degree ≤11 and weight ≤−13 against faces 15 and 3; B corrections degree ≤21 and weight ≤−11 against 25 and 5; all terms odd, p³ | A, p⁵ | B. Against the classification gate's row inventory (lattice `i+j≤15, 5i−7j≤3` and `i+j≤25, 5i−7j≤5`, outer-face zeros, inner-face slots `(2,1),(9,6)` and `(1,0),(8,5),(15,10)`, origin, negative lift rows, Jacobian) every family is satisfied through order 6 with k=0, and the low slots `[p]A`, `[gp²]A`, `[g²p]A` are zero by p³-divisibility. The jet is t-free in all support and lift rows, so it exists at t=−3 too; only the unit `y₀` and the recentering are generic.

## 4. Recentering, survivor status, obstruction (claim 4)

Own C4 with independent R,S, a Laurent variable h and `t(s)=t+(3/h)s²+(3/h²)s³`: `(h+t(s)−t)³ ≡ h³+9hs²+9s³` mod s⁴, matching `y(s)=−h³−9hs²−9s³` whose coefficients own C3 derives from `[p³](RS²)=−h` and `[p³](R²S)=−h²` (degree ≤13 products only); `F=A−R_{t(s)}³` starts at s² with `F₂=9RS²−(9/h)R²S` exactly. On the actual generators at h=3,1,−2: `F₂≠0`, `[p]F₂=[p³]F₂=[gp²]F₂=0`, `[p]R=−h` forces c=0 in `cR+dR²S`, and `F₂` is not proportional to `R²S`; `hS−R=3p³−H` holds symbolically. So the first motion is not a boundary tangent in the two-jet sense, and the unrestricted extension of that lemma is refuted at j=2.

`x=[gp²]A` is identically zero because p divides both generators. Mutation `--mutate-guarded-s4-survivor` fails at `0≠−81` (h=3). At h=0 the relation `x₂²=−3h³` is vacuous, which is one more reason the producer's t=−3 exclusion from the argument is the correct scope. The obstruction is exact: `[A,B]=2835s⁷S⁶[R_t,S]` by the chain rule (own instance `[R²,S]=2R[R,S]` verified), `[R_t,S]` is a nonzero polynomial with value 14 at g=p=1, t=0, and S(1,1)=1. Mutation `--mutate-full-arc-claim` fails at "finite toy is not a full commuting arc".

## 5. Custody and gaps

Own `gate_controls.py` (SHA `aecf4c76…`, stdlib only, zero Assert nodes, `-B` and `sys.dont_write_bytecode` before any import, RLIMIT 25 CPU s / 512 MiB per subprocess, 30 s wall): eight runs, four modes × normal/−O, positive witnesses byte-identical (`witness.json` SHA `fb60a47b…`), each mutation recorded by its first failing gate in `replay.json`. Positive run 0.08 s. No frozen file was modified; no `R³`, `R⁵`, degree-15/25 or full-jet expansion; no CAS, AWS, SSH, solver or peers.

Typed gaps, none charged to the producer: **GAP-CENTRALIZER** the K[R] centralizer and its s-adic lifting remain the external trust already declared upstream. **GAP-ROWLIST** the "whole source" verdict is against the row inventory recorded in the charged classification gate, not against the client file, which is not in the frozen inputs. **GAP-T=-3** the recentering and the unit `y₀` are generic-only, as the producer states. No exit-price assertion is made, so no `charge_basis` line. **STOP** after this gate.

<!-- BODY-END -->
