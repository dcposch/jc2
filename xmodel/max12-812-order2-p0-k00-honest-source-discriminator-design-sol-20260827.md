# `(8,12)` order two: K00 honest-source discriminator audit and minimal post-saturation incidence

Date: 2026-08-27

Status: **EXACT DESK AUDIT AND EXECUTABLE DESIGN.  NO SATURATION ENDPOINT,
TERMINAL-RECEIVER EMPTINESS, GATE-T, ORDER-TWO, MAXIMUM-TWELVE, OR JC2
VERDICT.  NO AWS JOB WAS LAUNCHED.**

## 0. Verdict

The all-depth K00 replay is a genuine theorem about the frozen raw ordinary
tail rows, but it is not a strict-source point.  The first omitted honest
equation is the terminal target

```text
Phi7 = r7(C,Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)
       -Lambda^19*Jdet/4.                            (0.1)
```

On the literal K00 common-quartic/load core, `r7=0`, so (0.1) is
`-Lambda^19*Jdet/4`.  It kills the **restriction-first** K00 section on the
strict open `D(Lambda*Jdet)`.  It does not decide whether a family with
nonzero transverse corrections can approach that core after the full source
ideal is saturated.  Saturation and restriction do not commute.

The cleanest next honest discriminator is therefore not another raw grade.
It is the small closure-first incidence

```text
K       = (Phi1,...,Phi7):Lambda^infinity:Jdet^infinity,
B_K00   = K + (Lambda) + M_K00,
H_K00   = B_K00:(C6*k10*Jdet)^infinity,              (0.2)
```

with the explicit invariant ideal `M_K00` in Section 7.  This is not yet
implemented.  It should be compiled from the frozen one-parameter source,
run as an exact-Q/good-prime AWS pair, and carry the restriction-first unit
as a negative control.

Notation warning: `Jdet` in this note is the retained nonzero Jacobian
constant called `J` by the one-parameter compiler.  It is unrelated to the
collision correction ideals `J1` and `J2`.

## 1. Frozen inputs

The raw K00 audit and its principal inputs are

```text
b6c1c4ce4cce9cc693d3e7e0b790b3d0d76306d4b1052349d522e215c538a009
  xmodel/max12-812-order2-p0-total-rees-j2-terminal-receiver-cascade-audit-sol-20260827.md
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  frozen tails.json (569 canonical terms)
5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587
  V20 actual-total emitter
0807540484b93ee12b6d6b7ea2b90a7e80418fd29fa7633bc9a8ab3485269f14
  V21 all-depth replay
f702630d71ea4b1168ab993848dc334e67fac4f436273e27fc5fb93637bd34ff
  V21 RESULT.json
```

The exact Rees-chart and routing statements are

```text
50db2706f5a8d435618e615bfc393d2eb7dd22828a9a3fa35ac8a2e685ab15c4
  xmodel/max12-812-order2-p0-total-rees-gate-t-obligation-table-20260826.md
6995a991b1e7803a26bbf5374b10d54a0cda7d17158ad9f1595db76218aadb92
  xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md
```

The reviewed square-component computations are

```text
523a32dd0da666029e2dee1531e0cd0775c0010d07d40ef440dfe5164cf152cf
  exact-square Pell/Chebyshev theorem
eff19a417bef9a9b1c4d4850ba454546e1c946895c5a21acb98c6d523f632fc1
  hostile review
2b42cf9f0f28818341ccb63de5af3accf72c5dc3026f4ebe6aec17898f1d2f85
  exact-square RESULT.md
2ba3ad04ca2fb181db9d146e947cfb5aa23588e1020a79577cfc72f80e388f65
  exact-square EVIDENCE.sha256

77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e
  affine-mu2 Faber connection/classification theorem
4ddc0e4837e1581129fddad70fc7b5c029d642e644f4fd8ab478a4dec59bded3
  hostile connection review
86d9da43b1f7823a4673ed219478b1c6ff60503eccbb2892894733979468b19c
  affine-mu2 RESULT.md
8e56b7ab944e956b9d67993e54bfc8996f02b16803889ac7dfbaa59e2ee0447c
  affine-mu2 EVIDENCE.sha256
```

The source-typed terminal client is

```text
82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f
  one-parameter Rees reduction promotion
1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de
  hostile one-parameter review
0fa0dc4afb160ae4b9ed6bc195e1158e44b92cdc5bb5ea1619a146e9d52aac96
  independent R-unit/delta review
5905e57578c5f9af047f70f8fce48a6ab56ce9dccfc2a33d868d8e05b3f4ea82
  compile_oneparam_rees.py
1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b
  terminal exact-differential theorem
db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251
  terminal theorem hostile review
```

## 2. What K00 exactly proves

At K00 every collision correction is zero, `k10=k` is nonzero, and

```text
p=-2*rho^2,       c=0,       r=p^2/4=rho^4,
k6=k2=0.                                             (2.1)
```

The centered monic octic coefficient tuple is

```text
C6=-4*rho^2,  C5=0,  C4=6*rho^4,  C3=0,
C2=-4*rho^6,  C1=0,  C0=rho^8.                      (2.2)
```

Equivalently, if `q=z^2-rho^2`, the quartic is `Q=q^2` and the octic is
`F=Q^2=q^4`.  Therefore

```text
F^(3/2)=q^6,             F^(5/4)=q^5                (2.3)
```

are polynomials.  The unloaded and unit-`k10` negative tails vanish
separately.  This explains the exact replay result: all 569 frozen tail
monomials cancel in every row and all 70 exported raw rows through grade 19
vanish.  The replay includes `D(k)` but does not include the terminal
right-hand side (0.1), either Taylor family, or an honest closure-first
saturation.

## 3. Rees charts: the precise statement, and a necessary correction

For `I=(f0,...,fn)` in a noetherian ring `A`, the actual standard blowup
chart is

```text
C_i=A[y_j:j!=i]/((fi*y_j-fj:j!=i):fi^infinity).     (3.1)
```

The colon is essential: the unsaturated bilinears can retain
symmetric-algebra torsion.  It can be computed by eliminating `u` from

```text
(fi*y_j-fj:j!=i) + (1-u*fi).                        (3.2)
```

For the collision routing ideals

```text
J1=(rs,cs,c0,c1),       J2=(a0,a1) on V(J1),        (3.3)
```

K00 has `J1=J2=0`.  Consequently every **restriction-first principal
section** is killed: if `M_K00` is imposed before the chart localization,
then `fi in M_K00` and

```text
((fi*y_j-fj)+M_K00):fi^infinity=(1).                (3.4)
```

However, (3.4) must not be misstated as “the geometric blowup fibre over
K00 is automatically empty.”  In general colon and base change do not
commute; for example the blowup of `(x,y)` has a nonempty `P^1` fibre over
the origin.  An honest chart-then-K00 fibre can retain transverse
exceptional directions.  Its emptiness requires the complete total source
and the Gate-T chart calculation; it does not follow merely from
`J1=J2=0`.

The DVR routing theorem says something different and exact.  For an arc
`phi:A->R` to a DVR:

```text
phi(J1)R != 0                 -> a J1 standard chart;
phi(J1)R = 0, phi(J2)R != 0  -> a J2 standard chart;
phi(J1+J2)R = 0              -> the terminal receiver V(J1+J2). (3.5)
```

Thus K00 is routed to the receiver because its pulled-back correction ideal
is identically zero.  It is not discarded.  The six chart lanes address
nonzero transverse correction ideals; their ordered unit certificates do
not substitute for the terminal-receiver pullback.

## 4. Existing receiver equations confirm, rather than exclude, K00

Normalize on `D(k10)` by

```text
beta=k6/k10,       gamma=k2/k10,       Delta=p^2-4*r.
```

The reviewed seven-tail reduced support is

```text
V(c,Delta)
 union
V(c,16*beta-5*Delta,256*gamma-5*Delta^2).           (4.1)
```

K00 has

```text
c=0,       Delta=4*rho^4-4*rho^4=0,
beta=gamma=0,                                       (4.2)
```

so it lies on the square component of (4.1).

With the literal affine Faber target `r2=mu2`, the reviewed reduced support
again has the square component

```text
c=0,       Delta=0,       mu2=0,                    (4.3)
```

with `beta,gamma` arbitrary.  K00 satisfies (4.3).  These computations
identify its receiver component; they provide no exclusion equation.

The reviewed generic-`Jdet` complete-local theorem at SHA
`fe1193abe8c45c590f7653d96998a7b053e8de0e09a751cd8fb686d2cbf72fc1`
(review SHA
`08a6bec022613a1d26ac64a5685e6408e875423b609c50fee604326fbb5a15dc`)
excludes a large open of the **non-square** `D(Delta)` graph.  Its explicit
firewall excludes `Delta=0`; it therefore does not decide K00.

## 5. The first honest target and the meaning of the localizer

For the fixed terminal source profile `[6,2]`, the reviewed differential is

```text
8*r7' = j/u.                                         (5.1)
```

After the rational Kummer normalization one has

```text
r7=(j/4)*T.
```

At the selected infinity point `T=1+tau`, the source target is
`(j/4)(1+tau)`.  The unit change

```text
Jdet=(1+tau)*j,       Lambda=tau^3*varrho            (5.2)
```

turns the complete seven-row ordinary source into

```text
Phi_l = r_l(C,Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)
        -Lambda^(12+l)*delta_l,
(delta1,...,delta7)=(0,mu2,0,mu4,0,mu6,Jdet/4).     (5.3)
```

Here `Jdet` is inverted because `j` is the nonzero constant Jacobian.  The
strict interior is `D(Lambda*Jdet)`.  In the collision weight convention
`Lambda=sigma^2`; hence

```text
D(Lambda*Jdet)=D(sigma*Jdet)                         (5.4)
```

as opens.  Neither `rho` nor a collision correction generator is included
in (5.4).  The unit-`k10` K00 ray additionally uses `D(k10)`.

By (2.3), all `r_l` vanish on the literal K00 core.  In particular

```text
Phi7|K00 = -Lambda^19*Jdet/4
          = -sigma^38*Jdet/4.                       (5.5)
```

The restriction-first unit has the explicit certificates

```text
(Lambda*Jdet)^19 = -4*Jdet^18*Phi7,
(sigma*Jdet)^38  = -4*Jdet^37*Phi7.                 (5.6)
```

Equivalently, saturation first by `sigma` turns (5.5) into `Jdet`, and
subsequent `Jdet` saturation gives `1`.  Thus the literal all-zero
correction section cannot itself be a strict source with nonzero Jacobian.

## 6. Why (5.6) does not kill the transverse saturated closure

The operation proved unit in (5.6) is schematically

```text
(I + M_K00):(Lambda*Jdet)^infinity,                 (6.1)
```

where the K00 core is imposed first.  The honest boundary incidence is

```text
(I:(Lambda*Jdet)^infinity) + (Lambda) + M_K00.      (6.2)
```

There is no general equality between (6.1) and (6.2).

The exact negative control is

```text
I=(x-Lambda*m) in Q[Lambda,m,x].                    (6.3)
```

The ideal is already saturated on `D(Lambda*m)`, and its boundary has
`Lambda=x=0` with `m` still a unit.  If `x=0` is imposed first, (6.3)
becomes `(Lambda*m)`, whose saturation on the same open is the unit ideal.
The transverse term `x=Lambda*m` disappears at the boundary but is exactly
what satisfies the interior equation.

Likewise a true source arc can have positive-order odd/even coefficient,
load, or target corrections whose combined `r7` is
`Lambda^19*Jdet/4`, while all those corrections specialize to the K00 core.
The 569-tail replay sets them identically to zero; it cannot test this
possibility.  Killing the literal section is therefore necessary but not a
closure theorem.

## 7. Smallest exact closure-first incidence

Work in the promoted one-parameter ring

```text
A=Q[Lambda,C0,...,C6,k10,k6,k2,mu2,mu4,mu6,Jdet].
```

The K00 common-quartic/load **core**, leaving the Jacobian parameter free,
is the ideal

```text
M_K00=(
  C5,C3,C1,
  8*C4-3*C6^2,
  16*C2-C6^3,
  256*C0-C6^4,
  k6,k2,mu2,mu4,mu6
).                                                   (7.1)
```

Indeed `C6=2p`, so (7.1) is exactly

```text
C4=3*p^2/2,       C2=p^3/2,       C0=p^4/16.       (7.2)
```

The generic moving K00 ray has `C6*k10 != 0`.  Keeping `Jdet` nonzero is
the honest terminal condition.  The exact computation is

```text
I     = (Phi1,...,Phi7),
KL    = I:Lambda^infinity,
K     = KL:Jdet^infinity,
B     = K + (Lambda) + M_K00,
H_K00 = B:(C6*k10*Jdet)^infinity.                   (7.3)
```

The order in (7.3) is load-bearing: saturate first, then take the boundary,
then impose the K00 core.  The last localization selects the generic
`rho!=0`, unit-`k10`, nonzero-Jacobian incidence; it is not a replacement
for either of the first two saturations.  Since `C6` is a unit there, the
coefficient irrelevant origin is already absent and no large irrelevant
ideal saturation is needed for this first slice.

An optional deck-explicit control adjoins `rho` and replaces the four even
relations in (7.1) by

```text
C6+4*rho^2,
C4-6*rho^4,
C2+4*rho^6,
C0-rho^8,                                           (7.4)
```

with `C5=C3=C1=0`.  The compiler should verify invariance under
`rho -> -rho` and contraction of (7.4) back to (7.1); it must not choose
one root orientation as extra source data.

Required controls and interpretation:

1. Restriction before saturation must reproduce the unit certificate
   (5.6).
2. Exact Q is the mathematical lane; a separately serialized good prime is
   a software/control lane.
3. `H_K00=(1)` with a saved certificate excludes only the generic K00
   incidence for this fixed source-typed `[6,2]` ordinary-tail client.
4. `H_K00!=(1)` records accessible algebraic boundary support.  It is not a
   Taylor realization, rational coefficient trajectory, or Keller pair.
5. Either outcome leaves the `C6=0` tip, `k10=0`, other load rays, other
   square-normal cones, and the full collision receiver untouched unless
   separately mapped.

## 8. What exists and what is missing

Available now:

- the exact standard-chart presentation (3.1)--(3.2);
- the rigorous iterated DVR routing (3.5);
- the complete frozen 569 ordinary tails and raw K00 cancellation;
- reviewed reduced square/Pell and affine-`mu2` receiver supports;
- the promoted, independently reviewed one-parameter seven-row source
  (5.3), including the terminal target and both interior localizers;
- the AWS-only one-parameter compiler.

Missing at this discriminator:

- no implementation of (7.1)--(7.3), no basis, and no unit/nonunit
  endpoint;
- the recorded one-parameter Q and characteristic-32003 launches reached
  `ONEPARAM_STAGE_LAMBDA_START`, but no mathematical endpoint is preserved;
  the registration's stale “not launched” line is superseded by
  `cases/max12_812_order2_u2_62_oneparam_rees_20260826/AWS_LAUNCHES.md`;
- the older two-parameter Q/prime saturations timed out after four hours
  with no verdict (timeout-manifest SHA
  `e2a596f01aea3d25d51c35cf2d0e4ae10f64c902409319a37320b954721a16cb`);
- the general-`rho` collision emitter is not complete through the target
  grades `28,32,36,38`; later receiver exports partly specialize `rho=0`;
- a literal collision-terminal-receiver to fixed `[6,2]` pullback with all
  correction jets through grade 38 is not implemented;
- neither finite Taylor family is compiled (`Taylor_x0` and `Taylor_x1`
  remain charged); and
- Gate T still lacks the complete common total-source/base-change maps and
  terminal-receiver pullback.  Ordered chart certificates do not fill this
  interface automatically.

Therefore (7.3) is the smallest honest next computation justified by the
current bytes.  It is much smaller than rerunning the full monolithic
boundary, but it is a discriminator for one generic terminal incidence,
not an emptiness proof for `V(J1+J2)` as a whole.

