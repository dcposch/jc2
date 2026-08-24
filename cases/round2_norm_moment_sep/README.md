# `NORM-MOMENT-SEP` bounded exact gate

This directory contains the frozen preregistration, a standard-library exact
receiver/control implementation, and a compact result certificate for the R
root launched on 2026-08-24.  The preregistered hard stop fired at
`DIFFERENT-INSUFFICIENT`; the native GGV source type gate was not executed.

## Replay

From the repository root:

```sh
python3 cases/round2_norm_moment_sep/norm_moment_sep.py \
  | LC_ALL=C shasum -a 256
```

Expected deterministic stdout digest:

```text
c81c75b0cc3721f1198d3dc049f66cd3c87fdb24c81e6542d7cecfd15bffae96  -
```

The output is 41,522 bytes with the frozen inputs.  Check the decisive gate:

```sh
python3 cases/round2_norm_moment_sep/norm_moment_sep.py | jq -e '
  .status == "STOPPED" and
  .verdict == "DIFFERENT-INSUFFICIENT" and
  .stages.receiver_controls == "PASS" and
  .stages.fixed_different_separator == "PASS_STOP" and
  .stages.native_source_type_gate ==
    "NOT_REACHED_BY_PREREGISTERED_HARD_STOP" and
  .derivation_checks.all_agree and
  .fixed_different_varying_moment.same_local_algebra and
  .fixed_different_varying_moment.same_different_and_conductor and
  .fixed_different_varying_moment.same_retained_decoration and
  .fixed_different_varying_moment.same_local_jacobian_data and
  .fixed_different_varying_moment.same_coordinate_valuations and
  .fixed_different_varying_moment.same_x_first_principal_part and
  (.fixed_different_varying_moment.same_x_second_principal_part | not)
'
```

The implementation uses only exact integers/fractions and sparse Laurent
polynomials over `QQ[q]`.  It computes no moment above two, does no sampling or
network access, and imports no round-1 producer code.  Record hashes cover the
canonical JSON body before its `record_sha256` field is inserted; the complete
deterministic stdout is separately content-addressed above.

## Perimeter

The result separates a quadratic coordinate moment from the displayed local
finite algebra, different/conductor, retained contact decoration, valuations,
and local Jacobian two-form.  The separating Darboux records are exact formal
local controls, not polynomial Keller maps.  The result therefore makes no
claim of trace regularity, integrality, properness, a global separator, or a
proof/disproof of the plane Jacobian conjecture.
