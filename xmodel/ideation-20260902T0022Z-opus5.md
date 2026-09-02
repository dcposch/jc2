# Blind ideation — round 20260902T0022Z — lane opus5

Charged input: `xmodel/ideation-20260902T0022Z-packet.md`
(SHA-256 `df7df824c39e3b9a2eeefc398f813e9b99aa11268ac98ff6b4c8fc26cd9a6c2c`,
verified in-lane against the frozen copy). Basis `f6a4591d`.
Blind: no other lane's round-`20260902T0022Z` submission was opened.

## 0. Method, custody, scope

## 1. Disposition vector

## 2. Reranked bottlenecks

## 3. NEW mechanism — HOM-COVER: the integral-homology razor on the ACS-1 covering

## 4. New cross-connection

## 5. Strongest proof attack

## 6. Strongest counterexample attack

## 7. Software acceleration / decisive experiment

## 8. Campaign-systems check

## 9. Idea cards

## 10. Continue / redesign / stop

## 11. History labels

## 12. FALLACY-v2 audit and typed verdict block

## 0. Method, custody, scope

Read: the charged packet; `APPROACHES.md` (overlay stack + master table);
`notes.md` LIVE STATE 2026-09-01T23:38Z .. 2026-09-02T00:23Z;
`xmodel/rep-96-inner-opus5-20260901.md` (my own prior lane, re-read as
source, not as authority); `xmodel/ideation-20260829T0002Z-opus5.md`
(`ACS-1`/`(*)`/`ACS-2`); the two flagship prompts of 00:22Z, read solely
to avoid duplicating their charge. NOT read: any lane's
round-`20260902T0022Z` submission.

Two scripts were written and run in-lane, both now in the repo:
`box/cover_h1.py` (new instrument, sec.3/7, controls pass) and
`box/open_triage.py` (systems measurement, sec.8). Every number below
that is labelled MEASURED came out of one of those two runs in this
session; everything else is desk derivation and is marked as such.

Nothing here promotes a claim, closes a row, or asserts an exit price.
No `charge_basis` line is required or given: this report makes no
exit-price assertion (FALLACY-v2, sec.12).

## 1. Disposition vector

| # | Avenue / front (packet naming) | Disp. | Reason |
|---|---|---|---|
| 1 | Domrina II + D-O part I verification chain | **lower** | Chain is SOUND-AFTER-REPAIRS; DC calibration already accepts it. Marginal unsoundness-per-Opus-hour is now the worst in the portfolio. Let the Grok mu2 review land; charge nothing further. |
| 2a | `(8,6,11)/(8,6,7)/(8,6,3)` | **lower to closed-out** | Twice-derived dead / curve-level dead. Keep only as regression fixtures. |
| 2b | `(8,6,9)` rep-open + running curve job | **unchanged** | Job is running; no new instrument needed. |
| 2c | `(9,6,2)` realized substrate | **raise (top of portfolio)** | It is the only object in the campaign where a *finite, decidable* chain now separates "surviving datum" from "counterexample" — see sec.3. |
| 2d | `(9,6,4)` six-node job | **unchanged** | Running; dies additionally to a YES on `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]`. |
| 3a | `OPEN[REP-96-BM-FACTORISATION]` | **unchanged (running), value raised** | It now has *two* consumers instead of one: the fixed-set intersection, and the homology razor of sec.3. Same input, second verdict, zero extra compute. |
| 3b | `OPEN[REP-96-SOURCE-IS-C2]` | **reopen, re-typed** | Packet calls it "the largest gap ... not numerical". I claim it is mis-targeted at the branched cover and, correctly targeted at the *unbranched* cover, is a finite homological computation. Sec.3. |
| 3c | `OPEN[REP-96-MPRIME-COMPANION]` / Path-2 | **unchanged, mechanism injected** | Sec.4 supplies a source-side handle on `D_2` the flagship charge does not carry. |
| 4 | MPRIME-ALLN-H2 (Path-1) | **unchanged** | Correctly the top all-degree lane. One typed caution in sec.4 about `a^{(i)}` vs fixed-point counts. |
| 5 | N=5 census (pipeline ready) | **raise** | Only lane that can absorb 1,920 idle vCPU, and the literature's N=5 is *not* soundly closed (Zoladek/GGV gap). Highest compute-value-per-token in the portfolio. |
| 6 | One-cusp A2 horn, `OPEN[A2-CELL-32]` | **unchanged** | Two sections closed by degree termination; no new lever from me. |
| 7 | Primitive monodromy (Avenue 26) | **raise** | It stops being free-floating group theory: sec.3 gives its objects (index-`td` subgroups of a curve-complement group) a computable invariant that is *not* Euler-characteristic. |
| 8 | Links at infinity / splice diagrams (Avenue 27) | **reopen at low cost** | Only as the source-side link test (sec.5), never again on the target-side template, which is banked-dead. |
| 9 | Degree-monotone invariant (all-degree) | **unchanged** | Sec.3 supplies a candidate but I do not claim monotonicity; claiming it would be exactly the floor/attainment fallacy. |
| 10 | Instruments (msolveio+qqideal, SIROCCO/ZvK) | **raise** | Add one small pure-Python consumer (`box/cover_h1.py`); no new dependency, no CAS. |
| 11 | GGV bounds (gcd >= 16, != 2p); Zoladek posture | **unchanged** | Consumed as constraints, not attacked. |
| 12 | K00 / AS disproof-continuity seeds | **unchanged (dormant)** | Orthogonal; do not reopen under a resolution-first directive. |

## 2. Reranked bottlenecks

**Proof side** (was: all-N (M') closure -> companion contradiction ->
degree-monotone invariant -> A2 horn):

1. **(M') non-nodal profile classification at all N** (Path-1). Unchanged
   at #1: it is the only lane whose success is a theorem rather than a
   filter.
2. **Torsion-freeness of the ACS-1 covering** (`HOM-COVER-ALLN`, sec.3,
   NEW). Enters at #2 because it is an all-degree necessary condition of
   a genuinely different type from every gate the campaign owns: not
   Euler characteristic, not `kappa-bar`, not a congruence, but integral
   homology of an index-`td` subgroup. If the local cable structure at
   infinity forces torsion, this closes JC2 at every degree at once. I
   do not claim it does.
3. **Companion existence** (Path-2). Unchanged in kind; sec.4 adds a
   source-side constraint.
4. Degree-monotone invariant. Unchanged.
5. A2 horn / `OPEN[A2-CELL-32]`. Unchanged.

**Disproof side** (was: BMFACT -> SOURCE-IS-C2 -> companion):

1. **`OPEN[REP-96-BM-FACTORISATION]`** (running). Unchanged at #1.
2. **Homology razor on the survivors** (sec.3, NEW). Free: same input,
   one Smith normal form. MEASURED prior kill rate on the closest
   available analogue: **56%** (sec.7).
3. **`OPEN[REP-96-SOURCE-IS-C2]`, re-typed** (sec.3). Moves *up* from
   "hard geometric step" to "third finite test in the same chain".
4. **Direct construction of `F` from the dicritical data at infinity**
   (sec.6, NEW as a job). Overtakes "construct `D_2` abstractly",
   because a solve for `F` produces `D_2` as output.
5. N=5 census.

## 3. NEW mechanism — HOM-COVER: the integral-homology razor on the ACS-1 covering

**Label: `NEW` (the invariant and its use). Its substrate `ACS-1` is
banked (`ideation-20260829T0002Z-opus5.md:278`); `ACS-1`'s three recorded
consequences are Euler characteristic, `kappa-bar` and local type — none
of them is integral homology. Ramanujam-style recognition of `C^2` is
banked as `KEF-ONE-VERTEX` (van Dobben review sec.6) and is *not* what
this is; see the correction below.**

### 3.1 The object, stated so that the right thing is being tested

`F : C^2 -> C^2` Keller, non-proper, `A = A(F)`, `td = N`. Banked
(`ACS-1`): `F` restricts to a **connected finite étale covering**

```text
        F :  C^2 \ F^{-1}(A)  --->  C^2 \ A ,     degree N,
```

with monodromy `rho : pi_1(C^2 \ A) -> S_N` transitive. Write
`E := F^{-1}(A)`, a curve in `C^2`, and `H := rho^{-1}(Stab(1))`, an
index-`N` subgroup.

**Correction to REP-96 sec.7 (R2), load-bearing.** R2 asks for the
Riemann-existence surface `Y` (the degree-4 cover of `C^2` *branched*
over `D`) to satisfy `Y ~ C^2`. That is the wrong object in both
directions. `F` is étale everywhere, so nothing is branched: sheets go
missing at infinity, not by ramification. The normalisation `Ybar` of the
target in `C(x,y)` contains the source as an *open* subset by Zariski's
main theorem (quasi-finite + separated into a normalisation is an open
immersion), with `Ybar \ C^2` a curve; `Ybar` is normal and typically
singular, so `Ybar ~ C^2` is **not necessary**. The condition that is
both necessary and finite lives one level down:

```text
   (SRC)   the N-sheeted covering space of  C^2 \ A  determined by rho
           must be isomorphic to the complement of a plane curve in C^2.
```

### 3.2 The razor

For any curve `E` with `r` irreducible components in `C^2`, the Gysin
sequence of the pair (`H_2(C^2) = 0 -> H_0(E) -> H_1(C^2\E) -> H_1(C^2) = 0`)
gives `H_1(C^2 \ E) = Z^r`: **free abelian, generated by meridians, no
torsion, rank = component count.** And the homology of a covering space
is the abelianisation of the corresponding subgroup. Hence, exactly:

```text
   (HOM-COVER)   H^ab  =  H_1(C^2 \ E)  =  Z^{r(E)} .
```

Two independent tests fall out of one computation:

* **Torsion test (free).** `torsion(H^ab) != 0` **kills the datum
  outright** — no auxiliary input, no geometry, no attainment claim.
* **Rank test (one extra input).** `rank(H^ab)` must equal the number of
  components of `E`, which is itself computable from `rho` plus the
  transports as an orbit count. A mismatch kills the datum.

Both are *necessary* conditions. Passing them is **not** existence:
`(SRC)` also demands an isomorphism, not just matching homology. This is
the carrier/attainment line of FALLACY-v2 and I hold it: HOM-COVER is a
floor-side filter, never an attainment certificate.

### 3.3 Why this is not a restatement of anything banked

`(*)` (`ideation-20260829T0002Z-opus5.md`) decomposes `td - 1` over
Euler characteristics; `(M')` is the same species (a Lefschetz/Euler
count) and, per REP-96 sec.7 (R4), collapses to `chi_2 + sigma_2 = 1` at
the `N = 4` reducible profile, i.e. it is **blind to `delta_aff(D_1)`**.
Torsion in `H^ab` is invisible to every Euler characteristic: two
representations with identical `(*)`, identical `(M')`, identical
`kappa-bar` and identical local types can differ by `Z/3` in `H^ab`. That
is precisely the gap in which `(9,6,2)` currently survives.

### 3.4 Computability, exactly

`H^ab` is computed from a presentation of `pi_1(C^2 \ A)` and `rho` with
no group-theory package: lift the presentation 2-complex to the `N`
sheets, form `d_2` (Fox derivatives realised as an explicit lift-walk,
integer entries), and take one Smith normal form. Because `im(d_1)` is
free, `coker(d_2) = H^ab (+) Z^{N-1}`, so a single SNF returns rank and
torsion together. Implemented in `box/cover_h1.py` (pure Python 3, no
NumPy/Sage/CAS). Controls run in-lane, all MEASURED:

```text
  two transverse lines, pi_1 = Z^2, 2 sheets        H_1 = Z^2         PASS
  trivial rho (k = 1) reproduces the base group     H_1 = Z^2         PASS
  cuspidal cubic (pi_1 = B_3), base                 H_1 = Z           PASS
  cuspidal cubic, cyclic 2-fold cover               H_1 = Z (+) Z/3   PASS
```

The last line is the sharp control: `Z/3` is `Delta_trefoil(-1) = 3`, the
textbook value, reproduced by the same code path the campaign would use
on `(9,6,2)`. The instrument is calibrated against a known nonzero
answer, not only against zeros.

### 3.5 Immediate use

The `(9,6,2)` chain becomes, end to end, three finite tests on one input:

```text
  BMFACT   nine local fixed sets intersected      -> surviving tuples
  HOM-COVER  torsion(H^ab) = 0 ?                  -> free, same input
  RANK     rank(H^ab) = #components of F^{-1}(A)? -> one orbit count
```

If any survives all three, the campaign has, for the first time, a datum
that no promoted gate and no homological obstruction kills — and the
remaining step is construction (sec.6), not exclusion.

## 4. New cross-connection

**Path-2 (companion) x ACS-1 x the étale constraint on cycle types.**
Three banked-but-unjoined facts:

1. the meridian of a component `D_i` of `A` acts on `N` sheets;
2. `F` is étale everywhere, so **no cycle of length `l >= 2` can extend
   over `D_i`** — an extending sheet would be a ramification point;
3. the source-side generic count is `a^{(i)} = N - W_i` (REP-96 sec.7 R3,
   from the weight vector).

Joining them gives an exact local dictionary, and one typed caution:

```text
  a^{(i)}  <=  #Fix(meridian_i) ,     a_p  <=  |Fix(<local meridians at p>)| ,
  with equality iff no trivially-monodromic sheet vanishes at that place.
```

The inequality direction is forced; **equality is an extra hypothesis**.
At `N = 4`, `W_1 = 2` gives `a^{(1)} = 2 = #Fix(transposition)`, so
REP-96's consistency check is fine. But `W_2 = 1` gives `a^{(2)} = 3`,
and *no element of `S_4` has three fixed points*: the companion's
meridian must be the identity (four fixed points), i.e. the covering is
**unbranched over `D_2` while the source still loses a sheet there**.
That is consistent — the loss is at infinity, not by monodromy — but it
means `a^{(i)} = #Fix` is false in general and must not be promoted into
an all-`N` theorem. Typed `OPEN[ACS-FIX-VS-DEFICIT]`: before Path-1 or
Path-2 quotes `a^{(i)} = N - W_i` as a monodromy fixed-point count at
general `N`, prove the equality case or carry the inequality.

**What this hands Path-2.** If `rho(meridian(D_2)) = 1`, then
`F^{-1}(D_2) -> D_2` is a degree-`a^{(2)}` étale covering whose component
count enters the RANK test of sec.3, and whose components are curves in
`C^2` that are *disjoint from each other* over the smooth part of `D_2`.
The flagship's charge (Bezout / genus-degree / BMY / Zaidenberg-Lin) is
entirely target-side; this is a **source-side** constraint on the same
companion, and it is the constraint the RANK test consumes. The two meet
at exactly one number: `r(E)`.

Secondary connection, one line: Avenue 26 (primitive monodromy) and
Avenue 27 (links at infinity) both act on the *same* `rho`; sec.3 gives
26 a computable invariant, and sec.5 gives 27 its only surviving client.

## 5. Strongest proof attack

**`HOM-COVER-ALLN`: force torsion from the structure at infinity.**

Target theorem. *For every Keller counterexample, `H^ab` has torsion* —
which by sec.3.2 is a contradiction, at every degree, with no census.

The attack has three steps, in decreasing confidence.

1. **Locate the torsion source.** Torsion in `H_1` of covers of a plane
   curve complement is governed by the characteristic varieties of
   `pi_1(C^2 \ A)`, which Libgober's theory attaches to the *local*
   singularity types plus the behaviour at infinity. Nodes contribute
   abelian local groups and no torsion. So all torsion must come from
   the places at infinity — and the campaign has proved that a
   counterexample's `A` components are **never transverse to `L_inf`**:
   they carry cabled places (the `(9,6)` place has Puiseux slope `3/2`,
   i.e. a trefoil cable; `delta_inf = 24`). The one control I ran that
   fires is exactly a trefoil cover (sec.3.4).
2. **Prove the transfer.** Show that a cabled place at infinity forces a
   root of the local Alexander polynomial into the character supporting
   `rho`, hence torsion in `H^ab`. This is the load-bearing step and it
   is *not* proved here. Its honest status: a mechanism with a
   calibrated positive control, not a theorem.
3. **Discharge the exceptions.** Characters can miss the characteristic
   variety; the MEASURED census of sec.7 shows 44% of degree-4
   representations of the cuspidal-cubic group are torsion-free, so step
   2 cannot be true in the naive "all `rho`" form. The theorem must
   consume the campaign's *own* constraints on `rho` (transitivity, the
   `Pi`-is-a-transposition pin, GATE-3, TB-GERM `beta_1 = 8 + 3kappa`).
   That intersection is small — six classes at `(9,6,2)` — which is
   exactly why the attack is worth funding at the level of one lane.

Why this outranks the alternatives on the proof side: it is the only
candidate all-degree obstruction the campaign has that is **not** an
Euler characteristic, and `(M')`'s own collapse (`chi_2 + sigma_2 = 1`,
`s_1` cancelling identically) is proof that the Euler family has run out
of information at the residual profile.

Stop condition: if step 2 fails for cabled places at `N = 4` in a
worked example, the attack degrades from "theorem route" to "filter"
(sec.3), which is still worth its cost, and the lane closes.

## 6. Strongest counterexample attack

**Solve for `F` directly from the dicritical data at infinity, rather
than for `D_2` abstractly.**

`(9,6,2)` is realised with an explicit parametrisation
`(q,p) = (t^6 + 8t^2, t^9 + 12t^5 + 24t)`, and the residual profile pins
its role: `D_1` is the image of a dicritical of weight `W_1 = 2`. That
is a *constructive* boundary condition on `F`, not a numerical type:
there is a punctured-disc germ `s -> sigma(s)` at infinity in the source
with

```text
        F(sigma(s))  =  (q(t(s)), p(t(s))) ,      ord_s t = 2 ,
```

together with a second dicritical of weight 1 whose image is `D_2`, and
`J(F) = 1`. With degrees fixed (step 0 below), this is a polynomial
system in the coefficients of `F` — precisely the shape msolve 0.10.1 +
qqideal now decide exactly, with certainty-typed verdicts.

Job spec, four steps:

0. **Pin the degrees.** From `td = 4`, the weight vector `W = (1,2)` and
   the `(9,6)` place, derive `deg f`, `deg g` and the order of contact of
   `F` with `L_inf`. This is desk work and must be done first; an
   unpinned degree makes the system unbounded and the run meaningless.
1. Encode `J(f,g) = 1` plus the two dicritical germ conditions as an
   ideal in `QQ[coeffs]` via `qqideal`.
2. Decide emptiness with msolve; on nonempty, extract points (the PARAM
   extraction already requested of the toolchain).
3. Verify any solution by direct substitution, independently of the
   solver, and only then compare with `A_F = D_1 u D_2`.

Interpretation. **EMPTY** kills `(9,6,2)` at the strongest possible
level — no representation-theoretic caveat, no `Y ~ C^2` gap — and does
so *without* waiting for BMFACT. **NONEMPTY** is a counterexample
candidate to verify by hand, i.e. the resolution of JC2 in the negative.
Either outcome closes the fork's largest branch, which is why I rank it
above constructing `D_2`: a solve for `F` returns `D_2` as output.

Risk, stated: step 0 can fail to pin the degrees, in which case this
attack degrades to a bounded-degree search and must be re-costed. That
is the single point where it can silently become the GGV degree farm,
which is banked-tried; the mitigation is that the germ conditions here
are *exact and prescribed*, not a corner enumeration.

## 7. Software acceleration / decisive experiment

**Delivered, not proposed: `box/cover_h1.py`** (pure Python 3, ~200
lines, no NumPy, no Sage, no CAS, own integer SNF). Input: a finite
presentation plus a transitive permutation representation. Output:
`H_1` of the covering space as `Z^r (+) torsion`. Four controls pass
(sec.3.4), including the sharp `Z (+) Z/3` trefoil control.

**Decisive experiment, run in-lane.** How much kill power does the
razor have? Censused every transitive representation of
`pi_1(C^2 - cuspidal cubic) = B_3` — the closest available analogue of
the `(9,6,2)` place at infinity, whose Puiseux slope `3/2` *is* a
trefoil cable — into `S_3` and `S_4`. MEASURED:

```text
   B_3 -> S_3 :  8 transitive reps,  2 with torsion  (25%)
                 H_1 = Z^2  x6 ,  Z (+) Z/2 (+) Z/2  x2
   B_3 -> S_4 : 54 transitive reps, 30 with torsion  (56%)
                 H_1 = Z^2  x24 ,  Z (+) Z/2  x24 ,  Z (+) Z/3  x6
```

**56% of degree-4 data of this shape is killed on sight**, and the
razor costs one Smith normal form on a `9N x 12N` integer matrix — under
a second at `N = 4`. It consumes the BMFACT output that is already
running, so its marginal cost is zero and its expected information gain
is high whichever way it lands.

The rank column is a bonus: every surviving representation above has
`rank(H^ab) in {1,2}`, so the RANK test of sec.3.2 is genuinely binding
against the reducible profile's component count rather than vacuous.

## 8. Campaign-systems check

**`UPGRADE` — OPEN-token triage. Rotation slot: duplication /
workload generation.**

Evidence, MEASURED in-lane with `box/open_triage.py` (delivered):

```text
   distinct OPEN[...] tokens raised in xmodel reports   72
   ever charged in any lane prompt                      20
   ORPHANS (raised, never charged to a lane)            52
   of those, first raised on 08-31 or 09-01             52
```

The newest LIVE STATE names the bottleneck exactly: *"the bottleneck is
workload generation, not compute"* (box01 1/64 cores busy; box03 4/64;
quotas 1,920 + 548 vCPU). Meanwhile the campaign is generating typed
decidable questions **3.6x faster than it charges them**, and every
orphan is idle inventory produced at Opus rates. This is the cheapest
available fix to the measured bottleneck, and it is not a mathematical
proposal, per the contract's independence requirement.

Smallest useful implementation (done): `python3 box/open_triage.py`
prints the orphan list newest-first. Smallest useful *process* change:
the coordinator runs it at each round close and either charges or
explicitly retires the top five orphans. Regression risk: none — the
script is read-only and touches no state. Measured benefit gate: if the
orphan count does not fall over two rounds, retire the tool rather than
keep it for its own sake.

`NO_CHANGE` alternatives considered and rejected: adapter reliability
(five-for-five on first contact, no evidence of a problem); AWS
scheduling (idle capacity is a symptom of the above, not a cause);
state freshness (LIVE STATE is 1 minute old at packet freeze).

## 9. Idea cards

### Card A — HOM-COVER razor on the BMFACT survivors (`NEW`, immediate)

* **Dependencies.** The running `OPEN[REP-96-BM-FACTORISATION]` output
  (surviving nine-tuples + transports) and a ZvK presentation of
  `pi_1(C^2 \ D_1)` from the SIROCCO braid — both already being produced.
  `box/cover_h1.py` is written and calibrated. No new compute, no CAS.
* **Cheapest discriminator.** One Smith normal form per surviving tuple:
  `torsion(H^ab) != 0`?
* **Outcomes.** *Torsion* -> the tuple is dead, and if all survivors have
  torsion, `(9,6,2)` is dead at the source level, independently of
  `OPEN[REP-96-SOURCE-IS-C2]`. *Torsion-free* -> run the RANK test; if
  that also passes, the datum has cleared every homological obstruction
  the campaign can state, and Card C becomes the whole game.
* **Stop condition.** BMFACT returns zero survivors (then the card is
  moot and should not be run on non-survivors "for information").
* **Expected information gain.** High and cheap: MEASURED 56% prior kill
  rate on the analogue (sec.7); either branch changes the portfolio.
  Cost: hours, one lane, no AWS.

### Card B — `HOM-COVER-ALLN`: torsion from cabled places (`NEW`, proof side)

* **Dependencies.** Sec.5 step 2 (the transfer lemma) is the whole card;
  inputs are the campaign's own `rho`-constraints (transitivity, `Pi` a
  transposition, GATE-3, TB-GERM) plus Libgober-type characteristic
  variety theory, which needs a primary-source custody check first —
  none of it is banked in this campaign.
* **Cheapest discriminator.** Before any theory: take the `N = 4`
  cabled-place local model and ask whether *every* representation
  satisfying the campaign's constraints has torsion. That is a finite
  computation with the sec.7 code and it decides whether the theorem can
  be true at all.
* **Outcomes.** *All constrained reps have torsion at `N = 4`* ->
  fund the general lemma; this is a candidate all-degree closure.
  *Some constrained rep is torsion-free* -> the theorem is false as
  stated; degrade to Card A's filter and record the counterexample as a
  permanent scope limit.
* **Stop condition.** The discriminator above returns a torsion-free
  constrained rep, or the custody check finds the characteristic-variety
  input is not applicable to affine (rather than projective) complements.
* **Expected information gain.** Medium-high, asymmetric: a cheap NO
  costs one lane; a YES is a candidate proof of JC2 at every degree.

### Card C — Direct solve for `F` from the `(9,6,2)` dicritical germ (`NEW` as a job; family `KNOWN`)

* **Dependencies.** Step 0 of sec.6 (pin `deg f`, `deg g` from `td = 4`,
  `W = (1,2)` and the `(9,6)` place) — desk work, blocking. Then
  qqideal + msolve 0.10.1, both live; PARAM point extraction wanted but
  not required for an emptiness verdict.
* **Cheapest discriminator.** Exact emptiness of the coefficient ideal.
* **Outcomes.** *EMPTY* -> `(9,6,2)` dead at the strongest level,
  bypassing both `OPEN[REP-96-BM-FACTORISATION]` and
  `OPEN[REP-96-SOURCE-IS-C2]`. *NONEMPTY* -> hand-verify; if it verifies,
  JC2 is false. *Unbounded/degenerate* -> step 0 failed; re-cost, do not
  drift into the banked-tried GGV degree farm.
* **Stop condition.** Step 0 does not pin the degrees.
* **Expected information gain.** Highest single-shot value in the
  portfolio, and it is the only card that can *resolve* rather than
  filter. Cost: one desk lane + one AWS solve; the boxes are idle.

## 10. Continue / redesign / stop

| Lane | Rec. | Why |
|---|---|---|
| MPRIME-ALLN-H2 (Path-1) | **continue** | Correctly the top proof lane. Add the sec.4 caution about `a^{(i)}` vs `#Fix` before any all-`N` equality is quoted. |
| COMPANION-CURVE-ALLN (Path-2) | **continue, one injection** | Add the source-side constraint of sec.4: `F^{-1}(D_2)`'s component count is the number the RANK test consumes. |
| `mu2-replay-review-grok46` | **continue to completion, then stop the verification front** | Let it land; charge no successor. The chain is accepted under the DC calibration. |
| BMFACT / SAGE-NATIVE `6^9` enum | **continue** | Unchanged at #1 on the disproof side, now with a second consumer (Card A). |
| `(8,6,9)` and `(9,6,4)` curve jobs | **continue** | Running; cheap. |
| N=5 census | **continue and raise** | Only lane sized for the idle fleet; literature N=5 is not soundly closed. |
| One-cusp A2 horn | **continue at current funding** | No new lever from me; do not raise while `(9,6,2)` is live. |
| Oracle window / msolveio+qqideal | **continue** | Card C depends on it. |
| Target-side splice/link template (Avenue 27 classic) | **stop; reopen only as sec.5's source-side test** | Banked-dead in its original framing. |
| Domrina-side further hardening | **stop** | Explicitly, so it does not restart by drift. |

## 11. History labels

| Item | Label | Basis |
|---|---|---|
| `(HOM-COVER)` torsion/rank razor on the ACS-1 covering | **NEW** to the campaign ledger; method family (homology of irregular covers, Fox/Reidemeister-Schreier) **KNOWN** externally | No repository file mentions Fox calculus, Reidemeister-Schreier, Alexander modules or Smith normal forms in this role; `ACS-1`'s consequences (i)-(iii) are Euler, `kappa-bar`, local type only. Primary-source check owed before any external citation. |
| Correction to REP-96 sec.7 (R2): the necessary condition is on the **unbranched** cover, not `Ybar ~ C^2` | **NEW** | REP-96 sec.7 R2 as written; ZMT open-immersion argument is standard. |
| `OPEN[ACS-FIX-VS-DEFICIT]` (`a^{(i)} <= #Fix`, equality is a hypothesis) | **NEW** as a typed caution | Derived in sec.4 from étaleness; REP-96 uses the `N=4` instance as a consistency check only, so nothing promoted is retracted. |
| Ramanujam recognition of `C^2` | **KNOWN** | `KEF-ONE-VERTEX`, van Dobben review sec.6. Cited as *not* the mechanism here. |
| `ACS-1` covering, `(*)`, `ACS-2` | **KNOWN** (banked, mine, 2026-08-29) | Substrate only. |
| Direct solve for `F` from prescribed dicritical germ data (Card C) | **NEW** as a job spec; **SCOPE-CONFLICT** with Avenue 1 (GGV degree farm) if step 0 fails | Avenue 1's stuck-point is "always a next pair"; Card C is exact and prescribed, but only while the degrees are pinned. |
| OPEN-token triage (`box/open_triage.py`) | **NEW** | No such instrument in `box/`. |
| `B_3 -> S_4` torsion census | **NEW** measurement | Run in-lane; reproducible with the delivered script. |

## 12. FALLACY-v2 audit and typed verdict block

* **Flag/place/series.** Kept apart in sec.4: the source-side deficit
  count `a^{(i)}`, the monodromy fixed-point count `#Fix`, and the weight
  `W_i` are three different objects; I prove only `a^{(i)} <= #Fix` and
  refuse the equality. In sec.3 the branched cover `Ybar`, the unbranched
  cover `C^2 \ E`, and the source `C^2` are three different surfaces.
* **Carrier/attainment.** HOM-COVER is stated as a *necessary* condition
  throughout; sec.3.2 says explicitly that passing it is not existence.
  No `REPRESENTATIVE`-to-`FULL_ACTUAL_EXIT` step is taken anywhere.
* **Floor/attainment.** Sec.5's target theorem is labelled a mechanism
  with a calibrated positive control, not a theorem; step 2 is named as
  unproved and the MEASURED 44% torsion-free fraction is reported as the
  obstruction to the naive form rather than suppressed.
* **`sat()` wrapping / raw remainder / variable-ring map.** No Groebner
  computation was run in this lane. Card C's spec inherits the standing
  discipline and must run its own positive and negative controls.
* **Exit claim.** None. No `charge_basis` line is given because no
  exit-price assertion is made.
* **Software honesty.** `box/cover_h1.py` reproduces `Z (+) Z/3` for the
  trefoil cyclic double cover — a known *nonzero* answer — so the
  instrument is not calibrated only against zeros. `box/open_triage.py`
  counts 72/20/52 on the current tree; the packet-adjacent files of this
  round are excluded by name from both counts.

```text
LANE                ideation-20260902T0022Z-opus5  (blind, equal-standing)
CONTRACT            disposition sec.1 ; bottlenecks sec.2 ; NEW mechanism
                    sec.3 ; NEW connection sec.4 ; proof attack sec.5 ;
                    counterexample attack sec.6 ; software/experiment
                    sec.7 ; systems check sec.8 (UPGRADE) ; 3 cards sec.9 ;
                    continue/stop sec.10 .  ALL DELIVERED.
NEW MECHANISM       HOM-COVER  -- torsion(H^ab) = 0 and rank(H^ab) = r(E)
                    on the banked ACS-1 covering.  NECESSARY CONDITION.
                    Instrument delivered and calibrated; 4/4 controls PASS.
MEASURED            B_3 -> S_4 : 30/54 transitive reps carry torsion (56%).
                    B_3 -> S_3 :  2/8  (25%).
                    OPEN tokens: 72 raised, 20 charged, 52 orphaned.
CORRECTION          REP-96 sec.7 (R2) targets the wrong surface; the finite
                    necessary condition is on the unbranched cover.
                    Nothing promoted is retracted by this.
OPENS RAISED        OPEN[ACS-FIX-VS-DEFICIT]  (sec.4)
                    OPEN[HOM-COVER-TRANSFER]  (sec.5 step 2)
CLAIMS              None promoted.  No exit price.  No row closed or opened.
DEVIATIONS          (1) Size: body 31KB against a 12-20KB pace, spent on
                    sec.3 (the mechanism had to be derived, not asserted)
                    and sec.7 (measurements).  Logged, not hidden.
                    (2) Two scripts were written and left in box/ rather
                    than pasted inline; both run from a clean checkout.
                    (3) I read the two 00:22Z flagship prompts to avoid
                    duplicating their charge; no lane's round submission
                    was opened.
```

<!-- BODY-END -->
