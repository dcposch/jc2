# G2: same-pair anti-standard source audit

**Date:** 2026-08-27  
**Producer:** Sol Ultra, primary-source and desk-scale theorem audit  
**Target:** the missing same-fixed-pair source on the other infinity chart  
**Primary sources:** VGG, arXiv:1401.1784v3, Definition 4.3,
Propositions 5.17--5.18, Remark 6.8, Proposition 6.9, Proposition 7.3 and
Corollary 7.4; GGV5, arXiv:1708.07936v1, Theorem 2.20

## 0. Verdict

The answer is neither “transpose fixes it” nor “only pure Sigray can touch
the other chart.”  The exact boundary is:

1. **There is no printed opposite-orientation version of GGV5 Theorem
   2.20.**  Reversing the direction order and replacing the defining
   negative sign by a positive sign does not make its proof go through.
   The standard sign is used before the theorem, in the existence and
   classification of regular corners, and again in the type-II.b cut and
   the termination argument.

2. **No constant-Jacobian automorphism of the same Laurent cylinder that
   preserves the physical `y=infinity` end can standardize the live
   opposite corner.**  For the `8_28` support this is a short no-go theorem,
   proved in Section 4.  VGG's `psi_2` is the only other cylinder-automorphism
   class: it swaps `y=infinity` with `y=0`, sends the live source direction
   to the wrong base direction, and asks for valuation ratios at unrelated
   old directions.  It is a useful degree-reduction normalization, not a
   same-physical-chart repair.

3. **Pure Sigray is nevertheless not the only honest route.**  VGG
   Proposition 7.3 and Corollary 7.4 are already a genuine theorem on the
   opposite side of the *same fixed Keller pair*.  After writing that pair
   in local coordinates `(Y,V)=(y,-x)`, they propagate bracket-zero and
   valuation-ratio data through the positive interval and certify perfect
   powers of the `P` leading faces.  In live `8_28`, the source has
   
   \[
     \frac1m\operatorname{st}_{-1,4}(P_y)=(28,8),
     \qquad 28-8=20>0,
   \]
   
   and `q=4`, so every eligible opposite-side face satisfies
   `ell(P_y)=R^(4m)=R^12` (up to an absorbable scalar convention).

4. **That Section 7 theorem is a face-power/root-cut engine, not a source
   forest.**  It does not retain all sibling roots, identify cumulative
   translations with Puiseux truncations, prove a leaf/place bijection,
   cover all pole paths, or supply deck, fibre, component-sort, `td/type`,
   or Sigray `Q/jump/max` data.

The shortest sound strategy is therefore a **hybrid**:

\[
 \text{same-pair VGG Cor. 7.4 face powers}
 \; + \;
 \text{all-root Newton--Puiseux/Sigray coverage}
 \; + \;
 \text{the existing exact local G2 compiler}.
\]

The exact earlier Conjecture-A boundary is unchanged:

\[
 \boxed{\text{signed-transpose equivariance of every printed clause: PASS}}
 \qquad
 \boxed{\text{same-fixed-pair second-source inference: FAIL}.}
\]

The first box gives a theorem on the conjugated pair and re-encodes the
native run.  The Section 7 result audited here is a separate, strictly
partial theorem on the anti side of the fixed pair; it does not turn the
second box into a complete-chain pass.

The minimal new result is not a wholesale anti-standard Theorem 2.20.  It
is the `C74-PLACE` all-root, cumulative-map, place/proximity interface stated
in Section 6; its first degree-bearing successor is `EXIT-RPMC(C)`.

## 1. The exact same-pair opposite chart

Let `(P,Q)` be the fixed polynomial Keller pair in the original variables
`(x,y)`.  Introduce local coordinates for the other chart by

\[
  (Y,V)=(y,-x),\qquad
  P_y(Y,V)=P(-V,Y),\qquad Q_y(Y,V)=Q(-V,Y).
  \tag{1.1}
\]

The coordinate map `(Y,V) -> (x,y)=(-V,Y)` has determinant one.  Directly,

\[
 [P_y,Q_y]_{Y,V}
 =(\partial_yP)(-\partial_xQ)-(-\partial_xP)(\partial_yQ)
 =[P,Q]_{x,y}.
 \tag{1.2}
\]

Thus (1.1) is an honest expression of the **same pair** in the other
coordinate cylinder.  It is different from using the transpose theorem on
a newly conjugated pair and then calling that old run a second source.

For a global exponent `(i,j)`, the local exponent is `(j,i)`.  The support
transpose reverses ordinary endpoint orientation.  Hence the native source
data

\[
  A_0=(8,28),\quad A'_0=(1,0),\quad
  (\rho_0,\sigma_0)=(4,-1),\quad (m,n)=(3,2),\quad p/q=3/4
  \tag{1.3}
\]

become

\[
  w_0=(-1,4),\qquad
  \frac1m\operatorname{st}_{w_0}(P_y)
  =\frac1n\operatorname{st}_{w_0}(Q_y)=(28,8).
  \tag{1.4}
\]

The relevant value is positive:

\[
 v_{1,-1}(28,8)=28-8=20,
 \qquad v_{-1,4}(28,8)=-28+32=4>0.
 \tag{1.5}
\]

The valuation-ratio hypotheses needed on this side are not guessed.  In
local coordinates,

\[
 v_{1,1}(P_y)=v_{1,1}(P),\qquad
 v_{0,1}(P_y)=v_{1,0}(P),
 \tag{1.6}
\]

and similarly for `Q`.  The two ratios in VGG Proposition 7.3 are therefore
exactly the two ratios already present in Definition 4.3 for the original
standard pair.

On the other hand, `(P_y,Q_y)` is **not** a VGG `(m,n)`-pair under the
printed Definition 4.3.  Its local horizontal endpoint is `(28,8)`, so both
the base sign and the extra standard sign are positive, whereas Definition
4.3 requires the relevant `v_(1,-1)` values to be negative.  This is the
precise reason Theorem 2.20 cannot simply be invoked on (1.1).

## 2. What VGG Section 7 actually proves on this side

### 2.1 Printed opposite-interval theorem

VGG Proposition 7.3 assumes

\[
 [P,Q]\in K^*,\qquad
 \frac{v_{1,1}(P)}{v_{1,1}(Q)}
 =\frac{v_{0,1}(P)}{v_{0,1}(Q)}=\frac mn,
 \tag{2.1}
\]

a direction `w_0=(rho_0,sigma_0)` with positive `P` valuation, aligned
starting points for `P,Q` and the iterated brackets `T_j`, and

\[
  \frac1m\operatorname{st}_{w_0}(P)=(a/l,b),
  \qquad b<a/l.
  \tag{2.2}
\]

Condition (2.2) is exactly the anti-standard positive sign
`v_(1,-1)(a/l,b)>0`.  On the maximal subinterval from `w_0` toward
`(0,-1)` on which `v_w(P)>0`, it concludes

\[
 [\ell_w(T_j),\ell_w(P)]=0,
 \qquad
 \frac{v_w(T_j)}{v_w(P)}
 =\frac{v_{w_0}(T_j)}{v_{w_0}(P)}.
 \tag{2.3}
\]

Corollary 7.4 specializes the central element `F`.  If

\[
 \operatorname{st}_{w_0}(F)=\frac pq(a/l,b),
 \qquad \gcd(p,q)=1,
 \tag{2.4}
\]

then for every direction in the same certified interval there is a
homogeneous `R_w` such that

\[
       \ell_w(P)=R_w^{qm}.
 \tag{2.5}
\]

The printed corollary states (2.5) only for `P`.  Its proof contains a useful
stronger companion: applying Proposition 7.3 also with `T_0=Q`, it writes
the four relevant leading forms as powers of one common primitive `R_0`;
the exponent calculation gives `u_P=qm*s/d` and `u_Q=qn*s/d`.  Thus, after
rescaling the same primitive factor,

\[
       \ell_w(P)=\alpha S_w^{qm},\qquad
       \ell_w(Q)=\beta S_w^{qn}.
 \tag{2.5a}
\]

For live `q=4`, this is the paired `R^12/R^8` architecture.  Formula (2.5a)
is recoverable from the printed proof, but the corollary does not package
the paired residual, choose a root, build a branch tree, or associate any
root with a place of a fibre.

This is not an inferred symmetry.  It is the paper's explicit “direcciones
menores” proposition and its `fracciones de F1` corollary.  The proof says to
mimic the greater-direction proof; its hypotheses deliberately replace the
standard negative corner by (2.2) and use the opposite interval.

The sign's role in that mirrored proof is exact.  In the printed
greater-direction proof, `b>a/l` first gives
`v_(1,-1)(en_w0(P))<0` and a nonnegative alignment coefficient for every
nonzero `T_j`.  The perpendicular direction to that endpoint is then placed
strictly on the correct side of each successive face using positivity of
the two endpoint valuations.  This placement drives the “an intermediate
unmatched face would make all later iterated brackets nonzero”
contradiction.  Inductively, the negative endpoint sign is preserved; if a
later direction crosses `rho+sigma=0`, the assumptions `v_w(P)>0` and
nonnegative polynomial-coordinate exponent rule out sign zero and the
opposite sign.  Proposition 7.3 exchanges `en` for `st`, reverses that
interval, and uses `b<a/l` to reproduce exactly these three steps with the
positive sign.  Thus the positive sign is genuinely proved usable for
(2.3), but only for (2.3)—the proof does not construct regular corners or
children.

### 2.2 Live `8_28` consequence

Equations (1.2), (1.4)--(1.6), together with the coefficient-complete GGV
source hypotheses, place the fixed pair in Corollary 7.4 with

\[
       w_0=(-1,4),\qquad (a,b)=(28,8),\qquad p/q=3/4.
 \tag{2.6}
\]

Consequently, on every face in the certified positive interval,

\[
       \ell_w(P_y)=R_w^{4m}=R_w^{12}.
 \tag{2.7}
\]

The campaign's exact support reduction makes this concrete.  Dividing the
flipped apex `(28,8)` by `q=4` gives

\[
       \operatorname{en}(R)=(7,2).
 \tag{2.8}
\]

The two arithmetically admissible continuations are

\[
 \begin{array}{c|c}
 \operatorname{st}(R)&\text{face direction}\\ \hline
 (1,0)&(1,-3)\\
 (3,0)&(1,-2).
 \end{array}
 \tag{2.9}
\]

The first is the face corresponding to the original physical
`upper_dir=(-3,1)`.  Its primitive factor has the exact shape

\[
       R=Y\,h(Y^3V),\qquad \deg h=2,
 \tag{2.10}
\]

so the residual multiplicity partitions are `[2]` and `[1,1]`.  For every
nonzero residual root `lambda`, the cut

\[
       V\longmapsto V+\lambda Y^{-3}
 \tag{2.11}
\]

has determinant one.  Thus Corollary 7.4 gives a theorem-backed root core
on the physical other side; it is not merely a support analogy.

This live conclusion remains conditional on an exact Keller realization of
the frozen `8_28` source packet.  The current `CornerData` supplies the
arithmetic in (2.6)--(2.10), not coefficients of a Keller pair.

### 2.3 Exact scope: supplied versus missing

| object | VGG 7.3/7.4 supplies it? | comment |
|---|---:|---|
| same fixed pair in the `y` cylinder | **yes** | (1.1)--(1.2), not a second conjugated pair |
| opposite-interval bracket-zero propagation | **yes** | equation (2.3) |
| constant valuation ratios | **yes** | equation (2.3) |
| perfect-power `P` faces | **yes** | equation (2.5) |
| legal determinant-one root translations | **yes, locally** | after a residual root is chosen |
| paired `Q` power on a certified face | **yes, from the proof** | common primitive exponents `qm/qn`; not stated in the corollary |
| paired `Q` residual custody after cuts | **no** | must be retained by the interface |
| all sibling roots retained | **no** | the degree-reduction use selects/cuts roots |
| cumulative map equals a Puiseux truncation | **no** | no branch evaluation appears in the theorem |
| termination and leaf/place bijection | **no** | no residual forest is constructed |
| every other-chart pole path reached | **no** | no fibre or boundary place is named |
| deck orbit and fibre tag | **no** | absent from the source type |
| `td/type` or Sigray `Q/jump/max` | **no** | these are downstream place invariants |

VGG's own final Section 8 remark confirms the limited scope.  Corollary 7.4
supports a successful “squeezing” in the special `B=16` argument, but the
paper gives a constant-Jacobian Laurent example where the stronger desired
linear-factor squeezing cannot be achieved.  A face power is not a hidden
complete-chain theorem.

## 3. Where the standard sign enters the complete-chain proof

The sign is not a cosmetic choice that can be repaired by reversing arrows
in the final statement.

| proof gate | exact use of the sign | why a formal reversal fails |
|---|---|---|
| VGG Definition 4.3 | An `(m,n)`-pair requires `v_(1,-1)(en_10(P))<0`; “standard” also requires `v_(1,-1)(st_10(P))<0`. | The same-pair local object fails before any regular-corner proposition is available. |
| VGG Proposition 4.5 | The negative endpoint is used to force endpoint alignment, positivity/integrality of the normalized corner, `v_(0,-1)<-1`, and non-monomiality. | Enlarging the definition to positive endpoints invalidates the base package used later. |
| definition and existence of regular corners | A regular corner `(a/l,b)` is required to have `b>a/l`, i.e. negative `v_(1,-1)`.  The unique-corner existence proof derives this directly from Definition 4.3. | The anti corner `(28,8)` is not a regular corner in this category. |
| VGG type-II.b multiplicity proposition | Its extra hypothesis is `v_(1,-1)(st_w(P))>0`; this is the exceptional positive lower endpoint *inside* a standard run. | The positive sign is already assigned a specific role, not obtained by globally flipping the category. |
| VGG Proposition 5.17 (Case III) | The statement starts from a regular corner and proves that a pure-power translation produces a predecessor regular corner while preserving the `(m,n)`-pair. | It inherits the negative regular-corner and standard-pair package; reversing `Pred` does not establish its analogue. |
| VGG Proposition 5.18 (Case II), including (5.9) | The multiplicity bound forces the translated starting point to have `v_(1,-1)<=0`; equality is excluded by the central theorem, hence it is strictly negative and becomes a type-II.a regular corner. | This is the orientation-reset step.  With all signs reversed, the same inequality points the wrong way. |
| unique primitive/type-II.b corner | The standard negative sign at direction `(1,0)` and the positive type-II.b starting sign imply that the type-II.b direction is not `(1,0)` and lies in the interior of `I=((1,-1),(1,0)]`. | The starting source and interval are not recovered from an anti endpoint. |
| GGV5 Theorem 2.20 initialization | The proof imports VGG Theorem 7.6's ordered set of regular corners: type II.a corners first, then the unique type II.b corner, with `A_0=en_10(P)/m`. | There is no anti Theorem 7.6 to import. |
| GGV5 recursion | Proposition 5.18 turns each selected type-II.b root into a negative generated corner; valid edges, generated corners and children all bake in that sign and decreasing direction order. | Reversing the displayed order leaves the definitions of valid/generated/child objects false. |
| termination | Case III is finite because `rho|l` and `0<-sigma<rho` in `I`; the main recursion has strict descent `v_01(A_(i+1))<v_01(A_i)` through positive integral corner heights. | The opposite arc has neither this finite direction box nor this bounded descent without a new proof. |

There are therefore two valid but different statements:

- Transporting **all** definitions by the signed transpose gives a complete
  theorem for the conjugated pair.  That is exact equivariance, but it is
  the old physical run in new coordinates.
- Holding the pair and physical chart fixed and merely reversing signs and
  direction order does **not** give Theorem 2.20.  VGG 7.3/7.4 is the
  strongest printed opposite-side substitute found in the primary source.

## 4. Normalization audit and no-go theorem

### 4.1 All constant-Jacobian automorphisms of the cylinder

Let

\[
       A=K[u^{\pm1},v].
\]

The units of `A` are `c*u^r`.  Consequently every `K`-algebra
automorphism has the form

\[
 \Phi(u)=c u^\epsilon,\qquad
 \Phi(v)=d u^k v+b(u),
 \quad \epsilon\in\{1,-1\},\quad c,d\in K^*,
 \tag{4.1}
\]

with `k` integral and `b(u)` Laurent.  Its ordinary Jacobian is

\[
       J(\Phi)=\epsilon cd\,u^{\epsilon+k-1}.
 \tag{4.2}
\]

It is a nonzero constant exactly when

\[
       k=1-\epsilon.
 \tag{4.3}
\]

Thus there are only two classes:

\[
 \begin{array}{c|c|c}
 \epsilon&\Phi(v)&\text{effect on the Laurent ends}\\ \hline
 +1&d v+b(u)&u=\infty\text{ is preserved}\\
 -1&d u^2v+b(u)&u=\infty\text{ and }u=0\text{ are exchanged}.
 \end{array}
 \tag{4.4}
\]

This classification includes polynomial normalizations that preserve the
same cylinder.

### 4.2 Live chart-preserving sign no-go

In the live opposite chart the `m`-normalized support is the transpose of

\[
       S=\operatorname{conv}\{(0,0),(1,0),(8,28),(0,4)\}.
\]

It has the unique coordinatewise maximal point `(28,8)`; the actual `P`
endpoint is `m(28,8)`.  Consider an end-preserving map in the first line of
(4.4).  Let `s` be the largest Laurent exponent in `b(u)`, with
`s=-infinity` when `b=0`.

- If `s<=0`, the monomial at `m(28,8)` retains its nonzero
  `u^(28m) v^(8m)` term, no support term has larger `u` exponent, and the
  normalized high endpoint is still `(28,8)`.  Its sign is `20>0`.
- If `s>0`, the unique highest-`u` contribution is the constant-in-`v`
  term coming from `u^(28m)(dv+b(u))^(8m)`; its normalized exponent is
  `(28+8s,0)`.  Its sign is again positive.

Therefore:

> **Live cylinder no-go theorem.** No constant-Jacobian automorphism of
> `K[Y^{+-1},V]` that preserves the divisor `Y=infinity` turns the same
> fixed `8_28` other-chart pair into an input satisfying the negative
> Definition 4.3 endpoint sign.

### 4.3 `psi_2` does not evade the no-go

VGG Remark 6.8 defines

\[
 \psi_1(x)=y,\quad\psi_1(y)=-x,
 \qquad
 \psi_2(x)=-x^{-1},\quad\psi_2(y)=x^2y.
 \tag{4.5}
\]

Both have ordinary Jacobian one.  The second is exactly the `epsilon=-1`
class in (4.4).  It acts on directions by

\[
       (\rho,\sigma)\longmapsto(-\rho,2\rho+\sigma)
 \tag{4.6}
\]

and exchanges edge endpoints.

There are three independent obstructions to using it as the repair:

1. It exchanges the physical `Y=infinity` end with `Y=0`.
2. It sends the live anti source `(-1,4)` to `(1,2)`, not to the standard
   base direction `(1,0)`.
3. To obtain the two output standard ratios at `(1,0)` and `(1,1)`, (4.6)
   requires input ratios at `(-1,2)` and `(-1,3)`.  In original global
   coordinates these are `(2,-1)` and `(3,-1)`, on the other side of the
   live `(4,-1)` source and not supplied by its successor-ratio theorem.

VGG Proposition 6.9 composes `psi_2` after `psi_1` precisely when it has the
special `(2,-1)` and `(3,-1)` data, moving that particular corner to
`(1,0)`.  It does not map the live `(4,-1)` occurrence to a standard base,
and it changes which Laurent end and branch are being encoded.

### 4.4 Swaps and bare inversion, separated

| operation | source Jacobian | bracket effect | source/chart effect | verdict |
|---|---:|---|---|---|
| unsigned variable swap `(x,y)->(y,x)` | `-1` | changes bracket sign | transposes support and reverses endpoints | algebraically harmless only after tracking the sign; by itself not same-pair standardization |
| signed variable rotation, pulled back as `P_y(Y,V)=P(-V,Y)` | `+1` | preserves bracket | gives the exact local expression (1.1) | honest same-pair anti chart, but its sign is `+20` |
| component swap `(P,Q)->(Q,P)` | n/a | `[Q,P]=-[P,Q]` | swaps `(m,n)`; support signs unchanged | cannot repair orientation |
| signed component swap `(P,Q)->(Q,-P)` | n/a | preserves the bracket | swaps component role; support signs unchanged | needed for downstream component sorting, not chart repair |
| bare inversion `Y=u^-1` | `-u^-2` | turns a constant bracket into a monomial bracket | swaps the Laurent end | not a Keller normalization |
| compensated inversion `psi_2` | `+1` | preserves bracket | swaps `Y=infinity` and `Y=0` | valid Laurent operation, wrong physical chart/source |

Composing the unsigned variable and component swaps restores the bracket
sign, but it still only relabels/conjugates the old occurrence.  It does not
create a second source on the fixed pair.

## 5. Why the Section 7 route is cheaper than a new anti-Theorem 2.20

A complete anti-standard chain theory would have to reprove, on a different
direction arc:

1. existence and uniqueness of the starting corner;
2. the full type I/II/III classification;
3. a reversed Case-III move;
4. a multiplicity theorem whose translated corner has the needed sign;
5. preservation of the anti pair at every child;
6. a bounded descent/termination invariant;
7. complete-chain arithmetic and admissibility.

Even if completed, the printed GGV construction follows one selected root.
It would still need an all-root and place-coverage theorem for G2.

Corollary 7.4 has already paid for the hardest face-algebra input needed on
the opposite side: it certifies the high power and exposes a primitive face
factor, up to the expected scalar/root-of-unity choices, under the Keller
hypotheses.  Newton--Puiseux already has the all-root termination and
place-completeness machinery.  The economical proof target is to show that
these two descriptions coincide, rather than rebuilding all seven chain
layers and then adding that coincidence anyway.

## 6. Precise minimal missing lemma and degree successor

### `C74-PLACE`: Corollary-7.4 all-root face-to-place/proximity lemma

Let `(P,Q)` be an exact polynomial Keller pair, let `(P_y,Q_y)` be its
same-pair local expression (1.1), fix the component-sorted fibre `H=a`, and
assume a coefficient-complete Corollary-7.4 packet at `w_0`, including the
central element, the exact paired leading forms and the cumulative source
map.

At each Corollary-7.4 face that meets the physical `y=infinity` boundary,
write

\[
       \ell_w(P_y)=R_w^{qm}
\]

and factor the one-variable residual of the primitive factor `R_w`.  Extract
and record the paired common-primitive form (2.5a); in live `(m,n,q)=
(3,2,4)` it is `ell(P_y)=alpha*R^12` and `ell(Q_y)=beta*R^8`.  For **every**
residual root, retain a child rather than choosing one: a nonzero root gets
the corresponding determinant-one translation in the required Kummer ring,
while a zero root gets its identity/axis continuation with explicit
provenance.  (For the live face (2.10), its nonzero constant endpoint makes
the roots of `h` nonzero.)  Complete each child by the ordinary all-root
Newton--Puiseux algorithm; do not assume that Corollary 7.4 recursively
re-applies after the cut.  Then prove:

1. **Truncation compatibility.**  Along each child, the composite source
   map is exactly the strict Newton--Puiseux truncation map of the
   corresponding branch of `H=a`.
2. **All-place coverage.**  Every boundary place of `H=a` in this
   `y=infinity` chart enters one of the certified first-root children, and
   the Newton--Puiseux completions terminate with leaves modulo the full
   Kummer deck action in bijection with those places.
3. **Typed custody.**  The fibre value, component-sort bit, paired `Q`
   residual, root multiplicity and deck stabilizer survive every cut, so a
   leaf feeds the existing exact local source-to-Sigray compiler.

`C74-PLACE` is deliberately local to the other chart.  Together with the
native-chart all-root version and the elementary two-chart partition of
boundary places, it gives pole-path coverage.  By itself it asserts no
`td/type` formula and no Sigray `Q/jump/max` value; those are computed from
the resulting exact places.

The load-bearing clause is (1).  Merely enumerating all factors of
`R_w` does not prove that the accumulated GGV translations are the actual
Puiseux coefficients of `H=a`.  Clauses (2)--(3) then prevent duplicate deck
presentations and loss of the paired component—the two failure modes already
visible in the campaign prototype.

For the resolution-theoretic use, add one output field: the infinitely-near
base center corresponding to every certified face and first exit, with no
duplication under deck quotient.  Proposition 7.3 gives

\[
       \frac{v_w(P)}m=\frac{v_w(Q)}n
\]

throughout its corridor.  Once `C74-PLACE` transports this equality through
the invertible proximity transform, and when `(m,n)` are identified with
the normalized pair exponents with the component sort tracked, the
normalized point-basis discrepancy is zero at every interior corridor
center.  Degree energy can occur only at the first nonproportional exits and
their descendants.

This identifies the clean numerical successor:

> **`EXIT-RPMC(C)` (still conjectural).**  Assign every nonzero normalized
> point-basis discrepancy to its unique first exit from a
> Proposition-7.3 corridor.  For each proper leading root of multiplicity
> `mu`, bound the total discrepancy energy of all its exit subtrees by
> `C*mu/B`, uniformly in `B`.

`C74-PLACE + EXIT-RPMC(C)` would give the existing `RPMC(C)` route to a
type-relative degree bound.  It would still not give a selected-pair type
cap or JC2.  The cheapest informative follow-on after the desk test below
is the `mu=1`, one-exit sector: classify the paired integrable first-exit
jets and seek the required root-length budget.  Extending a proportional
corridor farther has lower value, because its transported discrepancy is
zero.

## 7. Cheapest desk test and observed evidence

### 7.1 Frozen live arithmetic gate

The existing exact reducer was run locally (desk scale, about 1.2 seconds):

```text
PYTHONPATH=lib python3 - <<'PY'
from families import section4_families
from reduce4 import reduce_family
r = reduce_family(section4_families()['8_28'])
print(r.status, len(r.cases))
for line in r.log[:16]: print(line)
PY
```

It returned `reduced 2` and independently reproduced:

```text
Cor 7.4 at flipped chain edge 0, dir (-1, 4), q=4:
    l(P) = lam R^4m on the Pred faces, en(R)=(7,2)
continuations:
    st(R)=(1,0), dir=(1,-3)
    st(R)=(3,0), dir=(1,-2)
face (1,0)->(7,2) @(1,-3): residual shapes [2] and [1,1]
```

This tests the arithmetic specialization of the printed theorem.  It does
not create the missing exact Keller coefficients.

### 7.2 All-root interface regression

The custody-correct replay

```text
python3 cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify_r1.py
```

passed in about 0.06 seconds with
`mathematical_result_unchanged=true`.  Its deliberately non-Keller control
has a same-support `8_28` ledger and, in the `y=infinity` chart:

- residual `X^16-1`, with all 16 simple roots matching 16 unramified
  boundary places;
- a paired residual that distinguishes `tau=1` from `tau=2` although the
  ledger and branch count are unchanged;
- pole orders `{12:16}` versus `{12:15,11:1}` after that invisible
  mutation.

This is the cheapest regression for clauses (2)--(3) of `C74-PLACE`:
dropping siblings loses places, and dropping the paired residual loses pole
data.
Because the control is not Keller, its square-free faces are **not**
evidence for or against Corollary 7.4; they are a theorem-guard negative
control only.

### 7.3 Next desk proof test

Before any larger implementation, use the generic quadratic

\[
       R=Y(c_0+c_1Y^3V+c_2Y^6V^2)
\]

for the `(1,0)->(7,2)` face and perform both residual partitions `[2]` and
`[1,1]` symbolically.  For every root, record the map (2.11), its Kummer
deck action, and the transformed paired residual.  Check that:

1. every map has determinant one;
2. the cumulative map agrees term-by-term with one Newton--Puiseux
   truncation;
3. simple roots give distinct leaves before the deck quotient and exactly
   one leaf orbit afterward;
4. the paired-residual mutation from the prototype is detected.

This costs well under one CPU minute and needs no AWS or heavy algebra.  A
failure localizes `C74-PLACE` to truncation compatibility or custody before any
attempt at a general proof.

## 8. Evidence and scope controls

- Primary VGG source read from arXiv:1401.1784v3; downloaded source
  `vgg.tex` SHA-256
  `b4908fd5351210562958ad81ab13dddaee2c257a55362930f68790d0e234724d`.
- Primary GGV5 source read from arXiv:1708.07936v1; downloaded source
  `ggv5.tex` SHA-256
  `8f5571eb5fb5c594a9be47972e6331a3d0b6492edb6b44718ec102ae92dc1453`.
- Prototype custody wrapper `verify_r1.py` SHA-256
  `7c1205ff3247e06c31729c22a65c39b1e5bf3bd99e28d5fe6a7780ab3ac315b5`;
  frozen mathematical result SHA-256
  `deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd`.
- The signed-transpose clause audit in
  `xmodel/g2-transpose-equivariance-hostile-audit-sol-ultra-20260827.md`
  remains correct: theorem equivariance passes, but it does not create the
  same-pair second source.  This report adds the Section 7 partial theorem
  and the chart-preserving normalization no-go.
- No claim here promotes the coefficient-free live `CornerData` to an exact
  Keller pair, proves `G2-PSC`, or proves/disproves JC2.
- Only this xmodel report was created.  No canonical ledger was edited; no
  heavy local algebra or AWS job was run.  The nested `jc2-lean` tree was
  not entered, read, built, or modified.  A parent-repository
  `git status --short` displayed only its aggregate `M jc2-lean` submodule
  entry; no Lean content or Lean status was inspected or used.
