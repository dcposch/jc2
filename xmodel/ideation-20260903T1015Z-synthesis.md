# Ideation round 20260903T1015Z — synthesis (coordinator, Opus 5, cloud seat)

Round status: COMPLETE (five blind submissions sealed inside the window:
Opus 49KB b13149ec, GPT-5.5 37KB 5e1646f5, Grok 41KB, Fable 37KB, Sol 39KB;
coordinator's own 15KB submission committed at 550f218a BEFORE any was
opened). Packet 99c940d1 on basis f5aa1caf. Questions: Q1 OPEN[MOH-PROGRAM]
in uniform form; Q2 the D = 105 trio; Q3 the all-degree frame; Q4 the
machine filter. Also harvested into this synthesis (sealed during the
round): reducible-branch review (CONFIRMED with repairs → AUDIT delta 17(i)),
global-interpolation framework (Sol, unreviewed), branch-orbits v2 (Grok,
unreviewed), web sweep (negative).

## 1. Headline: six independent readings agree on the frame, and the census question is now a THEOREM

1. **The D = 105 trio is not a flagship — 6/6.** A kill buys D_min ≥ 108
   only; every submission demoted it to a method-client / regression target.
   The packet's "first target: the trio" is WITHDRAWN as a seat allocation.
2. **(1)–(13) + integral pinned N never empties — now PROVED at the skeleton
   level (Sol §2.3, PROVED-HERE/UNREVIEWED).** For every a ≥ 0, L = 8a + 5:
   n = 21L, m = 14L, M = (−14L, 7(3L+1)/4, 21L − 2), s = 3, V = (1, 5) passes
   (1)–(13) with δ = (−1, 2(3L−1)/(3(5L−1)), 7/12), q = 1/2, u = 5L, and the
   formal (UNI) packet k = 12 gives N = 6 exactly; degrees 105, 273, 441, …
   (first 21 members machine-checked). Consequence, stated by all five: a
   uniform theorem MUST use a datum not in the scalar skeleton. Q3(f) is
   CLOSED POSITIVE; "realise the infinite census" is not a program.
3. **What that datum is — three concrete, mutually compatible answers, each
   with an instrument:**
   (A) THE TRACE / MOMENT IDENTITIES (coordinator §0.3 and Opus §5,
       independently; Sol §2.2 "differential Reed–Solomon parity checks";
       the Sol framework lane's (DEG) block). d/dx Tr(f^{k+1}) =
       (k+1)·J·[y^{n−1}](f^k mod (g − c₂)) with deg_x bounded by
       (k+1)·max pole, pole per bottom root = q/e < 1: the O(1) pinned N bounds
       a family indexed by a free integer k whose natural size is Θ(k·m). The
       n − m − 1 degree conditions are M_r = Σ_i H_i τ_i^r/D_i = 0 (moments).
       Lane: ps-growth-opus5 (running).
   (B) MOH'S DESCENT (Fable §1–§3, SOURCE-READ pp.196–212; GPT-5.5 §1 the
       "Appendix-II compiler"; Sol layer 2). Moh's program = the (1)–(13)
       sieve + an unrecovered gate + Appendix II, and Appendix II is Prop
       6.3/6.4: when u_s = d_s − V_s = 1 the pair descends to a MONOMIAL-
       JACOBIAN pair in k[γ,π] of π-degrees (n/d_s, m/d_s) with
       J = −(u_s/b)γ^{v_s−u_s−1} and characteristic data {M_i/d_s, d_i/d_s};
       checked against p.207: (64,48) → (16,12; X), (84,56) → (21,14; X),
       (75,50) → (15,10; X²). Two of the three D = 105 groups descend:
       G2 → (15,10; γ⁴), G3 → (21,14; γ²) — Moh-sized problems (10–25
       unknowns). The descent lands in the GGV "[P,Q] = x^k" world of
       APPROACHES row 1, which the campaign already owns certificates for.
       Lanes: m2-descent-opus5, mohsieve-descent-engine-grok46 (running).
   (C) THE GALOIS-ORBIT STRUCTURE (branch-orbits v2, PROVED-HERE): (UNI) is
       NOT a theorem; the u copies of L₁ sit in ONE disc D_{s−1}; the orbit
       size of a bottom disc is |O| = ∏_{j=2}^{s−1} ω_j with ω_j = A_j on a
       (10)-level and 1 on an (11)-level; each orbit satisfies (8)–(13) on
       its own; the s = 3 packing is exact. On the trio every packet is a
       SINGLE orbit: k = 18, 13, 17 and N = 9 in all three (the UNI interval
       6..12 on group A is REFUTED). D = 88 is emptied in [6,16] (exact,
       s = 3; not at N ≥ 6). Grok's DESSIN-TOWER dimension (Card II) is the
       geometric form of (C). Lane: dessin-tower-dim-grok46 (running).
4. **Q1 — four measured candidate gates keep Moh's six rows and empty
   D = 105; none is sourced; Sol's is the sharpest.** All MEASURED on
   box/moh_skeleton_full.py at n ≤ 100 (658 rows / 63 classes base):
   - Opus: MOH-INCREMENT (A_j ≥ 2) ∧ NOT-ALL-(11) ∧ MAJOR-MULT (V_j ≥ 2):
     → 51 rows / 13 classes; MAJOR-MULT SOURCE-UNVERIFIED.
   - Fable: M₂ > m: → 94 rows / 32 classes; + integral N ≥ 6 → 33 rows (28
     beyond the table); AM semigroup conditions AUTOMATIC (refutes Q3(d) as
     the missing filter); twelve degrees empty at D ≤ 120; D = 108 keeps two
     groups in [6,16].
   - Sol: M₂ > n − d₂ ∧ forced-(10) at every level: → 10 rows / 6 classes —
     Moh's six plus FOUR extras ((96,64)×3, (100,40)); the P202-10 audit.
   - Coordinator: SECOND-POINT — RETYPED by branch-orbits v2: the "second
     point" L₂ is Moh's MINOR disc D*_{s−1}; its conditions are Props
     6.1–6.4, i.e. exactly the descent hypothesis (B). Not a new predicate.
   Fail-closed discriminator for all of them (Sol §3.4): the (1)–(13) row
   (75, 50, M₂ = 40, V₂ = 1) has an exact cyclic bottom solution
   (p = π³ + (3b/2)π, q = π² + b), so NO local/scalar filter can kill it
   honestly — a candidate gate that kills it must be global or sourced.
   Grok (§1.2 SPLIT-MOH) and Sol (§2.1) both warn: p.202's completeness is
   a 1983 program's claim; treat it as falsifiable, not as an oracle.
5. **Q2 — the trio, correctly typed.** Same rigid (2,3,V₂ = 1) bottom star
   (p_g = π³ − π, p_f = π² − 2/3); single orbit each (k = 18/13/17, N = 9);
   the first global order has 34 homogeneous moment identities + 1 monic
   (Sol framework: n − m − 1, not n − m); the razor counts (GPT-5.5: C has
   34 unknowns vs 35 equations) are COUNTS, not ranks — the Sol framework
   lane proved that no bare-tuple unknown count exists (needs the decorated
   skeleton). Cheapest honest kills, in order: (i) a sourced gate; (ii) the
   descended problems (15,10; γ⁴) and (21,14; γ²) solved exactly (Fable
   Route B); (iii) the first-order global moment rank with the decoration
   (d105-rank-gate-sol56, running).
6. **Q4 — one engine, three faces.** The global moment/parity-check matrix
   (Sol Card 1 = the sealed globalinterp.py + Sol's quotient-algebra form
   B = K[y]/(g − c), ∇ = ∂_x − (g_x/g_y)∂_y, 34+1 moment rows) is the same
   object as PS-GROWTH's residues and as the descended Appendix-II
   polynomiality; build it once, run it on (a) the trio, (b) the fixed-N = 6
   family L = 5, 13, 21, 29 (Sol Card 2: the all-degree laboratory — the
   parity block grows as 7L while the bottom packet stays fixed), (c) the
   descended small pairs. The sieve harness (mohsieve.py, Opus §4.1) and
   the descent engine (Fable §5) are the arithmetic front end.

## 2. Corrections banked from the round

1. (UNI) is not a theorem (branch-orbits v2); every UNI N-set in the record
   is a superset of the orbit-admissible set; the trio has N = 9 only.
2. The packet's "the three D = 105 groups are the first targets" —
   WITHDRAWN as a seat; kept as regression clients.
3. The coordinator's SECOND-POINT candidate — RETYPED as the minor-disc
   conditions (Props 6.1–6.4 / the descent hypothesis); not registered as a
   predicate.
4. "n − m degrees to kill" (packet item 6) — the exact count is n − m − 1
   homogeneous + 1 monic (Sol framework §1.3).
5. The coordinator's PS-3 sharpening (R_k ≡ 0 for k < e/q_max − 1) is a
   PROPOSAL charged to ps-growth-opus5, not a claim.
6. Q3(d) "silently used semigroup condition" — REFUTED as the missing
   filter (Fable, Sol: automatic on all 658); the AM one-place FRAME is
   raised (Fable §4).
7. Q3(c) characteristic p as a proof — LOWERED 5/5 (diagnostic /
   accelerator only; the inverse-Jacobian p-curvature is already zero).

## 3. Consensus dispositions

- Trio flagship: NO (6/6). Census-as-program: NO (6/6). Non-skeleton datum
  required: YES (6/6, now a theorem modulo review).
- Q3(a) D-module/Picard–Fuchs: RAISE in concrete form (Opus, Grok, GPT-5.5,
  Sol, coordinator) — the trace/moment cokernel or the pencil irregularity;
  Fable LOWERS (irregularity bounded by O(1) poles) — a real dissent, to be
  decided by ps-growth's residue lower bound and Grok's OPEN[PF-IRREG].
- Q3(b) dessin tower: RAISE as a lemma target / receiver (Opus, Grok,
  GPT-5.5); Sol/Fable: it bounds V₂, not D.
- Q3(d): scalar semigroup automatic (Fable, Sol); the descent/approximate-
  root FRAME raised (Fable, GPT-5.5, Grok, Sol).
- Q3(e) counterexample lift: RAISE only after a gate names the type
  (Grok, Sol, Opus); target V₂ ≥ 2 rows at D = 108/120 (Opus) or the
  descended small pairs (Fable) or group A k = 12 (Sol — note: k = 12 is not
  orbit-admissible per branch-orbits v2; k = 18, N = 9 is).
- APPROACHES: row 1 REOPEN as RECEIVER (descent lands in [P,Q] = x^k; RES-
  DEGREE) — 4/5; row 6 RAISE — 4/5; row 25 RAISE — 4/5; row 29 RAISE — 3/5;
  row 16/45: split (RAISE 3, LOWER 1) → RETYPE; row 20: LOWER — 5/5.
- Campaign-systems: adopt Opus's UPGRADE — every raised OPEN states its
  CHEAPEST TEST (instrument, gate, wall-clock) beside its bounded quantity;
  any OPEN under one lane-hour is attempted before a round's questions are
  set. (Evidence: PROP-5.6-SHADOW and MAJOR-MULT were both under an hour
  and sat unattempted.) Queued ops debt (non-blocking): GPT-5.5/Fable/Sol's
  artifact-presence receipt (hash refs/* opened by a lane) and Sol's
  systemd lifecycle fixture.

## 4. Lane decisions

Running (launched during the round, all consistent with the synthesis):
ps-growth-opus5 (A); m2-descent-opus5 (B; M₂ > m; the two descended trio
problems); mohsieve-descent-engine-grok46 (Q4 front end + leaderboard);
dessin-tower-dim-grok46 (C, geometric); d105-rank-gate-sol56 (Q2 (iii));
moh-source-three-questions-grok46 (MAJOR-MULT / MOH-INCREMENT / Appendix
II datum); moh-program-review-sol56 (second reader); global-interpolation-
review-grok46 (framework review).
LAUNCHED with this synthesis: fixed-n6-family-moment-defect-sol56 (Sol
Card 2 — the L = 8a + 5 family through the moment engine: the all-degree
laboratory); p202-ten-rows-gate-audit-grok46 (Sol's sharpest gate on the
ten rows + the (75,50,40,1) falsifier against all four candidate gates);
branch-orbits-v2-review-gpt55 (different-model gate for (C) — its D = 88
emptying and the trio N = 9 collapse are load-bearing).
STOPPED/REDESIGNED: DISC-COUPLING (the engine replaces it); box01 cluster
census (auxiliary, done).

## 5. Direct answer to the round

The all-degree program is NOT skeleton realisability. It is: (i) recover
or refute Moh's gate as a sourced predicate (four candidates, one
falsifier row, leaderboard running); (ii) attack the pair through a datum
outside the skeleton — the trace/moment code (whose size grows with D while
N is pinned), Moh's descent to monomial-Jacobian pairs (which terminates in
a degree range the campaign already owns), and the Galois-orbit/dessin-
tower gluing; (iii) use the trio and the fixed-N = 6 family as the
regression clients of one engine. A ceiling D ≤ C(N) is possible only
through (i)–(ii), never from the boundary.

<!-- BODY-END -->
