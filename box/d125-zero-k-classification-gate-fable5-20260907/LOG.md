# Custody log — d125-zero-k-classification-gate-fable5-20260907

- 03:47:10 UTC start; frozen inputs /tmp/jc2-lane.3223i6/inputs (13 files, hashed; report 129947ee…, check.py 61226b60…, witness fc345a15…, client.py ec2fa2d1…, predecessor gate 9d6f594f…, its controls 953455a9…, discriminator 99d25147…).
- 03:54–03:55 gate_controls.py --record: 8 runs PASS (normal/-O × none, --mutate-source-face, --mutate-missing-negative-row, --mutate-wrong-factor), 2.41 s wall, 40204 KB peak; witness 1461b907…, replay 5fbe22ab…, script 37e664c9….
- 03:55:33 frozen check.py run once read-only under caps: rc 0, stdout sha256 fc345a15… (matches charged witness). No frozen file written (a stray tee into the read-only dir failed; see frozen-check-readonly.log here).
- 03:56:47 report written: xmodel/d125-zero-k-classification-gate-fable5-20260907.md, 1696 words, single standalone BODY-END as last line, no seal; sha256 68e04e8c….
- Not executed/reused: predecessor gate_controls.py (R^3/R^5 and 15/25 jet-pair expansion at lines 84,130–134; its no_A15_B25_expansion flag is false).
