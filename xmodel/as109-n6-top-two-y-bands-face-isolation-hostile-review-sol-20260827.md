# Hostile review — AS109 `n=6` top-two-band face isolation

Date: 2026-08-27 11:00Z  
Reviewer: Sol (OpenAI), independent of the Grok producer  
Charged artifact: `xmodel/as109-n6-top-two-y-bands-face-isolation-grok-20260827.md`  
Charged SHA-256: `7640715607c640beae845855feb261a0d207ea9409a1ccf8a915899f4461ec10`

## Verdict

**CONFIRMED WITH ONE NON-LOAD-BEARING WORDING REPAIR.**

The producer's mathematical verdict `TWO_BANDS_TAUTOLOGICAL` is correct.
For the residual AS109 corner `deg_y(P)=m>=12`, `deg_y(Q)=6`, the two
highest Jacobian rows impose no new condition on the promoted leading-core
data.  The face card stops after the two promised bands.  The proposed
bounded W2/W3 gauge-conductor is not a new unrestricted successor: its two
possible finite-cap outcomes are already covered by the reviewed
wild-symplectic and polar-conductor results.

The only repair is in the valuation prose in producer section 5.  The
sentence saying that the integer prefactors `5,6,m` have 109-adic valuation
zero is false when `109 | m`; likewise `m-1` may be divisible by 109.  The
correct statement is:

> `5` and `6` are 109-adic units.  Either of `m` and `m-1` may have positive
> 109-adic valuation, but this can only raise the corresponding summand's
> valuation and does not weaken any lower bound.

No displayed lower bound, band equation, control, or stop decision uses the
incorrect wording.

## Independent derivation

Write

```text
P=sum_(i=0)^m p_i(x)y^i,     Q=sum_(j=0)^6 q_j(x)y^j.
```

The pair `(i,j)` contributes

```text
(j p_i' q_j - i p_i q_j') y^(i+j-1)
```

to `P_x Q_y-P_y Q_x`.  Consequently the only contributors in the two
charged bands are

```text
[y^(m+5)]J = 6 p_m' q_6 - m p_m q_6',

[y^(m+4)]J = 5 p_m' q_5 - m p_m q_5'
              + 6 p_(m-1)' q_6 - (m-1)p_(m-1)q_6'.
```

Both coefficients must vanish because `m+4>0`.  The seed terms have
`y`-degrees zero in `P` and one in `Q`, so neither enters these bands.

Put `d=gcd(m,6)`, `a=m/d`, `b=6/d` and use the already promoted leading
core over `Q_109[x]`:

```text
p_m=alpha h^a,       q_6=beta h^b.
```

The first row vanishes identically because `6a=mb`.  For the second row,
only inside `Q_109(x)`, set

```text
U=p_(m-1)/(alpha h^(a-1)),
V=q_5/(beta h^(b-1)),
W=bU-aV.
```

Direct substitution gives

```text
d h W' - (d-1)h'W = 0.
```

Thus the nonzero mismatch branch has `W^d/h^(d-1)` constant.  For the only
residual values this yields

```text
d=3: 3 deg(W)=2 deg(h), hence 3 | deg(h),
d=6: 6 deg(W)=5 deg(h), hence 6 | deg(h).
```

Those are exactly the already promoted divisibilities.  The aligned branch
`W=0`, zero next coefficients, and constant `h` all remain possible.  This
localized calculation is not copied into the integral ring by division;
the integral statement remains the second displayed band equation.

Every one of `p_m,q_6,p_(m-1),q_5` is divisible by 109 because all four
belong to positive `y`-degrees beyond the seed.  Differentiation preserves
that divisibility.  Hence every summand in both bands is divisible by
`109^2`, regardless of any extra valuation in `m` or `m-1`.  The undivided
relations are therefore `0=0` modulo both 109 and `109^2`.  Dividing the
exact integral equation by the proved common `109^2` merely reproduces the
same underdetermined characteristic-zero row on the residual coefficients;
there is no unit carry against which a Kummer-face contradiction could fire.

## Controls and successor audit

- For `u=x+y`, `v=y+u^6`, `(P,Q)=(u+v^2,v)`, direct chain-rule composition
  gives determinant one and degrees `(12,6)`.  Its leadings satisfy both
  rows, with `p_11=12x`, `q_5=6x`; this blocks any universal floor-seven
  inference from the two rows.
- For a polynomial `K` of `y`-degree `d`, the pairs
  `(alpha K^(m/d), beta K^(6/d))` have Jacobian zero and occupy every
  residual numerical type.  They are controls, not AS109 lifts.
- The reviewed polar-conductor theorem already proves that every fixed
  simultaneous polynomial map/gauge degree cap dies at some finite Witt
  depth and that the canonical completed gauge has unbounded degree.  The
  reviewed wild-symplectic theorem already makes unrestricted completed
  cohomology one orbit.  Re-running W2/W3 on an `n=6` rectangle would either
  produce another finite-depth survivor or another bounded-cap death;
  neither changes the unrestricted exact-lift state.

## Licensed conclusion

Bank the two displayed identities and the null result; stop the `n=6`
top-two-band face card and do not launch its W2/W3 bounded-gauge duplicate.
Do not infer that the residual `n=6` corner is empty, that a polynomial
AS109 lift exists, or that one is impossible.  Any new AS109 successor must
use a mechanism that sees the seed or changes the unrestricted polynomial
lift state, rather than another fixed support/degree cap.

