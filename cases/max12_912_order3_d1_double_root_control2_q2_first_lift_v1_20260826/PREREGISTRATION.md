# Preregistration: first omitted `q2` support layer of the `la^20` witness

Date: 2026-08-26 UTC

## Exact question

Start with the hostile-reviewed dehomogenized control-2 identity

```text
W = sum_i F_i E_i |_(q2=0)
```

in the fixed-axis source.  Restore the first omitted normal coefficient

```text
Q=q2*z^2+q1*z+q0
```

while keeping `a=1,h=k=nu=0,mu=2/3` and the same exact eight charged ordinary
rows.  Use the already checked dehomogenized multipliers `F_i` without a
refactor and form

```text
W_q2 := sum_i F_i E_i(full q2) = W + q2*C.
```

Compute and print the entire exact correction `C`, its canonical exponent /
rational-coefficient list, and every affine term-weight form under

```text
w(la,tau,rho)=(L,T,H),  L=3T+H,
w(q1)=w(q0)=beta*L,     w(rj)=(15/2)*L,
w(q2)=D.
```

At the first integral omitted layer of the discovery chart use

```text
(L,T,H;D;beta*L;alpha*L)=(4,1,1;23;22;30).
```

This is a **transported first lift**, not an optimal deformation of the
syzygy.  A correction term of weight at most `20L` only rejects these frozen
multipliers; it does not prove that no corrected multipliers or enlarged
witness exist.

## Source and controls

- Hash-pin the charged ordinary-tail source and the reviewed expanded B
  source.  Never consume the known-invalid factored-A renderer.
- Construct the full `q2` coefficient images exactly:

```text
a2 = 54 - 3*q1 + 2*q2 + r2,
a3 = -15 + q0 - 3*q2,
a5 = 27 + q2,
```

with the other images unchanged.
- Require specialization at `q2=0` to agree in all eight rows with the
  dehomogenized pinned B polynomials.
- Require `W_q2|_(q2=0)=W`, exact divisibility of `W_q2-W` by `q2`, and the
  literal identity `W_q2=sum F_i E_i`.
- Run byte-frozen emitted sources on two AWS hosts/orders: global `dp` and an
  `(lp(2),dp(8))` block order.  Any source-hash failure, compiler/CAS stderr,
  diagnostic, failed row check, failed identity, rc/timeout/cap failure, or
  disagreement is no verdict.

## Semantics/firewall

A positive result is a proof-generating identity in the fixed-axis full-q2
finite ideal.  Weight inequalities obtained from its finite support may be
reused only where `la^20` is its unique least-weight term.  It says nothing
about moving axis/cusp, `k` or `nu`, other support directions, the whole
Newton fan, D1, or JC2.  No substantive computation may run on the Mac.
