# K=7 beta-strata exact-Q certificate lane, round 3b

Lane `k7-cofactors-sol56-r3b-20260906`; frozen input root
`/tmp/jc2-lane.zrFRwF/inputs`; compact machine record
`box/k7-cofactors-20260906/r3-custody.json`. This was a certificate-only
relaunch. No ledger, `jc2-lean`, or `ideation-*` file was used as input or
edited.

## Verdict

**b9 q1 and b10 q1 are CERTIFIED-Q** by completed exact-Q reduced bases
literally `{1}`. **b9 q0 is STILL-SIGNAL-ONLY**: its four full 241-row runs
reached their 180-minute resource walls, and no later exact route completed a
unit basis or rational cofactor identity. Hence b10 becomes unconditional;
b9 does not.

The acceptance rule was kept literal. A chart is `CERTIFIED-Q` only when this
lane has either an explicit rational cofactor identity checked by fresh exact
multiplication in the full original ring, or a completed exact-Q reduced basis
whose fully delimited body is the singleton `1`. msolve `[-1]:`, finite-field
unit signals, partial transcripts, and computations stopped at a resource wall
are not certificates.

| charged chart | theorem-tier result | stratum consequence |
|:--|:--|:--|
| b9 q0 | **STILL-SIGNAL-ONLY**, exact resource wall | not unconditional |
| b9 q1 | **CERTIFIED-Q**, exact-Q reduced basis `{1}` | b9 still also needs q0 |
| b10 q1 | **CERTIFIED-Q**, exact-Q reduced basis `{1}` | with frozen b10 q0, **b10 is UNCONDITIONAL** |

Thus the frozen round-2 census of 7/10 theorem-tier charts rises to
9/10. The already certified b11, b12, and b13 strata are unchanged.

## 1. Frozen-input verification and custody

Before CAS work, `awk` mechanically paired every numbered
`charged_input_<i>_basename` and `_sha256` field in the lane receipt and wrote
the check manifest. `sha256sum -c` returned seven `OK` lines and no mismatch:

```text
1ffd191ae1ce427ddaa6941c2b80664e0d30e6520cf07ba50e82a65d03135aac  k7-cofactors-sol56-r2-20260906.md
913167e2a53e60eb5da58ce122339e3754badc460ae8c90038f40cdcf7ac026f  r2-custody.json
78edece02efa7223d9130aa334416339f69c10de6d3cf4c6b7873581b791e1f8  k7-strata-gate-sol56-20260905.md
c16199138f4e93d3babdde1372e0000fb02ef831e1dd2b9e143d486bb0a6b6ac  k8-b11-q1-sol56-20260905.md
95d12f5b23975e8699b634b1ba8c6f0e6fc4e24abfcd4bad2db936e1c74e9826  guided_gb.py
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

The manifest is 805 bytes, SHA-256
`beb8226199638903025d74959d677f4eb3d38e29a028a3ab56a2a58c1330559e`;
the checker stdout SHA-256 is
`1a6b26d402e491e6fbbae763b611fd721f2cf17adf84563484a83e7495be9106`.
Receipt SHA-256 is
`dc005b936794b5c4eebb6c0e6e87acdd5f0dddddeb85f1208ea65fd288498104`.

Host `/` was checked before any lane write: 96 GiB total, 12 GiB available,
88% used. The prompt's literal `fleet.sh launch r7i.8xlarge` was attempted
first, but this frozen driver parses its first positional argument as a count;
AWS rejected the malformed request before creating an instance. The documented
explicit-count equivalent, `fleet.sh launch 1 r7i.8xlarge`, created exactly
one lane-owned worker:

```text
instance  i-028a9c1579ea72e67
private   172.30.0.77
type      r7i.8xlarge
Owner     k7-cofactors-sol56-r3b-20260906
launched  2026-09-06T04:31:58Z
```

`fleet.sh wait` provisioned it and installed msolve 0.10.1. Singular 4.3.2
had binary SHA-256
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`;
the msolve binary SHA-256 is recorded in the custody JSON. All CAS inputs,
scripts, logs, temporary files, and an unused-at-seal guarded swap file stayed
below `/home/ubuntu/k7-cofactors-r3b-20260906` on that worker. No CAS log or
identity was copied to the host.

## 2. Rings, generator bytes, and exact row maps

The authoritative sources are denominator-cleared integral msolve lists in
their frozen one-based order. The first line gives the geometric names; the
Singular conversion maps its `i`th name positionally to `v_(i-1)`, checks the
image, and declares characteristic zero. The chart data are:

| chart | variables/generators | source SHA-256 | chart coordinate; inverse; localizer row |
|:--|--:|:--|:--|
| b9 q0 | 72/241 | `15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275` | v69; v71; 241 |
| b9 q1 | 71/235 | `09002c7229da517ca0d809f925873aeb94d44650467bd6addf71268aacbb7934` | v69; v70; 235 |
| b10 q1 | 78/255 | `a49433e9834c4fa7a76a89aef50e7f3852ee0e26ff1d665bc1c8516dc390f97d` | v76; v77; 255 |

Every basis script used `ring R=0,...`, `option(redSB)`, `short=0`, and either
`dp` or the exact positive `wp` vector frozen in the strata metadata. In
particular, “weighted” here is not an invented heuristic block: it is the
authoritative chart bigrading recorded by the charged gate. Complete literal
bases were placed between unique begin/end delimiters.

The successful cores were freshly rematerialized from the frozen sources, not
trusted from an old output. For b9 q1 the 124-row core has SHA-256
`f0f8d5886623eb78ecc5761e459336f3ebda27f5237cafbc5181667b954e6b8b`.
Its map receipt has SHA-256
`b314139fe63e2f384accfe4c51298b7604c2f9c54e1cf86938707738498cdaa4`
and records equal variable/field headers, counts 235/124/124, strictly valid
indices, every selected polynomial byte-equal to its source row, and the
unchanged localizer at index 235. For b10 q1 the corresponding 48-row core SHA
is `67906ac61f1e6a1034bb14081ae943f46b852a7fadd39d99ba30a5e0befa65fb`;
the fresh map-check output SHA is
`cd12fff4258dfb3002b90cecc8ede76bd4e5f61ec3f0c4e41be7a18f794c20af`.
It records counts 255/48/48, equal headers, no mismatch, and original indices
21-48, 54-57, 62-66, 75-79, 85-88, 254, 255. Since each core ideal is a
subideal of the full source ideal, a proved unit in the core proves a unit in
the full chart.

## 3. b9 q1: exact-Q singleton basis

The b9 q1 core used original indices
`11-17,19-28,30-42,44-50,61-75,77-90,92-108,110-131,133-148,150,234,235`.
The exact-Q `dp`/`slimgb` computation ran from 05:05:45Z to 05:30:49Z:
25:03.92 wall, 1,723,112 KiB maximum RSS, exit 0, and 1,502 Singular seconds.
Script/output/timing SHA-256 values are respectively
`7f59e7ce62aadcc50269df3f8b0c107a63f9589287c72ea9b5ca54694898964a`,
`ad491bcbc67df30a07b7ceaba7eef19099303cec48a004b48fdbf4f8c035a25c`,
and `a6ea85513dfc71db77177cb9a1b9323e5b9b2b3d7a285acadf8326c8a950ee52`.

A fresh strict audit required exit 0, the Q/dp/slimgb/redSB declarations, one
begin marker, one end marker, `GB_SIZE 1`, and `UNIT 1`. The raw bytes between
the delimiters were exactly hexadecimal `31 0a`, i.e. `1` plus newline. This
is the authorized exact-Q reduced-basis certificate; no cofactor or modular
promotion is claimed. A final two-chart recheck at 07:59:10Z took 0.16 s and
returned `ALL_PASS=1`; its JSON SHA-256 is
`e1d8477ab765cf6a93260e845c10c9797201cd084ed7d9f1ef7561874a8940cb`.

## 4. b10 q1: exact-Q singleton basis

The b10 q1 48-row core exact-Q `dp`/`slimgb` run began 04:39:32Z and completed
05:51:50Z: 1:12:17 wall, 4,335 Singular seconds, 3,346,144 KiB maximum RSS,
exit 0. Script/output/timing SHA-256 values are respectively
`6e4da295eae1216d4c17d08c8a3e122a759c5eef95f1284a4a9cede3d9dadb19`,
`f0289c5d5259d02c7fcc2e3d71ceda781e8bf5ce01db0d1da94fc4f4ef500e0f`,
and `0ccc46d58fc7c410056de1b90d3196f722ab824aa0c3cead12a8b27589cd9be5`.
The independent audit again found exactly one delimiter pair, raw basis body
`31 0a`, `GB_SIZE 1`, `UNIT 1`, and the required exact-Q options. This is a
second literal singleton reduced basis. The redundant b10 full/core `std` and
`slimgb` competitors were stopped only after this certificate; their incomplete
logs contain no basis delimiters and are not adverse algebraic results.

## 5. b9 q0 exact work and final classification

All four authoritative 241-row runs began at 04:37:07Z and received their
complete 10,800-second wall. None printed a basis delimiter. Their exact
Q/redSB results were:

| order/algorithm | wall; max RSS | script / timing SHA-256 |
|:--|:--|:--|
| dp/std | 3:00:02; 77,463,056 KiB | `248d80fd56f73b3955a1bf26a6c48a37d1fb7094d6ed9bd0708167f5dd0e6dd0` / `8c34f0f715f67ea74db0dc8f399b22a4a79c722828fe90a5e3ad53e0104a02ee` |
| dp/slimgb | 3:00:00; 2,445,688 KiB | `d7ed47bbf34a436cac0dd277eb17a3fb84ae641070f9af08dd3b3b2f3a952b07` / `533e2a0898e7d1438cf41269d52599863d63817bb556a2caf2464320b7b26c2c` |
| wp/std | 3:00:00; 20,399,828 KiB | `25186f8f168b5f4e9bfd500689398dd936f8471e6a965c79382fab1a9f9671a0` / `b93187c3307f12c9c4cbda5b801a38b3c39b3b9378485c3684fbc306a48fbd53` |
| wp/slimgb | 3:00:00; 1,122,860 KiB | `ec2378b0a4d5e3540b3dbfca8fafa9aa5317e5d2fa1568fd5181a5dec3efd791` / `a0fa958b7e51bacb7a4e694026924fde53988873e6439f61b04f003c156ba665` |

Each exited at the watchdog with `rc=124`; each stdout was exactly
`CERT__NGEN 241`, a blank line, and `halt 1` (common SHA-256
`676bc8d165fc7ae65625dc383fa52e0ca88309e9623a5baab6b5ddf7a5d524a9`).
These are exact resource walls, not non-unit calculations.

The triangular work used source rows 1,2,3,4,8 (then also 9,10,11) to solve
successively for v6,v12,v35,v43,v5,v11,v16,v20. A tracked Q(v69) five-pivot
lift verified every affine pivot, quotient, and representation exactly, then
reached its 80 GiB address-space ceiling after 1:15:43 with no unit. A separate
full-Q construction used v71 and `v69*v71-1`, avoiding any extra localization.
Its stages 1-7 passed exact row-membership lifts; an independent all-slot
stage-8 audit checked 232 direct quotient identities, reproduced 207
generators/5,063,191 terms, and matched construction ID
`59338ef7c8ca3d6f8d7c4c62b546976fc92ab5b8c52134a1a9b0a482d86359ec`.
The audit script/output/timing hashes are
`fcc68c217c024e87fceb30fb69cf3c5f80fa5df265688cfef2e99f8b0541226f`,
`a7faf25068feef1ee40b5cbdc317bd9f5882fe3997a08a178daa17ce9f6258e2`,
and `51434d6ca3b278639c40379f266b7086256a10e01ff7b6223e1b3e6c1df0282f`
(59.78 s, 2,324,040 KiB, exit 0). This proves the transformed rows are exact
consequences; it does not by itself prove a unit.

Finally, a p=32003 guide selected a 124-row pattern by mechanically taking the
pinned b9-q1 index array and changing only terminal indices 234,235 to 240,241.
That guide is not promoted. The selected rational rows were independently
byte-checked against the frozen q0 source and run under exact Q in both dp and
frozen wp orders with redSB/slimgb and complete delimiters.

Neither exact 124-row run completed before closeout: dp ran 55:31.79
(1,507,960 KiB peak) and wp ran 53:48.47 (857,244 KiB peak); both stopped
inside `slimgb`, with zero result delimiters and no unit marker. Exact Q
K195/K207 bases, the full-Q five-pivot lift, and the eight-pivot Q(v69) route
also ended at the lane wall without a result. The F_32003 tracked `liftstd`
used its 600-second watchdog (14,364,408 KiB peak) without a cofactor vector,
so CRT/reconstruction and the full-ring identity checker had no candidate to
consume. The chart is therefore **STILL-SIGNAL-ONLY**, solely by exact
resource wall; no non-unit conclusion is drawn.

## 6. msolve and modular evidence rejected as certificates

Exact-mode msolve 0.10.1 completed on all three full sources and printed the
same six bytes, `[-1]:` plus newline (SHA-256
`0333251e6ebb3890ef547f522ec55f27f0cef9a860998757e31f3e1b819e7490`).
The q0/q1/b10 walls and maximum RSS were 23:43.74/35,075,656 KiB,
2:41.45/6,352,104 KiB, and 0:25.23/1,699,772 KiB. Under the charged erratum,
that text is only a first-prime signal unless rational cofactors are recovered
and checked, so none of these outputs enters the verdict.

The charged `guided_gb.py` was inspected consistently with its warning: it
reconstructs scalar invariants, not cofactor vectors. Finite-field `liftstd`
experiments never produced a stable normalized cofactor support. A q0
p=32003 msolve guide first reached a deliberate 24 GiB address-space wall and
then, with 48 GiB allowed, reached its 900-second watchdog without output.
No deletion core, CRT vector, rational reconstruction, or holdout-prime claim
was manufactured from those runs. Had a candidate existed, promotion would
still have required fresh exact multiplication against all 241 original Q
generators.

## 7. Method coverage and resource semantics

For every charged chart the lane launched full exact-Q `dp` and frozen `wp`
jobs for both `std` and `slimgb`, each with a 10,800-second watchdog and fully
delimited output. It also launched exact triangular/prebasis routes and exact
msolve. Once b9 q1 or b10 q1 certified, its redundant competitors were closed
to protect the unresolved chart; their `rc=1` closeouts mean “terminated after
certificate,” not “non-unit.” For b9 q0 the long jobs were retained to a real
certificate or their stated time/address-space boundary. The custody JSON
separates certificates, deliberate closeouts, watchdogs, and memory ceilings.

## 8. Promotion logic and FALLACY-v2 audit

The charged cover is the pair q0 nonzero and q0=0/q1 nonzero; both are needed
for each beta-stratum closure (`k7-strata-gate-sol56-20260905.md:62-73`). The
frozen b10 q0 certificate plus the new b10 q1 certificate therefore makes b10
unconditional. Since b9 q0 did not certify, b9 remains conditional on that chart.

The coefficient field, monomial order, positional ring map, generator order,
core inclusion, localizer, and exact implication are all declared. No
`sat()` wrapping, raw-remainder shortcut, derivative-label inference,
flag/place/series identification, carrier/attainment claim, pole identity,
floor-to-equality step, merge/M-descent step, or target/arrival substitution is
used. In particular, modular evidence is never promoted to Q. This report
makes no new exit-price assertion, so the special exit-charge declaration is
not applicable.

For closeout, exact cmdline/cwd checks preceded stopping only this lane's
remaining jobs. At 08:12:55Z the worker showed no Singular or msolve process;
swap use was zero. AWS then re-confirmed the exact Owner tag, and
`fleet.sh term i-028a9c1579ea72e67` was issued at 08:13:06Z; AWS reported
`terminated` at 08:13:52Z.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14068`.
- Body SHA-256:
  `76dfe319b237f18069ef1083b52fac9462742c969448ca6bbf2dc6fd325f7f7a`.
- Frozen basis: `c662d44c2239b38d5c7e30d0365a680fba9e59c7`.
