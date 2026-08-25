# Preregistered next top-carry discriminator

## Frozen input

The runner consumes only the frozen first-following-Cartier package:

```text
xmodel/as-fonly-d7-vertical-next-cartier-20260824.md
SHA-256 cfd77aacacf5c47c74e001c26cfb5369e69b7545bd1d301627135f06fd30af15

cases/as_fonly_d7_vertical_next_cartier_20260824/MANIFEST.sha256
SHA-256 0c0d88b80038ed266bc57431cde7d395ebe592497ccdd0e9830480d26a41551f
```

## Exact test

Enumerate all `1,085,103` visible current-digit solutions of the `20 x 17`
parent gate.  First require every coefficient of

```text
N12={C7,D7}.
```

For each survivor, solve

```text
N11={C7,D6}+{C6,D7}
```

as an affine-linear system in the six derivative-zero degree-six spectator
directions.  Record exact counts, rank/fibre histograms, and deterministic
stream hashes.

## Interpretation

- zero `N12` survivors is an exact obstruction for this charged vertical
  finite-depth branch;
- nonzero `N12` but zero `N11` survivors is the next exact obstruction;
- any `N11` survivor is only a top-row successor and must descend through
  degrees 10..7 and the next Cartier row;
- timeout/OOM/incomplete output is no verdict.

`F/3` and first-/next-digit cross terms have degree at most nine, so they
cannot enter degrees twelve or eleven.  Lower current digits cannot enter
either row.  No no-lift, all-depth, characteristic-zero, counterexample, or
JC2 inference is licensed.
