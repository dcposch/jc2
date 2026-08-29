# Hostile review: order-two generic-square `r=1` and symbolic unique-`AC`, `d=1`

You are the independent hostile reviewer. Work read-only except for the single
report named below. Do not run Singular, Sage, msolve, Lean, Groebner-basis
computations, or any heavy/exhaustive computation. Do not run a broad worktree
inventory; inspect only the named target and the exact transitive files its
freeze/compiler chain pins. Stored PASS markers are evidence, never authority.

Write exactly one report:

`xmodel/max12-812-order2-square-r1-d1-v12-hostile-review-grok-20260826.md`

## Frozen target and custody

- producer report
  `cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v12_recurrence_products_20260826/RESULT.md`,
  SHA `fe7a5c8a528b059c22118cc0256c180a9b455d8ba04637b5dc3ae2d3dbf95ae3`;
- evidence manifest in the same directory, `RESULTS.sha256`,
  SHA `f06671486459aeb34a797e64ea4f8572cd01728218bb526d419ed6d326eda72a`;
- source freeze `FREEZE.sha256`,
  SHA `decc00a91c952354902da2eeeeac6eb9c7fdc06748bf5f96957f45617e07743a`;
- registration SHA
  `a90bbc2ab84cc9c05c68b373f4b250152298cbf1f2f0a65afcf7bd96911a40c7`;
- V12 compiler SHA
  `cb1b07bb679c1149bc2671c2ed88417352c0708787f8362756ed3ffb12d3a88a`;
- exact-Q compiled `r=1` / D1 inputs:
  `e253681e155c0cbbc2c2984ecd6eeb7b5edfcb3e75b7b0c5649ec1051be7e5b3`,
  `9ea31841e78ffdf927509b4e15aa4505c7c31c0acfe39a32cb3f3040007f9845`;
- `F_65521` compiled `r=1` / D1 inputs:
  `e388c06b366dbcf083529861ad94de0184105125c90d8e4a595eb75c9d184bc3`,
  `73fd282452e7f4a1b8bcb708b8678ed7d1729246a88ea0641f34473c124dced5`;
- marker-only `r=1` stdout SHA on both fields:
  `8adb20f408c987d72d346224d92bfcbb2af441a2ee82107434d1caf3f0b1ef25`;
- marker-only D1 stdout SHA on both fields:
  `c56b388cfc8f3b4cee41c9976d55012662529b885693d9c1b83f7593db154044`;
- V12 exact-Q and modular validation SHA:
  `d58eedfdb10620e85b1a4c19f44366a6a2fcc03afaf79d36141f20fc89e77247`;
- lower-hull design authority
  `xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md`,
  SHA `c9ecfe4000092912464e29ecc526ac5c065f950778d31cac81f58fe06622954d`;
- arcwise closure criterion
  `xmodel/max12-812-order2-square-contact-raising-closure-criterion-20260826.md`,
  SHA `3c0a33ceddfad8ca69afb145ae5249f0d2b4866c5a8af498d257e9d4a78cfd95`.

First run only lightweight hash checks against `RESULTS.sha256`, verify both
AWS metadata records have engine `rc=0`, and inspect both validators and all
four actual stdout/stderr pairs. Trace the V12 compiler through every pinned
V11--V1 freeze/compiler ancestor needed to reach the original shared-Faber
source. A syntactically successful patch chain is not by itself a proof of
source typing.

## Load-bearing questions

Give an explicit verdict on every item and search for the smallest failing
coefficient, identity, hypothesis, or scope statement.

1. Does the ancestry really regenerate all seven source-tail rows with the
   reviewed generic-square first-normal substitutions, all lower loads,
   gauges, signs, row order, absolute grades, and denominator convention?
   Verify that neither the `r=1` nor D1 input is an analytic-only surrogate.
2. For the normalized `r=1` receiver, independently derive the grade-13
   proper part `(5/16) k0 R0^3/L0`, including every term that can enter at
   that grade. Is the seven-row source vector exactly related to its Laurent
   coefficients by an invertible lower-unitriangular transform?
3. Audit the exact-Q ideal/radical computation for `r=1`. Is localization on
   `D(p*k0)` actually represented, and does the radical force both
   coefficients of the linear `R0` to vanish? Distinguish set-theoretic
   support from scheme structure, and check that `R0=0` contradicts the
   registered nonzero leading section rather than silently changing contact.
4. For D1, verify the symbolic substitution
   `A=sigma^2 theta(A0+sigma A1)`,
   `C=sigma^3 theta(C0+sigma C1)`,
   `R=sigma^2 theta eta R0` and the interpretation
   `theta=sigma^n`, `eta=sigma^s`. Does it cover exactly
   `a=2+n,c=a+1,r=a+s` for all integers `n,s>=0`, without inverting or
   specializing away `theta` or `eta`?
5. Derive the lower-face comparison and prove the three successor modules
   are exhaustive: `(n,s)=(0,0)` gives `C2,RC,R3`; `n>=1,s=0` gives
   `C2,RC`; `s>0` gives `C2`. Check all tie inequalities against the pinned
   lower-hull theorem and audit every moving-`L`/moving-`p` connection term.
6. Verify complete source-to-Laurent identities at absolute grades 15 and 16,
   including the seven rows and recurrence/proper-numerator degree bounds.
   In particular, a hardcoded expected polynomial or two copies of the same
   analytic expression are not an independent source bridge.
7. Audit the etale splitting of `L0` on `D(p)`, the first `AC/L` root
   allocation, and all four explicit source-to-target ring maps. Check the
   27-source-variable image order, both deck orientations, injectivity/faithful
   base change needed for the conclusion, and the nonvanishing chart factors.
8. Recompute the grade-16 allocated-root residue. Is the unmatched value
   exactly `(3/2) lambda^2 cv^2 theta^2`, and is every possible `RC`, `R3`,
   moving-connection, higher-correction, or load term accounted for in all
   three modules? Verify why it is nonzero on the registered chart.
9. Audit the V1--V12 software history. Verify by byte-level comparison that
   V12 changes only one `z^3`, one `z^2`, and three `p^2` spellings in the
   recurrence region, preserves the mathematical polynomials and guards, and
   that no Singular diagnostic or `=FAIL` marker remains. Exact Q must carry
   the characteristic-zero assertion; `F_65521` is only a software control.
10. Enforce the firewall. A positive verdict licenses only arcwise,
    set-theoretic elimination of the normalized `r=1` receiver and the
    unique-`AC` subcone `a>=2,c=a+1,r>=a` on `D(p*k0)`, subject to the frozen
    first-normal hypotheses. It does not cover `(1,3)`, `(1,4)`, other
    AC/RC/RA2 faces, positive-order or ramified loads, `p=0`, `k0=0`,
    zero/infinity sections, fan exhaustiveness, scheme structure, the whole
    square branch, exact order two, maximum twelve, or JC2.

If any load-bearing point is missing, issue `REPAIR` or `REFUTED`; quote the
smallest obstruction and do not rescue it with an unstated hypothesis. If the
two producer statements differ in verdict, state that explicitly and use
`REPAIR` unless the report can safely confirm the exact conjunction claimed.

End the report with exactly one final token:

- `ORDER2_SQUARE_R1_D1_V12_CONFIRMED`
- `ORDER2_SQUARE_R1_D1_V12_REPAIR`
- `ORDER2_SQUARE_R1_D1_V12_REFUTED`
