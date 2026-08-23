# WTC-1: from a Corollary-7.4 packet to an ordinary pencil center

**Date:** 2026-08-20  
**Scope:** the first missing packet-to-point-basis arrow isolated in
`xmodel/sol-pcc-orbits.md` §0.2/§2.2.  
**Status:** **WTC-1 is not proved.**  Its paired-power input and its local
commutative-algebra output are proved below.  The remaining geometric content
is reduced to four explicit sublemmas, all labelled **CONJECTURE**.

## 0. Verdict

There are two readings of WTC-1, and they must be separated.

1. On the **retained-data reading**, the stored Laurent face/root fields
   together with the two transformed denominator sections determine ordinary
   mobile multiplicities.  After the actual Keller pair and its off-face
   coefficients are forgotten, this implication is false as a matter of
   local algebra: the retained fields fix only the restriction to one
   exceptional divisor, while transverse numerator jets can lower the
   ordinary order.  Section 5 gives two local systems with the same support,
   the same formal packet shadow, and the same denominator, but different
   ordinary pencil multiplicities.  They are not claimed to satisfy the
   Corollary-7.4/Keller hypotheses; they prove that no formal manipulation of
   the presently banked face/support fields can establish WTC-1.

2. On the **Keller-geometric reading**, the actual Keller pair, its full four
   projective sections, and the cleared Jacobian identity may force the missing
   transverse divisibilities and denominator capacity.  That assertion is
   viable but unproved.  After the standard parts are removed, it is exactly
   the conjunction of:

   - **CONJECTURE WTC-CHART:** regular chart construction, fractional descent,
     and marked packet/root realization;
   - **CONJECTURE WTC-ID:** choice-independent center identity and
     cross-prefix functoriality;
   - **CONJECTURE WTC-ORD:** ordinary dominance of every transverse numerator
     coefficient; and
   - **CONJECTURE WTC-DEN:** enough residual order in both denominator
     sections.

Assuming those four statements, WTC-1 follows, in fact with the exact mobile
multiplicities

\[
R_p=q\alpha t,\qquad S_p=q\beta t,
\qquad h_p=qt,                                      \tag{0.1}
\]

not merely the lower bounds printed in `sol-pcc-orbits.md` (2.2).

The main positive correction is that the *paired* Corollary-7.4 packet is
already available.  Although Corollary 7.4 prints only
\(\ell(P)=R^{qm}\), the proof it invokes simultaneously writes the leading
forms of \(P\) and \(Q\) as powers of the same homogeneous element.  Thus
pair-packet extraction is not the gap.  The next formal gap is WTC-CHART; once
a compatible integral chart is supplied, the first local algebra gap is
passage from a weighted boundary restriction to an ordinary maximal-ideal
order.

The resulting status ledger is:

| assertion | status |
|---|---|
| same-root \((q\alpha,q\beta)\)-power packet | **PROVED** in §2 |
| rational projective lift of every integral Laurent cut | **PROVED** in §3 |
| weighted face becomes a boundary restriction on an integral toric chart | **PROVED** in §3 |
| generic pencil order is the order of its two-generator ideal | **PROVED** in §4 |
| exact transverse-divisibility criterion | **PROVED** in §4 |
| cut chart and marked root realize compatibly over the original plane, including fractional descent | **CONJECTURE WTC-CHART** |
| chart choices and successive occurrences have canonical center identities | **CONJECTURE WTC-ID** |
| Keller identity forces numerator transverse dominance | **CONJECTURE WTC-ORD** |
| both transformed denominators retain the packet capacity | **CONJECTURE WTC-DEN** |
| WTC-1 for every certified Keller packet | **CONJECTURE**, conditional theorem in §7 |
| all packets cover \(B^2-1\) without double counting | **CONJECTURE PCC-COVER**, §10 |

I rate the remaining WTC local dictionary **9/10**: WTC-CHART is largely
birational bookkeeping, but WTC-ORD/WTC-DEN are new uniform Keller statements.

---

## 1. Exact objects and a necessary wording repair

Let \(k\) be algebraically closed of characteristic zero, and let
\((f,g)\) be a Sigray-normalized nonautomorphic Keller pair of coprime type
\(2\leq\alpha<\beta\).  Write

\[
d=B\alpha,\qquad e=B\beta,
\]

and homogenize to sections

\[
F(X,Y,Z)=Z^df(X/Z,Y/Z),\qquad
G(X,Y,Z)=Z^eg(X/Z,Y/Z).
\]

The projective pencil ideal sheaves are

\[
\mathcal I_f=(F,Z^d),\qquad \mathcal I_g=(G,Z^e).       \tag{1.1}
\]

The phrase “complete ideal \((F,Z^d)\)” in the provisional WTC statement is
potentially misleading: a two-generated ideal need not be integrally closed.
Below, **full pencil ideal** means (1.1), including both generators.  Its local
integral closure has the same order and canonical base-point cluster, so one
may pass to the integral closure when using complete-ideal/point-basis
language.

Let \(\pi:X\to\mathbf P^2\) be the minimal simultaneous point resolution of
the two pencil maps.  For a proper or infinitely-near center \(p\), the
numbers \(R_p,S_p\) are the orders of the mobile strict transforms of *general*
pencil members immediately before \(p\) is blown up.  They are point-basis
coefficients.  They are not:

- orders of a selected special member;
- coefficients in the strict-exceptional basis;
- a Newton weight or a divisorial valuation; or
- Sigray pattern-factor multiplicities.

This is the convention fixed in `xmodel/sol-pcc-orbits.md:83-170`.

### 1.1 A formal packet

The repository currently has no formal two-pencil “Laurent factor packet.”
The closest stored object is the one-polynomial edge certificate at
`SECTION4-AUTOMATION.md:140-150`.  For WTC, define a **certified paired packet**
to be

\[
\mathfrak p=(\mathcal E,\omega,(\rho,\sigma),q,
             [\lambda],t,\widetilde R;\alpha,\beta),       \tag{1.2}
\]

where:

- \(\mathcal E\) identifies the original Keller pair and its exact
  Corollary-7.4 hypotheses;
- \(\omega\) is the Laurent cut prefix, before `T-final`;
- \((\rho,\sigma)\) is the certified direction and \(q\) is the GGV
  denominator from that certificate;
- \([\lambda]\) is the selected root, or its orbit under the deck action
  transported (conjugated) through the cut prefix when the homogeneous core
  lies in \(L^{(l)}\);
- \(t\) is the multiplicity of that nonmonomial root in \(\widetilde R\); for
  an \(L^{(l)}\)-packet this is initially an upstairs/core-root multiplicity,
  not a downstairs ordinary order; and
- after the component labels are sorted to \((\alpha,\beta)\),

\[
\ell(P)=\lambda_P\widetilde R^{q\alpha},\qquad
\ell(Q)=\lambda_Q\widetilde R^{q\beta}.                  \tag{1.3}
\]

At the chosen root, (1.3) predicts the two integers

\[
A:=q\alpha t,\qquad C:=q\beta t.                         \tag{1.4}
\]

Here \(t\) is a one-variable root multiplicity after a root chart has been
named.  Calling it an “ordinary order” before that point and its maximal ideal
exist would beg the WTC question.

The following three quantities also remain distinct throughout:

- the GGV cut integer
  \(q_h=v_{\rho_h,\sigma_h}(A_h)/\gcd(\rho_h+\sigma_h,
  v_{\rho_h,\sigma_h}(A_h))\);
- a Sigray pattern multiplicity \(b_i=M_i\); and
- the FC5 local pattern degree \(d_q\).

No banked theorem identifies them.  See
`SECTION4-AUTOMATION.md:154-165` and
`xmodel/sol-tdbound-review.md:320-347`.

---

## 2. Paired-packet extraction

### Theorem 2.1 — paired Corollary-7.4 power (**PROVED**)

Assume the exact hypotheses of Corollary 7.4 for coprime \(m,n>1\):
\(v_{1,1}(P)/v_{1,1}(Q)=v_{0,1}(P)/v_{0,1}(Q)=m/n\), the positive starting
direction, the proportional
normalized start points \((a/l,b)\) with \(b<a/l\), and
\(\operatorname{st}(F)=(p/q)(a/l,b)\), where \((p,q)=1\).  For every eligible
direction

\[
(\widetilde\rho,\widetilde\sigma)\le(\rho,\sigma)
  <(\rho_0,\sigma_0),
\]

there are \(\widetilde R_{\rho,\sigma}\in L^{(l)}\) and nonzero scalars
\(\lambda_P,\lambda_Q\) such that

\[
\ell_{\rho,\sigma}(P)=
 \lambda_P\widetilde R_{\rho,\sigma}^{qm},\qquad
\ell_{\rho,\sigma}(Q)=
 \lambda_Q\widetilde R_{\rho,\sigma}^{qn}.              \tag{2.1}
\]

Consequently, after fixing one dehomogenization, if a nonmonomial factor of
\(\widetilde R_{\rho,\sigma}\) has root multiplicity \(t\), the same residue
root occurs in the two leading forms with multiplicities \(qmt\) and \(qnt\).

#### Proof

Fix an eligible \((\rho,\sigma)\), abbreviate its leading-form operator by
\(\ell\), and write \(\widetilde R=\widetilde R_{\rho,\sigma}\).  Corollary
7.4 says to mimic the proof of Corollary 7.2.  In that proof,
Proposition 2.1(2b) is applied not merely to \(P\), but simultaneously to
\(G_0,G_1,P,Q\).  It produces one homogeneous \(R_0\), nonzero scalars
\(\gamma_i\), and exponents \(u_i\) with

\[
\ell(P)=\gamma_2R_0^{u_2},\qquad
\ell(Q)=\gamma_3R_0^{u_3}.                              \tag{2.2}
\]

The valuation vector in that proof is proportional to

\[
(rqm,\;rqm+sqm-ps,\;sqm,\;sqn).                         \tag{2.3}
\]

If

\[
\delta=\gcd(rqm,rqm+sqm-ps,sqm,sqn),
\]

then the proof computes

\[
\delta=\gcd(qm,s),\qquad \delta\mid s,                  \tag{2.4}
\]

and hence

\[
u_2=\frac{sqm}{\delta},\qquad
u_3=\frac{sqn}{\delta}.                                 \tag{2.5}
\]

Set \(\widetilde R=R_0^{s/\delta}\).  Equations (2.2)-(2.5) give
(2.1), with the scalars left outside the common core.  Over an algebraically
closed field one may also absorb either scalar into the corresponding printed
power, but doing so is unnecessary and can obscure that the same
\(\widetilde R\) serves both components.  Factoring \(\widetilde R\) proves
the last assertion. \(\square\)

The source is
[Guccione--Guccione--Valqui, Corollary 7.4 and the proof it invokes](https://arxiv.org/html/1401.1784v3#S7.Thmtheorem4).
The printed corollary states only the \(P\)-power; equations (2.2)-(2.5) are
visible in the proof of
[Corollary 7.2](https://arxiv.org/html/1401.1784v3#S7.Thmtheorem2), which
Corollary 7.4 explicitly says to mimic.

### Corollary 2.2 — the WTC input assumed in the selected-pair branch is
valid (**PROVED**)

For the globally minimal GGV pair selected by the hypotheses of
`TRANSPORT.md`, reorder the two output/component labels by that theorem's
determinant-one target rotation and denote the sorted multipliers by
\((\alpha,\beta)\).  Theorem 2.1 then gives exactly the paired input used at
`xmodel/sol-pcc-orbits.md:274-283` and
`xmodel/sol-tdbound-review.md:437-447`:

\[
\ell_{\rho,\sigma}(P)=\lambda_P\widetilde R_{\rho,\sigma}^{q\alpha},
\qquad
\ell_{\rho,\sigma}(Q)=\lambda_Q\widetilde R_{\rho,\sigma}^{q\beta}.
                                                               \tag{2.6}
\]

This repairs a small asymmetry in `SECTION4-AUTOMATION.md` R1, whose printed
certificate and implementation retain only the \(P\)-formula.  It does not
repair WTC: (2.6) is still weighted-face data.  Nor does it assert that an
arbitrary Sigray-normalized pair introduced abstractly in §1 has independently
been placed under Corollary 7.4; the conclusion is scoped to the selected GGV
pair and its transported component labels.

---

## 3. What can already be transported projectively

### Proposition 3.1 — one integral Laurent cut has an exact projective lift
(**PROVED**)

For \(K\geq1\) and \(\lambda\ne0\), the Laurent automorphism

\[
e_K(\lambda):(x,y)\longmapsto(x,y+\lambda x^{-K})       \tag{3.1}
\]

is induced on the affine torus by the birational projective map

\[
\Phi_{K,\lambda}[X:Y:Z]
=
[X^{K+1}:X^KY+\lambda Z^{K+1}:X^KZ].                   \tag{3.2}
\]

For the two pencils its four pullbacks are exactly

\[
F\circ\Phi_{K,\lambda},\quad (X^KZ)^d,\qquad
G\circ\Phi_{K,\lambda},\quad (X^KZ)^e.                 \tag{3.3}
\]

#### Proof

On the chart where the third coordinate in (3.2) is nonzero,

\[
\frac{X^{K+1}}{X^KZ}=\frac XZ=x,\qquad
\frac{X^KY+\lambda Z^{K+1}}{X^KZ}
=\frac YZ+\lambda\left(\frac ZX\right)^K
=y+\lambda x^{-K}.
\]

Pullback of the section \(Z^d\) is the \(d\)-th power of the third
coordinate, and likewise for \(e\), proving (3.3).  Since (3.1) has inverse
\(e_K(-\lambda)\) on the torus, (3.2) is birational.  The support of its base
scheme is the single point \([0:1:0]\); a birational map between smooth
projective surfaces is resolved by a finite sequence of point blowups.
\(\square\)

The source swap in `SECTION4-AUTOMATION.md:124-138` is a projective source
automorphism.  `T-const` is instead a linear change of pencil generators and
does not change the pencil base ideal.  Therefore a finite integral cut word
\(\omega\), before `T-final`, has a rational projective composition
\(\Phi_\omega\), a graph resolution by point blowups, and exact denominator
pullbacks

\[
(Z\circ\Phi_\omega)^d,\qquad (Z\circ\Phi_\omega)^e.     \tag{3.4}
\]

More precisely, take a smooth graph resolution with morphisms
\(s_\omega:Y\to\mathbf P^2_{\rm cut}\) and
\(t_\omega:Y\to\mathbf P^2_{\rm original}\), satisfying
\(t_\omega=\Phi_\omega\circ s_\omega\) as rational maps.  The four regular
sections on \(Y\) are pulled back by \(t_\omega\).  In §3.3, \(\rho\) denotes
this morphism to the original projective plane.  The two projections have
different point-blowup factorizations.  Only a factorization of
\(t_\omega\)—the projection to the plane carrying the original pencils—may
be used for pencil-center ancestry and proximity.  Domain-side graph blowups
alone do not supply the WTC center dictionary.

This is elementary but absent from the current Section-4 state
`(SuppP,SuppQ,Consts,Certs,Log)` at
`SECTION4-AUTOMATION.md:113-150`; `lib/reduce4.py` consequently has no
projective denominator object.

### Proposition 3.2 — a weighted face is a boundary restriction
(**PROVED**, integral toric chart)

Let \(w=(\rho,\sigma)\) be a primitive integral GGV direction.  GGV's
\(v_w\) uses the maximum convention.  Orient the toric cocharacter
\(\eta\) so that the selected maximal \(w\)-face is the *minimal*
\(\eta\)-face; thus one may take \(\eta=-w\).  Choose an adjacent primitive
cocharacter \(\eta'\) with determinant \(\pm1\), and write the toric chart on
the dense torus as

\[
x=u^{\eta_1}v^{\eta'_1},\qquad
y=u^{\eta_2}v^{\eta'_2}.                               \tag{3.5}
\]

For a Laurent polynomial \(H=\sum c_{ij}x^iy^j\), let

\[
a=\min_{c_{ij}\ne0}\langle\eta,(i,j)\rangle=-v_w(H).  
\]

Then

\[
H(u,v)=u^a\left(h_0(v)+u h_1(v)+u^2h_2(v)+\cdots\right),             \tag{3.6}
\]

where a common Laurent monomial is cleared if \(a<0\), and \(h_0\) is
precisely the dehomogenized GGV \(w\)-initial form.  Thus a factor
\((v-\lambda)^t\) in the homogeneous core gives a point

\[
p=(u,r)=(0,0),\qquad r=v-\lambda,                       \tag{3.7}
\]

on the toric boundary divisor (exceptional when \(-w\) is a newly inserted
ray), and its boundary order is \(t\).  The literal coordinate \(v\) and root
value \(\lambda\) depend on the chosen adjacent ray
and dehomogenization; the marked residue factor, not the bare scalar, is the
invariant datum that WTC-CHART must compare.

#### Proof

Under (3.5), the monomial \(x^iy^j\) acquires \(u\)-exponent
\(\langle\eta,(i,j)\rangle\).  Factoring their minimum leaves at \(u=0\)
exactly the monomials maximizing \(w\cdot(i,j)\).  If the minimum is
negative, multiplication by \(u^{-a}\) is the fixed monomial clearing that
turns the rational Laurent expression into its weak regular representative;
it does not alter \(h_0\).  Unimodularity gives a smooth toric chart; since
\(v=\lambda\ne0\) at the marked point, its centered regular parameters are
\((u,r=v-\lambda)\).  This gives (3.7). \(\square\)

The regular fan is obtained by Euclidean/Hirzebruch--Jung subdivision.  Each
new ray is an ordinary point blowup; its blowup word records whether a center
is free or satellite and hence the exceptional components through it.

### 3.3 Full weak pencil ideals

The cut prefix may include `T-const`.  Record the actual packet-designated
generators

\[
\widehat F_\omega=a_\omega F+b_\omega Z^d,\qquad
\widehat G_\omega=c_\omega G+d_\omega Z^e,              \tag{3.7a}
\]

with \(a_\omega c_\omega\ne0\).  These changes leave the two ideals (1.1)
unchanged, but the boundary packet attaches to the weak transforms of
\(\widehat F_\omega,\widehat G_\omega\), not automatically to the symbols
\(F,G\).  This generator provenance must be carried through every pullback.

On a graph resolution \(\rho:Y\to\mathbf P^2\) of a cut word, define the
fixed divisorial parts by

\[
\begin{aligned}
\Delta_f&=\sum_E
 \min\{v_E(\rho^*F),v_E(\rho^*Z^d)\}\,E,\\
\Delta_g&=\sum_E
 \min\{v_E(\rho^*G),v_E(\rho^*Z^e)\}\,E.              \tag{3.8}
\end{aligned}
\]

Here \(E\) runs over **all** prime divisors occurring in the two pulled-back
ideals, not only the exceptional ones.  Equivalently, (3.8) removes the full
height-one gcd.  The original pencils have no fixed curve, so in the intended
application every positive common component is exceptional; the all-prime
formulation is what makes the later local ideal gcd-free without an implicit
assumption.

The weak pencil ideals are

\[
\mathcal J_f=(\mathcal I_f\mathcal O_Y)\otimes\mathcal O_Y(\Delta_f),
\qquad
\mathcal J_g=(\mathcal I_g\mathcal O_Y)\otimes\mathcal O_Y(\Delta_g). \tag{3.9}
\]

Locally at a marked root point, write

\[
\mathcal J_{f,p}=(A_f,B_f),\qquad
\mathcal J_{g,p}=(A_g,B_g),                           \tag{3.10}
\]

where \(A_f,A_g\) are the weak transforms of the two designated sections in
(3.7a), and \(B_f,B_g\) are the weak transforms of the two denominator
sections.
Equations (3.2)-(3.9) make all four generators and all height-one gcds
algorithmically exact for an integral word.  No assertion about their
ordinary orders has yet been made.

### CONJECTURE WTC-CHART — chart, descent, and marked-root realization

For every certified paired packet (1.2), including \(L^{(l)}\)-packets, there
is a graph resolution and a marked point \(p=p_\chi\), with regular parameters
\((x,r)\), such that:

1. \(x=0\) is the selected exceptional component and \(r=0\) is the descent
   of the marked root orbit;
2. after (3.8), the numerator boundary restrictions are

   \[
   A_f(0,r)=u_f(r)r^A,\qquad
   A_g(0,r)=u_g(r)r^C,\qquad u_f(0)u_g(0)\ne0;           \tag{3.11}
   \]

3. a point-blowup factorization of the **original-plane projection**
   \(t_\omega\) is recorded; its exceptional components through \(p\) give
   the immediate proximity predecessors (with \(p\) appended as the next
   center when it is a residual base point).

For integral \(L^{(1)}\) data, Propositions 3.1-3.2 prove two separate
ingredients: the rational projective lift and the local toric face chart.
They do **not** prove that the selected toric root chart occurs compatibly on
the target-side factorization of the composed cut word.  That compatibility
remains part of WTC-CHART even for \(l=1\).
For \(l>1\), one must additionally compare with the actual GGV
\(L^{(l)}\)-packet and descend through the \(\mu_l\)-action without identifying
distinct roots incorrectly or changing orders.  The current transport theorem
expressly stops before this point:
`TRANSPORT.md:3-12,452-463,693-701`.

#### Proof plan for WTC-CHART

1. Normalize each packet direction in the original exponent lattice, not in
   a silently enlarged lattice.
2. Insert the primitive ray into a regular fan using the continued-fraction
   subdivision; emit the corresponding sequence of ordinary point blowups
   and its unimodular exponent matrices.
3. Replace every cut `e_K(lambda)` by (3.2), resolve its graph, and compose the
   graph resolutions.  Pull back all four sections, not just \(P,Q\).  Factor
   the target/original-plane projection into ordinary point blowups and keep
   that word distinct from the domain-side indeterminacy resolution.
4. For a fractional cut, pass to the required Kummer cover and transport the
   deck action through the **whole cut prefix** by conjugation.  The cut need
   not commute with the static action on \(x^{1/l}\).  Prove equivariance of
   the four pulled-back original sections for this transported action, resolve
   any cyclic quotient singularity, and descend the marked orbit.  Prove that
   ramification and stabilizers give the claimed integer multiplicity rather
   than silently multiplying or dividing it.
5. Verify (3.11) by the monomial calculation (3.6), including the tangential
   unit contributed by the denominator at a nonzero root.

This is a birational/descent problem, not the principal multiplicity problem.
I rate it **7/10**.

### CONJECTURE WTC-ID — canonical identity and successor functoriality

Let \(\chi,\chi'\) be any two WTC-CHART realizations of the same certified
packet.  On a common smooth model over the original projective plane, their
marked valuation/residue germs agree.  Once the residual ideals are base
ideals, they therefore define the same center and the same immediate parents
in the canonical simultaneous base cluster, independently of the regular
fan, graph resolution, Kummer presentation, or allowed pencil-generator
change.

Moreover, if two packet occurrences are related by the next certified
Laurent cut or by overlapping chart presentations, WTC-ID decides
functorially whether they represent:

- another presentation of the same center; or
- a distinct successor center, in which case the original-plane blowup words
  prove the asserted proximity edge or edges.

The resulting relation on occurrences is an equivalence relation compatible
with composition of cut prefixes and emits a canonical `center_id`.

#### Proof plan for WTC-ID

1. Replace a coordinate root token by a choice-free marked object: a
   divisorial valuation of \(k(x,y)\) together with its residue point/factor.
2. Compare any two regular fan subdivisions on a common regular refinement;
   prove that their marked valuation and residue homomorphism coincide.
3. Compare graph resolutions through a common resolution, always using the
   original-plane projections for ancestry.  Use the universal property of
   the normalized blowups of the two integral-closure pencil ideals once the
   local base criterion holds.
4. On fractional charts, compare orbits for the prefix-conjugated deck
   actions, including stabilizers and cyclic quotient resolutions.
5. Write exact overlap transition maps for a root and its strict transform.
   Prove the cocycle condition over three prefixes and show that the
   same-center/successor decision is invariant under refinement.

This is not needed merely to compute the order in one supplied chart, but it
is needed for WTC-1's word “determines,” its next-cut functoriality, and every
no-double-counting use in PCC.  The first paragraph is the minimal
single-packet identity lemma.  The successor/cocycle paragraph is required by
the strengthened WTC-1 printed in `sol-pcc-orbits.md:318-326`; if one deletes
that functorial clause from WTC-1, the successor part should instead be named
**CONJECTURE PCC-ID** and moved into PCC-COVER.  I rate the combined WTC-ID
**8/10**.

---

## 4. The exact local bridge to point-basis multiplicity

Work in the completed regular local ring

\[
\widehat{\mathcal O}_{Y,p}=k[[x,r]],\qquad
\mathfrak m=(x,r),                                      \tag{4.1}
\]

after stripping (3.8).

### Lemma 4.1 — order of a general pencil member (**PROVED**)

For nonzero \(A,B\in k[[x,r]]\), put \(I=(A,B)\).  Then

\[
\operatorname{ord}_{\mathfrak m} I
=\min\{\operatorname{ord}_{\mathfrak m}A,
        \operatorname{ord}_{\mathfrak m}B\}.            \tag{4.2}
\]

For general \(c\in k\),

\[
\operatorname{ord}_{\mathfrak m}(A-cB)
=\operatorname{ord}_{\mathfrak m}I.                    \tag{4.3}
\]

#### Proof

Let \(s\) be the minimum in (4.2).  If one generator has order greater than
\(s\), the degree-\(s\) initial form of the other survives for every nonzero
coefficient.  If both have order \(s\), their degree-\(s\) initial forms can
cancel identically for at most one scalar \(c\).  Since \(k\) is infinite,
(4.3) holds for a general pencil parameter. \(\square\)

Thus the mobile multiplicity is controlled by *both* the numerator and the
denominator.  A high-order special numerator does not suffice.

### Lemma 4.2 — transverse divisibility ladder (**PROVED**)

Write

\[
A_f(x,r)=\sum_{j\ge0}x^j a_j(r),\qquad
\operatorname{ord}_r a_0=A.                            \tag{4.4}
\]

Use \(\operatorname{ord}_r0=\infty\).  Then

\[
\operatorname{ord}_{\mathfrak m}A_f
=\min_{j\ge0}\{j+\operatorname{ord}_r a_j\}.           \tag{4.5}
\]

In particular,

\[
\operatorname{ord}_{\mathfrak m}A_f=A
\iff
\operatorname{ord}_r a_j\ge A-j
\quad\text{for every }0\le j<A.                        \tag{4.6}
\]

#### Proof

Every term \(x^jr^s\) has ordinary order \(j+s\), which proves (4.5).
Terms with \(j\ge A\) cannot undercut \(A\).  The \(j=0\) term has order
exactly \(A\), so (4.6) is necessary and sufficient. \(\square\)

The packet gives only the \(j=0\) equality.  WTC requires all the inequalities
for \(1\le j<A\).

### Corollary 4.3 — exact local WTC criterion (**PROVED**)

Assume WTC-CHART and use (3.10)-(3.11).  Write

\[
\begin{aligned}
A_f&=\sum_{j\ge0}x^ja_j(r),& A&=q\alpha t,\\
A_g&=\sum_{j\ge0}x^jc_j(r),& C&=q\beta t.
\end{aligned}                                           \tag{4.7}
\]

Define the two **local generic orders**

\[
m_{f,p}:=\operatorname{ord}_{\mathfrak m}(A_f,B_f),\qquad
m_{g,p}:=\operatorname{ord}_{\mathfrak m}(A_g,B_g).     \tag{4.7a}
\]

Then \(m_{f,p}=A\) and \(m_{g,p}=C\) if and only if

\[
\begin{array}{ll}
\operatorname{ord}_r a_j\ge A-j &(0\le j<A),\\
\operatorname{ord}_{\mathfrak m}B_f\ge A,&\\[2mm]
\operatorname{ord}_r c_j\ge C-j &(0\le j<C),\\
\operatorname{ord}_{\mathfrak m}B_g\ge C.&
\end{array}                                             \tag{4.8}
\]

#### Proof

The two ladders and (3.11) give
\(\operatorname{ord}A_f=A\) and
\(\operatorname{ord}A_g=C\) by Lemma 4.2.  Lemma 4.1 then gives

\[
m_{f,p}=\min(A,\operatorname{ord}B_f)=A,
\qquad
m_{g,p}=\min(C,\operatorname{ord}B_g)=C.               \tag{4.9}
\]

Conversely, because (3.11) gives
\(\operatorname{ord}A_f\le A\) and
\(\operatorname{ord}A_g\le C\), equality in (4.9) forces the two numerator
ladders and the two denominator inequalities. \(\square\)

If WTC is required only to prove the lower bounds in `sol-pcc-orbits.md`
(2.2), (4.8) still forces equality because the boundary terms cap the two
numerator orders by \(A,C\).

### Lemma 4.4 — survival in the minimal cluster (**PROVED**, conditional on
the local criterion)

Suppose (4.8) holds and \(A,C>0\).  Then \(p\) is a base point of both weak
pencil ideals.  Every ancestor of \(p\) in the recorded point-blowup
factorization of the original-plane projection \(t_\omega\) is a base point
of both pencils, so the path survives in the minimal
simultaneous base-point resolution.  The exceptional components through
\(p\) give its immediate proximity parent or parents.  On the canonical
cluster,

\[
R_p=m_{f,p}=A,\qquad S_p=m_{g,p}=C,\qquad h_p=qt.        \tag{4.10}
\]

#### Proof

By (3.11), neither numerator is divisible by the local equation of the
selected exceptional component.  Equation (3.8) removed every common
height-one factor.  Since a two-dimensional regular local ring is a UFD, a
principal ideal generated by two vanishing elements would have a nonunit
common prime factor.  Thus (4.8), which says that both generators of each
gcd-free ideal vanish at \(p\), makes both residual ideals nonprincipal
there.  Argue separately for the two pencils.  If either residual pencil
ideal were invertible at an ancestor on the path, every further pullback of
that ideal would remain invertible, contradicting its base point at \(p\).
Thus
pruning blowups away from the union of the two base clusters cannot remove
the path to \(p\).  On a smooth surface a free blowup center lies on one
exceptional component and is proximate to its creator; a satellite center
lies on two and is proximate to both.  Those components and their creators
are explicit in the retained blowup word. \(\square\)

Equivalently, one may invoke the canonical cluster of the integral closures
of (3.9).  This standard step is not the WTC gap: the gap is proving (4.8).

---

## 5. Why the retained packet shadow plus denominators does not determine
(4.8)

### Proposition 5.1 — identical packet-shadow/support data can have different
ordinary orders (**PROVED**, local retained-data countermodel)

Fix \(A\ge2\) and \(D\ge A\).  Let \(u=r+1\).  Choose a polynomial

\[
h_{\rm gen}(u)=\sum_{i=0}^{A-1}c_i u^i
\]

with every \(c_i\ne0\) and \(h_{\rm gen}(1)\ne0\), and put

\[
h_{\rm sp}(u)=(u-1)^{A-1}.                              \tag{5.1}
\]

Define

\[
f_{\rm gen}=(u-1)^A+xh_{\rm gen}(u),\qquad
f_{\rm sp}=(u-1)^A+xh_{\rm sp}(u),\qquad B=x^D.         \tag{5.2}
\]

In the variables \((x,u)\), the two numerators have identical monomial
support and Newton polygon: both have every \(u^i\), \(0\le i\le A\), and
every \(xu^i\), \(0\le i<A\).  Their restrictions to \(x=0\) are the same
formal boundary packet \((u-1)^A=r^A\), and their denominator section is the
same \(x^D\).
Nevertheless, at \(p=(x,r)=(0,0)\),

\[
\operatorname{ord}(f_{\rm gen},x^D)=1,
\qquad
\operatorname{ord}(f_{\rm sp},x^D)=A.                  \tag{5.3}
\]

#### Proof

The coefficient of \(x\) in \(f_{\rm gen}\) is a unit at \(u=1\), so its
ordinary order is one.  In contrast,

\[
f_{\rm sp}=r^A+xr^{A-1}=r^{A-1}(r+x)
\]

has ordinary order \(A\); taking the minimum with \(D\ge A\) proves (5.3).
The support assertion follows by expanding the two powers in characteristic
zero. \(\square\)

Repeat (5.1)-(5.3) with \(C=q\beta t\) and a denominator exponent at least
\(C\) for a second formal component.  This gives paired local **shadows** with
the advertised common root and both denominator sections but with different
ordinary mobile multiplicities.  It does not give certified packets in the
sense of Definition (1.2).

This is **not a Keller counterexample** and does not disprove the universal
Keller-geometric WTC assertion.  It does prove all of the following:

- a Corollary-7.4 edge factor is not an ordinary initial form;
- Newton support plus the edge factor does not determine the transverse
  divisibilities;
- adding the exact denominator monomial still does not determine them; and
- FC5 or a census quotient that forgets these jets cannot reconstruct them.

The shorter diagnostic already banked at
`xmodel/sol-pcc-orbits.md:303-312`,
\(r^A+x, r^C+2x\), expresses the same obstruction.  Proposition 5.1 makes it
stronger by preserving the full monomial support.

### Proposition 5.2 — denominator capacity is independent (**PROVED**)

Even if the numerator ladder holds, the packet order need not be the mobile
order.  For \(0<\delta<A\),

\[
I=(r^A,x^\delta)                                        \tag{5.4}
\]

has the exact boundary packet \(r^A\) and numerator order \(A\), but its
generic pencil order is \(\delta\).  Thus WTC-DEN cannot be hidden inside
WTC-ORD. \(\square\)

### 5.3 Concentration versus distribution

A weighted/divisorial datum is generally a proximity-weighted combination of
ordinary point-basis coefficients.  Under one blowup, a contact such as
\(r^A+x\) starts with ordinary multiplicity one and may persist through a
chain of infinitely-near points.  WTC-1 demands a much stronger
**non-distribution** assertion: the whole \(q\alpha t,q\beta t\) packet is
already visible as ordinary order at one named center.

This distinction matters quadratically.  Concentrating weight \(N\) at one
center contributes \(N^2\) to PCC; distributing it over \(N\) simple centers
contributes only \(N\).  A vector-valued cluster transport would be a natural
fallback if WTC-ORD is false, but it would not recover PCC's square mass for
free.

---

## 6. The two Keller order conjectures

### CONJECTURE WTC-ORD — transverse numerator dominance

In the WTC-CHART coordinates for every actual Keller packet, the numerator
coefficients in (4.7) obey

\[
\operatorname{ord}_r a_j\ge A-j\quad(0\le j<A),
\qquad
\operatorname{ord}_r c_j\ge C-j\quad(0\le j<C).         \tag{6.1}
\]

Equivalently,

\[
A_f\in\mathfrak m^A\setminus\mathfrak m^{A+1},
\qquad
A_g\in\mathfrak m^C\setminus\mathfrak m^{C+1}.         \tag{6.2}
\]

Corollary 7.4 together with WTC-CHART would supply only the \(j=0\) parts.
Corollary 7.4 alone does not yet identify a weak projective generator or its
ordinary chart coefficient.  No result in
`SECTION4-AUTOMATION.md`, `lib/reduce4.py`, `TRANSPORT.md`, FC5, NF-M, or the
censuses proves any \(j>0\) inequality.

#### Proof plan for WTC-ORD

The only plausible uniform source is the full Keller identity, not the
weighted factorization alone.

1. In the chart of WTC-CHART, retain all four weak sections and write the two
   rational functions as

   \[
   f_\omega=A_f/B_f,\qquad g_\omega=A_g/B_g.
   \]

2. Pull back \(df\wedge dg=J(f,g)\,dx_0\wedge dy_0\), including the Jacobian
   monomial/unit of the birational chart.  After clearing denominators the
   exact identity is

   \[
   (B_f\,dA_f-A_f\,dB_f)\wedge
   (B_g\,dA_g-A_g\,dB_g)
   =B_f^2B_g^2J_\omega(x,r)\,dx\wedge dr,                \tag{6.3}
   \]

   where \(J_\omega\) is explicitly computable from the blowup word.

3. Expand (6.3) in the exceptional parameter \(x\).  Assume \(j\) is the
   first failed inequality in (6.1), and extract the lowest nonzero
   \(r\)-coefficient in the \(x^j\) equation.  The common-power boundary terms
   cancel because their exponent ratio is \(\alpha:\beta\); the next equation
   must either contradict the monomial/unit right side or force the two low
   jets to be a common reparametrization.
4. Analyze the common-reparametrization alternative rather than discarding it:
   it is precisely how a high weighted contact can distribute along a chain.
   Use the whole eligible Corollary-7.4 direction interval and the first
   noncommon bracket coefficient to prove that such a reparametrization cannot
   undercut total degree \(A,C\) at a mobile packet point.
5. Express the induction as ideal membership

   \[
   a_j\in(r^{A-j}),\qquad c_j\in(r^{C-j}),               \tag{6.4}
   \]

   in the exact coefficient ring.  NF-M can be used as a backend only after a
   new certified coefficient-ring homomorphism carries the full transformed
   \(F,G\) jets into the Sigray merge-orbit variables for the same occurrence
   and frame; no such GGV-to-Sigray gluing is banked.  With that prerequisite,
   a fixed zero-dimensional NF-M schema could verify the remainders by
   saturation away from the root discriminant and declared nonzero
   coefficients.  A positive-dimensional NF-M component must remain open;
   finite sampling is not a proof.
6. Prove the induction uniformly in \(q,t,\alpha,\beta\).  A check of finitely
   many current census rows can only be a regression gate, because those rows
   have neither occurrence completeness nor polynomial realizability.

The load-bearing step is item 4.  It is a Keller-specific non-distribution
theorem, not standard Newton-polygon theory.  I rate WTC-ORD **9/10**.

### CONJECTURE WTC-DEN — residual denominator capacity

In the same chart, the weak denominator sections obey

\[
\operatorname{ord}_{\mathfrak m}B_f\ge q\alpha t,
\qquad
\operatorname{ord}_{\mathfrak m}B_g\ge q\beta t.        \tag{6.5}
\]

At a non-toric root these weak denominators are monomials in the exceptional
parameters times tangential units, so (6.5) is an explicit integer inequality
once the projective chart and fixed divisors are known.  What is unproved is
that every certified packet occurs before this residual capacity is exhausted.

#### Proof plan for WTC-DEN

1. From (3.3)-(3.9), record for every exceptional divisor \(E\) the two
   ideal values and the two denominator values

   \[
   \nu_E(\mathcal I_f),\quad d\,v_E(Z),\quad
   \nu_E(\mathcal I_g),\quad e\,v_E(Z).                 \tag{6.6}
   \]

   Also retain the designated-generator values for
   \(\widehat F_\omega,\widehat G_\omega\); the ideal values in (6.6) are
   invariant under `T-const`.

2. Subtract the two componentwise minima in (3.8).  In local normal-crossing
   parameters this gives exact monomials

   \[
   \delta_{f,E}=d\,v_E(Z)-\nu_E(\mathcal I_f),\qquad
   \delta_{g,E}=e\,v_E(Z)-\nu_E(\mathcal I_g),          \tag{6.6a}
   \]

   whose contributions at the marked point assemble as

   \[
   B_f=x^{\delta_f}r^{\epsilon_f}\cdot\text{unit},\qquad
   B_g=x^{\delta_g}r^{\epsilon_g}\cdot\text{unit}.      \tag{6.7}
   \]

   The conjectured inequalities are
   \(\delta_f+\epsilon_f\ge A\) and
   \(\delta_g+\epsilon_g\ge C\).
3. Define the residual common capacity at a packet occurrence by

   \[
   N(\mathfrak p)=\min\left(
     \left\lfloor\frac{\operatorname{ord}B_f}{\alpha}\right\rfloor,
     \left\lfloor\frac{\operatorname{ord}B_g}{\beta}\right\rfloor
   \right).                                             \tag{6.8}
   \]

   Prove \(qt\le N(\mathfrak p)\) from the exact valuation ledger, and derive
   a functorial update formula for \(N\) under the next blowup/root cut.
4. Check the formula on every existing integral Section-4 trace.  This is a
   finite exact test because denominators are monomials; it can falsify a
   proposed invariant immediately.
5. Prove the update uniformly from the Corollary-7.4 positivity interval and
   the degree identities \(d=B\alpha,e=B\beta\).  Do not substitute a Sigray
   \(b_i\) or FC5 \(d_q\) for GGV \(q\); no such dictionary is banked.

If (6.5) fails for one genuine packet, that packet is a special-fiber/weighted
feature after the generic pencil has already resolved, and the universal
wording of WTC-1 is false.  Thus the capacity test is substantive, not merely
bookkeeping.  I rate WTC-DEN **8.5/10**.

---

## 7. Conditional proof of WTC-1

### Theorem 7.1 — WTC-1 reduced to four conjectures

Assume WTC-CHART, WTC-ID, WTC-ORD, and WTC-DEN.  Then every certified paired
packet determines a named proper or infinitely-near common base center \(p\)
of the minimal simultaneous pencil resolution, its immediate proximity parent
or parents, and the exact mobile multiplicities (0.1).  The construction is
functorial under the next certified Laurent cut.

#### Proof

Theorem 2.1 supplies the same-core paired powers and the upstairs integers
\(A=q\alpha t,C=q\beta t\).  WTC-CHART supplies a descended regular marked
point, the boundary equalities (3.11), the four weak local generators, and the
original-plane blowup word.  WTC-ORD is exactly the pair of transverse ladders
in (4.8), while WTC-DEN is exactly the other pair of inequalities.  Corollary
4.3 therefore gives the local generic orders \(m_{f,p}=A,m_{g,p}=C\).
Lemma 4.4 places the point in the minimal simultaneous base cluster and gives

\[
R_p=A=q\alpha t,\qquad S_p=C=q\beta t,\qquad h_p=qt.
\]

WTC-ID makes the result independent of chart choices and supplies the
successor/root identity required for functoriality. \(\square\)

This is a genuine reduction, but no unnecessary independence claim is made.
Propositions 5.1 and 5.2 prove that WTC-ORD and WTC-DEN are separate from the
retained face data and from each other.  WTC-CHART and WTC-ID isolate,
respectively, existence of a marked projective realization and invariance of
the resulting name/ancestry under choices and successive presentations.

---

## 8. What the bank contributes—and cannot contribute

### 8.1 Corollary 7.4 and Section 4

The exact gain is Theorem 2.1.  The automated certificate stores

\[
\ell_{1,-K}(P)=\lambda_Px^cy^d
  \prod_i(z-\lambda_i)^{qmt_i},\qquad z=x^Ky,            \tag{8.1}
\]

and the cut shifts one selected root to zero.  This supplies direction, root
token, and multiplicity.  It does not store:

- the paired \(Q\)-factor as a first-class certificate;
- \(F,G,Z^d,Z^e\) as projective sections;
- exceptional fixed divisors;
- the transverse coefficient polynomials in (4.4)/(4.7);
- a center identifier or proximity parents; or
- relations between root tokens in different certificates.

Indeed shared-root relations currently force the Section-4 engine to stop:
`SECTION4-AUTOMATION.md:273-283`.  The support-level transformations in
`lib/reduce4.py` are faithful to their stated scope but cannot check (4.8).

### 8.2 The normalization transport theorem

`TRANSPORT.md` proves the pre-Laurent GGV-to-Sigray normalization and an exact
rational valuation ledger.  It explicitly says that it is not a
corner-to-tree functor, does not apply to the post-Laurent bracket objects, and
does not determine pole/fiber decorations (`TRANSPORT.md:3-12,452-463`).  Its
remaining `CONJECTURE T` is closely related to WTC-CHART, but even a complete
corner-to-tree functor would not by itself prove the ordinary ladders or
denominator capacity.

### 8.3 FC5

FC5 is exactly

\[
w_G=\frac{\bar\kappa_G(d_q-1)}{\nu_Gd_q},
\qquad M_G=\gcd(d_p,d_q).                               \tag{8.2}
\]

It consumes an already fixed local frame and emits two scalars.  It has no
root position, exceptional divisor, transverse jet, incoming point-basis
mass, proximity relation, or cross-chart identifier.  Its noninjectivity is
visible in the banked BB2 family

\[
(\nu,\bar\kappa,d_p,d_q)
=(N,6N+3,4N+1,2N+1),\qquad N\ge2,                      \tag{8.3}
\]

for which every \(N\ge2\) emits \((w,M)=(6,1)\).  See
`xmodel/sol-g5-emission.md:92-156,332-359` and
`cases/td11_census.py:1061-1120`.

FC5 could become a scalar consistency check only after a new certified
GGV-occurrence-to-Sigray-frame interface exists.  No \(q_h\leftrightarrow
b_i,d_q\) dictionary is banked.  Without that prerequisite—and certainly
before a center certificate—FC5 cannot check or produce WTC data, nor prove a
divisibility in (6.1).

### 8.4 NF-M and the census infrastructure

For a fixed discrete merge schema, NF-M bounds the zero-dimensional
coefficient types.  Its separate future-locality comparison additionally
requires the same type **and** the same emitted frame.  Positive-dimensional
components are retained whole, not replaced by a finite type list.  NF-M
neither names a projective point nor equates GGV root occurrences across
charts (`NF-M.md:95-122`).

`xmodel/sol-normalform.md` proposes a fat record rich in arithmetic,
root-orbit, arrival, scale, and local coefficient fields; its compiler-facing
schema is an interface that *should* expose those fields, not a claim that the
public censuses already store them.  The actual public census/book keys retain
selected arithmetic, pattern, and route data and deliberately aggregate or
discard parts of entry/context/provenance.  They do not retain the four
projective sections, the ordinary maximal ideal, exceptional valuations,
point-basis coefficients, or proximity.  The td-11 output is an
instrument-uniform death quotient, not a literal extension or occurrence
census.  Relevant audits are:

- `xmodel/sol-normalform.md:74-120,610-698`;
- `cases/book_enum.py:283-305,373-386`;
- `xmodel/sol-census-final.md:5-15,56-67`;
- `xmodel/sol-census-review.md:125-157`; and
- `TDBOUND.md:29-33`.

Accordingly, neither the 21-of-22 construction frequency nor an NF-M type
count is a center-coverage statement.  This confirms the negative conclusion
at `xmodel/sol-pcc-orbits.md:354-478`.

### 8.5 Productive use of the existing infrastructure

The existing exact-arithmetic and fail-closed machinery could be **extended**
to replay enriched certificates after the missing GGV/projective occurrence
interface is built.  It cannot check them in its current schema.  A minimally
adequate new record is:

```text
CenterPacketCertificate
  source_pair_id; exact Corollary-7.4 hypotheses
  cut_prefix; primitive direction; q
  T_const generator provenance for Fhat_omega, Ghat_omega
  root_token; conjugated deck orbit; upstairs root multiplicity t
  regular_fan; unimodular chart matrices
  domain_graph_resolution; original_plane_blowup_word
  exceptional_components_through_p; proximity_parent_ids
  pullback valuations of F, Z^d, G, Z^e
  fixed divisors Delta_f, Delta_g
  local generators A_f, B_f, A_g, B_g
  transverse quotients a_j / r^(A-j), c_j / r^(C-j)
  denominator orders; capacity N
  occurrence_id; canonical center_id; successor occurrence ids
  emitted R_p, S_p
  optional Sigray_frame_provenance_id; optional FC5 consistency fields
```

A gate should reject the record unless:

1. both graph projections replay, the domain maps compose to the Laurent word,
   and the original-plane blowup word factors the correct projection;
2. the `T-const` generator provenance replays;
3. the four section pullbacks and fixed divisors replay;
4. the two boundary packets replay;
5. every transverse division in (6.1) has zero remainder;
6. both capacity inequalities replay; and
7. parent and successor identifiers agree under chart overlap/descent.

An FC5 field may be checked only when the optional provenance identifier gives
the missing certified occurrence-to-Sigray-frame map.

This would certify WTC for a *given realized packet*.  It would not prove the
uniform Keller conjectures or the occurrence coverage needed by PCC.

---

## 9. If concentration fails: the correct fallback object

The local countermodels do not show that a packet is geometrically useless;
they show that its contribution may be a cluster vector instead of one large
point coefficient.  The natural fallback is:

> **CONJECTURE WTC-VEC.** Every certified paired packet determines a finite
> rooted subcluster, its two point-basis increment vectors, and the relevant
> rows of the proximity matrix.  Alternate chart presentations descend to the
> same rooted object, and the next cut extends that object functorially.

WTC-VEC is weaker than WTC-1.  In matrix language, it asks for enough
neighboring divisorial/contact data to invert the triangular proximity
transform, rather than declaring that the entire weighted packet is one
point-basis coordinate.  The paired, fiber-tagged all-root construction
proposed in `xmodel/sol-lateral3.md:135-175` has the right shape, but is not a
banked theorem.

A proof of WTC-VEC would require a new quadratic estimate on the resulting
vectors; it would not imply PCC merely from conservation of a linear packet
weight.

---

## 10. The exact theorem still required for PCC

Even a proof of WTC-1 would not prove PCC.  The remaining statement is not
“enumerate all roots.”  It is a coverage, identity, and **quadratic
concentration** theorem.

Let \(\Omega\) be the factor-expanded occurrence forest containing every
eligible root at every certified cut, rather than the one selected root path
used by a reduction trace.  Give \(\omega\in\Omega\) the certified weight

\[
w(\omega)=q_\omega t_\omega.                            \tag{10.1}
\]

WTC would give a center map

\[
\kappa:\Omega\longrightarrow K_f\cap K_g.                \tag{10.2}
\]

For a total, canonical \(\kappa\), define without any additive assumption

\[
c_p^{\max}:=\max\bigl(\{w(\omega):\kappa(\omega)=p\}\cup\{0\}\bigr). \tag{10.3}
\]

WTC gives \(c_p^{\max}\le h_p\).  Taking a maximum is deliberately
conservative: repeated sightings and even distinct packet factors at one
center contribute at most once.  It makes the remaining conjecture
noncircular.

> **CONJECTURE PCC-COVER (occurrence-faithful coverage and no double
> counting).** The all-root forest \(\Omega\) is exhaustive for the required
> packet mass, WTC's center map \(\kappa\) is total and canonical, and:
>
> 1. alternate charts or repeated certificates for the same geometric center
>    have the same \(\kappa\)-image;
> 2. a repeated strict transform is counted at a new center only when the WTC
>    blowup word proves a distinct infinitely-near child with the asserted
>    proximity ancestry;
> 3. every occurrence receives exactly one center image (including all deck,
>    overlap, and branch-divergence identifications); and
> 4. the canonically defined conservative weights (10.3) satisfy
>
>    \[
>    \sum_p (c_p^{\max})^2\ge B^2-1.                    \tag{10.4}
>    \]

Then (10.4) implies PCC because \(c_p^{\max}\le h_p\).  Equivalently this
version of PCC-COVER must prove the one-unit residual-energy bound

\[
B^2-\sum_p(c_p^{\max})^2\le1.                           \tag{10.5}
\]

If the maximum version is too strong, it may be weakened only by supplying an
**explicit packet-packing rule** \(\operatorname{pack}_p\), defined from
certified pairwise-coprime ordinary initial factors at \(p\), together with a
proof

\[
c_p^{\rm pack}:=\operatorname{pack}_p(\kappa^{-1}(p))\le h_p.        \tag{10.6}
\]

One may then replace \(c_p^{\max}\) by \(c_p^{\rm pack}\) in (10.4).
Merely asserting the existence of unspecified integers \(c_p\le h_p\) with
the desired square bound would be circular: taking \(c_p=h_p\) recovers PCC
itself.  No additive packing rule is presently banked.

The sharp point is nonlinear: even an exhaustive linear identity
\(\sum_pc_p=B\) permits \(B\) unit packets, for which
\(\sum_pc_p^2=B\ll B^2-1\).  Thus neither all-root enumeration, the linear
GGV intersection decompositions, FC5 scalar emission identities, nor census counts
can substitute for (10.4).  A proof needs a proximity-quadratic telescope or
comparable Keller rigidity at branch-divergence centers.

The present bank supplies none of the following indispensable inputs:

- an all-root occurrence completeness theorem;
- a canonical cross-chart center equivalence relation;
- a proof that successive sightings are distinct proximate centers;
- an optional coprime-factor packing law proving (10.6); or
- the residual-energy estimate (10.5).

I rate PCC-COVER **9.5/10**.  It is harder than the local WTC dictionary because
it must be globally exhaustive and prove near-total quadratic concentration,
not merely transport one packet correctly.  This is precisely the second
missing arrow stated at `xmodel/sol-pcc-orbits.md:333-352`.

---

## 11. Final assessment

WTC-1 should remain labelled **CONJECTURE**.  The strongest defensible result
from the bank is the conditional theorem of §7, with the following exact
division of labor:

1. Corollary 7.4 supplies the paired common-power packet—**proved**.
2. Integral Laurent words have explicit projective lifts and weighted faces
   have exact boundary interpretations—**proved**.
3. Four ordinary-order inequalities are necessary and sufficient for the
   predicted generic pencil multiplicities—**proved**.
4. Projective compatibility and fractional/root-orbit descent are
   **CONJECTURE WTC-CHART**.
5. Choice-independent center identity and cross-prefix functoriality are
   **CONJECTURE WTC-ID**.
6. The two transverse numerator ladders are **CONJECTURE WTC-ORD**.
7. The two residual denominator inequalities are **CONJECTURE WTC-DEN**.

The earliest missing arrow for arbitrary packets is WTC-CHART.  Once a
compatible integral chart is supplied, the first coefficient/geometric
obstruction is WTC-ORD together with WTC-DEN.  FC5 and the census could verify
shadows of a completed certificate only after a new occurrence interface;
they cannot create the missing ordinary point-basis data.  The best next
experiment is one fully realized integral Corollary-7.4 packet: lift all four
sections by (3.2), emit (3.8)-(3.10), and test the finite divisibility ladder
(4.8).  A single failure would refute the one-center concentration form and
redirect the lane to WTC-VEC; a successful example would expose the exact
coefficient identity needed for the uniform Keller induction.
