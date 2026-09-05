# Ideation round 20260905T1200Z — coordinator synthesis (4 blind: Astra, Grok, Fable, Opus)

Submissions: opus5 (50KB), grok46 (48KB), astra (45KB), fable5 (42KB); coordinator blind submission committed pre-read.

## 1. CORRECTIONS (banked; 3/4 flag these — they change what can be consumed)
- **The Moh ≤100 order chart is NOT proven complete (Astra §2,§3; corrects 17(ssssss)).** The corrected charts still owe an h-SUPPORT LEMMA: h retains two caps; 8 of 12 fibres OMIT D1-allowed h-monomials (76 coordinates listed). So the chart may STILL be a tot-degree/support SUB-SLICE — and a Singular timeout OR a future msolve UNIT is NOT a valid (T)-kill until the h-support lemma proves the emitted chart IS the full necessary over-approximation. This GATES the entire Moh ≤100 finish.
- **The K16 exact-square failure is PREDICTED, not proved (Astra §1; corrects 17(oooooo)).** The socle law gives an exponent UPPER bound, not equality/unboundedness; t≥9 failure is a prediction, t=9 open; only the tail-only t=4 failure is established. Retype 17(oooooo)'s "predicted false from t=9" as a prediction.
- **One residual row is s'=4, not s'=3 (Grok; corrects the packet).** 11 of the 12 rows are s'=3, ONE is s'=4 (17(nnnnnn) table row 12).
- **132/132 atlas coverage is conditional interface (Astra §4, per 17(mmmmmm)):** 296 split obligations remain; kills 0 sources.

## 2. K16 — TWO new mechanisms (both concrete, both cheap-testable)
- **Fable Card A — Γ GENERICITY / GALOIS all-or-nothing (the round's best new K16 idea).** MEASURED: the Eagon-Northcott curve Γ_t is REDUCED on b₄≠0 at t=3,4,5 (simple points — multiplicities carry no structure); at t=3 the 7 points of Γ_3∩{b₄≠0} form ONE irreducible Galois orbit over A_3 (deg-7 univariate irreducible over Q(√3), Frobenius (2,5) at p=32003). IF this persists, clause (ii) is ALL-OR-NOTHING at each t: T_top (defined over A_t) vanishes at every orbit point or none ⇒ (V0)-tail at fixed t = ONE nonvanishing at ONE simple point (a modular evaluation at a good-reduction point, NO number-field std). The all-t problem SPLITS into (I) irreducibility of Γ_t over A_t for all t + (II) one uniform point with T_top≠0. Cheapest test: exact factorization of the Γ_4 (46 pts, desk) and Γ_5 (265 pts, worker) point polynomials. This turns the atom from a std into a Galois/irreducibility statement.
- **Coordinator LIAISON angle (complementary):** Γ is arithmetically Cohen-Macaulay (EN resolution); the nonzerodivisor atom = T_top ∉ any associated prime of (G) = the colon ideal (G):T_top equals (G); test at t=3,4 via the EN mapping cone. Fold into the Γ lane.

## 3. Moh ≤100 (Q2) — the finish is GATED on the h-support lemma
msolve is breaking the Singular compute wall (moh14-msolve running, UNIT [1] modular signals) — BUT (Astra + Fable) a msolve UNIT closes a row ONLY if (i) exact-Q confirmed (not a first-prime [1] modular-only signal) AND (ii) the chart is the PROVEN full necessary over-approximation (the h-support lemma). So the order of operations: prove the h-support lemma FIRST (moh-h-support-source-gate), then consume the msolve UNIT certificates. Both are now launched. If h-support fails (the chart is a sub-slice), complete it (add the missing D1 h-monomials) and re-solve.

## 4. Q3/Q4 — the all-degree program
Coverage (source→receiver atlas) + routing maps are the real reduction gap (minimality 17(pppppp) closed the one-place leak). Consensus: FIRST-SEPARATION is a citable lemma (Moh p.194 + minimality — write it); ROUTE-TO-STATE is mechanical (u_s=1→order chart; split→joint; unsplit→k=4 ray). So coverage = first-separation lemma + a finite per-degree census sweep, now fast via msolve at fleet scale (Opus/coordinator Q4: deploy fleet+msolve on the D≤200 u_s≥2 census = 1359 classes as a bounded batch). K16 t=8..11 is a side quest (the ray needs the structural atom §2, not more t).

## 5. Dispositions and launches
1. moh-h-support-source-gate (Astra's #1 — GATES all Moh ≤100 kills; the h support theorem or the missing hypothesis; the 76-coordinate comparison is ready): LAUNCHED moh-hsupport-gate-astra.
2. K16 Γ genericity/Galois (Fable Card A + the liaison angle): LAUNCHED k16-gamma-galois-fable5.
3. moh14-msolve (running): its UNITs are receipts-only until (1) delivers the h-support lemma; keep it running for the solver result.
QUEUED: the first-separation lemma write-up; the D≤200 census sweep via msolve; K16 t=8 (side).
STOP: treating the socle law as a proof of exact-square failure; treating a modular msolve [1] or a timeout as a kill without the h-support lemma + exact-Q.

<!-- BODY-END -->
