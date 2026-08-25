# V2 registration — exact `(8,12)` coordinate envelope

- Registered UTC: `2026-08-25T16:21:28Z`, before the V2 solve.
- V1 source/output is preserved as a negative control.  Its unconstrained
  182-slot next digit was consistent but raised the first coordinate's
  partial `y`-degree above eight, so it is neither a frontier survivor nor an
  obstruction.

V2 retains the complete total-D12 support compatible with actual partial
degrees `(8,12)`:

```text
R-coordinate: i+j<=12 and j<=8     (81 slots),
S-coordinate: i+j<=12 and j<=12    (91 slots),
total variables: 172,
determinant rows through degree 22: 276.
```

The source seed, transported operator `D8`, direct-column comparison, and all
integer Frobenius guards are unchanged from `REGISTRATION.md`.  V2 does not
assume the V1 `W2` point.  It must:

1. solve the complete `W2` affine equation `D8(R2,S2)=u^2` in these 172
   slots;
2. choose the deterministic zero-free-variable RREF point if consistent;
3. compute the literal exact divided residual
   `E2=(det(P0+3R2,Q0+3S2)-1)/9`;
4. solve the complete next-digit equation `D8(R3,S3)=-E2 mod 3` in the same
   172 slots; and
5. replay the exact determinant modulo 27 and exact degree pair `(8,12)`.

An inconsistent W2 equation is a complete obstruction to this fixed D12
coordinate envelope.  An inconsistent W3 equation obstructs only the
deterministic registered W2 point, not every W2 point.  A consistent W3
equation produces one explicit finite survivor only.  No selected-Q8, TD6,
inverse-limit, characteristic-zero, counterexample, or JC2 conclusion is
licensed.
