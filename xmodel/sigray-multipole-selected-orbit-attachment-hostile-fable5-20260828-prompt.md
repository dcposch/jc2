# Independent hostile review: Sigray selected-orbit attachment repair

Work in `/Users/dc/code/math/jc2`.  You are Fable 5 acting as a hostile
mathematical referee, not as an editor or advocate.

Review exactly one frozen repair packet:

```text
9f4526f209366098f12bbe60387a190c6d2942a374c05fad092917bc79145f14
  xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md
```

It repairs the sole ambient attachment blocker in the frozen producer and
prior hostile review:

```text
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8
  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
ac49c025e3e010d3ecaf3839adf51c40cb88b0088198ae1c5ab1198e07cc8004
  xmodel/sigray-multipole-global-first-exit-partition-hostile-review-gpt56-20260828.md
```

Primary ground truth is `refs/sigray_full.pdf`, SHA-256
`9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`.
Independently read the relevant primary pages: Definitions 3.2--3.4,
Notation 3.1/3.3/3.8, Statements 3.2/3.3/3.5/3.6/3.18, the Section 6
orientation facts, and Statements 7.1--7.3.  Inspect only the additional
repair dependencies actually needed, especially `ladder/SHEET6-AF2.md` and
the hash-pinned Section 7/9 and Proposition 6.7--6.8 packets named by the
repair.  Recompute the argument; do not accept citations by consensus.

Attack these load-bearing points:

1. Does Definition 3.3 really imply `I_P(t)=I_Q(t)` iff
   `t <= O(P,Q)` at the exact object containing every selected cv flag, and
   does this rule out all post-split remerging?
2. Is the rootward segment of a quotient flag representative-independent?
   Is the union of full pole segments rootward closed?
3. For a selected local exit at `F=I_P(u)`, is it valid that every pole ray
   has contact exactly `u` with the selected ray, rather than merely at most
   or at least `u`?  Look for a direction/orbit ambiguity, a rational-grid
   gap, or an extra identification.
4. Does corrected Statement 3.18 plus the cited passed bridge establish that
   different effective cyclic orbits are different actual directions?  Do
   not assume the false stronger statement that cyclic orbits are the only
   identifications in the Eggers--Wall object.
5. Does Statement 7.3 give the cv witness on the same ray, and is it genuinely
   beyond the exit?  Check the use of `u<1` and Statement 7.1 `v>1`.
6. Can two selected witnesses based at the same or different vertices of the
   pole union coincide?  Try to construct an honest Puiseux/contact
   counterexample, not merely an abstract graph excluded by Definition 3.3.
7. Do repaired Propositions 6.7--6.8 exclude every remaining down direction
   from the selected-exit set, including at merges?  Are merge arrivals and
   shared suffixes charged exactly once?
8. Conditional on distinctness, does actual-weight Corollary 7.1 accept the
   whole same-fibre y-side set plus the separate x-side witness and prove
   exactly `sum lambda_F^exit <= td(f,g)-1-psi`?
9. Identify any hidden upgrade to printed `(22)`, literal `delta_a`,
   `(22-cl)`, cross-fibre `kappa`, equality/slack, MP8 no-refinement, root
   census, or `td=6`; all must remain rejected.

Give one verdict: `PASS`, `PASS-WITH-REPAIR`, or `FAIL`.  Separate theorem
truth from citation/scope/conformity.  If repair is needed, state the minimal
exact replacement and whether the MFE inequality still follows.  Keep the
report below about 8,000 words so delivery cannot hit the CLI response cap.
Only light source extraction and exact checks are permitted locally; no AWS
or heavy computation is needed.

Write exactly this report and no other campaign report:

```text
xmodel/sigray-multipole-selected-orbit-attachment-hostile-fable5-20260828.md
```

Then write its ordinary SHA-256 sidecar at the same path plus `.sha256`.
Do not edit canonical files.  Do not enter, list, search, read, build,
modify, status-check, or control `jc2-lean` in any way.
