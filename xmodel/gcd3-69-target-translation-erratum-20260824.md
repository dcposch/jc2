# GCD3 `(6,9)` target-translation erratum

**Verdict: `kappa` is not essential modulo the full constant target
translation group. It is a coordinate of the pinned first-target-constant
normalization. Correcting this language does not change the lower-Pfaffian
two-sheet exclusion.**

- Snapshot: 2026-08-24
- Charged bank: `1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a`
- Exact engine: SymPy 1.14.0 over `Q`
- Scope: gauge covariance of the aligned nontrivial-Kummer normal form only
- Cube mismatch, arbitrary `(6,9)`, JC2: open

## 1. The omitted legal gauge

The frozen first common-cubic gate writes

```text
f=z^6+a4z^4+a3z^3+a2z^2+a1z+a0,
g=g0(a)+kappa K,
K=z^3+(a4/2)z+a3/2.
```

It correctly removes the high-row constants `c6` and `c0` by a target shear
and a translation of the second coordinate, but calls `kappa=c3` essential.
That last word omitted the equally legal constant translation of the first
target coordinate

```text
(f,g) -> (f+q,g),             q in k.
```

This operation preserves the Keller determinant, actual degrees, the Kummer
extension, and polynomiality of both boundary values. No frozen hypothesis
pins the numerical value of the first target coordinate.

In the normalized coefficient chart the exact action is

```text
a0_new=a0+q,             kappa_new=kappa-3q/2.        (1)
```

Direct substitution in all eight solved high rows gives

```text
g0(a0+q)+(kappa-3q/2)K = g0(a0)+kappa K.             (2)
```

Thus `q=2kappa/3` gauges `kappa` to zero. The corrected statement is:

> after the chosen pin of the first target constant, the high rows retain
> the bookkeeping constant `kappa`; modulo the full affine target gauge,
> there is no essential aligned high-row constant.

## 2. Covariance of the lower invariants

Reconstructing the five lower coefficient rows from the undifferentiated
pair and reintegrating the four zero rows gives, under (1),

```text
I4_new=I4,        I3_new=I3,        I1_new=I1,
I2_new=I2+3kappa q-9q^2/4.                              (3)
```

Consequently

```text
mu_new=mu+3kappa q-9q^2/4,
C_new=kappa_new^2+mu_new=kappa^2+mu=C.                (4)
```

The elliptic-sheet parameter `C`, its curve
`Y^2=3X^3+4096C`, and its terminal one-form are therefore genuine
target-translation invariants.

On the zero-bracket sheet, `d` transforms to `d+q`, while

```text
kappa_new+3(d+q)/2=kappa+3d/2.                        (5)
```

So the physical coefficient of `K` in `g` and the zero-bracket conclusion
are unchanged. On the `C=0` sheet, choosing `q=2kappa/3` sends

```text
f_lambda-2kappa/3 -> f_lambda,        kappa_new=0,
```

and leaves `g_lambda`, the bracket `567lambda^6`, and the terminal ODE
unchanged. The "shifted DS" path is simply the ordinary DS path in a
translated target chart.

## 3. Mathematical impact

There is a real gauge-language error in the frozen first gate and its first
hostile review: `kappa` is not an essential modulus without an explicit
target-value pin. The clean fix is this immutable erratum plus corrected
canonical language; the frozen producer and review bytes should not be
rewritten.

No exclusion is retracted. The lower-Pfaffian successor treats every value of
`kappa`, its reduced decomposition is controlled by the invariant `C`, and
the translated DS endpoint has the same source bracket and valuation ODE.
Quotienting the redundant target translation only simplifies that proof.

The cube-mismatch branch has additional weight-unforced constants whose
translation action is different; it remains open and must be expressed in
target-translation-invariant combinations before promotion.

## 4. Replay and negative scope

Run:

```text
uv run --offline --no-project --with sympy==1.14.0 python \
  cases/gcd3_69_target_translation_erratum_20260824/check.py
```

Expected first marker:

```text
PASS-GCD3-69-TARGET-TRANSLATION-ERRATUM
```

This erratum proves no cube-mismatch obstruction, no full `(6,9)` theorem,
and no instance of JC2.

