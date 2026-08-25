# Immutable quarantine ledger

The following artifacts remain byte-for-byte available for audit but must not
be consumed as mathematical input after the hostile refutation:

| Artifact | SHA-256 | Status |
|---|---|---|
| `xmodel/max12-912-order3-nu-parity-normal-q12-20260824.md` | `9616396705d071efac3cf52332c5007a4a045989940bcc8743a545e87f763a1c` | refuted |
| `cases/max12_912_order3_nu_parity_normal_q12_20260824/MANIFEST.sha256` | `2af02f169f4c65e7bfd3627d8f05934b0bdbdc35df1c1b9a0577f765b0a6b70e` | refuted case manifest |
| `cases/max12_912_order3_nu_parity_normal_q12_20260824/FREEZE.txt` | `a2d342a0d70911263a72172ba3ee02f21e33951ca9d2f4753f8de39d1dca54d0` | refuted freeze |
| `xmodel/max12-912-order3-nu-q12-formal-branch-20260824.md` | `fd4db3e2125a11c05dac3c9613b8f4305942150d0e92a3200259e595c2afce62` | invalid descendant |
| `cases/max12_912_order3_nu_q12_formal_branch_20260824/MANIFEST.sha256` | `3ced488452275f29a4645efb098c87a987e54eb3df85b9f5646da8da8bdbe099` | invalid descendant manifest |
| `cases/max12_912_order3_nu_q12_formal_branch_20260824/FREEZE.txt` | `aa17408d0f860158fdd55577315299f9d9298599f8c7d37c72cb306fbb29b83c` | invalid descendant freeze |

Hostile refutation:

```text
xmodel/max12-912-order3-nu-parity-normal-q12-review-grok-20260824.md
SHA-256 fc0b0216784bdcec8f9b0955c5a6c71d57870ae2265ed927f306d19d31a79c30
```

The reviewed parity genus-five exclusion is not quarantined: its replay uses
the correct polynomial numerator `1+3v` and its theorem remains confirmed.
