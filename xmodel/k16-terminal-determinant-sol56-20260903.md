# Finite-quotient determinant and residual-axis audit on the normalized K=16 ray

**Lane:** `k16-terminal-determinant-sol56-20260903`  
**Date:** 2026-09-03  
**Verdict:** **PARTIAL.**  Neither requested uniform lemma has been proved.
The exact theorem on this ray therefore remains proved for `t=1,...,5`, with
the `b4=0` half also proved at `t=6`; it is not promoted for every `t`.

There are two concrete advances.  First, the determinant route has been made
componentwise and tested: at the split base `t=2` the selected quotient has
different ranks on the two factors (`1` and `2`), so a single free `A_t`-basis
is not a valid uniform target.  Both local determinants are nevertheless
nonzero.  At `t=6` both mod-`1009` fibres give finite quotient length `1224`,
which disproves the tempting extrapolation `9*5^(t-3)-1` from the charged
lengths `8,44,224`.  No indexed finite-basis construction or determinant
recurrence results.

Second, charged recurrence (6.4) has been executed in exact coefficient pairs.
All its denominators are uniformly safe; its reduced denominators and norms
are fully factored at `t=3,4,5,6`, and both exact factors pass at split `t=11`.
The norm is positive in exact tests through `t=20`, but there is no closed
all-`t` factorization.  A related two-solve calculation does give a closed,
positive norm on every outer-third coordinate axis
`ceil((2t+2)/3)<=j<t`.  These are coordinate-axis image statements, not the
ideal containments required by `RESIDUAL-ZERO`.

All labels below are literal.  `PROVED-HERE` denotes an indexed identity or an
exact characteristic-zero calculation in the declared algebra;
`MEASURED-MODULAR` denotes only a finite-field test; `OPEN[...]` is the exact
remaining mathematical statement.

## 1. Custody, algebra, map, and sign

The readable receipt
`xmodel/k16-terminal-determinant-sol56-20260903.run.v2` was parsed with `awk`.
Its paired `charged_input_<i>_sha256` and
`charged_input_<i>_basename` fields generated `/tmp/k16det-input-manifest.sha256`,
which was passed to `sha256sum -c`.  The result was **17/17 `OK`**; no digest
was typed into the check command.  The frozen terminal report Sections 2--8,
the middle-spine and pivot reports, the hostile gate, the fallacy guardrail,
and the charged JSON/Python artifacts were read from
`/tmp/jc2-lane.ZvRDkK/inputs`.  No ledger, `jc2-lean`, `ideation-*`, or excluded
in-progress report was read or edited.  Durable new files are confined to
`box/k16det-20260903/` and this report; the mechanically generated checksum
manifest is the cited temporary file under `/tmp`.

Use the charged notation

```text
q=2t+1,  e=3t+1,
H_t(y)=12q^2y^2-12q(t+1)y+(t+1)(3t+2),
d=2qy-(t+1),
A_t=Q[y]/(H_t)=Q[d]/(3d^2-(t+1)),
g=t(3t+1)(3d+2(t+1))/(6q^3),  c=-yg.                 (1.1)
```

The post-spine ring is

```text
A_t[b3,b4,u_2,...,u_(t-1)],  u_i=q_(i,0).            (1.2)
```

The frozen records store coefficients of `R=-E_t`, whereas the question uses

```text
T_(t,k)=[X^k]sigma_t(E_t)=-[X^k]sigma_t(R).          (1.3)
```

This sign does not change an ideal, quotient length, or the nonvanishing of a
determinant, but it is included in the exact `t=2` matrices below.

The rank-two algebra is separable.  It is a field unless
`t=3s^2-1`; at every such index it is the product obtained by evaluating
`d=+s` and `d=-s`.  In particular

```text
t=2:  (d,y)=(-1,1/5),(+1,2/5),
t=11: (d,y)=(+2,7/23),(-2,5/23).                     (1.4)
```

No determinant or inverse below treats a product algebra as a field.

## 2. Denominators already discharged by the terminal recurrence

For an affine class `ad+b`,

```text
Res_y(H_t,ad+b)=4q^2(3b^2-a^2(t+1)),
(ad+b)^(-1)=3(b-ad)/(3b^2-a^2(t+1)).                 (2.1)
```

The coefficient-array recurrence (charged (2.2)--(2.13)) inverts the algebra
classes `y`, `3d+2(t+1)` (the class of `g`), `L_C`, `L_Q`, and
`3qd+(t+1)` (the `b2` pivot).  Its rational/indexed factors are exactly

```text
2,3,6,q,q^2,q^3,t,e,t+1,3t+2,4t+1,
m+1                    (0<=m<t),
2m+1                   (0<=m<=2t),
4t-2j+1                (1<=j<t and t<=j<=2t),
q-j                    (t<=j<=2t),
F_C(t,j)               (1<=j<t),
F_Q(t,j)               (t<=j<=2t),
and constant factorial factors.                              (2.2)
```

The charged positivity identities give `F_C>0` and `F_Q>=12` on their full
integer ranges.  The indexed scalar factors in (2.2) are positive there.
Thus this recurrence has no specialization exception for integer `t>=2`.
This audit is consumed, not silently extended: a prospective quotient basis
or determinant may introduce additional leading coefficients, and no such
new denominator is declared safe without its own resultant.

## 3. TOP-TAIL-UNIT: the correct finite-algebra criterion

Put

```text
F_r=T_(t,t+r)|_(b4=1),          0<=r<t,
J_t=<F_1,...,F_(t-1)>,
B_t=A_t[b3,u_2,...,u_(t-1)]/J_t.                    (3.1)
```

For each field factor `K_e` of `A_t`, suppose
`B_(t,e)=B_t tensor_(A_t) K_e` is finite-dimensional.  Then

```text
<F_0,...,F_(t-1)>=[1] on K_e
 iff B_(t,e)/F_0 B_(t,e)=0
 iff mu_(F_0):B_(t,e)->B_(t,e) is bijective
 iff det(mu_(F_0)|B_(t,e)) != 0.                    (3.2)
```

Nilpotents in `B_(t,e)` cause no problem in (3.2).  At a split index the
two vector-space dimensions may differ, so the two determinants are separate
local determinants.  Equivalently, `B_t` may be a finite projective
`A_t=Q x Q` module of locally varying rank.  A single square matrix over
`A_t`, a single global rank, and a determinant obtained by inverting a
zero-divisor are not justified.

### 3.1 Exact split base `t=2`

Here `J_2=<F_1>` in one variable.  Direct replay of the authenticated exact
terminal record, with the sign (1.3), gives

```text
d=-1, y=1/5:
 F0= 7(16b3-35)/640,
 F1=-7(88b3-295)/640.

d=+1, y=2/5:
 F0=-18(287156086b3^2-27046560b3+106639425)/74352915125,
 F1=-14(1189646642b3^2+304374720b3-1207034325)/371764575625. (3.3)
```

On the first factor, `B_(2,-)` has basis `(1)` and

```text
det(mu_F0)=287/1408 != 0.                            (3.4)
```

On the second, use `(1,b3)` after making `F1` monic.  The multiplication
matrix is

```text
[ -8310084192/86249381545, 10387061461728/420707233300201 ]
[       430272/17682025,       -8847063648/86249381545 ]
```

and

```text
det(mu_F0)=2762023282304080896/297558232675799463481 != 0. (3.5)
```

Therefore `TOP-TAIL-UNIT` is exact at `t=2`, but

```text
dim_Q B_(2,-)=1,  dim_Q B_(2,+)=2.                   (3.6)
```

This is a positive base-case control and a negative control on the proposed
uniform free-basis formulation.  The correct all-split target is (3.2).

### 3.2 Finite quotient and determinant probes

The frozen emitter was imported from its authenticated read-only path; the
new probe changes only the post-map calculation in the explicitly declared
residual-variable ring.  For each test it forms `std(J_t)`, checks `dim`, then
uses `vdim` and `kbase` only on a zero-dimensional nonunit ideal.  Multiplication
matrices are filled by reducing `F_0` times every standard monomial.  Hence no
raw remainder is assigned a degree before zero and finiteness are handled.

The measured data are:

| `t` | coefficient computation | local lengths of `B_t` | determinant status |
|---:|---|---:|---|
| 2 | exact, `d=-1,+1` | `1,2` | exact nonzero, (3.4)--(3.5) |
| 3 | exact quadratic field | `8` | exact nonzero |
| 3 | mod `1009`, two fibres | `8,8` | `-11,-382` |
| 4 | exact quadratic field | `44` | nonzero follows from charged full unit |
| 4 | mod `1009`, two fibres | `44,44` | `202,-269` |
| 5 | mod `1009`, two fibres | `224,224` | `231,-165` |
| 6 | mod `1009`, two fibres | `1224,1224` | not computed / not needed for the length falsification |

The `t=3` exact standard-monomial basis has length `8`; the determinant is an
explicit nonzero affine class in the integral generator `a=3d`.  The modular
determinants at `t=3,4,5` are nonzero on both roots.  These are finite tests,
not a characteristic-zero proof at a new `t` and not an indexed recurrence.
The exact `t=4` computation proves `J_4` has length `44`; since the charged
full top-tail ideal is exactly `[1]`, criterion (3.2) proves its omitted-row
determinant nonzero without expanding a 44-square determinant.

The new `t=6` value is decisive only as a negative pattern control:

```text
9*5^(6-3)-1=1124 != 1224.                            (3.7)
```

Thus the three charged lengths `8,44,224` do not continue by the suggested
fit.  On the two `t=6` fibres the reduced bases have `525` elements and equal
colength `1224`.  Their detailed leading ideals are large and do not exhibit
a stable one-row/one-variable triangle.  Even at `t=4` the two fibre bases
have different reduced-basis sizes (`21` and `20`) although their colengths
agree, another warning against promoting one sampled initial ideal.

There is nevertheless a precise measured finiteness target.  The checked
leading ideals contain

```text
t=3: b3^3,u2^4
t=4: b3^5,u2^5,u3^6
t=5: b3^7,u2^6,u3^7,u4^8
t=6: b3^9,u2^7,u3^7,u4^9,u5^10.
```

Consequently all tests support, but do not prove,

```text
M_t=<b3^(2t-3), u_i^(t+i-1) : 2<=i<t>
       subset in_dp(J_t), t>=3.                       (3.8)
```

The stronger `u3^7` seen at `t=6` implies the displayed candidate `u3^8`.
An indexed sequence of S-polynomial or border reductions proving (3.8), with
every leading coefficient a unit on both split factors, would prove the
finite clause.  Equality with any sampled initial ideal is not asserted.

At the next split index `t=11`, the charged recurrence has all 23 exact
specialized high pivots nonzero, and its mod-`1009` values are `y=439,746`.
There is no charged or new completed finiteness/determinant computation for
`J_11`; no rank equality may be presumed from nonsplit cases or from `t=2`.

### 3.3 Exact open statement and cheapest test

The determinant route now has the following correct target.

```text
OPEN[TOP-TAIL-FINITE-LOCAL]:
 for every integer t>=3 and every field factor K_e of A_t,
 B_(t,e) is finite-dimensional; construct a specialization-safe local basis.

OPEN[TOP-TAIL-LOCAL-DETERMINANT]:
 for those bases, derive a bounded indexed recurrence for
 Delta_(t,e)=det(mu_(F0)|B_(t,e)) and prove Delta_(t,e)!=0. (3.9)
```

Away from split fibres, writing a computed determinant as `a_t d+b_t` would
reduce the unit test to

```text
3b_t^2-(t+1)a_t^2 != 0.                              (3.10)
```

At split fibres (3.10) is valid only if the determinant class itself
specializes from a basis that remains a basis.  The rank jump at `t=2` shows
why one must instead construct/check both local matrices when a leading
coefficient vanishes.  Every new basis denominator must be listed and its
resultant with `3d^2-(t+1)` checked before (3.10) is used.

The cheapest falsification remains the two-factor `t=11` job: specialize
`b4=1` and `J_11=<bands 12,...,21>` at `y=439,746 mod 1009`, compute only
`dim/vdim`, and only if both are finite form the band-11 multiplication
determinants.  A full top-tail standard basis is unnecessary.  A success is
still `MEASURED-MODULAR`; a dimension failure would refute the proposed
choice of `J_t`.

## 4. RESIDUAL-ZERO: the proved `b3` axis and its boundary

Let

```text
I_(t,+)=<T_(t,1),...,T_(t,2t-1)>|_(b4=0).            (4.1)
```

On the `b3` coordinate axis the charged symbolic solve gives

```text
C=X^(t-1),
U=X^(2t+1)+a b3 X^t,  b2=0,
a=-(6dt-3d+9t^2+2t-1)/(6t(3t-1)),                  (4.2)
```

and, for stored `R=-E`,

```text
[X^(2t-1)]R=lambda_b b3^2,
lambda_b=t(3t+1)(A_b d+B_b)/
         (12(2t+1)^2(3t-1)^2(3t+2)),
A_b=27t^3-30t^2+t-2,
B_b=6t^3+13t^2-3t+2.                                (4.3)
```

Its primitive norm factors as

```text
3B_b^2-(t+1)A_b^2
=-(t-2)(3t-1)^2(3t+2)(27t^3+17t^2+t+2).             (4.4)
```

The denominators introduced here are `2,3,t,2t+1,3t-1,3t+2`, plus the
already audited `y,p_C,p_Q,p_b2` pivots.  They are nonzero for `t>=3`, and every factor
in (4.4), apart from its displayed sign, is positive.  Thus (4.3) is a unit
for every integer `t>=3`, including both factors at every split index.

At `t=2`, (4.3) reduces to

```text
lambda_b=14(d+1)/625=28(5y-1)/625.                  (4.5)
```

It vanishes at `d=-1,y=1/5` and not at `d=+1,y=2/5`.  In fact the stored
`b4=0` rows are

```text
d=-1: (-7/625,0,0,0),
d=+1: (-42/625,0,0,28b3^2/625).                     (4.6)
```

So `RESIDUAL-ZERO` is false in `A_2=Q x Q`; the band-zero scalar is a unit on
each factor and closes that chart.  This is the required separate base.

Crucially, (4.3) proves only

```text
b3^2 in I_(t,+)+(u_2,...,u_(t-1)),                  (4.7)
```

Charged (2.14) says every positive row vanishes at the residual origin, so
the axis image is contained in `(b3)`; together with (4.7), its radical is
exactly `(b3)`.  This does not prove any `b3^N in I_(t,+)`.

## 5. Exact coefficient-pair execution of the `u2` recurrence

Work in `K_t=Q(t)[d]/(3d^2-(t+1))` and store an element as the pair
`(b,a)=b+ad`.  Pair multiplication and inversion are

```text
(b,a)(v,u)=(bv+(t+1)au/3, bu+av),
(b+ad)^(-1)=3(b-ad)/(3b^2-(t+1)a^2).                (5.1)
```

Set `z=u2`, `s=z/X^2`, `Theta=s d/ds`, and
`Delta_n=n-2Theta`.  The driver implements charged (6.4) coefficientwise:

```text
C=X^(t-1)chi(s), U=X^q upsilon(s), chi_0=1,
upsilon_0=upsilon_1=1,
beta_r=g(3t+2-6r)chi_r/(2y(t-2r))
       (0<=r<=floor((t-1)/2)); beta_r=0 otherwise,
f=3g Delta_q(upsilon)+chi beta-chi Delta_t(beta)
  +2 Delta_t(chi) beta,
delta_r=f_r/(y(4t-4r+1)),
xi={Delta_(t+1)(chi)delta-chi Delta_q(delta)
    +2 Delta_q(upsilon)beta}/(2y),
rho=chi xi-Delta_q(upsilon)delta.                   (5.2)
```

It solves `chi_r` for `1<=r<=floor((t-1)/2)` with `p_C(t,2r,d)`, then
`upsilon_r` for `ceil(t/2)<=r<=t` with `p_Q(t,2r,d)`.  Setting each new
coefficient first to zero and then one reproduces the charged pivot exactly;
after substitution `rho_1=...=rho_t=0`.  An independent reconstruction of
`C,U,B,S,V,Y,Z,N,P0',R` through charged (2.3)--(2.7), in `X` rather than the
compressed `s` series, gives

```text
[X^(2t-1)]R=lambda_2(t,d) u2^(t+1),
lambda_2=rho_(t+1).                                  (5.3)
```

Both implementations agree at `t=3,4,5,6,11`, and each passes the independent
direct-array reconstruction.  At `t=3` the result also agrees coefficientwise
with the frozen exact rows after the declared `y -> (d+t+1)/(2q)` map.  For
`t=4,5,6`, the charged exact-row-match status is consumed; this lane does not
pretend their metadata files contain row dumps.

### 5.1 Every recurrence denominator

Besides (2.2), the complete factor provenance in (5.2) is

```text
2,3,q=2t+1,t+1,3t+2,
t-2r                    (0<=r<=floor((t-1)/2)),
4t-4r+1                 (0<=r<=t),
t(3t+1)F_C(t,2r)        (1<=r<=floor((t-1)/2)),
t(3t+1)(q-2r)F_Q(t,2r)  (ceil(t/2)<=r<=t).           (5.4)
```

Here `t-2r>=1`, `4t-4r+1>=1`, and `q-2r>=1` on the displayed ranges;
`F_C>0`, `F_Q>=12`, and `y` has nonzero norm.  Hence every division used to
define `lambda_2` is valid for every integer `t>=3`, on both factors at a
split index.  The reduced denominator `D_t` divides a product of these safe
factors.  This proves denominator safety without pretending that the reduced
sequence `D_t` is one polynomial in `t`.

### 5.2 Fixed factorizations and the split test

Write the reduced result as `(A_t d+B_t)/D_t`, with
`gcd(A_t,B_t,D_t)=1`, `D_t>0`, and put
`N_t=3B_t^2-(t+1)A_t^2`.  The exact factorizations are:

```text
t=3:
D=2^3*7^4*13*1201^4
N=2^2*5^10*11*13^2*59*1201^4*34127

t=4:
D=3^9*17*1669^5
N=2^2*5^3*7^5*11*13^2*17^3*1669^5*889391

t=5:
D=5^2*7^2*11^6*23*31^6*311^6
N=2^6*3^25*17^3*23*31^5*311^6*10211367113652506331367

t=6:
D=3^2*13^7*43*79*8693^3*20161^7
N=2^4*3*5^2*7^5*11^14*19^2*43*79*277*8693^3*20161^7
  *1125763*193855531*655055668041221.               (5.5)
```

Exact primality tests were applied to the displayed terminal factors.  Thus
all four norms are positive.  The reduced denominator at the split test is

```text
D_11=2^9*17*19*23^13*29^2*73^4*103^12*107^12*131^6*193^4*331^6.
```

At split `t=11`, the two exact values are

```text
d=+2:
-6177238031896341800583932478426714962914784534097465979003012517235 /
 85640045846134140549846427464640089892780731720469546129870909190045312,

d=-2:
-78989420135234935451475848925292706365825292589619934748046875 /
 120682949885215691747048150993541893519416225027977328410273853472.
                                                               (5.6)
```

Both are nonzero; this is an exact two-factor falsification check, not merely
a mod-`1009` check.  Exact `N_t>0` also holds for every tested `3<=t<=20`.
The observed signs are `sign(B_t)=(-1)^t`, `sign(A_t)=(-1)^(t+1)`, with
`|B_t|>sqrt((t+1)/3)|A_t|`; this is only a candidate induction invariant.

There is no bounded closed formula or recurrence for `N_t` here.  Because
the number of solves in (5.2) grows with `t`, the individual factorizations
in (5.5) are not values of a displayed fixed polynomial whose integer roots
can be checked.  The exact remaining axis statement is

```text
OPEN[U2-NORM]: N_t != 0 for every integer t>=3.       (5.7)
```

## 6. A uniform outer-third family of axis factorizations

The same grading gives a broader **PROVED-HERE, AXIS-ONLY** statement.  Choose
integers `c>=1`, `t>=3c+2`, and put

```text
j=t-c, z=u_j, s=z/X^j, Theta=s d/ds,
Delta_n=n-j Theta.                                    (6.1)
```

Equivalently, `ceil((2t+2)/3)<=j<=t-1`.  On the coordinate axis obtained by
setting `b3,b4` and every `u_i` other than `u_j` to zero, the only high
weights divisible by `j` are `j` and `2j`.  Thus the only solves are
`chi_1` (`c_j`) and `upsilon_2` (`u_(2j)`); since `3j>q`, no further
`u` variable or `b2` occurs.  Replace `2Theta` by `jTheta` in (5.2) and use

```text
beta_r=g(3t+2-3jr)chi_r/(2y(t-jr)) (r=0,1),
beta_r=0 otherwise,
delta_r=f_r/(y(4t-2jr+1)).                            (6.2)
```

After the two charged pivots, the first surviving coefficient is

```text
[X^(4t+1-3j)]R=lambda_(t,j) u_j^3.                   (6.3)
```

The band lies in `1,...,2t-1`: the lower bound uses `j<=t-1`, and the upper
bound uses `3j>=2t+2`.

Write `lambda_(t,j)=a(t,c)d+b(t,c)` and define

```text
P(t,c)=3c^4+24c^3t+42c^3+66c^2t^2+146c^2t+119c^2
       +72ct^3+238ct^2+234ct+104c
       +27t^4+134t^3+223t^2+136t+32,
Q(t,c)=c^2+2ct+4c+t^2+t+1,
G(t,c)=c^2-10ct-14c+25t^2+22t+1.                    (6.4)
```

Exact symbolic coefficient-pair arithmetic gives the common denominator
`q^3 Q(t,c)P(t,c)^3` for `a,b`, and the completely factored norm

```text
3b^2-(t+1)a^2
=9t^2(t-c)^6(t+1)(3t+1)^2(4t+1)(t+c+1)^6 G(t,c)
 /[q^6 Q(t,c)P(t,c)^3].                              (6.5)
```

Here `P(t,c)=F_C(t,t-c)>0` is exactly the charged all-positive quartic, and
`Q>0`.  If `n=t-3c-2>=0`, then

```text
G(3c+2+n,c)=196c^2+140cn+332c+25n^2+122n+145>0.     (6.6)
```

Thus (6.5) is positive on the entire stated integer sector and
`lambda_(t,j)` is a unit on both factors of every split algebra.

For the denominator audit, the new scalars before cancellation are

```text
t, c=t-j, 2c+1=q-2j,
4t+1, 2t+2c+1, 4c+1, 6c-2t+1,                       (6.7)
```

together with `2,3,6,q,e=3t+1,t+1,3t+2,y,p_C(t,j),p_Q(t,2j)` already
covered in Section 2.  Before cancellation the three reduced intermediate
denominators are `qP`, `2(2c+1)qQP^2`, and `q^3QP^3`; the norm denominator is
`q^6QP^3`.  The last Euler numerator `f_3` is zero, so the last division is
avoidable; the executable performs it, and `6c-2t+1` is an odd nonzero
integer (indeed at most `-3`).  The two new primitive pivot-norm factors are
`P` and `Q`.  This lists every division in the two-solve calculation.

Specializing `c=1` gives the `u_(t-1)` axis for `t>=5` and recovers

```text
3b^2-(t+1)a^2
=9t^2(t-1)^6(t+1)(t+2)^6(3t+1)^2(4t+1)
  *(25t^2+12t-12)
 /[q^6(t^2+3t+6)
   *(27t^4+206t^3+527t^2+540t+300)^3].              (6.8)
```

In the stored-`R` sign convention, the new fixed-axis evaluator gives
`lambda=(-550304d+819920)/37500925` at `(t,j)=(5,4)` and
`lambda=(-22519104d+36635648)/1349232625` at `(6,5)`; both specialize
consistently with the charged exact-row-match status.
Exact substitutions at `(t,c)=(5,1),(6,1),(8,2),(9,2),(11,1),(11,2),
(14,4),(26,8)` agree with the general fixed-axis recurrence, including two
sector boundaries and split `t=11`.  At the exceptional
small schedules `t=3,4`, the `j=t-1` axis also has nonzero exact norm (the
`t=4` calculation correctly includes `b2`).

Every positive row vanishes at the residual origin by charged (2.14), so the
axis image is contained in `(u_j)`.  Consequently (6.3) proves that every
outer-third coordinate-axis image has radical exactly `(u_j)`, but only the
membership

```text
u_j^3 in I_(t,+)+(b3,{u_i : 2<=i<t, i!=j}).          (6.9)
```

It does not give the stronger successive quotient containment modulo only
`(b3,u_(t-1),...,u_(j+1))`.

## 7. Why the axis route still does not prove RESIDUAL-ZERO

The desired statement is

```text
sqrt(I_(t,+))=(b3,u_2,...,u_(t-1)) for every t>=3.  (7.1)
```

Coordinate-axis restrictions can miss an off-axis component.  In particular,
(4.7), (5.3), and (6.9) do not put a pure power into the original
multivariable ideal.  The `u2` calculation is the **last** conditional
triangular quotient, modulo `(b3,u_(t-1),...,u3)`; it is not the next step
after the `b3` axis.

A sufficient missing certificate remains exactly

```text
b3^N0 in I_(t,+),
u_j^Nj in I_(t,+)+(b3,u_(t-1),...,u_(j+1)),
                         j=t-1,t-2,...,2,             (7.2)
```

with an indexed reduction proving each membership and a unit norm for each
leading coefficient.  The first membership and all intermediate memberships
`j=t-1,...,3` remain open.  Even a proof of `OPEN[U2-NORM]` would close only
the final coefficient after those earlier containments were available.

The exact fixed radical certificates at `t=3,4,5,6` remain valid:

| `t` | pure powers checked in `I_(t,+)` |
|---:|---|
| 3 | `b3^3,u2^6` |
| 4 | `b3^4,u2^8,u3^6` |
| 5 | `b3^5,u2^13,u3^9,u4^7` |
| 6 | `b3^5,u2^16,u3^11,u4^8,u5^7` |

Their changing exponents do not define an induction.  The cheapest genuine
next test is not another coordinate restriction: at both `t=11` factors,
reduce proposed pure powers or successive quotient normal forms in the ideals
of (7.2), modulo a good prime, and record every vanished leading coefficient.
A full lexicographic radical computation is unnecessary.  Such a test can
falsify a proposed triangular schedule but cannot prove the all-`t` claim.

Thus

```text
OPEN[RESIDUAL-ZERO-UNIFORM]: prove (7.1), equivalently (7.2) or another
specialization-safe indexed containment certificate.              (7.3)
```

## 8. Controls `t=2,...,6`, assembly, and verdict

| `t` | terminal recurrence | `TOP-TAIL-UNIT` | residual chart |
|---:|---|---|---|
| 2 | exact on both rational factors | exact; local ranks `1,2`, dets nonzero | `RESIDUAL-ZERO` false; band zero unit on both factors |
| 3 | exact charged-row match | exact; local length `8` | exact radical; pair recurrence agrees |
| 4 | exact charged-row match | exact; mod local lengths `44,44` | exact radical; pair recurrence agrees |
| 5 | exact charged-row match | exact characteristic-zero unit; mod lengths `224,224` | exact radical; pair recurrence agrees |
| 6 | exact rows; charged modular fibres agree | exact full run inconclusive; mod prefix lengths `1224,1224` | exact radical; pair recurrence agrees |

At `t=1` the separate banked computation is exact.  At `t=11`, both product
factors are respected: the high-pivot formulas specialize without a zero,
the `u2` values (5.6) are nonzero, and the outer-third norm (6.5) is positive.
There is no top-prefix or full residual ideal result at that index.

The two-chart assembly in the charged report remains sound: a unit residual
chart makes `b4` invertible modulo the full terminal ideal, while a unit
dehomogenized top chart homogenizes to a power of `b4` in that ideal.  In a
nonzero quotient `b4` cannot be both invertible and nilpotent.  But the
uniform hypotheses needed by that assembly are precisely the componentwise
determinant target (3.9) and residual target (7.3); (3.8) is only a sufficient
measured candidate for the finiteness half of (3.9).

Therefore the requested verdict is

```text
PARTIAL.
(T) on the normalized K=16 ray is PROVED for t=1,2,3,4,5.
The b4=0 half is additionally PROVED at t=6.
The all-t TOP-TAIL-UNIT, RESIDUAL-ZERO, (8.1), and hence (T), remain OPEN.
```

## 9. FALLACY-v2 audit

- **Product algebra.**  Every split assertion is componentwise.  The unequal
  `t=2` local ranks are exposed; no zero-divisor is inverted and no global
  free basis is invented.
- **Specialization denominators.**  Section 2 lists the charged recurrence
  factors; (4.3), (5.4), and (6.7) list every new axis factor.  The missing
  determinant basis/resultant is left `OPEN`, rather than inferred from fixed
  primes or samples.
- **Raw remainders and ring maps.**  The probe first checks a zero-dimensional
  nonunit `J_t`, declares the residual generator order, and only then uses
  `vdim`, `kbase`, and normal forms.  Exact `y,d` images and the sign map are
  stated in Section 1.
- **Finite versus uniform.**  Exact fixed-`t` bases, modular fibre tests, and
  sign observations through `t=20` are not promoted to indexed theorems.  The
  failed length extrapolation (3.7) is retained as a negative control.
- **Axis versus containment.**  Axis images (4.7), (5.3), and (6.9) are never
  called memberships in `I_(t,+)`; the actual missing containments are (7.2).
- **Prime/derivative.**  `Theta=s d/ds`; a finite-field prime is written
  `mod 1009`.  No ambiguous prime mark is used.
- No exit-price assertion is made, so no `charge_basis` declaration applies.

## 10. Reproduction

All new drivers and bounded outputs are under `box/k16det-20260903/`.

```text
# exact split t=2 rows, bases, matrices, determinants, and residual control
python3 box/k16det-20260903/audit/t2_component_determinant.py

# exact u2 coefficient pairs; includes independent X-array reconstruction
python3 box/k16det-20260903/residual/u2_pair_recurrence.py 3 4 5 6 11

# bounded exact sign/norm audit for every 3<=t<=20
python3 box/k16det-20260903/residual/verify_u2_range.py 3 20 \
  > box/k16det-20260903/residual/u2_range_3_20.json

# closed two-solve outer-third formula; default without the variable gives c=1
K16_AXIS_OFFSET=symbolic \
  python3 box/k16det-20260903/residual_sector_m2_symbolic.py

# fixed-(t,j) axis controls, including exceptional schedules
python3 box/k16det-20260903/residual_uj_pairs.py 3
python3 box/k16det-20260903/residual_uj_pairs.py 4
python3 box/k16det-20260903/residual_uj_pairs.py 5
python3 box/k16det-20260903/residual_uj_pairs.py 6
python3 box/k16det-20260903/residual_uj_pairs.py 11
python3 box/k16det-20260903/residual_uj_pairs.py 8 --j 6
python3 box/k16det-20260903/residual_uj_pairs.py 9 --j 7
python3 box/k16det-20260903/residual_uj_pairs.py 14 --j 10
python3 box/k16det-20260903/residual_uj_pairs.py 26 --j 18

# finite quotient/determinant probes generated from the frozen emitter
python3 box/k16det-20260903/top_tail/probe_top_tail.py 3 --mode exact
python3 box/k16det-20260903/top_tail/factor_exact_determinants.py
python3 box/k16det-20260903/top_tail/probe_top_tail.py 4 --mode exact \
  --no-det --dump-leading --tag lm
for t in 3 4 5; do for b in 0 1; do
  python3 box/k16det-20260903/top_tail/probe_top_tail.py "$t" \
    --mode mod --branch "$b" --tag det
done; done
python3 box/k16det-20260903/top_tail/probe_top_tail.py 6 --mode mod \
  --branch 0 --no-det --dump-leading
python3 box/k16det-20260903/top_tail/probe_top_tail.py 6 --mode mod \
  --branch 1 --no-det --dump-leading

sha256sum -c box/k16det-20260903/artifacts.sha256
```

The proof-ready audit notes are
`box/k16det-20260903/audit/charged_controls.md` and
`box/k16det-20260903/residual/FINDINGS.md`; the top-tail notes are in
`box/k16det-20260903/top_tail/FINDINGS.md`, and the generic symbolic output is
`box/k16det-20260903/residual_sector_m2_tc.out`.  The bounded `t=3,...,20`
audit is `box/k16det-20260903/residual/u2_range_3_20.json`.  Each completed
cited Singular probe has stdout/stderr sidecars, empty stderr, and a terminal
`PROBE_DONE` in stdout.  The orphan sources
`probe_t4_exact_bNone.sing` and `probe_t6_mod_b0_det.sing` are interrupted
experiments without outputs and are not evidence here.  All computations and
cross-checks cited above completed before sealing.  The 102 durable artifacts
are covered by `box/k16det-20260903/artifacts.sha256`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `28586`.
- Body SHA-256:
  `abeb9eeee3689b66d4fb8c89c333b1529fa4abcbc703d0e0f414657969851bd9`.
- Frozen basis: `4b1322fefe85698f8dd710a9108a66caebbef14a`.
