# Modular fixed-builder experiment at p=1073741827

Created 2026-09-05 UTC to test whether the fixed full-chart builders can emit
the missing fibre rows without characteristic-zero coefficient swell.

The modulus is `1073741827`; GNU `factor 1073741827` returned the number
itself.  Each modular builder is a mechanical copy of its fixed exact-Q
builder with exactly two source-line substitutions:

1. `ring R=0,` becomes `ring R=1073741827,`.
2. `rows/<stem>_rows.tsv` becomes
   `rows_modular/<stem>_rows_p1073741827.tsv`.

No chart equation, monomial ordering, native division, gate, or localization
logic was changed.  The TSV is only a modular screen source.  Any later msolve
input must explicitly add/retain the Rabinowitsch equation and record source
characteristic 1073741827; a modular `[1]` is not an exact-Q certificate.

| Stem | Exact builder SHA-256 | Modular builder SHA-256 | Unified-diff SHA-256 |
|---|---|---|---|
| C_n16m12_M6_13_ell3_s3_V1_1 | b2f518d49e1f9058a8af56f9f0c1b0e232d1fb854257a719759a4b854991b38e | f62d14693856054f48a435094450e64699e9235bacb01609f639ce63d0e8b128 | c243a7c3e8df3f15567948f39feea422866513cf9b677254da9a176ddfccc4c8 |
| C_n16m12_M6_13_ell3_s3_V1_3 | 23daf3408493710d1865589e6e2c6806959a51f0bf8c86c47c0f86c337dc99eb | dd2e449f31ef02535b48314b10be9610e3b4f91670dcc434468b3f9d68059e22 | f08fe160915cf58551bb87980f8ccc9e390da827a22f3dc98c82dd1ac10b4d63 |
| C_n18m12_M2_9_ell2_s3_V1_8 | 7186aa33d3da9f2b5d45b41d5a6a1470ae766492e675706df5d6bcd6f503276f | 429229809e3f6174cd80d187ff20f0ca16d7dad6b20eef7a84bd0532576ee69b | 8e70c97aa0b3a016ae0631743ddc4d435ce833f66afbcc6700e1adc3f66f1017 |
| C_n18m12_M2_9_ell2_s3_V3_8 (completed control) | 9ae616df93be07cd63802f8bee4fbb94f89452f575a7cc2697dd4d177f4d2699 | abf0268705fb0ef22fe4240f77c6cc1e1a9fc28086fead11ecd07251a748ad7a | 92bf504b8b6fe15d1a1a224fc2531127dfdced7f6d0ab0a15b0f90e17fc3ef51 |
| C_n24m16_M12_17_ell1_s3_V1_2 | 17b90f1c47b7071279356c222bd497cc1b16f377a66390a4686351d51ff71fa9 | 410439e8ced197b072fff360674a46b5dbd36fcda6c5a2b00371ba06748b74d3 | 5a578202544c829642feb551532abf52e12bf292f08582dd7935010fe0001259 |
| C_n24m16_M12_17_ell1_s3_V2_1 | 442413745cb04e41faf4375af3e9913b2e89589da2eb673f105fc95405009915 | 8a82ddddb70d60b2749e2fe2b852c70853ed13073cb4fda19312da6af3fe8536 | 86e8cc6fb20f4f52128a54c44506dec403542fef6d948754d40b2afe3f907256 |
| C_n24m16_M12_17_ell1_s3_V3_2 | 700bc6f0deecb8704ed4be8e42af00b32416819dd9d4dbf78195f79946ab6739 | 71d4e9266d2c3526ba79ea23bbd29cd59ecd4ec33cfd7dedcce746fe5dcd310f | 5204b4ac208c70dee65ba38a1187cd0317ae3ea4389433c548b792a1d85b188c |
| C_n24m18_M9_20_ell1_s3_V1_9 | 652ac00e46cef3d680a2d75f851abf32742d985ffd0ae61c4cd8c214a2ae56f7 | bccf09db87779c8eca721d3c29aea5139e2d13f7ec8b610733d6848c14630df0 | 910345ae18bd6ec176db25760b06f4c275a4f099cf6ec711131a410f8931b720 |
| C_n24m18_M9_20_ell1_s3_V4_9 | 1fbdf9983332618af4a3ae672258a6623ccad6c36449bc12d28b2b5e0925a6b2 | 8957816323a67be760d7f3f0d9929be7b537790700559e2c747a7888651fd9c9 | eb438244acd74e7d13b781aa63b9910cef562034dd6bdcae14cc8e6817e6c9e0 |

Every unified diff has two removed and two added lines, corresponding exactly
to the substitutions above.

Jobs were launched with `setsid`/`nohup`, nice level 10, a 20-minute timeout,
and an initial 8 GiB virtual-address-space cap.  Remote live-job caps were
subsequently raised to 12 GiB, still within the authorized 8--12 GiB band.
Singular resets affinity to CPU 0
when invoked with `--cpus=1`, so the Singular child PIDs were explicitly
repinned after launch.  Logs and receipts are in each class's `jobs/`
directory with suffix `_builder_p1073741827`; outputs are in `rows_modular/`.

## Completed end-to-end control

The known complete `C_n18m12_M2_9_ell2_s3_V3_8` builder completed natively at
p in under about 25 seconds, versus about 3 minutes 43 seconds for the extant
QQ output.  It returned rc 0 and printed all required gates:

```text
NATIVE_GATE lead_h_is_yK=1
NATIVE_GATE level0_deg_x_before_minus_c=8
NATIVE_GATE target_xk_level0_nonzero=1
NATIVE_DONE equations=159
NATIVE_DONE max_nf_deg_x_after_minus_c=8
```

The resulting file has one header and 159 nonzero, five-field data rows.  Its
SHA-256 is
`c7645288e26b6e3cb313dcc216d0ac3f81bfe33d33fd5c7069ac0e06a7a1b109`;
it is byte-identical to the completed QQ TSV.  Strict `msolve_chart.py`
emission of (a) the QQ rows reduced to p and (b) the native-p rows, explicitly
recording the respective source characteristics and appending `z*c-1`, gave
byte-identical 160-generator msolve inputs with SHA-256
`aaab2e84684cdff1399ba624f987ca5b9d28e2eb7aae54d1137649d291cae8f3`.
The local comparison artifacts are in
`classes/C_n18m12_M2_9_ell2_s3/jobs/modular_control_compare/`.

## Rejected division micro-optimization

A separate control-only builder replaced Singular's `division()` call with
explicit degree-bucket long division by the y-monic divisor.  Its SHA-256 is
`df40f3eb62a7e5e4b4a166b76f9d7266364455fe120113ce3ab365a02a9e701a`.
It reproduced the control TSV byte-for-byte, but took 27.22 seconds and
148,912 KiB maximum RSS, versus 25.02 seconds and 149,212 KiB for the fixed
built-in-division builder.  Since it was about 9% slower and did not reduce
memory materially, it was not applied to any missing fibre.  Its builder,
rows, and logs are retained with suffix `_p1073741827_monic` under the M2
V3_8 class directories.

## Missing-fibre endpoint at the 12:32 UTC cutoff

The modular builders did not make the missing full-chart rows cheap enough
within this lane.  Every incomplete output below contains exactly the
42-byte TSV header (one line, SHA-256
`7f2d716d35087e97752089d9d8041944bd5a49fe5c1c4b1118591e1f3d587130`),
and its stdout reached only `NATIVE_GATE lead_h_is_yK=1`.  None printed a
second native gate or `NATIVE_DONE`; consequently none is a valid input to
`msolve_chart.py`, and none supplies algebraic evidence about the chart.

| Fibre | Endpoint | Runtime (s) | Maximum sampled RSS (KiB) | Detail |
|---|---:|---:|---:|---|
| M6 V1_1 | CUTOFF | 2816 | 11,554,740 | Targeted TERM at 12:32:13 UTC |
| M6 V1_3 | RESOURCE_CAP | at least 2646 | 12,562,080 | Explicit 12 GiB AS cap; stdout says `Singular error: no more memory`, `halt 14` |
| M12 V1_2 | CUTOFF | 2803 | 4,106,080 | Targeted TERM at 12:32:13 UTC |
| M12 V2_1 | CUTOFF | 2856 | 2,272,504 | Targeted TERM at 12:32:13 UTC |
| M12 V3_2 | TIMEOUT | 1200 + 2040 | 1,298,160 | Initial and restarted runs; both header-only; latter exact `/usr/bin/time` maximum |
| M9 V1_9 | CUTOFF | 2814 | 5,392,432 | Targeted TERM at 12:32:13 UTC |
| M9 V4_9 | CUTOFF | 2855 | 6,969,544 | Targeted TERM at 12:32:13 UTC |

The modular M2 V1_8 builder was deliberately stopped after 646.58 seconds
(maximum RSS 2,236,248 KiB) when its exact-Q builder completed and superseded
it.  Its header-only file therefore is not counted as a modular timeout.

For the long-running jobs, the original GNU `timeout` parents were detached
before their 1200-second watchdogs expired while the verified Singular
children remained live.  Their small `.stderr` resource summaries and `.rc`
values describe those killed wrapper processes, not the later Singular-child
endpoints; the sampled values in the table are authoritative.  The exception
is the V3_2 restart, whose retained `.restart.stderr` records rc 124, elapsed
34:00.04, and maximum RSS 1,298,160 KiB directly.

At 12:32:41 UTC, process-table checks on the local worker and workers
172.30.0.18, 172.30.0.166, and 172.30.0.254 found no
`builder_p1073741827.sing` process.  All remote transformed builders, modular
TSVs, stdout, stderr, rc, and driver logs were then synchronized back to this
chart box without touching exact-Q `rows/` files.
