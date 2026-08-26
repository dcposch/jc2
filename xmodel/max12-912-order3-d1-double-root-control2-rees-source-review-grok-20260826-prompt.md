# Text-only hostile source review — exact D1 control-2 Rees residue

Act as a hostile algebraic-geometry and computer-algebra referee.  This is a
**text-only source review**.  HARD RULE: do not execute Python, Singular,
Sage, msolve, Lean, Gfan, a solver, or any substantive symbolic computation
on the local Mac.  You may read files, inspect frozen hashes and already
emitted AWS text, and use lightweight hash/status commands.  State explicitly
that no local substantive computation was run.

Audit the frozen package

```text
cases/max12_912_order3_d1_double_root_control2_rees_20260826/
```

starting from these identities:

```text
30f06e6fc0775d36af9d4b53dcb94db9321b24b32fb6981a17d42ee7dfc1351e  SOURCE_CLOSURE.sha256
a7e8a56e54b35a74df653e1cdd96ead81eb8f47c19cfc11d99b99dd9188fdf9b  PRECOMPILE_FREEZE.sha256
```

Read `PREREGISTRATION.md`, `compile_control2_rees.py`, `remote_worker.sh`,
`AWS_REGISTRATION.md`, `COMPILE_CUSTODY.md`, and `PRESOLVE_FREEZE.sha256`.
Also read the independently confirmed correction review

```text
ec9fe740de4d330fbeaba7a5af5db4e56b36d62f417f051f3c35f85599edd3f1  xmodel/max12-912-order3-d1-double-root-newton-correction-review-grok-v2-20260825.md
```

Charge every item below.

1. Re-expand by hand the nine specialized coefficient images for
   `f=(z^3-3z+2)^3+(z^3-3z+2)(q1*z+q0)+(r2*z^2+r1*z+r0)` and verify the
   compiler images, including `q2=k=0`.
2. Verify the fixed loads and exact targets: row 3 `(2/3)*Lambda^15`, row 8
   `Lambda^20*(1+tau)`, every other row zero, and
   `Lambda=tau^3*rho`.
3. Verify the support mask, weight vector
   `(4,1,1,22,22,30,30,30)`, and residue
   `(1,1,1,1,-1,1,1,-2)`.  Explain why the known `-t^38/2` correction is a
   higher coefficient of `r0`, not an omitted finite coordinate.
4. Audit the sparse substitution, target subtraction, minimum-weight
   evaluation, and both emitted source encodings.  Check especially that the
   compact source and independently expanded source apply the same Rees map.
5. Prove or reject the contraction claim:

   ```text
   ( <f_i(s^w X)> in Q[s,X,s^-1] ) intersect Q[s,X]
   = <f_i(s^w X)> : s^infinity.
   ```

   Decide whether encoding A's `sat` and encoding B's `u*s-1` elimination
   compute that same object, and whether adding `s=0` then the residue maximal
   ideal is the correct exact membership test.
6. Audit the synthetic vertical/factor controls, monomial orders, inverse
   elimination block, source-hash gates, rc/stderr/PASS gates, memory/time
   caps, and fail-closed semantics.
7. Most importantly, adjudicate the theorem semantics.  Does a nonunit exact
   residue ideal imply, by algebraic curve selection after algebraic closure
   and finite ramification, a Puiseux arc of this finite ideal with the stated
   leading valuations/residue?  List every hypothesis needed.  Does a unit
   exclude exactly this support/weight/residue?  Flag any issue caused by
   fixing `a,h,q2,k,nu` identically or by `mu=2/3`.
8. Search for any direction reversal (minimum versus maximum weight), missing
   saturation, hidden moving-load permission, misuse of generator initial
   forms in place of the full initial ideal, or source equation error.

The AWS solvers may still be live.  Do not infer their outcome.  Write exactly
one report and make no other repository edits:

`xmodel/max12-912-order3-d1-double-root-control2-rees-source-review-grok-20260826.md`

End with exactly one token on its own line:
`REES_SOURCE_CONFIRMED`, `REES_SOURCE_REPAIRED`, or `REES_SOURCE_REJECTED`.

