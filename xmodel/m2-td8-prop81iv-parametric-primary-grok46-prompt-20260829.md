# Grok 4.6 primary research — td=8 affine family, Prop. 8.1(iv)

Work as an equal primary researcher, independently of the active Opus lane.
Repository root: `/Users/dc/code/math/jc2`. Write the durable report:

`xmodel/m2-td8-prop81iv-parametric-primary-grok46-20260829.md`

You may also create a small exact-arithmetic packet only at:

`cases/m2_td8_prop81iv_parametric_grok46_20260829/`

Read and verify:

- `xmodel/m2-td8-equal-join-route-family-sol56-20260829.md`;
- `xmodel/m2-td8-equal-join-route-family-hostile-review-grok46-20260829.md`;
- `cases/m2_td8_equal_join_route_family_r1_20260829/`;
- the precise Prop. 8.1/Not. 8.1 definitions in local
  `refs/sigray_full.pdf` (printed pp. 39--41), not only campaign paraphrases;
- the directly relevant derivations/engines in `ladder/SHEET6-L1.md`,
  `ladder/SHEET6-A3L1-REVIEW.md`, `ladder/SHEET6-MULTIPOLE.md`,
  `ladder/BOOK-OFFAXIS.md`, `ladder/BOOK-OFFAXIS-REVIEW.md`, and
  `cases/l1_ode_check.py`.

Do not read any Opus output produced after this prompt. Derive the object
cleanly from the printed identity
`delta*p*q' - (1-u)*p'*q = constant*p` and its surrounding hypotheses.
First pin the correct full/reduced normalization, degrees, orbit/root shapes,
`delta`, `u`, exponent `i`, coefficient field, and nonzero constant for the
affine cell

`nu=4+3t, (dp,dq,M,kbar,X,rho,w)=(24+18t,9+6t,3,6+4t,16+12t,2/3,4/3)`.

Then solve the coefficient problem uniformly in integer `t>=0`, or reduce it
to a rigorously specified finite exceptional set / decidable recurrence.
The preferred outcomes, in order, are: a uniform log/residue obstruction; an
exact classification of exceptional `t`; an explicit admissible formal
solution family; or a minimal symbolic recurrence whose first unresolved
condition is stated and tested. Check every printed root/eta/simple-root/
nonzero-constant condition, not just the ODE coefficients. Distinguish:

1. local formal cell survival/death under Prop. 8.1(iv);
2. exact lambda cost versus recorded lower bound;
3. source landing or geometric realizability;
4. any degree-bound or JC2 consequence.

Use exact rational/integer arithmetic. A bounded Python/SymPy experiment is
allowed locally; no Singular, msolve, Sage, PARI, long/high-memory process, or
AWS launch. If the honest computation is heavy, emit a source-ready AWS
design and stop before launch. Ordinary and `-O` tests plus adversarial
mutations are required for any code packet. Include full/body hashes,
reproduction commands, a clause-level claim firewall, and an explicit
`PROVED` / `DISPROVED` / `PARTIAL` verdict.

Hard boundaries: no web, commit, push, or canonical edits. Never access,
list, search, build, status, or control `jc2-lean`; never run global
`git status` or a workspace-wide search. Modify only the named report and
optional packet; use `/tmp` for scratch.
