# HOLD design: factor-etale to global polynomial `E22` gluing interface

Date: 2026-08-27

## Lifecycle hold

This is a design-only artifact.  The prospective local input is D4R1 freeze
`6beafdb4...`, which is not consumed as a theorem before fresh hostile
review.  No compiler execution, descendant claim, or face decision is
licensed by this preregistration.

## Objective

Join the factor-local Morse data to the smallest honest global object by
computing the determinant coefficient directly from the raw source and
using the local data only as a commutative/naturality check.  The interface
must never reconstruct a global polynomial from branch bits or root values.

## Rings

Let `C` be the polynomial ring over `Q` on all 400 positive-weight D3 raw
coefficient slots, with the weight-zero rows specialized to

```text
F0=H^2, G0=H^3, H=X^8-1.
```

Use

```text
S=C[X],
T=S[t]/(t^23),
A=C[c]/(c^8-1),
A_p=C[c]/(p(c))
```

for `p=X-1,X+1,X^2+1,X^4+1`.  The map `pi_H:S->A` is reduction modulo the
monic polynomial `H`.  CRT factor projections retain their D3 factor IDs,
deck, chart, orientation, and determinant tags.

## Direct raw determinant custody

For raw chart polynomials `F=sum t^i F_i(X)`, `G=sum t^j G_j(X)`, define in
`S`, without any local cleanup,

```text
D_n = sum_(i+j=n) ((12-j) F_i' G_j + (i-8) F_i G_j').
```

This is the literal coefficient of

```text
E=12F_XG-8FG_X-t(F_XG_t-F_tG_X).
```

The global `D22` is authoritative.  Since `H` is monic, exact Euclidean
division in `C[X]` gives unique objects

```text
D22 = H*Q22 + R22, deg_X(R22)<8.
```

`R22` is the factor-etale/CRT value; `Q22` is the exact global `H`-multiple
custody object.  Neither may be inferred from the other.  The literal
`D22` may then be reduced by the confirmed linear `M` algorithm to seven
exact expressions in `C`.

## Prospective D4R1 naturality square

Only after D4R1 review PASS, consume its exact series in `A[[t]]`:

```text
xi=c+s(t),
q0=u_X(xi,t),
U(t), V(t).
```

The constant-in-`u` local channel is

```text
C_n=sum_(i+j=n) V_i*(j-8)*U_j.
```

The compiler must replay through weight 22 the generic identity

```text
E(t,xi(t)) = q0(t)*C(t)
```

in `A[t]/(t^23)`, by evaluating the direct raw `D_n` at `X=xi(t)` and by
evaluating the D4R1 node roots.  This tests the raw-to-Morse map; it does not
define `D22`.

The Keller lower-row gate is load-bearing.  Only after exact polynomial
identities

```text
D0=...=D21=0 in C[X] (or in a frozen quotient/specialization)
```

may the weight-22 naturality identity simplify to

```text
pi_H(D22)=q0(0)*C22.
```

Without that gate, substitution `X=xi(t)` mixes derivatives of lower `D_n`
into weight 22.

## Target and mutations

For normalized target `E=t^22+O(t^23)`, an honest global check requires

```text
R22=1 and Q22=0,
```

equivalently the literal identity `D22=1`.  Factor-local carrier equations
can at most certify `R22=1` after the lower-row gate.

Registered fail-closed mutations:

1. add `H` to `D22`: all factor values/`R22` stay fixed, but `Q22` and the
   seven-vector change, so the compiler must reject equality with the old
   global object;
2. retain a nonzero lower `D21` and a nonzero critical shift: the simplified
   weight-22 formula must refuse to run;
3. drop or permute one factor/deck/orientation tag: reject the CRT gluing;
4. mutate one literal raw row or one sign in the determinant recurrence:
   direct/global versus local/naturality replay must fail;
5. replace direct Euclidean division by interpolation from the 16 carrier
   patterns: reject as an untyped map.

## Verdict firewall

A future PASS establishes a typed commutative interface and exact global
`H`-multiple custody.  It does not solve the raw Keller equations, prove
`Q22=0`, exclude an `8_28` face/family, prove `G2-PSC` or `G2-BD`, construct
a Keller pair, or decide JC2.
