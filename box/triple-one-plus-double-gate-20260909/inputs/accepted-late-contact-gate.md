# Hostile gate: triple-profile late endpoint j=12 (Fable 5.1, 2026-09-09)

Lane `/tmp/jc2-lane.x3too2`, frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. Root invitation 01:34 UTC, absolute target 01:54 UTC. Independent different-model hostile review of the producer proof `late-triple-proof.md` (source `xmodel/late-contact-triple-endpoint-astra-20260909.md`). PURE PROSE / MANUAL FACTORED REVIEW: no Python, CAS, checker, pair expansion, high H/R power, network, agent, ledger edit or link-following. Every derivation below was done by hand on degree<=5 factored objects.

## 0. Pins and read scope

`sha256sum` on the nine charged files in `/tmp/jc2-lane.x3too2/inputs` was run BEFORE any mathematical body was read. Every digest equals its `PINS.json` entry and its `charged-inputs.list` line:

| basename | sha256 (charged bytes) | bytes | read |
|---|---|---|---|
| PINS.json | `219780293d0a628cc42b5a318083855bad343061b750203b43acdd96aedde627` | 4311 | whole (metadata) |
| late-triple-proof.md | `b541308788da31f52e9f7985c7767e206231e8f3251ff53c1b2bd9c96b64f097` | 13685 | whole incl. seal |
| two-pattern-framework.md | `cbc0330b001faeb8692e45c3be3fdcd3c0727b5734e648143642234da5d63696` | 15640 | whole incl. seal |
| actual-moh-source.md | `07e53340002c48b29a97d567ceb9eb867a292e9cbdd932ce7f508e0694875c46` | 13229 | whole incl. seal |
| actual-moh-source-gate.md | `eade8ec8b9b9162bf3a6a9e60408094185b63b633e6343cce11b7e233e904284` | 14160 | whole |
| multiplicity-admissibility.md | `909ba868b027834a31c6eda37546f17694478cad93d35233d047f1321c0875c0` | 9758 | whole incl. seal |
| late-triple-transaction.json | `1c404f7e05d942156b3c5ac699559592af0045262007a157054db9d4738c90c5` | 703 | metadata only |
| late-triple-custody.json | `6cacbdeda4895267d6639e88f0bdaf4efd2004f0547b446a126e01bdb35a8872` | 2750 | metadata only |
| late-triple-input-pins.json | `e2e459fb322aef1570b4a7cd73bff77127eef5faf0861e0f44e013c9eb25fde4` | 1140 | metadata only |
| late-triple-publication.json | `6fce01a956847fcef94ae286325be27f2560f9eac59c1d5da8b2e57ba8d57bd4` | 1923 | metadata only |

The producer transaction's body hash `85e15287…e3dc` (13352 bytes) is recorded in PINS/transaction/custody consistently; I did not recompute a body hash (metadata, not evidence). The two-pattern framework was read only as an audit comparison; nothing from its squarefree-Q/golden scope, its Eisenstein simple-factor fibre argument, or its conditional local consumers is used as a premise here. The admissibility report is source typing only. No current blind, live gate, canonical post-state or uncharged file was read.

## Verdict table

| Target | Verdict |
|---|---|
| 1. Finite late-T lemma | **CONFIRMED** |
| 2. Triple centralizer K[H] without a simple factor | **CONFIRMED** |
| 3. Ordinary source (S), dilation, canonical R/alpha/a0, F!=0, 1<=j<=14, H²∤F_j | **CONFIRMED** |
| 4. B kernels, exact wedge identity (7), ord G>=2j, (9), H\|F_j², pL²\|F_j, j<=12 | **CONFIRMED** |
| 5. j=12: F12=λpL², G24=(5/9)λ²L, ord[R,T]>=36, s³⁶ coefficient (5/9)λ³L², contradiction | **CONFIRMED** |
| 6. Conditional Moh attachment and stopping scope | **CONFIRMED as conditional**; external trust named in §6 |

No target is REFUTED and no GAP was found inside the proof's own arrows. The theorem is: for any pair satisfying (S) over a characteristic-zero field, the canonical first-contact order j is not 12. Its attachment to the Moh receiver is conditional exactly as in §6.

## 1. Finite late-T lemma — CONFIRMED

**Re-derivation.** Bracket is in (g,p) with s a parameter. Let T be combined-homogeneous of degree N, T=Σ_l s^l T_l, T_l∈K[g,p] homogeneous of degree N−l. R=Σ_a s^a R_{D−a}, R_D=H. The s^l coefficient of [R,T] is Σ_{a+m=l}[R_{D−a},T_m]; if l=ord_s T then only a=0 survives, giving [H,T_l]. Hypothesis (2) says ord_s[R,T]>N>=l, so [H,T_l]=0. By the centralizer hypothesis T_l∈K[H]; homogeneity of degree N−l forces T_l=aH^i with Di=N−l, so the exponent N−Di=l>=0 is automatic and i<=N/D. If D∤(N−l) then T_l=0, contradicting the choice of l. Subtract a s^{N−Di}R^i: this is a polynomial of combined degree N, commutes with R (so the bracket is unchanged), and its order-l coefficient is aH^i, so the remainder has order>l. A nonzero combined-homogeneous polynomial of degree N has s-order<=N (the s^N coefficient is a scalar), so after at most ⌊N/D⌋+1 steps the remainder is zero. Hence T=Σ a_i s^{N−Di}R^i and [R,T]=0. T=0 and [R,T]=0 (infinite order) are trivially included. Scalar constants a∈K only; no field extension.

**Nonhomogeneous bounded T.** T=Σ_{n<=N}T^{(n)}; [R,T^{(n)}] is combined-homogeneous of degree n+D−2, distinct for distinct n, so no cancellation between pieces: ord_s[R,T]=min over nonzero pieces. Thus each piece has ord_s[R,T^{(n)}]>N>=n and the homogeneous case applies with its own bound n. Correct.

**Manual countercontrols (hand-checked, my own recomputation).**
(a) R=g³+s²p, T=g: R_g=3g², R_p=s², T_g=1, T_p=0; [R,T]=3g²·0−s²·1=−s², order 2>N=1, nonzero. The omitted hypothesis is the centralizer: [g³,T]=3g²T_p, so ker=K[g]≠K[g³]. Correctly located.
(b) R=g, T=s²p: [R,T]=1·s²−0=s², order 2; the centralizer of H=g is K[g]=K[H] (hypothesis satisfied), but T has combined degree 3, so N=1 is false and (2) fails with the true N=3. Correctly located. Neither control claims threshold sharpness; none is needed.

**Attacks tried.** (i) "T_l could be a scalar at l=N": then i=0, subtract a s^N; fine. (ii) "subtraction could raise the combined degree": no, s^{N−Di}R^i has degree exactly N. (iii) "hidden dependence on R being polynomial in s beyond order D": none, only R_D=H is used at the leading step and commutation [R,R^i]=0 elsewhere.

## 2. Centralizer of H=p²L³ — CONFIRMED

With L=p−g, u=pL: u²=p²L² so H/u²=L; u³=p³L³ so u³/H=p; g=p−L=u³/H−H/u². Hence K(H,u)=K(g,p), transcendence degree 2, so H,u are algebraically independent.

Sign, my own differentiation with [U,V]=U_gV_p−U_pV_g, L_g=−1, L_p=1: H_g=−3p²L², H_p=2pL³+3p²L²=pL²(2L+3p); u_g=−p, u_p=L+p. [H,u]=(−3p²L²)(L+p)−pL²(2L+3p)(−p)=p²L²(−3L−3p+2L+3p)=−p²L³=−H. Confirmed.

D=[H,−] is a K-derivation of K(g,p)=K(H,u) with D(H)=0, D(u)=−H, hence D=−H·∂/∂u in the (H,u) coordinates (two K-derivations agreeing on generators of a purely transcendental extension coincide). In characteristic zero ker ∂_u on K(H)(u) is K(H). Polynomial part: if r(H)/q(H)∈K[g,p] with r,q coprime in K[X], Bezout ar+bq=1 gives 1/q(H)=a(H)·r(H)/q(H)+b(H)∈K[g,p], so q(H) is a unit of K[g,p], hence a nonzero constant; since H is nonconstant, q is constant. So ker(D|K[g,p])=K[H], and a homogeneous element of degree e is a·H^{e/5} or zero. Valid over every characteristic-zero field; no algebraic closure, no simple factor, no generic-fibre integrality and no localization of the receiver are used. The rational coordinates appear only inside this kernel computation, as the proof states.

## 3. Ordinary source and canonical normalization — CONFIRMED

Dilation: A_s=s^{15}A(g/s,p/s), so ∂_g A_s=s^{14}A_g(g/s,p/s); [A_s,B_s]=s^{38}[A,B](g/s,p/s)=s^{38}c(g/s)²=cs^{36}g². Combined degrees 15/25. Confirmed.

R construction: with R=H+sR_4+…+s^5R_0, the order-a coefficient of R³ is 3H²R_{5−a} plus products of already fixed lower coefficients, so the order-a residual of A_s−R³ (before choosing R_{5−a}) is a homogeneous polynomial of degree 15−a; single-divisor monomial division by 3H² under lex g>p gives a unique quotient of degree 5−a and a remainder with no monomial divisible by LM(H²). Later stages and the alpha/a0 subtractions change only orders >a (resp. >=10, 15). Leading monomials, my own expansion: (p−g)³=−g³+3g²p−3gp²+p³, so H=−g³p²+3g²p³−3gp⁴+p⁵, LM=−g³p²; LM(H²)=g⁶p⁴. Confirmed. Order 10: residual of degree 5 divided by H gives scalar alpha; order 15: scalar a0. Denominators 3 (and 5/3, 4/3, 5/9, 2/3 in §4) are field units in characteristic zero. No root, extension, parity, weight, polygon or lift assumption enters; H has integer coefficients. A_s,B_s are never modified; R,alpha,a0 only decompose A_s.

F≠0: if F=0 then A_s=φ(R), φ(X)=X³+α_sX+a_0s^{15}, and [A_s,B_s]=(3R²+α_s)[R,B_s]. In K(s)[g,p], 3R²+α_s has (g,p)-degree exactly 10 with top form 3H² (the only degree-10 contribution to R² is H², at s⁰), so the product has degree>=10 or is zero, never cs^{36}g² of degree 2. Hence F≠0; F_0=A_{15}−H³=0 and F_{15}=0 give 1<=j<=14, deg F_j=15−j. H²∤F_j: for j<=5 a nonzero H²-multiple has leading monomial divisible by g⁶p⁴ (monomial order is multiplicative), contradicting normality; for j>=6, deg F_j<=9<10. Confirmed. The "H² at order 5 absorbed as R_0=1/3" remark is correct: quotient of H² by 3H² is 1/3, remainder 0.

Note (not a defect): the j=12 exclusion in §5–6 never uses normality or H²∤F_j; the normalization only makes j canonical. Ordinary total degrees 15/25 are those of (S), distinct from Moh's initial monic π-degrees; the proof keeps them apart.

## 4. All B kernels and the exact wedge — CONFIRMED

Degrees: b_{i,s}=b_is^{25−5i} has combined degree 25−5i, so every term of f_B is degree 25; q: R² (10), b_4R (5+5), b_3 (10), α (10); τ: b_2 (15), b_4α (15); δ: b_1 (20), b_3α (20), α² (20). Orders: α>=10, τ>=15, δ>=20 for all scalar values.

f_B' identity, my expansion: (3R²+α)q=5R⁴+4b_4R³+3b_3R²−(5/3)αR²+(5/3)αR²+(4/3)αb_4R+αb_3−(5/9)α²; adding τR+δ=2b_2R−(4/3)b_4αR+b_1−b_3α+(5/9)α² cancels the α-cross terms and leaves 5R⁴+4b_4R³+3b_3R²+2b_2R+b_1=f_B'. Confirmed.

Wedge: dA_s=(3R²+α)dR+dF; dB_s=(f_B'+q'F)dR+q dF+dG. dA∧dB=[(3R²+α)q−f_B'−q'F]dR∧dF+(3R²+α)dR∧dG+dF∧dG, and (3R²+α)q−f_B'=−(τR+δ). Directly from T=(3R²+α)G−(τR+δ)F−((5/3)R+(2/3)b_4)F²: [R,(3R²+α)G]=(3R²+α)[R,G]; [R,−(τR+δ)F]=−(τR+δ)[R,F]; [R,−((5/3)R+(2/3)b_4)F²]=−((10/3)R+(4/3)b_4)F[R,F]=−q'F[R,F]. So [A_s,B_s]=[R,T]+[F,G] exactly, retaining b_4,b_3,b_2,b_1,b_0 and α. Each T term has combined degree 10+25=35, (15 or 20)+... =35, 5+30=35. Confirmed.

ord G>=2j: G_0=H⁵−H⁵−0=0 (b_i have positive order, F has order>=1). If l=ord G<2j<=28<36, the order-l coefficient of (7) is [H,3H²G_l]: [F,G] has order>=j+l>l; (τR+δ)F has order>=15+j>2j since j<=14; the F² term has order>=2j>l. So 3H²G_l∈K[H], degree 35−l, forcing l∈{5,10,15,20,25} with G_l ∝ H⁴,H³,H²,H,1. Exact effects of b_i→b_i+e, my recomputation: b_4: f_B gains es⁵R⁴, q gains (4/3)es⁵R, τ gains −(4/3)es⁵α, δ unchanged, so G changes by −es⁵(R⁴+(4/3)RF); b_3: f_B gains es^{10}R³, q gains es^{10}, δ gains −es^{10}α, so G changes by −es^{10}(R³+F); b_2: −es^{15}R² (τ gains 2es^{15}); b_1: −es^{20}R (δ gains es^{20}); b_0: −es^{25}. Each change has order>=l, kills the leader at l, and τ/δ bounds persist. Finite: at most five sequential adjustments, ending with ord G>=2j or G=0 (needed when 2j>25, i.e. j=13,14). Not a target shear.

Order 2j: with ord G>=2j, T has order>=2j and T_{2j}=3H²G_{2j}−(5/3)HF_j² (the b_4 part of the F² factor enters at 5+2j; (τR+δ)F at >=15+j>2j; [F,G] at >=3j>2j; target at 36>2j). So [H,3H²G_{2j}−(5/3)HF_j²]=0, inner degree 10+25−2j=5+2(15−j)=35−2j. In K[H] this is nonzero only if 5|2j, i.e. j=5 (H⁵) or j=10 (H³); both are H²-multiples, so (5/3)HF_j²∈H²K[g,p] and H|F_j² in all cases. For H=p²L³ with p,L non-associate linear forms: p²|F_j² gives p|F_j; L³|F_j² gives 2·ord_L F_j>=3, so L²|F_j. Hence pL²|F_j, deg 3<=15−j, j<=12. This is the ⌈m/2⌉ rule for the actual multiplicities (2,3), not a rad(H) cover. At j=12, deg F_12=3 forces F_12=λpL², λ≠0. Confirmed.

## 5. Literal j=12 endpoint and signs — CONFIRMED

Inner degree 35−24=11, 5∤11, so 3H²G_24=(5/3)HF_12², i.e. G_24=(5/9)F_12²/H=(5/9)λ²p²L⁴/(p²L³)=(5/9)λ²L. Confirmed.

Order: [R,T]=[A_s,B_s]−[F,G]; the first has order 36 exactly, the second order>=12+24=36; hence ord_s[R,T]>=36>35=deg T. T is a polynomial (no division), combined-homogeneous of degree 35; R is combined-homogeneous of degree 5 with R(0)=H, centralizer K[H] by §2. The lemma gives [R,T]=0. T=0 is not asserted and not needed; the kernels b_4…b_0 are retained as whatever scalars the induction fixed.

Tail retention: F=s^{12}f_3+s^{13}f_2+s^{14}f_1 (F_15=0), G=s^{24}g_1+s^{25}g_0 with g_0 scalar. [F,G]=s^{36}[f_3,g_1]+s^{37}[f_2,g_1]+s^{38}[f_1,g_1] (all brackets with the scalar g_0 vanish). Coefficient equations: s³⁶: [f_3,g_1]=cg²; s³⁷: [f_2,g_1]=0; s³⁸: [f_1,g_1]=0. Only the first is used; the latter two are consequences of (13), not hypotheses, so nothing is assumed in advance.

Sign, my own computation: [p,L]=p_gL_p−p_pL_g=0−(1)(−1)=1; [pL²,L]=L²[p,L]+p[L²,L]=L². So [λpL²,(5/9)λ²L]=(5/9)λ³L², positive in the stated convention with A low. Then cg²=(5/9)λ³(p²−2pg+g²): the p² coefficient gives λ³=0, contradicting λ≠0; equivalently g=p=1 gives c=0, contradicting (S). Both roads close.

**Manual changed-object/sign controls (mine, hand-computed).**
(i) Convention swap [U,V]→−[U,V] (equivalently A↔B naming): both sides flip, c→−c and (5/9)→−(5/9); the mismatch L² vs g² is untouched. (ii) L→g−p (L_g=1,L_p=−1): [p,L]=−1, [pL²,L]=−L²; scalar sign flips, shape L² persists. (iii) Swapped multiplicity pattern H=p³L²: the same chain gives F_12=λp²L, G_24=(5/9)λ²F_12²/H=(5/9)λ²p, and [p²L,p]=(−p²)(1)−(2pL+p²)(0)=−p², so cg²=−(5/9)λ³p², again coprime shapes, again λ=0. (iv) Would-be consistent target: if (S) had Jacobian cL² instead of cg², (14) would read cL²=(5/9)λ³L² with the solution λ³=9c/5, showing the contradiction rests on coprimality of g² with the double-factor square, not on the scalar 5/9. These are honest manual checks; no automated mutation suite exists or is claimed.

## 6. Conditional Moh attachment and exact stopping scope — CONFIRMED as conditional

Inspected in the charged source `07e5…` §1–2 and its gate `eade…` §2: parent (125,75), M=(−75,105,123), d=(125,25,5,1), V=(2,4,1), u_s=1, v_s=4; Moh Prop 6.3 (via Prop 6.4's minor-radius hypothesis) gives P,Q∈K[γ,π] monic in π with π-degrees 25/15 and [P,Q]=−γ²/b; child datum (25,15;M2'=21,V2'=2;k=2), radii −1 and 7/5; simultaneous centering π→π+η(γ) (η=−[π¹⁴]Q/15), a common slope shear and a common constant translation, all determinant 1 and γ-fixing, so [P,Q]=cγ² persists and total degrees become exactly 25/15 with (1,1)-face tops H⁵,H³, H=π²S. In partition [3], S=(π−γ)³ after normalizing the nonzero slope to 1, so H=p²(p−g)³ under g=γ, p=π, and monicity makes the tops exactly H⁵,H³ (π²⁵,π¹⁵ coefficient 1). With A=Q, B=P, [A,B]=−[P,Q]=γ²/b≠0. So the [3]-stratum receiver satisfies (S) literally, and the initial π-degree statement of Prop 6.3(2) is kept distinct from the total degrees proved by centering. The proof's §1 states this correctly.

**External trust, stated exactly and not re-audited here:** (a) existence of an ordinary Keller pair with the named parent data is a hypothesis, not a fact; (b) Moh Props 6.3(1)–(3), 6.4 as printed on pp.197–199; (c) the child-data transport (25,15;21,2;2) accepted in the uncharged row2515 gate; (d) Def 5.1(1)/Prop 5.3 applied to the monomial-J child (named usage, Moh's own p.207 practice); (e) the outer-disc mean-centering lemma of the uncharged h-support gate §4, re-derived in the charged gate §2. Items (c)–(e) are outside the charged set and are consumed only at the accepted gate's named scope.

**Exact conclusion.** For every pair satisfying (S) over a characteristic-zero field, the canonical first-contact order satisfies j∈{1,…,11}; j=12 is impossible. Attached conditionally to the source map, this excludes only the canonical j=12 endpoint of the [3]-stratum (25,15) receiver of the named (125,75; M2=105) branch. NOT concluded: any of j=1…11, attainment of the [3] stratum by an actual parent, a reverse ordinary Keller lift, the [2,1] or [1,1,1] strata, the whole Moh 125 branch, all 15/25 pairs, all-degree JC2, scheme emptiness, radical/unit certificates, or properness of any chart ideal. No exit price is asserted and none is consumed.

## 7. Strongest valid scoped statement

The proof is correct at every numbered arrow as written. Its strongest valid content is the unconditional algebraic theorem: no A,B∈K[g,p] (char 0) with deg 15/25, tops H³/H⁵ for H=p²(p−g)³ and [A,B]=cg², c≠0, has canonical late-contact order 12; in fact the j=12 argument uses no normalization, so any reference decomposition F=A_s−R³−α_sR−a_0s^{15} with R(0)=H has ord_s F≠12. Everything beyond that is conditional on the named external trust and is not promoted here.

<!-- BODY-END -->
