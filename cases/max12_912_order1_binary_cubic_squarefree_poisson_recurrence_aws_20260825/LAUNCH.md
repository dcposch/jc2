# Launch custody

The accepted V4b jobs were staged from the exact `SOURCE.sha256` closure and
refused Darwin, non-Linux, a wrong hostname, a missing registered tag, and a
non-AWS DMI vendor.  The r6d run started at `2026-08-25T19:24:42Z`; Box02 at
`2026-08-25T19:25:17Z`.  Centralizer peak RSS was 15,252/15,576 KiB and
Singular peak RSS 13,408/12,580 KiB on r6d/Box02.  Every timed command exited
zero.  Exact tags and hostnames are retained under `evidence/*/out/`.

The V1, V2, and launcher-permission failures are immutable negative custody
under `evidence/`; only V4b is the accepted endpoint.
