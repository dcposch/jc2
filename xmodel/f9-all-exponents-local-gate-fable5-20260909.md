# Independent gate: degree-seven Jacobian obstruction, all coprime exponents

Gate model: Claude Fable 5.1 (claude-fable-5-1), independent different-model
review. Started 2026-09-09 08:05:36 UTC, hard stop 08:30 UTC.
Charged objects read WHOLE from /tmp/jc2-lane.5Sufff/inputs before review:

- f9-all-exponents-local-exclusion-coordinator-20260909.md, full SHA-256
  2dba41ed5e07d62b2e96221e67fc2c3ba16325d1a99f0015f09194d285c3d192 (matches
  the charged producer SHA; body SHA e10dc412... matches its artifact record).
- f9-all-exponents-local-exclusion-coordinator-20260909.md.artifact.json,
  SHA-256 0879580aa4171f10e1a5368ba47bd49253e317f9f6b411e822d66add72fba98a
  (matches the charged transaction).

Method: manual factored derivation only. No CAS, no Python, no enumeration,
no degree sweep, no checker, no AWS, no agent, no external source. The only
tool use was read-only cat/ls/sha256sum on the two charged inputs and writing
this report plus box/f9-all-exponents-local-gate-fable5-20260909/. No live
blind, peer report, root blind or source proof was accessed. The candidate's
label and the older m=3,n=5 result were given zero evidential weight; every
inequality below is rederived.

Notation follows the candidate: K=(b²-a²)²b(b²-3a²/2), A_s,B_s the dilation
homogenizations, N=7(m+n)-5, R_s, f_s, F, F_j, delta, L=m-delta, Delta,
eta, r, kappa, xi, rho, the two sheets +/-. Verdict scale: CONFIRMED (the
implication is proved by my own derivation), REFUTED (a literal failed
implication with a countercontrol), GAP (unproved as written).

## A. Finite A-only canonical reference — CONFIRMED

Dilation check. d_a A_s = s^(7m-1)(d_a A)(a/s,b/s), so
[A_s,B_s]=s^(7m+7n-2)·2c(a/s)³=2c s^(7(m+n)-5)a³, N=7(m+n)-5. Confirmed.

Orders 1..7. R_s^m = K^m + Σ_i s^i(mK^(m-1)R_(7-i) + T_i), where T_i depends
only on R_(7-i') with i'<i. Multiplication by mK^(m-1) is injective on the
degree-(7-i) forms (domain), and every degree-(7m-i) multiple of K^(m-1) is
K^(m-1)h with deg h=7-i, so the image is exactly the K^(m-1)-divisible
subspace of S_(7m-i). Fix a complement C_i; write A_(7m-i)-T_i = K^(m-1)h+c
uniquely and set R_(7-i)=-h/m. The residual c in C_i is nonzero only if not
K^(m-1)-divisible. Later R choices enter only at orders > i; alpha choices
enter at orders >= 14 > 7. At i=7 the image is k·K^(m-1) (R_0 a scalar),
which is precisely the effect an s^7 T^(m-1) term would have, so omitting
T^(m-1) from f_s is consistent. Orders >7: deg F_i = 7m-i < 7(m-1) = deg
K^(m-1), so nonzero residuals are not K^(m-1)-divisible. Scalar powers:
lambda K^i has degree 7i, which equals 7m-j only at j=7(m-i); for i<=m-2 the
term alpha_i s^(7(m-i)) R_s^i has leading contribution alpha_i K^i at that
order and nothing earlier, and processing i=m-2,...,0 in increasing order
of j keeps earlier orders fixed. Hence the first nonzero F_j satisfies (4).
m=2: f_s=T²+alpha_0 s^14; orders 8..13 have degree <7 so are not
K-divisible; order 14 is a constant, removed by alpha_0. Confirmed.

F=0 contradiction. If F=0 then A=f_1(R_1) at s=1, and [A,B]=f_1'(R_1)[R_1,B].
f_1'(T)=mT^(m-1)+... has degree m-1 (char 0), so f_1'(R_1) has degree
7(m-1)>=7>3 and is nonzero. It divides 2ca³ in the UFD k[a,b] (if [R_1,B]=0
the bracket is 0, contradicting c!=0), impossible by degree. Confirmed.
Strongest attempted failure: I tried to break the order-7 step by letting
R_0 interfere with orders 1..6; it cannot, since s^7 R_0 enters R_s^m only at
order >=7. No failure found.

## B. Minimizing factor and strict budget — CONFIRMED

Over algebraically closed k, K = b·(b-a)²(b+a)²·(b-a√(3/2))(b+a√(3/2)):
three simple lines, two double lines, Σe_i=7. delta = min ord_(L_i)(F_j)/e_i.
If delta >= m-1 every L_i^(e_i(m-1)) divides F_j, hence (coprime factors,
UFD) K^(m-1) | F_j, contradicting (4). So 0<=delta<m-1, delta in (1/2)Z, and
1<L<=m.

Budget (5). Only minimality is used: each L_i divides F_j to order >= e_i
delta. Integer delta=t: K^t | F_j, deg F_j >= 7t; equality forces F_j =
lambda K^t, excluded by (4) (including t=0, a nonzero constant), so
deg F_j >= 7t+1, i.e. j <= 7L-1. Half-integer delta=t+1/2: simple lines to
order >= t+1 (integer ceiling of t+1/2), double lines to order >= 2t+1;
the product has degree 3(t+1)+2(2t+1)=7t+5=7delta+3/2, so j<=7L-3/2. No
equal-multiplicity or F_j=K·C assumption is used. Confirmed.

Margins for every coprime m<n. With j<=7L-Delta:
(8): N-(m+n-1)j/L >= 7(m+n)-5-7(m+n-1)+(m+n-1)Delta/L = 2+(m+n-1)Delta/L>0.
(7): (m+n-1/2)/L >= (2m+1/2)/m > 2 since n>=m+1, L<=m; then
N-(m+n-1/2)j/L >= 7(m+n)-5-7(m+n)+7/2+(m+n-1/2)Delta/L
 = -3/2+(m+n-1/2)Delta/L > -3/2+2 = 1/2 > 0. Uniform in m,n.
Tightest instance I could find: m=2,n=3,delta=0 gives N=30, j<=13, and
(m+n-1/2)j/L <= 4.5·13/2 = 29.25 < 30, margin 3/4, strict. Confirmed.

## C. Formal charts, Euler/commutation/UFD lemmas — CONFIRMED

Sign: [A,B]_(y,X) with y=b, X=a equals -[A,B]_(a,b), target -2c s^N X³.
Simple line y=γX: K_y(γX,X) is γ-dependent but nonzero (e.g. at b=0 it is
-3X^6/2, at b=±√(3/2)X it is 3X^6/4), so R_y is a unit in k(X)[[s,y-γX]] and
z=R_s inverts to y(s,z,X) with nonnegative s-orders; uniqueness of the formal
inverse makes y homogeneous of degree 1 with deg z=7. Double line y=εX: with
w=y-εX, K=w²(2εX+w)²y(y²-3X²/2), so K_y(εX)=0 and K_yy(εX)/2=-2εX^5 (the
candidate's value; I recomputed it as 4X²·εX·(-X²/2)). Formal IFT gives the
unique y_c=εX+O(s) in k(X)[[s]]; R_s-xi vanishes to order 2 at y_c, so
R_s-xi=(y-y_c)²G with G(y_c)=-2εX^5+O(s) a unit; its square root exists in
E[[s]][[y-y_c]] with E=k(X^(1/2)) and k algebraically closed; zeta=(y-y_c)√G
is an exact Morse coordinate with invertible y_zeta, degree 7/2. Puiseux
extensions in s only rescale the grading and never specialize X. Confirmed.

Lemma 1. P monic in Z of degree M>0, Q of degree t with leading q_t. The
Z^(M+t-1) coefficient of P_Z Q_X - P_X Q_Z is M q_t' since deg_Z P_X<=M-1
(monicity). So [P,Q]=0 forces q_t'=0; then the Z^t coefficient of the Euler
identity gives X q_t'+ht q_t=Λ q_t, i.e. (Λ-th)q_t=0, impossible for
Λ-th>0 and q_t!=0 in the field E. t=0 is included (Q_Z=0, coefficient of
Z^(M-1) is M q_0'). Confirmed.

Lemma 2. From XP_X=emhP-hZP_Z and XQ_X=enhQ-hZQ_Z,
X[P,Q]=P_Z(enhQ-hZQ_Z)-(emhP-hZP_Z)Q_Z=eh(nP_ZQ-mPQ_Z), so [P,Q]=0 gives
(Q^m/P^n)_Z=Q^(m-1)P^(n-1)(mPQ_Z-nP_ZQ)/P^(2n)=0. In E(Z) the Z-constants are
E, and equal degrees emn with both monic force Q^m=P^n. In the UFD E[Z],
m v_π(Q)=n v_π(P) with gcd(m,n)=1 gives v_π(P)=m w_π, v_π(Q)=n w_π, so P=W^m,
Q=W^n, W monic of degree e. e=1: (Z+w_0)^m=Z^m+mw_0Z^(m-1)+..., so a
correction of degree<=m-2 forces w_0=0 and U=0. e=2: (Y²+w_1Y+w_0)^m has
Y^(2m-1) coefficient m w_1 and Y^(2m-2) coefficient m w_0+C(m,2)w_1²; with
deg U<=2m-3 these read m w_1=0 and m w_0=m b_0, so W=Y²+b_0, U=0. Confirmed.
Strongest attempted failure: coefficients in E depend on X, so I checked that
neither lemma assumes q_t constant; lemma 1 derives q_t'=0 and lemma 2 uses
only the Euler identities. No failure found.

## D. Minimizing simple line, whole B — CONFIRMED

Anchor. The s^j coefficient of transformed F is F_j(y(0,z,X),X) with
y(0,z,X)-γX=z/K_y+O(z²); ord_L F_j=d gives F_j=(y-γX)^d φ, φ(γX,X)!=0, so
f_d has order exactly j and f_l (l<d) order >j; all f_l have order >=j.
eta=min_(l<=d) ord f_l/(m-l) is finite, positive, eta<=j/(m-d)=j/L<7.
l<=d: order >= (m-l)eta+l eta = m eta. l>d: j+l eta >= (m-d)eta+l eta >=
(m+1)eta. Scalars: 7(m-i)+i eta-m eta=(m-i)(7-eta)>0. So (9) holds with
0!=U of degree <=d<=m-2. Confirmed.

Whole B. W_s=B_s-R_s^n has s-order>=1 as a polynomial; substituting y(s,z,X)
(nonnegative orders) keeps every z-coefficient at order>=1, so a term with
index l sits at order >=1+l eta. Earlier initial nu<n eta: t eta<=nu-1, and
Λ-th = 7n-nu-t(7-eta) >= 7n-nu-(nu-1)(7-eta)/eta = 7n-7nu/eta+7/eta-1 > 0,
because nu<n eta and eta<7 (this is (10)). Chain rule: A_z=A_y y_z,
A_X|_z=A_y y_X+A_X, and the y_X terms cancel, giving y_z[A,B]_(y,X) with
y_z=1/R_y a unit; d_Z=s^eta d_z adds eta, target order N+eta. Bracket order
m eta+nu < (m+n)eta <= N+eta by (8). So [P,Q]=0, contradicting lemma 1.
At order n eta the W contributions have l eta<=n eta-1, degree<n, so Q is
monic of degree n and z^n is not cancelled; (m+n)eta<N+eta by (8) gives
[P,Q]=0 with Euler degrees m(7-eta), n(7-eta), h=7-eta!=0; lemma 2 (e=1)
forces U=0, contradicting (9). All scalars retained. Confirmed.
Strongest attempted failure: I tried nu<m eta (B initial before A's); the
bracket order m eta+nu is still below N+eta and P is still A's initial, so
the exclusion is unchanged. No failure found.

## E. Double line, coalesced roots (kappa>=2r) — CONFIRMED

Anchor: at s=0, y-εX=zeta/√G_0+O(zeta²) and ord_(y-εX)F_j=d=2delta, so c_d
has order exactly j, c_l (l<d) order >j, all c_l order >=j. r=min_(l<=d)
ord c_l/(2m-l) is finite positive, r<=j/(2m-d)=j/(2L)<7/2 by (5); l>d terms
sit at j+lr>=(2m-d)r+lr>2mr. R_s=xi+zeta²=s^(2r)(Y²+s^(kappa-2r)xi_0+...),
so its order-2r initial is Y²+b_0 with b_0=xi_0 if kappa=2r and b_0=0 if
kappa>2r or xi=0; R_s^m has initial (Y²+b_0)^m at 2mr; scalars are later by
(m-i)(7-2r)>0. Hence (11), 0!=U of degree<=d<=2m-3<2m. Confirmed.
Whole B: every zeta-coefficient of W_s has order>=1 (y=y_c+zeta·unit has
nonnegative orders), so index l sits at >=1+lr. Earlier nu<2nr: tr<=nu-1
and with h=7/2-r, Λ-th >= 7n-nu-(nu-1)(7/2-r)/r = 7n-7nu/(2r)+7/(2r)-1>0.
Target: y_zeta is a unit, d_Y=s^r d_zeta, order N+r. Bracket 2mr+nu <
2(m+n)r <= N+r since (2m+2n-1)r <= (m+n-1/2)j/L < N by (7): this is (13).
At 2nr the W part has lr<=2nr-1, degree<2n, so Q=(Y²+b_0)^n+lower is monic;
[P,Q]=0 by (13); Euler degrees 2mh, 2nh; lemma 2 (e=2) forces U=0 against
(11). The equality case enters only through b_0!=0, which lemma 2 allows;
xi=0 is the b_0=0 case. All target exponents m<n covered by (7). Confirmed.
Strongest attempted failure: a correction of degree 2m-2 would escape lemma
2 (the candidate's own control); I checked that d<=2m-3 is forced by
2delta<2m-2 with 2delta integral. No failure found.

## F. Separated roots, F regrouping — CONFIRMED

kappa<2r finite, kappa a positive integer (xi in k(X)[[s]]), xi_0=λX^(7-kappa),
rho=√(-xi) of order kappa/2 with leading coefficient in E, homogeneous of
degree 7/2. zeta²=z-xi=rho²(1-z/xi) gives zeta=±rho√(1-z/xi), convergent
once ord z=eta>kappa. Regrouping: c_(2i)zeta^(2i)=c_(2i)(z-xi)^i and
c_(2i+1)zeta^(2i+1)=c_(2i+1)(z-xi)^i·zeta, so F=U(ξ+ζ²)+ζV(ξ+ζ²) as an
(s,zeta)-adically convergent identity, and on a sheet F_±=U±rho√(1-z/xi)V.
U_l=Σ_(i>=l)c_(2i)C(i,l)(-xi)^(i-l): summand orders >=j+(i-l)kappa tend to
infinity, so U_l exists with ord>=j; same for V_l. Anchors: d=2k gives
U_k=c_(2k)+(terms of order >=j+kappa), order exactly j; d=2k+1 gives the
same for V_k. Both k<=m-2 since d<=2m-3.
(15): l<=d: ord c_l+l kappa/2 >= (2m-l)r+l kappa/2 = m kappa+(2m-l)(r-kappa/2)
> m kappa. l>d: ord c_l+l kappa/2 >= (2m-d)r+l kappa/2 > (2m-d)kappa/2+
d kappa/2 = m kappa. Then ord c_(2i)+(i-l)kappa > (m-l)kappa and
kappa/2+ord c_(2i+1)+(i-l)kappa > (m-l)kappa; the summand orders tend to
infinity so the minimum is attained and q_l>(m-l)kappa strictly.
eta=min_(l<=m-2)q_l/(m-l): finite by the anchor, eta>kappa by q_l>(m-l)kappa.
Even: eta<=q_k/(m-k)<=j/L. Odd: eta<=(j+kappa/2)/(L+1/2)<j/L iff
L kappa/2<j/2 iff kappa<j/L, true since kappa<2r<=j/L. eta<7 from j<=7L-Delta.
eta<j: even L=m-k>=2; odd L=m-k-1/2>=3/2. m=2 gives (d,L)=(0,2) or (1,3/2).
Bases U_l z^l and ±rho V_l z^l at l<=m-2 have order>=q_l+l eta>=m eta with
equality at the minimiser; l>=m-1 bases have order>=j+(m-1)eta>m eta since
j>eta. A shift of an odd base by z^t/xi^t adds t(eta-kappa)>0 to that base.
No earlier base exists below m eta, so the order-m eta coefficients are the
tuple (u_l+v_l,u_l-v_l), zero on both sheets only if u_l=v_l=0; some base
attains m eta, so (18) holds with both P_± monic (z^m exact on both sheets,
scalars later by (m-i)(7-eta)). Confirmed.
Strongest attempted failure: I tried to make eta depend circularly on the
sheet expansion; U_l,V_l are defined from c_l and xi alone, eta from them,
and only then is z=s^eta Z substituted with eta>kappa. No failure found.

## G. Separated roots, WHOLE B regrouping and target — CONFIRMED

W_s's zeta-coefficients have order>=1, so U^B_l,V^B_l have order>=1 (same
convergent sums), and bases sit at >=1+l eta (even) and >=1+kappa/2+l eta
(odd); finitely many below any bound, so a global minimum nu exists. If
nu<n eta: shifts are later than their own bases by t(eta-kappa)>0 and every
base is >=nu, so nothing returns to nu; z^n starts at n eta>nu; the tuple
(u^B±v^B) is nonzero on at least one sheet, giving an actual initial Q there
with t eta<=nu-1 (19). Target: y_z=y_zeta·zeta_z=y_zeta/(2zeta), and
1/(2zeta)=±(1/(2rho))(1-z/xi)^(-1/2) whose z^t/xi^t terms have order
t(eta-kappa)>=0, so ord y_z=-kappa/2 exactly; y_X cross terms cancel as in D;
d_Z adds eta. Exact target order N-kappa/2+eta on both sheets. Margin (20):
(m+n-1)eta+kappa/2 <= (m+n-1)j/L+kappa/2 < (m+n-1)j/L+j/(2L) = (m+n-1/2)j/L
< N by (7); strict via kappa<j/L even when eta=j/L. Hence m eta+nu <
(m+n)eta < N-kappa/2+eta and [P_±,Q]=0 on that sheet; lemma 1 with
Λ-th >= 7n-7nu/eta+7/eta-1>0 (from (19), nu<n eta, eta<7) is a
contradiction. So no base on either sheet lies below n eta. At n eta: every
base is >=n eta so every shift is >n eta (no returning shift, no per-shift
coefficient bound used); bases at n eta have l eta<=n eta-1, degree<n; both
Q_± are monic of degree n. (20) gives [P_±,Q_±]=0 on both sheets, Euler
degrees m(7-eta), n(7-eta), h>0; lemma 2 (e=1) on each sheet gives
U_+=U_-=0, against (18). No ordG>=2j theorem is used anywhere. Confirmed.
Strongest attempted failure: a shifted term of an early odd B base returning
to n eta would need base order + t(eta-kappa) = n eta with base order<n eta,
which the first step excludes; the argument is global-minimum based, not a
degree bound on the shifted coefficient. No failure found.

## H. Scope, corollary, controls — CONFIRMED (as a formal-field theorem)

Exhaustion: F!=0 gives a minimizing line, simple (D) or double; double
splits into kappa>=2r including xi=0 and equality (E) and kappa<2r (F,G).
Weighted corollary: with g=a², p=b, A(a,b)=A'(a²,b) has ordinary top form
H^m(a²,b)=K^m of degree 7m (weight 7m maps to degree 7m, lower weights to
lower degrees), and A_a=2aA'_g, A_b=A'_p give [A,B]_(a,b)=2a[A',B']_(g,p)
=2a·cg=2ca³; the substitution k[g,p]->k[a,b] is injective. So the corollary
follows from (1). Confirmed as a receiver obstruction only.
Controls, each checked by hand: c=0 lets A=K^m,B=K^n (the F!=0 step divides
2ca³ by f_1'(R_1) and needs c!=0). gcd>1: P=Z²+u, Q=(Z²+u)² commute with a
degree-0 correction, so lemma 2 genuinely needs coprimality. Degree 2m-2:
(Y²+b_0+t)^m-(Y²+b_0)^m starts with m t Y^(2m-2), so the e=2 lemma is sharp
at 2m-3. One-sheet cancellation: u=-v gives (0,-2v), so one sheet may not be
dropped and the proof does not drop it. Degree-zero P: P=1,Q=X commute with
Q_X!=0, so lemma 1 needs M>0; here M=m or 2m>=2.
Scope: the argument is over the field E=k(X^(1/2)) with formal Puiseux
series in s; it says nothing about nonreduced coefficient rings, positive
characteristic, noncoprime exponents, other degree-7 K, actual Keller
sources or global JC2. No all-Keller-source or infinite-F9 bridge is
supplied or assumed.

## Verdict

A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED, E CONFIRMED,
F CONFIRMED, G CONFIRMED, H CONFIRMED.

The theorem (1), for every coprime 2<=m<n over any characteristic-zero
field, is FULLY PROVED as written, modulo only standard formal facts (formal
inverse/implicit function theorem, one-variable Morse coordinate, Puiseux
extensions, formal chain rule, UFD property of E[Z]), each of which I
checked applies in the stated rings. No failed implication was found, so no
countercontrol or repair hypothesis is owed. Minor presentational note, not
a gap: section 3's remark that the constants of E are k is never needed;
lemma 1 uses only that E is a field of characteristic zero.

No raised OPENs in this report. No Seal and no charge_basis line are
authored here (no new exit price is asserted). No downstream task or
acceptance is authorized by this verdict alone.

<!-- BODY-END -->
