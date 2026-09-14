# Blind full round 20260906T1210Z — Fable 5.1

Written 2026-09-06 12:17Z. Inputs: /tmp/jc2-lane.xRmgTl/inputs (12 files).
PDF sha256 ac18e80c…80bd and text sha256 f3eca2a5…2368 match the packet
line; packet body reproduces frozen basis 0d39df3c. Read: packet (complete),
APPROACHES.md avenue map, history section 1 rows 1–46, 1030 synthesis,
classical99 Opus gate, AUDIT 17(eeeeeeeeeeee)–17(hhhhhhhhhhhh), primary text
abstract/§1/§2 table/Thm 2.1/Prop 4.2 statement/§5 theorem and proposition
headers. NOT read line by line (typed): Prop 4.2 proof body, Props 5.2–5.6
proofs, §6, the three Fable gate reports beyond their titles, [1][2][3][5][6].

## 1. Disposition vector (46 avenues; historical scores not authority)

UNCHANGED (range as in history section 1): 2–35, 37–46. Reasons: no new
primary text or internal result in this packet touches any of them; the 1030
round produced no all-degree mechanism (packet), so no raise is licensed.
Changes:
- 1 (GGV corner families / degree farm): LOWER as a counterexample avenue at
  max deg < 125 and ≠(72,108), because GGHV Thm 2.1 (text line 97–98) is an
  external exclusion; RAISE as the *interface* avenue for D108 (§4 below).
- 36 (guided counterexample search): LOWER at (99,66) to STOP; keep range only
  for the GGHV open case (8,28)*(3,2) and for max ≥ 125.
- 46 (formal certification): UNCHANGED, but note the campaign needs a
  literature-exclusion ledger before any formalisation target is chosen.
No REOPEN. Whole-portfolio scan: no avenue outside 1/36 depends on 99.

## 2. Primary 99 verdict: APPLIES_AS_EXTERNAL_THEOREM (chain typed)

Chain in the charged text:
- Thm 2.1 (line 97): counterexample ⇒ max{deg P,deg Q} ≥ 125 or
  (deg P,deg Q) ∈ {(72,108),(108,72)}. Its case list is inherited from
  [5] §5–6 tables (line 94, 99–100), not reproved here: trust dependency 1.
- §2 table (line 125): A0=(9,24), (m,n)=(2,3), max 99, "no detail in [10]".
  GGHV explicitly do NOT credit Moh with 99; they discard it themselves.
- Prop 4.2 "Case (9,24)" (line 348): reduces to P,Q ∈ L^(1), [P,Q]=x, three
  Newton-polygon cases (1)–(3). Proof cites [1, Cor 7.4], [2, Prop 3.12],
  [6]: trust dependencies 2–4 (all same-author arXiv/Pro Mathematica).
- Thm 5.1 (line 659): no P,Q with the (9,24)/(9,27) endpoint data, via
  Props 5.2–5.6, Remark 5.3 (α-normalisation), Cor 5.7, using the
  polynomial-equation systems of [3] (arXiv:1406.0886): dependency 5.
Independently replayed by me: none of the proofs. Verified only that the
statements form a closed chain (66,99) → Prop 4.2 → Thm 5.1, and that the
degree-99 row is listed as discarded "in this paper" (line 130–131, 80).
Unverified (typed OPEN-PRIMARY): whether Thm 5.1's hypotheses cover all
three Prop 4.2 cases; publication/refereeing status of 2204.14178.

Convention check (packet's warning). Literal Thm 2.1 is false for
non-normalised pairs: (P, Q+P) is also a counterexample with degrees
(108,108) if (72,108) were one. So read it as a statement about a
normalised representative (Q ← Q − cP never raises max). The robust
consequence "no counterexample with max{deg P,deg Q} < 108" survives that
normalisation because normalising cannot raise the max. (99,66) has
deg P ≠ deg Q, gcd 33, so it is its own normal form; the 99 exclusion needs
only the robust reading. The complete physical-J source has honest degrees
99/66 at every point (packet), so a point would be a (99,66) counterexample
with max 99 < 108, contradicting the theorem. Hence: full (99,66) ideal is
the unit ideal, CONDITIONALLY on GGHV's chain. This is NOT an internal
certificate, and it does NOT imply any subset (466-row, δ=2 d2-z55, .63/.73)
ideal is unit; those remain independent instruments only.

Specific recorded objection? None found in charged inputs. The classical99
gate rows (its lines 111–112) show every recorded objection targets Prop 4.3
(the (72,108) analysis) or our own char-0 lifts, never §2/§4/§5. The
frontier tool checks gcd ≥ 16 only; NOT_CLOSED_BY_THIS_GATE is not openness.
Degree 99 is externally excluded (arXiv-level trust), not an open frontier.
Old Opus gate's "full unit predicts subset unit" is rejected here.

## 3. Bottleneck cards (two)

Card A — KNOWN/SCOPE-CONFLICT — Reconcile the census with Thm 2.1.
Mechanism: the n ≤ 200 arithmetic survivors (24,063→90→64) are an internal
population; GGHV excludes every row with max < 108 and, on the normalised
reading, every row with max < 125 except (72,108). Deps: Thm 2.1 chain
above only. Cheapest decisive test: one filter over
box/census-sweep-20260905/inventory.json by (normalised) max degree and
pair, producing three bins: EXTERNALLY_EXCLUDED_lt108, EXTERNALLY_EXCLUDED_
108to124_conditional_on_convention, RESIDUAL (72,108)-type ∪ max ≥ 125.
Interpretation: the residual is the only honest frontier; counts change,
arithmetic rows do not. Cap: minutes, no CAS. Stop: after one run.

Card B — NEW connection — D108 ↔ GGHV open case (8,28)*(3,2).
Mechanism: D108 source has Ftop = h^3, Gtop = h^2, h = (X+W)^8 W^28 (packet,
root literal read). GGHV's §2 table has exactly two 108 rows: A0=(8,28),
(m,n)=(3,2), starred, left OPEN (line 82); and A0=(9,27), (2,3), discarded by
Thm 5.1 (INFERRED from the §5 title "(9,24) and (9,27)" and the star; the
§4 (8,28) text was not read). D108's (3,2) ratio and (8,28) corner match the OPEN row by
inspection, not by proof. Cheapest decisive test: compute the Newton polygon
corners of the physical D108 F,G (support only, no Gröbner) and compare with
the (8,28) case normal forms in §4 (unread here). Outcome: match ⇒ D108 is
the literature's sole sub-125 frontier and our chart is the first internal
instrument on it; mismatch to (9,27) ⇒ D108 is externally excluded and the
counterexample front moves to max ≥ 125. Cap: one desk hour, exact support
arithmetic only. Stop: at either outcome.
Strongest attack: falsify Card B by finding a target-addition (F, G+cF^k
style) moving D108 between the two 108 rows; if it can, Thm 2.1's
representative convention decides, and the packet's warning applies.
charge_basis={"delta":"n/a","branch":"q=1-exact","flag_count":0,"citation":"ggvh-2204.14178v1.txt:82"}

## 4. Faster path now

Do Card A then Card B, in that order, before any solve. Then, if D108 maps
to the open row, read GGHV §4 (8,28) reduction fully and set the D108 chart
on the reduced L^(1) polygons (three-case style as Prop 4.2), which is a
dramatically smaller support than the 600-var/1629-row physical J.
No bigger compute at 99. No uniform K16 obstruction found: (T) at t ≤ 8 and
the norm model carry the same differential condition (packet) — NO_NEW_
MECHANISM there.

## 5. Software and campaign systems

NO_UPGRADE except ONE bounded proposal: add a second verdict field to
frontier_gate.py, `external_degree_overlay` with explicit `convention=
normalised_max`, citing Thm 2.1 and the (72,108) exception, never altering
the gcd field or the arithmetic counts. 48h trial is adequate.
Frontier-literature integration: the heading index failed to surface a
2022 theorem on our leading target; a `canonical-exclusions.md` ledger
(theorem, primary path, trust type, chain read/unread, rows it covers)
should be a standing input to every full round. Round overhead: this
replacement round is ~9 minutes; blind full scans at this cadence cannot
read a primary chain, so cadence debt should be recorded, not hidden.
Model roles: the coordinator checksum, not the blind lanes, found the
conflict; keep one lane per round assigned to primary-literature reading.

## 6. Continue / redesign / stop

- STOP: all new (99,66) frontier solves, expansions, witness campaigns; no
  99 full retry. Running .63/.73 subset solves finish as instruments only.
- REDESIGN: counterexample front → D108 via Card B interface check first.
- CONTINUE: transverse C-rank 191/190 root-code replay (gate PASS pending
  root); K16 (T) study at low priority; parent-residue pilot unchanged.
- STOP repeat web sweeps until the exclusions ledger exists.
- No external writes, no ledger/tool edits from this lane.
<!-- BODY-END -->
