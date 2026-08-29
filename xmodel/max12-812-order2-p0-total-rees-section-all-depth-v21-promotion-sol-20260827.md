# Promotion: actual-total named sections at all coefficient grades V21

Date: 2026-08-27

Status: **PROMOTED EXACT PREFIX-ROUTING THEOREM.**

## Custody

```text
producer report
  xmodel/max12-812-order2-p0-total-rees-section-all-depth-v21-producer-sol-20260827.md
  172755de690977d90448a6b6c6ac0abf0d9437dfecb46983638919eb241c7ffe

Fable5 hostile review
  xmodel/max12-812-order2-p0-total-rees-section-all-depth-v21-hostile-review-fable5-20260827.md
  f0c57c1ffecc7a1c8db1a6d8242e94e89fcd2798950ea3d91c5bb4168946ebaf

frozen exact result
  cases/max12_812_order2_p0_total_rees_section_all_depth_v21_20260827/RESULT.json
  f702630d71ea4b1168ab993848dc334e67fac4f436273e27fc5fb93637bd34ff
```

The reviewer independently derived the four source specializations from the
literal emitter, evaluated all 569 tails with a separate untruncated
`Q[sigma,rho]` implementation and numeric controls, regenerated the frozen
result byte-for-byte, and verified the V20 and modular bridges.

## Promoted theorem

For the literal actual-total source defined by the frozen 569 canonical tails,
the complete seven-row specialization in `Q[sigma,rho]` is

```text
CS0: every row is identically zero;
Z00: every row is identically zero;

A00:
  row 6 = -(1/16) sigma^15,
  all other rows = 0;

A10:
  row 3 = -(1/16) sigma^15,
  row 5 = -(3/32) sigma^15 rho^2,
  row 7 = -(3/128) sigma^15 rho^4,
  all other rows = 0.
```

There is no hidden grade cutoff.  Under each named assignment all coefficient
series become finite polynomials in `sigma`, every load-containing tail is
identically zero, and the remaining finite products were evaluated without
truncation.  Support is at most grade 15 on `A00/A10` and grade 12 on `CS0`;
the displayed answer is exhaustive.

Consequently grade 15 is the first and only nonzero literal-source grade on
either displayed pure `J2` point.  In particular
`Tg15_6(A00)=-1/16` and `Tg15_3(A10)=-1/16`, uniformly in `rho`, so grade 15
kills both horizontal witnesses without localizing at `rho`.

Conversely, no coefficient grade of this literal finite-tail source can kill
`CS0` or the terminal-origin section `Z00`.  A successor targeting either
must use genuine Rees/chart equations, a routing or receiver theorem, or a
different source family; deeper exports of the same source cannot help.

## Operational consequence

The first bounded stage-two source object is the full seven-row grade-15
export, followed by typed `T-a0` and ordered `T-a1` certificate design.  The
two unit points are controls, not chart closures.  Do not launch a higher-row
search whose only success condition is breaking `CS0` or `Z00` in this source.

## Scope firewall

This theorem kills two named points, not the full `J2` charts; it proves no
radical containment for `a0` or `a1`.  The `CS0/Z00` zeros are statements
about the frozen literal finite-tail source under the named assignments, not
about unwritten Rees equations, chart bilinears, another source family, or a
full formal-source arc.  `CS0` remains outside the named unit-`k10` family on
`D(k)`.  The theorem does not establish the terminal receiver, Gate T, order
two, maximum twelve, or JC2.
