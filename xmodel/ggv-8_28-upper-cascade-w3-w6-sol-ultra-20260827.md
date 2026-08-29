# Exact upper-face lower cascade through weights 3--6

Date: 2026-08-27  
Author: Sol Ultra  
Status: **EXACT DESK PRODUCER / AWAITING DIFFERENT-MODEL HOSTILE REVIEW**

## Verdict

The lower raw cascade through `D6` has a complete, small parametrization on
both squarefree degree-eight endpoint shapes.  No Groebner elimination is
needed.

Write `F0=H^2`, `G0=H^3`, and use the frozen D3 windows.  Then:

```text
P: H=A^2, deg A=4, A monic squarefree

   F1 = H V,                         deg V <= 7,
   F2 = (V^2 + H Z)/4,               deg Z <= 6,
   F3 = (V Z + A T)/8,               deg T <= 9,
   F4,F5,F6 arbitrary in their raw windows,
   c4,c6 arbitrary,
   c2=0 or A|V.

Q: H=A^2 B, deg A=3, deg B=2, A,B squarefree and coprime

   F1 = H V,                         deg V <= 7,
   F2 = (V^2 + H Z)/4,               deg Z <= 6,
   F3 = (V Z + A B T)/8,             deg T <= 8,
   F4,F5,F6 arbitrary in their raw windows,
   c4 arbitrary.
```

Here `c2,c4,c6` are exactly the polynomial homogeneous modes on P at
weights `2,4,6`; Q has only `c4` through weight six.  These conditions are
necessary and sufficient for polynomial raw coefficients satisfying
`D1=...=D6=0`.

The decisive strategic answer is negative: **the vanishing cascade does not
imply the q1 image gate.**  For any `V` of degree at most seven,

```text
U=H+(V/2)t,       F=U^2,       G=U^3
```

fits every frozen upper window and has `E(F,G)=0` identically.  Taking
`V=1`, hence `F1=H`, is outside the q1 image on both an exact P fixture and
an actual norm-survivor Q fixture.  This separator has `D22=0`, not `1`:
it settles the rows-1--14 implication question but says nothing about the
affine endpoint-normalized system or row `D23`.

## 1. Inputs, custody, and scope

The only mathematical input is the promoted D5G coefficient recurrence

```text
D_n = sum_(i+j=n) ((12-j) F_i' G_j + (i-8) F_i G_j').       (1.1)
```

The D3 windows used through weight six are

```text
deg F_n <= 16-n,       deg G_n <= 24-n,       n=1,...,6,
```

with lower degree zero.  Explicitly, every slot is retained:

| `n` | raw `F_n` window | dimension | raw `G_n` window | dimension |
|---:|---|---:|---|---:|
| 1 | `0..15` | 16 | `0..23` | 24 |
| 2 | `0..14` | 15 | `0..22` | 23 |
| 3 | `0..13` | 14 | `0..21` | 22 |
| 4 | `0..12` | 13 | `0..20` | 21 |
| 5 | `0..11` | 12 | `0..19` | 20 |
| 6 | `0..10` | 11 | `0..18` | 19 |

The P and Q factor shapes are treated as hypotheses;
the proof itself does not use the endpoint norm equation except that the Q
negative control below is chosen from it.

The Opus reviewer formulas motivating this successor were treated as
**provisional**.  Every identity below was rederived from (1.1) and the
characteristic modes.  No canonical ledger was edited, no AWS or heavy local
algebra was used, and `jc2-lean` was not read or touched.

## 2. Exact triangular architecture

Put

```text
R_n = G_n-(3/2)H F_n.
```

The same-weight operator is

```text
L_n(R)=2H((12-n)H'R-4HR'),
ker L_n = < H^((12-n)/4) > in K(X).                         (2.1)
```

For fixed `F`, (1.1) is linear in `G`, and direct substitution gives

```text
E(F,t^m F^((12-m)/8))=0.
```

Induction on the row therefore proves the complete truncated form

```text
G = F^(3/2) + sum_m c_m t^m F^((12-m)/8)  mod t^(N+1),     (2.2)
```

where the sum contains precisely those kernels whose coefficient is a raw
polynomial.  Through six these are `m=2,4,6` on P and `m=4` on Q.  Thus a
row is solvable exactly when the next coefficient of (2.2) is polynomial
and lies in its raw window.  This proves completeness, rather than merely
constructing one family of solutions.

The raw upper bound is automatic.  A term in the `F^(3/2)` coefficient at
weight `n` containing `k` positive coefficients has degree at most

```text
24 + sum_r(16-i_r) - 16k = 24-n.
```

The other modes lie strictly inside the same bound.  Since `n<=6`, there is
no positive lower-degree cutoff.

## 3. Rows two and three: `F1` becomes an `H`-multiple

Row one is unique:

```text
G1=(3/2)H F1.
```

Row two gives the already-audited exact gate

```text
H | F1^2.                                                   (3.1)
```

Thus `F1=A U` on P and `F1=AB U` on Q.  In either branch, the non-mode part
of `R3` is

```text
U(12A^2 F2-U^2)/(16A^3).                                   (3.2)
```

The P `c2` contribution is the polynomial `(5/4)c2 A^2U`; Q has no
weight-two kernel.  Because `A` is squarefree, (3.2) is polynomial if and
only if `A|U`.  Hence the **necessary-and-sufficient row-three gate** is

```text
F1=H V,       deg V<=7.                                    (3.3)
```

This proves the previously provisional P gate `A^2|F1` and extends it to
Q as `A^2B|F1`.

For fixed leading factors, the original 16-dimensional `F1` window is cut
to dimension eight on both branches: total codimension eight.  Relative to
row two, row three adds codimension four on P and three on Q.

## 4. Row four: the first square discriminant

Set

```text
Delta=4F2-V^2.
```

After (3.3), exact binomial expansion gives

```text
R4 = (3/4)V F3 + 3 Delta^2/(128H) + polynomial modes.       (4.1)
```

Consequently

```text
P: A  | Delta,       write Delta=A W,    deg W<=10;
Q: AB | Delta,       write Delta=AB W,   deg W<=9.          (4.2)
```

These conditions are necessary and sufficient.  For fixed `V`, row four
has codimension four in the P `F2` window and codimension five in the Q
window.

## 5. Row five: exact gcd strata

With (4.2), all omitted terms below are already polynomial.  The complete
remaining numerators are

```text
Q:  A^2 | 3W(16A F3-VW),                                  (5.1Q)

P:  A^2 | 3W(16A F3-VW)
             +10 c2 A V(8F2-V^2).                          (5.1P)
```

The other P `c2` term `(5/4)c2 A F3` is polynomial.  These are exact
necessary-and-sufficient row-five gates, including the kernel constant.

There is a useful complete stratification.  Put

```text
C=gcd(A,W),       A0=A/C,       W=C W0.
```

For Q, and for the `c2=0` P component, (5.1) is equivalent to

```text
A0 | V,
A0 | 16F3-(V/A0)(W/C).                                    (5.2)
```

For P one adds exactly

```text
c2=0  or  A|V.                                             (5.3)
```

If `c=deg C`, the Q stratum in `(V,W,F3)` has dimension `24+c` inside a
32-dimensional ambient space; its maximum is 28 at `C=A`.  The P
`c2=0` stratum has dimension `25+c`, maximum 29 inside the
34-dimensional `(V,W,F3,c2)` ambient.  The P component with arbitrary
`c2` and `A|V` has dimension 26.  These are honest fixed-factor dimensions;
there is no single constant-rank codimension before the gcd stratification.

## 6. Row six collapses the gcd stratification

The baseline nonpolynomial numerators at row six are

```text
N6P = 192A^3 W F4 + 6(8A F3-VW)^2 - A W^3,                (6.1P)
       denominator 1024 A^4;

N6Q = 192A^3 B W F4 + 6(8A F3-VW)^2 - AB W^3,            (6.1Q)
       denominator 1024 A^4 B.
```

On P the `c2` contribution, apart from `(5/4)c2 A F4`, is

```text
c2(640A^2 V F3+20A^2W^2-20AV^2W-5V^4)/(2048A^3).         (6.2)
```

Suppose a simple root of `A` does not divide `W`.  Row five then forces
`V=A v` locally and `16F3-vW` to vanish there.  In (6.1), the square has
order at least two while the last term has order exactly one.  The P mode
(6.2) has order at least three after putting it over the common denominator,
so it cannot cancel that term.  Contradiction.  Therefore

```text
A|W,       W=A Z.                                         (6.3)
```

In particular rows five and six strengthen (4.2) to

```text
Delta=H Z,       F2=(V^2+HZ)/4,       deg Z<=6.            (6.4)
```

Row five is now automatic on Q.  On P it is exactly `c2=0 or A|V`.
Substitution in row six leaves

```text
P: A  | 8F3-VZ;
Q: AB | 8F3-VZ.                                           (6.5)
```

Equations (6.4)--(6.5) give the parametrizations in the verdict.  `F4`
and `F5` occur only in polynomial terms, while `F6` is pure same-row gauge;
all three remain arbitrary.  The modes `c4,c6` are likewise free.

For fixed `A` (and `B`), the full raw solution scheme through row six has:

| branch/component | exact dimension | codimension in 210 raw `F1..F6,G1..G6` slots |
|---|---:|---:|
| P, `c2=0` | 63 | 147 |
| P, `A|V` with arbitrary `c2` | 60 | 150 |
| Q | 61 | 149 |

The P scheme is the union of the two displayed components; its dimension is
63.  The parameter maps are injective because `V,Z,T` are recovered in
order from `F1,F2,F3`, and the `c_m` are the distinct kernels of (2.1).

## 7. Exact controls and the q1 answer

The frozen replay includes one rejected mutation at every new gate:

* `F1=A` on P and `F1=AB` on Q pass row two but fail row three;
* `V=1,F2=0` passes row three but fails row four;
* on P, `V=Z=c2=1`, `W=A`, `F3=1/8` passes row four but fails row five;
* `V=Z=1,F3=0` passes row five with `W=A` and fails row six on each branch.

It also reconstructs three dense, full-upper-window positive fixtures:
the P `c2=0` component, the P active-`c2` component, and Q.  Every one has
the maximal raw degree at every weight and replays `D0=...=D6=0` over Q.

The clean q1 separator is stronger.  For arbitrary `deg V<=7`, set

```text
U=H+(V/2)t,        F=U^2,        G=U^3.                    (7.1)
```

Then both determinant brackets vanish identically, so `E=0`.  Its only
positive coefficients are

```text
F1=HV, F2=V^2/4;
G1=(3/2)H^2V, G2=(3/4)HV^2, G3=V^3/8,
```

which fit the frozen D3 windows exactly.  Take `V=1`.

* P fixture: `A=X^4-1`.  The q1 operator
  `Q -> 2AQ'-3A'Q`, `deg Q<=12`, has rank 13, while adjoining `F1=H=A^2`
  raises the rank to 14.
* Q norm-survivor fixture: `B=X^2-1`, `v=X^2/5`,
  `A=Bv'+(3/2)B'v=X^3-(2/5)X`.  The q1 operator
  `Q -> 4ABQ'-(6A'B+AB')Q`, `deg Q<=11`, has rank 12, while adjoining
  `F1=H=A^2B` raises the rank to 13.

Thus q1 is not implied by rows `D1..D6`; (7.1) shows that it is not implied
by **all homogeneous vanishing rows**, either.

The firewall is load-bearing: (7.1) has `D22=0`.  R7R1 licenses q1 only
after the affine target row and `D23=0`; there is no contradiction and no
claim here about the system `D1=...=D21=0,D22=1`.

## 8. Sharp successor

Fix the q1-negative P control

```text
A=X^4-1,       V=1,       F1=H=A^2,
```

and ask whether its raw extension satisfies

```text
D1=...=D21=0,       D22=1                              (no D23 yet).
```

A positive extension would prove that q1 contributes genuinely new
information exactly when row `D23` is added.  A negative result should emit
the earliest affine endpoint interaction and an exact certificate.  This is
a separate larger computation and is not smuggled into the present desk
artifact.

## 9. Replay and custody

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_upper_cascade_w3_w6_20260827/verify_upper_cascade.py --check
```

The replay uses exact `fractions.Fraction` arithmetic, a tiny Laurent ring,
direct binomial reconstruction, polynomial long division, and rational row
reduction.  It has no random seed or external CAS dependency.

Maximum licensed claim: the exact fixed-factor polynomial cascade through
`D6`, its dimensions, and nonimplication of q1 by the homogeneous vanishing
cascade.  No `D22=1` prefix, D23 theorem, endpoint exclusion, GGV landing,
counterexample, or JC2 conclusion follows.
