# Primary-source audit: Makar-Limanov shape and mate recovery

Date: 2026-08-24.  Repository basis: `a04affb7247fb5e87cad4e87f5926ab440254b24`.

## Verdict

**MIXED.**  The 2025 shape paper gives a genuine new necessary restriction on a specially reduced complex counterexample: the number of its admissible right edges is bounded by one less than the prime-factor length of the integral content of a particular vertex, and it separately excludes the ratio-two/vertical-edge configuration.  These statements are not a new bounded degree theorem, not a list of GGV admissible chains, and not a bridge from GGV data to Sigray pole trees.  On the data presently recorded in the campaign they eliminate none of `(72,108)`, residue-A, TD6, or the `(8,12)`/`(9,12)` maximum-partial-`y` branches.

The recovery paper proves, conditional on a polynomial mate already existing, that the mate is unique modulo `C[f]` and describes how its asymptotic terms are constrained by Newton/Puiseux reductions.  Its prose is algorithmic, but the published preprint does not give a finite, choice-independent, effective algorithm from arbitrary exact `f` to a mate: it assumes existence throughout, chooses Puiseux roots, allows a possibly countable resolution, does not give an a priori truncation/degree bound, and leaves some intermediate exponents to a final unspecified linear-algebra step.  It does not decide whether a mate exists and does not imply JC2.

Primary texts read in full:

- L. Makar-Limanov, [*On the shape of a counterexample to the two-dimensional Jacobian conjecture*](https://doi.org/10.55630/serdica.2025.51.299-314), Serdica Math. J. 51 (2025), 299–314; audit used the [official PDF](https://serdica.math.bas.bg/index.php/serdica/article/download/300/153/862).
- L. Makar-Limanov, [*A Jacobian mate defines the Jacobian pair*](https://doi.org/10.1007/s11856-025-2863-6), Israel J. Math. (2025); audit used the complete [official MPIM submitted version](https://archive.mpim-bonn.mpg.de/4771/1/mpim-preprint_2022-48.pdf), MPIM Preprint 2022 (48).  The MPIM record labels that PDF “Submitted Version.”  I did not obtain a publisher full text, so any claim that the journal pagination contains textual changes is quarantined as version drift.

No secondary technical source is used as mathematical authority below.  Campaign files are used only to compare scope and notation.

## 1. Shape paper: exact assertions and identities

The paper works over `C`.  Its bracket is

\[
J(a,b)=a_xb_y-a_yb_x.
\]

For a primitive integral weight `w=(alpha,beta)`, `w(x^i y^j)=alpha i+beta j`, `w(p)` is the maximum weight, and `p_w` is the corresponding form.  The paper's Newton polygon is the convex hull of the actual support; it does **not** automatically adjoin the origin.

### 1.1 Every theorem/lemma-level assertion

The following list includes the two numbered theorems and every named lemma carrying mathematical content.

1. **Lemma on the leading monomial.**  If `p,q in C[x,y]` are algebraically independent and leading monomials are taken in `w`-lexicographic order (`x >> y`) for any fixed weight `w`, then the semigroup of leading monomials of elements of `C[p,q]` contains two algebraically independent monomials.  The proof compares the quadratic growth `dim Span{p^i q^j:i+j<=N}=binom(N+2,2)` with linear growth if all leading exponent vectors lie on one ray.

2. **Lemma on independence.**  If `p,q in C[x,y]` are algebraically independent, `w` is a nonzero integral weight, and `p_w` is nonconstant, then there exists `r in C[p,q]` such that `r_w` and `p_w` are algebraically independent.  This follows because dependence of every leading form with `p_w` would force dependence of every leading monomial with the leading monomial of `p_w`, contradicting item 1.

3. **Divisibility lemma.**  If `rho,tau` are `w`-homogeneous elements in the setting constructed in the paper, `J(rho,tau)=rho`, `w(rho)>0`, `w(tau)>0`, and `rho` is not a monomial, then `w(rho)` does not divide `w(tau)`.  In particular `w(tau)/w(rho)` is not a positive integer.  The proof subtracts a scalar multiple of `rho^k` when that quotient is `k` and uses the preceding dependence argument.  This is not a statement for an arbitrary graded Poisson algebra; the ambient polynomial/rational homogeneous forms and the positivity hypotheses matter.

4. **Dependence lemma for total leading forms.**  If `(f,g)` is a counterexample with `J(f,g)=1`, its `(1,1)`-leading forms are algebraically dependent.  If they were independent, their bracket would be `1`, forcing affine-linear leading forms and hence an affine automorphism rather than a counterexample.

5. **Dependence lemma for weights.**  If `(f,g) in C[x,y]^2` is a counterexample with `J(f,g)=1` and `w=(alpha,beta)` satisfies `alpha+beta>0`, then `f_w` and `g_w` are algebraically dependent.  The proof treats the only possible independent case `J(f_w,g_w)=1`, reduces it to leading `x` and `y` terms, and shows that any extra mixed support leads to a second weight with the same forbidden pattern.  The condition `alpha+beta>0` is essential.

6. **Similarity lemma.**  After the paper's reduction, write the top vertex of `N(f)` as `(m,n)`, `0<m<n`, and the corresponding top vertex of `N(g)` as `(M,N)`.  After replacing one coordinate by a polynomial in the other so that `lambda=N/n` is neither an integer nor the reciprocal of an integer, the polygons obtained by adjoining the origin satisfy

\[
\operatorname{conv}(N(g)\cup\{0\})=\lambda\operatorname{conv}(N(f)\cup\{0\}).
\]

For every corresponding edge form, if `f_i=xi_i^{a_i}` for its maximal polynomial root, then `g_i=c_i xi_i^{b_i}` and `b_i/a_i=lambda`.  This is a source-dependent implication inside the reduced counterexample setup, not a statement about arbitrary Keller pairs.

7. **Lemma on forms.**  For a right edge `e_i`, `i>0`, and every `p in C[f,g]`, its `w_i`-form belongs to `C[xi_i,xi_i^{-1},tau_i]`, where `f_i=xi_i^{a_i}` and `J(f_i,tau_i)=f_i`.  The printed proof inducts on the nilpotence length of `J(f_i,-)` on the associated leading-form algebra.  The displayed antiderivative has the implicit integrality proviso that the residual exponent of `xi_i` exists as an integer.

8. **Dependence lemma for admissible edges.**  A right edge is “admissible” when at least one of its vertices lies strictly above the first-quadrant bisector.  If `e_i` is admissible and `p_i` is algebraically dependent with `f_i`, then `J(f_j,p_j)=0` for every integer `j` with `0<j<i`.  Consequently the same rational exponent propagates to all earlier right edges.

9. **Left-edge lemma.**  For the reduced left leading edge `e_0`, with `alpha<0<beta`, `alpha+beta<0`, and the formal/rational `tau` satisfying `J(f_0,tau)=f_0`, the leading monomials of `f_0` and `tau` are algebraically independent.  The proof uses `w(f_0)>0>w(tau)` and the support ray to rule out proportional exponent vectors.

10. **Theorem 1 (exact scope).**  If `f` is reduced in the paper's sense, there is no counterexample `(f,g)` with `deg_y f=2 deg_x f` and the stated vertical-edge condition at the first right edge (`e_1`; the PDF prints “vertical edge `v_1`,” apparently a notation slip).  The proof writes the leading monomial on that edge as `k(1,2)`, obtains `lambda_1=1/k`, transports polynomiality to the left edge, and forces the left-edge maximal root to have the form `xy^2+c`.  The forbidden intermediate `y` exponent is then `0`; hence `f(0,y)` is constant, and the constant-Jacobian row forces the first `g` coefficient to be affine, contradicting the earlier axis-degree restriction.

11. **Theorem 2 (exact scope).**  Let `(f,g)` be a counterexample in the paper's reduced setup.  Let `v_0` be the vertex of `N(f)` corresponding to the paper's barred (smallest, in the chosen weight-lex order) monomial `\bar f`.  Write

\[
v_0=D(a,b),\qquad D=\prod_{i=1}^k p_i^{\delta_i},\qquad \gcd(a,b)=1,
\]

where every `p_i` is prime.  Then the number `s` of admissible right edges of `N(f)` satisfies

\[
s\le \sum_{i=1}^k\delta_i-1.
\]

The proof associates to successive admissible edges reduced denominators `d_1>...>d_s`; each `d_{i+1}` divides `d_i`, each quotient is an integer greater than one, and the last denominator is divisible by at least one prime from `D`.  Thus the relevant denominator chain consumes prime factors of the vertex content.  **Quarantine:** `v_0` must not be silently identified with GGV's `A_0` or a displayed top corner without a separate geometric proof.

The statements called Remarks 1–7 are consequences or setup, not additional theorems.  In particular, “we just assume that `e_0` has slope larger than one” explicitly imports the exclusion of the bisector edge from papers [7]/[17]; it is a source-dependent normalization, not proved in this article.

### 1.2 Load-bearing re-derivations

For monomials,

\[
J(x^{i_1}y^{j_1},x^{i_2}y^{j_2})=(i_1j_2-i_2j_1)x^{i_1+i_2-1}y^{j_1+j_2-1}.
\]

Thus nonzero leading brackets have weight `w(a)+w(b)-w(xy)`.  With `partial=J(f,-)`, `partial(g^i)=i g^{i-1}` and therefore `partial` is locally nilpotent on `C[f,g]`; passing to leading forms gives local nilpotence of `J(f_w,-)` whenever the leading bracket does not cancel.  This is the engine behind the construction of homogeneous `rho,tau` with `J(rho,tau)=rho`.

Write `rho=x^r p(z)`, `tau=x^t q(z)`, `z=x^{-beta/alpha}y`.  Direct differentiation gives

\[
r p q'-t p'q=p,
\]

or, multiplying weights,

\[
w(rho)pq'-w(tau)p'q=\alpha p. \tag{S1}
\]

Dividing (S1) by `pq` yields

\[
\left(\log(q^{w(rho)}p^{-w(tau)})\right)'=\frac{\alpha}{q},
\]

hence

\[
p^{w(tau)}=q^{w(rho)}\exp\!\left(-\int\frac{\alpha\,dz}{q}\right). \tag{S2}
\]

The pole/root multiplicity conclusions in the paper follow from residues of `1/q`.  They require characteristic zero and algebraic closedness for factorization and the exponential-residue argument.

For similarity, `J(f_i,g_i)=0` in `C[x,y]` implies the homogeneous forms share a maximal root: `f_i=xi_i^{a_i}`, `g_i=c_i xi_i^{b_i}`.  Equality `b_i/a_i=lambda` starts at the common top monomial and propagates because the terminal monomial of one edge is the initial monomial of the next.  This proves homothety only after adjoining the origin and only along the connected boundary chain actually treated.

For Theorem 2, let `mu_i=w_i(p)/w_i(f)` and `lambda_i=w_i(tau_i)/w_i(f)`.  From `p_i=tau_i xi_i^{d_i}` and `f_i=xi_i^{a_i}`,

\[
\mu_i=\lambda_i+d_i/a_i.
\]

Earlier-edge polynomiality of both `f_j^{\mu_i}` and `f_j^{d_i/a_i}` forces `f_j^{\lambda_i}` polynomial for `j<i`, whereas the divisibility lemma says `f_i^{\lambda_i}` is not.  Reduced denominators therefore strictly drop along admissible edges and divide their predecessors.  This is the exact arithmetic content of the edge-count theorem; it does not bound the sizes of the vertices.

### 1.3 Published result versus choices and heuristics

- **Published:** the named lemmas and Theorems 1–2 above, over `C`, under the paper's reduced-counterexample hypotheses.
- **Source-dependent:** existence of the initial trapezoidal/reduced shape; collapse of the bisector-parallel left edge; facts about maximal roots of homogeneous forms; and the polynomial centralizer facts cited in the recovery paper.
- **Normal-form choices:** repeated polynomial automorphisms that decrease `deg_x f+deg_y f`; swapping `(x,y)` to arrange `m<n`; translating `y`; replacing `g` by `g-p(f)`; and selecting the coordinate with smaller degree ratio.  These choices are not shown canonical and are not linked to GGV global minimality.
- **Heuristic/prose:** “further information” and “we can find” do not by themselves provide an enumeration algorithm or complexity bound.

## 2. Exact comparison with GGV and the campaign

### 2.1 Notation map

| Shape paper | Meaning | GGV/campaign counterpart | Exactness warning |
|---|---|---|---|
| `w=(alpha,beta)`, `w(p)` | maximum linear weight | `v_{rho,sigma}(P)` with `(rho,sigma)=(alpha,beta)` | Same maximum convention. |
| `p_w` or `p_i` | leading form on edge `e_i` | `ell_{rho,sigma}(P)` | Same face form after matching direction. |
| smallest/leading monomial on an edge | endpoint under `w`-lex order | `st_{rho,sigma}`, `en_{rho,sigma}` | Which endpoint is `st` depends on GGV's orientation; it must be checked by cross product, not guessed. |
| `N(f)` | convex hull of actual support | GGV `Newt(P)`/campaign hull | GGV campaign often adjoins `(0,0)` by convention; shape paper adjoins it explicitly only in the similarity lemma. |
| top vertex `(m,n)` of `f` | `(deg_x f,deg_y f)` after reduction, `m<n` | a geometric corner, not GGV's coprime ratio `(m,n)` | **Name collision:** GGV reserves `(m,n)` for coprime degree-ratio parameters. |
| top vertex `(M,N)` of `g`; `lambda=N/n` | homothety ratio | `v(P)/v(Q)=m_GGV/n_GGV` (or its reciprocal, depending which coordinate is `P`) | In GGV standard notation, if `f=P`, `g=Q`, then `lambda=deg(g)/deg(f)=n_GGV/m_GGV`. |
| `e_1,e_2,...` | right boundary edges from top to `x`-axis | successive regular corners/directions in an admissible chain | Not every GGV admissible-chain condition is proved here, nor conversely. |
| admissible edge | at least one vertex above `i=j` | no exact one-word GGV equivalent; a geometric subset of regular corners | Do not equate with GGV “admissible chain.” |
| `xi_i`, `a_i,b_i` | maximal common root and powers `f_i=xi_i^{a_i}`, `g_i=c xi_i^{b_i}` | GGV common homogeneous factor/power data (`R`, `m,n`, `q`) | Local exponents, not Sigray pole-entry `(a_i,b_i)`. |
| `tau_i`, `J(f_i,tau_i)=f_i` | Dixmier auxiliary form | GGV homogeneous `F/G/R` bracket auxiliaries | Similar mechanism, no proved objectwise identification. |
| reduced denominators `d_i` | denominators of propagated weight ratios | denominators/divisibility data along GGV regular corners | No theorem identifies the sequences term-for-term. |
| shape `v_0=D(a,b)`, `gcd(a,b)=1` | vertex of the barred/smallest monomial; `D=gcd(v_{0x},v_{0y})` is its integral content | no pinned GGV symbol | Must not be called GGV `A_0` or the displayed top corner without proof. |

GGV's **standard minimal `(m,n)`-pair** is globally selected among all counterexamples by minimum `gcd(deg P,deg Q)`, with coprime degree-ratio parameters and valuation inequalities.  Makar-Limanov's **reduced `f`** is obtained by local polynomial automorphisms minimizing the positive-quadrant leading shape and translating an axis polynomial.  Neither paper proves these normal forms can be imposed simultaneously while preserving the detailed corner chain.  Therefore the shape theorem cannot simply be appended as another GGV chain predicate.

### 2.2 Does it strengthen the current foundation?

Conceptually, yes: Theorem 2 is an additional necessary restriction on the number of above-bisector right edges in a reduced complex counterexample, expressed through prime factors of the integral content `D` of `v_0`.  Theorem 1 is an additional ratio-two exclusion under a vertical-edge hypothesis.  Operationally, on the present campaign foundation, **no**: the repository does not identify the required `v_0`, prove that its GGV minimal pairs are in this reduced frame, or provide a transport of edge order and maximal-root denominators.

Consequences by active branch:

- **`(72,108)`: no narrowing.**  The GGV objects are Laurent-normalized pairs satisfying `[P,Q]=x^2` after a non-polynomial final map, not the original `J=1` reduced pair.  The two Proposition 4.3 polygons have top corners `(8,16)` and `(12,24)` in the reduced system, but those are scaled system corners and do not identify the theorem's primitive `v_0`.  The ratio of displayed top coordinates is two, yet Theorem 1 additionally requires the paper's reduced frame and its vertical-edge condition.  Neither is certified after GGV's Laurent transformations.  Applying Theorem 1 merely from `(8,16)` would be an overread.
- **Residue-A two-pole template: no narrowing.**  It is Sigray pole-tree data, not a Newton polygon with a provenanced barred-monomial vertex `v_0`.  `G2-PSC` remains missing.
- **TD6: no narrowing.**  Topological degree six and the eight terminal pole classes do not determine the number of Makar-Limanov admissible edges or the prime factorization in Theorem 2.
- **Maximum-partial-degree `(8,12)` and `(9,12)`: no narrowing.**  These are actual `y`-degree coefficient branches in a different shear/UFD/Faber normal form.  The shape paper uses a top exponent pair `(deg_x f,deg_y f)` after source automorphisms; `8,12` and `9,12` are the two coordinates' `y`-degrees, not that pair.  Theorem 1's ratio two is irrelevant, and Theorem 2 lacks its `v_0` input.
- **Finite book/tower software: no new predicate.**  `BOOK` enumerates pole-entry/tree/jump data at fixed `td`; tower checkers verify decorated routes.  None computes the Newton vertex or edge correspondence required here.  Adding a naked “number of edges” filter would be unsound.

Thus the shape paper is strictly stronger only as a theorem about its own reduced Newton frame, not stronger than the campaign's current **usable** GGV-to-book foundation.

## 3. Recovery paper: theorem, reconstruction, and effectiveness

### 3.1 Exact main statement and named lemmas

The paper assumes throughout that `f in C[x,y]` has at least one polynomial mate `g in C[x,y]` with `J(f,g)=1`, and after a polynomial automorphism assumes the cited trapezoidal shape with top monomial `x^m y^n`, `0<m<n`, no bisector-parallel edge.

Its main, unnumbered theorem is:

> For every such `f`, the subalgebra `C[f,g]` is independent of the choice of polynomial `g` satisfying `J(f,g)=1`; the mate can be reconstructed from `f` up to addition of an element of `C[f]`.

Equivalently, if `g,h in C[x,y]` both satisfy `J(f,g)=J(f,h)=1`, then `h-g in C[f]`, hence `C[f,h]=C[f,g]`.  The quantifier begins with **two existing polynomial mates**; it neither asserts nor decides their existence.

Named supporting assertions are:

1. **Radical lemma.**  In `A=C[x,x^{-1}]((y^{-1}))` written as series bounded above in `y`, if `a` has monomial leading form `c x^l y^k`, `r in Q`, and the chosen leading power `|a|^r` belongs to `A`, then the compatible binomial expansion `a^r` belongs to `A`.  A branch of the scalar/root is chosen so the leading coefficient is fixed.
2. **Positive-reduction lemma.**  Assuming a mate exists and `f` is shaped as above, at least one Newton-Puiseux reduction `f_k(x,y)=f(x,y+y_k)` has a positive principal edge.  The construction repeatedly chooses a root of multiplicity greater than `w_e(xy)/w_e(f)`; the proof uses the unseen mate to rule out reaching a nonpositive edge.
3. **Degree lemma.**  For every polynomial `p` algebraically dependent with `f` (the paper denotes the resulting relative algebraic-closure subalgebra by `C(f)`),
\[
\deg_y J(p,g)-\deg_y p\le -\deg_y f.
\]
The printed proof chooses an element maximizing the left-hand degree drop and derives a contradiction by canceling its leading fractional power of `f`.
4. **Centralizer conclusion.**  If `p in C[x,y]` and `J(p,f)=0`, then `p in C[f]`.  The proof invokes algebraic dependence, the degree lemma, integration under `J(-,g)`, and algebraic independence of `f,g`.  This is also attributed to Nousiainen.

### 3.2 Reconstruction, with every choice exposed

Normalize the leading coefficient so `|f|=x^m y^n`.  For an existing mate, cancellation of the top bracket gives

\[
|g|=c_0|f|^{\lambda_0},\qquad \lambda_0\in\mathbf Q.
\]

Repeatedly subtract compatible fractional powers in `A`:

\[
g_s=g-\sum_{i<s}c_i f^{\lambda_i},\qquad
\lambda_0>\lambda_1>\cdots.

\]

When the leading bracket first becomes one, direct solution of
`J(x^m y^n,|g_kappa|)=1` gives

\[
|g_\kappa|=\frac{1}{m-n}x^{1-m}y^{1-n}.
\]

The alternative homogeneous solution proportional to
`(x^m y^n)^{(1-n)/n}` is excluded because `0<m/n<1` makes the required `x` exponent nonintegral in `A`.  Therefore

\[
g=\sum_{i=0}^{\kappa-1}c_i f^{\lambda_i}+g_\kappa. \tag{R1}

\]

Next choose a Newton-Puiseux root `y_k` of `f(x,y)=0` as a descending fractional series in `x` and set `f_k=f(x,y+y_k)`, `g_k=g(x,y+y_k)`.  Since `f_k(x,0)=0`, the constant term of the bracket is

\[
1=-g_{k,x}(x,0)f_{k,y}(x,0). \tag{R2}
\]

Thus the principal vertex of `f_k` is `(mu(k),1)`, `mu(k) != 1`, and the corresponding vertex of `g_k` is `(1-mu(k),0)` or `(0,0)`.  The positive-reduction lemma says some choice of root path has a positive chain from leading to principal edge.

On a chosen positive edge, use `w(x)=1`, `w(y)=-alpha`, `z=x^alpha y`, and write

\[
f_k(e)=x^\rho p(z),\qquad g_{k,s}(e)=x^\sigma q(z).

\]

After subtracting all leading fractional powers of `f_k` on that edge, `J(f_k(e),g_{k,s}(e))=1`, so

\[
\rho p q'-\sigma p'q=1. \tag{R3}

\]

With `r=pq` and `tau=rho+sigma`, (R3) is exactly

\[
\rho p r'-\tau p'r=p,\qquad
p^\tau=r^\rho\exp\!\left(-\int dz/r\right). \tag{R4}

\]

For a positive edge `rho,tau>0`; pole comparison in (R4) forces `r` to be a polynomial, and its roots are simple.  Its partial fractions determine root multiplicities of `p`; a negative residue yields a root multiplicity larger than `tau/rho`, enabling the next positive Newton step.

At the principal edge, the proportional degree vertices give

\[
(1+\lambda_0)w(f_k)=w(xy), \tag{R5}

\]

so its line determines `lambda_0`.  Then solve the linear polynomial ODE (R3) for `q`; coefficient comparison determines `c_0`.  Repeat along the other edges for further `lambda_i,c_i`.  The paper explicitly acknowledges that vertices may hide intermediate exponents.  It finally states that if `d=gcd(m,n)` and `lambda_0=m_0/d`, then

\[
g=\left[\sum_{i=0}^{m_0}c_i f^{(m_0-i)/d}\right]_+, \tag{R6}

\]

where brackets mean polynomial part, and the remaining `c_i` are found by solving the exact linear identity

\[
\sum_i c_i J\!\left(f,[f^{(m_0-i)/d}]_+\right)=1. \tag{R7}

\]

Every operation in (R7) is linear in the unknown constants once the fractional-power polynomial parts have been computed.

Choices are: the initial shaping automorphism; which coordinate is `f`; normalization of its leading scalar; a compatible branch for every rational power; an initial Newton edge and root; at each multiple root, which root continues the reduction; a common denominator/root-of-unity embedding for Puiseux series; the positive reduction among the possible paths; representatives modulo `C[f]`; and a basis/normalization for the nullspace of (R7).  Different choices are not proved to yield identical representatives, only the same class modulo `C[f]` once a polynomial mate exists.

### 3.3 Termination and field assumptions

- The successive cancellation in the initial `y`-asymptotic series terminates for an existing polynomial `g` because its leading `y` degree strictly decreases until the bracket-leading term is `1`.  This is an existence-dependent termination argument; it supplies no bound from `f` alone.
- The Newton process is expressly allowed “possibly a countable number of steps.”  Characteristic zero bounds Puiseux denominators by `deg_y f`, but a denominator bound is not a step bound or coefficient-height bound.
- A fixed polynomial has finitely many polygon edges after a completed reduction, but obtaining the exact series root and knowing that the principal edge has been reached may require unbounded information.  The paper gives no effective stopping certificate from `f` alone.
- `C` is used for algebraic closedness, all roots of unity, factorization, residues, and characteristic-zero division/binomial coefficients.  Several formal identities extend to an algebraically closed characteristic-zero field; the paper does not formulate or prove that generalization, and the analytic word “asymptotic” is implemented formally, not by a convergence theorem.
- `A_w` is a union of Puiseux/Laurent series rings with element-dependent denominator.  Exact compilation therefore needs algebraic-number representations and branch bookkeeping absent from the paper.
- Solving (R3)/(R7) is effective after finite exact inputs are supplied.  The paper does not show how to enumerate a complete finite set of those inputs from arbitrary `f`, nor give a complexity estimate.

Accordingly the recovery construction is **constructive conditional mathematics**, but not a total exact algorithm for the mate-existence problem.

### 3.4 Hostile proof/effectiveness notes

1. The abstract's “if `f` is given” suppresses the standing promise that a polynomial mate exists.  Removing that promise changes the problem fundamentally.
2. The passage “after a finite number of steps” in edge cancellation is justified by the existing rational/polynomial `g_k`, not by a computable bound derived from `f_k(e)` alone.
3. The positive-reduction proof repeatedly reasons with the unknown `N(g_k)`.  It certifies existence of a good path but does not identify one using `f` alone without search and a finite completeness bound.
4. The article says the edge data find many but “not all” intermediate `lambda_i`; (R7) is the repair, but `m_0` and the finite exponent window must already be known.  No general input-size/degree bound is stated.
5. The centralizer proof uses `C(f)` for the algebraic-closure subalgebra rather than the rational function field and chooses a “minimal degree” element without spelling out the well-ordering/domain conventions.  The conclusion is a known cited theorem, but this presentation is not implementation-ready.
6. A kernel vector of (R7) can represent addition of `p(f)`.  Software must quotient or normalize it; treating a nonzero kernel as multiple inequivalent mates would be wrong.
7. No step shows `x,y in C[f,g]`.  Knowing the subalgebra from `f` does not prove that it is `C[x,y]`.

## 4. Exact controls

### 4.1 Nontrivial polynomial automorphism

Let

\[
u=x+y^2,\qquad f=y+u^3,\qquad g=-u.
\]

This is a composition of triangular automorphisms (up to the sign of the second target coordinate), and

\[
f_x=3u^2,quad f_y=1+6yu^2,quad g_x=-1,quad g_y=-2y,
\]

so

\[
J(f,g)=-6yu^2+(1+6yu^2)=1.
\]

Its top monomial is `x^3y^6`, so `(m,n)=(3,6)` and `d=3`.  Formally at infinity,

\[
f^{1/3}=u\left(1+y/u^3\right)^{1/3}=u+\text{negative powers of }u.
\]

Hence `[f^{1/3}]_+=u`, and the recovery representative is `-[f^{1/3}]_+=-u=g`.  Every other mate with bracket one is `g+p(f)`.  This is a positive exact control; it tests both fractional-power extraction and the modulo-`C[f]` ambiguity.

### 4.2 Campaign formal/truncated maximum-12 control

Take the `(8,12)` high-row Faber specialization

\[
f=z^8+xz^6,
\]

and the exact polynomial part

\[
\begin{aligned}
g=F_{12}=[f^{3/2}]_+={}&z^{12}+\frac32xz^{10}+\frac38x^2z^8-\frac1{16}x^3z^6\\
&+\frac3{128}x^4z^4-\frac3{256}x^5z^2+\frac7{1024}x^6.
\end{aligned}
\]

This is an exact specialization of the campaign's formal maximum-12 Faber ansatz, not an assertion that a campaign component exists.  Direct exact differentiation gives

\[
f_xg_z-f_zg_x=-\frac{63}{256}x^6z^5.
\]

Since `m=8`, the result has `z`-degree `5<=m-2=6`; all higher Jacobian rows vanish exactly, as the current Faber compiler promises.  It is not `1`, so this truncated/formal pair is **not a polynomial mate**.  The recovery expansion trivially returns the displayed `F_12` from its chosen Faber constant, but cannot turn the surviving lower row into a mate.  This is the required negative discipline control: finite high-row agreement is not existence.

## 5. Smallest fail-closed software client

No new recovery-paper client can soundly replace the full pair-variable system in residue-A, TD6, or the GGV `(72,108)` systems: those branches do not supply a single exact shaped `f`, a proven finite Puiseux path, and an a priori mate-degree/exponent bound.  The maximum-12 branch already has the sound portion of the recovery idea in a smaller and cleaner form: the reviewed unitriangular Faber high-row compiler eliminates high `g` coefficients.

The smallest useful addition is therefore a **bounded conditional verifier**, not a mate finder:

`RECOVER-BOUNDED(f, n, normalization, branch_data)`

- **Input:** an exact characteristic-zero coefficient domain; a monic/depressed polynomial `f in K[x][z]` of `z`-degree `m`; a declared mate `z`-degree `n`; a finite list of rational exponents/branches or, for the active maximum-12 client, the canonical monic root `w=f^(1/m)=z+O(z^-1)`; exact polynomial-boundary constraints; and an explicit normalization selecting a representative modulo `K[f]`.
- **Operation:** construct only the finitely required polynomial parts `[f^{j/m}]_+` (or Faber `F_j`), express `g_0=sum h_jF_j`, impose character filters and normalization, and solve every coefficient of `J(f,g_0)-1=0` linearly in the remaining `h_j` where it is linear.  Reconstruct the original `(x,y)` coordinates and check all Taylor-boundary/polynomiality constraints.  Never infer a missing exponent or Puiseux branch.
- **Positive output:** an explicit polynomial `g_0` plus a certificate consisting of (i) exact coefficient-domain metadata, (ii) the finite series identities used to construct each polynomial part, (iii) the complete coefficient list of `J(f,g_0)-1`, all zero, (iv) every boundary reconstruction identity, and (v) the normalization modulo `K[f]`.  A checker recomputes these from scratch.
- **Negative output:** only `NO-MATE-IN-DECLARED-BOUNDED-ANSATZ`, backed by an exact row-reduction/Farkas-style linear inconsistency certificate or a Gröbner/ideal certificate over the declared domain.  It must never print “no mate” for omitted branches, exponent windows, or degree bounds.  `UNKNOWN/INCOMPLETE-BRANCH-DATA` is mandatory whenever completeness is not certified.
- **Positive control:** the automorphism pair in section 4.1, recovering `-u` and verifying Jacobian one.
- **Negative controls:** the section 4.2 Faber truncation, which must retain the nonzero `-63x^6z^5/256` lower row; and `f=x^2+y^2`, for which the coefficient equations cannot yield a polynomial bracket-one mate in any declared bounded ansatz (with the output scoped to that ansatz unless a separate theorem certificate is supplied).
- **Complexity:** construction of Faber parts through degree `n` is polynomial in `n` arithmetic operations for dense univariate-in-`z` coefficient arrays (naively `O(n^2 m)` coefficient-ring operations; sparse growth depends on coefficient support).  The final coefficient solve is polynomial in the number of retained linear unknowns (`O(RH^2+H^3)` dense elimination for `R` rows, `H` unknown constants).  Polynomiality/boundary expansion can dominate through coefficient swell.  If nonlinear coefficient functions of `f` are themselves unknown, the system again becomes nonlinear and no polynomial complexity claim is licensed.

For the active `(8,12)`/`(9,12)` branch this client can certify and package the already-used high-row elimination, then fail closed on the lower Laurent fibres.  It does not currently reduce the genuinely open pair-variable portion beyond the existing Faber compiler.  Therefore **no new active client from the recovery paper is presently sound enough to promote as a replacement**.

## 6. Promotion and quarantine wording

### Promotion

> **MAKAR-LIMANOV SHAPE — CONDITIONAL REDUCED-FRAME NECESSARY CONDITIONS.**  Over `C`, for a counterexample in Makar-Limanov's reduced Newton frame, the ratio-two case with the paper's vertical first-right-edge condition is impossible.  If the vertex of the barred/smallest monomial is `v_0=D(a,b)`, `gcd(a,b)=1`, and `D=prod p_i^{delta_i}`, the number of admissible right edges is at most `sum delta_i-1`.  No compatibility with the campaign's GGV-minimal frame or Sigray frame is presently proved.

> **MATE RECOVERY — EXISTENCE-PROMISED UNIQUENESS/RECONSTRUCTION.**  If `f in C[x,y]` already has a polynomial mate and the paper's shaped setup is imposed, its asymptotic/Faber data constrain a representative `g`; any two polynomial mates with Jacobian one differ by an element of `C[f]`, so `C[f,g]` depends only on `f`.  Finite exact reconstruction is certified only after finite branch and degree/exponent data are supplied.

### Quarantine

> Do not infer existence of a polynomial mate from the recovery expansion, uniqueness as a literal polynomial rather than modulo `C[f]`, invertibility of `(f,g)`, equality `C[f,g]=C[x,y]`, or JC2.  Do not apply the shape edge bound to GGV polygons, `(72,108)`, residue-A, TD6, or maximum-partial-degree cells until an explicit normalization/notation bridge identifies the required reduced `v_0`, edge order, and maximal-root denominators.  Do not treat a finite Puiseux/Faber truncation or vanishing high Jacobian rows as a polynomial mate.

## 7. Ranked next actions (at most three)

1. **Bridge-or-stop test for the shape theorem.**  On one original (pre-Laurent-finalization) GGV family, formally track the source automorphisms into Makar-Limanov's reduced frame and machine-check the identity of `v_0`, admissible edges, and denominator chain.  If the map cannot be proved, record the shape theorem as permanently non-consumable by the GGV farm rather than adding heuristic filters.
2. **Add certificate packaging to the existing maximum-12 Faber compiler.**  Emit the complete `g` parameterization, all high-row zero coefficients, lower-row remainder, boundary reconstruction, and modulo-`C[f]` normalization in a small JSON checked independently.  This realizes the sound finite core of recovery without Puiseux overreach.
3. **Version-drift check.**  Obtain the Israel Journal publisher text for DOI `10.1007/s11856-025-2863-6` and diff theorem wording, hypotheses, and proof against MPIM 2022 (48), especially any revisions to termination, the degree lemma, and the final linear system.  Until then cite the MPIM text as the audited version.
