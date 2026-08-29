# Exact branch-P class prefix through row 29 and a row-30 discriminator

Date: 2026-08-27  
Author: Sol Ultra  
Status: **EXACT DESK CONSTRUCTION; REVIEW PENDING**

## Verdict

There are two different questions, and their answers must not be conflated.

1. On the literal fixed endpoint fixture

   ```text
   A=X^4-1,  H=A^2,  F1=H  (V=1),  c2=0,
   ```

   no licensed class prefix through row 29 exists.  It already fails row 23:
   on the component `p^2=A`,

   ```text
   q1=F1/(4p^5)=1/(4p),
   ```

   and `dX/(4p)` is a nonzero holomorphic differential on the smooth
   projective normalization of `p^2=X^4-1`, hence is not exact.  This remains
   false after every constant-field extension.  In particular the old
   q1-negative `V=1` control is not a gate survivor and is not used below.

2. On the broader, independently reviewed branch-P cascade, where `V` is a
   branch coordinate rather than frozen to `1`, there is a two-parameter
   exact prefix over `Q[u,v]`.  Put `A'=dA/dX` and

   ```text
   F0=A^4,
   F1=F3=F5=F7=0,
   F2=4u A^2 A',
   F4=2u^2 (A')^2,
   F6=v,
   F8,...,F14=0.                                      (0.1)
   ```

   It satisfies licensed class rows 23--29.  At row 30, allowing an arbitrary
   frozen-window `F8`, its first noncancellable class is represented on
   `p^2=A` by

   ```text
   q8 = A F8/4 + (uv/4) A'/A + (u^4/4) (A')^4/A^3.    (0.2)
   ```

   At a root `a` of `A`, the residue is

   ```text
   Res_a(q8 dX)=(uv+90a u^4)/4.                        (0.3)
   ```

   The residues at `a=1,-1` generate exactly `(uv,u^4)` in `Q[u,v]`.
   Thus the rational specialization

   ```text
   u=1,  v=0                                           (0.4)
   ```

   is nontrivial, survives every licensed class row 23--29, and fails row 30
   with residue `45/2` at `X=1`.  The `F8` term is polynomial, so no allowed
   `F8` can cancel this class.  This is the requested first
   non-mod-8/noncancellable nonlinear test point.

The construction is a class-prefix result.  It is not a solution of the raw
affine endpoint target `D22=1`, and it proves no face, Keller, or JC2 result.

## 1. Frozen inputs and custody

The mathematical inputs used here, hashed from the live bytes before the
calculation, are:

```text
66735327e17350a2884f73eb593cb30b4a587cd0fb37a12285505565fd67af98
  xmodel/ideation-20260827T2259Z-opus5.md
70fd8be4d3e00b4e14869166186cedf218fd3cd4370d0dcc049543a6853eb762
  xmodel/ideation-20260827T2259Z-opus5-hostile-review-sol-ultra.md
71befadb3496f5f6c8e3136e7019de95dec2f205f2655734eac2c84d8e0e24d1
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md
60670d0a7066ab0a1d1f72ad05a0ff44a858fa39dbf4d18fd225913d26b6d114
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-crossreview-opus5-20260827.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md
6e3d9104effe39c0dd0e34377bb7bdc6ede4f25f472f9f9c0098706aceffb60a
  xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md
7358e6623a84ddd6b1aaad1a9b07a1c0c8966f74f75203977c0314bf3588e7ec
  xmodel/ggv-8_28-upper-cascade-w3-w6-hostile-review-fable5-20260827.md
5d5ec41a66b2fd7d5563efc5b662ce622424ad7ef06458ceec6a06f54d3c9c04
  cases/ggv_8_28_upper_cascade_w3_w6_20260827/PREREGISTRATION.md
ac3197988a3c0eba6b717194696b28f772550b789426087cbcfb3e6feee5ac37
  cases/ggv_8_28_upper_cascade_w3_w6_20260827/verify_upper_cascade.py
60e6b274ca6daa64dd5dc2ddb9cd62984dbefff3ae04d612f2ec36fe1e1e26bf
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/PREREGISTRATION.md
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

Repository basis was
`418e413593120d19e15e6546eb50c985f4b1f038`.  The reviewed all-row formula
and its corrected scope are used, as is the R8 fixed-receiver gauge.  No
shifted right-hand side is substituted for the licensed gate.

## 2. Why the literal `V=1` endpoint cannot supply the prefix

The all-row formula is

```text
q_n = 2/(n+2) [t^n] F(t)^((n+2)/8).                      (2.1)
```

For `n=1`, it gives `q1=F1/(4p^5)`.  The strict endpoint preregistration
fixes `F1=H=A^2` and `p^4=H`; on the component `p^2=A`, this is

```text
q1 dX=dX/(4p).                                           (2.2)
```

The quartic `A=X^4-1` is squarefree.  At a finite branch point, `p` is a
uniformizer and `dX/p` is regular and nonzero.  At either point over infinity,
`p` has order `-2` and `dX` has order `-2`, so `dX/p` is again regular and
nonzero.  Hence (2.2) is a nonzero holomorphic differential.  If it were
`df` for a rational function on the complete curve, `f` could have no pole
(differentiating a pole makes a pole), so `f` would be constant.  Contradiction.

There is also a polynomial certificate.  The reviewed branch-P `q1` image is

```text
T_A(Q)=2A Q'-3A'Q,       deg Q<=12.                       (2.3)
```

If `T_A(Q)=A^2`, reduction modulo `A`, twice, forces `Q=A^2S`.  Equation
(2.3) then becomes

```text
A'S+2AS'=1.                                               (2.4)
```

For nonzero `S` of degree `d`, the left side has leading coefficient
`(4+2d)lc(S)` in degree `d+3`; it cannot equal `1` in characteristic zero.
For `S=0` it is zero.  Thus row 23 fails before rows 24--29 are relevant.

The narrowest structural relaxation is not a larger constant field.  It is
to unfreeze `V`.  Intersecting `F1=A^2V` with (2.3) gives exactly

```text
Q=A^2R,       V=A'R+2AR',       deg R<=4.                 (2.5)
```

Thus `Q[r0,...,r4]`, with `R=sum_(i=0)^4 r_i X^i`, is the smallest natural
coordinate ring for the full row-23-surviving branch-P slice.  The explicit
prefix below uses its specialization `R=0`, hence `V=0`, and needs only the
two remaining parameters `Q[u,v]`; the discriminator point (0.4) is already
defined over `Q`.

## 3. Literal branch and window checks for the relaxed point

The reviewed branch-P cascade through row six is

```text
F1=HV,                         deg V<=7,
F2=(V^2+HZ)/4,                 deg Z<=6,
F3=(VZ+AT)/8,                  deg T<=9,
F4,F5,F6 arbitrary in deg <=12,11,10,
c2=0 or A|V.                                             (3.1)
```

For (0.1), take

```text
V=0,       Z=16uA',       T=0,       c2=0.                (3.2)
```

Then (3.1) gives exactly `F2=4uA^2A'` and `F3=0`; `F4` and
`F6` are among the expressly free slots.  The degrees are

```text
deg F2=11 <=14,       deg F4=6 <=12,       deg F6=0 <=10,
deg Z=3 <=6,
```

and every omitted `F_i` is zero in its literal window.  In particular this
does not smuggle in an `F15` or `F16` translation tail.

As a branch-membership cross-check, set all characteristic constants to zero
and take the coefficients through weight seven of `G=F^(3/2)`:

```text
G0=A^6,
G2=6u A^4 A',
G4=9u^2 A^2 (A')^2,
G6=(3/2)A^2v+2u^3(A')^3,
G1=G3=G5=G7=0.                                           (3.3)
```

They have degrees `24,19,14,<=9` in windows `24,22,20,18`, and direct
substitution in the determinant recurrence gives `D0=...=D7=0`.  This is
only a low-row geometric branch check.  The natural full formal completion
`G=F^(3/2)` is homogeneous (`D22=0`), not an affine endpoint witness.

## 4. Rows 23--29 from the reviewed all-row formula

Because (0.1) has only even positive weights, (2.1) gives
`q1=q3=q5=q7=0`.  The remaining coefficients are short:

```text
q2 = (1/2)[t^2]F^(1/2)
   = F2/(4A^2)
   = uA',

q4 = (1/3)[t^4]F^(3/4)
   = F4/(4A) - F2^2/(32A^5)
   = 0,

q6 = (1/4)[t^6]F
   = v/4.                                                 (4.1)
```

Exact primitives in `Q[u,v,X]` are therefore:

| row `m` | `n=m-22` | `q_n` | primitive `h_n`, `dh_n=q_n dX` |
|---:|---:|---|---|
| 23 | 1 | `0` | `0` |
| 24 | 2 | `uA'` | `uA` |
| 25 | 3 | `0` | `0` |
| 26 | 4 | `0` | `0` |
| 27 | 5 | `0` | `0` |
| 28 | 6 | `v/4` | `vX/4` |
| 29 | 7 | `0` | `0` |

This table is also a literal check of the correct gauge.  With

```text
nabla_m=d+(m/4)dH/H=p^(-m) o d o p^m,
```

the licensed row representative is `p^(-m)q_n dX`, and

```text
p^(-m)q_n dX = nabla_m(p^(-m)h_n).                       (4.2)
```

No copied shifted equation with bare right side `F_n` is used.  The argument
also does not require a global `mu_4` action: the odd coefficients vanish,
and the nonzero prefix coefficients are base-rational.  On the other branch-P
component `p^2=-A`, the same vanishing/exactness conclusions hold.

## 5. Row 30 is nonlinear and cannot be repaired by `F8`

For `n=8`, formula (2.1) reads

```text
q8=(1/5)[t^8]F^(5/4).
```

The contributions have `F`-degrees one through four:

```text
q8 = A F8/4
    +(2F2F6+F4^2)/(32A^3)
    -3F2^2F4/(128A^7)
    +7F2^4/(2048A^11).
```

Substitution of (0.1) gives (0.2).  The new-slot term `AF8/4` is a
polynomial and therefore exact for every allowed `deg F8<=8`.  Row 30 is
not a mod-8-dead row (`n+2=10`), but its new slot is class-dead on branch P;
the remaining class is the lower-slot nonlinear carry.

For an exact residue reduction, differentiate the two displayed rational
functions to obtain

```text
d((A')^3/A^2)
  = (3(A')^2A''/A^2 - 2(A')^4/A^3)dX,

d(A'A''/A)
  = ((A''^2+A'A''')/A - (A')^2A''/A^2)dX.
```

Since for `A=X^4-1`,

```text
(3/2)(A''^2+A'A''')=360X^4,
```

one gets

```text
(A')^4/A^3 dX
 = d(- (A')^3/(2A^2) - 3A'A''/(2A))
   +360(1+1/A)dX.                                        (5.1)
```

At a simple root `a` of `A`,

```text
Res_a(A'/A dX)=1,
Res_a(360/A dX)=360/A'(a)=90a,
```

which proves (0.3).  The two rational roots already suffice:

```text
4 Res_1  = uv+90u^4,
4 Res_-1 = uv-90u^4.
```

Their sum and difference generate `(uv,u^4)`.  At `(u,v)=(1,0)`,
`Res_1(q8dX)=45/2`, so row 30 fails.  Because `q8` is base-rational, it
cannot acquire a primitive only after adjoining `p`: tracing such a primitive
from `Q(X,p)` to `Q(X)` would give a rational primitive and contradict the
same residue.

## 6. Exact replay

The following is deterministic, standard-library-only exact arithmetic.  It
reuses only the pinned tiny `Q[X]`/rational-function implementation from the
reviewed upper-cascade verifier; it performs no Groebner basis or CAS call.

```bash
cd /Users/dc/code/math/jc2
PYTHONDONTWRITEBYTECODE=1 python3 -B <<'PY'
from fractions import Fraction as Q
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import sys

src = Path("cases/ggv_8_28_upper_cascade_w3_w6_20260827/verify_upper_cascade.py")
spec = spec_from_file_location("prefix29_uc", src)
m = module_from_spec(spec)
sys.modules["prefix29_uc"] = m
spec.loader.exec_module(m)

A = m.psub(m.ppow(m.X, 4), m.P1)
Ap = m.pder(A)
H = m.ppow(A, 2)

# Rational discriminator u=1,v=0, with F8=0.
F = [
    m.ppow(H, 2), m.P0, m.pscale(m.pmul(H, Ap), 4), m.P0,
    m.pscale(m.ppow(Ap, 2), 2), m.P0, m.P0, m.P0, m.P0,
]
assert F[2] == m.pscale(m.pmul(H, m.pscale(Ap, 16)), Q(1, 4))
assert all(m.pdeg(F[n]) <= 16-n for n in range(9))

# Independent low-row branch check via G=F^(3/2), all modes zero.
G = [m.fractional_coeff(F, H, m.ppow(H, 3), Q(3, 2), n)
     for n in range(8)]
assert all(m.pdeg(G[n]) <= 24-n for n in range(8))
assert m.determinant_rows(F[:8], G, 7) == [m.P0] * 8

# q_n with p^(n mod 2) factored off (p^2=A component).
q = {}
for n in range(1, 9):
    coeff = m.fractional_series(
        F, H, m.ppow(A, (n+2)//2), Q(n+2, 8), n
    )[n].scale(Q(2, n+2))
    q[n] = coeff

assert q[2] == m.rpoly(Ap)
assert all(q[n] == m.R0 for n in (1, 3, 4, 5, 6, 7))
target = m.Rat(m.ppow(Ap, 4), m.pscale(m.ppow(A, 3), 4))
assert q[8] == target

def rder(r):
    return m.Rat(
        m.psub(m.pmul(m.pder(r.num), r.den),
               m.pmul(r.num, m.pder(r.den))),
        m.ppow(r.den, 2),
    )

R = (-m.Rat(m.ppow(Ap, 3), m.ppow(A, 2)).scale(Q(1, 2))
     -m.Rat(m.pmul(Ap, m.pder(Ap)), A).scale(Q(3, 2)))
reduced = target.scale(4) - m.Rat((Q(360),), A) - m.Rat((Q(360),))
assert reduced == rder(R)
assert sum(Ap, Q(0)) == 4                              # A'(1)
assert Q(90, 4) == Q(45, 2)                            # row-30 residue

print({
    "status": "PASS",
    "D0_D7_zero": True,
    "rows23_29": ["0", "A'", "0", "0", "0", "0", "0"],
    "row30_residue_at_1": "45/2",
})
PY
```

Observed output:

```text
{'status': 'PASS', 'D0_D7_zero': True,
 'rows23_29': ['0', "A'", '0', '0', '0', '0', '0'],
 'row30_residue_at_1': '45/2'}
```

Input hashes replay with:

```bash
LC_ALL=C shasum -a 256 \
  xmodel/ideation-20260827T2259Z-opus5.md \
  xmodel/ideation-20260827T2259Z-opus5-hostile-review-sol-ultra.md \
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md \
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-crossreview-opus5-20260827.md \
  xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md \
  xmodel/ggv-8_28-upper-cascade-w3-w6-hostile-review-fable5-20260827.md \
  cases/ggv_8_28_upper_cascade_w3_w6_20260827/PREREGISTRATION.md \
  cases/ggv_8_28_upper_cascade_w3_w6_20260827/verify_upper_cascade.py \
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/PREREGISTRATION.md
```

No AWS service was contacted.  No heavy local algebra, floating point,
randomness, or external CAS was used.  No canonical ledger or source artifact
was edited.  No file in the Lean subtree was read, built, or modified.

## Scope firewall

Promotable after independent review:

- strict `V=1` nonexistence already at licensed row 23;
- the exact `Q[u,v]` branch-P class prefix (0.1) through row 29;
- the correct-gauge primitives (4.1)--(4.2);
- the row-30 formula, residue ideal `(uv,u^4)`, and rational discriminator
  `(u,v)=(1,0)`;
- literal frozen-window containment and the low-row branch check (3.3).

Not proved:

- `D22=1`, any raw endpoint extension, or any determinant row beyond the
  explicitly replayed low-row check;
- equality between the class-prefix locus and a raw polynomial-window
  elimination;
- a full classification of branch-P row-29 survivors;
- a face/family exclusion, polynomial Keller pair, counterexample, or JC2.

## Report body hash

The SHA-256 of all bytes strictly before this heading is:

```text
0853f0e581cc7cb926c602081cc0bb809d3c718c8849ff72365c5bee03ac0c0b
```

Replay it with:

```bash
sed '/^## Report body hash/,$d' \
  xmodel/ggv-quarter-root-branch-p-prefix29-construction-r0-sol-ultra-20260827.md \
  | shasum -a 256
```
