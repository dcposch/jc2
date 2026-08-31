# AS109 / degree-12 seed provenance reconciliation

Lane: preflight, disproof side. Desk-scale exact reasoning only.
Scope: reconcile what artifacts *call* "AS109" or a "degree-12 disproof seed".
This report does not evaluate whether any seed threatens JC2.

## 0. Hash verification of frozen charged inputs

Frozen copies under `/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.nmrPpU/inputs` were hashed with SHA-256 (`shasum -a 256`). All three match the charged values. Proceed.

| expected | observed | file |
|---|---|---|
| `7bf7502e43a6bdd344b1c177cf3c2e83afd9ca464b7aeab451b96e6db7528b46` | match | `ideation-20260831T1033Z-sol56.md` |
| `329182487ac3e771be9aa73ded7b9f21c6ea3fd8e13235caafb8e103c96007a3` | match | `ideation-20260831T1033Z-grok46.md` |
| `426c7305fc215a3d55ef6a1d429f66c22071ac442384d6ca3d151b9d9029fad2` | match | `ideation-20260831T1033Z-crosspoll-sol56.md` |

Workspace copies of the same filenames were not used as authority. Citations below to those three charged files refer to the frozen copies. Historical `xmodel/as109-*-20260824*.md` files and later `as109` mentions were read in place, read-only.

## 1. Method and non-goals

Read-only desk comparison of the three frozen charged inputs, the tracked `xmodel/as109-*-20260824*.md` producers/reviews, later `as109` files and ideation mentions, and the F_3/Witt defining notes that those texts cite. No CAS, no uncertain-duration computation, no inspection of `jc2-lean`, no edit of canonical ledgers or charged files.

A *seed* here is any object an artifact names “AS109”, an Artin–Schreier collision used as a disproof seed, or a “degree-12” / “maximum-twelve” disproof cell. Matching labels (“AS”, “109”, “degree 12”) are not a ring map. UNSTATED is recorded rather than filled by family resemblance. This report does not ask whether any seed threatens JC2.

Later-ideation `as109` mentions that only rerank the lane, without new equations, are not extra seeds.

## 2. Definitive seed registry

Eight distinct objects. R6 is a theorem about R5, not a second special fibre. R7 is Sol’s proposed matrix cell and is not yet a seed.

### R1. `AS3-FIBRE` — special fibre over `F_3`

- **Also called.** Smallest typed odd-prime Artin–Schreier cap `AS3-MIN-W2`; Grok’s “typed `F_3` Artin–Schreier collision” at charged `ideation-20260831T1033Z-grok46.md:93–94`; `APPROACHES.md:208,275`.
- **Coefficient ring.** `F_3`. Stated: `cases/round2_witt_oddprime/PREREGISTRATION.md:39–43`; `xmodel/round2-witt-oddprime-20260824.md:11–16`.
- **Equations.** Over `F_3`, `P_a=x+a x^3`, `Q=y`, `a=1,2`; survivor `a=2` is `F=(x+2x^3,y)=(x-x^3,y)`. Jacobian one, generic degree three. Stated: preregistration `39–56`; oddprime report `11–20`. Schema `F_AS=(x-x^p,y)` at `p=3`: preregistration `13–14`.
- **`x` support.** `S_P={(1,0),(3,0)}`. Stated: preregistration `29–31`.
- **`y` support.** `S_Q={(0,1)}` (exact `y`-degree 1). Stated: preregistration `29–31`.
- **Generator order.** Enumeration order `a=1,2`. Stated: preregistration `39–41`. Polynomial monomial order: UNSTATED.
- **Gauge.** UNSTATED at this cap.
- **Collision.** Marked sources `r_0=(0,0)`, `r_1=(1,0)` to target `c=(0,0)`. Stated: preregistration `47–49`; oddprime report `17–20`.

### R2. `AS3-W2` — first Witt digit over `W_2(F_3)=Z/9`

- **Also called.** `W2-SURVIVOR`. Distinct from R1: AUDIT records the displayed correction already enlarges support (`AUDIT.md:10633–10638`).
- **Coefficient ring.** `W_2(F_3)=Z/9`. Stated: oddprime report `23–27`; `AUDIT.md:10628–10631`.
- **Equations.** Teichmüller `[2]=8`; `P̃=x+8x^3`, `Q̃=y`; obstruction `E=2x^2` in `F_3`; corrections `A=0`, `B=x^2 y`; lift `P_2=x+8x^3`, `Q_2=y+3x^2 y` with integer determinant `1+27x^2+72x^4`, hence `1 mod 9`. Stated: oddprime report `23–50`; `AUDIT.md:10628–10631`.
- **`x` support.** `P`: `{(1,0),(3,0)}`; `Q` gains `{(2,1)}`. Stated: oddprime report `43–50`.
- **`y` support.** `Q` still `y`-degree 1 (`y` and `x^2 y`). Stated: oddprime report `43–50`.
- **Generator order.** UNSTATED beyond the preregistered `a`-order.
- **Gauge.** UNSTATED.
- **Collision.** Same marked pair persists. Stated: oddprime report `17–20`; `AUDIT.md:10626–10631`.
- **Not shown.** No `W_3`, no bounded-support all-Witt tower, no `Z_3` or characteristic-zero polynomial lift (`AUDIT.md:10636–10638`).

### R3. `TATE-p` — growing-support all-Witt / cotangent control

- **Also called.** Unrestricted-support all-Witt Artin–Schreier control; rational cotangent `C_p`; Grok’s “lifts through every Witt level with growing degree” (`grok46.md:93–94`). Explicitly *not* a widening of R2 (`AUDIT.md:10640–10644`; `xmodel/witt-tate-control-20260824.md:11–14`).
- **Coefficient ring.** Finite levels `W_n(F_p)=Z/p^n` for odd primes `p`; inverse limit in the Tate algebra `Z_p⟨x,y⟩`. Stated: `witt-tate-control-20260824.md:36–59`; `AUDIT.md:10645–10655`; polar producer `as109-bounded-polar-conductor-gate-20260824.md:10–21`.
- **Equations.** `S_n=sum_{j=0}^{n-1} p^j x^{j(p-1)}`, `F_n=(x-x^p, y S_n)` over `Z/p^n`; integer identity `det J=1-p^n x^{n(p-1)}`. Inverse limit `C_p=(x-x^p, y/(1-p x^{p-1}))`. Stated: tate control `42–83`; polar gate `10–21`; `AUDIT.md:10645–10655`. At `n=1` this *is* the special fibre `(x-x^p,y)` (tate `57–59`).
- **`x` support.** `P` fixed `{(1,0),(p,0)}`. `Q` has exactly `n` monomials, `x`-exponents `{0,p-1,2(p-1),…,(n-1)(p-1)}`. At `p=3`, depths `2,3,4`: `{0,2}`, `{0,2,4}`, `{0,2,4,6}`. Stated: wild review `as109-wild-symplectic-conductor-review-grok-20260824.md:376–379`; `AUDIT.md:10651–10652`.
- **`y` support.** Always `y`-degree 1. Stated: wild review `376–379`.
- **Generator order.** Closed form; matrix order UNSTATED. Polar hostile review used `s`-first / `y`-major (`as109-bounded-polar-conductor-review-grok-20260824.md:121`). Wild independent engine used `Q1`-first / `y`-major (wild review `127`).
- **Gauge.** Unique identity-branch restricted-analytic symplectic `Phi_F` with `C_p ∘ Phi_F = F` for a hypothetical polynomial lift of the same special fibre (polar gate `40–46`; polar review `80`). Unrestricted completed symplectic gauge is one orbit (wild producer `as109-wild-symplectic-conductor-gate-20260824.md:25–30`). First Witt digit: one divergence-free affine orbit with forced Cartier `[x^{p-1} y] Q1 = 1` (wild producer `34–38`; wild review `5`).
- **Collision.** Fixed points `(0,0),(1,0)` collide at every finite level (`AUDIT.md:10649–10650`).
- **AS109 filename vs prime.** Wild review: compiler samples `p=3,5`; “the AS109 seed is `p=109`” (wild review `40`). Polar gate: “No `p=109` enumeration was performed” (polar gate `71`). Polar `p=3,5` digit matrices are controls on a general-odd-`p` theorem, not an `F_109` computation (polar review `53–54,84`).

### R4. `AS109-FIBRE` — special fibre over `F_109`

- **Also called.** Historical AS109 seed; prime/seed line of every 2026-08-24 AS109 gate.
- **Coefficient ring.** `F_109`. Stated: `as109-support-gate-20260824.md:6`; quadratic/cubic/quartic/closed-support/sextic-preflight headers (same formula).
- **Equations.** `(x-x^{109},y)` over `F_109`. Jacobian `I_2` as a matrix of polynomials because `d(x^{109})=0`. Fermat `a-a^{109}=0` on `F_109`, so `F_bar(a,b)=(0,b)`. Stated: support gate `86–97`; support review `50,65`; degree-cross review `as109-degree-cross-review-grok-20260824.md:37`.
- **`x` support.** `{(1,0),(109,0)}` on `P`. Not always written as a set; equivalent to the displayed seed. Closed-support packed form uses `s=x^{108}` (`as109-closed-support-gate-20260824.md:32–38`).
- **`y` support.** `Q=y`, so `{(0,1)}`. Stated by the seed formula.
- **Generator order.** UNSTATED in the producer freeze. Review engines used integer sparse dicts, not a campaign-normal order (support review `13,99–103`).
- **Gauge.** First-order triangular source family `G_m=(x+109 y^m,y)` used as a *control* that moves literal supports (support gate `142–149`; support review `62–63`). This is not a unique slice of R5.
- **Collision (frozen marked sections).** `A_i(1,0)-A_i(0,0)=0`, `B_i(1,0)-B_i(0,0)=0` for `i=0,1` (support gate `74–79`). Carry erratum *quarantines* generic marked-collision tests over `F_109` unless carry-aware or integral (`as109-support-gate-20260824-erratum.md:37–40`). Hensel collision of residue balls is a property of R5, not this fibre alone.

### R5. `AS109-LIFT` — hypothetical exact polynomial lift over `Z_109`

- **Also called.** Exact integral AS109 lift; Sol’s intended “canonical fixed-support AS109” (`sol56.md:99–101,142–148`); Grok row-19/21 “hypothetical exact `Z_109` lift” (`grok46.md:97–98`).
- **Coefficient ring.** `R=Z_109`, fraction field `K=Q_109` (characteristic zero). Stated: closed-support `6–7,32–38`; cubic `(3.1)` at `as109-cubic-coupling-gate-20260824.md:301–304`; floor-twelve `as109-max11-floor12-composition-opus5-20260826.md:10–20`; AS-TRI promotion `as109-one-sided-target-degree-tri-promotion-sol-20260827.md:16–32`; n=6 face `as109-n6-top-two-y-bands-face-isolation-grok-20260827.md:22–26`. Explicit firewall: the AS-TRI proof “would be false if `Z_109` were incorrectly read as `F_109`” (AS-TRI promotion `50–52`).
- **Equations.** `P=x-x^{109}+109 A`, `Q=y+109 B` in `Z_109[x,y]`, `det J(P,Q)=1`. Packed identity `det J-1 = 109(L(A,B)-x^{108}+109 N(A,B))` with `L=A_x+B_y` and `N=(A_x-s)B_y-A_y B_x` (closed-support `32–44`). Truncated digits modulo `109^3`: `P=x-x^p+p A_0+p^2 A_1`, `Q=y+p B_0+p^2 B_1` (support gate `49–63`; erratum `44–48`). Uncarried `E1,E2` over `F_109` are **not** the exact condition modulo `109^3` (erratum `31–40,121–125`).
- **`x` support.** UNSTATED as a finite set. Cap-eight literal-slot grammar is `NO-FROZEN-GRAMMAR`: already at the first lift, two-slot family `A_0=y^m`, `B_0=x^{108} y` has unbounded exponent `m` (support gate `13–21,117–140`; support review `29–33,64`). Independent-slot closed-support certificates force `x^{108k}` for every `k` (closed-support `13–16`). Floor theorems hold at *arbitrary finite* `x`-degree (quadratic gate `8–9`; one-sided floor-six `as109-one-sided-prime4-composition-sol-20260827.md:26–28`).
- **`y` support.** Not a unique cell. Banked exclusions, all for *both* corrections simultaneously: `<=2` (`as109-quadratic-coupling-gate-20260824.md:14–19`), `<=3` (cubic `(3.2)` at cubic gate `316`), `<=4` (`as109-quartic-discriminator-gate-20260824.md:7–10`). Two-sided floor: `max(deg_y A, deg_y B)>=12` (floor-twelve producer `17–20`; review `as109-max11-floor12-composition-review-sol-20260826.md:25–36`). One-sided: `deg_y Q=deg_y B>=6` (prime/4 composition `10–20`). Residual corner: `n=deg_y Q=6`, `m=deg_y P>=12`, `3|m`, `6|deg_x(q_6)`, `d=gcd(m,6) in {3,6}` (n=6 face `30–38`). Affine-`y` corrections are a no-go (closed-support `18–22`). Sextic coprime `(5,6)` remains a Pfaffian preflight, not an AS109 exclusion (`as109-sextic-frontier-preflight-20260824.md:19–35`).
- **Generator order.** UNSTATED for a matrix cell.
- **Gauge.** (i) Triangular `G_m=(x+109 y^m,y)` changes literal supports (support gate `142–149`). (ii) Exact source-translation group of the *lift set*: `sigma_tau(x,y)=(x+tau,y)` for every `tau in Z_109` (not merely Teichmüller of `F_109`); Fermat quotient `(tau-tau^{109})/109` is `R`-valued but not an `R`-polynomial in `tau`; action does not descend to `F_109` on the special fibre (`ideation-20260827T0145Z-opus5.md:460–495`). Slice `[x^{108} y^0]A=0` only if `deg_x A<=108` (same file `507–524`). (iii) Completed-orbit `Phi_F` of R3 at `p=109` is restricted-analytic, not a polynomial gauge (polar gate `40–63`). Deck translations of the reduction are a different object from (ii) (opus5 `497–505`).
- **Collision.** Hensel: each target ball `(0,b)+109 Z_109^2` has one preimage in every source ball `(a,b)+109 Z_109^2` (support gate `85–100`; support review `65`). Frozen two-layer marked sections are a stricter freeze, not required for Hensel (support review `42,203–206`).

### R6. `AS109-HENSEL` — 109-sheet consequence of R5

- **Also called.** Grok’s “109-sheet `Z_109` Hensel lane” (`grok46.md:97–98`; cross-poll `85`). `APPROACHES.md:210` row 21.
- **Coefficient ring.** Same as R5: `Z_109` / `Q_109`, plus formal tube `R=Z_109[[S,T]]`. Stated: `as109-hensel-global-degree-cross-gate-20260824.md:11–38`; degree-cross review `37,66`.
- **Equations.** Conditional on R5: `d=[K(x,y):K(P,Q)]>=109`; `L tensor_M E ≅ E^{109} × A_infinity` with `dim A_infinity=d-109`; local monodromy fixes the 109 displayed sheets; no `109|d` and no rational `C_109` deck (hensel-cross `27–47`; degree-cross review `8,214`). `xy`-membership: 109 conjugates of `xy` on the tube `(109 S, 1+109 T)`, so `xy notin M` (`as109-xy-membership-gate-20260824.md:12–26`).
- **`x`,`y` support, generator order, gauge.** UNSTATED — this is a function-field/tube statement, not a support cell.
- **Collision.** The 109 integral Hensel branches, not a new marked-point recipe.

### R7. `AS109-D12-CELL` — Sol’s proposed fixed-support matrix cell

- **Also called.** Card `AS109-D12` (`sol56.md:142–148`); fingerprint in cross-poll `18`; held in `ideation-20260831T1033Z-synthesis.md:104–107`.
- **Coefficient ring.** Named `F_109` for the rank certificate (`sol56.md:99–101,144–145`). That is R4’s field, or a *digit* field of R5, not R5’s coefficient ring `Z_109`. Witt rings and reduction maps are listed as *dependencies*, not given (`sol56.md:144`).
- **Equations.** “Linearized determinant-plus-collision matrix” at “the first unsolved Witt level” (`sol56.md:145`). Which Witt level, packed vs uncarried, and which collision: UNSTATED.
- **`x` support.** “Source-complete support grammar with maximum correction `y`-degree 12” (`sol56.md:144`). The campaign grammar stop is `NO-FROZEN-GRAMMAR` (support gate `1–21`). UNSTATED as an explicit finite set.
- **`y` support.** “Maximum correction `y`-degree 12” (`sol56.md:99–101`). That is R5’s two-sided *floor*, not a unique bidegree. Residual `n=6` (R5) and two-sided `(12,*)` are different shapes. UNSTATED which shape.
- **Generator order.** “Fixed generator order” as a dependency (`sol56.md:144`). Which order: UNSTATED.
- **Gauge.** “A gauge slice” as a dependency (`sol56.md:144`). Which of R5’s gauges: UNSTATED.
- **Collision.** “Transported through the same ring map” (`sol56.md:144`). The map itself: UNSTATED.

### R8. `MAX12-CHAR0` — characteristic-zero maximum-eleven / residual `(8,12)`/`(9,12)`

- **Also called.** “Degree-twelve frontier” in `ideation-20260826T2350Z-td6.md:340–360` Card C (“Integral AS109 routing into the degree-twelve frontier”). Not an Artin–Schreier seed.
- **Coefficient ring.** Characteristic-zero field (floor-twelve review `11–13`: every char-0 Keller pair with max actual partial `y`-degree `<=11` is an automorphism). Routing into `Z_109` is proposed, not constructed (td6 Card C `348–360`).
- **Equations / supports / gauge / order.** UNSTATED as an AS109 object. Card C asks for normalization automorphisms that are integral over `Z_109` *before* any tangent matrix over `F_109` (td6 `356–360`).
- **Relation.** The floor-twelve *composition* uses this char-0 theorem as one input to a statement about R5 (floor-twelve review `9–22`). That is a theorem, not an identification of R8 with R4.

Out of registry (not called AS109 or a degree-12 seed): Mondello char-2 hull, listed beside R1 in `APPROACHES.md:208`.

## 3. Ring-map audit

Pairs. “Written” means some artifact exhibits the map, not that the present lane recomputed it.

| Pair | Map in artifacts? | Verdict |
|---|---|---|
| R1 → R2 | Teichmüller `[2]=8` plus first-Witt correction `A=0`, `B=x^2 y` | Written: oddprime report `23–50` |
| R1 → R3 at `p=3` | `F_n mod 3 = (x-x^3,y)` because `S_1=1` | Written: tate control `57–59` |
| R2 → R3 | None. AUDIT: R3 is “a separate descendant/control, not a widening” of R2 | **NO MAP CLAIMED** (`AUDIT.md:10640–10644`; tate `11–27`) |
| R4 → R5 | Reduction modulo 109 of the displayed lift | Written as the *definition* of R5, not a constructed lift (support gate `86–87`) |
| R4 → R3 at `p=109` | `F_n=(x-x^{109}, y S_n)` reduces at `n=1` to R4; `C_{109}` is the inverse limit | Written for general odd `p` (tate `51–59`; polar `10–21`). Not a polynomial map `A^2→A^2` |
| R5 → R6 | Hensel/parameter inverse-function on residue balls and the tube `Z_109[[S,T]]` | Written as a *theorem about R5*, not a second seed (hensel-cross `11–38`) |
| R1 or R2 → R4 | Same schema `F_AS=(x-x^p,y)` at `p=3` vs `p=109` | **NO MAP CLAIMED.** No homomorphism `F_3→F_109` or `Z/9→F_109` appears |
| R3 at `p=3` (`W_n(F_3)` / `Z_3⟨x,y⟩`) → R5 (`Z_109`) | — | **NO MAP CLAIMED** |
| R3 at `p=3` → R6 | — | **NO MAP CLAIMED** |
| R7 → R4 or R5 | Sol lists “declared coefficient/Witt rings and reduction maps” as a *to-do* | **NO MAP CLAIMED** in the charged card |
| R8 → R5 | Card C proposes to audit integral normalizations modulo 109 then form a tangent matrix over `F_109` | Proposed, not exhibited (td6 `356–360`). **NO MAP CLAIMED** as written |
| R5 source translation `sigma_tau` | Integral action on the *moduli of lifts*, not a deck `F∘sigma=F` | Written: opus5 `471–505`. Does not identify R4 with R5 as rings |

Wild/polar theorems that quantify over “an odd prime `p`” are a *family of objects*, one per `p`. Instantiating `p=3` and `p=109` does not supply a ring map between those instances (wild review `40`; polar gate `71`).

## 4. Silent-identification flags

These artifacts treat two registry rows as one object without a map.

1. **Charged Sol card (load-bearing collision).** `sol56.md:99–101,142–148` names “the exact `F_109` Artin–Schreier seed” and a “maximum `y`-degree 12” Witt cell, citing `[A:208–210]`. `APPROACHES.md:208` concatenates R1/R2, the cap-eight R4 grammar stop, the R5 floor-twelve theorem, and R3’s unbounded polar conductor in *one* row-19 cell; line 210 is R6. Sol’s card therefore reads R4’s field, R5’s floor, and R7’s matrix as a single seed. Matching “AS” / “109” / “12” is exactly the fallacy the cross-poll names (`crosspoll-sol56.md:85`).

2. **Charged Grok bottleneck 2.** `grok46.md:93–94` says the typed `F_3` collision “lifts through every Witt level with growing degree.” R2 is a *single* `W_2` lift that already enlarges support and is not promoted further (`AUDIT.md:10636–10638`). R3 is the growing-support tower and is explicitly not a widening of R2. Grok’s sentence identifies R1/R2 with R3.

3. **Charged Grok “continue” of the degree-12 frontier as row 19.** `grok46.md:35,299` keeps “maximum-twelve partial degree (row 19)” as the live fixed-support Witt frontier. Row 19’s degree-twelve clause is the R5 floor; Grok’s bottleneck 2 in the same section is R1/R3. The continue-instruction therefore lets R3 and R5 share a row number. Bottleneck 4 correctly splits R6 (`grok46.md:97–98`).

4. **`APPROACHES.md:208` “same-seed tower”.** After listing R1 and R4/R5 in one cell, the stuck-point says “a same-seed tower lifts through every Witt level.” R3 is that tower, for every odd `p`. “Same-seed” is true of the *schema* `F_AS=(x-x^p,y)` and false as an identification of the `F_3` witness with the `F_109` fibre.

5. **AS109 filenames on general-odd-`p` gates.** `as109-wild-symplectic-conductor-gate-20260824.md` and `as109-bounded-polar-conductor-gate-20260824.md` are titled AS109, sample `p=3,5`, and refuse a `p=109` run (wild producer `310`; polar gate `71`; wild review `40,64`). The filename is not a ring map to R4/R5.

6. **Digit field vs lift ring.** Sol’s discriminator is a rank certificate *over `F_109`* (`sol56.md:145`). AS-TRI promotion `50–52` and the carry erratum `31–40,121–125` record that uncarried `F_109` equations are not the packed `Z_109` identity. Treating R4 arithmetic as R5 is a silent ring change.

7. **Card C routing R5 into R8.** `ideation-20260826T2350Z-td6.md:340–360` would send an AS109 residue into char-0 residual shapes `(8,12)`/`(9,12)` after integral normalization. No such normalization map is supplied. Later n=6 work keeps an automorphism of numerical type `(12,6)` as a *control that is not AS109* (n=6 face `332–351`; prime/4 hostile review records that control occupies the residual type with `v_{109}(q_6)=0`).

8. **Frozen marked sections vs Hensel balls.** Support freeze uses two lattice sections; Hensel uses 109 residue balls. Support review `203–206` already separates them. Sol’s “collision pair” (`sol56.md:100`) does not say which.

## 5. Reconciliation verdict

**DISTINCT SEEDS.**

The labels do not resolve to one object. The distinct objects are R1, R2, R3, R4, R5, with R6 a theorem about R5, R7 an underspecified cell, and R8 a char-0 degree bound used as an ingredient of the R5 floor.

**What the matrix programme may target, if it is charged at all:** a *declared* finite-support cell of **R5** (`Z_109` exact lift of R4) whose correction `y`-degrees respect the floor-twelve theorem and, if one-sided routing is used, the residual `n=6` shape. It may not target R1, R2, or R3: those already have documented finite-level lifts, and R3’s support/degree grow by construction (tate `23–27`; `AUDIT.md:10651–10656`). It may not treat R6 as a seed: 109 sheets are a consequence of an R5 lift, not a search grammar. It may not treat R4’s function theory on `F_109` as a polynomial lift over `Z_109` (AS-TRI promotion `50–52`). It may not treat R7 as already specified.

**Deciding criterion.** In the charged sources, “the first live bounded partial-degree frontier is maximum twelve” (`APPROACHES.md:208`; floor-twelve producer `17–20`; Grok `35,93–94,299`; Sol `18,99–101,159`) is a theorem about *hypothetical exact `Z_109` lifts of `(x-x^{109},y)`*. The `F_3` programme’s live question is uniform support of an already-known all-Witt *control*, which is the opposite of a new degree-12 cell. Hensel (row 21) does not kill `A_infinity` and does not freeze a support (`APPROACHES.md:210`; Grok `97–98`). Therefore the only object for which a degree-12 *matrix* could be a new bounded polynomiality test is R5, and only after R7’s UNSTATED fields are filled from an explicit freeze, not from labels.

R7 as written is not a ninth seed; it is R5 with missing data. Those missing data are listed in §6. They are not filled here by cap or analogy.

## 6. Minimal preflight the matrix lane must run

Fail closed before charging any matrix, enumerator, or AWS rank job. Desk-scale shape/rank estimate only; if dimensions or fill-in are uncertain, do not start the cell on the desk (`sol56.md:100–101,145`; campaign AWS policy as cited there).

1. **Name one registry id.** The charge sheet must say `R5` (or a named subshape of R5: two-sided floor-twelve, or residual `n=6`). Naming “AS109”, “F_109”, “degree 12”, or “Witt” is not a name. If the intended object is R1/R2/R3, stop: those are not the degree-12 frontier.

2. **Declare the matrix ring and the lift ring separately.** Lift ring: `Z_109[x,y]` with packed identity (closed-support `41–44`) *or* a named Witt truncation with *carry-aware* digits (erratum `31–48`). Matrix ring: if it is `F_109`, state that it is a reduction of that packed/carry-aware system, and exhibit the reduction map. Uncarried `E1,E2` over `F_109` are quarantined (erratum `37–40,121–125`). Do not read `Z_109` as `F_109` (AS-TRI promotion `50–52`).

3. **Declare the Witt level.** “First unsolved Witt step” (`sol56.md:145`) is not a level. Write `n` in `mod 109^n` and the exact digit unknowns.

4. **Freeze finite `x` support and finite `y` support as explicit exponent sets** for `A` and `B` (or for `P` and `Q`). A slot-count cap is not a grammar (support gate `13–21`). “Maximum correction `y`-degree 12” is a floor, not a set: choose the bidegree shape (`deg_y A`, `deg_y B`) and the `x`-exponents. If no finite exhaustive gauge-normal grammar exists, the historical stop is `NO-FROZEN-GRAMMAR` and the cell is not chargeable.

5. **Declare generator order** of the coefficient vector (e.g. `Q1`-first / `y`-major, or `s`-first / `y`-major). Matching variable names across files is not a map (FALLACY-v2 variable/ring map; Grok `171`).

6. **Declare the gauge slice** and prove the cell is a section of it: translation `sigma_tau` with a named `tau` (and the `deg_x A<=108` restriction if that slice is used), or a named triangular `G_m`, or a *polynomial* bound on `Phi_F` (polar: unbounded analytic gauge is the default). Record that `sigma_tau` acts on lifts, not as a deck.

7. **Declare the collision** as one typed condition: frozen marked sections, or Hensel residue-ball collision, or R1-style `(0,0),(1,0)→(0,0)` transported along the map of step 2. Do not mix them. Transport the chosen condition through the same declared map.

8. **Image checks.** After the map is declared, check: seed reduction is `(x-x^{109},y)`; `det J` is the packed 1, not a residue-unit substitute; chosen collision holds on the image; the `(12,6)` triangular automorphism control is *excluded* from the cell (it is determinant one and the numerical residual type, and is not AS109).

9. **Do not wrap the cell in `sat()`.** If an ideal appears later, extract the component, assert its ring, and run a positive and a negative control. No such ideal is licensed by R7 as written.

10. **Floor/attainment.** Inconsistency of a frozen cell kills *that cell* and may raise a bounded frontier only for that declared support (Sol `146–147`). Consistency is not a characteristic-zero polynomial counterexample and is not R3’s restricted-analytic limit. Next-level monomials outside the freeze are fixed-support failure, not a licence to widen the cap.

11. **Stop without charging** if any of 1–7 is UNSTATED, if the map of §3 for the chosen pair is `NO MAP CLAIMED` and is being assumed, or if the job is an unrestricted further Witt level of R3.

## 7. Citations index

Charged frozen copies: `ideation-20260831T1033Z-sol56.md`, `-grok46.md`, `-crosspoll-sol56.md` (hashes in §0). Historical AS109: support gate/erratum/review; closed-support; quadratic/cubic/quartic; sextic preflight; wild-symplectic producer/review; polar-conductor producer/review; hensel-cross/degree-cross; xy-membership; all `20260824`. Later: floor-twelve producer/review; AS-TRI promotion; one-sided floor-six; n=6 face; `ideation-20260827T0145Z-opus5.md` §4; `ideation-20260826T2350Z-td6.md` Card C. F_3/Witt defining notes cited by those texts: `round2-witt-oddprime-20260824.md`, `cases/round2_witt_oddprime/PREREGISTRATION.md`, `witt-tate-control-20260824.md`, `APPROACHES.md:208–210,275`, `AUDIT.md:10620–10656`.

<!-- BODY-END -->

