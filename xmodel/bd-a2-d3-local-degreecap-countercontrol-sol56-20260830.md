# D3 raw-degree-three local counter-control: the soluble level-two no-go is false

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, independent audit lane  
Frozen basis: `6d26a4b1e18c2f64862edd5e0a1ce8f0f0a36104`  
Lifecycle: **EXACT PROVISIONAL COUNTER-CONTROL / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

The proposed universal local lemma is **false**.  Over `R=C[[t]]`, the
ternary cubic

```text
Phi(t;x,y,z)=(x+tz)^3+t y^3+t^3 x^2y                    (0.1)
```

has all of the conjectured hypotheses:

- literal raw coefficient degree at most three in `t`;
- integral normal total surface;
- smooth generic plane cubic;
- a `C((t))`-point, namely `[-t:0:1]`;
- exact CFS level two;
- two explicit successful CFS drops, each with admissible Smith pair `(1,1)`;
- minimal additive floor of Kodaira type `I_0^*`.

Thus no exhaustive treatment of the four nontrivial CFS pairs

```text
(0,1), (1,1), (1,2), (2,3)
```

can prove the proposed impossibility.  The witness already inhabits the legal
`(1,1),(1,1)` branch.  It also includes a nonconstant integral `GL_3(R)`
interlude, the shear `X=x+tz`, so a theorem restricted to aligned standard
Weierstrass controls would miss it.

This is a local counter-control, not yet a proper-block occurrence or a JC2
counterexample.  The global class-`(3,3)` homogenization and boundary audit are
separate successors.

## 1. Raw presentation, point, and degree cap

Expanding (0.1) gives

```text
Phi=x^3+3t x^2z+3t^2xz^2+t^3z^3+t y^3+t^3x^2y.         (1.1)
```

Every coefficient is a polynomial of `t`-degree at most three, and the
coefficient of `x^3` is a unit, so the model is primitive.  Direct substitution
gives

```text
Phi(-t,0,1)=0,                                          (1.2)
```

hence its generic cubic is `K=C((t))`-soluble.

The shear

```text
X=x+tz                                                   (1.3)
```

belongs to `GL_3(R)` and rewrites the model as

```text
Phi'=X^3+t y^3+t^3(X-tz)^2y.                            (1.4)
```

Although (1.4) contains terms of `t`-degree four and five after expansion,
this is only an integral coordinate gauge.  The charged raw presentation is
(1.1), where the degree cap is literal.

## 2. Two exact admissible `(1,1)` drops

Define

```text
Phi_1=t^(-3) Phi'(tX,ty,z)
     =X^3+t y^3+t^3(X-z)^2y,                            (2.1)

Phi_0=t^(-3) Phi_1(tX,ty,z)
     =X^3+t y^3+t(tX-z)^2y                              (2.2)
     =X^3+t y^3+t z^2y-2t^2Xzy+t^3X^2y.
```

Both right sides are primitive integral ternary cubics.  After reordering the
coordinates as `(z,X,y)`, each transformation is

```text
[mu,M]=[t^(-3),diag(1,t,t)].                            (2.3)
```

This is precisely the CFS admissible pair `(a,b)=(1,1)`: in CFS notation
`a+b+1=3`, and integrality of (2.1)--(2.2) is the admissibility condition

```text
F(x,t^a y,t^b z)=0 mod t^(a+b+1).
```

For ternary cubics the invariant character is `mu det(M)`.  In (2.3),

```text
v(mu det M)=-3+2=-1.                                   (2.4)
```

Consequently each arrow lowers `(v(c4),v(c6),v(Disc))` by `(4,6,12)` and
lowers the CFS level by exactly one once the terminal model is known to be
minimal.  These are direct successful admissible transformations, not merely
same-level singular-line moves.

The source for the admissible-pair menu and invariant character is
J. E. Cremona--T. A. Fisher--M. Stoll, *Minimisation and reduction of 2-,
3- and 4-coverings of elliptic curves*, Algebra & Number Theory 4 (2010),
Theorem 4.3 and Lemma 4.4.

## 3. The terminal model is minimal of type `I_0^*`

The point `[X:y:z]=[0:0:1]` lies on `Phi_0`.  Permute coordinates by

```text
(X_lemma,Y_lemma,Z_lemma)=(X,z,y),
```

so that the point becomes `(0:1:0)`.  Then (2.2) has the exact form

```text
f1(X,Z)Y^2-f2(X,Z)Y-f3(X,Z)=0                          (3.1)
```

with

```text
f1=tZ,
f2=2t^2XZ,
f3=-(X^3+Z^3+t^3X^2Z).                                 (3.2)
```

CFS Lemma 3.14 passes to the generalized binary quartic

```text
w^2+2t^2XZ w
  =-tX^3Z-tZ^4-t^4X^2Z^2.                              (3.3)
```

Completing the square with `W=w+t^2XZ` cancels the two `t^4X^2Z^2`
terms and gives

```text
W^2=-t Z(X^3+Z^3).                                     (3.4)
```

The binary quartic `Z(X^3+Z^3)` has four distinct roots over `C`, so its
discriminant is a unit.  Scaling a binary quartic by `t` scales its
discriminant by `t^6`; hence

```text
v(Disc(Phi_0))=6.                                      (3.5)
```

Equivalently, in the affine chart `Z=1`, put `U=-tX` and `V=tW`.  Equation
(3.4) becomes

```text
V^2=U^3-t^3.                                           (3.6)
```

It has `v(c4)=infinity`, `v(c6)=3`, and `v(Disc)=6`, and Tate's algorithm in
residue characteristic zero gives Kodaira type `I_0^*`.  The equation is
minimal because `v(c6)=3<6`; alternatively, a positive CFS level would make
the model discriminant at least twelve larger than a nonnegative minimal
elliptic discriminant, contradicting (3.5).  Thus `Phi_0` has CFS level zero.

Combining (2.4) with (3.5),

```text
v(Disc(Phi_1))=18,
v(Disc(Phi))=30,
level(Phi_1)=1,
level(Phi)=2.                                          (3.7)
```

The original model therefore has exact, not merely lower-bounded, CFS level
two.  Its invariant valuations are

```text
v(c4)=infinity,       v(c6)=15,       v(Disc)=30,       (3.8)
```

so it also satisfies the promoted exact-level upper gate
`v(c6)<18`.

## 4. Generic smoothness and exact total singular locus

Write `u=x+tz`.  Over `K`,

```text
Phi=u^3+t y^3+t^3x^2y.
```

If a projective generic-fibre point were singular, the `z`-derivative

```text
Phi_z=3t u^2
```

would force `u=0`.  The remaining two spatial derivatives become

```text
Phi_x=2t^3xy,
Phi_y=t(3y^2+t^2x^2).
```

If `x=0`, then `u=tz=0`, and projectivity forces `y!=0`, contradicting
`Phi_y=0`.  If `y=0`, then `Phi_y=t^3x^2` forces `x=0`, and then `z=0`, also
impossible.  Hence the generic plane cubic is smooth.  This also follows from
the nonzero discriminant in (3.7).

On the closed fibre `t=0`,

```text
Phi|_(t=0)=x^3,
Phi_x|_(t=0)=3x^2,
Phi_y|_(t=0)=Phi_z|_(t=0)=0,
Phi_t|_(t=0)=3x^2z+y^3.                                (4.1)
```

The total-space singular equations therefore force

```text
t=0,      x=0,      y=0,
```

leaving the unique projective point

```text
p=[0:0:1].                                              (4.2)
```

There are no singular points away from the closed fibre by generic
smoothness.  The generic cubic is geometrically integral; (1.1) is primitive,
so the total hypersurface is integral.  A hypersurface is Cohen--Macaulay and
hence `S_2`.  Its singular locus is the single codimension-two point (4.2), so
it is regular in codimension one.  Serre's criterion proves:

```text
the total surface {Phi=0} subset P^2_R is normal.        (4.3)
```

This is the exact normality assertion required by the proposed lemma; it is
not a check only at a selected affine chart.

## 5. Why the earlier control sweep missed the witness

The terminal Jacobian is the standard additive type `I_0^*`, but the terminal
ternary embedding (2.2) is not the standard Weierstrass plane presentation
used in the initial control sweep.  Its rational point sits at `(0:1:0)` only
after a coordinate permutation, and Lemma 3.14 exposes a binary-quartic model
whose square completion is essential.  Reversing two `(1,1)` drops and then
undoing the integral shear (1.3) compresses every raw coefficient back to
`t`-degree at most three while leaving the total singularity isolated.

This shows precisely why the following inference is invalid:

```text
standard minimal Weierstrass controls become nonnormal
  => every soluble minimal ternary embedding becomes nonnormal.
```

Arbitrary integral `GL_3(R)` gauges and the degree-three divisor defining the
ternary embedding are load-bearing.  An admissible-pair exhaustion must retain
the moduli of minimal ternary embeddings, not only the Kodaira symbol of their
Jacobians.

## 6. Exact desk-scale replay

The following command uses only exact polynomial arithmetic.  It checks the
raw degree cap, the rational point, the integral shear, both `(1,1)` drops,
the central Jacobian data, and the nonzero order-three binary-quartic
`J`-invariant that gives discriminant order six.

```bash
python3 - <<'PY'
import sympy as s

t,x,y,z,X=s.symbols('t x y z X')
Phi=s.expand((x+t*z)**3+t*y**3+t**3*x**2*y)

assert max(s.degree(c,t) for _,c in s.Poly(Phi,x,y,z).terms()) <= 3
assert s.expand(Phi.subs({x:-t,y:0,z:1})) == 0

Phip=s.expand(Phi.subs(x,X-t*z))
wantp=s.expand(X**3+t*y**3+t**3*(X-t*z)**2*y)
assert Phip == wantp

Phi1=s.expand(Phip.subs({X:t*X,y:t*y}, simultaneous=True)/t**3)
want1=s.expand(X**3+t*y**3+t**3*(X-z)**2*y)
assert Phi1 == want1

Phi0=s.expand(Phi1.subs({X:t*X,y:t*y}, simultaneous=True)/t**3)
want0=s.expand(X**3+t*y**3+t*(t*X-z)**2*y)
assert Phi0 == want0

partials=[s.diff(Phi,v).subs(t,0) for v in (x,y,z,t)]
assert [s.expand(q) for q in partials] == [3*x**2,0,0,3*x**2*z+y**3]

# Binary quartic -t*Z*(X^3+Z^3): (a,b,c,d,e)=(0,-t,0,0,-t).
a,b,c,d,e=0,-t,0,0,-t
I=s.expand(12*a*e-3*b*d+c**2)
J=s.expand(72*a*c*e+9*b*c*d-27*a*d**2-27*b**2*e-2*c**3)
assert I == 0 and s.expand(J-27*t**3) == 0

print('D3_LOCAL_DEGREECAP_COUNTERCONTROL_PASS')
PY
```

Expected output:

```text
D3_LOCAL_DEGREECAP_COUNTERCONTROL_PASS
```

The replay is corroborative, not a replacement for the generic-smoothness,
minimality, and Serre-normality arguments in Sections 3--4.

## 7. Scope and successors

The counter-control falsifies only the proposed universal **local**
degree-cap closure.  It does not by itself supply:

- a normal integral global class-`(3,3)` surface over `P^1`;
- a rational surface or a dominant morphism from `A^2`;
- a finite proper-block incidence, an etale first leg, or a polynomial map;
- compatibility with the promoted global discrepancy row `D=-2F_t`;
- a JC2 counterexample.

The natural global homogenization of (1.1) in coefficient-base coordinates
`[S:T]` is

```text
S^3x^3+S^2T(3x^2z+y^3)+ST^2(3xz^2)+T^3(z^3+x^2y).     (6.1)
```

It should be audited separately for flatness, integrality, every total-space
singularity, rationality, ramification, and resolved boundary topology.  No
global conclusion about (6.1) is imported into the local theorem above.

For the local model, the next useful computation is the good-resolution graph
of the isolated singularity (4.2), including component genera and graph cycles.
Even if it is a rational tree, an actual proper-block occurrence still requires
the full morphic first-leg image before the rational-forest theorem can be
applied.

## 8. Maximum-safe theorem

There exists a primitive ternary cubic over `C[[t]]` of literal raw
coefficient degree at most three whose total surface is normal, whose generic
cubic is smooth and `C((t))`-soluble, and whose CFS level is exactly two.
Equation (0.1) is such a model.  It admits two successive admissible Smith
pairs `(1,1)`, and its minimal floor has Kodaira type `I_0^*`.

Therefore raw coefficient-base degree three, normality, generic smoothness,
solubility, exact level two, the complete four-pair CFS menu, and additive
minimal reduction do **not** jointly imply a local contradiction.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11252`.
- Body SHA-256:
  `62deff1fbf4df594feb0bbf7a5bca192210e28272dc7f62a858697e13138d7de`.
- Frozen basis: `6d26a4b1e18c2f64862edd5e0a1ce8f0f0a36104`.
