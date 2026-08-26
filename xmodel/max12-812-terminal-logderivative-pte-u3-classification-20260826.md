# `(8,12)` terminal maps as weighted moment configurations; complete `U=3`

Date: 2026-08-26  
Status: **PRODUCER COROLLARY; FROZEN FOR HOSTILE REVIEW**

## Charged theorem

This note consumes only the independently confirmed terminal extremal-abc
classification:

```text
149691f1784ffccea9473a63efaec4a7d0eea56f9c1e1ba267610b104022920e
  xmodel/max12-812-nontrivial-terminal-extremal-abc-classification-20260826.md
b9cf307094a3128ae459714d6a84e49d4f004308d97b5d5b8298afb1e300b149
  xmodel/max12-812-nontrivial-terminal-extremal-abc-review-grok-20260826.md
```

Work over an algebraic closure of a characteristic-zero field after the
already licensed finite constant extension.  Let `m in {2,4}` be the exact
Kummer order.  The charged theorem gives `U>=2`, coprime monic polynomials
`A,B` of a common degree `D`,

```text
T=A/B,       G=A-B,       P=rad(A) rad(B),       deg P=U,
W=A'B-AB'=kappa A B/P,       kappa!=0.                       (0.1)
```

The zeros of `A` have multiplicities `alpha_i<=m`; the zeros of `B` have
multiplicities `beta_j>=1`; and exact Kummer order is equivalent to

```text
gcd(m, all alpha_i, all beta_j)=1.                              (0.2)
```

## Theorem 1 — logarithmic derivative / weighted Prouhet form

Let the `U` distinct roots of `P` be `c_1,...,c_U`.  Give them signed
nonzero integer weights

```text
n_i= alpha_i       when c_i is a zero of A,
n_i=-beta_i        when c_i is a zero of B.                     (1.1)
```

Then

```text
T'/T = kappa/P = sum_i n_i/(x-c_i),                             (1.2)
```

and the support is exactly a weighted Prouhet--Tarry--Escott configuration:

```text
sum_i n_i c_i^k = 0                 for 0<=k<=U-2,              (1.3)
kappa = sum_i n_i c_i^(U-1) != 0.                               (1.4)
```

Equivalently,

```text
P'(c_i)=kappa/n_i                  for every i.                  (1.5)
```

Conversely, take `U>=2` distinct points `c_i` and nonzero signed integer
weights `n_i` satisfying (1.3), with positive weights at most `m`, and put

```text
A=product_(n_i>0) (x-c_i)^n_i,
B=product_(n_i<0) (x-c_i)^(-n_i).                               (1.6)
```

Then `A` and `B` are coprime monic polynomials of the same degree `D`,
`T=A/B` has (1.2), and

```text
deg(A-B)=D-U+1,       A-B is squarefree.                         (1.7)
```

Thus the moment data recover precisely the terminal extremal-abc triple.
If (0.2) also holds, the charged radicand formula gives an exact order-`m`
terminal solution.  This converse is only for the terminal differential
equation.

### Proof

Divide the Wronskian identity in (0.1) by `A B`:

```text
T'/T=A'/A-B'/B=W/(AB)=kappa/P.
```

The partial-fraction residues of `A'/A-B'/B` are exactly (1.1), proving
(1.2).  Expanding at infinity gives

```text
sum_i n_i/(x-c_i)
  = sum_(k>=0) (sum_i n_i c_i^k) x^(-k-1),
kappa/P = kappa x^(-U)+O(x^(-U-1)).                             (1.8)
```

Comparison proves (1.3)--(1.4).  Taking the residue of `kappa/P` at `c_i`
proves (1.5).

Conversely, the `k=0` equation says that the total positive and negative
weights agree, so the two polynomials in (1.6) are monic of the same degree.
The common-denominator numerator of `sum_i n_i/(x-c_i)` has degree at most
`U-1`.  Equations (1.3) say that its expansion at infinity begins in degree
`x^(-U)`; hence that numerator is the nonzero constant (1.4), proving
(1.2).

Since `A,B` are monic of equal degree, `T(infinity)=1`.  Integrating (1.8)
at infinity gives

```text
log T = -kappa/(U-1) x^(-(U-1))+O(x^(-U)),
T-1   = -kappa/(U-1) x^(-(U-1))+O(x^(-U)).                      (1.9)
```

Therefore `G=A-B=B(T-1)` has exact degree `D-U+1`.  At any finite zero of
`G`, neither `A`, `B`, nor `P` vanishes, and (1.2) gives `T'!=0`; hence that
zero of `G` is simple.  This proves (1.7).  Finally

```text
W=AB T'/T=kappa AB/P,
```

so all hypotheses of the charged converse are recovered.  QED.

## Theorem 2 — complete `U=3` terminal list

For `U=3`, every signed multiplicity profile has one and only one support up
to an affine change of `x` and permutations among equal-sign points.

There are two forms.

### Two zeros and one pole

For positive integers `a,b`, with `a,b<=m`, take signed weights
`(a,b,-a-b)`.  After putting the zero points at `0,1`, the `k=1` moment
forces the pole to be

```text
t=b/(a+b),
T_(a,b)(x) = x^a (x-1)^b/(x-t)^(a+b).                           (2.1)
```

The unordered pair `{a,b}` determines the affine class.  It is exact iff
`gcd(m,a,b)=1`.

### One zero and two poles

For positive integers `b,c`, with `b+c<=m`, take signed weights
`(b+c,-b,-c)`.  After putting the zero at `0` and the first pole at `1`, the
second pole is

```text
t=-b/c,
S_(b,c)(x) = x^(b+c)/((x-1)^b (x+b/c)^c).                       (2.2)
```

The unordered pair `{b,c}` determines the affine class.  It is exact iff
`gcd(m,b,c)=1`.

These lists are exhaustive because the only moment equations for `U=3` are
`sum n_i=0` and `sum n_i c_i=0`.  In both displays the three support points
are distinct in characteristic zero, and the moment of degree two is
nonzero, so no degenerate case was added.

## Explicit exact lists

The profile in the last column records the positive multiplicities of the
minimal radicand `d`; an exponent zero is written as “uncharged zero” rather
than included in the profile.

### Order two (`m=2`): exactly three affine terminal classes

| sign type | weights | `D` | minimal-radicand profile |
|---|---:|---:|---:|
| two zeros / one pole | `(1,1|-2)` | 2 | `[4,1,1]` |
| two zeros / one pole | `(1,2|-3)` | 3 | `[5,1]` plus one uncharged double zero |
| one zero / two poles | `(2|-1,-1)` | 2 | `[3,3]` plus one uncharged double zero |

The omitted profile `(2,2|-4)` has gcd two and belongs to the trivial
Kummer class, not the exact order-two leaf.

### Order four (`m=4`): exactly ten affine terminal classes

| sign type | weights | `D` | minimal-radicand profile |
|---|---:|---:|---:|
| two zeros / one pole | `(1,1|-2)` | 2 | `[6,3,3]` |
| two zeros / one pole | `(1,2|-3)` | 3 | `[7,3,2]` |
| two zeros / one pole | `(1,3|-4)` | 4 | `[8,3,1]` |
| two zeros / one pole | `(1,4|-5)` | 5 | `[9,3]` plus one uncharged fourth-order zero |
| two zeros / one pole | `(2,3|-5)` | 5 | `[9,2,1]` |
| two zeros / one pole | `(3,3|-6)` | 6 | `[10,1,1]` |
| two zeros / one pole | `(3,4|-7)` | 7 | `[11,1]` plus one uncharged fourth-order zero |
| one zero / two poles | `(2|-1,-1)` | 2 | `[5,5,2]` |
| one zero / two poles | `(3|-1,-2)` | 3 | `[6,5,1]` |
| one zero / two poles | `(4|-1,-3)` | 4 | `[7,5]` plus one uncharged fourth-order zero |

The omitted two-zero pairs `(2,2)`, `(2,4)`, `(4,4)` and the one-zero pair
`(2,2)` fail the gcd-four exactness test.

## Computational consequence

For fixed `U`, (1.3) is a finite exact system after affine normalization:
there are finitely many signed integer profiles because
`U-1<=D<=m(U-1)`, and each profile has `U-2` support variables and `U-2`
moment equations.  It is therefore a smaller and source-transparent frontend
for enumerating terminal clients than unrestricted coefficients of `A,B`.
For `U=3`, no CAS is needed; the thirteen displayed clients can be compiled
directly into the remaining six Faber tails and both Taylor boundary gates.

## Scope firewall

This note proves an exact reformulation and the complete `U=3` list for the
terminal differential equation only.  It does **not** prove that any listed
map satisfies another Faber tail, admits Taylor polynomialization, produces a
Keller pair, survives the coefficient-infinity boundary, closes an entire
Kummer leaf, closes `(8,12)`, bounds all `U`, or proves/disproves JC2.
