# Fable5.1 adversarial cross — FULL0920

tag: ideation-20260912T0920Z-cross-fable5
author: Fable 5.1 (claude-fable-5-1), fresh CLI reader, no inherited reuse
start_utc: 2026-09-12T09:50:42Z
reserve: 10:24Z  hard_stop: 10:27Z (2026-09-12)
mode: manual/documentary only — no interpreter, CAS, network, git, scratch, agents
scope: read CROSS-CONTRACT whole first, then the 7 other charged objects whole; strategy, not a review gate

## 0. Custody (pre-read)

Hashed at 09:51:00Z in /tmp/jc2-lane.ymAUSu/inputs before any body was read.

| snapshot | sha256 (pre-read) |
|---|---|
| CROSS-CONTRACT.md | 56a710ae0a87c348a240fc3b581416b982e8e1cbc2101e56c40ce59bfa401b0c |
| coordination.md | 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597 |
| ideation-20260912T0920Z-root.md | 09b55c8624c7deea82c357be28af8a16d27f94d57379180392e788a2257c7ac5 |
| ideation-20260912T0920Z-astra.md | 79a579c2c2721099c41b90289cb5942588e287853282e81481bfc7388aec9eab |
| ideation-20260912T0920Z-fable5.md | 2c9497c4cb96916a54c429fa4541664bc0b4273f33523cabe3b4fb928a168fa0 |
| ideation-20260912T0920Z-postblind-root.md | f6a679486f2d699180c7df63ed70850ff2f86c4a56270d6694b582f510ac4a16 |
| monodromy-history.md | 267390d0462705b1eb4b0eac50834a3863eeffbec2f8ffd4fefcb78a0d3d9cc7 |
| passport-history.md | 83e43010d79e6aca8e44b6e7fdecf61fb13032d39eca0ad4294ea8992b8649d9 |

CROSS-CONTRACT equals the invitation's expected value and its seven-row
table equals the other seven values above. Read order: contract WHOLE
first (one cat, 7915 bytes); then root, astra, fable5, postblind-root,
monodromy-history, passport-history each WHOLE in one unclipped cat
(197/123/258/157/142/76 lines); coordination WHOLE in three contiguous
byte ranges 1-16000, 16001-32000, 32001-48725 (806 lines). No other
file, current CROSS, box, original source or corpus was read. No
interpreter (empty or otherwise), code, CAS, network, git, process or
scratch write; the historical commands displayed inside the snapshots
were not executed. Only this report is written.

## 1. Contract compliance

- Same eight-object packet as the native Astra cross; all hashed before
  reading, CROSS-CONTRACT read fresh WHOLE first.
- No second full46 table. Surviving cards carry NEW/KNOWN/DUPLICATE/
  SCOPE-CONFLICT labels, missing input, cheapest test, information, stop.
- No charge_basis line: nothing below asserts a new exit price.
- No artifact_finalize; external lane.sh custody unchanged; ROOT owns
  collection, hard stop and every later launch decision.

## 2. Three blinds by OBJECT / MISSING ARROW / MECHANISM / TEST

| | ROOT | Astra | Fable |
|---|---|---|---|
| object | full normalization Y, R=Ram, mu=sigma^3/v | fixed r3 297-minor at 523/V0; S/T double cover | generic fibre C_t, ledger m=sum(delta)-N-r |
| missing arrow | LC(Y,R/2) on actual sources | worker-independent binding; any opposite bound on b,g | finite inertia per class; a genus ceiling |
| mechanism | log-bicanonical section versus A2 (cubic proof s.3-4) | rank certificate; RH for a degree-2 cover | RH on the generic fibre with the promoted floor |
| decisive test | one manual valuation composition | offline assembly, then rank | m<=1 on td6/td7/169 passports |

Deduplication. Astra's 4g+b>=6 and Fable's sum(delta)>=N+r+2 are ONE
mechanism (Riemann-Hurwitz plus the promoted genus floor yields a lower
bound on boundary ramification) applied to two objects; neither has an
upper bound, so both are filters on candidates that do not exist. ROOT's
and Astra's r3 cards are one deferred client with two time budgets.
ROOT's log card is the only all-degree mechanism in the packet, and the
postblind shows its section algebra is already inside the reviewed cubic
proof; what is new in this cross is the reformulation of its missing
hypothesis in section 3.

## 3. Missing source arrows and corrections

**Log route (ROOT card 1 + postblind).** I confirm KNOWN/DUPLICATE for
the section algebra and I re-derived the countercontrol by hand: J =
5x^5-7y^7; both displayed monic relations reduce to 0; weights (7,5) give
v(J)=35 exactly because the weight-35 form is nonzero; the chart x=t^7z^3,
y=t^5z^2 has determinant -1, dx^dy=-t^11z^4 dt^dz, r=t^35z^14(5z-7), so
A=12<35/2. Two corrections and one reformulation:

(a) Q-Cartier is NOT a missing hypothesis in dimension two. On a normal
surface Mumford's numerical pullback defines rho^*K_Y and rho^*R on any
resolution, so A_Y(w) is standard, and div(rho^*mu) = 3rho^*E - rho^*R +
2(K_X - rho^*K_Y) holds as Q-divisors: both sides agree off the
exceptional locus and have equal intersection numbers with every
exceptional curve. Adjunction for the Cartier divisor H on the
Cohen-Macaulay surface plus Serre duality gives h^0(omega_Y(H)) >= g(C)
>= 2 on the NORMAL model. Hence "LC(Y,R/2) implies no dominant regular
A2 -> Y minus D" needs neither smoothness nor Q-Gorenstein input, and
finiteness of a resolution is never used. The only missing arrow is
LC(Y,R/2) itself.

(b) LC(Y,R/2) is a finite tree condition, not a source theorem. From
K_Y = Phi^*K_P2 + R, every divisorial valuation w of C(x,y), with
restriction w' to C(u,v), ramification index e(w) and target log
discrepancy A_tgt(w'), satisfies A_Y(w) = e(w)A_tgt(w') - w(R). So

    LC(Y,R/2)  <=>  w(R) <= 2A_Y(w) for all w  <=>  3A_Y(w) >= e(w)A_tgt(w'),

checkable on one log resolution of (Y, Supp(R+H)). The Keller condition
evaluates the right side from the SOURCE compactification: with n_w =
w(H) the pole order of the map along w (0 at missed divisors) and m_w
the order of the source line at infinity L along w, du^dv = dx^dy gives

    e(w)A_tgt(w') = A_src(w) + 3(n_w - m_w).

Control: the automorphism (x+y^2, y) resolves with three blowups, the
contracted chain L(-1)-E2(-2)-E1(-2) solves M.a = (-2-F^2) to a=(3,2,1),
so A_Y(L)=4, and the identity gives 1+3(2-1)=4 with R=0. Therefore the
LC test at a boundary component is

    3A_Y(w) >= A_src(w) + 3(n_w - m_w),

with A_src from the blowup sequence, n,m from the weights, and A_Y from
the intersection matrix of the contracted non-dicritical configuration.
All three are class-tree data, and at L it says A_Y(L) >= d - 2/3 with
d the larger total degree (>=108 by the GGHV overlay).

(c) At a dicritical F, a prime divisor of Y, the test is e_F <= 3, and
the same bound applies at every missed divisor over A(F). For the
GENERIC direction the infinity profile is exactly the multiset {e_F with
multiplicity f_F}, sum e_F f_F = N (Bertini on the base-point-free |H|).
Any generic-direction profile with a part >= 4 REFUTES LC, so on such a
class ROOT's implication is vacuous: "Keller implies not LC" holds
trivially. The printed td profiles are coordinate-direction data; whether
they equal the generic profile is exactly the contract's own caveat, so
this is neither a kill nor an acquittal yet.

**GENUS-ESC (Fable).** The identity 2g-2+r = sum(delta)-N is right when
r counts every boundary place, but the prose "2N+2 plus finite-escape
places" conflates lost sheets with defect. The usable form is: finite
boundary defect >= 2N+2-ind(sigma_inf), i.e. 10 at N=6 for (3,3) and
(5,1). Residue-A has finite defect 42 and RH genus 18, already recorded
in the monodromy history, and it is the coordinate direction f=a, not
alpha f + beta g. No other class in this packet carries finite inertia,
by the survey's own list. So the consumer is vacuous where defined and
undefined elsewhere: KNOWN mechanism, DUPLICATE consumer, NO_LANE. The
premise of the 46-row systems card ("a finite consumer was missed") is
therefore false.

**S/T inequality (Astra).** Correct as stated. Hidden assumptions: the
cover must be etale over the whole affine pencil member (a property of
the S/T construction, not in this packet); connected C' needs the
S-pencil to be the image of the generic plane pencil; b is ramification
not removed points (Astra says so). No candidate pair exists to filter,
and the packet has no opposite bound. KNOWN mechanism, NEW attachment,
NO_LANE.

**r3 (ROOT/Astra).** Both name the same complete interface: a
topological order of the existing dependencies, an exact finite list of
facts that must remain late, and every early artifact either delivered
or shown to need a source repair. Neither supplies it and nothing here
may invent it. DUPLICATE. Benefit: one necessary-system exclusion at one
place, explicitly not JC2. Effort: 60-120 researcher minutes plus a
worker plus review, after every prior batch closed unrun. PARK unless
ROOT independently selects; it is not the highest JC2 contribution.

## 4. ROOT's postblind deductions, checked independently

1. Residue-A genus 18: CONFIRMED. 2g-2 = -12+42+4 = 34 for every (a,b,c)
   with a+2b+3c=42, so all 169 patterns have genus 18 and the floor
   bites nothing there.
2. Identical pairs: CONFIRMED and sharpened. ONE appended pair (tau,tau)
   already adds 2 to the defect and 1 to the genus, keeping product,
   transitivity and infinity profile; so every profile in the S_d table
   admits completions of every genus >= 0. A lower bound kills a witness,
   never a profile; only a complete passport has a genus.
3. Inputs not frozen: CONFIRMED by the survey's own list (genus, finite
   branch classes, branch values, vertex-to-inertia translation absent
   for td 7-9), and residue-A is a coordinate direction.
4. m=2g-2 even: CONFIRMED. The correct negative control is a complete
   genus-1 passport, e.g. (3,3) with eight finite transpositions of
   product one generating a transitive group, not a one-unit shift.

None of the four is wrong; "two pairs" in deduction 2 is merely stronger
than needed.

## 5. Combined idea and card verdicts

Combine ROOT's mechanism with Fable's consumer pattern: test the missing
hypothesis on the finite classes instead of hunting a source theorem
that supplies it. Section 3(b)-(c) makes that test explicit. Verdicts:

- ROOT log card: KNOWN mechanism, missing arrow restated as a tree
  inequality; cheapest test in section 7.
- Fable GENUS-ESC: KNOWN/DUPLICATE, NO_LANE.
- Astra S/T: NEW attachment of a KNOWN mechanism, NO_LANE.
- r3 assembly: DUPLICATE deferred client, PARK.

## 6. Systems trial (separate)

Choose ROOT's condensation: regroup the strategy paragraphs of
approaches by mechanism, with one source-use line per surviving card
(supplied hypothesis, missing hypothesis, next decision), preserving
every paragraph in history with its links. Evidence: approaches grew
from 25412 to 49146 bytes since the previous condensation, and this
round's postblind is itself a retrieval failure (a reviewed cubic proof
already held the mechanism). Test: at most 20 editorial minutes,
UNMEASURED; measure bytes, check every link, ask whether this round's
four verdicts are findable without a history scan; reject if a caveat
disappears. Reject Fable's 46-row-per-promotion table: its founding hit
was vacuous, and it grows the document whose size is the complaint. No
scheduler, cap, instrument or ranking change.

## 7. One next action

LC-TREE-TEST: one bounded documentary lane, owner chosen by ROOT, Fable
gate on any kill. Object: the td6 terminal classes, residue-A first.
Step 1: read each class's dicritical weights (e_F, f_F); if any e_F >= 4
(or any missed divisor has e >= 4) the class is NOT killable by the log
mechanism; record and stop for that class. Step 2, only where step 1
passes: solve M.a = (-2-F^2) on the contracted non-dicritical
configuration for A_Y and check 3A_Y(w) >= A_src(w) + 3(n_w - m_w) at
every boundary component of the resolution tree, L included. Outcomes:
any violation means the class survives this mechanism; all pass means
the class is excluded by the already reviewed implication, subject to
the different-model gate. Expected: violations everywhere, which retires
ROOT card 1 as DEAD-ON-SCOPE rather than SOURCE-GAP, a decision the
packet cannot make today. Cost: manual linear algebra per class,
planning estimate under one lane-hour for td6, UNMEASURED; no CAS,
worker or new batch. Stop: td6 only; if the class records lack
dicritical weights, report NONDECISION and extract nothing further.
Against the alternatives, r3 gives a local exclusion behind a deployment
wall and the two RH filters have no object; this is the only test that
can change the status of an all-degree mechanism this cycle. If ROOT
judges the records too thin for step 1, the honest alternative is
NO_LANE, not an r3 batch.

## 8. Post-pin and self-checks

Post-pin re-hash at 2026-09-12T10:07:51Z after the own WHOLE readback;
all eight values identical to section 0 and to the contract table.

| snapshot | sha256 (post-pin) |
|---|---|
| CROSS-CONTRACT.md | 56a710ae0a87c348a240fc3b581416b982e8e1cbc2101e56c40ce59bfa401b0c |
| coordination.md | 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597 |
| ideation-20260912T0920Z-root.md | 09b55c8624c7deea82c357be28af8a16d27f94d57379180392e788a2257c7ac5 |
| ideation-20260912T0920Z-astra.md | 79a579c2c2721099c41b90289cb5942588e287853282e81481bfc7388aec9eab |
| ideation-20260912T0920Z-fable5.md | 2c9497c4cb96916a54c429fa4541664bc0b4273f33523cabe3b4fb928a168fa0 |
| ideation-20260912T0920Z-postblind-root.md | f6a679486f2d699180c7df63ed70850ff2f86c4a56270d6694b582f510ac4a16 |
| monodromy-history.md | 267390d0462705b1eb4b0eac50834a3863eeffbec2f8ffd4fefcb78a0d3d9cc7 |
| passport-history.md | 83e43010d79e6aca8e44b6e7fdecf61fb13032d39eca0ad4294ea8992b8649d9 |

Checks: sections 1-7 count 1643 words by wc -w (cap 1800, custody
excluded); one next action named (LC-TREE-TEST) with object, quantity,
cheapest test, both outcomes and stop; one systems trial chosen
(condensation) and one rejected (46-row table); no OPEN[...] raised, so
no collision block; no charge_basis line (no new exit price); destination
is xmodel/ideation-20260912T0920Z-cross-fable5.md only, no box or scratch
write; no artifact_finalize. Writers idle after the marker below; no edit
follows it. Written under the original reserve 10:24Z / hard stop 10:27Z.

<!-- BODY-END -->
