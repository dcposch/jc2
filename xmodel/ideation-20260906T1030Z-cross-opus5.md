# Adversarial cross-exchange — Opus 5 — round ideation-20260906T1030Z

Custody: read only the charged list. Verified all indexed hashes before any
body: packet body 5890 B `f74aaf7e02e18f64…`; `collection.json` full-hashes for
astra `30bf0356…`, fable5 `a307783e…`, opus5 `82147acb…`, sol56 `f4ee3f30…`,
coordinator `1bb91823…`, FALLACY `e47fd16c…`; declared body seals recomputed
and matched for cross-packet, the four astra pilots, fable5's blind body (its
self-declared seal agrees with `collection.json`) and coordinator `b7858e26…`.
Four files carry no `## Seal` block (astra/opus5/sol56 blind bodies, fable5's
K16 gate); those are covered by `collection.json` or unindexed by design — I
record `k16-boundary-product-gate-fable5-20260906.md` = `d40a0aef…` as
**unindexed in any charged manifest**. No live CROSS or uncharged report was
opened. Nothing below repairs my own blind submission retroactively.

## 1. Strongest surviving mechanism

**Uniform corank bound on the C block** (opus5 §3(b), independently reached by
fable5 §4.2; coordinator Card 2 asks for the same object). Its surviving core
is exactly: `ker` of the *complete-coefficient* C-block `= V ∩ ker J(·,G)`,
`ker J(·,G) = k[G̃]` (closed-polynomial theorem), and `G_top = y^18(y−x)^48`
forces `deg G̃ ∈ {11,22,33,66}`, so with `deg C ≤ 35` the kernel has dimension
`≤ 4` at **every** parameter point. That is a genuine uniform theorem: no
genericity, no localization, no modular lift. Everything else in the linear-C
cluster (rank 191, the 189/190 pivots, the maximal-minor unit ideal) is either
a measurement at points or a basis-existence statement, and is strictly weaker.

## 2. Strongest refuted / overstated inference

**fable5 §4.2: "every Keller point has `M` of full column rank and `(C,a)`
uniquely determined".** The rows of `M` are the *positive-degree* Jacobian
coefficients, so a kernel element `P = C + (a/2)h` satisfies `J(P,G) ∈ k`, not
`J(P,G) = 0`. fable5 states the kernel condition as `J(C,G) = 0` (dropping both
the constant and the `a`-direction) and then applies Arzhantsev–Petravchuk,
which needs the zero. This is the packet's Q1 defect in its sharpest form, and
the post-cutoff transverse report does not repair it: that report reaches only
the *conditional* "at an actual Keller point the positive `(C,a)` block is
injective mod constants", and states that the unconditional stronger block
**fails at `D=b=0`**. Under the round rule, fable5's blind claim stands refuted
as written. opus5 §3(b) is not subject to this: it claims `≤4`-dimensional
kernel and rank `≥188`, and its "exactly 191" is explicitly generic + measured.
Second overstatement, smaller: opus5 §3(c)'s two modular points give
`rank_Q ≥ 191` **at that point** hence generically; the packet is right that
this is not "191 everywhere", and astra's own control below shows it is not.

## 3. Concrete composition of peers' ideas (new, desk-proved)

Compose opus5 §3(b)'s top-form divisibility with astra's positive-only
distinction and the campaign's own `n ≤ 100` baseline, to close Q1:

Let `P ∈ V_C ⊕ k·h`, `deg P ≤ 35`, with `J(P,G) = c ∈ k` (the true positive-only
kernel condition).

* If `c = 0`: opus5 §3(b) applies verbatim — `P ∈ k[G̃]`, `dim ≤ 4`.
* If `c ≠ 0`: the degree-`(deg P + 64)` part of `J` is `J(P_top, G_top)`, which
  must vanish, so `P_top, G_top` are algebraically dependent forms, hence powers
  of one primitive form. `G_top = y^18(y−x)^48 = L^6` with `L = y^3(y−x)^8`
  primitive of degree 11. Therefore **`11 | deg P` and `P_top = λL^{deg P/11}`,
  `deg P ∈ {11,22,33}`** — unconditionally, no genericity, char 0, over `k̄`.
* Further, `max(deg P, deg G) ≤ 100`, so Moh's degree-≤100 theorem makes `(P,G)`
  an automorphism, whence `G` is a coordinate and `G_top` is a scalar times a
  power of a *linear* form. `y^18(y−x)^48` has two distinct linear factors.
  **Contradiction: `c ≠ 0` is impossible.**

Consequence: for this frozen family the positive-only kernel *equals* the
complete-coefficient kernel, so the uniform `≤4` bound and rank `≥188` survive
the Q1 objection, and fable5's conclusion is true after the correct proof — but
only as of this composition, not as of its blind submission. Two honest riders.
(i) The `c ≠ 0` kill is **conditional on Moh ≤100 as a citable published
theorem**, which is precisely what the campaign's own residue lane is auditing;
the unconditional residue is the finite top-form check `deg P ∈ {11,22,33}`.
(ii) The check is **not vacuous**: astra's own literal control exhibits `P` in
the actual C-space with `J(P,G) = 0` at `G = H^6`, `P = H^3` (coefficients
`1,3,3,1` at `A3c_87_{8..11}`). So a nonconstant kernel element does occur at
parameter points of the family, and any claim of rank exactly 191 *everywhere*
is false; only `≥188` is uniform, and 191 needs the transverse-line hypothesis.

## 4. Attack on the transverse-line theorem and the 190-pivot lemma

* **Source support.** The theorem's hypotheses are literal: `h(X,0)=X+c`,
  `G(X,0)` monic quadratic, `deg G = 66`, `G_top = H^6`. Astra's own controls
  show each hypothesis is load-bearing (drop transversality → kernel exists;
  drop C-support → kernel exists with the correct leading form). So the "full C
  kernel constants everywhere" theorem is *everywhere on the transverse
  restriction*, which is a proper subvariety condition on the parameter space,
  not on the family. Reporting it as "uniform rank 191" would identify a chart
  hypothesis with the family — the FALLACY flag/place/series item.
* **Positive-only.** The report is explicit that its unconditional statement is
  the `J=0` block, and that positive-only injectivity is conditional at a Keller
  point. Accept as written; §3 above is what upgrades it, and it upgrades it
  only modulo Moh ≤100. `J(X, X^2+W)=1` is the report's own witness that
  positive-only ≠ full in general.
* **Nonreduced limits / degeneration.** Everything is a rank statement at
  geometric points. Rank is lower semicontinuous, so `rank ≥ 191` is *not*
  closed: it can drop on the boundary of the transverse locus, and `D=b=0` is
  named as a point where the stronger block fails. Any downstream use inside a
  saturation or a limit (where the ideal is nonreduced, or where `Zj·J0−1`
  forces a chart) must re-prove the hypothesis at the limit point, not inherit
  it. No promoted statement should read "full rank on the Keller locus" until
  the locus is known reduced there.
* **190-pivot lemma.** The triangularity argument is correct as stated —
  `[W^{r−1}]J(P,G) = −r p_r(X) G_X(X,0)` with `G_X(X,0)` of degree 1 giving the
  constant `−2r` at position `(i+1,r−1)`, and the W-order/X-degree ordering
  makes the selected submatrix triangular. Three limits, all conceded by the
  author and worth pinning: (a) it is an *existence* statement in an adapted
  rational basis; the source transformation is not emitted, so the elimination
  cost is unmeasured and the 1.046×/pivot fill-in law is not excluded — the
  basis change itself may densify what the pivots then eliminate; (b) it gives
  190 of 191, and the residual column is exactly the expensive one — a unit
  ideal without a constant entry or a Bezout expression is not a computational
  win; (c) `dim V_0 = 190` uses `image = span{1,X}`, i.e. `h(X,0)=X+c` literally
  — the same hypothesis as above. **Verdict: mathematically sound, currently a
  theorem-interface improvement with zero measured runtime benefit.** This is
  not a substitute for a different-model source/code gate.

## 5. Re-ranked bottlenecks

Proof side: (1) source→stage-8 **necessity** (still GAP; unchanged by this
round, and nothing here touches it); (2) an all-degree K16 obstruction — the
post-cutoff boundary result *removes* a hoped-for nonexistence route by
returning marked rational solutions to polynomial ones; (3) properness /
case-exclusion. CE side: (1) any nonvacuous point-level oracle on the complete
physical ideal (600 vars, 1629 rows) — the exact-Q slimgb timeout at 600.959 s /
33.29 GiB and the msolve 32-bit `calloc` overflow (`11,299,180×600` wrapping to
2,484,540,704) mean the current engines give *no* signal at all; (2) reducing
the 439 physical coordinates to 248 via the C collapse; (3) elimination cost.
**Declaration for this exchange: `NO_NEW_MECHANISM`** on the proof side. §3 is a
repair-and-sharpen of an existing mechanism, not a new one.

## 6. Cheapest discriminating experiment

**`TOPFORM-KERNEL-CENSUS`** — decide, exactly and unconditionally, whether the
positive-only C kernel can be nonconstant on the actual source, without Moh.

* Procedure: from the frozen `delta2_stage8.strongest.json` (`778eda93…`),
  extract the 192 C basis polynomials and `h`; for `m = 1,2,3` compute the
  linear condition "`P_top ∝ L^m`, `L = y^3(y−x)^8`" on `V_C ⊕ k·h` by matching
  the degree-`11m` homogeneous component; report the solution dimension.
* Assumptions: the C-space is the certified 192-dim rational injection; degrees
  `deg C ≤ 35`, `deg h = 33`, `G_top = y^18(y−x)^48` as recorded.
* Cost: **estimated** ≤ 10 min desk, exact rational linear algebra on ≤ 3
  matrices of size ≤ 36×193; no CAS, no fleet. Not measured here.
* Interpretation: dimension 0 for all `m` ⇒ positive-only injectivity mod
  constants is proved **unconditionally**, Q1 closed, and fable5's conclusion
  holds without Moh. Dimension > 0 ⇒ the surviving candidates are an explicit
  finite list; each is then either a `J=0` element (already covered) or must be
  killed by Moh ≤100 — and the list is exactly the set of parameter points where
  rank 191 can fail, which is what the transverse hypothesis is buying.
* Stop condition: stop if the extracted `G_top` or `deg h` disagrees with the
  record (source misreading, not mathematics), or if the `m=3` block reproduces
  astra's `1,3,3,1` control — that is the known solution and needs no rerun.

Explicitly **not** proposed: a capped modular solve of the complete ideal, an
allocation-safe parser retry, or 1000 LM starts. On the packet's Q6: the
allocation-safe modular parser is the only one of the four that can change a
rank, but it changes nothing about the *mathematics* until §3/§6-style structure
cuts 439→248; do that first, since it is free.

## 7. Post-cutoff facts used (labelled)

Producer-cost result (24 pivots / 575 vars / 668 rows / 9,967,234 terms), the
complete-Q slimgb timeout and msolve overflow, the K16 boundary promotion, and
the transverse-line report (PRODUCER-CHECKED, NOT PROMOTED) are all post-cutoff
and were not blind input. None of them retroactively repairs any blind claim,
including my own §3(c) generic-rank measurement.

## 8. Systems upgrade

**Choose: audit-heading index** (fable5 §7), bounded to a read-only
`ops/audit_index.py` parsing both heading grammars and failing if a `17(…)`
token in LIVE STATE is unindexed. Benefit: a real, demonstrated failure mode —
an old-grammar reader silently reports 02:51Z as newest and drops eight
promotions. Risk: none (read-only, no ledger write). Opportunity cost: ~15 min,
which is less than one re-derivation of a dropped promotion. Rejected: the
contract checker (larger, overlaps the seal conventions question) and durable
harvest catch-up (no failure demonstrated this round). `NO_UPGRADE` would leave
a live stale-state hazard for every mechanical reader, including blind ideators.

## 9. Continue / redesign / stop

* **Linear-C collapse** — CONTINUE, with §6 first and with "rank ≥ 188 uniform,
  191 only on the transverse locus" as the promoted wording.
* **Complete physical-J ideal (600×1629)** — REDESIGN. Both engines failed; the
  inclusion of T2/T3 points does not establish dominance for unit search
  (packet is right). Re-enter only after the 439→248 reparametrization.
* **2 TB T2/T3 build** — STOP (already operator-stopped); retain partials.
* **K16 boundary lane** — CONTINUE but downgrade expectation: the boundary
  promotion is a lemma about the rational category, not an obstruction, and the
  `t`-model is anti-invariant hence adds no equation. Queue the follow-on round.
* **Numerical variable projection** — REDESIGN before any 1000-start run:
  unmeasured per-iteration cost, and the packet's zero-J/inverse-escape and
  precision controls are not yet designed. Not infeasibility evidence either way.
* **Source→stage-8 necessity** — CONTINUE as the top proof obligation.

## OPENS RAISED

- OPEN[TOPFORM-KERNEL-CENSUS]: is `dim{P ∈ V_C ⊕ k·h : P_top ∝ L^m}` zero for
  `m ∈ {1,2,3}`? QUANTITY: solution dimension `= 0` closes Q1 unconditionally.
  Cheapest test: §6, estimated ≤ 10 min desk.
- OPEN[MOH100-DEPENDENCY]: the `c ≠ 0` kill in §3 depends on Moh ≤100.
  QUANTITY: `max(35, 66) ≤ 100`, so the dependency is inside the campaign's own
  audited range. Cheapest test: cite the audited residue lane's verdict.
- OPEN[K16-GATE-UNINDEXED]: `k16-boundary-product-gate-fable5-20260906.md`
  (`d40a0aef…`) appears in no charged manifest. QUANTITY: 1 unindexed charged
  input. Cheapest test: add its hash at packet freeze.

FALLACY-v2: no floor read as attainment (rank `≥188` is not 191); no
flag/place/series identification (transverse hypothesis kept distinct from the
family); ring maps and the primitive form `L` declared with degree checks; no
cap or analogy fills the `c ≠ 0` branch — it is closed by a cited theorem and
otherwise returned as a typed OPEN. No exit-price assertion is made, so no
`charge_basis` line is due.

<!-- BODY-END -->
