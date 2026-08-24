# Coordinator synthesis — round `20260824T0719Z-c17bd25`

Status: **FROZEN / DEGRADED / LAUNCH DECISION**  
Packet cutoff: `2026-08-24T07:19:08Z`  
Round close: `2026-08-24T07:55:37Z`  
Clean basis: `c17bd2542b40f3178ec619ae4a73501550555336`  
Packet SHA-256:
`ef61e5d5fe8f58081b9b36602b5bf98a83f655b9836cefe93a5a355dd90c9a2d`

This closes the event-triggered full-spectrum round and authorizes three
bounded first gates.  It promotes no mathematical claim.  The fifth blind
lane exceeded the collection latency budget and never froze a report; it was
cancelled and none of its partial reasoning was read.  The round is therefore
formally `DEGRADED`.  Four complete submissions remain adequate for a launch
decision, but only Grok supplies a different model family.

## 1. Frozen population

| Artifact | SHA-256 |
|---|---|
| `xmodel/ideation-20260824T0719Z-root.md` | `e0be8593921b5e4c298f26756be4c5e36dd8cfade43e6227f0bfdae592dd146a` |
| `xmodel/ideation-20260824T0719Z-zero-base.md` | `34bf61674a0cd30357a2f55bb7b960ff508ddf659aa7824c6b73c31fe3888ffb` |
| `xmodel/ideation-20260824T0719Z-atlas.md` | `838fca63549888e6fc28ae4af794be92adbfa9955636b637c8c8ae00b2155284` |
| `xmodel/ideation-20260824T0719Z-grok.md` | `341d1582620eb8ef221cb03f5647d6aded2b12b9fc8d31ea5e918cf81f2c5248` |
| `xmodel/ideation-20260824T0719Z-dedup.md` | `15460ebe43db3f96c7b7a42ef86406e899399860cdf22d9cd309f254ca9b74e7` |
| `xmodel/ideation-20260824T0719Z-adversary.md` | `64b427058a5eac9b6824ccb6f053c1234b4cd8c9eba87d65871ac681b2fddbe7` |
| `xmodel/ideation-20260824T0719Z-feasibility.md` | `7ce3bdded25b5ce503c1af1998cf84c95b6e6ad5e1895472fe1873fab6cc2b97` |

The Grok lane completed normally with exit zero.  The Claude/Fable adapter
remains quarantined from the preceding round; no submission or vote is
imputed to it.  Provider agreement is not a confidence multiplier because
all submissions consumed the same packet.

## 2. Canonical corrections before ranking

Four post-collection checks materially alter the raw vote.

### 2.1 Mapping degree four is already closed

The packet highlighted Orevkov's exclusion of multiplicities two and three
but omitted the campaign's already banked continuation.  Domrina's 2000
general-case theorem excludes four-sheeted complex plane polynomial maps
with nonzero constant Jacobian, and Żołądek Theorem 6.12 proves invertibility
for topological degree at most five.  The canonical sheet ledger in
`ladder/SHEET6.md` and `ladder/SHEET6-CAMPAIGN.md` already says `td <= 5`
closed.

Therefore `MAPPING-DEGREE-FOUR`, `QUARTIC-RESOLVENT-OPEN-CHART`, and
`N4-FILLING-NIELSEN` are `PRIORITY-ERROR/KNOWN-CASE`.  They are not launched
and may not be retargeted by replacing `4` with `6`.  The honest first sheet
frontier remains `td=6`, already funnelled into the existing sheet-six and
residue-A/global-landing program.

### 2.2 The advertised HC4 quintic gate already ran

`xmodel/sol-hc4probe.md` already computed the first post-top quintic module
`S_(13,2,2,2)` and the constant-linear `5 -> 4` Schur descent.  Its exact
restriction to the JC2 cotangent sector is `2 a_6 a_5`, which vanishes on the
reduced top locus `a_6=0`; verdict `NO LEVERAGE`.  The current HC4 cards name
no later observable.  They are `DUPLICATE/STALE` and receive no source-replay
or compute slot.

### 2.3 Two proposed controls are invalid as stated

- `P=x+x^2 y+y^k` is not unimodular for any `k>=1`: its two partial
  derivatives have a common complex zero.  It is removed from the
  Hamiltonian control suite.
- In the unit Tate algebra, `1-px^(p-1)` is a unit and its inverse is the
  convergent geometric series.  Its algebraic zeros lie outside the closed
  unit disc, so the proposed horizontal divisor is not a divisor on the
  claimed affinoid.  `TATE-HORIZONTAL-MIXED` stops `TYPE-FAIL` as written.

### 2.4 Untwisted action residues are automatic

For a Keller pair,

```text
P dQ - x dy = dS
```

for a polynomial `S`.  Ordinary divisorial residues of this exact form are
zero, and the companion primitive is dependent modulo `d(PQ-xy)`.  The raw
action nominee is `COSTUME` and is closed without another Laurent client.

These are corrections, not promoted progress toward JC2.

## 3. Deduplicated mechanism set

Twelve raw cards reduce to three live research mechanisms plus coordination
closeouts.

1. **H — Hamiltonian cokernel / weight.**  Root's class
   `[div V] mod D_P(R)` and Grok's complementary-row curl correction are the
   same obstruction.  The weight receiver and a possible infinity receiver
   are descendants of one root, not independent votes.
2. **P — dual-pencil infinity defect.**  Package the behavior at infinity of
   all `aP+bQ`.  This is adjacent to H through Gauss--Manin theory but is not
   duplicate without a typed comparison map.
3. **S — bounded Artin--Schreier support.**  Use the legal-degree `p=109`
   seed and ask for a finite coefficient-feasible feedback cycle rather than
   another Witt level.  The failed Tate formulation is a warning, not a
   separate root.

The standard boundary-different identity is bookkeeping inside P unless it
produces a new principal relation.  Degree four, the first HC4 layer, current
weighted D, fixed Broughton row, K3, unrestricted Witt, raw action, generic
sparse search, and new book cells remain stopped.

## 4. Mathematical adjudication

### 4.1 H has an exact core and a strict restatement firewall

For `R=C[x,y]`, `(P_x,P_y)=R`, choose `V(P)=1`, set

```text
D_P = P_y partial_x - P_x partial_y,
kappa(P) = [div V] in R/D_P(R).
```

The syzygy module of `(P_x,P_y)` shows that changing `V` changes its
divergence by `D_P(h)`.  Vanishing of the class is equivalent to adjusting
`V` to a divergence-free lift, hence by polynomial de Rham exactness to a
polynomial `Q` with `[P,Q]=1`.  Thus the class is exact but its universal
nonvanishing on noncoordinates is JC2 in new language.

The first gate must instead do two bounded things: source-check the likely
Brieskorn/Gauss--Manin priority, and prove an exhaustive no-leak weight
recurrence on a named proper family.  In differential-form language the
candidate identification is

```text
kappa(P) dx wedge dy = nabla_[P] [dx wedge dy]
```

in the Brieskorn module, because for `alpha=i_V(dx wedge dy)` one has
`dP wedge alpha=dx wedge dy` and `d alpha=div(V) dx wedge dy`.  This identity
is a source/definition target, not yet a promoted literature claim.

### 4.2 P must first prove that its proposed object is a divisor

An infinity-defect function on the dual pencil may be positive generically.
Then its support is all of the parameter line, not a finite effective
divisor.  Subtracting the generic value gives only a jumping cycle and loses
the proposed zero-degree endpoint.  P therefore stops first at one of
`GENERIC-ZERO`, `JUMP-ONLY`, or `TYPE-FAIL`.  No GRR program, client book, or
second compactification starts before `GENERIC-ZERO` and resolution
independence are proved.

### 4.3 S is a support instrument, not a modular-to-complex bridge

An exponent SCC alone ignores coefficients, `109`-adic valuations, gauge,
and the first nonlinear successor.  Only a `FEASIBLE-CYCLE`—a minimal SCC
with an exact coefficient solution through that successor and explicit gauge
quotient—may license one later integral coefficient-scheme child.  A height
certificate or no cycle at cap eight is exact only for that frozen grammar.
No finite-level or all-tested-level modular survivor implies a complex point.

## 5. Launch portfolio

The established `td=6` funnel remains the campaign's sheet/topology backbone.
This round does not reopen its held cells, D-series, or unbounded book work:
the recent landing audits already identify `G2-PSC` and `G2-BD/BMRQ` as the
missing theorems, and no new bounded sheet-specific mechanism survived this
collection.  P is the new arbitrary-Keller global bet; H is the exact
plane-family bet; S is the orthogonal disproof bet.

| Root | Share | First deliverable | Immediate stop |
|---|---:|---|---|
| **H — Hamiltonian/Brieskorn** | 35% | Source-priority freeze; exact `kappa` equivalence; coordinate/Henon/Broughton controls; one complete recurrence for the certified family `P=x+x^n y` beyond `n=2` | `KNOWN-MODULE` with no new receiver, failed control, no proved no-leak weight, or generic sparse widening |
| **P — dual-pencil definition** | 25% | A precise constructible/vanishing-cycle object and `GENERIC-ZERO`, `JUMP-ONLY`, or `TYPE-FAIL`; only then one blowup-invariance/degree formula | not a divisor, presentation dependence, costume, uncontrolled positive term, or automorphism control failure |
| **S — AS109 bounded support** | 20% | Frozen manifest/gauge/collision/cap; two independent enumerators; `HEIGHT-CERT`, `NO-CYCLE-AT-8`, or coefficient-feasible minimal cycle | unfrozen grammar, verifier disagreement, gauge cycle, support-only cycle, or cap widening |
| **C/T — coordination, review, td6** | 20% | Correct canonical ledgers; maintain the `td=6`/landing gap as backbone; source sweep; enqueue hostile review at the first provisional result | silent promotion, revival of a stopped representation, or a second speculative generation |

H, P, and S are mutually nonblocking.  A producer reaching the five-part
provisional gate freezes its hash and starts different-model hostile review
in the background; the other producers continue.  No descendant consumes an
unreviewed claim beyond the one-generation reversible allowance.

All first gates are local and paper/exact-certificate bound.  Box02 and Box03
remain stopped.  Box01's protected legacy `build_tails43.py` process is not
interrupted.  AWS expansion is not licensed by a support cycle alone.

## 6. Process correction

Blindness did its job against copying but could not protect against a shared
stale premise.  Before every future launch, coordination must run a canonical
history/priority checksum on each surviving card:

1. search `AUDIT.md`, `APPROACHES.md`, `PROGRESS.md`, the newest `LIVE STATE`,
   `ladder/REDUCTION.md`, and the repository reports for the exact target and
   synonyms;
2. reconcile any conflict with the master degree/known-case ledgers;
3. source-check load-bearing literature claims from primary text; and
4. record `NEW`, `KNOWN`, `DUPLICATE`, or `SCOPE-CONFLICT` before compute.

Consensus never overrides a banked exact result or primary theorem.  This
checksum would have caught both the degree-four and HC4 duplicates before
four blind cards were spent on them.

No statement in this synthesis proves or disproves JC2.
