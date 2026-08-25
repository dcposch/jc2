# Max12 `(9,12)` order-three Q8 branch: norm, Taylor, and terminal jet

Date: 2026-08-24  
Status: **producer-exact; hostile different-model review required**

## 1. Scope and coefficient field

This is a successor to the now-reviewed corrected-Q8 formal-branch theorem.
It uses no quarantined Q12 artifact. It computes the lowest local
normalization jet, types it in the reviewed root-free critical-value norm,
reconstructs both original Taylor families at their true center, and only
then pulls back the terminal differential row. It does not give a global
component model or exclude the punctured component.

Write

```text
Q8(v)=-999v^8-1539v^7+1782v^6+6498v^5+7320v^4
      +4428v^3+1548v^2+296v+24.
```

Modulo `7`, after making it monic, this is

```text
v^8+4v^7+2v^6+v^5+6v^4+2v^3+4v^2+v+5.
```

The replay checks the Rabin certificate

```text
x^(7^8)-x = 0 mod Q8,
gcd(Q8,x^(7^4)-x)=1.
```

Thus `Q8` is irreducible over `Q`, and computations below take place in the
field `E=Q[v]/(Q8)`. Every displayed nonzero residue is consequently a unit
at all eight conjugate contacts.

## 2. Lowest formal parameterization

Normalize `p=1` and choose the involution-odd, Kummer-fixed parameter

```text
t=a0.
```

Exact Gaussian elimination over `E`, followed by substitution into all seven
rows, gives

```text
a0=t,
a2=c2*t+d2*t^3+O(t^5),
a4=c4*t+d4*t^3+O(t^5),
a6=c6*t+d6*t^3+O(t^5),

p =1+P2*t^2+O(t^4),
x1=x1,0+X1,2*t^2+O(t^4),
x3=x3,0+X3,2*t^2+O(t^4),
x5=x5,0+X5,2*t^2+O(t^4).                    (2.1)
```

Every coefficient displayed in (2.1) is a unit of `E`. For the invariant
quotient and terminal tail,

```text
v(t)=v0+V2*t^2+O(t^4),       V2 in E^*,
r8(t)=rho0+C*t^2+O(t^4),     C in E^*.                (2.2)
```

The replay records canonical SHA-256 digests for all twelve residues and
reconstructs the original eight Faber tails from the pinned compiler. This
is coefficient-fibre geometry, not yet a differential trajectory.

## 3. Exact critical-value norm leaf

Let `nu=r6`, which the seven equations keep differential-constant. Before
the harmless constant scaling `nu -> 1`, the reviewed Wronskian quadratic is

```text
B/(54*nu)=z^2-s,
s=-p/3-10*r8/(9*nu).                                  (3.1)
```

Reduce `F=f^4` and `G=g^3` modulo `z^2-s`, and use the reviewed root-free
invariants

```text
E=G0*F1-G1*F0,
Norm(W)=Norm(G-F),
Norm(F)=F0^2-s*F1^2.
```

Direct substitution of (2.1) gives

```text
s=s0+s2*t^2+O(t^4),                    s0 in E^*,
Norm(F)=nF0+nF2*t^2+O(t^4),            nF0 in E^*,
Norm(W)=nW0+nW2*t^2+O(t^4),            nW0 in E^*,
E=e1*t+e3*t^3+O(t^5),                  e1 in E^*.       (3.2)
```

The exact certificate is

```text
gcd(num(e1),Q8)=1,
sha256(e1)=c289f3c14b0c9402cf78db10e71a4f4ce0e0c42d5f231e1e7e0c7f39726f248d,
sha256(e1^(-1) mod Q8)=cbb8465b21317aa250a55c1f9e55673a080893fae7bd0d0984268d3f1c79b9e6.
```

Consequently the parity contact itself lies in reviewed leaf 3,

```text
s*Norm(F)*Norm(W)!=0,   E=0
```

(two unabsorbed equal non-`1` critical values), but the punctured corrected
Q8 formal branch lies immediately in reviewed leaf 4,

```text
s*Norm(F)*Norm(W)*E!=0
```

(two unabsorbed unequal critical values). This is a formal-local leaf
classification; it neither algebraizes nor rationalizes the branch.

## 4. True Taylor boundary reconstruction

The original boundary is not the spectral center `z=0`. The reviewed
depression is

```text
z=u*y+r,            r=A/9,            r/u in C(x),     u^3=h.  (4.1)
```

Therefore both complete original Taylor families are

```text
[y^ell]P = u^ell/ell! * f^(ell)(r),     0<=ell<=9,
[y^ell]Q = u^ell/ell! * g^(ell)(r),     0<=ell<=12.     (4.2)
```

The replay reconstructs all `10+13` members of (4.2) in
`E[r][[t]]/(t^4)` and hashes every exact coefficient. Along an actual
trajectory every member remains charged to lie in `C[x]`; in particular

```text
P(x,0)=f(r),            Q(x,0)=g(r).                   (4.3)
```

Negative control for the old `z=0` temptation is machine-checkable:

```text
[r^9](f(r)-f(0))=1,     [r^12](g(r)-g(0))=1.          (4.4)
```

Thus `f(0)` and `g(0)` are not the original boundary values unless the
separate condition `r=0` is proved. No such condition is assumed here.
The full polynomiality constraints in (4.2) do not produce a local
contradiction by themselves because the global functions `u(x),r(x),t(x)`
have not yet been reconstructed.

As a spectral-center control only, at `t=0` the replay also proves

```text
f(0)=0,        f_z(0) in E^*,       g(0) in E^*,
gcd(f,f_z)=1,  gcd(f,g)=1.                              (4.5)
```

So the parity contact is squarefree and coprime, but (4.5) is not substituted
for either Taylor family.

## 5. Terminal row and its first local consequence

The original terminal row is retained exactly:

```text
9*r8'=j/u,              j in C^*,             u^3=h.   (5.1)
```

The geometric weights are

```text
wt(p)=2, wt(a0)=9, wt(r8)=20, wt(v)=0.
```

Restoring a general loaded contact from `p=1` uses a constant `p0`: indeed
`v0` is algebraic constant, `nu` is differential-constant, and
`p0^9*R6(v0)=nu`. Equation (2.2) becomes

```text
r8=p0^10*R8(v0)+p0*C(v0)*a0^2+O(a0^4).               (5.2)
```

Only after the Taylor reconstruction (4.2) and terminal provenance (5.1)
do we draw the following trajectory-local consequence. Differentiating
(5.2) in (5.1) gives

```text
18*p0*C(v0)*a0*a0' + O(a0^3*a0') = j/u.              (5.3)
```

At a finite `x`-place where an actual trajectory meets the Q8 node, let
`e=ord(a0)>0` and `m=ord(h)>=0`. Since `a0` is Kummer-fixed, `e` is an
integer, and the two sides of (5.3) have orders

```text
2e-1 >= 1,                 -m/3 <= 0.
```

They cannot agree. Hence an actual trajectory on this formal component
cannot meet its parity node above a finite `x`-place.

At infinity, if `a0` vanishes to order `e>0`, (5.3) gives only the necessary
condition

```text
deg(h)=3*(2e+1).                                          (5.4)
```

This is not an infinity exclusion.

## 6. Exact conclusion and open successor

The corrected Q8 branch is transverse not only to parity but also to the
equal-critical-value divisor: its leading `E` coefficient is a unit. Its
`r8` pullback has a unit quadratic coefficient, both complete Taylor
families remain charged at `r=A/9`, and terminal valuation forbids finite
contact with the node.

The punctured leaf-4 branch is not excluded. The decisive successor is to
derive its descended unequal-critical-value coordinates (or a global
normalization/projective boundary), pull back (4.2) and (5.1), and then test
genus or finite-pole compatibility. There is no all-`(9,12)`,
maximum-twelve, counterexample, or Jacobian-conjecture conclusion.

## 7. Replay

```sh
shasum -a 256 -c cases/max12_912_order3_nu_q8_normalization_jet_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_q8_normalization_jet_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_normalization_jet_20260824/replay.json -
```

The replay uses only Python's standard library. It pins the reviewed Q8
formal theorem and critical-value norm, certifies irreducibility modulo `7`,
solves and substitutes the exact truncated series, proves the norm-leaf unit
certificates, reconstructs all Taylor members at a formal `r=A/9`, and
checks both polynomial gcds.
