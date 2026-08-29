# AWS registration

Registered 2026-08-26 UTC before GO:

- Box03 `98.80.65.144`, job directory/tag
  `/home/ubuntu/jobs/max12_912_order3_d1_triple_root_weighted_two_chart_v10_20260826T050400Z_box03_forward`,
  forward, worker cap 8 GiB / 1800 s, nice 10.
- r6d `100.26.198.153`, job directory/tag
  `/home/ubuntu/jobs/max12_912_order3_d1_triple_root_weighted_two_chart_v10_20260826T050400Z_r6d_reverse`,
  reverse, worker cap 8 GiB / 1800 s, nice 10.

Prelaunch fleet audit: Box03 load 12 with 455 GiB available; r6d load 7
with 336 GiB available.  Existing registered jobs, including r6d PID 185517,
remain untouched.  Local placement audit found zero campaign-owned heavy
workers and stopped none.  This exact compiler runs only on the two AWS
hosts.  Teardown policy: remove only these two unique job directories after
their complete immutable outputs have been harvested and checkpointed; do
not terminate either host or any unrelated process.
