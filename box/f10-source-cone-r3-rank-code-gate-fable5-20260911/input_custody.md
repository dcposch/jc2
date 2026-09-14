# input_custody — f10-source-cone-r3-rank-code-gate-fable5-20260911 (Fable 5.1 FIRST, static only)

Lane inputs: /tmp/jc2-lane.ubjvQO/inputs (read-only, 15 unique basenames). First action 2026-09-11T01:38:24Z; both owned targets ABSENT at 01:38:57Z. Pins verified with `sha256sum -c --strict` (15 OK, exit 0) at 01:39:20Z BEFORE any body was read. Reserve 02:03:00Z / HARD 02:06:00Z never reset. Rows below are sha256sum/wc output, not typed.

## Pre-read pins (sha256sum, 01:39:20Z; identical to the charged list)

```
96f8374e9b3128ad5ff6ef498b1d547adc134da8a4202039a9b567bfc73d5af3  CONTRACT.md
bc9e7fa50564933edecdb8f37b39f5233171d7bda765a26ec5e1d7912294289b  CONTROLS.md
b9a93692f138193714b5359b6f958640f767aeabcdc66e4babe26bf862cf0a7f  READ-SCOPE.md
75d86856f0da7e8e0779ba9abecad08bce7a5f5e7424b09000bbbd4a45a980a9  authority.py
b9176ee7f0b8f34506e0fce03c2aea548756d0d489a53b732401cc7dbaa8c87f  check.py
6e780b49ad344879dd48b9e6e4d59724172820e0194cd7e8daf356282dbf695f  checker.py
678ccf0ded5b7a9e2551ed48c95ecc2322937def758218ac2674572d46a9bcb0  custody.json
11d1b3a34edfde4d736a946d5543576e79f37fb6a45c737fffa07b3c360e037b  f10-source-cone-fullrank-place-astra-20260911.md
6e73b5b992fb75d456c71928cacf980f30d0065117e8875403438c12e49112bc  f10-source-cone-fullrank-place-gate-fable5-20260911.md
712ac6023b6799c079e5b950822d07c20295d46788f38d64a433af7f45cd3103  f10-source-cone-r3-code-gate-fable5-20260911.md
cc92fc304b7950692ec3f16ce7ad7e2ec549178e585a05e348948a4e152fad1f  f10-source-cone-r3-rank-code-astra-20260911.md
e644208e84b5f2800559489af71f9fb05806a45c5abc0ae7c719ca38225401b7  finder.py
bd16da8c84ae3a8ad2d3bed3a654914fdb843ed0a2e4a1f9bfb6430adbd54986  ideation-20260910T2300Z-astra-source.md
76ad6c85a6c5d4ccbd01c642c43ff7002cb7060a1367e11ee5927a272ce06a5a  produce.py
492ce280b9069d377051c9b4193847d261b53453123a7e78143d5346c23fb9bf  wire.py
```

## Byte counts (wc -c; all equal custody.json rows where listed)

```
 10630 CONTRACT.md
  2350 CONTROLS.md
  2653 READ-SCOPE.md
 11372 authority.py
 27237 check.py
  8505 checker.py
  5356 custody.json
 11149 f10-source-cone-fullrank-place-astra-20260911.md
 12364 f10-source-cone-fullrank-place-gate-fable5-20260911.md
 15960 f10-source-cone-r3-code-gate-fable5-20260911.md
  7429 f10-source-cone-r3-rank-code-astra-20260911.md
 10881 finder.py
 15951 ideation-20260910T2300Z-astra-source.md
 15140 produce.py
  5353 wire.py
162330 total
```

## Sealed body hashes reproduced (head through the standalone marker line | sha256sum)

```
d3fc718e3ca04557850b43bd7ce66e6346d9936cdb33569360f57f7ae27989d9  7097 bytes  f10-source-cone-r3-rank-code-astra-20260911.md
68535062f0e931bb252f4cf813bbb84008d2474d8b5ebae487b8698e1d5eb1cd  10816 bytes  f10-source-cone-fullrank-place-astra-20260911.md
db02be69448e78b38e444a1379cbeead560f7cd8a30a4c1a5b4e31d187e6767a  15618 bytes  ideation-20260910T2300Z-astra-source.md
```

Read scope: every input FRESH_WHOLE through EOF with cat -n; check.py (540 lines) in two contiguous ranges 1-270 and 271-540; no clipping remained. Zero CAS/subprocess/import/AST/syntax/compile/test; no coefficient, fixture, baseline, place or candidate body; no provenance, live, peer, protected, network, Git or agent access. Writes: apply_patch only (this file, the report skeleton, bounded report sections, and the post-read append below).

## Post-read pins (2026-09-11T01:50:47Z; sha256sum -c --strict on the charged list returned 15 OK at 01:50:29Z and again here)

```
96f8374e9b3128ad5ff6ef498b1d547adc134da8a4202039a9b567bfc73d5af3  CONTRACT.md
bc9e7fa50564933edecdb8f37b39f5233171d7bda765a26ec5e1d7912294289b  CONTROLS.md
b9a93692f138193714b5359b6f958640f767aeabcdc66e4babe26bf862cf0a7f  READ-SCOPE.md
75d86856f0da7e8e0779ba9abecad08bce7a5f5e7424b09000bbbd4a45a980a9  authority.py
b9176ee7f0b8f34506e0fce03c2aea548756d0d489a53b732401cc7dbaa8c87f  check.py
6e780b49ad344879dd48b9e6e4d59724172820e0194cd7e8daf356282dbf695f  checker.py
678ccf0ded5b7a9e2551ed48c95ecc2322937def758218ac2674572d46a9bcb0  custody.json
11d1b3a34edfde4d736a946d5543576e79f37fb6a45c737fffa07b3c360e037b  f10-source-cone-fullrank-place-astra-20260911.md
6e73b5b992fb75d456c71928cacf980f30d0065117e8875403438c12e49112bc  f10-source-cone-fullrank-place-gate-fable5-20260911.md
712ac6023b6799c079e5b950822d07c20295d46788f38d64a433af7f45cd3103  f10-source-cone-r3-code-gate-fable5-20260911.md
cc92fc304b7950692ec3f16ce7ad7e2ec549178e585a05e348948a4e152fad1f  f10-source-cone-r3-rank-code-astra-20260911.md
e644208e84b5f2800559489af71f9fb05806a45c5abc0ae7c719ca38225401b7  finder.py
bd16da8c84ae3a8ad2d3bed3a654914fdb843ed0a2e4a1f9bfb6430adbd54986  ideation-20260910T2300Z-astra-source.md
76ad6c85a6c5d4ccbd01c642c43ff7002cb7060a1367e11ee5927a272ce06a5a  produce.py
492ce280b9069d377051c9b4193847d261b53453123a7e78143d5346c23fb9bf  wire.py
```

Input pre/post: ALL_MATCH (15/15). Own final WHOLE read of the report (full cat, no truncation) and of this custody file performed at 2026-09-11T01:50:47Z before the single marker write; marker appended as the last line of the report only after that read; nothing follows it. Own-only collision: both owned paths were absent at 01:38:57Z and are the only paths this lane created; no peer, live, provenance, protected or input file was opened for writing. OPEN raised: no new canonical ID (one existing exact-rank quantity, cheapest instrument and unmeasured numeric wall stated in the report). Adapter seals; this lane authored no Seal, charge_basis or transaction. Writers IDLE after the marker write.
