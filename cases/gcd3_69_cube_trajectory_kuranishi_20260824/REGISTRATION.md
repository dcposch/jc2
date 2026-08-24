# Registration — GCD3 `(6,9)` cube-core rational trajectory gate

- Date: `2026-08-24`
- Producer: independent Codex/Sol lane; no Claude successor output was read or
  consumed.
- Charged predecessor: the confirmed cube-mismatch Faber--Laurent gate and
  its hostile different-model review.
- Charged correction: the confirmed first-target-translation erratum.
- Reused algebra only: the universal lower-invariant decomposition from the
  lower-Pfaffian case; no nontrivial-Kummer weight or descent hypothesis is
  imported.
- Field: algebraically closed characteristic zero.

Charged immutable inputs:

```text
6a2799dfe46828c70462d51a842a3fc0adf0515b8ded7a576cdb837d81847d20  xmodel/gcd3-69-cube-mismatch-gate-20260824.md
2648eef3b8091970655a94743c6c181343a94534b6454f43c579b310331ba7d7  xmodel/gcd3-69-cube-mismatch-review-grok-20260824.md
43fa36968bb90414748330c1b4a5d5169a0eaa21b1925623764e96204e049c78  xmodel/gcd3-69-target-translation-erratum-20260824.md
f4cb57ca765138ed2decab01b12a7f884c37f9a847d80e90162ee751bb3df837  xmodel/gcd3-69-target-translation-erratum-review-grok-20260824.md
7671785519bf4e55b602f117740bd8d8571c6982a8916235407a2bb0a2263043  xmodel/gcd3-69-lower-pfaffian-successor-20260824.md
a000619d8b5597add21716d525856c459ff57d5a2b2ab75b85de5d9d08970b27  xmodel/gcd3-69-lower-pfaffian-successor-review-grok-20260824.md
557f3b33108dfc3279ad7699b796ea8a29eef673d3d162f144f6e655071391e6  cases/gcd3_69_lower_pfaffian_successor_20260824/verify_lower_invariants.sing
```

Registered question: classify every rational coefficient trajectory in the
two finite-pole alternatives forced by the predecessor,

```text
s in k*;                       or
s=C(x-a)^m, m>=2,
```

with `d!=0` and `d=0` kept separate, all high constants retained modulo the
legal target quotient, and both original polynomial boundary values retained.
Later target constants are also retained: in particular a nonzero `rho4`
after a `rho3`-leading balance may not be set to zero by first-row analysis.

Allowed positive conclusion: an exact weighted Newton--Puiseux/Kowalevski
classification, including exceptional rank strata and a reconstruction of
each survivor through the original Faber coefficient equations.  An exclusion
may be claimed only for the polynomial cube core.  This case does not import
the aligned Kummer hypotheses, close arbitrary `(6,9)` by itself, construct a
Keller pair, or decide JC2.

Registered exact checkpoints include the uniform pole laws
`(14-k)p=1` and `(14-k)p=m-1`, all projective high/target load charts, the
two `d!=0` squarefree orbits, and the full mixed `(rho3,rho4)` invariant
fiber.  Necessary Kuranishi projections must be followed either by an exact
reconstruction/unit certificate or by an explicitly retained global fiber.

Replay from the repository root:

```text
uv run --offline --no-project --with sympy==1.14.0 python \
  cases/gcd3_69_cube_trajectory_kuranishi_20260824/replay.py

Singular -q \
  cases/gcd3_69_cube_trajectory_kuranishi_20260824/verify_kuranishi.sing

Singular -q \
  cases/gcd3_69_lower_pfaffian_successor_20260824/verify_lower_invariants.sing
```
