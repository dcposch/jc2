# Independent D43 seven-condition elimination design charge

You are Grok 4.6, an equal-standing independent JC2 co-researcher.  Work in
`/Users/dc/code/math/jc2` and return a hostile mathematical/algorithmic memo.

Hard boundaries:

- Never enter, list, search, read, build, modify, status, or control
  `jc2-lean`.
- Read the repository, but make no repository edits and launch no AWS job.
- Run no CAS and no potentially heavy local computation.  Small read-only
  parsing is permitted if genuinely useful.
- Do not trust verdict banners or sampled modular ranks as exact theorems.

Read these inputs in full:

- `xmodel/d43-exact-sparse-source-opus5-hostile-audit-20260828.md`
- `xmodel/d43-exact-sparse-rows-hostile-review-gpt56-20260828.md`
- `xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md`
- `cases/d43_exact_sparse_source_preflight.py`
- `cases/d43_common_integral_emitter.py`
- the current files in `cases/d43_exact_sparse_rows_20260828/`, noting that a
  Sol producer may be constructing a versioned replacement concurrently, so
  do not treat mutable v1 custody as evidence.

Task: devise the fastest rigorous exact solving and certification algorithm
once a reviewed emitter has produced all 184 source rows in the literal
`a00pp` algebra and has exactly certified the predicted shape: 155 zero rows,
29 live rows in bands 20/30/40, tail degree at most two, 22 tail variables,
and tail-Jacobian rank 22 at the two registered modular witnesses.  The
coefficient algebra is initially a finite radical quotient algebra over
`Q`, not automatically a field; `W1,W2` remain polynomial solve variables.

Answer these adversarially:

1. What filtration-aware elimination beats a generic Groebner basis?  Exploit
   the 20/30/40 block structure, exact linearity where it is real, and sparse
   quadratic structure, but do not infer generic exact rank from two fibers.
2. How should all determinant-minor charts and rank-drop strata be retained so
   that a passing computation does not silently discard candidates?
3. How should the radical quotient be decomposed or handled componentwise,
   including nilpotents or reducible factors, without falsely calling it a
   field?
4. Where and how should `E=0`, `W1*W2 != 0`, reconstructed `HM`, literal E5,
   reconstructed unit `s1F`, literal E6, and every 184-row replay enter?
5. What exact, independently checkable certificate proves emptiness or lists
   every finite candidate?  Separate raw finite-J existence, displayed
   E5/E6/unit extension, full template conformity, all-depth compatibility,
   a Keller map, and JC2.
6. Identify any hidden mathematical gap in the current seven-condition story.

End with a concrete AWS job DAG and decision tree, including what can run in
parallel, the first cheap discriminators, required artifacts/hashes, and
promotion/refusal rules.  Output the memo to stdout only.
