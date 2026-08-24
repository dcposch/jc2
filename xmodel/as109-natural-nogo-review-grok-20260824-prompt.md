# Hostile different-model review — AS109 natural certificate no-go

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` on clean committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer artifacts on top.

Read in full:

- `xmodel/as109-closed-support-gate-20260824.md`
- every file under `cases/as109_closed_support_20260824/`
- the packed-equation and contraction sections of
  `xmodel/as109-support-gate-20260824.md`
- `xmodel/as109-support-gate-20260824-erratum.md`

Frozen producer hashes:

- report: `b3fa62651673db06b89fb6ad8217ebc2a61bacd5940b7a08501a1f3a47a7d717`
- replay: `01d890b7f048765565203778a038a2d31a7cc8132a7f59c15ebff2655599eb50`
- freeze file: `4fd38dfaac13042be5eb333c1bbdb28c604486a0468f2e661f31b9d40babe8bb`

Independently rerun the replay and attack exactly these claims:

1. The packed determinant identity over `Z_109` has the displayed `L` and
   `N`, with no digit/carry issue.
2. Under the report's precise **full independent literal-slot module**
   hypotheses, a unit right inverse at `s=x^108` forces the individual
   `Q` slot `(0,s*y)`. Check the coefficient and unit argument over
   `Z_109`, including the possibility of a coupled right-inverse preimage.
3. Check the induction for arbitrary `k`: the only two slots whose
   divergence can contribute `s^k`, the `Q`-slot branch, the `P`-only unit
   branch, and the polarization identity. Decide whether it really forces
   every `s^k` into an arbitrary finite free `W` without assuming that `W`
   has a monomial basis.
4. Check the theorem's exact scope: it excludes full independently variable
   literal supports, not coupled submodules/gauge sections. Verify the
   coupled rank-one countercontrol and ensure no arbitrary fixed-support
   lift is excluded.
5. For `A=a(x)+c(x)y`, `B=d(x)+b(x)y`, independently expand the determinant,
   verify the `y` and constant coefficients, derive `c=k(1+109b)`, and audit
   the polynomial-unit factorization. Pay special attention to why `k` is
   109-adically integral.
6. Verify the `x^108` coefficient obstruction
   `-109+109^2*a_109-109^3*k*d_109`, and decide whether it proves that no
   exact lift can have both corrections affine in `y`, without collision or
   degree assumptions.
7. Check the final resurrection statement: any surviving certificate must
   have essential coefficient coupling and at least one correction of
   `y`-degree at least two. No lift, characteristic-zero point, or JC2
   conclusion follows.

Use independent exact algebra, not the producer's verdict strings. Identify
the smallest missing hypothesis or overclaim. Do not edit producer or
canonical files and do not launch a search.

Write exactly one file:

`xmodel/as109-natural-nogo-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hash/replay evidence, scope exclusions, and precise promotion advice.
