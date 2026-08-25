# Registration: V2 `j!=0`-localized strict-Rees gate

Status: source-frozen; exact AWS emission complete; dual-host AWS saturation
running under `REGISTRATION_SATURATION_V2.md`.

V2 imports the frozen exact-tail compiler, requires the frozen client
erratum, preserves all seven tail polynomials byte-for-byte, and changes
only the Singular interior saturation from `tau,rho` to `tau,rho,j`.
The Shioda/Hall all-zero-lower-load optimization is explicitly absent.

Compilation uses a 128-GiB cap and 7,200-second timeout.  Saturation uses
the existing AWS-only runners (256 GiB on r6d, 192 GiB on Box03) and a
14,400-second timeout.  Each launch records host, remote directory, PID,
input hash, engine version, and UTC start before the payload.

No V1 endpoint is consumed.  A V2 unit endpoint would exclude strict tail
arcs for this fixed source only; either outcome leaves both Taylor families
and rational-section descent open.

The exact compiler run was
`max12_812_order2_u2_62_compile_v2_jsat_20260825T231200Z_r6d`.  It emitted
`strict_rees_v2.sing` with SHA-256
`021654e753f1186874f10110d4338e7d9f9457afbfed75419407e87e3b00982c`.
The evidence manifest is `aws_compile_v2_jsat/MANIFEST.sha256`.
