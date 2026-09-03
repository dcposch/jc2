# OPEN[SIBLING-COEFFICIENTS]: source reconstruction and bounded exact-CAS audit

Date: 2026-09-03  
Lane status: **UNREVIEWED**  
Scope: coefficient-level compatibility at adjacent nodes of Moh's major-disc tree  
Primary verdict: **the exact two-node problem is not determined by the printed
pair \((p_j,q_j)\); the p,q-only projection under the derived diagonal-action
ansatz survives
both controls and, by exact three-point monodromy witnesses, both requested
large rows. An explicit exact \(D=108\) family is recovered; the
\((90,60)\) characteristic-zero coefficient output ends at COUNTING-BOUND.
No new coefficient-level kill is promoted.**

## 0. Executive result

**SOURCE-READ.** Proposition 5.3 glues charts of the same global polynomials,
not coefficient lists: it fixes the factor centre, inherited Puiseux prefix,
radius, multiplicity, and child degrees. Only the top coefficient after
recentring follows from the old leading form; lower coefficients use discarded
higher \(t\)-jets. Moreover \(q_j\) and \(q_{j-1}\) come from different
approximate roots.

The source also forces three type corrections. Non-bottom nodes obey
\[
D(P,Q,p,q)=Ppq'-Qqp'=cp,\quad c\ne0,
\]
whereas the bottom has constant nonzero RHS. Minor factors get no automatic
child ODE. Finally \(q\) is squarefree and contains every root of \(p\), so
\(p,q\) are not coprime; \(\operatorname{rad}(p)\) and the q-only factor are.

**PROVED-HERE.** The 64 and 75 parent/bottom projections are explicit
dimension-two positive controls. The selected 90 and 108 parent curves also
survive. Their child equations reduce to Padé-tail systems; exact transitive
genus-zero triples prove both child loci nonempty with one-dimensional scaling
families, and 108 has explicit coefficients over a degree-five field. The 90
coefficient Gröbner output alone remains COUNTING-BOUND.

Thus the tree-decorated moment engine is the node-local ODE/Galois projection
once the tree supplies multiplicity labels. It is not the missing common-jet
gluing computation.

## 1. Custody, hash gate, and source-reading protocol

### 1.1 Frozen inputs

Before reading or executing any charged input, I recomputed SHA-256 on all ten
files in `/tmp/jc2-lane.XU3OWR/inputs`. Every digest matched the supplied
value exactly; the gate would have stopped on a mismatch. No ledger was edited
and no excluded lane file was read.

### 1.2 Pages actually source-read

**SOURCE-READ.** I rendered printed pages 143, 170--171, 180--183, 200--201,
and 205--211 at 300 dpi from
`refs/moh1983_jram340_configurations_of_roots.pdf`. With the lane's convention,
printed page \(N\) is PDF page \(N-139\). I also checked printed page 147 for
the leading-polynomial definition. These pages supply Moh's simultaneity
warning; Props. 1.2, 4.6 and 5.3; universal extension and the uniformizer
action; A.3--A.5; and the two Appendix-II examples. References below mean
these visual source reads, not OCR alone.

## 2. What the source actually attaches to a node

Fix a major disc at level \(j\) and a general point

\[
  \sigma_j(X)=\sum_{\nu<\delta_j}a_\nu t^\nu+X t^{\delta_j}.
\]

Write \(d_j\) for Moh's gcd datum. In the notation of Proposition 4.6 the
leading forms have the shape

\[
  g_{\sigma_j}=C_{g,j}\,p_j^{n/d_j},\qquad
  (T_j)_{\sigma_j}=p_j^{\ell_j}q_j,
  \qquad
  \ell_j={-\mu_j+M_j-n\over d_j}.
\]

Put \(P_j=\deg p_j\), \(Q_j=\deg q_j\). Proposition 4.6 gives

\[
  P_j=V_{j+1}{d_j\over d_{j+1}},\qquad
  Q_j=V_{j+1}{n-M_j\over d_{j+1}}.
\]

Its root assertions have the following precise algebraic content.

- \(q_j\) has distinct roots.
- Every root of \(p_j\) is a root of \(q_j\).
- \(p_j\) is not a power of \(q_j\).

Thus, unless \(p_j\) is constant, \(p_j\) and \(q_j\) are *not* coprime.
The useful coprimality statement is obtained by writing

\[
  R_j=\operatorname{rad}(p_j),\qquad q_j=R_jH_j:
  \quad \Disc(R_j)\Disc(H_j)\Res(R_j,H_j)\ne0.
\]

This corrects the literal “squarefreeness/coprimality of \(p,q\)” formulation
in the lane question. The inequation belongs to \(R,H\), while \(q\) itself is
squarefree.

### 2.1 The non-bottom ODE and the bottom exception

**SOURCE-READ.** After the common power is stripped as in Appendix-I
Propositions A.3--A.4, every node to which that argument applies satisfies

\[
  D(P_j,Q_j,p_j,q_j)=P_jp_jq_j'-Q_jq_jp_j'=c_jp_j,
  \qquad c_j\in k^\times.                                      \tag{2.1}
\]

Here a prime is differentiation with respect to the displayed polynomial
variable \(\pi\). Elsewhere in the paper decorations such as \(q^*\) are
labels; they must not silently be interpreted as derivatives.

At \(r=1\), Proposition 4.6 and Proposition A.5 give a different equation.
After dividing the common gcd, it has the form

\[
  d\,g(\pi)f'(\pi)-e\,f(\pi)g'(\pi)=\kappa,
  \qquad \kappa\in k^\times,                                  \tag{2.2}
\]

up to the harmless convention that interchanges \((d,e;g,f)\) and changes
the sign. Equation (2.2) forces \(g\) and \(f\) to be squarefree and coprime:
a repeated root or a common root would make its left side vanish there. It is
not legitimate to replace its right side by \(cp\).

Nor is it legitimate to put (2.1) or (2.2) on every factor called a “minor
sibling.” Proposition 5.3 constructs the next node from a factor in the major
window. The minor-disc discussion on page 200 supplies distribution/radius
bounds, not a specified next general point with a printed child ODE. A minor
factor remains represented in the parent multiplicity passport; attaching a
new bottom equation to it is an extra hypothesis.

### 2.2 What page 201's Galois action does and does not say

**SOURCE-READ.** The displayed automorphism on page 201 is
\(\bar t\mapsto\omega\bar t\) over
\(k\langle\langle\bar t^{A_j}\rangle\rangle\), for an
\(A_j\)-th root of unity \(\omega\). The page does not literally print
“\(\pi\mapsto\zeta\pi\)” for both \(p_j\) and \(q_j\).

**PROVED-HERE, conditional chart form.** Once the chosen chart is shown to
carry this action diagonally on its coefficient coordinate, it is safe to use
the semi-invariant ansatz

\[
  p(\pi)=\lambda_p\pi^bF(\pi^A),\qquad
  q(\pi)=\lambda_q\pi^eG(\pi^A),                               \tag{2.3}
\]

where \(b\ge0\) is the fixed-zero multiplicity, \(e\in\{0,1\}\), and
\(P\equiv b\pmod A,\ Q\equiv e\pmod A\). The semi-invariant character is
\(b\bmod A\). Nonzero roots occur in full \(A\)-orbits; if \(b>0\),
root containment forces \(e=1\). In this report
(2.3) is a **DERIVED-ANSATZ**, not attributed verbatim to page 201.

Writing \(z=\pi^A\), direct differentiation gives the exact quotient formula

\[
\begin{split}
 D(P,Q,p,q)=\lambda_p\lambda_q\pi^{b+e-1}{&
 (Pe-Qb)F(z)G(z)\\
 &+Az[P F(z)G'(z)-QG(z)F'(z)]\} .                 \tag{2.4}
\end{split}
\]

This identity is the coefficient engine used in every computation below.

## 3. The exact recentering calculation: determined versus missing data

Let \(C\) be a root of \(p_j\) of multiplicity
\(u>d_j/(n-M_j)\), and put

\[
  \epsilon=\delta_{j-1}-\delta_j>0,\qquad
  X=C+Yt^\epsilon.
\]

Then

\[
 \sigma_{j-1}(Y)=
 \sum_{\nu<\delta_j}a_\nu t^\nu+C t^{\delta_j}
       +\sum_{\delta_j<\nu<\delta_{j-1}}b_\nu t^\nu
       +Yt^{\delta_{j-1}}.                                    \tag{3.1}
\]

This is the precise meaning of “the parent factor recentered and rescaled.”
Proposition 5.3 determines the child degrees

\[
 P_{j-1}=u{d_{j-1}\over d_j},\qquad
 Q_{j-1}=u{n-M_{j-1}\over d_j},                               \tag{3.2}
\]

and its displayed product formula determines \(\delta_{j-1}\). In the lane's
index convention it is

\[
 \delta_{r-1}=1-
 { (n-M_{r-1})\prod_{i=r}^{s}[V_i(n-M_i)-d_i]
  \over
   (n-M_s-1)\prod_{i=r}^{s}[V_i(n-M_{i-1})-d_i]} .              \tag{3.3}
\]

The same proposition fixes the old coefficients below \(\delta_j\) and the
new coefficient \(C\) at \(\delta_j\). It does not say that the coefficients
of the child's stripped \(p,q\) are obtained by Taylor-expanding the parent's
stripped \(p,q\).

### 3.1 Jet lemma

The exact reason can be stated without any conjectural geometry. For any raw
polynomial or approximate root \(K\), write its whole expansion at the parent
chart as

\[
 K(\sigma_j(X))=t^\lambda\sum_{\rho\ge0}K_\rho(X)t^\rho .      \tag{3.4}
\]

Put
\[
 B(t)=\sum_{\delta_j<\nu<\delta_{j-1}}b_\nu t^{\nu-\delta_j}.
\]
Suppose \(K_0\) has multiplicity \(w\) at \(C\), and the characteristic
conditions make \(w\epsilon\) the child's first weight. Substitution of
\(X=C+B(t)+Yt^\epsilon\) into (3.4) gives

\[
 \operatorname{in}_{j-1}K(Y)=
 [t^{w\epsilon}]
 \sum_{\rho,k\ge0}{K_\rho^{(k)}(C)\over k!}
       (B(t)+Yt^\epsilon)^k t^\rho.                            \tag{3.5}
\]

For \(B=0\), this reduces to
\(\sum_{k=0}^wK_{(w-k)\epsilon}^{(k)}(C)Y^k/k!\), with absent
exponents contributing zero. In general the new \(b_\nu\)'s enter as well.
Since \(B\) has strictly positive order, the coefficient of \(Y^w\) is still
\(K_0^{(w)}(C)/w!\). Hence:

| Datum | Determined by parent \(p_j,q_j\)? |
|---|---|
| inherited series coefficients below \(\delta_j\) | yes, as chart data, not as coefficients of \(p_{j-1},q_{j-1}\) |
| centre \(C\) and factor multiplicity \(u\) | yes |
| child radius and degrees | yes, by Prop. 5.3 |
| coefficient of \(Y^w\) in a raw child initial form | yes: \(K_0^{(w)}(C)/w!\) |
| coefficients of \(Y^0,\ldots,Y^{w-1}\) | no: they involve new \(b_\nu\)'s and \(K_\rho\) for \(\rho>0\) |
| child \(q_{j-1}\) from parent \(q_j\) | no direct map: they come from \(T_{j-1}\) and \(T_j\), respectively |
| siblings in one cyclic orbit | one prototype plus Galois transforms, once the chart action is established |

The “no” entries are free gluing variables before the child ODE and shared-jet
equations; they are not unconstrained coefficients.

Equation (3.5) is **PROVED-HERE** by Taylor expansion. It identifies exactly
the missing variables: higher weighted jets of the *same global* \(f,g\) and
of their approximate roots.

If

\[
 h_C=\left.{p_j(X)\over(X-C)^u}\right|_{X=C}\ne0,              \tag{3.6}
\]

then the top raw coefficient acquired on recentering \(g\) is multiplied by
\(h_C^{n/d_j}\). **PROVED-HERE, not quoted from Moh:** after retaining the
same raw outer units and fixing the root-of-unity gauge,
the next non-bottom leading coefficients can be chosen as

\[
 \operatorname{lc}(p_{j-1})=h_C^{d_{j-1}/d_j},\qquad
 \operatorname{lc}(q_{j-1})=h_C^{(n-M_{j-1})/d_j}.             \tag{3.7}
\]

At a bottom child these become the raw leading-unit relations

\[
 \operatorname{lc}(g_{\rm child})=h_C^{n/d_2},\qquad
 \operatorname{lc}(f_{\rm child})=h_C^{m/d_2},                \tag{3.8}
\]

after a common outer-unit normalization. These relations are normalization
dependent: if the stripped child polynomials are made monic, the same powers
move into their raw constants. They therefore impose finite power/root choices,
but do not identify any of the lower monic coefficients.

For a nonzero orbit root \(r^A=\alpha_i\) of
\(p=\lambda_p\pi^b\prod_k(\pi^A-\alpha_k)^{u_k}\), formula (3.6) is explicitly

\[
 h_r=\lambda_p r^b(Ar^{A-1})^{u_i}
        \prod_{k\ne i}(\alpha_i-\alpha_k)^{u_k}.                \tag{3.9}
\]

For the zero factor it is
\(h_0=\lambda_p\prod_k(-\alpha_k)^{u_k}\). These are the only
coefficient-level parent-to-child formulas obtainable from the leading
polynomial alone.

### 3.2 Consequence for the requested “exact two-node system”

**OPEN[SOURCE-JET-GLUING].** There is no exact functor

\[
 (p_j,q_j,C,u)\longmapsto(p_{j-1},q_{j-1})
\]

in the cited pages. Any system claiming otherwise has silently set, identified,
or existentially forgotten the positive-\(\rho\) coefficients in (3.5). The
source-exact full system must instead introduce a bounded jet of the common
global \(f,g\), impose both substitutions (3.1), construct both approximate
roots, and then extract the two initial forms. Those jet variables and their
support were not part of the frozen tree rows.

This is also why merely requiring “one coefficient field” adds no equation.
Finitely many algebraic local solutions over \(\overline{\mathbf Q}\) live in
their compositum; parametrized solutions live over a common finitely generated
field. What can obstruct them is equality of their underlying global jet
coefficients, not the field containing those coefficients.

## 4. Polynomial systems over \(\mathbf Q\)

This section distinguishes an exact *node-local projection*, which is
computable from the supplied data, from the unavailable source-exact jet
fiber product.

### 4.1 One non-bottom node

Fix \((P,Q,A,b,\{u_i\}_{i=1}^r)\). Introduce quotient-root variables
\(a_1,\ldots,a_r\), a monic q-only factor

\[
 H(z)=z^s+h_{s-1}z^{s-1}+\cdots+h_0,
\]

and nonzero leaders \(\lambda_p,\lambda_q\). Put

\[
 F(z)=\prod_{i=1}^r(z-a_i)^{u_i},\quad
 R(z)=\prod_{i=1}^r(z-a_i),
\]
\[
 p(\pi)=\lambda_p\pi^bF(\pi^A),\qquad
 q(\pi)=\lambda_q\pi^eR(\pi^A)H(\pi^A).                       \tag{4.1}
\]

Squarefreeness forces \(e\in\{0,1\}\), fixed by \(Q\equiv e\pmod A\).
The degree constraints are

\[
 P=b+A\sum_i u_i,\qquad Q=e+A(r+s).                            \tag{4.2}
\]

The ideal \(I_{P,Q,A,\mathbf u}\) is generated over \(\mathbf Q\) by every
coefficient of

\[
 Pp q'-Qq p'-cp.                                               \tag{4.3}
\]

Equivalently, it is generated from the quotient expression (2.4). A convenient
open-locus product is

\[
 U=\lambda_p\lambda_qc\,
       R(0)H(0)\Disc(R)\Disc(H)\Res(R,H),                       \tag{4.4}
\]

with factors omitted when their polynomial has degree zero or when the zero
orbit is intentionally present. Compute \((I:U^\infty)\), equivalently add
\(TU-1\). The “\(p\) not a power of \(q\)” case is a discrete
passport exclusion: since \(q\) is squarefree, the forbidden case is exactly
equal supports with all multiplicities of \(p\) equal. It also follows from
(4.3) once \(c\ne0\).

This rational polynomial system avoids roots of unity by representing each
nonzero orbit by \(z-a_i\). Actual sibling roots require
\(r_i^A-a_i=0\), a primitive \(A\)-th root \(\zeta\), and the linear equations
expressing the chosen chart representation under \(r_i\mapsto\zeta r_i\).
The representation weights of the *child chart coefficients* are not printed
on page 201. This is OPEN[GALOIS-CHART-MAP], folded into
OPEN[SOURCE-JET-GLUING]; its bounded test is the same 16/12 first-band
experiment in §7.4, including an explicit action matrix.

### 4.2 A bottom node

For (2.2), introduce the allowed cyclic forms for \(g,f\), equate every
nonconstant coefficient of the Wronskian to zero, and equate its constant
coefficient to a variable \(\kappa\). Saturate at

\[
 U_{\rm bot}=\lambda_g\lambda_f\kappa\Disc(g)\Disc(f)\Res(g,f).
                                                                    \tag{4.6}
\]

The last three factors are logically redundant when the exact constant
Wronskian and \(\kappa\ne0\) have already been enforced, but retaining them is
a useful audit against a mistaken equation or ring map.

A particularly small exact reduction applies in the cases below. Let

\[
 g(\pi)=\pi G(\pi^A),\quad f(\pi)=F(\pi^A),\quad
 \deg F=M,\quad\deg G=N,
\]

and define the reversed monic polynomials

\[
 P(w)=w^MF(1/w)=1+a_1w+\cdots+a_Mw^M,\qquad
 H(w)=w^NG(1/w).
\]

For the convention \(d f g'-e g f'=\kappa\), the Wronskian is constant iff

\[
 H=\operatorname{trunc}_{N}P^{e/d},\qquad
 h_{N+1}=\cdots=h_{N+M-1}=0,\qquad h_{N+M}\ne0,                \tag{4.7}
\]

where \(P^{e/d}=\sum h_nw^n\). The coefficients are generated exactly over
\(\mathbf Q\) by

\[
 h_0=1,\qquad
 h_n=-{1\over dn}\sum_{i=1}^{\min(M,n)}
       [d(n-i)-ei]a_i h_{n-i}.                                \tag{4.8}
\]

Thus (4.7) is an exact sparse polynomial system, not a numerical series test.
Here \(d,e\) name the coefficients of \(fg'\) and \(gf'\); equivalently the
source ordering is \(D(e,d,g,f)\).

### 4.3 The maximal two-node projection

Let \(I_j\) and \(I_{j-1}\) be the ideals just defined. Introduce the raw
leading units discarded by monic normalization and add (3.7), or (3.8) at the
bottom. Under the derived diagonal-action ansatz, the computable projection is

\[
 I_{\rm diag}=I_j+I_{j-1}+I_{\rm leaders}.                     \tag{4.9}
\]

It is saturated at both open-locus factors and all leaders. The cyclic forms
use one prototype, not independent sibling variables. Identifying its
transforms with the actual sibling charts is conditional on
OPEN[GALOIS-CHART-MAP], the missing chart representation noted in §2.2.

Because \(I_{\rm leaders}\) omits monic lower coefficients, (4.9) is a product
of local ODE varieties up to finite power choices: necessary, not sufficient.

The source-exact replacement would be

\[
 \mathcal J_{f,g}\times_{\mathcal L_j}X_j
                   \times_{\mathcal L_{j-1}}X_{j-1},           \tag{4.10}
\]

Here \(\mathcal J_{f,g}\) is the common weighted-jet scheme and
\(\mathcal L_*\) are initial-form maps. They are absent from
\((P,Q,A,b,\{u_i\})\), so (4.10) remains OPEN[SOURCE-JET-GLUING].

### 4.4 Saturation discipline and controls

The Singular driver extracts the ideal component in its declared ring:

    list wrapped = sat(I,ideal(U));
    ideal Isat = wrapped[1];
    ideal G = std(Isat);

It checks wrapper/type and the normal form of 1. The Padé driver instead uses
\(I+\langle Th-1\rangle\); component mode eliminates \(T\) and maps the result
into a newly declared base ring. Thus neither a sat wrapper nor matching
variable names is mistaken for the intended ideal/ring map.

## 5. Calibration on Moh's printed controls

### 5.1 \((64,48)\): the \(D_2\) parent and four conjugate bottoms

The row is

\[
 (n,m;M_2,M_3;V_2,V_3)=(64,48;52,62;3,3),
\]

with \((d_1,d_2,d_3,d_4)=(64,16,4,2)\). At \(D_2\),

\[
 (P,Q,A,b)=(12,9,4,0),\qquad \{u_i\}=\{3\}.
\]

Set \(z=\pi^4\). A parent family is

\[
 p=(z-a)^3,\qquad
 q=\lambda\pi(z-a)(z-\tfrac54a),\qquad
 c=15\lambda a^2,                                             \tag{5.1}
\]

with \(a\lambda\ne0\). Direct expansion gives
\(D(12,9,p,q)=cp\). For monic \(q\),

\[
 \Disc_\pi(q)={5^5\over2^{10}}a^{18}\ne0.
\]

The parent saturated scheme has dimension two when the free q-leader
\(\lambda\) is retained and dimension one after monic normalization.

For a bottom prototype let \(\rho^2=6\), \(s\ne0\), and

\[
\begin{split}
 G(z)&=z^3+sz^2+s^2(\tfrac38-\tfrac{\rho}{24})z
                   +s^3{4-\rho\over96},\\
 F(z)&=z^2+\tfrac34sz+s^2{6-\rho\over32},\\
 g(\pi)&=G(\pi^4),\qquad f(\pi)=\pi F(\pi^4).
\end{split}                                                    \tag{5.2}
\]

Then the correct bottom equation is

\[
 D(4,3,g,f)=-{5s^5(\rho-3)\over384}\ne0.                       \tag{5.3}
\]

The exact discriminants/resultant printed by the verification driver are

\[
\begin{split}
 \Disc G&={s^6(8\rho^3-33\rho^2+72\rho-72)\over27648},\\
 \Disc F&={s^2(2\rho-3)\over16},\\
 \Res(G,F)&=-{s^6(\rho-2)(\rho^2+4)\over294912}.
\end{split}                                                    \tag{5.4}
\]

Each is nonzero modulo \(\rho^2-6\) and \(s\ne0\). The saturated bottom
scheme is a curve; its rational lex basis is printed by the Singular driver.

There are four selected roots \(r,ir,-r,-ir\) with \(r^4=a\), hence four
bottom siblings. They are Galois transforms of (5.2), not four independent
copies. At the selected root,

\[
 h_r=(4r^3)^3=64r^9,                                         \tag{5.6}
\]

so (3.8) matches the raw leaders by powers \(h_r^4,h_r^3\).
All coefficients may be placed in
\(\mathbf Q(i,\sqrt6,r,s)\). After monic normalization the representative
two-node family has dimension two, with parameters \(a,s\), and finite choices
of \(r,\rho\).

**Verdict: PROVED-HERE SURVIVES for the derived diagonal-action projection.** This
is the required positive control. It is not a claim that the global Jacobian
pair exists.

### 5.2 \((75,50)\), \(V_2=3\): the \(D_2\) parent and five major bottoms

The row is

\[
 (75,50;55,73;3,4),\qquad
 (d_1,d_2,d_3,d_4)=(75,25,5,1),
\]

and its \(D_2\) data are

\[
 (P,Q,A,b)=(20,16,5,0),\qquad\{u_i\}=\{3,1\}.
\]

Let \(z=\pi^5\), let \(15\theta^2-35\theta+21=0\), and put

\[
 b_0=(7-5\theta)a,\qquad d_0=\theta a.
\]

Then

\[
 p=(z-a)^3(z-b_0),\qquad
 q=\lambda\pi(z-a)(z-b_0)(z-d_0),
\quad c=-20\lambda ab_0d_0.                                  \tag{5.7}
\]

The coefficient ideal before this parametrization is

\[
 5d_0+b_0-7a=0,\qquad
 3ab_0+ad_0-3b_0d_0=0,\qquad
 c+20\lambda ab_0d_0=0.                                      \tag{5.8}
\]

The quadratic discriminant is \(-35\), and its two conjugate branches form
one irreducible rational-coefficient curve over the scale \(a\). All centres
and pairwise differences are nonzero when \(a\ne0\). In particular the full
\(\pi\)-discriminant is nonzero.

For the multiplicity-three major orbit, a bottom prototype is

\[
\begin{split}
 G(z)&=z^4+\tfrac32sz^3+\tfrac{21}{16}s^2z^2
       +\tfrac{35}{64}s^3z+\tfrac{63}{512}s^4,\\
 F(z)&=z^3+sz^2+\tfrac58s^2z+\tfrac3{32}s^3,\\
 g(\pi)&=\pi G(\pi^2),\qquad f(\pi)=F(\pi^2).
\end{split}                                                    \tag{5.9}
\]

It satisfies

\[
 D(3,2,g,f)=-{189\over8192}s^7\ne0,                            \tag{5.10}
\]

and

\[
 \Disc G={3^6 7^2\over2^{24}}s^{12},\quad
 \Disc F=-{3\,7^2\over2^{10}}s^6,\quad
 \Res(G,F)={3^4 7\over2^{27}}s^{12}.                           \tag{5.11}
\]

The Singular driver prints the exact rational lex basis of this bottom curve.

The five roots of \(\pi^5=a\) give five conjugate major bottom children. They
share the one prototype parameter \(s\). A common field is
\(\mathbf Q(\zeta_5,\theta,r,s)\), \(r^5=a\), and the monic two-node
projection again has dimension two. Here
\(h_r=(5r^4)^3(a-b_0)\), and the raw bottom leaders match by
\(h_r^3,h_r^2\).

The other p-orbit has multiplicity \(1\). Since the major threshold is
\(d_2/(n-M_2)=25/20=5/4\), it is minor. Proposition 5.3 supplies no bottom
child there, so imposing (5.10) on that orbit would be a formalization error.

**Verdict: PROVED-HERE SURVIVES for the derived diagonal-action projection.**

### 5.3 Positive and negative saturation controls

Exact rational saturation gives dimensions \(2,1,2,1,1,1\) for the 64
parent/bottom, 75 parent/bottom, 108 parent, and 90 parent respectively
(parent dimensions 2 retain the q-leader). Zero-ODE-constant controls are
unit ideals. The substantive collision controls \(d=a\), \(b_0=a\),
\(U(a)=0\), and both bottom zero-scale controls are also unit ideals.

On this host, the complete small Singular batch took 0.02 s and 11,660 KB
maximum RSS; the independent SymPy identity/invariant batch took 0.92 s and
49,332 KB. These are measured reproductions, not complexity estimates.

### 5.4 Why Appendix II can still kill the controls

**SOURCE-READ.** For reduced \((16,12)\), pages 208--209 take the major chart
\(\sigma=\pi t^{1/4}\), a minor chart
\[
 \sigma^*=t^{-1}+a_0+a_1t+a_2t^2+\pi t^3,
\]
and a truncation ending in \(\pi t^{11/4}\). A coherent system for the same
\(\bar g,\bar f\) gives a common approximate root \(h\):
\[
 \bar g=h^4+\alpha_1h^3+\alpha_2h^2+\alpha_3h+\alpha_4,\qquad
 \bar f=h^3+\beta_2h+\beta_3.
\]
For \((15,10)\), pages 210--211 similarly use
\[
 f=h^2+2\beta,\qquad
 \beta^2=\alpha h+\gamma,\qquad
 \beta^3=(3\gamma+a)h^2+\varepsilon h+\delta,
\]
plus shared polynomial forms forced by three root subdiscs. These are deeper
common-\((f,g,h,\beta)\) computations, so the local SAT controls do not
disagree with Appendix II.

## 6. The two requested nonprinted attacks

### 6.1 Lexicographically first \((90,60)\) excess witness

The frozen witness file gives, exactly,

\[
 (90,60,(10,45,88),((2,1),(3,8),(4,4))).                      \tag{6.1}
\]

This is the lexicographically first \((90,60)\) key in
full-tree-ode-excess-witnesses.json. Its gcd data and radii are

\[
\begin{split}
 (d_1,\ldots,d_5)&=(90,30,10,5,1),\\
 (\delta_4,\delta_3,\delta_2,\delta_1)
   &=(-1,\tfrac8{35},\tfrac5{21},\tfrac{17}{42}).
\end{split}
\]

At \(j=3\) the witness has

\[
 (L,A,P,Q,b)=(1,35,8,36,8),
\]

with no nonzero p-orbit. The selected multiplicity-eight factor is the fixed
zero factor. The entire parent curve is

\[
 p_3(\pi)=\pi^8,\qquad
 q_3(\pi)=\pi(\pi^{35}-d),\qquad
 c_3=280d,\qquad d\ne0.                                      \tag{6.2}
\]

Direct substitution proves
\(D(8,36,p_3,q_3)=c_3p_3\), and \(q_3\) is squarefree. The
negative control \(c_3=0\), localized at \(d c_3\), is the unit ideal.

The selected child is the \(j=2\) witness

\[
 (L,A,P,Q,b)=(35,3,24,64,0),\qquad
 (u_1,\ldots,u_8)=(1,\ldots,1).                               \tag{6.3}
\]

All eight nonzero p-orbits are simple. Hence, with \(z=\pi^3\),

\[
 p_2=F(z),\quad \deg F=8,\qquad
 q_2=\lambda\pi F(z)G(z),\quad\deg G=13.                       \tag{6.4}
\]

The factor \(F\) can be cancelled from the stripped equation without losing
an open component:

\[
\begin{split}
 D(24,64,p_2,q_2)=c_2p_2
 &\Longleftrightarrow
 D(24,40,F(\pi^3),\pi G(\pi^3))=c_2\\
 &\Longleftrightarrow
 D(3,5,F(\pi^3),\pi G(\pi^3))=\kappa.                          \tag{6.5}
\end{split}
\]

Thus the exact child coefficient ideal is the Padé system (4.7) with

\[
 (d,e,A,M,N)=(3,5,3,8,13):
\quad h_{14}=\cdots=h_{20}=0,\qquad h_{21}\ne0.                \tag{6.6}
\]

It has eight unnormalized coefficient variables and seven equations. The
weighted dilation \(a_i\mapsto\tau^i a_i\) accounts for the expected one
dimension if the open scheme is nonempty.

**Exact branch audit.** On a stratum where \(a_1=\cdots=a_{r-1}=0\) and
\(a_r\ne0\), root dilation permits \(a_r=1\) over the algebraic closure. The
Rabinowitsch Gröbner ideals are the unit ideal for \(r=3,4,5,6,7,8\).
The \(r=1\) and \(r=2\) strata were not decided within the bounded run. The
all-zero stratum is excluded by \(h_{21}\ne0\).

There is nevertheless an exact non-CAS existence witness. The permutation
arrays in passport_monodromy_witness.py satisfy
\(\sigma_0\sigma_\infty\sigma_1=1\), are transitive, and have cycle types
\[
 5^8,\qquad 3^{13}1,\qquad 21\,1^{19},
\]
transitivity, and total ramification \(78=2\cdot40-2\). The Riemann existence
theorem therefore gives a genus-zero three-point cover. Put its unique simple
pole at \(z=0\) and its 21-fold point over 1 at \(z=\infty\). It has the form
\[
 \beta(z)={F_0(z)^5\over zG_0(z)^3},\qquad
 \deg F_0=8,\quad\deg G_0=13,                                 \tag{6.8}
\]
over \(\overline{\mathbf Q}\), with \(F_0G_0\) squarefree and coprime, and
\[
 \operatorname{ord}_{w=0}
 \{\bar F_0(w)^5-\bar G_0(w)^3\}=21.                           \tag{6.9}
\]
Thus (6.6), including \(h_{21}\ne0\), has a solution.

The permutation triple implicitly defines the exact scaling family
\[
 F_\tau(z)=\tau^8F_0(z/\tau),\qquad
 G_\tau(z)=\tau^{13}G_0(z/\tau),\qquad\tau\in\overline{\mathbf Q}^{\times}.
                                                                    \tag{6.10}
\]
The normalized three-point cover is rigid up to finitely many Nielsen-class
choices, so this exhibited child component has dimension one.

The parent-to-child selected centre is zero and \(h_0=1\), so the leading-unit
part of the gluing adds no obstruction. The absent higher jets from (3.5)
remain absent.

**Verdict: PROVED-HERE SURVIVES for the derived diagonal-action p,q-only
projection.** Family (6.10), together with parent parameter \(d\), gives an
essential dimension-two component over a common field
\(L(d,\tau,\zeta_3)\), where \(L/\mathbf Q\) defines the three-point cover.
The requested explicit
characteristic-zero Gröbner coefficient vector remains COUNTING-BOUND: six of
eight scaling strata are empty, while the two strata supporting (6.10) were
not resolved over \(\mathbf Q\). Over \(\mathbf F_{1009}\), the normalized
open chart is zero-dimensional of degree 821 (281.68 s, about 0.87 GB), with
both zero-leader controls empty; this is not a characteristic-zero lift. No
common-jet/global survival of row (6.1) is claimed.

### 6.2 Selected \(D=108\) screened survivor

The selected row is

\[
 (108,72,(81,106),((2,7),(3,7))).                              \tag{6.11}
\]

The frozen candidate-results.json stores aggregate rather than individual
rows. In its C_FULL_TREE_ODE record, \(D=108\) has 20 assignments, 12 groups,
and 8 pinned-\(N\)-alive groups. Driver select_witnesses.py regenerates (6.11)
from the frozen skeleton module and verifies that the frozen full-tree-ODE
evaluator accepts it. Its selected witness is

\[
 (L,A,P,Q,b)=(1,4,28,21,0),\quad \{u_i\}=\{7\},\quad
 \delta_2=\tfrac14,
\]

with a bottom child \(V_2=7,A_1=2,\delta_1=3/8\) through condition (13).
Here

\[
 (d_1,d_2,d_3,d_4)=(108,36,9,1).
\]

Put \(z=\pi^4\). The parent ODE has the explicit curve

\[
 p_2=(z-a)^7,\qquad q_2=\lambda\pi(z-a)U(z),                   \tag{6.12}
\]

where

\[
 U(z)=z^4-\frac{17a}{4}z^3+\frac{221a^2}{32}z^2
      -\frac{663a^3}{128}z+\frac{3315a^4}{2048},               \tag{6.13}
\]

and

\[
 c_2=-\frac{23205}{512}\lambda a^5.                            \tag{6.14}
\]

Direct exact expansion verifies \(D(28,21,p_2,q_2)=c_2p_2\). For \(a\ne0\),

\[
\begin{split}
 \Disc U&={3^2 5^2 13^2 17^3\over2^{30}}a^{12},\\
 U(0)&={3\cdot5\cdot13\cdot17\over2^{11}}a^4,\\
 U(a)&={3\cdot5\cdot13\over2^{11}}a^4.
\end{split}                                                    \tag{6.15}
\]

These prove squarefreeness and separation from both the selected orbit and
zero. With monic normalization the saturated parent has dimension one.

For the bottom prototype write

\[
 g(\pi)=\pi G(\pi^2),\quad\deg G=10,\qquad
 f(\pi)=F(\pi^2),\quad\deg F=7.                                \tag{6.16}
\]

The source equation is \(D(3,2,g,f)=\kappa\), equivalently its negative
\(2fg'-3gf'=-\kappa\). The exact Padé system is

\[
 (d,e,A,M,N)=(2,3,2,7,10):
\quad h_{11}=\cdots=h_{16}=0,\qquad h_{17}\ne0.                \tag{6.17}
\]

This has seven unnormalized coefficient variables and six equations. Every
\(a_1=0\) stratum, normalized by its first nonzero coefficient
\(a_r=1\) for \(2\le r\le7\), has Rabinowitsch ideal \([1]\). Therefore any
open solution must have \(a_1\ne0\). On the normalized \(a_1=1\) stratum,
slimgb timed out after 600.479 s at 3,464,592 KB RSS. A sparse modular
reconstruction was then lifted and verified exactly in
the degree-five field \(K=\mathbf Q[\alpha]/(\Phi)\), where
\[
\begin{split}
\Phi={}&287548593020928\alpha^5-688401965085696\alpha^4\\
 &+640652914818432\alpha^3-292066554895024\alpha^2\\
 &+65563255857792\alpha-5817852446211.                         \tag{6.18}
\end{split}
\]
The exact driver proves \(\Phi\) irreducible and prints every coefficient of
monic
\[
 F_0=z^7+z^6+\alpha z^5+f_4z^4+\cdots+f_0,\qquad
 G_0=z^{10}+g_9z^9+\cdots+g_0
\]
as an element of \(K\). Reduction modulo \(\Phi\) verifies the constant
Wronskian, exact reversed order 17, and that \(F_0(0),G_0(0),\kappa\) are
units. Those gcd-one unit checks are positive and forced-zero negative
controls in the declared field. The exact family is
\[
 F_s(z)=s^{-7}F_0(sz),\qquad G_s(z)=s^{-10}G_0(sz),\qquad s\ne0. \tag{6.19}
\]

The same exact permutation driver supplies a transitive product-one triple
for this case, of types
\[
 3^7,\qquad2^{10}1,\qquad17\,1^4,
\]
with total ramification \(40=2\cdot21-2\). Normalize the unique simple pole
to \(z=0\) and the 17-fold point over 1 to \(z=\infty\). The resulting
algebraic three-point cover is
\[
 \beta(z)={F_0(z)^3\over zG_0(z)^2},\qquad
 \deg F_0=7,\quad\deg G_0=10,                                 \tag{6.21}
\]
where \(F_0G_0\) is squarefree and coprime and
\[
 \operatorname{ord}_{w=0}
 \{\bar F_0(w)^3-\bar G_0(w)^2\}=17.                           \tag{6.22}
\]
This independently explains why the exact family (6.19) exists and shows that
it is a one-dimensional component after the finite normalized cover choices.

The selected root \(r^4=a\) has
\(h_r=(4r^3)^7\); leader matching again consists only of nonzero power
relations. It cannot decide the lower coefficients in (6.17).

**Verdict: PROVED-HERE SURVIVES for the derived diagonal-action p,q-only
projection.** Exact family (6.19), together with parent parameter \(a\), gives
an essential dimension-two component over
\(K(a,s,r,\zeta_4)\), \(r^4=a\). Its five normalized shapes are
arithmetic conjugates in the quintic coefficient field; they are not the four
\(A_2=4\) tree-sibling charts. The direct Gröbner decomposition timed out, but
the exact witness settles nonemptiness. No common-jet/global survival is claimed.

### 6.3 Is the observed mechanism uniform?

No coefficient-level killing mechanism occurs in either local projection.
Both surviving children come from the same pattern of rigid three-point cover
\(F^e/(zG^d)\); the Padé recurrence and scaling stratification are uniform.
The empty late-first-coefficient strata are real, but the generic strata carry
the displayed covers. Promoting the partial empty pattern would commit the
vanished-leader fallacy: every first nonzero coefficient must be branched and
the next-tail leader kept inverted. Whether every tree passport admits the
required transitive genus-zero triple is a separate finite Hurwitz problem;
even a positive answer would not supply the missing common jets.

## 7. Reading: the decorated moment engine and a possible theorem

### 7.1 Exact root-moment dictionary at one node

Let \(q\) be monic with distinct roots
\(\beta_1,\ldots,\beta_Q\). Label the root \(\beta_\nu\) by its multiplicity
\(u_\nu\ge0\) in \(p\); \(u_\nu=0\) means a q-only root. Root containment says
\(\sum_\nu u_\nu=P\). Dividing (2.1) by \(pq\) gives

\[
 \sum_{\nu=1}^{Q}{w_\nu\over\pi-\beta_\nu}
   ={c\over q(\pi)},\qquad w_\nu=P-Qu_\nu.                     \tag{7.1}
\]

Expansion at infinity yields

\[
 \sum_\nu w_\nu\beta_\nu^k=0\quad(0\le k\le Q-2),\qquad
 \sum_\nu w_\nu\beta_\nu^{Q-1}=c.                             \tag{7.2}
\]

For nonmonic \(q\), the last right side is \(c/\operatorname{lc}(q)\).
The \(k=0\) equation is automatic:
\(\sum_\nu(P-Qu_\nu)=QP-QP=0\).

Equations (7.2), together with distinct-root inequations, are equivalent to
the node ODE. Under a cyclic action, a nonzero \(A\)-orbit contributes zero
to moments whose exponent is not divisible by \(A\). Passing to
\(z=\pi^A\) is therefore exactly the orbit-compressed moment calculation
implemented by (2.4).

### 7.2 Tree node versus decoration datum

The whole major tree supplies almost exactly the combinatorial decoration
needed by that local moment engine:

| Tree datum | Moment/coefficient datum |
|---|---|
| node \(D_j\) | one local ODE variety \(X_j\) |
| \((P_j,Q_j)\) | total p-degree, number of simple q-root slots |
| increment denominator \(A_j\) | cyclic orbit size / quotient coordinate \(z=\pi^{A_j}\) |
| fixed-zero multiplicity \(b_j\) | distinguished q-root \(\beta=0\) with label \(u=b_j\) |
| nonzero factor multiplicity \(u_i\) | common weight \(w_i=P_j-Q_ju_i\) on an \(A_j\)-orbit |
| unused q slot | label \(u_i=0\), weight \(P_j\) |
| major inequality | factor carries a recursive child pointer |
| edge | selected centre, multiplicity, and radius gap |
| minor factor | terminal label at this resolution; no automatic child ODE |
| bottom condition (12)/(13) | parity/residue choice of the constant-Wronskian endpoint |
| Galois orbit | one prototype configuration plus its conjugates |

This dictionary explains why the C_FULL_TREE_PASSPORT screen is natural. For
weights \(w_i\), a necessary orbit-count bound can be expressed through the
positive degree

\[
 d_+=\sum_i\max(w_i,0),\qquad
 g=\gcd_i|w_i|,\qquad S={Q-e\over A},
\]

in the form \(d_+/g\ge S\) used by the frozen passport driver. It is a
node-local necessary condition, not a construction of common global
coefficients.

### 7.3 Is a uniform sibling-coefficient theorem plausible?

**Plausible in a restricted form.** A local theorem could bound the essential
dimension/degree of \(X(P,Q,A,\mathbf u)\), equivalently the moment rank after
translation, dilation, and cyclic symmetry, sharpening the passport screen.

A genuine *sibling* theorem must bound a different quantity: the dimension of
the image/fiber of the common-jet restriction map
\[
 \mathcal J_{f,g}\longrightarrow\prod_{v\in T}X_v.             \tag{7.3}
\]
A rank lower bound for shared-jet equalities would upper-bound this fiber.
The tree lacks the positive-\(t\) coefficients in (3.5), so cannot determine it.

Accordingly:

- the tree-decorated moment engine **is** the whole-tree, node-local
  ODE/Galois computation;
- it is **not** the same computation as source-exact sibling gluing;
- it becomes a sibling engine only after every edge decoration is enlarged by
  a common-jet transition map.

### 7.4 Single cheapest next experiment

Build one source-faithful edge on Moh's smallest positive control, the reduced
\((16,12)\) configuration of pages 208--209. Use exactly his common
\(\bar g,\bar f,h\), the major chart and compatible minor chart, and retain
only the first weighted jet band needed by formula (3.5) across
\((\delta_2,\delta_1)=(-1,1/4)\). Clear denominators with one common
ramified parameter, print the variable/ring map, and compare the extracted
initial forms and the uniformizer-induced action matrix with the verified
local families before eliminating.

Cap it at 30 variables, 10 minutes, and 2 GB; if the band exceeds the cap,
return its counts. Success means reproducing (3.7)--(3.8), deriving the action
matrix, and identifying one lower child coefficient with a shared jet. Only
then reuse the generator on 90 or 108.

## 8. Findings ledger

- **SOURCE-READ:** Prop. 4.6 gives squarefree \(q\),
  \(\operatorname{roots}(p)\subset\operatorname{roots}(q)\), and not-power;
  A.3/A.4 give \(D=cp\); A.5 gives the coprime constant-RHS bottom.
- **SOURCE-READ:** Prop. 5.3 gives centre, prefix, radius, multiplicity and
  degrees, not lower coefficients. Page 201 acts on \(\bar t\); pp.208--211
  glue common global polynomials and approximate roots.
- **PROVED-HERE:** (3.5) identifies the missing positive-\(t\) jets; (2.4) and
  (4.7)--(4.8) are exact rational reductions.
- **PROVED-HERE:** the 64 and 75 projected parent/bottom families survive with
  essential dimension two. The 75 multiplicity-one orbit is minor.
- **PROVED-HERE:** the 90 and 108 parent families survive; exact transitive
  triples give both children one-dimensional \(\overline{\mathbf Q}\)-families.
  The 108 family is explicit over a quintic field.
- **COUNTING-BOUND:** explicit characteristic-zero coefficients for the 90
  child were not recovered by Gröbner computation.
- **OPEN:** SOURCE-JET-GLUING, the common weighted-jet scheme and edge maps.
- **NOT CLAIMED:** any killed row, global \((f,g)\), uniform sibling
  obstruction, or exit price. Hence no charge-basis line is declared.

## 9. Reproduction

From /home/ubuntu/jc2:

    python3 box/siblingcoef-drivers-20260903/select_witnesses.py
    python3 box/siblingcoef-drivers-20260903/verify_families.py
    Singular -q box/siblingcoef-drivers-20260903/saturation_controls.sing
    python3 box/siblingcoef-drivers-20260903/passport_monodromy_witness.py
    python3 box/siblingcoef-drivers-20260903/d108_exact_family.py
    python3 box/siblingcoef-drivers-20260903/pade_sat_audit.py 108 --first 2
    python3 box/siblingcoef-drivers-20260903/sparse_wronskian_mod.py 108 --timeout 60
    find box/siblingcoef-drivers-20260903 -maxdepth 1 -type f -print0 | sort -z | xargs -0 sha256sum

For the bounded 90 screen replace 108 by 90 and use --timeout 600; the
expensive finite-field run is optional. The directory contains the selection,
exact-family, saturation, Padé, modular, and permutation verifiers. All
routine reruns passed.

<!-- BODY-END -->
