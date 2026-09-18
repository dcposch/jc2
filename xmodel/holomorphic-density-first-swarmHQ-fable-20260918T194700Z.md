# Independent FIRST and corrections: holomorphic derivative-domain density

Reviewer: Fable 5.1 (requested model=fable, effort=max; hosted identity not independently exposed).
Integrator: swarmHQ ROOT (gpt-6-astra).
Date: September 18, 2026 UTC.
Reviewed producer commit: cc870925bc0b057fcc77a352f6909a50a943c25d.
Evidence tier: MANUAL, independent hostile review with named classical imports.
Lifecycle: completed FIRST; promotion is recorded separately in AUDIT.md.

## Reviewed claim and terminal custody

[Producer](holomorphic-domain-density-swarmHQ-root-20260918T192600Z.md),
full SHA256 3611b6fa35d7abf15273973d42b3592101b0279d7542bd25b3b354b24f5e8450.

For each polynomial Keller F:C2->C2, its common lifted holomorphic
first-derivative domain is dense in H_F exactly when F is invertible.
The proof constructs, under hypothetical noninvertibility, a globally
Gaussian-L2 source polynomial separated from the derivative domain by
a continuous Laurent-coefficient functional. No density premise or
noninvertible Keller map is supplied; this is not a proof of JC2.

The reviewer read the three charged immutable snapshots WHOLE; all
pre/post hashes matched. ROOT verified supervisor termination, original
process absence and absence of its service cgroup BEFORE receipt-first
collection, then read the entire terminal review and log. The receipt
records DONE/exit0, CLEAN/BODY_SEALED and all three inputs UNCHANGED.
Terminal output hashes matched the receipt and remained unchanged after
ROOT removed their write bits. No live review/log/receipt was read.

Retained original hashes:

- Review: 5e95f7408dbe3f64e236f8061352f2264eec75c9ea1335c4aace163fe67c07ae
- Receipt: 188384a0b7fbb16eea46d3f31b6a098512dd03a0bf99ba07de2b4ebf5b64ded9
- Log: 3d34684a94b0b0225f1e4cfea630cbe95151487d746da838a54e9f44960bbd1d

Reviewer sections1--5 below are preserved verbatim. Its original section6
contains operational custody and is summarized here, not reproduced;
internal references to section6 refer to that retained original.

## ROOT binding corrections and closure qualification

All seven producer claims survive this independent review. ROOT accepts
the proof with the following correction to REVIEWER commentary:

1. Claim4's aside that a general h*Omega has a pole along E whenever
   v_E(h)<0 is incorrect. Since v_E(Omega)=e-1, the precise condition is
   v_E(h*Omega)<0 iff v_E(h)<1-e. Negative valuations from 1-e to -1
   need not create such a pole. In particular, the constructed witness
   has v_E(h_0)=1-e and a REGULAR form. The producer uses this correct
   threshold; the review's calculation of the witness and the global
   integrability proof are unchanged. Read the attack-log general-polynomial
   warning as saying arbitrary h need not give a form regular on all Z,
   not that every negatively valued h fails.
2. The named classical imports are accepted at their stated scope.
   The reviewer checked applicability, not primary texts, linked historical
   reports or a literature-wide novelty claim. ROOT's selected Stacks
   source checks are documented in the producer. No rational-singularity
   or Grauert--Riemenschneider vanishing assumption is added.
3. The reviewer disclosed repairing malformed custody hashes AFTER first
   appending its completion marker. This violated the instructed
   append-marker-last sequence. Its initial completion timing therefore
   is not treated as authoritative. The disclosed repair is described
   by the author as metadata-only; ROOT did not inspect the earlier live
   version and cannot independently compare that version. The final
   terminal mathematical body, all final pins and receipt hashes were
   independently collected and checked. Terminal receipt completion is
   19:44:44 UTC; the original 19:43 soft target was missed, while the
   independent runtime cap was met. This integration is newly authored
   and finalized only after its own complete readback; the original is
   preserved unchanged. No silent rewrite or retrospective closure claim.
4. No claim of density for arbitrary Keller maps is promoted. The
   conditional nondensity theorem under noninvertibility and the
   automorphism converse together give the equivalence, not its premise.
   The earlier real Sobolev cutoff theorem remains intact.

## Verbatim mathematical review

<!-- REVIEW-MATH-BEGIN -->
## 1. Per-claim verdicts

Convention: one verdict per charged item, with the sub-checks the charge names.
"Import" means a named classical theorem accepted as stated and checked for
applicability only; no fresh primary audit of any import is claimed. All
reconstruction below is my own, from the frozen report text alone.

### Claim 1 (literal setup and the iff): CONFIRMED as scoped

- The real Jacobian determinant of a holomorphic map is |det JF|^2, so
  dvol_g = |c|^2 dV_z and dmu = |c|^2 exp(-|F|^2) dV_z exactly as displayed.
- D_i = sum_j (J^-1)_{ji} d/dz_j satisfies dF(D_i) = d/dw_i because
  sum_j (J^-1)_{ji} J_{kj} = delta_{ki}. Since det J = c is constant,
  J^-1 = adj(J)/c has polynomial entries, so D_i preserves entire functions
  and E_F is a well-defined linear subspace of H_F.
- Density is in the H_F norm. The noninvertible direction is proved by an
  element h_0 in H_F and a norm-continuous functional ell with ell(E_F) = 0,
  ell(h_0) != 0; ker(ell) is a proper closed hyperplane containing the
  closure of E_F, so this is genuine nondensity, not strict inclusion.
- Logic of the scope: "closure(E_F) = H_F implies automorphism" is the
  contrapositive of what is proved; hence density for every Keller map is
  equivalent to JC2. The report asserts no density premise, no counterexample
  and no JC2 solution. Scope statement is accurate.

### Claim 2 (finite normalization, open immersion, E with e > 1, local form): CONFIRMED

- A = C[F_1,F_2] is a polynomial ring (F_1,F_2 algebraically independent since
  det JF != 0). L/Frac(A) is finite, so S = integral closure of A in L is
  finite over A (import: finiteness of normalization, char 0, finite type).
  S is contained in R because R is a UFD, hence normal, and A is inside R.
  Frac(S) = L, so Y = Spec S is a normal affine surface, connected (S is a
  domain).
- F is etale (invertible Jacobian, smooth source and target of equal
  dimension), hence quasi-finite and separated. Algebraic ZMT gives an open
  immersion U = Spec R -> Spec(A') with A' the integral closure of A in R;
  A' = S because S lies in R. So U is open in Y and pi: Y -> A^2 is finite.
  U is the actual source, not an abstract chart. CONFIRMED.
- Degree one: S = A. A prime divisor V(p) of A^2 omitted from U would make p
  a unit of R = C[z_1,z_2], i.e. a nonzero constant, while A -> R is injective
  and p is nonconstant. So the complement has codimension >= 2, algebraic
  Hartogs on the normal A^2 gives Gamma(U,O) = A, i.e. R = A, and z_1, z_2 lie
  in C[F_1,F_2]: F is an automorphism. Contrapositive as stated. CONFIRMED.
- Degree > 1: purity (Zariski--Nagata) applies with Y normal, A^2 regular, pi
  finite surjective; unramified in codimension one would force pi etale. A
  connected finite etale cover of A^2(C) has degree one (simple connectivity
  plus Riemann existence), contradiction. So a height-one prime E of S with
  ramification index e > 1 exists (char 0: ramified iff e > 1). E misses U,
  since F = pi|_U is etale and would force e = 1 at the generic point of E.
  CONFIRMED.
- Local form at a general closed point p of E: Y smooth there (normal surface,
  isolated singularities), branch curve B = pi(E) smooth at pi(p), E -> B
  etale at p (generic, char 0), no other component of pi^-1(B) or of Y minus U
  through p (all finite sets avoided). With u a defining function of B and v a
  coordinate along B: pi*u = t_0^e (unit); put t = t_0 (unit)^{1/e},
  s = pi*v. Then dt wedge ds != 0 at p (ds restricts nonzero to E, dt is
  conormal), and pi(t,s) = (t^e, s) exactly. After shrinking, {t != 0} lies
  in U because Y minus U coincides with E near p. CONFIRMED.
- Measure: dmu = exp(-|w|^2) F*(dV_w) and in the chart F*(dV_w) equals
  |d(w)/d(u,v)|^2 composed with pi times e^2 |t|^{2e-2} dA(t) dA(s); the
  coordinate-change Jacobian and the Gaussian are bounded above and below on
  the shrunken bidisc. Hence dmu is comparable to |t|^{2e-2} dA(t) dA(s) with
  two fixed constants. No properness of F enters. CONFIRMED.

### Claim 3 (global witness h_0 with v_E(h_0) = 1-e): CONFIRMED

- Ybar = normalization of P^2 in L is projective, finite over P^2, and
  restricts to Y over A^2 (normalization is local on the base). A resolution
  r: M -> Ybar isomorphic over the smooth locus exists (import: resolution of
  normal projective surfaces, e.g. the minimal one). Z = f^-1(A^2) = r^-1(Y)
  is smooth, rho = r|_Z is proper (base change), and rho is an isomorphism
  over U and over a neighbourhood of p.
- G = rho_* omega_Z is coherent (import: proper pushforward). On the affine Y
  every quasi-coherent sheaf is the tilde of its global sections and is
  generated by them; Gamma(Y,G) = Gamma(Z, Omega^2_Z). Near p, G is the line
  bundle omega_Y, so the fibre G(p) = G_p tensor k(p) is C, nonzero.
  Surjectivity of Gamma(Y,G) tensor O_Y -> G at the stalk at p, reduced modulo
  m_p, yields a global regular two-form omega on Z with omega(p) != 0: in the
  chart omega = phi dt wedge ds with phi(p) != 0, so v_E(omega) = 0. The
  nonzero fibre is genuinely supplied by global generation; no local form is
  assumed to extend. CONFIRMED.
- Omega = F*(dw_1 wedge dw_2) = c dz_1 wedge dz_2 on U, and omega|_U lies in
  Gamma(U, Omega^2_U) = R dz_1 wedge dz_2, so h_0 = omega/Omega is in R: a
  polynomial on the whole actual source. On Z near p, Omega equals
  (jac composed with pi) e t^{e-1} dt wedge ds with jac a unit, so
  v_E(Omega) = e-1 and v_E(h_0) = 1-e. Explicitly h_0 = t^{1-e} psi(t,s) with
  psi holomorphic on the full bidisc and psi(0,0) != 0, so the Laurent
  leading coefficient a_{1-e}(s) = psi(0,s) is nonzero at s = 0 and nearby.
  CONFIRMED.

### Claim 4 (integrability, h_0 in H_F): CONFIRMED, no smuggling found

- Infinity support: omega is a rational section of K_M regular on Z, so its
  polar divisor is supported on M minus Z = f^-1(H_infty) = Supp div(sigma),
  sigma = f* s_infty. That set is the zero locus of a section of a line
  bundle on the irreducible surface M, hence pure of dimension one, and each
  component D_i has ord_{D_i}(sigma) >= 1. For m at least the largest pole
  order of omega, beta = sigma^m omega has no divisorial poles. CONFIRMED.
- Codimension two: M is smooth, hence normal, so a rational section of a line
  bundle regular off a codimension-two set is regular; beta is a global
  section of K_M tensor f*O(m). CONFIRMED.
- Metric: |s_infty|^2_FS = |W_0|^2 / sum |W_i|^2 = (1+|w|^2)^-1 on the affine
  chart, so |sigma|^2 = (1+|f|^2)^-1 on Z. beta is continuous on compact M,
  so |beta|^2 <= C and |omega|^2_{K_M} <= C (1+|f|^2)^m on Z. CONFIRMED.
- Metric cancellation for top forms: for omega = phi dz_1 wedge dz_2 and a
  Hermitian metric h, |omega|^2_{K_M} = |phi|^2 / det h while dvol_M equals
  det h times the standard coordinate volume form (universal constant), so
  |omega|^2 dvol_M = const times omega wedge conj(omega), independent of the
  metric. CONFIRMED.
- Gaussian integral: integral_Z exp(-|f|^2) |omega|^2 dvol_M is at most
  C sup_{q >= 0} (1+q)^m exp(-q) Vol(M), finite. The Gaussian is used only
  through this pointwise bound on Z; |f| need not be exhaustive on Z, so no
  properness of F is used. CONFIRMED.
- Equivalence with the H_F norm: on U inside Z, omega = h_0 Omega =
  h_0 c dz_1 wedge dz_2 and |f| = |F|; by the cancellation identity the
  integrand equals const times |h_0|^2 |c|^2 exp(-|F|^2) dV_z = const times
  |h_0|^2 dmu. So ||h_0||^2_mu is bounded by a constant times the finite
  Z-integral. CONFIRMED.
- Resolution choice is irrelevant to existence (a further blow-up pulls
  regular forms back to regular forms). Not every polynomial is claimed
  integrable: for general h in R the form h Omega has poles along components
  of Y minus U inside Z (along E whenever v_E(h) < 0), so the compactification
  bound does not apply to it; the argument is specific to forms regular on
  all of Z. Forms live on the smooth Z, never as reflexive forms on Y, so no
  rational-singularity or Grauert--Riemenschneider input is used. CONFIRMED.

### Claim 5 (Laurent and derivative step): CONFIRMED

- For entire h restricted to the punctured bidisc, a_k(s) = (2 pi i)^-1
  contour integral of h(t,s) t^{-k-1} dt is holomorphic in s. Tonelli plus
  circle Parseval: integral |h|^2 |t|^{2e-2} dA(t) = 2 pi sum_k |a_k(s)|^2
  integral_0^eps r^{2k+2e-1} dr, finite iff a_k(s) = 0 for all k <= -e (a.e.
  s, then every s by the identity theorem). Threshold 1-e confirmed; it is not
  itself needed for nondensity.
- Lift: dpi(d_t) = e t^{e-1} d_u and dpi(d_s) = d_v, so the lift of d_u is
  (1/e) t^{1-e} d_t. Lifting is linear over target functions and
  d_u = sum_i (dw_i/du) d_{w_i}, so (1/e) t^{1-e} d_t h = sum_i b_i D_i h with
  b_i = (dw_i/du) composed with pi, bounded holomorphic on the shrunken
  bidisc. For h in E_F this lies in L^2(bidisc, mu). Both D_i are involved,
  so the common domain is the right object. CONFIRMED.
- Weight cancellation is exact: |(1/e) t^{1-e} d_t h|^2 |t|^{2e-2} =
  e^-2 |d_t h|^2, so the unweighted integral of |d_t h|^2 over the bidisc is
  finite. Parseval: integral |d_t h|^2 dA(t) = 2 pi sum_k k^2 |a_k(s)|^2
  integral_0^eps r^{2k-1} dr; for k < 0 the radial integral diverges and
  orthogonality forbids cancellation across k, so a_k = 0 for every k < 0
  (Fubini for a.e. s, then identity theorem). k = 0 contributes 0 and is
  unconstrained; constants are neither excluded nor needed. CONFIRMED.
- Coordinate changes: "all negative coefficients vanish" is chart-independent
  (h extends holomorphically across E near p); the value a_{1-e}(s_0)
  depends on the chart, but ell is defined in one fixed chart. CONFIRMED.
- Old punctured control (e = 2) recomputed: u = s^2, v = y/(2s), det = 1,
  measure 4|s|^2 exp(-|s|^4-|v|^2) dA(s) dA(v); h = 1/s has finite norm
  4 pi integral exp(-|s|^4) dA(s); the lift of d_u is (1/(2s)) d_s and
  D_u h = -(1/2) s^-3 with norm integral r^-3 dr, divergent. Matches.

### Claim 6 (continuous separation): CONFIRMED

- ell(h) = a_{1-e}(s_0) = (2 pi i)^-1 contour integral over |t| = r_0 of
  h(t,s_0) t^{e-2} dt: exponent -k-1 at k = 1-e is e-2. Linear in h and
  independent of r_0 in (0, eps).
- Continuity in the full H_F norm: the circle K is compact inside the
  punctured bidisc, which is biholomorphic to an open subset of the actual
  source C^2; take a compact neighbourhood N of K there. The density
  |c|^2 exp(-|F|^2) is continuous and positive on N, hence >= m_N > 0. By
  compactness there is delta' > 0 with B(z,delta') inside N for every z on K,
  and the holomorphic submean inequality gives |h(z)|^2 <= (m_N Vol B)^-1
  ||h||^2_mu. Cauchy then gives |ell(h)| <= r_0^{e-1} sup_K |h| <= C' ||h||_mu.
  This is the L^2(mu) norm, not a graph norm and not a boundary evaluation at
  t = 0. CONFIRMED.
- Annihilation: for every h in E_F, Claim 5 gives a_k = 0 for all k < 0, and
  1-e <= -1, so ell(E_F) = 0; continuity gives ell = 0 on the closure. Claim 3
  gives ell(h_0) = psi(0,s_0) != 0 and Claim 4 gives h_0 in H_F. Hence
  closure(E_F) lies in ker(ell), a proper closed hyperplane. This is
  nondensity, strictly stronger than E_F != H_F. CONFIRMED.
- The remark that H_F is closed in L^2(mu) (locally bounded weight, L^2_loc
  limits of holomorphic functions are holomorphic) is correct but not needed.

### Claim 7 (converse, controls, scope): CONFIRMED

- F automorphism: w = F(z) gives dV_w = |c|^2 dV_z, so h -> h composed with
  F^-1 is an isometry of H_F onto the Fock space of C^2 with weight
  exp(-|w|^2) dV_w, intertwining D_i with d/dw_i. Monomials are orthogonal by
  rotation invariance; ||w^alpha||^2 = prod_i integral_C |w_i|^{2 alpha_i}
  exp(-|w_i|^2) dA = pi^2 alpha!; Parseval on polydiscs with monotone
  convergence gives ||phi||^2 = sum |c_alpha|^2 pi^2 alpha! for entire phi in
  the space, so Taylor truncations converge in norm. Polynomials lie in both
  derivative domains. Identity map is the trivial positive control. CONFIRMED.
- Scope: the proved implication identifies the holomorphic density premise
  with invertibility for a hypothetical counterexample. It refutes nothing
  about actual maps (which may all be automorphisms), proves no density, no
  completeness, no spectral bound, no all-polynomial moment bound, and no
  JC2. The sentences about the reviewed real Sobolev core and the fixed
  spectral control are comparison statements about linked reports I did not
  open; the proof does not depend on them, and "real density does not imply
  holomorphic-subspace density" is consistent with everything here. No
  novelty claim is made or needed. CONFIRMED with the contextual dependencies
  listed in Section 3.

## 2. Attack log (what was tried and did not break the result)

- Circularity through "all polynomials are in H_F": not used; only forms
  regular on all of Z are integrated over the compactification, and a general
  h Omega has poles along E.
- Hidden properness of F: not used; only compactness of M and a pointwise
  bound on Z.
- ell as a disguised boundary evaluation: no; fixed interior circle,
  submean on a compact set where the density is bounded below.
- a_{1-e} of h_0 vanishing identically in s: no; it equals psi(0,s) with
  psi(0,0) != 0.
- The k = 0 term: unconstrained, irrelevant because ell reads k = 1-e <= -1.
- E meeting U: impossible, etaleness on U forces e = 1 at the generic point.
- Degree one hiding a non-automorphism: impossible, Hartogs on A^2 forces
  R = A.
- FALLACY-v2 bullets: no exit claim is made, so no charge_basis line is owed;
  the L^2 witness is an attained element, not a floor; the pole-order
  identity v_E(h_0) = 1-e is computed at a general point with every
  hypothesis (smoothness, single branch component, etale E -> B) checked;
  the ring chain A in S in R in L is explicit, so no name-matching fallacy.

## 3. Accepted imports and unverified dependencies

Accepted as classical with applicability checked, no fresh primary audit:
finiteness of integral closure (finite type, char 0); algebraic Zariski Main
Theorem (open immersion into the spectrum of the integral closure);
algebraic Hartogs on normal schemes; purity of the branch locus
(Zariski--Nagata); Riemann existence with simple connectivity of C^2;
resolution of normal projective surfaces isomorphic over the smooth locus;
coherence of proper pushforward; global generation of quasi-coherent
sheaves on affine schemes; local form of a finite map at a general smooth
ramification point; Laurent expansion, Parseval, Cauchy, submean.

Not verified by me: the Stacks tag numbers 02O3 / 01I6 / 0BMB and their
section numbering (no network); the contents of the six linked reports and
the two notes.md entries (not opened, by charge). The basis commit 51e9d220
named in the report is the parent of the frozen cc870925, and the reviewed
report's bytes at cc870925 equal the snapshot (checked, see Section 6).
None of these is a mathematical dependency of Sections 3--7.

## 4. Contract compliance notes

COORDINATION: exact statement, evidence tier, lifecycle, producer model,
dependencies, comparison, known gaps, a COLLISIONS block and a terminal
BODY-END line are all present; the work is desk-only, so no replay block is
owed. This review is by a different model (claude-fable-5-1 versus
gpt-6-astra), which satisfies the different-model requirement; the producer
correctly records that its same-model co-check is not a FIRST. Cosmetic: the
report file name uses "root" in the model slot. Neither the producer nor this
review raises any OPEN entry.

## 5. Verdict

All seven charged items: CONFIRMED. No REFUTED item, no GAP. The proof of
"closure(E_F) = H_F iff F is a polynomial automorphism" is complete modulo
the named classical imports, at evidence tier MANUAL, with the conditional
scope exactly as the producer states it. I found no obstruction to ROOT
moving the report to PROVISIONAL / PROMOTED at that tier and scope; the
decision is ROOT's.

<!-- REVIEW-MATH-END -->

## ROOT disposition

Promote only the exact density/invertibility equivalence, with its
global L2 polynomial witness and continuous separation proof under
hypothetical noninvertibility, at MANUAL evidence tier with the named
classical imports and the binding reviewer correction above.
No new density proof, counterexample, general polynomial-integrability
claim, completeness, spectral conclusion, symmetry or JC2 resolution.
No scientific descendant or broader ideation-clock reset follows.

ROOT integration and complete readback finished by measured19:48:24 UTC.
The verbatim review block matches original lines29--285 byte-for-byte;
the trusted administrative collision check returned EMPTY. Final custody
and ledger integration follow without changing the original review.

## OPENS RAISED

None. The existing global density premise is not converted into a new
smaller task or a claimed consequence of the real Sobolev core.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21336`.
- Body SHA-256:
  `35fcc8544fbd84097abdc702b64c684db49f1c35f0a12afad03e28df8c3036a5`.
- Frozen basis: `cc870925bc0b057fcc77a352f6909a50a943c25d`.
