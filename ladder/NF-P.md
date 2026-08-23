# NF-P.md — the free-parameter / ν=1 schema quotient

Status: **REDUCED-WITH-PROVED-CORE (2026-08-14, round 1).** The
three NF-P object classes (`sol-normalform.md` §3: pure-(b) cells,
equal-handshake cylinders, ν=1 case-I merge schemas) are classified
at the single-vertex tier, the td-11 rider list is stamped with ZERO
live parametric objects, and the td-7 `(2,2t)` x-tail regression is
consistent. The one REDUCED residue is the conjecture's
reflexive-transitive closure demand across state-changing steps,
which is exactly the standing beyond-core numerator item — cited,
not a new obligation (NF-P-OB1). Machine gate: `cases/nfp_check.py`
(10 checks, exit 0; count printed). Sources: `sol-normalform.md`
§§2.2/3, `sol-gluing-design.md` §1.3, NF-M.md (the square system),
`cases/scratch_offaxis_pricing/px2.py` (the pure-b formula layer),
TOWER-TD11.md §17 riders. No git commit.

## 1. Where NF-P objects occur in the audited perimeter

* **Pure-(b) cells** (2.6): the priced parametric family
  `p = η^ε(η^ν − A)^l`, `q = η(η^ν − A)`, free integer `ν` —
  px2's `pure-b l{l}e{eps}` steps at every td-7/td-11 seed (the
  scope menus' "pure maxima" rows).
* **Equal-handshake merge cylinders**: the `C = 0` parametric
  families — already surfaced and killed inside the audited region
  by NF-M rounds 8–10 (the `(B,B)` `ε = 1` family; the outer
  `κ̄ = 2νQ+2` and `κ̄ = 4ν+2` families).
* **ν=1 case-I merge schemas** (η-absorbed and η-factor variants):
  the merge modes §2.2 excluded from its ν≥2 reduction — the
  TOWER-TD11 nested-row riders' "ν = 1 inner/outer modes".
* **State-changing clean resonances** (the closure demand's
  generators): 11-A's `5/8`, 11-B's `5/4`, the `w`-changing steps.
* **td-7 regression object**: the `(2, 2t)` x-tail family
  (`ν = 1`, rational `κ̄`, unbounded `ℓ_ex`), dead in the promoted
  panel.

## 2. Theorem NF-P-core (single-vertex classification)

**(i) ν-uniformity of the square system.** Lemmas M1/M2 of NF-M
never used `ν >= 2`: at `ν = 1` (η-factor form `q = η·ΠF_i·ΠG_r`,
`d_q = 1 + Q̂`) the leading coefficient still cancels identically
and the system is square. NF-M-core — computable ideal, `<=
(Q̂−1)!` types, 0-dim locality, OB1 retention — applies to ν=1
η-factor schemas VERBATIM (gate block A).

**(ii) The η-pole lemma: η-absorbed with `ε > 0` is EMPTY.** If
`q(0) ≠ 0` (no absorbed zero root) and `ε > 0`, the L3 relation
`d_p·p·q′ − d_q·p′·q = d_q·C·p` has η-order `ε − 1` coefficient
`−d_q·ε·q(0)·lead ≠ 0` for EVERY `C` — an impossibility
certificate, one line (gate block B). With `ε = 0` the absorbed
variant is square again (`d_q = Q̂`, leading cancels by the same
Fuchs identity); with an absorbed zero root it IS the η-factor form
with a boundary orbit value (guards differ, system identical). So
every ν=1 case-I mode is: empty (`ε>0` absorbed), or an NF-M square
system.

**(iii) Pure-(b): the free `ν` never reaches the state layer.** From
the formula layer: `w₂ = l·w/E`, `M₂ | E`, `λ = ⌈l·w/ε⌉` — all
ν-INDEPENDENT (`E = l − ε`); the free `ν` enters only the degree
multiplier `(ε+lν)/l` and the cell `(d_p, d_q) = (ε+lν, ν+1)` —
scale data in the NF-D sense. Consumers partition the ν-line
finitely: `κ̄ = l·w(ν+1)/(b_h·E) ∈ Z` is a CONGRUENCE in `ν`; the
gap `l(ν+1)/(deg·(ε+lν))` is monotone decreasing to `1/deg` — every
window predicate has one threshold. **One successor summary + a
finite (congruence × interval) partition with exact symbolic
updates: the NF-P partition for a single pure-b vertex** (gate
block C). On the td-11 seeds the pure maxima are `3/11, 1/5, 2/11,
3/10 < 1/2` — below-window at every `ν`; no live member.

**(iv) x-tails: flat degree ⇒ linear gap growth ⇒ finite window
cells.** The `(2, 2t)` family has degree multiplier `1` (flat), so
its gap at arrival degree `D` is `2t/D` — LINEAR in the free `t`:
members with `t > 5D/4` sit at or above the pole top `5/2`
(entry-packet violation); at most `⌊5D/4⌋` discrete cells remain.
The unbounded tail is uniformly dead; the finite head is ordinary
discrete enumeration — consistent with the promoted td-7 panel
deaths (gate block E).

**(v) Per-state resonance finiteness.** The state-changing clean
menu at `(w, M)` has `Δ | num(w)`, `ν | Δ−1` — finitely many steps
per state (the engine's clean loop). The CLOSURE across states is
NF-P-OB1 (§4).

## 3. The td-11 rider stamps (gate blocks D, F)

* **ν=1 inner/outer merge modes** (the nested-row rider): the full
  ν=1 menus at the 11-C decorations — `(A,B)` B-zero and `(B,B)`
  equal-handshake in both q-conventions, all `ε` positions including
  zero-edges — yield 18 schemas; EVERY one is below/at the window
  edge or in-window-REFUSED by the den-criterion at `k | 2`
  (notably `(3,6)M3` at gap `2/3` and `(5,3)M1` at `9/10`: refused).
  **Zero live ν=1 objects.** With (ii), the η-absorbed `ε>0` modes
  are empty outright.
* **Resonance-bearing chains**: 11-A's `5/8` is H8-dead (promoted,
  Lemma 11A-RES); 11-B's `5/4` is the resonant X, refused in the
  TD11-CLASH sweep. Both already dead; NF-P adds the per-state
  finiteness (v).
* **Pure-(b) at the seeds**: below-window at every `ν` (iii).

**No live parametric family exists on the audited td-11/td-7
perimeter.** (Had any schema in D survived, it would have been the
program's first live parametric object; none did.)

## 4. The honest residue

* **NF-P-OB1 (the closure demand).** The conjecture requires closure
  under the full reflexive-transitive state-changing P0 relation
  with finitely many successor summaries. Single steps are finite
  (v); iterating them is EXACTLY the reachable-numerator/beyond-core
  question already OPEN in TOWER-TD11 §13.0 — the same object, not
  a new one. Fail-closed there per the standing perimeter.
* **NF-P-OB2 (case-I handshake provenance).** The ν=1 menu
  enumerations use the (2.8)/(2.9) handshake shape at `ν = 1`; the
  general Prop 9.3 case-I law is cited, not re-derived. A different
  case-I affine law re-opens block D (the verdicts' den-criterion
  structure is robust, but the MENU would change).
* Positive-dimensional components: none observed (OB1 of NF-M never
  fires on the enumerated menus).

## 5. Reproduction

```bash
python3 cases/nfp_check.py     # 10 checks, exit 0 (count printed)
```

Blocks: A M1/M2 at ν=1 (η-factor); B the η-pole lemma lattice; C
pure-b ν-independence, congruence periodicity, monotone gaps, seed
maxima; D the ν=1 merge menus (18 schemas, all refused/out; both
q-conventions; zero live); E the `(2,2t)` x-tail thresholds and
td-7 consistency; F the rider-stamp summary and the OB1 citation.
No git commit.
