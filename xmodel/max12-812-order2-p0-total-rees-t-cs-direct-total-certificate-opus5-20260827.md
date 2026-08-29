# Direct total-family `rho` certificate for the ordered `T-cs` chart

Author: Opus 5, independent JC2 co-researcher
Date: 2026-08-27
Repo: `/Users/dc/code/math/jc2`, git HEAD `418e413593120d19e15e6546eb50c985f4b1f038`

## Verdict

**`DIRECT_CERTIFICATE`.**

There is an exact polynomial identity of the reviewed type, in the honest
ordered `T-cs` presentation, with the **trivial** `rho` cofactor:

```text
cs^447 * k^164 * (1 + rho*W)      with   W = 0
  in ( Tg10_1..Tg12_7, Tg14_5,
       rs-cs*qrs, c0-cs*qc0, c1-cs*qc1,
       qrs )                                             (*)
```

`N = 447`, `M = 164`, `W = 0`.  No factor of `cs` and no factor of `rho` is
inverted anywhere in (*); the only localization used is at `k`, and it is
paid for by `k^164`, i.e. by the already registered `k=0` residual stratum.
`W = 0` is admissible and is the strongest instance of the requested type:
`1 + rho*W` is required to be a unit-plus-`rho` cofactor, and `1` is one.

`N` and `M` are **not claimed minimal**; §6.3 explains exactly where their
size comes from and what would shrink them.

The reason `W = 0` is available is a finding not present in the four
reviewed documents:

> On `D(cs*k)` the registered ordered `T-cs` chart stratum is **empty
> outright**, not merely empty over `rho=0`.  The `rho != 0` half of that
> emptiness is a three-line consequence of the **grade-10 rows alone**
> (§4), needs neither grade 11, 12, nor 14, and is where the promoted
> `1 + rho*W` shape degenerates to `1`.

Because of this, the certificate is genuinely *total-family* and not a
repackaged special-fibre statement: the promoted grade-14 fibre theorem
(`sol-20260827`) supplies only the `rho = 0` half of (*).

## 0. What was read, and what this is conditional on

Read in full and used:

```text
16ec6f54e80a420755a52b8d2068390b65344311a5f84c4d486192513a928867
  xmodel/total-rees-localized-rho-unit-staged-calculus-promotion-sol-20260827.md
d9e5f43954240eee13311c5f386231f9ed506c4bbe978211cdfa711e3e8c86d9
  xmodel/max12-812-order2-p0-total-rees-t-cs-drop-g14-witness-opus5-20260827.md
7fbd9423b6840e4f3017687897e0dad373a04d2683589ccb432682553053c3cf
  xmodel/max12-812-order2-p0-total-rees-t-cs-drop-g14-witness-hostile-review-grok-20260827.md
5fd19f3577fbd24e74f2c395ab6fd17f84d75f73e00eeae53267536c33265fd4
  xmodel/max12-812-order2-p0-total-rees-t-cs-grade14-decisive-fibre-promotion-sol-20260827.md
b07e8e7ca19b9a90618e875c22dd797380cdd315bd9eec3ab5744d2f7b01ed95  PREREGISTRATION.md      (V18)
02be2839a80706511e0a7be8e60220e0dad5b114c6c66d9004f55a2b4a2164b3  PREREGISTRATION_V18R1.md
50596db3a7009fa887e1679a8dbbc636afd68af66f923bfe13e7b5c3599548e6  compile_t_cs_rho_unit_v18.py
c23c67a7f6f3e3071f384db229fe3ab4ba5578e0166dead85177a6923ef08ef6  compile_t_cs_rho_unit_v18r1.py
60692d787fe0a3e9bec285e038bc3bb69a4bf820413b9e2ba6db514e6b850472  PREREGISTRATION.md      (V19)
132108305f80db09e08572a2d5d623be968cd15612b3afe411f5840dd78ef17a  compile_t_cs_certificate_v19.py
```

All 22 consumed exact-`Q` row files were rehashed against their frozen
manifests before use and every hash matched (§9).  **Everything below is
conditional on those frozen V9/V17 bytes.  Their upstream literal-source
(Faber emitter) provenance debt is untouched and is inherited in full.**
No V18R1 or V19 engine output was read or relied on; no AWS state was read
or mutated; `jc2-lean` was not accessed; no web access.

## 1. Presentation, and the translation lemma

Work in the ordinary polynomial ring

```text
S# = Q[ cs, rs, c0, c1, qrs, qc0, qc1, rho, k, a0, a1, aa0, aa1, aaa0, aaa1,
        e0, e1, ee0, ee1, ell1..ell4, cs1..cs4, k1, k2c, k10_3, k10_4,
        rs1..rs4, ac3, ac4, az3, az4, ec3, ec4, ez3, ez4 ]
```

with the three `T-cs` bilinears and the ordered equation

```text
Bil = ( rs-cs*qrs,  c0-cs*qc0,  c1-cs*qc1 ),        z = qrs.
```

`cs` is the exceptional coordinate, `k` the genuine source localizer, `rho`
the deformation parameter.  Let `T = (Tg10_1..Tg12_7, Tg14_5)` be the 22
literal total rows as frozen (raw variables `rs, c0, c1`, no substitution).
Write

```text
K  = ( T, Bil, qrs )  subset S#.
```

**Lemma 0 (translation; verified for all 22 rows).**  For each row `f in T`
there are explicit polynomials `B_rs, B_c0, B_c1, B_qrs` with

```text
f = E_f + B_rs*(rs-cs*qrs) + B_c0*(c0-cs*qc0) + B_c1*(c1-cs*qc1) + B_qrs*qrs,
```

where `E_f` is `f` after `rs -> 0, c0 -> cs*qc0, c1 -> cs*qc1`.  The `B`'s
are the ordinary telescoping divided differences, computed by staged exact
division; the identity was checked term-by-term for every row.  Cofactor
term counts `(|B_rs|,|B_c0|,|B_c1|,|B_qrs|)`:

```text
Tg10_1 (2,1,1,1)    Tg11_1 (6,2,2,4)    Tg12_1 (11,3,3,8)
Tg10_2 (4,1,3,2)    Tg11_2 (9,2,4,6)    Tg12_2 (18,3,7,14)
Tg10_3 (2,2,2,1)    Tg11_3 (8,4,4,5)    Tg12_3 (21,7,8,15)
Tg10_4 (0,2,2,0)    Tg11_4 (0,1,3,0)    Tg12_4 (3,2,6,3)
Tg10_5 (2,2,2,1)    Tg11_5 (8,5,5,5)    Tg12_5 (28,12,14,19)
Tg10_6 (0,0,0,0)    Tg11_6 (0,0,0,0)    Tg12_6 (9,3,5,5)
Tg10_7 (2,2,2,1)    Tg11_7 (8,5,5,5)    Tg12_7 (29,14,16,20)
                                        Tg14_5 (131,38,45,97)
```

Consequently `K = (E_f : f in T) + Bil + (qrs)` and, writing

```text
S = Q[ cs, k, rho, qc0, qc1, and the 30 remaining names ],
I = ( E_1, ..., E_22 )  subset S,
```

**an identity `P in I` is the same thing as `P in K`, with the bilinear and
`qrs` cofactors supplied by Lemma 0.**  Nothing here is inverted.  This is
exactly the compiler's `chart_expression` map composed with `qrs = 0`; the
22 charted rows and their term counts `4,5,5,2,5,0,5 | 12,14,17,3,18,0,18 |
27,36,47,12,58,9,60 | 304` reproduce the frozen compiler and both
independent counts in the reviewed documents.  Note `Tg10_6 = Tg11_6 = 0`
literally.

Lemma 0 is a small **new obligation** for any certificate harvested from
V18/V19: those scripts consume the *substituted* rows `E_f`, so their output
lives in the substituted presentation, and returning it to the honest
ordered presentation of the promotion theorem needs precisely these `B`'s
(§7).

## 2. Statement to be proved

```text
cs^N * k^M  in  I,   with N = 447, M = 164.                       (**)
```

By Lemma 0 this is (*) with `W = 0`.

Structure: `I` contains an element that is a pure `rho`-power times
`cs^6 k^2` (§4, `rho != 0` half, grade 10 only), and an element that is
`cs^{147} k^{54}` plus a multiple of `rho^2` (§5, `rho = 0` half).
Multiplying them out gives (**) (§6).

All `rho` occurrences in all 22 rows are **even** (`rho^0, rho^2, rho^4,
rho^6, rho^8`), so throughout we may write `p := rho^2` without loss.

## 3. The grade-10 core

Set `u := cs*qc0`, `w := cs*qc1`, `p := rho^2`, `kap := (5/6)*cs^3*k*p`.
Four exact combinations of the charted grade-10 rows (each verified by
expansion):

```text
gam := (8/3) *Tg10_1                              = a0*w + a1*u + kap
del := (8/3) *Tg10_2                              = a0*u + (1/4)*w^2 + p*a1*w
alp := (16/3)*( Tg10_3 - (p/2)*Tg10_1 )           = u*w
bet := (32/3)*Tg10_4                              = u^2 + p*w^2
```

Two further exact facts, both certified, that will not be needed but pin the
structure: `Tg10_5 = (p/2)*Tg10_3 - (3/8)*p^2*Tg10_1` identically, and
`Tg10_6 = 0`.

**Proposition 3.1 (set level).**  Over any field in which `2,3,5` are
invertible, the four charted grade-10 rows have **no** common zero with
`cs != 0`, `k != 0`, `rho != 0`.

*Proof.*  `alp = 0` gives `u*w = 0`.  `bet = 0` gives `u^2 = -p*w^2`.  If
`w = 0` then `u^2 = 0`, so `u = 0`; if `u = 0` then `p*w^2 = 0` and `p != 0`
forces `w = 0`.  Either way `u = w = 0`, whence `gam = kap = (5/6)cs^3 k p
!= 0`, a contradiction. ∎

This is the whole reason the total-family certificate exists with `W = 0`,
and it uses no grade 11, 12 or 14 input.

## 4. Branch (a): the `rho != 0` half, in closed form

Proposition 3.1 is realised by an explicit five-line triangular chain.  Each
line is an exact identity of polynomials; `|` marks a certified element of
the grade-10 ideal.

```text
a0*u^2      = u*del - (1/4)*w*alp - a1*p*alp                        |
p*a0*w^2    = a0*bet - a0*u^2                                       |
p*w^3       = w*bet - u*alp                                         |
w^3+4p a1w^2= 4*w*del - 4*a0*alp                                    |
p^2*a1*w^2  = (1/4)*( p*(w^3+4p*a1*w^2) - p*w^3 )                   |
p*a1*u^2    = p*a1*bet - p^2*a1*w^2                                 |
p*kap*u     = p*u*gam - p*a0*alp - p*a1*u^2                         |
p*kap*w     = p*w*gam - p*a1*alp - p*a0*w^2                         |
p*kap^2     = p*kap*gam - a0*(p*kap*w) - a1*(p*kap*u)               |
```

Since `kap = (5/6)cs^3*k*p`, the last line is `(25/36)*cs^6*k^2*rho^6`.
Normalising:

**Certificate (a).**

```text
cs^6 * k^2 * rho^6
  = A1*Tg10_1 + A2*Tg10_2 + A3*Tg10_3 + A4*Tg10_4          (in I)
```

with, exactly,

```text
A1 = -24/5*a0*cs*qc1*rho^2 - 72/25*a1*cs*qc0*rho^2
     - 384/25*a0*a1*rho^4 + 16/5*cs^3*k*rho^4
A2 = -96/25*a0*cs*qc0 - 96/25*a1*cs*qc1*rho^2
A3 =  48/25*a0*cs*qc1 - 48/25*a1*cs*qc0 + 768/25*a0*a1*rho^2
A4 = 384/25*a0^2 + 96/25*a1*cs*qc1 + 384/25*a1^2*rho^2
```

In the **honest ordered presentation** of §1 the same statement reads

```text
cs^6*k^2*rho^6 = A1*Tg10_1 + A2*Tg10_2 + A3*Tg10_3 + A4*Tg10_4
                 - B_rs *(rs-cs*qrs) - B_c0*(c0-cs*qc0)
                 - B_c1*(c1-cs*qc1) - B_qrs*qrs
```

with

```text
B_rs  = -3/160*a0*cs*k*qc0*rs^2 - 3/160*a0*cs^2*k*qc0*qrs*rs
        - 9/40*a0*cs^2*k*qc1*rho^2*rs - 3/160*a0*cs^3*k*qc0*qrs^2
        - 9/10*a0*cs^3*k*qc0*rho^2 - 3/160*a1*cs*k*qc1*rho^2*rs^2
        - 9/40*a1*cs^2*k*qc0*rho^2*rs - 9/40*a0*cs^3*k*qc1*qrs*rho^2
        - 3/160*a1*cs^2*k*qc1*qrs*rho^2*rs - 9/40*a1*cs^3*k*qc0*qrs*rho^2
        - 3/160*a1*cs^3*k*qc1*qrs^2*rho^2 - 9/10*a1*cs^3*k*qc1*rho^4
        + 3/16*cs^4*k^2*rho^4*rs + 3/16*cs^5*k^2*qrs*rho^4
B_c0  =  36/25*a0^2*c0 + 9/25*a0*c1*cs*qc1 + 9/25*a1*c0*cs*qc1
        - 9/25*a1*c1*cs*qc0 + 144/25*a0*a1*c1*rho^2 + 9/25*a1*cs^2*qc0*qc1
        + 36/25*a1^2*c0*rho^2 - 72/25*a0*a1*cs*qc1*rho^2 + 6/5*a1*cs^3*k*rho^4
B_c1  = -9/25*a0*c1*cs*qc0 + 36/25*a0^2*c1*rho^2 - 9/25*a1*cs^2*qc0^2
        + 72/25*a0*a1*cs*qc0*rho^2 + 36/25*a1^2*c1*rho^4 + 6/5*a0*cs^3*k*rho^4
B_qrs = -3/160*a0*cs^4*k*qc0*qrs^2 - 9/10*a0*cs^4*k*qc0*rho^2
        - 9/40*a0*cs^4*k*qc1*qrs*rho^2 - 9/40*a1*cs^4*k*qc0*qrs*rho^2
        - 3/160*a1*cs^4*k*qc1*qrs^2*rho^2 - 9/10*a1*cs^4*k*qc1*rho^4
        + 3/16*cs^6*k^2*qrs*rho^4
```

This identity in `S#` was expanded and checked to be exact, and separately
evaluated at six random exact rational points by an independently written
parser/evaluator (§8).  It is the complete `rho != 0` half of (*), printed
in full.

## 5. Branch (b): the `rho = 0` half

Write `Ebar_i := E_i|_{rho=0}` and `J := (Ebar_1..Ebar_22) subset Sbar`,
`Sbar := S/(rho)`.  Here `Ebar` reproduces, term for term, the §3.1 display
of the producer report and its Grok re-derivation; I recomputed it from the
raw bytes rather than reading it.

Everything in this section happens in `Sbar[1/(cs*k)]`.  `cs` is inverted
**only inside the derivation**; the section's output (5.5) is a polynomial
identity with `cs^147` on the left, so `cs` is never asserted to be a unit
in the certificate.

### 5.1 Seven certified solved forms

Each is a rewrite `head -> tail`, exact modulo `J`, with the displayed
cofactors.  All seven were verified by expansion.

```text
B1  ell1    = 6/5*a0*e1/(cs^3*k) + 6/5*a1*e0/(cs^3*k)
              + 6/5*aa0*qc1/(cs^2*k) + 6/5*aa1*qc0/(cs^2*k) + qc0/cs
        from  (-16/5)*cs^-3*k^-1 * Tg11_1

B2  qc0*qc1 = 0                 from  (16/3)*cs^-2 * Tg10_3
B3  qc0^2   = 0                 from  (32/3)*cs^-2 * Tg10_4
B4  qc1^3   = 0                 from  (32/3)*cs^-2*qc1 * Tg10_2
                                    + (-64/3)*a0*cs^-3 * Tg10_3

B5  a0*e0   = -aa0*cs*qc0 - (1/2)*cs*e1*qc1 + a1*cs*ell1*qc1
        from  (8/3) * Tg11_2

B6  e0^2    = -2*cs*ee0*qc0 + 3*a0*cs^2*qc1 + 3*a1*cs^2*qc0
              + 2*cs*e1*ell1*qc1 + cs^2*ell2*qc1^2
        from  (32/3) * Tg12_4

B7  a0^2    = (1/2)*e0*e1/cs + (1/2)*ee0*qc1 + (1/2)*ee1*qc0
              - (1/2)*a0*ell2*qc1 - a1*cs*qc1 - (1/2)*a1*ell2*qc0
        from  (-4/3)*cs^-1*ell1 * Tg11_1 + (-8/3)*cs^-1 * Tg12_3
```

`B2, B3, B4` have **exactly zero tails**.  Hence, with
`U := (qc0, qc1)`,

```text
U^3  subset  J[1/(cs*k)],                                          (5.1)
```

because every degree-3 monomial in `qc0, qc1` is divisible by `qc0^2`,
`qc0*qc1` or `qc1^3`, and each of those three *is* an element of
`J[1/(cs*k)]` with the one-term cofactor shown.

### 5.2 The decisive grade-14 combination

Exactly, as an identity of polynomials,

```text
Tg14_5|_{rho=0} + (cs/2)*Tg12_2|_{rho=0}
  = -(7/256)*cs^5*k  +  g,        g in (qc0, qc1, e0, a0, ell1).      (5.2)
```

`g` has 57 terms; the single term of the left side free of
`{qc0,qc1,e0,a0,ell1}` is `-(7/256)*cs^5*k`.  (5.2) is the polynomial
sharpening of the reviewed `-(7/256)*cs^5*k` restriction; unlike the
reviewed version it is stated *before* any slice is taken, so it is usable
as a certificate.

### 5.3 One reduction

Let `X` be the normal form of `(256/(7*cs^5*k))*g` under `B1..B7` (rule
priority `B1, B2, B3, B4, B5, B6, B7`; 1880 rewrites).  Then

```text
1 - X = sum_i C_i * Ebar_i                                          (5.3)
```

exactly, with `C` supported on nine rows and `X` supported entirely in
`(qc0,qc1,e0,a0)`:

```text
|C_i| :  Tg10_2 32, Tg10_3 277, Tg10_4 87, Tg11_1 200, Tg11_2 51,
         Tg12_2 1, Tg12_3 38, Tg12_4 29, Tg14_5 1        (716 terms)
|X|   :  341 terms;  denominators cs^16 k^6;  C denominators cs^18 k^6
canonical sha256:  X  a0b896b2c0974846a0e4b3cf3c28d19ef97b07a7d6ad9a3f6c5b87dfe5e0d935
                   C  6fe2e6d47f594b77374f731660b91e5ee1de7ce6f11bbc7cc4b3c4fd034f3490
```

The surviving normal monomial shapes of `X` are only

```text
qc1^2, a0*qc1^2, a0*qc1, qc0, e0*qc1, a0*qc0, e0*qc1^2, e0*qc0,
qc1, e0, a0
```

so `X` lies in `(qc0,qc1,e0,a0)` and `a0*e0` never survives (that is `B5`).

### 5.4 `X^3` falls into `U`

Let `phi` be the quotient by `U = (qc0,qc1)`, i.e. `qc0 = qc1 = 0`.  Then
`phi(X)` has 13 terms and, exactly,

```text
phi(X)^3 = sum_i D_i * phi(Ebar_i),   D supported on
           Tg11_1 (10), Tg11_2 (152), Tg12_3 (10), Tg12_4 (156)
           (328 terms; denominators cs^36 k^9)
canonical sha256:  D  2259935f04449d33e53fdc9ed2df67697e0ea3935df51628d05653fdb9a190b6
```

Lifting the `D_i` verbatim, and setting `W_J := sum_i D_i*Ebar_i in J`,

```text
Y := X^3 - W_J   satisfies   phi(Y) = 0,   i.e.   Y in U.           (5.4)
```

This is where `a0` and `e0` die: modulo `U`, `B5` gives `a0*e0 = 0`, `B6`
gives `e0^2 = 0`, `B7` gives `a0^2 = (e1/2cs)*e0`, so `(a0,e0)^3 subset U`.
`phi(X)^2` still has 6 terms; `phi(X)^3` is exactly zero.

### 5.5 Assembly of branch (b)

```text
1 - X^9 = (1-X)*(1 + X + ... + X^8),
X^9     = (Y + W_J)^3 = Y^3 + W_J*(3Y^2 + 3Y*W_J + W_J^2),
Y^3     in U^3 subset J[1/(cs*k)]        by (5.1) and (5.4).
```

Hence `1 in J[1/(cs*k)]`.  Clearing denominators with the exponents
recorded above:

```text
term                       cofactor              cs-denom   k-denom
(1-X)*sum_{j<=8} X^j       C * sum X^j             146         54
Y^3 (via B2,B3,B4)         monomial quotients      147         54
3*Y^2*W_J                  3*Y^2*D                 132         45
3*Y  *W_J^2                3*Y*W_J*D               120         36
W_J^3                      W_J^2*D                 108         27
```

so with `A' = 147`, `B' = 54`:

**Certificate (b).**  `cs^147 * k^54 in J = (Ebar_1..Ebar_22)`, with
polynomial cofactors given by the table above.  Applying the *same*
cofactors to the `rho`-carrying rows `E_i` (and using `E_i - Ebar_i in
(rho^2)`) gives, in `S`,

```text
cs^147 * k^54 + rho^2 * H  in  I,     H a polynomial.               (5.5)
```

Note that (5.5) is precisely the V18R1 positive in explicit-cofactor form —
i.e. the mathematical content of V19 — obtained here by hand from the
frozen rows, without Singular, without a standard basis, and without
reading any V18R1/V19 engine output.

## 6. Composition, and the exponents

### 6.1 The identity

Put `A := cs^147*k^54` and `Bq := rho^2*H`, so `A + Bq in I` by (5.5), and
let `Xa := cs^6*k^2*rho^6 in I` by Certificate (a).  Then

```text
cs^6*k^2 * A^3 = cs^6*k^2*(A+Bq)*(A^2 - A*Bq + Bq^2) - H^3 * Xa ,
```

because `(A+Bq)(A^2-A*Bq+Bq^2) = A^3 + Bq^3` and
`Bq^3 = rho^6*H^3 = H^3 * (cs^6*k^2*rho^6)/(cs^6*k^2)`.  Both right-hand
terms lie in `I`.  The left side is

```text
cs^6*k^2 * (cs^147*k^54)^3 = cs^{6+441} * k^{2+162} = cs^447 * k^164,
```

which is (**), hence (*) with `W = 0` after Lemma 0.  Explicitly, the
cofactor of each literal row `f` in (*) is

```text
cs^6*k^2*(A^2 - A*Bq + Bq^2) * (branch-(b) cofactor of f)
   - H^3 * (branch-(a) cofactor of f),
```

and the bilinear / `qrs` cofactors are the corresponding `-sum (row cofactor)
* B_•` combinations of Lemma 0.

### 6.2 What is printed and what is not

Branch (a) is printed in full (§4), in both the substituted and the honest
ordered presentation, and independently expanded.  Branch (b) is printed as
its complete generating data — the seven solved forms (§5.1), the decisive
combination (5.2), and the two reductions (5.3), (5.4) with their cofactor
sizes, denominators and canonical hashes.  The **composite** cofactors of
(*) are not printed: they involve `cs^447`, and the expansion is not a
human-readable object.  They are deterministic given §5.1's rule list and
priority, and every factor entering them was expanded and checked exactly
(§8).  Reviewers wanting byte-level custody of `C` and `D` should recompute
them from §5.1 and compare against the canonical sha256 values above.

### 6.3 Why `N = 447`, and what would shrink it

Three multiplicative costs, in order of impact:

1. **The `9`th power in (5.5).**  `X^3` only reaches `U`, and `U^3` is what
   `B2..B4` kill, so `9` is forced by this rule set.  It contributes
   `X^8`, i.e. `cs^128`.
2. **The cube in §6.1**, forced by `rho^6 = (rho^2)^3` in Certificate (a).
   A branch-(a) element with `rho^2` instead of `rho^6` would give
   `N = A'+6`, `M = B'+2` directly.  Whether `cs^a*k^b*rho^2 in I` holds is
   open; the grade-10 ideal alone does not give it (the surviving obstruction
   is `a0^n*w^n` for all `n`, killed only after one further factor of `p`).
3. **The denominators `cs^16 k^6` in `X`**, inherited from `B1`'s
   `cs^-3 k^-1` and `B7`'s `cs^-1`.

A genuinely small certificate, if one exists, will come from (2), not from
better bookkeeping in (1) or (3).  I did not attempt a minimal-`N` search:
that is a bounded but real Groebner/linear-algebra question and is outside
the local, no-CAS scope I was given.

### 6.4 Geometric content

(**) says exactly: `V(I) intersect D(cs*k) = empty`.  Equivalently, the
scheme-theoretic closure of the registered ordered chart stratum over
`D(cs*k)` is empty, which is strictly stronger than the promoted
special-fibre statement.  It is worth being precise about the gap the
promotion document glosses:

- promoted `sol-20260827` / V18R1 positive: `V(I) ∩ V(rho) ∩ D(cs*k) = ∅`,
  i.e. `(cs*k)^m in I + (rho)`;
- certificate type (2) of the interface theorem: `1 in (I : (cs*k)^inf) +
  (rho)`, i.e. `closure(V(I) ∩ D(cs*k)) ∩ V(rho) = ∅`.

These are **not** equivalent — saturation and adjoining `rho` do not commute
— so the interface theorem's sentence *"chart-fibre emptiness has a
homogeneous power-containment form after clearing a finite saturation
exponent"* is, as written, too quick: clearing a saturation exponent from
`(cs*k)^m = P + rho*G` yields `(cs*k)^m - rho*G in I`, which is of type (2)
only if `(cs*k)^m | G`.  That is exactly the divisibility this prompt asks
about, and it does not follow from emptiness of the `rho=0` fibre.  Here the
gap is closed not by repairing the implication but by §4, which supplies the
missing `rho != 0` half outright.  I flag the interface theorem's converse
clause as **needing a repair or a restriction** independently of this chart.

## 7. What V19's inverse-variable cofactor would have to satisfy

V19 works in `R = Q[u, v, <40 chart names>]` with block order
`(dp(2),dp(40))` and asks Singular for

```text
matrix(ideal(1))*LiftUnit - matrix(RawSpecial)*LiftCertificate = 0,
deg(LiftUnit[1,1]) = 0,   LiftUnit[1,1] != 0,
RawSpecial = ( Ehat_1..Ehat_22, qrs, rho, 1-u*cs, 1-v*k )   (26 generators)
```

so a PASS returns `c in Q^x` and `L_1..L_26 in R` with

```text
c = sum_{i=1}^{22} L_i*Ehat_i + L_23*qrs + L_24*rho
    + L_25*(1-u*cs) + L_26*(1-v*k).                                  (V19)
```

**Clearing `u, v`.**  Let `psi : R -> Q[40 names][1/(cs*k)]` be the
`Q`-algebra map `u |-> cs^-1`, `v |-> k^-1`, identity elsewhere; it is the
quotient by `(1-u*cs, 1-v*k)`.  Applying `psi` annihilates `L_25` and
`L_26` and leaves

```text
c = sum_i psi(L_i)*Ehat_i + psi(L_23)*qrs + psi(L_24)*rho.
```

Let `a := max_{i<=24} deg_u L_i`, `b := max_{i<=24} deg_v L_i`.  Multiplying
by `cs^a*k^b` makes every cofactor polynomial:

```text
c*cs^a*k^b = sum_i Lam_i*Ehat_i + Lam_23*qrs + Lam_24*rho,
Lam_x := cs^a*k^b*psi(L_x)  in  Q[40 names].                        (V19')
```

**(V19') is `cs^a*k^b in I + (rho)` — the V18R1 positive with explicit
cofactors, i.e. exactly branch (b).  It is not, by itself, of the
total-family type.**  To be of the type `cs^N*k^M*(1+rho*W)` one needs the
`rho` term to be `c*cs^a*k^b*rho*(-W)`, i.e.

> **Exact condition.**  `cs^a*k^b` must divide `Lam_24` in `Q[40 names]`.
> Equivalently — and this is the checkable form — `psi(L_24)` must have **no
> negative power of `cs` and no negative power of `k`**: writing
> `L_24 = sum_{alpha,beta} L_24^{(alpha,beta)} * u^alpha * v^beta`, one needs
> `cs^alpha * k^beta | L_24^{(alpha,beta)}` for every `(alpha,beta)`.
> Then `N = a`, `M = b`, `W = psi(L_24)/c`.

Three further points, none of which a raw PASS establishes:

1. **Genericity.**  `lift` returns whatever the standard basis produces; it
   optimises nothing about `L_24`'s `u,v`-adic shape.  There is no reason to
   expect the divisibility, and it must be tested syntactically on the
   returned `lift_unit.matrix` / `unit_certificate.matrix`, not assumed.  The
   frozen V19 acceptance predicate (`LiftResidual==0`, `LiftScalar` a nonzero
   constant, three artifact writes) does **not** test it.
2. **Presentation.**  `Ehat_i` are the *substituted* rows.  Converting
   (V19') into the honest ordered `T-cs` presentation demanded by the
   interface theorem requires exactly Lemma 0's `B_rs, B_c0, B_c1, B_qrs`
   for the 22 rows.  That step is currently unrecorded anywhere in the
   V18/V19 preregistrations.
3. **`rho` is not inverted** in V19's generator list, which is correct and
   is preserved by `psi`; and `cs` appears only as the left-hand power
   `cs^a`, which is the legitimate exceptional-saturation exponent, not an
   inversion.  Those two typing requirements V19 does meet.

**Repair path, in order of preference.**

- (i) If the divisibility test on `psi(L_24)` passes, V19 alone yields
  `cs^a*k^b*(1 + rho*W)` and the type is met at the small exponents `a, b`.
- (ii) If it fails — the expected case — compose (V19') with Certificate (a)
  exactly as in §6.1, giving `cs^{3a+6}*k^{3b+2}` with `W = 0`.  Note this
  only needs V19's `a, b` and cofactors; §5 is then redundant for the
  exact-`Q` lane, and V19's value becomes "supply a smaller `a, b` than
  `147, 54`".
- (iii) Re-preregister the acceptance predicate to include the divisibility
  check, so that a future run cannot be harvested as a total-family
  certificate without it.

Because §5 already derives branch (b) by hand, **V19 is no longer needed for
the mathematics** of (*).  It remains useful for exponent quality and as an
independent machine check, and its protocol artifacts are not replaced by
this report — the same distinction Grok 4.6 drew for the V18R1 negative
control applies verbatim.

## 8. Verification log

Every identity below was checked by exact expansion in `fractions.Fraction`
sparse arithmetic; the second column is an *independent* re-check by a
separately written parser/evaluator that re-reads the frozen `.poly` bytes,
applies the chart at monomial level, and evaluates at random exact rational
points with `cs, k != 0`.

```text
claim                                                   expansion  random pts
Lemma 0, all 22 rows                                       PASS        -
grade-10 core gam/del/alp/bet                              PASS        -
Tg10_5 = (p/2)Tg10_3 - (3/8)p^2 Tg10_1                     PASS        -
branch (a), 9 chain lines                                  PASS        -
branch (a) final, substituted presentation                 PASS      6/6 PASS
branch (a) final, honest ordered presentation              PASS        -
seven solved forms B1..B7                                  PASS        -
B2,B3,B4 have exactly zero tails                           PASS        -
(5.2) decisive combination, 57-term residual in P          PASS        -
(5.3)  1 - X = sum C_i Ebar_i                              PASS      5/5 PASS
(5.4)  phi(X)^3 = sum D_i phi(Ebar_i)                      PASS      5/5 PASS
```

Two independent sanity agreements with the reviewed documents, obtained
after the fact and not used as input: the `Ebar` rows reproduce the
producer's §3.1 display term for term, and `Tg14_5|_{5-zero slice} +
(cs/2)Tg12_2| = -(7/256)cs^5 k` reproduces the promoted constant.

**A residual honesty note on the two reductions.**  (5.3) and (5.4) are
machine reductions, not hand chains: 1880 and (in the `U`-quotient) a
handful of rewrites.  They are deterministic, exact, and each individual
rewrite is one of the seven printed rules, so they are auditable — but they
are not, and I do not claim they are, of the same hand-checkable character
as §4.  §4 alone is fully hand-verifiable.

## 9. Frozen inputs, rehashed before use

Exact-`Q` V9 manifest `86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e`
and the 21 rows:

```text
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
```

V17 exact-`Q` `RESULT.json` `25d40556618983a350eda99d4fb6aae8d1e5cd2cf328041963b46d61729af543`,
`Tg14_5_q.poly` `91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7`.
All 22 matched.  `Tg10_6.poly` and `Tg11_6.poly` are the two-byte file `0\n`.

Local scripts (all pure Python, `fractions` only, no third-party imports;
written under `/tmp`, not committed):

```text
a4bb7098296fded9a31aeed1e02f24646b1a6a482754bea0fd89613c7f2786cd  poly.py
1ebd45568f02d4c813f995cf58ab365fbf559b1e519b934276e453373fba55f5  load.py
d6c8427b7aef43dd79815d341ed6b843efba3f234adaca5952ed807fc3204612  cert.py
ac53199f3599d44789dd2ad3d5ffc9ee0304e6415e41511d512a469d23924a7b  bar.py
94ff6955706d7c0a895b8edddbbfc7a3957edb1250024dcdeb47eafca10b0c4c  bfast.py
```

## 10. Method, and what was not done

Method: exact sparse `Q` arithmetic on the frozen bytes; staged exact
division for Lemma 0; a hand-derived nine-line triangular chain for branch
(a); a hand-chosen seven-rule directed rewriting for branch (b), with every
rule carrying and every derived element verified against its own cofactor
vector.

Not done, per instruction and per honesty:

- **no Groebner or standard basis**, no `S`-polynomials, no ideal
  intersection, quotient or saturation routine, no elimination, no Singular,
  no third-party CAS;
- no AWS read or mutation, no campaign launch, no `jc2-lean` access, no web;
- no re-extraction or independent confirmation of the V9/V17 coefficients;
- no reading of any V18R1 or V19 engine output, log, artifact or validator
  result;
- **no minimality claim** for `N = 447`, `M = 164`;
- no attempt at the `F65521` lane.  Branch (a) inverts only `2, 3, 5` and
  transfers verbatim; branch (b)'s rules invert `2, 3, 5` and the variables
  `cs, k`, so it also transfers, but I did not run the modular check and do
  not assert it.

One thing was attempted and **failed**, and is recorded because it is
informative: a single unified rewriting system that eliminates `rho^2` via
`Tg10_1` (so that `p in (qc0,qc1)` is used directly) **diverges** — the
`qc`-degree regresses upward through the free variable `a1`, term count
growing linearly without bound.  The two-branch split of §4/§5 is not a
stylistic choice; the naive unified reduction does not terminate.

## 11. Scope firewall

Established here, and only this:

> On the frozen V9/V17 exact-`Q` bytes, `cs^447 * k^164 * (1 + rho*0)` lies
> in `(Tg10_1..Tg12_7, Tg14_5, rs-cs*qrs, c0-cs*qc0, c1-cs*qc1, qrs)`, by an
> exact polynomial identity that inverts neither `cs` nor `rho` and localizes
> only at `k`.  Equivalently the registered ordered `T-cs` chart stratum is
> empty over `D(cs*k)`, its `rho != 0` half for a grade-10 reason.

Not established, and explicitly not inferred:

- the full `T-cs` chart: `k = 0` is untouched and remains a live residual
  stratum, now carrying weight `k^164`;
- Gate `T`, order two, the `(8,12)` frontier, maximum twelve, JC2;
- the later ordered charts `T-c0`, `T-c1`, either second-stage `A` chart,
  chart overlaps, the terminal all-zero receiver, the deck/square bridge, the
  generic comparison, or any effective bound on the decisive source grade;
- any statement about TD6, the prime-ray lane, AS109, or any Lean
  formalization;
- any validator PASS: this report harvests nothing, and in particular does
  not convert V18R1 or V19 into a recorded result.  Whether V19 should still
  run is a protocol decision (§7), not a mathematical one;
- independence from the frozen V9/V17 bytes.  The entire report is
  conditional on them and inherits their upstream literal-source provenance
  debt in full, exactly as recorded by the producer report, the Grok hostile
  review, and the grade-14 fibre promotion.

The only repository file written is this one.
