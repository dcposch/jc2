# Moh big-memory harvest — round 3 — 2026-09-05

## Disposition

At the 16:50Z cutoff, none of the eight solver attempts had produced a
terminal status, modular UNIT, exact-Q UNIT, or NONUNIT basis, and none showed
a credible final-output phase warranting the optional extension.  All eight
active solver sessions were externally stopped.  Post-stop custody completed,
the eight charged workers were individually terminated, and AWS subsequently
reported all eight `terminated`.  The separate `2_9/V1_8` native extraction
had already timed out after 3,600 seconds with `rc=124`, leaving only a header
and no native system.

Accordingly, this lane proves **zero kills**: `0/4` requested fibres and `0/3`
distinct targeted classes.  All four target verdicts are `OPEN`.

The four requested source-complete targets were
`m12_m2_5/V1_1_6` (77 intrinsic parameters), `2_9/V3_8` (111),
`m15_14/V1_9` (129), and `2_9/V1_8` (136).  A stopped run is recorded as
stopped and is not a solver result.  A first-prime `[1]` is only a modular
signal.  No class is called killed without a controlled exact-Q computation on
the identical completed generators (or a checked rational identity).

## Frozen-input verification and scope

Before reading the mathematical inputs, I mechanically built a checksum
manifest from the numbered `charged_input_<i>_sha256` and
`charged_input_<i>_basename` lines of
`xmodel/moh-bigmem-harvest-sol56-20260905.run.v2`, prepending the receipt's
`lane_inputs_dir=/tmp/jc2-lane.AUKSYB/inputs`, and ran `sha256sum -c`.
All seven entries returned `OK`; there was no content mismatch:

| Frozen basename | SHA-256 |
|---|---|
| `report_draft.md` | `24d9dd7ff97d827a157f80e7dbee8e41eb98758d34a7b2e0bf9815538717aed3` |
| `launched-workers.json` | `c5b71fba6ebb91be1bbf8ef5162e578311d35c7f160e51ff63dac1c680fb5c99` |
| `harvest_one.sh` | `06b3b7e52960793da2c58991532f21239d9ab7c3f2e0c94c9e4a7187eef694cd` |
| `moh-hsupport-gate-astra-20260905.md` | `4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354` |
| `fleet.sh` | `ab5ce23a113fc80b05e8261c0199d3513a7956aed3db3d033e0efb39bfe5a46d` |
| `dispatch.sh` | `dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599` |
| `FALLACY-v2.md` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |

The charged gate report §§7–8 supplies the presentation and consumption rules
used here.  The graph presentations are exact triangular extensions, while
§8 says that exact-Q UNIT on any one final completed fibre is sufficient for
its class.  It does **not** turn modular UNIT, a partial basis, a
timeout, an allocation failure, or a stopped run into a characteristic-zero
certificate.  The two requested `2_9` fibres belong to one class, so that class
is counted once even though two fibres were attempted.

The m12 jobs were launched under the actual artifact name
`C_n24m16_Mm12_m2_5_ell1_s4_union`, not silently relabelled as `V1_1_6`.
This is the gate's 77-parameter singleton-class union; its 425-row file is
reported under its actual custody.  The distinct `V1_1_6` file was not
launched, and any class consumption would be only through gate §8.

The name distinction is custody-relevant.  The launched union rows have SHA
`af3cf058c7e949d7e9958b1c9120b9350436c6eca7a952afbc8ea32f9794ef58`;
the nonlaunched `V1_1_6` rows have SHA
`35bb95778825af58477001b645c564449fef2995b9ab3a61937efba3b041efab`.
A mechanical identity-map audit finds the same 425
`(h_power,x_power,y_power)` keys and zero polynomial term-multiset differences.
After removing comments and the output-row filename, the two builder bodies
compare equal.  Their raw row hashes remain distinct and are not substituted
for one another.

## Launch protocol and solver custody

The r7i workers ran official msolve 0.10.1 with SHA-256
`0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f`,
flags `-g 2 -t 32 -v 2 -l 44`, prime `1073741827`, DRL/grevlex order,
unlimited pair selection, and a 10,800-second per-invocation watchdog.  The
RLIMIT_AS/virtual-memory ceiling was 700,000,000 KiB, unlike the 8–48 GiB caps in
the prior gate retries.  The x2idn workers ran Singular 4.3.2 at
`/usr/bin/Singular`, SHA-256
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`,
with 32 requested CPUs/threads.  Both binary hashes matched on all eight
workers at 15:03Z.

Every ideal is the full row ideal plus the nonvanishing equation for `c`:
msolve uses safe variables in the manifest order and appends `z*c-1`; Singular
uses the metadata variables followed by `T` in a `dp` ring and appends
`T*c-1`.  The slack-variable rename does not change the generators in the
parameter ring.  Native rows are the `x,y` coefficient polynomials extracted
in the builder's `y`-first `(lp(1),dp)` ring; the final parameter-ring solve
excludes `x,y`.

The frozen launch record says `launched_utc=13:50:00Z`, whereas the lane prompt
says 13:49Z; that one-minute discrepancy is retained rather than reconciled.
Observed work actually began at 14:05–14:12Z.  The fixed
16:50Z hard stop therefore supplies about 158–165 minutes of actual job wall,
not 180 minutes for every process.

The four r7i hosts initially had a helper whose missing default argument would
have blocked automatic exact-Q after modular UNIT.  At 14:58Z only that helper
was replaced, from SHA
`ae0ded5fe0bdd9c0c5b27572a2e8b51b4a895a44684e3edae87513b390483454`
to the two-line-corrected SHA
`829f59f21c2f1ae8771191263537ec58769230b8c94809c323cfce35089fd071`
already active on the guided hosts.  Hashes were verified; no active solver or
solver input changed.  See `harvest/exactq-helper-patch.txt`.

## Input custody

Counts below are `source rows / pre-localization variables -> solver generators
/ solver variables`; the arrow adds exactly the Rabinowitsch generator and its
slack variable.  Native pre-localization counts are intrinsic parameters;
graph counts include triangular auxiliaries shown parenthetically.

| Target and presentation | Counts | Rows SHA-256 | Metadata SHA-256 | Emitted/input identity |
|---|---:|---|---|---|
| m12 singleton-class union, native | `425 / 77 -> 426 / 78` | `af3cf058c7e949d7e9958b1c9120b9350436c6eca7a952afbc8ea32f9794ef58` | `2d5ce8b87443b24b02e249bebde9c7ada098968aeba7e5fcc672c1ea0d31187f` | msolve `.ms` `2c3ec84260713e3f721a10b7dc37247364a011f5d5c82ca75b52185feb8cc453` |
| `2_9/V3_8`, native | `174 / 111 -> 175 / 112` | `2b59ba92f2b889b09d38570f6f03bec865ede4d509e85c687f66f3033369254b` | `3040c7ce7e20b5d7d87b4458d0e4a08955f082c9de47efa9fe467a6c5dc5e3e6` | msolve `.ms` `4d3d8eac54467ba5be167c1d75b6c338772d5588e21bc38915dac2dc11c71128` |
| `2_9/V3_8`, graph | `335 / 279 (111+168) -> 336 / 280` | `762c5f71378d9a48a4a9de83927c452014693640de44405574444242bca872bf` | `07f22f0706be1004905f24a8a77fa6a70add72aaeb853f0654e4150ba326fbd5` | generated only if a graph stage starts |
| `m15_14/V1_9`, native | `177 / 129 -> 178 / 130` | `ad9c53e3276345ec49f36062dc33e2c81c152d93ac53ce1e580d7fcd9912153c` | `cdeaf2800538eaae3ddf55d5fff23212dd8e65360ada347c383acddd5194c49d` | msolve `.ms` `c5d52ad31b03bcb756d12d570c2dc0a8b86d5447f252509c37b904992ec1631a` |
| `m15_14/V1_9`, graph | `402 / 354 (129+225) -> 403 / 355` | `b79a4e89ef2f6fc808e27eafe241c32f2e178f525a70215c99c5f4dccaf20e96` | `32b3b199bec37e2784f01b3e4d1cc3f92ab44f1c42151bc222fec62801afd500` | generated only if the sequential graph stage starts |
| `2_9/V1_8`, native | `0 data rows / 136`; no solver system | header-only `7f2d716d35087e97752089d9d8041944bd5a49fe5c1c4b1118591e1f3d587130` | `9a728aa58bf294c4e96acd2bfe69d7dafe8c83f2e94f908c638338de3a1746b8` | builder SHA `121aac3dfe246e16aa6d64d9119a728fb39ed1ce9e6e13c5923765e24419579a`; extraction `rc=124` |
| `2_9/V1_8`, graph | `650 / 438 (136+302) -> 651 / 439` | `35ad3ecbf9f9ed5a341df81e8b7c76d763bcd3b2ad273cec775c6ef101488fee` | `8f04a52af0a0c8e5604c46e84140cf7492be38b4782ac597a9c08c595a93d644` | emitted `.ms`/guided `.sing` SHAs reported below |

## Per-presentation outcomes

Here `p=1073741827`.  `M(n)` means the manifest-ordered
`F_p[safe variables,z]` DRL system with `z*c-1`; `S(n)` means the metadata-
ordered `F_p[variables,T]` `dp` system with `T*c-1`.  `STOPPED/no rc` is an
external disposition, not a solver return.  Peak-RSS lower bounds take the
larger of sampled `VmHWM` and final observed RSS.  Solver elapsed values are
the last `ps` samples at 16:50:03–04Z, about two seconds before TERM, and thus
are lower bounds on final process wall; the extraction timeout is exact.

| Target / presentation | Worker (instance / IP) | System and actual input SHA-256 | State; elapsed evidence; peak-RSS floor | Primary output bytes / SHA-256; verdict |
|---|---|---|---|---|
| m12 singleton union, native msolve | r7i `i-0e95f8ff97f6462ce` / `.183` | `M(78)`, `426` gens; `2c3ec84260713e3f721a10b7dc37247364a011f5d5c82ca75b52185feb8cc453` | `STOPPED/no rc`; last `ps` `02:44:47`; `>=203.87 GiB` | `.g2.out` 0 / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; `OPEN` |
| m12 singleton union, guided native | x2idn `i-0780c67ecdc79cb0a` / `.121` | `S(78)`, `426` gens; script `98ce063898395b955ae2290f3d8eaf8fd499b433ea80519eb3213ccc1f6aaafa` | `STOPPED/no rc`; last `ps` `02:37:56`; `>=17.56 GiB` | `.out` 225 / `01de43c979ba296aeb5dbee75a45dc2a91f7cfe5a0f3de2acc9b64d1062b7d3e`; `OPEN` |
| `2_9/V3_8`, native msolve | r7i `i-0ce9ea50559403c22` / `.202` | `M(112)`, `175` gens; `4d3d8eac54467ba5be167c1d75b6c338772d5588e21bc38915dac2dc11c71128` | `STOPPED/no rc`; last `ps` `02:38:48`; `>=113.20 GiB` | `.g2.out` 0 / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; `OPEN` |
| `2_9/V3_8`, guided native | x2idn `i-018484399fd100293` / `.55` | `S(112)`, `175` gens; script `42a1b9bde121ea516c020519e3c84addd7d017b3c94399bf2a070a2c76f4685b` | `STOPPED/no rc`; last `ps` `02:37:56`; `>=38.37 GiB` | `.out` 226 / `eb5301cdfa38729667285bf0b7c6fd095512b5c2ab00520b81c9530f34d677a6`; `OPEN` |
| `m15_14/V1_9`, native msolve | r7i `i-0193dc1295fc5234a` / `.108` | `M(130)`, `178` gens; `c5d52ad31b03bcb756d12d570c2dc0a8b86d5447f252509c37b904992ec1631a` | `STOPPED/no rc`; last `ps` `02:38:48`; `>=155.33 GiB` | `.g2.out` 0 / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; `OPEN` |
| `m15_14/V1_9`, guided native | x2idn `i-043f250f1956bd34b` / `.45` | `S(130)`, `178` gens; script `5187721267a7617c7f782aadbea8228bad4c3dc0f3b39819297b6b541295b643` | `STOPPED/no rc`; last `ps` `02:37:56`; `>=10.82 GiB` | `.out` 226 / `64ac0bc6550cb408de3e2e043c9c1078f3bca64bc55d3c71d1e5177e70b92a30`; `OPEN` |
| `2_9/V1_8`, native extraction | r7i `i-0baedea1d34e4b978` / `.190` | Singular over `Q[y,x,136 params]`, `(lp(1),dp(137))`; builder `121aac3dfe246e16aa6d64d9119a728fb39ed1ce9e6e13c5923765e24419579a` | `rc=124 TIMEOUT`; exact `3600 s`; RSS `>=1.91 GiB` | 42-byte header-only rows / `7f2d716d35087e97752089d9d8041944bd5a49fe5c1c4b1118591e1f3d587130`; no basis |
| `2_9/V1_8`, graph msolve | r7i `i-0baedea1d34e4b978` / `.190` | `M(439)`, `651` gens; `545b1521ae7374623c4960de7c08c16c247d6546c39d69792ac9416a82ab2f9e` | `STOPPED/no rc`; last `ps` `01:38:49`; `>=141.39 GiB` | `.g2.out` 0 / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; `OPEN` |
| `2_9/V1_8`, guided graph | x2idn `i-02efd7ecd26becc5a` / `.125` | `S(439)`, `651` gens; script `dbc20390296da5f7d0ac5c84dedbd149883003acdaae03e8eb65eb9f1be5f147` | `STOPPED/no rc`; last `ps` `02:37:55`; `>=4.44 GiB` | `.out` 204 / `983d43dbfc7a69c0077aeca2a0fc525987328ab9f24830fc5e5e728946207865`; `OPEN` |

The `V3_8` and `m15` graph fallbacks never started because their native
msolve stages had not ended; m12 graph was not configured.  No exact-Q stage
started because no modular UNIT signal existed.

The guided files' signal-time trailing `halt 1` is not a natural solver rc or
`GG__STD_END`; all result JSON files remain absent.

The harvested manifests, logs, outputs, RSS samples, and existing rc/status
files are bound by the final custody manifest.  Empty or interrupted output
has no mathematical verdict.

### Certificate and basis harvest

No `.status.json` or `guided_gb_result.json` carrying a final verdict existed
before the stop.  No modular `[1]` was available to trigger the controlled
exact-Q rerun, and no rational identity was produced.  Thus there is no
characteristic-zero UNIT certificate.

**No NONUNIT basis completed.  Consequently there is no dimension, degree, or
sample point to report.**  Supplying one would turn an interrupted computation
into a fabricated result.  There was also no solver OOM/allocation-failure
marker; only the explicitly recorded preprocessing timeout above.

| Requested target | Typed verdict | Class consumption |
|---|---|---|
| m12 singleton-class union representing `m12_m2_5/V1_1_6` | `OPEN` | none |
| `2_9/V3_8` | `OPEN` | none |
| `m15_14/V1_9` | `OPEN` | none |
| `2_9/V1_8` | `OPEN` | none |

The two `2_9` fibres still count as one class; neither supplies a consumable
certificate.

## Honest compute picture

The current-RSS curves below use five common snapshots
`14:52 -> 15:32 -> 16:02 -> 16:32 -> 16:50Z`; values are GiB.  The complete
charged 14:32/14:45 captures and ten-minute series through 16:42, followed by
the cutoff capture, remain under `harvest/`.

| Run | Current-RSS curve | Completed F4 rows; maximum fully timed degree | Active cutoff front |
|---|---|---|---|
| `.183` m12 native msolve | `81.2 -> 93.1 -> 116.9 -> 183.2 -> 203.9` | `102`; degree `8` | degree 7, `302878 / 452145`; last write 16:47:52Z |
| `.202` V3_8 native msolve | `51.0 -> 63.9 -> 88.0 -> 107.9 -> 113.2` | `48`; degree `6` | degree 6, `42594 / 293033`, `3200998 x 7439076`; last write 16:09:01Z |
| `.108` m15 native msolve | `84.6 -> 131.1 -> 141.4 -> 150.7 -> 155.3` | `42`; degree `6` | degree 6, `266428 / 293340`, `3984465 x 5377773`; last write 15:23:09Z |
| `.190` V1_8 graph msolve | `1.7` extractor, then `140.2 -> 140.5 -> 140.9 -> 141.4` | `5`; degree `3` | degree 3, `84173 / 2264055`; last write 15:30:41Z |
| `.121` m12 guided native | `9.4 -> 12.4 -> 14.7 -> 16.3 -> 17.6` | n/a | `GG__STD_BEGIN`; no end marker |
| `.55` V3_8 guided native | `14.3 -> 21.6 -> 28.9 -> 35.9 -> 38.4` | n/a | `GG__STD_BEGIN`; no end marker |
| `.45` m15 guided native | `4.1 -> 6.6 -> 8.3 -> 9.9 -> 10.8` | n/a | `GG__STD_BEGIN`; no end marker |
| `.125` V1_8 guided graph | `2.6 -> 3.5 -> 3.9 -> 4.2 -> 4.4` | n/a | `GG__STD_BEGIN`; no end marker |

M12 native got furthest by observable telemetry: the only fully timed degree-8
row and 102 completed F4 rows.  This proves neither proximity nor a fair
native/graph comparison: the paired fallback stages never ran.  The guided
processes used about one CPU despite 32 requested threads.  Ample RAM remained;
RSS and incomplete fronts are telemetry, not allocation or basis verdicts.

## Hard stop, termination, and audit boundary

The guarded stop began at 16:50:00Z.  All eight charged ID/IP pairs matched
current running AWS records before the snapshot and again immediately before
mutation.  Cutoff polls were captured at 16:50:03–04Z.  TERM was sent to the
full captured job sessions at 16:50:05Z; after the KILL safety pass, every
worker reported `STOP_VERIFY_LEFT=0` at 16:50:12Z.  The eight strict post-stop
pulls each reported `hash_rc=0 pull_rc=0 compare_rc=0` and
`HASH_COMPARE_OK`.  Inputs excluded from the compact pull are retained as
remote hashes, not misdescribed as local mirrors.

The eight instance IDs were then passed separately to `fleet.sh term`; all
eight calls returned zero.  AWS recorded each as `shutting-down`, and the
16:50:25Z `fleet.sh ips` output contained none of them.  A persisted exact-ID
AWS describe at 17:01:01Z returned zero and reported all eight states as
`terminated`.  The hard stop ended at 16:50:25Z with `errors=0`,
`term_failures=0`, and `verify_failures=0`.

The 13-entry `final-custody-manifest.sha256` verifies from its evidence
directory and has SHA-256
`bbe1f13bca9ab0d4bbded888b66b6cae1a741c91ed3bbf5244a30b0fcb724572`.
It binds the eight remote custody inventories plus the hard-stop log
(`8adffc5d0c6f42e501165e70f4e1db30bc4da67806af90dec85f209669f441ab`),
the immediate shutting-down AWS state, the final all-terminated AWS state and
query metadata, and the final fleet listing
(`070d5315d97336f288c874a1962dc83f2420443c56f99e0285bb9ffdbb5d2e45`).

The older `dispatch.sh kill` did not cover these process trees, so full lane
sessions were stopped before exact-ID termination.  No `term-all` was used;
out-of-scope workers `.7`, `.28`, `.18`, and `.67` were never addressed.

This report makes no new exit-price assertion and promotes no prime label,
stopped run, or floor into a certificate or attainment claim.  `OPEN` remains
the typed answer.  No ledger, `jc2-lean`, or `ideation-*` file was edited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16826`.
- Body SHA-256:
  `f74a929912deb57cb0b3f7942becd105006ae9514ba9039a50b24b0fcc02263a`.
- Frozen basis: `6df670cbd429bbd683a42017457971541bc5734d`.
