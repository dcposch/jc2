# D1 double-root normal-chart AWS jobs

Date: 2026-08-25

This packet is separate from the parent global slope compiler.  It fixes the
unique projective discriminant point, retains all six normal directions, and
computes structural/Newton and exceptional-fibre local data only.  It does
not alter, replace, or serialize behind the global strict-Rees saturation.

All workers start behind a `GO` sentinel.  Their exact PIDs are recorded here
before any substantive Python or Singular payload is released.

- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_newton_20260825T230403Z_box03`,
  structural axis/cusp/Hermite/Newton compiler SHA-256
  `1726585d7e01256010096904370fa0fdb67019ba1b0f650aecab9880ec062751`;
  worker PID `120806`, held behind `GO` until this record; `timeout 1800`,
  16-GiB virtual-memory cap,
  `nice -n 10`.
- r6d `100.26.198.153`,
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_newton_20260825T230403Z_r6d`,
  byte-identical structural custody mirror; worker PID `176489`, held behind
  `GO` until this record;
  `timeout 1800`, 16-GiB virtual-memory cap, `nice -n 10`.
- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_exact_20260825T230403Z_box03_dp`,
  exact-tail compiler SHA-256
  `2fb9929f6ff4f47866005c68dcdec06cfd07cea0c66833a5509b182d4d52130c`
  followed by its emitted Singular `dp` standard basis; worker PID `120809`,
  held behind `GO` until this record; compiler timeout `1800`, Singular
  timeout `5400`, 64-GiB virtual-memory cap, `nice -n 10`.
- r6d `100.26.198.153`,
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_exact_20260825T230403Z_r6d_lp`,
  byte-identical exact-tail compiler followed by the independently emitted
  Singular `lp` standard basis; worker PID `176492`, held behind `GO` until
  this record; compiler timeout `1800`, Singular timeout `5400`, 64-GiB
  virtual-memory cap, `nice -n 10`.

The charged ordinary source for both compilers is
`independent_reconstruct.py` at SHA-256
`67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623`.

Harvest checkpoint: the Box03 `dp` exact basis completed with compiler rc 0,
Singular rc 0, empty stderr, `BASIS_SIZE=101`, and `VDIM=125`.  Its stdout
SHA-256 is
`2535262b4149a3ab72d498b38f0d7d38cdc589a78364c4bbbe662620005fea55`.
The r6d `lp` basis remained live at the freeze checkpoint under worker PID
`176492`; its compiler had rc 0 and the emitted input SHA-256 is
`9c621d39c4434078a3effde075f20d18eb06a1f17be87dfc142a13dfb81348c1`.

Both first structural workers failed closed before algebra because the base
Box03/r6d Python installations do not contain `sympy`.  Their rc/stderr are
retained.  The exact-tail compiler does not depend on `sympy` and completed
successfully on both hosts.  The structural repair is the following direct
Singular identity check:

- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_newton_v2_20260825T230745Z_box03`,
  source SHA-256
  `774bed3583944de1362eccaa037689872cc3f4dea694b69d1b35c5f2c25d8f45`;
  worker PID `121569`, held behind `GO` until this record; `timeout 1800`,
  16-GiB virtual-memory cap,
  `nice -n 10`.
- r6d `100.26.198.153`,
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_newton_v2_20260825T230745Z_r6d`,
  byte-identical direct-Singular custody mirror; worker PID `177257`, held
  behind `GO` until this record;
  `timeout 1800`, 16-GiB virtual-memory cap, `nice -n 10`.

Both V2 Singular processes returned shell rc 0 but their nonempty stderr
showed a parse failure at the rational coefficient `q^2/3`; Singular then
continued to the printed marker.  V2 is therefore quarantined.  V3 declares
`number third=1/3`, exits before the marker on any failed identity, and its
launcher additionally requires empty stderr plus the unique PASS marker:

- Box03 `98.80.65.144`,
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_newton_v3_20260825T230926Z_box03`,
  source SHA-256
  `ab59360a00b286c7e8b1f1094f61914735142faa55356ba769ccc02c5bac4277`;
  worker PID `121984`, held behind `GO` until this record; `timeout 1800`,
  16-GiB virtual-memory cap,
  `nice -n 10`.
- r6d `100.26.198.153`,
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_newton_v3_20260825T230926Z_r6d`,
  byte-identical V3 custody mirror; worker PID `177497`, held behind `GO`
  until this record; `timeout 1800`, 16-GiB virtual-memory cap,
  `nice -n 10`.

Both V3 workers completed with rc 0, empty stderr, the unique terminal marker
`PASS-D1-DOUBLE-ROOT-NEWTON-STRUCTURE-V3`, and byte-identical stdout.
