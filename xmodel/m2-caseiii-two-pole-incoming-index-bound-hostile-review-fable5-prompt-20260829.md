# Hostile theorem review: two-pole case-III incoming-index bound

You are Fable 5 at maximum reasoning. Independently falsify or verify Sol's
new cap-free bound on the *incoming* zero-edge index at a two-pole case-III
merge. This result is intended to remove the legacy `NUCAP=500` fallback;
return PASS only if the literal sheet laws support that exact conclusion.

Read in full:

- `/Users/dc/code/math/jc2/xmodel/m2-caseiii-two-pole-incoming-index-bound-sol56-20260829.md`
  (full SHA-256
  `406e78d220b62910e6296866db998bd0e7d898b2e6a618fe0aa70ffbeb73fd46`,
  body `8a16cad9cc3211f90e86b1cc31a3fe2991f3817138ae9da4f6dbc56ddf7b5c43`);
- `/Users/dc/code/math/jc2/cases/m2_caseiii_two_pole_nuh_bound_r1_20260829/`
  in full;
- the exact R2.1/R2.2/P2 and case-III sources cited by the report in
  `ladder/BOOK-OFFAXIS.md`, `ladder/SHEET6-DEPTH.md`, and the relevant
  MULTIPOLE review;
- `/Users/dc/code/math/jc2/xmodel/m2-budget-quotient-primary-research-opus5-20260829.md`
  only to adjudicate the report's claimed `nu_G` versus incoming `nu_H`
  notation correction.

Do not access, list, search, build, status, or control `jc2-lean`. Do not run
`git status` or another workspace-wide command. No web, AWS, local Singular,
msolve, Sage, PARI, or heavy computation; no canonical edits; no commit/push.
Bounded exact-rational Python and source mutations are allowed. Do not modify
the packet or producer report.

Write only
`/Users/dc/code/math/jc2/xmodel/m2-caseiii-two-pole-incoming-index-bound-hostile-review-fable5-20260829.md`.

Mandatory charges:

1. Reconstruct from the source whether the stated two-pole pattern really is
   `dp=mu0+nu_G*(mu+Sm)`, `dq=1+nu_G*(1+k+lex)`, including the zero-root
   convention, q-only extras, and every case-III/case-II handshake. Check
   whether `m_j*dq<dp<mu*dq` and hence `m_j<=mu-1` is licensed for every
   cell in the claimed scope, including `nu_G=1` normalizations.
2. Audit all three multiplicity regimes. For `mu0>mu`, attack every step in
   `D=nu_G*A-delta`, `A>=s`, the two-case proof of
   `dq/D<=2*delta+3`, `kbar=mu*w*dq/D`, and
   `mu0*h*w0=delta*kbar+mu*w`. Look specifically for a missing pattern,
   wrong inequality direction, zero denominator, or hidden integrality/
   positivity assumption. Produce a literal countercell if one exists.
3. Decide whether the theorem bounds the incoming `h=nu_H` and whether
   Opus's provisional `nu<=mu0*num(w0)` argument instead binds only the
   merge-local `nu_G`. Trace symbols through the actual equations rather
   than accepting either report's prose.
4. Reproduce the charged `(mu,w)=(1,2)`, `(mu0,w0)=(2,3/2)` conclusion:
   `h<=4`, odd ray leaves only `h=3`, cell `(dp,dq,kbar,X)=(5,7,7,5)`,
   `M=1`. Check against the previously promoted td-7 source, not just the
   new script.
5. Run normal and optimized tests, independently mutate the sharpness case,
   and assess whether the 130,095 checks exercise the theorem rather than
   merely its implementation. State whether the constant 2*delta+3 is
   genuinely attained.
6. Give the exact safe engine consequence. A PASS may remove only the
   two-pole case-III incoming-index cap. It must not certify the old
   `cell_check`, equal nonzero joins, multipole/inner merges, full landing,
   a degree ceiling, or JC2.

Allowed verdicts: `PASS_AT_STATED_SCOPE`, `REPAIR_REQUIRED`, or `REJECT`.
Report findings in severity order, end with a body self-hash, and provide
full-report hash instructions.
