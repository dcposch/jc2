# Cross exchange 20260906T1030Z — Fable 5.1

Basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. Written 11:52Z–12:01Z,
desk only. Custody: the 14 files in the lane `inputs/` were hashed; the
five blind bodies and FALLACY-v2 match `collection.json` (five full hashes,
fable5 body `ba0a59d3…`, coordinator body `b7858e26…`, 9,205 B); the cross
packet body recomputes to 5,890 B / `f74aaf7e…`; the six uncollected
terminal reports are byte-identical to their repo copies. One tiny exact
control was run (30 s, read-only) on the frozen source JSON `778eda93…`:
`h(X,0)=X+c`, `G(X,0)` monic quadratic, degree-33 C rows have W-exponents
24–32 only, and `h3` carries a fixed numeric `-8/3` at (4,5) plus the fixed
X-coefficient 1 in `C3`. No live CROSS submission, log or ledger was read.

Facts marked [POST-CUTOFF] come from the six terminal reports and the packet,
not from any blind body.

## 1. Strongest surviving mechanism

**The C block is a rigid linear graph, and its correct consumer is an
evaluator, not an expansion.** Four blind origins (root Card 2, Astra Card 1,
Sol Card 2, Opus Card 1, my §4) converge on the same algebra: with
`F=h^3+(3D+a)h/2+C`, `G=h^2-bh/3+D`, every J row is affine-linear in the 192
`A3` coordinates through `C ↦ J(C,G)`, the top operator is diagonal on
monomials with `J(Y^iW^j,Y^9W^24)∝(8i-3j)`, and the only resonances are
`H^k`, `k=0..3`. These are duplicates of one mechanism; I merge them.

[POST-CUTOFF] What survives with proof: the filtered pilot's 189 constant
pivots with a unit lower-triangular minor identically 1 over all lower `G`
coefficients (the actual graded source lacks `H^3`, so deficiency 3, not 4);
and the transverse-line theorem, full-map kernel `= k·1` at every base point.
What is refuted as a *computational* route: the structured pilot expanded
only the 24 top pivots and produced 668 rows with 9,967,234 terms, the
largest row 76,969 terms at semantic degree 5, against the original complete
export's 30,218-term maximum at degree 4. This is the fill-in law my blind
Card 2 predicted from R005, and it trips Sol's own blind stop rule
("projected fill exceeds about 3.8M terms ⇒ stop elimination"). So the
mechanism survives only in the form Opus and I both proposed: the
triangular DAG is a per-point oracle (exact rational or numerical), never a
symbolic Schur complement.

## 2. Strongest refuted or overstated inference

**Opus Card 2, "the T2/T3 chart is dominated on both sides."** The
containment `π(V(I)) ⊆ V(Jphys)` is fine, and existence is easier in the
larger locus. But for unit search the logic runs the other way: `I`
carries strictly more rows (localizers, T2/T3 leaders), so `1 ∈ I` is at
most as hard as `1 ∈ Jphys`, never harder. Redesigning `.103` on that
premise would be a decision built on a reversed inequality; the packet's
"inclusion alone does NOT establish computational dominance" is correct.

Runner-up, same report: Card 1(b) claims a *proved* uniform bound
`rank A ≥ 188` for the 1,468 positive-row matrix `A`, via
`ker A = V ∩ ker J(·,G)`. That identity is false: the positive-only kernel
is `{P ∈ V : J(P,G) ∈ k}`, and `J(X, X^2+W)=1` shows the gap. The
measurement (rank 191 at two modular points, sound direction) stands; the
"everywhere" and "C rigidly determined everywhere" wording is unproved by
that argument. A report cannot repair this retroactively; but see §4 for
what the post-cutoff theorem does license.

Against my own blind: (i) "rank-drop locus is *exactly* Ritt
decomposability" is overstated. Rank drop ⇒ `G=φ(R)` holds; the converse
needs the primitive `R` inside `V_C ⊕ k·h`, which is generally false. (ii)
OPEN[PHYSJ-GRADING] is answered NEGATIVE by the source: the fixed `-8/3` at
`h3(4,5)` and the fixed X-coefficient 1 in `C3` are inhomogeneous under any
positive weight with `w(h_{rz})=r`. The `J_0=1` dehomogenised chart and the
six gauge slices are therefore not licensed; keep `Zj·J0-1`. (iii) Every
per-iteration cost in my Card 1 is an estimate; nothing was measured.

Sol Card 1 (constructible source atlas) and the coordinator's necessity
obligation are the same missing theorem restated as a discipline; neither
supplies a map (packet Q5). Not refuted, but not a mechanism.

## 3. One concrete composition of peers' ideas

**DAG-as-oracle, reduced-space probe, exact acceptance.** Take the filtered
pilot's 189-pivot reconstruction graph (Astra, post-cutoff; 42,320 abstract
terms, 188 lower-`G` coefficients) as the evaluator: at any base point
`(h3,C2,C3,B2,a,b)` over a field, the graph solves 189 C coordinates by
back-substitution in microseconds; the remaining 1,279 previously nonzero
positive rows plus `Zj·J0-1` are the residual. Opus's per-point rank test
becomes "residual vanishes", with no rank computation. My Levenberg–Marquardt
probe then runs on the 250-coordinate space `(247 base, v22, v11, Zj)`
instead of 439 or 600, with the same acceptance contract (exact evaluation
of every original row in a nonzero `Q[T]/(H)`). Sol's occurrence and
constant-slot controls become the instrument's negative controls. Nothing
here expands anything; the structured-pilot wall is not touched.

## 4. Independent attack on the transverse-line theorem and the 190-pivot lemma

**Full-map theorem: holds at scope.** Chain checked: `J(P,G)=0`, `P`
nonconstant ⇒ `G=φ(R)`, `P=ψ(R)`; `W=0` gives `deg φ·deg_X R(X,0)=2`;
`deg φ=1` forces `deg P ≥ 66`; `deg φ=2` forces `deg R=33`, `ψ` linear,
`R_top^2 ∝ H^6 ⇒ R_top ∝ (X+W)^9W^24`, whose `W^33` coefficient is nonzero
while the source has none. My control confirms both literal inputs
(`h(X,0)=X+c`; degree-33 W-exponents 24–32). Over a non-closed field the
AP lemma is used fibrewise on geometric points, which is all properness needs;
the descent remark is unnecessary rather than wrong. The Fitting-ideal
globalisation (`I_191(M)=A` ⇒ split injectivity after any base change,
nonreduced included) is correct and is the only statement that survives
nonreduced limits. It buys no constant minor and no cheap left inverse; the
`(t,1-t)` example is the right warning.

**Positive-only distinction, sharpened.** Let `K⁺={P∈V_C: J(P,G)∈k}`. The
map `P↦J(P,G)` on `K⁺` is linear to `k` with kernel `k·1`, so
`dim K⁺ ≤ 2` everywhere: the positive-only C-block has rank `≥190` at every
base point, better than 188 and independent of Opus's argument. Rank 190
needs `P∈V_C` with `J(P,G)=1`, i.e. a Keller pair of degrees `(≤35,66)`;
by Moh's `≤100` theorem it is an automorphism, so `G` is a coordinate, and
then no `F` of degree 99 can be Keller with `G` (`99∤66`, `66∤99`). Hence the
rank-190 locus is disjoint from the Keller locus, matching the producer's
conditional statement without assuming a Keller point. Desk-only, ungated;
it needs a different-model check of the two classical citations.

**(C,a) block.** The `D=b=0`, `P=h` example is a genuine full-map kernel
vector, so no uniform 193-column statement exists. Correct as stated.

**190-pivot lemma: sound, but not an elimination advance.** Ordering columns
by minimum W-order `r` then decreasing X-degree, the pivot at row
`(i+1,r-1)` is `-2r·(leading coefficient of p_r)`; later columns cannot
reach that row, and same-`r` later columns have smaller X-degree. Lower
triangular with constant diagonal: correct. Three limits. (a) It pivots on
the *lowest* rows, whose off-diagonal entries are the densest base
polynomials; substituting upward into degree-99 rows is the same fill-in
mechanism the structured pilot measured downward. (b) It cannot be added to
the 189: both eliminate the same `V_C/(k·1)` up to two directions, so at
most 191 columns go in total. (c) Its rows are positive-degree, but it says
nothing about the residual column's constant entry, and the theorem
guarantees only a unit ideal, not a unit entry. Verdict: two valid
certificates, zero measured runtime; not a substitute for a dedicated
source/code gate.

## 5. Re-ranked bottlenecks

Proof: (1) uniform exclusion of an infinite admissible family (K16
`b·B_m·η_m≠0` on all `m≥4`, plus the `b=0` boundary); (2) source-to-stage-8
necessity, still GAP; (3) fixed-degree receiver decisions, now measured to
be elimination-bound, not build-bound; (4) Moh ℓ-shift completeness.
Unchanged from my blind; nothing this round touched (1) or (2).
[POST-CUTOFF] The K16 boundary gate confirms the pole lemma as
rational-to-polynomial only and shows the `t`-model is σ-anti-invariant, so
it carries exactly the `x`-line residual plus `M|Q` and no new equation. By
the coordinator's own Card 3 stop rule (leading balance, residue balance
equal to UT ⇒ STOP), the rational/norm mechanism is a STOP outcome.

Disproof: (1) no candidate point and no instrument yet calibrated; (2)
decision of the physical locus is elimination-bound: exact-Q slimgb timed
out at 600 s / 33.29 GiB with no basis, msolve crashed before F4 on a proved
32-bit `calloc` count overflow (`11,299,180·600` wraps to `2,484,540,704`;
I re-multiplied); (3) representation cost demoted, as Opus said and the
137 s build shows.

Mechanism verdict: **NO_NEW_MECHANISM** on the proof side. On the disproof
side one instrument and one composition (§3), no theorem.

## 6. Cheapest discriminating experiment

**Allocation-safe modular parser, then one capped F4 on the complete input.**
Assumptions: the two `calloc` products in `iofiles.c` are the only
sub-`2^32` sites left after the two existing patches (the pilot says no such
claim is made, so the patch must also review the remaining count products);
the modular input `5a7f6743…` is already all-row audited (1,629/1,629 rows,
11,299,180/11,299,180 terms). Measured costs: build 54.7 s, prepare 28.2 s,
audit 19.8 s. Estimated: a third patch of about ten lines and one review,
under 30 minutes; the run itself 600 s / 96 GiB, not launched here. Negative
control: the old 449-variable input must still parse and reproduce its
earlier F4 table. Interpretation: a modular unit or modular basis is a
signal only in both directions; the payload is the first per-degree F4
matrix table on the complete family, which is the missing "decision
hardness" measurement the coordinator's Card 1 wanted. Stop: crash again,
or matrix rows exceeding the class-A ceiling (degree 7, 3–9 M rows) before
degree 5, or the wall. Positive-only `J`, `J0=1`, or dropped `C` inputs
are forbidden.

This ranks above the W-filtration circuit (it changes nothing without
expansion, and expansion is refuted) and above numerical calibration
(cheap, but it discriminates the instrument, not the mathematics). It
ranks above any K16 all-degree obstruction only because none is on offer.
What could change the ranking: bounded F4 growth through degree 6 would
move fixed-degree decisions back to feasible; a converging numerical start
would move the disproof side to the top of everything.

**Q4, numerical controls (design only, unmeasured).** (i) Known target: draw
a rational base point `s*`, evaluate `J(F,G)(s*)` through the DAG, and
demand that 10 random starts on the residual `J(F,G)-J(s*)` reach `<1e-12`
with a quadratic tail from at least three; failure means instrument bug.
(ii) Zero-J escape: start at `ρ=1`, rest 0; `Zj` must diverge and the
positive residual must stay zero, so the inverse row is the only thing
rejecting the vertex. (iii) Precision: the residual at `s*` in double and
in 50-digit arithmetic must agree to `1e-10`; otherwise the probe reports
noise as convergence. Each control is at most 10 starts × 200 iterations;
seconds per iteration are unmeasured until (i) runs. Only after (i)–(iii)
pass is the 200-start probe a lane, and its negative outcome is never
evidence.

## 7. Systems upgrade

One choice: the **audit-heading index** (read-only, about 15 minutes). It is
the only candidate whose failure mode was measured this round: the grammar
drift from `## INTEGRATION #17 DELTA (id)` to `### 17(id) — time — title`
made an old-grammar reader report 02:51Z as newest and drop every promotion
since 09:35Z. Risk: none. Astra's harvest catch-up addresses a real gap
(two harvests due Sep 7 04:26Z) but needs a scheduler the coordinator says
is not exposed, and any process-adjacent action carries custody risk. Sol's
contract checker guards a failure that did not occur (all five bodies were
well formed). Mathematical opportunity cost of the index: negligible.

## 8. Continue / redesign / stop

- `.63`, `.73` capped solves: **continue** to caps, no extension; subset
  unit is a full-chart unit, nonunit/timeout has no force.
- `.103` 2 TB T2/T3 build [POST-CUTOFF operator-stopped after ~142 min,
  no row progress since 08:52]: **stop** further stages on that
  representation; keep partials. Not because it is "dominated" (§2) but
  because it never produced rows.
- Physical family exact solve: **redesign** to the modular parser repair
  of §6; no Q slimgb rerun.
- Linear-C expansion (189 or 190 pivots): **stop** expansion; **continue**
  the DAG as an evaluator only (§3).
- Numerical probe: **start** controls only, after §6.
- K16 boundary: **continue** the product target; the norm/rational route
  is a STOP outcome; queue the follow-on blind round as the packet says.
- R005, R050, Ni/relative-rank, degree-estimate lane: **stop** (the
  degree-estimate interface reproduces the 145/227 endpoint exactly).
- Necessity ledger (my blind Card 3): **start** as desk work; it decides
  whether any unit is a configuration kill.

## OPENS RAISED

- OPEN[POSITIVE-C-RANK-190-LOCUS] — QUANTITY: the number of base points of
  the frozen family at which some `P∈V_C` has `J(P,G)=1` `= 0` (target), or
  a witness `(P,G)` with `G` a coordinate. CHEAPEST TEST: 20-minute desk
  gate of §4's two citations (Moh `≤100`, JvdK divisibility) followed by
  the degree-11 and degree-22 mate identities `G=φ(P)+lower` against the
  actual `B11=H`, `B22` basis polynomials.
- OPEN[MSOLVE-COUNT-OVERFLOW-COMPLETE] — QUANTITY: the number of remaining
  sub-`2^32` count products in the pinned msolve after a third patch `= 0`.
  CHEAPEST TEST: grep every `calloc`/`malloc` size expression in
  `iofiles.c` and `neogb/io.c`, type each operand, 30 minutes desk.

Labels: §3 composition NEW at instrument level, KNOWN methodology; §4
sharpening NEW, ungated; everything else KNOWN or DUPLICATE as merged in
§1. FALLACY-v2: no exit-price assertion, hence no `charge_basis` line; no
floor read as attainment; ring `X=x`, `W=y-x` declared; no `sat()`, no raw
remainder, no pole identity used; all quantifiers fixed-degree unless
stated.

<!-- BODY-END -->
