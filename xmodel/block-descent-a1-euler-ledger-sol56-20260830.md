# Block descent `A1` Euler ledger: exact strata and the surviving `P1` branch

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, independent audit lane  
Frozen basis: `5775cfc63803dbb99b6d4574f8e91e201790f3c0`  
Lifecycle: **EXACT PROVISIONAL LEDGER / NO `P1` EXCLUSION**

## 0. Verdict

For the promoted proper-block sandwich

```text
A2 --g1, etale quasi-finite of generic degree d1--> Y
   --g2, finite flat of degree d2--> A2,
```

put `R=NonEt_Y(g2)`, `U=Y minus R`, and let
`rho:U->C` be the promoted `A1`-fibration.  There is an exact
presentation-free Euler ledger, but no degree-only numerical evaluation:

```text
e(U)=d2-D2=e(C)+Q,
Q=sum_t(q_t-1)>=0,                                      (0.1)
```

where `D2` is a signed Euler integral of the number of finite-cover sheets
lost to source ramification.  The nonproper first leg has its own exact
ledger

```text
D1=d1*e(U)-1.                                           (0.2)
```

Composing the two ledgers gives an identity, not a new inequality.  Pointwise
sheet deficits are nonnegative, but their Euler integrals have no sign because
one-dimensional strata can have negative Euler number.

For a cubic block, the result sharpens to

```text
e(U)=3-2e(B)-|S0|,                                      (0.3)
```

where `B=g2(R)` is the reduced target branch support and
`S0=A2 minus g2(U)` is a finite set.  Consequently the complete-base branch
would have to satisfy

```text
C=P1:       2e(B)+|S0|+Q=1.                             (0.4)
```

This is restrictive but not contradictory: `e(B)=0, |S0|=1, Q=0` is
numerically viable.  The qualitative control
`(P1 x P1) minus diagonal` has `C=P1`, `e=2`, constant units and a rational
forest boundary.  It even contains an etale `A2` big cell, but only with
generic degree one and without the charged finite-flat sandwich.  Thus it is
a sharp guard against excluding `P1` from (0.1) alone, not a block control.

The missing data are the Euler topology of the actual target discriminant,
the finite set of values with no unramified block sheet, and the Euler strata
of sheets lost at infinity by `g1`.  No current promoted theorem bounds these
quantities with the sign needed to eliminate `C=P1`.

## 1. Objects kept separate

Use compactly supported topological Euler characteristic, which is additive
and satisfies constructible Fubini for complex algebraic maps.  The relevant
objects are:

```text
R       = source non-etale support in Y;
B       = g2(R), the reduced target branch/discriminant support;
g2^-1(B)= full inverse image, including possible unramified sheets;
U       = Y minus R;
W       = g2(U), an open subset of the target A2;
V       = g1(A2), an open subset of U;
M       = U minus V, the first-leg nonproperness residue.
```

Neither `U` nor `V` is obtained by deleting the full inverse image of `B`.
An unramified point of `g2` can lie over a branch value.  Likewise `g1` is not
assumed proper or surjective onto `U`, and the ruling `rho` is not assumed to
be a coordinate on the source `A2`.

The promoted fixed-sheet theorem says that every irreducible target divisor
has a generically unramified component upstairs.  Since `g2|U` is etale and
therefore open, it follows that

```text
S0=A2 minus W
```

has codimension at least two, hence is finite.  This is the cover-side content
of the constant-unit obstruction.  It is stronger than merely saying that
`B` is nonempty and is already charged by the promoted Galois-block packet.

## 2. Finite-flat source/target ledger

Choose a finite constructible stratification `{S_alpha}` of the target such
that the finite map is topologically trivial and all fibre data below are
constant on each stratum.  For `z in S_alpha`, define

```text
u_alpha = # (g2^-1(z) intersect U),
r_alpha = # (g2^-1(z) intersect R_red),
delta_alpha = sum_(y in R_z)(length_y(Y_z)-1).           (2.1)
```

All residue fields are `C`.  Finite flatness gives a fibre of scheme length
`d2`, while every point in `U` has length one.  Therefore

```text
d2=u_alpha+r_alpha+delta_alpha,
d2-u_alpha=r_alpha+delta_alpha.                         (2.2)
```

This is the exact distinction between deleting the source support and
charging the higher scheme length at its points.  Constructible Fubini gives

```text
e(U)=sum_alpha u_alpha e(S_alpha),                       (2.3)
e(R_red)=sum_alpha r_alpha e(S_alpha),
e(Y)=sum_alpha (u_alpha+r_alpha)e(S_alpha).
```

Off `B`, `u_alpha=d2`.  Since `e(A2)=1`, put

```text
D2=sum_(S_alpha subset B)(d2-u_alpha)e(S_alpha).
```

Then

```text
e(U)=d2-D2.                                             (2.4)
```

Formula (2.4) is exact, but `D2` is not a nonnegative integer count.  Its
coefficient `d2-u_alpha` is pointwise nonnegative, yet the Euler number of a
curve stratum may be zero or negative.  Thus finite flatness, the degree and
the generic inertia partitions do not by themselves give an upper or lower
bound on `D2`.

The fixed-sheet theorem says that on every one-dimensional branch stratum

```text
1<=u_alpha<=d2-2.                                       (2.5)
```

The upper bound uses the scheme length at least two of one ramified point.
It recovers `d2>=3`; the stronger no-two-block theorem is already promoted by
the Galois packet.

## 3. First-leg sheet-loss ledger

Choose a finite constructible stratification `{T_beta}` of `U` on which

```text
a_beta=#g1^-1(y),             y in T_beta,
```

is constant.  Quasi-finiteness and the normalization lemma in the promoted
block theorem give

```text
0<=a_beta<=d1,
```

with generic value `d1`; the strata with `a_beta=0` are precisely `M=U\V`.
Constructible Fubini for `g1` gives

```text
1=e(A2)=sum_beta a_beta e(T_beta)
       =d1 e(U)-D1,                                    (3.1)

D1=sum_beta(d1-a_beta)e(T_beta)=d1 e(U)-1.              (3.2)
```

Again `D1` is a signed Euler integral, not the cardinality or degree of the
nonproperness locus.  In particular, `d1>=2` supplies no sign-improving bound
beyond the exact equality (3.2).

Let `f(z)=#F^-1(z)` for the full Keller map `F=g2 g1`.  Pointwise,

```text
f(z)=sum_(y in U_z) a(y),

d1d2-f(z)
 =d1(d2-u(z))+sum_(y in U_z)(d1-a(y)).                  (3.3)
```

Euler integration of (3.3) gives only

```text
d1d2-1=d1(d2-e(U))+(d1e(U)-1),                          (3.4)
```

an algebraic identity.  It is invalid to count the target discriminant once,
then count the full inverse image or the first-leg missing sheets as a second
independent positive defect.  Formula (3.3) is the exact non-double-counting
rule.

## 4. Comparison with the ruling

The promoted ruling theorem gives

```text
e(U)=e(C)+Q,            Q=sum_t(q_t-1)>=0,               (4.1)
```

with `e(C)=1` for `A1` and `e(C)=2` for `P1`.  Combining Sections 2--3,

```text
D2=d2-e(C)-Q,
D1=d1(e(C)+Q)-1.                                        (4.2)
```

Thus the two branches require

```text
C=A1:  D2=d2-1-Q,       D1=d1(1+Q)-1;
C=P1:  D2=d2-2-Q,       D1=d1(2+Q)-1.                   (4.3)
```

The projective-base branch forces a large first-leg sheet-loss integral
`D1>=2d1-1`, but no promoted theorem bounds that integral from above.  The
finite-cover integral `D2` can have either sign.  Consequently (4.3) is a
precise threat ledger, not a contradiction.

## 5. Cubic specialization

Let `d2=3`.  At a branch value, any non-etale fibre point has scheme length
at least two.  Hence there is at most one unramified point.  The fixed-sheet
theorem makes the generic branch partition exactly `(2,1)`.  Since
`S0=A2\W` is finite, one has

```text
u(z)=3,   z outside B;
u(z)=1,   z in B minus S0;
u(z)=0,   z in S0.                                      (5.1)
```

No smoothness or irreducibility of `B` is needed.  Additivity gives

```text
e(U)=3e(A2 minus B)+e(B minus S0)
    =3-2e(B)-|S0|.                                      (5.2)
```

Comparison with (4.1) yields the exact alternatives

```text
C=A1:  2e(B)+|S0|+Q=2;
C=P1:  2e(B)+|S0|+Q=1.                                 (5.3)
```

For `C=P1`, `|S0|+Q` must be odd and
`e(B)=(1-|S0|-Q)/2`.  This is useful finite arithmetic.  It does not exclude
the branch, but it forces `e(B)<=0`; any independent proof that the actual
cubic branch support has positive Euler number would close `P1`.  One minimal
numerical pattern is

```text
e(B)=0,                     |S0|=1,                    Q=0.  (5.4)
```

Eliminating `P1` therefore requires an independent restriction on the actual
cubic discriminant topology, on totally ramified target values, or on ruling
fibre splitting.

## 6. Controls and counterexamples to naive bounds

### 6.1 Fixed degree three has unbounded cover-side Euler ledgers

Put `p(s)=s^3-3s`.  For a polynomial `phi(x,y)`, let

```text
Y_phi={p(s)=phi(x,y)} subset A3,
g_phi:Y_phi->A2_(x,y).                                  (6.1)
```

This is monic finite flat of degree three.  Its source ramification is
`s=1` or `s=-1`, and the two target branch curves are
`phi=-2` and `phi=2`.  Each branch fibre has one double ramified root and one
unramified simple root, so `g_phi(U_phi)=A2` and `S0` is empty.

For odd primes `N>=5`, take first `phi=x^N`.  The surface is smooth: a
singular point would require `s=+-1`, `x=0`, and `p(s)=0`, which is
impossible.  It is integral; the pole valuation of `x^N` rules out a root of
the cubic in `C(x,y)` when `3` does not divide `N`.  The branch support is a
disjoint union of `2N` affine lines, so

```text
e(U_phi)=3-4N.                                          (6.2)
```

For `phi=y^2+x^N`, the same Jacobian check gives a smooth surface; the pole
valuation at `y=infinity` has value `-2`, which is not divisible by three,
and rules out a rational root of the cubic, so the surface is integral.
Each of the two branch curves is a smooth affine hyperelliptic curve with
Euler number `2-N`; hence

```text
e(U_phi)=3-2(4-2N)=4N-5.                                (6.3)
```

Thus `e(U)` is unbounded in both directions at fixed `d2=3`, even for smooth
connected finite-flat covers whose generic branch inertia has a fixed sheet
and whose etale-source image is all of `A2`.

These are not block controls.  On `U_phi`, the different
`3(s^2-1)` is a nonconstant unit, contradicting the promoted condition
`O(U)^*=C^*`; no first leg is supplied.  Their exact role is to disprove any
attempt to assign a sign to `D2` using only degree, flatness and generic
ramification type.

### 6.2 The missing-point term is real

The universal monic cubic

```text
g_c:A2_(s,a)->A2_(a,b),              b=-s^3-as          (6.4)
```

has ramification parabola `a=-3s^2` and cuspidal target branch

```text
4a^3+27b^2=0.
```

Away from the cusp, a simple unramified sheet survives.  Over `(0,0)` the
fibre is `s^3=0`, so no point of `U` remains.  Therefore

```text
e(B)=1,                 |S0|=1,                 e(U)=0,
```

exactly as (5.2) predicts.  This control prevents silently replacing `W` by
all of the target.

### 6.3 The complete-base qualitative control

Let

```text
U0=(P1 x P1) minus diagonal.
```

The diagonal is ample, so `U0` is smooth affine and rational.  Projection to
either factor is an `A1`-fibration over `P1`, every fibre is `A1`, and

```text
e(U0)=4-2=2,                O(U0)^*=C^*.
```

The unit statement follows because a unit divisor would be supported on the
single diagonal, whose nonzero class is not principal.  The completion
boundary is one rational vertex, hence a forest.

In affine-quadric coordinates

```text
U0={b^2-4ac=1} subset A3,
```

the formulas

```text
a=x,        b=1+2xy,        c=y(1+xy)                   (6.5)
```

give an etale open embedding `A2->U0`; its complement is the line
`{a=0,b=-1}`.  On its image the inverse is covered by
`y=(b-1)/(2a)` when `a!=0` and `y=2c/(b+1)` when `b+1!=0`.
This realizes the first-leg topology only at generic degree
one.  It neither supplies `d1>=2` nor realizes `U0` as the maximal etale open
of the promoted non-Galois finite-flat block.  Constructing the missing
simultaneous data would be comparable to the campaign's core difficulty.

## 7. Maximum-safe conclusion and next discriminator

The exact transferable result is the pair of constructible ledgers
(2.4), (3.2), their non-double-counting identity (3.3), and the cubic closure
(5.2).  They improve the qualitative bound to a finite arithmetic gate once
`e(B)`, `S0` and the ruling excess `Q` are known.  They do not currently rule
out `C=P1`.

The cheapest decisive successors are:

1. In a fixed cubic presentation, compute the normalization Euler number of
   `B`, the totally ramified set `S0`, and `Q`.  Equation (5.3) then decides
   the base branch without any coordinate assumption on the ruling.
2. Normalize `U` in `C(x,y)` and stratify its boundary
   `Z minus A2`.  Any geometric upper bound on
   `D1=sum(d1-a_beta)e(T_beta)` below `2d1-1` eliminates `P1`.
3. If external nonproperness-curve theorems are imported later, apply them
   separately to `B subset A(F)` and to the first-leg image residue.  Do not
   identify these curves or count their Euler defects twice.

Until one of these data is charged, `C=P1` remains genuinely open.

## 8. Replay and dependencies

The desk-scale algebra replay is

```text
1fe43b65e5df6d2515d359a23c0e2bed5cddf711a0f2902e6c1888afdc66b7e8
  ops/block_descent_a1_euler_ledger_replay.py
```

Under `uv run --with sympy==1.14.0`, ordinary, `-O` and `-OO` outputs are
byte-identical, 472 bytes, with SHA-256

```text
366db8f1b34e4fe0a18599bca5c60ff68bc7f576cde0613b037a63a8a88d9a12.
```

The mutation `--mutate-cusp-sign` exits one at the cusp-discriminant check;
the script has zero Python AST `assert` nodes.  It verifies the cubic
different and critical values, the universal-cusp parametrization, the
quadric big-cell identity and etaleness, and sample values of the two
unbounded Euler families.  Euler additivity and the imported structural
theorems are mathematical inputs proved above, not software outputs.

Exact promoted dependencies are

```text
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
d49a44ce65f13f0aba35e0a034923a1362594ba8a21fef27c63cc866ec7b667a
  xmodel/bd-a2-rational-forest-morphic-correction-sol56-20260830.md
```

This packet is an exact ledger and obstruction map conditional on a proper
block.  It proves neither block occurrence nor nonoccurrence, and no result
about the primitive horn or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14712`.
- Body SHA-256:
  `4ca7432cc20b2ac5e30d87ca7a647d8454156d15baee1450a7497c7f451057f1`.
- Frozen basis: `5775cfc63803dbb99b6d4574f8e91e201790f3c0`.
