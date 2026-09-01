# SHAPE-2-FINISH: the \(u\equiv3\pmod 6\) residual and the \(g\ge3\) inner case

## 0. Scope, integrity, and executive verdict

All three frozen inputs matched the required SHA-256 values before inspection; the
full custody record is in §7.  This lane uses only the charged residual hypotheses and
the primary sources listed there.  It neither assumes existence of a curve surviving an
outer tuple test nor replaces the geometric inner braid by another word with the same
exponent.

The branch-degree correction is decisive: at \(g=2\), \(d=2u\), so the residual
\(u=3k\ge9\) has degree \(6k\), not \(2u+4\).  Because the total product is in
\(V_4\), its \(S_3\)-resolvent always descends to
\(\mathbb P^2-\bar D\).  Divisibility by six is automatic and supplies no
contradiction.  What can be proved uniformly is the following sharper conditional
statement: assuming affine \(A_{2\ell-1}\)-exhaustiveness, a residual curve of this
shape cannot itself satisfy an index-one Cardano identity
\(F=4A^3+27B^2\) with degrees \((6k;2k,3k)\).  The proof treats all allowed
delta sequences.  The exhaustiveness assumption is not established by the frozen
inputs and is named OPEN[AFFINE-ALL-A_ODD] in §4.  Infinity orders alone do not
suffice; §4 gives an explicit torus curve with the right infinity germ but positive
normalization genus.

Accordingly, the \(g=2,\ u\equiv3\pmod6,\ u\ge9\) family is **pinned further but
OPEN**, because a general normal triple cover is not known to force the exact
index-one identity and the needed affine exhaustiveness is also unproved here.  For
\(g\ge3\), SK-2's pointwise fixedness does not extend.
The correct datum is the action of the actual inner word on a labeled Hurwitz fiber.
The product-one \(g=4\) sub-stratum dies, but explicit abstract fixed tuples show that
outer data plus the known exponent cannot kill the general case.  It too is **pinned
further but OPEN** at the word-action tool named in §5.

## 1. Charged statements and typed setup

Write `SK`, `REV`, and `COORD` for the three frozen files in the charge, by basename.  The
standing object is a rational one-place affine curve with a birational polynomial
parametrisation \(\gamma(t)=(p(t),q(t))\),
\[
d=\deg p>n=\deg q,\qquad g=\gcd(d,n),\qquad (d',n')=(d/g,n/g),
\]
and a meridional-transposition epimorphism
\(\phi:\pi _1(\mathbb A^2-D)\twoheadrightarrow S_4\) (SK:44--51).  Family 2 is
\((d',n')=(u,2)\), with \(u=2m+1\ge3\), hence
\[
(d,n)=(gu,2g),\qquad a:=d-n=g(u-2)                                      \tag{1.1}
\]
(SK:275--277).  In particular, at \(g=2\) the projective branch degree is
\(d=2u\), **not** \(2u+4\); \(n=4\) is the degree of the second coordinate, not an
extra branch component (SK:400--406; REV:204).

For blocks of \(g\) transpositions, let \(\Pi_i\) be the ordered block product.  At
\((d',n')=(u,2)\), outer fixedness is exactly
\[
XW^mX=W^{m+1},\quad W=XY,\quad
\Pi=W^mX=X^{-1}W^{m+1},\quad \Pi^2=W^u,                 \tag{1.2}
\]
where the block products alternate \(X,Y,X,Y,\ldots,X\) (SK:281--307; REV:94--102).
For \(g=2\), the reviewed classification leaves an \(S_4\)-capable outer datum only when
\(u\equiv3\pmod6\).  On every such datum
\[
\Pi=WX\text{ is a double transposition, hence }\Pi\in V_4.               \tag{1.3}
\]
The three displayed products proving this are at SK:340--353 and REV:126--134.  The
review also corrects “one \(\langle\Pi\rangle\)-orbit” to one class up to
\(S_4\)-conjugacy (REV:136).  None of this proves that a residual curve with
\(u\ge9\) exists (REV:138--144).

The frozen infinity information is much thinner than a family equation.  In the row
gauge it gives only
\[
(v,z)=\left(s^a\cdot\text{unit},\ \sum_{j\ge d}c_js^j\right),             \tag{1.4}
\]
and the lower bound that every characteristic numerator is at least \(d\)
(SK:102--105).  It defines a degree semigroup by a delta sequence beginning
\((\delta_0,\delta_1)=(d,n)\), with
\(\delta_{\rm aff}=\#(\mathbb N\setminus S_D)\), but supplies neither the later
\(\delta_i\), an AG--S normal form, nor coefficients of a general
\(u\equiv3\pmod6\) curve (SK:47--51,355--357).  Thus any conclusion depending on a
specific later characteristic term will be stated conditionally; shape data will not be
silently promoted to a full germ.

## 2. The \(g=2,\ u\equiv3\pmod 6\) residual: resolvent descent

Let \(q:S_4\to S_4/V_4\simeq S_3\) and \(\psi=q\circ\phi\).  Projectivising the
affine complement adds the relation that the meridian \(\gamma_\infty\) about the line at
infinity is trivial.  Its \(S_4\)-image is the total product \(\Pi\), up to the harmless
inverse convention.  Hence (1.3) gives
\[
\psi(\gamma_\infty)=q(\Pi)=1.                                             \tag{2.1}
\]
Thus \(\psi\) factors, still surjectively, through
\(\pi_1(\mathbb P^2-\bar D)\).  This is the entire INF-TRIVIAL step; it is
degree-free and requires no additional infinity theorem (SK:392--398; REV:202--206).
The branch divisor is the reduced curve \(\bar D\) of degree
\[
\deg\bar D=d=2u=6k,\qquad u=3k,\quad k\ge3\text{ odd}.                    \tag{2.2}
\]

By the usual finite-cover correspondence, the factor gives a connected Galois
\(S_3\)-cover \(Y\to\mathbb P^2\); quotienting by a transposition subgroup gives a
normal (generically non-Galois) degree-three cover.  Equivalently, if
\(W_2\to\mathbb P^2\) is the double cover branched on \(\bar D\), then
\(Y\to W_2\) is cyclic of degree three.  Descent kills generic inertia along the
line at infinity, so the compactified cover is unramified away from \(\bar D\).
At the generic smooth point of the irreducible \(\bar D\), a meridian still maps
to a transposition of \(S_3\).  Thus the degree-three quotient has no
index-three branch component: in Shirane's notation
\[
T_\pi=0,\qquad \Delta_\pi=S_\pi+2T_\pi=\bar D.             \tag{2.3}
\]
The charged local argument proves that this
cyclic cover is unramified over affine **nodes**: the two disjoint \(S_4\)-transpositions
have the same \(S_3\)-image, so the order-two inertia meets \(A_3\) trivially
(SK:428--442; REV:208).  It does not prove the same statement over a tangential
\(A_{2r-1}\) point, which the residual class permits (REV:210).  I therefore consume
descent (2.1), but not the stronger claim that all \(\mathbb Z/3\)-ramification is already
concentrated at infinity.

## 3. Degree-\(2u\) normal \(S_3\)-covers and the torus criterion

For the degree-three quotient \(\pi:X\to\mathbb P^2\), write
\(\pi_*\mathcal O_X=\mathcal O\oplus\mathcal T_\pi\).  Miranda's structure, as
recorded in Shirane §1.1.5, gives
\[
\mathcal O(\Delta_\pi)\simeq(\det\mathcal T_\pi)^{-2}.
\]
Thus the weighted branch identity (2.3) of degree \(6k\) says only
\(\det\mathcal T_\pi\simeq\mathcal O(-3k)\).  In general this is an even-degree
condition, not a splitting theorem.

If the cover is a triple section of \(L=\mathcal O(k)\), equivalently
\(\mathcal T_\pi\simeq L^{-1}\oplus L^{-2}\), its depressed cubic has coefficients
\[
A\in H^0(\mathcal O(2k)),\qquad B\in H^0(\mathcal O(3k)),
\]
and reduced discriminant
\[
F=4A^3+27B^2,\qquad \deg F=6k.                             \tag{3.1}
\]
Consequently an index-one Cardano model requires \(6\mid\deg\bar D\).  Here this is
numerically automatic: \(2u=6(u/3)\).  The requested degrees are
\(\deg A=2u/3=2k\) and \(\deg B=u=3k\); divisibility gives no kill.

The converse needed by this lane is not a general triple-cover theorem.  A rank-two
bundle on \(\mathbb P^2\) need not split, and even at degree six Shirane's Corollary 2.3
allows \(\mathcal T_\pi\simeq\Omega_{\mathbb P^2}\) as well as
\(\mathcal O(-2)\oplus\mathcal O(-1)\).  Shirane's Corollary 0.6 nevertheless proves,
by a special degree-six classification, that the *weighted branch divisor* of any such
sextic cover has a \((2,3)\)-torus equation.  Its hypothesis is literally
\(\deg\Delta=6\); no
degree-\(6k\), \(k>1\), analogue occurs in that paper.  Tokunaga's Cardano construction
works over the function field/minimal splitting variety.  The inspected sources do not
prove that its global discriminant representative has index one: square-class data may
leave a square index factor, schematically
\(4A^3+27B^2=F\,C^2\).  This is a warning about the unproved \(C=1\) step, not
a theorem attributed here to Tokunaga.

Therefore `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` remains a sufficient route, but the
exact weaker missing statement is
`OPEN[SHAPE-2-CARDANO-INDEX-ONE]`: prove that the descended cover's reduced branch
admits (3.1), or obtain the equivalent index-one divisor-class statement on the double
plane.  Section 4 proves impossibility if this missing statement and the affine
exhaustiveness hypothesis typed there both hold.

## 4. Infinity-germ valuation test for the family-2 residual

Here is the general valuation calculation.  Put \(u=3k\), with \(k\ge3\) odd.  The
Abhyankar--Moh conditions force the finite delta sequence to terminate after one
further generator and have the form
\[
\Delta=(6k,4,\eta),\qquad \eta\text{ odd},\quad 3k\le\eta<12k,\quad
2\eta\in\langle6k,4\rangle.                                                \tag{4.1}
\]
Indeed the gcd chain is \(6k,2,1\), with quotients \(3k,2\); after the gcd reaches
one there can be no further nontrivial quotient.  In a representation
\(2\eta=6kh+4b\), oddness of \(\eta\) forces \(h\) odd and hence
\(\eta\ge3k\), while the Abhyankar--Moh inequality gives
\(\eta<3k\cdot4=12k\).  Its symmetric-semigroup conductor is
\[
C=(3k-1)4+(2-1)\eta-6k+1=6k+\eta-3.
\]
Thus \(\delta_{\rm aff}=C/2\).  For the local conversion, the second
maximal-contact value is
\(\bar\beta_2=(6k)^2/2-\eta=18k^2-\eta\); since
\(\bar\beta_2=(3k-2)6k+\beta_2-6k\), this gives
\[
\delta_{\rm aff}={6k+\eta-3\over2},\qquad
(a;\beta_1,\beta_2)=(6k-4;6k,18k-\eta).                    \tag{4.2}
\]
No choice of \(\eta\) is being suppressed.

The frozen review distinguishes affine nodes from allowed tangential
\(A_{2\ell-1}\) double points (REV:208--210), but it does not state an
exhaustiveness theorem.  Fail closed at
OPEN[AFFINE-ALL-A_ODD], the hypothesis
\[
(\mathrm H_{\rm aff})\qquad
\text{every affine singularity is an \(A_{2\ell-1}\) pair of smooth branches.}
\]

**Conditional NO-TORUS proposition.**  Under \((\mathrm H_{\rm aff})\), no residual
curve with (4.1) can have an equation
\[
F=4A^3+27B^2,\qquad \deg A=2k,\quad\deg B=3k.             \tag{4.3}
\]

*Proof.*  Let \(Q\) be the unique point at infinity.  Irreducibility of \(F\) makes
\(A,B\) coprime.  At an affine common zero \(P\), multiplicity two of \(F\) forces
\(B=0\) to be smooth.  Put \(r_P=I_P(A,B)\) and take \(B=y\).  If
\(A(x,0)=x^{r_P}\) times a unit, Weierstrass preparation writes \(F\), up to a unit,
as \(y^2+p(x)y+q(x)\), with
\(\operatorname {ord}q=3r_P\) and \(\operatorname {ord}p\ge2r_P\).  Hypothesis
\((\mathrm H_{\rm aff})\) says that this is a pair of smooth graph branches, so its
discriminant is the square of their difference.  Hence \(r_P\) is even and their
intersection, therefore \(\delta_P\), is \(3r_P/2\).  Write
\(\sum_{P\ne Q}r_P=2s\).  Other affine singularities can only increase
\(\delta_{\rm aff}\), so
\[
3s\le\delta_{\rm aff}.                                                       \tag{4.4}
\]

Every common zero of \(A\) and \(B\) lies on \(F=0\).  Since the one-place curve
\(\bar D\) has only the point \(Q\) on the line at infinity, \(Q\) is their only
intersection there.  Bezout and \(F|_{A=0}=27B^2\) therefore give
\[
I_Q(A,B)=6k^2-2s,\qquad I_Q(F,A)=12k^2-4s.                  \tag{4.5}
\]
Using (4.1), (4.2), and (4.4),
\[
I_Q(F,A)\ge12k^2-{4\over3}\delta_{\rm aff}
=12k^2-4k-{2\eta\over3}+2>12k^2-12k+2.                    \tag{4.6}
\]

Choose local coordinates \((v,z)\) at \(Q\) with orders
\((6k-4,6k)=2(\alpha,\beta)\), where
\(\alpha=3k-2\), \(\beta=3k\).  Since \(2k<\alpha\), distinct monomials of total
degree at most \(2k\) have distinct \((\alpha,\beta)\)-weights.  If the least local
term of \(A\) is \(v^{q-j}z^j\), then
\[
I_Q(F,A)=2(q\alpha+2j),\qquad q\le2k.                       \tag{4.7}
\]
The left side is divisible by four by (4.5), while \(\alpha\) is odd, so \(q\) is
even.  If \(q\le2k-2\), its value is at most
\((2k-2)6k=12k^2-12k\), contradicting (4.6).  Hence \(q=2k\).

The required first Newton face of the one branch is
\((z^\alpha-\lambda v^\beta)^2\).  If \(j=0\), write the leading term of
\(A\) as \(a_0 v^{2k}\).  There is no term of \(B\) below weight
\(\alpha\beta\), and its degree bound leaves
\(B_{\rm face}=\mu z^\alpha+\xi v^\beta\), with \(\mu\ne0\).  The resulting
quadratic \(27(\mu T+\xi)^2+4a_0^3\), \(T=z^\alpha/v^\beta\), has discriminant
\(-432\mu^2a_0^3\ne0\), rather than being the required square.

If \(j>0\), \(A^3\) lies strictly above the first face, so
\(B_{\rm face}=\mu(z^\alpha-\lambda v^\beta)\).  Put
\(\nu=I_Q(A,B)=2k\alpha+2j\).  On the \((\alpha,\beta)\)-toric chart at the
point selected by this binomial there are analytic coordinates \((t,w)\) in which
\[
B=t^{\alpha\beta}w,\qquad A=t^\nu\cdot\text{unit}.
\]
Since \(3\nu-2\alpha\beta=6j\), the strict transform of \(F\) is
\[
27w^2+4t^{6j}\cdot\text{unit}^3
=27(w-t^{3j}h)(w+t^{3j}h),
\]
where the nonzero analytic unit \(h\) exists over \(\mathbb C\).  These are two
distinct branches, and a birational blowdown cannot merge them.  Thus in either case
\(F\) has at least two places at \(Q\), a contradiction.  \(\square\)

The affine hypothesis is essential.  Pure infinity orders do **not** prove this result:
\[
A_0=XZ^{2k-1},\quad B_0=X^2Z^{3k-2}-Y^{3k}
\]
give a degree-\(6k\) torus curve whose germ at \([1:0:0]\) is
\(4z^{6k-3}+27(z^{3k-2}-y^{3k})^2\).  It is one branch with orders
\((6k-4,6k)\), next characteristic numerator \(9k\), and numerically valid
\(\Delta=(6k,4,9k)\).  Indeed, for \(\lambda^2=-4/27\),
\[
z=t^{6k},\qquad
y=t^{6k-4}(1-\lambda t^{3k})^{1/(3k)}
\]
cancels the two displayed summands.  With
\(s=t(1-\lambda t^{3k})^{1/(3k(6k-4))}\), it becomes
\[
y=s^{6k-4},\qquad
z=s^{6k}+{\lambda\over3k-2}s^{9k}+O(s^{12k}).
\]
Thus \(9k\), not the raw correction \(9k-4\), is the next characteristic
numerator; \(\gcd(6k-4,6k,9k)=1\) makes the parametrisation primitive, and its
multiplicity exhausts the germ.  Since \(F(X,Y,0)=27Y^{6k}\), this is its unique
place at infinity.

This global curve is nevertheless not residual.  On \(Z=1\), setting
\(b=X^2-Y^{3k}\) and \(r=-3b/(2X)\) gives its normalization birationally as
\[
Y^{3k}=r^3(9r-2).
\]
The valuation \(1\) makes this Kummer cover connected, and the branch valuations
\(3,1,-4\) give by Riemann--Hurwitz
\(2g-2=3k-5\), hence \(g=(3k-3)/2>0\); moreover \((0,0)\) has multiplicity
three.  The witness therefore refutes an infinity-orders-only kill without
supplying a rational residual curve.

## 5. The \(g\ge3\) inner case: braid fixedness and the correct invariant

For a transposition block \(T=(t_1,\ldots,t_g)\), the left Hurwitz action is
\[
\sigma_iT=(\ldots,t_it_{i+1}t_i^{-1},t_i,\ldots).                         \tag{5.1}
\]
Thus \(\sigma_iT=T\) exactly when \(t_i=t_{i+1}\), and the common fixed locus of
all \(B_g\) is the diagonal locus \((\tau,\ldots,\tau)\).  SK-2 uses two facts in
this order: at \(g=2\), product one forces \((\tau,\tau)\); consequently **every**
possible inner braid fixes each block; only then does the outer \(u\)-cycle force all
blocks equal (SK:171--183; REV:82--84).

The review's shorthand needs this correction.  For odd \(g\), a product-one
transposition block is impossible by sign.  For even \(g\ge4\), diagonal product-one
blocks are \(B_g\)-fixed, but product one does not force diagonality; for example
\(((12),(12),(23),(23))\) is changed by \(\sigma_2\).  It is that implication, not
the existence of fixed blocks, which fails.

The correct invariant is the **labeled Hurwitz fiber and its stabilizer**.  The graph
\(\Gamma(T)\) on four letters whose edges are the factors records
\[
H(T)=\langle t_1,\ldots,t_g\rangle
=\prod_{V\in\pi_0\Gamma(T)}S_V;
\]
Hurwitz moves preserve its component vertex sets and the number of factors in each
component, as well as the ordered product.  For product-one blocks, write the actual
inner braid as \(\iota=(\beta_1,\ldots,\beta_u)\).  Since the permutation underlying
\(\delta_u^2\) is the single cycle \(q(i)=i+2\pmod u\), literal return is
\[
T_{q(i)}=\beta_iT_i,\qquad
\beta_{q^{u-1}(i)}\cdots\beta_{q(i)}\beta_i
   \in\operatorname {Stab}_{B_g}(T_i).                                    \tag{5.2}
\]
For nontrivial products the same statement carries the cabled conjugations.  Product,
parity, or exponent sum alone loses the stabilizer condition.

There is one small genuine kill inside (5.2).  A connected transposition graph on four
vertices whose product is one needs at least six edges: reading partial products from the
identity, a connected graph needs at least three cycle-joining transpositions, and return
to the identity needs as many cycle-cutting ones.  Hence at \(g=4,c=1\) every block has
a proper support partition; (5.2) forces the same labeled partition around the outer
cycle, so the total image is proper.  For every even \(g\ge6\), however,
\[
((12),(12),(23),(23),(34),(34))
\]
(padded by equal pairs) has product one, generates \(S_4\), and has an exponent-one
stabilizer.  Thus this pin does not close the family.

More strongly, the known total inner exponent is non-obstructive at every \(g\ge3\).
Choose an \(S_4\)-generating block \(T_g\), padding by equal pairs as necessary:
\[
\begin{array}{c|c|c}
g&T_g&c=\prod T_g\\ \hline
3&((12),(34),(23))&(1243)\\
g\ge4\text{ even}&((23),(23),(12),(34))&(12)(34)\\
g\ge5\text{ odd}&((34),(34),(23),(23),(12))&(12).
\end{array}                                                               \tag{5.3}
\]
Repeat \(T_g\) in all \(u\) blocks.  Then \(X=Y=c\), so (1.2) holds.  Let
\(Z_g=(\sigma_1\cdots\sigma_{g-1})^g\); it has exponent \(g(g-1)\) and acts by
simultaneous conjugation by \(c\).  The cable formula gives
\[
C_g(\delta_u^2)(S_1,\ldots,S_u)
=(c^uS_{u-1}c^{-u},c^uS_uc^{-u},S_1,\ldots,S_{u-2}).                       \tag{5.4}
\]
Taking the last two inner components to be \(Z_g^{-u}\), and initially taking all
others to be the identity, makes (5.4) return the repeated tuple.  For \(g\ge4\),
an equal adjacent pair supplies an exponent-one stabilizer, so one remaining
component can adjust the total exponent to any prescribed integer.  At
\(g=3\), \(\sigma_1^2\) stabilizes the first, disjoint pair; the required
\[
e(\iota)=gu-1+2\delta_{\rm aff}-2g(gu-g)                                  \tag{5.5}
\]
is even, so it too can be matched exactly.

This is an abstract tubular fixed tuple with image \(S_4\), not a residual-curve
existence theorem: the geometric \(\iota\) is a specific braid, not an arbitrary braid
with the same exponent.  The case is therefore **pinned further but OPEN** at
`OPEN[INNER-NIELSEN-WORD-ACTION]`: recover the blockwise braid word from the actual
Puiseux/resolution data and test the induced cabled transport among the
product-indexed labeled fibers
\[
\mathcal F_g(P_i)=\{T:\prod T=P_i,\ \langle T\rangle=S_4\},
\]
where the \(P_i\) alternate between \(X\) and \(Y\) in the general stratum.

## 6. Case-by-case disposition and remaining named tools

The exact disposition is:

| Case | What is now proved | Verdict |
|---|---|---|
| \(g=2,\ (d,n)=(2u,2)\) | Lemma SK-2/Corollary SK-2' applies unchanged. | **KILLED uniformly** (consumed charged result). |
| \(g=2,\ (d,n)=(2u,4)\), \(u\not\equiv3\pmod6\) | The outer \(A_4\) classification admits no \(S_4\)-capable tuple. | **KILLED uniformly** by SK-4. |
| \(g=2,\ u=3\), hence \((d,n)=(6,4)\) | The explicit degree-six ROW-NF/ROW-KILL theorem applies. | **KILLED**, conditional only on its already promoted ROW-NF identification. |
| \(g=2,\ u\equiv3\pmod6,\ u\ge9\) | The \(S_3\)-resolvent descends; \(d=2u=6k\).  Under affine \(A_{2\ell-1}\)-exhaustiveness, every exact index-one equation \(F=4A^3+27B^2\) of degrees \((6k;2k,3k)\) contradicts the affine delta budget and one-place germ. | **PINNED FURTHER, OPEN** at OPEN[SHAPE-2-CARDANO-INDEX-ONE] and OPEN[AFFINE-ALL-A_ODD]. |
| \(g=4,\ X=Y=1\) inside family 2 | Each product-one four-transposition block has a disconnected factor graph, hence lies in a proper Young subgroup; its labeled components are preserved around the cable cycle. | **KILLED sub-stratum**. |
| General family 2 with \(g\ge3\) | The outer relation and the integer (5.5) admit abstract \(S_4\)-generating fixed tuples.  They do not determine the action of the geometric inner word. | **PINNED FURTHER, OPEN** at OPEN[INNER-NIELSEN-WORD-ACTION]. |

For the fourth row, splitting
\(\mathcal T_\pi\simeq\mathcal O(-k)\oplus\mathcal O(-2k)\) would supply the
index-one equation, but is stronger than needed; this is the charged
OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT].  The conditional torus kill would still
need the separately typed affine exhaustiveness.  A second honest route, potentially
bypassing both, is
OPEN[SHAPE-2-INFINITY-Z3]: apply Tokunaga's divisor-class criterion directly on
the double plane, including the infinity singularity and every tangential affine
\(A_{2\ell-1}\) point.  The present lane proves none of these missing inputs.  In
particular it does not upgrade resolvent descent, numerical divisibility, or the
conditional NO-TORUS proposition into a uniform kill.

For odd \(g\), the total product has odd sign and is outside \(V_4\), so this
\(S_3\)-descent route is unavailable.  For even \(g\ge6\), even the \(c=1\)
stratum has abstract connected product-one blocks.  Both observations reinforce
that the word-level inner tool, rather than exponent or product data, is the correct
remaining test.

## 7. Primary sources and audit notes

The frozen root was
/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.YKynio/inputs.
Before reading, SHA-256 verification returned exactly:

~~~text
189bc45d83c97df3614c65450a8c6e926938e50f7ccc0b2bacd78a7fd8d11c4d  shape-kill-uniform-opus5-20260901.md
0213fcae67bbde4d426a50f2d5d17c71db907d78718860459f14ff50e2ce4a01  shape-kill-hostile-review-grok46-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
~~~

Primary literature consulted:

1. Taketo Shirane, [“A note on normal triple covers over
   \(\mathbb P^2\) with branch divisors of degree
   6”](https://arxiv.org/abs/1211.2526), Kodai Math. J. 37 (2014),
   330--340, DOI 10.2996/kmj/1404393890.  The exact arXiv v1 PDF stream
   had SHA-256
   b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153.
   Sections 1.1.5 and 1.1.7 and Corollaries 0.6 and 2.3 are the portions
   used in §3.
2. Rick Miranda, [“Triple Covers in Algebraic
   Geometry”](https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf),
   Amer. J. Math. 107 (1985), 1123--1158, DOI 10.2307/2374349.  The
   author-hosted PDF stream had SHA-256
   0bfbaaf77c3c795189d5645466dd3d3ee32b872f5c962309751142d65535f875.
   This supports the rank-two Tschirnhausen structure, not a splitting
   assertion.
3. Carlos Galindo and Francisco Monserrat, [“The Abhyankar--Moh theorem
   for plane valuations at infinity”](https://arxiv.org/abs/0910.2613),
   J. Algebra 374 (2013), 181--194, DOI
   10.1016/j.jalgebra.2012.11.001.  The exact arXiv v2 PDF stream had
   SHA-256
   637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9.
   Its Proposition 2.1 supplies the delta/maximal-contact conversion used in
   (4.1)--(4.2); the conductor and the resulting characteristic numerator are
   then calculated explicitly in §4.
4. T. Ben-Itzhak and M. Teicher, [“Graph Theoretic Method for
   Determining non Hurwitz Equivalence in the Braid Group and Symmetric
   group”](https://arxiv.org/abs/math/0110110), arXiv:math/0110110v1.
   The PDF stream had SHA-256
   808c7959381560b53a6c5c860d1ee3ef33a1cd9b2d956e91fb8dddf9c9575999.
   Its weighted-component invariant corroborates the direct Hurwitz
   calculation in §5.
5. Hiro-o Tokunaga, “Triple coverings of algebraic surfaces according
   to the Cardano formula,” J. Math. Kyoto Univ. 31-2 (1991), 359--375.
   The indexed scan was inspected for the Cardano/minimal-splitting
   framework.  No stable original-byte endpoint was available, so no
   custody hash or purported general-degree index-one theorem is
   recorded.  In particular, this report does not cite Tokunaga for the
   missing implication isolated in §3.

No CAS was run.  Machine work was limited to bounded text inspection,
hashing finite streams, and checking the report.  The jc2-lean tree was
not inspected; no charged or canonical file was edited.  The proof keeps
the outer product, the actual geometric inner word, and its exponent sum
as three distinct data.  The torus conclusion is conditional rather than
an attainment claim; affine singularity exhaustiveness is separately typed
OPEN; and the local witness in §4 is retained as the negative control.  No
exit-price assertion is made in this lane.

<!-- BODY-END -->
