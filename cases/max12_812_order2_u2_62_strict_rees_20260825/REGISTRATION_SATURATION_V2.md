# Registration: dual-host V2 `j!=0` strict-Rees saturation

Status: running on two registered AWS hosts from one immutable archive and
one byte-identical Singular input.  No V1 endpoint is consumed.

Common custody:

```text
source archive SHA-256:
  4d084b2116f193938078f652f2e169ca898689be1f0837b6a4b55fdd44e3c302
strict_rees_v2.sing SHA-256:
  021654e753f1186874f10110d4338e7d9f9457afbfed75419407e87e3b00982c
engine:
  Singular 4.3.2 (4330, 64 bit), x86_64-Linux
timeout:
  14,400 seconds
registered UTC:
  2026-08-25T23:15:16Z
```

Lane 1:

```text
tag: max12_812_order2_u2_62_strict_rees_sat_v2_jsat_20260825T231400Z_r6d
host: ip-172-30-0-45 (r6d)
remote job directory:
  /home/ubuntu/jobs/max12_812_order2_u2_62_strict_rees_sat_v2_jsat_20260825T231400Z_r6d
launcher PID: 178772
Singular PID at registration check: 178796
memory cap: 268435456 KiB
```

Lane 2:

```text
tag: max12_812_order2_u2_62_strict_rees_sat_v2_jsat_20260825T231400Z_box03
host: ip-172-30-0-249 (Box03)
remote job directory:
  /home/ubuntu/jobs/max12_812_order2_u2_62_strict_rees_sat_v2_jsat_20260825T231400Z_box03
launcher PID: 123062
Singular PID at registration check: 123086
memory cap: 201326592 KiB
```

The input differs from V1 only by the mandatory third principal
localization `K=KR:(j)^infinity` after the `tau` and `rho` localizations.
All seven `Psi` rows are byte-identical.  The Shioda/Hall all-zero-load
elimination is intentionally not compiled into these runs; it remains an
orthogonal theorem and potential later optimization.
