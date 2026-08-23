# TRANSPORT.md — the GGV–Sigray normalization transport

**Status (2026-08-17): THEOREM at the pre-Laurent normalization layer.**
The coordinate-cusp obstruction, exact target-degree formula, orbitwise
lexicographic minimality, and signed-axis transport are proved below.  The
machine gate is [cases/transport_check.py](cases/transport_check.py).

**Scope.** Work over \(\mathbf C\).  This document repairs REDUCTION gap G2
for the GGV-selected polynomial standard pair.  It does not turn a GGV
admissible chain into a decorated Eggers–Wall tree, does not apply to the
post-Laurent \([P,Q]=x^j\) objects, and does not repair book coverage or the
absence of an upper bound on topological degree.

## 0. Verdict

There is a lossless two-chart simultaneous normal form.

Let the pre-Laurent GGV pair have a common positive base corner
\(A=(a,b)\), with coprime multipliers \(m,n>1\):

\[
 \operatorname{Supp}P\subseteq[0,ma]\times[0,mb],\qquad
 \operatorname{Supp}Q\subseteq[0,na]\times[0,nb],
\]

and suppose the northeast corners \(mA,nA\) occur.  Put
\(\alpha=\min(m,n)\), \(\beta=\max(m,n)\).  After the determinant-one target
rotation

\[
 C(U,V)=
 \begin{cases}
 (U,V),&m<n,\\
 (V,-U),&n<m,
 \end{cases}
\]

the lower multiplier is first.  The resulting pair is already
lexicographically minimal under every Sigray source/target polynomial
equivalence.  The determinant-one source rotation

\[
 R(x,y)=(y,-x)
\]

then gives a Sigray-normalized representative with corners

\[
 (k_f,l_f)=\alpha(b,a),\qquad
 (k_g,l_g)=\beta(b,a),
\]

and type \((\alpha,\beta)\).  The original GGV polygon and chain ledger are
recovered exactly by the inverse rotations.

A literal one-chart normal form would be the wrong statement: GGV standard
orientation has \(a<b\), whereas Sigray fixes \(l_f\le k_f\).  The signed axis
rotation is therefore part of the theorem, not cosmetic notation.

The load-bearing new fact is the following coordinate-cusp theorem.  It has
a self-contained locally-nilpotent-derivation proof; weighted
Jung–van der Kulk is not an additional dependency.

## 1. The coordinate-cusp theorem

For positive weights \(w=(r,s)\), write

\[
 \deg_w\!\left(\sum a_{ij}U^iV^j\right)
   =\max_{a_{ij}\ne0}(ri+sj)
\]

and let \(\operatorname{in}_w h\) be the part of maximal \(w\)-degree.  A
polynomial \(h\in\mathbf C[U,V]\) is a **coordinate** if it is one component
of a polynomial automorphism.

### Theorem 1.1 (coordinate-cusp exclusion)

Let \(r,s>1\) be coprime and let \(c,d\in\mathbf C^*\).  If \(h\) is a
coordinate, then

\[
 \operatorname{in}_{r,s}h\notin
 \bigl(d^rU^s-c^sV^r\bigr).
 \tag{1.1}
\]

Equivalently,

\[
 \operatorname{in}_{r,s}h(cZ^r,dZ^s)\ne0.
 \tag{1.2}
\]

#### Proof

Choose a coordinate mate \(k\) with \(J(h,k)=\lambda\in\mathbf C^*\), and
set

\[
 \partial=J(h,-).
\]

In the coordinates \((h,k)\), \(\partial=\lambda\,\partial/\partial k\).
Thus \(\partial\) is a locally nilpotent derivation (LND).

Put \(\bar h=\operatorname{in}_{r,s}h\).  The highest filtered homogeneous
part of \(\partial\) is

\[
 D=J(\bar h,-).
\]

This \(D\) is also locally nilpotent.  Here is the filtered argument in the
form needed below.  The derivation \(D\) is homogeneous for the
\((r,s)\)-grading.  If it were not locally nilpotent, some homogeneous
\(q\) would have \(D^j(q)\ne0\) for every \(j\ge0\).  Inductively,
\(D^j(q)\) is then the highest homogeneous part of \(\partial^j(q)\).
Consequently no \(\partial^j(q)\) could vanish, contradicting local
nilpotence of \(\partial\).  Also \(D\ne0\), because \(\bar h\) is
nonconstant in characteristic zero.

For a nonzero element \(q\), define its LND degree

\[
 \delta_D(q)=\max\{j:D^j(q)\ne0\}.
\]

The Leibniz formula in a characteristic-zero domain gives

\[
 \delta_D(q_1q_2)=\delta_D(q_1)+\delta_D(q_2).
 \tag{1.3}
\]

Indeed, if the two degrees are \(e_1,e_2\), the only nonzero term of
\(D^{e_1+e_2}(q_1q_2)\) is
\(\binom{e_1+e_2}{e_1}D^{e_1}q_1D^{e_2}q_2\).  In particular
\(\ker D\) is factorially closed: if a product lies in \(\ker D\), both
factors lie in \(\ker D\).

Assume for contradiction that

\[
 \bar h=Bq,\qquad B=d^rU^s-c^sV^r.
\]

Since \(D(\bar h)=J(\bar h,\bar h)=0\), factorial closure gives
\(B\in\ker D\).  Hence

\[
 s d^rU^{s-1}D(U)=r c^sV^{r-1}D(V).
 \tag{1.4}
\]

Coprimality of the powers of \(U\) and \(V\) in the polynomial ring implies

\[
 V^{r-1}\mid D(U),\qquad U^{s-1}\mid D(V).
 \tag{1.5}
\]

Neither \(D(U)\) nor \(D(V)\) is zero: by (1.4), one vanishes if and only if
the other does, which would give \(D=0\).  Set
\(p=\delta_D(U)\) and \(q_0=\delta_D(V)\).  Since
\(\delta_D(Da)=\delta_D(a)-1\) whenever \(D(a)\ne0\), (1.5) and (1.3) give

\[
 p-1\ge(r-1)q_0,\qquad q_0-1\ge(s-1)p.
\]

Adding and rearranging yields

\[
 (s-2)p+(r-2)q_0\le-2,
\]

which is impossible because \(r,s\ge2\) and \(p,q_0\ge0\).  This proves
(1.1).

Finally, the homomorphism

\[
 \mathbf C[U,V]\longrightarrow\mathbf C[Z],\qquad
 U\longmapsto cZ^r,\quad V\longmapsto dZ^s
\]

has kernel \((B)\).  One way to see this is that \(B\) is the primitive
irreducible binomial for the coprime monomial curve, and both the quotient
and its image \(\mathbf C[Z^r,Z^s]\) are one-dimensional domains.  Thus
(1.1) and (1.2) are equivalent. \(\square\)

### Corollary 1.2 (exact cusp substitution degree)

If \(H\) is a nonconstant homogeneous polynomial of ordinary degree \(D\),
then every coordinate \(h\) satisfies

\[
 \deg h(cH^r,dH^s)=D\deg_{r,s}h.
 \tag{1.6}
\]

#### Proof

If \(e=\deg_{r,s}h\), every term of the top face becomes a scalar multiple
of \(H^e\).  The scalar is nonzero by Theorem 1.1.  Every lower face has
ordinary degree less than \(De\). \(\square\)

## 2. Orbitwise minimality of a rectangular cusp pair

### Theorem 2.1 (exact source/target degree transport)

Let \(1<r<s\) be coprime.  Suppose \(P,Q\in\mathbf C[x,y]\) have, for some
positive integers \(a,b\),

\[
\begin{aligned}
 \operatorname{Supp}P&\subseteq[0,ra]\times[0,rb],
 & [x^{ra}y^{rb}]P&=c\ne0,\\
 \operatorname{Supp}Q&\subseteq[0,sa]\times[0,sb],
 & [x^{sa}y^{sb}]Q&=d\ne0.
\end{aligned}
\tag{2.1}
\]

For a source automorphism \(L=(u,v)\), put

\[
 D_L=a\deg u+b\deg v,qquad H=u_+^av_+^b,
\tag{2.2}
\]

where \(u_+,v_+\) are the top ordinary homogeneous parts.  Then, for every
target coordinate \(h(U,V)\),

\[
 \deg h(P\circ L,Q\circ L)=D_L\deg_{r,s}h.
\tag{2.3}
\]

If \(K=(h_1,h_2)\) is any target automorphism, then

\[
 \bigl(\deg h_1(P\circ L,Q\circ L),
       \deg h_2(P\circ L,Q\circ L)\bigr)
 \ge_{\rm lex}
 \bigl(r(a+b),s(a+b)\bigr).
\tag{2.4}
\]

Consequently, if \((P,Q)\) is a counterexample with its \(r\)-component
first, it is almost normalized in Sigray's source/target equivalence class.

#### Proof

Every source coordinate is nonconstant, so \(\deg u,\deg v\ge1\) and

\[
 D_L\ge a+b.
\tag{2.5}
\]

The northeast monomial in each rectangle is the unique term maximizing the
positive degree functional
\((i,j)\mapsto i\deg u+j\deg v\).  Therefore

\[
 (P\circ L)_+=cH^r,\qquad (Q\circ L)_+=dH^s,
\tag{2.6}
\]

and their degrees are \(rD_L,sD_L\).  For a target polynomial \(h\), only
its maximal \((r,s)\)-face can contribute in ordinary degree
\(D_L\deg_{r,s}h\).  Cancellation at that degree would say

\[
 \operatorname{in}_{r,s}h(cZ^r,dZ^s)=0,
\]

which Theorem 1.1 forbids when \(h\) is a coordinate.  This proves (2.3).

Every nonconstant polynomial has \((r,s)\)-degree at least \(r\), so the
first degree in (2.4) is at least \(rD_L\ge r(a+b)\).  Equality throughout
forces \(D_L=a+b\) and \(\deg_{r,s}h_1=r\).  Since \(r<s\), the latter
identity forces

\[
 h_1=\gamma U+\gamma_0,\qquad \gamma\ne0.
\]

Now \(J(h_1,h_2)=\gamma\,\partial h_2/\partial V\in\mathbf C^*\), so
\(h_2\) has a nonzero term linear in \(V\) and
\(\deg_{r,s}h_2\ge s\).  Formula (2.3) gives the required second-coordinate
bound.  Thus no source/target equivalent representative has a smaller
ordered degree pair. \(\square\)

Two points are worth isolating.

1. The theorem is stronger than global GGV minimality.  It proves minimum
   degree inside this pair's entire Sigray equivalence class directly.
2. Ordinary nondivisibility of \(rD_L,sD_L\) alone would not be enough:
   \(P^s-Q^r\) can cancel.  Theorem 1.1 is exactly what excludes such a
   cancellation in a *coordinate* of a target automorphism.

## 3. The GGV-to-Sigray normalization theorem

### Theorem 3.1 (two-chart simultaneous normal form)

Assume JC2 is false and select the globally minimal standard GGV pair supplied
by the published GGV theorem.  Use the subrectangular conclusion in its exact
form: there are coprime \(m,n>1\), a positive integral base
\(A=(a,b)\) with \(a<b\), proportional support rectangles as in (2.1), and
both northeast corners occur.  Before proceeding, harmlessly scale one target
component so that \([P,Q]=1\); this does not change any support, degree, corner,
minimality, or chain datum used here.

Define \(C\), \(R\), \(\alpha\), and \(\beta\) as in Section 0 and set

\[
 (f,g)=C\circ(P,Q)\circ R.
\tag{3.1}
\]

Then:

1. \((f,g)\) is the same nonautomorphic Keller map up to Sigray
   equivalence, and its topological degree is unchanged;
2. \((f,g)\) is almost normalized;
3. its Newton polygons lie in the rectangles with positive northeast
   corners
   \[
   (k_f,l_f)=\alpha(b,a),\qquad
   (k_g,l_g)=\beta(b,a);
   \]
4. these corners satisfy
   \[
   \frac{k_f}{k_g}=\frac{l_f}{l_g}=\frac\alpha\beta,
   \quad k_f<k_g,\quad l_f<l_g,\quad l_f<k_f,
   \quad \frac{k_g}{k_f}=\frac\beta\alpha\notin\mathbf N;
   \]
5. hence \((f,g)\) is Sigray-normalized of type \((\alpha,\beta)\).

#### Proof

The target map \(C\) is either the identity or the determinant-one rotation
\((U,V)\mapsto(V,-U)\); it sorts the two multipliers without changing the
normalized base polygon.  Theorem 2.1 proves almost-normalized minimality.
The source map \(R(x,y)=(y,-x)\) also has determinant one and preserves total
degrees, so the rotated representative remains almost normalized and keeps
Jacobian one.  On exponents it sends \((i,j)\) to \((j,i)\), giving the two
displayed rectangles.  The five numerical assertions follow from
\(0<a<b\), \(1<\alpha<\beta\), and
\(\gcd(\alpha,\beta)=1\).  They are precisely Sigray's rectangular
normal-form conditions and type definition.  Polynomial automorphisms
preserve the function-field extension and noninvertibility. \(\square\)

For this selected-pair branch, Theorem 3.1 bypasses the Abhyankar inputs used
by Sigray Lemma 2.1: GGV supplies the rectangles, and Theorem 2.1 supplies
lexicographic minimality.  Sigray Notations 2.1–2.4 are used to identify the
resulting object as normalized and to name its type.  Sigray's theorem for an
arbitrary counterexample remains unchanged.

## 4. Exact transport of the GGV ledger

Let \(R^*H=H(y,-x)\), and write

\[
 T(i,j)=(j,i),\qquad T(\rho,\sigma)=(\sigma,\rho).
\tag{4.1}
\]

For every polynomial \(H\), every direction \(w=(\rho,\sigma)\), and every
edge with the usual GGV endpoint convention,

\[
\begin{aligned}
 \operatorname{Supp}(R^*H)&=T\operatorname{Supp}(H),\\
 N(R^*H)&=T N(H),\\
 v_{Tw}(R^*H)&=v_w(H),\\
 \ell_{Tw}(R^*H)&=R^*\ell_w(H),\\
 \operatorname{st}_{Tw}(R^*H)&=T\operatorname{en}_w(H),\\
 \operatorname{en}_{Tw}(R^*H)&=T\operatorname{st}_w(H).
\end{aligned}
\tag{4.2}
\]

The first four identities follow term by term from

\[
 x^iy^j\longmapsto(-1)^j x^jy^i,qquad
 (\sigma,\rho)\mathbin\cdot(j,i)=(\rho,\sigma)\mathbin\cdot(i,j).
\]

The last two reflect the fact that \(T\) reverses orientation on the exponent
lattice.  They can also be checked from GGV's defining inequality
\(w\times(\operatorname{en}-\operatorname{st})>0\).

In the native repo convention an oriented edge stores
\((A_h,A'_h)=(\operatorname{en}_w,\operatorname{st}_w)\).  There are two
closely related tuples after transport, and they must not be conflated.  The
**label-preserving rational ledger** is the involution

\[
 (A_h,A'_h;(\rho_h,\sigma_h))
 \longmapsto
 (TA_h,TA'_h;(\sigma_h,\rho_h)).
\tag{4.3}
\]

The **orientation-preserving endpoint tuple** of the transported leading
face is instead

\[
 (\operatorname{en}_w,\operatorname{st}_w;w)
 \longmapsto
 (T\operatorname{st}_w,T\operatorname{en}_w;Tw)
 =(TA'_h,TA_h;Tw).
\tag{4.4}
\]

Thus (4.3) retains the campaign names while (4.4) retains the GGV
`en`/`st` orientation.  In particular, if
\(w\mathbin\times(A_h-A'_h)>0\), then
\((Tw)\mathbin\times(TA'_h-TA_h)>0\), whereas the pointwise ordered pair in
(4.3) has the opposite cross-product sign.

The GGV5 certificate fraction is unchanged:

\[
 \frac{\rho_h+\sigma_h}{v_{\rho_h,\sigma_h}(A_h)}
 =
 \frac{\sigma_h+\rho_h}{v_{\sigma_h,\rho_h}(TA_h)}.
\tag{4.5}
\]

Accordingly its reduced \((p_h,q_h)\) tag is unchanged.  Target rotation
\(C\) only swaps component labels and scalar signs; the normalized base
corners are unchanged because the two component corners are \(mA_h,nA_h\).
Equations (4.1)–(4.5), together with the component label bit, are an explicit
inverse pair of maps.  No native GGV datum is discarded.

There are two necessary type cautions.

- Transposition reverses cyclic direction order and swaps `st`/`en`.  A
  direction-ordered display must therefore be reindexed.
- A GGV Laurent corner \((a/l,b)\) may transpose to \((b,a/l)\), which is
  not represented by the repo's x-fraction-only `Corner(a,l,b)` class.  The
  Sigray-side object is a rational valuation ledger, not a claim that all
  fourteen GGV5 admissibility clauses have been re-certified in their native
  chart.  Applying \(T^{-1}\) recovers the certified GGV chain exactly.

The Sigray representative is formed at the polynomial starting pair, before
**any** GGV5/GGV22 Laurent operation.  Later rational chain corners are
transported only as stored, exactly recoverable ledger metadata.  In
particular, the final maps involving \(x\mapsto x^{-1}\) are not polynomial
source automorphisms and the Proposition 4.3 endpoints have bracket \(x^2\),
not a nonzero constant.  Those reduced strip polygons are not Sigray inputs.

Finally, (4.2) is not a corner-to-tree functor.  It allows the original GGV
ledger to coexist losslessly with the Eggers–Wall data attached to the
explicit Sigray representative.  It does not say that corner data alone
determine pole status, fiber tags, residual \(g\)-cancellations, or Sigray's
decorations.

## 5. Exact machine instances

Run from the repository root:

```text
python3 cases/transport_check.py
```

The gate reads the live `(8,28)` object from `lib/families.py` and the reviewed
td-7 JSON certificate.  It exits zero and prints `"status": "PASS"`.

### 5.1 Conditional pre-Laurent `(72,108)` family-record transport

This is an exact lattice/support fixture from the live admissible-family
record.  The gate does not construct a polynomial Keller pair realizing the
record, and no such counterexample is known.

The live GGV record is

\[
 A_0=(8,28),\quad A'_0=(1,0),\quad A_{\rm final}=(11/4,7),
\]

\[
 (m,n)=(3,2),\quad (\deg P,\deg Q)=(108,72),\quad
 (\rho,\sigma,p,q)=(4,-1,3,4).
\]

Its recorded base polygon is

\[
 S=\operatorname{conv}\{(0,0),(1,0),(8,28),(0,4)\},
\]

with scaled hull vertices

\[
 3S:\ (0,0),(3,0),(24,84),(0,12),
\]

\[
 2S:\ (0,0),(2,0),(16,56),(0,8).
\]

After the component and source rotations, the Sigray corners are

\[
 (56,16)=2(28,8),\qquad (84,24)=3(28,8),
\]

so the ordered degrees are \((72,108)\) and the type is \((2,3)\).  The
label-preserving chain ledger becomes

\[
 (8,28)\mapsto(28,8),\quad
 (1,0)\mapsto(0,1),\quad
 (11/4,7)\mapsto(7,11/4),
\]

\[
 (4,-1,3,4)\mapsto(-1,4,3,4).
\]

For the first edge, the native ordered endpoints
\((\operatorname{en},\operatorname{st})=((8,28),(1,0))\) become

\[
 (\operatorname{en},\operatorname{st})=((0,1),(28,8)).
\]

The checker verifies orthogonality, the positive cross-product convention
on both oriented endpoint tuples, its sign reversal on the pointwise tuple,
and invariance of the \(p/q=3/4\) certificate.

### 5.2 Residue-A formal-frame control

The residue-A template records

\[
 (k_f,l_f)=(126,42),\quad(k_g,l_g)=(189,63),
 \quad(\deg f,\deg g)=(168,252),
\]

of type \((2,3)\).  Its inverse transported base is

\[
 T^{-1}(126,42)/2=(21,63).
\]

The checker performs the exact round trip

\[
 2(21,63)\mapsto(126,42),\qquad
 3(21,63)\mapsto(189,63),
\]

and verifies the two pole masses

\[
 \Lambda(1,1,2)=\frac{1\cdot1\cdot2\cdot3}{2}=3,
 \qquad 3+3=td=6.
\]

This is an independent **frame-schema control**, not a transport of the
`(8,28)` representative.  Its normalized degree pair \((168,252)\) differs
from \((72,108)\), and its inverse base \((21,63)\) differs from \((8,28)\).

### 5.3 One td-7 formal-configuration control

For the reviewed `(9,15,7,3)@mu0=2` direct certificate, the root record gives

\[
 (k_f,l_f)=(203490,67830),\qquad
 (k_g,l_g)=(305235,101745),
\]

again of type \((2,3)\).  The inverse transported base is

\[
 (33915,101745).
\]

The gate checks this round trip and the unique td-7 entry

\[
 (a,b,\nu)=(1,1,2)\oplus(1,2,3),\qquad M=(1,2),
\]

\[
 \Lambda_1=3,\qquad \Lambda_2=4,
 \qquad \Lambda_1+\Lambda_2=7.
\]

This is also an independent frame-schema control.  The filed cell is
tower-obstructed, not a realized polynomial counterexample, and its formal
normalized degree pair \((271320,406980)\) differs from \((72,108)\).

The mismatch in Sections 5.2–5.3 is a proved data-level negative, not an
omitted identification: if either formal record were realized as a
Sigray-normalized pair, it could not lie in the `(8,28)` equivalence class,
because the lexicographically minimal degree pair is an invariant of that
class.  The requested checks therefore validate the transport schema and
also fail closed against a false same-representative claim.

## 6. Consequence for `REDUCTION.md` T1–T10

The exact new sequential arrow is

\[
\begin{aligned}
 \mathrm{JC2\ false}
 &\xRightarrow{\mathrm{T2}}
 \text{one selected GGV-minimal standard polynomial pair with its native ledger}
 \\
 &\xRightarrow{\text{Theorems 2.1, 3.1 and (4.1)--(4.5)}}
 \text{an explicit Sigray-normalized representative of the same pair,}\\
 &\hspace{38mm}\text{same }td\text{, with the GGV ledger exactly recoverable.}
\end{aligned}
\tag{6.1}
\]

Thus the following become theorem-level statements.

- **T2 \(\to\) enhanced T4, for the selected pair:** no independent
  re-normalization is needed; the component-sorted pair
  \(C\circ(P,Q)\) is orbitwise lex-minimal, and (3.1) gives its Sigray
  frame.
- **T2 plus native pre-Laurent T3 \(\to\) enhanced T4:** every
  polynomial-native polygon corner, leading face, direction, and endpoint
  is carried by (4.1)–(4.4).  Additional rational GGV5 chain
  corners/directions and \((p_h,q_h)\) tags are retained losslessly as the
  raw/recoverable valuation ledger (4.3)–(4.5), with oriented endpoints
  separately recorded by (4.4).  This is not a claim that Laurent leading
  forms live in the same polynomial chart, nor a claim of native
  transposed-chain admissibility.  The fork drawn in T4 closes at the
  normalization layer.
- **Composition with T5–T7:** the same selected counterexample retains its
  topological degree, so T5 applies and the existing Sigray tree/entry
  constructions of T6–T7 can be attached without discarding the GGV
  ledger.

Nothing else is promoted by this theorem.

| T-link | consequence of this document |
|---|---|
| T1 | unchanged; the literal starting condition remains false |
| T2 | unchanged existential GGV theorem; now has a compatible T4 continuation |
| T3 | existing published/preprint and bounded perimeters unchanged; native data transport is proved only before Laurent cuts |
| T4 | strengthened for the T2-selected pair by Theorem 3.1; arbitrary-pair T4 remains the existing Sigray/Abhyankar theorem |
| T5 | unchanged published lower bound \(td\ge6\) |
| T6 | unchanged conditional sheet/tree perimeter; it now coexists with recoverable GGV data on the same equivalence class |
| T7 | unchanged conditional mass/entry theorem; composable with (6.1) |
| T8 | unchanged local marked-event landing perimeter |
| T9 | unchanged sector-specific enumerations and conditionalities |
| T10 | still **NOT ESTABLISHED** |

In particular, this theorem does not prove full-configuration landing, a
generic off-axis completeness theorem, or an upper bound on \(td\).

## 7. Dependencies and evidence

1. **GGV rectangle/selection input.** Guccione–Guccione–Valqui,
   *On the shape of possible counterexamples to the Jacobian Conjecture*,
   Proposition 4.7, the standardization proposition, and Corollary 5.21;
   see the [arXiv source](https://arxiv.org/abs/1401.1784) and the exact
   campaign statement in [REDUCTION.md](REDUCTION.md) T2–T3.  The GGV
   theorem is existential over all counterexamples.
2. **New algebraic input.** Theorem 1.1 and Theorem 2.1 are proved here.
   They use only elementary facts about a coordinate Hamiltonian LND, with
   the filtered-leading and factorial-closure steps proved in the text.
3. **Sigray nomenclature.** Notations 2.1–2.4 and Lemma 2.1's displayed
   rectangle conditions in [refs/sigray_full.pdf](refs/sigray_full.pdf),
   audited in [SIGRAY-AUDIT.md](SIGRAY-AUDIT.md).  Theorem 3.1 does not use
   Sigray's Abhyankar-based existence proof for the selected GGV pair.
4. **Admissible-chain fixture.** [lib/FAMILIES.md](lib/FAMILIES.md) and
   `lib/families.py`, whose GGV5 completeness scope is bounded exactly as
   recorded in [REDUCTION.md](REDUCTION.md).  This document transports a
   supplied certified chain; it does not enlarge GGV5's enumeration scope.
5. **Instance records.** [SHEET6-TEMPLATE.md](SHEET6-TEMPLATE.md),
   [BOOK-OFFAXIS.md](BOOK-OFFAXIS.md), [TOWER-UNIFORM.md](TOWER-UNIFORM.md),
   [TOWER-9-15.md](TOWER-9-15.md), and
   `cases/towers/t9_15_direct.json`.

The hostile normalization audit is [xmodel/grok-reduction-review.md](xmodel/grok-reduction-review.md);
its G2 diagnosis is the gap repaired here.  The pre-Laurent/post-Laurent
type boundary is recorded in
[SECTION4-AUTOMATION.md](SECTION4-AUTOMATION.md).

## 8. Remaining unproved statements

Everything below is explicitly unproved.

**CONJECTURE T (corner-to-tree functor).**  A fiber-tagged, paired
Newton–Puiseux construction may carry the complete GGV chain to the full
decorated Sigray Eggers–Wall pole tree.  The present theorem does not do so;
the GGV \(P\)-polygon alone does not determine residual \(Q\)-cancellation or
pole status.

**CONJECTURE A (native transposed admissibility).**  After changing from the
x-fraction Laurent convention to the transposed y-fraction convention, all
fourteen GGV5 complete-chain conditions should admit a convention-by-convention
transposed formulation.  Only the exact rational valuation ledger and its
inverse are proved here; native re-certification is not needed for (6.1).

No conjecture identifying residue-A or the td-7 formal record with the
`(8,28)` representative is viable under the normalized degree data: the
machine gate proves those frames are different.
