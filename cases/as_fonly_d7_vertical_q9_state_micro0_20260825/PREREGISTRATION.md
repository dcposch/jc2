# Q9 shard-zero acceleration

Keep the frozen 27-way Q9 run active as the canonical single-stream check.
Independently partition its imbalanced structural-base interval `[0,81)`
into 81 one-base shards by running the same source-frozen compiler with
`SHARD_COUNT=2187` and indices `0..80`.

Combine those 81 outputs with already completed frozen macroshards `1..26`.
The hybrid aggregate must prove exact interval coverage `[0,2187)`, reproduce
all four predecessor totals, preserve every rank/fibre/base histogram, and
emit an ordered 107-leaf Merkle certificate.  Any mismatch or failed shard
is no result.  Promotion still requires agreement with the monolithic
shard-zero output and independent review.

