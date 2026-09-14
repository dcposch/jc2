# Hostile gate: positive-face Euler composition (Fable, 2026-09-06)

Lane `/tmp/jc2-lane.bQEt6L`, basis `0d39df3c`. Charged root
`xmodel/monomial-j-positive-face-composition-root-20260906.md`, SHA-256
`41a2efed…bccf7b` (verified). Checker `check.py` SHA `89985fa9…3483f` (matches
root). GGV snapshot `core-ggv-layout.txt` SHA `e3694dde…9e37b1` (matches).
Read whole: root body, checker, Astra Euler-interface report, FALLACY-v2, the
GGV §1 definitions (lines 128–200), Lemma 2.2 statement, Remark 2.5, Theorem
2.6 statement and proof, Remarks 2.7–2.8, Proposition 2.11 statement and proof
of (1)–(3) (lines 364–481). Read in part: both 1435 blind ideations (only the
Euler/Laurent/root-count passages). No AWS, CAS, receiver farm, solver, cut,
ledger/tool/adapter/validator/FALLACY edit, external post, web or `jc2-lean`.

## Verdict summary

| Claim | Verdict |
|---|---|
| Polynomial twisted Euler element E in K[g,p] | CONFIRMED (conditional on GGV Thm 2.6 existence, whose [8, Lemma 2.2] step stays external) |
| Root bound floor((l r+s)/s), TWO at (1,l)/(1,1) | CONFIRMED |
| Endpoint exceptions transported to (l,1) | CONFIRMED |
| Source scope: full polynomial pair, k>=0 | CONFIRMED as stated; polynomial-face hypothesis is load-bearing (own negative control); residual client obligation listed below |

The root does repair the Fable blind count. No field or uniqueness
hypothesis is missing. No receiver exclusion or ranking change follows.

## 1. Constantization and 1/l pullback: CONFIRMED

Monomial identity, checked by hand and by exact script: for A,B in
K[t^(±1/l),p] and t=g^l,

    [A(g^l,p),B(g^l,p)]_(g,p) = l g^(l-1) [A,B]_(t,p)|_(t=g^l).

Hence [Pbar,Qbar]_(t,p)=c g^k/(l g^(l-1))=c/l exactly when k=l-1, and the
pullback of GGV's F gives [F(g^l,p),R]=l g^(l-1) R, so E=F(g^l,p)/l obeys
[E,R]=g^k R. GGV's bracket differentiates fractional powers of x (Prop 2.11
proof formula and Remark 2.5 confirm this), so the chain rule is the right
one. Own controls at k=1,2,4 replay c/l and the twisted relation.

## 2. Theorem 2.6 hypotheses in its actual ring: CONFIRMED

GGV Theorem 2.6 (line 366) needs only P in L^(l), (rho,sigma) in V_>0
(coprime, rho+sigma>0), v(P)>0, and some Q in L^(l) with [P,Q] in K^x.
There is no v(P)+v(Q)>rho+sigma clause, no Dir(P) clause, no minimal-pair
clause. K is any characteristic-zero field in §2; algebraic closure is
assumed only from line 894 onward, so no field hypothesis is missing.
Pbar,Qbar lie in K[t^(1/l),p] ⊂ L^(l). Its F is (rho,sigma)-homogeneous with
v(F)=rho+sigma, which the polynomiality proof uses; that homogeneity is in
the theorem statement, not assumed.

Primitive rescaling. V requires gcd(rho,sigma)=1, so the applied direction
is (rho,sigma)=(l r,s)/d, d=gcd(l r,s). Then v_(rho,sigma)(F)=(l r+s)/d, the
(l r,s)-weight of F is l r+s, and E is (r,s)-homogeneous of weight l r+s.
The face selected is exactly the (r,s)-face of P, and the bound
floor((rho+sigma)/sigma)=floor((l r+s)/s) is d-invariant. At source (1,l):
(l,l)/l=(1,1), weight 2, N=2. Consistent; the root's "before primitive
rescaling" phrase is correct.

## 3. Polynomiality (pole removal): CONFIRMED

Re-derived independently. E is (r,s)-homogeneous of weight l r+s>0 with
r,s>0, so each g-exponent carries one p-exponent. If the least g-exponent u
is negative then r u+s v=l r+s>0 forces v>=1. R is polynomial of positive
weight, least term b g^h p^j with h,j>=0 not both zero. The g-exponent of
[E,R] is minimised only by the pair of least terms, giving coefficient
a b (u j−v h) p^(v+j−1) with u j<=0, v h>=0 and equality impossible
(it would need h=j=0). The right side g^k R has no g-exponent below k+h>=h,
and u+h−1<h. Contradiction. The argument uses neither uniqueness of E nor
which F GGV supplies; it proves every homogeneous Laurent solution of
[E,R]=g^k R, and every weight-(l r+s) solution of [E,R]=0, is polynomial.
The pure-g face (j=0, h>0) is covered by −v h<0.

Own control: for the genuine polynomial pair P=A(g^3,p), Q=B(g^3,p) with
(A,B)=(t+(y+t^2)^2, y+t^2), [P,Q]=3g^2, I solved the twisted Euler system
exactly in a Laurent window (g-exponent >= −12) at eight positive primitive
directions. Every solution, including kernel directions (dimension 0 or 1),
is polynomial with p-degree at most floor((l r+s)/s). The supplied
determinant sample in `check.py` mislabels its variables and omits the j=0
case; my sample covers u<0, v>=1, (h,j)≠(0,0) exhaustively on a 6^3 box.

## 4. Root bound via Proposition 2.11(1): CONFIRMED

Prop 2.11 (line 420) needs (rho,sigma) in V_0 (rho>0, rho+sigma>0), F
homogeneous, v(P)>0, [F,ℓ(P)]=ℓ(P). All hold; clause (1) says f is
separable and every irreducible factor of p divides f, with p,f the face
factors after removing the monomials x^(r/l)y^s and x^(u/l)y^v (p(0)≠0≠f(0)),
so axes are not counted. With z=x^(−sigma/rho)y=g^(−s/r)p, the z-degree of f
equals the p-exponent spread of F (Remark 2.8), at most the maximal
p-exponent of F=l E(t^(1/l),p), which by nonnegative g-exponents is
floor((l r+s)/s). Distinct nonzero roots of the face factor over Kbar are
therefore at most N=floor((l r+s)/s); two at (1,l). Clauses (4),(5) are not
used. Own controls: a three-distinct-root polynomial face at (1,2), k=1,
admits no twisted Euler element even in the Laurent window (the theorem
says any such pair is impossible); the root's two-root fixture solves,
polynomially, with p-degree 2 and kernel dimension 0.

## 5. Endpoint alternatives: CONFIRMED as transport only

GGV's exceptional point (1,1) is the support point (i/l,j)=(1,1), i.e. the
monomial t p=g^l p, so it pulls back to (l,1). The exponent map
(a,b)→(l a,b) is linear with determinant l>0: proportionality and
counterclockwise order are preserved, and for positive directions st/en are
the min-p/max-p face points in both coordinates. Own controls: on monomial
faces E's support is exactly (l,1) (Remark 2.5's λxy pulled back), and
Thm 2.6(2)–(4) hold in transported form on every tested face. Astra's
interface objection (endpoint (1,1) of P=gp wrongly forbidden) is resolved:
(1,1)≁(3,1). Nothing beyond transport is claimed or confirmed.

## 6. Source scope and the blind repair

What the theorem consumes: an actual pair (P,Q), both in L^(l) after
constantization, with Jacobian exactly c g^k, c≠0, k>=0, and the (r,s)-face
of P having nonnegative exponents. The root's hypothesis P,Q in K[g,p] is
sufficient; strictly, Q may be Laurent in g and only P's face must be
polynomial. That face hypothesis is load-bearing: on the root's Laurent
fixture R=g^(−3)(p^3−g^3)^2 my solver finds the non-polynomial Euler element
in the window and NO polynomial one (three roots, N=2). A face alone, or a
chart truncation, licenses nothing, because Thm 2.6 needs [Pbar,Qbar] in K^x.

Fable blind card 1 counted weight-line monomials floor((rho+sigma)/sigma)+1
in L^(l). That count is false there (t-exponents may be negative, so the
line carries infinitely many monomials), and it was a monomial count, not the
degree bound; the same card's "at most two roots" at (1,1) was not derived.
The root supplies the missing pole lemma and the correct degree bound N, so
the repair is real for polynomial receivers and false for arbitrary Laurent
Euler data, exactly as stated. Astra's blind pole-removal proposal is the
ingredient; the composition is new within the frozen record.

Residual client obligation (later task, not this gate): for each receiver
row or K7 chart, exhibit both components as actual elements of K[γ,π] (or
L^(l) with polynomial P-face) in the same coordinates used to read the face,
with Jacobian exactly c γ^k, k>=0 (v_s>=2 when k=v_s−u_s−1), and then read
only forced faces; a face with three or more distinct nonzero roots at (1,l)
would contradict the theorem, but forced-face support is unestablished here.

## 7. Strongest attack and controls

Strongest attack: the only unverified link is [8, Lemma 2.2] (Joseph), used
by GGV to build F=ℓ(G0)ℓ(P)/[ℓ(G0),ℓ(P)]; the root declares it and I did not
read [8]. Everything after F exists is now independently derived. A weaker
attack is bite: on my genuine pair every positive face is monomial or
one-root, so the lemma may be vacuous on real receivers; that is the later
screen's question. Sharpness is shown only at Euler level.

Controls retained in `box/monomial-j-positive-face-gate-fable5-20260906/`:
`own_check.py` (SHA `ffa4a4e2…c5a4b98`), 76 PASS in normal and `-O`, 0.03 s,
13 MiB; supplied `check.py` 15 PASS in normal and `-O`, explicit exceptions
(no `assert`). Outputs `own_check.out`, `supplied_check_normal.out`,
`supplied_check_O.out`. No exit price is asserted; no basis line is due.

<!-- BODY-END -->
