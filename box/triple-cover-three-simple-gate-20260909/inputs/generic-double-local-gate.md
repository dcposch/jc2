# Gate: weight-free degree 15/25 composition (Fable 5.1, 2026-09-09)

Independent hostile whole-proof gate of framework.md (body SHA `47e59373…`), local-consumer.md (body `a8c6b2bc…`) and client-interface.md (body `5d9653bf…`), read whole from the frozen lane copy `/tmp/jc2-lane.CmZwYx/inputs`, plus the exact endpoint statements of minimal-receiver.md, sufficient-lift.md and published-chain-gate.md. Model start 00:45:47 UTC; target 01:16:00 UTC; report written 00:58–01:01 UTC, this correction 01:02 UTC (on time). No producer verdict is repeated: every arrow below was rederived by me from the hypotheses (S) alone. Old weighted sources and gates were not read and are not premises. No CAS beyond two 30-second sympy scalar/degree<=5 projections (inlined in §8); no H/R high power, A15/B25 or 6/10 pair was expanded.

Candidate statement audited (exact): over every characteristic-zero field K (containing a root rho of rho²-3rho+1 in the golden case, both conjugates), there are no A,B in K[g,p] with deg 15/25, tops H³/H⁵, [A,B]_(g,p)=c g², c≠0, for H_Q=p²(g³+p³) or H_G=p²(p+g)(p+(1-rho)g)². No weight, polygon, parity, inner-face, origin or inverse-polynomiality hypothesis was added at any point below.

## 1. Verdict table

| # | claim | verdict | basis (own derivation, §) |
|---|---|---|---|
| 1 | framework: normalization, F≠0, 1≤j≤14, H²∤F_j, centralizer K[H], five kernels, exact wedge identity, ord G≥2j, H\|F_j², rad H\|F_j, (6) | **CONFIRMED** | §2 |
| 2 | exact local charts and factor cover (simple j≤9; d1 j≤11 + golden j12; d2 j≤9; d3 j≤7; F12=λpLM) | **CONFIRMED** | §3 |
| 3 | coalesced consumer (kappa≥2r): monic 6/10 initials, lower-B lemma, common quadratic, strict margins | **CONFIRMED** | §4 |
| 4 | separated consumer (kappa<2r) and simple-root consumer: both sheets, infinite sums, G control, Jacobian loss | **CONFIRMED** | §5 |
| 5 | two golden resonances: (14), c=−5λ³t/9 at p, c=5λ³t(t−1)²/9 at M, incompatibility via 3rho≠0 | **CONFIRMED** (independently recomputed, both signs, both conjugates) | §6, §8 |
| 6 | conditional client/ideal endpoint: six literal receivers + six lift clients, unit ideals by maximal-ideal argument, standard-F2 necessity only | **CONFIRMED as conditional interface**, scope exactly as typed | §7 |

**First unsupported arrow: none found.** The complete candidate (framework + local consumer) is, by my independent reading, a proof of the weight-free statement at exactly its stated field scope. Surviving scope and what is NOT proved are in §7. Two presentation defects (not gaps) are noted in §2 and §3.

## 2. Target 1: framework without weights (independent derivation)

**Dilation.** A_s(g,p)=s^15A(g/s,p/s), so [A_s,B_s]=s^40·s^-2·[A,B](g/s,p/s)=c s^36 g². Combined degree 1 on s,g,p; every object below is combined-homogeneous.

**Normalization at orders 1..5.** Lex g>p; LM(H)=κ g³p² with κ=1 (Q) or κ=t²=rho (golden; t²=1−2rho+rho²=rho, control §8). LM(H²)=g⁶p⁴. At stage a the s^a coefficient of A_s−(reference)³ is homogeneous of degree 15−a; dividing by 3H² (single-divisor division in a graded monomial order) gives a homogeneous quotient R_{5−a} of degree 5−a and a remainder with no monomial divisible by g⁶p⁴. (R+s^aX)³=R³+3R²s^aX+O(s^{a+1}) with R≡H mod s, so exactly 3H²X is added at order a and nothing at lower orders. R_{5−a} may have any g-degree (H+s g⁴ is a legal stage-1 output since A_14 is free); no cubic-in-g or deg_g≤2 property is used anywhere downstream, I checked each later use. Order 10: the degree-5 residual divided by H has scalar quotient α and an H-normal remainder; α s^10 R_s changes only orders ≥10; a0 s^15 kills order 15. Hence F=A_s−R_s³−αs^10R_s−a0s^15 has F_1..F_5 H²-normal, F_10 H-normal, F_15=0.

**F≠0.** If F=0 then in the UFD K[s,g,p], (3R_s²+αs^10)·[R_s,B_s]=c s^36 g². The left factor is not divisible by s (value 3H²≠0 at s=0) and is not a unit times a power of g (its s=0 value has the factor p²), so it cannot divide c s^36 g². Thus 1≤j:=ord_s F≤14 and F_j≠0 is homogeneous of degree 15−j.

**H²∤F_j (2).** j≤5: a nonzero multiple H²X has LM=g⁶p⁴·LM(X), which the remainder lacks. j≥6: deg F_j=15−j≤9<10. No gap between the two ranges.

**Centralizer.** With u=g/p, T=1/p, K(g,p)=K(u,T) and H=h0 reads T⁵=V(u)/h0, V=u³+1 or (1+u)(1+tu)². Over the PID \bar{K(h0)}[u], V/h0 has a simple zero (any root of u³+1; u=−1 in golden, since t≠1⇔rho≠0), so Eisenstein at (u−u0) makes T⁵−V/h0 irreducible over \bar{K(h0)}(u); hence K(g,p)⊗_{K(h0)}\bar{K(h0)} is a field and K(H) is relatively algebraically closed in K(g,p) (a proper finite subextension E would give a non-domain E⊗\bar{K(h0)} inside a domain). The derivation d=[H,·]/H_g kills K(H), has d(p)=1, and K(g,p)/K(H)(p) is finite; applying d to the monic minimal polynomial of a d-constant z gives a lower-degree relation, so all coefficients are d/dp-constants in K(H)(p), i.e. in K(H); z is algebraic over K(H), hence in K(H). A polynomial r(H)/q(H) with gcd(r,q)=1 forces q(H)|1. So the polynomial centralizer is K[H] and a homogeneous element of degree e is 0 unless 5|e, then a scalar H^{e/5}. Reducedness of H=0 is never used. CONFIRMED.

**Exact wedge identity.** I verified f_B'(R)=(3R²+α)q(R)+τR+δ symbolically (§8 residual 0). With A=R³+αR+a0+F, B=f_B(R)+q(R)F+G and R,F,G independent, dA∧dB has dR∧dF coefficient −(τR+δ)−q'F, dR∧dG coefficient 3R²+α, dF∧dG coefficient 1; since [R,(3R²+α)G]=(3R²+α)[R,G], [R,(τR+δ)F]=(τR+δ)[R,F] and [R,(5R/3+2b4/3)F²]=q'F[R,F], identity (3) is exact. Orders: α_s=10, τ_s=15, δ_s=20.

**All five kernels.** If G first appears at l<2j, then at order l only [H,3H²G_l] survives (F² starts at 2j>l, (τR+δ)F at 15+j>2j for j<15, [F,G] at j+l>l, and [R_a,T_{l−a}] vanishes because T_{<l}=0). So G_l∈K[H], degree 25−l, l∈{5,10,15,20,25}, G_l=eH^{(25−l)/5}. Changing b_{4..0} by e changes G by exactly −es⁵(R⁴+(4/3)RF), −es^10(R³+F), −es^15R², −es^20R, −es^25 (b4 enters q, b3 enters q, b2,b1 only τ,δ which are not in G); each kills G_l and touches only orders ≥l. Hence ord G≥2j (∞ allowed). At order 2j<36: [H,3H²G_{2j}−(5/3)HF_j²]=0 with all other terms later (b4-part of the F² coefficient at 5+2j; [F,G] at ≥3j). The inner polynomial has degree 35−2j, centralizer value 0, or a scalar H⁵ (j=5) or H³ (j=10); all in H²K[g,p], so H|F_j² and rad H|F_j (any prime of H divides F_j², hence F_j; the "multiplicity 1 or 2" remark is not needed). Degrees: j≤11 (Q, deg D=4), j≤12 (golden, deg D=3). If H|F_j: deg F_j≥5 ⇒ j≤10, and j=10 is excluded by H-normality; so (6): F_j=HC, deg C=10−j, H∤C by (2). CONFIRMED.

Presentation defect (not a gap): "product has degree 2" in the F≠0 paragraph means (g,p)-degree; the combined degree is 38. Harmless.

## 3. Target 2: exact charts and cover

**Factors over \bar K.** Q: p double, three distinct simple factors of g³+p³. Golden: L simple; p and M double (L, M, p pairwise distinct since t≠0,1). Both double factors are treated; p is charted with (y,X)=(p,g), M and simple roots with (y,X)=(g,p).

**Simple chart.** H_y(y0,X)≠0 for X≠0, so R_s(y,X)=z inverts in \bar K(X)[[s,z]] with nonnegative orders, and y_z is a unit (1/H_y at s=z=0). With F_j=HC, C(y0)≠0: the s^j coefficient of F∘(inverse) is z·(unit), so ord f_1=j, ord f_0>j, all ord f_n≥j.

**Double chart, general degree-5 R_s.** R_y(y,X)=0 has a formal solution y_c(s,X)∈\bar K(X)[[s]] by Hensel at the nondegenerate critical point y0 (H_yy(y0,X)≠0 for X≠0). Taylor at y_c: R_s(y_c+w,X)=ξ_s+w²U_s(w,X), U_0(0,X)=H_yy(y0,X)/2 = (t²X³ at p=0; t(t−1)X³ at M=0; X³ at p=0 in Q), all verified in §8. sqrt(U_s)=sqrt(U_0(0,X))·(1+(s,w)-ideal)^{1/2} converges in \bar K(X^{1/2})[[s,w]]; ζ=w·sqrt(U_s) inverts with nonnegative s,ζ orders; R_s=ξ_s+ζ² exactly; ζ has degree 5/2; y_ζ(0,0)=1/(aX^{3/2}) with a²=U_0(0,X)/X³. All higher w-terms and the moving y_c are retained inside U_s; nothing is truncated. ord ξ_s=:kappa≥1 (ξ_0=H(y0,X)=0), integer or ∞. The s^j coefficient of F∘(chart) is F_j(y0+w(ζ),X)=w^d·(unit)=ζ^d·(nonzero)+O(ζ^{d+1}), so ord c_d=j, ord c_n>j for n<d, all ≥j. **Bracket transport.** [A,B]_(ζ,X)=[A,B]_(y,X)·y_ζ (chain rule with X fixed), so the target is c s^36 g² y_ζ with g=X (p-chart) or g=−X/t+O(s,ζ) (M-chart): exact order 36, nonzero leading coefficient. Sign: (y,X)=(p,g) gives [A,B]_(p,g)=−c g². B_s−R_s⁵∈sK[s,g,p] since B_0=H⁵=R_0⁵, and nonnegative-order substitution preserves ord≥1. CONFIRMED.

**Cover (own case split).** H|F_j (j≤9, F_j=HC, H∤C): (i) some simple factor ∤C ⇒ simple chart with nonzero C-value, j≤9; (ii) some double T∤C ⇒ ord_T F_j=2, j≤9; (iii) all factors divide C ⇒ D|C ⇒ j≤6 (Q), j≤7 (golden); if every double T had T²|C then H|C (coprime factors), so some T has ord_T C=1, ord_T F_j=3, j≤7. H∤F_j: D|F_j so every simple factor divides F_j and some double T has ord_T F_j=1 exactly; j≤11 (Q), j≤12 (golden). Golden j=12: deg F_12=3=deg D ⇒ F_12=λpLM, λ≠0, multiplicity exactly 1 at p and at M. Every branch uses a factor of multiplicity in {1,2,3}; d≥4 never arises. CONFIRMED. Ribbon/nilpotent rings never appear: all local work is over the field E=\bar K(X^{1/2}) and its Puiseux series.

## 4. Target 3: coalesced consumer

r=min_{n≤d} ord(c_n)/(6−n) is finite (c_d has order j), positive, ≤j/(6−d). Assume kappa≥2r. At ζ=s^rY: terms n≤d have order ≥6r with equality at the minimiser; n>d have order ≥j+(d+1)r≥(6−d)r+(d+1)r=7r. So F has a nonzero initial U(Y), deg U≤d≤3, at 6r; R has initial Y²+b at 2r with b=0 unless kappa=2r; R³ contributes exactly (Y²+b)³ at 6r (next term at 4r+kappa>6r); αs^10R at 10+2r>6r iff r<5/2; a0 later. P=(Y²+b)³+U monic 6, Euler degree 6h, h=5/2−r>0 (Y has degree 5/2−r).

**Lower-B lemma (own proof).** Below 10r all B terms come from B−R⁵ (R⁵'s terms have order (5−k)kappa+2rk≥10r), whose Morse coefficients have order ≥1; hence any coefficient of s^ν, ν<10r, has Y-degree n with nr≤ν−1. **Top-coefficient lemma (own proof).** P monic of degree m≥1, Q≠0 of degree n, [P,Q]_(Y,X)=0: the Y^{m+n−1} coefficient is m·q_n' (P_X has degree ≤m−1), so q_n∈\bar K and the Euler identity forces Λ=nh. With Λ=25−ν and nh≤(ν−1)(5/(2r)−1): 25−ν−nh≥24+(5/(2r))(1−ν)>0 iff ν<9.6r+1, implied by ν<10r and r≤5/2. Commutation holds because 6r+ν<36+r ⇐ 5r+ν<15r≤36. So B starts exactly at 10r with monic Q=(Y²+b)⁵+(degree<10), Euler degree 10h. If 15r<36 (16r<36+r), [P,Q]=0; Euler gives X[P,Q]=h(5P_YQ−3PQ_Y), so (Q³/P⁵)_Y=0, monicity gives Q³=P⁵, UFD in E[Y] gives P=W³ with W monic quadratic (the 3/5-coprime valuation argument is degree-independent; what is degree-specific is only the next step). W=Y²+βY+γ: Y⁵ coefficient 3β=0, Y⁴ coefficient 3γ=3b, so W=Y²+b and U=0 — contradiction. Control §8 confirms this and that deg U=4 would NOT be excluded (γ=b+u4/3 survives), so d≤3 is structural; the cover never needs d=4. Margins: 15r≤3j≤33 (d1,j≤11), ≤15j/4≤33.75 (d2,j≤9), ≤5j≤35 (d3,j≤7); r<5/2 in all. d1,j=12: r<12/5 excluded, r=12/5 open ⇒ §6. CONFIRMED; kappa≥2r is used only inside this branch.

## 5. Target 4: separated and simple consumers

**Separated (kappa<2r, so ξ≠0).** (7) ord c_n+n·kappa/2>3kappa: n≤d from ord c_n≥(6−n)r>(6−n)kappa/2; n>d from ord c_n≥j≥(6−d)r and n≥d+1 (gives >7kappa/2). Regroup F=U(z)+ζV(z), U_l=Σ_m C(m,l)c_{2m}(−ξ)^{m−l}: summand orders ≥j+(m−l)kappa→∞, so coefficientwise convergent, ord U_l,V_l≥j, and (8) ord U_l+l·kappa>3kappa, ord V_l+kappa/2+l·kappa>3kappa (strict survives summation since the infimum over a discrete set tending to ∞ is attained). Sheets ζ_±=±b_s(1−z/ξ)^{1/2}, b_s=sqrt(−ξ_s) of order kappa/2 (needs s^{kappa/2} and X^{(5−kappa)/2}∈E: fine). η=min(q0/3,q1/2)>kappa; finite because ord V_0=j (d1), ord U_1=j (d2), ord V_1=j (d3), giving η<2j/5, ≤j/2, <2j/3 respectively (using kappa<2r≤2j/(6−d)); so η<j and η<5 in all ranges including d1,j=12. At z=s^ηZ the k-th binomial correction of a base sits k(η−kappa)>0 later than its base; l≥2 bases are ≥j+2η>3η; l=0,1 bases are ≥3η with one attained; an attained coefficient has two-sheet tuple (a+b,a−b), not both zero in characteristic 0. Since R=z exactly, z³=s^{3η}Z³ with no ξ interference, αs^10z at 10+η>3η. So P_±=Z³+u_±Z+v_± (depressed: every Z² source is later, checked: l=2 base, k=1 correction of l=1, k=2 correction of l=0), with (u_+,v_+,u_−,v_−)≠0. Euler degree 3h, h=5−η.

B on a sheet: z⁵ at 5η; b_i terms at 25−i(5−η)>5η; (5/3)z²F at 5η contributing (5/3)Z²(u_±Z+v_±); the other q terms at 5+4η and 10+3η, later since η<5. G: Morse coefficients have order ≥2j; the same regrouping converges; the earliest order across sheets is the minimal base order (corrections later, distinct l distinct degrees, tuple argument). d1: 2j>5η so G is absent through 5η. d2: a base below 5η needs 2j+lη<5η, l=0; d3: l≤1. **Jacobian loss (own computation).** [A_±,B_±]_(z,X)=[A,B]_(ζ,X)·∂_zζ_±=(target)/(2ζ_±): order 36−kappa/2 with nonzero leading coefficient (c, g², y_ζ, sqrt(−ξ_kappa) all nonzero); in (Z,X) add η. An early G initial Q at ν<5η commutes with P_± since 3η+ν<36−kappa/2+η ⇐ 7η+kappa/2<36, which I re-derived: d1 ≤(7j+5kappa)/3<3j≤36; d2 <15j/4≤33.75; d3 ≤7j/2+9kappa/4<5j≤35. Then Λ=25−ν>0 (deg 0) or 25−ν−h=20−ν+η>20−4η>0 (deg 1) contradicts the top-coefficient lemma. So on each sheet Q_±=Z⁵+(5/3)Z²(u_±Z+v_±)+ℓ_±Z+e_± (ℓ=e=0 for d1), monic 5, Euler 5h; 8η<36−kappa/2+η gives [P_±,Q_±]=0; e=1 in the common-root lemma gives W=Z+β, depressed ⇒ β=0 ⇒ u_±=v_±=0 on BOTH sheets, contradicting (11). Neither sheet was discarded and no square-root correction was dropped; η=kappa is impossible because η>kappa is strict from (8). CONFIRMED for d1 j≤12, d2 j≤9, d3 j≤7.

**Simple root (independent, no normal-remainder injection).** η=min(j/2,q/3)∈(0,9/2]. At z=s^ηZ: n≥2 terms at ≥j+2η>3η; P=Z³+uZ+v, (u,v)≠0; αs^10z later (η<5). B: z⁵ and (5/3)z²F at 5η; b_i and other q terms later; G coefficients ≥2j, so below 5η only degree 0 (2j+η≥5η ⇔ η≤j/2), which commutes (2η+ν<7η<36, since 7η≤31.5) and is killed by Λ=25−ν>0; at 5η G adds ≤ linear+constant. Target order in (z,X) is exactly 36 (y_z unit), 36+η in (Z,X); 8η<36+η. So [P,Q]=0, W=Z, u=v=0: contradiction. CONFIRMED for j≤9. I found no counterexample to the analytic interface; every step is an inequality on exact orders plus the two one-variable lemmas.

## 6. Target 5: two golden resonances from total degree only

d1, j=12, coalesced with r=12/5 forced (r<12/5 dies by §4 with 15r<36; separated dies by §5). Then ord c_0/6≥12/5 ⇒ ord c_0≥72/5 ⇒ ≥15 (integer orders before rescaling); kappa≥24/5 ⇒ kappa≥5>2r ⇒ b=0. **Complete initials (own audit at ζ=s^{12/5}Y).** A: Y⁶ at 72/5 from (s^{24/5}Y²)³; next R³ term 3ξζ⁴ at ≥5+48/5=14.6>14.4; c_1ζ at 12+12/5=72/5 with leading kX^{1/2}; c_0 at ≥15; c_{n≥2} at ≥12+24/5=16.8; αs^10R at 14.8; a0 at 15. So P=Y⁶+kX^{1/2}Y exactly. B: Y^{10} at 24 (next R⁵ term at ≥5+96/5=24.2); b_i s^{25−5i}R^i at 25−i/5>24 for i≤4; (5/3)R²F at 48/5+72/5=24 giving (5/3)kX^{1/2}Y⁵; (4/3)b4s⁵RF at 24.2; (b3−5α/9)s^10F at 24.4; (5/3)R²c_0 at ≥24.6; G at ≥24 with only its ζ⁰ coefficient at 24, combined degree 25−24=1, hence eX, e∈\bar K. B has nothing below 24 and A nothing below 72/5, so the order-192/5 bracket coefficient is exactly [P,Q]_(Y,X), and it must EQUAL the target's leading coefficient (order 36+12/5 in (Y,X)), never zero.

**k in each chart (degree≤5 projections, §8).** p-chart (y,X)=(p,g): H has p²-coefficient t²g³=rho X³, F12 has p-derivative λtX² at p=0; ζ=w·aX^{3/2}+…, a²=rho, so k=λt/a. M-chart (y,X)=(g,p), y0=−X/t: H=t(t−1)X³w²+t²X²w³, F12=λ(t−1)X²w+O(w²); a²=t(t−1)=2rho−1≠0; k=λ(t−1)/a. **(14) recomputed** with T=X^{1/2}, ∂_X=∂_T/(2T): [P,Q]=(6e−10k²/3)Y⁵+ekX^{1/2} (§8 output; Y^{10} terms cancel at 5k each). **Targets.** p-chart: [A,B]_(p,g)=−cg²=−cX², times y_ζ=1/(aX^{3/2}): −cX^{1/2}/a. M-chart: cg²=cy²→cX²/t², times 1/(aX^{3/2}): cX^{1/2}/(t²a). Both force e=5k²/9; then c=−a·(5/9)k³=−(5/9)λ³t³/rho=−5λ³t/9 (p) and c=t²a(5/9)k³=(5/9)t²λ³(t−1)³/(t(t−1))=5λ³t(t−1)²/9 (M); both confirmed exactly modulo rho²−3rho+1 in §8 using 1/rho=3−rho and 1/(2rho−1)=2rho−5. a→−a sends k→−k and leaves ak³ fixed, so neither Morse sign is a branch. Equality requires (t−1)²+1=rho²+1=3rho=0, false for both conjugates (rho≠0); §8 gives c_p−c_M=5λ³(2rho−1)/3≠0. Local equality of the bracket coefficient with the nonzero target was used, not commutation. No weighted-face row, unequal-case relation or old M verdict enters. CONFIRMED.

## 7. Target 6: conditional client/ideal endpoint and surviving scope

Accepted at scope: minimal receiver gives, for each of the three polygon cases over k_Q or k_rho, polynomial (A,B) of degrees 15/25 with A_15=λ_P H³, B_25=λ_Q H⁵ (whole top forms), λ_Pλ_Q≠0, [A,B]=c0γ² with c0≠0, H literally H_Q or H_G with both conjugates kept. Dividing A by λ_P and B by λ_Q is a same-field operation giving tops H³/H⁵ and c=c0/(λ_Pλ_Q)≠0; no root extraction, no c=1, no centering, no dilation is needed for (S). Therefore WF (if accepted) applies verbatim to all six normalized receivers: unequal/Q (c=−5/9), unequal/Qrho (c=−5/(9rho), a unit since rho^{-1}=3−rho), common3 and common4 over Q and Qrho with c guarded by zc−1. **Maximal-ideal argument (own check).** If a receiver ideal I_rec in its original finitely generated guarded ring R over k∈{Q,Q(rho)} were proper, a maximal m⊇I_rec has residue field R/m finite over k (Zariski), characteristic 0, containing k (a field maps injectively), hence containing the same rho; the images give a pair over R/m with monic fixed tops H³/H⁵, all bracket rows zero except the target, and c≠0 by the guard or fixed unit — exactly (S), contradicting WF. So I_rec=(1), and I_full=I_rec R_full+(105 rows)=(1) by inclusion, and the common4/Q z_h-localized 372/817 ideal likewise. These are existential cofactors; no unit certificate, cofactor degree or solver statement follows. Sufficient lift stays a separate, WF-independent sufficiency contract (its systems would simply have no points). Necessity: published-chain gate (accepted) takes an already polynomial standard (3,5) F2 pair of degrees 75/125 with data (5,20),(1,0),(7/5,2) to (30,50) receivers with J=c0x³; the minimal receiver's S carries these to (15,25), J=c0γ² with the same scalar and whole top faces λ_P H³, λ_Q H⁵; rescaling gives (S). So WF would exclude exactly that standard-F2 input, conditional on the chain's named GGV/Algorithms imports and the rectangle normalization. NOT covered, and correctly not claimed anywhere: arbitrary 75/125 pairs, any D125/Moh/Roy object, any global degree bound, JC2. No narrowing of the local theorem occurred, so no narrowed client verdict is needed. CONFIRMED as a conditional interface.

**Precise surviving scope.** If root accepts §2–§6, the weight-free theorem holds over every characteristic-zero field, both rho conjugates, with no hypothesis beyond (S). The composition then yields: no field points on the six normalized receiver families; unit ideals in their original guarded rings and lift extensions (existentially); exclusion of the standard-F2 (3,5) 75/125 source under the accepted chain's external dependencies. Nothing here asserts properness, a point, source existence, novelty or solver performance.

Presentation defects (no mathematical effect): framework §4 "multiplicity 1 or 2" is unnecessary for rad H|F_j; local-consumer §3 writes "15r≤36" for the lower-B step and "15r<36" for the final step, which is correct but the reader must notice the equality case is deliberately deferred to §5.

## 8. Controls (exact code and output, Python -I -B, sympy, <1 s each)

ctrl.py (first run; the final scalar block of this file raised a sympy `rem` error on 1/rho and was replaced by ctrl2.py; the lines below are the successful output):
```
(14) bracket: T*e*k + Y**5*(6*e - 10*k**2/3)
(14) matches producer: True
t^2-rho -> 0  t(t-1)-(2rho-1) -> 0  (t-1)^2+1-3rho -> 0
p-chart: H p^2 coeff: rho  F12_p at p=0: -lam*rho + lam
M-chart: H w^2 coeff: 2*rho - 1  F12_w at root: -lam*rho
```
(−λrho+λ=λt and −λrho=λ(t−1) as claimed.) Code of the successful part of ctrl.py:
```python
import sympy as sp
Y,T,k,e,lam,a,rho,c=sp.symbols('Y T k e lam a rho c'); X=T**2
dX=lambda f: sp.diff(f,T)/(2*T)
br=lambda P,Q: sp.expand(sp.diff(P,Y)*dX(Q)-dX(P)*sp.diff(Q,Y))
P=Y**6+k*T*Y; Q=Y**10+sp.Rational(5,3)*k*T*Y**5+e*X; B=br(P,Q)
print("(14) bracket:",sp.collect(B,Y))
print("(14) matches producer:",sp.simplify(B-((6*e-sp.Rational(10,3)*k**2)*Y**5+e*k*T))==0)
t=1-rho; red=lambda f: sp.rem(sp.expand(f),rho**2-3*rho+1,rho)
print("t^2-rho ->",red(t**2-rho)," t(t-1)-(2rho-1) ->",red(t*(t-1)-(2*rho-1))," (t-1)^2+1-3rho ->",red((t-1)**2+1-3*rho))
g,p,w=sp.symbols('g p w'); H=p**2*(p+g)*(p+t*g)**2; F12=lam*p*(p+g)*(p+t*g)
print("p-chart: H p^2 coeff:",red(sp.Poly(sp.expand(H),p).coeff_monomial(p**2)/g**3)," F12_p at p=0:",red(sp.diff(F12,p).subs(p,0)/g**2))
HM=sp.expand(H.subs(g,-p/t+w)); FM=sp.expand(F12.subs(g,-p/t+w))
print("M-chart: H w^2 coeff:",red(sp.simplify(sp.Poly(HM,w).coeff_monomial(w**2)/p**3))," F12_w at root:",red(sp.simplify(sp.Poly(FM,w).coeff_monomial(w))/p**2))
```
ctrl2.py:
```python
import sympy as sp
Y,k,lam,rho,b,be,ga,u0,u1,u2,u3,u4=sp.symbols('Y k lam rho b beta gamma u0 u1 u2 u3 u4')
red=lambda f: sp.rem(sp.expand(f),rho**2-3*rho+1,rho); t=1-rho
inv_rho=3-rho; inv_tt1=2*rho-5
print("inverse checks:",red(rho*inv_rho-1),red((2*rho-1)*inv_tt1-1))
c_p=-sp.Rational(5,9)*lam**3*t**3*inv_rho
c_M= sp.Rational(5,9)*t**2*lam**3*(t-1)**3*inv_tt1
print("c_p - (-5 lam^3 t/9) ->",red(c_p+sp.Rational(5,9)*lam**3*t))
print("c_M - (5 lam^3 t (t-1)^2/9) ->",red(c_M-sp.Rational(5,9)*lam**3*t*(t-1)**2))
print("c_p - c_M ->",sp.factor(red(c_p-c_M)),"  (nonzero: coefficient of lam^3)")
W3=sp.expand((Y**2+be*Y+ga)**3)
for degU,U,vs in ((3,u0+u1*Y+u2*Y**2+u3*Y**3,[u0,u1,u2,u3]),(4,u0+u1*Y+u2*Y**2+u3*Y**3+u4*Y**4,[u0,u1,u2,u3,u4])):
    eqs=sp.Poly(sp.expand((Y**2+b)**3+U)-W3,Y).all_coeffs()
    print("deg U =",degU,"->",sp.solve(eqs,[be,ga]+vs,dict=True))
R,al,b4,b3,b2,b1=sp.symbols('R alpha b4 b3 b2 b1')
fB=R**5+b4*R**4+b3*R**3+b2*R**2+b1*R; q=sp.Rational(5,3)*R**2+sp.Rational(4,3)*b4*R+b3-sp.Rational(5,9)*al
print("f_B' identity residual:",sp.expand(sp.diff(fB,R)-((3*R**2+al)*q+(2*b2-sp.Rational(4,3)*b4*al)*R+(b1-b3*al+sp.Rational(5,9)*al**2))))
g,p=sp.symbols('g p')
for name,H in (("Q",p**2*(g**3+p**3)),("G",p**2*(p+g)*(p+t*g)**2)):
    print(name,"lead coeff g^3p^2:",red(sp.Poly(sp.expand(H),g,p).coeff_monomial(g**3*p**2)))
```
Output:
```
inverse checks: 0 0
c_p - (-5 lam^3 t/9) -> 0
c_M - (5 lam^3 t (t-1)^2/9) -> 0
c_p - c_M -> 5*lam**3*(2*rho - 1)/3   (nonzero: coefficient of lam^3)
deg U = 3 -> [{beta: 0, gamma: b, u0: 0, u1: 0, u2: 0, u3: 0}]
deg U = 4 -> [{beta: 0, gamma: (3*b + u4)/3, u0: u4*(27*b**2 + 9*b*u4 + u4**2)/27, u1: 0, u2: u4*(6*b + u4)/3, u3: 0}]
f_B' identity residual: 0
Q lead coeff g^3p^2: 1
G lead coeff g^3p^2: rho
```
Changed-object behaviour: the deg U=4 row is the genuine negative (the common-quadratic step fails there, as the producer asserts); the c_p−c_M line shows the two resonance values differ by a unit multiple of λ³. These are scalar/degree≤5 projections, not source expansions, and prove nothing universal by themselves; the universal content is §2–§7.

## 9. Limits and stop

Only the eleven charged frozen files were read; transactions/PINS/packet as provenance only. No canonical, shared or protected file was touched; the only writes are this report and /tmp/wfgate. No AWS/SSH/web/new agent, no charge_basis, no exit price, no Seal. Verdict: no unsupported arrow found in the framework, the local consumer or the conditional client typing; root alone decides acceptance and any follow-on. STOP/IDLE.

<!-- BODY-END -->
