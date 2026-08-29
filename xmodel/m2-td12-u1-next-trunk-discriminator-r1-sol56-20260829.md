# (M=2, td=12), U1 first-trunk discriminator: exact charge (8) and a depth-(24) pure-power gate

Date: 2026-08-29  
Author: Sol 5.6 (Ultra)  
Status: sealed primary note; no canonical promotion in this file

## Result

For the reviewed U1 first trunk

\[
(\nu_F,\bar k_F,X_F,M_F,w_F)=(25,17,25,3,2/3),
\]

the non-arrival orbit (B) has **exact first-separation price**

\[
\lambda_{F,B}=8.
\]

The previously open alternative (9) cannot occur.  The reason is global but
local to this trunk: two different critical-value flags below the same
nearrow (B)-direction would each cost at least (X_F-\bar k_F=8), already
exceeding (td=12).  Hence all sheets in the (B)-cluster remain together
until their unique critical-value flag.  The exact descent integral then
forces normalized critical-value level (25), no ramification jump, and price
(25-17=8).

Consequently the clean next source discriminator is finite and explicit.  At
each of the first (24) successive \(\kappa_F\)-graded coefficient levels in
the (B)-direction, the selected child polynomial must be a pure power of one
linear factor.  In particular, if the first child polynomial has any two
distinct roots, the whole U1 row is impossible.

This condition is formally compatible with all pinned top-pattern,
semi-invariance, degree, and arrival-transport data.  It is **not** presently
known to be realizable by a polynomial Keller pair: the packets do not contain
the lower graded coefficients, or the coupled (J(f,g)=1) recurrences that
would determine them.

## Exact dependencies and hypotheses

The argument uses only the following reviewed source/packet inputs.

1. **The pinned U1 row.**  The unique (td=12,m=3), type-((2,3))
   source row has three pole packages ((a,b,\nu)=(1,2,3)).  In U1,
   (n\geq5), (n\equiv1,5\pmod 6), and the displayed first trunk is

   \[
   p_F=(t-A)^2(t-B),\qquad
   q_F=\eta(t-A)(t-B),\qquad t=\eta^{25},
   \]

   with (A=8u,B=9u,u\ne0), and

   \[
   D_F/i_F=X_F=25,\quad \bar k_F=17,
   \quad j=1,\quad \psi=2.
   \]

   This is the row in
   `m2-td12-u1-trunk-consumer-primary-grok46-20260829.md`, with the
   arithmetic corrections retained from its Opus hostile review.

2. **The (B)-direction is nearrow and finite.**  Its AF2 gap is
   (X_F-\bar k_F=8>0).  Proposition 6.6 and the repaired Section 7
   statements imply that every ray continuing through this direction is a
   finite ray and has a critical-value flag.

3. **Corrected Statement 9.3.**  For every critical-value flag (H)
   below this same direction,

   \[
   \kappa_H(\pi(H)-1)\geq X_F-\bar k_F=8.
   \]

4. **Actual-weight inequality (Corollary 7.1).**  Any finite collection
   of distinct critical-value flags may be inserted in

   \[
   td\geq1+\sum_H\kappa_H(\pi(H)-1).
   \]

   On this route the terminal witness has weight at least (psi=2), so a
   single (B)-flag has available budget at most (12-1-2=9).

5. **Reviewed exact descent law.**  For a branch in an extra direction,
   put

   \[
   \tau=\kappa_F(u-\pi(F)),\qquad
   N(\tau)=\deg p_{I(u)},\qquad
   \tau_0=\kappa_F(\pi(H)-\pi(F)).
   \]

   If the full (B)-multiplicity is (i=i_F), then

   \[
   D_F=\int_0^{\tau_0}N(\tau)\,d\tau,
   \qquad
   \Delta_H=
   \frac{\kappa_H}{\kappa_F}(\tau_0-\bar k_F).
   \]

   This is the different-model-reviewed law in the td8 first-extra-jet
   primary and its Fable hostile review.

No claim below uses the withdrawn pole-price inference from the earlier Opus
trunk review.  Pole entry has independently been proved to have price zero.

## 1. Full multiplicity bookkeeping

Write (i_G) for the full sheet index at the U1 merge and (i=i_F) at
the first trunk.  Transport of the arrival multiplicity gives

\[
2i=(6n)i_G,qquad\text{so}\qquad i=3ni_G.
\]

For the displayed direct pole entries, the pole top has full degree (4)
and its merge-arrival child has reduced multiplicity (2).  Hence

\[
2i_G=4,qquad i_G=2,qquad i=6n.
\]

The proof of the exact price needs only (i>0); (i=6n) is useful when
writing the coefficient gate for the displayed direct-entry family.

## 2. There is exactly one critical-value flag below (B)

Every such flag (H) has weight at least (8) by corrected Statement 9.3.
If two distinct flags (H_1,H_2) occurred below (B), Corollary 7.1 would
give

\[
12=td\geq1+\operatorname{wt}(H_1)+\operatorname{wt}(H_2)
\geq1+8+8=17,
\]

which is impossible.  At least one exists by the finite-ray statement, so
there is exactly one; call it (H).

This also prohibits loss of sheets before (H).  Indeed, if two sheets in
the (B)-cluster separate while (d_f>0), the two resulting tree rays cannot
remerge.  Both rays remain finite, so each acquires its own critical-value
flag after the separation.  Those flags are distinct, contradicting the
preceding paragraph.  Therefore

\[
N(\tau)=i\qquad (0<\tau<\tau_0).
\]

This step is why the tempting charge-(9) defect partitions are spurious in
the actual (td=12) route: every positive defect would be caused by a split,
and the departed finite cluster contributes another weight-(geq8) flag.

## 3. Exact price

The full order is (D_F=25i).  Since the cluster size is constantly (i),
the exact descent integral is

\[
25i=D_F=\int_0^{\tau_0}i\,d\tau=i\tau_0,
\]

and hence

\[
\tau_0=25.
\]

Put (r=\kappa_H/\kappa_F\in\mathbb N_{>0}).  The exact weight is

\[
\Delta_H=r(\tau_0-\bar k_F)=r(25-17)=8r.
\]

Already with this one flag, Corollary 7.1 gives

\[
12\geq1+8r.
\]

Thus (r=1).  (Adding the distinct terminal witness of weight at least
(2) sharpens the available local budget to (9), but is not needed to
exclude (r\geq2).)  Therefore

\[
\boxed{\lambda_{F,B}=\Delta_H=8.}
\]

In particular, there is neither a characteristic-denominator jump nor a
contact split before the unique critical-value flag.

## 4. The finite coefficient discriminator

Let (c^{25}=B).  Expand the full (f)-top at (F) in
\(\kappa_F\)-graded pieces (P_k(\eta)).  The first child polynomial in the
direction (c) is

\[
C_1(z)=\sum_{k=0}^{i}
   [\,(\eta-c)^{i-k}\,]P_k(\eta)\;z^{i-k}.
\]

Since no sheets may separate at the first coefficient level,

\[
C_1(z)=\gamma_1(z-\alpha_1)^i
\]

for some (gamma_1\ne0).  Equivalently,

\[
\deg\gcd(C_1,C_1')=i-1.
\]

If

\[
C_1(z)=a_0z^i+a_1z^{i-1}+\cdots+a_i,qquad a_0\ne0,
\]

the same test is the finite list

\[
a_k=a_0\binom{i}{k}
       \left(\frac{a_1}{ia_0}\right)^k,
\qquad 2\leq k\leq i.
\]

Recenter at the unique root and repeat.  Because the critical-value level is

\[
\tau_0=25,
\]

the child polynomials at normalized levels (1,2,\ldots,24) must all be
pure (i)-th powers, and the denominator must remain (\kappa_F).  A split
at level (25) is at the critical-value flag itself and is not excluded by
this argument.  Therefore this is a finite depth-(24) recursive
gcd/subdiscriminant gate, with an immediate rejection on any earlier
characteristic-denominator jump.  The first failure is an exact
contradiction to (td=12); no reviewer round or numerical estimate is needed
to use it provisionally.

For the direct-entry family (i=6n), so the first test is

\[
\deg\gcd(C_1,C_1')=6n-1.
\]

## 5. Why the pinned top data do not already fail the gate

The semi-invariance residues do not obstruct a pure-power child.  Here

\[
N_1\equiv-\bar k_F\equiv8\pmod{25},
\qquad 8^{-1}\equiv22\pmod{25},
\]

and, since (D_F=25i\equiv0\pmod{25}), the (k)-th graded piece has
residue

\[
e_k\equiv22k\pmod{25}.
\]

Thus (e_k\equiv k e_1\), exactly the residue progression of the
coefficients of a pure power whose shift has residue (e_1=22).

There is also enough formal coefficient freedom to preserve the known
arrival child while choosing the first (B)-child arbitrarily within these
weight lines.  Put (T=\eta^{25}), choose (a^{25}=A), and for
(1\leq k\leq i) set

\[
P_k(\eta)=
\eta^{e_k}(T-A)^{2i-k}(T-B)^{i-k}R_k(T),
\]

where (R_k) is a polynomial of degree at most one.  The arrival diagonal at
(a) is a nonzero scalar multiple of (R_k(A)), whereas the extra-branch
diagonal at (c) is a nonzero scalar multiple of (R_k(B)).  Since
(A\ne B), linear interpolation chooses these two values independently.
The vanishing orders are exactly the required (2i-k) and (i-k), and the
semi-invariance residue is (e_k).

This interpolation does not violate the evident degree cap.  Taking
(0\leq e_k\leq24),

\[
\deg P_k\leq e_k+25(3i-2k+1)\leq75i
\qquad(k\geq1),
\]

with the closest case (k=1) equal to (75i-3).  The full top degree is
(75i).

In particular, take the desired (B)-diagonal coefficients to be those of
(\gamma(z-\alpha)^i), with (alpha) in residue line (22).  The displayed
interpolation realizes the first pure-power condition while retaining all
known arrival diagonals.  Repeating a common formal Puiseux coefficient for
all (i) sheets through level (24) gives a formal contact tree satisfying
the exact-price geometry.

This is only **formal local compatibility**.  It does not construct
polynomials (f,g\in\mathbb C[x,y]), does not solve the lower-term Keller
recurrences, and does not prove that the source map realizes these choices.

## 6. Smallest missing datum and cheapest next test

The smallest currently missing source datum is the first (B)-child
coefficient vector

\[
\bigl([\,(\eta-c)^{i-k}\,]P_k\bigr)_{k=1}^{i},
\]

or an equivalent Keller/transport recurrence that determines it.

The cheapest decisive test is:

1. extract that vector from the source polynomial identities;
2. form (C_1);
3. compute (\gcd(C_1,C_1')), or check the displayed binomial identities;
4. kill the U1 row immediately unless the gcd has degree (i-1);
5. if it passes, recenter and repeat through normalized level (24), also
   rejecting any characteristic-denominator increase before level (25).

The exact lambda computation is now closed: passing all these tests does not
reduce the price below (8), and failing any one of them forces at least two
weight-(geq8) critical-value flags and contradicts (td=12).

## 7. Review risks

1. **Finite-ray inheritance.**  The no-split proof needs Proposition 6.6 and
   the repaired Section 7 statement in the quantified form “every ray through
   the nearrow (B)-flag is finite and reaches a critical-value flag.”  If a
   source formulation only supplies one selected continuation, the proof must
   be supplemented for departed sheets.

2. **Distinctness after separation.**  The proof uses the tree fact that two
   rays separated while (d_f>0) cannot share their later (d_f=0) flag.
   This is standard from the flag-tree order, but should be cited explicitly
   on canonical promotion.

3. **Actual weights, not an ownership convention.**  The contradiction with
   two flags uses Corollary 7.1 directly, so it is independent of how the
   repaired first-separation ledger assigns owners.  This is deliberate.

4. **Endpoint convention.**  Purity is required at levels (1\) through
   (24).  A split exactly at normalized level (25) occurs at the unique
   critical-value flag and need not create a second critical-value flag.

5. **Formal versus polynomial realization.**  The interpolation argument
   proves freedom under the printed top/vanishing/weight/degree constraints
   only.  Constant-Jacobian lower recurrences may eliminate that freedom; no
   such recurrence was present in the pinned inputs.

## Dependency hashes

- `xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md`  
  SHA-256: `599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271`
- `xmodel/m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md`  
  SHA-256: `91b36515950f038d08a444df16f9c09ee9763adb7950d46e9c50e43451f25c0f`
- `xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md`  
  SHA-256: `991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508`
- `xmodel/m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md`  
  SHA-256: `ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370`
- `xmodel/m2-td12-pole-entry-price-r1-sol56-20260829.md`  
  SHA-256: `8fd4d1d01bcb082b6f7dfd0ccb91cee072a1e7e2fdb6a319c099075b0b39a9de`
- `xmodel/sigray-section7-full-independent-audit-sol-ultra-20260828.md`  
  SHA-256: `0159cdf18f9ad1c986677d4631916dbbef0b5310829958f6dac192eab2795a31`
- `xmodel/sigray-section9-source-audit-sol-ultra-20260828.md`  
  SHA-256: `2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933`

## Seal

Body SHA-256 (all bytes before this `## Seal` heading): `b25217e9b733efcc28d263c9df057d6ebcac61976002dd1c815e8063591caaae`
