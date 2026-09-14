# Input custody — FIRST review caprun-latebinder-first-fable5-20260911

Reviewer Fable 5.1. First action 2026-09-11 15:19:13 UTC (pin of the thirteen inputs). Harness runs 15:25:56 UTC (exit 1 from my own C05 assertion, which wrongly included SUMMARY.json; fixed) and 15:26:10 UTC (exit 0). Report written 15:27:53 UTC; BODY-END appended and this file written at 2026-09-11 15:29:13 UTC. Original reserve 15:37:00 / HARD 15:40:00 UTC, never reset. No Seal, no charge_basis, no transaction files authored; the external adapter owns receipt.

## Thirteen inputs in /tmp/jc2-lane.a27KVq/inputs (prepin at 15:19 UTC == postpin below, sha256sum -c OK 13/13 at 15:28 UTC, generated rows)

f276baaa99a89a46c32e279d0bb98a449ef3cc63c567f7afde818d9c9f9cbdf9  TASK.md
ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe  latebind.py
85d5390babe473deed13e9a88c40ea82193c6306284a4224cdb021f65ca5ec06  test_latebind.py
33e7308f21b60beb884977829fba0afeefd5ce6cac5183435677779a18de2d12  CONTRACT.md
68e416319cfb0e52900fd0ff0444644aa0d17a8e1d5488106876197f49b4e309  caprun-latebinder-code-astra-20260911.md
31c942b17ed290f13b0bcd87457ec3a2b68f760fc4cf99443fee0e8386eceb74  ROOT-REGISTRATION.preholder.json
4d0d8475ed7d4aac1e42b70b1c7b4ee0198270ead0c3bb46adb78d7a91153ba3  ROOT-REGISTRATION.json
58d35c476c3dc7c4f6fe36adf73b79e5e0d8843e6ddd388c27a745b747a40d2e  AUTHORITIES.preholder.json
1d9f837a23bb94b9609c7ac572909afbb0a4a96e44cb3c84b4875a9b310d02be  ROOT-EXECUTION-CARD.preholder.md
a92cf2680c8d6aff6044f5376fb1dcfeed87a29c527d55c953d940e39a99f281  ROOT-EXECUTION-CARD.md
6d414284920782a75a951fa3e59a8c23a391470a5efea28003b968bb1052fc62  final-install.preholder.sh
abff072f218cbecaa6f47278891a62b36463a70e34ae4be546e44a5f3c3cd208  final-install.sh
d90196456531bdf917098c84a84a88861384c220dcff6882a5305bacd48e8943  FINAL-INSTALL-INPUTS.sha256

## Owned outputs (generated rows; this file excluded as self)

3201abe5cae352f9e12ec6c842c6efe7ac463394b515cf2279d8266717296661  xmodel/caprun-latebinder-first-fable5-20260911.md
7b951a7dd5d8cfef0e20119f933f7dffa77fc0e1d8a4df16c6bcdd011e66b634  box/caprun-latebinder-first-fable5-20260911/review_controls.py

## Replay command and result

python3 -I -S -B box/caprun-latebinder-first-fable5-20260911/review_controls.py /tmp/jc2-lane.a27KVq/inputs

13/13 producer methods ok (unittest-reported 0.059 s); structural checks C01-C07 pass; 52/52 mutation controls as expected, of which six EXTERNAL rows (M13, M39, M43, M44, M45, M46) are accepted by the helper and documented as caller duties; PREPIN and POSTPIN 13/13; exit 0. Ordinary python3 3.12.3 with -I -S -B, no optimized mode.

## Read and test scope

All thirteen inputs read WHOLE through EOF with full-file reads. The producer harness's inferred default SOURCE path was overridden in memory before collection and never read. Every candidate stayed in memory; no registration, card, manifest, installer or authority document was written or executed; no input shell or Python document ran; stdlib only; no network, AWS, SSH, process control or /proc, /sys, /run, /opt inspection; no input mutation.

## Collision listing (xmodel entries matching the report name at 2026-09-11 15:29:13 UTC; only the .md is mine, nothing else edited)

-rw-rw-r--  1 ubuntu ubuntu      122 Sep 11 15:19 caprun-latebinder-first-fable5-20260911.log
-rw-rw-r--  1 ubuntu ubuntu     9937 Sep 11 15:27 caprun-latebinder-first-fable5-20260911.md
-rw-rw-r--  1 ubuntu ubuntu     4188 Sep 11 15:19 caprun-latebinder-first-fable5-20260911.run.v2
