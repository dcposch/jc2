# FACE-ISOLATION — porting Wilson 2607.23887 (GMC(2)) to the Keller-pair setting

Study task, 2026-08-04. Sources: arXiv:2607.23887 (fetched abs + full HTML, quotes below
verbatim from the paper); RECON.md §2; LEMMA.md (vertex-gap lemma). Status per section:
§1 = read off the paper (reliable); §2–§4 = our analysis (candidate-grade); §5 = verdict.

## 1. Wilson's technique, distilled

**Paper:** Michael Wilson, "A face-isolation proof of the two-variable Gaussian Moments
Conjecture", arXiv:2607.23887 (math.PR/math.AC), 2026-07-26.

**Setup.** (X,Y) independent standard real Gaussians; complexify Z=(X+iY)/√2,
W=(X−iY)/√2. The whole moment functional is the diagonal rule

    E(Z^a W^b) = δ_ab · a!            (Eq. 2.1)

so with weight wt(Z^aW^b) = a−b, E kills every monomial of nonzero weight and weighs
the weight-zero line by factorials. Hypothesis: P ∈ C[X,Y] with E(P^m)=0 for all m≥1.

**Main theorem (support one-sidedness).** The monomial support of P (in Z,W) is
*strictly* one-sided in wt: either every monomial has wt>0 or every one has wt<0.
Corollary (GMC(2), explicit threshold): E(Q·P^m)=0 for every Q whenever m > deg Q —
because (Lemma 3) "every monomial of Q·P^m has weight ≥ m − deg Q", nonzero, and E
kills it. So GMC(2) follows from a pure Newton-polygon support statement.

**The engine — five moves.**

1. **Multinomial stratification (3.1).** E(P^m) = Σ_{k∈N^S, |k|=m, A(k)=B(k)}
   (m choose k)·(Π_α c_α^{k_α})·A(k)!, sum over multi-indices k on the support S,
   with balance A(k)=B(k) (total Z-exponent = total W-exponent: only weight-zero
   products survive E). Strata = multi-indices k; "pure-face" strata are those
   supported on one face F ⊂ S.

2. **Face selection.** Pick an integral linear form ℓ(a,b)=ca+db with c+d>0; the
   exposed face F = argmin_S ℓ, λ = min value. Compress F to ONE variable: the face
   weight (Laurent) polynomial R(z) = Σ_{α∈F} c_α z^{a_α−b_α} — the face pushed
   forward along the weight wt.

3. **Prime isolation (Lemma 7, the core).** For λ/(c+d) ≥ 0 with denominator B:
   CT R(z)^{Bn} = 0 for all n ≥ 1. Proof mechanism: work over K=Q(c_α), pick a good
   prime p — "(G1) p unramified in K; (G2) every c_α is p-integral; (G3) p∤(c+d);
   (G4) p > R₀" where q=Bn, R₀=qλ/(c+d) — and evaluate E(P^m)=0 at m=qp. The
   pure-face strata sum to (pR₀)!·CT R^{qp} with v_p((pR₀)!) = R₀ exactly; every
   mixed stratum has valuation ≥ R₀+1, by Kummer's theorem (a base-p carry in the
   multinomial coefficient) or a divisibility split (k = p·l). So the p-adic
   valuation SEPARATES the chosen face from all other strata: the vanishing of a
   global scalar forces a face-local scalar to vanish mod p.

4. **Frobenius reduction.** Mod p (residue field κ): CT(R̄^{qp}) = CT((R̄^q)^p) =
   (CT R̄^q)^p, "since κ is a field, it follows that CT R^q ≡ 0 (mod p)". Running
   over infinitely many good p lifts to characteristic zero: CT R^q = 0 for all q
   in the arithmetic progression Bn.

5. **Duistermaat–van der Kallen + boundary walk.** DvdK (one variable!): "a Laurent
   polynomial in one variable which is neither a polynomial in z nor a polynomial in
   z^{-1} has some positive power with nonzero constant term." Applied to g=R^B:
   0 ∉ Newt(R), i.e. every face is weight-one-signed. Lemma 8 (plane convex
   geometry): if wt took both signs on S, a counterclockwise boundary walk of
   conv(S) finds an edge E where wt transitions sign; its inward normal isolates E
   as an exposed face with λ/(c+d) = t ≥ 0 (the diagonal-crossing parameter) on
   which wt vanishes or changes sign — contradicting move 3–5's conclusion on that
   same face. Hence global strict one-sidedness. (A separate Step 2 kills the pure
   weight-zero part via the known one-variable factorial/GMC(1) case.)

**Why it dies for n ≥ 3 (Remark 9).** Three independent breaks: (i) the face
compression R lives in r = n−1 ≥ 2 variables and "0 ∉ Newt(R) is strictly weaker
than one-sidedness"; (ii) "Lemma 8 is a statement about plane convex geometry with
no analogue in R^r for r ≥ 2" (no boundary walk); (iii) the weight-zero part needs
the multivariate Factorial Conjecture, "unavailable" — and indeed Long's explicit
P₄ (six monomials, arXiv:2607.18186) refutes GMC(n≥3). So the theorem is genuinely
a *two-variable / one-dimensional-face* phenomenon: every tool in the chain (DvdK,
boundary walk, factorial case) is dimension-1-of-faces specific. This is the same
"dim 2 is the last survivor" pattern as JC2 itself.

**Slogan.** A single scalar identity E(P^m)=0, evaluated along the arithmetic
progression m=qp, carries a p-adic filtration whose graded-top piece is ONE face of
the Newton polygon; the face inherits its own one-variable moment problem, which is
rigid (DvdK); plane convexity then propagates face rigidity to global support
rigidity.

## 2. The dictionary (moment world <-> bracket world)

| # | Moment world (Wilson / GMC(2)) | Bracket world (Keller pair / JC2) | Status |
|---|---|---|---|
| D1 | Single P; hypothesis E(P^m)=0 for ALL m≥1 (infinite scalar tower) | Pair (P,Q); hypothesis [P,Q]=1 (or x^k reduced): ONE bilinear identity = finite array of coefficient equations | **Deep disanalogy**: no intrinsic infinite tower per face; [P^m,Q]=mP^{m−1}[P,Q] is derivation-trivial, so powers buy nothing for free |
| D2 | Functional E, E(Z^aW^b)=δ_ab·a!: diagonal pairing between Z- and W-sides, factorial weights | coeff_γ∘[·,·]: pairing det(p,q)·a_p·b_q between supp(P) and supp(Q), symplectic weights; dies exactly on collinear pairs p∥q | Solid analogy: both are rank-degeneracy-weighted bilinear pairings; "diagonal a=b" ↔ "collinear p∥q" as the kernel locus |
| D3 | Weight wt=a−b; E kills wt≠0 | (ρ,σ)-gradings; constancy of [P,Q] kills every stratum of ℓ-degree > 0 | Solid |
| D4 | Multinomial strata k of E(P^m); mixing of faces inside one scalar; must be UNMIXED by p-adics (Lemma 7) | Bracket coefficient array is ALREADY graded by lattice position: the top ℓ-stratum involves only face(ℓ,P)×face(ℓ,Q). Isolation is free | **Key asymmetry**: Lemma 7's conclusion ports to the classical fact [ℓP,ℓQ]=0 (Abhyankar/GGV starting point). The port of "isolation" per se yields nothing new at leading order |
| D5 | Face compression: R(z)=Σ_{α∈F}c_α z^{wt(α)}, one-variable Laurent | Edge form ℓ_E(P)=x^{i₀}y^{j₀}·f(T), T the edge parameter — one-variable | Solid; both exploit dim-2 ⇒ faces are 1-dimensional |
| D6 | Face rigidity input: DvdK — CT(R^q)=0 ∀q ⇒ 0∉Newt(R) ⇒ one-sided | Edge rigidity inputs: [ℓP,ℓQ]=0 ⇒ ℓP,ℓQ powers of a common form h; carrying edge: Wronskian eq u·fg′−v·f′g=cT^s, solution set rigid/classifiable (= Suzuki's 5 dessin classes for the (8,28) top edge) | Analogy real at the "one-variable rigidity theorem" level, but the theorems are different animals: DvdK is an infinite-tower statement; the edge Wronskian is a single ODE |
| D7 | Global propagation: Lemma 8 boundary walk of conv(S) finds a sign-transition edge; face conclusion forbids it | GGV/Abhyankar (ρ,σ)-direction sweep: face relations at every direction force polygon similarity N(P)∼N(Q), corners at origin, cone confinement | Solid — and already classical in the bracket world; both are "planar convex geometry with no r≥2 analogue" |
| D8 | Arithmetic lever: m=qp, good primes (G1–G4), Kummer carries, v_p separates pure face (=R₀) from mixed (≥R₀+1); Frobenius CT((R̄^q)^p)=(CT R̄^q)^p | **No classical counterpart in JC2 polygon analysis.** Nearest structures: (a) unit-pivot graded elimination killing sub-vertex strata (LEMMA.md's chain — an exact-arithmetic analog of "mixed strata have higher valuation"); (b) char-p Keller structure: [A^p,B]≡0, P̄^p central, Cartier operator, BKK/Tsuchimoto Frobenius bridge (JC⟺DC) | **The genuinely portable novelty lives here**; see TL1, TL2 |
| D9 | Endgame: strict one-sidedness of supp(P) wrt wt ⇒ GMC(2) by degree bookkeeping (Lemma 3) | Endgame sought: polygon/support exclusions per (ρ,σ)-cell ⇒ degree bound (our campaign); or cone confinement ⇒ automorphism (Abhyankar–Moh shape) | Same proof architecture: support theorem first, analytic conclusion second |
| D10 | Failure mode n≥3: faces are r≥2-dimensional, DvdK unavailable, no boundary walk, Factorial Conjecture open; Long's P₄ counterexample | Failure mode n≥3: Alpöge/Gao mechanisms; every dim-2 analog proved (Shaska equivariant, GMC(2)) | The "dim 2 = 1-dim faces + planar walk" survival pattern is the SAME phenomenon in both worlds |

**Honest gaps in the dictionary.** (i) D1: Wilson consumes infinitely many scalar
identities; a Keller pair supplies finitely many per polygon — any port must
manufacture an infinite family (powers with p-adic descent, prime variation, or
direction sweep). (ii) D6: no bracket-world statement currently has DvdK's shape
("CT of all powers vanish ⇒ support one-sided"); the edge Wronskian is first-order
information. (iii) D8(b) is structurally attractive (Frobenius rescales the Newton
polygon by p, so char-p identities couple faces at p-separated positions =
candidate NON-ADJACENT face interactions) but nothing is proved.

## 3. Candidate transfer lemmas (stated precisely; unproven unless noted)

**TL1 (Polygonal surplus criterion — level filtration as valuation).**
Setting: reduced Keller-type pair over K, [P,Q]=x^k; N(P),N(Q) lattice strips of
widths w_P,w_Q along a common primitive direction d=(d₁,d₂), top edges through the
origin; bottom corners p₀,q₀ saturated; LEMMA.md hypotheses (i) vertex
normalization (x^k at the Minkowski vertex p₀+q₀, unique unimodular decomposition,
vertex equation a_{p₀}b_{q₀}=±1) and (ii) symmetrized gap max((p₀)_x,(q₀)_x) ≥ 2.
Let Λ be the level function ℓ_Λ(i,j)=⟨d^⊥,(i,j)⟩ ordering the strips, and filter
the bracket-coefficient array by Λ (the bracket-world v_p). Claim: the near-origin
block (Q-columns (q₀)_x..(q₀)_x+1, P-columns 1..2) satisfies
#\{vanishing bracket keys\} − #\{eliminable unknowns\} = 1, with the surplus key at
the block's top Λ-stratum, and back-substitution along Λ-graded unit pivots (pivot
constants = lattice determinants det(corner, ·) ≠ 0) expresses the surplus as
(unit)·M·b_{q₀}, M a monomial in non-unit P-coefficients — contradicting (i) on
the chart M≠0. I.e. LEMMA.md condition (iii) is a THEOREM given (i)+(ii)+strip
widths, by Wilson-style counting (pure stratum at valuation R₀ ↔ vertex path;
mixed strata ≥ R₀+1 ↔ higher-Λ keys killed by unit pivots), with no elimination
run needed. Evidence: c2 chain replay (10 events, all pivots unit·det, final
constant −1 — re-verified today, §4); short-strip toy reproduces the identical
collapse (LEMMA-REVIEW). This is the most promising port: it converts our
computed kill into a polygon-data lemma of exactly Wilson's counting shape.

**TL2 (Frobenius/Cartier non-adjacent face congruences — the p-lever).**
Setting: Keller pair over O_K, good prime p (unramified, coefficients p-integral,
p ∤ pivot constants). Mod p: [P̄,Q̄]=1 still; Frobenius makes P̄^p, Q̄^p central
for the Poisson structure ([A^p,B]≡0), and dP̄∧dQ̄=dx∧dy gives, via the Cartier
operator C on 1-forms (C(f^{p−1}df)=df, C kills exact forms), the identity
C(P̄^{p−1}Q̄^a dP̄) ≡ (Cartier descent of Q̄^a) for each a. Claim (candidate): the
resulting coefficient congruences relate the face data of N(P) at position γ to
data at p·γ + O(1) — Frobenius scales the polygon by p — yielding congruence
constraints between NON-ADJACENT faces/strata that are invisible to any single
(ρ,σ)-grading; running over infinitely many p manufactures the missing infinite
tower (dictionary gap D1) and lifts to char 0. Status: mechanism-level only; the
precise coefficient identity to extract is the (1/p)-normalized part of
[P^p,Q]=pP^{p−1} (a Buium-style p-derivation of the Keller relation). Related
deep precedent: Tsuchimoto/Belov-Kanel–Kontsevich char-p Azumaya bridge (JC⟺DC)
— evidence that Frobenius sees Keller structure; nothing face-local exists in
the literature we know. High risk, high novelty.

**TL3 (Carrying-edge DvdK — two-polynomial constant-term rigidity).**
Setting: direction d with the ℓ-degree drop failing (the carrying face, where the
rhs x^k lives). Edge forms ℓP=x^{i₀}y^{j₀}f(T), ℓQ=x^{i₁}y^{j₁}g(T) satisfy the
Wronskian edge equation u·fg′−v·f′g = c·T^s. Depth-r strata of [P,Q]=x^k along d
give a finite tower Σ_{i+j=r}[P_i,Q_j]=δ_{r,r₀}x^k, r ≤ w_P+w_Q. Claim
(candidate): the full tower is equivalent to the vanishing of the constant terms
CT(f^{−v/e}g^{u/e}·h_r(T)) of an explicit finite family of Laurent expressions in
the edge data (e=gcd(u,v)), and a DvdK-type rigidity statement — "if all these CTs
vanish then the pair (f,g) is a dessin-rigid pair: f,g are, up to common factor
and reparametrization, powers of a single h with prescribed ramification" — would
subsume and re-derive Suzuki's 5-class top-edge classification for (8,28) from
first principles, and export it to every cell of the (75,125) frontier. Status:
the tower and the edge equation are classical; the CT-reformulation and the
rigidity statement are conjectural; the finiteness of the tower (vs Wilson's
infinite m) is the honest obstruction — expect classification, not vanishing.

## 4. Worked toy examples (both sides, run 2026-08-04)

**Moment side — Lemma 7 mechanics verified exactly** (`cases/toy_face_isolation.py`,
new, runs in ms). P = Z²W + ZW² + t·Z⁵; face F = {(2,1),(1,2)} for ℓ=a+b, R = z+z⁻¹
(mixed sign), λ/(c+d)=3/2, B=2, q=2, good prime p=7 (>R₀=3), m=qp=14. Balanced
strata: k=(7,7,0) pure-face, (4,9,1), (1,11,2) mixed. Results:
pure-face total = 175344113533306798080000 = (pR₀)!·CT(R¹⁴) EXACTLY (identity
verified to the integer); v₇(pure) = 3 = R₀; v₇(mixed) = 4 ≥ R₀+1 — the p-adic
separation is real. Contrast with bad prime p=3 (violates G4: p ≤ R₀): the
normalization fails (v₃(pure-face) = 4 ≠ R₀ = 3), showing why G4 is needed for the
clean count. And E(P²)=12 ≠ 0 t-free: no coefficient choice rescues a mixed-sign
face, which is the theorem's content in miniature.

**Bracket side — the isolation instance we already own** (`cases/eq3_chain.py
open_8_28_c2`, re-run today, 8 s): cascade 3 zeroings + 41 unit-pivot
eliminations, all pivot constants nonzero lattice determinants
{−8,−6,−4,−2,2,3,...,22}; the surplus equation (original key (3,6)) is touched by
exactly 10 events and collapses to (−1/5)·a2²·a6·ia1²·b3; vertex equation then
reads −1. Read through the dictionary: the vertex stratum is the "pure-face term"
(valuation R₀), the gap/sub-vertex strata are the "mixed terms" (killed = higher
valuation), and the surplus back-substitution is the Frobenius/CT extraction. The
Λ-level filtration plays v_p. This is a completed bracket-world face-isolation
argument in the wild — which is what makes TL1 credible.

## 5. Verdict

**Partially real port — not superficial, but not a royal road.** The two proofs
share a genuine architecture unique to dimension 2: compress a 1-dimensional face
to a one-variable object (D5), apply a one-variable rigidity theorem (D6), and
propagate around the polygon by planar convexity (D7). JC2's classical theory
ALREADY occupies all three slots (leading-form commutation, edge Wronskian/dessin
rigidity, GGV direction sweep) — so naively porting Wilson reproves known facts:
his Lemma 7, transported, IS [ℓP,ℓQ]=0. The two genuinely new transferables are:

1. **The counting discipline (TL1)** — Wilson's "pure stratum has valuation exactly
   R₀, mixed strata ≥ R₀+1" is precisely the missing derivation of LEMMA.md's
   surplus condition (iii) from polygon data, with the Λ-level filtration playing
   v_p and unit lattice-determinant pivots playing good-prime integrality. This is
   concrete, evidenced on two families plus a toy, and directly serves the
   campaign (polygonal kill criterion for gap ≥ 2 cells, no F4 needed).

2. **The arithmetic lever (TL2)** — the m=qp / Frobenius trick has NO classical
   JC2 counterpart (D8); its bracket-world shadow (char-p centrality of P̄^p,
   Cartier operator, p-scaled polygon self-interaction) is the only candidate
   mechanism on the table for constraints between NON-ADJACENT faces. Speculative.

The deepest disanalogy (D1) is honest and load-bearing: Wilson consumes an
infinite tower E(P^m)=0 that the single bilinear Keller identity does not supply;
any port must manufacture infinity (prime variation, as in TL2) or settle for
finite-block counting (TL1). Second-order face interactions exist and are exactly
our vertex-gap collapse; constraints on non-adjacent faces remain unproven in both
worlds' vocabularies. Recommended next step: prove TL1 (O(1)-sized block, explicit
determinants — a bounded, paper-grade task flagged already in LEMMA.md §5), and
only then spend time on TL2.

## Erratum (2026-08-05): TL1's general claim is falsified outside the
(k,d2)=(2,2) regime (SURPLUS-REVIEW.md front 5: TRIVIAL at (3,2), surplus 4-6
at d2>=3). TL1 agrees with SURPLUS.md on all shared test families and is
superseded by SURPLUS.md's scoped theorem + scope map.
