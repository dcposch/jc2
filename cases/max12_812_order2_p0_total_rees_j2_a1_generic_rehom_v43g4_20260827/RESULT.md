# V43G4 exact generic-certificate rehomogenization

Date: 2026-08-27  
Status: **PRODUCER PASS; provisional pending independent hostile review and the separately live special-fibre converter input.**

## Exact result

In the literal total ring

```text
S = Q[t, X19_total],   t = rho^2,
```

with all 66 positive-weight variables retained in the reconstructed 59-row
corpus, the frozen V43G3 Laurent certificate was independently parsed and
multiplied against all 58 post-pivot literal rows.  It replays

```text
sum_i C_i Tg_i|_(a1=1) = 1             over Q(t).
```

The least denominator clearing found in those serialized multipliers is
`5*t^6`.  Sigma-residue projection modulo `wt(a1)=5` drops zero terms; the
surviving product levels are exactly 3 and 4.  Rehomogenizing to level 4 and
multiplying the original, non-dehomogenized literal total rows gives the
exact polynomial identity

```text
5*t^6*a1^4 = sum_i H_i Tg_i            in S.
```

Exactly eleven multipliers are nonzero, all on grades 11--15:

```text
Tg11_2 Tg11_7 Tg12_2 Tg12_7 Tg13_5 Tg13_7
Tg14_5 Tg14_7 Tg15_3 Tg15_5 Tg15_7.
```

The eliminated pivot is the sole `ez9` row `Tg19_2`; its reconstructed
multiplier is zero.  Thus the pivot substitution cannot contribute to the
displayed identity.  A literal mutation of `Tg15_7` leaves a one-term
nonzero residual.

This is an honest total polynomial certificate, but its coefficient has
positive `t`-valuation.  It is not by itself the required
`a1^N U(t)` certificate with `U(0) != 0`.  Conditional on exact replay of the
separately live special identity `a1^104-B=tH`, the reviewed converter yields
a pure total certificate at exponent `4+6*104=628`, with coefficient 5
(then rationally normalized).  That converter has not yet been run here.

## Custody and replay

- Frozen AWS source:
  `/home/ubuntu/jobs/max12_812_order2_p0_total_rees_j2_a1_generic_rehom_v43g4_20260827T111531Z_source`
- Frozen source manifest SHA-256:
  `89a4b9a0e33ce84b8e3dda793d2ddd37ef384951ba6fa7b1d0cccf6d94305fe7`
  (755 files, 23 MiB, made read-only before launch)
- AWS host: `ip-172-30-0-106`, instance `i-0f089e64c378f5da3`,
  `r6i.16xlarge`; one core, 64-GiB virtual-memory cap, one-hour wall cap
- AWS job:
  `/home/ubuntu/jobs/max12_812_order2_p0_total_rees_j2_a1_generic_rehom_v43g4_20260827T111531Z_exact_rehom_r6b`
- Local harvest: `aws_r6b_rehom_20260827T111531Z/`
- AWS evidence manifest SHA-256:
  `e64b8e8e3874ae02759a7ea8e3287d0cf1e09900fca472537b3d3ee4e28af18c`
- Exact result JSON SHA-256:
  `e97ebd6a893e73d8e3751692b56300f0df230a75184f20b05d91282ac455e962`
- Serialized total certificate JSON SHA-256:
  `e737b9ef129e5022c47100553d3a1725dbd6bc67e2486760e6d3d523db07b740`
- Preregistration SHA-256:
  `20bce356839fef3b25746d7b5c895ab0a0f2dfcfb3223e1fc06624831a9ecdb4`
- Rehomogenizer SHA-256:
  `62560313f046b8a7935852bc75e5ba5125c6db5441c19e5f75083a3c0951e902`
- Runner SHA-256:
  `ed3779565ca39647bc6a181a9c1b47f482d4e7737993e0f5ab0a64e41bfa66d6`

The compiler pins and verifies the complete V43G3 freeze, reparses every
individual Laurent multiplier with a fail-closed grammar, reconstructs the
literal total rows from the pinned V43 source, and performs all products over
exact `Fraction` arithmetic.  The inert Singular matrix-write artifacts from
V43G3 are never used.

## Scope firewall

The theorem is only the displayed identity in the frozen ordered-`a1`
grade-through-19 literal total ideal (indeed its eleven-row grade-through-15
subideal).  It is not yet a total ordered-chart closure theorem, terminal
receiver theorem, source/landing coverage theorem, `G2-PSC`, `G2-BD`, Gate T,
order-two, maximum-twelve, or JC2 result.
