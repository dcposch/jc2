# `(8,12)` order two: affine-`mu2` DVR rigidity and minimal `P3`

Date: 2026-08-26

Status: **SCOPED CHARACTERISTIC-ZERO LAURENT-VALUATIVE THEOREM AND
CORRECTION-AWARE SOURCE DESIGN.  THE DUAL-AWS `P2` PRODUCER PASSES, BUT
THE TOTAL-REES PULLBACK, HOSTILE REVIEW, TERMINAL CLIENT, AND BOTH TAYLOR
CLIENTS REMAIN OPEN.**

## 0. Frozen inputs and producer custody

The proof below uses the printed characteristic-zero equations and the hand
`D(c)` elimination.  The exact-Q AWS lane is supporting producer custody;
the good-prime lane is an independent software control and is not a lifting
argument.

```text
20cc74b60fdf0b599094c8b5d6cf61e48773391d3c861409ef0e20f4a8a85ff2
  xmodel/max12-812-order2-exact-square-affine-mu2-hand-elimination-20260826.md

9ed24f7f40b06b096c789fa5134db1f98ba11c6b3a3ef52d27b778b6224376aa
  cases/max12_812_order2_exact_square_affine_mu2_20260826/REGISTRATION.md
4eb04bca26c3bee1c76534f8fc02efdbb982316071e583676b65fb395f5f2c4b
  cases/max12_812_order2_exact_square_affine_mu2_20260826/compile_affine_mu2.py
88440f2a46078f0c9708587ea6db8c6d4f3e5f306affe35c94d2da521e8d4e5e
  cases/max12_812_order2_exact_square_affine_mu2_20260826/FREEZE.sha256

bf95fc3eff42375b6ee2adf77ab18bccd2d3f4e5f89092f050910fe3929c53e5
  cases/max12_812_order2_exact_square_affine_mu2_20260826/aws_q_v2/compiled/affine_mu2_q.sing
f446cae9b4158cb40317c41b23e78175a999031a4203e5682b956fb2ed250847
  cases/max12_812_order2_exact_square_affine_mu2_20260826/aws_q_v2/run/max12_812_order2_affine_mu2_20260826T122600Z_q_v2.stdout
9575c7da92a578d8a447fff4e9ed23ff7d32b72f6d6b27d1fa433325defe497d
  cases/max12_812_order2_exact_square_affine_mu2_20260826/aws_q_v2/run/max12_812_order2_affine_mu2_20260826T122600Z_q_v2.validation

46b5c21dbf0a6cf743dc1ce8523fbd8fb9d0f2d466b6663376c206dd88591d5c
  cases/max12_812_order2_exact_square_affine_mu2_20260826/aws_p65521_v2/compiled/affine_mu2_p65521.sing
b481b3930d964b88a2b5d65d70ff4e5cd362fd81867968fc65e82fb3042aa1e7
  cases/max12_812_order2_exact_square_affine_mu2_20260826/aws_p65521_v2/run/max12_812_order2_affine_mu2_20260826T122600Z_p65521_v2.stdout
9575c7da92a578d8a447fff4e9ed23ff7d32b72f6d6b27d1fa433325defe497d
  cases/max12_812_order2_exact_square_affine_mu2_20260826/aws_p65521_v2/run/max12_812_order2_affine_mu2_20260826T122600Z_p65521_v2.validation
```

Both V2 validators say `PASS_AFFINE_MU2_PROBE`.  Both engines return the
three proposed reduced components.  The V1 directories remain immutable
deployment-negative custody: their mathematics completed, but redundant
library-loading diagnostics made their stdout inadmissible as evidence.

## 1. Laurent receiver

Over a characteristic-zero field put

```text
Q=z^4+p*z^2+c*z+r,
H=sqrt(Q)*(Q^2+beta*Q+gamma),
H-[H]_+=sum_(ell>=1) h_ell*z^(-ell).                 (1.1)
```

The affine target face is

```text
h1=h3=h4=h5=h6=h7=0,             h2=mu2.            (1.2)
```

The new component of its reduced support is

```text
p=c=0,
5*r^2+8*r*beta+16*gamma=0,
32*mu2=r^2*(5*r+4*beta).                            (1.3)
```

Write

```text
t=5*r+4*beta.                                       (1.4)
```

On (1.3),

```text
beta=(t-5*r)/4,
gamma=r*(5*r-2*t)/16,
mu2=r^2*t/32.                                       (1.5)
```

The open `D(r*t)` is the genuinely affine-target part.  The boundary
`t=0` is the zero-target Chebyshev receiver and `r=0` is the square limit.

## 2. DVR horizontal-rigidity theorem

Let `A` be a DVR containing `Q`, or more generally a local integral
`Q`-algebra with fraction field `F`.  Let an `A`-valued tuple satisfy
(1.2), and suppose its image in the residue field lies on (1.3) with

```text
bar(r)*bar(t) != 0.                                  (2.1)
```

Then the entire tuple, not only its leading point, factors through (1.3):

```text
p=c=0,
gamma=r*(5*r-2*t)/16,
mu2=r^2*t/32                                        (2.2)
```

in `A`.  In particular every coefficient jet of `p` and `c` is zero.

### Proof

The hand elimination proves that (1.2) has no geometric point on `D(c)`
over any characteristic-zero field.  If `c` were nonzero in `A`, it would
be nonzero in `F`; after extending `F` to an algebraic closure this would
give a forbidden `D(c)` point.  Hence `c=0` in `A`.

On `c=0` the printed equations give the exact identity

```text
h4=-(p/2)*h2.                                       (2.3)
```

Condition (2.1) and the closed-point equation (1.5) make `mu2=h2` a unit
of `A`.  Thus (2.3) forces `p=0`.  At `p=c=0`, the exact rows are

```text
h6=-r^2*(5*r^2+8*r*beta+16*gamma)/128,
h2=(5*r^3+6*r^2*beta+8*r*gamma)/16.                 (2.4)
```

Now `r` is a unit.  The first equation in (2.4) gives the relation in
(1.3), and substituting it into the second gives (1.5).  This proves
(2.2).

This is a valuative statement about maps from reduced domains.  It neither
identifies the raw nonreduced scheme nor says that an arbitrary total-Rees
correction continues to satisfy the same unforced equations (1.2).

## 3. The four-pivot block

The same formulas give a smaller correction client even when literal
source corrections add inhomogeneous forcing.  Treat `(r,mu2)` and all
source-correction variables as parameters, and use `(p,c,beta,gamma)` as
four pivot variables.  At (1.3), order the four rows as

```text
G=(h4,h5,h6,h2-mu2).                                (3.1)
```

The nonzero blocks of its Jacobian are

```text
d(h4)/d(p)=-r^2*t/64,
d(h5)/d(c)=-r^2*t/64,

             beta       gamma
h6          -r^3/16     -r^2/8
h2-mu2       3*r^2/8      r/2.                      (3.2)
```

Therefore

```text
det dG/d(p,c,beta,gamma)=r^8*t^2/2^18.              (3.3)
```

It is a registered unit on `D(r*t)`.  Thus every successive literal source
coefficient has a unique formal solution for the four pivot corrections,
provided its leading four-row block is source-certified to be (3.2).
After this solve, only the Schur-reduced rows

```text
(h1,h3,h7)                                          (3.4)
```

remain as Kuranishi obstruction rows.  On the unforced Laurent receiver
they vanish identically and Section 2 applies.  In the total source they
must be recomputed; they are not zero by analogy.

This reduces generic affine-`mu2` `P3` from a five-variable component
decomposition to four triangular pivots plus three exact residuals.

## 4. Smallest literal `P3` pullback

The compiler must begin with the actual ordinary source

```text
Phi_ell = r_ell(C,Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)
          -Lambda^(12+ell)*delta_ell,

(delta_1,...,delta_7)=(0,mu2,0,mu4,0,mu6,J/4).      (4.1)
```

It must form the common-load total-Rees chart before setting its exceptional
parameter to zero.  On `D(k10)` it may normalize the leading `k10` only
after printing the two-sided unit change.  The normalized leading load
coordinates called `(1,beta,gamma)` must be derived from (4.1), including
all toric powers; naive unweighted ratios are not a source map.

The minimal exact client has two gates.

### Gate A: source identification

Retain, without radical or early elimination:

1. all coefficients of `C`, including the four square-normal defects;
2. every moving jet of `p,c,r` and of all three loads;
3. `mu2,mu4,mu6,J` at their exact weights and every target jet licensed by
   the ordinary source;
4. the inverse-root/Faber connection and the total-Rees kernel, including
   torsion; and
5. both root orientations and the deck action if the Kummer separation
   coordinate is still present.

After the exact divided-row extraction, Gate A must print that the leading
seven rows are precisely (1.2), with the frozen integer denominators, and
that the four-pivot coefficient is exactly (3.3).  Failure of either check
stops the Laurent import.

### Gate B: correction solve

Emit coefficients sequentially from the first post-`P2` grade through
absolute grade thirty-eight.  At each grade:

1. keep the raw predecessor ideal;
2. use (3.1)--(3.3) to solve the four pivot corrections over
   `D(k10*r*t)`;
3. substitute them into the three residual rows (3.4); and
4. print one of the typed endpoints below.

```text
PURE_RECEIVER
  Every external forcing term in the seven rows is zero.  Apply Section 2,
  keep p=c=0 identically, and route the rational (r,t) family to terminal
  and Taylor clients.

FORCED_TRANSVERSE
  Square-normal, connection, lower-load, or target terms force pivot
  corrections.  Preserve their exact solution and test the three residuals;
  do not invoke horizontal rigidity.

ROUTE_CHEBYSHEV
  t=0.  Return to the reviewed zero-target Pell/Chebyshev receiver.

ROUTE_SQUARE
  r=0.  Return to the exact-square higher-contact receiver.

ROUTE_K10_ZERO
  k10=0.  Start the two-load projective boundary; do not take a limit of
  beta or gamma.
```

The following terms can invalidate `PURE_RECEIVER` and therefore must be
present before Section 2 is consumed:

- the first nonzero square-normal defect of `f`;
- an inverse-root or Faber connection at the same divided grade;
- a load jet not absorbed by the certified `(1,beta,gamma)` coordinates;
- `mu4`, `mu6`, or `J` tying a correction row;
- a moving base/Kummer coordinate; and
- total-Rees torsion or a base-change discrepancy.

The pivot theorem survives such forcing as a solver design only if Gate A
certifies the same leading unit block.  The conclusion `p=c=0` does not.

## 5. Pell sentinels, terminal, and Taylor

On (1.5), with `x=z^2`, the exact remainder is

```text
A^2-Q*P(Q)^2
 =-(r^2*t/16)*x^4
  -(r^2*t*(t+5*r)/64)*x^2
  -r^3*(r+2*t)^2/256.                               (5.1)
```

Three subloci are mandatory controls:

```text
t=0:   remainder=-r^5/256                    (Chebyshev),
t=r:   remainder=-r^3*(4*x^2+3*r)^2/256,
t=4*r: remainder=-r^3*(8*x^2+9*r)^2/256.            (5.2)
```

The first negative coefficient after the seven tested Laurent rows is

```text
h10=-r^4*(t-r)/512.                                 (5.3)
```

Thus `t=r` is a sharp next-tail sentinel.  But `h10` is outside the seven
ordinary source rows; neither (5.2) nor (5.3) is an extra source equation.
They are compiler controls and possible terminal/Taylor stratifiers only.

Every survivor must be pulled independently to:

1. the exact terminal `U=2,[6,2]` client, including `8*r7'=j/u`; and
2. both finite Taylor families with the actual global coefficient
   functions.

A principal-part match, the polynomial `A` in (5.1), or a deck-symmetric
remainder is not a two-sided source-to-Taylor map.

## 6. AWS shards and stop rules

Use one exact-Q AWS lane and one independent good-prime lane on different
hosts, one capped core per process unless profiling justifies more.

```text
P3-A: total-Rees/source map and leading four-pivot identity;
P3-B: D(k10*r*t) triangular correction solve and three residuals to grade 38;
P3-T: terminal [6,2] pullback for each survivor;
P3-X0, P3-X1: the two Taylor pullbacks.
```

Launch `P3-T`, `P3-X0`, and `P3-X1` provisionally as soon as `P3-B` has a
source-certified survivor; hostile review runs in the background.

Stop a shard at the first raw localized unit, a certified route in Section
4, a source-map failure, or one explicitly normalized survivor.  A radical
unit, modular-only unit, missing target/load, or omitted correction is no
verdict.  Do not spend on grade thirty-eight or Taylor after a raw earlier
unit, and do not stop at a nonempty leading receiver.

## 7. Explicit nonclaims

This note does not promote the P2 radical calculation, identify its raw
nonreduced ideal, or prove that the common-load total-Rees chart has (1.2)
as its literal base change.  It does not say total-source corrections keep
`p=c=0`, does not constrain the `k10=0` boundary, and does not prove either
Taylor family or the terminal passport.  It neither constructs nor excludes
a strict arc and does not close the square branch, order two, `(8,12)`,
maximum twelve, or JC2.
