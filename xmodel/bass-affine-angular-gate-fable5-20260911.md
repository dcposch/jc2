# FIRST hostile gate: affine angular operator classification (Fable5.1)

tag: bass-affine-angular-gate-fable5-20260911
reviewer: Fable5.1 (claude-fable-5-1), independent different-model gate
skeleton written: 2026-09-11T21:31:40Z (UTC); body written 2026-09-11T21:36Z
charged report: xmodel/bass-affine-angular-root-20260911.md (read WHOLE)
charged source: bass-1989.pdf, printed 41--42 and 49 (PDF pages 4--5, 12),
pdftotext to stdout only. No other file, ledger, live report or external
source was read. No code, CAS, numerics, network or process inspection.

## Inputs (hashed before reading)
- bass-affine-angular-root-20260911.md sha256
  a6a6f06b201aeeed7e621b5a4a992443511592dc81af545ffd7f265791235ed5 (MATCH)
- bass-1989.pdf sha256
  86f642941d2cea0f1d438996d8e81833ac53b6039c4c81e1564adc411f614b1e (MATCH)

## Summary of verdicts
A CONFIRMED. B CONFIRMED. C CONFIRMED. D CONFIRMED at the conditional tier
stated below (one OCR GAP, not load-bearing). E CONFIRMED as a scope
statement. No counterexample found; two presentational nits recorded.

## A. Degreewise kernel, recurrence (1), algebraicity of H -- CONFIRMED

Independent derivation. With literal LEFT delta order, Phi acts on a
monomial by first applying A ep+B eq+C, then delta:

    Phi(p^i q^j) = (i-r) p^i q^j + j (A i+B j+C) p^(i+1) q^(j-1).

Total degree is preserved, so ker Phi on C[[p,q]] is the product of the
degreewise kernels. In degree d with f_d=sum a_i p^i q^(d-i), the
coefficient of p^m q^(d-m) in Phi f_d is

    (m-r) a_m + (d-m+1)(A(m-1)+B(d-m+1)+C) a_(m-1),   a_(-1)=0.

The matrix is triangular with diagonal m-r. For d<r every diagonal entry
is nonzero and induction from m=0 kills all a_m: kernel zero. For d=r+n,
the same induction gives a_m=0 for m<r, the m=r equation is 0=0 (a_r is
free), and for m=r+j, j>=1, the entry j is nonzero. Writing K=A r+C and
a_(r+j)=V_(n,j) with V_(n,0)=1, the equation is exactly

    j V_(n,j) + (n-j+1)[B n+K+(A-B)(j-1)] V_(n,j-1) = 0,

since A(r+j-1)+B(n-j+1)+C = K+Bn+(A-B)(j-1). Unwinding gives (1). Thus
each degree d>=r contributes one free coefficient c_n and (2) is the
complete formal kernel. If the RIGHT delta order were used the second
term would carry (A(i+1)+B(j-1)+C); the report's recurrence carries the
left-order factor, so the literal order is respected.

Algebraicity of H. Q(p,q,f)=0, weights (1,0,r). The weighted-homogeneous
part Q_mu applied to f=p^r H+p^(r+1)G equals p^mu Q_mu(1,q,H) plus terms
of p-order >mu. The lowest weight mu_0 present therefore gives
Q_(mu_0)(1,q,H)=0 as the p^(mu_0)-coefficient of the zero series, and
Q_(mu_0)(1,q,T) is a nonzero polynomial because a=mu_0-rk is determined
by k. Only p-orders in C[[q]][[p]] are used; no constant is substituted
into a formal series. Nit: the report's phrase "every summand has
p-degree mu after substitution" should read "p-order >= mu with
p^mu-part q^b H^k"; the conclusion is unaffected.

## B. B!=0 polynomiality and the Section 5 coefficient bound -- CONFIRMED

Section 5 audited step by step. (i) p=tz, q=z sends p^a q^b to
t^a z^(a+b), injective on C[p,q][T], so Q(tz,z,T) is a nonzero polynomial;
writing it as sum R_(bk)(t) z^b T^k, some R_(bk) is nonzero, so only
finitely many t make it vanish identically. (ii) For fixed t the map
C[[p,q]] -> C[[z]] is a continuous substitution of series without constant
term, hence a ring map; f goes to sum_d P_d(t) z^d with P_d(t)=F_d(t,1),
each coefficient a finite polynomial. So Q(tz,z, sum P_d(t)z^d)=0 with a
nonzero polynomial (its T-degree is >=1, else a nonzero R(z) would be
zero). Univariate algebraic formal series converge: standard external
background, correctly labelled. Hence |P_d(t)|<=M^(d+1) with M=M(t).
(iii) On a closed disk D avoiding the exceptional t, the sets
S_M={t in D: |P_d(t)|<=M^(d+1) for all d} are closed (intersection of
closed sets) and cover D; Baire gives S_M with nonempty interior in D, and
since int(D) is dense in D this contains a genuine closed disk of radius
eta about some t0. (iv) Cauchy on that disk bounds the Taylor
coefficients of P_d at t0 by M^(d+1) eta^(-j); summing d+1 terms on |t|=1
gives L^(d+1); a second Cauchy estimate on |t|=1 bounds every coefficient
of P_d, i.e. of F_d, by L^(d+1). Nothing here presumes two-variable
convergence; uniformity is manufactured by Baire from univariate
convergence only.

Growth argument for B!=0. Fix 0<epsilon<1 with epsilon|A-B|<=|B|/4
(possible since B!=0), j_n=floor(epsilon n). For 0<=k<j_n and
n>=4|K|/|B|: |Bn+K+(A-B)k| >= |B|n-|K|-|B|n/4 >= |B|n/2. The monomial
p^(r+j_n) q^(n-j_n) has total degree r+n, so its coefficient in f is
exactly c_n V_(n,j_n) (no other n contributes). With binom(n,j_n)>=1,
|c_n| (|B|n/2)^(j_n) <= L^(r+n+1), so |c_n|^(1/n) -> 0 because
j_n/n -> epsilon>0. H is entire and algebraic over C(q), hence polynomial
(root bound |H(q)|<=C|q|^N outside a disk from the leading coefficient of
its minimal relation, then Cauchy). Finitely many c_n gives f polynomial.
The early index is essential: with A=0,B=1,C=-1,r=0 the factor
n-1-k vanishes at k=n-1 for every n>=1, so the q=0 coefficient is
identically zero and would prove nothing; j_n<epsilon n<n-1 avoids all
such late zeros. I checked this example by hand: q and q^2-2pq are killed
by Phi, as (1) predicts.

## C. B=0 cases, formula (3), shear (4), controls -- CONFIRMED

B=0, A!=0: factors are K+Ak. If -K/A is not a nonnegative integer, no
factor vanishes; the p^(r+n) q^0 coefficient is c_n(-1)^n prod(K+Ak).
The last n/2 factors are each >=|A|n/4 for large n, so the nth root of
the product grows like sqrt(n); with the Section 5 bound this forces
|c_n|^(1/n)->0, H entire, hence polynomial. Nit: the report calls f(p,0)
a "convergent algebraic restriction"; Q(p,0,T) could vanish identically,
but stripping the largest q-power from Q repairs this, and the Section 5
bound alone suffices anyway. Not a gap.

K=-A J: the factor at k=J is zero, so V_(n,j)=0 for j>J, for every n.
For j<=J, prod_(k<j) A(k-J) = A^j (-1)^j J!/(J-j)!, so
V_(n,j)=binom(n,j) A^j J!/(J-j)!. Since sum_n c_n binom(n,j) q^(n-j)
= H^(j)(q)/j! (binomial zero for n<j matches the vanishing derivative),
f = p^r sum_j binom(J,j)(Ap)^j H^(j)(q): formula (3) with ordinary
derivatives and correct factorial normalisation. Direct check r=0,J=1
(C=-A): Phi(H+ApH') = ApH' + A delta(-H) = 0. Check r=J=0 (C=0):
Phi=(1+A delta)ep, and 1+A delta is unipotent on each homogeneous piece,
so ker Phi = ker ep = C[[q]] = formula (3). Converse direction and
"algebraic iff H algebraic" follow from A above and closure of algebraic
elements under sums, products and derivatives. H=1/(1-q) gives a rational
germ whose p^r-coefficient is nonpolynomial, so f is nonpolynomial.

A=B=0: u=q-Cp gives p d/dp|_u = ep + C delta, so Phi = p d/dp|_u - r and
the formal kernel is p^r C[[u]], i.e. (4). Cross-check from (1):
V_(n,j)=(-1)^j binom(n,j) C^j sums to (q-Cp)^n. Includes C=0 and r=0.
The case split (B!=0; B=0,A!=0 split on -K/A in N; A=B=0) is exhaustive.
The report correctly labels (3),(4) as refuting ALL-GERM polynomiality
and not as actual-Keller examples.

## D. Actual-source corollary -- CONFIRMED, conditional tier

OCR of printed 42 reads: "1.4 THEOREME. B/A est un module sans torsion
sur C[e_x,e_y]", with three cases (a) finite-dimensional A_psi, (b) some
k!=0 with k psi special linear, (c) dim A_psi infinite but every
f in Ahat_psi algebraic over C(x,y) lies in A. Printed 41 shows
A=C[x,y] subset B subset Ahat=C[[x,y]] and the remark that, the
operators being homogeneous, "psi f in A" may be replaced by "psi f=0".
Printed 42 states the proofs use Siegel and Fabry; printed 49 shows the
Fabry lacunary step and "une serie partout convergente qui est algebrique
sur C(x) est un polynome".

Audit of the report's argument. Phi preserves total degree, so Phi f in
C[p,q] forces Phi f_d=0 for d>N; the finitely many f_d, d<=N, lie in
C[p,q] subset R, so the tail g is in R, algebraic (finite function-field
extension of the dominant Keller map), and Phi g=0. Formal inverse: the
Keller map is etale at the chosen source point, R -> completed local ring
= C[[p,q]] is injective and restricts to the identity on C[p,q]. Growing
cases: g is polynomial by B and C without Bass. Case (3): g has p-degree
<= r+J, so the nonzero element psi=prod_(i=0)^(r+J)(ep-i) of the
commutative ring C[ep,eq] kills g; torsion-freeness of R/C[p,q] over
C[ep,eq] gives g in C[p,q] directly, with no need to split psi into
irreducibles or to know which of (a),(b),(c) applies. Case (4): the
composite of the Keller map with the linear automorphism (p,q)->(p,u) is
Keller, fixes the source point over the origin, and leaves R, C[p,q] and
the embedding unchanged; 1.4 for that map is torsion-freeness over
C[p d/dp|_u, u d/du], which contains Phi. Normalised-coordinate hypothesis
is explicitly preserved: ep is not translation-invariant, so the family
is tied to the chosen target origin, and the source-point-over-origin
hypothesis is stated, not derived.

Evidence tier. The theorem STATEMENT of 1.4 is read from the charged
pages. Its proof (Siegel, Fabry, [B] Prop D.1) and the standing setup of
section 1 (the definition of B as the source ring under the formal
inverse, and any normalisation such as F(0)=0) sit on pages 39--40 and
43--49, outside this charge, and remain EXTERNALLY TRUSTED. The report's
use is consistent with the printed-41 context (1.4(c) says "en
particulier B_psi subset A", so B consists of algebraic elements).
GAP (OCR, not load-bearing): the inequality signs in 1.3's conditions on
c ("c<0 si a=0, c>0 si b=0" vs non-strict) are unreadable, so whether
ep itself (i=0) is special linear is undetermined; the D argument uses
only the ring-level torsion-freeness and never needs this.

## E. Scope and missing arrow -- CONFIRMED

The report claims only: exact formal kernels for the displayed family,
algebraic-germ classification, and a conditional injectivity on R/C[p,q].
It does not show that a general element of Bass's U annihilating a
source element can be taken with delta-degree one, diagonal part ep-r,
or affine delta-coefficient, and it says so. Observation on placement:
Bass 1.5 (printed 42) excludes exactly the psi whose delta-free part is a
multiple of a special linear element; the family here has delta-free part
ep-r, which is special linear for r>=1, so it lies in the complement of
1.5's hypothesis but covers only its delta-degree-one affine slice. No
source realisation, no global U-torsion theorem, no JC2 conclusion, no
novelty claim, no computation. The native growing-shear report is cited
by hash only; every step it is credited with is re-derived in the charged
text, and I did not open it or its gate. No charge_basis line: no
exit-price claim is made or consumed.

## Disposition
All five claims stand as written; the only defects are two wording nits
(A, C) and one OCR sign GAP that the argument does not use. Promotion to
REVIEWED is supportable at the stated conditional tier.

## Postpins (re-hashed after body, 2026-09-11T21:38:07Z)
- a6a6f06b201aeeed7e621b5a4a992443511592dc81af545ffd7f265791235ed5  bass-affine-angular-root-20260911.md
- 86f642941d2cea0f1d438996d8e81833ac53b6039c4c81e1564adc411f614b1e  bass-1989.pdf
Both unchanged from the pre-read pins.

<!-- BODY-END -->
