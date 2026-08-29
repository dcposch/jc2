# Additive structural census note: the top row cancels

Date: 2026-08-27

This note does not alter the frozen question in `PREREGISTRATION.md`.  It
records a sharper consequence discovered by complete literal source
enumeration before the result was frozen.

The raw polygons have maximum weights 14 and 21, so weight 35 can receive
only the pair

```text
F14 = f_2_0 X^2,       G21 = g_3_0 X^3.
```

In

```text
D_n = sum_(i+j=n) ((12-j) F_i' G_j + (i-8) F_i G_j'),
```

that pair contributes at weight 35

```text
(-9)(2) f_2_0 g_3_0 X^4 + (6)(3) f_2_0 g_3_0 X^4 = 0.
```

Thus `D35` has two serialized pre-cancellation contributions but is
identically zero.  Weight 34 is genuinely nonzero.  The requested target
gate still includes `D35=0`, now as a checked redundant structural row;
the last nontrivial target equation is `D34=0`.  All rows above 35 vanish by
support, and all rows above 34 consequently vanish after this cancellation.

This is a compiler/census statement only.  It does not solve any target
equation or imply a specialization, landing, face, family, or JC2 result.
