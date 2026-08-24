# Hostile different-model review — TD6 TWO-CHART FIRST BAND

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer/review artifacts on top.

Read in full:

- `xmodel/td6-two-chart-first-band-20260824.md`
- every file under `cases/td6_two_chart_first_band_20260824/`
- the reviewed parent `xmodel/td6-global-compatibility-gate-20260824.md`
  and its hostile review
- the exact canonical SP-2, F1, r9/M2 material cited in the producer report

Frozen hashes:

- report: `cb373892233bddaf1b8fbf7722335ca43ee366b337151c3b244d2604d8168bf2`
- replay: `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`
- freeze: `995a0ba55a20b9aa59626654614fe54a5f8beb95742a5376ddf006eef3fe3d49`

Independently rerun the replay and attack exactly:

1. Audit source typing. Check that the fixed rectangles, shared centering
   `(1,1,1)`, F1 polynomial `P`, r9/M2 specialization, dead-stretch choice,
   pole scales, and every chart substitution are licensed as one control.
   Distinguish a selected specialization from data forced by a terminal class.
2. Independently recompute the x/F1/pole leading patterns and the pole ODE
   `3p q'-5p' q=25`, including the chart two-form signs and powers. Check that
   the first pole Jacobian row is genuinely built into transport.
3. Audit the sparse compilers and exact linear algebra: variables, all
   transport equations, ranks `946/976` and `2524/2626`, shared global
   coefficients, the 40 x-J rows with 38 new independent rows, and joint rank
   `3508/3602`. Look for duplicate, omitted, or locally copied variables.
4. Reconstruct or independently verify the deterministic rational witness,
   its support/serialization hash, and every imposed equation using a second
   path where feasible. Check that it proves nonemptiness over `Q`, not merely
   modulo a prime or numerically.
5. Recompute the first un-imposed rows `[s^-1]J` and `[r^1](J-1)`, their
   nonzero payloads/hashes, and the conclusions `global_J_exact=false` and
   `terminal_class_realized=false`. Identify exactly which later/global data
   remain untied or unquantified.
6. Decide the exact scope of `NONEMPTY-WITNESS`: one source-typed first-band
   specialization only. Check that it stops this proposed first-band
   obstruction but implies neither all first bands are nonempty nor a Keller
   pair, terminal realization, landing theorem, counterexample, or JC2.

Identify the smallest failing hypothesis or overclaim. Do not edit producer
or canonical files, append the next nonlinear rows, or launch AWS.

Write exactly one file:

`xmodel/td6-two-chart-first-band-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent exact checks, source-typing caveats, scope exclusions,
and promotion advice.
