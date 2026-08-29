# V82QST3 first-launch dispatch erratum

The first Box02 wrapper, SHA-256
`55a26d5d4eb3038cc0eab2fe8e386a424c79d268039ddaa012aac972e5c899f5`,
assigned the new callback to `m.run_staged`.  The imported V82QST2 `main()`
subsequently overwrote that name from its own module-level
`run_staged_f_raw`, so both q2 and q10 merely reran V82QST2 and printed its
old banner.  Their rc-zero endpoints contain no V82QST3 result and are not
consumed.

The repaired wrapper assigns the callback to `raw.run_staged_f_raw` before
calling `raw.main()`.  Its source SHA-256 is
`a69213807318b81600f667aec7be85ff6126c06ca008914e3a78a1281577bff0`.
Acceptance requires the distinct banner
`TD6-V82QST3-F-RAW-GENUINE-P12-SOURCE PASS`; the V82QST2 banner is a failed
deployment control.

The repaired-dispatch Box02 run rooted at
`/home/ubuntu/runs/td6_v82qst3_f_p12_v2_box02_20260826T1118Z` reached the
post-identity coordinate audit in both lanes, then exited 1 because the audit
attempted to call FLINT's `fmpq_mpoly_ctx` object as a constructor for the
constant polynomial one.  This is a reporter/API error, not a passed
certificate: the endpoint is quarantined and its absence of the PASS banner
is preserved.  The successor compares denominators with
`Rat3(1).denominator`; it must rerun every assertion and emit the complete
certificate before acceptance.  That corrected successor has SHA-256
`6977d0acb3d178447effe225f80f7f415a23042090092a648a8bbfbfc462a497`.
