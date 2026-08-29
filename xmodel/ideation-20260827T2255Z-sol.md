# Sol Ultra blind-lane custody failure — `20260827T2255Z`

## Disposition

**FAIL CLOSED.** No whole-portfolio ideation submission is made from this
packet because one mandatory canonical input failed its frozen SHA-256 check.

## Checks

- Packet
  `xmodel/ideation-20260827T2255Z-packet.md`: expected and observed
  `d8a01725bc2730ce49069c96f4287956fb867b64e324ea6828076e19986e6b15`
  — pass.
- `APPROACHES.md`: expected and observed
  `f9ed44dff02d455d2678f8aecf5a525f9ca2941013725abb8d8707ba76e21cc8`
  — pass.
- `AUDIT.md`: expected and observed
  `aee767b1df96cdd466616b97e9fe4979332ff23434bbe80061f9413c2df2b7cf`
  — pass.
- `COORDINATION.md`: expected and observed
  `743d684baadd4d5e0e73ecf05963041d83dd52ac1b90a40a7b1ccab206e467a0`
  — pass.
- `PROGRESS.md`: expected and observed
  `0d22e3972eba15547889a883cea588a4fde4f87f58ea3187e1d458a291276686`
  — pass.
- `notes.md`: expected
  `5d2abd49f67800b0be9d1983804a8459c27fff2f48c81696a5f38e00f8731cc2`,
  observed
  `919e37870acf362d4941f0eabe1d87fe7a5c7865066e35a7518588184308b73a`
  — **fail**.
- `xmodel/ideation-20260827T2137Z-synthesis-sol.md`: expected and observed
  `668d78c96088d168361874733f81d7dee724769a6177a723bd0561e60ad850d0`
  — pass.
- `xmodel/ideation-20260827T2137Z-opus5-crossreview-fable5.md`: expected and
  observed
  `b3f3886c7783ce22e060865206a700f0aab356caf6f708f75f355e99b684517a`
  — pass.
- `xmodel/ideation-20260827T2137Z-fable-linear-vacuity-hostile-review-sol-ultra.md`:
  expected and observed
  `5beb555075c662e76f8b86062efdf89b2c3a4dd0eb80ffd52fbf3c38bf130d55`
  — pass.
- `xmodel/ideation-20260827T2137Z-postseal-exact-hostile-review.md`: expected
  and observed
  `8bad7ca04ae9a6f45efde305b208309f528173820250d20dab67d00bc32d73a4`
  — pass.

## Scope and contamination ledger

- I read the prompt and packet in full, then performed the complete mandatory
  hash check before reading the mandatory corpus.
- On the `notes.md` mismatch I stopped, as required. I did not read any
  mandatory input contents, did not scan the 46 avenues, and did not infer a
  response from stale context.
- I did not inspect any peer `20260827T2255Z` response.
- I did not enter, list, search, read, build, status, or modify `jc2-lean`.
- I did not touch AWS or running jobs and ran no algebra.
- The hash command emitted only a host locale fallback warning; this does not
  affect SHA-256 values.
- No assumptions or conjectural mathematical claims were made. The sole
  failure is frozen-input custody, plausibly caused by a concurrent canonical
  edit but not investigated because the contract requires fail-closed
  behavior.

## Required recovery

Freeze a new packet (or explicitly amend this packet) with the intended
`notes.md` hash, then launch a fresh blind lane. This report must not be
treated as a substantive vote or model-capability sample.
