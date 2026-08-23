# The polar defect and the branch conductor: an exact different/contact ledger

**Date:** 2026-08-23

**Characteristic:** \(0\).

**Accepted as EXACT/PROVED:** `xmodel/sol-pc.md` and
`xmodel/sol-ucda.md` in full, `xmodel/sol-rpmc.md` Sections 0--4, and
`xmodel/sol-unify.md` Section 1.  The formal insertion tower is used only at
its stated H1 arithmetic tier.

## 0. Verdict

\[
 \boxed{\textbf{INDEPENDENT AS TERMINAL BOUNDS, WITH AN EXACT
 DIFFERENT/CONTACT IDENTITY.}}
 \tag{0.1}
\]

For one normalization branch \(\gamma\) of a general \(f\)-fiber, let
\(m_\gamma=\operatorname{ord}_\gamma z\), let \(p_\gamma\) be the pole
order of \(g\), and let \(I_\gamma\) be the intersection of \(\gamma\)
with all the other local branches of that projective fiber germ.  Then

\[
 \boxed{
 \Delta_\gamma=p_\gamma,
 \qquad
 2\delta(\gamma)+I_\gamma
   =(d-3)m_\gamma+p_\gamma+1.}
 \tag{0.2}
\]

Here \(\Delta_\gamma\) denotes the branch summand in the positive polar
defect; \(\Delta_P\) is the sum of these summands over the pole branches
above the proper root \(P\).  On residue A,

\[
 m_\gamma=\kappa_i,\qquad p_\gamma=3,\qquad
 \boxed{\Delta_\gamma=3,\quad
 2\delta(P_i)+I_i=(d-3)\kappa_i+4.}
 \tag{0.3}
\]

Thus the raw polar order does contain the branch different, but it also
contains the entire contact \(I_i\).  After the baseline
\((d-2)m_\gamma\) is removed, the conductor and contact terms cancel down
to the fixed pole order \(3\).  Local theory supplies no identity in
\(\delta(P_i)\) or the gcd indices \(\nu_j\) alone: the exact identity
also requires the ambient degree and the contact term.

The exact H1 \(\ell=0,\nu=2\) tower has

\[
 \kappa_i(r)=42\,2^r,\qquad
 \delta(P_i(r))\ge 42\,2^r-1,\qquad
 \Delta^{\mathrm{H1}}_\gamma(r)=3
 \tag{0.4}
\]

at the formal residue-A pole-mass tier.  The last equality means that every
Keller algebraization of that tower would have branch polar defect \(3\);
polynomial/Keller algebraization of the tower remains **UNKNOWN**.  The
two-leaf residue-A polar inventory remains \(3+3=6\).

There is also an actual Keller separator: a generalized Hénon tower can
have \(\kappa_r=42\,2^r\),

\[
 \Delta_\infty=1,\qquad
 \delta_\infty=\frac{(\kappa_r-1)(\kappa_r-2)}2\longrightarrow\infty.
 \tag{0.5}
\]

It is an automorphism and is not orbitwise degree-minimal, so it is not a
residue-A counterexample.  It nevertheless proves that polynomial origin
and \(J\in k^*\), even at the local germ level, impose no universal growth
coupling between polar defect and conductor.  A coupling restricted to
degree-minimal nonautomorphic residue-A Keller germs would be a new
Keller theorem; none is proved here.

---

## 1. One coordinate system for both invariants

Work at the residue-A point \([1:0:0]\) in the chart

\[
 z=Z/X,\qquad w=Y/X,\qquad
 A_\lambda(w,z)=F(1,w,z)-\lambda z^d.
 \tag{1.1}
\]

After subtracting the tangent, a primitive branch \(\gamma\) has

\[
 z=t^m,\qquad \operatorname{ord}_t w>m,\qquad m=\kappa_i.
 \tag{1.2}
\]

The polar in this chart is \(F_Y=A_{\lambda,w}\).  This is the symmetric
version of the \(F_X=\Phi_u\) polar in `sol-pc.md`; exchanging \(X,Y\)
turns one notation into the other.

### 1.1 Puiseux/approximate-root conductor

Let \(b_1<\cdots<b_s\) be the local characteristic exponents after the
tangent is subtracted, and put

\[
 e_0=m=\kappa_i,\qquad
 e_j=\gcd(e_{j-1},b_j),\qquad
 \nu_j=\frac{e_{j-1}}{e_j}.
 \tag{1.3}
\]

Then

\[
 e_j=\frac{\kappa_i}{\nu_1\cdots\nu_j},\qquad
 \prod_{j=1}^s\nu_j=\kappa_i.
 \tag{1.4}
\]

The classical branch-conductor formula is

\[
 \boxed{
 c(\gamma)=2\delta(\gamma)
 =\sum_{j=1}^s(e_{j-1}-e_j)b_j-m+1.}
 \tag{1.5}
\]

Equivalently, if \(\bar\beta_0=m,\bar\beta_1,\ldots,\bar\beta_s\)
are the approximate-root semigroup generators, then

\[
 \boxed{
 c(\gamma)=\sum_{j=1}^s(\nu_j-1)\bar\beta_j-m+1.}
 \tag{1.6}
\]

Consequently the indices \(\nu_j\) determine the multiplicity
\(m=\kappa_i\), but do **not** determine \(\delta(\gamma)\): the
characteristic exponents \(b_j\), equivalently the generators
\(\bar\beta_j\), are also required.  The accepted multiplicity bound is

\[
 \delta(\gamma)\ge m-1,\qquad c(\gamma)\ge2(m-1).
 \tag{1.7}
\]

### 1.2 The local different and the contact compensator (**PROVED**)

Factor the reduced germ

\[
 A_\lambda=U\prod_\eta A_\eta
 \tag{1.8}
\]

and define

\[
 I_\gamma=\sum_{\eta\ne\gamma}i(A_\gamma,A_\eta).
 \tag{1.9}
\]

For the irreducible branch \(A_\gamma=0\), the plane-branch different
formula gives

\[
 \operatorname{ord}_\gamma (A_\gamma)_w
 =c(\gamma)+\operatorname{ord}_t(dz/dt)
 =c(\gamma)+m-1.
 \tag{1.10}
\]

Restricting the derivative of (1.8) to \(\gamma\) adds the other branch
intersections.  Hence

\[
 \boxed{
 \operatorname{ord}_\gamma F_Y
 =c(\gamma)+m-1+I_\gamma
 =2\delta(\gamma)+m-1+I_\gamma.}
 \tag{1.11}
\]

Combining (1.5) with (1.11) also gives the common approximate-root form

\[
 \operatorname{ord}_\gamma F_Y
 =\sum_{j=1}^s(e_{j-1}-e_j)b_j+I_\gamma
 =\sum_{j=1}^s(\nu_j-1)\bar\beta_j+I_\gamma.
 \tag{1.12}
\]

Consequently the polar defect itself is

\[
 \boxed{
 \Delta_\gamma
 =\left[
 \sum_{j=1}^s(\nu_j-1)\bar\beta_j+I_\gamma
 -(d-2)m_\gamma
 \right]_+,\qquad
 \Delta_P=\sum_{\gamma\mid P}\Delta_\gamma.}
 \tag{1.13}
\]

This is the exact place at which the conductor enters the polar order.
It is linear in the approximate-root conductor contributions only after
the semigroup generators and the contact compensator are supplied; it is
not a function of the indices \(\nu_j\) alone.

### 1.3 Constant Jacobian and the normalized polar excess (**PROVED**)

Suppose \(J(f,g)=j\in k^*\), \(\operatorname{ord}_t x=-m\), and
\(\operatorname{ord}_t g=-p\).  Along \(f=\lambda\),

\[
 g'=-j\frac{x'}{f_y},\qquad
 \operatorname{ord}_t f_y=p-m.
 \tag{1.14}
\]

Homogeneity, \(F_Y=z^{d-1}f_y\), then gives

\[
 \boxed{
 \operatorname{ord}_\gamma F_Y=(d-2)m+p.}
 \tag{1.15}
\]

For residue A, (1.14) is exactly the accepted identity
\(\operatorname{ord}_t f_y=3-\kappa_i\).  Equating (1.11) and (1.15)
proves

\[
 \boxed{
 c(\gamma)+I_\gamma=(d-3)m+p+1.}
 \tag{1.16}
\]

In the \(Y\ne0\) convention of sol-pc.md, the symmetric statement is

\[
 \boxed{
 \operatorname{ord}_\gamma F_X=(d-2)m_\gamma+p_\gamma.}
 \tag{1.17}
\]

The branch polar summand is therefore

\[
\begin{aligned}
 \Delta_\gamma
 &=\operatorname{ord}_\gamma F_Y-(d-2)m\\
 &=c(\gamma)+I_\gamma-(d-3)m-1\\
 &=p.
\end{aligned}
\tag{1.18}
\]

There is no positive-part ambiguity on a pole branch.  In the canonical
differential notation this is the same calculation:

\[
 \omega=dg/j,\qquad
 \operatorname{ord}_\gamma\omega=-p-1,\qquad
 \Delta_\gamma=-\operatorname{ord}_\gamma\omega-1=p.
 \tag{1.19}
\]

For all branches over a proper root \(P\), including finite \(g\)-ends,
let \(r_P\) be the number of branches and let
\(\delta(A_{\lambda,P})\) be the delta-invariant of the whole reduced
local fiber germ.  Summing (1.11) and using the signed polar ledger gives

\[
 \boxed{
 \Delta_P-K_P
 =2\delta(A_{\lambda,P})-(d-3)\alpha\mu-r_P.}
 \tag{1.20}
\]

Thus even the rootwise identity contains the finite-end compensator
\(K_P\).  Formula (1.20) concerns the delta-invariant of the entire
multibranch germ; G2 concerns the individual branch invariant
\(\delta(P_i)\).

---

## 2. Filed residue-A arithmetic

The characteristic ladder is

\[
 1\xrightarrow{7}7\xrightarrow{3}21\xrightarrow{2}42,\qquad
 (e_0,e_1,e_2,e_3)=(42,6,2,1).
 \tag{2.1}
\]

The local characteristic exponents and approximate-root generators are

\[
 (b_1,b_2,b_3)=(54,74,79),\qquad
 (\bar\beta_0,\bar\beta_1,\bar\beta_2,\bar\beta_3)
 =(42,54,398,1199).
 \tag{2.2}
\]

Both conductor formulas give the banked value:

\[
\begin{aligned}
 c(P_i)
 &=36\cdot54+4\cdot74+1\cdot79-42+1\\
 &=1944+296+79-41=2278,\\
 \delta(P_i)&=1139,
\end{aligned}
\tag{2.3}
\]

and equivalently

\[
 (7-1)54+(3-1)398+(2-1)1199-42+1=2278.
 \tag{2.4}
\]

Here \(d=168\), \(m=\kappa_i=42\), and \(p=3\).  The other local
branches meet one pole branch with total contact

\[
 I_i=(P_1\cdot P_2)+(P_i\cdot B)=2388+2268=4656.
 \tag{2.5}
\]

In the arithmetic below, \(\Delta_{P_i}\) is shorthand for the branch
summand \(\Delta_{\gamma_i}\), not the proper-root sum \(\Delta_P\).

The different/polar ledger closes with no slack:

\[
\begin{aligned}
 \operatorname{ord}_{P_i}F_Y
 &=2278+42-1+4656=6975,\\
 (d-2)m&=166\cdot42=6972,\\
 \Delta_{P_i}&=6975-6972=3,
\end{aligned}
\tag{2.6}
\]

or, in its shortest form,

\[
 2278+4656=(168-3)42+4=6934.
 \tag{2.7}
\]

There are two pole leaves, so their polar allocation is

\[
 \Delta_P=3+3=6=\operatorname{td},\qquad
 \mathcal E_P=\frac{6}{2\cdot3}=1.
 \tag{2.8}
\]

At this Y-side root, \(\alpha\mu=126\), hence \(\mu=63\), while
\(B=84\).  Therefore the filed root has the exact DIR ratio

\[
 \frac{B\Delta_P}{\alpha\beta\mu}
 =\frac{84\cdot6}{6\cdot63}=\frac43.
 \tag{2.9}
\]

Thus `DIR(4/3)` is equality on this root.  This number has no dependence
on the much larger branch conductor \(2278\).  The passport
\(\{2,3\}\) and \(w=2\) likewise do not occur in (1.5), (1.16), or
(2.9), except that the terminal leaf index happens to be \(2\).  The
hidden factors \(7,3\) enter the conductor through (2.3)--(2.4) but are
cancelled from the polar excess by (2.6).

---

## 3. The formal \(\ell=0,\nu=2\) insertion tower

At H1 arithmetic tier, insert \(r\) factors \(2\).  Then

\[
 \kappa_i(r)=42\,2^r,\qquad
 c(P_i(r))\ge2(42\,2^r-1),\qquad
 \delta(P_i(r))\ge42\,2^r-1.
 \tag{3.1}
\]

The H1 data do not specify the new local exponents \(b_j(r)\), so an
exact value of \(\delta(P_i(r))\) beyond the lower bound (3.1) is **NOT
DETERMINED**.  Claiming a particular conductor recursion from the indices
\(\nu_j\) alone would be false.

The insertion preserves \(w=2\), the two entries
\((a_P,b_P,\nu_P)=(1,1,2)\), and the pole masses.  Hence the formal pole
ledger is

\[
 \boxed{
 \Delta^{\mathrm{H1}}_{\gamma_i}(r)=3,\qquad
 \Delta^{\mathrm{H1}}_{\gamma_1}(r)
 +\Delta^{\mathrm{H1}}_{\gamma_2}(r)=6}
 \tag{3.2}
\]

for every \(r\).  If a stage algebraizes to a Keller pair of degree
\(d_r\), its exact local equations must be

\[
\begin{aligned}
 \operatorname{ord}_{P_i}F_{\perp,r}
   &=(d_r-2)42\,2^r+3,\\
 2\delta(P_i(r))+I_i(r)
   &=(d_r-3)42\,2^r+4.
\end{aligned}
\tag{3.3}
\]

Equation (3.3) is a necessary Keller algebraization condition, not a proof
that such an algebraization exists.  It shows exactly how conductor growth
can be absorbed: by the growing ambient baseline and the contact term,
not by growth of the formal pole mass
\(\Delta^{\mathrm{H1}}_{\gamma_i}\).

Therefore

\[
 \boxed{
 \kappa_i\to\infty\ \not\Longrightarrow\
 \Delta^{\mathrm{H1}}_{\gamma_i}\to\infty}
 \tag{3.4}
\]

at the accepted formal residue-A tier, and the implication already fails
for actual Keller germs by the Hénon family below.

---

## 4. What one wall can imply

1. **DIR does not imply A-SCALE through these local invariants.**  DIR
   sees the normalized pole order, not the uncancelled branch different.
   The formal tower keeps the former equal to \(3\) while \(\kappa_i\)
   and the conductor lower bound diverge.  This defeats the proposed
   monotone implication.  A set-theoretic nonimplication on actual
   noninvertible polynomial residue-A maps is **UNKNOWN**.

2. **A-SCALE implies a residue-A DIR bound, but only by a coarse finite
   scale argument.**  If **CONJECTURE A-SCALE** gives \(B\le B_A\), then
   \(\Delta_P\le\operatorname{td}=6=\alpha\beta\) and \(\mu\ge1\) give

   \[
    \Delta_P\le B_A\alpha\beta\frac{\mu}{B}.
    \tag{4.1}
   \]

   Thus A-SCALE implies `DIR(B_A)` on the fixed residue-A inventory.  This
   is not a polar/conductor theorem; it is the tautological consequence of
   bounding the entire degree scale.

3. No bound on the product \(\prod\nu_j=\kappa_i\) alone controls
   \(\Delta_P\) in the general G5 problem, and no DIR bound controls the
   number of internal \(\nu_j\)'s.  The useful terminal directions remain
   different.

---

## 5. The two decoys

### 5.1 Hénon: actual Keller separation

For a generalized Hénon coordinate of degree \(d=\kappa\), the general
coordinate fiber is rational with one branch at infinity.  Its other
coordinate has pole order one.  Hence

\[
 I=0,\qquad
 c=(\kappa-1)(\kappa-2),\qquad
 \Delta=1.
 \tag{5.1}
\]

The exact bridge (1.16) becomes

\[
 (\kappa-1)(\kappa-2)=(\kappa-3)\kappa+2.
 \tag{5.2}
\]

Thus Hénon does not violate the bridge; it proves that the bridge permits
bounded polar defect and unbounded conductor under \(J=1\).  Orbitwise
degree minimization removes the tower and returns the identity pair.  The
conductor is therefore not an automorphism-orbit invariant.

### 5.2 Class-kill: the residual Jacobian curve

For

\[
 f=x^d+y,\qquad g=x^e+y^{e-1},
 \tag{5.3}
\]

the general \(f\)-fiber is rational with one branch at infinity and

\[
 m=d,\qquad I=0,\qquad
 c=(d-1)(d-2),\qquad
 \text{intrinsic polar excess}=1.
 \tag{5.4}
\]

Again the different identity closes:

\[
 (d-1)(d-2)-(d-3)d-1=1.
 \tag{5.5}
\]

But this pair is not Keller.  Its intersection defect is
\(d(e-1)\), because the residual-Jacobian correction is
\(de-d-1\).  Thus the pure-minor identity, not either classical local
invariant, excludes this decoy.

The mechanisms are orthogonal:

\[
\begin{array}{c|c|c}
 &\text{H\'enon tower}&\text{class-kill family}\\ \hline
 J\in k^*&\text{yes}&\text{no}\\
 \text{intrinsic polar excess}&1&1\\
 \text{conductor}&\to\infty&\to\infty\\
 \text{excluded by}&\text{orbit minimality}&\text{pure Jacobian support}
\end{array}
\tag{5.6}
\]

Neither \(\Delta\) nor \(\delta\) by itself excludes both.

---

## 6. No-decoy keystone

Rearranging (1.16) gives the exact contact-deficit invariant

\[
 \boxed{
 \Theta_\gamma:=(d-3)m_\gamma-I_\gamma
 =c(\gamma)-\Delta_\gamma-1.}
 \tag{6.1}
\]

On residue A,

\[
 \Theta_i=c(P_i)-4=2\delta(P_i)-4.
 \tag{6.2}
\]

Thus a uniform bound on \(\Theta_i\) would bound the conductor and hence
\(\kappa_i\).  It is not a new coupling: because
\(\Delta_{P_i}=3\) identically, bounding \(\Theta_i\) is exactly the
missing upper-conductor statement in different notation.

For clarity, the possible restricted theorem is:

> **CONJECTURE CONTACT-DEFICIT.**  There is a constant \(K_A\) such that
> every orbitwise degree-minimal, nonautomorphic residue-A Keller pair
> satisfies
> \[
>    (d-3)\kappa_i-I_i\le K_A.
> \tag{CD}
> \]

By (6.2), **CONJECTURE CONTACT-DEFICIT** is equivalent to a uniform upper
bound on \(c(P_i)\), and directly gives
\(\kappa_i\le\lfloor(K_A+4)/2\rfloor+1\).  This is the denominator form
of the G2 bound.  Under the question's stated residue-A identification of
that bound with A-SCALE, it then gives a residue-A DIR bound by (4.1).
From the displayed inequality \(\kappa_i\le2B\) alone, a bound on
\(\kappa_i\) would not conversely bound \(B\); that equivalence must be
part of the G2 dictionary.  CONTACT-DEFICIT has no proved support beyond
these reformulations.  Its degree-minimal and Keller hypotheses exclude
the Hénon and class-kill decoys respectively; the invariant itself
supplies no common exclusion mechanism.

Consequently there is no proved single no-decoy local rigidity statement.
The actual exact bridge is (1.16), and it exhibits rather than removes the
free compensator \(I_i\).  Hénon proves that no unrestricted
constant-Jacobian coupling can remove it.  Whether degree-minimal
noninvertible residue-A germs satisfy an additional contact-deficit bound
is precisely a new form of the G2 wall, not a merger of G2 with DIR.

\[
 \boxed{
 \begin{gathered}
 \textbf{Terminal verdict: INDEPENDENT.}\\
 \Delta_{P_i}=3\ \text{measures the pole of }g;\qquad
 2\delta(P_i)\ \text{measures the branch different}.\\
 \text{Their exact common ledger contains the uncontrolled contact }I_i.
 \end{gathered}}
 \tag{6.3}
\]
