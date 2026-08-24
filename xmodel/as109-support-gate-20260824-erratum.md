# Erratum — AS109 base-109 carry at the first nonlinear successor

**Verdict: `SCOPED-CORRECTION`; the `NO-FROZEN-GRAMMAR` stop survives.**

- Round: `20260824T0719Z-c17bd25`
- Prime/seed: `p=109`, `(x-x^109,y)`
- Enumeration: **not run**
- Existence or nonexistence inference: **none**
- Canonical ledgers: not edited

This note preserves the frozen producer and different-model review byte for
byte. It corrects one generic digit-lift statement while leaving the actual
parametric obstruction, Hensel lemma, and closed-support contraction
criterion intact.

## 1. Frozen trust boundary

| Artifact | SHA-256 |
|---|---|
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` |
| `cases/as109_support_20260824/PREREGISTRATION.md` | `be9138a90b661f069197a4c22235ee1caa4e03fcecd2dab8c980e8934f2d6301` |
| `cases/as109_support_20260824/manifest.json` | `c69d70805bdba5793f385fca9c289f9a12a8c58c45e1625e1c2f69a9632f0364` |
| `cases/as109_support_20260824/FREEZE.sha256` | `0a535ca2877ec3672044faa5c5f20878c4b95adddf4087b89f772d030d6e140e` |
| `cases/as109_support_20260824/verify_spec_obstruction.py` | `1bb8f86596b75bd43e467dc84b569e8fb2bb2744c198c40f5244f0b054634165` |
| `cases/as109_support_20260824/spec_obstruction.json` | `b95ad244da3ea75100c61143dc9c0026ac567c8acfc2398a86ce1623a101131e` |
| `cases/as109_support_20260824/verify_carry_erratum.py` | `cde7f3d467b492c0d914511b7fa609c916e40a33e6ca6c741af9be79a99d53f0` |

This erratum **overrides claim 2 only** in
`xmodel/as109-support-review-grok-20260824.md`. In that claim, the displayed
determinant expansion, bracket formula, and definition of `N` are correct,
but the assertion that the two displayed equations over `F_109` are by
themselves the exact condition modulo `109^3` omits a base-109 carry. Claims
1 and 3--8 of that review are unchanged. In particular, claims 3 and 4 use a
family whose carry is integrally zero.

The generic `E2` and marked-collision assertions in the producer,
preregistration, manifest, and review are quarantined unless either the
carry-aware equations below are used or the relevant first-layer equality
holds over `Z`, not merely modulo 109.

## 2. Carry-aware determinant equations

Put `p=109`, `s=x^108`, and take fixed integral coefficient lifts

```text
P=x-x^p+p A_0+p^2 A_1,
Q=y      +p B_0+p^2 B_1                 modulo p^3.
```

Define

```text
L(A,B)=A_x+B_y,
C_1=L(A_0,B_0)-s,
N_0=(A_0x-s)B_0y-A_0y B_0x.
```

Direct expansion over `Z[x,y]` gives

```text
det J(P,Q)-1
 =p C_1+p^2(L(A_1,B_1)+N_0)             modulo p^3.       (2.1)
```

The first digit requires `C_1=0 mod p`. After that, write
`K=C_1/p`. The correct second digit is

```text
K+L(A_1,B_1)+N_0=0 mod p.                                (2.2)
```

The producer's uncarried `E2` is valid when `C_1=0` integrally. It is not a
generic consequence of `E1` over `F_109`.

There is an analogous evaluation carry. For
`Delta H=H(1,0)-H(0,0)`, preservation of the marked collision modulo `p^3`
requires

```text
Delta A_0=0 mod p,
Delta A_0/p+Delta A_1=0 mod p,

Delta B_0=0 mod p,
Delta B_0/p+Delta B_1=0 mod p.                            (2.3)
```

Thus separate equations `Delta A_i=Delta B_i=0 mod p` do not generically
control the carry. Exact integral vanishing at each marked layer is
sufficient.

## 3. Five-slot countercontrol

Let

```text
A_0=x^109-x,
B_0=(1+x^108)y,
A_1=0,
B_1=(1+2x^108+x^216)y.
```

There are five labeled correction slots across the two layers:

```text
P: (109,0), (1,0),
Q: (0,1), (108,1), (216,1).
```

All four correction polynomials have exact marked difference zero. Writing
again `s=x^108`, exact calculation gives

```text
C_1=p s,
K=s,
N_0=-1+107s+108s^2,
L(A_1,B_1)=1+2s+s^2,
L(A_1,B_1)+N_0=p(s+s^2).
```

Consequently the frozen uncarried `E1` and `E2` both pass over `F_109`, but
the corrected second residual is `K=s`, and

```text
det J(P,Q)-1 = p^2 x^108 mod p^3 != 0.                    (3.1)
```

This is a countercontrol to the generic digit test, not a candidate Keller
map and not an enumeration result.

## 4. Why the registered stop survives

For every integer `m>=1`, the producer's obstruction family is

```text
A_0=y^m,
B_0=x^108 y.
```

Here

```text
C_1=A_0x+B_0y-x^108=0
```

**integrally**, so `K=0`. Its exact nonlinear source is

```text
N_0=-x^216-m*108*x^107 y^m over Z,
   =-x^216+(m mod 109)x^107 y^m over F_109.
```

For the transported successor

```text
A_1=-x^108 y^m,
B_1=x^216 y+108x^107 y^(m+1),
```

one has `L(A_1,B_1)+N_0=0` integrally. Every displayed correction also
vanishes identically on `y=0`, so there is no marked-evaluation carry. The
two-slot unbounded first layer, exact triangular source gauge, three new
transported slots, and failure of a literal same-slot cycle therefore remain
correct.

It follows that the registered procedural verdict remains
`NO-FROZEN-GRAMMAR`: a cap on the number of slots does not bound literal
exponents, and no finite exhaustive gauge normal form with successor
transport was proved. This remains only a specification stop. It proves
neither existence nor nonexistence of a cap-eight lift.

The Hensel lemma is independent of the digit bookkeeping: it assumes an
already exact `Z_109` polynomial map with determinant one. The
`CLOSED-SUPPORT + UNIT-L` criterion is also unchanged because it uses the
packed exact equation

```text
det J(x-x^p+pA, y+pB)-1
 =p(L(A,B)-s+p N(A,B)),
```

with full `Z_109` coefficients rather than separately chosen residue digits.
No closed support was found, so these remain conditional resurrection
lemmas and provide no counterexample.

## 5. Standalone exact replay

Run:

```text
python3 cases/as109_support_20260824/verify_carry_erratum.py
```

The replay imports no producer code. It checks every frozen hash above, the
five-slot determinant directly over integer sparse polynomials, the corrected
carry and collision equations, the parametric zero-carry identities at six
representative exponents, and the two closed-support controls. Expected
top-level fields are

```text
verdict = PASS-CARRY-ERRATUM
generic_E2_without_carry = QUARANTINED
no_enumeration_run = true
existence_inference = false
```

No statement in this erratum proves or disproves JC2.
