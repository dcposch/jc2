# F10 complete compact solutions: exact full-map field degree

2026-09-09. NEW/PROVISIONAL manual theorem-interface proof. Basis0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only. First exact local check16:28:32 UTC; conservative stop16:38 UTC. ZERO mathematical subprocesses.

## 1. Exact conditional conclusion

For EVERY characteristic-zero field K and integer r>=1, a hypothetical FULL guarded solution of accepted16q/16r, with m=3r+1,n=5r+2, has

    [K(U,V):K(P,Q)] = 3n = 15r+6.                 (1)

In particular r=1 gives field degree21, not3 and not the product of the source coordinate degrees112 and196. This is the degree of the ENTIRE reconstructed source map, not the rank of a separate module or covering. It is conditional on every residual, inverse-polynomiality condition and nonzero-top guard. No solution, ideal properness, source exclusion, map-degree classification or JC2 conclusion is established.

The proof counts all poles of the mate on the normalization of the generic A-fiber. It works over K(A) itself and counts residue degrees, so geometric irreducibility after scalar extension is not an additional hypothesis. A rational smooth boundary place is identified explicitly.

Only the two pinned accepted reports in PINS.json were read WHOLE. No other report, theorem-classification source or web text is a premise. Their normalization and birational source maps supply the exact identification in section7; all pole calculations below are independently derived.

## 2. Normalize without changing the generated field

By16r, nonzero constant output scalings, target translations and the mate shear B -> B-beta*A-gamma reduce the full pair to

    A=S t³+f(S)t²+h(S)t+k(S),
    B=sum_(j=0)^5 Bj(S)t^j, B5=S²,
    [A,B]_(S,t)=Delta,
    Delta=1+u t-ell t Pi-t Pi²,
    Pi=t-u t²+S t³,
    f=S d-u, h=1-u d+S v, k(0)=0,              (2)

with deg d<=r, deg v<=2r, deg k=m, a=[S^m]k nonzero, deg Bj<=n-rj and b=[S^n]B0 nonzero. These are full equations, not just the upper Euler reconstruction. The guard gives both a,b nonzero; neither is normalized to1 here.

Each displayed scalar change preserves K(A,B). The accepted inverse conditions say that BOTH substitutions

    S=p z³-z²+u z, t=z^-1

are ordinary polynomials in K[p,z]. For A one has the exact formula

    Abar(p,z)=k(S)+p+v(S)(p z²-z+u)+d(S)(p z-1). (3)

Thus Abar(p,0)=p-d0+u*v0 and its p derivative there is1. No value of u is excluded.

Put lambda=A, F=K(lambda) and E=K(S,t). The polynomial A-lambda over F is irreducible: K[lambda,S,t]/(A-lambda) is the domain K[S,t], and localization at nonzero polynomials in lambda remains a domain. It is primitive as a polynomial in t over F[S], since its leading coefficient is S and its constant coefficient at S=0 is -lambda. Hence it is irreducible over F(S), and its t-degree is exactly3. Consequently

    [E:F(S)]=3.                                  (4)

Here lambda is transcendental and F(S) is a genuine rational-function field over F. This proves the generic fiber has one function field E; no component is silently chosen.

## 3. The literal leading identity forces three distinct nonzero roots

Give S weight1 and t weight r, and put theta=t/S^r. The bounded highest-weight pieces of (2) are

    A_top=S^m C(theta), C=theta³+F2*theta²+H1*theta+a,
    B_top=S^n D(theta), D monic of degree5, D(0)=b.

F2,H1 here denote highest-weight scalar coefficients, not a residual or a field. The full target has highest weight7r+2 and piece -S²t^7: Pi has highest-weight piece S t³, and every other term of Delta is strictly lower for r>=1.

A direct weighted chain rule, retaining its orientation, gives

    m C D' - n C' D = -theta^7.                   (5)

Indeed the r*theta derivative terms cancel, and m+n-r-1=7r+2. The monic highest term is consistent because 5m-3n=-1. This identity is derived from the full Jacobian, not imported from a standalone initial-ODE existence result.

As a!=0, no root alpha of C is zero. At any root in an algebraic closure, (5) gives

    n C'(alpha)D(alpha)=alpha^7 !=0.

Therefore C has exactly THREE distinct roots, and D is nonzero at every one. Characteristic zero makes n nonzero. This accounts for all repeated-root, common-root and zero-root possibilities directly from the literal equations and guard.

## 4. Every place over S=infinity and its exact B pole

Let x=1/S and theta=x^r t. Multiplying A-lambda by x^m gives a MONIC degree-three polynomial in theta over F[x], with reduction C(theta) at x=0. The coefficient bounds in (2) are precisely what makes all its coefficients regular in x. There is no possible root at theta=infinity, since the polynomial is monic over the valuation ring.

At each distinct root alpha of C, the invertible derivative C'(alpha) recursively solves this equation in F(alpha)[[x]], with theta(0)=alpha. Each next coefficient is determined by division by that nonzero derivative. This is the elementary simple-root formal expansion; x remains a uniformizer. Equivalently, each irreducible factor of C over F defines one unramified place of E above S=infinity with residue field F(alpha). All factors together exhaust the degree-three extension (4), and their residue degrees sum to3. C has coefficients in K and lambda is transcendental, so its factor degrees over F are the same as over K. One may equally count three branches after splitting C, but no same-field splitting is assumed.

At each such place the mate satisfies

    x^n B = D(theta)+O(x).

The right side has nonzero residue D(alpha) by (5). Hence B has pole order EXACTLY n at every one of these places. The weighted sum of these pole orders, using residue degree over F, is

    n * sum_(P over S=infinity) [k(P):F] = 3n.    (6)

In this sum there is one P per irreducible factor of C over F, not one summand of that factor's degree for every conjugate root. Over a splitting field there are instead exactly three degree-one branches.

Neither cancellation of a mate leader nor hidden ramification changes this count: both were ruled out by (5) and the invertible formal derivative.

## 5. All remaining places: the unique t-infinity boundary

Consider ANY place of E over a finite place of F(S). If t is regular there, every Bj(S)t^j is regular, so B has no pole. Suppose t has a pole and set z=1/t. Dividing A-lambda by t³ gives

    Q(S,z)=S+f(S)z+h(S)z²+(k(S)-lambda)z³=0.    (7)

Since z has positive order and all coefficients are regular at a finite S-place, reduction forces S=0. Thus no finite nonzero S value can hide a t-pole.

At (S,z)=(0,0), Q_S=1. Solving (7) formally for S gives ONE smooth branch, with coefficient field F and local parameter z. It is the only branch at that point because the completed local equation is a power-series ring F[[z]]. The first coefficients are

    S=u z-z²+O(z³).                               (8)

For the second coefficient use f(0)=-u,f'(0)=d0,h(0)=1-u d0. Its equation is s2+u*d0+(1-u*d0)=0, so s2=-1. Thus (8) is valid even when u=0; in that case S has order2 rather than1. In both cases t has pole order1 and the place is rational over F.

Now

    p=(S+z²-u z)/z³

is regular by (8). The accepted ENTIRE inverse-polynomiality of B therefore makes Bbar(p,z) regular at this place. There is NO B pole here. Formula (3) identifies its residue explicitly:

    p(0)=lambda+d0-u*v0.

It is also visibly a smooth point of Abar=lambda, because Abar_p(p,0)=1. The preceding formal calculation was essential: merely exhibiting this finite-p boundary point would not by itself have excluded a different t-pole with p infinite. Equation (7) and its unique branch exclude that possibility.

This exhausts the places relevant to B: every place lies above a finite S-place or S=infinity by the finite extension (4); the finite ones either have regular t or are the one branch just analyzed. Singularities of another affine model cause no extra poles, since the polynomial functions are regular at every valuation centered on that affine chart.

## 6. From the pole divisor to the actual extension degree

The elementary function-field degree formula used here is the following. For a nonconstant function b in a one-variable function field E/F, the finite extension E/F(b) has degree equal to the degree over F of its pole divisor on the normal complete curve:

    [E:F(b)] = sum_(P a pole of b) (-ord_P b)*[k(P):F]. (9)

This is the valuation degree formula above the infinity place of the rational field F(b): its uniformizer is 1/b, so each ramification index is -ord_P b. The finite normalization of that valuation ring has total degree equal to the sum of ramification index times residue degree. Characteristic zero ensures separability; no classification of polynomial maps or Keller degrees is involved. This standard divisor/finite-extension fact does not require the curve to be smooth in the original affine coordinates or geometrically integral over F.

Here B is nonconstant by its poles in section4, so (9) applies. Sections4–5 identify its ENTIRE pole divisor; (6) yields

    [K(S,t):K(A,B)]=[E:F(B)]=3n.                 (10)

The rational place in section5 also prevents a hidden algebraic constant-field factor: an element of E algebraic over F and its inverse are integral at that place, and its residue embeds that algebraic field into the residue field F identically on F. Therefore the algebraic closure of F inside E is just F. The proof of (10) did not need to assume geometric integrality, or silently multiply by a number of geometric components. It used residue degrees over F throughout.

## 7. Source-field identification and exact limits

The accepted16q maps are birational and give

    K(U,V)=K(g,p)=K(p,z)=K(S,t),
    g=V^-1, p=V³U-V,
    z=p²-g+ell*p-u,
    t=z^-1, S=pz³-z²+uz,
    p=t-u t²+S t³.

The same report proves the resulting P,Q are ordinary on the WHOLE source plane by its two-ring argument; no lost divisor is being treated as a separate component. The allowed constant scalings/translations/mate shear in section2 do not change the generated two-function field. Therefore K(P,Q) corresponds exactly to K(A,B). Equation (10) proves (1) over the original field K, with no extension needed for the conclusion.

No degree-three-module argument was used or is sufficient for (1). Likewise the source polynomial degrees28m,28n are different numerical invariants from this finite field degree3n. An exact positive degree larger than1 is consistent with the conditional nonautomorphism already supplied by16q; it is not a constructed map or a further contradiction. No theorem restricting Keller maps of degree21 or15r+6 is imported, and no automatic follow-on task is authorized.

## 8. Manual changed-hypothesis controls and cheapest discriminator

1. Dropping mate inverse-polynomiality: replace B by B+t, keeping A. The degree envelopes and both highest-weight leaders remain unchanged because weight(t)=r<n. At the unique boundary place of section5, B was regular but t has a simple pole, so B+t has an additional pole of order1. At each S-infinity place it still has pole order n, since n>r. It has no other poles by the same finite-place argument. Thus its field degree on the same generic A-fiber is 3n+1. This changed object does NOT retain the full Jacobian (its bracket changes by A_S) and is not a compact/source point. It is an exact control showing why leaders and the three infinity branches alone are insufficient and why the inverse condition is load-bearing.

2. Dropping the literal leading identity: take the factored monic leaders C=(theta-1)³,D=(theta-1)^5. Their constants are nonzero, but C has a repeated root and D vanishes there. The left side of (5) is -(theta-1)^7, not -theta^7. Hence a count of three unramified B poles cannot be inferred from monicity and degree bounds alone. This is a changed-leader control, not an ODE solution or a full pair; no high-degree expansion is used.

3. Boundary parameter control: u=0 gives S=-z²+O(z³), so that place has S ramification2. Nevertheless z is still the local parameter, p remains regular, and B has no pole. Incorrectly assigning S pole/zero order1 there would change the geometry but cannot be justified by the generic-u calculation. The second-order coefficient -1 in (8) is the cheapest exact check of this special stratum.

The cheapest independent review is precisely the leading determinant (5), the two coefficients of (7), and the exhaustive finite/S-infinity partition, followed by the ordinary valuation formula (9). No coefficient builder, source powers, mathematical subprocess, test, CAS, remote action or new theorem search was performed. The two input hashes were checked before whole reads and are rechecked in terminal custody. Own whole/raised-OPEN checks precede sealing; all writers idle at handoff.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12946`.
- Body SHA-256:
  `9237fe7ac6df044bee4627377c03a2a10bc4fc9e1d9fce832c95fc3b4d102091`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
