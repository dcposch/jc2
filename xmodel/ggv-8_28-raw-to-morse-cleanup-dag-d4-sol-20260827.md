# DEP-D3: factor-local raw-to-Morse cleanup DAG through weight 22

Date: 2026-08-27  
Lane: `a1_total_lift_design` / Sol2  
Dependency: `DEP-D3`, with rollback on any D3 review change

## Result

**Producer PASS: `PASS-DEP-D3-FACTOR-LOCAL-CLEANUP-DAG-W22`.**

The missing D3 interface can be filled at the factor-local formal level.
A deterministic exact compiler now expresses every coefficient through
weight 22 of

```text
U(t), W(t), V(t), Q(t), Gamma(t)
```

as an `Add/Mul` expression DAG in the 400 named positive-weight raw
`2S/3S` rows, after fixing `F0=H^2`, `G0=H^3`.  It retains the four rational
factor tags, chart, deck, orientation, and determinant data.  The canonical
compact DAG has 49,964 nodes and an 8,400,824-byte encoding with SHA-256

```text
bc3bd04c453eef74d19682b020541f64ca1f42557f2c177692f02485ed1a17d7.
```

The frozen result is a certificate-sized manifest: it records the output
node ID at every index `0..22`, the complete recurrence metadata, node/op
census, and the canonical full-DAG digest.  The producer deterministically
reconstructs all nodes before byte-comparing the result.

This closes D3's missing *local cleanup-DAG type*, but not its global gluing
or `H`-multiple gap.

## 1. The first discriminator is positive

Raw `F14` containing only `X^2` does **not** prevent local `U14=X`.
There is a five-row literal synthesis:

```text
H = X^8-1,
u = H + t^6 X - (1/2)t^8,
U = t^14 X - (1/4)t^16.
```

Direct expansion gives

```text
F = u^2+U
  = H^2 + 2t^6 H X - t^8 H + t^12 X^2.
```

The apparent forbidden terms cancel exactly:

```text
t^14:  -X + X = 0,
t^16:  1/4 - 1/4 = 0.
```

Every surviving term is a literal legal D3 raw row:

| slot | chart row | coefficient |
|---|---|---:|
| `f_1_5` | `t^6 X` | `-2` |
| `f_9_29` | `t^6 X^9` | `2` |
| `f_0_0` | `t^8` | `1` |
| `f_8_24` | `t^8 X^8` | `-1` |
| `f_2_2` | `t^12 X^2` | `1` |

The raw `F14` coefficient is zero.  The coordinate has

```text
u=H mod t,
u_X=H'(X)+t^6,
```

so it is a valid formal local coordinate at every simple root of `H`.
This is not a claimed global polynomial automorphism; it is one explicit
factor-local chart, exactly the type R2 uses.

Sign and support mutations are detected.  Flipping the `-t^8/2` sign
changes the sparse identity; flipping `-t^16/4` leaves a forbidden nonzero
weight-16 row (the raw `F16` slice is empty); and a synthetic raw `F14:X`
is rejected because its pullback would be `x*y^-3` outside `2S`.

The strategic correction is sharp: the direct-row mismatch in R1 is real,
but it cannot be promoted to a support-only obstruction.  Nonlinear lower
raw rows can generate the local carrier.

## 2. Exact local algebra and recurrence

All four factors are handled simultaneously in the finite etale algebra

```text
A = Q[c]/(c^8-1)
  = product over p in {X-1,X+1,X^2+1,X^4+1} of kappa_p.
```

A coefficient of `A` is serialized as eight exact rationals.  Projection to
each factor inherits its D3 factor ID.  The compiler first solves

```text
xi(t)=c+s(t),
F_X(xi(t),t)=0,
s(0)=0
```

coefficient by coefficient.  The linear coefficient is

```text
F0''(c)=2H'(c)^2=128c^6,
```

with exact inverse `c^2/128` in `A`.  It then sets

```text
U(t)=F(xi(t),t).
```

Writing `z=X-xi(t)`, the centered expansion is

```text
F-U=z^2(A2+A3 z+A4 z^2+...),
u=z(q0+q1 z+q2 z^2+...).
```

The exact recurrences are

```text
q0^2=A2,          q0(0)=H'(c)=8c^7,
q1=A3/(2q0),
q2=(A4-q1^2)/(2q0).
```

The only square-root denominator is `2H'(c)=16c^7`, with inverse `c/16`.
The inverse-coordinate linear term is `alpha=q0^-1`; its closed-fibre
denominator `8c^7` has inverse `c/8`.  These are exact units on every factor,
not hidden rational functions of the raw rows.

For

```text
z=alpha*u+beta*u^2+gamma*u^3+O(u^4),
G(xi+z,t)=g0+g1*z+g2*z^2+g3*z^3+O(z^4),
```

the serialized outputs use

```text
W=g0,
V=g1*alpha,
Q=g1*beta+g2*alpha^2,
Gamma=g1*gamma+2*g2*alpha*beta+g3*alpha^3.
```

All series operations are exact through `t^22`.  Closed-fibre nodes reduce
exactly to

```text
s0=U0=W0=V0=Q0=0,  Gamma0=1.
```

The DAG census is:

| operation | nodes |
|---|---:|
| raw leaves | 400 |
| constants in `A` | 1,204 |
| additions | 18,332 |
| multiplications | 30,028 |
| total | 49,964 |

No inverse node involving a raw variable appears.  The full `u^4+` sidecar
is retained as the typed residual

```text
R_ge4=G(xi+z(u),t)-W-Vu-Qu^2-Gamma*u^3,
ord_u(R_ge4)>=4.
```

R2—not this compiler—is the theorem that this residual misses the first
constant carrier.

## 3. What remains open

The next step must impose/replay the Keller equations on these raw
expressions and glue the factor-local output to one literal polynomial
`E22 in Q[X]`, retaining the global `H`-multiple.  D3's exact diagonal test
shows that this multiple can move all seven cokernel coordinates, so the
factor-local DAG alone does not emit a global seven-vector.

No result here proves that a raw specialization satisfies the Keller
recurrence, that the local coordinates glue to a global polynomial
automorphism, or that any `8_28` face is excluded.

## Replay

```bash
python3 cases/ggv_8_28_raw_to_morse_cleanup_dag_d4_20260827/compile_cleanup_dag.py \
  --check \
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json \
  cases/ggv_8_28_raw_to_morse_cleanup_dag_d4_20260827/RESULT.json
```

The frozen replay is desk-scale exact arithmetic: one core, 84.14 seconds,
95,453,184 bytes maximum RSS, and no swap.

## Scope firewall

This provisional DEP-D3 result is a factor-local formal cleanup interface
through weight 22.  It is not a global `E22`, global `H`-multiple control,
`8_28` face/family exclusion, source/landing coverage theorem, `G2-PSC`,
`G2-BD`, Keller pair, counterexample, or JC2 result.
