# D3 sectioned two-support split control: elliptic exceptional curves and genus-three ramification

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, independent audit lane  
Frozen basis: `f86884a5ab78e5248977942f93547fbf25b5be8e`  
Lifecycle: **EXACT GLOBAL CONTROL / CONDITIONAL PROPER-BLOCK EXCLUSION / REVIEW REQUIRED**

## 0. Verdict

The collision control in the sectioned one-support row splits exactly.  Put

```text
H_0=X^3+t*y^3+t*(t*X-z)^2*y.                          (0.1)
```

For a linear parameter `u`, define the reverse `(1,1)` move

```text
R_u(H)=u^3*H(t;X/u,y/u,z).                             (0.2)
```

Then

```text
R_(t-b) R_(t-a) H_0
 =X^3+t*y^3+t*(t*X-(t-a)*(t-b)*z)^2*y.                (0.3)
```

After the integral shear `X=x+(t-a-b)z`, this is the raw-degree-three family

```text
F_(a,b)=(x+(t-a-b)z)^3+t*y^3+t*(t*x-a*b*z)^2*y.       (0.4)
```

The member `(a,b)=(1,-1)` is

```text
F=(x+t*z)^3+t*y^3+t*(t*x+z)^2*y.                      (0.5)
```

Its class-`(3,3)` closure is integral, normal and rational, and target
projection is finite flat of degree three.  It has exact CFS/Hodge level one
at each of `t=1,-1`, no other GR defect, and realizes the remaining sectioned
row

```text
m=1,       T=[1]+[-1],       D=-F_1-F_(-1),       rho(Y)>=12. (0.6)
```

This is a genuine global **surface** positive control.  It cannot be the
globally identified second leg of an actual proper block for two independent
reasons:

1. each defect singularity is resolved by one blowup whose exceptional curve
   is a smooth plane cubic;
2. the residual complete ramification component of the finite target
   projection has normalization genus three.

Either curve would be boundary for the actual everywhere-defined morphic
first leg and contradict the binding rational-forest theorem.  The exclusion
is not licensed by a merely local algebra match or abstract rationality.

## 1. Exact reverse chronology and Hodge levels

The identity (0.3) follows term by term from (0.1)--(0.2).  A second reverse
move replaces the first factor multiplying `z` by its product with the new
one.  The shear in (0.4) uses

```text
t*(x+(t-a-b)z)-(t-a)*(t-b)z=t*x-a*b*z.                (1.1)
```

Every displayed term in (0.4) has literal `t`-degree at most three.  The
section is

```text
[S:T] |-> [x:y:z]=[(a+b)S-T:0:S],                     (1.2)
```

and for (0.5) it is `[-T:0:S]`.

Locally at `t=a`, the factor `t-b` is a unit when `a!=b`; its reverse move is
an integral unit-coordinate equivalence.  Removing it leaves exactly
`R_(t-a)H_0`.  If also `a!=0`, the fibre of `H_0` at `a` is smooth because
the minimal Weierstrass curve is

```text
V^2=U^3-t^4,                                          (1.3)
```

whose discriminant is nonzero at `a`.  Thus the local CFS level is exactly
one.  The same argument applies at `b`.  At `(a,b)=(1,-1)`, the plane
invariants are, up to nonzero constants,

```text
c4=0,
c6=t^4*(t^2-1)^6,
Delta=t^8*(t^2-1)^12.                                 (1.4)
```

The orders at `t=+1,-1` are `(infinity,6,12)`, exactly one level above good
reduction.  At `t=0` the minimal fibre is `IV*`, with orders
`(infinity,4,8)`.  Homogenizing (1.4) to degrees `18,36` leaves orders
`(infinity,2,4)` at infinity, the minimal `IV` fibre.  Hence there are no
other singular coefficient-base fibres.  The minimal elliptic surface has
fibres `IV*+IV`, discriminant degree twelve and a section, so it is rational.
The resolution of the plane model is birational to it and is rational.

The only non-Du-Val points are the two exact level-one points.  Applying the
binding D3 Hodge-divisor theorem therefore gives (0.6), including the Picard
bound.

## 2. Finite flat target projection and normality

The homogeneous closure of (0.5), viewed as a binary cubic in `[S:T]`, has
target coefficients

```text
A_0=x^3,
A_1=3*x^2*z+y^3+y*z^2,
A_2=3*x*z^2+2*x*y*z,
A_3=z^3+x^2*y.                                        (2.1)
```

They have no common projective zero.  Indeed `A_0=0` gives `x=0`, then
`A_3=0` gives `z=0`, and finally `A_1=0` gives `y=0`.  Thus projection

```text
pi:X -> P2_[x:y:z]                                    (2.2)
```

is projective with length-three fibres and hence finite.  The hypersurface is
Cohen--Macaulay and `P2` is regular of the same dimension, so finite miracle
flatness makes `pi` locally free of rank three.

The invariant ledger (1.4) reduces the singular-locus audit to the four base
values `0,+1,-1,infinity`.  The complete singular set is

```text
t=+1:       p_+=[-1:0:1],
t=-1:       p_-=[ 1:0:1],
t=0:        [0:0:1], [0:i:1], [0:-i:1],
t=infinity: [0:1:0].                                  (2.3)
```

Sections 3--4 verify that these points are isolated.  Every other plane fibre
is smooth, so there can be no further total-space singularity.  The generic
fibre is smooth and geometrically integral.  The primitive hypersurface is
therefore integral; it is `S_2`, and the isolated singular set gives `R_1`.
Serre's criterion proves normality.

## 3. The two defect points expose elliptic exceptional curves

Work first at `t=a`, put `tau=t-a`, and remove the other unit reverse move.
In affine `z=1`, the local equation is `R_tau(H_0)`.  Its degree-three tangent
cone is exactly

```text
C_a: X^3+a*y^3+a*(a*X-tau)^2*y=0
     in P2_[X:y:tau].                                  (3.1)
```

This is the plane fibre `H_0(a;X,y,tau)`, hence is smooth whenever `a!=0` by
(1.3).  In particular both `C_1` and `C_(-1)` are smooth plane cubics.  The
ordinary blowup of the vertex has exceptional divisor `C_a`; quasismoothness
of the projectivized tangent cone makes the strict transform smooth along it,
so this one blowup resolves the point.  Each exceptional divisor has genus
one.

For a hypothetical actual block with (2.2) as its global second leg, the
first-leg image lies in `X_sm`.  A resolution that is an isomorphism over that
image therefore places both complete elliptic exceptional curves in the
first-leg boundary.  The corrected morphic rational-forest theorem forbids
even one positive-genus boundary component.

## 4. The other four singularities are `A_2`

At `t=0`, equation (0.5) has fibre `x^3=0`, and on `x=0` the base derivative
is

```text
F_t=y^3+y*z^2=y*(y^2+z^2).                            (4.1)
```

The three roots in (2.3) are simple on the projective line.  If `eta` is a
local coordinate along that line at any root, the local equation has
quadratic part a nonzero multiple of `t*eta` and transverse cubic term `x^3`.
The splitting lemma gives `uv+x^3`, an `A_2` rational double point.

On the chart `T=1`, put `s=S/T`.  The equation is

```text
(s*x+z)^3+s^2*y^3+(x+s*z)^2*y.                        (4.2)
```

At the unique point `[0:1:0]`, set `y=1` and `w=z+sx`.  Then

```text
F=w^3+s^2+((1-s^2)x+s*w)^2,                           (4.3)
```

whose quadratic part is `s^2+x^2`.  Again the splitting lemma gives an
`A_2` point.  These four points have zero GR defect and rational-chain
exceptional fibres.

## 5. A residual ramification component of genus three

The section (1.2) maps isomorphically to the target line `y=0`.  On that line
the binary cubic is `(Sx+Tz)^3`, so it is totally ramified and occurs with
different coefficient two.  The target discriminant has the exact form

```text
Disc_[S:T](F)=-y^2*B_10,                              (5.1)
```

with a residual degree-ten form `B_10`.

On the dense chart `S=x=1`, put

```text
u=1+t*z,                 q=u/y.                        (5.2)
```

After removing the section component, the equations `F=F_t=0` eliminate `y`
to

```text
P(q,t)=9*q^7*t+12*q^6*t^2+q^6+4*q^5*t^3+9*q^4*t^2
       +8*q^3*t^3+4*q^2*t^4+4*t^6=0.                 (5.3)
```

The penultimate subresultant is linear in `y` on a dense open, so (5.3) is
birational to the residual source ramification curve.  Exact absolute
factorization over characteristic zero finds one factor.

The Newton polygon of (5.3) has vertices

```text
(0,6),(6,0),(7,1),(5,3),                              (5.4)
```

area eight, ten boundary lattice intervals, and four interior lattice
points.  The curve has no torus singularity.  Three edge truncations are
nondegenerate.  The remaining edge is

```text
q^5*t*(3*q+2*t)^2.                                    (5.5)
```

and contributes one ordinary node.  Indeed in the toric chart
`q=1/r,t=w/r`, multiply by `r^8` and put `v=w+3/2`; the quadratic term is

```text
-6*v^2+(961/16)*r^2,                                  (5.6)
```

two distinct lines.  There are no other boundary singularities.  Hence the
complete residual component `R'` is irreducible and

```text
g(R'^nu)=4-1=3.                                       (5.7)
```

If (2.2) were globally the second leg of an actual block, points of `R'` over
the affine target would be missed as ramification and points over target
infinity would already be omitted.  Thus its complete genus-three strict
transform would be a boundary component, independently reproducing the
contradiction in Section 3.

## 6. Exact desk replay

```bash
python3 - <<'PY'
import math
import sympy as s

t,x,y,z,X,a,b,q,r,w,v=s.symbols('t x y z X a b q r w v')
H0=X**3+t*y**3+t*(t*X-z)**2*y

def reverse(H,u):
    return s.expand(u**3*H.subs({X:X/u,y:y/u},simultaneous=True))

Rab=s.factor(reverse(reverse(H0,t-a),t-b))
want=X**3+t*y**3+t*(t*X-(t-a)*(t-b)*z)**2*y
assert s.expand(Rab-want) == 0
Fab=s.expand(want.subs(X,x+(t-a-b)*z))
assert s.expand(Fab-((x+(t-a-b)*z)**3+t*y**3
                     +t*(t*x-a*b*z)**2*y)) == 0
F=s.expand(Fab.subs({a:1,b:-1}))
assert max(s.degree(c,t) for _,c in s.Poly(F,x,y,z).terms()) <= 3

coeff=[s.Poly(F,t).coeff_monomial(t**i) for i in range(4)]
assert coeff == [x**3,3*x**2*z+y**3+y*z**2,
                 3*x*z**2+2*x*y*z,z**3+x**2*y]
closed=[s.factor(s.diff(F,u0).subs(t,0)) for u0 in (x,y,z,t)]
assert closed == [3*x**2,0,0,3*x**2*z+y**3+y*z**2]
for point in ({t:1,x:-1,y:0,z:1},{t:-1,x:1,y:0,z:1}):
    assert all(s.diff(F,u0).subs(point) == 0 for u0 in (x,y,z,t))

# Dense residual ramification elimination.
u=s.symbols('u')
Fd=s.factor(F.subs({x:1,z:(u-1)/t}))
Rtd=s.factor((t*s.diff(F,t)).subs({x:1,z:(u-1)/t}))
A=s.factor((Fd.subs(u,q*y)*t/y))
B=s.factor((Rtd.subs(u,q*y)*t/y))
res=s.factor(s.resultant(A,B,y))
P=(9*q**7*t+12*q**6*t**2+q**6+4*q**5*t**3+9*q**4*t**2
   +8*q**3*t**3+4*q**2*t**4+4*t**6)
assert res == t**2*(t-1)**2*(t+1)**2*P

vertices=[(0,6),(6,0),(7,1),(5,3)]
area2=abs(sum(vertices[i][0]*vertices[(i+1)%4][1]
              -vertices[i][1]*vertices[(i+1)%4][0] for i in range(4)))
boundary=sum(math.gcd(abs(vertices[i][0]-vertices[(i+1)%4][0]),
                      abs(vertices[i][1]-vertices[(i+1)%4][1]))
             for i in range(4))
assert (area2,boundary,(area2-boundary+2)//2) == (16,10,4)

aux=s.symbols('aux')
def torus_smooth(poly):
    gb=s.groebner([poly,s.diff(poly,q),s.diff(poly,t),aux*q*t-1],
                  aux,q,t,order='lex')
    return len(gb.polys)==1 and gb.polys[0].as_expr()==1
assert torus_smooth(P)
edges=[q**6+9*q**4*t**2+8*q**3*t**3+4*q**2*t**4+4*t**6,
       q**6*(9*q*t+1),4*t**3*(q**5+t**3)]
assert all(torus_smooth(edge) for edge in edges)
Q=s.expand(r**8*P.subs({q:1/r,t:w/r}))
L=s.expand(Q.subs(w,v-s.Rational(3,2)))
quadratic=sum(c*r**i*v**j for (i,j),c in s.Poly(L,r,v).terms()
              if i+j==2)
assert s.expand(quadratic-(31*r-4*s.sqrt(6)*v)
                *(31*r+4*s.sqrt(6)*v)/16) == 0
print('D3_SECTIONED_TWO_SUPPORT_SPLIT_CONTROL_PASS')
PY
```

Expected output:

```text
D3_SECTIONED_TWO_SUPPORT_SPLIT_CONTROL_PASS
```

Absolute irreducibility of (5.3) is independently checked by:

```bash
Singular -q <<'EOF'
LIB "absfact.lib";
ring r=0,(q,t),dp;
poly P=9q7t+12q6t2+q6+4q5t3+9q4t2+8q3t3+4q2t4+4t6;
list L=absFactorize(P);
size(L);
EOF
```

The expected factor count is `1`.  The report layer uses finite miracle
flatness, `S_2+R_1`, ordinary blowup of a smooth projectivized tangent cone,
the toric genus formula, and the two named binding campaign theorems.

## 7. Maximum-safe conclusion

Splitting the two reverse moves produces an exact raw-degree-three normal
rational global surface in the sectioned two-support D3 row.  It is a sharp
positive control for abstract surface occurrence and simultaneously an exact
negative control for actual morphic proper-block occurrence: both local
elliptic exceptional curves and a global genus-three ramification component
violate the required rational boundary forest.  No conclusion is drawn from
local algebra alone, and no polynomial map or JC2 counterexample is built.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12539`.
- Body SHA-256:
  `6975f482e1f2eeb6d5277623951dd3c82a3a9bc3258ee00ac636169a65e01c6b`.
- Frozen basis: `f86884a5ab78e5248977942f93547fbf25b5be8e`.
