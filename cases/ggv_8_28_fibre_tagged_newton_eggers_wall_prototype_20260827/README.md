# GGV `8_28` paired fibre-tree prototype

This desk-scale exact control realizes the reviewed nontrivial `8_28` GGV
MN chain by a concrete polynomial pair, expands the two fibres `f=0,1` in
both infinity charts, and attaches residual, deck, sheet, pole, and Sigray
Q/jump/max data.  It also changes one coefficient that is invisible to the
current GGV ledger and detects the resulting one-unit pole-order change.

It is deliberately **not** a Keller pair and proves neither a GGV-to-tree
functor nor G2-PSC.  The exact non-Keller witness is part of the replay.

Run from the repository root:

```text
python3 cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify.py
```

The verifier uses only the standard library, checks all six source-file
hashes before importing the live `8_28` record, and requires its recomputed
object to equal `RESULT.json` exactly.

