# Input custody: f10-direct-rows-code-gate-fable5-20260911

lane=f10-direct-rows-code-gate-fable5-20260911
author=Fable 5.1 (claude-fable-5-1)
inputs_dir=/tmp/jc2-lane.Q9HCYx/inputs (read-only lane mount, 16 files, unique basenames, 184744 bytes total)
own_targets_absent_utc=2026-09-11T03:38:38Z (report and box both absent before first write)
prepins_verified_utc=2026-09-11T03:39:20Z (sha256sum -c against the charged list, 16/16 OK, before any body read)
postpins_verified_utc=2026-09-11T03:54:03Z (same list recomputed after every read, 16/16 OK)
skeleton_written_utc=2026-09-11T03:39:32Z (after prepins, before any body read)

## Charged pins (EXACT16, identical pre and post)

| sha256 | basename | lines |
|---|---|---:|
| 3be532afc6e784842694cf02d4399573228362abb47ae36130ef97c4274faa59 | OPERATIONS.md | 67 |
| 61b9ce5e1f9b40a765dcb2a2ea5aa3a928197b61bc41cb5cf945632b99ad4de2 | ASSERTIONS.md | 38 |
| b9060f0bbc14e92464079b0daca12faa1ba2d367f9ecc7307ba301689de5b77d | WIRE-AND-VALIDATION.md | 37 |
| 39ed9b3910efee02dd2f17ced7951a8b83557e612d100d4ae34f76e0895b4002 | ROOT-ADOPTED-CORRECTIONS.md | 147 |
| 90c940b021ba9f99f2298aaf394cb082793812ad4428e249b970ecf06baa6c47 | f10-direct-rows-wire-root-20260911.md | 205 |
| 68488229c5ff839f8c155662f903ba174d59d4e96bb5e046a53967313d497f1b | f10-direct-rows-wire-gate-fable5-20260911.md | 50 |
| 2b2770fe494098812a52c6829a4bd97803f44bb0474863b8008a69f3725956fd | ROOT-ADOPTED-WIRE-PINS.md | 103 |
| a0a40804071a6dac83eaf6acf38073229a6d15c8866af32e283015d65c1c74e7 | ROOT-AUTHOR-INTERFACE.md | 110 |
| 5629db5df0a37fdaecaa66f5ad0cde47006cb0c3047b37243b045daedef2ac29 | authority.py | 133 |
| d196346966f09f1e9ef2a4f6e20df74f8d218c32e06d2f341ccf25fb4b39d90b | arithmetic.py | 349 |
| 8a7bd82ea589744a9de22b54877156a329d724185948538958801475f983760e | produce.py | 382 |
| 9d2aac637dbdeaa192cc3fe531e83694f9853b6573556ad5d49362f754b1163e | check_arithmetic.py | 286 |
| 5052884779d781e55693115c3065db1207667ce224a5914bbb95721d0abe9f7b | check.py | 529 |
| f264cb7577a4a08ba07a403856d72af243c1bd91e5443f8f08f6da16c3528f0b | CONTRACT.md | 44 |
| 692c89cbe333e33c87c85f0ba92e6e39b505c57ae9f36d17814036a22c5e2833 | f10-direct-rows-producer-astra-20260911.md | 52 |
| bfac10237e7cbb10db0d2893c1cd14480a0fe9bfb438824f94cf8c2bf999f4a7 | f10-direct-rows-checker-astra-20260911.md | 171 |

## Read record (FRESH_WHOLE, no prior reuse, no provenance expansion)

- Fifteen files were displayed whole with line numbers in one parallel batch at 03:39-03:40Z via `cat -n`; each display ended at its last line (EOF; for sealed reports through the Seal block).
- check.py (529 lines) exceeded the display limit on that batch (persisted, first 2 KB shown). It was NOT claimed whole from that output; it was re-read in three explicit ranges 1-180, 181-360 and 361-529 (EOF confirmed) at 03:40:02Z via sed with computed line numbers.
- CONTRACT.md did not display in the first batch; it was read whole (44 lines, EOF) at 03:40Z on a second request.
- No file was read partially and then claimed whole; no clipped aggregate remains.

## Tools and prohibitions

- Tools used: date, ls, sha256sum, wc, cat, sed, awk, grep, printf, apply_patch. No python, no CAS, no import, no AST/syntax/compile, no test, no dummy, no network, no AWS/SSH, no git, no process control, no agents.
- No source code implemented or modified; no mathematical payload, fixture, prime, place or baseline generated.
- No Write/Edit tool and no shell redirection into owned files; every owned byte was written by apply_patch in bounded chunks under 1500 words.
- Owned files only: this custody file and xmodel/f10-direct-rows-code-gate-fable5-20260911.md. No Seal, charge_basis or transaction authored; the adapter seals.
