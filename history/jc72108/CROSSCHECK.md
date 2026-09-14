# CROSSCHECK — Helali (Zenodo 21479814) & Suzuki (Zenodo 21483636) vs our Generator A

Started 2026-08-04. Task: download both artifacts, diff their Prop 4.3 transcriptions
against ours (cases/emit.py CASES[open_8_28_c1/c2] + FIX, README Semantics), replay
Helali's gmpy2 script, assess Suzuki's structure, produce agreement matrix.

## Our reference transcription (for the diff)
- Prop 4.3, family A0=(8,28), (m,n)=(3,2) -> (deg P, deg Q)=(108,72); reduced bracket
  RHS: [P,Q] = x^2, bracket convention [P,Q] := P_x Q_y - P_y Q_x.
- Subcase 1 (open_8_28_c1): cornersP=[(0,0),(1,0),(8,14),(8,16),(0,8)],
  cornersQ=[(0,0),(2,1),(12,21),(12,24),(0,12)]; 187 vars / 303 eqs.
- Subcase 2 (open_8_28_c2): cornersP=[(0,0),(1,0),(8,14),(8,16)],
  cornersQ=[(0,0),(2,1),(12,21),(12,24)]; 73 vars / 93 eqs.
- Unknowns = all lattice points of hull(N(P)), hull(N(Q)); equations = all coeffs of
  [P,Q]-x^2; saturation t*prod(corner coeffs)=1 (corners attained); "nonorigin" leaves
  (0,0) coeff unconstrained; torus normalization FIX: P(8,16)=1, Q(12,24)=1.
- Status: c2 lane-2 msolve run pending verdict; c1 still computing.

## Download log
- Helali: GitHub bilLkarkariy/jc2-72-108-exact-certificates cloned (HEAD c530fe4, 184 MB);
  Zenodo 21479814 zip = same repo v1.0.1 (not re-downloaded). Replay workspace extracted:
  crosscheck/helali/repo/release_bundle/bundle/exact_replay/ (141 MB incl. 89,105,967-byte
  hard/h_certificate_exact.txt, hashes present). Deps: gmpy2, numpy, python-flint, sympy.
- Suzuki: Zenodo 21483636 v1.1.4 zip (5.1 MB) sha256 VERIFIED (d457fbee...74bd), EN PDF +
  full LaTeX source + verification package at crosscheck/suzuki/package/.

## (2) Transcription comparison — Prop 4.3

### Polygons and RHS: EXACT AGREEMENT, all three parties
Helali paper (sec 3) and Suzuki paper (sec 1, + source_proposition_4_3_case_8_28.txt quote):
- Case/subcase 1 ("larger"): N(P)=conv{(0,0),(1,0),(8,14),(8,16),(0,8)},
  N(Q)=conv{(0,0),(2,1),(12,21),(12,24),(0,12)} — identical to our open_8_28_c1 corners.
- Case/subcase 2 ("smaller"): drop (0,8),(0,12) — identical to our open_8_28_c2 corners.
- RHS [P,Q]=x^2, both. Suzuki states bracket [P,Q]=P_x Q_y - P_y Q_x explicitly = OURS.
  Helali works in Laurent coords t=xy^2, z=y^{-1} with [t,z]_{x,y}=-1, x^2=t^2z^4; I checked
  the induced band equations (J4: 2AD'-3A'D=t^2) are the P_xQ_y-P_yQ_x convention. AGREE.
- Numbering agrees: subcase 1 = 5-vertex/larger (has (0,8),(0,12)), subcase 2 = 4-vertex.
  (Suzuki's paper labels them "smaller"(=2)/"larger"(=1) but quotes GGV order identically.)

### Support/unknowns semantics: AGREEMENT
- Suzuki: Supp(F) within N(F)=conv(listed vertices), "every listed vertex coefficient is
  nonzero" — same reading as our corners-attained saturation. Lattice counts: smaller
  25 (P) + 47 (Q) = 72 = our c2's 73 vars minus the saturation var t; larger (after
  u=ts, s^8/s^12 shifts) 61+125 = 186 = our c1's 187 minus t. EXACT var-level match.
- Suzuki notes all lattice points have nonneg coords, so L^(1) Laurent setting reduces to
  ordinary k[x,y] — consistent with our polynomial-ring transcription.
- Helali: same band decomposition P=Az^2+Bz+C (A: t..t^8, B: t..t^8, C: 1..t^8),
  Q=Dz^3+Ez^2+Fz+G (D: t^2..t^12) = same lattice supports; case 1 adds negative z-bands
  z^{-1}..z^{-8} (P), z^{-1}..z^{-12} (Q) — the (0,8)/(0,12) fans. Same supports.
- I verified Suzuki's "larger" transformed bracket 8PQ_u-12P_uQ+s(P_uQ_s-P_sQ_u)=-u^2s^22
  and per-monomial factor j(8-k)+i(l-12) by hand from our convention: correct.

### Normalization: MODELING DIVERGENCES, all legitimate (gauge choices)
- Ours: FIX P(8,16)=1, Q(12,24)=1 (finite root-of-unity ambiguity, harmless for emptiness).
- Helali: A=t+a_2t^2+...+t^8 (P coeffs at (1,0) and (8,14) both =1; leaves 35th-root
  ambiguity — likely source of his degree-35 H(a_7): 5 dessin classes x 7 gauge).
- Suzuki: top-edge p_8=(s+1)^2, q_12=(s+1)^3 via A^17=1/(a^5cd); plus "additive
  normalization" Lemma: sets constant terms to 0 AND drops the (0,0) vertex-presence
  requirement — a RELAXATION (conservative: excludes a superset). Note our "nonorigin"
  mode is the same conservative spirit (leave (0,0) unconstrained); Suzuki additionally
  translates constants away, legitimate since [P,Q] is translation-invariant.
- No outright transcription error found on either side. All discrepancies are gauge/
  coordinate choices, each checked convertible to ours.

### Both cover subcase 1 (our c1, still computing on our side) — HIGH VALUE
- Helali case 1: 13 compatibility equations from negative z-bands; exhaustive split
  s=c / s=-c (c a nonzero vertex coefficient); relation E_6-lambda*E_2=S*Lambda^2 (S!=0)
  forces affine-linear Lambda=0; h=0 excluded by pre-division unit certificates per
  branch; s=c branch: hard identity h=Sum T_iE_i over L=Q[w]/(w^5-w^4+3w^3+3w^2+26) in
  L[h,u_1,u_2] (89 MB certificate); involution (h,u_1,u_2)->(h,-u_1,-u_2) transports to
  s=-c. Verdict: case 1 EMPTY.
- Suzuki larger: weighted descent in (u,s), 9 params -> 6 active (x_0,x_1,x_3,x_6,x_7,x_8;
  weights 1,1,2,3,3,4) after x_2,x_5 (additive consts) := 0 and x_4=rho*x_1^2 forced by a
  perfect-square obstruction; 15 positive-weight constraints (weights 5..8); Macaulay to
  weight 12: 351x261, labelled 261x261 minor det=21 mod 23 => exact minor nonsingular =>
  radical of obstruction ideal = (x_0,...,x_8-vars) => only common zero is the origin =>
  all below-top-edge coefficients vanish there, killing required vertices (0,8),(0,12).
  Verdict: larger (=subcase 1) EMPTY.
- Independent field convergence: both reduce the common top edge to a DEGREE-5 number
  field (Helali: w^5-w^4+3w^3+3w^2+26; Suzuki: explicit big-coefficient quintic M(X),
  Rabin-certified irreducible mod 67), matching Suzuki's "exactly 5 dessin classes"
  count (passport (3^7),(2^10 1),(17,1^4)). SAME-FIELD CHECK DONE: discriminant square
  classes match (both = 3*13*17 mod squares) and factorization shapes agree at 300/300
  good primes -> the two quintics generate the same field with overwhelming probability
  (P < (4/5)^300 if not). Two independent stacks converged on one number field.
  Helali's first-block field K is degree 35 = 5x7; his build_degree5.py asserts every
  residual coefficient lies in the subfield Q(u^7) (deg 5) — the extra 7 is his gauge
  (a_1=a_8=1 leaves 35th-root ambiguity), consistent with 5 dessin classes x 7.

## (3) Helali replay — RESULT: FULL PASS, 71 seconds wall
Env: macOS arm64, Python 3.14.6 venv (gmpy2 2.3.1, numpy 2.5.1, python-flint 0.9.0,
sympy 1.14.0). Command: PYTHON=<venv> ./verify_all.sh. Log: /tmp/helali_replay.log.
- All sha256 manifests OK; all stages green; final marker JC2_72_108_EXACT_REPLAY_PASS,
  exit 0. gmpy2 verifier: 13,410 coefficient-field products / 335,250 scalar products,
  exactly as the paper claims; run twice (branch 1 + branch 2 via symmetry transport).
- What is verified per subcase/chart:
  - Case 2 (c2): CASE2_SERIALIZED_EXACT_PASS — certificate generators are checked EQUAL
    to a from-scratch regeneration (case2_exact_generate.py, 25 residual eqs, 4 used),
    then 1 = Sum T_i R_i replayed over the degree-35 field. Unit ideal => empty.
  - Case 1 (c1): both branches. h=0 chart: unit certificates verified against the
    regenerated after_w systems specialized at h=0 (both branches PASS). h!=0 chart:
    hard identity h = Sum T_i E_i over L verified by independent gmpy2 evaluation
    against the regenerated hne0_polred system; branch 2 obtained by a VERIFIED
    polynomial involution (SYSTEM_SYMMETRY_PASS), identity replayed again. Together:
    every solution has h=0 and h!=0 — contradiction — both branches empty.
- Replay wall time 71 s (log birth->mtime), matching the claimed ~70 s.

### My independent audit of Helali's unverified steps (audit_gaps.py — all closed)
The stock replay does NOT itself assert two load-bearing identities; I verified both
with my own driver over their flint field (crosscheck/helali/audit_gaps.py):
1. Split exhaustiveness: all_comp[0] is UNIVARIATE in s (degrees {0,2,4}) and equals
   kappa*(s-c)^2*(s+c)^2 EXACTLY, kappa != 0, c != 0, branch values = +-c. So s=+-c
   is exhaustive: CONFIRMED. (Second compat eq vanishes on both branches: confirmed.)
2. Forced-r step: elim = E6 - lambda*E2 with lambda = +13/9 / -13/9 (exactly as the
   report claims) satisfies elim == S*Lambda^2 EXACTLY with S != 0 on both branches;
   Lambda is monic-linear in r, so eliminating r is lossless: CONFIRMED.
3. Checkpoint provenance: default replay only hash-checks case1_checkpoint.pkl (the 13
   compatibility equations). I deleted it and re-ran case1_descent_checkpoint.py from
   the polygon band data: regenerated pkl and case1_residuals_exact.txt are
   BYTE-FOR-BYTE IDENTICAL (sha256 2dcf13d9... / f026228c...). Layer structure: bands
   k=1,0,-1,-2,-3 give 0+2+2+4+5 = 13 compat eqs in 6 params (r,s,h,u1,u2,u3), matrix
   pivots are parameter-free K-scalars (sound linear algebra over a field).
4. Dropped-equation discipline: cascade keeps a SUBSET of substituted equations
   (inds 2,4,5,8,9,10,11) — conservative for emptiness. The h-shift is asserted
   invertible (bh != 0). The u3-elimination divides by h — valid exactly because the
   h=0 chart is certified separately. Architecture sound.
- Minor cosmetic weakness: verify_case1_reduction.py prints
  "generic_band_formula_verified_symbolically_by_chain_rule True" as a constant string
  (the real symbolic band check is only done for the case-2 bands in
  verify_laurent_reduction.py). Not load-bearing: the band formula is the chain rule.
- Remaining trust boundary (Helali, explicit and correctly disclosed): faithfulness/
  exhaustiveness of GGV Prop 4.3 itself, and the on-paper normalization argument
  (a_1=a_8=c_8=1 via rho,sigma,lambda,mu with rho*sigma*lambda^3*mu=1; constants
  subtractable). I checked the gauge arithmetic on paper: legitimate.

## (4) Suzuki assessment
- Static verification (stdlib-only): ALL PASS in 0.6 s (manifest, Rabin quintic
  irreducibility, small Bezout U*H0+V*H1=1 over K(alpha)[lambda], 261x261 labelled
  Macaulay minor det=21 mod 23, both negative controls detected, manifest re-check).
- FULL canonical regeneration (SymPy 1.14): ALL PASS in 21.5 s on this machine —
  every proof object regenerated in a temp build and compared BYTE-IDENTICAL to the
  distribution (incl. exact char-0 small layers, exact large D=23..18 descent, mod-23
  lower descent with recorded pivot residues, all independent audits).
- Structure: exhaustiveness of the 5-dessin split is machine-enumerated (Prufer trees
  with degree sequence (3,3,2,1,1,1,1) -> 2 shapes x 128 rotation systems ->
  canonicalized classes; two independent implementations agree). The omitted chart
  c_6=0 is excluded by a clean rigidity argument (z -> rz fixes the classification).
  The 5 conjugate representatives fill all 5 classes (primitivity of a_5=alpha).
- The smaller-polygon kill uses only necessary conditions (bracket layers s^4..s^1)
  and a Bezout identity uniform in the embedding — sound (subset of constraints).
- The larger-polygon kill: 15 positive-weight constraints => Macaulay minor nonsingular
  (certified mod 23, lifts because formation commutes with the specialization map)
  => radical = parameter maximal ideal => only solution is the weighted origin, where
  the required vertices (0,8),(0,12) get coefficient 0 => not in the larger stratum.
  I re-derived their transformed bracket 8PQ_u-12P_uQ+s(P_uQ_s-P_sQ_u)=-u^2 s^22 and
  the per-monomial factor j(8-k)+i(l-12) by hand from our conventions: both correct.
- Visible gaps / trust boundary (honestly disclosed in their sec. 7 table):
  (a) The D=17..0 lower descent is executed only over F_23; characteristic-zero
      validity rests on their Lifting Lemma (recorded nonzero pivot residues) — the
      argument is written out and looks correct, but the exact lower descent itself is
      never run over K. This is the one place where a skeptic must read a proof, not
      a certificate. (Conservative direction: only used to certify a SUBSET of exact
      constraints — the minor lift — so the risk is a false NON-exclusion, not a false
      exclusion... actually the risk direction is benign: det != 0 mod 23 => det != 0
      exactly; the subtle part is that the 15 finite constraints ARE reductions of
      exact consequences, which is what the pivot-lifting lemma establishes.)
  (b) The dessin/passport bridge (Riemann existence, Belyi passport derivation) is
      classical math taken as trusted input, not machine-checked.
  (c) The claim "second obstruction is redundant" after x_4 = rho*x_1^2 and c != 0 in
      the square obstruction are inside the audited exact D=18 data.
  No error found. The negative controls (mutated H0 coefficient; duplicated minor row)
  genuinely flip the verdict — sensitivity confirmed in both paths.

## (5) Bottom line and agreement matrix

| Subcase (GGV Prop 4.3) | Helali | Suzuki | Ours |
|---|---|---|---|
| (1) larger, 5-vertex, = open_8_28_c1 | EMPTY (replayed here, 71 s, + my gap audit) | EMPTY (replayed here, 21.5 s full regen) | still computing |
| (2) smaller, 4-vertex, = open_8_28_c2 | EMPTY (unit ideal, replayed) | EMPTY (Bezout, replayed) | msolve pending; line-probe codim>=2 consistent |
| (72,108) overall | excluded (conditional on Prop 4.3) | excluded (conditional on Prop 4.3) | pending |

- Three-way transcription agreement is EXACT at the level that matters: identical
  corner sets, identical lattice supports (25+47 and 61+125 points), identical bracket
  convention and RHS x^2, identical subcase numbering. All differences are gauge
  normalizations, each verified legitimate. This materially strengthens the
  exhaustiveness/faithfulness argument for OUR Generator A transcription too.
- BOTH artifacts certify subcase (1) — the one still computing on our side. Extracts
  for diffing against our c1 core are staged in crosscheck/c1_extracts/ (branch
  after_w systems + meta) plus, in the bundle: case1_residuals_exact.txt (the 13
  compatibility equations over K in (r,s,h,u1,u2,u3), regenerated byte-identical) and
  hne0_polred.pkl (4 generators over L in (h,u1,u2) feeding the 89 MB certificate).
  Suzuki's subcase-1 objects: large_D18_exact.json / large_mod23_certificate.json.
- Single most important discrepancy/gap found: NONE on polygons/bracket/supports.
  The most significant finding is a VERIFICATION-COVERAGE gap in Helali's stock
  replay: it never asserts the two identities that make his case-1 chain lossless
  (the s^2=c^2 factorization and elim=S*Lambda^2), and it trusts the 13-equation
  checkpoint by hash only. All three items now independently closed by me (sec. 3).
  For Suzuki the analogous item is the F_23-only lower descent covered by an on-paper
  lifting lemma. Neither is an error; both are places an auditor must look.
- Implication for our campaign: if our lane-2 runs return NONEMPTY for either subcase,
  the conflict is now three-way and almost certainly in OUR cascade/saturation, not in
  their transcriptions. Their two independent subcase-1 exclusions (same degree-5
  field, different methods) make a nonempty c1 verdict on our side very unlikely.

