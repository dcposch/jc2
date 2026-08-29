# Opus 5 independent checker: intrinsic exact-pair L3/L4/L5

Companion artifact for
`xmodel/g2-intrinsic-exact-pair-l3-l5-hostile-review-opus5-20260828-v1.md`.

Run:

```
python3 -B cases/g2_intrinsic_exact_pair_l3_l5_opus5_review_20260828/verify.py
```

Pure standard library, exact arithmetic over `F_2521` (`p-1 = 2520 = lcm(1..10)`),
under a second, no CAS, no AWS.  Exit code 0 on PASS.

## Independence design

Every curve test carries two objects produced independently of the
Newton-Puiseux recursion:

1. a **certified complete root set** — an exact Laurent-polynomial identity
   `A(t) * prod_i (y - r_i(t)) == h(t^-kappa, y)`, which pins the full root
   multiset (including the branches escaping to `y = infinity`) with no
   reference to any residual polynomial;
2. a **certified place list** — for each normalized `x`-chart place, an
   explicit parametrization `s |-> (x(s), y(s))` with `h(x(s), y(s)) == 0`
   exactly, plus a birationality certificate `s == Num(x,y)/Den(x,y)` verified
   by composing back, so that `e_S := -ord_s(x(s))` is read off geometrically.

Sigray's all-root recursion is then run as a third engine and compared
against both.  Part A is an exhaustive Z/kappa orbit-stabilizer sweep
(`kappa = 1..12`, all supports in `{0..11}`).

## Coverage

Tight and oversized Kummer covers; nontrivial support gcd; zero and constant
support; horizontal lines; vertical components; reducible curves; branches
escaping to `y = infinity`; premature common prefixes; Sigray Proposition 3.1
`(*)`/`(**)` and Statement 3.9 `(i)`/`(iii)` at every node; the terminal
`deg p = 1` certificate.

## Mutations (all must be detected, and are)

`M2` reduced denominator = ambient `kappa`; `M3` dropping the zero residual
root; `M4` non-squarefree equation; `M5` counting the escaping branches;
`M6` premature terminal declaration; `M7` support gcd read one step early;
`M8` raw cover `t`-order used as a place order.

Non-vacuity was additionally confirmed by five out-of-band sabotages
(corrupted root, wrong `e_S`, inverted residual extractor, `orbit == stab`,
trivial deck action); each is caught.
