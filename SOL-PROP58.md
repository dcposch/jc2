# Proposition 5.8: the pole-mass identity on every fiber

## Verdict

Let

\[
\mathcal F=(f,g):\mathbf A^2_{\mathbf C}\longrightarrow \mathbf A^2_{\mathbf C},
\qquad J(f,g)\in\mathbf C^*,
\]

and put \(d=\operatorname{td}(f,g)=[\mathbf C(x,y):\mathbf C(f,g)]\).
With Sigray's notation (and the corrections already recorded in
`SIGRAY-AUDIT.md`), the assertion is

\[
\boxed{
d=\sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F)
 =\sum_{F\in T_{a,\mathrm{pole}}}
   \frac{D_{g,F}\deg p_F}{\nu_F}
\quad\text{for every }a\in\mathbf C . }
\tag{P5.8}
\]

This assertion is true. The relative pole-divisor argument has two distinct
parts:

1. Its horizontal part is finite flat (in fact over all of
   \(\mathbf P^1_f\)) and has rank \(d\). On a nonempty open set of the
   \(f\)-line, its local intersection lengths are exactly Sigray's
   \(\Lambda(F)\)'s.
2. Flatness alone does **not** imply the result on a special fiber. There is
   an exact specialization defect, supported on boundary components on
   which \(f\) has a finite constant value and \(g\) is nonconstant. For a
   Keller map those components are excluded by Nguyen Van Chau's theorem on
   exceptional value curves. Hence the defect is zero for every \(a\).

Thus the proof does not need cross-fiber identification of individual
Eggers--Wall vertices, nor invariance of \(\nu_F\) under the maps
\(M_{a,b}\).

The degree-one case is immediate (and cannot be a normalized
counterexample), so the external source used below may harmlessly be read
under its standing assumption \(\max(\deg f,\deg g)>1\).

## 1. What is and is not proved in the cited thesis pages

Write \(R_a=f^{-1}(a)\), and let \(\overline R_a\) be the disjoint smooth
compactification (equivalently, the normalization of the projective closure
of each component). For a puncture
\(P\in\overline R_a\setminus R_a\), let

\[
\Lambda(P)=\operatorname{ord}_P(g)_\infty
\]

when \(P\) is a pole of \(g\).

These are Notation 1.4 (printed pp. 5--6) and Notation 1.5 (p. 6).
The leading data \(d_{h,F},p_{h,F}\) are defined in Notation 3.10 (p. 13),
\(D_{h,F}=\kappa_Fd_{h,F}\) in Notation 3.11 (pp. 13--14), and \(\nu_F\)
in Notation 3.4 (p. 12). The pole-vertex set is Notation 5.2 (p. 25).
Finally, \(\operatorname{td}\) is Definition 5.1 (p. 28); its
identification with the function-field degree appears in the introduction
(p. 5).

The following part is already present in
[`refs/sigray_full.pdf`](refs/sigray_full.pdf):

- Proposition 5.5, formula (18), printed pp. 26--27, characterizes the
  \(g\)-poles and computes \(\Lambda(P)\) from the pole vertex above \(P\).
- Proposition 5.6, formula (19), printed p. 27, groups all punctures
  represented by a pole vertex \(F\):

  \[
  \Lambda(F):=\frac{D_{g,F}\deg p_F}{\nu_F}
  =\sum_{\substack{P\in\overline R_a\setminus R_a\\
                    F=I_P(\pi(F))}}
    \Lambda(P).
  \tag{1}
  \]

  The root-of-unity orbit count in this formula uses the corrected reading
  of Statement 3.18, namely \(F*(\varepsilon c)\), and the simplicity and
  no-further-vertex conclusions in Proposition 5.3(v),(ix). These are the
  corrections and implicit inputs already itemized in
  `SIGRAY-AUDIT.md`; they do not affect (1).
- Proposition 5.7, printed pp. 27--28, proves
  \(\Lambda(F)\geq\beta\) for type \((\alpha,\beta)\).
- Proposition 5.8, formula (20), is stated on printed p. 28 with the words
  "For any \(a\in\mathbf C\)," but no proof follows: Section 6 begins on
  the next line.

Consequently, Propositions 5.5--5.6 reduce Proposition 5.8 exactly to

\[
d=\deg\bigl(g:\overline R_a\to\mathbf P^1\bigr)
 =\sum_{P:g(P)=\infty}\operatorname{ord}_P(g)_\infty
\quad\text{for every }a.
\tag{2}
\]

The first equality in (2), not the local formula (1), is the missing step.
Here and below, the degree of \(g\) on \(\overline R_a\) means the sum of
the degrees on the components of this disjoint smooth compactification.

For clarity, the local Sigray input is used with the following audit
corrections. On the fiber \(f=a\), \(p_F,d_F\) mean
\(p_{f-a,F},d_{f-a,F}\). Statement 3.15's zero/pole labels are swapped;
Proposition 5.5's displayed formula (18) is correct after that repair,
despite dropped \(g\)-subscripts in its proof. Statement 3.18 reads
\(F*(\varepsilon c)\). The integer \(D_{h,F}\) uses the canonical
jump/maximal-presentation value of \(\kappa_F\) forced by corrected
Statement 3.8. Proposition 5.3(ii),(viii) has its ratio inverted in print;
the correct formula is
\(d_{g,F}=(k_g/k_f)d_F=(\beta/\alpha)d_F\). The repaired \(q\)-half of
Proposition 5.4 underlies Statement 5.2(ii), Proposition 5.7, and table
(23). Finally, Proposition 5.1's gap at finite nonzero asymptotic
\(g\)-values is irrelevant here, because only actual \(g\)-poles enter.

Source-location correction: table (23) is not on pp. 26--30. It is in
Proposition 9.1 on printed p. 46. It lists the possible *individual* pole
data with \(\Lambda(F)\leq6\). The first of its two rows labelled "6" is
row 5, as the proof on p. 47 explicitly confirms.

## 2. A simultaneous resolution

Extend \((f,g)\) to the rational map

\[
\mathbf P^2\dashrightarrow \mathbf P^1_f\times\mathbf P^1_g.
\]

All indeterminacy lies on the line at infinity. Resolve it, and make further
boundary blowups if needed, to obtain a smooth projective surface \(X\), an
open immersion \(\mathbf A^2\subset X\), and morphisms

\[
p=\overline f:X\to\mathbf P^1_f,
\qquad
q=\overline g:X\to\mathbf P^1_g.
\]

Let \(D=X\setminus\mathbf A^2\) and
\(\Phi=(p,q):X\to\mathbf P^1\times\mathbf P^1\). Since
\(J(f,g)\neq0\), \(f,g\) are algebraically independent, so \(\Phi\) is
generically finite. Its degree is \(d\): a generic target point avoids the
curve \(\Phi(D)\), and its inverse image is the generic affine inverse image
used to define \(\operatorname{td}(f,g)\).

Put

\[
Q_\infty:=q^*(\infty).
\]

This is an effective Cartier divisor supported on \(D\). Decompose it,
with its divisor multiplicities, as

\[
Q_\infty=H+Q_{\mathrm v},
\tag{3}
\]

where a component belongs to \(H\) precisely when its restriction under
\(p\) is nonconstant, and belongs to \(Q_{\mathrm v}\) when \(p\) is
constant on it. We call \(H\) the horizontal pole divisor of \(g\) relative
to \(f\).

## 3. The horizontal pole divisor is finite flat of rank \(d\)

### Lemma 3.1

The map

\[
p|_H:H\longrightarrow\mathbf P^1_f
\]

is finite flat of rank \(d\).

### Proof

Every irreducible component of the support of \(H\) is a projective curve
on which \(p\) is nonconstant. Its map to \(\mathbf P^1\) is therefore
surjective and finite. Thus \(p|_H\) is proper with zero-dimensional fibers,
hence finite.

Because \(X\) is smooth, every Weil divisor on \(X\) is Cartier. In
particular, \(H\) is an effective Cartier divisor. It is consequently
Cohen--Macaulay and has no embedded associated points. Let \(t\) be a
uniformizer at a point of \(\mathbf P^1_f\). The pullback of \(t\) cannot
vanish identically on a component of \(H\), since every such component is
horizontal. Hence \(t\) lies in no associated prime of \(\mathcal O_H\), so
it is a nonzerodivisor. It follows that the finite
\(\mathcal O_{\mathbf P^1}\)-module \(p_*\mathcal O_H\) is torsion-free.
A finite torsion-free module over the local DVR of a smooth curve is free.
Therefore \(H\to\mathbf P^1\) is flat.

It remains to compute its rank. For every \(a\in\mathbf P^1\), the
projection formula gives

\[
\begin{aligned}
p^*[a]\cdot Q_\infty
 &=\Phi^*([a]\times\mathbf P^1)\cdot
   \Phi^*(\mathbf P^1\times[\infty])\\
 &=d\,([a]\times\mathbf P^1)\cdot
       (\mathbf P^1\times[\infty])
 =d.
\end{aligned}
\tag{4}
\]

If \(E\) is a component of \(Q_{\mathrm v}\), then

\[
E\cdot p^*[a]
=\deg\bigl((p|_{E^\nu})^*\mathcal O_{\mathbf P^1}(1)\bigr)=0,
\]

because \(p|_E\) is constant. Equations (3)--(4) give

\[
H\cdot p^*[a]=d.
\tag{5}
\]

For the finite flat map \(H\to\mathbf P^1\), the left side of (5) is the
length of a fiber. Thus its rank is \(d\). \(\square\)

This proves more than generic flatness: the horizontal divisor is finite
flat over the whole projective \(f\)-line. The subtlety is that, at a special
value, part of its length can meet boundary components of the total
\(p\)-fiber rather than the strict closure of the affine fiber.

## 4. Local lengths on the good open set are the \(\Lambda(F)\)'s

Delete from \(\mathbf A^1_f\) the finitely many values of the
\(p\)-vertical boundary components. Shrink once more to avoid the critical
values of the restrictions of \(p\) to horizontal boundary components and
the finitely many boundary crossings. Call the resulting nonempty open set
\(U\).

For \(a\in U\):

- the divisor \(p^*[a]\) has no boundary-only component and is the strict
  compactified affine fiber \(C_a\);
- near \(p^{-1}(a)\), the full pole divisor \(Q_\infty\) equals \(H\);
- after normalization \(\nu_a:\overline R_a\to C_a\), the pullback of
  \(Q_\infty\) is the polar divisor of the meromorphic function \(g\).

Thus, at the normalization branch corresponding to a puncture \(P\),

\[
i_P^{\mathrm{br}}(C_a,H)
:=\operatorname{ord}_P(\nu_a^*H)
=\operatorname{ord}_P(g)_\infty
=\Lambda(P).
\tag{6}
\]

If \(F\in T_{a,\mathrm{pole}}\), let \(Z_F\) be the cluster of punctures
represented by \(F\). Proposition 5.6, formula (19), says exactly that the
local intersection length of this cluster is

\[
i_{Z_F}(C_a,H)
=\sum_{P\in Z_F}i_P^{\mathrm{br}}(C_a,H)
=\sum_{P\in Z_F}\Lambda(P)
=\frac{D_{g,F}\deg p_F}{\nu_F}
=\Lambda(F).
\tag{7}
\]

Summing (7) and using the flat rank (5) proves (P5.8) for every \(a\in U\).
This is the generic-fiber reconstruction recorded in
`SIGRAY-AUDIT.md:74`.

## 5. Exact specialization formula

Now fix an arbitrary \(a\in\mathbf C\). Since \(df\) never vanishes on
\(\mathbf A^2\), the affine divisor \(f-a=0\) is reduced. Therefore the
total divisor of the fiber on \(X\) has a unique decomposition

\[
p^*[a]=C_a+B_a^\partial,
\qquad
B_a^\partial=\sum_{\substack{E\subset D\\p(E)=a}}m_EE,
\tag{8}
\]

where \(C_a\) is the reduced strict closure of the affine fiber and
\(m_E=\operatorname{ord}_E(p-a)>0\).

Intersect (8) with \(Q_\infty\). By (4),

\[
d=C_a\cdot Q_\infty
  +\sum_{\substack{E\subset D\\p(E)=a}}m_E(E\cdot Q_\infty).
\tag{9}
\]

Both terms have direct meanings.

First, because \(\mathcal O_X(Q_\infty)=q^*\mathcal O_{\mathbf P^1}(1)\),

\[
E\cdot Q_\infty
=\deg\bigl((q|_{E^\nu})^*\mathcal O_{\mathbf P^1}(1)\bigr)
=\deg(q|_{E^\nu}).
\tag{10}
\]

Here the degree is defined to be zero when \(q|_E\) is constant, including
the case \(q(E)=\infty\). Formula (10) remains valid when \(E\) is itself a
component of \(Q_\infty\); it is a line-bundle degree, not an unjustified
proper-intersection count.

Second, pull \(Q_\infty\) back to the normalization of \(C_a\). It is the
polar divisor of \(g\), so Propositions 5.5--5.6 give

\[
C_a\cdot Q_\infty
=\sum_{P:g(P)=\infty}\operatorname{ord}_P(g)_\infty
=\sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F).
\tag{11}
\]

Combining (9)--(11) yields the exact formula

\[
\boxed{
\sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F)
=d-\Delta_a^{\mathrm{pole}},
\qquad
\Delta_a^{\mathrm{pole}}:=
\sum_{\substack{E\subset D\\p(E)=a}}
m_E\deg(q|_{E^\nu})\geq0 .}
\tag{12}
\]

The superscript distinguishes this new pole defect from Sigray's unrelated
later quantity \(\delta_a\). This completely settles what specialization
alone can say:

- pole mass can only drop at a special fiber;
- only finitely many \(a\)'s can have a nonzero defect
  \(\Delta_a^{\mathrm{pole}}\);
- equality at a specified \(a\) holds if and only if every boundary
  component in \(p^{-1}(a)\) is constant under \(q\);
- equality for all finite \(a\) is equivalent to the absence of a boundary
  component lying over a finite value of \(p\) and dicritical for \(q\).

In particular, finite flatness of \(H\) by itself is insufficient. For the
generically finite map

\[
(x,y)\longmapsto(x,xy),
\]

the generic degree is one. On \(x=a\neq0\), \(xy\) has pole degree one,
whereas on \(x=0\) it is constant and the pole degree is zero. The missing
unit is carried by a vertical dicritical boundary component. This example
is not Keller (its Jacobian is \(x\)); it demonstrates exactly why a
Keller-specific input is still required after flatness.

## 6. The Keller condition kills the defect

The Keller map \(\mathcal F\) is étale and hence quasi-finite and open.
Every affine fiber is therefore finite and reduced. If a fiber has \(n\)
points, the complex inverse-function theorem gives pairwise disjoint small
analytic neighborhoods whose images have a common neighborhood of the
target point. Every nearby generic fiber then has at least \(n\) points.
Hence
\(n\leq d\), while a generic fiber has exactly \(d\) points. Thus Chau's
geometric degree
\(\deg_{\mathrm{geo}}\mathcal F=\max_z\#\mathcal F^{-1}(z)\) is the same
integer \(d\).

Let

\[
E_{\mathcal F}:=
\{z\in\mathbf C^2:\#\mathcal F^{-1}(z)<d\}
\]

be the exceptional value set. We use Chau's description of this
fiber-deficit set directly, so no identification with a differently defined
nonproper-value set is needed. This is Chau's definition of
\(E_{\mathcal F}\) on printed p. 303, after the preceding identification
\(\deg_{\mathrm{geo}}\mathcal F=d\).

Suppose \(\Delta_a^{\mathrm{pole}}>0\). Then some boundary component \(E\)
satisfies
\(p(E)=a\) and \(q|_E\) is nonconstant. Equivalently, \(\Phi(E)\) is the
projective vertical line \(\{a\}\times\mathbf P^1\). Formula (12) also shows
directly that, for generic \(b\in\mathbf C\) (in particular, avoiding the
finite values of \(g\) at the other punctures),

\[
\#\mathcal F^{-1}(a,b)
=\deg(g|_{\overline R_a})
=d-\Delta_a^{\mathrm{pole}}<d.
\]

Thus a dense open subset of the affine vertical line
\(\{a\}\times\mathbf C\) lies in \(E_{\mathcal F}\). Chau's theorem below
also says that \(E_{\mathcal F}\) is a finite union of algebraic curves;
therefore the closure of that dense subset, the vertical line, is an
irreducible component of \(E_{\mathcal F}\).

This is impossible by Nguyen Van Chau's theorem. In
[N. V. Chau, *Non-zero constant Jacobian polynomial maps of
\(\mathbf C^2\)*, Ann. Polon. Math. 71 (1999), 287--310,
Theorem 4.4(E1), printed pp. 304--305](https://matwbn.icm.edu.pl/ksiazki/apm/apm71/apm7135.pdf),
the exceptional set of a nonzero constant-Jacobian map is a finite union of
polynomially parametrized curves

\[
C[\varphi]
=\{(f_\varphi(\xi),g_\varphi(\xi)):\xi\in\mathbf C\},
\]

and every such curve satisfies

\[
\frac{\deg f_\varphi}{\deg g_\varphi}
=\frac{\deg f}{\deg g}>0.
\tag{13}
\]

A generic affine change of source coordinates makes both leading
\(y\)-coefficients nonzero constants, and independent nonzero scalings of
the two target coordinates make both polynomials monic in the variable
required in Chau's statement. These changes preserve the Keller condition
and the property of the exceptional set having a vertical-line component.
If a component
were \(\{a\}\times\mathbf C\), its parametrization would have
\(\deg f_\varphi=0\) and \(\deg g_\varphi>0\), contradicting (13).
(Chau's Theorem 4.4(E3), which literally says every curve
\(C[\varphi]\) has a singularity, independently excludes an affine line as
well.)

Therefore \(\Delta_a^{\mathrm{pole}}=0\) for every \(a\). Equation (12),
followed by (1), proves

\[
d
=\sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F)
=\sum_{F\in T_{a,\mathrm{pole}}}
  \frac{D_{g,F}\deg p_F}{\nu_F}
\quad\text{for every }a\in\mathbf C.
\]

This is Proposition 5.8 at its printed strength. \(\square\)

There is a useful independent source check in the same Chau paper.
Theorem 4.1(ii), printed pp. 301--302, explicitly identifies the geometric
degree with the sum of the local degrees at the poles of \(Q\) on \(P=0\).
Applying it to \((P-a,Q)\) gives the every-\(a\) pole-order equality in one
line. The argument above explains geometrically why that shifted statement
is valid and identifies the precise obstruction that its Keller hypothesis
removes.

## 7. Honest hypothesis perimeter

The proof has three logically separate levels.

### 7.1 Relative geometry alone

For any generically finite polynomial map \((f,g):\mathbf A^2\to\mathbf
A^2\), after resolution:

- the horizontal part of \(q^*(\infty)\) is finite flat of rank
  \(\operatorname{td}(f,g)\);
- the generic-fiber pole-mass identity holds;
- every fiber satisfies the defect formula (12), provided the strict-fiber
  cycle and its normalized components are counted with their scheme
  multiplicities.

No Keller condition is used in those assertions except that, in the Keller
case, the affine fibers of \(f\) are automatically reduced and smooth. For
a more general map, the strict-fiber cycle should be retained with its
scheme multiplicities.

### 7.2 Weakest sufficient hypothesis

For one fixed fiber \(a\), the necessary and sufficient hypothesis is

\[
\tag{NV\(_a\)}
\deg(q|_{E^\nu})=0
\quad\text{for every boundary component }E\text{ with }p(E)=a.
\]

For all finite fibers, the corresponding hypothesis is

\[
\tag{NV\(_{\mathrm{aff}}\)}
\text{there is no boundary component }E\text{ with }
p(E)\in\mathbf C\text{ and }q|_E\text{ nonconstant}.
\]

On a graph resolution this is equivalent to the affine exceptional set
having no vertical-line component: that set is the union of the affine
images of boundary components, so each vertical curve component is
dominated by a component with constant finite \(p\) and nonconstant \(q\).
This condition is resolution-independent. Components with
\(p(E)=\infty\) are irrelevant to Proposition 5.8. Without
(NV\(_{\mathrm{aff}}\)), generic flatness cannot be upgraded: the exact bad
set is

\[
B=\{p(E)\in\mathbf C:E\subset D,\ p|_E\text{ constant},\
q|_E\text{ nonconstant}\},
\]

and the failure at \(a\in B\) is the positive integer
\(\Delta_a^{\mathrm{pole}}\) in (12).

### 7.3 Keller input

Chau's Theorem 4.4 proves (NV\(_{\mathrm{aff}}\)) for complex polynomial
Keller maps. This is an external input absent from Sigray's printed proof
(indeed, Proposition 5.8 has no printed proof at all). It rules out only
finite vertical exceptional components; it does not assert that the whole
exceptional set is empty.

If the campaign elects not to import Chau's theorem, the strongest
self-contained conclusion from the relative argument is (12), together
with Proposition 5.8 on a nonempty generic open. No assertion about
cross-fiber invariance of \(\nu_F\) repairs this logical point by itself.

## 8. What this repairs downstream

1. **Layer E / BOOK.** The mass-identity rider in
   `BOOK-ENUM.md:199--201` (and the inherited rider in
   `BOOK-OFFAXIS.md:176--177`) is discharged once Chau's
   no-vertical-component theorem is admitted. The exact partitions

   \[
   d=\sum_i\Lambda_i,
   \qquad \Lambda_i\geq\beta
   \]

   are valid on every fiber. Thus the \(d=6\) singleton-or-\(3+3\) split,
   the two-pole row-1 forcing, the TDUNIFORM singleton equation
   \(\Lambda=d\), and the BOOK E-layer partition statement retain their
   every-fiber strength. Direct consumers include
   `SHEET6-CAMPAIGN.md:23--26,92--100`,
   `SHEET6-2POLE.md:89--98`, `SHEET6-L1.md:141--146`,
   `SHEET6-TDUNIFORM.md:52--56,240--256`,
   `SHEET6-MULTIPOLE.md:48,61`, and
   `SHEET6-DEPTH-REVIEW.md:250--257`. Proposition 5.7 supplies the lower
   bound; table (23), printed p. 46, supplies the local
   \(\Lambda\leq6\) possibilities. This repairs only the mass layer; it
   does not discharge BOOK's independent off-axis, mixed-merge, or other
   completeness riders. Fixed-cell algebra is unaffected, while any panel
   exhaustiveness claim continues to inherit those independent riders.

2. **No transport rider.** Specialization may split or merge pole vertices
   and may change individual \(\nu_F\)'s. The proof needs no claim that an
   individual vertex or \(\nu_F\) is invariant. Proposition 5.6 groups the
   actual punctures separately on each fiber, while (12) controls only the
   total. Without the Keller input, special fibers could therefore change
   both the pole count and the exact partition; this cannot rescue a pair
   already contradicted on the generic open.

3. **Fallback if the external lemma is withheld.** The campaign's global
   counterexample-exclusion arguments still survive with generic
   Proposition 5.8: choose one \(a\) in the common nonempty good open and
   run the same relevant entry/book argument on \(T_a\). Every global
   exclusion conclusion that is otherwise valid retains its force, because
   an impossible generic fiber rules out the pair. A good generic \(a\) may
   also be shifted to zero, so the coefficient gauges used downstream cause
   no loss (`SHEET6-LT-REVIEW.md:303--317`). What would remain unproved are
   only literal classifications of an arbitrarily prescribed exceptional
   fiber. Even without (NV\(_{\mathrm{aff}}\)), (12) gives
   \(\sum\Lambda(F)\leq d\), so bounds such as
   \(\#T_{a,\mathrm{pole}}\leq d/\beta\) still hold on every fiber; exact
   partitions require equality.

4. **The `LROOT` every-fiber \(\delta_a\) claim.** The warning in
   `SIGRAY-AUDIT.md:91` is stronger than necessary for this particular
   consumer. `SHEET6-LROOT.md:46--58,238--247` gets
   \(\delta_a=0\) for every \(a\) from Proposition 7.5's global equality,
   nonnegativity, and saturation on a generic carrier. Generic Proposition
   5.8 is still used earlier to classify and size that carrier. Once the
   carrier is established, however, the implication from ledger saturation
   to \(\delta_a=0\) for every \(a\) does not invoke Proposition 5.8 on a
   special fiber; its only explicit every-fiber use in that itemization is
   the no-hidden-poles sanity check at `SHEET6-LROOT.md:75--79`. Hence that
   implication survives even under the generic-only fallback; the present
   proof now also restores the sanity check at every-fiber strength.
