# Coefficient gluing for the td-7 off-axis survivors: design and pilot

Status: **DESIGN COMPLETE; IMPLEMENTATION IS GATED ON ROUTE/TOWER PROVENANCE**  
Date: 2026-08-13  
Target implementation: a new additive emitter; this document changes no
promoted theorem and does not run a solver.

## 0. Executive decisions

The requested emitter is buildable for a **concrete, fully decorated route**.
The current `px5` artifacts do not yet contain such routes. Four facts must be
made explicit before implementation.

1. `xmodel/sol-sixcells.md:51-60` proves transport plus vertex-local T1 only
   for `(9,15,7,3)@2`; its lines 353-374 explicitly leave the other five
   transport replays undone. The six solutions at
   `xmodel/sol-td7-law.md:270-283` are merge-local solutions. The premise that
   all six have already survived a common transport tier is therefore too
   strong.
2. The promoted case-III erratum E5 is material. Under the E5/H5a corrected
   update, four recorded class-C cells fail before coefficient emission:
   `(15,25,8,5)@7`, `(15,25,12,5)@3`, `(18,27,13,9)@5`, and
   `(39,65,32,13)@7`. The two cells with arrival and merge characteristic
   both equal to 7, `(9,15)@2` and `(10,15)@3`, survive this preflight.
   The arithmetic is in section 2.2.
3. The advertised 53 routes and 35 equality routes are 53/35 deduplicated
   **completion records**, not vertex paths. `px5.py` discards predecessors,
   equal-cost alternatives, some characteristics, and multiplicity
   partitions. The corresponding raw census is 59/41. No coefficient-system
   sharing among the 35 equality records is currently certified.
4. Statement 3.9 transports the full pattern of a fixed global polynomial
   and its jet, not the reduced Prop. 8.1 polynomials `p,q`. Thus an emitter
   which merely equates the six local `A` parameters is the wrong object.

The implementation consequently has two products:

- `LEAD-PILOT`: a necessary, finite system containing all certified local
  equations, exact full-`f` degree synchronization, actual continuation
  directions, and leading Taylor transport. Section 3 fully instantiates and
  exactly solves this system for a synchronized direct `(9,15)@2` route.
- `FULL-ROUTE`: the same system plus shared `f,g,h_j` jets, tower identities,
  every chart coefficient through the certified cancellation windows, and
  terminal/Jacobian closure. It may be emitted only from a complete route and
  tower certificate as defined below.

The direct pilot is **SAT over Q** at `LEAD-PILOT`; there is no smallest-cell
kill. The four E5 preflight failures are the first new next-tier eliminations,
conditional on the campaign's E5/H5a promoted reading.

`CONJECTURE H5a.` Notation 3.5's value at a doubly realized vertex is the
jump/max value. This is the campaign's coherence-forced convention and is
promoted in `SHEET6-III.md`, but `SIGRAY-AUDIT.md:26,92` still records the
underlying printed Notation 3.5 as a GAP. All statements below depending on
that convention say so. The E5 formula itself is rederived in
`SHEET6-III.md:131-147` and independently confirmed in
`SHEET6-HIII-REVIEW.md:102-134`.

## 1. The equation system

### 1.1 Field, orientation, and the route certificate

The thesis is over `C`. Every emitted characteristic-zero system is defined
over

\[
                         k_0=\mathbb Q                         \tag{F1}
\]

and satisfiability means a point over `Qbar`. Parameters such as `A` and an
actual continuation `c` remain polynomial variables; this avoids selecting
number fields prematurely. Equivalently, a single local family can be viewed
over `Q(A)`. Five of the six merge-local coefficient forms split over
`Q(A)`; the quadratic `(15,25,8,5)` form has roots
`A(1+-sqrt(2))/3`, so individually labelled roots require
`Q(A,sqrt(2))`. No such extension is needed in symmetric-coefficient form.
An edge normally requires `c^nu=A`; retaining both variables keeps the
system over `Q` and represents the union of root-of-unity branches.

Use one orientation everywhere:

- `L=rootward` is the shallower vertex;
- `U=poleward` is the deeper vertex;
- an edge is written `L -> U`, with `U=L*c` at one elementary level.

This avoids the source's letter reversal: Prop. 3.2/St. 3.17 write the deeper
vertex as `F=G+c`, while Prop. 9.3 writes it as `G=F+c`; see
`SHEET6-DEPTH-REVIEW.md:129-132`.

A `RouteCertificate` is not an endpoint `(w,M,lambda)`. It must contain:

\[
\begin{split}
\mathcal R=(&V,E,R,\{P_i\});\\
v\in V:\quad&
(\pi_v,\kappa_v,\nu_v,\bar\kappa_v,D_v,i_v,
 d_{p,v},d_{q,v},M_v,\rho_v,w_v,\lambda_v),\\
e=(L,U)\in E:\quad&
(\text{case}_e,n_e,\mu_e,N_e,c_e,
 \text{zero/nonzero},\text{arrival label}),                 \tag{F2}\\
&\text{the complete }(\epsilon,l,k,(m_j),\ell_{\rm ex})
 \text{ shape at every non-pole vertex},\\
&\text{the global labels }h_0=g,h_1,\ldots,h_m,
 (k_j,l_j),d_{h_j,v},m_v\text{ at every vertex},\\
&\text{root and x-side terminal data, all chart slots, and all
 discrete root-of-unity choices.}
\end{split}
\]

Here

\[
 \bar\kappa_v=\kappa_v(1-\pi_v),\qquad
 X_v=D_v/i_v,\qquad
 \rho_v={D_v\over\deg p^{\rm full}_{f,v}}
       ={X_v\over d_{p,v}},\qquad
 \theta_v={d_{p,v}\over d_{q,v}}={X_v\over\bar\kappa_v},
                                                                    \tag{F3}
\]

and

\[
                         w_v={\bar\kappa_v-\rho_v\over\nu_v}.       \tag{F4}
\]

`rho` and `theta` are different. `rho` is the DEPTH frame coordinate;
`theta` is the reduced T1 slope.

### 1.2 Algebraic variables

For fixed discrete data (F2), the default polynomial variables are:

| family | meaning |
|---|---|
| `p[v,a]`, `q[v,b]` | coefficients of the monic reduced patterns `p_v(eta)`, `q_v(eta)`, or their orbit-factored parameters |
| `C[v]` | normalized nonzero T1 constant in (L2) |
| `A[v,r]`, `B[v,s]` | nonzero orbit values in `t=eta^nu`; these are not full-pattern leading scales |
| `c[e,j]` | actual continuation and intermediate composite-chart coefficients; `c[e,0]` is the first direction |
| `S[v,h]` | leading scale of the full top pattern of the fixed global polynomial `h` at `v` |
| `J[v,h,r,a]` | coefficient of `eta^a` in jet row `P[v,h,r](eta)` |
| `s[j]` | global approximate-root/tower constant in `h[j+1]=h[j]^k-s[j](f-a)^l` |
| `F[a,b]`, `G[a,b]` | optional global coefficients of `f,g` in a certified Newton rectangle, for `GLOBAL-CLOSED` mode |
| `u[tag]` | a fresh Rabinowitsch inverse for one forced-nonzero polynomial |

Every variable has exactly one owner in the manifest. An orbit value `A`, an
actual direction `c`, a leading scale `S`, and a tower constant `s` are four
different objects and may not share a variable merely because a local gauge
could normalize one of them.

### 1.3 Local Prop. 8.1 equations

At a non-pole `v`, Prop. 8.1(i),(ii),(iv),(v) gives

\[
 p^{\rm full}_{f,v}=S_{v,f}p_v^{i_v},\qquad
 p_{h_{m_v},v}=S_{v,h_m}p_v^{k_v}q_v,
 \qquad k_v=i_v(\mu_v-1),                                \tag{L1}
\]

\[
 \theta_vp_vq'_v-p'_vq_v=C_vp_v,qquad C_v\ne0,           \tag{L2}
\]

or, without rational coefficients,

\[
 d_{p,v}p_vq'_v-d_{q,v}p'_vq_v-d_{q,v}C_vp_v=0.           \tag{L3}
\]

The emitter expands (L3) in `eta` and emits every coefficient. An equivalent
frame-normalized equation is

\[
 X_vp_vq'_v-\bar\kappa_vp'_vq_v=C_v^\kappa p_v,
 \qquad C_v^\kappa=\bar\kappa_v C_v\ne0.                  \tag{L4}
\]

The top row of (L3) is exactly the slope identity in (F3), not an additional
constraint. The ground statement and the full/reduced distinction are
`SHEET6-L1.md:68-81` and `SHEET6-MP-REVIEW.md:162-170`.

At a class-C merge, R2.2 fixes the factor form

\[
 p_v=\eta^{\epsilon_v}
 \prod_{e\ne0}(\eta^{\nu_v}-A_{v,e})^{\mu_e}
 \prod_j(\eta^{\nu_v}-B_{v,j})^{m_j},                    \tag{L5}
\]

\[
 q_v=\eta
 \prod_{\text{distinct nonzero }p\text{-orbits}}
       (\eta^{\nu_v}-A)
 \prod_r(\eta^{\nu_v}-Q_{v,r}).                         \tag{L6}
\]

A zero arrival contributes `eta^mu0`, not a nonzero orbit. The emitter must
check, before creating rows,

\[
 \mu_e d_q>d_p,\quad m_jd_q<d_p,\quad d_p\ne m d_q,
 \quad M=\gcd(d_p,d_q),\quad\gcd(M,\nu)=1.                \tag{L7}
\]

These are BOOK R2.2, `BOOK-OFFAXIS.md:317-325`, plus R1.0 at lines
209-224. Root separation, nonzero orbit values, squarefreeness, relevant
resultants, and `C_v` are open conditions. Each is internalized as

\[
                              u_g g-1=0                   \tag{L8}
\]

with a fresh `u_g`. No solver-side saturation is assumed.

At a pole, Prop. 8.1 is replaced by the Prop. 5.3 pole Wronskian and the
fixed pole degrees. The constructor receives the pole shape and emits its
coefficient rows, squarefreeness, coprimality and nonzero Wronskian constant;
it must not pretend that a pole has a reduced `q_v` belonging to an arbitrary
terminal tower member.

### 1.4 Numerical transport and degree synchronization

The numerical layer is an exact preflight, not a polynomial system to send
to msolve.

For a clean thickened chain child with
`(d_p,d_q)=(l*nu,n*nu+1)` and
`Delta=(n-1)*nu+1`, BOOK R1.2 states

\[
 \tau_e={\bar\kappa_U-\rho_U\over\Delta_L},\quad
 n_e=\tau_e\nu_L-\rho_U\in\mathbb N^*,\quad
 \bar\kappa_L={\tau_e d_{q,L}\over\nu_U},\quad
 \rho_L={\tau_e\over\nu_U},                              \tag{H1}
\]

\[
                         w_L=w_U{n\over\Delta_L}.          \tag{H2}
\]

Here the route direction is rootward `L` to poleward `U`; (H1) is BOOK
R1.2 (`BOOK-OFFAXIS.md:239-256`) with its parent/child names translated.
Use `tau`, never `t`, because local systems reserve `t=eta^nu`. For a dirty
child, R1.4 gives

\[
 \bar\kappa_L={l w_U d_{q,L}\over l d_{q,L}-d_{p,L}},
 \quad\rho_L={\bar\kappa_L\over d_{q,L}},
 \quad w_L=w_U{l(d_{q,L}-1)\over
                     \nu_L(l d_{q,L}-d_{p,L})}.            \tag{H3}
\]

At a merge `L=G`, a nonzero case-I/II arrival `U` obeys BOOK R2.1

\[
 X_G=\mu_e(\bar\kappa_G-w_U),\qquad
 n_e=\nu_U\bar\kappa_G-\bar\kappa_U\in\mathbb N^*.        \tag{H4}
\]

For a zero case-III arrival, do **not** emit BOOK's old mixed formula.
With E5/H5a and `G` rootward, `U` poleward,

\[
 D_G={\nu_GD_U+n_e\deg p^{\rm full}_{f,U}\over\nu_U},
 \qquad
 \bar\kappa_G={\nu_G\bar\kappa_U+n_e\over\nu_U},         \tag{H5}
\]

and hence

\[
                 X_G=\mu_0(\bar\kappa_G-\nu_Gw_U).        \tag{H6}
\]

BOOK R2.1 and `px5.py` instead use `nu_U*w_U`. The formulas coincide only
when `nu_G=nu_U`; section 2.2 applies this mandatory branch check.

The coefficient layer additionally requires the St. 3.17/St. 8.3 count
equalities. For every edge and fixed global `h`,

\[
 \deg p_{h,U}=\operatorname{mult}(p_{h,L},c_e).            \tag{H7}
\]

For `h=f-a`, (L1) makes this

\[
 \deg p^{\rm full}_{f,U}=i_L\mu_e.                        \tag{H8}
\]

At a merge all incoming values in (H8) must give the same `i_G`. This
`i`-synchronization was explicitly not used to kill in
`BOOK-OFFAXIS.md:640-646`; the coefficient emitter must produce the actual
integer witness before emitting a route.

The M-fold hazard at `BOOK-OFFAXIS.md:114-119` is precisely that
`(d_p,d_q)` need not be primitive. Never recover `tau` by reducing that pair
and silently dropping `M`. Either use the cross-multiplied Prop. 9.3 ratio or
the proved cancellation in R1.2. A route fails closed if neither derivation
is recorded.

### 1.5 Exact chart and full-jet transport

Fix one suitable common denominator `K` and put `z=x^(-1/K)`. For every
global polynomial label `h`, write the top-down jet at `v` as

\[
 h=x^{d_{h,v}}J_{v,h}(z,\eta_v),\qquad
 J_{v,h}=\sum_{r=0}^{B_{v,h}}z^rP_{v,h,r}(\eta_v),
 \qquad P_{v,h,0}=p_{h,v}.                                \tag{J1}
\]

For an elementary rootward-to-poleward step, St. 3.9 uses

\[
                  \eta_L=c_e+z\eta_U.                     \tag{J2}
\]

For a composite edge of `N_e=K*(pi_U-pi_L)` elementary slots, retain all
intermediate chart coefficients:

\[
 \eta_L=C_e(z)+z^{N_e}\eta_U,\qquad
 C_e(z)=c_{e,0}+c_{e,1}z+\cdots+c_{e,N_e-1}z^{N_e-1}.      \tag{J3}
\]

Setting an on-grid coefficient to zero is legal only when the route proves
it absent. The integer offset is checked from Prop. 9.3:

\[
 \pi_U-\pi_L={n_e\over\kappa_U}\quad(\mathrm{I/II}),
 \qquad
 \pi_U-\pi_L={n_e\over\nu_L\kappa_U}\quad(\mathrm{III}), \tag{J4}
\]

while at case IV, `pi_L=0` and
`pi_U=(nu_U-bar_kappa_U)/nu_U`. These offsets and the source naming warning
are audited in `SHEET6-DEPTH-REVIEW.md:129-132`.

Let

\[
 m_{e,h}=\operatorname{mult}(P_{L,h,0},c_{e,0})
          =\deg P_{U,h,0},\qquad
 d_{h,U}=d_{h,L}-{m_{e,h}N_e\over K}.                      \tag{J5}
\]

The honest transport equation is the coefficient identity

\[
 J_{L,h}\bigl(z,C_e(z)+z^{N_e}\eta\bigr)
       -z^{m_{e,h}N_e}J_{U,h}(z,\eta)=0                   \tag{J6}
\]

through every requested `(z,eta)` coefficient. This is St. 3.9, not an
extra hypothesis. At one elementary step, (J6) includes the divisibility
conditions

\[
 P_{L,h,r-j}^{(j)}(c_e)=0
       \quad(0\le r<m_{e,h},\ 0\le j\le r),               \tag{J7}
\]

and the deep rows

\[
 P_{U,h,s}(\eta)=
 \sum_{j=0}^{m_{e,h}+s}{P_{L,h,m_{e,h}+s-j}^{(j)}(c_e)\over j!}\eta^j.
                                                                    \tag{J8}
\]

Thus the leading coefficient of `P_U,0` is the `m`-th Taylor coefficient
of `P_L,0`, but its lower coefficients come from lower shallow jet rows.
This is exactly why equating reduced local `A_v` values is unsound.
Factorials in (J8) are cleared row by row before emission. For a child window
`B_U`, a necessary shallow window is at least

\[
                         B_L\ge m_{e,h}N_e+B_U.             \tag{J9}
\]

The manifest records whether the chosen windows satisfy every recurrence
needed by the requested theorem. A partial window is labelled `PREFIX`; it
is never labelled `FULL-ROUTE`.

### 1.6 Tower identities and common global objects

Prop. 4.2 defines

\[
 h_0=g,\qquad h_{j+1}=h_j^{k_j}-s_j(f-a)^{l_j}.            \tag{T1}
\]

Let `D[v,h]=K*d[h,v]` and
`E=max(D[v,h[j+1]],k_j*D[v,h[j]],l_j*D[v,f])`. The normalized jet equation
at each vertex is

\[
 z^{E-D_{j+1}}J_{v,h_{j+1}}
 -z^{E-k_jD_j}J_{v,h_j}^{k_j}
 +s_jz^{E-l_jD_f}J_{v,f}^{l_j}=0.                         \tag{T2}
\]

Every coefficient through the declared window is emitted. The same global
`s_j` is used at every vertex. A local terminal `q_v` is attached only to
the global label `h_{m_v}` justified by the certificate through (L1); the
terminal member may change with `v`. `SIGRAY-AUDIT.md:54` records a GAP in
Prop. 4.2 for a constant leading part. A route encountering that situation
must stop as `UNRESOLVED-PROP4.2`; it may not invent `l_j>0`.

In `GLOBAL-CLOSED` mode, global coefficient arrays `F[a,b]`, `G[a,b]` are
shared by every chart. Expanding those same arrays in every `(x,eta_v)` chart
must reproduce `J[v,f]`, `J[v,g]`. This is the strongest way to prevent
different branches from describing unrelated formal polynomials. A lighter
`FULL-ROUTE` mode shares jets and tower labels on the certified route and is
a necessary obstruction system, but its nonemptiness does not prove global
polynomiality.

### 1.7 Terminal and Jacobian closure

For the last y-side vertex `G`, BOOK P1 (`BOOK-OFFAXIS.md:486-500`) gives

\[
 {d_{(0,y)}\over\deg p^{\rm full}_{f,G}}
 ={\rho_G+\nu_G-\bar\kappa_G\over\nu_G}=1-w_G,             \tag{R1}
\]

\[
 R={1\over1-w_G},\qquad
 \psi=\left\lceil{1\over1-w_G}\right\rceil-1,
 \qquad\sum_F\lambda_F\le td-1-\psi,                     \tag{R2}
\]

\[
 0<w_G<1,\quad M_G\ge2,\quad
 j=M_G(1-w_G)\in\mathbb N^*.                              \tag{R3}
\]

The root has one y-side direction (`SHEET6-LROOT.md:100-126`):

\[
 p_{f,(0,y)}=S_R(\eta-c_0)^{k_f},\qquad
 k_f=\deg p^{\rm full}_{f,G},\qquad l_f=d_{(0,y)}.         \tag{R4}
\]

Use the corrected chart swap, not the duplicated printed St. 3.12 display:

\[
 d_{(0,x)}=k_f,\quad\deg p_{f,(0,x)}=l_f,
 \quad d_{(0,y)}=l_f,\quad\deg p_{f,(0,y)}=k_f.            \tag{R5}
\]

`SIGRAY-AUDIT.md:44` is the chart-label erratum. Equations (J6) are imposed
on the terminal edge for every live tower label. Terminal closure is not just
the numerical P1 check: the x-side/root tower certificate must supply the
patterns demanded by (R5).

Finally impose the Keller identity on the shared `f,g` jets. Since
`eta=x^pi(y-tail)` and `z=x^(-1/K)`, one has

\[
 J_{x,y}(f,g)=x^\pi J_{x,\eta}(f,g)=1,
\]

so, in a fixed chart orientation,

\[
 z^{K+1}(f_\eta g_z-f_zg_\eta)-Kz^{K\pi}=0.               \tag{R6}
\]

Clear Laurent powers and emit all coefficients in the certified window.
The sign and chart orientation receive a planted `J=1` unit test. If the
route has no x-side/root tower data, the emitter stops at `LEAD-PILOT` or
`PREFIX`; it must not silently call P1 alone a closed coefficient system.

## 2. Instantiation for the six cells and their completion records

### 2.1 Merge-local specializations

For every class-C target put

\[
 t=\eta^\nu,\qquad
 p=\eta^\mu(t-A),\qquad
 q=\eta(t-A)s(t),\qquad
 s=t^\ell+\sum_{j=0}^{\ell-1}s_jt^j.                       \tag{I1}
\]

Substitution in (L2) gives the exact triangular equation

\[
 (\theta-\mu)(t-A)s+(\theta-1)\nu ts
       +\theta\nu t(t-A)s'=C,\qquad \theta=d_p/d_q.        \tag{I2}
\]

Emit every coefficient of (I2). The six certified local solutions are:

| cell at `mu0` | `ell` | monic `s(t)` | normalized `C` | local coefficient field |
|---|---:|---|---|---|
| `(9,15,7,3)@2` | 1 | `t-2*A/3` | `-14*A^2/15` | `Q(A)` |
| `(10,15,7,5)@3` | 1 | `t-A/2` | `-7*A^2/6` | `Q(A)` |
| `(15,25,8,5)@7` | 2 | `t^2-2*A*t/3-A^2/9` | `-32*A^3/45` | coefficients in `Q(A)`; split roots in `Q(A,sqrt(2))` |
| `(15,25,12,5)@3` | 1 | `t-2*A/3` | `-8*A^2/5` | `Q(A)` |
| `(18,27,13,9)@5` | 1 | `t-A/2` | `-13*A^2/6` | `Q(A)` |
| `(39,65,32,13)@7` | 1 | `t-2*A/3` | `-64*A^2/15` | `Q(A)` |

This table is exactly `xmodel/sol-td7-law.md:264-283` and
`xmodel/td7-law-engine-check.md:99-108`. It is a regression registry, not a
six-route gluing certificate.

### 2.2 Mandatory E5 preflight: four recorded cells fail

The nonzero chain-1 arrival has `mu=1,w=2`, so (H4) gives

\[
                              X_G=\bar\kappa_G-2.           \tag{I3}
\]

Combining (I3) with the corrected zero-edge equation (H6) gives the
E5-required value

\[
 \bar\kappa_G^{\rm E5}
       ={\mu_0\nu_Gw_U-2\over\mu_0-1}.                    \tag{I4}
\]

Independently, the cell ratio and (I3) give

\[
 \bar\kappa_G^{\rm cell}={2d_q\over d_q-d_p},qquad
 X_G=\bar\kappa_G^{\rm cell}-2.                            \tag{I5}
\]

The complete check is:

| cell | `mu0` | zero-arrival `(w_U,nu_U)` | merge `nu_G` | `(bar_kappa_cell,X)` | `bar_kappa_E5` | verdict |
|---|---:|---|---:|---|---:|---|
| `(9,15,7,3)` | 2 | `(1/2,7)` | 7 | `(5,3)` | 5 | PASS |
| `(10,15,7,5)` | 3 | `(2/3,7)` | 7 | `(6,4)` | 6 | PASS |
| `(15,25,8,5)` | 7 | `(2/21,48)` | 8 | `(5,3)` | `5/9` | **REJECT** |
| `(15,25,12,5)` | 3 | `(1/2,8)` | 12 | `(5,3)` | 8 | **REJECT** |
| `(18,27,13,9)` | 5 | `(2/15,39)` | 13 | `(6,4)` | `5/3` | **REJECT** |
| `(39,65,32,13)` | 7 | `(2/21,48)` | 32 | `(5,3)` | `29/9` | **REJECT** |

This is a proved algebraic contradiction conditional on `CONJECTURE H5a` and
the promoted E5 correction. Under the other coherent reading—printed (g),(h)
together with the definitions—the printed formulas force `nu_G=nu_U`, so
the same four records are rejected. Only the old mixed engine reading keeps
`nu_U` free while using the printed denominator; that mixture corresponds to
neither Notation 3.5 value (`SHEET6-HIII-REVIEW.md:107-128`).

Default implementation policy:

- write a rejection manifest containing (I3)-(I5) for these four cells;
- emit no msolve job for them;
- retain a `--legacy-mixed-iii` diagnostic mode only for reproducing the old
  route book, with `UNSOUND-FOR-VERDICT` stamped into every artifact.

After this gate, the endpoint census is 49 deduplicated records, 31 at
budget equality, or 51 raw generator records, 33 at equality. These are the
two surviving cells only; they are still not concrete-route counts.

### 2.3 What the 53/35 census actually contains

The exact filed census is:

| cell at `mu0` | dedup records | dedup equality | raw records | raw equality | recorded arrival `(w2,lambda,nu2)` |
|---|---:|---:|---:|---:|---|
| `(9,15,7,3)@2` | 2 | 2 | 4 | 4 | `(1/2,4,7)` |
| `(10,15,7,5)@3` | 47 | 29 | 47 | 29 | `(2/3,2,7)` |
| `(15,25,8,5)@7` | 1 | 1 | 2 | 2 | `(2/21,5,48)` |
| `(15,25,12,5)@3` | 1 | 1 | 2 | 2 | `(1/2,5,8)` |
| `(18,27,13,9)@5` | 1 | 1 | 2 | 2 | `(2/15,5,39)` |
| `(39,65,32,13)@7` | 1 | 1 | 2 | 2 | `(2/21,5,48)` |
| **total** | **53** | **35** | **59** | **41** | |

The two `(9,15)` equality endpoints are the direct terminal
`(w,M,psi)=(2/3,3,2)` and the one-step trunk terminal `(2/5,5,1)`.
For `(10,15)`, the direct equality terminal is `(4/5,5,4)`. Its other 28
equality endpoints all have `psi=1`:

```text
(1/2,8) (1/3,12) (1/4,4) (1/4,8) (1/5,5) (1/5,10)
(1/6,6) (1/6,12) (1/7,7) (1/7,14)
(2/19,19) (2/21,21) (2/23,23) (2/25,25) (2/27,27)
(2/29,29) (2/31,31) (2/33,33) (2/5,10) (3/16,16)
(4/19,19) (4/21,21) (4/23,23) (4/25,25) (4/27,27)
(4/29,29) (4/31,31) (4/33,33)
```

The other singleton endpoints are `(2/5,5)` for both `(15,25)` cells,
`(4/9,9)` for `(18,27)`, and `(2/13,13)` for `(39,65)`.

The six raw-to-dedup collapses are not coefficient deduplications:

- each `(9,15)` terminal collapses arrivals with `M2=2` and `M2=4`;
- `(15,25,12)` collapses `M2=3,6`;
- `(18,27)` collapses `M2=5,15`;
- `(15,25,8)` and `(39,65)` each collapse `M2=7,21`.

For example, the collapsed `(18,27)` branches already have different
tie-broken predecessor shapes,

\[
 (21,15)\to(35,15)\to(117,27)\to(35,15)                  \tag{I6}
\]

and

\[
 (20,16)\to(130,40)\to(105,15).                          \tag{I7}
\]

The loss occurs because `close_with_cells` retains only a minimum cost and
small arrival set (`px5.py:63-87`), `trunk_routes` retains only
`(cost,psi,w,M)` (`:98-112`), and the final key ignores the current `M2`
(`:254-262`). In addition, `px2.py:66-76` omits the free `nu` from pure-b
tags and `:111-125` omits the NE multiplicity partition from dirty tags.

No pair among the 35 equality records is presently proved to share a
coefficient system. A tie-broken tag replay gives four **provisional**
`(10,15)` pairs with the same visible tag sequence:

\[
 (1/4,M=4/8),\ (1/5,M=5/10),\ (1/6,M=6/12),\ (1/7,M=7/14). \tag{I8}
\]

`CONJECTURE (provisional tag dedup).` If all omitted characteristics,
multiplicity partitions, tower labels, chart coefficients and full-degree
data also agree, (I8) will reduce the 35 equality summaries to 31 systems.
This is not a permitted implementation dedup. The only permitted dedup key
is a canonical hash of the fully assembled polynomial IR after alpha-renaming
and after a proved global gauge quotient.

### 2.4 Stage-0 route expansion and neutral-depth families

For each completion record, instantiation proceeds in this order.

1. Re-run the transition graph while retaining **all** equal-cost
   predecessors, the exact step cell, `nu,epsilon,l,k,(m_j),ell_ex`, edge
   `n`, arrival type, current `M`, and terminal path.
2. Apply the coherent Prop. 9.3 case classification and E5 preflight before
   selecting local coefficients.
3. Solve (H7)-(H8) for every global label, not only for `f`. Attach an exact
   integer `i_v` at every vertex.
4. Expand every zero-cost neutral step which is needed for degree
   synchronization. Record its actual characteristic and pattern; a
   state-level `neutral-drop` tag is insufficient.
5. Attach the complete tower labels and cancellation levels. If they cannot
   be deduced from promoted statements, return `UNRESOLVED-TOWER`.
6. Choose common `K`, compute every integer slot offset `N_e`, and retain the
   entire chart polynomial (J3).
7. Assemble local, transport, tower, terminal and guard rows. Only now
   canonicalize and hash.

There is an important finiteness boundary. Zero-cost neutral vertices can be
inserted without changing `(w,M,lambda)`, while multiplying full pattern
degrees. If both branches are padded, a single endpoint summary can represent
unbounded synchronized full degrees. Exponents are discrete and cannot be
made symbolic in msolve.

`CONJECTURE (neutral-insertion invariance).` After eliminating chart and
scale variables, inserting a clean neutral cell does not change the decisive
coefficient eliminant. No promoted result proves this. Until it is proved,
the emitter is complete only for an explicitly supplied finite
`RouteCertificate`; emptiness for one minimal representative does not kill
all neutral paddings of an endpoint summary. There must be no depth cap
masquerading as coverage.

### 2.5 Honest size accounting

Only merge-local sizes are exact before Stage 0. With monic `s`, the variables
`(A,s_0,...,s_(ell-1),C)` number `ell+2`, and (I2) has `ell+1` nontrivial
coefficient rows. One combined nonzero guard adds one variable/row; individual
auditable guards add more.

| cell | E5 default fate | exact factored merge-local vars/eqs | naive unnormalized dense-eta local vars/eqs | route-level information currently justified |
|---|---|---:|---:|---|
| `(9,15,7,3)@2` | emit | `3/2` | `27/24` | direct synchronized `LEAD-PILOT`: **83/74**, section 3; full jets TBD |
| `(10,15,7,5)@3` | emit | `3/2` | `28/25` | full paths TBD; one equality suffix has a dense local-only subtotal about `2610/2595` |
| `(15,25,8,5)@7` | reject | `4/3` | `43/40` | no default solver system |
| `(15,25,12,5)@3` | reject | `3/2` | `43/40` | no default solver system |
| `(18,27,13,9)@5` | reject | `3/2` | `48/45` | no default solver system; dedup branches differ as (I6)-(I7) |
| `(39,65,32,13)@7` | reject | `3/2` | `107/104` | no default solver system; legacy representative dense local-only subtotal about `2149/2131` |

The dense diagnostic counts use all coefficients of unnormalized `p,q` plus
`C`; they exclude transports, towers, terminal rows and guards. They are not
recommended parametrizations. A representative legacy path to `(39,65)` is

\[
 (20,16)\to(119,35)\to(55,11)\to(651,63)
 \to(1008,49)\to(39,65),                                  \tag{I9}
\]

already giving the stated `2149/2131` local-only subtotal. A `(10,15)` route
through `(279,63),(425,51),(1617,99)` is larger, so `(39,65)` is not uniquely
the biggest once route vertices are counted. It is nevertheless the largest
single merge-local dense pattern, and its default fate is now an inexpensive
E5 rejection rather than a giant solver lane.

For a decorated route, the emitter computes rather than estimates

\[
 N_{\rm jet}=\sum_{v,h}\sum_{r=1}^{B_{v,h}}
                 (1+\deg P_{v,h,r}),                       \tag{I10}
\]

plus local, chart, tower, global and inverse variables. The transport-row
count is the number of `(z,eta)` coefficients in (J6), including the low-slot
divisibility rows (J7); tower and Jacobian counts are computed similarly from
(T2) and (R6). The dry-run manifest must print every summand of these counts.

`CONJECTURE (engineering size only).` The first useful characteristic window
will have roughly 100-300 active series coefficients and `10^3-10^4` sparse
transport/Jacobian rows, as estimated in `xmodel/sol-avenues2.md:282`.
Full-route systems can be much larger, especially after exact `i`-sync. This
estimate is not a theorem, a cap, or a per-cell certified count.

## 3. Falsifiable pilot: direct `(9,15,7,3)@2`

### 3.1 Scope of the pilot

The repository does not contain the tower labels, tower levels, x-side root
patterns, or subleading chart rows needed to instantiate (J6),(T2),(R6) for
this route. Therefore a claimed full `h_j`-jet system written today would
invent data. The literal system in section 3.5 is instead the maximal
source-certified `LEAD-PILOT`:

- every displayed non-pole local T1 equation;
- both pole Wronskians;
- all root/anatomy guards;
- an exact full-`f` degree synchronization;
- actual continuation roots `c^nu=A`;
- leading St. 3.9 Taylor transport on every edge; and
- the numerical case-IV terminal closure.

Emptiness would kill this concrete route. Nonemptiness is only a leading-
pattern survival. Section 3.7 states the exact missing rows before the
implementation may promote it to `FULL-ROUTE`.

### 3.2 An exact synchronized representative

The path displayed in `xmodel/sol-sixcells.md:86-100` synchronizes the
chain-2 data numerically but not the full `f` degrees against a direct
chain-1 pole-to-merge edge. Add one zero-cost clean neutral chain-1 vertex

\[
 N:\quad \nu_N=11305,\quad
 p_N=\eta^{11305}-A_N,\quad
 q_N=\eta(\eta^{11305}-A_N).                              \tag{P1}
\]

From the chain-1 pole frame `(rho,kbar,nu;w,M)=(1,5,2;2,1)`, R1.2 with
`Delta=1` gives

\[
 \tau=4,\quad n_{N\to P_1}=45219,\quad
 (\rho_N,\bar\kappa_N,\nu_N;w_N,M_N)
    =(2,22612,11305;2,1).                                 \tag{P2}
\]

The nonzero merge edge then has

\[
 n_{G\to N}=11305\cdot5-22612=33913,qquad X_G=3.          \tag{P3}
\]

On the other branch use the certified representative

\[
 P_2\leftarrow F_1\leftarrow F_2\leftarrow F_3
       \leftarrow H_2\leftarrow G,                        \tag{P4}
\]

where arrows point rootward in the displayed chain, with the local cells from
`xmodel/sol-sixcells.md:86-100`. In the uniform rootward-to-poleward
orientation of section 1, the whole tree is

```text
R
|
G
+-- N  -- P1
+-- H2 -- F3 -- F2 -- F1 -- P2
```

The full `f` degree ledger is:

| vertex | reduced `(d_p,d_q,nu)` | `i_v` | full `f` degree | arriving reduced multiplicity from this rootward vertex |
|---|---|---:|---:|---:|
| `R` | root pattern | — | 203490 | 203490 at `c0` |
| `G` | `(9,15,7)` | 22610 | 203490 | 1 toward `N`; 2 at zero toward `H2` |
| `N` | `(11305,11306,11305)` | 2 | 22610 | 1 toward `P1` |
| `P1` | pole full degrees `(2,3)` | — | 2 | — |
| `H2` | `(14,8,7)` | 3230 | 45220 | 2 toward `F3` |
| `F3` | `(38,6,5)` | 170 | 6460 | 7 toward `F2` |
| `F2` | `(119,35,17)` | 10 | 1190 | 4 toward `F1` |
| `F1` | `(20,16,5)` | 2 | 40 | 2 toward `P2` |
| `P2` | pole full degrees `(4,6)` | — | 4 | — |

Every row satisfies (H8), e.g. `22610*2=45220` at the zero branch and
`170*7=1190` at `F3`. The case-III edge `G -> H2` has E5 raw `n=7`
(the `n'=1` used in `sol-sixcells.md` is `n/nu_G`); here
`nu_G=nu_H=7`, so E5 and BOOK coincide.

At the direct terminal,

\[
 (\rho_G,\bar\kappa_G,\nu_G;w_G,M_G)
   =(1/3,5,7;2/3,3),\quad
 k_f=203490,\quad l_f=(1-w_G)k_f=67830,                   \tag{P5}
\]

and `R=3,psi=2`. The charged chain-2 cost is 4, exactly the P1 budget
`6-psi=4`.

### 3.3 Local patterns and coefficient rows

The pilot variable `C_v` is the normalized constant in (L2). Put
`t=eta^nu` separately at each row. The patterns are:

| vertex | `p`, `q` | emitted local rows |
|---|---|---|
| `P1` | `p=eta^2-A_p1`, `q=eta*(eta^2-B_p1)` | `2*B_p1-3*A_p1=0`; `C_p1-3*A_p1^2=0` |
| `N` | `p=t-A_n`, `q=eta*(t-A_n)`, `nu=11305` | `11306*C_n+11305*A_n=0` |
| `G` | `p=eta^2*(t-A_g)`, `q=eta*(t-A_g)*(t-B_g)`, `nu=7` | `-14*A_g+21*B_g=0`; `-7*A_g*B_g-5*C_g=0` |
| `H2` | `p=(t-A_h)^2`, `q=eta*(t-A_h)`, `nu=7` | `4*C_h+7*A_h=0` |
| `F3` | `p=eta^3*(t-A_f3)^7`, `q=eta*(t-A_f3)`, `nu=5` | `3*C_f3+10*A_f3=0` |
| `F2` | `p=(t-A_f2)^4*(t-B_f2)^3`, `q=eta*(t-A_f2)*(t-B_f2)`, `nu=17` | `2*B_f2-3*A_f2=0`; `10*C_f2-51*A_f2^2=0` |
| `F1` | `R1(t)=t^2-Sig_f1*t+Pi_f1`; `p=(t-A_f1)^2*R1(t)`, `q=eta*(t-A_f1)*R1(t)`, `nu=5` | `Sig_f1-3*A_f1=0`; `Pi_f1-3*A_f1^2=0`; `4*C_f1+15*A_f1^3=0` |
| `P2` | `p=eta^4-A_p2*eta`; `q=eta^6+U_p2*eta^3+V_p2` | `2*U_p2+3*A_p2=0`; `8*V_p2-3*A_p2^2=0`; `8*C_p2-9*A_p2^3=0` |

The five non-pole chain rows and merge row are the exact substitutions
certified in `xmodel/sol-sixcells.md:145-174`. The neutral row follows from
(L2). The `P1` Wronskian is

\[
 2pq'-3p'q=C_{P1},                                        \tag{P6}
\]

and the displayed two rows are its coefficients. For the `(a,b,nu)=(1,2,3)`
pole, the same Prop. 5.3 Wronskian with full degrees `(4,6)` gives the exact
new derivation

\[
 p=\eta^4-A\eta,\quad q=\eta^6+U\eta^3+V,quad
 2pq'-3p'q=C_{P2},                                        \tag{P7}
\]

whose coefficients are precisely the three `P2` rows. Direct expansion
gives `U=-3*A/2`, `V=3*A^2/8`, `C=9*A^3/8`.

### 3.4 Directions and leading Taylor transport

The six nonzero continuation variables and derivative auxiliaries obey

\[
\begin{array}{lll}
 c_n^{11305}=A_n,&d_n=11305c_n^{11304},& N\to P1,\\
 c_g^7=A_g,&d_g=7c_g^6,&G\to N,\\
 c_h^7=A_h,&d_h=7c_h^6,&H2\to F3,\\
 c_{f3}^5=A_{f3},&d_{f3}=5c_{f3}^4,&F3\to F2,\\
 c_{f2}^{17}=A_{f2},&d_{f2}=17c_{f2}^{16},&F2\to F1,\\
 c_{f1}^5=A_{f1},&d_{f1}=5c_{f1}^4,&F1\to P2.
\end{array}                                                \tag{P8}
\]

Set

\[
 z_{f2}=A_{f2}-B_{f2},\qquad
 z_{f1}=A_{f1}^2-\mathrm{Sig}_{f1}A_{f1}+\mathrm{Pi}_{f1}. \tag{P9}
\]

For full `f`-pattern leading scales
`S_r,S_g,S_n,S_p1,S_h,S_f3,S_f2,S_f1,S_p2`, St. 3.9(ii) gives

\[
\begin{array}{rcl}
S_g&=&S_r,\\
S_h&=&S_gA_g^{22610},\\
S_n&=&S_gc_g^{45220}d_g^{22610},\\
S_{p1}&=&S_nd_n^2,\\
S_{f3}&=&S_hd_h^{6460},\\
S_{f2}&=&S_{f3}c_{f3}^{510}d_{f3}^{1190},\\
S_{f1}&=&S_{f2}d_{f2}^{40}z_{f2}^{30},\\
S_{p2}&=&S_{f1}d_{f1}^{4}z_{f1}^{2}.
\end{array}                                                \tag{P10}
\]

For example, the coefficient of the simple nonzero root of the reduced
merge pattern is `c_g^2*d_g`; raising it to `i_G=22610` gives the third
row. At the zero root its reduced coefficient is `-A_g`; the even exponent
gives the second row. At `F1`, the reduced Taylor coefficient is
`d_f1^2*z_f1`, then is squared because `i_f1=2`. These auxiliary-variable
rows avoid enormous integer tokens such as `7^22610`, which would trigger
the msolve `LONG_MAX` parsing hazard in positive characteristic.

### 3.5 Literal characteristic-zero msolve input

This block is ready for emission as written: 83 variables, characteristic
zero, 74 expanded polynomial generators, no parentheses. Rows 1-15 are
local equations, 16-21 direction equations, 22-27 derivative definitions,
28-29 separation auxiliaries, 30-37 leading transports, and 38-74 individual
Rabinowitsch guards.

```text
A_p1,B_p1,C_p1,A_n,C_n,A_g,B_g,C_g,A_h,C_h,A_f3,C_f3,A_f2,B_f2,C_f2,A_f1,Sig_f1,Pi_f1,C_f1,A_p2,U_p2,V_p2,C_p2,c_n,c_g,c_h,c_f3,c_f2,c_f1,d_n,d_g,d_h,d_f3,d_f2,d_f1,z_f2,z_f1,S_r,S_g,S_n,S_p1,S_h,S_f3,S_f2,S_f1,S_p2,u_p1_A,u_p1_B,u_p1_AB,u_p1_C,u_n_A,u_n_C,u_g_A,u_g_B,u_g_AB,u_g_C,u_h_A,u_h_C,u_f3_A,u_f3_C,u_f2_A,u_f2_B,u_f2_AB,u_f2_C,u_f1_A,u_f1_Pi,u_f1_disc,u_f1_z,u_f1_C,u_p2_A,u_p2_V,u_p2_disc,u_p2_qA,u_p2_C,u_S_r,u_S_g,u_S_n,u_S_p1,u_S_h,u_S_f3,u_S_f2,u_S_f1,u_S_p2
0
2*B_p1-3*A_p1,
C_p1-3*A_p1^2,
11306*C_n+11305*A_n,
-14*A_g+21*B_g,
-7*A_g*B_g-5*C_g,
4*C_h+7*A_h,
3*C_f3+10*A_f3,
2*B_f2-3*A_f2,
10*C_f2-51*A_f2^2,
Sig_f1-3*A_f1,
Pi_f1-3*A_f1^2,
4*C_f1+15*A_f1^3,
2*U_p2+3*A_p2,
8*V_p2-3*A_p2^2,
8*C_p2-9*A_p2^3,
c_n^11305-A_n,
c_g^7-A_g,
c_h^7-A_h,
c_f3^5-A_f3,
c_f2^17-A_f2,
c_f1^5-A_f1,
d_n-11305*c_n^11304,
d_g-7*c_g^6,
d_h-7*c_h^6,
d_f3-5*c_f3^4,
d_f2-17*c_f2^16,
d_f1-5*c_f1^4,
z_f2-A_f2+B_f2,
z_f1-A_f1^2+Sig_f1*A_f1-Pi_f1,
S_g-S_r,
S_h-S_g*A_g^22610,
S_n-S_g*c_g^45220*d_g^22610,
S_p1-S_n*d_n^2,
S_f3-S_h*d_h^6460,
S_f2-S_f3*c_f3^510*d_f3^1190,
S_f1-S_f2*d_f2^40*z_f2^30,
S_p2-S_f1*d_f1^4*z_f1^2,
u_p1_A*A_p1-1,
u_p1_B*B_p1-1,
u_p1_AB*A_p1-u_p1_AB*B_p1-1,
u_p1_C*C_p1-1,
u_n_A*A_n-1,
u_n_C*C_n-1,
u_g_A*A_g-1,
u_g_B*B_g-1,
u_g_AB*A_g-u_g_AB*B_g-1,
u_g_C*C_g-1,
u_h_A*A_h-1,
u_h_C*C_h-1,
u_f3_A*A_f3-1,
u_f3_C*C_f3-1,
u_f2_A*A_f2-1,
u_f2_B*B_f2-1,
u_f2_AB*A_f2-u_f2_AB*B_f2-1,
u_f2_C*C_f2-1,
u_f1_A*A_f1-1,
u_f1_Pi*Pi_f1-1,
u_f1_disc*Sig_f1^2-4*u_f1_disc*Pi_f1-1,
u_f1_z*z_f1-1,
u_f1_C*C_f1-1,
u_p2_A*A_p2-1,
u_p2_V*V_p2-1,
u_p2_disc*U_p2^2-4*u_p2_disc*V_p2-1,
u_p2_qA*A_p2^2+u_p2_qA*U_p2*A_p2+u_p2_qA*V_p2-1,
u_p2_C*C_p2-1,
u_S_r*S_r-1,
u_S_g*S_g-1,
u_S_n*S_n-1,
u_S_p1*S_p1-1,
u_S_h*S_h-1,
u_S_f3*S_f3-1,
u_S_f2*S_f2-1,
u_S_f1*S_f1-1,
u_S_p2*S_p2-1
```

### 3.6 Exact solve and pattern-positive anchors

The pilot has an explicit rational point. Set every local `A` and every
continuation `c` to 1, and set `S_r=1`. The remaining primary variables are

| vertex | values at the rational anchor |
|---|---|
| `P1` | `B_p1=3/2`, `C_p1=3` |
| `N` | `C_n=-11305/11306` |
| `G` | `B_g=2/3`, `C_g=-14/15` |
| `H2` | `C_h=-7/4` |
| `F3` | `C_f3=-10/3` |
| `F2` | `B_f2=3/2`, `C_f2=51/10` |
| `F1` | `Sig_f1=3`, `Pi_f1=3`, `C_f1=-15/4` |
| `P2` | `U_p2=-3/2`, `V_p2=3/8`, `C_p2=9/8` |

The auxiliaries are

\[
 (d_n,d_g,d_h,d_{f3},d_{f2},d_{f1})=(11305,7,7,5,17,5),
 \quad(z_{f2},z_{f1})=(-1/2,1),                            \tag{P11}
\]

and the scales are

\[
\begin{array}{lll}
S_g=1,&S_h=1,&S_n=7^{22610},\\
S_{p1}=7^{22610}11305^2,&S_{f3}=7^{6460},&
S_{f2}=7^{6460}5^{1190},\\
S_{f1}=7^{6460}5^{1190}17^{40}2^{-30},&
S_{p2}=S_{f1}5^4.&
\end{array}                                                \tag{P12}
\]

Set each inverse variable to the reciprocal of its named guard. All guards
are nonzero. The only composite checks not visually immediate are

\[
 \mathrm{Sig}_{f1}^2-4\mathrm{Pi}_{f1}=-3,\quad z_{f1}=1,
 \quad U_{p2}^2-4V_{p2}=3/4,
 \quad A_{p2}^2+U_{p2}A_{p2}+V_{p2}=-1/8.                 \tag{P13}
\]

Thus the saturated ideal is proper even over `Q`; no Gröbner computation is
needed to decide this pilot. A sparse exact expansion independently checks
all eight local Wronskian/T1 identities at this point.

For the standard good-prime smoke test `p=105337`, reduction of (P12) gives

```text
S_r=1 S_g=1 S_h=1 S_n=99463 S_p1=25391
S_f3=55907 S_f2=14678 S_f1=17872 S_p2=4278
```

and all inverse variables are set to finite-field reciprocals. The exact
rational anchor is the authority; this residue is a parser/emitter test, not
a mathematical verdict.

The implementation's pattern-positive gate reconstructs the actual
polynomials, rather than checking only the reduced rows:

1. **Value:** differentiate every displayed `p,q` in `eta` and verify every
   coefficient of (L3), (P6), and (P7).
2. **Alignment:** verify the exact supports, degrees, `t=eta^nu`, zero-root
   placement, and every equality in the full-degree ledger.
3. **Multiplicity:** verify each shared root occurs simply in `q`, every
   q-only root is simple, (P13), and the exact continuation multiplicity on
   each edge.
4. **Transport:** evaluate every row in (P10), first over `Q`, then at the
   finite-field anchor.

Required negative perturbations are: flip the T1 sign; omit one factor `nu`
from a derivative; move one jet level by one slot; replace `B_g=2*A_g/3` by
`3*A_g/2`; swap the rootward/poleward chart; and replace the E5 `nu_G` by
`nu_U` in a test with unequal characteristics. Every perturbation must fail
at least one independent anchor assertion.

**Pilot verdict: SAT / survives leading-pattern gluing.** This is an exact
solution, not a numerical or finite-field guess. No local msolve run was made;
`ops/FLEET.md:3-6` prohibits it, and a known rational point already settles
satisfiability.

### 3.7 Rows still owed for a full direct-route pilot

The following data are not present in the filed route artifacts and may not
be guessed:

- `m_v` and the common global `h_j` label whose top is
  `p_v^(i_v*(mu_v-1))*q_v` at each of `F1,F2,F3,H2,N,G`;
- every `(k_j,l_j,s_j)` and every `d_(h_j,v)` needed by (T2);
- the chart polynomial `C_e(z)` on each composite edge, including on-grid
  dead-stretch coefficients;
- the cancellation window depths needed to make each prescribed `q_v`
  emerge from the same global tower polynomial;
- root `g,h_j` patterns and the x-side data required by (R5)-(R6).

Once Stage 0 supplies them, the full pilot is instantiated mechanically:
seed row zero by (L1), recurse window bounds by (J9), emit all (J6) and (T2)
coefficients, attach the root/x-side arrays, then emit (R6). Until then, the
83/74 file must be named `lead_pilot`, not `gluing_full`.

This is not a claim that the missing full system is satisfiable.
`CONJECTURE (full-pilot survival).` The exact rational leading anchor extends
to compatible tower jets and terminal Jacobian rows. Nothing in the current
repository proves this conjecture; the honest emitter is intended to test it.

## 4. Soundness and proof perimeter

### 4.1 Emptiness implication

Fix a fully decorated route certificate `C` and let `I_C` be the ideal over
`Q` generated by its expanded local, chart, tower, terminal, Jacobian and
Rabinowitsch rows. There is a direct necessary-condition map:

\[
 \{\text{Keller pairs realizing }C\}
       \longrightarrow V_{\overline{\mathbb Q}}(I_C).      \tag{S1}
\]

Indeed, evaluate each variable at the corresponding coefficient of the
actual pair and its actual Puiseux charts. Prop. 8.1 gives (L1)-(L4), the
root law gives (L5)-(L8), the promoted handshakes give (H1)-(H6),
St. 3.9/3.17 and St. 8.3 give (H7)-(H8) and (J5)-(J8), the actual
approximate-root tower gives (T1)-(T2), and the terminal plus Keller identity
give (R1)-(R6). Every saturated quantity is nonzero on the genuine object,
so its inverse exists and satisfies (L8).

Consequently,

\[
                         1\in I_C\quad\Longrightarrow\quad
            \text{no Keller pair realizes }C.              \tag{S2}
\]

The same implication holds for any correctly generated necessary prefix:
emptiness of fewer necessary equations is still a kill. The manifest must
say exactly what was included; a prefix's nonemptiness has less content.

For an endpoint completion record rather than a concrete certificate, (S2)
kills the record only after **every** predecessor, arrival realization,
root-of-unity branch, neutral-depth family and tower branch represented by
that record has been covered. Current `px5` dedup does not provide this
coverage. A `[1]` result for one tie-broken path is a path kill, not one of
53 record kills.

A characteristic-zero reduced Gröbner basis `[1]` is the intended external
certificate, with the usual trust in the solver (`AUDIT.md:255-269`). A
mod-p `[1]` is corroboration only. A zero-byte output, timeout, partial basis,
nonzero return code, or unauthenticated log is no verdict.

### 4.2 What nonemptiness means

Nonemptiness of `LEAD-PILOT` means only that local patterns and full-`f`
leading Taylor scales can be made compatible on that concrete tree.
Nonemptiness of `PREFIX` means compatibility through the emitted jet depth.
Nonemptiness of `FULL-ROUTE` is still only a necessary formal route model.
It does not by itself prove:

- convergence or algebraicity of the formal Puiseux series;
- that un-emitted tail rows extend indefinitely;
- that every recorded tree direction is P-realizable;
- polynomiality away from the represented charts, unless `GLOBAL-CLOSED`
  coefficient arrays are included;
- the required global branch/cv inventory or budget realization; or
- existence of a global Keller counterexample.

A finite-field point is still weaker: it may lie on a characteristic-specific
component and is not a characteristic-zero lift without a separate argument.

### 4.3 Promoted inputs and explicit riders

The system consumes the following source results.

| input | use | rider |
|---|---|---|
| Prop. 8.1(i)-(v), `SHEET6-L1.md:68-81`, `SHEET6-MP-REVIEW.md:162-170` | full/reduced patterns and local ODE | use `h_(m_v)`, not an arbitrary `q` label |
| BOOK R1.0-R1.4, `BOOK-OFFAXIS.md:209-283` | root anatomy and chain transport | R1.2 is the repair for the M-fold ambiguity |
| DEPTH, `SHEET6-DEPTH.md:67-77,142-165,216-233` | `rho,w`, count and nonzero merge handshake | DEPTH alone does not transport reduced coefficients |
| BOOK R2.1/R2.2, `BOOK-OFFAXIS.md:293-325` | merge anatomy and nonzero handshakes | replace the mixed case-III row by E5 |
| E5, `SHEET6-III.md:131-147`, `SHEET6-HIII-REVIEW.md:102-134` | zero-edge update | conditional on `CONJECTURE H5a`; either coherent reading rejects unequal `nu` records |
| St. 3.9/3.17 and St. 8.3, summarized at `SHEET6-TEMPLATE.md:140-154` | chart, degree and full-jet transport | subleading deep coefficients require shallow jet rows |
| Prop. 4.2 | common `h_j` tower | constant-leading-part case is a GAP (`SIGRAY-AUDIT.md:54`) |
| BOOK P1, `BOOK-OFFAXIS.md:486-500` | case-IV `R,psi`, budget and terminal integers | numerical P1 is not coefficient closure |
| LROOT, `SHEET6-LROOT.md:100-126` | one root direction and exact `k_f` | inherits the recorded E9/H2 branch-at-F reading |
| corrected St. 3.12, `SIGRAY-AUDIT.md:44` | x/y root chart swap | literal printed pair is duplicated |

No `CONJECTURE` is allowed to generate a kill without appearing in the
verdict's dependency field.

### 4.4 Wrong-object hazards: fail-closed checklist

An implementation must reject emission when any of these checks fails.

1. **Reduced/full confusion.** St. 3.9 transports `S*p^i` and the full
   patterns of fixed global `h`, not reduced `p,q`.
2. **Tower-label drift.** `q_v` belongs to `h_(m_v)`; `m_v` can change along
   an edge. Never transport two `q` polynomials merely because both are
   called `q` locally.
3. **Edge-name reversal.** Store `rootward,poleward`; never infer direction
   from source letters `F,G`.
4. **Level-offset error.** Compute `N_e=K*(pi_U-pi_L)` from the applicable
   Prop. 9.3 case and assert it is a positive integer. A one-slot shift changes
   which shallow row supplies a deep coefficient.
5. **M-fold `tau` ambiguity.** Do not put `(d_p,d_q)` in lowest terms unless
   the exact R1.2 cancellation has first been proved.
6. **Orbit value versus direction.** `A=c^nu` loses the actual `c` and the
   St. 3.18 root-of-unity branch. Emit `c^nu-A=0`; track any inter-edge
   root-of-unity relation. `SIGRAY-AUDIT.md:52` records the corrected unique
   `epsilon*c` statement.
7. **Missing shallow rows.** A deep top's lower coefficients come from
   shallow subleading rows by (J8). Zero-filling them is an extra equation,
   not a default.
8. **Composite-edge collapse.** Retain every coefficient in (J3); a long edge
   is not the substitution `eta_L=c+z^N*eta_U` unless all intermediate slots
   are proved zero.
9. **Unsafe gauges.** Once vertices are glued, local leading scales are not
   independently normalizable. Set a scale to 1 only after proving a lossless
   global action with nonzero determinant.
10. **Mixed case III.** Never combine BOOK's printed denominator with a free
    unequal characteristic. Every case-III manifest records `printed`, `E5`,
    and selected coherent branch values.
11. **Terminal chart error.** Use (R5), not the literal St. 3.12 duplicate;
    test the sign in (R6) on a planted `J=1` pair.
12. **Cross-fiber twist.** St. 3.14 coefficient alignment may differ by a
    root-of-unity twist (`SIGRAY-AUDIT.md:47`). A single fixed-`a` route does
    not need cross-fiber identification; `GLOBAL-CLOSED` mode must represent
    the twist if it identifies fibers.
13. **Endpoint-summary overclaim.** A minimum state, visible tag, or current
    dedup key is not a route certificate.
14. **Neutral-depth cap.** No cap can replace coverage of an unbounded neutral
    family without a proved invariance theorem.
15. **Solver grammar.** Parentheses in msolve polynomial rows and unreduced
    positive-characteristic coefficients are prohibited by `AUDIT.md`.

## 5. Build plan and acceptance gates

### 5.1 Module and artifact layout

Use an additive layout consistent with `cases/book_offaxis.py` and the current
emitters:

```text
lib/td7_gluing.py
cases/td7_gluing.py
tests/test_td7_gluing.py
systems/td7_gluing/<cell>/<certificate-id>/
    system.ms
    system_p<P>.ms
    system.rows.txt
    manifest.json
runs/td7_gluing/                 # authenticated remote outputs only
```

`lib/td7_gluing.py` owns:

- immutable `Cell`, `Frame`, `Vertex`, `Edge`, `RouteSummary`,
  `RouteCertificate`, `TowerLabel`, `JetWindow`, `Equation`, and
  `NonzeroGuard` records;
- an exact `Fraction` polynomial IR with deterministic variable ownership,
  expansion, denominator clearing, content removal and alpha-renaming;
- the 62-cell local registry, the six positive local witnesses, and the E5
  preflight table;
- predecessor-complete route import and explicit neutral/tower expansion;
- separate constructors for (L3), pole Wronskians, (H1)-(H8), (J6), (T2),
  (R1)-(R6), and guards;
- structural canonicalization and equation hashing only after full assembly;
- characteristic-zero and pre-reduced mod-p emission;
- an independent tiny parser/evaluator, row legend and JSON manifest.

`cases/td7_gluing.py` is a thin CLI with no solver invocation:

```text
inventory | provenance | preflight | anchors | dry-run | emit | guards | manifest
```

Every command exits nonzero on unresolved provenance unless the caller asks
for a named diagnostic prefix. `emit --tier full-route` refuses a summary or
an unresolved tower.

Each manifest records at least: source commit/worktree fingerprint without
running git, cell and certificate IDs, every fixed discrete datum, ground
field/prime, coherent case-III reading, variable order and ownership, equation
number/source, every saturation target, common `K`, all windows, exact
vars/eqs/bytes, completeness label, canonical hash, prime exclusions, and
intended fleet lane.

### 5.2 Implementation milestones

1. **Provenance first.** Reproduce `53/35` and `59/41`, retain all equal-cost
   predecessors, and demonstrate the six existing raw collapses. Emit no
   coefficient rows yet.
2. **Coherent numerical gate.** Reproduce the six local witnesses and the E5
   `PASS,PASS,REJECT,REJECT,REJECT,REJECT` table. Produce the synchronized
   direct certificate of section 3, including all `i` values.
3. **Exact IR and local layer.** Emit the merge-local 62-cell registry and the
   literal 83/74 pilot. Pass exact rational and finite-field anchors.
4. **Chart/tower layer.** Implement (J6) and (T2) on planted microexamples,
   then attach real route tower certificates. Stop rather than infer missing
   Prop. 4.2 data.
5. **Terminal/global layer.** Add root/x-side charts, (R6), optional shared
   global coefficient arrays, canonical equation hash, and fleet manifests.
6. **Remote solve fleet.** Ship only guard-clean artifacts. Bank a verdict only
   after authenticated output validation.

`CONJECTURE (schedule).` Milestones 1-3 fit the prior 3-5 engineering-day
estimate. Milestones 4-5 depend on reconstructing tower/root provenance and
may exceed it; that reconstruction is mathematical work, not emitter polish.

### 5.3 Mandatory regression gates

The test suite must include all of the following.

**G0 — census and provenance**

- exact 62-cell registry and `56 dead / 6 local survivors`;
- filed completion counts `53/35` dedup and `59/41` raw, distributed exactly
  as in section 2.3;
- post-E5 counts `49/31` dedup and `51/33` raw;
- all six raw collapses identified, with (I6)-(I7) proving that visible dedup
  is not equation dedup;
- refusal to emit `FULL-ROUTE` from a `RouteSummary`.

**G1 — six positive local controls**

For every row of section 2.1, reconstruct `p,q`, differentiate in `eta`, and
verify all (L3) coefficients, exact degrees, `C!=0`, `s(0)!=0`, `s(A)!=0`,
squarefreeness and resultants. These are six merge-local controls, not six
certified route systems.

**G2 — 56 law-dead negative controls**

Load the exact tuples from `xmodel/sol-td7-law.md:218-262` or
`xmodel/td7-law-engine-check.md:116-179`. For each, assert

\[
 \mu=d_p-\nu,\quad \ell=(d_q-1)/\nu-1,\quad
 d_p=\mu+\nu,\quad d_q=1+(\ell+1)\nu,
 \quad\gcd(d_p,d_q)=M.                                    \tag{B1}
\]

Build (I2) independently. Before the `C` inverse it must have its unique
forced solution and be satisfiable; that solution has
`C=s(0)=s(A)=0`. After adjoining `u_C*C-1`, exact local elimination must be
empty. Do this in local exact Python; the largest `ell` is only 21. Do not
invent routes for cells already killed locally.

**G3 — E5 and handshake gates**

- reproduce (I3)-(I5) exactly;
- test equal-`nu` agreement on `(9,15)` and `(10,15)`;
- test all four unequal-`nu` rejections;
- force the legacy mixed formula and assert the manifest becomes
  `UNSOUND-FOR-VERDICT`;
- regression-test R1.2 with nonprimitive `(d_p,d_q)` so dropping `M` fails.

**G4 — pilot and jet anchors**

- exact 83 variables/74 rows and a deterministic characteristic-zero hash;
- exact substitution of (P11)-(P13), including every inverse row;
- reduction of the same point at `105337` and independent-parser equality;
- planted elementary/composite (J6) examples in which the deeper top's lower
  coefficient really comes from a shallow subleading row;
- all perturbations listed after (P13);
- a terminal chart/Jacobian sign microtest.

**G5 — emission hygiene**

- unique declared variables; no undeclared variables, zero IR rows, negative
  exponents or nondeterministic ordering;
- no `(` or `)` anywhere in an emitted polynomial body
  (`AUDIT.md:426-439`);
- per-row denominator clearing and content ledger;
- every mod-p coefficient represented in `[0,p)`, every intended row nonzero,
  and exact row/header counts preserved (`AUDIT.md:565-577`);
- independent-parser evaluations of the IR, char-zero text reduced mod `p`,
  and emitted mod-p text at two deterministic points;
- manifest byte/hash/row integrity and fleet coverage exactly once.

### 5.4 Fleet targets and verdict handling

`ops/FLEET.md:3-6` is absolute: never run msolve or another multi-GB solver on
the local Mac. Local exact Python for the triangular controls and planted
anchors is allowed.

- The already-solved 83/74 pilot needs no mathematical solver lane. If a
  parser/solver smoke run is desired, send it alone to **box01**, using
  `-t 2..4`; do not stack larger cores there.
- Send every real tower/jet route system and all parallel route lanes to
  **Box02**, normally `-t 8` with the 43,200-second cap. Resolve its current IP,
  run `sudo ldconfig` after start, inspect lifecycle cron state, and do not
  stop the instance while another queue is active.
- Ship files with `scp`, not inline generated SSH commands. Use the orphan-safe
  `nohup sh -c "timeout ... msolve ...; log rc/bytes/date"` pattern at
  `ops/FLEET.md:29-39`.
- Initial corroboration primes are `105337,105673,200257` only when none is
  excluded by a cleared denominator, route characteristic, derivative
  coefficient or guard. Reduce every coefficient before shipping.
- Preserve input, output, command, host, msolve version, return code, wall
  time and byte count. A 0-byte output is never a verdict.
- Four E5-rejected cells receive manifests but no solver jobs. Queueing them
  is a build-gate failure.

The first solver objective is not “run 53 files.” It is:

1. finish one complete tower certificate for the direct `(9,15)` route;
2. emit its first theorem-complete jet window and controls;
3. solve it on Box02;
4. only after that schema passes, expand the 51 post-E5 raw completion
   records and equation-hash actual duplicates.

## 6. Definition of done

The emitter is ready for mathematical verdicts only when:

- a route manifest contains every item in (F2), including a finite or proved
  invariant treatment of neutral padding;
- every variable and equation is traceable to a numbered item in this design;
- the six positive and 56 negative local gates pass;
- E5 rejects the four inconsistent cells by default;
- the direct pilot reproduces the exact rational point and all negative
  perturbations;
- `FULL-ROUTE` emission includes common tower labels, the required shallow
  jet rows, terminal root/x-side data and (R6); and
- remote output validation follows `AUDIT.md` and `ops/FLEET.md` verbatim.

Until those conditions hold, the mathematically correct deliverable is a
local, leading, or prefix obstruction system with that scope in its filename
and manifest—not a “full coefficient-gluing” verdict.
