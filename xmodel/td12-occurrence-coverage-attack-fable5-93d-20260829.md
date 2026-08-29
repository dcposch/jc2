# Independent attack — global occurrence/coverage versus td12

Date: 2026-08-29 UTC  
Researcher: Fable 5, equal-standing whole-portfolio lane  
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`  
Lifecycle: `PRIMARY_ATTACK_REPORT / NO_PROMOTION / FAIL_CLOSED`

## 0. Executive disposition

1. The requested implication graph is built in §2 with exact quantifiers.
   Every arrow from `JC2 false` down to a Sigray-normalized pair with a
   finite per-`td` entry menu is proved or conditional as already ledgered;
   every arrow from there to `td=12`, to the `[2,2,2]` entry, to the U1
   equality record, or to a named B25/S17 occurrence is **absent**, and
   several natural strengthenings are **false**.
2. The strongest honest occurrence theorem available today is a
   conditional trunk dichotomy *inside* the U1 equality record (§3). I
   attempted it seriously and it produced a sharp negative: even
   conditional on an actual td12 U1 equality landing, the conclusion
   "…contains a named actual B25 or S17 occurrence" is **refuted at the
   reduced/pinned-arithmetic tier**. The budget-legal terminal menu of the
   U1 trunk is not `{B25, S17}`: I exhibit hand-verified additional
   fitting terminal cells, a budget-legal continuation *out of* the B25
   state itself, and at least one `nu`-unbounded fitting family. The
   correct codomain is the finite-state reduced closure, not a two-cell
   list (§3.4–§3.6).
3. Current premises cannot force `td=12` or the U1 equality route. §4
   gives the interface no-go and three concrete escaping admissible
   families, two of them already frozen in the reviewed record.
4. The smallest materially useful new lemma is the family-aware
   `MERGE-FREE-TRUNK-TERMINAL-CLOSURE` (§5): exact hypotheses,
   conclusion, proof skeleton, dependencies, cheapest falsification, and
   non-duplication argument are given.
5. §6 audits the six requested cross-connections. No complete arrow
   exists; none is promoted.

No `PairRef`, source value, occurrence, attainment, degree ceiling,
counterexample, or JC2 conclusion is asserted anywhere in this report. All
prices consumed below are promoted `REPRESENTATIVE` AF2 floors at declared
cells; no new exit price is asserted, so no `charge_basis` line is due.

## 1. Sources actually read and consumed

Read in full this session at the frozen basis: the Sol 5.6 coordinator
source-interface audit (`body 76faa25a...`), the round synthesis
`ideation-20260829T1517Z-synthesis.md` (`body 2f5b6271...`), the current
overlays of `APPROACHES.md` (through 2026-08-29 16:35Z), `PROGRESS.md`
(2026-08-29 entries), and `AUDIT.md` (16:35Z promotions);
`ladder/REDUCTION.md` in full (T1–T10, Critical Gaps 1–7, §§5–7);
`ladder/TRANSPORT.md` in full; `ladder/SHEET6-AF2.md` in full;
`ladder/BOOK-OFFAXIS.md` §§0–2, 6–8 (status header, entry census, chain
calculus R1.0–R1.5, merge anatomy R2, td=7 history).

Reviewed td12/U1/B/S/entry/carrier artifacts read in full: the U1 trunk
consumer hostile review (`body 86ccd2f1...`), the sibling exact-charge
producer (`body 306d69f6...`), the sibling T1 ratio-solve review (verdict
`PASS`, `B/A=(9±3i)/8`), the next-trunk-discriminator producer and its
review verdict (`PASS_WITH_REPAIR`, exact `lambda_{F,B}=8`), the
pole-entry price producer (`POLE-EXIT-ZERO`, `body 9fcc2c5c...`), the B
bridge coordinator integration (`body 89fc2555...`), the S bridge
coordinator integration (`body dcc03cbc...`), the formal cascade-rank
integration (`body 3dfaa862...`), the source-mass floor producer (`body
42993a40...`) and its Fable 5 hostile review (`FAIL`, repaired lemmas
ASM'/NM', `body 1ca3948f...`) with the Sol erratum (`body 26631d03...`),
and the td12 global-budget kill producer plus its Grok review disposition
via the binding correction (`body 71681036...`). Carrier and LL-1 scope
were consumed through their binding overlay/ledger summaries
(`FULL_ACTUAL_EXIT=FULL_ACTUAL_FIRST_SEPARATION`, finite-`s`,
lower-floor-only; LL1-R4 `13->7` at `td=6` one fibre).

Desk scratch: one exact integer/fraction enumeration script in `/tmp`
(pure Python, no CAS, seconds of CPU), used only to *verify and extend* a
hand computation over the reviewed reduced grammar; §3.6 discloses its
tier honestly. No web, AWS, commit, push, canonical edit, or external
message. `jc2-lean` was not read, listed, stat'ed, built, or touched.

## 2. The exact quantified implication graph

Notation: `∃!`-free; each arrow carries its quantifier discipline.
Existential choices are never merged across different pairs or fibres:
the pair is selected once (A1); the fibre variable `a` remains universal
until a route names one; route data live on one named fibre of the one
selected pair.

```text
N0  JC2 false.

A1  N0 => ∃ (P,Q) GGV-minimal standard counterexample
    [PROVED, refereed GGV1; existential over ALL counterexamples;
     minimizes gcd(deg P,deg Q), NOT td; no control of td(P,Q)].

A2  selected (P,Q) => Sigray-normalized (f,g)=C∘(P,Q)∘R of the SAME pair,
    td preserved, type (alpha,beta), GGV ledger losslessly recoverable
    [PROVED, TRANSPORT Thms 1.1/2.1/3.1 + (4.1)-(4.5); selected-pair
     scope only].

A3  td(f,g) >= 6  [PROVED, Żołądek Thm 6.12, refereed].

A4  ∀ fibre a: mass identity td = Σ_F Λ(F) and a finite entry menu E(a)
    at each FIXED td [mass: PROVED relative to the audit-corrected
    inputs + Chau; entry parameterization (M=b pin etc.): CONDITIONAL on
    the corrected Sigray/TDU/MP package].

A5  ... => td = 12
    [ABSENT. No upper bound on td exists (CRITICAL 7); td in
     {6,8,9,10,12,14,...} all carry live single-pole/on-axis/off-axis
     survivors (HIGH 1/2); td=13 has 129 OPEN off-axis cells; td=11 has
     no certified census. Any assertion of this arrow is FALSE].

A6  td=12 => entry [2,2,2] of type (2,3)
    [ABSENT as stated: td=12 also has 71 surviving single-pole search
     classes (4 solver-OPEN kinds + a depth frontier), 12 surviving
     on-axis modeled cells, and other off-axis entries.
     CONDITIONAL variant (route-shaped, reviewed): IF the configuration
     has three disjoint arrival subtrees each of arrival multiplicity
     >= 2, THEN td >= 3·max(beta,2·alpha) >= 12 (repaired ASM'/NM'),
     and equality at td=12 forces type (2,3) and three (a,b,nu)=(1,2,3)
     poles. The antecedent is a route property, not a consequence of
     minimality].

A7  [2,2,2] => the U1 equality record
    [ABSENT. The merge-skeleton menu at this entry contains at least:
     (i) the reviewed U1 arity-3 equal-join record, (r,mu,eps,w) =
         (3,2,0,3/2), merge AP n ≡ 1,5 (mod 6), n >= 5 — formally ALIVE;
     (ii) the labelled NESTED-U2-P0-U2-RAY (w=1 arrivals) — DEAD at
         td=12 by the reviewed representative budget kill 5+5+1=11>10;
     (iii) the nested-binary skeleton with per-chain dirty steps
         (3/2,2)->(21,15,7)@w=2/3, mu=3 arrivals — typed OPEN in the
         reviewed source-mass FAIL review §5; NOT killed by (ii), NOT
         the U1 record;
     (iv) two-stage binary equal-join variants — unclassified.
     Nothing selects (i)].

A8  U1 record => constant reduced trunk state (w,M)=(9/2,2), n-free;
    merge price 0; three pole prices exactly 0 (POLE-EXIT-ZERO)
    [PROVED at reviewed reduced tier].

A9  U1 trunk => a named actual B25 or S17 occurrence
    [FALSE at the reduced/pinned-arithmetic tier — §3.4-§3.5 below.
     The reviewed one-step statement ("exactly two P1-fitting terminals
     among the 13 first edges") is correct and reproduced; the
     multi-step budget-legal terminal set is strictly larger and
     contains nu-unbounded families. The honest replacement arrow is
     "=> a terminal cell of the finite-state reduced closure" — still
     CONDITIONAL on grammar totality at actual tier].

A10 B25 occurrence => functorial native chart, greedy landing at
    s*=25(i+r)-17, landing ODE soluble iff 8B=9A, first resonance j=17
    identically vacuous [PROMOTED CONDITIONAL, named-actual-occurrence
    scope]. S17 occurrence => shear/floor/sibling/degree map, FLOOR-COORD
    WLOG gauge, deg f >= 136i [PROMOTED CONDITIONAL].

A11 B25/S17 => reviewed contradiction
    [ABSENT: B25 is T1-alive (B/A=9/8) with exact extra-branch charge 8
     and slack 1; S17 is T1-alive (B/A=(9±3i)/8) with exact charge 4+4=8
     saturating its budget; both source gates (24/16 pure-power levels)
     are necessary-only and unvalued].
```

Summary: the graph has a proved spine `N0 -> A1 -> A2 -> A3 -> A4` and a
proved conditional interior `A8`, with **every** selection arrow
`A5, A6, A7` absent and the coverage arrow `A9` false as spelled. The
missing global implication is therefore not one arrow but three stacked
selections plus one coverage statement, and the coverage statement needs
a different codomain even conditionally.

## 3. The strongest honest occurrence/coverage theorem — attempt and outcome

### 3.1 Setup and the six requested mechanisms

Fix the hypotheses of the U1 equality record on one named fibre `a`:
td=12, type (2,3), three `(1,2,3)` poles, one arity-3 equal-join merge
`G` with arrivals `(mu,w)=(2,3/2)` and index `n ≡ 1,5 (mod 6)`, `n>=5`.
Reviewed facts consumed: at source-mass equality each arrival subtree
has exactly one pole leaf (two poles would carry mass `>= 2*beta = 6 > 4`),
so the three pre-merge chains are merge-free and pairwise disjoint;
pole vertices price exactly zero (`POLE-EXIT-ZERO`); the merge prices
zero; the trunk below `G` is merge-free to the root and starts at
`(w,M)=(9/2,2)`, independent of `n`.

The six mechanisms named by the mission map onto this record as follows.

- **Earliest-marked-event.** The first non-neutral trunk event is
  well-defined after neutral quotienting and lies in the reviewed
  13-edge menu, complete at the maximal budget 10.
- **Actual-path termination.** The actual tree is finite (MP0), so the
  trunk reaches `(0,y)` in finitely many events; every priced event
  spends `lambda >= 1` of the shared Corollary 7.1 budget
  `sum lambda <= td-1-psi`, so at most `td-2 = 10` priced events occur.
- **Complete pole-side subtree.** Discharged at equality: three
  merge-free single-pole chains, price 0 each, seed `(3/2,2)`; in the
  U1 record the arrivals are at seed, so the pre-merge chains are
  neutral-only and quotient away.
- **Neutral-transition quotienting.** Reviewed safe: every zero-price
  P0 move weakly decreases reduced `w` and neutral moves fix `(w,M)`
  (`zero_cost_reduced_nonincrease`); quotienting preserves the typed
  state.
- **Unused branches.** Every dirty vertex spawns priced NE branches;
  their cv flags are the lambda payload; their jets are gated (the
  reviewed 24-level pure-power gate at B25 and the 2×16-level gate at
  S17) but unvalued.
- **Downstream-context preservation.** The terminal typing
  `j=M(1-w) ∈ Z>=1`, `psi=ceil(M/j)-1`, and the root Statement 8.5
  divisibility are the downstream context; the budget ceiling depends
  on the terminal's `psi`, so intermediate states may not be priced
  against any fixed `psi`.

### 3.2 The theorem shape that is actually available

> **Conditional trunk dichotomy (honest form).** Assume an actual typed
> landing of the U1 equality record. Then the trunk continuation,
> quotiented by neutral steps, is a finite priced path in the reviewed
> reduced P0 grammar from `(9/2,2)`; its last event is a P1-legal state
> (`0<w<1`, `j=M(1-w) ∈ Z>=1`) whose route satisfies
> `sum lambda <= 11 - psi`; and consequently the actual continuation
> lands in the finite-state reduced closure of `(9/2,2)` at ceiling 10.

Riders required beyond the promoted set: (i) totality of the §10 P0
grammar at actual tier (every actual non-neutral trunk event is a
grammar step — the repaired-R1.3-including-IIb perimeter; this is
exactly the "no unclassified transition" clause of CRITICAL 4/5); and
(ii) terminal typing at the root for a single arriving chain (the
`H3-psi` formalism presupposes `w<1` with integral `j` at the last
event; the reviewed root-merge kill R2.1(iv) covers merge arrivals, not
the single-chain root arrival — this rider is inherited by every
existing td12 budget statement, not introduced here).

### 3.3 What I proved about the codomain — reproduction first

I re-derived the one-step menu by hand from R1.3/R1.4/R2.2 and the
derived AF2 rule
`lambda >= Σ_j max(1,⌈X/m_j − kbar⌉) + [eps>0]·max(1,⌈(X/eps−kbar)/nu⌉)`
and reproduced the reviewed record exactly: the four P1-shaped one-step
children `(2/3,3)@25`, `(3/4,4)@17`, `(5/6,6)@13`, `(9/10,10)@11`, all
at `lambda=8`, with budgets `9,8,6,2`, exactly the first two fitting;
the `lambda=6` continuations at `nu=7` (`k=1`) and `nu=5` (`k=2`); the
four `eps=1` cells at `lambda=9`; the pure-epsilon cell at `lambda=9`.
My arithmetic agrees with the Opus review field-for-field wherever both
computed.

### 3.4 The negative result: `{B25, S17}` is not the terminal set

The reviewed "exactly two P1-fitting terminals" is a **one-step**
statement. Multi-step budget-legal routes exist. Three witnesses,
each hand-verified against every reviewed filter (E>0, NE `m_j·dq<dp`,
(R) `dp≠mu*·dq`, `kbar ∈ Z>0`, N1 `gcd(kbar,nu)=1`, `gcd(M,nu)=1`,
`dq≡1 (mod nu)`, `l | M_upper` (St 8.4), `gcd(nu_upper,l)=1` (R1.5),
all gaps positive, AF2 floors, Cor 7.1 ceiling):

```text
W1: (9/2,2) --D(l=2,k=1,nu=7),lam=6--> (2,3)  [cell (21,15,7), kbar=15]
          --D(l=3,m=2,nu=27),lam=3--> (2/5,5) [cell (135,55,27), kbar=11]
    total 9, terminal j=3, psi=1, budget 10: FITS, slack 1.

W2: (9/2,2) --same lam=6--> (2,3)
          --D(l=3,m=2,nu=7),lam=2--> (6/5,5)  [cell (35,15,7), kbar=9]
          --D(l=5,m=4,nu=13),lam=1--> (2/3,9) [cell (117,27,13), kbar=9]
    total 9, terminal j=3, psi=2, budget 9: FITS, slack 0.

W3: as W2 to (6/5,5), then --D(l=5,m=4,nu=49),lam=2--> (2/9,9)
    [cell (441,99,49), kbar=11]; total 10, j=7, psi=1, budget 10: FITS.
```

Every one of these terminal cells passes reduced Proposition 8.1(iv)
(T1) with a one-dimensional kernel, by the same computation pattern the
review validated at `nu=25` and `nu=7`: for the shape
`p=(t−C)^l (t−D)^(l−1)`, `q=eta(t−C)(t−D)`, `t=eta^nu`, the top
coefficient cancels identically (`rho·dq = dp`), and the linear
coefficient forces one ratio: `D=2C` at `(l,nu)=(3,7)` and `(5,13)`;
`D=(6/5)C` at `(3,27)` and `(5,49)`. All side conditions
(`C≠D`, both nonzero, `C_iv=rho·C·D≠0`) hold. So none of W1–W3 meets a
reviewed contradiction, and each ends at a P1-legal cell that is
neither B25 nor S17.

Two structural aggravations, found by extending the same enumeration:

1. **B25 is not even continuation-terminal.** From the B25 state
   `(2/3,3)@25` (spent 8) the grammar admits the legal dirty step
   `l=3, m=2, nu=7` at `lambda=1` to `(2/5,5)@7`
   [cell (35,15,7), kbar=3; `gcd(25,3)=1`], total 9 `<= 10`, `psi=1`.
   Reaching the B25 state therefore does not force terminating there:
   the B25 *occurrence* (with its `kappa_F>17` chart, landing row, and
   jet gate) is one branch of a choice that the budget does not decide.
2. **A `nu`-unbounded fitting family exists.** Through
   `(9/2,2) -> (9/4,4) [l=2,ms=(1,1),nu=5, lam=6, cell (20,16,5)]
   -> (9/10,10) [l=4,ms=(3,3),nu=13, lam=2] -> (6/19,19)
   [l=10,ms=(9),nu=47, lam=1]`, the pure-epsilon step `l=19, eps=7`
   yields `w=19·(6/19)/12 = 1/2` **independently of `nu`**, with
   `M=gcd(12,nu+1)=12` exactly on `nu ≡ 11 (mod 12)` and `lambda=1`:
   an arithmetic family `(1/2,12)@{nu ≡ 11 (12)}` of budget-legal
   terminal cells (total 10, `j=6`, `psi=1`, budget 10). This is the
   CRITICAL-5 "unbounded last-vertex `nu`" leak occurring *inside* the
   U1 record itself, on the trunk.

### 3.5 Consequence for `TD12-U1-ACTUAL-LANDING`

The coordinator audit's narrowest missing lemma reads "…every actual
continuation of the reviewed U1 record either meets an already reviewed
contradiction or contains a named actual B25 or S17 occurrence." As
spelled, this is **false at the tier at which B25/S17 are alive**:
W1–W3 are continuations meeting no reviewed contradiction and containing
neither state; the `(1/2,12)` family shows the set of such continuations
is not even finite as a list of `(w,M,nu)` cells. Any true landing
theorem for the U1 record must have as codomain the *reduced closure*:
the finite set of reachable `(w,M)` states (my superset enumeration
finds 83 within ceiling 10) together with their `nu`-family fibres
retained as family records, exactly the family-aware codomain REDUCTION
§5.1 item 4 already prescribes for full-configuration books. A two-cell
codomain is available only if some presently unreviewed law kills every
multi-step route; no such law is in the promoted set — the only
candidates (exact prices above floors; T1 failures; per-cell jet gates)
are either open or verified to pass on W1–W3.

### 3.6 Verification tier disclosure

The one-step reproduction, the three witnesses W1–W3, the B25
continuation, the `(1/2,12)` family membership, and all T1 solves in
§3.4 were computed **by hand** and cross-checked against the reviewed
cells. Separately, a `/tmp` exact-arithmetic scratch enumeration of the
same grammar (necessary-condition superset: it does not apply per-cell
T1 or jet gates) reproduced the reviewed 13-edge first-step menu
field-for-field, confirmed W1–W3 and the two aggravations, and reported
83 reachable reduced states and ~517 fitting `(w,M,nu)` terminal cells
within its scan bounds. The 83/517 figures are scratch-tier superset
counts, not reviewed results; the individually hand-verified objects
above are the load-bearing evidence. Nothing in this section asserts an
actual landing, realizability, or attainment: every `lambda` is a
promoted `REPRESENTATIVE` AF2 floor at a declared cell, and "FITS"
means "not excluded by floors," never occurrence.

## 4. Can current premises force `td=12` or the U1 route? No — interface no-go

**Claim.** No composition of promoted statements at basis `93db679d`
derives, from "JC2 is false" plus the A1–A4 spine, any of: `td=12`; the
`[2,2,2]` entry; the U1 equality record; or a B25/S17 occurrence.

**Proof at the level of logical interfaces.** Classify every promoted
statement touching topological degree into the four shapes that
actually occur in the ledger: (S1) existential selection (A1) and
td-preserving normalization (A2), which constrain no td value beyond
existence; (S2) the absolute floor `td>=6`; (S3) per-td statements —
finite entry menus, per-cell/per-route kills, floors, and formal
survivals — each of whose hypotheses names a fixed td or a fixed route
shape; (S4) type-relative conditionals (KJN/RPMC chain) whose
conclusions bound td only after an unproved type/constant menu is
supplied. A derivation of `td=12` must, in particular, exclude a
minimal counterexample at `td=13`. The only promoted `td=13` statements
are: the prime-td single-pole kill (S3, single-pole only); the off-axis
entry census (six L6-surviving entries at `td=13`); and the stage-R
recount leaving **129 OPEN cells** with the explicit ledger note that
no certified `td=13` census exists. Exclusion of `td=13` is therefore
not in the closure of the promoted set — it is recorded *as an open
problem* by the promoted set, and (S1)/(S2)/(S4) are silent about it.
The same argument runs at `td=14` (48 single-pole classes + 5 on-axis
cells + a `[2,5]` off-axis entry), and above `td=16` the ledger is
entirely silent (no artifacts at all), so every arrow `A5` candidate
fails. Identically at the next two levels: excluding the 71 single-pole
and 12 on-axis `td=12` survivors is not in the closure (A6), and
excluding skeleton (iii) of A7 — the nested-binary `(21,15,7)`-chain
ledger, which the reviewed FAIL review itself constructed, typed OPEN,
and showed meets the repaired source-mass floor with equality — is not
in the closure (A7). ∎

**Concrete abstract admissible families escaping the implication.**
(1) The `td=13` off-axis OPEN cells (any of the 129; e.g. the `m=2`,
type `(2,3)`, `Λ=(4,9)`, `M=[2,3]` entry, the unique prime-td survivor
with no `b=1` pole). (2) At `td=12` and the same `[2,2,2]` entry, the
frozen nested-binary ledger: three `(1,2,3)` chains, each taking the
dirty (A)-step `(3/2,2)->(2/3,3)` on cell `(21,15,7)` (`lambda>=2`),
arriving with `mu=3` at two nested binary merges; `Σ lambda >= 6 <= 10`;
arithmetically consistent, not the U1 record (its arrivals are at
`w=2/3`, not the record's seed or the dead ray's `w=1`). (3) Inside
the U1 record itself, the W1–W3 terminal cells and the `(1/2,12)`
family of §3.4, which escape the proposed *occurrence* implication
even after every selection is granted. Families (1) and (2) are
reviewed-frozen objects; (3) is this report's contribution.

**One further negative.** Statement 9.6's `nu=25/17` degree
coincidences remain the only printed hint of a td12-selection
mechanism, and they are already adjudicated DUPLICATE and broken
(`n=1 mod 3` violated, fractional child frames). I checked the p.53
possibility list against the reduced laws at the charged frame and
confirm the trunk review's finding that the printed `(9j,75j,25,3,6)`
tuple cannot be reconciled with `dq ≡ 1 (mod nu)`; it can serve
neither as a pin nor as a counter-cell.

## 5. Smallest new lemma

> **Lemma `MERGE-FREE-TRUNK-TERMINAL-CLOSURE` (family-aware).**
> Let a Sigray-normalized Keller counterexample have, on a fibre `a`, an
> actual last merge `G` whose down-path to `(0,y)` is merge-free, with
> reduced trunk state `(w_0,M_0)` and topological degree `td`. Let `C`
> be the reduced P0 closure of `(w_0,M_0)`: states reachable by the §10
> P0 grammar (clean-resonant, pure-epsilon, dirty including IIb),
> quotiented by neutral steps, pruned by
> `Σ max(1,⌈AF2 gap⌉) <= td-2`, with each pure-epsilon `nu`-fibre
> retained as one arithmetic family record. Then:
> (a) `C` is finite as a set of `(w,M)` states with family-record
>     fibres, and effectively computable;
> (b) the actual trunk's ordered non-neutral event sequence maps
>     totally and provenance-preservingly into a path of `C`;
> (c) the last event lands in the subset
>     `T(C) = {(w,M,nu-record) ∈ C : 0<w<1, M(1-w) ∈ Z>=1,
>     Σ lambda_floor <= td-1-psi}`; and
> (d) fail-closed: any actual event not matched by a grammar step is
>     typed `OPEN` and the map aborts rather than skips.

**Hypotheses, exactly.** The promoted P0/AF2/Cor-7.1 package (R1.0–R1.2,
repaired dirty grammar with IIb, derived lambda-rule with the St-9.4
integrality line and the 6.7/6.8 positive-gap bridge, actual-weight
Corollary 7.1); St 8.4 upper-M divisibility; the R1.5 arrival
coprimality; plus the two riders of §3.2 — grammar totality at actual
tier for merge-free trunk events, and single-chain root-arrival typing
(`w<1`, integral `j` at the last event). The riders are the honest
novel content: (a) and the enumeration of `T(C)` are computation;
(b)–(d) are where the proof lives.

**Conclusion's use.** Instantiated at `(w_0,M_0,td)=((9/2,2),12)`, it
converts `TD12-U1-ACTUAL-LANDING` into a well-posed finite dichotomy
with the *correct* codomain `T(C) ⊇ {B25, S17, W1, W2, W3,
(1/2,12)-family, ...}`, after which per-cell discriminators (T1, the
24/16-level jet gates, exact-price upgrades) can be aimed at a closed
list instead of a false two-cell target. It is family-aware: the same
statement covers every off-axis trunk at every `td`, so it also
addresses the CRITICAL-5/6 post-jump and `M>=2`-suffix holes for
merge-free suffixes.

**Proof skeleton.** (a): non-neutral steps cost `>=1`, so path length
`<= td-2`; per state the R1.4 divisor law `E | l·num(w)·M_F` bounds all
dirty `(nu,kbar)` up to the pure-epsilon fibres, which have
`nu`-independent `(w_F, lambda)` and `M_F | (l-eps)` — one family
record each; induct. (b): each actual non-neutral trunk event is a
chain vertex with a semi-invariant pattern; the repaired R1.3/IIb
classification plus R1.0 rigidity types it as exactly one grammar step;
totality is the rider, discharged by proving the pattern classification
exhaustive for merge-free `V_a ∩ T_a^↘` vertices (the known hole —
the omitted (II)(b) family — is already inside the grammar). (c):
root-arrival typing rider plus Cor 7.1 with the terminal's `psi`.
(d): construction.

**Dependencies.** All promoted: the finite-chain R2 closure reviews,
AF2 §§1–3, BOOK-OFFAXIS §6/§7/§10, POLE-EXIT-ZERO, Cor 7.1/MFE. New:
the two riders only.

**Cheapest falsification test.** Run the existing reviewed R2 closure
implementation from `(9/2,2)` at ceiling 10 and diff its terminal slice
against §3.4: absence of any of W1–W3, of the B25 continuation edge, or
of the `(1/2,12)@{nu≡11(12)}` family — or presence of a fitting
terminal my superset scan excludes — falsifies the lemma's codomain
computation immediately, at desk cost.

**Non-duplication.** It is not the marked-first-event landing theorem
(that is on-axis all-`b=1` and stops at the first jump; this is
off-axis `M>=2`, multi-event, terminal-typed). It is not `G2-PSC`
(no GGV packet is transported) and not `G2-BD` (no residue-A carrier
bound). It is not the source-constructor L3–L5 layer (that builds
completions *after* an occurrence; this bounds where occurrences can
be). It is not the R2 finite-closure theorem itself (that is
reachability of reduced states; the new content is totality of the
actual-to-reduced map, terminal typing, and the fail-closed family
codomain — precisely the parts whose absence let a two-cell codomain
circulate).

## 6. Cross-connection audit

- **Minimal topological degree.** GGV minimality is gcd-minimality; the
  selected pair's td is uncontrolled, and a td-minimal counterexample
  (well-ordering) carries no promoted structure: the only td-minimality
  consumer in the ledger is `UCD-A-min`, which is residue-A-class
  restricted and conditional. No arrow; none promoted.
- **Degree divisibility.** At type `(2,3)` the degree pair is
  `(2k,3k)`; nothing relates `k` to `td=12`. The B25/S17 floors
  (`deg f >= 136i`, `>= 204i` on the g-side) are lower floors on an
  unbounded index `i` (`i=6n` on the direct family), and the only
  `n`-law is the linear pin `i_F = 3n·i_G` — an attack surface for a
  cofinality argument, not an arrow. Statement 9.6's ratio coincidences
  are DUPLICATE/broken (§4). No arrow.
- **Finite/cofinal type control.** KJN and its equivalents are
  type-relative; the `(alpha,beta)` menu is finite only per fixed td
  (`beta <= td`). The U1 record does supply one exact cofinal handle —
  `i_F = 3n·i_G` with `i_G = 2` — but no premise converts an unbounded
  normalization index into a bound. No arrow.
- **GGV minimality.** Used exactly once (A1) and then logically idle in
  the pure-Sigray lane; the honest chain never consumes the polygon
  data (REDUCTION T10's redundancy observation stands at this basis).
  No arrow.
- **Boundary-tree Euler accounting.** Printed (22)/(22-cl) remain
  invalid/unproved; the actual-cluster-weight Corollary 7.1 inequality
  is the sole budget generator, and budgets prune (they killed the
  labelled ray and cells W-adjacent to mine) but never select: every
  fitting verdict in §3 is a non-exclusion. No arrow.
- **Monodromy.** The U1 merge gluing `t^3 - A*` and the trunk ratio
  `9/8` are unlinked by any printed law (confirmed in the trunk
  review's gauge analysis); deck-orbit control (L5-exact) exists only
  after an occurrence is named. The sibling's complex ratio
  `(9±3i)/8` versus the trunk's real `9/8` is suggestive for a future
  reality/conjugation discriminator between the two reviewed terminals,
  but no statement connecting field of definition to occurrence is
  promoted, and my W1–W3 cells (real ratios `2`, `6/5`) show reality
  alone cannot select B25. No arrow; none promoted.

## 7. Negative theorem, stops, and firewall

The sharpest citable outcome of this attack:

> **Interface theorem (negative).** At basis `93db679d`, the promoted
> statement set neither selects `td=12`, nor the `[2,2,2]` entry, nor
> the U1 equality record, from a hypothetical minimal counterexample
> (§4); and conditional on all three selections, the two-cell occurrence
> codomain `{B25,S17}` is refuted at reduced tier by explicit
> budget-legal alternative terminals, including a continuation out of
> B25 itself and one `nu`-unbounded family (§3.4). The narrowest true
> conditional statement available is the closure-codomain dichotomy of
> §3.2, pending its two riders.

Recommended stops consistent with this: do not spend the primary slot
proving `{B25,S17}`-codomain landing (it is false); do not launch
source-value or jet work on W1–W3 by analogy (they are superset-tier
cells awaiting the closure lemma's reviewed codomain); `j=42` stays
parked per the binding integration.

This report asserts no occurrence, attainment, `PairRef`, source value,
degree ceiling, panel exclusion, counterexample, or JC2 conclusion. All
new cells are formal reduced objects; a formal configuration is not an
actual polynomial map. Floors are floors. Files written: this report and
`/tmp` scratch only. No web, AWS, commit, push, canonical edit, or
`jc2-lean` access of any kind.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->`
  line, including its terminating newline; this seal is outside the body.
- Body bytes: `29245`.
- Body SHA-256:
  `cf21b43a54006cd73cd61571f3b47d9f728a48076d5a6c4692ad818e8c18e5fc`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
