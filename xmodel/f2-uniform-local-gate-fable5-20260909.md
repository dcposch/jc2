# f2-uniform-local-gate-fable5-20260909: independent hostile review

Reviewer: Fable 5.1 (external lane, own custody). Tag exact.
Start 2026-09-09T08:45:06Z (root invocation). Clock: min(25 min, 09:10Z) = 09:10:00Z.
Read scope: ONLY the two charged inputs in /tmp/jc2-lane.LE2M5G/inputs, each read
whole once by cat. Hashes matched the charge before reading:
proof e55b07e6a55de61dc70e604561f13ae5e91f6fda5c160ab2dadcc20c05182cc2 (18187 B),
transaction 4befe44825b81596f32eddba654e7601e778d801af8eb5963b55c1d7d06d7121 (684 B).
Transaction body_sha256 4a4c8b57...df1a1c4 and frozen basis 0d39df3c agree with the
proof's own Seal. No older report, blind, cross, log, receipt, F2 source output or
motivation path was opened. Zero mathematical subprocesses: no CAS, script, toy,
checker, solver, AWS, SSH, agent or web. All evidence below is manual factored
mathematics reconstructed from the proof text.

## Verdict table

| Item | Verdict | First failed implication / note |
|---|---|---|
| A reference, F!=0, budget (4) | CONFIRMED | none |
| B local tools, Euler lemmas, chain rule | CONFIRMED | none |
| C entire-B simple/coalesced/separated | CONFIRMED | no B-reference or ordG premise needed |
| D exponent ranges, (9),(10),(11) | CONFIRMED | (S) all coprime 2<=m<n; (G) n>=2m-1 only |
| E golden equality data, m=2 | CONFIRMED | support {0,n,2n} exact; c0 later |
| F (18), C_n, both charts, (20) | CONFIRMED | incompatibility holds for both rho roots |
| G scope | CONFIRMED as stated | local theorem only; no source/JC2 content |

No GAP and no REFUTED item was found. The proof is a correct local nonexistence
theorem under its explicit hypotheses. Notes marked (N) are hostile observations
that do not break the argument but should be visible to the next gate.

## A. Reference, nonzero F, multiplicity budget

Homogenization: A_s=s^{5m}A(g/s,p/s) is homogeneous of degree 5m with s=0 part
H^m. The bracket picks up s^{5m+5n} from the outputs and s^{-2} from the two
derivatives, and g^2 -> g^2/s^2, so N=5(m+n)-4. (1) confirmed.

Reference (2): at order i in 1..5 the s^i coefficient of R_s^m is mH^{m-1}R_{5-i}
plus a polynomial in the already fixed R_{5-i'}, i'<i, so the residual can be put
in a chosen linear complement of the image of multiplication by H^{m-1}. A nonzero
element of a complement is not in the image, hence not divisible by H^{m-1}
(divisibility with degree 5m-i>=5(m-1) would place it in the image). At i=5 the
image is k.H^{m-1}, which is why alpha_{m-1} is absent. For j>5 the degree 5m-j
is below 5(m-1). Scalar H^i is only possible at j=5(m-i), i<=m-2, and alpha_i
s^{5(m-i)}R_s^i removes it in increasing order. (3) confirmed at the first
surviving order, and j>=1 since order 0 is H^m.

F!=0: if F=0 then A=f_1(R_1) at s=1 and cg^2=f_1'(R_1)[R_1,B]; f_1'(R_1) has
leading form mH^{m-1}, degree 5(m-1)>=5>2, and cannot divide cg^2 (c!=0) in the
UFD k[g,p]. Confirmed; this is the only place m>=2 is used besides the budgets.

Budget (4): delta<m-1 because delta>=m-1 gives H^{m-1}|F_j. Integer delta:
H^delta|F_j, so 5m-j>=5delta with equality iff F_j is a scalar H^delta,
excluded by (3); j<=5L-1. Half-integer delta=a+1/2: simple lines carry >=a+1,
double lines >=2a+1, total >=a(S+2D2)+S+D2=5a+5/2+S/2=5delta+S/2 using
S+2D2=5. (S): S=3, Delta=3/2. (G): S=1, Delta=1/2. Simple minimizer d=delta<=m-2;
double minimizer d=2delta<=2m-3. All confirmed. Leading scalars: dividing A by a
and B by b gives Jacobian c/(ab) g^2, still nonzero. Confirmed.

## B. Local inverses, Morse coordinate, Euler lemmas, chain rule

Simple line: H=y.h1(y,X), h1(0,X)=const.X^4!=0, so z=R_s(y,X) inverts in
k(X)[[s,z]] with y(s,0,X)=O(s). Double line: d_yR_s=2y h2+... has a simple root
at (s,y)=(0,0), so y_c in E[[s]] with INTEGER s-orders; R_s-R_s(y_c) =
(y-y_c)^2 u with u(0)=h2(0,X)=a0^2 X^3 (a monomial because it is homogeneous in
the single variable X), and zeta=(y-y_c)sqrt(u) needs only X^{1/2}. kappa=ord_s xi
is an integer or infinity; the inverse y(s,zeta,X) has nonnegative integer
s-orders. Confirmed. Homogeneity: R_s has degree 5, zeta 5/2, y_c 1, and the
Puiseux extension of s changes nothing about X.

Euler lemma (5): P=Z^M+..., Q=q_vZ^v+...; the Z^{M+v-1} coefficient of
P_ZQ_X-P_XQ_Z is M q_v' because P_X has degree <=M-1 and Q_Z degree v-1 (also
for v=0). Homogeneity X q_v'+hv q_v=Lambda q_v then gives (Lambda-vh)q_v=0, so
q_v!=0 forces Lambda=vh. Confirmed.

Commuting lemma: XP_X=emhP-hZP_Z and XQ_X=enhQ-hZQ_Z give X[P,Q]=eh(nP_ZQ-mPQ_Z),
so (Q^m/P^n)_Z=0; monic in Z forces Q^m=P^n; coprimality in the UFD K[Z] gives
P=W^m, Q=W^n. e=1: Z^{m-1} coefficient m w0=0. e=2: Y^{2m-1} gives w1=0, Y^{2m-2}
gives m w0=m b0. Both use degU<=m-2 resp. 2m-3 literally. Confirmed.

Chain rule: for (y,X)->(zeta(y,X),X), A_y=A~_zeta zeta_y and
A_X=A~_zeta zeta_X+A~_X; the zeta_X cross terms cancel in the bracket and
[A,B]_(y,X)=zeta_y[A~,B~]_(zeta,X). X-dependence of the substitution is retained,
not discarded. Confirmed; same identity with z in place of zeta, and y_z =
y_zeta/(2 zeta) in the separated case.

(N) The nonzero leading target coefficient uses that g is not a factor of H, so g
restricted to any line of H is a nonzero multiple of the along-line coordinate
(g=X at p=0; g=y_c(0,X)=-X/t at p+tg=0). Both displayed H satisfy this; a general
H with the line g=0 would break the target claim. This is inside the hypotheses.

## C. Entire-B arguments

The only B input is W_s=B_s-R_s^n with s|W_s as a polynomial in (s,y,X), which
follows from the leading form H^n alone. Substituting the nonnegative-order
inverse keeps every coefficient w_l at s-order >=1, and after z=s^eta Z (or
zeta=s^r Y) the index-l term has order >=1+l eta, so any initial at nu has degree
v with v eta<=nu-1. (6): 5n-nu-v(5-eta)>=5n-1-5(nu-1)/eta=5n-5nu/eta+5/eta-1>0
from nu<n eta and eta<5. (8) is the same with 2r and 5/2-r. Both confirmed.

Simple (S4): A initial P=Z^m+U, U!=0, degU<=d<=m-2 at m eta, with l>d later by
j+l eta>m eta (eta<=j/(m-d)) and scalars later by (m-i)(5-eta). Target order
N+eta. (7): N-(m+n-1)j/L>=1+(m+n-1)Delta/L>0 from (4). Earlier Q commutes and
dies by (5)-(6); at n eta the initial is monic with corrections of degree <n and
the e=1 lemma kills U. Confirmed.

Coalesced (S5): with kappa>=2r the initial is (Y^2+b0)^m+U, degU<=2m-3, and the
earlier-Q step needs only (2m+2n-1)r<=N non-strict because nu<2nr is strict; the
monic step at 2nr needs it strict. Confirmed.

Separated (S6): regrouping (12) is the exact identity zeta^2=z-xi; U_l,V_l
converge since summands gain (i-l)kappa>=1 each. ord c_l+l kappa/2>m kappa for all
l (l<=d by r>kappa/2; l>d by j>=(2m-d)r) gives q_l>(m-l)kappa, hence eta>kappa,
which is exactly what makes every binomial shift later than its own base by
t0(eta-kappa) and makes the (z/xi) expansion order-convergent. Anchor: U_k or V_k
has order j with k<=m-2, so eta<=j/L (even d) or <(j+kappa/2)/(L+1/2)<j/L (odd
d, using kappa<j/L), and eta<j since L>1. Both-sheet tuple (u+v,u-v) cannot
vanish on both sheets. For B, the GLOBAL minimum base order nu receives no
shift, so on some sheet the initial is a nonzero polynomial with v eta<=nu-1.
Target order N-kappa/2+eta with y_z=y_zeta/(2 zeta). (13) is strict through
kappa<j/L even at E0=0. At n eta both sheets are monic and commute, e=1 forces
both corrections zero, contradiction. Confirmed; no ordG>=2j, no B-reference,
no inverse-lift premise is needed anywhere.

## D. Exponent ranges, (9), (10), (11)

E0=N-(m+n-1/2)j/L>=5(m+n)-4-5(m+n-1/2)+(m+n-1/2)Delta/L=-3/2+(m+n-1/2)Delta/L.
Integer delta: L<=m and n>=m+1 give (m+n-1/2)/L>2, E0>1/2. (S) half-integer:
Delta=3/2, E0>3/2. So (S) is strict for EVERY coprime 2<=m<n; sections 4-6
close it with no exception. (G) half-integer: Delta=1/2, L<=m-1/2, and n>=2m-1
gives m+n-1/2>=3(m-1/2)>=3L, so E0>=0 with equality iff n=2m-1 and delta=1/2,
then j=5L-1/2=5m-3; the bracket bound (2m+2n-1)r<=N is then an equality iff
r=j/(2L)=j/n. (10) confirmed as the unique equality datum. At equality every
line attains its minimal order (1,1,1) and deg F_j=3, so F_j=lambda p(p+g)(p+tg),
multiplicity 1 at both double lines; the simple line has delta=1 and is not a
minimizer, so section 4 is not the operative chart. (11) confirmed. For n<2m-1
the bound can be negative; the proof correctly claims nothing there.

## E. Golden equality data at both double lines, and m=2

2j=10m-6=5n-1, so gcd(j,n)|1; n odd >=3; 2r=5-1/n, so the integer kappa>=2r
forces kappa>=5>2r and b0=0. d=1 gives r=min(ord c0/(2m), j/n); survival at
r=j/n forces ord c0>=2mr=j+r, nonintegral, so ord c0>j+r (integer orders come
from E[[s]] before any Puiseux step). Higher c_l are later by lr>r; xi terms are
later by kappa-2r>0; scalars by 5-2r>0. Complete A initial P=Y^{n+1}+uY with
u=(F_j)_y|_root / (a0 X^{3/2}) = k0 X^{1/2}. Confirmed, including "no constant
A initial".

B at 2nr=2j: an index-l term of W_s at total order 2j has ord w_l=2j-lj/n, an
integer >=1, so n|l and l<2n, i.e. l in {0,n}; R_s^n contributes exactly Y^{2n}
because xi is later than zeta^2. h=5/2-j/n=1/(2n); Euler degree of Q is
5n-2j=1, so beta has degree 1/2 and gamma degree 1. Support {0,n,2n} is
COMPLETE: no omitted term, scalar or hidden contribution. Earlier B initials
are dead by the non-strict section 5 step. (16) confirmed.

m=2, n=3 under the same symbols: j=7, N=21=3j, L=3/2, 5L-1/2=7, r=7/3,
2r=14/3, kappa>=5, d=1=2m-3 (the quadratic-lemma bound is exactly tight here
and still holds), P=Y^4+uY, Q=Y^6+beta Y^3+gamma, h=1/6, beta=3u/2,
gamma=3u^2/8=C_3 u^2, [P,Q]=(3/8)k0^3 X^{1/2}. No exceptional smallest case.

## F. Coefficients (18), C_n, both charts, (20)

(17): XP_X=(n+1)hP-hYP_Y and XQ_X=2nhQ-hYQ_Y give X[P,Q]=h(2nP_YQ-(n+1)PQ_Y).
With P_Y=(n+1)Y^n+u and Q_Y=2nY^{2n-1}+n beta Y^{n-1}, my independent expansion:
Y^{3n}: 2n(n+1)-2n(n+1)=0; Y^{2n}: 2n(n+1)beta+2nu-n(n+1)beta-2n(n+1)u
=n(n+1)beta-2n^2u; Y^n: 2n(n+1)gamma+2nu beta-n(n+1)u beta
=2n(n+1)gamma-n(n-1)u beta; Y^0: 2nu gamma. No other powers. (18) confirmed.
The target at order N+r=2mr+2nr is Y-free and NONZERO (a constant times
X^{1/2}); it is retained, not set to zero. Hence beta=2nu/(n+1),
gamma=(n-1)u beta/(2(n+1))=n(n-1)u^2/(n+1)^2, C_n!=0 for n>=2, and
[P,Q]=2nh u gamma/X=C_n k0^3 X^{1/2}. C_3=3/8, C_5=5/9. Confirmed.

Chart data, rederived: (p,g) chart y=p, X=g: H=y^2(y+X)(y+tX)^2, h2(0,X)=t^2X^3
so a0^2=t^2; (F_j)_y|_{y=0}=lambda X.tX=lambda t X^2; [A,B]_(p,g)=-cg^2=-cX^2.
(g,p) chart y=g, X=p, root y=-X/t: X+ty=t(y+X/t), h2=X^2(X-X/t)t^2=t(t-1)X^3;
(F_j)_y=lambda X[(X+ty)+t(X+y)]=lambda(t-1)X^2 at the root;
[A,B]_(g,p)=cg^2=cy^2 -> cX^2/t^2. All four entries and both signs confirmed.
Chart-free form of (19): C_n[(F_j)_y]^3 = J_{yX}.h2.X on the line, invariant
under rescaling y or X. Chart 1: C_n lambda^3 t^3 = -c t^2, c=-C_n lambda^3 t.
Chart 2: C_n lambda^3 (t-1)^3 = c(t-1)/t, c=C_n lambda^3 t(t-1)^2. (20)
confirmed. Only c and lambda are shared; a0,k0,b0,d0 are chart-local, and the
sign of a0 or of X^{1/2} flips both sides together. Equality needs (t-1)^2=-1;
with t=1-rho, (t-1)^2+1=rho^2+1=3rho!=0 for BOTH roots of rho^2-3rho+1. Two
different actual lines were used, so this is a two-chart proof, not one-chart
consistency. Confirmed.

(N) Asymmetry check: the linear map (g,p)->((t-2)p-g, p+tg) preserves H up to
(t-1)^5 and swaps the two double lines, but sends g^2 to -(t-1)^2((t-2)p-g)^2,
so it does NOT preserve the Jacobian hypothesis. The two chart relations are
therefore not forced to agree by symmetry; their disagreement is meaningful.

## Manual controls (hypothesis / changed object, none executed)

- c=0: A=H^m, B=H^n satisfy every hypothesis but c!=0; F=0 and the F!=0 step is
  exactly what fails. Consistent.
- t generic in H=p^2(p+g)(p+tg)^2: (20) becomes compatible iff (t-1)^2=-1, i.e.
  t=1+-i. The golden value is load-bearing; for t=1+-i this proof leaves the
  (10) case open, which is the expected sharpness of a non-vacuous argument.
- n<2m-1 for (G): E0 can be negative and section 5 loses the non-strict bound;
  correctly excluded from the statement.
- Noncoprime (m,n): Q^m=P^n no longer forces P=W^m; correctly excluded.

## G. Scope

The theorem is the nonexistence of A,B in k[g,p] with leading forms H^m,H^n and
[A,B]_(g,p)=cg^2, c!=0, for the two displayed degree-five H, over any
characteristic-zero field (proved over its algebraic closure, which is
stronger). It uses only finite extensions k(X^{1/2}), square roots of
constants, and finite Puiseux extensions of s. It establishes no source
realization or selection, no full-ideal statement, no all-F2 coverage, no
positive-characteristic or general-H result, and nothing about JC2. A low-order
formal control satisfying the local equations to some order is not a
counterexample, and this receiver obstruction is not a counterexample either;
it excludes one exponent family for two top patterns. The "old 3/5 coefficient"
remark in section 8 was not checked against any older report (out of scope by
charge); C_5=5/9 follows from the formula alone.

## What survives and the single recommended gate

Everything charged survives. The only unreviewed external link is the
motivation chain, deliberately not consumed. One different-model gate (not
automatic follow-on work) could re-derive section 6 on its own and the two
chart tables from the raw H, since those are the two places where an
orientation or order slip would be silent. No new campaign OPEN is raised; no
owned raised OPEN exists for this lane.

## Publication check

Read scope: the two charged inputs, whole, once each; own body re-read whole
before the terminator. Files written: this report only; no box directory was
needed. No background process, subprocess or writer was started, so all
writers are IDLE at close. Start 08:45:06Z; body closed at the time stamped in
the final line below. No Seal and no charge_basis line are authored here.
End 2026-09-09T08:59:45Z; terminal state all-writers-IDLE.

<!-- BODY-END -->
