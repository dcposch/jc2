# Grok lateral sweep 2 — after T2→T4, into the actual remainders

**Date:** 2026-08-17  
**Author:** Grok 4.6  
**Scope:** new attacks on the three holes that are still load-bearing after
yesterday: the *corner-to-tree* remainder of G2 (TRANSPORT is a
normalization theorem, not a dictionary), off-axis completeness / universal
landing (G4), and a depth-stabilization argument that would turn the
D21→D23→D25→⋯ grind into a single theorem. Plus one framing that is none
of those. One file, no other modifications, no git.

This is a generation pass, not a review, and not a coordinator increment.
I am not proposing another CORE2 presentation, another D25 emission as
the strategy, another priced-cell census, or another TDBOUND scan. Those
are what yesterday's objects are already doing. The new fact of the last
twenty-four hours is that a 13-dimensional D21 window is nonempty mod \(p\)
at three primes and that sampled points die at D23. The right response is
to ask whether that inverse system can stabilize, and to attack the two
reduction remainders with objects the books do not already enumerate.

Checked against, and not repeating: `xmodel/grok-lateral1.md` (edge-power
Bézout defect, \(\mathrm{SL}_2\)-push of the chain, GGV6 masses = \(\Lambda\),
reciprocal-characteristic compactification, Kummer cover of an on-axis
book, \(\operatorname{Pic}\) of the graph in \(\mathbf P^2\times\mathbf P^2\));
`xmodel/sol-lateral3.md` (coordinate-cusp / simultaneous NF — now a
theorem; symbolic off-axis grammar; paired fiber-tagged Newton-cut
functor; primitive monodromy; contextual live-kernel; first-disagreement
rigidity; codifferent traces; \(C_6\) prolongation); `xmodel/sol-lateral.md`,
`xmodel/sol-accel2.md`, `xmodel/sol-avenues2.md`, `TRANSPORT.md` Conjecture T,
`TDBOUND.md` (coincidence-risk, \(\Delta^2\ge-2\)), `REDUCTION.md` CRITICAL
3/5/7, `SHEET6-DIRECTIONB.md` §7.S4–§8.S, `SHEET6-DEPTH.md`,
`BOOK-OFFAXIS.md` P5. Witt–Bockstein, `ctl0` continuation, LND descent,
farm-certificate interpolation, Hall deficiency, SOS, \(K_2\), \(p\)-adic
mass, \(\mathbb A^1\)-degree, CAP-DEN, Fitting kernels, forbidden
tower-minors of *already-killed* routes, high-tail gauge as a pin, fence
powers, no-log pins, toric circuits, St 9.4 equality, Mittag-Leffler of
the Keller primitive, coefficient holonomy, positive off-axis Puiseux
lifts, Gorenstein semigroups, Hermite–Padé, NF-Z/P/M, and Favre–Jonsson
eigenvaluations remain off this list because they are already on the board.

Novelty here means: no matching attack in that corpus. Each entry names
its nearest neighbor so the claim is falsifiable.

Last-24h calibration, used as input not as decoration: CORE2 fiber
nonempty mod \(p\) at three primes, 397-element GB, 13-dimensional, pole
scales pinned (\(W_1^4\), \(W_2^4\)); 0/12 sampled D21 points survive the
D23 Row_22 block; D23-core emitted (87 vars / 77 eqs, hybrid, minutes);
td-12 book closed at honest tier; TDBOUND downgraded to coincidence-risk
with the \(\sum a_F b_F/\nu_F\le 1\) / \(\Delta^2\ge-2\) reformulation as
the real lemma; transport = T2→T4 theorem, Conjecture T still open.

---

## What I would actually fund

| # | idea | gap it hits | why it is not a grind increment |
|---:|---|---|---|
| 1 | Edge-power comb menu | G2 remainder | Lattice + Cor. 7.4 factorization → finite predicted trees; no jet, no book |
| 2 | GGV-fan exceptional orders | G2 remainder | Dual graph of a finite toric resolution, not a Puiseux functor |
| 3 | Higman / Dickson on fat records | G4 landing | Finiteness by well-quasi-order, not by listing or compactifying a chart |
| 4 | Saturated CORE2 inverse system | D-∞ theorem | Ascending chain in a *fixed* Noetherian ring; D23 is the first step, not the strategy |
| 5 | Greenberg function of the jet scheme | D-∞ theorem | Names a finite \(D_*\) such that \(V_{D_*}\) empty iff \(V_\infty\) empty |
| 6 | Deleted-centers pencil is Du Val | G5, other framing | ADE classification, not a census correlation and not Hodge-index |

If only two pilots run: **#4 and #1**. #4 uses the object that already
exists on disk (`cases/directionb_core23_p*.ms`) and either kills the
D21 image at variety level or exhibits the first nontrivial chain step.
#1 is a finite factorization on the four gate-B chains plus two
automorphisms; it either gives Conjecture T a predicted finite menu or
dies in a day. #5 is the theorem-shape that makes the rest of the depth
ladder honest, and should start the moment a D25 core can be emitted as
a shape census (already pre-registered as minutes-cheap).

---

## 1. Edge-power combs: the GGV chain predicts a finite Eggers–Wall menu

**Gap:** G2 remainder — `TRANSPORT.md` Conjecture T; `REDUCTION.md`
CRITICAL 3. T2→T4 is real; the GGV ledger still does not name a Sigray
tree.  
**Side:** proof. The payoff is that the sheet engine starts from a
*predicted finite list of decorated combs*, not from a search over T7.

### Five-line pitch

1. GGV Cor. 7.4 says every certified edge is a power
   \(\ell_{\rho,\sigma}(P)=\lambda R^{qm}\). A plane branch (or a finite
   cluster of them) whose Newton faces are all powers has embedded
   resolution a *comb*: a spine indexed by the chain, with teeth the
   distinct roots of each \(R_h\).
2. The lattice data already in `lib/families.py` bound the comb: the
   direction list is the spine, each \(q_h\) is the contact of that
   tooth-generation, and the number of teeth at step \(h\) is at most
   \(\deg R_h\), which is a face-length quotient and is finite.
3. Pole status is not a further jet: it is whether the companion
   leading form of \(Q\) *vanishes* at that root of \(R_h\). Shared root
   ⇒ residual cancellation (possibly not a pole). Residual nonvanishing
   ⇒ the place is a pole and the mass is an intersection number of the
   two leading forms.
4. So the functor is not “chain → unique tree.” It is “chain → finite
   set of decorated combs,” one per root-sharing pattern. That set is
   the missing G2 input to T6–T7.
5. Combined with the already-proved rotations of `TRANSPORT.md`, the
   T2-selected pair lands in a *computed* T7 menu. The book then
   adjudicates a list, not a fork.

### Nearest neighbor, and why this is not it

Sol's Rank 3 (`xmodel/sol-lateral3.md`) is a paired, fiber-tagged
*Newton–Puiseux cut forest* — a jet construction that carries every
residual coefficient. This idea never opens a Puiseux jet. Yesterday's
#2 pushes directions by \(\mathrm{SL}_2\) and reads a type; yesterday's
#3 identifies GGV6 pairings with masses. Neither produces a tree
*shape*. Favre–Jonsson is a dynamical eigenvaluation on the valuative
tree and was already declined. Approximate-root *ladders* are the tower
trust set; they have never been read as the dual graph of a comb.

### First concrete test

Work on the polynomial start polygons, before \(\psi_j\).

1. For the four gate-B chains in `lib/FAMILIES.md` —
   \((9,27)\), \((9,24)\), \((8,28)\), \((7,21)\), directions
   \(((1,0),(3,-1))\), \(((3,-1))\), \(((4,-1))\), \(((7,-2))\) and
   tags \((p_h,q_h)\) as in `cd.steps` — compute, from face lengths and
   \(q_h\) alone, the maximum number of teeth at each spine vertex.
   Emit the finite set of abstract combs.
2. Decorate each comb by the \(2^{\#\text{teeth}}\) root-sharing
   patterns (Q-leading-form vanishes or not). Discard any decoration
   that makes every place finite: a Keller pair of type \((\alpha,\beta)\)
   with \(td\ge 6\) has at least one pole.
3. Controls, with coefficients: \((x,y+x^k)\) and \((x+y^2,y)\), put in
   GGV-standard shape if they admit one, otherwise recorded as
   “no-chain, td=1.” Their actual Eggers–Wall trees (hand, one page)
   must lie in the predicted menu, and every place of \(g\) must be
   finite. A predicted pole on an automorphism is a bug in the sharing
   rule, not a JC2 theorem.
4. One farm-side check: the \((8,28)\) comb menu, pushed through
   `TRANSPORT.md` (4.1)–(4.5), must not contain a T7 entry that the
   Bézout residual of that support forbids. A forbidden output is a
   dictionary bug.
5. No `msolve`. Output: four finite lists of decorated combs, plus
   two automorphism controls.

### Kill criterion

Kill if the predicted menu, on any of the four chains, is *all* of T7
at every \(td\) compatible with the support — then the comb restriction
is vacuous and G2 has not been reduced. Kill if a realized
automorphism's tree is not a comb of this type (a genuine branch point
that is not a Cor. 7.4 tooth). Kill if two coherent polynomial pairs
with the same chain and the same leading-form root-sharing have
different labelled pole trees: then jets really are necessary and the
thin functor is insufficient. A menu that works on automorphisms and is
empty on gate B is information (those chains cannot be realized as
Keller pairs in this decoration language), not a kill.

---

## 2. GGV-fan exceptional orders: pole status is a support function

**Gap:** the same G2 remainder, from the dual side.  
**Side:** proof. Eggers–Wall *is* the dual graph of the embedded
resolution; this writes that graph from the GGV fan.

### Five-line pitch

1. A GGV complete chain is a finite list of directions \((\rho_h,\sigma_h)\).
   Those rays, plus the two axes, are a fan \(\Sigma\) in \(N_{\mathbf R}\).
   The toric blowup of the line at infinity along \(\Sigma\) is a finite
   computation from `cd.steps`.
2. On each exceptional \(E_h\), \(\operatorname{ord}_{E_h}(P)\) and
   \(\operatorname{ord}_{E_h}(Q)\) are the support functions of the
   polygons \(mS\) and \(nS\). No coefficients enter.
3. After Cor. 7.4, each edge leading form factors. The non-toric
   blowups that finish the embedded resolution sit at the intersection
   points of the proper transform with \(E_h\), one per distinct root,
   and are again finite.
4. A component is a *pole* of a generic \(f\)-fiber precisely when
   \(\operatorname{ord}_E(Q)\) is strictly smaller than the order
   forced by the type ratio — i.e. when \(Q\) is more polar than
   \(P^{n/m}\) along \(E\). Residual cancellation is the opposite
   inequality. That is Conjecture T's missing bit, as a lattice
   inequality on exceptional divisors.
5. The dual graph of this (toric + tooth) configuration, decorated by
   those orders, *is* the Sigray Eggers–Wall pole tree of the
   T2-selected pair, up to the already-proved rotations.

### Nearest neighbor, and why this is not it

This is the resolution dual of idea 1 and of Sol's Newton-cut functor.
It is not Favre–Jonsson: there is no eigenvaluation, no tautological
metric, no dynamics. It is not yesterday's \(\mathrm{SL}_2\)-push: the
fan is not pushed into a Sigray chamber and then abandoned; the
exceptional *orders* are the decorations. FACE-ISOLATION uses mixed
volume as a char-\(p\) slogan, not as an order along \(E_h\).
`SHEET6-CLASSICAL.md` T1 computes splice determinants *after* the sheet
data are chosen; this computes the dual graph *from the GGV fan*,
before any sheet packet.

### First concrete test

1. Build \(\Sigma\) for each of the four gate-B direction lists. Write
   the support functions of \(mS\) and \(nS\) on every ray (the
   polygons are in `supports(cd)`).
2. For each ray, record the sign of
   \(n\cdot\operatorname{ord}_E(P)-m\cdot\operatorname{ord}_E(Q)\).
   This is the candidate pole bit.
3. Same two automorphism controls as idea 1: every exceptional order
   of \(g\) on a generic \(f\)-fiber must come out nonpolar. One
   monomial-map control: the rectangular hull of residue-A,
   \((k_f,l_f)=(126,42)\), \((k_g,l_g)=(189,63)\), must produce
   *exactly two* polar components, matching \(\Lambda=(3,3)\). That
   hull is not residue-A, but it is the leading-form shadow, and the
   order computation is exact on it.
4. Compare the dual graph of the \((8,28)\) fan, after the
   `TRANSPORT.md` axis swap, with the comb menu of idea 1 on the same
   chain. Disagreement is a bug in one of the two dictionaries.
5. No Groebner. Output: four fans, a table of orders, a pole-bit
   vector, one residue-A-shadow control.

### Kill criterion

Kill if the pole bit along a ray depends on the choice of linear
coordinates inside the GGV-standard class (it must be invariant under
the residual torus and under the already-proved \(C,R\)). Kill if the
residue-A rectangular shadow produces a number of polar components
other than two, *and* the missing or extra components cannot be
accounted for as non-toric teeth of the \((2,3)\) leading form. Kill if
the dual graph changes when the target automorphism \((f,g)\mapsto(f,g+f^2)\)
is applied: target mixing must not move source exceptional orders of
the *pair* except by an \(\mathrm{SL}_2^{\mathrm{target}}\) action that
the decoration already tracks. A fan that is too coarse (only toric,
no teeth) is a failed first approximation, not a kill; add the
Cor. 7.4 teeth and rerun.

---

## 3. Higman–Dickson landing: live off-axis records are well-quasi-ordered

**Gap:** G4 — `REDUCTION.md` CRITICAL 5; `BOOK-OFFAXIS.md` P5. The
generic grid has unbounded numerator and \(M\); there is no completeness
certificate for any \(b\ge 2\) entry.  
**Side:** proof. Completeness by a well-quasi-order, not by a compact
chart and not by a grammar.

### Five-line pitch

1. An off-axis fat record is a finite word in a finite event alphabet
   (the priced menu P0 / St 9.6 families / merge schemas) together with
   a tuple of nonnegative integer registers \((M_i,\operatorname{num} w_i,\nu_i,\ldots)\).
2. Higman's lemma well-quasi-orders the words; Dickson's lemma
   well-quasi-orders the register tuples; the product well-quasi-orders
   fat records under *minor* = “subword + coordinatewise \(\le\) on
   registers.”
3. If *death* is minor-closed (a dead minor of a live record is
   forbidden — equivalently, liveness is an upset), then the live
   records are a WQO-downset and there are only finitely many
   *minimal* live records at each T7 entry. That finite set *is*
   \(B_{\mathrm{off}}(d,E)\).
4. The td-7 inversion of the family \(w=2/(2k+1)\) is the planted
   positive example: those records form a Dickson *chain* in the
   register \(k\), not an antichain, and the inversion is the
   statement that the chain dies at a bounded minor.
5. Unbounded numerator is then harmless. An infinite grid can still
   have a finite live upset. P5's “no completeness certificate”
   becomes “prove minor-closed, then enumerate the finite antichain of
   minimal live records.”

### Nearest neighbor, and why this is not it

`xmodel/sol-accel2.md` contracts *already-killed* routes by forbidden
minors; that is a dual of existing kills, not a completeness theorem
for the live language. Sol's Rank 2 is a finitely presented grammar
with symbolic `OPEN`s; it proves landing of a derivation, not finiteness
of live records. Yesterday's #4 compactifies the characteristic; #5
covers off-axis by a Kummer extension of the on-axis book. NF-Z/P/M
quotients words. Contextual live-kernel (Sol Rank 5) quotients by
future-equivalence in a *fixed* context. None of these is “liveness is
an upset in a WQO.”

### First concrete test

1. Encode the td-7 §11a 17 cells and the 62 budget-fitting merge cells
   of `BOOK-OFFAXIS.md` §10 as fat records: event word plus the
   registers the priced menu actually consumes.
2. On this finite sample, test the hereditary claim in both directions.
   (a) If \(A\) is DEAD and \(B\) has \(A\) as a minor, is \(B\) DEAD?
   (b) If \(B\) is LIVE and \(A\) is a minor of \(B\), is \(A\) LIVE?
   One failure of (a) with a clear extra priced event in \(B\) is a
   *repair* (minors must retain priced letters); one failure of (a) with
   \(B\) obtained from \(A\) only by raising a register is a genuine
   kill of death-as-minor-closed.
3. Mandatory chain: the inverted family \(w=2/(2k+1)\). Confirm it is
   a Dickson chain in \(k\), and that the filed closure is a minor of
   every larger-\(k\) record. If those records are an *antichain*, the
   embedding is wrong; change the register coordinates (the inversion
   itself says \(T=1/k\) is the right one) and rerun.
4. One td-11 A/B/C pure-neutral probe: the co-scaled \(5^k\) tuples
   that die at a common earlier \(X\) (`xmodel/sol-lateral3.md` Rank 5's
   planted example) must be a Dickson chain of dead records, not an
   antichain of live ones.
5. No Groebner. Output: a yes/no hereditary table, plus the embedding
   that makes the td-7 inversion a chain.

### Kill criterion

Kill if the finite td-7 sample already contains a LIVE record with a
DEAD register-only minor — then death is not minor-closed in the
registers the engine actually uses, and WQO cannot enumerate the live
set. Kill if there is an infinite antichain of *jointly live* records
in one filed T7 entry (incomparable event words, all live at every
register). A new event letter required by a printed St 9.6 family is a
repair of the alphabet, not a kill. Do not claim completeness from
Higman alone without the hereditary check: WQO of the ambient is free,
and worthless.

---

## 4. The window ideal as an ascending chain in the CORE2 ring

**Gap:** the D25/D27/D-∞ iteration has no theorem. D21 is 13-dimensional
and nonempty mod \(p\); samples die at D23; the pre-registered move is
to emit D25 if D23 is nonempty. That is a grind unless the inverse
system stabilizes.  
**Side:** proof. This is the Noetherianity / saturation argument the
ladder is missing.

### Five-line pitch

1. Let \(A\) be the CORE2 coordinate ring after saturating by the pole
   scales: the 27-variable unsplit ring (or the 22-variable fiber ring)
   localized at \(W_1W_2\), i.e. the chart the D21 locus actually lives
   on. This is a finitely generated \(k\)-algebra, hence Noetherian.
2. For each even depth \(D\ge 21\), let \(V_D\) be the window at that
   depth and let
   \(J_D=\ker\bigl(A\to k[V_D]\bigr)\)
   be the elimination ideal of the new tails onto \(A\). Then
   \(J_{21}\subseteq J_{23}\subseteq J_{25}\subseteq\cdots\)
   is an ascending chain in \(A\), and stabilizes at some \(J_{D_*}\).
3. The last twenty-four hours already say the chain *moves* at the
   first step: 0/12 D21 points lie in \(V_{23}\), so those points are
   in \(V(J_{21})\) and not in \(V(J_{23})\), on one prime, as a
   sampling statement. The theorem is that the chain cannot move
   forever.
4. If the deeper tails are integral over \(A\) after saturation (the
   Row_22 block is polynomial in the deep tails, quadratic in highs,
   coefficients in \(A\)), the maps \(V_{D+2}\to V_D\) are finite and
   \(V_\infty=\emptyset\) if and only if some \(V_D=\emptyset\). That
   is the missing implication from “samples die” to “the germ dies.”
5. One Groebner run in a *fixed* ring then replaces the infinite
   ladder: compute \(J_{D_*}\) by eliminating the D23 (then D25, if
   needed) extra tails onto CORE2. If \(J_{D_*}=(1)\), residue-A is
   empty at the window tier as a variety statement, not a sample.

### Nearest neighbor, and why this is not it

Mittag-Leffler in `xmodel/sol-avenues2.md` is adjoint compatibility of
the Keller primitive as a meromorphic one-form; it is not an inverse
system of window ideals. Fitting kernels and Hermite–Padé are already
closed or on the board as *row* instruments; they do not name a chain
in a fixed ring. `xmodel/sol-instrument3.md` §4 treats D23/D25 as a
bounded shape census and explicitly warns that “more equations, same
variables” was false on the first reactivation. This idea agrees with
that warning: the new tails are new variables, which is why one must
*eliminate them back* onto \(A\) rather than grind a larger core.
Algkill (`xmodel/sol-algkill.md`) says every D23 *prefix* extends to a
polynomial in the support rectangle; that is about separate
algebraization, not about the ascending chain of joint images.

### First concrete test

The D23-core is already on disk:
`cases/directionb_core23_p{105337,105673,200257}.ms`
(38 CORE2 rows + 22 pivots + 10 Row_22 + rad/sat).

1. Identify the 10 deep-tail variables of Row_22 (levels 49/54).
   Eliminate them, and only them, from the D23-core ideal onto the
   CORE2 variable set. Saturate by \(W_1W_2\) (the `uW` rows already
   make this the chart). Do this at p105337 first; the other two
   primes are the robustness check.
2. Three exact outcomes, all informative:
   - \(J_{23}=(1)\): the D21 image is empty at D23 as a variety. This
     upgrades 0/12 samples to a window-tier kill and is the end of
     the residue-A screening argument (then char-0 of the small
     core).
   - \(J_{23}=(0)\): D23 does not cut the CORE2 base; the sample
     deaths are fiberwise. Then this ambient is the wrong Noetherian
     ring (see kill). Record that, do not pretend the chain moved.
   - \(J_{23}\) proper nonzero: the chain has moved. Compute
     dimension of \(V(J_{23})\) against the known 13. If the cut is
     supported only on the eight near-42 `tg*` frees and leaves the
     five-variable dead-stretch/merge block free, the 13-fold is
     mixed (gauge plus genuine) and the next ambient is the merge
     block's invariant ring.
3. Independent check, no new emission: replay the 12 dead sample
   points against \(J_{23}\). They must lie on \(V(J_{23})\) if
   \(J_{23}\ne(1)\), and must fail to lie on \(V_{21}\) only through
   coordinates that \(J_{23}\) actually cuts.
4. If \(J_{23}\) is proper nonzero, emit D25 only as a *shape census*
   (already pre-registered, minutes) and test \(J_{25}=J_{23}\) in
   \(A\). Equality is the first observed stabilization.
5. Do not launch a 12-hour D23-core Groebner as this test. The test
   *is* the elimination onto CORE2, which is a smaller object than
   the hybrid 87-variable core.

### Kill criterion

Kill *this ambient* if \(J_D=(0)\) in \(A\) for every even \(D\) while
random D21 points keep dying at \(D+2\). The conditions then live in
the fibers, not in the CORE2 base. Repair once: enlarge \(A\) by a
finite set of fiber moduli (the 10 deep tails' elementary symmetric
functions, or the invariant ring of the merge block). Kill the
*strategy* if no finite-type ambient works — i.e. if each depth
introduces algebraically independent new tails over every finitely
generated subring of the inverse limit. Algkill's separate-extension
result is then in tension with that conclusion and should be re-read
before declaring the inverse system non-Noetherian. A stabilization
that leaves a positive-dimensional \(V(J_{D_*})\) is not a kill: it
is the actual germ locus, and the ladder has become a theorem about
that scheme.

---

## 5. Greenberg function: a finite depth decides the formal germ

**Gap:** the same D-∞ hole, at the level of jet schemes rather than
CORE2 coordinates.  
**Side:** proof. This is why a \(D_*\) exists even if idea 4 picked
the wrong chart.

### Five-line pitch

1. Residue-A has a finite coefficient rectangle
   \((\deg_x,\deg_y)=(42,126)\) and \((63,189)\). The space of such
   pairs is an affine space \(X\) of finite type. The window \(V_D\)
   is a locally closed subset of a jet scheme of \(X\) (B-frozen,
   no-log, \(W\ne 0\) are algebraic conditions of bounded degree).
2. Greenberg's theorem: for a scheme of finite type over a field,
   there is a function \(\gamma\) such that a jet of order \(n\)
   lifts to a formal (equivalently, by Artin, algebraic) point if and
   only if it lifts to order \(\gamma(n)\). The images
   \(\pi_{m}(V_\infty)\subseteq V_m\) stabilize in the constructible
   topology.
3. Therefore there exists a finite \(D_*\) such that
   \(V_{D_*}=\emptyset\) if and only if \(V_\infty=\emptyset\). The
   depth grind is a computation of \(\gamma\), not an open-ended
   search.
4. The last day already computes the first Greenberg number from
   below: \(\operatorname{im}(V_{23}\to V_{21})\ne V_{21}\) on a
   13-dimensional nonempty base (samples; idea 4 upgrades this to a
   variety statement if \(J_{23}\ne(0)\)). The next number is
   whether \(\operatorname{im}(V_{25}\to V_{21})\) equals
   \(\operatorname{im}(V_{23}\to V_{21})\).
5. Algkill is supporting evidence, not a rival: every *separate* D23
   prefix algebraizes in the rectangle, which is exactly the
   statement that \(X\) is the right finite-type ambient. Joint
   compatibility is the jet-scheme image, which is what Greenberg
   controls.

### Nearest neighbor, and why this is not it

Not Mittag-Leffler of the primitive. Not Artin approximation used as a
slogan to “algebraize a D21 point” (the campaign already knows a D21
point is a germ, not a polynomial). Not Hermite–Padé, which asks
whether a *single* series satisfies a polynomial relation of bounded
degree and was killed at this depth. Not idea 4: that is Noetherianity
in one concrete ring; this is why some finite-type ring's jet scheme
is the correct object, and why a \(D_*\) exists in advance of computing
it. Formal GAGA / Grothendieck existence along a divisor is a cousin
and is not proposed separately: Greenberg is the jet-scheme form that
matches the window.

### First concrete test

1. From the D21 CORE2 fiber and the D23-core, compute the constructible
   image \(\operatorname{im}(V_{23}\to V_{21})\) as the elimination
   ideal of idea 4 (same computation, different reading: this *is*
   \(\pi_{21}(V_{23})\)).
2. Emit D25 only as the already-sanctioned shape census. Compute
   \(\operatorname{im}(V_{25}\to V_{21})\) the same way. Compare
   radicals, dimensions, and the three-prime support of the
   elimination ideals.
3. Record the first two Greenberg numbers empirically:
   \(n\mapsto\dim\operatorname{im}(V_{n+2}\to V_n)\) at \(n=21,23\).
   A drop that then holds is the first observed stabilization of
   images, which is stronger than stabilization of a single \(J_D\).
4. Control: the ctl0 (origin / constant-block-dropped) window must
   have \(\gamma\equiv\mathrm{id}\) — every jet lifts, because the
   origin is a genuine polynomial point. If ctl0's image shrinks, the
   elimination is buggy.
5. No 12-hour solve of D25. The test is two eliminations and a
   comparison of constructible sets.

### Kill criterion

Kill if the defining equations of \(V_D\) cannot be realized as jets
of a fixed finite-type scheme: degrees or numbers of independent new
conditions grow in a way no jet scheme of the residue-A rectangle (or
of any scheme of bounded embedding dimension built from it) can
produce. Algkill plus the finite genome make that failure unlikely;
if it happens, the window is not a jet scheme and Greenberg does not
apply. Kill if ctl0's image shrinks. An image that keeps dropping at
every even depth through, say, D41 does not kill Greenberg — it says
\(\gamma\) is large — but it does kill Greenberg as a *cheap*
replacement for the grind, and the idea should then be parked behind
idea 4's concrete chain. Do not call “\(V_{21}\) nonempty and
\(V_{23}\) samples empty” a Greenberg theorem; that is one value of
one image.

---

## 6. The deleted-centers pencil is Du Val: \(\Delta^2\ge-2\) by ADE

**Gap:** G5 — no upper bound on \(td\). TDBOUND's empirical
\(td\le mn\) is coincidence-risk; its *real* content is the lemma
\(\sum a_F b_F/\nu_F\le 1\), equivalently \(\Delta^2\ge-2\) after
deleting Cor. 7.4 proportional centers.  
**Side:** proof. A classification, not a scan.

### Five-line pitch

1. Hodge index on the Sigray surface gives \(\Delta^2\le 0\) for a
   class orthogonal to the hyperplane. TDBOUND needs a *lower* bound.
   Lower bounds on self-intersection of effective classes on rational
   surfaces come from the ADE / Du Val list, not from Hodge.
2. Cor. 7.4's proportional centers are the components along which
   \(P\) and \(Q\) are powers of a common form. Delete them. The
   residual pencil \(\lvert C_f-\lambda C_g\rvert\) should have only
   rational double points: the residual singularities are the teeth
   that ideas 1–2 already named, and those are of type \(A_{q_h-1}\)
   (a power \(R^{q}\) is an \(A_{q-1}\) after the toric blowup).
3. On a Du Val configuration, every class supported on the residual
   tree has \(\Delta^2\ge-2\). That is the missing lemma, and it uses
   \(J=1\) exactly once: to guarantee that the centers being deleted
   really are proportional (the Jacobian forces the two leading forms
   on a certified edge to be powers of a common \(R\)).
4. Combined with Żoładek \(td\ge 6\) and the finite GGV \((m,n)\)-list,
   the sheet ladder is finite. The coincidence-risk in the 23-row
   table becomes a theorem about residual singularities, and the one
   below-bound kill (td-12 type \((3,5)\)) is no longer a counterexample
   to the *lemma* — it is a configuration whose residual pencil is
   *not* Du Val, or whose centers were not Cor. 7.4.
5. This is independent of books, of GGV6 masses, and of
   \(\operatorname{Pic}\) torsion of the graph.

### Nearest neighbor, and why this is not it

Yesterday's #1 is a computational \(\Phi\) table on `case_rows(150)`;
that table is now `TDBOUND.md` and has been evidence-downgraded.
Yesterday's #6 is the class group of \(\overline X\subset\mathbf P^2\times\mathbf P^2\),
a torsion argument. `SHEET6-CLASSICAL.md` T1 is splice positivity on
the *template* after sheet data are chosen; T3 is log-BMY, an upper
bound. Sol's TDBOUND review already *names* \(\Delta^2\ge-2\); it does
not identify it with the ADE list or propose the deleted-centers
pencil as a Du Val configuration. Bounded negativity on rational
surfaces is the ambient conjecture; this idea does not need it,
because Du Val is a classification, not a conjecture.

### First concrete test

1. On residue-A, take the splice diagram already computed in
   `SHEET6-CLASSICAL.md` §1. Delete the two polar centers
   (\(\Lambda=(3,3)\)). Write the residual intersection matrix.
   Ask two exact questions: is it negative-definite of ADE type? What
   is \(\Delta^2\) for the normalized difference of the two residual
   fibers? The equality case \(td=mn=6\) must return \(\Delta^2\in\{0,-2\}\)
   and an ADE (or empty) residual.
2. The same computation on \((x,y+x^2)\) and on \((x+y^2,y)\): after
   deleting whatever Cor. 7.4 centers they have, \(\Delta^2\ge-2\) and
   the residual is ADE or empty. This is the td=1 calibration.
3. One formal negative: the unique td-7 off-axis entry
   \((2,3)\), masses \((3,4)\), \(M=(1,2)\). If TDBOUND's lemma is why
   this configuration is illegal, its residual pencil (from the
   filed tree, not from a polynomial realization) must either fail
   to be Du Val or give \(\Delta^2\le-3\). A residual that is ADE
   with \(\Delta^2\ge-2\) means the lemma does *not* kill td-7, and
   the book kill remains the actual reason — which is allowed, but
   then this idea does not explain the books.
4. The td-12 type-\((3,5)\) entry (the one below-bound row, now dead
   at honest tier) is the discriminator: if it is ADE with
   \(\Delta^2\ge-2\), the lemma is compatible with a book kill of a
   below-bound configuration, and the *frontier* form \(td=mn\) dies
   while the inequality \(td\le mn\) can live. Record that honestly.
5. No Groebner, no new census. The input is splice / intersection
   matrices the campaign already knows how to write.

### Kill criterion

Kill if the residue-A residual, after deleting the two poles, is not
ADE and has \(\Delta^2\le-3\): then the one realized equality case
already violates the lemma, and G5 has lost its candidate. Kill if
either automorphism control has \(\Delta^2\le-3\) in this
normalization. Kill if the ADE type depends on the compactification
(ordinary closure vs Sigray vs toric hull) by more than the
exceptional \((-1)\)-curves created by further blowups — Du Val is
stable under that, and a failure of stability means the object is
not the residual pencil. Do not recycle a positive splice
determinant as an ADE success: positivity of edge determinants is T1,
already passed. Do not treat “the 23-row table still holds” as
evidence; that table is the coincidence-risk.

---

## What I am deliberately not proposing

- Another D23-core or D25-core Groebner as the *strategy*. The D23
  core is an input to ideas 4 and 5, not the idea.
- Anything from yesterday's six: \(\mathrm{SL}_2\)-push, GGV6 masses,
  \(T=1/\nu\) compactification, Kummer covers, graph-Pic, the \(\Phi\)
  table. TDBOUND *is* that table, and it has been downgraded.
- Sol's paired Newton-cut functor, symbolic off-axis grammar,
  primitive-monodromy bound, contextual live-kernel, first-disagreement
  rigidity. Idea 1 is the thin (no-jet) special case of the first of
  those; if it dies, Sol's jet functor is the repair, not a repeat.
- Mittag-Leffler of the Keller primitive, Fitting kernels,
  Hermite–Padé, NF-Z/P/M, high-tail gauge as a pin, forbidden minors
  of already-dead routes, Favre–Jonsson dynamics.
- “Enumerate off-axis by deleting the `continue`.” Still how P5's
  2691 `OPEN`s were born.
- A new TDBOUND scan, a new td-8/10/14 book, or a char-0 lift of a
  random D21 point.

---

## Suggested order of death

```
idea 4  D23-core ↷ CORE2          →  J_23 = (1)?     yes: window-tier kill
                                     J_23 proper?    chain moved; test J_25
                                     J_23 = (0)?     wrong ambient; enlarge once
idea 1  four gate-B + 2 autos     →  finite comb menu, autos inside?
                                     yes: Conjecture T has a list
idea 2  same four fans            →  pole bits match idea 1 + residue-A shadow?
                                     yes: the dual dictionary
idea 5  im(V_25→V_21) vs im(V_23) →  images equal?   first Greenberg number
idea 3  td-7 fat-record table     →  death hereditary in registers?
                                     yes: G4 is a finite antichain
idea 6  residue-A residual matrix →  ADE and Δ² ∈ {0,-2}?
                                     yes: G5 is classification, not a scan
```

Ideas 1 and 2 share one sitting with `lib/families.py` and the
`TRANSPORT.md` rotations. Ideas 4 and 5 share the D23-core files and
one elimination; 5 needs a D25 shape census only if 4's chain moved
and did not die. Idea 3 is a table on filed td-7 records. Idea 6 is
a lattice computation on a splice diagram that already exists.

A successful #4 is the residue-A decision the last day is grinding
toward, except it is a theorem about an inverse system rather than a
hope that D25 is emptier than D23. A successful #1 is the G2 remainder
the transport theorem explicitly left open, except the landing is in a
finite predicted comb menu, not in a search. That is the point of
generating from the remainders instead of from the existing engines.
