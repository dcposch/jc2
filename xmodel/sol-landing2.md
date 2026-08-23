# Marked-jet landing: precise target, exact finite-window ranks, and the missing bounded-delay lemma

**Date:** 2026-08-23  
**Inputs:** `xmodel/sol-landing1.md`, `xmodel/grok-belyi-review.md`
Claim 3, `REDUCTION.md` G2/T8--T10, `TRANSPORT.md`,
`xmodel/sol-belyi.md`, and the banked residue-A depth records cited below.  
**Status convention:** **EXACT** means a formal consequence of the stated
definitions or an exact calculation over characteristic zero / the two
registered primes. New tower-to-Hurwitz assertions are labelled
**CONJECTURE**.

## 0. Verdict

The proposed theorem has a precise formulation, but its ordinary-Hurwitz
version is not merely unproved: it has the wrong target for faithfulness.

1. The gauge-quotiented tangent space of the fixed
   \(A_4\) passport at
   
   \[
   \beta(u)=\frac{u(u-2/3)^3}{(u^2-u+1/6)^2}
   \]
   
   is zero. Hence every genuine fixed-passport landing has zero
   differential after gauge. It can control the tower only if a separate
   theorem says that no non-gauge tower information can remain invisible
   for more than a uniformly bounded number of levels.
2. A uniform **rank** bound on the kernel would not cap depth. The needed
   condition is a uniform **bounded-delay/fiber** statement: a compatible
   tower chain may contain at most \(B\) successive non-gauge states with
   the same marked Hurwitz jet. Since the rigid Hurwitz jet is constant,
   that condition would give the desired depth cap.
3. `SHEET6-DEPTH.md` supplies the opposite kind of result. Its invariant
   \(w\) makes the reachable jump menu finite, but the unbounded \(l=0\)
   direction fixes \(w\). At residue A, \(w=2\), \(W(2)=\{2\}\), and
   arbitrarily long \(M=1\) tails have the same menu. Thus \(w\) bounds the
   **image** of the state map and explicitly does not bound its fibers or
   segment depth.
4. Absolute Belyi rigidity (one \(S_4\)-orbit) does not make the tower
   landing finite-to-one. On each banked D25 radical fiber the scheme is
   \(16\) disjoint copies of \(\mathbb A^{14}\), while the leading Belyi
   point is fixed. The naive leading-cover landing therefore has
   14-dimensional tangent kernel on every cell at both primes.
5. On the isolated six-tail rung-36 block, the banked row has rank \(1\)
   and kernel rank \(5\) at both primes. The complete two-coefficient first
   variation of \(g^2-f^3\) has rank \(2\) and kernel rank \(4\). Neither is
   the marked Hurwitz differential. The requested kernel rank of an
   *actual marked-jet map* is therefore presently undefined; no such map is
   constructed in the repository.

The landing theorem is **NOT IN REACH from the current data**. The single
minimal local lemma is a bounded-delay marked residual-quotient
factorization lemma, stated in Section 6. It must construct the four marked
branch jets from the D-series, prove the two passport equations, and prove
bounded-delay separation of non-gauge tower extensions.

There is also a scope correction. This local residue-A lemma would not by
itself close the remaining GGV-to-tree part of G2. `sol-landing1.md`
isolated that independent global statement as **CONJECTURE PSC**, the
surjectivity/fidelity of the complete GGV packet forest onto every Sigray
pole path. The logically correct route is

\[
 \text{GGV packets}
 \xrightarrow{\mathrm{PSC}}
 \text{decorated Sigray pole skeleton}
 \longrightarrow
 \text{residue-A D-series}
 \xrightarrow{\mathrm{BMRQ}}
 \text{marked tetrahedral jet}.
\]

Calling the first and last arrows the same theorem suppresses a real change
of domain and quantifier. A consolidated theorem may contain both, but the
present files prove neither implication from the other.

---

## 1. The two depth variables and the source object

Two notions called “depth” must be separated.

- \(d_{\rm sh}\) is the number of characteristic/chain vertices in the
  Sigray \(M=1\) segment. `SHEET6-DEPTH.md` concerns this depth.
- \(D\) is the D-series coefficient truncation: D21 uses rows
  \(0,\ldots,20\), D23 adds rows \(21,22\), and D25 adds rows \(23,24\). The D43 program
  adjoins later coefficient windows and rung graph equations.

Let \(\mathcal X_D\) denote the intended residue-A, B-frozen, no-log,
`PIN42`, \(W_1W_2\ne0\) D-truncation scheme, including every tower,
Jacobian, and reconstruction graph equation whose first occurrence is below
\(D\). Let

\[
 \pi_{D',D}:\mathcal X_{D'}\longrightarrow\mathcal X_D
 \qquad(D'\ge D)
 \tag{1.1}
\]

be coefficient truncation. This definition uses the **intended
graph-preserving** object. It does not identify it with the later D43
compatibility-only ideal, which `SHEET6-DIRECTIONB.md` Section 10.7 proved
to be an overapproximation.

At D25 the banked triangular certificate gives, **EXACT at each registered
prime and within its chart scope**,

\[
 \mathcal X_{25,\omega}
   \cong \coprod_{j=1}^{16}\mathbb A^{14}_{\mathbf F_p}
 \tag{1.2}
\]

for every parked radical fiber \(\omega\). The 36-fiber union is therefore
\(576\) copies of \(\mathbb A^{14}\). In particular every cell is smooth
and has tangent dimension \(14\).

The D25 result is modular and chart-local. It is not a characteristic-zero
existence theorem and does not assert that a D25 point prolongs to D43 or to
an inverse-limit formal germ.

---

## 2. The Hurwitz target

### 2.1 Mark space and passport equations

After target normalization to branch values \(0,1,\infty\) and source
normalization putting the triple point over \(1\) at source infinity, write

\[
 A(u)=(u-r)(u-b)^3,\qquad
 C(u)=(u-a)^2(u-c)^2.
 \tag{2.1}
\]

The open marked Hurwitz scheme \(\mathcal H^{\rm raw}\) is the locus of
distinct marks satisfying

\[
\begin{aligned}
 E_3&=2a-3b+2c-r=0,\\
 E_2&=-a^2-4ac+3b^2+3br-c^2=0.
\end{aligned}
\tag{2.2}
\]

These equations say \(\deg(A-C)\le1\), equivalently triple contact with
\(1\) at infinity. The tetrahedral point is

\[
 x_\beta=(r,b,a,c)=
 \left(0,\frac23,
 \frac12+\frac{\sqrt3}{6},
 \frac12-\frac{\sqrt3}{6}\right).
 \tag{2.3}
\]

Its raw tangent matrix, in the order \((r,b,a,c)\), is

\[
 J_H=
 \begin{pmatrix}
 -1&-3&2&2\\
 2&4&-3+\sqrt3/3&-3-\sqrt3/3
 \end{pmatrix}.
 \tag{2.4}
\]

It has rank \(2\). Its kernel is precisely the residual affine source
gauge, spanned by translation and scaling:

\[
 (1,1,1,1),\qquad
 \left(0,\frac23,a,c\right).
 \tag{2.5}
\]

After the gauges \(r=0\), \(a+c=1\), the determinant is
\(-2\sqrt3\ne0\). Thus

\[
 T_{[\beta]}\mathcal H
 :=\ker J_H/T_{x_\beta}(\operatorname{Aff}_1)=0.
 \tag{2.6}
\]

This is the infinitesimal form of the one-absolute-\(S_4\)-orbit rigidity.
It also shows why “landing into the Hurwitz tangent” must be phrased with
care: the target after gauge is the zero vector space.

### 2.2 The residual quotient whose marks would have to be extracted

At the residue-A merge, put \(t=\eta^3\) and

\[
 P(t)=(t-a_1)(t-a_2).
\]

The exact leading patterns in `SHEET6-TEMPLATE.md` give

\[
 p_f=S_MP^2,\qquad
 p_{h_1}=H_M\eta P^2(t-b),\qquad H_M^3=s_1S_M^4.
\]

Consequently the normalized residual quotient is

\[
 \operatorname{res}_{G_m}
 \left(\frac{h_1^3}{s_1f^4}\right)
 =\frac{t(t-b)^3}{P(t)^2}=\beta(t/\sigma)
 \tag{2.7}
\]

after the scale \(t=\sigma u\). Formula (2.7) is the exact leading Belyi
identity. A marked-jet theorem must do much more: from a finite D-series
truncation it must cancel the common carriers, form (2.7) to positive
transverse order, and Hensel-extract four labelled jets

\[
 r(z),\ b(z),\ a(z),\ c(z)
 \tag{2.8}
\]

with the prescribed multiplicities. No current D25/D43 artifact performs
this operation.

---

## 3. Precise marked-jet landing statement

Let \(R=\mathbf Z[1/S,\sqrt3]\) invert all denominators, discriminants, and
chart units used by the residue-A construction. Let
\(\widehat{\mathcal H}_{\beta}^{(q)}\) be the \(q\)-jet scheme of the
marked fixed-passport Hurwitz scheme at \(\beta\), with the affine source
gauge removed. Since (2.3) is an étale isolated point,

\[
 \widehat{\mathcal H}_{\beta}^{(q)}=\{\beta\},\qquad
 T\widehat{\mathcal H}_{\beta}^{(q)}=0
 \tag{3.1}
\]

over characteristic zero and every good specialization.

The desired statement can now be made without using “kernel” ambiguously.

> **CONJECTURE MJL (marked-jet landing with bounded delay).** There exist
> explicit integers \(D_0,q,B\) and compatible morphisms, modulo tower and
> affine-source gauge,
> 
> \[
>  \Phi_D:\mathcal X_D\longrightarrow
>       \widehat{\mathcal H}_{\beta}^{(q)}
>       \qquad(D\ge D_0),
>  \tag{3.2}
> \]
> 
> such that:
> 
> 1. **Marked extraction.** \(\Phi_D\) is obtained from the actual residual
>    quotient \(h_1^3/(s_1f^4)\), after exact removal of every common
>    carrier, and returns the four labelled Hensel factors (2.8). It is
>    compatible with \(\pi_{D',D}\), deck action, pole swap, and the two
>    infinity charts.
> 2. **Passport landing.** The extracted marks satisfy both equations
>    \(E_3=E_2=0\) through the asserted jet order. Thus (3.2) lands in the
>    fixed \(A_4\) passport, not merely in the ambient four-mark space.
> 3. **Bounded-delay faithfulness.** Along any compatible non-gauge tower
>    chain, at most \(B\) consecutive nontrivial tower states have the same
>    marked Hurwitz jet. Equivalently, every block of \(B+1\) genuinely new
>    tower levels is separated by the extracted marked jet.
> 4. **Arithmetic constancy.** The construction is defined over \(R\), and
>    all factorization and differential ranks used in 1--3 are constant at
>    the two registered good primes and at the characteristic-zero generic
>    point.

Clause 3 is the depth-capping meaning of “faithful with uniformly bounded
kernel.” Because (3.1) makes every passport-preserving marked jet equal to
\(\beta\), a tower chain past the landing level can have at most \(B\)
further non-gauge states. Thus

\[
 d_{\rm sh}\le d_{\rm landing}+B.
 \tag{3.3}
\]

By contrast, a statement such as

\[
 \dim\ker(d\Phi_D)\le K
 \tag{3.4}
\]

does **not** imply (3.3). The constant inverse system
\(\mathbb A^1\leftarrow\mathbb A^1\leftarrow\cdots\), mapped to one rigid
point, has kernel dimension \(1\) at every level and infinite depth. Even
infinitesimal injectivity of each vertical truncation would give uniqueness
of a lift, not nonexistence of a unique infinite lift. The set-theoretic
bounded-delay clause is therefore load-bearing.

There is a second useful linear diagnostic. Put

\[
 N_{D,B}(x)=
 \frac{\ker(d\pi_{D,D-B}:T_x\mathcal X_D\to T_{x_{D-B}}\mathcal X_{D-B})}
      {\text{vertical gauge}}.
 \tag{3.5}
\]

MJL would force \(N_{D,B}(x)=0\) once the marked target is gauge-quotiented.
Failure of this test disproves a proposed value of \(B\), but passing it
would still not replace the stronger fiber statement in Clause 3.

---

## 4. Attack I: neither \(w\) nor Belyi rigidity supplies Clause 3

### 4.1 The \(w\)-invariant has deliberately unbounded fibers

For an \(M=1\) segment,

\[
 w_F=\frac{\bar\kappa_F-\rho_F}{\nu_F},\qquad
 w_{F'}=w_F\frac{n}{(n-1)\nu+1}.
 \tag{4.1}
\]

When \(n=1\), the unbounded \(l=0\) direction, (4.1) gives
\(w_{F'}=w_F\) for every admissible \(\nu\). Resonant steps contract \(w\)
and yield a finite closure, so the jump menu stabilizes. But the theorem
expressly states that segment depth itself is not bounded.

At residue A,

\[
 (\rho,\nu,\bar\kappa)=(1,2,5),\qquad w_0=2,
 \qquad W(2)=\{2\}.
 \tag{4.2}
\]

There is no resonant step because its divisor
\(\Delta=(n-1)\nu+1\ge3\) would have to divide \(2\). The reachable
single-segment frames include the infinite family

\[
 (w,\nu,\bar\kappa)=(2,\nu,2\nu+2),\qquad \nu\ge2,
 \tag{4.3}
\]

and all yield the same residue-A first-jump menu. The exact checker was
rerun: all 13 checks pass; the cumulative menu is constant through the
tested depths and its cap-free proof is the arithmetic of (4.1)--(4.3).

Therefore:

\[
 \boxed{w\text{ gives finite image/menu, not finite fibers/depth}.}
 \tag{4.4}
\]

Any proof of MJL Clause 3 must use coefficient transport, global
polynomial-origin constraints, or Jacobian graph equations absent from the
\(w\)-state. `SHEET6-DEPTH.md` cannot be repurposed into the required kernel
bound.

### 4.2 One \(S_4\)-orbit does not imply a finite-to-one source map

Absolute rigidity says that the target \(\mathcal H\) has one geometric
point in the marked absolute Nielsen class. It says nothing about the fiber
of an unconstructed map \(\mathcal X_D\to\mathcal H\). A constant morphism
from an arbitrary positive-dimensional scheme to that point is compatible
with rigidity.

D25 makes this objection concrete rather than philosophical. On a fixed
radical fiber, all \(16\) cells in (1.2) carry the same B-frozen leading
tetrahedral quotient, while each cell is \(\mathbb A^{14}\). Thus the naive
leading-cover map is constant with a 14-dimensional tangent kernel. Belyi
rigidity does not turn it into a finite map.

The same issue persists set-theoretically: a rigid cover can have infinitely
many choices of a removed common divisor, Puiseux tail, \(B\)-side or
\(x\)-side completion, and Jacobian graph data. Those choices are not
objects in the Hurwitz moduli problem.

---

## 5. Attack II: exact rung-36/D25 ranks at both primes

All ranks in this section were recomputed by exact modular row reduction.
The square roots used by the bank are

\[
\begin{array}{c|c|c|c}
p&\sqrt3&a=1/2+\sqrt3/6&c=1/2-\sqrt3/6\\ \hline
105337&795&133&105205\\
105673&14686&90509&15165
\end{array}
\tag{5.1}
\]

and \((\sqrt3)^2=3\pmod p\) in both rows.

### 5.1 Hurwitz tangent

Reduction of (2.4) has rank \(2\) at both primes. The two gauge vectors
have rank \(2\), are killed by \(J_H\), and the gauge-fixed \(4\times4\)
matrix has rank \(4\). Hence

\[
 \dim T_{[\beta]}\mathcal H=0
 \tag{5.2}
\]

at both primes, exactly as in characteristic zero.

### 5.2 What the rung-36 row actually measures

Order the six level-48 carrier variables as

\[
 v=(F_1,F_2,G_1,G_2,H_1,H_2)
   =(tf1,tf2,tg1,tg2,tg01,tg02)_{48}.
\]

The banked row is

\[
 \lambda_p(v)=
 c_1(F_1+F_2)+c_2\{2(G_1+G_2)+H_1+H_2\}.
 \tag{5.3}
\]

Its exact data are

\[
\begin{array}{c|c|c|c|c}
p&c_1&c_2&c_1+3c_2&
 (\operatorname{rank}\lambda_p,\dim\ker\lambda_p)\\ \hline
105337&48635&54013&0&(1,5)\\
105673&50809&18288&0&(1,5)
\end{array}
\tag{5.4}
\]

Up to a nonzero scalar it is the characteristic-zero row

\[
 -3(F_1+F_2)+2(G_1+G_2)+(H_1+H_2)=0.
 \tag{5.5}
\]

This is one coefficient of the first variation of the upstream
common-power cancellation. Put

\[
 R_i=-3F_i+2G_i+H_i.
\]

For \(q_1=u-a,q_2=u-c\), the complete residual linear polynomial is

\[
 R_1q_2+R_2q_1.
 \tag{5.6}
\]

The map from the six carriers to its two coefficients has matrix

\[
 C_{a,c}=
 \begin{pmatrix}
 -3&-3&2&2&1&1\\
 3c&3a&-2c&-2a&-c&-a
 \end{pmatrix}.
 \tag{5.7}
\]

Since \(a-c=\sqrt3/3\ne0\),

\[
 \operatorname{rank}C_{a,c}=2,\qquad
 \dim\ker C_{a,c}=4
 \tag{5.8}
\]

at both primes. Rung 36 retains only the first row and loses one
pole-weighted anti-trace coefficient. For example

\[
 v=(1,-1,0,0,0,0)
 \]

is killed by (5.3), while the second coefficient in (5.7) is
\(-\sqrt3\), namely \(104542\) and \(90987\) at the two primes. This is an
exact measurement of the rung's extra kernel direction.

Matrix (5.7) is still **not** the Hurwitz Jacobian (2.4). Its variables move
three coincident upstream carriers over each pole; they do not give the
four labelled motions \((dr,db,da,dc)\). In particular, no exact dictionary

\[
 d\mathfrak m_D:
 (F_1,F_2,G_1,G_2,H_1,H_2,\ldots)
 \longrightarrow (dr,db,da,dc)
 \tag{5.9}
\]

has been constructed. Consequently neither the rank-1 row nor the rank-2
common-power map is the requested marked-jet landing.

### 5.3 The D25 kernel

On every D25 \(\mathbb A^{14}\) cell the leading Belyi point is fixed, so
the naive map to the ordinary gauge-quotiented Hurwitz tangent is

\[
 \mathbf F_p^{14}\longrightarrow 0.
 \tag{5.10}
\]

It has rank \(0\) and kernel rank \(14\) at both primes. This is exact for
the leading-cover landing. It is not a computation of (5.9), which is
undefined.

The six level-48 variables cancel from the D25 Schur residuals and first
appear later. On the isolated rung-36 six-variable slice, with the D25
point and all other tails fixed, (5.4) leaves a five-dimensional affine
kernel. It would be incorrect to add \(14+5\) and call the result the
tangent dimension of the graph-preserving D43 family: other rung graph
equations couple the lower and higher variables, and that family remains
unresolved. The only honest rank summary is

\[
\begin{array}{l|c|c|c}
\text{exact map at each prime}&\text{source dim}&\text{rank}&\text{kernel dim}\\ \hline
\text{D25 leading-cover landing}&14&0&14\\
\text{rung-36 trace functional}&6&1&5\\
\text{full common-power coefficient map }C_{a,c}&6&2&4\\
\text{actual marked-jet map }d\mathfrak m_D&\text{--}&\text{--}&\text{undefined}
\end{array}
\tag{5.11}
\]

### 5.4 Characteristic-zero leverage

The Belyi identity (2.7), \(J_H\), and the rational rung vector
\(3:-2:-1\) are characteristic-zero identities. They certify the leading
cover and explain one modular row. They do not certify the D25 or D43
families in characteristic zero. That would require an integral model with
constant specialization rank, or a direct characteristic-zero replay of
the relevant graph-preserving constructor. Agreement at two primes is not
such a theorem.

---

## 6. The single minimal local lemma

The information gap is not another rank computation. It is the absence of
the map whose rank one would compute.

> **CONJECTURE BMRQ (bounded-delay marked residual quotient).** There are
> explicit \(D_0,q,B\) such that every graph-preserving residue-A tower
> truncation through \(D+B\) determines, functorially and over
> \(\mathbf Z[1/S,\sqrt3]\), a normalized factorization
> 
> \[
>  \left[\frac{h_1^3}{s_1f^4}\right]_{q}
>  =
>  \frac{(u-r(z))(u-b(z))^3}
>       {(u-a(z))^2(u-c(z))^2}\pmod {z^{q+1}},
>  \tag{6.1}
> \]
> 
> after exact cancellation of all common carriers, with distinct labelled
> factors and gauges \(r=0,\ a+c=1\), such that:
> 
> 1. the two coefficients \(E_3,E_2\) vanish modulo \(z^{q+1}\); and
> 2. two compatible non-gauge tower states with the same factorization
>    (6.1) cannot remain distinct for more than \(B\) successive sheet
>    levels.

BMRQ is exactly MJL's missing local content. Once the correct residual
quotient is supplied, ordinary Hensel theory separates the four coprime
*clusters* because their centers are distinct and the pole discriminant is
nonzero. It does not prove that the lifted degree-\(3\) and degree-\(2\)
clusters remain pure powers; that multiplicity/purity assertion is part of
BMRQ. The other new content is that the D-series supplies the quotient after
all carrier cancellations, supplies *both* passport rows, and has uniformly
bounded invisible delay.

The rung-36 row supplies only the trace coefficient of the preceding
\(g^2-f^3\) cancellation. The absent pole-weighted coefficient in (5.7) is
the first concrete missing datum, but adjoining it would still not prove
BMRQ: one must then descend through \(h_1^3/f^4\), extract \(r,b,a,c\), and
prove the bounded-delay clause.

No present theorem implies BMRQ:

- \(w\)-closure forgets coefficient tails and permits arbitrary \(l=0\)
  delay;
- absolute Nielsen rigidity describes only the target point;
- D25 has 14-dimensional constant-leading-cover fibers;
- rung 36 has a five-dimensional trace kernel and is one collapse upstream;
- the graph-preserving D43 prolongation family is unresolved; and
- the approximate-root packet record of `sol-landing1.md` lacks the full
  residual all-root data unless strengthened, while PSC remains unproved.

---

## 7. Final disposition

The strongest exact conclusion is negative but decisive:

\[
\boxed{
 T_{[\beta]}\mathcal H=0,
 \quad \ker(D25\to T\mathcal H)=14,
 \quad \ker(\lambda_{36})=5,
 \quad \ker(C_{a,c})=4
}
\]

at both registered primes, with the last two kernels living in the
six-carrier block and not in the Hurwitz tangent complex.

Thus the current tower does not faithfully land in the tetrahedral Hurwitz
tangent space. `SHEET6-DEPTH` cannot repair this because it proves menu
stability while preserving an unbounded invisible direction; Belyi rigidity
cannot repair it because rigidity of the target gives no control on fibers
of the source map.

The #1 local target should be BMRQ, not another isolated left-kernel row.
But the campaign-level statement must retain the independent PSC arrow:
BMRQ could bound or kill the residue-A tower **after it has been reached**;
PSC is still what would prove that the GGV packet forest reaches every
Sigray pole path in the first place. Only their composition would provide
the advertised simultaneous leverage on G2, the book ladder, and residue-A
depth.
