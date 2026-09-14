# Independent hostile gate: uniform cone Jacobian degree bound (Fable 5.1)

tag=uniform-cone-jacobian-degree-gate-fable5-20260908. 2026-09-08 02:51–03:10 UTC.
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d (provenance only; no exit
price authored, no charge_basis). One <=25-minute LIGHT independent review.

**Verdict: all six targets CONFIRMED at the exact stated scope.** The proof in
uniform-proof.md is self-contained and, after my own re-derivation of every
universal step, I found no missing arrow. Two steps are stated tersely and were
supplied by me (uniqueness of the R_s-normal representation in §5, and the
positive (s,z)-order of implicit corrections carrying one Z per z in §6); both
are elementary and recorded below. The named scrutiny point ("z^5 cannot
cancel") closes by the global lower-Q0 argument, which I derive independently.
Twelve replay outcomes reproduce exactly. Nothing beyond the statement is
concluded: no JC2 receiver, no scheme/unit claim, no attachment.

## 1. Exact statement and read scope

Claim reviewed (exact-statement-and-scope.md): K any characteristic-zero
field, a,b>=1, D=a+b, 5b>4a+1; V(g,p) homogeneous of degree b, monic in g,
squarefree, p∤V; H=p^a V; w(g)=5, w(p)=-(5b-1)/a=-t; A,B in K[g,p] of total
degrees 3D,5D with top forms H^3,H^5 and w(A)<=3, w(B)<=5. Conclusion:
[A,B]!=0 implies deg_total[A,B]>=D+2.

Read perimeter: exactly the nine snapshot basenames under
/tmp/jc2-lane.TV2asS/inputs, each read whole, plus the launcher FALLACY text.
All nine sha256 values match PINS.json (verified before any proof work):

| basename | sha256 |
|---|---|
| PINS.json | b3b5ed1e4929de422c28775c8a66349b05c7b44b04ce3ccae45d2de59538164c |
| exact-statement-and-scope.md | eac423a25453972fd28e6181b44a5e904cec5f95652ea4183e790c841fef0196 |
| root-uniform-replay.json | c0482cbe441f0bf0b5b5491b900f5aea79bf04db751ee1046ab888c06ab03a1d |
| uniform-check.py | bf21db84db6fda0d1e98c102305505b18eab58ddc1ea6c86478fb15191efdec8 |
| uniform-custody.json | db898457ae232427fab4f69ec22dc718beff0391d5949cd4cd77c3daccfee5b5 |
| uniform-history-comparison-pins.json | 79586380c9e8a0c013fabdbc849ff636355bf0b0b61e105bf044b1f7803e91e7 |
| uniform-proof.md | 3bf207b31958cca8c4d5d1d0cf4ca4bacde0f7cd1ba267abc216a121675b7085 |
| uniform-replay.json | 6e5186908d56530cd4b3d79f0ba4ef7222fa227474b7a093c88243f65da12a2a |
| uniform-transaction.json | 0e11634e511e983d4a7c61773ad0e2c9a0affce46eeb668d46b9b452bd34268a |

Paths named inside custody/history/replay (four Astra reports, the producer
box) were treated as provenance and NOT opened. No agent, AWS/SSH, CAS, solver,
source stream, high H/R/A/B power, shared or protected edit, or peer blind
report was used. Root release and producer tests were not taken as proof.

## 2. Independent derivation, target by target

**T1 generic fibre / centralizer — CONFIRMED.** On H=h0 (h0 transcendental,
F0=K(h0)) p is a unit: p·(p^{a-1}V/h0)=1. With u=g/p, T=1/p, H=p^D V(u,1), so
the fibre ring over any extension F' of F0 is F'[u,T,T^{-1}]/(T^D-V(u,1)/h0)
(H-h0 = -h0 T^{-D}(T^D-V(u,1)/h0), units removed). Over Kbar, V=∏(g-λ_i p)
with the λ_i distinct (squarefree) and no p factor, so V(u,1)=∏(u-λ_i) has b
distinct roots, λ=0 allowed. Over F0bar=K(h0)bar the polynomial T^D-V(u,1)/h0 is
Eisenstein at (u-λ): constant term valuation 1, leading 1, middle 0; the Gauss
reduction (monic factors lie in the DVR, reduce to T^i·T^{D-i}, both constants
in (u-λ), product valuation >=2) is correct. So F0bar[u,T]/(…) is a domain, its
T-localization is a domain, and the generic fibre is geometrically integral.
Relative algebraic closure: a finite F1/F0 inside L=K(g,p) gives F1⊗F0bar ≅
F0bar^{[F1:F0]} (char 0) embedded by flatness into L⊗F0bar, a localization of
the domain; hence [F1:F0]=1. Derivation step: H_g=p^a V_g!=0 (b>=1, char 0),
d=[H,-]/H_g kills K(H), d(p)=1; p is transcendental over K(H) by transcendence
degree, so d restricted to K(H,p) is d/dp; L/K(H,p) is finite of degree <=b
(H(g,p)-H=0 has g-leading coefficient p^a). Differentiating the minimal
polynomial gives a lower-degree relation, so its coefficients are d/dp-constants,
i.e. in F0 (char 0); z is algebraic over F0, hence in F0. Bezout: q(H) a unit in
K[g,p] forces q constant. Homogeneous part of K[H] in degree e is K·H^{e/D} or
0. The reducible fibre H=0 is never used. No parity, nonzero-parameter or
algebraically-closed-base assumption enters.

**T2 A references and five B kernels — CONFIRMED.** A_s,B_s are combined-
homogeneous of degrees 3D,5D with w<=3,5; J_s=Σ s^{8D-2-e}J_e so M=8D-2-L0
>=7D-3 for L0<=D+1 (pure chain rule). At each r<=D the residual of A_s-R_s^3 is
divided by 3H^2 on the lex leader g^{2b}p^{2a}; every replacement term has
smaller g-degree, equal total degree and weight <=w(m) since all non-leading
monomials of H^2 have strictly smaller weight; quotient has degree D-r, weight
<=1; only 1 and 3 are inverted. Lower R terms have g-degree<b: g-degree>=b forces
p-degree<=a-1 and weight >=5b-t(a-1)=1+t>5>1. So the g-leader of R_s is
exactly g^b p^a with coefficient p^a and no s-correction. At order 2D the
degree-D residual has a single monomial divisible by g^b p^a, so the quotient
is the scalar α and F_{2D}=residual-αH is normal; α_s R_s only touches orders
>=2D and a0 s^{3D} kills the constant F_{3D}; earlier normalities are untouched.
F=0 gives J=(3R_1^2+α)[R_1,B] at s=1 with degree >=2D>D+1 or J=0; both
contradict. Hence 1<=j<=3D-1 and 2j<=6D-2<7D-3<=M (D>=3 since a=1 forces b>=2).
Kernel division: I expanded (3R^2+α)q with q=(5/3)R^2+(4b4/3)R+b3-5α/9 and got
5R^4+4b4R^3+3b3R^2+(4b4α/3)R+b3α-5α^2/9; adding τR+δ with τ=2b2-(4/3)b4α,
δ=b1-b3α+5α^2/9 gives f_B' exactly. Identity (5): wedge coefficients of
[f_A(R)+F, f_B(R)+q(R)F+G] are -(τR+δ)-q'F, 3R^2+α, 1 on dR∧dF, dR∧dG, dF∧dG;
those of [R,T]+[F,G] with T as displayed are ∂T/∂F=-(τR+δ)-((10/3)R+(4/3)b4)F,
∂T/∂G=3R^2+α, and 1. They agree, with q'=(10/3)R+(4/3)b4 carrying b4. Kernel
induction: for the first nonzero G_l with l<2j, ord(τRF)>=3D+j>l needs j<=3D
(true), ord(RF^2)=2j>l, ord(b4F^2)=D+2j>l, ord[F,G]>=j+l>l, so [H,3H^2G_l]=0 and
G_l∈K[H] homogeneous of degree 5D-l, forcing l∈{D,…,5D} with leaders H^4,…,1
(G_0=0). The five displayed increments are exact, change only orders >=l, and
move τ,δ only at orders 3D,4D; processing l increasingly ends with ord G>=2j or
G=0. F=0, α=0, zero scalar references, and G=0 are all covered.

**T3 tentative orders, H-divisibility, strict t>4 — CONFIRMED.** Starting from
j<=3D-1: at order 2j, [F,G] has order >=3j>2j, (τR+δ)F order >=3D+j>2j since
j<3D, b4F^2 order D+2j, ord G>=2j, and every term of T has order >=2j, so
[R_s,T]_{2j}=[H,T_{2j}] with T_{2j}=3H^2G_{2j}-(5/3)HF_j^2 of degree 7D-2j
>=D+2>D. Any homogeneous centralizer element of that degree is c·H^k with
k=(7D-2j)/D>1 hence k>=2, or 0; so H^2|T_{2j} and H|F_j^2. V squarefree gives
V|F_j (H itself is not squarefree when a>=2; the proof correctly uses V).
Weight additivity for the max-weight grading (top forms multiply nonzero in a
domain) gives w(Q)<=3-5b for F_j=VQ; a monomial of Q with p-exponent <=a-1 has
weight >=1-5b+t>3-5b because t>2; so p^a|Q and H|F_j. j=2D forces scalar C
against F_{2D} normality; j>2D forces deg F_j<D so F_j=0. Thus 1<=j<=2D-1,
C!=0, deg C=2D-j>0, w(C)<=2. g-degree: for j<=D, H^2-normality plus weight
2+t>3 excludes g-degree>=2b; for D<j<2D, deg F_j<2D alone gives p-degree<=2a-1
and the same weight excess. So deg_g C<=b-1 and V∤C. Nothing about
irreducibility of V, real or simple coefficients, or parity is used.

**T4 finite normal blocks / product injection — CONFIRMED.** Division by R_s on
the leader g^b p^a (coefficient p^a, no s) terminates by g-degree, preserves
combined degree, never raises weight (all R_s monomials have weight <=1) and
never lowers s-order. F has (g,p)-degree <=3D-1 since ord F>=1, so the third
quotient would have negative degree: P0+R_sP1+R_s^2P2 exactly; G with ord G>=2
gives Q0..Q4. Weights 3-i and 5-i follow from the leader weight 1. The normal
representation is unique: if P0=-R_s(P1+R_sP2) with P0 normal, the lex leader
of the right side is g^b p^a·LM(P1+R_sP2), a forbidden monomial, so
P1+R_sP2=0 and then P2=0 (this step is implicit in the proof; I supplied it).
Hence at order j the s^j-coefficient (P0)_j+H(P1)_j+H^2(P2)_j equals HC with C
normal (deg_g C<b), so (P0)_j=(P2)_j=0, (P1)_j=C, q0=ord P0>j (∞ allowed).
Normal weight<=5 polynomials have g-degree<b (else weight >=1+t>5, the strict
hypothesis). Restriction g↦λp into ∏_λ Kbar(p) over all b distinct λ is
injective because a g-polynomial of degree <b over the domain Kbar[s,p] cannot
have b distinct roots λp; injectivity is a product statement and λ=0 is allowed.
Implicit function: R_s(λp,p)=O(s) and R_{s,g}(λp,p)|_{s=0}=p^{D-1}V'(λ)!=0
(simple root), so R_s(X,p)=z has a unique solution X=λp+Y with Y in
(s,z)Kbar(p)[[s,z]]; later coefficients may have poles at p=0, harmless in the
field Kbar(p). η=min(j/2,q0/3) satisfies j/3<η<=j/2<=D-1/2, h=D-η>0. The
combined degrees are direct: u=C(λp,p)=p^{2D-j}C(λ,1) has degree 2h when j=2η,
v=(P0)_{q0}(λp,p) has degree 3D-q0=3h when q0=3η; no diagonal constant field
and no regularity of later coefficients is assumed. F<=3D-1 and G<=5D-2 give
exactly block powers 2 and 4.

**T5 every B initial term, no lower dZ, target order >=M — CONFIRMED (the
named scrutiny point closes).** After z=s^ηZ, the orders are: z^5 → 5η with
coefficient exactly Z^5 (z is the variable, no correction); b_i z^i →
(5-i)D+iη=5η+(5-i)h>5η; (5/3)z^2F → >=5η, equal only through
(5/3)Z^2(uZ+v); the b4,b3,α parts of qF → >=D+4η, 2D+3η >5η; z^iQ_i (i>=1) →
>=iη+2j>=5η; Q0 → >=2j>=4η, possibly below 5η. Implicit corrections: a
correction from block s^r z^i multiplies by Y-monomials each carrying one z per
Z, so a Z^5 term from any block with i<=4 has order >=r+5η with r>=ord(block)
>0, strictly above 5η; hence the Z^5 coefficient at 5η is 1 on every component
and the global order ν satisfies ν<=5η. Global lower-Q0 argument, derived
independently: let ν0=ord Q0 (an integer or ∞). On every component,
Q0(G_λ,p)=Σ_r s^r[(Q0)_r(λp,p)+O(Y)] with corrections of order >r; nothing else
lives below 5η. If ν0<5η the global minimum is exactly ν0, attained on a
component where (Q0)_{ν0}(λp,p)!=0, which exists by the product injection
(w(Q0)<=5, normal); its initial e_λ=c_λ p^{5D-ν0} is Z-free with 5D-ν0>0. The
(z,p)-bracket has candidate leading term s^{2η+ν0}(P_Z e_λ' - P_p·0) whose Z^2
coefficient is 3e_λ'; with 2η+ν0<7η<=7D-7/2<7D-3<=M this coefficient must vanish
on every component (the transformed bracket equals J_s(G_λ,p)/R_{s,g}(G_λ,p)
with unit denominator and order at least M, vanishing of J's leading form on
components only raising the order). So e_λ'=0, and positive p-degree forces
c_λ=0 on every component, contradicting the nonzero component. Therefore
ν0>=5η, ν=5η, and only then are later implicit Q0 corrections irrelevant at
5η. The 5η initial on each component is Z^5+(5/3)uZ^3+(5/3)vZ^2+wZ+x (w from
Q1 if η+ord Q1=5η, x from Q0 if ν0=5η), monic, no Z^4 (R_s^2P2 inside qF has
order >=4η+j+1>5η, Q4 has order >=8η, b4z^4 has order D+4η), homogeneous of
degree 5h with p-degrees 2h,3h,4h,5h integral whenever nonzero. [P,Q]_{Z,p}=0
follows at order 7η<M. The old nonodd review was not cited.

**T6 Euler/UFD lemma and exact bound — CONFIRMED.** From pP_p=mhP-hZP_Z and
pQ_p=nhQ-hZQ_Z, p[P,Q]=nhP_ZQ-hZP_ZQ_Z-mhPQ_Z+hZP_ZQ_Z=h(nP_ZQ-mPQ_Z) for any
m,n and any h. With [P,Q]=0, h!=0 (p!=0 in F(p)), (Q^m/P^n)_Z=
Q^{m-1}P^{n-1}(mQ_ZP-nP_ZQ)/P^{2n}=0, so Q^m/P^n∈F(p) (constants of d/dZ in
F(p)(Z), char 0), equal to 1 by comparing monic leaders of degree mn. In the
UFD F(p)[Z], m·v_π(Q)=n·v_π(P) gives v_π(P)=m'k_π, v_π(Q)=n'k_π with
m'=m/d, n'=n/d; W=∏π^{k_π} is monic of degree d. For 3/5, W=Z+r and the zero
Z^2 coefficient gives 3r=0, r=0 (char 0), componentwise, so u=v=0 on every
component against T4/T5. Countercontrols hold: h=0 with P=Z^3+1,Q=Z^5 commutes
with zero Euler degrees and Q^3!=P^5 at Z=0; gcd 2 with W=Z^2+p^2, m=6,n=10
commutes by the chain rule and W is quadratic (no degree 6/10 expansion). The
contradiction used L0<=D+1 only through M>=7D-3 in the strict margin (12), so
it proves exactly deg J>=D+2 for nonzero J; commuting pairs (J=0) escape at the
F=0 step, and at L0=D+2 the margin 7η<=7D-7/2 versus M=7D-4 fails, so D+2 is
not excluded. No JC2, D125, unit or certificate conclusion is drawn.

## 3. Replay (direct prlimit + subprocess timeout=30, no GNU timeout)

Checker byte-copied unchanged to own scratch (sha256 bf21db84…). Driver
replay_driver.py ran the six modes normally and with -O, argv
`/usr/bin/prlimit --cpu=25:25 --as=536870912:536870912 -- /usr/bin/python3 -I -B [-O] <scratch>/uniform-check.py <mode>`,
cwd=scratch, elapsed 3.28 s total.

| mode | rc (normal, -O) | stdout | stderr last line |
|---|---|---|---|
| positive | 0, 0 | bytes identical to uniform-replay.json; sha256 bd5d9f31ff843dfd8cb2a4b9188071ef9be1921e8970c2fb7524fda83f1bf606 = root record | empty |
| --omit-b4 | 1, 1 | empty | ValueError: all-five-kernel derivative division |
| --omit-b2 | 1, 1 | empty | ValueError: all-five-kernel derivative division |
| --wrong-euler-sign | 1, 1 | empty | ValueError: universal weighted Euler bracket identity |
| --false-h0 | 1, 1 | empty | ValueError: h-zero forbids power conclusion |
| --false-gcd-one | 1, 1 | empty | ValueError: gcd-two retains quadratic common factor |

All twelve rc, stdout bytes and error messages match the producer record and
root's stdout hashes; traceback path digests were not compared. Distinction:
--omit-b4, --omit-b2 and --wrong-euler-sign are actual algebraic mutations
(they change q, τ, or identity (14) and are rejected by the identity checks);
--false-h0 and --false-gcd-one are false-inference countercontrols on the
concrete h=0 and gcd=2 objects, not mutations of the proof algebra. Limits: the
checker stops at its first failed need(), so the two omit modes never reach the
bracket identity (5); the five (a,b) scalar rows illustrate inequalities only.

## 4. Independent changed-object attack (attack.py, exact Fractions, degree<=5)

- **Injection sharpness (T4).** The normal polynomial p^{a-1}V restricts to
  zero on every V component and has weight exactly 1+t. At the boundary rows
  (1,1), (6,5), (11,9) it is a weight-5 kernel element, so injection (9) fails
  there for every boundary (a,b), not only a=b=1; at in-scope rows (1,2),
  (2,2), (2,3), (3,3) its weight 1+t exceeds 5. The hypothesis 5b>4a+1 is
  exactly the injectivity condition at weight 5, which is the weight Q0 can
  reach. At (2,2) with V=g^2-p^2 no normal weight<=5 monomial has g-degree>=2
  and the Vandermonde determinant is -2, so injection holds.
- **Lower-Q0 step (T5).** With P=Z^3+p^2Z (h=1) and Z-free e=p, p^2 the
  bracket equals P_Z e' with Z^2 coefficients 3, 6; the changed object e=1
  (p-degree 0) gives bracket 0 and is NOT excluded, so the positive degree
  5D-ν0>0 is load-bearing; a Z-carrying e=Zp gives 3Z^3-p^2Z, not of the form
  P_Z e', confirming why Z-freeness of the raw restriction is needed.
- **Euler lemma consistency (T6).** For P=Z^3+p^2Z, EP=3P, no scalar c makes
  Q=Z^5+(5/3)p^2Z^3+cp^4Z commute (residual -20/3 p^3Z^3 + c(12p^3Z^3+2p^5Z),
  ratios 0 and 5/9 inconsistent), consistent with W^3=Z^3 being forced.
- **Margin (12).** Six rows show 7η_max<7D-3 strictly and 7η_max>7D-4, so the
  bound is D+2 exactly as claimed and not D+3.

These probes are degree<=5 sanity checks of load-bearing steps; the universal
claims rest on the derivations in Section 2, not on the probes.

## 5. Output pins (box/uniform-cone-jacobian-degree-gate-fable5-20260908/)

| file | sha256 |
|---|---|
| scratch/uniform-check.py (byte copy) | bf21db84db6fda0d1e98c102305505b18eab58ddc1ea6c86478fb15191efdec8 |
| replay_driver.py | 0aa8001c6d0289b381e1d962eea6a898e563d26c45e1618a074d27896232f042 |
| replay-fable5.json | 8324b565e5321081eff18ac25ece40937fc4773c1b23384b5b5f80838b008801 |
| attack.py | ae9cf3f88b986661b46eb26f289afcee390db52c0581aed32b80252c45a6c2dc |
| attack.out (rc 0) | 3656cf8d19badb99bd09e4a51406b038ec1ca440231c5b5c1577790abaec670b |
| attack.err (empty) | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

## 6. Failed claims, exceptions and limits

- No claim in the proof failed. No REFUTED or GAP target.
- Retained exceptions: the statement is a degree floor for nonzero J only;
  J=0 pairs exist (A=H^3, B=H^5); degree D+2 itself is not excluded; the
  boundary t=4 and repeated V are outside scope and the injection fails there.
- Producer text gaps filled by the reviewer, both elementary: uniqueness of
  the R_s-normal block representation (used for (P1)_j=C), and the explicit
  "one Z per z inside Y" order accounting that makes the Z^5 coefficient at 5η
  exactly 1.
- Not verified here: any actual JC2 receiver meeting the hypotheses, any
  scheme-level or unit-certificate statement, any D125/common/golden
  attachment. None is claimed by the proof or by this gate.
- Tiny controls are degree<=5 and cannot test universal quantifiers; the
  checker's mutation modes stop at the first failed identity.

All children terminal (replay_driver.py, attack.py; rc 0, within 30 s/25 CPU/
512 MiB). No new agents, AWS/SSH, CAS, solver, source expansion, shared or
protected edits. STOP/IDLE.

<!-- BODY-END -->
