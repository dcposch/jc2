# Sigray Section 7: weighted Euler inequality without kappa transport

**Date:** 2026-08-28  
**Producer:** coordinator (Sol Ultra)  
**Status:** provisional; requires different-model hostile review

## 0. Result

The final delta gate `758c0226...` correctly refutes transport of the
jump/max value `kappa_F` across fibres.  The roots of `P(z)-a` can change
from the zero coefficient orbit to nonzero coefficient orbits, so the
post-height lattice index can jump.

That obstruction kills the fixed-baseline proof of `(22-cl)`, but it does
not kill the inequality used by Corollary 7.1.  The repair is to integrate
the **actual cluster weight**

```text
w_i(z) = sum_(P in C(i,z)) Lambda(P)
```

on the abstract quotient line.  Away from finitely many coefficient
collisions this weight equals the maximal possible jump baseline.  At a
collision, proper local-degree conservation makes the special weight at
least that generic baseline.  Compactly supported Euler integration on
`A1` therefore gives a lower bound, despite the failure of pointwise
`kappa` transport.

The conclusion is

\[
 td(f,g)\ge 1+
 \sum_{F\in T_{a,cv}}\kappa_F(\pi(F)-1)                 \tag{C7.1*}
\]

for every fibre `f=a`, and hence the same inequality for every subset of
pairwise distinct critical-value flags.  This is exactly the strength of
the repaired Corollary 7.1 needed by the first-separation exit budget.

No claim is made for the printed per-puncture `delta_a`, printed equation
`(22)`, or the failed fixed-baseline `(22-cl)` formula.

## 1. Reviewed inputs

Let `Phi=(f,g):A2_C -> A2_C` be a polynomial Keller map and put
`d=td(f,g)`.

The proof uses the following reviewed pieces.

1. The every-fibre Proposition 5.8 replacement
   (`47eef0925470fc769eec08e6d3bf972446feaaff6f6ef709c154edaa31054caf`)
   gives the meromorphic degree `d` of `g` on the normalization of every
   fibre `f=a`.
2. The corrected Section 7 local package gives a unique zero-order flag for
   every finite-value puncture, root-orbit realization, direction clusters,
   and the proper local-tube conservation argument for Proposition 7.3.
3. Sections 2--4.2 and 5 of the failed quotient report, as adjudicated by
   the final Terra delta gate `758c0226...`, give:

   - an abstract quotient line `U_i=A1_eta/Gamma_i ~= A1_z` for each
     reference critical-value flag;
   - descended polynomials `P_i,Q_i` and
     `phi_i(z)=(P_i(z),Q_i(z))`;
   - the choice-independent quotient transport `tau_(i,a)`;
   - a bijection from `coprod_i U_i(C)` to all finite-value direction
     clusters in all fibres, with no cyclic or cross-flag duplication.

The delta gate expressly **passed** these unweighted clauses.  We do not use
the failed clause asserting constancy of `kappa_F`.

## 2. The two possible lattice values

Fix one reference flag `F_i` at height `u_i>1`.  In an arbitrary rational
Puiseux chart, use the notation

\[
 K_i,\qquad n_i=K_i u_i,\qquad
 e_i=\gcd\bigl(K_i,\{r<n_i:c_r\ne0\}\bigr).
\]

The lattice index strictly below the height and the effective coefficient
orbit order are

\[
 \kappa_i^-={K_i\over e_i},\qquad
 m_i={e_i\over\gcd(e_i,n_i)}.
\]

If the coefficient at height `u_i` is nonzero, the post-height gcd is
`gcd(e_i,n_i)` and the jump presentation has index

\[
 \kappa_i^+=m_i\kappa_i^-={K_i\over\gcd(e_i,n_i)}.
                                                        \tag{2.1}
\]

If the coefficient is zero, no new exponent enters the support and the
index remains `kappa_i^-`.  Thus the audited Q/jump/max value at the
transported flag on `f=a` is

\[
 \kappa_i(a)=
 \begin{cases}
 \kappa_i^+,&P_i(z)=a\text{ has a root }z\ne0,\\
 \kappa_i^-,&z=0\text{ is its only geometric root}.
 \end{cases}                                           \tag{2.2}
\]

Here `z=0` is equivalent to the covered coefficient `eta=0`; every
nonzero quotient point has nonzero covered lifts.  Formula (2.2) is also
valid when `m_i=1`, when the two displayed values coincide.  It is the
arbitrary-rational form of the reviewed Q/jump/max convention
(`dd09069b...`, review `3b8bd5c9...`).

Consequently

\[
 \kappa_i(a)\le\kappa_i^+\quad\hbox{for every }a,       \tag{2.3}
\]

and equality holds outside the single value `P_i(0)`.  Define the generic
baseline

\[
 b_i^+:=\kappa_i^+(u_i-1)>0.                            \tag{2.4}
\]

No cross-fibre invariance of the actual `kappa_i(a)` is asserted.

## 3. Actual cluster weight dominates the generic baseline

For `z in U_i(C)`, let `C(i,z)` be the direction cluster supplied by the
reviewed quotient bijection, on the fibre `a=P_i(z)` and with finite value
`b=Q_i(z)`.  Put

\[
 w_i(z):=L_{C(i,z)}
       =\sum_{P\in C(i,z)}\Lambda(P).                   \tag{3.1}
\]

### Lemma 3.1 (generic equality)

If `z!=0` and `P_i'(z)!=0`, then

\[
 w_i(z)=b_i^+.                                         \tag{3.2}
\]

Indeed, a nonzero quotient root has only nonzero covered lifts.  Since
`P_i'(z)!=0` and `d(eta^m)/deta!=0` at a nonzero lift, the covered residual
root is simple.  The simple-direction clause of repaired Proposition 7.3
then gives

```text
Lambda(P)=kappa_(F_i(P_i(z)))*(u_i-1)=kappa_i^+(u_i-1).
```

The direction cluster is the one root orbit counted by `z`, so this is
exactly (3.2).

### Lemma 3.2 (specialization inequality)

For every `z_0 in U_i(C)`,

\[
 w_i(z_0)\ge b_i^+.                                    \tag{3.3}
\]

To prove this, use the proper local tube already required in the repaired
proof of Proposition 7.3.  Isolate the punctures in `C(i,z_0)` by their
common strict Puiseux prefix and coefficient orbit, and take a small disc
`D` about `z_0`.  For a generic nearby value `a'` of the first coordinate,
the equation `P_i(z)=a'` has at least one root `z'` in `D`.  Choose `a'`
outside the discriminant and, when `z_0=0`, different from `P_i(0)`; then
`z'` is nonzero and simple.  Its covered direction has local degree
`b_i^+` by Lemma 3.1.

Conservation of local intersection number / degree in the proper finite
`g`-tube says that the degree of this one nearby point cannot exceed the
constant total degree `w_i(z_0)` of the tube.  Therefore (3.3) follows.
No sum over all nearby roots is taken: their `Q_i`-values may differ, so a
ramification-multiplicity factor would be unjustified and is unnecessary.

This is exactly the one-point specialization argument in the reviewed
general-direction part of Proposition 7.3, with the crucial correction that
the chosen nearby simple direction has the direction-specific nonzero value
`kappa_i^+`; no equality with the special vertex's `kappa_i(P_i(z_0))` is
asserted.

There is no conflict with the simple-direction formula at `z_0=0`.  If
`kappa_i^+>kappa_i^-`, then `m_i>1` and
`p(eta)=P_i(eta^{m_i})-P_i(0)` has covered root `eta=0` of multiplicity at
least `m_i`, so the simple clause does not assign it the low weight.  If
`m_i=1`, the two lattice values coincide.

In particular the Terra witness `K=e=2,n=3,P(z)=z` is absorbed correctly:
the special zero direction has the low vertex baseline `kappa^-*(u-1)`,
but its actual cluster weight is at least the generic high baseline
`kappa^+*(u-1)`.

## 4. Euler integral of the actual weights

Let

\[
 S_i=\{0\}\cup\{z:P_i'(z)=0\}.
\]

This is finite.  Lemma 3.1 says `w_i=b_i^+` on `U_i\S_i`, while Lemma
3.2 says `w_i(s)>=b_i^+` at every `s in S_i`.  Thus `w_i` is a
constructible integer-valued function and

\[
\begin{aligned}
 \int_{U_i}w_i\,d\chi_c
 &=b_i^+\chi_c(U_i\setminus S_i)+\sum_{s\in S_i}w_i(s)\\
 &=b_i^+(1-|S_i|)+\sum_{s\in S_i}w_i(s)\\
 &\ge b_i^+.                                           \tag{4.1}
\end{aligned}
\]

This is where integrating the actual weight differs from integrating the
variable baseline.  Compact Euler characteristic is not monotone for an
arbitrary nonnegative constructible function; (4.1) is valid because every
exceptional value is proved to jump **upward** from one common generic
value.

## 5. Global inequality

Put `N(a,b)=#Phi^(-1)(a,b)`.  The every-fibre degree theorem and simplicity
of affine Keller preimages give the pointwise identity

\[
 d-N(a,b)
 =\sum_{P\text{ at infinity on }f=a,\ g(P)=b}\Lambda(P).
                                                        \tag{5.1}
\]

The reviewed quotient bijection partitions the right side into the
clusters `C(i,z)`.  Therefore, as constructible functions on `A2`,

\[
 d-N=\sum_i(\varphi_i)_!w_i,                            \tag{5.2}
\]

where the pushforward sums `w_i(z)` over the finite geometric fibre of
`phi_i`.  No baseline and no `delta` are used in (5.2).

Euler-Fubini, Keller quasi-finiteness, and `chi_c(A2)=1` give

\[
 d-1
 =\int_{A2}(d-N)\,d\chi_c
 =\sum_i\int_{U_i}w_i\,d\chi_c
 \ge\sum_i b_i^+.                                      \tag{5.3}
\]

Now choose the original reference fibre to be any prescribed `f=a_0`.
For its transported reference flags, (2.3) gives

\[
 \kappa_{F_i}(\pi(F_i)-1)
 \le b_i^+.
\]

Combining with (5.3) proves `(C7.1*)` for the full set
`T_(a_0,cv)`.  Every omitted term is positive, so the inequality also holds
for any subset of pairwise distinct flags.  This is repaired Corollary 7.1.

## 6. Dependency and failure ledger

- The false inference identified by Terra is not repaired or reused:
  `kappa_i(a)` may vary between `kappa_i^-` and `kappa_i^+`.
- The theorem needs the **proper local-tube specialization** in Lemma 3.2.
  A merely pointwise invocation of Proposition 7.3 with the special
  `kappa_i(a)` is insufficient.
- The quotient transport `tau`, formal-deck/EW2 orbit bridge, centred value
  formulas, every-`z` realization, and no-duplication clauses were passed
  by the exact final delta gate `758c0226...` and are used only in those
  passed scopes.
- The proof imports every-fibre Proposition 5.8 by exact hash.  It is not
  inferred from Statement 3.14.
- Printed equation `(22)`, the literal per-puncture `delta_a`, and the
  failed fixed-weight `(22-cl)` remain unproved.  The present theorem is an
  inequality, which is all the later exit-budget consumers require.
- If hostile review confirms Lemmas 3.1--3.2 and the weighted pushforward,
  first-separation exit sets may use `(C7.1*)` once on their disjoint union.
  No nested literal `Y(F)` sum is restored.
