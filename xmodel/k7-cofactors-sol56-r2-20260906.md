# K=7 beta-strata exact-Q certificate audit, resumed round 2

Lane `k7-cofactors-sol56-r2-20260906`; frozen input root
`/tmp/jc2-lane.Z7bcss/inputs`; compact machine record
`box/k7-cofactors-20260906/r2-custody.json`. This is a certificate lane only:
no ledger, `jc2-lean`, or `ideation-*` input was read or edited.

## Verdict

**PARTIAL CERTIFICATE; do not retain the five-stratum promotion unconditionally.** At seal time, **7/10** cover charts have a
theorem-tier certificate over Q. The charts still carrying only the historical
msolve signal are **b9 q0, b9 q1, and b10 q1**. Therefore **the b11, b12, and
b13 closures stand unconditionally, while b9 and b10 remain open at one or
both covers.**

This deliberately supersedes the frozen gate's evidence typing, not its chart
construction. A characteristic-zero header on an msolve `[1]` is not enough:
the charged erratum says that output can be the first-prime unit printed before
rational reconstruction (`k8-b11-q1-sol56-20260905.md:15-20`). This audit
accepts only (a) an explicit rational cofactor identity checked by fresh exact
multiplication in the full original ring, or (b) the task-authorized fallback,
a completed Singular computation over Q whose fully delimited reduced basis is
literally `{1}`. A timeout, a protocol fragment, or a modular result is never a
certificate.

## 1. Frozen-input and resume custody

Before CAS work, `awk` mechanically paired every numbered
`charged_input_<i>_basename` and `_sha256` field in
`xmodel/k7-cofactors-sol56-r2-20260906.run.v2`; `sha256sum -c` then returned
five `OK` lines and no mismatch. The exact matched digests were:

```text
78edece02efa7223d9130aa334416339f69c10de6d3cf4c6b7873581b791e1f8  k7-strata-gate-sol56-20260905.md
c16199138f4e93d3babdde1372e0000fb02ef831e1dd2b9e143d486bb0a6b6ac  k8-b11-q1-sol56-20260905.md
2af3e012dd4157669308f3855a22582967e2fffdc25cad3bf825b1050f25be4c  k4ray-strata-solve-opus5-20260905.md
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

The awk manifest was 591 bytes, SHA-256
`e21ae2d43532611bbef39c4b6638e074992c29168bd2f544397e80510a7579c0`,
and the five-line checker stdout had SHA-256
`82c737f8b6432f9d96b952809288a77a3302d4ade27392cc193f358da390dd2c`.
Receipt SHA-256 was
`f39ede5ca66adcfcab4fed5a46d6fc4f57c5886de39682831a1884f965321395`.
There was no content mismatch.

The resumed lane adopted, rather than duplicated, the still-running worker
with owner tag `k7-cofactors-sol56-20260906`: instance
`i-08c88c3e0b82fad5e`, private IP `172.30.0.108`, type `r7i.8xlarge`, launch
`2026-09-06T00:36:53Z`. Every new CAS input, script, log, trial, and `TMPDIR`
lived below `/home/ubuntu/k7-cofactors-20260906` on that worker. No round-2 CAS
scratch or log was copied to the host. The inherited small round-1 files under
`box/k7-cofactors-20260906/` all predate this receipt. Host `/` was checked
before work (1.9 GiB then available) and again at 03:44Z (12 GiB available).

## 2. Charts, generator bytes, and ring map

The charged cover is `q0 != 0` together with `q0=0,q1 != 0`; both charts are
needed (`k7-strata-gate-sol56-20260905.md:62-73`). The seven charts lacking a
cofactor at entry were b9 q0/q1, b10 q0/q1, b11 q0/q1, and b12 q0. The other
three were b12 q1 and b13 q0/q1. The prompt's “44–51 variables” is stale for
these charts: the frozen authoritative counts are 71–100 variables, as the
charged table itself records at lines 100–111.

| chart | vars/gens | integral generator SHA-256 | certificate at seal |
|:--|--:|:--|:--|
| b9 q0 | 72/241 | `15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275` | signal only |
| b9 q1 | 71/235 | `09002c7229da517ca0d809f925873aeb94d44650467bd6addf71268aacbb7934` | signal only |
| b10 q0 | 79/261 | `273a1a0f65308af6019c3b8986fa921c76d4e27da30d0b675afc532bc3f3d434` | exact-Q basis `{1}` |
| b10 q1 | 78/255 | `a49433e9834c4fa7a76a89aef50e7f3852ee0e26ff1d665bc1c8516dc390f97d` | signal only |
| b11 q0 | 86/281 | `e8e57139c2292f0535226e7fb8fc2fac90b459685e939b825abec31531b2367e` | rational cofactor identity |
| b11 q1 | 85/275 | `42f96a5f916e94457887e933cb8cb3f8656537e1547e719e30851075990fd4f1` | exact-Q basis `{1}` |
| b12 q0 | 93/301 | `3a3821db1511fa96096f627d5d5ed23b1b60a2c95022f33dfb90791a4c60561d` | rational cofactor identity |
| b12 q1 | 92/295 | `875573726b784dc4700de3835f0130617279eb5bab451f712f77088c26cae4e2` | rational cofactor identity |
| b13 q0 | 100/325 | `970026efbf5ffd1150def477d64de057b8212455527a15f6abbf18807d5cce2c` | rational cofactor identity |
| b13 q1 | 99/317 | `570e241e4e2515d1c97c77f9b7696e5d519fb97697543da93410ca5eb2797a8b` | rational cofactor identity |

The source is the denominator-cleared integral list in unchanged one-based
order. Its positional `names[i] -> v_i` map uses longest-name-first
substitution; image checks are at `k4ray-strata-solve-opus5-20260905.md:162-169`
and `k7-strata-gate-sol56-20260905.md:90-98`. Singular 4.3.2 binary SHA-256 is
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.

Identities were finally multiplied over Q in the full authoritative `wp` ring.
Basis fallbacks used declared `dp`; `I=(1)` is order-independent. Cores used
only support variables, and adjoining unused source variables preserves a unit.
Indices always refer to the full frozen list.

## 3. New rational cofactor identities and direct checks

### b12 q0

Round 1 had completed this missing chart before the host filled. Singular
`liftstd` over Q used original indices `14,15,16,17,21,29,301` and the recorded
weighted block order. The 2,244,218-byte identity has SHA-256
`543fccec23528d6c701c50d7fe6aa960ec529da80ee314822b376709a4f44344`;
lift script/log SHAs are
`626d6d4f4ee50e07f94751ac9019c2d179fe21e155c7566bdf1fc566843ce3c7`
and `67259462df8dd66fda8d96ed7f243a8610769718b7b2fb2bfe79c6b1faaaec57`.
Lift wall/RSS were 23.52 s/549,528 KiB. A separately generated verifier loaded
all 301 original generators in the authoritative ring and performed only exact
rational multiplication. Script SHA
`4ac1d69f7d7fac1f0a1fa016241f42bbc3e178097ce5ed32fa8c8e20a48f5909`,
log SHA
`ff29069307d90ee119b221d8985210b70182299d832272e6d6375d449bc7dcbf`,
wall/RSS 13.43 s/1,219,016 KiB; markers are `DIRECT_PRODUCT 1` and
`EXACT_ONE 1`.

### b11 q0

An exact-Q(v83) triangular reduction made the lift tractable. All eight pivots
printed `PIVOT_ZERO 1`, `QUOTIENTS_EXACT 1`, and `REPRESENTATION 1`; exact
back-substitution produced an identity on original indices
`13,14,20,21,22,23,28,30,31,49,281`. Its only coefficient denominators were
powers of the chart coordinate v83. Clearing them and using the original
Rabinowitsch generator yielded a polynomial identity in the source ring, not a
localization-only claim.

The 6,880,557-byte identity SHA-256 is
`514b2a21ab779520cb40efe0a4ba7906bd633dc36b655f79d56b4f027063be66`.
Tracked lift script/log SHAs are
`24d04eafddd8590304fda169870e7deab719ce4faa64404275c13a455d8364bb`
and `711a5e5bb44d0f8b158948cbd17dc485bbc65cf939a746e6350962e30ec2ab65`
(1.67 s/149,660 KiB). Clearing construction script/log SHAs are
`fb9252f474b2ece9a2ddf502e29e888b66f1e718e849c2314f6f03158e199fd3`
and `37899b223c876bceba6fdca19ffc909cb06203ef9aa45f35aab38496d847e182`
(1.90 s/171,656 KiB; `DIVISIBLE 1`). The independent verifier loaded all 281
source generators under authoritative `wp` and directly formed the sum.
Script/log SHAs are
`a2ad23dfe39c3c6506dea03ba20d7ab86d07bfe640c8fe1bc73bcde80d82b561`
and `ab4e30e3634cbdd0b9b705b384f2e09416d11459c7192447fd2d1dd8a12a6b24`;
7.58 s/454,232 KiB, exit 0, `DIRECT_PRODUCT_ONE 1`, `CHECK_VALUE 1`.

## 4. Exact-Q basis fallback certificates

For these charts there is no claimed cofactor file, so the direct-product
requirement is inapplicable. They use the task's explicit alternative: a full
exact-Q Singular basis computation. `option(redSB)` was set, the complete basis
was printed between unique `CERT__GB_BEGIN`/`CERT__GB_END` delimiters, and an
independent strict parser accepted only a sole body `1` with exit 0 and the Q
metadata.

* **b10 q0:** core indices
  `27,28,29,30,35,36,37,38,39,40,41,47,48,49,50,59,68,69,80,260,261`.
  Exact-Q `dp` `slimgb`, 61.04 s, 151,996 KiB. Script SHA
  `b729ddd61067c3c46e6392e48741858ccde7e0f5a4362c8aa854672060f13e4b`;
  complete log SHA
  `e4bf35f32dd9a55f06e1d4cfb0257cc8e3a24c797fb329c6320fac70f53762c3`;
  timing-only stderr SHA
  `a5adc7cab868765f1c5017407d1dc4e835f3374c4061d4ff32118febdc77432a`.

* **b11 q1:** core indices
  `13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,35,46,47,56,274,275`.
  Exact-Q `dp` `slimgb`, 78.83 s, 256,612 KiB. Script SHA
  `028a2c3a5eefc89757ecf1b045a9b65fe80de1e995bb90f397484aa55c6482be`;
  complete log SHA
  `d3bac1db42272023316be29f506eeaab7fbebec453e34de368dbedf9cdb7b314`;
  timing-only stderr SHA
  `712ea0cc14748e2a46d4095669c55028deccbbd70c836a2f2d83b0b324a3c811`.

No other basis fallback completed.

## 5. The three charged identities rechecked

The pre-existing b12 q1 and b13 q0/q1 certificates are the three exact
identities described at `k7-strata-gate-sol56-20260905.md:219-253`. This lane
reran their independent exact multiplication scripts from frozen bytes:

| chart | nonzero original indices | verifier script SHA-256 | fresh output SHA-256 | result; wall/RSS |
|:--|:--|:--|:--|:--|
| b12 q1 | 12,13,15,17,18,295 | `35af3e1d11303b3c0e5fd2ba69b94a7073fe06296c38e28d050b9e27a95355eb` | `f8c7d678b5f463a15021a40ddc05c97b511f8230a4903b3ad537e28f60b1f2bf` | polynomial direct check 1; 0.68 s/31,888 KiB |
| b13 q0 | 2,8,325 | `af1fc3e6d34d19d2b4a21e10693da165b6a1f63d440c1c5e87c34ed419b78de6` | `223821eaf05865df3215d097a8173e7bf3f6cc7465e6459d2f19bc136ba6f9b3` | direct check 1; 0.00 s/10,288 KiB |
| b13 q1 | 1,317 | `43423e5723b4bcdcf2a81d68dcd3a0630e2af62e45d27a3dd443426f131cce2b` | `a456c399b7485768fc1f381d265216746b6315f59757f504d0cb6fb74407fefe` | direct check 1; 0.00 s/10,056 KiB |

For b12 q1 the localized relation was cleared to a polynomial identity with
the localizer before this check. The sparse b13 identities are already in the
original polynomial rings. Thus all identity rows in the verdict table have a
direct full-ring rational multiplication check independent of their lift.

## 6. Rejected evidence and resource outcomes

Tiny lifts with `UNIT 0`/`CHECK 0`, modular bases/syzygies/support, and all
msolve `[1]` outputs were rejected as certificates. A B11 q1 back-substitution
with `REPRESENTATION 0` was quarantined. Weighted B11 q1 `std` reached 2,400 s
with `rc=124`, no delimiters/unit; it and every incomplete run are engine
limits, never non-unit results.

Both b9 charts remain signal-only. Exact-Q `dp`/`redSB`/`slimgb` attempts on
the full 241-row q0 set (both input orders) and a 124-row q1 guide core (both
orders) were stopped at the lane closeout with `rc=1`/`halt 1`, no basis
delimiter and no unit marker. Their longest walls/RSS were 16:28.97/1,044,096
KiB (q0) and 16:29.00/1,550,280 KiB (q1). Representative script/log SHAs are
`4238a22343343a5a3ea852da5136f82a6f8f72743866fe8dce5ef97ff66329f8` /
`ef8c46e8e94fa576c5dce9022ccb8e0fae516dfa0ae19e1735d67d850fe993bf`
and `47bcf3afe5310baa4e4b2454b54bc9072a55f9d03d4f44f64b30dbb39ff48d54` /
`9f3889afd3a8b8dd2c09e431f7b1081987fd1323d85264131c6cd0accbed1fdf`.
The earlier msolve `[1]` results, including q1's 124-row core, remain guides
under the erratum and are not counted.

B10 q1 also remains signal-only. Its 48-row exact-Q `dp`/`redSB`/`slimgb`
attempt was stopped at 04:15Z after 22:11.51/1,459,612 KiB, `rc=1`, with no
basis delimiter or unit. Script/log SHAs are
`ba98a308216032f7990075cf5997551535087680c0fe36a7bad0394c4c22e5f5` and
`5fd6eccddf78ed00134e2ae2574115e55226a28beaf2cfc91cb0c5eef14fa6fe`.

## 7. Promotion logic and FALLACY-v2 audit

The charged gate's five closure claims require both cover charts
(`k7-strata-gate-sol56-20260905.md:70-73,298`). Consequently the theorem-tier
unresolved index census is `{6,7,8,9,10}`, rather than the gate's `{6,7,8}`.
No result here asserts a point, representative, carrier,
attainment, exit set, pole identity, descent route, or equality from a floor.
The flag/place/series, first-separation charge, carrier/attainment,
pole/interior, floor/attainment, raw remainder, derivative-label,
merge/M-descent, and target/arrival guardrails are not invoked. `sat()` is not
used. The geometric-to-`v_i` map, coefficient field, generator order, omitted
support variables, and order fallback are all explicit. A modular signal is
never promoted.

No new exit-price assertion is made, so no `charge_basis` line is emitted.

## 8. Fleet closeout and compact evidence

`fleet.sh term i-08c88c3e0b82fad5e` returned `shutting-down` at 04:17Z; an
AWS state wait confirmed the exact owner-tagged instance `terminated` at
04:18:18Z, before sealing. Because the host-write rule permits only this report and a
JSON no larger than 2 MiB, large identities and full new CAS logs remained on
the worker; their exact byte counts and SHA-256 hashes are in this report and
the compact JSON. The inherited b12 q0 identity/check and the three charged
checks remain under `box/k7-cofactors-20260906/` and
`box/k7-strata-gate-20260905/`. The JSON records commands, UTC intervals,
orders, original generator indices, hashes, wall/RSS, classifiers, rejected
trials, disk observations, and termination custody.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13422`.
- Body SHA-256:
  `fbe04004e6b1a69b1e0b53b62dad59dd281d174e236f3ea5403da97700b30ac0`.
- Frozen basis: `2193fcad3f78e1dc2af93c80c7c140b9160f7822`.
