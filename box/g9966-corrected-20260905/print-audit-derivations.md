# Source derivation audit, 2026-09-05

This note audits the mathematical chart, not an endpoint ideal. The source is the frozen Moh PDF. `moh-layout.txt` is a fresh `pdftotext -layout` extraction; all `M:` numbers below refer to its physical lines. Printed page numbers were checked on rendered images. In this PDF printed page p is PDF page p−139 (one based), so printed149 is PDF10. The images `moh-p149.png`, `moh-p150.png`, `moh-p152.png`, `moh-p170.png`, and `moh-p179.png` retain the inspected print. These formulas are executed by `source_data.py`, with output `print-audit-source-data.json`; coefficients are generated from arithmetic and polynomial operations rather than copied from the old engine.

## 1. What is input and what is derived

The branch input is `n=99,m=66`, characteristic entries `M1=−66,M2=77,M3=97`, major multiplicities `V2=V3=8`, and the two minor cases `(δ,[multiplicities])=(2,[2,1]),(5/2,[1,1,1])`. The polynomial called `g` by Moh is the engine's degree99 `F`; Moh's first characteristic polynomial is the degree66 `G`. The canonical degree33 and degree11 auxiliary roots are called h2 and h3. They are not Moh's characteristic polynomials T2 and T3.

Moh p150, the two displays immediately after “Recall” and “auxiliary notations” (M:567–582), gives

```
d1=n, d_(j+1)=gcd(n,M1,...,Mj),
q1=M1, qj=Mj−M_(j−1), lambda_j=sum_(i<=j) qi di,
mu_j=lambda_j/dj.
```

Thus `d=(99,33,11,1)`, `q2=143`, `lambda2=−1815`, `mu2=−55`. Printed p152 Prop2.2(1), at the bottom of `moh-p152.png` (M:680 onward), identifies the characteristic y-degrees as `−mu_j` under its stated `Mj<=e` hypothesis. On the present Keller branch the previous characteristic data license T1,T2; the relevant degrees are99,66,55 and their reduced ratio is9:6:5. This last ratio, not the degrees of h2,h3, is used for divisibility of minor multiplicities.

The cube-root indices follow `99/33=3` and `33/11=3`. At infinity, the two leading clusters have h3 multiplicities8 and `11−8=3`, whence the monic form is `P0=y^3(y−x)^8` after placing their directions. Moh p169 Prop4.5 (M:1596–1599) supplies at most two distinct linear factors in the stated `Ms=n−2` case; p170 Prop4.6(1) (M:1632–1635), applied at the top major disc, supplies their common-power relationship. This yields `F_top=P0^9`, `G_top=P0^6`, `h2_top=P0^3`, `h3_top=P0`. With `t=x^−1,w=ty,z=w−1`, the h3 normalized top is generated as `z^8(1+z)^3`.

## 2. Exact radii and the centres actually permitted

The inspected p179 Def5.1(3) display (M:2131–2138) says

```
delta_i = 1 − (n−Mi) prod_(j=i+1..s)[Vj(n−Mj)−dj]
                 / ((n−Ms−1) prod_(j=i+1..s)[Vj(n−M_(j−1))−dj]).
```

In particular the denominator uses `M_(j−1)`, not `Mj−1`. Substitution gives

```
delta3=1−2=−1,
delta2=1−22*5/165=1/3,
delta1=1−165*143*5/(1287*165)=4/9.
```

These are y-radii. Since `z=ty−1`, the z-radii are `1+delta2=4/3` and `1+delta1=13/9`. Clearing denominators generates `t=s^3,z=pi*s^4` and `t=e^9,z=alpha*e^12+Pi*e^13`. Consequently the D2 weight is `3r+4q`, and the D1 exponent of the kth term of a normalized monomial is `9r+12q+k`.

Printed p147 Prop1.2 and its preceding paragraph (M:373–390) identify the unique general point of a disc and its root multiplicity. Def5.1(1) (M:2120–2124) gives `99*8/11=72` g-roots in D2. A deck transform sends D2 to an equal-radius disc containing72 of99 roots. Equal-radius ultrametric discs are equal or disjoint; disjointness would require144 roots. Thus D2 is invariant under every finite Puiseux deck group. Its unique centre truncated strictly below radius1/3 is invariant, so it has no nonintegral exponent. Total degree equal to y-degree places root exponents at least−1. After selecting direction y=x the only remaining term below1/3 is a constant. One source translation sets it to0. The D2 substitution therefore omits no hidden fractional centre.

The nonzero D2 residue alpha has a full degree3 orbit. Each alpha-packet contains exactly24 g-roots. Deck transformations fixing `t^(1/3)` preserve the packet. The D1 disc contains all24 roots of its packet, so the same disjointness argument makes its centre invariant under that stabilizer. Its centre belongs to `k((t^(1/3)))`. There is no exponent in that lattice strictly between1/3 and4/9; consequently no intermediate D1 centre is missing.

For the minor first-splitting disc, all27 minor roots remain in a unique disc until the declared first separation. The full packet is invariant under deck transformations. Uniqueness of this pre-splitting disc and its truncated centre forces integral exponents below the first splitting radius. Hence the complete local inputs are

```
delta2:  y=jet0+u*t+(a2+zeta)*t^2,
delta52: y=jet0+u*t+v*t^2+pi*t^(5/2).
```

At delta2 a2 is the double-root residue at the splitting level. It is not a lower centre term and cannot simply be deleted after writing a double root at zero in the face. At delta52 the deck involution fixes one residue and exchanges two; after the integer centre v has been included, the three residues are0 and an opposite nonzero pair. These statements carry the first-separation hypothesis; they are not claims about an arbitrary later disc.

## 3. Coherent systems and the uses of approximate roots

The printed p148 Def1.4 (M:445–461) requires disjoint discs, total multiplicity equal to polynomial degree, and equal generic valuation. Printed p149 Thm1.1 (M:478–483) transfers such a system to a dth approximate root only when d divides every multiplicity. Its statement supplies multiplicities; it must not be read as saying that a single-disc leading polynomial is automatically a dth power.

At D2 the generic g order is `72*(1/3)+27*(−1)=−3`. Complete this point by following each remaining minor ray until its generic g valuation is−3, merging repeated discs. Generic valuation along each root ray is a continuous piecewise rational-affine sum of distances and increases to infinity, so the required rational radius exists. All these added discs lie strictly within the principal minor packet. Its top multiplicity3 is below `d3/(n−M3)=11/2`, so the hypotheses of p191 Prop6.1(2) hold: every negative-order point there is a distribution detector for g,T1,T2. The printed statement is M:2739–2762; the proof at M:2855–2874 explicitly covers radii at least1 as well as below1. Def3.1(4) and its remark, p161 M:1155–1172, then force every added g multiplicity to be a multiple of9 because the degree ratio is9:6:5. The D2 multiplicity72 is also a multiple of9. Apply Thm1.1 twice with d=3. The coherent accuracies become−1 for h2 and−1/3 for h3, and D2 multiplicities become24 and8.

At D1, use all three conjugate major children and complete their system with minor points at g accuracy−1/3. Each major child has24 g-roots, and minor multiplicities remain multiples of9 by Prop6.1. One application of Thm1.1 therefore gives h2 multiplicity8 in each D1 child. It does not justify a second application at D1: eight is not divisible by3. In particular no C2/C3 D1 valuation bound is inferred by treating h3 as a D1 detector.

For either requested minor endpoint an even simpler complete system is available. The target minor disc contains27 g-roots with generic accuracy A=−18 or−9/2. A major disc centred at y=x with radius `r=(A+27)/72` has the same accuracy. This gives r=1/8 or5/16, strictly below1/3, and its full72-root packet remains intact. The pair is complete and both multiplicities are divisible by9. To transfer the *minor face* as well as its total multiplicity, refine the minor discs to a slightly higher common negative accuracy still below−3, retaining the entire major packet. Prop6.1 and Def3.1 force refined minor multiplicities divisible by9. Apply Thm1.1 twice to the refined complete system and use Prop1.2 to read the residues back at the original splitting radius. This transfers the minor factors and their multiplicities to h2 and h3 without identifying a face from total multiplicity alone.

The same coherent systems make h2 a square quasi-approximate root of G: Prop6.1/Prop4.6 distribution gives G multiplicities two thirds those of F and G accuracy two thirds that of F, whereas h2 has one third F multiplicities and accuracy. Thus h2 has half G multiplicity and accuracy at each system point. Def1.5 on p149 (M:488–493) is the applicable definition.

## 4. D2 K2 face and the full allowed h3 face

At D2, Def5.1(4) and Prop4.6(1) yield `F_face=p(pi)^3`, where p is monic of degree24. The selected child has multiplicity8 in p. The centred cover only has pi-powers divisible by3; since p is monic, `p(omega*pi)^3=p(pi)^3` forces `p(omega*pi)=p(pi)`. A zero residue cannot have multiplicity8 in a polynomial in pi^3. Therefore the selected residue alpha is nonzero and its three conjugates, each multiplicity8, exhaust degree24. Thm1.1 and the completed D1 system transfer this to h2. The orbit product is generated by

```
Res_alpha(alpha^3−beta,pi−alpha)=pi^3−beta,
face_D2(K2)=(pi^3−beta)^8, beta=alpha^3 !=0.
```

After one uniform dilation, beta may be1 over the algebraic closure. The eight nonleading equality coefficients are generated from this product; their positions satisfy `3r+4q=96`. K2's valuation follows `ord_t(h2)=−1`, hence normalized floor `3*(33−1)=96`.

Similarly h3 order is `8*(1/3)+3*(−1)=−1/3`, yielding normalized floor `3*(11−1/3)=32`. Enumerating the entire degree11 lower triangle gives exactly two equality slots `(r,q)=(4,5),(8,2)` in addition to the fixed leading `(0,8)` term. The permitted face is initially `H=pi^8+kappa*pi^5+ell*pi^2`. No theorem licenses deletion of the two slots.

The inspected last line of p149 Thm1.2 (M:495–507) says `ord h_j(sigma_i) >= (lambda/d)*j`. With `h2=h3^3+C2*h3+C3`, `deg_y C2,deg_y C3<11`, and accuracy−1, this gives orders−2/3 and−1. The equality of the total-degree33 tops in h2 and h3³, followed by monic division in y with both remainders of y-degree below11, forces total-degree bounds21 and32 for C2 and C3. Normalize them by t22 and t33 respectively; their slots therefore start at r=1. Their D2 floors are64 and96. Lattice enumeration gives

```
U=U10*pi^10+U7*pi^7+U4*pi^4+U1*pi,
V=V9*pi^9+V6*pi^6+V3*pi^3+V0,
(pi^3−beta)^8=H^3+U*H+V.
```

Since `deg(UH)<=18` and `deg V<=9`, the pi21 coefficient forces `3*kappa=−8*beta`. The complete identity has no further condition on ell. The executable Q-linear coefficient elimination, `print-audit-face-control.py`, gives

```
kappa = −8*beta/3,
U10 = 20*beta^2/3−3*ell,
U7  = −520*beta^3/27+8*beta*ell,
U4  = 1510*beta^4/81−20*beta^2*ell/3,
V9  = −U1−1528*beta^5/243+40*beta^3*ell/27,
V6  = 8*U1*beta/3+28*beta^6−1510*beta^4*ell/81+20*beta^2*ell^2/3−ell^3,
V3  = −U1*ell−8*beta^7,
V0  = beta^8.
```

Both ell and U1 are free at face level. Every displayed pivot is−1; there is no division by ell or beta. Substitution into the full polynomial identity returns exactly0. The old kappa=0 face leaves pi21 coefficient−8*beta and fails whenever beta is nonzero.

Crucially, unrestricted low-q K2 output coordinates do **not** automatically impose the C2/C3 floors. For instance at t5 a free `z^21` output perturbation divides by the top h3 `z^8(1+z)^3` with C2 quotient

```
z^10−3z^9+6z^8−10z^7+15z^6−21z^5+28z^4−36z^3+45z^2−55z+66.
```

Its normalized C2 weights start at15, below64. The exact quotient/remainder check is in the same JSON control. Thus a replacement that merely adds h3 equality terms to the old unconstrained K2 outputs is still an enlargement of the true approximate-root chart. This enlargement is safe for a unit implication if coverage is proved, but a point on it is weaker than a point satisfying the source C2/C3 conditions. The direct C2/C3 construction allocates the full ambient coefficient triangles, imposes all coefficients below64/96 as explicit equations, and solves them only by Q* pivots. It does not infer a face or remove equality unknowns from a floor.

## 5. The h2 D1 rows and all outer exponents

Root distances give

```
ord_t F(sigma1)=24*(4/9)+48*(1/3)+27*(−1)=−1/3,
ord_t h2(sigma1)=−1/9.
```

Consequently `ord_e K2>=9*(33−1/9)=296`. Under `z=e^12(1+Pi*e)` each D2 monomial has exponent `3W+k`, `W=3r+4q`. The weight96 face product vanishes through exponent295 because `(z^3−t^4)^8` contains e296. Terms at W97 require k=0,...,4 to vanish, and W98 require k=0,1 to vanish: exactly the seven old h2 D1 rows. These are coefficient equations, not a typed D1 face. At exponent296 a polynomial in Pi of degree8 remains; its lower coefficients are not forcibly zero. The leading coefficient is generated from the selected orbit factor and is `(3*alpha^2)^8`.

The canonical h2 is the cube approximate root of F, so

```
F=h2^3+A2*h2+A3,
G=h2^2+B1*h2+B2,
deg_y(A2,A3,B1,B2)<33.
```

The missing h2² term in F is the characteristic-zero approximate-root definition, printed p148 M:463–468, not a group normalization. Because the top F and G forms already equal h2³ and h2², monic Euclidean division gives total-degree bounds65,98,32,65 respectively. For a block Q of total-degree bound D define `K_Q=t^D Q(t^-1,(z+1)/t)`; it has slots `r,q>=0,r+q<=D,q<=32`. The normalized F/G contribution acquires one extra t because each total-degree bound is one below its containing degree.

Thm1.2 at D2 and D1 yields the following inequalities. Every entry in the last two columns is computed as cover times `(D+required order)`, not independently chosen:

| block | D | D2 required order | D2 floor | D1 required order | D1 floor |
|---|---:|---:|---:|---:|---:|
| A2 |65|−2|189|−2/9|583|
| A3 |98|−3|285|−1/3|879|
| B1 |32|−1|93|−1/9|287|
| B2 |65|−2|189|−2/9|583|

D2 coefficients strictly below each floor vanish. The equality coefficients remain unknown. At D1, expansion of `(1+Pi*e)^q` gives rows `sum_(3r+4q=W) binom(q,k)c_(r,q)=0` whenever `3W+k<threshold`. This derives every old outer offset, including the finite last offset7. In particular the lists of old pivot counts are controls on linear algebra, not mathematical input.

## 6. Minor faces, pole ceilings and Jacobian exhaustion

Write P for the h3 minor face. In delta2 the at-level centre a2 records the double residue and define rho as minus the other residue divided by3. The product from the input partition is `P=zeta^2(zeta+3*rho)`, with rho nonzero. This definition spends no source action. In delta52 the cover involution generates the resultant orbit polynomial `Res_alpha(alpha^2−c,pi−alpha)=pi^2−c`, so `P=pi*(pi^2−c)` with c nonzero. The powers are generated as `h2_face=P^3`, `F_face=P^9`, `G_face=P^6`, using the complete/refined system from §3 and Prop6.1 distribution. Monicity is exact because outside-packet factors have leading constants−1 raised to the even multiplicities8,24,72,48.

For y-radius delta the h3 order is `3*delta−8`. If t=s^L with L the denominator of delta, normalized local floors are `L*(degree+order)`. Hence:

| branch | h3 order | K3 floor | h2 order | K2 floor | F order | KF floor | G order | KG floor |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| delta2 |−2|9|−6|27|−18|81|−12|54|
| delta52 |−1/2|21|−3/2|63|−9/2|189|−3|126|

The pole exponents are18/12 on t and9/6 on the denominator2 cover. Every local coefficient **strictly below** its floor is zero. At equality it is the indicated nonzero P power, not zero. The frozen `raw_minor_support` uses an inclusive `<=0` test, so blindly running it through its last support power would incorrectly zero the equality face. A safe full schedule must replace those equality rows by face differences or stop zero rows strictly below the ceiling. In addition to F/G rows, K2 local rows below27/63 and the corresponding P³ equality are independently necessary and may reduce computation.

For the normalized global polynomials `KF=t^99 F`, `KG=t^66 G`, direct differentiation in `x=t^-1,y=(z+1)/t` gives

```
t^163 J(F,G) = 99 KF KG_z −t KF_t KG_z −66 KF_z KG +t KF_z KG_t.
```

The t-power r is global Jacobian degree163−r. Every degree above0 must vanish; degree0 is a scalar. The leading homogeneous degree163 vanishes from the common powers. Stages1 and2 may partition degree162 rows for historical control purposes, but a full chart must eventually include every positive-degree coefficient, not only occupied historical labels. No Jacobian row with degree0 should be set to0 if the purpose is a necessary Keller chart. One may retain the scalar as an unknown, optionally localizing it if the instrument demands a genuine nonzero-J chart. A full positive-degree chart survivor with zero scalar is a necessary-chart point and does not supply a Keller pair.

## 7. Gauge accounting and promotion conditions

Two projective directions are placed at y=0 and y=x by two independent linear source choices; source translations do not change these directions. Target scalings make F,G monic. The canonical root monic conventions follow internally. Uniform source dilation, compensated by target scalings, sends `beta -> beta*lambda^-4`; it supplies one beta=1 normalization and must not also set rho or c to1. The two source translations `(x,y)->(x+A,y+B)` act independently on the major constant and the minor constant. The major constant is set to0 using B−A. If jet0 is retained free for the requested controls, the remaining diagonal translation is retained as chart redundancy, not silently spent a second time. If jet0 is fixed to0 for a separate computation, the exact translation map must transport all other coefficients and the controls.

The delta2 at-level a2 is retained regardless of this ledger; deleting it by a parameter division would lose the u=0 stratum. Neither rho nor c is assigned a numerical value except when constructing an explicit point. Hc_11_0 is free. Every other allowed h3 term has positive z-power, so `h3(x,x)=Hc_11_0`; diagonal translation preserves this value. It cannot be removed by that residual translation. Approximate-root definitions, monic division, Q* coefficient pivots and changes from y to z coordinates are not extra group spends.

A unit on the enlarged full necessary chart implies a unit on the source image only after this coverage argument. A unit after specializing ell, a2, Hc_11_0, rho/c, or an otherwise unrestricted remainder coefficient does not kill the branch. A rational point is claimed only for the explicitly enumerated rows and localizers that it satisfies. In particular the gate's old diagnostic points may legitimately fail the newly imposed C2/C3 equations; that failure should be recorded at the pre-stage source block and does not contradict the gate's finite diagnostic statement.

## 8. Coverage of the complete canonical remainder parametrization

The underlying parametrization has a source-to-chart map without a generic-leader assumption. For any normalized source pair F,G, let h2 be the unique canonical cube approximate root of F over k[x], and h3 the unique canonical cube approximate root of h2. Monic Euclidean division then uniquely defines C2,C3,A2,A3,B1,B2 in

```
h2=h3^3+C2*h3+C3,
F=h2^3+A2*h2+A3,
G=h2^2+B1*h2+B2.
```

The remainders have the y-degree bounds and total-degree boxes already derived above. Conversely, any tuple in those coefficient boxes reconstructs F,G. Since the y-degrees of `C2*h3+C3` and `A2*h2+A3` are strictly below22 and66 respectively, the formal polynomial parts of the cube roots are exactly h3 and h2. Thus the missing squared terms encode the canonical approximate-root definitions, while B1 is retained because h2 is only required to be a square *quasi*-approximate root of G. No condition identifies h2 with the canonical square approximate root of G.

Every normalized source pair with the declared branch data has all coefficients in these ambient boxes. The preceding source arguments prove all imposed D2, D1 and minor equations. The h3 change from raw z-monomials to `z^v(1+z)^j` is triangular with diagonal1. The exchange that keeps the equality coordinate E82 free and solves Hc_8_3 has rational unit leader1. Each incidence elimination has a nonzero rational pivot, so it describes the entire solution locus as a polynomial graph; no branch with a vanishing parameter leader is excluded. The only open conditions are the declared rho or c localizers and the already normalized nonzero beta. Consequently the map from every source object into the necessary chart survives all these eliminations. A unit in this full chart would be a valid obstruction to the branch. Surjectivity from every chart tuple to a Keller pair is neither required nor asserted.

The fresh independent driver `print-audit-generic-incidence.py` derives source incidence before expanding minor centre maps. It allocates22 free h3 coordinates after the forced kappa equation,33 C2 coordinates and37 C3 coordinates:92 in total. The D2 face and D1 valuations produce24 displayed rows and exactly14 Q* pivots with zero residual. Composing the independently derived minor maps gives78/76 pre-incidence coordinates and64/62 final coordinates on delta2/delta52. These results are in `print-audit-generic-incidence-delta2.json` and `print-audit-generic-incidence-delta52.json`. Identity verification is compositional: every generic polynomial row maps to0, then applying the minor coefficient-ring homomorphism maps this zero to0. This avoids needlessly expanding powers of long centre polynomials while proving the same exact identities.

The implementation's replacement of simultaneous `subs` by `xreplace` is valid here because every key is an independent Symbol and every expression is a polynomial. One `xreplace` is precisely simultaneous generator substitution. Iteration resolves the same triangular map; its iteration bound and cycle checks do not authorize division or dropping terms. The ambient scalar zero maps can be applied directly without iterative expansion. A timed probe located the earlier multi-minute delay in repeatedly applying a large simultaneous substitution dictionary to individual scalar coordinates, not in the source incidence equations.

## 9. Additional minor remainder rows from the same printed theorem

The coherent minor endpoint system in §3 licenses Thm1.2 for *every* canonical/quasi remainder, not just the aggregate F/G polynomial. Let L be the cover denominator and a the h3 order (`−2` or`−1/2`). For C2,C3, whose normalization degrees are22 and33, it gives local floors `L*(22+2a)` and `L*(33+3a)`. These equal twice and three times the K3 local floor. Thus the strict C2/C3 zero rows run below18/27 on delta2 and42/63 on delta52. Equality faces remain unknown. Once these strict rows and the h3 leader P are imposed, the K2 equality condition is exactly

```
face_minor(C2)*P + face_minor(C3) = 0,
```

because h3³ already contributes P³ and no higher local h3 term can enter the equality power27/63. This identity permits a small inner proof ideal without any global F/G multiplication.

A first explicit consequence is already visible. C2's minimum normalized t-exponent is8, and its unique slot there is `(8,10)`. At the minor centre z starts at−1, so this coefficient is U10 in local power8 or16, strictly below18/42. Hence the minor source condition imposes U10=0. Combined with the derived D2 face coefficient `U10=20/3−3*ell`, it forces `ell=20/9`. This is an additional theorem-derived row. It is not a gauge spend or a D2-face pin, and it does not contradict ell being free before minor remainder rows.

For outer remainders let b be the h2 minor order (`−6` or`−3/2`). Thm1.2 gives orders at least2b,3b,b,2b for A2,A3,B1,B2. The square quasi-approximate-root argument for G is exactly the one in §3: G has twice the h2 multiplicities and accuracy at each point of the complete system. The local floors are:

| block | unshifted normalization degree | delta2 floor | delta52 floor | effective contribution floors |
|---|---:|---:|---:|---|
| A2 |65|53|124|54 /126|
| A3 |98|80|187|81 /189|
| B1 |32|26|61|27 /63|
| B2 |65|53|124|54 /126|

The effective contribution acquires one t, hence one or two units of local cover power. Every coefficient strictly below the listed floor vanishes; equality faces are not assigned. These inequalities hold simultaneously with the D2 and D1 rows on the same canonical remainder polynomials. They can therefore be added to the full necessary chart, or used as a smaller obstruction ideal, with no extra chart restriction.

The separate exact inner-minor probe has now completed. On delta2 its44 raw rows yield28 strict and5 equality Q* pivots, zero residual, and affine localized dimension31 from the source64 coordinates. On delta52 its65 raw rows yield48 strict and3 equality Q* pivots, zero residual, and dimension11 from source62. Every solved coordinate is retained through its polynomial graph map; rho or c is never a pivot. Both runs derive E82=20/9 and produce explicit rational points. These are **inner-chart** results, before outer and Jacobian rows. Driver, raw rows, full pivot ledgers and rational assignments are `print-audit-inner-minor-probe.py` and `print-audit-inner-minor-delta2.json` / `-delta52.json`.

An independent numeric verification reconstructs all K2 polynomial coefficients at each point (178 and179 nonzero coefficients) and substitutes the full carried minor series by rational sparse arithmetic, without using the symbolic equality reduction. It obtains exactly P³ at local27/63 and zero below, and verifies all strict C2/C3 minor rows. Adding t20*z9 to C3 creates15/26 failures, starting with−1 at local20/40. The independent positive and negative controls are `print-audit-inner-minor-independent-check.py/.json`.
