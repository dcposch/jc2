# K00-REES-SANDWICH V1 quarantine receipt

UTC: 2026-08-30  
Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Lifecycle: `QUARANTINED / NO VERDICT / NEGATIVE CONTROL FOR V2`

## Exact process and custody

The first AWS process used campaign host r6b, instance
`i-0f089e64c378f5da3`, boot
`3dca2ad4-9cbb-48f9-9c62-02d37a90bd19`.  The registered launcher was PID
33354, start tick 12392959.  `CAPRUN/v1` registered Singular PID/PGID 33378,
start identity
`boot=3dca2ad4-9cbb-48f9-9c62-02d37a90bd19;start_ticks=12392967`.
It ended normally after 517.345730393 wall seconds with maximum observed
aggregate RSS 28,385,280 bytes.  PIDs 33354, 33377, and 33378 were all absent
at the post-run audit.

The immutable input packet-manifest file has SHA-256
`25946344ff3d5b62c5c120860b3b0937cab2a16f84ff2e848b601b6530b7746f`.
The frozen output manifest is `V1_QUARANTINE_RESULTS.sha256`, SHA-256
`a53c3e6b94b1fc541add399daf88c7883784894d7ef5c4cebaca85dfc174ace3`.

## Defect and typing

After the adaptive membership loop, the script changed from source ring `R`
to target ring `H` and then evaluated

```text
poly fifthPlane=scaledPlane(f0^5);
```

The ring-local name `f0` was no longer defined.  Singular 4.3.2 emitted five
diagnostic lines, beginning with

```text
   ? `f0` is not defined
```

and also reported that `fifthPlane` was undefined.  Singular nevertheless
continued after the failed statements and printed the script's unconditional
terminal PASS line.  The V1 runner required that PASS line and rejected only
explicit `K00_REES_FAIL=` markers; it did not reject generic Singular
diagnostics.  It therefore incorrectly wrote `lane_status=PASS` despite the
five diagnostics.

This is a source/runner failure, not mathematical evidence.  Every line from
this process, including all apparent containment lines and the apparent
smallest-exponent line printed before the defect, is quarantined as
`NO VERDICT` and must not be quoted as a theorem, calibration, or replay
input.  The witness files are retained only for incident custody.

V2 must start from the original immutable prelude and multiplier files in a
new directory and process.  It must avoid the stale ring-local reference,
reject generic Singular diagnostics, and first run a planted undefined-symbol
script containing a fake PASS marker to demonstrate that the repaired output
validator rejects exactly this failure mode.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `2417`.
- Body SHA-256:
  `8b8f5cbcb79f550b82e759662da1ccd747b693c136d9ce1c2f4d1bae0053e711`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
