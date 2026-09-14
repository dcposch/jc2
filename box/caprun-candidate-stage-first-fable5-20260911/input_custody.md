# Input custody — caprun-candidate-stage FIRST (Fable 5.1)

Inputs directory: `/tmp/jc2-lane.TOa5oq/inputs` (22 files, all read-only, count verified 22).

PREPIN 2026-09-11T17:55Z: all 22 charged SHA-256 values matched (`sha256sum -c`, 22 OK) before any read.
All 22 files were then read WHOLE through EOF with unclipped full-file reads; no linked source, fixture original, runtime, corpus or peer path was opened.

POSTPIN 2026-09-11T18:00Z (harness POSTPIN step, after all controls): all 22 charged hashes matched again; inputs unchanged.

Charged hashes (identical to the lane packet, verified pre and post):

```
6ac8e9ea645a2cb42c91ba0fe389d60d3db6c277b201c3557c2b231be8656067  TASK.md
f7c61db67a9982a99f1febaed6dae0b6e3595199ffccad70647b66556b907066  stage_patch.py
fbec59b7317689fd71124bc5702ebdd0cd5ddb4ec8854592bb8a0f0447d66ff8  historical_exercise.py
e8e59687fb87adf42f8656c265e8a525741c21239d4479ce0b3da8f855a8e54a  test_stage_patch.py
e21c3efe2a061dfbd25328c9d0f519b6fe693938317e127ecabb351514dc9da5  CONTRACT.md
88e7bc408852d226b119cc6dd26f9e91d0be16897e414b669e9c690142bab579  RECIPE.js
e37735ceeee1d60ee97ce492e196c312a8b9ee5d887f8abc9809af71924ce5b5  EXERCISE.json
69449fd5c02eb9f604d9b9f71532de9ecaf0e513e1e584c058da7db7bd9124d2  tests.stdout
ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe  latebind.py
85d5390babe473deed13e9a88c40ea82193c6306284a4224cdb021f65ca5ec06  test_latebind.py
3201abe5cae352f9e12ec6c842c6efe7ac463394b515cf2279d8266717296661  caprun-latebinder-first-fable5-20260911.md
31c942b17ed290f13b0bcd87457ec3a2b68f760fc4cf99443fee0e8386eceb74  ROOT-REGISTRATION.preholder.json
4d0d8475ed7d4aac1e42b70b1c7b4ee0198270ead0c3bb46adb78d7a91153ba3  ROOT-REGISTRATION.json
58d35c476c3dc7c4f6fe36adf73b79e5e0d8843e6ddd388c27a745b747a40d2e  AUTHORITIES.preholder.json
1d9f837a23bb94b9609c7ac572909afbb0a4a96e44cb3c84b4875a9b310d02be  ROOT-EXECUTION-CARD.preholder.md
a92cf2680c8d6aff6044f5376fb1dcfeed87a29c527d55c953d940e39a99f281  ROOT-EXECUTION-CARD.md
6d414284920782a75a951fa3e59a8c23a391470a5efea28003b968bb1052fc62  final-install.preholder.sh
abff072f218cbecaa6f47278891a62b36463a70e34ae4be546e44a5f3c3cd208  final-install.sh
d90196456531bdf917098c84a84a88861384c220dcff6882a5305bacd48e8943  FINAL-INSTALL-INPUTS.sha256
0363a58346b318be4767cf7938d77ff199a135d86f9d916e459f8db0b8b6a95a  PINS.json
498787894944fe77717687e1483979851993f93fb30a1e652e7fca3f5f9e143f  caprun-candidate-stage-root-20260911.md
4f8a2a2990ff7dafa018132a3be01493887896c5cbebc97c87b0c9b10f220d60  caprun-candidate-stage-root-20260911.md.artifact.json
```

Own outputs (authored via apply_patch only; no Write/Edit/redirection):

- `box/caprun-candidate-stage-first-fable5-20260911/review_controls.py` SHA-256 `b28501f3738c19cbdc6c13fd41f46610d08184d5b2012acd323f5f7967ff9a13`
- harness stdout SHA-256 `d3269b5a916a312b098aa32b2016e1285863da5090f461890ae0e56a47929306` (deterministic; 35/35 controls)
- `xmodel/caprun-candidate-stage-first-fable5-20260911.md` (9330 bytes, 1305 wc words, unique standalone `<!-- BODY-END -->` last line, nothing after, no Seal, no charge_basis) SHA-256 `d96d979c950bf51faea0ad430af4f2eed1366d8f7b3e952e27d048ca2dff2273`; marker appended 18:02:54 UTC after own full read and 22/22 postpins at 18:02:28 UTC.
- Same-stem `.log` and `.run.v2` files in xmodel/ pre-existed at 17:54 UTC (external adapter launch records); not authored, opened or counted as own outputs.
- No harness or writer process remained after the last write (pgrep at 18:03 UTC); all writers idle.

Replay: `python3 -I -S -B box/caprun-candidate-stage-first-fable5-20260911/review_controls.py /tmp/jc2-lane.TOa5oq/inputs`

Not opened: any path outside the inputs directory and these three own outputs; no original fixture directory, no linked runtime, corpus or peer file; no input .sh/.js executed.
