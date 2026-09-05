# K16 intrinsic quotient: exact emptiness through t=5 and the uniform residual

Lane: `k16-xempty-astra-20260905`. Astra, primary. 2026-09-05.

**VERDICT: PROVED for t=2,3,4,5, on every field factor; the all-t
emptiness assertion remains OPEN. Both literal charts at t=3,4,5 are
unit in characteristic zero. No whole-ray theorem (T) is promoted.**

The requested all-t conclusion has not been obtained. The reduction
`U ≅ G_m × X` survives the audit, including its nilpotent and collision
strata. The finite work reconstructs the literal main and complementary
charts at t=3,4,5. The characteristic-zero certificate route and its
independent checks are given below. No per-t unit is identified with an
all-t theorem, and no inhomogeneous inverse chart is declared proper.

The t=2 control in the request needs correction. On d=-1, y=1/5, it is
the full positive cone that is nonempty and has a free b-axis. Both B
and eta vanish on that family. Therefore U and X are empty there. This
is exactly how the weak target (8.1) can hold while V0 fails. Requiring
this X to be nonempty contradicts the named equations, the frozen
certificate, and the quotient lemma simultaneously. The exceptional
family is preserved explicitly in Section 5.

## 1. Custody, coefficient fields, and precise reconstruction

The ten inputs were checked before mathematical work. An awk manifest
paired `charged_input_<i>_sha256` with `_basename` in the receipt
`xmodel/k16-xempty-astra-20260905.run.v2`, and `sha256sum -c` returned
ten OK results. The first manifest loop used zero-based indices; its
malformed empty entry was corrected to the receipt's actual indices
1 through 10. There was no content mismatch. The successful manifest
and transcript are `input-manifest.sha256` and `input-verification.log`
under `box/k16xempty-20260905/`. No hash digit was retyped.

All mathematical charged inputs were read from the frozen directory
`/tmp/jc2-lane.Fz7unY/inputs`. The report's internal references to their
basenames mean those verified bytes, not later mutable originals.
The receipt's frozen basis is
`5a378d76e1b5c1b0728412715eeb45d7b0370176`. No ledger, jc2-lean source,
or uncharged ideation report was edited or used. The charged historical
collision scanner was inspected but not run against an unrelated corpus.
New drivers and arithmetic artifacts are confined to the requested box.

Fix t>=2. Put

```
q=2t+1,  3d^2=t+1,  y=(d+t+1)/(2q),
alpha=3/(4y^2),
omega=1/(4y^2(2d+1)),
g=(3t+1)t(3d+2t+2)/(6q^3).
```

Work over one field factor k of `Q[d]/(3d^2-t-1)`, and use its algebraic
closure when discussing geometric points. The algebra splits exactly
at `t=3m^2-1`, d=+m,-m. In the requested finite range, t=3,4,5 are
irreducible quadratic fields, with equations `3d^2=4,5,6`. One exact
calculation over each field covers both embeddings. The t=2 controls
are separate calculations over Q at d=+1 and d=-1. No nonzero element
of a product algebra is silently treated as a unit.

The normalizer scalars are units on every permitted factor; for example

```
N(y)=(t+1)(3t+2)/(12q^2),
N(g)=t^2(t+1)(3t+1)^2(4t+1)/(36q^6).
```

Let x be the translated polynomial variable. Define

```
C=x^(t-1)+c1*x^(t-2)+...+c_(t-1),
W=omega*x^q+w_(q-1)*x^(q-1)+...+w1*x-B,
eta=w1,  r=b^2/4,
K=x^2*C-y*b,  A_Abel=alpha*x^3*C^2,  D_Abel=3b*x*C/(2y).
```

The actual polynomial F is the left side minus the right side of

```
2(xW-r)W' = W^2+(B-2A_Abel+D_Abel)W
             +A_Abel(A_Abel-D_Abel)/3-B(A_Abel-D_Abel)
             -b*eta*K/(2y)-B*eta*x
             +(2r*A_Abel-4r(B+W))/x.                 (1)
```

The final quotient is polynomial because x divides A_Abel and B+W.
It is not a localization at a polynomial root. The name A used for
the slice numerator below is different from A_Abel.

The frozen Theorem H is applied literally. Starting with the leading
coefficient fixed, solve `[x^(q+k)]F=0` successively for w_k,
k=q-1,...,1. The diagonal is

```
lambda_k=2*omega*(k+2t+3+6d).
```

It is a scalar unit: `(k+2t+3)^2-12(t+1)>0` at every indicated index.
Then the x^q row solves B with diagonal `-2alpha*d`, also a unit.
The x^0 and x^1 rows vanish identically. The exact remaining equations
are `E_k=[x^k]F`, k=2,...,2t. This defines

```
S=k[c1,...,c_(t-1),b],  J=(E2,...,E_(2t)).
```

These constructions use scalar-unit divisions only and so preserve
arbitrary coefficient algebras, including nilpotents. Fresh finite rows
were emitted using the frozen `controls_emit_direct.py --raw-only`.
Every high pivot, leading equation, automatic low row, and eliminated
high row was checked before the charts were built. The saved raw files
are the full coefficient data, not a list of leading terms.

The weights are

```
wt(c_j)=j, wt(b)=t+1, wt(B)=2t+1, wt(eta)=2t,
wt(E_k)=4t+2-k, wt(T)=4t+1, where T=B*eta.
```

In particular B and eta are affine in b. The coefficient coordinates
are the actual translated C coordinates. Their map from the banked
spine variables is triangular with scalar units; translated c1 is a
nonzero scalar multiple of b4. No c1, b, discriminant, or root
difference is inverted in the reconstruction. The b4=0 and repeated-C-root
strata therefore remain in the input scheme.

## 2. Exact quotient and the literal two pieces

Define polynomial presentations with inverse variables

```
U=Spec S[z]/(J,1-z*B*eta),
X=Spec S[s]/(J,B-eta,1-s*B).
```

On U, let `v=B/eta`, a unit. The normalization map is

```
a_j=c_j*v^(-j),  b_X=b*v^(-t-1),  s_X=v^q/B.
```

Homogeneity gives all E rows at (a,b_X), and
`B(a,b_X)=eta(a,b_X)=B*v^(-q)`. Conversely, from `(v,a,b_X,s_X)` put

```
c_j=v^j*a_j,  b=v^(t+1)*b_X,
z=v^(-(2q-1))*s_X^2.
```

The two compositions are identities. They are maps of the displayed
polynomial quotient rings: `v=B^2*z` and `v^(-1)=eta^2*z` on U,
so the apparent ratios introduce no extra hypothesis. This proves
`U ≅ G_m × X` on arbitrary k-algebras. No root extraction or reducedness
assumption occurs. It follows that

```
X=empty  <=>  U=empty  <=>  B*eta belongs to radical(J). (2)
```

Write the reconstructed affine expressions as

```
B=M+b*N, eta=rho+b*sigma,
Delta=N-sigma, A=rho-M, H=N*rho-M*sigma.
```

The slice equation is exactly `b*Delta=A`, and the checked identities are

```
Delta*B-H=N*(b*Delta-A),
Delta*eta-H=sigma*(b*Delta-A),
M*Delta+N*A=rho*Delta+sigma*A=H.                     (3)
```

For each row set `d_k=deg_b(E_k)`; a zero row has d_k=0. Define the
polynomial coefficient-clearing operator

```
clear(f,e)=sum_(j=0)^e [b^j]f * A^j * Delta^(e-j),
F_k=clear(E_k,d_k).
```

Thus no rational substitution is used to define F_k at Delta=0.
The two literal pieces requested in the task are

```
X_main=Spec k[c1,...,c_(t-1),u]
       /(F2,...,F_(2t),1-u*Delta*H),

X_boundary=Spec k[c1,...,c_(t-1),b,s]
       /(E2,...,E_(2t),Delta,A,1-s*(M+b*N)).          (4)
```

The first identifies with D(Delta) in X. An entirely polynomial map
from its presentation is `b=u*A*H`, `s=u*Delta^2`; equations (3) then
give `B=eta=u*H^2`. The second is the closed quotient at Delta=0.
It retains A=0 as a required equation, including the N=sigma=0 locus.

The open and closed pieces suffice to test emptiness even for a
nonreduced X. If its coordinate ring R has `R_Delta=0`, some power of
Delta is zero; if also `R/(Delta)=0`, Delta is a unit. Both conditions
force R=0. Thus the complement was neither discarded nor recovered by
a dense-open argument.

The exact field-sensitive size inventory is:

| t | d_2,...,d_(2t) | terms B / eta | terms Delta / A / H | terms F2,...,F_(2t) |
|---:|---|---:|---:|---|
| 3 | 3,2,2,2,2 | 6 / 6 | 4 / 8 / 5 | 40,24,24,21,21 |
| 4 | 3,3,2,2,2,2,2 | 16 / 13 | 7 / 22 / 19 | 290,271,144,132,121,110,100 |
| 5 | 3,3,3,2,2,2,2,2,2 | 33 / 28 | 11 / 50 / 53 | 1508,1366,1303,581,542,480,434,377,354 |

All entries come from exact coefficients in the declared fields.
`emit_charts.py` checks (3), b affinity, each actual b exponent, and
independence of the cleared rows from b. Its first draft incorrectly
used Singular's weighted `deg` for the b exponent in a weighted ring;
the accepted version uses the b component of `leadexp`. The rejected
draft's assertion caught this error before any result was consumed.
The separate transport checker reconstructs the F rows and compares
them with the saved main presentation under an explicit ring map.

## 3. Finite characteristic-zero certificates and their promotion scope

| t / factor | source certificate | X_main | X_boundary |
|---|---|---|---|
| 2, d=-1 | exact Q identity for T | UNIT | UNIT |
| 2, d=+1 | exact Q identity for T | UNIT | UNIT |
| 3, 3d^2=4 | exact source cofactors for T^2, expanded main replay | UNIT | UNIT |
| 4, 3d^2=5 | exact rational block solve and independent polynomial replay | UNIT | UNIT |
| 5, 3d^2=6 | exact full-rank minor, independent model/determinant replay, adjugate circuit | UNIT | UNIT |


The freshly computed full-cone bases at t=3,4 have dimensions zero
and lengths 66,338, agreeing with the banked proofs. They show
`T not in J` but `T^2 in J` at both indices. These exact membership
results are controls on the source model, not an inferred uniform
nilpotence law. The chart certificates below use the actual source
identity and do not require V0.

At t=3 an exact Singular lift supplies polynomial coefficients a_k.
At t=4 a targeted homogeneous linear calculation is much smaller than
unrestricted module lifting. In weight `D=8t+2`, form every polynomial
multiple `m*E_k` with `wt(m)=4t+k`. Express these multiples in the full
monomial basis of S_D. The sizes are

| t | D | all weight-D monomials | available row multiples |
|---:|---:|---:|---:|
| 3 | 26 | 56 | 120 |
| 4 | 34 | 340 | 726 |
| 5 | 42 | 1792 | 3504 |

For the exact rational block solve put e=3d, so e^2=3(t+1). A
coefficient a+b*e acts by the rational matrix

```
[[a,3(t+1)*b], [b,a]].
```

This is an explicitly checked ring representation of the coefficient
field. Rational row scalings clear denominators. Modular pivot
selection chooses a square minor, after which the t=4 system is solved
over Q and its identity checked both as a rational matrix product and
as a fresh Singular polynomial expansion in the original d field.
The final coefficients satisfy

```
(B*eta)^2=sum_(k=2)^(2t) a_k*E_k.                    (5)
```

At t=4 the selected rational block system is 680 by 680 and its exact
solve plus serialization took under four seconds. The resulting
certificate is about 5.95 MB; some coefficients have more than 5,000
decimal digits. Coefficient growth, rather than the small number of
variables alone, explains the poor unrestricted-lift performance.

For t=5 the separately audited determinant route is also sufficient,
even if a full expansion of the rational inverse is costly. The
1792-column selected minor is specified by exact polynomial multiples
and the full target monomial order. Its reduction uses

```
p=32009, e=3d -> 7868, d -> 23962,
e^2=18, d^2=2 modulo p,
det(selected minor) -> 29155 modulo p, nonzero.       (6)
```

The producer used FLINT to obtain (6). The independent replay began
with a new Singular coefficient export from `controls_t5_raw.sing`,
parsed the rational field coefficients separately, checked all 1792
weight-42 monomials and all selected multiplier weights, and rebuilt
the integral matrix from scratch. NumPy integer Gaussian elimination
with row pivoting reproduced 29155. All raw denominators are p-units.
The accepted result is `INDEPENDENT_T5_RANK_MODEL_AND_DETERMINANT_PASS`
in `t5_rank_independent_result.json`. Thus (6) is a checked minor of
the stated characteristic-zero coefficient matrix, not a rank from
an unmatched modular presentation.

Here is the precise characteristic-zero argument. The matrix entries
are exact rational pairs in e. After clearing the recorded scalar
denominators they lie in Z[e]; the reduction is a declared ring map.
A nonzero determinant image proves that the exact determinant is
nonzero in Q(e). Therefore the selected columns form a basis of S_42
over that field. In particular the coefficient vector of T^2 is in
their span. This is a finite matrix argument about the actual rows,
not a claim that modular radical membership lifts.

For a fully specified unexpanded certificate, let C_* be that exact
square coefficient matrix and let h be the exact coefficient vector
of T^2 in the saved monomial order. Set

```
lambda=adj(C_*)*h/det(C_*),
a_k=sum_(selected columns j from row k)
       lambda_j * (recorded scalar multiple of monomial m_j).
```

These are exact field elements and polynomials, giving (5).
The matrix identity with the adjugate is the standard minors identity
in [Stacks, Lemma 10.15.5](https://stacks.math.columbia.edu/tag/07DQ).
Equivalently, over the local coefficient ring at the checked prime,
surjectivity of the finite coefficient map follows from
[Nakayama, Lemma 10.20.1(6)](https://stacks.math.columbia.edu/tag/00DV).
All hypotheses concern a finite module and a scalar determinant.
The affine scheme in (4) is not made proper by this argument.

A full-rank weight piece is sufficient for (5), not necessary. Nor
does one vanished weight piece establish V0 in a nonstandard weighted
ring: a pure variable axis whose weight does not divide D can be
invisible in S_D. Only the stated target-square and chart conclusions
are consumed from (6). No cone length at t=5 is inferred from this
matrix.

Two controls separate this argument from the forbidden shortcuts.
The ideal `(pX-1)` is unit modulo p but nonunit over Q; the rank
certificate here instead makes a finite matrix minor nonzero, and
explicitly bounds the polynomial supports that it spans. Even
homogeneity alone would not justify lifting membership: `(x+p*y)`
contains x modulo p but contains no power of x over Q. Its fixed
weight coefficient matrix lacks the full-row-rank property used here.

## 4. Literal polynomial certificates on both charts

For a fixed t, start with the verified identity (5). Let
`e_k=deg_b(a_k)`, with zero coefficient assigned degree zero, and put

```
m=max(4,max_k(e_k+d_k)),
Q_k=Delta^(m-e_k-d_k)*clear(a_k,e_k).
```

Homogenize (5) in b to degree m with independent numerator Y and
denominator Z. This is an identity in k[c,Y,Z]. Substitution
Y=A, Z=Delta is a polynomial ring map, and (3) gives

```
sum Q_k F_k=Delta^(m-4)*H^4.                         (9)
```

Every exponent is nonnegative. The identity is a polynomial identity
before localization, even if its coefficients are retained as finite
arithmetic circuits instead of expanded expressions. The exact t=3
check also expands (9) using the actual A,Delta,H and compares both
sides. The t=4 checker verifies the coefficientwise homogenization,
the actual maps (3), and equality with every saved main row.

The t=3 lift has b-degrees `(3,3,4,4,4)` and the t=4 lift has
`(0,0,4,4,4,4,4)`. Both have m=6. Consequently the literal main unit
certificate at these indices is

```
1=sum_k u^4*Delta^2*Q_k*F_k
  +(1-u*Delta*H)*sum_(j=0)^3 (u*Delta*H)^j.           (10)
```

For t=5 the determinant circuit has homogeneous source coefficients
and m may safely be taken as 7, whether or not an individual zero
coefficient could lower its actual b degree. The same proof gives
`sum Q_k F_k=Delta^3*H^4`; its main multiplier is `u^4*Delta`.
The selected rows are E5,...,E10, all quadratic in b; the selected
cofactor monomials have b degree at most five. The matrix circuit,
recorded row scalings, and coefficient-clearing operator specify every
cofactor in this certificate exactly. Its only scalar division is
by the proven nonzero exact determinant.

For the boundary use `eta-B=A-b*Delta`. Directly in the actual
coefficient ring,

```
B^4=(B*eta)^2-B^2*(eta+B)*(A-b*Delta).
```

Thus the following is a literal unit certificate in k[c,b,s]:

```
1=sum_k s^4*a_k*E_k
  -s^4*B^2*(eta+B)*A
  +s^4*B^2*(eta+B)*b*Delta
  +(1+s*B+(s*B)^2+(s*B)^3)*(1-s*B).                 (11)
```

Here eta is its saved polynomial in c,b, not an extra generator.
This covers the whole Delta=0 branch, including N=sigma=0 and all
root collisions. `transport_certificates.py` and the separate t=5
rank circuit give the exact source and generator-image checks.

There is also a uniform transport lemma without imposing n=2.
If `T^n=sum a_k E_k`, choose homogeneous cofactors of weight
`n(4t+1)-(4t+2-k)`. Then

```
e_k+d_k <= floor(n(4t+1)/(t+1)) < 4n.
```

With `m=max(2n,max(e_k+d_k))`, clearing gives
`sum Q_kF_k=Delta^(m-2n)H^(2n)`. Multiplying by
`u^(2n)Delta^(4n-m)` and adding the geometric-series multiple of
`1-uDeltaH` gives 1. On the boundary use

```
B^(2n)-T^n=B^n*(bDelta-A)*sum_(j=0)^(n-1) B^(n-1-j)*eta^j
```

and the length-2n geometric series for sB. These are all-t conversion
identities conditional on a source radical certificate. They do not
supply the missing n or a_k. This distinction is the uniform residual.

## 5. The exceptional t=2 control and agreement with (8.1)

The independent `audit_t2.py` starts from (1), reconstructs W and B,
and computes all four ideals U, X, main, and boundary separately over
Q at d=+1 and d=-1. Each is UNIT. Removing the E rows leaves NONUNIT
controls, as does the full positive cone without an inverse equation.

At d=-1, y=1/5, put c=c1. Exact reconstruction gives

```
B=18c^5/125-3c^2*b/5,
eta=3c^4/10+9c*b/2,
E2=441c^8/2500-6c^5*b/25-9c^2*b^2/4,
E3=102c^7/25-93c^4*b/5,
E4=177c^6/50-33c^3*b/2,

B*eta=(6c/5)E2-(72c^2/1025)E3+(171c^3/5125)E4.       (7)
```

This is an ideal identity, valid before taking radicals. A standard
basis up to scalar normalization is

```
59c^6-275c^3*b, c^4*b, c^2*b^2.
```

Its reduced support is the complete b-axis c=0. On that axis

```
C=x, W=-25*x^5/4+(5b/2)*x^2, B=eta=0, b arbitrary.
```

Thus V0 fails while the weak target holds. In U, the inverse equation
would read 1=0 on this family. In X it would also read 1=0. The
exceptional family was excluded by the target's specified open set,
not by an unauthorized gauge or the removal of a root collision.

The t=2 main unit can also be seen without a basis computation. At
d=-1, exact coefficient clearing yields

```
H=-207c^6/250,
F3=9c^8(32c-3325)/1250,
F4=9c^7(7c-580)/250.
```

Since H is inverted on main, c is a unit there. The remaining linear
factors have the constant combination

```
7(32c-3325)-32(7c-580)=-4715.
```

Hence main is empty, exactly as (7) predicts. At d=+1, y=2/5, the
monomial candidate has `W=25x^5/48-(b/4)x^2` and residual `-2b^2x^4`,
so only b=0 survives on that axis. Independent exact certificates
for this factor are in `audit_t2.json`; no conjugate-factor inference
is used across the split product algebra.

For t=3,4,5 the decoupled main gauge is also inhabited over the
declared field: set c1=1 and all other c_j=0, check Delta and H are
nonzero, and take `b=A/Delta`, `s=Delta/H`. The terminal rows are
what exclude these points. On the decoupled boundary, an independent
t=3 NONUNIT calculation and explicit algebraic point construction
are described below. These controls prevent tautological acceptance
of an inconsistent normalization.

## 6. Uniform homogeneous interpretation of the boundary

The weights of the four coefficients are

```
wt(M)=2t+1, wt(N)=t, wt(rho)=2t, wt(sigma)=t-1.
```

Therefore H is homogeneous of weight 3t, though Delta and A are
inhomogeneous. Before any terminal row is imposed,

```
H=N*eta-B*sigma.
```

On X, where B=eta is a unit, this becomes `H=B*Delta` and the slice
equation gives `A=b*Delta`. Consequently the complementary closed
piece is exactly V(H) in X, scheme-theoretically; the main piece is
D(H). Under U=G_m x X, homogeneity multiplies H by the unit v^(3t),
so these are the corresponding pieces of the localized homogeneous
cone as well. In particular

```
X_main=empty     <=> T*H in radical(J),
X_boundary=empty <=> T in radical(J+(H)).             (12)
```

This is a useful uniform reformulation, not an assertion that either
radical membership is automatic. It has an exact gluing rule. If
`(T*H)^r in J` and `T^s=H*L mod J`, then

```
T^(r(s+1))=T^r*(T^s)^r=T^r*H^r*L^r=0 mod J.
```

Thus any two branch certificates yield a certificate for T itself.
No r or s uniform in t was found.

The boundary is not a defective normalization. With C held fixed,
`partial_b(B/eta)=H/eta^2`; this is an ambient derivative, not a
vector field proved tangent to V(J). Let
`D_c=sum j*c_j*partial_(c_j)`. The weight identities give

```
D_c Delta=N+(t-1)Delta,
D_c A=-M+2t*A,
D_c(B-eta)=B modulo (Delta,A).
```

The last quantity is a unit on the boundary. Vanishing of the
b-direction derivative therefore does not make the full slice singular
or contradict its scaling transversality. It does not identify a
repeated-root stratum of C either.

An exact negative control at t=3 shows that the decoupled boundary
`(Delta,A,1-sB)` is NONUNIT of dimension one; imposing b=0 leaves
a NONUNIT scheme of length four. These standard bases were computed
over Q(d), 3d^2=4. There is an explicit algebraic description. Set
`c1=a`, `c2=a^2*z` and write

```
M=a^7*m(z), N=a^3*n(z), rho=a^6*r(z), sigma=a^2*sigma0(z),
H=a^9*h(z), h=n*r-m*sigma0.
```

The exact h is a squarefree quartic, and
`gcd(h,m*n*r*sigma0)=1`. For any of its roots z, choose

```
a=sigma0(z)/n(z), c1=a, c2=a^2*z, b=0,
s=1/(a^7*m(z)).
```

All denominators are nonzero and the decoupled equations hold.
The terminal E rows are essential to empty this branch. The raw
coefficient data, exact gcd checks, and dimensions are saved in
`boundary_structure_t3.sing` and its completed log.

The other proposed shortcut, reusing the first descent as a Keller
descent, also fails a literal hypothesis. The frozen reconstruction
gives

```
Jac_(h,x)(Q,P)=tau+c*b1*x+c*b2*x^2+c*b3*x^3-c*(h-b4)*x^4,
c=-yg.
```

Its h*x^4 coefficient is a scalar unit. Even when tau is invertible,
this is not a constant Jacobian on the plane. The other marked chart
has a nonzero linear Jacobian form; a change to a monomial-Jacobian
object does not restore the original constant-Jacobian source theorem.
A second descent would need an actual closed marked category, a
polynomial coefficient map, preservation of the inherited data, and a
strict decrease within that category. The equations Delta=A=0 supply
none of those missing arrows. The next section checks a concrete
degree-lowering substitution directly.

## 7. Uniform differential reformulation and failed descent

### 7.1. A t-independent polynomial differential equation

Use `N=t+1`, so `q=2N-1`. Avoid overloading the slice determinant H by naming
the differential factor `Hdiff`. Starting from the charged RC1-RC2 identity,
put

```
L = K/y = x^2*C/y-b,
P = x*W-b^2/4,
Hdiff = 2*x*P'-3*P-B*x+(3/2)*L*(L+b),
Rfree = (3/16)*L^2*(L*(L+2*b)-4*B*x)
        -eta*x^2*(b*L/2+B*x).
```

Then the full Abel equation is exactly

```
P*Hdiff = Rfree.                                      (UF)
```

All coefficients in (UF) are rational constants: y and t have disappeared
from the differential equation. They occur only in the degree and leading
coefficient constraints. The initial jets are

```
L(0)=-b,    L'(0)=0,
P(0)=-b^2/4,    P'(0)=-B,    P''(0)=2*eta.              (UJ)
```

The complete normalization is

```
deg L=N,    lc(L)=1/y,
deg P=2*N,  lc(P)=omega,
3*d^2=N,
omega*y^2=1/(4*(2*d+1)).                              (UL)
```

Conversely, (UJ) makes

```
C=y*(L+b)/x^2,
W=(P+b^2/4)/x
```

polynomials with the prescribed constant/linear jets. The leading conditions
make C monic of degree t-1 and W normalized of degree 2t+1. Substitution into
the charged polynomial identity gives `x^2*F=P*Hdiff-Rfree`. Multiplication by
x is injective in any coefficient ring's polynomial ring, so the equation is
equivalent scheme-theoretically; it is not merely an equivalence on reduced
points or away from x=0. This last fact also keeps all root collisions.

The new form follows by replacing `K` with `y L` in RC1:

```
3*K*(K+yb)/(2*y^2) = (3/2)*L*(L+b),
Q = y^2*(L*(L+2*b)-4*B*x),
J_RC = b*L/2+B*x.
```

No variable denominator is introduced. A direct exact symbolic expansion,
with W,W',C,b,B,eta,y,x independent and y inverted, checked

```
x^2*F-(P*Hdiff-Rfree)=0.
```

This formulation makes an especially compact single uniform residual:

> There is no polynomial pair P,L over an algebraically closed field of
> characteristic zero satisfying (UF), (UJ), and (UL) for any N>=4 and either
> d, with eta=B nonzero.

That statement is exactly the slice target, not a weaker support theorem.
It remains open in these notes.

#### The leading comparison remains consistent at every N

Let `a=lc(L)` and `p=lc(P)/a^2`. The top coefficient of (UF) is

```
(4*N-3)*p^2+(3/2)*p-3/16=0.                           (UT)
```

With `N=3*d^2`, the selected solution is

```
p=1/(4*(2*d+1)).
```

Exact substitution checks (UT). Thus removing t from the differential
equation does not produce a degree contradiction: the required leading
ratio solves the top equation for each index and factor. To finish through
(UF), one must classify its polynomial solutions with all the linked jets.
No assertion that a generic Abel equation of the same degrees is impossible
is made.

#### The exceptional proportional-square family in this form

At t=2, d=-1, y=1/5, the exceptional family becomes

```
L=5*x^3-b,
P=-L^2/4,
B=eta=0.
```

This is an exact explanation of the boundary rather than an omitted chart.
More generally, when B=eta=0 and P=-L^2/4, expansion of (UF) gives

```
P*Hdiff-Rfree = L^3*(x*L'-3*L-3*b)/4.                 (US)
```

Over a field, nonzero L therefore forces
`x*L'=3*(L+b)`, hence `L=a*x^3-b`. This proportional-square family has degree
N=3, i.e. t=2. If b is nonzero and P is proportional to L^2 at all, the
constant jet already forces its proportionality factor to be -1/4. This
classification concerns the proportional-square locus only; no argument
here forces an arbitrary solution onto that locus.

### 7.2. Why the elementary degree descent does not close

An obvious degree-lowering attempt is to remove a linear factor of C and
two degrees from W. At the marked origin, B is a unit on the target, so

```
W(0)=-B != 0.
```

In particular W cannot be divided by x^2, even on the stratum `C=x*Ctilde`.
The canonical polynomial substitute is instead

```
W=-B+eta*x+x^2*V,    deg V=2*t-1.
```

After this substitution, `F/x^2` is polynomial: the constant and linear
coefficients of F vanish identically by the marked jets. Its coefficient
of V' is exactly

```
2*x^3*V+2*eta*x^2-2*B*x-b^2/2.                       (UD)
```

This was checked directly over Q with independent symbols. The same Abel
category at t-1 would require a V' coefficient of the form
`2*x*V-b_new^2/2`. To obtain the coefficient of xV from (UD), division by
x^2 yields

```
2*x*V+2*eta-2*B/x-b^2/(2*x^2).
```

The pole `-2B/x` is present on the entire target, including b=0. Consequently
this literal truncation does not define a polynomial Abel equation of the
same category. A successful second descent would need a different
transformation, or a larger marked rational category with a proved return
to polynomiality, and would have to track these terms. Decreasing the
displayed degree of V alone is not a closed induction.

The same issue appears at other C roots in a different form. The charged
RC9 bound says

```
deg gcd(C,P*Hdiff)<=3   on B*eta != 0.
```

In particular `deg gcd(C,P)<=3`. Thus for t>=5 the whole degree-(t-1)
polynomial C cannot divide P. A proposed global root removal which assumes
that divisibility is false on the target. On repeated-root fibres the
correct bound counts gcd multiplicity; it does not assert the existence
of a distinct root outside the exceptional locus. A root can remain in C
with excess multiplicity even when the gcd has small degree.

This is a defect of the stated simple transformations, not a proof that
every conceivable marked descent is impossible.

### 7.3. Global rational parametrization of the quartic factor curve

Assume B*eta is nonzero throughout this subsection. There is an
additional global reduction behind (UF). Regard Rfree as a
polynomial in the two independent variables x and L, with b,B,eta fixed.
On the locus xL nonzero, its zero curve is rational. Put

```
f(v)=-2*b*v+4*B*v^2+(8*b*eta/3)*v^3+(16*B*eta/3)*v^4,
g(v)=f(v)/v
    =-2*b+4*B*v+(8*b*eta/3)*v^2+(16*B*eta/3)*v^3.
```

The exact identity is

```
Rfree(x,L)=(3*L^4/(16*x))*(x-f(x/L)).                 (UR1)
```

Consequently the inverse rational parameter is `v=x/L`, and the
parametrization is

```
x=f(v),    L=g(v).                                    (UR2)
```

These identities were checked by exact symbolic expansion. The rational
expression is used only in the explicitly localized ring; its numerator
is the original polynomial Rfree. Geometrically the plane quartic has a
triple origin, which the open condition xL nonzero removes. The formulas, not
a generic smoothness assumption, establish the parameterization on the
open set for every parameter value.

#### The b nonzero chart: an exact finite-algebra transform

Assume b B eta nonzero and a solution of (UF), and write

```
R(x)=Rfree(x,L(x))=P(x)*Hdiff(x),
Q(v)=L(f(v))-g(v).
```

Since L(0)=-b, the constant R(0) is `-3*b^4/16`, hence x is a unit in
`k[x]/(R)`. Reducing R modulo L gives `-B*eta*x^3`, so L is also a unit
there. Define v=x/L. Equation (UR1) gives x=f(v); dividing by the unit v
gives L=g(v). Conversely, in `k[v]/(Q)`, g is a unit because

```
gcd(g,Q)=gcd(g,L(0))=1.
```

Also Q(0)=b is nonzero, so v and f(v)=v g(v) are units. These calculations
give literal inverse k-algebra maps

```
k[x]/(R)  <-->  k[v]/(Q),
v=x/L(x),       x=f(v).                               (UR3)
```

The maps are valid on all multiplicities. Both algebras have dimension
4N: the leading term of R is nonzero of degree 4N, and f has degree four
because B eta is nonzero. Under (UR3), the factor P selects a degree-2N
factor `M_P(v)` of Q, and Hdiff selects its complementary degree-2N
factor. In particular

```
M_P = monic gcd(P(f(v)), Q(v)),
deg M_P=2*N.
```

The finite-algebra isomorphism proves this including repeated factors;
it is not a comparison only of distinct roots. Equivalent descriptions
can use resultants or norms, but they must keep the differential equation
defining Hdiff. An arbitrary half-degree factor of Q does not provide
that differential factor.

#### The b zero chart: the distinguished triple point is removable explicitly

If b=0 and B eta is nonzero, then L has a factor x^2, P has order one
at x=0, and Hdiff has order two. Thus

```
Rbar=R/x^3,
Pbar=P/x,
Hbar=Hdiff/x^2
```

are polynomials, with `Rbar=Pbar*Hbar` and `Rbar(0)=-B*eta` nonzero.
Their degrees are 4N-3, 2N-1, and 2N-2. Write `L=x^2*Ltilde`. Here
`f=v*g`, with g of degree three, and

```
Q/g = v^2*g(v)*Ltilde(f(v))-1.                        (UR4)
```

This polynomial has degree 4N-3 and is coprime to g; it is also nonzero
at v=0. The same mutually inverse maps as in (UR3) therefore give

```
k[x]/(Rbar)  <-->  k[v]/(Q/g).                        (UR5)
```

The two factors now have degrees 2N-1 and 2N-2. This is the correct
version of the transform on b=0; using the b nonzero quotient unchanged
would silently omit the marked x=0 behavior or count the three
extraneous parameter roots.

#### What the global order count does and does not prove

The transformed total intersection length is 4N on b nonzero and 4N-3
after the explicit b=0 removal. The differential factors have exactly
the complementary lengths above. All these integers are consistent for
every N>=4. No integrality condition on d follows from this count.
The branch curve being rational likewise supplies no forbidden genus.

For a check useful in any subsequent residue calculation, differentiation
of Rfree before specialization gives

```
(partial Rfree/partial L)(f(v),g(v))
    =(3/16)*g(v)^2*f'(v).                             (UR6)
```

Thus a calculation dividing by f' must branch on its zeros; they are
not absent by the parameterization. On the graph, the derivative of
R at an intersection is

```
R'(x)=(3/16)*L(x)^2*Q'(v),    v=x/L(x),
```

evaluated at the intersection. This relates multiplicities correctly
but, together with `R'=P'Hdiff+P Hdiff'`, remains compatible with (UF).
It did not yield a residue whose nonzero value contradicts polynomiality.
The first still-missing statement is precisely that no factor of the
prescribed size in (UR3) or (UR5) satisfies the linked differential
formula for Hdiff and the initial jets. The degree transform alone
does not lower N, so it is not a terminating second descent.

## 8. Full dependency chain and the remaining quantified statement

In the original residual variables, the banked row-image theorem
identifies the ideal J with the positive terminal ideal after the
triangular coefficient change and high elimination. Its explicit
row identity is

```
gy*F(x)+3x*(D0(x+b4)-D0(b4))=0.
```

Translation is triangular on nonconstant coefficient rows; multiplying
by x shifts their indices. This is the declared generator map behind
the use of the F3 rows, not an inference from matching lengths.

Write `I+=(T_(t,1),...,T_(t,2t-1))`, and use the homogeneous target
`tau=T_(t,0)-yg`. The boundary identity is

```
R_boundary=U_h'(b4)+b3*C_h(b4)=y*eta/3,
tau=-(gy/3)*B*eta modulo I+.
```

The scalar gy/3 is a unit. Therefore at every fixed t, factorwise,

```
both ideals in (4) are unit
  <=> X=empty
  <=> U=empty
  <=> B*eta in radical(J)
  <=> tau in radical(I+)
  <=> (I+, T_(t,0))=S_t                                  [(8.1)]
   => terminal normalized receiver chart is empty
   => original K16 ray system has no solution
       [banked constant spine, normalizer, second affine spine]
   => theorem (T) at t.                                  (8)
```

For the weighted-cone equivalence in (8), if tau is nilpotent modulo
I+, then `yg+tau` has a finite geometric-series inverse. Conversely,
a geometric cone point with tau nonzero could be rescaled by a
weight-(4t+1) scalar so that tau=-yg, contradicting the displayed
unit ideal. The argument permits a positive-dimensional cone and
does not invoke V0, Cohen-Macaulayness, a DVR, an hsop, or an
unproved rank-curve height statement. Literal T_(t,0), with its
nonzero constant, is never placed in radical(I+).

This report's finite certificates supply the antecedent for t=2,3,4,5.
They agree with the banked t=3,4 theorem proofs. The frozen reports
also bank a characteristic-zero range through t=7; this lane does not
reissue certificates at 6 and 7 or enlarge that whole-index range.
Consuming that stated range, the remaining whole-index frontier is
t>=8. No new whole-ray promotion is made.

Here is one fully explicit residual, with no fixed nilpotence bound:

```
OPEN[K16-INTRINSIC-SLICE-UNIT], unchanged mathematical target:

For every integer t>=8 and every field factor k of
Q[d]/(3d^2-t-1), reconstruct E_k,B,eta by (1) and its stated
scalar-unit recurrence. There exist an integer n>=1 and
homogeneous a_k in k[c1,...,c_(t-1),b] of weight
n(4t+1)-(4t+2-k) such that

        (B*eta)^n = sum_(k=2)^(2t) a_k E_k.             (R)
```

Negative cofactor weights mean the corresponding coefficient is zero.
The integer n and all cofactor degrees may depend on t and on the
factor. Statement (R) is equivalent to the missing radical target;
the general transport in Section 4 turns it into literal certificates
for both ideals in (4). Without consuming the frozen t=6,7 results,
replace t>=8 in (R) by t>=6. No assertion that n=2 works uniformly is
made. A socle bound or the observed n=2 at these finite indices does
not prove (R).

The uniform degree-independent differential formulation above is an
equivalent single polynomial-solution statement. The new rational
quartic transform retains the differential factor and the b=0
marked-point correction, but its lengths are compatible for every N.
The unresolved step is excluding a factor of the prescribed size
that also satisfies that differential linkage and all initial jets.
An arbitrary factorization or an unlicensed second descent does not
provide that exclusion.

## 9. Reproduction, rejected attempts, and completion audit

The fresh direct reconstruction and chart emission can be replayed by
running the frozen emitter with `t --raw-only --root
box/k16xempty-20260905`, then `emit_charts.py t`, then the emitted
Singular scripts. All exact coefficient fields and ring orders are
written in those scripts. For the completed literal certificates use:

```
stdbuf -oL python3 box/k16xempty-20260905/audit_t2.py
stdbuf -oL python3 box/k16xempty-20260905/transport_certificates.py 3 --run --expand-main
stdbuf -oL python3 box/k16xempty-20260905/transport_certificates.py 4 --run
stdbuf -oL python3 box/k16xempty-20260905/rank_minor_replay.py
stdbuf -oL python3 box/k16xempty-20260905/t5_rank_chart_circuit.py
```

The t=5 replay starts from the exact raw source rows, reconstructs the
complete weighted monomial basis and listed minor, checks the rational
field map and all denominators, and recomputes its determinant with a
different elimination implementation. The determinant/adjugate circuit
then gives both literal units; its full specification is
`t5_rank_chart_circuit.json`. The additional t=5 rational solve and
exact matrix-product check succeeded in about 587 seconds. Its expanded
source-cofactor file is 200,267,594 bytes. The optional fresh Singular
expansion hit its 600-second cap, returned 124, and was reaped; it is
typed INCONCLUSIVE_TIMEOUT. No t=5 expanded-source PASS is claimed.
The independently checked minor and exact adjugate circuit are the
accepted, complete t=5 proof.

Rejected or incomplete jobs are retained with their actual scope.
The naive exact t=3 main GB timed out at 180 seconds and the t=4
boundary GB at 300 seconds. Neither timeout was read as nonemptiness.
Local larger exact jobs were stopped and reaped before moving them
to the permitted workers. Fleet t=4 module lifting was stopped after
the separate exact linear certificate succeeded; fleet t=5 full-cone
GB was stopped after the independently replayed determinant certificate
succeeded. Neither produced an accepted basis. No msolve success string
or modular inverse-chart UNIT is part of the proof.

CAS processes ran in the foreground under stdbuf and fixed timeouts;
long Singular jobs set CPU, thread, and FLINT-thread flags to one,
and the linear-algebra processes were restricted to one thread. The lane stayed
within five CAS cores across the local machine and fleet. Only the
permitted workers 172.30.0.7 and 172.30.0.18 were used. The separate
same-model checks cover arithmetic and maps; they are not a
different-model campaign promotion vote. No task was left running at
sealing. Final job status, accepted-result hashes, source links,
and the artifact manifest are banked beside the report.

No new exit-price assertion is made, so the FALLACY-v2 charge-basis
declaration is inapplicable. The checks relevant here are the exact
field-factor map, the constant shift in tau, preservation of vanished
pivots and collision strata, the scoped matrix lift, and the distinction
between a finite certificate and the quantified residual (R).

<!-- BODY-END -->
