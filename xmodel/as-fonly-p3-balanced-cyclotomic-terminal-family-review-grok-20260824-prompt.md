# Hostile different-model review — balanced cyclotomic AS terminal family

You are the independent different-model hostile reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`1e60fcedc8626650c7c7544ad296c3624173415f`. Read in full:

- `xmodel/as-fonly-p3-balanced-cyclotomic-terminal-family-20260824.md`;
- every payload in
  `cases/as_fonly_p3_balanced_cyclotomic_family_20260824/MANIFEST.sha256`;
- the confirmed D7 triangular terminal producer/review, only as a regression
  target for `m=3`.

Frozen hashes:

- producer report:
  `8d6873550d06136f3a725160161500a844b43c9793a90c59798e5dc2b3c4c8e4`;
- manifest / README / replay / freeze:
  `c4244493a6e94c5f2ddb275d8aab1bd61902e78d6a8bcba9af3fff3441398494` /
  `d55b6c3c58c9e5e756553e767a071a640d351ffdfa7d5682ef7579b89bdfc006` /
  `7464a1936ee089fc0d22f24ff4c3151225aea7942845a14d69ad283388fc53ef` /
  `577e974fafbbff2db9af99ca920660175a8bb5944651eb8228e4aa1bc4308d6a`;
- replay payload:
  `badabc43d596f94e8fbae3ca2f2afbbaf6115af529423ed8974b544cb739b27b`;
- confirmed D7 producer/review:
  `5325890a505489570a6e02409d64e026560d2635ddf989b865039eeb6ecddccb` /
  `75ff0c8588c633fcf53e17104bf77cdc74fba30bc9c02aa776b23ad0baaa2318`.

Verify the manifest and rerun the registered program. That is regression only.
Then independently attack the universal claim:

1. For every odd integer `m>=3`, derive from geometric sums that
   `A_m=(1+z)(1+...+z^(m-1))`, `B_m=A_m(-z)` satisfy
   `A_m B_m=1-z^(2m)`. Check the oddness hypothesis and signs; give a failing
   even-m control.
2. With `z=3x^2`, reconstruct the zero-constant antiderivative
   `P_m'=A_m(z)` and `Q_m=yB_m(z)`. Prove every coefficient of `P_m` is in
   `Z_3`: after reducing `A_k 3^k/(2k+1)`, its denominator must be a 3-adic
   unit. Prove the only nonzero correction coefficient modulo three is the
   `2x^3` term, so the special fibre is exactly `(x-x^3,y)`. Verify both
   total degrees are `D=2m+1`, including possible top-coefficient cancellation.
3. Independently compute the determinant over `Q_3[x]` and obtain exactly
   `1-3^(2m)x^(4m)`, not merely a congruence. Verify survival modulo
   `3^(2m)` and define legitimate clean coefficient representatives modulo
   the next power even when `3|(2k+1)`.
4. Linearize every same-residue lift at depth `2m+1`. Derive
   `-x^(4m)+U_x+V_y mod3`; prove `deg(U_x+V_y)<=2m` under cap `D=2m+1` and
   hence terminality. Attack mixed monomials, Frobenius derivatives,
   representative changes, target shears, and the quadratic determinant term.
5. Independently instantiate `m=3,5,7,9`: recover the exact frozen D7
   coefficients and clean `1566` representative at `m=3`; print a complete
   D11 `m=5` point modulo `3^10` and verify its determinant/next obstruction
   without importing the producer script.
6. Determine the exact meaning: an infinite family of different finite-degree
   points, each terminal one digit after depth `D-1`. Reject any compatible
   all-depth branch at fixed `D`, classification of a full locus, uniform
   upper death bound for other branches, characteristic-zero lift/no-lift,
   counterexample, or JC2 inference. Assess its value as a compiler regression
   family and whether any stronger scoped finite-cap terminality follows.

Use exact arithmetic and independent derivations. Do not edit producer, case,
canonical, ladder, notes, prompt, log, run, or erratum files; do not launch
AWS. Keep scratch outside tracked paths. Write exactly one report:

`xmodel/as-fonly-p3-balanced-cyclotomic-terminal-family-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, the independent general proof and examples, the smallest failing
identity if any, exact promotion language, and quarantine language at both
ends.
