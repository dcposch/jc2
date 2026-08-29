# Provisional addendum: the nonzero cutoff-five branch is unit at `D18`

Date: 2026-08-28  
Producer: Sol Ultra, independent characteristic-mode lane  
Status: `PROVISIONAL EXACT-Q(t) UNIT; LITERAL-SOURCE COFACTOR FREEZE REQUIRED`

## Result

Assume the licensed cutoff-five field-radical cascade through `D14`, the
live exact `D15` consequence

```text
T=C*Q,   hence F7=R/2+H*Q,
C=X^4-1, H=C^2,
```

and the exact `D13`--`D15` scalar core from the frozen producer packet.  The
first new eliminated compatibility from `D16,D17` is

```text
K17 = v*(b*v+r^2)=0,
```

where `v=V0`, `r=R0`, and `b=F7[X^0]`.

The branch `v=0` is already incompatible with the endpoint by the explicit
unit identity in
`xmodel/ggv-upper-endpoint-tail5-characteristic-core-unit-r0-sol-ultra-20260828.md`.
On the complementary field branch `v!=0`, put `t=r/v`.  The scalar core
reduces exactly to

```text
12*t^2+6*t+1=0,
v = -3*t^4*(1+4*t),
b = -t^2*v,
r = t*v,
e = -(3/8)*t^2*v*(1-4*t).
```

The case `t=0` would force `v=0`, so it is absent on this branch.  Modulo the
quadratic, the substitutions have the compact linear form

```text
v =  t/24,
r = -t/48  - 1/288,
b = -t/144 - 1/576,
e = -t/192 - 7/4608,
c = (2*t+1)/36864.
```

Keep both endpoint partners `a=p32` and `d=p91`, and every non-core partner,
symbolic.  Exact rational row reduction gives the following cumulative ranks
over

```text
K = Q[t]/(12*t^2+6*t+1):
```

```text
through D16: rank 20, no nonzero scalar in the span;
through D17: rank 38, no nonzero scalar in the span;
through D18: rank 58, literal 1 in the span.
```

Thus the nonzero quadratic branch is empty already at `D18`; `D19` is not
needed.  Together with the `v=0` endpoint certificate, this would retire all
characteristic-zero field-valued points of the fixed cutoff-five endpoint
specialization once the live row provenance is frozen and independently
reviewed.

## Exact coefficient-field calculation

No root of the quadratic was chosen.  Every reduced coefficient is uniquely
written `A+B*t`, using

```text
t^2 = -t/2-1/12.
```

For each compatibility polynomial `f`, the calculation forms the rational
pair

```text
f,  reduce(t*f).
```

The `K`-linear span of the original compatibilities is exactly the
`Q`-linear span of those pairs.  Therefore finding the literal rational
polynomial `1` in this doubled span is a genuine identity

```text
1 = sum_i (A_i+B_i*t)*f_i  in K[remaining variables].
```

It does **not** treat the coefficients of `1` and `t` as two independent
polynomial equations, and it does not infer that `t=0`.  The polynomial
`12*t^2+6*t+1` is irreducible over `Q`, so `K` is a field; the calculation
simultaneously covers its two conjugate embeddings.

One exact sparse cofactor found in the displayed compatibility ordering is

```text
  1119744             * D16[4]
+  944784*t           * D16[12]
- (85847040/7)        * D17[1]
- (258450912/7)*t     * D17[1]
-  2985984            * D17[5]
-  2519424*t          * D17[5]
+  5038848*t          * D17[9]
+ (103514112/7)       * D18[2]
+ (465813504/7)*t     * D18[2]
+  7962624            * D18[6]
+ 35831808*t           * D18[6]
+ (23887872/7)        * D18[10]
+ (107495424/7)*t     * D18[10]
= 1.
```

Indices are zero-based within each nonzero displayed compatibility list.
This identity was expanded exactly with rational arithmetic after all
progressive substitutions.  It is provisional because those `D16`--`D18`
lists and their maps to literal source rows have not yet been serialized in
an immutable case packet.

## Weight-eight gauge and the licensed slice

The raw coordinate `p129=F8[X^0]` is absent from every determinant row.  The
reason is the exact additive symmetry

```text
F -> F+mu*t^8:
(mu*t^8)_X=0,  (t*d/dt-8)(mu*t^8)=0.
```

Consequently every orbit meets `p129=0`, and fixing that slice changes no
determinant equation or endpoint carrier.  This is a global additive-gauge
slice, not a normalization of `a,b,c`, or `d`.  Repeating the `D16,D17`
checks on this slice does not restore the naive square-root cascade: neither
`N mod C`, `N^2 mod C`, nor `N^2 mod H` lies in the compatibility span, and
`v^2` is not obtained.  The genuine next relation is `K17` above.

## Mutation

Deleting the complete `D18` compatibility block gives the exact preceding
`K`-rank 38 system.  Its intersection with `K` is zero: neither `1` nor any
other nonzero scalar lies in the linear span.  Restoring `D18` raises the
rank to 58 and produces the displayed unit.  The regression therefore
detects omission of the decisive row and guards against accidentally
reusing the `D17` branch relation as a unit.

## Inputs and required promotion packet

The calculation used the authoritative raw system

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
```

and these frozen cutoff-five inputs:

```text
a3382efcd72104d48abb40981a33b87d9dacb5e7a9018a12937bef1f794f942c
  cases/ggv_8_28_upper_endpoint_tail5_desk_20260828/TAIL5/TAIL_DEFORMATION_SYSTEM.json
f1da5750faf3793fc58e4ec80d91b4dc212fd42fb39f7d0662e98fc25edf5902
  cases/ggv_8_28_upper_endpoint_tail5_desk_20260828/TAIL5_DESK_ANALYSIS.json
8a028ff624cbdc6c72ed4e771b64868db699c187cefc441cdab7dde71e0f4342
  xmodel/ggv-upper-endpoint-tail5-characteristic-core-unit-r0-sol-ultra-20260828.md
```

Before promotion, the independent compiler lane must freeze and replay:

1. the `D15` witnesses for all four coefficients of `T^2 mod C`, followed by
   the exact parameterization `T=CQ`;
2. the progressively substituted `D16`, `D17`, and `D18` compatibility
   lists, with every item tracked to literal raw source rows;
3. the cofactor above, first in those displayed lists and then composed all
   the way back to the literal source rows;
4. the `K17` extraction, the two-branch cover, and the five linear quadratic-
   branch substitutions;
5. a live coefficient mutation in a used `D18` source row, in addition to
   the row-deletion regression above;
6. endpoint-carrier sign checks and the fact that no carrier was normalized.

## Scope firewall

This is a provisional exact calculation for characteristic-zero field
points in the fixed branch-P square-baseline cutoff-five specialization.
The upstream `D10`--`D15` parameterizations use field-radical squarefreeness,
so even a confirmed source-row cofactor will not be an upstream nonreduced-
scheme unit.  It does not cover the full branch-P family, another GGV branch,
a Keller pair, a counterexample, or JC2.  `D23` is not imposed and `G22` is
absent.  No local CAS, Groebner basis, modular inference, AWS job, or root
choice was used.
