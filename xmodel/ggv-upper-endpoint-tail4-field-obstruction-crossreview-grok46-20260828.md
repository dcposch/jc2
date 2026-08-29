# Hostile cross-review: cutoff-four upper-endpoint field obstruction

Reviewer: Grok 4.6, independent hostile lane  
Date: 2026-08-28  
Producer packet: `cases/ggv_8_28_upper_endpoint_tail4_desk_20260828/`  
Temporary reconstruction: `/tmp/tail4_grok46_audit/` (outside the repository)

Charged pins (recomputed on live bytes):

```text
f5b3b6ec80648972f66b0bd057f0128bffba6682dc84d9348ded49093205ca9e  RESULT.md
2e4edbaded44a53eee1f4639f55617fbb94159c68be98d1c45f8b350b55d663c  analyze_tail4.py
3a1dc7eff0598e76cf0a284e2b4bc93d6e887b1069079cb0ecc5035783221fe5  TAIL4_DESK_ANALYSIS.json
```

All three match the charge.  This is a field-radical statement about
characteristic-zero field points of one fixed square-tail specialization.
It is not scheme emptiness, a branch-P theorem, or a JC2 theorem.

## Verdict

**PASS.**  Every charged exact atom survives independent reconstruction.
Nothing charged is REFUTED or sent back for REPAIR.  No missed
characteristic-zero field branch, denominator loss, or scope overclaim
was found.

| # | Charge | Verdict |
|--:|---|---|
| 1 | Source hashes, replay, cutoff-four census/rank/nullity/endpoint/carriers; stale specialization or row scaling | **CONFIRMED** |
| 2 | D8--D15 remainder models, progressive substitution, degree windows, eight field-radical steps, cumulative D14/D15, no carrier normalization | **CONFIRMED** |
| 3 | `E13,E14,E15`, carrier formula, additive `p161=0` gauge, D18 invariant `v*(b*v+r^2)` with provenance | **CONFIRMED** |
| 4 | `v=0` six-generator cofactor packet expands to literal `1`; endpoint/carrier signs; no localization | **CONFIRMED** |
| 5 | `v!=0` formulae for `b,h,x,v`; D20 combination equals `tau^9*P3^3`; `v!=0 => tau*P3!=0`; displayed roots are the `v=0` boundary; endpoint/D21/D22 unused | **CONFIRMED** |
| 6 | Hostile mutations of coefficients, shifts, signs, `P3`, D20 cofactors, localization; search for missed branch | **CONFIRMED** |

Producer replay is recorded as a hash check only.  Load-bearing identities
were re-derived by independent prefix compilation from the literal raw
recurrence, independently specified remainder models, independent
`h`-coordinate algebra, independent expansion of both frozen certificates,
and independent mutations.  No CAS and no `jc2-lean`.

## Strongest exact theorem

Work over a characteristic-zero field.  Start from the frozen branch-P
square baseline inside

```text
cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
SHA-256 ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
```

with raw-slot weights from

```text
cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
SHA-256 28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
```

Set every raw deformation parameter of weight below four to zero (the
seven `z_*` and ten `tt_*` slots).  Impose the literal rows `D0=...=D21=0`
and `D22=1`.  There is no `G22` slot and `D23` is not imposed.  Write
`C=X^4-1` and `H=C^2`.

**Theorem.**  This cutoff-four specialization has no characteristic-zero
field-valued point.

The proof is the eight squarefreeness implications of §2, followed by the
exhaustive field split `v=0` or `v!=0` on the D18 invariant, the `v=0`
Nullstellensatz unit of §4, and the `v!=0` identity `tau^9 P3(tau)^3=0`
in the D20 compatibility span of §5.  Each passage `P^2=0 mod C` (or
`mod H`) to `C|P` is a characteristic-zero field-radical implication, not
a statement about the nonreduced coefficient scheme.

No Keller pair, unrestricted branch-P family, other GGV branch, or JC2
statement is claimed.

## 1. Hashes, replay, independent prefix

Live SHA-256 of every frozen artifact matches `SOURCE.sha256` and
`EVIDENCE.sha256` except the self-hash of the evidence file, which is
not listed inside itself:

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0  RAW_DIRECT_SYSTEM.json
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876  RAW_INPUT.json
fbdda8422c1a5152de5f24a4ead5da45c2788293eb005e55e6b0af4f61d91fa8  PREREGISTRATION.md
7daebb9fae41211297d70759bf441163afe2c9f1714097727533da2708b7b3cf  SOURCE.sha256
16c79c06110de5dba897b78acadbca58069d59551ded931781e2d27a69decbf4  TAIL4/TAIL_DEFORMATION_SYSTEM.json
3247945c1df4d8118c60b137cdc7933edacad8bef79e077625817ad62ee9a859  CERTIFICATES/tail4_R0_zero_unit.json
b7397f15a6558e201340ff984f8227bafe9dc1479b9ddadd239926cd43c0d58f  CERTIFICATES/tail4_R0_nonzero_D20.json
```

Producer replay `python3 -B analyze_tail4.py --check` from the case
directory: exit 0 in 30.63 s, status `PASS`.  Printed payload hashes
equal the frozen bytes of the four JSON artifacts.  `--check` does not
itself `cmp` against disk; the printed hashes were compared here.

Independent prefix compile from the two raw JSON files (own RREF, own
weight table, no producer compiler):

| atom | independent | frozen |
|---|---:|---:|
| raw variables | 303 | 303 |
| weight `<4` deformation slots | 17 (`7 z + 10 tt`) | 17 |
| retained | 286 | 286 |
| prefix generators `D4..D7` | 138 | 138 |
| exact rank | 76 | 76 |
| nullity | 210 | 210 |
| remaining generators `D8..D22` | 375 | 375 |
| constraint-hash mismatches | 0 | — |
| term mismatches | 0 | — |
| annihilator failures of the 210-basis | 0 | — |

Weight formulae `f_i_j → 8+3i-j` and `g_i_j → 12+3i-j` match the
inventory with zero exceptions.  Prefix rows are linear in the retained
slots (0 nonlinear kept terms); 4574 low-weight monomials drop under
the cutoff, as they must.  Specialized constraint hashes match the
frozen file term-for-term, so there is no stale specialization and no
row scaling.

Literal endpoint, source generator 495, row 22, `X^0`:

```text
raw:          -1 - f_0_1*g_1_0 + f_1_0*g_0_1
specialized:  -1 - p32*p171 + p86*p91
display:       1 + p32*p171 - p86*p91 = 0
```

The display form is exactly minus the specialized generator.  Coefficients
remain `-1,-1,+1`; no scaling.  Carrier identification against the
nullspace basis:

| coordinate | raw slot | chart | lift |
|---|---|---|---|
| `p32=a` | `g_1_0` | `G15[X^1]` | pure `1` |
| `p86=c` | `g_0_1` | `G11[X^0]` | pure `1` |
| `p91=d` | `f_1_0` | `F11[X^1]` | pure `1` |
| `p171=b` | `f_0_1` | `F7[X^0]` | `f_0_1 + (3/2)g_8_29 - 3 g_4_17 + (3/2)g_0_5` |

The three G-terms in `p171` are the forced weight-7 characteristic
corrections on the prefix nullspace; the free F-slot is `f_0_1`.  Window
constants `F4[X^0]=p209`, `F5[X^0]=p195`, `F6[X^0]=p183`, `F7[X^0]=p171`,
`F8[X^0]=p161` are each the unique nullspace parameter carrying that
raw F-slot with coefficient `1`.  `D23` is not imposed; `G22` is absent.

## 2. D8--D15 remainder models and eight field-radical steps

Progressive substitution is load-bearing (each stage consumes the
previous parameterization).  Independently specified models, recomputed
compatibility, and frozen remainder certificates agree.  Degree windows:

| object | window | reason |
|---|---|---|
| `F4` | deg `<=12` (13 slots) | weight-4 F-window |
| `B` | deg `<=8` (9) | `F4=C*B` |
| `V` | deg `<=4` (5) | `B=C*V`, hence `F4=H*V` |
| `F5` | deg `<=11` (12) | weight-5 F-window |
| `W` | deg `<=7` (8) | `F5=V/2+C*W` |
| `R` | deg `<=3` (4) | `W=C*R` |
| `F6` | deg `<=10` (11) | weight-6 F-window |
| `T` | deg `<=6` (7) | `F6=R/2+C*T` |
| `U` | deg `<=2` (3) | `T=C*U` |
| `F7` | deg `<=9` (10) | weight-7 F-window; `F7[X^0]=b` preserved |
| `S` | deg `<=5` (6) | `F7=U/2+C*S` |
| `Q` | deg `<=1` (2) | `S=C*Q` |

Stage logs (independent = frozen):

| row | eq | cand | rank | free | displayed compat | span | remainder model |
|---:|---:|---:|---:|---:|---:|---:|---|
| D8 plain | 32 | 26 | 16 | 10 | 16 | 8 | 7 pure eqs inside `F4^2 mod H` |
| D8 after `F4=C*B` | 32 | 26 | 16 | 10 | 4 | 1 | mixed scalar in `p172,F6,F5,p196,B0` |
| D9 | 31 | 23 | 16 | 7 | 15 | 9 | all 4 coeffs of `B^2 mod C` |
| D10 | 30 | 21 | 14 | 7 | 16 | 8 | **equals** `(F5-V/2)^2 mod H` |
| D11 | 29 | 18 | 13 | 5 | 16 | 9 | all 4 coeffs of `W^2 mod C` |
| D12 | 28 | 16 | 12 | 4 | 16 | 8 | **equals** `(F6-R/2)^2 mod H` |
| D13 | 27 | 13 | 11 | 2 | 16 | 9 | all 4 coeffs of `T^2 mod C` |
| D14 | 26 | 11 | 10 | 1 | 16 | 9 | all 4 coeffs of `(F7-U/2)^2 mod C` |
| D15 | 25 | 8 | 8 | 0 | 17 | 11 | cumulative D14+D15 contains `S^2 mod C` |

D8 pure quadratic rank is 7; the 7×8 matrix of those equations against
the eight coefficients of `F4^2 mod H` has kernel exactly

```text
(-1, 0, 0, 0, 1, 0, 0, 0)
```

which is the remainder of `C=X^4-1` modulo `H`.  So `F4^2 ≡ 0 (mod C)`.
Squarefreeness of `C` in characteristic zero gives `C|F4` on field
points, `F4=C*B`.  After that parameterization the D8 compatibility
span is the single mixed scalar

```text
p172 - (3/2) F6[X^0] - (3/4) F5[X^0] - (1/4) p196 - (3/8) B0 = 0
```

solved monically for `p172`.  This is a coordinate elimination, not a
unit normalization.

D10 and D12 are span equalities with the eight-coefficient `mod H`
squares (stronger than inclusion).  D14 is only `mod C`, as RESULT
states: the eight-coefficient `mod H` square is **not** the D14 span.
D15 remainder inclusion uses the cumulative D14+D15 space; source-row
provenance of the four `S^2 mod C` certificates is exactly `{14,15}`.
Omitting the D15 block loses remainder degree 0 of `S^2 mod C`.

Eight field-radical implications, each using squarefreeness of `C` over
a characteristic-zero field and none promoted to a scheme equality:

1. `F4^2 ≡ 0 (mod C)` ⇒ `F4=C*B`
2. `B^2 ≡ 0 (mod C)` ⇒ `B=C*V`, hence `F4=H*V`
3. `(F5-V/2)^2 ≡ 0 (mod H)` ⇒ `F5=V/2+C*W`
4. `W^2 ≡ 0 (mod C)` ⇒ `W=C*R`, hence `F5=V/2+H*R`
5. `(F6-R/2)^2 ≡ 0 (mod H)` ⇒ `F6=R/2+C*T`
6. `T^2 ≡ 0 (mod C)` ⇒ `T=C*U`, hence `F6=R/2+H*U`
7. `(F7-U/2)^2 ≡ 0 (mod C)` ⇒ `F7=U/2+C*S`
8. `S^2 ≡ 0 (mod C)` from D14+D15 ⇒ `S=C*Q`, hence `F7=U/2+H*Q`

D11 excludes `p86` from the pivot list and writes it monically as a
polynomial in `(b,s,v,r)` after later substitution.  D15 excludes `p32`
likewise.  D14 does not substitute `F7[X^0]=p171`.  None of `a,b,c,d`
is set to one or inverted.  Frozen remainder certificates match the
independently recomputed cofactors and literal source-row provenance
at every degree.

## 3. Scalar core, carrier, gauge, D18

Write `x=V0`, `v=R0`, `r=U0`, `b=p171`, `s=p196-(3/4)x`,
`h=p152-s*x`.  Independently expanding the frozen monomials of
`E13,E14,E15` against this change of coordinates gives exact equality
with RESULT:

```text
E13 = h*v - (3/4)*b*v + (3/2)*b*r - (3/8)*r^2
E14 = h*r + (3/4)*b^2 - (3/2)*b*r + (3/16)*r^2 - (3/8)*x*v^2
E15 = h*b - (3/4)*b^2 - (1/8)*v^3 - (3/16)*x*v^2 - (3/4)*x*v*r
```

Post-D15 invariant intersection onto `{p152,p196,b,x,v,r}` has rank 3
and is the span of `{E13,E14,E15}`.  Literal provenance after
parameterizations: `E13` and `E14` from D14 source generators
`318,322,334,338`; `E15` from those four plus D15 generators
`344,348,352`.

Carrier reconstruction, independently from the D11 monic `p86` formula
after the later substitutions:

```text
c = b*s + (3/4)*v*r + (3/16)*v^2
```

matches both the frozen `c_formula` and RESULT.  The relation
`c_relation = p86 - c_formula` is monic in `p86`.

Additive gauge: `p161=F8[X^0]=f_0_0` occurs in **zero** of the 375
specialized constraints and in **zero** of the 513 raw generators.
The same holds for the parallel G-side line `p69=g_0_0=G12[X^0]`
(undocumented in RESULT; see nit N1).  The slice `p161=0` does not
touch an endpoint carrier.  It is the additive symmetry `F → F+μ t^8`
(`i-8=0` kills every `F8` contribution; `F8[X^0]` has vanishing
`X`-derivative).

No new invariant appears at D16 or D17 (ranks stay 3).  At D18 the
cumulative compatibility contains

```text
K18 = v*(b*v + r^2) = b v^2 + v r^2
```

as an exact linear combination of the post-D15 + D16 + D17 + D18
generators.  Independent reconstruction matches the frozen 64-term
cofactor list.  Literal source rows of `K18` are `{16,17,18}`
(generators `369..432` in the recorded provenance), with no D21/D22.
Invariant rank through D18 becomes 4, and the span equals
`{E13,E14,E15,K18}`.

Continuation logs, independent = frozen:

| row | eq | cand | rank | free | span |
|---:|---:|---:|---:|---:|---:|
| D16 | 24 | 7 | 7 | 0 | 12 |
| D17 | 23 | 6 | 6 | 0 | 17 |
| D18 | 22 | 5 | 5 | 0 | 17 |
| D19 | 21 | 3 | 3 | 0 | 18 |
| D20 | 20 | 2 | 2 | 0 | 18 |

## 4. Branch `v=0`

Substituting `v=0` into the `h`-forms and expanding independently:

```text
2*b*E13 + 4*b*E14 - 4*r*E15  |_{v=0}  =  3 b^3
```

so `3 b^3 = 0` on field points of characteristic zero, hence `b=0`.
The carrier then gives `c=0`, and the endpoint becomes `1=0`.

The stronger certificate is a polynomial identity in six generators,
no division, no carrier set to one.  Independently rebuilt cofactors
from the geometric identity `(1+z)(1-z+z^2)=1+z^3` with
`z=b(a-s d)`, the core `3b^3` identity, and the exact `v`-cofactor of
`2b E13+4b E14-4r E15-3b^3`, then multiplied against the frozen
generators, reconstruct the literal constant `1`.  The frozen packet
expands to the same unit.  Generator order
`endpoint, c_relation, E13, E14, E15, R0`.  Endpoint used here is the
display form `1+ab-cd`, equal to minus the specialized source record;
the ideals coincide.  Cofactor denominators are in `{1,2,3}`, so the
identity is genuinely characteristic zero (it cannot even be written
in characteristic 3).  No localization of `v` or of a carrier.

## 5. Branch `v!=0`

Set `tau=r/v`, so `r=tau v`.  `K18` and `v!=0` give `b=-tau^2 v`.
Independent substitution into `E13` produces

```text
h = (3/8) v tau^2 (4 tau - 1).
```

Independent substitution into `E14` produces

```text
x = (tau^2 / 2) (12 tau^2 + 6 tau + 1).
```

Independent substitution into `E15` then produces

```text
v = -(3/4) tau^2 P3(tau),
P3 = 1 + 10 tau + 40 tau^2 + 64 tau^3
   = (4 tau + 1)(16 tau^2 + 6 tau + 1).
```

These five formulae kill `E13,E14,E15,K18` identically as polynomials
in `tau` (with `p196` left free).  The identity
`v=-(3/4) tau^2 P3` forces: if `v!=0` then `tau!=0` and `P3!=0`.
The displayed roots `tau=-1/4` and `16 tau^2+6 tau+1=0` (discriminant
`-28`, not a square in `Q`) are precisely the `v=0` boundary of the
`tau` chart.  They are not open-branch points.  `tau=0` is likewise
`v=0`.

After the open substitution, the D16--D20 compatibility generators
are 92 polynomials in `(tau, p196, ...)` matching the frozen
certificate term-for-term.  An exact linear combination with 10
nonzero cofactors among 92 reconstructs

```text
tau^9 P3(tau)^3
= tau^9 + 30 tau^{10} + 420 tau^{11} + 3592 tau^{12} + 20640 tau^{13}
  + 82560 tau^{14} + 229888 tau^{15} + 430080 tau^{16}
  + 491520 tau^{17} + 262144 tau^{18}.
```

First nonzero serialized cofactor: index 35, value `-2998/4851`.
Literal source rows of this combination are `{17,18,19,20}`
(generators `393,409,416,424,428,432,438,442,446,450,459,463,467,471`;
`x`-degrees `{3,7,11,15,19}`).  D21, D22, and the endpoint are absent.
`D19` alone does not contain the target.  `p196` is not substituted on
this branch; the `{tau,p196}` projection of the D20 generators has
rank 2 and is spanned by two univariate polynomials in `tau`, the
second of which is exactly the target.  Common zeros of that rank-2
span are `V(tau P3)`.  The endpoint polynomial does not vanish
identically after the open substitution, confirming it is not silently
used.

Observation, not a defect: the same rank-2 projection also contains
`tau^8 P3^3`, via the exact identity

```text
(first projection generator) + 30*(target) = tau^8 P3^3.
```

`tau^7 P3^3` is not in the span, nor is `tau^9 P3^2`.  The serialized
witness charged in RESULT is exactly `tau^9 P3^3`.  The extra
`tau^8 P3^3` generator has the same field zeros given `v=-(3/4)tau^2 P3`,
and does not create a missed branch.

## 6. Hostile mutations and missed-branch search

| mutation | residual |
|---|---|
| Delete one D8 pure equation | remainder kernel dimension 2, not 1 |
| Replace D8 kernel by `(1,0,0,0,1,0,0,0)` (`X^4+1`) | not the computed kernel |
| Reverse the `V/2` shift at D10 | `(F5+V/2)^2 mod H` not contained in D10 |
| Drop the D10 shift entirely | `F5^2 mod H` not the D10 span |
| Reverse the `R/2` shift at D12 | not the D12 span |
| Omit the D15 block | `S^2 mod C` degree 0 not contained in post-D14 |
| Delete the `(3/16)v^2` carrier term | exact nonzero remainder `(3/16) R0^2` |
| Reverse one endpoint bilinear sign | no longer equals specialized source 495 |
| Reverse the endpoint constant sign | likewise mismatches |
| Omit D20 | D19 span does not contain `tau^9 P3^3` |
| Flip the middle coefficient of `P3` (`40 → -40`) | mutated target not in the D20 span |
| Flip `P3` constant or linear coefficient | not in the D20 span |
| Replace target by `tau^9 P3^2` | not in the D20 span |
| Omit serialized D20 cofactor index 35 | reconstruction ≠ target |
| Drop the hypothesis `v!=0` | `tau=-1/4` gives `P3=v=target=0`; those points are the `v=0` branch |

Missed-branch search, all negative:

- `v=0` is killed by a unit, not by a hidden division.
- `v!=0` is killed by D20 before D21/D22 and without the endpoint.
- `tau=0` and the three roots of `P3` are `v=0`, already covered.
- Extra D20 projection factors do not enlarge the field zero set of
  `{tau^8 P3^3, tau^9 P3^3}` beyond `V(tau P3)`.
- `p196` remains free and does not rescue `tau`.
- `p161=0` is a no-op (coordinate absent from every constraint).
- `a_partner` (the fourth post-D15 basis element) is unused on the
  open branch; extra constraints can only kill more points.
- Characteristic 2 would destroy squarefreeness of `C`; characteristic
  3 would destroy the `3b^3` identity.  Both are excluded by the
  characteristic-zero firewall.  Half-shifts `V/2,R/2,U/2` live in `Q`.
- The definition `tau=r/v` is confined to the open branch.
- No carrier is inverted, so there is no denominator loss at `c=0`
  or `a=0`.

## Issues, ranked

No load-bearing defect.  Two non-blocking notes.

**N1 (documentation).**  The same additive mechanism that licenses
`p161=F8[X^0]=0` also gives a free line `p69=g_0_0=G12[X^0]`, absent
from all 513 raw generators and all 375 specialized constraints.
RESULT names only the F-side gauge.  Harmless: a never-referenced free
line.

**N2 (observation).**  The D20 `{tau}`-projection has rank 2 and
contains both `tau^8 P3^3` and the serialized target `tau^9 P3^3`.
The charged witness is correct as stated.  The lower-power generator
does not change field zeros and is not required for the contradiction.

RESULT's scope firewalls (field vs scheme, `v=0`/`v!=0` split only
for field points, D20 witness after radical/branch substitutions not
a global pre-radical certificate, `p161` not a carrier normalization,
no `D23`/`G22`, cutoff-four only) are accurate and were respected by
the certificates.

## Promotion recommendation

**Promote** the packet as a desk-exact characteristic-zero field-point
exclusion of the **fixed cutoff-four square-tail specialization** of
the frozen branch-P upper endpoint.

**Do not promote** any of: emptiness of the nonreduced upstream scheme;
the full branch-P family; cutoffs 3, 2, or 5; other GGV branches;
Keller pairs; JC2.

The next honest exact target, if any, is a different cutoff or the
unreduced family, not a repair of this lane.
