# Correction: the converse direction of the staged rho-unit calculus

Date: 2026-08-27

Status: **PROMOTED NARROW CORRECTION.**  The forward certificate theorem and
all promoted chart certificates remain unchanged.

## Evidence

The overbroad converse was isolated in the direct-`T-cs` producer and
independently confirmed in its different-model hostile review:

```text
7af66e58a7262ca05bf140919ed3d6ff4e0357bdb6db3378d494907ff33baa8f
f16e1114b24e88dfa60d0e687881817f73055361d450547f40ddc9cd5374a844
```

This corrects the sentence “Conversely, chart-fibre emptiness has a
homogeneous power-containment form” in promotion `16ec6f54...` only insofar
as it could be read as producing the same multiplicative rho-unit type.

## Correct statement

Let `J` be the unsaturated honest chart ideal, `f` its exceptional
coordinate, `s` a genuine localizer, and `rho` the degeneration parameter.
If the total chart's closed fibre is empty after localizing at `s`, finite
generation yields exponents `N,m` with

```text
f^N*s^m in J+(rho).                                      (C)
```

Equivalently, there is some polynomial `H` with

```text
f^N*s^m = element_of(J) + rho*H.
```

In general `(C)` does **not** imply an identity

```text
f^N*s^m*(1+rho*W) in J,
```

because `H` need not be divisible by `f^N*s^m`.  Saturation/localization and
adjoining `rho` do not commute in the way that stronger claim requires.

## What remains promoted

The forward theorem is unchanged: an actual identity

```text
f^N*s^m*(1+rho*W) in J
```

is sufficient for the localized special-fibre and DVR-arc conclusions.  A
direct identity with `W=0`, such as the reviewed `T-cs` certificate, is
stronger still.  Standard-chart coverage, ordered-stratum coverage, and the
three obligation removals for a **direct total-family certificate** remain
valid.  A separately specialized unit or fibre-emptiness calculation remains
a screen until either a direct certificate or the exact total-chart
special-fibre statement is established with the needed saturation custody.

