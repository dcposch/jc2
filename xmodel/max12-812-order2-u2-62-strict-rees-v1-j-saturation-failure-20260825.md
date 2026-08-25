# Failure analysis — V1 omitted the mandatory `j!=0` localization

Date: 2026-08-25  
Status: **V1 STRICT-SATURATION INPUT QUARANTINED AS NON-DECISIVE; EXACT TAIL
COMPILATION AND RAW COMMON-QUARTIC SUPPORT UNAFFECTED**

## Smallest failing line

The emitted V1 ring retains the Jacobian constant `j` as a polynomial
variable, but its saturation block is

```text
I=(Psi1,...,Psi7);
KT=I:(tau)^infinity;
K=KT:(rho)^infinity;
boundary=K+(tau,rho);
H=boundary:(B0,...,B6)^infinity.                     (0.1)
```

The source theorem requires `j!=0`.  Therefore (0.1) must also localize at
`j`, or specialize to a fixed nonzero `j`, before taking the boundary.  V1
does neither.

## Exact spurious component

Set

```text
j=k10=k6=k2=mu2=mu4=mu6=0.                          (0.2)
```

Choose the common quartic

```text
K0=z^4+z^2,       f0=K0^2,
```

so in the V1 coefficient variables

```text
B6=2, B4=1,       B5=B3=B2=B1=B0=0.                (0.3)
```

All odd coefficients vanish, so the chart twist
`C_i=(1+tau)^(i mod 2)B_i` leaves (0.3) fixed for every `tau`.  The seven
unloaded Faber tails of `f0=K0^2` vanish identically.  Under (0.2), every
target term also vanishes.  Hence (0.2)--(0.3) solve all seven `Psi` rows for
arbitrary nonzero `tau,rho`, survive both interior saturations, specialize
to `tau=rho=0`, and survive the coefficient irrelevant saturation because
`B6=2`.

Thus V1 necessarily has a nonempty boundary supported at `j=0`.  A nonunit
V1 endpoint cannot say anything about the required `j!=0` client.  A unit
endpoint would have been a stronger valid exclusion, but the literal family
above proves that such an endpoint cannot occur in exact arithmetic.

## Quarantined dual-host runs

The mistake was found while both exact-input runs were active.  They were
terminated deliberately and preserved without consuming an endpoint:

```text
r6d:
  max12_812_order2_u2_62_strict_rees_sat_v1_20260825T225334Z_r6d
  host ip-172-30-0-45, 2026-08-25T22:54:07Z--23:05:44Z, rc 1

Box03:
  max12_812_order2_u2_62_strict_rees_sat_v1_20260825T225834Z_box03
  host ip-172-30-0-249, 2026-08-25T22:59:44Z--23:05:44Z, rc 1
```

Both consumed the same input

```text
e3cbb667cdd390bac3981ed4aaeaa032bf1de6c83061c6890512758179ca70a7
  strict_rees.sing
```

and their interrupted stdout is byte-identical, SHA-256
`d9fd3452b5eaf244f200e55afd7cbed6cd8d5828c3a1f5b918ebd21ed5599055`.
That is custody only, not an endpoint.  Exact evidence is under

```text
cases/max12_812_order2_u2_62_strict_rees_20260825/
  aws_saturation_v1_quarantine/{r6d,box03}/
```

## Clean repair

Keep the seven `Psi` rows byte-for-byte and replace only the interior block
by

```text
KT=I:(tau)^infinity;
KR=KT:(rho)^infinity;
K=KR:(j)^infinity;                                   (0.4)
```

before the same boundary and irrelevant saturations.  This computes over
the required open parameter locus `j!=0`.  The order of these principal
localizations is immaterial algebraically, but the displayed order keeps the
two strict-Rees interior steps visible.

The separate Shioda/Hall result can later justify removal of the closed
all-six-lower-loads-zero locus as an optimization.  That optimization is
not part of repair (0.4) and must remain logically separate until its hostile
review is frozen.

## Scope firewall

This failure invalidates only the V1 global saturation as a decision
procedure.  It does not change the exact seven tails, their weights, the
terminal target, the raw unloaded exceptional fibre, its common-quartic
reduced support, or the two charged Taylor families.  V1 proves no nonunit
boundary for `j!=0`, no strict arc, no rational section, no order-two
closure, and nothing about JC2.
