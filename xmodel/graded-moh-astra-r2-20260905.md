Moh completed charts — resumed grading and certificate lane — 2026-09-05

**Disposition: the completed coefficient ideals are positively graded cones; the c≠0 chart is an explicit Laurent product of its c=1 section over Q. Exact finite bidegree tests and a rigorous universal cutoff are established. Exact rational finite quotients prove c∉I on all four tested fibres. Class emptiness remains OPEN; no exact-Q UNIT or rational c-power identity has been certified.** Final solver and worker dispositions are recorded below.

**Custody and scope.** Round 2 began at 14:19:30Z with receipt basis `dd24342e1eca2a44ee9c603bce9361efb56512a5`. Before reading the charged mathematical contents, awk joined the seven numbered `_basename` and `_sha256` fields with the receipt input directory; `sha256sum -c` returned seven OK results. The mechanical manifest is `resume-r2/charged-inputs.sha256`, rooted at `/tmp/jc2-lane.NOv2jX/inputs/`. The charged 21,356-byte round-1 draft was adopted unchanged as evidence and developed below; its verified SHA-256 is `0c7237a34c50adf774e1ce973c38353108dc249e50653df5b5b14be6307a7bee`. Paths beginning box/, xmodel/ or ops/fleet/ are repository-root paths; other artifact paths below are relative to box/graded-moh-20260905/.

Round 1 began at 13:47:42Z; its charged draft records the successful eight-input hash check in `frozen-inputs.sha256`. The eight metadata/builder files for the tested fibres match the gate's `completion-core.sha256`, as recorded in `validation/source-gate-hashes.json`. Round 2's fresh audits bind the same complete source presentations.

The consumable chart family is exclusively the repository-root path `box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes/`. Each has the frozen gate's support S_i(V)=D_i(V)∪G_i, with independent coefficients and its stated β1/terminal-constant gauges. The class-uniform G_i embedding is the reason an exact-Q UNIT on any one completed fibre kills its class. No result from an old capped chart, from a header-only row file, or from a fixed arbitrary parameter point is transported into this family. The preserved 425-row s′=4 control is used only with its explicit builder-identity custody.

The frozen gate is consumed as a source-support theorem; this lane proves new algebraic reductions of its completed receivers. The six-class Moh census/descent dependencies are inherited, not re-proved. No new exit-price assertion is made, so no exit charge_basis line applies. Work is confined to this lane's driver/artifact directory and the requested report. No ledger, jc2-lean, or ideation file is edited.

**Why the grading survives the actual chart.** Assigning a parameter merely the weight of the monomial it multiplies gives the wrong sign for a coefficient-ring identity unless the monic block is accounted for. The invariant is its block deficit. The proof below uses the nonnegative x-charge convention; some round-1 audits use the equivalent signed first component −b. Negating the first component is the declared isomorphism between their degree lattices. The monicity and omitted constant gauges are homogeneous in either convention.

The geometric physical weight d(iK−a)−b is not uniformly positive on D_i∪G_i: D_i can add coordinates outside the outer-disc weighted envelope. The strictly positive y-deficit grading avoids that difficulty and applies to every finite support in these monic blocks. Its existence does not require that the completed chart itself obey the G-only physical bound. This distinguishes the source's weighted bound from the algebraic grading of the larger receiver.


Use the frozen gate's final S_i=D_i∪G_i inventories. Let n=eK, m=qK, D=n+m−1, R=Q[z,c], and write z=h_ba or A_i,ba or B_i,ba. Missing terminal constant coordinates are identically zero, and β1=0. In the following formulas an h coordinate has block index i=1. Define the NONNEGATIVE bidegree

    deg z=(b,iK−a),           deg c=(ℓ+1,D).                 (1)

Its second component w(z)=iK−a is strictly positive: 0≤a<K and i≥1. In the ambient coefficient extraction ring give formal x degree (−1,0), formal y degree (0,1). Then h has degree (0,K), α_i and β_i degree (0,iK), P degree (0,n), Q degree (0,m), and J(P,Q)−cx^ℓ degree (1,D). Thus the ordinary coefficient row [x^b y^a](J−cx^ℓ) is bihomogeneous of degree (b+1,D−a). Monic h-adic division preserves homogeneity; its row indexed x^b y^a h^j has degree

    (b+1,D−a−jK).                                      (2)

The coefficient ideals from ordinary and h-adic extraction agree: the monic triangular basis transformation between y^a h^j and ordinary y powers is invertible over R[x], with polynomial entries in both directions. Consequently the EXACT chart ideal I before adjoining Tc−1 is N²-homogeneous. This proof uses only monic block structure; arbitrary finite support subsets, including the actual D∪G unions, preserve it. No source-support parameter is dropped.

The corresponding two-dimensional torus is explicit:

    z ↦ λ^b μ^(iK−a) z;       c ↦ λ^(ℓ+1) μ^D c;
    h'(x,y)=μ^K h(λx,μ^(−1)y),
    P'(x,y)=μ^n P(λx,μ^(−1)y),
    Q'(x,y)=μ^m Q(λx,μ^(−1)y).

The chain rule gives J(P',Q')=λ^(ℓ+1)μ^D c x^ℓ. Monicity, β1=0, omitted constant gauges, and every coordinate support set are preserved. Setting λ=1 makes all parameter powers of μ positive. The action extends to μ=0, taking the chart to its vertex (all parameters including c zero), where P=y^n and Q=y^m. Hence V(I) is a genuine positive weighted affine cone, not merely a variety with a signed torus grading. It need not be an ordinary scalar cone.

Over algebraic closure, the Rabinowitsch equivalences are

    I+(Tc−1)=(1)  ⇔  c∈√I  ⇔  V(I)⊆{c=0}.

They hold for arbitrary I; the grading additionally gives the cone and computational decompositions. Existence of polynomial identities over an extension field descends to Q by solving the finite coefficient linear system over Q. No assertion about rational points alone is used.

For all six classes, (D,ℓ+1) is respectively (27,4),(29,3),(39,2),(39,2),(41,2),(41,2). Their gcd is one. In each complete fibre every non-c parameter has 1≤w(z)≤n<D. Therefore its residual torus weight

    r(z)=(ℓ+1)w(z)−Db

is nonzero: otherwise D divides w(z). The residual one-parameter torus λ=t^(−D), μ=t^(ℓ+1) fixes c and acts on z with weight r(z).

Global c gauge, now over Q itself. Put p=ℓ+1. Choose integers A,B with Ap+BD=1: (7,−1),(10,−1),(20,−1),(21,−1) for (p,D)=(4,27),(3,29),(2,39),(2,41). Let k(z)=A b_z+B w_z and k(c)=1. With S=R/(I,c−1), the explicit inverse Q-algebra maps are

    (R/I)[c^−1] ≅ S[s,s^−1],
    c ↦ s, z ↦ s^k(z) z̄;       s ↦ c, z̄ ↦ c^−k(z)z.

A row of bidegree (u,v) maps to s^(Au+Bv) times its c=1 image, proving the maps descend and compose to the identity. Hence the c≠0 chart is the product (c=1 section)×G_m over Q, and

    I+(Tc−1)=(1) ⇔ I|_(c=1)=(1).

No rational-point assumption or root extraction is needed for this first gauge. It removes c and T: the solver has r−1 variables instead of r+1. An exact section identity Σ h_i(z)f_i(z,1)=1 converts to a full-ring c-power identity: expand h_i into monomials m, put k_i=A u_i+B v_i, and choose M≥1 and M≥k(m)+k_i for every term. Then

    c^M = Σ_i Σ_m coeff_m(h_i) c^(M−k(m)−k_i) m f_i(z,c).

Every exponent is nonnegative; exact multiplication in the original ring verifies the identity. The residual torus described above acts on S. A second coordinate gauge z=1 is valid only on the open set z≠0. All x-dependent coordinates (b>0) supply a complete finite cover: if they all vanish, P and Q depend only on y, so J=0 and the target equation forces c=0. Their residual weights are nonzero, so over algebraic closure each branch admits z=1 while maintaining c=1; this normalization may require roots. An exact-Q UNIT on EVERY branch proves the complete chart empty. One arbitrary branch is insufficient. A smaller cover requires a proved implication or a hitting set for a validated expression of c; numerical nonzero observations do not provide it.

Low-weight staging has an exact limitation. Every native row has 1≤w(f)≤D, and c occurs only at weight D in the unique target row. For any w0<D, the subsystem of rows of weight≤w0 is independent of c. Its point with all other parameters zero and c=1 is a solution. Therefore it cannot force c=0. If the full ideal forces c=0, the minimum equation-weight threshold in this positive grading is EXACTLY D; if the full ideal does not, no threshold works. This statement determines the only possible threshold and proves all smaller thresholds fail, but does not assert that full forcing occurs. At weight d every row has the stronger form M_d z_d+P_d(z_<d), with a constant rational matrix M_d: a weight-d variable cannot multiply any positive-weight factor. Thus constant Gaussian pivots eliminate coordinates globally, without parameter denominators or omitted branches. Rank-deficient blocks leave free variables and nonlinear compatibility equations. Since all non-c weights are≤n<D, at weight D the only new variable is c in its unique row F−c. The staging is useful but does not make the remaining equations linear.

There is no Artinian shortcut. Setting all b>0 coordinates and c to zero leaves an affine subspace of V(I) of dimension D−1 (26,28,38,40 as applicable). Hence R/I has no finite top graded degree. A Fröberg or Artinian socle cutoff requires additional hypotheses; none is supplied here.

The useful truncation is a finite BIGRADED membership block. Let C=(ℓ+1,D). Because I is bihomogeneous, c^N∈I iff c^N belongs to the Q-linear span of all m f, where f is a declared homogeneous coefficient generator and m ranges over parameter monomials of degree NC−deg(f). For a native row (j,b,a), the multiplier must satisfy

    Σ_z b_z exponent_z = N(ℓ+1)−b−1,
    Σ_z w(z) exponent_z = ND−(D−a−jK).                 (3)

Both sums run over all intrinsic variables, including c, and have nonnegative summands and the second has strictly positive parameter weights. Each required component is finite. In particular, no row with b>N(ℓ+1)−1 can contribute. For N=1, only the x^b rows with b≤ℓ are relevant. This is a rigorous restriction on certificate multipliers in the FULL ideal, not a restriction of parameter support. If those rows prove c∈I, the proof is consumable; a completed failed membership test proves only c∉I and says nothing about c²,c³,… . Variables with b_z>N(ℓ+1) are unused in the entire relevant component and can be omitted, with no value assigned to them. At N=1 this reduces the first four intrinsic rings, including c, to 77,93,101,109 variables. A UNIT of the selected rows with c=1 is independently sufficient as a genuine generator-subset certificate. This restriction can drastically reduce the x bands even though raw finite blocks remain large.

The exact component counts from ∏_z(1−u^(b_z)v^(w_z))^(−1), including c, are: 77-parameter fibre, [u²v³⁹]=67,177,159; 111-parameter fibre, [u³v²⁹]=5,667,097; 129-parameter fibre, [u²v⁴¹]=31,667,827; 136-parameter fibre, [u³v²⁹]=24,153,138. These are ambient monomial counts before quotienting low equations, not matrix ranks, degree bounds, or nonmembership results. Parameter count alone misorders expected membership-block difficulty. Driver proof/grading_profiles.py enumerates all 12 parameter gradings and counts exactly; proof/grading-profiles.json binds the metadata hashes.

A completed weighted Gröbner computation through weight ND suffices to decide c^N membership, provided its order refines the positive weights and all required critical pairs of weight≤ND are processed, including the target degree. A finite truncation says nothing about powers beyond its range. A Hilbert-driven stop additionally needs a certified Hilbert function or equivalent completion argument; the ambient generating function above is not the quotient Hilbert series. An exact row-span certificate is often preferable because its multipliers and rational identity can be verified without trusting a solver's completion signal. Circuit graph presentations are homogeneous as well when an auxiliary is assigned the bidegree of the coefficient it represents; their monic graph relations preserve the original ideal under elimination, but adding auxiliaries changes ambient Hilbert counts.

There is a rigorous, impractically large fallback bound. Use the ordinary x,y coefficient presentation and eliminate c through its unique equation c=F (with the native sign convention handled explicitly). Every remaining coefficient polynomial has ordinary parameter degree≤d0=e+q. This follows from degree≤e in P coefficients and degree≤q in Q coefficients. Put r=#intrinsic parameters including c. In Q[z] with r−1 variables, c∈√I means F belongs to the radical of the remaining direct coefficient ideal. Replace any degree-two generator f by f². This keeps the radical, makes a subideal, and all generator degrees remain≤d0 because d0≥5 here. No generator now has degree two.

Kollár's Corollary 1.7 and Theorem 1.5, printed p.965, then give an exponent N≤d0^(r−1). Applying the bihomogeneous projection back in R yields a certificate at weight ND≤D*d0^(r−1). This invocation deliberately handles the paper's degree-two exception; it does not assume generic equations or finite-dimensional quotient. For the requested first four fibres the bounds are respectively 39·5^76, 29·5^110, 41·7^128, and 29·5^135. They prove a finite terminating search exists but are not a practical resource estimate. Source: J. Kollár, “Sharp Effective Nullstellensatz,” JAMS 1 (1988), 963–975, [primary PDF](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Kollar/kollarnullstellen.pdf). Primary-source PDF and text are retained here.

This yields an exact SINGLE universal decision target, not merely an unbounded search: put N*=d0^(r−1). Then

    c∈√I ⇔ c^N*∈I,
    universal bidegree = ((ℓ+1)d0^(r−1), D d0^(r−1)).

Indeed the bounded exponent s≤N* from Kollár can be increased by multiplication by c^(N*−s). Thus the first four universal targets are (2·5^76,39·5^76), (3·5^110,29·5^110), (2·7^128,41·7^128), (3·5^135,29·5^135). Their second coordinates have 55,79,110,96 decimal digits. These sufficient bounds are not remotely reachable here; they are not estimates of the minimum exponent. For fixed N, a completed test through exactly (N(ℓ+1),ND), using all eligible rows and multipliers in (3), decides that exponent alone. N=1 requires (2,39),(3,29),(2,41),(3,29), respectively. Neither a timeout below those targets nor a completed failure at N=1 decides radical membership.

The primary PDF printed p.965 was checked again; `resume-r2/math-audit.json` binds its hash and hypotheses. No genericity, Fröberg, or finite-socle assumption is used.

Certificate conversion is explicit: from c^N=Σ a_i f_i obtain 1=Σ T^N a_i f_i−(Tc−1)Σ_(k=0)^(N−1)(Tc)^k. All coefficients remain rational.

Mechanical implementation check: the retained `proof/row-grading-audit.json` checks 1,953,555 terms in the 111/129 native and direct files plus the licensed 425-row s4 control. Its count must not be called the count of all four requested direct files. Round 2 closes that custody wording gap: `resume-r2/audit_math.py` freshly verifies all 842 rows and 718,633 terms in the four full direct files, with exact source/custody hashes, variable order, bidegrees, unique c row and ordinary-degree bounds 5/5/7/5. This is recorded in `resume-r2/math-audit.json`. No header-only file is counted as an empty ideal.

Exact x-charge quotient for bounded membership. Write B(z)=b and B(c)=ℓ+1, and fix target (X,Y)=(N(ℓ+1),ND). Let M_X be the monomial ideal consisting of all monomials of B-charge>X. It is an ideal because every parameter has nonnegative B-charge. It is finitely generated, including every variable of charge>X. Then (M_X)_(X,Y)=0 and

    (I+M_X)_(X,Y)=I_(X,Y).

Therefore the image of c^N is zero in R/(I+M_X) iff c^N∈I. Weighted Gröbner computation in the qring R/M_X through positive weight Y is legitimate for this membership question and can suppress irrelevant larger-x computations. It is not a valid replacement chart for saturation: c^(N+1)∈M_X, so adding Tc−1 to that qring ALWAYS produces a unit ideal, even for I=0. Such a UNIT has no chart meaning.

For certificate custody, lift the quotient membership to c^N=Σ a_i f_i+Σ b_j m_j in R. Projection to (X,Y) removes the overflow part, whose multipliers would need negative first charge. Check the resulting rational identity c^N=Σ a_i,hom f_i by polynomial arithmetic in the original FULL ring. A quotient success string alone is insufficient; omitted coordinates are not asserted zero in the full chart.

Small exact torus cover. Independent target-polynomial analysis finds minimum positive-x monomial hitting set sizes 3,10,11,10 for the first four fibres (77,111,129,136 parameters). “Minimum” is relative to covering the support of the literal target polynomial F; reduction modulo other equations may admit better covers. For the 77-parameter fibre, its target equation is F−c=0, with the exact identity

    F = A3_2_0*(−4*h_0_1*h_0_0−2*B2_0_1)
      + B2_1_0*(h_0_0*A2_1_1+h_0_1*A2_1_0+A3_1_1)
      + B2_1_1*(−h_0_0*A2_1_0−A3_1_0).

Thus (F)⊆(A3_2_0,B2_1_0,B2_1_1). At every c=1 solution one of these three coordinates is nonzero. Their residual torus characters are −30,−7,−9, respectively. Each corresponding open set has a section with that coordinate equal to 1 and c still equal to 1. The three full-equation sections cover all c≠0 torus orbits; no zero-prefix conditions are required, and intersections between sections are harmless. All three exact-Q UNITs would kill the full completed fibre/class. Solving fewer sections leaves the remaining opens unproved.

The minimum support-cover computation, exact identities F=Σ z q_z for all four targets, residual characters, source hashes, full branch equations, preserved generator orders, and explicit ring maps are in proof/torus_branches/. The three 77-parameter scripts retain every one of the 150 direct coefficient generators and all 75 coordinates other than c and its chosen gauge coordinate. Driver proof/torus_hitting_sets.py emits Singular dp and msolve p=0/p=1073741827 inputs. proof/verify_torus_branches.py checks cover identities in Singular and every branch generator image by independent exact rational sparse-polynomial arithmetic; the msolve inverse rename must reproduce the same complete branch list.

**The four direct presentations are fully checked.** Reconstructed 77/136 rows come from every native pre-division H_j block;111/129 use their existing completed direct rows. The ordinary-coefficient presentation preserves exactly the completed ideal and all parameter support, by the monic basis argument above.

There is an independent exact symbolic check over Q in all intrinsic parameters, stronger than evaluating at sample points: reconstruct the complete polynomial from the emitted rows, independently form P and Q from the actual source builder's h, AA_i, BB_i definitions, and compare with diff(Q,x)diff(P,y)−diff(Q,y)diff(P,x)−cx^ell. All four differences are identically zero. A deliberate +1 perturbation is nonzero in all four. The source uses the native Q,P ordering; relative to J(P,Q), c_native=−c_(P,Q) and T_native=−T_(P,Q), preserving Tc−1. The coefficient ideal and both torus sections are invariant under that explicit sign map.

| Completed fibre | Intrinsic parameters incl. c | Direct rows | Nonzero terms | c weight | c=1 solver variables |
|---|---:|---:|---:|---:|---:|
| Mm12_m2_5 / V1_1_6 | 77 | 150 | 33,030 | 39 | 76 |
| M2_9 / V3_8 | 111 | 167 | 74,878 | 29 | 110 |
| Mm15_14 / V1_9 | 129 | 177 | 239,501 | 41 | 128 |
| M2_9 / V1_8 | 136 | 348 | 371,224 | 29 | 135 |

`ops/verify_direct.py` is the independent checker; its scripts, logs and summary are under `validation/`. It additionally inverse-maps every renamed msolve polynomial, for both characteristic zero and p=1073741827, and compares it with the exact c=1 image of its declared source row. Variable order, full generator order, source hashes, and all maps are explicit in each `instrument/<stem>/custody.json`. Matching variable names alone is not used as a ring-map argument.

The term audit supplements the proof for all twelve completed fibres. Homogeneous monic Horner graph extensions remain legitimate under their explicit elimination maps; intrinsic and auxiliary variable counts are kept separate.

**Degree truncation is tested as an actual algorithm.** Singular must use `std` and one positive weighted `wp` block for the declared weighted degree cutoff. A block order or `slimgb` can interpret degree differently. Small positive and negative controls verify the installed behavior. For example in Q[b,a] with weights (2,1), I=(b²−a⁴,ab), cutoff4 leaves a⁵ unreduced, while cutoff5 reduces a⁵ to zero and leaves a⁴ nonzero; a⁵=−a(b²−a⁴)+b(ab) verifies the membership identity directly. The supplied truncated controls intentionally distinguish a finite-degree result from a full standard basis.

**Finite certificate computations: all four first-power tests are settled.** Over Q, **c∉I on each of the 77, 111, 129, 136 completed fibres**. Thus every possible c-power certificate has N≥2. This is a negative ideal-membership result, not radical nonmembership, a c≠0 point, or a class kill.

The certificates give explicit homomorphisms from each FULL quotient R/I to a smaller rational algebra where c survives. For 111/136, send charge-zero coordinates and declared omitted positive-charge coordinates to zero, fixing the retained coordinates and c; use positive degree B and cutoff 3. For 77/129, send every charge-zero coordinate z to t^w(z), with deg(t)=(0,1), retain the declared positive-charge coordinates and c, and send omitted positive-charge coordinates to zero. Use H=w+(D+1)B, with cutoffs 119/125. These total polynomial maps preserve both gradings; t remains an indeterminate.

Let G be the saved rational polynomial list and M the ideal of all monomials beyond the stated positive-degree cutoff. Every full source row maps into (G)+M: all eligible images divide exactly to zero by G, and every omitted row has larger degree. For the curve receivers the smallest omitted source degrees are123/139, strictly beyond 119/125. Verify every required S-pair through the cutoff. The bounded Buchberger criterion proves that the saved nonzero NF(c) survives in A=Q[receiver variables]/(G+M), hence c∉I. No reverse assertion G⊆image(I) is needed for this negative proof. Membership in I would persist under the map, contradicting its nonzero image.

| Fibre | Full rows / terms audited | Eligible rows / nonzero images | Saved basis | Exact required S-pairs | NF(c) |
|---|---:|---:|---:|---:|---|
| 77 | 150 / 33,030 | 77 / 77 | 382 | 775 | c |
| 111 | 167 / 74,878 | 78 / 67 | 60 | 466 | c |
| 129 | 177 / 239,501 | 70 / 70 | 67 | 256 | 21 nonzero terms |
| 136 | 348 / 371,224 | 87 / 76 | 68 | 574 | c |

Independent Python Fraction verifiers reproduce source images and polynomial division; a second independent audit starts from ALL original direct rows and verifies the total maps, both gradings, 2,071 required S-pairs and saved remainders. A basis row reduces to zero; adding c produces the nonzero remainder; 1 stays nonzero. Complete rational bases, source hashes, ordered rings, maps and controls are under `resume-r2/{triangular,truncation}/`; `resume-r2/nonmembership-second-audit.{md,json}` and `audit_nonmembership.py` unify the four proofs.

In all four witness algebras c²=0 automatically because of the degree overflow. Therefore these certificates cannot prove radical nonmembership or supply a geometric point with c≠0. A UNIT or zero c² remainder after these parameter maps would not prove a positive statement in the original chart. This direction distinction is essential to FALLACY-v2.

The triangular computations are also complete as algebraic reductions. Rational DAGs eliminate 27/71 unit pivots from the full 77/136 presentations, leaving 50/65 coordinates. A compact recursive circuit replay checks every pivot identity and rejects each +1 perturbation, without expanding millions of terms. In the N=1 component the 136 chart has 49 eligible pivots and 60 remaining coordinates, with 5,209,906 ambient monomials; 77 has 18,574,576. Corrected exact replay confirms 42/37 substitutions for111/129. The original replay's declaration and ideal-comparison errors were rejected. The early curve checker with an undefined lcm routine was likewise rejected; independent rational arithmetic and a clean Singular check replace it. No success marker from an erroneous script is consumed.

The 77/136 strict-low subsystems contain 147/338 rows; the111/129 counts are 157/168. Every one admits z=0,c=1. All four expensive direct/pivot-order N=1 attempts on .67 were explicitly stopped after the exact nonmembership proofs; their actual rc1 and cancellation reasons are retained, not renamed timeouts.

Bounded N=2 probes also ran on all four fibres, retaining every source row eligible by first charge. Zero remainders were returned by the 77 curve,111 zero-charge,129 selected-curve and136 zero-charge probes. The fuller 136 curve probe timed out at 600 s. These specialized/truncated zero outputs are unpromoted solver dispositions; they establish neither c²∈I nor c²∉I in the original charts. The further full 77 test retains all 150 original rows, uses the reversed pivot order with positive weights w, and targets c² at (4,78) through weight 78. It timed out rc124 after 1200.03 s under 128 GiB, without a completed basis or rational identity; original c² membership remains OPEN.

**Adopted fleet and full saturation attempts.** Ownership is established by round-1 `ops/owned-worker*.json`, launch records, status host fields and EC2 launch times: `.67`=`i-05bbedf0197e8eee3` launched 13:50:31Z, `.86`=`i-02aaa996f54d2c004` launched 13:56:42Z, both r7i.16xlarge. Both were adopted; no additional worker was launched. The requested `sh fleet.sh ips` rejected Bash's pipefail option, so the same fleet script was run with Bash. Other instances were neither used nor terminated, including .7/.18/.28.

The two inherited msolve slices were already FINISHED rc124 when reached: 77 took 1,201.84 s and peaked 71,234,288 KiB RSS; 111 took 1,200.86 s and peaked 32,639,412 KiB. These were time limits, not fresh memory-allocation failures. Each had a 420 GiB address-space limit. The inherited exact-Q Singular full slices timed out at 600 s, and all three 77 second-torus Q branches timed out at 900 s.

| Full chart / section | msolve modular full | Singular Q full | Additional exact-Q sections |
|---|---|---|---|
| 77 | rc124,1200s | std rc124,600s | 3/3 torus branches: std900s and slimgb1800s, all rc124 |
| 111 | rc124,1200s | std rc124,600s | full slimgb rc124,1800s |
| 129 | rc124,1800s | std rc124,1800s | none |
| 136 | rc124,1800s | std rc124,1800s | none |

All entries are TIMEOUT/OPEN, with no basis verdict. Round-2 msolve peaks were 23,260,020 KiB for 129 and 98,170,236 KiB for 136, below their 180 GiB limits. The observed obstruction was bounded computation time; these runs did not report allocation failure.

All full c=1 jobs preserve the declared complete direct generator lists and all remaining coordinates. Singular runs use Q and dp; msolve 0.10.1 runs use p=1073741827, grevlex, 16 threads, -g2, linear-algebra 44, and a 2,000-pair batch in round2. Modular output is only a signal; the msolve first-prime output is never relabelled exact Q. The three 77 torus branches are the complete proved cover, but timeouts on them establish no cover emptiness. The slimgb variants change only std(I) to slimgb(I); exact rational unit/nonunit and lifted-identity controls pass.

Final custody is in `resume-r2/execution-custody.json`, `run-summary.json`, and the two subtask disposition records. They retain exact commands, variable and generator orders, fields, input and executable hashes, actual return codes, time/RSS, output hashes and cancellation causes. The final `resume-r2/final-custody.sha256` manifest binds the lane artifacts and is mechanically checked. Positive UNIT promotion requires a valid exact-Q computation or a rational original-ring identity; no such result occurred. This lane certifies zero class kills. The four first-power obstructions are complete; higher-power membership and all saturation claims remain OPEN.

Both owned workers were terminated with `bash ops/fleet/fleet.sh term <ID>` after harvesting: `.67` first, then `.86`. The final EC2 record `resume-r2/owned-instances-final.json` confirms TERMINATED for both exact IDs. All 33 status-recorded invocations are finished and all their declared input/output hashes match. Operational cutoff: 15:14:00Z (54m30s in round2), within 150 min. No ledger, jc2-lean, ideation, or other-lane worker was changed. The frozen draft remains byte-identical to its charged hash.


<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `29377`.
- Body SHA-256:
  `18090f534fea730b2bf2cd884080c6d8abcc04f5ea3a0e154f3dec2b7214003c`.
- Frozen basis: `dd24342e1eca2a44ee9c603bce9361efb56512a5`.
