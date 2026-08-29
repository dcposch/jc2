# Sigray Proposition 5.8 (20): independent every-fiber audit

Date: 2026-08-28 (America/Los_Angeles)  
Scope: `refs/sigray_full.pdf`, printed p. 28; corrected campaign notation;
promoted Proposition 5.1 and Proposition 5.4 repairs; current direct
consumers.  No canonical ledger was edited, and no `jc2-lean` file was read
or modified.

## 0. Executive verdict

For a normalized complex Keller pair \((f,g)\), with the campaign's corrected
reading

\[
 p_F=p_{f-a,F},\qquad d_F=d_{f-a,F},
\]

and its promoted Proposition 5.1 repair, Sigray's formula is true at the
printed strength:

\[
 \boxed{
 \operatorname{td}(f,g)
 =\sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F)
 =\sum_{F\in T_{a,\mathrm{pole}}}
   \frac{D_{g,F}\deg p_F}{\nu_F}
 \quad\text{for every }a\in\mathbf C.}
\tag{20}
\]

The thesis does not prove this: Proposition 5.8 is followed immediately by
Section 6 on printed p. 28.  There are, however, two valid closures.

1. **Internal corrected-tree closure (new audit proof below).**  A pole
   threshold is strictly in \(T_a^+\) by the promoted Proposition 5.1
   sidedness theorem.  At positive \(f-a\) order, replacing \(a\) by another
   fiber value changes only an order-zero term and cannot change the strict
   Puiseux truncation or its leading equation.  Direct Newton--Puiseux
   continuation therefore gives a bijection of pole vertices across fibers,
   preserving \(d_g,\deg p_F,\kappa_F,\nu_F\), hence each \(\Lambda(F)\).
   This is proved below without citing Statement 3.14's unproved exact root
   alignment.
2. **Independent relative-surface closure.**  On a simultaneous resolution
   one obtains the exact formula

   \[
   \sum_F\Lambda(F)=d-\Delta_a,\qquad
   \Delta_a=\sum_{E\subset D,\ \bar f(E)=a}
     \operatorname{ord}_E(f-a)\deg(\bar g|_{E^\nu})\ge0.
   \]

   The only possible loss is an \(f\)-vertical, \(g\)-dicritical boundary
   component.  Chau, Theorem 4.4(E1), excludes a vertical component of the
   fiber-deficit set of a Keller map, so \(\Delta_a=0\) for every finite
   \(a\).  The one-line nonconstancy repair omitted from the body of
   `SOL-PROP58.md` is supplied in section 6 below.

Thus there is no mathematical rollback of the mass/entry layer.  The
remaining issue is status drift: `SIGRAY-AUDIT.md` still labels Proposition
5.8 a GAP and still advertises the incomplete one-line
Statement-3.14/\(\nu_F\) route, while `REDUCTION.md` and `SOL-PROP58.md`
already record the external replacement.

## 1. Frozen source hashes

All hashes are SHA-256 of the files read for this audit.

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7  refs/chau1999_apm71_full.pdf
71f894f632b0edfe1fa47247c517da3c6735f6fa535042eded897876aab629e0  ladder/SIGRAY-AUDIT.md
2647dd29eca7ec81028bbe735e7937ae60d55b6155397e4d965c3011d8732592  ladder/SOL-PROP58.md
569661d0771b8353ae76e4d8f48a809f996e83b36a93239f1e8540bb274fbac8  ladder/SOL-PROP58-REVIEW.md
9ff5d00567d7b6752ecc79892bb41959a450ddff3837bdb26179899ad2dfad5a  ladder/SHEET6-LROOT.md
b76f5a6a0ea50e67b4611b9fca1a6db2e0386866f09b177c6bb5066b967ee0d2  ladder/SHEET6-TDUNIFORM.md
086a475927b5cdec68dcdffc836bf06c0418616113aa3ccc91bc98d9eafb1678  ladder/SHEET6-CAMPAIGN.md
78215e1ff847f10ee4df26615443f56ab49c9e21366137898c0742525d78decc  ladder/SHEET6-MULTIPOLE.md
c52e310e0647293959d8651db31e569b7175db814eb411d81b894f47c775531d  ladder/REDUCTION.md
a0470416481378c02cc5a20e8aef826be1203c32c6dbfe664ae197cfdc34b9dc  xmodel/sigray-prop51-forced-puncture-shift-sol-ultra-20260828.md
dc549047acc39385e3c025a16108098edc82c827495dc53fea81437c81dd334a  xmodel/sigray-prop51-forced-puncture-shift-hostile-review-opus5-20260828-r1.md
110591663b4077509dee35f4c39daf687603c94cd3e20d559f78426da3ef6ca7  xmodel/sigray-prop51-forced-puncture-shift-coordinator-integration-sol-ultra-20260828.md
be9e4b747e02ba97a30b8d6254514f568dec8a197dcbbc4a49446ba5fdb38a9e  xmodel/sigray-prop54-qhalf-sol-ultra-20260828-r2.md
c3f0bfde24fb265e6ece9fce40089868fd64b01b3f6f5eac3ef0ee5df43e1f30  xmodel/sigray-prop54-qhalf-hostile-review-opus5-20260828-r1.md
6375bc05958cc513c753759ce9e2f84adfff78a76bef61d331c4dd33d44a3e80  xmodel/sigray-prop54-qhalf-coordinator-integration-sol-ultra-20260828.md
```

## 2. Exact local statement and corrected dependency perimeter

Let \(R_a=f^{-1}(a)\), let \(\overline R_a\) be the disjoint smooth
compactification of its components, and let \(P\) be a puncture.  If \(g\)
has a pole at \(P\), write

\[
 \Lambda(P)=\operatorname{ord}_P(g)_\infty.
\]

The corrected local Sigray package gives:

\[
 \Lambda(F):=\frac{D_{g,F}\deg p_F}{\nu_F}
 =\sum_{P:\,F=I_P(\pi(F))}\Lambda(P),
 \qquad F\in T_{a,\mathrm{pole}}.
\tag{L}
\]

The exact dependencies of (L) are:

- corrected Proposition 5.1/Notations 5.1--5.2, so that
  \(T_{a,\mathrm{pole}}\) is exactly the set of thresholds belonging to
  actual \(g\)-poles and no finite puncture leaks into it;
- Proposition 5.3(v),(ix), for simple terminal roots and no later vertex;
- corrected Statement 3.18, with continuation \(F*(\varepsilon c)\);
- Propositions 5.5--5.6, including the corrected \(g\)-subscripts in the
  proof of Proposition 5.5;
- the campaign's canonical jump/maximal-presentation convention for
  \(\kappa_F\), so \(D_{g,F}=\kappa_Fd_{g,F}\) is intrinsic.

The promoted Proposition 5.1 repair is especially important.  For a
puncture \(P\), set

\[
 b_P=\begin{cases}g(P),&g(P)\in\mathbf C,\\0,&g(P)=\infty,\end{cases}
 \qquad
 \rho_P(v)=d_{f-a,I_P(v)}+d_{g-b_P,I_P(v)}+v-1.
\]

It proves that the first zero \(u_P\) of \(\rho_P\) is a sided threshold:

\[
 g(P)=\infty\iff F_P^*=I_P(u_P)\in T_a^+,
 \qquad
 g(P)\in\mathbf C\iff F_P^*\in T_a^-;
\tag{S}
\]

in particular a threshold never lies in \(T_a^0\).  At a pole, \(b_P=0\),
so the original printed pole formulas are literal.

The Proposition 5.4 repair is **not** needed to prove the equality (20).
It is needed immediately downstream: it supplies the omitted \(q\)-half of
the \(\eta^{\nu_F}\)-pattern, hence Statement 5.2(ii)'s \(\nu_F\)-menu,
Proposition 5.7's \(\Lambda\ge\beta\) arithmetic, and the finite entry table.
Therefore the equation and the campaign enumeration have slightly different
trust perimeters.

## 3. Generic-fiber identity from finite etale degree

Put

\[
 d=[\mathbf C(x,y):\mathbf C(f,g)]=\operatorname{td}(f,g).
\]

The constant nonzero Jacobian makes
\(\mathcal F=(f,g):\mathbf A^2\to\mathbf A^2\) etale and quasi-finite.
There is a nonempty open set \(W\subset\mathbf A^2\) over which
\(\mathcal F\) is finite etale of rank \(d\).  Choose \(a_0\) so that the
vertical line \(L_{a_0}\) is not contained in \(\mathbf A^2\setminus W\).
For generic \(b\),

\[
 \#\mathcal F^{-1}(a_0,b)=d.
\]

On every irreducible component \(\Gamma\subset R_{a_0}\), the restriction
of \(g\) is nonconstant: otherwise both \(df\) and \(dg\) annihilate the
one-dimensional tangent space \(T\Gamma\), contradicting
\(df\wedge dg\ne0\).  For generic \(b\), also avoiding the finitely many
branch values of the compactified restrictions and the finite \(g\)-values
at punctures, all points counted by
\(\deg(g:\overline R_{a_0}\to\mathbf P^1)\) are affine and simple.  Hence

\[
 d=\deg(g|_{\overline R_{a_0}})
  =\sum_{P:g(P)=\infty}\Lambda(P)
  =\sum_{F\in T_{a_0,\mathrm{pole}}}\Lambda(F).
\tag{G}
\]

This establishes Proposition 5.8 on a nonempty generic open without any
cross-fiber tree assertion.

## 4. Direct positive-tail transport lemma

The following is the missing internal upgrade.  It deliberately proves only
what pole vertices require and does not cite Statement 3.14.

### Lemma (positive pole-data transport)

For any \(a,b\in\mathbf C\), there is a bijection

\[
 \tau_{a,b}:T_{a,\mathrm{pole}}\longrightarrow T_{b,\mathrm{pole}}
\]

such that, for \(F'=\tau_{a,b}(F)\),

\[
 d_{g,F'}=d_{g,F},\quad
 \deg p_{F'}=\deg p_F,\quad
 \kappa_{F'}=\kappa_F,\quad
 \nu_{F'}=\nu_F,
\tag{T1}
\]

and therefore \(D_{g,F'}=D_{g,F}\) and \(\Lambda(F')=\Lambda(F)\).

### Proof

Fix \(F=F_P^*=I_P(u)\in T_{a,\mathrm{pole}}\).  By (S),
\(d_{f-a,F}>0\).  Work in one of the two Puiseux charts; the other is
symmetric.  Choose a common suitable ramification index \(K\), and write the
strict truncation of the selected series as

\[
 s_{<u}(x)=\sum_{j/K<u}c_jx^{-j/K},
 \qquad y=s_{<u}(x)+x^{-u}\eta.
\]

With this substitution,

\[
 (f-a)(x,s_{<u}+x^{-u}\eta)
 =x^{d_F}\bigl(p_F(\eta)+\text{lower }x\text{-order}\bigr),
 \qquad d_F>0.
\tag{T2}
\]

Replacing \(a\) by \(b\) adds the constant \(a-b\), of order zero.
Because \(d_F>0\), it cannot alter the leading exponent or polynomial in
(T2):

\[
 d_{f-b}=d_F,\qquad p_{f-b}=p_F
\tag{T3}
\]

at this strict truncation.  Let \(c\) be the coefficient of the branch
\(P\) at height \(u\); it is a root of \(p_F\).  Proposition 3.1 applied to
the squarefree polynomial \(f-b\) gives a branch \(Q\) of \(f=b\) with the
same truncation and the same coefficient \(c\) at height \(u\).  Squarefree
is automatic because \(df\) never vanishes.  At a pole vertex the roots of
\(p_F\) are simple by Proposition 5.3(v), so this continuation is unique for
each root in a fixed common Puiseux field.  Repeating it for every root gives
a bijection between the complete sets of series/presentations realizing the
two height-\(u\) classes.  Set

\[
 F':=I_Q(u).
\]

This class is independent of all choices.  Classes at height \(u\) remember
only coefficients strictly below \(u\); any two continuations constructed
above have contact at least \(u\).  Repeating the construction from \(b\)
to \(a\) returns the same strict-truncation class, so the resulting map is
injective and has inverse \(\tau_{b,a}\).  More explicitly, the construction
commutes with every deck conjugation in the common Puiseux field.  Hence it
preserves the maximum contact over conjugates used in Definition 3.2; if two
transported classes acquired contact at least \(u\), reverse transport would
give the same contact for the original classes.  No global alignment choice
for the auxiliary maps \(\Omega\) is being assumed.

For every polynomial \(h\), not merely \(f\), the formal expression

\[
 h(x,s_{<u}+x^{-u}\eta)
\]

depends only on the common strict truncation.  Consequently the leading
\(g\)-data at \(F\) and \(F'\) agree.  If independently chosen Puiseux
representatives use different deck conjugates, the relation is
\(\eta\mapsto\zeta\eta\) for a root of unity \(\zeta\); this preserves the
leading exponent, degree, root multiplicities, and nonvanishing of the
leading Jacobian.  Thus

\[
 d_{g,F'}=d_{g,F},\qquad \deg p_{F'}=\deg p_F.
\tag{T4}
\]

The same argument works at every height \(v\le u\) on the two matched
paths.  In particular the corrected functions \(\rho_P(v)\) agree through
height \(u\).  Below \(u\) they are positive and at \(u\) they vanish.
Moreover, at a pole threshold \(d_g>0\), and monotonicity gives positive
\(g\)-order at every earlier height.  Subtracting any finite target constant
from \(g\) therefore cannot change this leading data through \(u\).  Hence
\(u\) is also the corrected Proposition 5.1 threshold of \(Q\), whether its
centre is provisionally written as zero or as a hypothetical finite
\(g(Q)\).  Since its \(f-b\) order is the positive number in (T3), the
sidedness equivalence (S) forces \(g(Q)=\infty\).  Thus
\(F'\in T_{b,\mathrm{pole}}\), and the inverse construction proves
bijectivity on pole vertices.

It remains to justify the two indices rather than assume them.  For one
presentation with characteristic data
\((K,\beta_1,\ldots,\beta_j,\ldots)\), Sigray's printed presentation-value
at height \(u\) is

\[
 \kappa_F=K/e_j,
 \qquad e_j=\gcd(K,\beta_1,\ldots,\beta_j),
\]

with the last characteristic exponent at or below \(u\).  This is the
denominator index of that presentation's nonzero exponents visible through
height \(u\); later ramification is irrelevant.  At a multiply realized
vertex the printed value can depend on the presentation.  The campaign's
canonical Q/jump/max repair takes the maximum of these presentation-values.
The preceding all-root correspondence preserves the **entire set** of
presentations and each member's denominator index, so it preserves their
maximum: \(\kappa_{F'}=\kappa_F\).

Likewise, a presentation realizes \(F\in V_1\) precisely when height \(u\)
produces a new denominator jump.  If it does, then

\[
 \nu_F=e_{j-1}/e_j
       =\frac{K/e_j}{K/e_{j-1}},
\]

the jump in the denominator index at \(u\).  The coefficient witnessing a
characteristic exponent is nonzero; its aligned coefficient on the
corresponding series is the same up to a nonzero root-of-unity factor.  The
all-root correspondence therefore preserves which presentations jump and
their jump ratios.  Using the already audited presentation-independence of
Notation 3.4, it follows that \(\nu_{F'}=\nu_F\); if neither vertex lies in
\(V_1\), both indices are one.  No exact equality of the two chosen
\(\eta\)-coordinates is asserted.

Equations (T1) follow.  Finally

\[
 \Lambda(F')
 =\frac{\kappa_{F'}d_{g,F'}\deg p_{F'}}{\nu_{F'}}
 =\frac{\kappa_Fd_{g,F}\deg p_F}{\nu_F}
 =\Lambda(F).
\]

This completes the lemma. \(\square\)

### Completion of (20)

Transport the pole vertices of an arbitrary fiber \(a\) to the generic
fiber \(a_0\) of (G).  The lemma is a bijection preserving every summand,
so

\[
 \sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F)
 =\sum_{F\in T_{a_0,\mathrm{pole}}}\Lambda(F)=d.
\]

This proves Proposition 5.8 for every \(a\).

## 5. Adjudication of the proposed Statement 3.14 plus nu route

The old proposed route was directionally right but not a proof as stated.

### What the printed statement does not justify

1. The source must use \(f-a\), not the printed bare \(f\), in the
   definitions of \(d_F,p_F,T_a^\pm,T_a^0\).
2. The line “\(\eta_F=\eta_G\)” assumes compatible choices of Puiseux deck
   representatives.  In general one gets equality only after a
   root-of-unity conjugation \(\eta\mapsto\zeta\eta\).
3. Invariance of \(\nu_F\) alone is insufficient.  Formula (20) also needs
   transport of the pole set itself, \(d_{g,F}\), \(\kappa_F\) (hence
   \(D_{g,F}\)), and \(\deg p_F\).
4. Statement 3.14 states preservation of the \(f\)-leading form, not the
   all-polynomial leading-data functoriality needed for \(g\) and the
   threshold predicate.

### What now makes a repaired route work

The promoted Proposition 5.1 repair supplies the formerly missing firewall:
every pole threshold is strictly positive, while every finite-puncture
threshold is strictly negative.  Therefore pole transport never reaches the
order-zero wall where the fiber constant can change the leading Newton
equation.  Section 4 directly proves the needed all-polynomial transport and
derives \(\kappa_F,\nu_F\) invariance from the exponent-denominator filtration.
The root-of-unity twist is harmless because (20) uses only numerical
invariants.

Accordingly:

- **Do not cite printed Statement 3.14 plus “\(\nu_F\) is invariant” as a
  one-line proof.**  That route has multiple missing links.
- **The narrowed positive-pole transport lemma is valid** under the promoted
  Proposition 5.1 repair and closes those links without exact root alignment.
- Proposition 5.4 does not enter this transport; it resumes at the
  \(\nu\)-menu/lower-bound/entry-enumeration layer.

## 6. Independent relative-surface check and exact fallback

This section rederives the already promoted geometric replacement and
identifies the sharp weakening if the internal transport lemma or the Keller
input is withheld.

Resolve the rational extension of \((f,g)\) to obtain a smooth projective
surface \(X\supset\mathbf A^2\) and morphisms

\[
 p=\bar f:X\to\mathbf P^1,
 \qquad q=\bar g:X\to\mathbf P^1.
\]

Let \(D=X\setminus\mathbf A^2\) and \(Q_\infty=q^*[\infty]\).  Since
\(\Phi=(p,q)\) is generically finite of degree \(d\), projection gives

\[
 p^*[a]\cdot Q_\infty=d.
\tag{R1}
\]

The Keller condition makes \(f-a\) smooth and reduced on the affine plane,
so

\[
 p^*[a]=C_a+\sum_{E\subset D,\,p(E)=a}m_EE,
 \qquad m_E=\operatorname{ord}_E(f-a)>0,
\tag{R2}
\]

where \(C_a\) is the reduced strict closure of \(R_a\).  Because
\(\mathcal O_X(Q_\infty)=q^*\mathcal O_{\mathbf P^1}(1)\),

\[
 E\cdot Q_\infty=\deg(q|_{E^\nu})\ge0,
\tag{R3}
\]

where the degree is zero if \(q|_E\) is constant, including \(q(E)=\infty\).
Pulling \(Q_\infty\) to the normalization of \(C_a\) gives the polar divisor
of \(g\); (L) therefore gives

\[
 C_a\cdot Q_\infty
 =\sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F).
\tag{R4}
\]

Combining (R1)--(R4):

\[
 \boxed{
 \sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F)
 =d-\Delta_a,\qquad
 \Delta_a=\sum_{E\subset D,\,p(E)=a}
 m_E\deg(q|_{E^\nu})\ge0.}
\tag{R5}
\]

Thus relative geometry alone proves equality generically and
\(\sum\Lambda\le d\) on every fiber.  Equality fails exactly when a boundary
component is constant with finite \(p\)-value and nonconstant under \(q\).

For a Keller pair, suppose \(\Delta_a>0\).  For generic \(b\), avoiding both
branch values of \(g|_{\overline R_a}\) and the finite \(g\)-values of
punctures,

\[
 \#(f,g)^{-1}(a,b)=\deg(g|_{\overline R_a})=d-\Delta_a<d.
\]

The equality here uses the line supplied in section 3: \(g\) is nonconstant
on every component of \(R_a\), since otherwise \(df\wedge dg\) vanishes on
its tangent.  Chau defines the geometric degree as the maximum fiber
cardinality.  It equals \(d\) here: if one fiber has \(n\) points, etaleness
gives \(n\) disjoint analytic inverse neighborhoods over a common target
neighborhood; a generic point in that neighborhood has \(d\) preimages and
therefore \(n\le d\), while generic fibers attain \(d\).  A cofinite subset
of the vertical line \(\{a\}\times\mathbf C\) then lies in Chau's
fiber-deficit set.  Theorem 4.4 writes that set as a finite union of
polynomial curves \((P_\varphi(t),Q_\varphi(t))\) satisfying

\[
 \frac{\deg P_\varphi}{\deg Q_\varphi}
 =\frac{\deg f}{\deg g}>0.
\]

Each nonconstant polynomial parametrization has closed image (it is finite
over either nonconstant coordinate).  Since the union is finite, a cofinite
subset of the irreducible vertical line forces that line to be one of its
curve components.  Such a component would have numerator degree zero and
denominator degree positive, contradicting the displayed positive ratio.
Hence \(\Delta_a=0\) for every finite \(a\).  Generic source coordinates and
independent target scalings make both polynomials monic in Chau's required
variable without changing verticality or the degree ratio.

As a calibration showing that neither flatness nor generic equality alone
is enough, consider \((f,g)=(x,xy)\).  Its generic degree is one.  On
\(x=a\ne0\), \(g=ay\) has pole degree one; on \(x=0\), it has pole degree
zero, and \(\Delta_0=1\).  Its Jacobian is \(x\), so it lies outside the
Keller and corrected-sidedness hypotheses exactly where it should.

## 7. Consumer audit and blast radius

### Direct consumers restored at every-fiber strength

| Consumer | Exact use | Verdict after this audit |
|---|---|---|
| `SHEET6-CAMPAIGN.md` lines 36--39, 112--119 | \(d=6\) partition: one \(\Lambda=6\) pole or two \(3+3\) poles | Sound relative to the corrected local/entry perimeter. |
| `SHEET6-TDUNIFORM.md` lines 52--56, 240--256 | singleton \(\Lambda(F)=d\), closed-form rows, prime-\(d\) entry theorem | Mass step sound; its \(\nu\)-menu and \(\Lambda\ge\beta\) additionally require the promoted Proposition 5.4 repair. |
| `SHEET6-2POLE.md`, `SHEET6-L1.md`, `SHEET6-A3L1-REVIEW.md` | \(3+3\) forcing and row-1 identification | Sound at arbitrary prescribed \(a\). |
| `SHEET6-MULTIPOLE.md` | \(d=\sum_i\Lambda_i\ge m\beta\), hence \(m\le d/3\) | Sound.  No other multipole completeness rider is repaired. |
| `BOOK-ENUM.md`, `BOOK-OFFAXIS.md`, `SHEET6-DEPTH-REVIEW.md` | exact layer-E partitions and finite entry menu | Mass rider discharged; off-axis/merge/suffix completeness remains separate. |

### `SHEET6-LROOT.md`

The every-fiber use at lines 80--84 is a pole-purity/no-hidden-pole sanity
check and is now justified.  It is not the logical source of the stronger
claim \(\delta_a=0\) for every \(a\) at lines 243--252.  That conclusion
comes from Proposition 7.5's single global equality, nonnegativity, and
saturation by a generic carrier.  Consequently, even the generic-only
fallback (R5) would preserve the `LROOT` all-\(a\) \(\delta\)-conclusion once
the carrier is established.

### Status drift, not a mathematical rollback

- `SIGRAY-AUDIT.md` lines 74 and 116 still say GAP and name
  Statement-3.14/\(\nu_F\) transport as the highest-priority repair.  The
  source-page verdict “printed proof absent” remains correct; the campaign
  replacement status is stale.
- `REDUCTION.md` T7 and its dependency ledger already record an every-fiber
  replacement via `SOL-PROP58.md` plus Chau.  That is consistent with this
  audit.
- `SOL-PROP58.md` has a truthful main argument but its body still omits the
  one-line “\(g\) nonconstant on every component” step and still links to a
  truncated external PDF URL.  The full local source hash above contains
  Theorem 4.4.  These are publication/citation repairs, not proof failure
  once `REDUCTION.md` T7 and the local source are included.
- `BOOK-ENUM.md:199` and `BOOK-OFFAXIS.md:199` retain generic-\(a\) rider
  prose even though the master reduction records the completed replacement.

If both the direct lemma of section 4 and Chau's theorem are deliberately
withheld, the exact safe weakening is (R5): generic equality and
\(\sum_F\Lambda(F)\le d\) for every \(a\).  Then per-fiber exact partitions
must be weakened, but bounds such as \(|T_{a,\mathrm{pole}}|\le d/\beta\)
survive.  Global contradiction arguments may still choose a good generic
fiber; only classifications of an arbitrarily prescribed exceptional fiber
would lose exactness.

## 8. Final dependency verdict

**Equation (20), every finite fiber:** proved under the campaign's corrected
local Sigray package.  The new essential internal input is the reviewed
Proposition 5.1 sidedness/non-leakage theorem.  The proof does not consume
the repaired Proposition 5.4, printed Statement 3.14's exact root alignment,
or an assumed standalone invariance of \(\nu_F\).

**Entry arithmetic derived from (20):** additionally conditional on the
promoted Proposition 5.3 degree/ratio corrections, Proposition 5.4
\(q\)-half repair, Statement 5.2 corrections, and Proposition 5.7.

**Independent external cross-check:** the relative divisor formula plus
Chau Theorem 4.4(E1) proves the same every-fiber conclusion and exposes the
precise defect that would occur outside the Keller perimeter.

**Blast radius:** no rollback to `CAMPAIGN`, `TDUNIFORM`, the two-pole/`L1`
entry forcing, or the multipole mass bound.  No conclusion about later
Section 6--9 completeness, off-axis landing, merge coverage, coefficient
realizability, or JC2 follows from this repair.
