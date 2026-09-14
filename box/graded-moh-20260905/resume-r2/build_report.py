from pathlib import Path
root=Path('box/graded-moh-20260905');p=Path('/tmp/jc2-lane.NOv2jX/inputs/report-draft-r1.md');s=p.read_text()
s=s.replace('Moh completed charts: grading, torus sections, and finite certificate computation','Moh completed charts — resumed grading and certificate lane — 2026-09-05')
s=s.replace('**Disposition at draft: the coefficient ideals are positively graded cones. Their saturation questions admit an exact c=1 torus section and finite bidegree membership computations. No class kill has yet been certified.** This draft will be replaced with final solver dispositions and sealed only after owned-worker termination.','**Disposition: the completed coefficient ideals are positively graded cones; the c≠0 chart is an explicit Laurent product of its c=1 section over Q. Exact finite bidegree tests and a rigorous universal cutoff are established. Class emptiness remains OPEN; no exact-Q UNIT or rational c-power identity has been certified.** Final solver and worker dispositions are recorded below.')
needle='**Custody and scope.** '
s=s.replace(needle,needle+'Round 2 began at 14:19:30Z with receipt basis `dd24342e1eca2a44ee9c603bce9361efb56512a5`. Before reading the charged mathematical contents, awk joined the seven numbered `_basename` and `_sha256` fields with the receipt input directory; `sha256sum -c` returned seven OK results. The mechanical manifest is `resume-r2/charged-inputs.sha256`, rooted at `/tmp/jc2-lane.NOv2jX/inputs/`. The charged 21,356-byte round-1 draft was adopted unchanged as evidence and developed below; its verified SHA-256 is `0c7237a34c50adf774e1ce973c38353108dc249e50653df5b5b14be6307a7bee`. Paths below are relative to `box/graded-moh-20260905/` unless otherwise specified.\n\n')
a=s.index('Global c gauge.');b=s.index('A second coordinate gauge',a)
s=s[:a]+'''Global c gauge, now over Q itself. Put p=ℓ+1. Choose integers A,B with Ap+BD=1: (7,−1),(10,−1),(20,−1),(21,−1) for (p,D)=(4,27),(3,29),(2,39),(2,41). Let k(z)=A b_z+B w_z and k(c)=1. With S=R/(I,c−1), the explicit inverse Q-algebra maps are

    (R/I)[c^−1] ≅ S[s,s^−1],
    c ↦ s, z ↦ s^k(z) z̄;       s ↦ c, z̄ ↦ c^−k(z)z.

A row of bidegree (u,v) maps to s^(Au+Bv) times its c=1 image, proving the maps descend and compose to the identity. Hence the c≠0 chart is the product (c=1 section)×G_m over Q, and

    I+(Tc−1)=(1) ⇔ I|_(c=1)=(1).

No rational-point assumption or root extraction is needed for this first gauge. It removes c and T: the solver has r−1 variables instead of r+1. An exact section identity Σ h_i(z)f_i(z,1)=1 converts to a full-ring c-power identity: expand h_i into monomials m, put k_i=A u_i+B v_i, and choose M≥1 and M≥k(m)+k_i for every term. Then

    c^M = Σ_i Σ_m coeff_m(h_i) c^(M−k(m)−k_i) m f_i(z,c).

Every exponent is nonnegative; exact multiplication in the original ring verifies the identity. The residual torus described above acts on S. '''+s[b:]
s=s.replace('This is a proved torus section, not a cap/prefix specialization. ','')
a=s.index('The ideal-membership bound is conditional only');b=s.index('Certificate conversion is explicit:',a)
s=s[:a]+'''This yields an exact SINGLE universal decision target, not merely an unbounded search: put N*=d0^(r−1). Then

    c∈√I ⇔ c^N*∈I,
    universal bidegree = ((ℓ+1)d0^(r−1), D d0^(r−1)).

Indeed the bounded exponent s≤N* from Kollár can be increased by multiplication by c^(N*−s). Thus the first four universal targets are (2·5^76,39·5^76), (3·5^110,29·5^110), (2·7^128,41·7^128), (3·5^135,29·5^135). Their second coordinates have 55,79,110,96 decimal digits. These sufficient bounds are not remotely reachable here; they are not estimates of the minimum exponent. For fixed N, a completed test through exactly (N(ℓ+1),ND), using all eligible rows and multipliers in (3), decides that exponent alone. N=1 requires (2,39),(3,29),(2,41),(3,29), respectively. Neither a timeout below those targets nor a completed failure at N=1 decides radical membership.

The fresh degree audit also permits the harmless one-factor improvement d0^(r−2): each direct non-target list has a linear row and more than r−1 rows, so Kollár's product uses one degree1 and at most r−2 factors≤d0. The conservative draft bound is retained above. The primary PDF's printed p.965 was checked again; `resume-r2/math-audit.json` records its hash and the degree hypotheses. No Fröberg or finite-socle assumption is used.

'''+s[b:]
s=s.replace('Mechanical implementation check: check_row_grading.py verifies every term of the five currently complete native/direct files, including the preserved 425-generator s4 control whose byte identity is separately licensed by the frozen gate. All 1,953,555 terms passed; row-grading-audit.json records exact paths, hashes, weights, counts, and degrees. These term checks supplement the general proof; no missing/header-only file is counted as an empty generator set.', 'Mechanical implementation check: the retained `proof/row-grading-audit.json` checks 1,953,555 terms in the 111/129 native and direct files plus the licensed 425-row s4 control. Its count must not be called the count of all four requested direct files. Round 2 closes that custody wording gap: `resume-r2/audit_math.py` freshly verifies all 842 rows and 718,633 terms in the four full direct files, with exact source/custody hashes, variable order, bidegrees, unique c row and ordinary-degree bounds 5/5/7/5. This is recorded in `resume-r2/math-audit.json`. No header-only file is counted as an empty ideal.')
s=s.replace('The grading audit is exhaustive at the term level on these four direct presentations.','The fresh round-2 grading audit is exhaustive at the term level on these four direct presentations.')
s=s.replace('Low-weight equations can still be used first for exact eliminations before adding weight D. The weight≤w0 equations involve only parameters of weight≤w0, because every parameter has strictly positive weight. Thus the staging is triangular in weights, not generally solvable by linear substitutions.','At weight d every row has the stronger form M_d z_d+P_d(z_<d), with a constant rational matrix M_d: a weight-d variable cannot multiply any positive-weight factor. Thus constant Gaussian pivots eliminate coordinates globally, without parameter denominators or omitted branches. Rank-deficient blocks leave free variables and nonlinear compatibility equations. Since all non-c weights are≤n<D, at weight D the only new variable is c in its unique row F−c. The staging is useful but does not make the remaining equations linear.')
s=s[:s.index('[FINAL COMPUTE, TORUS-COVER, EXACT PREPROCESSING, AND TERMINATION SECTIONS TO BE INSERTED]')]
(root/'resume-r2/report-foundation.md').write_text(s)
print('foundation bytes',len(s.encode()))
