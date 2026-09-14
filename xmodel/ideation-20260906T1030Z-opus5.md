# Blind whole-portfolio ideation — Opus 5 — round 20260906T1030Z

Basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. Desk work only: no AWS, no
fleet change, no heavy host CAS, no ledger/tool/adapter edit, no `jc2-lean`, no
public contact. I did not read root's sealed submission, any peer submission of
this round, the live factored-J Fable gate, the Sol 2 TB report, or the local
K16 boundary report.

**Headline.** One genuinely new mechanism, measured, not proposed:
**[C-COLLAPSE]** — on the frozen δ=2 (99,66) physical family the 192 `A3`
source parameters are *not* 192 degrees of freedom. The whole Jacobian system
is affine-linear in that block, the block's linear map has generic rank exactly
**191** (measured; certificate one-sided in the sound direction) and rank **≥
188 at every parameter point** (proved from a charged theorem). So `C` is
rigidly determined by `(h,D,a,b)` up to an additive constant, everywhere, and
the physical counterexample question on this family has effective dimension
**≤ 248**, not 439 or 600. Consequences: the disproof-side search target should
be reparametrized, and the currently dominant object to solve is the physical
locus, not the T2/T3 chart. No properness, no point, no exclusion, and JC2
remains unresolved.

## 0. Manifest verification (mechanical)

`/tmp/jc2-lane.BKTGvL/charged-inputs.list` gives 18 indexed `path key sha256`
records. I looped them into `sha256sum` against `inputs/<key>`: **18/18 OK**,
including the six packet-named ledger hashes, which I did not retype. Packet
self-seal recomputed: exactly one standalone `<!-- BODY-END -->` at line 197,
body **11,656 bytes**, SHA-256 `db7e289dffdd38e7f8d54ff158e67998bbdfef6ca6be7df142bda5ea9d17c3d6`
— both match its own Seal block. Read completely: packet, `APPROACHES.md`,
archived master union table §1 (avenues 1–46), the 10:26Z LIVE STATE plus the
02:52Z–09:53Z entries, `preflight.py`, and the seven charged reports. My own
notes and the reproducible script are `box/cblock-collapse-20260906/`
(16 KB, well under the 2 MB cap). The one source file I opened outside the lane
inputs is the frozen `box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json`,
read-only, whose SHA-256 I re-verified against the pin already inside charged
`preflight.py`: `778eda93…3e1ea`. Field is **Q** throughout unless a modular
step is marked; every modular step below is stated with its direction of
one-sidedness.

## 1. Disposition vector — all 46 archived avenues

Legend: **ACTIVE** = carries current work; **CLIENT** = supplies a consumed
ingredient, not a program; **DORMANT** = alive but not now; **LOW** = keep
parked; **CLOSED/REFUTED** = do not restart at the stated hypotheses. Only
rows marked *(change)* differ from the archived/current reading; the archive's
scores are not treated as authority.

| # | Disp | # | Disp | # | Disp | # | Disp |
|--:|---|--:|---|--:|---|--:|---|
|1|ACTIVE|13|DORMANT|25|DORMANT|37|LOW|
|2|DORMANT-HIGH|14|DORMANT|26|DORMANT|38|LOW|
|3|DORMANT|15|LOW|27|DORMANT|39|LOW|
|4|DORMANT *(change: lower)*|16|LOW|28|DORMANT|40|LOW|
|5|CLIENT *(change: raise)*|17|CLOSED|29|ACTIVE *(change: raise)*|41|REFUTED|
|6|DORMANT|18|CLOSED|30|DORMANT|42|LOW|
|7|DORMANT|19|DORMANT|31|DORMANT|43|CLIENT *(change: raise)*|
|8|LOW|20|LOW|32|DORMANT|44|CLOSED|
|9|DORMANT|21|LOW|33|CLOSED-COSTUME|45|LOW|
|10|CLOSED *(change: confirmed)*|22|LOW|34|LOW|46|LOW|
|11|REFUTED|23|LOW|35|LOW| | |
|12|LOW|24|LOW|36|ACTIVE *(change: raise)*| | |

Reasons for the six changes, and only those:

- **5 (Jung–van der Kulk degree descent) → CLIENT.** Not as a program: as the
  consumed final arrow. Arrow 4 of the promoted reverse gate is exactly `99∤66`,
  `66∤99`. The avenue's archived stuck-point ("amalgam rigidity never bites on
  non-automorphisms") is irrelevant to that use, because the theorem is applied
  contrapositively to an assumed pair. Do not re-open the descent program.
- **10 (HC4 bridge) → CLOSED, confirmed this round.** The charged Ni interface
  audit finds the pairing needs a plane component of degree ≤ 2; for arbitrary
  `Q` the leading-coefficient test degenerates to an identity. Two independent
  negative results now (sol-hc4probe, this audit). The `a≠0` strengthening
  stays at producer scope and is not a JC2 lane.
- **29 (LND / Hamiltonian derivation) → ACTIVE.** Newly load-bearing, not
  aspirational: §3 shows the entire `C` block of the physical family is the
  image of the Hamiltonian derivation `δ_G = J(·,G)` restricted to a
  192-dimensional space, and its kernel is computed by the closed-polynomial
  theorem. The avenue's own archived obstacle ("LND-ness with a slice is the
  conjecture again") is *not* triggered: I use only the kernel of `δ_G`, never
  local nilpotence. See the explicit negative control in §3.
- **36 (guided counterexample search) → ACTIVE.** For the first time it has a
  licensed target with exact forced degrees (`h_top = y⁹(y−x)²⁴` fixed at every
  parameter value ⇒ `deg F=99`, `deg G=66`), a promoted one-way
  point-⇒-counterexample implication, and — new here — a millisecond exact
  feasibility oracle over 247 parameters. Its archived objection ("above the
  GGV cutoff the space is enormous") is materially weakened, from 439 free
  physical coordinates to ≤ 248, though 248 is still not small.
- **43 (Ritt / composite coordinates) → CLIENT.** The only place where the
  [C-COLLAPSE] rank can drop below 191 is where `G` is a proper composite
  `G=φ(G̃)`; the admissible `deg G̃` are pinned to `{11,22,33}` by the fixed top
  form. That is a Ritt-type condition used as a stratum test, nothing more.
- **4 (formal-germ certification) → lower.** The physical locus of §3–4 is the
  polynomial object that germ prolongation was a proxy for, at strictly better
  logical strength (`modular nonempty ≠ germ ≠ char-0 ≠ polynomial` was the
  avenue's own stuck-point). Spending on D-series depth is now dominated.

Avenues 2, 26, 27, 28, 30, 31 remain the only credible *all-degree* proof
family and are unchanged: they still lack a universal landing/coverage theorem
and an absolute td ceiling, and nothing this round touched either gap.

## 2. Reranked bottlenecks

**Proof / exclusion side** (highest first; #1 and #2 swapped versus the
implicit ordering of the current computational queue):

1. **Source-to-chart necessity (typed GAP).** Until "genuine Keller pair of
   this configuration ⇒ point of the tested chart" is proved, *no* emptiness
   result anywhere in the T2/T3 or physical program excludes a case. This
   dominates everything else on the proof side; a solver win does not touch it.
2. **Uniform exclusion of the 44 `u_s=1` receivers at all degrees.** `n ≤ 200`
   is a test population, not a universe. Unchanged.
3. **K16**: `OPEN[K16-UETA-WHOLE-POLYNOMIAL]` at every actual `m≥4` and every
   factor of `Q[d]/(3d²−m)`, plus the separate `b=0` (BOUNDARY) obligation.
4. **Decision cost on a single chart.** *Demoted* from its de-facto top
   position. §3 shows a large part of the recent variable count was illusory;
   and by #1 a decision on the current charts is not currently promotable to an
   exclusion in either direction.

**Disproof / existence side:**

1. **No candidate point, and no search strategy over the right parameters.**
   *(New #1; previously "representation/build cost".)*
2. **Deciding the 247-parameter, degree-≤2-in-D residual system** after the
   `C` block is collapsed. Undecided; I do not claim it is cheap.
3. Representation/build cost — *demoted*: the pilot already builds the complete
   physical presentation in 137 s / 1.71 GiB, and §3 removes 191 of its
   directions before any solver sees them.
4. Verification of a hit — **effectively solved**: exact rational Cramer plus
   direct expansion of `J(F,G)`, no Gröbner, no compressor, no Theorem B.

## 3. NEW MECHANISM — CARD 1: [C-COLLAPSE]

Provisional label: **NEW** at the level of the charged record. Possible
**DUPLICATE** of root's sealed follow-up to `preflight.py`, which already
establishes the 192-parameter linearity and the highest-face identity that I
start from; I could not read that submission, so I flag the overlap rather than
claim priority. The rank measurement, the uniform corank bound and the
reparametrization consequence are not in any charged input.

**Statement.** On the frozen δ=2 source map (99-branch), with `X=x`, `W=y−x`,
`F = h³+(3D+a)h/2+C`, `G = h²−bh/3+D`:

```text
(I)   J(F,G) = ((3D+a+b·h)/2)·J(h,D) + J(C,G).
```

I verified (I) symbolically with `h,D,C` free, together with the charged
pilot's three-term form and the identity
`(2h−b/3)J(C,h)+J(C,D) = J(C,G)` that converts one into the other
(`box/cblock-collapse-20260906/`, three `True`s). (I) is a two-term regrouping
of the charged identity, not a new physical formula; its point is that **every**
`A3` parameter now sits inside a single Jacobian bracket.

Consequences, in order of logical strength:

- **(a) Exact affine-linearity.** `c ↦ C` is linear and injective (each of the
  192 `A3c_*` symbols occupies an identity slot; charged `preflight.py` asserts
  this and I re-verified the support). Hence the 1,468 positive-degree Jacobian
  rows form an affine-linear system `A(h,D,a,b)·c = −Φ(h,D,a,b)` with
  `Φ = ` positive part of `((3D+a+bh)/2)J(h,D)`, and `A`'s columns are
  `J(C_k,G)`.
- **(b) Uniform corank bound (proved, all parameter points, char 0).**
  `ker A = V ∩ ker J(·,G)` where `V` is the 192-dimensional image of the `A3`
  window. By the closed-polynomial theorem (Arzhantsev–Petravchuk; the same
  theorem the promoted reverse gate consumes for its `j=0` exclusion),
  `ker J(·,G) = K[G̃]` with `G = φ(G̃)`. The top form `G_top = y¹⁸(y−x)⁴⁸` is
  fixed at every parameter value, so `(G̃_top)^{66/e} = G_top` forces
  `66/e | gcd(18,48) = 6`, i.e. `e = deg G̃ ∈ {11,22,33,66}`. Since
  `deg C ≤ 35`, `dim(K[G̃] ∩ {deg ≤ 35}) = 1+⌊35/e⌋ ≤ 4`. **Therefore
  `rank A ≥ 188` at every point of the parameter space**, with no genericity
  assumption and no localization.
- **(c) Generic rank exactly 191 (measured, sound direction).** At an integer
  parameter point I built `A` and `Φ` exactly and reduced modulo
  `p = 2³¹−1`: `rank A = 191`, `rank[A|Φ] = 192`, over **1,468** positive-degree
  rows out of **1,469** nonzero physical positions. Repeated at a second seed
  and `p = 1000003`: identical. Since rank can only drop under reduction,
  `rank_Q A ≥ 191` at that point, hence generic `rank_Q A ≥ 191`; and the
  constant polynomial is in the window (`A3c_98_0` is an identity slot at
  `(r,z)=(98,0)`), so `1 ∈ ker A` always and generic rank is **exactly 191**.
  The one kernel direction is the additive constant of `C`, which changes `F`
  by a constant and `J(F,G)` not at all.
- **(d) Reparametrization.** 439 physical coordinates split exactly as
  192 (`C`) + 245 (`h`,`D`) + 2 (`a`,`b`) — reproduced from the source, matching
  the pilot's 439. After (b)+(c), the effective search space is
  **≤ 245+2+1 = 248**, and the residual system is quadratic in the 182 `B2`
  parameters, of degree ≤ 3 in the 7 `h3` parameters, and *empty of `C`*.

**Independently reproduced from the frozen source, not consumed:** `deg h=33`,
`deg D=34`, `deg G=66`, `deg Φ=99`, the 1,469/1,468 support counts, and
`min_r(B2)=31`, `min_r(A3)=63`.

**Negative controls this survives.** (i) It does *not* assert `δ_G` is locally
nilpotent. The tempting step "`δ_G(F)=j≠0` ⇒ slice ⇒ `K[X,W]=ker δ_G[F/j]`" is
**false for non-LND derivations** — `δ=∂_x+y∂_y` has slice `x` and kernel `K` —
and assuming it would be assuming JC2. I use only the kernel theorem.
(ii) It is not a generic-only shortcut: (b) is uniform over all points, and (c)
is one-sided in the direction that makes the conclusion safe. (iii) It is not a
modular-to-Q leap: the modular step lower-bounds a rank over `Q`; nothing is
lifted. (iv) It is not a finite-to-all-degree extrapolation: the claim is about
one frozen source family, and I claim nothing at other degrees.

- **Dependencies.** The frozen source map (hash-pinned); `preflight.py`'s
  linearity/identity-slot checks; the Arzhantsev–Petravchuk closed-polynomial
  theorem as already charged; the pilot's physical reconstruction of `F,G`.
- **Cheapest discriminator.** Already run: build `A`,`Φ` at one integer point,
  one mod-`p` rank pair. ~4 minutes wall on the host, 16 KB of artifacts.
- **Gate/time price.** A different-model gate needs the same script plus the
  three symbolic identities: ≤ 30 minutes desk, no fleet.
- **Outcomes.** rank 191 (observed) ⇒ collapse holds, act on §4/§6. rank < 188
  would contradict (b) and indicate a source/support misreading — treat as a
  bug, not mathematics. rank 192 would mean the constant is not really in the
  window ⇒ collapse is *stronger* (`C` fully determined). `rank[A|Φ] = rank A`
  at a random point would have been a feasibility signal only, never a point.
- **Stop condition.** Stop if any of: the identity check fails on a re-derived
  `F,G`; `A3` is found not to be injective on the window; or the source map is
  superseded.
- **Information gain.** Removes 191 of 439 physical coordinates from every
  downstream decision on this family, and converts "which of 600 variables"
  into "which of 248 parameters", with an exact per-point oracle (§6).

## 4. NEW CONNECTION — CARD 2: the physical locus dominates the T2/T3 chart

Provisional label: **NEW**; the packet states the weaker "a unit excludes only
this family", which is consistent with, but does not record, the containment.

Let `I` be the complete direct T2/T3 ideal on the **same** frozen δ=2 source map
(the promoted reverse gate names `778eda93…` among `build_direct.py`'s three
maps; the pilot's sole source is that same hash), and let `Jphys` be the pilot's
complete lifted physical Jacobian ideal. Arrow 2 of the promoted gate says every
field point of `J_core ⊆ I` has `J(F,G) ∈ K×`; "`J(F,G)` is a nonzero constant"
is *literally* the generator set of `Jphys` (1,468 positive coefficients vanish,
plus `Zj·J0−1`), and the graph variables `Hfact`, `Zj` are uniquely determined
functions of the source point. Hence, on the shared source coordinates,

```text
(II)  π(V(I)) ⊆ V(Jphys)      [δ=2, (99,66) branch only; not D108]
```

with `π` forgetting the five T2/T3 auxiliaries `Zρ,t3eq,t3_fq,λ3,Z3` and the
five unused source names. Both directions of (II) matter and they point the
same way:

- **Existence:** a point of `Jphys` is *directly* a counterexample (Arrows 1
  and 4 need only the parameter-free `h_top` and `99∤66`), and `V(Jphys)` is the
  larger set. So `Jphys` is the easier place to find a point.
- **Exclusion:** `V(Jphys)=∅` implies `V(I)=∅`. So `Jphys` emptiness is the
  strictly stronger theorem — and, by the unresolved source-necessity GAP,
  *neither* emptiness statement currently excludes the (99,66) case.

**Therefore the T2/T3 chart is dominated on both sides for this source map**,
and the honest reading is that the current chart program has no promoted payoff
until the GAP closes, while the physical locus retains one (existence). Two
scope limits I will not blur: (II) is proved only for the δ=2 99-branch, not for
D108; and `Jphys` **omits** the ρ/T2/T3 leader localizers, so it is a strictly
larger family with no necessity or coverage claim, and its emptiness excludes no
Moh row.

Sub-connection, no extra card: the closed-polynomial theorem does *double duty*
— the same charged theorem that kills `j=0` at chart points (gate Arrow 2)
bounds the `C`-block corank in §3. Charging it twice is free.

- **Cheapest discriminator for (II) itself.** Confirm that `build_direct.py`'s
  99-branch source hash equals the pilot's (done: `778eda93…`), and that
  `T2_upper ∪ T2_strict ∪ face ∪ T3_strict` is a subset of the emitted rows
  (already established in the promoted gate). ~10 minutes desk.
- **Outcomes.** If the two builders were found to use different δ=2 maps, (II)
  is void and the two loci are simply incomparable — this is the only way the
  card fails, and it is a hash check.
- **Stop condition / information gain.** Stop if the source hashes diverge;
  otherwise the gain is a strict reranking of which object to spend on, at zero
  compute.

## 5. Strongest proof attempt, and strongest disproof/falsification attack

**Strongest proof-side move available now (and it is not a chart solve).**
Close the source-to-chart necessity GAP for one configuration, or prove the
*complement*: exhibit a genuine normalized (99,66) Moh datum whose realizing
polynomials do **not** satisfy the stage-8 gauge slices (`beta=1`, `jet0=0`,
`ρ≠0`, the Prop 4.6 `T3` face). Either outcome is decisive for the whole
exclusion program, and neither needs a solver. Everything else on the proof side
is currently blocked behind it. I do **not** offer a new exclusion mechanism;
on the receiver front my honest verdict is **NO_NEW_MECHANISM** — more descent
on already-transported arithmetic has no recorded yield, the family-C radius
licence is refuted from print, and I found nothing cheaper this round.

**Strongest disproof/falsification attack — CARD 3: the 248-parameter exact
oracle search.** After [C-COLLAPSE], searching for a counterexample in this
family is: choose `(h3,C2,C3,B2,a,b) ∈ Q^{247}`; build `A`,`Φ` (milliseconds);
decide `rank[A|Φ] = rank A` **exactly over Q**; if equal, Cramer gives `C`
exactly; then expand `J(F,G)` and check it is a nonzero constant. A success is a
complete, self-certifying plane-JC counterexample with no Gröbner basis, no
compressor, no modular lifting and no Theorem B. This is avenue 36 with a
licensed target.

- **Dependencies.** Card 1 (a)–(c); Arrows 1 and 4 of the promoted gate for
  degrees and non-automorphy; exact rational linear algebra only.
- **Cheapest discriminator.** The 4-minute script already written, looped.
- **Gate/time price.** A first bounded sweep is ≤ 1 host-hour with no fleet;
  a structured sweep (see §6) is one worker-day if authorized.
- **Interpretation of every outcome.** *Consistent point found* ⇒ verify
  exactly, then it is a counterexample (scope: over `Qbar`, from a `Q`-point it
  is over `Q`). *All sampled points inconsistent* ⇒ **nothing**: the consistency
  locus is a proper closed subset of a 247-dimensional space, so sampling
  failure is not exclusion, ever. *A point consistent but `J0 = 0`* ⇒ rejected
  by the `Zj·J0−1` row, exactly the control the pilot's `ρ=1` case exercises.
- **Stop condition.** Stop the sweep after a fixed budget; do not report a
  sampling failure as evidence. Stop permanently if the source map is
  superseded or if `Jphys` is shown proper by other means.
- **Information gain.** Bounded but real: it is the only route in the portfolio
  whose *success* needs no unproved interface. Its failure gains nothing, and I
  say so rather than dressing it as evidence.

## 6. Software acceleration / decisive experiment

**Not a new solver; a preprocessing rule and an oracle.**

1. **Never hand a solver the `C` block.** Any future elimination on this family
   should first (i) fix a 191-row base with a nonzero minor at a witness point,
   (ii) declare the localization complement `{minor = 0}` explicitly as a
   separate stratum, bounded by Card 1(b) to corank ≤ 4 and by the Ritt
   condition `deg G̃ ∈ {11,22,33}`, and (iii) solve only in the ≤ 248 remaining
   parameters. I do **not** claim symbolic Cramer is affordable: a 192×192
   determinant in 247 parameters is not, and I checked that before proposing.
   The affordable form is the per-point oracle, not a symbolic elimination.
2. **The oracle is the acceleration.** Exact feasibility of 1,468 equations in
   192 unknowns is one rank comparison: microseconds modulo `p`, milliseconds
   exactly over `Q`. Compared with an 85 GiB / 1,192 s build of an *incomplete*
   466-row subset, or a ~1.5 TiB still-building full stream, this is five to six
   orders of magnitude cheaper per decision — while deciding a strictly smaller
   question (one parameter point, not the whole locus). Both halves of that
   sentence are load-bearing.
3. **Structured sweep, if authorized.** The top-degree row is already solved in
   closed form by charged `preflight.py`: `D_top = x²(x+z)⁵z²⁵·ℓ`,
   `C_top = (3/8)x⁴(x+z)z²⁶·ℓ²` with `ℓ = aa·x²+bb·xz+cc·z²` arbitrary, i.e. a
   3-parameter solved face. Sweep *along that face* (top row satisfied by
   construction) rather than uniformly at random; the oracle then measures how
   deep the consistency survives. This is a measurement of where the family
   dies, which is information whether or not a point exists.

## 7. Systems UPGRADE — reasoned NO_CHANGE, with one narrow exception

**NO_CHANGE** to models, ceilings, seats, custody protocol, seal contract, or
lane tooling. The observed failure modes this round were mathematical scoping
(a completion-count assertion defect, a wrong `t3eq` deletion suggestion, an
unlicensed blanket `T3⇔Keller` proposal), all caught by the existing
different-model gate discipline. Adding seats or RAM addresses none of them, and
the packet's own evidence is that increasing RAM does not answer an elimination
wall. One narrow exception, which costs nothing:

- **Add a "declared-freedom audit" to the pre-launch checklist**: before any
  solve is launched on a chart, record which variable blocks enter *linearly*
  and measure the rank of each such block at one point. Had this existed, the
  192 `C` coordinates would have been known to be 1 effective coordinate before
  any TB-scale build. It is a 60-line script, no infrastructure, no new seat.

## 8. Continue / redesign / stop for major current work

- **`.63` (99,66) δ=2 466-row subset long solve — CONTINUE to its due time, do
  not extend or relaunch.** It is detached and paid for. But its value is
  one-sided and small: per the promoted gate's own table a nonunit on a subset
  `S ⊉ J_core` has *no* existence force, and a unit excludes the chart but not
  the case (GAP). Harvest, do not reinvest.
- **`.73` k7-b9q0 — CONTINUE.** Independent K=7 strata target, 9/10 already
  certified, untouched by anything here.
- **`.103` full 2 TB T2/T3 build — REDESIGN (coordinator's call; I am blind to
  its report).** By Card 2 it is building the *dominated* object: emptiness
  there is weaker than `Jphys` emptiness and still excludes no case, while a
  point there is harder to reach than in `Jphys`. Note explicitly that
  [C-COLLAPSE] does **not** transfer to it: the T2/T3 rows contain `F²`, so they
  are *quadratic*, not linear, in `C`. Before any solver is started on
  ~1.5 TiB of built stream, run the declared-freedom audit of §7 on its blocks.
- **Compressor / R005 continuation — STOP as a general strategy.** Its own
  continuation banks `x6.149` term growth at 54 pivots with no decision; the
  packet already refuses automatic deeper pivots and 44-receiver ports. The
  scalar-monic substitution is sound and stays available as a local tool.
- **R050 parent-residue — STOP.** Gate is terminal, `NO_NEW_MECHANISM`, the
  residue mixes Jacobian rows of degrees 1..250 with no measured pruning, and
  the `e=28` conjugate place adds no condition. Do not fund the larger replay.
- **K16 — CONTINUE at the weakest sufficient target** (`b·B_m·η_m ≠ 0` empty on
  `V(K_m)` for every actual `m ≥ 4` and every factor of `Q[d]/(3d²−m)`), plus
  the separate `b=0` boundary. Do not spend on `B=0` families (support gcd > 1
  already forces `B=0`) or on full solution classification, which is strictly
  stronger than what the terminal chart consumes.

## 9. OPENs raised here — exact quantity and cheapest test

- `OPEN[C-BLOCK-MINIMUM-RANK]`. **Quantity:** `min` over the 247-parameter
  space of `rank A ∈ [188,191]`, equivalently whether any parameter point makes
  `G = h²−bh/3+D` a proper composite with `deg G̃ ∈ {11,22,33}`. **Cheapest
  test:** for each `e ∈ {11,22,33}` ask whether `G` can equal `φ(G̃)`, `deg φ =
  66/e`; the `e = 33` case is one polynomial identity `G = G̃²+βG̃+γ` in the
  245+1 parameters, testable by comparing the `(r,z)` supports of `B2` against
  the forced support of `G̃²`, minutes of desk work. Consequence if empty:
  `rank A ≡ 191` on the whole space and the localization complement disappears.
- `OPEN[UNIVERSAL-COKERNEL-UNIT]`. **Quantity:** whether some row vector
  `ℓ(params)` with `ℓ·A ≡ 0` identically has `ℓ·Φ` a **unit**. The left-null
  module has rank `1468 − 191 = 1277` over `Q(params)`, so such `ℓ` exist in
  abundance; the question is only whether one of them evaluates `Φ` to a nonzero
  constant, which would be a one-line emptiness proof for this family.
  **Cheapest test:** the classical instance is evaluation at a critical point of
  `G`, which gives `ℓ·Φ = j ≠ 0` and reproves only the classical
  `V(G_X,G_W) = ∅`; so the cheap test is whether the *family-specific* part
  (the 192-dimensional window versus all of `{deg ≤ 35}`) contributes any `ℓ`
  beyond that — compute, at one point, `rank A` versus the rank of the full
  truncated multiplier map `(A,B) ↦ A·G_X+B·G_W`, `deg A,B ≤ 34`. One extra
  rank computation on the same script.
- `OPEN[SOURCE-NECESSITY]` (restated, not new). **Quantity:** whether every
  genuine normalized (99,66) Keller pair realizes the stage-8 gauge
  (`beta=1`, `jet0=0`, `ρ≠0`, Prop 4.6 `T3` face). **Cheapest test:** one
  realized Moh datum checked against the four slices by direct substitution.

## 10. FALLACY-v2 audit

No exit claim is asserted anywhere above, so **no `charge_basis=` line
applies**. Floors are never promoted to attainment: `rank ≥ 188` is used only as
a lower bound and `rank = 191` is stated as measured-at-a-point plus a proved
upper bound. The modular step is one-sided in the safe direction and is not
lifted. `sat()` does not appear; the one localization (`minor ≠ 0`) is declared
with its complement and a bound on the complement's corank. Ring, coordinates
(`X=x`, `W=y−x`, determinant `+1`), generator order and coefficient field are
declared; the `A3`→`C` map is stated with its injectivity check rather than
inferred from matching names. Nilpotents: all statements are about geometric
points over `Qbar`, which is exactly what Nullstellensatz properness controls;
I make no claim about the scheme structure, and Card 1(c)'s rank is a statement
about a matrix over a field, not about the ideal being radical. All-degree
quantifiers: every claim in §3–§6 is scoped to one frozen source family at one
degree pair, and none of it is extrapolated to other degrees, to D108, or to
all-degree exclusion. Source/receiver direction: §3–§6 are **source-side**
(existence); the receiver/exclusion direction receives an explicit
`NO_NEW_MECHANISM` in §5.

**Portfolio recommendation: REDESIGN.** Not "stop" — the K16 lane and the
`.63`/`.73` capped solves should run out — and not "continue", because the
current centre of gravity (build and solve ever-larger T2/T3 charts) is spending
on a doubly dominated object: its emptiness is weaker than the physical locus's
and still excludes nothing under the open GAP, while its points are harder to
reach. Redesign to two threads: (1) the source-necessity GAP, which is the only
thing that can make any emptiness result mean something; (2) the C-collapsed
248-parameter physical search, which is the only route whose success needs no
unproved interface. Everything else is maintenance.

<!-- BODY-END -->
