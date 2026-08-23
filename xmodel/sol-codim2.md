# ECO-2: the equivariant carrier--obstruction mechanism

**Round 2 research note; pre-registered before a D25 dimension result.**  The
scope throughout is the residue-A, fixed-`r`, B-frozen, no-log, `PIN42`,
`W1*W2 != 0` chart over the split primes
`p=105337` and `p=105673`.  Nothing here promotes a
characteristic-zero point, a formal germ, or a Keller pair.

**Pre-registration lock: 2026-08-21T03:04:29Z.**  At the lock time there was
no completed D25 Groebner basis or dimension in the repository.  The banked
per-fiber table at `p=105337` contained four one-hour timeouts, 32
cancellations, zero EMPTY/NONEMPTY verdicts, and no dimensions.  The two
union lanes and the long `a00pp` lane had not returned a verdict.  All
D25 facts used below were extracted from the already-emitted input equations,
not from lane output.

The answer to the prediction question is:

\[
\boxed{
\begin{array}{c}
\text{D25 projected-base codimension}=2,\\
\text{D25 full residual codimension}=4,\\
\text{every full lane dimension}=13.
\end{array}}
\tag{0.1}
\]

The distinction between the first two lines is essential.  The D23 base has
dimension 11, but the D25 solver ring has six live lift variables and hence
dimension 17 before the five new residual rows.  Two effective equations
solve lift variables and two are projected compatibility equations.  The
prediction is therefore

\[
  11\longrightarrow 9\quad\text{in the 22-variable base projection},
  \qquad
  17\longrightarrow 13\quad\text{in the full 28-variable lane}.
\tag{0.2}
\]

The algebraic reduction to two projected equations is exact.  Their
dimension-nine, top-component-survival effect is **CONJECTURE ECO-D25**.
Thus the number 13 is a falsifiable prediction, not a dimension inferred
from an equation count.

---

## 1. What the correction changes

Let

\[
 R_{21,\ell}=S_p/I_{21,\ell},\qquad
 J_{23,\ell}=I_{21,\ell}+(g_{1,\ell},g_{2,\ell},g_{3,\ell}),
\]

where \(\ell\) is one of the 36 radical-fiber labels.  The exact uniform
D23 signature on all 72 fibers is

\[
(\dim\langle g\rangle,\operatorname{rank}w,
  \operatorname{rank}\mathrm{NF},\dim\ker\mathrm{NF},
  \operatorname{rank}C,\dim V(I_{21}),\dim V(J_{23}))
=(3,3,5,1,2,13,11).
\tag{1.1}
\]

In particular, the three displayed classes \(g_1,g_2,g_3\) are
constant-linearly independent.  Their private standard monomials are

\[
x_{57}^{2}uW_1^2,\qquad x_{57}^{2}uW_2^2,\qquad x_{70},
\]

each with coefficient one.  This is the correction in
`SHEET6-DIRECTIONB.md` section `8.S6-CORRECTION` and the confirmed
Target A conclusion of `xmodel/grok-k-g5-review.md`.

The rank-five fact belongs to a different object: the six preliminary
compatibility normal forms.  Their lift matrix has rank two; its
four-dimensional left kernel contains one direction whose inhomogeneous
part is identically zero, leaving the three independent rows \(g_i\).
Consequently,

\[
6\text{ preliminary rows}\longrightarrow4\text{ compatibility directions}
\longrightarrow3\text{ independent }g\text{-rows}.
\tag{1.2}
\]

This proves only "four becomes three."  It does not explain the maximum
dimension drop \(13\to11\).  Nor can equivariance manufacture an internal
dependency: the group acts freely on the fiber labels, so a fixed fiber has
no nontrivial stabilizer from which such a relation could follow.

The corrected explanation has two geometric stages:

1. a lower-dimensional, equivariantly transported \(q\)-open carrier
   supplies the maximal D23 survivors; and
2. the three independent residuals become one equation after localization
   on that carrier.

Thus the two drops are **component selection** \(13\rightsquigarrow12\)
and **localized principalization** \(12\to11\), not two independent
constant-linear conditions among the \(g_i\).

---

## 2. The promoted equivariance theorem is load-bearing

The promoted theorem in `xmodel/sol-pcc-orbits.md`, confirmed by
`xmodel/grok-orbits-review.md`, gives

\[
G=(C_3)^2\times(C_2)^2
\]

acting freely and transitively on the 36 labels at each fixed split prime.
For \(g=(a,b,e_1,e_2)\), the diagonal coordinate map

\[
T_g:X_\ell\longrightarrow X_{g\ell}
\]

satisfies the exact row identity

\[
F_{r,g\ell}(T_gx)=
\omega^{a d_{1r}+b d_{2r}}F_{r,\ell}(x),
\tag{2.1}
\]

with the recorded sign scalings on coordinates.  It follows that the fiber
schemes are isomorphic.  Normal forms, Jacobian ranks, Schur complements,
unit pivots, and saturations commute with transport; in particular,

\[
S_g(I:q^\infty)=S_g(I):(S_gq)^\infty.
\tag{2.2}
\]

This has two consequences for a proposed mechanism.

First, one may prove a representative statement and transport it to the
other 35 fibers **within the same prime**, provided every auxiliary object
is transported too.  One may not copy the same printed annihilator into
all fibers.  Second, every isomorphism invariant, including emptiness and
dimension, must be uniform on the 36 components.  The theorem does not
connect the two primes.

### 2.1 Character test for the D23 torsion

The cube characters of the D23 rows are

\[
\chi(g_1)=(2,2),\qquad
\chi(g_2)=(0,1),\qquad
\chi(g_3)=(2,0),
\tag{2.3}
\]

with trivial sign characters.  Hence relations of the form

\[
q(g_2-\lambda g_1)=0,\qquad q(g_3-\mu g_1)=0
\tag{2.4}
\]

are equivariant only if

\[
\chi(\lambda)=(1,2),\qquad \chi(\mu)=(0,1).
\tag{2.5}
\]

This is exactly the measured law.  With label `aij**` and signs
suppressed,

\[
\lambda_{ij}=\lambda_{00}\omega^{i-j},
\qquad
\mu_{ij}=\mu_{00}\omega^j.
\tag{2.6}
\]

Normalize the representative annihilator as

\[
q_{00}=x_{70}(x_{65}-x_{57})
       +A_{00}(x_{54}-x_{63})+B_{00}(x_{59}-x_{66}).
\tag{2.7}
\]

The only compatible transported normalized family is

\[
A_{ij}=A_{00}\omega^j,\qquad
B_{ij}=B_{00}\omega^{2i+2j},
\tag{2.8}
\]

independent of the two sign labels.  Then

\[
q_{g\ell}(T_gx)=\omega^{2a+b}q_\ell(x),
\tag{2.9}
\]

so \(q\) has character \((2,1)\).  Equations (2.3)--(2.9) make both
torsion identities character-homogeneous.  This repairs the equivariance
gap in the old proposal: the correct object is the orbit
\(\{q_\ell\}\), not one fixed numerical polynomial on 36 fibers.

The representative constants are

\[
\begin{array}{c|rrrr}
p&A_{00}&B_{00}&\lambda_{00}&\mu_{00}\\ \hline
105337&102224&100248&29311&42896\\
105673&43198&44573&101767&105528\\
\end{array}
\tag{2.10}
\]

---

## 3. D23: exact modular carrier and principalization

The review correctly objected that the normal-form identities and the
saturation table in the previous note were not backed by repository
artifacts.  This round replayed the claims directly from the shipped
inputs rather than inheriting those assertions.

### 3.1 Exact quotient torsion, replayed at both representatives

Using the first 397 rows of
`cases/directionb_det23_p105337.ms` and
`cases/directionb_det23_p105673.ms` as the monic \(G_{21}\) bases,
exact reduction gives, at `a00pp`,

\[
\operatorname{NF}_{G_{21}}
 \bigl(q(g_2-\lambda g_1)\bigr)=0,
\qquad
\operatorname{NF}_{G_{21}}
 \bigl(q(g_3-\mu g_1)\bigr)=0
\tag{3.1}
\]

at both primes, with (2.10).  The degree-at-most-two quotient-syzygy map
was also independently rebuilt:

\[
227\text{ standard coefficient monomials},\quad
681\text{ columns},\quad
\operatorname{rank}=673,\quad
\operatorname{nullity}=8
\tag{3.2}
\]

at both primes.  Thus (3.1) is an exact identity in \(R_{21,00}\), not a
witness interpolation or a conormal-only statement.

Now define \(q_{g\ell}\) by (2.8), equivalently by normalized transport.
Normal forms commute with \(T_g\), so (3.1) transports to all 36 fibers at
each prime.  This is an exact modular family theorem; no 72-fold
recomputation is needed.

### 3.2 The saturation dimensions, replayed without the old hashes

Fresh Rabinowitsch saturations and boundary Groebner computations from the
banked bases give the following at `a00pp` for **both** primes:

\[
\begin{array}{c|c|c}
\text{ring/ideal}&\dim&\text{fresh standard-basis size}\\ \hline
I_{21}&13&397\\
I_{21}+(q)&13&14\\
I_{21}:q^\infty&12&500\\
J_{23}&11&509\\
J_{23}+(q)&10&144.
\end{array}
\tag{3.3}
\]

The saturation replay used Singular 4.4.1p5 in the banked 22-variable
degree order and the command \( \operatorname{std}(\operatorname{sat}
(I,(q))[1]) \); all reported lanes finished with return code zero.  The
second-prime dimension of \(J_{23}:q^\infty\) follows algebraically below
from the directly computed dimensions of \(J_{23}\) and
\(J_{23}+(q)\), rather than from a redundant second saturation run.

The invariant used below is the dimension.  The old unbanked saturation
counts 676 and 581 were not reproduced and are not reused.  The fresh
standard-basis computation has 500 elements for \(I_{21}:q^\infty\); a
direct first-prime computation has 509 for \(J_{23}:q^\infty\).
Standard-basis element counts are not the proof invariant here; the
dimensions and localized-ideal equality are.

Set

\[
K_\ell=V(I_{21,\ell}:q_\ell^\infty)
      =\overline{V(I_{21,\ell})\cap D(q_\ell)}.
\tag{3.4}
\]

Equations (3.3) imply:

- \(\dim K_\ell=12\);
- every 13-dimensional component of \(V(I_{21,\ell})\) is contained in
  \(q_\ell=0\), because the entire \(q\)-open closure has dimension 12;
- \(q\) is a zero-divisor/component selector, not a generic hypersurface
  equation.

On \(D(q_\ell)\), (3.1) permits cancellation of \(q_\ell\), giving

\[
(J_{23,\ell})_{q_\ell}
=(I_{21,\ell}+(g_{1,\ell}))_{q_\ell}.
\tag{3.5}
\]

Because \(\dim V(J_{23})=11\) while
\(\dim V(J_{23}+(q))=10\), no maximal 11-dimensional D23 component is
contained in \(q=0\).  Hence saturation retains every maximal D23
component and

\[
\dim V(J_{23}:q^\infty)=11.
\tag{3.6}
\]

Local equality (3.5) gives equality after contraction,

\[
J_{23}:q^\infty=(I_{21}+(g_1)):q^\infty,
\tag{3.7}
\]

so the localized residual ideal is principal on the 12-dimensional
carrier and its closure has dimension 11.  Finally,
\(\dim V(J_{23}+(q))=10\) says that every maximal D23 survivor meets this
open carrier; a different 11-dimensional boundary component is not hiding
in \(q=0\).

The promoted saturation identity (2.2) transports (3.3)--(3.7) from
`a00pp` to all 35 other fibers at the same prime.  Therefore the
following is now stronger than the old Conjecture-K claim.

> **EXACT MODULAR THEOREM (ECO-2 at D23).**  In all 72 current atlas
> fibers, the three residual rows are constant-linearly independent, but
> on the equivariant 12-dimensional \(q\)-open carrier their localized
> ideal is generated by one of them.  All maximum-dimensional
> (11-dimensional) D23 survivor components arise from this open carrier.
> Thus the observed maximum
> dimension change factors as
> \[
> 13\rightsquigarrow12\longrightarrow11.
> \]

No irreducibility, reducedness, or uniqueness of \(K_\ell\) is asserted.
The theorem is modular, chart-local, and about the currently emitted
ideals.

### 3.3 Conormal check

At each of the twelve banked D23 witnesses, direct replay of the parked
first 29 rows gives

\[
\operatorname{rank}J(I_{21})=10,\qquad
\operatorname{rank}J(I_{21}+g_i)=11
\]

for every individual \(g_i\), every pair, and the triple.  Thus the three
conormal classes span exactly one dimension there.  All twelve values
\(q(P)\) are nonzero.  Differentiating (3.1) at such a point gives

\[
[dg_2]=\lambda[dg_1],\qquad [dg_3]=\mu[dg_1],
\tag{3.8}
\]

which explains both the rank and the measured ratios.  This is local
corroboration of (3.5), not a substitute for the saturation argument.

### 3.4 What remains conjectural at D23

> **CONJECTURE ECO-SOURCE.**  The transported modular family
> \((q_\ell,\lambda_\ell,\mu_\ell)\), its torsion identities, and the
> carrier/principalization construction descend from one
> character-homogeneous identity over the pristine characteristic-zero
> coefficient algebra and have the asserted good reductions.

The two-prime computations do not prove this source statement.  They also
do not identify a prime or reduced component, and they do not imply an
all-depth recurrence.  Those gaps stay open.

---

## 4. D25: an exact pre-outcome reduction

The present D25 emission makes a much sharper prediction possible than the
older 9--10 forecast.  For each label, write

\[
B_\ell=S_p/J_{23,\ell},\qquad \dim B_\ell=11,
\]

and let

\[
T_\ell=B_\ell[t_1,\ldots,t_6]
\]

for the six live lift aliases

\[
(x_{33},x_{38},x_{16},x_{19},x_{24},x_{27}).
\tag{4.1}
\]

Thus \(\dim T_\ell=17\).  The five emitted D25 residuals are affine in
these variables:

\[
R=A_\ell(z)t+b_\ell(z),
\qquad A_\ell\in\operatorname{Mat}_{5\times6}(B_\ell).
\tag{4.2}
\]

Everything in this section was checked coefficientwise in both selector
union files and all 72 parked fiber files before a solver outcome existed.

### 4.1 One exact D25 row identity

The same integer coefficient vector gives an exact identity in both current
modular emissions:

\[
\boxed{R_2+6R_3+30R_4+144R_5=0.}
\tag{4.3}
\]

The full five-row polynomial coefficient matrix has rank four at both
primes, with (4.3) its unique constant relation; \(R_1\) is independent.
Since 144 is a unit at both primes,

\[
(R_1,\ldots,R_5)=(R_1,R_2,R_3,R_4).
\tag{4.4}
\]

This is a genuine constant dependency at D25.  It must not be confused
with the refuted constant dependency among the D23 \(g_i\).

All five \(R_\nu\) have trivial \(G\)-character, so (4.3) is invariant
under the promoted action.  Pulling its coefficient vector back through
the recorded \(L_{24}\) Schur matrix gives

\[
(0,1,6,30,144,684,3240,15336,72576),
\tag{4.5}
\]

whose nonzero tail satisfies

\[
a_n=6a_{n-1}-6a_{n-2}.
\tag{4.6}
\]

Writing \(r^2=3\) and indexing this tail by \(a_0=1\), it also has the
exact closed form

\[
a_n=\frac{(3+r)^{n+1}-(3-r)^{n+1}}{2r}.
\]

The characteristic roots are \(3+r=A_1^3\) and \(3-r=A_2^3\).  Cube
rotations therefore fix them, which explains why the observed recurrence
is compatible with the trivial D25 row character.

> **CONJECTURE ECO-BIANCHI.**  Equations (4.3)--(4.6) are the reductions
> of a pristine, characteristic-zero Row-24 Bianchi/recurrence identity,
> rather than a relation introduced only by quotient compilation.

The emitted modular identity (4.3) is exact; the source interpretation is
the conjecture.

### 4.2 The lift rank is exactly two

The twelve lift-carrier coefficient vectors occurring in \(A_\ell\) span
a two-dimensional space at every fiber and both primes.  Hence every
three-by-three lift minor vanishes.  Conversely, the minor using rows
\((R_1,R_2)\) and columns \((x_{33},x_{38})\) is a nonzero scalar times

\[
uW_1^2uW_2^2.
\tag{4.7}
\]

At `a00pp` the scalar is 75772 modulo 105337 and 9899 modulo
105673.  Since the \(W\)-chart equations make both \(uW_i\) units, the
minor is a unit.  Therefore

\[
\operatorname{rank}A_\ell=2
\tag{4.8}
\]

everywhere on the chart.  Equivariance transports the representative
unit minor and rank, while the direct 72-file audit independently checks
the same fact.

The constant left kernel of \(A_\ell\) has dimension three.  One direction
is the vector \((0,1,6,30,144)\) and annihilates both \(A_\ell t\) and
\(b_\ell\) by (4.3).  Choose two complementary directions and call their
nonzero base-only compatibility normal forms \(h_{1,\ell},h_{2,\ell}\).
Constant row operations followed by the unit pivot (4.7) put the five
equations into the form

\[
\begin{array}{rcl}
t'_1-f_1(z,t'_3,t'_4,t'_5,t'_6)&=&0,\\
t'_2-f_2(z,t'_3,t'_4,t'_5,t'_6)&=&0,\\
h_{1,\ell}(z)&=&0,\\
h_{2,\ell}(z)&=&0,\\
0&=&0.
\end{array}
\tag{4.9}
\]

Consequently there is an exact chart-algebra isomorphism

\[
\boxed{
T_\ell/(R_1,\ldots,R_5)
\simeq
\bigl(B_\ell/(h_{1,\ell},h_{2,\ell})\bigr)
[u_1,u_2,u_3,u_4].}
\tag{4.10}
\]

In particular,

\[
\dim V_{25,\ell}
=\dim V(J_{23,\ell}+(h_{1,\ell},h_{2,\ell}))+4.
\tag{4.11}
\]

This is the corrected meaning of a D25 "projected obstruction."  The
five-row system has four effective equations: two lift solves plus two
base compatibilities.  The four surviving lift directions are genuine
affine-space factors, not an informal variable count.

### 4.3 The equivariant effective-obstruction module

Conceptually, (4.2) defines a lift map from a rank-six lift module to a
rank-five row module.  Its cokernel has rank three.  The invariant identity
(4.3) is a unimodular functional on that cokernel which kills the
inhomogeneous section.  After an invertible row change, one compatibility
is zero and the section lies in a rank-two direct summand represented by
\((h_1,h_2)\).  Because Schur operations and unit backsolves commute with
\(G\), these pairs transport as one equivariant rank-two obstruction family.

This is the D25 continuation of ECO-2.  Equivariance forces the pair's
height and quotient dimension to be the same in all 36 fibers of a fixed
prime.  It does **not** force height two: the action is free, and there is
no symmetry stabilizer inside a fiber.  Height two is the transversality
statement to be tested by the running computation.

> **CONJECTURE ECO-D25 (pre-registered).**  At each of the two current
> split primes, \((h_{1,\ell},h_{2,\ell})\) is proper and has the full
> projected maximum-dimension effect on the D23 survivor scheme:
> \[
> \dim B_\ell/(h_{1,\ell},h_{2,\ell})=9.
> \tag{4.12}
> \]
> The causal clause is additional to the bare dimension equality: at least
> one 11-dimensional D23 component survives a height-two cut, and no other
> surviving component has dimension above 9.

The stronger carrier-continuation form makes two further pre-registered
claims.  Put \(H_\ell=J_{23,\ell}+(h_{1,\ell},h_{2,\ell})\).  Then

\[
\dim V(H_\ell:q_\ell^\infty)=9,
\qquad
\dim V(H_\ell+(q_\ell))\leq8.
\tag{4.13}
\]

> **CONJECTURE ECO-D25-CARRIER.**  Equation (4.13) holds at both primes.
> Thus the maximal projected D25 locus still comes from the equivariant
> D23 carrier, while the \(q=0\) boundary is strictly smaller.

The exact rank-two obstruction makes (4.12) the natural regular value,
but it does not prove it.  The old D23 carrier story alone did not choose
between a one- and two-dimensional projected cut.  By exposing exactly two
nonzero projected compatibility rows, the new D25 emission makes height
two the sharp regular prediction.  This is why a single number can now be
pre-registered.

The twelve old D23 witnesses do not settle (4.12).  At each, the lift
matrix has rank two but the augmented affine matrix has rank three, so
those particular base points do not automatically extend to D25.  This is
consistent with a codimension-two projected sublocus and is not evidence
of emptiness.

---

## 5. Exact D25 lane predictions

Combining (4.10) with CONJECTURE ECO-D25 gives

\[
\dim V_{25,\ell}=9+4=13.
\tag{5.1}
\]

Equivalently, the residual system has:

\[
\begin{array}{c|c}
\text{quantity}&\text{pre-registered value}\\ \hline
\text{D23 base dimension}&11\\
\text{projected compatibility codimension}&2\\
\text{projected D25 dimension}&9\\
\text{free lift-fiber dimension}&4\\
\text{pre-residual full dimension}&17\\
\text{incremental full residual codimension}&4\\
\text{full D25 lane dimension}&13.
\end{array}
\tag{5.2}
\]

The exact lane-level pre-registration is:

| lane/object | verdict | global dimension | componentwise dimensions |
|---|---:|---:|---:|
| `d25fam_p105337` selector union | NONEMPTY | 13 | \((13)^{36}\) |
| `d25fam_p105673` selector union | NONEMPTY | 13 | \((13)^{36}\) |
| `p105337` PF1 `a00pp` | NONEMPTY | 13 | 13 |
| any parked fiber at either prime | NONEMPTY | 13 | 13 |

Here \((13)^{36}\) means a 36-entry vector all of whose entries are 13;
the component mask is `1` repeated 36 times.  The four selector
equations define a finite split etale algebra, so the 32-variable union is
a finite disjoint union and the selectors add no dimension.  Hence its
global dimension is the maximum component dimension, also 13.

For bookkeeping only, the final affine codimension is

\[
28-13=15\quad\text{per parked fiber},
\qquad
32-13=19\quad\text{for a selector union}.
\tag{5.3}
\]

These are total presentation codimensions, not the incremental D25
residual codimension.  The latter is four.  Calling it "codimension two"
without the word **projected** would now be wrong.

The PF1 presentation has 509 Groebner-basis rows for \(J_{23}\) (called
\(I_{23}\) by the D25 assembly) plus the same five residuals, rather than
the sparse 29-plus-five presentation;
they generate the same ideal and must have the same dimension.  There is a
plumbing trap: `cases/d25pf1_run.sh` writes
`out/d25pf1_a00pp.out` and a `D25PF1` marker, while
`cases/d25pf_verdict.py` recognizes only the older `D25PF` marker and
`d25pf_p<P>_<label>.out` names.  The PF1 result must therefore be
parsed explicitly before declaring that it is absent.

The older numbers 9--10 in `xmodel/sol-round5.md` and
`xmodel/sol-conjecture-k.md` were conditional **projected-base**
forecasts made before the six surviving D25 lift variables were known.
They are not 28-variable solver dimensions.  In the current emission,
projected dimension 9 means lane dimension 13; projected dimension 10
would mean lane dimension 14.

---

## 6. What will refute ECO-D25

The following table is locked with the prediction, not fitted after the
lanes return.

| observed faithful D25 result | exact interpretation via (4.10) | verdict on ECO-D25 |
|---|---|---|
| NONEMPTY, dimension 13 | projected quotient has dimension 9 | numerical prediction passes; mechanism still needs component/source checks |
| NONEMPTY, dimension 14 | projected quotient has dimension 10; only a one-unit maximum drop | **REFUTED** |
| NONEMPTY, dimension 15 | projected quotient has dimension 11; no maximum-dimensional projected cut | **REFUTED** |
| proper NONEMPTY, dimension at most 12 | projected dimension at most 8; top-component loss or extra obstruction | **REFUTED** |
| EMPTY | the compatibility pair kills every component | **REFUTED** |
| dimension above 15 | impossible under the exact two-equation projection (4.10) | emission, ideal-equivalence, or parser failure |

A TIMEOUT, CANCELLED or ERROR marker, a zero-byte output, or failure of the
current parser to recognize the PF1 filename is not a mathematical verdict.
It neither confirms nor refutes the pre-registration.

There are additional structural refutations.

1. **Mixed fibers at one prime.**  Different verdicts or dimensions among
   the 36 labels contradict the promoted equivariance theorem as applied
   to the emitted D25 ideals, or show that the lanes did not solve faithful
   specializations.  A mixed mask is not an allowed ECO-2 outcome.
2. **Union/representative disagreement.**  A union result inconsistent
   with `a00pp` contradicts the finite-product specialization or PF
   ideal-equivalence.  This is a pipeline failure before it is geometric
   evidence.
3. **Cross-prime disagreement.**  Uniform dimension 13 at one prime and a
   different uniform answer at the other does not refute within-prime
   \(G\)-equivariance, but it **does refute the two-prime ECO-D25
   pre-registration** (or identifies one prime as exceptional for the
   conjectural source model).
4. **Wrong projection/fiber split.**  Even if a black-box lane reports
   dimension 13, failure of the elimination quotient to have dimension 9
   and an \(\mathbb A^4\) lift factor contradicts the proposed causal
   mechanism.  Equation (4.10) makes this primarily an emission-fidelity
   check.
5. **Carrier gate failure.**  Total dimension 13 together with
   \(\dim V(H:q^\infty)<9\), or with a dimension-nine component contained
   in \(q=0\), passes the headline number but **refutes
   ECO-D25-CARRIER**.  Primary-component tracking is still needed to show
   that a dimension-nine open component descends from a maximal D23
   component rather than from a pre-existing lower component.
6. **Failure of (4.3) in a faithful pristine rebuild.**  That would refute
   CONJECTURE ECO-BIANCHI.  Failure in one of the current emitted files
   would instead contradict the exact input audit.

Conversely, dimension 13 alone does not prove ECO-SOURCE or a universal
depth recurrence.  A decisive causal confirmation should also compute the
base elimination ideal, verify
`dim B/(h1,h2)=9` componentwise, verify the two carrier gates (4.13),
identify a surviving maximal D23 component, and derive (4.3) from pristine
rows over the source coefficient algebra.

---

## 7. Promotion ledger

### Exact at the current two-prime modular scope

- the D23 signature \((3,3,5,1,2,13,11)\) and absence of a constant
  relation among \(g_1,g_2,g_3\);
- the promoted \(G\)-equivariance and transport of normal forms,
  Jacobians, Schur operations, and saturations;
- the representative torsion identities (3.1) at both primes and their
  equivariant transport to all 72 fibers;
- the representative saturation/boundary dimensions (3.3) at both primes
  and their equivariant transport;
- the D23 carrier/principalization factorization at the modular
  dimension level, without irreducibility or reducedness;
- the D25 emitted-row identity (4.3), full row rank four, lift rank two,
  two nonzero projected compatibility rows, and the quotient isomorphism
  (4.10), in both unions and all 72 parked systems.

### CONJECTURE

- **ECO-SOURCE:** characteristic-zero/pristine origin and good reduction
  of the D23 torsion/carrier package;
- **ECO-BIANCHI:** pristine/source origin of the D25 recurrence and row
  identity;
- **ECO-D25:** a dimension-nine top-component cut by the projected pair,
  hence full lane dimension 13 at both primes;
- **ECO-D25-CARRIER:** the saturated and boundary inequalities (4.13),
  with a maximal D23 component supplying the dimension-nine survivor;
- any iteration of this mechanism at D27 or beyond;
- irreducibility, reducedness, or uniqueness of any carrier or survivor
  component.

The corrected conclusion is therefore narrower and more testable than
Conjecture K.  D23 is explained modularly by an equivariant
component-carrier plus localized principal equation.  D25 has an exact
equivariant rank-two projected obstruction, and the pre-registered test is
whether it cuts with full projected height two.  The running lanes must
say **13 everywhere**; any other faithful dimension refutes that
prediction.
