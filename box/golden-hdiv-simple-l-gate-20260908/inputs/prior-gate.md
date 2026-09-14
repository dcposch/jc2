# Independent Fable gate: whole golden non-H-divisible source composition

2026-09-08. Tag golden-nonh-composition-gate-fable5-20260908. Frozen basis
0d39df3c9fd69c939a8420c54d03228b9077777d. LIGHT hostile mathematical review of
the two-arrow composition (source-proof.md then consumer-proof.md). THIS
REPORT IS A REVIEW, NOT A PROMOTION. No live report, peer submission, mutable
ledger, AWS/SSH, CAS, solver, protected jc2-lean file, new agent, shared edit
or external channel was touched. Old accepted foundations (the minimal receiver
composition supplying system (S), the nonodd producer, the divisibility
control) were not re-reviewed; they enter only as the literal hypotheses (S).

## 0. Verdict

The composed argument is CONFIRMED at its literal scope. For the system (S)
of source-proof.md Section 1 (characteristic-zero field K containing a root
rho of rho^2-3rho+1, t=1-rho, L=p+g, M=p+tg, H=p^2LM^2, Delta=pLM, deg A=15,
deg B=25, A_15=H^3, B_25=H^5, w(g)=5, w(p)=-7, w(A)<=3, w(B)<=5,
[A,B]=c g^2, c!=0), with the A-only canonical reference F of source Section 2,
the first nonzero correction F_j satisfies H | F_j. The non-H-divisible
alternative is excluded in full and without any parity hypothesis. All six
targets below are CONFIRMED; no target is REFUTED; no GAP was found inside the
declared scope. First missing arrow: NONE inside scope. Outside scope (not
excluded by either report and not claimed here): the H-divisible branch
F_j=HC (source Section 7 bounds it to j<=9, deg C>=4 when C vanishes on both
reduced lines, and leaves the other C alternative open), any golden pair not
satisfying (S) literally, common polygons, whole D125, nilpotent source
algebras, reverse-lift equations and JC2. No all-degree coverage is claimed.

## 1. Read and pin evidence

All ten charged inputs were read WHOLE from the immutable lane basenames in
/tmp/jc2-lane.mRFR0l/inputs. Their SHA-256 values, recomputed at 22:33 UTC,
equal the box copies under box/golden-nonh-composition-gate-20260908/ and the
PINS.json entries (status FROZEN_ROOT_CHECKED_NOT_PROMOTED). The seals of both
proofs agree with their transaction JSONs (body 17824 B / 0c59263b..., body
10031 B / c2bc73bf...). Custody history paths named in PINS/custody were
treated as provenance only and were not opened.

| lane basename | sha256 |
|---|---|
| PINS.json | `5fb7ad6de6810b019b6d32fa64b9ae2ff574fa4ed702098f9a150061ebc1fd12` |
| source-proof.md | `14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6` |
| source-transaction.json | `a80659d8c6b38fd4800b7eb70b650af57a0065e0c67b077f2878c1c24377c8af` |
| source-custody.json | `fcc12304ee659dc5b83eb8f5e323a8c38a7cf3616e6a4b2f4b53cd1ca438568d` |
| source-check.py | `e49907ee44870195b3d437ea7b095619ecd9f6bc315702dc6932cfe7937687f8` |
| source-replay.json | `422c6258cbad8674d0138d360bfb82702a69939237c1d3cbe8f6e78369037c4f` |
| consumer-proof.md | `1770c414adacb5f8a60438ed3379b3e39969c50e247cee2e5e898acc689f3c8f` |
| consumer-transaction.json | `aec7cfe1801ec0b6b45855f2ab263289d2a6e1f9852f781905f07b400725a3c0` |
| consumer-check.py | `b47cffd1436080d8f32e925b94160361d6a781047d755b6ad2c387c47717a47b` |
| consumer-replay.json | `afda7aeeb7ddecddbe528693d475b020f71b23e7c2f42ff07df2731be19e716b` |

## 2. Target 1: source reference and kernel induction. CONFIRMED

Centralizer. On the fibre H=h0 with u=g/p, T=1/p one has
T^5=(1+u)(1+tu)^2/h0. At u=-1 the factor 1+tu equals 1-t=rho!=0, so u+1
divides the right side exactly once; Eisenstein at the prime u+1 of
Kbar(h0)[u] makes T^5-(1+u)(1+tu)^2/h0 irreducible, hence the generic fibre
is geometrically integral and K(H) is relatively algebraically closed in
K(g,p). The repeated factor M^2 is never treated as squarefree: only the
simple L root is used. The derivation d=[H,-]/H_g satisfies d(H)=0, d(p)=1,
so on K(H,p) it is d/dp; applying d to the minimal polynomial over K(H)(p) of
a rational constant C shows every coefficient is d/dp-constant, i.e. lies in
K(H); C is algebraic over K(H), hence in K(H); Bezout then gives
K(H) cap K[g,p]=K[H], and a homogeneous element of K[H] is a scalar H-power.
Re-derived and correct.

References. A_s=sum s^(15-d)A_d gives [A_s,B_s]=s^38 c(g/s)^2=c s^36 g^2.
Division of the order-r A residual (r=1..5) by 3H^2 with leading monomial
3rho^2 g^6p^4 (unit 3rho^2) produces R_(5-r) of degree 5-r and weight<=1;
a weight-1 monomial g^ap^b needs 5a-7b=1, whose only solution of degree<=5
is (3,2) (attack 3), so every lower component has g-degree<=2 and R_s is
cubic in g with fixed leading coefficient rho p^2. alpha (order 10, degree
5, removes the single g^3p^2 monomial of F_10) and a0 (order 15, constant)
are the only remaining scalar references; F!=0 because otherwise
3R_s^2+alpha s^10 (degree 10, not a monomial) would divide c s^36 g^2 in the
UFD K[s,g,p]. So 1<=j<=14 initially.

Identity (2). Expanding [R^3+alpha R+a0+F, f_B(R)+q(R)F+G] with
[phi(R),psi(R)F]=phi'(R)psi(R)[R,F] gives the [R,F] coefficient
(3R^2+alpha)q-f_B'-q'F; the first two terms cancel to -(tau R+delta) with
tau=2b2-(4/3)b4 alpha, delta=b1-b3 alpha+5alpha^2/9, and q'=(10/3)R+(2/3)b4
equals twice the F^2 coefficient in T. I re-expanded this by hand; (2) is
exact, and no b4 or alpha term is dropped.

Induction. For m=ord G<2j (2j<=28<36 and 2j<15+j for j<=14) the order-m part
of [R,T]+[F,G] is 3H^2[H,G_m], so G_m is a homogeneous centralizer element
of degree 25-m: zero unless m in {5,10,15,20,25}, where it is eH^4..e.
Re-choosing b4,b3,b2,b1,b0 subtracts e s^5(R^4+(4/3)RF), e s^10(R^3+F),
e s^15R^2, e s^20R, e s^25 from G, touches no lower order, and moves tau,
delta only at orders>=15,>=20. Each b_i is consumed at most once, so the
process ends with ord G>=2j. At order 2j the only surviving terms are
3H^2G_(2j) from (3R^2+alpha)G and -(5/3)HF_j^2 from the F^2 term (tau R F
sits at >=15+j>2j, [F,G] at >=3j), so 3H^2G_(2j)-(5/3)HF_j^2 is a
centralizer element of degree 35-2j: zero, or eH^5 at j=5, or eH^3 at j=10.
All are divisible by H^2, hence H | F_j^2. Since p, L, M are distinct primes
(t!=1, t!=0), p^2LM^2 | F_j^2 gives only Delta=pLM | F_j, so 15-j>=3, j<=12.
Normal blocks: division by R_s (leading monomial g^3p^2 in lex g>p>s, all
other monomials of lower g-degree, weight<=1) terminates, never lowers
s-order, keeps combined homogeneity, and the (g,p)-degree bounds 14, 9, 4
force P3=0 and P2 automatically normal; weights 3,2,1. A normal monomial
g^ap^b with a>=3 has b<=1 and weight>=8>3, so deg_g P0_j<=2. If H does not
divide F_j then P0_j!=0, Delta | P0_j (subtracting H-multiples), and
P0_j=Delta*C with deg_g C=0, C=lambda p^(12-j), lambda in K*. Exactly (4).
Its g-derivative at g0=-p/t is lambda(t-1)p^(14-j)!=0, exactly (5). No
oddness is used anywhere. Non-load-bearing remarks: the H^2-normality of
orders 1..5 and deg_g F_j<=5 are not used by the later argument; the
load-bearing normality is P0's R_s-normality.

## 3. Target 2: moving critical point and Morse coordinate. CONFIRMED

H(g0+w,p)=p^2(p-p/t+w)(tw)^2=t(t-1)p^3w^2+rho p^2w^3 (attack 5 verifies the
w^2 and w^3 coefficients in both embeddings through degree<=3 factors). Since
H_gg(g0)=2t(t-1)p^3 is a unit of K(p), the formal implicit function theorem
gives the unique g_c in K(p)[[s]] with g_c(0)=g0; simultaneous scaling of
(s,g,p) and uniqueness make g_c combined-homogeneous of degree 1, so its
s^n coefficient is a Laurent monomial c_n p^(1-n). Because the g^3
coefficient of R_s is the constant rho p^2, Taylor expansion at g_c is
exactly (7): xi_s+w^2(a_s+rho p^2w), a_0=t(t-1)p^3. Over E=Kbar(p^(1/2))
with sqrt(a_0)=a p^(3/2), a^2=t(t-1)!=0, the unit a_s+rho p^2w has a formal
square root in E[[s]][[w]], zeta=w*sqrt(...) has invertible linear
coefficient a p^(3/2), and the inverse w_s(zeta) has coefficients in
E[[s]]: nonnegative s-orders, Laurent p-monomials, p-poles harmless. (8)
R_s=xi_s+zeta^2 is exact. Degrees: xi_s 5 (xi_kappa has integer p-degree
5-kappa), a_s 3, zeta 5/2, so an s^r zeta^n coefficient of P0 has p-degree
15-r-5n/2. In (9), theta_s=P0(g_c,p) has order>=j+1 because
P0_j(g0,p)=lambda p^(12-j)Delta(g0,p)=0 (M(g0)=0); ell_s=P0_g(g_c,p)/
sqrt(a_s) has exact order j with ell_j=lambda(t-1)p^(25/2-j)/a!=0; every
d_(n,s) has order>=j. Infinity orders, the earlier-constant control
R_s=H(g+s,p) with P0_10=p^2Delta giving -(t-1)p^4s+tp^3s^2 (q0=11=j+1), all
later coefficients and the p-poles are all retained. CONFIRMED.

## 4. Target 3: coalesced regime and q0<=3kappa. CONFIRMED

Regime A (kappa>=2j/5), r=min(j/5,q0/6), 0<r<=12/5<5/2, zeta=s^rY. Orders
(every one re-derived, and every inequality enumerated by attack 1 over
26,814 triples with zero violations): R_s at 2r with initial Y^2+b, b!=0
only if kappa=2r; F initial at 6r equals uY+v with u=ell_j[j=5r],
v=theta_q0[q0=6r], at least one nonzero by the choice of r, distinct
Y-degrees; d_n zeta^n at >=j+2r>=7r; R P1 at >=7r; R^2P2 at >=9r;
alpha R at 10+2r>6r; a0 at 15>6r. B: b_i R^i at 10r+(5-i)(5-2r)>10r;
(4/3)b4 s^5RF at 5+8r>10r; b3F, alphaF at 10+6r>10r; G at >=2j>=10r with
initial the constant e=G_(2j)(g0,p) in E when 2j=10r (both g_c-g0 and
w_s(s^rY) have positive order). So (10) and (11) are the exact initials, both
monic over the field E. Bracket order: [A,B]_(Y,p)=s^r[A,B]_(zeta,p)=
c s^(36+r)g^2 g_zeta, while the initial bracket sits at 6r+10r; in the zeta
chart this is 15r against 36 (attack 1 endpoints: 33 at j=11, 35 at
j=12,q0=14, 36 at j=12,q0>=15). Y has combined degree h=5/2-r>0 and P,Q have
Euler degrees 6h,10h (b has degree 2h, u 5h, v 6h, e 10h, all consistent).
Euler lemma (Section 4 of the source): the monomial identity
[Y^ip^al,Y^jp^be]=(i be-j al)Y^(i+j-1)p^(al+be-1) with al=(m-i)h, be=(n-j)h
gives i be-j al=h(in-jm), so p[P,Q]=h(nP_YQ-mPQ_Y) by bilinearity; [P,Q]=0
then makes Q^m/P^n Y-constant, monicity gives Q^m=P^n, and UFD in E[Y]
gives P=W^3, Q=W^5 with W monic quadratic. Common quadratic in prose only:
W=Y^2+al Y+be has W^3 with Y^5 coefficient 3al and, once al=0, Y^4
coefficient 3be; P has Y^5 coefficient 0 and Y^4 coefficient 3b, so W=Y^2+b,
W^3=(Y^2+b)^3 and uY+v=0. Independent confirmation without the UFD step for
b=0 (attack 2, monomial-pair bracket of the 3-term P and 4-term Q): the Y^3
row is -40h v^2, the Y^0 row is e u, the Y^5 row is 6e-(10/3)u^2, so v=0
then u=0. Hence j<=11 fails (15r<=3j<=33) and j=12 with q0<=14 fails
(r=q0/6, 15r=5q0/2<=35). At j=12, q0>=15, kappa>=5 (integer form of
kappa>=24/5) the bracket order is exactly 36 and equals the nonzero target;
the source correctly refuses to call this commutation. The q0<=3kappa
subcase of regime B: r=q0/6 gives 2r<=kappa, r<j/5, the same coalesced
initials with only v!=0 and e=0 (G strictly later), and 15r=5q0/2<3j<=36 by
q0<=3kappa<6j/5; the W=Y^2+b argument kills v. CONFIRMED. No W^3, W^5,
degree-6 or degree-10 power was computed anywhere in this gate.

## 5. Target 4: separated sheets. CONFIRMED

Regime B, kappa<2j/5 (so kappa finite, and empty for j<=2), q0>3kappa
including q0 infinite. Roots zeta_pm=pm sqrt(-xi_s) of order kappa/2, leading
values in E since xi_kappa=xi p^(5-kappa). On the two sheets the constant
term of F is theta_s pm ell_s sqrt(-xi_s)+sum d_n zeta_pm^n with global
minimum nu=min(q0,j+kappa/2): the d_n part is at >=j+kappa>nu, and on a tie
the two leading values theta pm ell_j sqrt(-xi_kappa) cannot both vanish in
characteristic zero (ell_j sqrt(-xi_kappa)!=0). nu>3kappa holds because
q0>3kappa and j+kappa/2>3kappa iff kappa<2j/5. With eta=nu/3>kappa and
z=R_s=s^eta Z, the sheet expansion (14) sqrt(1-z/xi_s) is legitimate: its
Z^k term carries s^(k(eta-kappa)), positive. Implicit corrections: the
ell-linear correction sits at j-kappa/2+eta>3eta iff j>5kappa/2 (regime B);
d_n corrections at >=j+eta>3eta iff j>2eta, true since 2eta<=2(j+kappa/2)/3<j
iff kappa<j. R P1 at >=eta+j>3eta, R^2P2 later, alpha R at 10+eta>3eta and
a0 at 15>3eta since eta<2j/5<=24/5<5. B side: b_i R^i at 5eta+(5-i)(5-eta),
b4 s^5RF at 5+4eta>5eta, b3F at 10+3eta>5eta, and every G term at >=2j>5eta
since 5(j+kappa/2)/3<2j iff 5kappa/2<j. So on each sheet P=Z^3+v_pm,
Q=Z^5+(5/3)v_pm Z^2, with (v_+,v_-) a nonzero tuple. Target in the (z,p)
chart: c s^36 g^2 g_zeta/(2zeta), order 36-kappa/2 with nonzero leading
coefficient. Initial bracket order 3eta+5eta-eta=7eta, and
7eta<=7(j+kappa/2)/3<36-kappa/2 iff 7j+5kappa<108, implied by
7j+5kappa<9j<=108. Euler weight h=5-eta>0, degrees 3h,5h; the depressed
cubic forces W=Z and v=0. Independent confirmation without UFD (attack 2):
[Z^3+v p^(3h), Z^5+(5/3)v p^(3h)Z^2]=-10h v^2 Z p^(6h-1), nonzero for
h!=0, v!=0. The contradiction lives on the sheet with v_pm!=0; on a sheet
with v_pm=0 the initials (Z^3,Z^5) commute and nothing is forced, which is
why the global nonzero tuple must be established before a component is
chosen. Source wording "both v components vanish" should read "the nonzero
component vanishes"; harmless. Endpoints: q0 infinite gives nu=j+kappa/2;
kappa=1 at j=5 (only B value there) gives nu=min(q0,11/2), eta<=11/6>1,
7eta<=77/6<71/2; j=12, kappa=4, q0=13 gives 7eta=91/3<34. Attack 1 finds
zero violations over kappa<=40, q0<=60 and infinity, and every inequality is
affine in (j,kappa,q0) with the stated direction, so the enumeration is a
control and the prose is the proof. CONFIRMED.

## 6. Target 5: resonant source-to-consumer map. CONFIRMED

At j=12: P1 has combined degree 10 and s-order>=12, P2 degree 5 and
order>=12, so P1=P2=0 and F=P0 (equivalently F has (g,p)-degree<=3<5 and is
already normal); theta_s of the source and F(g_c,p) of the consumer agree.
Delta | F_12 with deg F_12=3 gives F_12=lambda Delta, lambda!=0. The
consumer's Section 1 data (R_s with lower g-degree<=2, alpha s^10, a0 s^15,
b_i s^(25-5i), q_s, ord G>=24, combined degree 25, (R) kappa>=5, q0>=15,
zero series infinite) are exactly the source's outputs; alpha, a0, b_i may
vanish and nothing divides by them or by c. Independent derivation: with
zeta=s^(12/5)Y, R_s=xi_s+s^(24/5)Y^2 has initial Y^2 at 24/5 because
kappa>=5>24/5; F: ell_s zeta at 12+12/5=72/5 with coefficient
k p^(1/2), k=lambda(t-1)/a, from (5) divided by a p^(3/2); theta at >=15>72/5;
d_n zeta^n at >=12+24/5=84/5; alpha R at 74/5; a0 at 15; R^3 at 72/5 with
Y^6. So P=Y^6+k p^(1/2)Y at 72/5 exactly, no extra initial coefficient. B:
R^5 gives Y^10 at 24; (5/3)R^2F gives (5/3)k p^(1/2)Y^5 at 48/5+72/5=24;
b_iR^i at 25-i/5>24; b4 s^5RF at 121/5; b3F, alphaF at 122/5; G_24 is
homogeneous of degree 1 and restricts at g0 to e p, e in K, corrections
positive; G_25 at 25. So Q=Y^10+(5/3)k p^(1/2)Y^5+e p at 24 exactly. Target:
c s^36 g^2 g_zeta has order-36 coefficient c(p/t)^2/(a p^(3/2))=
c p^(1/2)/(t^2 a), Y-independent and nonzero; initial bracket order
72/5+24-12/5=36, so [P,Q]_(Y,p) equals that constant exactly. Monomial-pair
bracket (attack 2, six pairs, no power expanded): Y^10 row (3q-5)k p^(-1/2)
vanishes iff q=5/3; Y^5 row 6e-(10/3)k^2; constant row e k p^(1/2); no
other row. Hence e=5k^2/9 and c=e k t^2 a=(5/9)k^3t^2a=
(5/9)lambda^3(t-1)^3t^2/a^2=(5/9)lambda^3 t(t-1)^2. Replacing a by -a flips
k and the target reciprocal together, so c is unchanged; both rho embeddings
are handled by the same formal identities. CONFIRMED.

## 7. Target 6: weighted faces and scope. CONFIRMED

Slots (attack 3): 5i-7j=3 with i+j<=15 has exactly (2,1),(9,6); 5i-7j=5
with i+j<=25 has exactly (1,0),(8,5),(15,10); 5i-7j=1 with i+j<=5 has
exactly (3,2). The weight-3 part of A is a_f g^2p+rho^3 g^9p^6 (H^3's
weight-3 part is the cube of rho g^3p^2), the weight-5 part of B is
d_f g+e_f g^8p^5+rho^5 g^15p^10, and the weight-10 part of [A,B] is exactly
their bracket because monomial pairs of weights (w1,w2) contribute at weight
w1+w2+2<=10 with equality only for (3,5). Rows (i be-j al): [g^2p,g]=-1,
[g^2p,g^8p^5]=2, [g^2p,g^15p^10]=5, [g^9p^6,g]=-6, [g^9p^6,g^8p^5]=-3,
[g^9p^6,g^15p^10]=0. Hence 5a_f rho^5=3rho^3e_f, 2a_fe_f=6rho^3d_f,
c=-a_fd_f, giving e_f=5a_f rho^2/3, d_f=5a_f^2/(9rho), c=-5a_f^3/(9rho)
(inversions by 3 and rho only; attack 4 checks both rows vanish with these
values in both embeddings). a_f=[g^2p]A=[s^12 g^2p]A_s. The s^12 part of
R_s^3 is a sum over index triples i+j+k=12 with 0<=i,j,k<=5; all ten triples
have every index>=2 (attack 3), and the components R_(5-i), i>=1, have
maximal weights -4,-9,-2,-7,0 (attack 3), so no product reaches weight 3 and
no g^2p appears; alpha s^10R_s contributes alpha R_3 of weight<=-9; a0 s^15
nothing; F_13,F_14 have degree<3. Therefore a_f=[g^2p](lambda pLM)=
lambda t, and with rho=t^2, c=-5lambda^3t^3/(9t^2)=-5lambda^3t/9. Comparing
with target 5: (t-1)^2=-1, i.e. (t-1)^2+1=rho^2+1=3rho, a unit (rho!=0 as
rho(3-rho)=1). Contradiction over the field; no nilpotent or reducedness
shortcut is used, every inversion (2, 3, 9, rho, t, a, sqrt(a_0), 2zeta on a
sheet) is a field unit. Scope: the H-divisible branch F_j=HC remains
unexcluded (source Section 7 only bounds it), and no all-degree, all-golden,
D125 or JC2 coverage follows. CONFIRMED.

## 8. Replay of both checkers

Both standalone checkers were inspected before execution: exact Q[rho]
arithmetic, degree<=5 cap enforced in the source checker's multiplication,
scalar projections only in the consumer checker, no Assert node (the single
textual "assert" in each file is the ast.Assert self-check), no inner
timeout, subprocess or process group. They were byte-copied unchanged to
scratch/source-check.py and scratch/consumer-check.py (hashes e49907ee...
and b47cffd1..., identical to the lane inputs). Each run used direct
/usr/bin/prlimit --cpu=25 --as=536870912 -- /usr/bin/python3 -I -B [-O]
under subprocess.run(timeout=30); no GNU timeout. All 20 runs matched the
charged replay JSONs on rc, stdout bytes and the terminal ValueError line
(traceback path hashes differ by scratch path, as expected). Elapsed 5.3 s.

| checker | mode | opt | rc | expected rc | stdout bytes match | terminal error match | stdout sha256 prefix |
|---|---|---|---|---|---|---|---|
| source | positive | normal | 0 | 0 | 1 | 1 | `69ff601ce0adf8ea` |
| source | --wrong-critical-shift | normal | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| source | --drop-constant | normal | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| source | --drop-half-loss | normal | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| source | --drop-split-sign | normal | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| source | positive | -O | 0 | 0 | 1 | 1 | `69ff601ce0adf8ea` |
| source | --wrong-critical-shift | -O | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| source | --drop-constant | -O | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| source | --drop-half-loss | -O | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| source | --drop-split-sign | -O | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| consumer | positive | normal | 0 | 0 | 1 | 1 | `2f8ff88f1fc18292` |
| consumer | wrong-quintic-factor | normal | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| consumer | wrong-face-sign | normal | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| consumer | wrong-target-factor | normal | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| consumer | drop-resonant-target | normal | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| consumer | positive | -O | 0 | 0 | 1 | 1 | `2f8ff88f1fc18292` |
| consumer | wrong-quintic-factor | -O | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| consumer | wrong-face-sign | -O | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| consumer | wrong-target-factor | -O | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |
| consumer | drop-resonant-target | -O | 1 | 1 | 1 | 1 | `e3b0c44298fc1c14` |

Control semantics, as required: the four source modes change the critical
shift, discard the earlier constant, use 7*(2r) instead of 15r, and identify
the two sheet signs; the consumer's wrong-quintic-factor, wrong-face-sign and
wrong-target-factor modes change actual coefficients, while
drop-resonant-target replaces the expected order 36 by 0 and is a FALSE
INFERENCE check (72/5+24-12/5 is not 0), not a changed source. Source line
73 (3*0==0 and 3*7==21) is a tautology and controls nothing. None of these
scalar outcomes is a proof; the universal reasoning is Sections 2-7 above.

## 9. Independent bounded attacks (own scratch)

attack/attack.py, run under the same prlimit/-I -B/timeout discipline
(rc 0, 1.6 s, empty stderr), performs five attacks on load-bearing order and
coefficient assumptions using only Fractions, exponent projections, monomial
-pair bracket coefficients with free symbols k,e,u,v and degree<=3 factors:
1. Exhaustive regime arithmetic over 1<=j<=12, kappa in 1..40 or infinite,
   q0 in j+1..60 or infinite (26,814 triples): every inequality used in
   Sections 5-6 of the source holds (0 violations), and the survivors are
   exactly the resonant set j=12, kappa>=5, q0>=15 (1,739 triples).
2. Monomial-pair Jacobians: the resonant bracket equals
   (6e-(10/3)k^2)Y^5+ekp^(1/2) and the Y^10 row is (3q-5)k p^(-1/2); regime B
   bracket -10h v^2 Z p^(6h-1); regime A (b=0) rows -40h v^2 Y^3, eu Y^0,
   6e-(10/3)u^2 Y^5, confirming u=v=0 without the UFD step.
3. Weight slots and R_s component weights as quoted in Section 7.
4. Face rows and both coefficient formulas in both embeddings; discrepancy
   3rho.
5. Critical cubic and transverse D jet coefficients by degree<=3 factors.
No H^2/H^3/H^5/R power, no degree-15/25 A/B, no degree-6/10 initial
polynomial and no random high-degree object was built.

## 10. Owned evidence and hashes

| path | sha256 |
|---|---|
| box/golden-nonh-composition-gate-fable5-20260908/scratch/source-check.py | `e49907ee44870195b3d437ea7b095619ecd9f6bc315702dc6932cfe7937687f8` |
| box/golden-nonh-composition-gate-fable5-20260908/scratch/consumer-check.py | `b47cffd1436080d8f32e925b94160361d6a781047d755b6ad2c387c47717a47b` |
| box/golden-nonh-composition-gate-fable5-20260908/replay/replay_harness.py | `1cbf9701f90676decea90967322d384d201dc8c332ff423275542bfe46152378` |
| box/golden-nonh-composition-gate-fable5-20260908/replay/replay.json | `1cd66f44cd9c13120fc99a0c3b17ffbcf934d3a45a7660872d72e06d83c16445` |
| box/golden-nonh-composition-gate-fable5-20260908/attack/attack.py | `86ce5481cd98660b247f836c820f00fa957a6b5ce493f651782980db7387d876` |
| box/golden-nonh-composition-gate-fable5-20260908/attack/run_attack.py | `bbac774de211a1cdbfe4d5366974522e3efefc8aff3f0cc05b2339e0fd3ff567` |
| box/golden-nonh-composition-gate-fable5-20260908/attack/attack.out | `fd153c52d1d9bde7fb0da6545d2cbd1746fcf1c00e24fc1054d49dc85290b97a` |
| box/golden-nonh-composition-gate-fable5-20260908/attack/attack.err | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Commands: /usr/bin/python3 -I -B replay/replay_harness.py (rc 0) and
/usr/bin/python3 -I -B attack/run_attack.py (rc 0; child argv recorded in
its stdout line and in Section 9). replay/replay.json holds every argv, rc,
stdout, stderr terminal line and hashes; attack/attack.out is the full attack
JSON, attack/attack.err is empty.

## 11. Corrections and closing

- Source Section 6 wording: the Euler contradiction is on the sheet(s) whose
  v component is nonzero; a zero component forces nothing.
- Source Section 2: H^2-normality of orders 1..5 and deg_g F_j<=5 are
  unused later; P0's R_s-normality carries the shape (4).
- Source checker line 73 is a tautological control.
- Consumer Section 5's conditional wording is now discharged by this gate at
  the literal scope; its independence claim from the odd-j12 theorem and the
  ansatz theorem is consistent with the text read here, which never invokes
  either.
No charge_basis line is authored: no exit-price assertion is made. No Seal
is authored. All children (20 replay runs, 1 attack run) and writers are
terminal; wall time of this gate under 25 minutes. STOP/IDLE.

<!-- BODY-END -->
