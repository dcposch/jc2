# Selected-Q8 moving-v Hensel lift, order 16

This immutable custody package freezes the completed AWS order-16 run of the
moving-v coefficient-by-coefficient Hensel lift. The producing source remains
in
`cases/max12_912_order3_nu_q8_p127_hensel_coordinate_lift_aws_20260825/`;
its exact hashes are repeated in `run.meta` and the report.

Replay verification is lightweight and performs no CAS:

```sh
python3 cases/max12_912_order3_nu_q8_p127_hensel_order16_aws_20260825/verify.py
```

The mathematical scope is formal-local over `F_127` through
`(w-25)^16`. This is not rational reconstruction, global quotient-component
membership, characteristic-zero lifting, or a trajectory theorem.

