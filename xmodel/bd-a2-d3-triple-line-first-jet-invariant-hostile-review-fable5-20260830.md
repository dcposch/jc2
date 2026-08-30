# Hostile review: D3 triple-line first-jet invariant gate

Date: 2026-08-30 UTC  
Reviewer: Fable 5 (different-model hostile reviewer)  
Producer under review: Sol 5.6 Ultra (provisional)  
Charged artifacts (all SHA-256 verified byte-exact before reading):

```text
7e73b7a6ebd1c4f6529c8c4502e150de1a8b4e4664d03323bfc8631b03ab08c5
  xmodel/bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md
a389b0a700a96f1ac68f3123f19fc7fa502e31b305e0973f164e50c5d6c585bd
  xmodel/bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md.artifact.json
08c523e2b2dade813d5c12652bfc501ec02de80470f44e3763571387940e852c
  ops/d3_triple_line_first_jet_invariant_replay.py
087953ec71175d8e470cd2aa89dd7928ef0ab88223009c619e2d95dc39287637
  xmodel/bd-a2-d3-hodge-level-divisor-sol56-20260830.md
e571684152a54d9921cc38bdcb9f8833a6f875bda659cf6ebeb8877871246a87
  xmodel/bd-a2-d3-hodge-level-divisor-sol56-20260830.md.artifact.json
```

Custody cross-checks: both `.md` body hashes and byte counts recomputed and
equal to the seal and artifact-JSON values (`69b1cbe2…`/8949 for the gate,
`3f3d7e0c…`/16387 for the upstream theorem); one `BODY-END` marker each; both
canonical documents published read-only 0444; both frozen-basis commits exist
(`7dd85a65` "Freeze hostile review of degree-three Hodge gate", `5cc7b502`
"Freeze ruling-transfer hostile-review prompt").

The mathematics was reconstructed from the stated hypotheses; nothing was
inferred from seals, prior agreement, or campaign status. The upstream
four-row theorem is consumed as the declared provisional hypothesis, exactly
as the gate declares it; this review checks the gate's use of it, not the
theorem itself.

## 0. Itemized verdicts

| # | charge item | verdict |
|---|---|---|
| 1 | normal form, unit + det-one gauge, order-by-order continuation | CONFIRMED |
| 2 | normality iff `G!=0` under smooth generic fibre | CONFIRMED |
| 3 | Hessian normalization, pencil identity, exact `24`/`-216` constants | CONFIRMED |
| 4 | higher-jet independence via seven-dimensional slice + polarization | CONFIRMED |
| 5 | one-way invariant-to-Hodge inference; discriminant redundancy | CONFIRMED |
| 6 | `PGL2` classification `y^2z, q2=0` / `y^3` | CONFIRMED |
| 7 | executable replay | CONFIRM_WITH_CORRECTIONS (hardenings; no false claim) |
| 8 | pricing: necessary local finite-jet gate only | CONFIRMED |

Overall: **CONFIRM_WITH_CORRECTIONS**. No REFUTED item, no GAP. The
corrections are verification hardenings for the replay; no mathematical
statement in the charged gate body changes.

## 1. Item 1 — formal normal form

Write `F1 = a x^3 + x^2 L(y,z) + x Q(y,z) + G(y,z)`. Hand-checked:

- `(1-at)F = x^3 + t(F1 - a x^3) + O(t^2)` removes the `x^3` term at order
  one.
- `(x - (t/3)L)^3 = x^3 - t x^2 L + (t^2/3)xL^2 - (t^3/27)L^3`, so the
  substitution cancels `x^2 L` at order one and pushes everything else to
  `O(t^2)`. The matrix is unipotent over `C[[t]]`, determinant exactly one.
- Neither step touches `xQ + G` at order one, so the gate's `Q, G` are
  literally the corresponding components of the original degree-three base
  coefficient `F1`. No new parameters appear; higher orders are determined.
- Order-by-order continuation: at order `k`, multiply by `1 - a_k t^k` and
  substitute `x -> x - (t^k/3)L_k`. Each step is the identity mod `t^k` and
  fixes all lower orders, so the infinite composition converges `t`-adically
  to a single pair (unit `u ∈ 1 + tC[[t]]`, `M ∈ SL3(C[[t]])`) and every
  coefficient `F_k` lands in the seven-dimensional slice `{xQ + G}`.
- Invariant control is stronger than "valuations preserved": under
  `F -> uF∘M` with `det M = 1`, `c4 -> u^4 c4`, `c6 -> u^6 c6`. Since
  `u ≡ 1 mod t` and all lower Taylor coefficients of `c4` (through `t^2`)
  and `c6` (through `t^3`) vanish identically, the two leading coefficients
  `[t^3]c4`, `[t^4]c6` are preserved exactly, not merely their vanishing
  order. The initial constant `PGL3` normalization of the triple line scales
  the invariants by a nonzero constant, which changes neither vanishing nor
  the classification (0.4).

CONFIRMED.

## 2. Item 2 — normality exactly `G != 0`

On the gauged form, every partial `F_x, F_y, F_z` vanishes identically on
`{x = t = 0}` and `F_t|_{x=t=0} = G(y,z)`; equation (1.1) is correct.

- Necessity (the only direction the gate consumes): `G ≡ 0` puts the whole
  central line in the singular locus, codimension one in the surface, so
  `R1` fails and the germ is not normal. A normal `X` therefore forces
  `G != 0`.
- Sufficiency, under a smooth generic fibre: any one-dimensional component
  of the singular locus either lies in the special fibre — whose reduction
  is the irreducible central line, excluded because `G != 0` makes
  `Sing ∩ {t=0}` the finite zero scheme of `G` — or dominates
  `Spec C[[t]]` and meets the generic fibre, contradicting generic
  smoothness. So `Sing` is finite, the hypersurface in the regular ambient
  threefold is Cohen–Macaulay hence `S2`, and Serre's criterion gives
  normal. No hidden codimension-one singular locus is possible.
- The generic-smoothness hypothesis is genuinely load-bearing for
  sufficiency, not decorative: `F = x^3 + t y^3` has `G = y^3 != 0` yet its
  singular locus contains the horizontal section `{x = y = 0}` (the generic
  fibre is three concurrent lines). The gate's Section 1 and its firewall
  state the hypothesis correctly.

CONFIRMED: under a smooth generic fibre, `G != 0` is necessary and
sufficient; the gate uses only necessity.

## 3. Item 3 — Hessian normalization, pencil identity, exact constants

All constants were re-derived with an independently written SymPy program
(no code shared with the replay), plus hand arithmetic at an integer point.

- Normalization control: `H(xyz) = -(1/2)det d^2(xyz) = -xyz` re-derived;
  the pencil rows give `c4(xyz) = 1`, `c6(xyz) = -1`, consistent with
  `1728·Disc = c4^3 - c6^2` and `Disc(xyz) = 0` for the triangle.
- Structure of (2.2): the classical Hesse–Salmon syzygy says the Hessian of
  a pencil member `F + μH(F)` stays in the pencil. Covariant bookkeeping
  pins the shape: the invariant ring of ternary cubics is `C[S,T]` with
  degrees 4 and 6, so an order-3 covariant of degree 5 must be a multiple
  of `S·F` (no degree-2 invariant exists), and of degree 7 a combination of
  `T·F` and `S·H`. Hence `[μ] = α S F` and `[μ^2] = β T F + γ S H` with
  universal constants. I verified full pencil membership *as polynomial
  identities* (all ten cubic monomials, not just `x^3`): on the
  seven-parameter gate family, on the two-parameter Weierstrass family, on
  `xyz`, and by exact rank tests (`rank[F, [u]-part] = 1`,
  `rank[F, H, [u^2]-part] = 2` with `rank[F,H] = 2`) at three dense random
  integer cubics spanning generic 10-dimensional directions.
- Normalization anchored, signs included: applying the identical extraction
  to `F_W = y^2 z - x^3 - a x z^2 - b z^3` returns `c4 = -48a`,
  `c6 = -864b` — the classical Weierstrass values, i.e. Fisher's
  normalization as used by Cremona–Fisher–Stoll — and
  `(c4^3 - c6^2)/1728 = -16(4a^3 + 27b^2)`, the classical discriminant.
  This pins `α/3` and `(β, γ)` to the doc's constants `(3, 6, -3)` through
  the two-parameter family, on which `(S,T)` is dominant.
- Exact leading terms: on `U = x^3 + t(xQ + G)`,
  `[t^3]c4 = 24(6b0b2q2 - 9b0b3q1 - 2b1^2q2 + b1b2q1 + 6b1b3q0 - 2b2^2q0)`
  and `[t^4]c6 = -216·Disc_binary(G)` verified symbolically, and by hand at
  `Q = (2,-3,5)`, `G = (7,1,-4,3)`: mixed `= -299`, `24·(-299) = -7176`;
  `Disc = -11623`, `-216·(-11623) = 2510568`; both equal the machine
  values.
- Convention (2.4) equals SymPy's univariate cubic discriminant of
  `b0Y^3 + b1Y^2 + b2Y + b3` symbolically; both `mixed` and `Disc` verified
  invariant under an explicit `SL2` shear and rotation. Invariant theory
  independently forces the shapes: torus weights show `[t^3]c4` is bidegree
  `(1,2)` in `(Q,G)` and `[t^4]c6` is degree 4 in `G` alone; since the
  invariant ring of binary cubics is `C[Disc]`, `[t^4]c6` had to be a
  constant times `Disc(G)` — only `-216` needed computing.
- Extra structure confirming the derivation: on the truncated family,
  `c4 = 24·mixed·t^3 + (4q0q2 - q1^2)^2 t^4` exactly and
  `c6 = -216·Disc(G)t^4 + [t^5]t^5 + (4q0q2 - q1^2)^3 t^6` exactly; with
  `Q = 0`, `c6 = -216·Disc(G)t^4` on the nose. This reproduces the upstream
  Section 5 controls independently: `x^3 + t(y^3+z^3)` gets
  `Disc = -19683 t^8` (order eight) and `x^3 + ty^3 + t^2z^3` gets order
  twelve.

CONFIRMED, with the constants now derived rather than trusted.

## 4. Item 4 — higher-jet independence

The argument is a genuine proof, not an experiment, and it checks out:

- The replay's vanishing checks with all seven slice parameters symbolic
  are exactly the statements `C_j|_slice ≡ 0` for the degree-`j` polar
  tensors of `c4` (`j ≤ 2`) and `c6` (`j ≤ 3`) at `x^3`, re-verified
  independently. The slice `{xQ + G}` is a linear subspace, so char-0
  polarization upgrades diagonal vanishing to multilinear vanishing on
  slice tuples.
- Partition bookkeeping for a gauged arc `x^3 + Σ t^k F_k`, all
  `F_k ∈ slice`: `[t^3]c4` receives `C_1(F_3)`, `C_2(F_1,F_2)`,
  `C_3(F_1,F_1,F_1)`; the first two die on the slice, leaving the pure
  first-jet cubic term. `[t^4]c6` receives `C_1(F_4)`, `C_2(F_1,F_3)`,
  `C_2(F_2,F_2)`, `C_3(F_1,F_1,F_2)`, `C_4(F_1^4)`; all but the last die.
  This is precisely why the seven-dimensional slice check (with the gauge
  putting *every* `F_k` into the slice) suffices, and why an arbitrary
  ten-dimensional direction is never needed: the unit factor
  `u ≡ 1 mod t` and determinant-one factors do not shift the two leading
  coefficients (Section 1 above).
- Direct corroboration: six exact numeric probes with random second *and*
  third jets, both slice-only and full ten-dimensional (including `x^3` and
  `x^2L` directions), leave `[t^3]c4` and `[t^4]c6` unchanged.
- Sharpness: the same probes move `[t^5]c6` to six distinct values, so the
  gate's two terms are exactly the maximal first-jet-invariant set; the
  document claims no more.

Execution note: a fully symbolic 14-parameter two-jet membership
computation was started and abandoned as too heavy for this session; the
claim does not rest on it. It rests on the machine-checked slice-vanishing
identities plus polarization (a complete proof) and the exact numeric
probes above.

CONFIRMED.

## 5. Item 5 — invariant-to-Hodge inference

- Direction: the charged upstream theorem gives, at a point of local Hodge
  colength `k`, `v(c4) ≥ 4k`, `v(c6) ≥ 6k` via `c4_plane = s^4 c4_min`,
  `c6_plane = s^6 c6_min`, `v(s) = k`, `v(minimal invariants) ≥ 0`. The
  gate consumes only `k ≥ 1 ⇒ v(c4) ≥ 4 > 3` and `v(c6) ≥ 6 > 4`, killing
  exactly the two displayed leading terms, and `k = 2 ⇒ 8/12` for the
  one-point Halphen row. Both Halphen rows carry a defect unit at the
  triple fibre in the upstream table, so the gate correctly applies to
  both. The converse (bounds ⇒ level) is nowhere used and is explicitly
  disclaimed, correctly, since minimal invariants vanish under additive
  reduction. The Cremona–Fisher–Stoll citation is corroborative
  orientation; the load-bearing identity is the assumed upstream one, with
  no local-solubility hypothesis smuggled in.
- Discriminant redundancy is ideal-theoretic, not merely pointwise: from
  `1728·Disc = c4^3 - c6^2`, every monomial of `[t^j](c4^3)` with `j < 24`
  has three `t`-indices summing to `j`, hence one index `< 8`, so it lies
  in the ideal generated by `{[t^i]c4 : i < 8}`; likewise `[t^j](c6^2)`
  with `{[t^i]c6 : i < 12}`. So all `[t^j]Disc`, `j < 24`, lie in the
  `8/12` elimination ideal and `v(Disc) ≥ 24` adds no generator.

CONFIRMED (conditional, as declared, on the charged provisional upstream
theorem).

## 6. Item 6 — `PGL2` orbit classification

- A nonzero binary cubic over `C` is a product of three linear forms; the
  non-squarefree types are exactly double-plus-simple (`l1^2 l2`,
  `l1 ∦ l2`) and triple (`l^3`), transitive to `y^2z` and `y^3`. Zero is
  excluded by normality (Item 2); squarefree is excluded by
  `[t^4]c6 = -216·Disc(G) = 0`. No orbit is missed.
- `G = y^2z`: `[t^3]c4 = -48 q2` (verified symbolically and numerically),
  so `q2 = Q(0,1) = 0`, i.e. `Q` vanishes at the double root. The `GL2`
  stabilizer of `y^2z` is the diagonal torus (the double and simple roots
  cannot swap), which scales `q2` by a unit; the condition is
  stabilizer-invariant, so the stratum does not secretly refine.
- `G = y^3`: every monomial of the mixed invariant contains `b2`, `b3`, or
  `b1`, so `[t^3]c4` vanishes identically in `Q`, and `Disc(y^3) = 0`; no
  first-jet condition on `Q`. Confirmed term-by-term and by machine.
- Squarefree control `yz(y-z)`: `Disc = 1`, `[t^4]c6 = -216 ≠ 0`,
  eliminating the squarefree transverse stratum from both Halphen rows, as
  claimed.

CONFIRMED, including (0.4) exactly as stated.

## 7. Item 7 — executable replay

Reproduction on Python 3.9.6, SymPy 1.14.0 (the pinned version):

- Ordinary, `-O`, and `-OO` outputs byte-identical, 919 bytes, SHA-256
  `d2da55b85ef0da6eaefd8a1ed38a0c33546a4a82522d6d1c1ebac3ad3c69eede` —
  exactly the charged claim.
- `--mutate-disc-sign` exits 1 with
  `FAIL:binary discriminant sign/control failed`; an unknown argument exits
  1 with `FAIL:unknown command-line argument`.
- AST guard: the source contains zero `assert` statements; the self-scan
  counts AST nodes from the source text, so it is immune to `-O`
  bytecode stripping. Tamper probe on a scratch copy with an injected
  `assert`: caught with exit 1 in both ordinary and `-O` modes. Fail-closed
  behavior confirmed.
- No circular hard-coding: `c4_t3`, `c6_t4`, the discriminant, and all
  controls are derived then `require`-checked against the document's
  formulas; the literal `"0"` strings in the JSON controls are each backed
  by a preceding symbolic `require`. The output hash is version-scoped by
  embedding `sympy_version`, which is honest.

Two hardenings (the corrections):

1. The extraction of `c4`, `c6` uses only the `x^3` coefficients of the
   pencil rows, silently assuming pencil membership (2.2) off that single
   coefficient; membership is fully verified only at `xyz`. If (2.2) had a
   component outside `span{U, H}`, every `require` could still pass with
   wrong invariants. Membership is in fact true — this review verified
   `[u]-part = 3·c4·U` and `[u^2]-part = 6·c6·U - 3·c4·H(U)` identically on
   the gate family (and on the Weierstrass family, plus random-cubic rank
   tests) — but the replay should assert it: two cheap `require`s on the
   already-computed expressions.
2. The replay never pins its normalization to the classical one it is
   interfaced with (harmless here, since the gate consumes valuations
   only, which survive any constant rescaling; still, a one-line
   Weierstrass-anchor `require` — `c4 = -48a`, `c6 = -864b` on
   `y^2z - x^3 - axz^2 - bz^3` — would make the script self-contained
   against convention drift).

Cosmetic: Section 4's "uses SymPy only to perform exact polynomial
differentiation, determinants, coefficient extraction, and factorization"
also covers expansion and substitution; immaterial.

CONFIRM_WITH_CORRECTIONS. Nothing the replay or Section 4 asserts is false.

## 8. Item 8 — pricing and successor

The theorem is priced correctly: a necessary local finite-jet gate at the
possible index-three Halphen fibre, conditional on the provisional four-row
theorem. It is not arc existence, not minimisation, not a global
class-`(3,3)` surface, not a map, not a counterexample, not JC2; Section 0
and the firewalls say so explicitly and the firewalls match FALLACY-v2
discipline (floor vs attainment kept separate throughout).

Cheapest decisive successor (concrete, computed here to be well-posed):
the `k ≥ 1` gate at the triple fibre is not yet exhausted — `v(c6) ≥ 6`
also demands `[t^5]c6 = 0`, which is a *second-jet* condition
(`C_4(F1^3 F2)` plus the first-jet part `C_5(F1^5)`). On the two surviving
strata the first-jet parts collapse (torus weights force them):

- on `G = y^2z, q2 = 0`: first-jet part of `[t^5]c6` is `0`, so
  `[t^5]c6 = 0` is inhomogeneous-linear in the slice second jet
  `(Q_2, G_2)` — one small SymPy job of exactly the replay's shape;
- on `G = y^3`: first-jet part is `864 q2^3`, so `[t^5]c6 = 0` couples
  `q2` to the second jet — again one equation.

That single computation is the cheapest new information on both normal
forms and directly feeds the `k = 2` tower (`c4 mod t^8`, `c6 mod t^12`)
the gate proposes, which should then be organized by the torus-weight
grading (each `[t^N]` coefficient splits into few quasi-homogeneous blocks
`(d_a, d_q, d_b)` with `3d_a + d_q` fixed — e.g. `[t^4]c4` has first-jet
part `(4q0q2 - q1^2)^2` and `[t^6]c6` has `(4q0q2 - q1^2)^3`), with the
residual stabilizer torus used to normalize one further coefficient per
stratum before any saturation, retaining every induced higher term, and
ending in actual minimisation of survivors, per the gate's own Section 5
and the upstream Section 5 successor. CONFIRMED with this refinement.

## 9. Maximum-safe theorem

Let `R = C[[t]]` and let `X ⊂ P2_R` be the hypersurface of a ternary cubic
`F ∈ R[x,y,z]_3` whose special fibre is a triple line, with smooth generic
fibre, and with the germ of `X` along the central line normal. Then:

1. After a constant `PGL3` normalization, a unit rescale, and a
   determinant-one `C[[t]]`-substitution in `x`, `F = x^3 +
   Σ_{k≥1} t^k (x Q_k + G_k)` with `Q_k` binary quadratic and `G_k` binary
   cubic; the pair `(Q, G) := (Q_1, G_1)` consists of the corresponding
   components of the original first coefficient, and normality forces
   `G ≠ 0` (and, with generic smoothness, is equivalent to it).
2. In the classical (Weierstrass-anchored, Fisher/CFS) normalization,
   `v(c4) ≥ 3` and `v(c6) ≥ 4`, with
   `[t^3]c4 = 24(6b0b2q2 - 9b0b3q1 - 2b1^2q2 + b1b2q1 + 6b1b3q0 - 2b2^2q0)`
   and `[t^4]c6 = -216·Disc_binary(G)`, and these two coefficients are
   unchanged by `F_k` for every `k ≥ 2` and by the admissible gauge.
3. If additionally the Hodge colength of the charged upstream comparison at
   `t = 0` is `≥ 1`, then `Disc_binary(G) = 0` and the bracketed joint
   invariant vanishes; hence, up to `PGL2` on the central line, either
   `G = y^2z` with `Q(0,1) = 0`, or `G = y^3` with no first-jet condition
   on `Q`. The squarefree transverse first-jet stratum is impossible in
   both Halphen rows.
4. For colength `2`, `v(c4) ≥ 8` and `v(c6) ≥ 12` are necessary, and every
   `[t^j]Disc`, `j < 24`, lies in the ideal generated by the `c4`/`c6`
   coefficient conditions.

No occurrence, attainment, arc-existence, minimisation, global-surface,
map, or JC2 statement is made or implied.

## 10. Exact dependencies

- **Provisional (charged, different-model review separate):**
  `bd-a2-d3-hodge-level-divisor-sol56-20260830.md` — four-row theorem,
  triple-line form of the `m = 3` fibre, defect unit at the triple fibre,
  and the Hodge-scaling identities (5.1)/(5.3). The gate is conditional on
  it and inherits its provisional status.
- **Classical mathematics:** Serre's normality criterion; Cohen–Macaulay
  property of hypersurfaces in regular ambients; characteristic-zero
  polarization; invariant ring of binary cubics `C[Disc]`; invariant ring
  `C[S,T]` of ternary cubics and the Hesse–Salmon Hessian-pencil syzygy
  (structure classical; constants and membership verified computationally
  in this review on every family used); Fisher's invariant normalization
  anchored at the Weierstrass cubic (verified computationally:
  `c4 = -48a`, `c6 = -864b`); Cremona–Fisher–Stoll level theory used as
  corroboration only.
- **Software (exact rational arithmetic throughout):** SymPy 1.14.0 on
  Python 3.9.6 for the charged replay (hash `d2da55b8…`, version-scoped)
  and for this review's independent scripts.

## 11. Review-constraint compliance

No `jc2-lean` access; no q6 report or sibling external-model prompt, log,
report, or receipt was opened (the sibling `gpt55` files present in
`xmodel/` were left unread); no heavy local CAS (all completed jobs were
replay-scale, seconds to ~21s; one heavier symbolic probe was started,
found slow, killed, and replaced by the proof-plus-numeric route disclosed
in Section 4); no inputs, Git state, or canonical artifacts edited; all
scratch work in temporary directories. This review makes no exit-price
assertion and emits no `charge_basis` line; receipt status `ABSENT` is
expected.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20761`.
- Body SHA-256:
  `1af7e69e4b269ea2e8903606616628438c9b71a3a6e96c4da080a205c41be5da`.
- Frozen basis: `81c1db3fb787749562894c83439d327a10d19d70`.
