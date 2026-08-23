# Coefficient gluing for the td-7 off-axis survivors: design and pilot

Status: **LEAD-PILOT COMPLETE; FULL-ROUTE DESIGN IS GATED ON CERTIFICATE/WINDOW PROVENANCE**  
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
   update, four recorded arrival/cell data are **CONDITIONAL-REJECT** before
   coefficient emission:
   `(15,25,8,5)@7`, `(15,25,12,5)@3`, `(18,27,13,9)@5`, and
   `(39,65,32,13)@7`. The two cells with arrival and merge characteristic
   both equal to 7, `(9,15)@2` and `(10,15)@3`, survive this preflight.
   The arithmetic is in section 2.2.
3. The advertised 53 routes and 35 equality routes are 53/35 deduplicated
   **completion records**, not vertex paths.
   `cases/scratch_offaxis_pricing/px5.py` discards predecessors,
   equal-cost alternatives, some characteristics, and multiplicity
   partitions. The corresponding raw census is 59/41. No coefficient-system
   sharing among the 35 equality records is currently certified.
4. Statement 3.9 pins the multiplicity, deeper top coefficient and valuation
   drop for the full pattern of a fixed global polynomial, not for the
   reduced Prop. 8.1 polynomials `p,q`. Subleading jet rows are related by
   the exact coordinate identity for that same global polynomial. Thus an
   emitter which merely equates the six local `A` parameters is the wrong
   object.

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
kill. The four E5 preflight failures are candidate next-tier eliminations:
every verdict is conditional on the campaign's E5/H5a promoted reading and
is labelled accordingly below.

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
`A*(1+sqrt(2))/3` and `A*(1-sqrt(2))/3`, so individually labelled roots require
`Q(A,sqrt(2))`. No such extension is needed in symmetric-coefficient form.
An edge normally requires `c^nu=A`; retaining both variables keeps the
system over `Q` and represents the union of root-of-unity branches.

The default is **fiber-zero gauge**: replace the original first polynomial
`f_old` by `f=f_old-a` and rename it `f`. If a `MINUS` tower is used, also
replace `g_old` by `g=g_old-b` before defining that tower. These are lossless
target translations, set the selected constants to zero, and do not change
the Jacobian. Thus all default equations remain over `Q`; no algebraicity
assumption on the original complex values `a,b` is being smuggled into
`k_0`. An optional ungauged mode instead declares `a_fiber` and, for MINUS,
`b_fiber`, with distinct labels `fbar=f-a` and `gbar=g-b`. For
`Dint[v,h]=K d_(h,v)` and
`E=max(Dint[v,fbar],Dint[v,f],0)`, the exact Laurent identity

\[
 z^{E-Dint[v,\mathrm{fbar}]}J_{v,\mathrm{fbar}}
 -z^{E-Dint[v,f]}J_{v,f}+a_{\rm fiber} z^E=0.            \tag{F1a}
\]

For MINUS, with `E_g=max(Dint[v,gbar],Dint[v,g],0)`, also emit

\[
 z^{E_g-Dint[v,\mathrm{gbar}]}J_{v,\mathrm{gbar}}
 -z^{E_g-Dint[v,g]}J_{v,g}+b_{\rm fiber}z^{E_g}=0.        \tag{F1b}
\]

The gauge is chosen exactly once, before charts, jets, tower labels, the
Jacobian rescaling and global arrays are defined. Default mode has no
pre-translation constant variables or constraints; ungauged mode emits the
dependency-closed coefficients of (F1a) and, when applicable, (F1b). The
emitter may not silently substitute `f` for `f-a` or `g` for `g-b`.

Use one orientation everywhere:

- `L=rootward` is the shallower vertex;
- `U=poleward` is the deeper vertex;
- an edge is written `L -> U`; one elementary slot has the source relation
  `U=L*c`, while a composite edge owns an ordered elementary-slot sequence or
  a directly certified composite chart.

This avoids the source's letter reversal: Prop. 3.2/St. 3.17 write the deeper
vertex as `F=G+c`, while Prop. 9.3 writes it as `G=F+c`; see
`SHEET6-DEPTH-REVIEW.md:129-132`.

A `RouteCertificate` is not an endpoint `(w,M,lambda)`. It must contain:

\[
\begin{split}
\mathcal R=(&V,E,v_{\rm root},\{v_{{\rm pole},i}\},K);\\
v\in V:\quad&
(\pi_v,\kappa_v,\nu_v,\bar\kappa_v,d_{f,v},i_v,
 d_{p,v},d_{q,v},M_v,\rho_v,w_v,
 \lambda_v^{\rm lb},\lambda_v^{\rm exact},
 \mathsf{lambdaAuthority}_v,\mu_v,k_v),\\
e=(L,U)\in E:\quad&
(\text{case}_e,n_e,\mu_e,\mathsf{chartMode}_e,
 \mathsf{slots}_e\ \text{or}\ \{c_{e,j}\}_{0\le j<N_e},
 \text{zero/nonzero},\text{arrival label},
 \{\text{TransportAuthority}_{e,h}\}_h,
 \mathsf{Derived}(N_e,\{r_{e,h}\}_h)),                    \tag{F2}\\
&\text{the complete }(\epsilon,l,k,(m_j),\ell_{\rm ex})
 \text{ shape at every non-pole vertex},\\
&\text{the global labels }h_0=g\ (\mathrm{PLUS})
 \text{ or }g-b\ (\mathrm{MINUS}),h_1,\ldots,h_m,
 (k_j,l_j),\text{ tower side/base},d_{h_j,v},m_v
 \text{ at every vertex},\\
&\text{root and x-side terminal data, all top-pattern certificates,
 JetWindows/chart slots, and all discrete root-of-unity choices.}
\end{split}
\]

Here `v_root` is the unique root chart and the typed family
`{v_pole[i]}` is the set of pole charts. `lambda_lb` is the proved P0/AF2
lower bound. `lambda_exact` is optional and may be populated only with a
source authority—for example the equality-budget sandwich—not by copying a
minimizing price into a slack route. The tower exponent is not free data:

\[
 \mu_v=\alpha_{m_v}=\sum_{j<m_v}{(k_j-1)l_j\over k_j},
 \qquad k_v=i_v(\mu_v-1)\in\mathbb N .                    \tag{F2a}
\]

The certificate records the source proof of integrality.  This is the
`alpha_m` definition in `SHEET6-TEMPLATE.md:49-55`; omitting `mu_v` would
leave (L1) under-specified.

An `ElementarySlot` is typed as

\[
 s=(v_s,v_{s+1},\pi_s,\pi_{s+1},\kappa_s,c_s,\delta_s,
       \{m_{s,h},\mathsf{topWitness}_{s,h}\}_h),
 \quad \pi_{s+1}-\pi_s={1\over\kappa_s},\quad
 v_{s+1}=v_s*c_s,\quad \delta_s=K/\kappa_s.              \tag{F2b}
\]

For `chartMode=EXPANDED_SLOTS`, the ordered sequence must start at `L`, end
at `U`, and match adjacent endpoints and levels. `K`, `delta_s`, `N_e` and
`r_(e,h)` are derived/verified fields, never mutually independent user
inputs. Direct `ELEMENTARY` mode has one slot; a theorem-certified composite
mode may instead carry the complete chart coefficients and its named
authority.

Here

\[
 \bar\kappa_v=\kappa_v(1-\pi_v),\qquad
 X_v=d_{f,v}/i_v,\qquad
 \rho_v={d_{f,v}\over\deg p^{\rm full}_{f,v}}
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
| `A[v,r]`, `B[v,s]`, `Q[v,r]` | incoming p-orbits, non-chain p-orbits, and q-only orbits in `t=eta^nu`; every `A` and `B` orbit occurs once in `q`, while only `Q` is q-only |
| `c[e,j]` | actual continuation and intermediate composite-chart coefficients; `c[e,0]` is the first direction |
| `d[e]` | optional derivative/Taylor auxiliary for a nonzero orbit direction |
| `S[v,h]` | leading scale of the full top pattern of the fixed global polynomial `h` at `v` |
| `J[v,h,r,eta_deg]` | coefficient of `eta^eta_deg` in jet row `P[v,h,r](eta)` |
| `tower_s[j]` | global approximate-root/tower constant in `h[j+1]=h[j]^k-tower_s[j]*base[j]^l`, with certified base `f` or `f-a` |
| `a_fiber`, `b_fiber` | optional selected f/g-fiber values in ungauged mode (`b_fiber` occurs only for MINUS) |
| `gamma` | optional nonzero constant Jacobian before the default target rescaling |
| `Fcoef[i,j]`, `Gcoef[i,j]` | optional global coefficients of `f,g` on a certified finite support, for `GLOBAL-CLOSED` mode |
| `u[tag]` | a fresh Rabinowitsch inverse for one forced-nonzero polynomial |

Every variable has exactly one owner in the manifest. An orbit value `A`, an
actual direction `c`, a leading scale `S`, and a tower constant `s` are four
different objects and may not share a variable merely because a local gauge
could normalize one of them.

Serialized names are injective by construction: in particular use
`tower_s[j]` for global tower constants and `local_s[v,j]` for coefficients
of a local q-extra polynomial. Mathematical subscripts do not authorize
textual name reuse.

A recorded root-of-unity choice is algebraic data, not a string tag. It is
represented over `Q` by a variable `eps[e]`, the exact polynomial defining
the allowed order (`Phi_M(eps)=0` for primitive order `M`, or
`eps^M-1=0` when all M-th roots are allowed), and the equations

\[
 \Phi_M(\epsilon_e)=0\ \text{ or }\ \epsilon_e^M-1=0,
 \qquad c_{e_2}-\epsilon_ec_{e_1}=0.                     \tag{F5}
\]

Alternatively a manifest may enumerate branches over
a declared number-field minimal polynomial. A fixed unrecorded complex
`epsilon`, or a direction relation stated only after passing to `A=c^nu`,
fails closed.

### 1.3 Local Prop. 8.1 equations

At a non-pole `v`, Prop. 8.1(i),(ii),(iv),(v) gives

\[
 p^{\rm full}_{f,v}=S_{v,f}p_v^{i_v},\qquad
p_{h_{m_v},v}=S_{v,h_m}p_v^{k_v}q_v,
 \qquad k_v=i_v(\mu_v-1),                                \tag{L1}
\]

These are emitted equations, not notation. With the jet convention (J1),
either inline the right sides as row-zero expressions or, in the default
explicit-IR mode, emit coefficientwise

\[
 [\eta^a]\bigl(P_{v,f,0}-S_{v,f}p_v^{i_v}\bigr)=0,
 \qquad
 [\eta^a]\bigl(P_{v,h_{m_v},0}
       -S_{v,h_m}p_v^{k_v}q_v\bigr)=0                    \tag{L1a}
\]

for every coefficient, plus the corresponding certified pole and root
top-pattern equations. A non-pole `FULL-ROUTE` system without (L1a) is
disconnected and invalid.

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
 \prod_e(\eta^{\nu_v}-A_{v,e})
 \prod_j(\eta^{\nu_v}-B_{v,j})
 \prod_r(\eta^{\nu_v}-Q_{v,r}).                         \tag{L6}
\]

A zero arrival contributes `eta^mu0`, not a nonzero orbit. The emitter must
check, before creating rows,

\[
 \mu_{v,e}d_{q,v}>d_{p,v},\quad
 m_{v,j}d_{q,v}<d_{p,v},\quad
 d_{p,v}\ne m^*d_{q,v}\ \text{for every root multiplicity }m^*\text{ of }p_v,
 \quad M_v=\gcd(d_{p,v},d_{q,v}),\quad\gcd(M_v,\nu_v)=1. \tag{L7}
\]

These are BOOK R2.2, `BOOK-OFFAXIS.md:317-325`, plus R1.0 at lines
209-224. Root separation, nonzero orbit values, squarefreeness, relevant
resultants, and `C_v` are open conditions. Each is internalized as

\[
                              u_g g-1=0                   \tag{L8}
\]

with a fresh `u_g`. No solver-side saturation is assumed.

The guard builder first creates a typed `RequiredNonzero` registry, then
requires an exact registry-to-guard-or-implication coverage audit. It includes:

- every orbit value required away from zero, and every pairwise difference
  among distinct `A,B,Q` orbit values required by the pattern;
- the discriminant of the squarefree orbit radical and of `q`, plus each
  theorem-required resultant or q-only evaluation;
- every `C_v`, actual nonzero continuation, allocated full-pattern scale,
  `tower_s[j]`, retained `gamma`, and variable exact-degree leading
  coefficient; and
- every pole/root open condition named by its `TopPatternCertificate`.

Never guard `disc(p_v)` when (L5) prescribes repeated factors: it then
vanishes on the intended family. Guard its squarefree radical/orbit factors
instead. Default mode assigns one inverse and row to every required target;
an optional product guard must preserve the factor-to-target ledger and is
accepted only when the product is proved equivalent. A missing or extraneous
guard is a build failure, not a solver option. The only default implication
discharge is a continuation (and its characteristic-zero derivative) proved
nonzero by guarded `A!=0` plus (L9); the manifest records that proof edge.

For each nonzero edge direction attached to incoming orbit `A[L,e]`, emit

\[
 c_{e,0}^{\nu_L}-A_{L,e}=0,
 \qquad d_e-\nu_Lc_{e,0}^{\nu_L-1}=0                     \tag{L9}
\]

when the derivative auxiliary is requested; otherwise inline the second
expression in the exact Taylor coefficient. The `A` guard and first equation
already force `c_(e,0)!=0`. A zero arrival has certified direction zero and
does not receive (L9) or a nonzero-direction guard.

At a pole, Prop. 8.1 is replaced by the Prop. 5.3 pole Wronskian and fixed
pole degrees. Every live label at a pole or root is supplied by a typed

```text
TopPatternCertificate(vertex,label,source,degree,
                      exact_factored_or_sparse_polynomial,
                      leading_scale,required_nonzero,coefficient_oracle)
```

and is tied coefficientwise to `J0` or installed as its `TopOracle`. The pole
constructor additionally receives the exact Prop. 5.3 `(p,q)` template,
Wronskian normalization and degrees; it creates raw coefficient rows, then
applies only the per-row primitive/sign normalization of section 2.3. The root constructor receives the exact top
polynomial for every live `f,g,h_j` label, not only a numerical degree. A
missing label returns `UNRESOLVED-TOP-PATTERN`. In particular, a pole must not
be assigned a reduced `q_v` belonging to an arbitrary terminal tower member.

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

For the `mu_e=1` DEPTH handshake this specializes to the exact conserved
arrival invariant

\[
 \bar\kappa_G-X_G=w_U,qquad
 \bar\kappa_G={w_Ud_{q,G}\over d_{q,G}-d_{p,G}},\quad
 X_G={w_Ud_{p,G}\over d_{q,G}-d_{p,G}},\quad
 \rho_G={w_U\over d_{q,G}-d_{p,G}}.                       \tag{H4a}
\]

Thus every all-`mu=1` nonzero arrival at the same merge has the same `w`.
This is `SHEET6-DEPTH.md:142-165,216-233`; it is a numerical handshake, not
a coefficient identification.

For a zero case-III arrival, do **not** emit BOOK's old mixed formula.
With E5/H5a and `G` rootward, `U` poleward,

\[
 d_{f,G}={\nu_Gd_{f,U}+n_e\deg p^{\rm full}_{f,U}\over\nu_U},
 \qquad
 \bar\kappa_G={\nu_G\bar\kappa_U+n_e\over\nu_U},         \tag{H5}
\]

and hence

\[
                 X_G=\mu_0(\bar\kappa_G-\nu_Gw_U).        \tag{H6}
\]

BOOK R2.1 and `cases/scratch_offaxis_pricing/px5.py` instead use
`nu_U*w_U`. The formulas coincide only
when `nu_G=nu_U`; section 2.2 applies this mandatory branch check.

The coefficient layer additionally requires the St. 3.9/3.17/8.3 count
equalities, with their hypotheses recorded rather than generalized. On one
**elementary** chart step, St. 3.9 gives, for every fixed global `h`,

\[
 \deg p_{h,U}=\operatorname{mult}(p_{h,L},c_e).            \tag{H7}
\]

Across a composite vertex edge, St. 3.17 supplies (H7) for `h=f-a`, and
St. 8.3(ii) supplies it only for a common live tower label `h_j`,
`j<=m_U`, under that statement's hypotheses. For any other label the route
must either expand the edge into elementary certified slots or omit that
transport and downgrade the system. For `h=f-a`, (L1) makes (H7)

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

Each elementary chart slot carries the suitable ramification `kappa_e` from
Prop. 3.1/Statement 3.9. Define

\[
 K_0=\operatorname{lcm}\bigl(\{\kappa_e\}_e,
   \{\operatorname{den}\pi_v\}_v,
   \{\operatorname{den}d_{h,v}\}_{v,h}\bigr).             \tag{J0}
\]

The certificate supplies a common `K`, a positive multiple of `K0`, together
with a Prop. 3.1 suitability witness for every chart; canonical mode chooses
the least certified multiple. Merely clearing denominators is insufficient.
Put `z=x^(-1/K)` and assert every `K*pi_v`, `Dint[v,h]=K*d_(h,v)`, edge
offset and valuation drop below is integral. For an elementary slot set
`delta_e=K/kappa_e`; its native coordinate is
`zeta_e=x^(-1/kappa_e)=z^(delta_e)`.

For every global polynomial label `h`, write the **formal, untruncated**
top-down jet at `v` as

\[
 h=x^{d_{h,v}}J_{v,h}(z,\eta_v),\qquad
 J_{v,h}=\sum_{r\ge0}z^rP_{v,h,r}(\eta_v),
 \qquad P_{v,h,0}=p_{h,v},                                \tag{J1}
\]

where the equality in (J1) is enforced by (L1a), by its pole/root analogue,
or by syntactic inlining. It is never an unasserted alias.

For an elementary rootward-to-poleward step, St. 3.9 uses

\[
             \eta_L=c_e+z^{\delta_e}\eta_U
                    =c_e+\zeta_e\eta_U.                   \tag{J2}
\]

For a composite edge of `N_e=K*(pi_U-pi_L)` global `z`-grid units, retain all
intermediate chart coefficients:

\[
 \eta_L=C_e(z)+z^{N_e}\eta_U,\qquad
 C_e(z)=c_{e,0}+c_{e,1}z+\cdots+c_{e,N_e-1}z^{N_e-1}.      \tag{J3}
\]

In `EXPANDED_SLOTS` mode this polynomial is not independently guessed. If
`slots_e=(s_0,...,s_(q-1))`, put

\[
 D_s=\sum_{u<s}\delta_u,\qquad
 N_e=\sum_{s=0}^{q-1}\delta_s=K(\pi_U-\pi_L),\qquad
 C_e(z)=\sum_{s=0}^{q-1}c_s z^{D_s},                      \tag{J3a}
\]

and certify every other common-grid coefficient zero. For every transported
label,

\[
 r_{e,h}=\sum_s m_{s,h}\delta_s
         =K(d_{h,L}-d_{h,U}).                              \tag{J3b}
\]

The composer checks every per-slot relation in (F2b), endpoint/level
matching, every elementary top witness, (J3a), (J3b), and the final `J_U`
owner before granting
`TransportAuthority=EXPANDED_SLOTS`.

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

For every transported pair `(e,h)`, define and verify the integral valuation
drop

\[
 r_{e,h}:=K(d_{h,L}-d_{h,U})\in\mathbb N.                 \tag{J5}
\]

The exact coordinate identity is

\[
 J_{L,h}\bigl(z,C_e(z)+z^{N_e}\eta\bigr)
       -z^{r_{e,h}}J_{U,h}(z,\eta)=0.                     \tag{J6}
\]

For one elementary step, St. 3.9 proves
`r_(e,h)=m_(e,h)*delta_e`, where
`m_(e,h)=mult(P_(L,h,0),c_(e,0))=deg P_(U,h,0)`. For a
composite edge, `r_(e,h)=m_(e,h)N_e` may be asserted only for `f-a` under
St. 3.17, or for a common live tower label under St. 8.3(ii), with the
applicable hypotheses stored in the certificate. Otherwise materialize the
elementary slots and obtain `r_(e,h)` as the sum of their elementary
valuation drops `sum_s m_(s,h)*delta_s`. A `TransportAuthority` enum
`ELEMENTARY | ST3.17_F | ST8.3_LIVE | EXPANDED_SLOTS` is mandatory for each
emitted `(e,h)` block; `NONE` fails closed.

The identity (J6) is the exact change of coordinates between expansions of
the same global `h`; it is not a claim that St. 3.9 directly supplies every
subleading row. Once that common-object identity and the elementary chart are
licensed, coefficient comparison gives the low-slot divisibility conditions

\[
 P_{L,h,s-j\delta_e}^{(j)}(c_e)=0
 \quad\left(0\le s<r_{e,h},\ 0\le j\le
       \left\lfloor{s\over\delta_e}\right\rfloor\right), \tag{J7}
\]

and the deep rows

\[
 P_{U,h,t}(\eta)=
 \sum_{j=0}^{\lfloor(r_{e,h}+t)/\delta_e\rfloor}
 {P_{L,h,r_{e,h}+t-j\delta_e}^{(j)}(c_e)\over j!}\eta^j.
                                                                    \tag{J8}
\]

Thus the leading coefficient of `P_U,0` is the `m`-th Taylor coefficient
of `P_L,0`, but its lower coefficients come from lower shallow jet rows.
This is exactly why equating reduced local `A_v` values is unsound.
Factorials in (J8) are cleared row by row before emission and entered in the
prime-exclusion ledger.

A finite emitter never replaces (J1) by a truncated series. Instead every
`JetWindow` stores

\[
 \mathcal W_{v,h}=(\mathsf{Allocated}_{v,h},
   \mathsf{CertifiedZero}_{v,h},\mathsf{TopOracle}_{v,h}), \qquad
 \Omega_B\subset\mathbb Z\times\mathbb N,                \tag{J9}
\]

for each equation block `B`. `Allocated` is the exact finite set of
subleading coefficient indices `(r,a)` for variables
`[z^r eta^a]J_(v,h)`; `CertifiedZero` contains only indices ruled out by a
recorded degree/support theorem; `TopOracle` returns exact coefficients of
the factored or sparse row zero; and `Omega_B` is the exact set of output
`(z,eta)` coefficients to emit. For every `omega in Omega_B`, the IR computes
the full dependency set `Dep_B(omega)`. Each dependency must be an allocated
variable, a row-zero oracle value, or a certified zero. An unknown omitted
coefficient produces `UNRESOLVED-WINDOW`; it is never substituted by zero.
The block emits

\[
 \{[z^s\eta^a](\text{full identity})=0:
                         (s,a)\in\Omega_B\}.              \tag{J10}
\]

This rule applies equally to (J6), (T2), (F1a), (F1b) and (R6), including every
product convolution and derivative shift. A simple sufficient recurrence
bound for an elementary child band `0<=t<=B_U` is
`B_L>=r_(e,h)+B_U`, but the dependency audit—not that scalar bound—is the
acceptance condition.

Default `INLINE-J0` allocates no dense row-zero coefficient variables:
(L1) and certified pole/root top polynomials form `TopOracle`, which expands
only coefficients requested by a dependency set. Its emitted result is still
an expanded polynomial; factor syntax never reaches msolve. Optional
`DENSE-J0` allocates and counts every row-zero coefficient and emits (L1a).
For the pilot's degree 203490, pretending dense row zero costs nothing would
under-count by at least 203491 coefficients at one vertex alone.

The manifest records every support, projection and dependency hash. A
partial projection is labelled `PREFIX`. `FULL-ROUTE` requires dependency
closure for every finite cancellation, tower and terminal band demanded by
the certificate; it never means that an unknown formal tail was set to zero.

### 1.6 Tower identities and common global objects

The certificate carries `tower_side in {PLUS,MINUS}`, the initial label and a
base polynomial `base_j`. Prop. 4.2 on `T_a^+` starts at `g` and uses `f`;
Prop. 4.3 on `T_a^-` starts at `g-b` and uses `f-a`:

\[
 h_0=\begin{cases}g,&T_a^+,\\ g-b,&T_a^-,\end{cases}
 \quad h_{j+1}=h_j^{k_j}-\sigma_j\operatorname{base}_j^{l_j},
 \quad \operatorname{base}_j=
 \begin{cases}f,&T_a^+,\\ f-a,&T_a^- .\end{cases}       \tag{T1}
\]

In the default fiber-zero gauge of section 1.1, a MINUS tower translates both
constants first and is then represented with `h0=g,base=f`; the source-side
tag is still retained because it licenses a different proposition. In
ungauged mode the emitter allocates `fbar,gbar`, enforces (F1a)-(F1b), and
selects both `h0` and `base` literally from (T1).

Prop. 4.3 also requires its condition (7): the chosen
`(g-b)^+_F` is not constant. Every MINUS authority therefore carries a
`TopPatternCertificate` at the licensing vertex proving

\[
 Dint[F,\mathrm{gbar}]\ne0
 \quad\text{or}\quad \deg_\eta p_{\mathrm{gbar},F}>0.     \tag{T0}
\]

Indeed `(g-b)^+_F=xi^(d_(gbar,F))*p_(gbar,F)(eta)`; only
`Dint=0` **and** eta-degree zero is constant. Translation/rescaling preserves
this property. A constant or missing top returns `UNRESOLVED-PROP4.3` and no
(T2) rows.

Let `Dint[v,h]=K*d[h,v]` and
`E=max(Dint[v,h[j+1]],k_j*Dint[v,h[j]],l_j*Dint[v,base[j]])`. The normalized jet
equation at each vertex is

\[
 z^{E-Dint[v,h_{j+1}]}J_{v,h_{j+1}}
 -z^{E-k_jDint[v,h_j]}J_{v,h_j}^{k_j}
 +\sigma_jz^{E-l_jDint[v,base[j]]}J_{v,base[j]}^{l_j}=0.  \tag{T2}
\]

Only the dependency-closed projection `Omega_T2` from (J9)-(J10) is emitted.
The same global `sigma_j` (serialized `tower_s[j]`) is used at every vertex. A local terminal `q_v` is attached only to
the global label `h_{m_v}` justified by the certificate through (L1); the
terminal member may change with `v`. `SIGRAY-AUDIT.md:54` records a GAP in
Prop. 4.2 for a constant leading part. A route encountering that situation
must stop as `UNRESOLVED-PROP4.2`; it may not invent `l_j>0`.
The `f-a` substitution is legal on a `PLUS` tower only after recording and
testing the global shift gauge `a_fiber=0`. Confusing the two bases changes
subleading bands and can produce a false kill; this exact bug is documented
at `SHEET6-LT-REVIEW.md:301-317`.

`GLOBAL-CLOSED` additionally requires a `GlobalSupportCertificate` containing
finite monomial supports for `f,g`, exact degree/leading conditions, one
coefficient variable per support element, and a dependency-closed chart
projection equating the expansion of those same arrays to every route jet.
This is the strongest way to prevent different branches from describing
unrelated formal polynomials. The repository supplies no such finite support
certificate, so `GLOBAL-CLOSED` is **UNIMPLEMENTED in v1** and must fail
closed rather than infer a Newton rectangle. A lighter `FULL-ROUTE` mode
shares jets and tower labels on the certified route and is a necessary
obstruction system, but its nonemptiness does not prove global polynomiality.

### 1.7 Terminal and Jacobian closure

For the last y-side vertex `G`, BOOK P1 (`BOOK-OFFAXIS.md:486-500`) gives

\[
 {d_{(0,y)}\over\deg p^{\rm full}_{f,G}}
 ={\rho_G+\nu_G-\bar\kappa_G\over\nu_G}=1-w_G,             \tag{R1}
\]

\[
 R_{\rm term}={1\over1-w_G},\qquad
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

`SIGRAY-AUDIT.md:44` is the chart-label erratum; the four rectangle
equalities used in (R5) are supplied by Lemma 2.1 as recorded at
`SHEET6-H3.md:99-103`. Equations (J6) are imposed
on the terminal edge for every live tower label. Terminal closure is not just
the numerical P1 check: the x-side/root tower certificate must supply the
patterns demanded by (R5).

Finally impose the Keller identity on the shared `f,g` jets. The thesis
normalization is `J_(x,y)(f,g)=gamma` with `gamma in C*`. The default applies
the lossless target rescaling `g -> gamma^(-1)g` after the applicable
f/g-fiber translations and sets `gamma=1`; ungauged mode retains `gamma` and
saturates it. Perform this
choice once before tower labels/top certificates are created and transform
their scales consistently. Since `eta=x^pi(y-tail)` and
`z=x^(-1/K)`, one has

\[
 J_{x,y}(f,g)=x^\pi J_{x,\eta}(f,g)=\gamma.
\]

Write the **full Laurent functions**, not just their normalized jets, as

\[
 f=z^{-Dint_f}J_f(z,\eta),\qquad
 g=z^{-Dint_g}J_g(z,\eta),
\]

Then, in a fixed chart orientation,

\[
\begin{split}
 &z^{K+1}(J_{f,\eta}J_{g,z}-J_{f,z}J_{g,\eta})\\
 &\quad+z^K(Dint_fJ_fJ_{g,\eta}-Dint_gJ_{f,\eta}J_g)
       -K\gamma z^{K\pi+Dint_f+Dint_g}=0 .                \tag{R6}
\end{split}
\]

The second line contains the prefactor-derivative terms and may not be
dropped. Clear any remaining Laurent power and emit all coefficients in the
certified window. Before expansion assert
`Dint_f,Dint_g,K*pi in Z`; if `K*pi+Dint_f+Dint_g` or a shifted row exponent is negative,
clearing means a formal coefficient-index shift—`z` is bookkeeping, not an
msolve variable. Window propagation must include both derivatives and both
prefactor shifts. The sign, target rescaling, and chart orientation receive a
planted `f=x,g=y,eta=x^pi*y` unit test: then
`(Dint_f,Dint_g,J_f,J_g)=(K,-K*pi,1,eta)` and (R6) reduces to
`K*z^K-K*z^K=0`. If the route has no x-side/root tower data, the
emitter stops at `LEAD-PILOT` or `PREFIX`; it must not silently call P1 alone
a closed coefficient system.

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

### 2.2 Mandatory E5 preflight: four conditional legacy rejections

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
| `(15,25,8,5)` | 7 | `(2/21,48)` | 8 | `(5,3)` | `5/9` | **CONDITIONAL-REJECT (H5a)** |
| `(15,25,12,5)` | 3 | `(1/2,8)` | 12 | `(5,3)` | 8 | **CONDITIONAL-REJECT (H5a)** |
| `(18,27,13,9)` | 5 | `(2/15,39)` | 13 | `(6,4)` | `5/3` | **CONDITIONAL-REJECT (H5a)** |
| `(39,65,32,13)` | 7 | `(2/21,48)` | 32 | `(5,3)` | `29/9` | **CONDITIONAL-REJECT (H5a)** |

This is a proved algebraic contradiction conditional on `CONJECTURE H5a` and
the promoted E5 correction. Under the other coherent reading—printed (g),(h)
together with the definitions—the printed formulas force `nu_G=nu_U`, so
the same four records are conditionally rejected under the selected coherent
reading. Only the old mixed engine reading keeps
`nu_U` free while using the printed denominator; that mixture corresponds to
neither Notation 3.5 value (`SHEET6-HIII-REVIEW.md:107-128`).

Default implementation policy, conditional on `CONJECTURE H5a`/the selected
coherent case-III reading:

- write a `CONDITIONAL-REJECT` manifest containing (I3)-(I5) for these four legacy
  arrival/cell records;
- emit no msolve job for them;
- retain a `--legacy-mixed-iii` diagnostic mode only for reproducing the old
  route book, with `UNSOUND-FOR-VERDICT` stamped into every artifact.

Conditionally filtering the **legacy mixed-reading records** through this
gate leaves 49
deduplicated records, 31 at budget equality, or 51 raw records, 33 at
equality. These belong to the two passing legacy cells and are still not
concrete-route counts. They are not a complete E5-corrected book: E5 changes
the case-III class-B/class-C construction itself, so a fresh coherent enumeration could add
different cells or routes. The complete corrected census is **UNKNOWN**.

The corrected enumerator must not replace the old `nu` cap by a new guessed
cap. There is a cap-free inversion for the one-orbit class-C branch. Fix a
reachable chain-2 state `(r,M_U)` with `r=w_U>0`, and `m=mu0>=2` with
`m|M_U`. Under P3's one-orbit classification
(`BOOK-OFFAXIS.md:521-549`; `xmodel/sol-td7-law.md:65-90`), put

\[
 g=\nu_G\ge2,\quad d_p=m+g,\quad d_q=d_p+c,
 \quad c\in\mathbb N^*,\quad g\mid m+c-1.                 \tag{I5a}
\]

Combining (I4), (I5) and the slope equation gives

\[
 c(g)={2(m-1)(m+g)\over m(gr-2)},\qquad
 g(c)={2m(c+m-1)\over cmr-2(m-1)}.                       \tag{I5b}
\]

Positivity is `gr>2`. Let
`g0=max(2,floor(2/r)+1)`. On `g>=g0`, `c(g)` is strictly decreasing,

\[
 c'(g)={-2(m-1)(mr+2)\over m(gr-2)^2}<0,
 \qquad \lim_{g\to\infty}c(g)={2(m-1)\over mr}.           \tag{I5c}
\]

Hence every solution has integer `c` in the finite interval

\[
 {2(m-1)\over mr}<c\le c(g_0),                            \tag{I5d}
\]

and (I5b) supplies its unique candidate `g`. Test exact integrality,
`g>=g0`, integral `bar_kappa>2`, (I5a),
`M_G=gcd(m+g,m+g+c)>=2`, `gcd(bar_kappa,g)=1`, arrival
legality, local T1/admissibility, and trunk/budget conditions.

**Conditional theorem.** Equations (I5a)-(I5d) are a proved exhaustive
finite enumeration for one fixed reachable state, conditional on
`CONJECTURE H5a`/E5 and P3's promoted one-orbit class-C classification. They
do not prove that the reachable-state family itself has been completely
enumerated.

Class B (`m=1`) must also be regenerated. Corrected H6 and the chain-1
handshake give `g*r=2`; therefore retain a state only if `g=2/r` is an
integer at least 2. Then `d_p=1+g`, `g|c`, and

\[
 \bar\kappa=2+{2(1+g)\over c},                            \tag{I5e}
\]

so it suffices to enumerate the divisors `c|2(1+g)` which are divisible by
`g`, then apply the same gates. Every other P3 case-III branch, including the
chain-1-at-zero exclusion, is rerun under coherent E5. The old loops at
`cases/scratch_offaxis_pricing/px5.py:123-150,229-252` use `nu_U`, not
`nu_G`, and are regression fixtures rather than a completeness proof.

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

The remaining 18 `(10,15)` records are slack. Five have trunk cost 1,
total cost 3:

```text
(w,M,psi)=(2/3,3,2) (4/7,7,2) (2/7,7,1) (2/9,9,1) (4/9,9,1)
```

Thirteen have trunk cost 2, total cost 4 and `psi=1`:

```text
(1/2,2) (1/2,4) (1/3,3) (1/3,6) (2/11,11) (2/13,13)
(2/15,15) (2/17,17) (2/5,5) (4/11,11) (4/13,13)
(4/15,15) (4/17,17)
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
small arrival set (`cases/scratch_offaxis_pricing/px5.py:63-87`),
`trunk_routes` retains only `(cost,psi,w,M)` (`:98-112`), and the final key
ignores the current `M2` (`:254-262`). In addition,
`cases/scratch_offaxis_pricing/px2.py:66-76` omits the free `nu` from pure-b
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
is normalized-IR equality, never inferred ideal equivalence. Canonicalization
is exact and deterministic:

1. alpha-rename variables from the lexicographically ordered typed-owner
   records;
2. expand and combine monomials in the fixed emitted variable/monomial order;
3. per row, clear by the positive LCM of denominators, divide by integer
   content, and choose the sign so the first nonzero coefficient is positive;
4. serialize sorted monomials, sort the resulting polynomial multiset, and
   hash both it and the owner/schema manifest.

Gauge quotienting is `OFF` by default. If enabled, the certificate names a
proved global action, its nonzero determinant hypotheses, guarded pivot,
normalization equations and inverse map; otherwise the ungauged IR is hashed.

### 2.4 Stage-0 route expansion and infinite provenance families

There are two deliberately different graph products.

- `LEGACY-REPLAY` retains every predecessor attaining the filed minimum cost
  and reproduces the 53/59 summaries. It is a regression mode, not theorem
  coverage.
- `COVERAGE` retains every budget-feasible positive-cost stratum, keyed at
  least by `(w,M,spent)` plus full discrete provenance, for every
  `spent<=6-psi`, and every finite zero-cost clean-resonant predecessor.
  The td-7 budget makes charged depth finite. Zero-cost SCCs, neutral padding
  and free-characteristic families remain symbolic.

The distinction is essential for the 18 slack `(10,15)` records: a dearer
predecessor can still fit the terminal budget and produce a different
coefficient system. Dijkstra minima suffice only where a proved equality
sandwich excludes extra charge.

For each branch, instantiation proceeds in this order.

1. Re-run the appropriate graph mode, retaining the exact step cell,
   `nu,epsilon,l,k,(m_j),ell_ex`, edge `n`, arrival type, current `M`, spent
   charge and terminal path. An arrival is a coupled object
   `(nu_U,M_U,spent,path_id)`; never join a set of arrival characteristics to
   an unrelated scalar `dist[(w,M)]`. The latter under-pricing bug occurs in
   `cases/scratch_offaxis_pricing/px5.py:81-84,230-250`.
2. Represent identity self-loops, neutral-padding families, and
   free-characteristic pure-b transitions symbolically; do not unfold any of
   them to an artificial cap. A specialization fixes all discrete parameters
   and yields one finite `RouteCertificate`.
3. Apply the coherent Prop. 9.3 case classification and E5 preflight before
   selecting local coefficients. Store `lambda_lb` and its authority; store
   `lambda_exact` only when proved. A slack allocation or additional cv
   inventory not fixed by the branch returns `UNRESOLVED-BUDGET-INVENTORY`
   for a full completion claim, although an explicitly independent necessary
   prefix may still be emitted with that scope.
4. Apply (H7)-(H8) to `f-a` and to each common live label for which St. 8.3
   applies. Attach a `TransportAuthority` to every `(edge,label)` block;
   expand into elementary slots or fail closed for any other requested label.
   Attach an exact integer `i_v` at every vertex.
5. Expand every zero-cost neutral step needed for degree synchronization.
   Record its actual characteristic and pattern; a state-level
   `neutral-drop` tag is insufficient.
6. Attach complete tower labels, top-pattern certificates, cancellation
   levels and `JetWindow` projections. If they cannot be deduced from
   promoted statements, return `UNRESOLVED-TOWER` or `UNRESOLVED-WINDOW`.
7. Choose and certify common `K` by (J0), compute every `delta_e,N_e,r_eh`,
   and retain the entire chart polynomial (J3).
8. Assemble local, transport, tower, terminal and guard rows. Only now
   canonicalize and hash.

Production coverage may not inherit the exploratory caps
`k in range(0,7)` or `ell_ex in range(0,41)` from
`cases/scratch_offaxis_pricing/px2.py:82-88`, `NCAP=400` from
`cases/scratch_offaxis_pricing/px5.py`, or
`PCAP_STATES=4000`, numerator `10^4`, and `M>200` cutoffs from
`cases/book_offaxis.py:598-621`. Legacy replay may retain them only to match a
filed fixture. Coverage must instead record the budget proof bounding charged
NE orbits, the P0 Diophantine stopping inequality
`2*C_shape<=l*num(w)*T` (source `C`) for `ell_ex`, and the closed tail
inversion. A boundary cap
or OPEN-superset diagnostic is never a completeness certificate.

The uncharged clean part has its own termination proof. For an R1.2 clean
resonant edge with `n>=2`,
`Delta=(n-1)*nu+1`, `nu>=2`, so `n<Delta`; integrality gives
`Delta|num(w)`, and the numerator of
`w'=w*n/Delta` strictly decreases even before final fraction reduction. The
`n=1` clean/neutral case fixes `w` and belongs to the symbolic SCC/M-divisor
family. Thus charged budget, strict numerator descent, dirty Diophantine
stopping and symbolic neutral/pure-b families are separate required
termination certificates.

There are two independent finiteness boundaries. Zero-cost neutral vertices
can be inserted without changing `(w,M,lambda)`, while multiplying full
pattern degrees. In addition, a positive-cost pure-b transition can have free,
unbounded characteristic while retaining the same visible state and price;
`cases/scratch_offaxis_pricing/px2.py:66-76` omits that `nu` from its tag. The certified `(9,15)` endpoint
already represents such a family: `F3` with `nu=5` is one explicit
representative, not a universal pin (`xmodel/sol-sixcells.md:320-324`).
If both branches are padded, a single endpoint summary can also represent
unbounded synchronized full degrees. Exponents are discrete and cannot be
made symbolic in msolve.

`CONJECTURE (neutral-insertion invariance).` After eliminating chart and
scale variables, inserting a clean neutral cell does not change the decisive
coefficient eliminant. No promoted result proves this. Until it is proved,
the emitter is complete only for an explicitly supplied finite
`RouteCertificate`; emptiness for one minimal representative does not kill
all neutral paddings of an endpoint summary. There must be no depth cap
masquerading as coverage.

`CONJECTURE (pure-b characteristic invariance).` The decisive eliminant of a
pure-b transition is independent of its free characteristic after a suitable
orbit reparametrization. This is distinct from neutral insertion and is also
unproved. A finite `RouteCertificate` fixes one concrete characteristic; an
EMPTY result for the pilot's `nu=5` representative does not kill the whole
endpoint family without this theorem or a separate parametric proof.

### 2.5 Honest size accounting

Only merge-local sizes are exact before Stage 0. With monic `s`, the variables
`(A,s_0,...,s_(ell-1),C)` number `ell+2`, and (I2) has `ell+1` nontrivial
coefficient rows. One combined nonzero guard adds one variable/row; individual
auditable guards add more.

| cell | E5 default fate | exact factored merge-local vars/eqs | naive unnormalized dense-eta local vars/eqs | route-level information currently justified |
|---|---|---:|---:|---|
| `(9,15,7,3)@2` | emit | `3/2` | `27/23` | direct synchronized `LEAD-PILOT`: **83/74**, section 3; full jets UNKNOWN pending tower/window certificate |
| `(10,15,7,5)@3` | emit | `3/2` | `28/24` | full paths UNKNOWN pending Stage 0; one equality suffix has the exact dense local-only subtotal `2610/2590` |
| `(15,25,8,5)@7` | conditional reject (H5a) | `4/3` | `43/39` | no default solver system under coherent-III policy |
| `(15,25,12,5)@3` | conditional reject (H5a) | `3/2` | `43/39` | no default solver system under coherent-III policy |
| `(18,27,13,9)@5` | conditional reject (H5a) | `3/2` | `48/44` | no default solver system; dedup branches differ as (I6)-(I7) |
| `(39,65,32,13)@7` | conditional reject (H5a) | `3/2` | `107/103` | no default solver system; legacy representative exact dense local-only subtotal `2149/2125` |

The dense diagnostic counts use all coefficients of unnormalized `p,q` plus
`C`; their equation counts omit the identically zero top Wronskian row. They
exclude transports, towers, terminal rows and guards and are not recommended
parametrizations. A representative legacy path to `(39,65)` is

\[
 (20,16)\to(119,35)\to(55,11)\to(651,63)
 \to(1008,49)\to(39,65),                                  \tag{I9}
\]

giving the exact diagnostic sum
`39/35+157/153+69/65+717/713+1060/1056+107/103=2149/2125`.
The `(10,15)` representative
`(21,15)->(10,15)->(279,63)->(425,51)->(1617,99)` gives
`39/35+28/24+345/341+479/475+1719/1715=2610/2590`, so `(39,65)` is not uniquely
the biggest once route vertices are counted. It is nevertheless the largest
single merge-local dense pattern, and its conditional default fate is now an
inexpensive E5 preflight rejection rather than a giant solver lane.

For a decorated route, the emitter computes rather than estimates

\[
 N_{\rm jet}^{\rm inline}
   =\sum_{v,h}|\mathsf{Allocated}_{v,h}|,
 \qquad
 N_{\rm jet}^{\rm dense}
   =\sum_{v,h}|\mathsf{Allocated}_{v,h}|
      +\sum_{v,h}(1+\deg P_{v,h,0}).                       \tag{I10}
\]

The first count is default `INLINE-J0`; the second is `DENSE-J0`. Both add
local, chart, tower, global and inverse variables. Equation counts are
`|Omega_B|` after removing independently proved zero IR rows, with every
block projection and dependency count printed. The dry-run manifest also
prints the expanded term/byte cost of each row-zero oracle result; inlining
does not make that work free.

`CONJECTURE (engineering size only).` Under `INLINE-J0`, the first useful
subleading projection may have roughly 100-300 allocated series coefficients
and `10^3-10^4` sparse
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

The root direction `c0` does not occur in this leading projection: the
Taylor coefficient of `S_r*(eta-c0)^203490` at its own root is `S_r`.
Accordingly it is omitted, not normalized; the full root chart must allocate
it and its subleading dependencies.

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

“Direct completion” here means the `(w,M,psi)=(2/3,3,2)` terminal is attached
at `G` with no trunk suffix. The neutral `N` lies on an incoming chain and is
the explicit finite synchronization representative; it does not change that
terminal classification.

From the chain-1 pole frame `(rho,kbar,nu;w,M)=(1,5,2;2,1)`, R1.2 with
`Delta=1` gives

\[
 \tau=4,\quad n_{N\to P_1}=45219,\quad
 (\rho_N,\bar\kappa_N,\nu_N;w_N,M_N)
    =(2,22612,11305;2,1).                                 \tag{P2}
\]

The nonzero merge edge then has

\[
 n_{G\to N}=11305\cdot5-22612=33913,\qquad X_G=3.         \tag{P3}
\]

On the other branch use the certified representative

\[
 P_2\leftarrow F_1\leftarrow F_2\leftarrow F_3
       \leftarrow H_2\leftarrow G,                        \tag{P4}
\]

where the arrows point poleward, matching the uniform rootward-to-poleward
orientation of section 1, and the local cells are from
`xmodel/sol-sixcells.md:86-100`. The whole tree is

```text
R0
|
G
+-- N  -- P1
+-- H2 -- F3 -- F2 -- F1 -- P2
```

The full `f` degree ledger is:

| vertex | reduced `(d_p,d_q,nu)` | `i_v` | full `f` degree | continuation multiplicity (reduced except at the root) |
|---|---|---:|---:|---:|
| `R0` | root pattern | — | 203490 | 203490 at `c0` |
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
(the `n'=1` used in `xmodel/sol-sixcells.md` is `n/nu_G`); here
`nu_G=nu_H=7`, so E5 and BOOK coincide.

At the direct terminal,

\[
 (\rho_G,\bar\kappa_G,\nu_G;w_G,M_G)
   =(1/3,5,7;2/3,3),\quad
 k_f=203490,\quad l_f=(1-w_G)k_f=67830,                   \tag{P5}
\]

and `R_term=3,psi=2`. The charged chain-2 cost is 4, exactly the P1 budget
`6-psi=4`.

### 3.3 Local patterns and coefficient rows

The pilot variable `C_v` is the normalized constant in (L2). Put
`t=eta^nu` separately at each row. The patterns are:

| vertex | `p`, `q` | emitted local rows |
|---|---|---|
| `P1` | `p=eta^2-A_p1`, `q=eta*(eta^2-B_p1)` | `2*B_p1-3*A_p1=0`; `2*A_p1*B_p1-C_p1=0` |
| `N` | `p=t-A_n`, `q=eta*(t-A_n)`, `nu=11305` | `11306*C_n+11305*A_n=0` |
| `G` | `p=eta^2*(t-A_g)`, `q=eta*(t-A_g)*(t-B_g)`, `nu=7` | `-14*A_g+21*B_g=0`; `-7*A_g*B_g-5*C_g=0` |
| `H2` | `p=(t-A_h)^2`, `q=eta*(t-A_h)`, `nu=7` | `4*C_h+7*A_h=0` |
| `F3` | `p=eta^3*(t-A_f3)^7`, `q=eta*(t-A_f3)`, `nu=5` | `3*C_f3+10*A_f3=0` |
| `F2` | `p=(t-A_f2)^4*(t-B_f2)^3`, `q=eta*(t-A_f2)*(t-B_f2)`, `nu=17` | `2*B_f2-3*A_f2=0`; `10*C_f2-51*A_f2^2=0` |
| `F1` | `R1(t)=t^2-Sig_f1*t+Pi_f1`; `p=(t-A_f1)^2*R1(t)`, `q=eta*(t-A_f1)*R1(t)`, `nu=5` | `Sig_f1-3*A_f1=0`; `Pi_f1-3*A_f1^2=0`; `4*C_f1+15*A_f1^3=0` |
| `P2` | `p=eta^4-A_p2*eta`; `q=eta^6+U_p2*eta^3+V_p2` | `2*U_p2+3*A_p2=0`; `A_p2*U_p2+4*V_p2=0`; `3*A_p2*V_p2-C_p2=0` |

The five non-pole chain rows and merge row are the exact substitutions
certified in `xmodel/sol-sixcells.md:145-174`. The neutral row follows from
(L2). The `P1` Wronskian is

\[
 2pq'-3p'q=C_{P1},                                        \tag{P6}
\]

Its raw coefficient rows are `4*B_p1-6*A_p1` and
`2*A_p1*B_p1-C_p1`; the displayed rows are their primitive, sign-normalized
canonical IR. For the `(a,b,nu)=(1,2,3)`
pole, the same Prop. 5.3 Wronskian with full degrees `(4,6)` gives the exact
new derivation

\[
 p=\eta^4-A\eta,\quad q=\eta^6+U\eta^3+V,\quad
 2pq'-3p'q=C_{P2},                                        \tag{P7}
\]

whose raw coefficient rows are
`-6*U_p2-9*A_p2`, `-3*A_p2*U_p2-12*V_p2`, and
`3*A_p2*V_p2-C_p2`. Per-row primitive/sign normalization gives precisely the
three displayed `P2` rows; no ideal-changing triangularization is used.
Direct elimination
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
2*A_p1*B_p1-C_p1,
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
A_p2*U_p2+4*V_p2,
3*A_p2*V_p2-C_p2,
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
- every `(k_j,l_j,tower_s[j])` and every `d_(h_j,v)` needed by (T2);
- the `PLUS/MINUS` tower side and hence both the correct initial label
  `g`/`g-b` and base `f`/`f-a`;
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
Rabinowitsch rows. If (H5)-(H6) occurs, the following paragraph and every
resulting kill are conditional on `CONJECTURE H5a`, and that dependency must
be in the manifest. Evaluation gives a direct necessary-condition map:

\[
 \{\text{Keller pairs realizing }C\}
       \longrightarrow V_{\mathbb C}(I_C).                 \tag{S1}
\]

Indeed, evaluate each variable at the corresponding coefficient of the
actual pair and its actual Puiseux charts. Prop. 8.1 gives (L1)-(L4), the
root law and actual directions give (L5)-(L9), the promoted handshakes give (H1)-(H6),
St. 3.9 gives (H7) and the top/drop part of (J5) on elementary steps,
St. 3.17 gives the composite `f-a` instance, and St. 8.3(ii) gives only the
certified common-live tower instances. Equation (J6) is the exact coordinate
identity for those same global objects, and (J7)-(J8) are its coefficient
consequences. Expanded elementary slots justify all remaining emitted
transport blocks. The dependency proof for (J9)-(J10) ensures no unknown tail
was set to zero. The actual
approximate-root tower gives (T1)-(T2), and the terminal plus Keller identity
give (R1)-(R6). Every saturated quantity is nonzero on the genuine object,
so its inverse exists and satisfies (L8). Since field extension is faithfully
flat, a proper ideal over `Q` remains proper over `Qbar`; the weak
Nullstellensatz then supplies a `Qbar` point. No algebraicity of the original
complex coefficients is assumed.

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
root-of-unity branch, neutral-depth family, free-characteristic pure-b family,
nonminimum budget-feasible charged stratum, and tower branch represented by
that record has been covered. Current `px5`
dedup does not provide this
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
| St. 3.9/3.17 and St. 8.3, summarized at `SHEET6-TEMPLATE.md:140-154` | chart, degree and full-jet transport | St. 3.9 is elementary/all `h`; composite authority is only `f-a` under St. 3.17 or common-live `h_j` under St. 8.3(ii), unless elementary slots are expanded |
| Prop. 4.2 / Prop. 4.3 | `PLUS` / `MINUS` common `h_j` towers | PLUS has `h0=g,base=f`; MINUS has `h0=g-b,base=f-a` and requires condition (7), equivalently (T0); Prop. 4.2 constant-leading-part case is a GAP (`SIGRAY-AUDIT.md:54`), Prop. 4.3 is verified with that gate (`SIGRAY-AUDIT.md:55`) |
| BOOK P1, `BOOK-OFFAXIS.md:486-500` | case-IV `R_term,psi`, budget and terminal integers | numerical P1 is not coefficient closure |
| LROOT, `SHEET6-LROOT.md:100-126` | one root direction and exact `k_f` | inherits the recorded E9/H2 branch-at-F reading |
| corrected St. 3.12, `SIGRAY-AUDIT.md:44` | x/y root chart swap | literal printed pair is duplicated |

No `CONJECTURE` is allowed to generate a kill without appearing in the
verdict's dependency field.

### 4.4 Wrong-object hazards: fail-closed checklist

An implementation must reject emission when any of these checks fails.

1. **Reduced/full confusion.** St. 3.9 transports `S*p^i` and the full
   patterns of fixed global `h`, not reduced `p,q`. Row-zero jets must be
   tied coefficientwise by (L1a) or inlined; a naming convention is not an
   equation.
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
   are proved zero. Nor does one endpoint multiplicity imply
   `r=m*N` for an arbitrary global label: require a per-label
   `TransportAuthority` or expand the elementary slots.
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
16. **Tower-side/base confusion.** Apply the global fiber-zero gauge once, or
    keep `f,f-a` and, for MINUS, `g,g-b` distinct via (F1a)-(F1b). A `PLUS`
    identity starts at `g` with the Prop. 4.2 base; a `MINUS` identity starts
    at `g-b` with the Prop. 4.3 base and needs the nonconstant condition-(7)
    witness (T0).
17. **Normalized-jet Jacobian.** Differentiate the full Laurent functions.
    Dropping either prefactor term in the second line of (R6) changes the
    Keller equation.
18. **Unsaturated structural constants.** Every full-pattern scale, tower
    constant, Jacobian constant, continuation required nonzero, and pattern
    guard has an explicit (L8) row; solver-side wishes are not equations.
19. **Truncated-series false zero.** Emit only an `Omega_B` whose complete
    dependency set is allocated, inlined, or certified zero. Expanding a
    truncated `J` and reading its high rows as equations can false-kill.
20. **Unsuitable ramification.** The LCM in (J0) is only a candidate. Every
    chart needs a Prop. 3.1 suitability witness, and an elementary
    substitution uses `z^delta_e`, not automatically `z`.
21. **Cost/arrival decoupling.** An arrival characteristic travels with its
    precise path and spent charge. Never combine a union of arrivals with a
    Dijkstra minimum for the same visible state.
22. **Lower-bound promotion.** `lambda_lb` is not `lambda_exact` on slack
    records. A full budget/cv inventory needs an authority or an explicit
    enumeration of the slack allocation.

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

- immutable `Cell`, `Frame`, `Vertex`, `ElementarySlot`, `Edge`, `RouteSummary`,
  `ParametricRouteFamily`, `NeutralPaddingFamily`,
  `FreeCharacteristicFamily`, `RouteCertificate`, `TowerLabel`,
  `TopPatternCertificate`, `TransportAuthority`, `JetWindow`,
  `GlobalSupportCertificate`, `Equation`, and `NonzeroGuard` records; each
  parametric family has an explicit
  `specialize(discrete_parameters)->RouteCertificate` boundary;
- an exact `Fraction` polynomial IR with deterministic variable ownership,
  expansion, denominator clearing, content removal and alpha-renaming;
- the 62-cell **regression** registry, the six positive local witnesses, and
  the E5 preflight table, plus a generic class-C/class-B constructor and
  admissibility gate for every cell produced by corrected enumeration;
- separate legacy-minimum replay and all-budget-strata coverage import,
  coupled arrival/path/cost records, and explicit neutral/tower expansion;
- separate constructors for (L1)/(L1a), (L3), (L9), pole/root top patterns and
  Wronskians, (H1)-(H8), (J6), (T2), (F1a)-(F1b), (R1)-(R6), and guards;
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

Each manifest records at least: `source_digest`, the SHA-256 of the ordered
list of relative source paths and exact input bytes plus the emitter source
digest/version (not a claimed git commit); cell and certificate IDs; every
fixed discrete datum; ground
field/prime, coherent case-III reading, variable order and ownership, equation
number/source, every saturation target, common `K`, all supports, projections
and dependency hashes, exact
vars/eqs/bytes, completeness label, canonical hash, prime exclusions, and
intended fleet lane.

### 5.2 Implementation milestones

1. **Provenance first.** Reproduce legacy `53/35` and `59/41` in
   `LEGACY-REPLAY`. In `COVERAGE`, retain every finite budget-feasible charged
   stratum and zero-cost clean-resonant predecessor in a cycle-quotiented
   nonidentity DAG, couple each arrival to its path/cost, encode
   self-loop/neutral and free-characteristic pure-b families symbolically,
   and demonstrate the six existing raw collapses.
   Run a fresh coherent E5 class-B/class-C enumeration using (I5a)-(I5e),
   rerun every case-III branch, and produce a cap-free completeness proof for
   each fixed reachable state. Do not call the filtered legacy list complete;
   do not claim global census completeness until reachable-state provenance
   is also cap-free. Emit no coefficient rows yet.
2. **Coherent numerical gate.** Reproduce the six local witnesses and the E5
   `PASS,PASS,CONDITIONAL-REJECT x4 (H5a)` table. Produce the synchronized
   direct certificate of section 3, including all `i` values.
3. **Exact IR and local layer.** Reproduce the merge-local 62-cell regression
   registry, instantiate the generic constructor on every newly enumerated
   cell, and emit the literal 83/74 pilot. Pass exact rational and
   finite-field anchors.
4. **Chart/tower layer.** Implement (J6), (J9)-(J10) and (T2) on planted
   microexamples, then attach real route tower/top/window certificates. Stop
   rather than infer missing Prop. 4.2 data or truncate an unknown tail.
5. **Terminal/global layer.** Add root/x-side top certificates, (R6),
   canonical equation hash, and fleet manifests. Keep `GLOBAL-CLOSED`
   disabled until a `GlobalSupportCertificate` exists.
6. **Remote solve fleet.** Ship only guard-clean artifacts. Bank a verdict only
   after authenticated output validation.

`CONJECTURE (schedule).` Milestones 1-3 fit the prior 3-5 engineering-day
estimate. Milestones 4-5 depend on reconstructing tower/root provenance and
may exceed it; that reconstruction is mathematical work, not emitter polish.

### 5.3 Mandatory regression gates

The test suite must include all of the following.

**G0 — census and provenance**

- exact filed legacy 62-cell regression registry and
  `56 dead / 6 local survivors`;
- filed completion counts `53/35` dedup and `59/41` raw, distributed exactly
  as in section 2.3;
- frozen canonical keys for all 53 dedup and 59 raw legacy records
  (`total,budget,ctx`, arrival `M2`, terminal), including the exact 29
  `(10,15)` equality endpoints and all 18 slack records; aggregate counts
  alone do not detect route drift;
- conditional-on-H5a E5-filtered **legacy-record** counts `49/31` dedup and
  `51/33` raw, while the fresh corrected-book census is explicitly `UNKNOWN`
  until regenerated;
- exact evaluation of the cap-free inversions (I5a)-(I5e), including class B
  and every P3 case-III branch; a loop bound such as the legacy `numax` is not
  a completeness certificate;
- all six raw collapses identified, with (I6)-(I7) proving that visible dedup
  is not equation dedup;
- `LEGACY-REPLAY` retains every minimum-cost predecessor, while `COVERAGE`
  retains every positive-cost stratum with `spent<=6-psi`, including
  nonminimum branches for all 18 slack records;
- every arrival characteristic is joined only to its own `path_id,spent`, and
  a planted px5-style decoupled union/minimum join is rejected;
- `lambda_lb` cannot populate `lambda_exact` without an equality/sandwich
  authority; unresolved slack/cv allocation downgrades the coverage claim;
- provenance enumeration terminates by charged-budget proof, cycle quotient,
  strict numerator descent on zero-cost clean-resonant edges, dirty
  Diophantine stopping, and symbolic neutral plus free-characteristic pure-b
  families; it rejects
  inherited `range(0,7)`, `range(0,41)`, `NCAP`, `PCAP_STATES`, numerator and
  `M` cutoffs as completeness machinery;
- refusal to emit `FULL-ROUTE` from a `RouteSummary`.

**G1 — six positive local controls**

For every row of section 2.1, reconstruct `p,q`, differentiate in `eta`, and
verify all (L3) coefficients, exact degrees, `C!=0`, `s(0)!=0`, `s(A)!=0`,
squarefreeness of the orbit radical/q (never `disc(p)` when p repeats), and
resultants. These are six merge-local controls, not six
certified route systems.

**G2 — 56 law-dead negative controls**

Load the exact tuples from `xmodel/sol-td7-law.md:218-262` or
`xmodel/td7-law-engine-check.md:116-179`. For each, assert

\[
 \mu=d_p-\nu,\quad \ell=(d_q-1)/\nu-1,\quad
 d_p=\mu+\nu,\quad d_q=1+(\ell+1)\nu,
 \quad\gcd(d_p,d_q)=M.                                    \tag{B1}
\]

Build (I2) independently. The raw coefficient system with `A!=0`, but with
the three known-failing admissibility inverses omitted, must solve uniquely
for `(local_s[v,*],C)` over `Q(A)` and remain a one-parameter satisfiable
family; use `A=1` as the explicit SAT witness. The forced solution has
`C=s(0)=s(A)=0`. After adjoining only `u_C*C-1`, exact local elimination must
already be empty. The production constructor may then add the other guards.
Do this in local exact Python; the largest `ell` is only 21. Do not invent
routes for cells already killed locally.

**G3 — E5 and handshake gates**

- reproduce (I3)-(I5) exactly;
- test equal-`nu` agreement on `(9,15)` and `(10,15)`;
- test all four unequal-`nu` conditional rejections and require
  `CONJECTURE H5a` in each verdict dependency field;
- force the legacy mixed formula and assert the manifest becomes
  `UNSOUND-FOR-VERDICT`;
- regression-test R1.2 with nonprimitive `(d_p,d_q)` so dropping `M` fails.

**G4 — pilot and jet anchors**

- exact 83 variables/74 rows and a deterministic characteristic-zero hash;
- exact substitution of (P11)-(P13), including every inverse row;
- reduction of the same point at `105337` and independent-parser equality;
- planted elementary/composite (J6) examples in which the deeper top's lower
  coefficient really comes from a shallow subleading row;
- a nontrivial `delta_e>1` example and rejection of a denominator-clearing
  `K` which lacks a Prop. 3.1 suitability witness;
- rejection of a composite arbitrary-`h` block with no
  `TransportAuthority`, and agreement of expanded-slot `r` with (J5);
- a three-slot composition checking both equations in (J3a)-(J3b), endpoint
  ownership, cumulative exponents and certified zeros; perturbing one
  `delta,c,m` or endpoint must revoke `EXPANDED_SLOTS` authority;
- exact `JetWindow` dependency maps for (J6),(T2),(R6), including boundary
  fixtures where the first omitted row contributes one slot beyond the last
  legal `Omega` coefficient; that row is refused, never zero-filled;
- planted `PLUS` and `MINUS` tower examples whose `h0` and bases both differ
  before the fiber-zero gauge, plus coefficientwise verification of
  (F1a)-(F1b); fixtures with `Dint!=0,eta-degree=0` and with
  `Dint=0,eta-degree>0` must pass (T0), while only the doubly zero/constant
  MINUS `gbar` top returns `UNRESOLVED-PROP4.3`;
- primitive and all-M-th-root fixtures for the two allowed root-of-unity
  representations, with an unrecorded fixed twist rejected;
- all perturbations listed after (P13);
- a terminal chart/Jacobian sign microtest which fails if either Laurent
  prefactor-derivative term in (R6) is deleted.

**G5 — emission hygiene**

- unique declared variables; no undeclared variables, zero IR rows, negative
  exponents or nondeterministic ordering;
- no `(` or `)` anywhere in an emitted polynomial body
  (`AUDIT.md:426-439`);
- per-row denominator clearing and content ledger;
- primitive-sign/monomial/row sorting and owner-order alpha-renaming exactly
  as specified in section 2.3; gauge quotienting is off unless certified;
- every mod-p coefficient represented in `[0,p)`, every intended row nonzero,
  and exact row/header counts preserved (`AUDIT.md:565-577`);
- prime validation and exclusions for `K`, every cleared J8 factorial,
  tower/binomial normalization integer, row-operation pivot, derivative
  coefficient and fixed nonzero coefficient; mod-p reduction must leave every
  exponent token byte-for-byte unchanged;
- independent-parser evaluations of the IR, char-zero text reduced mod `p`,
  and emitted mod-p text at two deterministic points;
- compute every generator's constant term; if they are all zero, record the
  origin as a witness and reject any external `[1]` verdict as impossible;
- one known-SAT emitted fixture per emitter tier (the literal pilot is the
  lead-tier fixture);
- manifest byte/hash/row integrity and fleet coverage exactly once;
- verdict acceptance requires `rc=0`, nonzero output, matching input SHA,
  logged command/host/msolve version, and an independent parser confirming
  that the complete reduced basis is exactly `[1]`, not a substring or
  partial output.

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
  excluded by `K`, a cleared denominator/J8 factorial, tower/binomial
  normalization, any explicitly ledgered row pivot,
  route characteristic, derivative coefficient, fixed nonzero coefficient,
  or guard. Assert each selected modulus is prime. Reduce coefficients—but
  never exponents—before shipping.
- Preserve input, output, command, host, msolve version, return code, wall
  time and byte count. A 0-byte output is never a verdict.
- Emit one **CONDITIONAL-REJECT (H5a/coherent-III)** preflight manifest for
  each of the four incompatible
  legacy arrival/cell types, listing both raw branch IDs (eight raw records
  total). Under the selected policy they receive no solver jobs. Queueing any of those raw branches
  under its recorded incompatible data is a build-gate failure; a distinct
  cell produced by a fresh coherent enumeration is a new certificate, not a
  revival of the rejected record.

The first solver objective is not “run 53 files.” It is:

1. finish one complete tower certificate for the direct `(9,15)` route;
2. emit its first theorem-complete jet window and controls;
3. solve it on Box02;
4. only after that schema passes, consume the fresh coherent census already
   produced in milestone 1 and expand its certificates into fleet jobs. The
   51 surviving legacy raw records may be used as regression inputs, not
   asserted as complete corrected-book coverage.

## 6. Definition of done

The emitter is ready for mathematical verdicts only when:

- a verdict manifest either proves parametric/invariance coverage or fixes
  one concrete finite representative—its exact neutral insertion sequence
  and depth plus every free characteristic—and claims only that certificate;
- every variable and equation is traceable to a numbered item in this design;
- the six positive and 56 negative local gates pass;
- the coherent-III default labels the four incompatible legacy arrival/cell
  records `CONDITIONAL-REJECT` with `CONJECTURE H5a` in the dependency field;
- the direct pilot reproduces the exact rational point and all negative
  perturbations;
- `FULL-ROUTE` emission includes common tower labels, the required shallow
  jet rows, terminal root/x-side data and (R6); and
- remote output validation follows `AUDIT.md` and `ops/FLEET.md` verbatim.

Until those conditions hold, the mathematically correct deliverable is a
local, leading, or prefix obstruction system with that scope in its filename
and manifest—not a “full coefficient-gluing” verdict.
