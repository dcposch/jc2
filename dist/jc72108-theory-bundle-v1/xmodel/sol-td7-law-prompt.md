# Task: closed-form kill law for the td=7 off-axis book (62 cells)

You are GPT 5.6 Sol doing PRIMARY RESEARCH on the plane Jacobian Conjecture
campaign in /Users/dc/code/math/jc72108 (you have full read access).

## Context (read these, in this order; use offsets/limits, files are long)
1. `BOOK-OFFAXIS.md` sections 6-10 (the lambda-budget repair and the honest
   td-7 book: 62 fully pinned cells = 1 class-B (3,9) route + 61 class-C,
   all T1-rigidity targets; budget-equality routes 1390/1689).
2. `BOOK-BASH-R2.md` — the two known CLOSED-FORM kill laws on the on-axis
   book: ZCH cells die iff (nu+1) | l; family-I cells die iff l/r or r/l
   is an integer. Study HOW these were derived from Prop 8.1(iv) rigid
   solves.
3. `SHEET6-TEMPLATE.md` — the T1 rigidity mechanism (template-forced
   coefficient towers) and the E5-corrected w_i^4 formula (line ~239).
4. `SHEET6-LROOT.md` and `SHEET6-DEPTH.md` — the L6 primitivity law
   gcd(kappa_V, nu_V)=1 and the depth-closure invariant w=(kappa-rho)/nu,
   which pin the cell parameters.

## The question
For the 61 class-C pinned cells (and the single class-B route), derive a
closed-form arithmetic criterion — analogous to (nu+1)|l — that decides
Prop 8.1(iv) rigid-solve death directly from the cell parameters
(kappa, nu, l, r, lambda-budget data), WITHOUT running the per-cell
Groebner bash. Partial laws (covering a proper subset of the 62 with an
explicit exception list) are valuable too.

## Deliverable
Write `/Users/dc/code/math/jc72108/xmodel/sol-td7-law.md` containing:
- The criterion (theorem statement) with proof or proof sketch;
- Exactly which of the 62 cells it kills / leaves (list them);
- Every ingredient cited as file + section/line;
- Anything unproven labeled CONJECTURE in bold;
- A 5-line summary at top: LAW FOUND (full/partial/none), cells killed,
  confidence.

## Rules
- Do NOT modify any repo file except writing your one output file.
- Do NOT git commit or push.
- Honesty over optimism: a clean "no uniform law exists, here is the
  obstruction" is a valid and useful answer.
- All claims must be reproducible from the cited files; no invented cell
  data. If the 62-cell list itself is ambiguous in BOOK-OFFAXIS.md, say so
  precisely rather than guessing.
