# Independent hostile implementation review: `T-rs-0` discovery

Work in `/Users/dc/code/math/jc2`.  This is a read/audit task.  Do not edit
the producer package, top-level ledgers, or `jc2-lean`; write only the report
named below.  Do not run Singular or any heavy algebra locally.

Read completely:

1. `xmodel/max12-812-order2-p0-total-rees-t-rs-implementation-audit-codex-20260826.md`
2. `xmodel/max12-812-order2-p0-total-rees-gate-t-obligation-table-20260826.md`
3. every source file in
   `cases/max12_812_order2_p0_total_rees_t_rs0_discovery_20260826/`
4. `cases/max12_812_order2_p0_cusp_g10_g11_20260826/compile_p0_cusp_g10_g11.py`
5. `cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_v2_20260826/compile_raw_cusp_g12_cech_v2.py`
6. `cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py`

The V0R1 two-prime AWS discovery is live.  Audit source and logic rather than
trusting any future PASS marker.  In particular:

- rederive the corrected total family and determine whether the candidate
  ceilings `12,10,10,7,7,7,7,8,0` for `p,C,R,A1,A0,E1,E0,K10,K6` are a
  genuinely complete prefix ceiling modulo `sigma^13`;
- check that the primitive coefficient dictionary is exactly the frozen
  owner dictionary with only the intended total-series extension;
- check use of the quotient by `sigma^13`, recursive division/extraction,
  multiplication-back checks, deck involution, and the coefficientwise
  `rho=0` comparison; look for any zero-divisor or quotient artifact;
- check the reviewed V2 cusp certificate and `-1536*cs*c0*c1` omission
  residue as implemented;
- attack the literal-wrong-`p`, synthetic omission, dependency-manifest,
  inactive-source, and `Delta/rho^2` controls;
- inspect the Python validator for missing/duplicate-marker, malformed
  integer, false-PASS, characteristic, hash, or scope vulnerabilities;
- distinguish what a two-prime V0 agreement would establish from what still
  requires exact Q and from the later Rees/base-change computation.

Do not require V0 to know its minimal manifest: discovery is its declared
purpose.  Do require the *candidate ceiling* to be proved complete and the
output sufficient to freeze a minimal V1 manifest.  If a defect is found,
give the smallest exact repair and a negative control that would catch it.

Write
`xmodel/max12-812-order2-p0-total-rees-t-rs0-discovery-implementation-review-grok-20260826.md`
with SHA pins, an attack table, and one final verdict:

- `GO_TO_FREEZE_V1_MANIFEST`,
- `REPAIR_BEFORE_V1`, or
- `NO_VERDICT`.

No total-Rees, moving-`p`, order-two, maximum-twelve, or JC2 theorem can be
promoted from this review.
