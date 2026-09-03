# Uniform-pattern audit for the K=16 ray

Date: 2026-09-03.  This is a supporting audit, not the requested lane report.
It uses the frozen inputs under `/tmp/jc2-lane.fjoTgL/inputs` and writes only
under `box/k16uniform-20260903/`.

## 1. Custody and scope

The lane receipt
`xmodel/k16-uniform-structure-sol56-20260903.run.v2` was parsed mechanically:
`charged_input_<i>_basename` and `charged_input_<i>_sha256` were paired by
their numeric index with `awk`, prefixed by the receipt's frozen input
directory, and piped to `sha256sum -c`.  All 15 inputs returned `OK`.

The theorem under attack is nonexistence of a monic polynomial pair carrying

```text
(n,m;M2,V2;J)=(12t+4,8t+4;12t+1,3;c*gamma),  c != 0.
```

The gcd/exponent data are `e=3t+1`, `q=2t+1`; see the frozen Newton report
at `k16-ray-T-newton-sol56-v3-20260903.md:194-227`.  The two-disc chart is a
necessary superset, not an equivalent moduli description: this logical
direction is stated explicitly in the charged uniform report at lines
`498-502`.  Therefore a characteristic-zero unit ideal for the chart proves
theorem (T), while a surviving chart point is not a pair and would still need
the omitted Laurent/tuple bridge (charged lines `477-485`).

## 2. Uniform grading

Put intrinsic weights

```text
wt(gamma)=wt(pi)=wt(z)=1, wt(B)=2, wt(A)=3, wt(h)=4.
```

The coefficient spaces and safe gauges are exactly those at charged uniform
report lines `62-107`:

```text
S_i=<1>                         1 <= i <= t,
S_i=<1,A>                       t < i <= 2t,
S_i=<1,A,B>                    2t < i <= 3t,
S_e=<1,gamma,A,B,z>             e=3t+1,

alpha_t=0, const(beta_q)=0, const(alpha_e)=0.
```

For a coordinate multiplying a basis element `phi` in `alpha_i` or `beta_i`,
define

```text
wt(coordinate)=4*i-wt(phi),
wt(b_j)=j,
wt(c)=4(e+q)-3=20t+5=5(4t+1).
```

This is a proof, not a fit.  Under source dilation, each `alpha_i` and
`beta_i` has total weight `4i`, hence every term of `P` has weight `4e` and
every term of `Q` weight `4q`.  The Jacobian has weight `4(e+q)-2`; matching
`c*gamma` gives `wt(c)=4(e+q)-3`.  The banded identity and monic carry are
homogeneous.  Every weight is positive for `t>=1`.  Each Q-constant affine
pivot is consequently grading-equivariant, so the grading descends through
the charged constant-pivot quotient.

In particular, with

```text
x = beta_(t+1),A = q(t+1)_1,
y = beta_q,B     = q(2t+1)_1,
```

one has

```text
wt(x)=4t+1, wt(y)=8t+2=2wt(x), wt(c)=20t+5=5wt(x).
```

This proves the linear weight pattern.  It specializes to `(9,18,45)`,
`(13,26,65)`, and `(17,34,85)` at `t=2,3,4`, agreeing with the exact charged
computations (`k16-t3-uniform...md:190-206,275-288`) and with the fresh frozen
replays.

## 3. The all-t normalizer lemma

The quadratic is not an interpolation from three samples.  The charged raw
band formula and monic carry are at `k16-t3-uniform...md:127-145`, and its
uniform Q-constant spine is proved at lines `371-401`.  Extract the following
five coordinates from that spine:

```text
g1 = alpha_(t+1),A,
g2 = alpha_q,B,
g3 = alpha_e,z,
x  = beta_(t+1),A,
y  = beta_q,B.
```

After the constant gauge at the endpoint, `alpha_e` has basis
`(gamma,A,B,z)`; its `gamma` coordinate is the penultimate endpoint pivot and
maps to zero.  Direct coefficient extraction from the charged band identity,
reducing each row by the preceding higher-band rows, gives Q-star associates
of

```text
E1, band 4t+1: q*g1-e*x = 0,
E2, band 3t+1: 2q*g2-(e-q)*x*g1-2e*y = 0,
E3, band 2t:   3q*g3-(e-2q)*x*g2-(2e-q)*y*g1 = 0,
E4, band t:    (e-3q)*x*g3+(2e-2q)*y*g2 = 0,
E0, band 0:    c+y*g3 = 0.
```

Here the literal endpoint `gamma*pi^2` row used for `E3` has pivot
`-3q/4`; multiplying by a nonzero rational and reducing by the earlier row
gives the displayed recurrence.  This matches the charged endpoint-pivot
calculation at lines `383-390`.

There is also a compact conceptual derivation.  On the top chain

```text
h_top=pi*A_top, A_top=pi*B_top, B_top=pi*z.
```

In the associated h-adic Laurent grading put `U=A*h^(-(t+1))`.  Then

```text
U^2=B*h^(-q), U^3=z*h^(-e).
```

Thus the distinguished portions of `Q/h^q` and `P/h^e` are

```text
F(U)=1+xU+yU^2,
G(U)=1+g1 U+g2 U^2+g3 U^3.
```

The high Jacobian rows are the first coefficients of

```text
q*F*G'-e*F'*G=0.
```

The coefficient recurrence is

```text
k*q*g_k=(e-q(k-1))*x*g_(k-1)+(2e-q(k-2))*y*g_(k-2).
```

For `k=1,2,3` this is `E1,E2,E3`.  There is no `g4`: the P-table ends at
deficit `e`, and its endpoint chain ends with `z`, i.e. `U^3`.  Therefore the
`k=4` coefficient is an obstruction equation `E4`, not another solve.  This
also explains why its band is the moving band `h=t`.

Writing `r=e/q`, solving the three safe recurrences gives the first three
coefficients of `F^r`:

```text
g1 = r*x,
g2 = r*y + binom(r,2)*x^2,
g3 = 2*binom(r,2)*x*y + binom(r,3)*x^3.
```

The forbidden fourth coefficient is

```text
binom(r,2)*y^2 + 3*binom(r,3)*x^2*y + binom(r,4)*x^4.
```

Since `t,e,q` are nonzero for positive integral `t`, `E4=0` is equivalent to

```text
Hhat_t(x,y) = 12q^2*y^2 - 12q(t+1)*x^2*y
              + (t+1)(3t+2)*x^4 = 0.                 (H)
```

The sign in `E0` follows from the convention `J(Q,P)=c*gamma`: the terminal
terms are `yB` and `g3 z`, while
`J(B,z)=z+b1=pi-gamma+b1`, whose gamma coefficient is `-1`.  Hence
`c=-y*g3`, namely

```text
c = t(3t+1)/(6(2t+1)^3) * x*y
    * ((t+1)x^2-6(2t+1)y).                            (C)
```

The exact Q(t) identities, including all four recurrences, are checked by
`uniform_binomial_identities.py`.  `uniform_extract_normalizers.py` starts
from the frozen charged builders and independently recovers the literal
sparse source rows for `t=1,2,3,4,5`; the extra `t=5` row is
`242y^2-132x^2y+17x^4` and its c-row is
`1331c+880xy^2-80x^3y`.

## 4. Weighted slice and the rank-two algebra

Equation (C) shows that `c!=0` forces `x!=0`.  Over an algebraic closure choose
`lambda^(4t+1)*x=1` and apply the grading action.  No target point is lost;
the inverse scaling recovers every orbit.  On `x=1`, one may take

```text
H_t(y)=12(2t+1)^2*y^2-12(2t+1)(t+1)*y+(t+1)(3t+2),
c_t(y)=t(3t+1)y((t+1)-6(2t+1)y)/(6(2t+1)^3).
```

`H_t` has degree two over `Q(t)`, with polynomial coefficients in `t`, and

```text
disc_y(H_t)=48(2t+1)^2(t+1).
```

This is the discriminant of the displayed unscaled `H_t`.  A primitive
specialized associate is divided by a t-dependent integer content, so its
numerical discriminant is divided by the square of that content.  The first
four primitive specializations are

| t | primitive H_t | primitive discriminant |
|---:|---|---:|
| 1 | `54y^2-36y+5` | 216 |
| 2 | `25y^2-15y+2` | 25 |
| 3 | `147y^2-84y+11` | 588 |
| 4 | `486y^2-270y+35` | 4860 |

The t=3 and t=4 rows are exactly the charged rows at uniform-report lines
`193-210` and `280-288`.

The phrase “quadratic field uniformly in t” is false.  The generic polynomial
is irreducible over `Q(t)`, but at a positive integer it splits precisely when
`3(t+1)` is a square, equivalently

```text
t=3s^2-1  (s>=1).
```

There are infinitely many such specializations; `t=2` is the first, with
`H_2=(5y-1)(5y-2)`.  Uniformly correct language is the separable rank-two
algebra

```text
A_t=Q[y]/(H_t).
```

It is a field off the split set and a product of two fields on that set.
It is always reduced for `t>=1`, since the discriminant is nonzero.

The c-image is a unit in `A_t` for every positive integer `t`.  Indeed

```text
H_t(0)=(t+1)(3t+2),
H_t((t+1)/(6(2t+1)))=(t+1)(4t+1)/3,
```

and both are nonzero.  Equivalently, the two relevant resultants are

```text
Res_y(H_t,y)=(t+1)(3t+2),
Res_y(H_t,(t+1)-6(2t+1)y)
  =12(t+1)(2t+1)^2(4t+1).
```

Thus the normalizer and c-unit step, including every split fiber, are uniform.

## 5. The fixed residual proposal is false

The proposal “six equations in `(b3,b4,a2_0)` from bands `0,...,5` for every
t” fails literally at `t=2`: the safe gauge is `alpha_t=alpha_2=0`, so
`a2_0` does not exist.  The frozen exact t=2 replay instead gives 20 rows in
14 auxiliary variables after the H/c slice; twelve unit-only affine pivots in
the full etale algebra leave four equations in `(b3,b4)`, one from each band
`0,1,2,3`, of degrees `9,8,7,6`.  Both rational fibers have exact basis `[1]`.
See `t2_t1_audit.md:54-185`.

At `t=3`, the charged deterministic pass gives 29 rows in 20 auxiliaries,
seventeen unit pivots, and six rows in `(b3,b4,a2_0)`, one at each band
`0,...,5`, of degrees `13,...,8`; see charged lines `214-225` and the exact
replay `t3_normalization_audit.json`.

At `t=4`, the fresh exact pass starts with the charged 38-row, 26-auxiliary
normalized system.  Twenty-two successive coefficients are proved units in
`Q[v]/(486v^2-270v+35)` by explicit inverses, and every substitution is checked
modulo the quadratic.  Eight rows remain in four variables
`(b3,b4,a2_0,q3_0)`, one from each band `0,...,7`, all with remainder tag
`(gamma_power,pi_power)=(0,1)`, and with total degrees `17,...,10`.  The choice
of `q3_0` rather than `a3_0` is a pivot-coordinate choice, so the invariant
statement here is the count, band support, and dimension, not a canonical list
of variable names.  The complete substitution audit is
`t4_affine_audit.json` (SHA-256
`374674e76d58e27e154380c6823f3ed7c7b2caf90f40a94c21b4d6419014e05d`).

At `t=1`, the normalizer formula also holds, but the post-slice system finds a coefficient-
field unit after four affine pivots.  Its intrinsic final ideal is `[1]`, not
the t=3 terminal presentation.  This agrees with, but does not claim to be the
printed details of, Moh's `(16,12)` conclusion; the source limit and the
independent positive control are described in the Newton report at lines
`132-190`.  See `t2_t1_audit.md:206-286` for the frozen generalized-chart
replay.

The exact finite data expose a different tentative pattern for `t>=2`:

```text
post-H/c input:       9t+2 rows in 6t+2 auxiliaries,
affine pivots:        5t+2,
candidate terminal:  2t rows in t pivot-order-dependent variables,
candidate bands:      0,...,2t-1,
candidate degrees:    4t+1,...,2t+2.
```

The first line is measured at `t=1,2,3,4`; the complete terminal count/band/
degree pattern is exact at `t=2,3,4` but is not promoted as an all-t theorem.
The terminal coordinate names depend on the valid affine pivot order.  The
finite pattern already shows
why one fixed polynomial ring over `Q(t)` is unavailable: both the number of
middle scalar variables and the number of terminal equations grow with `t`.

## 6. Exact uniform blocker and bounded next step

What is proved uniformly is:

1. the denominator-free banded family and safe gauges;
2. the positive grading;
3. the `3t+4` Q-constant high-side pivots, through bands `4t+1` down to `2t`;
4. the normalizer `(H),(C)` and the c-unit statement.

The object not yet controlled is the **second affine spine after passage to
`A_t`**.  At each prospective pivot its coefficient is an element
`u_{t,j}(y)` of `A_t`; a valid uniform elimination requires a closed recurrence
for these elements and a proof that

```text
Norm_A_t/Q(u_{t,j}) = Res_y(H_t,u_{t,j}) != 0
```

for every required index and every positive integer `t`.  It must also prove
the claimed zero/duplicate-row recurrence and identify the resulting `2t`
terminal rows.  The charged fixed-low-band witness has defects only at the
moving levels `2t` and `3t+1` (uniform report lines `422-452`), and the systems
at `t` and `t+1` first differ at low band `t` and high offset `t` (lines
`459-475`).  These facts locate the obstruction in the t-scaling middle, not
in the now-solved quadratic normalizer.

The bounded next step is therefore not a Groebner basis in a guessed fixed
ring.  It is: prove the second affine recurrence by induction on the band
index; record each pivot norm/resultant; derive the `t`-variable, `2t`-row
terminal family; then seek a terminal recurrence whose last equation is a
nonzero coefficient-algebra constant.  Fixed `t=4` is the immediate induction
check.

## 7. Specialization and FALLACY-v2 obligations

Even if a future fixed-size reformulation gives `[1]` over
`Q(t)[y]/(H_t)`, FALLACY-v2 forbids the conclusion “all t” without a lifted
membership certificate.  Clear the denominators in

```text
1 = sum_i A_i(t,y,z)*R_i(t,y,z) + B(t,y,z)*H_t(y)
```

to obtain a common nonzero `D(t)`.  The certificate specializes only where
`D(t0)` and the leading coefficient of `H_t0` are nonzero.  Every root of
`D` must be handled exactly.  Every inverted coefficient-algebra element must
contribute its resultant to `D`.  The infinite split set `t=3s^2-1` is not a
finite denominator-exception set: specialization there must be interpreted in
the etale product algebra, and remains valid whenever the recorded resultants
are nonzero.

Full-chart runs must extract the `c`-saturation component, assert its ring, and
run both wrapper controls, exactly as required by `FALLACY-v2.md:16-21`.
Normalized runs must verify `c_t` is a unit and retain declared-ring positive
and negative controls.  The charged controls are summarized at uniform-report
lines `489-510`.

The actual-pair semantic control is

```text
(F,G)=(pi,pi-gamma^2/2), J(F,G)=gamma.
```

It passes both reciprocal quadratic-anchor shapes but has pi-degrees `(1,1)`,
so it fails the K=16 tuple.  This is proved in the Newton report at lines
`112-128` and must never be inserted as a target-chart point.

## Verdict

**PARTIAL.**  The grading, weighted normalization, degree-two `H_t`, c-image,
and c-unit statement are now uniform and explicit.  The claimed fixed six-by-
three residual system is refuted.  No uniform unit certificate exists in the
charged material: the post-normalization middle system grows with `t`, and its
second affine spine/pivot resultants have no proved all-t recurrence.  Hence
theorem (T) on the entire ray is not proved by this audit.

No exit set or exit price is asserted, so no `charge_basis=...` line is due.

<!-- BODY-END -->
