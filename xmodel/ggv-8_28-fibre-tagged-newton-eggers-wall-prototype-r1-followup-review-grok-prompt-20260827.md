# Follow-up hostile review: GGV `8_28` prototype R1 repairs

Date: 2026-08-27

Review only the two repairs requested in
`xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-hostile-review-grok-20260827.md`.
Do not edit producer, canonical, or `jc2-lean` files.

Inputs:

- original hostile review SHA-256
  `971147c5c8a6d3f26c103b0a2da1095ca7c302a2cfd1e812556eaddf6d21a316`;
- R1 adjudication
  `xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-r1-adjudication-sol-20260827.md`;
- custody wrapper SHA-256
  `7c1205ff3247e06c31729c22a65c39b1e5bf3bd99e28d5fe6a7780ab3ac315b5`;
- custody note SHA-256
  `c456cffd52d836ada364b585fc1cc361bc0a07f6efa5d3718e6e41e45ac19edb`;
- frozen result SHA-256
  `deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd`;
- current `ladder/TRANSPORT.md` SHA-256
  `9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c`.

Independently rehash the inputs.  Audit that `verify_r1.py` pins the exact R0
verifier, changes only the contextual transport digest, reruns all original
mathematics, and compares every mathematical output field exactly.  Run it
and require `PASS`.  Confirm that no frozen R0 byte was rewritten.

Then audit the packet-scope correction: “minimal” must be withdrawn; only
the `y`-residual/root/pole vector and `x*y^15` provenance are
collision-forced, while the other listed fields are merely sufficient or
example-supported.  Enforce the non-Keller/Keller and `G2-PSC` firewall.

Write only

```text
xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-r1-followup-review-grok-20260827.md
```

with verdict `PASS`, `FAIL`, or `INDETERMINATE`, exact replay hashes, and the
smallest licensed result.  Print its path and SHA-256 on completion.
