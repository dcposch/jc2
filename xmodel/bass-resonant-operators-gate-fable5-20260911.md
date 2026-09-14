# Gate (Fable 5.1): bass-resonant-operators-astra-20260911

Tag: bass-resonant-operators-gate-fable5-20260911. Reviewer: Fable 5.1, independent different-model hostile gate. Started 2026-09-11 21:23 UTC; HARD 21:39 UTC. Documentary reads only: the charged report whole, Bass 1989 printed 41--42 and 49 (PDF 4--5, 12), van den Essen 1993 printed 373--378 whole, via pdftotext to stdout. No code, CAS, web, git, other reports or live artifacts.

## Pre-pins (sha256, /tmp/jc2-lane.TZNubZ/inputs, hashed before reading; all three match expected)

- bass-resonant-operators-astra-20260911.md c179106b8dabb3eeb20a0757e75faf952d0d6f42511fc90f2450126b11ef58b7
- bass-1989.pdf 86f642941d2cea0f1d438996d8e81833ac53b6039c4c81e1564adc411f614b1e
- vandenessen-1993.pdf 07f29ddee54e89cfc38b5b228518347799995c06ad359b952eb952f511253db4

## Summary

A CONFIRMED. B CONFIRMED. C CONFIRMED. D CONFIRMED under two stated standard facts and one normalization caveat. E CONFIRMED with van den Essen's external ingredients declared. No refutation found; no blocking GAP. Not re-proved: two classical one-variable analytic facts (F1, F2) and the imported commutative algebra behind van den Essen's Thm 4.1.

## A. Mixed resonant family: CONFIRMED

Shear sign. On degree d, L_d = a e_p - b e_q + g(d) delta is a derivation of the degree-d piece (g(d) is a scalar; e and delta commute since delta is homogeneous of degree 0). L_d p = a p; L_d q = -b q + g(d) p; for u = q - h p, L_d u = -b q + (g(d) - a h) p, which equals -b u iff h = g(d)/(a+b). So u_d = q - g(d)p/m with the MINUS sign. (p, u_d) is an invertible linear change, so {p^i u_d^j} is a basis with eigenvalue a i - b j - c, consecutive i differing by m; the degree-d kernel has dimension at most one.

Exhaustion. Integer solutions of a i - b j = c are (i_0 + b n, j_0 + a n), n in Z; with a, b > 0 both coordinates grow with n, so the nonnegative ones are exactly {n >= n_min}: a unique first (r, s) and the family (r + b n, s + a n). Phi preserves total degree, so Phi f = 0 iff each homogeneous piece dies, and the kernel is exactly the formally convergent sums (1) with unique arbitrary c_n.

Lowest weight with one negative weight. With wt(p)=a, wt(q)=-b, the k-th binomial term of summand n has weight c + m k, so weights of f are >= c and the weight-c part is p^r q^s B(p^b q^a), nonzero once some c_n is. Ring check: for series with weights bounded below, the weight components f^{(w)} are well-defined elements of C[[p,q]] (possibly infinite series because q has negative weight), (fg)^{(w)} = sum_{w1+w2=w} f^{(w1)} g^{(w2)} holds coefficientwise with finite sums, and f -> sum_w tau^w f^{(w)} is a ring homomorphism from that subring into C[[p,q]]((tau)). Polynomials lie in the subring, so H(tau^a p, tau^{-b} q, f_tau) = 0 there; the monomial p^i q^j T^k contributes tau^{a i - b j + c k}(p^i q^j f_0^k + O(tau)), so the tau^mu coefficient is H_mu(p,q,f_0), and H_mu != 0 as a nonempty sub-sum of H's monomials. A nonzero initial relation survives. Confirmed.

p = lambda. f_0 is in C[p][[q]] (the q^j coefficient is a single monomial or zero, using a > 0); evaluation p = lambda is a coefficientwise ring homomorphism C[p][[q]] -> C[[q]]; H_mu in C[q,T][p] vanishes identically at finitely many lambda only. Excluding those and 0 gives a nonzero relation for lambda^r q^s B(lambda^b q^a) over C(q); dividing in the fraction field, B(lambda^b q^a) is algebraic over C(q), hence over C(t), t = lambda^b q^a, and C[[q^a]] = C[[t]] transports the relation to B(t). Confirmed; no arbitrary-point substitution of a two-variable series is used.

q = 0. Write H = q^k H' with q not dividing H'; H'(p,q,f) = 0 in the domain C[[p,q]] and H'(p,0,T) != 0, so f(p,0) is algebraic over C(p). Evaluation at q = 0 is (p,q)-adically continuous and commutes with the sum (1); the p^{d_n} coefficient is c_n(-h_n)^{s+an}, no cancellation since the d_n are distinct. Confirmed.

Coefficient bound. (F1), external standard, declared not re-proved: a one-variable formal series algebraic over C(p) has positive radius of convergence (Bass p.49 uses it implicitly via "cercle de convergence"). Then |c_n| |h_n|^{s+an} <= M rho^{-d_n} whenever h_n != 0. h_n = g(r+s+mn)/m is a degree-k polynomial in n, k >= 1, so |h_n| >= K n^k eventually and |c_n|^{1/n} <= M^{1/n} rho^{-m-(r+s)/n}(K n^k)^{-a-s/n} -> 0. Finitely many zeros of g do not affect the radius. The exponent a >= 1 on the shear is what makes this work; a = 0 is excluded. So B is entire. Consistency: with constant g the same bound gives only a finite radius, matching C.

Entire algebraic is polynomial. (F2), cited by Bass p.49 as [B] Prop. (D.1); the report's sketch (root bound gives polynomial growth for |t| large, then Cauchy) is correct. Hence finitely many c_n and f polynomial. Verdict A: CONFIRMED modulo (F1), (F2).

## B. Endpoint e_p - r + delta g(e): CONFIRMED

On degree d, L = e_p + g(d) delta has L p = p, L q = g(d) p, so u = q - g(d) p has L u = 0 and p^i u^j has eigenvalue i. Kernel of L - r: zero for d < r, spanned by p^r(q - g(d)p)^{d-r} for d >= r, giving (4). Lowest p-order is r with coefficient B(q) = sum c_n q^n != 0; with wt(p)=1, wt(q)=0, wt(T)=r all weights are nonnegative, so the initial-form argument is the ordinary p-adic one, and the same p = lambda step gives B algebraic. At q = 0 the p^{r+n} coefficient is c_n(-g(r+n))^n; f(p,0) is algebraic by the q-factor argument; (F1) gives |c_n|^{1/n} <= M^{1/n} rho^{-1-r/n}/|g(r+n)| -> 0 away from finitely many zeros. B entire and algebraic, so polynomial by (F2), so f polynomial. Degeneracies: r = 0 literally covered (kernel starts at degree 0 with c_0); g(r) = 0 harmless because the n = 0 term is c_0 p^r with exponent 0 on g(r); no division by any c_n. Verdict B: CONFIRMED modulo (F1), (F2).

## C. Constant-g controls: CONFIRMED

With g = gamma, u = q - gamma p/m is a global linear coordinate and D = a e_p - b e_q + gamma delta is a derivation with D p = a p, D u = -b u; so D(p^b u^a) = 0, D(p^r u^s) = c p^r u^s, and every term of p^r u^s/(1 - p^b u^a) = sum p^{r+bn} u^{s+an} has eigenvalue c: Phi f = 0. The denominator has constant term 1, positive degree, and is coprime to p and u, so f is a nonpolynomial rational germ. At the endpoint D = e_p + gamma delta kills u = q - gamma p and p^r/(1-u) has eigenvalue r. Both confirmed.

Not actual-Keller counterexamples: under the embedding of D such an f would lie in C(F) \ C[F], impossible inside C[X] by Bass Cor. 1.3 (abstract form: Bass 1989 Lemma 2.1, p.42); independently van den Essen Thm 4.1 covers constant g for b > 0 (E). Hidden actual-source assumptions or global degree projections in A/B: none found. Both proofs live in C[[p,q]] with its intrinsic total-degree decomposition and never use a trace section, a global automorphism, nilpotence, or a Keller map.

## D. Composition corollary and embedding: CONFIRMED with stated assumptions

If Phi(f) = P is polynomial then Phi(f_d) = P_d = 0 for d > deg P, so f minus its finite low part is an algebraic kernel element, polynomial by A/B, so f is polynomial. This is Bass's p.41 remark that "phi f in A" may be replaced by "phi f = 0".

Actual Keller application: det JF in C*, normalized F(0) = 0. Caveat: if F(0) != 0 the statement is for the shifted coordinates p = F_1 - F_1(0), q = F_2 - F_2(0) and their Euler operators, not for F_1 partial_{F_1}; this is the translation van den Essen also performs. Stated external facts: (F3) formal inverse function theorem C[[X]] = C[[F]] (van den Essen p.375 cites it unproved); (F4) C(X)/C(F) is finite, so every element of R = C[X] is algebraic over C(p,q). The derivations partial/partial F_i on C[[F]] equal sum_j ((JF)^{-1})_{ji} partial/partial X_j with polynomial entries, so they preserve R and agree with the unique Keller extensions; Phi on R/A is the restriction of the formal operator. Hence Phi f in A, f in R, forces f in C[p,q] = A: Phi is injective on R/A. The projections f -> f_d are taken in C[[p,q]]; each f_d is in A but the infinite sum is not an R-internal object; the proof only subtracts the finite partial sum, which lies in A. Distinction respected. Verdict D: CONFIRMED modulo (F3), (F4), F(0) = 0.

## E. History and boundary: CONFIRMED

Source (van den Essen p.377, Thm 4.1, read from the PDF): F nice, F(0) = 0, x = F_1, y = F_2, P = sum_i (y partial_x)^i P_i(e_x, e_y) with P_0(e_x, r) != 0 for all r in N; then M = k[X]/k[F] has no P-torsion. Its delta is y partial_x; ours is p partial_q, so p = y, q = x: swap confirmed. Our Phi_0 becomes P_0(X,Y) = aY - bX - c and P_0(X, r) = ar - bX - c != 0 for every r because b > 0; delta g(e) = (y partial_x) P_1 with P_1 = g(X+Y). So after the generic nice normalization Thm 4.1 already excludes actual-Keller torsion for the whole mixed family, indeed for arbitrary P_i (i >= 1) and constant g. Not a new frontier; A's content is the larger category of arbitrary algebraic germs, where C shows constant g fails.

Endpoint: Phi_r gives P_0(X,Y) = Y - r, P_0(X, r) = 0: hypothesis fails at that r; Cor 4.2(i)'s role swap changes delta to x partial_y and does not apply. Not covered, as claimed.

Proof replay: m != 0, cap y^p M = 0, write m = y^r m', m' not in yM; P y^r = y^r P~ with P~ = sum (y partial_x)^i P_i(e_x, e_y + r); no y-torsion gives P~ m' = 0; P~ = P_0(e_x, r) + yQ since (y partial_x)^i in yA_2 for i >= 1 and P_0(e_x, e_y + r) - P_0(e_x, r) in e_y A_2 subset yA_2; so P_0(e_x, r) kills the nonzero class of m' in M/yM subset k[[x]]/k[x]. Prop 1.3 re-proved: P(x partial_x) x^n = P(n) x^n, so P(x partial_x) g in k[x] forces g_n = 0 beyond the roots and degree. Sound.

External ingredients NOT re-proved: Bass [3] Cor 1.3, k[X] cap k(F) = k[F] (Bass 1989 Lemma 2.1 p.42 is the abstract form; its proof and flatness of C[X] over C[F] are outside scope); faithful flatness k[X]_{(X)} -> k[[X]] (Prop 1.5); formal inverse function theorem (Prop 2.3); Bertini via Schinzel (Lemma 3.2), Krull intersection and primitive element (Lemma 3.3, Cor 3.4) for the nice normalization (Prop 3.1). The normalization replaces F by F^{(lambda)}, so the exclusion is for translated Euler operators, which suffices for the Jacobian Conjecture.

Boundary: nothing deduces that an arbitrary U-annihilator has the displayed form (PBW gives sum delta^i P_i(e_p,e_q) with arbitrary P_i, strictly larger than delta g(e)); no JC2 proof, counterexample, general U-torsion theorem or novelty claim is made or endorsed. Bass Thm 1.5 (p.42) excludes exactly the special-linear phi_0 case, which is both families here. No charge_basis line: no exit-price claim.

## Post-pins (sha256 of the three lane inputs, regenerated after the body was written)

- c179106b8dabb3eeb20a0757e75faf952d0d6f42511fc90f2450126b11ef58b7  bass-resonant-operators-astra-20260911.md
- 86f642941d2cea0f1d438996d8e81833ac53b6039c4c81e1564adc411f614b1e  bass-1989.pdf
- 07f29ddee54e89cfc38b5b228518347799995c06ad359b952eb952f511253db4  vandenessen-1993.pdf

Post-pins equal pre-pins (all three unchanged). Whole-report readback done at 21:30:56 UTC before this marker. No later edits; no Seal section (launcher owns custody).

<!-- BODY-END -->
