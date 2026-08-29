# Hostile review — `(8,12)` order two: exact-square combined-load Pell/Chebyshev support

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-exact-square-pell-chebyshev-support-theorem-20260826.md` |
| Target SHA-256 | `523a32dd0da666029e2dee1531e0cd0775c0010d07d40ef440dfe5164cf152cf` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged reviews and the dual-AWS result were opened only because they are named; no producer status line, no `PASS` token, and no printed radical/standard basis is evidence |
| Method | source reading and hand derivation only; SHA-256 of the target and the six frozen inputs; no Singular, Sage, SymPy, msolve, Lean, CAS, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`523a32dd0da666029e2dee1531e0cd0775c0010d07d40ef440dfe5164cf152cf`,
matching the required pin. Independently recomputed SHA-256 of the six
artifacts pinned in target §0 match those pins. Producer verdict language,
the target's own status line, charged review tokens, the printed
`PASS_EXACT_REDUCED_SUPPORT` string, and both exact-Q and `F_65521` radical
outputs were not used as evidence. No file other than this review was
written.

---

## Verdict

**CONFIRMED.**

The recurrence `(2.1)` is the coefficient form of logarithmic
differentiation of `(1+p t^2+c t^3+r t^4)^alpha`, and the seven tails of
`H=sqrt(Q)*(Q^2+beta Q+gamma)` are exactly the index-shifted combination
`(2.2)`. Characteristic zero is used to divide by `n=1,...,17` and by the
powers of two that appear as leading denominators.

Seven-tail vanishing forces `c=0` on geometric points. The original
equations are affine-linear in `(beta,gamma)`. On `D(c)` the first three
tails force `beta=5 Delta/8` together with the weight-twelve relation
`Delta^3+8 p Delta c^2+8 c^4=0`; in particular they do **not** force
`gamma=0` as an intermediate. The leftover one-parameter candidate of
`E1,E2,E3,E6` is
`Delta=-32 p^2/9`, `c^2=128 p^3/27`, and is killed by `E5=-128 p^6 c/729`.
The `p=0` slice is killed already by `E5` together with `E1,E2,E3`. Thus
`V(E1,...,E7) intersect D(c)` is empty over an algebraic closure of
characteristic zero. Nullstellensatz puts `c` in the radical, so the
saturation `(E1,...,E7):c^infinity` is the unit ideal. The displayed
exact-Q standard-basis elements were not independently verified as
ideal-membership statements and are not used.

On `c=0` the two negative `T`-coefficients `(4.2)` are correct, the passage
to `(E2,E4,E6)` is triangular, and `T^{-5}` cannot contribute before
`z^{-10}`. The reduced locus is the square component `V(c,Delta)` with
arbitrary `(beta,gamma)`, union the Chebyshev component
`V(c,16 beta-5 Delta,256 gamma-5 Delta^2)`. Direct expansion gives the Pell
identity `A^2-Q P(Q)^2=Delta^5/262144=D^5/256`, so
`A-sqrt(Q) P(Q)=O(z^{-10})` with leading term `D^5/(512 z^{10})` whenever
`D!=0`. The seven-row bound is therefore strictly unsharp on a reduced
nonsquare family.

The radical/intersection formula `(1.3)` is the ideal of that union in
`L[p,c,r,beta,gamma]`. Both components are defined over `L`. The statement
is the affine chart `k10=1` of `(0.1)`; the hyperplane `k10=0` is a
different two-load problem and is not silently a Chebyshev family on
`c=0`. Unitriangular Laurent-to-Faber transport through seven rows applies
to `H` because it is a property of `z0(w)=w+O(w^{-1})`, but `(1.2)` is not
a literal total-Rees, target-tie, terminal `[6,2]`, or Taylor theorem.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-exact-square-pell-chebyshev-support-theorem-20260826.md` | `523a32dd0da666029e2dee1531e0cd0775c0010d07d40ef440dfe5164cf152cf` | target (matches required pin) |
| `xmodel/max12-812-order2-first-normal-pade-support-promotion-20260826.md` | `40790378bfcc7b0e0719038ef0e951712abef570b4865c0bca371409706c9f94` | charged Padé promotion; nonzero-`k10` square implication for a different series `F`; unitriangular seven-row transport |
| `xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md` | `2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5` | charged Padé lemma; not a combined-load theorem |
| `xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md` | `73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6` | named parent of the Padé theorem; opened only to obey the inspection clause |
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md` | `82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f` | charged source weights `Lambda^2 k10`, `Lambda^6 k6`, `Lambda^10 k2` and target grades `Lambda^{13}` through `Lambda^{19}` |
| `cases/max12_812_order2_exact_square_pell_20260826/RESULT.md` | `2b42cf9f0f28818341ccb63de5af3accf72c5dc3026f4ebe6aec17898f1d2f85` | named producer result; opened only because it is charged; its radical and `PASS` token are not evidence |
| `cases/max12_812_order2_exact_square_pell_20260826/EVIDENCE.sha256` | `2ba3ad04ca2fb181db9d146e947cfb5aa23588e1020a79577cfc72f80e388f65` | named evidence list; not used as a calculation |

All seven hashes match the values printed in the target. Two-prime modular
calculations are not used. The charged algebraic input actually used is:
the principal-part substitution `z0(w)=w+O(w^{-1})` with even correction
`O(w^{-2})`, hence unitriangularity of the first seven negative
`z`-coefficients against the first seven negative `w`-coefficients, for an
arbitrary series; the first-normal identification of those seven
`w`-coefficients with the first-normal gate; and the Rees weight list
`Lambda^2 k10`, `Lambda^6 k6`, `Lambda^10 k2` with inhomogeneous target
`(delta_1,...,delta_7)=(0,mu2,0,mu4,0,mu6,J/4)`. The charged Padé lemma
`k10!=0 => K` square is a theorem about
`F=(3/8) N^2/K+k10 K^{5/2}`, not about `H`, and is not used to classify
`H`.

---

## Strongest exact theorem that survives

Work over a field `L` of characteristic zero. Write

```text
Q = z^4 + p z^2 + c z + r,
Delta = p^2 - 4 r,
H = sqrt(Q) (Q^2 + beta Q + gamma),
```

in the formal branch `sqrt(Q)=z^2+O(1)` at infinity, and let `E_l` be the
coefficient of `z^{-l}` in `H`. After base change to an algebraic closure,

```text
V(E1,...,E7)_red
  = V(c, Delta)
    union
    V(c, 16 beta - 5 Delta, 256 gamma - 5 Delta^2).
```

Equivalently, in `L[p,c,r,beta,gamma]`,

```text
rad(E1,...,E7)
  = (c, Delta (5 Delta - 16 beta), Delta (beta^2 - 5 gamma)).
```

The first component is the square locus `Q=(z^2+p/2)^2` with arbitrary
load ratios `(beta,gamma)`. The second is a reduced two-parameter family,
nonsquare on `Delta!=0`, on which the scaled identity

```text
A^2 - Q P(Q)^2 = Delta^5 / 262144,
P(Q) = Q^2 + (5 Delta/16) Q + 5 Delta^2/256,
A = T^5 - (5 Delta/16) T^3 + (5 Delta^2/256) T,
T = z^2 + p/2,
```

gives `A-sqrt(Q) P(Q)=O(z^{-10})` with nonzero `z^{-10}` coefficient
whenever `Delta!=0`.

This is the exact seven-tail support of the normalized combined load
`(0.1)` on the chart `k10=1`. It does not classify `k10=0`, does not pull
the identity back through the literal total-Rees rows or the target grades
`Lambda^{13},...,Lambda^{19}`, does not impose the terminal `[6,2]`
passport or either Taylor family, does not construct or exclude a strict
arc, does not close order two or `(8,12)`, and does not prove maximum
twelve or JC2.

---

## Attack 1 — recurrence `(2.1)`, index shifts in `(2.2)`, and the seven tails of `sqrt(Q)(Q^2+beta Q+gamma)`

**CONFIRMED.** There is no off-by-one and no wrong branch.

Let `g(t)=1+p t^2+c t^3+r t^4` and
`f=g^alpha=sum_{n>=0} a_n(alpha) t^n`, with `a_n=0` for `n<0` and
`a_0=1`. Logarithmic differentiation gives

```text
g f' = alpha g' f,
g' = 2 p t + 3 c t^2 + 4 r t^3.
```

The coefficient of `t^{n-1}` is

```text
n a_n + p (n-2) a_{n-2} + c (n-3) a_{n-3} + r (n-4) a_{n-4}
  = 2 alpha p a_{n-2} + 3 alpha c a_{n-3} + 4 alpha r a_{n-4},
```

hence

```text
n a_n
  = p (2(alpha+1)-n) a_{n-2}
  + c (3(alpha+1)-n) a_{n-3}
  + r (4(alpha+1)-n) a_{n-4},
```

which is `(2.1)`. Characteristic zero inverts every `n>=1` needed below.

Now `Q=z^4 g(t)` with `t=z^{-1}`, and the branch `sqrt(Q)=z^2 g^{1/2}`
gives

```text
H = z^{10} g^{5/2} + beta z^6 g^{3/2} + gamma z^2 g^{1/2}.
```

The coefficient of `z^{-l}` is therefore

```text
E_l = a_{10+l}(5/2) + beta a_{6+l}(3/2) + gamma a_{2+l}(1/2),
```

which is `(2.2)`. For `1<=l<=7` one needs `a_n` through `n=17,13,9`
respectively. The first negative power of `H` is `z^{-1}` from `a_11`, not
from `a_10`; the polynomial part starts at `z^{10}` and is not a tail.

Independently computed integer-content denominators of `E1,...,E6` over
`Z[p,c,r,beta,gamma]` are `256,1024,512,2048,2048,32768`, matching the
first six entries of `(2.3)`. The seventh claimed denominator `4096` is
compatible with the 2-adic content of the recurrence at `n=17` and is not
load-bearing for the variety.

---

## Attack 2 — seven-tail vanishing versus `c=0` in characteristic zero

**CONFIRMED** as a reduced-point statement, by a CAS-free elimination from
`(2.2)`. The producer's Groebner narrative is not an implication from the
original seven equations in the order claimed, and is not used.

Write `C_l=a_{2+l}(1/2)`, `B_l=a_{6+l}(3/2)`, `A_l=a_{10+l}(5/2)`, so
`E_l=A_l+beta B_l+gamma C_l`. Split `g=g_even+c t^3` with
`g_even=1+p t^2+r t^4`, and write
`psi_k(beta)=[u^k](1+p u+r u^2)^beta`. Odd and even parts of `g^alpha` are
then finite sums in `c^{2j+1}` and `c^{2j}` against these `psi_k`.

The first three tails, computed this way and rewritten in
`Delta=p^2-4r`, are

```text
E1 = (c/256) (15 Delta^2 - 48 beta Delta + 128 gamma - 40 p c^2),
E2 = (-5 Delta^3 + 24 beta Delta^2 - 128 gamma Delta
      + 120 p Delta c^2 - 192 beta p c^2 - 40 c^4) / 1024,
E3 = (c/512) (-15 p Delta^2 + 48 beta p Delta - 128 gamma p
      + 20 (3 p^2-4 r) c^2 - 32 beta c^2).
```

The two odd tails combine as polynomials by

```text
512 E3 / c + 256 p E1 / c
  = 4 c^2 (5 Delta - 8 beta),
```

equivalently `128 E3 + 64 p E1 = c^3 (5 Delta - 8 beta)`. On `D(c)`,
`E1=E3=0` therefore forces

```text
beta = 5 Delta / 8,
gamma = 15 Delta^2 / 128 + 5 p c^2 / 16.
```

(The Chebyshev ratio is `beta=5 Delta/16`, so this is a different line.)
Substituting into `E2` yields

```text
Delta^3 + 8 p Delta c^2 + 8 c^4 = 0.                 (E2'')
```

If `Delta=0` then `8 c^4=0`, hence `c=0`, contradicting `D(c)`. So any
hypothetical `D(c)` point has `Delta!=0`.

The even tail `E4` is dependent on `E1,E2,E3`: after the same substitution
it equals `5 p (Delta^3+8 p Delta c^2+8 c^4)/2048`. The next even tail is
not. With the same `(beta,gamma)` one finds

```text
E6 = -5 Delta (p^2 Delta^2 + 8 p^3 c^2 - p Delta c^2 - 3 c^4)
     / 32768   modulo (E2'').
```

On `D(c)` this forces

```text
p^2 Delta^2 + 8 p^3 c^2 - p Delta c^2 - 3 c^4 = 0.    (E6'')
```

If `p=0`, then `(E6'')` is `-3 c^4=0`, hence `c=0`. Directly on `p=0`,
`(E2'')` is `c^4=8 r^3` and `E5` becomes `-40 r^3+3 c^4=0`, hence
`16 r^3=0` and again `c=0`. The remaining case is `p!=0`. The weighted
ratios `t=Delta/p^2` and `mu=c^2/p^3` reduce `(E2'')` and `(E6'')` to

```text
t^3 + 8 mu t + 8 mu^2 = 0,
t^2 - mu t + 8 mu - 3 mu^2 = 0.
```

Eliminating gives `mu=-4 t/3` and then `t(9 t+32)=0`. The root `t=0`
forces `mu=0`, i.e. `c=0`. The leftover geometric candidate is

```text
Delta = -32 p^2 / 9,     c^2 = 128 p^3 / 27,
beta = -20 p^2 / 9,      gamma = 80 p^4 / 27.
```

On that locus the next odd tail evaluates to

```text
E5 = -128 p^6 c / 729,
```

which is nonzero in characteristic zero whenever `p!=0` and `c!=0`.
Therefore there is no geometric point of `V(E1,...,E7)` on `D(c)`.

This uses `E1,E2,E3,E5,E6`. The seventh tail is not required. Characteristic
zero is essential: the leftover residue is `-2^7/3^6`, and the intermediate
denominators include `2,5,8,9,16,27,128,256,512,729`.

The displayed standard-basis elements `gamma^2 c`,
`3 beta^2 c^3-10 gamma c^3`, `c^3(5 Delta-8 beta)`, and the length-four
`c`-form in target §3 were not checked as membership in `(E1,...,E7)`.
Interpreted as a description of the original equations, the smallest false
intermediate implication in that paragraph is: “on `D(c)`, the first row
gives `gamma=0`”. From `E1,E2,E3` on `D(c)` one has
`gamma=15 Delta^2/128+5 p c^2/16`, which is not `gamma=0`. The subsequent
order `gamma=0 => beta=0 => Delta=0 => p=r=0` is therefore not the
elimination of `(2.2)`. The emptiness conclusion is nevertheless true, by
the argument above, so this is a defect of the CAS paragraph that the
target itself declines to treat as evidence, not a defect of `(1.2)` or
`(1.3)`. By Nullstellensatz over an algebraic closure of characteristic
zero, `c` lies in `rad(E1,...,E7)`, and the saturation by `c` is the unit
ideal.

---

## Attack 3 — `c=0`: `[T^{-1}]`, `[T^{-3}]`, triangular passage, square/Chebyshev split

**CONFIRMED.**

On `c=0` set `T=z^2+p/2` and `D=Delta/4`, so `Q=T^2-D`. Then

```text
Q^2 + beta Q + gamma = T^4 + B T^2 + C,
B = beta - 2 D,
C = D^2 - beta D + gamma,
```

which is `(4.1)`. The branch `sqrt(Q)=T (1-D/T^2)^{1/2}` gives
`H=T^5 sigma` with `sigma=(1-D u^2)^{1/2}(1+B u^2+C u^4)` and `u=T^{-1}`.
The binomial series

```text
(1-D u^2)^{1/2}
  = 1 - (D/2) u^2 - (D^2/8) u^4 - (D^3/16) u^6 - (5 D^4/128) u^8 + ...
```

yields

```text
[T^{-1}] H = [u^6] sigma = -D^3/16 - B D^2/8 - C D/2,
[T^{-3}] H = [u^8] sigma = -5 D^4/128 - B D^3/16 - C D^2/8.
```

Substituting `B,C` produces exactly `(4.2)`:

```text
[T^{-1}] H = -(D/16) (5 D^2 - 6 beta D + 8 gamma),
[T^{-3}] H = -(D^2/128) (5 D^2 - 8 beta D + 16 gamma).
```

Because `H` is a series in odd powers of `T`, and `T=z^2+p/2` is even in
`z`, all odd `E_l` vanish. Through `z^{-7}`,

```text
T^{-1} = z^{-2} - (p/2) z^{-4} + (p/2)^2 z^{-6} + O(z^{-8}),
T^{-3} = z^{-6} + O(z^{-8}),
T^{-5} = z^{-10} + O(z^{-12}).
```

Hence `E2=X`, `E4=-(p/2) X`, `E6=(p/2)^2 X+Y` with
`X=[T^{-1}]H` and `Y=[T^{-3}]H`. This map is triangular, so
`E1=...=E7=0` if and only if both brackets in `(4.2)` vanish.
(`T^{-5}` cannot contribute before `z^{-10}`, so the same vanishing is
equivalent already for the first nine negative coefficients.)

If `D=0`, both brackets vanish identically and `Q=T^2` is a square in
`L[z]`, with `(beta,gamma)` free. If `D!=0`, subtracting the two bracketed
equations gives `gamma=beta D/4`; substitution then gives
`beta=5 D/4` and `gamma=5 D^2/16`, i.e.

```text
beta = 5 Delta / 16,     gamma = 5 Delta^2 / 256.
```

That is the second component of `(1.2)`. The two closed sets are
irreducible: `(c,Delta)=(c,p^2-4r)` is prime (linear in `r`), and the
Chebyshev ideal is a graph over the `(p,r)`-plane.

---

## Attack 4 — Pell identity, the constant `Delta^5/262144`, and the tail order

**CONFIRMED.** The identity is exact, and the first uncancelled negative
power is `z^{-10}`, not an earlier order.

With `D=Delta/4` the displayed polynomials are

```text
P = Q^2 + (5 D/4) Q + 5 D^2/16
  = T^4 - (3 D/4) T^2 + D^2/16,
A = T^5 - (5 D/4) T^3 + (5 D^2/16) T.
```

Direct expansion, collecting even powers of `T`:

```text
A^2 = T^{10} - (5 D/2) T^8 + (35 D^2/16) T^6
      - (25 D^3/32) T^4 + (25 D^4/256) T^2,
Q P^2 = T^{10} - (5 D/2) T^8 + (35 D^2/16) T^6
        - (25 D^3/32) T^4 + (25 D^4/256) T^2
        - D^5/256.
```

All positive-degree terms cancel, and `A^2-Q P^2=D^5/256`. Since
`Delta=4 D` and `4^5=2^{10}`, `262144=2^{18}`,

```text
Delta^5 / 262144 = 2^{10} D^5 / 2^{18} = D^5 / 256,
```

which is `(5.2)`. Equivalently, `T=sqrt(D) x` conjugates `(5.2)` to the
standard identity `T_5(x)^2-(x^2-1) U_4(x)^2=1`, with
`A=D^{5/2} T_5(x)/16` and `P=D^2 U_4(x)/16`; the polynomial identity does
not require `D!=0`.

On `Delta!=0`,

```text
A - sqrt(Q) P(Q)
  = (D^5/256) / (A + sqrt(Q) P(Q)).
```

The denominator has leading term `2 z^{10}`, so the difference is
`D^5/(512 z^{10})+O(z^{-12})`. In particular it is `O(z^{-10})` and not
`O(z^{-9})` or better: the coefficient of `z^{-10}` is nonzero. Combined
with Attack 3, the first nine negative Laurent coefficients vanish on the
whole Chebyshev component, and the seventh row is not merely failing at a
nilpotent or a closure point.

---

## Attack 5 — radical formula, dimensions, field hypotheses, `k10=1`, lost branches

**CONFIRMED** for the numbered claims. The affine chart `k10=1` is
essential and is stated.

Let `I1=(c,Delta)` and `I2=(c,16 beta-5 Delta,256 gamma-5 Delta^2)` in
`L[p,c,r,beta,gamma]`. Both are prime in characteristic zero. Their
intersection is the ideal of the union in `(1.2)`. Writing
`u=16 beta-5 Delta` and `v=256 gamma-5 Delta^2`, one has
`(u,v,Delta)=(Delta,beta,gamma)` and `(Delta) cap (u,v)=(Delta u, Delta v)`
because `L[p,r][beta,gamma]/(u,v) ≅ L[p,r]` is a domain. The identity

```text
256 (beta^2 - 5 gamma) = u^2 + 10 Delta u - 5 v
```

then shows, with `5` and `256` units,

```text
I1 cap I2
  = (c, Delta (5 Delta-16 beta), Delta (beta^2-5 gamma)).
```

Attacks 2--3 give `V(E1,...,E7)_red=V(I1) union V(I2)` after geometric
base change. Both sides of `(1.3)` are radical (`I1 cap I2` is an
intersection of primes; characteristic zero is perfect), so
`rad(E1,...,E7)=I1 cap I2`. The equality of radicals descends from an
algebraic closure to `L` because the generators have rational
coefficients.

Affine dimensions in `(p,c,r,beta,gamma)`: the square component is
three-dimensional (`p,beta,gamma` free, `c=0`, `r=p^2/4`); the Chebyshev
component is two-dimensional (`p,r` free); their intersection is the
curve `c=Delta=beta=gamma=0`. The second component is nonsquare precisely
on `Delta!=0`, as claimed. No further reduced component exists.

Field hypotheses: characteristic zero is used throughout (binomial square
root of `1+O(t^2)`, inversion of `n`, inversion of `2,5,16,256`, and the
residue `-128/729`). Geometric base change is stated for `(1.2)` and is
sufficient; it is not needed to define either component, both of which are
`L`-rational in the coefficients `(p,c,r,beta,gamma)`.

Normalization `k10=1`: the series `H` is the chart `k10!=0` of `(0.1)`
after dividing by `k10`. Vanishing of tails is unaffected by a nonzero
scalar, so the reduced support of the projective load
`(k10:k6:k2)` on `D(k10)` is exactly `(1.2)` in the ratios
`beta=k6/k10`, `gamma=k2/k10`. The hyperplane `k10=0` is not in this
chart. It is not a silently lost Chebyshev family on `c=0`: the two-load
series `sqrt(Q)(beta Q+gamma)` has, for `c=0` and `D!=0`, incompatible
`[T^{-1}]` and `[T^{-3}]` conditions unless `beta=gamma=0`. A leftover
`k10=0` analysis on `D(c)` is outside the target. Projective closure of
`(p,c,r)` is not claimed.

---

## Attack 6 — application boundary

**CONFIRMED** as a firewall, not as a total-Rees theorem.

The charged substitution is `z0(w)=w+O(w^{-1})` with even correction
`O(w^{-2})`. For an arbitrary series `S=sum_{k>=1} a_k z^{-k}` one has
`z0^{-k}=w^{-k}+O(w^{-(k+2)})`, so the coefficient of `w^{-m}` depends
only on `a_1,...,a_m`. Unitriangularity through seven rows is therefore a
property of the coordinate change, not of the particular series `F` in the
Padé lemma, and applies to `H`. Vanishing of the first seven Faber rows of
`H` is equivalent to `E1=...=E7=0`, hence to `(1.2)` on the chart
`k10=1`.

That is not a literal total-Rees pullback. The charged one-parameter Rees
presentation is the flat pullback of

```text
Phi_ell
  = r_ell(C, Lambda^2 k10, Lambda^6 k6, Lambda^10 k2)
    - Lambda^{12+ell} delta_ell,
(delta_1,...,delta_7)=(0, mu2, 0, mu4, 0, mu6, J/4).
```

The three source loads have distinct weights. The unweighted combination
`(0.1)` is the receiver only after those weights, and a chosen valuation
ray, have been substituted into the literal total source, as target §6
states. A simultaneous source-load tie can make the three weighted summands
comparable; it does not identify them with `H` before that substitution.

A target tying the same grade is a separate inhomogeneous row and cannot
be merged into `(0.1)`. The terminal `[6,2]` passport, both Taylor
families, and any higher-contact section are not present in `(1.2)`. No
strict arc is constructed or excluded. Nothing here closes order two,
`(8,12)`, maximum twelve, or JC2.

The charged Padé lemma remains a theorem about a different series
`F=(3/8)N^2/K+k10 K^{5/2}`. Isolated vanishing of the `k10 Q^{5/2}` tail
still forces the square locus, in agreement with that lemma: the Chebyshev
ratios require a genuine three-load cancellation, not a single-load
cancellation.

---

## Scope firewall

This review confirms only the exact seven-tail support of the normalized
combined load `H=sqrt(Q)(Q^2+beta Q+gamma)` over a characteristic-zero
field, in the affine chart `k10=1`, together with the Pell identity
`(5.2)` and the tail order `(5.3)`. It does not:

- classify the two-load chart `k10=0`, nor any projective-load point with
  `k10=0` on `D(c)`;
- pull `(1.2)` through the literal total-Rees rows, the substitutions
  `Lambda^2 k10`, `Lambda^6 k6`, `Lambda^10 k2`, or a chosen valuation ray;
- absorb target grades `Lambda^{13},...,Lambda^{19}`, the terminal
  `[6,2]` condition, or either Taylor family into `(0.1)`;
- identify `H` with the first-normal series `F`;
- construct or exclude a strict `Lambda!=0` arc;
- close order two, `(8,12)`, maximum twelve, or JC2.

The CAS paragraph in target §3 is not part of the confirmed statement.
Its intermediate order `gamma=0`, then `beta=0`, then `Delta=0`, then
`p=r=0` is not the elimination of `(2.2)` and is not relied upon.

CONFIRMED
