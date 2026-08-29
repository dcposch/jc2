# `(8,12)` order two: affine-Faber to total-Rees Gate-A audit

Date: 2026-08-26

Status: **FAIL-CLOSED SOURCE AUDIT.  THE DELAYED-LOAD RAY HAS THE
NORMALIZED EXACT-SQUARE AFFINE-FABER SYSTEM AS ITS LITERAL GRADE-FOURTEEN
CENTRAL FACE.  THE GENERIC COMPLETE-LOCAL THEOREM AND THE NEW `A`-FACE
FORMAL `J` ARC ARE NOT YET TOTAL-REES CONSEQUENCES.  THE NATURAL
MINIMAL-VALUATION LIFT OF THE `A` ARC ALREADY HAS A NONZERO UNLOADED
GRADE-TEN FORCING TERM.**

## 0. Typed verdict

There are three different assertions that must not be conflated.

```text
WEIGHTED_ROW_SECTION
  The coefficient-homogeneity substitution reproduces the normalized
  ordinary rows after division.  This is an exact identity on D(Lambda),
  but its central point is coefficient-irrelevant.

DELAYED_LOAD_P2
  With k10=Lambda^12*K10, k6=Lambda^8*K6,
  k2=Lambda^4*K2 and literal C=Q^2, the Lambda^14 face is exactly the
  normalized affine-mu2 ordinary-Faber receiver.  This statement passes.

TOTAL_REES_GATE_A
  Every source arc on the named face is represented by a two-sided
  integral chart, with all coefficient normals, moving variables, decks,
  targets, torsion, and divided-row forcing retained.  This statement is
  not proved and therefore fails closed.
```

In particular, neither the generic complete-local `J=0` theorem nor the
normalized exceptional `A`-face `J` arc may presently be promoted to the
literal total-Rees ledger.  The `A` arc is an exact normalized
ordinary-Faber formal arc, but its most direct minimal-valuation source
substitution is rejected before the affine-Faber grade is reached; see
Section 6.

## 1. Literal one-parameter source

The reviewed one-parameter source is

```text
Phi_l =
 r_l(C, Lambda^2*k10, Lambda^6*k6, Lambda^10*k2)
 - Lambda^(12+l)*delta_l,                           (1.1)

(delta1,...,delta7)=(0,mu2,0,mu4,0,mu6,J/4).
```

It is the flat pullback of the strict two-parameter source on the unit
chart `R=1+tau` under

```text
Lambda=tau^3*varrho,
C_i=B_i                    (i even),
C_i=R*B_i                  (i odd),
J=R*j.                                             (1.2)
```

All three finite lower loads and all four targets remain variables.  The
registered boundary operation is, in this order,

```text
Iint=(Phi_1,...,Phi_7):(Lambda*J)^infinity,
H=((Iint+(Lambda)):(C0,...,C6)^infinity).           (1.3)
```

Thus an exact row substitution whose `Lambda=0` image has
`C0=...=C6=0` is not by itself a chart of the registered boundary open.

## 2. What the reviewed chart chain actually proves

### 2.1 First normal chart

The exact square-division blowup is

```text
K=z^4+p*z^2+c*z+r,
N=n3*z^3+n2*z^2+n1*z+n0,
C=K^2+Lambda*N.                                    (2.1)
```

In coefficients this is

```text
C6=2p,                       C5=2c,
C4=p^2+2r,                   C3=2pc+Lambda*n3,
C2=c^2+2pr+Lambda*n2,        C1=2cr+Lambda*n1,
C0=r^2+Lambda*n0.                                   (2.2)
```

On `D(Lambda)` the inverse is triangular and divides the four square-normal
defects by `Lambda`; its Jacobian is `8*Lambda^4`.  Every pulled source row
is divisible by `Lambda^2`.  At the first divided grade the complete
principal part is

```text
[(3/8)*N^2/K + k10*K^(5/2)]_-.                     (2.3)
```

On `D(k10)`, vanishing of the seven reviewed first-normal rows forces the
quartic `K` itself to be a square.  Consequently the literal nonzero
boundary octic

```text
C=(z^4-1)^2
```

does **not** lead to the common-load affine-Faber receiver with unit
`k10`: at grade two only `k10` is present, and `K=z^4-1` is nonsquare.

### 2.2 Generic square and higher contact

On the reviewed generic square open one adjoins a Kummer coordinate

```text
Lambda=sigma^2,
L=z^2+p/2,
K=L^2+Lambda*R,
N=L*M+Lambda*S,                                    (2.4)
```

and on the half-weight ray

```text
M=sigma^3*A,
S=sigma*C,
R=cs*z+rs/4.                                       (2.5)
```

The literal source is divisible by `sigma^10`, and the complete grade-ten
receiver is

```text
[(3/8)*(L*A+C)^2/L^2 + (5/16)*k10*R^3/L]_- .      (2.6)
```

This already contains forcing and is not an ordinary unforced Faber row.
On `D(p*k10)` its reduced support has `C=R=0`, with `A` free.  The reviewed
higher-contact cone

```text
R=sigma^2*(B0+sigma*B1+...),
C=sigma^4*(E0+sigma*E1+...),
A=A0+sigma*A1+...                                  (2.7)
```

has divided grades fourteen and fifteen.  For example its grade-fourteen
Laurent receiver is

```text
[(3/4)*A0*E0/L
 -(3/8)*B0*A0^2/L^2
 +(5/32)*k0*A0^2/L]_- .                            (2.8)
```

A moving square modulus `L -> L+sigma*ell` changes the next receiver by
`ell*partial_L(2.8)` and changes the ordinary rows by the derivative of
the Laurent-to-Faber connection.  These are genuine source terms, not a
choice of notation.

The promoted D1 contact-`a=8` theorem keeps the first `k6` and `mu2`
forcing and eliminates that fixed contact on `D(p*k10)`.  Its hypotheses
explicitly exclude `p=0`; it neither reaches nor contradicts the collision
common-load receiver below.

### 2.3 Collision and the unproved overlap

At `p=0`, the proposed collision atlas first separates roots by

```text
p=-2*rho^2
```

and then forms the actual Rees algebras of

```text
J1=(rs,cs,c0,c1),
J2=(a0,a1) on V(J1).                               (2.9)
```

Six standard charts cover the nonzero `J1`/`J2` directions valuatively.
The complement `V(J1+J2)` is the proposed exact-square/all-load receiver.
However, the existing design explicitly leaves open the two-sided maps
between these Rees charts and the specialized source clients, their Rees
kernels and torsion, and the common-load complement.  This is the break in
the reviewed chain.  A list of normalized equations on that complement is
not yet an overlap theorem.

## 3. Why coefficient homogeneity is not Gate A

Faber homogeneity gives the exact identity

```text
r_l(Lambda^(8-i)*a_i,
    Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)
 =Lambda^(12+l)*r_l(a,k10,k6,k2).                  (3.1)
```

Thus the graph

```text
C_i=Lambda^(8-i)*a_i                               (3.2)
```

has prime kernel, is `Lambda`-torsion-free, and has the explicit inverse
`a_i=C_i/Lambda^(8-i)` on `D(Lambda)`.  Pulling (1.1) through (3.2) and
dividing by `Lambda^(12+l)` gives the normalized ordinary rows exactly.

Nevertheless (3.2) sends the whole central fibre to

```text
Lambda=0, C0=...=C6=0,                             (3.3)
```

which is removed by (1.3).  It is a useful one-sided row section and a
chart of a possible further weighted modification, but it is not a
two-sided chart of the registered source open.  In particular it does not
prove that a normalized point is an accessible total-Rees boundary point.

Keeping the nonzero base octic `(z^4-1)^2` repairs (3.3), but then the
reviewed first-normal grade (2.3), with only the unit `k10` load present,
excludes its nonsquare quartic.  The coefficient-homogeneity route and the
literal-nonzero-coefficient route therefore cannot be spliced without an
additional valuation chart.

## 4. The delayed-load ray: a valid central-face map

There is a clean alternative which keeps the literal coefficient octic
nonzero.  Make the integral toric substitution

```text
k10=Lambda^12*K10,
k6 =Lambda^8 *K6,
k2 =Lambda^4 *K2.                                  (4.1)
```

Then the three effective loads in (1.1) are all

```text
Lambda^14*(K10,K6,K2).                             (4.2)
```

The graph kernel

```text
(k10-Lambda^12*K10,
 k6-Lambda^8*K6,
 k2-Lambda^4*K2)                                  (4.3)
```

is prime; the graph ring is a polynomial domain and has no `Lambda`
torsion.  On `D(Lambda)` the inverse is the displayed division by
`Lambda^(12,8,4)`.  This proves the row map for the chosen valuation ray.
It does not by itself prove fan coverage or commutation with every later
colon operation.

At literal `C=Q^2`, the unloaded `F12` tail vanishes because `Q^3` is a
polynomial.  Dividing the source by `Lambda^14` therefore gives exactly

```text
H=sqrt(Q)*(K10*Q^2+K6*Q+K2),                       (4.4)

R1=R3=R4=R5=R6=R7=0,
R2=mu2.                                            (4.5)
```

The target and load schedule is

| source datum | literal power | relative to grade 14 |
|---|---:|---:|
| all three delayed lower loads | `Lambda^14` | `0` |
| `mu2` target | `Lambda^14` | `0` |
| `mu4` target | `Lambda^16` | `2` |
| `mu6` target | `Lambda^18` | `4` |
| `J/4` target | `Lambda^19` | `5` |

On `D(K10)`, the leading receiver has the two-sided unit change

```text
beta=K6/K10,        gamma=K2/K10,
mubar2=mu2/K10,

K6=K10*beta,        K2=K10*gamma,
mu2=K10*mubar2.                                      (4.6)
```

No Kummer coordinate is required for this scalar leading-face
normalization, and `K10` must remain as a unit variable in subsequent
grades.  This differs from a full weighted normalization of the complete
ordinary source.  The latter would require a square root with
`q^2*K10=1`, would have deck `q -> -q`, and would produce weighted ratios
`K6/K10^3` and `K2/K10^5`, not (4.6).

Equations (4.1)--(4.6) establish `DELAYED_LOAD_P2`.  They do not identify
the transverse coefficient completion with the normalized ordinary-Faber
completion.

## 5. Square-normal forcing on the delayed ray

Write the unique square division near the literal exact square as

```text
C=Q^2+E,             deg(E)<=3.                    (5.1)
```

The unloaded part begins

```text
(Q^2+E)^(3/2)
 =Q^3+(3/2)*Q*E+(3/8)*E^2/Q-(1/16)*E^3/Q^3+... .  (5.2)
```

The first two terms are polynomial.  The first possible unloaded forcing
is therefore the negative part of `(3/8)E^2/Q`.  The delayed loaded terms
begin

```text
Lambda^14*K10*(Q^2+E)^(5/4),
Lambda^14*K6 *(Q^2+E)^(3/4),
Lambda^14*K2 *(Q^2+E)^(1/4).                       (5.3)
```

If `ord_Lambda(E)=d`, the first unloaded normal forcing has grade `2d`,
whereas the first loaded linear normal term has grade `14+d`.

```text
d<7:   an unloaded normal equation occurs before the affine face;
d=7:   (3/8)E0^2/Q forces the grade-14 face;
7<d<14: the central affine face comes first, but unloaded normal forcing
         precedes the loaded normal differential;
d=14:  unloaded quadratic and loaded linear normals tie at grade 28;
d>14:  the loaded linear normal term precedes its unloaded square.
```

Consequently the grade-fourteen equations are ordinary Faber rows exactly
on the zero-normal exact-square section.  A complete total-Rees chart has
inhomogeneous forcing unless it proves that the relevant normal variables
vanish to a sufficiently high order.  The formal IFT block in normalized
coordinates cannot be imported merely because (4.5) matches its central
fibre.

## 6. The exact rational `A` point and its first source obstruction

The frozen normalized producer uses

```text
F=Q^2+N,
Q=z^4+p*z^2+c*z+r,
N=n3*z^3+n2*z^2+n1*z+n0,
D=(p^2-4r)/4,                                      (6.1)
```

and the `A`-face scaling

```text
c=t*x,
n3=t^3*v,
n1=t^3*(u+p*v/2),
n2=t^2*e2,
n0=t^2*e0,
beta =15*D/8+t^2*b,
gamma=15*D^2/16+t^2*g.                             (6.2)
```

At

```text
(D,p,x,b,g,e0,e2,u,v)=(1,0,1,0,0,0,0,0,-1/20)    (6.3)
```

the three divided odd equations vanish and

```text
4*R7/t^3=-5/32.                                    (6.4)
```

The exact-Q Jacobian in `(u,v,e0)` has determinant `-3125/8192`, so the
normalized formal arc exists.  Its next solved even divided jet is

```text
u=(13/800)t^2+O(t^4),
v=-1/20+O(t^4),
e0=-(21/640)t^2+O(t^4).                            (6.5)
```

This result has dual-AWS producer custody but no hostile review yet.

### 6.1 Necessary terminal tie

On the delayed-load chart, the affine receiver is at grade fourteen and
the source `J` target is at grade nineteen.  If `j0=ord_Lambda(J)`, a
nonzero cubic (6.4) can meet the terminal row only on a ray satisfying

```text
3*ord_Lambda(t)=5+j0.                              (6.6)
```

For the minimal ray with `J` a DVR unit this is

```text
t^3=unit*Lambda^5,
Lambda=s^3, t=s^5                                  (6.7)
```

after a cubic ramification.  Its ramification deck must be retained over a
field containing the relevant roots of unity.  If the already reviewed
square chart `Lambda=sigma^2` is retained simultaneously, a common toric
refinement is `Lambda=q^6`, `sigma=q^3`, `t=q^10`.

### 6.2 Grade-ten rejection of the natural minimal lift

For (6.3), the leading square-normal term is

```text
N=t^3*(-1/20)*z^3+terms of higher t-order.          (6.8)
```

Under (6.7), the unloaded quadratic term (5.2) appears at
`Lambda^10`, strictly before the delayed loads and every target at grade
fourteen:

```text
(3/8)*(1/400)*z^6/(z^4-1)
 = (3/3200)*(z^2+z^-2+z^-6+...).                   (6.9)
```

Thus its raw Laurent coefficients satisfy

```text
h2=h6=3/3200.                                      (6.10)
```

At `p=c=0,r=-1`, the charged ordinary connection gives

```text
R2=h2=3/3200,
R6=h6+(r/2)*h2=3/6400.                             (6.11)
```

There is no source target at grade ten.  Hence the natural substitution of
the normalized `A` arc into the delayed-load chart is not even divisible
through grade fourteen: it is rejected by the literal source at grade ten.
This is exact characteristic-zero algebra, not a modular observation.

For general `j0>=0`, the same leading normal square occurs at grade

```text
10+2*j0.                                           (6.12)
```

Positive `J` valuation is allowed by `J`-saturation, so (6.11) is not a
classification of all ramified rays.  At larger `j0`, target jets or other
source corrections may tie and must be emitted.  Scaling the normal `N`
by an extra power of `Lambda` avoids (6.11), but then the normalized
Jacobian and formal arc (6.2)--(6.5) are no longer the divided source
equations.  They must be recomputed with forcing.

The nominal next normalized IFT equation is relative `t^5` (the `t^2`
coefficient after division by `t^3`).  On the minimal ray it would occur at
`Lambda^(67/3)`, or at grade `67` after (6.7).  That number has no source
force until every earlier grade, beginning with (6.9), has been cleared.

## 7. Ordinary rows, forcing, and the connection firewall

The normalized producer reconstructs the frozen **ordinary Faber** rows.
It is not a raw `z`-Laurent classifier.  With raw Laurent coefficients
`h_l`, the first seven ordinary rows are related by the reviewed
unitriangular map; in particular

```text
R2=h2,
R4=h4+(p/2)*h2+(c/4)*h1,
R6=h6+p*h4+(3c/4)*h3+(p^2/8+r/2)*h2+(pc/8)*h1.    (7.1)
```

The nonzero affine target `h2` makes this connection load-bearing.  It is
the reason (6.11), rather than the pair of raw values (6.10), is the source
statement.

The divided rows are therefore:

```text
pure weighted coefficient section: exact ordinary rows, but irrelevant;
delayed-load exact-square central fibre: exact ordinary affine-Faber rows;
first-normal / half-weight / higher-contact charts: ordinary transforms of
  rational receivers with explicit square-normal, moving-base, load, and
  target forcing;
transverse delayed-load completion: unknown until (5.2)--(5.3) and every
  later correction are emitted from Phi.
```

No raw-Laurent support theorem may replace the ordinary rows in the last
line.

## 8. Variables and actions required by the missing chart

The smallest complete client must retain the following data.

| class | mandatory variables/actions |
|---|---|
| literal base | `Lambda`; or `tau,varrho,R` with (1.2) on the overlap |
| delayed loads | `K10,K6,K2`, all moving jets, graph kernel (4.3), and the original finite loads |
| coefficient square | every moving coefficient of `Q`, including tangential `p,D` jets |
| square normals | all four coefficients of `E`; on the `A` fan these include `e0,e2,u,v` and all later jets |
| exceptional `A` fan | `t,x,b,g,e0,e2,u,v`; retain `x` and saturate by it unless the `x=1` chart map is printed |
| targets | complete `mu2,mu4,mu6,J` arcs at powers `14,16,18,19`, without early projection |
| moving centre | either an explicit odd translation coordinate and its rows, or a two-sided unit gauge proving that the frozen centered source has removed it |
| square Kummer | `Lambda=sigma^2` and deck `sigma -> -sigma`, if this predecessor chart is used |
| collision separation | `p=-2*rho^2`, both root orientations, and deck `rho -> -rho` |
| terminal tie | the toric relation (6.6), including ramification/deck data |
| source parity | `z -> -z`; prove rather than assume its identification with `t -> -t` |
| optional load normalization | if a weighted `K10=1` normalization is used, its Kummer coordinate and both sheets; otherwise retain `K10` and use only (4.6) |
| algebraic custody | actual Rees kernels, weak transforms, `Lambda`/`J` torsion and colon checks, and both overlap maps before the central fibre |

The hyperelliptic sign of `sqrt(Q)`, the factor deck used after splitting
`Q`, the order-two source deck, the root-separation deck, and the terminal
ramification deck are separate until explicit overlap maps identify them.

## 9. Smallest missing map and bounded successor

The smallest missing object is not another normalized support
decomposition.  It is a two-sided **delayed-load plus coefficient-normal
total-Rees chart before central specialization**.

It should start from (1.1), impose the prime load graph (4.3), perform
square division (5.1) without deleting `E`, and construct the actual
weighted Rees/dilatation algebra for the valuations of `E`, the moving
coefficients of `Q`, and the `A` parameter `t`.  On `D(Lambda*K10*x)` it
must print the inverse map.  Before setting any exceptional parameter to
zero it must prove:

1. equality of the pulled raw `Phi_l` ideal and the chart ideal, not merely
   equality of radicals;
2. the Rees kernel and absence, or explicit retention, of `Lambda`- and
   `J`-torsion;
3. the exact weak transform of the coefficient-irrelevant ideal, with at
   least one literal `C_i` remaining a unit on the registered open;
4. grade-fourteen identity (4.5) on `E=0` and the complete forcing module
   for `E!=0`;
5. the ordinary connection (7.1), every load and target occurrence, and
   every moving/deck variable in Section 8; and
6. sequential divided coefficients through the first of: a raw unit, a
   certified route, or the terminal grade nineteen.

For the frozen rational `A` point the first mandatory negative control is
exactly (6.9)--(6.11).  A client that reports the normalized `t^3` cubic
before printing this grade-ten coefficient is fail-closed invalid.

Typed endpoints are

```text
GATE_A_MAP_FAIL
  A map, kernel, torsion, omission, connection, or registered-open check
  fails.  Do not import a normalized theorem.

A_RAY_UNIT_BEFORE_P2
  A raw source coefficient before grade 14 excludes that fixed ray.

FORCED_A_FACE
  Grade 14 is reached but coefficient/load/target forcing changes the
  normalized rows.  Recompute the Schur/IFT block from those rows.

PURE_AFFINE_FABER
  The exact divided rows and their complete transverse completion equal the
  normalized ordinary-Faber system.  Only this endpoint licenses the
  generic complete-local theorem and the exceptional formal arc.
```

The grade-ten calculation gives `A_RAY_UNIT_BEFORE_P2` only for the natural
minimal-valuation lift of (6.3).  The overall chart remains
`GATE_A_MAP_FAIL`/pending until the general client is built.

## 10. Cross-lane acceleration delta

Three campaign mechanisms combine unusually well here.

1. The TD6 total-`F` V85 method should be reused as a **chart-identity
   compiler**: retain every source coordinate, clear only registered
   denominators, and seek literal identities of the form

   ```text
   s=sum_i H_i*Phi_i+exceptional_parameter*H.
   ```

   Its fail-closed denominator and omission census is exactly what the
   delayed-load/Rees overlap needs.
2. The generic parity/IFT calculation should become a reusable
   Schur-complement engine.  Given source-emitted forced rows, it separates
   even pivots from the complete odd block, factors the determinant, and
   routes exceptional factors without waiting for a full primary
   decomposition.
3. The promoted D1 `a=8` result supplies the scheduling discipline: derive
   every load/target entrance grade first, compile only the small active
   module at each grade, and keep the full frozen source as an independent
   row bridge.  Here that discipline found grade ten before any expensive
   `P3` computation.

A small software layer can encode valuation maps, graph kernels, inverse
opens, decks, source-variable censuses, ordinary/Laurent transport, and
colon order once, then emit exact-Q and good-prime AWS clients.  Content-
addressed row DAGs should be shared across the TD6, D1, and parity clients;
hostile review can run in the background after a producer endpoint, while
downstream provisional clients consume the frozen bytes.

## 11. Frozen dependencies

The audit charged the following bytes.

| SHA-256 | file | role |
|---|---|---|
| `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` | `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md` | literal one-parameter source |
| `1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de` | `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md` | hostile source review |
| `82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f` | `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md` | source promotion |
| `827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc` | `xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md` | exact first-normal map |
| `27275f3d13471521bec0016d4fbc6e12d5bf8e539deeb4694fe0c01f04b025bd` | `xmodel/max12-812-order2-first-normal-divisibility-jet-review-grok-20260826.md` | first-normal review |
| `2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5` | `xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md` | first support theorem |
| `73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6` | `xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md` | first support review |
| `40790378bfcc7b0e0719038ef0e951712abef570b4865c0bca371409706c9f94` | `xmodel/max12-812-order2-first-normal-pade-support-promotion-20260826.md` | first support promotion |
| `37a7234cee998a0069f33b7a36bb945123b305acd01485a771d8e6ed7dac65fd` | `xmodel/max12-812-order2-generic-square-halfweight-kuranishi-design-20260826.md` | half-weight map |
| `49744ab901f05ae6d8f0163fd195f3b0219e725f051c3aeebf31fcdaa13c4214` | `xmodel/max12-812-order2-square-halfweight-kuranishi-hostile-review-grok-20260826.md` | half-weight review |
| `00640cd4b80b079aa2123a686aad351ae3801ee0f4203aac2f7451c8c6d16c6d` | `xmodel/max12-812-order2-square-a-prolongation-hostile-review-grok-20260826.md` | fixed-base higher contact |
| `a3bbee7bb523bd1d049a4c4654e5843a8f37f372f362e69da514c18c52044f06` | `xmodel/max12-812-order2-square-a-ptangent-hostile-review-grok-20260826.md` | moving-base higher contact |
| `3d847561946751c68a081db55f2f514b3808c22f7ac6e236fcbff10911ab1ce6` | `xmodel/max12-812-order2-square-d1-a8-k6-mu2-v3-promotion-20260826.md` | promoted D1 `a=8` closure |
| `99e45e341925ceb9a01843b4dd36ab99218f97055449c203e792e91e38244434` | `xmodel/max12-812-order2-p0-cech-lowcontact-pell-total-rees-successor-design-20260826.md` | collision/Gate-T design, not a theorem |
| `77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e` | `xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-classification-20260826.md` | corrected ordinary rows |
| `4ddc0e4837e1581129fddad70fc7b5c029d642e644f4fd8ab478a4dec59bded3` | `xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-hostile-review-grok-20260826.md` | connection/support review |
| `fe1193abe8c45c590f7653d96998a7b053e8de0e09a751cd8fb686d2cbf72fc1` | `xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-theorem-20260826.md` | normalized hand theorem; hostile review pending |
| `64f01dc1aa8ed829d3dd93fcc764e547d437aaf0a0c68c7bf8f8f6860371203f` | `xmodel/max12-812-order2-exact-square-affine-faber-exceptional-j-correction-fan-design-20260826.md` | exceptional source design |
| `62e0f17d0679f21a00b1e96d36d68399ee93e22f698f8ed96ef01405c1053046` | `cases/max12_812_order2_affine_faber_a_ift_lift_20260826/RESULT.md` | normalized `A` producer result |
| `1afbeb633080bf6f3d4cf4ec41cd24bcf50821ff5dc843053f047f3f90d07b92` | `cases/max12_812_order2_affine_faber_a_ift_lift_20260826/EVIDENCE.sha256` | dual-AWS evidence manifest |
| `62d92caf30d030d9976f0f76e06a6e7ac405036af5f0e2eecbed30989dabeb8e` | `cases/max12_812_order2_affine_faber_a_ift_lift_20260826/FREEZE.sha256` | normalized producer source freeze |
| `f5af4a1c2e5259000ff266807206b3f4c32576ba9143073239464c71b925e3ce` | `cases/td6_c1_c2_c3_total_f_raw_p12_source_v85tf1_aws_20260826/RESULT.md` | total-`F` certificate pattern |

The generic complete-local theorem's hostile review was still incomplete at
the time of this audit.  The normalized `A` producer has exact-Q and
independent good-prime custody, but hostile review and total-Rees typing are
pending.  No local CAS and no new AWS computation were used for this
bounded audit.

## 12. Scope firewall

This note proves the elementary toric load identity (4.1)--(4.5), the
ordinary normalization distinction (4.6), and the exact natural-ray
obstruction (6.9)--(6.11).  It audits, but does not construct, the missing
total-Rees overlap.  It neither classifies every delayed-load valuation,
promotes the generic IFT theorem, disproves the normalized `A` arc, nor
asserts a strict source, terminal, Taylor, order-two, `(8,12)`, maximum-
twelve, or JC2 result.
