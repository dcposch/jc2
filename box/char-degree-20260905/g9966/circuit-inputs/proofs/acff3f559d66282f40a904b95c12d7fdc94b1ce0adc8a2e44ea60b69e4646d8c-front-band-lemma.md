# Front-band elimination from characteristic degree and the actual source rows

This is an exact preprocessing lemma, not an extra source gauge or a
specialization. The original characteristic and source rows remain in
the final ideal. All implications below hold pointwise over every
characteristic-zero extension field; extracting individual zero
coordinates is therefore radical consequence unless an explicit
linear graph elimination has already established ideal membership.

## Notation and hypotheses

Let h be the degree-k canonical outer root, k=33 or 36. Write the
outer physical polynomials as

\[
F=h^3+A_2h+A_3,\qquad G=h^2+B_1h+B_2.
\]

The characteristic family is
`Q=G^3-F^2+aG^2+bFG+cF+dG+e0`, with all five targets scalar.
Its degree upper rows force `B1=-b/3` and `A2=(3B2+a)/2` by the
audited proof in `source-audit.md`, section 6. Define the physical
depressed polynomials

\[
H=h-b/6,\quad v=B_2+a/3+b^2/18,
\]
\[
V=A_3-bB_2/4+ab/12+b^3/54-c/2.
\]

From the same exact identity and monic y-division,

\[
V=\frac12\operatorname{quo}_y(3v^2/4+p,H)
 =\frac38\operatorname{quo}_y(v^2,H),\tag{1}
\]

because p is scalar and has zero quotient on division by degree-k H.
Here only the necessary bound `deg_y Q<2k` is used. No variable
coefficient is inverted.

Normalize in the engine variables `t=1/x,z=ty-1`:

\[
\mathsf H=t^k H(t^{-1},(1+z)t^{-1}),\quad
\mathsf D=t^{2k-1}B_2(t^{-1},(1+z)t^{-1}),\quad
\mathsf C=t^{3k-1}A_3(t^{-1},(1+z)t^{-1}),
\]

and `mathsf v=mathsf D+(a/3+b^2/18)t^(2k-1)`.
The normalized version of (1) is exactly

\[
\mathsf C=\frac38 t\operatorname{quo}_z(\mathsf v^2,\mathsf H)
 +\frac b4t^k\mathsf D
 -(ab/12+b^3/54-c/2)t^{3k-1}.\tag{2}
\]

This shift by **one** in the quotient term comes from
`2(2k-1)-k=3k-2`, compared with C's normalization degree `3k-1`.
The polynomial mathsf H is monic in z, of degree k, with fixed
t-zero term

\[
H_0=z^{24}(1+z)^9\quad(k=33),\qquad
H_0=z^{28}(1+z)^8\quad(k=36).
\]

Let r be the first nonzero t-band of mathsf D, and denote its
coefficient by D_r(z). The scalar addition to mathsf v enters only
at t^(2k-1). Monic division is polynomial in the divisor's lower
coefficients, so when `r<2k-1`, the first potentially nonzero quotient
band is

\[
[t^{2r}]\operatorname{quo}_z(\mathsf v^2,\mathsf H)
  =\operatorname{quo}_z(D_r^2,H_0).\tag{3}
\]

If in addition `r<k-1`, the bD term of (2) starts at r+k>2r+1 and
its scalar term is still later. Hence

\[
C_{2r+1}=\frac38\operatorname{quo}_z(D_r^2,H_0).\tag{4}
\]

All r considered below satisfy these inequalities. Thus no lower
target coefficient, h correction, or bD cross term has been dropped.

## Actual frozen source support

For (99,66), B2 has normalization degree 65, z-degree at most 32,
and floor `3r+4q>=189`; A3 has degree 98, the same q cap, and floor
`3r+4q>=285`. Therefore D starts no earlier than r=21 and C no
earlier than r=53. In the actual `outer_state(0)` graph,
`(B2c_27_27)` maps to zero: its weight equals 189, and every outer
D2 equality coordinate is killed by the offset-zero D1 rows. The
independent full-rank certificate is `nondegeneracy-controls.json`.

For D=108, the corresponding values are normalization degrees
71 and 107, q cap 35, and floors `4r+5q>=276` and `>=416`. D starts
at r>=26 and C at r>=61. The original source maps preserve exactly
these bounds; preprocessing must act on their **images**, not infer
images from coordinate names.

## The (99,66) cutoff

Assume, for contradiction, that the first nonzero D band has r<=27.

For r=21,...,25, the left side of (4) is absent because 2r+1<53.
The quotient is zero. A nonzero polynomial whose square has zero
quotient by monic degree-33 H0 has degree at most 16. But the D
source floor forces its smallest z-power to be at least
`ceil((189-3r)/4)>=29` for r<=25. Contradiction.

For r=26, C53's only possible source power is q=32. The quotient
in (4) has degree at most `2*32-33=31`. These spaces intersect only
in zero; hence the quotient is zero again. Now D26's smallest
possible power is 28, also incompatible with degree at most 16.

For r=27, the source floor puts C55 in the span of z30,z31,z32.
The quotient has degree at most 31, so write it R(z) with z-order
at least 30. The source floor puts D27 in z27*k[z]. In the division
identity

\[
D_{27}^2=R H_0+S,\qquad\deg S<33,
\]

both D27^2 and R H0 are divisible by z54. Thus S is divisible by
z54 and has degree below 33; it is zero. Since H0 divides D27^2,
the factor `(1+z)^9` forces `(1+z)^5` to divide D27. Combining
z-order at least 27 with degree at most 32 gives

\[
D_{27}=\tau z^{27}(1+z)^5.
\]

Its z27 coefficient is tau. The actual source equality image at
(r,q)=(27,27) is zero, so tau=0, contradiction. Therefore

\[
\boxed{D_r=0\ \text{for every }r\le27.}
\]

Now mathsf D starts at r>=28. The quotient contribution in (2)
starts at t57; bD starts at t61; the scalar term starts at t98.
Consequently

\[
\boxed{C_r=0\ \text{for every }r\le56.}
\]

These are precisely the B2/A3 position-row consequences used by
`root_preprocess_front.py`. Applying rational elimination to those
position rows may solve coordinates in higher bands as a consequence
of earlier source graph relations; it does not justify deleting a
free coordinate merely because its name contains a low r.

## The D=108 cutoff and optional next band

For r=26,...,29, 2r+1<61, so the quotient in (4) is zero. Nonzero
D_r would then have degree at most 17, while the source floor puts
its smallest possible power at least 32. For r=30, C61 has only
power q=35, while the quotient has degree at most
`2*35-36=34`; both must vanish, yielding the same contradiction.
Therefore

\[
\boxed{D_r=0\ \text{for every }r\le30.}
\]

Equation (2) now gives its quotient contribution starting at t63,
bD at t67, and the scalar at t107, so

\[
\boxed{C_r=0\ \text{for every }r\le62.}
\]

The next band is not legitimately set to zero by this argument.
If r=31, D31 has possible powers 31,...,35; C63 has source powers
33,...,35; the quotient has degree at most 34. Write it
`R=z^33(alpha*z+beta)`. The remainder `D31^2-R H0` has degree
less than 36 and is divisible by z61, so it is zero. Its z61
coefficient forces beta=0. Factoring the exact square then gives

\[
D_{31}=\tau z^{31}(1+z)^4,\qquad
R=\tau^2z^{34},\qquad C_{63}=\tfrac38\tau^2z^{34}.
\]

Here tau is a retained coefficient, with no inversion or nonzero
pin. These graph constraints preserve tau=0. They are optional;
they do not license a blanket cutoff of D31 at stage zero.

## Logical status for computation

The equations just proved are zero-coordinate consequences on the
algebraic set of the original characteristic and source ideal.
When a proof uses square divisibility to conclude a coefficient is
zero, adding that coefficient is a radical strengthening. Over
characteristic zero it preserves the geometric locus, properness,
and unit/nonunit status; it must be recorded as such rather than
claimed to be a linear ideal consequence without a certificate.
Every original source and characteristic row must still be mapped
and checked after this preprocessing. A final UNIT requires those
checks and the gauge/localization ledger; no claim is made here
that the preprocessing itself kills either full chart.

`front-band-controls.py/.json` imports both frozen engines read-only,
records their hashes, checks their actual offset-zero outer maps and
all vanished equality images, and recomputes the source minima and
every boundary band's allowed powers. Its exact division controls
verify the (99,66) r27 form and the D=108 r31 form. The first is a
negative control for omitting the source equality corner; the second
is a negative control for extending the D108 cutoff to r31. Both
would be lost by an unsupported stronger preprocessing claim.
