# D3 raw-degree-three local counter-control R1: corrected `IV*` floor

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, independent audit lane  
Frozen basis: `6d26a4b1e18c2f64862edd5e0a1ce8f0f0a36104`  
Lifecycle: **EXACT PROVISIONAL CORRECTED COUNTER-CONTROL / REVIEW REQUIRED**

## 0. Mandatory supersession and verdict

This report supersedes

```text
82f930fff174c2b599e5965459c6e2eb0c10117cfca084bc8116ddf82bbac79d
  xmodel/bd-a2-d3-local-degreecap-countercontrol-sol56-20260830.md
```

in full.  The earlier sealed report dropped one factor of `t` when permuting
the terminal ternary cubic into the CFS Lemma 3.14 form.  Its counterexample,
two `(1,1)` drops, raw degree, solubility and normality are correct, but its
terminal `I_0^*` label and valuations `(infinity,3,6)` are **RETRACTED**.

The corrected terminal equation is

```text
V^2=U^3-t^4,
```

so the minimal fibre is `IV*` with valuations `(infinity,4,8)`.  Accordingly
the level-one and level-two discriminant orders are `20` and `32`, not `18`
and `30`.

The main verdict is unchanged and exact: the conjectured local impossibility
is **false**.  Over `R=C[[t]]`,

```text
Phi(t;x,y,z)=(x+tz)^3+t y^3+t^3x^2y                    (0.1)
```

has literal raw `t`-degree at most three, normal integral total surface,
smooth `C((t))`-soluble generic cubic, exact CFS level two, two admissible
Smith pairs `(1,1)`, and a minimal additive `IV*` floor.

## 1. Raw model and two admissible drops

Expansion gives

```text
Phi=x^3+3t x^2z+3t^2xz^2+t^3z^3+t y^3+t^3x^2y.         (1.1)
```

Thus every raw coefficient has `t`-degree at most three, the model is
primitive, and

```text
Phi(-t,0,1)=0.                                          (1.2)
```

Put `X=x+tz`, an integral determinant-one shear.  Then

```text
Phi'=X^3+t y^3+t^3(X-tz)^2y.                            (1.3)
```

Two direct integral transforms are

```text
Phi_1=t^(-3)Phi'(tX,ty,z)
     =X^3+t y^3+t^3(X-z)^2y,                            (1.4)

Phi_0=t^(-3)Phi_1(tX,ty,z)
     =X^3+t y^3+t(tX-z)^2y                              (1.5)
     =X^3+t y^3+t z^2y-2t^2Xzy+t^3X^2y.
```

After reordering coordinates as `(z,X,y)`, each arrow is

```text
[mu,M]=[t^(-3),diag(1,t,t)].                            (1.6)
```

This is CFS admissible pair `(a,b)=(1,1)`, because `a+b+1=3`.
Moreover

```text
v(mu det M)=-1,                                         (1.7)
```

so each arrow lowers the invariant valuations by `(4,6,12)` and the level by
one once `Phi_0` is verified minimal.  This legal `(1,1),(1,1)` branch alone
refutes any universal no-go based on exhausting
`(0,1),(1,1),(1,2),(2,3)`.

## 2. Correct terminal invariant calculation

The point `[X:y:z]=[0:0:1]` lies on `Phi_0`.  Set the CFS Lemma 3.14
coordinates to

```text
(X_lemma,Y_lemma,Z_lemma)=(X,z,y).
```

The terminal equation is

```text
X^3+tZ^3+t(tX-Y)^2Z=0,                                 (2.1)
```

not the equation with coefficient one on `Z^3` printed in the superseded
report.  In the form `f1Y^2-f2Y-f3=0`, the correct forms are

```text
f1=tZ,
f2=2t^2XZ,
f3=-(X^3+tZ^3+t^3X^2Z).                                (2.2)
```

The associated generalized binary quartic is

```text
w^2+2t^2XZ w
  =-tX^3Z-t^2Z^4-t^4X^2Z^2.                            (2.3)
```

Completing the square with `W=w+t^2XZ` gives

```text
W^2=-tX^3Z-t^2Z^4=-tZ(X^3+tZ^3).                       (2.4)
```

In the affine chart `Z=1`, put `U=-tX` and `V=tW`.  Then

```text
V^2=U^3-t^4.                                            (2.5)
```

Thus

```text
v(c4(Phi_0))=infinity,
v(c6(Phi_0))=4,
v(Disc(Phi_0))=8.                                      (2.6)
```

Tate's algorithm in residue characteristic zero gives Kodaira type `IV*`.
The Weierstrass equation is minimal because `v(c6)=4<6`.  Hence `Phi_0` has
CFS level zero.  Equations (1.7) and (2.6) now give

```text
                 Phi_0       Phi_1       Phi
v(c6)               4           10         16
v(Disc)              8           20         32
CFS level            0            1          2.         (2.7)
```

In particular the source model has exact level two and satisfies the promoted
upper gate `v(c6)=16<18`.

As an independent check, projection from `P=[0:0:1]` by setting `y=sX` in
the affine chart `z=1` factors off `X` and leaves

```text
(1+t s^3+t^3s)X^2-2t^2sX+ts=0.
```

Its quadratic discriminant is

```text
-4ts(1+t s^3),                                         (2.8)
```

the same binary-quartic class as (2.4).  It has invariant orders `4,8`,
confirming the correction.

## 3. Smooth generic cubic and normal total surface

Let `u=x+tz`.  On the generic fibre,

```text
Phi_z=3tu^2,
Phi_x=3u^2+2t^3xy,
Phi_y=3ty^2+t^3x^2.
```

A singular point would have `u=0`, then `xy=0` and
`3y^2+t^2x^2=0`.  If `x=0`, then `z=0` and projectivity forces `y!=0`, a
contradiction.  If `y=0`, then `x=0` and consequently `z=0`, also impossible.
The generic cubic is smooth.

On the closed fibre,

```text
Phi|_(t=0)=x^3,
(Phi_x,Phi_y,Phi_z,Phi_t)|_(t=0)
  =(3x^2,0,0,3x^2z+y^3).                               (3.1)
```

Hence the complete projective total-space singular locus is the single point

```text
t=0,               [x:y:z]=[0:0:1].                    (3.2)
```

The primitive hypersurface is integral because its generic plane cubic is
smooth and hence geometrically integral.  A hypersurface is `S_2`; (3.2)
shows regularity in codimension one.  Serre's criterion proves that the total
surface is normal.

## 4. Corrected exact replay

```bash
python3 - <<'PY'
import sympy as s

t,x,y,z,X=s.symbols('t x y z X')
Phi=s.expand((x+t*z)**3+t*y**3+t**3*x**2*y)
assert max(s.degree(c,t) for _,c in s.Poly(Phi,x,y,z).terms()) <= 3
assert s.expand(Phi.subs({x:-t,y:0,z:1})) == 0

Phip=s.expand(Phi.subs(x,X-t*z))
Phi1=s.expand(Phip.subs({X:t*X,y:t*y},simultaneous=True)/t**3)
Phi0=s.expand(Phi1.subs({X:t*X,y:t*y},simultaneous=True)/t**3)
assert Phip == s.expand(X**3+t*y**3+t**3*(X-t*z)**2*y)
assert Phi1 == s.expand(X**3+t*y**3+t**3*(X-z)**2*y)
assert Phi0 == s.expand(X**3+t*y**3+t*(t*X-z)**2*y)

partials=[s.expand(s.diff(Phi,v).subs(t,0)) for v in (x,y,z,t)]
assert partials == [3*x**2,0,0,3*x**2*z+y**3]

# Correct binary quartic -t*X^3*Z-t^2*Z^4.
a,b,c,d,e=0,-t,0,0,-t**2
I=s.expand(12*a*e-3*b*d+c**2)
J=s.expand(72*a*c*e+9*b*c*d-27*a*d**2-27*b**2*e-2*c**3)
assert I == 0 and s.expand(J-27*t**4) == 0

slope=s.symbols('s')
quad_disc=s.expand((-2*t**2*slope)**2
    -4*(1+t*slope**3+t**3*slope)*(t*slope))
assert s.factor(quad_disc) == -4*t*slope*(t*slope**3+1)
print('D3_LOCAL_DEGREECAP_COUNTERCONTROL_R1_PASS')
PY
```

Expected output:

```text
D3_LOCAL_DEGREECAP_COUNTERCONTROL_R1_PASS
```

## 5. Scope and global successor

The counter-control is local.  It does not supply a rational global surface,
a dominant `A^2` map, a proper-block occurrence, a compatible discrepancy
row, a polynomial map, or JC2.

Its natural class-`(3,3)` homogenization is

```text
S^3x^3+S^2T(3x^2z+y^3)+ST^2(3xz^2)+T^3(z^3+x^2y).     (5.1)
```

Global integrality, normality at every point (especially `S=0`), finite
flatness of the target projection, ramification, rationality, and resolved
boundary topology are **OPEN in this report** and require a separate audit.
The local good-resolution graph of (3.2) is also not computed here.

## 6. Corrected maximum-safe theorem

Equation (0.1) is a primitive raw-`t`-degree-three, normal, soluble, generically
smooth ternary cubic of exact CFS level two.  Two admissible pairs `(1,1)`
lower it to the minimal `IV*` model (2.5).  Therefore the proposed local
degree-cap impossibility is false, even after the full CFS admissible-pair menu
and additive minimal fibres are included.

Only this R1 report may be consumed; every conflicting fibre label or
valuation in the superseded report is retracted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7793`.
- Body SHA-256:
  `4e0c58a36bf8645603dc86d9d5b1ce042415139400ef8738022aeae33764ac62`.
- Frozen basis: `6d26a4b1e18c2f64862edd5e0a1ce8f0f0a36104`.
