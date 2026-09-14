# F10 full-map field degree: bounded hostile geometry gate

2026-09-09, Fable 5.1 gate. Launch 16:40:36 UTC; deadline 16:52:36 UTC (launch+12 min, earlier than 16:55:00). ZERO mathematical subprocesses, CAS or scripts; manual algebraic geometry plus owned metadata only. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only.

## 0. Custody and read scope

All four ordered SHA256 matched before any read (sha256sum, 16:40:36 UTC): 8a643dd3…de26 (field-degree report, 13279 B), b2eddc44…0862 (its artifact.json, 694 B), 6c6fe089…6d7f (compact contract, 13354 B), a5ab487c…f8d5 (whole-mate Euler elimination, 19277 B); full digests are in the owned box READ-SCOPE.md. All four read WHOLE. Inputs 3/4 are consumed only at their accepted 16q/16r interface scope: the contract's conditions 1–4 and source-field identification, and the whole-mate normal form (2)–(3), guard (13) and gauges (11). Nothing else was read: no ledger, provenance followers, tree/univariate/genus reports, live outputs or web.

## 1. Verdict

CONFIRMED at the conditional scope, A–D all CONFIRMED, with limitations in section 4. For every full guarded solution over a characteristic-zero field K with m=3r+1, n=5r+2, the map degree is

    [K(U,V):K(P,Q)] = [K(S,t):K(A,B)] = 3n = 15r+6,   r=1: 21.

This is an exact invariant of a hypothetical solution. It is not a constructed map, an exclusion, a new point, or any global theorem.

## A. Generic-fiber field — CONFIRMED

Checked by hand. With lambda=A, F=K(lambda), E=K(S,t): K[lambda,S,t]/(A-lambda) is K[S,t] via lambda->A (injective on K[lambda] since A is nonconstant), a domain; (A-lambda) meets K[lambda] only in 0, so it stays prime after inverting K[lambda]\{0}. Hence A-lambda is irreducible in F[S,t]. Being irreducible of positive t-degree it is automatically primitive over F[S]; the report's explicit content check (leading coefficient S, t^0 coefficient k(S)-lambda with value -lambda at S=0 because k(0)=0 is an explicit gauge) is also correct. Gauss gives irreducibility in F(S)[t] and [E:F(S)]=3, with E=F(S)(t)=K(A,S,t)=K(S,t). No component is chosen.

Base field: the original base is K(A)=F, and E is a one-variable function field over F (transcendence degree 2 over K minus 1). Allowed changes (nonzero constant scalings, target translation A->A-k(0), mate shear B->B-beta*A-gamma with beta,gamma in K, the base translation S=R-v0, division by the accepted leading scalars kappa_A, kappa_B) each preserve K(A,B) as a subfield of K(S,t) and preserve polynomiality of Abar,Bbar in (p,z), so the degree is invariant under all of them.

Geometric integrality is NOT needed. The degree formula (9) is the fundamental identity sum e_P f_P=[E:F(B)] over the place 1/B=0 of F(B), whose residue field is F; residue degrees [k(P):F] are the correct weights whatever the constant field of E. Constant-field assertion checked: an element alpha of E algebraic over F has alpha and 1/alpha integral over F, hence in every O_P; at the rational place P_0 of section C the residue map is an F-embedding F(alpha)->k(P_0)=F, so alpha in F. Therefore F is algebraically closed in E, and in characteristic zero E/F is regular (geometrically integral). This is a consequence, not a hypothesis.

## B. Weighted bracket and every S-infinity place — CONFIRMED

Weights w(S)=1, w(t)=r, theta=t/S^r. Coefficient bounds put every term of A at weight <=m and of B at weight <=n; A_top=S^m C(theta), C=theta^3+d_r theta^2+v_{2r} theta+a, B_top=S^n D(theta), D monic quintic from B_5=S^2 with D(0)=b. Delta's top piece is -t(S t^3)^2=-S^2 t^7 of weight 7r+2; the competitors -ell t Pi (4r+1), 2u S t^6 type terms (6r+1), u t, 1 are strictly lower for r>=1. Chain rule, orientation A_S B_t - A_t B_S (the same orientation as the whole-mate contribution (l A_k' B_l - k A_k B_l') and as the t^7 coefficient -S^2 from A_3=S, B_5=S^2): A_S=S^{m-1}(mC-r theta C'), A_t=S^{m-r}C', similarly for B, so

    [A,B]_top = S^{m+n-r-1}(m C D' - n C' D),  m+n-r-1=7r+2,

the r*theta*C'D' terms cancel, and (5) mCD'-nC'D=-theta^7 holds with leading coefficient 5m-3n=-1. Confirmed.

Roots: C(0)=a!=0 so no zero root; at any root alpha in an algebraic closure, n C'(alpha)D(alpha)=alpha^7!=0, so C'(alpha)!=0 (three distinct roots) and D(alpha)!=0. Characteristic zero is used only for n!=0. Confirmed.

Places over S=infinity: x=1/S, theta=x^r t. x^m(A-lambda)=theta^3+c_2(x)theta^2+c_1(x)theta+c_0(x)-lambda x^m with c_j in K[x] exactly because deg f<=r+1, deg h<=2r+1, deg k<=m; reduction at x=0 is C. Monic over F[[x]] forbids a place with theta infinite. Hensel with simple roots lifts each irreducible factor C_i of C over F to an irreducible factor over F((x)); each gives one place with e=1, uniformizer x, residue field F[theta]/(C_i). Residue degrees sum to deg C=3=[E:F(S)], so these are ALL places over S=infinity: no extra place, no ramification, no same-field splitting assumed (over a splitting field they are three rational branches; over F they are one place per factor, counted once with its degree). Since C in K[theta] and lambda is transcendental, factor degrees over F equal those over K; this is not load-bearing. x^n B=sum x^{n-rj}B_j(1/x)theta^j=D(theta)+O(x) by deg B_j<=n-rj, residue D(alpha)!=0, so ord_P B=-n exactly at every such place and the weighted pole degree is 3n. Confirmed.

## C. Every finite-S place; the unique t-pole branch — CONFIRMED

Let v be a place of E with v(S)>=0. If v(t)>=0 then B in K[S,t] is regular: no pole. If v(t)<0, z=1/t has v(z)>0 and A=lambda divided by t^3 gives Q(S,z)=S+f(S)z+h(S)z^2+(k(S)-lambda)z^3=0 with every coefficient in O_v (lambda in F), so reducing mod m_v forces v(S)>0. Hence O_v contains F[S,z]/(Q) and the centre of v is the F-rational maximal ideal (S,z). Q_S(0,0)=1, so that point is smooth; its local ring is a DVR of E, and the only valuation ring dominating a DVR with the same fraction field is the DVR itself. This is the whole force of the argument: there is exactly ONE place with v(S)>=0 and v(t)<0, so a second t-pole branch with p infinite (or anything else) cannot exist. The residue field is F (rational point), z is a uniformizer (S ≡ u z mod m^2), t has a simple pole.

Coefficients rechecked from Q: order z gives s_1=-f(0)=u; order z^2 gives s_2=-f'(0)u-h(0)=-d_0 u-(1-u d_0)=-1, valid at u=0 (then S has order 2 but z stays the parameter); order z^3 gives s_3=lambda+d_0-u v_0. So p=(S+z^2-u z)/z^3=s_3+O(z) is regular and p(0)=lambda+d_0-u v_0. Formula (3) rechecked term by term: S t^3+f t^2+h t+k with S=pz^3-z^2+uz, t=1/z sums to k(S)+p+v(S)(pz^2-z+u)+d(S)(pz-1), so Abar(p,0)=p-d_0+u v_0 and Abar_p=1 there; Abar(p(0),0)=lambda is consistent. The accepted inverse condition (contract condition 4 for B, whole-mate (3) for A, both invariant under the gauges) makes Bbar in K[p,z]; substituting the embedding E->F((z)) gives B=Bbar(p(z),z) in F[[z]]: no pole at P_0. Confirmed.

Other affine models: B, Delta, A_t are polynomials in S,t, so any place with S and t regular is a regular point for them regardless of singularities of any model; the only smoothness used is Q_S(0,0)=1 at the one point that matters. Exhaustion: each place of E restricts to a nontrivial place of F(S) (E/F(S) is algebraic), which is either finite (this section) or S=infinity (section B). Confirmed.

## D. Degree formula, transport, controls — CONFIRMED

(9) is the fundamental identity for the place 1/B=0 of F(B): ramification index at a pole P is -ord_P B because 1/B is a uniformizer below, residue field below is F, and the identity holds with equality for a finite separable extension (characteristic zero). B is transcendental over F since it has poles. Pole divisor of B: three places over S=infinity of order n with residue degrees summing to 3, nothing else (sections B, C). So [E:F(B)]=3n, and F(B)=K(A)(B)=K(A,B) inside K(S,t). Transport rechecked: U=g^2(1+gp), V=1/g inverts g=1/V, p=V^3U-V; z=p^2+ell p-u-g is triangular in (g,p); p=Pi(S,t)=t-u t^2+S t^3 and z=1/t recover (p,z) from (S,t), and Pi(pz^3-z^2+uz,1/z)=p identically. Hence K(U,V)=K(S,t)=E and K(P,Q)=K(Ahat,Bhat)=K(A,B), so [K(U,V):K(P,Q)]=3n over the original K.

Degree bookkeeping: 3n=21 at r=1 is the product of the place count 3 (=[E:F(S)], the "rank 3" of the cubic fibre) and the per-place pole order n=7 ("auxiliary degree 7"); neither factor is the map degree. 28m*28n=112*196 is the Bezout ceiling for the fibre count, a different invariant. No theorem excluding map degree 21 or 15r+6 is charged or invented; equality of a numerical degree with some other cover says nothing about monodromy or Galois structure, which remain unknown here.

Controls, both rechecked by hand. (1) B+t with A fixed: w(t)=r<n keeps both leaders and the three order-n poles (x^n t=x^{n-r}theta -> 0); at P_0, B is regular and t has a simple pole, so B+t has one extra pole of degree 1 and no others (still in K[S,t]); the same formula (9) gives 3n+1. It fails the full source equations: [A,B+t]=Delta+A_S with A_S=t^3+f't^2+h't+k'!=0, and t=1/z violates inverse polynomiality. (2) C=(theta-1)^3, D=(theta-1)^5: mCD'-nC'D=(5m-3n)(theta-1)^7=-(theta-1)^7!=-theta^7, so these leaders violate (5); they show monicity plus nonzero constants alone allow a repeated root with D vanishing on it, i.e. (5) is load-bearing. (3) u=0: S=-z^2+O(z^3), place ramified over S=0 but still rational with parameter z, p regular, B regular; no change to the count.

## 2. Gained invariant and remaining scope

Gained: any full guarded solution is a Keller pair whose source map has exact generic-fibre degree 3n=15r+6 over K, with the generic P-fibre geometrically integral over K(P) (section A) and with B totally of pole type n,n,n at the three S-infinity places and regular at the single t-pole place. Scope unchanged: conditional on every residual row (12), guard (13), the accepted leading forms A_3=S, B_5=S^2 and both inverse conditions; no point, properness, unit or exclusion follows, and 3n>1 is merely consistent with the accepted nonautomorphism.

## 3. One cheapest proof-side discriminator (no task or compute authority)

NEW/PROVISIONAL, manual, derived only from A–D. Delta is in K[S,t], so its poles on the generic fibre X_lambda are the four boundary places: order 7r+2 at each S-infinity place (Delta ~ -t(S t^3)^2, theta=alpha!=0) and order 1 at P_0 (Delta=(z+u-ell p-p^2)/z with p(0)^2+ell p(0)-u a nonzero polynomial in lambda). Hence deg Z(Delta|X_lambda)=3(7r+2)+1=21r+7 (28 at r=1), all at affine places. The affine fibre is smooth (lambda transcendental avoids the finitely many critical values), and at an affine point dB|X = -(Delta/A_t)dS or (Delta/A_S)dt, so the finite ramification of B is exactly deg Z(Delta) plus e_{P_0}(B)-1. Riemann–Hurwitz for B (degree 3n, three places of index n over infinity): 2g-2 = -6n+3(n-1)+21r+7+(e_{P_0}-1) = 6r-3+e_{P_0}. Riemann–Hurwitz for S (degree 3, unramified over infinity): the finite ramification is deg Z_aff(A_t)+(1 if u=0), and A_t has poles of order 2r+1 at each S-infinity place and order 1 at P_0 iff u!=0, so it equals 6r+4 in both cases and 2g-2=-6+6r+4, i.e.

    g(X_lambda)=3r  (3 at r=1),  and then e_{P_0}(B)=1.

Cheapest test: compare 3r with any independently computed genus of the generic P-fibre (the uncharged fibre-genus line, not read here); a mismatch is a contradiction on one side. Wall: one manual recheck of the four displayed pole orders, about 20 minutes; no CAS. Bounded quantity: one integer per r. This is beyond restating the coefficient rows because it is a global topological consequence of them; it is NOT raised as an OPEN because it may duplicate the uncharged fibre-genus work, which an own-only collision check cannot see.

## 4. GAPs and limitations

- GAP (imported, not verified here): A_3=S and B_5=S^2 exactly, with kappa_A kappa_B=c!=0, are the accepted 16q gate's result cited by the whole-mate report; the weight analysis in B needs them. Also imported at accepted scope: contract conditions 1–4, whole-mate (3) as the exact A inverse condition, and the contract's two-ring ordinariness of P,Q (used only for K(P,Q)=K(A,B), which holds even as rational functions).
- No Galois, monodromy or ramification-type conclusion about the degree-3n cover is made; section 3 is provisional and unreviewed.
- Read/tool scope: exactly the four charged inputs, whole; date/ls/sha256sum/wc metadata only; no CAS, scripts, subprocesses, process census, network, AWS, SSH or agents. Owned outputs: this file and box/f10-full-map-field-degree-gate-fable5-20260909/READ-SCOPE.md. No Seal and no charge_basis line are authored.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check (none raised); no corpus scan.

<!-- BODY-END -->
