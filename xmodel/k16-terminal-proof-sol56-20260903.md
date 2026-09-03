# The terminal family on the normalized K=16 ray

**Lane:** `k16-terminal-proof-sol56-20260903`  
**Date:** 2026-09-03  
**Verdict:** **PARTIAL.**  A closed, coefficientwise, symbolic-`t` recurrence
for every `T_(t,k)` is proved below and checked against all charged finite
records through `t=6`.  It gives coefficient weight/degree bounds, all
high-spine leading coefficients, and a split-safe denominator audit.  It does
**not** prove either sharpened lemma for arbitrary `t`.  New exact computations prove
`TOP-TAIL-UNIT` at `t=5` and `RESIDUAL-ZERO` at `t=5,6`; therefore (8.1), and
hence theorem (T) on this ray, is newly proved at `t=5` in addition to the
banked `t=1,2,3,4`.  No statement at an unbounded set of `t` is inferred from
these computations.  A uniform residual-axis calculation does prove that the
top positive row cuts the `b3`-axis for every `t>=3`; the multivariable
containment needed by `RESIDUAL-ZERO` remains open.

All claim labels are literal.  `PROVED-HERE` means an indexed identity or an
exact checked computation over the declared characteristic-zero coefficient
algebra.  `MEASURED-MODULAR` is only a finite-field control.  `OPEN[...]` is a
typed missing statement.

## 1. Custody, ring, and sign

The readable receipt
`xmodel/k16-terminal-proof-sol56-20260903.run.v2` was parsed mechanically with
`awk`: the `charged_input_<i>_sha256` and matching
`charged_input_<i>_basename` fields generated a temporary 19-line manifest
under `/tmp`, which was passed to `sha256sum -c`.  The result was **19/19
`OK`**.  No digest was manually transcribed into the check.  The frozen Sol
report sections 2--8 and the charged Opus bridge report were read before the
drivers were changed.  No ledger, `jc2-lean`, `ideation-*`, or excluded
in-progress lane report was read or edited.

Put

```text
q=2t+1,       e=3t+1,
H_t(y)=12q^2 y^2-12q(t+1)y+(t+1)(3t+2),
A_t=Q[y]/(H_t),
d=2qy-(t+1).
```

Direct substitution gives

```text
H_t((d+t+1)/(2q))=3d^2-(t+1).                         (1.1)
```

Thus `A_t=Q[d]/(3d^2-(t+1))`.  It is a separable rank-two algebra, not
uniformly a field.  At `t=3s^2-1` it is the product obtained by `d=s` and
`d=-s`; every split calculation below is made separately on those two
factors.  Set

```text
g = et(3d+2(t+1))/(6q^3),       c=-yg.                (1.2)
```

The frozen JSON records store coefficients of `R=-E_t`.  The symbol in the
question is therefore

```text
T_(t,k)=-[X^k] sigma_t(R).                             (1.3)
```

This sign has no effect on any ideal, but it matters for the constant:
`T_(t,0)(0)=yg=-c`.

## 2. Closed coefficient-array recurrence for `T_(t,k)`

The coefficient-array identities in this section are **PROVED-HERE**.  They
turn the charged equations (6.1)--(6.4) into indexed scalar arithmetic, rather
than interpolation from fixed integers, and hide no monomial order.  The
closed high-pivot formulas (2.10)--(2.12) are consumed from the proved Laurent
spine in the charged Sol report, Section 5.1, equations (5.9)--(5.15).  This
report rechecks their norms and fixed specializations; it does not relabel
that banked symbolic derivation as new.

Write `L=X-b4`, put `u_i=q_(i,0)`, and initially retain the high variables
`u_t,...,u_(2t)` and `c_1,...,c_(t-1)`:

```text
U(X)=X^q + sum_(i=2)^(2t) u_i X^(q-i),
C(X)=X^(t-1)+sum_(j=1)^(t-1)c_j X^(t-1-j).            (2.1)
```

Let `U_m=[L^m]U(L+b4)` and `C_m=[L^m]C(L+b4)`, with an array entry understood
as zero outside its range.  Explicitly,

```text
U_m = binom(q,m)b4^(q-m)
      +sum_(2<=i<=2t, q-i>=m)
         u_i binom(q-i,m)b4^(q-i-m),
C_m = binom(t-1,m)b4^(t-1-m)
      +sum_(1<=j<t, t-1-j>=m)
         c_j binom(t-1-j,m)b4^(t-1-j-m).             (2.2)
```

The polynomial called `T` in the compact remainder formula is denoted `B`
here to distinguish it from the terminal rows.  Its integration constant is
set to zero, and its remaining coefficients and the Euler solution `S` are

```text
B_0=0,
B_(m+1)=g(3m+5)C_m/(2y(m+1)),  0<=m<=t-1,             (2.3)

S_m={3g(m+1)U_(m+1)
     +sum_(a+b=m-1)(3+2a-b)C_a B_b
     +(g b3/2)(5m+7)C_m}/(y(2m+1)),  0<=m<=2t.       (2.4)
```

To verify (2.4), use `R_0=LC` in the charged Euler identity.  Its three
bilinear terms combine as

```text
R_0 B-LR_0 B'+2LR_0'B=3LCB+2L^2C'B-L^2CB',
```

whose `L^m` coefficient is the convolution in (2.4); moreover
`C+(5/2)(LC)'` contributes `(5m+7)C_m/2`.  This is a coefficient proof for
every `m`, not a CAS pattern.

Define

```text
V=L^2C-yb3,       Y=LS-b3B-gb2,       Z=LB-gb3,
N=-VY'+V'Y+2U'Z,
P0'=(N-N(0))/(2yL),
R=VP0'-U'Y-yg=-E_t.                                  (2.5)
```

The displayed numerator `N-N(0)` is divisible by `L`.  The separate charged
`D1` evaluation, already incorporated in (2.5), gives

```text
b1=-b3(U_1+b3 C_0)/y.                                 (2.6)
```

For completeness, changing the omitted constant `B_0` by `delta` changes the
Euler right side by `delta(3LC+2L^2C')`; hence
`delta S=(delta/y)LC`, `delta Y=(delta/y)V`, and `delta Z=delta L`.
Consequently `delta N=2 delta L U'`, `delta P0'=delta U'/y`, and the two
variations in `E_t=-VP0'+U'Y+yg` cancel.  Thus the terminal family is genuinely
independent of `B_0`.  The charged gauge diagonal `q/y` is still a unit, but
need not be computed to obtain the terminal rows.

Here is the completely coefficientwise version of (2.5):

```text
V_m=C_(m-2)-yb3 delta_(m,0),
Y_m=S_(m-1)-b3 B_m-gb2 delta_(m,0),
Z_m=B_(m-1)-gb3 delta_(m,0),

N_m=-sum_(a+b=m)V_a(b+1)Y_(b+1)
    +sum_(a+b=m)(a+1)V_(a+1)Y_b
    +2sum_(a+b=m)(a+1)U_(a+1)Z_b,
(P0')_r=N_(r+1)/(2y),
R_m=sum_(a+b=m)V_a(P0')_b
    -sum_(a+b=m)(a+1)U_(a+1)Y_b-yg delta_(m,0).      (2.7)
```

All convolution indices in (2.4),(2.7) are nonnegative, and every array is
zero outside its displayed polynomial range.

### 2.1 The high-weight recursion

Order the variables

```text
z_j=c_j                    (1<=j<t),
z_j=u_j                    (t<=j<=2t),
z_(2t+1)=b2.                                         (2.8)
```

Give these spine variables the weights
`wt(c_j)=wt(u_j)=j` and `wt(b2)=2t+1`.
After weights `<j` have been solved, let `rho_j` be
`[X^(4t+1-j)]R` with `z_j=0`.  Weighted homogeneity proves that this row is
independent of every later variable and is affine in `z_j`: a later variable
has weight greater than `j`, while `z_j^2` has weight greater than `j`.
Therefore the exact induction is

```text
z_j=-rho_j/p_j.                                       (2.9)
```

For `1<=j<t`, put

```text
A_C=9j^2t+18j^2-54jt^2-81jt-26j
    +72t^3+144t^2+88t+16,
B_C=-9j^2t-10j^2+24jt^2+33jt+10j
    -12t^3-20t^2-8t,
L_C=A_C d+B_C,
p_j=3te L_C/((t+1)(3t+2)^3(4t-2j+1)).               (2.10)
```

For `t<=j<=2t`, put

```text
A_Q=12t^2+16t+4-j(3t+4),
B_Q=2(t+1)(j-t),
L_Q=A_Q d+B_Q,
p_j=-3te(q-j)L_Q/
    ((t+1)q(3t+2)^2(4t-2j+1)).                       (2.11)
```

The last diagonal is

```text
p_(2t+1)=gd/(2y)
          =te(3qd+t+1)/(6q^2(3t+2)).                 (2.12)
```

Equations (2.2)--(2.12), followed by

```text
T_(t,k)=-sum_(m>=k) binom(m,k)(-b4)^(m-k) R_m,
                                      0<=k<2t,        (2.13)
```

are the requested closed symbolic-`t` form.  Formula (2.13) is simply the
change from `L=X-b4` back to `X`.  Induction on `j` using (2.9) proves it is
the same substitution `sigma_t` as the charged Laurent/Euler spine through
band `2t`.  Section 3 proves every `p_j` is a unit for integer `t>=2`, so the
recursion terminates after exactly `2t+1` solves and (2.13) lies in
`A_t[b3,b4,u_2,...,u_(t-1)]`, as required.

### 2.2 Degrees and coefficients

Give the residual variables weights

```text
wt(b4)=1,  wt(b3)=t+1,  wt(u_i)=i  (2<=i<t).
```

Every monomial `b3^a b4^b product u_i^c_i` in `T_(t,k)`, for `k>0`, obeys

```text
(t+1)a+b+sum_(i=2)^(t-1)i c_i=4t+1-k.                (2.14)
```

For `k=0`, the same rule holds for the nonconstant part and the extra term is
`-c`.  Hence, with `W=4t+1-k`,

```text
deg_b4 <= W,
deg_b3 <= floor(W/(t+1)),
deg_(u_i) <= floor(W/i),
total degree <= W.                                   (2.15)
```

Reduction by `H_t` makes every coefficient affine in `y`.  At integer `t` the
binomials in (2.2) are integer-valued; symbolically, after the displayed unit
divisions, all coefficients lie in `Q(t)+Q(t)y`.  Clearing the finite
parameter-dependent denominator set in Section 3, together with the constant
factorial denominators of expanded binomials, gives literal polynomials in
`(t,y)`.  The support bound, before cancellations, is

```text
[z^W] 1/((1-z)(1-z^(t+1)) product_(i=2)^(t-1)(1-z^i)). (2.16)
```

No assertion that every allowed monomial occurs is needed or made.

## 3. Denominators, resultants, and split safety

This section is **PROVED-HERE** by exact algebra and the executable
`denominator_audit.py`.  For a linear class `ad+b`,

```text
Res_y(H_t,ad+b)=4q^2(3b^2-a^2(t+1)),                 (3.1)
(ad+b)^(-1)=3(b-ad)/(3b^2-a^2(t+1)).                 (3.2)
```

The elementary inverses used in (2.3)--(2.12) are

```text
y^(-1)=6q((t+1)-d)/((t+1)(3t+2)),
g^(-1)=6q^3(2(t+1)-3d)/(t(t+1)e(4t+1)),
p_(2t+1)^(-1)=6q^2(3qd-(t+1))/(t(t+1)e(4t+1)).       (3.3)
```

For `n=t-j>=1`,

```text
3B_C^2-A_C^2(t+1)=-(3t+2)^3 F_C(t,t-n),
F_C(t,t-n)=
 3n^4+24n^3t+42n^3+66n^2t^2+146n^2t+119n^2
 +72nt^3+238nt^2+234nt+104n
 +27t^4+134t^3+223t^2+136t+32.                     (3.4)
```

Every term on the last two lines is nonnegative for `t>=2,n>=1`, and the
constant part is positive.  For `n=q-j>=1`,

```text
3B_Q^2-A_Q^2(t+1)=-(t+1)(3t+2)^2 F_Q(t,q-n),
F_Q(t,q-n)=n^2+4nt+6n+4t^2-3 >= 12.                 (3.5)
```

Thus the primitive leading classes and their polynomial resultants are

| diagonal class | resultant with `H_t` | roots in its admissible integer range |
|---|---|---|
| `y` | `(t+1)(3t+2)` | none for `t>=2` |
| `3d+2(t+1)` (the class of `g`) | `12q^2(t+1)(4t+1)` | none for `t>=2` |
| `L_C` | `-4q^2(3t+2)^3 F_C(t,j)` | none for `t>=2, 1<=j<t` by (3.4) |
| `L_Q` | `-4q^2(t+1)(3t+2)^2 F_Q(t,j)` | none for `t>=2, t<=j<=2t` by (3.5) |
| `3qd+(t+1)` | `-12q^2(t+1)(3t+2)(4t+1)` | none for `t>=2` |

The additional residual-axis coefficient used in Section 6 has primitive
linear class

```text
A_b d+B_b,
A_b=27t^3-30t^2+t-2,   B_b=6t^3+13t^2-3t+2,
```

and exact resultant

```text
-4q^2(t-2)(3t-1)^2(3t+2)(27t^3+17t^2+t+2).          (3.6)
```

It is nonzero for every integer `t>=3`: every factor is then positive except
the displayed leading minus sign.  Its sole admissible boundary zero is
`t=2`, which is treated factorwise in Section 6.

For literal completeness, the resultants of the actual leading coefficients,
rather than only their primitive linear classes, are

```text
Res(H_t,g)=t^2e^2(t+1)(4t+1)/(3q^4),
Res(H_t,p_C)=-36q^2t^2e^2 F_C /
 ((t+1)^2(3t+2)^3(4t-2j+1)^2),
Res(H_t,p_Q)=-36t^2e^2(q-j)^2 F_Q /
 ((t+1)(3t+2)^2(4t-2j+1)^2),
Res(H_t,p_b2)=-t^2e^2(t+1)(4t+1)/(3q^2(3t+2)).       (3.7)
```

Their numerator roots and denominator poles have the same empty admissible
set.  The complete list of parameter-dependent rational factors is

```text
2, 3, 6, q, q^2, q^3, t, e, t+1, 3t+2, 4t+1,
m+1 (0<=m<t), 2m+1 (0<=m<=2t),
4t-2j+1 in the ranges of (2.10),(2.11),
q-j (t<=j<=2t), F_C, F_Q.                            (3.8)
```

The axis formula adds only `3t-1` to this denominator list.

The only integer roots among the unindexed linear denominator factors in
(3.8) are `t=0` (the factor `t`) and `t=-1` (the factor `t+1`); their other
linear roots are nonintegral.  The indexed odd factor `4t-2j+1` cannot be zero and is
positive in its stated ranges, while `1<=q-j<=t+1`.  Equations
(3.4)--(3.5) exclude all admissible roots of `F_C,F_Q`.  Thus the
specialization-exception set for integer
`t>=2` is empty.  The infinite split set `t=3s^2-1` is not put into a
denominator: (3.1) proves the pivot is a unit on both factors.

## 4. Controls for the recurrence

The new Singular driver performs the equivalent full `B0,b1` Laurent
recurrence and checks every affine pivot row before substitution.  Its exact
output agrees, with the sign (1.3), with every terminal coefficient in the
banked JSON at `t=2,3,4,5`.
The `t=5` source hash is independently authenticated by the charged status
record.  At `t=6` the driver emitted all twelve exact characteristic-zero rows
over `Q[y]/(H_6)`.  Separately regenerated modular rows on both roots of
`H_6 mod 1009` agree coefficientwise with the two banked modular JSON records;
this is not presented as a direct polynomial reduction of the exact dump.

An independent implementation of the convolution formulas (2.2)--(2.13)
used seed `160903`, three residual points per fibre, and both roots of `H_t`
modulo `1009` for every `t=2,...,6`.  At every one of the ten `(t,fibre)`
cases it checked every high diagonal against (2.10)--(2.12) and every one of
the `2t` terminal values against the banked modular row.  All ten cases report
`PASS_RECORD`.

The exact/finite degree sequences are

```text
deg T_(t,k)=4t+1-k, k=0,...,2t-1, for t=2,...,6,
deg_y(coefficient)<=1,
```

where the equality is a finite control and (2.14)--(2.15), not equality, is
the uniform theorem.

At the first split index,

```text
A_2 = Q[y]/((5y-1)(5y-2)) = Q x Q,
```

the exact recurrence and both terminal chart tests were run separately at
`y=1/5` and `y=2/5`; every high pivot was nonzero and `TOP-TAIL-UNIT` and the
full `b4=0` unit test passed on both factors.  No element of the unsplit
rank-two algebra was inverted.

At the next split index `t=11`, `d=+2,-2`, equivalently
`y=7/23,5/23`.  Modulo `1009` these are `y=439,746`.  Five deterministic
residual points on each factor completed the coefficient recurrence, matched
every measured high diagonal to (2.10)--(2.12), killed all high bands, and
emitted all 22 terminal values.  There is no independent `t=11` terminal
record comparison.  This is a formula/split-safety control only; it is not an
ideal test and is labelled **MEASURED-MODULAR**.
For completeness, a direct positive-row `dp/std` job was then attempted on
the first fibre.  It hit its hard 600-second bound with exit code 124 and no
basis or radical verdict; the second fibre was not run after that timeout.
The exact label is `INCONCLUSIVE_TIMEOUT`, not failure or success of the
lemma, and the status JSON retains both independently emitted fibre systems.

## 5. `TOP-TAIL-UNIT`

Set `b4=1`.  Vanishing of bands `t,...,2t-1`, after the high recursion, says
that `deg_X E_t<t`.  The requested universal conclusion is still

```text
OPEN[TOP-TAIL-UNIT]:
 <T_(t,t),...,T_(t,2t-1)>=[1]
 in A_t[b3,u_2,...,u_(t-1)] for every t>=2.           (5.1)
```

### 5.1 Exact advance at `t=5`

The charged `t=5` JSON has SHA-256
`f68a4666afb25490ceb62ec2b2f9ebe9b22b61c415cbf66edc074eb50a650689`,
exactly the hash recorded in the frozen status input.  Under

```text
d=22y-6,       A_5=Q[d]/(d^2-2),
```

the five rows at bands `5,...,9`, with `b4=1`, were made primitive in the
declared ring

```text
ring R=(0,d),(b3,q2_0,q3_0,q4_0),dp;  minpoly=d2-2;
```

Singular `modStd(I,1)` returned the reduced basis `G[1]=1` in 13.10 seconds,
with empty stderr.  The local library documents exactness flag `1` as computing
a standard basis "for sure" and invokes its final exact verification.  This is
therefore **PROVED-HERE in characteristic zero**, and supersedes the charged
timeout (which used a less favorable coefficient presentation).

At `t=6`, the tau-free recurrence likewise passed over the integral model
`Q[a]/(a^2-21)`, `d=a/3`, and emitted the six exact top rows.  The subsequent
exact `modStd(I,1)` call hit its hard 1800-second bound with exit 124, empty
stderr, and no `UNIT` or `NONUNIT` line.  Its mathematical status is therefore
**INCONCLUSIVE_TIMEOUT**, not nonunit.

### 5.2 Why the proposed affine triangle is not yet present

In the residual auxiliaries every original top row is nonlinear in every
original variable.  The exact per-variable degrees, with entries ordered by
ascending band, are

| `t` | variables | degree vectors by band |
|---:|---|---|
| 3 | `(b3,u2)` | `(2,5),(2,4),(2,4)` |
| 4 | `(b3,u2,u3)` | `(2,6,4),(2,6,4),(2,5,3),(2,5,3)` |
| 5 | `(b3,u2,u3,u4)` | `(2,8,5,4),(2,7,5,3),(2,7,4,3),(2,6,4,3),(2,6,4,3)` |

Thus no permutation of the original rows and variables even has an initial
affine-unit pivot.  Modular subsystem audits on one `H_t` fibre give the
following zero-dimensional lengths after the first `t-1` rows; only adding
the final row produces `[1]`:

| `t` | ascending bands | descending bands |
|---:|---:|---:|
| 3 | 10 | 8 |
| 4 | 57 | 44 |
| 5 | 298 | 224 |

Removing any one top row at `t=3,4,5` also leaves a nonzero zero-dimensional
ideal; at `t=5` this leave-one-out check was repeated on both fibres.  Thus
none of these records supplies the requested induction "one
original row introduces one auxiliary with a unit affine coefficient".  A
nonlinear triangular change may exist, but it has not been derived.  Calling
the final Gröbner reduction a uniform triangle would violate the indexed-
recurrence guardrail.

### 5.3 Exact determinant reduction of the open step

Put `F_r=T_(t,t+r)|_(b4=1)` for `0<=r<t`, choose
the cheaper measured prefix `J_t=<F_1,...,F_(t-1)>`, and set
`B_t=A_t[b3,u_2,...,u_(t-1)]/J_t`.  If `B_t` is first proved finite over
`A_t`, the finite-algebra multiplication criterion gives, componentwise in
the separable rank-two algebra,

```text
<F_0,...,F_(t-1)>=[1]
 iff multiplication by F_0 on B_t is bijective
 iff Delta_t=det(mu_(F_0)) is a unit in A_t.           (5.2)
```

At a split index the two determinants must be checked at `d=+s,-s`; one may
not invert their product in advance.  For a displayed class
`Delta_t=a_t d+b_t`, the single split-safe norm condition is
`4q^2(3b_t^2-a_t^2(t+1))!=0`.  What remains is exactly

```text
OPEN[TOP-TAIL-DETERMINANT-RECURRENCE]:
 prove B_t finite, construct an indexed A_t-basis and recurrence for Delta_t,
 and prove its norm has no admissible integer zero.                  (5.3)
```

The fixed lengths `8,44,224` at `t=3,4,5` do not prove the first clause
uniformly; no extrapolation from those three values is made.

## 6. `RESIDUAL-ZERO`

At `b4=0`, (2.14) proves every positive-band row vanishes at the residual
origin.

### 6.1 A uniform `b3`-axis calculation

Set all `u_2,...,u_(t-1)` to zero as well.  The weight induction (2.8)--(2.9)
then leaves exactly

```text
C=X^(t-1),
U=X^(2t+1)+a b3 X^t,       b2=0,
a=-(6dt-3d+9t^2+2t-1)/(6t(3t-1)).                  (6.1)
```

Indeed, a solved high variable of weight `j` can be nonzero on this axis only
when `j` is a multiple of `wt(b3)=t+1`; in the high range the sole possibility
is `u_(t+1)`.  Its affine pivot equation gives the displayed `a`; the final
weight `2t+1` cannot occur, so `b2=0`.  Substitution of (6.1) in the indexed
arrays (2.3)--(2.7), and extraction at weight `2t+2`, gives for the stored sign
`R=-E_t`

```text
[X^(2t-1)]R = lambda_b b3^2,
lambda_b = t(3t+1)(A_b d+B_b)/
           (12(2t+1)^2(3t-1)^2(3t+2)).              (6.2)
```

This coefficient extraction is an identity in `Q(t)[d]/(3d^2-t-1)`, not a
fit to fixed values.  Resultant (3.6) proves `lambda_b` is a unit for every
integer `t>=3`, on both factors at every split index.  Consequently the image
of the positive-row ideal on the `b3`-axis has radical `(b3)`.  This is only a
coordinate-axis statement: it does **not** imply a power of `b3` belongs to
the original multivariable ideal.  The bounded exact driver
`residual_b3_axis_exact_audit.py` asserts the high solve, coefficient reduction,
and resultant factorization symbolically; its output explicitly labels the
claim axis-only.

### 6.2 Exact fixed-`t` radical certificates

Exact standard bases give the following pure-power containments in the
positive-band ideal `I_(t,+)`:

| `t` | coefficient algebra | basis size | checked powers lying in `I_(t,+)` |
|---:|---|---:|---|
| 3 | `Q[y]/(H_3)` | 4 | `b3^3, u2^6` |
| 4 | `Q[y]/(H_4)` | 17 | `b3^4, u2^8, u3^6` |
| 5 | `Q[y]/(H_5)` | 63 | `b3^5, u2^13, u3^9, u4^7` |
| 6 | `Q[y]/(H_6)` | 253 | `b3^5, u2^16, u3^11, u4^8, u5^7` |

Each reduction was zero in the displayed characteristic-zero algebra.  Since
all generators vanish at the origin and a power of every residual variable
lies in the ideal, these checks prove exactly

```text
sqrt(I_(t,+))=(b3,u_2,...,u_(t-1))  for t=3,4,5,6.   (6.3)
```

The `t=5,6` instances are new exact promotions.  They remain fixed-integer
proofs, not an induction, and the varying exponents do not define a uniform
recurrence.

There is a useful correction at `t=2`.  The positive rows are not literally
all zero in `A_2`: the stored band-three row at `b4=0` is

```text
28(5y-1)b3^2/625
```

for `R=-E`.  It is zero on the `y=1/5` factor and a unit times `b3^2` on the
`y=2/5` factor.  Therefore the proposed radical equality is still false in
the product algebra, while the band-zero row is a unit on both factors and
closes that chart exactly.

### 6.3 An exact recurrence for the `u_2`-axis obstruction

There is also a **PROVED-HERE** indexed reduction of the next axis calculation,
although its final norm is not yet factored.  Put `h=X`, `z=u_2`,
`s=z/h^2`, `Theta=s d/ds`, and `Delta_n=n-2Theta`.  Over
`K_t=Q(t)[d]/(3d^2-t-1)`, grading forces

```text
C=h^(t-1) chi(s),       U=h^q upsilon(s),
chi_0=1,                upsilon_0=upsilon_1=1.
```

The only high unknowns are `chi_r` for
`1<=r<=floor((t-1)/2)` and `upsilon_r` for
`ceil(t/2)<=r<=t`; odd-weight high variables and `b2` vanish.  With products
interpreted as coefficient convolutions and truncated through weight `2t+2`,
define

```text
beta_r=g(3t+2-6r)chi_r/(2y(t-2r))
       (0<=r<=floor((t-1)/2)), and beta_r=0 otherwise,
f=3g Delta_q(upsilon)+chi beta-chi Delta_t(beta)
  +2 Delta_t(chi) beta,
delta_r=f_r/(y(4t-4r+1)),
xi={Delta_(t+1)(chi) delta-chi Delta_q(delta)
    +2 Delta_q(upsilon) beta}/(2y),
rho=chi xi-Delta_q(upsilon) delta.                    (6.4)
```

These are exactly `B=h^t beta`, `S=h^(2t)delta`,
`P0'=h^(3t)xi`, and `R=-yg+h^(4t+1)rho(s)` in the nonconstant range.
Triangularly, set
`chi_r=-rho_r|_(chi_r=0)/p_C(t,2r,d)` in the first range and then
`upsilon_r=-rho_r|_(upsilon_r=0)/p_Q(t,2r,d)` in the second.  This kills
`rho_1,...,rho_t` and leaves

```text
lambda_2(t,d)=rho_(t+1),
[X^(2t-1)]R=lambda_2(t,d) u_2^(t+1) on this axis.     (6.5)
```

All pre-pivot scalar denominators are safe: `t-2r>=1` in the beta range and
`4t-4r+1>=1` where `f_r` can occur.  Writing the reduced output as
`lambda_2=(A(t)d+B(t))/D(t)` turns its remaining unit test into the univariate
identity

```text
Res_y(H_t,A(t)d+B(t))=4q^2(3B(t)^2-(t+1)A(t)^2).      (6.6)
```

The recurrence is a valid finite certificate format, but neither `D(t)` nor
the norm polynomial in (6.6) has been obtained in closed form.  As with
Section 6.1, an axis calculation alone is not a containment in the full ideal.

The universal statement remains

```text
OPEN[RESIDUAL-ZERO-UNIFORM]: prove (6.3) for every t>=3. (6.7)
```

The missing step is now precise: exhibit, by an index induction, `b3^N` in
`I_(t,+)` and then a power of `u_j` modulo
`(b3,u_(t-1),...,u_(j+1))`, with each coefficient's norm nonzero.  The
finite exponents above show that guessing a sharp pure-power exponent from
`t=3,4,5` is unsafe (`b3^5`, not first `b3^6`, already occurs at `t=6`).

## 7. Assembly and exact theorem status

Let `I_t=<T_(t,0),...,T_(t,2t-1)>`.  If the `b4=0` chart is unit, then `b4`
is invertible in the quotient by `I_t`, because `(I_t,b4)=[1]`.  If the
dehomogenized `b4=1` chart is unit, choose a finite certificate
`1=sum a_k T_(t,k)|_(b4=1)` among the weighted-homogeneous top rows.
Homogenizing that certificate to a common weight gives `b4^N in I_t`, so
`b4` is nilpotent in the same quotient.  An element cannot be both invertible
and nilpotent in a nonzero ring, hence `I_t=[1]`.  This is the standard
two-chart cover, with no saturation component suppressed.

For every `t>=3`, the uniform residual lemma (6.7), if proved, would make the
first chart unit: modulo its positive rows the residual maximal ideal is
nilpotent, while `T_(t,0)` has unit constant `-c=yg`.  The `t=2` first chart
is already closed separately as in Section 6.2.

At `t=5`, Section 6 plus `T_(5,0)(0)=-c` makes the `b4=0` chart unit, and
Section 5 proves the `b4=1` chart unit.  Hence

```text
<T_(5,0),...,T_(5,9)>=[1] in A_5[b3,b4,u2,u3,u4].    (7.1)
```

Together with the banked exact cases, theorem (T) on this ray is now proved
for `t=1,2,3,4,5`.  `RESIDUAL-ZERO` also closes the `b4=0` half at `t=6`.
The exact `t=6` top-tail run is inconclusive as recorded in Section 5, so
(8.1) is not promoted at `t=6` here.

Consequently the requested all-`t` verdict is **PARTIAL**, not
`PROVED-HERE`.  The exact unresolved mathematical content is the pair
(5.1),(6.7), or any direct indexed identity implying `I_t=[1]` for all
integers `t>=2`.

## 8. Cheapest next proof/test

The cheapest proof target is no longer expansion of `sigma_t`: Section 2 has
removed it.  For `TOP-TAIL-UNIT`, first prove that a selected `t-1`-row
subideal has finite quotient, and then compute the determinant of
multiplication by the omitted row.
The finite lengths in Section 5 show exactly what must be controlled.  A
usable certificate is a recurrence for that determinant (or for a nonlinear
triangular basis) together with its resultant against `3d^2-(t+1)`; a generic
CAS answer without its specialization denominator is insufficient.

For `RESIDUAL-ZERO`, specialize `b4=0` in (2.2)--(2.13) before expanding and
derive the successive one-variable coefficient modulo
`(b3,u_(t-1),...,u_(j+1))`.  The cheapest falsification test is the two-factor
`t=11` job (`d=+2,-2`) modulo a good prime, checking those reductions rather
than a full lexicographic radical.  Section 6.1 finishes the first coordinate
axis, and Section 6.3 supplies the exact recurrence for the next.  The cheapest
remaining symbolic job is to execute that recurrence in coefficient pairs,
factor `D(t)` and the norm in (6.6), and check their integer roots.

## 9. FALLACY-v2 audit

- `A_t` is always called a rank-two algebra.  Split indices are evaluated in
  both factors; no zero divisor is inverted.
- Every division in the main terminal recurrence is indexed in (3.3)--(3.8);
  the extra axis denominators are checked in Sections 6.1 and 6.3.  No fixed
  sample is used as an all-`t` denominator check.
- The exact `t=5,6` computations are explicitly fixed-specialization proofs.
  Modular and random-point checks are not promoted across characteristic and
  are not called unit certificates.
- The two-chart assembly states the actual ring and explains both localization
  directions.  No bare `sat()` output is used.
- A prime denotes differentiation only in the displayed polynomial formulas;
  the finite-field prime is always written `p` or `mod 1009`.
- No exit-price assertion is introduced, so no `charge_basis` line is
  applicable.

## 10. Reproduction and artifacts

Primary drivers and outputs are under
`box/k16terminal-sol56-20260903/`:

```text
cd box/k16terminal-sol56-20260903
bash verify_charged_inputs.sh \
  ../../xmodel/k16-terminal-proof-sol56-20260903.run.v2
python3 denominator_audit.py
python3 residual_b3_axis_exact_audit.py
python3 terminal_array_recurrence.py --t 2 3 4 5 6 \
  --prime 1009 --points 3 --records ../k16spine-20260903
python3 singular_terminal_driver.py 2 --mode split-exact --branch 0 \
  --charts all --compare-record /tmp/jc2-lane.8Syavm/inputs/terminal_laurent_t2.json --run
python3 singular_terminal_driver.py 2 --mode split-exact --branch 1 \
  --charts all --compare-record /tmp/jc2-lane.8Syavm/inputs/terminal_laurent_t2.json --run
python3 singular_terminal_driver.py 3 --mode exact --charts all \
  --compare-record ../k16spine-20260903/terminal_laurent_t3.json --run
python3 singular_terminal_driver.py 4 --mode exact --charts all \
  --compare-record ../k16spine-20260903/terminal_laurent_t4.json --run
python3 singular_terminal_driver.py 5 --mode exact --charts residual \
  --compare-record ../k16spine-20260903/terminal_laurent_t5.json --run
python3 top_tail_exact_replay.py ../k16spine-20260903/terminal_laurent_t5.json \
  top_tail_t5_exact.sing --run --metadata top_tail_t5_exact.json
python3 top_tail_fast_recurrence.py 6 --mode exact --chart top --run \
  --timeout 1800 --stem top_tail_fast_t6_exact_integral
python3 singular_terminal_driver.py 6 --mode exact --charts residual \
  --algorithm modstd --run
python3 terminal_array_recurrence.py --t 11 --prime 1009 --points 5
python3 validate_claim_artifacts.py
python3 build_artifact_manifest.py
```

`claim_status.json` is the typed result summary; `artifacts.sha256` and
`artifact_summary.json` record exact sizes and digests.  Empty stderr, ring
maps, branch values, basis sizes, and timeouts are retained next to each run
rather than inferred from filenames.

<!-- BODY-END -->
