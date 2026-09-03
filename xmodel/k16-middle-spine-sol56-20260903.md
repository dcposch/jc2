# K=16 middle-spine audit on the normalized ray

Date: 2026-09-03.  Charged lane: `k16-middle-spine-sol56-20260903`.

## Verdict

**PARTIAL.  The theorem (T) for every positive integer `t` is not proved
here.**  This audit proves the uniform post-`H/c` row skeleton, gives a compact
closed polynomial form for every row, proves the `2t` zero/duplicate
recurrence, and proves a split-safe **second affine spine for every `t>=2`**
by an alternative Laurent/Euler recurrence; the exceptional
`t=1` fibre is already killed by the banked four-pivot-plus-unit audit.  It
also finds a genuine
obstruction to the originally proposed unbranched charged-coordinate order:
on every split index

```text
t = 3s^2-1
```

the scheduled high scalar pivot in offset `s` is a nonzero zero divisor of
`A_t`.  At `t=2` the deterministic unit-deferral computation repairs this by
a later unit pivot.  The proof spine below bypasses every such pivot and has
uniformly nonzero norms.  The terminal ideals are exactly unit ideals for
`t=1,2,3,4`; the finite `t=5,6` results below are typed separately.  No
induction proving the terminal ideal `[1]` for arbitrary `t` was found.

Thus this file says `PROVED-HERE` for the `t>=2` second affine spine, but does **not**
say `PROVED-HERE` for (T).  The sole residual statement and its cheapest exact
test are in section 8.

## 1. Frozen inputs and typing

The receipt was parsed mechanically: its `lane_inputs_dir`,
`charged_input_i_basename`, and `charged_input_i_sha256` fields generated
`box/k16spine-20260903/charged_inputs.sha256`.  Running

```text
sha256sum -c box/k16spine-20260903/charged_inputs.sha256
```

returned `OK` for all 15 charged files.  No hash was transcribed into the
check command.  All new drivers and finite artifacts are confined to
`box/k16spine-20260903/`; no ledger was edited.

Throughout,

```text
q=2t+1,  e=3t+1,
H_t(y)=12q^2 y^2-12q(t+1)y+(t+1)(3t+2),
A_t=Q[y]/(H_t).
```

The map to the charged chart keeps the charged generator names and order.
The weighted slice is `x=q_(t+1),1 -> 1`,
`y=q_(2t+1),1 -> y`, and

```text
g=g_3=t(3t+1)(6qy-(t+1))/(6q^3),
c=-yg=t(3t+1)y((t+1)-6qy)/(6q^3).
```

All quotient reductions in this audit are polynomial remainders modulo the
displayed `H_t`.  An element is inverted only after an extended-gcd check;
this remains valid when `A_t` is a product algebra.

It is useful to put

```text
d=2qy-(t+1).
```

Direct substitution, without division in `A_t`, gives

```text
H_t((d+t+1)/(2q)) = 3d^2-(t+1).
```

Consequently, for a linear form `a d+b`,

```text
Res_y(H_t, a d+b)=4q^2(3b^2-a^2(t+1)).                 (1.1)
```

Rational rescaling changes this resultant by a nonzero square and never its
vanishing.  Formula (1.1) is the unit test used below.

## 2. A compact, exact h-adic identity

This is the main structural advance.  It replaces tens of thousands of
expanded terms by four coefficient polynomials and is verified by direct
symbolic expansion in `compact_remainder.py`.

Use an independent variable `X` for `h`, and let `U,R,V,S,T` be polynomials
in `X`.  After the already proved constant spine every normalized expression
has the form

```text
Q=U(X)+A R(X)+yB,
P=V(X)+A S(X)+B T(X)+g z.                              (2.1)
```

Write `L=X-b4` and localize temporarily at `p=pi`.  The charged definitions
give identities in the Laurent polynomial ring, not assumptions:

```text
A=L/p,
B=L/p^2-b3/p,
z=-b1-b2/p-b3/p^2+L/p^3.
```

Hence (2.1) is

```text
Q=U+Q1/p+Q2/p^2,
P=P0+P1/p+P2/p^2+P3/p^3,                              (2.2)

Q1=LR-yb3,       Q2=yL,
P0=V-gb1,        P1=LS-b3T-gb2,
P2=LT-gb3,       P3=gL.
```

Here a prime means `d/dX`; it is not a label.  Since the coordinate
Jacobian is `J(X,p)=-p^3`, coefficient comparison in (2.2) says that
`J(Q,P)=c gamma` is exactly the following five polynomial identities:

```text
D0 = Q1 P0' - U' P1                                      = -c,
D1 = 2Q2 P0' + Q1 P1' - Q1'P1 - 2U'P2                   = -cb1,
D2 = -3U'P3 + Q1P2' - 2Q1'P2 + 2Q2P1' - Q2'P1          = -cb2,
D3 = Q1P3' - 3Q1'P3 + 2(Q2P2' - Q2'P2)                 = -cb3,
D4 = 2Q2P3' - 3Q2'P3                                    = cL.       (2.3)
```

There was no division by `p` in the conclusion: multiply by the needed
power of `p` and compare Laurent coefficients, so (2.3) is an identity in
the declared polynomial coefficient ring.

In the charged `(gamma-degree,pi-degree)` tags, direct reduction of (2.1)
also gives four independent polynomials

```text
C12=-RT+L(RT'-2R'T+2yS')+yS-b3(gR'+yT')-3gU',
C11=-2gR+L(2yT'-3gR'),
C00=L^2(R'S-RS')
    +L{b3(R'T-yS')+2b2(gR'-yT')+2TU'-2yV'}
    +gb3^2R'+gb2R+gb3U'+b1gy,
C01=(b3y-LR)V'+(LS-b3T-b2g)U'+gy
     -b2 C12-b1 C11.                                  (2.4)
```

The remaining tags satisfy the universal syzygies

```text
C03=-C12,
C02=-b1 C12-C11,
C10=-yg.                                               (2.5)
```

The script expands the six charged brackets, reduces by the monic relation
`h(pi,gamma)-X`, verifies that exactly the seven expected tags occur, and
checks (2.4)-(2.5) to zero over a polynomial ring with independent symbols.
This is a proof of the identities, not fixed-`t` interpolation.

Two immediate consequences of (2.3) are

```text
c=-yg,
R=LC,
T'=(g/(2y))(5C+3LC')                                  (2.6)
```

for a polynomial `C`: the constant term of `C11=0` first gives `R(b4)=0`,
and coefficient comparison in `L` then gives (2.6).  Both `y` and `g` are
units in `A_t`, so this division is legitimate, including on split fibers.

## 3. Exact post-H/c support and the duplicate recurrence

The degree bounds in (2.4), together with the charged coefficient-space
boundaries, give the following support after imposing `H_t`, `c=-yg`, and
`x=1`:

| bands | tags present | rows |
|---|---|---:|
| `0 <= k < t` | `12,11,02,01,00` | `5t` |
| `t <= k < 2t` | `12,02,01,00` | `4t` |
| `k=2t` | `01,00` | `2` |

Thus the post-`H/c` system has exactly `9t+2` rows in the known `6t+2`
auxiliaries.  This derives the previously observed count for arbitrary `t`.
The two moving boundaries are visible: `C11` stops at `t-1`, while `C12`
stops at `2t-1`.

Take coefficients in descending `L`-degree (equivalently, once higher
coefficients have vanished, in descending `X`-degree).  Retain `C12`, then
`C11`, at each band.  Formula (2.5) gives

```text
[L^k]C02=-b1[L^k]C12-[L^k]C11.
```

For `k>=t`, the second term is absent or is the already imposed `H_t` row;
for `k<t` both retained coefficients have just vanished.  Therefore every
one of the `2t` tag-`02` rows reduces exactly to zero.  The tag-`03` copy was
already removed as the rational associate `-C12`.  This proves the observed
zero/duplicate recurrence for all `t`; it does not depend on a Gröbner basis
or on samples.

For `t>=2`, the row count after the affine eliminations is consequently

```text
(9t+2)-(5t+2)-2t = 2t,
```

and the only possible survivors are tag `01` in bands `0,...,2t-1`.

## 4. Canonical second-spine order

For `t>=2`, the deterministic order used for comparisons is:

1. bands `k=2t,2t-1,...,0`;
2. at `k=2t`, tag `01` followed by tag `00`;
3. below `2t`, tag `12`, then tag `11` when present, then tag `00`;
4. a nonunit candidate is deferred without inversion, and the scan restarts
   at the first pending unit in this same priority list;
5. variables use the numerical order `a(i,j)`, then `q(i,j)`, then `b_i` only
   to break ties not fixed by the following explicit schedule.

The scheduled variables are

```text
k=2t, tag 01:              a_(2t+1),0
k=0,...,2t, tag 00:       b1 (k=0), b2 (k=t), a_(e-k),0 otherwise
k=0,...,t, tag 12:        q_(2t-k),0
k=t+1,...,2t-1, tag 12:   q_(e-k),1
k=1,...,t-1, tag 11:      a_(t-k),0
k=0, tag 11:              q_q,0.                       (4.1)
```

There are `1+(2t+1)+2t+t=5t+2` scheduled pivots.  If all exist as units,
the remaining variables, in canonical names, are

```text
b3,b4,q_2,0,...,q_(t-1),0,                             (4.2)
```

exactly `t` variables.

## 5. Pivot coefficients and a proved split-safe spine

The top-face recurrence is the coefficient recurrence for

```text
G(Z)=(1+Z+yZ^2)^(e/q)=sum_(n>=0) g_n Z^n:
q(n+1)g_(n+1)=(e-qn)g_n+y(2e-q(n-1))g_(n-1).          (5.1)
```

It gives `g4=0` modulo `H_t` and

```text
g5=-yg3/(5q)
  =-t(t+1)(3t+1)(5d+2t+3)/(60q^5).                    (5.2)
```

Thus `g5` is a unit.  For the cleared numerator its resultant is

```text
4t^2(t+1)^2q^2(3t+1)^2(3t+2)(4t+1),                  (5.3)
```

which never vanishes at a positive integer.

Exact Schur elimination and the band recurrence identify the following
primitive-associate classes.  The symbol `~` means multiplication by a
nonzero rational number, harmless for the unit test.

| family / band | pivot class | resultant of displayed class |
|---|---|---|
| top endpoint | `1` | `1` |
| tag `12`, `t<k<2t` | `d` | `-4q^2(t+1)` |
| tag `12`, `k=t` | `3d+1` | `-12q^2(3t+2)` |
| tag `00`, `k=t+s`, `1<=s<=t` | `d+s` | `4q^2(3s^2-(t+1))` |
| tag `00`, `k=t` (`b2`) | `2d+1` | `-4q^2(4t+1)` |
| tag `00`, `0<k<t` | `y` | `(t+1)(3t+2)` up to leading-factor convention |
| tag `00`, `k=0` (`b1`) | `5d+2t+3` | `4q^2(3t+2)(4t+1)` |
| tag `11`, `k=0` | `3d+2(t+1)` | `12q^2(t+1)(4t+1)` |

These account for `3t+3` of the `5t+2` scheduled positions before split
deferrals.  All displayed resultants are nonzero for `t>=2` except precisely

```text
d+s at t=3s^2-1.                                      (5.4)
```

Equation (5.4) is not a removable denominator accident: in
`A_t ~= Q x Q` it vanishes on one factor.  Inverting it would discard a
component and violate FALLACY-v2.  The `t=2,s=1` record shows the safe
behavior: the candidate `5y-1` has resultant zero, is deferred, and a later
row pivots on `39y-10`, whose resultant is nonzero.

The original charged-coordinate order still has unclassified generic lower
positions: the `t` lower tag-`12` pivots and `t-1` lower tag-`11` pivots, as
well as a changing deferred replacement for (5.4).  That is a defect of that
coordinate order, not an obstruction to the quotient.  The following
recurrence supplies a different canonical proof order and closes the spine.

### 5.1 Laurent/Euler proof order

Use (2.6), put `R=LC`, and write the scalar part of `Q` as

```text
U=h^q+sum_(i=2)^(2t) q_i h^(q-i),
C=h^(t-1)+sum_(j=1)^(t-1) C_j h^(t-1-j).              (5.5)
```

The `C11` coefficients determine the nonconstant coefficients of `T` by

```text
T'=(g/(2y))(5C+3LC'),                                  (5.6)
```

leaving only `T(0)`.  The `C12` coefficients determine `S` by the diagonal
Euler inverse

```text
y(1+2L*d/dL)S
 =3gU'+RT-LRT'+2LR'T+gb3(R/L+5R'/2).                  (5.7)
```

More explicitly, if `C=sum c_m L^m` and the right side of (5.7) is
`sum e_m L^m`, coefficient comparison gives the band recurrences

```text
[L^(m+1)]T = g(3m+5)c_m/(2y(m+1)),
[L^m]S     = e_m/(y(2m+1)).                           (5.7b)
```

Thus induction on increasing `m` reconstructs every nonconstant coefficient
of `T` and every coefficient of `S`; each diagonal is a unit.  The next
identity first solves its divisibility condition and then reconstructs the
scalar polynomial `V` from `V'` coefficientwise; its integration constant is
the charged zero constant of `V`.  Conversely these steps reconstruct a
unique charged `P`.  Thus the combined `D3,D2,D1` reconstruction, including
(5.6)-(5.7), eliminates exactly the old `3t-1` scalar-`P` coordinates.  The
count is transparent on the other side: (5.5), `T(0)`, and
`b1,b2,b3,b4` leave `3t+3` variables from the original `6t+2`.

The reconstruction also lands in the monic charged chart, rather than only
in an unrestricted polynomial space.  With `g1=e/q` and the charged `g2`,
the three leading-coefficient checks are

```text
(3t+2)g-2t*y*g2 = -t(3t+1)H_t/(6q^3),
3q*g+(t+1)g2    = (4t+1)y*g1,
2q*g2-t*g1      = 2e*y.                              (5.7a)
```

The first vanishes in `A_t` and the other two are rational identities.  They
give respectively the prescribed leading terms of `T`, `S`, and `V'`.

Every change is triangular with coefficient `g`, `2my`, or `(2m+1)y`.
Multiplying the Laurent identity by a power of `p` gives mutually inverse
polynomial coefficient maps, so this is a solution-functor/quotient-ring
isomorphism; it is neither a projection nor saturation by `p`.

There are only two primitive quotient classes among these reconstruction
diagonals:

```text
y,                 Res_y(H_t,y)=(t+1)(3t+2),
3d+2(t+1),         Res_y(H_t,3d+2(t+1))
                     =12q^2(t+1)(4t+1).              (5.7c)
```

The second is a rational associate of `g`.  Integer multiples of the first
cover `2my` and `(2m+1)y`; hence every reconstruction pivot has a nonzero
norm for its stated index range.

The `D1` divisibility condition solves `b1` with coefficient `yg=-c`.
The gauge `alpha_t=0`, namely `[h^(q-1)]V'=0`, then solves `T(0)` with
coefficient `q/y`.  Both are units.  After these two substitutions,
coefficients of the convenient terminal associate
`-E_t` in descending degree `4t,...,2t` eliminate

```text
C_1,...,C_(t-1), q_t,...,q_(2t), b2                  (5.8)
```

in increasing weight.  There is exactly one new variable in each weight
`j=1,...,2t+1`.  Its affine coefficient has weight zero, so it cannot depend
on any positive-weight residual variable.  It is therefore equal to its
linearization at the homogeneous origin.  This observation turns the
following symbolic linear calculation into the exact nonlinear pivot, not
merely a tangent heuristic.

This is also the band induction requested in the lane.  After step `j-1`,
the coefficients of `-E_t` in degrees `4t,...,4t-j+2` vanish and precisely
the first `j-1` variables in (5.8) have been solved.  The next coefficient is
affine in the next variable, its already-solved part lies in the preceding
substitution ring, and its diagonal is `p_C(t,j)`, `p_Q(t,j)`, or `p_b2`
below.  Unitness of that diagonal proves the induction step.  At `j=2t+1`
all coefficients through degree `2t` vanish and exactly the `t` variables
(4.2) remain.

For `1<=j<=t-1`, define

```text
A_C=9j^2t+18j^2-54jt^2-81jt-26j
    +72t^3+144t^2+88t+16,
B_C=-9j^2t-10j^2+24jt^2+33jt+10j
    -12t^3-20t^2-8t,
L_C=A_C d+B_C.                                         (5.9)
```

The pivot on `C_j` is

```text
p_C(t,j)=3t(3t+1)L_C /
          ((t+1)(3t+2)^3(4t-2j+1)).                   (5.10)
```

Its linear norm factor is

```text
3B_C^2-A_C^2(t+1)=-(3t+2)^3 F_C(t,j).
```

Putting `n=t-j` gives the manifestly positive expression

```text
F_C(t,t-n)=
 3n^4+24n^3t+42n^3+66n^2t^2+146n^2t+119n^2
 +72nt^3+238nt^2+234nt+104n
 +27t^4+134t^3+223t^2+136t+32.                       (5.11)
```

Here `t>=2` and `n>=1`; every term is nonnegative and the constant term is
positive.  Taking the primitive pivot class `u_(t,j)=L_C`, (1.1) gives the
requested polynomial resultant

```text
Res_y(H_t,L_C)=-4q^2(3t+2)^3 F_C(t,j),                (5.11a)
```

so every `C_j` pivot is a unit, including on split fibers.

For `t<=j<=2t`, define

```text
A_Q=12t^2+16t+4-j(3t+4),
B_Q=2(t+1)(j-t),
L_Q=A_Q d+B_Q.                                         (5.12)
```

The pivot on `q_j` is

```text
p_Q(t,j)=-3t(3t+1)(q-j)L_Q /
 ((t+1)q(3t+2)^2(4t-2j+1)).                           (5.13)
```

Moreover

```text
3B_Q^2-A_Q^2(t+1)=-(t+1)(3t+2)^2 F_Q(t,j),
F_Q(t,q-n)=n^2+4nt+6n+4t^2-3.                         (5.14)
```

In the required range `1<=n=q-j<=t+1`; the right side is at least `12`.
For the primitive class `u_(t,j)=L_Q`,

```text
Res_y(H_t,L_Q)=-4q^2(t+1)(3t+2)^2 F_Q(t,j).           (5.14a)
```

All rational denominator factors in (5.10) and (5.13) are positive in their
stated ranges.  Therefore every pivot in (5.8), except the last, is a unit by
(1.1).  The last coefficient is

```text
p_b2=g*d/(2y)
    ~ L_2=3q*d+(t+1),
Res_y(H_t,L_2)=-12q^2(t+1)(3t+2)(4t+1).               (5.15)
```

a product of units.  This proves all `2t+1` high-`E_t` eliminations.

Counting (5.6)-(5.7), the two divisibility/gauge pivots, and (5.8) gives

```text
(3t-1)+2+(2t+1)=5t+2.
```

Together with section 3 this is the **SECOND AFFINE SPINE,
PROVED-HERE for every `t>=2`**.  The `t=1` coefficient-space boundaries
collide and this spine does not instantiate there; the separate banked exact
audit instead makes four checked affine pivots and then encounters a unit.
Thus the ray's base case is discharged without asserting a nonexistent
seven-pivot `t=1` spine.  The symbolic driver `laurent_pivot_formulas.py` verifies
(5.9)-(5.15) in `Q(t,j)[d]/(3d^2-t-1)` and compares them, up to rational
associates, with every available exact Laurent record.

## 6. Closed terminal family

For `t>=2`, let `sigma_t` denote the proved Laurent/Euler substitutions of
section 5 through band `2t`.  Put

```text
E_t(X)=(b3*y-LR)V' + (LS-b3T-b2*g)U' + g*y.            (6.1)
```

By (2.4), after `C12=C11=0`, this is exactly `C01`; fixed records may choose
its negative primitive associate.  In particular, the
`terminal_laurent_t*.json` records use `-E_t`.  The terminal family is the explicit
coefficient family

```text
T_(t,k) = [X^k] sigma_t(E_t),       0<=k<2t.           (6.2)
```

Formula (6.2), together with the coefficient recurrences (5.5)-(5.15) and
polynomial coefficient extraction, is a closed indexed `t>=2`
description; it avoids printing expressions whose rational numerators have
thousands of digits.  It is also executable without any choice of monomial
order.  Before division it is a coefficient recurrence over `Z[t,y]`; after
the displayed pivots it lies in `Q(t)[y]/(H_t)`, and multiplication by the
finite product of the denominators in section 9 returns integral
coefficients.  The fixed-`t` TSV/JSON files print every expanded polynomial
without hiding this clearing factor.

The grading proves

```text
variables: b3,b4,q_2,0,...,q_(t-1),0,
bands:     0,...,2t-1,
weights:   wt(b4)=1, wt(b3)=t+1, wt(q_i,0)=i,
wt(T_(t,k))=4t+1-k for 1<=k<2t;
T_(t,0)=-c plus a homogeneous part of weight 4t+1.    (6.3)
```

On the chart `b4 != 0`, set

```text
z=b3/b4^(t+1),  r_i=q_i,0/b4^i.
```

Then for `k>0`

```text
T_(t,k)=b4^(4t+1-k) F_(t,k)(z,r_2,...,r_(t-1);y).     (6.4)
```

The invariant emitter checks (6.4) monomial by monomial before writing a
Singular job.  This is the smallest useful finite presentation of the
terminal obstruction: `2t-1` equations in `t-1` affine variables over the
quadratic algebra.  It must still be paired with the `b4=0` chart; scaling
alone says nothing about that hyperplane.

At the residual origin (`b3=b4=q_2,0=...=0`) the recurrence is explicit:

```text
U=X^q, R=X^t, T=g2 X^t, S=g1 X^(2t), V'=e X^(e-1),
T_(t,0)=-c=-5q*g5.                                    (6.5)
```

Thus it really ends in the already proved unit `-c`, not just a sampled
nonzero constant.  At `t=2,3` the entire nonconstant part of `T_(t,0)` is
divisible by `b4`, but the exact `t=4` row has fourteen nonconstant terms
surviving at `b4=0`.  Thus that tempting shortcut is false, not merely
unproved.

## 7. Finite exact data and controls

The fixed computations use the same canonical band/tag order.  `u` below is
the primitive integral linear associate recorded by the exact Schur audit;
the final column lists lower tag-`11` pivots after a semicolon.

| `t` | lower tag-`12`, descending `k` | lower tag-`11`, descending `k` |
|---:|---|---|
| 2 | `k1:40y-11, k0:35y-3` | `k1:125y-21` |
| 3 | `k2:49y-13, k1:147y-41, k0:21y-10` | `k2:49y-8, k1:420y-71` |
| 4 | `k3:180y-47, k2:432y-115, k1:864y-245, k0:9y-5` | `k3:81y-13, k2:720y-119, k1:630y-107` |
| 5 | `k4:143y-37, k3:88y-23, k2:198y-53, k1:66y-19, k0:11y-7` | `k4:605y-96, k3:1100y-179, k2:6y-1, k1:88y-15` |
| 6 | `k5:416y-107, k4:1677y-434, k3:4836y-1267, k2:26y-7, k1:24y-7, k0:39y-28` | `k5:845y-133, k4:1560y-251, k3:286y-47, k2:650y-109, k1:117y-20` |

Every resultant in this table is nonzero at its recorded integer; the exact
values and row source indices are in `source_linear_spine_t2_t6.tsv`.
For `t=2,3` these Schur coefficients were also compared with the full
nonlinear canonical substitutions and agree up to rational associates.
The status of the `t=4,5,6` full nonlinear comparison is recorded in the
artifact manifest and must not be strengthened from `SCHUR-EXACT` to a
uniform theorem.

The finite row counts are:

| `t` | post-H/c rows / auxiliaries | affine pivots | dropped `02` | terminal rows / variables | status |
|---:|---:|---:|---:|---:|---|
| 1 | `11 / 8` | `4 then unit` | n/a | n/a | banked exact `[1]`; boundary collision |
| 2 | `20 / 14` | `12` | `4` | `4 / 2` | fresh exact; both product factors `[1]` |
| 3 | `29 / 20` | `17` | `6` | `6 / 3` | fresh exact; `[1]` |
| 4 | `38 / 26` | `22` | `8` | `8 / 4` | fresh exact post-`H/c`; exact Laurent terminal charts `[1]` |
| 5 | `47 / 32` | `27` | `10` | `10 / 5` | exact rows and `b4=0` `[1]`; `b4=1` timeout; modular checks `[1]` |
| 6 | `56 / 38` | `32` | `12` | `12 / 6` | exact post-`H/c`; mod 1009 both fibres/charts/top `[1]` |

For `t=2`,

```text
H_2=12(5y-1)(5y-2),
```

and the computation never treats the quotient as a field.  It runs both
specializations `y=1/5` and `y=2/5`; both terminal Gröbner bases are `[1]`.
For example, at `y=1/5` primitive terminal representatives are

```text
-19200 b3^2 b4^3+191000 b3 b4^6-406875 b4^9-1024,
-b4^2(192 b3^2-8960 b3 b4^3+28925 b4^6),
-b4^4(16 b3-35 b4^3),
 b4^3(88 b3-295 b4^3).
```

The incompatible last two equations on `b4!=0`, followed by the first
equation on `b4=0`, exhibit the terminal constant directly in this fiber.

For `t=3`, the six expanded terminal rows are in
`terminal_t3_canonical_side-first_exact.json`.  In the Laurent coordinates,
the top `t` bands after setting `b4=1` have exact Gröbner basis `[1]` for
`t=2,3,4`; the exact full `b4=0` and `b4=1` charts are also unit ideals for
`t=3,4`.  These are not the same subsets as the failed banked side-first
`t=4` last-band probes: the Laurent change of variables and elimination order
must be applied first.  Modulo `1009`, the Laurent top-five, full `b4=0`, and
full `b4=1` systems are `[1]` on both roots of `H_5`.  This is strong finite
evidence for a high-tail recurrence, but not an all-`t` proof.  The same six
checks pass for the two roots `y=380,940` of `H_6` modulo `1009`.

The characteristic-zero Laurent `t=5` record is exact, and its `b4=0` chart
has basis `[1]`.  The `b4=1` `std` run reached its 3600-second cap without a
basis or verdict; bounded `std` on the top five rows and `slimgb` on all ten
rows likewise timed out.  These are typed `INCONCLUSIVE_TIMEOUT`, never
`NONUNIT`; the modular successes are not promoted across characteristic.

There is similarly sharp evidence on `b4=0`.  Delete band zero and call the
remaining ideal `I_(t,+)`.  Exact bases give

```text
sqrt(I_(3,+))=(b3,q_2,0),
sqrt(I_(4,+))=(b3,q_2,0,q_3,0).                       (7.1)
```

They contain a triangular chain beginning with `b3^t` and then a power
`q_j,0^(t+1)` modulo the previously killed variables.  On both mod-`1009`
fibres at `t=5`, the identical 63-monomial lead ideal contains
`b3^5,q_4,0^6,q_3,0^6,q_2,0^6`.  Band zero at their common radical origin is
the unit `-c=-5qg5`.  These computations isolate the likely induction invariant
without promoting a finite pattern.

### Required low-level control

Set `b1=b2=b3=b4=0`, so `h=pi^3(pi-gamma)`, and take

```text
Q=h^q+B,
P=h^e+2pi-gamma,
c=-1.
```

The charged exact differentiation gives

```text
J(Q,P)=-gamma+q*pi^2(2pi-3gamma)h^(q-1)-2e h^e.
```

Thus all low levels through `2t-1` vanish, while the moving bands `2t` and
`3t+1` fail.  This reproduces the charged positive and negative control and
explains why no fixed collection of low bands can prove (T).

## 8. Exact residual statement

Only the terminal statement remains.  Form the coefficient family (6.2) by
the proved Laurent/Euler spine and prove

```text
<T_(t,0),...,T_(t,2t-1)> = [1]
in A_t[b3,b4,q_2,0,...,q_(t-1),0]                    (8.1)
```

for every integer `t>=2`; `t=1` is the separate exact unit base case.  The
cheapest exact test is weighted
two-chart elimination:

```text
b4 != 0:  set b4=1 and test the F_(t,k) from (6.4);
b4 = 0:   test <b4,T_(t,0),...,T_(t,2t-1)>.
```

On split indices both tests are made in the product algebra, equivalently at
`d=s` and `d=-s`; no zero divisor is inverted.  A certificate for (8.1) must
be an indexed recurrence or must carry a specialization denominator whose
integer roots are checked separately.  Fixed `t<=6` Gröbner bases are tests,
not an induction.

The cheapest sharpened proof target separates into two lemmas:

```text
RESIDUAL-ZERO:
 sqrt(<T_(t,1),...,T_(t,2t-1)>|_(b4=0))
   =(b3,q_2,0,...,q_(t-1),0)  for t>=3;

TOP-TAIL-UNIT:
 <T_(t,t),...,T_(t,2t-1)>|_(b4=1)=[1].              (8.2)
```

The first lemma plus the unit value `T_(t,0)(0)=-c=-5qg5` closes the `b4=0`
chart; the second closes `b4!=0`.  At `t=2` all positive-band rows on
`b4=0` vanish, so `RESIDUAL-ZERO` would be false; instead the band-zero row
itself is a unit there, as the exact product-algebra base case shows.  The
`t=1` case is likewise banked exact.  Exact evidence proves
`RESIDUAL-ZERO` at `t=3,4` and `TOP-TAIL-UNIT` at `t=2,3,4`; mod-`1009`
evidence checks both fibres of `H_5` and `H_6`.  Either a proof of the two
indexed statements (with these base cases) or a direct proof of (8.1) is
still required.

Statement (8.1) is exactly the missing theorem (T) on this normalized ray.
Sections 2-6 reduce the original chart to it without a projection or an
untyped localization.

## 9. Denominators and FALLACY-v2 audit

The polynomial identities (2.3)-(2.5) are denominator-free.  The displayed
top recurrence through `g5` can be cleared with

```text
D_top(t)=60(2t+1)^5.
```

Its only rational root is `t=-1/2`, so it has no positive integer root.  The
leading coefficient of `H_t` is `12(2t+1)^2`, likewise nonzero for every
positive integer.  Divisions by `y` and `g` in (2.6) are justified by their
recorded resultants, not by treating `A_t` as a field.

For the proof spine, the displayed coefficient denominators divide products
of

```text
2, 3, 5, t, q, 3t+1, t+1, 3t+2, t-j, q-j,
4t-2j+1, m, 2m+1,
```

and the pivot inverses additionally use the nonzero norms (5.11), (5.14),
and (5.15).  Every rational factor is positive on its declared integer index
range, and the three norm factors are proved nonzero there.  (The factor `m`
only occurs where an integrated nonconstant coefficient has `m>=1`; also
`1<=q-j<=t+1` in its pivot range.)  Thus
the indexed recurrence
has no positive-integer exceptional specialization.  No
`D_terminal(t)` is declared: no generic terminal certificate was obtained.
Inventing one from finite samples would be precisely the forbidden
generic-specialization fallacy.

The discriminant of `H_t` is `48q^2(t+1)`, and it is reducible over `Q`
exactly when `t=3s^2-1`.  These infinitely many indices are not a finite
denominator exception set.  All statements above either use the
squarefree product algebra or branch to its two rational factors.  In
particular, (5.4) is recorded as a zero divisor and never inverted.

## 10. Reproduction

The compact identity check is

```text
python3 box/k16spine-20260903/compact_remainder.py
```

and prints `COMPACT_REMAINDER_IDENTITIES_PASS`.  The fixed exact Schur table
is reproduced by

```text
python3 box/k16spine-20260903/source_linear_spine.py 2 3 4 5 6
```

after checking the frozen chart hash internally.  Canonical expanded rows,
pivot inverses, substitution checks, resultants, split-fiber jobs, and output
hashes are indexed as follows:

```text
canonical_status.json
  exact post-H/c audits/row vectors for t=2,...,6;
canonical_pivots_schur_t2_t6.{tsv,json}
  all fixed exact side-first Schur pivots and resultants;
laurent_pivots_t2_t6.tsv
  exact specializations of (5.9)-(5.15);
terminal_laurent_t2_product_exact.json
  both factors and both b4 charts at split t=2;
terminal_laurent_t{2,3,4,5}.json
  expanded exact Laurent recurrences and terminal rows;
terminal_laurent_t{3,4}_b4_{0,1}_exact.out
  exact two-chart unit certificates;
terminal_laurent_t5_b4_0_exact.out
  exact unit certificate for the t=5 zero chart;
canonical_t5_b4_1_fallback_status.json
terminal_laurent_t5_b4_1_exact_status.json
  three explicitly inconclusive exact runs on the other chart;
canonical_terminal_mod_t{5,6}_p1009_branch*_b4_*.out
terminal_mod_t{5,6}_p1009_branch*.out
  explicitly modular full-chart and top-tail discovery checks.
```

The formula checker

```text
python3 box/k16spine-20260903/laurent_pivot_formulas.py
```

prints `LAURENT_PIVOT_FORMULAS_PASS` and exact-associate agreement for the
available `t=2,3,4,5` Laurent records.  The split exact control is reproduced
by `terminal_split_exact_check.py`.  `canonical_artifacts.sha256` covers the
canonical extraction subset; `final_manifest.sha256` covers the completed
lane directory and is checked from inside that directory with
`sha256sum -c`.

All producer processes were stopped before manifesting.  The final manifest
contains 234 files, has SHA-256
`d828fb12e664d1a77187fd552607adb2ed22f38c804a784e426c11e42f4d9ef8`,
and its complete `sha256sum -c` replay passed.  The exact `t=5,b4=1`
timeout remains deliberately preserved as an inconclusive control.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `29282`.
- Body SHA-256:
  `54889e8ca4961dd6218d5b5c641cfe8b6b555f9fdbf904bd2025040f843b7977`.
- Frozen basis: `cd3ff3e85aefe9491f0db695761e24e4228ea97b`.
