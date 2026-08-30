# Hostile review — intermediate block descent via codimension-one image (Opus crosspoll §5.3)

```text
reviewer   : Fable 5 (different-model hostile reviewer)
round      : 20260829T2254Z inputs, review dated 20260830
basis      : 0f7ee003be45ee40d51d4048897cdacf63821172  (git rev-parse HEAD, verified)
target     : xmodel/ideation-20260829T2254Z-crosspoll-opus5.md §5.3 (lines 615–667)
             plus the §5.4 L4 reading (lines 669–684)
context    : xmodel/ideation-20260829T2254Z-sol56-alt.md Card 2 (MIN-TD-BLOCK-SURFACE/v1)
             xmodel/sol-lateral3.md §4 (primitive monodromy as a td bound)
             xmodel/ideation-20260829T2254Z-crosspoll-fable5.md §5.3
overall    : CONFIRM_WITH_CORRECTIONS — every §5.3 step is individually sound or
             one-line-repairable, but the codim-1 image hypothesis is not an open
             hypothesis to attack: it is REFUTABLE, and the Y ≅ A² recognition
             target is IMPOSSIBLE, for every nontrivial block of every Keller
             counterexample.  The surviving content is stronger than what §5.3
             claims and is promoted below as Theorem BD.
scope      : desk commutative algebra only.  No CAS, no web, no AWS, no edits to
             canonical files, no contact with jc2-lean.  Scratch: /tmp/bd-review-scratch/.
```

## 0. Custody and receipts

Verified on the frozen basis (all SHA-256, computed this session):

```text
git HEAD  0f7ee003be45ee40d51d4048897cdacf63821172                          MATCH
72aa958a…dd297  ideation-20260829T2254Z-sol56-alt.md        (28534 B)       MATCH
  body: head -c 28201 → 0477ab88…83fd5                                      MATCH
6e48015c…bab296 ideation-20260829T2254Z-crosspoll-opus5.md  (53567 B)       MATCH
  body: head -c 53234 → 647bca66…0346b                                      MATCH
e1ce0169…83a5971 ideation-20260829T2254Z-crosspoll-fable5.md (42429 B)      MATCH
  body: head -c 42096 → 0c2adb5a…2da599                                     MATCH
a6cc7385…293ca  sol-lateral3.md                             (28005 B)       MATCH
```

Execution disclosure.  Shell was used only for hashing and file reads.  Every
load-bearing step below is proved in place; the four external citations that
are consumed rather than reproved (Zariski–Nagata purity, Riemann existence,
Jelonek's structure of `A(F)`, quasi-finite ⇒ finite-after-completion) are
desk-recall with no web check, are individually flagged where used, and three
of the four are additionally bypassed by self-contained arguments.  Notation:
`F=(f,g): A² → A²` Keller (`Jac F = c ∈ C^*`), hypothetically not invertible;
`d = [C(x,y):C(f,g)]` its topological degree; `K` a proper intermediate field
(`C(f,g) ⊊ K ⊊ C(x,y)`), `d2 = [K:C(f,g)] ≥ 2`, `d1 = [C(x,y):K] ≥ 2`,
`d = d1·d2`; `B_K`, `Y = Spec B_K`, `F = g2∘g1` as in the mandate.  `R ⊆ Y`
denotes the non-étale locus of `g2` and `A(·)` the Jelonek nonproperness set.
Standing recall: `F` non-invertible Keller ⇒ `d ≥ 2` ⇒ `F` étale (char 0:
constant nonzero Jacobian kills `Ω`, quasi-finiteness follows from
unramifiedness, flatness by miracle flatness over the regular target), and `F`
is neither finite nor proper (a connected finite étale cover of `A²_C` is
trivial, §3.3, so finite ⇒ `d=1`).

---

## 1. Item 1 — the diagram: objects, and the exact status of `g1`

**VERDICT: CONFIRM** (all four §5.3 claims), with sharpenings that exceed the
card: `g1` is provably étale and open, and singular image points cannot occur.

**1.1 `B_K ⊆ C[x,y]`: CONFIRMED.**  An element `b ∈ B_K` is integral over
`C[f,g] ⊆ C[x,y]`, hence integral over `C[x,y]`, and lies in `K ⊆ C(x,y)`;
`C[x,y]` is integrally closed in `C(x,y)`, so `b ∈ C[x,y]`.  Opus's remark
that properness of `F` is not used is correct.  Precision kept: only
`B_K ⊆ K ∩ C[x,y]` is claimed or needed; equality would say every polynomial
in `K` is integral over `C[f,g]`, which nothing here provides.

**1.2 Module-finiteness over `C[f,g]`: CONFIRMED.**  `K/C(f,g)` is finite and
separable (char 0), so the trace form on `K` is nondegenerate; `B_K` embeds
into the trace-dual of a free `C[f,g]`-lattice spanned by a `C(f,g)`-basis of
`K` chosen inside `B_K` (clear denominators), and `C[f,g]` is noetherian, so
`B_K` is a finite `C[f,g]`-module (E. Noether).  Hence `B_K` is an affine
`C`-algebra, `Y` is an integral normal affine surface with `Frac(B_K) = K`
(every `α ∈ K` is `b/s` with `b ∈ B_K`, `s ∈ C[f,g]∖{0}`), and `g2` is finite.

**1.3 `g2` is moreover flat and surjective (sharpening).**  Surjective: finite
+ dominant (lying over for the integral extension `C[f,g] ⊆ B_K`).  Flat: `Y`
is a normal surface, hence Cohen–Macaulay (S2 and dim 2); the target is
regular; the fibers are finite; miracle flatness [Matsumura 23.1] applies.  So
`B_K` is locally free of rank `d2` over `C[f,g]`.  This is used in §3.2, §4.4.

**1.4 Status of `g1`: dominant and quasi-finite CONFIRMED; finite, proper, and
surjective all provably FAIL.**  Dominant: `B_K ⊆ C[x,y]` induces `K ⊆ C(x,y)`
on fraction fields.  Quasi-finite: any positive-dimensional `g1`-fiber sits
inside a fiber of `F = g2∘g1`, and `F` is quasi-finite (étale); so `g1` has
finite fibers.  Not finite: `g1` finite would make `F` a composite of finite
maps, hence finite, contradicting §0.  Not proper: proper + quasi-finite +
separated ⇒ finite [EGA III 4.4.2].  Not surjective: §4.2 below (it misses the
entire nonempty branch locus `R`).  So Opus's "`g1` finite: NOT AVAILABLE" is
correct and upgradeable: finiteness is not merely unavailable, it is refuted
for a counterexample; the honest-gap framing survives.

**1.5 Sharpening (new): `g1` is étale everywhere, its image is open and lies
in `Y_sm ∖ R`.**  This removes the mandate's warning case ("do not assume …
étale at singular image points") by proving singular image points do not
exist.  Everything rests on:

> **Lemma E (completion rigidity).**  Let `x ∈ A²` be a closed point,
> `y = g1(x)`, `z = g2(y) = F(x)` (closed, residue fields `C`).  Assume `F` is
> étale at `x`, `g1` is quasi-finite at `x`, and `O_{Y,y}` is normal (given:
> `Y` normal) with `dim O_{Y,y} = 2` (given: `y` closed on the surface `Y`).
> Then the induced maps `Ô_z → Ô_y → Ô_x` are both isomorphisms.  In
> particular `Y` is smooth at `y`, `g1` is étale at `x`, and `g2` is étale
> at `y`.  (No finiteness of `g2` is used.)

*Proof.*  (i) `F` étale at `x` with trivial residue extension gives
`m_z O_x = m_x` and flatness, hence `O_z/m_z^n → O_x/m_x^n` is an isomorphism
for every `n` (surjectivity by Nakayama from the trivial closed fiber,
injectivity by faithful flatness of the local base change), so `Ô_z → Ô_x` is
an isomorphism; both are `C[[s,t]]`.  (ii) `g1` quasi-finite at `x` means the
fiber germ is zero-dimensional, so `Ô_x/m_yÔ_x` is artinian, i.e.
`m_x^N ⊆ m_yÔ_x` for some `N`; lifting a `C`-basis of `Ô_x/m_yÔ_x` and using
completeness (topological Nakayama: the finite submodule generated by the
lifts is complete, hence closed, and dense) makes `Ô_x` a finite
`Ô_y`-module.  (iii) `B_K` is excellent (finite type over `C`), so `Ô_y` is a
normal local ring, hence a domain, of dimension 2, catenary and
equidimensional (complete local domain, finite over `C[[u,v]]` by Cohen).
(iv) The kernel `p` of `Ô_y → Ô_x` is prime (the target is a domain), and
`Ô_x` is finite over `Ô_y/p`, so `dim(Ô_y/p) = dim Ô_x = 2`, so `ht p = 0`,
so `p = 0`: injective.  (v) The composite `Ô_z → Ô_x` is surjective by (i),
so `Ô_y → Ô_x` is surjective, hence an isomorphism by (iv); then `Ô_z → Ô_y`
is an isomorphism too.  (vi) Descent to the uncompleted rings: `m_yO_x` and
`m_x` have the same extension to `Ô_x`, so they coincide (faithful flatness of
completion); `Tor_1^{O_y}(O_x, κ(y)) ⊗_{O_x} Ô_x = Tor_1^{O_y}(Ô_x, κ(y)) =
Tor_1^{O_y}(Ô_y, κ(y)) = 0` since `Ô_y` is `O_y`-flat, so `O_x` is `O_y`-flat
by the local criterion [Matsumura 22.3]; flat + unramified + finite type =
étale at `x`.  The same criterion applied to `Ô_z → Ô_y` gives `g2` étale at
`y`.  `Ô_y ≅ C[[s,t]]` gives regularity, hence smoothness (char 0).  ∎

Step (ii) is the standard "quasi-finite becomes finite after completion"
[EGA IV 18; the proof above is self-contained].  Consequences, since `F` is
étale at *every* point:

- **(E1)** `g1` is étale at every closed point, and the non-étale locus is
  closed with no closed points, hence empty (`A²` Jacobson): **`g1` is étale**,
  therefore flat and **open**; `g1(A²)` is open and dense.
- **(E2)** Every closed point of `g1(A²)` is a smooth point of `Y` at which
  `g2` is étale.  For an arbitrary point `y` of the open set `g1(A²)`: pick a
  closed point `y'` of `Y` in the (nonempty, open in `cl{y}`) set
  `cl{y} ∩ g1(A²)`; the étale locus of `g2` is open and contains `y'`, and an
  open set meeting `cl{y}` contains its generic point `y`.  Hence
  **`g1(A²) ∩ R = ∅` and `g1(A²) ∩ Sing(Y) = ∅`** at all points, of every
  codimension.
- **(E3)** `Sing(Y) ⊆ R` (étale over a regular scheme forces regularity), so
  the singular points of `Y`, if any, also lie outside the image and over the
  discriminant.

Correction recorded against the sibling report: crosspoll-fable5 §5.3
("`A² → Y_K` … not known étale — smoothness of `Y_K` is exactly what the
`A²`-recognition must supply, since `g∘f` étale plus `g` finite does not give
`f` étale at singular image points") is superseded.  The quoted abstract
caution is vacuous in this setting: with `Y` normal and `g1` quasi-finite,
singular image points cannot occur, and `g1` *is* étale.  No `A²`-recognition
input is involved.

---

## 2. Item 2 — does `dF` invertible force `g2` étale at smooth codim-1 image points?

**VERDICT: CONFIRM.**  Yes, and characteristic-free.  Two independent proofs;
Opus's own proof needs a one-line repair at non-closed points.

**2.1 Direct proof at the codim-1 point.**  Let `y ∈ Y` be a codimension-1
point in `g1(A²)`.  Any preimage `x` is codimension-1 (it is not generic —
`g1` is dominant so the generic point maps to the generic point — and not
closed, since closed points map to closed points among finite-type
`C`-schemes).  Set `z = g2(y)`, again codimension-1 (`g2` finite maps the
curve `cl{y}` onto a curve).  Then `O_{A²,z}`, `O_{Y,y}`, `O_{A²,x}` are DVRs
(the middle one because `Y` is normal: R1 — this is where "smooth codim-1
point of `Y`" is automatic, so the mandate's phrase carries no extra
hypothesis).  `F` étale at `x` gives `e(x/z) = 1` and `κ(x)/κ(z)` separable.
Valuation theory gives multiplicativity `e(x/z) = e(x/y)·e(y/z)` (the
restriction of `v_x` to `K` is a valuation dominating the maximal DVR
`O_{Y,y}`, hence equivalent to `v_y`), so `e(y/z) = 1`; and `κ(y)/κ(z)` is a
subextension of a separable extension, hence separable.  So `g2` is unramified
at `y`; it is flat at `y` (torsion-free, finitely generated over the DVR
`O_z`); so `g2` is étale at `y`.  ∎

**2.2 Opus's tangent-map proof, audited.**  "`d(g2)∘d(g1)` invertible ⇒ `dg1`
injective and `dg2` an isomorphism at every smooth point of `Y` in the image"
is correct at smooth *closed* points (2×2 matrices; Jacobian criterion between
smooth surfaces).  The §5.3 sentence "therefore `g2` is étale away from
`Sing(Y_K) ∪ (Y_K ∖ g1(A²))`" is a statement about all points, including the
codimension-1 ones that purity consumes, and the tangent-map argument does not
literally reach non-closed points.  Repair (one line, two options): (a) use
§2.1; or (b) if the codim-1 point `η` of a curve `E` lies in the image, the
image is constructible (Chevalley), so it contains a dense open of `E`, hence
all but finitely many closed points of `E`, all but finitely many of which are
smooth points of `Y` (`Sing(Y)` finite); `g2` is étale at those closed points,
and the étale locus is open, hence contains `η`.  With Lemma E the repair is
free (E2).  The claim itself: CONFIRMED.

**2.3 Characteristic and separability inventory (mandated).**  Item 2 is
characteristic-free once its actual input — `F` unramified (equivalently
étale) at the chosen preimage `x` — is granted:

- `dF` invertible everywhere ⇒ `Ω_{A²/A²} = coker(Jac^T) = 0` ⇒ `F` unramified
  ⇒ fibers discrete ⇒ quasi-finite ⇒ flat (miracle flatness, both planes
  regular) ⇒ étale.  Valid in every characteristic, including `p > 0`
  (Artin–Schreier maps like `x ↦ x − x^p` are honest examples).
- Ramification-index multiplicativity is valuation-theoretic, char-free.
- Residue separability at `y` is inherited from `κ(x)/κ(z)` separable, which
  unramifiedness of `F` supplies; over an algebraically closed (perfect) base,
  codim-1 residue fields are separably generated anyway.
- Where characteristic 0 *is* consumed in the surrounding argument: the
  triviality of `π₁^{ét}(A²)` (§3.3 — false in char p), Riemann existence,
  the Galois correspondence needing `C(x,y)/C(f,g)` separable (free here:
  `F` étale ⇒ separable in any characteristic), and the Jelonek theory used in
  §4 (developed over `C`).  Lemma E as proved uses residue field `C` at closed
  points and excellence; it is otherwise characteristic-free.

---

## 3. Item 3 — the purity step and the finite-étale endgame

**VERDICT: CONFIRM_WITH_CORRECTIONS.**  The boxed conditional of §5.3 is a
true theorem with correctly identified hypotheses; the correction is about its
*use*: the antecedent is not an open hypothesis, it provably never holds
(§4.2), so the box functions only as the engine of a contrapositive.

**3.1 The purity theorem, named, with hypotheses checked against `Sing(Y)`.**
Zariski–Nagata purity of the branch locus [SGA 1, Exp. X, Thm 3.1; SGA 2,
Exp. X, 3.4; Nagata 1959]: for a quasi-finite dominant morphism from a
*normal* noetherian scheme to a *regular* noetherian scheme, the ramification
locus is pure of codimension 1 (or empty).  Hypothesis check for `g2: Y → A²`:
target regular — yes, it is `A²`, and regularity is demanded of the *target*,
not of `Y`; source normal — yes, by construction `B_K` is integrally closed in
`K`; quasi-finite dominant — it is finite dominant (§1.2–1.3).  Possible
singularities of `Y` are exactly what the normality hypothesis tolerates; the
theorem applies with no smoothness repair.  Citation is desk-recall (no web);
the next paragraph removes any dependence on it.

**3.2 Elementary bypass, immune to the citation.**  `g2` is finite *flat*
(§1.3), `B_K` locally free of rank `d2`, and `K/C(f,g)` separable, so the
trace-form discriminant `disc ∈ C[u,v]` is nonzero and well-defined up to unit
squares; for a closed point `z`, the fiber algebra `B_K ⊗ κ(z)` is étale iff
`disc(z) ≠ 0` (discriminant commutes with base change of locally free
algebras).  Hence `g2(R) = V(disc)` set-theoretically: **empty or pure of
codimension 1** in the target, with `R = g2^{-1}(V(disc))`-supported and
mapping finite-surjectively onto it.  Everything §5.3 needs from purity
("branch locus is a divisor or empty") follows from this principal-ideal
statement; Zariski–Nagata is then only decoration (it adds purity of `R`
upstairs, which nothing below consumes).

**3.3 Connected finite étale over `A²_C` is an isomorphism: CONFIRMED.**
Riemann existence [SGA 1, Exp. XII] identifies finite étale covers of `A²_C`
with finite topological covers of `C²`, which is contractible; so
`π₁^{ét}(A²_C) = 1` and a *connected* finite étale cover has degree 1.  `Y` is
connected (integral, §1.2).  A degree-1 finite morphism onto a normal variety
that is birational is an isomorphism.  Characteristic 0 is essential
(Artin–Schreier covers kill this in char p); so is the target being `A²`
(control D, §5.4) and `g2` being finite rather than quasi-finite (control B).

**3.4 The boxed conditional, assembled: CONFIRMED as a theorem.**  If
`g1(A²)` contains every codimension-1 point of `Y`, then by item 2 `g2` is
étale at every codimension-1 point; by §3.1/§3.2 the branch locus, which would
otherwise contain a codimension-1 point, is empty; `g2` is finite étale; by
§3.3 it is an isomorphism; so `d2 = 1` and the block is trivial.  All
hypotheses discharged, including at singular points of `Y` (which, under the
antecedent, are forced not to exist — étale over regular).  Opus's two guards
(only normality of `Y` and regularity of `A²` used; invalid if "finite" is
substituted for "dominant" on `g1`) are both correct and are exactly the right
guards.

**3.5 CORRECTION (main finding of this review).**  §5.3 frames the antecedent
as "the single missing hypothesis … which should be attacked directly," and
§5.4 prices launch `L4` with "A `PASS` on `L4` would give primitivity of
minimal-`td` monodromy."  The direct attack terminates *negatively and
unconditionally*: by §4.1–§4.2 below, for every Keller counterexample and
every proper intermediate `K`, the branch locus `R` is a nonempty union of
curves entirely missed by `g1`.  The antecedent of the box is therefore
*refuted*, not open; `L4` has no reachable `PASS` branch; and no primitivity
statement is obtainable from this criterion (item 6).  What survives — and is
stronger than what was asked — is the contrapositive structure theorem.

---

## 4. Item 4 — the contrapositive: `g1` must miss a divisor, and where it goes

**VERDICT: CONFIRM (strengthened).**  "Must `g1` miss a divisor of `Y`?" —
yes, provably, and canonically: it misses *every point of the entire branch
locus*, which is a nonempty union of curves; and the finite image of every
missed divisor (branch or not) lies in the Jelonek set `A(F)`.  Proofs:

**4.1 `R ≠ ∅`, and it contains a divisor.**  If `R = ∅` then `g2` is finite
étale of degree `d2 ≥ 2` from a connected `Y`, contradicting §3.3.  So
`R ≠ ∅`; by §3.2 `V(disc) = g2(R)` is then a nonempty curve and `R` (mapping
finite-surjectively onto it) contains at least one irreducible curve; by §3.1
it is even pure of codimension 1.  Note this uses only `d2 ≥ 2`, not
minimality of `d` and not `d1 ≥ 2`.

**4.2 `g1` misses all of `R`.**  Lemma E consequence (E2): `g1(A²) ∩ R = ∅`.
In particular the generic point of every branch curve is outside `g1(A²)`:
the codim-1 image hypothesis of §3.4 fails for every nontrivial block.  Also
`Sing(Y) ⊆ R` (E3) is missed.  This answers item 4's first question in the
strongest form: the missed divisor is not merely existent but canonical, and
it is missed pointwise, not just generically.

**4.3 The composition identity and the `A(F)` localization.**  Recall
Jelonek's set for a map `h` of complex affine varieties: `w ∈ A(h)` iff there
is a sequence `x_k → ∞` (leaving every compact) with `h(x_k) → w`.

> **Identity.**  `A(F) = g2(A(g1))`.  *Proof.*  (⊆)  If `x_k → ∞` in `A²` and
> `F(x_k) → z`, then `y_k = g1(x_k)` is eventually contained in the compact
> `g2^{-1}(cl B(z))` (`g2` finite ⇒ proper in the Euclidean topology), so a
> subsequence converges to some `y*`; then `y* ∈ A(g1)` and `g2(y*) = z`.
> (⊇)  If `x_k → ∞` and `g1(x_k) → y*`, then `F(x_k) → g2(y*)` by continuity. ∎

> **Missed points escape.**  `Y ∖ g1(A²) ⊆ A(g1)`.  *Proof.*  `g1(A²)` is
> Zariski-dense and open (E1), hence Euclidean-dense in `Y(C)` (`Y`
> irreducible).  A missed point `y` is thus a Euclidean limit of `g1(x_k)`;
> if `(x_k)` had a bounded subsequence, its limit `x*` would give
> `g1(x*) = y ∈ g1(A²)`, contradiction; so `x_k → ∞` and `y ∈ A(g1)`. ∎

Combining with §4.1–4.2: **`g2(R) = V(disc) ⊆ g2(Y ∖ g1(A²)) ⊆ g2(A(g1)) =
A(F)`**, and the same holds for every missed divisor, branch or not.  Since
`V(disc)` is a nonempty pure-1-dimensional closed set inside the algebraic set
`A(F)` of dimension ≤ 1, every irreducible component of `V(disc)` *is* an
irreducible component of `A(F)`; by Jelonek's structure theorem
[Jelonek 1993, Ann. Polon. Math. 58; 1999, Math. Ann. — cited, desk-recall:
for dominant polynomial `C² → C²`, `A(F)` is a closed algebraic curve or
empty, every component a polynomial curve], each such component is a
polynomially parametrized curve.  This last cosmetic clause is the only place
the Jelonek citation is load-bearing; the inclusion itself is proved above.

**4.4 Quantitative secondary proof (independent of §4.3).**  For closed `z`:
`#g2^{-1}(z) ≤ d2` (rank-`d2` locally free fiber algebra), and
`#g1^{-1}(y) ≤ d1` (ZMT: `A²` embeds as an open of `Z = Spec` of the integral
closure of `B_K` in `C(x,y)` — birational quasi-finite into normal is an open
immersion — with `Z → Y` finite of degree `d1` onto the normal `Y`, whose
fibers have at most `d1` points; control C below shows normality is
load-bearing).  For `z ∈ V(disc)`, at least one fiber point lies in `R`,
contributes zero, and so `#F^{-1}(z) ≤ (d2−1)·d1 = d − d1 ≤ d − 2`.  For étale
`F`, `#F^{-1}(z) < d` forces `z ∈ A(F)`: otherwise `F` is proper over a
Euclidean neighborhood `U` of `z`, a proper étale local homeomorphism onto `U`
is a finite covering of constant degree, and `U` meets the Zariski-dense open
over which the degree is `d`.  This re-derives `V(disc) ⊆ A(F)` with the
bonus of a fiber deficit ≥ `d1` along the discriminant.  (Upper bounds only;
no attainment claim — the deficit does not decide whether points of `V(disc)`
are attained values.)

**4.5 The four notions, kept distinct (mandated).**

| notion | lives in | status here |
|---|---|---|
| missed divisor (curve component of `Y ∖ g1(A²)`) | `Y` | exists: every component of `R` is one (§4.1–4.2); whether *non-branch* missed divisors can occur: typed OPEN-1 |
| branch divisor (curve component of `R`) | `Y` | nonempty, pure codim 1; `⊆` missed set; converse OPEN-1 |
| nonproperness component (component of `A(F)`) | target `A²` | contains every component of `g2(missed divisor)`; components of `V(disc)` are components of `A(F)`; whether every `A(F)`-component arises this way for some/this `K`: typed OPEN-2 |
| missing value (`z ∉ F(A²)`) | target `A²` | `F(A²) ⊇ A² ∖ A(F)` (étale count, §4.4), so missing values form a closed subset of `A(F)` (`F` open); a point of `V(disc)` may still be attained — deficit `≤ d−d1` does not mean zero.  Distinct from all three above |

No identification among the four is made anywhere below; FALLACY-v2
flag/place-style conflations avoided by construction.

---

## 5. Item 5 — comparison, controls, and the cheapest next step

**VERDICT (assessment item): CONFIRM_WITH_CORRECTIONS** — the criterion is a
genuine bridge, not a tautology; but the comparison target itself
(`Y ≅ A²` recognition) is refuted as a live alternative.

**5.1 Against the older `Y ≅ A²` recognition target: that target is
impossible, unconditionally.**

> **Theorem (no `A²` model, no minimality).**  For *any* non-invertible
> Keller `F` and *any* nontrivial block field `K` (`d2 ≥ 2`), `Y ≇ A²` as an
> abstract variety.  *Proof.*  Suppose `φ: Y → A²` is an isomorphism; set
> `G1 = φ∘g1`, `G2 = g2∘φ^{-1}`, polynomial self-maps of `A²` with
> `F = G2∘G1`.  Chain rule: `(Jac G2 ∘ G1)·Jac G1 ≡ c ≠ 0`, so `Jac G1` is a
> zero-free polynomial, hence a nonzero constant (Nullstellensatz); then
> `Jac G2` is constant on the Zariski-dense set `G1(A²)`, hence constant
> nonzero everywhere; so `G2` is étale *and* finite of degree `d2 ≥ 2` over
> `A²` with connected source — contradicting `π₁^{ét}(A²_C) = 1` (§3.3). ∎

Consequences, each a correction to a sealed document:

- Sol-alt Card 2's "intermediate-`A²` theorem" (`every nontrivial block has
  B_K ≅ C[u,v]`) is unprovable except vacuously: proving it is *equivalent* to
  proving no nontrivial block exists (primitivity itself).  Its fallback
  dichotomy collapses to the second horn — the boundary/divisor object —
  which Theorem BD below makes precise.  Avenue 30's raise-rationale ("whose
  being `A²` has a lower-`td` consequence") should be re-typed: the correct
  object of study is the forced *non*-`A²` surface with its located branch
  divisor.
- Opus §5.3 last bullet ("The Jacobian factor argument if `Y_K ≅ A²`:
  CONFIRMED but now secondary … reaching `Y_K ≅ A²` is the hard part"): the
  displayed argument is CONFIRMED as algebra, but it is not a hard-to-reach
  descent — it is a two-line reductio showing the case never occurs.
  Minimality of `d`, which both Sol-alt and §5.3 invoke there, is not used by
  anything that survives.
- crosspoll-fable5 §5.3's minimality-based factor lemma (including the
  Ax–Białynicki-Birula endpoint) is correct but strictly subsumed: the
  contradiction is absolute, not merely against minimality.

**5.2 Against properness / JC2 / bare nonproperness.**  The criterion (in its
surviving contrapositive form, Theorem BD) is: strictly weaker than JC2 — it
is a structure theorem about hypothetical counterexamples, vacuous if JC2
holds, and refutes nothing by itself; *not* a tautological restatement of
nonproperness — nonproperness of `F` says `A(F) ≠ ∅` and is available for
every counterexample, whereas BD requires imprimitivity as input and returns
strictly more: a new normal surface `Y`, a finite flat degree-`d2` cover with
*nonempty* branch divisor forced into `A(F)`-components, an everywhere-étale
open `g1`, and `Sing(Y)` confined over the discriminant.  None of that is
recoverable from `A(F) ≠ ∅` alone.  It is also not implied by properness
statements in any nonvacuous way (properness of `F` is itself contradictory
for a counterexample, §0).

**5.3 Bridge value (Avenues 7/26/31).**  Avenue 7 (Jelonek `A(F)`): the
components of `A(F)` acquire a mandatory client — for every block field, the
discriminant curve of the block cover must occupy `A(F)`-components; and the
pushforward identity `A(F) = g2(A(g1))` is a reusable tool independent of
blocks.  Avenue 26 (primitive monodromy): "imprimitivity is potentially
fatal" is *withdrawn* — imprimitivity is not killed by descent (item 6); the
honest reformulation is: minimal-`td` primitivity ⇔ nonexistence of an étale
sandwich `A² →^{ét,d1} Y →^{fin flat,d2} A²` with the BD constraints.  Avenue
31 (integrality/ZMT/Rees): `Y` *is* the integral-closure object that avenue
kept requesting, now with a located divisor (`R`, `V(disc)`, conductor
support) mapping into `A(F)`.  So: a genuine bridge, with the caveat that it
constrains a hypothetical object and supplies no selector (the §5.4 preserved
gap stands).

**5.4 Controls (mandated: one finite non-Keller factorization, one
open-immersion/quasi-finite control; two more added).**

- **Control A (finite non-Keller): `F = (x², y²)`, `K = C(x², xy)`.**
  `B_K = C[x², xy, y²] = C[U,V][w]/(w² − UV)` — the quadric cone (invariant
  ring of `μ2`, normal, full closure since normal with fraction field `K`).
  `g1` is the quotient map: *surjective*, so the codim-1 image hypothesis
  holds; yet `g2` is branched: trace-form discriminant over the basis `{1,w}`
  is `det diag(2, 2UV) = 4UV`, so `V(disc) = {UV = 0}` and `R ≠ ∅` meets the
  image.  No contradiction with items 2–4: `dF` is invertible nowhere on
  `{xy = 0}`, which is exactly the `g1`-preimage of `R`.  Also `A(F) = ∅`
  (`F` finite), so `V(disc) ⊄ A(F)`.  Verdict: every Keller input in items
  2, 4 is load-bearing; the boxed conditional of §3.4 is false without it.
  This is Opus's own cone control, confirmed and sharpened (Opus used it only
  against `A²`-recognition; it also calibrates items 2 and 4).
- **Control A′ (same `F`, `K = C(x², y)`):** `B_K = C[x², y] ≅ C[u,v]`, so
  `Y ≅ A²` with `g2 = (u,v) ↦ (u, v²)` finite and branched.  A non-Keller
  factorization *can* have an `A²` block surface: in §5.1's proof the chain
  breaks precisely at "`Jac G1` zero-free" (`Jac G1 = 2x`).  So the
  no-`A²`-model theorem consumes Keller essentially.
- **Control B (open-immersion/quasi-finite): `A² ∖ {0} ↪ A²`.**  Étale,
  quasi-finite, connected, image contains every codimension-1 point, yet not
  an isomorphism and not finite.  If §3.4 were stated with `g2` merely
  quasi-finite, it would be false; the module-finiteness of `B_K` (§1.2) is
  load-bearing, and no analogous triviality can be run on `g1` (étale but
  non-proper) — which is why the sandwich does not instantly self-destruct.
- **Control C (normality in the fiber bound): normalization of a nodal
  curve.**  Degree 1, two points over the node: the `#fiber ≤ deg` lemma of
  §4.4 genuinely needs the *normal* target, which `Y` supplies by
  construction.
- **Control D (target `π₁`): `(s,t) ↦ (s², t)` on `(C^*)²`.**  Finite étale
  degree 2, Jacobian a unit, yet not injective: §3.3 is a theorem about `A²`,
  not about étale maps in general; the simply-connected target is
  load-bearing.

**5.5 Cheapest next theorem / countermodel.**  The cheapest next theorem is
Theorem BD itself (§7): it is fully desk-proved in this review and promotable
as stated.  A countermodel to the *package* is impossible without exhibiting a
Keller counterexample (everything is conditional on one), so falsification
effort should aim at the lemma level — the controls above already probe every
hypothesis — or at the sandwich-existence question, which is the launch (§8).

---

## 6. Item 6 — the minimal-topological-degree factor argument

**VERDICT: REFUTE** (as a route to primitivity of minimal counterexamples);
the residual structure is confirmed and typed.

**6.1 Both known bridges from "nontrivial block" to "smaller Keller
counterexample" are closed.**  (a) The codim-1-image bridge (§3.4 + §5.4-L4):
its hypothesis is refuted unconditionally (§4.2) — there is no reachable
`PASS`.  (b) The `Y ≅ A²` bridge (Sol-alt Card 2, sol-lateral3 §4 step 4,
Opus §5.3 final bullet): the hypothesis is impossible (§5.1).  Since both
bridges fail by theorem rather than by lack of proof, the inference "minimal
`td` ⇒ primitive monodromy" is not merely unproved — *this* route to it is
permanently closed.  Sol-lateral3 §4's kill criterion ("one exact example
where the intermediate normalization has no `A²` model … kills the minimality
bridge as stated") is satisfied wholesale: *every* intermediate normalization
of *every* nontrivial block has no `A²` model, by theorem; no example was
needed, and none could have been exhibited anyway (no counterexample is
available to instantiate one).

**6.2 What minimality still buys here: nothing.**  Every surviving statement
(Theorem BD, §7) holds for an arbitrary non-invertible Keller `F`; the
minimal-`td` selection contributes no additional constraint through this
mechanism.  Minimal-degree reasoning retains force only against genuine
`A² → A² → A²` polynomial factorizations with both factors Keller — which BD
shows never arise from blocks (`g2` is necessarily branched; `g1`'s target is
necessarily not `A²`).

**6.3 Primitivity, correctly typed.**  Primitivity of minimal-counterexample
monodromy is **OPEN-3**, and BD converts it into an exact geometric
equivalence: a nontrivial block of a Keller counterexample exists iff there
exists an "étale sandwich" — a normal affine surface `Y ≇ A²` with a finite
flat `g2: Y → A²` of degree ≥ 2 branched over a nonempty union of
`A(F)`-components, and an everywhere-étale, quasi-finite, non-proper
`g1: A² → Y` of degree ≥ 2 with open image `⊆ Y_sm ∖ R` missing all of `R`.
Ruling such sandwiches out (per block-degree, or wholesale) is the honest
successor problem; asserting primitivity before that is done would violate
the mandate's own warning, and after §4.2 the warning has teeth: the codim-1
hypothesis is not "not yet proved," it is false.

---

## 7. Item-by-item verdicts, and the maximum exact theorem safe for promotion

| item | claim under attack | verdict |
|---|---|---|
| 1 | `B_K ⊆ C[x,y]`; finiteness; normal `Y`; status of `g1` | **CONFIRM** (+ sharpening: `g1` étale, open; finite/proper/surjective all refuted; no singular image points) |
| 2 | `dF` invertible ⇒ `g2` étale at smooth codim-1 image points | **CONFIRM** (char-free; Opus's set-level phrasing repaired at non-closed points) |
| 3 | purity + `π₁` endgame under the codim-1 image hypothesis | **CONFIRM_WITH_CORRECTIONS** (conditional true — Zariski–Nagata hypotheses verified, `Y`-singularities tolerated, flat-discriminant bypass supplied; correction: antecedent unsatisfiable, `L4` has no `PASS` branch) |
| 4 | must `g1` miss a divisor; does its `g2`-image lie in `A(F)` | **CONFIRM** (strengthened: all of `R ≠ ∅` missed pointwise; `g2(R) = V(disc) ⊆ A(F) = g2(A(g1))`; components of `V(disc)` are `A(F)`-components; four notions kept distinct; OPEN-1/OPEN-2 typed) |
| 5 | weaker than JC2 / tautology / bridge; controls | **CONFIRM_WITH_CORRECTIONS** (genuine bridge; not a tautology; the rival `Y ≅ A²` target refuted outright; controls A, A′, B, C, D run) |
| 6 | minimal-degree factor argument ⇒ primitive monodromy | **REFUTE** as a route (both bridges closed by theorem); primitivity itself OPEN-3, re-expressed as sandwich nonexistence |

**Maximum exact theorem safe for promotion.**

> **Theorem BD (block-descent structure; char 0; unconditional in `K`,
> no minimality).**  Let `F = (f,g): A²_C → A²_C` be a Keller map that is not
> invertible, `d = d1·d2` as in §0, and `C(f,g) ⊊ K ⊊ C(x,y)` any
> intermediate field.  With `B_K`, `Y`, `g1`, `g2` as constructed:
> 1. `B_K ⊆ C[x,y]`; `B_K` is module-finite over `C[f,g]`; `Y` is an integral
>    normal affine surface with function field `K`.  [§1.1–1.2]
> 2. `g2` is finite, flat, surjective of degree `d2 ≥ 2` with nonzero
>    trace-form discriminant `disc ∈ C[u,v]`.  [§1.3, §3.2]
> 3. `g1` is étale (everywhere), quasi-finite, dominant, open, of degree
>    `d1 ≥ 2`, and neither finite, nor proper, nor surjective.  [§1.4–1.5]
> 4. `g1(A²) ⊆ Y_sm ∖ R`, `Sing(Y) ⊆ R`, and `R` is nonempty and contains a
>    divisor (pure codim 1 by purity); every point of `R` — in particular the
>    generic point of every branch curve — is missed by `g1`.  Consequently
>    the codim-1 image hypothesis of §3.4 fails for every such `K`.
>    [§4.1–4.2]
> 5. `Y ∖ g1(A²) ⊆ A(g1)`, `A(F) = g2(A(g1))`, and
>    `g2(R) = V(disc) ⊆ A(F)`; the same inclusion holds for every missed
>    divisor.  Every irreducible component of `V(disc)` is an irreducible
>    component of `A(F)` (hence, by Jelonek's structure theorem — the one
>    citation-dependent clause — a polynomial curve).  [§4.3]
> 6. Every closed `z ∈ V(disc)` satisfies `#F^{-1}(z) ≤ d − d1`; every closed
>    `z ∉ A(F)` satisfies `#F^{-1}(z) = d`.  [§4.4]
> 7. `Y ≇ A²`.  If additionally `R` were empty, then `d2 = 1`; both horns of
>    Sol-alt's dichotomy therefore collapse to: `Y` is a non-`A²` normal
>    surface carrying a nonempty branch divisor over `A(F)`-components.
>    [§5.1, §4.1]

Clauses 1–4, 6, 7 and the inclusions of clause 5 are proved in this document
from first principles plus standard local algebra (miracle flatness, local
criterion of flatness, completion of excellent normal local rings,
quasi-finite-to-finite completion, ZMT, Riemann existence); the sole
downstream-fragile ingredient is the "polynomial curve" wording in clause 5
(Jelonek, desk-recall, decorative — dropping it costs nothing structural).
Promotion of Theorem BD is recommended; promotion of any primitivity claim is
rejected (OPEN-3).

**Typed OPEN register (no cap/analogy fills):**
- **OPEN-1** — can `Y ∖ g1(A²)` contain a divisor on which `g2` is étale
  (a missed non-branch divisor)?  No mechanism or countermodel either way.
- **OPEN-2** — must every component of `A(F)` be `g2(R)`-covered for some
  (or this) block `K`?  Only the forward inclusion is proved.
- **OPEN-3** — primitivity of minimal-counterexample monodromy ⇔ nonexistence
  of BD-sandwiches; undecided in both directions.
- **OPEN-4** — smoothness of `Y` itself (`Sing(Y) ⊆ R` is proved; `Sing(Y) =
  ∅` is not).

---

## 8. One launch, with stop conditions

**LAUNCH BD-D2 (prove-side, desk): rule out index-2 blocks.**  Target
statement: no non-invertible Keller `F` admits a block field with
`d2 = [K:C(f,g)] = 2`.  Rationale: degree 2 is Galois, so `Y` is the
normalization of `Spec C[u,v][w]/(w² − h)` with `h` the squarefree
discriminant-support polynomial, and Theorem BD pins `V(h) ⊆ A(F)` (a union
of `A(F)`-components, polynomial curves), while `g1` must be an
everywhere-étale degree-`d/2` map of `A²` into `Y ∖ {branch}` missing the
branch curve pointwise.  The attack surface: double-cover monodromy of
`π₁(A² ∖ V(h))` against simple connectivity of the source, one-place-at-
infinity structure of polynomial curves (Abhyankar–Moh–Suzuki / Lin–
Zaidenberg), and log-Euler/Riemann–Hurwitz bookkeeping on the sandwich.  Stop
conditions: **(S1)** a proof that no `d2 = 2` block exists — promote
"`2` does not divide the block index at the bottom" and iterate on small
`d2`; **(S2)** a fully consistent model of a `d2 = 2` sandwich meeting every
BD constraint — bank it as the first concrete Avenue-30/31 boundary object
and stop the obstruction attempt (it would demote OPEN-3's optimistic horn);
**(S3)** two desk sessions (or one hostile-review cycle) yielding neither —
park as typed OPEN, record the partial invariants, no cap or analogy fill.
Deliverable in either terminal state: a standalone `xmodel/` note under the
usual different-model hostile review.

## 9. Nonclaims

No claim that a Keller counterexample exists; every statement above is
conditional structure on a hypothetical object.  No exit-price assertion is
made and `charge_basis` is intentionally omitted.  No selector progress: the
§5.4 preserved gap (no arrow from an arbitrary minimal counterexample to a
bounded `td`/type/entry client) is untouched by Theorem BD, which constrains
blocks but selects nothing.  No formalization: jc2-lean was neither inspected
nor modified.  Citations marked desk-recall were not web-verified (web access
prohibited by the mandate); each is either bypassed by an in-document proof
or confined to the flagged decorative clause.

<!-- BODY-END -->
