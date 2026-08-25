# JC2 blind full-spectrum ideation — round `20260824T2024Z` — Claude (Fable) lane

Cutoff honored: `2026-08-24T20:24:00Z`. Basis: clean charged commit
`2e6104a417cfe15a93a901aa0a9129094a2ae11b` plus the untracked frozen
`20260824` max12/AS/TD6 case and report artifacts named by the packet.
Blind contract: this report was written without reading any other
`ideation-20260824T2024Z-*` submission (a filename-only grep hit on the Grok
lane file was not opened). No canonical, producer, reviewer, case, packet,
run, log, prompt, or source file was edited. No web or shell tools were used;
consequently the packet's SHA-256 lines could not be independently recomputed
in this lane — I verified existence, internal consistency, and content
agreement of every named accessible input instead, and I flag hash replay as
coordinator-side work already done per the review documents.

Inputs read in full or in relevant part: the packet; `APPROACHES.md` (all 46
rows + all overlays); `AUDIT.md` (headings complete; all 2026-08-24 entries
in full); `PROGRESS.md`; `notes.md` newest `LIVE STATE` (19:32Z, plus 18:28Z
and 19:08Z); `COORDINATION.md`; `ladder/REDUCTION.md` (complete);
`xmodel/max12-912-order3-nu-belyi-collision-boundary-review-grok-20260824.md`
(verdict CONFIRMED, scope and successor list as packeted);
`xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md` (§§1–4;
algebra matches the packet's `v`, `x5`, `R(v)` displays up to sign
normalization); `xmodel/as-fonly-d7-postd10-d98-f3-erratum-20260824.md`
(exact `[K_Frob/3]` witnesses `2x^7+2x^8`);
`xmodel/as-fonly-d7-degree10-pointwise-review-grok-20260824.md` (CONFIRMED);
`cases/td6_c1_quadratic_stratum_20260824/replay.stdout` (ranks `3470/3602`,
`38/132`, `t12` unit PASS). File-presence check: the parity genus-5 hostile
review has a prompt but no completed review artifact — consistent with the
packet's "not yet frozen or reviewed".

---

## 1. Evidence discipline — what is reviewed vs provisional at cutoff

**Reviewed/promoted (safe to build on):** maximum-actual-partial-`y`-degree
≤ 11 automorphism theorem; max-12 frontier = exactly `(8,12)` and `(9,12)`;
universal Faber high-row landing with exact route widths; Kummer preflight
(orders `4,2,1` / `3,1`; every nontrivial Kummer class forces `delta=0` on
the monic-core divisor class, including the `(8,12)` order-2 leaf); the
`(9,12)` order-3 `k=mu=nu=0` DZ20 exclusion; **the new full-absorption
exclusion** (both passports `(18,2,2,1^14)`, `(18,3,1^15)` on the order-3
`k=mu=0, nu!=0` landing); the Keller coprimality/squarefreeness firewall; AS
D7 triangular terminal point, balanced cyclotomic terminal family, associated
top components, divided-carry erratum (corrected residual `L/3+K+C_x+D_y`,
40/30/dim-18 nonradical ideal), **D10 pointwise gate** (vertical component +
two endpoint supports); TD6 q2-pencil emptiness, centering full-cokernel
tangent (sensitivity at a nonsolution only); Pinchuk audit (Thm 4.1 local
identity only; Thm 3.4 GAP); Makar-Limanov intake (conditional own-frame
restrictions, no typed bridge).

**Provisional (use only behind the speculative gate):** the parity genus-5
descent (producer-exact, boundary checks and hostile review open); the TD6
licensed-`c1`-line closure (generic open + `C=3` + `J=4C^2+20C+1` stratum;
freeze/review open); generic-`c1`-pivot-open emptiness via nine
compatibilities; the corrected AS literal-F3 censuses (`314127/1594323`
vertical, `918/354294` g-endpoint, 12+360 empty structural bases — explicitly
unlicensed until source audit); AS D9 vertical global section and D8 rank
loci surviving the erratum.

**Retracted this delta:** the post-D10 D9/D8 `50939` and `954` censuses
(omitted `[K_Frob/3]` single-cross). The retraction is process-positive: the
fail-closed integer-quotient rule caught it.

---

## 2. Reranked principal bottlenecks

Proof side, nearest-first:

1. **P1 — the residual `(9,12)` order-3 `nu!=0` strata.** After full
   absorption (reviewed) and parity (provisional), what remains is exactly
   the reviewer's successor list: (i) no `B`-root in `W`, (ii) one simple
   `B`-root in `W`, (iii) double `B`-root off `W` (`3*nu*p+10*r8=0`),
   (iv) equal non-1 critical values — all genuinely four-or-five-branch-point
   families, outside fixed-passport Hurwitz finiteness. Card 1 gives the
   mechanism. Then the order-1 core (width 17) and both Taylor boundaries.
2. **P2 — TD6: one licensed line → a family/neighborhood obstruction.** The
   parameter-free unit `t12=-k/50` is the transverse invariant; its
   source-ideal lift decides whether the obstruction is moduli-uniform
   (answer to packet Q3 below).
3. **P3 — the standing global walls (unchanged, above everything for actual
   JC2):** `G2-PSC` transport, full landing/coverage, absolute/cofinal td
   ceiling (`ladder/REDUCTION.md` CRITICAL 3–7). No delta this round touches
   them; Card 2 offers a genuinely new cheap probe into the coverage wall
   from the partial-`y` side.
4. **P4 — `(8,12)`:** untouched lower fibres; the reviewed order-2 quadratic
   leaf has `delta=0`, so the same Faber/terminal engine will apply.

Disproof side, nearest-first:

1. **D1 — the AS D8 vertical divided-carry row** (first potentially decisive
   vertical gate; Card 3).
2. **D2 — licensing of the corrected literal-F3 censuses** (source audit in
   flight; nothing downstream until it lands).
3. **D3 — TD6 SP-2 in the unfixed moduli** (center family beyond the `c1`
   line; a *failure* of `-k/50` moduli-uniformity would be a live family
   lead — falsification value both ways).
4. **D4 — AS109 coupled-section grammar**, with a ledger correction: the
   reviewed max-11 theorem raises the AS109 correction `y`-degree floor from
   the banked "at least nine" to **at least twelve** (any exact lift is a
   characteristic-zero Keller pair). Cheap ledger update, not new math.

---

## 3. Direct answers to packet questions 1–4

**Q1 (generalize the genus-5 cube descent).** Yes, and the right general
form is *Kummer-invariant moduli descent + hyperbolicity/genus certificate +
the already-reviewed isotriviality kill*. The parity proof secretly has three
parts: (a) a weight-zero coordinate (`v=A/(p*x5)`) that Galois-descends to
`C(x)`; (b) reversible elimination onto an explicit receiver curve
(`Y^3=quintic/(3v^2-2)`, genus 5); (c) nonconstant `P^1 -> genus>=1`
impossible, constant case killed by the terminal row. Part (c) is the same
engine as the confirmed full-absorption scaling kill
(`[z^18]W=-3*nu` forces `lambda` constant, then `r8'=0` contradiction). The
exact invariant coordinates for the *whole* loaded fibre are the weight-zero
quotients `sigma0=(3*nu*p+10*r8)/p` (the normalized `B`-discriminant; note
`wt(p)=wt(r8)=2`) and the symmetric functions `e1=c1+c2`, `e2=c1*c2` of the
two extra branch values `c_i=beta(±z0)` at the `B`-roots — `B` is even, its
roots swap under both `z -> -z` and the order-3 covariance `sigma(z)=zeta*z`,
so `e1,e2` descend to `C(x)` (descent to be verified as the card's first
dependency, not asserted). Cheapest discriminator per stratum: the exact
genus (and gonality) of the receiver curve from reversible elimination; where
elimination does not collapse, the genus of the fixed-passport four-point
Hurwitz curve versus the explicit genus of the base curve
`u^3=h` (a nonconstant map cannot raise genus). Details and staging in
Card 1.

**Q2 (smallest exhaustive stratification).** Stratify by three *resultant/
discriminant* conditions, never primary decomposition: `R1=Res_z(B,W)`,
`D=disc_z(B)=-1296*nu*(3*nu*p+10*r8)`, and `S=(c1-c2)^2` (a rational
expression in `sigma0` and fibre coefficients). The complete case tree on
(`#{B-roots in W}` ∈ {0,1,2}) × (`D=0`?) × (`S=0`?) has exactly five leaves:
full absorption (both roots in `W` — closed, reviewed); one-collision
(`R1=0`, one root); double-root-off-`W` (`D=0`, `W(0)!=0`; note `B` even
forces the double root at `z=0`, and this is literally the banked "first
collision boundary" `3*p+10*r8=0` at `nu=1`); equal-values (`S=0`, `D!=0`,
`R1!=0`); generic no-collision. Exhaustiveness is by construction of the case
tree; every condition is polynomial in the loaded coefficients, so both
Taylor-jet boundary families are preserved (intersect the same conditions
with the frozen boundary jets). The firewall already excludes `B`-roots on
`f*g=0`, so `c_i` are finite and nonzero generically — the degenerations sit
inside the strata, not outside the tree. Parity is *not* needed for
exhaustiveness: it is a sublocus of the equal-values leaf (on the parity
slice `f` odd/`g` even makes `beta` even, so `c1=c2` automatically) — see the
imprimitivity remark in §4. Four-point Hurwitz geometry and Kummer character
descent are exactly the tools that avoid primary decomposition; equal-
critical-value loci enter as the `S=0` leaf, not as an extra mechanism.

**Q3 (TD6: one line → neighborhood).** The finite cover that most cheaply
upgrades the licensed `c1` line is the *pivot-denominator atlas*: the staged
elimination's identity `D(C)*P12=D(C)*(-k/50)+sum M_i L_i` holds wherever its
pivots are units; the pivot denominators are banked polynomials in `(C,`
remaining moduli`)`; the exceptional set is their finite vanishing
stratification, and the cover is complete iff every leaf either inherits the
generic Bezout identity or carries a raw producer-exact rebuild (exactly what
`C=3` and the `J`-stratum already did). Completeness is then a *certificate
by construction* — the leaf list equals the factor list of the banked
denominators, fail-closed if any leaf is unrebuilt. The transverse invariant
that converts the line into a family obstruction is the parameter-free unit
`t12 ≡ -k/50`: if the active source-ideal lift proves it identically in the
remaining center/boundary/dead-stretch/F1/pole moduli on the valid chart,
the whole chart-validity neighborhood dies at the current band; if it fails,
the failure locus is a live family lead (D3). Either outcome is decisive;
prioritize the lift over further single lines.

**Q4 (AS: survivors → honest recursion or falsifiable candidate).** Convert
counts into *scheme + section + control* form. (a) Keep the nonreduced ideal
(the embedded component is load-bearing, per the reviewed top-components
result); accepted-digit recursion must be run against the corrected residual
with **all** divided carries generated systematically (see the avenue-12
reopen in §4: generate the carry algebra from Witt/carry polynomial calculus
rather than hand enumeration — the `[K_Frob/3]` omission was a hand-
enumeration failure). (b) Mandatory per-depth negative controls: the
balanced cyclotomic family (must survive to exactly depth `2m`, die at
`2m+1`, `m=3,5`) and the D7 triangular point (die at cap seven) — an
old-pass/new-fail battery satisfying the COORDINATION review rule. (c) The
falsifiable all-depth algebraization candidate is the explicit generating
function of the vertical-branch digit sections: the D9 row has a global
polynomial section; conjecture the closed form of the section tower and test
it at D8, where the divided integer carry first enters. Card 3.

---

## 4. Genuinely new mechanism and new cross-avenue connections

**New mechanism — base-genus/gonality isotriviality certificate with
imprimitivity stratification** (history-checked: no prior campaign use of
gonality, braid orbits, cross-ratio descent, or isomonodromy language;
`Ritt` exists only as untried avenue 43; "four-point Hurwitz geometry" is
named as a question in this packet but no mechanism exists in the ledgers).
Two parts:

- *Moduli-map constancy by curve theory.* Each residual stratum's cover
  family `beta=g^3/f^4` is a point of a fixed-passport four-point (or
  five-point) Hurwitz space `H` over a base curve of explicitly bounded
  genus: the branch data are defined over `L'=L(z0)` with `[L':C(x)] <= 6`
  (`u^3=h` times the quadratic splitting of `B`), and `g(X')` is computable
  from `h` and `sigma0`. A nonconstant classifying map `X' -> H̄` forces
  `g(H̄) <= g(X')`; so whenever the braid-orbit Hurwitz curve has larger
  genus (SPECULATIVE until computed; degree-36 four-point spaces are
  typically high-genus), the family is isotrivial and the reviewed scaling +
  terminal-row engine kills it. This is the parity argument with the ad-hoc
  receiver replaced by the intrinsic one, and it is exactly what fixed-
  passport finiteness degenerates to when a branch point moves.
- *Imprimitivity (Ritt) stratification.* The parity slice is precisely the
  locus where the degree-36 cover decomposes through `z -> z^2`
  (`f` odd, `g` even ⇒ `beta` even ⇒ `beta=b1(z^2)`, `deg b1=18`). So
  "parity" is not an accident of coordinates: it is the first *Ritt/
  imprimitivity locus* of `beta`. Systematically: enumerate block systems of
  degree-36 monodromy compatible with the passports (blocks of size
  2,3,4,6,...); each imprimitivity pattern is a constructible coefficient
  locus (a generalized parity slice) on which `beta` factors and the
  passports contract to degree ≤ 18 — strictly cheaper genus computations;
  the primitive complement can be attacked through the degree-36 primitive-
  groups database (a permutation containing an 18-cycle with many fixed
  points is very restrictive; if only `A_36/S_36` survive, Hurwitz spaces
  are large and the genus certificate is favorable; if a small rigid group
  survives, rigidity itself gives finiteness — either branch helps;
  SPECULATIVE which occurs).

**New cross-avenue connection 1 — the partial-`y` ladder × the Sigray
books (avenue 2).** History-checked: nothing in the ledgers feeds the
brand-new max-11 theorem back into the sheet frame. Every Aut×Aut
representative of a counterexample is a counterexample, so the reviewed
max-11 theorem says: *every Sigray-normalized counterexample has rectangle
data `l_g = m*beta >= 12`* (the normal form has `deg_y f = l_f < l_g` with
`(l_f,l_g)=m*(alpha,beta)`). This is a new, unconditional decoration cut on
every book: type `(2,3)` forces `m>=4`, `(3,4)` forces `m>=3`, `(2,5)` and
`(3,5)` force `m>=3`, `(5,6)` forces `m>=2`. Striking checksum: the max-12
frontier cells are exactly the smallest Sigray-compatible frames beyond the
theorem — `(8,12) = m=4` of type `(2,3)` (residue-A's type!) and
`(9,12) = m=3` of type `(3,4)`. The two ladders meet at the frontier. Card 2
develops the cheap gates and the honest limits (whether book cells pin `m`
at all is the first question, not assumed).

**New cross-avenue connection 2 — avenue 12 (p-adic carry calculus) as the
AS carry generator.** The `[K_Frob/3]` omission is a Kummer/Witt carry-
bookkeeping failure. Wilson-style carry analysis (avenue 12, "analyzed, not
executed") has a real, bounded instrument role here: derive the complete
divided-carry algebra of `det J - 1` at `p=3` per depth from carry
polynomials, so the compiler's residual is generated, not hand-assembled.
Instrument-tier reopen only; no proof claim.

**Secondary software connection.** The exact Bezout/unit-certificate engine
from the TD6 `E[B]` pencil kill is the right tool to certify the AS "empty
structural bases" (rank statements → unit certificates), replacing count
assertions with replayable certificates.

---

## 5. Strongest attacks

**Strongest proof attack (near-term theorem density):** finish the `(9,12)`
order-3 `nu!=0` fibre by the five-leaf stratification of Q2 + Card 1's
mechanism, in order: double-root leaf (cheapest, codim 1, elimination-only),
one-collision leaf, equal-values leaf, generic leaf (Hurwitz/gonality
backstop), then the order-1 polynomial-cube core with the same terminal
engine, then Taylor boundaries. Each closed leaf is a reviewable theorem of
the same shape as the two already confirmed. JC2-scale honesty: this closes
cells of a partial-degree ladder, not JC2; the JC2-scale proof surface
remains TD6/coverage (P2/P3), where the `-k/50` uniformity lift is the
single highest-value step.

**Strongest counterexample/falsification attack:** the AS D8 vertical
divided-carry gate (Card 3) — it is the first row where the divided integer
carry genuinely enters, the vertical component is the only surviving
positive-dimensional AS object with a universal section above it, and both
outcomes are decisive (vertical death collapses the map-only D-series
disproof lane to endpoint rays; survival with a section upgrades the
algebraization candidate to a falsifiable closed form). Secondary: the TD6
`-k/50` uniformity test doubles as a falsification probe — a nonuniform
locus is a live family lead.

---

## 6. Software accelerator / decisive experiment

**Accelerator — the stratum→curve compiler.** Generalize the parity scripts
(`generate_parity_slice/resultants/projection.py`,
`generate_weighted_projection.py`) into one exact tool: input a constructible
stratum of the loaded fibre (list of resultant/discriminant conditions),
output (a) the weight-zero invariant coordinates, (b) the reversible-
elimination receiver curve over `Q`, (c) its exact genus (and gonality bound
when superelliptic), (d) the isotriviality endgame report (which scaling/
terminal identity applies). Reusable verbatim for the `(8,12)` order-4 and
order-2 fibres later; no AWS, one local core, exact arithmetic only.

**Decisive experiment (first run of the compiler):** the double-root leaf
`3*nu*p+10*r8=0`. One equation, `z=0` critical of index 3, extra branch value
`c=g(0)^3/f(0)^4` with `c` in `C(x)*` and `c != 0,1,infty` by the firewall
and the closed absorbed stratum. Expected: parity-style collapse to an
explicit receiver; outcomes in Card 1.

---

## 7. Idea cards (exactly three)

### Card 1 — Close the residual `(9,12)` order-3 `nu!=0` strata by invariant-coordinate descent (label: mechanism NEW; stratification skeleton KNOWN — it is the confirmed review's successor list)

- **Target obstruction:** P1 — the four leftover collision strata.
- **Mechanism:** Q2's five-leaf resultant stratification; per leaf, Q1's
  invariant coordinates (`sigma0`, `e1`, `e2`, `v`-analogues) + reversible
  elimination onto an explicit receiver curve; kill nonconstant families by
  genus (receiver or Hurwitz curve vs base `g(X')`, base degree ≤ 6 over
  `C(x)`); kill constant families by the reviewed scaling identity
  `[z^18]W=-3*nu` + terminal row `9*r8'=j/u`. Imprimitivity slices
  (generalized parity) as accelerators where present.
- **Dependencies:** reviewed Faber landing, Kummer preflight, full-absorption
  review (all promoted); coprimality firewall (promoted); Kummer descent of
  `e1,e2` to `C(x)` (first internal check, half a page); parity mechanism as
  template only (provisional but not consumed).
- **Cheapest discriminator:** the double-root leaf (§6). Second: one-collision
  leaf with `Res_z(B,W)=0` imposed.
- **Outcome interpretation:** receiver genus ≥ 1 with the constant case
  contradicted → leaf closed (freeze + hostile review, same shape as full
  absorption). Genus 0 receiver with rational points and no divisor
  obstruction → the leaf owns an explicit candidate family: switch the lane
  to *construction* mode (falsification value: an actual surviving
  nonisotrivial family is the first live max-12 counterexample lead).
  Elimination non-collapse (ideal too big) → hand the leaf to the Hurwitz/
  primitive-group backstop; if the degree-36 braid-orbit computation exceeds
  one core-week after block reduction, stop that leaf and report
  `HEAVY`.
- **Stop condition:** two consecutive leaves landing in `HEAVY` without a
  kill or a candidate → stop the descent variant, keep the stratification as
  the fibre's canonical case tree, and reassess at the next full round.
- **Expected information gain:** high in every branch — each leaf is either
  a new reviewable exclusion, an explicit candidate family, or a certified
  hardness datum that reroutes the `(9,12)` allocation to `(8,12)`.

### Card 2 — Partial-`y`/sheet-ladder crosswalk: `l_g >= 12` as a new book decoration (label: NEW connection)

- **Target obstruction:** P3's coverage wall, probed from a new side; plus
  cheap kills inside existing td-6..8 objects.
- **Mechanism:** the reviewed max-11 theorem forces every Sigray-normalized
  counterexample to have `l_g=m*beta>=12`. Two gates: (G1) for each of the
  eight td-6 terminal classes and the 23 modeled on-axis survivor cells,
  determine from the banked ladder files whether the class pins or bounds
  `m` (equivalently `l_g`); any cell forcing `l_g<=11` dies instantly at the
  theorem's tier. (G2) the frontier checksum: `(8,12)` is `m=4` of type
  `(2,3)`, `(9,12)` is `m=3` of type `(3,4)`; enumerate which `(td, entry)`
  menus from T7's arithmetic are consistent with these rectangles, and
  check the hypothetical pairs against the *closed* panels (td ≤ 5
  unconditional; td-7 filed-perimeter tier; td-11 conditional tier) —
  carefully labeled at those conditional tiers, never above.
- **Dependencies:** max-11 theorem (promoted); Sigray T4 rectangle normal
  form (conditional-on-thesis tier — inherited, stated); T7 entry arithmetic
  (conditional tier); no provisional input.
- **Cheapest discriminator:** G1 on the eight td-6 terminal classes — a
  reading-plus-arithmetic afternoon, no compute.
- **Outcome interpretation:** if books pin `m`: immediate new kills or
  immediate proof that all surviving cells sit at `l_g>=12` (sharpening
  where a counterexample can hide, and giving the books a brand-new cut
  dimension for free). If books do not pin `m`: promoted conclusion is
  "rectangle scale `m` is an independent decoration the books must carry" —
  a concrete, bounded addition to the REDUCTION.md repair list (5.1), and
  the crosswalk becomes a specification for the future typed landing map.
  If G2 finds a td-menu inconsistency for `(9,12)`-shaped pairs at closed
  panels: a conditional-tier exclusion transporting sheet work onto the
  max-12 frontier — the first two-ladder theorem.
- **Stop condition:** if G1 shows the ladder files contain no relation
  between entry data and `(k,l)` rectangles at all, write the negative
  result and stop; do not build the bridge speculatively.
- **Expected information gain:** medium-high at near-zero cost; every
  outcome produces a durable ledger fact; upside is a new class of kills on
  both ladders.

### Card 3 — Fail-closed AS D8 divided-carry vertical gate with terminal-family controls (label: target KNOWN/active; control-and-generator discipline NEW)

- **Target obstruction:** D1 — the first potentially decisive vertical row.
- **Mechanism:** build the D8 gate from the corrected residual
  `L/3+K+C_x+D_y` with the complete divided-carry algebra *generated* by
  carry-polynomial calculus (avenue-12 instrument; every cross term of the
  form `[K_Frob/3]` and below produced systematically, none hand-listed),
  on the nonreduced predecessor scheme (embedded component retained).
  Mandatory regression battery before any census is banked: (i) balanced
  cyclotomic family at `m=3,5` must survive to exactly depth `2m` and die
  at `2m+1`; (ii) the D7 triangular point must die at cap seven; (iii) the
  erratum's integer witnesses `2x^7+2x^8` and `2xy^6+2x^4y^5` must
  reproduce. Then decide the D8 vertical row: global section, partial
  section, or empty.
- **Dependencies:** D10 pointwise gate (promoted); divided-carry erratum
  (promoted); D9 global section (provisional — labeled, consumed only as a
  conjecture-shaping input, not as evidence); corrected F3 censuses (NOT
  consumed until the source audit licenses them).
- **Cheapest discriminator:** the regression battery itself — if the
  generated carry algebra disagrees with the hand-corrected 30-row residual
  anywhere, freeze and erratum first (fail closed).
- **Outcome interpretation:** D8 vertical empty → the vertical branch
  terminates; the map-only D-series disproof lane collapses to the two
  endpoint rays; reallocate AS capacity to the endpoint digits or wind the
  lane down. D8 vertical nonempty with a global section → freeze the
  explicit all-depth section generating-function conjecture as the
  campaign's first falsifiable AS algebraization candidate and hand it to
  hostile review. Nonempty without a section → honest recursion continues
  one digit with the same controls.
- **Stop condition:** any control failure stops the lane pending erratum;
  two consecutive depths with neither death nor section (pure survival
  without structure) → stop and demand a locus-level theorem before more
  depth, per the standing "pointwise is not locus" discipline.
- **Expected information gain:** high; this is the only currently active
  gate whose *both* outcomes move the disproof portfolio decisively.

---

## 8. Compact 46-avenue disposition

Default is `unchanged` — no delta this round touches the row, and the prior
synthesis stands. Every non-default entry has its reason inline.

| # | Avenue | Disposition |
|--:|---|---|
| 1 | GGV corner farm | unchanged |
| 2 | Sheet ladder / Sigray books | **raise** — the TD6 pivot-denominator atlas method (generic identity + raw rebuilds at `C=3`, `J`-stratum) is a repeatable family-closure instrument (provisional until review); Card 2 adds a new unconditional decoration cut (`l_g>=12`) |
| 3 | Vertex-gap / strip ODE | unchanged |
| 4 | Formal-germ / D-series + AS | unchanged — D10 confirmation and the D9/D8 retraction net out; carry discipline hardened; Card 3 is the next gate |
| 5 | JvdK descent | unchanged |
| 6 | Abhyankar–Moh | unchanged |
| 7 | Jelonek A(F) | unchanged |
| 8 | Formal-inverse combinatorics | unchanged |
| 9 | Conjecture E | unchanged |
| 10 | HC4 bridge | unchanged (stopped) |
| 11 | Mathieu/GMC ladder | unchanged (refuted) |
| 12 | Face isolation / p-adic multinomials | **reopen (instrument tier only)** — carry-polynomial calculus as the systematic generator of AS divided-carry algebras (§4); no proof role claimed |
| 13 | Dixmier DC(2) | unchanged |
| 14 | End(A_1) / Zheglov | unchanged |
| 15 | Commuting PDOs | unchanged |
| 16 | D-module / holonomic index | unchanged |
| 17 | BCW cubic stabilization | unchanged |
| 18 | Graded / GIT | unchanged (closed) |
| 19 | Char-p + Witt lifting | unchanged — active backbone; erratum handled inside it; AS109 `y`-floor ledger note (≥12) recorded in §2 |
| 20 | p-curvature formalism | unchanged |
| 21 | p-adic injectivity / Hensel | unchanged |
| 22 | Integral points / heights | unchanged |
| 23 | Analytic global inverse | unchanged |
| 24 | Real / Pinchuk maps | unchanged (the 2021 Pinchuk paper audit explicitly does not touch this row) |
| 25 | Monodromy / dessins / Hurwitz passports | **raise** — fixed-passport Hurwitz finiteness is now load-bearing inside a different-model-CONFIRMED exclusion (full absorption); the four-point/braid extension is the named successor mechanism (Card 1); the old "Riemann existence is too generous" objection is bypassed because passports are combined with isotriviality and the terminal ODE, not used alone |
| 26 | Primitive-monodromy td bound | **raise (narrow)** — the degree-36 primitive-group census is now a bounded concrete client (Card 1 backstop) instead of an unbounded global-td program; the global-bound version stays where it was |
| 27 | Links at infinity / splice | unchanged |
| 28 | Log surfaces / BMY | unchanged |
| 29 | LND / Hamiltonian | unchanged (scoped stop) |
| 30 | Affine classification / ML invariant | unchanged — ML/MLT intake stays conditional own-frame, no typed bridge |
| 31 | Integrality / ZMT | unchanged |
| 32 | Collision ideal / injectivity | unchanged |
| 33 | Symplectic action residues | unchanged (stopped) |
| 34 | Tangent-sweep / pole removal | unchanged |
| 35 | Dim-3 descent | unchanged |
| 36 | Guided CE search | unchanged |
| 37 | Finite-field census | unchanged |
| 38 | Tropical | unchanged |
| 39 | Cohomological cluster | unchanged |
| 40 | Free-associative lift | unchanged |
| 41 | Naive scaling deformation | unchanged (refuted) |
| 42 | Markus–Yamabe | unchanged |
| 43 | Ritt decomposition | **reopen (narrow)** — as the imprimitivity filter for the degree-36 spectral covers: parity is exactly the `z^2`-decomposition locus, and the remaining strata should be sliced by decomposition type before any heavy Hurwitz computation (Card 1); the original composite-coordinates program stays closed |
| 44 | Moskowicz prime-td | unchanged (closed as proof input) |
| 45 | Differential Galois / Liouvillian | unchanged |
| 46 | Lean / formal certification | unchanged — note only: the max-≤11 theorem stack is now the natural next formalization insurance target when capacity frees |

---

## 9. Continue / redesign / stop for every major active lane

- **Max-12 `(9,12)` loaded `nu=1` block elimination (owner lane):**
  **continue, with redesign of the target list** — adopt the five-leaf
  stratification and run the double-root leaf first (Card 1); do not open a
  generic coefficient rectangle (review's own successor discipline).
- **Parity genus-5 freeze + boundary audit + hostile review:** **continue**
  — highest review priority in the queue (high fanout: it is the template
  for Card 1); until confirmed, nothing consumes it.
- **AS corrected-rows integer-source comparison / F3 census licensing:**
  **continue** — hard gate before any census number is used anywhere.
- **AS D10 → D9/D8 successor (carry-aware compiler):** **continue, with
  redesign** — add the generated carry algebra + mandatory control battery
  (Card 3) before the D8 census is banked.
- **AS erratum hostile review:** **continue** (active, nonblocking).
- **TD6 combined `c1`-line portable freeze + hostile review:** **continue**.
- **TD6 `-k/50` source-ideal lift:** **continue and elevate** — it is the
  family-upgrade decision point (Q3); prefer it over further single-line
  rebuilds.
- **TD6 generic `c1/c3` dual + exceptional-fibre atlas:** **continue**
  (licensed stagewise route; the one-shot affine Smith shortcut stays
  stopped).
- **Broad web sweep #9 (due 21:25Z):** **continue** — add: Pakovich (and
  coauthors) on Davenport–Zannier pair deformations and rational-function
  decomposition; four-point-cover/braid-orbit and Hurwitz-curve genus
  literature; primitive permutation groups of degree 36; isotriviality/
  Zannier-style function-field specialization results; plus the standing
  competitor and old-but-new watches.
- **AWS expansion:** **stop (keep stopped)** — every current gate is
  symbolic/certificate-bound; nothing in this report needs fleet compute.
- **Local exact TD6 dual-core job:** **continue**.
- **Held/stopped set (D-series depth expansion beyond gates, B=168, raw
  passports, secant descendants, new book cells, primitive-group global
  census without support bound, etc.):** **keep stopped** — nothing here
  reopens them except the two narrow instrument-tier reopens (12, 43) scoped
  above.
- **Coordination v2 outer loop / ideation cadence:** **continue**.

---

## 10. Canonical history/priority checksum

Performed per COORDINATION step 6, within this lane's tool limits (no web):

- **Searched** `APPROACHES.md`, `AUDIT.md`, `PROGRESS.md`, newest
  `LIVE STATE`, `ladder/REDUCTION.md`, and `xmodel/`+`ladder/` reports for
  every surviving mechanism and close synonyms: gonality, braid, cross-ratio,
  isomonodromy, imprimitivity, `M_{0,4}`, Ritt (only the untried avenue-43
  row), four-point (only this packet's Q2 and the new producer/review
  bytes), and a partial-`y`↔book crosswalk (absent; `l_g` occurs only as
  Sigray rectangle notation). **Labels:** Card 1 mechanism NEW (its
  stratification skeleton KNOWN — it is the confirmed review's successor
  list; credit there); Card 2 NEW; Card 3 target KNOWN/active with NEW
  control/generator discipline; avenue-12 and avenue-43 reopens NEW at
  instrument tier.
- **Known-degree/closed-case ledger reconciliation:** first open sheet
  degree is six (Domrina; Żołądek ≤ 5); td-7 panel closed at filed-perimeter
  tier; td-11 conditional certificate; td-12 type-(3,5) book at its stated
  tier; `(72,108)` exclusion external-certificate-supported, conditional on
  the GGV-Horruitiner bridge; max actual partial-`y` ≤ 11 automorphism
  (reviewed theorem, this window); max-12 primitive cells exactly
  `(8,12)`,`(9,12)`; maximum-12 order-3 closures: DZ20 face (reviewed) +
  full absorption (reviewed) + parity (provisional). **Ledger correction to
  file:** the AS109 correction-`y`-degree floor should read ≥ 12 (max-11
  theorem), superseding the banked "at least nine".
- **Primary-text checks:** no new external literature claim is load-bearing
  in this report. The consumed external facts (Pinchuk Thm 4.1 scope,
  Pakovich–Zvonkin unitree scope, ML/MLT conditional frame, Chau, Żołądek,
  Domrina, Wright, Orevkov) are already primary-audited in the ledgers. The
  Hurwitz/braid/gonality literature proposed in Card 1 is flagged for sweep
  #9 intake *before* any braid-orbit computation is trusted.
- **Speculation register:** (i) receiver/Hurwitz-curve genus exceeding the
  base bound — SPECULATIVE until computed; (ii) small-group vs `A_36/S_36`
  monodromy dichotomy — SPECULATIVE; (iii) whether book cells pin the
  rectangle scale `m` — unknown, resolved by Card 2's first gate; (iv) the
  D9 section's closed form — conjecture-shaping only. No provisional fact
  (parity, `c1`-line, F3 censuses, D9 section) is consumed as evidence
  anywhere above.

No result in this report proves or disproves JC2; the strongest licensed
readings are exactly those stated in §1.
