# Hostile review: selected-Q8 positive-genus exclusion, repaired V2

**Reviewer:** independent algebraic-geometry referee (Grok; different model family from the GPT-family producer).  
**Target:** `xmodel/max12-912-order3-nu-q8-selected-contact-positive-genus-exclusion-repaired-v2-20260825.md`  
**Eligibility:** only this V2 file. V1 remains immutable and is not promoted.

## 0. Execution disclosure

This session has **no Bash, no CAS, no network access, and no file writes**. SHA-256 values were not recomputed. Singular, python-flint, and every AWS replay were not executed. Parent computational residues are taken from the frozen, independently reviewed attestations named below; the composition itself is hand-checked as a curve-theoretic argument over those inputs.

## 1. Files read

V2 report; V2 case `README.md`, `REGISTRATION.md`, `MANIFEST.sha256`, `FREEZE.sha256`; V1 repaired composition and its case files; the CONFIRMED genus review `xmodel/max12-912-order3-nu-q8-p127-positive-genus-point-count-review-grok-20260825.md`; and every parent report/review named by V1’s table: selected global quotient + Claude CONFIRMED review; mod-127 component successor + sparse-contact CONFIRMED_WITH_REPAIRS review; plane-`H` integrality + Claude CONFIRMED review; rational-contact residual erratum + Claude CONFIRMED_WITH_REPAIRS review; arithmetic full-contact bridge + Claude CONFIRMED review; positive-genus point count; specialization-bypass note + Codex conditional audit; infinity passport, Galois primitivity, and their joint Claude CONFIRMED review. The superseded provisional composition was read only to identify the defects V1/V2 claim to close.

Hash strings quoted by V2 for V1 (`b543738a…`), the V1 manifest (`57717e15…`), and the genus review (`1b79cddc…`) agree with the V2 case manifest as read. They were not recomputed.

## 2. Exact claim under audit

Conditional on the reviewed cube/Faber and selected-global-quotient landing of an **actual** order-three trajectory in the leaf `k=mu=0`, `nu!=0` whose selected coefficient component meets a corrected-Q8 contact: no such trajectory exists.

Not claimed: components disjoint from those contacts, every `nu!=0` component, the polynomial core, `(8,12)`, all of `(9,12)`, maximum twelve, an arbitrary Keller pair, or JC2.

## 3. Repair-closure checklist

**Finite DVR before `P1`.** Closed. Geometric Lüroth over `K0` yields only geometric rationality of `Ytilde`. A finite extension `K1/K0` is taken so that `Ytilde` acquires a rational point (and any finite trajectory constants); a complete DVR `R1` above `R0` is formed, possibly ramified; then `Ytilde_(K1) ≅ P1_(K1)`. The identification with `P1` is never made over `K0`.

**Proper-model / divisorial-valuation existence of a component dominating the special curve.** Closed. Two equivalent existence routes are given: (i) projective closure of the integral horizontal component of `Z_(R1)` selected by `Y_(K1)`, then normalization and lying-over above the generic point of `C_(k1)`; (ii) the divisorial valuation of `K0(Y)` cut out by `C` (height one on the excellent flat integral arithmetic surface `Z`, after normalization) extends to the finite extension `K1(t)`, and its center `Gamma` is residually transcendental with residue containing a finite extension of `k1(C)`. Regularity of an arithmetic-surface model is permitted only to display the same valuation; it is not a substitute for the whole-source attachment.

**Geometric Lüroth after finite constant extension.** Closed in both uses. Section 5 tests geometric rationality of `Ctilde` over an algebraic closure, not `k0`-rationality of `k0(C)`. Section 6 passes to `ell(C) -> ell(s)` after the finite constant extension in the residue field, then applies geometric Lüroth; ground-field Lüroth over `k1` is not used.

**Full `8 x 8` unit at the winning contact as local-uniformizer certificate.** Closed. The parameter `w` is taken from the reviewed full relative Jacobian unit at the marked full contact `q=(0,q_v)`, `q_v in {26,58,67}`, not from a charged fibre `w=w_i ≠ 0`. The bridge review already evaluated the reduced determinant at those three roots (`104`, `27`, `61` mod `127`). The plane unit `H_v(q)≠0` is invoked only for an optional ramification-index/separability cross-check; Riemann–Hurwitz is not a premise of `g(Ctilde)>0`.

**Galois propagation only among characteristic-zero components.** Closed. Singleton propagation uses `Qbar`-isomorphism of the eight characteristic-zero components (same geometric genus / geometric rationality). The text explicitly refuses the claim that all eight specializations are `H`-supported.

**Semistable reduction / arithmetic-genus semicontinuity.** Closed. Named only to be discarded. The load-bearing contradiction is ruled residue plus geometric Lüroth.

**Fibre-completion precision.** Closed. `K0[[w]]` and `k0[[w]]` are declared to be the completed generic and special fibre local rings of `Spf R0[[w]]`, not `R0[[w]] ⊗ K0`.

**V2 finite-field-of-definition / unramified-base treatment.** Closed, and this is the only new mathematical content relative to V1. V1 introduced an “integral mod-127 component `C`” over the residue field of the splitting DVR and then treated it as geometrically integral. That is not licensed: an `F_127`-irreducible component need not remain irreducible after the degree-five unramified residue extension. V2 proceeds in the only safe order:

1. Over `Fbar_127`, the full `8 x 8` unit gives completed local ring `Fbar_127[[w]]`, hence a unique geometric source branch and a unique geometric component through the rational contact `q`.
2. The residual theorem supplies that this unique germ is `H`-supported (at least one of the three rational contacts lies on an `H`-supported component; uniqueness identifies it).
3. `q`, the source, and `H` are defined over `F_127`. Uniqueness plus `Frob(q)=q` makes the component Gal-stable, hence it has a finite field of definition `k0=F_(127^m)` (in fact `m=1` is forced, though the argument never needs that sharpening).
4. The splitting DVR of the bridge is replaced by the finite unramified complete/Henselian `R0` with residue `k0` **before** geometric integrality or genus of `C` is used.
5. `C/k0` is then the geometrically integral model of that unique component, still dominant onto `H_(k0)`.

The parent 8×8 unit, contact section, and six-row uniqueness are `Z_(127)`-statements (127-unit denominators; unit determinant at the rational contacts). They base-change to any unramified `R0`. For a rational contact one does not need the quintic splitting extension.

## 4. Attack on the load-bearing chain

**Common whole-source `R0[[w]]`.** The ambient localized source is the reviewed eight-equation `Z_(127)`-scheme that does not invert `w`. Formal implicit functions at a point where the full `8 x 8` Jacobian is an `R0`-unit give `Spf R0[[w]]`. The generic completed fibre is a domain, so there is one characteristic-zero germ `Y`. Six-row uniqueness (gate + bridge) identifies it with the selected non-parity branch through this contact. No plane section is used.

**Zero closure ideal and unique special branch.** Let `Z` be the schematic closure of `Y` in the common source. Locally in `R0[[w]]`, the ideal of `Z` vanishes in `K0[[w]]` because that completed generic fibre is exactly the germ of `Y`. `R0[[w]] -> K0[[w]]` is injective (`R0` a domain, coefficientwise). So the ideal is zero, the special-fibre completion is `k0[[w]]`, and there is one reduced multiplicity-one branch through `q`. Flatness of the integral closure `Z/R0` is the torsion-freeness just used: schematic closure of a generic-fibre curve over a DVR is flat. After a possibly ramified `R1/R0`, the scheme-theoretic special fibre of `R1[[w]]` is still `k1[[w]]`; ramification is arithmetic, not in `w`.

**Identity with an `H`-dominating geometric component.** Plane incidence `H(q)=0` is not enough. The residual erratum places at least one rational full contact on an `H`-supported **source** component, using the unique `F_127[[w]]` branch, substitution of that branch into the eight source equations and into `H`, and the repaired intersection bound `40960>37010`. Combined with geometric uniqueness at `q`, that unique geometric component is `H`-supported. Section 4 then identifies the special branch of `Z` with the branch of this `C`, so `C` is a special component of the horizontal closure, not a second plane component through the same point. A hypothetical `F_127`-component that split geometrically into several pieces, only one of which dominated `H`, is blocked by uniqueness: Gal acts on geometric components through the rational point `q`, so the orbit through `q` has size one and the `F_127`-component is geometrically irreducible.

**Positive genus upstairs.** The Grok-CONFIRMED count is `g(Htilde)>0` for the pinned geometrically integral plane curve (16,168 smooth affine `F_(127^2)`-points inject into the normalization, against `#P1=16130`). Dominance of projective integral curves gives a finite nonconstant map `Ctilde -> Htilde_(k0)`. If `Ctilde` were geometrically rational then `kbar(Htilde) subset kbar(t)`, and geometric Lüroth (valid in every characteristic in transcendence degree one) would make `Htilde` rational. This does not use separability, Riemann–Hurwitz, or a `k0`-point of `C`. Geometric genus is invariant under the finite constant extension `k0/F_127`.

**Ruled residue / geometric-Lüroth obstruction.** An actual trajectory supplies, by the CONFIRMED infinity theorem, a nonconstant morphism `P1_x -> Ytilde`, hence geometric rationality of `Ytilde` in characteristic zero. After `K1`, the generic function field is `K1(t)`. The valuation of `C` remains residually transcendental under finite extension of function fields (residue-field extensions are finite, so transcendence degree one is preserved). Ruled residue for a residually transcendental divisorial valuation of a rational function field gives `kappa(Gamma)=ell(s)` with `ell/k1` finite. Dominance/`generically finite` puts `k1(C)` inside `ell(s)`; the compositum is `ell(C) subset ell(s)`; geometric Lüroth contradicts `g(Ctilde)>0`. Therefore `Ytilde` is not geometrically rational and admits no nonconstant map from `P1`.

The residue field of `R1` is finite, so the identification of a genus-zero residue curve with `P1_ell` is the usual one; the classical ruled-residue statement for `K(t)` already gives a rational residue field over a finite constant extension. Completeness of `R1` is unused. Inseparable residue phenomena in characteristic 127 do not affect Lüroth in transcendence degree one.

**Primitive all-eight / eight-singleton propagation.** CONFIRMED primitivity: the Gal(`Qbar/Q`) partition of the eight contacts by unique geometric components is `8` or `1+...+1`. All-eight is already empty for an actual trajectory (CONFIRMED infinity: two distinct normalization points cannot both be the image of `x=infinity`). In the singleton alternative, Section 6 kills the component attached at `q`; the other seven are `Qbar`-isomorphic conjugates, hence not geometrically rational either. No inference is drawn about their special fibres.

**No escape from the selected leaf.** Every charged object is a selected non-parity Q8 component or its mod-127 specialization at a corrected full contact. Components disjoint from the eight contacts, other `(9,12)` cells, Taylor realization, maximum twelve, and JC2 are repeatedly excluded. The cube/Faber and global-quotient landing is a hypothesis, not a conclusion. The genus review’s standalone-plane firewall is respected: V2 composes that theorem with separately reviewed source/contact/bridge facts rather than extracting those facts from the count.

## 5. Defects affecting V2

None. Optional sentences that are not premises (`H_v(q)≠0` as a separability cross-check; the word “equivalently” between Frobenius-stability and mere existence of a finite field of definition) do not carry the theorem. Frobenius-stability is the stronger uniqueness corollary and is available; finite field of definition is what is used. Projective closure of `Z_(R1)` is the standard compactification of a finite-type `R1`-scheme and is backed by the valuation-theoretic existence route.

Inherited residual engine trust (python-flint on the genus count; single-run Normaliz on the vertical bidegree bound) lives in CONFIRMED / CONFIRMED_WITH_REPAIRS parents whose repaired successors V2 consumes. It is not a V2 composition defect.

## 6. Verdict

The V2 descent — unique geometric `H`-supported component through the rational full contact, finite field of definition, unramified `R0` before any geometric-integrality or genus claim — closes the remaining V1 gap. The rest of the repaired chain (finite DVR before `P1`, proper/divisorial existence, geometric Lüroth after constant extension, `8 x 8` uniformizer, fibre completions, characteristic-zero-only Galois propagation, semistable reduction unused) holds at the registered selected-leaf scope.

CONFIRMED
