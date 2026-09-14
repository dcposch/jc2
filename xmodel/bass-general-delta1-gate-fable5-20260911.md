# FIRST hostile gate: arbitrary complex first-delta-order operators

tag: bass-general-delta1-gate-fable5-20260911
reviewer: Fable5.1 (independent, different model from Astra/ROOT)
opened: 2026-09-11 21:51:38 UTC
status: IN PROGRESS (skeleton; body follows)

## Input pins (pre-read)

bass-general-delta1-astra-20260911.md f4d2eedb3254659deb36d4437e1f632825af9ef68ba1caf38c81d8b10e91f9d7 (match)
bass-1989.pdf 86f642941d2cea0f1d438996d8e81833ac53b6039c4c81e1564adc411f614b1e (match)

## Sections
A. Recurrence / exhaustion / algebraicity / vertical factor
B. Nonlinear test G=Y-(X-r)^2 and Fabry
C. General complex G, Puiseux root argument
D. Formal vs actual-source assertion, Bass 1.4 under shear
E. Controls, scope, strongest surviving conclusion

## Verdict

Producer report read WHOLE (11,623 B, hash matched before reading). Bass printed 41--42 and 49 read via pdftotext to stdout (PDF pages 4--5 and 12), no files created. All five items were re-derived independently; no CAS, code or numerics.

Summary: A CONFIRMED. B CONFIRMED. C CONFIRMED modulo the listed standard premises (none freshly primary-verified by producer or by me). D CONFIRMED as a two-tier statement: the formal assertion for nonconstant G without accessible vertical factor is self-contained modulo standard analysis; the actual-source assertion for ALL G is CONDITIONAL on Bass 1.4 (externally trusted) in the vertical and constant cases, where the formal assertion is provably false. E scope respected. I found no refutation. The genuine weak points are external premises, not the producer's own steps.

## A. Recurrence, exhaustion, algebraicity, vertical factor -- CONFIRMED

Own derivation. On p^a q^b, G(e_p,e_q) then delta gives Phi(p^a q^b) = (a-r)p^a q^b + b G(a,b) p^(a+1) q^(b-1); total degree preserved. In degree d, coefficient x_i of p^i q^(d-i) satisfies (i-r)x_i + (d-i+1)G(i-1,d-i+1)x_(i-1) = 0, i = 0..d, with no x_(-1) term. Triangular with diagonal i-r: for r>0, x_0 = 0 and inductively x_i = 0 for i<r; the i=r equation is 0 = 0; for r=0 x_0 is free. So d<r has zero kernel, every degree d = r+n has a one-dimensional kernel, and with j = i-r the recurrence is exactly the producer's; unrolling gives V(n,j) = (-1)^j binom(n,j) prod_(k<j) G(r+k,n-k) with the LEFT-delta argument G(r+k,n-k), not G(r+k+1,n-k-1). (1) and (2) are exact and exhaustive.

Algebraicity of H: F(p,q,p^r T) is a nonzero polynomial; dividing by its exact p-power leaves a nonzero Q(q,T) at p=0; f/p^r = H + p S is a formal series, so Q(q,H(q)) = 0. If Q were independent of T it would be a nonzero polynomial in q equal to zero, impossible; hence H is algebraic over C(q). The producer's "lowest p-weight relation with wt(T)=r" is right. No projection property of algebraic series is assumed.

Vertical factor: G = (X-(r+J))G_1 gives G(r+J,n-J) = 0, so V(n,j) = 0 for all j >= J+1 and every n. Formal kernel elements have p-degrees in [r,r+J] and are killed by Psi = prod_(j<=J)(e_p-r-j), a nonzero element of C[e_p,e_q] (commuting diagonal operators). Bass 1.4's first sentence is the module statement "B/A est un module sans torsion sur C[e_x,e_y]"; torsion-freeness for a nonzero product follows from the irreducible cases by peeling factors in the UFD. G=0 is the J=0 case. The countercontrol p^r/(1-q) is correct: for vertical G the FORMAL assertion is false (also G = X-r-1 gives p^r H - p^(r+1) H' with H = 1/(1-q)), so Bass 1.4 is load-bearing there.

Finite-prefix reduction: Bass p.41 text confirmed: "phi f in A signifie que phi f_d = 0 pour tout d > N", f_(N) in A, phi(f - f_(N)) = 0, "on peut remplacer l'hypothese phi f in A par phi f = 0". Phi is homogeneous of degree 0 in (p,q) and preserves R (lifted derivatives are polynomial by J=1), so f - f_(N) in R and is an exact kernel element. Only a finite prefix is subtracted; no infinite subseries is asserted in R.

## B. G = Y-(X-r)^2 -- CONFIRMED

g(k,n) = n-k-k^2 = n-k(k+1). For n = m(m+1), the k=m factor vanishes, so V(n,j) = 0 for j >= m+1; the last live j is m ~ sqrt(n), sublinear. Correctly refutes any uniform linear nonzero window.

Inequality: for n >= 8 and k >= ceil(n/2), k(k+1)-n >= (n/2)(n/2+1)-n = n(n-2)/4 >= n^2/8 iff n >= 4. There are n - ceil(n/2) = floor(n/2) such k; the other factors are nonzero integers of modulus >= 1 off E. So |V(n,n)| >= (n^2/8)^floor(n/2) and its n-th root is >= (n^2/8)^(1/2 - 1/(2n)) -> infinity. Edge cases n in {0,2,6} and n<8 are finitely many and irrelevant to radii.

f(p,0) algebraic: divide F by its exact q-power, the q=0 coefficient is a nonzero polynomial in (p,T), specialise. One-variable algebraic formal series converge (standard); Cauchy gives |c_n V(n,n)| <= M rho^(-r-n), hence |c_n|^(1/n) -> 0 off E and H_good is entire. H is algebraic (A), so convergent; H_bad = H - H_good has positive radius; its support is a subset of E, whose l-th element is >= (l-1)l, so nu_l/l -> infinity.

Fabry version: Bass p.49 states (13) "n_m/m -> infinity" and concludes via "theoreme de Fabry (1896) (cf. [D], Ch. XI, 3.11) que tout point du cercle de convergence est singulier". That is the density-zero (Fabry) gap theorem, not the Hadamard ratio version; the producer's nu_l/l -> infinity hypothesis is exactly Bass's (13). The mechanism "algebraic function has finitely many singular points, hence converges everywhere, hence polynomial by [B] Prop. D.1" is verbatim on p.49. The producer's extra step (H_bad natural boundary survives addition of the entire H_good, contradicting finitely many singularities of H) is the producer's own and is trivially valid: singular points of H and H_bad on |q| = R_bad coincide. Neither subseries is presumed algebraic. Bass p.49 licenses the cited mechanism; the "plus entire" twist is not on p.49 but needs nothing beyond it.

## C. General complex G -- CONFIRMED modulo standard premises

Own audit of each listed point.

- Leading coefficient / v=0: g(k,n) = G(r+k,n-k) has k-degree v <= deg G with leading coefficient A(n) in C[n], A nonzero since G nonzero; v=0 iff G = A(X+Y-r), and nonconstant G then forces deg A >= 1, so |A(n)|^n gives the growth with only finitely many zeros of A. Finitely many n with A(n)=0 for v>=1 are discarded harmlessly.
- Epsilon and sigma: with finitely many branches, epsilon < min|c|/4 over slope-1 branches and sigma in (max s<1, 1) exist. For n^sigma <= k <= epsilon n: sublinear/bounded branches have |z| <= n^sigma/2 <= k/2, slope-1 branches |z| >= |c|n/2 >= 2 epsilon n >= 2k, superlinear larger; so |k-z| >= k/2 and (5) holds with gamma+v >= 1.
- Early window k < n^sigma, classification: non-real branch has |Im z| >= c n^(-L0) from the first nonzero imaginary Puiseux coefficient (uniform in k); real bounded branch tends to a real a: if a not in Z constant separation, if a in Z and z not identically a the first nonzero term gives |z-a| >= c n^(-t) while |z-k| >= 1/2 for k != a; z identically an integer J>=0 forces G(r+J,Y) = 0, the excluded factor; J<0 and negative unbounded branches stay >= 1/2 from k>=0; a=0 approached from below (z = -1/n) is the a in Z case. Real positive unbounded branches with s >= 1 lie outside the window. Only c>0, 0<s<1 remain. Tiny nonzero complex factors cannot escape: a Puiseux series has no sub-polynomial nonzero terms, so every non-excluded distance is bounded below by a fixed power of n. Repeated roots multiply exponents only.
- Sublinear positive branch: z' = cs n^(s-1)(1+o(1)) > 0 eventually; on [N,2N] z' >= C N^(s-1); range length O(N^s) hence O(N^s) integer targets; for fixed target t the set {n : |z(n)-t| < N^(-L)} is an interval of length O(N^(1-s-L)) < 1 for L > 1-s, so at most one integer n. Summing dyadic blocks and finitely many branches: |E_* cap [1,X]| = O(X^sigma) after raising sigma below 1. Then nu_l >= (l/C)^(1/sigma), nu_l/l -> infinity.
- Product growth off E_*: O(n^sigma) early factors each >= C n^(-L''), loss O(n^sigma log n); middle factors >= 1 eventually; k in [epsilon n/2, epsilon n] give >= C n^(gamma+v), so log|V(n,floor(epsilon n))| >= (epsilon/2)(gamma+v) n log n - O(n^sigma log n) - O(n), n-th root -> infinity. This holds for ALL sufficiently large good n (all bounds are uniform in k and n >= n_0), not a subsequence. Exact zeros g(k,n)=0 at large n arise only on positive sublinear branches at dist 0 < n^(-L), so they lie in E_*; the cofinite V(n,n)=0 control is exactly why the moving window j = floor(epsilon n) is used.
- Uniform coefficient bound: complex algebraicity of f in C[[p,q]] gives convergence on a polydisc, then Cauchy gives |c_n V(n,j)| <= M rho^(-r-n) with r+n the total degree. For actual f in R the analytic inverse function theorem suffices without the algebraic-convergence theorem.

Standard premises used (exact versions), not primary-verified by producer or here: (P1) a formal power series in C[[p,q]] algebraic over C(p,q) converges near 0 (algebraic power series are convergent); (P2) one-variable version of P1; (P3) Newton--Puiseux at infinity: roots of P in C[n][k] with A(n) not identically 0 admit convergent expansions in n^(-1/e), finitely many positive powers, valid for real n >= n_0, termwise differentiable; (P4) Fabry gap theorem, density-zero form (Dienes XI 3.11 as Bass cites); (P5) an algebraic function element has finitely many singular points; (P6) entire algebraic over C(q) is polynomial (Bass's [B] Prop. D.1). Minor imprecision only: "O(1) integer-degree count" is in fact <= 1; L need only exceed 1-s, the producer's stronger choice is harmless.

## D. Formal versus actual assertion -- CONFIRMED, two tiers

Formal tier (self-contained modulo P1--P6): for every nonconstant G with no factor X-(r+J), J>=0, every algebraic f in C[[p,q]] with Phi f = 0 is a polynomial. Verified through C.

Actual tier for ALL G, on N = R/A: normalization puts source (0,0) over target (0,0); Keller Jacobian gives the formal (indeed analytic) inverse and the embedding R -> C[[p,q]]; trdeg C(p,q) = 2 so R is algebraic over C(p,q); the lifted derivations are the unique derivations of R dual to dp,dq and agree with formal partials under the embedding. Linear shear: with p' = p, u = q - gamma p, the dual derivations are d_(p') = d_p + gamma d_q, d_u = d_q, so e_(p') = e_p + gamma delta and Phi = e_(p') - r exactly as claimed; (p',u) is again a normalized Keller pair with the same A and R, so Bass 1.4 applies in that frame. The formal assertion is false for constant nonzero G (kernel p^r C[[u]] contains p^r/(1-u)) and for vertical G, so Bass 1.4 is indispensable there. Tier label: CONDITIONAL on Bass 1.4 (external, trusted at this scope, including its proof and the source setup); this gate is not a source audit. OCR of 1.3's sign conditions on c is unreadable, but only the unconditional module sentence of 1.4 is used, so nothing depends on it.

## E. Controls, scope, surviving conclusion

Controls: G = (Y-1)(X-r+1) gives g = (n-k-1)(k+1), roots n-1 (slope 1) and -1 (negative constant), V(n,n) = 0 for n>=1 but V(n,floor(epsilon n)) != 0; correctly a non-counterexample showing the fixed q=0 column is useless. B's sublinear zeros at n = m(m+1) confirmed. Rational germs p^r/(1-q), p^r/(1-u) are exactly the algebraic non-polynomial kernel elements in the vertical/constant cases and are excluded from N only by Bass 1.4.

Scope: the report claims no source realization of Phi, no normal form for arbitrary U-annihilators, no general U-torsion theorem, no properness, novelty or JC2; Bass 1.5 does not cover this family because phi_0 = e_p - r is special linear, and the left-delta form equals a right-delta form with G(e_p-1,e_q+1), so no exhaustion is implied. Compliant.

Strongest surviving conclusion if a part fails: if P1 (two-variable algebraic convergence) were doubted, the actual-source assertion still stands because f in R converges by the inverse function theorem, and only the purely formal tier would need P1. If Bass 1.4 were withdrawn, the nonconstant non-vertical formal tier survives intact and injectivity on N would hold for exactly that class of G; the vertical and constant cases would revert to Bass's own open status. No step internal to the producer's argument was found wrong.

## Custody

Opened 2026-09-11 21:51:38 UTC; skeleton written before any input read. Input pins recomputed before reading matched the expected values (see top). Postpins and readback appended below after the body draft. No other file written, no jc2-lean access, no network, no code.

## Postpins and readback

Own WHOLE readback of this report done 2026-09-11 22:00:53 UTC (headings A--E present, no marker before this section). Input postpins recomputed at the same time:

bass-general-delta1-astra-20260911.md f4d2eedb3254659deb36d4437e1f632825af9ef68ba1caf38c81d8b10e91f9d7 (unchanged)
bass-1989.pdf 86f642941d2cea0f1d438996d8e81833ac53b6039c4c81e1564adc411f614b1e (unchanged)

Status: SEALED body, verdicts as stated. No artifact_finalize; launcher owns custody. No charge_basis declaration.

<!-- BODY-END -->
