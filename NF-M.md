# NF-M.md — multi-orbit coefficient locality: the square-system classification

Status: **REDUCED-WITH-PROVED-CORE; round 2 executes the 67-row
enumeration — all 67 nested 11-C rows DEAD-AT-TIER (§5)
(2026-08-14).** For every
fixed `ν >= 2` discrete merge schema (finite per entry/budget by
`sol-normalform.md` §2.2), the Prop. 8.1(iv) coefficient equation
reduces to an explicitly computable **square polynomial system** —
`Q̂ − 1` homogeneous equations in the `Q̂ − 1` orbit unknowns modulo
the scaling torus (Lemmas M1/M2) — whose solution set modulo
permutation × scaling is the certificate:

* **0-dimensional components** (the generic case, and EVERY observed
  td-7/td-11 instance): a finite set of **types**, at most
  `(Q̂ − 1)!` per schema (Bézout; the coefficient-`x^j` equation is
  homogeneous of degree `Q̂ − j`), each future-local (Lemma M3) —
  **PROVED**.
* **positive-dimensional components**: locality NOT claimed; the
  component is RETAINED unreduced in `Omega` (fail-closed — exactly
  the conjecture's own retention clause). **NF-M-OB1.**
* **empty (with the L7/L8 guards, `C ≠ 0`)**: impossibility
  certificate; the schema is rejected.

Excluded, as `sol-normalform.md` §2.2 itself assigns them: the
`ν = 1` case-I η-modes (NF-P). Machine gate: `cases/nfm_check.py`
(18 checks, exit 0; count printed). Sources: `sol-gluing-design.md`
§1.3 (L1–L9), `sol-normalform.md` §§2.2/3, `cases/tower_check.py`
`t1_local` machinery, `cases/towers/t9_15_direct.json` `t1_local`
rows, Lemma Z-Omega (NF-Z.md). No git commit.

## 1. The objects

At a `ν >= 2` class-C merge, R2.2 fixes (L5/L6):

```text
p = η^ε · Π_i F_i(x)^{p_i},        q = η · Π_i F_i(x) · Π_r G_r(x),
x = η^ν,
```

with `F_i, G_r` monic in `x` (linear factors `x − a_i` for split
orbits; higher-degree monic blocks for unsplit orbit packets — the
F1 row's quadratic is one), multiplicities `p_i` the arrival `μ_e`
and NE `m_j` values, `ε` the zero-slot exponent, and the q-extras
`G_r`. Degrees: `d_p = ε + ν·Σ p_i f_i`, `d_q = 1 + ν·Q̂` where
`Q̂ = deg_x(Π F_i · Π G_r)` and `f_i = deg F_i`. The Prop. 8.1(iv)
equation is the Fuchs relation (L3):

```text
d_p · p · q′ − d_q · p′ · q = d_q · C · p,     C ≠ 0.
```

The coefficient data is `(F_i, G_r)` modulo (i) permutation of equal-
multiplicity orbits and (ii) the scaling torus `η ↦ λη`
(`a ↦ λ^ν a` on orbit values) — "orbit permutation and the allowed
scaling" of the conjecture.

## 2. The reduction (Lemma M2) and the automatic cancellation (Lemma M1)

**Lemma M2 (the `x`-reduction).** Dividing (L3) by `p` and clearing,
the equation is equivalent to the polynomial identity in `x` alone:

```text
F(x) := (d_p − d_q·ε)·G(x)
        + ν·x·[ d_p·G′(x) − d_q·Σ_i p_i·(G/F_i)(x)·F_i′(x) ]
      = d_q · C          (constant),
where G = Π_i F_i · Π_r G_r  (monic, degree Q̂).
```

*Proof.* `p′/p = ε/η + Σ_i p_i·ν·η^{ν−1}·F_i′(x)/F_i(x)`; `q/η = G`
and `η^{ν−1}·q/F_i = x·(G/F_i)` are polynomials; every surviving
term sits in exponents `≡ 0 (mod ν)`. Machine block A verifies the
reduction against the direct (L3) expansion on every certificate row
and on random schemas. ∎

**Lemma M1 (leading coefficient vanishes identically).** The
`x^{Q̂}`-coefficient of `F` is

```text
(d_p − d_q·ε) + ν·(d_p·Q̂ − d_q·Σ p_i f_i)
  = d_p·(1 + ν·Q̂) − d_q·(ε + ν·Σ p_i f_i) = d_p·d_q − d_q·d_p = 0.
```

So `F` has degree `<= Q̂ − 1` automatically — the Fuchs degree
identity, not a constraint. ∎ (machine block B, full lattice)

**Corollary (the square system).** The identity `F ≡ d_q·C` imposes
exactly the vanishing of the `x^1 … x^{Q̂−1}` coefficients — `Q̂ − 1`
equations — on the `Q̂` orbit-block coefficients modulo the 1-dim
scaling torus: **`Q̂ − 1` equations in `Q̂ − 1` essential unknowns.**
`F(0) = d_q·C` defines `C`; `C ≠ 0` is the open guard (L8). The
`x^j`-equation is homogeneous of degree `Q̂ − j` in the orbit data,
so the projective Bézout bound is `Π_{j=1}^{Q̂−1}(Q̂ − j) =
(Q̂ − 1)!`.

## 3. Theorem NF-M-core

**Theorem.** *For every fixed `ν >= 2` discrete merge schema, the
solution set of the Prop. 8.1(iv) equation modulo permutation ×
scaling is the algebraic set of the square system of §2 — an
explicitly computable ideal (the certificate type data). If the set
is 0-dimensional modulo scaling, it consists of at most `(Q̂ − 1)!`
types; two solutions of the same type with the same emitted frame
have identical chain/E5F/tower futures (Lemma M3). If it is empty
under the guards, the schema carries an impossibility certificate.
If a component is positive-dimensional, locality is NOT claimed and
the component is retained whole in `Omega` (NF-M-OB1).*

**Lemma M3 (future-locality on 0-dimensional types).** A later edge
observes the merged chart through: the emitted frame (discrete), the
degrees (discrete), `C` (a scaling-covariant function of the type),
and the orbit values via continuations (L9). Two same-type solutions
differ by an element of permutation × scaling; scaling is the chart
coordinate change `η ↦ λη`, under which the entire downstream system
(L1–L9 at all later vertices) is covariant, and permutation of
equal-multiplicity orbits is a relabelling of attachment slots.
Hence the futures are identical modulo the same symmetry. ∎ —
This argument NEEDS the 0-dimensional hypothesis: inside a
positive-dimensional component two solutions need not be
symmetry-related, and a later edge's own solve takes the arriving
orbit value as a parameter whose variation is observable (resultant
conditions); hence OB1's retention, matching the conjecture's
"retain every coefficient/root label that a later edge can observe".

**Type-set size per (entry, budget).** §2.2 gives the finite schema
menu (mults bounded by `μ_e | M_e`, `r_0 <= m`, `k <= b`, the NE
inequalities); per schema the bound is `(Q̂ − 1)!` with
`Q̂ <= r_0 + k + x` bounded by the same data. So the total type
count is computable from (entry, budget). Observed instances are far
below the bound: every td-7 certificate row has EXACTLY ONE type.

## 4. Regressions (machine blocks C–E)

* **Lemma Z-Omega is the `Q̂ = 1` instance.** One orbit, no extras:
  zero equations, one parametric type, `C = F(0)/d_q = −d_p·a/d_q`
  (at `ε`-adjusted mults) — the NF-Z neutral row `11306·C + 11305·A
  = 0` and the H2/F3 rows reproduce exactly.
* **td-7 certificate rows (t9_15_direct.json `t1_local`).** All six
  rows: the reduction reproduces the certified `C` exactly, the
  higher coefficients vanish at the certified orbit values, and the
  direct (L3) residual is zero. The two `Q̂ = 2` rows are pinned by
  their single LINEAR homogeneous equation to a UNIQUE ratio — the
  certified `Q/A = 2/3` (G row) and `B/A = 3/2` (F2 row, with
  `10C = 51A²`); the `Q̂ = 3` row (F1, quadratic block `t² − 3At +
  3A²`) satisfies its two equations. One type each, `<= (Q̂−1)!`.
* **The pure cylinder is the expected degeneration.** Equal mults
  `μ`, no extras, `ε = 0`: the system forces `g_1 = … = g_{r−1} = 0`
  and leaves `g_0` free — `G = x^r + g_0`, the `μ`-cylinder, a
  SINGLE parametric type (0-dimensional modulo scaling), exactly
  §2.2's surviving `C = 0` shape.

## 5. The 67 nested 11-C rows — EXECUTED (round 8, machine blocks
F–H)

Block F's conservative screen (0 stamps, valuation-free) is
superseded by the full per-row enumeration:

**The inner-schema menus (block G).** §2.2 instantiated at the rows'
decorations, all cases (both-nonzero / one-zero orientations ×
`ν_e`, equal-handshake with `ε ∈ {0, free zero roots, μ}`, NE
extras, q-extras), with the R2.2/L7 shape laws and MP6
(`M_G | Σμ_e`) as filters:

* `(A,B)` inner (`μ = (1,2)`, `w = (2, 3/2)`): both-nonzero PINS
  `(κ̄, X) = (1, −1)` — contradiction; A-zero likewise; B-zero
  yields EXACTLY two schemas — `ν_e = 3`: `(ν, ε, x) = (3, 2, 1)`,
  `κ̄ = 7`, `(d_p, d_q) = (5, 7)`, `M = 1`, merged-vertex gap
  **`7/10`, IN-WINDOW**; `ν_e = 4`: `(2, 2, 1)`, `κ̄ = 10`,
  `(4, 5)`, `M = 1`, gap **`5/4`, IN-WINDOW**. (The `ν_e = 2`
  candidate dies on MP6: `M = 5 ∤ 3`.)
* `(B,B)` `μ = (1,1)`: one schema (`ν = 5`, `(10,16)`, `M = 2`,
  gap `1/10` — out); the cylinder is parity-dead
  (`κ̄ = 3(1+2ν)/2 ∉ Z`).
* `(B,B)` `μ = (2,2)`: six discrete schemas (all windowed out,
  incl. the familiar `(20,16)` at `κ̄ = 4`) **plus exactly one
  parametric family** — §2.2's cylinder-with-free-zero-root
  (`ε = 1`, `C = 0`): `κ̄ = 6ν+3`, `(4ν+1, 2ν+1)`, `M = 1`, type
  `b = −a`, merged-vertex gap `(6ν+3)/(2(4ν+1)) ∈ (3/4, 5/6]` —
  **IN-WINDOW for every `ν >= 2`**.

**The interesting objects and their death (blocks H1–H2).** All
three in-window emissions have solvable, uniquely-typed square
systems (`q = (2/5)a`, `q = a/4`, `b = −a`) — genuine merged charts
whose vertex gap exceeds every 11-C `gap(X) <= 2/3`, so they die
FIRST. And their own death step is **CAP-DEN-refused**: over the
full register lattice and the divisor-complete 11-C caps `{1, 2}`,
`den(α − 1 + gap)` carries a factor `∤ 2` (the `5`-part of `7/10`;
the `4` of `5/4`; the odd factor `(4ν+1)/gcd(4ν+1,3) >= 3` for the
cylinder family — `ν`-lattice to 200 plus the odd-factor law). The
window intruders self-refuse; the kill fires at the merged vertex.

**The stamps (block H3).** All 67 rows DEAD-AT-TIER(`ν >= 2`):
**31 DEAD-UNREALIZABLE** (no schema matches the row's `M_in`: the
28 A-flavor `M_in = 3` rows, 3 `(B,B)` `μ=(1,1)` `M_in = 1` rows),
**21 DEAD-WINDOWED-OUT**, **15 DEAD-SELF-REFUSED** (the rows
carrying the in-window objects). 0 LIVE-AT-TIER, 0 DEFERRED, 0
positive-dimensional components (OB1 never fires here).

**Riders (block H4):** `ν = 1` inner η-modes remain NF-P's (the
stamp is `ν >= 2`-scoped); merged-chart descendant strata and
current-state arrivals stay in the standing perimeter; the `(A,B)`
schemas are conditional on the B-arrival handshake realizing
`ν_e ∈ {3, 4}` — if the refile realizes neither, those rows are
DEAD-UNREALIZABLE instead. Dead either way.

## 6. Perimeter

* `ν = 1` case-I schemas (both η-modes): NF-P's, per §2.2's own
  assignment — nothing here touches them.
* Symbolic incoming records (parametric cylinders): the same square
  system over the parameter field; generic 0-dimensionality gives
  parametric types, and degenerate parameter loci fall to OB1's
  retention. No terminating projection is claimed for symbolic
  scale parameters (the §2.2 caveat stands).
* NF-M-OB1: positive-dimensional components are retained, not
  quotiented. No observed td-7/td-11 instance is
  positive-dimensional (the cylinder's free `g_0` is the scaling
  direction's companion parameter, one type).
* Relative to the promoted L1–L9/R2.2 laws as cited; a consumer
  observing coefficient data outside (frame, degrees, `C`, orbit
  values via L9) re-opens Lemma M3.

## 7. Reproduction

```bash
python3 cases/nfm_check.py     # 18 checks, exit 0 (count printed)
```

Blocks: A the M2 reduction vs direct (L3) on all certificate rows +
random schemas (linear and block orbits); B the M1 cancellation over
the full (ε, ν, mults, blocks, extras) lattice + the square count;
C the Z-Omega/`Q̂ = 1` regressions; D the td-7 rows — exact `C`
match, unique-ratio solves for `Q̂ = 2` (2/3 and 3/2 recovered by
solving, not assuming), the F1 block row, type counts vs `(Q̂−1)!`;
E the cylinder degeneration; F the round-1 conservative outer-`v_2`
screen (historical); G the inner-schema menus (contradiction pins,
MP6 rejections, the exactly-one parametric family); H the square
solves, the self-refusal law, the 67 deterministic stamps
(31/21/15), and the riders. No git commit.
