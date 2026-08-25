# Hostile review (claude2): erratum for the selected-Q8 good-reduction no-merger lemma

Date: 2026-08-25
Reviewer: independent hostile pass (Claude wrapper, second model), documentary
and hand-algebraic only.

Files read in full:

- `xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-lemma-20260825.md`
  (original producer lemma, expressly superseded)
- `xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-erratum-20260825.md`
  (object under review)
- `xmodel/max12-912-order3-nu-q8-generic-length-degree-one-lemma-20260825.md`
  (companion conditional certificate source)

Execution context disclosure: this review session is read-only with no shell,
no computer algebra, and no network, matching the prompt's own constraints.
Every verification below is hand algebra on the displayed rings and standard
commutative-algebra citations. The erratum is reviewed exactly as it asks to
be: a conditional abstract theorem plus discharge checklist, with none of its
Q8 computational hypotheses assumed complete.

## 1. The counterexample to the original wording is valid

Take `R = k[[pi]]`, `k` algebraically closed, and
`X = Spec R[x,y,z]/(x z, y z, pi x y)`.

**Special fibre.** Mod `pi` the ideal is `(xz, yz)`. Since `(x,y)` is prime
and `z` is not in it, `z f` lies in `(x,y)` iff `f` does; hence
`(xz, yz) = (z) ∩ (x,y)`, an intersection of two primes, so `X_k` is reduced
everywhere. Its components are the plane `D = V(z)` (dimension 2) and the
line `C = V(x,y)` (dimension 1). At the origin `q` both pass through, and `C`
is the unique **one-dimensional** local component — so the original
hypothesis 3 is satisfied as literally worded, while `D` sits through `q`
unnoticed.

**Flatness and reducedness at `eta_C`.** The prime of `eta_C` is
`(x, y, pi)`. Localizing, `z` is a unit, so `xz = yz = 0` forces `x = y = 0`,
and `A = O_(X,eta_C) = R[z]_(pi)`-localized: a DVR with uniformizer `pi` and
residue field `k(z)`. Hence `pi` is a nonzerodivisor (hypothesis 1) and
`A/pi A` is a field (hypothesis 2). Both hold exactly as the erratum claims.

**Generic fibre and closures.** With `pi` invertible the ideal becomes
`(xy, xz, yz)`, the three coordinate axes — three distinct geometrically
irreducible curve components. The containment
`(xz, yz, pi x y) ⊆ (y, z)` shows the scheme-theoretic closure of the generic
`x`-axis is `Spec R[x]`, integral, `R`-flat, containing `q`; symmetrically
for the `y`-axis. So original hypothesis 4 holds for two distinct geometric
components at the same marked point, and the original conclusion fails.

**Failure locus.** The special-fibre germ of `Spec R[x]` at `q` is the
`x`-axis, which lies inside `D`, not on `C`. The original proof's step "by
assumption 3 that germ lies on `C`" is a non sequitur: uniqueness among
one-dimensional components does not prevent a one-dimensional germ from
sitting inside a higher-dimensional component. The erratum's diagnosis is
exactly right. Two remarks confirming minimality and legitimacy:

- The generator `pi x y` is what splits the plane generically while leaving
  it whole in the special fibre. `X` is not `R`-flat at the generic point of
  `D` (there `xy` is `pi`-torsion), but the original lemma assumed flatness
  only at `eta_C`, so the counterexample fairly satisfies every stated
  hypothesis.
- In two ambient variables one cannot have both a one-dimensional special
  component `C` and a strictly higher-dimensional vertical component through
  the marked point, so three variables is essentially minimal.

Point 1 of the audit: **refutation of the original wording confirmed**.

## 2. The corrected hypothesis and the regular/`k[[w]]` replacement

Corrected hypothesis 3 — `C` is the unique irreducible component of `X_k`
through each `q_i` **in every dimension** — fails in the counterexample
(`D` passes through `q`), so the counterexample is blocked. In the corrected
proof this hypothesis is used exactly once: a component `W` of `(Z_i)_k`
through `q_i` is contained in some component of `X_k` through `q_i`, which
hypothesis 3 forces to be `C`; then `dim W = 1 = dim C` with `W` closed
irreducible inside irreducible `C` forces `W = C`. Sound. (A 0-dimensional
component `{q_i}` can never occur: it would be non-maximal inside `C`.)

**Stronger replacement.** If `O_(X_k, q_i)` is regular local of dimension
one, it is a domain, hence has a unique minimal prime, hence there is a
unique irreducible component of `X_k` through `q_i`; since `q_i ∈ C` and `C`
is a component, that unique component is `C`, and its dimension at the
closed point `q_i` is 1. So the replacement implies hypothesis 3 and is
strictly stronger (hypothesis 3 tolerates `C` singular at `q_i`, e.g. nodal).
The trailing clause "and `C` is its unique local branch" is redundant —
regularity already forces a single branch and the component through `q_i`
must be `C` — but harmless.

**Completed form.** `Ohat_(X_k, q_i) ≅ k[[w]]` suffices: the completion map
is faithfully flat local with `dim O = dim Ohat`, and regularity descends
along faithfully flat local homomorphisms (Matsumura 23.7). So the
degree-one lemma's certificate (4) is a sufficient discharge of hypothesis 3,
with two guard rails the erratum itself states and which I verify are
load-bearing:

1. The completed ring must be that of the **special fibre** (the full
   char-127 source quotient over `kbar`) at `q_i`, not of a plane
   projection — `H_v != 0` supplies projection smoothness only (erratum
   item 4 correctly demotes it).
2. Deriving `k[[w]]` from a rank-eight internal Jacobian by the formal
   implicit-function theorem is valid only when the local presentation is
   exactly those rows in those ambient variables. With extra rows present,
   an eight-row minor certifies smoothness only of the scheme cut by the
   eight pivot rows; every extra row must additionally be shown to lie in
   their local ideal. Erratum item 5 states this rider explicitly.

Point 2 of the audit: **corrected hypothesis and both replacement forms
confirmed sufficient**.

## 3. The domain claim at `eta_C`

`A = O_(X,eta_C)` is Noetherian local (`X` finite type over Noetherian `R`).

- Flatness at `eta_C` over a DVR is torsion-freeness, so `pi` is a
  nonzerodivisor. Correct.
- `A/pi A = O_(X_k, eta_C)`; since `eta_C` is a generic point of `X_k`, this
  is a zero-dimensional Noetherian local ring, reduced by hypothesis 2, hence
  a field. Correct.
- Krull intersection: `pi A` is a proper ideal (its quotient is a nonzero
  field), so `pi ∈ m_A` and `∩_n pi^n A = 0` by Krull's intersection theorem
  in a Noetherian local ring. Correct.
- Order removal: writing `a = pi^n a'`, `b = pi^m b'` with `a', b'` not in
  `pi A` (possible by separatedness), `ab = 0` gives `pi^(n+m) a' b' = 0`,
  cancel the nonzerodivisor to get `a' b' = 0`, contradicting domainhood of
  `A/pi A` since both factors are nonzero mod `pi`. Correct — and in fact
  `m_A = pi A` with these properties makes `A` a DVR, which is the cleanest
  reading of the endgame.
- Dimension claim: any nonzero prime of `A` contains some `pi^n·unit`, hence
  `pi`, hence equals `m_A`; so `A` is a one-dimensional local domain whose
  only prime avoiding `pi` is `(0)`. Correct.

**Excellence.** The proof body never uses it. Krull intersection,
cancellation, the Hauptidealsatz, and the dimension formula need only
Noetherianity plus universal catenarity, and *every* DVR is regular, hence
Cohen–Macaulay, hence universally catenary. Excellence quietly earns its
keep in one place only: it makes the integral closure of `R` in a finite
extension `K'` module-finite, so "common finite DVR extension" is literally a
localization of a finite normalization. Without excellence, Krull–Akizuki
still yields a suitable DVR `R'` with fraction field `K'`. Verdict on this
attack: the hypothesis is dispensable and should be labeled convenience, but
an extra hypothesis cannot falsify the lemma. No defect.

**After a common finite DVR extension `R → R'`.** Because `k` is
algebraically closed and residue extensions of finite valued-field
extensions are finite (fundamental inequality `e·f ≤ [K':K]`), the residue
field does not move: `k' = k`. Hence
`X'_(k') = X ×_R R' ×_(R') k' = X_k` — the special fibre, its components,
`C`, the `q_i`, and hypothesis 3 are literally unchanged; flatness at
`eta_C` is stable under base change; and `A'/pi'A' = O_(X_k, eta_C)` is the
same field, so `A'` is again a DVR. The erratum's instruction to "recheck
hypotheses 1–3" is therefore automatically satisfied — conservative wording,
not a gap. One application-side wording flag (not an abstract-lemma defect):
starting from `Z_(127)` the residue field `F_127` is **not** algebraically
closed; reaching `k = kbar` requires the standard *infinite* unramified base
change (a `W(Fbar_127)`-type DVR) before any finite step. Checklist item 1's
"a DVR above 127 … after residue extension" gestures at this and should say
it outright. The transfer is safe because `F_127` is perfect: regularity and
reducedness of fibre local rings ascend along the extension, and item 3's
smooth-rational-point argument is precisely what makes integrality of `H`
geometric.

Point 3 of the audit: **domain proof confirmed at every step; excellence
non-load-bearing; extension behavior sound**.

## 4. The closures `Z_i`: dominance, flatness, purity, and the endgame

- **Integrality.** The scheme-theoretic closure of the reduced irreducible
  `Y_i` is integral, and its generic fibre is the closure of `Y_i` in
  `X'_(K')`, which is `Y_i` itself (a component with its reduced structure
  is closed): a curve. Correct.
- **Dominance/flatness.** The generic point of `Z_i` lies in the generic
  fibre, so `Z_i` dominates `Spec R'`; its coordinate rings embed in a
  field extension of `K'`, hence are torsion-free, hence flat — over a DVR
  torsion-free implies flat with no finiteness needed. Correct.
- **Purity of the special fibre (the wrapper's focus).** `(Z_i)_k =
  V(pi')` with `pi'` a nonzero element of a domain: every irreducible
  component `W` has codimension exactly 1 in `Z_i` (Hauptidalsatz gives
  `≤ 1`; irreducibility of `Z_i` and `pi' ≠ 0` give `≥ 1`). The dimension
  formula for integral finite-type schemes over a universally catenary base
  (Stacks 02JX / EGA IV 5.6.5; packaged for flat families over a DVR as
  EGA IV 14.3.10) then gives
  `trdeg_k κ(eta_W) = dim O_(R',s) + trdeg_(K') R(Z_i) − codim(W, Z_i)
  = 1 + 1 − 1 = 1`, so `dim W = 1`. The special fibre of each closure is
  pure one-dimensional: no isolated points, no excess components. This is
  precisely the step the original lemma fumbled; here it feeds hypothesis 3,
  which now bites in every dimension.
- **Hidden-assumption sweep.** *Properness*: never used; nonemptiness of
  `(Z_i)_k` is hypothesized (`q_i ∈ Z_i`), not derived — without properness
  a characteristic-zero component may have empty special-fibre closure,
  which is exactly why checklist item 6 is a separate obligation. Correctly
  separated. *Catenarity*: needed for the dimension formula, automatic for
  every DVR; a citation would harden the text but there is no gap.
  *Equidimensionality*: a conclusion (purity), not an assumption.
  *Normalization*: expressly eliminated; replacing "integral closure inside
  `X`" by scheme-theoretic closure is correct and necessary, since the
  normalization is in general not a closed subscheme of `X`.
- **Endgame.** `W = C` gives `eta_C ∈ Z_i`, so `eta_(Z_i)` is a point of
  `Spec A` whose prime avoids `pi` (it lies in the generic fibre). `A` is a
  one-dimensional local domain, so that prime is `(0)` — the same point of
  `X'` for every `i`. Hence the `Z_i` coincide as integral closed
  subschemes and the `Y_i` are one component; after the splitting extension,
  same `K'`-component means same geometric component. Complete.

Point 4 of the audit: **closure audit passes; no hidden properness,
catenarity, equidimensionality, or normalization assumptions beyond what
every DVR supplies automatically**.

## 5. Checklist separation

Mapping items to the corrected lemma's needs:

| Checklist item | Supplies |
|---|---|
| 1 common integral source scheme | the `R`-model itself; `q_i` integral and pairwise distinct (squarefree `Q8bar` mod 127); finite-type hypotheses |
| 2 actual component, not projection | existence of `C` as a genuine one-dimensional component and hypotheses 1–2 at `eta_C` (generic multiplicity one = `A/pi A` a field) |
| 3 standalone `H` | arithmetic then geometric integrality of the plane image; explicitly quarantined until item 2 passes |
| 4 all eight full contacts | the full-coordinate `q_i` lie on the closure of the graph, with exact corrected values; `H_v != 0` correctly demoted to projection-only |
| 5 unique special-fibre component in every dimension | hypothesis 3 at each `q_i`, in the strong regular-dimension-one form; expressly the counterexample-killer |
| 6 integral specialization | hypothesis 4: `closure(Y_i) ∋ q_i` via an integral formal section (algebraizes over a complete `R'`; scheme-theoretic closure commutes with the flat base change) or any direct proof; a projected root correctly ruled insufficient |
| 7 scheme identity | transfer of the conclusion: the lemma identifies components **of this** `X_K` only, so identity with the primitive-grouping/infinity components is a genuine separate obligation |

This matches the prompt's required five-way separation, with generic
multiplicity housed in item 2 and local uniqueness in item 5. No item
silently assumes another beyond item 6's stated reference to item 4's
points. Two hardening flags, neither a correctness defect:

- **Extra rows.** Items 2 and 5 rest on Jacobian units "in the full source
  presentation." That qualifier is load-bearing: a unit 8×8 minor among
  eight selected rows, evaluated mod 127, certifies `R`-level étaleness over
  the `w`-line only for the scheme cut by exactly those rows. An extra row
  that vanishes mod 127 but equals `pi·(unit)` on the horizontal germ would
  destroy flatness at `eta_C` while every mod-127 check passes. Item 5
  carries the rider ("ambient variables, selected original rows, extra rows,
  and localizer all checked"); item 2 should carry it verbatim as well.
- **Residue field.** Item 1 should require the DVR to be taken with
  algebraically closed residue field (after the standard unramified base
  change), per §3 above.

Point 5 of the audit: **separation confirmed correct**, with the two wording
hardenings recorded.

## 6. Scope enforcement

The erratum's §5 states that current exact evidence supplies the standalone
plane integrality (item 3) and the `(w,v)` boundary factorization only, and
that items 2, 4, 5, 6 are not supplied. Under the controlling "only"
sentence, items 1 and 7 are *also* not supplied — item 1's unit-denominator
and integrality audit has no frozen certificate beyond the squarefree
specializations, and nothing certifies item 7 at all. The enumeration should
name 1 and 7 as open to prevent misreading; because the "only" sentence
governs, this is a wording hazard, not an overclaim. The companion
degree-one lemma is itself conditional on its pending length-190 endpoint
(its §5 lists six unresolved races), so nothing may be borrowed from it
unconditionally today.

Even with all seven items certified, the lemma yields exactly one step —
all eight characteristic-zero selected contact branches lie on one geometric
component — feeding the separately confirmed primitive grouping and infinity
exclusion. It proves no component lift by itself, no selected-trajectory
exclusion, no landing, no maximum-twelve theorem, and no JC2. The erratum
says the same. Firewall intact.

## Findings

1. **No mathematical error found.** Counterexample valid; corrected lemma
   true with the proof given; checklist sufficient and correctly separated;
   scope honest.
2. *Advisory*: excellence is never used in the proof body; keep it as
   convenience (finite normalization) or drop via Krull–Akizuki, but mark it
   non-load-bearing.
3. *Advisory*: cite the dimension formula (universal catenarity — automatic
   for every DVR) at the purity step.
4. *Advisory*: checklist item 1 should demand an algebraically closed
   residue field explicitly; erratum §5 should list items 1 and 7 as open.
5. *Advisory*: extend item 5's extra-rows rider verbatim into item 2.
6. *Advisory*: the "unique local branch" clause in the stronger form of
   hypothesis 3 is redundant given regularity; harmless.

## Verdict

The erratum refutes the original lemma exactly as claimed, its corrected
conditional lemma is true as stated with a correct proof, its discharge
checklist correctly separates the obligations, and its scope claims are
honest. The advisory items are wording hardenings only; none affects the
truth of any stated claim.

CONFIRMED
