# Hostile audit of `TRANSPORT.md` Conjecture A: transpose equivariance

**Producer/reviewer:** Sol Ultra, desk-scale theorem audit  
**Date:** 2026-08-27  
**Target:** `ladder/TRANSPORT.md` Conjecture A and the proposed second-source
repair of the typed `G2-PSC` interface  
**Primary sources:** GGV5, arXiv:1708.07936v1, Theorem 2.20; VGG,
arXiv:1401.1784v3, Propositions 5.17--5.18, including (5.9)

## 0. Verdict

There are two different claims here, and the audit separates them.

1. **`TRANSPORT.md` Conjecture A itself is a clausewise PASS.**  There is an
   exact signed-transpose conjugation from the x-fraction category
   `K[X^{+-1/l},Y]` to the y-fraction category `K[y^{+-1/l},x]`.  With the
   y-native direction order and endpoint names transported, every one of
   GGV5 Theorem 2.20's fourteen clauses and every clause of VGG Propositions
   5.17--5.18 is the image of its x-native counterpart.  VGG (5.9) is
   invariant.  No theorem clause is non-equivariant.

2. **The stronger campaign inference, “therefore this supplies the other
   infinity chart of the same fixed pair,” is a FAIL before Theorem 2.20.**
   The guaranteed y-run on the signed-transposed pair is exactly the original
   x-run written in new coordinates.  It is not a second branch run.  To see
   the other chart of the fixed pair one needs a y-run on the *untransposed*
   pair (equivalently an x-run on the transposed pair).  That object is not a
   y-`(m,n)`-pair under the printed standard-orientation hypothesis.  For a
   standard base corner `(a,b)` with `a<b`, its y-local corner is `(b,a)` and
   the defining sign is `b-a>0`, whereas Definition 4.3 requires it to be
   negative.

If the request's “separately conjugated second source run” means an abstract
run on the conjugated pair, it is theorem-equivalent and passes.  If it means
the independently needed run on the other chart of the same pair, it does
not exist by this argument.  The first failed application is the
**standard-`(m,n)`-pair input**, exposed first inside Theorem 2.20 at
**clause (3)**; clause (6)'s initial-corner assertion then also has no source.
This is an input/object-identity failure, not a non-equivariant algebraic
clause.

For live `8_28`, Conjecture A may therefore be promoted at the recoverable
ledger/admissibility layer, but the second-chart part of `G2-PSC` remains
open.  The next `H-TRUNC` check can be run as a sign/interface regression on
the explicit non-Keller prototype, where it passes at the first cut, but the
coefficient-free live `CornerData` cannot certify it for a hypothetical
Keller realization.

## 1. The exact conjugation

Keep the printed source variables capitalized and write

\[
 L_X^{(l)}=K[X^{1/l},X^{-1/l},Y],\qquad
 L_y^{(l)}=K[y^{1/l},y^{-1/l},x].
\]

Use the same determinant-one signed rotation as `TRANSPORT.md`:

\[
 \tau_l:L_X^{(l)}\longrightarrow L_y^{(l)},\qquad
 \tau_l(X^{1/l})=y^{1/l},\qquad \tau_l(Y)=-x.
 \tag{1.1}
\]

The maps commute with all Kummer inclusions.  Their inverses send
`y^(1/l)` to `X^(1/l)` and `x` to `-Y`.  For polynomials,

\[
 (\tau F)(x,y)=F(y,-x).
\]

The signed choice is useful rather than cosmetic: the chain rule gives

\[
 [\tau F,\tau G]_{x,y}=\tau([F,G]_{X,Y}),
 \tag{1.2}
\]

whereas the unsigned swap changes the bracket sign.  Either preserves the
property “bracket in `K^*`”; (1.1) also preserves the actual constant.

Let

\[
 T(r,s)=(s,r).
\]

Termwise,

\[
 X^{i/l}Y^j\longmapsto (-1)^j x^j y^{i/l}.
 \tag{1.3}
\]

Hence, in global `(x,y)` exponent coordinates,

\[
 \operatorname{Supp}(\tau F)=T\operatorname{Supp}(F),\qquad
 v_{Tw}(\tau F)=v_w(F),\qquad
 \ell_{Tw}(\tau F)=\tau(\ell_w(F)).
 \tag{1.4}
\]

This is the same support/weight map proved in `TRANSPORT.md` (4.1)--(4.2).

### 1.1 The endpoint convention that makes the theorem equivariant

The transpose reverses orientation on the exponent lattice.  With the
ordinary global x-oriented endpoint convention,

\[
 \operatorname{st}^{\rm glob}_{Tw}(\tau F)=T\operatorname{en}_{w}(F),
 \qquad
 \operatorname{en}^{\rm glob}_{Tw}(\tau F)=T\operatorname{st}_{w}(F).
 \tag{1.5}
\]

A native y-fraction theory uses local coordinates `(y,-x)`: the first local
coordinate is the Laurent one and the second is polynomial.  Therefore its
endpoint names in global coordinates must be

\[
 \begin{aligned}
 \operatorname{en}^{y}_{Tw}(\tau F)&:=T\operatorname{en}_{w}(F)
   =\operatorname{st}^{\rm glob}_{Tw}(\tau F),\\
 \operatorname{st}^{y}_{Tw}(\tau F)&:=T\operatorname{st}_{w}(F)
   =\operatorname{en}^{\rm glob}_{Tw}(\tau F).
 \end{aligned}
 \tag{1.6}
\]

Likewise put `I_y:=T(I_X)` and transport the order:

\[
 Tw_1 <_y Tw_2\quad\Longleftrightarrow\quad w_1<_Xw_2.
 \tag{1.7}
\]

In the ordinary global circular order, `T` reverses order.  Thus a y-native
predecessor is a global successor:

\[
 \operatorname{Pred}^{y}_{\tau F}(Tw)
   =T\operatorname{Pred}_{F}(w)
   =\operatorname{Succ}^{\rm glob}_{\tau F}(Tw),
 \tag{1.8}
\]

and conversely for successors.  Equations (1.6)--(1.8) are mandatory.  A
naive convention that transposes the weight but retains the global x-native
`st/en` names would first break Theorem 2.20 at clause (5), before reaching
the familiar clause-(6) starting-corner mismatch.

### 1.2 Corners, local arithmetic, and pair type

An x-native corner `(a/l,b)` is the y-native corner with the same local
record `(a/l,b)_y`; in global exponent coordinates it is

\[
 (a/l,b)_X\longmapsto (b,a/l)_{x,y}.
 \tag{1.9}
\]

Thus the theorem data transport as

\[
 \widehat P_i=\tau P_i,\quad \widehat Q_i=\tau Q_i,\quad
 \widehat A_i=TA_i,\quad \widehat A'_i=TA'_i,\quad
 \widehat w_i=Tw_i,\quad \widehat l_i=l_i.
 \tag{1.10}
\]

Every integer operation on the local corner record -- gcd, divisibility,
`gap(rho,l)`, generated corners, children, final corners and complete-chain
arithmetic -- is literally unchanged.  In global coordinates the x-native
functional `v_01` becomes `v_10`.

For clarity, the conjugated y-`(m,n)`-pair definition is not the old
definition applied blindly in global coordinates.  In local `(y,-x)`
coordinates it is the printed definition verbatim.  In global coordinates
its valuation ratios are `v_11` and `v_01`, its base direction is `(0,1)`,
and the printed local `v_(1,-1)` sign becomes global `v_(-1,1)`.  By
(1.1)--(1.6),

\[
 (P,Q)\text{ x-standard}\quad\Longleftrightarrow\quad
 (\tau P,\tau Q)\text{ y-standard}.
 \tag{1.11}
\]

Regular corners and their types I.a, I.b, II.a, II.b and III also transport
verbatim: brackets, factor counts and local sign tests are preserved.

## 2. Successor automorphisms and residual variables

At an x-native type-II.b step, GGV/VGG use

\[
 z=X^{-\sigma/\rho}Y,\qquad
 \phi(X^{1/l'})=X^{1/l'},\qquad
 \phi(Y)=Y+\lambda X^{\sigma/\rho},
 \quad l'=\operatorname{lcm}(\rho,l).
 \tag{2.1}
\]

Conjugating gives

\[
 \widehat z=\tau(z)=-y^{-\sigma/\rho}x,
 \tag{2.2}
\]

and

\[
 \psi:=\tau\phi\tau^{-1},\qquad
 \psi(y^{1/l'})=y^{1/l'},\qquad
 \psi(x)=x-\lambda y^{\sigma/\rho}.
 \tag{2.3}
\]

In the local polynomial coordinate `V=-x`, formula (2.3) is exactly
`V -> V + lambda*y^(sigma/rho)`.  Thus the same face polynomial `p(z)`, the
same root `lambda`, the same multiplicity `m_lambda`, and the same Kummer
index occur.  If one chooses the unsigned swap instead, (2.2)--(2.3) lose
the minus signs and the Jacobian constant changes sign; no admissibility
condition changes.

The generated corner formula also conjugates exactly.  In x-local
coordinates it is

\[
 A^{(1)}=\left(\frac{k}{ml},0\right)
       +\frac{m_\lambda}{m}\left(-\frac\sigma\rho,1\right).
\]

In global y-run coordinates this is

\[
 TA^{(1)}=\left(0,\frac{k}{ml}\right)
       +\frac{m_\lambda}{m}\left(1,-\frac\sigma\rho\right).
 \tag{2.4}
\]

## 3. GGV5 Theorem 2.20, all fourteen clauses

The following table uses the transported data (1.10), y-native endpoints
(1.6), and y-native order (1.7).

| clause | conjugated statement | verdict |
|---|---|---|
| (1) | $\widehat l_i=l_i$; the nondecreasing sequence and $l_0=1$ are unchanged. | **PASS** |
| (2) | $\widehat w_0>_y\cdots>_y\widehat w_{j+1}$, where $\widehat w_i=T(w_i)$, because the order itself is transported.  In ordinary global order the display reverses. | **PASS** |
| (3) | $(\widehat P_i,\widehat Q_i)$ is a y-$(m,n)$-pair in $L_y^{(l_i)}$ and $(\widehat P_0,\widehat Q_0)=(\tau P,\tau Q)$, by (1.2) and (1.11). | **PASS** |
| (4) | Apply `tau` to every earlier leading-form equality and use (1.4). | **PASS** |
| (5) | Type II.a is invariant and $m^{-1}\operatorname{st}^y_{\widehat w_h}(\widehat P_i)=T A_{h+1}$.  This is where retaining global `st` would be wrong. | **PASS** |
| (6) | The x base direction $(1,0)$ becomes global $(0,1)$; $\widehat A_0=m^{-1}\operatorname{en}^y_{0,1}(\widehat P)=T A_0$.  All stage corners keep type II. | **PASS** |
| (7) | A type-II.a identity step stays the identity; $\widehat A_{i+1}=\widehat A'_i=m^{-1}\operatorname{st}^y(\widehat P_i)$. | **PASS** |
| (8) | $l_{i+1}=\operatorname{lcm}(\rho_i,l_i)$; in global weight $\widehat w_i=(\sigma_i,\rho_i)$, $\rho_i$ is the coefficient of the fractional y-exponent.  Equations (2.2)--(2.4), root multiplicity and $m\mid m_\lambda$ give the full clause. | **PASS** |
| (9) | Type I is defined by transported bracket/factor/sign predicates, hence the terminal corner remains type I in $L_y^{(l_{j+1})}$. | **PASS** |
| (10) | The child relation is a local-corner arithmetic predicate; applying `T` to the geometric realizations changes none of it. | **PASS** |
| (11) | Local $v_{0,1}$ descent becomes global $v_{1,0}(T A_{i+1})<v_{1,0}(T A_i)$. | **PASS** |
| (12) | Valid edge, generated corner, final corner, child and $l_0=1$ all conjugate, so the y-chain is complete. | **PASS** |
| (13) | The greatest $t$ with $l_t=1$ is unchanged; the full regular-corner set, II.a/II.b types, last-lower-corner label and identity pairs all transport.  “Lower” is y-native; its ordinary global geometric name is different. | **PASS** |
| (14) | $\operatorname{Reg}_y(\widehat P_{j+1},\widehat Q_{j+1})=T\operatorname{Reg}_X(P_{j+1},Q_{j+1})$, with y-native weights/order. | **PASS** |

This is more than a numerical symmetry: given the printed x-source theorem,
apply it to $(\tau^{-1}\widehat P,\tau^{-1}\widehat Q)$ and conjugate its entire witness.  That is a
proof of the y-source theorem.  It does not depend on the campaign software
guard.

## 4. VGG Propositions 5.17 and 5.18

### 4.1 Proposition 5.17 (Case III)

Suppose the x-face is `X^(k/l) mu(z-lambda)^r`.  Under (2.2) the y-local face
is `y^(k/l) mu(zhat-lambda)^r`.  Therefore:

- `rho | l` is unchanged;
- the automorphism is exactly (2.3);
- VGG 5.17(1)'s preserved endpoint and all intermediate leading forms follow
  by applying `tau`; the open interval is read in the transported order;
- (2) is (1.2) plus the conjugated pair definition;
- in (3), `Pred^y=T Pred^X`, which is ordinary global `Succ`, as in (1.8);
- (4) becomes `T(a/l,b)=m^(-1) st^y_(Tw)(psi(tau P))`.

All four clauses pass.  The only easy way to manufacture a failure is to use
ordinary global `Pred` or ordinary global `st` while calling it y-native.

### 4.2 Proposition 5.18 (Case II), including (5.9)

The hypotheses `[ell(P),ell(Q)]=0`, `#factors(p)>1`, `lambda in K^*`, and the
root multiplicity are preserved.  The bound is best written invariantly:

\[
 \frac{m}{l}\frac{a\rho+bl\sigma}{\rho+\sigma}
 =m\frac{v_w(A)}{\rho+\sigma}.
 \tag{4.1}
\]

Since

\[
 v_{Tw}(TA)=v_w(A),\qquad
 (Tw)_1+(Tw)_2=\sigma+\rho,
\]

VGG (5.9) is literally invariant.  Its proof's two sign inequalities are
the y-local images of the originals; globally `v_(1,-1)` and `v_(0,-1)`
become `v_(-1,1)` and `v_(-1,0)`.

The four conclusions then transport as follows:

1. preserved `en^y` and intermediate leading forms;
2. the y-`(m,n)`-pair in `L_y^(l')`;
3. `Tw` is a y-native direction, (2.4) gives `st^y`, and `m | m_lambda`;
4. both regular corners, with the old one type II.a and the new direction
   `Pred^y` (ordinary global `Succ`).

Thus VGG 5.18, including the load-bearing side condition (5.9), passes
without a new hypothesis.

## 5. Why the clausewise pass does not produce the other chart

Write `C_X(P,Q)` for the printed x-native source witness.  The theorem above
constructs

\[
 C_y(\tau P,\tau Q)=\tau C_X(P,Q).
 \tag{5.1}
\]

Equation (5.1) is theorem-equivalent, but it is the *same occurrence* under a
coordinate isomorphism.  It does not construct either of the objects needed
for the other physical axis:

\[
 C_y(P,Q)\qquad\text{or equivalently}\qquad C_X(\tau P,\tau Q).
 \tag{5.2}
\]

The obstruction is already in VGG Definition 4.3.  If the original standard
pair has positive base corner `(a,b)` with `a<b`, then in y-local coordinates
the same pair has corner `(b,a)`.  Its defining local sign is

\[
 v_{1,-1}^{y}(b,a)=b-a>0,
 \tag{5.3}
\]

where an `(m,n)`-pair requires `<0`; the additional standard-pair endpoint
condition fails in the same orientation.  Equivalently, `tau(P,Q)` has global
x-corner `(b,a)` and is not an x-`(m,n)`-pair.  Transposition therefore
permutes the two admissible combinations

```text
x-source on (P,Q)  <----conjugate---->  y-source on tau(P,Q),
```

but neither theorem supplies either cross-combination in (5.2).

This is not the software line `assert a < b`; that line faithfully reflects
the primary-source sign condition.  Nor is it a failure of one of the
fourteen identities.  If one nevertheless tries to feed the fixed pair into
the y-theorem, clauses (1)--(2) are formal bookkeeping and **clause (3) is
the first substantive failure**: `(P_0,Q_0)` is not a y-`(m,n)`-pair.  Clause
(6) then cannot identify a y-source initial regular corner.

Consequently:

- Conjecture A closes native recertification of the transported ledger;
- it does not close the “other chart” clause (4.0) proposed by the Opus5
  review;
- the other chart still needs a theorem for the nonstandard orientation, a
  normalization that demonstrably preserves and glues that physical chart,
  or a pure-Sigray construction from the exact pair.

## 6. The live `8_28` chain

The frozen record is

\[
 A_0=(8,28),\quad A'_0=(1,0),\quad w_0=(4,-1),\quad l_0=1,
 \quad A_1=(11/4,7),\quad (m,n)=(3,2).
\]

Its y-native conjugate has the same local records.  In global coordinates,

\[
 \widehat A_0=(28,8),\quad \widehat A'_0=(0,1),\quad
 \widehat w_0=(-1,4),\quad \widehat A_1=(7,11/4),\quad l_1=4.
 \tag{6.1}
\]

The global ordinary endpoint tuple is reversed relative to the y-native
labels, exactly as `TRANSPORT.md` (4.3)--(4.4) warns.  The successor fixes
`y^(1/4)` and sends

\[
 x\longmapsto x-\lambda y^{-1/4}.
 \tag{6.2}
\]

VGG (5.9) remains the already-reviewed calculation

\[
 3\frac{v_{4,-1}(8,28)}{4-1}
 =3\frac{4}{3}=4,
\]

or, after transpose,

\[
 3\frac{v_{-1,4}(28,8)}{-1+4}=4.
\]

Every face root has `m_lambda=21`, so `21>=4` and `3|21`.  The four roots are
one deck orbit.  Thus the clausewise conjugated chain is fully admissible and
reproduces (6.1); there is no remaining root or (5.9) debt at this edge.

But the same fixed native pair viewed y-locally has corner `(28,8)` and

\[
 28-8=20>0.
\]

That is the explicit input failure for the other chart.  The conjugated
chain (6.1) is the old native x-chain transported to the normalized
y-infinity chart, not a new chain naming the normalized x-infinity chart.
Therefore the live residue remains second-chart source/coverage,
pole-path reachability and gluing, followed by Q/jump/max and tower data.

## 7. Consequence for the next `H-TRUNC` check

`H-TRUNC` is itself conjugation-invariant.  In native variables it asks that
the cumulative sum of selected translations

\[
 \sum_{h<i}\lambda_h X^{\sigma_h/\rho_h}
\]

equal the actual branch truncation strictly below the current height.  Under
`tau`, this becomes the same equality in local `(y,-x)` coordinates; in
global `(x,y)` coordinates the polynomial coordinate and coefficients carry
the minus sign from (1.1).

The explicit non-Keller `8_28` prototype gives a useful exact regression.
For each `zeta^4=1` and `xi^14=1`, its native x-infinity branch begins

\[
 Y=\zeta X^{-1/4}+\frac{\zeta\xi}{4}X^{-9/28}+\cdots.
 \tag{7.1}
\]

Thus the first GGV translation `lambda=zeta` is exactly the strict
truncation before the next exponent `9/28`.  After signed transpose,

\[
 x=-\zeta y^{-1/4}-\frac{\zeta\xi}{4}y^{-9/28}+\cdots,
 \tag{7.2}
\]

and (6.2) is the correct conjugated source-map sign.  This desk-scale
prototype `H-TRUNC` atom passes.

It does **not** certify live `H-TRUNC`: the prototype is explicitly
non-Keller, while live `CornerData` stores neither an exact pair, the root
coefficient, the cumulative source map nor a branch series.  A live proof
must be theorem-level (show every VGG/GGV type-II.b prefix equals the actual
Newton--Puiseux truncation, including type-II.a gaps) or consume a
coefficient-complete exact-pair witness.  Moreover, checking (7.1) concerns
the already covered native-x/conjugated-y chart; it cannot substitute for
the missing other-chart source object diagnosed in Section 5.

## 8. Evidence, reproducibility, and scope

Primary source text was fetched read-only from
`https://arxiv.org/e-print/1708.07936` and
`https://arxiv.org/e-print/1401.1784`, independently extracted, and checked
against the corresponding PDFs.  Relevant source/PDF hashes in the temporary
workspace were:

```text
GGV5 TeX  8f5571e527c4e579b185f7e75dcf48cd6c92fa88c82c46c33019d38ab89d78f5
GGV5 PDF  e04e3bfd88c62346c467ec7c32f5bb236cdcb2ee4796525408c0c8d68632fcdb
VGG TeX   b4908fd596d555c745b3bdce9613e64c056052d7237efc1419d9c24c0e6004d5
VGG PDF   8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60
```

Repository pins read during the audit:

```text
ladder/TRANSPORT.md                                                     9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c
xmodel/g2-psc-typed-source-to-pole-tree-interface-hostile-review-opus5-20260827.md
                                                                         f7de3ae12918c9103d595e81ddc7fcb9082ba950698f70966ade3ea576cc79a1
lib/families.py                                                          729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e
prototype RESULT.json                                                    deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd
```

Checks were theorem-level substitutions, the bracket chain rule, exact
weight/endpoint calculations, a read-only `section4_families()['8_28']`
inspection, and comparison with the already reviewed prototype series.  No
CAS, AWS, or heavy local algebra was used.

This report proves no `G2-PSC`, pole-path surjectivity, landing theorem,
family exclusion, degree ceiling, counterexample or JC2 result.  It does not
repair the Q/jump/max interface or the filed Sigray Proposition 4.2 tower
gap.  It promotes only the abstract y-fraction conjugate of the GGV/VGG
source theorem, while rejecting the inference that this conjugate is an
independent other-chart run on the same selected pair.

Exactly this one report was written.  No canonical ledger or frozen artifact
was edited.  One initial discovery `rg`, launched from the directory above
the repository, used `--glob '!jc2-lean/**'`; because the searched paths then
had a leading `jc2/`, that pattern failed to exclude the child and the output
incidentally included a few matching child-file lines.  None was used in the
audit.  After that discovery call, every search ran from the repository root
with the child excluded.  No child path was directly opened or listed, and
the child was not built, status-inspected or modified.
