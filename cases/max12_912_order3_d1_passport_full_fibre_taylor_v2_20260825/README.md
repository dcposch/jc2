# Cyclic-D1 full-fibre/Taylor gate V2

This is a nonmutating successor to the immutable V1 source/preregistration
freeze.  V1's first AWS smoke failed closed because its staged closure omitted
two parent transitive freeze files.  See `DEPLOYMENT_ERRATUM.md`.

V2 adds:

- `independent_reconstruct.py`: independent Faber/inverse/tail arithmetic;
- `compile_gate_v2.py`: exact comparison with the frozen parent, corrected
  character descent, and source-row emission;
- `stage_a_interface.py`: generic absolute-decomposition navigation plus an
  exact constant-field section-certificate verifier;
- `stage_b_taylor.py`: exact 18-parameter/23-coordinate Taylor-ideal compiler
  for one certified Stage-A section;
- `stage_b_membership_controls.py`: certificate-free exact synthetic coverage
  of the `C[x]` membership routine, including its zero-quotient branch;
- `run_modular_msolve_portfolio_aws.sh` and
  `run_sretained_modular_navigation_aws.sh`: AWS-hardened finite-field
  navigation runners; their output is never a characteristic-zero section
  theorem;
- `SECTION_CERTIFICATE.example.json`: schema example only, deliberately not a
  claimed D1 section;
- `PREREGISTRATION_V2.md`: theorem semantics, stop rules, and scope firewall.

No V2 source has been executed locally.  Until AWS source equality passes,
all V2 mathematics remains source-only.  Generic Stage-A output is explicitly
navigation-only over the full coefficient field `Q(s,k,mu,nu)` (hence it
retains no special load divisor), and Stage B cannot run without an exact
Stage-A section.  The `mu=0`, `nu=0`, and discriminant strata require separate
later jobs.

## Proposed AWS sequence

From a closure-complete staged repository on a registered Amazon EC2 host,
use the hardened runner.  `D1_RUN_DIR` must not already exist; the runner
refuses duplicate tags/directories and verifies EC2 DMI identity before any
Python or Singular process starts:

```sh
export JC2_AWS_TAG=max12_912_order3_d1_v2_<UTC>_<HOST>
CASE=cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825
export D1_RUN_DIR=/home/ubuntu/jobs/${JC2_AWS_TAG}_results
test ! -e "$D1_RUN_DIR"
bash "$CASE/run_source_and_generic_aws.sh"
```

For a bounded source/row/emitter replay that deliberately does not start a
second generic decomposition, set `D1_SOURCE_ONLY=1`; the same closure,
EC2, tag, and fresh-directory checks remain mandatory.

If and only if Stage A yields an explicit constant-field section certificate,
continue under the same EC2 identity/tag guard:

```sh
python3 "$CASE/stage_a_interface.py" \
  --section-verifier "$D1_RUN_DIR/section.json" \
  >"$D1_RUN_DIR/verify_section.sage"
sage "$D1_RUN_DIR/verify_section.sage" \
  >"$D1_RUN_DIR/verify_section.stdout" \
  2>"$D1_RUN_DIR/verify_section.stderr"
sage -python "$CASE/stage_b_taylor.py" \
  --certificate "$D1_RUN_DIR/section.json" \
  --output "$D1_RUN_DIR/taylor_ideal.json" \
  >"$D1_RUN_DIR/taylor_compile.stdout" \
  2>"$D1_RUN_DIR/taylor_compile.stderr"
```

The certificate-free membership controls may be run earlier, but only on an
EC2 host with the same DMI/tag preflight:

```sh
export JC2_AWS_TAG=max12_912_order3_d1_membership_<UTC>_<HOST>
/home/ubuntu/venvs/as-sympy-1.13.3/bin/python \
  "$CASE/stage_b_membership_controls.py"
```

The modular runners are routing controls.  The fixed-specialization
portfolio checks finite algebras after all four load coordinates have been
specialized.  The `s`-retained runner fixes `(k,mu,nu)=(1,1,1)` over
`F_32003` while retaining `s` as a ninth variable.  Neither result can
certify or exclude a geometric degree-one component in characteristic zero.

Every command must run from repository root so relative source paths and pins
resolve.  Record hostname, PID, archive/source SHA, command, rc, elapsed time,
and maximum RSS.  Do not infer a theorem from the generic job alone.
