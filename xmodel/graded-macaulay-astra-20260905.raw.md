**Graded Macaulay computation — Astra — 2026-09-05**

**Disposition: exact N=2,3 sizes are computed for all four full fibres and the licensed s′=4 control. Every requested target matrix exceeds the proposed 10⁷-column threshold, including after a proved minimal-variable polynomial presentation. The smallest reduced N=2 matrix has 6,782,152,172 columns. Exact rational sparse linear algebra supplies full-ideal Hilbert truncations in smaller degrees; target ranks, c²/c³ membership, and class emptiness remain OPEN. Zero class kills are certified. No Gröbner basis was computed and no fleet instance was launched.**

**Custody and scope.** Work began at 15:19:17 UTC, with receipt basis `4536d3fff7d8a13898168dbe430d163b1a0be731`. Before reading charged mathematical contents, awk joined the six numbered `charged_input_<i>_sha256` and `_basename` fields of `xmodel/graded-macaulay-astra-20260905.run.v2`; `sha256sum -c` returned six OK results against `/tmp/jc2-lane.f1FF7T/inputs/`. The first manifest write into the frozen directory was rejected as read-only; moving only the manifest into this lane succeeded. There was no content mismatch. `inputs.sha256` and `inputs-check.log` retain the receipt-derived manifest and check. All abbreviated artifact paths below are relative to `box/graded-macaulay-20260905/`.

The consumable family remains `box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes/`, with independent union supports D_i∪G_i, β₁=0, and the stated terminal constant gauges. The JSON outputs bind source/metadata hashes, ring and generator orders, and degrees. No source parameter is specialized in the new full-ideal computations.

The gate §8 permits a class kill only after an actual exact-Q UNIT or rational original-ring identity on one completed fibre, using its common G_i embedding. This lane consumes that source-support theorem and the frozen census/descent dependencies; it does not re-prove or strengthen them. The closeout’s remaining named source obligations are not silently discharged by these counts. No new exit-price assertion is made, so no charge_basis line is due. No ledger, jc2-lean, or ideation file was edited.

**Four rings and the target degrees.** Write B(z)=b, w(z)=iK−a, p=ℓ+1, D=n+m−1, C=(p,D). Variables include c, with degree C, and exclude the inverse variable T. The first charge negates the earlier signed convention. The source Jacobian ordering is the audited native Q,P ordering. Switching to P,Q changes c’s sign, which must also be reflected in any identity. We preserve the native target equation F−c throughout.

| Parameters | Completed fibre M/V | K | (p,D) | δ₂ | δ₃ | Direct generators |
|---|---|---|---|---|---|---|
| 77 | m12_m2_5/V1_1_6, s′=4 | 8 | (2,39) | (4,78) | (6,117) | 150 |
| 111 | 2_9/V3_8 | 6 | (3,29) | (6,58) | (9,87) | 167 |
| 129 | m15_14/V1_9 | 6 | (2,41) | (4,82) | (6,123) | 177 |
| 136 | 2_9/V1_8 | 6 | (3,29) | (6,58) | (9,87) | 348 |

Direct rows mean every ordinary x,y coefficient of the audited completed Jacobian. Their ideal agrees with the native h-adic coefficient ideal by the invertible monic triangular coefficient transformation established in the frozen report. The 77 fibre IS the s′=4 control; it is not an additional fifth fibre. Its licensed alternate native list has 425 rows and SHA-256 `af3cf058c7e949d7e9958b1c9120b9350436c6eca7a952afbc8ea32f9794ef58`. The builder-identity custody is inherited and checked against the gate’s actual union control. Header-only files are never counted as empty ideals.

**Finite linear system and exact counting method.** For a coefficient row g at native position (j,b,a), deg(g)=(b+1,D−a−jK). Every monomial multiple of that degree contributes one generated row. Set

    h(X,Y) = [u^X v^Y] ∏_(z including c) (1−u^B(z) v^w(z))^(−1),
    columns(M_(X,Y)) = h(X,Y),
    generated_rows(M_(X,Y)) = Σ_g h(X−B(g),Y−w(g)).

A negative complementary coordinate contributes zero. The count is by the declared ordered generator presentation: dependent or repeated rows are still rows. Within each row, distinct original terms remain distinct after monomial multiplication, so the exact sparse input nnz count is Σ_g size(g)·h(δ−deg(g)). It is an input count, not a rank or a prediction of elimination fill.

The variable-by-variable unbounded-knapsack recurrence starts at h(0,0)=1 and adds h(X−B(z),Y−w(z)) in increasing indices. Its integers have arbitrary precision. An independent grouped convolution uses the coefficient binomial(k+t−1,t) for t copies of a degree occurring k times. These methods agree at EVERY entry of the rectangles through 3C, not merely the target entries. The count driver also verifies 1,618 source rows and 2,357,809 distinct nonzero terms across all counted presentations. N=1 reproduces 67,177,159 / 5,667,097 / 31,667,827 / 24,153,138 original columns in fibre order.

Bihomogeneity gives c^N∈I exactly when its vector lies in this row space. All omitted higher-degree rows or variables have no monomial capable of reaching δ_N; omission from a component assigns them no value. This is the complete original-ideal degree block, rather than a parameter specialization.

| Fibre | N | δ_N | Columns | Generated rows | Input nonzeros |
|---|---|---|---|---|---|
| 77 | 2 | (4, 78) | 2,173,263,807,826 | 7,739,145,216,105 | 578,249,602,766,164 |
| 77 | 3 | (6, 117) | 7,872,244,687,495,969 | 45,327,198,982,606,969 | 4,595,588,864,599,880,497 |
| 111 | 2 | (6, 58) | 137,012,693,048 | 334,303,684,260 | 23,755,539,424,633 |
| 111 | 3 | (9, 87) | 518,941,050,672,107 | 1,819,581,485,129,325 | 201,878,995,789,733,317 |
| 129 | 2 | (4, 82) | 1,809,679,091,378 | 2,739,296,550,558 | 515,676,697,172,721 |
| 129 | 3 | (6, 123) | 13,593,638,842,081,849 | 30,066,331,094,247,691 | 9,360,202,154,693,600,881 |
| 136 | 2 | (6, 58) | 1,419,917,816,025 | 3,078,242,780,365 | 314,198,796,104,316 |
| 136 | 3 | (9, 87) | 10,646,231,492,188,445 | 33,980,530,027,024,206 | 5,744,399,851,371,692,167 |

The number of direct generators with a nonzero multiplier component at N=2/N=3 is respectively 141/150, 135/164, 123/159, and 171/252. Merely testing componentwise degree inequalities can overcount active generators: some nonnegative complementary bidegrees contain no monomial. Every source contribution and complementary degree is retained in `counts/ambient-counts.json`.

The native presentation changes generated row counts while preserving the row space and column space. Its alternate counts are below; columns are exactly those in the preceding table for the same fibre and N. The 425-row control is therefore explicitly counted in its own preserved presentation, not replaced silently by the 150-row direct list.

| Fibre | Native generators | N | Generated rows | Input nonzeros |
|---|---|---|---|---|
| 77 | 425 | 2 | 7,739,343,467,721 | 1,100,043,162,897,715 |
| 77 | 425 | 3 | 45,505,693,933,918,581 | 13,450,672,889,193,081,545 |
| 111 | 174 | 2 | 331,384,782,309 | 19,723,072,209,347 |
| 111 | 174 | 3 | 1,794,052,584,170,196 | 205,181,815,229,319,289 |
| 129 | 177 | 2 | 2,739,296,550,558 | 278,315,165,167,692 |
| 129 | 177 | 3 | 30,066,331,094,247,691 | 5,150,679,149,867,014,982 |

**Exact N-independent elimination and minimal number of variables.** The phrase “charge-zero eliminations” needs correction. All 27/71 frozen unit pivots have B>0. Every generator has B≥1, hence I_(0,Y)=0 for every Y: no nonzero homogeneous relation can eliminate a B=0 coordinate. The 38/28/40/28 charge-zero coordinates remain a free polynomial subalgebra. Also no non-c coordinate has residual torus character pw−DB equal to zero, since gcd(p,D)=1 and 1≤w≤n<D.

Fresh full-row processing finds every positive-charge A coordinate as a constant-unit pivot. There are 27/57/57/71 such coordinates. For each ordered source equation q_j a_j+P_j=0, q_j∈Q*, the driver verifies that a_j occurs exactly once and every other pivot dependency precedes it. It defines φ(a_j)=−φ(P_j)/q_j, fixing all remaining variables and c. Each equation is homogeneous and every image vanishes at the origin. The recursive map and the inclusion of remaining coordinates into the quotient are inverse algebra maps. Imposing the images of ALL remaining source rows therefore gives the full chart quotient, with no localization or discarded branch.

The frozen 111/129 lists of 42/37 pivots include c and came from N=1 selected rings. Their counts remain in `counts/reduced-ambient-counts.json`. The full positive-A lists here are stronger; 77/136 reproduce the frozen 27/71 lists.

After removing pivot rows, additional identically zero source images number 3/3/0/11. The surviving ordered image lists have 120/107/120/266 nonzero generators. To establish those numbers without expanding enormous nonzero polynomials, the driver evaluates the recursive rational map at two recorded finite-field points, using p=1073741827. A NONZERO value certifies that the rational polynomial is nonzero; this is not modular ideal-membership promotion. Every remaining zero candidate is composed and checked exactly with FLINT rational multivariate polynomials. The source indices, pivot equations, all point values, residues, and exact zero indices are retained in `reduced/<fibre>/reduced-counts.json`. Independent audit confirms the source-index/position correspondence.

One further global unit equation is φ(F)−c. Eliminate c and write S=Q[u] and J for the images of all other rows. Then R/I≅S/J as bigraded Q-algebras, c maps to F̄=φ(F), and the target becomes F̄^N∈J. This is the smallest possible number of polynomial coordinates for the FULL affine algebra, not just a convenient reduction: the independent exact Fraction audit computes the original linear-part ranks, verifies all residual linear parts vanish, and obtains the cotangent dimensions at the rational origin. Any presentation by s polynomial generators induces a surjection Q^s→𝔪/𝔪², so s must be at least that dimension. Our presentations attain the bound.

| Fibre | A pivots | Linear rank incl c | Coordinates retaining c | Minimal coordinates after c | Nonzero generators of J |
|---|---|---|---|---|---|
| 77 | 27 | 28 | 50 | 49 | 119 |
| 111 | 57 | 58 | 54 | 53 | 106 |
| 129 | 57 | 58 | 72 | 71 | 119 |
| 136 | 71 | 72 | 65 | 64 | 265 |

Minimality here concerns polynomial generators of the full affine Q-algebra. It is not a Krull-dimension assertion and does not bound coordinate counts after localization or on the c=1 section. The generators of J are the ordered nonzero source images; no claim of a minimal ideal-generating list is made. `audit/minimality.json` independently verifies ranks 28/58/58/72 and cotangent dimensions 49/53/71/64 using all 842 direct rows.

Let h_A count the A-pivot quotient with c retained and h_S count the c-free polynomial ring. The exact identity h_S(X,Y)=h_A(X,Y)−h_A(X−p,Y−D) holds throughout every computed rectangle. Applying the same generator×complement rule gives:

| Fibre | N | Columns, c retained | Rows, c retained | Columns in minimal S | Rows for J |
|---|---|---|---|---|---|
| 77 | 2 | 199,868,375,503 | 944,963,908,931 | 199,849,800,927 | 944,918,324,651 |
| 77 | 3 | 253,021,215,038,760 | 2,274,459,643,503,149 | 252,821,346,663,257 | 2,273,314,829,793,291 |
| 111 | 2 | 6,783,223,313 | 3,763,666,560 | 6,782,152,172 | 3,762,385,613 |
| 111 | 3 | 6,941,217,913,524 | 7,510,952,733,340 | 6,934,434,690,211 | 7,500,406,914,608 |
| 129 | 2 | 223,956,685,248 | 11,869,895,680 | 223,946,470,992 | 11,859,659,200 |
| 129 | 3 | 645,926,870,167,810 | 140,536,245,414,981 | 645,702,913,482,562 | 140,300,429,048,309 |
| 136 | 2 | 84,272,526,796 | 42,139,064,212 | 84,267,316,890 | 42,133,172,370 |
| 136 | 3 | 180,791,914,571,260 | 189,576,590,775,130 | 180,707,642,044,464 | 189,450,184,394,028 |

`counts/independent-reduced-check.json` checks all 2,004 source contributions and both dynamic programs throughout the reduced rectangles. Reduced expansion can enlarge row support; original term counts cannot estimate its sparse storage.

**The torus section is valid but does not make this finite block smaller by itself.** Setting c=1 identifies the nonzero-c localization with its section times G_m, as proved in the frozen report. On the vector space R_(NC), however, the substitution c↦1 is INJECTIVE. A z-monomial has at most one exponent j making z^α c^j have degree NC. Its image is precisely

    ⊕_(k=0)^N Q[z]_(kC).

Thus the finite section window has exactly the same column count as the homogeneous block, and the target maps to 1. The inherited row images must be kept within this window. If A₀p+B₀D=1, the window is residual character zero with 0≤k=A₀B(z^α)+B₀w(z^α)≤N. Residual character zero alone is infinite-dimensional: there are positive and negative residual weights, whose monomials supply a nonconstant character-zero monomial and all its powers. Dropping the finite window changes the fixed-N question.

The minimal S presentation uses c=F̄ and preserves the bigrading. A section UNIT needs rational lifting and homogenization to certify an exponent. Setting charge-zero coordinates to zero or t^w is a specialization, not a chart isomorphism.

**Which degree pieces vanish, and exact Hilbert information.** There is a complete N-independent answer for vanishing of the IDEAL pieces. For nonnegative integers (B,Y),

    I_(B,Y)=0 ⇔ B=0 or Y<λ(B),
    λ_77(B)=B; λ_111(B)=2B;
    λ_129(B)=ceil(13B/3); λ_136(B)=ceil(B/3).

All variable and generator degrees satisfy the displayed lower slope inequalities. For the converse, `hilbert/global_support_vanishing.json` supplies nonzero original generators in the necessary residue classes, a period variable, and a degree-(0,1) coordinate. Multiplying a residue generator by powers of the period coordinate and the (0,1) coordinate constructs a nonzero element of every claimed nonzero ideal piece; the original polynomial ring is a domain. Thus this is an exact support theorem for I, not an extrapolation from a finite numerical table. The corresponding ring component is zero below λ(B); where I_(B,Y)=0, the full quotient Hilbert value equals the ambient count.

In particular, H_(R/I)(0,Y) is exactly the coefficient of v^Y in ∏_(B(z)=0)(1−v^w(z))^−1. At the target second weights, these FULL quotient values are:

| Fibre | H(0,D) | H(0,2D) | H(0,3D) |
|---|---|---|---|
| 77 | 6,734,854 | 27,685,630,381 | 15,176,246,758,887 |
| 111 | 411,455 | 422,432,178 | 76,314,908,354 |
| 129 | 11,406,589 | 62,103,598,456 | 42,907,618,352,778 |
| 136 | 411,455 | 422,432,178 | 76,314,908,354 |

They refer to first charge zero, not to NC. These permanent polynomial directions prohibit any Artinian top-degree shortcut. Also every row of w<D is c-free and is satisfied by z=0,c=1. A strict-low-weight subsystem therefore cannot force c to vanish; if full forcing occurs, the minimum equation-weight threshold is D. Neither fact decides a higher c power.

**New full-ideal sparse linear algebra.** `hilbert/compute_hilbert.py` constructs finite original-ring Macaulay blocks, keeping every eligible original generator and multiplier, and computes their exact rational ranks with primitive integer Gaussian elimination. Integer cross-multiplication and gcd normalization preserve the rational row span. An independent modular pass uses p=1073741827. No critical-pair completion, polynomial leading-ideal substitution, or Gröbner algorithm is involved.

The exact cutoffs and completion counts are below. All cells are complete, with no component skipped by the configured column cap. Direct rational and modular ranks agree; exactness comes from rational arithmetic. One final cell is derived through the homogeneous unit quotient, as detailed below.

| Fibre | B range | Y range | Completed components | Elapsed seconds |
|---|---|---|---|---|
| 77 | 0…4 | 0…14 | 75 | 58.473 |
| 111 | 0…6 | 0…14 | 105 | 13.541 |
| 129 | 0…4 | 0…14 | 75 | 5.463 |
| 136 | 0…6 | 0…12 | 91 | 1681.19 |

| Fibre | (B,Y) | Columns | Rows | Exact rank | H_(R/I)(B,Y) |
|---|---|---|---|---|---|
| 77 | (2, 14) | 11,881 | 15,896 | 11,118 | 763 |
| 77 | (4, 14) | 13,129 | 36,947 | 12,836 | 293 |
| 111 | (3, 14) | 5,499 | 7,608 | 4,607 | 892 |
| 111 | (6, 14) | 104 | 327 | 97 | 7 |
| 129 | (2, 14) | 310 | 210 | 189 | 121 |
| 129 | (3, 14) | 10 | 7 | 6 | 4 |
| 136 | (3, 12) | 21,090 | 21,879 | 16,522 | 4,568 |
| 136 | (6, 12) | 80,415 | 146,269 | 76,595 | 3,820 |

For 136 at (6,12), the exact unit quotient has 8,765 columns, 5,554 rows and rank 4,945, hence H=3,820 and original rank 80,415−3,820=76,595. Its (5,12) value H=4,446 independently matches the completed direct calculation. The redundant original (6,12) run was stopped only after this proof; its partial echelon is unused. This final cell is typed EXACT_Q_VIA_HOMOGENEOUS_UNIT_MAP, not an invented original matrix completion.

The JSON files give full rectangular Hilbert tables, source hashes, computation-specific matrix/echelon hashes, pivot counts, and timings. All 718,633 terms in the four original direct files were freshly rechecked for degree and nonzero coefficients before constructing these matrices. Independent FLINT fmpq_mat/nmod_mat calculations reproduce four actual chart blocks and 100 deterministic random-matrix controls. Rational-combination replay passes a positive membership control; ordinary negative membership, a bad-prime false NO, and a bad-prime false YES are also checked.

These low-degree computations do not reach δ₂ or δ₃. No full target rank or exact target Hilbert value is claimed. The reduced counts do give rigorous intervals, since H_(S/J)(δ)=columns−rank and 0≤rank≤rows. The following lower bounds are arithmetic consequences of the c-free full presentation, rather than guessed Hilbert series:

| Fibre | N | H(NC) lower bound | H(NC) upper bound | Exact value |
|---|---|---|---|---|
| 77 | 2 | 0 | 199,849,800,927 | OPEN |
| 77 | 3 | 0 | 252,821,346,663,257 | OPEN |
| 111 | 2 | 3,019,766,559 | 6,782,152,172 | OPEN |
| 111 | 3 | 0 | 6,934,434,690,211 | OPEN |
| 129 | 2 | 212,086,811,792 | 223,946,470,992 | OPEN |
| 129 | 3 | 505,402,484,434,253 | 645,702,913,482,562 | OPEN |
| 136 | 2 | 42,134,144,520 | 84,267,316,890 | OPEN |
| 136 | 3 | 0 | 180,707,642,044,464 | OPEN |

A positive Hilbert dimension in a target component would not imply that its particular vector c^N survives. Conversely, an ambient column count is never a quotient Hilbert value. The bounds above respect that distinction.

The frozen exact N=1 witness algebras can be counted as well. Rechecking their custody and standard monomials gives witness dimensions at C of 1/2/21/2, with ambient receiver counts 448/190/605/206. Their total graded maps imply only H_(R/I)(C)≥1/2/21/2; the saved normal forms of c separately prove c∉I as already frozen. Those finite receivers have zero pieces at 2C and 3C because of their overflow cutoffs. Such zeros are NOT H_(R/I)(2C) or H_(R/I)(3C), and they prove no original membership. `audit/hilbert-audit.json` explicitly distinguishes these quantities. No old timeout or specialized zero remainder is promoted.

**Modular verdicts and the certificate boundary.** For the requested N=2,3 blocks, no modular membership test was executed: even the minimal ring exceeds the stated feasibility threshold. There is therefore no modular YES, modular NO, or rational c-power identity to promote.

For a future finite block M and target e, an unrestricted modular NO is not automatically exact. Clearing original coefficient denominators is insufficient. For example, take the primitive integer rows (1,1) and (1,1+p), and e=(1,0). Over Q the two rows span everything; modulo p they coincide and miss e. The exceptional prime destroys rank despite primitive rows and integral entries. A modular YES is likewise only a signal: the single row (1,p) contains e modulo p and does not contain it over Q.

The correct good-prime negative implication is conditional. Certify rank_Q(M)=rank_Fp(M)=r, for example using a modular nonzero r-minor for the lower bound together with an exact rational row factorization for the upper bound. If rank_Fp([M;e])=r+1, the augmented nonzero minor survives over Q and exact nonmembership follows. Equivalently, verify an exact rational separating vector v with Mv=0 and ev≠0. Agreement over several primes alone supplies no rational rank upper bound. Membership over Q reduces modulo every prime avoiding the denominators of a valid rational solution, but an unknown solution’s exceptional primes cannot be excluded by assertion.

For a positive signal, solve on identified support over Q or reconstruct with CRT, then multiply out the ORIGINAL full-ring identity Σ a_i g_i=c^N. If elimination was used, include the rational-unit pivot identities when transporting it back. If c=1 was used, homogeneous lifting must first give nonnegative c exponents. From an actually verified original c-power identity one obtains

    1 = Σ_i T^N a_i g_i − (Tc−1) Σ_(k=0)^(N−1) (Tc)^k.

Only that exact full-ring identity, with the completed source custody, supplies the requested gate §8 class kill. No saturation in an x-charge overflow ring is admissible: c becomes nilpotent there by construction, so adjoining Tc−1 always creates a false UNIT even for I=0. Projection onto the target degree can justify a lifted membership calculation, but the original identity must still be checked.

**Feasibility and operational disposition.** The explicit direct N=2 input for the 77 fibre has 578,249,602,766,164 nonzeros. Even a compact representation with four-byte values and eight-byte column indices needs more than 6.9 petabytes for its entries, before row pointers and elimination fill. After the minimal exact coordinate reduction, the smallest N=2 block is still about 678 times the requested 10⁷-column ceiling. This is an explicit matrix-size obstruction, not a Gröbner timeout, a rank conclusion, or a theorem excluding a future compressed algorithm.

Counts and the exact small blocks ran locally on the existing approximately 123 GiB host. The root reduction driver finished the four full unit-map audits/counts in about 17 seconds total; it expands only exact-zero candidates. Additional RAM was not required. Consequently the conditional fleet launch was not triggered: this lane owns no worker to terminate and touched no other worker. No msolve, Singular basis command, or guided_gb invocation was made. FLINT 0.9.0 was loaded read-only from the existing Python package directory; it was used for rational polynomial composition and matrix verification, not Gröbner computation.

All new drivers, outputs, exact maps, per-generator contributions, run records, and checksum manifests are confined to this lane directory; the sole report is the requested xmodel path. `run-status.json` records final local-job and fleet dispositions. `artifacts.sha256` binds the final lane artifacts and is mechanically checked before sealing. The frozen input manifest is checked again at closeout. No partial target matrix is labeled a completed test.

**Reproduction and final typed result.** Run from the repository root:

    python3 box/graded-macaulay-20260905/counts/exact_counts.py
    python3 box/graded-macaulay-20260905/reduced/reduce_counts.py
    python3 box/graded-macaulay-20260905/counts/check_root_reduced.py
    python3 box/graded-macaulay-20260905/audit/audit_minimality.py
    python3 box/graded-macaulay-20260905/hilbert/verify_support.py

The exact Hilbert commands and independently checked linear-algebra controls are retained with their final status records under `hilbert/`; each command preserves the full declared ring and all eligible original rows. `build_report.py` inserts numerical tables directly from the checked JSON results.

Completed: exact original/native/reduced N=2,3 column and row counts; minimal full-affine coordinate presentation; exact ideal support-vanishing theorem; full-ideal rational Hilbert truncations; careful finite torus-section interpretation; complete input/map/artifact custody. **OPEN[c²∈I], OPEN[c³∈I], and OPEN[c∈√I] remain on all four fibres. Exact target Hilbert values remain OPEN. Zero class kills; no ledger promotion.**

Operational closeout time: 2026-09-05 16:02:45 UTC, within the 180-minute limit measured from 15:19:17 UTC.

<!-- BODY-END -->

Seal (outside the body):

- Body: every byte through the unique standalone BODY-END marker and its terminating newline.
- Body bytes: `24472`.
- Body SHA-256: `5587ef5551fa6aaf49d9652bdddcdc31a2caa020a578bf31736d6becb87ee01f`.
- Frozen basis: `4536d3fff7d8a13898168dbe430d163b1a0be731`.
