Moh completed-chart grading: independent proof and exact limitations

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

Global c gauge. Every c≠0 point has a torus translate with c=1 (use an (ℓ+1)st root in λ, or a Dth root in μ). Thus

    I+(Tc−1)=(1)  ⇔  I|_(c=1)=(1).

The solver ring has r−1 variables after c=1, versus r+1 with c,T: two fewer variables, and the complete c=0 stratum is removed. This is a proved torus section, not a cap/prefix specialization. A second coordinate gauge z=1 is valid only on the open set z≠0. All x-dependent coordinates (b>0) supply a complete finite cover: if they all vanish, P and Q depend only on y, so J=0 and the target equation forces c=0. Their residual weights are nonzero, so each branch admits z=1 while maintaining c=1. An exact-Q UNIT on EVERY branch proves the complete chart empty. One arbitrary branch is insufficient. A smaller cover requires a proved implication or a hitting set for a validated expression of c; numerical nonzero observations do not provide it.

Low-weight staging has an exact limitation. Every native row has 1≤w(f)≤D, and c occurs only at weight D in the unique target row. For any w0<D, the subsystem of rows of weight≤w0 is independent of c. Its point with all other parameters zero and c=1 is a solution. Therefore it cannot force c=0. If the full ideal forces c=0, the minimum equation-weight threshold in this positive grading is EXACTLY D; if the full ideal does not, no threshold works. This statement determines the only possible threshold and proves all smaller thresholds fail, but does not assert that full forcing occurs. Low-weight equations can still be used first for exact eliminations before adding weight D. The weight≤w0 equations involve only parameters of weight≤w0, because every parameter has strictly positive weight. Thus the staging is triangular in weights, not generally solvable by linear substitutions.

No Artinian/socle shortcut follows. Set all b>0 coordinates and c to zero, leaving all b=0 coordinates arbitrary. This gives a closed affine subspace of V(I). Direct support enumeration finds dimension D−1 for each fibre: 26,28,38,40 as applicable. Consequently R/I is positive dimensional, its Hilbert series is not a polynomial, and there is no global finite socle degree. A Fröberg/truncated-socle guess needs additional proved hypotheses. The outer-disc numerical grading d(iK−a)−b is not positive on every D∪G coordinate; some D additions exceed the outer envelope. Formula (1), rather than that unverified positive grading, avoids the issue.

The useful truncation is a finite BIGRADED membership block. Let C=(ℓ+1,D). Because I is bihomogeneous, c^N∈I iff c^N belongs to the Q-linear span of all m f, where f is a declared homogeneous coefficient generator and m ranges over parameter monomials of degree NC−deg(f). For a native row (j,b,a), the multiplier must satisfy

    Σ_z b_z exponent_z = N(ℓ+1)−b−1,
    Σ_z w(z) exponent_z = ND−(D−a−jK).                 (3)

Both sums have nonnegative summands and the second has strictly positive parameter weights. Each required component is finite. In particular, no row with b>N(ℓ+1)−1 can contribute. For N=1, only the x^b rows with b≤ℓ are relevant. This is a rigorous restriction on certificate multipliers in the FULL ideal, not a restriction of parameter support. If those rows prove c∈I, the proof is consumable; a completed failed membership test proves only c∉I and says nothing about c²,c³,… . Variables with b_z>N(ℓ+1) are unused in the entire relevant component and can be omitted, with no value assigned to them. At N=1 this reduces the first four intrinsic rings, including c, to 77,93,101,109 variables. A UNIT of the selected rows with c=1 is independently sufficient as a genuine generator-subset certificate. This restriction can drastically reduce the x bands even though raw finite blocks remain large.

The exact component counts from ∏_z(1−u^(b_z)v^(w_z))^(−1), including c, are: 77-parameter fibre, [u²v³⁹]=67,177,159; 111-parameter fibre, [u³v²⁹]=5,667,097; 129-parameter fibre, [u²v⁴¹]=31,667,827; 136-parameter fibre, [u³v²⁹]=24,153,138. These are ambient monomial counts before quotienting low equations, not matrix ranks, degree bounds, or nonmembership results. Parameter count alone misorders expected membership-block difficulty. Driver grading_profiles.py enumerates all 12 parameter gradings and counts exactly; grading-profiles.json binds the metadata hashes.

A completed weighted Gröbner computation through weight ND suffices to decide c^N membership, provided its order refines the positive weights and all required lower-degree pairs are processed. A finite truncation says nothing about powers beyond its range. A Hilbert-driven stop additionally needs a certified Hilbert function or equivalent completion argument; the ambient generating function above is not the quotient Hilbert series. An exact row-span certificate is often preferable because its multipliers and rational identity can be verified without trusting a solver's completion signal. Circuit graph presentations are homogeneous as well when an auxiliary is assigned the bidegree of the coefficient it represents; their monic graph relations preserve the original ideal under elimination, but adding auxiliaries changes ambient Hilbert counts.

There is a rigorous, impractically large fallback bound. Use the ordinary x,y coefficient presentation and eliminate c through its unique equation c=F (with the native sign convention handled explicitly). Every remaining coefficient polynomial has ordinary parameter degree≤d0=e+q. This follows from degree≤e in P coefficients and degree≤q in Q coefficients. Put r=#intrinsic parameters including c. In Q[z] with r−1 variables, c∈√I means F belongs to the radical of the remaining direct coefficient ideal. Replace any degree-two generator f by f². This keeps the radical, makes a subideal, and all generator degrees remain≤d0 because d0≥5 here. No generator now has degree two.

Kollár's Corollary 1.7 and Theorem 1.5, printed p.965, then give an exponent N≤d0^(r−1). Applying the bihomogeneous projection back in R yields a certificate at weight ND≤D*d0^(r−1). This invocation deliberately handles the paper's degree-two exception; it does not assume generic equations or finite-dimensional quotient. For the requested first four fibres the bounds are respectively 39·5^76, 29·5^110, 41·7^128, and 29·5^135. They prove a finite terminating search exists but are not a practical resource estimate. Source: J. Kollár, “Sharp Effective Nullstellensatz,” JAMS 1 (1988), 963–975, https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Kollar/kollarnullstellen.pdf . Primary-source PDF and text are retained here.

The ideal-membership bound is conditional only in the necessary way: if no power belongs, the bounded exhaustive tests all fail. The bound makes that finite failed search a radical nonmembership decision, but completing it at these enormous degrees is not claimed. Any claimed class kill still requires an actual exact-Q UNIT on the correctly declared completed chart/torus cover, or a verified rational identity for c^N (convertible to a unit identity after Tc−1). Modular UNIT remains only a signal.

Certificate conversion is explicit: from c^N=Σ a_i f_i obtain 1=Σ T^N a_i f_i−(Tc−1)Σ_(k=0)^(N−1)(Tc)^k. All coefficients remain rational.

Mechanical implementation check: check_row_grading.py verifies every term of the five currently complete native/direct files, including the preserved 425-generator s4 control whose byte identity is separately licensed by the frozen gate. All 1,953,555 terms passed; row-grading-audit.json records exact paths, hashes, weights, counts, and degrees. These term checks supplement the general proof; no missing/header-only file is counted as an empty generator set.

Exact x-charge quotient for bounded membership. Write B(z)=b and B(c)=ℓ+1, and fix target (X,Y)=(N(ℓ+1),ND). Let M_X be the monomial ideal consisting of all monomials of B-charge>X. It is an ideal because every parameter has nonnegative B-charge. Its minimal monomial generators contain only positive-charge variables; they satisfy sumcharge−minimum_factorcharge≤X<sumcharge. There are finitely many, including each individual variable of charge>X. Then (M_X)_(X,Y)=0 and

    (I+M_X)_(X,Y)=I_(X,Y).

Therefore the image of c^N is zero in R/(I+M_X) iff c^N∈I. Weighted Gröbner computation in the qring R/M_X through positive weight Y is legitimate for this membership question and can suppress irrelevant larger-x computations. It is not a valid replacement chart for saturation: c^(N+1)∈M_X, so adding Tc−1 to that qring ALWAYS produces a unit ideal, even for I=0. Such a UNIT has no chart meaning.

For certificate custody, lift the qring membership to c^N=Σ a_i f_i+Σ b_j m_j in R, with the original declared coefficient rows f_i and monomial quotient generators m_j. Project to bidegree (X,Y). Every coefficient multiplying m_j would require negative x-charge, so its projected contribution is zero. Replace a_i by its component of degree (X,Y)−deg(f_i). The resulting rational identity c^N=Σ a_i,hom f_i is checked by ordinary polynomial arithmetic in the ORIGINAL full ring. This projection is the essential final gate; a qring success string alone is not a certificate. High-charge coordinates omitted by the qring are not asserted zero in the full chart.

Small exact torus cover. Independent target-polynomial analysis finds minimum positive-x monomial hitting set sizes 3,10,11,10 for the first four fibres (77,111,129,136 parameters). “Minimum” is relative to covering the support of the literal target polynomial F; reduction modulo other equations may admit better covers. For the 77-parameter fibre, its target equation is F−c=0, with the exact identity

    F = A3_2_0*(−4*h_0_1*h_0_0−2*B2_0_1)
      + B2_1_0*(h_0_0*A2_1_1+h_0_1*A2_1_0+A3_1_1)
      + B2_1_1*(−h_0_0*A2_1_0−A3_1_0).

Thus (F)⊆(A3_2_0,B2_1_0,B2_1_1). At every c=1 solution one of these three coordinates is nonzero. Their residual torus characters are −30,−7,−9, respectively. Each corresponding open set has a section with that coordinate equal to 1 and c still equal to 1. The three full-equation sections cover all c≠0 torus orbits; no zero-prefix conditions are required, and intersections between sections are harmless. All three exact-Q UNITs would kill the full completed fibre/class. Solving fewer sections leaves the remaining opens unproved.

The minimum support-cover computation, exact identities F=Σ z q_z for all four targets, residual characters, source hashes, full branch equations, preserved generator orders, and explicit ring maps are in torus_branches/. The three 77-parameter scripts retain every one of the 150 direct coefficient generators and all 75 coordinates other than c and its chosen gauge coordinate. Driver torus_hitting_sets.py emits Singular dp and msolve p=0/p=1073741827 inputs. verify_torus_branches.py checks cover identities in Singular and every branch generator image by independent exact rational sparse-polynomial arithmetic; the msolve inverse rename must reproduce the same complete branch list.
