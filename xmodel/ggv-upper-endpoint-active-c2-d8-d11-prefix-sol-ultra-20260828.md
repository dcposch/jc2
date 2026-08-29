# Deep active-`c2` prefix after the D9 repair: exact D8--D11 factors

Date: 2026-08-28  
Author: Sol Ultra  
Status: **EXACT PROVISIONAL DISCOVERY / AWAITING HOSTILE REVIEW**

## Verdict

On the deep component `A|V0` with scalar `c2 != 0`, the complete
characteristic recurrence has a short rootwise cascade after the provisional
D9 repair `A|T`.  Two D8 lifts and one D9/D10 product repair reduce the live
data to a single residual factor by D10.  The deepest D11 class retains that
factor and does not yet close the component.

This is a necessary characteristic-polynomiality theorem at
characteristic-zero field points.  It is not yet independently reviewed and
does not prove raw-window existence or emptiness, scheme divisibility, a
complete branch-P exclusion, or JC2.

Exact checker:

`xmodel/ggv-upper-endpoint-active-c2-d8-d11-prefix-sol-ultra-20260828-check.py`

## 1. Setup and dependencies

Use the reviewed reduced prefix

```text
F0=A^4,
F1=A^2 V0,
F2=(V0^2+A^2 Z)/4,
F3=(V0 Z+A T)/8,
```

with squarefree quartic `A` over a characteristic-zero field and the complete
characteristic continuation

```text
G = F^(3/2) + sum_(m=2,4,...,20) c_m t^m F^((12-m)/8).
```

Assume the deep branch `V0=A S`, the genuine open `c2 != 0`, and the
provisional D9 repair `T=A U`.  No q1 representation is used below.  On the
q1 locus one may later specialize `S=3 lambda A'`, but none of the identities
depends on that specialization.

The checker pins the frozen general-prefix recurrence implementation at SHA

```text
fceb189badafad877c1142b8925480516111790707954d2000421b8190fde119
```

and reconstructs every mode through weight 11.  Reusing that recurrence is a
source dependency, not a different-model hostile review.

## 2. D8 gives two successive lifts

Put

```text
K = 64 F4-Z^2.
```

After `V0=A S` and `T=A U`, the complete deepest D8 polar class is

```text
g8[-2] = 3 K^2/(32768 A^2).
```

Thus field-radical polynomiality and squarefreeness give `A|K`; write

```text
K=A R.
```

After this lift the *entire* remaining D8 polar part is

```text
g8^- = -5 c2 (S^2-2Z)^3/(65536 A).
```

Because `c2` is a nonzero scalar on the active open, D8 gives the second
field-radical lift

```text
S^2-2Z=A Q.                                             (A8)
```

This second conclusion is not licensed on the `c2=0` deep sublocus; that
sublocus must remain separate.

## 3. D9 product and D10 repair

Define

```text
D = R-4 S U,
P = 256 F5-R S+2 S^2 U.
```

After the two D8 lifts, the complete D9 polar part factors exactly as

```text
g9^- = 3 D P/(65536 A).                                 (A9)
```

Hence D9 polynomiality gives `A|DP`.  The deepest D10 class is independently
reconstructed from the full recurrence as

```text
g10[-2] = 3 P(P-2 S D)/(524288 A^2).                    (A10)
```

At any root of squarefree `A`, equation (A9) says `D P=0`.  If `P=0` there is
nothing to prove; if `D=0`, (A10) becomes `P^2=0`.  Thus in both cases
`P=0`.  Rootwise over a field and then by squarefreeness,

```text
D9=D10=0  ==>  A | P
             = 256F5-RS+2S^2U                         (A10-repair)
```

on this active open.  This deletes the tempting `D=0` alternative at the
deepest D10 order, even though `D` reappears in the lower D10 class.

## 4. First residual after writing `P=A P1`

Set `P=A P1` and define

```text
Q2 = 2048 F6-2 S P1+Q(R-8 S U)-8U^2.
```

Every D9 pole disappears.  The complete remaining D10 polar part is

```text
g10^- = D[20 c2 D+3 Q2]/(524288 A).                     (A10r)
```

The deepest D11 class is

```text
g11[-2] = D B11/(1048576 A^2),                          (A11)

B11 = -10 c2 S D -3072 F6 S +3 P1 S^2
      -3 Q S(R-6 S U)-6 U(R-6 S U).
```

Consequently the branch `D=0 mod A` survives both (A10r) and the deepest
D11 equation.  Subleading D11 terms and later rows may still kill it, but no
such conclusion is claimed here.  This is now the smallest exact successor
on the active-`c2` locus.

## 5. Exact checks and mutations

The standard-library checker:

1. pins and loads the complete frozen recurrence through D11;
2. reconstructs the D8 square, D8 cubic, D9 product, D10 product repair,
   residual D10 factor, and deepest D11 factor coefficient by coefficient;
3. checks both D9 root branches with exact rational scalars;
4. confirms that the `D=0,P!=0` branch passes D9 but fails the deepest D10
   class, while the `P=0` branch passes both;
5. rejects mutations replacing the D8 square or cube, dropping the D9 `D`
   factor, or replacing the D10 product by `P^2`.

Replay:

```bash
python3 -B xmodel/ggv-upper-endpoint-active-c2-d8-d11-prefix-sol-ultra-20260828-check.py
```

Expected terminal marker:

```text
PASS_EXACT_ACTIVE_C2_D8_D11_PREFIX
```

## 6. Scope and next discriminator

Promotable only after independent reconstruction:

- the two D8 field-radical lifts on `c2 != 0`;
- the exact D9/D10 product repair `A|P`;
- the residual D10 and deepest D11 factors.

Not claimed:

- any statement on the `c2=0,A|V0` sublocus;
- q1, D23, or a parameterized-`A` raw compiler;
- satisfaction of literal raw coefficient windows by a point;
- disappearance of the `D=0` residual branch;
- endpoint, branch-P, Keller, or JC2 emptiness.

The cheapest next calculation is to impose `D=0` and `P=A P1` in the full
D11/D12 recurrence, retain all subleading `c2,c6` classes, and determine the
first row that either kills this residual or produces a window-respecting
survivor.  This should remain desk work until a frozen finite raw ideal is
identified.
