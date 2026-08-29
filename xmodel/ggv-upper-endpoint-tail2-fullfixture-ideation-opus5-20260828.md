# Cutoff two: the full fixed branch-P endpoint fixture

Date: 2026-08-28
Author: Opus 5 (independent researcher)
Status: **REDUCTION** — exact, cover-free, verified against the frozen source.
Not an exclusion, not a witness. No promotion claimed.

## Verdict in one paragraph

The complete 303-variable / 513-generator fixed branch-P cutoff-two fixture
reduces *exactly* — with no Groebner basis, no localization of any endpoint
carrier, no cover, and no characteristic assumption beyond `char 0` — to a
divisibility system in **96 raw parameters plus five scalars**, together with a
**single closed-form endpoint identity carrying one free rational constant**.
The 18 literal `D22` coefficient equations collapse to

```text
A^5 * Phi_22  =  X^5/40 - X/8 + gamma,        gamma in Q,   A = X^4-1,
```

and the 495 equations of rows `D4..D21` collapse to the statement that
`G` is the truncation of an explicit five-mode algebraic family. A corollary
that is already exact and cover-free pins the endpoint pole order at three of
the four roots of `A`. The cutoff-five two-branch mechanism does **not**
survive; the cutoff-five additive gauge does, and a second one appears.

---

## 0. Custody, scope firewalls, and what was *not* done

Authoritative source, hash re-verified in this session:

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json   (slot/weight registry)
```

Firewalls actually honoured:

* **Every mathematical claim below was rederived from the displayed recurrence
  and diffed term-by-term against the 513 frozen generators.** Nothing is
  inferred from a specialized unit. The tail-5 packet
  `cases/ggv_8_28_upper_endpoint_tail5_desk_20260828/` was read for patterns
  only; every item reused from it (the endpoint determinant, the `F8[X^0]`
  gauge) is independently re-derived here and cited as such.
* **Characteristic.** Everything is over a field `K` of characteristic zero.
  Used twice and only twice: `ker(d/dX)` on `K[X]_A` equals `K`; and `A=X^4-1`
  is squarefree. No modular reduction is used anywhere; no modular fact is
  evidence.
* **Localization.** Exactly one localization appears: `K[X] -> K[X]_A`
  (inverting `A=X^4-1`). It is used only to *derive* the mode form; because
  `K[X] -> K[X]_A` is injective and the mode form is pulled back as literal
  `A`-divisibility of numerators, the resulting equivalence in §4 and §5 is an
  **equivalence over `K[X]`, requiring no cover**. No endpoint carrier
  (`a,b,c,d`, `V0`, `Z`, `T`, any `f_*`/`g_*`) is ever normalized or inverted.
* **Field radical vs scheme.** §4/§5 are statements about `K`-valued points.
  They are *not* asserted as identities of the nonreduced coefficient scheme.
  §2 (the two additive gauges) *is* a scheme identity and is flagged as such.
* No AWS job launched. No local CAS (Singular/Macaulay2/Sage) used — all
  arithmetic is exact `fractions.Fraction` in standard-library Python.
* `jc2-lean` was not entered, listed, searched, read, built, or modified.
  No canonical ledger and no existing case packet was edited. This report is
  the only file written outside `/tmp`.
* No promotion is claimed. Everything below awaits different-model review.

---

## 1. Independent reconstruction of the fixture (VERIFIED)

The fixture is rebuilt from scratch from

```text
D_n = sum_(i+j=n) ( (12-j) F_i' G_j + (i-8) F_i G_j' ),        ' = d/dX
```

with `A = X^4-1`, `H = A^2` and the *fixed* head

```text
F0 = A^4          G0 = A^6
F1 = A^2          G1 = (3/2) A^4
F2 = (1 + A^2 Z)/4                    G2 = (3/8) A^4 Z + (3/4) A^2
F3 = (Z + A T)/8                      G3 = (3/16) A^3 T + (3/8) A^2 Z + 1/8
Z = sum_{k=0}^{6} z_k X^k             T = sum_{k=0}^{9} tt_k X^k
```

`G1,G2,G3` are **derived**, not assumed: they are the unique solutions of
`D1=D2=D3=0` with `c2=0`. `F_4..F_14`, `G_4..G_21` are the literal raw windows.

Diff result against the frozen source:

* rows `D0,D1,D2,D3` vanish **identically** (all X-degrees, symbolically);
* rows `D4 .. D21`: every one of the 495 generators matches term-for-term
  and coefficient-for-coefficient;
* row `D22`: all 18 generators match, with exactly one difference — the frozen
  `row 22, x_degree 0` generator carries an extra constant `-1`. That is the
  folded-in affine target `D22 = 1`. `per_row["22"].target == 1` confirms it.

Literal endpoint coordinate, reconstructed (not imported):

```text
D22[X^0] - 1  =  -1 - f_0_1*g_1_0 + f_1_0*g_0_1
              =  -1 - F7[X^0]*G15[X^1] + F11[X^1]*G11[X^0].
```

The tail-5 carrier identification `a=g_1_0`, `c=g_0_1`, `d=f_1_0` and
`b <-> F7[X^0]` therefore transfers verbatim to the full fixture, **but** the
tail-5 gloss "`b = F7[X^0]` plus its forced prefix `G` lift" has no cutoff-two
meaning (there is no linear prefix at cutoff two — see §7).

Slot dictionary used throughout (verified against the weight registry):

```text
f_a_b  <->  X^a t^n  in F,  with  n = 8 + 3a - b
g_a_b  <->  X^a t^n  in G,  with  n = 12 + 3a - b
```

Variable census by weight: `z_* (7) @ w=2`, `tt_* (10) @ w=3`, then
`F_4..F_14` (79 slots) and `G_4..G_21` (207 slots); total 303. All 513
generators have **total degree exactly <= 2** in the raw variables.

---

## 2. Two exact additive gauges (SCHEME identity, cover-free)

Exactly two of the 303 variables occur in **no** generator:

```text
f_0_0 = F8 [X^0]          g_0_0 = G12[X^0]
```

Reason, from the recurrence and not from a census: `F_8` enters `D_n` only
through `(12-j)F_8' G_j` because its own weight coefficient `(i-8)` vanishes at
`i=8`; a constant is killed by `'`. Dually `G_12` enters only through
`(i-8) F_i G_12'` because `(12-j)` vanishes at `j=12`.

Consequence: the coefficient scheme is a product with `A^2_K`, i.e.
`f_0_0 = g_0_0 = 0` is a **global `G_a x G_a` slice meeting every orbit**. This
is a scheme-level identity, needs no cover, and is not a carrier
normalization. Effective variable count `303 -> 301`.

The tail-5 packet reports the `F8[X^0]` gauge (its `p129`). The `G12[X^0]`
gauge is, as far as this report's reading goes, new at cutoff two; it is the
exact dual and is verified here directly.

---

## 3. The `R_n` absorption identity (VERIFIED, rows 1..22)

Put `R_n = G_n - (3/2) H F_n` and `P_n = sum_{i+j=n, i,j>=1} F_i F_j`. Then,
as an identity of polynomials in `X` and the 303 raw variables:

```text
D_n = L_n(R_n)
    + sum_{i+j=n, i,j>=1} [ (12-j) F_i' R_j + (i-8) F_i R_j' ]
    + 3 H P_n'  +  (3/4)(n-16) H' P_n ,

L_n(R) = 2H [ (12-n) H' R - 4 H R' ].
```

Verified symbolically for `n = 1..22` on the full fixture (zero residual).

Two consequences that matter:

1. **`F_n` cancels out of `D_n` entirely.** The `H^2 H' F_n` coefficient is
   `3(n-8) + 3(12-n) - 12 = 0`. So `F_n` is free at row `n` and first acts at
   row `n+1`. This is what makes the system triangular.
2. `(F_n, G_n) -> (F_n, R_n)` is a **triangular linear automorphism of the raw
   affine space**: `H * (F_n window) is contained in (G_n window)` for every
   `n` (checked slot-by-slot), so `R_n` sweeps exactly the `G_n` window while
   `F_n` remains a free fibre coordinate. No localization, no cover.

Head values: `R_1 = 0`, `R_2 = (3/8) H`, `R_3 = (3/16) H Z + 1/8`.

---

## 4. The complete general solution: five modes (VERIFIED)

Generating-function form of the recurrence (rederived, then verified):

```text
E(F,G) = F_X * (12 - t d/dt) G  +  G_X * (t d/dt - 8) F,        E = sum_n D_n t^n.
```

For any `beta`, `E(F, t^m F^beta) = t^m F^(beta-1) F_X F [ (12-m) - 8 beta ]`,
so `E(F, t^m F^((12-m)/8)) = 0` identically. Over `K[X]_A[[t]]` (where
`F_0 = A^4` is invertible) these span the general solution of `E(F,G)=0`.

Writing `W = F^(1/4)` (pinned by `W_0 = A` via `G_0 = A^6`), the modes with
polynomial leading coefficient are exactly `m` even, `0 <= m <= 12`, giving
`A^((12-m)/2) = A^4, A^3, A^2, A, 1` at `m = 4,6,8,10,12` — the five
preregistered P characteristic directions, here **derived** rather than
posited. Odd `m` needs `A^(half-integer)` and is excluded over `K[X]_A`.

> **Theorem D.** For `K`-valued points, `D4 = ... = D21 = 0` is *equivalent* to
> ```text
> G  ==  sum_{k=0}^{6} c_{12-2k} t^(12-2k) W^k      (mod t^22),     W = F^(1/4),
> ```
> with `c_0 = 1`, `c_2 = 0` (the fixture pin), and `c_4,c_6,c_8,c_10,c_12` free
> scalars in `K`. Coefficientwise:
> ```text
> G_n = (F^(3/2))_n + c_4 F_{n-4} + c_6 (F^(3/4))_{n-6}
>                   + c_8 (F^(1/2))_{n-8} + c_10 (F^(1/4))_{n-10} + c_12 [n=12].
> ```

Note `Phi(w,s) = sum_k c_{12-2k} s^(12-2k) w^k` is weighted-homogeneous of
weight 12 with `wt(w)=2`, `wt(s)=1`; the fixture's `c_2 = 0` deletes the
`s^2 w^5` monomial.

**Independent confirmations run in this session.**

* The kernel dimension of `L_n` restricted to the literal `G_n` window,
  computed by exact RREF straight from the frozen generators, is
  `1,0,1,0,1,0,1,0,1` for `n = 4,5,6,7,8,9,10,11,12` and `0,0,0` at
  `n = 13,14,15` — exactly the five even modes and nothing else.
* Positive control, replayed against all 513 frozen generators: on the
  reviewed separator `U = A^2 + t/2`, `F = U^2`, `G = U^3` (all 303 raw
  variables zero) plus arbitrary `c_4 t^4 U^2 + c_8 t^8 U + c_12 t^12`
  (tested at `(c_4,c_8,c_12) = (1,0,0), (0,1,0), (0,0,1), (3/7,-5,11/2)`),
  **every** generator of rows 4..21 evaluates to `0` and row 22 gives
  `D22 = 0`. `c_6, c_10` are not polynomial on this `F`, as predicted.
* Compatibility-condition counts predicted by the theorem,
  `(40-n) - dim(G_n window) + [n even and n<=12]`, reproduce the exact RREF
  counts row by row: `16,15,16,15,16,15,16,15,16,16,16,16` for `n=4..15`
  (the cascade was carried that far in this session; rows 16..21 are
  predicted `17,17,17,18,18,18`, unverified).
* Rows `D4, D5, D6` produce **zero** nonvacuous conditions (all 47 left-null
  contractions vanish identically), independently confirming the reviewed
  "`F4,F5,F6` arbitrary, `c4,c6` arbitrary" cascade. The first genuine
  conditions appear at **row 7** (15 of them, on 30 variables).

**Bookkeeping after Theorem D.** The 495 equations of rows 4..21 become 293
divisibility/window conditions, of which 47 are vacuous, leaving **246
nonvacuous conditions on 96 raw parameters (`z`, `tt`, `F_4..F_14`) plus 5
scalars `c_*`** — before the endpoint.

---

## 5. The endpoint in closed form (the main new object)

Because there is **no `G22` slot**, `R_22 = G_22 - (3/2)H F_22 = 0`, so `D22`
is exactly the deficit of the ideal solution:

```text
D22 = - L_22(Phi_22),       Phi_22 := [t^22] ( sum_k c_{12-2k} t^(12-2k) W^k ).
```

and, since `L_22(R) = 2H[(12-22)H'R - 4HR']`,

```text
- L_22(R) * A  ==  8 * ( A^5 R )'          (verified for random R)
   i.e.   D22 = (8/A) * ( A^5 Phi_22 )'.
```

> **Theorem E (endpoint closed form).** For `K`-valued points satisfying rows
> `D4..D21 = 0`,
> ```text
> D22 = 1     <==>     A^5 * Phi_22  =  X^5/40 - X/8 + gamma      for some gamma in K,
> ```
> and, because `F_18 = 0` and `[t^10] 1 = 0`, the `c_4` and `c_12` modes drop out:
> ```text
> Phi_22 = (F^(3/2))_22 + c_6 (F^(3/4))_16 + c_8 (F^(1/2))_14 + c_10 (F^(1/4))_12.
> ```

Check of the integration constant: `8 * (X^5/40 - X/8 + gamma)' = X^4 - 1 = A`,
so `D22 = (8/A)(A^5 Phi_22)' = A/A = 1`, verified symbolically. **Eighteen
literal coefficient equations have become one functional identity with one
free scalar.**

> **Corollary E1 (the gamma obstruction — exact, cover-free).** Write
> `N = 40*(X^5/40 - X/8 + gamma) = X^5 - 5X + 40*gamma`. Then
> ```text
> N  =  X*A  +  (-4X + 40*gamma),        so     N mod A  =  -4X + 40*gamma  =/=  0
> ```
> for every `gamma` (the `X` coefficient is `-4`). Hence `A` never divides `N`,
> and for a root `rho` of `A`, `N(rho) = -4*rho + 40*gamma = 0` forces
> `gamma = rho/10`. For `gamma` in a field containing only `rho = +-1` among
> the fourth roots of unity — in particular for `gamma in Q` — at most **one**
> of the four roots can satisfy `N(rho) = 0`, and only when `gamma = +-1/10`.
>
> Therefore **at least three of the four roots `rho` of `A` satisfy
> `v_rho(Phi_22) = -5 exactly`.**

This is a hard, exact, branch-free necessary condition on the fixture. It is
the natural target of the exclusion program in §6. (Over `K = Q(i)` all four
roots are available, so the cover is: `gamma in {1/10, -1/10, i/10, -i/10}`
gives one exempt root; every other `gamma` exempts none. In all cases at least
three roots are pinned.)

---

## 6. Quadratic transport: an equivalent *polynomial* system

Square roots can be eliminated entirely. Put `Xi := G^2 - F^3` and

```text
E24(F, Y) := F_X * (24 - t d/dt) Y  +  Y_X * (t d/dt - 8) F.
```

> **Theorem F (transport).** `2 * G * E(F,G)  ==  E24(F, G^2 - F^3)`, identically.
> Verified symbolically in `t`-degrees 0..8 on the full fixture.

Since `G_0 = A^6` is a nonzerodivisor, the charged system is **exactly
equivalent** to

```text
E24(F, Xi) == 0  (mod t^22),        [t^22] E24(F, Xi) = 2 A^6,
```

with `Xi = G^2 - F^3` an explicit **cubic** polynomial in the raw variables and
no localization anywhere. Same-weight operator:

```text
Ltilde_n(Xi) = -8 A^(4+b_n) ( Xi * A^(-b_n) )',      b_n = (24-n)/2,
```

kernel `A^((24-n)/2)` for even `n <= 24`. The mode coefficients are
`e_m = sum_{k+l=m} c_k c_l`, so `e_0 = 0` and `e_2 = 2 c_2 = 0`. Verified
directly: **`Xi_0 = Xi_1 = Xi_2 = 0` identically** on the fixture.

In the special case `c_* = 0` this gives the compact statement

```text
G^2 == F^3 (mod t^22),     [t^22](G^2 - F^3) = -(1/20) * A * (X^5 - 5X - 20*delta).
```

This formulation is the recommended one for any machine lane: degree 3, no
denominators, no square roots, no localization.

---

## 7. Does the cutoff-five two-branch mechanism survive? — **It does not.**

Determined explicitly, as charged.

* **The linear prefix disappears.** The tail-5 packet's first move is an RREF
  of the linear prefix `D0..D9` (201 equations, rank 89, nullity 163). That
  prefix exists because rows `n <= 2*cutoff - 1 = 9` are linear in variables of
  weight `>= 5`. At cutoff two, `2*cutoff - 1 = 3 < 4`, so **no charged row is
  linear**: every one of `D4..D22` is genuinely quadratic. The census confirms
  it — the frozen row-4 generator already contains `(3/8) z_0 z_1`. "Prefix
  rank / prefix nullity / prefix lift" have no cutoff-two analogue, so
  `b = F7[X^0] plus its forced prefix G lift` is not a cutoff-two object.
* **The radical cascade changes shape.** The tail-5 cascade
  (`D10: F5^2 = 0 mod H => F5 = C*B`, `D11: B^2 = 0 mod C => B = C*V`, ...) is
  driven by `F_5` being the lowest surviving slot with `F_1..F_4` truncated
  away. At cutoff two `F_1 = A^2` and `F_2 = (1 + A^2 Z)/4` are present and
  `F_2(rho) = 1/4 =/= 0` at every root of `A`. The Newton polygon of `F` in
  `(t, lambda)` at a root therefore has vertices `(0,4), (1,2), (2,0)` — a
  single slope `-2` segment — and the correct cascade invariant is not a
  square-divisibility of `F_5` but the **Weierstrass discriminant**
  ```text
  disc = F_1^2 - 4 F_0 F_2 = A^4 - A^4 (1 + A^2 Z) = - A^6 Z,
  ```
  whose valuation is already `>= 6` where the generic value would be `4`. That
  automatic degeneracy *is* branch-P at cutoff two.
* **The scalar core does not transfer.** `E13, E14, E15, K17` and the branch
  variable `V0 = F5[X^0]` are defined by the cutoff-five prefix elimination;
  with no prefix they have no cutoff-two meaning. The `V0 = 0` / `V0 =/= 0`
  split is replaced by the branch data of §5: the four roots of `A` and the
  three-or-four-way `gamma` cover.
* **What does transfer, verbatim and re-derived here:** (i) the endpoint
  determinant `1 + a*b - c*d` with the same four carriers; (ii) the
  `F8[X^0]` additive gauge (`p129` there, `f_0_0` here). A **second** gauge
  `g_0_0 = G12[X^0]` appears at cutoff two.
* **Also determined:** the *lower-face* route is not cheap here. In the grading
  `deg X = -3`, `deg t = 1`, `F` has degree `<= 8`, `G` degree `<= 12`,
  `E` degree `<= 23`; the degree-23 part of `E` is entirely in rows `>= 23`
  (unconstrained), and the degree-22 part has **exactly one** constrained
  coefficient, which is precisely `f_1_0*g_0_1 - f_0_1*g_1_0 = 1` — matching
  the frozen row bit for bit. But that single equation already involves 14
  variables (`f_{a,0}, f_{a,1}, g_{a,0}, g_{a,1}`), and the equation:variable
  ratio only worsens going down. A lower-face pin alone cannot exclude.

Summary answer: **the cutoff-five mechanism fails, not splits.** Its gauge
survives; its branch variable, its prefix, and its scalar core do not.

---

## 8. Ranked next-experiment plan

**#1 (desk, exact, highest value): close the pole-order theorem.**

Setup. Fix a root `rho` of `A` and work in `K(rho)[[lambda]]`, `lambda = A`
(a uniformizer, `A' (rho) = 4 rho^3 =/= 0`). By §7 the Newton polygon gives a
Weierstrass factorization `F = Q * V` with `Q = t^2 + beta t + alpha`,
`v(alpha) = 4`, `v(beta) >= 2`, `V` a unit. Substituting `t = lambda^2 tau`
turns `Q` into `lambda^4 * (tau - tau_1)(tau - tau_2)` with `v(tau_i) = 0`,
and the branch-P degeneracy is `v(tau_1 - tau_2) = v(epsilon) >= 1`. Then

```text
mode k contributes to Phi_n a term of lambda-order  24 - 3k - 2n ;
the dominant mode is k=6 (the U^3 term):  Phi_n = lambda^(6-2n) * c_n .
```

Facts already in hand:

```text
rows n <= 21 integral   =>  v(c_n) >= 2n - 6 ;  in particular v(c_21) >= 36
endpoint (Corollary E1) =>  v(c_22) = 33 exactly,  at >= 3 of the 4 roots.
```

Because `[(tau-tau_1)(tau-tau_2)]^(3/2) = sum_k binom(3/2,k)(-epsilon)^k (tau-tau_2)^(3-k)`
and the `k >= 4` terms are the only infinite ones, the *heuristic* order of
`c_n` is `4*v(epsilon)`, **independent of `n`**. If that is made exact (a
uniform lower bound `v(c_22) >= v(c_21) - delta` with `delta < 3`), then
`v(c_21) >= 36` forces `v(c_22) >= 34 > 33` and the fixture is **excluded**.

Deliverable: a proof or refutation of

```text
  (INEQ)   v_rho(c_22)  >=  v_rho(c_21) - 2      for all K-points of rows 4..21,
```

uniformly at each root, with the sub-modes `k = 1,2,3,4` handled by their own
`lambda^(24-3k-2n)` scalings and with `V^(k/4)` handled by a unit expansion.
This is pure desk algebra in one variable over a complete DVR; it should not
need a machine. It would also explain the cutoff-7/6/5 cascade uniformly:
each cutoff is the same "row 21 integrality outruns the row 22 pole budget"
count with a shifted polygon.

**#2 (desk/laptop, exact): substituted triangular cascade.**
The *unsubstituted* cascade run in this session reaches row 15 in 170 s, with
the largest carried condition growing `118, 438, 1072, 2528, 5548, 11724,
24373, 49680, 100600` terms at rows `7..15` — a clean factor `~2` per row, so
rows 16..21 would cost hours and many GB. The blow-up is entirely because the
compatibility conditions are *carried* rather than *imposed*. Impose them:
row 7 gives 15 conditions on 30 variables; solve and back-substitute before
row 8. Exact rationals, standard library. Expected to collapse `z, tt,
F_4..F_6` immediately. Cheap; do it before anything heavy.

**#3 (desk, exact): the `Xi` lane.** Redo #2 in the §6 formulation
(`Xi = G^2 - F^3`, `E24`). No denominators, no roots, degree 3, and
`Xi_0 = Xi_1 = Xi_2 = 0` for free. Different engine, same fixture — a genuine
algorithm-diversity control on #2.

**#4 (only if #1..#3 stall) — AWS specification, not a launch.**

```text
target      : NEW immutable namespace
              cases/ggv_8_28_upper_endpoint_tail2_xi_saturation_20260829/
              (must not exist; runner fails closed if it does)
input       : XI_SYSTEM.json compiled by #3, its own SHA-256 recorded in the
              manifest, plus the two pins above
node        : pinned Box03 r6i.16xlarge identity; fail closed otherwise
lanes       : (a) exact-Q  std/lp  saturation of the Xi ideal by A
              (b) exact-Q  slimgb/dp on the same generators (diversity control)
              lanes are separate processes; no shared output namespace
order       : eliminate G-slots by weight, high n first (they are linear in Ltilde_n)
caps        : one global 6 h wall cap; per-lane VM cap 280 GiB, 1 core;
              at launch >= 150 GiB host headroom and zero swap; /usr/bin/time -v
stop markers: STOP-A  a printed exact-Q unit certificate with cofactors
              STOP-B  a printed exact-Q point with all 96+5 coordinates
              STOP-C  wall cap reached  -> NO RESULT (not negative evidence)
              STOP-D  VM cap reached    -> NO RESULT
promotion   : none from this job alone; exact-Q bytes + independent raw replay
              of all 513 literal generators required
```

Modular shards remain discovery-only and are not evidence either way.

---

## 9. Mutation and falsifier design

Any replay of this report must reject all of the following.

| # | mutation | must do |
|---|---|---|
| M1 | frozen: target `D22=0` keeping a positive witness | **must PASS** — the separator `U=A^2+t/2` with any `c_4,c_8,c_12` is a live witness (replayed here); closed form becomes `A^5 Phi_22 = gamma`, `gamma=0` |
| M2 | frozen: add `1` to the constant coefficient of `D21` | must break the cascade at row 21 |
| M3 | frozen: admit a synthetic constant `G22` slot | must change `L_22`; Theorem E's closed form then becomes solvable — forbidden in the charged system |
| M4 | frozen: replace `F1=H` by a `q1`-image vector | out of scope for this report; not used in any claim here |
| M5 | new: drop the `c_2 = 0` pin | mode count `5 -> 6`, `Xi_2 = 2 c_2 A^11 =/= 0`; §6's `Xi_2 = 0` check must fail |
| M6 | new: perturb the endpoint antiderivative, e.g. `X^5/40 - X/8 + X^2 + gamma` | `8 N' = A` must fail |
| M7 | new: target `D22 = -1` | closed form `A^5 Phi_22 = -(X^5/40 - X/8) + gamma`; Corollary E1 must still bite, with `N(rho) = 4 rho + 40 gamma` |
| M8 | new: delete the `(i-8)` factor at `i=8` | the `f_0_0` gauge of §2 must disappear |
| M9 | new: claim `ker L_n =/= 0` at an odd `n` | the exact RREF kernel census must return `0` at `n=5,7,9,11` |
| M10 | new: replace `A = X^4-1` by a non-squarefree quartic | §0's squarefreeness firewall is then violated; every §5 pole statement must be withdrawn |

Live regressions actually run in this session: M1 (passes, as required), M6
(fails, as required), M9 (kernel `0` at every odd row), plus the term-by-term
diff of §1 and the `-L_22(R)*A == 8(A^5 R)'` random-`R` check.

---

## 10. Replay recipe

All of it is standard-library Python 3 with `fractions.Fraction`; total
runtime for everything in §1--§6 is under 30 seconds on a laptop.

```text
1. hash-check RAW_DIRECT_SYSTEM.json against
   ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
2. represent a polynomial in X and the 303 raw variables as
   dict[(xdeg, sorted-tuple-of-varnames)] -> Fraction
3. build A, H, F0..F3, G0..G3 as in §1 ; build F4..F14, G4..G21 from
   RAW_DIRECT_SYSTEM.json["windows"] using slot name -> X-degree = first index
4. Drow(n) = sum_{i+j=n} (12-j)*F_i'*G_j + (i-8)*F_i*G_j'
5. DIFF: for n=0..22 compare Drow(n) coefficientwise against the frozen
   generators grouped by (row, x_degree).  Expect: identical for n<=21,
   and row 22 x_degree 0 differs by exactly the constant -1.
6. GAUGE: scan all 513 generators for variables that never occur -> {f_0_0, g_0_0}
7. ABSORPTION: R_n = G_n - (3/2) H F_n ; verify the §3 identity for n=1..22
8. KERNEL CENSUS: for each n, build the (40-n) x dim(G_n window) matrix of
   G_n coefficients from the frozen row and take its exact RREF; the kernel
   dimension must be 1 at n=4,6,8,10,12 and 0 elsewhere; the number of
   compatibility conditions must be (40-n) - rank
9. POSITIVE CONTROL: set all 303 variables to 0, then add
   G4 += c4*A^4, G5 += c4*A^2, G6 += c4/4, G8 += c8*A^2, G9 += c8/2, G12 += c12
   (writing a polynomial into slots via g_a_b with b = 12+3a-n).
   Evaluate all 513 generators: every one must be 0 except row 22 x_degree 0,
   which must be -1 (i.e. D22 = 0).
10. ENDPOINT: verify  -L_22(R)*A == 8*(A^5*R)'  on random R, and 8*N' == A
    for N = X^5/40 - X/8 + gamma
11. TRANSPORT: Xi_n = [t^n](G^2 - F^3); verify Xi_0=Xi_1=Xi_2=0 and
    2*sum_i G_i*D_{n-i} == sum_{i+j=n} (24-j)F_i'Xi_j + (i-8)F_i Xi_j'
```

No step needs a CAS, a network, or more than a few hundred MB.

---

## 11. Status

**REDUCTION.**

Delivered and verified against the literal frozen source:

* an independent term-by-term reconstruction of all 513 generators (§1);
* two exact additive gauges, a cover-free scheme identity (§2);
* the `R_n` absorption identity making the system triangular, with `F_n`
  provably absent from `D_n` (§3);
* the complete five-mode general solution, replacing 495 equations by a
  divisibility system on 96 + 5 unknowns, with rows 4--6 proved vacuous and
  the first conditions located at row 7, and the condition census verified
  through row 15 (§4);
* **the endpoint closed form `A^5 Phi_22 = X^5/40 - X/8 + gamma`**, replacing
  the 18 row-22 equations, together with the exact `gamma` obstruction pinning
  `v_rho(Phi_22) = -5` at three or more of the four roots of `A` (§5);
* a square-root-free, localization-free quadratic transport reformulation (§6);
* an explicit determination that the cutoff-five two-branch mechanism fails at
  cutoff two, with the surviving and non-surviving items itemized (§7).

Not delivered: an exclusion, a witness, or a certificate. Inequality (INEQ) in
§8 is stated as a conjecture with a proof strategy, and is *not* claimed. No
promotion; different-model hostile review required before any of this is used
downstream.
