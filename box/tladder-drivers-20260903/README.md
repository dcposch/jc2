# T-LADDER symbolic controls (2026-09-03)

All computations use `x=gamma`, `y=pi`, characteristic zero, and
`J(F,G)=F_x G_y-F_y G_x`.  They are read-only with respect to the charged
inputs and make no ledger/report edits.

Run:

```bash
python3 hadic_identity_check.py
python3 moh_1510_jacobian_control.py
python3 moh_1612_reduction_control.py
python3 keller_uniform_counterfamily.py
```

Files and scope:

- `hadic_identity_check.py`: exact differential-polynomial audit of the
  charged `(2,3)` identity, including a concrete counterexample to the
  charged formula and the corrected identity.
- `moh_1510_jacobian_control.py`: Moh pp.210--211 post-simplification
  12-parameter family; canonical H-digits, degrees, and an exact coefficient
  certificate that `J=C*x^2`, `C!=0`, has no solution.
- `moh_1612_reduction_control.py`: literal p.208 general 17-parameter shape
  and equation-size control; p.209 normalized 10-parameter family, canonical
  H-digits, eight embedding relations, and an exact coefficient certificate
  that `J=C*x`, `C!=0`, has no solution.
- `keller_uniform_counterfamily.py`: uniform exact family with
  `J(P,Q)=x^k`; at `k=0` every member is a Keller automorphism.  It has one
  nonconstant H-digit of unbounded `x`-degree.

Important limitations:

- Moh p.208 literally prints the same `c5` on both terms of `alpha3`.  That
  gives `4+1+12=17`.  Reading the second as a likely independent `c6` and
  gauging away constant `alpha1` also gives 17; the driver keeps these two
  interpretations separate.
- The p.208 statement `22 [15 or 13]` for the third case is not accompanied
  by its ansatz.  The supplied pp.210--211 `(15,10)` shape is already the
  later 12-parameter simplification.  Thus `22 [15 or 13]` is SOURCE-READ but
  cannot honestly be reconstructed from that frozen shape; the driver emits
  this as a failed reconstructibility control instead of inventing slots.
- The literal 17-parameter `(16,12)` coefficient system is generated and
  sized but not solved.  The normalized ten-parameter system is solved by a
  short exact coefficient/resultant certificate, without a large Groebner
  basis.
