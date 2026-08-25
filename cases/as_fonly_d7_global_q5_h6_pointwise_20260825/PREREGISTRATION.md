# Q5 / homogeneous H6,J6 pointwise successor

Consume only a direct-replayed SAT model from the frozen global Q6/high gate.
The filtered source order descends next to Q5; it does **not** permit dividing
all low determinant coefficients by 243.

Adjoin homogeneous degree-six order-81 digits `(H6,J6)` (14 `F3`
coefficients).  Impose:

- the six degree-five source rows
  `G5 + (H6)_x + (J6)_y = 0`;
- after this restoration, all 63 terminal rows `R12,...,R7 = 0`, with the
  cross-carry of both `(H7,J7)` and `(H6,J6)` included.

Derive the exact affine 69-by-14 system by zero/unit substitution, verify
affine linearity on every pair of unit directions, compute matrix and
augmented ranks over `F3`, and either emit a canonical solution or a sparse
left-null inconsistency certificate.  Direct integer determinant rows at
degree five and degrees seven through twelve are replayed for any solution.

Strict scope is the two displayed SAT states only.  Failure is not a whole
base/fibre theorem; success is not a complete mod-243 map or lift.

