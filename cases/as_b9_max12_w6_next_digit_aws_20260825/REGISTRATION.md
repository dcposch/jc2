# Registration — complete fixed-D12 next digit after the B9 `Z/243` point

- Registered UTC: `2026-08-25T16:22Z`, before execution.
- Parent: frozen producer-exact
  `cases/as_b9_max12_w5_survivor_aws_20260825/`.
- Execution: dual AWS only, 1 GiB / 120-second cap.

Rebuild the exact parent pair and determinant.  Divide `det-1` coefficientwise
by `243`, reduce the quotient modulo three, and solve the **complete** affine
next-digit equation

```text
D(R,S)=-((det-1)/243) mod 3,
D(R,S)=R_x-u^3*R_y+S_y,
```

where both `R,S` range over every monomial of total degree at most twelve.
Use deterministic exact Gaussian elimination over `F_3`, emit rank, pivot
columns, selected correction support, the full divided residual, and a
canonical digest.  If consistent, construct `P+243R,Q+243S`, literally
expand the integer determinant, and require equality to one modulo `729`.
The old point without the new digit is the negative control.

This decides only the next digit above one fixed `Z/243` point in the complete
D12 output-digit cone.  It does not classify all lower-level fibres, prove an
all-depth branch, produce a characteristic-zero map/counterexample, settle
maximum twelve, enter TD6, or resolve JC2.
