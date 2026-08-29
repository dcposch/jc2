# V43C4 exact result: unsplit rho-zero `a1^104` membership

Status: **provisional exact PASS; different-model hostile review pending**.

In the ordinary polynomial ring `Q[X19_rho0]` on the frozen 65-variable
ordered-a1 alphabet, the 51 named raw rows through grade 19 generate an ideal
containing `a1^104`.  The exact serialized certificate uses 16 literal rows:

`Tg11_1, Tg12_1, Tg12_2, Tg13_1, Tg13_2, Tg13_4, Tg14_1, Tg14_2,
Tg14_3, Tg14_4, Tg15_3, Tg16_5, Tg16_6, Tg17_5, Tg18_6, Tg19_7`.

The corrected derivation first rebases the inherited branch assumptions by

`e1 = (e1-4*a1*ell1) + 4*a1*ell1`,

`ee0 = (ee0+4*aa0*ell1) - 4*aa0*ell1`.

All subsequent ClearPower and CombineBranches guards replay unchanged.  At the
final cleanup, the only surviving assumption multipliers are exact-zero DAG
products.  The replay checks a literal direct factor and expands it over Q:

| label | multiplier root | zero direct factor | peak terms |
|---|---:|---:|---:|
| `assume:ee1` | 721 | 427 | 9 |
| `assume:ez3` | 723 | 401 | 3 |
| `assume:rs2` | 722 | 399 | 3 |

`PruneZeroFactor` verifies root membership of each factor, exact zero
expansion, and committed telemetry before deleting the term.  Serialized
replay independently reconstructs all 71 derivation nodes and 29 checkpoints.
The final certificate has no assumption labels.

Controls all reject as registered: Tg19_7 omission; exponent 2 changed to 3;
both rebase signs flipped separately; and each zero factor changed separately
to direct nonzero factor 371 (`a1`).

## Evidence

- AWS host: r6b (`ip-172-30-0-106`), one core, zero swap.
- Runtime: 7.03 seconds; maximum RSS 36,764 KiB.
- Immutable source-manifest SHA-256:
  `27f42f0f280ea30101d6f5aab193953ee0581eefc59ad673f9b398e1b86cd89f`.
- Exact proof SHA-256:
  `3e0e80c0c9ab07803d60ea6b3284daeae6dbdeb858c6af875a1457174f5b0862`.
- Result JSON SHA-256:
  `629a0763f784e2d18c5acc433313c486d51b141a91d933b01303fb7d7959393c`.
- Harvested AWS evidence-manifest SHA-256:
  `88cad66d11b885197437e87350709fd81cff887421332d1ff090461fd3e1a1b3`.
- Precursor exact factor diagnostic SHA-256:
  `b9ebbaa4d73c12705096cad73a1c9e3b5b7a4c633a9dc94d7eaa86ff3d42b0cc`.

## Firewall

This proves only membership in the frozen raw `rho=0` ideal.  It does not by
itself prove an unspecialized-rho or saturated-Rees statement.  Combined with
the separately reviewed exact generic identity `5*t^6*a1^4 in J`, it supplies
the special-fibre input for a *prospective* exponent-628 converter; that total
certificate must be built and replayed separately, and no exponent-628 claim
is made here.
