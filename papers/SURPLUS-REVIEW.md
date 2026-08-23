# SURPLUS-REVIEW.md — Adversarial review of SURPLUS.md + cases/surplus_count.py

Reviewer: Claude (adversarial pass, 2026-08-04). Status: COMPLETE.
Verdicts: 1 CONFIRMED, 2 CONFIRMED, 3 CONFIRMED (one corollary refuted as
written), 4 OBSERVED/WEAKENED, 5 WEAKENED. Overall: SURPLUS.md stands.

## 1. Reproduction + 4 new stress families
Verdict: CONFIRMED (one scope subtlety at k=1, see below and Front 2)

New families (reviewer-constructed, /tmp/rev_new.py, run through the repo engine):

| family | k | d2 | gap side | widths | predicted | got |
|---|---|---|---|---|---|---|
| nf_minimal (strips cut to block only, P ends x=2, Q x=3) | 2 | 2 | Q | 2,3 | 9/8/1 PINS -1/5 a2^2 a6 @(4,7) | EXACT match |
| nf_gapP (gap on P side, fresh corner data) | 2 | 2 | P | 2,3 | swap then 9/8/1 PINS | EXACT match (swapped=True) |
| nf_k3_d3 (new lengths) | 3 | 3 | Q | 3,8 | scope map 21/17/4 OTHER solvable | EXACT match |
| nf_k1_d2 (no-gap cell ABSENT from scope map) | 1 | 2 | none | 2,1 | my hand count 5/4/1, leftover (3,5) OTHER (a2a5/(2a1)-2a6)b_q0 | EXACT match |

- Scope map correctly predicts every constructed outcome, including the extreme
  minimal-length strips (strongest possible confirmation of "any strip lengths").
- Prop A formula 2(wP+wQ)-1 held on all 6 reviewer families.
- k=1 caveat: the "gap side = x-max" normalization is UNDEFINED at k=1 (both
  bottom corners have x=1); raw counts are labeling-dependent there (Front 4).

Reproduction (2026-08-04, this machine): `python3 cases/surplus_count.py` and `scan`
both exit 0. All 6 table rows reproduce at depth 2: open/swap/mini 9/8/1 PINS
`-1/5*unit*a(1,1)^2*a(2,4)` at (4,7); reg 9/8/1 TRIVIAL (3,8); toy_k3 13/12/1
TRIVIAL (5,9); toy_w3 15/11/4 OTHER, probe "NO torus point". All 16 scan cells
match the scope map byte-for-numbers. Presentation nick: the default-mode summary
table prints toy rows at escalated depth D=5 (34/30/4, 39/29/10), not the depth-2
numbers the SURPLUS.md table quotes; depth-2 values appear only in the per-family
log lines. Not an error (D column discloses it), but easy to misread.

## 2. Independent re-derivation of Propositions A and B
Verdict: CONFIRMED (exact agreement; two scope sharpenings)

Method (/tmp/rev_indep.py, written from scratch, deliberately different
formulation): strips enumerated parametrically (no hulls); the near-origin
system treated as a LINEAR system M(a)b=0 over Q[a] in all Q-side coefficients
of columns 1..k+1 (gap columns included — gap-kill NOT assumed); obstruction
tested as exact-rank rowspace membership "b_q0 = 0 on every solution" at random
rational points; residuals via fraction-free cross-multiplication (no unit
inversion, no M2, no cascade).

- Prop A (n_keys = 2(wP+wQ)-1): CONFIRMED on my own enumeration for the full
  grid k=1..5, d2=1..4, plus the k=1 reverse labeling. No exceptions.
- Prop B (2wQ+1 unit-pivot eliminations, pivot = q_y * a_p0, unique): CONFIRMED
  structurally 100% in the normalized orientation, all 20 grid cells.
- Gap-kill: independently CONFIRMED by rank tests (every gap b forced to 0).
- Sharpening 1 (k=1 scope): the doc's "gap side = bottom-corner x-max"
  normalization is UNDEFINED at k=1 (both corners have x=1). In the reg
  labeling (p0=(1,1), q0=(1,0)) Prop B fails at exactly one point:
  q=(1,1) has pivot det((1,1),(1,1)) = 0 (this is reg's known free b2). There
  the Q-elim count is 2wQ (=6), not 2wQ+1, and the Corollary formula
  2(wP-1)-z gives 0 while the actual raw surplus is 1. Props A/B are stated
  under the normalization so they are not false, but the doc's table and note 1
  silently apply raw-count language to reg, whose labeling the propositions do
  not cover. The raw count at k=1 is labeling-dependent (see Front 4).
- Sharpening 2 (char): Prop A/B counts use integer dets (q_y, k*w, pivots);
  over small positive characteristic rows/pivots can vanish, so both
  propositions implicitly assume char 0 or char outside the dets used. Unstated.
- Main-theorem cross-check by linear algebra (no cascade): at generic a,
  b_q0 is forced to 0 (obstruction) for every cell tested, incl. (2,2); the
  consistency locus for (2,2) is EXACTLY {a3=0 and (a2=0 or a6=0)}: rank tests
  give solvable at (a3=0,a2=0) and (a3=0,a6=0), obstructed at a3=0-generic and
  at (a2=a6=0, a3 generic). Fraction-free residuals (gap columns then killed):
  row (3,5) -> -2*a3^2 * b_q0; row (4,7) -> (10*a2*a3*a5 - 2*a2^2*a6
  - 32*a1*a3*a6) * b_q0, which at a3=0 is -2*a2^2*a6*b_q0. Exact match with
  the doc's cascade and with my separate hand back-substitution.
- Bonus: inner-extra pattern for d2=2, k=2..5 reproduced fraction-free:
  -2a3^2, -5a1a3^3, -14a1a3^4, -42a1a3^5 (unit cofactors; 2,5,14,42 = 2*Catalan)
  — confirms the doc's "-a3^k b_q0 a1^{1-k}, verified k<=5".

## 3. Main theorem proof, (k,d2)=(2,2): step-by-step audit
Verdict: CONFIRMED at variety level; one stated corollary (chart-free ideal
membership) is REFUTED as literally written — radical membership only.

Step-by-step (all re-derived by hand, then machine-checked twice):
1. Enumeration {p0,q0}={(1,0),(k,1)} from (i): re-proved (b in {0,1};
   a-b(k+1)=+-1 forces the two splits; negatives excluded). OK.
2. Gap-kill: proof sound. Note it needs y invertible for every gap point
   (y in {1,2} at (2,2), i.e. char != 2 — inside the claimed set). OK.
3. Block self-containment: re-proved for arbitrary strip lengths (any pair with
   j>=3 hits a dead gap column; j=0 hits the origin, det=0). "ANY lengths"
   is PROVED, and confirmed empirically down to minimal strips (nf_minimal).
4. All 9 displayed block equations verified monomial-by-monomial by hand
   (independent det computations). All coefficients correct.
5. Reduction lines incl. cancellations [C1],[C2] verified by hand AND by
   fraction-free linear algebra. Important subtlety found: [C2] does NOT need
   a3=0 (the a3-terms cancel identically: 3a3b7 - 2a4b5 = 0 and
   -a2b8 + 2a5b4 = 0 pre-substitution); the displayed proof routes [C2]
   through "after a3=0", which is correct but weaker than what is true.
6. M2 at (3,5): the reduced form is -(a3^2)b3/a1, QUADRATIC in a3. Setting
   a3:=0 is a variety/radical step (a3^2 in the ideal, a3 not). Consequences:
   - The "Chart-free restatement" ("unit*a2^2*a6*b_q0 lies in the block ideal +
     gap-kill ideal") is FALSE as literally stated. Witness: over K[eps]/(eps^2)
     set a3=eps, a2=1, a6 = eps*c: all block+gap+vertex equations are
     satisfiable while a2^2*a6*b_q0 = eps*c*b_q0 != 0. What is true (and what
     the geometric conclusion needs): u := unit*a2^2*a6*b_q0 satisfies
     u = -(1/2)*residual(4,7) + a3*(...), and a3^2 in the ideal, so u^2 in the
     ideal — RADICAL membership. Same correction applies to LEMMA.md's
     "a2^2 a6 in I(core)" if I(core) is read as the generated ideal (fine if
     I(core) means the ideal of the core variety). LEMMA.md sec 2.2's "key (2,4)
     reduces to (unit)*a3" has the same imprecision: exponent is 2
     (block-local and full-system alike); LEMMA-REVIEW did not catch it.
   - The theorem's own conclusion ("the chart inverting {a2,a6} is empty",
     "forces a2^2 a6 = 0" at points) is variety-level and CORRECT.
7. Bookkeeping 9-8=1, position rule (k+2, d2(k+2)-1)=(4,7): correct; position
   rule also matches every reviewer family (incl. (3,5) at k=1,d2=2 and (3,8)
   at reg).
8. Char exclusions {2,3,5}: exactly the primes in {gap pivot 2; block pivots
   2,3,4,3,4,5,6; final 1/5} — needed for THIS derivation and sharp for it
   (each of 2,3,5 occurs); claim that 7,11,13 are not needed is verified
   block-locally. Empirically (mod-p rank tests at random points, p=2,3,5,7,
   11,101) the generic-a obstruction persists even at p in {2,3,5}, so the
   exclusions are proof-technical, not intrinsic — consistent with the doc's
   phrasing, which only asserts validity outside {2,3,5}.
9. fix_ones: the block derivation uses only a_p0, b_q0 as units (hypothesis
   (i)); no dependence on LEMMA.md's far-corner fix_ones normalization, in
   either the script or my re-derivation. Confirmed non-issue.
10. Unimodularity: used exactly twice (units from the vertex equation; the
    enumeration in step 1). No hidden further use.
Minor: "Machine check: reproduces every line above exactly (assertion-locked)"
overstates — assertions lock surplus=1, PINS class, and the monomial a2^2*a6,
not each displayed line (the lines are nevertheless correct).

## 4. Content-vs-count discriminator: proved or observed?
Verdict: OBSERVED (doc says so, honestly) — and WEAKENED as a general no-gap
statement: "leftover content == 0" is special to reg's family AND labeling.

- Status in the doc: "leftover reduces to 0" for reg is an empirical run
  outcome with a mechanism sketch (its P-side inputs are M2-zeroed), not a
  proof. The doc's scope map contains NO k=1 row; condition (iii) is correctly
  stated content-wise ("(unit)*M*b_q0 with M nonzero"). Honest.
- New no-gap test 1, reg_swap (reg with P,Q swapped — the SAME pair up to
  [Q,P]=-x, a legal relabeling since bracket sign is count-irrelevant per the
  doc's own Method): raw counts CHANGE: 9 keys / 7 unknowns / surplus 2;
  leftovers = (3,8) TRIVIAL + (3,7) OTHER (4 monomials, torus-solvable).
  So even for reg's geometry, "leftover reduces to 0" is labeling-dependent,
  and the raw count 1 quoted in note 1 is too (1 vs 2).
- New no-gap test 2, nf_k1_d2 (k=1, d2=2): leftover (3,5) is OTHER:
  (a2a5/(2a1) - 2a6)*b_q0 — content nonzero but torus-solvable (verified
  independently: rank test solvable exactly on {a3=0, a2a5=4a1a6}).
- Conclusion: what survives every test is the PINS-based discriminator (an
  obstruction leftover (unit)*(nonzero monomial)*b_q0 vs anything else), which
  is how the doc states condition (iii). What does NOT survive is the stronger
  narrative "no-gap => leftover content 0": no-gap families can leave genuine
  nonzero P-constraints. Also note (Front 2): my linear-algebra view shows even
  reg's block FORCES a(1,2)=a(1,3)=0 (a support restriction on P); "no
  obstruction" means only that b_q0 stays free AFTER those forced zeroings.
  A paper write-up should state the k=1 side as observed-only, labeling-
  sensitive, and restricted to the families computed.

## 5. Consistency with FACE-ISOLATION.md TL1
Verdict: WEAKENED — no disagreement on any family computed in both documents,
but TL1's general claim is falsified by SURPLUS's own scan, and SURPLUS.md
explicitly supersedes it. FACE-ISOLATION.md itself still needs an erratum.

- Same claim? Same intended claim (LEMMA condition (iii) as a counting
  criterion on the same near-origin block: Q-cols (q0)_x..+1, P-cols 1..2 —
  block definitions match). TL1 asserts it for ALL widths given (i)+(ii);
  SURPLUS proves it exactly for (k,d2)=(2,2) and refutes it elsewhere.
- Families in both test sets: open, swap, mini — TL1 predicts surplus 1 +
  (unit)*M*b_q0: agrees with SURPLUS (PINS -1/5 a2^2 a6). reg — TL1's (ii)
  fails, TL1 silent; SURPLUS raw 1 TRIVIAL: no conflict. Full agreement.
- TL1 refuted outside (2,2) (all verified independently this review):
  (3,2),(4,2),(5,2): count = 1 but M = 0 (TRIVIAL — TL1's "M a monomial",
  i.e. the obstruction form, fails); (2,3),(3,3): surplus 4; (2,4),(3,4): 6 —
  TL1's "= 1" fails outright. toy_k3 and toy_w3 satisfy TL1's hypotheses and
  break its conclusion.
- Formulation gap (level filtration vs direct counting): TL1's filtration
  L_Lambda = <d-perp,.> is the w-stratum grading; but the well-founded pivot
  order that makes the elimination triangular is l = d2*x+y (SURPLUS Prop B).
  TL1 conflates the two. Also "the surplus key at the block's top
  Lambda-stratum" is ambiguous: there are TWO top (w=1) keys; SURPLUS shows
  the inner one is the a3-M2 event and the OUTER one (k+2, d2(k+2)-1) is the
  surplus. TL1 as stated cannot distinguish them, and its "no elimination run
  needed" promise is contradicted by the fact (SURPLUS note 1, confirmed here)
  that the bare count equals 1 even at k=1/reg where no obstruction exists —
  content, which requires the reduction, decides.
- SURPLUS.md's Status paragraph states the correct relationship ("TL1 ... TRUE
  as stated only in the (2,2) cell; correct general form is torus-emptiness").
  Nothing in FACE-ISOLATION.md records this; TL1 there is labeled candidate-
  grade, so not an error, but it should be annotated to prevent drift.

## Overall verdict

SURPLUS.md SURVIVES adversarial review unusually well. Reproduction is exact
(6/6 table rows, 16/16 scan cells); Propositions A and B are independently
re-proved (own enumeration, own linear-algebra formulation) with zero
discrepancies inside their stated scope; the (2,2) main theorem's equations,
cancellations, obstruction monomial a2^2*a6, obstruction locus
{a3=0}∩({a2=0}∪{a6=0}), char set {2,3,5} (sharp for the proof), strip-length
freedom, and gap-side symmetry were each confirmed by at least two independent
routes; the scope map correctly predicted all four reviewer-constructed
families including minimal-length strips and a P-side gap.

Defects found (all repairable, none fatal to the (2,2) theorem):
1. REFUTED as written: the "chart-free restatement" — unit*a2^2*a6*b_q0 is in
   the RADICAL of block+gap ideal, not the ideal (dual-number witness; the
   a3-elimination is quadratic: -a3^2*b3/a1). Same exponent imprecision in
   LEMMA.md sec 2.2 ("(unit)*a3"). One-line fixes; variety-level conclusions
   unaffected.
2. k=1 scope gap: the gap-side normalization is undefined at k=1; Prop B and
   the Corollary do not cover reg's labeling (pivot det = 0 at q=(1,1)); raw
   counts at k=1 are labeling-dependent (reg 1 vs reg_swap 2). Note 1's k=1
   claims are family- and labeling-specific.
3. The no-gap "leftover content == 0" is observed, not proved, and is NOT a
   general no-gap fact (reg_swap and nf_k1_d2 leave genuine nonzero,
   torus-solvable P-constraints). The doc's PINS-based statement of (iii)
   survives; the reg anecdote should not be generalized.
4. Props A/B silently assume characteristic 0 (or char avoiding the integer
   dets). Unstated.
5. Cosmetic: duplicated empty section headers ("Notes per family", "Key
   count", "Unknown count"); default-mode summary table prints deep-block
   counts for the toy rows.

WEAKEST STEP: the chart-free ideal-membership sentence (the only literally
false statement found), with the a3^2/radical subtlety it hides; runner-up:
resting the count-vs-content contrast for k=1 on the single reg family in a
labeling the propositions don't cover.

PAPER-READINESS (joint SURPLUS.md + LEMMA.md write-up of the vertex-gap
theorem, (2,2) regime): YES — ready for paper-grade drafting after the small
errata above. The full chain (i)-enumeration -> gap-kill -> Props A/B ->
explicit block reduction -> obstruction (unit)*a2^2*a6*b_q0 -> empty chart is
now proved from corner data alone for (k,d2)=(2,2), any strip lengths, char
not in {2,3,5}, side-symmetric, and is machine-verified three independent
ways. Outside (2,2) the document's own scope map honestly marks (iii) as
failing (k>=3, d2=2), absent (d2=1), or changing form with numeric-only
evidence (d2>=3) — keep those out of the theorem statement, keep the
torus-emptiness conjecture clearly labeled, and add the TL1 erratum to
FACE-ISOLATION.md.

Reviewer artifacts: /tmp/rev_new.py, /tmp/rev_indep.py, logs
/tmp/rev_{default,scan,new}.log (run 2026-08-04, CPython 3, this machine).
