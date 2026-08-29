# AS109 residual `n=6`: low-Witt/common-core Cartier gate

Date: 2026-08-27 11:24Z  
Producer: Sol (OpenAI)  
Verdict: **`PASS-LOW-WITT-CARTIER` — PROVISIONAL, BRANCH-LOCAL**  
Compute: exact desk-scale Python stdlib replay; no Singular, AWS, or
`jc2-lean`

## 0. Result

The stopped top-two-band attack misses a lower, first-Witt constraint.  Let

```text
P=x-x^109+109 A,       Q=y+109 B
```

be an exact polynomial map over `Z_109` with determinant one, and suppose its
residual leading corner has

```text
deg_y(P)=m>=12,        deg_y(Q)=6,
d=gcd(m,6) in {3,6},
p_m=alpha h^(m/d),     q_6=beta h^(6/d),
```

with `h` primitive over `Z_109`.  Put `b=6/d`, so `b in {1,2}`.

If `v_109(beta)=1`, then

```text
(bar h)^b in im(d/dx : F_109[x] -> F_109[x]).              (0.1)
```

Equivalently, every coefficient of `(bar h)^b` at `x^(109k-1)` is zero.
Writing `Hbar=deg(bar h)`, this gives the immediate leading-degree condition

```text
b Hbar != 108 (mod 109).                                   (0.2)
```

Thus:

```text
d=6 (b=1): Hbar != 108 mod 109,
d=3 (b=2): Hbar != 54  mod 109.                            (0.3)
```

These are exact necessary conditions only on the valuation-one `q_6` content
branch.  They do not show that branch is populated, do not see
`v_109(beta)>1`, and do not exclude the residual `n=6` corner as a whole.

There is also a positive compatibility control.  If, in addition,
`v_109(alpha)=1` and `gcd(m/d,109)=1`, then the top `P` coefficient forces
`bar h` to be a polynomial in `x^109` up to scalar.  In that subbranch (0.1)
is automatic.  The new condition is therefore a discriminator, not a hidden
universal contradiction.

## 1. Trust boundary and history checksum

Frozen replay:

```text
cases/as109_n6_low_witt_cartier_v1_20260827/FREEZE.sha256
fcb578ae1940e19d0b7b76e39db33754ac1471e61f462e3e19388d572ae6900a
```

Its three payload hashes are:

```text
PREREGISTRATION.md          5f3dd79b6050d2a66429866ad95a3068fbc1116ed6bdd26aad61fd5a7e784bea
verify_low_witt_cartier.py  65097ad0aa07447b442a07ce4ca865f834978c87136b1b78d1d068acf75bc5a8
EXPECTED_RESULT.json        e0fbc93fa41feaa377d1e75a2457bf7539a68ce625db3f266f40fa5c58477907
```

Load-bearing history reread before promotion language:

```text
as109-one-sided-prime4-composition-sol                 3d6d09fd1c9d1548dc6af78221f74c83276eb89378ee06cecac5fd19b46fcb36
as109-n6-top-two-y-bands-face-isolation-grok           7640715607c640beae845855feb261a0d207ea9409a1ccf8a915899f4461ec10
as109-n6-top-two-y-bands hostile review Sol            571c5e2bda00cf9221debcd43b26f635016a68622714bbf8bbb0e2a68f33525f
as109-support-gate                                      b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5
as109-support-gate carry erratum                        ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb
```

The first-Witt equation and its Cartier cokernel are known campaign objects.
The leading common core is known.  The apparent novelty is limited to
coupling the **low `y^5` first-Witt row** to the residual
`q_6=beta h^b` common core.  The just-stopped calculation used the two highest
rows `y^(m+5)` and `y^(m+4)`; neither can see this coefficient.

No canonical ledger is edited by this producer.  Independent hostile review
is required before promotion.

## 2. Packed determinant identity

Over `Z_109[x,y]`, write `s=x^108`.  The four partial derivatives are

```text
P_x=1+109(A_x-s),       P_y=109 A_y,
Q_x=109 B_x,            Q_y=1+109 B_y.
```

The determinant is quadratic in the correction derivatives, so there is no
omitted higher term:

```text
det J(P,Q)-1
 =109(A_x+B_y-s)
  +109^2((A_x-s)B_y-A_yB_x).                              (2.1)
```

This is the packed exact equation used in the earlier support gate.  It avoids
the digit-carry error corrected by the 2026-08-24 erratum: no separately
chosen second digit is being inferred here.

Reducing (2.1)/109 modulo 109 gives

```text
bar A_x + bar B_y = x^108.                                (2.2)
```

## 3. Coefficientwise first-Witt rows

Write

```text
bar A=sum_(i>=0) a_i(x)y^i,
bar B=sum_(j>=0) b_j(x)y^j.
```

The coefficient of `y^i` in (2.2) is exactly

```text
a_i'(x)+(i+1)b_(i+1)(x)=delta_(i,0)x^108.                 (3.1)
```

Because `deg_y(B)=6`, the row just below its top is

```text
a_5'+6b_6=0.                                              (3.2)
```

This is deliberately not a third step in the top-band cascade.  It is a low
row of the first Witt digit, and it sees the seed through the global packed
equation (2.2).

## 4. Cartier image and the common core

For `f=sum c_e x^e in F_109[x]`, the coefficient of `x^e` in a derivative
can only come from `x^(e+1)`, with scalar `e+1`.  Hence

```text
f in im(d/dx)
 iff c_(109k-1)=0 for every k>=1.                         (4.1)
```

Now `q_6=109 b_6` because every positive `y` coefficient of `Q-y` is
divisible by 109.  In the primitive common-core normalization,

```text
q_6=beta h^b,       b=6/d.
```

If `v_109(beta)=1`, reduction after division by 109 gives

```text
bar b_6=(beta/109 mod 109)*(bar h)^b,
```

with nonzero scalar.  Equation (3.2) therefore proves (0.1) by (4.1).

If `Hbar=deg(bar h)`, the leading term of `(bar h)^b` is nonzero and has
degree `b Hbar`.  If that degree were `108 mod 109`, it would be one of the
forbidden exponents in (4.1).  This proves (0.2)--(0.3).  Notice that `Hbar`
is the degree **after reduction**, not necessarily `deg(h)` over `Z_109`;
no unit-leading-coefficient assumption is hidden.

The replay checks the two sharp monomial controls:

```text
d=6: h=x^108, b=1  -> forbidden x^108 coefficient 1;
d=3: h=x^54,  b=2  -> forbidden x^108 coefficient 1.
```

## 5. Top-`P` compatibility control

For every `i>=6`, `b_(i+1)=0`, so (3.1) gives `a_i'=0`.  In particular,
`a_m'=0`.  If `v_109(alpha)=1`, then

```text
bar a_m=(alpha/109 mod 109)*(bar h)^a,
a=m/d.
```

Thus `(bar h)^a in F_109[x^109]`.  Since the field is perfect, this is a
109th power in `F_109[x]`.  Unique factorization and `gcd(a,109)=1` imply
that `bar h` itself is a 109th power up to scalar, equivalently
`bar h in F_109[x^109]` after absorbing a scalar.

Every polynomial `g(x^109)` is in the derivative image because

```text
d/dx (x*g(x^109)) = g(x^109).
```

Therefore `(bar h)^b` automatically passes (0.1) on this subbranch.  The
replay uses `bar h=1+x^109` for both `b=1` and `b=2`, constructs an explicit
antiderivative, sets `a_5=-6*integral(b_6)`, and obtains precisely
`bar A_x+bar B_y=x^108` with the `y^5` coefficient zero.

## 6. Exact replay

Run from the repository root:

```text
shasum -a 256 -c cases/as109_n6_low_witt_cartier_v1_20260827/FREEZE.sha256
python3 cases/as109_n6_low_witt_cartier_v1_20260827/verify_low_witt_cartier.py
```

The replay uses exact integer sparse bivariate arithmetic for twelve
deterministic tests of (2.1), finite-field univariate arithmetic for the
Cartier criterion and antiderivatives, and exact integer univariate arithmetic
for representative `d=3` and `d=6` common-core Wronskians.  Its output matches
the frozen expected JSON byte for byte and reports:

```text
verdict                              PASS-LOW-WITT-CARTIER
packed_determinant_identity          true (12/12)
d6_Hbar_108_obstruction              {108:1}
d3_Hbar_54_squared_obstruction       {108:1}
common_core_wronskian_d6             ZERO
common_core_wronskian_d3             ZERO
top_a_frobenius_derivative           ZERO
```

The replay is a regression/control suite.  The general proof is the
coefficientwise derivation above, not random testing.

## 7. Licensed use and next discriminator

Provisionally bank only this statement:

> An exact AS109 residual `n=6` lift whose `q_6` common-core scalar has
> 109-adic valuation exactly one must satisfy the coefficientwise Cartier
> conditions (0.1), hence (0.2)--(0.3).

The cheapest next step is not W2/W3.  Intersect the existing residual
parameterization with three content strata:

```text
v_109(beta)=1, v_109(alpha)=1;
v_109(beta)=1, v_109(alpha)>=2;
v_109(beta)>=2.
```

The first has the Frobenius positive control.  The second is where the new
Cartier equations can genuinely cut.  The third is invisible at this digit
and should stop unless a mechanism reaches the first nonzero `q_6` digit.

If a compatible finite support emerges, it may seed the already-reviewed
`CLOSED-SUPPORT + UNIT-L` contraction criterion.  That is a possible
counterexample construction route, not a conclusion here.

## 8. Scope firewall

This producer does **not**:

- prove that `v_109(beta)=1`, that `v_109(alpha)=1`, or that either content
  pattern occurs in a lift;
- identify `Hbar` with the characteristic-zero degree of `h` when the leading
  coefficient reduces to zero;
- inspect `v_109(beta)>1`;
- run another top band, W2/W3, a bounded gauge, a support cap, or a degree
  rectangle;
- construct a closed nonlinear support module;
- prove or disprove an AS109 polynomial lift, a characteristic-zero
  counterexample, Gate T, or JC2.

