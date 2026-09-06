# Low-weight λ on the source-support order charts

**Disposition: the proposed λ-power test cannot kill the homogeneous Jacobian receivers. PROVED-HERE:** every nonzero x-charge-zero polynomial, including each correctly derived λ, has every positive power outside the homogeneous Jacobian coefficient ideal. All ten receivers also admit exact points satisfying the complete second-characteristic upper equations and λ≠0, with **c=0**. These are points of a necessary enlargement, not Keller pairs, not source realizations, and not campaign survivors. The separate computations retaining c≠0 have the finite-cutoff or resource-limited statuses recorded below. **No class is declared DEAD.**

The actual leader weights are **4,14,3,28,27,18** on the six classes ordered by unknown count, and **30,21,21,25** on R001–R004. Two weights are small; there is no uniform “tiny deficit” statement. A correct global h-adic polynomial lift of λ can involve coefficients of h. Replacing it by a convenient top α coordinate without its required upper equations would localize the wrong polynomial.

**Custody and scope.** Receipt: `xmodel/lambda-lowweight-astra-20260906.run.v2`; frozen basis: `7bb207ab90c0bd4a0494478521926b943ecfd618`; start: 2026-09-06 00:33:26 UTC. Before reading charged contents, awk joined the numbered `_sha256` and `_basename` entries; `sha256sum -c` against `/tmp/jc2-lane.IZAvbL/inputs` returned **8/8 OK**, with no content mismatch. The manifest and transcript are retained as `inputs.sha256` and `hash-check.txt` in the lane directory.

Only the charged 00:00Z submission was read as ideation input. Moh's primary PDF, `refs/moh1983_jram340_configurations_of_roots.pdf`, was checked directly, including rendered printed pp.152 and 157. No ledger was edited, and `jc2-lean` was not used. New drivers and evidence are confined to the requested lane directory.

**Which ideal is being tested.** This distinction is necessary to interpret both the proposal and the executable charts. Let R be the polynomial ring over Q in every declared G-coordinate and c. Let

\[
 I_J=([x^b y^a](J(P,Q)-cx^\ell))\subset R.
\]

Equivalently use every coefficient in the monic h-adic expansion of that same Jacobian. The positive bigrading in the charged report belongs to **I_J before inversion**. The production G-only solver instead uses `I_J+(Tc−1)`. The proposal's equivalence “λ-localizer is a unit iff some λ^N∈I” is valid for either fixed ideal, but those two choices of I have different meanings. Our structural nonmembership theorem concerns I_J. It does not assert nonmembership in the ideal already containing `Tc−1`.

Write U for the characteristic upper equations described below. We derive a global polynomial λ that agrees with the attained leader on U. Actual realizations satisfy `I_J+U+(Tc−1,Zλ−1)`. Dropping U or the c-localizer yields a necessary enlargement: a unit identity in such an enlargement would still kill, but its properness cannot certify realization. Baseline runs follow the literal proposed `I_J+(Zλ−1)`; separate production-condition probes retain `Tc−1`. The exact c=0 witnesses additionally show that retaining all of U does not rescue the λ-only strategy.

**Printed attainment, including the order-chart Jacobian exponent.** Use Moh's order `(f,g)=(Q,P)`, with `deg_y P=n=eK`, `deg_y Q=m=qK`, gcd(e,q)=1. Moh's source-series integer called e is denoted E here, to distinguish it from the h-exponent e. Printed p.152, Proposition 2.2, assumes `M_r≤E`; it gives the exact equality `deg_y T_r^ψ(Q,P)=−μ_r`, and for `M_r<E` gives a unit y-leader. The charged characteristic report checks the unit convention at the end of the proof, p.154. This is attainment, not an upper bound.

The coefficient specialization ψ acts on a target polynomial before composition, not on physical source-x terms after composition. The order charts have `J(P,Q)=c x^ell`, so the scalar-Jacobian version of Lemma 2.1 is not applied silently. Put `η=P^(−1/n)` and expand `Q=Σ f_j(x)η^j`, beginning with `η^(−m)`. At fixed η the chain rule gives

\[
 J(Q,P)=\left.\partial_x Q\right|_\eta P_y,
 \qquad P_y=n\eta^{-(n-1)}(1+O(\eta)).
\]

For c≠0, therefore, `f_j'(x)=0` for j<n−1 and `f_(n−1)'(x)=−c x^ell/n` with our P-first convention. Integrating in characteristic zero gives a nonconstant coefficient at n−1 and only constant earlier coefficients. Hence **E=n−1** also for these order charts. Every requested M2 is strictly smaller than n−1. Proposition 2.2 thus supplies exactly D2 and a nonzero scalar leader on every actual requested realization. This short extension is proved here from the chain rule; it is not claimed as an extra printed statement.

The numerical definitions on printed p.150 give `d1=n`, `d2=K`, `q1=−m`, `q2=M2+m`. Thus, with L=em=qn=eqK,

\[
 D_2=-\frac{-mn+(M_2+m)K}{K}=L-(M_2+m),
 \qquad W=L-D_2=M_2+m.                         \tag{1}
\]

In six-class metadata, `M_prime` omits M1 and its first entry is M2. In roster child data the first entry is M1=−m and the second is M2. The driver treats those conventions separately. R002 and R003 have distinct V labels but the same G receiver, ring, polynomial λ, and coefficient ideal.

**The full target family and an explicit polynomial formula for every λ.** Proposition 3.1 on printed p.157 supplies the recursive expansion, weight bound, and unique equality term. After the licensed normalization `Q=T1^ψ` from the charged source-support closeout, its T2 family is

\[
 \mathcal T=Q^e-P^q+
 \sum_{\substack{u,v\ge0,\ v<e\\un+vm<L}}\gamma_{uv}P^uQ^v,
 \qquad \gamma_{uv}\text{ scalars}.             \tag{2}
\]

The unique equality term is P^q and its coefficient is −1 by monicity. The bound already forces u<q. For (e,q)=(3,2), the lower monomials are `1,Q,P,Q²,PQ`; for (4,3), they are `1,Q,P,Q²,PQ,P²,Q³,PQ²,P²Q`. Their degrees are distinct: equality of two degrees would require `e(u−u')=q(v'−v)`, and the exponent restrictions force both differences zero. No permitted lower monomial is removed from the necessary family. Those of degree below D2 cannot affect either its upper equations or its leader. D2 is never divisible by K here, so no target monomial has degree exactly D2.

Here is a finite polynomial circuit specifying λ explicitly, including all carries in h-adic division. It is also the specification implemented by `derive_leaders.py` and the ten compact `.derive.sing` files. Define

\[
 h_0(y)=y^K+\sum_{a<K}h_{0,a}y^a,\quad
 A_i(y)=\sum_{a<K}A_{i,0,a}y^a,\quad
 B_i(y)=\sum_{a<K}B_{i,0,a}y^a,
\]

with exactly the declared β1=0 and terminal-constant gauges. Put `p(H)=H^e+Σ A_i H^(e−i)` and `q(H)=H^q+Σ B_i H^(q−i)`. These are the physical x^0 coefficient-ring calculation; this is legitimate because the desired scalar and every pivot have x-charge zero. It is not a specialization of the coefficient ideal used in the solver.

Define C(F) for a polynomial F(y,H) by the following recurrence. Starting from its H-coefficients f_j(y), divide `f_j=h_0 d_j+r_j`, with `deg_y r_j<K`, store r_j and add d_j to f_(j+1), in increasing j. Then `C(F)=Σ r_j H^j`. All division is by a monic polynomial, so the coefficients remain polynomials over Q in the original coordinates. This is a canonical h-adic expansion, with no parameter denominator. Initialize `F=C(q^e−p^q)`. For the pivot list in the next table, in decreasing r, perform

\[
 \gamma_{uv}=-[H^r y^0]F,\qquad
 F\leftarrow F+\gamma_{uv}C(p^u q^v),
 \qquad r=eu+qv.                              \tag{3}
\]

After the listed pivots, the explicit formula is

\[
 \boxed{\lambda=[H^J y^a]F,\quad D_2=JK+a.}    \tag{4}
\]

Equations (2)–(4) and the finite table determine every coefficient without an unspecified normal form. All 76,134 expanded terms are retained as deterministic gzip text; `leaders.json` records their raw/compressed hashes, byte counts, and term counts.

| chart shorthand | full class or receiver | (K,e,q) | D2=(J K+a) | ordered pivots r:(u,v) | expanded λ terms |
|---|---|---|---|---|---:|
| C70 | C_n24m16_Mm12_m2_5_ell1_s4 | (8,3,2) | 44=(5·8+4) | none | 6 |
| C109 | C_n18m12_M2_9_ell2_s3 | (6,3,2) | 22=(3·6+4) | 5:(1,1),4:(0,2) | 108 |
| C127 | C_n24m18_Mm15_14_ell1_s3 | (6,4,3) | 69=(11·6+3) | none | 4 |
| C171 | C_n24m16_M12_17_ell1_s3 | (8,3,2) | 20=(2·8+4) | 5:(1,1),4:(0,2),3:(1,0) | 7,075 |
| C341 | C_n24m18_M9_20_ell1_s3 | (6,4,3) | 45=(7·6+3) | 11:(2,1),10:(1,2),9:(0,3),8:(2,0) | 42,866 |
| C455 | C_n16m12_M6_13_ell3_s3 | (4,4,3) | 30=(7·4+2) | 11:(2,1),10:(1,2),9:(0,3),8:(2,0) | 2,672 |
| R001 | n21_m14_Mlast16_ell1; 193 unknowns | (7,3,2) | 12=(1·7+5) | 5:(1,1),4:(0,2),3:(1,0),2:(0,1) | 3,263 |
| R002 | n15_m10_Mlast11_ell2; 199 unknowns | (5,3,2) | 9=(1·5+4) | 5:(1,1),4:(0,2),3:(1,0),2:(0,1) | 417 |
| R003 | same receiver as R002; own V=3 | (5,3,2) | 9=(1·5+4) | same as R002 | 417 |
| R004 | n16_m12_Mlast13_ell1; 241 unknowns | (4,4,3) | 23=(5·4+3) | 11:(2,1),10:(1,2),9:(0,3),8:(2,0),7:(1,1),6:(0,2) | 19,306 |

For example, write `a_j=A1_0_j` and `h_j=h_0_j`. The exact global lifts on the two smallest-weight classes are

\[
 \lambda_{70}=-2a_4-2a_7a_5-a_6^2
              +2h_7a_7a_6-(h_7^2-h_6)a_7^2,    \tag{5}
\]
\[
 \lambda_{127}=3h_5a_5^2-a_5^3-6a_5a_4-3a_3.   \tag{6}
\]

The necessary upper equations give `a7=a6=a5=0` in (5), and `a5=a4=0` in (6), reducing them to −2a4 and −3a3. Those simplified expressions are valid **on the upper characteristic locus**. The unrestricted baseline runs use the full polynomials (5) and (6). This explicitly repairs the claim that the global lift only uses top α/β coefficients.

Why (4) is the actual leader on realizations: the target monomial at a pivot has y-degree rK and monic leader 1. Every lower target monomial has degree less than rK. On the upper locus the canonical coefficient `[H^r y^0]` must vanish, forcing exactly (3). After those uniquely forced scalar pivots, form the FULL P,Q expression in R[x,y], substitute the derived scalar γ values, and denote its full monic h-adic coefficients by H_j(x,y). Impose every coefficient `[x^b y^a]H_j=0` when `jK+a>D2`, and every coefficient with b>0 when `jK+a=D2`. These are U. Monicity makes the y-to-h-adic change triangular and invertible; consequently U is exactly the required upper-degree and scalar-leading-row block. Then (4) equals `[y^D2]T2` and Proposition 2.2 makes it nonzero. Lower target monomials, although retained existentially, cannot change that coefficient. No family representative is identified with the canonical characteristic polynomial away from this necessity statement.

**Bigrading and the three requested power components.** Give the original coordinates degrees

\[
 \deg h_{b,a}=(b,K-a),\quad
 \deg A_{i,b,a}=\deg B_{i,b,a}=(b,iK-a),\quad
 \deg c=(\ell+1,n+m-1).                        \tag{7}
\]

Every second weight is positive. Assigning each target scalar in (2) degree `(0,L−un−vm)` makes the entire family homogeneous. The monic division recurrence preserves that grading, and every rational pivot is homogeneous. Hence **deg λ=(0,W)** and **deg λ^N=(0,NW)**. Independent sparse parsing checked every one of the 76,134 expanded monomials against these degrees, then evaluated each polynomial at an independently constructed exact-degree point.

| chart | deg(c) | deg(λ) | deg(λ²) | deg(λ³) | homogenized cutoffs B=NW+3 |
|---|---|---|---|---|---|
| C70 | (2,39) | (0,4) | (0,8) | (0,12) | 7,11,15 |
| C109 | (3,29) | (0,14) | (0,28) | (0,42) | 17,31,45 |
| C127 | (2,41) | (0,3) | (0,6) | (0,9) | 6,9,12 |
| C171 | (2,39) | (0,28) | (0,56) | (0,84) | 31,59,87 |
| C341 | (2,41) | (0,27) | (0,54) | (0,81) | 30,57,84 |
| C455 | (4,27) | (0,18) | (0,36) | (0,54) | 21,39,57 |
| R001 | (2,34) | (0,30) | (0,60) | (0,90) | 33,63,93 |
| R002 | (3,24) | (0,21) | (0,42) | (0,63) | 24,45,66 |
| R003 | (3,24) | (0,21) | (0,42) | (0,63) | 24,45,66 |
| R004 | (2,27) | (0,25) | (0,50) | (0,75) | 28,53,78 |

**PROVED-HERE: the decisive x-charge obstruction.** An h-adic Jacobian row indexed by `(j,b,a)` is homogeneous of degree `(b+1,n+m−1−jK−a)`. Every such row has first charge at least 1. Every coordinate multiplier has nonnegative first charge. Therefore

\[
 I_J\cap R_{\text{x-charge }0}=0.              \tag{8}
\]

In particular, since every displayed λ is a nonzero polynomial of charge zero, `λ^N∉I_J` for **every N≥1**, not merely N=1,2,3. There are no Jacobian-row multipliers with the negative first charge needed to reach `(0,NW)`. This is the exact bigraded membership calculation requested by the proposal, and explains why increasing the y cutoff cannot fix its λ-only version.

Equivalently, send all positive-x-charge coordinates and c to zero, retaining all charge-zero coordinates freely. The Jacobian rows vanish because P and Q then depend only on y. This gives a surjection `R[Z]/(I_J,Zλ−1)→R0[λ^(−1)]`, with R0 a polynomial ring in the charge-zero coordinates. The target is nonzero, proving properness over Q without supplying a nonzero-Jacobian point.

Adjoining U can introduce charge-zero equations, so (8) alone does not prove properness of `I_J+U`. The next witnesses provide the separate proof. Adjoining `Tc−1` invalidates the c=0 projection entirely. Neither enlargement is hidden in the notation I.

**Exact-degree witnesses, and their limited role.** In this table h=y^K, all omitted coordinates are zero, c=0, and every target scalar in (2) can be zero. The displayed difference `Q^e−P^q` already has exact degree D2. These choices respect every G support, β1=0, and the two terminal constant gauges. The scalar λ is nonzero, so take Z=1/λ.

| chart | P | Q | λ |
|---|---|---|---|
| C70 | y^24+y^20 | y^16 | −2 |
| C109 | y^18+y^4 | y^12 | −2 |
| C127 | y^24+y^21 | y^18 | −3 |
| C171 | y^24+(3/2)y^10 | y^16+y² | 3/4 |
| C341 | y^24+(4/3)y^15+(2/9)y^6 | y^18+y^9 | −4/27 |
| C455 | y^16+(4/3)y^10+(2/9)y^4 | y^12+y^6 | −4/27 |
| R001 | y^21+(3/2)y^11+(3/8)y | y^14+y^4 | −1/8 |
| R002,R003 | y^15+(3/2)y^8+(3/8)y | y^10+y³ | −1/8 |
| R004 | y^16+(4/3)y^11+((4/3)a+2/9)y^6+((4/9)a−4/81)y | y^12+y^7+a y² | 2/243−4a/81 |

For R004 use `Q[a]/(54a²−36a+5)`. The reduced expansion has only degrees 23,18,13,8,3, and `Res_a(54a²−36a+5,2/243−4a/81)=8/6561≠0`. This field-valued point proves properness of the Q ideal. The other nine cases have rational points.

`verify_j0_witnesses.py` independently checks the expansions, field reduction, supports, gauges, and leaders; `j0-witness-controls.json` records ten passes. Thus `I_J+U+(Zλ−1)` is proper with c=0. Excluding Δ does not exclude the other zero-Jacobian points. The charged split-chart report's stronger exclusion is not imported into these order receivers.

**Cone-vertex localizer control, with a cofactor identity.** On Δ every α_i and β_i is constant; h remains an arbitrary allowed monic polynomial. Thus every constant-target polynomial in P,Q belongs to k[h]. Its canonical h-adic coefficients are constants. Since each D2 has a nonzero residue a modulo K, (4) is identically zero on Δ, without first assigning h any value. This last conclusion is particular to the canonical h-adic lift: a raw ordinary coefficient `[y^D2]T2` can be nonzero in a higher-degree element of k[h] before upper equations are imposed.

There is an explicit certificate in the full coordinate ring. Every monomial of λ contains some `A_i_0_a` or `B_i_0_a` with a>0. Partition its monomials according to the first such factor v in each serialized monomial and remove one factor v. This defines exact rational polynomials C_v with

\[
 \lambda=\sum_v v C_v,\qquad
 1=\sum_v (Z C_v)v-(Z\lambda-1).              \tag{9}
\]

All v belong to the defining ideal of Δ. The driver verifies the partition term by term, all 76,134 monomials, and exact Singular controls give UNIT on Δ. Separate untruncated `std(Zλ−1)` runs use each original expanded λ and return a principal basis with `NF(1)=1`, providing actual unrestricted negative controls; a toy inverse-variable control also passes. The formula uses only charge-zero coordinates; unused positive-x h coordinates may be freely adjoined. Thus arbitrary full h and permitted scalar α/β parameters remain free. `delta-controls.json` records all ten PASS results and formula custody. Equation (9) is **PROVED-HERE, UNIT ON Δ ONLY**. It is not a cofactor certificate in the unrestricted class ideal and is not promoted as a class kill.

**Valid weighted truncation.** `Zλ−1` cannot be homogeneous in a positive y-deficit grading: homogeneity would require weight(Z)=−W. A direct inhomogeneous `wp` call with `degBound` therefore does not have the homogeneous completion semantics needed for the proposed negative conclusion. The primary [Singular manual source, degBound](https://github.com/Singular/Singular/blob/spielwiese/doc/reference.doc) warns about global inhomogeneous inputs and specifies that block-order cutoffs otherwise use ordinary degree. The installed backend is Singular 4.3.2. We use a single positive `wp` block, not a mixed block order that silently changes the cutoff degree.

Introduce a homogenizer s and give Z and s weight 1. The executed baseline is

\[
 H=(I_J,\ Z\lambda-s^{W+1}),\qquad B=NW+3.    \tag{10}
\]

Every selected input row is homogeneous. Rows are omitted only as whole polynomials when their weight exceeds B; no monomial tail of a generator is deleted. Run exact-Q `std` with `degBound=B` and test the normal form of **s^B**. Since all original generator degrees are positive, rows above B cannot contribute to this target. A zero normal form would require a lifted exact cofactor identity before promotion. A completed nonzero normal form proves absence of a unit certificate whose homogenized summands have weight at most B; it does not establish properness at higher weights or realization.

For I_J before inversion, margin 3 covers N=1,2,3: a homogeneous identity for λ^N yields one for `s^(N(W+1))`. Writing `u=Zλ`, `v=s^(W+1)`,

\[
 s^{N(W+1)}=Z^N\lambda^N-
 (Z\lambda-s^{W+1})\sum_{k=0}^{N-1}u^k v^{N-1-k}. \tag{11}
\]

This supplies the exact conversion to a unit cofactor identity after s=1. It also explains why an unqualified “weight NW of the affine localizer” would be wrong.

For a second, exact target-component check, the baseline's x-charge-zero component contains only the localizer: all I_J rows have positive charge, while Z,s have charge zero. Consequently `(H)_(0,B)=((Zλ−s^(W+1)))_(0,B)`. The `chargezero` runs retain the coordinate ring and discard only generators proved irrelevant to this target component. No overflow quotient or coordinate specialization is imposed before localization. The remaining principal generator is a complete Gröbner basis: there are no distinct S-pairs, and its leading monomial contains Z, so it cannot reduce s^B.

For the production-condition variants, add T of weight 1 and homogenize `Tc−1` as `Tc−s^(n+m)`. That row enters only when B≥n+m. In particular it is absent at **all three** C70 and C127 cutoffs. These smallest-weight experiments cannot inspect c≠0 at the requested N, regardless of hardware. The same row is present in the larger probes explicitly marked below; (8) is not used to classify those systems.

In `I_J:c^∞`, membership of λ^N means `c^r λ^N∈I_J` for some r. Applying the geometric-sum identity to both localizers converts that homogeneous certificate at weight `r(n+m)+N(W+1)`—a sufficient bound, not a claim of minimality. The cutoffs NW+3 do not guarantee this conversion for r≥1. Thus the c-probes test bounded unit certificates, without claiming exhaustive N=1,2,3 membership tests in the saturated ideal.

A separate `UX` variant retains a linear subset of U. For W>K, the unique highest correction `−q α1 h^(eq−1)` forces α1 to have y-degree zero; the upper row `−q α1(x)+γ_top` then forces α1 scalar. For W<K, remove α1 deficits below W and positive-x coefficients at W. Descending through deficits gives constant pivots −q; α1 powers and h corrections involve previously removed coordinates. Hence **UX⊂U as ideals**, without a radical or parameter division. `UX-note.md` and `UX.json` give the proof and 140 explicit coordinate equations. Exact monomial partition verifies `λ−λ_UX=Σ zD_z`; retaining UX makes reduction of λ and Jacobian rows valid. These strengthened runs remain necessary conditions, separate from the baseline.

`grading-controls.sing` passes its cutoff, vertex-unit, and properness controls. For example `H=(l²,Zl−s²)` has `s³` nonzero at cutoff 3 and `s⁴=Z²l²−(Zl+s²)(Zl−s²)` at cutoff 4. No dimension, full-basis, or modular-promotion claim is made.

**Generator custody and actual run results.** The six original row files were streamed from their existing locations; their full hashes, variable order, and the selected rows' individual bidegrees are recorded per run. No huge native row file was copied into the lane. For R001/R002/R004, `roster_rows.py` reconstructs the exact production support/compiler/builder-fix program and demands byte-for-byte equality of its SHA-256 with the frozen roster's emitted-program digest. It then uses the previously audited sparse integer monic-division arithmetic. The resulting 289/300/378 h-adic rows match every frozen coordinate and count; R003 uses the identical R002 receiver.

The temporary roster rows contain 3,037,655 / 2,200,025 / 1,602,984 terms. Independent exact-integer recomposition at two full parameter assignments compares every emitted row with literal `J(P,Q)−c x^ell`. All six checks pass; reversed orientation and a one-term perturbation fail. `roster-row-controls.json` binds the checks; only hashes and regeneration drivers are retained.

Retries preserve the ideal. Prefix-12 preprocessing verifies the prefix generators and replaces later rows by congruent remainders; it does not certify the augmented cutoff. Packed storage retains Q, every ordered variable, and `wp`. Audited masks 511/255 have safe capacities 255/127; mask 255 is confined to C455 with 2B≤114. No exponent quotient is introduced. UX caches bind original/reduced rows by coordinate cofactors and require all eliminated UX generators. C455's Jacobian term count falls only about 9%.

All **30 charge-zero target computations completed** at the listed B, with basis size 1 and `NF(s^B)=s^B`. The final replay took 19.193 seconds and peaked at 145.4 MiB; `chargezero-independent-audit.json` binds these target-component results.

Cells list N=1,2,3: **C** = completed truncated nonunit at the listed B; **D** = exact target bound below the c-row, not a full basis; **O** = OPEN, no completed weight; **—** = no executed UX probe.

| case | all-row baseline | with c-localizer | with c-localizer and UX |
|---|---|---|---|
| C70 | C,C,C | D,D,D | —,—,C |
| C109 | C,O,O | D,O,O | —,O,O |
| C127 | C,C,C | D,D,D | —,—,— |
| C171 | O,O,O | D,O,O | —,O,O |
| C341 | O,O,O | D,O,O | —,O,O |
| C455 | O,O,O | D,O,O | —,O,O |
| R001 | O,O,O | D,O,O | —,O,O |
| R002 | O,O,O | D,O,O | —,O,O |
| R003 | O,O,O | D,O,O | —,O,O |
| R004 | O,O,O | O,O,O | O,O,O |

R003 reuses the verified identical R002 presentation. `best-results.json` pins chosen receipts and their history; `run-summary.md` gives individual bounds, times, and memory. No class-unit certificate was obtained.

**Resource disposition and delivery.** All computation was local; no fleet was launched. Bounded GB wall caps were at most 900 seconds; observed RSS peaked at 15.750 GiB. An early C455 disk-full receipt remains `OPEN_DISK_RECORD_LOST` with unknown metrics; preserved retries cover it. All owned workers were stopped at 03:32:08 UTC, and temporary rows/caches were removed. `shutdown-owned.json` records custody. Report and retained evidence total less than 2 MB; `final-audit.json` checks the seal, hashes, and 200-minute elapsed-wall-time limit.

**Promotion boundary.** No new exit-price assertion is made, so no exit `charge_basis` line is appropriate. Equation (9) certifies only the cone control. A finite-cutoff nonunit is not a survivor; a resource expiry has no completed-weight claim. The c=0 witnesses concern the specified necessary enlargement. The c≠0 realization question retains the separate probe statuses; no class is promoted DEAD.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24410`.
- Body SHA-256:
  `9034685d15538a6b01efbe43b8c0843cb0312d789a21ef3450b7bd4bbaf10853`.
- Frozen basis: `7bb207ab90c0bd4a0494478521926b943ecfd618`.
