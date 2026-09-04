# Chart-necessity dossier for the (99,66) joint two-point chart

Date: 2026-09-04 UTC
Lane: `g9966-chart-necessity-opus5-20260903`
Frozen basis: `ce00e907002c40891a1d441badbc569100789e29`
Type: paper-grade necessity argument, plus desk-scale verification of the
chart's combinatorial and gauge spine. The engine kills are not recomputed.

## Result

This document assembles the necessity half of the conditional verdict carried by
the banked kills (`stage4_J_d159_k35 = 6264`, `stage8_G_local16_coord0 = 64`).
Every row family of the chart is traced to a printed statement of Moh 1983 or
Xu 2016 or to an identity of the chart; every convention is classified as a
gauge, a canonical construction, or an unsourced normalisation. The outcome is a
theorem with an explicitly enumerated, typed set of gaps:

```text
THEOREM 8.1 (conditional).  k algebraically closed, char 0.  Let (F,G) in k[x,y]^2
satisfy J(F,G) in k*, deg F = 99, deg G = 66, with Moh characteristic data
M = (-66,77,97), d = (99,33,11,1), V = (V_3,V_2) = (8,8)  (so s = 3, d_s = 11,
v_s = 8, u_s = 3), and with the principal minor roots split.  Assume N1-N4.
Then no such (F,G) exists.
```

`N1`, `N2` are inherited from the printed literature and were already typed
`OPEN` in the charged reports. `N3`, `N4` are **new findings of this lane**, both
about normalisations the charged chart uses silently: **N3** (sec 2.4) the chart
sets *both* constant centres to zero -- the major `D_2` centre constant `w_0` and
the principal-minor centre constant `a_0` -- but the gauge group supplies one
constant `y`-translation, moving them *together*, and normalises only the
invariant combination `8w_0 + 3a_0 = -[y^{10}]H`; the further condition
`a_0 = w_0` is unsourced. **N4** (sec 2.5, 3.4) the `D_1` recentring fixes the
`e^{12}` coefficient to 1 (equivalently the scale `beta` in the `h2` `D_2` face
`(pi^3-beta)^8`); this is proved free for all `D_1` **ranks** but not for the
ideal generated jointly with the other row families.

Independently verified here from the frozen sources, agreeing exactly with the
charged reports:

```text
CONFIRMED[CHART-IS-A-BIJECTION]     k^7161 <-> {(F,G) : deg = deg_y = (99,66),
                                    monic, in F = P^9, in G = P^6}; 7161 = 5049+2277-165
CONFIRMED[TOP-FORMS-ARE-FORCED]     Moh p.194 (Prop 5.4 + Lemma 5.3 + Prop 6.1)
CONFIRMED[MAJOR-SUPPORT-COUNTS]     h3: 66 = 43+2+21 ;  h2: 561 = 384+8+169
CONFIRMED[OUTER-D2/D1-COUNTS]       6600 -> 5598 -> 1002 -> 225 raw rows, exact
                                    Q-rank 176 (51/108/15/51 ; 44/73/15/44) -> 826
CONFIRMED[FACE-ODE-IDENTITIES]      Xu (8.2); design (2.5) with k = 5; q1' + 2p^3 = 0
CONFIRMED[PIVOT-LEDGER-CLOSED-FORM] all 66 (delta=5/2) and 31 of 35 (delta=2) joint
                                    Q* pivots re-derived: |coeff| = 9(99 - 3n - 11i),
                                    never 0 since 11 does not divide 3n, 1 <= n <= 8
```

The four gaps are listed with their exact missing statements in sec 9. No
`charge_basis` line is emitted: no new exit price is asserted.

## 0. The skeleton hypothesis, stated exactly

### 0.1 What "the (99,66) row" is

Work over algebraically closed `k`, char 0. For `(f,g)` monic in `y` with
`deg_y f = m`, `deg_y g = n`, Moh's *characteristic data* `{M_i, d_i}` are the
orders of contact `< n-2` in the factorisation of `f(y)` over `k[x]((g^{-1}))`,
together with `M_s = n-2`, and `d_r = gcd{n, M_1,...,M_{r-1}}` (Moh p.201 (4),(5)).
**The (99,66) row is Moh p.202, line 4:**

```text
n = 99,  m = -M_1 = 66,  M_2 = 77,  M_3 = 97 = n-2,  V_3 = 8,  V_2 = 8,
delta_2 = 1/3,  delta_1 = 4/9,  delta_3 = -1,  s = 3,
d = (99, 33, 11, 1),   d_s = 11,  v_s := V_s = 8,  u_s := d_s - v_s = 3,
n/d_s = 9,  m/d_s = 6,   -mu_1 = 66,  -mu_2 = 55,  -mu_3 = 145   (Xu (8.1)).
```

Regenerated here from Moh Definition 5.1(3) by the frozen census driver
(charged input 8), whose CONTROL 1 reproduces the printed `delta_2, delta_1`.
`u_s = 3` is what makes this row hard: it is the `d_s`-unit multiplicity of the
*second* (principal-minor) point at infinity; `u_s = 1` -- the other census rows
and the `(64,48)` control -- collapses to one Puiseux branch (Moh Prop 4.4, Xu
Prop 7.3) and carries no split. **Label reversal:** here `F` is the degree-99 and
`G` the degree-66 polynomial, so `(F,G) = (g_Moh, f_Moh) = (g_Xu, f_Xu)` and
`J(F,G) = -J(f_Moh, g_Moh)`; the charged convention.

### 0.2 Why a Keller pair of degrees (99,66) has *some* skeleton in the census

Source: Moh's **Theorem, p.200** (from Propositions 5.4 and 6.1) with the search
list p.200 l.-6 to p.201 l.13. (i) Moh p.194 l.-12: "we shall only consider the
case `M_s = n - 2` and the highest homogeneous form `g(x,y)` equals
`[(y-ax)^{v_s}(y-bx)^{u_s}]^{n/d_s}` for `a != b`, where `u_s = d_s - v_s`"; the
one-point alternative `d_s = -1` is excluded by Corollary 6.1 for a
minimal-degree counterexample. (ii) `d_s >= 4`, `3 <= s <= 5` (p.200 l.-14,
p.201 (6)). (iii) A hypothetical Keller pair with `deg f = m < deg g = n <= 100`,
`n` not dividing `m`, `M_s = n-2`, `J = 1`, degrees not simultaneously reducible,
satisfies the printed conditions (1)-(13). (iv) Moh p.202 l.3: "The Computer
program produces only the following exceptions which satisfy the necessary
numerical restrictions" -- four classes `(64,48)`, `(84,56)`, `(75,50)`,
`(99,66)`, with exactly one `(99,66)` row, that of sec 0.1.

### 0.3 Which other (99,66) skeletons exist -- the census gap

Running Moh's conditions (1)-(13) verbatim in his own search space, restricted
to `n = 99, m = 66`: (1)-(7) admit **1180** `V`-assignments, (1)-(13) admit **8**
(all with `d = (99,33,11,1)`, `s = 3`, `M_3 = 97`):

```text
M_2 = -22 : V_3 = 9,  V_2 = 1   u_s = 2   delta = (2/7,   3/14, -1)
M_2 =  22 : V_3 = 7,  V_2 = 1   u_s = 4   delta = (11/16, 9/16, -1)
M_2 =  22 : V_3 = 8,  V_2 = 1   u_s = 3   delta = (6/11,  4/11, -1)
M_2 =  22 : V_3 = 10, V_2 = 1   u_s = 1   delta = (8/23,  2/23, -1)
M_2 =  22 : V_3 = 7,  V_2 = 5   u_s = 4   delta = (7/12,  9/16, -1)
M_2 =  55 : V_3 = 10, V_2 = 2   u_s = 1   delta = (14/39, 1/13, -1)
M_2 =  77 : V_3 = 7,  V_2 = 8   u_s = 4   delta = (8/13,  7/13, -1)
M_2 =  77 : V_3 = 8,  V_2 = 8   u_s = 3   delta = (4/9,   1/3,  -1)  <- Moh p.202
```

Moh prints only the last. The printed conditions do not by themselves cut the
class down to it; the frozen census driver reaches the same conclusion globally
("the printed list (1)-(13) is NOT the whole of Moh's program"), and Moh's p.202
remark about `(75,50)` shows his program used more. What the extra restrictions
were is not printed. Typed:

```text
GAP[MOH-CENSUS-COMPLETENESS]:  MISSING -- "a Keller pair of degrees (99,66)
normalised as in sec 0.2 step 1 has M = (-66,77,97), V = (8,8)"; equivalently the
seven other (1)-(13)-admissible V-assignments at (99,66) are excluded.
```

Theorem 8.1 therefore carries the skeleton as a **hypothesis**, exactly as the
charged reports do. It is a theorem about the `(99,66)` row, not about the
degrees `(99,66)`.

### 0.4 The configuration trichotomy inside the row

Moh p.209 ("the fourth case"): there is a unique `pi`-root `sigma` of `g` of the
form `sigma = a_{-1}t^{-1} + a_0 + a_1 t + pi t^2` with
`g(sigma) = g_sigma(pi)t^{-18} + ...`, `deg g_sigma = u_s(n/d_s) = 27`, and

> "The polynomial `g_sigma(pi)` is either a power of a linear polynomial or the
> 9-th power of a cubic polynomial with precisely two roots."

* **(A) unsplit:** `g_sigma = (pi-c)^{27}`. Moh p.209 transforms the data to
  `n = 27, m = 18, M_2 = 21, V_2 = 8, delta_2 = -1, delta_1 = 0`, Jacobian `x^4`,
  and reduces to 10 coefficients. **Outside** this chart; it is the banked
  predecessor gate the delta-5/2 kill gate names `17(tt)`.
* **(B) `[2,1]` at `delta = 2`:** `g_sigma = p^9`, `p = pi^2(pi+3a)`, `a != 0`.
* **(C) `[1,1,1]` at `delta = 5/2`:** `p = pi(pi^2-c)`, `c != 0`. Xu 2016 sec 8
  shows Moh's dichotomy is incomplete: claim (i) has "one exception case open",
  namely this one.

Sec 7 proves (A),(B),(C) exhaust the possibilities; (B),(C) are the two chart
branches, killed by `17(pppp)` and `17(tttt)`.

## 1. The tower, the Theorem-1.2 order rows, and the chart

### 1.1 The tower is canonical

In char 0 the `d`-th *approximate root* of monic `Q in k[x][y]` of `y`-degree `N`,
`d | N`, is the unique monic `h` of `y`-degree `N/d` with
`deg_y(Q - h^d) < N - N/d` (Abhyankar-Moh; Moh sec 1). Put

```text
h2 := 3rd approximate root of F  (y-degree 33),   h3 := 3rd approximate root of h2  (11).
```

Both exist and are unique; no choice is made. `h3` is then the 9th approximate
root of `F`, i.e. a quasi-approximate root in the sense of Moh Definition 1.5,
which is what Theorem 1.2 requires.

**Lemma 1.1.** `deg h2 = deg_y h2 = 33` and `deg h3 = deg_y h3 = 11`.

*Proof.* The approximate root is given by universal polynomials with rational
coefficients in the coefficients of `Q` (only division by `d` occurs), so with
`(sigma_lambda Q)(x,y) = lambda^{-N}Q(lambda x, lambda y)` -- again monic in `y`
of `y`-degree `N`, with coefficients polynomial in `lambda^{-1}` -- one has
`A_d(sigma_lambda Q) = lambda^{-N/d}(A_d Q)(lambda x, lambda y)`. The left side is
bounded as `lambda -> infinity`; the right side is bounded only if
`deg A_d Q <= N/d`. As `A_d Q` is monic of `y`-degree `N/d`, equality holds. QED

### 1.2 The chart is a bijection

**Proposition 1.2.** With `P = y^3(y-x)^8` and
`S(D,r) = {A : deg A <= D, deg_y A < r}`, `dim S(D,r) = r(D+1) - r(r-1)/2`, the map

```text
h3 = P + H,              H  in S(10,11)   66
h2 = h3^3 + C2 h3 + C3,  C2 in S(21,11)  187 ,  C3 in S(32,11)  308
F  = h2^3 + A2 h2 + A3,  A2 in S(65,33) 1650 ,  A3 in S(98,33) 2739
G  = h2^2 + B1 h2 + B2,  B1 in S(32,33)  561 ,  B2 in S(65,33) 1650
```

is a bijection from `k^{7161}` onto the set of pairs `(F,G)` with
`deg F = deg_y F = 99`, `deg G = deg_y G = 66`, both monic in `y`, `in F = P^9`,
`in G = P^6`.

*Proof.* (Into.) `deg H <= 10 < 11` gives `in h3 = P`, `deg h3 = 11`; then
`deg(C2h3) <= 32`, `deg C3 <= 32 < 33` give `in h2 = P^3`, `deg h2 = 33`; then
`deg(A2h2) <= 98`, `deg A3 <= 98 < 99` give `in F = P^9`; and `deg(B1h2) <= 65`,
`deg B2 <= 65` give `in G = P^6`.

(Onto, injective.) Put `h2 = A_3(F)`, `h3 = A_3(h2)`; degrees 33, 11 by
Lemma 1.1. Since `deg_y(F - h2^3) <= 65 < 99`, the degree-99 forms agree, so
`(in h2)^3 = P^9`, hence `in h2 = P^3` (unique monic cube root of a form in
char 0) and likewise `in h3 = P`; so `H = h3 - P` lies in `S(10,11)`. Next
`F - h2^3` has total degree `<= 98` (top forms cancel) and `y`-degree `<= 65`;
dividing by `h2`, monic with `deg h2 = deg_y h2 = 33`, each step subtracts
`c(x)y^{j-33}h2` of degree `<= (98-j)+(j-33)+33 = 98`, so `deg A3 <= 98`,
`deg A2 <= 65`, both of `y`-degree `<= 32`. The same argument on
`deg(G-h2^2) <= 65` and on `deg(h2-h3^3) <= 32`, `deg_y(h2-h3^3) <= 21` gives
`B1 in S(32,33)`, `B2 in S(65,33)`, `C2 in S(21,11)`, `C3 in S(32,11)`. Each step
is division with remainder by a monic polynomial, hence unique. QED

**Counts (recomputed).** `66+187+308+1650+2739+561+1650 = 7161`. Without the two
fixed top forms the blocks are `77,198,319,1683,2772,594,1683`, total `7326`,
which equals `#{x^i y^j : i+j <= 99, j < 99} = 5049` plus
`#{i+j <= 66, j < 66} = 2277`; fixing the two top forms removes exactly
`99 + 66 = 165`. So the chart is a chart, not a dimension heuristic.

**No lost solutions.** Proposition 1.2 is an equivalence: every pair with the two
declared leading forms, in the normalised coordinates, has unique coordinates in
`k^{7161}`. The Tschirnhausen omissions (`no h3^2` in `h2`, `no h2^2` in `F`) are
not discarded terms but the defining property of the approximate root in char 0.
The `h2^1` term in `G` is *not* omitted (`B1` is free): `h2` is the approximate
root of `F`, not of `G`, and `G = h2^2 + B1 h2 + B2` is only `h2`-adic division.

### 1.3 The Theorem-1.2 order rows

**Source.** Moh Theorem 1.2 (p.149): for `f` monic in `k<<t>>[y]` with a coherent
complete system of `pi`-roots of multiplicities `{l_i}` and accuracy `lambda`,
`d | gcd(l_i)`, `h` a `d`-th quasi-approximate root of accuracy `lambda`,
`f = h^d + sum_{j<=d} h_j h^{d-j}`, `deg_y h_j < deg_y h`:

```text
ord h_j(sigma_i) >= (lambda/d) j = j * ord h(sigma_i).
```

**Order table.** With `t = x^{-1}`, `w = y/x`, at the major nodes `D_2`
(`delta_2 = 1/3`) and `D_1` (`delta_1 = 4/9`):

| object | degree | mult `D_2` | `ord D_2` | mult `D_1` | `ord D_1` |
|---|---:|---:|---:|---:|---:|
| `h3` | 11 | 8 | `-1/3` | -- | not defined |
| `h2` | 33 | 24 | `-1` | 8 | `-1/9` |
| `F` | 99 | 72 | `-3` | 24 | `-1/3` |
| `G` | 66 | 48 | `-2` | 16 | `-2/9` |

Derivation of the `h3` entry, which fixes the pattern: `h3` has 3 minor roots (at
distance `t^{-1}`) and 8 major roots (inside `D_2`), and the `D_2` general point
sits at distance exactly `t^{1/3}`, so `ord h3(sigma_2) = 3(-1) + 8(1/3) = -1/3`;
multiply by 3 and 9 for `h2`, `F`, and use `in G = P^6` for `-2`. There is
deliberately no `h3` row at `D_1`: 24 is not divisible by 9, so no `h3` child
chart exists there and none is invented.

Applied to the outer expansions of Proposition 1.2:

```text
D_2 :  ord A2 >= -2,   ord A3 >= -3,   ord B1 >= -1,   ord B2 >= -2
D_1 :  ord A2 >= -2/9, ord A3 >= -1/3, ord B1 >= -1/9, ord B2 >= -2/9
```

With base `h3` (`ord = -1/3`) it gives `ord C2 >= -2/3`, `ord C3 >= -1`, already
inside the charged 516-variable major tower. The `h3`-adic expansion of `F,G`
gives `F_1 = G_1 = 0` (chart identities), `F_2 = 3C2`, `F_3 = 3C3`, `G_2 = 2C2`,
`G_3 = 2C3 + B1`, etc.; the bounds `ord F_j >= -j/3`, `ord G_j >= -j/3` follow by
adding lower bounds and yield **no new rows** (a sum of `>=` bounds is a `>=`
bound; no equality is claimed).

## 2. The gauges

Four normalisations. Three are group actions; the fourth (sec 2.4) is not.

### 2.1 The two lines, the top forms, and `J_0 = 1`

**Necessity of the shape.** Moh p.194 l.-12 gives
`in g = [(y-ax)^{v_s}(y-bx)^{u_s}]^{n/d_s}` with `a != b`; and, same page,
"Proposition 6.1 implies that the highest homogeneous forms in `x` and `y` of
`T_1^psi,...,T_s^psi` are determined up to constant multiples", of which
`T_1 = f` is the degree-66 member. With `(v_s,u_s,d_s,n,m) = (8,3,11,99,66)`:
`in g = [(y-ax)^8(y-bx)^3]^9`, `in f = c[(y-ax)^8(y-bx)^3]^6`.

**Group.** `Gamma` = pairs `(A,(lambda,mu))`, `A in GL_2(k)` on `(x,y)`,
`lambda,mu in k*`, `(F,G) -> (lambda(F o A), mu(G o A))`, with source translations
`(x,y) -> (x+c_1, y+c_2)` and target translations `(F,G) -> (F+e_1, G+e_2)`. Each
element preserves Keller (`J_0 -> lambda mu det(A) J_0`), degrees, and the
characteristic data.

**Orbit representative.** (i) Some `A` sends the independent forms `y-ax`, `y-bx`
to `y-x`, `y`, uniquely up to the 2-torus scaling them separately; then
`in(F o A) = c''P^9`, `in(G o A) = c'P^6`, `P = y^3(y-x)^8`. (ii) `lambda = 1/c''`,
`mu = 1/c'` makes both monic with `deg = deg_y`. (iii) The residual freedom
`F -> s'^{-99}F(sx,s'y)`, `G -> s'^{-66}G(sx,s'y)` fixes `y = 0`, sends `y = x` to
`y = (s/s')x`, and multiplies `J_0` by `s s'^{-164}`; keeping the major line at
`y = x` forces `s = s'`, and the remaining one-parameter group scales `J_0` by
`s^{-163}`, so algebraically closed `k` supplies `s` with `s^{163} = J_0`. Hence

```text
in F = P^9,  in G = P^6,  P = y^3(y-x)^8,  J(F,G) = 1
```

is a legitimate representative: **the torus parameter `a = 1` in
`P_a = y^3(y-ax)^8` and the normalisation `J_0 = 1` are the same single gauge.**
`J_0 != 0` is not a gauge but the Keller hypothesis; only `J_0 = 1` is imposed.

The multiplicities follow: `in F = y^{27}(y-x)^{72}`, `in G = y^{18}(y-x)^{48}`,
matching Moh **Prop 6.2** (p.195): `deg_y g-hat = v_s n/d_s = 72`,
`deg_z g-hat = u_s n/d_s = 27`, and `48/18` for `f`.

### 2.2-2.3 Tschirnhausen omissions; target translations

The omissions are canonical (sec 1.1, Prop 1.2), not a gauge. The target
translations preserve `J` and the leading forms, changing only `A3(0,0)`,
`B2(0,0)`; available and unused.

### 2.4 The two constant centres -- the one normalisation that is not free

New finding; source of `GAP[TWO-CENTRE-NORMALISATION]`. The chart uses
simultaneously

```text
major D_2 general point : w = 1 + pi t^{4/3}          (i.e.  w_0 = 0)
minor general point     : w = a_0 t + u t^2 + z t^3   with a_0 = 0.
```

Both come from Moh Definition 5.1(4), `sigma_i = sum_j w_j t^j + pi t^{delta_i}`:
for `D_2` the centre is `t^{-1} + w_0` (the exponents `< delta_2 = 1/3` are `-1`
and `0`); for the minor disc Moh p.209 writes `a_{-1}t^{-1} + a_0 + a_1 t`, and
the minor line at `y = 0` forces `a_{-1} = 0` (linear gauge) while `a_1 = u` stays
free. Two constants remain.

**The gauge is one-dimensional.** The only element of `Gamma` moving them is
`y -> y - b`, under which `w_0 -> w_0 - b`, `a_0 -> a_0 - b`; so `w_0 - a_0` is a
gauge invariant. **What it normalises:** the 11 roots of `h3` are 8 major
(`= x + w_0 + O(x^{-1/3})`) and 3 minor (`= a_0 + O(x^{-1})`), summing to
`-[y^{10}]h3 = 8x - h_{10}` with `h_{10} := [y^{10}]H` a constant
(`deg H <= 10`), so comparing constant terms

```text
8 w_0 + 3 a_0 = - h_{10},      h_{10} -> h_{10} - 11 b
```

(the same computation with `F` gives `9(8w_0+3a_0)`, with `G` gives
`6(8w_0+3a_0)`: no new information). Hence in the gauge `h_{10} = 0` the
conditions `w_0 = 0` and `a_0 = 0` are equivalent to each other, and each is
**one scalar condition beyond the gauge**.

**Desk-scale check that neither is automatic** (`box/g9966necessity-20260903/`).
Major centre general (`w = 1 + w_0 s^3 + pi s^4`, `t = s^3`), all 66 `h3` lower
slots unknown, requirements `ord_s K3 >= 32` and `[s^{32}]K3 = pi^8`: for each
tested `w_0 in {0,1,2,-3}` the system has **45 scalar rows of rank 45, 21 free** --
the same counts as at `w_0 = 0`, but a different, non-diagonal row set. Minor
centre general (`w = a_0 t + u t^2 + z t^3`) on the 21-dimensional strict `h3`
space, requirement `ord_t K3 >= 9`: for each tested `(a_0,u)` the system has **15
rows of rank 15, 6 free** and is consistent for `a_0 != 0`. So the configuration
with `a_0 != w_0` is a genuinely different point, not a translate of the
normalised one. Typed:

```text
GAP[TWO-CENTRE-NORMALISATION]:  MISSING -- "for a Keller pair with the (99,66)
skeleton, in the gauge [y^10]H = 0, the constant term a_0 of the principal-minor
centre vanishes (equivalently a_0 = w_0)."
COST IF FALSE: the chart parametrises only the sub-family a_0 = w_0; the kills
then hold only there.  It is a NECESSITY gap, not a soundness gap -- the rows
imposed inside the chart remain correct.
BOUNDED REMEDY: carry a_0 as one extra symbolic coordinate with w_0 = -3a_0/8;
every row family is polynomial in it and (by the two probes) the block ranks are
unchanged, so the cost is one dimension, not a restructuring.
```

### 2.5 The `D_1` recentring scale

The `D_1` node uses `t = e^9`, `w = 1 + e^{12} + Pi e^{13}`; the `e^{12}` term is
the `D_2`-radius offset `t^{4/3}` of the `D_1` centre inside `D_2`, with
coefficient normalised to 1. Sec 3.4 proves every `D_1` rank is independent of
that scale; the joint-ideal statement is `N4`.

## 3. The outer `D_2` support preblock and the `D_1` boundary bands

### 3.1 Statement and source

The eight inequalities of sec 1.3 are the whole content: Moh Theorem 1.2 (p.149)
supplies them, Moh Proposition 6.2 (p.195) the multiplicities, Definition 5.1(3)
(p.179) the radii. **No equality face is imposed on the outer blocks:**
Theorem 1.2 is a `>=` statement, so only strictly-below slots become rows.

### 3.2 The weight cut, derived

Homogenise `Q in S(D,33)` by
`K_Q(t,w) = t^D Q(t^{-1}, w/t) = sum Qc_{r,q} t^r (w-1)^q`, `r >= 0`, `q < 33`,
`r+q <= D` -- an invertible change of basis (triangular from `x^i y^j`, with
`r = D - i - j`). Then `Q(t^{-1},sigma) = t^{-D}K_Q(t,w)`.

**`D_2`.** With `w = 1 + pi t^{4/3}`, `t = s^3`: `t^r(w-1)^q = pi^q s^{3r+4q}`, so
`W(r,q) = 3r+4q` is the exact `s`-weight. Distinct slots of equal weight carry
distinct powers of `pi`, so **no cancellation between slots is possible** and
`ord_s K_Q = min{W : Qc != 0}`. The bound `ord_t Q >= B` therefore reads
`W(r,q) >= 3(D+B)` on every occupied slot, i.e. `Qc_{r,q} = 0` whenever
`3r+4q < 3(D+B)`: a **unit** row per slot.

| block | `D` | `B` | `3(D+B)` | ambient | deleted | remaining | min `r` left |
|---|---:|---:|---:|---:|---:|---:|---:|
| `A2` | 65 | `-2` | 189 | 1650 | 1386 | 264 | 21 |
| `A3` | 98 | `-3` | 285 | 2739 | 2442 | 297 | 53 |
| `B1` | 32 | `-1` | 93 | 561 | 384 | 177 | 0 |
| `B2` | 65 | `-2` | 189 | 1650 | 1386 | 264 | 21 |
| total | | | | **6600** | **5598** | **1002** | |

(recomputed here from the thresholds alone). Two consequences used later: the whole degree-`D` face of `A2, A3, B2` is deleted
(`A2` has `4q <= 128 < 189` at `r = 0`) while `B1` survives at `r = 0` for
`q >= 24`; and **through `t`-power 21 the identities `KF = K2^3` and
`KG = K2^2 + tK_{B1}K2` are exact**, since `A2, B2` first survive at `r = 21` and
`A3` at `r = 53`.

**`D_1`.** With `t = e^9`, `w = 1 + e^{12} + Pi e^{13}`, a remaining slot
contributes `Qc_{r,q}e^{9r+12q}(1+Pi e)^q`, so the coefficient of `Pi^j e^E` is
`sum_{9r+12q+j = E} binom(q,j) Qc_{r,q}`, and `ord_t Q >= B_1` says all rows with
`E < 9(D+B_1)` vanish. Thresholds `583, 879, 287, 583`. Unlike `D_2` these are
**not** unit rows: several `(r,q)` share one `(E,j)`.

### 3.3 The exact `D_1` rank, recomputed

`D_2` has already forced `9r+12q >= 3 x (D_2 threshold)`, so the `D_1` rows live
in a finite window:

| block | `e`-window | raw `(E,j)` rows | exact `Q`-rank |
|---|---|---:|---:|
| `A2` | `[567,582]` | 51 | 44 |
| `A3` | `[855,878]` | 108 | 73 |
| `B1` | `[279,286]` | 15 | 15 |
| `B2` | `[567,582]` | 51 | 44 |
| total | | **225** | **176** |

so `1002 - 176 = 826` outer coordinates survive. Recomputed here by exact
Gaussian elimination on the integer binomial matrix; the 49 dependent rows reduce
identically to zero (slot dependencies, not a cokernel obstruction). The same
driver reproduces the *major* `h2` `D_1` band: 7 rows at `e`-powers
`291:1, 292:1, 293:1, 294:2, 295:2`, rank 7. Every pivot is a nonzero rational and
`rho, c, u, v` do not occur, so these rows are branch-independent and imposed
identically in both branches (they constrain the *first* point).

### 3.4 Scale-independence of the `D_1` block

With centre offset `alpha e^{12}`, `alpha != 0`, one has
`t^r(w-1)^q = alpha^q e^{9r+12q}(1 + (Pi/alpha)e)^q`, so the `(E,j),(r,q)` entry
becomes `binom(q,j)alpha^{q-j}`. Since `j` depends only on the row and `q` only
on the column,

```text
M(alpha) = diag(alpha^{-j}) . M(1) . diag(alpha^{q}),
```

both diagonal factors invertible. Hence the raw counts and the exact ranks
`44/73/15/44` (and 7 for `h2`) are **independent of `alpha != 0`**, and the row
space of `M(alpha)` is the image of that of `M(1)` under
`Qc_{r,q} -> alpha^q Qc_{r,q}`. Not established: that this substitution is a
symmetry of the other row families simultaneously. See `N4`.

### 3.5 The inner major blocks

Same weight cut with the fixed faces. For `h3`
(`K3 = w^3(w-1)^8 + sum Hc_{r,q}t^r(w-1)^q`, `r >= 1`, `q <= 10`, `r+q <= 11`),
boundary `3(11-1/3) = 32`: of 66 ambient slots **43** lie strictly below and **2**
on the face, at `(r,q) = (4,5),(8,2)`; the latter are rows because the `D_2` face
of `K3` must be exactly `pi^8`, a power of a linear polynomial (Moh Prop 4.4 /
Prop 6.1), and those slots would contribute `pi^5, pi^2`. Total **45** rows,
**21** free coordinates `(r,d)` with `v_r = max(0,ceil((33-3r)/4)) <= d <= 11-r`,
`1 <= r <= 11`. For `h2` (ambient `S(32,33) = 561`, boundary `3(33-1) = 96`):
**384** strictly below, **8** on the face at `(r,q) = (4k, 24-3k)`, `1 <= k <= 8`,
with values forced to `(-1)^k binom(8,k)` because the `D_2` face of `K2` is
`(pi^3-1)^8`; **169** strict coordinates remain, **392** rows. All four counts
were recomputed here.

The charged design asserts the face `(pi^3-beta)^8` without derivation; it follows
from the multiplicities (24 at `D_2`, 8 at `D_1`, so the 24 `D_2` roots form three
clusters of eight and the weight-96 face is a degree-24 polynomial in `pi` with
three distinct roots of multiplicity 8 each). The scale `beta` is fixed to 1 by
sec 2.5 -- a normalisation, not a theorem: the same one as `N4`.

## 4. The minor-incidence block, per branch

### 4.1 The branch datum and its necessity

Fix a branch `delta in {2, 5/2}` (sec 7). After the gauges of sec 2, with
`t = x^{-1}`:

```text
delta = 2   :  y = u t + z t^2,                     w = y t = u t^2 + z t^3
delta = 5/2 :  t = s^2, y = u s^2 + v s^4 + pi s^5, w = u s^4 + v s^6 + pi s^7
```

leaders `p = pi^2(pi+3a)`, `a != 0` (`[2,1]`) and `p = pi(pi^2-c)`, `c != 0`
(`[1,1,1]`). Xu sec 8 records `f(sigma) = p^6 t^{6(-8+3delta)} + ...`,
`g(sigma) = p^9 t^{9(-8+3delta)} + ...`, `T2(sigma) = p^5 t^{5(-8+3delta)} + ...`,
`T3(sigma) = q(pi)t^{13(-8+3delta)-1+delta} + ...`, `deg p = u_s = 3`,
`deg q = 13u_s+1 = 40`. At `delta = 2` this gives `ord F(sigma) = 9(6-8) = -18`,
`ord G(sigma) = -12`, i.e. exactly Moh p.209's
`g(sigma) = g_sigma(pi)t^{-18} + ...`, so

```text
t^{18} F(t^{-1},sigma) = p^9 + O(t),     t^{12} G(t^{-1},sigma) = p^6 + O(t).
```

These are *equalities* of Laurent expansions; they say two necessary things:

1. **Pole rows.** All coefficients below the leader vanish. Homogenised,
   `t^{18}F(t^{-1},sigma) = t^{-81}KF` and `t^{12}G = t^{-54}KG`, so the
   coefficient at pole exponent `-81+n` is `[t^n]KF`; `[t^0]KF = 0` automatically
   (the homogenised top form `w^{27}(w-1)^{72}` vanishes at `w = 0`), so the rows
   start at `n = 1`. The leader sits at `n = 63` (exponent `-18`), so 62 such
   vanishing rows exist for `F`; the engine used eight. For `delta = 5/2`, `s^9F(s^{-2},sigma) = s^{-189}KF`,
   `s^6G = s^{-126}KG`, so local power `n` is pole exponent `n-189` (resp.
   `n-126`) and the stage-8 row `G_local16_coord0` is the coefficient at `-110`.
2. **Leader rows.** The leading coefficient equals `p^9` (resp. `p^6`), imposed
   one level down on the common tower: `[t^9]K3 = p` for `delta = 2`,
   `[s^{21}]K3 = p` for `delta = 5/2`, all lower coefficients zero. Those are the
   18 (resp. 20) inner pivots.

`O(t)`/`O(s)` is a finite instruction, not an unknown tail: all polynomials have
finite support.

### 4.2 Pullback and truncation

Substitution is performed on the *same* 7161 chart coordinates, expanding
`(w-1)^q = (X-1)^q` with `X` of positive local order, so only `O(M/ord X)`
binomial terms survive to truncation `M`. The engine truncates at `t^9` (all
bands run at `t`-power `<= 8`); by sec 3.2 (`A2,B2` from `r = 21`, `A3` from
`r = 53`) this truncation is **exact**, since `KF = K2^3` and
`KG = K2^2 + tK_{B1}K2` identically through `t`-power 21. Raw finite-support row
counts are `(F,G) = (1134,513)` for `delta = 2` and `(1316,594)` for
`delta = 5/2`; those are equation labels, not ranks.

### 4.3 The face ODE and the `T3` packets

Xu's equation (7.1),
`d(T_s(sigma), g(sigma))/d(t,pi) = -J (T_s)_f(sigma) t^{-2+delta}`, descends from
Moh Proposition 4.1 and drives the classification. On the leaders it becomes a
polynomial identity; verified exactly in this lane:

* `delta = 2`, Xu display (8.2):
  `d(pi(pi+3a)^2(pi-2a)t^{-1}, pi^2(pi+3a)t^{-2})/d(t,pi) = 5pi^4(pi+3a)^2 t^{-4}`
  -- **identically true**, and the right side is `5p^2`.
* The degree-40 `T3` leader of the `delta = 2` branch,
  `R = z^{25}(z+3rho)^{14}(z-2rho)` with `p = z^2(z+3rho)`, satisfies
  `2 p R' - 25 p' R = k p^{14}` with **`k = 5`**, remainder 0. The exponent vector
  is `(25,14,1)`, **not** the `(26,13,1)` of `p^{13}(z-2rho)`; that difference is
  precisely what makes `delta = 2` survive Xu's step-by-step deduction.
* `delta = 5/2`: `q = p^{10}q_1`, `deg q_1 = 3u_s + 1 = 10`, `q_1' + 2p^3 = 0` with
  `p = pi(pi^2-c)`; with the charged normalisation
  `q_1 = -(1/5)(pi^{10} - (15/4)c pi^8 + 5c^2 pi^6 - (5/2)c^3 pi^4 + b_0)` the
  identity `d(q_1, p t^{-1/2})/d(t,pi) = -p^4 t^{-3/2}` holds identically. `b_0`
  is the integration constant; the charged `b_0 = 0` is a normalisation whose
  cost was measured independently (every `delta = 5/2` dimension rises by exactly
  1 without it, and the stage-8 residue is still exactly 64), so it is
  dimension-only and participates in no kill.

Packets, from Xu sec 7.3 (`(-mu_i)u_s/d_s` for `i <= s-1`, `((-mu_s-2)u_s/d_s)+1`
for `i = s`): `F = T0 : 27`, `G = T1 : 18`, `T2 : 15`, `T3 : 40`.
**Not imposed.** The identification of `T2, T3` with elements of `k[F,G]` -- the
effective-root bridge -- is `OPEN`: after the monic cancellation `G^3 - F^2`
(resp. `G^9 - F^6`) the Tschirnhausen span on the leading pair `(p^9,p^6)` is
`span{p^{18},p^{15},p^{12},p^9,p^6,p^0}`, containing neither `p^5` nor a degree-40
polynomial of shape `(25,14,1)` or `p^{10}q_1`; those leaders are residuals of
*subleading* jets, nonlinear in the chart coordinates. Its absence **weakens** the
imposed subsystem, so it cannot rescue a unit ideal.

## 5. The pole rows and the Jacobian rows

**Pole rows** are sec 4.1(1); necessity rests on the branch datum only. Engine
labels: `delta = 2` uses `F: -80,-79,-78` then `-77-k`, `G: -53,-52,-51` then
`-50-k`; `delta = 5/2` uses `F: -187,-185,-183` then `-181-2k`,
`G: -124,-122,-120` then `-118-2k`. The parity in the second branch (because
`t = s^2`) is why the `G` pole rows meet the Jacobian band every second stage
there but every stage at `delta = 2` -- the whole four-stage gap between the two
deaths.

**Jacobian rows.** `J(F,G) = 1` is an identity in `k[x,y]`, so every coefficient
`[x^i y^j](F_xG_y - F_yG_x)` with `i+j > 0` vanishes and the constant coefficient
is 1. The engine uses only the former, in total degrees `163 = 99+66-2` downward:

* degree 163 vanishes structurally, not as a row: `J(P^9,P^6) = 54P^{13}J(P,P) = 0`;
* the charged prefix uses `[x^{145}y^{17}]J, ..., [x^{136}y^{26}]J` (degree 162);
* stage 0 adds `[x^{135}y^{27}]J`; stage 1 the remaining degree-162 coefficients
  (`y`-powers 28..162); stage `n >= 2` **all** coefficients of total degree
  `163-n`. Stage 8 imposes all 156 coefficients of degree 155.

Homogenised, `J(F,G) = x^{163}KJ(1/x, y/x)` with

```text
KJ = 99 KF (KG)_w - t (KF)_t (KG)_w - 66 (KF)_w KG + (KF)_w t (KG)_t,
```

so `[x^i y^j]J = [t^{163-i-j} w^j]KJ`: Jacobian total degree `163-n` is `t`-power
`n`, and the label index `k` is the `w`-power (the invariant
`deg_w KJ_n <= 163-n`, i.e. `i >= 0`, is asserted on every run).

**Well-definedness.** Each `[x^iy^j]J` is `Z`-bilinear in the coefficients of `F`
and `G`, which by Prop 1.2 are polynomials with integer coefficients in the 7161
chart coordinates. So each Jacobian row is such a polynomial and involves **no
branch parameter**: `u,v,rho,c` occur only in the pole and leader rows, and the
Jacobian rows are identical in the two branches. The constant `1` (or a free
`kappa`) lives only in degree 0 and is never touched by `J162...J155`, so no kill
inverts or fixes a Jacobian constant.

**Mechanism.** Below the `A2/A3/B2` onset, with `A = K2`, `B = K_{B1}`,
`KJ = tA^3(99 A B_w - 96 B A_w) + 3t^2 A^3 (A_w B_t - A_t B_w)`; once
`B_0 = ... = B_{n-2} = 0` have been eliminated,
`[t^n]KJ = A_0^3(99A_0 B_{n-1,w} - (99-3n)B_{n-1}A_{0,w})` with
`A_0 = w^9(w-1)^{24}`. Writing `B_{n-1} = sum_q B1c_{n-1,q}(w-1)^q` and
`A_{0,w} = w^8(w-1)^{23}(33w-9)`,

```text
[t^n] KJ = w^{35}(w-1)^{95} sum_q B1c_{n-1,q}(w-1)^q ( 99 q w - (99-3n)(33w-9) ).
```

Three facts at once: the lowest `w`-power is exactly **35** (so Jacobian rows with
`k < 35` are vacuous -- this is why the charged prefix rows `k = 17..26` and the
stage-0 row `k = 27` reduce to `0 = 0`); each band is **linear in `B_{n-1}`
alone**; and the `k = 35` row is `-9(99-3n) sum_q (-1)^q B1c_{n-1,q} = 0`.

## 6. The `Q*`-pivot reductions and the localisations

### 6.1 The pivot rule

A row is used for elimination only when some variable occurs in exactly one
monomial, that monomial is the pure linear one, and its coefficient is a nonzero
**rational**. Such a row is `alpha X + L = 0`, `alpha in Q*`, `L` free of `X`, and
eliminating `X` is the ring isomorphism `A/(alpha X + L) ~= A'`, `X -> -L/alpha`.
`rho` and `c` are forbidden as pivots, and the engine asserts after each reduction
that the localisation parameter survives. So the whole elimination is a chain of
ring isomorphisms and the final constant residue proves emptiness in the original
presentation. (The `K2c` computation basis is unit-triangular with diagonal
coefficient 1 -- the delta-5/2 gate serialised the 495-rule inverse ledger -- and
a unit-triangular polynomial coordinate change preserves the unit ideal.)

### 6.2 The `66 + 35` joint pivots, listed and re-derived

Ledgers: `box/g9966s8-20260903/runs/delta52/stage8.json` and
`box/g9966band-20260903/runs/delta2/stage4.json`. Audited here:

```text
delta = 5/2 : 66 joint Q* pivots ; every coefficient a nonzero integer ;
              every pivot variable in the B1c block ; none is rho, c, u or v.
delta = 2   : 35 joint Q* pivots ; same three properties.
```

The 66 coefficients by stage `n` (pivot `B1c_{n-1,q}`, row `J_d(163-n)_k(35+i)`):

```text
n=1 : -864 -765 -666 -567 -468 -369 -270 -171 -72    (q = 24..32)
n=2 :  837  738  639  540  441  342  243  144   45   (q = 23..31)
n=3 : -810 -711 -612 -513 -414 -315 -216 -117  -18   (q = 22..30)
n=4 : -783 -684 -585 -486 -387 -288 -189  -90        (q = 22..29)
n=5 :  756  657  558  459  360  261  162   63        (q = 21..28)
n=6 : -729 -630 -531 -432 -333 -234 -135  -36        (q = 20..27)
n=7 :  702  603  504  405  306  207  108    9        (q = 19..26)
n=8 :  675  576  477  378  279  180   81             (q = 19..25)
```

The `delta = 2` ledger is the same `J`-band rows for `n = 1..4` with `k = 36..43`
(`36..42` at `n = 4`), together with four `G`-pole pivots `G_local5_coord0, ..., G_local8_coord0` of
coefficients `8, -8, 8, 8`, which take over the `k = 35` slot at each stage (the
label `G_local...` precedes `J_d...` in lexicographic pivot order).

**Closed form (new here).** From the mechanism of sec 5, with the `B1` outer
`D_2` support `3r+4q >= 93` and the two outer-`D_1` offset-0 kills `B1c_{3,21}`,
`B1c_{7,18}`, sequential elimination of the rows `k = 35, 36, ...` reproduces
**all 66** coefficients exactly, and

```text
| pivot coefficient at stage n, i-th pivot | = 9 (99 - 3n - 11 i),   sign constant
within a stage.
```

*Nonvanishing, proved:* `9(99-3n-11i) = 0` needs `11 | 3n`, i.e. `11 | n`, but
`1 <= n <= 8`. The smallest value attained is `9` (at `n = 7, i = 7`). So every
joint pivot divides by an explicit nonzero integer, independent of every chart
coordinate and of `u,v,rho,c`. The 31 `J`-band coefficients of the `delta = 2`
ledger obey the same formula; the four `G`-pole coefficients `+-8` are integers
read from the ledger.

With sec 3.3 (outer `D_1`: integer binomial matrix, all pivots nonzero rationals)
and sec 3.2/3.5 (outer and inner `D_2`: unit rows), this discharges the
requirement that **no elimination step in either branch divides by anything but a
nonzero rational constant**.

### 6.3 `J_0 != 0` and the branch localisations

`J_0 != 0` is the Keller hypothesis; `J_0 = 1` is the torus gauge of sec 2.1(iii),
available over algebraically closed `k`. No engine row touches degree 0, so no
kill depends on the value of `J_0`.

* `delta = 2`: the branch hypothesis is Moh p.209's second possibility --
  `g_sigma` is the 9th power of a cubic with **precisely two** roots -- so
  `p = z^2(z+3rho)` has exactly two distinct roots and `rho != 0`. If `rho = 0`
  then `p = z^3` is Moh's *first* possibility, case (A), excluded by hypothesis.
  (Xu Cor 7.5 independently forbids three distinct roots at
  `delta = 2 < (v_s+1)/(u_s+1) = 9/4`.)
* `delta = 5/2`: the branch is `[1,1,1]`, i.e. `p = pi(pi^2-c)` has `u_s = 3`
  distinct roots, which holds iff `c != 0`; `c = 0` gives `p = pi^3`, case (A).
* Neither kill actually needs them: `6264` and `64` are nonzero integers in the
  **unlocalised** reduced ideal, so it is already `[1]`; localising a zero ring
  cannot make it nonzero. The wrappers `Zrho*rho-1`, `Zc*c-1` were nevertheless
  run, with empty/point/raw controls `0,1,0` in both branches.

## 7. Exhaustiveness of the split classification

**Lemma 7.1.** Let `(F,G)` be a Keller pair with the `(99,66)` skeleton,
normalised as in sec 2, and `sigma` a `pi`-root of `F` for the principal minor
roots. Then exactly one of:

```text
(A) sigma does not split: F_sigma(pi) is a power of a linear polynomial;
(B) split at delta = 2   with p = pi^2(pi+3a), a != 0   ([2,1]);
(C) split at delta = 5/2 with p = pi(pi^2-c),  c != 0   ([1,1,1]).
```

*Proof.* Write `delta` for the split order, `p` for the leading polynomial,
`deg p = u_s = 3`; Xu Prop 7.3 (whose proof shows `p` is a linear power at order
1) gives `delta > 1`.

*Step 1 (ceiling).* Xu sec 8: `g(sigma) = p^9 t^{9(-8+3delta)} + ...`, i.e.
`ord F(sigma) = (n/d_s)(u_s delta - v_s) = 9(3delta-8)`; a root at infinity has
`ord F(sigma) < 0`, so `delta < v_s/u_s = 8/3`.

*Step 2 (denominator).* Xu sec 8: "our tools are two constrains: one is that the
denominator of order `delta <= u_s = 3`". So `den(delta) in {1,2,3}`, and

*Step 3 (candidates)* the rationals with `1 < delta < 8/3`, `den <= 3` are exactly
`{4/3, 3/2, 5/3, 2, 7/3, 5/2}`.

*Step 4 (how many parts).* Xu Cor 7.5: if `u_s > 1` and
`delta < (v_s+1)/(u_s+1) = 9/4`, `sigma` cannot split into `u_s = 3` different
roots; so `{4/3, 3/2, 5/3, 2}` admit only a two-part split, `{7/3, 5/2}` two or
three.

*Step 5 (the ODE).* Xu sec 8(i): "When `delta != 2` and `delta != 5/2`. From
equation 7.1, we can step by step deduce `q(pi) = p(pi)^{13}(pi - c)` and the
equation 7.1 can not hold for it." This removes `4/3, 3/2, 5/3, 7/3`. At
`delta = 2` Xu exhibits the surviving solution, display (8.2) -- verified in
sec 4.3 -- which is Moh's two-root split, the three-root alternative being
excluded by Step 4 (Xu sec 8(ii)). At `delta = 5/2` Xu deduces `q = p^{10}q_1`
with `q_1' = -2p^3`, which "can hold for any `p(pi)`", and records
`p = pi(pi^2-c)`: three distinct roots. `den(5/2) = 2`, and the Galois
automorphism `s -> -s` of `t = s^2` must permute the parts, consistently with
`p = pi(pi^2-c)` (it exchanges `+-sqrt(c)` and fixes 0).

*Step 6 (face gauge).* `pi -> lambda pi` sends `a -> lambda a`,
`c -> lambda^2 c`, so a nonzero branch parameter may be normalised; the engine
does not use this and keeps `rho`, `c` symbolic.

*Step 7 (no later split).* Xu sec 8(iii): after the `delta = 2` split the roots in
the disc centred at the double root do not split again before the final level
(`gcd(12,18,10,25) = 1` forces `p` and `q` to be powers of a common linear
factor). So (B) is a complete configuration, not a stage of a longer tower.

(A),(B),(C) are mutually exclusive (`p` is a linear power, or has exactly two, or
exactly three distinct roots), and Steps 1-5 leave nothing else. QED

**Sourced vs not.** Steps 1, 4, 6, 7 and the two surviving conclusions of Step 5
are printed (Xu sec 7.3, Cor 7.5, sec 8). Step 5's *elimination* of
`{4/3, 3/2, 5/3, 7/3}` rests on a single unproved sentence; Step 2's denominator
bound is asserted without proof (it is the numerical shadow of Moh p.201
(8)-(11), the Galois argument `t-bar -> omega t-bar` with `omega` an
`A_{r-1}`-th root of unity). Both are `N2` in sec 9. Case (A) is Moh p.209's
first possibility; it is **not** in the joint chart and **not** addressed here.

## 8. The theorem and its dependency graph

**Theorem 8.1 (conditional).** `k` algebraically closed of char 0,
`(F,G) in k[x,y]^2` with `J(F,G) in k*`, `deg F = 99`, `deg G = 66`; Moh
characteristic data of `(f,g) = (G,F)` equal to `M = (-66,77,97)`,
`d = (99,33,11,1)`, `V = (8,8)` (so `s = 3`, `d_s = 11`, `v_s = 8`, `u_s = 3`,
`M_s = n-2`, two points at infinity); and the principal minor roots split (case
(B) or (C) of Lemma 7.1). Assume `N1`-`N4` of sec 9. Then no such pair exists.

*Proof.* By sec 2, `(F,G)` may be replaced by a `Gamma`-equivalent pair with
`in F = P^9`, `in G = P^6`, `P = y^3(y-x)^8`, `J = 1`, and (by `N3`) both constant
centres zero; by Prop 1.2 it then has unique coordinates in `k^{7161}`. By sec 1.3
and 3.1-3.3 it satisfies the 45 inner `h3` rows, the 392 `h2` `D_2` rows, the 7
`h2` `D_1` rows, the 5598 outer `D_2` unit rows and the 176 outer `D_1` rows (using
`N4` for the presentation of the last two). By Lemma 7.1 it lies in branch (B) or
(C); by sec 4 it satisfies the branch leader and pole rows, and by sec 5 all
Jacobian rows of degrees 163 down to 155. By sec 6 every elimination on that
system is a ring isomorphism. The charged engine, two hostile gates and a
clean-room re-implementation all reduce branch (B) to a residue containing the
integer `6264` at stage 4 and branch (C) to `64` at stage 8; since
`1 = (1/6264)*6264 = (1/64)*64` in `Q`, both ideals are the unit ideal. QED

### Dependency graph

```text
sec 2 gauges      <- Moh p.194 (Prop 5.4, Lemma 5.3, Prop 6.1) + Prop 6.2 p.195
                     + k algebraically closed, GL_2 and translations
Prop 1.2 (chart)  <- Abhyankar-Moh approximate roots (char 0) + Lemma 1.1 + sec 2
sec 3 rows        <- Moh Thm 1.2 p.149 + Def 5.1 p.179 + Prop 1.2   [N4]
skeleton          <- Moh Thm p.200 + p.202 table                    [N1]
Lemma 7.1         <- Xu Prop 7.3, Cor 7.5, sec 8(i)(ii)(iii) + Moh p.209   [N2]
sec 4 rows        <- Lemma 7.1 + Prop 1.2 + sec 2.4                 [N3]
sec 5 rows        <- the identity J(F,G) = 1 + Prop 1.2
sec 6             <- Q*-pivot ring isomorphisms; all pivots in Q*
kills             <- AUDIT 17(pppp) delta=2 stage-4 residue 6264
                     AUDIT 17(tttt) delta=5/2 stage-8 residue 64
                     + clean-room re-implementation (both, row-level)
Theorem 8.1       <- all of the above, conditional on N1-N4
```

Charged lane reports behind the computational nodes (all sealed, all
hash-verified at the head of this lane): `g9966-global-design-sol56` (chart,
tower, minor charts, first `F,G/J` prefix); `g9966-outer-bridge-grok46` (outer
`D_2`/`D_1`; `T2,T3` bridge `OPEN`); `g9966-global-band-sol56` (staged
continuation, `delta = 2` stage-4 death); `g9966-delta52-stage8-sol56`
(`delta = 5/2` stage-8 death); `g9966-branchB-kill-gate-gpt55` and
`g9966-delta52-kill-gate-gpt55` (hostile gates; the `K2c` inverse ledger);
`g9966-independent-engine-opus5` (clean-room re-implementation, both branches).
Banked audit deltas named there: `17(sss)` (branch classification), `17(tt)` (the
unsplit predecessor, case (A)), `17(pppp)`, `17(tttt)`.

**What the theorem is not.** Not a statement about unrestricted degrees `(99,66)`
(that needs `N1` and case (A)); not about the other three census classes; not
about the two-dimensional Jacobian conjecture. No point survived either branch,
so nothing is recomposed and no `REPRESENTATIVE`, `FULL_ACTUAL_EXIT` or `KELLER`
claim is made anywhere.

## 9. What the referee will attack

**N1. `GAP[MOH-CENSUS-COMPLETENESS]` (inherited; derived in sec 0.3).**
*Missing:* "a Keller pair of degrees `(99,66)` normalised as in sec 0.2 (i) has
`M = (-66,77,97)`, `V = (8,8)`." Asserted by Moh p.202; the printed conditions
(1)-(13) leave 8 `V`-assignments. *Severity:* none for the kills (the skeleton is
a hypothesis of Theorem 8.1); fatal for a degree statement.

**N2. `GAP[XU-8(i)-STEP]`, `GAP[DEN(delta) <= u_s]` (inherited; sec 7).**
*Missing:* (a) "if `sigma` splits at order `delta` then `den(delta) <= u_s`";
(b) "for `delta in {4/3, 3/2, 5/3, 7/3}`, equation (7.1) forces
`q = p^{13}(pi-c)`, which is impossible." (a) is asserted by Xu sec 8 without
proof (it should follow from Moh p.201 (8)-(11)); (b) is one sentence of Xu
sec 8(i), of the same shape as the proof of Cor 7.5 but not written out for these
four values. *Severity:* fatal to exhaustiveness; the two kills are untouched.
*Remedy:* four finite face-ODE computations of the size of sec 4.3.

**N3. `GAP[TWO-CENTRE-NORMALISATION]` (new; derived in sec 2.4).** *Missing:*
"in the gauge `[y^{10}]H = 0`, the constant term of the principal-minor centre
vanishes (equivalently `a_0 = w_0`)." *Severity:* a **necessity** gap, not a
soundness gap -- rows imposed inside the chart remain correct, but the chart may
parametrise only the sub-family `a_0 = w_0`. *Remedy:* carry `a_0` as one extra
symbolic coordinate with `w_0 = -3a_0/8`; every row family is polynomial in it and
the block ranks are unchanged, so the cost is one dimension.

**N4. `GAP[D1-RECENTRING-SCALE]` (new; derived in sec 3.4).** *Missing:* "the
`D_1` centre offset coefficient `alpha` (equivalently the scale `beta` in the `h2`
`D_2` face `(pi^3-beta)^8`) may be set to 1 jointly with the other
normalisations." Sec 3.4 proves every raw count and exact rank
(`51/108/15/51`; `44/73/15/44`; `7`) is `alpha`-independent and that the row space
transforms by `Qc_{r,q} -> alpha^q Qc_{r,q}`; what is missing is that the same
substitution fixes the major `D_2`, minor, pole and Jacobian rows. *Severity:*
moderate. *Remedy:* check that substitution against the four other families, or
carry `alpha` symbolically in the `D_1` block.

**Other attacks, with the answers already on record.**

* *"An engine artefact."* The branches die at different stages (4 vs 8) on
  different row families (a Jacobian row vs a `G` pole row); and dropping the
  Jacobian band alone, or the pole rows alone, leaves `delta = 2` **alive** at
  stage 4 (dimensions 945, 915, no residue). The death is their interaction.
* *"The implementation is wrong."* The clean-room re-implementation reproduced
  both constants, both stage numbers, all intermediate dimensions, the outer
  raw/rank sequences, the joint `Q*` sequence and the stage-8 pivot coefficients;
  sec 6.2 re-derives all 66 in closed form from a two-line formula.
* *"The `K2c` basis hides a non-invertible change."* The delta-5/2 gate serialised
  the 495-rule triangular inverse (diagonal coefficient 1, every non-leader
  dependency solved earlier in the `(r,-q)` order); unit-triangular polynomial
  coordinate changes are ring isomorphisms.
* *"The residue is nonzero only after localisation."* No: `6264` and `64` are
  integers in the *unlocalised* reduced ideal (sec 6.3).
* *"An omitted condition could rescue the branch."* Omitting rows only enlarges
  the scheme, so `OPEN[EFFECTIVE-T2-T3-BRIDGE]` and the unranked remainder of the
  Jacobian ideal cannot restore a point to a unit ideal.
* *"It would kill a genuine automorphism."* The strongest available control is the
  tame automorphism `F = x + y^6`, `G = y + (x+y^6)^6` of degrees `(6,36)`, whose
  normalised Jacobian has exactly one nonzero `(t,w)` slot and survives every
  band; perturbing one homogeneity weight makes it fail on 8 slots, so the control
  is not vacuous. A *two-point* automorphism of degrees `>= 6` does not exist
  (Jung-van der Kulk), so the two-point control is necessarily at degrees `(1,1)`,
  where the `s = 3` tower is `NOT-APPLICABLE`.
* *"The `(64,48) -> (16,12)` calibration is missing."* The p.208 display equations
  are absent from the frozen PDF's text layer and the clean-room lane declined to
  reconstruct them (`GAP[P208-ANSATZ]`). The charged control ideals are `[1]` under
  both readings of the printed repeated `c_5`, wrapper controls passing, but
  `OPEN[PRINTED-C5-EMENDATION]` remains. It calibrates the method, never
  `(99,66)`.

## 10. Reproduction and audit

### 10.1 Custody

The lane receipt `xmodel/g9966-chart-necessity-opus5-20260903.run.v2` was parsed
mechanically: `awk` joined each indexed `charged_input_<i>_sha256` to the matching
`charged_input_<i>_basename` under the receipt's `lane_inputs_dir`, and the
generated 11-line manifest was streamed to `sha256sum -c`. **11/11 OK**; no digest
was retyped. No ledger, `jc2-lean`, `ideation-*` file, or in-progress lane report
was read or edited. Reads outside the frozen set: the two source PDFs (themselves
frozen inputs), the repository twin `box/moh_skeleton_N.py` imported by charged
input 8 as its own control, and the engine run JSONs named in sec 6.2. All writes
are this report plus `box/g9966necessity-20260903/`.

### 10.2 Desk-scale jobs run here

All drivers and outputs are in `box/g9966necessity-20260903/`, covered by
`artifacts.sha256` (`ef588f010806d2f5985c0e073a939014fa37fa595e977e57611ad09dd9caa9c3`,
which excludes itself); every entry passes `sha256sum -c`.

| driver -> output | what it checks (sec) | wall |
|---|---|---:|
| `census_9966.py` -> `census-9966.txt` | (1)-(7) and (1)-(13) at `(99,66)`; the p.202 row (0.1, 0.3) | 41 s |
| `support_and_ranks.py` -> `support-and-ranks.txt` | chart counts, multiplicities, split arithmetic, inner `h3`/`h2` blocks, outer `D_2` thresholds, exact `D_1` ranks (1.2, 2.1, 3.2, 3.3, 3.5, 7) | 7 s |
| `face_odes.py` -> `face-odes.txt` | Xu (8.2); `2pR' - 25p'R = 5p^{14}`; `q_1' + 2p^3 = 0` (4.3) | 3 s |
| `pivot_ledger.py` -> `pivot-ledger.txt` | the `66 + 35` pivot audit and the closed form (5, 6.2) | 40 s |
| `centre_probes.py` -> `centre-probes.txt` | the two centre-constant consistency probes (2.4) | 60 s |

All foreground, all far under 10 minutes; Python 3 with SymPy and exact
`fractions.Fraction` arithmetic over `Q`. `census_9966.py` imports the frozen
census driver (charged input 8) via its repository twin.

### 10.3 FALLACY-v2 audit

* **Flag/place/series.** The major flag (`D_2`, `D_1`, radii `1/3`, `4/9`, residue
  `y = x`), the principal-minor place (`y = 0`, `u_s = 3`), the split order
  `delta`, the pole filtration and the Jacobian homogeneous filtration are five
  distinct indices; sec 5 writes out the conversion between the last two. Shared
  coefficient arrays are arrays, not identified flags. Strict-below `D_2`
  deletion stays distinct from at-level `D_1` parting and denominator shedding.
* **Floor/attainment.** Theorem 1.2 is used only as a `>=` bound; outer equality
  faces are deliberately not rows (sec 3.1). The two inner faces (`pi^8`,
  `(pi^3-1)^8`) are rows only because the corresponding leading forms are *fixed*
  by sec 2.1, and the `beta = 1` normalisation is flagged as `N4`, not promoted.
* **Carrier/attainment.** Nothing is `REPRESENTATIVE` or `FULL_ACTUAL_EXIT`; no
  point survived, so no pair is recomposed and no `F_xG_y - F_yG_x == 1` check is
  claimed.
* **Pole/interior.** Pole identities are used only inside the declared vertex
  hypotheses of Lemma 7.1; no new pole theorem is inferred.
* **`sat()` wrapping.** The only saturations are the two Rabinowitsch scripts,
  rings `0,(rho,Zrho),dp` and `0,(c,Zc),dp`, three controls each; sec 6.3 notes
  the residues are units before wrapping.
* **Raw remainder degree.** Residues are normal forms in the declared `Q*`
  quotient, each a nonzero integer constant before any nonlinear question arose;
  sec 6.2 proves no pivot leader vanishes.
* **Variable/ring map.** The label reversal, the homogenisation
  `K_Q = t^D Q(t^{-1},w/t)`, the substitutions `t = s^3`, `t = e^9`, the two branch
  substitutions and the field `Q` are declared. Name agreement between
  implementations is never used as evidence; sec 6.2 compares computed values.
* **Prime label/derivative.** Primes are `d/dz` in the `delta = 2` face ODE and
  `d/dpi` in the `delta = 5/2` one; `_w, _t, _pi` are declared partials.
* **Merge-free/M-descent; target/arrival index.** Not used.

No exit-price assertion is made, so **no `charge_basis` line is emitted**.

### 10.4 Final typed result

```text
ASSEMBLED[CHART-NECESSITY-DOSSIER, (99,66) JOINT TWO-POINT CHART]
THEOREM[NO-KELLER-PAIR-WITH-THE-(99,66)-SKELETON | N1, N2, N3, N4]   (sec 8)
GAP[MOH-CENSUS-COMPLETENESS] = N1        GAP[XU-8(i)-STEP] + GAP[DEN<=u_s] = N2
GAP[TWO-CENTRE-NORMALISATION] = N3 (new) GAP[D1-RECENTRING-SCALE] = N4 (new)
OPEN[EFFECTIVE-T2-T3-BRIDGE]  (an omission; cannot rescue a unit ideal)
NOT-ADDRESSED[case (A), the unsplit principal-minor configuration]
```
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `51805`.
- Body SHA-256:
  `12994be18a3c1564f5536a8eb0407aca89a83152784f2d98ebb52f4ae191e034`.
- Frozen basis: `ce00e907002c40891a1d441badbc569100789e29`.
