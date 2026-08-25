# V1 failed-aggregation custody record

The frozen V1 source ran on r6a at
`/home/ubuntu/jobs/as_active4_plus_one_20260825T034000Z`.  All 28 shard
processes printed their PASS sentinel with empty stderr, but the launcher
returned one because no `shard_*.json` files existed and aggregation failed.

Cause: `mixed_shard.py` replaced `OUTPUT_JSON` by `BOOTSTRAP_JSON` before
importing its parent and did not restore the requested final result path.  The
mathematical result therefore overwrote each bootstrap file.  V1 bytes and
remote outputs remain preserved as a deployment negative control and are not
promoted as result evidence.  V2 pins V1 and changes only this routing.

