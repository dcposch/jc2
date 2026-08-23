# WTC-1 round 2: flag transport is canonical; concentration is the residual

**Date:** 2026-08-23  
**Scope:** the geometric residual isolated in `xmodel/sol-wtc1.md`, and the
subsequent PCC coverage/no-double-counting arrow.  
**Status:** the infinitely-near point/proximity naming part of WTC-1 is proved
below at theorem level; membership in the two base clusters comes only after
the order lemma.  The claimed ordinary multiplicities are **not** proved.  They are
equivalent to one minimal global lemma, **CONJECTURE KPC**.  A stronger exact
local separation example shows that KPC cannot follow from the paired leading
power, the two denominator capacities, and the pulled-back Jacobian identity
alone.  The unconditional object carried by a packet is a flag/contact flow,
not a point-basis atom.

---

## 0. Verdict

Put

\[
 d=B\alpha,\qquad e=B\beta,\qquad
 T=qt,\qquad A=\alpha T,\qquad C=\beta T.             \tag{0.1}
\]

For a certified paired Corollary-7.4 packet, the previous round proved

\[
 \ell(P)=\lambda_P\widetilde R^{q\alpha},\qquad
 \ell(Q)=\lambda_Q\widetilde R^{q\beta},              \tag{0.2}
\]

and a root of multiplicity \(t\) in \(\widetilde R\) therefore gives boundary
orders \(A,C\).  The new conclusions are as follows.

1. **The packet canonically names a flag over the original plane.**  The
   weight is a divisorial valuation and the selected residue root is a closed
   point on its divisor.  Their composition is an intrinsic rank-two flag
   valuation.  Pulling it back through the exact Laurent prefix, and
   restricting a fractional packet from the Kummer field to \(k(x,y)\),
   gives a unique proper or infinitely-near point.  The point's Enriques
   path gives its proximity parent or parents.  Common refinements, alternate
   regular fans, graph resolutions, root coordinates, and Kummer
   presentations do not change this point.  This proves the mathematical
   content of the previous **WTC-CHART** and **WTC-ID** assertions, provided
   “certified packet” retains the exact field maps and the conjugate root
   orbit, as Definition (1.2) of `sol-wtc1.md` requires.

2. On a regular realization of the flag, after removing the full height-one
   gcds, the two weak ideals have the form

   \[
   I_f=(A_f,B_f),\qquad I_g=(A_g,B_g),                 \tag{0.3}
   \]

   with

   \[
   A_f(0,r)=u_f(r)r^A,\qquad
   A_g(0,r)=u_g(r)r^C.                                \tag{0.4}
   \]

   Hence their ordinary orders are at most \(A,C\).  The entire remaining
   WTC assertion is exactly the following ideal-containment statement:

   > **CONJECTURE KPC (global Keller packet concentration).**  For every
   > packet coming from the selected *polynomial* Keller pair with its full
   > eligible Corollary-7.4 prefix,
   > \[
   > I_f\subseteq\mathfrak m_p^A,
   > \qquad I_g\subseteq\mathfrak m_p^C.              \tag{KPC}
   > \]

   Boundary equality (0.4) then forces

   \[
   \operatorname{ord}_p I_f=A,qquad
   \operatorname{ord}_p I_g=C.                        \tag{0.5}
   \]

   Conversely, the WTC multiplicity conclusion forces (KPC).  Thus KPC is
   necessary and sufficient; it combines the old WTC-ORD and WTC-DEN without
   retaining artificial independence between them.

3. **A packet is naturally contact flow, not concentrated mass.**  For a
   general member of either pencil, (0.4) says that its intersection with the
   selected exceptional component is \(A\), respectively \(C\).  Noether's
   blowup formula transports these numbers into sums of ordinary
   multiplicities along the unique contact chains:

   \[
   A=m_{f,0}+m_{f,1}+\cdots,qquad
   C=m_{g,0}+m_{g,1}+\cdots.                           \tag{0.6}
   \]

   The denominator transforms decide exactly which prefix consists of pencil
   base points.  KPC is the extreme assertion that each sum in (0.6) is
   concentrated in its first summand and that the two concentrations occur at
   the same point.

4. The concentration step is genuinely global.  Section 5 gives a Laurent
   Jacobian pair with \([P,Q]=-3/2\), the exact paired face
   \(R^2,R^3\), a nonzero marked root, and weak denominator orders \(2,3\),
   but its ordinary weak-ideal orders are \(1,2\).  Its contact vectors are
   \((1,1)\) and \((2,1)\).  This is not a polynomial Keller counterexample
   and is not asserted to be a full certified Corollary-7.4 occurrence.  It
   proves that no argument using only (0.2), both denominator capacities, and
   the local cleared Jacobian equation can establish KPC.  A proof must use
   polynomial origin and/or the whole eligible-prefix rigidity.

5. Assuming KPC, the no-double-counting *identity* problem has a canonical
   solution: quotient occurrences by equality of their infinitely-near point
   IDs, not by root-token equality.  What remains for PCC is the irreducible
   quantitative statement **CONJECTURE PFE**:

   \[
   \sum_p\left(\max_{\omega\mapsto p}q_\omega t_\omega\right)^2
   \ge B^2-1.                                         \tag{PFE}
   \]

   Here the forest must be all-root and occurrence-complete.  Neither
   Corollary 7.4 nor the present flag theorem proves this quadratic energy
   bound.  Section 8 records the exact square loss under contact splitting and
   shows why linear packet conservation cannot substitute for PFE.

Accordingly, **WTC-1 remains CONJECTURE**, but its geometric residual has
shrunk from four named conjectures to the single, necessary-and-sufficient
global concentration lemma KPC.  If one replaces WTC-1 by the correct
vector-valued transport, the flag/contact-chain theorem below is proved.

---

## 1. Exact local and valuative objects

Let \(k\) be algebraically closed of characteristic zero and
\(K=k(\mathbf P^2)=k(x,y)\).  A certified packet includes:

- the exact original pair and four projective sections
  \(F,Z^d,G,Z^e\);
- an exact Laurent cut prefix, including generator changes;
- a primitive weight \(w\), its GGV integer \(q\), and the common core in
  (0.2); and
- a nonzero selected root, or the full conjugate orbit of that root on an
  \(L^{(l)}\)-chart.

The nonzero-root qualification is the one used by the Section-4 certificates:
the zero-root case changes the starting point of the face and is rejected or
re-certified as a different packet.

### 1.1 The flag valuation of a root

First work in an integral chart.  Orient the primitive weight so that its
selected face is the minimum face of a divisorial valuation \(\nu\).  On a
regular toric realization let \(E\) be the corresponding divisor and let
\(z\) be a coordinate on its dense torus.  If \(H\in K^*\), divide its pullback
by a local equation of \(E\) to the power \(\nu(H)\), then restrict to \(E\).
Denote the resulting nonzero residue rational function by
\(\operatorname{res}_\nu(H)\).  At the marked root \(z=\lambda\), define

\[
 \widehat\nu_\lambda(H)=
 \left(\nu(H),
 \operatorname{ord}_{z=\lambda}
      \operatorname{res}_\nu(H)\right)\in\mathbf Z^2_{\rm lex}. \tag{1.1}
\]

This is the composite valuation of the divisorial valuation \(\nu\) and the
discrete valuation of its residue field at \(\lambda\).  Coordinate changes on
\(E\) replace \(z-\lambda\) by a unit times another local parameter, so (1.1)
does not depend on the displayed root coordinate.

The leading form in (0.2) is precisely an associated-graded residue.  Thus,
if \(\widetilde R\) has marked-root multiplicity \(t\),

\[
 \operatorname{ord}_{\lambda}
   \operatorname{res}_\nu(P)=q\alpha t,qquad
 \operatorname{ord}_{\lambda}
   \operatorname{res}_\nu(Q)=q\beta t.                \tag{1.2}
\]

The official statement of GGV Corollary 7.4 promises a power leading form;
the paired same-core version used here is the simultaneous calculation in the
proof of Corollary 7.2, as proved in `xmodel/sol-wtc1.md` Theorem 2.1.  Source:
[Guccione--Guccione--Valqui, arXiv:1401.1784v3, Corollary 7.4](https://arxiv.org/html/1401.1784v3#S7.Thmtheorem4).

### 1.2 Fractional charts

For an \(L^{(l)}\)-packet, let \(K_l/K\) be the finite Kummer extension used
by the certified prefix.  Construct (1.1) upstairs and take the entire
transported deck orbit.  Restriction to \(K\) gives a rank-two valuation after
normalizing the first value group.  All members of one deck orbit have the
same center on the quotient normalization.

There is no hidden factor of \(l\) in the tangential root order.  Before
conjugating by the prefix, the deck group acts on the residue coordinate by a
character, \(z\mapsto\chi(\zeta)z\).  If a group element stabilizes a nonzero
root \(\lambda\), then \(\chi(\zeta)=1\), so it also acts trivially on the
tangential parameter \(z-\lambda\).  Conjugating the action by the exact cut
prefix preserves this inertia statement.  Normal ramification changes the
normal/divisorial normalization, but it does not multiply or divide the
second entry in (1.1).  Consequently the descended root order is still \(t\).

If a future certificate permits a root with nontrivial tangential inertia,
the correct packet integer is the *descended* residue order, not the upstairs
token \(t\).  Such a certificate is outside the nonzero-root convention used
here and must not silently use (0.1).

---

## 2. Canonical flag-to-point transport

### Theorem 2.1 — canonical packet flag and proximity path (**PROVED**)

Let a certified paired packet retain the data listed in §1.  Then it
determines canonically:

1. a proper or infinitely-near point \(p_\omega\) over the original
   \(\mathbf P^2\);
2. the finite sequence of ordinary point blowups from \(\mathbf P^2\) to
   \(p_\omega\); and
3. the immediate proximity parent or parents of \(p_\omega\).

The result is independent of a regular fan, a graph resolution of the cut
word, a Kummer presentation, a root coordinate, and an allowed change of
pencil generator.  Two packet presentations give the same infinitely-near
point if and only if their finite point sequences agree.  Equivalently, their
terminal centers agree on a common carrier model on which the relevant
predecessor divisors have been realized and the terminal point has not yet
been blown up.

#### Proof

An integral Laurent cut is an automorphism of the function field.  Compose
the valuation (1.1) with the inverse of the exact cut prefix.  This gives a
rank-two valuation of the original field \(K\).  In the fractional case use
the restriction constructed in §1.2.  Thus in all cases the packet produces
one intrinsic valuation of \(K\), not merely a coordinate root token.

Every divisorial valuation of the function field of a smooth surface is
obtained by a finite sequence of point blowups.  Concretely here, insert the
primitive weight ray by the Euclidean regular subdivision; every inserted ray
is a point blowup.  The first component of (1.1) is realized by a prime
divisor \(E\), and the second component is the closed point on \(E\) selected
by the residue root.  If the cut prefix has indeterminacies, resolve its graph
and then take the center of the pulled-back valuation.  This construction uses
the projection to the original plane automatically, because the valuation is
already a valuation of its function field.

The valuative criterion of properness gives a unique center on every proper
model.  Given two fan or graph realizations of the same packet, pass to a
common regular carrier on which its divisorial component is present but its
selected residue point has not yet been blown up.  Their displayed roots have
the same center there because they define the same flag valuation.  The
minimal sequence of centers needed to reach that divisor, followed by the
residue point, is therefore independent of the realization.  Conversely,
different terminal centers on such a carrier give different point IDs.

At the final point, one or two exceptional components pass through the
center.  Their creators are, by definition, the immediate proximity parent or
parents.  They are read from the canonical point-blowup sequence.  A nonzero
toric residue root is away from the toric fixed points and is therefore a
free point on that toric realization; a later graph or quotient presentation
may display the same point differently, but the common-model definition also
covers satellite points.  Pencil-generator changes do not change either
two-generated base ideal and hence do not change the valuation center.
\(\square\)

### Corollary 2.2 — mathematical WTC-CHART and WTC-ID (**PROVED**, with an
interface rider)

The existence, descent, choice-independence, center naming, and proximity
parts called WTC-CHART and WTC-ID in the first round are consequences of
Theorem 2.1.  Successive occurrences are compared by their point IDs:

- identical terminal point sequences mean the same center;
- a proper extension of the point sequence means a distinct successor; and
- the proximity edges in the extension prove its ancestry.

This is a theorem about a *certified exact prefix*.  The current support-only
Section-4 state does not store all the maps needed to compute (1.1), so the
existing implementation cannot emit the point ID merely by invoking this
theorem.  That is an interface/certificate omission, not a remaining
existence theorem.

---

## 3. The one residual local assertion

Let \(Y\) be a regular realization of the canonical point and use completed
parameters

\[
 \widehat{\mathcal O}_{Y,p}=k[[x,r]],\qquad
 E=(x=0),\qquad \mathfrak m=(x,r).                     \tag{3.1}
\]

Pull back all four projective sections and remove, separately for the two
pencils, their full height-one gcds.  Keep the packet-designated numerator
generators.  The weak ideals are (0.3).  The associated-graded calculation in
§1 gives (0.4), after absorbing tangential units.

### Lemma 3.1 — packet boundary orders cap ordinary orders (**PROVED**)

For the two weak ideals,

\[
 \operatorname{ord}_{\mathfrak m} I_f\le A,qquad
 \operatorname{ord}_{\mathfrak m} I_g\le C.           \tag{3.2}
\]

Moreover

\[
 \begin{aligned}
 \operatorname{ord}_{\mathfrak m} I_f=A
   &\Longleftrightarrow I_f\subseteq\mathfrak m^A,\\
 \operatorname{ord}_{\mathfrak m} I_g=C
   &\Longleftrightarrow I_g\subseteq\mathfrak m^C.
 \end{aligned}                                        \tag{3.3}
\]

#### Proof

The restriction \(A_f(0,r)=u_f(r)r^A\) contains the monomial \(r^A\), so
\(\operatorname{ord}A_f\le A\), and the ideal order is no greater than the
order of either generator.  This proves the first inequality; the second is
identical.  An ideal is contained in \(\mathfrak m^N\) exactly when both of
its generators have order at least \(N\).  Together with the upper bounds,
this is equivalent to equality. \(\square\)

Writing

\[
 A_f=\sum_{j\ge0}x^ja_j(r),\qquad
 A_g=\sum_{j\ge0}x^jc_j(r),                            \tag{3.4}
\]

KPC is equivalently the finite collection

\[
 \begin{array}{ll}
 \operatorname{ord}_r a_j\ge A-j &(0\le j<A),\\
 \operatorname{ord}B_f\ge A,&\\[1mm]
 \operatorname{ord}_r c_j\ge C-j &(0\le j<C),\\
 \operatorname{ord}B_g\ge C.&
 \end{array}                                          \tag{3.5}
\]

Thus (KPC) is exactly the old transverse-numerator ladders plus the two
denominator capacities, expressed invariantly as orders of the *ideals* whose
point-basis coefficients WTC needs.

### Theorem 3.2 — WTC-1 is equivalent to KPC (**PROVED**)

For certified packets with exact prefix data, WTC-1, including its predicted
ordinary mobile multiplicities and proximity output, holds for every packet
if and only if KPC holds for every packet.

#### Proof

Theorem 2.1 supplies the named point and its proximity path, while (0.4)
supplies the upper bounds (3.2).  If KPC holds, Lemma 3.1 gives (0.5).  Since
\(A,C>0\), all four local generators vanish.  The full height-one gcd has
already been removed; in the two-dimensional regular UFD a gcd-free
two-generated ideal whose generators both vanish is not invertible.  Hence
the point is a base point of both pencils.  If any ancestor on its path were
not a base point, pullback past that ancestor would remain invertible, a
contradiction.  The path therefore survives in the minimal simultaneous base
cluster, and its point-basis coefficients are

\[
 R_p=A=\alpha T,qquad S_p=C=\beta T,qquad h_p=T.      \tag{3.6}
\]

Theorem 2.1 supplies choice-independence and successor comparison.

Conversely, WTC gives the equalities in (3.6).  Lemma 3.1 then gives the two
ideal containments in KPC. \(\square\)

This is not a renaming of four gaps.  It removes the standard birational and
identity pieces from the conjectural perimeter and leaves one exact assertion
about the order filtration of two specified local ideals.

---

## 4. What is provable without concentration

The correct unconditional geometric meaning of (0.4) is contact with the
exceptional divisor.

### Theorem 4.1 — weighted-to-contact-chain transport (**PROVED**)

Let \(I=(A,B)\subset k[[x,r]]\) be one of the two weak pencil ideals at the
canonical packet point.  Assume

\[
 E=(x=0),\qquad A(0,r)=u(r)r^N,qquad u(0)\ne0,        \tag{4.1}
\]

and let \(H_c=A-cB\) be a general pencil member.

1. If \(B|_E=0\), then
   \[
   I_p(H_c,E)=N.                                      \tag{4.2}
   \]
2. Blow up successively the unique intersection of the strict transforms of
   \(H_c\) and \(E\), stopping when they separate.  If \(p_0=p,p_1,\ldots,p_s\)
   are those points and \(m_i\) is the ordinary multiplicity of the strict
   transform of \(H_c\) at \(p_i\), then
   \[
   N=\sum_{i=0}^s m_i.                                \tag{4.3}
   \]
3. The transforms of \(B\) decide exactly which initial segment of this
   contact chain is independent of \(c\) and belongs to the pencil base
   cluster.  On that segment, \(m_i\) is the point-basis coefficient of the
   pencil.  If the denominator remains nonunit along the whole contact chain,
   the whole sum (4.3) consists of base-point coefficients.

#### Proof

Restricting \(H_c\) to \(E\) kills \(B\) and leaves \(u(r)r^N\), proving
(4.2).  For one blowup at a point of two curves with no common component,
Noether's formula is

\[
 I_p(H_c,E)=m_p(H_c)m_p(E)
       +\sum_{q\mapsto p}I_q(H_c',E').                \tag{4.4}
\]

Here \(E\) is smooth, so \(m_p(E)=1\), and only the unique point where its
strict transform meets the new exceptional divisor can contribute to the
remaining intersection with \(E'\).  Iterating (4.4) until separation gives
(4.3).

At a point where both transformed generators vanish, a general combination
has the generic ideal order, so \(m_i\) is the mobile point-basis coefficient.
If the transformed denominator is a unit, the pencil is already generated by
a unit there and that point is not a base point; any remaining contact belongs
only to the selected numerator member.  Thus the exact denominator transforms
select the base prefix. \(\square\)

### Corollary 4.2 — proved vector-valued WTC, with exact capacity data

For the two packet components, the canonical flag and the four actual weak
generators determine two contact chains and their ordinary multiplicity
vectors.  When the denominators survive the full chains,

\[
 \sum_iR_{p_i}=\alpha T,qquad
 \sum_jS_{q_j}=\beta T.                               \tag{4.5}
\]

This is the precise proved form of the proposed WTC-VEC for one occurrence.
It includes point names and proximity paths.  It does **not** say that the two
chains coincide, that their entries are pointwise in ratio \(\alpha:\beta\),
or that either vector has one nonzero entry.  Those are exactly the kinds of
extra rigidity needed for PCC's quadratic mass.

### Corollary 4.3 — KPC is maximal contact concentration

Under KPC, \(m_0=N\) in (4.3), so every later term is zero.  Conversely, if
the full contact number is carried by the first mobile base coefficient, then
the corresponding KPC containment holds.  Thus WTC-1 does not merely
transport weight; it asserts the extremal, no-splitting case of Noether's
contact identity.

---

## 5. Exact separation example

This section strengthens the diagnostic examples in the first round.  It
keeps a constant Laurent Jacobian, the paired same-core leading powers, a
nonzero root, and both denominator capacities simultaneously.

### Proposition 5.1 — paired Laurent Jacobian packet data do not force KPC
(**PROVED**)

In \(k[u^{\pm1},v]\), set

\[
 R=u^3v-u^{-1},\qquad
 P=R^2+u^{-1},\qquad
 Q=R^3+\frac32u^{-1}R.                                \tag{5.1}
\]

Then

\[
 [P,Q]=-\frac32.                                      \tag{5.2}
\]

For \(w=(-1,4)\),

\[
 v_w(P)=2,\quad v_w(Q)=3,\qquad
 \ell_w(P)=R^2,\quad\ell_w(Q)=R^3.                   \tag{5.3}
\]

Also

\[
 \frac{v_{1,1}(P)}{v_{1,1}(Q)}=\frac8{12}=\frac23,
 \qquad
 \frac{v_{0,1}(P)}{v_{0,1}(Q)}=\frac23.              \tag{5.4}
\]

On the regular root chart

\[
 x=u,qquad r=u^4v-1,                                 \tag{5.5}
\]

the marked factor of \(R=u^{-1}r\) is the nonzero residue root
\(u^4v=1\).  The rational functions and their weak pencil ideals are

\[
 \begin{aligned}
 P&=\frac{r^2+x}{x^2},& I_f&=(r^2+x,x^2),\\
 Q&=\frac{r^3+\frac32xr}{x^3},&
 I_g&=(r^3+\tfrac32xr,x^3).                           \tag{5.6}
 \end{aligned}
\]

Their boundary restrictions are \(r^2,r^3\), and the denominator orders are
exactly \(2,3\), but

\[
 \operatorname{ord}I_f=1,qquad
 \operatorname{ord}I_g=2.                             \tag{5.7}
\]

After blowing up in the common tangent direction, their \(E\)-contact
base-prefix vectors are respectively

\[
 (1,1),\qquad(2,1),                                   \tag{5.8}
\]

whose sums are \(2,3\).

#### Proof

Expanding (5.1) gives

\[
\begin{aligned}
P={}&u^6v^2-2u^2v+u^{-2}+u^{-1},\\
Q={}&u^9v^3-3u^5v^2+3uv-u^{-3}
     +\frac32u^2v-\frac32u^{-2}.
\end{aligned}                                         \tag{5.9}
\]

Direct differentiation gives (5.2).  Every term of \(R\) has \(w\)-degree
one.  The extra term of \(P\) has degree one rather than two, and the extra
term of \(Q\) has degree two rather than three; this proves (5.3).  The
maximum ordinary and \(v\)-degrees in (5.9) give (5.4).  Substitution (5.5)
gives (5.6), from which (5.7) is immediate.

For the first ideal, use the blowup chart \(x=rx_1\):

\[
 (r^2+x,x^2)=r\,(r+x_1,rx_1^2),                      \tag{5.10}
\]

so the weak orders on the contact with the strict transform of \(E\) are
\(1\) and then \(1\).  For the second,

\[
 (r^3+\tfrac32xr,x^3)
 =r^2\,(r+\tfrac32x_1,rx_1^3),                       \tag{5.11}
\]

so they are \(2\) and then \(1\).  At the second common point the two
numerator tangents are \(r+x_1=0\) and \(r+\frac32x_1=0\); hence any further
base points lie over distinct points of the next exceptional divisor.  This
proves (5.8) and shows that there is no later common base center. \(\square\)

At the two common base points in this example,

\[
 \min\!\left(\left\lfloor\frac{R_p}{2}\right\rfloor,
              \left\lfloor\frac{S_p}{3}\right\rfloor\right)=0, \tag{5.12}
\]

so the predicted packet weight \(T=1\) produces no PCC unit.  Further centers
belong to at most one pencil cluster and also have \(h_p=0\).

### Scope of the example

Proposition 5.1 is **not** a counterexample to the plane Jacobian conjecture,
to PCC, or to KPC as stated.  The pair is Laurent rather than polynomial, has
no claimed Sigray/minimal-pair provenance, and its displayed common-power edge
is not claimed to be an eligible *output occurrence* of the full Corollary-7.4
prefix (in particular, the starting-direction/F-data have not been supplied).

It is decisive for the reduction perimeter: it satisfies the paired power,
both denominator capacities, and even the constant Laurent Jacobian.  Hence
KPC must use a hypothesis absent from that local package—most plausibly the
polynomial origin together with the whole eligible direction/cut prefix.
Repeating the cleared-Jacobian coefficient induction of the first round
without that global input cannot prove KPC.

### Proposition 5.2 — a general formal monomial-Jacobian separation family
(**PROVED**)

Let \(2\le\alpha<\beta\), \(T,L,k\in\mathbf N\), \(L\ge T\), and
\(k<\alpha T\).  Put

\[
 f=\frac{r^{\alpha T}+x^k}{x^{\alpha L}},\qquad
 g=\frac{r^{\beta T}+(\beta/\alpha)x^k
                   r^{(\beta-\alpha)T}}{x^{\beta L}}. \tag{5.13}
\]

Then the boundary packet and denominator capacities are exactly the predicted
ones, while

\[
 \operatorname{ord}I_f=k<\alpha T,qquad
 \operatorname{ord}I_g=k+(\beta-\alpha)T<\beta T.     \tag{5.14}
\]

Nevertheless the pulled-back Jacobian is the single boundary monomial

\[
 [f,g]=
 \frac{\beta}{\alpha}(\beta-\alpha)T(k-\alpha L)
 x^{2k-(\alpha+\beta)L-1}
 r^{(\beta-\alpha)T-1}.                               \tag{5.15}
\]

#### Proof

The order assertions are immediate from \(L\ge T\) and \(k<\alpha T\).
Differentiate (5.13) after writing the two numerators as \(A,G\).  In the
cleared bracket

\[
 x(A_xG_r-A_rG_x)+\beta L A_rG-\alpha LAG_r,          \tag{5.16}
\]

the pure \(r^{(\alpha+\beta)T-1}\) terms cancel because the exponent and
denominator ratios are both \(\alpha:\beta\).  The
\(x^kr^{\beta T-1}\) terms cancel because the coefficient in (5.13) is
\(\beta/\alpha\).  The sole remaining term is (5.15). \(\square\)

The specialization \((\alpha,\beta,T,L,k)=(2,3,1,1,1)\) has no \(r\)-factor
on the right and becomes Proposition 5.1 after the root chart (5.5).

---

## 6. The minimal remaining proof target

KPC is deliberately scoped to *actual polynomial-origin packets*.  An
equivalent operational statement is:

> **CONJECTURE KPC (coefficient form).**  Let \(j\) be the first index for
> which one of the divisibilities in (3.5) fails, or let a denominator order
> be the first capacity failure.  For a packet produced by the exact eligible
> Corollary-7.4 prefix of the selected polynomial Keller pair, no such first
> failure exists.

The separation family shows what a proof must rule out.  Its two weak
numerators share the required boundary powers; their low transverse jets are
tuned so that all nonmonomial terms in the cleared Jacobian cancel, leaving
the allowed boundary monomial.  Therefore “take the first failed jet and read
off a contradiction from \(df\wedge dg\)” is incomplete: the common
reparametrization/contact-splitting alternative really occurs.

There are two plausible sources of the missing contradiction.

1. **Eligible-prefix saturation.**  A failed ordinary divisibility creates a
   new Newton side after the selected root cut.  Prove that this side still
   lies in the Corollary-7.4 eligible interval, or is the next certified cut,
   and that its required common-power structure is incompatible with the
   first failure.  This must be a theorem about the *entire prefix*, since
   Proposition 5.1 shows that one face is insufficient.

2. **Polynomial-origin/canonical-divisor compatibility.**  Use the exact
   divisor of the pulled-back affine form \(dx\wedge dy\), not merely the fact
   that its local coefficient is a monomial.  The valuations of the four
   projective sections, the discrepancy coefficients, and the degree
   identities \(d=B\alpha,e=B\beta\) may forbid the separation model on a
   point lying in the polynomial pencil cluster.

No theorem in the repository supplies either step.  FC5, the scalar depth
invariant, NF-M, and the censuses forget precisely the transverse jets and
canonical point ID needed here.  Accordingly KPC is labelled **CONJECTURE**.

The strongest safe theorem is now:

### Theorem 6.1 — exact WTC reduction (**PROVED**)

For the selected polynomial pair and exact paired packets:

\[
 \boxed{\text{WTC-1}\quad\Longleftrightarrow\quad\text{KPC}.}      \tag{6.1}
\]

Without KPC, every packet still has a canonical point/proximity ID and exact
contact-chain transport as in Theorems 2.1 and 4.1.

---

## 7. Canonical no-double-counting after KPC

Let \(\Omega\) be the factor-expanded all-root occurrence forest, and let

\[
 w(\omega)=q_\omega t_\omega.                         \tag{7.1}
\]

Theorem 2.1 assigns to every occurrence an intrinsic infinitely-near point
ID.  It is useful to make the equivalence relation explicit.

### Definition 7.1 — point-ID equivalence

Write \(\omega\sim\omega'\) if their finite Enriques point sequences
terminate at the same infinitely-near point (and therefore have the same
proximity relations).  Equivalently, on a common carrier model realizing the
required predecessor divisors and not yet blowing up either terminal point,
the two flags have the same closed center.

Equality of bare root scalars, Laurent factors, or divisorial valuations is
neither necessary nor sufficient.  At a satellite point two divisor-based
presentations can name the same closed center; conversely, the same root
scalar in two unrelated charts can name different points.

### Proposition 7.2 — identity/no-double-counting relation (**PROVED**)

The relation in Definition 7.1 is a canonical equivalence relation,
independent of all packet chart choices.  A next-cut occurrence is a new
center exactly when its Enriques sequence properly extends the old sequence;
the extension records its proximity edge or edges.

#### Proof

Equality of finite infinitely-near point sequences is an equivalence
relation.  A common carrier model converts that equality into equality of
terminal closed centers.  Blowing up a terminal point replaces it by later
points, so equality is deliberately defined by the finite sequence rather
than by centers on every higher refinement.  Theorem 2.1 proves that changing
a packet presentation does not change its sequence. \(\square\)

Thus the *bookkeeping* half of PCC-COVER is no longer conjectural at theorem
level.  It still needs an implementation record if the Section-4 engine is to
compute it.

Assume KPC.  Let \(\kappa:\Omega\to K_f\cap K_g\) be the resulting point map
and define conservatively

\[
 c_p=\max\bigl(\{w(\omega):\kappa(\omega)=p\}\cup\{0\}\bigr).     \tag{7.2}
\]

Then

\[
 c_p\le
 \min\!\left(\left\lfloor\frac{R_p}{\alpha}\right\rfloor,
              \left\lfloor\frac{S_p}{\beta}\right\rfloor\right)
 =h_p.                                                \tag{7.3}
\]

In the exact-equality form of KPC, two occurrences at the same center must in
fact have the same weight; the maximum convention remains the safe definition
for duplicated certificates and for any future lower-bound version of WTC.

---

## 8. The exact PCC remainder and an attempted proof

### CONJECTURE PFE — packet-flag energy coverage

For the selected polynomial Keller pair, the all-root occurrence forest is
complete, every occurrence has the certified provenance required in §1, and
the conservative point weights (7.2) satisfy

\[
 \boxed{\sum_pc_p^2\ge B^2-1.}                        \tag{PFE}
\]

KPC + PFE imply PCC term by term via (7.3), and hence imply
\(\operatorname{td}\le\alpha\beta\).  PFE is the exact surviving content of
the previous PCC-COVER after the point-identity/no-double-counting relation is
made canonical.

If the maximum convention is too strong, it can be replaced only by an
explicit local packing function \(c_p^{\rm pack}\le h_p\), proved from
pairwise-coprime ordinary initial factors.  Merely choosing unspecified
\(c_p\le h_p\) with a large square sum is PCC itself and is circular.

### 8.1 Contact splitting has the wrong quadratic sign

Suppose, optimistically, that one packet of weight \(T\) has synchronized
proportional contact vectors

\[
 R_{p_i}=\alpha u_i,qquad S_{p_i}=\beta u_i,qquad
 \sum_i u_i=T.                                        \tag{8.1}
\]

Then its actual PCC mass is

\[
 \sum_i u_i^2
 =T^2-2\sum_{i<j}u_i u_j\le T^2,                     \tag{8.2}
\]

with equality if and only if the packet is concentrated at one center.  Thus
Noether contact conservation gives a *linear* identity, while PCC needs the
opposite, maximally concentrated quadratic behavior.  Proximity by itself
does not repair the sign; it records the splitting responsible for the loss.

Proposition 5.1 is worse than synchronized splitting: the vectors \((1,1)\)
and \((2,1)\) are not pointwise proportional, and the floor meet loses the
entire unit packet.

### 8.2 A sharp conditional obstruction to linear root enumeration

Suppose an all-root theorem supplied positive integer weights
\(T_1,\ldots,T_s\) with only the linear conservation law

\[
 \sum_iT_i=B.                                         \tag{8.3}
\]

If no weight equals \(B\), convexity gives

\[
 \sum_iT_i^2\le(B-1)^2+1
 =B^2-2B+2<B^2-1\qquad(B\ge2).                        \tag{8.4}
\]

Hence enumerating all roots of a degree-\(B\) core and conserving their total
multiplicity cannot prove PFE unless one root already carries all \(B\), or
additional levels create certified mass not governed by (8.3).  This is why
“all roots” is not yet a coverage theorem.

### 8.3 What a proof of PFE must add

The attempted proof stops at a precise place.  A successful argument needs a
global telescope that simultaneously accounts for:

1. creation of new packet weight at later eligible cuts;
2. loss under repeated presentations, removed by Definition 7.1;
3. loss under contact splitting, quantified by (8.2); and
4. normalized divergence of the two pencil vectors, which can erase floors as
   in Proposition 5.1.

Equivalently, it needs to prove that all splitting and divergence defects
leave at most one unit of residual point-basis energy:

\[
 B^2-\sum_pc_p^2\le1.                                 \tag{8.5}
\]

The GGV divisibility chain controls which powers may occur, but no banked
identity relates its \(q_j,t_j\) to the quadratic defect in (8.5).  FC5 and the
censuses provide scalar or frequency data after forgetting the point IDs and
therefore cannot supply this telescope.  PFE remains **CONJECTURE**.

A normalized multi-Rees/b-divisor approach may be better aligned with (8.5):
the flag theorem already places packets on canonical Rees/valuation data, and
one could seek an intersection inequality for the two entire cluster vectors
instead of imposing KPC packet by packet.  That would bypass one-center
concentration, but the required quadratic inequality is new and is not proved
here.

---

## 9. Exact arithmetic reproduction

The following pure-Python calculation verifies the fraction arithmetic in
Proposition 5.1.  A Laurent polynomial is a dictionary
`(u_exponent,v_exponent) -> Fraction`.

```python
from fractions import Fraction as F

def add(A, B):
    C = A.copy()
    for m, c in B.items():
        C[m] = C.get(m, F(0)) + c
    return {m: c for m, c in C.items() if c}

def mul(A, B):
    C = {}
    for (i, j), a in A.items():
        for (k, l), b in B.items():
            C[(i+k, j+l)] = C.get((i+k, j+l), F(0)) + a*b
    return {m: c for m, c in C.items() if c}

def der(A, z):
    C = {}
    for (i, j), a in A.items():
        n = (i, j)[z]
        if n:
            m = (i-1, j) if z == 0 else (i, j-1)
            C[m] = a*n
    return C

def scale(A, c):
    return {m: c*a for m, a in A.items() if c*a}

def bracket(A, B):
    return add(mul(der(A, 0), der(B, 1)),
               scale(mul(der(A, 1), der(B, 0)), F(-1)))

P = {(6,2):F(1), (2,1):F(-2), (-2,0):F(1), (-1,0):F(1)}
Q = {(9,3):F(1), (5,2):F(-3), (1,1):F(3), (-3,0):F(-1),
     (2,1):F(3,2), (-2,0):F(-3,2)}

print(bracket(P, Q))
# {(0, 0): Fraction(-3, 2)}
```

The local orders are

```text
ord(r^2+x, x^2)             = 1
ord(r^3+(3/2)xr, x^3)       = 2
predicted packet orders      = 2, 3
contact-vector sums          = 1+1, 2+1
```

All computations are over \(\mathbf Q\); no modular or floating-point step is
used.

---

## 10. Final dependency ledger

| assertion | status after round 2 |
|---|---|
| paired same-core Corollary-7.4 powers | **PROVED** in `sol-wtc1.md` §2 |
| integral projective lift / boundary interpretation | **PROVED** in `sol-wtc1.md` §3 |
| intrinsic packet flag over the original plane | **PROVED**, Theorem 2.1 |
| fractional nonzero-root orbit descent | **PROVED**, §1.2 |
| chart-choice-independent center ID | **PROVED**, Theorem 2.1 |
| proximity parents and successor comparison | **PROVED**, Corollary 2.2 / Proposition 7.2 |
| boundary packet transports to contact number \((\alpha T,\beta T)\) | **PROVED**, Theorem 4.1 |
| contact number transports to exact multiplicity vectors when denominator transforms survive | **PROVED**, Corollary 4.2 |
| one-center ordinary multiplicities \((\alpha T,\beta T)\) | **CONJECTURE KPC** |
| WTC-1 | **equivalent to KPC**, Theorem 3.2 |
| same-power + denominators + local Jacobian imply KPC | **FALSE as a formal/local implication**, Proposition 5.1 |
| canonical occurrence no-double-counting relation | **PROVED**, Proposition 7.2 |
| all-root occurrence completeness and square mass \(\ge B^2-1\) | **CONJECTURE PFE** |
| PCC | **CONJECTURE; follows from KPC + PFE** |
| `td <= alpha*beta` | **CONJECTURE; follows from PCC** |

The main mathematical advance is therefore exact but limited: the geometric
name/proximity problem is not the obstruction.  A Corollary-7.4 packet
canonically determines a flag and a contact flow.  The unproved leap is that a
polynomial Keller packet cannot distribute that flow.  KPC is the minimal
named lemma for that leap; PFE is the separate global quadratic-coverage
lemma.  Both remain labelled **CONJECTURE**.
