# Hostile review: finite `x5=0` cylinder local-germ exclusion

Act as an independent hostile algebraic-geometry and source-fidelity referee.
Read these files in full:

- `xmodel/max12-912-order3-nu-q8-w0-x5-cylinder-local-germ-20260825.md`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/PREREGISTRATION.md`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/README.md`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/generate.py`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/generate_v2.py`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/generate_v3.py`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/replay.py`
- `cases/max12_912_order3_nu_q8_w0_x5_cylinder_local_germ_aws_20260825/MANIFEST.sha256`
- both V3 `input.sing`, `stdout`, `stderr`, `run.meta`, and `source.sha256`
  endpoints under that case's `aws_box02_v3/` and `aws_box03_v3/`
- the AWS replay endpoint under `aws_box02_replay/`
- the hash-pinned transitive sources
  `cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py`
  and `cases/max12_912_order3_fibre_20260824/order3_fibre.py` only as needed
  to check source provenance.

Do not browse, run shell commands, execute CAS, or perform new computation.
Use repository Read/Grep/Glob only.  Do not edit any producer or frozen file.
Write exactly
`xmodel/max12-912-order3-nu-q8-w0-x5-cylinder-local-germ-review-claude-20260825.md`.

The claimed theorem is deliberately local and narrow.  Over characteristic
zero, in the localization `x3!=0`, the full six-row source `X` and the
explicit cylinder

```text
B: x5=0, x1=x3, d2=d4=0, c*x3=1
```

have identical local schemes.  Therefore no finite point of `B` lies in the
closure *inside X* of `X intersect D(x5)`, hence none is a landing point of
the smaller selected open `D(w*x5*(x3-2*x5))`.  There is no claim at
`x3=0`, `x3=infinity`, coefficient/projective infinity, or for a separate
trajectory leaf contained in `B`.

Try to falsify every load-bearing step:

1. **Source identity.** Verify from the emitted V3 source that the six rows
   are exactly `(e1,e3,e5,e7,e2,e4)` from the pinned compiler; that `w`
   remains free; that the localization equation is `ib*x3-1`; and that all
   source rows and all six `w` derivatives reduce to zero modulo the full
   cylinder ideal.  Check no specialization to `w=0`, parity, terminal row,
   or aligned assumption slipped in.
2. **Rank exactly five.** Check that `J` really is the full `6 x 7` Jacobian
   in `(w,c,d2,d4,x1,x3,x5)`, all seven `6 x 6` minors are tested, and the
   displayed `5 x 5` minor is a genuine minor of that Jacobian.  Verify its
   exact value `(1024/1594323)*x3^6` is a unit on `D(x3)` and no bad
   characteristic issue enters the characteristic-zero claim.
3. **Tangent statement.** Check the stated coefficient tangent
   `(-a^-2,0,0,1,1,0)` and that `F_w=0`; in particular, confirm the report is
   right to retract any interpretation of the old augmented-rank equality as
   evidence of approach from `D(x5)`.
4. **Dimension and embedding dimension.** At an arbitrary geometric point
   `q in B`, audit carefully the inequalities
   `dim O_(X,q)>=dim O_(B,q)=2` and
   `embdim O_(X,q)=7-rank(J)=2`.  Challenge whether localization, residue
   field extension, nonreduced structure, or embedded components can break
   the inference `dim=embdim=2`.
5. **Regular local domain.** Check the use of the regular-local criterion and
   the inference that `O_(X,q)` is a domain at every geometric point of the
   finite cylinder.
6. **Equal-dimension quotient.** Audit the surjection
   `O_(X,q)->O_(B,q)` and the claim that its kernel is zero.  Explicitly
   challenge the statement that a nonzero ideal in this two-dimensional
   regular local domain forces quotient dimension at most one; flag any
   catenarity, height, or residue-field hypothesis that must be stated.
7. **Closure conclusion.** From zero kernel, verify scheme-theoretically that
   `x5=0` in a neighborhood of `q` in `X`, and hence
   `q notin closure_X(X intersect D(x5))`.  Check the direction of every
   inclusion and that the conclusion is neither merely tangent-level nor a
   false global component claim.
8. **Custody/software.** Verify the two accepted V3 endpoints are
   diagnostic-free, independent engine/order implementations with fixed
   hashes and one PASS marker; V1/V2 must remain negative software controls.
   Check replay and manifest coverage, and distinguish any custody nit from a
   mathematical defect.
9. **Firewall.** Reject any inference at the overlap `x3=x5=0`, at infinity,
   about Taylor/terminal reconstruction, other `(9,12)` leaves, all maximum
   twelve, Keller pairs, or JC2.  The final report's last paragraph may only
   name those next gates.

Give a final verdict exactly `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or
`REJECTED`.  Enumerate every issue and the smallest exact repair.  State
whether the source-local exclusion of the finite `a!=0` cylinder survives.
