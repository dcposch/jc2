# R1 adjudication: one-chain GGV `8_28` fibre-tree control

Date: 2026-08-27

This additive note preserves the frozen producer and folds the two repairs
requested by Grok's hostile review (SHA-256 `971147c5...`).

## 1. Custody repair

During the review, the coordinator folded the already-filed errata from
`xmodel/grok-transport-review.md` into `ladder/TRANSPORT.md`.  The original
prototype verifier correctly failed closed because that contextual file's
digest changed from `39a607c8...` to `9750aa9d...`.

No frozen R0 artifact was edited.  The additive wrapper

```text
cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify_r1.py
```

pins the exact R0 verifier (`4dfe7c6...`), changes only the expected
`TRANSPORT.md` digest, reruns the complete unchanged mathematics, and
requires equality with frozen `RESULT.json` after separating its contextual
`source_pins` field.  It passes with
`mathematical_result_unchanged=true`.

R1 wrapper SHA-256: `7c1205ff3247e06c31729c22a65c39b1e5bf3bd99e28d5fe6a7780ab3ac315b5`.
Custody note SHA-256: `c456cffd52d836ada364b585fc1cc361bc0a07f6efa5d3718e6e41e45ac19edb`.
Frozen result SHA-256: `deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd`.

## 2. Packet-scope repair

The producer heading “minimal sufficient typed packet” is withdrawn at the
word **minimal**.  The eight fields listed there form one sufficient packet
for this example; the collision does not prove every field necessary.

The `tau=1 -> 2` collision forces only the information that distinguishes
the two controls:

- the paired `y`-chart residual `X^8+1+tau*X` modulo `X^16-1`;
- its roots and cancellation multiplicities;
- the resulting pole-order vector; and
- provenance of the source monomial `x*y^15` carrying `tau`.

The fibre tag, both chart maps, `x`-chart residuals, deck/place grouping,
Q/jump/max data, and the displayed partial provenance are useful and
example-supported, but not collision-necessary.  A total inverse/source
provenance map is a proposed compiler interface, not a theorem from this
example.

## 3. Smallest licensed result

The independently replayed mathematics is retained exactly at this scope:
one explicit **non-Keller** pair realizes the complete live one-edge `8_28`
GGV record; both infinity charts, sheet count 72, Q/jump/max `1 -> 4 -> 28`,
and pole mass 276 are exact; changing `tau` from 1 to 2 preserves the current
GGV ledger but drops one `y`-chart pole from 12 to 11 and the mass from 276 to
275.  Therefore the present coarse GGV ledger is insufficient for arbitrary
polynomial controls with that ledger.

Nothing here proves insufficiency inside the Keller subclass, a general
packet-to-tree functor, `G2-PSC`, a source/landing theorem, a topological
degree ceiling, or JC2.
