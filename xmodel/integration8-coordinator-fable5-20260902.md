# INTEGRATION #8 — coordinator binding (Fable 5, 2026-09-02)

Basis 4ab4478e. Supplements integration #7 (1f8dd6eb) and its
recorded delta (AUDIT: CUSP-CAGE repaired-and-strengthened).
Different-model review satisfied on every PROMOTED item.

## A. The cusp/homology theorem set (producer opus fa52e816;
## reviewer gpt55 fadc17c8 — all CONFIRMED)

**PROMOTED — THEOREM NO-PUSHFORWARD** (torsion does not push
forward along either local-to-global map; with the measured
trefoil witness). Closes the charged transfer inference
direction; the HOM-COVER razor remains a per-datum filter, never
an all-degree obstruction by itself.
**PROMOTED — THEOREM CENTRAL-RANK** (r = j-1 exactly; the r=j
branch impossible). BINDING as the CUSP-CAGE repair per the
AUDIT delta.
**PROMOTED — THEOREM CUSP-PARITY** and **THEOREM ORBIFOLD-CAGE**
(s + s' = M + 2 - j).
**PROMOTED — THEOREM CUSP-A-EMPTY** at its stated typing:
MPRIME case (A) is EMPTY for 4 <= N <= 7 (proved for N <= 6;
measured-exhaustive at N = 7; first survivors at N = 8).
Corollary (binding composition with THEOREM PROFILE): the N=4
H2 residual is EXACTLY case (B3) — the one-cusp horn with
k >= 1 double points; OPEN[MPRIME-CUSP-J2] closed NEGATIVE for
N <= 7.
**PROMOTED — ACS-FIX-VS-DEFICIT resolution**: a = #Fix(rho(m))
exactly, under H2 + THEOREM 7.B only (not beyond).

## B. The realized-substrate representation kills

**PROMOTED — (9,6,2) curve kill.** The realized (9,6,2) curve
admits no REP-96-admissible full-image (transitive S_4)
representation compatible with its braid factorisation.
Evidence: SAGE-NATIVE full ZvK zero (artifacts 7ad79c5c /
537e0fa0; positive controls 144/144 both orientations);
KILL-BINDING by bmfact-962-kill-review-sol56 663f86da, which
PROVED the inversion coverage of the absent inverse-full run
and handled the basepoint for the decision. Scope: THIS curve
(REPRESENTATIVE discipline; not the numerical row).
**PROMOTED — (9,6,4) curve kill.** The realized six-nodal
(9,6,4) curve admits no such representation. Evidence: native
full ZvK zero in BOTH orientations (artifacts 01bac03c /
709c08c8; census ledger 20 census_ok; 72-control exact);
KILL-BINDING by bmfact-964-kill-review-gpt55 67a2ceb4 (pruner
certification audited: 550=550, symmetric difference 0; one
nonblocking instrument repair: free_auto_F9 metadata
quarantine). Scope: this curve only.

**Board line (recorded):** every explicit N=4 object the
campaign has produced is now dead by at least one BINDING
route; the residual N=4 bookkeeping ((8,6,9) curve system 869,
(9,6) row orbit coverage) is confirmatory under
N=4-CHECKED-CLOSED. The pipeline (realization -> SIROCCO census
-> native ZvK decision) is validated end-to-end on two curves
and is the N >= 6 instrument.

## C. Recorded (not promoted; review debt LOW)

- SG-lane items (source-gate-962 474ba0a0): Lemma SRC-0 (the
  three source objects are one scheme; retype to
  OPEN[SOURCE-OPEN-U] official), THEOREM SG-1 (the four-box
  Euler razor in Mode 1 IS (M')), Lemma SG-2, Lemma HC-1
  (r(E) <= a), Cor HC-2 (rank decides sheet location), the
  HOM-COVER instrument fail-open repair + CONTROL 4, and
  box/covergeo.py. Mode-1 source-open at (9,6,2): closed
  NEGATIVE (equivalent to (M')). New OPENs:
  OPEN[SOURCE-OPEN-COMPLETION-UNDECLARED].
- Grok Chern-species claim REFUTED AS STATED (same lane).
- Card C: DEAD AT STEP 0 (deeba90a); revival only via
  OPEN[CARD-C-SOURCE-NORMAL-FORM].
- NA-sharpness: honest OPEN with one named missing hypothesis
  (09bca3cc).
- N5-SOUNDNESS (610c06c8) with the 01:11Z Heitmann/Zoladek
  typing correction: gcd >= 16 sound; != 2p and >16 gapped.
- DOMRINA-INSTANTIATE: NOT-INSTANTIABLE benign;
  OPEN[RESIDUAL-TO-DOMRINA-STATE] aliases the source neck
  (ef837b4d).
- 962 instrument repairs (emitter diagnostic, B6 prose) and the
  964 free_auto_F9 repair: queued, non-blocking.

## D. Standing fronts after this integration

1. **The one-cusp horn (B3)** — THE H2-side neck for N <= 16;
   its group family is torus-knot-with-relators, on which the
   merged homology program computes (CENTRAL-RANK / CUSP-PARITY
   / ORBIFOLD-CAGE are its tools). Successor lanes: the A2
   3x3 determinant at e >= 1 (CELL-32 §6) and a horn-focused
   flagship consuming the new cusp theorems.
2. **Case (A) survivors at N >= 8** — the CUSP-A machinery is
   exactly computable there; a bounded sweep lane can chart the
   survivor structure.
3. **OPEN[COMPANION-R0-REALISATION] / degree-cap** — the only
   handle on companion degree (reducible branch).
4. **N >= 6 counterexample frontier** — the validated pipeline +
   qqideal stack on both boxes; census design must respect the
   S_6 scale and the faithfulness preflight.
5. Bookkeeping: 869 decision (running), oracle window verdicts,
   orbit-coverage typing for the (9,6) row.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4837`.
- Body SHA-256:
  `dcce5652e14bd74875835731af8236c939e55d0b61cd2db71d1bdaadf2b5eb2a`.
- Frozen basis: `4ab4478e3f9fde80e7d23348fbc5a55154fc6d39`.
