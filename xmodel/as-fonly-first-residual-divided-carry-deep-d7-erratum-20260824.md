# Erratum and replacement: the divided-linear first residual at `p=3,D=7`

**Producer verdict: THE QUADRATIC FIRST-CARRY BRACKET HAS UNIVERSALLY ZERO
BASIC CARTIER COEFFICIENT, BUT IT IS NOT THE FULL FIRST RESIDUAL.  THE
SOURCE-HONEST RESIDUAL CONTRIBUTES THE ADDITIONAL ROW
`u5_3+v5_2=0`.  ON THE DEEP `D=7` BRANCH THE CORRECT IDEAL HAS 40
VARIABLES AND 30 ROWS AND ADMITS THE EXACT THREE-PIECE NONREDUCED COVER
RECORDED BELOW.**

- Date: 2026-08-24
- Prime/cap: `p=3`, map-only total-degree cap 7
- Status: exact producer; hostile different-model review pending
- Supersedes and quarantines producer report SHA-256
  `b0ee40acf7e1df81574d0a41f0338df86b124cae475ad56bbf4e464b481a27f7`
  and freeze SHA-256
  `ef500fa54af3cb8070ccfb991cb9ae9d09772177e3ae427199ac87be3b31a071`
- The quarantined bytes were not mutated.

## 1. Source-honest integer expansion

Let

```text
P_0=x-x^3,                 Q_0=y,
P=P_0+3U,                  Q=Q_0+3V.
```

Direct expansion over the integers gives

```text
det J(P,Q)-1 = 3L+9K,                              (1)
L=U_x+V_y-x^2,
K=(U_x-x^2)V_y-U_yV_x.
```

The first digit is admissible modulo nine exactly when `L=0 mod 3`.
After adjoining the next bounded digit

```text
P_new=P+9C,                 Q_new=Q+9D,
```

division of the integer determinant by nine and reduction modulo three
gives the actual extension equation

```text
L/3 + K + C_x+D_y = 0.                            (2)
```

The quarantined producer used only `K+C_x+D_y` and omitted `L/3`.

## 2. The exact Cartier row

For every prime `p`, a monomial pair contributing to
`x^(p-1)y^(p-1)` in the bracket `{U,V}` has exponents

```text
a+c=p,                 b+d=p,
```

and multiplier

```text
ad-bc=a(p-b)-b(p-a)=p(a-b)=0 mod p.               (3)
```

The seed term `-x^(p-1)V_y` also contributes zero there because it would
differentiate `y^p`.  Thus the old universal statement

```text
[x^(p-1)y^(p-1)]K=0                               (4)
```

is correct, but (4) concerns only the quadratic bracket.

In the full residual (2), the same coefficient of `L/p` is

```text
u_(p,p-1)+v_(p-1,p).                              (5)
```

At `p=3,D=7`, (5) is the source-derived linear row

```text
ell = u5_3+v5_2 = 0.                              (6)
```

There are no other sources for this coefficient.  The derivative factors
are exactly three, so (6) follows before any clearing, radicalization, or
component split.

## 3. Negative control: the omission changes acceptance

Take integer representatives

```text
U=x^3y^2,                  V=x^2y.
```

Modulo three these satisfy `U_x+V_y=x^2`.  Their quadratic carry is

```text
K=2x^4+2x^4y^2 mod 3,
```

so every old divergence and degree-eight/degree-seven cap-boundary row
vanishes, and the quadratic Cartier coefficient is zero.  Nevertheless,
direct integer expansion gives

```text
det J(x-x^3+3U, y+3V)-1
  = -9x^4+9x^2y^2-9x^4y^2.                       (7)
```

Thus the full residual has `[x^2y^2]=1 mod 3`.  No bounded divergence
`C_x+D_y` can cancel that Cartier class.  Equation (7) is an explicit
source-honest witness that the omitted row matters.

## 4. Corrected 30-row ideal

Use the same deep branch as the quarantined calculation:

```text
U_7=V_7=0,
U_6,V_6 are degree-six Frobenius polynomials,
all coefficients of U,V in degrees 1,...,5 are retained.
```

The six degree-six Frobenius coefficients do not enter the cap-boundary or
basic Cartier obstruction and remain a free factor.  On the 40 displayed
lower variables the corrected ideal `I` contains:

- 14 nonzero first-divergence rows;
- 9 quadratic-carry rows in degree eight;
- 6 nonzero quadratic-carry rows in degree seven;
- the divided-linear Cartier row (6).

Exact Singular computation gives

```text
variables                          40
rows                               30
reduced Groebner basis size       269
dimension                          18
radical Groebner basis size        44
I radical?                         no
```

No minimal-prime or primary-decomposition claim is made here.

## 5. Exact nonreduced three-piece cover

Let `q4` be the explicit quartic printed by the generator, inherited only as
a localization separator from the earlier associated-top calculation.  Set

```text
Q0 = I : q4^infinity,
B  = I + (q4^2),
Q1 = B : u5_0^infinity,
E  = B + (u5_0^2).
```

The replay computes every ideal from the original 30-row `I` and verifies
both containment directions for

```text
I = Q0 intersect B,
I = Q0 intersect Q1 intersect E.                 (8)
```

The four remainder ideals in the two-sided tests all have size zero.  The
piece statistics are

```text
dim(Q0), GB size(Q0) = 18, 150,
dim(Q1), GB size(Q1) = 18, 169,
dim(E),  GB size(E)  = 17, 3277.
```

Equation (8) is an equality of the original nonreduced ideal.  The pieces
are localization aids only: this producer does **not** claim that `Q0`,
`Q1`, or `E` is primary, nor that they are the minimal components.  In
particular the large supported remainder `E` is retained and is load-bearing
for any successor calculation.

## 6. Preservation and retraction ledger

| Earlier statement | Status after source audit |
|---|---|
| Universal vanishing of the basic Cartier coefficient of `K` | Preserved, with scope narrowed to the quadratic bracket |
| Degree-eight and degree-seven cap-boundary rows | Preserved: `L/3` has degree at most four on the displayed lower layers and at most five including the free degree-six Frobenius layer |
| The separately reviewed associated-top degree-12/11 gate | Preserved; the divided-linear term cannot reach those degrees |
| Six derivative-invisible degree-six Frobenius parameters | Preserved as a free acceptance factor |
| `K` is the full first residual | Retracted; equation (2) is the replacement |
| The 29-row ideal completely characterizes acceptance | Retracted and replaced by the 30-row ideal |
| Old dimension 19 and old minimal/saturation component statistics | Retracted for the corrected gate |
| Old two-piece saturation equality | Retracted; it fails after adjoining (6), and (8) replaces it |

## 7. Scope and next gate

This producer exactly corrects first-digit acceptance only on the aligned
deep branch above.  It does not classify an accepted second digit, impose
the following integer carry, cover the other associated-top branches, empty
the full `D=7` locus, or imply an all-depth, characteristic-zero, no-lift,
counterexample, or JC2 statement.

Successor work must start from the original corrected ideal `I`.  The three
pieces in (8) may guide localization, but none may replace `I`; the next
degree-ten and accepted-digit rows must be checked against their intersection.

## 8. Replay

From the replacement case directory:

```sh
python3 replay_divided_linear_carry.py
Singular -q audit_divided_linear_carry.sing
python3 generate_corrected_deep_branch_gate.py | Singular -q
COVER=1 python3 generate_corrected_deep_branch_gate.py | Singular -q
RADICAL=1 python3 generate_corrected_deep_branch_gate.py | Singular -q
shasum -a 256 -c MANIFEST.sha256
```

The first two commands independently reconstruct (7).  The cover replay
generates the ideal from coefficient arithmetic, computes all three pieces,
and exits nonzero unless both two-sided equalities in (8) hold.
