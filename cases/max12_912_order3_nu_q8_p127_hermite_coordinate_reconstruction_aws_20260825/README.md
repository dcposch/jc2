# Hermite reconstruction from shape fibres and moving-v jets

This AWS-only successor combines the 123 exact full-degree shape fibres with
the independently computed moving-v Hensel jet at `w=25`.  For jet order
`N`, every scalar coordinate coefficient is reconstructed modulo

```text
M_N(s) = s^N * product_{a in sampled w-values, a != 25}(s-(a-25)),
s=w-25,
```

so the effective exact Hermite condition count is `122+N`, not 123.  It
searches unique full-rank common denominators hierarchically per coordinate,
on the two natural triples, on the six true-centre coordinates, and globally
with the localizer inverse.  Lower-order candidates must survive the
independent higher-order jet; a candidate first appearing at the higher
order remains provisional.

This is reconstruction evidence only.  Any surviving rational graph must be
substituted exactly in every original quotient row modulo the monic candidate
`H(w,v)`, and must then pass the full Q8 contact/no-merger checklist.  No
recurrence or finite-field graph alone licenses a characteristic-zero
component or a Keller trajectory.

