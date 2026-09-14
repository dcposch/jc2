# Uniform full-characteristic Keller criterion: recovery gate

**Verdict: CONFIRMED, with two hypothesis repairs made explicit.** The charged auxiliary theorem is a correct, purely algebraic reverse criterion, uniform in the tower length s and in every degree n: (A) the composed U-derivative of each T_i has exact total degree D_i+M_i; (B) a nonzero J(F,G) has total degree at most n−M_s−2; (C) at the endpoint M_s=n−2 it is a nonzero constant; (D) gcd(n,D_1,…,D_s)=gcd(d_s,2), so the final gcd is 1 or 2 and both parities occur; (E) an unequal two-line top of F excludes J=0 through Arzhantsev–Petravchuk Lemmas 4–5. The repairs: the exponents n_i must be declared as the characteristic quotients d_i/d_{i+1}, after which the appendix's "additional" gcd identity is a consequence rather than an assumption; and every attained degree must be a **total** degree. With y-degree attainment and scalar leaders alone the same proof gives only J(F,G)∈k[x], which is exactly where Moh's J=x^l family lives. The printed necessity is **CONFIRMED at its printed, Keller-assumed, all-degree scope**. No finite census enters either direction and none is asserted to be an all-degree exclusion. No exit price is claimed, so no `charge_basis` line applies.

**1. Custody.** Receipt `xmodel/full-characteristic-uniform-gate-fable5-20260906.run.v2`, basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. I paired the receipt's `charged_input_<i>_basename` and `_sha256` fields into [inputs.sha256](../box/full-characteristic-uniform-gate-20260906/inputs.sha256) and ran `sha256sum -c` inside `/tmp/jc2-lane.Izlo4z/inputs`: **6/6 OK** ([hash-check.txt](../box/full-characteristic-uniform-gate-20260906/hash-check.txt)). Moh pages were rendered from the frozen PDF and read as images (printed page = PDF ordinal + 139); the page-by-page reading is [source-notes.md](../box/full-characteristic-uniform-gate-20260906/source-notes.md). The Arzhantsev–Petravchuk paper was re-fetched from arXiv (math/0608157v2); its SHA-256 `70429c3820eede008640a0d462d67ddb1f32c1f6e37f6b35f3589a0be2081e28` equals the copy retained at `box/char-degree-20260905/arzhantsev-petravchuk-closed-polynomials.pdf`, so the duplicate was not kept; the Lemma 4–5 text is [excerpted](../box/full-characteristic-uniform-gate-20260906/ap-lemmas-4-5-excerpt.txt). Lemma 4 is cited there to [7, Ch. 3, Th. III] and [18, Cor. 2], not proved; Lemma 5 is proved on p5 from Proposition 1 (p3). Desk controls are [controls.py](../box/full-characteristic-uniform-gate-20260906/controls.py) with output [controls.out](../box/full-characteristic-uniform-gate-20260906/controls.out); sympy degree checks only. No ledger, `jc2-lean`, `ideation-*`, launcher or adapter file was touched.

**2. The theorem with exact hypotheses.** Write J(F,G)=F_xG_y−F_yG_x and use Moh's order (f,g)=(G,F): U↔G, V↔F, n=deg F.

- (H0) k a field of characteristic 0; F,G∈k[x,y] nonconstant.
- (H1) T_1=U+P(V) with P∈k[V], so ∂_U T_1=1.
- (H2) T_{i+1}=T_i^{n_i}+Σ c_{j,α} V^j ∏_{l≤i} T_l^{α_l}, scalar c_{j,α}∈k, integers n_i≥1. For every nonzero c_{j,α} the weight W=jn+Σ_l α_l D_l satisfies W≤n_iD_i, and W=n_iD_i forces α_i=0.
- (H3) H_i:=T_i(G,F) has **actual total degree** D_i (nonzero leading form). Put M_1:=−D_1 and M_{i+1}:=n_iD_i+M_i−D_{i+1}; require M_1<M_2<…<M_s.

Then for i=1,…,s the polynomial (∂_U T_i)(G,F) is nonzero of total degree D_i+M_i. (1)

The "at most one equality summand" clause and the restrictions 0≤α_l<n_l are not used by (1); they only identify the T_i with Moh's approximate roots. Strict increase of M is equivalent to D_{i+1}<n_iD_i, i.e. the top of T_i^{n_i} cancels at every step. Nothing in (H0)–(H3) mentions Keller, realizability, Puiseux data, or algebraic closure; the statement holds at every point of any coefficient chart on which (H1)–(H3) are imposed, and the induction has no bound on s or n.

**3. Audit of (1)–(3).** Base: ∂_U T_1=1, degree 0=D_1+M_1. Step: differentiate (H2) in U with V fixed,

\[
\partial_U T_{i+1}=n_iT_i^{n_i-1}\partial_UT_i+\sum c_{j,\alpha}V^j\sum_l \alpha_l T_l^{\alpha_l-1}(\partial_UT_l)\prod_{l'\ne l}T_{l'}^{\alpha_{l'}} .
\]

Composed, the first term is a product of nonzero polynomials (char 0 gives n_i≠0 in k) of degree (n_i−1)D_i+D_i+M_i=n_iD_i+M_i. The summand differentiated at factor l has degree at most W−D_l+(D_l+M_l)=W+M_l by strong induction. If W<n_iD_i then W+M_l≤n_iD_i−1+M_i. If W=n_iD_i then α_i=0, so l<i and M_l<M_i. Both are strictly below n_iD_i+M_i, so the leading form of the first term survives, and n_iD_i+M_i=D_{i+1}+M_{i+1} by (H3). This is Moh's Prop 3.2(3), p159, whose proof on p160–161 makes the same two-case split (M_i<M_r in the equality case) in y-degree; Moh's subscript f is defined on p155 as ∂/∂f, so the prime-label check passes.

(2) With scalar coefficients, ∂_x[T_s(G,F)]=(∂_UT_s)G_x+(∂_VT_s)F_x and likewise in y; the ∂_V terms cancel, giving J(F,H_s)=(∂_UT_s)(G,F)·J(F,G) (Moh p155 for H∈k[f,g]). In total degree, deg J(F,H_s)≤(n−1)+(D_s−1). If J(F,G)≠0, degree additivity and (1) give

\[
\deg J(F,G)\le n+D_s-2-(D_s+M_s)=n-M_s-2 .\tag{2}
\]

(3) If some index has M_i=n−2, (2) at that index gives deg J(F,G)≤0: J(F,G) is zero or a nonzero constant. Consistency: a further scalar level at M=n−1 with actual degree D would force deg J≤−1, hence J=0; Moh's Prop 2.2(3) says precisely that at M_r=e=n−1 the leader is cf_e(x)y^{−μ_r} with deg_x f_e=1, so the total degree is D+1 and the bound returns 0.

Why total degree is essential. Running §3 in y-degrees (Moh's Prop 3.2 verbatim) with scalar leaders on F and H_s gives deg_y F_x≤n−1 and deg_y ∂_xH_s≤D_s−1, hence deg_y J(F,G)≤n−M_s−2=0: J(F,G)∈k[x], not k. A chart imposing only Prop 2.2 rows (y-degree D_i, scalar leader) cannot force constancy; the total-degree block is what separates l=0 from Moh's J=x^l family (Remarks p169, p171). Scalar target coefficients are essential for the chain rule: an x-dependent c would add (∂_xT_s)(G,F)·F_y to J(F,H_s) and raise the weights in (H2).

**4. gcd arithmetic and zero exclusion.** Take d_1=n, d_{i+1}=gcd(d_i,M_i), n_i=d_i/d_{i+1}, q_1=M_1, q_i=M_i−M_{i−1}, λ_i=Σ_{j≤i}q_jd_j, D_i=−λ_i/d_i (Moh p150). Telescoping the q's gives λ_i=Σ_{j<i}(d_j−d_{j+1})M_j+d_iM_i, the p154 recovery formula solved for λ. Since d_i divides d_j and d_{j+1} for j<i, D_i≡−M_i (mod d_i); D_i is an integer and D_{i+1}=n_iD_i+M_i−M_{i+1} because μ_{i+1}=n_iμ_i+q_{i+1}. Induction: gcd(n,D_1)=gcd(n,M_1)=d_2 and gcd(d_i,D_i)=gcd(d_i,M_i)=d_{i+1}, so gcd(n,D_1,…,D_i)=d_{i+1}, which is Moh's p154 statement gcd{n,μ}=gcd{n,M}. Only the definitions are used, so the gcd identity is a consequence once n_i=d_i/d_{i+1} is declared, and the abstract D_i of (H3) coincide with −μ_i because both obey the same recurrence from D_1=−M_1. At M_s=n−2, d_s|n gives d_{s+1}=gcd(d_s,2): **1 when d_s is odd, 2 when d_s is even**. The strict-drop rule d_{s+1}<d_s then needs d_s even and at least 4, and the tower continues with a non-effective terminal M_{s+1}=n−1 (p174).

Zero exclusion. Suppose J(F,G)=0. AP Lemma 4 (char 0) makes F,G algebraically dependent; Lemma 5 (any field) gives H∈k[x,y]∖k with F,G∈k[H], hence every H_i∈k[H]. With k_0=deg H, k_0 divides n and every D_i (D_i=0 trivially), so k_0 | gcd(d_s,2). Also F=f(H) has leading form c·(H_top)^{n/k_0}. If k_0=1, F_top is a power of one linear form. If k_0=2, H_top is L² or L_1L_2, so F_top is cL^n or c(L_1L_2)^{n/2}, two lines of equal multiplicity n/2. Hence a top of F with two distinct linear factors of unequal multiplicity excludes J=0; for odd d_s two distinct factors already suffice. The appendix's k_0 argument is correct, and deg F=deg_y F is not needed for it (k_0 is the total degree of H). Combined with (3): under (H0)–(H3), n_i=d_i/d_{i+1}, M_s=n−2 and such a top, J(F,G)∈k^×.

**5. Printed necessity: source interfaces.** Every item assumes Moh's setup: k algebraically closed of characteristic 0, f,g monic in y, deg_y f=m, deg_y g=n, J_{x,y}(f,g)=1 or a nonzero constant. Lemma 2.1's note (p151) derives y∈k(x,f,g) from the Jacobian condition, so the p150 supposition is not extra. Every item is an all-degree statement.

| Interface | Printed source (read as image) | Verdict |
|---|---|---|
| Arithmetic d,M,n_j,q,λ,μ and D_i=−μ_i | p150 definitions; p154 gcd identity and recovery formula | CONFIRMED, re-derived in §4 |
| e=n−1, deg_x f_{n−1}=1 | Lemma 2.1 p151, printed as an **iff** with J=c≠0 | CONFIRMED; all M_i≤n−1 |
| Exact y-degree −μ_r and scalar leader | Prop 2.2(1),(2) p152, proof p153–154 ("monic means unit"); case (3) M_r=e has leader cf_e(x)y^{−μ_r} | CONFIRMED; y-degree only |
| Scalar recurrence, weights, equality summand with α_r=0 | Prop 3.1 p157 with (5),(6) p155; proof p158–159; Remark p159 "remains valid after ψ" | CONFIRMED; y-degree weights |
| Derivative degree θ_{r+1}=−μ_{r+1}+M_{r+1} | Prop 3.2(1)–(3) p159, proof p160–161; Remark p161 specialization for M_{r+1}≤e; chain rule p155 | CONFIRMED; equals (1) in y-degree |
| Two-point top forces some M_i=n−2 | Prop 4.3 p166 (deg g=deg_y g=n>1), contrapositive; proof uses Prop 4.2 | CONFIRMED, Keller-assumed |
| Common top of g and T_i (i<r), ≤2 lines, unequal multiplicities | Prop 4.5 p169, proof p172 via Prop 4.6 with λ=−1, v=d_r, deg q=2 | CONFIRMED, Keller-assumed |
| Total degree = y-degree of T_i^ψ(f,g) for all i≤r | p172: δ=min root order of g∏_{i≤r}T_i^ψ is −1; Prop 4.6(2) at λ=−1 reads ord T_i^ψ(σ)=μ_i, i.e. total degree −μ_i, "trivial to verify" | CONFIRMED for i≤r including r; Keller-assumed |
| Effective list drops M_h=n−1 | p174 Definition–Remark | CONFIRMED |

Interface to (H3): Prop 2.2 gives y-degree attainment with scalar leader at every effective index, and the p172 argument lifts it to total degree for i≤r when M_r=n−2. Interface to (H2): Prop 3.1's weights are y-degrees, equal to the total-degree weights of (H2) by the previous line. So every Keller pair with a two-point top and effective datum (M_1,…,M_s), M_s=n−2, lies on the chart cut out by (H1)–(H3) with scalar T_i, and every point of that chart with the unequal top is a Keller pair. The equivalence is per datum. For (99,66), d_3=11 is prime and 11∤M_3∈[78,97], so a two-point top forces M=(−66,77,97). For (108,72), d_3=9 also admits towers (−72,81,M_3,106) with M_3∈{84,87,93,96,102}, so the D108 equivalence is for its own row only. That M_s=n−2 holds for every minimal counterexample rests on the promoted Prop 5.4/First-Separation reduction, inherited and not re-audited here.

**6. Controls.** Clients: (99; −66,77,97): d=(99,33,11,1), n_i=(3,3,11), Λ=(−6534,−1815,−1595), D=(66,55,145), gcd chain (99,33,11,1), bounds n−M_i−2=(163,20,0). (108; −72,81,106): d=(108,36,9,1), n_i=(3,4,9), Λ=(−7776,−2268,−2043), D=(72,63,227), chain (108,36,9,1), bounds (178,25,0). The recurrence D_{i+1}=n_iD_i+M_i−M_{i+1} holds at every step. Even final gcd: n=20, M=(−12,18): d=(20,4,2), D=(12,30), gcd(20,12,30)=2=gcd(d_2,2); likewise (12; −8,10) and (24; −16,22). The datum (8; −6,6) is rejected since d_2=2 divides M_2. Dropped endpoint: G=y²+x, F=G²−x³ (n=4, m=2), T_2=U²−V, H_2=x³ of total degree 3 and y-degree 0; n_1=2, M=(−2,−1), D=(2,3); J(F,G)=−6x²y in the convention above (J(G,F)=+6x²y), of degree 3=n−M_2−2, saturating (2); (∂_UT_2)(G,F)=2G has degree 2=D_2+M_2, and the chain-rule identity checks exactly. This point lies outside Moh's setup (G²−F=x³, so y∉k(x,F,G)) and controls the abstract theorem only. Dropped unequal top: F=(xy)², G=xy, J=0, gcd(4,2)=2, top x²y² with equal multiplicities: a control for the k_0=2 branch of §4, not an endpoint tower.

**7. Cheapest usable consequences.** (a) On any chart carrying a scalar T_2 of Prop 3.1 form with actual total degree D_2 and scalar leader, every Jacobian coefficient of total degree above n−M_2−2 (20 for (99,66), 25 for D108) vanishes identically; those quadratic rows may be adjoined as free redundant helpers and can never kill (r2 §4 already noted this). (b) On the T_2 chart with the placed unequal two-line tops, the last level is an exact equivalence: "there is a scalar T_3 in the Prop 3.1 family (nine monomials at (99,66)) with actual total degree 145/227" ⟺ "J(F,G)∈k^×". The left side costs about 3,100 total-degree cancellation rows of degree 9 in the chart coordinates; the right side is the roughly 230/350 quadratic Jacobian rows of total degree 1 to 20/25 plus J_0≠0. A compiler should not build the last attainment block; the full characteristic chart is the Keller locus for its datum, a proper full chart proves a counterexample with that datum exists, and no leaf kill is cheaper through it than through the Jacobian rows. (c) No zero-Jacobian exclusion at T_2 level follows from the top form alone: gcd(n,m,D_2)=11/9, y²⁷(y−x)⁷² is a ninth power and y²⁴(y−x)⁸⁴ a twelfth power, so r2's Theorem B with the D2 face covers remains the operative T_2-level exclusion.

**8. Limits and FALLACY check.** The theorem decides no existence question; it re-expresses Keller on a per-datum chart. Its necessity half is Keller-assumed and printed for all n; no finite census is an all-degree exclusion and none is claimed. One-point tops with M_s=n−2, if realizable, are not covered by the §4 exclusion. Total-degree rows are necessary only through p172, i.e. only for realized Keller data; on a y-degree-only chart the conclusion weakens to J∈k[x]. Prop 4.5's common-top statement is for i<r; the i=r total-degree fact comes from its proof, not its statement. Field: (1)–(3) need only characteristic 0; §4 uses AP Lemma 4 (char 0) and linear factors over the algebraic closure. FALLACY-v2: prime label defined (p155); variable map declared (U↔G, V↔F, sign of J); floor and attainment separated (actual degrees are hypotheses, never inferred from bounds); no exit claim, hence no `charge_basis` line; no `sat()`, remainder or ring-map computation was run.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14218`.
- Body SHA-256:
  `650ec46c880f4b1eafa55fa274361ce5cdb0a921c1428d5a1cbde2221772551c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
