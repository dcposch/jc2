# Q1 small note: characteristic face, diagonal recursion, and the tiny T3 upper block

Blind subtask; only the frozen charged packet/reports/Moh PDF were read. Root mechanically verified the 12 hashes before delegation. All algebra below is proposed or proved here as explicitly labelled; no production chart decision was run. Source-report line numbers refer to frozen files in `/tmp/jc2-lane.Iol3Bk/inputs/`. No exit price is asserted.

## 1. A canonical D2 face is much stronger than global T2 attainment

The char-degree report 15–40 proves canonical effective attainment from Moh pp.150–154; 53–79 gives the full necessary Q family and common top; 120–132 gives the actual F/G D2 faces; 213–215 explicitly leaves full characteristic compatibility unimposed. Moh **Definition 5.1(4), printed p.179**, says the general point of each major tower disc satisfies all hypotheses of Prop.4.6. Thus the first task is to bind the existing D2 chart to this named major disc and canonical T2. It is not enough to invoke Prop.4.6 on an arbitrary necessary-chart point.

For a realized datum, write A=pi^3-beta, P=A^8 for (99,66), and A=pi^4-beta, P=A^7 for D108; beta is the already nonzero D2 separation scale, normalized to 1 in the charged charts. On the covers

* (99,66): (x,y)=(s^-3,s^-3+pi*s), F=s^-9 P^3+..., G=s^-6 P^2+..., Q=s^-5 P*q+...;
* D108: (x,y)=(s^-4,s^-4+pi*s), F=s^-12 P^3+..., G=s^-8 P^2+..., Q=s^-7 P*q+....

The Q orders and face-degree requirements are canonical source consequences needing that Def.5.1(4) route map. Prop.4.6(2)–(4), printed p.170, gives Qface=P*q, q squarefree, all roots of P roots of q, deg q=16/21. These numbers follow from nu=24/28, (-mu2+M2-n)/d2=1 and nu(n-M2)/d2=16/21.

Let cJ=J(F,G), a nonzero constant for the realized pair. The chain rule in char-degree 100–106 gives J(F,Q)=Q_G*cJ, whose leading factor Q_G is 3G^2. Directly computing the cover determinants (-3s^-3 and -4s^-4) gives the **exact face ODEs**

    (pi^3-beta) q' - 16 pi^2 q = cJ (pi^3-beta),
    (pi^4-beta) q' - 21 pi^3 q = cJ (pi^4-beta).

At beta=1 their unique polynomial solutions are

    q99/cJ = pi - 4pi^4 + (48/7)pi^7 - (216/35)pi^10
             + (1296/455)pi^13 - (243/455)pi^16;
    q108/cJ = pi - (21/5)pi^5 + (112/15)pi^9 - (448/65)pi^13
              + (3584/1105)pi^17 - (2048/3315)pi^21.

An in-memory exact SymPy solve substituted these six coefficients into the ODE and returned zero; gcd(q,q')=1 in both normalized cases. Uniqueness does not assume the orbit ansatz: a homogeneous polynomial solution would be (pi^a-beta)^(d/a), with d/a=16/3 or 21/4, which is not polynomial. The leading q coefficient is the global characteristic leader lambda, so

    cJ = -(455/243) beta^5 lambda                 (99),
    cJ = -(3315/2048) beta^5 lambda               (108).

The weights check exactly: beta has weight4/5, lambda143/153, and cJ163/178 (char-degree 90–98, 140–147; cone gate 242–273). This does not reduce the identity by renaming its depth: it transports a coefficient through the **whole canonical face**. The full q-face has 14/13 allowed pi coefficients after multiplication by P, all determined by lambda and beta.

Because q(0)=0 and its linear coefficient is cJ, the same scalar is carried by the physical degree-three coordinate

    e=[x^2 (y-x)]Q = beta^8 cJ                 (99),
    e=[x^2 (y-x)]Q = -beta^7 cJ                (108).

Thus e=-(455/243) beta^13 lambda or +(3315/2048) beta^12 lambda. Its old ambient-Q weights are195/213; its degree-Q normalizer weights are52/60; its transverse (y-x) order is1. All three gradings should be printed rather than conflated. This is a concrete distinguished nonnilpotent coordinate after beta/lambda localization.

**Instrument and price.** Audit Def.5.1(4) and the canonical-to-existential-Q constant-shift map (char-degree 79) for 60–90 minutes; emit the exact characteristic D2 support/face as a small linear map, 30 minutes; then test it against the source quotient for 2–4 hours, one CPU and <=8GiB, no expanded artifact. Count variables after rational pivots; stop the CAS phase at >70 essential nonlinear coordinates. A lower-face valuation or face degree incompatible with the proposed route map refutes its applicability; a single exact full mapped solution with e nonzero refutes a claimed support kill. A proper face system only establishes a necessary face survivor.

## 2. Exact diagonal lemma and a one-polynomial-per-level Jacobian recursion

Canonical D2 floors imply F(x,x) has degree<=3, G(x,x)<=2 and Q(x,x)<=1. Complete the square and shift the target using the five free target scalars in char-degree 53–59:

    Q = X^3 + pX + q0 - Y^2,

where X=G+constant and Y=F-(bG+c_target)/2. This is a target polynomial automorphism with constant determinant, and it retains all target scalars.

**Proved here.** If deg X<=2, deg Y<=3 and deg(X^3+pX+q0-Y^2)<=1 as univariate polynomials in x, the last polynomial is constant. If deg X=1 its cubic leading degree cannot cancel a square; if deg X=0 then Y is constant. In the degree2 case, after an explicitly retained invertible affine parameter change, X0=t^2+B; coefficient comparison gives Y0=epsilon(t^3+3Bt/2), p=-3B^2/4, and the residual is constant. For a Keller pair the constant case is impossible because both tangential derivatives would vanish. Also B!=0: otherwise both tangential derivatives vanish at t=0, again forcing the Jacobian to vanish. The affine parameter change is an algebraic ring map, not permission to spend another source gauge; its slope rescales the Jacobian constant and must be retained.

Consequently Q-q0' is divisible by z=y-x. In the normalized line parameter, choose the orientation X0=t^2+B, Y0=t^3+3Bt/2. Write X=sum X_r(t)z^r and Y=sum Y_r(t)z^r. At each transverse order r,

    (r+1)[2t Y_(r+1) - (3t^2+3B/2)X_(r+1)] = known R_r(t),

where R_r depends only on earlier levels and on the constant Jacobian at r=0. A fixed Bezout solution of 2t*v-(3t^2+3B/2)*u=1 is

    u=-2/(3B), v=-t/B.

Thus every pair of next coefficients is this particular solution times R_r/(r+1), plus

    (X_(r+1),Y_(r+1)) = (2t,3t^2+3B/2) A_r(t) + particular.

This is an exact chart reduction from two coefficient polynomials to **one** A_r at each level, with pivots only in B and rational integers. Major support bounds are narrow strips: in x^p z^q, p<=3+floor(q/3) for F and <=2+floor(q/3) for G in 99, replacing /3 by /4 in108. The transported support conditions on A_r, every terminal zero condition, both minor-source faces, and the complete characteristic relation remain necessary. Truncating the A_r sequence does not prove a kill.

**Price and refutation.** 2h derive the map and exact support strip/intersection count, 2h implement recurrence and all terminal rows, 4h bounded elimination, <=8GiB. Go/no-go after support count: do not sell this as a <70 chart until counted. A symbolic inverse reconstructing X,Y and every raw Jacobian row is mandatory. A B=0 branch with nonzero raw Jacobian would refute the diagonal lemma application; a missed free polynomial in the Bezout kernel refutes the reduction. The main hoped-for output is a small nonlinear terminal ideal deciding the localized e coordinate, not another shallow Jacobian computation.

## 3. Only one/two high-weight scalar terms of T3 matter

Char-degree 46–51 gives D3=145/227, and 90–96 gives n2=3/4 and intrinsic defect20/25. Moh Prop.3.1, pp.157–159, supplies the recursive monomial weights. Exact enumeration gives:

* 99: allowed lower target monomials are 1,Q,G,F,Q^2,GQ,G^2,FQ,FG. Only FQ (weight154) and FG(165) exceed145.
* 108: among16 allowed monomials, only FQ^2(234),FGQ(243),FG^2(252) exceed227.

Therefore the complete T3 upper block is exactly expressible as

    deg[Q^3-lambda^3 FG+alpha FQ] <=145;
    deg[Q^4-lambda^4 FG^2+alpha FGQ+beta3 FQ^2] <=227.

The coefficient of the equality monomial is forced by the common whole homogeneous forms; beta3 here is a new target scalar, not the D2 beta. All omitted monomials have degree<=D3 and cannot enter this upper block. This adds only **one scalar in99 and two in108**. No T3 leading normalization is needed to prove the following degree consequence.

Let S be the displayed expression. Its target derivative S_G has unique highest term 9Q^2G^2 in99 and12Q^3G^2 in108, degrees242 and333. Other target terms have derivative degrees at most231/324. Since J(F,S)=S_G J(F,G), while deg J(F,S)<=n+D3-2=242/333, the Jacobian is constant or zero. Theorem B (char-degree128–134) excludes zero on the actual attained two-point face chart. This proves the full upper block plus T2/actual faces implies the Keller equation, as anticipated at char-degree215.

**Price.** The symbolic proof and weighted enumeration cost <1h; expression-circuit implementation2h. Dense upper-block bounds are3130/6025 coefficient rows, so a blind expanded Groebner retry remains unpriced. Apply it after the diagonal recurrence; record retained nonlinear count and memory before committing a 4h elimination. A forbidden equal/higher-weight derivative term or a lost upper row refutes the reduction. Properness of the *complete* necessary chart carrying these exact blocks and Theorem B is far stronger than earlier T2-only properness; no such properness has been computed.

## 4. Optional quotient coordinate, with its gap explicit

After lambda localization, monic y-division gives lambda G=H Q+R, deg_y R<D2. H has degree11/9 and fixed whole top y^3(y-x)^8 / y^2(y-x)^7, hence only66/45 lower total-degree coefficients. It is not automatically the old auxiliary h3. If one proves its major valuation>=-1 and R's valuation>=-6/-8, the equality face at pi=0 gives Rface(0)=lambda because Qface(0)=0 and Gface(0)=1 at beta=1. The R-face weights in K_G are192/280, physically cover valuations-6/-8. Forcing Rface(0)=0 by exact two-place h-support would kill the chart.

Polynomial division alone does **not** prove those valuation bounds: cancellation in Q's leading form can spoil them. Price90min for the source-support lemma, then stop or retain all failed-leader strata. This is a concrete small-root route, presently conditional, not an attained floor or identified h3.
