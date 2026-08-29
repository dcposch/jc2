You are Grok 4.6 acting as an independent hostile mathematical reviewer in the
Plane Jacobian Conjecture campaign. Work only in /Users/dc/code/math/jc2.
Never enter, enumerate, search, read, build, status, modify, or control any
jc2-lean path. Use local files only; no web, AWS, or heavy computation.

Review this producer from first principles:

  xmodel/qe5-delta0-state-slot-map-r1-sol56-20260829.md

Read every local source on which a load-bearing formula depends, especially
the exact cited ranges in ladder/BOOK-OFFAXIS.md, ladder/SHEET6-DEPTH.md,
ladder/SHEET6-III.md, ladder/SHEET6-MULTIPOLE.md, ladder/TOWER-UNIFORM.md,
xmodel/m2-caseiii-two-pole-e5-local-index-r3-repair-fable5-20260829.md,
xmodel/m2-caseiii-two-pole-e5-local-index-r3-hostile-review-opus5-20260829.md,
and cases/book_offaxis.py. Verify source hashes rather than trusting the
producer's table.

Hostile-review every algebraic step and every scope transition. In particular:

1. Decide whether fixed (M_G, nu_G, kbar_G), together with the explicitly
   declared equal-state data, really determines X_G, the reduced ratio,
   (dp,dq), D, s, Sm, mmax, kmin, and the remaining pattern slots. Identify
   every hidden existence, sign, divisibility, or uniqueness assumption.
2. Re-derive Proposition 4.1, including D=nu_G*A, A>=s>=1,
   M_G*nu_G | D, the bound dq/D <= 2+1/(M_G*nu_G), and the finite K menu.
3. Prove or refute Proposition 5.1's bounded-positive-partition criterion.
   Check both Sm=0 and Sm>0, the strict-NE cap floor((dp-1)/dq), k<=s,
   q-only orbit count, S/R, and all edge cases.
4. Inspect cases/book_offaxis.py directly. Verify the claims that cell_check
   searches an unbound nu (including nu=1), omits gcd(kbar,nu)=1, and can
   accept the Section 6.2 profile only at nu=3 rather than forced nu_G=2.
5. Inspect the R3 producer directly and determine whether M_U is genuinely
   unbound in its migration sketch, whether this changes a theorem or only
   pseudocode, and the smallest exact repair.
6. Recompute all three controls and distinguish pattern-grammar existence
   from ODE, edge, source, polynomial, or Keller realization.

Return PASS, PASS_WITH_REPAIR, or FAIL. For every defect, give exact replacement
wording or the smallest formula repair and say whether any downstream
conclusion changes. Do not edit canonical ledgers or any file except your
review report. Write the report exactly to:

  xmodel/qe5-delta0-state-slot-map-hostile-review-grok46-20260829.md

Include exact source citations and SHA-256 hashes, invocation/model disclosure,
scope exclusions, review risks, and a seal defining the body as all bytes before
the literal `## Seal` heading with its body byte count and SHA-256. Do not
commit or push.
