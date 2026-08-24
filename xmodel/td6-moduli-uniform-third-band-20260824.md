# TD6-MODULI-UNIFORM-THIRD-BAND — normalized family eliminated

Date: 2026-08-24  
Charged clean basis: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`  
Status: **PROVISIONAL PRODUCER / EXACT NORMALIZED-FAMILY KILL / STOP**

## Verdict

The moduli-zero curve left by the preceding gate does not survive the next
centered Jacobian band.  Under the fixed normalized boundary-pattern control
specified below, the row `[s^0t^0]J=1` first cuts the one-dimensional curve to
six source-typed complex points.  The remaining coefficients of the same
centered band are then inconsistent at every one of those points.  An exact
left-syzygy gives a nonzero residue already at degree `t^4`.

Thus the verdict is

```text
NORMALIZED-BOUNDARY-FAMILY-EMPTY-AT-CENTERED-BAND
```

The quadratic next pole row is not used.  This eliminates one fixed
normalized reduced-boundary family, not SP-2, a terminal class, or JC2.

## 1. Exact hypotheses

The calculation retains:

- global rectangles `f:(15,60)`, `g:(25,100)` over characteristic zero;
- common centered chart
  \[
  y=s^{-1},\qquad x=s+s^2+s^3+t s^4;
  \]
- x-boundary values
  \[
  [s^0]f=t^{15},\qquad [s^0]g=t+t^{25};
  \]
- zero r9 dead stretch;
- normalized reduced F1 polynomial
  \[
  R(z)=(z-1)^2(z^2-Sz+D),
  \]
  with leading values `R(eta^5)^3,R(eta^5)^5`;
- the source relation and r9 pole normalization
  \[
  H=1-S+D,\qquad L=25H,\qquad L^8A^3=9;
  \]
- every first-band transport equation, `[s^-2]J=0`, the complete previous
  centered row `[s^-1]J=0`, and, where noted, the inherited affine pole row
  `[r^1](J-1)=0`.

The preceding exact obstruction restricts the symmetric moduli to

\[
 Q=-2S^2+2S+5D-3=0,
 \qquad D={2S^2-2S+3\over5}.                         \tag{1}
\]

The transport matrix has `6547` rows and rank `3508/3602`, leaving `94`
affine parameters.  The previous centered row has rank `36/94`; its unique
symbolic compatibility condition is a nonzero rational multiple of `Q`.
Consequently (1) leaves an exact `58`-dimensional affine family before the
inherited pole row.  The pole row is consistent and adds rank two, recovering
the prior `56`-dimensional paired survivor.

## 2. First coefficient of the new centered band

Write

\[
\begin{aligned}
F&=p+s f_1+s^2f_2+s^3f_3+\cdots,\\
G&=q+s g_1+s^2g_2+s^3g_3+\cdots,
\end{aligned}
\]

where `p=t^15` and `q=t+t^25`.  Exact propagation of the symbolic F1/r9
right-hand sides through the shared transport gives

\[
 f_{2,1}=0,\qquad f_{3,0}=H^3.
\]

Both quantities have zero coefficient on all 58 free parameters.  Therefore
the constant term of

\[
\begin{aligned}
[s^0]J={}&f_1g_2'+2f_2g_1'+3f_3q'\\
          &-3p'g_3-2f_1'g_2-f_2'g_1
\end{aligned}
\]

is

\[
 \boxed{[s^0t^0]J-1=3(1-S+D)^3-1.}                 \tag{2}
\]

After substituting (1), equation (2) is `F(S)/125`, where

\[
\boxed{
\begin{aligned}
F(S)={}&24S^6-252S^5+1170S^4-3045S^3\\
      &+4680S^2-4032S+1411.
\end{aligned}}
\tag{3}
\]

The replay proves (3) by exact polynomial substitution, not interpolation.
Rabin's criterion modulo `31` proves that `F` is irreducible over `Q`; hence
it is also squarefree.  Thus (2) leaves exactly six distinct complex values
of `S`, not a positive-dimensional locus.

No source exclusion removes these values.  Exact Euclidean gcds with `F`
are `1` for the divisors controlling `D=0`, `U=V`, `U=1` or `V=1`, `S+2=0`,
and `H=0`.  Since `L=25H` and `A^3=9/L^8`, both pole parameters are nonzero.
This is the requested saturation of the normalized source-open curve.

## 3. Exact residue field and the full centered band

Let

\[
 K=\mathbb Q[S]/(F),\qquad
 D={2S^2-2S+3\over5},\qquad H={2S^2-7S+8\over5}.
\]

Equation (3) is equivalent to `3H^3=1`.  Put

\[
 \alpha={9\over(25H)^8}={243H\over25^8},\qquad
 E=K[A]/(A^3-\alpha).                               \tag{4}
\]

This is genuinely a degree-18 field over `Q`.  The replay computes by an
exact `6 x 6` multiplication determinant

\[
 N_{K/\mathbb Q}(\alpha)={3^{28}\over5^{96}}.
\]

Its 3-adic valuation is not divisible by three, so `alpha` cannot be a cube
in `K`.  The cubic in (4) is therefore irreducible.  The basis
`1,A,A^2` is exact; no numerical embedding or branch choice is involved.

All forty coefficients of `[s^0]J-1` are compiled over `E`.  There are `35`
nonzero affine rows and the homogeneous matrix has rank `25/58`.  Exact
echelon reduction produces a left-null combination whose first contradiction
appears at the input row `t^4`.  Its right-hand side is

\[
\boxed{
\begin{aligned}
\rho={}&{1\over3625}(2495634-4154976S+4405068S^2\\
 &-2488119S^3+761922S^4-105084S^5)
 +{136875\over29}A.
\end{aligned}}
\tag{5}
\]

The replay retains the complete left-syzygy, verifies directly against the
unreduced coefficient matrix that its variable side is zero, and reproduces
(5) on its constant side.  Since the coefficient of `A` is nonzero and
`1,A,A^2` is a `K`-basis of `E`, `rho != 0`.  Every embedding of `E` sends a
nonzero element to a nonzero element, so the contradiction holds at all
`6 x 3 = 18` pole-normalized conjugate points above (3).

The inherited pole row was separately evaluated over `E` and remains
consistent of rank two.  It is unnecessary for the contradiction: the new
centered band is already inconsistent in the larger 58-dimensional family.
The nonlinear row `[r^2](J-1)=0` was therefore not compiled or used.

## 4. Provenance, stop, and next implication

The deterministic replay imports only the frozen moduli-uniformity compiler,
checks its hash, rebuilds the shared transport, derives (2)--(3), proves both
field irreducibility statements, saturates the source exclusions, and verifies
the full left-syzygy over exact arithmetic.

Run:

```text
python3 cases/td6_moduli_uniform_third_band_20260824/replay.py
```

| artifact | SHA-256 |
|---|---|
| replay | `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8` |
| canonical stdout | `c5c3417f3ba32574a778126de4cbc2bab5ee1f4528a17d3f86b106b68cbbd2ea` |
| compiled centered equations | `afcc6e2d51be0bc3d66f18afc030ba974aebc7c872732d04941bc4a319dd37a9` |
| exact left-syzygy | `6fffd7e470665e2af6f66a6f5b5dad1ddc066389bc4bdd8af8d4bdc845964aee` |
| formula payload | `cf1a56c1d31a27ee06071d216aea8dd648ab6754e1888ea2fe4050163a2e2047` |
| imported replay | `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab` |
| imported report | `499e95763759fe195ab1eba5fbf97bfb9d255bbf6fb2b090add938d92f1f3a06` |
| imported freeze manifest | `8d28ce7bc0ca31b51887457e9f5e33537f0ec86d950a6e0e21c78813a78994af` |

No modular sampling, floating point, AWS, broader degree rectangle, quadratic
pole solve, or protected process was used.

**Smallest missing implication.**  This family fixed `p=t^15`,
`q=t+t^25`, center `(1,1,1)`, zero dead stretch, and one reduced F1 boundary
pattern.  The next licensed gate is to identify the smallest additional
boundary/dead-stretch coefficient that can enter (2) or the syzygy (5), and
repeat the exact elimination with only that bounded deformation.

**JC2 scope.**  The result proves emptiness only for the normalized family
listed in section 1.  It does not eliminate all SP-2 data, any of the eight
terminal classes, or either side of JC2.  No top-level canonical file was
edited.
