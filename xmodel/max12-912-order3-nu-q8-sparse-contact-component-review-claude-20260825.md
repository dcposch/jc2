# Hostile review: selected-Q8 sparse contact forces a mod-127 component

Date: 2026-08-25
Reviewer: Claude (independent hostile algebraic-geometry referee; no producer role)
Status: **REVIEW COMPLETE**

## Verdict

**CONFIRMED WITH REPAIRS.**

The narrow claim under review — over `F_127` (geometrically, over its algebraic
closure), at least one relevant irreducible one-dimensional source-curve
component of the localized six-row divided approximate-cubic system has
cycle-theoretic projected image in the `(w,v)` plane equal to the geometrically
irreducible degree-190 curve `H` — follows from the frozen artifacts, **given
three repairs stated below**.  All three repairs are exposition-level: each is
provable from data already certified in the frozen runs, and none requires new
computation or changes any number.  I found no wrong mathematics.  The strict
inequality `704 > 658` is load-bearing exactly as designed, and the margin
structure is sharper than the producer text states (see Issue 4).

**Numerical count reviewed:** the self-contained erratum count

```text
80 order-8 fibres:   80*8 = 640
w=25 order-64 fibre:         64
total normalized contact:   704 > 658,   strict excess 46.
```

I did **not** rely on the superseded `123 + 63 + 68*7 = 662` count, which
appears in the immutable breadth report, the breadth FREEZE, the lemma's
equation (3), and `breadth_summary.json` (`contact_sum_first_68`,
`strict_component_inequality: "662>658"`).  Those artifacts remain
byte-immutable by design; the operative count is the erratum's.

## Files read

Producer reports (in full):

- `xmodel/max12-912-order3-nu-q8-sparse-contact-component-lemma-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-breadth-component-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-breadth-component-self-contained-erratum-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-full-contact-jacobian-aws-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-hensel-order64-aws-20260825.md`

Frozen cases (README, FREEZE, manifest, summary, plus load-bearing scripts and
frozen outputs):

- `cases/max12_912_order3_nu_q8_sparse_mixed_volume_aws_20260825/`
  (README, FREEZE, manifest.sha256, `mixed_volume.py` head, both
  `result.json` files: Box02 full replay, Box03 affine shard)
- `cases/max12_912_order3_nu_q8_p127_breadth_order8_aws_20260825/`
  (README, FREEZE, manifest presence, `breadth_summary.json` in full,
  `run_one.sh`, `generate_breadth.py` moving/final blocks, `summarize.py`,
  lane `w001` frozen `result.out` markers, lane `w083` custody file set)
- `cases/max12_912_order3_nu_q8_p127_hensel_order64_aws_20260825/`
  (README, `verify.py`, frozen `input.sing` identity blocks, frozen
  `result.out` markers) — read because the erratum's count is unprovable
  without this lane
- `cases/max12_912_order3_nu_q8_p127_component_self_contained_count_20260825/`
  (README, FREEZE, `replay.py`)

Not consulted: any later bidegree or high-order-contact successor, per the
review charter.

## Execution disclosure

This review session has no shell.  I did not recompute any SHA-256, did not
re-run Normaliz, Singular, `verify.py`, or `replay.py`, and performed no new
heavy computation.  Verdicts rest on (a) direct reads of the frozen bytes
named above, (b) citation-level cross-consistency of the pinned hashes, and
(c) hand algebra.  Hash *values* are therefore trusted as attested; hash
*cross-references* were checked by eye and are consistent everywhere I looked
(details at the end).

---

## Point-by-point findings

### 1. Full rank ⟹ unique reduced branch, `w-w_i` uniformizer, generically finite projection — SOUND

At each charged point `y_j` the certified unit 6×6 Jacobian in
`(c,d2,d4,x1,x3,x5)` (per-lane `gcd_detJ_H0_degree=0`, i.e. a unit at all 190
conjugate points simultaneously, with an explicit inverse-matrix witness
`checkK0` in the base block) gives, by the formal implicit function theorem —
which is Hensel's lemma for the complete local ring and is valid over any
field, with no separability input — a completed local ring
`F̄[[w-w_i]]` for the six-row scheme `W` at `y_j`.  Hence: exactly one
irreducible component of `W` through `y_j`; that component is reduced at
`y_j`; its dimension is 1; and `w-w_i` generates the maximal ideal, i.e. is a
uniformizer.  Since `w-w_i` maps to a nonzero element (`s`) of the branch,
`w` is nonconstant on the component `C`, so `pi(C)` is an irreducible curve,
not a point, and `C → pi(C)` is a dominant map of curves, hence generically
finite.  The chart function `v=(x3-2x5)/x5` is regular at `y_j` because the
localizer identity `inv*x5*(x3-2x5)=1` is certified at the base.  No gap.

A useful corollary the producer text does not draw (needed in Point 2):
`C → A^1_w` is **unramified** at `y_j` (ramification index 1), so the function
field extension `K(C)/F̄(w)` is separable — an inseparable finite map of
curves factors through Frobenius and has ramification index ≥ 127 at every
point.  Consequently the intermediate extension `K(C)/K(pi(C))` is separable.

### 2. Generic pulled-back line: isolated roots and the exact count — SOUND AFTER REPAIRS 1–2

The intended argument: pick a generic affine line `l: a*w+b*v+c=0`; its
division-free pullback `a*w*x5 + b*(x3-2x5) + c*x5` cuts each relevant
component `C` in exactly `deg(C→D_C) * deg(D̄_C)` distinct points (`D_C =
pi(C)`, `D̄_C` its projective closure), all isolated in the zero set of the
full seven-polynomial system; summing over relevant components gives
`deg(pi_* Z̄)`, the projective degree of the pushed-forward cycle.  This is
correct, but two steps are unproven as written:

- **Separability (Issue 1).** In characteristic 127, if `C → D_C` were
  inseparable, a generic fibre would have strictly fewer than `deg(C→D_C)`
  points and the count would undercount `deg(pi_*Z̄)`; inequality (1) of the
  lemma would not follow from the root count as stated.  The repair is the
  corollary in Point 1: the certified unramifiedness at a single charged
  point already forces `K(C)/F̄(w)`, hence `K(C)/K(D_C)`, separable, so
  generic fibres of `C → D_C` have exactly `deg(C→D_C)` reduced points.
  (Alternative repair: use the with-multiplicity form of the isolated-root
  bound together with `Σ_{q→p} e_q = deg(C→D_C)`, the fundamental identity,
  valid also for inseparable maps.)
- **The finite bad set (Issue 2).** The lemma lists the chart boundary, other
  components, collision values, and the points of `D̄_C` at infinity.  One
  further finite set must be avoided and is not named: images of the finitely
  many boundary points of the completed model of `C` itself (points of the
  closure of `C` in a projective compactification of the source that do not
  lie on the affine chart).  Over such an image point the affine fibre of `C`
  drops.  Same genericity mechanism, one more finite set; over the infinite
  field `F̄_127` a common generic `(a,b,c)` exists for all finitely many
  components simultaneously.

Two points the lemma uses implicitly that are fine in characteristic p and
deserve one line each in the repair: (i) a generic line meets a reduced plane
curve transversally in `deg` distinct smooth points in **any** characteristic,
because the closure of the tangent-line locus (dual curve, or a pencil for a
strange curve) is a proper closed subset of the dual plane — no
generic-smoothness input is needed; (ii) each pulled-back point is isolated in
the zero set of the **full** system because locally the zero set is
`C ∩ {pullback=0} = {q}` — the generic line avoids `pi(C ∩ (union of the
finitely many other components of W))`, so no other component of `W`, of any
dimension, passes through `q`.  Unrelated positive-dimensional components
elsewhere (including the junk locus `{x5=x3=0}` introduced by the
division-free multiplication by `x5`) are harmless: the theorem is applied to
isolated roots only, and the charged points have `x5 != 0`.

### 3. The 658 bound after mod-127 support shrinkage — SOUND AS USED

The exact use is the chain

```text
#isolated roots of the actual mod-127 seven-polynomial system
   <= MV(conv(A'_1 ∪ {0}), ..., conv(A'_7 ∪ {0}))     [affine isolated-root
                                                        theorem, algebraically
                                                        closed field, any char]
   <= MV(conv(A_1 ∪ {0}), ..., conv(A_7 ∪ {0})) = 658  [monotonicity]
```

where `A_i` are the characteristic-zero supports fed to Normaliz and
`A'_i ⊆ A_i` are the true mod-127 supports.  Both steps are correct: the
theorem is applied to the actual reduced polynomials with their actual
supports; and mixed volumes of convex bodies are monotone under inclusion in
each argument, which the origin-augmentation makes applicable since
`conv(A'_i ∪ {0}) ⊆ conv(A_i ∪ {0})`.  (Without origin-augmentation,
support shrinkage does *not* interact safely with torus counts; the producers
correctly use the augmented version.)  The tolerance of excess components is a
correct reading of the arbitrary-characteristic affine bound: it charges
isolated roots only.  With Repair 1 in place, only the multiplicity-free form
of the theorem is needed (the count is of distinct points on a **reduced**
cycle `Z` at transverse generic intersections), which firewalls the argument
against any with/without-multiplicity ambiguity in the cited statement.  One
degenerate corner should be stated (Issue 5): no row vanishes identically mod
127 — immediate, since an identically-zero row would kill the certified unit
6×6 Jacobian minor.

Frozen numerics, checked by hand where possible: seven supports in seven
variables `(w,c,d2,d4,x1,x3,x5)`; row supports of sizes `10,20,35,57,16,29`
(imposed rows `e1,e3,e5,e7,e2,e4`); line support exactly
`{x5, x3, w*x5}` matching the division-free pullback; `2^7-1 = 127` subset
volumes; `3316320 = 658 * 5040` (verified); raw torus `519 <= 658`
(consistent, as augmentation can only increase); both controls `1`; the
line-support singleton subset has rank 4 and volume 0, consistent with a
3-dimensional polytope in 7-space.  The supports are extracted from the same
hash-pinned `quotient_compiler.py` (`22b0cd...`) that the breadth lanes pin,
so the bound and the contact lanes are provably about the same six rows —
this identity of provenance is essential and holds.

Caveat (Issue 6): the two agreeing 658 computations are two executions of the
same `mixed_volume.py`/Normaliz-3.10.2 pipeline on different boxes with
byte-identical per-subset Normaliz outputs, not two independent
implementations; the lemma's phrase "a second Box03 implementation" oversells
what the case README states accurately.  I could not re-execute either.

### 4. Order-N lift ⟹ at least N at each of 190 distinct plane points — SOUND

Direction of maps is correct: the certified lift is a scheme map
`Spec A_N → (localized source)`, `A_N = F_127[s,v]/(s^N, H(w_i+s,v))`, i.e. a
family of N-jets *into* the source, whose `(w,v)`-composite is tautologically
`(w_i+s, v)`.  Because `H` is monic in `v` of degree 190 and
`H(w_i,·)` is squarefree with `H_v` a unit (both certified per lane, with an
explicit inverse witness for `H_v`), Hensel over the artinian local ring
`F̄[s]/(s^N)` splits `A_N ⊗ F̄` into exactly 190 jets `F̄[s]/(s^N)`, one per
root `v_j` — matching the certified lengths `moving_vdim = 1520 = 190*8` and
`12160 = 190*64` (and, for `w=25`, the certified leading ideal `{s^64,
v^190}`, which pins the standard-monomial basis).  Each jet's closed point is
the lex-shape base point `y_j` (base remainders certified zero), where by
Point 1 the source is formally `F̄[[w-w_i]]`; since the jet sends
`w-w_i ↦ s`, it is surjective onto the order-N truncation of the **unique**
branch.  The certified ratio identity `v*x5-x3+2*x5 = 0` in `A_N` forces the
branch's `v`-series to agree with the Hensel root `φ_j(s)` modulo `s^N`;
factoring `H(w_i+s,v) = Π_k (v - φ̂_k(s))` over `F̄[[s]]`, the 189 factors
with `k ≠ j` are units along the branch and the `j`-th has order `>= N`, so

```text
ord_s (pi^* H |_branch) >= N,  i.e.  i_{y_j}(pi^*H · C) >= N.
```

Ramification of `C → D_C` at `y_j` is irrelevant to this lower bound; branch
uniqueness (Point 1) prevents any splitting of the contribution; `Z` carries
`C` with multiplicity exactly 1 on **both** sides of the ledger (reduced-cycle
convention used consistently — no scheme-multiplicity of `W` along `C` is ever
invoked, which is the conservative and consistent choice).  Pushforward
multiplicities enter only through
`i_p(H · pi_*C) = Σ_{q→p} i_q(pi^*H · C) >= i_{y_j} >= N`, valid on a proper
model (Repair 2).  Distinctness: within a fibre the 190 plane points
`(w_i, v_j)` are distinct (squarefree), across fibres the `w_i` differ; local
contributions at distinct points add.  All sound.

The w=25 order-64 lane deserves special note because the erratum's count dies
without it (see Issue 4).  The order-64 xmodel report's prose does not itemize
the ratio and localizer checks through `s^64`, but the frozen, hash-pinned
`input.sing` contains the identical `evfinal`/`locfinal`/six-row
`final_fail` block used by the breadth lanes, with corrections at
`s^1..s^63`, and the frozen `result.out` (SHA pinned in `verify.py` and equal
to the SHA quoted in the xmodel report) shows `final_fail=0`, `base_fail=0`
(whose block includes the base ratio, base localizer, `H_v` and `det J`
inverse witnesses), `coefficient_order=1..63` each once, `order=64`,
`moving_vdim=12160`.  The erratum's sentence "the frozen w=25 lane certifies
the same through order 64" is therefore accurate at the frozen-byte level, not
merely attested.

### 5. Projective Bezout on the pushed-forward cycle — SOUND AFTER REPAIR 2

Under the reductio hypothesis (no component of `pi_*Z` equals `H`), each
`D̄_C` is an irreducible plane curve different from the irreducible `V(H̄)`,
so `H̄` shares no component with the effective 1-cycle `pi_*Z̄`; equivalently
`H ∘ pi` is not identically zero on any relevant `C`, so every local number is
finite.  Then

```text
I(H̄, pi_*Z̄) = 190 * deg(pi_*Z̄) <= 190 * 658 = 125020,
```

an equality-then-bound valid over the algebraically closed field in any
characteristic.  The charged affine contributions are among the nonnegative
local terms, so `190*704 = 133760 <= 125020` — contradiction, hence some
`D̄_C = V(H̄)` and the affine statement `pi(C)` has closure `H` follows.  The
dichotomy is clean: the properness needed for the local-global pushforward
ledger (Repair 2) is supplied by the normalization of the closure of the graph
of `pi|_C`, on which the map to `P^2` is finite; extra boundary points only
add nonnegative terms and cannot break the lower bound; and the affine
generic-line count of Point 2 computes exactly the projective degree
`deg(pi_*Z̄)` used here, because the generic line avoids each `D̄_C`'s points
at infinity — so the 658 bound and the Bezout budget refer to the same number.
The consistency of these two accountings is the crux of the proof and it
holds.

### 6. The self-contained count — VERIFIED

From the frozen `breadth_summary.json`: `all_passing_w` is exactly
`{1..83} \ {25,39,56}` (counts 24+13+16+27 = 80, verified by hand from the
list), `pass_count=80`, `fail_count=0`, `order=8`, `prime=127`; the Box02/03
split (`1..42 \ {25,39}` and `43..83 \ {56}`, 40+40) matches `summarize.py`'s
hard-coded preregistration.  `w=25` is excluded from the breadth set by
construction, so all 81 lifted fibres are distinct.  `80*8+64 = 704`,
`704 > 658` strict, excess `46`.  The count uses only fibres with a stored
positive-order moving lift; the 123-fibre baseline enters nowhere (its only
residue is the preregistered good-fibre filter in `run_one.sh` and the pinned
lex-shape base data each lane consumes — both stored artifacts, so the
erratum's "self-contained" label is fair: no *unstored* hypothesis remains).
The fail-closed `replay.py` pins the breadth summary, order-64 stdout/meta,
and the lemma report by hash, checks distinctness and `25 ∉` set, and
recomputes `704 > 658`.  `summarize.py` is fail-closed per lane (exact marker
multiset including `final_fail=0`, `moving_vdim=1520`, `coefficient_order`
exactly `1..7`, no Singular diagnostics, empty generator stderr, per-lane
pinned source hashes, and input/stdout/stderr hash agreement with each lane's
`run.meta`).  I spot-checked lane `w=1`'s frozen `result.out` markers directly
and lane `w=83`'s custody file set; the other 78 lanes rest on the summary's
per-lane hash ledger plus the summarizer's logic, which I read.

Margin structure (worth stating explicitly; the producer text does not): the
count tolerates the invalidation of at most 5 of the 80 order-8 lanes
(`704 - 8k > 658  ⟺  k <= 5`) and does **not** tolerate loss of the w=25
order-64 lane (`640 < 658`).  All 80 breadth lanes are load-bearing; the old
"twelve failure-tolerance lanes" language belongs to the superseded 68-lane
plan only.

### 7. Hidden assumptions — ENUMERATED

- **Separability** (char-p): genuinely used, not stated; repairable from
  certified data (Issue 1).  Repairable exposition gap, not wrong mathematics.
- **Properness / pushforward model**: needed for the local-global ledger and
  for "cycle-theoretic pushforward" of affine curves; standard graph-closure
  repair (Issue 2).  Exposition gap.
- **Reducedness**: `Z` is *defined* as the reduced cycle and multiplicity 1 is
  used consistently on both the sparse-count side and the contact side; no
  hidden reducedness of the six-row scheme `W` is assumed anywhere.  Clean.
- **Equidimensionality**: never needed globally; all statements are
  per-component, and each relevant component is a curve by the full-rank
  argument.  Unique-component-through-charged-point kills the worry that a
  charged point might sit on a higher-dimensional component.  Clean.
- **Saturation**: not needed; the lifts are verified by direct identity
  checks in the truncated algebra, not by ideal-theoretic elimination.  Clean.
- **Field extension**: all intersection theory is geometric (over
  `F̄_127`); the statement should be read as asserting a component over
  `F̄_127` (a Galois orbit descends to an `F_127`-irreducible component whose
  base change contains such a component; image equality is Galois-stable since
  `H` is defined over `F_127`).  Half-line clarification recommended
  (Issue 5).
- **Pinned inputs inside the firewall**: global geometric irreducibility of
  `H`, monicity in `v`, and exact total degree 190 are imported from
  predecessor frozen certificates and are *not* re-established by the reviewed
  artifacts (the lanes re-certify only fibrewise degree/squarefreeness).  If
  irreducibility failed, the same machinery would prove image = some
  irreducible factor of `H`, weakening the stated conclusion; the theorem's
  exact form rests on that pinned certificate.  Correctly cited as an input;
  flagged here as a dependency, not verified by this review.
- **Degenerate rows mod 127**: a row vanishing identically mod 127 would
  degenerate the seven-equation system; excluded by the certified unit
  Jacobian (Issue 5, one line).

### 8. Scope firewall — RESPECTED

All five reports carry explicit exclusions, and the erratum re-affirms them:
no degree-one/graph claim, no all-contact grouping (in particular the eight Q8
boundary contacts are *not* placed on the component — the full-contact
Jacobian certificate is boundary-local data, internally consistent, and is not
used in the count), no characteristic-zero no-merger, no Taylor realization,
no polynomial-boundary/terminal-row, no rationality, no Keller/trajectory/JC2
conclusion, and nothing about later bidegree or high-order-contact successors.
The conclusion reviewed here is exactly the mod-127 projected-component
existence statement, and nothing in the reviewed chain overreaches it.

---

## Issues and exact repairs (ranked)

1. **[Repair required — lemma text] Char-127 separability in the
   generic-line count.**  Where: lemma, "Why 658 bounds the relevant
   projection cycle."  As written, "the number of these points ... is exactly
   deg(pi_*Z)" is false for an inseparable `C → D_C` (undercount by the
   inseparable degree), which would break inequality (1)'s derivation.
   Cleanest repair (two sentences, no computation): *at a charged point the
   certified unit Jacobian makes `w-w_i` a uniformizer, so `C → A^1_w` is
   unramified there; hence `K(C)/F̄(w)` is separable (inseparable curve maps
   are everywhere-ramified with index ≥ p), hence so is the intermediate
   extension `K(C)/K(D_C)`; therefore a generic fibre of `C → D_C` consists
   of exactly `deg(C→D_C)` reduced points.*  Optionally also record that
   generic-line transversality is characteristic-free (dual locus is a proper
   closed subset of the dual plane).

2. **[Repair required — lemma text] Proper model for the pushforward
   ledger, and the source-infinity bad set.**  Where: lemma, same section and
   "Additive finite contact."  Add one paragraph: define `pi_*` and the
   local-global identity `i_p(H·pi_*C) = Σ_{q→p} i_q(pi^*H·C)` on the
   normalization of the closure of the graph of `pi|_C` (finite onto `D̄_C`);
   note that boundary/infinity points only add nonnegative terms, so the
   charged lower bound survives; and add "images of the finitely many closure
   points of `C` outside the affine chart" to the list of finite sets the
   generic line must avoid, so that the affine root count equals the
   projective degree `deg(pi_*Z̄)` consumed by Bezout.

3. **[Repair recommended — lemma text] State the root count as an
   inequality.**  Replace "counted with cycle multiplicity, is exactly
   `deg(pi_*Z)`" by "is at least `deg(pi_*Z̄)` distinct isolated roots" (with
   Repairs 1–2 it is in fact equal, but only `>=` is used).  This makes the
   argument depend only on the multiplicity-free form of the
   arbitrary-characteristic affine isolated-root bound and removes any
   sensitivity to the exact multiplicity convention in the cited theorem.

4. **[Statement recommended — erratum] Criticality of the w=25 lane and the
   true failure tolerance.**  The erratum's "strict margin is 46 normalized
   orders" invites misreading as fibre-level slack.  State explicitly: losing
   the order-64 lane is fatal (`640 < 658`); losing up to 5 order-8 lanes is
   survivable; all 80 breadth lanes are otherwise load-bearing.  The cheapest
   hardening, if ever desired, is three additional order-8 fibres
   (`83*8 = 664 > 658`), which would make the count independent of the single
   order-64 artifact.  (Also: cosmetically, itemize the ratio/localizer
   order-64 checks in the order-64 report or case README; the frozen
   `input.sing`/`result.out` already contain them, as verified above.)

5. **[Repair recommended — half-lines] Three small statements:** (i) no row
   vanishes identically mod 127 (unit-Jacobian argument); (ii) the component
   in the conclusion is a component over `F̄_127` (Galois descent remark);
   (iii) global geometric irreducibility, monicity, and total degree 190 of
   `H` are pinned predecessor inputs — cite their frozen certificate hash next
   to the claim in the lemma/breadth reports.

6. **[Wording — lemma] "A second Box03 implementation" overstates.**  The
   Box03 shard is the same hash-pinned `mixed_volume.py` (its `base_sha256`
   equals the Box02 script hash) re-executed affine-only, with byte-identical
   per-subset Normaliz outputs.  It is execution replication, not
   implementation independence.  Either amend the sentence in a successor
   (the case README's phrasing is accurate) or, if implementation
   independence is wanted, run one genuinely independent mixed-volume
   computation.  Not verdict-relevant: my confirmation rests on the frozen
   attestation either way.

7. **[Record hygiene — no action on frozen files] Superseded 662 fields.**
   `breadth_summary.json` (`strict_component_inequality: "662>658"`), the
   breadth FREEZE, and lemma equation (3) still display the superseded count.
   Immutability is correct; recommend only that future tooling key on the
   self-contained case (`replay.py`, FREEZE `704>658`), and that any new
   summary carry a `superseded_by` pointer.

No issue rises to REJECTED: items 1–3 are gaps in the written proof whose
repairs are forced by already-frozen certificates; items 4–7 are statement,
provenance, and hygiene matters.

## Custody cross-checks performed (citation level, hashes not recomputed)

- Lemma report SHA `78fb3e...` quoted identically by: sparse FREEZE, breadth
  component report, self-contained `replay.py`.
- Breadth component report SHA `fa3498...` quoted by breadth FREEZE; erratum
  SHA `2aa347...` quoted by self-contained FREEZE.
- `breadth_summary.json` SHA `7cfeb9...` pinned by both the breadth report's
  custody block and `replay.py`; `generate_breadth.py` `6b33f1...`,
  `run_one.sh` `0318b2...` pinned identically by the breadth report,
  `summarize.py` SOURCES, and the summary's `source_sha256`.
- Order-64 stdout SHA `f750d9...` quoted identically by the order-64 xmodel
  report, the order-64 `verify.py`, and `replay.py`; `run.meta` SHA
  `3cd0c3...` by the latter two.
- Sparse case: lemma custody block's `74685b...`/`d9cc48...`/`a6a516...`
  match `manifest.sha256` entries for Box02/Box03 `result.json` and
  `mixed_volume.py`; the supports' compiler hash `22b0cd...` matches the
  breadth lanes' pinned compiler, tying the 658 bound to the same six rows the
  lifts satisfy.
- Hand arithmetic verified: `658*5040 = 3316320`; `190*8 = 1520`;
  `190*64 = 12160`; `80*8+64 = 704`; `190*704 = 133760 > 125020 = 190*658`;
  `|{1..83}\{25,39,56}| = 80`; `|{1..126}\{39,56,125}| = 123`.

## Conclusion

With Repairs 1–3 written into a successor of the lemma (no recomputation
needed), the chain

```text
frozen order-8/order-64 lifts (704)  +  frozen 658 sparse bound
   ⟹  190*704 > 190*658  ⟹  some relevant mod-127 source component
                              projects onto the degree-190 irreducible H
```

is exact at the stated tier, conditional only on the pinned predecessor
certificates it cites (candidate `H` irreducibility/degree/monicity and the
lex-shape base custody).  **CONFIRMED WITH REPAIRS**, on the self-contained
count `80*8 + 64 = 704 > 658` and on no other count.
