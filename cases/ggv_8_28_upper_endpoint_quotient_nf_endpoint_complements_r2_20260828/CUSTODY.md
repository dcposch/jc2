# R2 custody

- AWS host: `54.224.45.13`, `ip-172-30-0-106`, instance
  `i-0f089e64c378f5da3` (`r6i.4xlarge`, 16 vCPU, 128 GiB).
- Job: `ggv_endpoint_complement_q1p03_r2_20260828T174009Z_i0f089`, CPU 2.
- Runtime: 2026-08-28T17:40:19Z through 17:41:40Z; component elapsed
  72.13 s, maximum RSS 26,952 KiB, swap zero throughout.
- Frozen preregistration SHA-256:
  `5ed4151dc634517d3036dd469abc3f91f72a7cdd7c507a7000babecd56d0f693`.
- Frozen source manifest SHA-256:
  `0dcf4c1c4b929c99246988eda10942ca997b24740ab7c4fe91d38286c04a6e68`.
- Frozen source archive SHA-256:
  `dfb0448bcc5af30dbc4004e2e050fdb7273bcad287767c9fe744aa4de0fc5ed8`.
- Exact generated-reduction AWS preflight archive SHA-256:
  `fcff706e0da2c4927c7e820d2f293bbea784f1d394e692138b56779a937e93e5`.
- Failed full-pilot terminal archive SHA-256:
  `f59f382955f1b2f1c0fc7d497250a4e2651ca1307bbac2d6fe11f802df4b8dbf`.
- Failed node-1 saturation script SHA-256:
  `dce6893a04eda90801214de2a599acaeb8ebdff46760dcf0bef04a723f0fb7ef`.
- Failed node-1 saturation stdout SHA-256:
  `55b9fac200295af34bc10b11927ea222ae7262e66ed17e68f3c6f50b7ef6b749`.
- The raw terminal marker was `NO_VERDICT_OPEN_REMAINDER`; its frozen sidecar
  SHA-256 is
  `afd1323fc145452a8a3f192a9241822aa51e748ca5fb54d80ac5b806ca4df9d0`.
  This marker is explicitly superseded by `ADAPTER_FAILURE_NO_VERDICT` because
  it was emitted after the unhandled Singular diagnostic.

The terminal archive, remote checksum sidecar, raw marker, and preflight
archive are retained below `custody/`.  Source and raw evidence were not
rewritten after launch.

