# `WEIGHT-AT-ATYPICAL`: an exact type-(2,3) analytic Keller surrogate

Author: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `31777ce90994a106aade85064c0d868e32863f94`  
Lifecycle: `PROVISIONAL / INTERNAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED`  
Evidence tier: `EXACT LOCAL-ANALYTIC SURROGATE / NOT A POLYNOMIAL MAP`

## 0. Result

The proposed bridge

```text
an atypical value of f  =>  at least one unit of Section-7 actual-weight excess
```

is not implied by the following isolated pointwise ingredients: an analytic
Keller boundary chart, the same local-degree cluster rule and proper-tube
conservation used in Section 7, a boundary collision, a local Milnor cycle,
and the normalized degree ratio `2:3`.

There is an exact analytic boundary-chart control, defined over the whole
parameter line `A1_t`, with all of those features for which

```text
P(z)=z^2,                    Q(z)=z^3+z,
u=3, kappa^-=kappa^+=1,     b^+=kappa^+(u-1)=2,
w_an(z)=2 for every z,      I_an=integral_(A1) w_an dchi_c=2,
b^+=2,                      I_an-b^+=0,
```

while `a=0` is a holomorphic Morse degeneration at the boundary and hence
has one local Milnor cycle.  Thus even the analytic-profile analogue of
`EXCESS-1` fails at this exact local interface.

This is not a global polynomial Keller pair, does not construct the
source-complete Section-7 quotient bijection or `d-N` pushforward, and does
not refute `WEIGHT-AT-ATYPICAL`, `PCB-EXCESS`, PCB, or JC2 on actual
polynomial maps.  It proves only a local dependency barrier: any proof must
use something beyond the listed pointwise analytic data, such as the
single-valued rational/polynomial origin of the boundary functions or a
global filling identity.  A local Milnor cycle and the Chau-compatible
degree ratio alone are insufficient.

## 1. Exact local Keller chart

Use the boundary chart already admitted by the hostile-reviewed Section-7
proper-tube control,

```text
s=y^(-1),       t=x y^3,
x=t s^3,        y=s^(-1).
```

Then

```text
dx wedge dy = s ds wedge dt.
```

Choose the analytic square-root branch on, for example, any disc
`|s|<rho<sqrt(2/3)`, and put

```text
R(s)=sqrt(1+3s^2/2),        A(s)=(2/3)(R(s)-1),
f(s,t)=t^2+A(s),            g(s,t)=t^3+tR(s).        (1.1)
```

These are holomorphic on `A1_t` times that fixed small `s`-disc.  Since
`R'(s)=3s/(2R(s))` and `A'(s)=s/R(s)`, one has

```text
f_s=s/R,       f_t=2t,
g_s=3st/(2R),  g_t=3t^2+R,

df wedge dg = {s(3t^2+R)/R - 2t(3st)/(2R)} ds wedge dt
            = s ds wedge dt
            = dx wedge dy.                           (1.2)
```

Thus the local Jacobian is exactly one on the affine chart.  In the original
variables the same control is the algebraic-analytic pair

```text
R=sqrt(1+3/(2y^2)),
f=x^2 y^6+(2/3)(R-1),
g=x^3 y^9+x y^3 R,
```

which makes the missing global condition explicit: the pair is algebraic
and analytic near this boundary component, but it is not a polynomial pair
(nor a rational pair on the original affine plane).  The exact differential
calculation (1.2), not the displayed change of coordinates alone, is the
evidence.

On the boundary `s=0`, the residual value map is exactly

```text
z=t,       (P(z),Q(z))=(z^2,z^3+z).                 (1.3)
```

It has degree ratio `deg P:deg Q=2:3`, the normalized type relevant to the
active U1 laboratory.  The parametrized value curve has a finite
self-intersection at `(P,Q)=(-1,0)`, coming from `t=+-i`; this does not merge
the two source parameters.  In an actual Section-7 packet, direction
clusters and weights likewise live on the source quotient line before their
values are pushed to the target.

## 2. The value `a=0` has the local Morse geometry of atypicality

At the boundary point `(0,0)`,

```text
df(0,0)=0,
Hess_(s,t) f(0,0)=diag(1,2).
```

Hence `f` has a nondegenerate holomorphic critical point on the boundary.
Equivalently, its central fibre has an ordinary node there.  Indeed, on
`f=0`,

```text
R=1-(3/2)t^2,
s^2=-2t^2+(3/2)t^4=-2t^2(1-3t^2/4),                (2.1)
```

where the equality after squaring is equivalent on the chosen square-root
branch near the origin.  This has two normalized analytic branches.  A
nearby fibre `f=a!=0` is the Milnor smoothing.  The local Milnor number is
one, so the extended analytic function has one local Milnor cycle.  In a
compactified polynomial setting this is local geometry that can contribute
to atypicality at infinity; this analytic model alone does not certify a
globally atypical value of a polynomial map.

The affine Keller condition is not contradicted: the critical point lies on
the removed boundary `s=0`, where the pulled-back affine area form itself has
the factor `s`.

## 3. Exact analytic local-degree profile

Read the chart through the height-three notation of the reviewed Section-7
local model.  Its strict prefix has lattice index one and its coefficient
quotient is unramified, so the formal comparison data are

```text
u=3,       kappa^-=kappa^+=1,       b^+=2.           (3.1)
```

### 3.1 Nearby simple directions

Fix any `t_0!=0` and set `a=P(t_0)=t_0^2`.  (For a nearby generic value these
are the two simple roots `t_0=+-sqrt(a)`.)  On the fibre `f=a`, implicit
expansion at that boundary point gives

```text
t-t_0 = -s^2/(4t_0) + O(s^4),
R=1+(3/4)s^2+O(s^4),
g-(t_0^3+t_0) = -s^2/(4t_0) + O(s^4).              (3.2)
```

Thus each simple direction is a singleton analytic cluster of local
`g`-degree two.  This agrees numerically with repaired Proposition 7.3:

```text
w_an(t_0)=b^+=2.                                     (3.3)
```

### 3.2 The Morse-collision direction

At `a=0`, the two branches in (2.1) share the coefficient direction `z=0`.
On each normalized branch, `t` is a uniformizer and

```text
g=t-(1/2)t^3
```

has local degree one.  They form one analytic direction cluster, so its
local-degree profile is the sum

```text
w_an(0)=1+1=2=b^+.                                  (3.4)
```

Consequently the constructible analytic profile on the whole parameter
line is constant:

```text
w_an(z)=2 for all z in A1.                           (3.5)
```

Compactly supported Euler integration of this profile and its formal
height-three baseline therefore give

```text
I_an=integral_(A1)w_an dchi_c=2,
b^+=kappa^+(u-1)=2,
I_an-b^+=0.                                          (3.6)
```

There is no strict local-degree specialization and no unit of profile
excess, even though the boundary fibre has a nontrivial local Milnor cycle.
The notation `w_an` is deliberate: without polynomial-origin
Eggers--Wall/tree realization this is not asserted to be an actual weight
in the global Section-7 pushforward identity.

## 4. What this rules out

The example is simultaneously a negative control for three proposed
pointwise proof mechanisms.

1. **Local Morse geometry alone.** A boundary Morse degeneration need not
   make `w_an(z)>b^+` at the exceptional parameter.
2. **Pointwise Milnor-cycle injection.** A nonzero local Milnor-cycle space
   need not inject into analytic local-degree excess: here its dimension is
   one and the profile excess is zero.
3. **Profile-level budget transfer.** Since `I_an-b^+=0`, the local profile
   has no saved unit to transfer across parameter values.

The control preserves the distinctions among a normalized boundary branch,
an analytic direction cluster, and its source parameter.  The two special
normalized branches belong to one analytic direction and contribute local
degrees `1+1`; they are not counted as two parameter points.

It does not rule out a theorem using the full global Section-7 Euler
package, the rationality forced by polynomial origin, simultaneous behaviour
at every boundary component, an algebraic compactification identity
unavailable to arbitrary analytic germs, or a new signed global invariant.
Such an input must be named and used essentially; the isolated pointwise
ingredients instantiated here cannot supply it.

## 5. Provisional disposition and next discriminator

At the present evidence tier:

```text
ATYPICAL-EXISTENCE for a nonproper Keller map:            retained;
local Morse data => analytic profile EXCESS-1:            false in surrogate;
atypical => actual EXCESS-1 for polynomial Keller maps:   open;
Milnor cycles => actual Section-7 weight excess:          open;
PCB-EXCESS / PCB on actual polynomial maps:               open;
```

The next honest gate is a theorem whose hypotheses exclude (1.1)
through actual-map provenance--for example rational/polynomial origin on the
affine plane together with the complete quotient pushforward.  Candidate
inputs must produce a strict inequality at the quotient collision, not
merely identify a critical value, a Milnor number, or nontrivial monodromy.
This surrogate alone does not stop `WEIGHT-AT-ATYPICAL`; it shows exactly
which pointwise argument is insufficient.

No CAS, AWS, web, or formalization action was used.  All calculations above
are exact differential and one-variable local-series identities.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8993`.
- Body SHA-256:
  `80b6fd58a0a141ec1a395c064c92bd2f7e206aa9eec9af15aea285aa69c6e350`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
