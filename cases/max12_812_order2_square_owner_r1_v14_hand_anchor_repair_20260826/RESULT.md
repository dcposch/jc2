# Result: `r=1` V14 hand-anchor repair

Date: 2026-08-26

Status: **DUAL-AWS MATHEMATICAL OUTPUT POSITIVE, VALIDATOR FAIL-CLOSED;
NO FORMAL ENDPOINT.**

V14 moved the hand-remainder check after the declarations.  Exact Q and
`F_65521` each returned engine `rc=0`, printed all twelve required markers
exactly once, and emitted identical marker-only stdout with SHA-256
`fc6ba5c3ec390a8aebf2991920cf8e05c63f64b275e253d79d3222eeac135dff`.
There was no Singular `?`, `// **`, `error occurred`, or `=FAIL` marker.

The validator still failed because it rejected any nonempty stderr, while
the evidence wrapper puts benign `/usr/bin/time -v` telemetry there.  Thus
V14 is preserved as a validator negative control; its mathematical bytes
are consumed only through the fresh V15 replay.  Evidence manifests are
frozen by `EVIDENCE.sha256` (SHA-256
`a855622483b2149df49b7ad6edbe668a77005a010758d8044d39047c9995425e`).

