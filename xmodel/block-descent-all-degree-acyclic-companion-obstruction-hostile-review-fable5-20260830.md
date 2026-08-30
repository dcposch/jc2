# Hostile review: all-degree acyclic-branch companion obstruction

Reviewer: Fable 5, independent co-researcher, hostile mode  
Date: 2026-08-30 UTC  
Target: `xmodel/block-descent-all-degree-acyclic-companion-obstruction-sol56-20260830.md`  
Overall verdict: **CONFIRM_WITH_CORRECTIONS** — the all-degree theorem, both
Euler-enhanced extensions, the canonical-normalization endpoint, and the
generic-field-degree-three corollary all reconstruct; two proof-articulation
corrections and one citation-pinning obligation are recorded below.  No
refutation was found.  This review asserts no exit price; receipt status
`ABSENT` is expected.

## 0. Custody and execution record

All ten charged hashes were reproduced byte-exact with `shasum -a 256`
before any content was read, including the target document
(`28f29711...e4d2eda`), its artifact (`3d0b72c7...73beb3`), the replay
(`a75a91d6...800cb98`), the pinned Arzhantsev--Zaidenberg PDF
(`41245c20...d5c36fc`), and the six coordinator-integration interfaces.  The target's internal seal was
independently recomputed: body `23932` bytes through the unique standalone
`<!-- BODY-END -->` line, body SHA-256
`4d51593b20e6bbc473e54881370a1d748ca7337a56a9dda449f5deb5ddaa8724`, file
`24265` bytes, matching the artifact JSON exactly.

This session had a working shell.  Executed: `pdftotext` on the pinned AZ
source; the desk replay ordinarily, under `-O`, under `-OO`, and with
`--mutate-drop-centrality` (also under `-O`); an AST scan of the replay.  No
heavy CAS was run.  No sibling external-model prompt, log, report, or receipt
was read; `jc2-lean` was not touched.  Exactly this one repository file is
written.

## 1. Itemized audit

### Item 1 — Arzhantsev--Zaidenberg source check: CONFIRMED

From the pinned PDF (page 3 of the print layout):

- **Corollary 1.2** verbatim: "Any disconnected, simply connected, reduced
  plane curve is equivalent to a union of r >= 2 parallel lines."
- **Theorem 1.3(b)** verbatim: "Any reduced, simply connected plane curve is
  equivalent to a curve given by one of the equations `y^{eps_y} p(x) = 0`
  (1) or `x^{eps_x} y^{eps_y} prod_{i=1}^r (y^a - kappa_i x^b) = 0` (2),
  where eps_x, eps_y in {0,1}, p in C[t] is a polynomial with simple roots,
  a, b >= 1 and gcd(a,b) = 1, r > 0, and kappa_i in C^x pairwise distinct."

The producer's transcription in section 1 is exact, including the
constraints.  Equivalence is under `Aut(A2)` ("Two plane curves C and C' will
be called equivalent if C' = gamma(C) for some gamma in Aut(A2)"), and I
verified that every theorem hypothesis (finite flat degree, integrality,
normality, non-etale support, henselian rank-one factors, `e_c(U)`) is
`Aut(A2)`-equivariant under base pullback, so normal-form reduction is licit.

**Meaning of "simply connected" for a disconnected curve.**  The paper
defines acyclic as `pi_0 = pi_1 = 1` and keeps "simply connected" as the
`pi_1`-only half.  Corollary 1.2's own wording ("disconnected, simply
connected") would be vacuous under a connected reading, and the proof of
Lemma 3.11 (Case 3) contradicts "the assumption of simply connectedness"
by producing "a non-contractible cycle in C".  So the operative meaning is:
trivial fundamental group at every basepoint, i.e. **every connected
component simply connected**.  The producer's section 6 reading is exactly
this and is correct.

Connected-case exhaustion also checks: for connected `B`, form (1) with
`eps_y=0` forces one root (vertical line); `eps_y=1` with constant `p` is the
horizontal line; `eps_y=1` with `s>=1` roots is the comb; all components of
form (2) pass through the origin, pairwise meeting only there (distinct
`kappa_i` force any intersection onto `x = 0`, hence to the origin), so
form (2) is always connected.  Sections 3 and 4 of the
target exhaust the connected list; Corollary 1.2 exhausts the disconnected
list.

### Item 2 — Normal height-one inertia, arbitrary degree: CONFIRM_WITH_CORRECTIONS

Reconstructed in full.  For finite flat `pi` the non-etale image is
`V(disc)` of the trace form, so `B` is automatically a **pure
one-dimensional** reduced curve (no purity theorem needed), and every
component `D` carries `disc` in its generic prime, so some point of `X` over
the generic point `xi` of `D` is non-etale.  Normality makes the semilocal
ring over the DVR `O_{A2,xi}` a product-free semilocal Dedekind domain with
DVR localizations; in residue characteristic zero, `e = 1` plus separable
residues means unramified means etale, so a non-etale point over `xi` has
`e >= 2`.  **Residue degrees are harmless**: a generic point `x_i` with data
`(e_i, f_i)` splits, over all but finitely many closed `b in D`, into `f_i`
distinct closed points with trivial residue extension (`C` is algebraically
closed at closed points), each contributing one cycle of length `e_i`.  Thus
the generic transverse-disk inertia has cycle type `(e_i` with multiplicity
`f_i)`: nonidentity iff some `e_i >= 2` (true, by the above), and a
generically unramified factor (`e_i = 1`) yields **exactly** `f_i` fixed
sheets — "generic unramified factor gives a fixed sheet" is exact, not just a
floor.  A rank-one henselian factor at a specific closed `b` is a genuine
section (Nakayama argument checked; rank-one finite flat over local is the
base) and fixes a sheet of the entire local group.

**Correction 2a (articulation, not truth).**  The step from DVR-level
`e >= 2` to a nontrivial disk meridian at a general closed point silently
uses the arbitrary-degree version of the charged cubic addendum's C1: each
henselian local factor at a closed point of the normal excellent `X` is
analytically normal, hence **analytically irreducible**, so over a ball
meeting `B` in one smooth disk (`pi_1 = Z`) each point contributes a single
cycle whose length is its local rank; and some component of `R` surjects
(finitely) onto `D`, so every such `b` has a point of local rank `>= 2`
above it.  The document states the DVR facts and asserts the disk
conclusion; the missing two sentences should be bound, exactly as the
addendum `b3bdd87b...` did at rank three.  Without analytic irreducibility
the claim is false — that is precisely the section 5.3 control.

**Nonnormal conductor control verified.**  `z^2 = x^2 y` is integral (`x^2 y`
is not a square), nonnormal (`w = z/x` is integral, not regular), with
discriminant `4x^2 y`, so `B = {xy = 0}`: connected and simply connected.
Off `x = 0` the normalization `w^2 = y` is unramified over the conductor
axis, and I confirmed the meridian of `x = 0` acts as the identity: the
non-etale support of a nonnormal cover can carry identity inertia.  I also
confirmed the document's claim that this example fails hypothesis 2
everywhere on `B`: at every branch point the fibre is one point, so the
henselian algebra is local of rank two with no rank-one factor.  So it is a
normality control, not a counterexample, exactly as stated.

### Item 3 — All-degree comb proof: CONFIRMED

`A2 - {y p(x) = 0}` is literally `(C - {alpha_1..alpha_s}) x C^*`, so
`pi_1 = F_s x Z` with the `Z` factor generated by the spine meridian `h` at a
general tooth-free spine point; `h` is central, which also disposes of every
based-meridian issue (all conjugates of a central element coincide, and
circles of different radii in the fibre `{x_0} x C^*` are homotopic, so
`rho(h)` is the actual generic spine inertia).  (1.1) at the spine gives
`sigma = rho(h) != 1` with nonempty proper `Fix(sigma)`; the centralizer
lemma (`sigma(gv) = g sigma(v)`) makes `Fix(sigma)` invariant under the whole
image; intransitive.  Line degenerations: `pi_1(A2 - line) = Z`, cyclic image
preserves the fixed set, intransitive.  `d = 2`: no nonidentity permutation
with a fixed point exists, so (1.1) is locally contradictory and the theorem
holds there with no global argument — matching the replay's empty degree-two
row.  Crucially, **no companion label is propagated**: tooth inertias are
never identified with the spine companion; only the spine's own (1.1) is
consumed.  Arbitrary partitions on non-companion factors and multiple
companions are covered by the fix-set identity with no case analysis.

### Item 4 — Weighted cone, both proofs: CONFIRMED

**Pointwise proof.**  Under `t.(x,y) = (t^a x, t^b y)` each factor
`y^a - kappa_i x^b` scales by `t^{ab}` and the axes are preserved, so `B` is
invariant; `N = |x|^{2/a} + |y|^{2/b}` satisfies `N(t.p) = t^2 N(p)`, each
punctured weighted ray meets `{N=1}` once, and both displayed product
decompositions hold, making the inclusion of every small sublevel complement
a `pi_1`-isomorphism (the addendum's C2 pattern: pick the ordinary analytic
splitting ball first, fit `{N <= delta}` inside it).  The origin's rank-one
factor gives a section over that ball, so the origin-local group — which
**is** the global group — fixes a sheet; the image lies in a point
stabilizer, intransitive for `d >= 2`.  Since `r > 0` in form (2), the
origin always lies on `B`, so the decomposition applies to every row,
including smooth degenerations and axis factors, with no generic-partition
input.  No global companion label appears.

**Generic + Euler proof.**  `B_i^* = B_i - {0}` are pairwise-disjoint
topological `C^*`s (injective polynomial parametrizations, `gcd(a,b)=1`).
The fibre-count `u` of the quasi-finite etale `U -> A2` is constructible, and
the semicontinuity direction is right: etale points spread out through local
sections, so nearby fibres dominate and **special values only drop**,
giving (6.1) `u(z) <= u_i` with `P_i` finite.  If `u(0) > 0` an etale point
over the vertex is a rank-one henselian factor (trivial residue extension)
and the pointwise proof applies, forcing (6.2) `u(0) = 0`.  Euler signs all
verified: `e_c(B) = 1`, `e_c(A2 - B) = 0`, `e_c(C^*) = 0`,
`e_c(B_i^* - P_i) = -|P_i|`, and constructible Fubini gives (6.3)
`e_c(U) = sum_i sum_{P_i} (u(z) - u_i) <= 0`, contradicting `e_c(U) > 0`.

**Sharp control recomputed.**  For `w^4 + a w + b`: discriminant
`256 b^3 - 27 a^4` (checked), irreducible weighted cone; `X ≅ A2_{(w,a)}`;
`R = {a = -4w^3}`; `U ≅ A1_w x Gm_{a+4w^3}`, `e_c(U) = 0`.  Two double roots
or a triple root force `a = b = 0`, so `P = empty` and (6.3) is saturated
with equality — positivity cannot be weakened to `>= 0`.  The section 5.1
cusp control `z^3 - 3xz + 2y` (discriminant `108(x^3 - y^2)`, checked)
likewise has `U ≅ A1 x Gm`, `e_c(U) = 0`, so it evades the generic version
through the Euler gate and the pointwise version through the vertex — both
firewalls are exact.

### Item 5 — Disconnected parallel-line inequality: CONFIRMED

`pi_1(A2 - r parallel lines) = F_r`, freely generated by a based meridian
system, so the image is `<sigma_1..sigma_r>` and conjugation ambiguity only
conjugates the subgroup.  Normality plus generic companions give each
`sigma_i != 1` with a fixed point, hence `c_i >= 1` and `2 <= s_i <= d-1`.
The document correctly builds spanning trees **per nontrivial cycle**
(`s_i - c_i` edges each), not per support: a permutation's disjoint cycles do
not connect each other, so charging `s_i - 1` edges would be wrong; the
per-cycle count makes the graph components exactly the orbits.  Transitivity
gives `sum(s_i - c_i) >= d-1`, hence `sum s_i >= d-1+r >= d+1` for `r >= 2`
(6.4), and with lines of Euler characteristic one and drops-only special
fibres, `e_c(U) <= d - sum s_i <= -1` (6.5) in every degree, contradicting
`e_c(U) > 0`.

**New sharp witness (this review).**  The explicit Keller-shaped cover

```text
(t, y) |-> (3t^2 - 2t^3, y),        X = A2 -> A2,   degree 3
```

has critical locus `{t=0} u {t=1}`, branch `B = {x=0} u {x=1}` (two parallel
lines), fibre partition `(2,1)` with a rank-one companion factor at **every**
branch point (`3t^2-2t^3 = (t)^2(3-2t)` shape at `0`;
`3t^2-2t^3-1 = -(t-1)^2(2t+1)` at `1`), transitive `S3` monodromy, and
`U = (C - {0,1}) x C` with `e_c(U) = -1 = d - sum s_i`.  This (i) realizes
the replay's abstract two-transposition control geometrically, (ii) saturates
(6.4) and (6.5) exactly, and (iii) **proves the pointwise theorem's
connectedness hypothesis is essential**: every-point companions with a
disconnected simply-connected branch are realizable, so clause 1 of the
section 0 theorem cannot be relaxed and the disconnected extension genuinely
needs `e_c(U) > 0`.  The producer's architecture places the hypotheses
exactly at this boundary.

### Item 6 — Canonical-normalization endpoint: CONFIRMED

Every interface reconstructs at `d1 = 1`:

- **Finiteness and containment.**  `S` finite over `A = C[F,G]` (finiteness
  of normalization for the excellent polynomial ring); a monic equation over
  `A` is one over `C[x,y]`, which is integrally closed in `L`, so literally
  `S subset C[x,y]`, giving `j` with `F = pi o j`.
- **Finite flatness.**  Normal surface implies Cohen--Macaulay; miracle
  flatness over the regular target; degree `d`.
- **Open immersion.**  `j`-fibres sit in fibres of the etale (hence
  quasi-finite) `F`, so `j` is quasi-finite and birational; Zariski Main into
  the normal `Y` makes it an open immersion; `pi` restricted to `j(A2)` is
  `F o j^{-1}`, etale, so `j(A2)` avoids `R`, and only
  `R subset Y - j(A2)` is claimed (correct: the boundary may contain
  unramified points).  `R != empty` for `d >= 2` since `A2` is simply
  connected and `Y` is connected.
- **Generic companion over every component.**  `p_D(F,G)` is nonconstant
  (injectivity of `C[u,v] -> C[x,y]`), its nonempty zero curve maps
  quasi-finitely into `D` with dense constructible image, and every point of
  it factors through the ramification-avoiding chart, so `u >= 1` on a dense
  subset of every `D` — the `d1 = 1` specialization of the reviewed
  missed-principal-divisor mechanism, self-contained here.  Correctly only
  generic: omitted target values remain possible and are handled by the
  Euler substitute.
- **Ruling.**  Affineness via Stacks `0ECD` exactly as in the promoted
  packet (finite morphism from the normal affine `Y` to regular `A2`; the
  affine-morphism conclusion plus affine `Y`); smoothness from etaleness;
  rationality is literal (`C(U) = C(x,y)`); units by pullback along dominant
  `j`; `bar-kappa(U) = -infinity` by the correct monotonicity direction
  (dominant generically finite `A2 -> U` pulls log-pluricanonical sections
  back injectively); Miyanishi--Sugie plus the charged fibration extension
  and Gurjar--Miyanishi fibre lemma give `rho: U -> C`, `C = A1` or `P1`,
  reduced fibres disjoint unions of `A1`, and
  `e_c(U) = e_c(C) + Q >= 1`.

**Hidden `d1 > 1` check: none found.**  I walked section 2 of the promoted
ruling integration step by step; every step consumes only dominance,
etaleness/quasi-finiteness of the first leg, and the sandwich properties —
all independently established here at `d1 = 1` (indeed strengthened: the
first leg is an open immersion).  The "proper block" phrasing in the
promoted packets is scope labeling of those seals, not a mathematical
dependency; the target legitimately re-derives inline rather than consuming
a promoted theorem outside its firewall, and says so.  The morphic
rational-forest license is likewise satisfied on its own terms: `j` is an
everywhere-defined dominant morphism `A2 -> U`, exactly the interface whose
absence refuted the retracted rational-map version.

### Item 7 — Generic-field-degree-three corollary: CONFIRM_WITH_CORRECTIONS

- **Point bijectivity.**  A non-etale local factor at a residue-`C` point has
  rank `>= 2` (rank-one flat local factors are sections, hence etale), and
  `2 + 2 > 3`, so each branch value carries exactly one non-etale point; this
  needs no smoothness of `Y`, so it holds at singular points too.
  `R_red -> B` is then a finite continuous bijection of locally compact
  Hausdorff analytic spaces, hence a homeomorphism.  Confirmed.
- **Nonproperness interface.**  `R` lies in the dense chart's boundary; a
  chart sequence converging to a point of `R` escapes every compact set of
  the source while its `F`-image converges, so `pi(R) subset A_F`; since
  `B` is a pure curve and `A_F` a curve, each component of `B` is an
  **entire** component of `A_F`; equality of the whole curves is never used.
  Confirmed, with the containment/equality distinction kept throughout.
- **Source forest and (8.1).**  Chau's parametrization gives each component
  of `B`, and via the finite bijection (birational per component in
  characteristic zero) each component of `R_red`, normalization `A1`.  The
  morphic forest theorem applied to a completion resolving `bar R` and
  infinity makes the affine incidence multigraph of `R_red` (self-nodes
  become parallel edges through the exceptional tree; distinct intersection
  points get disjoint chains) a minor of a forest, hence a forest; so
  `e_c(R_red) = b0(R_red)` and (8.1) follows through the homeomorphism.
- **Census and uniqueness.**  `S0 subset B` finite (item 6 genericity plus
  constructibility); fibre census `(1,1,1)/(2,1)/(3)` with `u = 3/1/0`
  forced by rank arithmetic; `e_c(U) = 3 - 2h - |S0|`; against
  `e_c(U) = e_c(C) + Q`, the `P1` branch reads `2h + |S0| + Q = 1`,
  impossible for `h >= 1`; the `A1` branch reads `2h + |S0| + Q = 2` with
  unique solution `h = 1, S0 = empty, Q = 0`.  Confirmed.
- **Closure.**  `h = 1` plus forest plus unibranch components (self-nodes
  are forbidden, so normalization is bijective and each component is
  topologically `A1`) makes `R_red`, hence `B`, contractible; `S0 = empty`
  upgrades the generic companion to a rank-one henselian factor at **every**
  branch point; the section 0 theorem then contradicts integrality.
  `[C(x,y):C(F,G)] != 3` follows, correctly glossed as generic field degree.
  No Picard and no Hartogs appear anywhere in sections 7--8.

**Correction 7a (trust boundary, must be pinned).**  The Chau citation
(Ann. Polon. Math. 84 (2004), Theorem 1) is the single external mathematical
input of section 8 that is not pinned in the charged set (the classical
surface-theory inputs are consumed through the reviewed ruling packet).  The
same citation was consumed by the reviewed cubic one-place packet, and the
weaker consequence actually used — every component of `A_F` has `A1`
normalization — also follows from Jelonek's earlier general theorem that
`A_F` is a `C`-uniruled curve for any dominant polynomial pair, with no
Jacobian hypothesis.  Still, a pinned PDF (Chau or Jelonek) should be added
to `refs/` and hash-charged before this endpoint is consumed downstream.

**Correction 7b (minor).**  Section 8's one-place argument should state the
singular-point clause explicitly (rank arithmetic is smoothness-free), as
the cubic packet's section 2.1 did; one sentence.

### Item 8 — Replay: CONFIRMED

- Ordinary, `-O`, and `-OO` runs: exit 0, **byte-identical** stdout, SHA-256
  `71499353da07d047ec0d222454649779769e331db013845a5af3370fe7ebd35b`,
  matching the document.
- Embedded `payload_sha256`
  `3586519ac48ca485bf4c91e8d32a5a89b3ebf3f77329b2e925abefd2e805f492`
  recomputed from the canonical serialization: match.
- `--mutate-drop-centrality`: exit 1 with
  `RuntimeError: an allowed comb image moved a spine-fixed sheet out of the
  fixed set` and empty stdout; the mutation also fails under `-O`.  All
  checks route through `require()`/`RuntimeError`; AST scan confirms **zero
  `Assert` nodes**, so no `-O` fail-open channel exists.
- Payload independently recomputed: relevant cycle types per degree equal
  `p(d-1) - 1` (0,1,2,4,6,10,14 for `d = 2..8`), centralizer element totals
  2, 7, 30, 101, 486, 2367 hand-verified from centralizer orders, point
  stabilizer orders `(d-1)!`, degree-two row empty, 3-cycle control
  transitive, two-transposition control of order 6 with support sum
  `4 = d+1` and Euler bound `-1`, nonnormal identity fixed set improper.
- **Separation is honest**: the script and section 9 disclaim any encoding
  of the classification, complement presentations, inertia, henselian
  comparison, or cover realization; the arbitrary-degree theorem rests on
  the section 2 identity, and the `d <= 8` sweep is a control, not the
  proof.

## 2. Consolidated corrections

1. **(2a)** Bind the arbitrary-degree C1 articulation into section 1, fact
   three: analytic irreducibility of henselian local factors on the normal
   excellent source, plus a component of `R` surjecting onto each branch
   component, yield the single-cycle-per-point disk picture at every general
   closed point.  Two sentences; the cubic addendum already contains the
   rank-three template.
2. **(7a)** Pin Chau (or Jelonek) as a hashed `refs/` PDF before downstream
   consumption of section 8.
3. **(7b)** Add the smoothness-free clause to the one-place step.
4. **(Cosmetic)** In section 0, the sentence extending the Euler-enhanced
   version to disconnected `B` should repeat the `e_c(U) > 0` hypothesis
   inline: the witness in item 5 above shows the pointwise theorem is
   **false** for disconnected `B`, so a scope misreading of that sentence
   would be fatal, and the hypothesis restated once costs a clause.

None of these changes a conclusion.

## 3. Maximum-safe theorem

> **(a) Pointwise version.**  Let `pi: X -> A2_C` be finite flat of degree
> `d >= 2` with `X` integral and normal, and let `B`, the reduced non-etale
> image support, be nonempty, **connected**, and simply connected.  If the
> henselian fibre algebra at **every** point of `B` has a direct factor
> locally free of rank one, no such cover exists.
>
> **(b) Generic + Euler version.**  Same sandwich, `U = X - NonEt_X(pi)`.
> If every irreducible component of `B` has a generically unramified sheet,
> every **connected component** of `B` is simply connected (`B` may be
> disconnected), and `e_c(U) > 0`, no such cover exists.

Exact firewalls, each with a verified witness: one companion-free branch
point defeats (a) (`z^3 - 3xz + 2y`, vertex only); `e_c(U) = 0` is
realizable under all other hypotheses of (b) (`w^4 + aw + b`, and the cusp
cubic), so positivity is sharp; disconnected `B` with every-point companions
is realizable at `e_c(U) = -1` (`(3t^2 - 2t^3, y)`), so (a) cannot drop
connectedness and (b) cannot drop the Euler gate; nonnormal `X` can carry
identity conductor inertia (`z^2 = x^2 y`), so normality is load-bearing in
(1.1).  No statement is made for any branch point lacking a length-one
factor, for `B` with a non-simply-connected component (e.g.
`z^3 - 3z + 2 + xy`), or for any nonreduced or non-curve branch structure.

## 4. Exact endpoint corollary

> For a hypothetical noninvertible complex Keller map of any generic field
> degree `d >= 2`, the canonical normalization
> `A2 --j--> Y --pi--> A2` satisfies `e_c(Y - R) >= 1`, has a generic
> unramified sheet over every branch component, and therefore its reduced
> branch support has at least one connected component with nontrivial
> fundamental group.
>
> At `d = 3` the one-place census forces the branch contractible with
> companions everywhere, contradicting the theorem; hence **no complex
> plane Keller map has generic field degree `[C(x,y):C(F,G)] = 3`**,
> conditional only on the pinning obligation of correction 7a (Chau or
> Jelonek).  This is field degree, not total polynomial degree, and it
> strictly supersedes the strict-intermediate cubic-block exclusion: the
> middle surface is the full-field normalization and the first leg is an
> open immersion.

## 5. Cheapest useful successor

**BD-A2-QUARTIC-TWO-POINT-CENSUS.**  At `d = 4` the rank arithmetic allows
up to two non-etale points per branch value (`(2,2)`), so `R_red -> B` loses
bijectivity and target conductor identifications can create branch cycles
that the source forest does not see.  Every other ingredient is already
licensed at `d1 = 1` for all degrees: the sandwich, generic companions,
the morphic forest on `R_red`, the ruling identity `e_c(U) = e_c(C) + Q >= 1`,
and the new theorem's requirement that some component of `B` be
non-simply-connected.  The successor stratifies `B` by fibre type
`(2,1,1) / (2,2) / (3,1) / (4)`, writes `e_c(U) = 4 - (census)` against the
ruling identity, and adds the quotient comparison of `e_c(B)` with
`e_c(R_red) = b0(R_red)` under the finite surjection.  Deliverable gate:
decide whether the `P1` base dies at `d = 4` and enumerate the surviving
`(h, |S0|, strata)` rows.  Before it runs, discharge correction 7a by
pinning the parametrization source — that is the cheapest single action
protecting the already-proved `d = 3` endpoint.

## 6. Fallacy sweep

Per `FALLACY-v2.md`: no cv-flag/place/series identification arises; no
exit-set charge is made and no `charge_basis` line is emitted (receipt
`ABSENT` expected); all inequalities were checked for direction at their
point of use ((6.1) drop-only, (6.4)--(6.5) floors, `e_c(U) >= 1` a floor
consumed as a floor); no `sat()` or CAS normal-form claims occur; ring maps
in section 7 are declared with their coefficient fields; `REPRESENTATIVE`
vs attainment does not arise; every gap found had a safe replacement and is
recorded as a correction rather than filled by analogy.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `25124`.
- Body SHA-256:
  `49a081ea4f3c17ebd9b02d0ea4478fcf753f26d25d8789e8289ccbafe2e9a617`.
- Frozen basis: `d08e8e5f50161d753f3fb86a6d4854afbc7e0390`.
