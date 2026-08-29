# G2-PSC: typed source-to-decorated-pole-tree interface

**Date:** 2026-08-27T19:19Z  
**Author lane:** Sol Ultra, `g2_psc_typed_bridge`  
**Lifecycle:** frozen producer; independent review not yet attached  
**Verdict:** **EXACT PAIR-TO-TREE CONSTRUCTOR AND EXACT LOCAL FLAG
TRANSPORT; CURRENT FROZEN LEDGER IS NOT A SOURCE OBJECT; GLOBAL GGV
POLE-SKELETON CAPTURE REMAINS OPEN**

## 0. Result in one page

There are three different arrows, and only the first and the local part of
the second are presently theorems.

\[
\begin{array}{ccccc}
\text{exact pre-Laurent Keller pair + fibre}
 &\xrightarrow{\text{Newton--Puiseux}}&
 \text{corrected decorated Sigray pole tree} \\[1mm]
 \downarrow ? && \uparrow \text{exact local compiler}\\[-1mm]
\text{two-chart, all-root, source-provenanced GGV packet forest}
 &\xrightarrow{\qquad}&
 \text{same decorated pole tree.}
\end{array}
\tag{0.1}
\]

1. The top arrow is an exact, canonical construction once the **actual
   polynomial pair** and a fibre value are supplied.  Section 2 types it by
   explicit coordinate rings, completion maps, residual polynomials, and
   labels.  It is essentially the standard Newton--Puiseux construction; it
   is not `G2-PSC`, because it does not show that the GGV packet or farm
   controls the output.
2. A coefficient-complete GGV type-II.b cut, together with a compatible
   branch evaluation, maps exactly to one deck orbit of one Sigray flag.
   Section 3 gives the commutative ring diagram and the residual identity.
3. The left vertical arrow is the missing theorem.  GGV5 Theorem 2.20 gives
   a **linear selected-root trace** in the native `X=infinity` sector.  It
   does not give a two-chart all-root forest, does not prove that every pole
   path is reached, and does not supply the presentation maximum required by
   the reviewed Q/jump/max value of `kappa_F`.

The first obstruction occurs even earlier for the frozen campaign source.
The live `CornerData` record has fields

```text
name A0 A0p chain final steps k family mn j degP degQ S c upper_dir rhs_exp
```

and has no coefficient field, polynomials `P,Q`, fibre `a`, face polynomial,
selected root, deck action, or ring map.  Consequently there is no typed map

\[
  K[X,Y]/(H-a)\longrightarrow K((t))
\]

to even name a boundary branch.  The reviewed non-Keller `8_28` collision
then proves that this is a genuine information loss in the ambient
polynomial class: two controls with the same frozen ledger have pole masses
`276` and `275`.

The cleanest repair is therefore not one more integer in `CornerData`.
Retain the discrete record as a necessary-condition index, but make the G2
producer type an **all-root residual forest over the exact pre-Laurent pair**,
with both infinity charts, the fibre tag, cumulative source maps, paired
residual polynomials, and deck orbits.  The local forest-to-tree compiler is
exact.  Proving that GGV-eligible occurrences supply a complete such forest
is precisely the scoped pole-skeleton-capture obligation, not an
implementation detail.

## 1. Exact source types

### 1.1 Polynomial source and the lossless normalization map

Work over an algebraically closed characteristic-zero field `K`; for the
campaign theorem take `K=C`.  Keep native GGV variables capitalized:

\[
 A=K[X,Y],\qquad B=K[x,y].
\]

Let `(P,Q) in A^2` be the selected **pre-Laurent** standard GGV pair, with

\[
 [P,Q]=c\in K^*,\qquad \operatorname{mult}(P,Q)=(m,n),
 \qquad \gcd(m,n)=1,\quad m,n>1.
\]

The determinant-one source rotation in `ladder/TRANSPORT.md` is the ring
isomorphism

\[
 r^*:A\longrightarrow B,qquad X\longmapsto y,qquad Y\longmapsto -x.
\tag{1.1}
\]

Sort components before applying `r^*`:

\[
 (H,J)=
 \begin{cases}
   (P,Q),&m<n,\\
   (Q,-P),&n<m,
 \end{cases}
 \qquad (f,g)=(r^*H,r^*J).
\tag{1.2}
\]

Then `[H,J]=[f,g]=c`.  The first component `H` is load-bearing.  GGV's
chain convention follows native `P`, whereas Sigray's fibre is the
lower-multiplier component.  In the live `8_28` record `(m,n)=(3,2)`, so

\[
 H=Q,\qquad J=-P.
\tag{1.3}
\]

Any source contract containing only the `P` face, without its paired `Q`
face and the component-sort bit, is therefore ill-typed for the Sigray
fibre used downstream.

For `a in K`, put

\[
 B_a=B/(f-a),\qquad C_a=\operatorname{Spec}B_a.
\tag{1.4}
\]

Since `[f,g]=c`, the two partial derivatives of `f` cannot vanish together
at an affine point.  Thus `C_a` is smooth (and in particular reduced).
Let `bar C_a` be its projective closure, let

\[
 \nu_a:\widetilde C_a\longrightarrow\bar C_a
\]

be the normalization, and let

\[
 \mathcal B_a=\widetilde C_a\setminus C_a
\]

be its finite set of boundary places.  Every
\(S\in\mathcal B_a\) has a
complete DVR and an exact evaluation map

\[
 \iota_S:B_a\longrightarrow
 \operatorname{Frac}\widehat{\mathcal O}_{\widetilde C_a,S}
 \simeq K((t_S)).
\tag{1.5}
\]

Equation (1.5), not a corner tuple, is the smallest object that actually
names a fibre branch.

### 1.2 Coefficient-complete GGV witness

For comparison with GGV5 Theorem 2.20, define

\[
 L_i=K[X^{1/l_i},X^{-1/l_i},Y].
\tag{1.6}
\]

A **coefficient-complete witness** retains, for every stage `i`,

\[
 (P_i,Q_i,A_i,A_i',\rho_i,\sigma_i,l_i)
\]

and an exact cumulative homomorphism

\[
 \theta_i:A\longrightarrow L_i,qquad
 \theta_i(P)=P_i,\quad\theta_i(Q)=Q_i,
\tag{1.7}
\]

with `theta_0` the natural inclusion.  At a type-II.a step the transition is
the identity.  At a type-II.b step GGV5 supplies

\[
 l_{i+1}=\operatorname{lcm}(l_i,\rho_i),\qquad
 Z_i=X^{-\sigma_i/\rho_i}Y,
\tag{1.8}
\]

and a selected nonzero root `lambda_i` of the exact face polynomial in

\[
 \ell_{\rho_i,\sigma_i}(P_i)
   =X^{k_i/l_i}\mathfrak p_i(Z_i).
\tag{1.9}
\]

The Kummer-coordinate automorphism is

\[
 \phi_i(X^{1/l_{i+1}})=X^{1/l_{i+1}},\qquad
 \phi_i(Y)=Y+\lambda_iX^{\sigma_i/\rho_i},
\tag{1.10}
\]

so that `Z_i` is translated to `Z_i+lambda_i`.  A literal producer packet
must retain `(mathfrak p_i,lambda_i,phi_i)` and the corresponding data for
the paired component, not merely the corner and direction.  The frozen
`CornerData` object is only the candidate arithmetic projection of
(1.6)--(1.10); no polynomial Keller realization of the live candidate is
known.

For any `E in L_i`, write

\[
 v_i(E)=v_{\rho_i,\sigma_i}(E),\qquad
 u_i=-\frac{\sigma_i}{\rho_i}.
\]

There is a unique residual polynomial `r_{E,i}` with

\[
 \ell_{\rho_i,\sigma_i}(E)
 =X^{d_{E,i}}r_{E,i}(Z_i),
 \qquad d_{E,i}=\frac{v_i(E)}{\rho_i}.
\tag{1.11}
\]

This follows term by term: on the face,
`rho_i*r+sigma_i*s=v_i(E)` and
`X^rY^s=X^(r-u_i*s)Z_i^s`.

The GGV integer `l_i` is an ambient Kummer denominator.  It is not, without
the deck stabilizer and all branch presentations, automatically the global
Sigray `kappa_F` decoration.

## 2. The exact target type

### 2.1 Two branch fields and the Eggers--Wall forest

Sigray Statement 3.1 splits the boundary into two sets:

\[
\begin{aligned}
 \mathcal B_{a,y}&=\{S:x(S)=\infty, y(S)\in K\},\\
 \mathcal B_{a,x}&=\{S:y(S)=\infty, x(S)\in K\}.
\end{aligned}
\tag{2.1}
\]

For \(S\in\mathcal B_{a,y}\) choose a Puiseux presentation

\[
 x=t^{-\kappa},\qquad
 y=\sum_{j\ge0}c_jt^j=\sum_{j\ge0}c_jx^{-j/\kappa};
\tag{2.2}
\]

for \(S\in\mathcal B_{a,x}\) use the symmetric presentation with `x,y`
interchanged.  Root-of-unity choices are quotiented by the full deck orbit.

Within either chart let `O(S,T)` be the first exponent at which two Puiseux
series differ.  Define

\[
 T^*_{a,\chi}
  =(\mathcal B_{a,\chi}\times[0,\infty])/\sim,
 \qquad
 (S,u)\sim(T,u)\Longleftrightarrow u\le O(S,T),
\tag{2.3}
\]

and `T_a^*=T^*_{a,x} \sqcup T^*_{a,y}`.  Its vertices are the two
roots, all characteristic exponents, and all pairwise contact exponents.
This already exhibits a hard type mismatch: GGV5's primary chain lies in
the native `X=infinity, Y finite` sector.  Under (1.1) it maps to the single
Sigray component `y=infinity, x finite`.  It supplies no second-chart
forest.

### 2.2 Corrected denominator and residual decorations

Suppose a presentation has Puiseux characteristic

\[
 (\kappa,\beta_1,\ldots,\beta_s),\qquad
 e_j=\gcd(\kappa,\beta_1,\ldots,\beta_j).
\]

At a height `u` with
`beta_j/kappa <= u < beta_(j+1)/kappa`, its presentation denominator is
`kappa/e_j`; at a characteristic jump its presentation jump is
`e_(j-1)/e_j`, and otherwise it is `1`.  At a multiply realized vertex the
target uses the reviewed **Q/jump/max** convention: choose a jump
presentation attaining the maximum denominator.  This gives the global
labels

\[
 \kappa_F=\max_{S:\,F\in I_S([0,\infty])}\kappa_F(S),
 \qquad \nu_F=\text{the corresponding jump ratio (or 1)}.
\tag{2.4}
\]

Thus one selected GGV presentation cannot in general emit `kappa_F`.  The
exact local unequal-presentation model in `xmodel/sol-h5a.md` has values `1`
and `3` at the same vertex; the correct global value is `3`.

For `F in T_{a,y}` of height `u`, let `s_F(x)` be the common truncation
below `u` and put

\[
 \eta_F=x^u(y-s_F(x)).
\tag{2.5}
\]

In a suitable Kummer ring every `h in B` has a unique top expression

\[
 h^F(x,\eta)=x^{d_{h,F}}p_{h,F}(\eta)
   +\text{lower powers of }x,
\tag{2.6}
\]

with the symmetric definition on `T_{a,x}`.  Record

\[
 D_{h,F}=\kappa_Fd_{h,F}\in\mathbb Z,qquad
 \bar\kappa_F=\kappa_F(1-u).
\tag{2.7}
\]

The fibre selector and map component must both be present:

\[
 p_{f-a,F},\quad p_{f,F},\quad p_{g,F}.
\tag{2.8}
\]

Starting with `h_0=g`, retain Sigray's exact approximate-root tower whenever

\[
 (h_{j,F}^+)^{k_j}=s_j(f_F^+)^{l_j},qquad
 \gcd(k_j,l_j)=1,\quad s_j\in K^*,
\tag{2.9}
\]

and set

\[
 h_{j+1}=h_j^{k_j}-s_jf^{l_j}.
\tag{2.10}
\]

For each boundary place `S`, let `F_S^*` be the first point after which its
tower length is zero.  The Sigray pole vertices are the positive such
thresholds.  At a pole vertex retain at least

\[
 \bigl(u,\kappa_F,\nu_F,D_{f,F},D_{g,F},
 p_{f,F},p_{g,F},\deg p_{f,F},\deg p_{g,F},
 (h_j,k_j,l_j,s_j)_j\bigr),
\tag{2.11}
\]

the chart, parent/child and contact data, the deck action, and

\[
 M_F=\gcd(\deg p_{f,F},\deg p_{g,F}),\qquad
 \Lambda(F)=\frac{D_{g,F}\deg p_{f,F}}{\nu_F}.
\tag{2.12}
\]

Call the resulting two-component, pole-spanned decorated forest
`DPT_a(f,g)`.  This target contains the labels consumed by the later book
machinery; an integer corner chain does not.

### Theorem 2.1 (exact pair constructor)

The data `(K,P,Q,c,m,n,a)` in Section 1.1 determine `DPT_a(f,g)` uniquely up
to deck-equivariant decorated rooted-forest isomorphism.

**Status:** **EXACT relative to standard Newton--Puiseux theory and the
campaign's reviewed corrections to Sigray's definitions.**

**Proof.**  Equations (1.1)--(1.4) determine the exact fibre algebra.  Its
projective normalization determines the finite set (1.5) intrinsically.
Newton--Puiseux over an algebraically closed characteristic-zero field
constructs all expansions (2.2); conjugate presentations are exactly deck
orbits.  Their characteristic exponents and pairwise contacts define
(2.3).  Substitution in (2.5)--(2.6) evaluates every named polynomial and
hence determines all residuals, the Q/jump/max labels, and the tower
(2.9)--(2.10).  Pole orders in the complete DVRs determine the pole
thresholds and (2.12).  Every operation is invariant under reparametrizing
`t_S`; the deck quotient removes the Kummer-root choice.  This proves
existence and uniqueness of the decorated forest.  \(\square\)

This theorem is deliberately not called `G2-PSC`.  It consumes the whole
unknown polynomial pair, so it transfers no coefficient-free GGV farm
restriction to a receiver.

## 3. What a coefficient-complete GGV cut does prove

Let

\[
 \mathscr P_X=\bigcup_{N\ge1}K((X^{-1/N}))
\tag{3.1}
\]

be the native Puiseux field.  A branch cylinder through stage `i` is an
evaluation

\[
 \beta_i:L_i/(\theta_i(H)-a)\longrightarrow\mathscr P_X.
\tag{3.2}
\]

At a transition it must satisfy the literal commutative condition

\[
 \beta_i=\beta_{i+1}\circ\phi_i
 \quad\text{on }L_i,
\tag{3.3}
\]

with the natural Kummer inclusion understood.  Equivalently,

```text
 A/(H-a)  --theta_i-->  L_i/(theta_i(H)-a)
    |                         |
    |                         | beta_i
    v                         v
 A/(H-a)  ------------->   P_X
```

commutes at every prefix.  The root/deck orbit of (3.2), rather than a root
token, is the intrinsic occurrence.

Compose (3.2) with the inverse of (1.1): normalized functions satisfy

\[
 x=-Y,\qquad y=X.
\tag{3.4}
\]

Thus a native `X=infinity` cylinder maps to the normalized Sigray
`y=infinity` component.  At height `u_i=-sigma_i/rho_i`, after the earlier
cuts have been absorbed into `theta_i`, Sigray's transverse coordinate is

\[
 \eta_F=y^{u_i}(x-\text{earlier truncation})=-Z_i.
\tag{3.5}
\]

Combining (1.11) and (3.5) gives the exact local identities, up to the
recorded target sign and deck conjugacy,

\[
\begin{aligned}
 d_{f,F_i}&=d_{\theta_i(H),i},
 &p_{f,F_i}(\eta)&=r_{\theta_i(H),i}(-\eta),\\
 d_{g,F_i}&=d_{\theta_i(J),i},
 &p_{g,F_i}(\eta)&=r_{\theta_i(J),i}(-\eta).
\end{aligned}
\tag{3.6}
\]

On the positive-weight segment the constant `a` does not change the leading
face; outside it, the packet must separately retain `r_{theta_i(H)-a,i}`.
The same formula evaluates every transported approximate root `h_j`.

### Proposition 3.1 (local flagged transport)

Given the exact source data (1.6)--(1.11) and a compatible evaluation
(3.2)--(3.3), equations (3.4)--(3.6) determine a deck-stable Sigray flag
segment and preserve its paired residuals, current divisorial orders, and
source provenance.  If the supplied segment reaches the pole threshold and
separates its branch, it also determines that branch's pole order.  If all
presentations through a vertex are supplied, (2.4) determines its corrected
`kappa,nu` labels.

**Proof.**  Newton polygon root lifting gives the branch cylinder once its
exact residual root and fibre-component compatibility are supplied.
Equations (3.3) pull the cylinder back through every Kummer translation.
The signed-axis substitution (3.4) is an isomorphism of function fields,
and the calculation (3.5) proves (3.6) term by term.  Contact and
characteristic data are invariant under the field isomorphism.  Taking all
presentations and the deck quotient gives (2.4).  \(\square\)

This is the strongest unconditional packet-to-tree statement found at desk
scale.  It maps **one certified occurrence to one flag segment**.  It does
not assert that the occurrence exists for the sorted fibre component at
every primary selected root, that all roots were selected, that the other
chart was run, or that every pole threshold was reached.

## 4. The narrowest composable G2-PSC contract

Do not ask a linear GGV chain to return a full tree.  Define an intermediate
source object `ARF_a(P,Q)` (all-root residual forest) with the following
receiver-demand fields and no precomputed Sigray pole mass:

1. exact references to `(P,Q)`, `a`, the component-sort bit, and (1.1);
2. one root in each of the two infinity charts;
3. at every node, a cumulative source/Kummer map `theta_omega`, its inverse
   on the function field, a chart and rational cut height;
4. the full residual polynomials of `H-a,H,J` and every active `h_j`, with
   coefficients, factor multiplicities, and every deck/root orbit;
5. parent IDs and intrinsic rank-two flag/Enriques IDs for gluing duplicate
   presentations;
6. deck stabilizers, so reduced presentation denominators can be computed;
7. a fail-closed degree/normalization certificate that every boundary
   branch orbit has been emitted and expanded through all characteristic and
   contact vertices needed to decide its `g` order and tower threshold.

The fields in this list are **sufficient**, not claimed collision-minimal.
In particular, the reviewed `8_28` collision forces only the changed
second-chart residual/root/pole vector and its source-monomial provenance;
it does not prove every listed field individually necessary.

### Theorem 4.1 (forest compiler)

If `ARF_a(P,Q)` satisfying items 1--7 is supplied, the procedure in Theorem
2.1 factors through it and emits `DPT_a(f,g)` uniquely.  It preserves every
label in (2.11)--(2.12), adjacency, chart, deck orbit, and source
provenance.

**Status:** **EXACT.**  This is finite Newton--Puiseux/approximate-root
reconstruction: full residual factorization emits successors; intrinsic
flag IDs glue occurrences; all presentations give Q/jump/max; paired
residual evaluation gives `d,D,p`, the tower, pole status, and pole mass.

### Scoped conjecture G2-PSC, now typed

For the globally selected pre-Laurent GGV-minimal Keller pair and every
fibre `a`, the factor-expanded occurrences licensed by the GGV source theory
can be organized into an `ARF_a(P,Q)` satisfying items 1--7.

Equivalently, the missing content has three clauses:

\[
\boxed{\text{all roots + both charts + all pole-path thresholds}}
\tag{4.1}
\]

\[
\boxed{\text{exact paired residual/source-map fidelity at each occurrence}}
\tag{4.2}
\]

\[
\boxed{\text{deck/flag quotient has no missing or spurious adjacency}.}
\tag{4.3}
\]

Clause (4.2) is the local theorem once an occurrence and its maps are
present.  Clauses (4.1) and the no-missing half of (4.3) are the global
mathematics.  GGV5 Theorem 2.20 proves none of them at forest scope: it
selects one `lambda_i` at a type-II.b step, stays in one direction sector,
and ends in one complete chain.

## 5. First exact obstructions

### O0. Frozen source type: failure before mathematics

The live `8_28` `CornerData` contains no `K,P,Q,a`.  Hence neither the
domain `A/(H-a)` nor any map (3.2) can be formed.  It also lacks
`mathfrak p_i,lambda_i,phi_i`, so the first type-II.b branch is unnamed.
This is an exact schema obstruction, not a difficult proof step.

### O1. Nonfunction on the ambient polynomial class

The frozen reviewed controls

\[
 f=B^2-x-y^8,\qquad
 g_\tau=B^3-2x^2y^2+y^{12}+\tau xy^{15},
 \quad B=x(xy^4-1)^7,
\]

with `tau=1,2` have the same current `8_28` ledger.  Their second-chart
residual differs at one root, changing a pole order `12 -> 11` and total
pole mass `276 -> 275`.  Therefore a function

\[
 \texttt{CornerData}\longrightarrow\texttt{DPT}
\]

does not exist on arbitrary polynomial realizations.  These controls are
not Keller, so this does not refute a Keller-restricted theorem.

### O2. A primary complete chain is a trace, not a forest

At each type-II.b step Theorem 2.20 asserts existence of **a** root
`lambda_i`; it does not retain every root orbit.  The direction interval is
the native `X=infinity` chart.  A linear chain therefore lacks unselected
roots, the other infinity chart, and contact data between occurrences.  Even
the complete residual germ on its chosen trace can miss a pole created on
the other chart; `xmodel/sol-landing1.md` gives an exact hidden-tail
separation.

### O3. One presentation does not determine Q/jump/max

An ambient Kummer denominator `l_i`, or the denominator read along one
selected branch, need not equal the maximum (2.4) at a multiply realized
vertex.  Substituting the coarse presentation value can make
`D_(h,F)=kappa_F*d_(h,F)` nonintegral.  Thus the tempting assignment
`kappa_F=l_i` (or blindly `l_(i+1)`) is not a valid global label without an
all-presentation/deck certificate.

### O4. The post-Laurent endpoint has the wrong algebraic type

The GGV22 Proposition 4.3 endpoints with `[P,Q]=X^2` are not objects in the
constant-Jacobian polynomial category of (1.1)--(1.5).  They may be retained
as recoverable valuation metadata, but cannot replace the pre-Laurent pair
in Theorem 2.1.

## 6. Failed shortcuts and their smallest failure

| attempted shortcut | first failure |
|---|---|
| `CornerData -> tree` | no coefficient/fibre ring or branch map; ambient `8_28` collision |
| exact selected GGV chain -> full tree | one root trace, one chart, no pole-skeleton surjectivity |
| `l_i -> kappa_F` | ignores deck stabilizer and Q/jump/max across presentations |
| retain only residual degrees/multiplicities | paired coefficient cancellation changes pole order |
| use only native `P` | sorted Sigray fibre is native `Q` when `n<m`, including `8_28` |
| use symplectic residue to find omitted places | residue evaluates an already named flag; it does not enumerate branches |
| call Theorem 2.1 `G2-PSC` | it consumes the whole pair and imports no packet/farm restriction |
| use GGV22 `[P,Q]=X^2` endpoint | wrong bracket and non-polynomial inverse source step |

## 7. Cheapest next discriminator

The smallest missing receiver scalar already isolated by the reviewed
`8_28` collision is the second-chart residual value

\[
 R_\tau(C)=C^8+1+\tau C\pmod{C^{16}-1};
 \qquad R_\tau(-1)=2-\tau.
\tag{7.1}
\]

The cheapest Keller-specific information test is therefore not a full tree
compiler.  On the exact source-pinned `8_28` coefficient scheme:

1. expose the source coefficient(s) mapping to the analogue of `tau` and
   serialize the paired second-chart residual scalar `r`;
2. impose the literal constant-Jacobian rows and every localization defining
   the chosen GGV stratum;
3. ask whether `r` is constant in the reduced localized coordinate ring, or
   produce two exact points with the same discrete packet and different
   `r`;
4. only if it is forced, move to the next root orbit/label.

An exact two-point Keller collision would refute **ledger-only** fidelity on
that stratum.  Constancy of this one scalar would merely bank one missing
field; it would not prove all-root or both-chart coverage.  Finite truncation
or modular variation alone is diagnostic, not a Keller-pair theorem.  Any
large elimination belongs on a registered AWS node; none was run for this
report.

At the interface level, an even cheaper immediate engineering test is to
serialize one occurrence with

```text
(PairRef, fibre, component-sort, chart, theta_i,
 paired face residuals, root/deck orbit, inverse source map, flag ID)
```

and require the literal commutative identities (3.3) and (3.6).  Failure
returns `NOT_TYPED_COMPOSABLE`; success proves only one flagged segment and
may be consumed while the global coverage review runs in parallel.

## 8. Exact desk checks

All checks were read-only, standard-library, and desk-scale.  No Singular,
large Python algebra, AWS job, or `jc2-lean` action was used.

```text
$ python3 -B tests/test_families.py
...
Gate B OK: S4 corner data for (9,27),(9,24),(8,28),(7,21) exact
ALL FAMILIES TESTS PASS
exit 0

$ python3 -B cases/transport_check.py
status: PASS
8_28 GGV degrees: (108,72)
Sigray degrees/type: (72,108), (2,3)
exit 0

$ python3 -B cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify_r1.py
status: PASS
mathematical_result_unchanged: true
frozen_result_sha256: deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd
exit 0
```

Direct source introspection printed all sixteen `CornerData` fields and
confirmed `has_exact_pair=False`, `has_fibre=False`,
`has_face_root=False`, and `has_ring_map=False`.

## 9. Dependencies and frozen snapshot

Observed repository HEAD: `418e413593120d19e15e6546eb50c985f4b1f038`.
The shared campaign worktree was concurrently dirty; this producer did not
edit any canonical file.

### Canonical snapshot read

```text
6fb539c679083c7d5de1ecba0ba2f6ac272f8fbf0e65c4d2c6ed049056482fe2  COORDINATION.md
1ff57e1f8a632f33d3558c924dadf26bdd1d389797d48be43515b88718a2e725  ladder/REDUCTION.md
9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c  ladder/TRANSPORT.md
11561125758a9cbf4afae30f2479114df96635acbc69e9444d47a2326a12ab0d  AUDIT.md
64fda6612ef813f86701618af4886af84e8a6c6f53638c8a856dbd26527d4919  APPROACHES.md
eab83c1fe9b5bc8d2ee5ac62f47958d6d0372c7a53e6389dd1a9988ae1889414  notes.md
f4964e2fdfef7b3081a3effb0f54eb2cac0f52d34a7c1118ef329ddefc2090d2  ladder/SIGRAY-AUDIT.md
```

### Primary and source artifacts

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
1394871719df5a9ae7726268c1ad760af3bc89e7f8e707af550e6155e9114d88  lib/FAMILIES.md
729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e  lib/families.py
845d42a2d410234f889d5d846f22f7152354896c67ab3d49152469260e892c0d  tests/test_families.py
```

GGV5 Theorem 2.20 and its fourteen clauses were checked against the pinned
official primary version:
`https://arxiv.org/html/1708.07936v1`.  In particular, item 8 explicitly has
`l_(i+1)=lcm(rho_i,l_i)`, one selected root `lambda`, and the translation
`Y -> Y+lambda X^(sigma_i/rho_i)`.

### Prior and frozen packet work

```text
5751fdacd00351b84c4fc14f7203eeca1265bda78f24099441230ed04056fb5b  xmodel/sol-landing1.md
9122478627e6fa904633bb007cee0aa5e487f18f023f1d95b4817bc799b7c56d  xmodel/sol-wtc1-round2.md
dd09069baeeaaa38644963571f929077af016cbbac664aaea9f3f50bee8f6d90  xmodel/sol-h5a.md
3b8bd5c9e2a1f4132cff4353e0e7e0fd9b4426cbeea0b0c13d092161018f5d2f  xmodel/grok-h5a-review.md
7647f2f118d4fe9fdd060b9e3e9450b58a62e287a80e942cad6de752a3f34ae8  xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-sol-20260827.md
5c3d5005d5adaa0ab27cd507dea3a6d55affd78499cddf4ceeac999a77efafd4  xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-r1-adjudication-sol-20260827.md
8f20bc6b42eb26a7185c8d806a9108f35e80f3c0548ddbb75a9d5de681592bce  xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-r1-followup-review-grok-20260827.md
7c1205ff3247e06c31729c22a65c39b1e5bf3bd99e28d5fe6a7780ab3ac315b5  cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify_r1.py
deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd  cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/RESULT.json
```

History/deduplication result: `xmodel/sol-landing1.md` already isolated the
two-chart all-root residual forest and named pole-skeleton capture as the
minimal global lemma.  This report does **not** rename that idea as new.  Its
increment is the explicit ring-level interface (1.1)--(3.6), the
sorted-component `H=Q` issue for `8_28`, the separation between GGV Kummer
denominators and corrected Q/jump/max labels, and the resulting exact
three-arrow composition audit.

## 10. Scope firewall and rollback

- This report proves no `G2-PSC`, `G2-BD`, GGV family exclusion, degree
  ceiling, counterexample, or JC2 result.
- The `8_28` collision is non-Keller.  It proves ambient ledger
  insufficiency only, not insufficiency on the hypothetical Keller locus.
- Theorem 2.1 is a constructor from the whole exact pair, not evidence that
  the GGV ledger determines a tree.
- Proposition 3.1 is conditional on an exact compatible branch evaluation;
  it proves one deck-stable flag segment, not global coverage.
- All statements exclude the post-Laurent `[P,Q]=X^2` endpoints as Sigray
  source objects.
- The target uses the reviewed Q/jump/max and Sigray audit corrections.  A
  change to that perimeter rolls back only the affected label formulas, not
  the source-ring type failure or the ambient `8_28` collision.
- If hostile review finds a sign/orientation error in (3.5)--(3.6), roll back
  only the displayed local residual identification and repair it through
  the explicit isomorphism (1.1).  The all-root/two-chart/coverage
  obstruction remains.
- No canonical file, frozen artifact, or `jc2-lean` file was edited.  No
  heavy local computation was run.

## 11. Operational conclusion

Use the following status vocabulary going forward:

```text
exact pair + fibre -> corrected decorated pole tree      PROVED/CONSTRUCTOR
certified exact GGV occurrence -> one decorated flag     PROVED/LOCAL
CornerData -> decorated pole tree                        NOT TYPED / AMBIENTLY NONFUNCTIONAL
primary one-chain witness -> full pole skeleton          NOT PROVED / WRONG SOURCE SHAPE
GGV all-root two-chart forest -> full pole tree           PROVED CONDITIONAL ON FOREST
GGV source theory produces that complete forest           G2-PSC, OPEN
```

New work can consume a provisionally certified local flag immediately while
coverage is reviewed in the background, but every such descendant must
carry the occurrence ID, pair/fibre reference, chart, and rollback tag.  No
local PASS should be promoted as a global GGV-to-book landing theorem.
