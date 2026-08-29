# Producer handoff: cutoff-six square-tail field obstruction

Date: 2026-08-28  
Producer: Sol Ultra, independent tail-six lane  
Status: `PASS-TAIL6-FIELD-LOCUS-EMPTY; HOSTILE REVIEW REQUESTED`

## Exact result

For the pinned branch-P square baseline, with every deformation parameter of
weight below six set to zero, the cutoff-six prefix has 220 retained raw
variables, 260 equations through `D11`, rank 98, and nullity 122.  The
literal endpoint equation is

```text
D22[X^0]-1=-1-p32*p110.
```

Rows 12 and 13 give field-radical implications

```text
F6=(X^4-1)^2 V,  deg(V)<=2,
V0=0  or  V0=4*p110.
```

On each of those two branches, exact tracked rational RREF of the row-14 and
row-15 compatibility lists gives `p110^2`.  With zero-based compatibility
indices, the frozen sparse witnesses are

```text
V0=0:
p110^2 = (1/12)r14[1] + (1/9)r14[13]
          -(2/9)(r15[3]+r15[7]+r15[11]+r15[15]).

V0=4*p110:
p110^2 = -r14[9] -(37/9)r14[13]
          +(16/9)r15[3] +(32/9)r15[7]
          +(256/45)r15[11] +(512/63)r15[15].
```

The checker reconstructs each selected compatibility from rational
combinations of the substituted literal source rows before reconstructing
`p110^2`; this rules out a cumulative-span emission artifact.  Together
with `1+p32*p110`, either branch target is unit by the direct identity

```text
1=(1-p32*p110)*(1+p32*p110)+p32^2*(p110^2).
```

No Groebner basis, Singular run, modular inference, dehomogenization, or AWS
job is involved.  The two row-13 branches cover all characteristic-zero
field-valued points, hence the fixed cutoff-six square-tail endpoint locus
has none.

## Scope firewall

This is only the fixed branch-P square baseline and cutoff-six tail.  The
row-12/13 parametrizations use field-radical implications, so this handoff
does not claim a lifted unit certificate for the upstream nonreduced ideal.
It does not cover the branch-P family and makes no Keller-pair,
counterexample, or JC2 claim.  Neither `D23` nor a `G22` slot is imposed.

## Direct replay

```bash
python3 cases/ggv_8_28_upper_endpoint_tail6_desk_20260828/analyze_tail6.py \
  --check \
  --output cases/ggv_8_28_upper_endpoint_tail6_desk_20260828
```

Expected marker:

```text
"direct_unit_certificate": "PASS_BOTH_ROW13_BRANCHES_NO_GB"
```

## Frozen custody hashes

```text
7481713f12c85134df27b647eedf5e6b437f8748b67a2bd4990d3fe37a0e66ed  cases/ggv_8_28_upper_endpoint_tail6_desk_20260828/RESULT.md
7ed247251df0122fa71211a945f7ab092a9f157bbe31842c3cc8c92f9d53b5fb  cases/ggv_8_28_upper_endpoint_tail6_desk_20260828/TAIL6_DESK_ANALYSIS.json
812dc5b7d337dc8a6bb68b5419c4ce0556c2e0ed29e1eb4213d5a79ece3a8269  cases/ggv_8_28_upper_endpoint_tail6_desk_20260828/UNIT_CERTIFICATE.json
86a0c851cea30bb397d4e80bb9cda8a6f50559d5cbc7de649a431960ecd10113  cases/ggv_8_28_upper_endpoint_tail6_desk_20260828/analyze_tail6.py
c038fd929d8c11cf8465dd72edb5fc4cca430140d11199f3c6fbd2f968e1b389  cases/ggv_8_28_upper_endpoint_tail6_desk_20260828/TAIL6/TAIL_DEFORMATION_SYSTEM.json
a411d66158b01e3baf611067e29b223d88370bf01e7c8d84e09e87e72023f626  cases/ggv_8_28_upper_endpoint_branch_p_20260827/tail_deformation.py
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

The exact-Q target custody hashes remain

```text
f2c59134e29b68c9a33e45aa418d1ce821755673f44e0793f2d23fc5685699d6  TARGETS/v0_zero_row14_15_localized_q.sing
e458f63fcb8964f4ebce98146ff577860a4e11222e43ad33f74334ca3a76e70c  TARGETS/v0_four_p110_row14_15_localized_q.sing
```

Hostile review should concentrate on (1) the row-12/13 field-radical cover,
(2) progressive substitution semantics in the tracked row-14/15 RREF, and
(3) whether the endpoint sign and parameter identities `p32=G15[X^1]`,
`p110=F7[X^0]` agree with the pinned raw system.
