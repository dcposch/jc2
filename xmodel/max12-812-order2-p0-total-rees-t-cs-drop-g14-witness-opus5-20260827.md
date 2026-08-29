# Exact-Q witness for the V18R1 `drop grade 14` negative control

Author: Opus 5, independent exact-algebra researcher
Date: 2026-08-27
Prompt SHA-256: `8a3f6e5274ca4042b7e8867b465d2a9be7bd9ceb47edfd319151597ba780d532`

## Verdict

**`EXACT_WITNESS`.**

There is an explicit rational point of the ordered `T-cs` special fibre that
kills all 21 charted grade-10--12 rows, satisfies `qrs=0`, `rho=0`,
`1-u*cs=0`, `1-v*k=0`, and does **not** satisfy `Tg14_5`.  Hence

```text
1 not in (Tg10_*,Tg11_*,Tg12_*, qrs, rho, 1-u*cs, 1-v*k)
```

over `Q`, which is exactly the assertion the frozen V18R1 negative control
(`noG14Unit==0`, token `V18_DROP_G14_NONUNIT=1`) is computing.  The
long-running standard-basis control is therefore **mathematically redundant**
and can be retired or cut short; see §8 for the exact conditions under which
that substitution is legitimate.

The witness is not isolated.  §6 gives the *complete* description of the
special fibre: it is an irreducible rational **31-dimensional** subvariety of
the 42-variable chart, so the control was never close to a knife edge.

## 1. The literal object under test

From frozen `compile_t_cs_rho_unit_v18.py`
(SHA-256 `50596db3a7009fa887e1679a8dbbc636afd68af66f923bfe13e7b5c3599548e6`)
and its three-name repair `compile_t_cs_rho_unit_v18r1.py`
(SHA-256 `c23c67a7f6f3e3071f384db229fe3ab4ba5578e0166dead85177a6923ef08ef6`),
the generated exact-Q script builds

```text
ring R=0,(u,v,<40 chart variables>),(dp(2),dp(40));
ideal Prefix12   = E1,...,E21;                     // charted Tg10_1..Tg12_7
ideal Localizers = ideal(qrs,rho,1-u*cs,1-v*k);
ideal NoG14      = std(Prefix12+Localizers);
int  noG14Unit   = (reduce(1,NoG14)==0);
if (noG14Unit!=0) { print("FAIL_DROP_G14_CONTROL_UNIT"); quit; }
```

`E1..E21` are the frozen exact-Q V9 grade-10/11/12 coefficients after the
literal chart substitution

```text
rs -> (cs*qrs),   c0 -> (cs*qc0),   c1 -> (cs*qc1)
```

applied by `chart_expression` with word-boundary regexes, so that `rs1`,
`rs2`, `cs1`, `cs2`, `k1`, `k2c`, ... are untouched.  I re-executed exactly
that substitution locally and recovered the compiler's ring: 40 chart
variables plus `u,v`, i.e. `ring_variable_count = 42`, matching the compiler's
own field.  The 40 are

```text
a0 a1 aa0 aa1 aaa0 aaa1 ac3 ac4 az3 az4 cs cs1 cs2 cs3 cs4 e0 e1 ec3 ec4
ee0 ee1 ell1 ell2 ell3 ell4 ez3 ez4 k k1 k10_3 k10_4 k2c qc0 qc1 qrs rho
rs1 rs2 rs3 rs4
```

(the `ac*/az*/ec*/ez*/ell3/ell4/cs3/cs4/rs3/rs4/k10_*` names enter the ring
only through `Tg14_5`, which the negative control drops; they remain ring
variables and so must still be assigned).

## 2. The witness

Base point, all 42 ring variables:

| variable | value | | variable | value |
|---|---|---|---|---|
| `cs` | `1` | | `e1` | `1` |
| `k` | `12/5` | | `u` | `1` |
| `v` | `5/12` | | | |
| `qrs` | `0` | | `rho` | `0` |
| `qc0` | `0` | | `qc1` | `0` |
| `a0` | `0` | | `a1` | `0` |
| `aa0` | `0` | | `aa1` | `0` |
| `aaa0` | `0` | | `aaa1` | `0` |
| `e0` | `0` | | `ee0` | `0` |
| `ee1` | `0` | | `ell1` | `0` |
| `ell2` | `0` | | `ell3` | `0` |
| `ell4` | `0` | | `cs1` | `0` |
| `cs2` | `0` | | `cs3` | `0` |
| `cs4` | `0` | | `k1` | `0` |
| `k2c` | `0` | | `k10_3` | `0` |
| `k10_4` | `0` | | `rs1` | `0` |
| `rs2` | `0` | | `rs3` | `0` |
| `rs4` | `0` | | `ac3` | `0` |
| `ac4` | `0` | | `az3` | `0` |
| `az4` | `0` | | `ec3` | `0` |
| `ec4` | `0` | | `ez3` | `0` |
| `ez4` | `0` | | | |

Compactly: **every variable is `0` except `cs=1`, `e1=1`, `k=12/5`, `u=1`,
`v=5/12`.**

Localizer residuals:

```text
qrs      = 0
rho      = 0
1-u*cs   = 1 - 1*1     = 0
1-v*k    = 1 - (5/12)*(12/5) = 0
cs = 1    != 0
k  = 12/5 != 0
```

so the point genuinely lies on `V(rs/cs) ∩ D_+(cs) ∩ D(k)` with `qrs=0`,
`rho=0`, as required.

## 3. All 21 exact residuals

Every charted grade-10--12 row evaluates to exact `0`:

| row | residual | | row | residual | | row | residual |
|---|---|---|---|---|---|---|---|
| `Tg10_1` | `0` | | `Tg11_1` | `0` | | `Tg12_1` | `0` |
| `Tg10_2` | `0` | | `Tg11_2` | `0` | | `Tg12_2` | `0` |
| `Tg10_3` | `0` | | `Tg11_3` | `0` | | `Tg12_3` | `0` |
| `Tg10_4` | `0` | | `Tg11_4` | `0` | | `Tg12_4` | `0` |
| `Tg10_5` | `0` | | `Tg11_5` | `0` | | `Tg12_5` | `0` |
| `Tg10_6` | `0` | | `Tg11_6` | `0` | | `Tg12_6` | `0` |
| `Tg10_7` | `0` | | `Tg11_7` | `0` | | `Tg12_7` | `0` |

The dropped row is nonzero, as it must be for consistency with the V18R1
positive:

```text
Tg14_5 = -21/320   != 0.
```

### 3.1 Hand-checkable reduction

Setting `qrs=0` and `rho=0` alone (before any other choice) reduces the 21
charted rows to the following, which anyone can confirm term-by-term against
the frozen `.poly` files:

```text
Tg10_1 : 3/8*a0*cs*qc1 + 3/8*a1*cs*qc0
Tg10_2 : 3/8*a0*cs*qc0 + 3/32*cs^2*qc1^2
Tg10_3 : 3/16*cs^2*qc0*qc1
Tg10_4 : 3/32*cs^2*qc0^2
Tg10_5 : 0
Tg10_6 : 0
Tg10_7 : 0
Tg11_1 : 3/8*a0*e1 + 3/8*a1*e0 + 3/8*aa0*cs*qc1 + 3/8*aa1*cs*qc0
         + 5/16*cs^2*k*qc0 - 5/16*cs^3*ell1*k
Tg11_2 : 3/8*a0*e0 - 3/8*a1*cs*ell1*qc1 + 3/8*aa0*cs*qc0 + 3/16*cs*e1*qc1
Tg11_3 : -3/16*a0*cs*ell1*qc1 - 3/16*a1*cs*ell1*qc0 + 3/16*cs*e0*qc1
         + 3/16*cs*e1*qc0
Tg11_4 : 3/16*cs*e0*qc0 - 3/32*cs^2*ell1*qc1^2
Tg11_5 : -3/32*cs^2*ell1*qc0*qc1
Tg11_6 : 0
Tg11_7 : 0
Tg12_1 : 3/8*a0*ee1 + 3/8*a1*ee0 - 3/8*a1^2*cs + 3/8*aa0*e1 + 3/8*aa1*e0
         + 3/8*aaa0*cs*qc1 + 3/8*aaa1*cs*qc0 + 5/16*cs*cs1*k*qc0
         + 5/16*cs*e0*k + 5/64*cs*k*qc1*rs1 + 15/256*cs*k*rs1^2
         - 15/16*cs^2*cs1*ell1*k + 5/16*cs^2*k1*qc0 - 5/16*cs^3*ell1*k1
         - 5/16*cs^3*ell2*k
Tg12_2 : -3/4*a0*a1*cs + 3/8*a0*ee0 - 3/8*a1*cs*ell2*qc1 - 3/8*a1*e1*ell1
         + 3/8*aa0*e0 - 3/8*aa1*cs*ell1*qc1 + 3/8*aaa0*cs*qc0
         + 3/16*cs*ee1*qc1 + 5/64*cs*k*qc0*rs1 - 5/16*cs^2*ell1*k*qc1
         - 15/64*cs^2*ell1*k*rs1 - 5/128*cs^4*k + 3/32*e1^2
Tg12_3 : -3/16*a0*cs*ell2*qc1 - 3/16*a0*e1*ell1 - 3/8*a0^2*cs
         - 3/16*a1*cs*ell2*qc0 - 3/8*a1*cs^2*qc1 - 3/16*a1*e0*ell1
         - 3/16*aa0*cs*ell1*qc1 - 3/16*aa1*cs*ell1*qc0 + 3/16*cs*ee0*qc1
         + 3/16*cs*ee1*qc0 - 5/32*cs^2*ell1*k*qc0 + 5/32*cs^3*ell1^2*k
         + 3/16*e0*e1
Tg12_4 : -9/32*a0*cs^2*qc1 - 9/32*a1*cs^2*qc0 - 3/16*cs*e1*ell1*qc1
         + 3/16*cs*ee0*qc0 - 3/32*cs^2*ell2*qc1^2 + 3/32*e0^2
Tg12_5 : -3/64*a0*cs*ell1^2*qc1 - 3/16*a0*cs^2*qc0 - 3/64*a1*cs*ell1^2*qc0
         - 3/32*cs*e0*ell1*qc1 - 3/32*cs*e1*ell1*qc0
         - 3/32*cs^2*ell2*qc0*qc1 - 3/64*cs^3*qc1^2
Tg12_6 : -3/64*cs^3*qc0*qc1
Tg12_7 : -3/128*cs^2*ell1^2*qc0*qc1
```

At the witness (`qc0=qc1=a0=a1=e0=aa0=aa1=aaa0=aaa1=ee0=ee1=ell1=ell2=cs1=k1=rs1=0`,
`cs=1`, `e1=1`, `k=12/5`) every displayed monomial contains one of the
zeroed variables except the two in `Tg12_2`:

```text
-5/128*cs^4*k + 3/32*e1^2 = -5/128*(12/5) + 3/32 = -3/32 + 3/32 = 0.
```

That single cancellation is the entire content of the witness; the other 20
rows vanish monomial-wise.

## 4. A parametric family, not a lucky point

Set, for any rationals `b,w` with `b*w != 0`:

```text
cs = b,   e1 = b^2*w,   k = (12/5)*w^2,   u = 1/b,   v = 5/(12*w^2),
```

all 38 other chart variables `= 0`.  Then all 21 rows vanish identically and

```text
Tg14_5 = -(21/320)*b^5*w^2.
```

Verified exactly at `(b,w) = (1,1), (1,-1), (2,3), (-3/5,7/2), (5,1/4)`;
in each case all 21 residuals are `0` and `Tg14_5` matches
`-(21/320)*b^5*w^2` exactly.  The reported base point is `(b,w) = (1,1)`.

## 5. The two-line reason the witness exists

On `qrs=rho=0` with `cs,k` invertible the system collapses by an exact
five-step forcing chain (each step is a literal identity in the reduced rows
of §3.1, and step 4 is a one-term syzygy):

```text
1.  Tg10_4  = 3/32*cs^2*qc0^2                                  => qc0 = 0
2.  Tg10_2| = 3/32*cs^2*qc1^2                                  => qc1 = 0
3.  Tg12_4| = 3/32*e0^2                                        => e0  = 0
4.  Tg12_3| + (1/2)*ell1*Tg11_1| = -3/8*a0^2*cs                => a0  = 0
      where  Tg11_1| = 3/8*a0*e1 - 5/16*cs^3*ell1*k
             Tg12_3| = -3/16*a0*e1*ell1 - 3/8*a0^2*cs + 5/32*cs^3*ell1^2*k
5.  Tg11_1| = -5/16*cs^3*ell1*k                                => ell1 = 0
```

(steps 1--5 are valid at any point of a field with `cs*k != 0`, in
characteristic `0` and equally in `65521`, since only `2,3,5` are inverted).

## 6. Complete description of the special fibre

After `qc0=qc1=e0=a0=ell1=0`, nineteen of the 21 rows vanish **identically**
and only two survive:

```text
Tg12_2| = -5/128*cs^4*k + 3/32*e1^2                        (i.e. 12*e1^2 = 5*cs^4*k)
Tg12_1| = 3/8*a1*ee0 - 3/8*a1^2*cs + 3/8*aa0*e1
          + 15/256*cs*k*rs1^2 - 5/16*cs^3*ell2*k
```

`Tg12_1|` is **linear in `ell2` with invertible coefficient** `-5/16*cs^3*k`,
so it can always be solved for `ell2`.  Therefore the drop-grade-14 special
fibre on `D(cs*k)` is exactly

```text
qrs = rho = qc0 = qc1 = e0 = a0 = ell1 = 0,
12*e1^2 = 5*cs^4*k,          cs*e1 != 0   (equivalently cs*k != 0),
ell2 = (16/(5*cs^3*k)) * (3/8*a1*ee0 - 3/8*a1^2*cs + 3/8*aa0*e1
                           + 15/256*cs*k*rs1^2),
u = 1/cs,  v = 1/k,
```

with the remaining **29** variables
(`a1 aa0 aa1 aaa0 aaa1 ac3 ac4 az3 az4 cs1 cs2 cs3 cs4 ec3 ec4 ee0 ee1 ell3
ell4 ez3 ez4 k1 k10_3 k10_4 k2c rs1 rs2 rs3 rs4`) completely free.  Since
`(cs,e1) = (b, b^2 w)` rationally parametrizes the conic `12e1^2 = 5cs^4k`,
this is an irreducible **rational 31-dimensional** variety, nonempty over `Q`
and over every field where `2,3,5` are invertible.

Five randomized points on this locus (random rationals in all 29 free slots,
`ell2` solved as above, seed `20260827`) were checked: all 21 residuals `0`
in every case.

## 7. Transfer to the `F65521` control lane

The F65521 lane inputs were checked to be the reductions of the exact inputs
(the same comparison the generated script performs via `FAIL_MODULAR_INPUT_*`):
all 22 charted pairs agree at 6 independent random points of `F65521^40`.
Reducing the base point (denominators `5, 12, 320` are units mod `65521`):

```text
cs = 1,   e1 = 1,   k = 12*inv(5) = 39315,   u = 1,   v = inv(k) = 38221,
all other variables 0.

21 residuals mod 65521 : all 0
Tg14_5 mod 65521       : 20680   != 0
1-u*cs, 1-v*k          : 0, 0
```

So the same witness discharges the negative control on **both** registered
lanes.

## 8. Does the negative-control computation remain necessary?

**No, as mathematics.**  A `Q`-point of `V(Prefix12+Localizers)` is a
complete proof that `1` is not in that ideal: evaluating any purported
identity `1 = sum f_i g_i` at the point would give `1 = 0`.  This is
strictly stronger than what the standard basis returns, is independent of
term order and of Singular, and costs no computation.  The same holds mod
`65521` by §7.

Three conditions bound that substitution, and all three are met here:

1. **Input custody.**  The witness is only about the frozen bytes.  All 21
   exact-Q V9 coefficient files and the V17 grade-14 file were hash-checked
   against their frozen manifests before use (§10).  If V18R1 runs against a
   different byte set, the witness says nothing.
2. **Same ring, same substitution.**  I re-derived the ring and the chart map
   from the frozen compiler, and recovered its own `ring_variable_count = 42`.
   The witness assigns all 42 variables, including the ten that enter the ring
   only through the dropped `Tg14_5`.
3. **Preregistration.**  `PREREGISTRATION.md` registers the control as part of
   the frozen protocol.  Replacing a preregistered computation with a proof is
   a protocol decision, not a mathematical one; if the campaign wants the
   frozen artifact set (`drop_g14.ideal` and its hash) it should still let the
   control finish.  My recommendation is to **cut the control short and record
   this witness in its place**, because the standard basis can only re-derive
   a fact that is now certified by hand, and the host time is better spent on
   V19's cofactor lift.

## 9. Secondary finding (firewalled): the V18R1 *positive* also follows

Restricting the frozen `Tg14_5` to the locus of §6 gives, exactly,

```text
Tg14_5| = -3/64*cs*e1^2 - 1/128*cs^5*k
        = -(21/320)*cs*e1^2                    (using 12*e1^2 = 5*cs^4*k)
        = -(7/256)*cs^5*k.
```

Since `cs` and `k` are units on the chart, `Tg14_5` is nonvanishing at every
point of the special fibre.  Hence `V(Prefix12,Tg14_5,Localizers)` is empty
over `Q̄`, so by the weak Nullstellensatz plus faithful flatness the V18
ideal (1) is the unit ideal over `Q` — which is the V18R1 positive claim.

**Firewall on this paragraph.**  This is an emptiness/Nullstellensatz
argument, not an explicit membership certificate: it exhibits no cofactors
`a_i` with `1 = sum a_i g_i`, and therefore does **not** discharge V19, whose
whole point is the explicit 26-generator lift `matrix(ideal(1))*U -
matrix(RawSpecial)*L = 0` with constant `U`.  V18R1's positive lanes have
already provisionally passed anyway; this is a cross-check on them, not a
replacement.  It is also downstream of the same frozen V9/V17 inputs, so it
inherits their source-provenance dependency and adds no independent evidence
about the upstream Faber source.

## 10. Independent corroboration from a frozen, unrelated artifact

I derived §§2--6 purely from the V18 charted rows, with no input from the
normalized odd sheet.  Only afterwards did I compare against the frozen
promotion `max12-812-order2-p0-odd-grade14-unit-elimination-promotion-20260826.md`
(SHA-256 `f48401b5a5635fa8212db76ac0f9f7eea44e8904e0b1aa18a4fbbc38389d56c3`).
The agreement is literal and complete, and it supplies the substitution map
rather than assuming one:

| frozen odd-sheet statement | this report, derived independently |
|---|---|
| `e0=a0=ell1=0` | §5 steps 3--5 |
| `12*e1^2-5*k0*b^4=0` | §6, `12*e1^2 = 5*cs^4*k` |
| `w=e1/b^2`, `k0=(12/5)*w^2` | §4 parametrization |
| `E_(5,14) = -(21/320)*b^5*w^2` | §4 `Tg14_5 = -(21/320)*b^5*w^2` |
| `= -(21/320)*b*e1^2` | §9 second form |
| `= -(7/256)*k0*b^5` | §9 third form |
| controls `700 mod 32003`, `20680 mod 65521` | `-21/320 = 700 (32003)`, `20680 (65521)` |

so the literal map is `b <-> cs`, `k0 <-> k`, `e1 <-> e1`, `rs=0 <-> qrs=0`,
`p=0 <-> rho=0`, `a0,e0,ell1` matching by name.  The odd-sheet report was
produced by a different producer against a different source manifest
(`b018dc4e...`) and an independently implemented sparse collector
(`9a4f6014...`), so this is genuine external agreement, not a restatement.

## 11. Method, and what was not done

Two mutually independent exact implementations, both pure substitution:

- `evaluate.py` (SHA-256 `7dce6118e571fd0390cb3d241f567982143b6b73f5e03a5bef42f777b30be93f`):
  Python `ast` walk of the charted Singular expression with `fractions.Fraction`
  arithmetic;
- `terms.py` (SHA-256 `b4cf51d074c36e55832728e6676813cff8f976b252ac656dfb1b4d036aac3f46`):
  hand-rolled sparse monomial parser on the *raw* files with the chart map
  applied at monomial level; shares no code with the first.

Both produce the same 21 zeros and the same `Tg14_5 = -21/320`.  Supporting
scripts: `chart.py` `c11a330676c6ac08...` (re-derives the compiler's chart map
and ring), `forcing.py` `dba1dde53e1e3598...` (symbolic forcing chain),
`family.py` `00f2af750507b47c...` (parametric + randomized locus),
`modlane.py` `60f2eaa9c5df549c...` (F65521 input comparison and transfer).
Monomial counts of the parsed rows: `4,5,5,2,5,1,5 | 12,14,17,3,18,1,18 |
27,36,47,12,58,9,60` and `304` for `Tg14_5`.

Not done, per instruction: no Groebner/standard basis, no ideal arithmetic,
no saturation, no elimination, no heavy local computation (peak work is
substituting into 304 monomials), no web access, no AWS mutation, no
`jc2-lean` read or write.  No claim here rests on the V18R1 positive result or
on a normalized analogy: §§2--6 are literal substitutions into the frozen
charted rows, and §10 is a post-hoc comparison.

## 12. Source hashes

Frozen protocol and compilers:

```text
b07e8e7ca19b9a90618e875c22dd797380cdd315bd9eec3ab5744d2f7b01ed95  PREREGISTRATION.md
02be2839a80706511e0a7be8e60220e0dad5b114c6c66d9004f55a2b4a2164b3  PREREGISTRATION_V18R1.md
50596db3a7009fa887e1679a8dbbc636afd68af66f923bfe13e7b5c3599548e6  compile_t_cs_rho_unit_v18.py
c23c67a7f6f3e3071f384db229fe3ab4ba5578e0166dead85177a6923ef08ef6  compile_t_cs_rho_unit_v18r1.py
8b29e8f46084ab0f527959ee55c6460d24d45c883280c0f7f667b9210418a249  validate_t_cs_rho_unit_v18r1.py
```

Consumed inputs (exact `Q`), each verified against its frozen manifest before
use:

```text
86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e  V9 aws_q_v9/COEFFICIENTS.json
9a055c5343e43abef6017f82d7aa0f9405d2152227dbd8d3ac4a0e74bac02fec  Tg10_1.poly
50c88196628dc04407c47c49059849f7f43265ade03afa13c9f27eecc1f928a6  Tg10_2.poly
4913e736b6713433411dc1513e8813968bace256b80e6597367ea9917f8a8cda  Tg10_3.poly
6c33503e153a1adda56810a62db220f74b1dfd8c71158d1f3794f128773c503d  Tg10_4.poly
5c1d7ae3fb821011d5c65bbd2bf81389587bbf82c515a9be03b095dfe095a5ec  Tg10_5.poly
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  Tg10_6.poly
080d52ab67b2d5a28c8a8cc35e912b9e99d4be8a53bfb73d1d9bc6d70b20b440  Tg10_7.poly
11f6bd635957677cb8a0b29cedc847369d68d6b695e844efdf32f683078db469  Tg11_1.poly
fa9c5c109541478fc56a0a4c9564a80cbdd9aeaa2bd8a1c2eabfa5076afb1093  Tg11_2.poly
52e685581979a789b4aa72457d982f269d0f344530fd1fab8af541f2570f1650  Tg11_3.poly
d56bce83a56222c76169b259f55b452be61cb892b55d71d0d34abdcdda5ca050  Tg11_4.poly
ca08b238d9d592e5736a167981857a6af60af908b2402e4ff43633fa6fc71ef2  Tg11_5.poly
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  Tg11_6.poly
3c298d36d1353ae5b7ec7e0ce597d2a2ab85ef6fbfe7eebe086e761343e0b156  Tg11_7.poly
799ccff5e54711c53da6498ac01f8ac3fae2290600fd19664238cb49ed8d6e54  Tg12_1.poly
b66a3e858c41d22b4ce3f4592cdee28664e5ba677f138860f840565625b073e6  Tg12_2.poly
b0d090f9000f6e74bd214a0c443450114994c3fd61a0a577453f8c69acc42f87  Tg12_3.poly
091117b510011acf659038b94b3c872423d7b568cb28b04fb2cf9555fd4da327  Tg12_4.poly
9389b34abad72debf6e621bb0082c2882c3cfcc02cbdcd1a00d03cdff89bf1aa  Tg12_5.poly
d545fc9b104202d5e4db12fbd56433ba7fd714f13669e9a11536dc47c9137ebf  Tg12_6.poly
68b897df93e18da37a237bbdddab4776f947d37bdc2444f4d2e3ea043ee79f75  Tg12_7.poly
91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7  Tg14_5_q.poly  (dropped row)
```

Modular control lane (used only for §7):

```text
dc7757090bac53482ff674794e4e45cf33ff052d10c34f4e29a1de4133befde4  V9 aws_p65521_v9/COEFFICIENTS.json
760d4f3b155decdf0e847a587254ae701f2b5948d8dd6135c52f5f213c10835b  Tg14_5_p65521.poly
```

Read for scope and corroboration only:

```text
ceea3b67169ab04d48f5ed96fa562b98d3b1a4e89eae7f4d94edc8d04c0aa412  xmodel/ideation-20260826T2350Z-synthesis.md
2c7f624cc6556ae2b106d58065391263f6e0f0c26da45e537b736815d0b593aa  xmodel/...t-cs-row5-g14-v17-promotion-sol-20260826.md
f48401b5a5635fa8212db76ac0f9f7eea44e8904e0b1aa18a4fbbc38389d56c3  xmodel/...p0-odd-grade14-unit-elimination-promotion-20260826.md
```

## 13. Scope firewall

This report establishes exactly one thing: **the frozen V18R1 drop-grade-14
negative control has an explicit exact-`Q` witness, so it will report
nonunit, and the standard-basis computation of that fact is redundant.**

It does **not**:

- prove or reprove the V18R1 positive as an explicit certificate (§9 is an
  emptiness argument only, and does not discharge V19);
- validate any V18R1 run, artifact, engine log, custody chain, or validator
  output — no V18R1 result was read or relied on;
- re-extract, re-derive, or independently confirm the upstream V9/V17
  coefficients; the entire witness is conditional on those frozen bytes, and
  their source-provenance dependency stands untouched;
- say anything about the other charts `T-c0`, `T-c1`, `T-a0`, `T-a1`, the
  `A` charts, chart overlaps, the terminal all-zero receiver, or `k=0`;
- close Gate T, order two, the `(8,12)` frontier, maximum twelve, or JC2;
- bear on TD6, the prime-ray lane, AS109, or any Lean formalization.

`jc2-lean` was not accessed.  No AWS state was read or mutated.  No campaign
computation was launched.  The only file written is this one.
