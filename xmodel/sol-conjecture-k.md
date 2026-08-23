# Conjecture K: the D23 torsion/component mechanism

Date: 2026-08-19

Scope: the residue-A, B-frozen, no-log, `PIN42`,
\(W_1W_2\ne0\) chart and the radical-fiber D21/D23 systems banked in this
repository. All theorem labels below are finite-field, fiberwise statements
unless explicitly promoted. There is no characteristic-zero or all-depth
claim.

## 0. Verdict

The premise that \(g_1,g_2,g_3\) have one constant-linear dependency
**is false**. In every one of the 72 fibers in the two atlases they span a
three-dimensional condition space. This was already the correction in
`sol-round5.md` section 2, and the banked payloads prove it directly.

There is nevertheless an exact source for the \(13\to11\) dimension cut.
In the D21 quotient there are nonzero zero-divisors \(q\) for which

\[
 q(g_2-\lambda g_1)=q(g_3-\mu g_1)=0.                 \tag{K.1}
\]

These are **two quotient-torsion syzygies**, not one constant syzygy. On
the open set \(D(q)\), they become

\[
 g_2=\lambda g_1,\qquad g_3=\mu g_1.                 \tag{K.2}
\]

Exact saturation proves, in all 36 \(p=105337\) atlas fibers and at
`a00pp` for \(p=105673,200257\), that

\[
 13\ \rightsquigarrow\ 12
 \quad\text{(select the \(q\)-open D21 stratum)}
 \quad\longrightarrow\quad
 11\quad\text{(one equation after localizing at \(q\))}.         \tag{K.3}
\]

The first arrow is passage from the 13-dimensional component stratum to a
lower-dimensional component stratum, not a second equation on one
irreducible 13-fold. The quotient syzygies themselves were recomputed in
all 36 fibers at each of \(p=105337,105673\). Radicality, irreducibility,
and uniqueness of the 12-dimensional \(q\)-open closure were not
established.

At the level of implications proved here:

1. **Proved modular source:** zero-divisor torsion and
   non-equidimensional/component selection already in \(S/I_{21}\).
2. **Not sufficient by itself:** the rank-two factorization
   \(A=C\operatorname{diag}(uW^2)\). Its directly proved consequence is
   the earlier \(4\to3\) compression.
3. **Not sufficient by itself:** the \((j-i)\bmod3\) grading. Its directly
   proved role is transport of coefficients and syzygies.
4. **CONJECTURE:** the torsion has a uniform pristine-row
   depth-ladder/Keller source. Neither the \(w\)-invariant nor Keller
   exactness currently derives (K.1).

No unconditional D25 or all-depth codimension law follows. The two precise
conditional recurrences are stated in section 8.

## 1. Objects and audit scope

For a specialized radical fiber over \(\mathbf F_p\), let

\[
\begin{aligned}
S_p={}&\mathbf F_p[
x_{68},x_{70},x_{71},x_{72},x_{73},x_{47},x_{52},x_{53},x_{54},
x_{55},x_{57},x_{58},x_{59},x_{60},x_{62},x_{63},x_{65},x_{66},\\
&W_1,W_2,uW_1,uW_2],\\
R_p={}&S_p/I_{21},\qquad J_{23}=I_{21}+(g_1,g_2,g_3).
\end{aligned}
\]

The chart equations \(W_i uW_i-1\) belong to \(I_{21}\). The audit used:

- `cases/nf_reduced_rows_p*.txt`;
- both 36-fiber `cases/d23_atlas_*.json` files;
- the three `cases/directionb_det23_p*.rows.txt` files and the banked
  397/509-element bases;
- `cases/d23_witnesses_p105337.json` and
  `cases/d23_witnesses_p105673.json`;
- the D21 core emissions, `SHEET6-DIRECTIONB.md` sections
  8.S5/8.S6/8.S8, `sol-round5.md` section 2,
  `sol-round6.md` section 2, and `grok-det23-review.md`.

“EXACT MODULAR” below means an exact normal form, finite-field rank,
leading-term dimension, or Rabinowitsch saturation. Matching modular
support is not silently promoted to characteristic zero.

## 2. The literal dependency is refuted

At \(p=105337\), `a00pp`, the canonical D21 normal forms are

\[
\begin{aligned}
g_1&=(x_{57}-x_{65})^2uW_1^2+50008x_{53}uW_1+103704x_{72},\\
g_2&=(x_{57}-x_{65})^2uW_2^2+4803x_{58}uW_2+13955x_{72},\\
g_3&=x_{70}+52700x_{72}.
\end{aligned}                                                   \tag{K.4}
\]

Suppose \(a g_1+b g_2+c g_3\in I_{21}\), with
\(a,b,c\in\mathbf F_p\). Since the \(g_i\) are already canonical normal
forms, their linear combination is supported on standard monomials. The
coefficients of the private monomials

\[
 x_{57}^2uW_1^2,\qquad x_{57}^2uW_2^2,\qquad x_{70}
\]

are \(a,b,c\), respectively. Thus \(a=b=c=0\). Those same private
monomials occur with coefficient one in every atlas fiber.

> **EXACT MODULAR THEOREM 2.1.** The three classes
> \(g_1,g_2,g_3\in R_p\) are constant-linearly independent in all 72
> fibers of the \(105337\) and \(105673\) atlases, and in the third-prime
> `a00pp` payload at \(p=200257\).

Every one of the 36 fibers at each atlas prime has the exact signature

\[
(\dim\langle g\rangle,\operatorname{rank}w,
  \operatorname{rank}\mathrm{NF},\dim\ker\mathrm{NF},
  \operatorname{rank}C,\dim V(I_{21}),\dim V(J_{23}))
=(3,3,5,1,2,13,11).                                      \tag{K.5}
\]

There are zero anomalies. In the saturation-tested fibers, the two-unit
drop in maximum dimension comes from a non-equidimensional base and does
not imply a constant-linear relation among three generators. There is also
a counting correction: a conormal span of rank one for three classes has
nullity **two**, not one.

Accordingly, “codimension two” in the atlas is only shorthand for the
global maximum-dimension signature \(13-11=2\). It is not a claim that
\((g_1,g_2,g_3)\subset R_p\) has Krull height two. In each
saturation-tested fiber, the 12-dimensional \(q\)-open stratum carries
the maximal survivors, and the localized residual ideal has a
one-equation, dimension-11 cut.

## 3. What the rank-two factorization proves

The six reduced D23 compatibility rows have the exact affine form

\[
 \mathrm{NF}=At+b,\qquad
 A=C\operatorname{diag}(uW_1^2,uW_2^2,uW_1^2,uW_2^2),             \tag{K.6}
\]

where

\[
 C=[c_1\mid c_2\mid-c_1\mid-c_2],\qquad \operatorname{rank}C=2. \tag{K.7}
\]

Because the \(uW_i\) are chart units, \(\operatorname{rank}A=2\)
everywhere. Hence \(\dim\operatorname{leftker}C=4\). One of those four
compatibility combinations is the zero polynomial because the six normal
forms themselves have rank five. The other three directions span exactly
\(\langle g_1,g_2,g_3\rangle\):

\[
 6\text{ normal forms}
 \longrightarrow4\text{ left-kernel conditions}
 \longrightarrow3\text{ independent residual rows}.             \tag{K.8}
\]

The normalized dependencies among the six normal forms are

\[
\begin{array}{c|c}
p&\text{kernel vector}\\ \hline
105337 &[1,58526,64401,35257,74853,58238]\\
105673 &[1,93937,29382,35369,63348,105378]\\
200257 &[1,44507,189160,66897,97147,85205].
\end{array}                                                       \tag{K.9}
\]

This exact dependency proves “four becomes three.” By itself it cannot
explain why adjoining the three independent rows lowers the maximum
dimension by only two rather than three. In the ambient localized
polynomial ring, their private variables \(x_{53},x_{58},x_{70}\) make them a
coordinate-elimination regular sequence of codimension three. The anomalous
dimension behavior occurs only after quotienting by \(I_{21}\).

## 4. The grading is transport, not redundancy

Work in the displayed radical coefficient algebra

\[
\mathcal B=
\frac{\mathbf Q[r,A_1,A_2,h_1,h_2]}
 {(r^2-3,\ A_1^3-3-r,\ A_2^3-3+r,\ 2h_1^2-3,\ 2h_2^2-3)}
[1/(A_1A_2)].
\]

Thus

\[
 r^2=3,\quad A_1^3=3+r,\quad A_2^3=3-r,\quad
 h_i=HW_i/W_i,\quad \Delta=x_{57}-x_{65}.
\]

Exact monomial-dictionary replay of all 72 atlas triples gives

\[
\begin{aligned}
g_1={}&\Delta^2uW_1^2
-2(r+2)h_1\frac{A_1}{A_2}x_{53}uW_1
+\left(\frac92+3r\right)A_1^2x_{72},\\
g_2={}&\Delta^2uW_2^2
-2h_2x_{58}uW_2
+\left(\frac92-3r\right)A_2^2x_{72},\\
g_3={}&x_{70}+(r-2)\frac{A_2}{A_1}x_{72}.                       \tag{K.10}
\end{aligned}
\]

This matches all 864 atlas coefficients and all 12 terms of the
\(p=200257\) `a00pp` rows. It identifies the displayed radical-algebra
coefficient template, but is not by itself a characteristic-zero ideal
identity.

Let \(\omega\) be the atlas's chosen primitive cube root. For fiber label
`aijuv`, replace \(A_1,A_2\) by \(A_1\omega^i,A_2\omega^j\) and choose
the two signs in \(h_1,h_2\). Then

\[
\begin{array}{c|c|c}
\text{row}&\text{label dependence}&\text{number of classes}\\ \hline
g_1&(i,j,s_1)&18\\
g_2&(j,s_2)&6\\
g_3&(j-i)\bmod3&3.
\end{array}                                                       \tag{K.11}
\]

The joint triple has 36 classes. Formula (K.10) therefore explains the
observed grading completely as finite-group character covariance. Since
the rows are independent inside every fixed fiber, covariance alone cannot
cause the maximum-dimension defect.

## 5. Exact quotient torsion

### 5.1 One explicit annihilator

For the three `a00pp` prime specializations define

\[
 q_p=x_{70}(x_{65}-x_{57})
     +a_p(x_{54}-x_{63})+b_p(x_{59}-x_{66}).                     \tag{K.12}
\]

Exact normal-form reduction against the 397-element D21 bases gives

\[
\begin{array}{c|r|r|r|r}
p&a_p&b_p&\lambda_p&\mu_p\\ \hline
105337&102224&100248&29311&42896\\
105673&43198&44573&101767&105528\\
200257&102168&95503&12194&48153.
\end{array}                                                       \tag{K.13}
\]

For every row,

\[
\operatorname{NF}_{G_{21}}\!\left(q_p(g_2-\lambda_p g_1)\right)=0,
\qquad
\operatorname{NF}_{G_{21}}\!\left(q_p(g_3-\mu_p g_1)\right)=0.   \tag{K.14}
\]

This is equality in \(R_p\), not a sampled-point or radical assertion.

The computation came from the exact map

\[
 \Phi:(R_p)_{\le2}^{\oplus3}\longrightarrow R_p,\qquad
 (a,b,c)\longmapsto\operatorname{NF}_{G_{21}}(ag_1+bg_2+cg_3).
\]

There are 227 quotient-standard coefficient monomials of degree at most
two, with profile \(1+20+206\). Thus this is the degree-at-most-two
truncated syzygy kernel, not a claim about the unbounded module. The matrix
of \(\Phi\) has 681 columns, rank 673, and nullity eight. Its kernel
factors as four common
multipliers \(q_0,q_1,q_2,q_3\) times the two triples
\((-\lambda,1,0)\) and \((-\mu,0,1)\). Each \(q_j\),
\(g_2-\lambda g_1\), and \(g_3-\mu g_1\) has nonzero canonical normal
form. These are genuine quotient-torsion relations. The \(q_p\) in
(K.12) is \(q_0\) and alone proves the mechanism.

### 5.2 All 36 fibers at both atlas primes

The 36 D21 fibers were folded from the common source and their
397-element bases recomputed independently at each of \(p=105337,105673\).
Every one of the 72 maps \(\Phi\) has the same rank-673/nullity-eight
factorization:

- four common multipliers \(q_j\), giving both relations (K.1);
- stable multiplier supports and normalizations;
- multiplier coefficients independent of both sign labels;
- \(\lambda,\mu\) independent of signs and transported by cube-root
  characters.

Writing \(\delta=j-i\bmod3\), the exact scalar tables are

\[
\begin{array}{c|ccc|ccc}
 &\multicolumn{3}{c|}{\lambda(\delta)}
 &\multicolumn{3}{c}{\mu(j)}\\
p&0&1&2&0&1&2\\ \hline
105337&29311&71192&4834&42896&71022&96756\\
105673&101767&81036&28543&105528&98427&7391.
\end{array}                                                       \tag{K.15}
\]

With the atlas primitive cube root \(\omega\),

\[
 \lambda_{ij}=\lambda_{00}\omega^{\,i-j},
 \qquad \mu_{ij}=\mu_{00}\omega^{\,j}.                           \tag{K.16}
\]

The grading transports an existing syzygy; it is not why the syzygy
exists. The numerical scalars differ between primes: “cross-prime
identical” means the syzygy support, nullity, character law, and dimension
signature, not one integer coefficient vector. At \(p=200257\), only
`a00pp` was tested because there is no
36-fiber atlas at that prime.

### 5.3 The conormal rank-one mechanism

Let \(P\in V(J_{23})\cap D(q)\). Differentiate (K.1) at \(P\). Since
\(g_1(P)=g_2(P)=g_3(P)=0\), the terms involving \(dq\) vanish. Since
\(q(P)\ne0\), put

\[
\mathcal C_P=
\frac{\Omega_{S_p/\mathbf F_p}\otimes_{S_p}\kappa(P)}
{\operatorname{span}_{\kappa(P)}
 \{df(P):f\in I_{21}\}}.
\]

Then

\[
 [dg_2]_P=\lambda[dg_1]_P,\qquad
 [dg_3]_P=\mu[dg_1]_P
 \quad\text{in }\mathcal C_P.                                   \tag{K.17}
\]

All twelve banked D23 witnesses lie in \(D(q)\). Their \(q\)-values are

\[
\begin{array}{c|l}
105337&102541,6465,79283,58450,56564,83508\\
105673&32822,64325,11126,41201,85849,979.
\end{array}                                                       \tag{K.18}
\]

Thus (K.17) proves the measured conormal rank and ratios at those
witnesses. It also proves conormal rank at most one at every point of the
family-wide \(q\ne0\) D23 loci. The measured fact that each individual
\(dg_i\) is nonzero in the conormal quotient makes the rank exactly one at
the twelve witnesses.

## 6. Saturation proves component selection

Use a Rabinowitsch variable \(z\) and the equation \(zq-1\) to compute the
\(q\)-open closure. At `a00pp` for all three primes, exact Gröbner bases
have element-for-element identical leading-term supports and give

\[
\begin{array}{c|c|c|c}
\text{ideal or localization}&\dim&\#G&\text{LT hash}\\ \hline
I_{21}&13&397&\text{banked}\\
I_{21}+(q)&13&14&\mathtt{e50a85c583a44133}\\
I_{21}:q^\infty&12&676&\mathtt{07480ceeed3f95d4}\\
(I_{21}+(g_1)):q^\infty&11&581&\mathtt{b2f63c3e065506bf}\\
J_{23}&11&509&\text{banked}\\
J_{23}+(q)&10&144&\mathtt{a14bcb6f3bad67ae}.
\end{array}                                                       \tag{K.19}
\]

The combination
\(\dim(I_{21}+(q))=13\) and \(\dim(I_{21}:q^\infty)=12\) shows that
every 13-dimensional D21 component lies in \(q=0\): \(q\) is a
zero-divisor, not a generic equation. Define safely

\[
 K:=V(I_{21}:q^\infty)
   =\overline{V(I_{21})\cap D(q)},\qquad \dim K=12.               \tag{K.20}
\]

No irreducibility or reducedness is used. From (K.1),

\[
 (J_{23})_q=(I_{21}+(g_1))_q,\qquad
 J_{23}:q^\infty=(I_{21}+(g_1)):q^\infty.                       \tag{K.21}
\]

Thus the residual ideal is principal on \(K\cap D(q)\), and the closure of
that localized one-equation locus has dimension 11. This does not assert
that \(g_1\) is Cartier or a nonzerodivisor along the \(q=0\) boundary of
\(K\). Since \(J_{23}+(q)\) has dimension 10, every maximal
11-dimensional D23 component meets \(D(q)\). This proves (K.3).

At \(p=105337\), all 36 fibers have the same saturation dimensions, basis
sizes, and leading-term hashes as `a00pp`; all 36 \(J_{23}+(q)\) ideals
also have dimension 10. Hence the full K mechanism is proved on the
complete first-prime atlas.

> **CONJECTURE K-FAMILY-SAT.** The same three saturation gates hold in the
> 35 non-`a00pp` fibers at \(p=105673\). The syzygies and uniform
> \(13\to11\) dimensions are exact in those fibers, but their saturations
> were not run. No unproved coordinate transport is substituted for them.

There is independent component evidence. Several D21 rows have a common
factor \(QL\), where

\[
 L=-3x_{47}+2x_{57}+x_{65}.
\]

At \(p=105337\),

\[
\dim(I_{21}+(L))=\dim(I_{21}+(Q))=13,\qquad
\dim(I_{21}+(L,Q))=12,
\]

so this coarse split is not itself \(K\). Let
\(H=\operatorname{equidimMax}(I_{21}+(L))\). Then

\[
\dim(H+(g_i))=12,\quad
\dim(H+(g_i,g_j))=11,\quad
\dim(H+(g_1,g_2,g_3))=10,                                      \tag{K.22}
\]

whereas

\[
\dim(I_{21}+(L,g_1,g_2,g_3))=11.                               \tag{K.23}
\]

Therefore the dimension-11 part on this coarse \(L\)-branch comes from
its lower-dimensional component structure, not its 13-dimensional hull.
In each saturation-tested fiber, the separate \(q\)-saturation argument
above controls all global 11-dimensional D23 components. Moreover,
\(H\) imposes
\(x_{57}=x_{65}\), \(x_{54}=x_{63}\), and \(x_{59}=x_{66}\), so \(q_0\)
vanishes identically on it. The twelve witnesses occupy both coarse
\(Q\)- and \(L\)-branches while all have \(q\ne0\); neither branch label
alone is the source.

## 7. Structural source

The three alternatives can now be separated sharply.

**Rank-two factorization.** Equations (K.6)--(K.9) prove its direct role:
it constructs three obstruction rows from six compatibility rows. By
itself it supplies no \(q\), sees no associated component of \(I_{21}\),
and does not imply (K.19). It could still participate in a future
universal derivation together with the D21 identities.

**Mod-3 grading.** Equations (K.10)--(K.16) prove diagonal character
transport of the residual and syzygy coefficients. Torsion is a
fixed-fiber quotient identity and persists at three primes, so grading
alone is not sufficient to produce it. The grading may still be part of a
future universal formulation.

**Depth-ladder/Keller source.** The exact proof currently stops at
“torsion in \(S/I_{21}\).” The \(w\)-invariant proved in
`SHEET6-DEPTH.md` controls decorated-tree arithmetic and explicitly
leaves the coefficient layer and \(M\ge2\) suffixes out of scope.
Keller/de Rham exactness supplies the no-log level-42 pins already inside
\(I_{21}\), but the repository has no pristine-row derivation of
(K.12)--(K.14). The variables occurring across the four \(q_j\) span the
level-34/36/38/40 ladder, which is suggestive but not a proof.

> **CONJECTURE K-SOURCE.** The \(q_j\) and the two torsion syzygies lift to
> a coefficient-algebra identity in the universal depth-ladder system,
> ultimately forced by Keller exactness. Promotion requires symbolic
> \(q_j,\lambda,\mu\) over the coefficient algebra and direct reduction
> against unspecialized \(I_{21}\). Three modular supports do not suffice.

## 8. D25 and every deeper level

### 8.1 What is actually banked

There is no completed D25 algebra in the repository.
`cases/d25_reduce.py` is a recovery/checkpoint reducer requiring external
jet and 36-basis payloads that are absent. No reduced Row-24 residual,
mask, D25 system, Gröbner basis, dimension, witness, or verdict is banked.

The exact symbolic statement in `sol-round6.md` is only that the nine
Row-24 rows have a rank-four ten-variable first-occurrence symbol, hence
five existential compatibility residuals before normal-form reduction.
Those five residuals have not been tested for an analogue of (K.1), and
the dormant/reactivated lift variables must be eliminated before a base
dimension is inferred.

Therefore no unconditional D25 dimension follows.
**CONJECTURE / FORECAST:** the earlier conditional range remains 9--10;
it is not a proved bound.

### 8.2 Two distinct conditional recurrences

The D23 proof separates two effects that were previously conflated. Under
a transversality hypothesis, principalization contributes one drop in
maximum dimension; selecting a lower-dimensional \(q\)-open stratum
contributes another. At later depths either one or both may recur.

> **CONJECTURE K-DEPTH-P.** After the correct projected elimination at
> every odd-depth step, all new residuals become one transverse principal
> generator on a \(q_D\)-open stratum of the **same** maximal dimension
> as the incoming survivor, and the residual locus in \(q_D=0\) has no
> component larger than this open principal cut.

Under K-DEPTH-P, each \(D\mapsto D+2\) step after D23 drops dimension by
one:

\[
\boxed{\dim D_{23+2r}=11-r\quad(0\le r\le11)}.                  \tag{K.24}
\]

Thus

\[
\begin{array}{c|rrrrrrrrrrrr}
D&23&25&27&29&31&33&35&37&39&41&43&45\\ \hline
\dim&11&10&9&8&7&6&5&4&3&2&1&0.
\end{array}
\]

The same transverse rule predicts emptiness at D47.

> **CONJECTURE K-DEPTH-S.** Alternatively, every step repeats the full D23
> component-selection event: all incoming top components lie in
> \(q_D=0\), the \(q_D\)-open closure has dimension one less, all new
> residuals become one transverse principal generator there, and the
> residual locus in \(q_D=0\) is smaller than the open principal cut.

Under this stronger recurrence, every step drops two:

\[
\boxed{\dim D_{23+2r}=11-2r\quad(0\le r\le5)},                  \tag{K.25}
\]

so D25, D27, D29, D31, D33 have predicted dimensions
\(9,7,5,3,1\), and D35 is predicted empty under K-DEPTH-S.

The present D23 proof does not choose between (K.24) and (K.25). Hence the
explicit D25 prediction is **10 under repeated principalization only, 9
under repetition of the full selection-plus-principal-cut mechanism**. A
mixed component mask, a non-transverse generator, or failure of the
annihilator identity can give a different pattern.

The decisive D25 test is now precise: after projected elimination, compute
the low-degree syzygy module of the five residuals and test whether common
annihilators factor it into scalar-normalized differences
\(r_\nu-\lambda_\nu r_1\). Then compute
\(I_{23}:q_{24}^{\infty}\), the localized residual ideal, and the
\(q_{24}=0\) residual stratum. Residual-row counts and witness Jacobians
alone cannot decide either recurrence.

## 9. Promotion boundary

Proved:

- no constant-linear dependency among \(g_1,g_2,g_3\);
- the \(18/6/3\) coefficient classes and their character-template source;
- two exact \(q\)-torsion syzygies in all fibers at both atlas primes;
- the exact implication from those syzygies to conormal rank one on
  \(D(q)\);
- the complete \(13\rightsquigarrow12\to11\) saturation mechanism in all
  36 \(p=105337\) fibers and at `a00pp` for three primes.

Still **CONJECTURE**:

- the saturation gates in the 35 remaining \(p=105673\) fibers;
- a characteristic-zero coefficient-algebra lift and good-reduction
  theorem;
- radicality, irreducibility, or uniqueness of \(K\);
- derivation from the \(w\)-invariant or Keller exactness;
- either D25/all-depth recurrence.

The accurate replacement for the old wording is:

> In each saturation-tested fiber, the D23 residuals are three independent
> normal-form rows. Their ideal lowers the maximum dimension from 13 to 11
> because the D21 quotient is non-equidimensional: two quotient-ring
> torsion syzygies principalize the residual ideal after localization on a
> 12-dimensional \(q\)-open stratum, and the closure of its one-equation
> locus has dimension 11. The character grading transports this mechanism
> across the finite fibers; grading alone is insufficient to produce it.
