# Hostile different-model review — AS109 SEXTIC FRONTIER PREFLIGHT

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer/review artifacts on top.

Read in full:

- `xmodel/as109-sextic-frontier-preflight-20260824.md`
- every file under `cases/as109_sextic_frontier_preflight_20260824/`
- the confirmed quartic producer/review
- the quintic producer/review only to understand its independent pending or
  landed status; the sextic preflight must not consume it

Frozen hashes:

- report: `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4`
- replay: `21bc494f552587ee0b64c01c735b2f1243eafce9599f1e05bc526d23e38f73ad`
- freeze: `2890f3dd5d09b45e4f047cbb509b42430c3c9a677412cccef0b18fd66b44c4ab`

Independently rerun the replay and attack exactly:

1. Exhaust the max-`y`-degree-six pair sweep. Verify divisible-degree shears
   for `(1,6),(2,6),(3,6)`, equal-degree reduction, and that both `(4,6)` and
   `(5,6)` genuinely remain. Check no quintic theorem is silently consumed.
2. For `(4,6)`, recompute the leading normalization
   `a4=H^2,b6=H^3`, the definition `N=3a3H-2b5`, and the full `[y^8]`
   coefficient. Prove or refute
   `H(2HN'-5NH')=0 => (N^2/H^5)'=0 => N^2=kappa H^5`, including zero cases,
   UFD valuations, and constants.
3. Audit both `(4,6)` branches. For `kappa=0`, check the common quadratic
   generator's top coefficients without promoting lower-row compatibility.
   For `kappa!=0`, derive `H=h^2,N=lambda h^5`, recompute the depression
   mismatch `lambda/12`, and verify exactly why allowable target operations
   do not remove it. Ensure neither branch is claimed empty.
4. For `(5,6)`, independently derive leading/depression alignment and all
   nine Jacobian rows (5.1), including the chain-rule factor `h`. Recompute
   the five integrated coefficient formulas (5.2), all integration constants,
   and every allowed target normalization.
5. Directly differentiate `I_3,I_2` and verify they equal `E3,E2` after
   substitution. Recompute every coefficient of `omega` and `eta`, the rank
   determinant `(6/5)^4` at the control point, and the displayed exterior
   component. Distinguish “omega is not exact by this immediate mechanism”
   from the much stronger and unproved absence of a rational integrating
   factor or first integral on the level surface.
6. Audit the algebraic-equation count and polynomiality gap. Check both
   `y=0` boundary equations, why no monic eliminant follows yet, and the exact
   rational trajectory `A=B=C=0,D=x^-5,h=x^11,r=-x^-1`: all Pfaffian rows,
   `h*eta=-6`, first boundary polynomial, and second residual `-x^-6/5`.
   Confirm it is a negative control, not a Keller pair or lift.
7. Verify replay hashes, exact controls, and scope. The correct outcome may be
   a sharply specified survivor only: no degree-<=6 theorem, no strengthened
   AS109 floor, no finite-support existence/nonexistence, and no JC2 inference.
   State the smallest valid successor for each of `(4,6)` and `(5,6)`.

Try hard to find a missing degree pair, sign error, hidden division, or false
integrability statement. Do not edit producer/canonical files, continue the
survivor discriminator, or launch AWS.

Write exactly one file:

`xmodel/as109-sextic-preflight-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent algebra/replay, dependency status, exact scope
exclusions, and promotion advice.
