# Blind full-portfolio ideation — round 20260831T1033Z — opus5

Packet hash verified: `196e1700fbc46855c5ebd3dbb5d28997cfa1b56a0ba75c0a3049c03dfb55b476`.

Packet hash verified against the frozen copy:
`196e1700fbc46855c5ebd3dbb5d28997cfa1b56a0ba75c0a3049c03dfb55b476`.
All five frozen inputs read (APPROACHES.md overlays + 46-row inventory,
AUDIT.md current-state block, three integrations). No CAS was run; every
number below is hand arithmetic.

## 0. Packet statements I flag

**F1 (compression that mis-ranks, not an error).** The six-line state
summary says "rank four is an irreducible one-place frontier". The
promoted `m=1` theorem is stated for *every actual rank-four **proper
block***; the primitive / no-proper-block branch at generic degree four
is untouched by today's news and is not named in the summary. The
06:55Z overlay does retain that front explicitly ("Retain reducible,
multiple-place, and primitive/no-proper-block fronts"), so this is a
packet compression, but a reader ranking avenues off the summary alone
will underweight primitivity. It matters here because the mechanism I
give in §3 is **block-free** — it needs no block hypothesis at all —
and therefore reaches the primitive branch too.

**F2 (avoidable dependency).** The `m=1` chain's link 3 rests on
Orevkov's dicritical formula, typed at content level only: the
integration records "block quotes are normalized transcriptions, not
byte-exact" and "a clean byte-hashed Orevkov acquisition is queued".
The budget `N-1 = 3` is therefore load-bearing on an un-byte-hashed PDF.
§3 re-derives the same budget (`d-1` sheets lost over `A_F`) from
Euler-characteristic additivity plus covering-space theory, with no
Orevkov input. That is worth banking purely as custody de-risking, even
if nothing else in this report is adopted.

**F3 (a cheaper route than the packet's).** The packet says the
`Theta_h` datum "awaits one SNC boundary model". Two already-promoted
facts short-circuit part of it: the mandatory clause
`gamma_h=(d_h-r_h-2)/2` forces `Theta_h` **even and non-negative**, and
the promoted one-cusp theorem (no `A1`, no `C*` generic coordinate
fibre, on `R=C[A,U,Z]/(U^2-A-A^2Z)`) forces the general fibre to be
hyperbolic, i.e. `e(fibre) = 2-2*gamma_h - n <= -1` with `n>=1` places.
Hence `2*gamma_h + n >= 3`: either `gamma_h >= 1` (so `Theta_h >= 2`,
`d_h >= r_h+4`) or `n >= 3`. A parity-and-sign computation of
`Theta_h mod 2` plus the puncture count `n` is strictly cheaper than
the SNC model and kills or pins rows before it is built. See §6.

**No statement in the packet is, as far as I can check, wrong.**

## 1. Disposition vector over the 46-row avenue inventory

Scope note: I score the *avenue*, not any single packet. "raise"/"lower"
are relative to the position implied by the 2026-08-31 10:32Z overlay.
Rows with no change carry no reason, per the charge.

| # | Approach (short) | Disp. | Reason (changes only) |
|--:|---|---|---|
| 1 | GGV corner farm | unchanged | |
| 2 | Sheet ladder / Eggers–Wall / dicritical trees | unchanged | Still the backbone; §3 feeds it rather than replacing it. |
| 3 | Vertex-gap / strip ODEs | unchanged | |
| 4 | Formal-germ certification + algebraization | unchanged | |
| 5 | JvdK degree descent / amalgam | unchanged | |
| 6 | Abhyankar–Moh one-place / coordinate recognition | **raise** | Consensus item 3 says AM was run on the wrong object and "the correct one-place objects are `A(F)` components, whose place data are unpinned". Today pins them: `m=1`, `normalization=A1`, one place at infinity. The stated blocker is gone; AM/semigroup theory now applies to the *right* object. |
| 7 | Jelonek asymptotic variety `A(F)` | **raise** | Same reason from the other end, plus §3: `A_F` is irreducible, `A1`-normalized, and its Euler characteristic is now *forced* by a one-line identity. "`A(F)` is never constructed" weakens to "`A(F)` is now numerically constrained without construction". |
| 8 | Formal-inverse combinatorics | unchanged | |
| 9 | Lee–Li Conjecture E | unchanged | |
| 10 | HC4 ⇒ JC2 | unchanged | Stopped at `NO LEVERAGE`; not revived. |
| 11 | Mathieu/GMC/Zhao ladder | unchanged | Refuted. |
| 12 | Face isolation / p-adic multinomials | unchanged | |
| 13 | Dixmier DC(2) | unchanged | |
| 14 | End(A_1) / Zheglov audit | unchanged | |
| 15 | Spectral surfaces / commuting PDOs | unchanged | |
| 16 | D-module / holonomic index | unchanged | |
| 17 | BCW / Druzkowski / Yagzhev | unchanged | |
| 18 | Graded / equivariant / GIT | unchanged | Closed by Shaska 2026. |
| 19 | Char-p CEs + Witt lifting | **lower** | §4 connection B: in char `p` the Euler budget identity of §3 fails *exactly* by the Swan conductor (Grothendieck–Ogg–Shafarevich); wild ramification is precisely what supplies the missing `d-1`. That is a structural explanation of why char-`p` collisions exist and why every observed lift needs growing support. The lane's residual information is lower than "open search" pricing implies. |
| 20 | Reduction mod p / p-curvature | unchanged | |
| 21 | p-adic injectivity / Hensel / model theory | **lower** | Same mechanism: the obstruction to descending is the wild part, now named. |
| 22 | Diophantine integral points | unchanged | |
| 23 | Analytic global inverse | unchanged | |
| 24 | Real JC / Pinchuk | unchanged | |
| 25 | Fibre monodromy / dessins / passports | **raise** | The stuck-point of record is "Riemann existence is generous; single-cover passports ignore the second coordinate and Jacobian contacts". §3 supplies the missing coupling in the cheapest possible currency: an **exact identity** linking `#Fix` of every local inertia group to the Euler characteristic of `A_F`. Passports stop being free. |
| 26 | Primitive-monodromy bound / function-field Galois | **raise** | The §3 mechanism needs no block: Zariski's Main Theorem supplies the finite-flat factorization for *any* Keller pair. So the primitive branch is no longer a mechanism-free zone, and results previously gated on the block dichotomy are partly unconditional. |
| 27 | Links at infinity / splice diagrams | **lower** | `m=1` retires the multi-component splice targets by theorem (integration §1), and §3 kills the single-node configuration at every degree by arithmetic. What remains for splice diagrams is a narrower unibranch slice already covered by row 2. |
| 28 | Log surfaces / BMY / log-Kodaira | **raise** | Two new cheap facts: `kappa-bar(Y) = -infty` for the intermediate surface (`Y` contains `A^2` as a Zariski-open, and `kappa-bar` is non-decreasing on opens), and the Euler ledger is no longer the "predicted non-result" — it now yields the exact identity of §3. |
| 29 | LND / Hamiltonian completeness / commuting frames | **reopen (new scope)** | The scoped gate that closed this row was run on `C[x,y]`. `kappa-bar(Y)=-infty` forces an `A^1`-fibration on the *intermediate* surface `Y`, i.e. a nonzero LND on `C[Y]`, whose degenerate-fibre combinatorics is pinned by `Cl(Y) = Z^{m_Y}` (§3). This is a different ring, not a resurrection of the closed statement. |
| 30 | Affine-surface classification / ML invariant / exotic surfaces | **raise** | §3: `Cl(Y)` is **free** of rank `m_Y` (torsion-free — the units sequence gives it in three lines), `pi_1(Y)=1`, `kappa-bar(Y)=-infty`. That is a Danielewski/Gizatullin-type recognition problem with an explicit fibration count `sum_i (k_i - 1) = m_Y` and no multiple single-component fibres. The row's complaint ("impossible rather than a recognition") is answered. |
| 31 | Integrality / ZMT / Rees valuations | **raise** | ZMT is doing real work in §3 rather than "exposing" the gap: it gives, unconditionally, `A^2 =~ U ⊂ Y --q--> A^2` with `q` finite flat of degree `d`, `Y` normal, `q` étale off `Y\U`, and `A_F = q(Y\U)`. |
| 32 | Off-diagonal collision ideal | unchanged | |
| 33 | Global symplectic exactness / action residues | unchanged | `COSTUME` verdict stands; note that transporting it to `Y` does not help — `pi_1(Y)=1` so `H^1_dR(Y)=0` and primitives still exist. Recorded as a *closed* check, not a revival. |
| 34 | 2D tangent sweep / pole removal | unchanged | |
| 35 | Descent of dim>=3 CEs | unchanged | |
| 36 | Guided CE search (SAT/sparse) | unchanged | |
| 37 | Finite-field census | unchanged | |
| 38 | Tropical geometry | unchanged | |
| 39 | Cohomological cluster (K2, motivic, prismatic) | **raise** | Grok's stated bar was "refuse to start until a 10-line class is written". §3 writes it: compactly-supported Euler characteristic (and, in char `p`, the Grothendieck–Ogg–Shafarevich Euler–Poincaré formula) is a named, computable invariant that is *not* blind to sheets and that produces an exact identity. It is the low-tech end of this row, and it works. |
| 40 | Free-associative lift | unchanged | |
| 41 | Naive scaling deformation | unchanged | Falsified. |
| 42 | Markus–Yamabe | unchanged | |
| 43 | Ritt decomposition | unchanged | |
| 44 | Moskowicz "no prime td" | unchanged | Refuted-as-proof. |
| 45 | Differential Galois / Liouvillian | unchanged | |
| 46 | Lean / formal certification | unchanged | |

Net: 9 raises (6, 7, 25, 26, 28, 30, 31, 39 plus the scoped reopen of
29), 3 lowers (19, 21, 27), 1 reopen (29), 33 unchanged. Every raise
traces to the same mechanism, which is the point of §3.

## 2. Bottleneck reranking

### Proof bottlenecks (ranked)

1. **Attainment/realizability of the surviving unibranch delta-sequences.**
   The ladder is saturated and cannot close another genus; nothing in the
   portfolio currently converts "colourable delta-sequence" into "actual
   charged curve". *(§3 gives the first attainment instrument: an exact
   identity constraining the local inertia groups of every cusp.)*
2. **No absolute or cofinal degree ceiling.** Unchanged as the deepest
   gap and still the consensus diagnosis; every promoted exclusion is
   degree-four-scoped or class-scoped. *(§3 is degree-uniform, which is
   why I rank it below only attainment.)*
3. **Primitivity / the no-proper-block branch.** Structurally untouched
   all day and, per F1, invisible in the packet summary. Rises to third
   because everything else at rank four is now closed or reduced.
4. **The `m>=2` (several-component `A_F`) case at general degree.** The
   promoted `m=1` is degree-four-only; the same dicritical count gives
   at best `m <= floor((d-1)/2)` at degree `d`, so higher degrees keep a
   reducible frontier that degree four no longer has.
5. **`Theta_h` for the one-cusp horn.** One datum, one model; ranked
   fifth only because it is cheap and scheduled, not because it is easy.
6. **Arbitrary-surface `(2.3')` and Prop. 4.3 / Cor. 5.5 (C3).**
   Recorded GAPs with repair paths; they block export of the plane
   result to other surfaces.

### Disproof bottlenecks (ranked)

1. **Algebraization.** Formal germ ⇏ algebraic ⇏ polynomial. Every
   disproof lane terminates here and none of today's news moves it.
2. **Uniform support/degree in char-`p` lifting.** Now *explained*, not
   merely observed: §4 identifies the Swan conductor as the exact
   quantity a char-0 limit must destroy. Explanation lowers the lane's
   information value (rows 19/21 lowered) without closing it.
3. **Search volume above the classical firewalls.** Moh removes bounded
   degree eight; above it the space is enormous with no pruning
   invariant. *(§3's identity is the first candidate pruning invariant
   that is cheap to evaluate on a candidate.)*
4. **No candidate object.** End(A_1)/Dixmier have no witness to audit;
   refuting a proof there still yields no counterexample.

**Rank change of note:** disproof bottleneck 2 moved from "open
empirical question" to "named structural obstruction", and proof
bottleneck 3 (primitivity) moved *up* because the block-free character
of §3 makes it the only branch with no live mechanism at all.

## 3. New avenue / mechanism

### THE EULER–INERTIA BUDGET: an exact identity coupling `A_F`, its
### singular local groups, and the degree

Nothing in the 46-row inventory or in any overlay uses compactly
supported Euler characteristic as a *primary* instrument; row 28 records
the Euler ledger as "passes identically (the predicted non-result)" and
the Grok one-cusp review explicitly "rejected an Euler/covering-space
shortcut". That rejection was correct for the shortcut it addressed
(non-proper étale maps do not have constant fibre cardinality). The
mechanism below never assumes constant cardinality; it *computes* the
drop.

**Setup and standing hypotheses.**
`F: A^2 -> A^2` polynomial, étale (Keller), not an automorphism,
`d = [C(x,y):C(F_1,F_2)] >= 2`. `A_F` = Jelonek's non-properness set,
a curve, pure codimension one (Jelonek, *The set of points at which a
polynomial map is not proper*, Ann. Polon. Math. 58 (1993) 259–266).
Write `D := A_F`.
- **(H2)** `D` is irreducible — promoted today at rank four (`m=1`).
- **(H3)** `normalization(D) =~ A^1` — promoted (`5d7df7ce...:84-104`).

**Step 0 (free factorisation; no block hypothesis).** Let `Y` be the
normalisation of the target `A^2` in `C(x,y)`. Then `q: Y -> A^2` is
finite, `Y` is normal, and by miracle flatness (`Y` Cohen–Macaulay over
a regular base, equidimensional) `q` is finite **flat** of degree `d`.
`F` factors through `Y`; the induced `A^2 -> Y` is birational and
quasi-finite, hence by **Zariski's Main Theorem an open immersion**
`A^2 =~ U ⊂ Y`. `B_Y := Y \ U` is pure codimension one (an affine open
in a normal variety has pure-codimension-one complement), and
`A_F = q(B_Y)` exactly (a limit escaping `U` with bounded image is
trapped in a `q`-compact set, and conversely `U` is dense). *This
reproduces the block-descent architecture with no block hypothesis.*

**Step 1 (the budget identity).** By definition `F` is proper over
`A^2 \ D`; it is étale; `A^2 \ D` is connected. Hence
`F: F^{-1}(A^2\D) -> A^2\D` is a `d`-sheeted covering and
`e(F^{-1}(A^2\D)) = d * e(A^2\D)`. Compactly supported Euler
characteristic is additive on the decomposition
`A^2 = F^{-1}(A^2\D) ⊔ F^{-1}(D)` and agrees with ordinary `e` for
complex algebraic varieties, so

> **(E)  `1 = d*(1 - e(A_F)) + e(F^{-1}(A_F))`.**

Sanity: `A_F = ∅` gives `1 = d`, i.e. the classical "proper étale
self-map of `A^2` is an automorphism". So (E) is exactly the
quantitative form of that classical argument: **failure of properness
must pay `d-1` units of Euler characteristic.**

**Step 2 (local inertia bookkeeping).** Let `g in S_d` be the image of a
meridian of `D` under the transitive monodromy
`pi_1(A^2\D) -> S_d` (transitive because `F^{-1}(A^2\D)` is the
complement of a curve in `A^2`, hence connected). All meridians of an
*irreducible* curve are conjugate — this is precisely correction **C1**
bound on the promoted one-node theorem — so `sigma := #Fix(g)` is well
defined. `g != 1` (else the covering extends over the generic point of
`D` and `D ⊄ A_F`), hence `sigma <= d-2`.
For `p in D` let `H_p <= S_d` be the image of the local fundamental
group of the germ (generated by the meridians of the `r_p` local
branches) and `s_p := #Fix(H_p)`. Since `F` is étale, a point of
`F^{-1}(p)` has a neighbourhood mapping isomorphically, i.e. it is a
*trivial* local orbit; conversely a trivial orbit fills in. Therefore
**`#F^{-1}(p) = s_p`**, and `0 <= s_p <= sigma` (a conjugate of `g`
lies in `H_p`). Over `D \ Sing(D)` the local group is `<g>`, so
`F^{-1}(D\Sing D) -> D\Sing D` is a genuine `sigma`-sheeted covering.

**Step 3 (assemble).** With `s := #Sing(D)`, `nu := sum_p (r_p - 1)`
(total branch excess; `nu = 0` iff `D` is unibranch everywhere), (H3)
gives `e(D) = 1 - nu`, and
`e(F^{-1}(D)) = sigma*(e(D) - s) + sum_{p in Sing D} s_p`.
Substituting into (E):

> **(M)  `sigma * (nu + s - 1)  -  sum_{p in Sing(A_F)} s_p  =  d*nu - 1`,**
> with `1 <= sigma <= d-2` and `0 <= s_p <= sigma`.

(M) is an **exact identity**, not an estimate. Everything in it is
combinatorial data the campaign already computes for census rows.

### What (M) delivers immediately

**(a) The promoted all-degree one-node theorem, reproved in three lines
and generalised.** Sole affine singularity an ordinary node: `s=1`,
`nu=1`, so (M) reads `sigma * 1 - s_p = d - 1`, i.e.
`sigma - s_p = d-1`. But `sigma <= d-2` and `s_p >= 0`. **Contradiction
for every `d >= 2`.** The promoted theorem
(`c61f0ceb...`, `CONFIRM_W_CORR`) needed `d>=4`, a one-place hypothesis,
a transposition class, corrected Neumann–Rudolph goodness, node
smoothing, Neumann's minimal-Seifert theorem, genus-one graph-knot
classification and the trefoil's meridian rank. (M) needs none of them —
only (H2), (H3) and `d>=2`. This is the strongest available control on
the mechanism: it reproduces a promoted result from a disjoint
direction, and strengthens it.

**(b) A general node-count obstruction.** Feeding `s_p <= sigma` and
`sigma <= d-2` into (M):
> **`(d-2)*(s-1) >= 2*nu - 1`.**
At `d=4`: **`s >= nu + 1`** — the number of singular points of `A_F`
must strictly exceed its branch excess. In particular at degree four a
single non-unibranch point is impossible unless another singularity
accompanies it, and `s=1` forces `nu=0` (the surviving configuration is
exactly *unicuspidal*, which is the campaign's live one-cusp horn).

**(c) An exact cusp-local-group law (the attainment instrument).** When
`nu = 0` (all singularities unibranch — the surviving frontier), (M)
collapses to
> **`sum_{p} s_p = sigma*(s-1) + 1`.**
For the charged quartic *transposition* class, `sigma = 2`, so
`sum_p s_p = 2s-1`: **exactly one cusp has `s_p = 1` and every other
cusp has `s_p = 2`.** `s_p = 2 = sigma` forces `H_p = <g>` cyclic of
order two, i.e. *the local knot group of that cusp maps abelianly*: all
its meridians go to the same transposition. For `sigma = 1` (generic
inertia a 3-cycle) every cusp must satisfy `s_p = 1`, forcing every
`H_p` to be cyclic of order three. Either way the cusp local
representations are pinned, and the pinning is checkable directly from
the Puiseux/iterated-torus data the census already carries.

**(d) The Orevkov budget, re-derived.** Over a generic point of `D`
exactly `sigma` sheets survive and `d - sigma` escape, distributed as
the non-trivial cycles of `g` — cycle length = ramification index of the
corresponding `B_Y` component = dicritical multiplicity. So the total
sheet loss is `d - sigma >= 2` and the promoted "generic branch
partition `(2,1,1)` or `(3,1)`" is exactly "`g != 1`". The `N-1 = 3`
budget at `d=4` is the Euler cost of non-properness. **This discharges
the un-byte-hashed-Orevkov custody risk (F2) for the budget itself.**

**(e) Structure of the intermediate surface, free.** From Step 0: the
units/localisation sequence
`C[U]^* / C[Y]^* -> Z^{m_Y} -> Cl(Y) -> Cl(A^2)=0` with
`C[Y]^* = C[U]^* = C^*` gives **`Cl(Y) =~ Z^{m_Y}` — free**, where
`m_Y = #`components of `B_Y`. Since `A^2 ⊂ Y` is Zariski-open and
`kappa-bar` does not decrease on opens, **`kappa-bar(Y) = -infty`**;
`pi_1(A^2) ↠ pi_1(Y)` gives **`pi_1(Y)=1`**. For smooth `Y`,
Miyanishi–Sugie/Fujita then give an `A^1`-fibration over `A^1` whose
degenerate fibres satisfy `sum_i (k_i - 1) = m_Y` with **no multiple
single-component fibre** (that would put torsion in `Cl(Y)`), and
`e(Y) = 1 + m_Y`. Two side-effects: `Cl(Y) != 0` re-proves
"`Y` is not `A^2`" in one line, and every torsion-in-`Cl(Y)` /
cyclic-torsor argument on `Y` is dead by theorem.

### Honest gaps and scope

- (M) needs (H2)+(H3). At rank four both are promoted; elsewhere they
  are hypotheses. Without (H3), `e(D) = e(D-tilde) - nu` with
  `e(D-tilde) <= 1`, so (M) becomes an inequality in the same direction
  and (a) survives whenever `e(D-tilde) = 1`.
- The `m >= 2` version needs `e(A_F) = sum_i e(D_i) - (identifications)`
  and one `sigma_i` per component; the identity generalises but the
  clean corollaries (a)–(c) do not transfer verbatim. Typed **OPEN**.
- I claimed at one point in derivation that every component of
  `F^{-1}(D)` is finite over `D`; that is **false in general** (a
  component's closure in `Y` may meet `B_Y`), and I do not use it. (M)
  as stated is independent of it. Recording the discarded step so no
  successor re-imports it.
- Smoothness of `Y` is used only in (e), not in (M); for normal `Y`
  run (e) on a resolution containing `U`.

## 4. New connection between existing avenues

**Connection A — row 6 x row 7, unblocked by today's news (the one the
survey consensus asked for).** Consensus item 3 in APPROACHES is that
Abhyankar–Moh "was run on the wrong object" and that the right objects
are `A(F)` components "whose place data are unpinned". Today pins them
completely: `m=1` makes `A(F)` irreducible, `normalization = A^1` makes
it a polynomial curve, and the promoted one-place structure gives it a
single place at infinity. So rows 6 and 7 are now **one avenue**: `A_F`
is a one-place-at-infinity `A^1`-parametrised plane curve, exactly the
object AM/Assi–García-Sánchez semigroup theory governs — and exactly the
object the delta-sequence ladder already enumerates. The ladder was
built as a *knot-colouring* screen on the charged branch; connection A
says it is simultaneously an *AM semigroup* screen on `A(F)`, so the two
inventories' stuck-points cancel rather than compound.

**Connection B — rows 28/39 x rows 19/21: the Swan conductor is why
char-`p` counterexamples exist.** Identity (E) rests on one fact:
a finite étale cover of degree `d` multiplies compactly supported Euler
characteristic by `d`. In characteristic `p` this is **false**, and the
exact failure is the Swan conductor: Grothendieck–Ogg–Shafarevich gives
`chi_c(U, sheaf) = rk * chi_c(U) - sum_x Swan_x`, and the
Artin–Schreier cover `A^1 -> A^1`, `x |-> x^p - x`, is finite étale of
degree `p` with `e_c = 1` on both sides. So the classical "`A^2` is
simply connected, hence a proper étale self-map is an automorphism"
argument — and its quantitative form (E) — fails in char `p` **exactly
by the wild part**. This is a structural explanation, not an analogy,
for the campaign's own char-`p` record: the Mondello `F_2` stratum, the
explicit `F_3` Artin–Schreier collision confirmed through every Witt
level, and the observation that its limit is "restricted-analytic, not
polynomial" because the support has to grow. A char-0 polynomial limit
must annihilate a Swan conductor that is the only thing paying for the
map's existence. This connects a proof-side instrument to the two
disproof-side rows and is the evidence behind lowering 19 and 21.

**Connection C — row 29 x rows 30/31, at a new ring.** Row 29's LND gate
was completed on `C[x,y]` and is closed there. Step 0 + (e) of §3 give,
unconditionally, a second ring: `C[Y]` with `kappa-bar(Y) = -infty`,
`pi_1(Y)=1`, `Cl(Y) = Z^{m_Y}` free. `kappa-bar = -infty` on a smooth
affine surface *is* the existence of a nonzero LND, so row 29's machine
runs on `C[Y]` with its degenerate-fibre count fixed by `Cl(Y)`
(`sum_i (k_i-1) = m_Y`, no multiple single-component fibre). Row 30's
"recognition problem" and row 31's ZMT are the two halves of producing
that ring. The three rows become one pipeline: ZMT builds `Y`, class
group and `kappa-bar` classify it, LND theory computes on it.

## 5. Strongest proof attack and strongest falsification attack

### Strongest proof attack: the cusp-local-group law as an attainment filter

The saturation result says the colouring ladder can no longer *exclude*
a conductor; the surviving rows are exactly those admitting a
meridian-to-transposition colouring. Identity (M) at `nu = 0` turns
colourability from a *permission* into a *quota*:

> `sum_{p in Sing(A_F)} #Fix(H_p) = sigma*(s-1) + 1`, `sigma = #Fix(g)`.

In the charged quartic transposition class `sigma = 2`, so the quota is
`2s - 1`: **exactly one cusp may have a two-generated local image
(`#Fix = 1`, forcing `H_p =~ S_3` inside a point stabiliser), and every
other cusp must have cyclic local image `<g>` (`#Fix = 2`).** For a
unicuspidal row (`s=1`) the quota is `1`: the single cusp's local group
must have exactly one fixed point, i.e. the cusp knot must admit a
meridian-to-transposition representation **onto `S_3`, not onto `Z/2`
and not onto anything with a different fixed-point count**.

*Cheapest decisive first computation (desk-scale, reuses banked data):*
the ladder census already enumerates charged colourings row by row
(counts `72`, `72/24/72`, `8`, and the exact `6x3` odd-residue table are
all banked). **Add one column: for each enumerated colouring, the number
of points of `{1,2,3,4}` fixed by the image subgroup.** Then apply the
quota. No new enumeration, no CAS, no new theory — a fixed-point count
on tuples already written down. Outcomes: a surviving row whose every
colouring violates the quota is **dead**; a row where the quota selects
a proper subset of colourings is **sharpened** (and its successor
analysis shrinks); a row where all colourings satisfy the quota is
**unchanged but now typed**. Because the quota is an equality, it can
kill rows that colourability alone cannot — which is precisely the
capability the saturation result says the ladder lacks.

### Strongest falsification attack: the canonical-class sieve on `Y`

The disproof side has no candidate object; §3 hands it a **classified**
one. `Y` is a normal affine surface with `pi_1(Y)=1`,
`Cl(Y) =~ Z^{m_Y}` **free with basis the components of `B_Y`**,
`kappa-bar(Y) = -infty`, containing `A^2` as the complement of `B_Y`,
and carrying a finite flat degree-`d` map `q` to `A^2` étale off `B_Y`.
Riemann–Hurwitz for `q` (tame, char 0, `K_{A^2} ~ 0`) gives

> **`K_Y ~ sum_j (e_j - 1) [B_{Y,j}]` in `Cl(Y) = ⊕_j Z[B_{Y,j}]`,**

with at least one `e_j >= 2` (if every `e_j = 1` then `q` is finite
étale over the simply connected `A^2`, forcing `d=1`). Since the basis
is free, **`K_Y != 0` in `Cl(Y)`**. Hence:

> **Corollary.** The intermediate surface of a hypothetical plane Keller
> counterexample never has trivial canonical class. In particular it is
> **not** a smooth hypersurface or complete intersection in any affine
> space (adjunction makes `K` trivial there).

*Cheapest decisive first computation (minutes, by hand):* the smallest
candidate. `Y_1 = {xz = y^2 - 1} ⊂ A^3` is smooth, `pi_1 = 1`,
`Cl(Y_1) = Z`, and `Y_1` minus one line of its degenerate fibre **is**
`A^2` (after deleting `{x=0, y=1}` the projection to `A^1_x` has every
fibre a reduced `A^1`, hence is a trivial `A^1`-bundle over `A^1`). So
`Y_1` satisfies every structural requirement. But `K_{Y_1} ~ 0` by
adjunction, so no admissible `q` exists — **`Y_1` and the whole
Danielewski family `{x^n z = P(y)}` are excluded in one line.** This is
the first time the counterexample side has a *finite classified family*
to sweep rather than an unbounded coefficient search; the sieve costs a
canonical-class computation per candidate. Outcome interpretation: a
surface passing the sieve is the strongest counterexample lead the
campaign has ever had; a proof that no surface passes it is JC2 at
degree `d`.

## 6. Software acceleration / decisive experiment

**Software acceleration — `euler_inertia_check.py` (pure Python, no
CAS, no network, deterministic, < 100 lines).** Input: one census row in
the format the ladder already emits — the delta-sequence / singularity
multiset of the charged curve, plus the enumerated meridian tuples in
`S_4`. Output, per row: `s`, `nu`, `e(A_F) = 1 - nu`, `sigma = #Fix(g)`,
`#Fix(H_p)` per singular point (as the subgroup generated by that
point's meridian tuple), the residual of identity (M), and a
`PASS/KILL` verdict with the violated clause named. Three properties
make it worth writing rather than doing by hand: it is total (every
banked row can be replayed), it is mutation-testable (perturb one
`#Fix` and the verdict must flip), and it is *degree-generic* — the same
file runs at `d=5,6,...` the moment `(H2)`/`(H3)` are available there.
Cost is an hour; it consumes only banked data; it has no CAS dependency,
so it cannot fail-open the way `sat()`-wrapped or `-O`-stripped replays
have.

**Decisive experiment — `Theta_h` without the SNC model.** Per F3, two
promoted facts already constrain `Theta_h = d_h - r_h - 2`: the
mandatory clause forces `Theta_h` even and `>= 0`, and the promoted
hyperbolic-generic-fibre theorem forces
`e(fibre) = 2 - 2*gamma_h - n <= -1` with `n >= 1` places at infinity,
i.e. `2*gamma_h + n >= 3`. So compute, in this order:
1. `n` — the number of places at infinity of the general coordinate
   fibre, readable off the promoted boundary structure `(1.12)`–`(1.14)`
   and the local flow-divisor formulas `(2.1)/(2.4)`, all promoted at
   local scope;
2. `Theta_h mod 2` from the same local data (parity of `d_h - r_h`);
3. only then, if steps 1–2 leave more than one partition row alive, the
   full SNC model.
If `n <= 2` then `gamma_h >= 1`, hence `Theta_h >= 2` and
`d_h >= r_h + 4` — which by itself may pin the partition row. Expected
saving: the SNC boundary model, which is the single most expensive
scheduled item in the one-cusp lane. Expected risk: steps 1–2 may
under-determine the row, in which case nothing is lost but the ordering.

## 7. Campaign-systems check

### `UPGRADE` card — `REPLAY-SEMANTICS/v1`

**Defect class, evidenced three times in the frozen inputs.** Replays
are passing without testing anything load-bearing.
- Sol's review of the component-tree ledger: "the replay is semantically
  shallow (hard-coded rows, tautological `require(3<=3)`, a broken
  `orbit_size`)" — and the coordinator had already verified that same
  replay "byte-identically in normal/`-O`/`-OO` and all three documented
  mutations exit 1". So the *strongest* replay discipline the campaign
  has (three interpreter modes plus documented mutations) certified a
  replay whose assertions were vacuous.
- The corrected local degree-cap review: "the embedded R1 replay
  hand-entered its binary quartic; future regression code must derive
  that input mechanically."
- Custody note: the launcher/receipt layer is clean (twelve lanes,
  DONE/BODY_SEALED, inputs `UNCHANGED`), so the failure is *not* in
  custody. It is in what the replay asserts.

**Smallest useful implementation (a linter, not a framework; ~60 lines,
one afternoon, no dependencies).** `ops/replay_lint.py`, run in CI over
every `ops/*_replay.py`, failing the lane on any of:
1. **Tautology check.** Any assertion whose two operands are
   syntactically identical, or are both literal constants, is a hard
   fail. (`require(3<=3)` dies.)
2. **Hand-entry check.** Any literal numeric array of length `>= 4` that
   is not derived from a frozen input file within the same script is
   flagged; the script must either read it from a charged input or
   compute it. (The hand-entered binary quartic dies.)
3. **Constant-mutation coverage.** For each numeric constant reachable
   in the assertion graph, auto-perturb it by `+1` and re-run; the
   replay must exit non-zero. Any constant whose perturbation still
   passes is reported as **dead weight** — this is the check that would
   have caught `orbit_size`. Documented hand-written mutations remain,
   but coverage stops being author-chosen.
4. **No bare `assert`.** Assertions must be explicit `if ...: raise`,
   because `assert` is erased under `-O`; the three-mode replay
   discipline currently *hides* this rather than catching it (a replay
   whose only checks are `assert` passes `-O` vacuously).

**Why this and not more.** It is a static/dynamic linter over existing
artifacts; it changes no promotion rule, adds no review load, and is
falsifiable on day one by running it against the already-quarantined
ledger replay — if it does not flag `require(3<=3)` and `orbit_size`,
the card is wrong and should be dropped. **Acceptance test:** run it on
the two banked replays whose defects are already documented; it must
flag both, and must not flag the conductor-census replay whose stdout
hash reproduced in three modes and whose mutations are real.

## 8. Idea cards

### Card 1 — `EULER-INERTIA/M`: bank identity (M), then run the quota filter

**Statement to bank.** `sigma*(nu+s-1) - sum_p s_p = d*nu - 1` under
(H1)+(H2)+(H3), with `1 <= sigma <= d-2`, `0 <= s_p <= sigma`.
**Dependencies.** Promoted: `m=1`; `normalization(B_i)=A^1`; correction
C1 (all meridians of an irreducible curve conjugate). External: Jelonek
1993 (`A_F` a curve); ZMT; additivity of `e_c`. No Orevkov, no
dicritical typing, no `(2.3)/(2.3')`, no block hypothesis.
**Cheapest discriminator.** The one-node control: `s=1, nu=1` gives
`sigma - s_p = d-1` against `sigma <= d-2`. If (M) does **not**
reproduce the promoted all-degree one-node exclusion, (M) is wrong and
the card dies immediately — this is a same-day, zero-cost falsification
test against a promoted theorem.
**Outcomes.** *Reproduces it:* bank (M) and run §5's quota column.
*Fails to reproduce it:* discard the card; the error will be in Step 2
(`#F^{-1}(p) = #Fix(H_p)`), which is where I would look first.
*Reproduces it but the quota kills no surviving row:* still bank it —
(M) is degree-generic and becomes the `d=5,6` screen for free.
**Stop condition.** Stop if the quota column leaves every banked row
alive at three consecutive conductors; that means `#Fix` is not
discriminating and the instrument is a consistency check, not a screen.
**Expected information gain.** High and cheap. Best case: a class of
surviving colourable rows dies for a reason the ladder structurally
cannot supply (the ladder tests *existence* of a colouring; (M) tests an
*equality* on all of them). Worst case: an independent, citation-light
re-derivation of the `N-1` budget and of a promoted theorem, which
discharges the flagged Orevkov custody risk (F2) on its own.

### Card 2 — `CANON-SIEVE/Y`: the canonical class of the intermediate surface

**Statement to bank.** `Cl(Y) =~ Z^{m_Y}` free on the components of
`B_Y`; `pi_1(Y)=1`; `kappa-bar(Y) = -infty`; and
`K_Y ~ sum_j (e_j-1)[B_{Y,j}] != 0`. Corollary: `Y` is never a smooth
hypersurface or complete intersection in affine space.
**Dependencies.** ZMT + miracle flatness (Step 0); the units sequence
(`C[Y]^* = C^*` because `C[Y] ⊂ C[x,y]`); Iitaka monotonicity of
`kappa-bar` on opens; tame Riemann–Hurwitz. Independent of `m=1`.
**Cheapest discriminator.** Hand-check `Y_1 = {xz = y^2-1}`: verify
(i) `Y_1 \ {x=0,y=1} =~ A^2` via the trivial `A^1`-bundle argument, and
(ii) `K_{Y_1} ~ 0` by adjunction, hence no admissible `q`. Both are
five-line computations.
**Outcomes.** *(i) and (ii) both confirm:* the sieve is real and the
whole `{x^n z = P(y)}` family is excluded; proceed to Gizatullin-type
surfaces with non-trivial `K`. *(i) fails* (the complement is not `A^2`):
my structural picture is wrong somewhere and Card 2 should be dropped
before Card 1 is affected — they share only Step 0. *(ii) fails:*
recheck whether `q` can be everywhere étale, which would force `d=1`.
**Stop condition.** Stop if the surviving `Y`-candidates after the sieve
form an unbounded family with no further invariant — i.e. if the
classification is not effectively finite, this becomes another
"always a next pair" and should not be farmed.
**Expected information gain.** Medium-high, and uniquely *two-sided*:
it is simultaneously the first structured counterexample search the
campaign has had and a potential exclusion mechanism. It also gives the
disproof side something to build rather than only something to certify.

### Card 3 — `THETA-CHEAP`: parity and puncture count before the SNC model

**Statement to test.** `Theta_h` is even and `>= 0`; and hyperbolicity
plus promoted connectedness force `2*gamma_h + n >= 3`.
**Dependencies.** Promoted: `gamma_h=(d_h-r_h-2)/2` clause;
coordinate-fibre connectedness; the locally-finite/LND/hyperbolic-fibre
theorem on `R = C[A,U,Z]/(U^2-A-A^2Z)`; boundary structure
`(1.12)`–`(1.14)` and flow-divisor formulas `(2.1)/(2.4)`, all promoted
at local scope.
**Cheapest discriminator.** The puncture count `n` of the general
coordinate fibre from the promoted boundary data. If `n <= 2` then
`gamma_h >= 1` and `Theta_h >= 2`.
**Outcomes.** *`n` computable and `<= 2`:* partition row pinned or
narrowed without the SNC model. *`n >= 3`:* `gamma_h` may be `0`; the
SNC model is then genuinely required, and this card has cost one
afternoon. *`Theta_h` odd on the local data:* the configuration is dead
by the mandatory consistency clause — the cheapest possible kill.
**Stop condition.** Stop after step 2 if two or more partition rows
survive with the same parity and puncture count; build the SNC model.
**Expected information gain.** Moderate; its value is schedule, not
depth — it can retire the most expensive scheduled item in the one-cusp
lane, and it cannot mislead, since every input is already promoted.

## 9. Lane dispositions

| Lane (packet state summary) | Verdict | One-line basis |
|---|---|---|
| Rank-four irreducible one-place frontier (colouring ladder) | **redesign** | Saturation says the ladder cannot close another genus; keep the banked rows and re-point the lane at the §5 quota filter, which reuses the same enumerations and tests an equality rather than existence. |
| Reducible rank four (rows, trees, splices, `n22`) | **stop** | Closed by theorem today; already stopped in the overlay. Retain as regression fixtures only; I propose no work here. |
| All-degree layer (nontrivial-`pi_1` branch component; one-node meridional obstruction) | **continue, with a redesigned successor** | The theorem stands and is promoted; but (M) reproves the one-node case at every `d >= 2` without the transposition or one-place hypotheses, so the *successor* should skip the genus-two graph-knot classification and go straight to the unibranch/tangential quota of §5. |
| One-cusp quartic horn (`Theta_h`) | **continue** | Scheduled and cheap; reorder per Card 3 so the SNC model is built only if parity and puncture count leave it necessary. |
| Primitive / no-proper-block branch (implicit; see F1) | **continue — and reprioritise up** | Now the only branch at degree four with no live mechanism; §3 is block-free and reaches it, so it is newly attackable rather than newly orphaned. |
| Disproof: K00 formal-germ algebraization | **continue** | Untouched today, orthogonal, and its bottleneck (algebraization) is unchanged. |
| Disproof: fixed-support AS/Witt lifting | **redesign** | Connection B names the obstruction (the Swan conductor is what pays for the map). Re-scope the lane to ask directly whether a char-0 limit can survive Swan annihilation, rather than to search for another finite-level lift. |
| Disproof: sparse searches above classical firewalls | **continue (low priority)** | Unchanged, but note Card 2 offers a *structured* alternative target (surfaces, not coefficient tuples) that this lane could adopt. |
| Review pairing (different-model gate + producer-side pre-review) | **continue** | Two data points, both informative, pointing opposite ways; the experiment is not finished and the promotion rule should not move on it. |

**Sources named in this report** (all citations by name for the
coordinator to pin; I fetched no PDFs and ran no CAS): Jelonek,
*The set of points at which a polynomial map is not proper*, Ann. Polon.
Math. 58 (1993); Grothendieck–Ogg–Shafarevich Euler–Poincaré formula
(for Connection B); Miyanishi–Sugie and Fujita on `kappa-bar = -infty`
and `A^1`-fibrations (Miyanishi, *Open Algebraic Surfaces*, CRM 12);
Zariski's Main Theorem and miracle flatness (standard); Abhyankar–Moh,
*Embeddings of the line in the plane*, J. reine angew. Math. 276 (1975);
Danielewski surfaces `{x^n z = P(y)}` (standard). Campaign-internal
facts are cited by the hashes in the frozen inputs.

<!-- BODY-END -->
