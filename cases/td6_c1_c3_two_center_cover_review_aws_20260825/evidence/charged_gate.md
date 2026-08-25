# TD6 two-center cover gate — exact fixed-family kill

## Verdict

**PASS, fixed scope.**  For the frozen source-typed TD6 construction, the
normalized two-center section

```text
(c1,c2,c3)=(C,1,U)
```

has no solution through the first-band/P12 gate.  The proof is an exact open
cover with raw rebuilds on every exceptional stratum.  It is not an SP-2
kill, a full-centering theorem, a neighbourhood theorem, or a JC2 result.

The portable freeze is
`cases/td6_c1_c3_two_center_cover_20260824/`.

## Exact cover

Let

```text
H=C-3U^2,
B=4C^2U^2+24CU^4-4CU+20U^6-20U^3+1,
T=4C^2U^2+28CU^4-4CU+24U^6-24U^3+1.
```

The ascending certificate is valid off `UHB`; the B-local certificate is
valid off `UHT`.  Both reduce genuine P12 to `-k/50` and lift to the original
28 first-band rows.  Since

```text
Res_C(B,T)=64U^10,   B(C,0)=1,
```

their union covers all points off `UH=0`.

On `U=0`, an exact first-band left-null witness kills the open `C != 0`; the
raw `(C,U)=(0,0)` rebuild has the same unit residual with no chart factor.
Thus the entire U-divisor is empty before P12.

On `H=0`, a raw source certificate reduces P12 to `-k/50` off

```text
U P(U)=0,  P(U)=128U^6-32U^3+1=B(3U^2,U).
```

The U-root is already covered.  The remaining `P=0` fibre was rebuilt from
raw transport over the exact field `Q[U]/(P)`.  The V7 producer proves `P`
irreducible and squarefree, obtains transport rank 3470/3602 and first rank
38/132, and reduces the 2885-term raw P12 to the same constant `-k/50`.
The constant has an exact inverse in the full base extension; the relation
lifts through 28 original rows/1540 slots and passes a perturbation negative
control.  Hence `H=P=0` is empty too.

The failed V6 localized attempt is retained deliberately: its relation
denominator has factor `P`, so it cannot license the finite fibre.  This is
why the independent V7 quotient rebuild is logically necessary.

## Evidence custody

The case freeze contains the complete V4–V7 source archives, their recursive
source manifests, AWS metadata, stdout/stderr, a top-level manifest, and
deterministic replay commands.  Principal output hashes are:

```text
generic       08a4320433c765fbfc101cd2a6c49e7af7f0aa73ff81e84237f3a31dd15f343c
B-local       2532ff680b358201ac4e50e15b8fb86a9d1c38a7a29b589fe3b1c7dac41e00e4
H-zero        68d3a56bcd1fb2f5b0467896cec8995407c22fadd340d2e4aab4f0dfc3116c9e
U-zero        0943cc4235a7b3280c841f402e68c670f16b8597ca01a67f59b85e6154e541a6
intersection  91f2940154d8bcdbbcefaa5e3c9a2af02d555334cda9cc5cf0a83c795e4dcc78
raw quotient  b4c9eb15f50fc45479609c7bd3d71516239ee54994cae46fdbff7348d52d6bcf
```

## Successor

The smallest licensed successor is the next independent, source-typed
centering coefficient beyond this normalized two-center section, or the first
matrix-changing dead-stretch/boundary modulus if source provenance shows that
the third center direction is gauge or dependency-incomplete.  Producer work
should continue provisionally while this package undergoes hostile review.
