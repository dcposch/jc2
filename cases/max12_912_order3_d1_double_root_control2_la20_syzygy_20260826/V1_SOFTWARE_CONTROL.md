# V1 software control — no mathematical verdict

Status: `QUARANTINED_NO_VERDICT`.

- AWS host: r6d (`100.26.198.153`)
- job tag: `max12_912_order3_d1_double_root_control2_la20_syzygy_20260826T015817Z_r6d_LPDP`
- registered worker PID: `203253`
- stopped Singular PID: `203642` (this registered job only)
- start/finish: `2026-08-26T02:00:07Z` / `2026-08-26T02:07:25Z`
- frozen input SHA-256: `2d22f9867aceb250d8df6002fc4a541fffd225dfb6f8b18d3bbce2aab0f75737`
- stdout SHA-256: `90bc881ec6d51f34b1797ff8a612b5ff97b0452933613e313e364e654eb74d00`
- stderr SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty)
- time SHA-256: `80cbfc7e1e5dc053e18dc5657ddcd9342ac7eab33ac9a770f1d9cf9fcd903fc8`
- remote quarantine marker SHA-256: `48c7edf57e6f59925d633f4cb5d83c9cdbe36383ebacf8b0b074211c7a9c76b1`

The emitted Singular source declared `ideal GCD=std(CD);`. On Singular
4.3.2, `GCD` is a reserved/outdated identifier. Singular printed parser
diagnostics to stdout and continued past the malformed declaration. The V1
wrapper did not classify stdout parser diagnostics independently of stderr.
The process was stopped and returned rc `1`.

No printed intermediate, including the apparent saturation exponent, is a
mathematical endpoint. This run is retained only as a source/deployment
negative control. The previously frozen corrected-A fixed-weight obstruction
does not depend on this run.
