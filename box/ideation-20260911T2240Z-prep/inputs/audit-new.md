### DS-INV-1. Exact-support scalar-pair invariantization — PROVED-HERE / PROMOTED, 2026-09-11

- [ROOT proof](xmodel/danielewski-invariantization-root-20260911.md), SHA
  28fb540a4bb834ad40d1aa0349b8a2458cf7665951484e4896638f18275e3189;
  expected artifact manifest8f77443b5e8cd281b5127b97a13a1a9a413ed76a33ec56e38fe63c30e03c0eac
  VERIFIED. [FIRST Fable](xmodel/danielewski-invariantization-gate-fable5-20260911.md),
  SHA688ce2cafce3ef85593468f517de850098ee801ee9a82dbcf762dc6b5a6fdae5;
  receipt2fb860155733c7591c4de419872cc46813959e33bc87f651bd330d80461ddc0b.
  Terminal/process absence preceded receipt-FIRST; all retained pins match,
  composed prompt/sandbox hashes reproduced; report read WHOLE. Exact scope
  and custody in [ROOT intake](box/danielewski-invariantization-gate-fable5-20260911/INTAKE.md).
- Over C, T={t^2-1=x^2Z}, S={U^2=A+A^2Z}, sigma=(-x,-t,Z). The classical
  maps q=(x^2,xt,Z), j=(2U,1+2AZ,Z), E=j q=(2xt,2t^2-1,Z) satisfy
  q*Omega=omega, j*omega=2Omega, E*omega=2omega, for the displayed global
  nowhere-zero forms. q is finite etale degree2, j identifies S with
  T minus {Z=0,t=-1}; this is NOT the A2 chart's deleted {x=0,t=-1}.
- If (H,G) is any regular scalar pair on T, (H composed E,G composed E/2)
  is an invariant pair with the same scalar and EXACT SAME Laurent support
  in each coordinate for weights(1,0,-2). Negative weight m with
  k=ceil(-m/2) uses p_m=(t^2-1)^k a and coefficient
  2^m4^k t^(m+2k)(t^2-1)^k a(2t^2-1), polynomial and nonzero.
  Thus nonemptiness on unrestricted T, invariant T and S is equivalent,
  even at prescribed supports (S weights are induced by q).
- This is a known-map attachment, not a novelty claim. The review checks
  averaging/pole/error controls and the implication that an actual pair
  gives a JC2 counterexample on the A2 chart. It establishes neither
  existence nor nonexistence of such a pair.
  No ordinary-degree bound, function-space equality, target-orbit equivalence,
  all-T exclusion or converse reduction of arbitrary JC2 is asserted.
  The separate Newton-ratio report was NOT charged to this review; no
  promotion of it follows. The standalone support theorem needs none of it.
  Merge existence interfaces; no duplicate invariant/unrestricted search,
  scientific descendant, AWS allocation or automatic re-review.

### TRACE-IC-1. Field-trace image of any plane Keller map — PROVED-HERE / PROMOTED WITH NAMED STANDARD INPUT, 2026-09-11

- [ROOT proof](xmodel/keller-trace-image-root-20260911.md), SHA256
  76fa7291c32150f8728b704116fdc92171ad40bf4c468bddfb1f01e0bf55c025;
  expected manifest1b830d99313873580424ba0c0988c4271c35c5652574b01dd34460c42dc0981a
  VERIFIED. [FIRST Fable](xmodel/keller-trace-image-gate-fable5-20260911.md)
  CONFIRMED A--E, SHA256
  518c507c88330add26c507a50dbe74f22b7ebfa5de06ee3153e82b4fea04e385;
  receipt350d4f6228cbdf95680f56bc2f35c91a4feb0249d1a22f58da23ffafc369521e.
  Terminal/process absence preceded receipt-FIRST, current pins and WHOLE
  review. [Full intake and timestamp qualification](box/keller-trace-image-gate-fable5-20260911/INTAKE.md).
- Let F=(P,Q) be any actual complex plane Keller map, A=C[P,Q]=C[p,q],
  R=C[x,y], K=Frac A, L=Frac R, and D=(d=0) its ACTUAL reduced
  nonproperness divisor, d=product_i d_i. Set W=D_A,
  H=A[1/d]/A, and L_i the unique simple IC W-submodule of
  A[1/d_i]/A inside H. With pi:A[1/d]->H and L_D=direct_sum_i L_i,

      M=Tr_(L/K)(R)=pi^-1(L_D)
        =A+sum_i (W·((partial_p d_i)/d_i)+W·((partial_q d_i)/d_i)).

  If D is empty use d=1 and M=A. The displayed sum is ADDITIVE, not an
  algebra or fractional ideal; there is no bound on polynomial/geometric
  degree, support, dicritical count, or ramification/defect assumed here.
- Standard primary input: Yekutieli, arXiv:alg-geom/9602011v2, Section7
  pp27--33 including proofs, integral-curve exact quotient
  0->L_i->A[1/d_i]/A->sum_z delta_z^(r_i,z-1)->0.
  ROOT extends it to reducible D by local-cohomology Mayer--Vietoris and
  elementary point-module Ext: H/L_D=sum_z delta_z^(r_z-1).
  r_z counts analytic branches; intersection multiplicity is not counted.
  The general df/f formula's outside-Section7 citation is replaced by
  Fable's direct Theorem7.1 residue proof: coefficients of df/f have
  regular differential residues on the normalization, hence all branch
  residues zero, and their nonzero classes generate the simple L_i.
- Core Keller attachment: polynomial lifted partial_p,partial_q commute
  with trace and give H2(M)=M/(partial_p M+partial_q M)=0 by polynomial
  integration on A2. At every generic point eta_i of actual D, the finite
  normalization trace-dual lattice shows M_eta_i=K: bounded trace poles
  would force R_eta_i finite. The image of M in H/L_D is then zero by
  RIGHT exactness of top de Rham cohomology and H2(delta_z)=C. Simplicity
  and generic fullness give the reverse containment L_D<=M/A.
  No lower-cohomology surjectivity, holonomicity of R, normalization-A1
  hypothesis, or total-Betti comparison is used.
- At ANY ordinary node with S=widehat(A_z)=C[[u,v]], d a unit times uv,
  ordinary flat tensor base change gives

      S tensor_A M=S[1/u]+S[1/v],
      S tensor_A(A[1/d]/M)=H2_(u,v)(S).

  This is not adic completion of the nonfinite source. The point quotient
  has D-module length1, not finite O-length or C-dimension. Mixed negative
  Laurent coefficients vanish for each trace. Elementary coefficient
  restatement: n/(u^a v^b) lies in this sum iff n in (u^a,v^b)S,
  a,b>=1; clear denominators or inspect the finite mixed rectangle.
  No actual source trace failing the test or finite moment cutoff is known.
- Negative controls retain the exact limits: a torus open immersion has
  full mixed localization but H2(source)=C; A1 times Gm satisfies the trace
  formula without being an A2 source; (x,xy) fails derivation stability;
  an artificial divisor for the identity fails generic fullness.
  Therefore no properness, source characterization, degree bound, actual
  counterexample or JC2 resolution follows. No novelty claim is made.
  The separate Astra node-cover and global-dimension reports were not
  charged and are not promoted by this review. Historical branch-cluster
  disjointness is a deduplication hit, not a newly funded theorem.

### TRACE-CUTOFF-1. No rank-only cutoff for node-module power traces — EXACT / PROMOTED, 2026-09-11

- [Astra powers](xmodel/keller-trace-powers-astra-20260911.md),
  SHAbf94cc3ebf702f85a6971b80560ac3076d84e8873b74778c645333cf173503f0;
  [FIRST Fable A--B](xmodel/keller-trace-shortcuts-gate-fable5-20260911.md),
  SHA78c8a8fbf6f0136f90bd99a75b62f3407f5cc91c6cf970d34d86a47e4008ffdb.
  Native expected transaction verification and terminal/custody-FIRST/WHOLE
  intake completed. [Fable intake](box/keller-trace-shortcuts-gate-fable5-20260911/INTAKE.md)
  records terminal authority, receipt, all current pins and exact scope.
- S=C[[u,v]], K=Frac(S), B=S[1/u]+S[1/v]. For h_m=1/u+u^m/v, m>=0,
  h_m^k lies in B for0<=k<=m+1, while the first failure k=m+2 has mixed
  coefficient (m+2)/(uv). Both divisorial pole orders are1, independently
  of m. Rank1 trace is the identity; K^N with h=(h_m,0,...,0) gives the
  same failure in every rankN. Thus rank and these pole orders do NOT bound
  the necessary number of B-membership tests. The growing quantity is
  tangential numerator contact. Connected Kummer controls also give delay,
  but normalized pole orders there scale with the extension degree.
- All powers of h=v/u+u/v lie in B, although the connected genuine etale
  open T=S[1/(uv)] has full trace image T containing1/(uv). One element's
  all-power test does not test an entire source algebra. One-branch Kummer
  covers trace onto S[1/u]; t^e=uv with t inverted first exposes the mixed
  trace at power e. These are exact local controls, NOT Keller A2 sources.
- Actual-source corollary uses TRACE-IC-1: if T=R tensor_A S contains a
  component idempotent eps with uv invertible on its nonzero component,
  eps/(uv) has trace n_i/(uv), n_i>0, contradicting Tr(T)=B. Ordinary flat
  tensor elements are finite S-linear sums of source elements, so no global
  polynomial idempotent is required. Generic splitting of the field algebra
  does NOT establish membership of eps/(uv) in T.
- Preserve the TRUE ring criterion: firstN power traces in a Q-algebra A
  imply characteristic coefficients in A by Newton, hence integrality and
  all later traces in A. For actual Keller x,y this is the August24
  TRACE-REGULARITY properness criterion, not a newly refuted or new result.
  B is not an algebra; the recurrence cannot be used there. No finite
  cutoff for actual-source regularity, actual forbidden trace, degree bound,
  source realization or JC2 conclusion is asserted. Stop rank-only B scans,
  not every finite-trace or source-attached approach.

### TRACE-SPLIT-1. Actual trace-section obstruction and conditional kernel cohomology — PROMOTED AT STATED TIERS, 2026-09-11

- [Astra kernel](xmodel/keller-trace-kernel-astra-20260911.md),
  SHA7d943729d2ff5b101e38e015df006ab596651e3fea3d4915bdf01d9b45b6b2bd;
  [same FIRST Fable C--E](xmodel/keller-trace-shortcuts-gate-fable5-20260911.md)
  and intake above. Parent TRACE-IC-1, actual complex Keller R/A, M=Tr(R),
  K=Frac(A), E=ker(Tr), actual reduced nonproperness divisor D.
- PROVED-HERE: R intersect K=A. Any irreducible denominator ell in A
  pulls back to a nonconstant polynomial, hence has a source divisor;
  quasifiniteness forces this divisor to dominate ell=0, so a relatively
  prime numerator cannot cancel its valuation. No novelty claim.
- PROVED-HERE: if D is nonempty, Hom_A(M,R)=0. A map generically multiplies
  K by fixed r in L. At a retained source divisor over generic ell in D,
  M_eta=K supplies ell^-n for all n, while R_eta has nonnegative source
  valuation. Therefore r=0. If D is empty M=A and m/N is a trace section.
  Thus an A-linear (or W-linear) section of Tr is equivalent to properness;
  assuming a section does not close the conjecture independently.
- CONDITIONAL on the explicitly named IC/normalization de Rham comparison:
  H0(M)=C, H1(M)=C^c, H0(E)=H1(E)=0, H2(E)=H1(M)=C^c, where c counts
  irreducible components of D. H1(M)'s count needs connected normalizations,
  not an extra A1 restriction. The classes dd_i/d_i form its residue basis.
  The trace of a polynomial primitive represents exactly the obstruction
  to correcting that primitive into E. No proof that H2(E)=0 follows.
- Exact etale-open control: 0->A->A[1/p]->H_p->0 does not split, since
  H_p is p-power torsion and A[1/p] is p-torsion-free. CONDITIONAL on the
  stipulated holonomic simplicity/duality inputs, its dual has H_p as a
  submodule, so the localization is not globally self-dual despite its
  perfect rational trace pairing. This is a nonproper-open control, not an
  A2 source or a refutation of future trace/kernel methods.
- No primary literature was charged to this FIRST: comparison and duality
  remain stipulated, not newly externally verified. No source-derived mixed
  trace, source characterization, properness proof or JC2 result. ROOT's
  iteration report was not charged and remains MANUAL/UNREVIEWED.

### BASS-SHEAR-1. Growing-shear algebraic-formal kernel exclusion — PROVED-HERE / PROMOTED, 2026-09-11

- [Astra producer](xmodel/bass-resonant-operators-astra-20260911.md),
  SHAc179106b8dabb3eeb20a0757e75faf952d0d6f42511fc90f2450126b11ef58b7;
  [FIRST Fable](xmodel/bass-resonant-operators-gate-fable5-20260911.md),
  SHA8b5617ba9a3f4b8f28e96468cee647d9cd121a9ce42e69b3139c64a074e5950c.
  [Intake](box/bass-resonant-operators-gate-fable5-20260911/INTAKE.md)
  records terminal-first custody, current pins, WHOLE review and qualifications.
- Let ep=p partial_p, eq=q partial_q, e=ep+eq, delta=p partial_q.
  For coprime integers a,b>0, c in Z and nonconstant g in C[T],

      (a ep-b eq-c+delta g(e))f=0, f algebraic in C[[p,q]],
      implies f in C[p,q].

  Separately, for every integer r>=0, the same conclusion holds for
  ep-r+delta g(e), including r=0 and g(r)=0. No degree bound or coefficient
  arithmetic hypothesis. The proof uses exact homogeneous shears and a
  nonzero bounded-below weighted initial relation to show the coefficient
  series algebraic; convergence of f(p,0) and growing shear force it entire,
  hence polynomial. Univariate algebraic convergence is standard external
  background; the entire-algebraic step follows by root bounds and Cauchy.
- Inhomogeneous corollary: Phi(f) polynomial implies f polynomial by
  subtracting finitely many homogeneous terms. Thus these exact operators
  are injective on R/C[p,q] for an actual plane Keller source embedded by
  the formal inverse over the target origin. Coordinates must be NORMALIZED
  with a source point above (0,0); translating arbitrary fixed coordinates
  changes the Euler operators. Formal inverse existence and finite
  function-field extension are stated standard inputs, not new theorems.
- Constant-g controls are nonpolynomial rational germs:
  p^r u^s/(1-p^b u^a), u=q-gamma p/(a+b), ar-bs=c, and at the endpoint
  p^r/(1-q+gamma p). They show the nonconstant condition is essential for
  ALL algebraic germs, not for actual-source polynomiality. No actual
  Keller source is realized by these controls.
- History boundary: van den Essen1993 Theorem4.1 already covers the
  positive-a,b ACTUAL-KELLER consequence after generic nice normalization,
  for arbitrary higher delta terms. Its condition Phi_0(r,eq)!=0 for all
  r>=0 fails for the new coordinate endpoint ep-r. The original Bass1.5
  likewise does not apply to special-linear diagonals. The larger
  arbitrary-algebraic-germ category is distinct; no novelty claim is made.
  Selected Bass pages41--42/49 and the whole van den Essen article were
  charged; external normalization/flatness/Bertini ingredients are declared.
- No theorem puts an arbitrary U-annihilator into either displayed family.
  Therefore no general U-torsion-freeness, properness, degree bound, JC2
  proof or counterexample follows. ROOT's separate affine-angular candidate
  has its own FIRST gate; its promotion is not implied by this entry.

### BASS-AFFINE-1. Complete affine-angular kernel classification — PROMOTED AT STATED TIERS, 2026-09-11

- [ROOT producer](xmodel/bass-affine-angular-root-20260911.md),
  SHAa6a6f06b201aeeed7e621b5a4a992443511592dc81af545ffd7f265791235ed5;
  [FIRST Fable](xmodel/bass-affine-angular-gate-fable5-20260911.md),
  SHA88a3d52ec379fb23e9b7600eda743cb5db2dcafad0043ea462ce1b5e5202b8b0;
  [intake](box/bass-affine-angular-gate-fable5-20260911/INTAKE.md).
  Expected transaction VERIFIED before review; terminal-first receipt,
  current pins and WHOLE review completed. Native report is provenance,
  not an imported unproved premise: needed leading-order facts are re-derived.
- PROVED-HERE: for r>=0 integer and arbitrary complex constants alpha,
  beta,gamma, put Phi=ep-r+delta(alpha ep+beta eq+gamma), delta on LEFT,
  K=alpha r+gamma. Its formal kernel is exactly

      f=p^r sum_(n>=0)c_n sum_(j=0)^n V(n,j)p^j q^(n-j),
      V(n,j)=(-1)^j binom(n,j) product_(k=0)^(j-1)
                  [beta n+K+(alpha-beta)k].

  If f is algebraic, H(q)=sum c_n q^n is algebraic by the nonzero p-initial
  polynomial relation. Every algebraic formal f has a uniform exponential
  coefficient bound; the report proves this via univariate restrictions,
  Baire and Cauchy, using standard univariate algebraic convergence.
- If beta!=0, the first floor(epsilon n) factors have growing modulus for
  fixed sufficiently small epsilon>0, even if later factors vanish. Thus
  H is entire algebraic, hence polynomial, and so is f. If beta=0,
  alpha!=0 and -K/alpha is not a nonnegative integer, the q=0 product
  grows faster than exponentially and gives the same conclusion.
- Exact exceptional families among ALGEBRAIC GERMS: if beta=0,
  alpha!=0 and K=-alpha J, J>=0 integer, all kernels are

      f=p^r sum_(j=0)^J binom(J,j)(alpha p)^j H^(j)(q).

  If alpha=beta=0, all kernels are p^r H(q-gamma p). In either case
  f is algebraic iff H is algebraic. H(t)=1/(1-t) gives a nonpolynomial
  rational control. These refute uniform all-germ polynomiality, not JC2.
- CONDITIONAL on Bass1989 Theorem1.4 and its linear-coordinate applicability:
  EVERY displayed Phi is injective on R/C[p,q] for an actual polynomial-plane
  Keller source in normalized target coordinates with a source point over0.
  Finite homogeneous-tail subtraction handles Phi(f) polynomial. Growing
  cases follow above; the first exceptional family has p-degree<=r+J and
  is killed by product_(i=0)^(r+J)(ep-i), so Bass applies. The second is a
  linear target shear of ep-r, again covered by Bass. The theorem statement
  was primary-read; its full proof/source setup remains externally trusted.
- No general annihilator can yet be placed into this delta-degree1,
  linear-diagonal, affine-coefficient form. No degree bound, actual
  counterexample, properness theorem, novelty claim or JC2 resolution.
  No automatic descendant or duplicate affine review. The independently
  assigned general-G test is not a consequence promoted by this entry.

### BASS-DELTA1-1. Arbitrary polynomial first-delta coefficient — PROMOTED AT STATED TIERS, 2026-09-11

- [Astra producer](xmodel/bass-general-delta1-astra-20260911.md),
  SHA f4d2eedb3254659deb36d4437e1f632825af9ef68ba1caf38c81d8b10e91f9d7;
  [FIRST Fable](xmodel/bass-general-delta1-gate-fable5-20260911.md),
  SHA f34c4d4a4abbcb92229fe750ed65bc890725723f4760877aee2a1fdce5dc52c3;
  [terminal-first intake](box/bass-general-delta1-gate-fable5-20260911/INTAKE.md).
  ROOT's separately pinned proof lead is attributed; the reviewer re-derived
  the proof independently. No earlier unreviewed report is a hidden premise.
- Let ep=p partial_p, eq=q partial_q, delta=p partial_q. For r>=0 integer,
  G in C[X,Y], put Phi=ep-r+delta G(ep,eq), delta on the LEFT.
  If G is nonconstant and has no factor X-(r+J) for any integer J>=0,
  every algebraic f in C[[p,q]] satisfying Phi f=0 lies in C[p,q].
  Evidence: manual proof modulo explicitly stated standard convergence,
  convergent Newton--Puiseux at infinity, density-zero Fabry, and elementary
  algebraic-function singularity/entirety facts. These analytic premises
  remain externally trusted; selected Bass pages corroborate the Fabry form.
- The exact degree-r+n kernel has coefficients

      c_n V(n,j), V(n,j)=(-1)^j binom(n,j)
                          product_(k=0)^(j-1) G(r+k,n-k).

  Its leading p-coefficient H(q)=sum c_n q^n is algebraic. A moving linear
  j-window has superexponential product growth outside O(X^sigma) bad
  degrees, sigma<1: Puiseux branches give polynomial lower bounds away
  from sparse near-integer sublinear roots. Early small-factor losses are
  O(n^sigma log n), below the positive c*n*log n growth. Thus H splits
  into an entire series and a density-zero supported series. Fabry and
  algebraicity force H, and then f, polynomial. Arbitrary complex G is
  covered; no integer-coefficient or Diophantine estimate is assumed.
- CONDITIONAL on Bass1989 Theorem1.4, EVERY G gives an injective operator
  on R/C[p,q] for an actual plane Keller R=C[x,y], normalized with a source
  point above target0. Accessible vertical factors bound p-degree and
  provide a nonzero diagonal annihilator; constant G is a linear target
  shear of ep-r. Finite-prefix subtraction handles Phi(f) polynomial.
  In these two cases nonpolynomial algebraic germs exist, so actual-source
  applicability of Bass is indispensable. Full Bass proof remains external.
- Exact controls: G=Y-(X-r)^2 has quadratic sparse truncation degrees;
  G=(Y-1)(X-r+1) has cofinite q=0 zeros, requiring a moving window.
  The intake corrects a non-load-bearing sign in the review's vertical
  example. No uniform nonzero window without exceptions is asserted.
- Composition subsumes affine and coordinate-endpoint cases, NOT arbitrary
  U-annihilators. U-torsion and the common diagonal factor do not yet give
  this normal form. No general U-torsion-freeness, properness, novelty,
  actual counterexample, degree bound or JC2 resolution follows.

### BASS-SELECTION-1. Mellin attachment and selection obstructions — PROMOTED AT STATED TIERS, 2026-09-11

- [Astra Mellin producer](xmodel/keller-mellin-rank-astra-20260911.md),
  SHA180c9a64c98d8cf89e791fabd9f4d1ac690c33128235b073875a25475651e8e1;
  [ROOT nonmonic control](xmodel/bass-nonmonic-control-root-20260911.md),
  SHA80a1ce08a20b880516779d6722bfd0133a437f0e3922f5806c92efe772fef312;
  [ROOT rank1 control](xmodel/bass-rankone-selection-root-20260911.md),
  SHA79a4cdc51503d81365df572d56b0b7e1c5c1ccf8d9e81edbc7343d28d2621582.
  [Independent FIRST Fable](xmodel/bass-mellin-selection-gate-fable5-20260911.md),
  SHA9ce11f9c70ff6f1e699571b600d972ce666a2bcc4dc8278ed81da058fd368417;
  [terminal-first intake](box/bass-mellin-selection-gate-fable5-20260911/INTAKE.md).
- CONDITIONAL: actual affine etale F=(p,q):A2->A2 has holonomic direct
  image R=C[x,y] in degree0, without properness. For A=C[p,q], N=R/A,
  B=C[ep,eq], E=FracB, corrected Loeser--Sabbah Mellin rank and de Rham
  comparison give rank_B N=1-chi(p=0)-chi(q=0)+#F^-1(0).
  Holonomic direct image, corrected LS Thm2(1), algebraic de Rham comparison
  and Euler additivity remain named external premises. Torus localization,
  E tensor A=0 and sign(+1) in dimension2 are checked. Translations change
  Euler operators as well as fibers. No rank0 conclusion is supplied.
- PROVED-HERE: B=C[t,z], sigma(z)=z-1, sigma(t)=t, with
  delta v1=v2, delta v2=zv1 gives a B-free, U-torsion, rank2 module with
  bijective localized delta and NO stable E-line for any vector. The
  required a*sigma(a)=z contradicts parity of rational z-degree.
  Thus those module properties alone do not imply first-order selection.
- PROVED-HERE: sqrt(1-q(p+q)) is an algebraic nonpolynomial germ killed by
  2ep(eq+1)+delta(ep-eq); left normalization yields rational coefficient
  (ep-eq)/(2eq), not polynomial G. If the square relation held for an
  actual f in Keller R, derivatives give p,q in fR and then1 in f^2R,
  contradicting units of R and independence of p,q. This is one control.
- PROVED-HERE: the rank1 module E v with delta v=a v,
  a=z(z-t-1)/(z-t/2-1), rejects z-r+delta G(z,t-z) for EVERY nonzero
  vector b v, b in E, every integer r>=0 and every polynomial G.
  Infinity forces G=-1 and the resulting rational shift quotient has
  nonzero total divisor multiplicity on the orbit of t/2+1. Hence even
  rank1 and arbitrary rational gauge do not supply the required normal form.
  Neither abstract module is claimed to be full Weyl, holonomic or Keller.
- PROVED-HERE: finite homogeneous-prefix subtraction lifts every
  quotient U-relation to an exact relation on a representative in normalized
  actual R, because all U operators preserve total degree. This supersedes
  the Mellin producer's separate lifting OPEN, not its source-selection gap.
- BASS-DELTA1-1 composes only after source-specific first-order selection
  AND polynomial-G/resonant normalization, both still UNPROVED. The Mellin
  formula supplies neither. No arbitrary-annihilator theorem, actual source
  counterexample, degree bound, novelty or JC2 resolution is claimed.
  The optional BBKP AppendixB criticism is not reviewed or promoted here.
