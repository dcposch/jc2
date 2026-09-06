# Face-level Xu (7.1) audit of the family-C ES leaves

**Lane:** `xu71-es-leaves-sol56-20260906`  
**Disposition:** **36 leaves, not 38; 0 face deaths; 36 offset-one OPENs; family-C residual 20 rows / 36 necessary ES leaves.**

The full leading face ODE was checked over exact `Q` on every charged leaf and has
a polynomial solution on every declared face chart.  The proposed next row cannot
be instantiated from the charged inputs: Xu prints only leading coefficients and
the roster stores only the split order and multiplicity partition.  In particular,
the absence of the three next coefficients is not an identity-zero computation.
No leaf is typed `ES_LEAF_DEAD_BY_XU71`, and no leaf is typed
`OPEN[XU71-PLUS-ONE-VACUOUS]`.

## 0. Custody, scope, and terminology

The receipt's numbered `_basename` / `_sha256` fields were converted mechanically
with `awk` to `/tmp/jc2-xu71-manifest.sha256`; `sha256sum -c` returned `OK` for all
eight frozen files.  The charged roster hash is
`cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf`.
Before writing, `df -h /` reported 2.8 GB free.  The only lane artifacts are the
small driver and JSON named in section 8; no CAS dump or artifact tree was made.
No ledger was edited, no `jc2-lean` was used, and no `ideation-*` input was read.

Throughout this report:

* `rho` or \(\rho\) is a leaf's first split order.  It maps to
  `split_window.leaves[].rho`, **not** to the unrelated roster array
  `source.delta`.
* \(\lambda=(\lambda_i)\) is the roster's root-multiplicity partition of
  \(\deg p=u\).  It is not Moh's scalar `lambda_s` used to compute \(\mu_s\).
* \(t\) is Xu's Puiseux coordinate, fixed by \(x=t^{-1}\).  The split-screen
  number \((\rho-1)/(v-u\rho)\) is renamed \(\theta\), never `t`.
* A surviving leaf is still an `ES_NECESSARY_LEAF_NOT_ATTAINMENT`.  Nothing here
  promotes a face, place, carrier, or polynomial pair.

## 1. The one-line reducer: 36 is authoritative

The requested reducer is:

```bash
jq -s '[.[] | select(.split_window.applies == true) |
  .split_window.leaves[]? |
  select(.type == "ES_NECESSARY_LEAF_NOT_ATTAINMENT")] | length' \
  /tmp/jc2-lane.lw2JIQ/inputs/roster.jsonl
```

It prints `36`.  Four independent roster checks agree: there are 20 rows with
`split_window.applies == true`; these are exactly the 20 rows with `source.u_s >=
2`; the sum of the 20 declared `leaf_count` values is 36; and the sum of the
actual array lengths is 36.  Regenerating all 20 rows through the frozen
`split_window.py` reproduces every `(rho, lambda, Q, theta, kappa)` tuple and all
36 survivors.  Every row also satisfies
`raw_pair_count = killed_count + leaf_count`.

The charged structural report prices 38 at
`residual65-structure-fable5-20260905.md:47-48,120-125,252-253,282-287`, but no
reducer on the current charged schema yields 38.  `galois_zero_choices` are
witness choices, not additional leaves, and the row's D2 alternative is not an
ES leaf.  The current charged roster therefore decides the operative count:

```text
OPEN[ROSTER-ES-LEAF-COUNT-36-VS-38]
decision = 36
reason   = 36 typed leaf objects in the current charged roster; 38 is stale text
```

The three requested controls are aliases of existing records, not extra charges:
`D=108, delta=3` is `R012-L01`; `(99,66), delta=2` and `delta=5/2` are
`R015-L01` and `R015-L02`.  Here user `D` maps to `source.n` and user `delta`
maps to leaf `rho`.

## 2. Xu's coordinates and the declared rings

The frozen source is arXiv:1604.07683v4, dated 15 February 2022.  Although the
task calls it “Xu 2016 p.11,” equation (7.1) is on **printed/PDF p.12** of this
frozen revision.  Xu defines on printed p.1–2

\[
  x=t^{-1},\qquad
  \sigma(t,\pi)=\sum_{j<\rho}a_jt^j+\pi t^\rho,
\]

with \(t,\pi\) independent.  In the explicit section-8, \(\rho=2\) chart
(printed p.12),

\[
  \sigma=a_{-1}t^{-1}+a_0+a_1t+\pi t^2.
\]

The ring map is therefore declared, rather than inferred from matching names:

\[
 \phi_\sigma:K[x,y]\longrightarrow K[\pi]\!\left\langle\!\left\langle
 t\right\rangle\!\right\rangle,quad
 x\mapsto t^{-1},\quad y\mapsto\sigma(t,\pi),
\]

where \(K\) is algebraically closed of characteristic zero and
\(J_{t,\pi}(A,B)=A_tB_\pi-A_\pi B_t\).  For
\(T_s=T_s(f,g)\), the subscript in \((T_s)_f\) is differentiation in the formal
first argument, not differentiation in \(y\).  Moh Proposition 4.1 (printed
p.164/PDF p.25) and the chain rule give Xu (7.1):

\[
 \frac{\partial(T_s(\sigma),g(\sigma))}{\partial(t,\pi)}
   =-J\,(T_s)_f(\sigma)t^{\rho-2}. \tag{7.1}
\]

Xu does **not** introduce a modulus ring or `Zc`.  For the exact-Q leading-face
checks I add the following presentations.  On every one-orbit or two-root chart,

\[
 S=\mathbf Q[c,Z_c]/(Z_cc-1),\qquad S[\pi],
\]

with generator order `(c,Zc,pi)`.  On the three collision-sensitive records
`R043-L02`, `R053-L02`, and `R055-L04`, let \(r\) be the root-ratio modulus and
let the task's localized coordinate \(c\) be its collision product:

\[
 S=\mathbf Q[r,c,Z_c]/(c-r(r-1),\ Z_cc-1),\qquad S[\pi], \tag{2.1}
\]

with generator order `(r,c,Zc,pi)`.  The two face forms are respectively
\(p=\pi(\pi-1)(\pi-r)\) and
\(p=\pi(\pi^2-1)(\pi^2-r)\).  Thus the mandated localizer is literally
`Zc*c-1`, while its image is the complete collision divisor \(r(r-1)\).
Using the root ratio itself as `c` and inverting only it would incorrectly retain
the collision at ratio 1.

All maps are explicit.  The quotient sends
`r -> r`, `c -> r*(r-1)`, `Zc -> (r*(r-1))^-1` in (2.1), and sends
`c -> c`, `Zc -> c^-1` on the other charts.  The coefficient map

\[
 \psi:\mathbf Q[p_0,\ldots,p_u,q_0,\ldots,q_D]\longrightarrow S
\]

sends \(p_i\mapsto[\pi^i]p\) and \(q_j\mapsto[\pi^j]q\) for the displayed
face and witness.  A specialization to \(K[\pi]\) sends the modulus to a value
with nonzero collision product, `c` to that product, `Zc` to its inverse, and
`pi -> pi`.  The JSON prints every generator image.  The driver checks the
images are monic of degrees \(u,D\), obey the Q-Galois coefficient congruence,
invert the collision coordinate, and satisfy (F) exactly.

The other
Q>1 forms follow from the charged covariance
`p_i=0 unless i == u (mod Q)` (`split_window.py:229-278`).  At Q=1 the Galois
action is trivial, so the affine gauges displayed below are additional declared
normalizations.  The partition-level coordinate independence proved at
`split-window-gate-opus5-20260905.md:92-112` does not itself supply an
offset-one jet map.

## 3. The leading face ODE and exact polynomial witnesses

Put

\[
 E=n/d_s,\quad W=(-\mu_s-2)/d_s,\quad X=u\rho-v<0,
 \quad \alpha=WX-1+\rho,\quad D=Wu+1.
\]

The source-consistent leading terms are

\[
 g(\sigma)=a_1p^Et^{EX}+\cdots,\quad
 (T_s)_f(\sigma)=bp^{W+E}t^{(W+E)X}+\cdots,
\]
\[
 T_s(\sigma)=a_sq\,t^\alpha+\cdots,qquad \deg p=u,quad\deg q=D.
\]

Substitution in (7.1), followed by a declared monic normalization of \(p,q\),
gives the charged face equation (`split_window.py:20-28,358-383`):

\[
 \boxed{\alpha q p_\pi-Xp q_\pi-(v-u)p^{W+1}=0.} \tag{F}
\]

The scalar step matters: before monic normalization the right coefficient is
\(-Jb/(a_sa_1E)\); monicity makes it
\(\alpha u-XD=v-u\).  Those leading scalars are not serialized in the compact
roster and must not be reused unannounced at offset one.

Set

\[
 \theta=\frac{\rho-1}{v-u\rho},\qquad \kappa=W-\theta=\alpha/X,
 \qquad d=u\theta+1=-\frac{v-u}{X}.
\]

An integrating factor gives

\[
 (q p^{-\kappa})_\pi=d\,p^\theta,qquad
 q=d\,p^\kappa\int p^\theta\,d\pi. \tag{3.1}
\]

Whenever \(\theta\in\mathbf Z\), this is visibly a monic polynomial of degree
\(Wu+1\).  The driver checks the exact antiderivative in
`Q[c,pi]`; the large power cancels formally.  Every fractional case also
polynomializes on its forced multiplicity/Galois chart.  The four templates are:

| \(p,\theta\) | exact monic \(q\) (an optional polynomial homogeneous solution may exist) |
|---|---|
| \(\pi^r(\pi-c),\ 1/r\) | \(\pi^{rW-1}(\pi-c)^{W+1}(\pi+\frac r{r+1}c)\), \(r=2,3,4\) |
| \((\pi^2-c)^2,\ 3/2\) | \(7(\pi^2-c)^{2W-3}\int(\pi^2-c)^3d\pi\) |
| \(\pi^2(\pi^2-c),\ 3/2\) | \(\pi^{2W-3}(\pi^2-c)^{W+1}(\pi^2+\frac25c)\) |
| \(\pi^2(\pi^3-c),\ 5/2\) | \(\pi^{2W-5}(\pi^3-c)^{W+1}(\pi^3+\frac27c)\) |

For each fractional template the driver reduces (F), using logarithmic
derivatives, to zero in the exact rational-function field `Q(c,pi)`.  Thus all
36 leading ODE checks pass; this is stronger than merely replaying (G)+(L), but
it is still only a necessary face configuration.

### 3.1 Cheapest row first: R012 / D=108, rho=3

Here \((u,v,W,E,X,\alpha,D)=(2,7,25,12,-1,-23,51)\), so

\[
 -23qp_\pi+pq_\pi=5p^{26}.
\]

The cone report's face is \(p=\pi^2-c\) (`cone-vertex-gate...md:171-176`).
An exact monic solution is

\[
 q=(\pi^2-c)^{23}
   \left(\pi^5-\frac{10}{3}c\pi^3+5c^2\pi\right),
\]

and an arbitrary multiple of \((\pi^2-c)^{23}\) may be added.  Hence the
leading row is not a unit for `c != 0`.  Here \(\gamma=(W+E)X=-37\); the raw
offset-one power would be \(t^{\gamma+\rho-1}=t^{-35}\), not bare \(t^2\).

### 3.2 Next cheapest: R015 / (99,66)

At \(\rho=2\),
\((u,v,W,E,X,\alpha,D)=(3,8,13,9,-2,-25,40)\), and

\[
 -25qp_\pi+2pq_\pi=5p^{14}.
\]

With \(p=\pi^2(\pi+3a)\),

\[
 q=\pi^{25}(\pi+3a)^{14}(\pi-2a)
   =p^{12}\,\pi(\pi+3a)^2(\pi-2a),
\]

which reduces exactly to Xu's (8.2) on printed p.13.  This is the demanded
positive control.

At \(\rho=5/2\), \(X=-1/2,\alpha=-5,D=40\), and

\[
 -5qp_\pi+\tfrac12pq_\pi=5p^{14}.
\]

For \(p=\pi(\pi^2-c)\), the monic solution is
\(q=p^{10}(10\int p^3d\pi)\), with a free `p^10` homogeneous term.  Xu writes
the reduced equation as \(q_1'=-2p^3\) and leaves this case open.  The factor
`-2` versus monic `10` is a nonzero leading-scalar normalization, not a ring-map
identity; Xu's printed `dx` in the integral must be `d pi` by his determinant.

## 4. The actual offset-one coefficient

Use the source ring first, without absorbing the leading scalars:

\[
 A=T_s(\sigma)=t^\alpha\sum_{r\ge0}A_r(\pi)t^r,\quad
 B=g(\sigma)=t^\beta\sum_{s\ge0}B_s(\pi)t^s,
\]
\[
 C=(T_s)_f(\sigma)=t^\gamma\sum_{h\ge0}C_h(\pi)t^h,qquad
 \alpha+\beta-1=\gamma+\rho-2.
\]

The supports may be rational.  Exact coefficient extraction from (7.1), with
`J=1`, gives at every offset \(h\)

\[
 F_h=\sum_{r+s=h}\left((\alpha+r)A_r(B_s)_\pi
       -(\beta+s)(A_r)_\pi B_s\right)+C_h=0. \tag{4.1}
\]

Thus the requested offset-one row is the full \(r+s=1\) convolution.  Only if
one separately proves there are no offsets strictly between 0 and 1 does it
reduce to

\[
 (\alpha+1)A_1(B_0)_\pi+\alpha A_0(B_1)_\pi
 -(\beta+1)(A_0)_\pi B_1-\beta(A_1)_\pi B_0+C_1=0. \tag{4.2}
\]

Its raw power is \(t^{\gamma+\rho-1}\).  Calling it the coefficient of bare
\(t^{\rho-1}\) is valid only after first factoring \(t^\gamma\).

This is the stopping point forced by the evidence:

* Xu's generic p.12 displays and all five section-8 displays on printed p.13
  give only \(A_0,B_0,C_0\), each followed by `+ ...`.  Xu prints no
  \(A_1,B_1,C_1\) and no support-gap theorem.
* The compact roster intentionally keeps `rho`, `lambda`, Galois zero choices,
  and the (L) data, but not \(p,q\), leading scalars, arc coefficients, or next
  series coefficients (`split_window.py:413-445`).
* The charged split gate explicitly says (G)+(L) discard the full coefficient
  system (`split-window-gate...md:251-260`).

Consequently (4.1) is not a polynomial in the displayed modulus ring until a
new emitter declares the images of all required \(A_r,B_s,C_1\).  There is no
legal elimination to a unit, a nonzero univariate in `c`, or identity zero.

There is one useful negative control.  If “the 1-jet of the arc” means only
\(\sigma\mapsto\sigma+z t^{\rho+1}\), then
\(\pi\mapsto\pi+zt\) and
\((A_1,B_1,C_1)=z(A_0',B_0',C_0')\).  Substitution gives

\[
 F_1=z\,\partial_\pi F_0=0\pmod{F_0}.
\]

So a pure arc-translation jet is identically vacuous.  That does **not** prove
the actual leaf row vacuous, because the intrinsic next coefficients hidden in
Xu's ellipses have not been shown to equal those translation terms.  The correct
per-leaf type is therefore

```text
OPEN[XU71-PLUS-ONE-ARC-JET-DATA-MISSING]
```

not `OPEN[XU71-PLUS-ONE-VACUOUS]`.  The absent rational-support information is
also recorded as `OPEN[XU71-OFFSET-ONE-SUPPORT]`.

## 5. All 36 family-C leaves

In the table, every leading equation is (F) with the displayed parameters.
`PASS / OPEN*` means: an exact polynomial leading witness passed, while the
actual offset-one row has type
`OPEN[XU71-PLUS-ONE-ARC-JET-DATA-MISSING]`.  The complete coefficient data,
raw offset-one power, declared map, and witness formula for every record are in
the JSON.

| leaf | `(D,m); (u,v,W,E)` | `rho=P/Q; lambda` | `X; alpha; deg q` | normalized `p`; `L(c)` | result |
|---|---|---|---|---|---|
| `R012-L01` | (108,72); (2,7,25,12) | 3=3/1; `[1,1]` | -1; -23; 51 | `pi^2-c`; `c` | PASS / OPEN* |
| `R015-L01` | (99,66); (3,8,13,9) | 2=2/1; `[2,1]` | -2; -25; 40 | `pi^2(pi-c)`; `c` | PASS / OPEN* |
| `R015-L02` | (99,66); (3,8,13,9) | 5/2=5/2; `[1,1,1]` | -1/2; -5; 40 | `pi(pi^2-c)`; `c` | PASS / OPEN* |
| `R016-L01` | (168,112); (2,5,99,24) | 2=2/1; `[1,1]` | -1; -98; 199 | `pi^2-c`; `c` | PASS / OPEN* |
| `R023-L01` | (165,110); (2,9,41,15) | 4=4/1; `[1,1]` | -1; -38; 83 | `pi^2-c`; `c` | PASS / OPEN* |
| `R024-L01` | (165,110); (2,9,41,15) | 4=4/1; `[1,1]` | -1; -38; 83 | `pi^2-c`; `c` | PASS / OPEN* |
| `R029-L01` | (168,112); (3,5,67,21) | 3/2=3/2; `[1,1,1]` | -1/2; -33; 202 | `pi(pi^2-c)`; `c` | PASS / OPEN* |
| `R035-L01` | (144,108); (2,7,89,16) | 3=3/1; `[1,1]` | -1; -87; 179 | `pi^2-c`; `c` | PASS / OPEN* |
| `R038-L01` | (135,90); (4,11,13,9) | 2=2/1; `[3,1]` | -3; -38; 53 | `pi^3(pi-c)`; `c` | PASS / OPEN* |
| `R038-L02` | (135,90); (4,11,13,9) | 5/2=5/2; `[2,2]` | -1; -23/2; 53 | `(pi^2-c)^2`; `c` | PASS / OPEN* |
| `R038-L03` | (135,90); (4,11,13,9) | 5/2=5/2; `[2,1,1]` | -1; -23/2; 53 | `pi^2(pi^2-c)`; `c` | PASS / OPEN* |
| `R038-L04` | (135,90); (4,11,13,9) | 8/3=8/3; `[1,1,1,1]` | -1/3; -8/3; 53 | `pi(pi^3-c)`; `c` | PASS / OPEN* |
| `R043-L01` | (168,112); (3,11,25,12) | 3=3/1; `[2,1]` | -2; -48; 76 | `pi^2(pi-c)`; `c` | PASS / OPEN* |
| `R043-L02` | (168,112); (3,11,25,12) | 3=3/1; `[1,1,1]` | -2; -48; 76 | `pi(pi-1)(pi-r)`; `c=r(r-1)` | PASS / OPEN* |
| `R043-L03` | (168,112); (3,11,25,12) | 7/2=7/2; `[1,1,1]` | -1/2; -10; 76 | `pi(pi^2-c)`; `c` | PASS / OPEN* |
| `R044-L01` | (147,42); (2,5,49,21) | 2=2/1; `[1,1]` | -1; -48; 99 | `pi^2-c`; `c` | PASS / OPEN* |
| `R045-L01` | (147,63); (2,5,103,21) | 2=2/1; `[1,1]` | -1; -102; 207 | `pi^2-c`; `c` | PASS / OPEN* |
| `R049-L01` | (189,126); (2,7,67,21) | 3=3/1; `[1,1]` | -1; -65; 135 | `pi^2-c`; `c` | PASS / OPEN* |
| `R051-L01` | (180,144); (2,7,185,20) | 3=3/1; `[1,1]` | -1; -183; 371 | `pi^2-c`; `c` | PASS / OPEN* |
| `R052-L01` | (165,99); (3,8,67,15) | 2=2/1; `[2,1]` | -2; -133; 202 | `pi^2(pi-c)`; `c` | PASS / OPEN* |
| `R052-L02` | (165,99); (3,8,67,15) | 5/2=5/2; `[1,1,1]` | -1/2; -32; 202 | `pi(pi^2-c)`; `c` | PASS / OPEN* |
| `R053-L01` | (200,150); (3,7,137,20) | 2=2/1; `[2,1]` | -1; -136; 412 | `pi^2(pi-c)`; `c` | PASS / OPEN* |
| `R053-L02` | (200,150); (3,7,137,20) | 2=2/1; `[1,1,1]` | -1; -136; 412 | `pi(pi-1)(pi-r)`; `c=r(r-1)` | PASS / OPEN* |
| `R054-L01` | (175,70); (2,5,83,25) | 2=2/1; `[1,1]` | -1; -82; 167 | `pi^2-c`; `c` | PASS / OPEN* |
| `R055-L01` | (171,114); (5,14,13,9) | 2=2/1; `[4,1]` | -4; -51; 66 | `pi^4(pi-c)`; `c` | PASS / OPEN* |
| `R055-L02` | (171,114); (5,14,13,9) | 5/2=5/2; `[3,1,1]` | -3/2; -18; 66 | `pi^3(pi^2-c)`; `c` | PASS / OPEN* |
| `R055-L03` | (171,114); (5,14,13,9) | 5/2=5/2; `[2,2,1]` | -3/2; -18; 66 | `pi(pi^2-c)^2`; `c` | PASS / OPEN* |
| `R055-L04` | (171,114); (5,14,13,9) | 5/2=5/2; `[1,1,1,1,1]` | -3/2; -18; 66 | `pi(pi^2-1)(pi^2-r)`; `c=r(r-1)` | PASS / OPEN* |
| `R055-L05` | (171,114); (5,14,13,9) | 8/3=8/3; `[2,1,1,1]` | -2/3; -7; 66 | `pi^2(pi^3-c)`; `c` | PASS / OPEN* |
| `R055-L06` | (171,114); (5,14,13,9) | 11/4=11/4; `[1,1,1,1,1]` | -1/4; -3/2; 66 | `pi(pi^4-c)`; `c` | PASS / OPEN* |
| `R062-L01` | (180,135); (4,11,49,12) | 2=2/1; `[3,1]` | -3; -146; 197 | `pi^3(pi-c)`; `c` | PASS / OPEN* |
| `R062-L02` | (180,135); (4,11,49,12) | 5/2=5/2; `[2,2]` | -1; -95/2; 197 | `(pi^2-c)^2`; `c` | PASS / OPEN* |
| `R062-L03` | (180,135); (4,11,49,12) | 5/2=5/2; `[2,1,1]` | -1; -95/2; 197 | `pi^2(pi^2-c)`; `c` | PASS / OPEN* |
| `R062-L04` | (180,135); (4,11,49,12) | 8/3=8/3; `[1,1,1,1]` | -1/3; -44/3; 197 | `pi(pi^3-c)`; `c` | PASS / OPEN* |
| `R065-L01` | (180,120); (3,9,29,15) | 5/2=5/2; `[1,1,1]` | -3/2; -42; 88 | `pi(pi^2-c)`; `c` | PASS / OPEN* |
| `R066-L01` | (162,108); (2,7,53,18) | 3=3/1; `[1,1]` | -1; -51; 107 | `pi^2-c`; `c` | PASS / OPEN* |

## 6. The three named cone faces after the roster sweep

These checks do not add three records to 36.

* **D=108, rho=3:** the charged cone report supplies only
  `K3(sigma)=-t^8(pi^2-c)+O(t^9)` and the derived leading `K2` target
  `(pi^2-c)^4` (`cone-vertex-gate...md:171-176`).  It supports the R012 leading
  representative and leaves exactly the `O(t^9)` coefficient unknown.
* **(99,66), rho=2:** its `K3` face is
  `zeta^2(zeta+3*varrho)` (`...md:200-208`), which maps to Xu's
  \(p=\pi^2(\pi+3a)\).  Equation (8.2) is reproduced exactly.
* **(99,66), rho=5/2:** its `K3` face is
  `-zeta(c-zeta^2)` at the corresponding tau chart, the same
  \(\pi(\pi^2-c)\) shape.  Xu himself leaves this leading case open.

The cone report mentions `jet1,jet2` but declares no map from them to
\(A_1,B_1,C_1\) (`...md:113-115,182-190,250-259`).  Its exact cancellation is a
different statement, `J(F,G)=0` on a degenerate band-chart subspace
(`...md:49-96`); its `J=1` exclusion occurs at the global depth discussed at
`...md:240-273`.  Historical units are explicitly missing-target artifacts on
the old engines (`...md:275-303`).  None may be imported as the missing Xu
offset-one row.  All three named faces therefore retain the same OPEN as their
roster records.

## 7. Verdict and FALLACY-v2 audit

```text
authoritative family-C rows                         20
authoritative typed ES leaves                       36
full leading face ODE polynomial witnesses          36 PASS
ES_LEAF_DEAD_BY_XU71                                 0
nonzero modulus conditions with only localized c=0   0
actual OPEN[XU71-PLUS-ONE-VACUOUS] leaves             0
OPEN[XU71-PLUS-ONE-ARC-JET-DATA-MISSING]             36
rows whose every ES leaf died                         0
family-C row residual                                20
family-C necessary ES-leaf residual                  36
D2 alternatives retained                             20
overall charged residual after this lane             65 (unchanged)
```

Thus there are no “descent-only prefixes” created by this lane: every one of the
20 rows retains at least one ES necessary leaf as well as its D2 alternative.
The 20 are necessary prefix configurations, not pairs.  The 36 leaf records are
not added to the 20 D2 alternatives as though they were attained objects.

FALLACY-v2 checks:

* **Necessary versus sufficient / floor versus attainment:** a leading ODE
  witness proves only that this necessary face is nonempty; it proves no lift or
  Keller pair.  No floor is reported as attained.
* **Variable/ring map:** section 2 declares the source map, coefficient field,
  generator order, affine/Galois gauges, and both collision localizers.  The two
  places where `Zc*c-1` is insufficient are not hidden.
* **Raw remainder / zero:** the exact tests branch between integral and
  fractional \(\theta\), prove polynomiality, and test zero in the declared
  rational-function field.  No `sat()` wrapper is used.
* **Prime labels:** every prime in (F), (4.1), and (4.2) means
  \(\partial/\partial\pi\); roster/child primes are not used.
* **Identical vanishing:** only the explicitly restricted arc-translation
  control vanishes.  It is not promoted to a verdict on the unknown intrinsic
  jet.
* **Flag/place/series and charging:** no exit set or new exit-price assertion is
  made, so no `charge_basis=` line applies.

Open records carried by this lane are:

```text
OPEN[ROSTER-ES-LEAF-COUNT-36-VS-38]
OPEN[XU71-PLUS-ONE-ARC-JET-DATA-MISSING]
OPEN[XU71-OFFSET-ONE-SUPPORT]
OPEN[XU71-FACE-GAUGE-LOCALIZER-MAP]
```

The last item means that a future offset-one kill must prove equivariance across
the roster's unchosen zero-root/affine charts.  The leading charts, generator
images, specializations, and collision divisors in this report are already
declared and checked.

## 8. Reproduction artifacts

```text
box/xu71-leaves-20260906/xu71_leaves.py
box/xu71-leaves-20260906/xu71-leaves.json
```

Run:

```bash
python3 box/xu71-leaves-20260906/xu71_leaves.py
```

The driver re-hashes all eight charged inputs, regenerates the roster leaves via
the frozen screen, checks every rational identity and coefficient-map image,
verifies integral cases in the declared polynomial charts, checks fractional
cases by exact logarithmic normal form in the corresponding fraction fields,
and refuses to label the missing offset-one row as a unit or zero.
The JSON is under 1 MB and contains all 36 expanded records.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21238`.
- Body SHA-256:
  `47fc4a963e99428214f14d8e64105add03c769217960c73a939ba1a7fbedab8b`.
- Frozen basis: `ed41ab403503f96ca603ab5711a0783d734b2180`.
