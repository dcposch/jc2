# `K00-V20R2-VALUATIVE-COMPARISON/v1`

Date: 2026-08-29  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `31777ce90994a106aade85064c0d868e32863f94`  
Status: **SOURCE-COMPLETE RAMIFIED RESIDUAL / NO INCIDENCE ENDPOINT**

## 0. Endpoint

The pinned source does not contain a theorem reducing every closure-first DVR
arc to `ord_t(Lambda)=1`.  Such a reduction is not formal: the exact control
`x^2-Lambda` has a ramified arc and no `K[[Lambda]]` section.  The K00 source
is singular to first transverse order, so no reviewed etale/smooth projection
theorem supplies the missing reduction.

This packet therefore returns

```text
RAMIFIED_RESIDUAL_EMITTED
```

and registers the first cell not represented by V20R2:

```text
K00-V20R2-RAM-E2-M1-B11111/v1

e = ord_t(Lambda) = 2,
m = min_i ord_t(d_i) = 1,
ord_t(k10)=0,
ord_t(k6)=ord_t(k2)=ord_t(mu2)=ord_t(mu4)=ord_t(mu6)=1,
ord_t(Jdet)=0.
```

Here `B11111` records the five exact boundary-series orders in the displayed
order.  “First” means lexicographically smallest ramification `e>1`, then
smallest positive transverse order, then smallest finite order of every
K00-boundary load/target series.  The cell is a constructible source cell,
not a point and not an assertion that it is nonempty.

## 1. Exact source and closure order

Work in

```text
A=Q[Lambda,C0,...,C6,k10,k6,k2,mu2,mu4,mu6,Jdet]
```

with the seven frozen rows

```text
Phi_l = r_l(C,Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)
        - Lambda^(12+l)*delta_l,
delta=(0,mu2,0,mu4,0,mu6,Jdet/4).
```

The `r_l` are the exact 569 frozen ordinary-tail monomials.  The K00 core is

```text
M_K00=(C5,C3,C1,
       8*C4-3*C6^2,16*C2-C6^3,256*C0-C6^4,
       k6,k2,mu2,mu4,mu6).
```

The only incidence compared here is

```text
I  = (Phi1,...,Phi7),
KL = I:Lambda^infinity,
K  = KL:Jdet^infinity,
B  = K+(Lambda)+M_K00,
H  = B:(C6*k10*Jdet)^infinity.                    (1.1)
```

No K00 equation is imposed before the first two saturations.  The final
localizer selects only the generic K00 ray.  The equivalent eventual-open
optimization does not alter this semantic order.

## 2. Exact DVR comparison

Let a geometric point of `V(H)` lie in `D(C6*k10*Jdet)`.  By algebraic curve
selection followed by normalization, closure from the source open gives,
after a finite residue extension, a complete DVR `R=K[[t]]` and a map
`A -> R` such that

```text
Lambda(0)=0,                     Lambda(t) != 0,
C6(0),k10(0),Jdet(0) != 0,
d(0)=0,
k6(0)=k2(0)=mu2(0)=mu4(0)=mu6(0)=0.
```

Write `Lambda=u(t)t^e`, `u(0)!=0`.  After adjoining an `e`th root of the
unit and changing uniformizer, one may and will put

```text
Lambda=t^e.                                           (2.1)
```

This removes only a unit; it does not change `e`.

The full source is invariant under the weight action

```text
C_i    -> a^(8-i) C_i,       k10 -> a^2  k10,
k6     -> a^6 k6,            k2  -> a^10 k2,
mu2    -> a^14 mu2,          mu4 -> a^16 mu4,
mu6    -> a^18 mu6,          Jdet-> a^19 Jdet,
Lambda -> Lambda.
```

Every row scales by `a^(12+l)`.  Since `C6(t)` is a unit, a finite faithfully
flat weight-two Kummer extension supplies `a(t)^2*C6(t)=1`.  Thus `C6=1`
is valid on this generic ray; all displayed orders and unit opens are
unchanged because `a(t)` is a unit.  Define the exact normalized coordinates

```text
C0=(1+d0)/256, C1=d1, C2=(1+d2)/16,
C3=d3, C4=(3+d4)/8, C5=d5, C6=1.                  (2.2)
```

Equations (2.1)--(2.2) are the complete licensed normalization.  They do not
turn `t` into `Lambda` when `e>1`.

## 3. Why `e=1` does not follow

The source rows have no constant or linear unloaded term at K00.  Their exact
normal-order stencil is

```text
ord_d R_l >= (2,2,2,2,2,3,2),
ord_d A10_l >= (2,2,2,2,2,2,2),
ord_d A6_l  >= (1,1,1,2,1,2,1),
ord_d A2_l  >= (1,1,1,1,1,1,1),                  (3.1)
```

where

```text
Phi=R(d)+Lambda^2*k10*A10(d)+Lambda^6*k6*A6(d)
       +Lambda^10*k2*A2(d)-targets.
```

Consequently the differential in the coefficient-normal directions vanishes
at the K00 point.  None of the pinned artifacts proves that the projection to
the `Lambda` line is smooth, etale, or admits an unramified curve through
every boundary point.

The source-independent negative control is

```text
X=Spec K[Lambda,x]/(x^2-Lambda).
```

The origin is in the closure of `X intersect D(Lambda)` and is reached by
`Lambda=t^2,x=t`.  A section `x in K[[Lambda]]` would have
`2 ord_Lambda(x)=1`, impossible.  Thus an implication

```text
closure incidence => K[[Lambda]] section
```

requires a source-specific theorem.  V20R2 supplies no such theorem.  This
control does not prove that the K00 source has a ramified arc; it proves that
the proposed `e=1` reduction is not licensed by general formal logic.

## 4. First ramified cell: literal source

Put `e=2` and work in `T38=K[t]/(t^39)`.  The exact seven rows are

```text
Psi_l(t)=r_l(C(t),t^4*k10(t),t^12*k6(t),t^20*k2(t))
          -t^(2*(12+l))*delta_l(t),                 (4.1)
```

with all `273=7*39` coefficient equations

```text
[t^g]Psi_l=0,       1<=l<=7, 0<=g<=38.             (4.2)
```

The complete labelled source through this cutoff is

```text
d_i   = sum_(n=1)^38 d_i[n] t^n,                    i=0,...,5,
k10   = sum_(j=0)^34 k10[j] t^j,
k6    = sum_(j=0)^26 k6[j] t^j,        k6[0]=0,
k2    = sum_(j=0)^18 k2[j] t^j,        k2[0]=0,
mu2   = sum_(j=0)^10 mu2[j] t^j,       mu2[0]=0,
mu4   = sum_(j=0)^6  mu4[j] t^j,       mu4[0]=0,
mu6   = sum_(j=0)^2  mu6[j] t^j,       mu6[0]=0,
Jdet  = Jdet[0].
```

There are

```text
6*38+35+27+19+11+7+3+1 = 331
```

labelled columns and `326` free columns after the five boundary-zero columns
are removed.  Exactness of this cell adds the constructible opens

```text
D(d0[1]) union ... union D(d5[1]),
D(k10[0]*k6[1]*k2[1]*mu2[1]*mu4[1]*mu6[1]*Jdet[0]). (4.3)
```

No coefficient is set to zero merely because it is late or absent from an
optimized solve.

Using the exact stencil (3.1), only the following `316` free columns can
occur in (4.2):

```text
d_i[1..37]                                           222
k10[0..32]                                            33
k6[1..25]                                             25
k2[1..17]                                             17
mu2[1..10], mu4[1..6], mu6[1..2], Jdet[0]             19
                                                       ---
                                                       316.
```

The ten other free labelled columns are retained in the source census and
certified inert through grade 38: `d_i[38]` (six), `k10[33..34]`, `k6[26]`,
and `k2[18]`.

## 5. Literal grade calendar

The first possible grades, derived from (3.1) and the exact orders in the
cell, are

| sector | rows | first `t` grade |
|---|---|---:|
| unloaded `R` | `1,2,3,4,5,7` | 2 |
| unloaded `R` | `6` | 3 |
| `t^4 k10 A10` | all seven | 6 |
| `t^12 k6 A6` | `1,2,3,5,7` | 14 |
| `t^12 k6 A6` | `4,6` | 15 |
| `t^20 k2 A2` | all seven | 22 |
| `t^28 mu2` | row 2 | 29 |
| `t^32 mu4` | row 4 | 33 |
| `t^36 mu6` | row 6 | 37 |
| `t^38 Jdet/4` | row 7 | 38 |

Equivalently, the sequential source ledger is

```text
G00--G01: identically zero;
G02:      unloaded rows 1,2,3,4,5,7 begin;
G03--G05: every unloaded row is active;
G06--G13: unloaded + K10;
G14:      K6 begins in rows 1,2,3,5,7;
G15--G21: K6 is active in every row;
G22--G28: K2 is also active;
G29--G32: row-2 mu2 target active;
G33--G36: row-4 mu4 target also active;
G37:      row-6 mu6 target also active;
G38:      row-7 Jdet target active.
```

“Active” means the sector can occur; cancellations on a leading-rank stratum
remain possible and must be decided from the literal equations.  The calendar
does not import any valuation-two/four/five periodicity.

## 6. Restriction/saturation negative control

In `K[Lambda,m,x]`, let

```text
I0=(x-Lambda*m),       open=D(Lambda*m).
```

Since `K[Lambda,m,x]/I0` is a domain and `Lambda*m` is nonzero there,

```text
I0:(Lambda*m)^infinity=I0.
```

After taking the boundary and the transverse core one obtains the proper
incidence `(Lambda,x)` with `m` still a unit.  Restriction first instead gives

```text
(I0+(x)):(Lambda*m)^infinity
=(x,Lambda*m):(Lambda*m)^infinity=(1).
```

Every producer must replay both outcomes.  It is invalid to replace (1.1) by
restriction-first rows.

## 7. Minimal producer/AWS contract

No elimination was run for this report.  A producer for the emitted cell must:

1. pin and independently parse all 569 tail monomials, verify their weights
   and affine load-linearity, and rederive (3.1);
2. emit the 331-column table, the five boundary equations, the opens (4.3),
   and all 273 equations in grade-major order as exact rational DAGs;
3. compare every DAG root with direct tail-series evaluation on two exact
   fixtures and one separately serialized good-prime fixture;
4. certify the ten inert columns by syntactic occurrence, not sampling;
5. replay the two controls in Sections 3 and 6;
6. require mutations `t^4->t^2` in K10, `t^12->t^6` in K6,
   `t^38 Jdet->t^37 Jdet`, deletion of all odd `t` columns, and one Kummer
   weight error to change the serialization or fail a fixture; and
7. stop after source emission unless a separate sequential rank/Fitting
   solver is preregistered.  Any uncertain elimination belongs on campaign
   AWS with exact-Q as the mathematical lane; a prime is navigation only.

Allowed source-packet endpoints are

```text
PASS_RAMIFIED_SOURCE_EMISSION
NOT_TYPED_OR_SOURCE_DRIFT
RESOURCE_CAP_NO_VERDICT.
```

A later solve must cover every constructible rank cell created by (4.2).
One random point, one modular survivor, or one compatible prefix is no
incidence verdict.

## 8. Scope firewall

This packet proves only that `e=1` is not presently reducible from the pinned
source and gives the complete first missing ramified finite source functor.
It does not prove that `H` is proper, that the emitted cell has a point, that
any finite jet lifts, or that any formal arc is algebraic, Taylor-realizable,
rational, polynomial, source-reachable from the collision receiver, or
attained by a Keller map.  It does not cover other `(e,m,load-order)` cells,
the `C6=0` tip, `k10=0`, other load rays or square normals, Gate T, order two,
maximum twelve, or JC2.  Formal data are not a map, and a residual cell is not
attainment.

## Pinned bytes

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848  frozen tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b  V20R2 compiler
9e304f58310fda008a3930b21bf0f49bc198322ee5dd98d805af04068ed5b3c8  V20R2 result
4cdbd2ca462378adbcd0fba103f79a2ad9e5fbd6c6a7d81682ebc45230c2b1c4  V20 preregistration
c2996ec867f481d62663517022dd86a7ebea9065d70f6d8d825d505a250140d8  closure-first preregistration
abcb00ab31807437601073454488a8b787e3c11aaaffb2083e2e16769a7648e5  source history/type audit
5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b  one-parameter Rees reduction
e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7  strict-Rees source client
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11063`.
- Body SHA-256: `c15bda710b725c04c6ccf289fcf570c3414fe8825669ae68238c1d26fe96d51c`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
