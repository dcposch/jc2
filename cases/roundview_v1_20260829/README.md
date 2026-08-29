# ROUNDVIEW/v1 bounded systems trial

Status: **generated, non-authoritative infrastructure trial**.  This packet
does not alter `APPROACHES.md`, create a launch queue, or promote any claim.
Its only input is a hash-pinned `APPROACHES.md` snapshot.

`roundview.py` emits a compact round input containing exact source-byte
slices for:

1. the preamble;
2. the newest superseding strategy overlay;
3. the canonical master-union table heading, header, and all 46 numbered
   avenues (the whole table section is retained, so wrapped continuation
   lines cannot be dropped);
4. an index of every older overlay heading, with exact source line range and
   full-section SHA-256; and
5. a custody manifest with the source SHA-256, source size, exact slice line
   ranges and hashes, plus explicit `GENERATED_NON_AUTHORITATIVE` and
   `NO_SECOND_QUEUE` warnings.

The emitted body has an internal byte-count/SHA-256 seal.  `--check` first
verifies that seal and then compares a fresh compile byte-for-byte, so either
stored-output drift or source drift fails closed.  `--expect-source-sha256`
pins round custody before compilation.

## Use

From the repository root:

```sh
python3 cases/roundview_v1_20260829/roundview.py \
  --source APPROACHES.md \
  --source-label APPROACHES.md \
  --expect-source-sha256 "$(shasum -a 256 APPROACHES.md | awk '{print $1}')" \
  --output /tmp/jc2-roundview.md

python3 cases/roundview_v1_20260829/roundview.py \
  --source APPROACHES.md \
  --source-label APPROACHES.md \
  --check /tmp/jc2-roundview.md
```

The writer refuses a symlink output and uses a same-directory atomic replace.
The source is read twice from one descriptor while both descriptor and path
fingerprints are checked before and after the reads.

## Fail-closed grammar

Compilation stops on any of the following:

- a missing overlay, duplicate overlay heading, a non-newest first strategy
  overlay, or reverse-chronology violation;
- a missing or duplicate master-table heading/header/divider;
- numbered avenue rows other than exactly `1,2,...,46` in that order;
- source mutation while reading or mismatch against the expected source hash;
- a compiled size that is not strictly below 15% of its source; or
- malformed stored body seal or any byte difference under `--check`.

The heading grammar is intentionally narrow.  A deliberate canonical format
change should update and review the compiler rather than silently selecting a
plausible-looking section.

## Tests

```sh
python3 -m unittest -v cases/roundview_v1_20260829/test_roundview.py
python3 -O -m unittest -v cases/roundview_v1_20260829/test_roundview.py
```

The suite checks ordinary/`-O` byte determinism, exact-slice inclusion,
negative missing/duplicate overlay and avenue fixtures, the 15% size ceiling,
source/output hash drift, and the `20260829T0820Z` historical basis.  That
backtest obtains `APPROACHES.md` from basis commit
`eaad172e59742ef8cfd055eace9bc6d3b2da8463` and verifies the source SHA-256
printed in the sealed state packet.

## Scope limitation

ROUNDVIEW/v1 compacts only `APPROACHES.md`.  It does not retrieve new evidence
from `PROGRESS.md`, `AUDIT.md`, `notes.md`, source papers, or live lane state.
A coordinator must still provide the round-specific delta and contracts.  The
output is therefore context material, not a complete state packet and never a
second campaign authority.
