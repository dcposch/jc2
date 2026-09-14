# Cross report — Fable 5.1 — ideation-20260906T1210Z

Written 2026-09-06 12:32Z. Inputs `/tmp/jc2-lane.IEDsL2/inputs`: four report
SHA-256 match collection.json; PDF `ac18e80c…` and text `f3eca2a5…` match the
packet. No live report/log, AWS, CAS, ledger or adapter access. One exact check
(Python, <1 s) and one read-only fetch of [1] (arXiv:1401.1784) for a
definition. No exit-price assertion is made. Fable's blind is QUARANTINED and
critiqued, not inherited.

## 1. Endpoint verdict: MISTAKEN ENDPOINT, not a missing reduction

Opus's objection ("Prop 4.2 case (1) fails Thm 5.1 because `v_{-1,1}` ties at
(0,12) and (6,18), so `st_{-1,1}(P)=(0,12)`") uses the wrong orientation.

Primary definition, [1] Notation 1.6: `st_{ρ,σ}(P)` and `en_{ρ,σ}(P)` are the
first and last points of the (ρ,σ)-edge "when we run counterclockwise along the
boundary of H(P)"; Remark 1.7: `(ρ,σ) × (en − st) > 0`. The charged text pins
the same orientation without [1]: Thm 5.1(2) (txt:661) asserts
`st_{1,0}(P)=(6,16)`, `en_{1,0}(P)=(6,18)`, i.e. the (1,0)-edge runs upward,
and `en_{3,-1}(P)=(6,16)` with the (3,−1)-edge (1,1)→(6,16). Both edges are
counterclockwise; the clockwise reading contradicts the statement itself.

Exact check on all eight polygons (Prop 4.2 (1)–(3) and Cor 5.7, P and Q):

| polygon | st_{-1,1}(P) | en_{-1,1}(P) | Thm 5.1 endpoint data |
|---|---|---|---|
| 4.2 (1), corner (0,12) | (6,18) | (0,12) | satisfied |
| 4.2 (2), corner (0,6) | (6,18) | (6,18) | satisfied |
| 4.2 (3), no corner | (6,18) | (6,18) | satisfied |
| Cor 5.7, corner (0,18) | (0,18) | (0,18) | fails (v=18>12) |

Q rows behave identically. Cross-product control for case
(1): `(-1,1)×((0,12)−(6,18)) = 12 > 0`, Opus's assignment gives −12. So Astra
and Sol are right that all three cases are covered, and the paper's design is
visible: Prop 4.2's left corners all satisfy `v_{-1,1} ≤ 12`, while Prop 4.1's
(0,18) corner does not, which is exactly why only the 108 shape needs the Cor
5.7 shear. `OPEN[PROP-4.2-CASE-1]` is CLOSED by definition, not by majority.
What survives of Opus's point: the paper never states that Prop 4.2's cases
meet Thm 5.1's hypotheses, a one-line expository omission, not a gap. Line
164's reversed direction order affects Succ/Pred only; st/en are fixed by the
statement.

Trust status unchanged: `APPLIES_AS_EXTERNAL_THEOREM` with typed unread
dependencies [1] Cor 7.4/Prop 8.2/1.13/2.1, [2] Prop 3.12, [3], [5] tables,
[6], [12] Prop 10.2.6. Three independent (5.9) replays agree; no internal unit
follows; the root/agent certificate is post-cutoff and unreviewed.

## 2. Theorem 2.1 scope

Use only the robust reading: normalisation `Q → Q − cP^k` never raises the
max, and every normalised pair in the paper has max ≥ 108, so any actual
counterexample has max ≥ 108. The complete physical-J source has actual degrees
99/66, so its full ideal is unit conditionally on the chain; the 466-row subset,
δ=2 d2-z55 and .63/.73 charts get NO status from this (all five agree). Sol's
literal "any counterexample" reading must stay scoped: if a (72,108)
counterexample existed, (P+Q,Q) would be a (108,108) counterexample outside the
list, so the literal all-pairs form is either false or equivalent to the
normalised one. No blanket 108–124 filtering; Fable's blind bin
"108to124_conditional_on_convention" is an overreach and is dropped. The .73
K7 chart has target `x^k`, not a polynomial Keller pair, so the degree theorem
classifies nothing there; original caps stand pending root adjudication.

## 3. One deduplicated card (five proposals collapse to it)

**Card D108→GGHV (8,28).** KNOWN ingredients: literal source top
`h=(X+W)^8 W^28`, `F_top=h^3`, `G_top=h^2` (root read); §2 table rows (8,28)
*(3,2) open (txt:82,123) and (9,27) (2,3) closed by Cor 5.7; Prop 4.3 (txt:492)
reduces (8,28) to two `L^(1)` polygons with `[P,Q]=x^2`. NEW composition only:
a declared ring map (field, generator order, images) from the D108 source
coordinates to `L^(1)`, matched against `A0=(8,28)` and the (3,2) multiplicity.
Nothing is proved: matching integers between a literal source top and a corner
of a transformed Laurent polygon is the flag/place/series conflation, and
target addition (`G+cF^k` moving D108 between the two 108 rows) is the second
failure mode. Cheapest test, desk, ≤30 min: compute the support corners of the
literal D108 (F,G), apply Prop 4.3's printed normalisation chain, check ONE
invariant both sides (`[P,Q]=x^2` versus the D108 Jacobian normalisation) plus
one mutated non-image control. Outcomes: match ⇒ D108 is the literature's own
open row and our chart is a client of a known frontier (no solve licensed);
mismatch to (9,27) ⇒ D108 externally excluded; unmapped arrow ⇒ typed OPEN.
Stop at first unmapped hypothesis. Dependencies: [5] corner tables (unread),
Prop 4.3 proof body.

Proof side: `NO_NEW_MECHANISM`. Still required: an all-m obstruction on
`b·B_m·η_m ≠ 0` with the separate `b=0` boundary. The coordinator's
Hamiltonian-linear-space Card 2 is an untested composition, queued behind the
D108 card.

## 4. Corrected route ranking

1. D108 interface card (desk, capped, before any port or compute).
2. 99: closed externally; keep as method control only; STOP frontier work.
3. Transverse C-rank 191/190 root gate-code replay (pending).
4. K16 at `t ≤ 8`; no norm-only rewrites.
5. Best attack: the D108 category mismatch; no new proof attack.

## 5. Model roles by surviving work and correction cost

Astra: deepest read (pp.15/18 repairable slips, syzygy identity, ODE order
40/3), lowest correction cost; primary integration. Sol: exact (5.9)
reconstruction with the exceptional case, one scope slip (literal 2.1), one
minute late; bounded certificates. Opus: raised the only checkable new question
and replayed (5.9) correctly, but the endpoint claim was wrong and would have
cost a lane; bounded source extraction with a mandatory definition check before
any "gap" label. Fable blind: no proof body read, invalid basis JSON, three
overreaches (filter bins, .73 reclassification, sweep stop); hostile review only
after reading bodies. Coordinator: sealed early, correct verdict, one untested
composition.

## 6. Software and systems, separated

Software, ONE bounded test, no new ledger: add a pinned external-verdict field
to the existing frontier gate with four controls, 99/66 `CLOSED_max<108` while
still `GCD_GATE_PASS`, 108/72 `NOT_CLOSED_BY_BOUND`, total cap 107 closed /
108 not, partial-y 99/66 unbounded not closed. The gcd field and arithmetic
counts are untouched. Astra's `nv*idx` overflow controls remain the separate
authorised repair.

Systems: `NO_UPGRADE`. No canonical-exclusions ledger; the failure was
composing a known bound with the actual client, not indexing, and the
pre-launch frontier check covers it. Cadence debt is recorded, not repaired.

## 7. Continue / redesign / stop

STOP: new 99 solves, retries, dense expansions, witness campaigns, K16
norm-only rewrites. CONTINUE: capped .63/.73 solves under original custody,
.103 protected partials, C-rank root replay. REDESIGN: counterexample front to
D108 through the card; census rows keep arithmetic counts with external status
attached separately. No JC2 resolution, point, properness or new internal
exclusion is claimed.

<!-- BODY-END -->
