# Round-1 boundary covariance probe

This directory contains the exact falsification-first implementation for
portfolio root P1. It uses only rational symbolic arithmetic.

Replay:

```bash
uv run --no-project --with sympy==1.14.0 \
  python3 cases/round1_boundary_probe/boundary_probe.py --summary \
  > /tmp/round1-boundary-results.json
diff -u cases/round1_boundary_probe/results.json \
  /tmp/round1-boundary-results.json
```

## Exact local schema

For separate-degree homogenizations `F,G`, use

```text
A = [[F_X, G_X],
     [F_Y, G_Y]].
```

At the generic point of a boundary divisor with DVR parameter `t`, the full
two-by-two cokernel is recorded by its Smith exponents `(a,b)`:

```text
a     = ord_t Fitt_1(coker A) = min ord_t(A_ij),
a + b = ord_t Fitt_0(coker A) = ord_t(det A).
```

Thus the pair contains all generic DVR isomorphism data for the torsion
cokernel; it is stronger than the determinant order whenever `a != 0`.

The standard compactification chart is

```text
X=1:  u=Z/X, v=Y/X, x=1/u, y=v/u.
```

The explicit blow-up chart at `[1:0:0]` is

```text
u=s, v=s*w, hence x=1/s, y=w.
```

The meromorphic log-coframe matrix has columns `df,dg` in the basis
`(du/u,dv)` before the blow-up and `(ds/s,dw)` after it. For every `J=1`
map its determinant orders are respectively `-2` and `-1`; this is only the
ambient coordinate-volume transformation. Its individual Smith exponents can
and do depend on the polynomial presentation.

The non-Keller class-kill decoy is evaluated at its own leading root in the
symmetrical `Y=1` chart, with blow-up `z=s,r=s*w`.

## Scope

- Mandatory Keller controls: identity, `T_2`, `T_4`,
  `T_4^{-1} o T_4`, and the promoted Hénon tower at `r=0,1`.
- Every Keller control is a polynomial automorphism, so exact orbit
  minimization sends it to the identity. Raw presentation data and minimized
  data are both reported.
- The class-kill map is a non-Keller schema/negative control only.
- No residue-A leading truncation is treated as a Keller input. Without its
  unknown tails it does not satisfy the pure-boundary identity.
- `results.json` is generated output frozen for audit; the script itself is
  the exact checker.
