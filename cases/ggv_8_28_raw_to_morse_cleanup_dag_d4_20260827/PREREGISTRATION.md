# Preregistration: DEP-D3 raw-to-Morse cleanup DAG through weight 22

Date: 2026-08-27

## Dependency and rollback

This is a provisional descendant of D3
`STOP-FIRST-MISSING-PROVENANCE`.  It pins the complete D3 freeze and report,
names the dependency `DEP-D3`, and is discarded if D3 review changes the raw
slice or interface typing.

## Frozen question

Starting from the 442 literal symbolic raw `2S/3S` slots frozen by D3 and
the fixed leading edge

```text
F0=(X^8-1)^2,  G0=(X^8-1)^3,
```

construct a deterministic expression DAG for the oriented factor-local
formal Morse cleanup through `t^22`.  Every coefficient of

```text
U(t), W(t), V(t), Q(t), Gamma(t)
```

must be an explicit exact expression in named raw rows.  The output retains
factor, deck, chart, orientation, and determinant tags.  It is a local
formal coordinate calculation and makes no global-polynomial automorphism
claim.

The first discriminator is exact: determine whether `U14=X` can arise from
legal raw rows even though the raw `F14` slice contains only `X^2`.  Accept
only a literal sparse identity or a first unavoidable nonunit division,
pole, or non-polynomial raw term.

## One simultaneous factor-local algebra

Use the finite etale `Q`-algebra

```text
A = Q[c]/(c^8-1) = product_p kappa_p,
```

where `p` runs over `X-1`, `X+1`, `X^2+1`, and `X^4+1`.  A coefficient in
`A` is a degree-at-most-seven vector.  Projection to each factor is tagged
but need not be duplicated algebraically.  Since

```text
H'(c)=8c^7
```

is a unit in `A`, the implicit critical-section and oriented square-root
recurrences are legal simultaneously on all four factors.

In `A[[t]]`, solve the unique critical section

```text
xi(t)=c+s(t),  s(0)=0,  F_X(xi(t),t)=0.
```

Then set

```text
U(t)=F(xi(t),t).
```

Writing `z=X-xi(t)`, expand

```text
F(xi+z,t)-U(t)=z^2(A2+A3*z+A4*z^2+...),
u=z(q0+q1*z+q2*z^2+...),
q0^2=A2, q0(0)=H'(c).
```

Only `q0,q1,q2` are needed for the exact `u^0..u^3` coefficients of `G`.
If

```text
z=alpha*u+beta*u^2+gamma*u^3+O(u^4),
G(xi+z,t)=g0+g1*z+g2*z^2+g3*z^3+O(z^4),
```

then serialize

```text
W=g0,
V=g1*alpha,
Q=g1*beta+g2*alpha^2,
Gamma=g1*gamma+2*g2*alpha*beta+g3*alpha^3.
```

The full `u^4+` sidecar is retained as the typed residual
`G-W-Vu-Qu^2-Gamma*u^3`, rather than falsely discarded.  R2, not this
compiler, licenses its irrelevance to the first constant channel.

## Expression-DAG contract

- Leaves are exact constants in `A` or named D3 raw slots.
- Internal nodes are `Add` or `Mul`; all inversions in series recurrences
  must expose and exactly invert a constant unit of `A`.
- Raw coefficient polynomials are obtained only from D3 slot exponents.
- The compiler serializes the coefficient-node IDs for every index `0..22`
  of `U,W,V,Q,Gamma`, the critical section, and the coordinate jets.
- A replay rebuilds the complete DAG deterministically and compares bytes.
- Factor projections inherit the four D3 factor IDs.  Orientation is
  `u=H mod t`, determinant is `H'(c)`, and deck is `ORIENTED_PLUS_H`.
- No alias supplies a map.

## Registered discriminator and mutations

The prospective positive discriminator is

```text
u = H + t^6 X - (1/2)t^8,
U = t^14 X - (1/4)t^16,
F = u^2+U = H^2 + 2t^6 H X - t^8 H + t^12 X^2.
```

It is accepted only if every surviving coefficient is a legal D3 raw slot,
the `t^14` and `t^16` cancellations replay exactly, `u=H mod t`, and
`u_X=H'+t^6` is a unit at every simple `H`-root.  Mutations of either minus
sign, deletion of a supporting raw row, or replacement of a legal exponent
by the nonexistent raw `F14:X` must fail.

The generic DAG must also fail closed if the leading edge is changed, if
`H'(c)` is not invertible, if an output index is missing, or if a factor,
deck, orientation, chart, or determinant tag is removed.

## Scope firewall

A successful DAG proves only a factor-local formal cleanup interface through
weight 22.  It does not prove that a given raw specialization satisfies the
Keller recurrence, does not glue a global polynomial `E22`, does not control
the global `H`-multiple, and does not prove an `8_28` face/family exclusion,
`G2-PSC`, `G2-BD`, a Keller pair, a counterexample, or JC2.
