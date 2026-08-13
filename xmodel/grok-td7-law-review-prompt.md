# Hostile review: xmodel/sol-td7-law.md (td-7 closed-form kill law)

You are Grok 4.6, hostile referee, repo /Users/dc/code/math/jc72108
(full read access, python3 allowed).

Under review: GPT-5.6-Sol's claim of a FULL decision law for the
Prop. 8.1(iv) local rigid solve on the 62-cell td-7 book:
cell T1-DEAD iff d_p | d_q (iff M = d_p iff kbar in {3,4});
56/62 dead (class-B (3,9,2,3) + 55 class-C), 6 class-C exceptions
with explicit admissible solutions; on-axis ZCH law (nu+1)|ell
recovered as special case.

Attack list, priority order:
1. THE NORMAL FORM (its section "Proof" step 1): does Prop. 8.1(iv) +
   the P3 class-B/C pins really force p = eta^mu (t - A),
   q = eta (t - A) s(t), t = eta^nu, up to nonzero scalars? Check the
   cited BOOK-OFFAXIS.md lines (R1.0 209-224, R2.2 317-327, P3
   521-549) actually say what is claimed. A wrong normal form is the
   classic wrong-object failure here.
2. THE IFF, both directions: replay the symbolic argument (its (2)-(6)).
   Hunt for: divisibility off-by-one, the mu(ell+1)-1 arithmetic, the
   claim that merge arity r=2 never enters, and the boxed equivalence
   kbar in {3,4} <-> d_p | d_q (specific to td=7 pins — verify from the
   pin equations, not from the census).
3. CENSUS: run its reproduction block (px5.py + the perl line + the
   arithmetic). Confirm 61 class-C tuples, 55 dead, the exact 6
   exceptions it lists, and the route counts (1636/1689 removed;
   53 remaining routes, 35 budget-equality).
4. THE 6 EXCEPTIONS: verify its explicit admissible solutions actually
   satisfy the reduced equation with NONZERO rhs constant (substitute,
   exactly).
5. Its two citation corrections (L6 lives in SHEET6-III.md 121-129 not
   LROOT; route-count conventions 1713/1689, 1413/1390) — true or false?

Deliverable: /Users/dc/code/math/jc72108/xmodel/grok-td7-law-review.md,
VERDICT first line (SOUND / SOUND-WITH-ERRATA / BROKEN + one sentence),
findings ranked, each with how-checked. Modify no other repo file. No git.
