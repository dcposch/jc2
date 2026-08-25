# Hostile different-model review — corrected Q8 normalization, norm, Taylor, and terminal jet

| Field | Value |
|---|---|
| Claim under review | Frozen producer: the corrected `Q8` non-parity formal branch, in the reviewed seven-row `k=mu=0, nu!=0` fibre with parameter `t=a0`, has even/cubic lowest jet with all displayed coefficients units of `E=Q[v]/(Q8)`; `v-v0` and `r8-rho0` have unit quadratic coefficients; in the reviewed root-free critical-value norm the node is in leaf 3 and the punctured branch in leaf 4 (`E/t` a unit); both original Taylor families are reconstructed at the true center `r=A/9`; the retained terminal row `9*r8'=j/u` forbids an actual trajectory on this component from meeting the node above a finite `x`-place; at infinity only the necessary condition `deg(h)=3*(2e+1)` follows |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none found |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking inventory below) |
| Evidence tier | hand re-derivation of the mod-7 reduction, root scan, Rabin logic, and Gauss lift; hand chart inversion for `V2`; affine-linearity proof licensing the finite-difference jet solve; involution/Kummer character audit; hand expansion of the general-`nu` leaf quadratic and scaling covariance; exact hand `u`-algebra from the pinned compiler's terminal descent to `9*r8'=j/u`; complete valuation case analysis (finite, ramified, fractional, infinity); line-by-line audit of `replay.py` against the frozen `replay.json`; textual cross-verification of the full hash-pin web against both pinned Grok parent reviews |
| Reviewer / model | Claude (Fable 5, Anthropic). Different model family from the producer (OpenAI Codex, GPT-5 family) and from the parent reviewer (Grok 4.6, xAI) |
| Repo | `/Users/dc/code/math/jc2` |
| Charged hashes | report `739fbad475bc10540756c7a0180168185523f6e3cfe368225e03efa1abe62d65`, manifest `036b8656ba53dd3b1b212b2bf5bec6d0eed83f8a56023cf3ebf0b689156d8971`, freeze `807ad9dacbc477972c3c30b3770d84ca27340b5771ec2aad3efc90d7eb3e5b50` |
| Execution disclosure | **This review session had no shell** (Bash absent; Monitor denied by policy). The registered replay was not executed by this reviewer and no byte hash was recomputed here. Per repo protocol for shell-less sessions the verdict rests on hand algebra plus the frozen attestations, with the execution gap disclosed and machine checks staged for the producer at `/tmp/q8jet_review_claude_replay.sh` (charged hashes, manifest, replay diff) and `/tmp/q8jet_review_claude_probe.py` (independent-path reconstruction: fresh field/series/linear-algebra code, Cramer tangent, fresh Gauss jet, leaf quantities, all 23 Taylor digests, fresh Rabin) |

Read in full before any verdict: the producer report; all six case files (`README.md`, `REGISTRATION.md`, `replay.py`, `replay.json`, `MANIFEST.sha256`, `FREEZE.txt`); the pinned parents `xmodel/max12-912-order3-nu-q8-formal-branch-20260824.md` with its Grok review, `xmodel/max12-912-order3-critical-value-norm-20260824.md` with its Grok review, `cases/max12_912_order3_fibre_20260824/order3_fibre.py`, and the helper layer of `cases/max12_912_order3_nu_parity_genus5_20260824/replay.py`. The quarantined Q12 package was not read and is not consumed. The already-present successor report (`leaf4-descent-jet`) was not consumed. No producer, case, canonical, coordination, prompt, log, run, or other review file was edited.

---

## Promotion

**Accept `THE CORRECTED Q8 BRANCH HAS A UNIT-COEFFICIENT EVEN/CUBIC LOWEST JET, ITS NODE IS IN NORM LEAF 3 AND ITS PUNCTURED BRANCH IN LEAF 4, BOTH TAYLOR FAMILIES ARE RETAINED AT r=A/9, AND THE TERMINAL ROW FORBIDS FINITE-PLACE NODE CONTACT FOR AN ACTUAL TRAJECTORY ON THIS COMPONENT` at the stated scopes.**

**Do not promote this to:** exclusion of the punctured leaf-4 branch; a global normalization, algebraization, or rational Keller trajectory; any infinity exclusion; Kummer descent of the branch itself; all-`(9,12)`; maximum twelve; a counterexample; or JC2. The report, registration, README, FREEZE scope block, and replay payload all refuse these, and the refusals are accurate.

---

## Attack ledger (charged points 1–7)

| # | Charged attack | Result |
|---|---|---|
| 1 | `Q8` irreducibility over `Q`; unit inferences | **holds** — hand-verified reduction and lift; Rabin logic correct; units follow from `E` being a field |
| 2 | seven-row fibre, `t=a0`, cubic/even jet, unit `r8` quadratic | **holds** — base on fibre live-asserted; equivariant jet shape licensed by the reviewed parent; finite-difference solve exact by affine-linearity; `rho2`, `V2` unit-certified |
| 3 | node in leaf 3, `E/t` unit, branch in leaf 4 | **holds** — `E=0` at the node is exact (parity kills `F1,G1`), asserted not assumed; `s0`, `nW0`, `nF0`, `e1` units; leaf Booleans scaling-invariant |
| 4 | localization/scaling; `p0`; `nu` constant; formal-vs-trajectory firewall | **holds** — weight algebra hand-verified; `nu` constancy is the charged landing row frozen in the pinned compiler; firewalls present and accurate |
| 5 | 23 Taylor members at `r=A/9`; `z=0` negative control | **holds** — pure Taylor calculus; families hashed; control machine-checked; constraints retained, not exploited |
| 6 | provenance of `9*r8'=j/u`; jet differentiation; finite-place contradiction | **holds** — row derived exactly from the pinned compiler's `r8=u^2*R`, `9hR'+6h'R=j`; contradiction robust to cancellation, ramification, fractional valuations, `p0/v0` variation, and omitted higher terms |
| 7 | infinity only necessary; no global claim | **holds** — one order-matching equation, correctly not an exclusion; scope firewalls verified |

---

## 1. `Q8` irreducibility and unit inferences

Hand reduction of `(24,296,1548,4428,7320,6498,1782,-1539,-999)` mod `7` gives ascending `(3,2,1,4,5,2,4,1,2)`; multiplying by `4=2^{-1}` gives the monic `[5,1,4,2,6,1,2,4,1]`, exactly the replay constant and the displayed `v^8+4v^7+2v^6+v^5+6v^4+2v^3+4v^2+v+5`. A hand root scan at `v=0..6` gives values `5,5,6,3,2,2,3` — no root, consistent with (and implied by) the gcd half of the certificate. The Rabin logic is correct for `n=8` with sole prime divisor `2`: `x^{7^8}≡x mod Q8` forces every irreducible factor degree to divide `8` (and forces squarefreeness), and `gcd(Q8,x^{7^4}-x)=1` kills degrees `1,2,4`, leaving only `8`. The lift to `Q` needs two side conditions the report leaves tacit, and both hold: `Q8` is primitive (`gcd(999,296)=37`-free: `999=3^3·37`, `296=2^3·37`, `gcd(37,24)=1`, content `1`) and the mod-7 degree is preserved (`999≡5`). Gauss then gives irreducibility over `Z`, hence `Q`. The `fp_*` implementation in `replay.py` is a correct dense `F_7[x]` layer by inspection.

Unit inferences: `E` is a field, so nonzero ⟺ unit; `digest`'s `gcd(·,Q8)=1` test is exactly nonvanishing of the reduced representative, which (with `Q8` irreducible) is nonvanishing at every one of the eight conjugate contacts. The `NF` extended-Euclid inverse maintains the Bézout invariant and is correct.

## 2. Fibre, parameter, jet

The compiler's ring is `(a0..a7,k)`; the ninth slot of `base` and `make_series` is `k≡0` — the order-three `k=mu=0` landing, matching (1.1) of the reviewed parent. The base is the genuine corrected chart at `p=1`: `x5=-36v^2A2/D`, `x3=x5(v+2)`, `x1=x5(v+1)+x5^2(3v+1)/(9v)` — the `1+3v` numerator, not the quarantined constant; as a cross-check, the reviewed chart identity `A=x3-2px5` gives `A=x5·v` at `p=1`, so `v=A/(px5)` is consistent. Rows `r1..r5,r7` are asserted to vanish at the base **live over `E`** (i.e. simultaneously at the generic `Q8` root); `r6=nu`, `r8=rho0` are values, both units. The parameter `t=a0` is involution-odd (`a_i↦(-1)^{i+1}a_i`, reviewed parent) and Kummer-fixed (`wt(a_i)=-i mod 3`, live-checked inside the pinned compiler), exactly as the payload records.

Tangent: the `3×3` solve against the reviewed unit minor, then the live assertion that all four odd rows annihilate `n1=(1,c2,c4,c6)` — this re-proves at runtime that `det(J_N)` vanishes at the generic `Q8` root, an independent confirmation of the erratum determinant's `Q8` factor.

Jet: with odd coordinates odd in `t` and even coordinates even in `t` — the shape forced by the reviewed equivariant normal form, so imposing it loses nothing — every tail becomes an odd/even series according to its character, so the `t^0,t^1` asserts plus the solved `t^2` (even rows) and `t^3` (odd rows) coefficients exhaust all conditions through `t^3`. Through this truncation the seven equations are **exactly affine-linear** in the seven unknowns (any unknown×unknown product lands in `t^{≥4}`), so the finite-difference matrix construction is exact, not an approximation. The system solves uniquely (Gauss-Jordan raises on singularity), and the true branch jet is a solution of the same affine system, so the computed jet **is** the branch jet in the canonical `t=a0` parameterization. `nu` is constant through `t^3` (asserted), `r8`'s odd coefficients vanish (asserted, matching its even character), `rho2` and `V2` are asserted units; the `V2` formula `x3_2/x5-(v+2)(p2+x5_2/x5)` is the hand-inverted chart relation `v+2=x3/(px5)`. The twelve residue digests and ten coefficient digests are frozen with `unit_mod_Q8: true`, enforced by the diff protocol.

## 3. Norm leaf typing

`s=-p/3-10r8/(9nu)` is exactly the reviewed general-`nu` quadratic: `B=54nu·z^2+18nu·p+60r8` (norm review, claim 2, with `a7=3p`) gives `B/(54nu)=z^2-s`. The reduction/power/norm code in the quadratic algebra is a correct implementation of the reviewed pair calculus (`E=G0F1-G1F0`, `Norm(W)=W0^2-sW1^2`, `Norm(F)=F0^2-sF1^2`), applied to the generic `k=0` Faber pair with the jet substituted. At the node `f` is odd and `g` even, so `F1=G1=0` and `E=0` **exactly**; the replay asserts this rather than assuming it. `s0`, `nW0`, `nF0` are asserted units, so the node satisfies `s·Norm(F)·Norm(W)≠0`, `E=0`: reviewed leaf 3. Along the branch `E` is an odd series (frozen pattern `0,unit,0,unit`), `e1` is a unit with a certified inverse — the two displayed certificate hashes match the frozen `E_series[1]` and `E_lead_inverse_mod_Q8` — so `E/t` is a unit of `E[[t]]` and the punctured branch has all four quantities nonzero: reviewed leaf 4. The typing at general `nu∈E^*` is legitimate: embed `E→C` at any of the eight roots (the gcd certificates make every quantity nonzero at all of them) and rescale by `lambda^{18}=1/nu` (weights `nu:18`, `r8:20`, `a7:2`, verified in the reviewed norm claim 1); the leaf Booleans are invariant. This is formal-local typing only, and the report says so.

## 4. Localization, scaling, firewall

Restoring `p0`: the weighted action `wt(p,a0,r8,v)=(2,9,20,0)` is cross-consistent with both parent reviews and with every chart formula (`x5:4`, `x3:6`, `x1:8`, `r6:18`). Taking `lambda^2=p0` maps the normalized branch to the branch through the general node, and `lambda^{18}R6(v0)=p0^9R6(v0)=nu` pins `p0^9` from constants (`v0` an algebraic constant, `R6(v0)≠0` reviewed, `nu≠0`). The scaled expansion is exactly (5.2): `lambda^{20}rho0=p0^{10}R8(v0)`, `lambda^{20}·C·lambda^{-18}=p0·C(v0)`, and the `O(a0^4)` coefficient scales by the constant `p0^{-8}`. `nu` differential-constant is the charged landing row, frozen verbatim in the pinned compiler output (`constant_rows=r1=r2=r4=r5=r7=0;r3=mu;r6=nu`); the report's clause "which the seven equations keep differential-constant" is a compression of that charged statement (non-blocking remark 3). The formal-fibre/actual-trajectory distinction is maintained at the end of §2, §3, and §4, and §5's conclusion is drawn only under the explicit hypothesis of an actual trajectory **on this formal component**; a trajectory germ through the node lies in one of the two reduced branches (reviewed two-branch structure), and the parity alternative is a parity trajectory, which this report does not need and does not smuggle in.

## 5. Taylor reconstruction

(4.2) is Taylor's theorem for `z=uy+r` — `[y^ell]P=u^ell f^{(ell)}(r)/ell!` — and `taylor_family` implements `sum_d C(d,ell)c_d r^{d-ell}` exactly; all `10+13=23` members are reconstructed in `E[r][[t]]/(t^4)` and hashed (the two singleton top members share the digest of `"0,0,0,1/1"`, as they must). The center `r=A/9` is the standard depression shift: eliminating the `z^8` term of a monic degree-9 depression gives `r=c8·u/(9c9)`, so `r/u=c8/(9c9)∈C(x)` as charged, and the Kummer bookkeeping closes (`z` and `r` of character `omega`, `a_i` of character `omega^{-i}`, matching the compiler's live weight check). The negative control (4.4) is trivially true for monic `f,g` and is machine-asserted; its force is exactly what the report claims: `f(0),g(0)` are not the boundary values unless `r=0` is separately proven, which is nowhere assumed. (4.5) is correctly scoped as a `t=0` spectral-center control (`f(0)=0`, `f_z(0)`, `g(0)` units, `gcd(f,f_z)=gcd(f,g)=1`, all live-asserted over `E`). The polynomiality constraints on the 23 members are retained and correctly **not** used for a local contradiction, since `u(x),r(x),t(x)` are not reconstructed.

## 6. Terminal row and the finite-place contradiction

Provenance: the pinned compiler's frozen terminal descent is `r8=u^2·R` with `9hR'+6h'R=j`. With `u^3=h`, `u'=h'/(3u^2)`, hence `9(u^2R)'=18uu'R+9u^2R'=(6h'R+9hR')/u=j/u`. So (5.1) is **exactly** the charged row, with no drift; `j∈C^*` is the Keller constant. Differentiating (5.2): `r8` restricted to the branch is an even series in `a0` to **all** orders (an invariant function on an involution-stable branch with anti-invariant parameter — reviewed equivariance), so `9r8'=18p0C(v0)a0a0'+sum_{k≥2}9·2k·c_{2k}a0^{2k-1}a0'`, and the term orders `2ke-1` are strictly increasing in `k`. At a finite `x`-place where a trajectory on this component meets the node: `a0` is Kummer-fixed, hence in `C(x)`, so `e=ord(a0)` is a positive integer (`a0≢0` since the branch is punctured; `a0` nonconstant since it vanishes at the place), `ord(a0')=e-1` exactly in characteristic zero, and `ord(LHS)=2e-1≥1` exactly, since `18p0C(v0)≠0`. On the right, `h` is a polynomial, so at a finite place `w(u)=m/3≥0` and `w(j/u)=-m/3≤0`. The sides cannot agree. Every charged escape fails: **cancellation** — impossible, the orders `2ke-1` are distinct with a unique minimum; **ramification** — on any cover place of index `rho`, the comparison becomes `rho(2e-1)≥1>0≥-rho·m/3`, unchanged; **fractional valuations** — only `u` can be fractional; if `m∉3Z` the sides differ by integrality alone, if `m∈3Z` by sign; **variation of `p0` or `v0`** — both are constants at the contact (`nu` constant by the landing, `v0` a root of `Q8`, `p0^9=nu/R6(v0)`), so (5.2) has constant coefficients; **omitted higher terms** — bounded by `O(a0^3a0')` of order `≥4e-1>2e-1`. The conclusion is correctly restricted to trajectories on this formal component and to finite places.

## 7. Infinity and scope

At infinity, if `a0` vanishes to order `e>0` in `1/x`, then `ord_∞(a0a0')=2e+1` (differentiation raises the infinity order by one) while `ord_∞(j/u)=deg(h)/3`; matching orders gives `deg(h)=3(2e+1)` — one necessary equation, (5.4). No contradiction arises, leading coefficients are unconstrained, and the scenario `a0` not vanishing at infinity is not covered; the report correctly labels this "not an infinity exclusion". No global algebraization, rationality, punctured-branch exclusion, all-`(9,12)`, maximum-twelve, counterexample, or JC2 conclusion is drawn anywhere in the report, registration, README, FREEZE scope block, or payload scope string.

---

## Replay, hashes, and the identity/interpretation split

Not executed here (disclosed above); staged at `/tmp/q8jet_review_claude_replay.sh` and `/tmp/q8jet_review_claude_probe.py`. What was verified without a shell: the prompt's report and manifest hashes match `FREEZE.txt`; `MANIFEST.sha256`'s five lines match `FREEZE.txt`'s five payload hashes; `replay.py`'s eight dependency pins match `replay.json`'s `dependency_sha256` block **and** match, digit for digit, the hashes computed independently by the two pinned Grok reviews at their close (compiler `a4fdac…`, genus5 replay `c965bb…`, Q8-formal replay/report `a55cfc…`/`37ce84…`, norm report/review/replay `733947…`/`b6ae95…`/`88f4e2…`) and the genus5 replay's own internal compiler pin. Five independently produced frozen documents agree; the only byte not textually cross-attested is `FREEZE.txt`'s own hash `807ad9…`, which appears in the prompt alone.

Checked by replay (frozen + asserts): the Rabin certificate; base-on-fibre; kernel residuals; the seven-row jet solve and residual; evenness/constancy patterns of `nu`, `r8`, `E`; unit certificates for `rho2`, `V2`, `e1` (with inverse), `s0`, `nW0`, `nF0`, `x1`, `g(0)`; both gcds at `t=0`; all 23 Taylor digests; the twelve residue digests. Interpretive deductions (all correctly scoped): the Gauss lift to `Q`; jet-equals-branch-jet (parent uniqueness + equivariance); all-orders evenness of `r8|branch`; leaf typing at general `nu` via scaling; restoring `p0`; trajectory-germ-in-branch; the finite-place valuation contradiction; the infinity necessity.

## Attacks that do not land

- **Q12 inheritance.** The dependency table pins no Q12 artifact; the chart uses the genuine `(3v+1)/(9v)`; the residual is the erratum octic. Verified at source level.
- **Finite differences as approximation.** Exact by affine-linearity through `t^3`.
- **Unchecked odd/even coefficients of the rows.** Forced to vanish identically by the character structure under the equivariant substitution.
- **Leaf typing spoiled by higher-order terms.** Constant terms of `s`, `Norm(F)`, `Norm(W)` and the linear term of `E` are units; no higher term can restore vanishing.
- **`nu=1` normalization illegitimate over `E`.** Not performed; the quantities are computed at general `nu` and the Boolean pattern is scaling- and embedding-invariant.
- **`e` fractional.** Blocked by the Kummer-fixedness of `a0`, live-checked in the pinned compiler's weight audit.
- **`z=0` boundary relapse.** The families are kept at formal `r`; the monic negative control is asserted; (4.5) is labelled a control and never substituted.

## Non-blocking remarks

1. The order-three fibre compiler still has no completed different-model review (standing caveat in both pinned parent reviews). It matters more here than before: the terminal row `(5.1)` — used differentially for the first time — and the eight tails are consumed from it. The tails are digest-matched by an independent Grok reconstruction; the terminal row is consumed as the frozen charged equation `r8=u^2R`, `9hR'+6h'R=j`, whose `u`-algebra to `9r8'=j/u` is exact. A dedicated review of the terminal descent's derivation is the right hygiene before any successor leans on (5.1) at infinity.
2. `order3_fibre.py` verifies its upstream pins (including `shared_faber_probe.py`) only inside `main()`; imported as a module by this replay, the shared Faber engine is loaded without a load-time hash gate. Tampering would be caught only by output divergence under the diff protocol. Recommend adding the gate to the next compiler freeze.
3. "`nu=r6`, which the seven equations keep differential-constant" compresses the charged landing statement (the differential constancy is the landing's row ledger, frozen in the compiler output), not a consequence of the fibre equations themselves.
4. The report's Gauss lift leaves primitivity and mod-7 degree preservation tacit; both hold (content `1`; `999≡5 mod 7`).
5. The unit flags on the ten (2.1) coefficient digests are enforced by the frozen diff rather than in-process asserts; adequate under the replay protocol.
6. This session's execution gap is disclosed in the header; the staged scripts make every machine-checkable statement here replayable by the producer.

## What this does not license

No emptiness or existence for the punctured leaf-4 branch; no global normalization, algebraization, or rational trajectory; no infinity exclusion; no Kummer descent of the branch; no all-`(9,12)`, maximum-twelve, counterexample, or JC2 conclusion; no promotion of the unreviewed compiler beyond its frozen-engine role.

---

**Verdict.** `CONFIRMED`
