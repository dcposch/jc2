# Follow-up hostile review: GGV `8_28` prototype R1 repairs

**Reviewer:** Grok 4.6 (independent hostile referee). **Date:** 2026-08-27.  
**Scope:** only the two repairs requested in the original hostile review
(SHA-256 `971147c5c8a6d3f26c103b0a2da1095ca7c302a2cfd1e812556eaddf6d21a316`).
Not a re-proof of the pair, charts, Q-data, mutation, or sheet/pole arithmetic.

**Overall verdict:** **PASS**

| Repair | Verdict |
|---|---|
| Custody wrapper (`verify_r1.py`) | **CONFIRMED** |
| Packet-scope correction | **CONFIRMED** |

No item is **REFUTED**. No remaining **GAP/REPAIR** on the two charged items.
Producer `PASS` tokens were not used as evidence. Producer, freeze, canonical,
and `jc2-lean` files were not edited. No AWS, no CAS.

**Firewall.** This example is non-Keller. It cannot prove a GGV-to-tree functor,
global source/landing coverage, `G2-PSC`, `G2-BD`, a cofinal ceiling, Gate T,
order two, maximum twelve, JC2, or a counterexample. It supplies no V43-to-K00
ring map. A non-Keller control is not upgraded to a Keller-domain
counterexample below.

---

## Independent hashes

Recomputed SHA-256, all matching the assignment where a pin was supplied:

```text
971147c5c8a6d3f26c103b0a2da1095ca7c302a2cfd1e812556eaddf6d21a316
  xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-hostile-review-grok-20260827.md
5c3d5005d5adaa0ab27cd507dea3a6d55affd78499cddf4ceeac999a77efafd4
  xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-r1-adjudication-sol-20260827.md
7c1205ff3247e06c31729c22a65c39b1e5bf3bd99e28d5fe6a7780ab3ac315b5
  cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify_r1.py
c456cffd52d836ada364b585fc1cc361bc0a07f6efa5d3718e6e41e45ac19edb
  cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/CUSTODY_R1.md
deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd
  cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/RESULT.json
9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c
  ladder/TRANSPORT.md
```

The adjudication path was not pre-pinned; the digest above is the independent
hash of the file as reviewed.

Frozen R0 bytes, recomputed against the original freeze and still identical:

```text
4dfe7c6dc1e873892f9128ac2712f319a8c85ffb051701ddafa442d779e11f28  verify.py
deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd  RESULT.json
f5d8e4efd33064dc23dbef3e7b7ad2bd1285631d095922ff6e2894e50863af0a  README.md
676bdd3ce960221072f037e7160d457a9d1d64c8e7353891f69e9931ae71149b  FREEZE.sha256
7647f2f118d4fe9fdd060b9e3e9450b58a62e287a80e942cad6de752a3f34ae8  sol report
```

The five remaining live source pins still match the R0 table. `HEAD` is
still `418e413593120d19e15e6546eb50c985f4b1f038`. `HEAD:ladder/TRANSPORT.md`
is still `39a607c8935153c814cd51fb65a2f1c708a9e4ba5e1dd0f38f9c96401fc4a624`.
The working tree of `ladder/TRANSPORT.md` is the already-reviewed 45-line
errata fold (28 insertions, 17 deletions): machine gate demoted to a
fixture, “repairs G2” rewritten as the T2-to-T4 normalization fork. That
file is hashed, not parsed, by the prototype.

---

## 1. Custody repair — CONFIRMED

`verify_r1.py` is a custody-only wrapper. Independently:

1. It pins the exact R0 verifier by SHA-256
   `4dfe7c6dc1e873892f9128ac2712f319a8c85ffb051701ddafa442d779e11f28`
   and refuses to load any other `verify.py`.
2. It copies `SOURCE_PINS` and changes **only** the `ladder/TRANSPORT.md`
   digest, from the frozen
   `39a607c8935153c814cd51fb65a2f1c708a9e4ba5e1dd0f38f9c96401fc4a624`
   to the live
   `9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c`.
   The other five pins are asserted equal to the freeze.
3. It `exec_module`s the frozen verifier and calls that module’s `main()`.
   That is the complete original mathematics: live `8_28` import, sparse
   pair, both chart identities, deck orbits, Q/jump/max, cyclotomic gcds,
   next coefficient, and sheet/pole totals. The wrapper does not reimplement
   or skip any of those checks. The original `__main__` block is not
   executed, so the frozen `RESULT.json` is not used as the computed object.
4. After `source_pins` is popped from both sides, it requires Python-object
   equality of every remaining field with frozen `RESULT.json`. That is
   exact comparison of the eight mathematical top-level keys
   `status`, `scope`, `non_keller_witness`, `ggv`, `x_infinity`,
   `y_infinity`, `totals`, `fidelity_mutation` (75 leaves). The live
   TRANSPORT pin must be the R1 digest; the frozen TRANSPORT pin must remain
   the R0 digest.

Unmodified run from the repository root, `python3 -B`, Python 3.14.6,
stdlib only, exit 0:

```text
{
  "frozen_result_sha256": "deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd",
  "mathematical_result_unchanged": true,
  "original_verifier_sha256": "4dfe7c6dc1e873892f9128ac2712f319a8c85ffb051701ddafa442d779e11f28",
  "scope": "custody-only TRANSPORT.md errata-fold replay",
  "status": "PASS",
  "transport_r1_sha256": "9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c"
}
```

A second, independent load of frozen `verify.py` with the same one-key pin
patch reproduced the same 75-leaf object, with empty missing/extra/mismatch
sets and no type mismatch. Three live mutations of the frozen copy
(`baseline_g_pole_mass` 276→277, `next_coefficient` `7/4`→`21/8`, x-chart
`(z-1)^14`→`(z-1)^15`) are detected as inequality. Unpatched
`verify.py` still fail-closes on `assert observed_pins == SOURCE_PINS`
(exit 1) before importing `8_28`. Restoring the R0 TRANSPORT pin in the
loaded module likewise fail-closes against the live file.

**No frozen R0 byte was rewritten.** The five freeze artifacts keep the
hashes recorded in the original review. `verify_r1.py` does not write
`RESULT.json`, `verify.py`, `README.md`, `FREEZE.sha256`, or the sol
report. `RESULT.json` still hashes to `deb3a630...` after both replays.
The producer heading in §6 is still `Minimal sufficient typed packet`;
the correction is additive, which is the licensed repair style under a
freeze.

Non-blocking wording: `CUSTODY_R1.md` says the returned object equals
frozen `RESULT.json` “exactly.” The load-bearing wrapper is stricter and
correct: equality holds after separating the contextual `source_pins`
field. That abbreviation is not a mathematical drift and is not charged
as a remaining gap.

The original smallest failing hypothesis,
`sha256(ladder/TRANSPORT.md) = 39a607c8...`, is therefore repaired without
touching the freeze: the R1 wrapper pins the live errata-fold digest and
replays the unchanged mathematics.

---

## 2. Packet-scope repair — CONFIRMED

The additive note withdraws the producer heading at the word **minimal**.
It does not relabel the frozen file, and it does not re-assert minimality
elsewhere.

Collision-forced by `τ=1→2`, and only these:

- the paired `y`-chart residual `X^8+1+τ X` modulo `X^{16}-1`;
- its roots and cancellation multiplicities;
- the resulting pole-order vector `{12^{×16}}` versus `{12^{×15},11^{×1}}`;
- provenance of the source monomial `x y^{15}` carrying `τ`.

Example-supported, sufficient for this packet, not collision-necessary:

- fibre tag `a`;
- both chart maps;
- `x`-chart residuals;
- deck/place grouping;
- Q/jump/max data;
- the displayed partial provenance of `τ` and `γ`.

A total inverse/source provenance map is marked as a proposed compiler
interface, not a theorem from this example. The eight listed fields remain
one sufficient packet for this example; the collision does not prove every
field necessary. That is exactly the repair demanded in original §8.

Non-Keller / Keller split is kept: the pair remains a non-Keller control,
and ledger-insufficiency is licensed only for arbitrary polynomial
controls with this GGV record, not inside the Keller subclass. `G2-PSC` is
refused in the R1 licensed paragraph and in the frozen `scope` string
`not G2-PSC`, which the custody replay compared exactly.

---

## Replay record (independent, not the producer `PASS`)

- Assignment hashes: 5/5 pinned inputs match; adjudication independently
  hashed as `5c3d5005...`.
- Frozen R0: 5/5 SHA-256 unchanged from the original review.
- Live pins: 5/6 match the freeze; `ladder/TRANSPORT.md` is the reviewed
  errata fold `9750aa9d...`.
- Original verifier: exit 1 on the pin assert (fail-closed).
- `verify_r1.py`: exit 0, `status=PASS`,
  `mathematical_result_unchanged=true`.
- Independent second exec of frozen `verify.py` with only the TRANSPORT pin
  changed: 75/75 mathematical leaves equal frozen `RESULT.json`.
- Sensitivity: pole mass, next coefficient, and x-chart identity mutations
  all break equality.
- No R0 write; no `__pycache__` under the prototype tree.

---

## Smallest licensed result

One explicit **non-Keller** pair realizes the complete live one-edge
`8_28` GGV record. Both infinity charts, sheet count 72, Q/jump/max
`1 → 4 → 28`, and pole mass 276 are exact. Changing `τ` from 1 to 2
preserves the current GGV ledger but drops one `y`-chart pole from 12 to
11 and the mass from 276 to 275. The present coarse GGV ledger is
therefore insufficient for arbitrary polynomial controls with that
ledger.

The `τ=1→2` collision forces only the `y`-residual, its roots and
cancellation multiplicities, the pole-order vector, and the provenance of
`x y^{15}`. The other listed packet fields are sufficient or
example-supported, not collision-necessary, and are not a minimal typed
packet.

Nothing here proves insufficiency inside the Keller subclass, a general
packet-to-tree functor, `G2-PSC`, a source/landing theorem, a topological
degree ceiling, or JC2.

**Smallest failing hypothesis on the two charged repairs:** none.
