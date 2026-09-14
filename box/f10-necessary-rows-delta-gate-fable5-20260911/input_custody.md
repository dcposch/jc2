# input_custody: f10-necessary-rows-delta-gate-fable5-20260911

Started 2026-09-11 06:18 UTC. Inputs dir /tmp/jc2-lane.47oEv6/inputs (26 files, immutable).

## Pre-pins

All 26 charged pins verified with `sha256sum -c` against the charged list (26 OK, rc 0) at 2026-09-11 06:20:55 UTC, BEFORE any body read. Table generated from sha256sum output, basenames only:

```
176363939a8aa6861995cd72a99c61f7d04bfeab5a9634f6d3143dcd3d3bd098  ROOT-ADOPTED-NECESSARY-ROWS.md
7beffe39c68b19e2998edc02949f8d24b3fe55a925d53139dff1c27a6690a482  ROOT-NECESSARY-ROWS-CANDIDATE.json
feef0643e84fbd28307c3bd3469fba974fa6b7f58ed0ef42bc2f92aa3c597aa3  ROOT-SOURCE-CONTRACT.json
acd07f800707c379aba60bd06f239d38cd83c86867729561367abd2bcc04ce73  arithmetic.py
6d74b9d7c879ad921a0c72f71d1a67d13fce933daa0b796653077487662f5c47  authority.diff
804c7aff56538fc332bf68638b03b7167eccdb49f73337f1a5f1823348b522a4  authority.py
7ba8b176f40c37c9643856135f4d8a17fbe9d3f08b148f39c685c8158fc07044  check.diff
1d2d5b5408bfbf13b96f09453b1f14dfe884d261e702843bc31e5a043ffa53d1  check.py
9d2aac637dbdeaa192cc3fe531e83694f9853b6573556ad5d49362f754b1163e  check_arithmetic.py
073e22dbcfa3a11a2afaf6fd9c845ca6ad1d0038ccd3fddc22db21e9f5beeb24  dispatch.py
f3c61b9a40d16e953950e3ff6a65401475a719fae6dbe3e1386cd05c49ef515f  dispatch.py.diff
0d6cb121ebdd769fb909608043b38e6ef08923d6e6a0411ca5ec057325169784  f10-direct-rows-code-gate-fable5-20260911.md
a02f120acda2439197a9fc173ec068ec0a5a208ec8d15f6b96cc9dfe65ee6ff9  f10-direct-rows-runtime-gate-fable5-20260911.md
8e07e419d321b09ecd13c61a1c5fdc3dbaf9a099c1a1ebedf9b9fe6ef280073b  f10-necessary-rows-design-gate-fable5-20260911.md
12eac7bbe5566ac0372c51b36617409e0501595024d948d6086a767f90d84eec  mutate.py
f5e3967d1603fb3e02ed0cb4a21ab306c866227f4e892a2f5c79414f2e19ed73  mutate.py.diff
5629db5df0a37fdaecaa66f5ad0cde47006cb0c3047b37243b045daedef2ac29  old-authority.py
5052884779d781e55693115c3065db1207667ce224a5914bbb95721d0abe9f7b  old-check.py
f5b6e6c43da4574c1dd9fc241d2f0596071ab505d561e67579eb28d382814480  old-dispatch.py
cc0621aa44d17b1dac346e87d20a53f69ce950b343d68c8ed0d3791d42120af0  old-mutate.py
09845fabff9a8b7f997e3b2d01160e5ff51d728124b9f5cd0b7176f8c19ea063  old-probe.py
8a7bd82ea589744a9de22b54877156a329d724185948538958801475f983760e  old-produce.py
5f1211e1a77b5ce2bb4cc496deabc533e3c41cdea88ea750149dac886cc09c69  probe.py
6fccfd82949cc678b4c423690e098e02f902e0a62f89d9efed5c2c6dee386432  probe.py.diff
592df59a401a2bf292b36214496b748cf6370c17f6bf65319db67e6245a210c4  produce.diff
5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a  produce.py
```

## Read scope

Independent `diff -u old-X.py X.py` for all six pairs, compared with the retained diffs after the two header lines by cmp: produce 49/49, authority 11/11, check 44/44, dispatch 93/93, probe 29/29, mutate 52/52 lines, all hunks identical. WHOLE reads: six .diff files; ROOT-ADOPTED-NECESSARY-ROWS.md (144 lines, through Seal); ROOT-SOURCE-CONTRACT.json (68); ROOT-NECESSARY-ROWS-CANDIDATE.json (141); design gate (44), code gate (53), runtime gate (66) through their markers; authority.py new (133). CONTEXT reads only: old-produce.py 262-280, 328-338; produce.py 2-7, 76-227 grep lines, 311, 315-325, 344-352; old-check.py 386-408; check.py 1-9, 74-92, 123-375 grep lines, 469-488, 494-514; dispatch.py 398-410 and grep lines; probe.py, mutate.py grep lines. HASH_ONLY: arithmetic.py, check_arithmetic.py. Token census (grep -c) over all twelve old/new sources. No whole read of produce/check/dispatch/probe/mutate is claimed. No linked, provenance, live or uncharged input.

## Post-pins

All 26 recomputed after every input read: `sha256sum -c` 26 OK, rc 0, at 2026-09-11 06:27:18 UTC; identical to the pre-pin table above and to the charged list. Inputs directory is read-only; scratch under /tmp/f10dg-scratch only. Tools: date, ls, mkdir (box directory only), sha256sum, wc, cat, sed, grep, awk, diff, cmp, apply_patch. No Write/Edit or redirection into owned files.
