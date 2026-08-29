# JC2 `20260828T1707Z` cross-pollination review — Opus 5

Lane: Opus 5 (`claude-opus-5`), unblinded adversarial cross-review.
Cross-packet `xmodel/ideation-20260828T1707Z-cross-packet.md`, SHA-256
`9cc1d824e35abbd9f367f59cc94bfde2f6c93f37a099ee48238211b6bbbec8e9` —
**verified before reading**. All five corpus hashes and all five overlay hashes
verified `OK` before the corresponding file was opened (§7.6). `jc2-lean` was
not entered, listed, searched, read, built, modified, status-checked or
controlled. No AWS, Singular, msolve, Sage, Lean or heavy local CAS. One small
stdlib-only exact script (20 checks, all `PASS`, §7.5). Sole write: this file.

**This report proves and disproves nothing about JC2.** Its deliverable is a
line-by-line audit verdict, three retractions (two of them mine), one repaired
theorem, one rejection, and a queue.

---

## 0. Verdicts in one page

| # | charge | verdict |
|---|---|---|
| 1 | `ROOT-W2` / two-pole `td=6` root-sector closure | **REPAIR.** Conclusion survives and is stronger than filed; my proof was wrong at step (a) and the packet's suspected weak link (`L1a(b)`) is **not** the weak link. Real dependency: **`MP1` + the `V_2`-vs-`r≥2` identification**. Repaired form = `ROOT-BUDGET` (§1.4). |
| 2 | residue-A proposals | Consensus #1 (two-parent H1 match) is **symmetric-trivial at Q-level** and cannot discriminate (§2.2). `Q-GHOST` **void** (§2.4). `MERGE-DIFFERENT` is the only budget-side proposal whose stated magnitude would actually kill. `RES-AV` and `A47` are the same object (§2.6). |
| 3 | `A47` | Identities `(A47.1)/(A47.2)` **verified exact** (18 instances). Budget interface **REJECTED**: both sides need the same missing landing data, and my "injectivity is already available" claim is **retracted** (§3). |
| 4 | GGV | **Hybrid**: Fable5's level-wise Fitting atlas as the mathematics, the repaired substitution-only adapter as the vehicle. Headline gate: a **planted-nonzero control**, absent from all four reports and from the overlay-C contract (§4.2). |
| 5 | new connections | Three (§5): the `w`-ladder crossing at 1; ramification-divisor unification; the symmetric-trivial parent match. |
| 6 | queue | §6. 70/30 proof/disproof, with the disproof half spent on *invalidating* rather than extending the finite lane. |
| 7 | scope | §7. Two errata filed against canonical/packet text (§7.1). |

---

## 1. Charge 1 — line-by-line audit of `ROOT-W2`

`ROOT-W2` (mine, `1707Z` §3.2): *in the two-pole `td=6` configuration there is
no root merge, for any `μ`.* Proof steps (a) `L1a(b)`; (b) `DS2/DS3`;
(c) entry pin `w_0=2`, `W(2)={2}`; (d) `(R2)` gives `w_G<1`; contradiction.

### 1.1 Step (d) is now stronger than I claimed — and it is not mine

Overlay A promotes, **edgewise at all multiplicities**, `X_R=A/B`,
`w_e=1-A/(μ_e B)`, `0<w_e<1`. My step (d) is therefore discharged by a
reviewed result, not by my reading of `(R1)`. Independent corroboration:
`SHEET6-2POLE §4b` already records the case-I parent condition
`κ̄_parent < ν_parent`, which is the integer shadow of `w_e<1`
(`w=(κ̄-ρ)/ν<1 ⟺ κ̄<ν+ρ`). Both tests agree on the pole
(`κ̄=5 ≮ ν=2`, `w=2`). **CONFIRMED.**

### 1.2 Steps (b),(c) hold, cap-free

`W(2)={2}` recomputed cap-free (`num(w)=2` has no divisor `Δ≥3`;
`Δ=(n-1)ν+1≥3` from `n,ν≥2`). Entry pin `w_0=(5-2/2)/2=2` agrees with
`Q(P_i)`. **CONFIRMED.**

### 1.3 Step (a) is where it breaks — and not for the reason anyone expected

The packet and overlay A both flag `L1a(b)` as the narrow audit item ("whether
every such root meet receives a certified row-1 `M=1`, `W={2}` branch"). I did
the audit. Two findings, in this order:

**(i) `L1a(b)` itself is sound at `G_m=(0,y)`.** `SHEET6-DEPTH §1` *defines* an
`M=1` segment as ending "at the last vertex before a merge vertex `G` (`r(G)≥2`)
**or before `(0,y)`**", so `DS1`–`DS3` are already stated over the root case;
`DS1(a)`'s exclusion is of `(0,y)` as a *segment vertex*, not as a segment
endpoint. `L1a(b)`'s third-pole induction (St 8.4 + St 8.2 + Prop 6.8) never
uses interiority of the meet. My own `§3.2` attack point 1 — "the single most
fragile step" — is **wrong**; retract it.

**(ii) The premise is nevertheless false, in the interior-merge branch.** The
sector has two branches (MP1, `m=2`: exactly one vertex with `r≥2`). If that
vertex is interior — residue A's own configuration — then the parent of `(0,y)`
is the **post-jump suffix**, which `L1a(b)` does not cover and whose `w` is not
in `W(2)`. Exact data from the canonical exhibit
(`SHEET6-2POLE §6a`, `Q=(D,\deg p,ν,M,κ̄)`):

```text
w(P_i)   = (5 - 2/2)/2   = 2       kappabar=5 >= nu=2   -> root-parent test FAILS
w(G_m)   = (5 - 6/12)/3  = 3/2     kappabar=5 >= nu=3   -> FAILS
w(suffix)= (5 - 42/126)/7= 2/3     kappabar=5 <  nu=7   -> BOTH TESTS PASS
```

`w=2/3 ∈ (0,1)`. **Residue A's own suffix parent satisfies overlay A's root
window and the `§4b` case-I parent condition.** The alphabet argument does not
touch it. So the packet's audit question has the answer **no**: a certified
row-1 `W={2}` branch does *not* reach every candidate root meet in the sector.

`ROOT-W2` as written is therefore **not proved**. `SHEET6-2POLE §4c.2` was
already correctly scoped ("two all-`M=1` chains cannot terminate together at
the root"); I over-generalized it.

### 1.4 The repair: `ROOT-BUDGET`

The conclusion survives, by a different and more portable argument.

> **`ROOT-BUDGET` (candidate, INTERNAL-UNREVIEWED).** Let `(f,g)` be normalized
> with `m` on-axis poles.
> **(E)** *Entry above one.* On-axis, `w_0 = Λ(α+β-1)/(αβ) ≥ (α+β-1)/α > 1`,
> using only `Λ≥β` (Prop 5.7) and `β≥2`. So no entry frame lies in the root
> window `(0,1)`.
> **(C)** *Contraction events.* By `DS2`, `w` is conserved by every non-resonant
> `M=1` chain step; it changes only at (i) a resonant chain step, which requires
> `Δ=(n-1)ν+1 ≥ 3` with `Δ | num(w)` (`DS3`), or (ii) a merge vertex.
> **(B)** *Budget.* By `MP0/MP1`, `Σ_{G∈U, r(G)≥2}(r(G)-1) = m-1`; a root merge
> at `(0,y)` is itself such a vertex and consumes `r-1 ≥ 1` of that budget.
> **Conclusion.** By overlay A every arriving parent of a genuine root merge has
> `w_e<1`, so **every** arriving branch needs at least one contraction event
> strictly between its entry and the root, drawn from (C) — with the merge
> budget already reduced by the root merge itself.

At `m=2`, `td=6`: both entries are row 1 (`Λ=3+3`, `§2a`), `w_0=2`,
`num(w_0)=2` admits no `Δ≥3`, so **no resonant chain step exists on either
branch**; the root merge consumes the whole `m-1=1` merge budget, so no
interior jump can supply the contraction either. Hence no genuine root merge.
∎ (modulo §1.5).

This is strictly better than `ROOT-W2`: it makes the `MP1` dependency explicit,
it is `μ`-free, and it *predicts* where root merges become live. Fable5's
`td=7` frame is the confirming instance: entry `(a,b,ν)=(2,1,3)`, `w_0=8/3`,
`num=8`, `Δ=8` admissible, `W(8/3)={8/3,4/3,2/3}` — a **resonant chain step**,
not a merge, delivers `2/3<1`. Recomputed here cap-free (`PASS`). So `td=6` is
closed not by luck but because `num(w_0)=2` is the arithmetic minimum.

### 1.5 The one residual, stated exactly

`MP1` counts `r(G)` = `T_a↘∩V_a` predecessors and states outright that every
vertex strictly below `G*` has a *unique* such predecessor. Overlay A's
hypothesis is `R ∈ V_{2,a}\V_{1,a}` (fibre separation). These coincide unless
`(0,y)` carries a **northeast** root:

> **`ROOT-Y-NE` (residual).** Exclude: `(0,y) ∈ V_{2,a}\V_{1,a}` with exactly
> one searrow arrival plus `≥1` northeast root, in the interior-merge branch.

By St 8.2 (`SHEET6-2POLE §4a`: searrow iff `deg q·mult(p,c) > deg p`), a
northeast root needs `μ''·B < A`, i.e. `X_R = A/B > 1`. Overlay A gives
`X_R = μ_e(1-w_e)` at the single searrow parent, and St 8.4 gives `μ_e | M_e`.
For **all four recorded IV survivor classes** on residue A the suffix satisfies
`w = 1 - 1/M` exactly (verified: `(1/3,7,3,5)→2/3`; `(2/3,3s+2,3,2s+2)→2/3`
for all `s`; `(1/4,5,4,4)→3/4`; `(3/4,4s+3,4,3s+3)→3/4` for all `s`), hence

```text
X_R = mu(1-w) = mu/M <= 1   for every mu | M,  with equality at mu = M.
```

so no northeast root exists and `ROOT-Y-NE` is **closed on the recorded book**,
*exactly at the boundary*. A sector-wide closure needs either
(a) `μ_e(1-w_e) ≤ 1` at every reachable post-jump parent of `(0,y)`, or
(b) a scope ruling that "genuine contact-zero root merge" means `r≥2`.
`SHEET6-2POLE §6b` warns the book is "not an exhaustive current census", so
(a) is a real obligation, not a formality.

### 1.6 Verdict

**`REPAIR`.** Promote `ROOT-BUDGET` at scope "on-axis, `m=2`, `td=6`, modulo
`ROOT-Y-NE`(a)". Do **not** promote `ROOT-W2` as stated. Do **not** cite
`L1a(b)` as the fragile step — it is sound; the fragile step is the identification
of `V_{2,a}\V_{1,a}` at the root with `r((0,y))≥2`. The queued `m=2` root
recensus stays cancelled either way; its remaining scope is `m≥3`, SF1,
off-axis and `td≥7`, where `ROOT-BUDGET` says the door reopens through resonant
chain steps, not merges.

---

## 2. Charge 2 — the residue-A proposals, compared and combined

### 2.1 What must be beaten

All four reports compute MFE on residue A and get `2 ≤ 3`, slack 1. Confirmed
here. Grok's slack arithmetic is the binding constraint and I endorse it
without reservation: **`+1` yields `3≤3` and kills nothing.** A budget kill
needs `≥ +2`, a larger `ψ`, or a non-budget argument.

### 2.2 Simultaneous coefficient / parent match — **cannot discriminate as described**

Grok Card A, Fable5 Card 1a, Sol Card A and my Card 1 all rank a two-parent
match first. Three of the four describe it as *the per-edge Prop 9.3 (a)–(d)
system plus the rigid `(iv)` scale*. That system is already recorded solved,
and it is **symmetric-trivial**:

```text
both parents: (rho,kappabar,mu) = (1,5,1),  n = (5,5)
edge 1: dp/dq = 1*(1+5)/(5+5) = 6/10        edge 2: identical
kappabar(G_m) = (5+5)/2 = 5 (both)          D(G_m) = (2+5*2)/2 = 6 (both)
```

`P1 = P2` as `Q`-records, so the "two ratio equations" of `§2b.2` are literally
one equation, satisfied. There is no discrimination at `Q` level, and there
never was. The whole live content sits one level lower, in the **substitution /
`⊖`-constant transport** between the three independently rigid patterns
(`SHEET6-L1 §5` closing paragraph and `§7.2(ii)` say exactly this). Ranking
recommendation: keep the attack at #1, but re-specify it as
transport-across-one-edge, not as an edge-equation solve. This reallocates
three peer lanes onto the same target and stops three teams from re-verifying a
tautology.

Related adjudication — **Sol's Galois/inversion insight (§6) is void over `ℂ`.**
The merge ODE determines the *unordered* pair `{a_1,a_2}` through the symmetric
relations `a_1a_2=σ²/6`, `σ=a_1+a_2`; `2+√3` and `2-√3` are the two labellings
of that one pair, not two configurations. Parent swap is a relabelling, so no
fixed-point condition arises. It could only bite for a pair over a field
`k ∌ √3` with individually `k`-rational poles, which is not a licensed
reduction.

### 2.3 `MERGE-DIFFERENT` (Sol) — the only budget proposal with a killing magnitude

Sol claims relative-different length `≥ l+1 = 2` at the merge, hence `+2` and
`4 > 3`. Grok's "+1 is useless" objection does **not** apply to Sol's stated
magnitude; the two peers are arguing past each other. The real weak link is the
second clause: *the non-pole summands inject into pairwise-distinct actual cv
flags*. That is the same unproved arrow every `T_a` charge needs, and it is
harder here because the summands sit at directions with no `T_a` vertex.
**Sees the orbit geometrically: yes** (a module length at a local extension is
not a renaming). **Usable: not yet**, and its failure mode is the quarantined
`(22)`-style double charge.

### 2.4 `Q-GHOST` (Grok) — **void as stated**

`T_a`, `V_a` and the set of fibre branches are constructed from the Puiseux
roots of `f-a` alone (Def 3.4, Prop 3.1(**)). They are **independent of `g`**.
Translating `g ↦ g-b` moves thresholds and puncture *values*, but cannot make a
non-root of `p_F` into a direction of any tree, because there is no fibre branch
there in any translate. Grok's own §1.1 states the reason (St 3.18). Recommend
recording `Q-GHOST` as closed at its first gate, at zero cost.

### 2.5 `RES-AV` (Fable5) — geometric, but resting on an unpinned identification

`D_g = κ̄ - D = -1` at `G_m` is arithmetically right (St 9.1; verified: pole
`+3`, merge `-1`, suffix `-37`). Two objections:

1. `D_g` is a datum of the **vertex**, not of the resonant direction. The step
   from "`G_m` has `D_g=-1`" to "*the `l=1` orbit* cancels the last polar level"
   is an extra inference and is not supplied.
2. **Which function's pattern is `q`?** Prop 8.1(iv) is written for a member of
   the `h`-family (`Not 8.1`: `M_F=gcd(deg p_F, deg p_{h_0..h_m,F})`,
   `h_0=g`), and `m_F=0` is asserted only at **pole** vertices (Prop 5.1(i)).
   `SHEET6-L1 §7.2(i)` reads the resonant root as carrying branches of
   `h_1 = g² - s_0f³`, not of `g`. `RES-AV`'s "`g→b` finite" reading needs
   `m_{G_m}=0`; `A47` needs `m_{G_m}≥1`. **They cannot both be right, and
   nothing I read pins it.** This is the cheapest decisive item in the whole
   ghost-pricing lane (§6 item 3), and it gates `RES-AV`, `A47` and (already
   dead) `Q-GHOST` simultaneously.

### 2.6 Combination: `RES-AV` and `A47` are one object

`J(f,h_1)=α g^{α-1}` (verified exact, §3) makes `{g=0}` the entire critical
locus of `(f,h_1)`, and `(f,h_1) = τ∘(f,g)` with `τ(u,v)=(u,v^α-s_0u^β)` of
degree `α`, so `td(f,h_1)=α·td`. Fable5's target-side asymptotic door and my
`h`-side branch count are the two projections of the **same ramification
divisor**; Sol's merge-different is its local shadow. One computation — the
branch count of `h_1` at infinity over the fibre-`a` sector, together with the
`m_F` ruling of §2.5 — serves all three. That is the combination worth building;
three separate cards are not.

### 2.7 Seed-to-jet lifting

Not a charge on the orbit; a construction that consumes one. It sees the orbit
as the pinned coefficient `b=(2/3)σ`. Correctly placed by all four reports on
the disproof side, and correctly gated behind the transport question of §2.2.

### 2.8 Scoreboard

| proposal | sees the orbit geometrically? | live? |
|---|---|---|
| two-parent H1 match | as a coefficient, yes; **as a discriminator, no** | re-specify to substitution transport |
| `MERGE-DIFFERENT` | yes (module length) | yes, blocked on the injection clause |
| `RES-AV` | yes (asymptotic values) | blocked on `m_{G_m}` |
| `Q-GHOST` | no — renames a non-direction | **void** |
| `A47-BUDGET` | yes (branches of `h_1`) | **budget rejected**, identification retained |
| seed-to-jet lifting | yes (as data) | yes, downstream |

---

## 3. Charge 3 — `A47`: identity verified, budget rejected

### 3.1 The identity

With `J(f,g)=1`, `h=g^α - s_0f^β`:

```text
(A47.1)  J(f,h) = alpha*g^(alpha-1)          (A47.2)  J(h,g) = -s_0*beta*f^(beta-1)
```

**Verified exactly**, 18 instances (tame Keller pairs `f=x`, `g=y+P(x)`,
`(α,β) ∈ {(2,3),(3,4),(2,5)}`, exact `Fraction` bivariate arithmetic, stdlib
only). Both are elementary consequences of the derivation property of the
bracket and `J(f,f)=J(g,g)=0`. Corollary, also exact: `(f,h)=τ∘(f,g)` with
`deg τ = α`, so `td(f,h)=α·td` (`=12` here), and the critical locus of `(f,h)`
is `{g=0}` with multiplicity `α-1`.

### 3.2 The first exact missing implication — and why it sinks the budget

I proposed `Σ_F l_F ν_F ≤ N_∞(h) - N_∞(h ∩ f=a)` and claimed its injectivity
half was "already available" from the promoted Definition 3.3 attachment lemma.
**Both claims are retracted.**

- *Injectivity.* The attachment lemma assigns witnesses to **flags of `T_a`**.
  The resonant directions are not flags of `T_a` (St 3.18). Nothing transfers;
  the argument would have to be rebuilt in the ambient contact quotient. Fable5
  reached the identical conclusion from the other side ("`T_a` attaches to
  fibre-relevant rays only") and its disclosed failed attempt is the same wall.
- *Computability — the fatal one.* I claimed this was "the first inequality
  whose two sides are both explicitly computable from pinned data". It is not.
  Because `h` is an explicit polynomial in `(f,g)`, every invariant of `(f,h)`
  is determined by `(f,g)` plus the fixed `τ`; in particular `N_∞(h)` in the
  fibre-`a` sector is a function of the **boundary/landing data of `(f,g)`** —
  precisely the datum whose absence is proof bottleneck #1. The two sides of
  `A47-BUDGET` are blocked by the same missing input.

So the first exact missing implication is not a lemma about `h`; it is:

> **(A47-MISS)** an independent determination of the branch count of `h_1` at
> infinity over the fibre-`a` sector — equivalently, exactly the landing datum
> the campaign lacks.

### 3.3 Verdict

**`REJECT` `A47-BUDGET` as a budget or contradiction. `RETAIN` `(A47.1)`,
`(A47.2)` and `td(f,h)=α·td` as exact identities**, whose residual value is
that they name `{g=0}` as the locus carrying the resonant behaviour — the
identification that unifies §2.6 and that `RES-AV` needs anyway. My `1707Z §5`
sentence "the first inequality of the right *type*, and the first one whose two
sides are both explicitly computable" is withdrawn; the second half was false.

---

## 4. Charge 4 — fastest complete GGV route

### 4.1 Route: hybrid, with Fable5's level-wise design as the mathematics

All four reports converge on Fitting. Fable5's formulation is the correct one
and supersedes mine, Grok's and Sol's on one decisive point: the successor of a
level is the **single closed set** `V_{k+1} = V_k ∩ V(all size-r_k minors)`, not
a complement per chart. My `1707Z §6` said "there are no complements"; that was
right in spirit and imprecise in fact — there is exactly **one** complement per
*level*, and it is canonical. Grok's and Sol's "recurse on the complement of
`Δ`" reintroduce the per-chart explosion the redesign exists to remove. Adopt
Fable5's level-wise atlas.

Vehicle: the **repaired substitution-only adapter**, not a rebuild. Overlay C is
explicit that the q1p03 failure was a `REDUCER_PLACEHOLDER` surviving
generation, caught by the 95-pivot marker gate before any inference. That is a
gate working correctly; it is not evidence about the mathematics and must not
trigger a redesign of the mathematics.

### 4.2 The gate everybody missed: a planted-nonzero control

Overlay C reports, on six of six charts: *all bordered identities and lifts have
normal form zero; all endpoint coefficients vanish.* A uniform six-for-six
all-zero result is exactly the signature a silently-zero reducer, a wrong
ambient ideal, or a dropped substitution would also produce. The existing gates
(95-pivot marker, NF replay, `q2 mod (q2)=0`) catch *generation* and *reducer*
failures; **none of them can fail on an all-zero semantic bug**, because zero is
the expected answer.

> **`PLANT` (mandatory, fail-closed).** In every job, alongside the real
> endpoint `E`, reduce (i) `E+1` and (ii) one bordered identity with a
> precomputed nonzero normal form. Both must reduce to something **nonzero**.
> A job in which every tested quantity — including the plants — reduces to zero
> is a **FAIL**, not a `PASS`.

This is the single cheapest action available on the finite lane, and it is the
only one whose negative outcome would be worth more than its positive one: it
either certifies six banked results or invalidates them.

### 4.3 Fail-closed proof-object contract

```text
G0 GENERATION   emitted script contains no placeholder token; byte-diff of
                emitted vs template shows every slot substituted; rc==0 AND
                zero parser diagnostics (rc0-with-diagnostics is a FAIL).
G1 AMBIENT      pinned std(I) hash; NF after every entry/row/minor/syzygy op;
                q2 mod (q2) = 0 negative control.
G2 PIVOTS       the 95-pivot marker gate, unchanged.
G3 RANK         nonzero-NF minor witness AND exhaustive next-size vanishing.
G4 COVER        per level, either a cocertificate 1 in (size-r minors)+I(V_k),
                or the explicit residual closed set V_{k+1} passed forward.
                No dense-open inference, ever.
G5 PLANT        section 4.2. Both plants nonzero.
G6 BANNER       leaf verdicts only EMPTY | ENDPOINT-ZERO | SURVIVOR, each with
                its level index; anything else emits
                NO_VERDICT_LEVEL_k_UNCOVERED. Zero swap; custody manifest
                replay; independent re-run of one leaf per branch.
TERMINATION     rank strictly drops; hard cap 9 levels (from the banked 9/104).
```

### 4.4 AWS fanout trigger

Single-node first, no blind fanout. Trigger: **`Q1P03` (smallest, `4/99`) level 1
passes `G0`–`G6` including both plants.** Only then fan out to the remaining
five branches at level 1, 16 vCPU / 128 GiB each, zero swap (`96` vCPU of the
`512` quota). Levels are sequenced on their predecessor's residual, never
fanned out speculatively. Rollback: any `G0`/`G5` failure quarantines the whole
level and its siblings, because those two gates are correlated across jobs.

---

## 5. Charge 5 — three connections that exist only after the unblinding

**C1. The `w`-ladder crosses `1` exactly at the resonant jump.**
`2 → 3/2 → 2/3` along residue A. Overlay A says root merges live in `w∈(0,1)`;
`(E)` of §1.4 says entries live in `w>1`; `DS2/DS3` say only resonant steps and
merges move `w`. Therefore **root merges are strictly downstream of contraction
events, and contraction events are budgeted** — `ROOT-BUDGET`. Neither DEPTH
(which had `w`), nor overlay A (which had the window), nor MP1 (which had the
budget) states this; it needs all three, and the third only became available as
a *shared* constraint once overlay A removed the `μ=1` hypothesis. It also
converts Fable5's `td=7` observation from an anecdote into the predicted first
live frame.

**C2. `{g=0}` is the common object under `A47`, `RES-AV` and `MERGE-DIFFERENT`.**
Via `J(f,h_1)=αg^{α-1}` (§3.1). Three cards collapse to one computation plus
one page of source reading (`m_{G_m}`).

**C3. The campaign's #1-ranked attack is symmetric-trivial at the layer three of
four reports describe.** §2.2. Worth more than either of the above in the next
six hours, because it prevents three lanes from spending a day confirming
`6/10 = 6/10`.

---

## 6. Charge 6 — ranked six-hour queue

Ranked by expected information per wall-clock hour. Split: **≈70% proof,
≈30% disproof**, with the disproof share deliberately spent on *invalidating*
the finite lane (highest-value negative information available cheaply) rather
than extending it.

| # | window | item | side | stop rule |
|---|---|---|---|---|
| 1 | 0:00–0:45 | Bank `ROOT-BUDGET` (§1.4) with the `MP1` dependency explicit and `ROOT-Y-NE` filed as an open rider. Retract `ROOT-W2` and my "`L1a(b)` is the fragile step" claim. | proof | If a reviewer rules "genuine contact-zero root merge" `≡ V_2\V_1` **and** exhibits a reachable post-jump parent with `μ(1-w)>1`, downgrade to the root-meet branch only and stop. |
| 2 | 0:45–2:15 | `SUBST-TRANSPORT`: the `⊖`-constant / substitution transport across **one** edge `P_i → G_m`, between `p=η²-w_i²` and `p=(η³-c_1³)(η³-c_2³)`, `a_1/a_2=2+√3`. Re-specified per §2.2. | proof | Stop if the transport carries `≥2` free scales per edge (vacuous); stop if St 3.9's `κ` rider cannot be discharged with a common `h`-suitable `κ`. |
| 3 | 2:15–2:45 | `m_F` ruling: read `Not 5.1/5.2` + `Prop 4.2` and decide whether `q_{G_m}` is the `g`-pattern or an `h_j`-pattern (§2.5). | proof | If the printed text does not pin `m_F` at merges, file a source GAP and **stop `RES-AV`, `A47` and all ghost-pricing** until it is pinned. |
| 4 | 2:45–3:15 | Add `PLANT` (§4.2) to the repaired adapter; rerun `Q1P03` level 1. | disproof | Any all-zero-including-plants result quarantines the six banked `D(Δ)` charts pending rework. |
| 5 | 3:15–4:30 | `M≥2` `w`-transfer law (Fable5's `w_child=w(r+l)/(lν+1)`; reproduces `3/2` at `(2,3,1)`). This is the generalization engine for `ROOT-BUDGET` past `td=6`. | proof | Stop if the law needs anything beyond Prop 9.3 (a)–(d) arithmetic; it is supposed to be elementary. |
| 6 | 4:30–5:30 | Conditional on 4: level-1 fanout, five remaining branches, `G0`–`G6`. | disproof | Correlated-gate rollback per §4.4. |
| 7 | 5:30–6:00 | Ledger: retractions (§3.3, §1.3(i)), `Q-GHOST` closed, Sol's Galois insight closed, the two errata of §7.1. | — | — |

Explicitly **not** in the queue, with reasons: any further `λ`/exit refinement
(cannot reach residue A — all four reports agree, and the slack arithmetic is
decisive); a two-parent `Q`-level edge solve (§2.2, tautological); an `m=2` root
recensus (superseded); `Q-GHOST` (void); a `minor atlas` (superseded by §4.1).

---

## 7. Charge 7 — epistemic ledger, errata, scope

### 7.1 Two errata filed

**E-A (datum, canonical + packet).** `SHEET6-2POLE §6a` displays the pole record
as `Q = (D,\deg p,ν,M,κ̄) = (2,2,2,2,5)`, i.e. `M_{P_i}=2`. The same file's
`§2a/§2c/§2d`, `MP4`, `L1a(a)` and `SHEET6-L1 §1` (table (23) row 1) all give
`M_{P_i} = gcd(\deg p, \deg p_g) = gcd(2,3) = 1`, and `MP4`'s own shape
`Q(P_i)=(a α, b α, ν, b, a(α+β))` forces slot 4 `= b = \deg p/α = 1`. Slot 4
should read `1`. The `1707Z` packet §2.4 reproduces the defective value, as do
my `1707Z` report and Grok's §1.1 table (Grok's Card A correctly writes
`(2,2,2,1,5)`, so that report is internally inconsistent); Fable5 wrote
`(2,2,2,·,5)` and avoided it. Non-load-bearing for `Σλ`, `ψ` or the budget;
**load-bearing** for every argument that runs `M=1` at entry → `MP5` → `μ=1`,
which is the backbone of §1 and of Fable5 §10 and Grok §1.2.

**E-B (scope, mine).** `1707Z §3.2` attack point 1 named `L1a(b)` at
`G_m=(0,y)` as "the single most fragile step". It is not fragile; `SHEET6-DEPTH
§1` already defines segments ending "before `(0,y)`". Retracted (§1.3(i)).

### 7.2 Promoted facts consumed, at their scopes only

Overlay A's mixed-root window at **edgewise scope only** (`X_R=μ_e(1-w_e)`,
`X_R=A/B`, `0<w_e<1`); its firewall against inferring `A=Σμ`, `B=r+l`, `k=0`,
no-northeast or `B>A` at an all-`μ≥2` merge is respected throughout. MFE at
selected-exit/shared-inequality scope with the pole-endpoint repair; it is an
inequality and restores nothing. `(C7.1*)`. Corrected Prop 8.4 (nonroot only);
St 8.5 divisibility; root `M=1` legal. `MP0`–`MP7` at their filed perimeters.
`DS1`–`DS4`. `L1a` (printed tier). Table (23) row 1 and the `Λ=3+3` forcing.
Overlay C's six charts as `ENDPOINT_DEAD_ONLY_ON_D(Δ)`; every complement open.

### 7.3 Provisional / conjectural in this report

`ROOT-BUDGET` (§1.4) — new, unreviewed, scoped on-axis `m=2` `td=6` modulo
`ROOT-Y-NE`(a). `ROOT-Y-NE` closure on the four recorded IV classes — sound as
computed, but the class list is not certified exhaustive (`§6b`). The `m_F`
question (§2.5) — open, not decided here. Fable5's `M≥2` transfer law — used
only as a consistency observation, not assumed. `SHEET6-L1.md` remains
**not packet-pinned**; hash `9697f10aa646536927c73c6cc67804a2b62df9dfd8e9c1f42bdb38617bfb4adb`
(unchanged since my `1707Z` read); its "PROMOTED" status is self-asserted and I
did not verify its review chain. `§1.4` step (a) and `§2.2` depend on it.

### 7.4 Retracted / closed this round

Mine: `A47-BUDGET` as a budget (§3.3); the "injectivity already available"
claim; the "both sides explicitly computable" claim; `ROOT-W2` as stated (§1.6);
`L1a(b)`-is-fragile (§7.1 E-B). Peers': `Q-GHOST` void at its first gate
(§2.4); Sol's Galois/inversion obstruction void over `ℂ` (§2.2); the
two-parent `Q`-level edge match as a discriminator (§2.2); per-chart complement
recursion superseded by level-wise Fitting (§4.1). Not revived by anyone and
still dead: printed `(22)`, `(22-cl)`, literal `δ_a`, fixed/cross-fibre `κ`,
equality/slack itemization, MP8's no-refinement claim, dense-open death as
branch death.

### 7.5 Checks actually run

One script, `/tmp/opus5_cross_checks.py`, pure standard library
(`fractions`, `math`, `random`), instantaneous, no CAS, no network, no AWS.
20 checks, **0 failures**:

```text
w-ladder 2 -> 3/2 -> 2/3 ; entry pin w0=2 ; kappabar<nu at suffix only ;
Dg = (+3,-1,-37) ; all four IV classes satisfy w = 1-1/M ; X_R = mu/M <= 1
for every mu|M ; on-axis w0>1 for every admissible (alpha,beta,Lambda) at
td<=6 and the closed form w0 >= (alpha+beta-1)/alpha ; W(2)={2} cap-free ;
W(8/3) = {2/3,4/3,8/3} ; psi=2 ; MFE 2<=3 slack 1 ; +1 gives 3<=3 ;
M_pole = gcd(2,3) = 1 ; A47.1/A47.2 on 18 exact instances ; td(f,h)=alpha*td.
```

Failed attempt, disclosed: I first tried to close `ROOT-Y-NE` in general from
`A ≤ B` (ROOT LAW) and could not — `A>B` is possible once some `μ_c ≥ 2`, so
the closure genuinely needs the `μ_e(1-w_e) ≤ 1` bound and currently holds only
on the recorded book. Second failed attempt: I looked for a `td`/degree ceiling
out of `td(f,h)=α·td`; it gives none, because `τ` is fixed and carries no new
information about `(f,g)` (§3.2).

### 7.6 Custody, contamination, firewalls

Verified before reading, all `OK`: the cross-packet; the five corpus files
(`…-packet.md` `1e40e710…`, `…-sol-ultra.md` `2706e64e…`, `…-grok.md`
`4cbb9182…`, `…-fable5.md` `01cffc70…`, `…-opus5.md` `029dfc67…`); the five
overlay files (`aaa4d179…`, `86b491ad…`, `9f4526f2…`, `f55a00f5…`,
`c74fc0f9…`). This round is **deliberately unblinded**; all four peer reports
were read in full, as instructed. Dependency reads beyond the pinned set, as
licensed by the cross-packet: `ladder/SHEET6-L1.md`,
`ladder/SHEET6-DEPTH.md` (§§0–5), `ladder/SHEET6-2POLE.md` (§§2,4,6),
`ladder/SHEET6-MULTIPOLE.md` (`MP0`–`MP8`), plus a directory listing of
`ladder/`. `jc2-lean` untouched in every sense. No canonical file, case, or
peer report was modified. No AWS, no running job, no heavy or uncertain local
CAS. Sole write: this file. Model: `claude-opus-5`.

### 7.7 Exact scope

Nothing here proves or disproves JC2, excludes `td=6`, closes landing,
`RPMC(C)`, type control or a cofinal ceiling, certifies a root or SF1 census, or
promotes any endpoint/component conclusion. `ROOT-BUDGET` is a candidate at
on-axis `m=2` `td=6` scope with one named rider. The `A47` identities are the
only unconditional new mathematics in this report, and they are elementary.
Every verdict above is a review verdict; **a model verdict is not mathematical
evidence**, and every new item requires the ordinary producer / different-model
hostile / coordinator-promotion gates.

### 7.8 Mid-session custody event — disclosed, re-verified, not fatal

While this report was being written, a concurrent campaign process modified
three files I had already read, plus three I had not
(`cases/book_enum.py`, `cases/book_offaxis.py`, `ladder/BOOK-OFFAXIS-REVIEW.md`).
Post-write hashes:

```text
ladder/SHEET6-2POLE.md      45d08fdb...(base-packet pin, read)  ->  a9085645...
ladder/SHEET6-MULTIPOLE.md  48a5d9cd...(base-packet pin)        ->  f51f2f5c...
ladder/SHEET6-L1.md         9697f10a...(not pinned, read)       ->  69e6e4c1...
ladder/SHEET6-DEPTH.md      ad9ced6c...  UNCHANGED
```

All ten cross-packet hashes (five corpus, five overlay) and this file's own
content are **unchanged**. Read-time status: I hashed `SHEET6-2POLE.md`,
`SHEET6-DEPTH.md` and `SHEET6-L1.md` before use and got the values in the left
column, so those reads are pinned; I did **not** hash `SHEET6-MULTIPOLE.md`
before reading it, so its read is unpinned.

Because `MP0`–`MP7` are load-bearing for §1.4–§1.5, I re-verified every quoted
statement against the **current** files after the change. `MP0` and `MP1` are
byte-identical to what I quoted; `L1a(b)`'s clause, `SHEET6-DEPTH §1`'s
"ending at the last vertex before a merge vertex `G` (`r(G)≥2`) or before
`(0,y)`", `SHEET6-2POLE §4c.2`, and the `§6a` pole display (still
`(2,2,2,2,5)`, so erratum **E-A** stands) are all unchanged. No conclusion in
this report depends on a superseded byte. A coordinator should nonetheless
re-pin `SHEET6-2POLE.md` and `SHEET6-MULTIPOLE.md` in the next packet, since
their base-packet custody values are now stale.
