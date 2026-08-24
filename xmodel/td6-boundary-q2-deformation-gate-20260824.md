# TD6-BOUNDARY-Q2-DEFORMATION — two scoped points remain empty

Date: 2026-08-24  
Charged clean basis: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`  
Status: **PROVISIONAL PRODUCER / TWO EXACT EMPTY SPECIALIZATIONS / STOP**

## Verdict

The first bounded widening of the frozen x-boundary was

\[
 p(t)=t^{15},\qquad q_B(t)=t+B t^2+t^{25}.           \tag{1}
\]

This is the lowest-degree deformation that keeps the displayed degree data,
`q_B(0)=0`, and `q_B'(0)=1`; `p=t^15` retains the normalized single x-cluster.
The prior hostile review explicitly classified `t^15 / (t+t^25)` as a
selected monomial boundary inside broader degree-15/25 data, not as a
terminal-forced normal form.  The calculation here is nevertheless only a
bounded compiler control: it does not claim that (1) by itself realizes every
global SP-2 source condition.

Two exact values of `B` were tested through the full next centered band:

1. `B=1`;
2. an exact degree-18 algebraic value chosen to cancel the affine secant of
   the old and `B=1` degree-four residues.

Both are empty at `[s^0t^4]J`.  Therefore the first visible `B`-sensitivity
does not immediately produce a finite-band survivor.  This does **not** prove
emptiness for arbitrary `B`; the full one-parameter boundary family remains
open.

## 1. Retained source and global data

Both tests keep the fixed rectangles `(15,60)/(25,100)`, common center
`(1,1,1)`, zero dead stretch, reduced F1 pattern

\[
 R(z)=(z-1)^2(z^2-Sz+D),
\]

and r9 source relation

\[
 D={2S^2-2S+3\over5},\quad
 H=1-S+D,\quad L=25H,\quad L^8A^3=9.              \tag{2}
\]

The centered constant row from the preceding frozen gate remains zero only
on

\[
 F(S)=24S^6-252S^5+1170S^4-3045S^3
       +4680S^2-4032S+1411=0.                     \tag{3}
\]

The exact coefficient field is

\[
 K=\mathbb Q[S]/(F),\qquad
 E=K[A]/(A^3-9/L^8),                               \tag{4}
\]

of degree 18 over `Q`, with the irreducibility proof imported byte-for-byte
from the frozen uniform third-band replay.  Thus `1,A,A^2` is a `K`-basis.

For (1), the first centered Jacobian row is correctly recompiled as

\[
 f_1(1+2Bt+25t^{24})-15t^{14}g_1=0.               \tag{5}
\]

All later centered formulae use the same derivative
`q_B'=1+2Bt+25t^24`; no `B=0` matrix is silently reused.

## 2. Exact `B=1` result

At `B=1`, exact transport plus (5) has the same total rank as before,
`3508/3602`, and leaves 94 affine parameters.  The complete previous
centered row has rank `36/94` on (2)--(4), leaving dimension 58.

The new centered band has tangent rank `25/58` and is inconsistent at its
degree-four row.  Its exact residue is

\[
\begin{aligned}
\rho_1={}&{1\over3625}(2145334-4154976S+4405068S^2\\
 &-2488119S^3+761922S^4-105084S^5)
 +{136875\over29}A.                                \tag{6}
\end{aligned}
\]

The frozen `B=0` residue was the same expression with constant numerator
`2495634`.  Hence the exact observed change is

\[
 \rho_1-\rho_0=-{350300\over3625}=-{14012\over145}.\tag{7}
\]

This proves that the degree-four obstruction is `B`-sensitive; it is not an
invariant copied unchanged from the monomial boundary.  It does not prove
that the full reduced residue is affine in `B`, because the preceding affine
solution space and its echelon pivots also vary with `B`.

## 3. Exact adaptive candidate

The smallest fail-fast candidate suggested by (7) is

\[
 B_*={\rho_0\over 14012/145}\in E,                 \tag{8}
\]

which would kill `rho_0-(14012/145)B` if that secant extrapolation were the
true uniform residue.  Since (8) has no constant or linear-boundary
degeneracy, `q_{B_*}` still has degree 25, vanishes at zero, and has derivative
one there.

The adaptive replay does not assume the secant formula.  It rebuilds the
transport-only matrix, inserts (8) into every x-boundary and Jacobian
coefficient, and obtains:

| stage | exact result |
|---|---:|
| transport only | rank `3470/3602`, dimension `132` |
| first Jacobian band (5) | adds rank `38`, dimension `94` |
| previous centered + inherited pole bands | add rank `38`, dimension `56` |
| new centered homogeneous matrix | rank `25/56` |
| new centered affine system | **empty at input row `t^4`** |

The final residue has nonzero coefficients in all three independent basis
slots `1,A,A^2`.  It is therefore nonzero in `E`.  In particular, the simple
secant cancellation is false after the full `B`-dependent transport and
previous-band solve; (8) is not a survivor.

## 4. Exact conclusion and remaining gap

What is proved:

- the earlier degree-13 obstruction and degree-zero sextic cut persist at
  the tested low-degree deformation values;
- the later degree-four compatibility is genuinely `B`-sensitive;
- `B=1` and the exact adaptive value (8) are both impossible through the
  displayed centered band;
- the adaptive value passes the inherited opposite-side affine pole row
  before failing, so its death is not a one-sided omission.

What is not proved:

- no formula uniform in arbitrary `B` has yet been derived;
- rank-jump values of the full `B`-dependent linear systems have not been
  eliminated;
- nonzero dead-stretch coefficients, other q-boundary coefficients, general
  common centering, other F1 patterns, and the other terminal classes remain
  unquantified.

The next mathematically honest implication, when resumed, is a symbolic
one-parameter elimination in `B`, including every pivot/rank-jump locus.  A
few more samples or an affine extrapolation would not suffice.

## 5. Reproducibility and hashes

Exact replays:

```text
python3 cases/td6_boundary_q2_deformation_20260824/sextic_probe.py
python3 cases/td6_boundary_q2_deformation_20260824/adaptive_probe.py
```

| artifact | SHA-256 |
|---|---|
| bounded compiler helpers / rational `B=1` preflight | `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357` |
| exact sextic `B=1` replay | `8834cd9b365a9a20d058c3ef6b0ef927c6aee05c895b650b6bc2b927ed6250ca` |
| exact adaptive replay | `ca09d8dc6d154eec7a0fe39747c6ea348fc5e7cccd26bae7bdadae148cd51be5` |
| `B=1` canonical stdout | `68863a4c0deb4eb0d2745714612bfb8ea7b445dd7355833181cf5178241ef2bd` |
| `B=1` exact residue | `d091b65e4bc7c66a83946499ab037ceb3812bcedc4c5311bbda8276bfa213732` |
| adaptive canonical stdout | `b5cf24e87e84900f796affb8c78a63af805bb0c68c0fdab03d0ef99fa318aceb` |
| adaptive candidate `B_*` | `64010183890daa1938b4eac6add7933767238738e9783f41b5821dcc4b56d750` |
| adaptive exact residue | `be22c8d155c26a5091494d68c32e043cce66b4275330a022e493528659a4a53b` |
| imported uniform-third replay | `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8` |

No floating point, modular inference, AWS, degree widening, generic sparse
search, canonical edit, or protected process was used.

**JC2 scope.**  The verdict is two exact empty points of one smallest
q-boundary deformation inside one normalized SP-2 chart-pattern control.
The one-parameter `B` family is not killed.  SP-2, every terminal class, and
JC2 remain open.
