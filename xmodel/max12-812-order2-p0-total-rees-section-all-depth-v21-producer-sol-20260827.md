# Producer report: actual-total named sections at all coefficient grades V21

Date: 2026-08-27

Status: **PRODUCER-CHECKED EXACT RESULT; DIFFERENT-MODEL HOSTILE REVIEW REQUIRED.**

## Frozen replay and custody

Case:
`cases/max12_812_order2_p0_total_rees_section_all_depth_v21_20260827/`.

```text
FREEZE.sha256  403451572df3dd1929d873f63a6fe22972e2127c24a24fa5b8ccfbdf18bea38b
RESULT.json    f702630d71ea4b1168ab993848dc334e67fac4f436273e27fc5fb93637bd34ff
tails.json     d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
V20 emitter    5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587
```

The confirmatory replay used an untruncated sparse implementation of
`Q[sigma,rho]`; it did not select a maximum grade.  It evaluated every one of
the 569 frozen canonical tails after reconstructing the four literal source
specializations from the actual-total emitter formulas.  Runtime was 0.06
seconds with about 13 MB maximum RSS.  Exact reduction checks over `F_32003`
and `F_65521` passed, and the grade-13/14 zero results bridge to both V20
result files.

## Exact result

The complete nonzero output is

```text
A00:
  Tg15_6 = -1/16.

A10:
  Tg15_3 = -1/16,
  Tg15_5 = -(3/32) rho^2,
  Tg15_7 = -(3/128) rho^4.
```

Every other row coefficient is zero on `A00` and `A10`.  In particular,
grade 15 is the first source grade that is nonzero on either named `J2`
prefix section; the constant values `Tg15_6(A00)=-1/16` and
`Tg15_3(A10)=-1/16` kill those two displayed sections without localizing in
`rho`.

On `CS0` and `Z00`, every one of the seven entire row series is identically
zero in `Q[sigma,rho]`.  This is an all-coefficient statement for the frozen
finite-tail source, not a cutoff observation.  The reason the computation is
finite and exhaustive is that after each named assignment all coefficient
series are finite polynomials in `sigma`; every load-containing tail is zero,
and all remaining tail products are multiplied without truncation.

## Provisional interpretation

Conditional on hostile review:

1. Full grade-15 export is the first useful bounded source input for the two
   `J2` charts; grade 13/14 cannot decide them, whereas grade 15 at least
   destroys the simplest horizontal witnesses.
2. Searching higher coefficient grades of this same finite-tail source for a
   row that breaks `CS0` or `Z00` is futile: no such row exists.  Those two
   residuals require chart/Rees equations, routing to another source family,
   or a structural receiver argument rather than a deeper source export.

## Scope firewall

Killing `A00` and `A10` does not prove `a0` or `a1` is radical and does not
empty either `J2` Rees chart.  Persistence of `CS0` and `Z00` is restricted
to the literal source from the frozen 569 canonical tails under the named
assignments; it is not a claim about unwritten Rees equations, chart
bilinears, other source families, or extension to a full formal source arc.
`CS0` is outside the named unit-`k10` family on `D(k)`.  Nothing here proves
Gate T, order two, maximum twelve, or JC2.
