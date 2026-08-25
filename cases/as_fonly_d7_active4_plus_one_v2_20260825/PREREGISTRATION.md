# V2 output-routing correction

V1 completed all 28 mathematical shard computations but failed closed before
aggregation because its bootstrap import replaced `OUTPUT_JSON` and the final
result was consequently written to the bootstrap path.  Preserve V1 bytes and
outputs as a deployment negative control.

V2 pins the V1 compiler SHA-256 and makes exactly two in-memory source edits:
save the requested output path before bootstrap import, and use that saved path
for the final JSON.  Re-run all 28 shards and the unchanged pinned aggregator.
No mathematical equation, coordinate, assertion, or discriminator changes.

