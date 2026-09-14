# K16 intrinsic quotient: exact emptiness through t=5 and the uniform residual

Lane: `k16-xempty-astra-20260905`. Astra, primary. 2026-09-05.

**Final verdict placeholder: finite chart certificates are being completed;
uniform emptiness is OPEN. This draft is not sealed.**

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

FINITE_RESULT_TABLE

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

RANK_AUDIT_RESULT

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

CERTIFICATE_TRANSPORT

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

BOUNDARY_STRUCTURE

## 7. Uniform differential reformulation and failed descent

UNIFORM_STRUCTURE

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

OPERATIONAL_RECORD

No new exit-price assertion is made, so the FALLACY-v2 charge-basis
declaration is inapplicable. The checks relevant here are the exact
field-factor map, the constant shift in tau, preservation of vanished
pivots and collision strata, the scoped matrix lift, and the distinction
between a finite certificate and the quantified residual (R).
