# First transverse-cusp transport of the corrected q2 witness

Date: 2026-08-26 UTC

Status: **DUAL-AWS EXACT TRANSPORT THRESHOLD / NEGATIVE CONTROL; hostile
review pending.**

Restore the single transverse discriminant direction

```text
p=-3, c=2+h,
K=z^3-3z+2+h,
```

while fixing `a=1`, `k=nu=0`, `mu=2/3` and retaining full
`Q=q2*z^2+q1*z+q0`, full quadratic `R`, all eight exact charged ordinary
tails, and the reviewed corrected multipliers

```text
F1'=F1+q2/12, F2'=F2-q2/9, Fi'=Fi (i>=3).
```

Both AWS encodings reconstruct the same 98-term polynomial `W_h` and the
same 61-term correction `(W_h-W')/h`.  Its specialization at `h=0` is the
literal reviewed 37-term corrected witness `W'`, SHA

```text
ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b.
```

The correction canonical SHA is

```text
3ef3c9c2e950f2e8508f86d2b474608ed4a277eea5b210cf67569661b3f7d58f,
```

and the complete coefficient/monomial/weight certificate SHA is

```text
93dd031f5d523085d166d7382490f05652261af1ccd281a51aeb88994baeb425.
```

## Exact unchanged-witness threshold

Normalize by `wt(la)=L` and put

```text
alpha=15/2, beta=5+u, delta=5+v, eta=wt(h)/L,
u>0, v>0, T>0.
```

For every non-target monomial the certificate records its exact difference
from target weight `20L` as

```text
c + q*u + d*v + e*eta.
```

The unchanged corrected witness has unique least term `la^20` uniformly for
all `u,v>0` exactly when

```text
eta >= 15/2.
```

At `eta=15/2`, every equality at the closed corner `u=v=0` becomes strict in
the open quadrant.  The eight new extremal correction terms are

```text
-88/27 h*q2*r2   +11/9 h*q2*r1   -22/27 h*q2*r0,
+11/9  h*q1*r2   -22/27 h*q1*r1  +11/27 h*q1*r0,
-22/27 h*q0*r2   +11/27 h*q0*r1.
```

The first three have normalized margin `eta-15/2+v`; the other five have
margin `eta-15/2+u`.  Thus they are strict at `eta=15/2` for `u,v>0`.
Conversely, if `0<eta<15/2`, choosing the relevant `u` or `v` sufficiently
small makes one of these terms lie below target, so no smaller eta gives a
uniform open-quadrant conclusion from this unchanged witness.  The full
certificate retains all 50 correction terms that are below target for some
positive eta and all 28 closed-corner threshold monomials (20 old and eight
new).

Therefore this computation says

```text
OLD_CORRECTED_WITNESS_DOES_NOT_TRANSPORT_UNIFORMLY for 0<eta<15/2.
```

This is a negative control for the witness, not evidence that an arc or
branch survives.  The low-eta cells require a new graded syzygy correction.

## Ordinary covariance checksum

Independently, the compiler verifies for each `ell=1,...,8` that every
ordinary source monomial in row `ell` has coefficient weight `12+ell` under
`wt(a_i)=9-i` and `wt(kbar)=6`.  This is consistent with the unit-axis
change

```text
f(z) -> a^-9 f(a*z), Lambda -> a^-1 Lambda, rho -> a^-1 rho,
q2,q1,q0 -> a^-4 q2,a^-5 q1,a^-6 q0,
r2,r1,r0 -> a^-7 r2,a^-8 r1,a^-9 r0,
tau,k,mu,nu unchanged.
```

This checksum supports a separate moving-axis reduction; it is not promoted
here as that theorem.

## Dual AWS custody

- Box03 `98.80.65.144`, forward tag
  `max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826T034500Z_box03_forward`,
  registered worker PID `153321`: rc 0, empty stderr, 22,476 KiB maximum
  RSS, zero swap.
- r6d `100.26.198.153`, reverse tag
  `max12_912_order3_d1_double_root_control2_h_first_transport_v4_20260826T034500Z_r6d_reverse`,
  registered worker PID `221060`: rc 0, empty stderr, 22,444 KiB maximum
  RSS, zero swap.

Both ran under 4-GiB / 900-s caps after pre-GO registration and source hash
checks.  They returned byte-identical certificate JSON despite opposite
traversal orders.

## Firewall

This classifies only the weight behavior of one explicit corrected witness
after restoring one cusp coordinate.  It does not compute the full initial
ideal or fan and does not cover low-eta cells, a newly corrected h-witness,
moving axis, moving loads, another normal direction, equality support faces,
a formal arc, the whole double-root locus, D1, or JC2.
