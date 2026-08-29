# Cutoff-four upper-endpoint square tail: exact desk result

Date: 2026-08-28  
Status: `PROVISIONAL EXACT FIELD-POINT EXCLUSION; HOSTILE REPLAY REQUIRED`

## Result

The fixed branch-P square-baseline cutoff-four specialization has no
characteristic-zero field-valued point satisfying the upper endpoint.  The
proof is an exact standard-library rational calculation.  It uses a finite
sequence of field-radical divisibility implications, then an exhaustive
two-branch split.  It is not an upstream scheme-unit claim.

Run the replay with

```text
python3 -B analyze_tail4.py --check
```

No CAS is invoked.

## Pinned source and census

```text
RAW_DIRECT_SYSTEM.json
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0

RAW_INPUT.json
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
```

After setting every raw parameter of weight below four to zero, the literal
`D0,...,D7` prefix has 138 equations on 286 retained variables, exact rank
76, and nullity 210.  Substitution into `D8,...,D22` leaves 375 literal
generators.  The endpoint record is

```text
D22[X^0]-1 = -1-p32*p171+p86*p91,
```

or, with

```text
a=p32=G15[X^1],  b=p171=F7[X^0],
c=p86=G11[X^0],  d=p91=F11[X^1],
```

```text
1+a*b-c*d=0.
```

All four carriers remain literal; none is normalized or inverted.

## Exact square/divisibility cascade

Put `C=X^4-1` and `H=C^2`.  Every stated remainder inclusion has exact
compatibility cofactors and literal source-row provenance in
`TAIL4_DESK_ANALYSIS.json`.

1. The pure quadratic part of `D8` has rank seven inside the eight
   coefficients of `F4^2 mod H`.  Its coefficient kernel is exactly
   `(-1,0,0,0,1,0,0,0)`, the line spanned by `C`.  Modulo `C`, this gives
   `F4^2=0`; squarefreeness gives `F4=C*B` on field points.
2. `D9` contains all four coefficients of `B^2 mod C`, hence `B=C*V` and
   `F4=H*V`.
3. `D10` is the eight-coefficient space of `(F5-V/2)^2 mod H`, hence
   `F5=V/2+C*W`.
4. `D11` contains `W^2 mod C`, hence `W=C*R` and
   `F5=V/2+H*R`.
5. `D12` is `(F6-R/2)^2 mod H`, hence `F6=R/2+C*T`.
6. `D13` contains `T^2 mod C`, hence `T=C*U` and
   `F6=R/2+H*U`.
7. `D14` contains `(F7-U/2)^2 mod C`, hence `F7=U/2+C*S`.
8. The cumulative `D14+D15` compatibility space contains `S^2 mod C`,
   hence `S=C*Q` and `F7=U/2+H*Q`.

The `D8` mixed scalar is retained and solved monically; the monic `p86` and
`p106` consequences at `D11` are likewise retained in the audit.  These are
coordinate eliminations, not unit normalizations.

## Scalar core and carrier

Write

```text
x=V0, v=R0, r=U0, b=p171,
s=p196-(3/4)*x,
h=p152-s*x.
```

The three post-`D15` invariant equations are

```text
E13 = h*v -(3/4)*b*v +(3/2)*b*r -(3/8)*r^2,

E14 = h*r +(3/4)*b^2 -(3/2)*b*r +(3/16)*r^2
      -(3/8)*x*v^2,

E15 = h*b -(3/4)*b^2 -(1/8)*v^3 -(3/16)*x*v^2
      -(3/4)*x*v*r.
```

The exact carrier reconstruction is

```text
c=b*s+(3/4)*v*r+(3/16)*v^2.
```

The constant `p161=F8[X^0]` is absent from every charged determinant row.
The continuation uses the resulting additive-gauge slice `p161=0`; this
does not touch an endpoint carrier.

No new scalar invariant appears at `D16` or `D17`.  At `D18`, literal
compatibility gives

```text
K18 = v*(b*v+r^2)=0.
```

## Exhaustive field branches

### Branch `v=0`

Here the lower mode `x` drops out of the scalar core.  The exact identity

```text
3*b^3 = 2*b*E13+4*b*E14-4*r*E15  modulo v
```

forces `b=0` on field points, and the carrier formula then gives `c=0`,
contradicting the endpoint.  The stronger emitted certificate reconstructs
the literal constant `1` from

```text
endpoint, c_relation, E13, E14, E15, v
```

with polynomial cofactors and no division.

### Branch `v!=0`

Set `tau=r/v`.  Exact reduction of `E13,E14,E15,K18` gives

```text
b = -tau^2*v,
h = (3/8)*v*tau^2*(4*tau-1),
x = (tau^2/2)*(12*tau^2+6*tau+1),
v = -(3/4)*tau^2*P3(tau),

P3(tau)=1+10*tau+40*tau^2+64*tau^3
       =(4*tau+1)*(16*tau^2+6*tau+1).
```

An exact `D20` compatibility witness reconstructs

```text
tau^9*P3(tau)^3=0.
```

But `v!=0` and the displayed formula for `v` imply both `tau!=0` and
`P3(tau)!=0`, an immediate contradiction.  The endpoint is not used on
this branch.  The roots `tau=-1/4` and
`16*tau^2+6*tau+1=0` are precisely `v=0` boundary points of this chart;
they are not surviving open-branch cases.

## Mutation checks

- Deleting one `D8` pure equation enlarges the remainder kernel from one to
  two dimensions.
- Reversing the `V/2` shift at `D10` destroys remainder-span inclusion.
- Omitting the `D15` block destroys a named `S^2 mod C` coefficient.
- Deleting the `3*R0^2/16` carrier term leaves that exact nonzero monomial.
- Reversing an endpoint sign no longer matches the literal source record.
- Omitting `D20` loses the decisive open-branch target.
- Reversing the middle coefficient of `P3` gives a target outside the exact
  compatibility span.
- Omitting the first nonzero serialized `D20` cofactor no longer reconstructs
  the target.
- Dropping `v!=0` admits the displayed boundary roots with
  `P3=v=target=0`, confirming that the localization hypothesis is essential.

## Scope and firewalls

1. Every square-to-divisibility step is a characteristic-zero field-radical
   implication using squarefreeness of `C`; it is not a statement about the
   nonreduced upstream scheme.
2. The split `v=0` or `v!=0` is exhaustive only for field-valued points.
   The definition `tau=r/v` is confined to the second branch.
3. The open-branch `D20` witness is a rational linear combination after the
   explicitly serialized radical and branch substitutions.  It is not a
   global pre-radical ideal certificate.
4. The additive `p161` slice is a determinant symmetry, not an endpoint
   normalization.
5. `D23` is not imposed and there is no `G22` slot.
6. This result concerns only the fixed cutoff-four square-tail endpoint
   specialization.  It does not by itself exclude the full branch-P family,
   prove a Keller-pair theorem, or settle JC2.

## Frozen artifacts

```text
TAIL4/TAIL_DEFORMATION_SYSTEM.json
TAIL4_DESK_ANALYSIS.json
CERTIFICATES/tail4_R0_zero_unit.json
CERTIFICATES/tail4_R0_nonzero_D20.json
analyze_tail4.py
```
