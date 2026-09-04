# Ideation round 20260904T0000Z — blind submission (Opus 5, research seat)

Lane `ideation-20260904T0000Z-opus5`, basis `ce00e907`, written 2026-09-04 between
08:25Z and the round deadline. Blind: no `ideation-20260904T0000Z-*` file other than
the charged packet was read; no in-progress lane report was opened (the four
`.run.v2` receipts of `g108-delta3-kill-gate-gpt55`, `g9966-chart-necessity-opus5`,
`k16-square-resultant-fable5`, `row2515-order-gate-sol56` were checked and all four
carry `initial_status=RUNNING` with no `final_status`). No canonical ledger was
edited; `jc2-lean` was not touched. FALLACY-v2 applies throughout. No new exit-price
assertion is made, so no `charge_basis` line is due.

## 0. Custody

The receipt `xmodel/ideation-20260904T0000Z-opus5.run.v2` was parsed with a single
`awk -F=` program pairing its `charged_input_<i>_sha256=` and
`charged_input_<i>_basename=` lines into `/tmp/manifest.sha256`, then checked with
`sha256sum -c`. **4/4 OK**, no digit retyped:

```text
ideation-20260904T0000Z-packet.md      OK
ideation-20260903T1200Z-synthesis.md   OK
FALLACY-v2.md                          OK
COORDINATION.md                        OK
```

Banked reports read (all `final_status=DONE`): `k16-toptail-quadratics-fable5`,
`k16-hilbert-regseq-sol56`, `k16-chain-gate-grok46` (head), `order-chart-general-gpt55`
(head), `g108-joint-band-sol56` (head), plus AUDIT deltas 17(ll), (aaaa), (uuu), (vvv),
(jjjj), (iiii), (tttt)–(ccccc), the newest `LIVE STATE` (2026-09-04T08:22Z), and the
current `APPROACHES.md` overlay stack. One primary-source read: Moh 1983, printed
p. 208 (PDF page 69) as an image.

## 1. Verdict, up front

```text
V1  PROVED-HERE (identification, exact).  Sol's t-row tail
    J_t^tail = <T_(t,t),...,T_(t,2t-1)> and Fable's Lemma SQUARE act on the SAME
    t rows: R_r = Res_b3(T_(t,2t-1), T_(t,2t-1-r)), r=1..t-1, is the b3-elimination
    of J_t^tail.  The implication runs one way only — V(R)={0} => V(J^tail)={0},
    not conversely — so 17(wwww)'s target is STRICTLY STRONGER than 17(vvvv)'s, and
    the round should merge the two deltas onto the weaker (hsop) target.
V2  PROVED-HERE (exact, verified against the four measured lengths).  The
    complete-intersection length of the square tail is
        L_t = prod_(d=2t+2)^(3t+1) d / ((t-1)! (t+1)) = 2*binom(3t+1, t-1),
    i.e. 90, 572, 3640, 23256, 149226, 961400 at t = 3..8 — exactly Sol's
    measured lengths at t = 3,4,5,6.  The "t/(t+1) binom(3t+1,t)" form is the
    same number; the binomial form is the one a combinatorial proof would target.
V3  MEASURED/PROVED-HERE (counting).  The Bezout number of Fable's resultant
    system is B_t = 2^(t-2) * L_t (exact identity, checked t = 3..12).  The
    b3-elimination therefore INFLATES the intersection count by 2^(t-2), which is
    the arithmetic reason Fable measured the resultant route to be more expensive
    than the direct chart.  Res_w(R_1..R_(t-1)) has total degree ~7.4e5 in the
    coefficients of the R_r at t = 7 and ~9.9e6 at t = 8.
V4  ANSWER to revised Q1 (typed NO, with a replacement).  Res_w(R_1..R_(t-1)) is
    NOT computable in closed form in t, and it is the wrong object: it carries a
    factor 2^(t-2) of pure elimination waste, its existence as a weighted
    resultant needs hypotheses on (d_r, w_j) that are not checked in 17(wwww),
    and its content is carried without loss by the hsop/length statement V2.
    THE UNIFORM TARGET SHOULD BE: "T_(t,t..2t-1) is a homogeneous system of
    parameters for every t >= 3", certified by length = 2*binom(3t+1,t-1).
V5  FRAMING CORRECTION.  The packet sets the uniform K16 target as (V0).  (V0) is
    strictly stronger than what (T) needs (the ledger knows this: 17(mmmm)
    "tau-criterion strictly weaker"), and (V0) is FALSE on the one fibre where the
    two have ever been separated (t = 2, y = 1/5: dim I_(2,+) = 1, (8.1) holds).
    A failure of (V0) at some t >= 8 must not be read as a failure of (T).
V6  PROVED-HERE (source read, closes a flagged GAP).  GAP[MOH p.208 (16,12)
    CALIBRATION] (17(tttt): "chart absent from the PDF text layer") closes
    POSITIVE by image; printed p. 208 reads
        gbar = h^4 + a1 h^3 + a2 h^2 + a3 h + a4,   fbar = h^3 + B2 h + B3,
        h(x,y) = y^3(y-x) + b1 y^3 + b2 y^2 + b3 y + b4 = yA + b4 = y^2 B + b3 y + b4,
        h = the fourth approximate root of fbar,  deg_y a_i, B_i <= 3,
        ord a_i(sigma) >= -i/4,  ord h(sigma) >= -1/4,  17 coefficients.
    CONSEQUENCE (new connection): b3, b4 (and the eliminated b2, b1) ARE Moh's
    h-tower coefficients, and the K16 ray at parameter t is Moh's p. 208 chart
    with (deg_h gbar, deg_h fbar) = (3t+1, 2t+1) in place of (4,3) — exactly
    Sol's constant q = 2t+1.  The K16 terminal cone is the coefficient system of
    an APPROXIMATE-ROOT TOWER (Avenue 6), not a generic overdetermined system.
V7  STRATEGIC (my strongest disagreement with the round's framing).  (V0)-for-all-t
    should be DEMOTED from flagship to method prototype.  Even if proved it kills
    one family: 17(ll) types the K = 16 ray as "the ONLY KNOWN cofinal family",
    not the only one, so the screened census does not become finite.  The
    flagship should be the u_s >= 2 half, whose target theorem I name MINOR-EMPTY
    in Sec. 6 and which now has three clients and an engine.
```

Nothing above is promoted by me; V1–V3 and V6 are exact and replayable, V4–V5 and
V7 are judgements with stated evidence.

## 2. Disposition vector (changes only)

| avenue / live row | disposition | reason |
|---|---|---|
| MINOR-DICHOTOMY (u_s > 1; overlay 2026-09-03T16:36Z, "co-principal with (T)") | **RAISE to sole principal proof row** | four clients emptied in a day by one method; the stratum no screen or descent reaches (296 rows / 166 groups at D ≤ 200); the only live row with an engine. |
| Row 1 (GGV corner / monomial-Jacobian receiver; the u_s = 1 half) | **unchanged as principal, RETYPE** | it is one half of a dichotomy, not the programme; its only known cofinal client is the K = 16 ray; its stated uniform target (V0) is over-strong (V5). |
| K = 16 ray / theorem (T) as a *flagship* | **LOWER** (keep as prototype + regression client) | 17(ll) types it "the ONLY KNOWN cofinal family": killing it does not finitise the census, and the 20260903T1200Z synthesis already says a t-uniform obstruction "is not JC2". Fixed-t Gröbner is exhausted at t = 7 and both structural routes stalled on the same open condition. |
| Row 6 (Abhyankar–Moh one-place / approximate roots) | **RAISE** | V6: the terminal system IS the coefficient system of Moh's approximate-root tower. Approximate-root/semigroup theory, not commutative-algebra genericity, is its native language. The round's new connection. |
| Row 36 (guided counterexample search) | **RETARGET** (not lower) | move the disproof side off the u_s > 1 stratum (4/4 empty; the order chart returns SATURATED-EMPTY generically) onto the ten OPEN two-point s_eff = 2, u_s = 1 rows at D ≤ 200 (17(bbbb)), where freedom grows and no chart has closed. |
| Rows 25 / 27 / 28 / 32 | unchanged | untouched by this round's evidence. |

No avenue is reopened and none is closed: nothing was refuted this round that was not
already typed dead.

## 3. Q1 — the K = 16 uniform statement

### 3.1 The two "square" theorems are one theorem

Sol (17(vvvv)) refuted the literal Proposal A and proposed the repair
`J_t^tail = <T_(t,t),...,T_(t,2t-1)>`: **t** forms of weighted degrees
`3t+1, 3t, ..., 2t+2` in the **t** variables `b4, q_(2,0),...,q_(t-1,0), b3` of
weights `1, 2, ..., t-1, t+1` (variable count `1 + (t-2) + 1 = t`, valid for
`t >= 2`). Fable (17(wwww)) took the *top tail* `k = t..2t-1` — **the same t rows** —
and eliminated `b3` using `lc_b3 T_(t,2t-1) = alpha_t`, a unit, producing
`R_r = Res_b3(T_(t,2t-1), T_(t,2t-1-r))`, `r = 1..t-1`.

These act on the same object, and the implications run ONE way (Fable §5.2 is explicit
that the converse fails: a point of `V(R)` may have the shared `b3`-root differ from row
to row, and with `t-1` rows against the two roots of `Q_0` there is no pigeonhole):

```text
V(R_1,...,R_(t-1)) = {0}  =>  V(J_t^tail) = {0}   [Fable, Lemma SQUARE]
                          =>  V(I_(t,+)) = {0}    [J_t^tail subset I_(t,+)]
                          =>  (V0) => (8.1) => (T),
and NOT conversely: V(R) can be strictly larger than the image of V(J_t^tail).
```

So Fable's resultant target is **strictly stronger** than Sol's hsop target, and the
excess is measured exactly by the `2^(t-2)` factor below.

The two lanes therefore verified the *same* statement at overlapping indices by two
instruments — Sol by length (`t = 3,4` exact; `5,6` modular + properness + CM), Fable by
resultant (`t = 3` exact; `4,5` modular). That is corroboration, not two routes: the
synthesis should merge 17(vvvv) and 17(wwww) into one delta with one target. It also
explains quantitatively why Fable measured the elimination as *slower* than the direct
chart:

```text
Bezout(tail)      = prod(degrees)/prod(weights) = L_t
Bezout(resultant) = prod_(r=1)^(t-1)(4t+4+2r) / (t-1)! = 2^(t-2) * L_t   (exact)
```

checked at `t = 3..12`: `B_t/L_t = 2, 4, 8, 16, 32, 64, ...`. Eliminating `b3` throws
away nothing and multiplies the intersection count by `2^(t-2)`; every excess unit is
a spurious root of the two quadratics that is not a root of the pair.

### 3.2 Revised Q1, answered: the resultant is the wrong uniform object

The revised question asks whether `Res_w(R_1,...,R_(t-1)) in A_t` has a closed form in
`t`. Typed answer: **NO, and it should not be asked.** Four independent reasons.

1. **Size.** `Res_w` has total degree `sum_r B_t/D_r` (`D_r = 4t+4+2r`) in the
   coefficients of the `R_r`: `19, 287, 4041, 5.5e4, 7.4e5, 9.9e6` at `t = 3..8`, while
   the `R_r` already carry `1904..5402` terms at `t = 7` (Fable §5.1). No closed form in
   `t` is reachable by any Macaulay-matrix construction at desk scale, and no standard
   closed-form family (Sylvester, Dixon, Morley–Coble) applies to a weighted system with
   `t-1` distinct weights.
2. **Waste.** By V3 the resultant carries a factor `2^(t-2)` of pure elimination excess:
   a closed form for it is a closed form for `L_t` times one for the spurious roots.
3. **Strictly stronger than needed.** `V(R) = {0}` implies, and is not implied by,
   `V(J_t^tail) = {0}` (§3.1). Aiming at `Res_w != 0` is aiming past the target.
4. **Well-definedness.** The criterion `Res = 0 <=> common zero in P(w)` requires
   hypotheses on `(d_r, w_j)` that 17(wwww) does not check. `P(1,2,...,t-1)` is well
   formed, but the vanishing criterion still needs a citation. **This is a FALLACY-v2
   "variable/ring map" hazard: the object is named, its defining theorem is not.** The
   hsop formulation needs no such citation — it is Krull dimension.

**Replacement target (this is my answer to Q1).**

```text
UNIFORM TARGET (SQUARE-TAIL).  For every t >= 3 the t weighted forms
T_(t,t),...,T_(t,2t-1) are a homogeneous system of parameters in
S_t = A_t[b4,q_(2,0),..,q_(t-1,0),b3];  equivalently
      dim_(A_t) S_t/J_t^tail = L_t = 2*binom(3t+1, t-1) < infinity.
This implies (V0), hence (8.1), hence (T), for every t >= 3.
NEGATIVE CONTROL: it must FAIL at t = 2, y = 1/5, where dim I_(2,+) = 1.
```

Verified: `L_3 = 90`, `L_4 = 572`, `L_5 = 3640`, `L_6 = 23256` — the four lengths Sol
measured, exactly. `L_7 = 149226`, `L_8 = 961400` are the predictions.

Why this is the better object: it is a **Krull-dimension** statement (no resultant
theory), it is **square** (Koszul-resolved, so its Hilbert series is forced once
`dim = 0`), it has a **binomial closed form** (so a standard-monomial/lattice-path
proof is conceivable), and it makes the Hilbert-driven Gröbner engine usable — see
Card A. The Fröberg statement Sol conjectures for the *full* cone
(`66, 338, 1709, 8621, 43133`) is a strictly harder, genericity-flavoured statement
and should be demoted to a diagnostic; the CI statement for the tail is the one with
a proof shape.

### 3.3 Why every degeneration argument has failed, stated exactly

Fable's §5.3 obstruction is correct and it is more general than its statement. Let
`J` be any of the chart ideals `I_(t,+)|_(x_i=1)`. For a weighted form `f`,
`in_top(f|_(x_i=1)) = f|_(x_i=0)` when the latter is nonzero, so

```text
<in_top(generators of J)> = I_(t,+)|_(x_i=0),
and  dim <in_top(gens)> = 0  <=>  V(J) FINITE,  never  V(J) = empty.
```

Emptiness is `1 in in_top(J)`, and `in_top(J)` is not computable from the generators
— the gap between `<in_top(gens)>` and `in_top(J)` is exactly the non-Koszul syzygies.
So: **RESIDUAL-ZERO, the top-weight test, the b3-axis and b4-axis theorems, the
sub-chart chain steps, and the Hilbert-series termination all live on the wrong side
of a single wall.** They collectively prove that `V(I_(t,+))` is a finite union of
weighted lines, every one of which misses `{b4 = 0}` and misses each axis; they cannot
prove there are none. 17(llll)'s conclusion ("the axis route cannot give
`b4 in sqrt I`") is this wall, and it applies verbatim to every variable, not only
`b4`. Any future proposal that computes an initial ideal *from the generators* is dead
on arrival; this should be a standing screen on K16 lane designs.

What survives the wall: (i) a genuine standard basis (Gröbner), exhausted at `t = 7`;
(ii) an explicit Nullstellensatz certificate `x_i^(N_i) = sum_k h_(i,k) T_(t,k)` with
indexed `h`; (iii) a **length** identity, because for a square system finiteness and
the CI length are equivalent to `V = {0}` and the length is computable by a *guided*
Gröbner run that never has to discover the Hilbert function. Route (iii) is Card A.

### 3.4 Pricing the packet's four routes, plus one

**(a) Induction in `t`.** Blocked where nobody has said it is blocked: the coefficient
ring changes with `t`. `A_t = Q[d]/(3d^2-(t+1))`, so there is no `Q`-algebra map
`A_(t+1) -> A_t`, and the variable count grows. The repair — and this is worth banking
independently of induction — is to **reparameterise the ray by `d`**: every banked
closed form (`alpha_t`, `b_j`, `d_j`, `n_j`, `dq_j`, `nq_j`, `p_(b2)`) is a rational
function of `(t, j, y)` reduced modulo `H_t`, i.e. of the form `P(t) + Q(t) d` with
`3d^2 = t+1`. Hence

```text
u in A_t is a unit  <=>  N(t) := P(t)^2 - Q(t)^2 (t+1)/3 != 0,
```

a ONE-VARIABLE rational function of `t`; "unit for every t >= 3" is the decidable
statement "the numerator of `N` has no integer root >= 3". The campaign already works
this way informally (17(uuu): "every pivot norm ... a nonzero polynomial in `t` with
no positive-integer root"). It should be a typed artifact: a `unit_in_At` certificate
`(P, Q, N, integer_roots)`. *Cheapest decisive test of (a) itself:* on the banked
indexed form of `T_(t,k)` (17(iiii) §2, the w-picture), set `q_(t,0) = 0` in the
`t+1` system and ask whether the resulting coefficient arrays are the `t` arrays with
`t -> t+1` in the coefficient field. Symbolic, no Gröbner, ~1 lane-hour on records
already banked at `t = 3,4,5`. If a restriction map exists, induction is live and the
whole problem may collapse; if not, route (a) is dead and should be typed so. **This
test has never been run and is the cheapest live item on the K16 board.** (Card C.)

**(b) Hilbert series / regular sequence.** This is the surviving route, in the
sharpened form SQUARE-TAIL of §3.2. Sol's own framing (the *full* `2t-1` rows,
weighted Fröberg) is the harder statement; the tail is square and its series is forced.
*Cheapest decisive test:* Hilbert-driven `std` on the **tail only** at `t = 7`, mod a
good prime, with the conjectured numerator `prod_(d=2t+2)^(3t+1)(1-s^d)` supplied. See
Card A for the mandatory controls — a Hilbert-driven `std` with a wrong series returns
a wrong basis *silently*, which is a FALLACY-v2 hazard of exactly the kind this
campaign exists to avoid.

**(c) Monomial order / initial ideal.** Refuted as a *pattern* at `t = 7` (17(mmmm))
and, by §3.3, structurally incapable of reaching the open condition unless it is a
genuine standard basis. One measured datum is nevertheless now *explained*: the `b4`
pure-power exponent `2t+2` (8, 10, 12, 14, 16 at `t = 3..7`) is just
`wt T_(t,2t-1) = 2t+2` — in `wp(1,2,..,t-1,t+1)` with reverse-lex tie-break the lowest
row's leading monomial is `b4^(2t+2)` precisely because that row's `b4`-axis value is a
unit (17(llll)). So Sol's `b4` column is a theorem; the other columns are not, and Sol
is right to refuse to smooth them. PRICE: do not fund (c) further.

**(d) Cohomological / deformation reading.** I looked for a tangent–obstruction
structure and found nothing beyond a renaming: `I_(t,+)` is the ideal of obstructions to
lifting Moh's Theorem-1.2 expansion, but there is no ambient deformation functor whose
`H^1` it is — the thing being deformed is a chart normalisation, not a scheme. PRICE:
unfundable until someone writes the functor down. *But* V6 supplies the reading (d) was
groping for: the tower is an **approximate-root** tower, so the right structural theory
is Abhyankar–Moh semigroup theory (Avenue 6), and that is where an indexed certificate
would come from.

**(e) NEW — the target is over-strong; carry the weaker one.** `(T)` needs
`tau_t in sqrt(I_(t,+))` (Lemma CONE), not `(V0)`. The two have been separated exactly
once — `t = 2, y = 1/5` — and there `(V0)` is FALSE while `(8.1)` holds, because
`tau_t` vanishes on the `b3`-axis, which is the whole cone there. For `t >= 3` the
`b3`-axis theorem excludes that failure mode, which is the campaign's (reasonable)
ground for expecting `(V0)`. My point is procedural and load-bearing: **if the
SQUARE-TAIL test returns `dim > 0` at some `t >= 8`, that refutes `(V0)`, not `(T)`,
and the campaign must already have the `tau`-criterion instrument in place** so that
the day is not lost. Cost of holding it: one line in the lane design.

## 4. Q2 — (99,66): hostile scrutiny of the two kills, and what the engine implies

The packet's original Q2(a) ("predict whether the dimension reaches 0") is answered by
events: it did, at stage 8, residue 64. Q2(b)/(c) are moot. The live question is the
one the addendum names: the kills are PROMOTED **conditional on chart necessity and
split exhaustiveness**. I attack those two, hardest first.

### 4.1 The five places the (99,66) verdict can still fail

**(H1) The gauge is used at two points; the automorphism control is single-point.**
17(aaaa)(1) types the chart's normalisation as "a gauge, not a degree swap": the minor
line goes to `y = 0` where Moh's (8) puts the major line. But a joint chart uses ONE
coordinate system for BOTH points at infinity, and a normalisation free at the major
point need not be free at the minor point — the residual group after fixing the major
gauge may be strictly smaller than the one the minor rows assume. This is the campaign's
own standing lesson (no two-point automorphism above degree 1; the control pair
`F = x + y^6`, `G = y + (x + y^6)^6` collapses the Keller–Jacobian slots to one).
**Dossier obligation: exhibit one group element realising both declared normalisations
simultaneously, compute the residual stabiliser, and show the declared free coefficients
are exactly its orbit space.** Until that exists, "necessary chart" is a claim about two
charts not proved compatible. It is the most dangerous line in the dossier and the
cheapest to settle.

**(H2) The only end-to-end kill control is modular.** 17(aaaa)(5): the `(16,12)`
calibration was replayed over `GF(32003)` (77 rows, both `c5` readings `[1]`), while the
*survival* control (the tame automorphism) is over `Q`. That is the wrong way round for
an instrument whose output is a unit ideal. The two (99,66) verdicts are themselves over
`Q` (6264, 64; char-0 replay; `dim -1`), so this does not touch them, but it leaves the
engine uncalibrated in char 0. Cheapest fix: rerun `(16,12)` over `Q` — minutes.
Raised as `OPEN[ENGINE-CHAR0-CALIBRATION]`.

**(H3) The `c != 0` / `J_0 != 0` localisations.** Both kills are certified *after*
localising (Rabinowitsch `Zc*c - 1`, and localisation at `J_0`). FALLACY-v2's `sat()`
and pole/interior items apply: the dossier must source `c != 0` and `J_0 != 0` as
NECESSARY, not convenient. If `c = 0` is admissible the chart is a proper subset of the
necessary conditions and the kill is a kill of a sub-case. I expect this is fine (`c`
is a leading coefficient), but it must be a cited line, not a convention.

**(H4) The split ceiling.** Exhaustiveness rests on `delta in {2, 5/2}` from Prop 6.1
with the ceiling `delta < 8/3`. Prop 6.1 must be read in the MINOR normalisation
(`V_r = u_s`), giving `ord g = (n/d_s)(u_s*delta - v_s)` and the ceiling
`delta < v_s/u_s`; with `u_3 = 3` that means `v_s = 8`, which is `V + 1` for
`V = (7,7)`. **Dossier obligation: display the derivation of `v_s = 8` from the row
data, in the minor reading, with the p. 202 major reading explicitly not used.** This
is a place where a plausible-looking off-by-one changes the admissible `delta` set and
therefore the completeness of the classification.

**(H5) The p. 208/209 calibration text.** Closed positive by this report (V6): the
`(16,12)` chart is on printed p. 208 and I have read it. It also settles a related
worry: Moh's own sentence there — "Similar arguments can be applied to the second case
to show the impossibility directly and to the third case to reduce the number of
coefficients to 22 [15 or 13]" — is the p. 209 case split that 17(pppp) promoted as
mechanically complete, and it is consistent with what the gate found.

Net: I do not believe the (99,66) verdict is wrong. I believe (H1) is the one item
that could turn "the declared chart is empty" into something weaker than "no Keller
pair has this skeleton", and it is a one-page obligation, not a research programme.

### 4.2 What the engine's success does and does not imply

It implies **method**, not theorem. Three clients, three *different* killing row
families:

| client | killing family | stage | certificate |
|---|---|---|---|
| (99,66) δ = 2 | Jacobian degree-159 row | 4 | 6264 (unit) |
| (99,66) δ = 5/2 | pole/Jacobian degree-155 rows, joint `Q*` | 8 | 64 (unit) |
| D = 108 δ = 3 | common-`h3` minor incidence | 0 (preflight) | localised unit |
| (25,15) | Theorem-1.2 order rows alone (no Jacobian) | order chart | SATURATED-EMPTY / Q |

The (99,66) *schedule* transfers to nothing: at D = 108 the kill happens before the
schedule starts, and at (25,15) it happens in a strictly weaker instrument. So the
correct reading of the day is: **the joint chart is over-determined for every client,
but which rows do the work is datum-dependent**, and a uniform theorem must be about
the *reason* the chart is over-determined, not about a schedule. That reason is my
Card B (SHARED-LEADER).

## 5. Q3 (revised) — the minimal necessity dossier, and the row families the two new kills need

### 5.1 The dossier, as nine sourced statements

The dossier is not prose about (99,66); it is a template with a row per obligation,
instantiated per client. Minimal set (each line must cite Moh/Xu, not a validator):

```text
D1 SKELETON      the row's (M, V, d, u_s, N) data are forced for a Keller pair of
                 those degrees                                    [Moh §5-6; census]
D2 SPLIT-EXH     the admissible (delta, partition) list is complete, in the MINOR
                 reading of Prop 6.1, with the ceiling derived    [Prop 6.1; (H4)]
D3 GAUGE         one coordinate change realises BOTH declared normalisations; the
                 residual stabiliser is computed; the declared free coefficients are
                 exactly its orbit space                          [(H1) — the hard one]
D4 OUTER BANDS   Theorem 1.2 at the major point yields the declared D2/D1 rows as a
                 necessary PREFIX (order bounds, not equalities)  [Moh Thm 1.2]
D5 INCIDENCE     the packets of the split share the declared tower coefficients
                 (common h3), necessarily                         [split datum]
D6 POLE ROWS     each declared pole/order row is necessary        [Moh (8), p.209]
D7 JACOBIAN      the graded expansion of F_x G_y - F_y G_x = 1 in the chart, and the
                 truncation used, are a necessary prefix          [Keller]
D8 LOCALISATION  c != 0 and J_0 != 0 are necessary, not conventions  [(H3)]
D9 CERTIFICATE   the exhibited unit combination is exact over Q and independently
                 replayed                                         [banked for (99,66)]
```

`D1, D2, D4, D6, D7, D9` are banked for (99,66) (17(aaaa), 17(tttt)); `D3` and `D8` are
the residue; `D5` exists only as a computation. **The dossier is two pages, not a
programme — and it is the difference between "the chart is empty" and a theorem about
Keller pairs.** I would not launch another client before `D3` is written once: it is the
only obligation shared by every client, and it could invalidate all of them at once.

### 5.2 Which row families the D = 108 and (25,15) kills need

**D = 108 (δ = 3).** The kill is `D5` alone, at preflight. Its dossier needs exactly
one new derivation: *why the two 12-packets of the `[1,1]` split share `h3`*. That is
a statement about the principal-minor tower (both packets are branches of the same
principal minor, so their level-3 tower coefficient is the same object), and it is the
place where a uniform lemma is visible. It does **not** need `D6`, `D7`, or the
continuation scheduler. It **does** need `D2` in a sharper form than (99,66): the
"single admissible split" claim (17(ssss)) plus the no-split alternative, whose Prop
6.3 descent to `(24,16)` is separately typed `OPEN[DESCENT-SUPPORT/VARIABLE-MAP]` —
**so the D = 108 row is NOT closed even if the δ = 3 gate confirms**; the no-split
branch is a second, independent obligation and the ledger should say so in one line.

**(25,15).** The kill is `D4` alone (Theorem-1.2 order rows plus gauges plus
saturation) — no Jacobian, no pole rows, no incidence. Its dossier needs `D1`, `D2`
(three strata `[3], [2,1], [1,1,1]` all `[1]`), `D3`, `D4`, `D8` (the saturation: which
ideal component was extracted, in which ring, with positive and negative controls —
FALLACY-v2's `sat()` item is the live hazard for this one), `D9`. The instrument note
17(oooo) is right that large rows need the order chart; the *logical* consequence is
better than the computational one: **an order-chart kill is a strictly stronger result
than a joint-chart kill, because it uses fewer necessary conditions.** Any row that
dies in the order chart should be recorded as dying at a lower tier, and the census
should be run order-chart-first.

### 5.3 Is the engine uniformisable? Yes as a census, not yet as a theorem

Recommended scheduler, replacing the (99,66) continuation order:

```text
tier 0  general ORDER chart (Thm 1.2 rows + gauge + saturation)   [cheapest; (25,15)]
tier 1  minor INCIDENCE compiler, parameterised by (delta, partition, tower)  [D=108]
tier 2  pole rows                                                  [(99,66) branch B]
tier 3  Jacobian continuation with exact Q* reduction              [(99,66) delta=5/2]
```

Cost for the 166-group `u_s > 1` census at `D <= 200`: tier 0 is built and instant per
row; tier 1 is the missing piece (Sol's "parameterised incidence compiler ahead of the
scheduler"), 2–4 lane-days; tiers 2–3 exist but are per-client. If tier 0 empties a large
majority — (25,15) is one data point, the K16 replay another — the census is affordable
within a week of lanes. **That yields a census, not a theorem.** The theorem is Card B.

## 6. Q4 — the all-degree programme, in one sentence, and the theorem to name

**The programme.** *A plane Keller pair's Moh skeleton either splits a principal minor
at the second point at infinity (`u_s >= 2`), where the necessary joint two-point
system — order rows, minor-incidence rows, pole rows, Jacobian rows — is inconsistent
over `Q`; or it does not (`u_s = 1`), where Prop 6.3/6.4 descends it to a
monomial-Jacobian pair carrying the entire inherited tree, where a coefficient theorem
of Appendix-II type applies; JC2 in the plane is the conjunction of these two halves,
and neither half is a census.*

**The single theorem to name.** Not "(V0) for the K = 16 ray" (a family: even proved,
17(ll) types the ray as the only *known* cofinal family, so the census stays infinite).
Not "the joint chart is empty for every screened skeleton" (a census: unprovable as
stated, since the screened census is cofinally nonempty). It is the coordinator's third
option, a structural statement about Keller pairs at two points at infinity:

```text
MINOR-EMPTY.  Let (F,G) be a Keller pair whose Moh skeleton has u_s >= 2 at the
second point at infinity.  Then the declared necessary joint two-point system is
inconsistent.  Equivalently: no Keller pair carries a principal-minor split.
```

**Why this one.** (i) It is the stratum no screen and no descent reaches — 296 rows /
166 groups at `D <= 200`, and the reason `OPEN[MINOR-DICHOTOMY]` has been carried since
p. 209 was first read. (ii) It is the only live statement with an *engine* and three
independent clients in one day. (iii) It is the half that Moh's own method never
covered, which is exactly why his `<= 100` theorem had a hole at (99,66). (iv) Proved,
it reduces JC2 to `u_s = 1`, where descent is a theorem and the target is a *finite*
reduction to monomial-Jacobian pairs — i.e. it converts the two-headed problem into
row 1 of APPROACHES with a single client class.

**Price.** Honest, and not small.
- *Census form* (every screened `u_s >= 2` row at `D <= 200` dies): tier-1 incidence
  compiler 2–4 lane-days, then ~1 week of lanes; deliverable a measured census plus the
  dossier instantiated 166 times. **Affordable now.**
- *Theorem form*: needs the killing residue to be a unit for **every** datum — a formula,
  not a computation (Card B). Unpriced until attempted; the four banked values suffice to
  falsify a candidate and not to confirm one. First milestone: a formula fitting all
  four. 2 lanes.
- *Risk*: if the residue has no closed form, MINOR-EMPTY is a census and the all-degree
  programme has no proof route on this side either. Type that possibility now.

**Where the coordinator's framing is wrong** (asked explicitly).
1. Revised Q1 asks for a closed-form resultant. Wrong object, three reasons (§3.2);
   the right one is the hsop/length statement, which is cheaper *and* stronger-typed.
2. The addendum presents 17(vvvv) and 17(wwww) as two results. They are one square
   system seen before and after a `b3`-elimination that costs a factor `2^(t-2)` (§3.1).
3. The packet's uniform K16 target `(V0)` is over-strong and is false on the one fibre
   where it has been separated from `(8.1)`. The ledger knows this; the packet does not
   say it, and a `dim > 0` at `t >= 8` would be mis-read as a disaster (§3.4(e)).
4. "Q3 is now 'how to make this paper-grade and uniform', not 'does it die'" is right
   for (99,66) and **wrong for D = 108**: the no-split alternative there is a live,
   separately-typed obligation (`OPEN[DESCENT-SUPPORT/VARIABLE-MAP]`), so the D = 108
   row is not closed by the δ = 3 kill however the gate returns.
5. The round's ordering treats K16 as the flagship. On the evidence of the last 12
   hours the flagship is the minor stratum; K16 is a prototype and a regression client
   (§2, V7).

## 7. Bottleneck reranking, strongest attacks, decisive experiment

**Principal PROOF bottlenecks, reranked.** (1) `D3` GAUGE — one coordinate change
realising both point-normalisations, with the residual stabiliser; blocks every
joint-chart verdict at once; one page. (2) The killing-residue formula (MINOR-EMPTY's
theorem form) — the only route from engine to theorem. (3) SQUARE-TAIL for all `t`
(was `(V0)`/`Res_w`) — blocks the `u_s = 1` prototype only. (4)
`OPEN[DESCENT-SUPPORT/VARIABLE-MAP]` and `OPEN[DESCENT-STATE-S3]`: the descent leg is
still typed at `s' = 2` and D = 108's no-split branch needs it — previously low, now
load-bearing for a live client. (5) The Fröberg statement for the full cone — demoted
to diagnostic.

**Principal DISPROOF bottlenecks, reranked.** The `u_s > 1` stratum is now hostile
territory (4/4 empty). Disproof effort should sit entirely on the ten OPEN two-point
`s_eff = 2`, `u_s = 1` rows (17(bbbb)) and the descended `(18,12; γ³)` / `(24,16)`
objects, where dimension grows rather than collapses, with `F_x G_y - F_y G_x ≡ 1`
recomposition the only accepted verdict (a numerical lift stays `REPRESENTATIVE`).

**Strongest proof attack**: SQUARE-TAIL + Hilbert-driven Gröbner (Card A) — the only
proposal that gets past `t = 7`, with an informative rather than silent failure mode.
**Strongest falsification attack**: the same test at `t = 8` *hoping for `dim > 0`*,
which would refute `(V0)` as a uniform statement, leave `(T)` intact via the
`tau`-criterion, and be the first structural surprise on the ray since `t = 2` — the
campaign has never run a test on the ray designed to fail. **New mechanism**:
SHARED-LEADER (Card B), the first proposal treating the four kills as instances rather
than four computations. **New connection**: Avenue 6 ↔ the K16 terminal cone, via V6 —
semigroup/Newton theory of approximate-root towers is the native language of `I_(t,+)`
and the natural source of an indexed Nullstellensatz certificate. **Software
acceleration / decisive experiment**: Hilbert-driven `std` with the conjectured CI
numerator on the square tail — acceleration and experiment at once, and the only route
to an answer at `t = 8` at desk scale.

## 8. Three idea cards

### Card A — SQUARE-TAIL / guided Gröbner (`NEW` as a target; `DUPLICATE`-adjacent to 17(vvvv) as a computation)

- **Target obstruction.** `(V0)` for `t >= 8`, via "the `t` tail rows are an hsop".
- **Object.** `J_t^tail = <T_(t,t),...,T_(t,2t-1)>` in `S_t` with `wp(1,2,..,t-1,t+1)`.
- **Dependencies.** The banked terminal driver (`singular_terminal_driver.py`) and the
  `t = 7, 8` row generation; Singular's Hilbert-driven `std(I, hilb, weights)`;
  17(iiii) properness lemma to promote a modular `dim 0` to char 0; Cohen–Macaulayness
  to force the char-0 series from the degrees (Sol's argument, already used at `t = 5, 6`).
- **Cheapest discriminator.** Supply `prod_(d=2t+2)^(3t+1)(1-s^d)` as the first Hilbert
  series and run the guided `std` on the tail at `t = 7` mod a good prime. Predicted
  `vdim = 149226`. Then `t = 8`, predicted `961400`.
- **Mandatory controls (this is the FALLACY-v2 hazard of the card).** A guided `std`
  with a WRONG series returns a wrong basis silently. Therefore: (i) positive control at
  `t = 5, 6` reproducing 3640 and 23256; (ii) membership check `NF(T_(t,k), G) = 0` for
  all `t` rows after every guided run; (iii) `vdim(lead(G))` equals the predicted `L_t`;
  (iv) negative control at `t = 2, y = 1/5`, where `(V0)` is FALSE — the guided run must
  not return `dim 0`; (v) a deliberately perturbed series must produce a detectable
  failure in (ii) or (iii). No result is reported without all five.
- **Interpretation.** `dim 0` + `vdim = L_t` at `t = 7`: the CI prediction survives a
  sixth index, `t = 8` becomes the frontier. Same at `t = 8`: SQUARE-TAIL is the right
  uniform statement and the residue is an indexed certificate. `dim > 0`, or controls
  fail: `(V0)` is refuted as a uniform statement — `(T)` must be carried by the
  `tau`-criterion from that day on.
- **Stop condition.** Two consecutive indices not completing in 10 minutes; or any
  control failure not repaired in one attempt.
- **Expected information gain.** High: the ray's status today is "exhausted at `t = 7`",
  and this is the only cheap proposal that moves the frontier with a negative outcome as
  informative as its positive one.

### Card B — SHARED-LEADER: the minor-split kill as a residue formula (`NEW`)

- **Target obstruction.** MINOR-EMPTY in theorem form (Q4).
- **Mechanism (the conjecture).** In a principal-minor split the packets are branches
  of the *same* principal minor, so they share their tower leader (`h3` at D = 108);
  Theorem 1.2 at the major point assigns the branches independent order weights. The
  resulting linear system on the shared coefficient carries a residue that is a rational
  function of the split datum `(delta, partition, u_s, V, weights)`; the chart dies
  exactly when that residue is a unit.
- **Dependencies.** The four banked certificates (6264 at (99,66) δ=2 stage 4; 64 at
  δ=5/2 stage 8; the D = 108 preflight unit; the (25,15) saturated-empty tier-0 run);
  the parameterised incidence compiler (tier 1).
- **Cheapest discriminator.** Do not build the compiler first. Take the two (99,66)
  residues and the D = 108 one, and ask whether a single expression in the datum
  reproduces all three *and* predicts the (16,12) calibration value. Four points, one
  candidate family; a fit that misses any point kills the candidate. Symbolic, ~1 lane.
- **Interpretation.** A formula fitting 4/4: MINOR-EMPTY has a theorem route and the
  compiler becomes a verification tool rather than the programme. A formula fitting 3/4:
  the missing client identifies the extra datum. No formula from any natural family:
  type MINOR-EMPTY as a census-only statement and say so in the ledger — that is itself
  a decision-grade outcome.
- **Stop condition.** Two candidate families refuted.
- **Expected information gain.** Highest strategic value on the board: it decides
  whether the flagship half has a proof or only an engine.

### Card C — the induction restriction test (`NEW`; packet route Q1(a), never attempted)

- **Target obstruction.** Whether `(V0)` admits induction in `t`.
- **Object.** The banked indexed form of `T_(t,k)` (17(iiii) §2) and the terminal JSON
  records at `t = 3, 4, 5`.
- **Cheapest discriminator.** Set `q_(t,0) = 0` in the `(t+1)`-system and test whether
  the coefficient arrays restrict to the `t`-system's arrays with the coefficient field
  changed by `t -> t+1` (i.e. `3d^2 = t+2 -> 3d^2 = t+1`). Symbolic; no Gröbner; the
  records exist. ~1 lane-hour.
- **Interpretation.** A restriction map exists: induction in `t` is live and `(V0)`
  may reduce to a base case plus a unit condition — the cheapest possible route to the
  uniform statement, and it would obsolete Cards A's frontier chase. No map: route (a)
  is typed DEAD and the ledger stops carrying it as an option in every packet.
- **Stop condition.** One negative result; do not search for exotic substitutions.
- **Expected information gain.** Moderate-to-high per unit cost — it is the cheapest
  unattempted item on the K16 board and it removes or promotes a standing option.
- **Dependency note.** Card C is *cheaper* than Card A but its expected value is lower
  (most such maps do not exist). If capacity allows, run both; if not, see §9.

## 9. The single first lane

`k16-square-tail-stdhilb` (Card A), on any adapter with Singular. Reasons: it merges
two lanes' results into one target; it is the only proposal that moves the ray past
`t = 7`; both outcomes are decision-grade; and its controls are cheap and explicit.
Card C is cheaper and should be folded into the same lane as its first 30 minutes if
the adapter has budget (they share the terminal records and neither needs new rows).
Card B is the higher-value lane but belongs to the coordinator's flagship queue, not
to a first lane launched from a blind submission.

If exactly one lane can be launched campaign-wide, launch the `D3` GAUGE page instead
of any of the three: it is one explicit group element, it blocks every joint-chart
verdict, and it is the only item that can invalidate work already promoted.

## 10. Continue / redesign / stop per running lane (receipts only)

The six lanes named in packet §3 have all sealed since the freeze (`final_status=DONE`,
exit 0, per `.run.v2`); their reports were not opened. Dispositions are therefore for
the four lanes launched with this round, whose receipts show `initial_status=RUNNING`,
plus a retrospective note on the six.

| lane | receipt state | disposition |
|---|---|---|
| `g108-delta3-kill-gate-gpt55` | RUNNING (08:25:23Z) | **CONTINUE**, with one scope addition: the gate should be asked to type the *no-split* branch separately, since the δ = 3 kill does not close the D = 108 row (§6 item 4). |
| `g9966-chart-necessity-opus5` | RUNNING (08:25:28Z) | **CONTINUE, REDESIGN SCOPE**: make `D3` GAUGE the first deliverable, not a section — it is the only obligation that can invalidate promoted work (§4.1 H1). Add `D8` localisation necessity. |
| `k16-square-resultant-fable5` | RUNNING (08:25:33Z) | **REDESIGN**: retarget from `Res_w` closed form to SQUARE-TAIL (§3.2). If the lane has already priced the resultant, the `B_t = 2^(t-2) L_t` identity says the answer without the computation. |
| `row2515-order-gate-sol56` | RUNNING (08:25:38Z) | **CONTINUE**; require the `sat()` positive/negative controls explicitly (FALLACY-v2), since the (25,15) verdict rests on a saturation. |
| six §3 lanes (k16-subchart-q-opus5, k16-t6-sol56, k16-t11-cone-gpt55, preprocess-native-gpt55, g9966-branchB-kill-gate-gpt55, g9966-delta52-stage8-sol56) | all DONE, exit 0 | **STOP** (complete). No relaunch: their successors are the four above. |

## 11. Systems check — one UPGRADE

**Rotation slot: state freshness / scheduling.** `UPGRADE[PACKET-STALENESS-CONTRACT]`.

*Measured evidence, this round.* The packet was frozen 2026-09-03T22:18Z and fired
2026-09-04T08:30Z — a 10h12m gap — during which ten lanes sealed (17(tttt)–(bbbbb)).
The coordinator patched with an addendum that **changed Q1 and Q3**, and recorded
(17(ccccc)) that its own blind submission was written before the seals and is "partly
superseded". Consequences: (i) blind submissions are no longer comparable — one was
written against Q1, five against revised Q1; (ii) the deduplication step in
COORDINATION §4 fingerprints by "target obstruction, mechanism, object, decisive test",
and a question change silently shifts the target obstruction, so operational duplicates
will mis-merge; (iii) §1 "Binding state" prose was materially stale at launch.

*Upgrade.* Give the packet two header fields, `frozen_utc` and `launch_utc`, plus a
rule: if `launch_utc - frozen_utc > 90 min` **or** ≥ 3 promotions land between them, the
round is **re-frozen and re-named**, not addended; the coordinator's blind submission is
rewritten or withdrawn; questions are never edited after freeze under the same name.

*Smallest useful test.* Add the two fields and a staleness check to the round launcher
that refuses an over-age packet without `--stale-ok` and prints the delta letters banked
since `frozen_utc`. One evening's work; it prevents a whole round of non-comparable
submissions, the most expensive failure this protocol has.

*Not proposed.* Nothing about compute, adapters, or routing: compute behaved this round
and the two timeouts were mathematical.

## OPENS RAISED

- `OPEN[SQUARE-TAIL]` — decide whether the `t` forms `T_(t,t..2t-1)` are a homogeneous
  system of parameters for every `t >= 3`. QUANTITY: decide `dim_(A_t) S_t/J_t^tail`
  (predicted finite, `= 2*binom(3t+1,t-1)`) versus `dim > 0`, first at `t = 7, 8`.
  CHEAPEST TEST: Hilbert-driven `std` on the tail with the CI numerator supplied, mod a
  good prime, with the five controls of Card A; Singular; ~10 min per index.
- `OPEN[K16-INDUCTION-RESTRICTION]` — decide whether `q_(t,0) = 0` restricts the
  `(t+1)` terminal arrays to the `t` arrays. QUANTITY: decide existence of the
  restriction map (yes/no), and if yes bound the number of correction terms by a
  function of `t`. CHEAPEST TEST: symbolic comparison of the banked indexed arrays at
  `(t,t+1) = (3,4)` and `(4,5)`; no Gröbner; ~1 lane-hour.
- `OPEN[SPLIT-RESIDUE-FORMULA]` — decide whether the minor-split killing residue is a
  closed expression in the split datum. QUANTITY: bound the number of datum parameters
  needed to reproduce all four banked certificates (6264, 64, the D = 108 preflight
  unit, the (25,15) tier-0 verdict); at most 5 is the useful threshold. CHEAPEST TEST:
  fit one candidate family against the four banked values; symbolic; ~1 lane.
- `OPEN[JOINT-GAUGE-COMPATIBILITY]` — decide whether the two declared point-
  normalisations of a joint two-point chart are simultaneously realisable. QUANTITY:
  exhibit one group element realising both, and bound the residual stabiliser's
  dimension (predicted 0 after the declared moduli are fixed). CHEAPEST TEST: write the
  coordinate change for (99,66) explicitly and compute its stabiliser; one page, no
  compute; ~1 lane-hour. This is `D3` and it gates every joint-chart verdict.
- `OPEN[ENGINE-CHAR0-CALIBRATION]` — decide whether the joint-chart engine reproduces
  the `(16,12)` kill over `Q`. QUANTITY: decide whether the localised calibration ideal
  `= [1]` over `Q` on all 77 rows (at present known only mod 32003), i.e. bound the
  number of rows whose char-0 reduction differs from the modular one by 0. CHEAPEST TEST: rerun the banked
  `(16,12)` control with the char-0 flag; Singular; minutes.

OPENS CLOSED (by this report): `GAP[MOH p.208 (16,12) CALIBRATION]` closes POSITIVE —
the chart is printed on p. 208 (PDF page 69) and is transcribed in V6; it is absent only
from the PDF text layer. Read via the existing page image
`box/jetedge-20260903/moh1983-printed-p208-pdf69.png`.

## 12. FALLACY-v2 checklist

- **Floor/attainment.** §3.3 refuses the top-weight/initial-ideal inference and states
  the exact reason (`<in_top(gens)>` vs `in_top(J)`); no axis or `b4 = 0` statement is
  promoted to a radical membership anywhere here.
- **`sat()` wrapping.** Flagged as the live hazard for the (25,15) verdict (§5.2) and
  required as `D8`; not used by me.
- **Variable/ring map.** The weighted resultant's vanishing criterion is typed as an
  uncited hypothesis (§3.2 item 3); `A_t` and its `d`-presentation are declared with the
  split index `t = 3s^2-1`.
- **Prime label/derivative.** Moh's `b1..b4` (p. 208) are identified with the campaign's
  by their weights `3t+1, 2t+1, t+1, 1` at `t = 1`, not by name-matching.
- **Raw remainder degree / promotion direction.** Card A requires `NF(T_(t,k), G) = 0`
  after every guided run precisely because a guided basis can be silently wrong; nothing
  modular is promoted by me, and Card A's promotion path is 17(iiii) properness plus CM.
- **Carrier/exit charge.** No exit claim; no `charge_basis` line is due.

## 13. Artifacts

No durable artifact outside this report. The two arithmetic identities of V2/V3 were
computed with a five-line `python3` script over `math.comb`/`math.prod` (tail degrees
`2t+2..3t+1`, weights `1,2,..,t-1,t+1`; resultant degrees `4t+4+2r`, weights `1..t-1`),
checked at `t = 3..12`, and agree with Sol's measured lengths at `t = 3,4,5,6`; they are
one-line rederivations and need no box directory. The p. 208 read used the existing
image `box/jetedge-20260903/moh1983-printed-p208-pdf69.png` (no new render).

## 14. Collision scan

`ops/open_collision.py xmodel/ideation-20260904T0000Z-opus5.md` exits 0 with status
CANDIDATES. Reading of hits: the `17(wwww)` hit on `OPEN[SQUARE-TAIL]` is the
intended one — it is the delta this OPEN reformulates (V1/V4), not a closure; the
`max12-812-*` hits are lexical noise from a retired case; the `17(llll)/(tttt)/(uuuu)`
hits on `OPEN[SPLIT-RESIDUE-FORMULA]` are the source certificates the card fits
against. The only same-round file appearing is the charged packet itself. No hit
closes any raised OPEN. Verbatim block:

```text
  ## COLLISIONS

  status: CANDIDATES

  ### OPEN[SQUARE-TAIL]

  - `AUDIT.md:17678` — ### 17(wwww) (PROVED-HERE, producer Fable): Theorem TOPTAIL (uniform in t ≥ 3): on b₄ = 1 the rows T_{t,2t−1−r}, r = 0..t−1, are quadratics Q_r = a_r b₃² + b_r b₃ + c_r with a_r, b_r, c_r the b₄ = 1 images of weighted forms of weights r,...
  - `xmodel/ideation-20260904T0000Z-packet.md:121` — - K16 ray: literal Proposal A (top t + 2 rows regular) is IMPOSSIBLE for every t; a corrected tail is regular at t = 3..6; Lemma SQUARE (Fable): (V0) ⇐ V(R_1..R_{t−1}) = {0} for a SQUARE weighted-homogeneous system of resultants in the t...
  - `xmodel/max12-812-order2-exact-square-pell-chebyshev-support-hostile-review-grok-20260826-prompt.md:33` — 2. Independently decide whether seven-tail vanishing really forces `c=0` in
  - `xmodel/max12-812-order2-square-third-tail-sharp-v2-hostile-review-grok-20260826-prompt.md:67` — Decide whether this proves `alpha=beta=0` at the necessary third-tail gate.
  - `xmodel/max12-812-order24-coefficient-infinity-review-grok-v2-20260825-prompt.md:32` — at most three for the seven order-two tail rows. Decide whether the

  - `OPEN[K16-INDUCTION-RESTRICTION]` (report:688): NONE

  ### OPEN[SPLIT-RESIDUE-FORMULA]

  - `AUDIT.md:17580` — ## INTEGRATION #17 DELTA (llll) (2026-09-03T22:10Z, PARTIAL, producer Sol): THE b₄ DIRECTION OF THE K = 16 TERMINAL CONE — PROVED[INDEXED-B4-AXIS-FORMULA] for all t ≥ 2 (every pure-b₄ coefficient of T_{t,k}|_{b₃ = q = 0} in closed indexe...
  - `AUDIT.md:17672` — ### 17(tttt) (PROMOTED, gate GPT-5.5 + independent re-implementation Opus): THE (99,66) δ = 5/2 BRANCH IS DEAD — 17(qqqq) PROMOTED; hence, with 17(pppp) (δ = 2 dead, PROMOTED) and the complete split classification 17(nnn)/(rrr)/(sss) (δ ...
  - `AUDIT.md:17674` — ### 17(uuuu) (counting bound, producer Sol): the δ = 5/2 T2/T3 bridge (17(qqqq)'s consistency check) did NOT finish the full elimination; exact prefix through s⁶³: five independent Q* pivots (first T2_s56_pi0 = −98304·(alternating sum of...

  - `OPEN[JOINT-GAUGE-COMPATIBILITY]` (report:698): NONE

  - `OPEN[ENGINE-CHAR0-CALIBRATION]` (report:704): NONE
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `50003`.
- Body SHA-256:
  `759703cfcea4ab3013a5b4b2cc7211f72c7cf0fad37e596bd18d08259a9640af`.
- Frozen basis: `ce00e907002c40891a1d441badbc569100789e29`.
