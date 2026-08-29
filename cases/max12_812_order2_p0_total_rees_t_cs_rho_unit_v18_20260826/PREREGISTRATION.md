# T-cs ordered-chart rho-unit test V18

Date: 2026-08-26

## Claim under test

Let `E12` be the literal total moving-p source equations in all seven rows at
grades 10, 11, and 12, and add the complete total fifth-row grade-14
coefficient exported by frozen V17.  Form the actual T-cs chart by

```text
rs=cs*qrs,  c0=cs*qc0,  c1=cs*qc1
```

and localize at `cs`.  On the ordered closed complement of the already tested
T-rs chart, set `qrs=0`.  V18 tests whether the special fiber on `D(k)` is
empty:

```text
1 in (E12,Tg14_5,qrs,rho,1-u*cs,1-v*k).             (1)
```

If (1) holds, then in the actual total chart localized at `cs*k` there is an
identity `1=a+rho*h`; hence rho is a unit.  No equality with a separately
formed specialized Rees chart is required.

## Inputs and controls

- Every V9 grade-10--12 coefficient is checked against its frozen manifest.
- V17 `Tg14_5` is checked against its harvested validator result and hash.
- In characteristic 65521, every selected input is compared to the reduction
  of the exact-Q input before chart substitution.
- The chart uses an ordinary polynomial ring and exact inverse-variable
  localization equations; qring is forbidden.
- Dropping `Tg14_5` must leave a nonunit ideal.  This is the decisive-row
  negative control.
- Exact Q runs on Box02; F65521 is an independently compiled software/control
  lane on r6d.  Any compiler, engine, diagnostic, custody, or validator
  failure is no verdict.

## Scope

A PASS establishes rho-unit exclusion only on
`V(rs/cs) intersect D_+(cs) intersect D(k)` for this complete prefix.  It
does not cover the later c0/c1/A charts, the terminal all-zero receiver,
global Gate T, order two, maximum twelve, or JC2.

