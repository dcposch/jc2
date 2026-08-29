# AWS registration

Registered 2026-08-26 UTC before GO:

- Box03 `98.80.65.144`, job directory/tag
  `/home/ubuntu/jobs/max12_912_order3_d1_triple_root_moving_load_v11_20260826T054500Z_box03_forward`,
  forward, worker cap 8 GiB / 1800 s, nice 10.
- r6d `100.26.198.153`, job directory/tag
  `/home/ubuntu/jobs/max12_912_order3_d1_triple_root_moving_load_v11_20260826T054500Z_r6d_reverse`,
  reverse, worker cap 8 GiB / 1800 s, nice 10.

Live prelaunch audit at `2026-08-26T05:48:06Z`: Box03 load 9.00 with
445 GiB available; r6d load 6.02 with 330 GiB available; both have zero
swap.  Existing workers, including r6d PID `185517`, remain untouched.  Both
registered job directories were absent.  The exact compiler runs only on
these two AWS hosts.  Teardown may remove only the two unique job directories
after immutable outputs are harvested; do not terminate a host or unrelated
process.

