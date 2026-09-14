# input_custody — f10-direct-rows-wire-gate-fable5-20260911

reader: claude-fable-5-1
inputs_dir: /tmp/jc2-lane.4kF5lM/inputs (EXACT9, unique basenames, mode -r--------)
pins_verified_utc: 2026-09-11T02:55:28Z (sha256sum, BEFORE any body read)
own_targets_absent_utc: 2026-09-11T02:55:28Z (both own outputs absent)

## Pre-read pins (all nine MATCH the charged pins)

| sha256 | bytes | file |
|---|---|---|
| 3be532afc6e784842694cf02d4399573228362abb47ae36130ef97c4274faa59 | 13873 | OPERATIONS.md |
| 61b9ce5e1f9b40a765dcb2a2ea5aa3a928197b61bc41cb5cf945632b99ad4de2 | 7439 | ASSERTIONS.md |
| b9060f0bbc14e92464079b0daca12faa1ba2d367f9ecc7307ba301689de5b77d | 10787 | WIRE-AND-VALIDATION.md |
| 425682e04adc5afa85b2c1482f8b75912b5f23e79336c203864afbb844c368e1 | 20787 | f10-source-cone-direct-circuit-gate-fable5-20260911.md |
| 39ed9b3910efee02dd2f17ced7951a8b83557e612d100d4ae34f76e0895b4002 | 8579 | ROOT-ADOPTED-CORRECTIONS.md |
| 90c940b021ba9f99f2298aaf394cb082793812ad4428e249b970ecf06baa6c47 | 12558 | f10-direct-rows-wire-root-20260911.md |
| e6df0a6458c682128c841a054e4cfb0be00cb2efde0325743f197cdcb0564725 | 16919 | f10-source-cone-direct-place-astra-20260911.md |
| 1aca7ad822cf88a95b30b2cb43c4a07227a78ca389fa28679e8fc1947e530ab0 | 20664 | f10-source-cone-direct-place-gate-fable5-20260911.md |
| 11d1b3a34edfde4d736a946d5543576e79f37fb6a45c737fffa07b3c360e037b | 11149 | f10-source-cone-fullrank-place-astra-20260911.md |

## Read log

All nine bodies were read FRESH_WHOLE in one parallel unclipped Read per file at 02:56:15Z, after the 02:55:28Z pin barrier, each through EOF (Seal or standalone marker where present); no clipping, no recovery needed. Line counts observed: OPERATIONS.md 68; ASSERTIONS.md 39; WIRE-AND-VALIDATION.md 38; f10-source-cone-direct-circuit-gate-fable5-20260911.md 56; ROOT-ADOPTED-CORRECTIONS.md 148 (Seal outside body); f10-direct-rows-wire-root-20260911.md 206 (Seal outside body); f10-source-cone-direct-place-astra-20260911.md 82 (Seal); f10-source-cone-direct-place-gate-fable5-20260911.md 54; f10-source-cone-fullrank-place-astra-20260911.md 65 (Seal). No linked, source, provenance, ledger, peer, live, payload or code body was opened; inputs directory is read-only and nothing in it was modified.

## Post-read pins

Recomputed by sha256sum after all reads at 03:02:56Z (prefix display) and again in full at the time of this write (03:03-03:04Z); all nine equal the pre-read table above and the charged list, byte for byte. Sizes unchanged (13873, 7439, 10787, 20787, 8579, 12558, 16919, 20664, 11149). Tools executed in this lane: date, ls, wc, sha256sum, cut, awk, tr, cat, apply_patch. Zero scientific subprocess/import/AST/compile/test/CAS. Owned outputs: xmodel/f10-direct-rows-wire-gate-fable5-20260911.md and this file only, both created by apply_patch, absent at 02:55:28Z. No Seal, charge_basis or transaction authored; adapter seals.
