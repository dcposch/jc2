# Input custody — FIRST review, supplied-input candidate caller (Fable 5.1)

Lane inputs directory: `/tmp/jc2-lane.kgQvAj/inputs` (read-only; the lane tmp root is a read-only filesystem, so harness output was captured by pipe, never written).

- First action 2026-09-11 18:30:19 UTC (clock, owned-target absence, apply_patch presence).
- PREPIN: `sha256sum -c` 23/23 OK at 18:30 UTC, directory count 23, before any read.
- All 23 inputs read WHOLE through EOF (three large JSON files in two overlapping unclipped halves each).
- Harness PREPIN 23/23 and POSTPIN 23/23 inside `review_controls.py`; independent `sha256sum -c` POSTPIN 23/23 OK at 18:40 UTC, directory count still 23 (no bytecode or artifact created).
- No linked, original, sibling, corpus, peer, runtime or protected path opened; no subprocess launched by the harness; nothing applied, installed, observed or released.

## Charged input pins (unchanged pre and post)

```
34bfd0953a0f08cd2e2ea16284da01fe23d26e424ce7d44afde3d39304a6e937  TASK.md
ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe  latebind.py
3201abe5cae352f9e12ec6c842c6efe7ac463394b515cf2279d8266717296661  caprun-latebinder-first-fable5-20260911.md
f7c61db67a9982a99f1febaed6dae0b6e3595199ffccad70647b66556b907066  stage_patch.py
e37735ceeee1d60ee97ce492e196c312a8b9ee5d887f8abc9809af71924ce5b5  EXERCISE.json
d96d979c950bf51faea0ad430af4f2eed1366d8f7b3e952e27d048ca2dff2273  caprun-candidate-stage-first-fable5-20260911.md
31c942b17ed290f13b0bcd87457ec3a2b68f760fc4cf99443fee0e8386eceb74  ROOT-REGISTRATION.preholder.json
4d0d8475ed7d4aac1e42b70b1c7b4ee0198270ead0c3bb46adb78d7a91153ba3  ROOT-REGISTRATION.json
58d35c476c3dc7c4f6fe36adf73b79e5e0d8843e6ddd388c27a745b747a40d2e  AUTHORITIES.preholder.json
1d9f837a23bb94b9609c7ac572909afbb0a4a96e44cb3c84b4875a9b310d02be  ROOT-EXECUTION-CARD.preholder.md
a92cf2680c8d6aff6044f5376fb1dcfeed87a29c527d55c953d940e39a99f281  ROOT-EXECUTION-CARD.md
6d414284920782a75a951fa3e59a8c23a391470a5efea28003b968bb1052fc62  final-install.preholder.sh
abff072f218cbecaa6f47278891a62b36463a70e34ae4be546e44a5f3c3cd208  final-install.sh
d90196456531bdf917098c84a84a88861384c220dcff6882a5305bacd48e8943  FINAL-INSTALL-INPUTS.sha256
73596b115c73db9aac6751c08d26b2a90cbddccfaa1d6a8615ada65a8076df90  caller.py
e5c6a438016c5b0129f13b2f0cf2ae5a1cdf450750429c8c5a5450c590b4cc35  test_caller.py
f57c247414746a6f4576b45a84f8f17c52052be4414f69e951e3be093b82e9cd  CONTRACT.md
e465ca6c062a8de1822eedd3f29ed5cb7bc2490b8d09fccaa89e79890048970d  PINS.json
d4d68584e3b60bb166155a20fcedc5bb67a1526235726ca0b2c53fda8d96853a  fixture-pins.json
6b4ab0834f67b69fa4f6af8d7246ec4d1de5f26a3b2731a2f4cf637280430126  fixture-observation.json
7f9ff04852b1d2c6a59815aff6ca28968204abb42ece7e5c5d444d489186e53e  fixture-decision.json
2a673cbd51a163c476f5b0a14faa4683a51851477a9780a0f76c5fbd05ca26da  caprun-candidate-caller-astra-20260911.md
511b7c06ab00dc1609039589415b231d0934f912332c3116badf443d6337bfc2  caprun-candidate-caller-astra-20260911.md.artifact.json
```

## Owned outputs (all authored via apply_patch; no Write/Edit/redirection)

```
1f74c77a16f6300e8ca8d33c3003302a2855943b50d760ff22627673cc531e3d  box/caprun-candidate-caller-first-fable5-20260911/review_controls.py
254bd2905fbc670374ffe717724733720e86b963c0a86dba9d98f73925a0dfe6  xmodel/caprun-candidate-caller-first-fable5-20260911.md
```

- Harness run: `python3 -I -S -B review_controls.py /tmp/jc2-lane.kgQvAj/inputs`, Python 3.12.3, exit 0, 170 expectations / 0 failed, stdout SHA-256 `5f58337e0d57390ec9f3c895de950c2d477c81f3ee99951a6b5c17f1fb70fa93` (stderr empty).
- Report: body authored 18:39 UTC; own full read and postpins 18:40 UTC; marker appended 18:40 UTC. One wording correction to the claim-3 sentence (the apply_patch tool unescaped a JSON escape sequence in the first text) was applied at 18:41 UTC with the marker retained as the unique last line and nothing after it; the report hash above is the final one. This file is the only artifact authored after the marker.
- No Seal and no charge_basis authored; no canonical OPEN raised. Original reserve 18:48:00 / HARD 18:51:00 UTC, never reset. All writers idle.
