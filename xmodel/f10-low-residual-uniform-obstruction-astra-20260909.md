# F10 low residuals: a uniform degree obstruction, not full exclusion

2026-09-09. PROVISIONAL manual theorem; one bounded child of the provisional whole-mate Euler reduction. Basis `0d39df3c9fd69c939a8420c54d03228b9077777d` is provenance only. ZERO mathematical subprocesses. Invitation was approximately 11:50 UTC; first exact local check was 11:51:30 UTC. The conservative controlling stop remains 12:10 UTC.

## 1. Outcome and exact dependency boundary

The two FULL low residual identities imply a genuine, limited uniform restriction:

    r >= 2  ==>  deg h >= ceil(r/3).                         (1)

More precisely, if tau=deg h (not the chart variable t), the gauge-invariant polynomial

    D = h B2 - f B1

has exact degree `3tau-r` and an explicit nonzero leading coefficient, except for the exceptional case r=1,tau=0. In particular the stratum deg h<r/3 is impossible for r>=2. This is a consequence of BOTH entire residuals, not a fixed-A test, leading ODE, root simplicity assumption or a computation at finitely many r.

This is NOT a full-system obstruction: the permitted range tau<=2r+1 contains many values meeting (1), including its full-degree stratum. No inconsistency of the remaining coefficients is proved. The exact residual system, its reconstruction, its guard and both inverse-polynomiality conditions remain mandatory. No point, properness, unit certificate, F10 exclusion or JC2 claim follows.

The independently stated polynomial lemma below uses only the displayed two identities and degree hypotheses. Its attachment to the complete reduced system is conditional on the still-provisional Euler report. The three underlying compact-contract/module objects are accepted at 16q. Their historical headers are not a new review debt. The four complete inputs and current hashes are recorded in the owned READ-SCOPE.md and PINS.json; no live Euler review was read.

## 2. Full objects retained

Work over an arbitrary characteristic-zero FIELD K. Let r>=1, m=3r+1, n=5r+2. Retain the normalized complete pair

    A = S t^3 + f(S)t^2 + h(S)t + k(S),
    B = sum_(j=0)^5 Bj(S)t^j,       B5=S^2,

with

    f=S d-u,       h=1-u d+S v,
    deg d<=r,      deg v<=2r,
    deg k=m,       deg B0=n,
    a=[S^m]k !=0,  b=[S^n]B0 !=0,
    deg Bj<=n-rj.

The letters a,b here are the moving leading coefficients remaining after the nonzero output scalings; they are NOT set to one. The parent retains the guard omega*a*b-1, k(0)=B0(0)=0 and the scalar mate shear gauge. In particular

    deg f<=r+1,   deg h<=2r+1,
    deg B1<=4r+2, deg B2<=3r+2.

The FULL two residual equations are, with primes denoting d/dS,

    E0 = k' B1-h B0'-1 = 0,
    E1 = 2k' B2+h' B1-h B1'-2f B0'-u = 0.       (2)

In the actual reduced client the Bj are the entire polynomial Euler reconstruction from d,v,k,u,ell, not new independent variables. Its six upper t-coefficients (t^2 through t^7), both boundary conditions, the two scalar gauges and every coefficient of (2) are retained. Nothing below replaces that reconstruction by freely chosen low coefficients. The appearance of ell only through the reconstructed Bj is not permission to drop ell.

For completeness the parent reconstruction is the descending whole-polynomial recursion

    (j-3S*d/dS) Bj = delta_(j+2)
       -(j+1) f' B_(j+1)+2f B'_(j+1)
       -(j+2) h' B_(j+2)+h B'_(j+2)
       -(j+3) k' B_(j+3),                     j=4,3,2,1,0,

with B5=S^2, higher Bj zero, and target coefficients

    (delta0,...,delta7)
      =(1,u,-ell,ell*u-1,2u-ell*S,-u^2-2S,2uS,-S^2).

The parent proves the two resonances automatic and fixes [S]B3=0 and B0(0)=0. This report neither reproves nor silently strengthens that provisional result. The argument below is valid for any actual polynomials satisfying the listed hypotheses; hence its source attachment can be rerooted in any sound construction of them.

## 3. Entire-row elimination identity

Set N=B1, P=B0'. E0 gives k'N-hP=1. Therefore h cannot be the zero polynomial: otherwise k'N=1, contrary to deg k'=3r>0. It also gives

    gcd(k',h)=1 in K[S].                                      (3)

This means polynomial coprimality including all root multiplicities. No algebraic closure or squarefreeness is used. Since b!=0 and characteristic is zero, deg P=n-1=5r+1. The product hP has positive degree, so the constant 1 cannot affect its leading term. If tau=deg h and H=[S^tau]h, then E0 implies

    deg N=tau+2r+1,
    nu:=lc(N)=n*b*H/(m*a) !=0.                                (4)

Multiply the ENTIRE E1 by h and subtract 2f E0. The B0' terms cancel, giving the exact polynomial identity

    2 k' (h B2-f N)
       = h^2 N'-h h' N-2f+u h.                               (5)

No division by h, k', u, S or a root value has occurred. In terms of the residuals themselves, without assuming (2),

    h E1-2f E0
       = 2k'(h B2-f N) - (h^2 N'-h h'N-2f+u h).              (6)

Thus (5) is a literal polynomial consequence of the TWO given rows with signs fixed, not a substitution into an approximate or leading equation. If desired, once h is known nonzero, E0 together with (5) is equivalent to E0,E1 over K[S], since that domain permits cancellation of the nonzero polynomial h. No such cancellation over an arbitrary nilpotent coefficient ring is claimed.

The rational notation h^3*(N/h)' for the first two terms on the right is only explanatory; the proof uses the polynomial form (5) and retains every zero of h.

## 4. Degree proof and the exact remaining margin

By (4), the leading coefficient of h^2N'-h h'N is

    ((tau+2r+1)-tau)*H^2*nu = (2r+1)*H^2*nu,

and its exact degree is 3tau+2r. This coefficient is nonzero in characteristic zero. Repeated roots and the value u=0 do not alter it.

The other terms -2f+u h have degree at most max(r+1,tau). For r>=2, or for r=1,tau>=1,

    3tau+2r > max(r+1,tau).

Consequently the right side of (5) is NONZERO with exact degree 3tau+2r. It is divisible by k', of degree 3r, so necessarily

    3tau>=r,
    deg D=3tau-r,
    lc(D)=(2r+1)*n*b*H^3/(2*m^2*a^2).                      (7)

This proves (1) and (7). They are field-point necessary conditions for the complete client, conditional only on its stated polynomial presentation. One may exclude the entire low-degree-h stratum for each r>=2; one may NOT promote this to a unit of the original whole ideal.

The comparison fails precisely where it should at r=1,tau=0: then the main degree is 2 and -2f may also have degree 2. In that case h=H is a nonzero scalar. Both sides of (5) have the following forced behavior: its right side has degree <=2<deg k'=3, so it must vanish identically and

    H B2=f N,              H^2 N'=2f-u H.                  (8)

E0 still forces deg N=3 and nonzero leading coefficient. Thus f must have degree exactly 2, with

    [S^2]f = 21*b*H^3/(8*a).

There is no contradiction in these low-row conditions alone. Section 6 checks this exceptional possibility explicitly while preserving the distinction from an Euler-reconstructed mate.

Where the attempted global obstruction loses its margin is now exact, not an inability to find a proof: the allowed degree tau=2r+1 yields deg D=5r+3, exactly the a priori maximum deg(hB2) and deg(fN). The leading term in (7) can be carried by the allowed polynomial D. For smaller surviving tau, (7) forces cancellations in that combination, but does not show they are impossible. No argument here rules out any tau>=ceil(r/3), nor does this label those strata nonempty.

The result is a bounded campaign candidate at this four-input scope, not a history or literature novelty determination. It supplies no additional independent equation to the full ideal: it extracts a useful uniform degree-stratum consequence of equations that were already mandatory.

## 5. Gauges, the u=0 boundary and algebraic scope

The allowed mate change B -> B+beta*A+gamma changes N to N+beta*h, B2 to B2+beta*f and B0 to B0+beta*k+gamma. Therefore D=hB2-fN, (2), (5), and the derivative (N/h)' are unchanged. Its scalar beta does not affect (4), since deg N>deg h. Translation of k by a scalar has no derivative effect. The result does not introduce a new gauge or assume a=1 or b=1.

There is no localization at u. If u=0, then h=1+S v. In particular h is never the zero polynomial; the restriction (1) remains valid. For r>=2 the boundary subcase v=0 has constant h and is excluded by the same proof. If v is nonzero then deg h=1+deg v, so (1) becomes the corresponding necessary degree bound on v; all remaining boundary equations remain in force. For r=1, v=0 is the exceptional case (8), not automatically excluded.

No assumption on roots of h, k' or their discriminants is made. Identity (3) is forced by E0 rather than selected as a generic open set. The theorem is over every characteristic-zero field; no new field extension or embedding is introduced. A parameter-ring formulation of the raw identity (6) is automatic, but the exact degree proof and nonzero-leading-coefficient conclusions are stated only over fields (or separately specified unit-leading strata). There is no undeclared arbitrary-ring degree argument.

## 6. Hand controls: the exceptional cancellation and the missing upper arrow

Here is an exact changed-hypothesis control at r=1, not a solution of the complete reduced client. Take u=ell=0 and

    d=S, v=0, f=S^2, h=1, k=S^4,
    B0=(8/21)S^7-S^4-S,
    N=B1=(2/3)S^3-1,
    B2=(2/3)S^5-S^2,
    B3=(2/3)S^4, B4=0, B5=S^2.                             (9)

All displayed coefficient bounds hold; a=1 and b=8/21 are nonzero. The constants k(0),B0(0) and [S]B3 vanish. Both inverse-boundary conditions hold exactly: at u=0, with p=t+St^3 and y=St^2, A=k+p+S*y, while

    B=B0+N*p+((2/3)S^4-S+p)*y.

This verifies ordinaryness in the accepted rank-three ring without deleting a boundary equation. E0 is zero because B0'=k'N-1. Also B2=fN and N'=2f, so E1 is zero identically and (8) holds. These checks use the full two scalar-polynomial residuals, not evaluation at a point of S.

Nevertheless this is NOT the parent's reconstructed mate: the t^6 coefficient of [A,B]-Delta is

    5 f' B5-2f B5'=6S^3 !=0,

since B4=0 and delta6=0. The first missing arrow is exact. Thus no full-source/Keller point is being exhibited, and this control cannot invalidate a possible future full-system exclusion. It does show that extending (1) to r=1 by ignoring the tied -2f term is false, even if all coefficient bounds, gauges, nonzero top coefficients and both inverse-boundary conditions are retained.

For an actual changed-object check of (2), replace only B2 in (9) by B2+1: E0 stays zero, while E1 becomes 2k'=8S^3, so the claimed low-row compatibility is genuinely lost. This is a hand proof of a changed polynomial, not a programmed toy or a source counterexample. Equally, replacing the -2f term on the right of (5) by +2f destroys its zero right side in (9), giving 4S^2. These controls check the sign and the exceptional cancellation.

The parent section 8 example is not charged as exclusion evidence and is not needed for this theorem. Conversely (9) does not erase the upper equations in the actual task: it marks precisely why the necessary degree test is not a replacement for them.

## 7. Terminal decision

There is a rigorously derived uniform low-degree-h exclusion and exact gauge-invariant degree identity (7). The stronger proposed conclusion that the full low-residual system is incompatible for every r is NOT proved. For the requested all-r full-system exclusion, this one degree/Bézout mechanism ends in NO GAIN beyond the explicitly delimited degree-stratum pruning. No automatic next experiment, new review lane, solver or descendant is authorized.

All mathematical work was hand algebra; no mathematical subprocess of any size, source reconstruction, coefficient script, CAS, numeric test, AWS/SSH, web lookup, blind/cross read, live-review read or shared edit occurred. The report's only mathematical inputs are its four pinned files. Current-input postchecks and final artifact custody are in the owned box. All authorship is restricted to this private leased body and that box. The provisional Euler dependency remains explicit regardless of any later reviewer verdict.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12339`.
- Body SHA-256:
  `46ec8e488153e16eb7924b7ede38d085b2293ef54498222aef112c95a4a58220`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
