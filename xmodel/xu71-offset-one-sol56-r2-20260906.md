# Xu (7.1) offset-one audit of the family-C ES leaves

**Lane:** `xu71-offset-one-sol56-r2-20260906`  
**Verdict:** **20 family-C rows / 36 typed ES leaves; 0 proven DEAD, all
36 retained with a residual system, and no free-jet row is identically zero.**

The source does determine the relative-offset-one coefficient of the Jacobian
identity as a formal convolution.  It does **not** determine the Puiseux supports
or the intrinsic next coefficients occurring in that convolution.  After the
leading face is normalized, the missing next coefficient of
\((T_s)_f(\sigma)\) occurs with the nonzero coefficient
\(-E(v-u)\).  Hence the **free-jet relaxation** is triangular and proper for
every leaf and every allowed face modulus.  Per the charge, each leaf therefore
"survives with residual system" rather than dying.  This is not proof that the
completed, realized offset scheme is proper: the absent support and
realization/compatibility ideal remains OPEN, and no polynomial pair, physical
place, or attainment is produced.

## 0. Custody, disk discipline, and scope

The numbered `charged_input_<i>_basename` and `_sha256` fields of
`xmodel/xu71-offset-one-sol56-r2-20260906.run.v2` were paired mechanically by
`awk` and piped directly to `sha256sum -c`.  All six frozen paths returned
`OK`, with hashes:

```text
c76be040e115dc3fab84098eef218d157948afe8717318fd2cc6f20e1aa576b9  xu71-es-leaves-sol56-20260906.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  roster.jsonl
be99effafff67501f20c80d5e0366162091c3fe1c0fcd3b6672896cd3db9aedd  split_window.py
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

Initial `df -h /` showed 2.0 GB free.  All PDF extraction, symbolic trials, and
Singular runs were done on worker `172.30.0.163`, which had 23 GB free, under
`/home/ubuntu/jc2/box/xu71-offset-one-20260906` with
`TMPDIR=/home/ubuntu/jc2/box/xu71-offset-one-20260906/tmp`.  No CAS scratch or
log was pulled to the host.  The only new host outputs are this report and the
92,445-byte JSON.  Immediately before the JSON pull, `df -h /` showed 11 GB
free.  No ledger was edited, `jc2-lean` was not used, and no exit-price claim is
made.

One exploratory delegate accidentally surfaced a few matches from a prohibited
uncharged `ideation-*` path.  It was stopped immediately; none of its content or
conclusions is used here.  A replacement audit was restricted to the six exact
frozen paths and independently reproduced the derivation and verdict below.

The authoritative reducer remains 36, not the stale count 38.  There are 20
roster objects with `split_window.applies=true`, and their typed leaf arrays
contain 36 objects.  The charge's `D=108` means roster `source.n=108`; below it
is called \(N\), since \(D_q=Wu+1=51\) is the degree of the face polynomial
\(q\).  Roster `source.delta` is tower data and is never identified with leaf
split order \(\rho\).

## 1. What the sources actually say

Moh Proposition 4.1, printed p.164 (PDF p.25), takes
\(x=t^{-1}\), a generic point
\(\sigma=\sum_{j<\delta}a_jt^j+\pi t^\delta\), and
\(h=h(f,g)\).  If

\[
 g(\sigma)=g_0(\pi)t^{\lambda_g}+\cdots,\qquad
 h(\sigma)=h_0(\pi)t^{\lambda_h}+\cdots,
\]

then, with prime meaning \(d/d\pi\),

\[
 J_{t,\pi}(h(\sigma),g(\sigma))=
 (\lambda_hh_0g_0'-\lambda_gh_0'g_0)
 t^{\lambda_h+\lambda_g-1}+\cdots
 =-h_f(\sigma)t^{\delta-2}. \tag{1.1}
\]

The proof is the chain rule and
\(J_{t,\pi}(x,\sigma)=-t^{\delta-2}\).  With a general constant
\(J=J_{x,y}(f,g)\), the last member is \(-J h_f(\sigma)t^{\delta-2}\).
Pages 165--166 use only formal orders and leading coefficients; they emit no
next jet.

Moh Definition 5.1(4) is printed p.179 (PDF p.40), not in Xu: it says that the
unique general point
\(\sigma_i=\sum_{j<\delta_i}a_jt^j+\pi t^{\delta_i}\) of a tower disc
satisfies Proposition 4.6.  It supplies no term after \(\pi t^{\delta_i}\).
Moh already warns on printed p.163 that after a factor \((\pi-b)^l\) selects a
proper smaller disc, the size of that disc is not determined.  Thus an at-level
multiplicity partition is not a next radius or a next Puiseux coefficient.

Xu defines the same \(\pi\)-root on printed pp.1--2.  Proposition 7.3 (p.10),
Corollary 7.5 and its proof (pp.11--12), and all section-8 displays (p.13) give
only leading coefficients followed by ellipses.  Xu (7.1), printed/PDF p.12, is
(1.1) with \(h=T_s\).  There is no Xu Definition 5.1(4); Xu has a Theorem 5.1.

There is a typographical inconsistency in the generic display on Xu p.12.  The
section-8 degrees and exponents, Proposition 7.3, and exponent alignment in
(7.1) force

\[
 E=\frac n{d_s},\qquad W=\frac{-\mu_s-2}{d_s},
\]

so \((T_s)_f\) has the face power \(p^{W+E}\), while
\(\deg q=Wu+1\).  Using \((-\mu_s+n-2)/d_s=W+E\) as the exponent of
\(q\) contradicts Xu's own \((99,66)\) display, where \(W=13\) and
\(\deg q=40\), not 67.

## 2. Full expansion through relative offset one

Declare the source map and determinant orientation:

\[
 \Phi_\sigma:K[x,y]\longrightarrow K[\pi]\!\left\langle\!\left\langle
 t\right\rangle\!\right\rangle,quad
 x\mapsto t^{-1},\quad
 y\mapsto\sum_{j<\rho}a_jt^j+\pi t^\rho,
\]

\[
 J_{t,\pi}(A,B)=A_tB_\pi-A_\pi B_t,qquad
 A=T_s(\sigma),\ B=g(\sigma),\ C=(T_s)_f(\sigma).
\]

The subscript \(f\) is differentiation in the formal first argument of
\(T_s(f,g)\), not differentiation in \(y\).  Allow arbitrary rational Puiseux
supports and write

\[
 A=t^\alpha\sum_{r\ge0}A_r(\pi)t^r,quad
 B=t^\beta \sum_{s\ge0}B_s(\pi)t^s,quad
 C=t^\gamma\sum_{h\ge0}C_h(\pi)t^h,
\]

where \(\alpha+\beta-1=\gamma+\rho-2\).  Direct coefficient extraction from
Xu (7.1) gives, at every relative offset \(h\),

\[
 \boxed{\Phi_h=\sum_{r+s=h}
 \big((\alpha+r)A_rB_s'-(\beta+s)A_r'B_s\big)+J C_h=0.} \tag{2.1}
\]

This is the full source-derived answer.  In particular, the offset-one row is a
convolution over **every** supported pair \(r+s=1\).  If, and only if, a support
gap excludes \(0<r,s<1\), it reduces to

\[
 (\alpha+1)A_1B_0'+\alpha A_0B_1'
 -(\beta+1)A_0'B_1-\beta A_1'B_0+J C_1=0. \tag{2.2}
\]

The frozen source and roster contain no such gap theorem.  Below \(M_1(\pi)\)
denotes the omitted middle convolution in (2.1), not zero.

From here on set \(J=1\), as charged.  For the face normalization put

\[
 X=u\rho-v<0,quad \alpha=WX-1+\rho,quad
 \beta=EX,quad\gamma=(W+E)X,quad K=E(v-u)>0,
\]

and choose monic \(P,q\) with

\[
 A_0=q,\qquad B_0=P^E,\qquad C_0=-K P^{W+E}.
\]

The scalar statement before normalization is
\(Jb/(a_sa_1)=-E(v-u)\); it fixes a ratio, not the three leading scalars
individually.  The leading row is exactly

\[
 F_0=\alpha qP'-XPq'-(v-u)P^{W+1}=0. \tag{2.3}
\]

Normalize the intrinsic next functions as \(R= A_1/a_s\),
\(S=B_1/a_1\), and \(H=C_1/b\).  The honest offset-one residual is

\[
 \boxed{L_1=(\alpha+1)R(P^E)'+\alpha qS'
 -(\beta+1)q'S-\beta R'P^E+M_1-KH=0.} \tag{2.4}
\]

### The arc 1-jet

Definition 5.1(4) does not provide a 1-jet.  If one freely appends the common
centre translation \(z t^{\rho+1}\), equivalently
\(\pi\mapsto\pi+zt\), then

\[
 A_1=R+zA_0',\quad B_1=S+zB_0',\quad C_1=b(H+z(P^{W+E})').
\]

Its entire contribution is
\(z\,\partial_\pi[\alpha q(P^E)'-\beta q'P^E-KP^{W+E}]\), which vanishes
modulo the leading face row.  Thus the pure translation direction is vacuous
and \(z\) is free.  The intrinsic row (2.4) is **not** vacuous: setting
\(R=S=M_1=0,H=1\) gives \(-K\ne0\) as a formal polynomial.  Whether the
row becomes redundant after imposing the missing realization ideal is not
decided.

## 3. Determined data versus free data

| input | determined | not determined by that input |
|---|---|---|
| numerical tower `(n,m,M,d,V,delta)` | \(u,v,E,W\), root counts and tower radii | actual discs, centre coefficients, next disc/radius, any coefficient after a disc boundary |
| leaf \(\rho\) | \(X,\alpha,\beta,\gamma,\theta,\kappa,Q\) and face degrees | support sets between offsets 0 and 1; the 1-jet \(z\) |
| partition \(\lambda\) | multiplicities and charged Galois/zero-root alternatives | root positions, chosen affine/Galois gauge, modulus value |
| leading Xu row | ODE (2.3), scalar ratio, allowed leading \(q\) family | individual leading scalars; intrinsic \(R,S,H,M_1\) |
| a full realized `(f,g,T_s,disc)` plus next characteristic data | would determine all composite series compatibly | this realization map and next characteristic data are absent from the roster |

The roster serializes only the necessary tower and leaf data.  In particular,
its `own_child` and `receiver_chart` fields concern the alternative D2 descent;
there is no declared map from those coefficient coordinates to an ES
\((R,S,H,M_1)\) block.  Importing them by matching names would violate the
variable/ring-map guardrail.

The leading face itself can also have a homogeneous integration constant
\(\eta\).  It is polynomial on 28 leaves and must remain free; it is absent on
the eight fractional-\(\kappa\) leaves
`R015-L01,R038-L01,R038-L03,R052-L01,R055-L01,R055-L05,R062-L01,R062-L03`.

## 4. Exact rings, maps, and the small Singular decision

For the 33 ordinary chosen charts use

\[
 S_c=\mathbf Q[c,Z_c,\eta]/(Z_cc-1),
\]

omitting \(\eta\) on the eight leaves just listed.  For the three
collision-sensitive charts `R043-L02`, `R053-L02`, `R055-L04`, use

\[
 S_r=\mathbf Q[r,c,Z_c,\eta]/(c-r(r-1),\ Z_cc-1)
 \simeq\mathbf Q[r,(r(r-1))^{-1},\eta]. \tag{4.1}
\]

The quotient maps are respectively
`c -> c, Zc -> c^-1` and
`r -> r, c -> r(r-1), Zc -> (r(r-1))^-1`.
Thus the mandated localizer is literally `Zc*c-1`; merely inverting the root
ratio \(r\) would retain the collision \(r=1\).  In every case `pi -> pi` as a
polynomial indeterminate.  An identity in \(S[\pi]\) means all of its
\(\pi\)-coefficients vanish; \(\pi\) is not an existential point.

Because the charged data give no finite support emitter, an exact finite
leaf-realization system cannot be formed.  The legal finite check is the
free-jet relaxation of one generic coefficient of (2.4).  For a formal
coefficient \(k\), introduce \(U_k\) as the coefficient of all terms in
\(L_1\) except \(-KH\), and let \(h_k=[\pi^k]H\).  The declared block map is

\[
 \chi_k: \mathbf Q[r,c,Z_c,U_k,h_k,z,\eta]\longrightarrow
 S[\hbox{jet coefficients}],quad
 U_k\mapsto[\pi^k](L_1+KH),\quad h_k\mapsto[\pi^k]H,
\]

with the face generators mapped as above and `z -> z`, `eta -> eta`.
The block row is \(U_k-Kh_k\).  Missing support and global derivative
compatibility form a separate residual ideal \(I_{\rm realize}\); the frozen
inputs do not define it, so it is not invented.

The worker ran Singular 4.3.2 over exact \(\mathbf Q\), uniform generator order
`(r,c,Zc,U,H,z,eta)`, one universal relaxed block for each of the 36 leaves.
Here `r` is harmless on ordinary charts, and `eta` is harmless on the eight
faces without a polynomial homogeneous term:

```text
ordinary:  I=<Zc*c-1, U-K*H>
collision: I=<c-r*(r-1), Zc*c-1, U-K*H>
```

For every leaf Singular returned `NF(1,I)=1`, so \(I\ne(1)\), and substitution
`H=U/K` reduced the row to zero.  `diff(row,z)=0`; adding `c` to either localized
ideal returned the unit ideal, the negative control for the localizer.  The
ordinary rational point is
\((c,Z_c,U,H,z,\eta)=(1,1,0,0,0,0)\); the collision-chart point is
\((r,c,Z_c,U,H,z,\eta)=(2,2,1/2,0,0,0,0)\).  These are points of the relaxed
row system, not realized Keller pairs.

This computation deliberately asserts no tensor independence between
different \(k\).  The \(U_k\) arise from shared \(R,S,M_1\) data and may obey
unknown support, degree, Galois, and cross-coefficient relations.  Consequently
the printed status `SURVIVES_RESIDUAL` means only "not killed by the declared
free block; retain the leaf with \(I_{\rm realize}\) OPEN."

The common printed certificate suffix is:

```text
ROW_NONZERO=1|NF1=1|OFFSET_IDEAL_UNIT=0|TRIANGULAR_H_SOLVE=1|ARC_Z_FREE=1|C0_NEGCTRL_UNIT=1|STATUS=SURVIVES_RESIDUAL
```

## 5. Named instantiations

### R012-L01: charge `D=108`, \(\rho=3\)

Here \((N,m;u,v,W,E)=(108,72;2,7,25,12)\),
\((X,\alpha,\beta,\gamma,D_q)=(-1,-23,-12,-37,51)\), and \(K=60\).
In \(\mathbf Q[c,Z_c,\eta][\pi]/(Z_cc-1)\), choose

\[
 P=\pi^2-c,qquad
 q=P^{23}\left(\pi^5-\frac{10}{3}c\pi^3+5c^2\pi+\eta\right).
\]

The full relative-offset-one residual, including unknown middle support, is

\[
 -22R(P^{12})'-23qS'+12R'P^{12}+11q'S+M_1-60H=0. \tag{5.1}
\]

Its raw power is \(t^{\gamma+\rho-1}=t^{-35}\), not bare
\(t^{\rho-1}\).  Printed line:

```text
R012-L01|ROW_NONZERO=1|NF1=1|OFFSET_IDEAL_UNIT=0|TRIANGULAR_H_SOLVE=1|ARC_Z_FREE=1|C0_NEGCTRL_UNIT=1|STATUS=SURVIVES_RESIDUAL
```

### R015: charge \((99,66)\)

Both leaves have \((u,v,W,E,K)=(3,8,13,9,45)\).

For `R015-L01`, \(\rho=2\),
\((X,\alpha,\beta,\gamma)=(-2,-25,-18,-44)\), and

\[
 P=\pi^2(\pi-c),\qquad
 q=\pi^{25}(\pi-c)^{14}\left(\pi+\frac23c\right).
\]

The declared map to Xu's p.13 notation is \(c\mapsto-3a\); it sends
\(P\) to \(\pi^2(\pi+3a)\) and the last factor of \(q\) to \(\pi-2a\).
The row and raw power are

\[
 -24R(P^9)'-25qS'+18R'P^9+17q'S+M_1-45H=0,qquad t^{-43}. \tag{5.2}
\]

For `R015-L02`, \(\rho=5/2\),
\((X,\alpha,\beta,\gamma)=(-1/2,-5,-9/2,-11)\), and

\[
 P=\pi(\pi^2-c),\quad
 q=P^{10}\left(\pi^{10}-\frac{15}{4}c\pi^8+5c^2\pi^6
 -\frac52c^3\pi^4+\eta\right).
\]

Its row and raw power are

\[
 -4R(P^9)'-5qS'+\frac92R'P^9+\frac72q'S+M_1-45H=0,
 \qquad t^{-19/2}. \tag{5.3}
\]

Printed lines:

```text
R015-L01|ROW_NONZERO=1|NF1=1|OFFSET_IDEAL_UNIT=0|TRIANGULAR_H_SOLVE=1|ARC_Z_FREE=1|C0_NEGCTRL_UNIT=1|STATUS=SURVIVES_RESIDUAL
R015-L02|ROW_NONZERO=1|NF1=1|OFFSET_IDEAL_UNIT=0|TRIANGULAR_H_SOLVE=1|ARC_Z_FREE=1|C0_NEGCTRL_UNIT=1|STATUS=SURVIVES_RESIDUAL
```

## 6. All 36 per-leaf verdicts

Chart codes are:
`P2=pi^2-c`, `P31=pi^2(pi-c)`, `P32=pi(pi^2-c)`,
`P41=pi^3(pi-c)`, `P42=(pi^2-c)^2`,
`P43=pi^2(pi^2-c)`, `P44=pi(pi^3-c)`,
`P51=pi^4(pi-c)`, `P52=pi^3(pi^2-c)`,
`P53=pi(pi^2-c)^2`, `P54=pi^2(pi^3-c)`,
`P55=pi(pi^4-c)`, `P3r=pi(pi-1)(pi-r)`, and
`P5r=pi(pi^2-1)(pi^2-r)`.  `eta` records whether the leading homogeneous
solution remains polynomial.  Every `S` entry means the leaf-specific printed
line is its ID followed by the common certificate suffix in section 4, with
`S` interpreted only as retained/survives-with-residual in that declared
free-jet model.

| leaf | `rho; lambda` | `(alpha,beta,gamma); K` | raw \(t\)-power | chart; eta | verdict |
|---|---|---:|---:|---|---|
| R012-L01 | `3; 1,1` | `(-23,-12,-37);60` | `-35` | P2; yes | S |
| R015-L01 | `2; 2,1` | `(-25,-18,-44);45` | `-43` | P31; no | S |
| R015-L02 | `5/2; 1,1,1` | `(-5,-9/2,-11);45` | `-19/2` | P32; yes | S |
| R016-L01 | `2; 1,1` | `(-98,-24,-123);72` | `-122` | P2; yes | S |
| R023-L01 | `4; 1,1` | `(-38,-15,-56);105` | `-53` | P2; yes | S |
| R024-L01 | `4; 1,1` | `(-38,-15,-56);105` | `-53` | P2; yes | S |
| R029-L01 | `3/2; 1,1,1` | `(-33,-21/2,-44);42` | `-87/2` | P32; yes | S |
| R035-L01 | `3; 1,1` | `(-87,-16,-105);80` | `-103` | P2; yes | S |
| R038-L01 | `2; 3,1` | `(-38,-27,-66);63` | `-65` | P41; no | S |
| R038-L02 | `5/2; 2,2` | `(-23/2,-9,-22);63` | `-41/2` | P42; yes | S |
| R038-L03 | `5/2; 2,1,1` | `(-23/2,-9,-22);63` | `-41/2` | P43; no | S |
| R038-L04 | `8/3; 1,1,1,1` | `(-8/3,-3,-22/3);63` | `-17/3` | P44; yes | S |
| R043-L01 | `3; 2,1` | `(-48,-24,-74);96` | `-72` | P31; yes | S |
| R043-L02 | `3; 1,1,1` | `(-48,-24,-74);96` | `-72` | P3r; yes | S |
| R043-L03 | `7/2; 1,1,1` | `(-10,-6,-37/2);96` | `-16` | P32; yes | S |
| R044-L01 | `2; 1,1` | `(-48,-21,-70);63` | `-69` | P2; yes | S |
| R045-L01 | `2; 1,1` | `(-102,-21,-124);63` | `-123` | P2; yes | S |
| R049-L01 | `3; 1,1` | `(-65,-21,-88);105` | `-86` | P2; yes | S |
| R051-L01 | `3; 1,1` | `(-183,-20,-205);100` | `-203` | P2; yes | S |
| R052-L01 | `2; 2,1` | `(-133,-30,-164);75` | `-163` | P31; no | S |
| R052-L02 | `5/2; 1,1,1` | `(-32,-15/2,-41);75` | `-79/2` | P32; yes | S |
| R053-L01 | `2; 2,1` | `(-136,-20,-157);80` | `-156` | P31; yes | S |
| R053-L02 | `2; 1,1,1` | `(-136,-20,-157);80` | `-156` | P3r; yes | S |
| R054-L01 | `2; 1,1` | `(-82,-25,-108);75` | `-107` | P2; yes | S |
| R055-L01 | `2; 4,1` | `(-51,-36,-88);81` | `-87` | P51; no | S |
| R055-L02 | `5/2; 3,1,1` | `(-18,-27/2,-33);81` | `-63/2` | P52; yes | S |
| R055-L03 | `5/2; 2,2,1` | `(-18,-27/2,-33);81` | `-63/2` | P53; yes | S |
| R055-L04 | `5/2; 1,1,1,1,1` | `(-18,-27/2,-33);81` | `-63/2` | P5r; yes | S |
| R055-L05 | `8/3; 2,1,1,1` | `(-7,-6,-44/3);81` | `-13` | P54; no | S |
| R055-L06 | `11/4; 1,1,1,1,1` | `(-3/2,-9/4,-11/2);81` | `-15/4` | P55; yes | S |
| R062-L01 | `2; 3,1` | `(-146,-36,-183);84` | `-182` | P41; no | S |
| R062-L02 | `5/2; 2,2` | `(-95/2,-12,-61);84` | `-119/2` | P42; yes | S |
| R062-L03 | `5/2; 2,1,1` | `(-95/2,-12,-61);84` | `-119/2` | P43; no | S |
| R062-L04 | `8/3; 1,1,1,1` | `(-44/3,-4,-61/3);84` | `-56/3` | P44; yes | S |
| R065-L01 | `5/2; 1,1,1` | `(-42,-45/2,-66);90` | `-129/2` | P32; yes | S |
| R066-L01 | `3; 1,1` | `(-51,-18,-71);90` | `-69` | P2; yes | S |

`R023-L01` and `R024-L01` have the same face parameters but distinct charged
towers, so both are retained.  The concrete charts are representatives; the
properness argument itself is gauge-independent because the zero section
\(R=S=M_1=H=0\) works for every leading face and every noncollision modulus.

## 7. Final typed disposition and guardrails

```text
family-C roster rows                                      20
typed ES necessary leaves                                 36
proven ES_LEAF_DEAD_BY_XU71_OFFSET_ONE                     0
RELAXED_OFFSET_BLOCK_PROPER                               36
SURVIVES[XU71_OFFSET_ONE_RESIDUAL] (retained category)    36
formal free-jet rows identically zero                      0
actual full-row redundancy decisions                       0
actual offset statuses still OPEN                         36
actual ES realization ideals instantiated                   0
family-C row residual                                      20
family-C necessary-leaf residual                           36
D2 alternatives retained                                   20
```

The residual attached to every survivor is

```text
OPEN[XU71_OFFSET_ONE_REALIZATION_MAP_MISSING]
OPEN[XU71_OFFSET_ONE_RATIONAL_SUPPORT_UNSERIALIZED]
```

The first asks for the structural ideal relating the composite next
coefficients of \(T_s(f,g)\), \(g\), and \((T_s)_f\) to one actual polynomial
pair and one actual next characteristic level.  The second asks for the
rational support sets needed to turn (2.1) into a finite coefficient list.
Until both are supplied, neither consistency nor redundancy of the completed
actual offset scheme is decided; solving the free row is neither a lift nor an
attainment.  Conversely, a free variable left unconstrained is not a kill.

No `sat()` wrapper is used.  All localizers are equations in declared rings;
the unit and nonunit controls are explicit.  Prime marks mean
\(d/d\pi\).  The face, a physical place, and a cover series are not identified.
No lower bound is promoted to equality.  No new exit-price assertion is made,
so FALLACY-v2 requires no `charge_basis=` line.

## 8. Reproduction artifacts

```text
box/xu71-offset-one-20260906/xu71_offset_one.py
box/xu71-offset-one-20260906/xu71-offset-one.json
```

The driver was already present from the aborted first attempt and was not
edited on the host in this round.  It was copied to the worker and run with an
explicit frozen-input path.  Its SHA-256 is
`54459ce7eab96d14aac26c1a544f2e6f42829af9c3664c5e038133688c8079e7`.
The JSON SHA-256 is
`dccd5865c53f1ce2332a04b066bc9a6246f4037c24072e7c045e5807ba2174fb`.
The final JSON preserves the worker records and all 36 literal Singular lines;
the post-run semantic audit corrected its metadata to use scalar `z`, declare
the `eta` extension of each base face chart, and disclaim cross-coefficient
independence.  It contains the declared maps, leading representatives,
residual row for every leaf, and the exact verdict counts.  It records
`actual_realization_systems_formed=0`, `actual_offset_status_open=36`, and no
cross-coefficient independence, so the relaxed block decision cannot be
misread as a global lift.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20452`.
- Body SHA-256:
  `42ec9031f9161b9fe3fc8206c23e3336f0c4195c401d49ea2dcc3d33589a5f86`.
- Frozen basis: `2193fcad3f78e1dc2af93c80c7c140b9160f7822`.
