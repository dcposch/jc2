# Hostile gate: conditional late-contact Keller descent and direct leading-form obstruction (Fable 5.1, 2026-09-09)

Lane `/tmp/jc2-lane.I63H89`, frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d` (provenance only). Joint independent different-model review of the sealed descent report `keller-descent-proof.md` (source `xmodel/late-contact-keller-descent-astra-20260909.md`) and the root addendum `late-contact-direct-obstruction-coordinator-20260909.md`. PURE PROSE / MANUAL FACTORED REVIEW: no Python, CAS, checker, pair expansion, H/R power, source stream, network, agent, ledger edit or link-following. Every derivation below is my own hand computation on symbolic degrees, brackets and coefficients; the only executed commands were `sha256sum`, `head -c`, `cat`, `ls`, `date` and one `grep`/`diff` on metadata.

## 0. Pins and read scope

`sha256sum` on the twelve charged basenames was run BEFORE any mathematical body was read. Every digest equals its ROOT-PINS.json entry, its PINS.json entry (where listed) and its `charged-inputs.list` line. Table rows are generated from the tool output, not typed:

| basename | sha256 (charged bytes) | bytes |
|---|---|---|
| ROOT-PINS.json | `e9c36daaf1698eb4ad7f94ef390d905503a08360414915d250ebcaa819549fbe` | 2481 |
| PINS.json | `8465e05a5e3af6795ed51d1e4d9ad32b5f96878164082b98d7097632fcbe3484` | 3777 |
| keller-descent-proof.md | `857b2e2fa93cc14acb24fa590a2ffa76961a0d136113908f12b213e126889672` | 16138 |
| accepted-lateT-proof.md | `b541308788da31f52e9f7985c7767e206231e8f3251ff53c1b2bd9c96b64f097` | 13685 |
| accepted-lateT-gate.md | `c9a399a87dc91d78bfc4f811249996ea3e217eda075be679cf27b41af5795c26` | 16975 |
| late-contact-direct-obstruction-coordinator-20260909.md | `2dcff1644acdc77a4665916d71dd4865b6f8f35d0965fb43ece6dd3c671393fa` | 9933 |
| late-contact-direct-obstruction-coordinator-20260909.md.artifact.json | `a5e0a005c7a773740ae3cafe279cc21e66396397de3728b3c641f0892e555f8c` | 684 |
| custody.json | `8cdebed7f994bca759a4937266730fa30d905a0e3667cf0942e22ce178faa943` | 1753 |
| keller-descent-transaction.json | `e922c1a601d9692f1cd21eb20b319e3eb5a5c7dcdb14d0632ecb8ef9a034b37e` | 714 |
| keller-descent-custody.json | `6447efd368e5f1ce4df5f632c5c80f7325e414a8bb60d1602fb11f4374b4e606` | 1773 |
| keller-descent-input-pins.json | `3c40531e03ad55b150f99ce17b37a7631f2435293b8abdf38888cc01f884ce1d` | 622 |
| keller-descent-publication.json | `b465b6bcec9332fb527176fde6f3ee1f6eb56422aa42c541f55d1b10365d9223` | 2826 |

Producer transaction relation, recomputed: the first 15805 bytes of `keller-descent-proof.md` hash to `def446a906f4d914d323e6af543a5e9a9e56750ea835706b59b48770513fd23c`, equal to the `body_sha256` in `keller-descent-transaction.json`, PINS.json and `keller-descent-custody.json`; the first 9601 bytes of the root addendum hash to `146b3af7452d232bae0c79bce1c3b3cbafd9a31c71772a075b3e4510affa70a4`, equal to its artifact manifest. The trailers after each `<!-- BODY-END -->` are seals only. Read whole: the descent proof, the root addendum, `accepted-lateT-proof.md`, `accepted-lateT-gate.md`. Custody, input-pins, publication, transaction and artifact JSON were read as metadata only; no path or citation inside them was followed; the accepted pair's named older reports (Moh receiver, two-pattern framework, admissibility intake) are NOT charged and were not opened. No current blind/cross submission, pending triple/cubic report, other gate or mutable campaign file was read.

Premise discipline: from the accepted pair only the general finite late-T lemma (accepted-lateT-proof §3, its gate §1) is a premise, at its stated polynomial/combined-homogeneous/centralizer scope; I re-derive it in §4 below rather than import it blind. The triple-specific j=12 endpoint, the centralizer computation for H=p²L³, and the monomial-J receiver are NOT premises here. The original descent claim and the root strengthening are both PROVISIONAL inputs.

## Verdict table

| Group | Verdict |
|---|---|
| 1. Coordinate obstruction, all cases | **CONFIRMED** |
| 2. Arbitrary-D canonical reference, F≠0, 1≤j≤3D−1, deg F(1)=3D−j | **CONFIRMED** |
| 3. Five B kernels, exact wedge identity, ord G≥2j | **CONFIRMED** |
| 4. Finite scalar polynomial T=t(R) at D≥3, 3j>7D | **CONFIRMED** (D=2 and 3j=7D outside) |
| 5. Keller descent [f,g]=c and nonautomorphy, including after extension | **CONFIRMED** |
| 6. Global minimality corollary j≤⌊7D/3⌋ and its exact limits | **CONFIRMED as stated; the antecedent is empty by group 7** |
| 7. Root direct leading-form obstruction; removal of minimality | **CONFIRMED**, with scope qualifications in §7 |

No group is REFUTED and no GAP was found inside the arrows of either proof. No theorem beyond the explicitly proved finite lemma and elementary polynomial algebra is used by either document, so nothing had to be imported.

Notation throughout: [P,Q]=P_uQ_v−P_vQ_u in the variables u,v; s is a parameter never differentiated; "order" means s-order; "degree" means total (u,v)-degree unless "combined" (s,u,v) is said.

## 1. Coordinate obstruction (C) — CONFIRMED

Statement re-derived. K any characteristic-zero field, x,y independent, alpha,tau,delta,b4∈K arbitrary (zero allowed), t∈K[T] arbitrary (zero or constant allowed). Identity (C): (3r²+alpha)y−(tau·r+delta)x−((5/3)r+(2/3)b4)x²=t(r). Claim: no nonconstant r∈K[x,y].

Case deg_y r=0. Then r∈K[x] and the only y-bearing term of (C) is (3r²+alpha)y; the right side has no y. So 3r²+alpha=0 in K[x], i.e. r² is a constant. In the domain K[x], deg(r²)=2deg r, so r is constant. Nothing else is needed in this case; the y⁰ row is irrelevant to the lemma.

Case n=deg_y r≥1, a(x)≠0 the y-leading coefficient. y-degrees on the left: 3r²·y has degree 2n+1 with leading coefficient 3a², nonzero in a domain of characteristic zero; alpha·y has degree ≤1; (tau·r+delta)x has degree ≤n; ((5/3)r+(2/3)b4)x² has degree ≤n. Since n≥1, 2n+1>max(n,1), so the left side has y-degree exactly 2n+1. If t is zero or constant the right side has y-degree ≤0: impossible. So m=deg t≥1 and t(r) has y-degree exactly mn with leading coefficient t_m a^m≠0. Hence mn=2n+1, (m−2)n=1, so n=1, m=3. Write r=a(x)y+b(x). Since r=ay+b with a≠0 is transcendental over K(x), y↦r is a K(x)-algebra automorphism of K(x)[y]=K(x)[r], so coefficient comparison in K(x)[r] is legitimate and asserts no inverse of any map on K[u,v]. Substituting y=(r−b)/a, my expansion of the left side is (3/a)r³−(3b/a)r²+(alpha/a−tau·x−(5/3)x²)r+(−alpha·b/a−delta·x−(2/3)b4x²), agreeing with the proof's display. Comparing with t3r³+t2r²+t1r+t0: r³ gives a=3/t3∈K* (t3≠0 because m=3); r² gives b=−a·t2/3∈K; r¹ requires alpha/a−tau·x−(5/3)x²=t1∈K, but the x² coefficient −5/3 is nonzero in characteristic zero. Contradiction. No division by alpha, tau, delta or b4 occurs anywhere, so every zero pattern of the scalars is covered.

Field extension: the proof uses only "characteristic-zero field" and domain properties, so it holds verbatim over every extension K'⊇K, with the same scalars.

Manual dependency controls (hand-checked, mine):
- Constant r is genuinely excluded, not proved impossible: r=0, alpha=delta=b4=0, t=0 satisfies (C) for every tau. Correct as a control of the nonconstancy hypothesis.
- Delete the −(5/3)r·x² term: r=y, all scalars zero, t(T)=3T³ gives 3y²·y=3y³. The altered identity holds, so that term is load-bearing.
- Allow t coefficients in K[x]: r=y, scalars zero, t_x(T)=3T³−(5/3)x²T gives 3y³−(5/3)x²y on both sides. So scalar coefficients of t are load-bearing; this is exactly why group 4 must deliver t_i∈K.
These are dependency controls only; none is a source point or an executed test.

## 2. Arbitrary-D canonical reference and F≠0 — CONFIRMED

Dilations. A_s=s^{3D}A(u/s,v/s)=Σ_d s^{3D−d}A_d is combined-homogeneous of degree 3D; likewise B_s of degree 5D. ∂_uA_s=s^{3D−1}A_u(u/s,v/s), so [A_s,B_s]=s^{8D−2}[A,B](u/s,v/s)=c·s^{8D−2} because c is constant. No further subtraction for a target variable. Confirmed.

R construction. With R=H+Σ_{a=1}^D s^aR_{D−a}, R³=(H+S)³=H³+3H²S+3HS²+S³; the order-a coefficient of 3H²S is 3H²R_{D−a}, and the order-a coefficients of 3HS²+S³ involve only R_{D−b} with 1≤b<a. So at stage a the order-a residual of A_s−R³ (before choosing R_{D−a}) is a homogeneous form of degree 3D−a, fixed by earlier stages. Single-divisor division by 3H² under lex u>v (any fixed order) terminates, gives a homogeneous quotient of degree D−a≥0 (a≤D) and a remainder with no monomial divisible by LM(H²); set R_{D−a}=quotient. Coefficients stay in K (3 is a unit). Orders <a are untouched. At order 2D the residual of A_s−R³ has degree D; division by H gives a scalar quotient alpha and an LM(H)-normal remainder; subtracting alpha·s^{2D}R changes only orders ≥2D>D, so the D normalized residuals survive. At order 3D the residual of A_s−R³−alpha_sR is a scalar a0; subtract a0s^{3D}. F=A_s−R³−alpha_sR−a0s^{3D} is combined-homogeneous of degree 3D with F_0=A_{3D}−H³=0 and F_{3D}=0. No shape of H, parity, weight or one-variable degree bound enters; nothing imported.

F≠0. If F=0 then A_s=φ(R) with φ(X)=X³+alpha_sX+a0s^{3D}, and [A_s,B_s]=(3R²+alpha_s)[R,B_s] in K(s)[u,v], a domain in which (u,v)-degree is additive. R has (u,v)-top form H (all other terms have degree <D), so 3R²+alpha_s has degree exactly 2D>0; the product is 0 or of degree ≥2D, never the nonzero degree-0 element c·s^{8D−2}. Hence F≠0, 1≤j=ord_sF≤3D−1, and F_j is nonzero homogeneous of degree 3D−j. At s=1, F(1)=Σ_{l≥j}F_l with pairwise distinct degrees 3D−l, so deg F(1)=3D−j exactly with top F_j; R(1) has degree D≥3 with top H, nonconstant. Confirmed. The normalization makes j canonical for the chosen order; I note that none of groups 3–7 uses normality, only R(0)=H, alpha∈K and F_{3D}=0.

## 3. Five B kernels and the exact wedge — CONFIRMED

Degrees. beta_i=b_is^{(5−i)D} has combined degree (5−i)D, so every term of f_B(R) has degree 5D; q(R)=(5/3)R²+(4/3)beta4R+beta3−(5/9)alpha_s has degree 2D; tau_s=(2b2−(4/3)b4·alpha)s^{3D} exactly, so ord≥3D (∞ if the scalar vanishes); delta_s=(b1−b3·alpha+(5/9)alpha²)s^{4D}, ord≥4D; G=B_s−f_B(R)−q(R)F has degree 5D.

Scalar identity, my expansion: (3z²+alpha)q(z)=5z⁴+4beta4z³+3beta3z²−(5/3)alpha z²+(5/3)alpha z²+(4/3)alpha·beta4z+alpha·beta3−(5/9)alpha²; adding tau z+delta=2beta2z−(4/3)beta4·alpha z+beta1−beta3·alpha+(5/9)alpha² cancels the cross terms and leaves f_B'(z)=5z⁴+4beta4z³+3beta3z²+2beta2z+beta1. Confirmed.

Wedge, by direct brackets rather than differentials: [A_s,B_s]=[R³+alpha_sR+F, f_B(R)+q(R)F+G]. Terms: [R³+alpha_sR,f_B(R)]=0; [R³+alpha_sR,q(R)F]=(3R²+alpha_s)q(R)[R,F]; [R³+alpha_sR,G]=(3R²+alpha_s)[R,G]; [F,f_B(R)]=−f_B'(R)[R,F]; [F,q(R)F]=−q'(R)F[R,F]; and [F,G]. Sum: (3R²+alpha_s)[R,G]−(tau_sR+delta_s+q'(R)F)[R,F]+[F,G]. For T=(3R²+alpha_s)G−(tau_sR+delta_s)F−((5/3)R+(2/3)beta4)F²: [R,T]=(3R²+alpha_s)[R,G]−(tau_sR+delta_s)[R,F]−((10/3)R+(4/3)beta4)F[R,F], and (10/3)R+(4/3)beta4=q'(R). So [A_s,B_s]=[R,T]+[F,G] exactly (4)–(5), retaining beta4,beta3,beta2,beta1,beta0, alpha and the constant a0 (which drops only because it is s-scalar). Every term of T has combined degree 2D+5D=3D+D+3D=4D+3D=D+6D=7D; T is a polynomial, homogeneous of degree 7D or zero.

ord G≥2j, full induction. G_0=H⁵−H⁵−(5/3)H²F_0=0. Suppose G≠0 with l=ord G<2j. Orders in (4): target 8D−2>6D−2≥2j>l; [F,G]≥j+l>l; in T, (tau_sR+delta_s)F has order ≥3D+j>2j because j≤3D−1; F² has order ≥2j>l; (3R²+alpha_s)G has order ≥l with order-l coefficient 3H²G_l. Hence ord T≥l, T_l=3H²G_l, and the order-l coefficient of [R,T] is Σ_{a+m=l}[R_{D−a},T_m]=[H,T_l]. The order-l equation is [H,3H²G_l]=3H²[H,G_l]=0, so [H,G_l]=0 and by the ASSUMED centralizer G_l∈K[H]. G_l is nonzero homogeneous of degree 5D−l with l>0, so l∈{D,2D,3D,4D,5D} and G_l=e·H^{5−l/D}, e∈K. Effects of b_i→b_i+e, my recomputation: b4: f_B gains es^DR⁴, q gains (4/3)es^DR, tau gains −(4/3)es^D·alpha_s, delta unchanged, so G changes by −es^D(R⁴+(4/3)RF), whose order-D coefficient is −eH⁴ (RF starts at D+j>D); b3: f_B gains es^{2D}R³, q gains es^{2D}, delta gains −es^{2D}alpha_s, so G changes by −es^{2D}(R³+F), order-2D coefficient −eH³ (F starts at 2D+j); b2: −es^{3D}R², coefficient −eH²; b1: −es^{4D}R, coefficient −eH; b0: −es^{5D}. Each change kills the leader at its l and touches no earlier order; tau_s,delta_s keep their exact s-powers. The identity (4) is exact for every scalar choice, so the same order-l equation applies to the new leader. Each l is used at most once and the leaders strictly increase, so at most five steps end with ord G≥2j or with G=0 (forced when 2j>5D, since a nonzero degree-5D polynomial has order ≤5D). This is a choice of reference scalars inside an exact identity; no ordinary coefficient or source equation is discarded and no target gauge is invoked. [F,G] has order ≥j+ord G at every step. Confirmed.

## 4. Finite scalar polynomial T=t(R) — CONFIRMED

Under (L) 3j>7D and D≥3: [R,T]=c·s^{8D−2}−[F,G], ord[F,G]≥j+2j=3j>7D, and 8D−2>7D exactly when D>2. So ord_s[R,T]>7D=combined degree of T (or [R,T]=0). Both strict inequalities are load-bearing: at D=2 the target order 14 equals 7D, and at 3j=7D the bracket order is only ≥7D. Neither case is covered, and the proof says so (§7); I state it explicitly: D=2 and 3j=7D are OUTSIDE this proof.

Lemma re-derived (not imported blind). T=Σ_l s^lT_l with T_l homogeneous of degree 7D−l. If T≠0 let l=ord T≤7D. The order-l coefficient of [R,T] is [H,T_l]; the hypothesis ord[R,T]>7D≥l gives [H,T_l]=0, so T_l∈K[H]; being homogeneous of degree 7D−l it equals t·H^i with iD=7D−l, t∈K (distinct powers of H have distinct degrees, so a homogeneous element of K[H] is a scalar times one power; if D∤(7D−l) then T_l=0, contradicting the choice of l). Subtract t·s^{(7−i)D}R^i: a polynomial of combined degree exactly 7D, commuting with R, with order-l coefficient tH^i; the remainder has strictly larger order and the same bracket. Since a nonzero degree-7D polynomial has order ≤7D, at most eight steps (i=7,…,0) exhaust T. Hence T=Σ_{i=0}^7 t_is^{(7−i)D}R^i with all t_i∈K, exponents (7−i)D≥0 (no negative powers), and [R,T]=0. T=0 is included trivially. This is finite polynomial subtraction; no rational centralizer, series, convergence or localization is used. The accepted lemma is applied at exactly its hypotheses: R polynomial combined-homogeneous of degree D with R(0)=H, T polynomial of combined degree ≤7D, centralizer K[H].

Why scalar t_i matter: the §1 control with t_x(T)=3T³−(5/3)x²T shows that if the coefficients were merely in K[x] (i.e. functions of f after transport), r=y would satisfy the identity and group 5's contradiction would evaporate. The representation (8) forbids this. Confirmed.

## 5. Keller descent and nonautomorphy — CONFIRMED

From (4) and [R,T]=0: [F,G]=c·s^{8D−2} as an exact polynomial identity. Specialization s=1 is a ring map commuting with ∂_u,∂_v, so [f,g]=c for f=F(1), g=G(1). Since c≠0 both f and g are nonconstant; in particular G=0 and G∈K[s] are impossible. Degrees: deg f=3D−j (§2); 3j>7D gives deg f<2D/3. G=Σ_{l≥ord G}s^lG_l with distinct degrees 5D−l and ord G≥2j, so 1≤deg g≤5D−2j<D/3. If 5D−2j≤0 then G is 0 or a scalar multiple of s^{5D}, g is constant and [f,g]=c is already violated: the hypotheses (S)+(L) are impossible there and no zero/constant component is called a Keller pair. deg f+deg g≤8D−3j<D against the original 8D. Confirmed.

Nonautomorphy over K. Suppose φ:K[x,y]→K[u,v], x↦f, y↦g, is an isomorphism. Then r0=R(1)∈K[u,v]=φ(K[x,y]) has a preimage r∈K[x,y]; r∉K since φ fixes K and r0 has degree D≥3. Specializing (5) and (8) at s=1 gives, in K[u,v], (3r0²+alpha)g−(tau·r0+delta)f−((5/3)r0+(2/3)b4)f²=t(r0) with alpha, tau=2b2−(4/3)b4·alpha, delta=b1−b3·alpha+(5/9)alpha², b4∈K and t(Z)=Σt_iZ^i∈K[Z]. Let Φ(r,x,y)∈K[x,y] be the left minus right side of (C) for this r. Then φ(Φ)=0 and φ is injective, so Φ=0: exactly (C) with y↔g and x↔f. Group 1 forbids nonconstant r. So (f,g) is not a polynomial coordinate pair. Only the assumed polynomial inverse (surjectivity for the preimage, injectivity for the identity) is used: no rational inverse, no K(u,v)=K(f,g), no blanket "smaller Keller pairs are nonautomorphic".

After extension K'⊇K (characteristic zero): the identities (5),(8) at s=1 live in K[u,v]⊂K'[u,v] with unchanged scalars; if K'[f,g]=K'[u,v] the same transport gives (C) over K' with r∈K'[x,y] nonconstant, and group 1 holds over K'. The centralizer hypothesis is NOT used in this step; it was consumed only in constructing (6) and (8) over K, which persist. Confirmed. This differs from the accepted triple source, whose target c·s^{36}g² would specialize to [f,g]=cg², not a Keller pair; the constant Jacobian is what makes (9) a genuine Keller descent, and the triple endpoint is correctly excluded from this theorem.

## 6. Global minimality corollary — CONFIRMED as stated

If some nonautomorphic Keller pair over K exists, the set of their maximum component degrees is a nonempty set of positive integers and has a minimum; existence is used only under that conditional. Let (A,B) attain it and satisfy (S). If also (L), group 5 supplies a nonautomorphic Keller pair (f,g) over K with max(deg f,deg g)<2D/3<5D=max(deg A,deg B): a contradiction with minimality among ALL nonautomorphic Keller pairs over K, regardless of whether (f,g) has 3:5 degrees, a closed H, or any contact structure. Hence 3j≤7D, i.e. j≤⌊7D/3⌋. The report's own limits are exact: it does not claim that a minimal counterexample has these degrees, this H or late contact; it draws no conclusion for j≤⌊7D/3⌋, D<3, 3j=7D, monomial Jacobian or arbitrary counterexamples; it asserts no novelty and no automatic iteration (the descended pair need not have the interface). So the original report proves precisely the stated conditional all-D bound and nothing stronger.

Qualification from group 7: the root lemma shows that (S)+(L)+D≥3 is INCONSISTENT, so the descent theorem's antecedent is empty and its conclusion is never instantiated. This does not invalidate any step (a theorem with inconsistent hypotheses is valid), but the minimality hypothesis in the corollary is dispensable, as the root addendum states.

## 7. Root direct obstruction — CONFIRMED, with scope

Lemma re-derived. Hypotheses: r,f,g∈K[u,v]; D=deg r≥3 with top form H and ker[H,−]=K[H] on K[u,v]; m=deg f, n=deg g positive integers with D/2<m<D and n≤2m−D; [f,g]=c∈K*; alpha,tau,delta,b4∈K; t∈K[Z]; identity (C) with x→f, y→g.

Put L=D+2m. m>D/2 gives L>2D; m<D gives L<3D; so L is strictly between 2D and 3D, in particular not a multiple of D and positive. Degrees on the left: 3r²g has degree 2D+n≤2D+2m−D=L, with equality iff n=2m−D; (5/3)rf² has degree exactly L with top form (5/3)Hf_m²≠0; tau·rf has degree ≤D+m<L since m>0; delta·f has degree m<L; (2/3)b4f² has degree 2m<L; alpha·g has degree n<L. A zero scalar deletes a term and can raise nothing; 3 and 5/3 are nonzero. On the right, t nonconstant of degree e gives deg t(r)=eD exactly (top form t_eH^e≠0), and zero/constant t has degree ≤0.

If n<2m−D the unique degree-L contribution is −(5/3)Hf_m², so the left side has degree L, which is neither eD nor ≤0: impossible. If n=2m−D the degree-L coefficient is 3H²g_n−(5/3)Hf_m²; if nonzero the same contradiction; so it vanishes, whatever t is, and dividing by the nonzero H in the domain: 3Hg_n=(5/3)f_m², i.e. g_n=(5/9)f_m²/H in K(u,v), with g_n already a polynomial (no rational-to-polynomial claim). Next, D≥3 and m>D/2 give m≥2, and n≥1, so m+n−2≥1; the degree-(m+n−2) component of the constant [f,g] is [f_m,g_n] and must vanish. Differentiating (R) in K(u,v), where [f_m,−] is a derivation: [f_m,g_n]=(5/9)(f_m²[f_m,H^{−1}]+H^{−1}[f_m,f_m²])=−(5/9)(f_m²/H²)[f_m,H]. With f_m≠0≠H in a field, [f_m,H]=0, so f_m∈K[H] by the explicit centralizer. A nonzero homogeneous element of K[H] has degree a·D with a≥1 (distinct powers of H cannot cancel), contradicting 0<m<D. All cases closed. I also checked that the sign of the F² term is immaterial: with the opposite sign the same chain gives [f_m,g_n]=+(5/9)(f_m²/H²)[f_m,H] and the identical contradiction. Consistency check against the accepted triple data (hand computation, no premise): with f_3=λpL², g_1=(5/9)λ²L, H=p²L³, the formula gives −(5/9)λ³[pL²,p²L³]/(p²L²)=−(5/9)λ³(−p²L⁴)/(p²L²)=(5/9)λ³L², matching that report's direct bracket; there the nonzero target cg² legitimately absorbs it, here the constant target forces zero. Confirmed.

Application through the FULL framework. From groups 2–4, for any source with (S), D≥3 and 3j>7D: r=R(1) has degree D and top H; f=F(1), g=G(1) with [f,g]=c; the specialized (5) and (8) give exactly (C) with scalars alpha,tau,delta,b4∈K and t∈K[Z]; m=3D−j<2D/3<D; n≥1 because c≠0 (positive n is forced, not assumed); n≤5D−2j=2m−D; n≥1 then forces m>D/2. If 5D−2j≤0 the nonzero bracket already contradicts the hypotheses (impossible G endpoints), otherwise every hypothesis of the lemma holds in K[u,v] itself, with no transport, inverse or automorphism assumption. Contradiction either way. Therefore every source with this interface has canonical j≤⌊7D/3⌋, with NO minimality of any kind. I confirm the answer to the invitation's question: yes, for EVERY actual source with the explicit 3:5 / tops H³,H⁵ / ker[H,−]=K[H] / [A,B]∈K* / D≥3 interface. Numerically the lemma is first non-vacuous at D=5, j=12 (m=3,n=1); at D=3,4 every late j already dies at the endpoint 5D−2j≤0.

Field extension: the lemma is applied over K, where the centralizer hypothesis is given, so no extension is needed for the bound. If one did pass to K', the lemma would need ker[H,−]=K'[H] there; this is a distinct inference from group 5's transport of already-built identities, as the addendum correctly says. My own observation, not required by either proof: that hypothesis does transfer, because [H,−] is K-linear and the kernel of its base change to K'[u,v]=K'⊗_KK[u,v] is K'⊗_KK[H]=K'[H].

Scope qualifications, none removed: the bound needs D≥3 (8D−2>7D), strict 3j>7D (equality untreated), the constant nonzero Jacobian (monomial c·g² is not an instance, addendum control 3), degrees exactly 3D/5D with tops H³,H⁵ for one H, the polynomial centralizer K[H] (proper powers h^k are excluded, addendum control 1), and the canonical finite reference of §2–3. No existing unresolved client is claimed to have these hypotheses; no novelty, all-degree coverage, family retirement, iteration or JC2 conclusion follows. The manual controls 1–10 of the addendum §3 were re-checked by hand and are correctly located; controls 5 and 6 (m+n=2 and m∈{D/2,D}) mark genuine boundaries of the lemma.

## 8. Strongest valid scoped statement

Both documents are correct at every numbered arrow as written. The original report proves: for D≥3, any A,B over a characteristic-zero field with (S) and canonical 3j>7D yields a nonautomorphic Keller pair (f,g) with deg f=3D−j<2D/3 and 1≤deg g≤5D−2j<D/3, nonautomorphic after every extension; hence a globally minimal nonautomorphic Keller pair with this interface has j≤⌊7D/3⌋. The root addendum proves, without minimality, that (S) with D≥3 and 3j>7D is inconsistent, so every source with the interface has j≤⌊7D/3⌋. Not concluded by either or by this gate: any contact j≤⌊7D/3⌋, D≤2, 3j=7D, nonconstant Jacobian targets, sources without the centralizer or 3:5 interface, existence or nonexistence of such sources, or any exit price.

<!-- BODY-END -->
