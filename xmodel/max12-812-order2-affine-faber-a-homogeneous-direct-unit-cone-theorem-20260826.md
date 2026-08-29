# Affine-Faber `A`: homogeneous predecessor/direct-unit cone

Date: 2026-08-26

Status: **PROVISIONAL THEOREM AND SOURCE COROLLARY.  EXACT SUPPORT IS
DUAL-AWS FROZEN; DISTINCT HOSTILE REVIEW REQUIRED BEFORE PROMOTION.**

## 1. Internal affine theorem

Work over a complete characteristic-zero valued field, after finite
ramification, in the repeated-`A` affine coefficient chart on `D(E*M)`:

```text
Q=A^2*(A^2+4*a*A+E)+U*A+R0,
N=M*A*(A^2+4*a*A+E)+V*A+M*U/2+W0.
```

Let the extracted normal scale have positive valuation `h`.  Assume

```text
v(a) >= h/3,
q=min(v(U),v(V))>0,                               (1.1)
```

and impose the reviewed complementary-pivot dichotomy: an earlier linear
polar unit kills the arc, or the genuine complement variables have
valuation at least `2q`.

Suppose every effective lower-load coefficient and every target that can
enter rows 1, 3, 4, or 6 has valuation at least

```text
14*h/5.                                           (1.2)
```

Then the seven ordinary-Faber rows have no formal or Puiseux solution on
this weighted formal neighbourhood.

## 2. The low-kernel half of the cone

If

```text
0<q<2*h/5,                                        (2.1)
```

the first quadratic face has valuation

```text
2*h+2*q < 14*h/5 < 3*h.                           (2.2)
```

It therefore precedes every load/target in (1.2) and the intrinsic cubic.
After removing a common unit normal factor, the complete initial rows are

```text
G1=-3*r1*M^2/8+3*s0*M/4,
G3=-3*E*r1*M^2/32-3*M*x*y/8+3*E*s0*M/16,
G4= 3*M^2*x^2/32-3*E*M^2*r0/16-3*E*y^2/16,
G6=-3*E^2*M^2*r0/64+3*E^2*y^2/64.                (2.3)
```

These are the reviewed forms with the closed-point unit `p` renamed `E`.
The exact combinations

```text
G3-(E/4)*G1=-(3/8)*M*x*y,
G6=0 => r0*M^2=y^2                                (2.4)
```

kill both projective residue charts: on `D(x)`, `G4=3*M^2*x^2/32`; on
`D(y)`, `G4=-3*E*y^2/8`.  Unequal kernel orders land on one of the same
axes.  Moving center and tangent coefficients only raise the first face or
multiply already-zero predecessor rows.

## 3. The high-kernel half is a rescaled exact support certificate

The full exact polynomial `K=E*H3+H5` has frozen custody

```text
e0a64e55ea21c41ee06e635740f7b8af375ce64855638cc44109afb8b384492a
  cases/max12_812_order2_affine_faber_a_full_k_multisupport_20260826/RESULT.md
c16d31a8089dca365014a710e40d33a6e5a0b4924053439ead03f584a4e45e7b
  cases/max12_812_order2_affine_faber_a_full_k_relative_cone_v2_20260826/RESULT.md
f7606a759e5cf6f9a52432baef1af2fb170ce04b65cbd573a96a0f17bbdc0619
  cases/max12_812_order2_affine_faber_a_full_k_relative_cone_v2_20260826/EVIDENCE.sha256
743742bac469af09ccb3b46b6366657fa62c4161e6b61a11361f63cbc5f2d0c8
  cases/max12_812_order2_affine_faber_a_full_k_relative_cone_v2_20260826/FREEZE.sha256
```

It contains 371 exact-Q coefficient groups, with an identical exponent
sequence in the good-prime software control.  At the integer weight vector

```text
a:5, normal:15, U:V:6, complements:12,
loads/mu2/mu4:42,                                 (3.1)
```

the unique minimum is

```text
-E*M^3*normal^3/16                                (3.2)
```

of weight 45; the next raw-support weight is 47.  (`mu6` and `J` cancel
identically from `K`.)  The exact formal identity and its different-model
review independently prove the same coefficient before support grouping.
The frozen target derivatives are

```text
dK/dmu4=4*a,       dK/dmu2=-a*E+20*a^3,           (3.3)
```

so assigning `mu4` the lower bound 42 in (3.1), rather than its fixed-ray
source value 48, introduces its first term only at weight 47 and does not
alter the unique minimum.

For `q>=2*h/5`, multiply every weight in (3.1) by `h/15`.  Conditions
(1.1)--(1.2) and the complement bound place every actual variable at or
above the corresponding rescaled weight.  Since all 371 support weights
are linear in the valuations, (3.2) remains the unique minimum at weight
`3h`; increasing any input valuation cannot create a new tie.  Thus `K`
has a unit leading coefficient and the seven rows cannot all vanish.

Sections 2 and 3 meet at `q=2*h/5` and exhaust every `q>0`.  This proves
the internal theorem.

## 4. Arcwise delayed-source corollary

On the fixed delayed source ray

```text
Lambda=sigma^3,
k10=Lambda^12*K10,  k6=Lambda^8*K6,  k2=Lambda^4*K2,
```

the three effective loads and `mu2` start at sigma valuation 42; the later
targets start at 48, 54, and 57.  Let the exact square division be

```text
C=Q^2+Delta,       ord_sigma(Delta)=H,
Q mod sigma=z^2*(z^2+p),       p a unit.           (4.1)
```

For every

```text
0<H<=15,             ord_sigma(a)>=H/3,            (4.2)
```

the unloaded first square-normal block occurs at `2H<=30<42`.  The frozen
first-block divisibility bridge forces

```text
Delta/sigma^H mod sigma=m*z*(z^2+p),       m a unit. (4.3)
```

The exact coefficient isomorphism on `D(M)` then has central coordinates

```text
(a,E,U,R0,M,V,W0)=(0,p,0,0,m,0,0),                (4.4)
```

so `q>0`.  Finally,

```text
42 >= 14*H/5                                        (4.5)
```

is precisely (1.2).  The internal theorem excludes the arc.  Equality in
(4.5) is the reviewed `H=15` fixed ray; all `H<15` lie in its strictly
higher-load homogeneous cone.

## 5. Boundaries and nonclaims

- `H>15` is not covered: the effective load is below the homogeneous
  threshold.  The first new boundary is the graph-relative/mixed-load fan.
- `ord(a)<H/3` is an earlier moving-center face.  At `H=15`, the first raw
  center/load equality is `ord(a)=3`, and the exact affine-graph
  cancellation must be imposed before taking its Newton hull.
- A square, squarefree, triple-root, quadruple-root, `p=0`, `M=0`, or
  other factor-degenerate special fibre is routed separately by the factor
  classifier.  No `K10` unit is used: `K10=0` is included when all remaining
  effective loads satisfy (1.2).
- The source corollary is arcwise.  It is not a total-Rees atlas, a
  saturation/base-change theorem, or coverage of all normal/load slopes.

This theorem does not close the routed factor-degenerate receivers,
terminal/Taylor, order two, `(8,12)`, maximum twelve, or JC2.
