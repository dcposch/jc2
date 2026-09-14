# Real-triangle feasibility: exact bounded certificate, nonresonance still GAP

First08:13:05 UTC; stop08:31:05, reserve08:29:05. Seven current-pinned inputs; manual only. No later residue theorem is used. No real-domain resonance or direct nonresonance theorem is proved.

## Domain and honest extension

The endpoint h values give

    2/7<=tau<1/3,  3-3tau<=alpha<=1+4tau.
    tau=(6+t)/21, alpha=(45-3t+7ts)/21,
    0<=t<1, 0<=s<=1.                                  (1)

The interval width is 7tau-2=t/3, proving surjectivity, including the collapsed t=0 edge.

The accepted D/K Bezout identity remains valid for EVERY real tau here: its only parameter denominators are nonzero multiples of

    f=(2tau-1)(3tau-1)(3tau-2),
    e=(1+tau)(6tau-1)/49,

both nonzero on (1). Thus D is a unit and F[V,W]/(E_nu,Q_nu)=F[V]/S for F=Q(tau,alpha) inside R. The guard extends independently: E=Q=0 yields

    c d'-nu c'd=(5-3nu)W*t5*z^7,
    c=1+z+Vz²+Wz³, d=trunc_5(c^nu).

If W*t5=0 in a maximal residue field, degrees give deg(d)=nu*deg(c). But 5/3<nu<=12/7 and no ratio q/p in this interval has 1<=p<=3,1<=q<=5. Hence the guard is a unit. This argument allows complex V,W; no finite-etale extension is assumed or needed.

## One finite exact identity contract

Use the WHOLE accepted integer-coefficient S(tau,V), T(tau,alpha,V)=DP-ell K. Their degrees are

    deg_V S=7, totaldeg_(tau,V) S<=8;
    deg_V T=5, totaldeg_(tau,alpha,V) T<=5, deg_alpha T<=3.

Use the fixed rational UNIT c0=lc_V(T)=10080 to divide

    S=Qdiv*T+Frem, deg_V Qdiv<=2, deg_V Frem<=4.

Three long-division steps suffice; c0^3*Qdiv and c0^3*Frem are integral polynomials. No parameter coefficient is inverted. Form the 9-by-9 matrix M with columns V^i Frem (i=0..4), V^j T (j=0..3), rows V^0..V^8, retaining all zero slots even when Frem drops degree. If adj(M)e_0 supplies A,B, set

    R=c0^15*det(M), U=c0^15*A,
    Wcof=c0^15*(B-A*Qdiv).

    R=U*S+Wcof*T, deg_V U<=4, deg_V Wcof<=6.          (2)

All these polynomials have integer coefficients: A uses four Frem columns, B five, and Qdiv costs at most c0^3. Check the division identity too. If U_i,Wcof_j denote V-coefficients, parameter-degree bounds are 32-i and35-j. Also

    totaldeg_(tau,alpha) R<=40, deg_alpha R=21.         (3)

Derivation: deg_parameter(Qdiv_i)<=3-i and deg_parameter(Frem_i)<=8-i. Matrix column weights 8+i,5+j minus row weights k sum to40; minors and reconstruction give the cofactor bounds. The padded determinant equals, up to sign, c0^-3*Res_V(S,T). Its highest alpha term is proportional to lc(S)^3*Res_V(S,D), nonzero since S=2K² modulo D and D,K are coprime. Thus R is not identically zero, not necessarily nonzero everywhere.

Independent verification reconstructs S,T from their pinned formulas and checks EVERY coefficient of (2), in variable order (tau,alpha,V), canonical rational strings only. It need not trust determinant software. Parameter denominators are forbidden; only nonzero integer coefficient denominators are allowed.

## Fixed positivity test, not an asserted outcome

Set Rhat=21^40*R((6+t)/21,(45-3t+7ts)/21), an integer polynomial of bidegree at most(40,21). Extract its maximal VERIFIED factor (1-t)^j, 0<=j<=40. No other factor is removed. In particular t,s,1-s cannot be discarded.

If Rhat(0,0)!=0, set epsilon to its exact sign; otherwise require a countercertificate or return INCONCLUSIVE. Request the exact Bernstein expansion of G=epsilon*Rhat/(1-t)^j at bidegree(A,21), A=40-j:

    G=sum b_i,jj binom(A,i)t^i(1-t)^(A-i)
                       *binom(21,jj)s^jj(1-s)^(21-jj).

(The second index jj is distinct from the removed exponent j.) Require every b_i,jj>=0 and b_0,0,b_0,21>0. The two corner terms already give strict positivity for ALL t<1 and s in[0,1]; hence (2) proves no common complex root. Exact expansion equality and all signs must be checked independently. Failure of this sufficient test is INCONCLUSIVE, not a refutation. No degree elevation, subdivision, extra factor, sample or automatic retry belongs to this one attempt.

Boundary control: at tau=1/3, D=12(V-1/3)^2 and K=qD by the accepted division formula; S has factor D² and T factor D. Therefore R vanishes identically on the EXCLUDED t=1 edge. This cannot license removing an admissible edge or asserting positivity of the unmodified determinant on the closed square.

## Outcomes and cap

PROVED requires both full identity and positivity witnesses. REFUTED requires exact real-algebraic parameters: one squarefree rational polynomial with an isolated real root, parameter expressions with certified denominator inverses, and exact domain-sign proofs. Supply a monic common factor of degree1..5 of specialized S,T and verify both divisibilities in that coefficient algebra. The guard argument reconstructs a complex leading resonance; it need not be a linked integer pair. No reality of V,W is required. Otherwise INCONCLUSIVE, including any cap or unsupported output.

One prospective registration only: aggregate360 wall/330 CPU seconds,2GiB sampled RSS,16MiB per file, formation plus independent check; unmeasured and NOT authorized here. No solver implementation, coefficient artifact or execution. No new OPEN ID: the remaining quantity is nonvanishing on the whole triangle; the specific bounded test is (2)-(3) plus the fixed Bernstein witness. Real-algebraic zeros off the linked integer lattice are not excluded by any accepted premise. No actual-source or JC2 conclusion. Own WHOLE/degree/denominator/boundary/OPEN/collision review completed08:24 UTC before marker; no unfinished writer or unquantified raised OPEN.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5626`.
- Body SHA-256:
  `d46d0559d12e528d437e2757329ab205a4fc3ae9d875a08dd08ca8dfe0aafe59`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
