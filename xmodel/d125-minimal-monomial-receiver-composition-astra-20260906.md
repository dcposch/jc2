# F2 minimal monomial receiver: exact degree-(15,25), J=c gamma² composition

Status: **PROVISIONAL COMPOSITION / PREFLIGHT**, 2026-09-06. Parent's terminal gate has accepted the conditional standard-F2 to three degree-(30,50), J=x³ polygon implication; this packet proves a smaller coordinate presentation of exactly those receiver families. No primary-chain replay, source builder, CAS, classifier, solver or AWS work. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.

## Result

The extra unramified map proposed by root is valid and loses no receiver coefficient data. Every accepted receiver becomes a **polynomial** pair `(A,B)` of degrees `(15,25)` with `[A,B]=c gamma²`, `c!=0`, and one of these exact Newton polygons:

| case | N(A), degree 15 | N(B), degree 25 | raw coefficient counts |
|---|---|---|---|
| unequal | `(0,0),(0,15),(9,6),(2,1)` | `(0,0),(0,25),(15,10),(1,0)` | `83+215=298` |
| common_3 | `(0,0),(0,15),(9,6),(3,0)` | `(0,0),(0,25),(15,10),(5,0)` | `94+241=335` |
| common_4 | `(0,0),(0,15),(9,6),(9,0)` | `(0,0),(0,25),(15,10),(15,0)` | `115+296=411` |

Counts include every lattice point of each closed polygon, before prescribed faces, monicity, scalar/vertex guards or any other equations. Pick's formula and independent literal lattice enumeration agree. The lower reported degrees and smaller bounding box are exact, **not a measured solving advantage**; the map is a lattice bijection, so it does not reduce the number of coefficient slots relative to the accepted degree-(30,50) polygon presentation.

The conditional implication is

`actual polynomial standard F2 pair (75,125) -> one of these three polynomial monomial-J receivers`.

The hypotheses and external theorem dependencies of the accepted incoming F2 reduction are unchanged. This is not an assertion that Roy B0 is necessary, not a global degree-125 reduction proof, and not a reverse lifting theorem. Excluding every correctly guarded necessary receiver would be useful; properness of a receiver ideal alone would **not** certify a Keller counterexample.

## 1. Exact coordinate maps, coefficient bijection and sign

Let `(U,V)` be the accepted degree-(30,50) receiver in variables `(x,y)`. All three polygons are contained in `i>=j>=0`. Define

`S(U)(gamma,pi)=U(gamma,pi/gamma)`.

A monomial `x^i y^j` maps to `gamma^(i-j) pi^j`, so S takes every supported polynomial to a polynomial. The exponent map is integral with determinant 1; its inverse is `(a,b)->(a+b,b)`, or

`U(x,y)=A(x,xy)`.

Thus coefficient values are carried literally, without mixing or denominators. Every displayed vertex and its nonzero coefficient is carried to the corresponding vertex. Total degree after S is the old x-exponent, at most 15 or25 and attained at the transported upper vertices. The coordinate determinant is `Jac S=gamma^-1`; hence

`[S(U),S(V)]=gamma^-1 S([U,V])`.

In particular J=x³ becomes J=gamma² with the **same scalar and no sign change**.

Equivalently, use the accepted pair P1,Q1 before the old inversion. Its lower-support inequality is `i<=4j`, and its upper-face inequality is `-i+5j<=5m`, where m=3 or5. Replace the old involution T5 by

`T4: x -> gamma^-1, y -> gamma^4 pi`.

Its exponent map is `(i,j)->(-i+4j,j)`, so nonnegative gamma exponents follow exactly from `i<=4j`, and total degree `-i+5j` is at most `5m`. Also `T4=S o T5` and `Jac T4=-gamma²`. If `[P1,Q1]=d`, then `[T4(P1),T4(Q1)]=-d gamma²`. The earlier source swap has its own minus sign; none is silently discarded. Dividing the second target by a nonzero scalar can give the desired convention. The direct inverse of T4 is `gamma=x^-1, pi=x^4 y`; it is an involution after relabeling variables, in the Laurent ring only.

### Complete Jacobian coefficient rows

The presentation change is stronger than a pointwise implication. For source supports `i>=j`, every potentially nonzero coefficient of `[U,V]` has index `(I,J)` with `I-J>=1`. Indeed a bracket contribution from `(i,j),(k,l)` has `I-J=(i-j)+(k-l)`; if this sum is zero then i=j and k=l, so its determinant `i*l-j*k` is zero. Thus there are no hidden negative powers after multiplication by gamma^-1.

Every nonzero full Jacobian coefficient row is transported unchanged under

`(I,J) -> (I-J-1,J)`, with inverse `(a,b)->(a+b+1,b)`.

The target row `(3,0)` becomes `(2,0)`. This proves equality of the full coefficient ideals after the explicit coefficient-variable renaming, including any carried vertex/scalar inverse rows; identically zero rows can be retained on either side. It does **not** turn a subset, projection or unexpanded source formula into a certified complete row stream. No such stream is built here.

## 2. Exact outer face, both quartic cases

Use the accepted normalization of the selected initial root to 1. Before the final map, the common primitive face after its double-root cut is

`R0'=(y+x^-5)(x^5 y)^2 h(1+x^5 y)`,

where h has degree two, `h(1)!=0`. The two accepted quartic cases are

`h(w)=w²-3w+3`, or `h(w)=(w-rho)²`, `rho²-3rho+1=0`.

All nonzero scalar factors of the common root are absorbed into the nonzero target face scalars. Substituting T4 literally gives

`H=pi²(pi+gamma) [gamma² h(1+pi/gamma)] = pi² S3(gamma,pi)`.

There are no negative powers after expansion; H is homogeneous of degree five and monic in pi. The exact alternatives are:

| quartic pattern before the cut | S3, with coefficient of pi³ equal to 1 | coefficient kappa of gamma³ |
|---|---|---|
| `(2,1,1)` | `(pi+gamma)(pi²-gamma*pi+gamma²)=pi³+gamma³` | `1` |
| `(2,2)` | `(pi+gamma)(pi+(1-rho)gamma)²` | `rho` |

In the second row the expanded cubic is

`pi³+(3-2rho)gamma*pi²+(2-rho)gamma²*pi+rho*gamma³`.

This uses `rho²=3rho-1`, so `(1-rho)²=rho`; it is not a label-based choice of a golden slope. Both conjugate roots of `rho²-3rho+1` are retained. They are nonzero and distinct from 1, and the simple and double cubic factors are distinct. In the first row the cubic is squarefree in characteristic zero. Both formulas are in the root-normalized coordinates **before any further slope normalization**.

For every polygon case,

`A_15=lambdaP H³`, `B_25=lambdaQ H⁵`, `lambdaP*lambdaQ!=0`.

In particular the shared corner coefficients at `(9,6)` and `(15,10)` are `lambdaP*kappa³` and `lambdaQ*kappa⁵`, while the coefficients of pi^15 and pi^25 are lambdaP and lambdaQ. These values, their relation, the two root branches and the original scalar must be kept when a forced-face model is used. A bare polygon envelope is a weaker necessary family.

## 3. Inner face coefficients are also transported literally

This section carries the face shapes already derived in the terminal producer; it does not extend the primary successor classification.

For the unequal case, the transported face has direction `(5,-7)` and is necessarily of the form

`A_face=a gamma² pi + b gamma⁹ pi⁶`,

`B_face=d gamma + e gamma⁸ pi⁵ + f gamma¹⁵ pi¹⁰`.

Their full bracket is

`-a*d gamma² + (2a*e-6b*d)gamma⁹ pi⁵ + (5a*f-3b*e)gamma¹⁶ pi¹⁰`.

Because this is the target-weight face, the literal equations are

`-a*d=c`, `2a*e-6b*d=0`, `5a*f-3b*e=0`,

with `b=lambdaP*kappa³`, `f=lambdaQ*kappa⁵`. All five endpoint/face coefficients are nonzero. This is a transported block, not a proof that the rest of the Jacobian coefficients vanish.

For common_3, the primitive face `x^-1(x³y-mu)²`, `mu!=0`, maps to

`G3=gamma(gamma*pi-mu)²`.

For common_4, `x^-3(x⁴y-mu)²` maps to

`G4=gamma³(pi-mu)²`.

Their directions in the new coordinates are `(1,-1)` and `(1,0)` respectively. In either case the faces of A and B are exactly

`lambdaP*kappa³ Gk³`, `lambdaQ*kappa⁵ Gk⁵`,

with the same mu. The scalars follow by comparing the shared `(3,2)` primitive corner with H, whose coefficient there is kappa. No independent face scalars are added. Both faces commute identically, as required; the nonzero target is supplied by lower terms. The assertion that these common faces have a double root is part of the accepted producer's face derivation; no new common-face classification is undertaken here.

## 4. Monicity and scalar normalization: exact scope

Independent target rescaling by lambdaP^-1 and lambdaQ^-1 makes the pi^15 and pi^25 coefficients equal to 1. It changes the Jacobian scalar from c0 to

`c=c0/(lambdaP*lambdaQ) != 0`.

Thus monicity alone is a same-field operation on the guarded locus; it does not keep the old numerical value of c. The common outer H remains as above.

For monic A,B, let tau be nonzero and set

`A_tau= tau^-15 A(tau*gamma,tau*pi)`,

`B_tau= tau^-25 B(tau*gamma,tau*pi)`.

Every term of the outer faces has total degree 15 or25, so **both entire outer faces, including all slope ratios and kappa, are unchanged**. The bracket becomes

`[A_tau,B_tau]=c tau^-36 gamma²`,

since the target rescalings contribute tau^-40, differentiation contributes tau², and the monomial target contributes another tau². Over an algebraic closure choose `tau^36=c` to set the scalar to 1. No same-field existence of such a root is asserted; with c variable this is not an automatic rational scheme isomorphism or a nilpotent-support theorem.

This scaling preserves the entire literal polygon supports and every nonzero vertex. It preserves the common-face families too: `mu -> mu/tau²` for common_3, and `mu -> mu/tau` for common_4. For the unequal case the low endpoint a changes to `a/tau^12`; the corresponding high endpoint and middle coefficient change to `d/tau^24` and `e/tau^12`, while b and f stay fixed. The three displayed face equations transform consistently. Therefore simultaneous monicity and c=1 are licensed **geometrically over the algebraic closure**, with the stated guarded source-face data, not by setting additional endpoint coefficients arbitrarily.

For example, after monicity the unequal face forces

`e=(5/3)a*kappa²`, `d=(5/9)a²/kappa`, `c=-(5/9)a³/kappa`.

Consequently one cannot also set a=1 while independently fixing c and kappa. This explicit relation prevents an over-normalized terminal chart.

## 5. Boundaries and the Moh comparison

The new `(15,25)`, J=c gamma² presentation aligns in **outer degree and Jacobian exponent** with the historical `(25,15;21;2;k=2)` receiver after exchanging the low/high names. That is not an identification of the source families, characteristic data, rings of parameters or lower coefficients. No Moh minor/pole condition, approximate-root lift, or Strinz/Roy coefficient dictionary has been supplied here.

The root distinction is concrete: the squarefree H has projective root multiplicities `(2,1,1,1)`, and the golden H has `(2,2,1)`. These cannot be identified by an invertible linear source change with the specific historical top `pi²(pi-gamma)³`, whose multiplicities are `(2,3)`. This only rules out that immediate linear top-form identification; it does not rule out a nonlinear/filtered relation or prove different moduli. The public carrier quadratics were already present in the pinned source record. No novelty priority is asserted.

At the receiver level S is a genuine coefficientwise equivalence with the accepted larger polygons. By contrast, recovering an original Keller pair still requires undoing T4 and the earlier negative-power cuts, proving cancellation of every negative power, and checking the polynomial source, original degrees and desired normalization data. A point satisfying receiver rows is not known to meet those conditions. For a tiny negative control, `(gamma,gamma²*pi)` has Jacobian gamma², while its T4 inverse has first coordinate x^-1 and is not polynomial. This fixture is not claimed to satisfy the large exact polygon/face guards, so it does not refute an as-yet-unproved stronger reverse theorem.

If one later defines a full parameter ideal, every coefficient row of `[A,B]-c gamma²` must be retained. Exact vertices and c may be guarded by explicit inverse equations; target translations can instead fix nonzero constants if desired, without changing the bracket or other faces. A model using the forced outer/inner faces must retain all their relations and both golden conjugates, not only the names of the branches. No ideal or builder is produced in this desk packet, and no properness or exclusion is claimed.

## 6. Controls, pinned input and terminal custody

Read whole: the terminal Fable gate `xmodel/d125-published-chain-gate-fable5-20260906.md`, SHA `5be50d001d285481233c8de415b2f4d22411a22cb930a0c1db287c0579b3cd7b`. Its prior producer is pinned at SHA `9b439af269c23e349615d3e404e0732c9c7f491a9342d5500e061aab91ad4e88`, and its exact control script at `5de0795dff082796b86e6612332f9c5584b4db2ddb2c6e21f7005af69b242e48`. This task accepts that gated chain with its stated external dependencies; it does not reread/reprove the primary chain or assume the gate covered arbitrary original coordinates.

Owned `box/d125-minimal-monomial-receiver-composition-20260906/check.py` uses standard-library exact rational polynomial dictionaries and reduction modulo `rho²-3rho+1`. It checks both coordinate Jacobians and signs, the inverse and composition maps, the nonnegative full-row index shift, literal substitution of both initial root faces, expanded golden coefficients, all three inner-face formulas, the scaling exponent and unchanged outer faces, six lattice counts independently by Pick and enumeration, and a negative reverse-lift example. Both ordinary and `-O` runs pass. Genuine wrong-map and wrong-golden-coefficient mutations are fed to the same verifier and fail with nonzero exit. These are small controls, not a full-ideal expansion or a second proof of the incoming theorem.

Registration, input pins, replay and custody are in that owned box. Each command is capped at 30 wall seconds, 25 CPU seconds and 512 MiB. No live positive-face receiver gate body/code/log/receipt or protected project was read, and no shared ledger or earlier artifact was edited. All writers finish before terminal handoff. Root retains the decision to commission an independent composition gate and any later computation. **STOP after this map/preflight.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14145`.
- Body SHA-256:
  `ad0581a0cd7e9879fb547c05ef1ea3ec8a8f2f4b63fac262adbbd12c97c041ad`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
