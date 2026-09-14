Mathematical completion and independent audit for round 2

The draft's positive grading, cone, coefficient-ideal equivalence, and finite membership reductions are sound. The completed argument gives an exact rational Laurent-product description of the c≠0 chart, and a precise finite universal membership target. No mathematical statement here promotes a solver timeout, a modular result, or a failed small-exponent membership test to a class disposition.

**The completed receiver is a weighted affine cone.** Write p=ell+1, D=n+m−1, n=eK, m=qK, R=Q[z,c]. For h coordinates use block index i=1. Assign deg(z_ba)=(b,iK−a) and deg(c)=(p,D). All non-c variables have positive second degree, since 0≤a<K and i≥1; all first degrees are nonnegative. Give the formal extraction variables deg(x)=(−1,0), deg(y)=(0,1). Each monic block, including its leading y power, is homogeneous: h has degree (0,K), alpha_i and beta_i degree (0,iK), P degree (0,n), and Q degree (0,m). Consequently the Jacobian target polynomial has degree (1,D), and its ordinary coefficient row at x^b y^a has degree (b+1,D−a). Its native h-adic coefficient at x^b y^a h^j has degree (b+1,D−a−jK).

Monic h-adic division changes the finite y-basis by an invertible unitriangular matrix over R[x]. In each direction, every coefficient in R[x] is a polynomial R[x]-linear combination of the other coefficient list. Taking all x coefficients therefore gives equal ideals in R. This establishes equality of the ordinary and h-adic coefficient ideals, not merely equality of their zero sets. Every completed support D_i∪G_i and both stated gauges respect this argument.

The two-torus acts by z_ba↦lambda^b mu^(iK−a)z_ba and c↦lambda^p mu^D c. This is the action induced by h'(x,y)=mu^K h(lambda x,mu^−1 y), P'=mu^n P(lambda x,mu^−1 y), Q'=mu^m Q(lambda x,mu^−1 y). With lambda=1 the action extends to mu=0 and contracts V(I) to the origin. Thus the scheme is positively weighted homogeneous and its affine variety is a weighted cone. The ordinary scalar action need not preserve it. The native builder's Q,P Jacobian convention changes c by a sign relative to P,Q, which leaves every grading and saturation assertion invariant.

**The c=1 section is defined over Q.** The four distinct pairs (p,D) in the six classes are (4,27), (3,29), (2,39), (2,41), all coprime. Choose integers A,B with Ap+BD=1, respectively (7,−1), (10,−1), (20,−1), (21,−1). Define the possibly signed integer character k(z)=A b_z+B w_z and k(c)=1. Set S=R/(I,c−1), using bars for its non-c coordinates. There is an explicit Q-algebra isomorphism

    (R/I)[c^−1]  ≅  S[s,s^−1],
    c ↦ s,                  z ↦ s^k(z) zbar,
    s ↦ c,                  zbar ↦ c^−k(z) z.

Indeed a row of bidegree (u,v) maps to s^(Au+Bv) times its c=1 image; the inverse has the same property and both compositions are the identity. Negative powers are legitimate in these Laurent rings. In particular the c≠0 chart is a product of its c=1 section and G_m over Q. Therefore

    I+(Tc−1)=(1)  iff  I|c=1=(1)  iff  c belongs to radical(I).

This proof does not require the existence of rational solutions or a root extraction. Equivalently, normalize a c≠0 point by lambda=c^−A, mu=c^−B. The remaining torus has primitive cocharacter (lambda,mu)=(t^−D,t^p) and weights r(z)=p w_z−D b_z. Since 1≤w_z≤n<D and gcd(p,D)=1, every non-c residual weight is nonzero. A further section z=1 on z≠0 is exhaustive over algebraic closure; it can require roots when |r(z)|>1. A complete finite cover of such opens, proved from the target polynomial, is needed to infer a full-chart UNIT from these second sections.

Certificate clearing for the first section is explicit. If sum_i h_i(z) f_i(z,1)=1 over Q, let k_i=Au_i+Bv_i for the degree (u_i,v_i) of f_i. Expand each h_i into monomials. Choose M at least 0 and every k(m)+k_i appearing in the expansion. Substitution z→c^−k(z)z and multiplication by c^M gives the polynomial identity

    c^M = sum_i sum_(m in h_i) coeff(m) c^(M−k(m)−k_i) m f_i(z,c).

All exponents of c on the right are nonnegative; this identity can be checked in the original full ring. If desired take M≥1. A c-power identity then yields a Rabinowitsch unit identity by the draft's geometric-sum formula.

**The exact finite block for a chosen exponent.** For N≥1 put (X,Y)=(Np,ND). Since I is bihomogeneous,

    c^N in I  iff  c^N in span_Q{m f_i : deg(m)=(X,Y)−deg(f_i)}.

Here m ranges over monomials in every intrinsic variable, including c. Each component is finite because the second degree is strictly positive on every variable. For a native row (j,b,a), the required multiplier degree is (Np−b−1,ND−D+a+jK). Thus no row with b>Np−1 contributes, and no variable with first degree>X or second degree>Y occurs anywhere in this component. Omitting these coordinates from the component is exact and assigns no values to the full chart coordinates.

An exact rational row-span identity at this bidegree proves membership immediately. To obtain a negative membership result by a weighted standard basis, complete every required reduction and critical pair through second degree Y, in a positive weight order, retaining first degree≤X if the exact overflow quotient is used. A stopped or timed-out basis computation proves neither membership nor nonmembership. The ambient Hilbert generating function is not a quotient Hilbert function and gives no Hilbert-driven completion certificate.

Let M_X be the monomial ideal of first charge>X. Then (M_X)_(X,Y)=0 and (I+M_X)_(X,Y)=I_(X,Y). This justifies computing c^N in the quotient R/M_X. Any positive result must be lifted and projected to (X,Y), where all overflow-generator terms disappear because their multipliers would require negative first charge; the resulting full-ring rational identity is the final check. Saturating this quotient is invalid: c^(N+1) is already in M_X, so adding Tc−1 produces UNIT even when I=0.

**A finite universal radical-decision cutoff, with its hypotheses checked.** Use the ordinary coefficient presentation I=(g_1,...,g_t,F−c), where only the target row contains c. Every g_i and F has ordinary parameter degree at most d0=e+q: P has parameter degree≤e, Q has parameter degree≤q, and differentiation in x,y does not increase parameter degree. Put nu=r−1, the number of non-c intrinsic variables. This is the affine variable count required in Kollár's corollary, not r and not the number of variables after homogenization.

Discard zero g_i. Replace each g_i of degree exactly two by g_i² and call the resulting ideal J'. Then J'⊆J=(g_i), radical(J')=radical(J), and every resulting generator has degree different from two and at most d0, because d0≥5 here. No genericity, Artinian, or zero-dimensionality assumption is made. If c is in radical(I), then F vanishes on V(J'); Kollár's Corollary 1.7 and Theorem 1.5 give F^s in J' for some s≤d0^nu. Thus c^s is in I. Conversely any c-power membership implies c in radical(I). Hence the single conservative exponent N*=d0^(r−1) satisfies the exact equivalence

    c in radical(I)  iff  c^N* in I.

The forward direction uses c^(N*−s)c^s; testing every intervening power is unnecessary. Therefore one certified universal decision target is the single bidegree (p d0^(r−1),D d0^(r−1)). It is a sufficient cutoff, not a claim that the minimum necessary exponent is that large.

| Fibre parameter count | d0 | Conservative N* | Exact universal bidegree |
|---|---:|---|---|
| 77 | 5 | 5^76 | (2·5^76,39·5^76) |
| 111 | 5 | 5^110 | (3·5^110,29·5^110) |
| 129 | 7 | 7^128 | (2·7^128,41·7^128) |
| 136 | 5 | 5^135 | (3·5^135,29·5^135) |

The second coordinates have 55,79,110,96 decimal digits, respectively. None is a reachable exhaustive cutoff in this lane's resource budget. The N=1 component counts in the adopted draft, already between 5.7 million and 67.2 million ambient monomials, are counts of potential columns before taking any quotient, not evidence of a small universal matrix.

The actual direct degree histograms additionally show a linear non-target generator in each fibre and more than nu non-target generators. The product formula in Theorem 1.5 then sharpens this conservative bound to d0^(r−2): after the degree-two replacement, the smallest degree is 1 and the nu−1 largest degrees are at most d0. This one-factor improvement remains impractical and does not change any solver disposition. The table retains the draft's valid bound for continuity.

Primary source checked directly: János Kollár, “Sharp Effective Nullstellensatz,” Journal of the American Mathematical Society 1 (1988), 963–975, Theorem 1.5 and Corollary 1.7 on printed p.965; its proof of Corollary 1.7 is on p.967. The retained PDF's fourth page visibly confirms the degree-two exclusion, exponent s≤N', and the product bound. Definition 1.4 on printed p.964 uses nu+1 homogeneous variables, while Corollary 1.7 uses nu affine variables, so there is no off-by-one homogenization cost. Source: https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Kollar/kollarnullstellen.pdf . The PDF, text, and audit hashes are recorded in math-audit.json; kollar-p965.png is the inspected page rendering.

**The low-weight test has a complete negative result below D.** Every nonzero original coefficient row has positive second degree at most D, and c occurs only in the target row of degree D. Thus for every w0<D the row subsystem of weights≤w0 has the exact rational point z=0,c=1. It cannot force c=0. If the complete chart does force c=0, its smallest equation-weight threshold is exactly D; otherwise no threshold works. This settles every strict-low threshold without claiming that full forcing occurs. The witness belongs to the subsystem and makes no full-chart nonemptiness assertion.

There is more usable triangular structure than mere variable containment. A weight-d row is a constant Q-linear form in the variables of weight exactly d, plus a polynomial in variables of weights strictly below d: any product containing a weight-d variable and another positive-weight factor would exceed d. Therefore each weight stage has the form M_d z_d+P_d(z_<d)=0, with a constant rational matrix M_d; the first grading splits these matrices further by x-charge. Exact Gaussian elimination of a nonzero constant pivot is legitimate globally, with no nonzero-coordinate branch and no denominator involving a parameter. Rank-deficient stages leave free variables and polynomial compatibility conditions, so the grading does not imply that all equations are solvable by linear substitution. Since every non-c variable has weight≤n<D, the weight-D stage contains c as its only weight-D variable, with its single row F−c.

The b=0 subspace with all b>0 coordinates and c set to zero remains a positive-dimensional family of full-chart points; the adopted inventory gives dimensions D−1. Consequently the full quotient has no finite global socle cutoff. Any Artinian or Fröberg-based bound would need additional proved quotient hypotheses.

**Fresh round-2 term audit.** The retained round-1 row-grading-audit.json checks two native files, their two direct files, and the licensed 425-row s4 control; its 1,953,555-term count must not be described as the count of the four requested direct files. Round 2 closes that wording gap with resume-r2/audit_math.py and math-audit.json. The fresh audit checks the full direct files for 77/111/129/136 against their metadata and instrument custody hashes, declared variables in order, every source index, and every rational monomial: 842 rows and 718,633 terms pass. Counts by requested order are 150/33,030; 167/74,878; 177/239,501; 348/371,224 (rows/terms). It also checks the unique c row, the positive weight range, the constant-linear form of every top-weight occurrence, the Laurent character on every monomial, and ordinary parameter-degree bounds 5/5/7/5. These are exact presentation audits and do not assert any ideal is UNIT.
