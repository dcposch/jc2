# Hostile audit: quarter-root characteristic/de Rham tower R7

Date: 2026-08-27  
Reviewer lane: `a1_total_lift_design` / Sol2  
Target producer:
`xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7-sol-20260827.md`,
SHA-256
`b0e60671662953a50318e4989a20a08e5b84e28cb1bfaea075e241fc367a818a`  
Target case freeze:
`cases/ggv_quarter_root_characteristic_r7_20260827/FREEZE.md`,
SHA-256
`4dedc255ea4de97dace097d201e7f61599f0a13b23e42c3a74cf3481d0ba6d08`.

## Verdict

**CORRECTION: THE EXACT CONJUGACY AND DE RHAM NECESSITY THEOREM PASS;
THREE SCOPE/KERNEL CLAIMS REQUIRE REPAIR.**

The identities

```text
E=8P^19((tP_t-P)W_X-tP_XW_t)=8P^21 J(s,W),
W_X|s=-(s^22/8)(Q+(s/2)Q_s),
w_(n+22)'=-(n+2)q_n/16
```

are correct.  The formal substitution is invertible over `L`, the displayed
`q0,q1,q2` formulas are correct, exact `E=t^22` forces all `q_n dX` to be
exact, and coefficientwise exactness constructs a solution over `L`.
Trace descent recovers R5 at `q0` and makes the rational `q2` condition a
genuine base-field necessary condition.

The smallest repairs are:

1. The homogeneous kernel is **all** of `C_L[[s]]`, where
   `C_L=ker(d/dX:L->L)`, not only the coefficients `w0,...,w21`.  Every
   inhomogeneous coefficient `w_(n+22)` also has an arbitrary integration
   constant.
2. The “four Kummer characters” statement is literal only after adjoining
   `mu_4` and passing to a setting where `p->zeta p` is an automorphism.
   Over an arbitrary characteristic-zero `K`, one may retain the exponent
   grading, but not an unqualified four-character decomposition.
3. Bounded raw support does not make the tower finite by truncation.  It
   gives an algebraic implicit presentation of `Q`, which generally has
   infinitely many nonzero coefficients.  No finite decision bound or
   recurrence certificate is proved in R7.  Also, a frozen raw jet through
   weight 22 licenses only `q0`; higher `q_n` require the exact Keller
   identity or determinant rows through weight `n+22`.

With these repairs, R7 is a valid exact theorem over `L` and a promising
necessary-condition generator for a fully typed polynomial Keller client.
It is not yet a finite compiler for D3/D5G's weight-22 corpus.

## Verdict table

| Charged item | Verdict |
|---|---|
| Eighth-root branch `P_0=p` in `L[[t]]` | **PASS** |
| Formal invertibility of `s=t/P` | **PASS** |
| Differential-polynomial conjugacy and signs | **PASS** |
| Formula `w_(n+22)'=-(n+2)q_n/16` | **PASS** |
| `q0,q1,q2` formulas | **PASS** |
| Exact target forces all rows | **PASS** |
| Truncation modulo `t^23` forces only `q0` | **PASS** |
| Converse over `L` | **PASS** |
| Kernel described by only `w0,...,w21` | **CORRECTION** |
| Descent to `K(X)` | **NOT AUTOMATIC; producer firewall is correct** |
| Trace recovery of R5 and rational `q2` descent | **PASS** |
| Four-character cycling over arbitrary `K` | **CORRECTION: base-change qualification required** |
| Bounded support makes the tower effectively finite | **NOT PROVED; false if it means coefficient truncation** |
| Existing D3/D5G endpoint data imply higher rows | **NO; only `q0` is licensed** |
| Actual typed polynomial Keller pair has exact `E=t^22` | **PASS** |

## 1. Formal field and coordinate change

Let `R=K(X)`, choose a field factor `L=R(p)` with `p^4=H`, and extend
`d/dX` uniquely to the finite separable extension `L/R`.  Since
`p^8=H^2=F_0`, characteristic zero gives the unique binomial branch

```text
P=p+O(t) in L[[t]],  P^8=F.
```

The series

```text
s=t/P=t/p+O(t^2)
```

has invertible linear coefficient `1/p`, so it has a unique compositional
inverse `t=T(X,s)` in `sL[[s]]`.  Derivatives with respect to `X` commute
with this formal substitution by the ordinary chain rule.  No convergence
or additional algebraic extension is required.

The constant field need not equal `K`.  For example, with
`K=Q`, `H=2X^4`, and `p=2^(1/4)X`, the field `L` contains the constant
`2^(1/4)`.  Consequently every occurrence of “arbitrary scalar series” in
the extension theorem must mean coefficients in

```text
C_L={c in L : c'=0}.
```

Base-field descent of the resulting `G` remains a separate invariance
condition, as the producer correctly warns.

## 2. Independent conjugacy derivation

Set `F=P^8` and `G=P^12W`, with the derivatives here initially taken at
fixed `(X,t)`.  Direct product-rule expansion gives

```text
12F_XG-8FG_X = -8P^20 W_X,
F_XG_t-F_tG_X = 8P^19(P_XW_t-P_tW_X).
```

Therefore

```text
E=8P^19((tP_t-P)W_X-tP_XW_t).                       (2.1)
```

For `s=t/P`,

```text
s_X=-tP_X/P^2,
s_t=(P-tP_t)/P^2,
J(s,W)=s_XW_t-s_tW_X
      =((tP_t-P)W_X-tP_XW_t)/P^2.
```

This proves `E=8P^21J(s,W)`.  If `E=t^22=s^22P^22`, then
`J=s^22P/8`.  Writing `W` in `(X,s)` coordinates gives
`J=-s_t W_X|s`; since `1/s_t=t_s` and `t=sP`,

```text
W_X|s=-(s^22/8)P(P+sP_s)
     =-(s^22/8)(Q+(s/2)Q_s),  Q=P^2.                (2.2)
```

If `Q=sum q_n s^n` and `W=sum w_m s^m`, coefficient comparison in (2.2)
is exactly

```text
w_(n+22)'=-(n+2)q_n/16.                             (2.3)
```

All scalars are nonzero in characteristic zero.

## 3. Exact target, truncations, converse, and kernel

Equation (2.3) proves the forward theorem: an exact solution `G` makes every
`q_n dX` exact in `L`.  Conversely, if `q_n=a_n'`, a particular solution is
obtained by taking

```text
w_(n+22)=-(n+2)a_n/16,
w_0=...=w_21=0,
```

then setting `G=P^12W` and composing back with `s=t/P`.

The full solution space is

```text
W_particular + Phi(s),  Phi(s) in C_L[[s]].          (3.1)
```

The producer's phrase that only `w0,...,w21` constitute the characteristic
kernel is incomplete: constants may be added independently to every
`w_(n+22)` too.  If one also requires `G_0=H^3=P_0^12`, then (3.1) must be
normalized by `Phi(0)=1`; descent can impose further coupled conditions.

More generally,

```text
E=t^22+O(t^N)
```

transforms to (2.2) modulo `s^N`, because all divided factors are units and
`ord_s(t)=1`.  It forces precisely the displayed exactness rows with
`n+22<N`.  Thus:

```text
mod t^23 -> q0 only,
mod t^24 -> q0,q1,
mod t^25 -> q0,q1,q2.
```

This confirms the producer's explicit `t^23` firewall and sharpens the
general cutoff.

A concrete counterfixture shows why the firewall is load-bearing.  Take

```text
H=X^4, p=X,
F=X^8+4X^4 t.
```

Then `q0=X^2` is exact but `q1=1/X`, so `q1 dX=dX/X` has nonzero residue and
is not rationally exact.  Equation (2.2) can be solved through `s^22` by
choosing `w22=-X^3/24`, giving a finite truncation with
`E=t^22+O(t^23)`, but it cannot extend to an exact solution.  Endpoint data
alone therefore do not license the `q1` row.

## 4. Independent `q0,q1,q2` expansion

In `(X,s)` coordinates the implicit equation is

```text
P^8=F(X,sP).
```

Write `P=p+a s+b s^2+O(s^3)`.  Comparing the first two coefficients gives

```text
a=F1/(8p^6),
b=F2/(8p^5)-5F1^2/(128p^13).
```

Squaring yields

```text
q0=p^2,
q1=F1/(4p^5),
q2=F2/(4p^4)-F1^2/(16p^12)
  =F2/(4H)-F1^2/(16H^3).
```

An independent sparse-Q expansion, not importing the producer verifier,
replayed these coefficient equations exactly.  The producer's `1/15`
mutation of the final denominator fails as charged.

## 5. Descent, characters, and R5

Let `M=K(X)(p^2)`.  If `q0 dX=p^2dX=da` in `L`, then separability and the
uniqueness of the extended derivation give

```text
d Tr_(L/M)(a)=[L:M] p^2 dX.
```

After division by the nonzero degree, `q0 dX` is exact in `M`; the converse
is immediate.  Write `H=A^2B`, put `w=p^2/A`, and choose the sign so
`w^2=B`.  Then

```text
d(vBw)=(Bv'+(3/2)B'v)w dX.
```

Together with the already audited quadratic pole argument, exactness of
`Aw dX` is equivalent to

```text
A=Bv'+(3/2)B'v.
```

Hence the grade-zero row recovers R5 exactly, including shared factors of
`A` and `B`.

Likewise `q2` lies in `K(X)`.  If it is exact in `L`, tracing all the way to
`K(X)` and dividing by `[L:K(X)]` supplies a primitive in `K(X)`.  The
producer's rational `q2` residue test is therefore a valid necessary
condition for an actual exact base-field solution.

For the character claim, after adjoining a primitive fourth root `zeta`
and assuming `p->zeta p` defines the relevant automorphism, uniqueness of
the implicit branch gives

```text
P^sigma(X,s)=zeta P(X,zeta s),
q_n^sigma=zeta^(n+2) q_n.                            (5.1)
```

This proves the four-cycle after the stated base change.  Without `mu_4`,
or when `p^4-H` has smaller degree, there need not be four automorphisms or
four literal character eigenspaces.  Formula (5.1), suitably base-changed,
is the clean repair.

## 6. Exact polynomial clients versus bounded raw jets

For an actual polynomial Keller pair in the typed chart

```text
x=t^3X, y=t^-1, f=t^-8F, g=t^-12G,
```

the chain rule gives exactly

```text
[f,g]_(x,y)=t^-22 E(F,G).
```

Thus `[f,g]=1` really does imply the exact identity `E=t^22`, and every R7
row is a legitimate necessary condition for such a fully sourced client.

This must not be weakened to “bounded support.”  The current frozen D3/D5G
corpus contains generic raw rows only through weight 22 and proves no exact
Keller specialization.  It licenses `q0`, not `q1,q2,...`.  Moreover bounded
support does not truncate `Q`: for the bounded polynomial `F` in Section 3,
`Q=P^2` satisfies

```text
(Q^4-X^8)^2=16X^8 s^2 Q.
```

If nonconstant `Q` were a polynomial of `s`-degree `d`, the two sides would
have degrees `8d` and `d+2`, forcing `7d=2`, impossible.  Hence this bounded
`F` produces infinitely many nonzero `q_n` in general.

An eventual finite algorithm may be possible using the algebraic equation,
Hermite reduction, and a certified recurrence in the finite-dimensional de
Rham quotient, but R7 does not construct or bound such a recurrence.  The
phrase “for bounded raw support effectively finite” should therefore be
deleted or downgraded to a research program.

## Scope firewall

After the three repairs, R7 proves an exact differential-algebra equivalence
over the fixed finite extension `L` and necessary trace-descended rows for an
actual exact base-field Keller client.  It does not prove descent of the
converse, polynomiality, finite verification of the infinite tower, raw
source landing, a face/family exclusion, `G2-PSC`, `G2-BD`, a Keller pair,
a counterexample, or JC2.
