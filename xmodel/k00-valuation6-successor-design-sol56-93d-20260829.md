# K00 transverse valuation six: exact successor design and hand obstruction

Author: Sol 5.6 subresearch lane  
Date: 2026-08-29 UTC  
Frozen campaign basis: `93db679d3160c957b0610297afccc1f2fad53125`  
Lifecycle: `PROVISIONAL_EXACT_DESK_THEOREM / INDEPENDENT REPLAY REQUIRED`

## 0. Executive result

The proposed valuation-six nonlinear solve is unnecessary.  In the exact
V20R2 normalized K00 source, every jet with

```text
C6=1,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
k10[0] != 0,
Jdet[0] != 0,
Lambda^6 | d_i for i=0,...,5
```

is already impossible through `Lambda^19`.

The only nontarget term that can survive in the scalar-contracted equation at
grade 19 is

```text
k6[1] * D6^[2](x),       x=(d0[6],...,d5[6]),
```

where `D6^[2]` is the quadratic part of the contracted `K6` target.  Exact
coefficient comparison gives

```text
D6^[2] = -4*Q1 - 32*Q3,
```

with `Q1,Q3` the literal grade-12 row-1 and row-3 quadratic forms.  Those two
forms vanish already in the grade-12 raw system.  The grade-19 contraction is
therefore `-5*Jdet[0]=0`, contradicting the source unit open.

This closes the entire closed divisibility condition `Lambda^6 | d`, not only
the constructible exact-valuation-six locus.  Consequently it also subsumes
the provisional valuation-at-least-seven conclusion.  It says nothing about
valuations two through five, a differently normalized source, a compatible
infinite arc outside this finite client, a polynomial map, a counterexample,
or JC2.

## 1. Frozen source and boundary ledger

Write the seven V20R2 rows as the row-vector identity

```text
Phi = R(d)
    + Lambda^2  k10 A10(d)
    + Lambda^6  k6  A6(d)
    + Lambda^10 k2  A2(d)
    - Lambda^14 mu2 e2
    - Lambda^16 mu4 e4
    - Lambda^18 mu6 e6
    - Lambda^19 (Jdet/4) e7,
```

where `e_i` is the `i`th standard row vector.  At the normalized K00 point,
the exact homogeneous-order ledger is

```text
ord_d R >= 2,        ord_d A10 >= 2,
ord_d A6 >= 1,       ord_d A2  >= 1.
```

The literal source columns and boundary conditions are

```text
d_i    = sum_(q=1)^19 d_i[q] Lambda^q,       i=0,...,5,
k10    = sum_(j=0)^17 a_j Lambda^j,          a_0 != 0,
k6     = sum_(j=0)^13 b_j Lambda^j,          b_0 = 0,
k2     = sum_(j=0)^9  c_j Lambda^j,          c_0 = 0,
mu2    = sum_(j=0)^5  m_j Lambda^j,          m_0 = 0,
mu4    = sum_(j=0)^3  n_j Lambda^j,          n_0 = 0,
mu6    = sum_(j=0)^1  o_j Lambda^j,          o_0 = 0,
Jdet   = J,                                      J != 0.
```

For valuation at least six substitute `d_i[1]=...=d_i[5]=0` before any
solve or saturation.  Put

```text
v_j=(d_0[6+j],...,d_5[6+j]) in Q^6,   j=0,...,7,
x=v_0.
```

Only the following 74 source coefficients can occur in grades 12 through
19:

```text
v_0,...,v_7                         48
a_0,...,a_5                          6
b_1,...,b_7                          7
c_1,c_2,c_3                          3
m_1,...,m_5                          5
n_1,n_2,n_3                          3
o_1, J                               2
                                    --
                                    74.
```

Every later serialized V20R2 column is genuinely out of this valuation-six
window; it must remain named in source custody, but it must not be inserted
as a solve column.

Exact valuation six adds `x != 0`.  The source-faithful constructible cover is

```text
D(x_0) union ... union D(x_5),
```

implemented either as the six Rabinowitsch charts
`z_j*x_j-1=0` or as saturation by the irrelevant leading ideal
`(x_0,...,x_5)`.  A leading-direction `Proj` prepass is permissible, but a
naive substitution `x_j=1` is not: it silently quotients scale unless the
simultaneous Lambda-reparametrization action on every higher source
coefficient is also serialized.  The obstruction below is stronger and
holds even at `x=0`, so neither a projective chart nor an irrelevant-ideal
saturation is needed for its proof.

## 2. Exact grade-12 through grade-19 system

Let the symmetric polarizations be normalized by

```text
R^[2](z)=B(z,z),             R^[3](z)=C(z,z,z),
A10^[2](z)=E(z,z),
A6^[1](z)=L(z),              A6^[2](z)=M(z,z),
A2^[1](z)=N(z).
```

Each symbol is a seven-row vector-valued map extracted from the literal
V20R2 tails at `C6=1`.  No higher homogeneous part can enter before grade 20.
With the boundary zeros already substituted, the complete eight vector
equations are as follows.

```text
G12 = B(v0,v0).

G13 = 2 B(v0,v1)
    + b1 L(v0).

G14 = 2 B(v0,v2) + B(v1,v1)
    + a0 E(v0,v0)
    + b1 L(v1) + b2 L(v0).

G15 = 2 B(v0,v3) + 2 B(v1,v2)
    + 2 a0 E(v0,v1) + a1 E(v0,v0)
    + b1 L(v2) + b2 L(v1) + b3 L(v0)
    - m1 e2.

G16 = 2 B(v0,v4) + 2 B(v1,v3) + B(v2,v2)
    + a0 (2 E(v0,v2) + E(v1,v1))
    + 2 a1 E(v0,v1) + a2 E(v0,v0)
    + b1 L(v3) + b2 L(v2) + b3 L(v1) + b4 L(v0)
    - m2 e2.

G17 = 2 B(v0,v5) + 2 B(v1,v4) + 2 B(v2,v3)
    + a0 (2 E(v0,v3) + 2 E(v1,v2))
    + a1 (2 E(v0,v2) + E(v1,v1))
    + 2 a2 E(v0,v1) + a3 E(v0,v0)
    + b1 L(v4) + b2 L(v3) + b3 L(v2) + b4 L(v1)
    + b5 L(v0)
    + c1 N(v0)
    - m3 e2 - n1 e4.

G18 = 2 B(v0,v6) + 2 B(v1,v5) + 2 B(v2,v4) + B(v3,v3)
    + C(v0,v0,v0)
    + a0 (2 E(v0,v4) + 2 E(v1,v3) + E(v2,v2))
    + a1 (2 E(v0,v3) + 2 E(v1,v2))
    + a2 (2 E(v0,v2) + E(v1,v1))
    + 2 a3 E(v0,v1) + a4 E(v0,v0)
    + b1 L(v5) + b2 L(v4) + b3 L(v3) + b4 L(v2)
    + b5 L(v1) + b6 L(v0)
    + c1 N(v1) + c2 N(v0)
    - m4 e2 - n2 e4.

G19 = 2 B(v0,v7) + 2 B(v1,v6) + 2 B(v2,v5) + 2 B(v3,v4)
    + 3 C(v0,v0,v1)
    + a0 (2 E(v0,v5) + 2 E(v1,v4) + 2 E(v2,v3))
    + a1 (2 E(v0,v4) + 2 E(v1,v3) + E(v2,v2))
    + a2 (2 E(v0,v3) + 2 E(v1,v2))
    + a3 (2 E(v0,v2) + E(v1,v1))
    + 2 a4 E(v0,v1) + a5 E(v0,v0)
    + b1 L(v6) + b2 L(v5) + b3 L(v4) + b4 L(v3)
    + b5 L(v2) + b6 L(v1) + b7 L(v0)
    + b1 M(v0,v0)
    + c1 N(v2) + c2 N(v1) + c3 N(v0)
    - m5 e2 - n3 e4 - o1 e6 - (J/4) e7.
```

The literal system is `G12=...=G19=0`, seven scalar rows at each grade.
Grades zero through eleven vanish identically after the valuation and
boundary substitutions.  This table is a source window, not an assertion
that sequential affine solving is globally valid: rank changes still require
constructible prefix strata if one ever computes beyond the hand
obstruction.

## 3. The grade-19 hand obstruction

The exact V20R2 contraction is

```text
Rmix = Lambda^2  k10 D10
     + Lambda^6  k6  D6
     + Lambda^10 k2  D2
     + Lambda^14 mu2 u2
     + Lambda^16 mu4 u4
     + Lambda^18 mu6 u6
     - Lambda^19 Jdet h/4,

h=20+63*d4.
```

The serialized minimum transverse degrees are

```text
(D10,D6,D2,u2,u4,u6,h)=(3,2,2,1,1,1,0).
```

For `Lambda^6 | d`, all contributions except the first possible `D6` term
and the constant part of the Jacobian target lie above grade 19.  Therefore

```text
[Lambda^19] Rmix = b1 D6^[2](x) - 5 J.             (3.1)
```

Direct extraction of the `gen(2)` quadratic part of `K_VECTOR.txt` gives

```text
D6^[2] =
  -3/32   d0*d1 + 3/8    d1*d2 + 3/128  d0*d3
  -3/32   d2*d3 - 3/16   d1*d4 + 3/64   d3*d4
  -3/512  d0*d5 + 3/128  d2*d5 - 3/256  d4*d5.
```

At `C6=1`, the independently reviewed literal quadratic rows are

```text
Q1 =
   3/64   d1*d2 + 3/1024 d0*d3 - 3/64   d1*d4
  -3/128  d2*d3 - 3/2048 d0*d5 + 9/512  d3*d4
  +9/1024 d2*d5 - 3/512  d4*d5,

Q3 =
   3/1024 d0*d1 - 9/512  d1*d2 - 9/8192 d0*d3
  +3/256  d1*d4 + 3/512  d2*d3 + 3/8192 d0*d5
  -15/4096 d3*d4 - 15/8192 d2*d5 + 9/8192 d4*d5.
```

Coefficient by coefficient,

```text
D6^[2] = -4 Q1 - 32 Q3.                            (3.2)
```

The row-1 and row-3 components of `G12=0` are precisely
`Q1(x)=Q3(x)=0`.  Equations (3.1)--(3.2) reduce the grade-19 contracted row
to

```text
-5 J = 0.
```

Characteristic zero gives `J=0`, contradicting `Jdet[0] != 0`.  Notice that
neither `x != 0` nor `a0 != 0` was used; retaining both is nevertheless
mandatory in the exact source declaration.  There is no hidden cancellation:

```text
Lambda^2 k10 D10       starts at grade 20,
Lambda^6 k6 D6         contributes at 19 only as b1 D6^[2](x),
Lambda^10 k2 D2        starts at grade 23,
Lambda^14 mu2 u2       starts at grade 21,
Lambda^16 mu4 u4       starts at grade 23,
Lambda^18 mu6 u6       starts at grade 25,
Lambda^19 J(h-20)/4    starts at grade 25.
```

Thus the obstruction is a consequence of two raw grade-12 equations and one
exact contracted grade-19 equation.  Grades 13 through 18 need not be solved.

## 4. Smallest promotion packet and mutation controls

No nonlinear CAS or AWS stratum solve is mathematically justified for
valuation six.  The smallest reviewable packet is a deterministic exact
rational extractor, `K00-R6-CONTRACTION/v1`, which should:

1. pin and parse the frozen 569-tail source, the V20R2 coordinate map,
   `K_VECTOR.txt`, and the literal source-column map;
2. independently reconstruct `Q1,Q3` from the row-labelled tails rather
   than copy the formulas above;
3. extract the degree-two `D6` component and verify (3.2) coefficientwise;
4. derive the active-column census and every term-order bound in (3.1) from
   the serialized source, not a handwritten table;
5. compare the contracted grade-19 root against the V20R2 arithmetic DAG on
   deterministic exact-Q fixtures; and
6. emit the ideal identity
   `b1*D6^[2](x)-5*J = b1*(-4*Q1(x)-32*Q3(x))-5*J` together with the
   Rabinowitsch unit certificate obtained after adjoining `zJ*J-1`.

Mandatory fail-closed mutations are:

```text
one D6^[2] coefficient changed;
the coefficient -32 of Q3 changed;
k6[0]=0 not substituted before extraction;
one d_i coefficient below grade 6 restored;
h(0)=20 changed or the Jdet/4 sign changed;
Jdet aliased with collision ideals J1 or J2;
one literal row label permuted;
one of the five boundary-zero columns treated as free.
```

All must change or fail the claimed identity/source ledger.  This is a
desk-scale parser-and-linear-identity replay, not CAS.  If operational policy
nevertheless requires remote isolation, one core with a two-minute cap is
ample; no large-memory AWS allocation is warranted.

## 5. Custody and scope

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output/K_VECTOR.txt
d88ed015576f32f3c3211c89a3b33a03736ed395a03c5cfb7ad207eaf0cdf921
  cases/max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21_20260827/aws_q_box01_r1_pass/input/target_K6.txt
5e2f100de529cb3980fd9db08e74adae89cfcc60f5377d7c60bc67f6ed798835
  cases/max12_812_order2_u2_62_k00_quadratic_normal_v6_20260827/replay_k00_quadratic_normal_v6.py
49ee91fd8710b5c282d3d2c50c8ee6ad516dbf99bed4796aad5bab0f5f115096
  xmodel/max12-812-order2-u2-62-k00-quadratic-normal-v6-hostile-review-grok-20260827.md
```

No CAS, AWS resource, web source, git operation, canonical campaign file, or
`jc2-lean` object was used or touched in this derivation.

This is a finite normalized-source obstruction.  It does not itself prove
that the complete K00 closure incidence is empty, exclude valuations two
through five, algebraize a finite jet, produce or exclude a polynomial
Keller map, settle the maximum-twelve reduction, or prove JC2.

<!-- BODY-END::K00-R6-SUCCESSOR-SOL56-93D-20260829 -->

## Seal

- Body definition: every byte through the unique body-end marker above,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11532`.
- Body SHA-256:
  `52ca8725c5ca7e8322a2ac8aaca81c69bce75a933ce0aa9151764638f8f23408`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
