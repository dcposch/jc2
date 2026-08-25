# TD6 `(c1,c2,c3)=(C,1,U)` exact two-center cover

Frozen status: exact, dependency-complete kill of this fixed source-typed TD6
two-center family.  This is not a neighbourhood theorem, an SP-2 kill, or a
resolution of JC2.

## Statement

Retain the frozen TD6 source, boundary data, pole data, normalization, and
transport typing, and vary only the normalized center block

```text
(c1,c2,c3) = (C,1,U).
```

There is no member of this two-parameter family satisfying the first-band and
P12 conditions.  The proof is an exact open cover of the `(C,U)` plane, with
every exceptional divisor rebuilt from raw source rows.

Put

```text
H = C - 3 U^2
B = 4 C^2 U^2 + 24 C U^4 - 4 C U + 20 U^6 - 20 U^3 + 1
T = 4 C^2 U^2 + 28 C U^4 - 4 C U + 24 U^6 - 24 U^3 + 1
P = B(3U^2,U) = 128 U^6 - 32 U^3 + 1.
```

The exact cover is:

1. The ascending generic source certificate gives `P12=-k/50` off `U H B=0`.
   Its multiplier denominator is `(1/4) B U^2 H^2`; its conservative
   termwise denominator is `(1/4) B U^3 H^3`; it uses 28 original rows and
   1489 relation slots.
2. The B-local source certificate gives the same obstruction off `U H T=0`.
   Its multiplier denominator is `(1/4) U^2 T`; its conservative termwise
   denominator is `(1/4) U^3 H T`; it uses 28 original rows and 1564 slots.
   The exact identities `Res_C(B,T)=64 U^10` and `B(C,0)=1` show that these
   two certificates cover every point off `U H=0`.
3. On `U=0`, the raw first band is inconsistent over `Q(C)` off `C=0`.  The
   exact witness is original row 13, key `('X-2',14)`, with unit residual;
   the complete conservative chart is `C^3`.  At `C=0`, a separate raw
   rebuild gives the same unit residual with chart 1.  Thus all of `U=0` is
   empty before P12.
4. On `H=0`, the raw specialized source certificate gives `P12=-k/50` off
   `U P=0`, using 28 original rows and 1515 slots.  The case `U=0` is already
   covered by item 3.
5. The remaining finite stratum `H=P=0` is rebuilt over the exact quotient
   `Q[U]/(P)`, not obtained by specializing a localized echelon.  The producer
   certifies that `P` is irreducible and squarefree, rebuilds transport at
   rank 3470/3602 and the first band at rank 38/132, and reduces the genuine
   2885-term P12 to the same constant `-k/50`.  It explicitly inverts that
   constant, lifts through 28 original rows/1540 slots, and passes a source
   negative control.  Therefore the final finite stratum is empty as well.

The V6 sparse-H experiment is retained as a negative control: it fails its
intentional coverage assertion because both its multiplier and termwise
denominators contain `P`.  It is evidence that the V7 raw quotient rebuild is
necessary; V6 itself is not a proof step.

## Charged evidence

All exact producer closures are frozen under `archives/`, including their own
`SOURCE.sha256` and runbook.  AWS outputs and launch metadata are frozen under
`evidence/`.

```text
V4 archive  4bb6352397a8f608345e11560687d9c8ef444e3f009f8b5cc4ba05c08674755e
V5 archive  c7be01534de522c5404dfe92d857d3b1af580ab680debe462f51fda7a7f6ba2a
V6 archive  db865fa52582e5a62dda912c7334b84536843b09392587f46e20ab748780cd1f
V7 archive  02985c91fe3e0fda5caa7a2e13f723993a89cd12574b760510c03c1689189aef

generic stdout       08a4320433c765fbfc101cd2a6c49e7af7f0aa73ff81e84237f3a31dd15f343c
B-local stdout       2532ff680b358201ac4e50e15b8fb86a9d1c38a7a29b589fe3b1c7dac41e00e4
H-zero stdout        68d3a56bcd1fb2f5b0467896cec8995407c22fadd340d2e4aab4f0dfc3116c9e
U-zero V5 stdout     0943cc4235a7b3280c841f402e68c670f16b8597ca01a67f59b85e6154e541a6
intersection stdout  91f2940154d8bcdbbcefaa5e3c9a2af02d555334cda9cc5cf0a83c795e4dcc78
V6 negative stdout   80fab173e260155e3b0d0208500019b54d6fe49405790db8fe4ad1dd13c39f4e
V7 quotient stdout   b4c9eb15f50fc45479609c7bd3d71516239ee54994cae46fdbff7348d52d6bcf
```

Every successful run has empty stderr.  V6 has the expected assertion
traceback and stderr SHA256
`4b253d4f3afc18c33a6b6e05ce6a6e033ecc164625fde506e3636bd30b5d4571`.

## Deterministic replay

Extract each charged archive into a separate temporary directory, verify its
`SOURCE.sha256`, and run with Python 3 plus `python-flint` 0.9.0 or compatible.
The theorem-producing commands are:

```sh
# V4: run from its extracted root
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py --b-local-pivots
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py --stratum=h-zero

# V5: run from its extracted root
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py --stratum=u-zero
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py --stratum=intersection

# V7: run from its extracted root
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/h_b_raw_quotient.py
```

The optional V6 command is expected to exit nonzero precisely when it detects
the nonunit gcd `P`:

```sh
python3 jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py \
  --stratum=h-zero --sparse-pivots
```

## Scope quarantine

This cover holds only for the fixed licensed TD6 source and the normalized
two-center section `(C,1,U)`.  It does not cover a third independent centering
modulus, boundary/dead-stretch moduli, a neighbourhood in the full TD6 source
space, all SP-2 cases, or JC2.
