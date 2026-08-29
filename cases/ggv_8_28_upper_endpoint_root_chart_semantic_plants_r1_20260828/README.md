# TRIPLE03 root-chart semantic-plant replay

This case retrospectively replays the frozen TRIPLE03 root open chart with
fail-closed semantic controls for endpoint-zero detection. It preserves the
original chart bytes and regenerates the original delta, endpoint-coefficient,
and bordered-identity artifacts byte for byte.

The production result is exact and narrowly scoped:

`TRIPLE03_ROOT_D_DELTA_ENDPOINT_DEAD_WITH_SEMANTIC_PLANTS`

See `RESULT.md` for the root-open verdict, `UNION_THEOREM.md` for the explicitly
conditional root-open/closed-complement union, and `CUSTODY.md` for AWS custody.
No result here applies to another component or to the ambient HENS-CT problem.
