# Result: uniform D1 `a>=13` grade-38 `J` obstruction

Date: 2026-08-26

Status: **DUAL-AWS EXACT-Q PRODUCER PASS; AWAITING HOSTILE REVIEW.**

## Exact theorem produced

In characteristic zero, after the previously registered square/D1 gates,
the seven literal Faber source equations have no point on the Keller chart
`D(J)` with

```text
ord_sigma(A)=a,  ord_sigma(C)=a+1,  ord_sigma(R)=r,
a>=13, r>=a.
```

This is a scheme-theoretic source-row statement. It uses no radical and no
contact-coefficient localization. Write at the baseline

```text
A=sigma^13*theta*Abar,
C=sigma^14*theta*Cbar,
R=sigma^13*theta*eta*Rbar.
```

The complete source through grade 38 has pole denominator at most `L^2`.
Consequently its moving odd rows satisfy

```text
Phi7-(p(sigma)/4)*Phi5-(p(sigma)^2/32)*Phi3
    -(p(sigma)^3/128)*Phi1 = 0 mod sigma^39.
```

The literal Keller target occurs only in row seven, as
`-sigma^38*J/4`. Thus the corresponding relation for the full equations is

```text
-sigma^38*J/4 mod sigma^39.
```

All seven equations therefore force `J=0`. Adjoining `iJ*J-1` gives the
unit ideal exactly, before radicals.

## Complete support and timing through grade 38

The producer reconstructs every one of the seven frozen rows, with the
moving connection and independent jets of `A,C,R,k10,k6,k2` and all four
targets. At the smallest contact `a=r=13`, the nonpolynomial source families
which can enter by grade 38 are exactly:

| first grade | source family | pole order |
|---:|---|---:|
| 31 | `(3/4) sigma^17 k6 C/L` | 1 |
| 35 | `(1/2) sigma^22 k2 R/L` | 1 |
| 37 | `(3/4) sigma^10 A C/L` | 1 |
| 38 | `(3/8) sigma^10 C^2/L^2` | 2 |
| 38 | `(5/8) sigma^11 k10 R C/L` | 1 |
| 38 | `(1/4) sigma^25 k2 A/L^2` | 2 |

The first triple-pole family, `(1/4) sigma^25 k2 C/L^3`, begins at grade
39. Every higher-pole family begins later. Raising `a` or `r` only delays
these walls.

The exact sparse targets are retained at their licensed times:

```text
row 2: -sigma^28*(mu20+...+sigma^10*mu20_10),
row 4: -sigma^32*(mu4 +...+sigma^6 *mu4_6),
row 6: -sigma^36*(mu6 +...+sigma^2 *mu6_2),
row 7: -sigma^38*J/4.
```

Thus load and target jets through grade 38 are not silently set to zero.
The source reconstruction pins the corrected parenthesized-load ancestry and
the complete 131-entry row-seven tail (and all six other tails).

## Why `J` is source-required and nonzero

`J` is the constant Jacobian of the Keller pair, not a freely discardable
normal coefficient. The source equation requires the row-seven target
`J/4`; on the named chart `D(J)` it is invertible (and may be normalized to
`J=1` after a target scaling). The row syzygy forcing `J=0` is therefore a
contradiction on precisely that chart. No conclusion is claimed on `V(J)`.

## Homogeneous contact coverage

The exact congruence is checked polynomially with independent `theta,eta`.
Substituting `theta=sigma^n`, `eta=sigma^s` gives every integer contact
`a=13+n`, `r=a+s`. After a common ramification, the same homogeneous
substitution covers every rationally valued arc with `a>=13,r>=a`; all
source monomials acquire nonnegative additional powers, so no omitted wall
moves earlier. This is a symbolic coverage argument, not a finite sampling
of contacts.

## Separate sharpness control at `a=12`

The producer separately rebuilds `a=12` and verifies that the order-two
recurrence fails at grade 38 by a nonzero coefficient depending on the
leading `k2` load. This is exactly the newly arriving `k2*C/L^3` triple-pole
wall. It proves only that the order-two proof cannot be extended to `a=12`;
it is **not** a survival result. The residual `a=10,11,12` contacts require
the separately preregistered order-three replay.

## AWS custody

Exact Q and `F_65521` both print all required recurrence, unit, symbolic,
negative-control, and Pell sentinels exactly once; both engines return zero,
both validators pass, and neither host swaps. Full lane details are in
`AWS_LAUNCH_METADATA.md` and every retrieved byte is pinned by
`EVIDENCE.sha256`.

## Firewall

This result excludes only the stated D1 high-contact cone on `D(J)` for the
seven literal source rows after the cited upstream gates. It does not by
itself cover `a<=12`, other D1 cells, excluded lifecycle charts, the whole
square component, order two, `(8,12)`, maximum twelve, or JC2.
