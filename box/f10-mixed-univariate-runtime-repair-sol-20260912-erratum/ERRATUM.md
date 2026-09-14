# Provenance erratum

This corrects provenance metadata for the immutable
`f10-mixed-univariate-runtime-repair-sol-20260912` packet only. It changes no
source, report, manifest, PINS, custody, authority, or runtime status.

The actual SHA-256 of the charged prior custody file
`box/f10-mixed-univariate-runtime-sol-20260912/custody.json` is:

`39c5c3438293d6893f7c56bc3428acb5ae824df8aec937c1a9035f7f59051bf0`

The immutable repair packet's `PINS.json` incorrectly transcribed that value as
`39c5c343829d6893f7c56bc3428acb5ae824df8aec937c1a9035f7f59051bf0`.
The terminal shell postpin output itself displayed the correct actual digest;
the defect is in the authored PINS transcription and downstream blanket
`inputs_postpins_match` wording.

The original fresh WHOLE-read scope was: `COORDINATION.md`; prior runtime
`custody.json`, `dispatch.py`, `probe.py`, `REGISTRATION.disabled.json`,
`CONTRACT.md`, and `PINS.json`; delivered `DISABLED-AUTHORITY.template.json`,
`produce.py`, `check.py`, `CONTRACT.md`, and `VALIDATION.md`. The resulting
repair `dispatch.py`, `REGISTRATION.disabled.json`, `CONTRACT.md`, `PINS.json`,
report, and manifest were also read back WHOLE.

Additionally, delivered `authority.py` was in fact read WHOLE: lines 1--220
were requested and the file has 160 lines. It was omitted from the authored
read-scope census and was not hash-pinned before or after that read. Therefore
the repair packet's postpin claim is valid only for the files explicitly shown
in its terminal shell postpin output, using the corrected prior-custody digest;
it does **not** establish an `authority.py` pre/post pin. The static trace to
`authority.py` must be treated as an unpinned read, not authenticated source
provenance.

All runtime statuses remain DISABLED / UNEXECUTED / UNREVIEWED / UNREGISTERED.
No worker or execution authority is approved by this erratum.
