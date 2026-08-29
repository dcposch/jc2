# Whole-portfolio synthesis — round `20260827T0935Z`

Date sealed: 2026-08-27 09:35Z  
Date synthesized: 2026-08-27 10:36Z  
Coordinator: Sol

Status: **COORDINATOR NAVIGATION AND ALLOCATION DECISION.**  Mathematical
claims retain the evidence tier and lifecycle state of their producer and
review artifacts.  Nothing here proves or disproves JC2, Gate T, order two,
maximum twelve, either `G2` obligation, source/landing coverage, or a terminal
receiver.

## 0. Custody, blindness, and equal-standing researchers

The common packet and four submissions were sealed before any ideator saw
another submission:

```text
packet    e871e3d71a8777ca50f7c796bf7547023a8c2ca8e2930c6a0981ddcebd6ae3db
Sol       98a494a561f39cfef770eec11c07eca3e17e4e9fac61a1a3d143f614d991b90c
Fable 5   098b81d19cba6f278e93a809e60a3a4892eea7979758ffe6b0bb2997163b98c0
Grok      265cfa731dd0e1614966c5eec3367d0dc38a959a2b43a848256c64c4be0b6217
Opus 5    3295402670b65b0a61d56aa9d4f117084b282d649eb72a2afd7df6fe3195782e
```

Fable5 and Opus5 received the same whole-portfolio packet, blindness rule,
maximum-effort setting, tool boundary, and deadline as Sol and Grok.  Model
identity was not used as a vote.  Claims were deduplicated by mechanism and
then attacked.

Cross-pollination:

```text
Fable 5   dd7535ad32bc2e90eabb7829e23d1ff4dd63b5df02b941f6a79aa11ae5d81d48
Grok      e74ade19a9be1b31c476668da44665564f5c2ad84b8a3b700e9d1c6ac19bd490
Opus 5    0fabd42ec761b64824629c96d875886a3e538a883d3925ff2d3b4ed1d4fd7142
```

New Fable/Opus launches reached the shared Claude-account usage cap after the
blind submissions.  Already-running cross-reviews nevertheless completed.
That operational cap delayed launches but did not degrade the sealed blind
round or block the campaign; Grok absorbed time-sensitive new reviews.

## 1. Round headline: one finite decision replaces an exponent ladder

Fable5 and Opus5 independently found the same load-bearing reduction for the
frozen ordered-`a1` total chart.  Let

```text
S=Q[rho,X],       wt(rho)=0, all X positive-weight,
J=the frozen homogeneous literal-total ideal,
K=J:a1^infinity,  J0=J|(rho=0),
T={u(rho):u(0)!=0}.
```

Then

```text
K+(rho)=(1)
  <=> exists N,U, U(0)=1, a1^N U(rho) in J
  <=> a1 in sqrt(J*T^(-1)S)
  <=> [a1 in sqrt(J*Q(rho)[X])] and [a1 in sqrt(J0)]
  <=> the a1=1 dehomogenizations are units over Q(rho) and Q.
```

For the even source, `U` may be taken in `Q[rho^2]`.  The theorem is now
triply derived and hostile-reviewed.  Its clean proof uses:

- the reviewed weight-zero projection;
- the fact that the only coefficient primes surviving localization at
  polynomials nonzero at zero are `(0)` and `(rho)`; and
- the graded-unit lemma, not scaling by fifth roots or a Nullstellensatz over
  `Q`/`Q(rho)`.

The repaired central statement is
`xmodel/max12-812-order2-p0-total-rees-j2-a1-two-fibre-generic-decision-theorem-repaired-sol-20260827.md`.

Promoted V42 already supplies the full special-fibre conjunct.  Therefore one
complete full-system Gröbner computation over `Q(rho)` decides the frozen
chart in both directions.  The running source is even and is compiled over
`Q(t)`, `t=rho^2`; the injective degree-two faithfully flat extension
`Q(t)->Q(rho)` makes unitness equivalent over the two fields.  This bridge is
pinned in `FIELD_BRIDGE_ADDENDUM.md` (`25f52000...`).  The per-exponent ladder
can raise floors but cannot decide existence, and leaves the critical path.

### Selected rows versus all 59 rows

This asymmetry is mandatory:

- a generic **unit** for any literal-row subideal proves the positive result
  for the full ideal;
- a generic **nonunit** for a selected subideal proves nothing about the full
  ideal;
- a complete generic nonunit for all 59 literal rows is decisive for the
  frozen grade-through-19 chart, but remains prefix-relative.

The full ring has 66 positive-weight variables, includes eight rows that
vanish at `rho=0`, and includes the `(3/8)rho^2 a1 ez9` term in `Tg19_2`.
Those general-only terms are exactly why a selected-row or special-fibre
negative cannot be promoted.

## 2. Eliminant dispute: resolved against the advertised third branch

Opus's blind report claimed that the selected-row compiler conflated

```text
E=0
```

with a live case `0!=E subset (t)`, where `E=I cap Q[t]`.  Fable's
cross-review initially endorsed this.  The claim is false under the exact
special control used by the lane.

If `I+(t)=(1)`, then `t` is a unit modulo `I`.  Thus
`t^s q in I cap Q[t]` implies `q in I cap Q[t]`.  Every nonzero eliminant
therefore yields an element nonzero at `t=0`.  Under the passed control, the
current nonzero-constant predicate is already equivalent to `E!=0`.

Opus then independently withdrew its own claim in cross-review and supplied
the correct repair: add an inconsistency sentinel.  If the same-ideal special
control passes but the engine reports nonzero elimination with no generator
surviving removal of a `t`-power, fail closed; do not invent a third success
token.  The phenomenon `0!=E subset(t)` is real only when the special
conjunct fails, e.g. `J=(t x)`.

This is an instructive model comparison: Opus produced a wrong blind code
diagnosis, Fable failed to catch it, Sol and Grok independently refuted it,
and Opus's own hostile pass then gave the sharpest self-correction and the
best mutation guard.

## 3. Constructive positive branch

The abstract decision and the campaign's promotion object are different.
Promotion still requires a literal replay of

```text
a1^N U(rho^2) in J,       U(0)=1.
```

Two constructive formulations now agree.

1. If a special identity lifts as `a1^M-B=tH`, `B in J`, and the generic
   run rehomogenizes to `t^s q(t)a1^D in J`, `q(0)!=0`, then

   ```text
   q(t) a1^(D+M*s) in J.
   ```

2. Opus's Lemma C gives the corresponding general formula: from
   `t^e f^M in I` and `f^m in I+(t)`, infer `f^(M+e*m) in I`.  This is the
   algebra implemented by the existing `clear_power` primitive.

Rehomogenization must first project multiplier terms to the correct weight
class modulo `wt(a1)=5`; the existing homogenizer already implements that
guard.  The constructive special-fibre tree has reduced its candidate target
to `a1^104` and is replaying on AWS.  Until it returns a serialized literal
zero and survives review, `104` is not a theorem.

The separate exact `rho=0` N6 lifecycle is now repaired and complete
(`a3749a7c...`): the independent R1 control checks every one of the 607
`Tg19_7` products, detects the real V42 row-coefficient mutation in exactly
six residuals, restores compiler custody, and promotes
`a1^i notin J0` for every `i<=6` at the frozen grade-through-19 scope.  This
is a valuable certificate floor and consistency gate, but no longer a
decision lane.

## 4. K00: local question effectively decided; mixed deformation becomes next

Sol, Fable5, and Opus5 independently proposed the same global-colon test:

```text
r7 in (r1,...,r6)_(d)
  <=> ( (r1,...,r6):r7 ) is not contained in (d0,...,d5).
```

The V14R1 producer now exhibits

```text
h=63*d4+20, h(0)=20,
h*r7=sum u_i*r_i,
```

with a full 36-entry lift and fresh-process zero replay.  It remains
provisional pending a different-model hostile review.  If it passes, global
nonmembership and local membership coexist exactly as expected; every
`(d)`-adic truncation is compatible, so D9+ cannot discover a first filtered
obstruction and stays stopped.  Opus's independent D8 review already PASSed
the narrower degree-eight theorem and makes D8 a useful consistency check.

The next object is the first-order load deformation of this local membership.
For `phi0:A^6->A`, a chosen zero-order witness `q0`, first variation `phi1`,
and target variation `b1`, use

```text
[b1-phi1(q0)] in (A/I)/im(Syz(phi0) -> A/I).
```

Changing `q0` by a syzygy changes the numerator by the quotient image.  Opus
also caught a tempting wrong version: quotienting by syzygies of all seven
rows is identically vacuous because the known membership witness kills its
own obstruction.  The correct source is `Syz(r1,...,r6)`, with the seven
honest deformed rows pinned as the presentation.  Even then it is an
obstruction in the compiled chart, not honest owner-source attainability,
closure-first incidence, Taylor realization, or a receiver theorem.

V16R1 has producer-PASS evidence that the full 87-generator polynomial
syzygy evaluation has rank one and forces the constant coordinates
`M2(0)=M4(0)=M6(0)=0`; its different-model review is running.  Polynomial
forcing is valid after localization; polynomial non-forcing would not be
complete without a localization argument.

## 5. Unique-`AC` software compression

The uniform contact-shift naturality theorem and generated V0--V4 verifier
remove serial `ACT-TOT-G22/G24/...` exports from the mathematical critical
path.  Grok's V46 review (`13450b72...`) confirmed V0, V1, V3, V4, and
infrastructure sufficiency; V2 has the isolated shifted-root coordinate gap
below and is being repaired additively.  Per-endpoint bridge checks remain.
The direct three-row syzygy is a complementary local certificate, not a
replacement for the schema.  V45's `(2,5,>=3)` instance has separately passed
review and received a narrow contact-only promotion (`99d32a77...`).

The verifier must keep:

- generated rather than hand-written renaming maps;
- endpoint status pinned by promotion hashes, not filenames;
- raw-total versus D1-normalized `C/R` coordinate types;
- a factor-two mutation that detects their conflation;
- the `a=7` load-tie representative;
- single-jet tagging instead of vacuous raw-valuation bounds; and
- a shared alias table flagging the two meanings of `k2c` across the contact
  and ordered-`a1` pipelines.

These results concern strict unique-`AC` on `D(rho)` only.  Ramified
`rho=0`, equality faces, unique-`RC`/`R3`, `k=0`, positive-order leading
loads, Rees charts, receiver coverage, and Gate T remain outside them.

## 6. New structural and orthogonal ideas

After history deduplication, the worthwhile new or newly executable items are:

1. **Origin funnel (Fable; independently echoed by Grok).**  Every homogeneous
   saturated-chart survivor component meets the terminal origin.  Therefore
   receiver work stays load-bearing under either generic-fibre outcome, and a
   negative branch should be parametrized from the origin.  This is support
   geometry, not reachability or an all-depth theorem.
2. **AS109 `n=6` face plus gauge conductor (Fable + Sol).**  Extract the top
   two `y`-degree bands with 109-adic carry constraints, then test the same
   corner in the bounded polynomial-gauge quotient at Witt levels W2/W3.
   Stop after two bands without a new constraint.
3. **Lee--Li compiler retarget (Fable).**  Reuse the exact weighted
   nonmembership engine on the smallest fixed-degree row-9 targets.  Very low
   marginal software cost; idle-capacity only.
4. **Primitive-group sidecar (Fable revival of a historical route).**  One
   GAP/Magma database census with the Orevkov `(48,64)` control.  It consumes
   no AWS algebra quota and no landing-path share.
5. **Bernstein--Sato probe (Fable).**  A named invariant at last, but circular
   unless the hypersurface is pinned before the computation and possibly
   identically trivial for Keller pairs.  Hold for an idle afternoon only.
6. **Jelonek component hygiene (Opus, primary-source checked by Sol).**  The
   counterexample locus is open inside the bounded-degree Keller locus and
   hence dense in every component it meets.  This does not make ambient random
   search useful and supplies no plane component theorem.  The scaling action
   shows the automorphism locus meets every component; any claimed component
   purity would already be equivalent to bounded-degree JC2.  Record this as
   a citation firewall; launch neither component enumeration nor random search.

No external proof or counterexample progress was found in the sweep feeding
this round.  The Jelonek paper is a useful structural reframe, not progress on
JC2 itself.

## 7. Correctness-adjusted model evaluation

### Fable5

Fable5 was the strongest blind ideator this round.  Unique or best-formulated
contributions were the two-fibre theorem, exact selected-row one-sidedness,
the origin funnel, the AS109 face card, the row-9 tooling transfer, and the
largest executed hostile verification on the contact naturality interface.

Its misses were real: the original dehomogenization proof wording, the
overweight assigned to a rational fibre sample, the automatic-cofactor
converter wording, and its cross-review endorsement of Opus's impossible
eliminant branch.  Equal standing does not mean review immunity.

### Opus5

Opus5 did **not** dominate Fable5 in blind ideation.  It independently found
the same two-fibre decision and supplied useful controls and custody census,
but its blind selected-row negative, eliminant third branch, and actionable
Jelonek raise were wrong or overstrong.

Opus5 nevertheless adds significant unique capability.  Its cross-review was
the strongest self-audit of the round and contributed:

- the exponent-explicit clearing lemma and its identification with the
  existing certificate compiler;
- withdrawal of its own eliminant claim plus the exact torsion boundary and
  an inconsistency sentinel;
- the proof that the all-seven-row K00 syzygy quotient is vacuous and the
  corrected six-row obstruction;
- a shared `k2c` alias hazard across two critical pipelines;
- sharp lane-stopping arguments for a proposed specialization probe and for
  its own Jelonek search idea; and
- prior independent byte-level reviews of V43 N6 and K00 D8.

This capability is materially nonduplicative.  Retain Opus5 as an
equal-standing whole-portfolio researcher.  The evidence suggests a useful
post-blind pairing—not a permanent role restriction—in which Fable often
leads theorem/interface reasoning while Opus aggressively attacks proof
objects, source code, custody, and its own claims.

### Sol and Grok

Sol's unique contributions were the executed K00 colon lane, constructive
certificate tree, direct three-row contact lemma, AS109 gauge-conductor,
Jelonek primary-source correction, and portfolio integration.  Sol missed
the two-fibre reduction in the blind phase and initially left N7 too high.

Grok's best contribution was the scope/transport firewall and its hostile
repair of the two-fibre proof and compute plan.  It independently refuted the
eliminant third branch and kept the general-only rows visible.  Its blind
specialization/floor card and local-order repair were superseded.

## 8. Four merged executable cards

### Card 1 — `TA1-GENERIC-DECISION`

Continue the already-running full 59-row exact `Q(t)` computation on AWS;
the pinned faithful field bridge makes it the exact `Q(rho)` decision.
Selected-row lanes remain one-sided; the constructive tree supplies an
effective special certificate.

- **Unit:** lift, residue-project modulo weight five, rehomogenize, combine
  with the special certificate if needed, and replay a normalized even
  cofactor.  Stop N-duals and high-memory exponent hunts.
- **Complete nonunit:** prove `K+(rho)!=(1)` for the frozen prefix, stop the
  N-ladder, and unhold grade-20+ only to attack the explicit survivor.
- **Timeout/OOM/incomplete basis:** no verdict; only then consider an
  unrestricted unseeded next-exponent fallback.

### Card 2 — `K00-MIXED-COKERNEL`

Finish the V14R1 review and V16R1 review.  On V14R1 PASS, permanently stop
D9+ and compute the six-row first-order load obstruction.  A nonzero class is
the first load-aware compiled K00 exclusion; zero triggers one full loaded
colon, then honest owner-source reachability.  Do not infer a germ from either
outcome.

### Card 3 — `UAC-LINKER-FREEZE`

Build and review V46R1's isolated root-map repair, and finish the
direct-three-row review with the mutation and alias guards above.  The common
schema/naturality review has already passed, so serial higher-grade exporters
leave the unique-`AC` critical path; a V46R1 failure would restrict only the
shifted-root linker duty.  V45 is narrowly promoted for one contact.  Coverage
and ramified/equality-face work continue independently.

### Card 4 — `AS109-N6-FACE`

Run the top-two-band face calculation and W2/W3 gauge quotient as an
orthogonal counterexample-side lane.  Add the primitive-group census as a
no-contention sidecar.  No lower bands or broad support enumeration without a
new mechanism.

## 9. Launch, continue, hold, stop, and allocation

**Already running, continue without waiting on reviews:** full 59-row generic
`Q(t)` (equivalently `Q(rho)` by the pinned bridge); selected-row
exact/modular lanes; constructive `a1^104` replay;
V14R1/V16R1 reviews, V46R1, and the direct-contact review; closure-first
receiver work; TD6 to its registered caps.  V45 is already narrowly promoted.

**Launch as slots free:** Card 2's first-order mixed quotient after its input
review gate; Card 4's two desk-scale reads; shared alias table; row-9 retarget;
primitive-group census.  These do not contend with the large AWS algebra run.

**Hold:** unseeded N7 unless the generic lane has no verdict; b-function to
idle-only; Jelonek/component search; full `3P-E31`; descendants of provisional
contact claims.

**Stop:** dead fixed N7 seed; per-N ladder as an existence method; whole-unit
high-memory multiplier extraction as a primary lane; K00 D9+; V11/V13 local
ordering repair; serial higher-grade unique-`AC` exports after the V46 gate;
random bounded-degree counterexample sampling from the ambient space.

Target research allocation after current jobs settle:

```text
40%  ordered-a1 generic decision, certificate, and survivor follow-up
25%  K00 mixed deformation, honest reachability, and receiver incidence
15%  unique-AC linker plus the uncovered ramified/equality/coverage faces
10%  AS109/TD6 and other counterexample-side work
10%  hostile review, software gates, integration, and web surveillance
```

Review remains nonblocking: once a result is provisionally credible, its
descendants may start under an explicit dependency label while adversarial
review runs in parallel.  Review reversal rolls back the dependent subtree;
unrelated lanes never wait.
