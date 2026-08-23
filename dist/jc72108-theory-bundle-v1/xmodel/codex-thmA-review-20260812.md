Reading additional input from stdin...
OpenAI Codex v0.147.0
--------
workdir: /Users/dc/code/math/jc72108
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: ultra
reasoning summaries: none
session id: 019ff78d-a91e-79f1-a83a-62a1088ea2e0
--------
user
You are an adversarial mathematical referee. Working directory: a research repo on the plane Jacobian Conjecture. Review the claimed proof of "Theorem A" in MATHIEU.md (the rigidity half of the residue conjecture): over char 0, if A, C are polynomials with A*C' - w*A'*C = c a nonzero constant (normalization inside the doc), then deg A <= 1. Read MATHIEU.md in full, plus MATHIEU-REVIEW.md (a prior review that confirmed it) and RESIDUE.md for context. Your job: try to REFUTE the proof. Re-derive every step independently; hunt for missed degree configurations, char-0 edge cases, and errors in the bridge Lemma B (block-to-ODE reduction, conventions in LEMMA.md). Attempt small counterexamples computationally if useful (python3 available; exact arithmetic only). VERDICT format: CONFIRMED / REFUTED / GAP-AT-<step>, then a numbered list of findings, each with the precise location and your independent derivation. Be terse and technical. Do not modify any files.
codex
I’ll audit the proof adversarially in three parallel tracks: a line-by-line independent derivation, a focused check of Lemma B against `LEMMA.md` conventions, and an exact-arithmetic counterexample search. I’ll read all three requested documents in full myself and make no file changes.
exec
/bin/zsh -lc 'wc -l MATHIEU.md MATHIEU-REVIEW.md RESIDUE.md LEMMA.md && rg -n "Theorem A|Lemma B|normalization|block|ODE|char|degree" MATHIEU.md MATHIEU-REVIEW.md RESIDUE.md LEMMA.md' in /Users/dc/code/math/jc72108
 succeeded in 32ms:
RESIDUE.md:8:Sources read: SURPLUS-EXT.md (§1.2-1.3, §2 Steps 3-4), SURPLUS.md (block
RESIDUE.md:11:- Block ODEs (units a1=c1=1): (I) AC' - kA'C = 1 (col k+1);
RESIDUE.md:34:  column-ODE solve, exact Fractions).
RESIDUE.md:105:dichotomy k+1 <= 2d2-1 (paper1 §6) is the degree count for the pole of
RESIDUE.md:119:second cokernel functional unreachable by G via degree count).
RESIDUE.md:125:one functional supported in degrees > deg G (invisible to every
RESIDUE.md:126:inhomogeneity); so the block obstruction on the binomial locus is
RESIDUE.md:131:Koszul/Lie differential of the near-origin block.
RESIDUE.md:135:extras t>=1 == 0 by pure degree count (deg G = 2d2+k-1 < (k+1)d2 + 1);
RESIDUE.md:145: S1 deg G <= 2d2+k-1 < (k+1)d2, since (k-1)(d2-1) > 0  [degree count]
RESIDUE.md:166:the depth-2 near-origin block is solvable iff
RESIDUE.md:175:dy/A^{k+1} at roots of A vanish AND the valuation normalization holds;
RESIDUE.md:203:    the block window (syzygy/Koszul reading), which is what makes the
LEMMA.md:1:# The −1 lemma for open_8_28_c2 chartG
LEMMA.md:3:Discharges the AUDIT.md claim-7 / notes.md TODO: identify equation #3,
LEMMA.md:7:`two_chart`. Re-runnable analysis: cases/eq3_anatomy.py, cases/eq3_chain.py
LEMMA.md:42:i.e. eq #3 is the **vertex normalization**: x² must be attained at the bottom
LEMMA.md:82:4. **two_chart.** For b3 this equation is the best pivot (|coeff|=1,
LEMMA.md:83:   |rest|=0): on the generic chart the coefficient is inverted and
LEMMA.md:90:   it. Full symbolic census after cascade+chart: 51/92 originals ≡ 0, 40
LEMMA.md:94:Equivalent ideal statement (chart-free): the derivation shows
LEMMA.md:97:precisely the cCa2/cCa6 complement split, and the generic chart (a2, a6
LEMMA.md:101:field in which the pivot constants are invertible: all char-0 fields, and
LEMMA.md:115:  **corner normalization**: for [P,Q] = x², the valuation of x² selects the
LEMMA.md:122:- With the gap dead, the near-origin block of tower relations becomes
LEMMA.md:123:  **overdetermined by one**: the block keys (2,0)..(2,4), (3,2)..(3,6) are
LEMMA.md:130:  corner normalization**. So yes: eq #3's collapse is a recognizable
LEMMA.md:142:  (i) *(vertex normalization)* x^k sits at the Minkowski vertex p₀+q₀ with
LEMMA.md:151:      elimination of the near-origin block (Q-columns (q₀)_x … (q₀)_x+1,
LEMMA.md:153:      eliminable unknowns; the surplus is the block's top-stratum key
LEMMA.md:158:the key x^k, i.e. the Minkowski vertex p₀+q₀) reduces on the chart where the
LEMMA.md:173:- (iii) fails with it: the near-origin block is exactly balanced /
LEMMA.md:176:  two_chart the vertex equation itself is consumed as the *definition*
LEMMA.md:177:  b1 := −1/a1 (chart pivot source = key (1,0), |rest|=1). Symbolic census:
LEMMA.md:179:  known fact that this chartG needed genuine F4 work.
LEMMA.md:184:to 0 against the vertex normalization), while reg_9_24_c3 has (q₀)_x = 1
LEMMA.md:189:- What is proved here (re-runnably): for open_8_28_c2, −1 ∈ ideal(chartG)
LEMMA.md:200:  the block is O(1)-sized and explicit — but not done here).
LEMMA.md:211:  with notes.md on c1's two_chart swell).
LEMMA.md:225:  10-event collapse, supporting an O(1)-block derivation of condition (iii).
MATHIEU.md:27:   coordinate-free proof (Theorem A) that A C′ − k A′ C = 1 with A, C
MATHIEU.md:28:   polynomials forces deg A ≤ 1, for every k ≥ 1, in characteristic 0.
MATHIEU.md:31:   (3,4), (4,4), (5,4) and all d2 ≥ 5.  Status: PROVED + PROMOTED (2026-08-12, MATHIEU-REVIEW.md: all six fronts CONFIRMED; Theorem A real; conj:R closes at every cell k,d2>=2 char 0). Original status: new proof, this file;
MATHIEU.md:125:j < d2).  So on the binomial locus the torus normalization is exact and
MATHIEU.md:126:NO twist blocks DvdK: it applies as stated.  But its conclusions are
MATHIEU.md:128:(one-sided supports in w) those hold for trivial degree reasons; DvdK
MATHIEU.md:158:Throughout §§3–5, F is a field of characteristic 0 (see §5.4 for char p),
MATHIEU.md:162:LEMMA B (block ⟺ ODE; the precise content of "rigidity half").  Fix
MATHIEU.md:164:The d2 − 1 inner extras of the depth-2 block vanish at a if and only if
MATHIEU.md:166:    (ODE)   A·C′ − k·A′·C = 1 .
MATHIEU.md:174:= 0 identically (Prop A's stratum w = 0); and the block keys
MATHIEU.md:176:y^1..y^{(k+1)d2−2} of (ODE).  The triangular solve (col_series, pivots
MATHIEU.md:177:n+1 ≠ 0 in char 0) uses the equations y^1..y^{kd2−1} to determine
MATHIEU.md:180:witnesses (ODE).  Conversely, a witness C of (ODE) with the stated
MATHIEU.md:183:constants of (F(y), d/dy) are F in char 0), and A^k(0) = 1 forces the
MATHIEU.md:189:(a) (properness) No element of M_A = Im(L_A) has y-degree (k+1)δ − 1;
MATHIEU.md:206:if d ≠ kδ then deg L_A(D) = δ+d−1 exactly (char 0: d − kδ ≠ 0 in F);
MATHIEU.md:208:C with L_A(C) of degree (k+1)δ−1: writing C = α·y^{kδ} + (rest), the
MATHIEU.md:209:y^{kδ}-part contributes degree ≤ (k+1)δ−2 and each other degree d
MATHIEU.md:210:contributes exact degree δ+d−1 ≠ (k+1)δ−1 with no cross-cancellation at
MATHIEU.md:211:distinct degrees — the top degree present among the parts survives.
MATHIEU.md:212:Hence degree (k+1)δ−1 is never attained.  [Machine check M2a.]
MATHIEU.md:219:F[y]_{≤n+δ−1} (by the lc-formula its degree is δ + deg C − 1 > n+δ−1
MATHIEU.md:226:(d) 1 ∉ M_A for all 2 ≤ deg A ≤ d2 says (ODE) has no polynomial
MATHIEU.md:230:Lemma B the inner extras then vanish only where deg A ≤ 1.  Conversely
MATHIEU.md:232:solves (ODE) within the support, so the extras vanish there — the
MATHIEU.md:261:  obstruction: the binomial locus), while for δ ≥ 2 Theorem A says no
MATHIEU.md:277:### 5.1 Theorem A
MATHIEU.md:279:THEOREM A (rigidity, all weights).  Let F have characteristic 0, let
MATHIEU.md:291:(i,j) = (δ,d).  [Machine check M4b.]  In char 0, d ≠ wδ implies
MATHIEU.md:294:Step 2 (top degree of C).  If deg C ≠ wδ, Step 1 gives
MATHIEU.md:301:Step 4 (subtract the kernel at top degree).  Let β := lc(C)/α^w ∈ F^×
MATHIEU.md:309:C = y at a2 = 0, for c = 1), so Theorem A is sharp; and it is exactly
MATHIEU.md:312:(w+1)δ − 1, which exceeds the map degree wδ as soon as δ ≥ 2 — the
MATHIEU.md:320:any field of characteristic 0: the inner extras of the depth-2 block
MATHIEU.md:324:Proof.  (⇐) On the binomial locus the explicit C above solves (ODE)
MATHIEU.md:325:within the support {y,…,y^k} ⊆ {y,…,y^{kd2}}; by Lemma B the extras
MATHIEU.md:326:vanish.  (⇒) If the extras vanish, Lemma B produces a polynomial C with
MATHIEU.md:327:A C′ − k A′ C = 1; Theorem A (w = k ≥ 2 ≥ 1) forces deg A ≤ 1.  ∎
MATHIEU.md:336:(ODE) at the multiple root (0 = 1) — no squarefreeness lemma needed —
MATHIEU.md:337:and squarefree A of degree ≥ 2 die by Step 4 — no residue divisibility
MATHIEU.md:339:Theorem A proves it could never hold (Corollary E).
MATHIEU.md:341:COROLLARY D (conj:R, full statement).  For every k, d2 ≥ 2, char 0:
MATHIEU.md:352:this file's review status.  Corollary C itself depends only on Lemma B
MATHIEU.md:353:and Theorem A.
MATHIEU.md:367:A C′ − (m−1) A′ C = A^m g′ = 1.  Theorem A (w = m−1 ≥ 1) forces
MATHIEU.md:376:never survives past degree 1.
MATHIEU.md:380:Theorem A as stated uses char 0 twice: (d − wδ) ≠ 0 in Step 1/2/4, and
MATHIEU.md:381:"constants of (F(y), d/dy) = F" inside Lemma B's uniqueness (and the
MATHIEU.md:382:triangular pivots n+1).  For the block instance all degrees are capped:
MATHIEU.md:384:holds over any field of characteristic p > (k+1)·d2 (conservative), in
MATHIEU.md:386:(2,2), etc.).  In small characteristic Step 2 genuinely fails (deg C
MATHIEU.md:388:Mondello example living in char 2.
MATHIEU.md:414:than two punctures, and this repo's block geometry is a ready-made
MATHIEU.md:416:(Theorem A stands independently).
MATHIEU.md:429:  of the full linear system (Gaussian elimination, generous degree cap),
MATHIEU.md:435:- M4 Theorem A's two computational identities, SYMBOLICALLY (generic A
MATHIEU.md:439:  two identities verified, the remaining content of Theorem A's proof
MATHIEU.md:453:list): no depth-2 block point with all coordinates nonzero for any
MATHIEU.md:463:hypotheses (gap-kill, full block columns), d1 = 1, no y-axis support;
MATHIEU.md:464:depth ≥ 3 untouched — though Theorem A is already the homogeneous
MATHIEU.md:469:Recommended next steps, in order: (1) adversarial review of Lemma B +
MATHIEU.md:470:Theorem A (the proof is 15 lines; the risk concentrates in Lemma B's
MATHIEU.md:471:block ⟺ ODE identification, which M5 tests at 9 cells); (2) absorb
MATHIEU.md:474:modulo §4b's write-up); (3) Lean formalization of Theorem A (kernel +
MATHIEU-REVIEW.md:4:Scope: Theorem A (rigidity, all weights), Lemma B (block ⟺ ODE), the
MATHIEU-REVIEW.md:11:dependency-status note), 5 CONFIRMED (scope characterized), 6 CONFIRMED
MATHIEU-REVIEW.md:18:## 1. Theorem A itself
MATHIEU-REVIEW.md:27:- Step 2: C = 0 gives LHS 0 ≠ c; deg C ≠ wδ gives exact LHS degree
MATHIEU-REVIEW.md:36:Step 2, no relative-degree assumption anywhere; C or A with repeated
MATHIEU-REVIEW.md:39:normalization lives in Lemma B, not here); w-coefficient edge — w ≥ 1
MATHIEU-REVIEW.md:42:(b) char-0 usage: exactly "(d − wδ) ≠ 0 in F" (Steps 1/2/4). Nothing
MATHIEU-REVIEW.md:43:else. §5.4's small-characteristic analysis is consistent (see §7 nit 1).
MATHIEU-REVIEW.md:45:(c) the c ≠ 0 normalization: RIGHT, and it cannot degenerate on a
MATHIEU-REVIEW.md:46:subvariety. In the unnormalized block gauge the ODE right side is
MATHIEU-REVIEW.md:48:block key — forces a1c1 = 1 on the whole variety. So after unit scaling
MATHIEU-REVIEW.md:60:counterexample exists in the sweep; exhaustive small-degree non-existence
MATHIEU-REVIEW.md:72:## 2. Lemma B (block ⟺ ODE) — the flagged weak point
MATHIEU-REVIEW.md:80:  (2,5). Post-gap-kill self-containedness of the depth-2 block is
MATHIEU-REVIEW.md:82:  and x^{k+1} coefficients are exactly the block equations.
MATHIEU-REVIEW.md:88:  triangular in c_2..c_{kd2} with pivots n+1 ∈ {2..kd2} ≠ 0 in char 0;
MATHIEU-REVIEW.md:94:  coefficient of the ODE); two witnesses differ by K ∈ ker L_A = F·A^k
MATHIEU-REVIEW.md:95:  (constants of (F(y), d/dy) = F in char 0 — standard, and the kernel
MATHIEU-REVIEW.md:99:- Gauge/normalization matching: units a_{p0} = b_{q0} = 1 as in
MATHIEU-REVIEW.md:103:  (Theorem A's weight w vs the stratum weight w = d2·i − j) — cosmetic,
MATHIEU-REVIEW.md:115:sound: distinct source degrees d ≠ kδ give distinct exact image degrees
MATHIEU-REVIEW.md:116:δ+d−1, the y^{kδ} part stays ≤ (k+1)δ−2, so degree (k+1)δ−1 is never
MATHIEU-REVIEW.md:121:the r_i — cosmetic). Circularity check: Theorem A's proof consumes ONLY
MATHIEU-REVIEW.md:147:  the dense chart), and solvability at a2 = 0 was fresh-verified
MATHIEU-REVIEW.md:153:  ARBITRARY b: block solvable).
MATHIEU-REVIEW.md:155:End-to-end (CHECK4, fresh linear algebra on the raw block, both columns,
MATHIEU-REVIEW.md:160:therefore stands; its honest dependency note is now discharged by this
MATHIEU-REVIEW.md:162:full block columns, depth 2, char 0.
MATHIEU-REVIEW.md:178:pathological A, end-to-end open-cell block tests. All OK. Remaining
MATHIEU-REVIEW.md:188:UPGRADES (if/now that Theorem A stands):
MATHIEU-REVIEW.md:192:  corollaries of Lemma B + Theorem A + the §4b closed form; the
MATHIEU-REVIEW.md:195:- Block-level: no depth-2 block point with all coordinates nonzero at
MATHIEU-REVIEW.md:208:- Depth ≥ 3 (attackable, NOT closed): Theorem A is weight-uniform
MATHIEU-REVIEW.md:210:  exists; what is missing is the depth-D Lemma B (block layout,
MATHIEU-REVIEW.md:217:than the block; deeper Minkowski columns (each adds one residue-type
MATHIEU-REVIEW.md:219:characteristic p ≤ (k+1)d2 (Mondello-consistent); SC1 (still open, still
MATHIEU-REVIEW.md:220:unneeded). Theorem A closes the depth-2 rigidity question — it does not
MATHIEU-REVIEW.md:228:2. Symbol collision: Theorem A's weight w vs LEMMA/SURPLUS's stratum
MATHIEU-REVIEW.md:233:confidence labels; nothing in Corollaries C/D depends on it — Theorem A
MATHIEU-REVIEW.md:237:Theorem A is a correct, complete, 15-line proof; Lemma B's block ⟺ ODE
MATHIEU-REVIEW.md:241:conj:R at EVERY cell k, d2 ≥ 2 in characteristic 0, including (3,4),
MATHIEU-REVIEW.md:252:  Theorem A sweep w ≤ 6, δ ≤ 5, adversarial A, kernel = span{A^w};
MATHIEU-REVIEW.md:253:  CHECK3 inner dichotomy at 7 cells; CHECK4 end-to-end conj:R block

exec
/bin/zsh -lc "nl -ba MATHIEU.md | sed -n '1,260p'" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
     1	# MATHIEU.md — Mathieu–Zhao framing of R_{k,d2}, and the rigidity half of conj:R
     2	
     3	Subject: the Mathieu subspace (Mathieu–Zhao) formulation of the residue
     4	functional R_{k,d2} (RESIDUE.md), and an attack on the rigidity half of
     5	paper1 conj:R through it.  Sources read: RESIDUE.md (full), SURPLUS.md,
     6	SURPLUS-EXT.md §§0–1, LEMMA.md, paper1/main.tex §§ variants+functional.
     7	Machine layer: cases/residue_check.py, new `mathieu` mode (§7; exit 0).
     8	
     9	## 0. Headline
    10	
    11	The Mathieu–Zhao lens does three things here.
    12	
    13	1. BRIDGE (§3): with M_A := Im(L_A), L_A := A d/dy − kA′ (the 1-variable
    14	   shadow of ad_{xA}, RESIDUE.md interp (c)), the rigidity half of conj:R
    15	   at (k,d2) is EXACTLY the statement "1 ∉ M_A for every A with
    16	   2 ≤ deg A ≤ d2".  If M_A is a Mathieu subspace, this follows at once,
    17	   because a Mathieu subspace containing 1 is the whole algebra and M_A is
    18	   provably proper.  Derived in full in §3.
    19	2. APPLICABILITY (§4): the outer functional R is an honest Laurent-
    20	   polynomial constant term (machine check M3), so Duistermaat–van der
    21	   Kallen applies literally there — but vacuously.  The inner (rigidity)
    22	   functional lives on a (δ+1)-punctured line, outside every proved
    23	   instance of the MZ program; the Mathieu property of M_A is open (§6).
    24	3. ATTACK (§5): the DvdK MECHANISM — the valuation-at-infinity /
    25	   one-sided-support argument that proves the 1-variable case — applies
    26	   directly to L_A and CLOSES the rigidity half: an elementary,
    27	   coordinate-free proof (Theorem A) that A C′ − k A′ C = 1 with A, C
    28	   polynomials forces deg A ≤ 1, for every k ≥ 1, in characteristic 0.
    29	   Consequently (with RESIDUE.md §4b's uniform outer theorem) conj:R
    30	   holds at ALL cells k, d2 ≥ 2 — including the previously open
    31	   (3,4), (4,4), (5,4) and all d2 ≥ 5.  Status: PROVED + PROMOTED (2026-08-12, MATHIEU-REVIEW.md: all six fronts CONFIRMED; Theorem A real; conj:R closes at every cell k,d2>=2 char 0). Original status: new proof, this file;
    32	   machine-corroborated at every step (§7); NEEDS adversarial review
    33	   before the paper absorbs it (repo practice: LEMMA-REVIEW pattern).
    34	
    35	## 1. The Mathieu–Zhao frame
    36	
    37	### 1.1 Definitions (Zhao)
    38	
    39	Let 𝒜 be a commutative algebra over a field F.  A subspace M ⊆ 𝒜 is a
    40	MATHIEU SUBSPACE (Mathieu–Zhao space) if: for every a ∈ 𝒜 such that
    41	a^m ∈ M for ALL m ≥ 1, and every b ∈ 𝒜, there is N = N(a,b) with
    42	b·a^m ∈ M for all m ≥ N.  Every ideal is Mathieu (with N = 1); the point
    43	of the notion is that M need not be closed under multiplication by 𝒜 —
    44	only powers of "radical-like" elements eventually absorb factors.
    45	Radical language: r(M) := {a : a^m ∈ M for all m ≫ 0} and
    46	sr(M) := {a : ∀b, b·a^m ∈ M for all m ≫ 0}; M is Mathieu iff every a
    47	with all powers in M lies in sr(M).
    48	
    49	Trivial but load-bearing lemma (used in §3): if M is Mathieu and 1 ∈ M,
    50	then M = 𝒜.  Proof: take a = 1; then 1^m = 1 ∈ M for all m, so for every
    51	b there is N with b = b·1^m ∈ M.  ∎
    52	
    53	### 1.2 The Duistermaat–van der Kallen theorem
    54	
    55	THEOREM (DvdK, Indag. Math. 9 (1998)).  Let 𝒜 = C[x_1^{±1},…,x_n^{±1}]
    56	and CT: 𝒜 → C the constant-term functional.  Then ker CT is a Mathieu
    57	subspace of 𝒜: if CT(f^m) = 0 for all m ≥ 1, then for every g ∈ 𝒜,
    58	CT(g f^m) = 0 for all large m.
    59	
    60	This is the abelian (torus) case of Mathieu's 1995 conjecture for compact
    61	connected Lie groups, and it is the ONE deep proved instance of the
    62	program.  In one variable the proof yields the sharp support dichotomy:
    63	
    64	  (DvdK-1D)  CT(f^m) = 0 for all m ≥ 1  ⟺  supp(f) ⊆ Z_{>0} or
    65	             supp(f) ⊆ Z_{<0}  (f a Laurent polynomial, f = 0 allowed).
    66	
    67	The mechanism of the 1-variable proof is a VALUATION argument at the two
    68	punctures 0, ∞: if the support is two-sided, the leading behavior of f^m
    69	at one puncture cannot cancel out of the constant term for every m.
    70	That mechanism — leading-term one-sidedness at a distinguished place —
    71	is what we transport in §5.  (Confidence: statement of the theorem HIGH;
    72	the 1-D dichotomy as stated HIGH on truth, MEDIUM on being verbatim in
    73	the paper.)
    74	
    75	### 1.3 Ledger: theorem vs conjecture in the MZ literature
    76	
    77	From memory (no web access); confidence labels per line.
    78	
    79	PROVED:
    80	- DvdK theorem, all n (above).  [HIGH]
    81	- Zhao's framework papers exist and fix the definitions used here:
    82	  "Generalizations of the image conjecture and the Mathieu conjecture"
    83	  (J. Pure Appl. Algebra 214 (2010)) and "Mathieu subspaces of
    84	  associative algebras" (J. Algebra 350 (2012)).  [HIGH]
    85	- van den Essen–Wright–Zhao: the Image Conjecture for COMMUTING
    86	  order-one operators with CONSTANT leading coefficients (the family
    87	  containing the Gaussian-moment / ∂_i − x_i reformulations of JC),
    88	  and: images of LOCALLY FINITE derivations of C[x,y] are Mathieu
    89	  (J. Pure Appl. Algebra 215 (2011)).  [MEDIUM]
    90	- Muzychuk–Pakovich: solution of the polynomial moment problem
    91	  (vanishing of all moments forces composition structure) — the closest
    92	  proved relative of "all residues of all powers vanish ⟹ structural
    93	  degeneration" on multiply-punctured domains.  [MEDIUM-HIGH]
    94	
    95	CONJECTURAL / NOT AVAILABLE:
    96	- Mathieu's conjecture for nonabelian compact G: open.  [HIGH]
    97	- Zhao's Image Conjecture in general: open.  [HIGH]
    98	- Images of order-one operators with NON-CONSTANT leading coefficient
    99	  (our L_A = A∂ − kA′): no proved Mathieu statement I can cite.  [HIGH
   100	  that I cannot cite one; the statement itself is §6's SC1.]
   101	- CT/residue functionals at ≥ 3 punctures (algebra C[y, 1/A], deg A ≥ 2):
   102	  outside DvdK and outside every weighted-CT extension known to me; the
   103	  weighted/twisted CT results in the MZ corpus stay on the 2-punctured
   104	  torus with monomial or Gaussian weights.  [MEDIUM-HIGH]
   105	- Laurent-SERIES analogues of DvdK (completed algebras): status unknown
   106	  to me; not usable as a theorem.  [MEDIUM]
   107	
   108	## 2. Our objects: algebras, functionals, candidate M
   109	
   110	The campaign's functional (paper1 §functional, RESIDUE.md):
   111	R_{k,d2} = Σ_{j=max(k+2,d2)}^{2d2} (−1)^j C(j,k+2) a2^{2d2−j} b_j,
   112	with three verified interpretations: CT-at-infinity (b), iterated
   113	Grothendieck residue of dP∧dQ/(x^{k+2}A^{k+2}) at the toric boundary
   114	point (a), Koszul moment functional μ spanning the reachable cokernel of
   115	ad_{xA} (c).  Three candidate (algebra, subspace) pairs present
   116	themselves; choosing correctly is most of the work.
   117	
   118	(i) OUTER pair — 𝒜 = C[w^{±1}], w = A(y) = 1 + a2·y the edge coordinate
   119	on the binomial locus (a2 ≠ 0), M = ker CT.  Here R is literally a
   120	Laurent-polynomial constant term:
   121	    R_{k,d2} = CT_w( β′(w) · w^{−(k+1)} ),   β(w) := B((w−1)/a2),
   122	equivalently a2^{2d2}·β_{k+2} = (−1)^k R (machine check M3, 12 cells —
   123	this identity also re-derives the max(k+2,d2) lower-limit correction of
   124	RESIDUE.md §1, since C(j,k+2) = 0 for j < k+2 and b_j is absent for
   125	j < d2).  So on the binomial locus the torus normalization is exact and
   126	NO twist blocks DvdK: it applies as stated.  But its conclusions are
   127	eventual-vanishing statements, and on the elements we care about
   128	(one-sided supports in w) those hold for trivial degree reasons; DvdK
   129	gives no leverage on the outer half — which RESIDUE.md §4b anyway proved
   130	uniformly.  The outer half is not where MZ content lives.
   131	
   132	(ii) INNER localized pair — 𝒜 = W := C[y][1/A] (the coefficient ring
   133	with the strip's edge polynomial inverted; A = P-column-1, deg A =: δ),
   134	M = Im(d/dy|_W) = ∩_{A(r)=0} ker Res_r(· dy).  This is the right
   135	invariant content: rigidity concerns the powers A^{−(k+1)}, and W is the
   136	function ring of the (δ+1)-punctured projective line (roots of A and ∞).
   137	For δ = 1 and A = y this is (a residue twist of) the DvdK 1-D situation;
   138	for δ ≥ 2 it is outside every proved MZ instance (§1.3).
   139	
   140	(iii) INNER polynomial pair (THE BRIDGE FRAME) — 𝒜 = C[y],
   141	    L_A := A·d/dy − k·A′  (multiplication),   M_A := Im(L_A).
   142	L_A is the 1-variable shadow of ad_{xA} on the inner column (RESIDUE.md
   143	interp (c), weight k), and L_A(C) = A^{k+1}·(C/A^k)′.  Note that
   144	ker(R) itself — the hyperplane in the b-coordinates — is NOT the right
   145	M: R is the pairing of the FIXED cokernel functional μ against the
   146	variable inhomogeneity G; the Mathieu structure lives on the μ/image
   147	side, i.e. in M_A, not in one hyperplane of values.
   148	
   149	Basic structure of M_A (proved in §3): μ_i ∘ L_A = 0 for the residue
   150	functionals μ_i(f) := Res_{r_i}(f·A^{−(k+1)} dy) at the roots r_i of A —
   151	the global, multi-point form of RESIDUE.md's μ; for squarefree A,
   152	M_A = ∩_i ker μ_i, of codimension exactly δ in C[y].  So M_A is a
   153	finite-codimension residue-kernel subspace — precisely the multi-point
   154	generalization of DvdK's ker CT.
   155	
   156	## 3. The bridge theorem
   157	
   158	Throughout §§3–5, F is a field of characteristic 0 (see §5.4 for char p),
   159	A ∈ F[y] with A(0) = 1 (units a1 = c1 = 1 scaled out as in SURPLUS-EXT
   160	§0), δ := deg A, and k ≥ 1.
   161	
   162	LEMMA B (block ⟺ ODE; the precise content of "rigidity half").  Fix
   163	k ≥ 2, d2 ≥ 2 and a point a = (a2,…,a_{d2+1}), A = 1 + Σ_{i≥1} a_{i+1}y^i.
   164	The d2 − 1 inner extras of the depth-2 block vanish at a if and only if
   165	there exists C ∈ F[y] with support in {y,…,y^{kd2}} such that
   166	    (ODE)   A·C′ − k·A′·C = 1 .
   167	Proof.  Post-gap-kill, bracket Minkowski column k+1, read as a
   168	polynomial in y, is A C′ − k A′ C with C = Q-column-k (SURPLUS-EXT §0,
   169	cross-verified against the independent lattice-determinant enumeration
   170	by surplus_ext.wide_W1).  The pair (A_i, c_j) contributes
   171	(j − ki)·a_{(1,i)}c_j·y^{i+j−1}, so with deg A ≤ d2, supp C ⊆ {1..kd2}:
   172	the y^0-coefficient is c_1 (the vertex equation, = 1 after unit
   173	scaling); the y^{(k+1)d2−1}-coefficient is (kd2 − k·d2)a_{(1,d2)}c_{kd2}
   174	= 0 identically (Prop A's stratum w = 0); and the block keys
   175	(k+1, s), s = 2..(k+1)d2−1 are exactly the remaining coefficients
   176	y^1..y^{(k+1)d2−2} of (ODE).  The triangular solve (col_series, pivots
   177	n+1 ≠ 0 in char 0) uses the equations y^1..y^{kd2−1} to determine
   178	c_2,…,c_{kd2} uniquely from c_1 = 1; the extras are the leftover
   179	equations y^{kd2}..y^{(k+1)d2−2}.  If the extras vanish, the solved C
   180	witnesses (ODE).  Conversely, a witness C of (ODE) with the stated
   181	support is UNIQUE: two solutions differ by an element of
   182	ker L_A = F·A^k (if A K′ = k A′ K then (K/A^k)′ = 0 in F(y), and the
   183	constants of (F(y), d/dy) are F in char 0), and A^k(0) = 1 forces the
   184	difference's constant term — hence the difference — to be 0 when both
   185	have zero constant term.  So the solved series equals C and the extras
   186	vanish.  ∎
   187	
   188	BRIDGE THEOREM.  Fix k ≥ 1 and A with δ = deg A ≥ 2.  Then:
   189	(a) (properness) No element of M_A = Im(L_A) has y-degree (k+1)δ − 1;
   190	    in particular y^{(k+1)δ−1} ∉ M_A and M_A ⊊ C[y].
   191	(b) (residue description) μ_i ∘ L_A = 0 for every root r_i of A, where
   192	    μ_i(f) := Res_{r_i}(f·A^{−(k+1)}dy); if A is squarefree,
   193	    M_A = ∩_{i=1}^{δ} ker μ_i, of codimension exactly δ.
   194	(c) (bridge) If M_A is a Mathieu subspace of C[y], then 1 ∉ M_A.
   195	(d) Hence: if M_A is Mathieu for every A with 2 ≤ deg A ≤ d2, then the
   196	    rigidity half of conj:R holds at (k, d2): the inner extras force
   197	    a_{(1,i)} = 0 for 2 ≤ i ≤ d2 ("A binomial").
   198	
   199	Proof.
   200	(a) LEADING-COEFFICIENT LEMMA (the engine of everything below): for
   201	D ∈ F[y] nonzero with d := deg D,
   202	    lc-formula:  coefficient of y^{δ+d−1} in L_A(D) = (d − kδ)·lc(A)·lc(D),
   203	and L_A(D) has no coefficient above y^{δ+d−1}.  [Only the top×top pair
   204	(i,j) = (δ,d) reaches i+j−1 = δ+d−1; its weight is (j − ki) = d − kδ.
   205	Machine check M4b, symbolic, k, δ = 1..4, all d ≤ kδ+2.]  So:
   206	if d ≠ kδ then deg L_A(D) = δ+d−1 exactly (char 0: d − kδ ≠ 0 in F);
   207	if d = kδ the top cancels and deg L_A(D) ≤ (k+1)δ − 2.  Now take any
   208	C with L_A(C) of degree (k+1)δ−1: writing C = α·y^{kδ} + (rest), the
   209	y^{kδ}-part contributes degree ≤ (k+1)δ−2 and each other degree d
   210	contributes exact degree δ+d−1 ≠ (k+1)δ−1 with no cross-cancellation at
   211	distinct degrees — the top degree present among the parts survives.
   212	Hence degree (k+1)δ−1 is never attained.  [Machine check M2a.]
   213	(b) μ_i(L_A(C)) = Res_{r_i}((A C′ − kA′C)A^{−(k+1)}dy)
   214	= Res_{r_i}((C/A^k)′ dy) = 0: the residue of an exact rational form
   215	vanishes.  This is RESIDUE.md interp (c)'s "μ ∘ L = 0", globalized from
   216	the binomial locus to every root of every A.  Codimension: L_A maps
   217	F[y]_{≤n} to F[y]_{≤n+δ−1} with 1-dimensional kernel F·A^k (n ≥ kδ), so
   218	dim L_A(F[y]_{≤n}) = n; and no C with deg C > n has L_A(C) in
   219	F[y]_{≤n+δ−1} (by the lc-formula its degree is δ + deg C − 1 > n+δ−1
   220	unless deg C = kδ ≤ n), so Im(L_A) ∩ F[y]_{≤n+δ−1} = L_A(F[y]_{≤n})
   221	has codimension δ in F[y]_{≤n+δ−1}, stably in n.  For squarefree A the δ
   222	functionals μ_i are linearly independent (f = (A/(y−r_i))^{k+1}·(y−r_i)^k
   223	separates them) and annihilate Im(L_A) by the above, so they cut it out.
   224	(c) By §1.1's lemma, a Mathieu M_A containing 1 would equal C[y],
   225	contradicting (a).  So 1 ∉ M_A.
   226	(d) 1 ∉ M_A for all 2 ≤ deg A ≤ d2 says (ODE) has no polynomial
   227	solution when deg A ≥ 2 (the support cap is automatic: any solution has
   228	deg C = kδ ≤ kd2 by the lc-formula, and can be normalized to zero
   229	constant term by subtracting C(0)·A^k, which preserves deg ≤ kδ).  By
   230	Lemma B the inner extras then vanish only where deg A ≤ 1.  Conversely
   231	on the binomial locus C = ((1+a2y)^k − 1)/(ka2) (or C = y at a2 = 0)
   232	solves (ODE) within the support, so the extras vanish there — the
   233	variety of the inner extras is exactly {A binomial}.  ∎
   234	
   235	Remark (shape of the bridge).  The mission's expected reduction was
   236	"powers of a unit-type element have eventually-vanishing R".  The frame
   237	that closes is sharper and simpler: the unit-type element is 1 itself,
   238	whose powers are constant — so "eventually" collapses to "now", and the
   239	Mathieu property is consumed exactly once, through "1 ∈ M ⟹ M = 𝒜".
   240	In the localized frame (ii) the same statement reads: rigidity at all
   241	weights simultaneously ⟺ NO power A^{−m} (m ≥ 2) of the unit 1/A of W
   242	lies in Im(d/dy|_W) when δ ≥ 2 — a per-power nonvanishing, which is
   243	strictly stronger than what Mathieu-ness of Im(d/dy|_W) asserts.  This
   244	is the honest reason MZ theorems alone cannot finish: they control
   245	eventual behavior, rigidity needs every power.  The proof in §5 supplies
   246	the per-power statement directly.
   247	
   248	## 4. Applicability of DvdK: exact diagnosis
   249	
   250	Is our CT form literally a Laurent-polynomial constant term?
   251	- OUTER: YES, with no twist.  R = CT_w(β′(w)·w^{−(k+1)}) on the binomial
   252	  locus (M3).  DvdK applies as a theorem; its conclusion is vacuous for
   253	  our purposes (§2(i)).  No weighted/twisted extension is needed.
   254	- INNER: NO.  Off the binomial locus the natural expansion places are
   255	  the δ roots of A plus ∞; the algebra is W = C[y,1/A], the function
   256	  ring of a (δ+1)-punctured P^1, and the functional is a TUPLE of
   257	  residues (μ_1,…,μ_δ), not one CT.  The DvdK hypothesis that fails is
   258	  the algebra itself: C[w^{±1}] is the 2-punctured case δ = 1.  The
   259	  minimal degeneration is visible already there: for δ = 1 the powers
   260	  A^{−m} (m ≥ 2) DO all lie in ker Res (one-sided Laurent support — no

exec
/bin/zsh -lc "nl -ba MATHIEU.md | sed -n '261,484p'" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
   261	  obstruction: the binomial locus), while for δ ≥ 2 Theorem A says no
   262	  power does.  The rigidity dichotomy of conj:R IS the DvdK 1-D support
   263	  dichotomy transported to the strip's toric boundary: "1/A behaves
   264	  like a one-sided Laurent monomial ⟺ deg A ≤ 1 ⟺ the edge polynomial
   265	  meets the boundary in at most one simple point".
   266	- Zhao's known extensions (weighted CT, image-conjecture cases with
   267	  constant leading coefficients, locally finite derivations in 2
   268	  variables) all stay on ≤ 2 punctures or constant-coefficient
   269	  operators; none covers L_A = A∂ − kA′ with deg A ≥ 2 (§1.3).  So the
   270	  bridge hypothesis of §3(c) is genuinely conjectural (SC1, §6) — but,
   271	  decisively, it is NOT needed: the DvdK mechanism itself closes the
   272	  problem at the one place where our geometry is still one-sided for
   273	  every A — the puncture at infinity.  That is §5.
   274	
   275	## 5. The attack: the rigidity half, proved
   276	
   277	### 5.1 Theorem A
   278	
   279	THEOREM A (rigidity, all weights).  Let F have characteristic 0, let
   280	w ≥ 1 be an integer, and let A, C ∈ F[y] satisfy
   281	    A·C′ − w·A′·C = c   for some constant c ∈ F, c ≠ 0.
   282	Then deg A ≤ 1.
   283	
   284	Proof.  Both A and C are nonzero (else the left side is 0 ≠ c).  Write
   285	δ := deg A, α := lc(A), and suppose δ ≥ 2.
   286	
   287	Step 1 (leading-coefficient lemma).  For any nonzero D ∈ F[y] with
   288	d := deg D, the coefficient of y^{δ+d−1} in A D′ − w A′ D is
   289	(d − wδ)·α·lc(D), and no higher power of y occurs.  Indeed the pair
   290	(A_i, D_j) contributes A_i D_j (j − wi) y^{i+j−1}, maximized at
   291	(i,j) = (δ,d).  [Machine check M4b.]  In char 0, d ≠ wδ implies
   292	(d − wδ) ≠ 0 in F, so then deg(A D′ − w A′ D) = δ + d − 1 exactly.
   293	
   294	Step 2 (top degree of C).  If deg C ≠ wδ, Step 1 gives
   295	deg(A C′ − w A′ C) = δ + deg C − 1 ≥ δ − 1 ≥ 1 > 0 = deg c,
   296	a contradiction.  Hence deg C = wδ.
   297	
   298	Step 3 (kernel element).  A·(A^w)′ − w·A′·A^w = wA^wA′ − wA′A^w = 0.
   299	[Machine check M4a.]
   300	
   301	Step 4 (subtract the kernel at top degree).  Let β := lc(C)/α^w ∈ F^×
   302	and D := C − β·A^w.  By Step 3, A D′ − w A′ D = c still; by
   303	construction deg D < wδ.  If D = 0 then c = 0, a contradiction.  If
   304	D ≠ 0 then d := deg D < wδ, so by Step 1
   305	deg(A D′ − w A′ D) = δ + d − 1 ≥ δ − 1 ≥ 1 > 0 = deg c,
   306	again a contradiction.  Hence δ ≥ 2 is impossible.  ∎
   307	
   308	For δ ≤ 1 the equation IS solvable (C = ((1+a2y)^w − 1)/(wa2), resp.
   309	C = y at a2 = 0, for c = 1), so Theorem A is sharp; and it is exactly
   310	the "valuation at infinity" DvdK mechanism: ord_∞ applied to
   311	dt = dy/A^{w+1}, t = C/A^w, says t − t(∞) vanishes at ∞ to order
   312	(w+1)δ − 1, which exceeds the map degree wδ as soon as δ ≥ 2 — the
   313	support of the would-be solution is forced one-sided past its own
   314	budget.  (The algebraic Steps 1–4 are that valuation argument made
   315	elementary; no Riemann–Hurwitz needed.)
   316	
   317	### 5.2 The rigidity half of conj:R
   318	
   319	COROLLARY C (rigidity half, ALL cells).  For every k ≥ 2, d2 ≥ 2, over
   320	any field of characteristic 0: the inner extras of the depth-2 block
   321	vanish at a = (a2,…,a_{d2+1}) iff a3 = … = a_{d2+1} = 0.  Equivalently
   322	V(inner extras) = {A binomial}: the inner column forces deg A ≤ 1.
   323	
   324	Proof.  (⇐) On the binomial locus the explicit C above solves (ODE)
   325	within the support {y,…,y^k} ⊆ {y,…,y^{kd2}}; by Lemma B the extras
   326	vanish.  (⇒) If the extras vanish, Lemma B produces a polynomial C with
   327	A C′ − k A′ C = 1; Theorem A (w = k ≥ 2 ≥ 1) forces deg A ≤ 1.  ∎
   328	
   329	This settles, structurally and uniformly, the cells proved before by
   330	per-cell work — (2,2) (inner extra −a3^k), (2,3)/(2,4) (squarefree +
   331	A | N(A) divisibility), (3,3),(4,3),(5,3) (resultant certificates
   332	with exponents (15,12),(26,34),(40,44)) — and the OPEN cells
   333	(3,4),(4,4),(5,4) and all d2 ≥ 5, where the perfect-power component of
   334	the divisibility route was the obstacle.  Note how the two halves of
   335	the old argument collapse: perfect powers (1+uy)^δ die by evaluating
   336	(ODE) at the multiple root (0 = 1) — no squarefreeness lemma needed —
   337	and squarefree A of degree ≥ 2 die by Step 4 — no residue divisibility
   338	A | N(A) needed.  The residue condition is bypassed, not solved:
   339	Theorem A proves it could never hold (Corollary E).
   340	
   341	COROLLARY D (conj:R, full statement).  For every k, d2 ≥ 2, char 0:
   342	    V(extras) = {A binomial} ∩ ({a2 = 0} ∪ {R_{k,d2} = 0}).
   343	Proof.  Corollary C reduces V(extras) to {A binomial} ∩ V(outer extras).
   344	On the binomial locus, RESIDUE.md §4b (uniform outer theorem, chain
   345	S1–S5; polynomial identities in (a2, b), so valid at a2 = 0 too) gives:
   346	outer extras t ≥ 1 vanish identically and
   347	extra_0 = ±(k+2)/C((k+1)d2, k+1)·a2^{(k−1)d2}·R_{k,d2}, which vanishes
   348	iff a2 = 0 or R = 0 (note (k−1)d2 > 0).  ∎
   349	Dependency note, honestly: §4b's S1–S5 is stated in RESIDUE.md as a
   350	general derivation with each step a short general argument, machine-
   351	verified at 11 cells; Corollary D inherits exactly that status plus
   352	this file's review status.  Corollary C itself depends only on Lemma B
   353	and Theorem A.
   354	
   355	### 5.3 The residue dichotomy (the statement MZ was circling)
   356	
   357	COROLLARY E.  Let A ∈ C[y] be squarefree with deg A ≥ 2.  Then for
   358	EVERY m ≥ 2 there is a root r of A with Res_r(A^{−m} dy) ≠ 0.  (For
   359	m = 1 all residues 1/A′(r) are nonzero; for deg A ≤ 1 all residues of
   360	all powers m ≥ 2 vanish.)
   361	
   362	Proof.  Suppose all residues of A^{−m}dy vanish.  Partial fractions
   363	(simple roots): A^{−m} = Σ_i Σ_{l=2}^{m} c_{i,l}(y−r_i)^{−l} with no
   364	l = 1 terms and no polynomial part; termwise integration gives
   365	g ∈ C(y) with g′ = A^{−m} and pole order ≤ m−1 at each r_i and no other
   366	poles.  Then C := A^{m−1}·g is pole-free, hence a polynomial, and
   367	A C′ − (m−1) A′ C = A^m g′ = 1.  Theorem A (w = m−1 ≥ 1) forces
   368	deg A ≤ 1, a contradiction.  ∎
   369	
   370	Corollary E is the exact multi-place analogue of DvdK-1D: "all powers
   371	of 1/A residue-free ⟺ the pole configuration is one-sided (a single
   372	simple point)".  It also explains RESIDUE.md §5's observation that
   373	perfect powers pass the residue test but fail the valuation: the
   374	residue test alone (A | N(A) for k = 2) has the perfect-power
   375	solutions, but the INTEGRATED statement — polynomiality of A^{m−1}g —
   376	never survives past degree 1.
   377	
   378	### 5.4 Characteristic
   379	
   380	Theorem A as stated uses char 0 twice: (d − wδ) ≠ 0 in Step 1/2/4, and
   381	"constants of (F(y), d/dy) = F" inside Lemma B's uniqueness (and the
   382	triangular pivots n+1).  For the block instance all degrees are capped:
   383	deg C ≤ kd2, |d − kδ| ≤ kd2, pivots n+1 ≤ (k+1)d2 − 1.  So Corollary C
   384	holds over any field of characteristic p > (k+1)·d2 (conservative), in
   385	the spirit of the campaign's per-cell prime exclusions ({2,3,5} at
   386	(2,2), etc.).  In small characteristic Step 2 genuinely fails (deg C
   387	can be wδ + p with vanishing leading weight), consistent with the
   388	Mondello example living in char 2.
   389	
   390	## 6. What remains for the MZ program proper: SC1
   391	
   392	The bridge hypothesis of §3(c) is now not needed, but it is the
   393	sharpest statement that MZ machinery would settle, and rigidity gives
   394	it evidence.  Recording it precisely:
   395	
   396	SUB-CONJECTURE SC1.  (a) Polynomial form: for every A ∈ C[y] squarefree
   397	with deg A = δ ≥ 1 and every k ≥ 1, M_A = Im(A∂ − kA′) =
   398	∩_{i=1}^δ ker(f ↦ Res_{r_i}(f A^{−(k+1)}dy)) is a Mathieu subspace of
   399	C[y].  (b) Localized form: Im(d/dy) = ∩_i ker Res_{r_i}(· dy) is a
   400	Mathieu subspace of C[y, 1/A].
   401	
   402	Status: open; not covered by DvdK (wrong algebra for δ ≥ 2: δ+1
   403	punctures) nor by any proved image-conjecture case (non-constant
   404	leading coefficient).  Evidence from this file: (1) Corollary E
   405	computes the full power-behavior of the natural test element a = 1/A in
   406	frame (b): for δ ≥ 2 NO power lies in M (so a imposes no Mathieu
   407	condition — consistency is free but meaningful: a genuinely fails the
   408	membership test at every m, not just at one); for δ = 1 all powers
   409	m ≥ 2 lie in M and the Mathieu conclusion holds explicitly —
   410	Res_r(b·A^{−m}) = u^{−m}b^{(m−1)}(r)/(m−1)! = 0 as soon as
   411	m > deg b + 1.  So SC1 passes every test reachable through powers of
   412	1/A.  (2) DvdK-1D is (a twist of) the case δ = 1 of (b).  A proof of
   413	SC1 for δ ≥ 2 would be the first Mathieu theorem on a curve with more
   414	than two punctures, and this repo's block geometry is a ready-made
   415	consumer; conversely a COUNTEREXAMPLE to SC1 would not damage conj:R
   416	(Theorem A stands independently).
   417	
   418	## 7. Mechanical verification (exact arithmetic)
   419	
   420	cases/residue_check.py, new additive mode:
   421	    python3 cases/residue_check.py mathieu     (exit 0 = all OK)
   422	Default invocation is unchanged (T0–T5 suite re-run: ALL OK).  Checks,
   423	all exact Fractions, run 2026-08-12, 0.3 s, MATHIEU OK:
   424	- M1 rigidity dichotomy: for k = 1..5, d2 = 2..5, every deg A = δ ≤ d2,
   425	  random/perfect-power/mixed numeric A: inner extras vanish ⟺ δ ≤ 1.
   426	  (Sampled corroboration of Corollary C on and off the repo grid.)
   427	- M2 bridge: (a) y^{(k+1)δ−1} ∉ Im(L_A) — properness witness of §3(a) —
   428	  and (b) 1 ∈ Im(L_A) ⟺ δ ≤ 1, both by exact inconsistency/solvability
   429	  of the full linear system (Gaussian elimination, generous degree cap),
   430	  k = 1..4, δ = 1..4, including non-squarefree A.  The δ = 1 solvable
   431	  control confirms the checker detects consistency when present.
   432	- M3 CT form: a2^{2d2}·β_{k+2} = (−1)^k R_{k,d2} symbolically at 12
   433	  cells (11 repo cells + (2,6)): R is an honest Laurent constant term;
   434	  independently re-derives the max(k+2,d2) lower-limit correction.
   435	- M4 Theorem A's two computational identities, SYMBOLICALLY (generic A
   436	  and D, k, δ = 1..4, all d ≤ kδ+2): L_A(A^k) ≡ 0, and the
   437	  leading-coefficient formula lc(L_A(D)) = (d − kδ)·lc(A)·lc(D) with
   438	  exact cancellation at d = kδ and no overflow above δ+d−1.  With these
   439	  two identities verified, the remaining content of Theorem A's proof
   440	  is integer inequalities (δ + d − 1 ≥ 1, d − wδ ≠ 0).
   441	- M5 per-cell tie at (2,2),(2,3),(3,3),(3,4),(4,4),(5,4),(2,5),(3,5),
   442	  (2,6) — including every previously OPEN cell within reach: symbolic
   443	  inner extras vanish identically on the binomial locus; are nonzero at
   444	  all perfect-power points (1+uy)^δ, 2 ≤ δ ≤ d2 (the historically
   445	  dangerous family) and at random off-binomial points; and the symbolic
   446	  and numeric solve paths agree.
   447	
   448	## 8. Consequences and next steps
   449	
   450	For conj:R: the conjecture's rigidity half is a theorem (Corollary C),
   451	and with RESIDUE.md §4b the full conj:R variety statement holds at every
   452	cell k, d2 ≥ 2 (Corollary D).  Downstream (paper1 §functional's own
   453	list): no depth-2 block point with all coordinates nonzero for any
   454	k, d2 ≥ 2; pinning-type obstruction only at (2,2); no b-side obstruction
   455	for d2 ≥ 3; no residue condition for k > 2d2 − 2.  The (3,3),(4,3),(5,3)
   456	certificates upgrade from certified computation to structural theorem;
   457	(3,4),(4,4),(5,4) and d2 ≥ 5 close.
   458	
   459	For the strip program: every strip-shaped reduced subcase with k ≥ 2,
   460	d2 ≥ 2 now carries the uniform support-rigidity + residue-hyperplane
   461	constraint at depth 2 — the case analysis of SECTION4/coverage can cite
   462	one theorem instead of a cell table.  Unchanged scope limits: strip
   463	hypotheses (gap-kill, full block columns), d1 = 1, no y-axis support;
   464	depth ≥ 3 untouched — though Theorem A is already the homogeneous
   465	engine at every weight w = k+D−1, so the depth-D prediction of
   466	RESIDUE.md §5 (one residue functional per deeper column) should now be
   467	attackable by the same two lemmas.
   468	
   469	Recommended next steps, in order: (1) adversarial review of Lemma B +
   470	Theorem A (the proof is 15 lines; the risk concentrates in Lemma B's
   471	block ⟺ ODE identification, which M5 tests at 9 cells); (2) absorb
   472	into paper1 (§ variants shrinks: thm:23/thm:24 rigidity halves and
   473	thm:k3 become corollaries; §functional's conjecture becomes a theorem
   474	modulo §4b's write-up); (3) Lean formalization of Theorem A (kernel +
   475	leading-coefficient argument; small, fits the repo's lean/ practice);
   476	(4) depth ≥ 3 via the weight-w engine; (5) SC1 as a standalone MZ
   477	contribution (first ≥ 3-puncture Mathieu statement), with Corollary E
   478	as its power ledger.
   479	
   480	## 9. Files
   481	
   482	- MATHIEU.md (this file).
   483	- cases/residue_check.py — `mathieu` mode appended (M1–M5); default
   484	  T0–T5 suite unchanged and re-verified.

exec
/bin/zsh -lc "nl -ba MATHIEU-REVIEW.md | sed -n '1,255p'" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
     1	# MATHIEU-REVIEW.md — Adversarial review of MATHIEU.md (commit 7242f2c)
     2	
     3	Reviewer: Claude (max-depth adversarial pass, 2026-08-12). Status: COMPLETE.
     4	Scope: Theorem A (rigidity, all weights), Lemma B (block ⟺ ODE), the
     5	Mathieu-frame bridge, composition with RESIDUE.md §4b, machine checks
     6	M1–M5, consequence audit. Reviewer code: /tmp/mathieu_review/fresh_check.py
     7	(written from scratch — own symbolic poly engine, own linear algebra, no
     8	imports from the repo; run 2026-08-12, exit 0, ~5 s).
     9	
    10	VERDICTS: 1 CONFIRMED, 2 CONFIRMED, 3 CONFIRMED, 4 CONFIRMED (with a
    11	dependency-status note), 5 CONFIRMED (scope characterized), 6 CONFIRMED
    12	(two scope sharpenings). Overall: **THEOREM A IS A REAL PROOF.** The
    13	rigidity half of conj:R is closed at every cell k, d2 ≥ 2, and with
    14	RESIDUE.md §4b (whose S1–S5 chain this review independently re-derives in
    15	full generality) conj:R holds in full. No error found in any load-bearing
    16	line. Nits: 3, all cosmetic, listed in §7.
    17	
    18	## 1. Theorem A itself
    19	Verdict: CONFIRMED — correct, complete, elementary, sharp.
    20	
    21	Independent re-derivation (from scratch, before re-reading §5.1; my
    22	derivation reproduced Steps 1–4 exactly):
    23	- Step 1: A D′ − w A′ D = Σ_{i,j} A_i D_j (j − wi) y^{i+j−1}; the exponent
    24	  δ+d−1 is reached ONLY by (i,j) = (δ,d) (i ≤ δ, j ≤ d, i+j = δ+d forces
    25	  equality), coefficient (d − wδ)·lc(A)·lc(D); nothing higher. Char 0
    26	  enters here and only here: d ≠ wδ (integers) ⟹ d − wδ ≠ 0 in F.
    27	- Step 2: C = 0 gives LHS 0 ≠ c; deg C ≠ wδ gives exact LHS degree
    28	  δ + deg C − 1 ≥ δ − 1 ≥ 1 > 0 = deg c (uses δ ≥ 2; this is where the
    29	  d = 0 loophole of δ = 1 is closed — see scope remark below). So
    30	  deg C = wδ.
    31	- Step 3: L_A(A^w) = 0 — one line, any ring.
    32	- Step 4: D := C − (lc(C)/lc(A)^w)A^w has deg D < wδ and L_A(D) = c by
    33	  linearity; D = 0 gives c = 0, D ≠ 0 re-enters Step 2. Contradiction. ∎
    34	
    35	Degree-configuration audit (the mission's (a)): deg C < deg A — killed by
    36	Step 2, no relative-degree assumption anywhere; C or A with repeated
    37	roots — irrelevant, the proof is pure leading-coefficient algebra;
    38	A(0) = 0 or lc(A) pathological — the theorem nowhere uses A(0) = 1 (the
    39	normalization lives in Lemma B, not here); w-coefficient edge — w ≥ 1
    40	integer suffices, w enters only through d − wδ and A^w.
    41	
    42	(b) char-0 usage: exactly "(d − wδ) ≠ 0 in F" (Steps 1/2/4). Nothing
    43	else. §5.4's small-characteristic analysis is consistent (see §7 nit 1).
    44	
    45	(c) the c ≠ 0 normalization: RIGHT, and it cannot degenerate on a
    46	subvariety. In the unnormalized block gauge the ODE right side is
    47	det(p0,q0)·a_{p0}·b_{q0} = a1·c1, and the vertex equation — itself a
    48	block key — forces a1c1 = 1 on the whole variety. So after unit scaling
    49	c = 1 identically; there is no locus where the constant vanishes. (c = 0
    50	must be excluded: C = λA^w solves the homogeneous equation for every A.)
    51	
    52	Counterexample sweep (fresh code, CHECK2): w = 1..6, deg A = 2..5,
    53	adversarial A — random, perfect powers (1+uy)^δ, mixed multiplicity
    54	(y−r)^{δ−1}(y−s), A(0) = 0 (y^m·squarefree), pure monomials y^δ, huge
    55	coefficients (lc = (10^9+7)/3) — window deg C ≤ wδ + 12 (well past the
    56	forced wδ): the system A C′ − w A′ C = 1 is INCONSISTENT in every
    57	instance; δ ≤ 1 controls solvable; and the homogeneous kernel on the full
    58	window is EXACTLY span{A^w} in every instance (independent confirmation
    59	of Steps 3–4's structure, beyond M2's k ≤ 4, δ ≤ 4, window kδ+6). No
    60	counterexample exists in the sweep; exhaustive small-degree non-existence
    61	strengthens the theorem as requested.
    62	
    63	Also verified: the ord_∞ remark's arithmetic (ord_∞(c·dy/A^{w+1}) =
    64	(w+1)δ − 2 ⟹ t − t(∞) vanishes to order (w+1)δ − 1, vs the deg-based
    65	order wδ − deg D ≤ wδ; (w+1)δ − 1 > wδ ⟺ δ ≥ 2 forces D = 0,
    66	contradicting dt ≠ 0). The remark is a faithful reading of Steps 1–4.
    67	
    68	Scope remark (not an error): at δ = 1 constant C also solve (with
    69	c = −wa2C ≠ 0), so "any solution has deg C = wδ" is a δ ≥ 2 statement —
    70	exactly the scope in which Bridge (d)'s parenthetical invokes it.
    71	
    72	## 2. Lemma B (block ⟺ ODE) — the flagged weak point
    73	Verdict: CONFIRMED. Every step re-derived; conventions match; no slip.
    74	
    75	- Column identification, independently: fresh symbolic bracket
    76	  computation (CHECK1, own poly engine): for fully symbolic A, B, C, E,
    77	  [xA + x²B, x^kC + x^{k+1}E] has x^k column ≡ AC′ − kA′C, x^{k+1}
    78	  column ≡ AE′ − (k+1)A′E + 2BC′ − kB′C, x^{k+2} column ≡ the depth-3
    79	  column 2BE′ − (k+1)B′E, and nothing else — verified at (2,2), (3,4),
    80	  (2,5). Post-gap-kill self-containedness of the depth-2 block is
    81	  SURPLUS.md's Prop A/B territory (reviewed there); given it, the x^k
    82	  and x^{k+1} coefficients are exactly the block equations.
    83	- Bookkeeping, by hand: y^0 coefficient = 1·c_1 (vertex; det(p0,q0) =
    84	  det((1,0),(k,1)) = 1, so a1c1 = 1 and c_1 = 1 in the scaled gauge);
    85	  y^{(k+1)d2−1} coefficient = (kd2 − kd2)a_{(1,d2)}c_{kd2} = 0, and
    86	  (i,j) = (d2, kd2) is the ONLY pair reaching that exponent — the w = 0
    87	  stratum of Prop A, correctly matched; equations y^1..y^{kd2−1}
    88	  triangular in c_2..c_{kd2} with pivots n+1 ∈ {2..kd2} ≠ 0 in char 0;
    89	  extras = y^{kd2}..y^{(k+1)d2−2}, count d2 − 1 = Prop B's inner strata
    90	  w ∈ [1, d2−1]. All checked against surplus_count/surplus_ext
    91	  conventions (w0/W1 lattice cross-check re-run, exit 0) and against
    92	  LEMMA.md's (2,2) instance (−a3²b3/a1 ↔ normalized −a3²).
    93	- Converse/uniqueness: a witness C automatically has c_1 = 1 (the y^0
    94	  coefficient of the ODE); two witnesses differ by K ∈ ker L_A = F·A^k
    95	  (constants of (F(y), d/dy) = F in char 0 — standard, and the kernel
    96	  claim was independently confirmed numerically in CHECK2) with
    97	  K(0) = 0 ⟹ λ = 0 since A^k(0) = 1. Equivalently: triangularity alone
    98	  forces witness = solved series. Both routes valid.
    99	- Gauge/normalization matching: units a_{p0} = b_{q0} = 1 as in
   100	  SURPLUS-EXT §0; the corner saturations enter only through the vertex
   101	  equation, which supplies the nonzero constant (Front 1(c)); the
   102	  stratum-w conventions match Prop A/B exactly. One symbol collision
   103	  (Theorem A's weight w vs the stratum weight w = d2·i − j) — cosmetic,
   104	  §7 nit 2.
   105	- Numeric dichotomy at the previously OPEN cells, fresh path (CHECK3):
   106	  inner system solvable ⟺ deg A ≤ 1 at (3,4), (4,4), (5,4), (2,5),
   107	  (3,5), (2,6), (2,2), random/power/mixed A, every δ ≤ d2. All OK.
   108	
   109	## 3. The bridge (Mathieu frame) and circularity
   110	Verdict: CONFIRMED — implication direction correct; no circularity;
   111	the Mathieu hypothesis is genuinely bypassed.
   112	
   113	Bridge chain: M_A proper (a) + Mathieu ⟹ 1 ∉ M_A (c) ⟹ rigidity (d) —
   114	each step's direction checked. (a)'s no-cross-cancellation argument is
   115	sound: distinct source degrees d ≠ kδ give distinct exact image degrees
   116	δ+d−1, the y^{kδ} part stays ≤ (k+1)δ−2, so degree (k+1)δ−1 is never
   117	attained (fresh-verified as M2a's witness, and by hand). (b)'s residue
   118	description: μ_i∘L_A = 0 is the exactness of (C/A^k)′dy; the
   119	independence witness A^{k+1}/(y−r_i) is a polynomial with μ_j-value
   120	δ_{ij}; codimension-δ bookkeeping checks (needs the splitting field for
   121	the r_i — cosmetic). Circularity check: Theorem A's proof consumes ONLY
   122	the lc-formula and L_A(A^w) = 0 — no Mathieu property, no rigidity, no
   123	§4b, no M_A structure. §3(c)'s hypothesis (SC1) is never used
   124	downstream; MATHIEU.md says so explicitly and truthfully (§4, §6). The
   125	per-power Remark after the Bridge Theorem is also correct: Corollary E
   126	gives every power, which Mathieu-ness alone could not.
   127	
   128	## 4. Composition with RESIDUE.md §4b ⟹ conj:R in full
   129	Verdict: CONFIRMED — and this review now supplies the missing general
   130	hand-derivation of §4b's chain, upgrading Corollary D's dependency.
   131	
   132	RESIDUE.md §4b (S1–S5) had "general derivation + 11-cell machine check"
   133	status with no standalone review. Re-derived here in full generality:
   134	- S1: deg G ≤ 2d2+k−1 < (k+1)d2 ⟺ (k−1)(d2−1) > 0 ✓ (k, d2 ≥ 2).
   135	- S2: outer extras t ≥ 1 touch only e_n with n > (k+1)d2 (absent) and
   136	  G_n = 0 ✓ identically zero.
   137	- S3: extra_0 = ((k+1)d2 − (k+1))·a2·e_top = (k+1)(d2−1)a2·e_top ✓.
   138	- S4: L(E_solved) + G = extra_0·y^{n0} exactly as polynomials; μ∘L = 0
   139	  gives extra_0·μ(n0) = μ(G); μ(n0) = ±C(n0,k+1)a2^{−(n0+1)} ≠ 0 ✓.
   140	- S5 (first full-generality hand check in the campaign): with z = 1+a2y,
   141	  μ(G) = (1/a2)[z^{k+1}](2βz^{k−1} − β′z^k + β′) = (1/a2)(2β_2 − 2β_2 +
   142	  (k+2)β_{k+2}) = (k+2)β_{k+2}/a2, and β_{k+2} = (−1)^k a2^{−2d2}R (M3's
   143	  symbolic identity, itself a two-line binomial expansion). Sign:
   144	  (−1)^{(k+1)d2−1} = (−1)^{k+(k+1)(d2−1)} ✓; a2-power (k−1)d2 ✓; unit
   145	  (k+2)/C((k+1)d2,k+1) ✓ — the closed form is exact, all k, d2 ≥ 2.
   146	- a2 = 0 branch: the closed form is a polynomial identity (extends from
   147	  the dense chart), and solvability at a2 = 0 was fresh-verified
   148	  directly (CHECK4d).
   149	- Sum-start correction j = max(k+2,d2): automatic in R (C(j,k+2) = 0
   150	  below k+2, b_j absent below d2); fresh-verified at (2,5).
   151	- Empty-sum cells k+2 > 2d2: R ≡ 0, Corollary D degenerates to
   152	  V(extras) = {A binomial} — fresh-verified at (5,3) (binomial A +
   153	  ARBITRARY b: block solvable).
   154	
   155	End-to-end (CHECK4, fresh linear algebra on the raw block, both columns,
   156	unknowns (C,E)): at (3,4), (4,4), (5,4), (2,5), (5,3) — non-binomial A
   157	⟹ inconsistent; binomial, a2 ≠ 0, R ≠ 0 ⟹ inconsistent; binomial with
   158	R = 0 (or a2 = 0, or empty sum) ⟹ consistent. Exactly conj:R's
   159	biconditional, at every previously open cell within reach. Corollary D
   160	therefore stands; its honest dependency note is now discharged by this
   161	review. Scope unchanged: k, d2 ≥ 2, strip hypotheses (i) + gap-kill +
   162	full block columns, depth 2, char 0.
   163	
   164	## 5. Machine checks M1–M5: theorem vs instances
   165	Verdict: CONFIRMED as corroboration; scope correctly disclosed in §7.
   166	
   167	What the code actually tests: M1, M2, M5(ii)(iii)(iv) are SAMPLED
   168	instances (random/structured points, finite grids) — they corroborate,
   169	they do not prove universally quantified statements. M3 and M4 are
   170	symbolic identities, but on finite (k, δ, d) grids. M5(i) is a genuine
   171	per-cell symbolic proof of the ⇐ direction (binomial ⟹ extras ≡ 0) at
   172	9 cells. The universal content rests on the 15-line proof — whose entire
   173	computational payload is exactly M4's two identities plus integer
   174	inequalities, as §7 honestly states. Both suites re-run: `mathieu` exit
   175	0 (0.3 s), default T0–T5 ALL OK, surplus_ext exit 0. Decisive additional
   176	check, run in /tmp (nothing added to the repo): fresh_check.py CHECK1–4
   177	as described above — independent implementation, wider windows,
   178	pathological A, end-to-end open-cell block tests. All OK. Remaining
   179	gold-standard step (recommended, not required): the planned Lean
   180	formalization of Steps 1–4, and/or Groebner radical-membership
   181	certificates a3,…,a_{d2+1} ∈ √(inner ideal) at (3,4),(4,4),(5,4) as a
   182	third algebraic path (no sympy on this machine; the repo's resultant
   183	certificates already cover the d2 = 3 grid and (2,4)).
   184	
   185	## 6. Consequence audit
   186	Verdict: CONFIRMED, with the boundary drawn precisely.
   187	
   188	UPGRADES (if/now that Theorem A stands):
   189	- paper1: conj:R (§functional) becomes a theorem for all k, d2 ≥ 2
   190	  modulo absorbing §4b's write-up; thm:23/thm:24 rigidity halves,
   191	  thm:23full/thm:24 outer parts, and thm:k3's certificates become
   192	  corollaries of Lemma B + Theorem A + the §4b closed form; the
   193	  "certified computation, not a structural proof" caveat and the "open
   194	  at (3,4),(4,4),(5,4) and d2 ≥ 5" paragraph both die.
   195	- Block-level: no depth-2 block point with all coordinates nonzero at
   196	  any k, d2 ≥ 2 (a_{(1,2)} = 0 is forced); pinning form only at (2,2);
   197	  no b-side obstruction for d2 ≥ 3; no residue condition for
   198	  k > 2d2 − 2.
   199	- GGV catalog (SURPLUS-EXT §3 / paper1 §coverage): the conditional
   200	  "d2 ≥ 4 would be open" branch for the four k ≥ 3 rows closes — ANY
   201	  hypothetical strip reduction of any admissible family now lands in a
   202	  theorem-covered cell at depth 2; the scope map's cell table collapses
   203	  to one uniform statement.
   204	- Farm/SECTION4: the depth-2 rigidity + residue-hyperplane constraint is
   205	  available uniformly as a pre-filter at every strip-shaped cell — one
   206	  citation instead of a cell table; SURPLUS-EXT's per-cell resultant
   207	  certificates become redundant (kept as independent corroboration).
   208	- Depth ≥ 3 (attackable, NOT closed): Theorem A is weight-uniform
   209	  (w = k+D−1), so the deeper inner columns' homogeneous rigidity engine
   210	  exists; what is missing is the depth-D Lemma B (block layout,
   211	  self-containedness, inhomogeneity structure) — RESIDUE §5's prediction
   212	  remains a prediction.
   213	
   214	DOES NOT FOLLOW: k = 1 (no-gap) families — no bridge there (and conj:R
   215	excludes them); pentagon / y-axis-support shapes (subcase-1-type,
   216	open_8_28_c1 regime — gap-kill fails); d1 ≥ 2 strips; strips shorter
   217	than the block; deeper Minkowski columns (each adds one residue-type
   218	condition, joint behavior open — "deeper Minkowski columns" stay open);
   219	characteristic p ≤ (k+1)d2 (Mondello-consistent); SC1 (still open, still
   220	unneeded). Theorem A closes the depth-2 rigidity question — it does not
   221	by itself discard any GGV family whose reduction is not strip-shaped.
   222	
   223	## 7. Nits (no load-bearing consequence; suggest absorbing)
   224	1. §5.4: "pivots n+1 ≤ (k+1)d2 − 1" — true for the inner column
   225	   (≤ kd2), but the OUTER column's triangular pivots reach (k+1)d2.
   226	   The stated conservative bound p > (k+1)d2 still covers both columns
   227	   (and Corollary C needs only the inner ones); no conclusion changes.
   228	2. Symbol collision: Theorem A's weight w vs LEMMA/SURPLUS's stratum
   229	   weight w = d2·i − j. Rename one in the paper write-up.
   230	3. Bridge Theorem (b): the μ_i live over the splitting field of A;
   231	   harmless (and (b) is not load-bearing for rigidity).
   232	Also noted: §1.2–1.3's literature ledger is memory-sourced with honest
   233	confidence labels; nothing in Corollaries C/D depends on it — Theorem A
   234	is self-contained. DvdK is inspiration, not dependency.
   235	
   236	## 8. Bottom line
   237	Theorem A is a correct, complete, 15-line proof; Lemma B's block ⟺ ODE
   238	bridge — the author's own flagged weak point — survives full re-derivation
   239	and an independent bracket-level machine check; the composition with
   240	RESIDUE.md §4b (S1–S5 now hand-derived in full generality here) yields
   241	conj:R at EVERY cell k, d2 ≥ 2 in characteristic 0, including (3,4),
   242	(4,4), (5,4) and all d2 ≥ 5, with the empty-sum and sum-start edge cases
   243	verified. The rigidity half of conj:R is a theorem. Recommend: absorb
   244	into paper1 (with nits 1–2), keep the resultant certificates as
   245	redundancy, proceed with the Lean formalization of Steps 1–4, and open
   246	the depth-≥3 front via the weight-w engine.
   247	
   248	## Files
   249	- MATHIEU-REVIEW.md (this file).
   250	- /tmp/mathieu_review/fresh_check.py — reviewer's independent suite
   251	  (CHECK1 symbolic bracket identity at (2,2),(3,4),(2,5); CHECK2
   252	  Theorem A sweep w ≤ 6, δ ≤ 5, adversarial A, kernel = span{A^w};
   253	  CHECK3 inner dichotomy at 7 cells; CHECK4 end-to-end conj:R block
   254	  tests at (3,4),(4,4),(5,4),(2,5),(5,3)). Exit 0. Not added to the
   255	  repo per review protocol; re-create from this description if needed.

exec
/bin/zsh -lc "nl -ba RESIDUE.md | sed -n '1,217p'" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
     1	# RESIDUE.md — Is R_{k,d2} a residue?
     2	
     3	Subject: R_{k,d2} = sum_j (-1)^j C(j,k+2) a2^(2d2-j) b_j (from SURPLUS-EXT.md).
     4	Question: is R a residue in a precise sense (Grothendieck residue / constant-term
     5	extraction / Koszul obstruction), and does that give a coordinate-free proof?
     6	
     7	## 0. Setup and data (from repo)
     8	Sources read: SURPLUS-EXT.md (§1.2-1.3, §2 Steps 3-4), SURPLUS.md (block
     9	cascade, scope map), LEMMA.md §3 (tower/valuation reading), paper1/main.tex
    10	§6 (conj:R).
    11	- Block ODEs (units a1=c1=1): (I) AC' - kA'C = 1 (col k+1);
    12	  (II) AE' - (k+1)A'E = -(2BC' - kB'C) =: -G (col k+2).
    13	  A = P col 1 (deg d2, A(0)=1), B = P col 2 (y^{d2}..y^{2d2}, coeffs b_j),
    14	  C = Q col k (val 1), E = Q col k+1 (val d2+1... val >= 3 at d2=2).
    15	- On binomial locus A = 1 + a2 y, z := 1 + a2 y, beta(z) := B(y(z)):
    16	  E = -(1/a2) z^{k+1} int_1^z [2 beta w^{-3} - beta' w^{-2} + beta' w^{-(k+2)}] dw.
    17	  Obstruction = coefficient of w^{-1} in beta'(w) w^{-(k+2)}, i.e.
    18	  beta'_{k+1} = (k+2) beta_{k+2} (z-basis coeff). Repo asserts
    19	  beta'_{k+1} ≐ R_{k,d2} = sum_{j=k+2}^{2d2} (-1)^j C(j,k+2) a2^{2d2-j} b_j
    20	  up to unit * a2-power. NOTE b_j here = P-col-2 coefficient a_{(2,j)}.
    21	- KEY OBSERVATION (starting point): R is BY CONSTRUCTION a residue at w=0
    22	  of the 1-form beta'(w) w^{-(k+2)} dw — the repo's derivation already says
    23	  so. The real question is whether this lifts to a residue of a form built
    24	  COORDINATE-FREELY from (P,Q) themselves (interp (a)/(b)), not from the
    25	  solved column's integrand. Also: Res_{w=0} beta' w^{-(k+2)} dw =
    26	  Res_{w=infty} too (sum of residues = 0 on P^1, only poles 0, infty)?
    27	  beta' has deg 2d2-1, so at infty pole order (2d2-1)-(k+2)+2; nonzero
    28	  residue at infty iff k+1 <= 2d2-1: SAME dichotomy. To check.
    29	- Proved cells with exact data: (2,2) [R = b4 = a6, obstruction
    30	  -(1/5)a2^2 a6]; (2,3) [R = a2^2 b4 - 5 a2 b5 + 15 b6, unit a2^3/21];
    31	  (2,4) [R4, unit -a2^4/55]; certified (3,3) [-a2^6/99], (4,3)
    32	  [2a2^9/1001], (3,4) [-a2^8/364]; (5,3) empty sum, all outer vanish.
    33	- Machine layer to reuse: cases/surplus_ext.py wide_setup (general (k,d2)
    34	  column-ODE solve, exact Fractions).
    35	
    36	## 1. Explicit R in proved cells
    37	Machine: cases/residue_check.py (exact Fractions; reuses surplus_ext.py;
    38	run 2026-08-07, exit 0, 48 checks OK). T0 anchors the direct binomial-locus
    39	solve against the repo's general-solve-then-restrict (binom_outer) at
    40	(2,2),(2,3),(3,3): identical extras.
    41	Cells computed (11): (2,2),(2,3),(2,4),(3,3),(4,3),(3,4),(5,3) [repo grid]
    42	+ (4,4),(5,4),(2,5),(3,5) [NEW, beyond repo grid]. Surviving outer extra
    43	on the binomial locus, all cells (T5, exact):
    44	  extra_0 = (-1)^{k+(k+1)(d2-1)} * (k+2)/C((k+1)d2, k+1) * a2^{(k-1)d2} * R
    45	  (2,2): -(4/20) a2^2 b4        = -(1/5) a2^2 a6      [= repo theorem]
    46	  (2,3): +(4/84) a2^3 R         = (a2^3/21) R          [= repo]
    47	  (2,4): -(4/220) a2^4 R        = -(a2^4/55) R         [= repo]
    48	  (3,3): -(5/495) a2^6 R        = -(a2^6/99) R         [= repo]
    49	  (4,3): +(6/3003) a2^9 R       = (2 a2^9/1001) R      [= repo]
    50	  (3,4): -(5/1820) a2^8 R       = -(a2^8/364) R        [= repo]
    51	  (5,3): R = empty sum, extra_0 = 0                    [= repo]
    52	  NEW  (4,4): -(6/C(20,5)) a2^12 (a2^2 b6 - 7 a2 b7 + 28 b8)
    53	  NEW  (5,4): -(7/C(24,6)) a2^16 (-a2 b7 + 8 b8)
    54	  NEW  (2,5): +(4/C(15,3)) a2^5 (-5a2^5 b5 + 15a2^4 b6 - 35a2^3 b7
    55	              + 70a2^2 b8 - 126a2 b9 + 210 b10)
    56	  NEW  (3,5): -(5/C(20,4)) a2^10 R_{3,5}
    57	DEFINITION CORRECTION found at (2,5): the sum must run
    58	j = max(k+2, d2)..2d2 (b_j exists only for j >= d2); the repo's lower
    59	limit k+2 is correct only when k+2 >= d2, which held on its whole grid.
    60	The mystery unit denominators 5,21,55,99,1001,364 are (k+2)/C((k+1)d2,k+1)
    61	— the moment mu(n0) of the residue functional at the top pivot (see §4b).
    62	
    63	## 2. Interpretation (a): Grothendieck/global residue of a rational form
    64	CANDIDATE (a1). Let P = xA + x^2 B (+ higher cols), A = (P/x)|_{x=0} the
    65	edge polynomial on the toric boundary divisor D = {x=0} (origin end of the
    66	strip), y0 a simple root of A (binomial locus: y0 = -1/a2, the unique point
    67	of {P=0} n D). Q = x^k C + x^{k+1} E + ... with C the solved col k. Claim:
    68	  Res2 := Res_x Res_y [ dP ^ dQ / (x^{k+2} A^{k+2}) ]  (iterated at (0,y0))
    69	       ?= (k+2) (-1)^k a2^{-2d2-1} R_{k,d2},
    70	INDEPENDENT of E and of deeper columns of P and Q (their contributions are
    71	exact forms / wrong x-order). Refutation control (a2-variant): the naive
    72	  dP ^ dQ / P^{k+2}
    73	should give iterated residue == 0 identically (omega = d(-(1/(k+1))
    74	P^{-(k+1)} dQ) is exact), i.e. pure P,Q-power denominators canNOT see R;
    75	the toric factor x^{k+2} (boundary divisor) and edge polynomial A are
    76	essential. TEST: T3a (identity Jac(P,x^k C) = x^k + x^{k+1} G), T3b
    77	(E-part (AE'-(k+1)A'E)/A^{k+2} = (E/A^{k+1})' has residue 0), T3c
    78	(P^{k+2}-variant total residue == 0).
    79	VERDICT: VERIFIED (T3a,b,c OK on all 11 cells). (a1) holds: R is the
    80	iterated Grothendieck residue of dP ^ dQ at the boundary point
    81	p* = {P=0} n {x=0}, against the pair (x^{k+2}, A^{k+2}); by T3b it is
    82	independent of Q col k+1 (any E: exact form) and of deeper columns of
    83	both polynomials (wrong x-order) — so the FULL pair (P,Q), any strip
    84	lengths, can be used in the numerator. The naive dP^dQ/P^{k+2} is
    85	REFUTED exactly as predicted: its total residue is 0 identically
    86	(the form is d(-(1/(k+1)) P^{-(k+1)} dQ)); pure powers of P,Q cannot
    87	carry R — the toric boundary factor x^{k+2} is what breaks exactness.
    88	
    89	## 3. Interpretation (b): constant-term / CT extraction identity
    90	CANDIDATE (b1, 1-variable residue; the core formula). With G := 2BC'-kB'C
    91	= (Jac(P, x^k C) - x^k)/x^{k+1} (Jacobian connection):
    92	  Res_{y=y0} [ G(y) / A(y)^{k+2} ] dy  ?=  (k+2)(-1)^k a2^{-2d2-1} R_{k,d2}.
    93	Equivalently CT form: R ≐ [w^{k+1}] beta'(w) = coefficient extraction in
    94	w = A(y) (shifted variable), beta = B as function of w.
    95	CANDIDATE (b2, residue theorem / CT at infinity): the only poles of
    96	G A^{-(k+2)} dy on P^1 are y0 and infinity, so
    97	  Res_{y0} = -Res_{infty}:  R ≐ -(coeff of y^{-1} of the Laurent expansion
    98	of G A^{-(k+2)} at infinity) — a CT identity in the pair data alone.
    99	TEST: T1 (exact, cells (2,2),(2,3),(2,4),(3,3),(4,3),(3,4),(5,3)); T2.
   100	VERDICT: VERIFIED (T1, T2 OK on all 11 cells, with the max(k+2,d2)
   101	lower-limit correction of §1 at (2,5)). Exact identity, every cell:
   102	  Res_{y=-1/a2}[(2BC'-kB'C)/A^{k+2}] dy = (k+2)(-1)^k a2^{-2d2-1} R_{k,d2},
   103	and Res_{y0} = -Res_infty (residue theorem on P^1; the CT-at-infinity
   104	path is an independent binomial-series computation). The obstruction
   105	dichotomy k+1 <= 2d2-1 (paper1 §6) is the degree count for the pole of
   106	beta' w^{-(k+2)} at w = infty. Jacobian connection: G is literally
   107	(Jac(P, x^k C) - x^k)/x^{k+1} (T3a), so R ≐ residue of the Jacobian
   108	defect against A^{k+2} — the classical Jacobian-as-residue, localized
   109	at the strip's boundary root.
   110	
   111	## 4. Interpretation (c): Koszul / syzygy obstruction
   112	CANDIDATE (c1). L := A d/dy - (k+1)A' = ad-operator E -> [xA, x^{k+1}E]
   113	/ x^{k+1} on column spaces (source: E-support y^{d2+1}..y^{(k+1)d2};
   114	target: eq window). The moment functional mu(y^n) := Res_{y0}[y^n A^{-(k+2)}
   115	dy] = (-1)^{n-k-1} C(n,k+1) a2^{-(n+1)} satisfies mu o L = 0 (row identity
   116	m C(m-1,k+1) = (m-k-1) C(m,k+1)) — mu spans the G-reachable part of
   117	coker(L)^*, and the obstruction system on the binomial locus is EQUIVALENT
   118	to mu(G) = 0. TEST: T4 (mu.L == 0 as exact matrix identity; coker rank;
   119	second cokernel functional unreachable by G via degree count).
   120	VERDICT: VERIFIED (T4 OK on all 11 cells; a2 specialized to 3/7 and 5/3
   121	for the exact rank computations, mu o L = 0 checked as the integer
   122	identity m C(m-1,k+1) = (m-k-1) C(m,k+1), all m in the window — hand-
   123	provable, so this step is a general theorem, not per-cell). Findings:
   124	L is injective; coker on the window is 2-dimensional, spanned by mu and
   125	one functional supported in degrees > deg G (invisible to every
   126	inhomogeneity); so the block obstruction on the binomial locus is
   127	EXACTLY mu(G) = 0, one residue condition. This is the precise syzygy
   128	statement: R generates the annihilator of im(ad_{xA}) restricted to the
   129	reachable window — a cokernel-of-Koszul-differential interpretation
   130	with ad_{xA}(x^{k+1}E) = [xA, x^{k+1}E] the (1-variable shadow of the)
   131	Koszul/Lie differential of the near-origin block.
   132	
   133	## 4b. DERIVED (paper calc, to machine-verify): uniform outer theorem
   134	Chain S1-S5 (see §5) predicts, for ALL k,d2 >= 2 on the binomial locus:
   135	extras t>=1 == 0 by pure degree count (deg G = 2d2+k-1 < (k+1)d2 + 1);
   136	surviving extra_0 = a2 (k+1)(d2-1) e_top; and applying mu to the solved
   137	system: extra_0 = mu(G)/mu(n0), n0 = (k+1)d2, giving CLOSED FORM
   138	  extra_0 = (-1)^{k+(k+1)(d2-1)} * (k+2)/C((k+1)d2, k+1) * a2^{(k-1)d2} * R.
   139	Checks against ALL repo units: 1/5 (2,2) [C(6,3)=20, 4/20], 1/21 (2,3)
   140	[4/84], 1/55 (2,4) [4/220], 1/99 (3,3) [5/495], 2/1001 (4,3) [6/3003],
   141	1/364 (3,4) [5/1820]; signs all match (-1)^{k+(k+1)(d2-1)}. The mystery
   142	denominators are C((k+1)d2, k+1): binomial from the moment mu(n0).
   143	VERDICT: VERIFIED — T5 OK on all 11 cells (including the 4 new ones).
   144	Proof chain, each step GENERAL (not per-cell):
   145	 S1 deg G <= 2d2+k-1 < (k+1)d2, since (k-1)(d2-1) > 0  [degree count]
   146	 S2 hence extras t>=1 see neither G nor E: identically 0
   147	 S3 extra_0 = G_{n0} + a2(k+1)(d2-1) e_top = a2(k+1)(d2-1) e_top
   148	 S4 apply mu to the solved system: mu(L E_solved) = 0 (interp (c)),
   149	    equations < n0 hold, so extra_0 * mu(n0) = mu(G)
   150	 S5 mu(G) = (k+2)(-1)^k a2^{-2d2-1} R  [interp (b), Step-3 integrand:
   151	    exact part 2 beta w^{-3} - beta' w^{-2} contributes 0, residue term
   152	    beta'_{k+1} = (k+2) beta_{k+2}, beta_{k+2} = (-1)^k a2^{-2d2} R]
   153	Every step is either a two-line general argument (S1-S4, S5's beta
   154	expansion) or the verified exactness lemma; so this is a UNIFORM
   155	THEOREM for all k >= 2, d2 >= 2 at depth 2, machine-verified at 11
   156	cells. It upgrades paper1 conj:R's outer half from per-cell certificate
   157	to closed form, explains all unit factors, and yields NEW exact outer
   158	certificates at the open cells (4,4), (5,4), (2,5), (3,5).
   159	
   160	## 5. Coordinate-free conjecture (and what it would prove)
   161	STATEMENT (coordinate-free residue form of the obstruction). Let (P,Q)
   162	be a reduced strip pair of type (k,d2) satisfying (i), gap-killed, with
   163	x | P; let D = {x=0} be the toric boundary divisor at the origin end,
   164	A := (P/x)|_D the edge polynomial of P on D. On the rigidity locus
   165	(deg A <= 1, i.e. {P=0} meets D in at most one point p*, transversally):
   166	the depth-2 near-origin block is solvable iff
   167	    Res2_{p*} [ dP ^ dQ / (x^{k+2} A^{k+2}) ] = 0,
   168	where Res2 is the iterated (Grothendieck) residue at p*, Q may be taken
   169	with FULL support (independence of col k+1 and deeper columns: §2), and
   170	the value equals (k+2)(-1)^k a2^{-2d2-1} R_{k,d2}. If A has no root on D
   171	(a2 = 0), there is no residue and no obstruction — matching the {a2=0}
   172	branch of conj:R. Conjecture conj:R thus REDUCES to its rigidity half:
   173	"the inner column forces deg A <= 1". Residue reformulation of that
   174	half too: (I) solvable in C with val >= 1 iff all local residues of
   175	dy/A^{k+1} at roots of A vanish AND the valuation normalization holds;
   176	perfect powers A = (1+uy)^delta pass the residue test (single pole,
   177	sum-of-residues) but fail the valuation — explaining exactly why the
   178	repo's divisibility argument must carry both halves (squarefreeness +
   179	divisibility). Not closed here; honest status: open as before.
   180	BEYOND THE GRID. Proved uniformly by §4b: the outer half at ALL
   181	(k,d2), k,d2 >= 2, depth 2 — no more per-cell certificates; empty-sum
   182	rule k+2 > 2d2 <=> no obstruction (k>=3,d2=2 theorem is its shadow).
   183	NOT removed: the strip hypothesis (column/window structure and gap-kill
   184	are load-bearing in S1-S4), the gap condition (ii), the rigidity half,
   185	and depth >= 3. PREDICTION for depth D >= 3: the D-th column's operator
   186	is ad_{xA} at weight k+D with cokernel functional Res[ . A^{-(k+D+1)} dy],
   187	so each deeper column should contribute one residue functional
   188	R^{(D)} ≐ Res_{p*}[dP ^ dQ / (x^{k+D+1} A^{k+D+1})] — consistent with
   189	SURPLUS.md's observed "one torus-solvable leftover per deeper column";
   190	untested here, proposed as the next check.
   191	
   192	## 6. Verdict
   193	REAL STRUCTURE, not coincidental shape. Three mutually consistent
   194	formalizations all verify exactly on 11 cells (7 repo + 4 new):
   195	(b) R ≐ Res_{y0}[(Jac(P,x^kC)-x^k)/(x^{k+1} A^{k+2})]dy, with CT/
   196	    at-infinity form via the residue theorem — the alternating-binomial
   197	    shape IS the residue expansion (w-1)^j |-> (-1)^{j-k-2} C(j,k+2);
   198	(a) equivalently an iterated Grothendieck residue of dP ^ dQ at the
   199	    point where {P=0} meets the toric boundary {x=0}, twisted by the
   200	    boundary equation — and provably NOT expressible with pure P,Q
   201	    powers (dP^dQ/P^{k+2} is exact: residue 0);
   202	(c) equivalently the generator of the cokernel pairing of ad_{xA} on
   203	    the block window (syzygy/Koszul reading), which is what makes the
   204	    elimination collapse to ONE functional.
   205	The payoff is not just interpretation: the S1-S5 chain turns the
   206	per-cell "outer identity" into a uniform closed-form theorem
   207	  extra_0 = (-1)^{k+(k+1)(d2-1)} (k+2)/C((k+1)d2,k+1) a2^{(k-1)d2} R_{k,d2}
   208	for all k,d2 >= 2, explaining every unit factor in SURPLUS-EXT §1.3 and
   209	extending exact outer certificates to (4,4),(5,4),(2,5),(3,5). Limits,
   210	honestly: rigidity half of conj:R still open (residue view reformulates
   211	but does not close it); strip + gap hypotheses still required; depth
   212	>= 3 untouched (prediction stated in §5). One repo correction: R's sum
   213	starts at j = max(k+2, d2), visible first at (2,5).
   214	
   215	## 7. Files
   216	- cases/residue_check.py — all tests, exact arithmetic (exit 0 = OK).
   217	- RESIDUE.md (this file).

exec
/bin/zsh -lc "nl -ba LEMMA.md | sed -n '1,227p'" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
     1	# The −1 lemma for open_8_28_c2 chartG
     2	
     3	Discharges the AUDIT.md claim-7 / notes.md TODO: identify equation #3,
     4	reconstruct its substitution chain, interpret it, attempt a generalization.
     5	System: `SystemA("open_8_28_c2", cornersP, cornersQ, x², nonvanish="nonorigin",
     6	fix_ones=[("P",(8,16)),("Q",(12,24))])`; `Cascade3(level_dir=(2,1))`; then
     7	`two_chart`. Re-runnable analysis: cases/eq3_anatomy.py, cases/eq3_chain.py
     8	(the latter replays the full pipeline with per-equation provenance tracking
     9	and reproduces the AUDIT claim-7 census **symbolically**, not just at points).
    10	
    11	## 1. Which bracket coefficient equation #3 is
    12	
    13	Equations are the coefficients of [P,Q] − x², ordered by sorted bracket
    14	support; the support begins (verified):
    15	
    16	    index:   0      1      2      3      4    ...      (92 keys total)
    17	    key  : (1,0)  (1,1)  (1,2)  (2,0)  (2,1) ...
    18	
    19	**Equation #3 is the coefficient of the right-hand-side monomial x² itself**
    20	(key (2,0)). Since coeff_{(i,j)}[P,Q] = Σ_{p+q=(i+1,j+1)} det(p,q)·a_p·b_q,
    21	eq #3 lives at Minkowski point (3,1). Geometry (P = hull{(0,0),(1,0),(8,14),
    22	(8,16)}, Q = hull{(0,0),(2,1),(12,21),(12,24)}):
    23	
    24	- Both polygons are narrow strips along the direction d = (1,2). With
    25	  w := 2i−j: P occupies w ∈ {0,1,2} (w=0 top edge (0,0)–(8,16), w=2 bottom
    26	  edge (1,0)–(8,14)); Q occupies w ∈ {0,1,2,3} (w=0 top edge (0,0)–(12,24),
    27	  w=3 bottom edge (2,1)–(12,21)). Both top edges lie on lines through the
    28	  origin, so the extreme stratum w_key = −1 of the bracket vanishes
    29	  identically (det of proportional points).
    30	- N(P)+N(Q) = hull{(0,0),(1,0),(3,1),(20,35),(20,40)}. **(3,1) is a vertex**
    31	  — the lower endpoint of the long Minkowski edge (3,1)→(20,35) of direction
    32	  (1,2) (17 primitive steps = the concatenation of the two parallel bottom
    33	  edges: 7 steps from P, 10 from Q).
    34	- (3,1) has the **unique decomposition** (1,0)+(2,1) = (bottom corner of P) +
    35	  (bottom corner of Q), with det((1,0),(2,1)) = 1. Both are saturated
    36	  corners: a1 := coeff_P(1,0), b3 := coeff_Q(2,1) are unit variables.
    37	
    38	Hence
    39	
    40	    eq #3  =  a1·b3 − 1        (two terms; the −1 is the rhs −x²)
    41	
    42	i.e. eq #3 is the **vertex normalization**: x² must be attained at the bottom
    43	vertex of the parallel-edge tower, forcing a1·b3 = 1 (both bottom corners
    44	nonzero, product 1). In the w-grading, x² has w = 4 = w_max(P)+w_max(Q)−1:
    45	it is reachable only by bottom-edge × bottom-edge pairs, and at the vertex
    46	only by the corner pair.
    47	
    48	## 2. The substitution chain
    49	
    50	Structural fact: eq #3 contains only unit variables (a1, b3), so Cascade3
    51	never substitutes into it and never pops it — **eq #3 passes through the
    52	entire cascade verbatim**. The whole collapse is carried by ONE other
    53	equation. Verified chain (cases/eq3_chain.py output):
    54	
    55	1. **Immediate M2 zeroing (before any elimination).** The sub-vertex keys
    56	   (1,0), (1,1) (Minkowski column 2, strictly between the y-axis and the
    57	   vertex column) read a1·b1 = 0 and 2·a1·b2 = 0 with a1 a unit
    58	   ⇒ **b1 = coeff_Q(1,1) := 0, b2 = coeff_Q(1,2) := 0** — Q's entire column
    59	   x=1 (the "gap column" wedged between origin and Q's bottom corner (2,1))
    60	   is annihilated. Key (1,2) then vanishes identically.
    61	2. **Level-(2,1) cascade, 41 unit-pivot eliminations,** consuming Q's columns
    62	   from x=12 down to x=2 (all non-corner b's). Every pivot coefficient is a
    63	   unit corner coefficient times a nonzero lattice determinant: the far
    64	   eliminations pivot on the top corners P(8,16)=1 / P(8,14) (source keys
    65	   (15..19,·)); the rest pivot on a1 via the equation at Minkowski point
    66	   (1,0)+q (source key q−(0,1)), pivot constant det((1,0),q) ≠ 0.
    67	   Three M2 zeroings interleave; the relevant one: key (2,4) reduces to
    68	   (unit)·a3 ⇒ **a3 = coeff_P(1,2) := 0** (P's top-edge point in column 1).
    69	3. **The culprit equation: original key (3,6)** (Minkowski point (4,7) =
    70	   (1,1)+3·(1,2), on the second-highest stratum w_key = 0; column = vertex
    71	   column + 1). Originally
    72	   3a2·b10 − a3·b9 + 2a5·b6 − 2a6·b5 + a8·b2 − 3a9·b1, it is touched by
    73	   exactly 10 events — zero(b1), zero(b2), elim b10(3,6), b9(3,5), b8(3,4),
    74	   b7(3,3) [Q column 3, sources keys (3,2)..(3,5)], elim b6(2,4), b5(2,3),
    75	   b4(2,2) [Q column 2, sources keys (2,1)..(2,3)], zero(a3) — after which it
    76	   is the single monomial
    77	
    78	        (−1/5)·a2²·a6·ia1²·b3  = 0        (a2 = P(1,1), a6 = P(2,4))
    79	
    80	   All eliminated b's were expressed back in P-data; the surviving factor is
    81	   b3 times the non-unit a-monomial a2²a6.
    82	4. **two_chart.** For b3 this equation is the best pivot (|coeff|=1,
    83	   |rest|=0): on the generic chart the coefficient is inverted and
    84	   **b3 := 0**. (The b43-inversion is vacuous — its pivot is the adjoined
    85	   b43·ib43 = 1.) Substituting b3 = 0 into the untouched vertex equation:
    86	
    87	        eq #3  =  a1·0 − 1  =  **−1**.
    88	
    89	   The −1 is literally the transcription of −x²; no other arithmetic touches
    90	   it. Full symbolic census after cascade+chart: 51/92 originals ≡ 0, 40
    91	   remain polynomial, and **eq #3 is the unique constant** — the exact
    92	   symbolic upgrade of AUDIT claim 7's 6-point numeric audit.
    93	
    94	Equivalent ideal statement (chart-free): the derivation shows
    95	**unit·a2²·a6·b3 ∈ I(core)**; since the vertex equation makes b3 a unit,
    96	a2²·a6 ∈ I(core) — the core variety lies in {a2=0} ∪ {a6=0}, which is
    97	precisely the cCa2/cCa6 complement split, and the generic chart (a2, a6
    98	inverted) is empty. Denominator hygiene: the chain's pivot constants are
    99	{−8,−6,−4,−2,2,3,…,16,18,20,22} (lattice determinants det(corner, q)); the
   100	final coefficient only carries 1/5 — so the derivation is valid over any
   101	field in which the pivot constants are invertible: all char-0 fields, and
   102	all F_p with p ∉ {2,3,5,7,11,13} (conservative superset of the primes
   103	dividing any pivot constant).
   104	
   105	## 3. Valuation interpretation
   106	
   107	The level function ℓ = 2i+j orders lattice points along the strips; the
   108	cascade is exactly the classical tower argument "Q is determined by P":
   109	solving the bracket coefficients from the top of the filtration downward
   110	expresses each Q-coefficient at level ℓ through P-data, pivoting on the two
   111	invertible corner coefficients (the fixed top corners, then the bottom
   112	corner a1). The GGV-style reading of the collapse:
   113	
   114	- The vertex equation at the Minkowski vertex p₀+q₀ = (1,0)+(2,1) is the
   115	  **corner normalization**: for [P,Q] = x², the valuation of x² selects the
   116	  bottom vertex of the (1,2)-tower, forcing a_{p₀} b_{q₀} = 1, in particular
   117	  b_{q₀} ≠ 0.
   118	- Because Q's bottom corner q₀ = (2,1) does not lie in the first support
   119	  column, there are bracket coefficients **below/left of the vertex**
   120	  (Minkowski column 2 = keys (1,·)) which must vanish but involve only
   121	  a1·(Q-gap column); invertibility of a1 kills the gap column b1, b2.
   122	- With the gap dead, the near-origin block of tower relations becomes
   123	  **overdetermined by one**: the block keys (2,0)..(2,4), (3,2)..(3,6) are
   124	  the vertex equation plus 9 tower relations for 8 eliminable unknowns
   125	  (b4..b10 and a3); the surplus relation — the
   126	  top-stratum key (3,6), the "would-be tower relation" that in a consistent
   127	  tower would define the next Q-coefficient — has no free Q-coefficient left
   128	  to define. Back-substitution turns it into (unit)·a2²·a6·b_{q₀} = 0: the
   129	  tower forces the bottom corner of Q to vanish, **inconsistent with the
   130	  corner normalization**. So yes: eq #3's collapse is a recognizable
   131	  principle — a corner/tower inconsistency at the parallel-edge direction,
   132	  localized entirely in the O(1) neighbourhood of the origin end of the
   133	  strips.
   134	
   135	## 4. Candidate general lemma, and the regression test
   136	
   137	**Candidate Lemma (vertex–gap obstruction).** Let (P,Q) be a reduced pair
   138	with [P,Q] = x^k, N(P) and N(Q) lattice strips of widths ≤ w_P, w_Q along a
   139	common primitive direction d, top edges through the origin parallel to d,
   140	bottom edges E_P from p₀, E_Q from q₀ (corners saturated). Assume:
   141	
   142	  (i) *(vertex normalization)* x^k sits at the Minkowski vertex p₀+q₀ with
   143	      unique decomposition p₀+q₀ and det(p₀,q₀) = ±1, giving the vertex
   144	      equation a_{p₀} b_{q₀} = ±1;
   145	  (ii) *(gap condition)* N(Q) has support columns strictly between the
   146	      y-axis and x = (q₀)_x — equivalently (q₀)_x ≥ 2 — so the bracket has
   147	      sub-vertex coefficients, and each such coefficient is a1-times-linear
   148	      in the gap column (automatic when (p₀)_x = 1), forcing the gap
   149	      column to vanish;
   150	  (iii) *(surplus condition)* after the gap dies, the level-ordered
   151	      elimination of the near-origin block (Q-columns (q₀)_x … (q₀)_x+1,
   152	      P-columns 1 … 2) has one more vanishing bracket coefficient than
   153	      eliminable unknowns; the surplus is the block's top-stratum key
   154	      (here Minkowski point (1,1)+3d) and its back-substituted form is
   155	      (unit)·(a-monomial)·b_{q₀}.
   156	
   157	Then the bracket coefficient **at the rhs monomial itself** (position rule:
   158	the key x^k, i.e. the Minkowski vertex p₀+q₀) reduces on the chart where the
   159	surplus a-monomial is inverted to the nonzero constant −1, hence the generic
   160	stratum is empty, and the whole variety lies in the vanishing locus of the
   161	surplus a-monomial's non-unit support.
   162	
   163	**Test against the solved family reg_9_24_c3** (P = hull{(0,0),(1,1),(6,16),
   164	(6,18)}, Q = hull{(0,0),(1,0),(9,24),(9,27)}, [P,Q] = x; strips along
   165	d = (1,3); verified by cases/eq3_chain.py reg_9_24_c3):
   166	
   167	- (i) HOLDS there too: x sits at the Minkowski vertex (2,1) = (1,1)+(1,0),
   168	  unique decomposition, det = −1; the vertex equation −a1·b1 − 1 = 0 is
   169	  equation index **0**. So (i) alone does not discriminate.
   170	- (ii) **FAILS**: Q's bottom corner is q₀ = (1,0), (q₀)_x = 1 — there is no
   171	  gap column and no sub-vertex bracket coefficient (the support starts AT
   172	  the vertex key). Nothing forces near-origin Q-coefficients to vanish.
   173	- (iii) fails with it: the near-origin block is exactly balanced /
   174	  underdetermined — the cascade leaves b2 = coeff_Q(1,1) completely free
   175	  (it drops out of every equation), no surplus relation pins b1, and in
   176	  two_chart the vertex equation itself is consumed as the *definition*
   177	  b1 := −1/a1 (chart pivot source = key (1,0), |rest|=1). Symbolic census:
   178	  38/69 equations ≡ 0, **no equation reduces to a constant** — matching the
   179	  known fact that this chartG needed genuine F4 work.
   180	
   181	**Verdict: the candidate lemma DISCRIMINATES the two families**, and the
   182	discriminating hypothesis is sharp in the computed pair: open_8_28_c2 has
   183	(q₀)_x = 2 (gap column {(1,1),(1,2)} killed ⇒ overdetermination ⇒ b3 pinned
   184	to 0 against the vertex normalization), while reg_9_24_c3 has (q₀)_x = 1
   185	(no gap ⇒ vertex equation is a definition, not a constraint).
   186	
   187	## 5. Honest assessment
   188	
   189	- What is proved here (re-runnably): for open_8_28_c2, −1 ∈ ideal(chartG)
   190	  via an explicit 10-event linear substitution chain, entirely inside the
   191	  near-origin columns; equivalently a2²a6 ∈ I(core). This upgrades AUDIT
   192	  claim 7 from numerically-audited to symbolically re-derived
   193	  (cases/eq3_chain.py is the committed audit script the TODO asked for).
   194	- The candidate lemma's conditions (i)+(ii) are cheap, purely polygonal,
   195	  and discriminate the two families examined. Condition (iii) is NOT yet a
   196	  polygonal criterion: it is verified by running the elimination, not read
   197	  off the corners. The counting that produces "surplus = 1" here uses the
   198	  specific strip widths (3 and 4), (p₀)_x = 1, and (q₀)_x = 2; a
   199	  paper-grade lemma would need to derive (iii) from these data (plausible —
   200	  the block is O(1)-sized and explicit — but not done here).
   201	- Generality is untested beyond the two families. For open_8_28_c1
   202	  (pentagon polygons): condition (i) and the nonempty gap column hold
   203	  verbatim (same bottom corners p₀=(1,0), q₀=(2,1), same vertex (3,1) with
   204	  unique decomposition), but the y-axis support ((0,1)..(0,8) in P,
   205	  (0,1)..(0,12) in Q) breaks the *mechanism* of (ii): the sub-vertex
   206	  coefficients (1,j) also contain det((0,a),(2,b)) = −2a terms mixing
   207	  P-column-0 with Q-column-2, so the gap column is not forced to zero by
   208	  M2 alone, and whether an analogous collapse occurs is open (the c1
   209	  analysis run — `python3 cases/eq3_chain.py open_8_28_c1`, long-running —
   210	  was stopped after ~15 min without completing its cascade; consistent
   211	  with notes.md on c1's two_chart swell).
   212	- Sign/index caveat: "equation #3" is ordering-dependent bookkeeping; the
   213	  invariant statement is "the bracket coefficient at the rhs monomial /
   214	  Minkowski vertex p₀+q₀". In reg_9_24_c3 the same coefficient is index 0.
   215	
   216	## Post-review corrections (2026-08-03, per LEMMA-REVIEW.md)
   217	- Erratum §2: the M2 zeroings interleave as 2 before / 1 after the
   218	  eliminations (not "three interleave").
   219	- §4 sharpness CORRECTED: condition (ii) must be symmetrized —
   220	  max((p0)_x, (q0)_x) ≥ 2. The review showed (a) under (i), k=1 forces
   221	  (q0)_x = 1, so the k-vs-gap confound is intrinsic (untestable cell), and
   222	  (b) the swapped-polygon family (k=2, gap on the P side) ALSO collapses
   223	  to −1 — the obstruction is side-symmetric.
   224	- Localization confirmed: a short-strip toy family reproduces the identical
   225	  10-event collapse, supporting an O(1)-block derivation of condition (iii).
   226	- Status: §§1–3 paper-ready per review; remaining for paper grade:
   227	  symmetric-(ii) restatement + surplus-condition derivation from polygon data.

codex
The standalone degree argument is internally very short and currently looks sound; the only plausible failure surface is whether the repo’s “inner extras” are exactly the omitted coefficients of that ODE. I’m now tracing the raw block equations and normalization back through the support/index conventions rather than accepting the prior review’s summary.
exec
/bin/zsh -lc "rg -n \"Prop A|Prop B|inner extras|col_series|wide_W1|gap.kill|block|a1|c1|AC'|C'|Minkowski column|column k\" SURPLUS.md SURPLUS-EXT.md cases/*.py paper1/main.tex" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
cases/bench_fastcoef.py:4:  <case>    reg_9_24_c3 | open_8_28_c2 | open_8_28_c1 | moh_48_64
cases/export_lean.py:6:(-1/5)*a2^2*a6*ia1^2*b3 modulo the unit relations iv*v = 1.
cases/export_lean.py:68:print("final == (-1/5)*a2^2*a6*ia1^2*b3  OK")
cases/export_lean.py:113:# whether or not the reduction consumed them (ia1 backs the cascade pivots,
cases/export_lean.py:115:va1 = S.varof[("P", (1, 0))]
cases/export_lean.py:118:                    {(min(v, C.invof[v]), max(v, C.invof[v])) for v in (va1, vb43)})
cases/export_lean.py:123:    return vn[i]                      # a1, b3, ia1, ... already good Lean ids
cases/export_lean.py:176:w("`eq #3 = a1*b3 - 1` evaluates at `b3 = 0` to the unit `-1`.")
cases/export_lean.py:178:w("theorem eq3_at_b3_zero {K : Type*} [CommRing K] (a1 b3 : K) (h : b3 = 0) :")
cases/export_lean.py:179:w("    a1*b3 - 1 = -1 := by subst h; ring")
cases/export_lean.py:185:w("single monomial `(-1/5)*a2^2*a6*ia1^2*b3` in the localized ring of the")
cases/export_lean.py:186:w("generic chart: `hu1`/`hu2` are the adjoined unit relations `ia1*a1 = 1`,")
cases/export_lean.py:188:w("in fact consume `hu1`/`hu2` — `a1` and `b43` never occur in the chain, so")
cases/export_lean.py:191:w("`Q[a,b][ia1,ib43]/(ia1*a1-1, ib43*b43-1)` of LEMMA.md.  Stated over a")
cases/dc2_deg3.py:76:    """Global unknown list: w-block (all slots, quad), then v-block (slots, cubic)."""
cases/dc2_deg3.py:382:            blocks = set()
cases/dc2_deg3.py:384:                blocks.add(("w" if a < nW else "v") + ("w" if b < nW else "v"))
cases/dc2_deg3.py:385:            place.setdefault(st, set()).update(blocks)
cases/dc2_deg3.py:402:        assert not any(row[:40]), "deg-2 lambda touches w-block?!"
cases/dc2_deg3.py:544:    w0 = grad_vec(cdict, vs, vidx)          # w-block filled, v-block zero
cases/dc2_deg3.py:763:        for (a1, b1), c1 in p.items():
cases/dc2_deg3.py:765:                key = (a1 + a2, b1 + b2)
cases/dc2_deg3.py:766:                out[key] = out.get(key, 0) + c1 * c2
cases/dc2_deg3.py:781:    # s3(E^dual) = c1^3 - 2 c1 c2 + c3 in Chern classes of E
cases/l1_ode_check.py:19:       p = pt(t) = (t-a1)(t-a2),  q = eta * pt(t) * s(t), deg s = l,
cases/l1_ode_check.py:21:  B. merged nu=1, l extra simple q-roots: p = (e-a1)(e-a2), q = p*s:
cases/l1_ode_check.py:86:    a11, a12, c1 = Ep[2] - E00[2], Eb[2] - E00[2], E00[2]
cases/l1_ode_check.py:88:    det = a11 * a22 - a12 * a21
cases/l1_ode_check.py:90:    pi = (-c1 * a22 + c2 * a12) / det
cases/l1_ode_check.py:91:    b  = (-a11 * c2 + a21 * c1) / det
cases/l1_ode_check.py:435:        a11, a12, c1 = Ep[2] - E00[2], Eb[2] - E00[2], E00[2]
cases/l1_ode_check.py:437:        det = a11 * a22 - a12 * a21
cases/l1_ode_check.py:440:        pi = (-c1 * a22 + c2 * a12) / det
cases/l1_ode_check.py:441:        b = (-a11 * c2 + a21 * c1) / det
SURPLUS.md:14:Near-origin block := bracket keys in Minkowski columns k+1, k+2. Post-gap-kill
SURPLUS.md:18:- n_keys: lattice count of block Minkowski points with >=1 live det!=0 pair,
SURPLUS.md:21:- n_unknowns: ground truth from a tiny in-block symbolic cascade (M2 single-
SURPLUS.md:23:  non-unit block coefficients zeroed or expressed. Gap-column variables excluded
SURPLUS.md:32:FINAL (depth-2 block = Minkowski cols k+1, k+2; run `python3
SURPLUS.md:54:  block), so the effective surplus (number of obstruction leftovers) is 0,
SURPLUS.md:58:  outer extra key (5,9) reduces IDENTICALLY to 0. Deeper blocks (D=3..5) add
SURPLUS.md:101:b_{(g,y)} = 0 (M2). No block key is consumed. QED
SURPLUS.md:103:BLOCK. Minkowski columns k+1, k+2. Post-gap-kill the only live pairs landing
SURPLUS.md:106:only there. The block is therefore SELF-CONTAINED: its equations involve
SURPLUS.md:107:exactly the block variables, so counting can be done locally (this is the
SURPLUS.md:134:m = p0 + q; this consumes exactly the block keys of strata w in
SURPLUS.md:149:w in [1, w_P-1] of the two block columns. QED
SURPLUS.md:164:q0 = (2,1)), strips of ANY lengths containing the block columns. Then
SURPLUS.md:170:Proof: explicit reduction of the 9 block keys (labels a1* = a(1,0),
SURPLUS.md:175:    (3,2)  2a1b4 - a2b3            => b4  = a2b3/(2a1)
SURPLUS.md:176:    (3,3)  3a1b5 - 3a3b3           => b5  = a3b3/a1
SURPLUS.md:177:    (3,4)  4a1b6 + a2b5 - 2a3b4    => b6  = -(a2a3-a2a3)b3/(4a1^2) = 0   [C1]
SURPLUS.md:178:    (3,5)* 2a2b6 - a3b5            => -a3^2 b3/a1 = 0  => M2: a3 := 0
SURPLUS.md:179:    (4,3)  3a1b7 - 2a4b3           => b7  = 2a4b3/(3a1)
SURPLUS.md:180:    (4,4)  4a1b8 - 4a5b3           => b8  = a5b3/a1
SURPLUS.md:181:    (4,5)  5a1b9 + a2b8 - 3a3b7 + 2a4b5 - 2a5b4 - 6a6b3
SURPLUS.md:182:                                   => b9  = 6a6b3/(5a1)                  [C2]
SURPLUS.md:183:    (4,6)  6a1b10 + 2a2b9 - 2a3b8 + 4a4b6 - 4a6b4
SURPLUS.md:184:                                   => b10 = -a2a6b3/(15a1^2)
SURPLUS.md:186:                                   => -(1/5) a2^2 a6 b3 a1^{-2}   SURPLUS
SURPLUS.md:189:substituting b5 = a3b3/a1 and b4 = a2b3/(2a1) into a2b5 - 2a3b4 gives
SURPLUS.md:190:a2a3b3/a1 - a2a3b3/a1 = 0, killing b6; in (4,5), a2b8 = a2a5b3/a1 and
SURPLUS.md:191:-2a5b4 = -a2a5b3/a1 cancel (after a3 = 0), leaving b9 proportional to a6
SURPLUS.md:197:{2,3,4,3,4,5,6} and the final 1/5: primes {2,3,5} ONLY - a block-local
SURPLUS.md:204:Chart-free restatement: unit * a2^2 a6 * b_{q0} lies in the block ideal +
SURPLUS.md:205:gap-kill ideal; with the vertex equation (b_{q0} a unit), a2^2 a6 lies in the
SURPLUS.md:211:The surplus key is the topmost non-identically-vanishing key of the block's
SURPLUS.md:213:N(P)+N(Q)) in Minkowski column (p0+q0)_x + 1. Coordinates:
SURPLUS.md:224:Scope map (cases/surplus_count.py scan; depth-2 block, generic lengths;
SURPLUS.md:245:2. d2 = 1 (w_P = 1): no extra keys at all; block exactly balanced; no
SURPLUS.md:248:   -a3^k b_{q0} a1^{1-k}, verified exactly k <= 5), but the outer extra
SURPLUS.md:258:5. Out of scope entirely: d1 >= 2 (sparse columns), y-axis support (the c1
SURPLUS.md:259:   regime, where gap-kill itself fails), strips shorter than the block.
SURPLUS.md:282:  -a3^k b q0 a1^{1-k} verified k <= 5); exact (non-numeric) torus verdicts
SURPLUS-EXT.md:12:- Depth-2 block = Minkowski cols k+1, k+2; live pairs P cols {1,2} x Q cols
SURPLUS-EXT.md:13:  {k,k+1}; self-contained. n_keys = 2(w_P+w_Q)-1 (Prop A); 2w_Q+1 unit-pivot
SURPLUS-EXT.md:14:  eliminations (Prop B); 2(w_P-1) extra keys, strata w in [1, w_P-1].
SURPLUS-EXT.md:19:  Post-gap-kill, bracket Minkowski column k+1 as a poly in y is
SURPLUS-EXT.md:20:  A C' - k A' C, column k+2 is A E' - (k+1) A' E + 2 B C' - k B' C;
SURPLUS-EXT.md:26:  w_P>=3 and other unresolved cells; OUT-OF-SCOPE = y-axis support (c1
SURPLUS-EXT.md:27:  shape, gap-kill fails) or d1>=2; UNKNOWN = reduction data unavailable.
SURPLUS-EXT.md:38:scope map). Machine layer: cases/surplus_ext.py wide_setup/wide_W0/wide_W1
SURPLUS-EXT.md:40:cross-checked against an independent lattice-det enumeration of every block
SURPLUS-EXT.md:44:Coordinates (units a1 = a_p0, c1 = b_q0 scaled to 1): A = 1 + a2 y + a3 y^2
SURPLUS-EXT.md:46:points (2,3)..(2,6)). Q cols 2,3 are eliminated (Prop B, 2w_Q+1 = 11 pivots).
SURPLUS-EXT.md:49:Leftover positions (Prop B strata w in [1,2] of both block columns):
SURPLUS-EXT.md:51:A C' - 2 A' C; outer pair L3 = (4,10) [w=2], L4 = (4,11) [w=1] — coeffs of
SURPLUS-EXT.md:52:y^9, y^10 in A E' - 3 A' E + 2 B C' - 2 B' C. Exact reduced forms:
SURPLUS-EXT.md:65:    series continuation ctilde_7, ctilde_8 of C = a1 c1 A^2 int_0^y A^-3
SURPLUS-EXT.md:66:    (L1 = -7 a1 ctilde_7; L2 = -(8 a1 ctilde_8 + 5 a2 ctilde_7)), so
SURPLUS-EXT.md:69:    the E-series with inhomogeneity G = 2 B C' - 2 B' C.
SURPLUS-EXT.md:75:THEOREM (surplus-4 variant, inner part; (k,d2) = (2,3), depth-2 block, any
SURPLUS-EXT.md:78:to the binomial a1 + a2 y (support = p0 and (1,1)). Consequently the FULL
SURPLUS-EXT.md:79:4-leftover system has NO common zero with all block coordinates nonzero
SURPLUS-EXT.md:95:Extras vanish iff the polynomial identity  C'A - 2A'C = a1 c1  holds exactly
SURPLUS-EXT.md:98:constant: so A is SQUAREFREE, and at simple roots -2A'(r)C(r) = a1 c1 gives
SURPLUS-EXT.md:100:evaluating at r: C'(r) = -2A''C/A', then -C'A'' - 2A'''C - 2A''C' = 0
SURPLUS-EXT.md:115:phaseC2b, W4, exit 0). On the forced locus a3 = a4 = 0 (A = a1 + a2 y):
SURPLUS-EXT.md:120:with z = 1 + a2 y/a1, beta(z) = B(y(z)), the only singular integrand term
SURPLUS-EXT.md:122:-(c1/a2) beta'_3 z^3 log z. Both outer extras are forced multiples of the
SURPLUS-EXT.md:143:Leftover COUNT: 2(w_P - 1) exactly, all cells (Prop B; z = 0 since no M2
SURPLUS-EXT.md:148:V(inner extras I1,I2,I3) = {a3 = a4 = a5 = 0}: P col 1 is again forced to
SURPLUS-EXT.md:149:the binomial a1 + a2 y, so torus-emptiness PERSISTS at w_P = 4, exactly.
SURPLUS-EXT.md:157:extras vanish iff C'A - 2A'C = a1 c1 exactly => A squarefree and
SURPLUS-EXT.md:214:in a2..a6, units a1 = c1 = 1 scaled out; run 2026-08-04, exit 0):
SURPLUS-EXT.md:217:  reduces to exactly -a3^k (i.e. -a3^k b_q0 a1^{1-k} with units restored).
SURPLUS-EXT.md:221:  b10 = -a2 a6 b3/(15 a1^2) and surplus -(1/5) a2^2 a6 b_q0 a_p0^{-2}.
SURPLUS-EXT.md:226:precise statement). Write the block in the column-ODE form of §0 with
SURPLUS-EXT.md:227:d2 = 2: A = a1 + a2 y + a3 y^2, B = a4 y^2 + a5 y^3 + a6 y^4,
SURPLUS-EXT.md:229:    (I)  A C' - k A' C = a1 c1        (col k+1; vertex eq = y^0 coeff)
SURPLUS-EXT.md:230:    (II) A E' - (k+1) A' E = -(2 B C' - k B' C) =: -G   (col k+2)
SURPLUS-EXT.md:232:C = A^k (kappa + a1 c1 int_0^y A^-(k+1)); val >= 1 forces kappa = 0 and the
SURPLUS-EXT.md:234:equals -(2k+1) a1 ctilde_{2k+1} (the would-be next series coefficient).
SURPLUS-EXT.md:235:Closed form ctilde_{2k+1} = a3^k c1 / ((2k+1) a1^k): VERIFIED k <= 10 (V2),
SURPLUS-EXT.md:239:Step 2 (a3 = 0 collapses (I) to a binomial). With a3 = 0, A = a1 + a2 y and
SURPLUS-EXT.md:241:    C = (a1 c1/(k a2)) [ (1 + a2 y/a1)^k - 1 ]   (deg k <= 2k: fits N(Q)).
SURPLUS-EXT.md:242:(a2 = 0 too: C = c1 y, same conclusion.)  So all col-(k+1) keys hold.
SURPLUS-EXT.md:244:z := 1 + a2 y/a1 (so A = a1 z, y = (a1/a2)(z-1)) and set beta(z) := B(y(z)),
SURPLUS-EXT.md:245:a polynomial of z-degree 4 with beta(1) = B(0) = 0. Then C' = c1 z^{k-1},
SURPLUS-EXT.md:246:G = c1 [2 beta z^{k-1} - beta'(z)(z^k - 1)], and the unique val>=3 solution
SURPLUS-EXT.md:248:  E = -(c1/a2) z^{k+1} int_1^z [ 2 beta w^-3 - beta' w^-2 + beta' w^-(k+2) ] dw.
SURPLUS-EXT.md:254:  E = (c1/a2) [ beta(z) z^{k-1} - sum_m beta'_m (z^m - z^{k+1})/(m-k-1) ],
SURPLUS-EXT.md:256:column k+1, its val >= 3 is forced by the ODE (G has val 2), and EVERY key
SURPLUS-EXT.md:257:of column k+2 — including both extras — holds identically. QED (k >= 3).
SURPLUS-EXT.md:260:beta'_3 = 4 a6 (a1/a2)^4. The log tail z^{k+1} log z contributes to y^6 the
SURPLUS-EXT.md:261:coefficient -(c1/a2) 4 a6 (a1/a2)^4 (a2/a1)^6 [t^6](1+t)^3 log(1+t) =
SURPLUS-EXT.md:262:-(c1/a2) 4 a6 (a2^2/a1^2)(1/60) = -a2 a6 c1/(15 a1^2) = b10, and the outer
SURPLUS-EXT.md:263:extra -(1/5) a2^2 a6 c1 a1^-2 — the (2,2) surplus monomial. So the entire
SURPLUS-EXT.md:267:Char caveat: the derivation divides by s*a1 (s <= 2k+3), k, (m-k-1), a2;
SURPLUS-EXT.md:269:directly: A = a1 gives E = -int G/a1, polynomial of deg 5 <= 2k+2. All of
SURPLUS-EXT.md:274:THEOREM (no near-origin obstruction, k >= 3, d2 = 2, depth-2 block; char 0
SURPLUS-EXT.md:276:allowed), arbitrary unit values a1 = a_p0, c1 = b_q0, the assignment
SURPLUS-EXT.md:277:a3 := 0, C := (a1 c1/(k a2))[(1 + a2 y/a1)^k - 1], E := the Step-3 closed
SURPLUS-EXT.md:278:form, satisfies EVERY key of the depth-2 block. Consequences:
SURPLUS-EXT.md:279:(1) The block variety maps onto the whole a3 = 0 slice of P-coefficient
SURPLUS-EXT.md:291:    Sharp form "inner extra = -a3^k b_q0 a1^{1-k}" (hence the locus is
SURPLUS-EXT.md:321:impossible for subcases keeping that corner (c1/pentagon regime). Widths in
SURPLUS-EXT.md:322:the strip shape: w_P = d2, w_Q = k*d2-1 (SURPLUS Prop A scope).
SURPLUS-EXT.md:339:| (8,28) A1=(11/4,7) | (3,2) 108 | 2 | 2 | REDUCED: c1 pentagon, c2 strip |
SURPLUS-EXT.md:355:reg_9_27, reg_9_24_c1, reg_9_24_c2, open_8_28_c1: pentagons (y-axis
SURPLUS-EXT.md:356:support) -> OUT-OF-SCOPE shape (gap-kill fails; SURPLUS note 5).
SURPLUS-EXT.md:363:  subcase c2 is the proved (2,2) theorem; its sibling subcase c1 is
cases/book_enum.py:24:  C' chain layer   -> w0_of: w0 = a(b(alpha+beta)-1)/(b*nu); w_closure: resonant
cases/book_enum.py:62:(residue-A configuration, a1/a2 = 2+-sqrt(3)), R empty (w = 2 >= 1).
cases/book_enum.py:126:# ------------------------------------------------------ C'. w-arithmetic
cases/book_enum.py:196:# --------------------------------------------------- C'. cascade closure
cases/book_enum.py:210:    """M=1-emitting merge of the given branch alphabets: child w's (C' (ii))."""
cases/book_enum.py:247:        for blocks in block_partitions(ws):
cases/book_enum.py:248:            kids |= merge_cascade_ws([branch_alph(b) for b in blocks])
cases/book_enum.py:267:def block_partitions(ws):
cases/book_enum.py:268:    """Partitions of the w0 multiset into >= 2 blocks, deduped by signature."""
cases/book_enum.py:273:        blocks = tuple(sorted(tuple(sorted(ws[i] for i in blk)) for blk in part))
cases/book_enum.py:274:        if blocks not in seen:
cases/book_enum.py:275:            seen.add(blocks)
cases/book_enum.py:276:            out.append(blocks)
cases/book_enum.py:358:        for blocks in block_partitions(ws):
cases/book_enum.py:359:            balphs = [branch_alph(b) for b in blocks]
cases/emit.py:23:    "reg_9_24_c1": dict(
cases/emit.py:41:    "open_8_28_c1": dict(
cases/emit.py:75:    "reg_9_24_c1": [("P", (6, 18)), ("Q", (9, 27))],
cases/emit.py:79:    "open_8_28_c1": [("P", (8, 16)), ("Q", (12, 24))],
cases/r1_12_sat.py:12:    h1+ = s1 (f+)^2, so p_h1,Gm = s1*S_M^2*P^4 (P = (e3-a1)(e3-a2),
cases/r1_12_sat.py:15:    and lam_i = 9 S_M c_i^4 (a1-a2)^2 (TEMPLATE 2c-E5, f-side, branch-
cases/r1_12_sat.py:17:        -(3/4)*729*S_M^3*c_i^12*(a1-a2)^6*w_i^4
cases/r1_12_sat.py:18:            = s1*S_M^2*(3 c_i^2)^4*(a1-a2)^4
cases/r1_12_sat.py:19:        <=>  w_i^4 = -(4/27)*s1 / (S_M*c_i^4*(a1-a2)^2)
cases/r1_12_sat.py:21:             c_i^4 = a_i alpha_i, (a1-a2)^2 = 12, S_M = 7^12/2^6).
cases/r1_12_sat.py:71:    a1, a2, b = R1.A1c, R1.A2c, R1.Bc
cases/r1_12_sat.py:73:    da2 = (a1 - a2) * (a1 - a2)
cases/r1_12_sat.py:76:    bmin = (mk(9) + mk(5) * s3) * (a1 - b) / (a1 * a1) + \
cases/r1_12_sat.py:80:    b12 = (mk(9) + mk(5) * s3) / a1 + (mk(9) - mk(5) * s3) / a2
cases/r1_chain_sat.py:20:(a1-a2)^2, m_i^2 = s0 lam_i^3 -- ring constants already inside the
cases/r1_chain_sat.py:77:    a1, a2, b = R1.A1c, R1.A2c, R1.Bc
cases/r1_chain_sat.py:81:    assert ((a1 - a2) * (a1 - a2) - mk(12)).iszero()
cases/r1_chain_sat.py:82:    assert not (b - a1).iszero() and not (b - a2).iszero()
cases/r1_chain_sat.py:83:    # E6-analogue f-transport: lam_i = 9 S_M c_i^4 (a1-a2)^2 with
cases/r1_chain_sat.py:86:    for ai in (a1, a2):
cases/r1_chain_sat.py:92:        "(a1-a2)^2 unit, m_i^2 = s0 lam_i^3 solvable in K3; pole "
cases/r1_chain_sat.py:156:    a1, a2 = R1.A1c, R1.A2c
cases/r1_chain_sat.py:158:    P2 = [a1 * a2, -(a1 + a2), R1.K1]
cases/r1_chain_sat.py:165:    tq = _pmul(_pmul(_tpow([-a1, R1.K1], 5), _tpow([-a2, R1.K1], 5)),
cases/r1_chain_sat.py:237:    st = FC.load("blocks.pkl")
cases/hiii_compose.py:252:        print(f"[{name}] {'SANC' if sanct else 'ext '} iv_hits={len(seen_h)} "
cases/dc2_slice.py:26:# monomial key (a1,a2,b1,b2)  =  x1^a1 x2^a2 d1^b1 d2^b2  (normal order)
cases/dc2_slice.py:39:    for (a1, a2, b1, b2), ca in A.items():
cases/dc2_slice.py:40:        for (c1, c2, d1, d2), cb in B.items():
cases/dc2_slice.py:41:            for s1 in range(min(b1, c1) + 1):
cases/dc2_slice.py:43:                    co = ca * cb * comb(b1, s1) * comb(c1, s1) * factorial(s1) \
cases/dc2_slice.py:45:                    k = (a1 + c1 - s1, a2 + c2 - s2, b1 + d1 - s1, b2 + d2 - s2)
cases/dc2_slice.py:65:    for (a1, a2, b1, b2), c in A.items():
cases/dc2_slice.py:67:        for g, e in zip(img, (a1, a2, b1, b2)):
cases/depth_closure_check.py:272:    c1 = Wr <= Wc
cases/depth_closure_check.py:281:    all_ok &= c1 and c2 and c3 and c4
cases/depth_closure_check.py:283:                 len(jumps(cum[8])), c1 and c2 and c3 and c4))
cases/r1_q0_gate.py:2:quotient sub-block of the minimal-branch F_s ladder (SHEET6-R1.md sec
cases/r1_q0_gate.py:136:    """suborbit-Newton fold, mod-p port of R1.fs_block: e_syms of the
cases/r1_q0_gate.py:288:    # ---- anchor A1b: exact-ring fs_block reference through slot 40
cases/r1_q0_gate.py:296:        ex = R1.fs_block(orbs84[on], 41)
cases/r1_q0_gate.py:319:        log("  anchor A1b %s: specialized fold == exact-ring fs_block "
cases/r1_q0_gate.py:537:      4*(a_i-b)*HM + 729*S_M^3*(a1-a2)^4*a_i^2*alpha_i*W_i^4 = 0
cases/r1_q0_gate.py:747:            r = R1.rmono(za=rk[1], a1=rk[2], a2=rk[3], w1=rk[4],
cases/r1_q0_gate.py:812:        folds[on] = R1.fs_block(spec[on], SCAP)
cases/r1_q0_gate.py:882:    for i, (ai2, arg) in enumerate(((R1.A1c * R1.A1c, dict(a1=1, w1=4)),
cases/r1_12_decompose.py:28:TMP = "/tmp/r1dec12"
cases/r1_decompose.py:622:    for (cr3, ca1, ca2, cw1, cw2, cf) in (
cases/r1_decompose.py:627:            cr3, ca1, ca2, cw1, cw2
cases/r1_decompose.py:638:    # intended locus: w_i^4 = k_i alpha_i^2 => E -> C*[(9+5s)(a1-4)/a1^2
cases/r1_decompose.py:646:    a1, a2 = (Fr(3), Fr(1)), (Fr(3), Fr(-1))
cases/r1_decompose.py:647:    T1 = mul(mul((Fr(9), Fr(5)), (a1[0] - 4, a1[1])), inv(mul(a1, a1)))
cases/r1_q2_screen.py:314:                raise SizingAbort("block %s: %d terms > budget %d"
cases/r1_q2_screen.py:557:        c1 = (9 + 5 * r3) % p * pt["A1"] % p
cases/r1_q2_screen.py:560:            "%d*W1^4+%d*W2^4" % (c1, c2))
cases/r1_q2_screen.py:777:            r = R1.rmono(za=rk[1], a1=rk[2], a2=rk[3], w1=rk[4],
cases/r1_q2_screen.py:821:        folds[on] = R1.fs_block(spec[on], SCAP)
cases/r1_q2_screen.py:908:    for i, (ai2, arg) in enumerate(((R1.A1c * R1.A1c, dict(a1=1, w1=4)),
cases/r1_experiment.py:6:h1 = g^2 - f^3; A = 1, eta_A = 1; sigma = 6 => a1 = 3+sqrt3, a2 = 3-sqrt3,
cases/r1_experiment.py:87:# monomial key (za, ea1, ea2, ew1, ehw1, ew2, ehw2, eB):
cases/r1_experiment.py:132:    za, ea1, ea2, ew1, eh1, ew2, eh2, eB = key
cases/r1_experiment.py:137:    q, ea1 = divmod(ea1, 3)                 # alpha^-1 -> alpha^2/a
cases/r1_experiment.py:151:        out.append(((j, ea1, ea2, ew1, eh1, ew2, eh2, eB), c*zc))
cases/r1_experiment.py:179:def rmono(za=0, a1=0, a2=0, w1=0, h1=0, w2=0, h2=0, B=0, c=K1):
cases/r1_experiment.py:180:    out = {}; racc(out, (za, a1, a2, w1, h1, w2, h2, B), mk(c)); return out
cases/r1_experiment.py:252:    assert rmul(rmono(a1=1), rmul(rmono(a1=1), rmono(a1=1))) == rC(A1c)
cases/r1_experiment.py:257:    x, y, w = rmono(za=5, a1=2), rmono(za=40, a2=1, w1=3), rmono(h1=1, B=6)
cases/r1_experiment.py:379:    a1m, a2m, w1m, w2m = rmono(a1=1), rmono(a2=1), rmono(w1=1), rmono(w2=1)
cases/r1_experiment.py:395:    mkorb("P1", {12: RONE, 32: a1m, 37: w1m}, {**uf, **vf1, **t1}, 42)
cases/r1_experiment.py:398:    mkorb("Gp1", {12: RONE, 32: a1m, 37: hw1m}, {**uf, **vf1, **g1}, 42)
cases/r1_experiment.py:400:    mkorb("G0p1", {12: RONE, 32: a1m}, {**uf, **vf1, **g01}, 21)
cases/r1_experiment.py:643:def fs_block(orb, depth):
cases/r1_experiment.py:662:        jp = jmul(jp, fs_block(orbs[on], depth), depth)
cases/r1_experiment.py:663:        print("      [fs_jet2 %s] block %s done (%d terms, %.1fs)"
cases/r1_experiment.py:908:    pat = eta_poly_ref([(A1c, 2), (A2c, 2)], K1)     # (e3-a1)^2(e3-a2)^2
cases/r1_experiment.py:1055:    gk("G_m f-jet slot-0 = S_M (e3-a1)^2(e3-a2)^2, S_M = 7^12/2^6 (E6)",
cases/r1_experiment.py:1057:    gk("G_m g-jet slot-0 = G_M (e3-a1)^3(e3-a2)^3, G_M = -7^18/2^9 (E6)",
cases/mondello_collapse.py:4:  P = a1 x + a2 x^2 y + a3 x^4 + a4 x^6 y^2
cases/mondello_collapse.py:6:System: [P,Q] = 1 (Keller), corners a1, b0 saturated (vertex eq a1 b0 = 1).
cases/mondello_collapse.py:22:    SUPP_P[(1, 0)] = "a1"
cases/mondello_collapse.py:25:    SUPP_P = {(1, 0): "a1", (2, 1): "a2", (4, 0): "a3", (6, 2): "a4"}
cases/mondello_collapse.py:43:UNITS = {"a1", "b0"}
cases/mondello_collapse.py:48:    """cancel a1*ia1 pairs inside a monomial tuple."""
cases/mondello_collapse.py:50:    while "a1" in mon and "ia1" in mon:
cases/mondello_collapse.py:51:        mon.remove("a1")
cases/mondello_collapse.py:52:        mon.remove("ia1")
cases/mondello_collapse.py:82:# vertex normalization first: key (0,0) is det((1,0),(0,1)) a1 b0 - 1
cases/mondello_collapse.py:85:      "  -> normalization b0 := 1/a1 (det = +1, ODD - survives char 2)")
cases/mondello_collapse.py:86:values["b0"] = {("ia1",): Fraction(1)}   # ia1 = 1/a1, unit
cases/mondello_collapse.py:87:pivots.append(("V", vkey, +1, "b0 := ia1 (vertex normalization)"))
cases/mondello_collapse.py:102:            nonunits = [s for s in mon if s not in UNITS and s != "ia1"
cases/mondello_collapse.py:118:                if s not in UNITS and s != "ia1" and s not in values:
cases/mondello_collapse.py:125:                if all(x in UNITS or x == "ia1" for x in cof):
cases/mondello_collapse.py:127:                    icof = tuple("ia1" if x == "a1" else "a1" if x == "ia1"
cases/mondello_collapse.py:149:allsyms = sorted(set(SUPP_P.values()) | set(SUPP_Q.values()) - {"a1", "b0"})
cases/surplus_count.py:6:near-origin block (Minkowski columns k+1, k+2, after the gap columns are
cases/surplus_count.py:9:  n_keys      forced-vanishing bracket keys in the block (vertex key (k+1,1)
cases/surplus_count.py:11:  n_unknowns  eliminable coefficients = ground truth from an in-block cascade
cases/surplus_count.py:14:              are excluded by construction (they die below the block)
cases/surplus_count.py:21:are treated as units per hypothesis (i).  Exact Fraction arithmetic; block
cases/surplus_count.py:81:            f"{tag}: y-axis support (breaks gap-kill; c1 regime)"
cases/surplus_count.py:106:    for m1, c1 in p1.items():
cases/surplus_count.py:108:            padd_into(r, mmul(m1, m2), c1*c2)
cases/surplus_count.py:193:    """depth D block: P cols 1..D, Q cols k..k+D-1, Minkowski cols k+1..k+D.
cases/surplus_count.py:222:    # block equations: live pairs P cols 1..D x Q cols k..k+D-1
cases/surplus_count.py:247:    # ---- in-block cascade ----
cases/surplus_count.py:361:        while pins == 0 and k >= 2 and dep < 5:   # probe deeper blocks
cases/surplus_count.py:378:    p0=(1,0), q0=(k,1), top direction d=(1,d2); depth-2 block."""
cases/r1_minimal_ext.py:143:                ob = R1.fs_block(orbs[on], SCAP)
cases/r1_minimal_ext.py:166:    # independent-path cross-check at cap 7: fs_block (Newton) vs
cases/r1_minimal_ext.py:171:        assert R1.fs_block(orbs[on], 7) == ref, "block!=jet %s" % on
cases/r1_minimal_ext.py:173:    log("cross-check: fs_block == fs_jet == sequential fold at slot "
cases/r1_minimal_ext.py:222:    (ground truth) + blocks.pkl vmeta (name -> vid)."""
cases/r1_minimal_ext.py:223:    vm = FC.load("blocks.pkl")["vmeta"]
cases/r1_minimal_ext.py:306:    # regression gate: core block byte-identical to the banked emission
cases/r1_minimal_ext.py:308:    assert back[:105] == eqs0, "REGRESSION GATE: core block changed"
cases/r1_minimal_ext.py:531:    ob = R1.fs_block(orbs[on], SCAP)   # Newton path (6x the linear fold)
cases/sheet6_campaign.py:125:    families detected from the alpha1=0 congruence structure and slope==|Am| checked;
cases/sheet6_campaign.py:810:                print(f"[td={lam_t} {name}] {'SANC' if sanct else 'ext '} "
cases/sheet6_campaign.py:843:            print(f"[{name}] {'SANC' if sanct else 'ext '} verdict={r['verdict']} "
cases/residue_check.py:29:from surplus_ext import (V, ONE, pscale, padd, col_series, extra_value,
cases/residue_check.py:48:    """Exact solution of AC'-kA'C=1 on the binomial locus:
cases/residue_check.py:88:    Cs = col_series(A0, k + 1, {}, 1, k * d2)
cases/residue_check.py:92:    G = deriv_prod(C, B, 2, -k, None)                   # 2BC' - kB'C
cases/residue_check.py:93:    E = col_series(A0, k + 2, G, d2 + 1, (k + 1) * d2)
cases/residue_check.py:124:    # T3a: AC' - kA'C == 1  (=> Jac(P, x^k C) = x^k + x^(k+1) G exactly,
cases/residue_check.py:241:#   Theorem A: A C' - w A' C = c (const != 0), w >= 1  =>  deg A <= 1.
cases/residue_check.py:242:# M1 rigidity dichotomy: inner extras of cell (k,d2) vanish at numeric A
cases/residue_check.py:253:#    symbolic inner extras vanish identically on the binomial locus; are
cases/residue_check.py:303:    C = col_series(A, k + 1, {}, 1, k * d2)
cases/toy_face_isolation.py:3:P = Z^2 W + Z W^2 + t Z^5,  support S = {a1=(2,1), a2=(1,2), a3=(5,0)}.
cases/toy_face_isolation.py:4:Face for l(a,b)=a+b (c=d=1): F = {a1,a2}, lambda=3, lambda/(c+d)=3/2, B=2.
cases/r1_fullcore.py:12:    validation of the block fast path at full degree.
cases/r1_fullcore.py:15:  --blocks   build exact per-(orbit,k) blocks           -> /tmp/r1full/blocks.pkl
cases/r1_fullcore.py:60:# ---------------------------------------------------------------- blocks
cases/r1_fullcore.py:65:def gm_blocks(orbnames, orbs):
cases/r1_fullcore.py:66:    """exact per-(orbit,k) G_m blocks, mirroring gm_jet2 (through-d0 kept
cases/r1_fullcore.py:67:    as one exact block per A-orbit; Delta suborbit-Newton blocks else)."""
cases/r1_fullcore.py:73:    blocks = []
cases/r1_fullcore.py:89:                blocks.append(((on, "d0"), blk))
cases/r1_fullcore.py:116:            blocks.append(((on, k), blk))
cases/r1_fullcore.py:117:    return blocks
cases/r1_fullcore.py:119:def phase_blocks():
cases/r1_fullcore.py:122:    fb = gm_blocks(R1.FORB, orbs)
cases/r1_fullcore.py:123:    log("f-side blocks: %d (%.1fs)" % (len(fb), time.time() - t0))
cases/r1_fullcore.py:124:    gb = gm_blocks(R1.GORB, orbs)
cases/r1_fullcore.py:125:    log("g-side blocks: %d (%.1fs)" % (len(gb), time.time() - t0))
cases/r1_fullcore.py:130:    save("blocks.pkl", dict(f=fb, g=gb, nvars=len(R1.VARS),
cases/r1_fullcore.py:132:    log("blocks saved (%d vars registered)" % len(R1.VARS))
cases/r1_fullcore.py:183:def spec_blocks(blocks, pt, p):
cases/r1_fullcore.py:185:    for lab, blk in blocks:
cases/r1_fullcore.py:223:def tree_fold(blocks, mul, tag, ckname=None):
cases/r1_fullcore.py:225:    layer = list(blocks); lvl = 0
cases/r1_fullcore.py:298:    evaluated numerically mod p — independent of the block machinery."""
cases/r1_fullcore.py:337:    st = load("blocks.pkl")
cases/r1_fullcore.py:345:            sb = spec_blocks(st[side], pt, p)
cases/r1_fullcore.py:358:    log("CHECK PASS: block fold == direct 126/189-factor product "
cases/r1_fullcore.py:371:    st = load("blocks.pkl")
cases/r1_fullcore.py:376:    fb = spec_blocks(st["f"], pt, p); gb = spec_blocks(st["g"], pt, p)
cases/r1_fullcore.py:453:    st = load("blocks.pkl")
cases/r1_fullcore.py:470:    st = load("blocks.pkl")
cases/r1_fullcore.py:555:def blocks_to_p(blocks, p):
cases/r1_fullcore.py:557:                   for key, vex in blk.items()}) for lab, blk in blocks]
cases/r1_fullcore.py:783:    st = load("blocks.pkl")
cases/r1_fullcore.py:791:        def conv_blocks(blocks):
cases/r1_fullcore.py:795:                    for lab, blk in blocks]
cases/r1_fullcore.py:796:        fb = conv_blocks(st["f"]); gb = conv_blocks(st["g"])
cases/r1_fullcore.py:834:    """pointwise-z per-prime F2 = fold of f-block squares (za-basis out,
cases/r1_fullcore.py:836:    st = load("blocks.pkl")
cases/r1_fullcore.py:872:def fold_seq(blocks, mul, tag):
cases/r1_fullcore.py:874:    partial multiplies one SPARSE low-density block at a time)."""
cases/r1_fullcore.py:875:    acc = blocks[0]
cases/r1_fullcore.py:877:    for i, b in enumerate(blocks[1:], 1):
cases/r1_fullcore.py:879:        if i % 5 == 0 or i == len(blocks) - 1:
cases/r1_fullcore.py:880:            log("%s: %d/%d blocks, %d entries (%.1fs)"
cases/r1_fullcore.py:881:                % (tag, i + 1, len(blocks), jsize(acc), time.time() - t0))
cases/r1_fullcore.py:885:    st = load("blocks.pkl")
cases/r1_fullcore.py:892:        fb = blocks_to_p(st["f"], p); gb = blocks_to_p(st["g"], p)
cases/r1_fullcore.py:912:    st = load("blocks.pkl")
cases/r1_fullcore.py:919:        fb = blocks_to_p(st["f"], p)
cases/r1_fullcore.py:1013:    st = load("blocks.pkl")
cases/r1_fullcore.py:1037:    st = load("blocks.pkl")
cases/r1_fullcore.py:1170:    st = load("blocks.pkl")
cases/r1_fullcore.py:1226:    st = load("blocks.pkl")
cases/r1_fullcore.py:1291:    patterns: p3/p5/p6/p10 = (t-a1)^k(t-a2)^k (t = eta^3, k=3,5,6,10),
cases/r1_fullcore.py:1292:    pq34/pq46 = eta*(t-a1)^m(t-a2)^m*(t-b) (m=5,7) — the level-2
cases/r1_fullcore.py:1314:        a1, a2, b = (3 + pt["r3"]) % p, (3 - pt["r3"]) % p, 4
cases/r1_fullcore.py:1320:            want = (pow(x, eta, p) * pow(t - a1, m, p) * pow(t - a2, m, p)
cases/r1_fullcore.py:1333:    st = load("blocks.pkl")
cases/r1_fullcore.py:1367:    st = load("blocks.pkl")
cases/r1_fullcore.py:1373:        blks = [{k: v for k, v in b.items() if k[1] < dg}  # block^5-first
cases/r1_fullcore.py:1458:    st = load("blocks.pkl")
cases/r1_fullcore.py:1643:    st = load("blocks.pkl")
cases/r1_fullcore.py:1875:    st = load("blocks.pkl")
cases/r1_fullcore.py:1936:    if "--blocks" in args: phase_blocks()
cases/r6_window.py:230:    open cases share it: i=2, p = P = (eta^3-a1)(eta^3-a2), delta = d/i =
cases/r6_window.py:234:      b = (2/3)(a1+a2)  and  a1*a2 = (a1+a2)^2/6,  a1+a2 != 0.
cases/r6_window.py:241:    p2 = p1 * p1 / 6                            # a1a2 = (a1+a2)^2/6
cases/r6_window.py:251:          " b = (2/3)(a1+a2), a1a2 = (a1+a2)^2/6, a1+a2 != 0; deg q = 10."
cases/r6_window.py:255:    W = _pmul(P_t, [-b_pin, Fr(1)])             # (t-a1)(t-a2)(t-b)
cases/r6_window.py:289:        # (C'/D') pole edges, corrected d-arithmetic: d_h2@P = 2/7 = k1/7,
cases/r6_window.py:294:        print(f"    (C'/D') h3@P: h2-side wins (12/7 > {l2}/21), p_h3@P ="
cases/r6_window.py:333:              f" a1a2 = (a1+a2)^2/6, a2/a1 = 2+-sqrt(3)).")
cases/surplus_ext.py:5:of the log-residue mechanism.  Post-gap-kill, Minkowski column k+1 of [P,Q]
cases/surplus_ext.py:6:as a polynomial in y is A C' - k A' C (A = P col 1, C = Q col k) and column
cases/surplus_ext.py:7:k+2 is A E' - (k+1) A' E + 2 B C' - k B' C (B = P col 2, E = Q col k+1);
cases/surplus_ext.py:8:key (X,s) = coeff of y^{s-1}.  The in-block cascade of surplus_count.py is
cases/surplus_ext.py:12:Checks (exact Fraction arithmetic, symbolic in a2,a3,a4,a5,a6; a1=c1=1 wlog
cases/surplus_ext.py:16:  V2  inner extra == -a3^k * c1 * a1^(1-k) for k=2..10  (extends the k<=5
cases/surplus_ext.py:20:      e_top == -(1/15) a2 a6 (matching b10 = -a2 a6 b3/(15 a1^2)).
cases/surplus_ext.py:45:def col_series(Acoef, ncoef, inhom, val, top):
cases/surplus_ext.py:47:    + inhom_n = 0 for n >= 1 (A_0 = 1, a1 scaled out; ncoef = k+1 for the
cases/surplus_ext.py:48:    C-column A C' - k A' C, ncoef = k+2 for the E-column A E' - (k+1) A' E).
cases/surplus_ext.py:98:        C = col_series(A, k + 1, {}, 1, 2 * k)
cases/surplus_ext.py:108:        # G_n = coeffs of 2 B C' - k B' C  (inhom for E-column with + sign)
cases/surplus_ext.py:109:        G = deriv_prod(C0, B, 2, -k, None)               # 2 C'... careful order
cases/surplus_ext.py:110:        # deriv_prod(F,G,cF,cG) = cF F'G + cG F G': want 2 B C' - k B' C =
cases/surplus_ext.py:113:        E = col_series(A0, k + 2, G, 3, 2 * k + 2)
cases/surplus_ext.py:138:    """Column-ODE data, general (k,d2), units a1=c1=1 scaled out.
cases/surplus_ext.py:144:    t = 0..d2-2 (strata w = d2-1-t .. matches Prop B's w in [1, w_P-1])."""
cases/surplus_ext.py:149:    C = col_series(A, k + 1, {}, 1, k * d2)
cases/surplus_ext.py:151:    G = deriv_prod(C, B, 2, -k, None)             # 2 B C' - k B' C
cases/surplus_ext.py:154:    E = col_series(A, k + 2, G, d2 + 1, (k + 1) * d2)
cases/surplus_ext.py:169:def wide_W1(k=2, d2=3):
cases/surplus_ext.py:170:    """Lattice cross-check: enumerate every block key from dets (independent
cases/surplus_ext.py:202:            ok &= (e == {(): Fraction(1)})       # det(p0,q0) a1 c1 = 1
cases/surplus_ext.py:227:    coefficients [c0, c1, ...]."""
cases/surplus_ext.py:330:    print("W5a (2,4) inner extras vanish on {a3=a4=a5=0}:",
cases/surplus_ext.py:457:    ok = wide_W0() and wide_W1(2, 3) and wide_W1(2, 4) and wide_W1(3, 3)
cases/surplus_ext.py:459:    print("(2,3) inner extras (keys (3,7),(3,8)); 10*L:")
cases/surplus_ext.py:471:    print("V2 (inner extra = -a3^k c1 a1^{1-k}, k<=10):", "OK" if v2 else "FAIL")
cases/surplus_ext.py:475:    c1 = phaseC1()
cases/surplus_ext.py:480:    sys.exit(0 if (a and v2 and v3 and v4 and c1 and c2 and c2b and c3 and c3b)
cases/template_lift.py:10:  6. W-collapse: t(t-b)^3 - (t-a1)^2(t-a2)^2 = (sig^3/27)(t - 3sig/4)
cases/template_lift.py:11:     + forcing: t^3,t^2 coefficients vanish IFF b = 2sig/3, a1a2 = sig^2/6
cases/template_lift.py:149:# G_m vertex over Q(sqrt3): a12 = (sig/2)(1 +- 1/sqrt3), b = 2sig/3
cases/template_lift.py:151:a1 = mk(Fr(sig,2)) * (K3(1) + SQ3.inv()); a2 = mk(Fr(sig,2)) * (K3(1) - SQ3.inv())
cases/template_lift.py:153:chk("a1+a2 = sig, a1a2 = sig^2/6, a1/a2 = 2+sqrt3",
cases/template_lift.py:154:    (a1+a2 - sig).iszero() and (a1*a2 - Fr(sig**2,6)).iszero()
cases/template_lift.py:155:    and (a1/a2 - (K3(2)+SQ3)).iszero())
cases/template_lift.py:157:Ppol = pmul(cube(a1), cube(a2))
cases/template_lift.py:224:    """t(t-b)^3 - (t-a1)(t-a2) squared, with a1+a2=ss, a1a2=pp, over K3."""
cases/template_lift.py:229:Wgood = Wpoly(b, a1*a2, mk(sig))
cases/template_lift.py:239:chk("b2 not in {a1,a2,b}, all nonzero",
cases/template_lift.py:240:    not (b2-a1).iszero() and not (b2-a2).iszero() and not (b2-b).iszero())
cases/template_lift.py:296:chk("27 a1 (a1-b)^3 = sig^3 (a1 - 3sig/4) over Q(sqrt3)", Fi(a1).iszero())
cases/template_lift.py:298:chk("both sides = sig^4(2sqrt3-3)/12 at a1",
cases/template_lift.py:299:    (mk(27)*a1*(a1-b)*(a1-b)*(a1-b)
cases/template_lift.py:302:    not (a1-b).iszero() and not (a2-b).iszero())
cases/r1_reduce.py:219:    for (rk1, xk1), c1 in p1.items():
cases/r1_reduce.py:226:            cc = c1 * c2
cases/r1_reduce.py:243:        for rk1, c1 in cur.items():
cases/r1_reduce.py:246:                    nc = nxt.get(nrk, Fr(0)) + c1 * c2 * rc
cases/r1_reduce.py:284:                # u * (-1/a0)*(a1 + a2 u + ... ) = 1
paper1/main.tex:27:Below degree $125$, the reduction program of Guccione, Guccione, Valqui and Horruitiner leaves a single open family of possible counterexample degrees to the plane Jacobian conjecture, $(\deg P,\deg Q)=(108,72)$. One of its two reduced subcases is a pair of parallel Newton-polygon strips with $[P,Q]=x^2$. We develop an obstruction theory for such strip pairs: a vertex normalization at a Minkowski vertex, a gap condition on the bottom corners, and a counting argument on a self-contained near-origin block. At $(k,d_2)=(2,2)$ this empties the generic chart; the $(8,28)$ family is the explicit ten-step case. Our main theorem describes the block at every cell $k,d_2\geq 2$ in characteristic zero: the depth-two block variety is $\{A\ \text{binomial}\}\cap(\{a_2=0\}\cup\{R_{k,d_2}=0\})$, where $A$ is the low $P$-column and $R_{k,d_2}$ is an explicit logarithmic-residue functional whose one-term case is the $(2,2)$ theorem. The rigidity input is an elementary lemma: if $AC'-\nu A'C$ is a nonzero constant, with $A,C$ polynomials and $\nu\geq1$ an integer, then $\deg A\leq 1$. Deeper Minkowski columns, the $k=1$ cells, and non-strip shapes remain open. All claims are machine-verified in exact arithmetic.
paper1/main.tex:38:For reduced strip pairs with $[P,Q]=x^k$ and direction $(1,d_2)$ (Section \ref{sec:setup}), we prove two counting propositions that locate a self-contained near-origin block of bracket equations (Section \ref{sec:gap}); the vertex-gap theorem at $(k,d_2)=(2,2)$, emptying the chart $a_2a_6\neq 0$ by a surplus relation of pinning type in the radical of the block ideal (Section \ref{sec:gap}); variants at $(2,3)$ and $(2,4)$ (support rigidity of a $P$-column plus a residue hyperplane), rigidity certificates at $(3,3)$, $(4,3)$, $(5,3)$, and the absence of any near-origin obstruction for $k\geq 3$ at $d_2=2$ (Section \ref{sec:variants}); and the explicit ten-event collapse for the $(8,28)$ generic chart (Section \ref{sec:example}). Section \ref{sec:functional} proves the main structural result: a logarithmic-residue functional $R_{k,d_2}$, whose one-term case is the $(2,2)$ theorem, describes the depth-two block variety at every cell $k,d_2\geq 2$ in characteristic zero, subsuming and completing the per-cell results of Section \ref{sec:variants}. Section \ref{sec:coverage} records which GGV families the theory covers; Section \ref{sec:computation} describes verification and AI assistance.
paper1/main.tex:99:We now assume (i) and (ii) in the normalized labels: $p_0=(1,0)$, $q_0=(k,1)$, $w_P=d_2$, $w_Q=kd_2-1$, and $a_{p_0}$, $b_{q_0}$ units. The plan: first the gap columns die; then a small block of keys near the origin becomes a self-contained linear system in the nearby coefficients; counting its equations against its unknowns explains, and in favorable cells proves, the collapse.
paper1/main.tex:101:\begin{lemma}[gap kill]\label{lem:gapkill}
paper1/main.tex:112:\noindent\textbf{The near-origin block.} Define the \emph{block} to be the set of keys in Minkowski columns $k+1$ and $k+2$. After the gap kill, a pair $(p,q)$ with $a_pb_q$ alive can land in the block only with $p$ in $P$-column $1$ or $2$ and $q$ in $Q$-column $k$ or $k+1$: the origin pairs have $\det=0$, gap columns are dead, and larger $P$-columns would push $q$ into a dead or negative column. Conversely such pairs land only in the block. So the block is \emph{self-contained}: its equations involve the coefficients in $P$-columns $1,2$ and $Q$-columns $k,k+1$ only, no matter how long the strips are. All counting can be done locally, and the block has fixed size depending only on $(k,d_2)$.
paper1/main.tex:115:For all $k,d_2\geq 1$, the number of forced-to-vanish block keys that are not identically zero is $n_{\mathrm{keys}}=2(w_P+w_Q)-1$.
paper1/main.tex:119:Column $k+1$ of $N(P)+N(Q)$ is the ladder $(k+1,y)$, $1\leq y\leq d_2(k+1)$, i.e.\ strata $w=0,\dots,w_P+w_Q$; the vertex $(k+1,1)$ is the bottom stratum $w=w_P+w_Q$. The stratum $w=0$ is identically zero: $w(p)+w(q)=0$ with both weights $\geq 0$ forces $w(p)=w(q)=0$, so $p,q\in\mathbb{R}d$ and $\det(p,q)=0$. Every stratum $1\leq w\leq w_P+w_Q$ occurs after the gap kill: for $w\geq w_P$ take the pair $(p_0,q)$ with $q$ in the full $Q$-column $k$ at weight $w-w_P$, whose determinant is $q_2\geq 1$; for $1\leq w\leq w_P-1$ take $p=(1,d_2-w)$ in $P$-column $1$ and $q=(k,kd_2)$ the top of $Q$-column $k$, with $\det(p,q)=kw\neq 0$. Distinct pairs give distinct monomials $a_pb_q$, so no cancellation occurs and each such key is a genuine equation. Removing the vertex key leaves $w_P+w_Q-1$ keys. Column $k+2$ is the same ladder argument with bottom point $(k+2,1+d_2)$ on the long Minkowski edge (witnesses: $(p_0,q)$ with $q$ in column $k+1$, and $p=(1,d_2-w)$ against the top of column $k+1$, $\det=(k+1)w$); there is no vertex to remove, giving $w_P+w_Q$ keys. Total $2(w_P+w_Q)-1$.
paper1/main.tex:123:All $2w_Q+1$ non-corner coefficients $b_q$ with $q$ in $Q$-columns $k$ and $k+1$ are eliminable by unit pivots, each from its own key at $m=p_0+q$; this consumes the block keys of strata $w_P\leq w\leq w_P+w_Q$ (vertex excluded). The remaining \emph{extra keys} are the $2(w_P-1)$ keys of strata $1\leq w\leq w_P-1$ in the two block columns.
paper1/main.tex:127:The key at $p_0+q$ contains $\det(p_0,q)\,a_{p_0}b_q=q_2\,a_{p_0}b_q$ with $q_2\geq 1$ and unit cofactor $a_{p_0}$, and this is the only monomial of that key containing $b_q$ (the pair with second factor $q$ is unique). The map $q\mapsto p_0+q$ is injective, hits the strata $w(p_0+q)=w_P+w(q)\in[w_P,w_P+w_Q]$ in each block column, and misses only the vertex ($q=q_0$). Triangularity: in any other monomial $(p',q')$ of the key at $p_0+q$ one has $\ell(p')>\ell(p_0)$ (a point of $P$-column $1$ other than $p_0$ has $\ell=d_2+j>d_2$, and column $2$ has $\ell\geq 2d_2$), hence $\ell(q')<\ell(q)$, so eliminating in increasing level of $q$ is well founded and each substitution inserts only already-expressed or lower-level variables. The counts follow: $2w_Q+1$ keys consumed (a full $Q$-column has $kd_2=w_Q+1$ points, two columns minus the corner), and $n_{\mathrm{keys}}-(2w_Q+1)=2(w_P-1)$ extra keys, namely the strata $1\leq w\leq w_P-1$.
paper1/main.tex:133:Let $(P,Q)$ be a reduced strip pair of type $(2,2)$ satisfying \textup{(i)}, with strips of any lengths containing the block columns, over a field of characteristic not in $\{2,3,5\}$. Write
paper1/main.tex:137:for the block $P$-coefficients ($a_1$ a unit) and $b_3=b_{(2,1)}$ (a unit), $b_4=b_{(2,2)}$, $b_5=b_{(2,3)}$, $b_6=b_{(2,4)}$, $b_7=b_{(3,3)}$, $\dots$, $b_{10}=b_{(3,6)}$ for the block $Q$-coefficients. Then every solution satisfies $a_3=0$ and $a_2^2a_6=0$. Thus the locus $a_2a_6\neq 0$ is empty, and the block variety is contained in $\{a_3=0\}\cap(\{a_2=0\}\cup\{a_6=0\})$.
paper1/main.tex:141:Here $w_P=2$, $w_Q=3$, $p_0=(1,0)$, $q_0=(2,1)$; by Proposition \ref{prop:A} there are $9$ block keys besides the vertex, and by Proposition \ref{prop:B} seven of them eliminate $b_4,\dots,b_{10}$. After the gap kill ($b_{(1,1)}=b_{(1,2)}=0$), the nine keys, in elimination order, reduce as follows (each line lists the Minkowski point, the key, and its consequence after substituting the previous lines):
paper1/main.tex:157:The step $a_3=0$ is extracted from the relation $a_3^2b_3/a_1=0$, which is quadratic in $a_3$. The chart-free form of the conclusion is therefore a \emph{radical} membership: $u:=a_2^2a_6b_{q_0}$ satisfies $u^2\in I$, where $I$ is the ideal generated by the block, gap and vertex equations, but $u\notin I$. A witness over the dual numbers $K[\varepsilon]/(\varepsilon^2)$: set $a_3=\varepsilon$, $a_2=1$, $a_6=\varepsilon c$; all generators of $I$ can be satisfied while $u=\varepsilon c\, b_{q_0}\neq 0$. Every variety-level statement in Theorem \ref{thm:22} is unaffected.
paper1/main.tex:161:In the general labels, the surplus key is the topmost non-vanishing key of the \emph{outer} block column: stratum $w=1$ of Minkowski column $k+2$, i.e.
paper1/main.tex:174:Outside $(2,2)$, by Proposition \ref{prop:B} the block has $2(w_P-1)=2(d_2-1)$ extra keys, so the single-surplus picture is special to $d_2=2$. To compute the extra keys uniformly we assemble each strip column into a generating polynomial. Write
paper1/main.tex:181:for $P$-columns $1,2$ and $Q$-columns $k,k+1$. From $\det((1,i),(k,j))=j-ik$ and $\det((2,i),(k,j))=2j-ik$ one checks directly that the block keys are the coefficients of
paper1/main.tex:183:\text{column } k{+}1:\;\; AC'-kA'C, \qquad
paper1/main.tex:184:\text{column } k{+}2:\;\; AE'-(k{+}1)A'E+2BC'-kB'C,
paper1/main.tex:186:the key at Minkowski point $(k{+}1,s)$ resp.\ $(k{+}2,s)$ being the coefficient of $y^{s-1}$, and the vertex equation the constant term $a_{p_0}b_{q_0}$ of the first expression. This assembly is machine-checked against an independent lattice-determinant enumeration of every block key. Proposition \ref{prop:B} solves the lower coefficients of these two linear ODE-like relations for $C$ and $E$; the extra keys are the would-be next coefficients of the solved series. We normalize the units $a_{p_0}=b_{q_0}=1$ in this section; unit factors are restored routinely.
paper1/main.tex:190:At $(k,d_2)=(2,3)$ we have $A=1+a_2y+a_3y^2+a_4y^3$, $B=\beta_3y^3+\dots+\beta_6y^6$, and there are four extra keys: the inner pair $L_1,L_2$ (Minkowski $(3,7),(3,8)$, the coefficients of $y^6,y^7$ in $AC'-2A'C$) and the outer pair $L_3,L_4$ ($(4,10),(4,11)$). Back-substitution gives the exact forms
paper1/main.tex:206:The inner extras vanish when and only when the column identity $C'A-2A'C=1$ holds as polynomials, with $C$ the solved column of degree $\leq 6$. At a root $r$ of $A$ of multiplicity $\geq2$ the left side is divisible by $y-r$ while the right side is $1$: so $A$ is squarefree, and at each simple root $-2A'(r)C(r)=1$, whence $A'(r),C(r)\neq0$. Differentiating the identity twice and evaluating at $r$ yields $3A''(r)^2=A'(r)A'''(r)$, i.e.\ $A$ divides $N(A):=3A''^2-A'A'''$. If $\deg A=3$ then $N=(12a_3^2-6a_2a_4)+60a_3a_4y+90a_4^2y^2$ has degree $<3$, so divisibility forces $N=0$, but its top coefficient $90a_4^2$ is nonzero. If $\deg A=2$ then $N=12a_3^2$ is a nonzero constant. Hence $\deg A\leq 1$.
paper1/main.tex:209:\begin{theorem}[complete block variety at $(2,3)$]\label{thm:23full}
paper1/main.tex:214:Hence $V(L_1,L_2,L_3,L_4)=\{a_3=a_4=0,\ a_2=0\}\ \cup\ \{a_3=a_4=0,\ R=0\}$, so the block variety contains no point with all block coordinates nonzero. The inner (rigidity) part uses only characteristics outside $\{2,3,5\}$; the outer computation excludes primes in $\{2,3,5,7,11\}$.
paper1/main.tex:221:\begin{theorem}[rigidity and block variety at $(2,4)$]\label{thm:24}
paper1/main.tex:222:Let $(k,d_2)=(2,4)$, $A=1+py+qy^2+ry^3+sy^4$, over characteristic $0$ (the proof excludes only primes in $\{2,3,5,7\}$ for the rigidity part, plus $11$ for the outer part). The three inner extras force $q=r=s=0$, so $A$ is again a binomial; on that locus two of the three outer extras vanish identically and the third equals $-\frac{p^4}{55}R_4$ with
paper1/main.tex:226:Hence $V(\text{all six extras})=\{q=r=s=0,\ p=0\}\cup\{q=r=s=0,\ R_4=0\}$, and again no point has all block coordinates nonzero.
paper1/main.tex:230:As in Theorem \ref{thm:23}, the inner extras vanish iff $C'A-2A'C=1$, forcing $A$ squarefree and $A\mid N(A)=3A''^2-A'A'''$. Compute $N-336sA=E_0+60E_1y+30E_2y^2$ (the top two coefficients cancel), where $E_0=12q^2-6pr-336s$, $E_1=qr-6ps$, $E_2=3r^2-8qs$. If $\deg A=4$ ($s\neq0$), divisibility of the degree-$\leq2$ remainder by $A$ forces $E_0=E_1=E_2=0$; the identities
paper1/main.tex:242:At $(k,d_2)=(3,3),(4,3),(5,3)$ the inner extra keys again force $a_3=a_4=0$ ($A$ binomial); consequently these block varieties contain no point with all block coordinates nonzero. The proof is a machine-verified pair of exact Sylvester resultant computations for each cell: an $a_4$-resultant of two inner extras equal to $c\,a_3^m$ with constant $a_4$-leading coefficient, followed by an $a_2$-resultant on the slice $a_3=0$ equal to $c'a_4^N$; the exponents $(m,N)$ are $(15,12)$, $(26,34)$, $(40,44)$ respectively. The certificates are exact rational arithmetic, locked by executable assertions in the repository (Section \ref{sec:computation}).
paper1/main.tex:259:satisfy every key of the depth-two block. Consequently no extra key of pinning type exists, no chart in the coordinates $(a_2,\beta_2,\beta_3,\beta_4)$ is emptied, and the only near-origin restriction on $P$ is the support condition $a_3=0$.
paper1/main.tex:263:The column-$(k{+}1)$ relation $AC'-kA'C=1$ has the one-dimensional solution family $C=A^k(\kappa+\int_0^yA^{-(k+1)})$, and the valuation $\geq1$ forces $\kappa=0$. The inner extra key is the would-be next series coefficient of this $C$; its vanishing locus contains $\{a_3=0\}$, since with $A=1+a_2y$ the series truncates: $C$ is the stated polynomial of degree $k$, fitting $Q$-column $k$. For column $k+2$, substitute $z=1+a_2y$ and $\beta(z):=B(y(z))$ (a polynomial of $z$-degree $4=2d_2$ with $\beta(1)=0$); the relation $AE'-(k+1)A'E=-(2BC'-kB'C)$ integrates to
paper1/main.tex:270:Limitations. The theorem concerns the depth-two block only: deeper Minkowski columns add one leftover key per column, each a residue-type linear condition on the fresh $P$-column; numerical probes suggest these are satisfiable, but we have not proved it. Also, the sharp form of the inner extra key (reduction to $-a_3^k b_{q_0}a_1^{1-k}$, vanishing locus $\{a_3=0\}$ by radicality) is verified by exact computation for $k\leq10$ but not closed for general $k$; the containment used above is proved for all $k$.
paper1/main.tex:285:The pipeline (Section \ref{sec:computation}) runs a level-ordered elimination: after the gap kill $b_{(1,1)}=b_{(1,2)}=0$, it performs $41$ unit-pivot eliminations expressing the $Q$-coefficients of columns $x=12$ down to $x=2$ in $P$-data, then passes to the generic chart. Equation $\#3$ contains only the units $a_1,b_3$ and is never rewritten. The collapse is carried by the key at Minkowski point $(4,7)$ (artifact key $(3,6)$),
paper1/main.tex:289:Ten recorded events touch it, namely the block-local reduction of Theorem \ref{thm:22} plus the gap kill:
paper1/main.tex:291:\item[1--2.] $b_{(1,1)}:=0$ and $b_{(1,2)}:=0$ (gap kill);
paper1/main.tex:321:Let $F$ have characteristic zero, let $\nu\geq1$ be an integer, and let $A,C\in F[y]$ satisfy $AC'-\nu A'C=c$ for some constant $c\in F$, $c\neq0$. Then $\deg A\leq 1$.
paper1/main.tex:329:\emph{Step 2 (degree of $C$).} If $\deg C\neq\nu\delta$, Step 1 gives $\deg(AC'-\nu A'C)=\delta+\deg C-1\geq\delta-1\geq1$, while $\deg c=0$. Hence $\deg C=\nu\delta$.
paper1/main.tex:338:The bridge to the block is the solved inner column of Proposition \ref{prop:B}; keep $a_{p_0}=b_{q_0}=1$, so $A=1+a_2y+\dots+a_{d_2+1}y^{d_2}$; the extra keys of Minkowski column $k+1$ are the \emph{inner extras}, those of column $k+2$ the \emph{outer extras} ($d_2-1$ of each).
paper1/main.tex:340:\begin{lemma}[block to ODE bridge]\label{lem:bridge}
paper1/main.tex:341:Fix $k,d_2\geq2$ over a field $F$ of characteristic zero and fix a point $a=(a_2,\dots,a_{d_2+1})$. The $d_2-1$ inner extras vanish at $a$ if and only if some $C\in F[y]$ with support in $\{y,\dots,y^{kd_2}\}$ satisfies $AC'-kA'C=1$.
paper1/main.tex:345:By \eqref{eq:odes} the inner-column keys are the coefficients of $AC'-kA'C$, $C=\sum_{j=1}^{kd_2}c_jy^j$: the pair $(a_{(1,i)},c_j)$ contributes $(j-ki)\,a_{(1,i)}c_j\,y^{i+j-1}$. The constant coefficient is $c_1$, set to $1$ by the vertex equation. The top coefficient, of $y^{(k+1)d_2-1}$, is $(kd_2-kd_2)\,a_{(1,d_2)}c_{kd_2}=0$ identically: the $w=0$ stratum of Proposition \ref{prop:A}. The coefficients of $y^1,\dots,y^{kd_2-1}$ determine $c_2,\dots,c_{kd_2}$ triangularly (the pivot of $y^n$ is $n+1\neq0$), and the inner extras are the leftover coefficients of $y^{kd_2},\dots,y^{(k+1)d_2-2}$ of the solved series. If the extras vanish at $a$, the solved $C$ satisfies $AC'-kA'C=1$. Conversely a solution with the stated support is unique: two differ by $K$ with $AK'=kA'K$, i.e.\ $(K/A^k)'=0$ in $F(y)$, so $K=\lambda A^k$, and constant terms ($A^k(0)=1$, $K(0)=0$) force $\lambda=0$. Any solution is thus the solved column, and the extras vanish.
paper1/main.tex:357:Write $L(E):=AE'-(k+1)A'E$ and $G:=2BC'-kB'C$, with $C$, $E$ the solved columns of Proposition \ref{prop:B}. On the binomial locus $\deg C=k$, so $\deg G\leq 2d_2+k-1<(k+1)d_2$ (the difference is $(k-1)(d_2-1)>0$), and $\deg A=1$ gives $\deg(L(E)+G)\leq(k+1)d_2$. The coefficients of $y^{d_2},\dots,y^{(k+1)d_2-1}$ are the consumed keys of Proposition \ref{prop:B}, hence zero, and the valuation is at least $d_2$, so $L(E)+G=e\,y^{(k+1)d_2}$ with $e$ the lowest outer extra; the higher outer extras vanish identically. To evaluate $e$, assume $a_2\neq0$ and pair with $\mu(f):=\operatorname{res}_{y=-1/a_2}\bigl(fA^{-(k+2)}dy\bigr)$, the local residue (not the resultant of Section \ref{sec:variants}). Since $L(E)A^{-(k+2)}=(E/A^{k+1})'$ is exact, $\mu(L(E))=0$ and $e\,\mu(y^{(k+1)d_2})=\mu(G)$. Both sides are elementary in $z=1+a_2y$: $\mu(y^n)=(-1)^{n-k-1}\binom{n}{k+1}a_2^{-(n+1)}$, while $G=2\beta z^{k-1}-\beta'z^k+\beta'$ gives $\mu(G)=a_2^{-1}[z^{k+1}]G=(k+2)\,a_2^{-1}[z^{k+2}]\beta$, and $[z^{k+2}]\beta=\sum_j\beta_ja_2^{-j}\binom{j}{k+2}(-1)^{j-k-2}=(-1)^ka_2^{-2d_2}R_{k,d_2}$. Solving for $e$ gives the display. Both sides are polynomials in $(a_2,\beta_\bullet)$, so the identity extends to $a_2=0$.
paper1/main.tex:360:\begin{theorem}[log-residue description of the block variety]\label{thm:R}
paper1/main.tex:361:For every $k\geq2$, $d_2\geq2$, and every reduced strip pair of type $(k,d_2)$ satisfying \textup{(i)}, over a field of characteristic zero, the variety of the extra keys of the depth-two block is
paper1/main.tex:369:Inner half. If the inner extras vanish, Lemma \ref{lem:bridge} produces a polynomial solution of $AC'-kA'C=1$, and Theorem \ref{thm:ode} with $\nu=k$ forces $\deg A\leq1$: the point is binomial. Conversely on the binomial locus the solution in Remark \ref{rem:sharp} has support in $\{y,\dots,y^k\}$, so the inner extras vanish there. Outer half. On the binomial locus, by Lemma \ref{lem:outer} the outer extras vanish exactly when $a_2^{(k-1)d_2}R_{k,d_2}=0$, i.e.\ when $a_2=0$ or $R_{k,d_2}=0$, since $(k-1)d_2>0$. Intersecting the halves gives the display. When $k+2>2d_2$ the sum defining $R$ is empty, $R\equiv0$, and the statement degenerates to $V(\textup{extras})=\{A\textup{ binomial}\}$ (Theorem \ref{thm:kbig} at $d_2=2$).
paper1/main.tex:372:Theorem \ref{thm:R} settles what Section \ref{sec:variants} left open: no point of the depth-two block has all coordinates nonzero when $k,d_2\geq2$ (the forced $a_{(1,2)}=0$); a pinning-type obstruction only at $(2,2)$, where $R$ is a single monomial; no $b$-side obstruction for $d_2\geq3$ ($R$ is then a multi-term linear form, satisfiable with every coordinate nonzero); no residue condition for $k>2d_2-2$. The rigidity halves of Theorems \ref{thm:23} and \ref{thm:24} and the certificates of Theorem \ref{thm:k3} become corollaries, retained as independent corroboration; the cells $(3,4)$, $(4,4)$, $(5,4)$ and all $d_2\geq5$, out of reach of the divisibility argument, are closed (indeed evaluating $AC'-kA'C=1$ at a multiple root gives $0=1$, so perfect powers die with no squarefreeness lemma).
paper1/main.tex:374:The boundary deserves equal precision. Theorem \ref{thm:R} is a depth-two statement under the strip hypotheses of Definition \ref{def:strip}: Minkowski columns beyond $k+2$ contribute one further residue-type condition each, and their joint behavior remains open. It says nothing at $k=1$ (no gap column, no bridge); nothing for pentagon-shaped or $y$-axis-supported subcases, where the gap kill fails, or for strips of direction $(d_1,d_2)$ with $d_1\geq2$; and it is claimed in characteristic zero only, though the rigidity half holds verbatim for $p>(k+1)d_2$ (a conservative bound on the pivots and weights used).
paper1/main.tex:378:Section 7 of \cite{GGV4} tabulates all $34$ admissible corner families with $\max(\deg P,\deg Q)\leq150$. For each family the type data of a hypothetical strip reduction is pure corner arithmetic: for family corner $A_0=(a,b)$ with $b>a$, the right-hand exponent is $k=\lceil b/a\rceil-2$, and if $b/a$ is not an integer the strip slope is $d_2=a/(\lceil b/a\rceil a-b)$. If $b/a$ is an integer, the $A_0$-corner maps onto the $y$-axis under the reduction, so any subcase keeping that corner has $y$-axis support and is outside Definition \ref{def:strip} (the gap-kill mechanism fails there; see after Lemma \ref{lem:gapkill}). Classifying the $34$ rows:
paper1/main.tex:394:Annotations. The single theorem-covered row is covered only in part: the $(8,28)$ family reduces in \cite{GGHV} to two subcases, and only subcase (2) is strip-shaped; subcase (1) is pentagon-shaped with $y$-axis support, outside the theory, and was handled computationally. For the $19$ rows with $k=1$, the absence of the mechanism is proved (under (i), $k=1$ forces both bottom corners into column $x=1$, so no gap column exists on either side); this does not discard those families, only that this obstruction cannot explain their failure. The $4$ rows with $k\geq3$ all have $b/a$ integral, so if their corners survive reduction the shape is not a strip and the question is moot; if some subcase were strip-shaped, Theorem \ref{thm:R} would cover its depth-two block at every $d_2\geq2$ (with Theorem \ref{thm:kbig} showing that at $d_2=2$ the block imposes nothing beyond support rigidity). Of the $9$ unknown $k=2$ rows, one (the second reduced branch of $(8,28)$ itself) has $d_2=2$ and would land in the proved cell if it strip-reduces; the other eight are $y$-axis flagged.
paper1/main.tex:403:\noindent\textbf{Verification.} Every displayed reduction is checked by re-runnable exact-arithmetic scripts with executable assertions: a full-pipeline replay with per-equation provenance (the ten-event chain of Section \ref{sec:example}), an independent block-local engine that re-derives Propositions \ref{prop:A}, \ref{prop:B} and the reduction tables from corner data alone, and a third layer that solves the column relations \eqref{eq:odes} in exact rational arithmetic, cross-checks them against a lattice-determinant enumeration of every block key, and carries the resultant certificates of Theorems \ref{thm:23}, \ref{thm:24}, \ref{thm:k3}. A further \texttt{mathieu} mode of the residue checker verifies, in exact arithmetic at all computed cells, the identities of Section \ref{sec:functional}: Theorem \ref{thm:ode}'s two computational identities symbolically, the solves of Lemmas \ref{lem:bridge} and \ref{lem:outer}, and the rigidity dichotomy, including every perfect-power instance $(1+uy)^\delta$. Each write-up stage was subjected to adversarial review in a separate session with independently written code. Those reviews confirmed the derivations and produced three corrections incorporated here: the gap condition must be stated side-symmetrically; the chart-free conclusion is radical membership, not ideal membership (Remark \ref{rem:radical}); and numerical probes at $(3,3)$, $(4,3)$, $(5,3)$ had reported solvable systems that are in fact empty (tolerance against multiplicity-three zeros), replaced by the certificates of Theorem \ref{thm:k3}. Numerical verdicts are untrusted throughout; every claim above rests on displayed proofs or exact-arithmetic certificates. Scripts, run logs, review documents, and pinned versions: the archived artifact at \texttt{doi.org/10.5281/zenodo.21894922} (self-contained reproduction bundle: pipeline, certificates, Lean sources, review documents), with the full campaign repository at \texttt{github.com/dcposch/jc72108} (to be made public with this note).

exec
/bin/zsh -lc "nl -ba SURPLUS.md | sed -n '1,170p'; nl -ba SURPLUS-EXT.md | sed -n '1,180p'" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
     1	# SURPLUS: Deriving Condition (iii) — surplus = 1
     2	
     3	## Phase 1: Computational validation
     4	
     5	### Method
     6	
     7	Script: `cases/surplus_count.py` (self-contained; no lib deps). Input: corners of
     8	N(P), N(Q), k. Derived: primitive strip direction d=(1,d2) (top edges through
     9	origin), widths w_P,w_Q, bottom corners p0,q0. Orientation normalized so the gap
    10	side (bottom-corner x = max) is Q; if that requires swapping, noted (bracket sign
    11	irrelevant to counts). Hypothesis (i) verified: p0+q0=(k+1,1), unique lattice
    12	decomposition, |det(p0,q0)|=1.
    13	
    14	Near-origin block := bracket keys in Minkowski columns k+1, k+2. Post-gap-kill
    15	live pairs: P cols {1,2} x Q cols {k, k+1} (gap cols 1..k-1 of Q die first via
    16	triangular a_{p0}-pivots on sub-vertex keys; verified structurally).
    17	
    18	- n_keys: lattice count of block Minkowski points with >=1 live det!=0 pair,
    19	  excluding the vertex key (k+1,1) (= rhs x^k) and identically-zero keys
    20	  (all pairs det=0; includes the top stratum w=0).
    21	- n_unknowns: ground truth from a tiny in-block symbolic cascade (M2 single-
    22	  monomial zeroings + unit-cofactor eliminations, eager substitution): count of
    23	  non-unit block coefficients zeroed or expressed. Gap-column variables excluded
    24	  by construction. Units a_{p0}, b_{q0} invertible per (i).
    25	- surplus := n_keys - n_unknowns = number of leftover equations; each leftover
    26	  is classified: PINS-b_q0 (reduces to unit*(a-monomial)*b_{q0}, the
    27	  obstruction), TRIVIAL (reduces to 0), or OTHER.
    28	- Cross-check column: closed-form candidate n_keys = 2(w_P+w_Q)-1.
    29	
    30	### Validation table
    31	
    32	FINAL (depth-2 block = Minkowski cols k+1, k+2; run `python3
    33	cases/surplus_count.py`). Leftover classes: PINS = reduces to
    34	(unit)*(non-unit monomial)*b_q0 (the obstruction); TRIVIAL = reduces to 0.
    35	
    36	| family       | k | d     | wP | wQ | gap? | n_keys | n_unk | surplus | leftover               | expected | verdict |
    37	|--------------|---|-------|----|----|------|--------|-------|---------|------------------------|----------|---------|
    38	| open_8_28_c2 | 2 | (1,2) | 2  | 3  | yes  | 9      | 8     | 1       | (4,7) PINS -1/5 a2^2a6 | 1        | MATCH   |
    39	| swap_8_28_c2 | 2 | (1,2) | 2  | 3  | yes  | 9      | 8     | 1       | (4,7) PINS (same, normalized) | 1 | MATCH   |
    40	| mini_gap     | 2 | (1,2) | 2  | 3  | yes  | 9      | 8     | 1       | (4,7) PINS (identical) | 1        | MATCH   |
    41	| reg_9_24_c3  | 1 | (1,3) | 2  | 3  | no   | 9      | 8     | 1(raw)  | (3,8) TRIVIAL -> eff. 0| <=0      | MATCH*  |
    42	| toy_k3 (new) | 3 | (1,2) | 2  | 5  | yes  | 13     | 12    | 1(raw)  | (5,9) TRIVIAL -> eff. 0| 1?       | BREAKS  |
    43	| toy_w3 (new) | 2 | (1,3) | 3  | 5  | yes  | 15     | 11    | 4       | 4x OTHER, torus-EMPTY  | 1?       | BREAKS  |
    44	
    45	The three known collapsing families reproduce LEMMA.md exactly: 9 forced keys,
    46	8 eliminable (7 gap-side + 1 P-zeroed a(1,2)), surplus key (4,7), reduced form
    47	(-1/5)*a(1,1)^2*a(2,4)*b_q0*a_p0^-2 — byte-identical incl. the 1/5.
    48	
    49	### Notes per family
    50	
    51	* MATCH* (reg): the raw count n_keys - n_unknowns equals 1 for reg TOO; the
    52	  true discriminator is the leftover's CONTENT: reg's leftover (3,8) reduces
    53	  to 0 (its P-side inputs a(1,2), a(1,3) are themselves M2-zeroed by the
    54	  block), so the effective surplus (number of obstruction leftovers) is 0,
    55	  matching "<= 0 for the solved shape". Condition (iii) must be stated as
    56	  "the leftover reduces to (unit)*M*b_q0 with M nonzero", not as a bare count.
    57	* toy_k3 (k=3, d2=2): gap condition holds, a(1,2) is still M2-forced, but the
    58	  outer extra key (5,9) reduces IDENTICALLY to 0. Deeper blocks (D=3..5) add
    59	  one leftover per column, all torus-SOLVABLE (numeric probe, 80 restarts):
    60	  they merely constrain P; no empty-chart obstruction. Condition (iii) FAILS
    61	  at k=3 even though (i)+(ii) hold: (iii) is genuinely independent.
    62	* toy_w3 (k=2, d2=3, wP=3): no M2 ever fires (extra keys have >=2 monomials);
    63	  2(wP-1)=4 leftovers, a 4-eqs/7-vars system among P-coefficients with NO
    64	  torus point (numeric probe, stable D=2..5): an obstruction plausibly
    65	  persists but NOT in the surplus=1 single-monomial form. wP=2 is load-bearing.
    66	
    67	PHASE 1 DONE. Deliverable: table above + cases/surplus_count.py (self-checked
    68	against LEMMA.md ground truth by assertion).
    69	
    70	### Notes per family
    71	
    72	## Phase 2: General counting argument
    73	
    74	### Setup and symbolic enumeration
    75	
    76	Standing hypotheses (LEMMA.md (i) + review-symmetrized (ii)), after the
    77	normalization (P,Q) -> (Q,-P) if needed so the gap side is Q:
    78	
    79	- strips along primitive d = (1,d2), d2 >= 1 (d1 = 1 assumed; d1 >= 2 gives
    80	  sparse columns and is out of scope), top edges of both polygons on the line
    81	  R*d through the origin; bottom corners saturated;
    82	- (i): x^k at the Minkowski vertex p0+q0 = (k+1,1), unique det!=0
    83	  decomposition, det(p0,q0) = +-1. By the review's enumeration this forces
    84	  {p0,q0} = {(1,0),(k,1)}; normalized: p0 = (1,0), q0 = (k,1);
    85	- (ii): k >= 2 (equivalently max((p0)_x,(q0)_x) >= 2);
    86	- strip lengths: P contains columns 1,2 in full, Q contains columns k,k+1 in
    87	  full (i.e. strips extend at least 2 resp. k+1 columns past the origin).
    88	
    89	Derived data (not free parameters!): w(i,j) := d2*i - j >= 0, zero exactly on
    90	the top edges; w_P = w(p0) = d2, w_Q = w(q0) = k*d2 - 1. Column x = c of P
    91	resp. Q is the full ladder of d2*c+1 resp. lattice points between bottom and
    92	top edge (columns are w-intervals [0,w_side], bijectively y = d2*c - w).
    93	Units: a_{p0}, b_{q0} (vertex equation a_{p0} b_{q0} = +-1, hypothesis (i)).
    94	
    95	GAP-KILL LEMMA. Q's columns 1..k-1 vanish on the variety. Proof: induction on
    96	column g and, inside it, on level l = d2*x+y. The sub-vertex key at Minkowski
    97	point p0 + (g,y) contains det(p0,(g,y))*a_{p0}*b_{(g,y)} = y*a_{p0}*b_{(g,y)}
    98	with y >= 1 (gap points are above the bottom edge 0->q0); its other monomials
    99	pair P col j >= 1 with Q gap points of strictly lower level or lower column,
   100	already zero. So each key reduces to a single monomial with unit cofactor:
   101	b_{(g,y)} = 0 (M2). No block key is consumed. QED
   102	
   103	BLOCK. Minkowski columns k+1, k+2. Post-gap-kill the only live pairs landing
   104	there are P cols {1,2} x Q cols {k,k+1} (anything else hits the origin column,
   105	a gap column, or column sums outside {k+1,k+2}); conversely these pairs land
   106	only there. The block is therefore SELF-CONTAINED: its equations involve
   107	exactly the block variables, so counting can be done locally (this is the
   108	localization the review's mini-family confirmed empirically).
   109	
   110	### Key count
   111	
   112	PROPOSITION A. n_keys = 2(w_P + w_Q) - 1, for every k >= 1, d2 >= 1.
   113	
   114	Proof. Column x = k+1 of N(P)+N(Q) is the ladder y = 1..d2(k+1), i.e. strata
   115	w = 0..w_P+w_Q (w = d2(k+1)-y; vertex (k+1,1) is the bottom stratum
   116	w = w_P+w_Q). (a) A key of stratum w = 0 is identically zero: w(p)+w(q) = 0
   117	with w >= 0 forces w(p) = w(q) = 0, so p,q are both on R*d and det(p,q) = 0.
   118	(b) Every stratum 1 <= w <= w_P+w_Q is genuinely in the post-gap support:
   119	for w >= w_P take the pair (p0, q), q in Q col k with w(q) = w - w_P (the
   120	column is full), det(p0,q) = q_y >= 1; for 1 <= w <= w_P-1 take
   121	p = (1, d2-w) in P col 1 and q = (k, k*d2) the top of Q col k, det = k*w != 0.
   122	Distinct pairs contribute distinct monomials a_p b_q, so no cancellation.
   123	Removing the vertex key leaves (w_P + w_Q) - 1 forced-vanishing keys.
   124	Column x = k+2: same ladder argument (bottom of the column is (k+2, 1+d2) on
   125	the long Minkowski edge, stratum w_P+w_Q; support witness for w >= w_P is
   126	(p0, q), q in Q col k+1 full; for w <= w_P-1 use q = top of col k+1); no
   127	vertex to remove: w_P + w_Q keys. Total 2(w_P+w_Q) - 1. QED
   128	(Verified by the script on all 6 families and the 16-cell scan.)
   129	
   130	### Unknown count
   131	
   132	PROPOSITION B (gap-side eliminations). All 2w_Q + 1 non-corner coefficients
   133	b_q, q in Q cols k, k+1, are unit-pivot eliminable, each from its own key
   134	m = p0 + q; this consumes exactly the block keys of strata w in
   135	[w_P, w_P+w_Q] (both columns, vertex excluded), leaving as remainder the
   136	2(w_P - 1) "extra" keys of strata w in [1, w_P-1].
   137	
   138	Proof. The key at m = p0 + q contains the monomial det(p0,q)*a_{p0}*b_q with
   139	det(p0,q) = q_y >= 1 and unit cofactor a_{p0}; it is the only monomial of that
   140	key containing b_q (the pair with second factor q is unique). q -> p0 + q is
   141	injective, hits exactly strata w(m) = w_P + w(q) in [w_P, w_P+w_Q] in each
   142	column, and misses only the vertex (q = q0). Triangularity: in any other
   143	monomial (p',q') of the key p0+q one has l(p') > l(p0) (l = d2*x+y is
   144	injective... l(p') = d2+j > d2 for p' = (1,j), j>=1, and l >= 2*d2 >= l(p0)+1
   145	for p' in col 2), hence l(q') < l(q): eliminating in increasing level l(q) is
   146	well-founded and each substitution only inserts already-defined or
   147	lower-level variables. Count of consumed keys = count of eliminated b's =
   148	2w_Q + 1; remainder n_keys - (2w_Q+1) = 2(w_P-1) keys, exactly the strata
   149	w in [1, w_P-1] of the two block columns. QED
   150	
   151	COROLLARY (raw count). n_keys - n_unknowns = 2(w_P - 1) - z, where z = number
   152	of P-side coefficients zeroed by M2 events among the extra keys. The
   153	CONTENT of the extra keys after back-substitution decides everything; it is
   154	regime-dependent (Theorem below and scope map).
   155	
   156	### Key count
   157	
   158	### Unknown count
   159	
   160	### Main count: n_keys − n_unknowns = 1
   161	
   162	THEOREM (condition (iii) from polygon data, regime (k,d2) = (2,2)). Let (P,Q)
   163	satisfy the setup with k = 2, d = (1,2) (hence w_P = 2, w_Q = 3, p0 = (1,0),
   164	q0 = (2,1)), strips of ANY lengths containing the block columns. Then
   165	n_keys = 9, n_unknowns = 8, surplus = 1; the surplus key is Minkowski (4,7),
   166	and its back-substituted form is (-1/5)*a2^2*a6*b_{q0}*a_{p0}^{-2}, i.e.
   167	(unit)*(a-monomial)*b_{q0}. With (i) this forces a2^2 a6 = 0: the chart
   168	inverting {a2, a6} is empty. Valid over any field of char not in {2,3,5}.
   169	
   170	Proof: explicit reduction of the 9 block keys (labels a1* = a(1,0),
     1	# SURPLUS-EXT: Extending the vertex-gap theorem beyond (k,d2)=(2,2)
     2	
     3	Status: SKELETON — sections filled incrementally.
     4	
     5	## 0. Setup and conventions
     6	Recap (SURPLUS.md, LEMMA.md); notation fixed for this file:
     7	- Reduced pair: [P,Q] = x^k; N(P), N(Q) strips along primitive d = (1,d2),
     8	  top edges through origin; bottom corners saturated; hypothesis (i) forces
     9	  {p0,q0} = {(1,0),(k,1)}; normalized so gap side is Q: p0=(1,0), q0=(k,1).
    10	  Widths w_P = d2, w_Q = k*d2 - 1. RHS exponent from GGV corner data:
    11	  k = ceil(b/a) - 2 for family corner A0=(a,b), b>a (SECTION4-AUTOMATION §1).
    12	- Depth-2 block = Minkowski cols k+1, k+2; live pairs P cols {1,2} x Q cols
    13	  {k,k+1}; self-contained. n_keys = 2(w_P+w_Q)-1 (Prop A); 2w_Q+1 unit-pivot
    14	  eliminations (Prop B); 2(w_P-1) extra keys, strata w in [1, w_P-1].
    15	- Column-ODE view (new here, used in §§1-2): write P col 1 as A(y) =
    16	  sum_{i=0}^{d2} a_{(1,i)} y^i (a_{(1,0)} = a_{p0} unit), P col 2 as B(y)
    17	  (monomials y^{d2}..y^{2 d2}), Q col k as C(y) (y^1..y^{k d2}, coefficient
    18	  of y^1 = b_{q0} unit), Q col k+1 as E(y) (y^{d2+1}..y^{(k+1) d2}).
    19	  Post-gap-kill, bracket Minkowski column k+1 as a poly in y is
    20	  A C' - k A' C, column k+2 is A E' - (k+1) A' E + 2 B C' - k B' C;
    21	  key (X,s) = coefficient of y^{s-1}. Vertex equation = y^0 coeff of col k+1.
    22	  (To be machine-verified against cases/surplus_count.py by surplus_ext.py.)
    23	- Cell labels used in §3: THEOREM-COVERED = (k,d2)=(2,2) gap regime (proved
    24	  theorem, SURPLUS.md); MECHANISM-ABSENT = k<=0 / k=1 (no gap) / d2=1 (no
    25	  extra keys) / k>=3 verdict cells (see §2); NEEDS-COMPUTATION = wide strips
    26	  w_P>=3 and other unresolved cells; OUT-OF-SCOPE = y-axis support (c1
    27	  shape, gap-kill fails) or d1>=2; UNKNOWN = reduction data unavailable.
    28	  Added in Phase C: SURPLUS-4-COVERED = wide-strip cells whose leftover
    29	  system is exactly solved by the surplus-4 variant theorem (§1): torus-
    30	  empty via forced P-col-1 binomial support (NOT a PINS obstruction);
    31	  currently (2,3), (2,4) full variety + (3,3), (4,3), (5,3) rigidity.
    32	
    33	## 1. Target 1 — Wide strips (w_P = 3): the surplus-4 leftovers
    34	### 1.1 Symbolic characterization of the 4 leftover constraints
    35	
    36	Cell: (k,d2) = (2,3) (w_P = d2 = 3, w_Q = 5; toy_w3's cell; the header's
    37	"w_P = 3" — note w_P = d2 identically, so this is the d2 = 3 column of the
    38	scope map). Machine layer: cases/surplus_ext.py wide_setup/wide_W0/wide_W1
    39	(run 2026-08-05, exit 0): the general-(k,d2) column-ODE solve is
    40	cross-checked against an independent lattice-det enumeration of every block
    41	key — eliminated keys reduce to 0, vertex to +1, and the 4 leftovers equal
    42	the ODE extras EXACTLY (also verified at (2,2) anchor, (2,4), (3,3)).
    43	
    44	Coordinates (units a1 = a_p0, c1 = b_q0 scaled to 1): A = 1 + a2 y + a3 y^2
    45	+ a4 y^3 (P col 1, points (1,0)..(1,3)), B = b3 y^3 + .. + b6 y^6 (P col 2,
    46	points (2,3)..(2,6)). Q cols 2,3 are eliminated (Prop B, 2w_Q+1 = 11 pivots).
    47	NO M2 ever fires (z = 0): the leftover count is exactly 2(w_P-1) = 4.
    48	
    49	Leftover positions (Prop B strata w in [1,2] of both block columns):
    50	inner pair L1 = key (3,7) [w=2], L2 = (3,8) [w=1] — coeffs of y^6, y^7 in
    51	A C' - 2 A' C; outer pair L3 = (4,10) [w=2], L4 = (4,11) [w=1] — coeffs of
    52	y^9, y^10 in A E' - 3 A' E + 2 B C' - 2 B' C. Exact reduced forms:
    53	
    54	    10*L1 =  2 a3^3 - 4 a2^2 a3^2 + 2 a2^3 a4 + 19 a2 a3 a4 - 25 a4^2
    55	    10*L2 = -2 a2 a3^3 + a2^2 a3 a4 + 8 a3^2 a4 + a2 a4^2
    56	    L3, L4: 18 monomials each, LINEAR in (b3..b6), coefficients in
    57	            Q[a2,a3,a4] (not displayed; machine-held, wide_setup(2,3)).
    58	
    59	Structure (generalizing the (2,2) machinery):
    60	(a) B-grading: L1, L2 are B-FREE (pure P-col-1 constraints); L3, L4 are
    61	    linear in B — same split as (2,2)'s inner -a3^2 / outer -(1/5)a2^2 a6.
    62	(b) Weighted homogeneity: deg(a_{i+1}) = deg(B_i) = i gives deg L1..L4 =
    63	    6, 7, 9, 10 (= the y-levels); each key is also w-stratum homogeneous.
    64	(c) ODE meaning: L1, L2 are unit-triangular combinations of the would-be
    65	    series continuation ctilde_7, ctilde_8 of C = a1 c1 A^2 int_0^y A^-3
    66	    (L1 = -7 a1 ctilde_7; L2 = -(8 a1 ctilde_8 + 5 a2 ctilde_7)), so
    67	    ideal(L1,L2) = ideal(ctilde_7, ctilde_8): "P col 1 must make the
    68	    C-series truncate one AND two steps past deg 6". Likewise L3, L4 for
    69	    the E-series with inhomogeneity G = 2 B C' - 2 B' C.
    70	(d) Monomial content of the inner pair: restricted to a2 = 0 or a3 = 0 or
    71	    a4 = 0 the pair stays a genuine 2-eq system (no M2 event, unlike
    72	    (2,2)/(k>=3,2) where the inner extra is the single monomial -a3^k).
    73	### 1.2 Torus-emptiness: theorem or sub-regime
    74	
    75	THEOREM (surplus-4 variant, inner part; (k,d2) = (2,3), depth-2 block, any
    76	strip lengths containing it; char not in {2,3,5}). The inner leftover pair
    77	alone forces a3 = a4 = 0, i.e. V(L1,L2) = {a3 = a4 = 0}: P col 1 collapses
    78	to the binomial a1 + a2 y (support = p0 and (1,1)). Consequently the FULL
    79	4-leftover system has NO common zero with all block coordinates nonzero
    80	(any zero has a3 = 0): the toy_w3 "torus-EMPTY" numeric verdict is now an
    81	exact theorem.
    82	
    83	Proof 1 (resultant; machine-verified, wide phaseC2, exit 0).
    84	Res_a4(10L1, 10L2) = -3200 a3^7, and the a4-leading coefficient of 10L1 is
    85	the CONSTANT -25, so for every fixed (a2,a3) the two polynomials in a4 have
    86	a common root iff the resultant vanishes: any common zero has a3 = 0. Then
    87	10L2|_{a3=0} = a2 a4^2 and 10L1|_{a3=0} = 2 a2^3 a4 - 25 a4^2: a2 a4^2 = 0
    88	with a4 != 0 gives a2 = 0 and then L1 = -(5/2) a4^2 != 0 — so a4 = 0.
    89	Conversely a3 = a4 = 0 kills both (every monomial contains a3 or a4).
    90	Primes used: pivots 2..6 of the triangular solve, 3200 = 2^7 5^2, 25, 5/2:
    91	char not in {2,3,5} suffices (denominator/pivot set audited as in (2,2)).
    92	
    93	Proof 2 (structural: squarefree-forcing + log-free divisibility; conceptual
    94	route, generalizes — used again at d2 = 4 in §1.3).
    95	Extras vanish iff the polynomial identity  C'A - 2A'C = a1 c1  holds exactly
    96	with C the solved column (deg <= 6). (i) At any root r of A of multiplicity
    97	m >= 2 the left side is divisible by (y-r), the right side is a nonzero
    98	constant: so A is SQUAREFREE, and at simple roots -2A'(r)C(r) = a1 c1 gives
    99	A'(r), C(r) != 0. (ii) Differentiating the identity once/twice and
   100	evaluating at r: C'(r) = -2A''C/A', then -C'A'' - 2A'''C - 2A''C' = 0
   101	forces 3A''(r)^2 = A'(r)A'''(r). Hence A | N(A) := 3A''^2 - A'A'''.
   102	(iii) Case delta := deg A: delta = 3: N = (12a3^2-6a2a4) + 60a3a4 y
   103	+ 90a4^2 y^2 has deg 2 < 3, so N = 0: 90a4^2 = 0, impossible. delta = 2:
   104	N = 12a3^2 != 0 constant, impossible. So delta <= 1: a3 = a4 = 0. QED
   105	
   106	Class of the obstruction — HONEST: this is a SUPPORT-RIGIDITY statement
   107	(a3 = coeff_P(1,2), a4 = coeff_P(1,3) are forced to 0; neither is a
   108	saturated corner, so hypothesis (i) is untouched), NOT a PINS-form
   109	(unit)*(monomial)*b_q0 obstruction: b_q0 stays free. What survives of the
   110	(2,2) collapse mechanism at d2 = 3 is exactly this forced degeneration of
   111	the P-side column; the b-side content is settled next (outer pair on the
   112	binomial locus).
   113	
   114	COMPLETE VARIETY (surplus-4 variant theorem, full form; machine layer
   115	phaseC2b, W4, exit 0). On the forced locus a3 = a4 = 0 (A = a1 + a2 y):
   116	    L4 == 0 IDENTICALLY, and  L3 = (a2^3/21) * R,
   117	    R := a2^2 b4 - 5 a2 b5 + 15 b6      (b3 ABSENT).
   118	Hence  V(L1,L2,L3,L4) = {a3=a4=0, a2=0}  u  {a3=a4=0, R=0}.
   119	Mechanism of both facts (log-residue view, §2 Steps 3-4 with d2 = 3):
   120	with z = 1 + a2 y/a1, beta(z) = B(y(z)), the only singular integrand term
   121	is beta'_3 w^{-1} (m = k+1 = 3), so the non-polynomial part of E is
   122	-(c1/a2) beta'_3 z^3 log z. Both outer extras are forced multiples of the
   123	SINGLE residue beta'_3 = 4 R/a2^6 (units scaled to 1), where
   124	R = sum_{j=4}^{6} (-1)^j C(j,4) a2^{6-j} b_j; and the two tail coefficients
   125	of z^3 log z satisfy
   126	11*[y^11] + 7 a2 [y^10] = 0 for the z^3 log z series (11/1320 = 7/840),
   127	which kills the top extra L4 on the locus identically. The coefficients
   128	1, -5, 15 are (-1)^j C(j,4), j = 4..6 — at d2 = 2 the sum degenerates to
   129	the single term C(4,4) b4 = a6: the (2,2) PINS monomial is the d2 = 2
   130	shadow of this residue functional.
   131	Consequences: (1) torus-emptiness holds (via a3 = 0), settling the cell
   132	EXACTLY; (2) on the main component (a2 != 0) the residual b-side condition
   133	R = 0 is a 3-term linear form: solvable with all of b3..b6, b_q0 nonzero —
   134	NO empty chart in the b-coordinates and NO PINS leftover: condition (iii)
   135	in its (2,2) single-monomial form FAILS at (2,3); its correct analog is
   136	"P col 1 binomial + one residue hyperplane R = 0". (3) char caveats: the
   137	outer computation adds e-pivots 7,8,9 and denominators 21, 840, 1320
   138	(primes {2,3,5,7,11}); the INNER rigidity (the part torus-emptiness needs)
   139	uses only {2,3,5}.
   140	
   141	### 1.3 The pattern in w_P: rigidity at w_P = 4 and the k-grid
   142	
   143	Leftover COUNT: 2(w_P - 1) exactly, all cells (Prop B; z = 0 since no M2
   144	fires for w_P >= 3 — every extra key has >= 2 monomials, seen on the whole
   145	grid below). Scan values 4 (w_P=3), 6 (w_P=4): formula confirmed.
   146	
   147	THEOREM (w_P = 4, cell (2,4); char 0, excluded primes within {2,3,5,7}).
   148	V(inner extras I1,I2,I3) = {a3 = a4 = a5 = 0}: P col 1 is again forced to
   149	the binomial a1 + a2 y, so torus-emptiness PERSISTS at w_P = 4, exactly.
   150	On the forced locus the outer extras satisfy O2 = O3 = 0 IDENTICALLY and
   151	O1 = -(a2^4/55) R4, R4 := a2^4 b4 - 5 a2^3 b5 + 15 a2^2 b6 - 35 a2 b7
   152	+ 70 b8 (machine: phaseC3/W5-W6, exit 0). So
   153	  V(all 6 leftovers) = {a3=a4=a5=0, a2=0} u {a3=a4=a5=0, R4=0},
   154	same shape as (2,3): support rigidity + ONE residue hyperplane; no PINS.
   155	Proof of the inner part (structural route of §1.2 Proof 2, now with the
   156	delta = 4 divisibility case; every identity machine-asserted in phaseC3):
   157	extras vanish iff C'A - 2A'C = a1 c1 exactly => A squarefree and
   158	A | N(A), N := 3A''^2 - A'A'''. Writing A = 1 + py + qy^2 + ry^3 + sy^4:
   159	  N - 336 s A = E0 + 60 E1 y + 30 E2 y^2   (top two coeffs cancel), with
   160	  E0 = 12q^2 - 6pr - 336s, E1 = qr - 6ps, E2 = 3r^2 - 8qs.
   161	delta = 4 (s != 0): divisibility means E0 = E1 = E2 = 0; the identities
   162	  9s E0 = 84 s (q^2 - 36 s) - 3 q E2 + 9 r E1,
   163	  27 r^2 - 2 q^3 = 9 E2 - 2 q (q^2 - 36 s)
   164	give q^2 = 36s, 27r^2 = 2q^3, and (via E1, q != 0) r = pq/6; these force
   165	(p,q,r,s) = (4u, 6u^2, 4u^3, u^4), i.e. A = (1 + u y)^4 — NOT squarefree
   166	(u = 0 would give s = 0): contradiction. delta = 3 (s = 0, r != 0):
   167	N = (12q^2 - 6pr) + 60qr y + 90r^2 y^2 has degree 2 < 3, so N = 0:
   168	90 r^2 = 0, impossible. delta = 2: N = 12q^2 != 0 constant, impossible.
   169	Hence delta <= 1. QED (perfect powers (1+uy)^delta satisfy the
   170	divisibility for every delta >= 4 — squarefreeness is what kills them;
   171	any general-d2 proof must keep both halves).
   172	
   173	GRID (phaseC3b, exit 0). Inner rigidity V(inner) = {A binomial} is also
   174	CERTIFIED at (k,3) for k = 3, 4, 5 by a uniform two-resultant certificate:
   175	Res_a4(J1,J2) = c a3^m with CONSTANT a4-lead of J1 (=> a3 = 0), then on
   176	the slice Res_a2 = c' a4^N with pure-a4 a2-lead (=> a4 = 0); exponents
   177	(m,N) = (7,8), (15,12), (26,34), (40,44) for k = 2,3,4,5. Combined with
   178	d2 = 2 (inner = -a3^k, k <= 10) and (2,4): rigidity holds on the ENTIRE
   179	computed grid k in 2..5, d2 in 2..4 except (3,4)/(4,4)/(5,4) (inner not
   180	yet eliminated there; (3,4) numeric-EMPTY is consistent with rigidity).

exec
/bin/zsh -lc "rg -n \"def wide_setup|def col_series|inner|extras|W1|lattice|ode\" cases/surplus_ext.py cases/residue_check.py | head -n 220; sed -n '1,260p' cases/surplus_ext.py; sed -n '1,260p' cases/residue_check.py" in /Users/dc/code/math/jc72108
 succeeded in 0ms:
cases/residue_check.py:18:      G_n == 0 for n >= (k+1)d2;  extras t>=1 == 0;  extra_0 ==
cases/residue_check.py:84:    """Binomial-locus data: A=1+a2y, C exact, G, solved E, extras."""
cases/residue_check.py:94:    extras = [extra_value(A0, k + 2, G, E, (k + 1) * d2 + t)
cases/residue_check.py:96:    return A0, B, C, G, E, extras
cases/residue_check.py:103:        _, _, _, _, _, extras = direct_cell(k, d2)
cases/residue_check.py:104:        ok &= (rep == extras)
cases/residue_check.py:106:              f"solve: {'OK' if rep == extras else 'FAIL'}")
cases/residue_check.py:220:def t5_uniform(k, d2, G, E, extras):
cases/residue_check.py:223:    ok_hi = all(extras[t] == {} for t in range(1, d2 - 1))
cases/residue_check.py:226:    ok_e = (extras[0] == pred_e)
cases/residue_check.py:230:    ok_cf = (extras[0] == closed)
cases/residue_check.py:232:          f" | extras t>=1 == 0: {'OK' if ok_hi else 'FAIL'}"
cases/residue_check.py:239:# `mathieu` mode — MATHIEU.md companion (run: python3 residue_check.py mathieu)
cases/residue_check.py:242:# M1 rigidity dichotomy: inner extras of cell (k,d2) vanish at numeric A
cases/residue_check.py:253:#    symbolic inner extras vanish identically on the binomial locus; are
cases/residue_check.py:302:def _inner_extras(A, k, d2):
cases/residue_check.py:317:                        ex = _inner_extras(A, k, d2)
cases/residue_check.py:323:    print(f"M1 rigidity dichotomy (extras==0 <=> deg A<=1), k=1..5, d2=2..5, "
cases/residue_check.py:450:        ex = _inner_extras(A, k, d2)
cases/residue_check.py:451:        # (i) binomial locus: extras vanish identically (symbolic)
cases/residue_check.py:481:            exn = _inner_extras(An, k, d2)
cases/residue_check.py:486:        print(f"M5 ({k},{d2}): binomial extras==0: {'OK' if okb else 'FAIL'}"
cases/residue_check.py:508:        A0, B, C, G, E, extras = direct_cell(k, d2)
cases/residue_check.py:512:        if d2 >= 2 and extras:
cases/residue_check.py:513:            allok &= t5_uniform(k, d2, G, E, extras)
cases/surplus_ext.py:16:  V2  inner extra == -a3^k * c1 * a1^(1-k) for k=2..10  (extends the k<=5
cases/surplus_ext.py:45:def col_series(Acoef, ncoef, inhom, val, top):
cases/surplus_ext.py:99:        inner = extra_value(A, k + 1, {}, C, 2 * k)          # key (k+1, 2k+1)
cases/surplus_ext.py:101:        v2 = (inner == want)
cases/surplus_ext.py:127:            print(f"k={k:2d}: V2 inner=-a3^k {'OK' if v2 else 'FAIL '+mstr_p(inner)}"
cases/surplus_ext.py:137:def wide_setup(k, d2):
cases/surplus_ext.py:141:    Returns (A,B,C,inner,E,outer): C,E solved series (dict s->poly);
cases/surplus_ext.py:142:    inner = extras of col k+1 at y^n, n = k*d2 + t   (key (k+1, n+1)),
cases/surplus_ext.py:143:    outer = extras of col k+2 at y^n, n = (k+1)*d2+t (key (k+2, n+1)),
cases/surplus_ext.py:150:    inner = [extra_value(A, k + 1, {}, C, k * d2 + t) for t in range(d2 - 1)]
cases/surplus_ext.py:157:    return A, B, C, inner, E, outer
cases/surplus_ext.py:161:    A, B, C, inner, E, outer = wide_setup(2, 2)
cases/surplus_ext.py:162:    ok = (inner[0] == {mono({'a3': 2}): Fraction(-1)})
cases/surplus_ext.py:165:    print("W0 (2,2) anchor: inner=-a3^2, outer|a3=0=-(1/5)a2^2*b4:",
cases/surplus_ext.py:169:def wide_W1(k=2, d2=3):
cases/surplus_ext.py:172:    eliminated keys -> 0, vertex -> const, extras -> inner/outer polys."""
cases/surplus_ext.py:173:    A, B, C, inner, E, outer = wide_setup(k, d2)
cases/surplus_ext.py:198:    ex_in = {(k + 1, k * d2 + t + 1): inner[t] for t in range(d2 - 1)}
cases/surplus_ext.py:209:    print(f"W1 ({k},{d2}) lattice keys == ODE view "
cases/surplus_ext.py:210:          f"(eliminated->0, extras match):", "OK" if ok else "FAIL")
cases/surplus_ext.py:267:    """(2,3) torus-emptiness: exact resultant certificate for the inner pair.
cases/surplus_ext.py:272:    A, B, C, inner, E, outer = wide_setup(2, 3)
cases/surplus_ext.py:273:    L1, L2 = inner
cases/surplus_ext.py:291:    """Outer extras restricted to the binomial locus (a3=..=a_{d2+1}=0).
cases/surplus_ext.py:293:    A, B, C, inner, E, outer = wide_setup(k, d2)
cases/surplus_ext.py:319:    """(2,4) = w_P 4: inner rigidity V(I1,I2,I3) = {a3=a4=a5=0} via the
cases/surplus_ext.py:323:    A, B, C, inner, E, outer = wide_setup(2, 4)
cases/surplus_ext.py:325:    for I in inner:                      # vanish on the binomial locus
cases/surplus_ext.py:330:    print("W5a (2,4) inner extras vanish on {a3=a4=a5=0}:",
cases/surplus_ext.py:398:    """Grid survey. (a) d2=3, k=2..5: certify inner rigidity
cases/surplus_ext.py:401:    k=2..5, d2=3 and k=2..3, d2=4: which extras vanish identically; the
cases/surplus_ext.py:408:        A, B, C, inner, E, outer = wide_setup(k, 3)
cases/surplus_ext.py:409:        J1, J2 = inner
cases/surplus_ext.py:457:    ok = wide_W0() and wide_W1(2, 3) and wide_W1(2, 4) and wide_W1(3, 3)
cases/surplus_ext.py:458:    A, B, C, inner, E, outer = wide_setup(2, 3)
cases/surplus_ext.py:459:    print("(2,3) inner extras (keys (3,7),(3,8)); 10*L:")
cases/surplus_ext.py:460:    for t, L in enumerate(inner):
cases/surplus_ext.py:462:    print("(2,3) outer extras: term counts",
cases/surplus_ext.py:471:    print("V2 (inner extra = -a3^k c1 a1^{1-k}, k<=10):", "OK" if v2 else "FAIL")
#!/usr/bin/env python3
"""SURPLUS-EXT companion script (see SURPLUS-EXT.md).

Part 1 (Phase B, k>=3 / d2=2): exact verification of the column-ODE view and
of the log-residue mechanism.  Post-gap-kill, Minkowski column k+1 of [P,Q]
as a polynomial in y is A C' - k A' C (A = P col 1, C = Q col k) and column
k+2 is A E' - (k+1) A' E + 2 B C' - k B' C (B = P col 2, E = Q col k+1);
key (X,s) = coeff of y^{s-1}.  The in-block cascade of surplus_count.py is
equivalent to solving the column ODEs coefficient-by-coefficient; the extra
keys evaluate minus the "would-be next" series coefficients.

Checks (exact Fraction arithmetic, symbolic in a2,a3,a4,a5,a6; a1=c1=1 wlog
by unit scaling -- reduced forms carry the units back):
  V1  keys from the ODE view == keys from surplus_count.py enumeration
      (d2=2..3, k=2..5).
  V2  inner extra == -a3^k * c1 * a1^(1-k) for k=2..10  (extends the k<=5
      verification of SURPLUS.md; general k NOT proved, see SURPLUS-EXT §2).
  V3  with a3=0: outer extra == 0 identically for k=3..10, and for k=2
      outer extra == -(1/5) a2^2 a6 (matching the theorem) with
      e_top == -(1/15) a2 a6 (matching b10 = -a2 a6 b3/(15 a1^2)).
  V4  with a3=0: E-closed-form degree bound deg_y E <= k+3 (k=3..10).
Part 2 (Phase C, (k,d2)=(2,3) wide strip): see functions wide_*.
"""
import os, sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from surplus_count import analyze, mono, pmul, ppow, padd_into, psubst, mstr

# poly in variables 'a2','a3',... : dict {mono: Fraction}; mono from surplus_count
ONE = {(): Fraction(1)}

def V(name):
    return {mono({name: 1}): Fraction(1)}

def pscale(p, c):
    return {m: cc * c for m, cc in p.items()}

def padd(p, q):
    r = dict(p)
    for m, c in q.items():
        padd_into(r, m, c)
    return r

def col_series(Acoef, ncoef, inhom, val, top):
    """Column X of the bracket reads sum_i (n+1 - i*ncoef) A_i c_{n+1-i}
    + inhom_n = 0 for n >= 1 (A_0 = 1, a1 scaled out; ncoef = k+1 for the
    C-column A C' - k A' C, ncoef = k+2 for the E-column A E' - (k+1) A' E).
    Solves for c_{val..top} (c_1 := 1 when val == 1); returns dict s->poly."""
    out = {}
    if val == 1:
        out[1] = ONE
    n = 1 if val == 1 else val - 1
    while n <= top - 1:
        acc = dict(inhom.get(n, {}))
        for i, Ai in Acoef.items():
            if i == 0:
                continue
            j = n + 1 - i
            if j in out:
                coef = Fraction(n + 1 - i * ncoef)
                if coef:
                    acc = padd(acc, pscale(pmul(Ai, out[j]), coef))
        # (n+1) * 1 * c_{n+1} + acc = 0
        out[n + 1] = pscale(acc, Fraction(-1, n + 1))
        n += 1
    return out

def extra_value(Acoef, ncoef, inhom, out, n):
    """Evaluate equation n with series coefficients out (missing -> 0)."""
    acc = dict(inhom.get(n, {}))
    for i, Ai in Acoef.items():
        j = n + 1 - i
        if j in out:
            coef = Fraction(n + 1 - i * ncoef)
            if coef:
                acc = padd(acc, pscale(pmul(Ai, out[j]), coef))
    return acc

def deriv_prod(F, G, cF, cG, deg):
    """coefficients of cF*F'G + cG*FG' ... helper: returns dict n->poly of
    cF * F' * G + cG * F * G' for coefficient dicts F,G (s->poly)."""
    res = {}
    for sf, pf in F.items():
        for sg, pg in G.items():
            n = sf + sg - 1
            coef = Fraction(cF * sf + cG * sg)
            if coef:
                res.setdefault(n, {})
                for m, c in pmul(pf, pg).items():
                    padd_into(res[n], m, c * coef)
    return {n: {m: c for m, c in p.items() if c} for n, p in res.items()}

def phaseB(kmax=10, verbose=True):
    okV2 = okV3 = okV4 = True
    for k in range(2, kmax + 1):
        A = {0: ONE, 1: V('a2'), 2: V('a3')}
        C = col_series(A, k + 1, {}, 1, 2 * k)
        inner = extra_value(A, k + 1, {}, C, 2 * k)          # key (k+1, 2k+1)
        want = pscale({mono({'a3': k}): Fraction(1)}, Fraction(-1))
        v2 = (inner == want)
        okV2 &= v2
        # now a3 := 0 everywhere
        A0 = {0: ONE, 1: V('a2')}
        C0 = {s: psubst(p, 'a3', {}) for s, p in C.items()}
        C0 = {s: p for s, p in C0.items() if p}
        B = {2: V('a4'), 3: V('a5'), 4: V('a6')}
        # G_n = coeffs of 2 B C' - k B' C  (inhom for E-column with + sign)
        G = deriv_prod(C0, B, 2, -k, None)               # 2 C'... careful order
        # deriv_prod(F,G,cF,cG) = cF F'G + cG F G': want 2 B C' - k B' C =
        #   with F=C0, G=B: 2 C0' B  + (-k) C0 B'  -> cF=2, cG=-k
        assert not G.get(0) and not G.get(1)
        E = col_series(A0, k + 2, G, 3, 2 * k + 2)
        outer = extra_value(A0, k + 2, G, E, 2 * k + 2)  # key (k+2, 2k+3)
        etop = E.get(2 * k + 2, {})
        if k == 2:
            v3 = (outer == pscale(pmul(pmul(V('a2'), V('a2')), V('a6')),
                                  Fraction(-1, 5))
                  and etop == pscale(pmul(V('a2'), V('a6')), Fraction(-1, 15)))
        else:
            v3 = (outer == {})
        okV3 &= v3
        degE = max([s for s, p in E.items() if p], default=0)
        v4 = (k == 2) or (degE <= k + 3)
        okV4 &= v4
        if verbose:
            print(f"k={k:2d}: V2 inner=-a3^k {'OK' if v2 else 'FAIL '+mstr_p(inner)}"
                  f" | V3 outer {'OK' if v3 else 'FAIL '+mstr_p(outer)}"
                  f" | degE={degE} (bound {k+3}) {'OK' if v4 else 'FAIL'}")
    return okV2, okV3, okV4

def mstr_p(p):
    return " + ".join(f"{c}*{mstr(m)}" for m, c in sorted(p.items())) or "0"

# ---------------- Phase C: wide strips w_P = d2 >= 3 (SURPLUS-EXT §1) -------

def wide_setup(k, d2):
    """Column-ODE data, general (k,d2), units a1=c1=1 scaled out.
    A = 1 + sum_{i=1}^{d2} a_{i+1} y^i  (vars 'a2'..'a{d2+1}', P col 1),
    B = sum_{i=d2}^{2d2} B_i y^i        (vars 'b{i}',        P col 2).
    Returns (A,B,C,inner,E,outer): C,E solved series (dict s->poly);
    inner = extras of col k+1 at y^n, n = k*d2 + t   (key (k+1, n+1)),
    outer = extras of col k+2 at y^n, n = (k+1)*d2+t (key (k+2, n+1)),
    t = 0..d2-2 (strata w = d2-1-t .. matches Prop B's w in [1, w_P-1])."""
    A = {0: ONE}
    for i in range(1, d2 + 1):
        A[i] = V(f'a{i+1}')
    B = {i: V(f'b{i}') for i in range(d2, 2 * d2 + 1)}
    C = col_series(A, k + 1, {}, 1, k * d2)
    inner = [extra_value(A, k + 1, {}, C, k * d2 + t) for t in range(d2 - 1)]
    G = deriv_prod(C, B, 2, -k, None)             # 2 B C' - k B' C
    for n in range(0, d2):
        assert not G.get(n), f"G has low support at {(k, d2, n)}"
    E = col_series(A, k + 2, G, d2 + 1, (k + 1) * d2)
    outer = [extra_value(A, k + 2, G, E, (k + 1) * d2 + t)
             for t in range(d2 - 1)]
    return A, B, C, inner, E, outer

def wide_W0():
    """Anchor: wide_setup(2,2) reproduces the (2,2) theorem quantities."""
    A, B, C, inner, E, outer = wide_setup(2, 2)
    ok = (inner[0] == {mono({'a3': 2}): Fraction(-1)})
    o0 = psubst(outer[0], 'a3', {})
    ok &= (o0 == {mono({'a2': 2, 'b4': 1}): Fraction(-1, 5)})
    print("W0 (2,2) anchor: inner=-a3^2, outer|a3=0=-(1/5)a2^2*b4:",
          "OK" if ok else "FAIL")
    return ok

def wide_W1(k=2, d2=3):
    """Lattice cross-check: enumerate every block key from dets (independent
    path, mirrors surplus_count), substitute the ODE solution for all b's:
    eliminated keys -> 0, vertex -> const, extras -> inner/outer polys."""
    A, B, C, inner, E, outer = wide_setup(k, d2)
    subs = {}                                     # Q-side: (col, y) -> poly
    for s, p in C.items():
        subs[(k, s)] = p
    for s, p in E.items():
        subs[(k + 1, s)] = p
    Aco = {i: (A[i] if i else ONE) for i in range(0, d2 + 1)}
    keys = {}
    # P col 1 points (1, i) i=0..d2 (coef A_i); col 2 points (2, i) i=d2..2d2
    Ppts = [((1, i), Aco[i]) for i in range(0, d2 + 1)] + \
           [((2, i), B[i]) for i in range(d2, 2 * d2 + 1)]
    for (p, ap) in Ppts:
        for (qc, qy), bq in subs.items():
            X = p[0] + qc
            if X not in (k + 1, k + 2):
                continue
            det = p[0] * qy - p[1] * qc
            if det == 0:
                continue
            m = (X, p[1] + qy)
            keys.setdefault(m, {})
            for mm, cc in pmul(ap, bq).items():
                padd_into(keys[m], mm, cc * det)
    keys = {m: {mm: c for mm, c in e.items() if c} for m, e in keys.items()}
    ok = True
    ex_in = {(k + 1, k * d2 + t + 1): inner[t] for t in range(d2 - 1)}
    ex_out = {(k + 2, (k + 1) * d2 + t + 1): outer[t] for t in range(d2 - 1)}
    for m, e in sorted(keys.items()):
        if m == (k + 1, 1):
            ok &= (e == {(): Fraction(1)})       # det(p0,q0) a1 c1 = 1
        elif m in ex_in:
            ok &= (e == ex_in[m])
        elif m in ex_out:
            ok &= (e == ex_out[m])
        else:
            ok &= (e == {})
    print(f"W1 ({k},{d2}) lattice keys == ODE view "
          f"(eliminated->0, extras match):", "OK" if ok else "FAIL")
    return ok

def selftestV1():
    """ODE-view keys == surplus_count enumeration keys (spot families)."""
    ok = True
    for d2, k in [(2, 2), (2, 3), (2, 5), (3, 2), (3, 3)]:
        cP = [(0, 0), (1, 0), (4, 3 * d2), (4, 4 * d2)]
        cQ = [(0, 0), (k, 1), (k + 3, 1 + 3 * d2), (k + 3, (k + 3) * d2)]
        r = analyze(f"v1_k{k}_d{d2}", cP, cQ, k, verbose=False)
        # ODE-view key count: col k+1 strata 2..(wP+wQ+1)-? == 2(wP+wQ)-1 total
        ok &= (r["n_keys"] == 2 * (d2 + k * d2 - 1) - 1)
    print("V1 key-count vs enumeration:", "OK" if ok else "FAIL")
    return ok

def pcoeffs(p, v):
    """View dict-poly p as univariate in variable v: list of dict-poly
    coefficients [c0, c1, ...]."""
    out = {}
    for m, c in p.items():
        d = dict(m)
        e = d.pop(v, 0)
        out.setdefault(e, {})
        padd_into(out[e], mono(d), c)
    deg = max(out, default=0)
    return [out.get(i, {}) for i in range(deg + 1)]

def pdet(M):
    """Determinant of a small matrix of dict-polys (cofactor expansion)."""
    n = len(M)
    if n == 1:
        return M[0][0]
    acc = {}
    for i in range(n):
        if not M[i][0]:
            continue
        minor = [[M[r][c] for c in range(1, n)] for r in range(n) if r != i]
        term = pmul(M[i][0], pdet(minor))
        for m, c in term.items():
            padd_into(acc, m, c if i % 2 == 0 else -c)
    return acc

def presultant(p, q, v):
    """Sylvester resultant of p, q with respect to variable v."""
    P, Q = pcoeffs(p, v), pcoeffs(q, v)
    m, n = len(P) - 1, len(Q) - 1
    N = m + n
    M = [[{} for _ in range(N)] for _ in range(N)]
    for r in range(n):                       # rows of p-coefficients
        for j, c in enumerate(P[::-1]):
            M[r][r + j] = c
#!/usr/bin/env python3
"""RESIDUE.md companion: is R_{k,d2} a residue?  Exact Fraction arithmetic.

Tests (see RESIDUE.md for statements):
  T0  anchor: repo's binom_outer (general solve, then restrict) agrees with
      the direct binomial-locus solve used here (cells (2,2),(2,3),(3,3)).
  T1  (interp b1) Res_{y=-1/a2}[G/A^{k+2} dy] == (k+2)(-1)^k a2^{-2d2-1} R.
  T2  (interp b2) residue theorem: Res_{y0} == -Res_infty (independent
      Laurent-at-infinity computation).
  T3  (interp a) T3a Jac(P, x^k C) == x^k + x^{k+1} G;  T3b the E-part
      (AE'-(k+1)A'E)/A^{k+2} has residue 0 for arbitrary symbolic E
      (exactness => Res2 of dP^dQ/(x^{k+2}A^{k+2}) is E-independent);
      T3c the naive dP^dQ/P^{k+2} variant has TOTAL iterated residue 0.
  T4  (interp c) mu o L == 0 (moment functional kills im ad_{xA});
      left-null-space of L on the window is 2-dim = span{mu, top functional
      supported above deg G}  =>  obstruction <=> mu(G) = 0.
  T5  (uniform outer theorem) on the binomial locus, for each cell:
      G_n == 0 for n >= (k+1)d2;  extras t>=1 == 0;  extra_0 ==
      a2 (k+1)(d2-1) e_top;  and the closed form
      extra_0 == (-1)^(k+(k+1)(d2-1)) (k+2)/C((k+1)d2,k+1) a2^((k-1)d2) R.
      Cells include (4,4),(5,4),(2,5),(3,5): NEW, beyond the repo grid.
"""
import os, sys
from fractions import Fraction as F
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from surplus_count import mono, pmul, ppow, padd_into, psubst
from surplus_ext import (V, ONE, pscale, padd, col_series, extra_value,
                         deriv_prod, wide_setup, binom_outer, mstr_p)

def cmb(n, r):
    return comb(n, r) if 0 <= r <= n else 0

def a2pow(e):
    return {mono({'a2': e}): F(1)}

def Rpoly(k, d2):
    """R_{k,d2} = sum_{j=k+2}^{2d2} (-1)^j C(j,k+2) a2^(2d2-j) b_j."""
    R = {}
    for j in range(max(k + 2, d2), 2 * d2 + 1):   # b_j exists only for j>=d2

        padd_into(R, mono({'a2': 2 * d2 - j, f'b{j}': 1}),
                  F((-1) ** j * comb(j, k + 2)))
    return R

def binom_C(k):
    """Exact solution of AC'-kA'C=1 on the binomial locus:
    C = ((1+a2 y)^k - 1)/(k a2) = sum_{i=1}^k C(k,i)/k a2^(i-1) y^i."""
    return {i: {mono({'a2': i - 1}): F(comb(k, i), k)} for i in range(1, k + 1)}

def Bpoly(d2):
    return {j: V(f'b{j}') for j in range(d2, 2 * d2 + 1)}

def res_S(H, p):
    """Res_{y=-1/a2}[H(y)/A^p dy], A = 1+a2y.  Returns (S, N) with
    Res = S * a2^(-(N+1)):  S = [w^(p-1)] sum_n H_n a2^(N-n) (w-1)^n."""
    N = max(H.keys())
    S = {}
    for n, hn in H.items():
        c = F(cmb(n, p - 1) * (-1) ** (n - p + 1))     # [w^(p-1)](w-1)^n
        if c:
            for m, cc in pmul(hn, a2pow(N - n)).items():
                padd_into(S, m, cc * c)
    return {m: c for m, c in S.items() if c}, N

def res_inf_S(H, p):
    """-[y^(-1)] of H/A^p expanded at infinity: (S', N) with
    Res_inf = S' * a2^(-(N+1)); independent path (binomial series)."""
    N = max(H.keys())
    S = {}
    for n, hn in H.items():
        t = n - p + 1                                   # y^(n-p-t) = y^-1
        if t < 0:
            continue
        c = F(-((-1) ** t) * cmb(p + t - 1, t))         # -C(-p,t)
        if c:
            # a2^(-p-t) * a2^... total a2 exponent -(n+1); scale to N
            for m, cc in pmul(hn, a2pow(N - n)).items():
                padd_into(S, m, cc * c)
    return {m: c for m, c in S.items() if c}, N

def direct_cell(k, d2):
    """Binomial-locus data: A=1+a2y, C exact, G, solved E, extras."""
    A0 = {0: ONE, 1: V('a2')}
    C = binom_C(k)
    # cross-check C against the series solver
    Cs = col_series(A0, k + 1, {}, 1, k * d2)
    Cs = {s: p for s, p in Cs.items() if p}
    assert Cs == C, f"C mismatch at {(k, d2)}"
    B = Bpoly(d2)
    G = deriv_prod(C, B, 2, -k, None)                   # 2BC' - kB'C
    E = col_series(A0, k + 2, G, d2 + 1, (k + 1) * d2)
    extras = [extra_value(A0, k + 2, G, E, (k + 1) * d2 + t)
              for t in range(d2 - 1)]
    return A0, B, C, G, E, extras

def t0_anchor():
    ok = True
    for (k, d2, azero) in [(2, 2, ['a3']), (2, 3, ['a3', 'a4']),
                           (3, 3, ['a3', 'a4'])]:
        rep = binom_outer(k, d2, azero)
        _, _, _, _, _, extras = direct_cell(k, d2)
        ok &= (rep == extras)
        print(f"T0 ({k},{d2}): general-solve|binomial == direct binomial "
              f"solve: {'OK' if rep == extras else 'FAIL'}")
    return ok

def t1_t2_residue(k, d2, G):
    R = Rpoly(k, d2)
    S, N = res_S(G, k + 2)
    # claim: S * a2^-(N+1) == (k+2)(-1)^k a2^(-2d2-1) R
    lhs = pmul(S, a2pow(2 * d2))
    rhs = pscale(pmul(a2pow(N), R), F((k + 2) * (-1) ** k))
    ok1 = (lhs == rhs)
    Si, Ni = res_inf_S(G, k + 2)
    ok2 = (pmul(S, a2pow(Ni)) == pscale(pmul(Si, a2pow(N)), F(-1)))
    print(f"T1 ({k},{d2}): Res_y0[G/A^(k+2)] == (k+2)(-1)^k a2^(-2d2-1) R:"
          f" {'OK' if ok1 else 'FAIL'} | T2 Res_y0 == -Res_inf:"
          f" {'OK' if ok2 else 'FAIL'}")
    return ok1 and ok2

def t3_groth(k, d2, A0, B, C, G):
    # T3a: AC' - kA'C == 1  (=> Jac(P, x^k C) = x^k + x^(k+1) G exactly,
    # G being by construction the x^(k+1)-column)
    dd = {n: p for n, p in deriv_prod(C, A0, 1, -k, None).items() if p}
    ok_a = (dd == {0: ONE})
    # T3b: arbitrary symbolic E-part has residue 0 (exactness)
    Esym = {m: V(f'e{m}') for m in range(d2 + 1, (k + 1) * d2 + 1)}
    LE = deriv_prod(Esym, A0, 1, -(k + 1), None)        # AE' - (k+1)A'E
    S_LE, _ = res_S(LE, k + 2)
    ok_b = (S_LE == {})
    # T3c: naive dP^dQ/P^(k+2): Res_x gives G/A^(k+2) - (k+2) B/A^(k+3);
    # total y-residue must vanish (the form is exact).
    S_G, N_G = res_S(G, k + 2)
    S_B, N_B = res_S(B, k + 3)
    tot = padd(pmul(S_G, a2pow(N_B)),
               pscale(pmul(S_B, a2pow(N_G)), F(-(k + 2))))
    tot = {m: c for m, c in tot.items() if c}
    ok_c = (tot == {})
    print(f"T3 ({k},{d2}): a) Jac identity {'OK' if ok_a else 'FAIL'}"
          f" | b) E-part residue 0 (any E): {'OK' if ok_b else 'FAIL'}"
          f" | c) dP^dQ/P^(k+2) residue == 0: {'OK' if ok_c else 'FAIL'}")
    return ok_a and ok_b and ok_c

def t4_koszul(k, d2, G):
    lo, hi = d2 + 1, (k + 1) * d2                       # E-support
    tlo, thi = d2, (k + 1) * d2 + 1                     # window
    # mu o L == 0: m C(m-1,k+1) == (m-k-1) C(m,k+1) for all m in source
    ok_mu = all(m * cmb(m - 1, k + 1) == (m - k - 1) * cmb(m, k + 1)
                for m in range(lo, hi + 1))
    # exact left null space at generic a2 = 3/7 (and 5/3 as guard)
    ok_rank = True
    for a2v in (F(3, 7), F(5, 3)):
        rows = list(range(tlo, thi + 1))
        cols = list(range(lo, hi + 1))
        M = [[F(0)] * len(cols) for _ in rows]          # M[n][m] = L coeff
        for jc, m in enumerate(cols):
            M[rows.index(m - 1)][jc] += m               # m y^(m-1)
            M[rows.index(m)][jc] += a2v * (m - k - 1)   # a2(m-k-1) y^m
        # left null space = null space of transpose
        A = [list(r) for r in map(list, zip(*M))]       # cols x rows
        nr, nc = len(A), len(A[0])
        piv = []
        r = 0
        for c in range(nc):
            pr = next((i for i in range(r, nr) if A[i][c]), None)
            if pr is None:
                continue
            A[r], A[pr] = A[pr], A[r]
            A[r] = [x / A[r][c] for x in A[r]]
            for i in range(nr):
                if i != r and A[i][c]:
                    A[i] = [x - A[i][c] * y for x, y in zip(A[i], A[r])]
            piv.append(c)
            r += 1
        free = [c for c in range(nc) if c not in piv]
        null = []
        for fc in free:
            v = [F(0)] * nc
            v[fc] = F(1)
            for i, pc in enumerate(piv):
                v[pc] = -A[i][fc]
            null.append(v)
        ok_rank &= (len(null) == 2)
        # mu in null space?
        mu = [F((-1) ** (n - k - 1) * cmb(n, k + 1)) * a2v ** (-(n + 1))
              for n in rows]
        for v in null:                                  # reduce mu by null
            pass
        # check mu satisfies mu.M == 0 directly
        okm = all(sum(mu[i] * M[i][jc] for i in range(len(rows))) == 0
                  for jc in range(len(cols)))
        ok_rank &= okm
        # second functional supported above deg G: eliminate to get a null
        # vector vanishing on all n <= degG
        degG = max(G.keys())
        span = [list(v) for v in null]
        # gaussian-eliminate span on coordinates n <= degG
        r = 0
        for i, n in enumerate(rows):
            if n > degG:
                continue
            pr = next((j for j in range(r, len(span)) if span[j][i]), None)
            if pr is None:
                continue
            span[r], span[pr] = span[pr], span[r]
            for j in range(len(span)):
                if j != r and span[j][i]:
                    fpiv = span[j][i] / span[r][i]
                    span[j] = [x - fpiv * y for x, y in zip(span[j], span[r])]
            r += 1
        # after elimination, vectors span[r:] vanish on n <= degG
        ok_rank &= (len(span) - r == 1)
    print(f"T4 ({k},{d2}): mu o L == 0: {'OK' if ok_mu else 'FAIL'}"
          f" | coker dim 2, mu in ann(im L), 2nd functional above deg G:"
          f" {'OK' if ok_rank else 'FAIL'}")
    return ok_mu and ok_rank

def t5_uniform(k, d2, G, E, extras):
    n0 = (k + 1) * d2
    ok_deg = all(n < n0 for n in G.keys())
    ok_hi = all(extras[t] == {} for t in range(1, d2 - 1))
    etop = E.get(n0, {})
    pred_e = pscale(pmul(a2pow(1), etop), F((k + 1) * (d2 - 1)))
    ok_e = (extras[0] == pred_e)
    sign = (-1) ** (k + (k + 1) * (d2 - 1))
    closed = pscale(pmul(a2pow((k - 1) * d2), Rpoly(k, d2)),
                    F(sign * (k + 2), comb(n0, k + 1)))
    ok_cf = (extras[0] == closed)
    print(f"T5 ({k},{d2}): deg G < (k+1)d2: {'OK' if ok_deg else 'FAIL'}"
          f" | extras t>=1 == 0: {'OK' if ok_hi else 'FAIL'}"
          f" | extra_0 == a2(k+1)(d2-1) e_top: {'OK' if ok_e else 'FAIL'}"
          f" | closed form (+/-)(k+2)/C({n0},{k + 1}) a2^{(k - 1) * d2} R:"
          f" {'OK' if ok_cf else 'FAIL'}")
    return ok_deg and ok_hi and ok_e and ok_cf

# ---------------------------------------------------------------------------
# `mathieu` mode — MATHIEU.md companion (run: python3 residue_check.py mathieu)
# Machine checks for the Mathieu-Zhao bridge and the rigidity theorem
#   Theorem A: A C' - w A' C = c (const != 0), w >= 1  =>  deg A <= 1.
# M1 rigidity dichotomy: inner extras of cell (k,d2) vanish at numeric A
#    iff deg A <= 1 (random / perfect-power / mixed A, exact Fractions).
# M2 bridge witness + linear form: y^((k+1)delta-1) not in Im(L_A) (properness
#    of the candidate Mathieu subspace), and L_A(C) = 1 inconsistent iff
#    deg A >= 2 (solvable control at deg A <= 1).
# M3 CT form: R_{k,d2} is the honest Laurent constant term
#    CT_w(beta'(w) w^-(k+1)) on the binomial locus (a2^{2d2} beta_{k+2}
#    == (-1)^k R); independently re-derives the max(k+2,d2) lower limit.
# M4 proof identities of Theorem A, symbolically: L_A(A^k) == 0 and the
#    leading-coefficient lemma lc(L_A(D)) = (deg D - k deg A) lc(A) lc(D).
# M5 per-cell tie (incl. OPEN cells (3,4),(4,4),(5,4),(2,5),(3,5),(2,6)):
#    symbolic inner extras vanish identically on the binomial locus; are
#    nonzero at perfect-power and random off-binomial points; symbolic and
#    numeric evaluation paths agree.
import random

def _num(c):
    c = F(c)
    return {(): c} if c else {}

exec
/bin/zsh -lc "PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from fractions import Fraction
from itertools import product

def consistent(A,w,extra=4):
    delta=len(A)-1
    cap=w*delta+extra
    rows=delta+cap
    M=[]
    for n in range(rows):
        row=[Fraction(0) for _ in range(cap+1)]
        for i,ai in enumerate(A):
            j=n+1-i
            if 0 <= j <= cap:
                row[j] += Fraction((j-w*i)*ai)
        rhs=Fraction(1 if n==0 else 0)
        M.append(row+[rhs])
    r=0; cols=cap+1
    for c in range(cols):
        piv=next((q for q in range(r,len(M)) if M[q][c]),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        z=M[r][c]
        M[r]=[x/z for x in M[r]]
        for q in range(len(M)):
            if q"'!=r and M[q][c]:
                z=M[q][c]
                M[q]=[x-z*y for x,y in zip(M[q],M[r])]
        r+=1
    return not any(all(x==0 for x in row[:cols]) and row[-1]!=0 for row in M)

vals=range(-2,3)
total=sol=0
by={}
for delta in range(2,5):
  for low in product(vals, repeat=delta):
    for lead in (-2,-1,1,2):
      A=tuple(low)+(lead,)
      for w in range(1,5):
        total+=1
        ok=consistent(A,w)
        sol+=ok
        by[(delta,w)]=by.get((delta,w),[0,0])
        by[(delta,w)][0]+=1; by[(delta,w)][1]+=ok
print('"'exact exhaustive coefficient grid A_i in [-2,2], lc "'!= 0'"')
print('systems tested:',total,'solutions:',sol,'C cap = w*deg(A)+4')
print('by (degA,w):',sorted(by.items()))
# char-p failure control
for p in (2,3,5,7):
    # A=y"'^p-y, C=1, w=1: -A'"'=1 in F_p
    deriv_coeff=(-1)%p
    lhs=(-deriv_coeff)%p
    print(f'F_{p}: A=y"'^{p}-y, C=1, w=1 gives c={lhs}'"')
PY" in /Users/dc/code/math/jc72108
 succeeded in 14298ms:
exact exhaustive coefficient grid A_i in [-2,2], lc != 0
systems tested: 12400 solutions: 0 C cap = w*deg(A)+4
by (degA,w): [((2, 1), [100, 0]), ((2, 2), [100, 0]), ((2, 3), [100, 0]), ((2, 4), [100, 0]), ((3, 1), [500, 0]), ((3, 2), [500, 0]), ((3, 3), [500, 0]), ((3, 4), [500, 0]), ((4, 1), [2500, 0]), ((4, 2), [2500, 0]), ((4, 3), [2500, 0]), ((4, 4), [2500, 0])]
F_2: A=y^2-y, C=1, w=1 gives c=1
F_3: A=y^3-y, C=1, w=1 gives c=1
F_5: A=y^5-y, C=1, w=1 gives c=1
F_7: A=y^7-y, C=1, w=1 gives c=1

exec
/bin/zsh -lc 'git status --short; git diff -- MATHIEU.md MATHIEU-REVIEW.md RESIDUE.md LEMMA.md' in /Users/dc/code/math/jc72108
 succeeded in 0ms:
?? ops/stuck7_verdicts.sh

codex
The convention trace agrees in the anchor case: for \(k=d_2=2\), solving the normalized inner column gives \(c_2=a_2/2,\ c_3=a_3,\ c_4=0\), and the sole leftover is \(-a_3^2\), exactly the relation recorded in `LEMMA.md`. I also found one harmless typo in the valuation remark, not in the proof: it drops the factor \(c\) from \(dt=c\,dy/A^{w+1}\).
exec
/bin/zsh -lc 'PYTHONDONTWRITEBYTECODE=1 python3 cases/residue_check.py mathieu' in /Users/dc/code/math/jc72108
 succeeded in 153ms:
M1 rigidity dichotomy (extras==0 <=> deg A<=1), k=1..5, d2=2..5, all deg A, random/power/mixed A: OK
M2 bridge: y^((k+1)d-1) not in Im(L_A) (properness), and 1 in Im(L_A) <=> deg A<=1, k=1..4, deg A=1..4: OK
M3 CT form: a2^(2d2) beta_(k+2) == (-1)^k R (R is the Laurent constant term CT_w(beta' w^-(k+1))), 12 cells: OK
M4 Theorem A identities: L_A(A^k)==0 and lc(L_A(D))==(deg D - k deg A) lc(A) lc(D), symbolic, k,deg A=1..4: OK
M5 (2,2): binomial extras==0: OK | perfect-power nonzero: OK | random off-binomial nonzero: OK | paths agree: OK
M5 (2,3): binomial extras==0: OK | perfect-power nonzero: OK | random off-binomial nonzero: OK | paths agree: OK
M5 (3,3): binomial extras==0: OK | perfect-power nonzero: OK | random off-binomial nonzero: OK | paths agree: OK
M5 (3,4): binomial extras==0: OK | perfect-power nonzero: OK | random off-binomial nonzero: OK | paths agree: OK
M5 (4,4): binomial extras==0: OK | perfect-power nonzero: OK | random off-binomial nonzero: OK | paths agree: OK
M5 (5,4): binomial extras==0: OK | perfect-power nonzero: OK | random off-binomial nonzero: OK | paths agree: OK
M5 (2,5): binomial extras==0: OK | perfect-power nonzero: OK | random off-binomial nonzero: OK | paths agree: OK
M5 (3,5): binomial extras==0: OK | perfect-power nonzero: OK | random off-binomial nonzero: OK | paths agree: OK
M5 (2,6): binomial extras==0: OK | perfect-power nonzero: OK | random off-binomial nonzero: OK | paths agree: OK
MATHIEU OK

2026-08-12T20:04:09.921901Z ERROR codex_core::tools::router: error=timeout_ms must be at least 10000
collab: Wait
collab: Wait
codex
CONFIRMED

1. [MATHIEU.md:287–292](/Users/dc/code/math/jc72108/MATHIEU.md:287), Step 1. For \(\delta=\deg A\), \(d=\deg D\),
   \[
   AD'-wA'D=\sum_{i,j}(j-wi)a_i d_jy^{i+j-1}.
   \]
   Degree \(\delta+d-1\) is reached uniquely by \((i,j)=(\delta,d)\), with coefficient
   \[
   (d-w\delta)\operatorname{lc}(A)\operatorname{lc}(D).
   \]
   Thus, in characteristic \(0\), the image has exactly that degree whenever \(d\ne w\delta\).

2. [MATHIEU.md:294–306](/Users/dc/code/math/jc72108/MATHIEU.md:294), Steps 2–4. Assuming \(\delta\ge2\), a constant nonzero image forces \(\deg C=w\delta\). Subtract
   \[
   D=C-\frac{\operatorname{lc}(C)}{\operatorname{lc}(A)^w}A^w.
   \]
   Since \(L_A(A^w)=0\), \(L_A(D)=c\), while \(\deg D<w\delta\). If \(D=0\), then \(c=0\); otherwise
   \[
   \deg L_A(D)=\delta+\deg D-1\ge\delta-1\ge1,
   \]
   again impossible. This exhausts all degree configurations, including constant \(C\), \(\deg C<\deg A\), and cancellation below the leading term.

3. Theorem A uses neither \(A(0)=1\), algebraic closure, nor root multiplicities. Repeated roots, \(A(0)=0\), and arbitrary characteristic-zero fields cause no exception. Both assumptions are essential: if \(c=0\), \(C=\lambda A^w\) works for arbitrary \(A\); in characteristic \(p\),
   \[
   A=y^p-y,\quad C=1,\quad w=1
   \]
   gives \(AC'-A'C=1\) with \(\deg A=p\).

4. [MATHIEU.md:162–179](/Users/dc/code/math/jc72108/MATHIEU.md:162), Lemma B. Under the stated post-gap-kill strip conventions,
   \[
   [xA,x^kC]=x^k(AC'-kA'C),
   \]
   and \((1,i),(k,j)\) contributes \((j-ki)a_ic_jy^{i+j-1}\). With \(0\le i\le d_2\), \(1\le j\le kd_2\), the coefficient of \(y^n\), \(1\le n\le kd_2-1\), pivots on
   \[
   (n+1)c_{n+1},
   \]
   using only earlier \(c_j\). The remaining \(d_2-1\) equations are exactly \(n=kd_2,\ldots,(k+1)d_2-2\). The sole higher possible coefficient has \(n=(k+1)d_2-1\), unique pair \((d_2,kd_2)\), and weight \(kd_2-kd_2=0\). No coefficient is missed, including when \(\deg A<d_2\).

5. [MATHIEU.md:180–186](/Users/dc/code/math/jc72108/MATHIEU.md:180), converse. Two supported witnesses differ by \(K\) satisfying
   \[
   (K/A^k)'=0.
   \]
   In characteristic \(0\), \(K=\lambda A^k\). Both witnesses have zero constant term and \(A^k(0)=1\), hence \(\lambda=0\). Therefore the triangularly solved column is the unique witness.

6. [LEMMA.md:13–44](/Users/dc/code/math/jc72108/LEMMA.md:13) uses actual bracket keys, whereas MATHIEU uses Minkowski points: \((k+1,s)\) corresponds to bracket key \((k,s-1)\). At \(k=d_2=2\),
   \[
   c_2=a_2/2,\qquad c_3=a_3,\qquad c_4=0,
   \]
   and the inner leftover is \(-a_3^2\), exactly LEMMA’s key \((2,4)\). It is distinct from LEMMA’s outer surplus key \((3,6)\); no sign or off-by-one error occurs.

7. Lemma B is valid only with the reduced-strip, gap-kill, full-column, \(d_1=1\), no-\(y\)-axis hypotheses recorded at [MATHIEU.md:462–464](/Users/dc/code/math/jc72108/MATHIEU.md:462). Outside them, extra terms such as \(2BD'-(k-1)B'D\) can enter the same column. This is a scope dependency, not a gap. Minor wording error at line 171: the cap on \(C\) comes from Q-column support, not from \(\deg A\le d_2\).

8. Exact searches found no counterexample: 12,400 rational systems with \(w=1,\dots,4\), \(\deg A=2,\dots,4\), and \(\deg C\le w\deg A+4\); plus 23,400 direct block computations covering \(k=1,\dots,6\), \(d_2=2,\dots,5\), coefficient values \(\{-2,-1,0,1,2\}\), including degree drops. Extras vanished exactly when \(\deg A\le1\). The repository’s exact `mathieu` suite also passed.

9. Harmless typo at [MATHIEU.md:311](/Users/dc/code/math/jc72108/MATHIEU.md:311): for \(t=C/A^w\), the equation gives
   \[
   dt=c\,dy/A^{w+1},
   \]
   not \(dy/A^{w+1}\). Since \(c\ne0\), the valuation argument is unchanged. No files were modified.
tokens used
202,360
CONFIRMED

1. [MATHIEU.md:287–292](/Users/dc/code/math/jc72108/MATHIEU.md:287), Step 1. For \(\delta=\deg A\), \(d=\deg D\),
   \[
   AD'-wA'D=\sum_{i,j}(j-wi)a_i d_jy^{i+j-1}.
   \]
   Degree \(\delta+d-1\) is reached uniquely by \((i,j)=(\delta,d)\), with coefficient
   \[
   (d-w\delta)\operatorname{lc}(A)\operatorname{lc}(D).
   \]
   Thus, in characteristic \(0\), the image has exactly that degree whenever \(d\ne w\delta\).

2. [MATHIEU.md:294–306](/Users/dc/code/math/jc72108/MATHIEU.md:294), Steps 2–4. Assuming \(\delta\ge2\), a constant nonzero image forces \(\deg C=w\delta\). Subtract
   \[
   D=C-\frac{\operatorname{lc}(C)}{\operatorname{lc}(A)^w}A^w.
   \]
   Since \(L_A(A^w)=0\), \(L_A(D)=c\), while \(\deg D<w\delta\). If \(D=0\), then \(c=0\); otherwise
   \[
   \deg L_A(D)=\delta+\deg D-1\ge\delta-1\ge1,
   \]
   again impossible. This exhausts all degree configurations, including constant \(C\), \(\deg C<\deg A\), and cancellation below the leading term.

3. Theorem A uses neither \(A(0)=1\), algebraic closure, nor root multiplicities. Repeated roots, \(A(0)=0\), and arbitrary characteristic-zero fields cause no exception. Both assumptions are essential: if \(c=0\), \(C=\lambda A^w\) works for arbitrary \(A\); in characteristic \(p\),
   \[
   A=y^p-y,\quad C=1,\quad w=1
   \]
   gives \(AC'-A'C=1\) with \(\deg A=p\).

4. [MATHIEU.md:162–179](/Users/dc/code/math/jc72108/MATHIEU.md:162), Lemma B. Under the stated post-gap-kill strip conventions,
   \[
   [xA,x^kC]=x^k(AC'-kA'C),
   \]
   and \((1,i),(k,j)\) contributes \((j-ki)a_ic_jy^{i+j-1}\). With \(0\le i\le d_2\), \(1\le j\le kd_2\), the coefficient of \(y^n\), \(1\le n\le kd_2-1\), pivots on
   \[
   (n+1)c_{n+1},
   \]
   using only earlier \(c_j\). The remaining \(d_2-1\) equations are exactly \(n=kd_2,\ldots,(k+1)d_2-2\). The sole higher possible coefficient has \(n=(k+1)d_2-1\), unique pair \((d_2,kd_2)\), and weight \(kd_2-kd_2=0\). No coefficient is missed, including when \(\deg A<d_2\).

5. [MATHIEU.md:180–186](/Users/dc/code/math/jc72108/MATHIEU.md:180), converse. Two supported witnesses differ by \(K\) satisfying
   \[
   (K/A^k)'=0.
   \]
   In characteristic \(0\), \(K=\lambda A^k\). Both witnesses have zero constant term and \(A^k(0)=1\), hence \(\lambda=0\). Therefore the triangularly solved column is the unique witness.

6. [LEMMA.md:13–44](/Users/dc/code/math/jc72108/LEMMA.md:13) uses actual bracket keys, whereas MATHIEU uses Minkowski points: \((k+1,s)\) corresponds to bracket key \((k,s-1)\). At \(k=d_2=2\),
   \[
   c_2=a_2/2,\qquad c_3=a_3,\qquad c_4=0,
   \]
   and the inner leftover is \(-a_3^2\), exactly LEMMA’s key \((2,4)\). It is distinct from LEMMA’s outer surplus key \((3,6)\); no sign or off-by-one error occurs.

7. Lemma B is valid only with the reduced-strip, gap-kill, full-column, \(d_1=1\), no-\(y\)-axis hypotheses recorded at [MATHIEU.md:462–464](/Users/dc/code/math/jc72108/MATHIEU.md:462). Outside them, extra terms such as \(2BD'-(k-1)B'D\) can enter the same column. This is a scope dependency, not a gap. Minor wording error at line 171: the cap on \(C\) comes from Q-column support, not from \(\deg A\le d_2\).

8. Exact searches found no counterexample: 12,400 rational systems with \(w=1,\dots,4\), \(\deg A=2,\dots,4\), and \(\deg C\le w\deg A+4\); plus 23,400 direct block computations covering \(k=1,\dots,6\), \(d_2=2,\dots,5\), coefficient values \(\{-2,-1,0,1,2\}\), including degree drops. Extras vanished exactly when \(\deg A\le1\). The repository’s exact `mathieu` suite also passed.

9. Harmless typo at [MATHIEU.md:311](/Users/dc/code/math/jc72108/MATHIEU.md:311): for \(t=C/A^w\), the equation gives
   \[
   dt=c\,dy/A^{w+1},
   \]
   not \(dy/A^{w+1}\). Since \(c\ne0\), the valuation argument is unchanged. No files were modified.
