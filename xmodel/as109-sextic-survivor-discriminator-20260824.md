# AS109 sextic survivor discriminator: the full `(4,6)` gate

**Verdict: `EXACT ALGEBRAIC SURVIVOR`; the `(4,6)` family is not yet
closed.**

- Charged bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Parent: frozen sextic frontier preflight
- Field calculation: characteristic zero, temporarily in a quadratic
  algebraic differential extension of `Kbar(x)` when required
- Branches carried through every Jacobian row: `kappa=0` and `kappa!=0`
- Both polynomial constant-term boundary equations retained: yes
- Exact replay: Singular over `Q`; no coefficient/exponent enumeration
- AWS, broad support search, finite-Witt inference: none
- Full `y`-degree-at-most-six theorem: not proved
- New AS109 exclusion, lift, or JC2 inference: none

The preflight split

```text
N^2=kappa H^5,
N=3a_3H-2b_5,
a_4=H^2,                    b_6=H^3                     (0.1)
```

can be carried much farther.  After adjoining `h` with `h^2=H`, both
branches have one exact depressed normal form.  The mismatch parameter is

```text
L=0       if kappa=0,
L!=0      if kappa!=0.                                  (0.2)
```

Every nonconstant Jacobian row integrates: five rows determine the second
coordinate, and the next two give polynomial first integrals.  What remains
is an explicit algebraic curve with a regular one-form, together with two
explicit boundary equations for the rational depression.  Its weighted
compactification has exactly one point at infinity, the compositional
square/cube degeneration.  This localizes the unresolved work sharply but
does not eliminate every branch through that point.

For `L=0` the coefficient curve reduces further to one explicit plane
equation of bidegree at most `(4,4)`.  Its two obvious affine-line components are closed here using the
constant row and both boundary equations.  A nonlinear rational component
exists as an exact control, so it would be wrong to infer that the curve is
only those lines.  The remaining task is a local-normalization/pole analysis
of that plane curve and its boundary cover.  Because `(4,6)` remains open,
this task does not consume effort on the parent `(5,6)` Pfaffian system.

## 1. Trust and non-promotion

The frozen parent is
`xmodel/as109-sextic-frontier-preflight-20260824.md`.  This child independently
recomputes every `(4,6)` coefficient identity it needs.  The confirmed
quartic theorem is background only.  Provisional quintic work is neither
consumed nor promoted.

The calculation below is a family normal form, not an existence theorem.  A
rational point or trajectory on the coefficient curve is not a Keller pair
until both polynomial boundary equations and the nonzero constant last row
hold simultaneously.

## 2. Unifying the two leading branches

The preflight proved (0.1).  If `kappa!=0`, UFD valuations give

```text
H=h^2,                       N=lambda h^5,
lambda in Kbar^*.                                       (2.1)
```

The linear depression shifts then differ by `lambda/12`.  Depress the
degree-four coordinate.  In the resulting variable `z=hy+r`, the
degree-six coordinate has a constant `z^5` coefficient
`L=-lambda/2`, hence `L!=0`.

If `kappa=0`, the shifts align.  Adjoin `h` with `h^2=H` to
`Kbar(x)` if `H` is not already a square.  The algebraic differential
extension has the same algebraically closed constant field.  The common
depression gives the same normal form with `L=0`.

Thus, in both cases, over the working differential field,

```text
f=z^4+A z^2+B z+C,
g=z^6+L z^5+P z^4+Q z^3+R z^2+S z+T,                  (2.2)
```

where `L` is constant.  This is an identity in the algebraic extension; it
does not assert that `z` is a polynomial source coordinate.

## 3. Every Jacobian row

The chain rule gives `J_(x,y)=h J_(x,z)`.  The coefficients of
`J_(x,z)(f,g)` from `z^7` through `z^0` are

```text
E7 = 6A'-4P',
E6 = 5L A'+6B'-4Q',
E5 = -2AP'+5L B'+4PA'+6C'-4R',
E4 = -2AQ'-BP'+5L C'+4PB'+3QA'-4S',
E3 = -2AR'-BQ'+4PC'+3QB'+2RA'-4T',
E2 = -2AS'-BR'+3QC'+2RB'+SA',
E1 = -2AT'-BS'+2RC'+SB',
E0 = -BT'+SC'.                                         (3.1)
```

The first five equations integrate exactly to

```text
P = 3A/2+alpha,
Q = 5LA/4+3B/2+beta,
R = 3A^2/8+alpha A+5LB/4+3C/2+gamma,
S = 5LA^2/32+3AB/4+3beta A/4+alpha B+5LC/4+delta,
T = -A^3/16+5LAB/16+3AC/4+gamma A/2
    +3B^2/8+3beta B/4+alpha C+epsilon,                 (3.2)
```

for constants `alpha,beta,gamma,delta,epsilon`.

The next two equations are exact derivatives.  Define

```text
I_2 = -5LA^3/32-3A^2B/4+5LAC/4-3beta A^2/8+delta A
      +5LB^2/8+3BC+2gamma B+3beta C,                    (3.3)

I_1 = 3A^4/32-15LA^2B/32-3AB^2/4-3A^2C/4
      -3beta AB/4-gamma A^2/2+5LBC/4+delta B
      +3C^2/2+2gamma C.                                 (3.4)
```

Then

```text
E2=I_2',                 E1=I_1'.                       (3.5)
```

Hence a Keller trajectory lies on a fixed coefficient curve

```text
I_2=k_2,                 I_1=k_1.                       (3.6)
```

The last equation is

```text
h E0=jbar!=0.                                             (3.7)
```

## 4. The three-variable coefficient curve

Set

```text
U=A^2-4C.                                                (4.1)
```

Equations (3.3)--(3.4) simplify to

```text
J_2 = 5LA^3/32+3beta A^2/8-5LAU/16+delta A
      +5LB^2/8-3BU/4+2gamma B-3beta U/4 = k_2,          (4.2)

J_1 = -5LA^2B/32-3AB^2/4-3beta AB/4-5LBU/16
      +delta B+3U^2/32-gamma U/2 = k_1.                 (4.3)
```

Thus the coefficient object is the explicit affine complete-intersection
curve

```text
C_(L;k1,k2) = {J_2=k_2, J_1=k_1} in A^3_(A,B,U).        (4.4)
```

In these coordinates the last-row one-form `eta`, with
`E0=eta(A',B',U')`, is

```text
eta_A = 15LA^3/64-5LB^2/16-5LAU/32+3beta A^2/8
        +3BU/16-gamma B/2+delta A/2,
eta_B = -5LAB/16-3B^2/4-3beta B/4,
eta_U = -15LA^2/128+5LU/64-3beta A/16-delta/4.          (4.5)
```

The exact differential gate is therefore

```text
dJ_2(X')=0,          dJ_1(X')=0,
h eta(X')=jbar!=0,             X=(A,B,U).                (4.6)
```

Unlike the parent `(5,6)` gate, no non-exact intermediate Pfaffian row
remains.  The obstruction has moved entirely to the algebraic curve, its
one-form, and the polynomial boundary cover below.

## 5. Both polynomial boundary equations

Let

```text
D_0=f(x,0),          G_0=g(x,0),
q=r^2+A/2,
E_0=G_0-alpha D_0-epsilon.                              (5.1)
```

Here `D_0,E_0` are polynomials in the original `x`.  Exact substitution of
`C=(A^2-U)/4` in (2.2) gives the first boundary

```text
D_0 = rB+q^2-U/4.                                       (5.2)
```

The second boundary is

```text
E_0 = 3Lr^5/8-5Lr^3q/4-beta r^3/2+5Lr^2B/8
      +15Lrq^2/8+3rqB/2+3beta rq/2-5LrU/16+delta r
      +q^3+5LqB/8-3qU/8+gamma q+3B^2/8+3beta B/4.      (5.3)
```

Equations (4.2), (4.3), (5.2), and (5.3) are four exact algebraic equations
for the four initially rational quantities `r,q,B,U`; `A=2q-2r^2`.
They are the full boundary cover of the coefficient curve.  Dropping either
(5.2) or (5.3) would enlarge the survivor illegitimately.

## 6. Weighted infinity: one point, not yet no points

Give `(r,q,B,U)` weights `(1,2,3,4)`.  The highest weighted parts of the
four equations are

```text
F_inf = rB+q^2-U/4,
G_inf = q^3+3rqB/2-3qU/8+3B^2/8,
J2_inf = -3BU/4,
J1_inf = 3r^2B^2/2-3qB^2/2+3U^2/32.                   (6.1)
```

Their only common weighted-projective point is

```text
[r:q:B:U]=[1:0:0:0].                                   (6.2)
```

Indeed, `B=0` in `J2_inf` forces `U=0` from `J1_inf`, then `q=0` from
`F_inf`.  If instead `U=0` and `B!=0`, `J1_inf` gives `q=r^2`.  When
`r=0`, `G_inf=3B^2/8!=0`; when `r!=0`, `F_inf` gives `B=-r^3`, and then

```text
G_inf=-r^6/8!=0.                                        (6.3)
```

The point (6.2) is exactly the compositional degeneration

```text
f_inf=w^2,              g_inf=w^3.                      (6.4)
```

This is why a naive monic-elimination argument fails.  The lower-weight
terms, including the mismatch `L`, determine the formal branches through
(6.2).  The replay verifies the full equations needed for that local
normalization, but this report does not claim that every branch has been
eliminated.

## 7. The aligned branch `L=0`: an explicit plane curve

For `L=0`, put

```text
X=B+beta,                 V=U-8gamma/3,

Phi(A)=4delta A/3+beta A^2/2
       -4(k_2+2beta gamma)/3,                            (7.1)

R(A,X)=8AX(X-beta)-32delta(X-beta)/3
       +32(k_1+2gamma^2/3)/3.                            (7.2)
```

Equations (4.2)--(4.3) become exactly

```text
XV=Phi(A),                 V^2=R(A,X).                  (7.3)
```

Eliminating `V` gives the explicit plane curve

```text
Phi(A)^2 = X^2 R(A,X).                                  (7.4)
```

Thus the smallest aligned survivor is not an unspecified ODE: it is the
normalization of the plane curve (7.4), equipped with the pulled-back
one-form (4.5) and the boundary cover (5.2)--(5.3).

### 7.1 Two line components close

The first obvious line family occurs when `beta=delta=0`, `B=0`, and `V`
is constant while `A` varies.  On it `eta=0`, contradicting (4.6).  It
cannot support a Keller trajectory.

The second line family has

```text
delta=0,                 A=0,                 V=0,       (7.5)
```

with `B` variable and the levels fixed accordingly.  Along it

```text
eta=-(3/4)B(B+beta)dB.                                  (7.6)
```

Allowed target translations put `gamma=C=0` on this line.  Writing

```text
D=D_0,
E=G_0-alpha D_0-epsilon,
```

the two boundary equations eliminate `B` to the monic equation

```text
r^8-2beta r^5-6D r^4+8E r^2-6beta D r-3D^2=0.          (7.7)
```

Hence `r` is integral over `Kbar[x]`; the quadratic second boundary then
makes `B` integral as well.

If `H=h^2` in the base field, `h,r,B` are polynomials.  Equation (4.6) is a
nonzero constant product

```text
-(3/4)h B(B+beta)B'=jbar,                               (7.8)
```

so every factor is a unit.  In particular `B` is constant, contradicting
`B'!=0`.

If `H` is nonsquare, conjugation sends `h,r,B` to their negatives and fixes
the base field; the coefficient formula forces `beta=0`.  Put

```text
K=B^2,                  M=hB.                           (7.9)
```

Both are invariant and integral, hence lie in `Kbar[x]`.  Also
`M^2=HK`.  The constant row becomes

```text
-(3/8)M K'=jbar.                                        (7.10)
```

Thus `M` is a unit, while `M^2=HK` forces both `H` and `K` to be units;
then `K'=0`, contradicting (7.10).  Therefore the second line component is
also closed in both square and nonsquare leading branches.

### 7.2 A nonlinear rational control survives the coefficient equations

It would be false to conclude that (7.4) consists only of those lines.  At

```text
beta=1,       gamma=delta=k_1=k_2=0,
```

the exact polynomial parametrization

```text
A=t+t^4/32,
B=t^3/32,
U=t^2/2+t^5/64                                           (7.11)
```

satisfies both first-integral equations.  The pulled-back last-row form is

```text
eta = (3/262144)t^2(t^3+32)(5t^6+122t^3+512) dt.        (7.12)
```

For a nonconstant polynomial `t(x)`, (7.12) is not a nonzero constant;
this particular coefficient component therefore fails (4.6) when `h` is a
polynomial.  It remains an essential negative control: any claimed general
closure must handle nonlinear components of (7.4), not just the two line
families.

The unresolved aligned gate is to normalize all parameter specializations
of (7.4), pull back `eta`, and use both equations (5.2)--(5.3) at every place
over the infinity point (6.2).

## 8. The mismatch branch `L!=0`

For `L!=0`, the exact survivor is the complete intersection
`C_(L;k1,k2)` in (4.2)--(4.4), with differential (4.5) and boundary cover
(5.2)--(5.3).  The `L`-terms first appear one weighted layer below the
square/cube point (6.2).  They are not a target shear and cannot be dropped.

This report deliberately does not assert that the mismatch kills every
formal branch.  A valid closure must compute the local normalization of the
four-equation boundary system at (6.2), not merely observe a nonzero
`L r^5` or `L A^3` term: fractional Puiseux corrections can occur at the
same lower layer.  The frozen equations now make that calculation finite and
unambiguous.

Thus the smallest mismatch survivor is

```text
(C_(L;k1,k2), eta, boundary cover (5.2)--(5.3)), L!=0.  (8.1)
```

No characteristic-zero Keller pair realizing (8.1) has been found.

## 9. Exact replay

Run:

```text
Singular -q cases/as109_sextic_survivor_discriminator_20260824/verify_46_discriminator.sing
```

The replay checks over `Q`:

- the full Jacobian expansion (3.1), with every summand derived from (2.2);
- all five integrated coefficient formulas (3.2);
- `E2=I_2'`, `E1=I_1'` and the transformed curve (4.2)--(4.3);
- every coefficient of the last-row form (4.5);
- both boundary equations (5.2)--(5.3);
- the exact infinity rejection (6.3);
- both shifted identities (7.3) and hence the plane curve (7.4);
- the monic line-component resultant (7.7);
- the nonlinear control (7.11) and the exact factorization (7.12).

Expected output is

```text
PASS-SEXTIC-46-SURVIVOR-DISCRIMINATOR
full_sextic_theorem_proved=false
lift_found=false
jc2_inference=false
```

No enumerator or exponent rectangle is present.

## 10. Exact next gate

The fastest next bounded calculation is local normalization at (6.2):

1. homogenize (4.2), (4.3), (5.2), and (5.3) with weights `(1,2,3,4)`;
2. compute every Puiseux branch through `[1:0:0:0]`, separately for `L=0`
   and `L!=0`;
3. pull back `eta` and both boundary functions to each branch;
4. reject a branch only if a pole remains in a boundary polynomial or
   `h eta` cannot be a nonzero constant.

Only after every branch is rejected may `(4,6)` be closed and work move to
the parent `(5,6)` Pfaffian system.  This report does not prove the
`y`-degree-at-most-six theorem, raise the AS109 degree floor, construct a
lift, or decide JC2.

## 11. Provenance

The exact artifact hashes are frozen in
`cases/as109_sextic_survivor_discriminator_20260824/FREEZE.sha256` after the
final replay.  Inputs:

| Artifact | SHA-256 | Status/use |
|---|---|---|
| `xmodel/as109-sextic-frontier-preflight-20260824.md` | `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | frozen parent |
| `cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py` | `21bc494f552587ee0b64c01c735b2f1243eafce9599f1e05bc526d23e38f73ad` | parent replay |
| `xmodel/as109-quartic-discriminator-gate-20260824.md` | `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276` | confirmed background only |

No parent, review, canonical file, ledger, or AWS resource was edited.
