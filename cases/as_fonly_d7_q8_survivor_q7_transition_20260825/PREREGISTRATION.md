# Canonical Q8-survivor to Q7 transition

Consume the canonical survivor `x23=x30=1`, with zero Q8 restored vector and
zero degree-six Frobenius spectators.  Restore the six derivative-zero
`C6,D6` coefficients and all twelve `W5,Z5` coefficients.  Impose, from the
full integer source before reduction,

```text
F5 = E5/3 + M5 + div(W6,Z6),
F4 = E4/3 + M4 + div(W5,Z5),
G7 = F7/3 + {C,D}7 + T7.
```

Every division must be asserted coefficientwise over the integers.  Emit
the exact 19-by-18 affine rank pair, a substituted witness if compatible or
a sparse left-null certificate if not, plus a one-coordinate RHS control.
This is one canonical Q8 point only, not the entire 13-dimensional chart or
the full six-spectator Q9 fibre.
