# Freeze registration — GCD3-69-LOWER-PFAFFIAN-SUCCESSOR-20260824

Frozen: 2026-08-24T14:14:45Z  
Charged bank: 1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a

## Chronology disclosure

Exploratory hand derivation and private scratch computations preceded this
file. This registration freezes the coherent successor claim, replay, case
split, and failure perimeter before the registered repo replay. It is not
represented as a blinded preregistration of the discoveries.

## Frozen input and license

The sole mathematical input package is the frozen first gate:

~~~text
f63bf74fd1013c74645f9f7fe9292db69199572b390b5b19d160c5ed13b373e8  xmodel/gcd3-69-common-cubic-first-gate-20260824.md
0ec1a7295cb9a3b090e1be2dfab1f730c12e2d8aeeec492c22932c9d720d3a94  cases/gcd3_69_common_cubic_first_gate_20260824/replay.py
ea4761f641e1778bbc3cfa9f7769a9129ab1a3ca0ddd6d8944431400645eb06a  cases/gcd3_69_common_cubic_first_gate_20260824/verify_constant_w_scheme.sing
65370031b04014f96efc3ac814477a6689d5d5fef6b2695066ba6d60658ee585  cases/gcd3_69_common_cubic_first_gate_20260824/FREEZE.sha256
~~~

That gate provisionally licenses only the aligned, nontrivial cubic-Kummer
branch, its five-moving-coefficient-plus-essential-kappa normal form, the
reviewed history condition 3 | deg(h), and its pure-DS valuation lemma. It
does not license the cube-core mismatch branch, a global filtered common
root, or a full (6,9) exclusion.

The Birch/Shioda Davenport--Stothers control is consumed only through the
exact polynomial identity replayed in the frozen predecessor and again in
this case. Primary-source metadata is recorded in Section 5.1 of that
report; no downloaded source is added here.

## Registered questions

1. Do the four zero lower rows z^4,...,z integrate exactly?
2. What is the complete reduced scheme cut out by the Kummer-compatible
   integration constants?
3. Does its terminal z^0 row equal j/s on either reduced component?
4. Are constant maps, chart denominators, ramified preimages, embedded
   components, component intersections, and every displayed determinant
   zero dispatched without matrix inversion?
5. Does the shifted DS constant alter the source bracket or the reviewed
   nontrivial-Kummer valuation obstruction?

## Frozen claim perimeter

Allowed positive conclusions are exact identities and a provisional
exclusion of the aligned nontrivial-Kummer (6,9) branch, conditional on the
frozen predecessor. A boundary equation is not consumed; in particular no
chosen-root equation is promoted to full-cubic divisibility.

The cube/mismatch branch, the aligned cube branch outside the predecessor's
nontrivial-Kummer high-row reduction, arbitrary (6,9), and JC2 remain open.
Any missing reduced component, denominator/rank stratum, or source-field
case fails the gate closed.

## Registered replay

Run without network:

~~~text
uv run --offline --no-project --with sympy==1.14.0 python \
  cases/gcd3_69_lower_pfaffian_successor_20260824/replay.py

Singular -q \
  cases/gcd3_69_lower_pfaffian_successor_20260824/verify_lower_invariants.sing
~~~

The Python replay must terminate with
PASS-GCD3-69-LOWER-PFAFFIAN-SUCCESSOR and explicit negative-scope markers.
The independent Singular replay must terminate with
PASS-GCD3-69-LOWER-INVARIANT-DECOMPOSITION, verify exactly two minimal
reduced components, and place the C=0 associated prime inside the
zero-bracket component.
