# AWS custody supplement: hostile review of the TD6 two-center cover

This is a separate, immutable execution supplement for the hostile review

```text
xmodel/td6-c1-c3-two-center-cover-review-claude-20260825.md
SHA256 56c4ece1224c723f8bbe107f0c9af6776dc0affcb03923a394628838923bde19
```

It does not modify the producer freeze
`cases/td6_c1_c3_two_center_cover_20260824/`.  Its sole purpose is to close
the shell-bearing execution condition in section 11 of that review.

The final independent stdlib-only probe was run on AWS Box03 from
`/home/ubuntu/td6_review_probe_20260825` with

```text
/usr/bin/time -v python3 probe.py
```

and exited `0`.  The stdout contains 108 explicit `PASS` assertions, four
`INFO` provenance lines, and the final line
`PROBE PASSED: all checks succeeded`.  The 114-line stdout should therefore
not be described as “114 PASS assertions.”  Maximum RSS was 19,040 KiB and
wall time was 0.10 seconds.

The first staged attempt stopped before mathematical checks because a macOS
AppleDouble top-level archive entry was selected as the extracted payload.
The frozen `probe.py` fixes only that harness issue by selecting the extracted
directory explicitly.  The final run is the charged run.

The probe independently:

- recomputes the charged and manifest hashes;
- verifies exhaustive manifest coverage and each run-meta stdout/stderr pin;
- extracts V4--V7 and verifies every archived `SOURCE.sha256`;
- pins producer hashes and byte-compares archived parents with the staged
  parent modules;
- recomputes the generic/B-local/H-zero denominator identities and
  resultants with a from-scratch rational polynomial engine;
- rechecks the quotient-field unit certificates, irreducibility witnesses,
  `k`-inverse, norm noncube, and the `U=0`/origin residual agreement.

Thus this supplement confirms execution of the reviewer’s independent probe.
It adds no new mathematical scope: the promotable statement remains exactly
the fixed source-typed normalized section `(c1,c2,c3)=(C,1,U)` at the
first-band/P12 gate.  It says nothing about `c2 != 1`, a neighborhood, SP-2,
maximum degree, or JC2.

## Files

- `probe.py`: exact final probe executed on Box03;
- `evidence/probe.stdout`: final stdout;
- `evidence/probe.stderr`: `/usr/bin/time -v` stderr;
- `evidence/charged_gate.md`: exact charged producer report staged remotely;
- `RUN.meta`: host, command, hashes, and outcome;
- `MANIFEST.sha256`, `FREEZE.sha256`: custody pins.

