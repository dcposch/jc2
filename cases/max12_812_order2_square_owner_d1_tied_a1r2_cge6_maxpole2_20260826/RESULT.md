# Producer result: tied D1 `(a,r)=(1,2)`, closed `c>=6` face

Date: 2026-08-26

Status: **EXACT-Q PRODUCER PASS WITH TWO FRESH GOOD-PRIME CONTROLS; HOSTILE
REVIEW REQUIRED BEFORE PROMOTION.**

## Exact result

After the frozen generic-square and D1 source gates, the complete seven
literal Faber equations are empty on

```text
D(p*k0), ord(A)=1, ord(R)=2, ord(C)>=6.
```

No leading coefficient of `C` is inverted.  At baseline contact six, every
`C`-dependent source starts after the decisive grade 16, and raising the
contact only delays it.  Thus the calculation is a closed `C`-order tail,
not an inference from a dense exact-contact subset.

An independent cost-bounded census of all four frozen binomial summands
finds exactly the following first-grade primitives:

```text
(5/32) k0*A^2/L,  (5/16) k0*R^3/L,
-(3/8) R*A^2/L^2.
```

All occur in grade 16; `RA2` is the unique pole-two family.  The padded
census is identical.  `AC` starts only at grade 17.  The compiler rebuilds
all seven literal source rows and the independent analytic Laurent source,
checks their coefficientwise grade-16 bridge, exact recursive quotients,
and exact absence of `C`, lower loads, connection/normal corrections, and
all seven targets.

With `L=z^2+p/2`, the reconstructed pole-two numerator is the canonical
remainder modulo `L^2` of

```text
(5/32)k0*A^2*L +(5/16)k0*R^3*L -(3/8)R*A^2.
```

The exact ordinary quotient and pole-two recurrence are retained.  Both
root Faber functionals and both derivative-row syzygies pass.  The first
root equations force `L|R*A^2`; the two same-root charts are unit ideals and
the two opposite-root charts exhaust the survivors.  On those survivors,
exact division by `L` gives the deck terminals

```text
+(5/2)k0*lambda^3*bu^3, -(5/2)k0*lambda^3*bu^3,
```

and derivative terminals `5*k0*lambda^4*bu^3`.  They are units on the
registered exact-`R`, `D(p*k0)` charts before radicals.  Removing `R3`
makes the quotient terminal zero, so the required source column is not
silently supplied by another family.

## AWS executions

| endpoint | tag | rc / wall / max RSS KiB / swap | stdout SHA256 |
|---|---|---|---|
| exact `Q`, Box02 | `max12_812_order2_square_d1_tied_a1r2_cge6_maxpole2_v1_q_box02_20260826T1955Z` | 0 / 0.08 s / 19716 / 0 | `e800e78d04a38ffdb00fed8ad89b775ec3879f2053c8a60bb5905f01f73ccdb2` |
| `F_65519`, Box03 | `max12_812_order2_square_d1_tied_a1r2_cge6_maxpole2_v1_p65519_box03_20260826T1955Z` | 0 / 0.07 s / 20040 / 0 | same |
| `F_65521`, r6d | `max12_812_order2_square_d1_tied_a1r2_cge6_maxpole2_v1_p65521_r6d_20260826T1955Z` | 0 / 0.07 s / 20064 / 0 | same |

All validators returned `PASS_D1_TIED_A1R2_CGE6_MAXPOLE2_EMPTY`; all
engines returned rc 0 with zero swap.  Exact `Q` is the characteristic-zero
endpoint and the primes are software/host controls.  The generated programs
use ordinary polynomial rings and explicit reduction ideals; no Singular
`qring` occurs.

## Custody and firewall

All hosts received the same source archive, SHA256
`682a8d9ab3c04e7ebd4dd7e04f23d114b0c064b5269c8df3563d4cf5acb0c5a6`,
and passed `FREEZE.sha256` before compilation.  `EVIDENCE.sha256` and
`PRODUCER_FREEZE.sha256` pin the retrieved executions and theorem statement.

This producer does not import or amend the separately reviewed
`(a,c,r)=(1,5,2)` producer.  It says nothing about `ord(C)<=5`, another
primary/tied face, positive-order leading load, `p=0`, `k0=0`, an excluded
zero/infinity or terminal/global chart, fan exhaustiveness, order two,
maximum twelve, or JC2.
