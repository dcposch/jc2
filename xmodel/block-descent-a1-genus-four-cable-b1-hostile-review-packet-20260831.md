# Hostile-review packet: conductor-eight genus-four Betti obstruction

Date: 2026-08-31 UTC  
Coordinator basis: `59f25428`  
Purpose: independent different-model audit; no downstream promotion is implied.

## Charged files

Reproduce every SHA-256 before reading the corresponding file.

```text
070faa884a26b0c96aaacafa7738cb39746407803d156a5a327d360eabf613e5
  xmodel/block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md
c79b7197d9c84e8a9a161cf153430849ad730b35d950a51afc32d1cd73ffa707
  ops/block_descent_a1_genus_four_cable_b1_replay.py
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa
  xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md
03b16c2deba48605482963ae7f98f5e74aca26ce0e1761bbeab653a164bec4b4
  xmodel/block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
be4c287fe56c067208496f39a7388c56592c562a93fe46665e693958ad972a3a
  xmodel/post-ledger-dependency-hash-corrigendum-sol56-20260831.md
```

If any hash differs, return `CUSTODY_FAIL` without using that file. Do not
inspect any sibling review/report, model log, run receipt, mutable lane output,
or excluded workspace.

## Claimed theorem to audit

At the exact charged scope—reduced irreducible complex affine plane curve,
normalization `A1`, one place at infinity, `Delta_aff=4`, `b1=1`, and a
transitive meridional-transposition representation to `S4`—the producer
claims that no curve exists. It enumerates exactly four conductor-eight
delta-sequences, removes three by full-`S4` coloring, and normalizes the sole
survivor `(9,6,2)` to

```text
U=t^6+8t^2,
V=t^9+12t^5+24t,
V^2-U^3-64U=64t^2.
```

Four disjoint normalization pairs would then force `b1>=4`.

## Mandatory hostile checks

1. Re-derive the complete genus-four prime iterated-knot list and the
   conductor-eight delta-sequence list from the stated conductor, freeness,
   primitivity, and height conditions. Look for omitted length, winding-one,
   sign, mirror, coordinate-order, or semigroup cases.
2. Independently check the braid convention and the labelled full-`S4` and
   Fox-3 counts, including all sign/chirality variants. State precisely which
   boundary-to-affine and meridian interfaces are consumed.
3. Treat producer section 5 as the highest-risk bridge. Determine whether the
   approximate-root theorem really licenses the exact Weierstrass form and
   `deg_t H=2`; whether all lower weighted monomials can be removed by legal
   target automorphisms; whether `U=Z^2+R`, the polynomial part `W`, and
   `V=W` are exhaustive; and whether the coefficient comparison omits any
   family or cancellation. Check the `a=0` cases and the scaling to `a=8`.
4. Verify birationality and the normalization-pair argument, including the
   possibility that several pairs share an image or that a fibre contains
   additional points. Check the exact implication for `b1` versus
   `Delta_aff`.
5. Run the replay under ordinary Python, `-O`, and `-OO`; compare stdout
   hashes; run all three mutations and require nonzero exit. Explain what the
   replay does not prove.
6. Audit scope. Do not infer rank-four emptiness, JC2, a result for reducible
   branches, or genus at least five.

## Required report

Return one leading verdict: `CONFIRM`, `CONFIRM_WITH_CORRECTIONS`, `OPEN_GAP`,
or `REFUTE`. Separate exact theorem, computational checks, primary-source
interfaces, and remaining assumptions. Give the maximum safe statement and
its blast radius. If a gap is repairable, give the cleanest exact repair; if
not, identify the first invalid implication. End with a standalone
`<!-- BODY-END -->` line and add no seal.
