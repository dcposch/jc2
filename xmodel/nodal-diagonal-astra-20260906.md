**Nodal diagonal instrument — transport and maps proved; exact branch decision OPEN**

Lane `nodal-diagonal-astra-20260906`, frozen basis `87bade844af276b13fba99c2b84dcd8c236ba9bf`. The transport preserves both client signs. The diagonal and transverse maps are invertible on the required localization. Both boundaries and all three complete source circuits have been built over Q. Circuit construction is not an ideal certificate; the nilpotence decision remains OPEN.

**Custody and scope.** Before any mathematical input read, I used `awk -F=` to join the receipt's numbered `_basename` and `_sha256` fields, prefixed its `lane_inputs_dir`, and piped the resulting manifest to `sha256sum -c`. All seven frozen inputs returned **OK**. The retained manifest and transcript are `box/nodal-diagonal-20260906/inputs.sha256` and `hash-check.txt`. Mathematical reads were restricted to the seven charged frozen copies, including my own sealed ideation submission and the Moh PDF. Links inside those reports were not treated as additional charged evidence. No other ideation input, ledger, or `jc2-lean` was used or edited.

Here **M** means the charged Moh print; **CD** the charged characteristic-degree report; **G99** the corrected-engine report; **CV/JD** the two charged cone/dependency reports. New executable evidence is entirely under `box/nodal-diagonal-20260906/`. Three bounded agents independently audited the print, the coefficient maps, and the boundary arithmetic. Mathematical conclusions below are separated from controls, circuit completion, and ideal decisions.

**The decision and its signs.** For a specified coefficient ring A over Q, necessary ideal I, and distinguished element

\[
s_{99,2}=\rho\lambda,\qquad s_{99,5/2}=c\lambda,
\qquad s_{108}=c\lambda,
\]

use a NEW indeterminate Z. Exactly

\[
D_{\operatorname{Spec}(A/I)}(s)=\varnothing
\iff s\in\sqrt I
\iff 1\in IA[Z]+(Zs-1).
\]

A unit localized ideal proves the branch **DEAD on this necessary chart** and excludes every licensed source point mapping into it. A proper localized ideal has the opposite sign: s is **not nilpotent**, and it supplies an existential nondegenerate **necessary-chart survivor** over an algebraic closure. Such properness does not certify the complete prescribed root/characteristic configuration. Neither an unfinished computation nor a proper projection is either conclusion. There is no `sat()` wrapper in these drivers.

**Printed license and declared source maps.** Engine F has degree n=99/108 and G has degree m=66/72. Moh's argument order is `(f,g)=(G,F)`. To distinguish the coefficient variable from physical x, write

\[
\psi:K[\xi][U,V]\longrightarrow K[U,V],\quad
\xi\mapsto0,\ U\mapsto U,\ V\mapsto V,
\]
\[
\mathrm{ev}:K[U,V]\longrightarrow K[x,y],\quad U\mapsto G,
\quad V\mapsto F.
\]

The specialization precedes physical evaluation; it does not set physical x to zero. M Prop.2.2, pp.152–154, gives actual y-degree `−mu_i` and a scalar unit leader at effective indices `M_i<e=n−1`. Here `M2=77<98` and `81<107`, giving D2=55/63. The p.154 convention “monic” means a unit leader, not an extra normalization to 1.

M Prop.3.1, p.157, with its specialization remark p.159, gives the target recursion. Enumerating weights at most `3m=2n`, with G-exponent below 3, gives `1,G,G²,F,FG,F²`; only F² has equality weight. Cancellation of the monic top forces its coefficient −1. Thus retain the complete family

\[
R=G^3-F^2+aG^2+bFG+c_tF+d_tG+e_0.\tag{1}
\]

The canonical `T2^psi(G,F)` is one member; the chart retains an existential representative R. The subscript t distinguishes target scalars from minor separation c. Two representatives of degree below m differ only by a constant: the four other target differences have distinct degrees `n+m,2m,n,m`, all above D2. Thus their negative faces agree.

Prop.2.2 alone does not prove total degree. The charged CD argument uses Prop.4.5, p.169, and the root-order argument p.172 to obtain the total-degree bound in the existing coordinates and the entire top:

\[
R_{55}=\lambda y^{15}(y-x)^{40},\qquad
R_{63}=\lambda y^{14}(y-x)^{49},\qquad\lambda\ne0.\tag{2}
\]

At the actual major D2 disc, Definition5.1(4), p.179, requires all of Prop.4.6's hypotheses. Its r=2 parameters are

| client | n | d_r | M_r | −mu_r | physical radius | printed scale | v |
|---|---:|---:|---:|---:|---:|---:|---:|
|99|99|33|77|55|1/3|−1/33|24|
|108|108|36|81|63|1/4|−1/36|28|

The scale here is not the characteristic leader lambda. The earlier inequality against the r=1 scale holds. The actual F/G faces, rather than merely their floors, are supplied by the charged outer-equality source argument: its four equality matrices have full column ranks `11,11,8,11` and `9,9,7,9`. Prop.4.6, pp.170–171, then gives R-face `P q`, since `(-mu_r+M_r-n)/d_r=1`, with degrees q=16/21. Write

\[
(d,k,P)=(3,8,(\pi^3-1)^8)\quad\hbox{or}\quad
(4,7,(\pi^4-1)^7).
\]

The actual F/G faces are P³/P². The injective map

\[
\chi_d:K[x,y]\hookrightarrow K[\pi][s,s^{-1}],\quad
x\mapsto s^{-d},\quad y\mapsto s^{-d}+\pi s
\]

sends `x^i(y−x)^k` to `pi^k s^(k−di)`. Its determinant is `−d s^(−d)`. The F,G,R valuations are `−3d,−2d,−(2d−1)`. The modified-Jacobian Remark on p.171 explicitly treats `J(f,g)=x^ell`; it changes the scale numerator to `−1−ell+delta`. Allowing an arbitrary nonzero constant C below follows by multiplying the same chain-rule identity by C. No second scale is spent to set C=1.

**Exact transport, including the omitted coefficient rows.** Set `C=J_(x,y)(F,G)`. Direct differentiation of (1) gives the polynomial identity

\[
J(F,R)=(3G^2+2aG+bF+d_t)C.\tag{3}
\]

Taking its leading cover coefficient gives

\[
-3dP^4q'+3(d-1)P^3P'q=-3dCP^4.
\]

Cancellation of the monic polynomial P and substitution `P=(pi^d−1)^k` yield

\[
(\pi^d-1)q'-N\pi^{d-1}q=C(\pi^d-1),
\quad N=k(d-1)=16\ \hbox{or}\ 21.\tag{4}
\]

Over Q its unique polynomial solutions are

\[
q_{99}/C=\pi-4\pi^4+\frac{48}{7}\pi^7-
\frac{216}{35}\pi^{10}+\frac{1296}{455}\pi^{13}-\frac{243}{455}\pi^{16},
\]
\[
q_{108}/C=\pi-\frac{21}{5}\pi^5+\frac{112}{15}\pi^9-
\frac{448}{65}\pi^{13}+\frac{3584}{1105}\pi^{17}-\frac{2048}{3315}\pi^{21}.
\]

A solution of degree greater than N has a nonzero uncancelled leading term in (4). A homogeneous polynomial solution of degree at most N would have root multiplicities N/d=16/3 or21/4 at each root of `pi^d−1`, and therefore is zero. Equivalently, the rational coefficient matrices have full column rank. `exact_controls.py` solves them, selects independent square rows, and substitutes back into **every** original row. The full matrices are **19×17 and25×22**; the selected square solves are17×17 and22×22. The promise “at most22” bounds the unknown columns/square solve, not the full row count or the full chart.

Comparing leaders and then coefficients of pi gives

\[
\lambda=-243C/455,\qquad\lambda=-2048C/3315,
\]
\[
\boxed{e=[x^2(y-x)]R=C=-455\lambda/243\quad(99)},
\]
\[
\boxed{e=[x^2(y-x)]R=-C=3315\lambda/2048\quad(108)}.\tag{5}
\]

Only `x²(y−x)` contributes to that pi coefficient at the specified valuation. The sign difference is P(0)=+1/−1. This is a source theorem for constant-Jacobian points, not an identity on the older T2-only chart, whose Jacobian could have degree20/25.

| depth convention |99|108|
|---|---:|---:|
|whole R leader, ambient normalizer 2n|143|153|
|constant Jacobian|163|178|
|e, ambient normalizer 2n|195|213|
|e, actual-degree R normalizer|52|60|
|transverse order of e|1|1|

No old ambient-depth threshold has moved. The instrument accesses a deep coefficient through an exact different coordinate presentation.

**Target completion, diagonal translation, and the node.** The scalar q below is distinct from the face polynomial q(pi). Put

\[
A=a+b^2/4,\quad p=d_t+bc_t/2-A^2/3,
\quad q=e_0+c_t^2/4-A(d_t+bc_t/2)/3+2A^3/27.
\]

The parameter-ring isomorphism has inverse

\[
a=A-b^2/4,\quad d_t=p+A^2/3-bc_t/2,
\quad e_0=q+Ap/3+A^3/27-c_t^2/4.
\]

Let epsilon=+1 for99 and−1 for108. The target automorphism and inverse are

\[
X=G+A/3,\quad Y=\epsilon(F-(bG+c_t)/2),
\quad G=X-A/3,\quad F=\epsilon Y+(b(X-A/3)+c_t)/2.
\]

Thus `R=X³+pX+q−Y²` and `j=J(X,Y)=−epsilon C`. Along y=x the actual major bounds give degrees X=2,Y=3,R≤1, with positive X/Y leaders. Write `X(x,x)=x²+Lx+M`, retain `h=L/2`, and declare

\[
u=x+h,\quad z=y-x;\qquad x=u-h,\quad y=u-h+z.
\]

This source coordinate map has determinant1. It reparametrizes the diagonal without setting h to zero. Put B=M−h². Cancellation of u⁵,u⁴,u³,u² in the characteristic identity, respectively, gives

\[
X_0=u^2+B,\quad Y_0=u^3+\tfrac32Bu,
\quad p=-\tfrac34B^2,\quad R_0=q+B^3/4.\tag{6}
\]

The u¹ term then vanishes identically. This is a coefficient proof, not a genus inference. The two parameters `u²=−3B/2` have common image `X=−B/2,Y=0`; they form the node when B is a unit.

The B localization is licensed scheme-theoretically. The constant-in-u zeroth Jacobian row is

\[
j=-\tfrac32B X_1(0),\qquad B^{-1}=-3X_1(0)/(2j).
\]

On `D(separation*lambda)`, (5) makes j a unit, so adjoining B inverse removes no part of the tested locus. B is not normalized to1. Equation (6) mostly determines target constants; it does not by itself remove five arbitrary F/G coefficients.

**The finite transverse recurrence and its inverse.** Over any Q-algebra with B invertible, expand X,Y in z. For r≥0 define

\[
K_r=\sum_{i=1}^r\big((r+1-i)X_i'Y_{r+1-i}-iX_iY'_{r+1-i}\big),
\quad H_r=(j\delta_{r0}-K_r)/(r+1),\quad D=3u^2+3B/2.
\]

Then the exact coefficient of z^r in `J(X,Y)=j` is equivalent to

\[
2uY_{r+1}-DX_{r+1}=H_r.
\]

Every polynomial solution, with no omitted component, is uniquely

\[
a_r=-2H_r(0)/(3B),\quad X_{r+1}=a_r+2uA_r(u),
\quad Y_{r+1}=\frac{H_r+Da_r}{2u}+DA_r(u).\tag{7}
\]

The numerator has zero constant term; u is **not inverted**. The inverse map is `a_r=X_(r+1)(0)`, `A_r=(X_(r+1)−a_r)/(2u)`. Induction gives inverse coefficient-ring homomorphisms, using only Q denominators and powers of B. At r=0,

\[
X_1=-2j/(3B)+2uA_0,\quad Y_1=-ju/B+DA_0,
\quad R_1=-j(u^2+3B/2).\tag{8}
\]

This independently proves (5), including invariance of the u² coefficient under u=x+h. Also `R−R0=zS` with `S(u,0)=−j(u²+3B/2)`. This divisibility is a genuine extra circuit reduction, not a contradiction.

Polynomial termination is part of the map. For strip k impose

\[
\deg_u X_k\le\min(m-k,2+\lfloor k/d\rfloor),\quad
\deg_u Y_k\le\min(n-k,3+\lfloor k/d\rfloor).
\]

A negative bound means zero. Once X disappears, keep `H_(k−1)(0)=0`; truncate Y only while retaining **every overflow coefficient**. After the last Y strip, retain every remaining Jacobian coefficient through z-degree `n+m−2`. The possible next coefficient vanishes identically because the last X/Y coefficients are scalars. For R retain every overflow beyond `min(D2−k,floor((k+2d−1)/d))`, and subtract both its entire homogeneous top and complete actual major face.

`recurrence_stream.py` implements exactly these operations as rational straight-line circuits. Its raw A allocations are625/610, with at most18/16 coefficients in one strip. Those are generator allocations, not dimensions. The 99 and108 runs constructed13,913,568 and13,575,116 arithmetic nodes and7,948/7,748 syntax rows. Graph definitions are acyclic; eliminating them is an isomorphism.  No millions-node artifact tree was written.

Explicitly the transverse coefficient ring is `Q[B,Binv,j,A_(r,i),q,lambda,h,A_target,b_target,c_target,minor parameters,Z]`, modulo `B*Binv−1` and all emitted rows. Order is B,Binv,j, then (r,i) lexicographically, then the displayed scalars, minor parameters `(u_m,a2,rho)`, `(u_m,v_m,c)`, or `(u_m,v_m,c,mu)`, and Z. The source coefficient ring uses physical F/G coefficients and target/minor scalars, modulo the same full constraints and localized at separation*lambda; equations (6)–(7), target completion and physical substitution define the forward homomorphism. Coefficient extraction, canonical division and the displayed inverses define the reverse. Ordered variable lists and row blocks are retained per client; graph nodes adjoin only acyclic defining equations.

**Both boundary directions, with full targets.** Work with `K_P=t^N P(t^−1,w/t)=sum t^r K_r(w)`, `deg K_r≤N−r`. Major w=1; the minor substitution is

\[
\begin{array}{ll}
99,2:&y=u_m/x+(a_2+\zeta)/x^2,\quad P_m=\zeta^2(\zeta+3\rho);\\
99,5/2:&y=u_m/x+v_m/x^2+\pi/x^{5/2},\quad P_m=\pi(\pi^2-c);\\
108:&y=u_m/x+v_m/x^2+\pi/x^3,\quad T_m=(\pi-\mu)^2-c.
\end{array}
\]

The audited `jet0=0` translation slice is used; its free translation factor is recoverable. The variable u_m is not the diagonal parameter u. The D108 mean mu remains free. In the half-integral case use t=tau² throughout.

At each depth r, the major and minor equations prescribe Taylor jets at w=1 and0. The lower minor centres contribute only already reconstructed depths. If their lengths are a_r,b_r, the exact reconstruction is

\[
K_r=M_r+(w-1)^{a_r}\big[((N_r-M_r)(w-1)^{-a_r})\bmod w^{b_r}\big]
 +w^{b_r}(w-1)^{a_r}E_r.
\]

Here M_r is expressed in w−1, and N_r is the required minor jet after earlier contributions are subtracted. The inverse of `(w−1)^a` modulo w^b has integral coefficients. No centre, separation, discriminant, or generic pivot minor is inverted. Exact division by `w^b(w−1)^a` gives the inverse free-coefficient map. The prescribed top is the single compatibility at depth0; it is not zeroed.

For F/G the major jet lengths are `max(0,floor((288/192−3r)/4)+1)` or `max(0,floor((420/280−4r)/5)+1)`. Minor lengths are `max(0,floor((81/54−r)/3)+1)`, `max(0,floor((189/126−2r)/7)+1)`, and `max(0,floor((96/64−r)/4)+1)`. Enumerating the exact free E widths gives:

| client | F after both full boundaries | G | pair | R | F/G/R |
|---|---:|---:|---:|---:|---:|
|99 delta2|336|146|482|100|582|
|99 delta5/2|154|65|219|44|263|
|108 free mean|255|110|365|83|448|

These exclude centres and target scalars and precede nonlinear compatibility. `boundary_maps.py` constructs all nine universal maps, checks298 integral inverse matrices, and replays6,680 minor plus20,660 major rows at each of two exact rational controls. Universality follows from the unit matrices and inverse formulas, not those evaluations. The largest boundary pivot is27; it is unrelated to the22-column face solve.

The R minor targets have a separate source license: M Prop.6.1(2), pp.190–193, and Def.3.1, p.161. Principal minor multiplicities `3<11/2` and `2<9/2`, with negative F orders `−18,−9/2,−12`, give the distribution ratios9:6:5 and12:8:7. Therefore R has orders `−10,−5/2,−7` and full targets

\[
\lambda P_m^5,\quad\lambda P_m^5,\quad
\boxed{-\lambda((\pi-\mu)^2-c)^7}.
\]

The scalar is fixed by (2), not free: the largest minor pi coefficient comes uniquely from `x40 y15` or `x49 y14`. The latter has coefficient **−lambda**. Reversing that sign would manufacture a false `2lambda=0` row.

**Measured further reduction.** At homogeneous Jacobian depth r, the current F/G boundary coefficients enter through the rational linear map

\[
nF_0G_r'-(m-r)F_0'G_r+(n-r)F_rG_0'-mF_r'G_0.
\]

Everything else involves preceding coefficients and remains a compatibility equation. Exact RREF after removing a common monic polynomial factor gives:

| client | boundary generators | rational Jacobian pivots | remaining generators |
|---|---:|---:|---:|
|99 delta2|482|327|155|
|99 delta5/2|219|145|74|
|108 free mean|365|243|122|

The kernels consist of the paired G variations plus9/9/12 radial directions. These are actual graph eliminations, not tangent-space dimensions of the final ideal. Adding the current T2 high-degree equations, retaining b,a,c_t at their entrance depths, gives149/68/113 generators. The scalar d_t enters later and is solved by a rational leading coefficient. Every unselected compatibility row is retained; subtracting ranks from an unrelated presentation would be invalid.

There is a proved polynomial product decomposition by three target parameters. The transformations `F'=F+beta G+gamma`, `G'=G+alpha` preserve R after transporting its five coefficients, preserve C,lambda and all source centres, and have explicit inverses. Their canonical roots transform as `h2'=h2+beta/3`, `h3'=h3`. Only the last inner remainder shifts by beta/3; the outer remainder formulas preserve all their degree and negative-order bounds. The completed X,Y,p,q are invariant. Thus `(A,b,c_t)` are three affine orbit coordinates, with the displayed global inverse, not three more source gauges.

After factoring these coordinates, the delta5/2 base chart has **65 G coefficients +3 minor parameters + free q =69 generators**, of which68 occur in the equations. Adjoining Rabinowitsch Z gives69 occurring variables, or70 including free q. Normalize as `R=G³−F²+pG+q`. At depth r≤99, divide the known numerator by monic F_top; set F_r to half the quotient and retain every remainder. At132 solve p; at143 recover lambda. These are inverse polynomial coefficient maps and do not invert physical w. `boundary_full_dag.py` reached characteristic depth198 and Jacobian depth163, retaining33,135 coefficients in46,770,392 operations. Its canonical addon matched146 replay blocks/19,605 coefficients, then adjoined40,906 source and localizer rows: **74,041 retained rows in the full localized presentation**. Algebraic reduction is still required.

**Full source transport.** From physical F recover the unique monic approximate cube root h2, then its monic cube/quartic root h3. The recursion uses nonzero rational denominators; no coefficient pivot is inverted. Ordinary monic division recovers

\[
F=h_2^3+A_2h_2+A_3,\quad G=h_2^2+B_1h_2+B_2,
\quad h_2=h_3^r+\sum_{i=2}^r C_i h_3^{r-i},\quad r=3/4.
\]

The inverse is these reconstruction identities. Monic division and unit Hermite pivots remain valid over coefficient rings with zero divisors; reducedness is not assumed. Every recovered remainder retains its y/total-degree overflow rows, D2, licensed D1, and minor strict rows. With k=33/36 and k3=11/9, outer y-degrees are below k and total bounds are `(2k−1,3k−1,k−1,2k−1)`; `deg_y Ci<k3`, `deg Ci≤ik3−1`.

For99 the D1 cover is `x=e^−9,y=e^−9+e³+Pi e⁴`; for108 it is `x=e^−8,y=e^−8+e²+Pi e³`. The h2/F/G floors are−1/−3/−2 in those covers. Outer floors are−2/−3/−1/−2. No h3 D1 block is invented: the h2 child multiplicities8 and7 are not divisible by3 and4. Deck transformations carry the selected-child rows to all conjugates.

`source_stream.py` composes the full transverse map, target inverse, physical source substitution, canonical divisions, all source blocks, and the actual `Z*separation*lambda−1` row. All three executions completed:

| client | arithmetic nodes | retained syntax rows | peak RSS KiB |
|---|---:|---:|---:|
|99 delta2|38,897,516|52,893|956,964|
|99 delta5/2|39,587,492|53,672|972,688|
|108 free mean|48,697,186|75,111|1,195,064|

Some rows are algebraically redundant; they are retained rather than presumed zero by syntax. Each receipt binds the graph, ordered rows, ordered variables and both driver hashes. `source_controls.py` independently checks monic recovery, division, physical composition, all minor substitution coefficients, and wrong-target detection over Q. The source map is a two-way **presentation** map after all constant-Jacobian and characteristic/source rows are imposed. It is not a two-way map from the older T2-only chart into the constant-Jacobian chart.

**An additional supported quotient, with the centre issue resolved.** The complete boundary conditions also license monic division

\[
\lambda G=H R+S,\quad \deg H\le11/9,\quad \deg S<55/63.
\]

H has the difference major/minor valuation bounds `(1,2)`, `(1,1)`, `(1,1)` in the respective integral covers. A homogeneous subtraction alone would not prove this: along a nonzero centre, `xy−u_m` can have better valuation than its homogeneous part. The proof instead constructs a full supported lower-degree lift of every allowed quotient leading piece, by the same unit Hermite interpolation, and subtracts that lift times R. Both valuation bounds are preserved and total degree strictly drops. The finite lifting check covers every quotient degree0..11/9 over the full centre ring.

The remainder's face degree is below the divisor's face degree. Exact pi division consequently gives

\[
H_{99,\mathrm{major}}=\pi^2(9\pi^6-24\pi^3+20)/9,
\quad H_{108,\mathrm{major}}=\pi^3(4\pi^4-7)/4.
\]

Its minor face is P_m or−T_m. The full H boundary maps leave3/1/1 coefficients, with centres and separation retained. This repairs the previously unproved quotient-support subproblem; see `h-quotient-proof.md` and its exact symbolic controls. It does **not** kill the residual: S still has the permitted major coefficient lambda at x², and x² satisfies the improved minor bound. A proper one-coordinate H chart is not a full-chart survivor.

**Gauges, leading targets, and controls.** Direction placement uses the initial source linear transformations; F/G monicity uses their target scales. Uniform source dilation sets the major beta=1 once; separation, lambda, C and B stay free as required. The first translation removes the major ordinary constant. The audited remaining translation gives the jet0=0 slice with its explicit inverse and centre transport; for108 it retains mu. The diagonal u=x+h is a reparametrization with h retained. Target completion and the proved three affine factors are coordinate maps with inverses, not extra scalar normalizations.

Every leading equation is **coefficient minus the whole forced target**. The F/G minor targets are `P_m^9/P_m^6` for99 and `T_m^12/T_m^8` for108, at normalized powers81/54,189/126,96/64. Every strictly lower power has zero target. Equation (2) subtracts all16/15 nonzero binomial coefficients of the R top.

The cone/dependent-family control retains all four parameters in `F=h³+b0h+c0`, `G=h²+d0h+eta0`. Every constant-target composition lies in K[h]. After its high coefficients vanish, the remaining characteristic is constant; exact degree55/63, neither divisible by33/36, forces lambda=0. Localizing lambda makes this restriction unit. This is **PROVED-HERE: UNIT ON THE DEPENDENT FAMILY**, not a unit of the unrestricted branch.

Fresh Singular controls in the declared Q ring return unit bits `[0,1]` for proper/nilpotent localizations and `[0,1]` for each correct-face/wrong-sign pair. The face controls have explicit rational points with `C=B=separation=1`, `lambda=−243/455` or`−2048/3315`, and e=+1/−1. They are typed **ODE/FIRST-STRIP CONTROLS ONLY**, not necessary-chart survivors. The wrong108 minor-top sign is separately rejected by the exact boundary compatibility control.

**Decision record and resource closeout.** **EXACT-Q OPEN for 99 delta2, 99 delta5/2, and108 free mean.** No full-chart nilpotence certificate, properness certificate, or witness was obtained. The source and coefficient maps pass; the proposed small-matrix decision reduction is unproved. Its exact missing step is an extension/elimination theorem from the proper face/H projection through every remaining source, characteristic, Jacobian and termination row. A proper base can map to the zero quotient. The allowed S term lambda*u² prevents the proposed immediate remainder kill.

Construction followed the requested client order. The149/113 presentations exceeded the charged ideation's70-variable stop criterion. Polynomial expansion was attempted on the reduced delta5/2 presentation. Three exact-Q attempts, each capped at600 CPU seconds, completed characteristic prefixes27,48,58, respectively; all stopped before the full decision ideal was assembled as expanded polynomials. The final attempt uses `G E_t−3G_t E=−F T`, with `E=F²−G³`, `T=3G_t F−2G F_t`. Monic coefficient division proves ideal-level equivalence, including nilpotents; see `differential-prefix-proof.md`. Zero residuals on those prefixes certify no full-chart conclusion. The complete source circuits remain reproducible separately.

The lane's conservative aggregate CPU bound is3460 seconds, including failed attempts, repeats and small-control allowances; peak measured RSS is1,838,936KiB. Completion is within200 minutes. Retained report, drivers, receipts and notes total under1MB; no artifact trees or writes above10MB were made. No ledger edits or jc2-lean execution occurred. The closing manifest binds every retained driver and receipt; custody hashes and both localization signs were checked again. No branch gate is promoted.

No new exit-price assertion is made. FALLACY-v2 controls apply: floors are not attainment, whole targets and coefficient maps are explicit, and proper projections or completed circuits supply no branch decision.

<!-- BODY-END -->
