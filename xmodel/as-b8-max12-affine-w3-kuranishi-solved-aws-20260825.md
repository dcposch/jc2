# B8 fixed-D12: complete `W2` fibre and solved first quadratic `W3` gate

Status: **PRODUCER-EXACT / DUAL-AWS / HOSTILE REVIEW PENDING**.

## Result

For the B8 residue seed

```text
u=x+y^4,              P0=y+u^2,              Q0=u^3-u
```

retain every coefficient in the fixed degree-compatible envelope

```text
R: total degree <=12 and y-degree <=8       81 slots,
S: total degree <=12 and y-degree <=12      91 slots,
determinant rows through total degree 22    276 rows.
```

The complete first-digit equation over `F3` has rank 104.  Hence its `W2`
solution fibre is an affine `68`-space, not merely the previously frozen
RREF point.

The first genuinely nonlinear compatibility equation occurs at the next
digit.  On the complete affine parameterization

```text
T(t)=T0+sum_{i=0}^{67} t_i K_i,
```

it is the full cokernel-valued quadratic

```text
kappa(t)=pi((det J(F0+3T(t))-1)/9)=0.                 (1)
```

The source compiler constructs (1) independently by exact analytic
polarization and by determinant interpolation at `0,e_i,2e_i,e_i+e_j`.
The canonical ANFs agree exactly, at SHA-256

```text
9121d7cb4ee5aa5f38f31312077c084dc98fbc1b4175c73cef4a95dadaad45a4.
```

Before ideal reduction, the 172 cokernel coordinates have polynomial-span
rank 81, quadratic-coefficient rank 42, tangent rank 41 at the frozen point,
and 39 exact pure-linear consequences.  Solving those 39 rows leaves 29
coordinates `s0,...,s28`; exact substitution reduces the whole obstruction
ideal to

```text
I=(s22,
   s26+2*s22*s26,
   s22^2,
   s26^2+s19*s22,
   s22*s27).                                          (2)
```

Both direct `std` and independent `slimgb` replays prove

```text
I=(s22,s26).                                          (3)
```

Indeed `I` is visibly contained in `(s22,s26)`; conversely `s22` is the
first generator and
`s26=(s26+2*s22*s26)-2*s26*s22` lies in `I`.  Thus the first nonlinear
Kuranishi gate is solved scheme-theoretically: its compatible predecessor
locus is the reduced affine space `A^27_F3`, with exactly `3^27 =
7,625,597,484,987` `F3` points.

For every compatible predecessor point, the fresh 172-coordinate digit
equation again has rank 104 and kernel dimension 68.  RREF supplies a
polynomial section, so the complete fixed-D12 `W3` solution scheme is

```text
A^27 x A^68 = A^95 over F3.                           (4)
```

Equivalently, the truncation image in the prior `W2` fibre has dimension 27,
each fresh fibre has dimension 68, and there are `3^95` coefficient-digit
solutions modulo 27 above the fixed residue seed.

## Source-honesty and degree controls

The compiler pins the frozen B8 parent source SHA-256

```text
691c89fc78dbbdb053449e0c26df326a5b459ab8de28b333cbd5329f48168a13
```

and compares the transported formula with the direct determinant operator
on all 172 columns.  Kernel identities, left-cokernel projection, exact
coefficient divisions, and all 276 determinant positions are retained.
Unreduced integer lifts of the `F3` kernel parameters are used, so no
canonical-digit carry is hidden in (1).

The reduction producer tested the registered zero/weight-one/weight-two
routing set of 1,683 points; 1,459 passed.  This sample is not used for
completeness.  It reconstructed and replayed ten literal distinct solutions
through the integer determinant modulo 27.  Every emitted witness has
actual partial `y`-degrees `(8,12)`, actual total degrees `(8,12)`, and all
276 determinant rows zero.  Across the entire family, the partial degrees
remain exactly `(8,12)` because the seed's `y^8` and `y^12` coefficients are
3-adic units; the honest total-degree statement for the whole family is the
registered cap `<=12` in each coordinate, not that every member has first
total degree exactly eight.

## AWS custody

Case:
`cases/as_b8_max12_affine_kuranishi_aws_20260825/`.

The primary compiler ran on Box02 and Box03 in 9.42 and 9.00 seconds, with
maximum RSS 74,980 and 76,184 KiB.  Their result JSON is byte-identical at

```text
265c73641f8b0251525c4de052718a53b6738188b4088e00372712a8c637967b.
```

The independent reduction endpoints ran in 9.72 and 9.61 seconds, with
maximum RSS 76,024 and 76,204 KiB.  Their result JSON and reduced ANF are
byte-identical at

```text
da74d46dbbdc6530a7ef2179c2927b9859016fe49a24c6d089ad34b1a49a6ee0
b4a8c457a49143c0bf2b8eb4b30a95bd60ceacf3fdb458bdfa82bf24351cde2d.
```

The final ideal equality was replayed with Singular `std` on Box02 and
`slimgb` on Box03.  Their stdout SHA-256 values are respectively

```text
1fe763cd977673399ca9442298c8fc003636d6395c61974332dd3c319d276fc9
2fcb672163ea2eb248615d1b14e69862660492551b613e783f9f872cf219c12a.
```

The first verifier attempt is preserved as a negative control: it compared
zero ideals aggregate-wise in a way Singular does not support, printed FAIL,
then continued because `exit(91)` is undefined.  No V1 verifier output is
consumed.  V2 tests every generator separately and its shell runner rejects
any `FAIL` line.

## Scope firewall

This proves the complete fixed-D12 affine family only through `W3=Z/27` and
solves its first nonlinear transition.  It does not construct a compatible
inverse system, a `Z_3` or characteristic-zero Keller map, a nonautomorphism,
a selected-Q8/TD6 landing, a maximum-twelve theorem, or a JC2 conclusion.
The natural next digit is linear over each point of (4) but its carry varies
over all 95 parameters; it requires a separately preregistered full-family
gate, not continuation of one chosen witness.

