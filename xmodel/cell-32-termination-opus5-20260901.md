# CELL-32-TERMINATION: two sections of the live cell closed by degree termination

## 0. Integrity, scope, and typed verdict

Before mathematical inspection, `shasum -a 256` on the frozen `inputs` copies
returned

```text
86caf003268ddc40143daa68d439079dbd82d1dac41e1da93f33a661d52f96ac  cell-32-spec-sol56-20260901.md
8c859f60fa1447e51778dedb3135e7ca6b0bebd7e2fcb25c5b65cfee8bdf6743  one-cusp-a2-hostile-review-sol56-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

All three match the charge. Only those frozen copies were read. No CAS was run;
no literature was needed or fetched; no canonical ledger and no charged file was
edited; `jc2-lean` was not inspected. This report is the only file written.
Citations abbreviate the basenames as `spec` and `review`.

The charged spec's live-cell residue was
`OPEN[ETA-S-DEGREE-TERMINATION,G!=0]` (`spec:317-322`): the section `F=G=0` was
proved empty there, and no termination was obtained on the complement. This
report attacks that complement. Two of its sections close.

```text
THEOREM T3.  In the live section (G != 0), s = 0 is impossible.
THEOREM T4.  In the live section, deg eta = 0 is impossible.
```

A third, T5 in Section 6, removes `r' = 0` up to one wall window. These are
unconditional degree-termination proofs on the review-corrected 7/7 system, over `C`, with `a b kappa != 0` and `eta != 0`. They rest on two new
structural identities that hold on the whole live section:

```text
THEOREM T1.  O2 has the unique solution C1 = (3a/2b)[(Z eta)'s + sG/(2b eta)];
             in particular eta | sG.
THEOREM T2.  E3 is equivalent to  Z^2 * Xi = (3a/b) * (Z eta^2 G^2)' / eta,
             with Xi displayed in Section 3.
```

The typed verdict is

```text
OPEN[A2-CELL-32].
Live-section closures obtained: EMPTY[G!=0, s=0], EMPTY[G!=0, deg eta=0],
and EMPTY[G!=0, r'=0] up to one explicit wall window (T5, Section 6).
Together with the charged EMPTY[F=G=0], any surviving pair has
G != 0, s != 0, deg eta >= 1.
No global termination in (deg eta, deg s, deg G) was obtained; no counterexample
witness was obtained.
```

Section 6 states exactly what survives and what the next pass must decide. No
boundary, flag, cover-series, attainment or exit-price assertion is made
anywhere in this report.

## 1. Conventions, the corrected system, and the shear normalization

Notation is the charged spec's (`spec:35-115`), taken over verbatim. Every prime
is `delta = d/dZ`; it is never a label and never `d/dV`. Work in `C[Z]`;
`deg 0 = -infinity`; `ord_Z` denotes the `Z`-adic order, with `ord 0 = +infinity`.
Constants `a,b,c5,kappa` have `a b kappa != 0`. The seven free polynomials are
`eta,s,p,C1,q,r,G` with `eta != 0`, and

```text
E2 = b Z eta^2,   D2 = a Z eta^3,   C2 = Z eta(3a s + c5 eta)/(2b),
E1 = E2' + G,     D1 = D2' + (3a/2b) eta G,
F  = D1 - D2' = (3a/2b) eta G,      G = E1 - E2'.
```

The seven residual equations `O0,O1,O2,E0,E1,E2,E3` are quoted from
`spec:76-114`; to avoid a name clash with the polynomial `E1` I write the last
three equations as `E1eq, E2eq, E3eq`. Throughout, `d := 3a/(2b)`,
`psi := (Z eta)' = eta + Z eta'`, `chi := eta + 2Z eta'`,
`phi := eta + 3Z eta'`, and

```text
e = deg eta,   sigma = deg s,   g = deg G,   m = deg q,   n = deg r,
epsilon = ord_Z eta,   nu = ord_Z G.
```

Leaders are `eta_e, s_sigma, G_g, q_m, r_n`. Note `deg psi = deg chi = deg phi = e`
with leaders `(1+e)eta_e, (1+2e)eta_e, (1+3e)eta_e`.

**Shear normalization, live section.** The residual affine shear `f -> f+lambda g`
fixes `g`, hence fixes `s, E_i, G`; it fixes `D_1,D_2` because `L1=L2=0`; it
fixes `kappa`; and it sends `c5 -> c5 + 2 lambda b^2` (`review:267-271`,
`spec:186-190`). The spec applies `lambda = -c5/(2b^2)` only inside its `G=0`
section. Nothing in that argument uses `G=0`: the shear moves `C1 -> C1+lambda E1`
and `C2 -> C2 + lambda b Z eta^2` and leaves the pair's cell and pole data
unchanged. Hence **`c5 = 0` may be assumed on the live section too**, and

```text
C2 = d Z eta s.
```

Every statement below is made under `c5 = 0`; the shear that achieves it is a
polynomial automorphism of the target, so emptiness statements transport back.

**`E0` as an identity.** `E0` reads `2(q r' - p' s) = kappa`. Wherever the
combination `4Z(q r' - p' s)` occurs (it occurs in `E1eq`) it may be replaced by
`2 kappa Z`. So

```text
E1eq:  6 D1 r' - 4q'E1 + 2q E1' + 4C1 s' - 2C1' s + 2 kappa Z = 0.        (1.1)
```

**Two operators.** For `Y in C[Z]` set

```text
M(Y)  = 2Z eta Y' -   eta Y - 4Z eta' Y,
M2(Y) = 2Z eta Y' -   eta Y - 2Z eta' Y.
```

If `Y != 0` has degree `k`, then `deg M(Y) = e+k` with leader
`eta_e Y_k (2k-1-4e)` and `deg M2(Y) = e+k` with leader `eta_e Y_k(2k-1-2e)`.
Both multipliers are odd integers, hence nonzero: **`M` and `M2` are injective on
`C[Z]`**. This is the review's termination multiplier (`review:245-250`) and the
spec's `L_eta` multiplier (`spec:160-166`) in one frame. Dually, if
`ord_Z Y = j` then the order-`e+j` coefficient of `M(Y)` carries the factor
`(2j-1-4e)` and that of `M2(Y)` the factor `(2j-1-2e)`: both nonzero. The
degree and order calculi are formally identical, because every expression below
is built from `Z`, `eta`, `G`, `s`, `q`, `r` and `d/dZ`, and both the leading and
the trailing coefficient are computed by the same Euler-operator eigenvalue with
`e,g,sigma,...` replaced by `epsilon,nu,...`. I use this **degree/order duality**
repeatedly and flag each use.

## 2. THEOREM T1 — `O2` solves exactly; the divisibility `eta | sG`

The spec factors `O2` only after setting `G=0` (`spec:192-205`). Carrying `G`
through gives a closed form on the whole live section.

**Step 1 (the `G`-free part).** With `C1 = d h`, `h0 := psi s`, `e0 := Z eta^2`,
direct collection reproduces the spec's factorization

```text
O2|_{G=0} = 6a[(h-h0) e0' - 2(h-h0)' e0] = -6a eta * M2(h-h0).
```

I verified this by expanding both sides in the basis
`{eta^3 s, Z eta^2 eta' s, Z^2 eta eta'^2 s, Z^2 eta^2 eta'' s, Z eta^3 s',
Z^2 eta^2 eta' s'}`; both sides equal

```text
-3 eta^3 s + 3Z eta^2 eta' s - 6Z^2 eta eta'^2 s + 6Z^2 eta^2 eta'' s
+ 6Z eta^3 s' + 6Z^2 eta^2 eta' s'
```

times `2a`. So the charged display is confirmed, not merely quoted.

**Step 2 (the `G`-linear part).** The `G`-dependence of `O2` sits in `E1 = E2'+G`
and `D1 = D2'+d eta G` only. Substituting and using `C2 = d Z eta s`,

```text
Delta2(G) := O2 - O2|_{G=0}
 = 8C2 G' - 4C2' G + 2 d eta s G + 8 d Z eta s' G - 4 d Z (eta G)' s
 = 2d[ 2Z eta s G' - eta s G - 4Z eta' s G + 2Z eta s' G ]
 = (3a/b) * M(sG),
```

the last equality because `M(sG) = s M(G) + 2Z eta s' G` by the Leibniz rule.

**Step 3 (exact solution).** Hence

```text
O2  <==>  2b eta * M2(h-h0) = M(sG).                                   (2.1)
```

Put `Psi := sG`. If `eta` divides `Psi`, then `u := Psi/(2b eta)` satisfies

```text
2b eta M2(u) = 2[Z eta Psi' - 2Z eta' Psi] - eta Psi = M(Psi),
```

by direct differentiation of the quotient. Since `M2` is injective, `u` is the
only solution of (2.1), and it is a polynomial only if `eta | Psi`. Therefore:

> **THEOREM T1.** On the live section, `O2` is equivalent to the conjunction of
>
> ```text
> eta | sG          and          C1 = d[ psi s + sG/(2b eta) ].
> ```
>
> In particular `C1` is not a free polynomial: the corrected model has five free
> polynomials `eta, s, p, q, r` and the one live deviation `G`, against six
> residual equations `O0, O1, E0, E1eq, E2eq, E3eq`.

Two remarks. First, T1 specializes at `G=0` to the spec's `(2.1)`
`C1=(3a/2b)(Z eta)'s` (`spec:205-209`), so it is a strict strengthening.
Second, T1 supersedes the spec's four-family `O2` degree table
(`spec:166-186`): that table read off `deg C1 = deg Rem2 - 2e` away from the
walls `sigma=e`, `g=2e`; T1 gives instead, for `s != 0`,

```text
deg C1 = max(e+sigma, sigma+g-e),
```

with equality failing only on the single wall `g=2e` **and** the pinned
coincidence `G_{2e} = -2b(e+1)eta_e^2`. Writing `Phi := sG/eta` (a polynomial by
T1, of degree `sigma+g-e` and order `>= sigma+nu-epsilon`) the closed form is

```text
C1 = d psi s + (d/2b) Phi.                                             (2.2)
```

`Phi` is the only place where the live deviation enters `C1`, and every
subsequent degree count uses (2.2) rather than a cap.

## 3. THEOREM T2 — the `E3` normal form and its three laws

`E3` is the top even equation and the analogue of `O2`. Collecting it the same
way — split `D1 = D2' + F`, `E1 = E2' + G` with `F = d eta G`, substitute
`E2 = bZeta^2`, `D2 = aZeta^3`, `C2 = dZ eta s` — produces massive cancellation.

**`G`-free part.** Every surviving monomial carries `Z^2`:

```text
E3|_{G=0} = Z^2 [ 12ab eta^3 eta'(eta' + 2Z eta'')
                 + 4d s(eta s' - eta' s)
                 + 8b eta(q eta' - q' eta)
                 + 12a eta^3 r' ].
```

(The four groups come respectively from `6D2'E2''-4D2''E2'`-type terms, from the
`C1^{(0)},C2,s` block, from the `q` block, and from `12Z D2 r'`. In the first
group the coefficients of `Z eta^4 eta'`, `Z eta^4 eta''` and `Z^3 eta^2 eta'^3`
all cancel identically; only `12Z^2 eta^3 eta'^2 + 24Z^3 eta^3 eta' eta''`
survives. The spec's `e=0` corner display `4Z^2 I = 0` with
`I = 3A0 r' - 2B q' + t s s'` (`spec:220-226`) is the `eta' = 0` specialization,
which I used as a control.)

**`G`-part.** The `G`-linear terms again collapse:

```text
E3 - E3|_{G=0}
 = 12a Z^2 eta[(eta eta'' - eta'^2)G + eta eta' G']
   - (3a/b)[ eta G^2 + 2Z eta' G^2 + 2Z eta G G' ],
```

and the bracket in the last line is exactly `(Z eta^2 G^2)'/eta`. Hence:

> **THEOREM T2.** On the live section, `E3` is equivalent to
>
> ```text
> Z^2 * Xi = (3a/b) * (Z eta^2 G^2)' / eta,                            (3.1)
> ```
>
> equivalently `eta Z^2 Xi = (3a/b)(Z eta^2 G^2)'`, where
>
> ```text
> Xi = 12ab eta^3 eta'(eta'+2Z eta'')            (i)
>    +  4d s(eta s' - eta' s)                    (ii)
>    +  8b eta(q eta' - q' eta)                  (iii)
>    + 12a eta^3 r'                              (iv)
>    + 12a eta[(eta eta'' - eta'^2)G + eta eta' G'].   (v)
> ```

Since `a,b,eta,G` are nonzero the right side of (3.1) is nonzero, so `Xi != 0`.
Three laws follow.

**(L1) Degree law.** `deg[(Z eta^2 G^2)'/eta] = e + 2g` with leader
`(3a/b)(1+2e+2g) eta_e G_g^2`. Hence

```text
deg Xi = e + 2g - 2,   leader(Xi) = (3a/b)(1+2e+2g) eta_e G_g^2.       (3.2)
```

The five families have exact degrees and leaders

| family | degree | leader | present iff |
|---|---:|---|---|
| (i) | `5e-2` | `12ab e^2(2e-1) eta_e^5` | `e>=1` |
| (ii) | `2sigma+e-1` | `4d(sigma-e) eta_e s_sigma^2` | `s!=0, sigma!=e` |
| (iii) | `2e+m-1` | `8b(e-m) eta_e^2 q_m` | `q!=0, m!=e` |
| (iv) | `3e+n-1` | `12a n eta_e^3 r_n` | `r'!=0` |
| (v) | `3e+g-2` | `12a e(g-1) eta_e^3 G_g` | `e>=1, g!=1` |

Families (i) and (v) exceed, equal, or fall below the target `e+2g-2` according
as `g < 2e`, `g = 2e`, `g > 2e` — the same trichotomy for both. Family (ii) has
degree `= e+1 mod 2` while the target has degree `= e mod 2`: **(ii) can never
match the target and can never cancel against (i)**, whose degree is also
`= e mod 2`. This is the parity separation the spec used at `spec:255-262`, here
derived for the live section.

**(L2) Order law.** By degree/order duality applied to (3.1),
`ord[(Z eta^2 G^2)'/eta] = epsilon + 2nu` with lowest coefficient
`(3a/b)(1+2epsilon+2nu) eta~(0) G~(0)^2 != 0`, so

```text
ord Xi = epsilon + 2 nu - 2,   hence   epsilon + 2 nu >= 2.            (3.3)
```

Evaluating (3.1) at `Z=0` gives the weaker `eta(0) G(0)^2 = 0`; I re-derived
that independently by evaluating the raw `E3` at `Z=0`, where the coefficient of
`eta(0)^3 G(0)` cancels between `-2D1E1`, `6D1E2'` and `-4D2'E1` (using
`4bd = 6a`) leaving exactly `-2d eta(0)G(0)^2 = 0`. The two routes agree; (3.3)
is the sharper statement.

**(L3) Divisor law.** At any `z != 0` with `eta(z)G(z) = 0`,
`ord_z((Z eta^2 G^2)') = 2 ord_z(eta) + 2 ord_z(G) - 1`, so (3.1) gives

```text
ord_z(Xi) = ord_z(eta) + 2 ord_z(G) - 1.
```

Summing over the `N` distinct nonzero roots of `eta G` together with (3.3)
accounts for `e + 2g - 2 - N` of the `e+2g-2` zeros of `Xi`: `Xi` has exactly `N`
further zeros. This is a rigidity statement, not used below, but it is the exact
finite datum a later exact-computation pass should carry.

## 4. THEOREM T3 — the section `s=0` is empty

> **THEOREM T3.** There is no live solution (`G != 0`) with `s = 0`.

*Proof.* Assume `s=0`. Then `C2 = d Z eta s = 0`, `Phi = 0`, and T1 gives
`C1 = 0`. `O1` collapses to `-8 p' E2 = 0` with `E2 = bZeta^2 != 0`, so `p'=0`;
`O0` becomes vacuous. `E0` reads `2 q r' = kappa != 0`, so `q = q0` and `r' = rho`
are nonzero constants, `deg r = 1`, `q' = 0`, `kappa = 2 q0 rho`. Equation (1.1)
becomes

```text
3 rho D1 + q0 E1' + kappa Z = 0,                                       (4.1)
```

so `deg D1 <= max(deg E1 - 1, 1)`.

**Corner `e=0`.** Families (i),(ii),(iii),(v) of `Xi` all vanish (`eta'=0`,
`s=0`, `q'=0`), leaving `Xi = 12a rho eta_0^3`, a nonzero constant. Law (L1)
gives `0 = e+2g-2 = 2g-2`, so `g=1`; law (L2) with `epsilon=0` gives `nu>=1`, so
`G = G_1 Z` exactly. Writing `B=b eta_0^2`, `A0=a eta_0^3`, `t=d eta_0` and using
`6A0 = 4tB`, equation `E2eq` reduces to

```text
18 A0 rho Z + 2 q0 B + 2t G G' + 8t rho Z G + 4 q0 Z G' = 0,
```

whose `Z^2` coefficient is `8 t rho G_1 != 0`. Contradiction.

**`e >= 1`.** Here `D1 = a eta^2 phi + d eta G` has candidate degrees `3e` and
`e+g` with leaders `a(1+3e)eta_e^3` and `d eta_e G_g`; `E1 = b eta chi + G` has
candidate degrees `2e` and `g` with leaders `b(1+2e) eta_e^2` and `G_g`.

*If `g > 2e`*: `deg D1 = e+g`, `deg E1 = g`, and (4.1) forces
`e+g <= max(g-1,1)`, false for `e>=1`. *If `g < 2e`*: `deg D1 = 3e`,
`deg E1 = 2e`, and (4.1) forces `3e <= max(2e-1,1)`, false for `e>=1`.

*If `g = 2e`*: the two leaders can drop, but not both, since
`G_{2e} = -(2b/3)(1+3e)eta_e^2` (call it **Wall A**, killing `deg D1 = 3e`) and
`G_{2e} = -b(1+2e)eta_e^2` (**Wall B**, killing `deg E1 = 2e`) would force
`(2/3)(1+3e) = 1+2e`, i.e. `2/3 = 1`. With neither wall, (4.1) gives
`3e <= 2e-1`: false. Under Wall B, `deg D1 = 3e <= max(2e-2,1)`: false. So Wall A
holds, and then `deg E1 = 2e` with leader `b eta_e^2/3`.

Now apply (L1) with `g=2e`, so the target degree is `5e-2`. Families present:
(i) at `5e-2`, (v) at `5e-2`, (iii) at `2e-1` (with `m=0`), (iv) at `3e`
(with `n=1`). For `e >= 2` we have `5e-2 > 3e` and `5e-2 > 2e-1`, so (3.2) reads

```text
12a e(2e-1) eta_e^3 [ b e eta_e^2 + G_{2e} ] = (3a/b)(1+6e) eta_e G_{2e}^2.
```

Substituting Wall A, the left side is `-4ab e(2e-1)(3e+2) eta_e^5` and the right
is `(4ab/3)(1+6e)(1+3e)^2 eta_e^5`, so

```text
-3e(2e-1)(3e+2) = (1+6e)(1+3e)^2,  i.e.  72e^3 + 48e^2 + 6e + 1 = 0,
```

impossible for `e >= 1`. Only `e=1` remains, where `3e = 5e-2` and family (iv)
also reaches the top.

**Finish `e=1, g=2`, Wall A.** Write `eta = uZ+w` (`u != 0`),
`G = G_2Z^2+G_1Z+G_0`, `G_2 = -(8b/3)u^2`, `kappa_1 := bu^2+rho`,
`Lambda := kappa_1+G_2`. Then

```text
Xi = 12a[ kappa_1 eta^3 + u eta P2 ] + 8b q0 u eta,
P2 = eta G' - uG = u G_2 Z^2 + 2w G_2 Z + (w G_1 - u G_0),
```

with coefficients `Xi_3 = 12a u^3 Lambda`, `Xi_2 = 36a u^2 w Lambda`,
`Xi_1 = 12au[3w^2 kappa_1 + uwG_1 + 2w^2G_2 - u^2G_0] + 8b q0 u^2`.

1. (4.1) forces `deg D1 <= 1`. Its `Z^3` coefficient vanishes by Wall A; its
   `Z^2` coefficient is `9au^2w + d(uG_1+wG_2)`, and `dG_2 = -4au^2`, so
   `5au^2w + duG_1 = 0`, i.e. `G_1 = -(10b/3)uw`.
2. The right side of (3.1) is `(3a/b)[(3uZ+w)G^2 + 2Z eta G G']`. Divisibility by
   `Z^2` forces its `Z^0` and `Z^1` coefficients `wG_0^2` and
   `3uG_0^2+4wG_0G_1` to vanish, hence `G_0 = 0` (if `G_0!=0` then `w=0` and then
   `3uG_0^2=0`).
3. With `G_0=0`, the right side has `Z^5..Z^2` coefficients
   `7uG_2^2`, `12uG_1G_2+5wG_2^2`, `5uG_1^2+8wG_1G_2`, `3wG_1^2` times `(3a/b)`.
   Matching `Z^5` gives `Lambda = (112/9)bu^2`, i.e. `rho = (127/9)bu^2`. Matching
   `Z^4` gives `448 ab u^4 w = (1280/3) ab u^4 w`, hence `w = 0`.
4. `w=0` forces `G_1 = 0`, so `G = G_2Z^2` and `eta = uZ`. The right side is then
   `(3a/b)7uG_2^2 Z^5` alone, so its `Z^3` coefficient is `0`, while
   `Xi_1 = 8b q0 u^2`. Hence `q0 = 0`, contradicting `q0 != 0`. QED

Consequently every live pair has `s != 0`, so `C2 != 0` and, by T1,
`Phi = sG/eta` is a nonzero polynomial. The charged spec's `s=0` sub-branch
(`spec:228-236`) was established only inside `F=G=0`; T3 is its live-section
counterpart and does not follow from it.

## 5. THEOREM T4 — the section `e=0` is empty

> **THEOREM T4.** There is no live solution with `deg eta = 0`.

Put `eta = eta_0 != 0`, `B := b eta_0^2`, `A0 := a eta_0^3`, `t := d eta_0`,
`mu := t/(2B)`. The scalar identities used below are

```text
B t = (3/2) A0,      A0/B = (2/3) t,      t^2/A0 = 3 mu.
```

By T3, `s != 0`. T1 gives `C1 = t s + mu s G` (the divisibility is vacuous at
`e=0`). Set `I := 3A0 r' - 2B q' + t s s'`.

**5.1 The three working equations.** Substituting into `E3eq`, `E1eq` (in the
form (1.1)) and `E2eq` and using `6A0 = 4tB`:

```text
E3d:  2 Z^2 I = t (Z G^2)'.
E1d:  I + 3tGr' - 2q'G + qG' + mu s(s'G - sG') + kappa Z = 0.
E2d:  6ZI + 2Bq + 8tZGr' - 4Zq'G + 4ZqG' + 2tGG' - 2 mu s^2 L(G) = 0,
      L(G) := 2ZG' - G.
K1 := (E2d - 6Z*E1d)/2:
      Bq - 5tZGr' + 4Zq'G - ZqG' + tGG' + mu s^2 G + mu Z s^2 G'
      - 3 mu Z s s' G - 3 kappa Z^2 = 0.
```

`E3d` is (3.1) at `e=0` (there `Xi = 4I`), and I cross-checked it against the
spec's `e=0` display `4Z^2 I = 0` (`spec:220-226`), which is the `G=0`
specialization. From `E3d`, `ord_Z(G^2+2ZGG') = 2 nu` exactly, so `nu >= 1`
(this is (L2) with `epsilon = 0`), and

```text
deg I = 2g-2,    leader(I) = t(1+2g) G_g^2 / 2,    g >= 1.            (5.1)
```

Evaluating `E2d` at `Z=0` (all terms carry `Z`, `G` or `L(G)`, and
`G(0)=L(G)(0)=0`) gives `2Bq(0)=0`, so `Z | q`. Evaluating `E0` at `Z=0` then
gives `-2p'(0)s(0) = kappa != 0`, so `s(0) != 0`. (A further `[Z^1]` expansion of
`E1d` gives `nu <= 2`, but the proof below does not need it.)

**5.2 The three top-degree relations.** Write `Mx := max(m, n, 2 sigma)`, with
the `n`-family absent when `r'=0` and the `m`-family absent when `q=0`; the
`sigma`-family always carries a factor `sigma`, so `sigma=0` contributes nothing
to `I`. Since `deg I <= Mx - 1`, (5.1) forces

```text
Mx >= 2g - 1.                                                          (5.2)
```

Comparing degrees inside `E1d` and `K1` — the `I` family sits at `2g-2`, the
`tGG'` family at `2g-1`, the `kappa` families at degree `1` resp. `2`, and
`Bq` at `m < m+g` — the strict maxima are `g-1+Mx` in `E1d` and `g+Mx` in `K1`
whenever `Mx >= 2`, because `Mx >= 2g-1 > g-1`. Reading off the three top
coefficients (and dividing `E1d`,`K1` by `G_g`):

```text
(E3top) [n=Mx] 3A0 n r_n - [m=Mx] 2B m q_m + [2sigma=Mx] t sigma s_sigma^2
        =  t(1+2g)G_g^2/2   if Mx = 2g-1,      =  0   if Mx >= 2g;
(E1top) [n=Mx] 3t n r_n + [m=Mx] (g-2m) q_m + [2sigma=Mx] mu s_sigma^2(sigma-g) = 0;
(K1top) [m=Mx] (4m-g) q_m - [n=Mx] 5t n r_n + [2sigma=Mx] mu s_sigma^2(1+g-3sigma) = 0.
```

**5.3 `Mx = 2g-1`.** This is odd, so `2sigma != Mx`; only `m` and/or `n` are
active. If only `n`: `(K1top)` gives `-5t(2g-1) r_n = 0`, so `r_n = 0`, false.
If only `m`: `(K1top)` gives `(4m-g)q_m = 0` with `q_m != 0` (forced by
`(E3top)`, whose right side is nonzero), so `4(2g-1) = g`, i.e. `7g = 4`: not an
integer. If both, `(E1top)` gives `(2Mx-g)q_m = 3tMx r_n`, i.e.
`q_m = 3t(2g-1)r_n/(3g-2)`, and `(K1top)` gives `(7g-4)q_m = 5t(2g-1)r_n`;
eliminating `q_m` (legitimate: `r_n != 0`, `2g-1 != 0`, `3g-2 != 0`) yields
`3(7g-4) = 5(3g-2)`, i.e. `6g = 2`, `g = 1/3`. Not an integer. All three
sub-cases die.

**5.4 `Mx >= 2g`.** Now `(E3top)` is homogeneous, and the three relations are a
homogeneous linear system in the leaders. Singles: `n` alone gives
`3A0 Mx r_n = 0`; `m` alone gives `2B Mx q_m = 0`; `2sigma` alone gives
`t sigma s_sigma^2 = 0` with `sigma = Mx/2 >= g >= 1`. All false. Pairs:

* `{m,n}`: `(E3top)` gives `3A0 r_n = 2B q_m`, i.e. `q_m = t r_n`; then
  `(K1top)` gives `4Mx - g = 5Mx`, i.e. `Mx = -g`. False.
* `{m,2sigma}` (`sigma = Mx/2`): `(E3top)` gives `q_m = mu s_sigma^2/2`; then
  `(K1top)` gives `(4Mx-g)/2 + 1 + g - 3Mx/2 = 0`, i.e. `Mx/2 + g/2 + 1 = 0`.
  False.
* `{n,2sigma}`: `(E3top)` gives `3A0 r_n = -t s_sigma^2/2`; then `(K1top)`, using
  `t^2/A0 = 3mu`, gives `mu(Mx + 1 + g) = 0`. False.

All three: set `X = t r_n`, `Y = q_m`, `W = mu s_sigma^2`, `M = Mx`,
`sigma = M/2`. Dividing `(E3top)` by `MB` and using `A0/B = (2/3)t`,
`mu = t/(2B)`, the system is

```text
   2 X  -   2 Y   +          W        = 0
 3M X  + (g-2M) Y + (M/2 - g) W       = 0
-5M X  + (4M-g) Y + (1+g-3M/2) W      = 0
```

with determinant `2[(g+gM-2M+M^2)] + 2[(3M-2gM-2M^2)] + [2M^2+2gM] = 2(g+M)`,
which is nonzero because `g >= 1` and `M >= 2`. Hence `X=Y=W=0`, contradicting
`r_n != 0`. Every `Mx >= 2g` configuration dies.

**5.5 The residue `Mx = 1`.** By (5.2) this occurs only for `g = 1`, and then
`1 <= nu <= g` forces `G = G_1 Z`, `sigma = 0`, `m <= 1`, `n <= 1`; with `Z|q`,
`q = q_1 Z` and `r = r_0 + r_1 Z`, `s = s_0 != 0`. `E3d` gives
`I = (3t/2)G_1^2`. `E0` gives `2 s_0 p' = 2q_1 r_1 Z - kappa`. Substituting into
`O0` and clearing `2s_0`:

```text
8t s_0^2 r_1 + 4t s_0^2 r_1 G_1 Z/B - 4(B+G_1Z)(2q_1r_1Z - kappa) - 4q_1 s_0^2 = 0.
```

Its `Z^2` coefficient is `-8 q_1 r_1 G_1`, so `q_1 r_1 = 0`. If `r_1 = 0` the
`Z^1` coefficient reduces to `4 kappa G_1 = 0`: false. If `q_1 = 0` the `Z^1` and
`Z^0` coefficients give `kappa = -t s_0^2 r_1/B` and `kappa = -2t s_0^2 r_1/B`,
forcing `r_1 = 0` and `kappa = 0`: false.

Sections 5.3–5.5 exhaust `Mx`, so `e = 0` is empty. QED

T4 is also what removes `e=0` from the `r'=0` analysis of Theorem T5 below.

## 6. Residual: exact surviving windows for `e>=1`

After T1–T4 and the charged `EMPTY[F=G=0]`, a surviving pair must satisfy

```text
G != 0,   s != 0,   e = deg eta >= 1,   eta | sG,
epsilon + 2 nu >= 2,   deg Xi = e+2g-2 with the pinned leader (3.2),
ord Xi = epsilon + 2 nu - 2.
```

The three chambers of (L1) are separated by `g` against `2e`, and in each the
`Xi` balance is one explicit algebraic relation, never a cap.

**Chamber III, `0 <= g < 2e`.** Family (i) sits strictly above (v) and strictly
above the target, and (ii) has the opposite parity, so (i) must be cancelled by
(iii) or (iv). Hence

```text
deg q = 3e-1   or   deg r = 2e-1   (or both),
```

and, dividing the degree-`5e-2` balance by `4b(2e-1) != 0`,

```text
3a e^2 eta_e^5 - 2 eta_e^2 q_{3e-1}[m=3e-1] + 3(a/b) eta_e^3 r_{2e-1}[n=2e-1] = 0.
```

If `deg q = e` the family (iii) leader vanishes and its degree drops to at most
`3e-2 < 5e-2`; then no family reaches `5e-2` at all, which is already a
contradiction — so `deg q != e` in this chamber. Family (v) also sits above the
target here (`3e+g-2 > e+2g-2` iff `g < 2e`), so there is a **second** balance,
at degree `3e+g-2`, which for `g >= 2` reads

```text
12a e(g-1) eta_e^3 G_g + 4d(sigma-e) eta_e s_sigma^2 [2sigma = 2e+g-1]
 + 8b(e-m) eta_e^2 q_m [m = e+g-1] + 12a(g-1) eta_e^3 r_{g-1} [n = g-1] = 0,
```

the `s` term occurring only when `g` is odd. For `g = 1` the (v) leader vanishes
and the constraint is absent.

**Chamber II, `g = 2e`.** Families (i) and (v) both sit at the target `5e-2`
with combined leader `12a e(2e-1) eta_e^3 [b e eta_e^2 + G_{2e}]`, and (ii) can
never reach it (`sigma = 2e - 1/2` is not an integer). The balance is

```text
12a e(2e-1) eta_e^3 [b e eta_e^2 + G_{2e}]
 + 8b(1-2e) eta_e^2 q_{3e-1}[m=3e-1] + 12a(2e-1) eta_e^3 r_{2e-1}[n=2e-1]
 = (3a/b)(1+6e) eta_e G_{2e}^2.
```

With `s=0` this collapses to `72e^3+48e^2+6e+1 = 0` (Section 4); with `s != 0`
the `q,r` terms are free and it does not close.

**Chamber I, `g > 2e`.** Families (i), (v) and (ii) all sit strictly below the
target, so (iii) or (iv) must supply it. Two consequences:

* `deg q != e` (same vanished-leader argument as in Chamber III), and
* `max(2e+m-1, 3e+n-1) = e+2g-2`, i.e. `m = 2g-e-1` or `n = 2g-2e-1`, with the
  degree-`(e+2g-2)` leaders summing to `(3a/b)(1+2e+2g) eta_e G_g^2`.

**THEOREM T5 (the sub-section `r' = 0`).** `r' = 0` is impossible except
possibly in Chamber II under the `E1`-wall, with `E1 != 0`.

*Proof.* `E0` forces `p's = -kappa/2`, a nonzero constant, so `s = s_0` and `p'`
are nonzero constants, `sigma = 0`, `deg p = 1`. The spec's (2.2) — which I
re-derived from `O0` and `E0` alone, `2(sC1-qE1)r' + kappa E1 + q s s' - q' s^2 = 0`
(`spec:277-279`) — reduces to `kappa E1 = q' s_0^2`. Substituting
`E1 = (s_0^2/kappa) q'` and `s'=0` into (1.1) gives the Wronskian form

```text
(s_0^2/kappa)[ q q'' - 2 q'^2 ] - s_0 C1' + kappa Z = 0.               (6.1)
```

If `deg q = m >= 1`, the bracket has exact degree `2m-2` and leader
`-m(m+1) q_m^2 != 0`. By T1, `C1 = d[s_0 psi + Phi/(2b)]` with
`deg Phi = g-e`, so `deg C1 <= max(e, g-e)` and `deg C1' <= max(e,g-e)-1`.
Now `deg E1 = m-1`, and:

* Chamber I (`g>2e`): `deg E1 = g`, so `m = g+1` and the bracket has degree
  `2g`, while the rest of (6.1) has degree at most `max(g-e-1,1) < 2g`.
* Chamber III (`g<2e`) and Chamber II off the wall: `deg E1 = 2e`, so
  `m = 2e+1` and the bracket has degree `4e`, while the rest has degree at most
  `max(e-1,1) < 4e` for `e >= 1`; `e=0` is T4.

Both are contradictions. Under the Chamber II `E1`-wall
`G_{2e} = -b(1+2e)eta_e^2` the `C1` leader survives (the two wall conditions
`(1+2e)` and `2(1+e)` differ), so `deg C1 = e` and (6.1) forces
`2 deg E1 <= max(e-1,1)`. The extreme case `E1 = 0` closes explicitly: then
`q' = 0`, `G = -b eta chi`, `Phi = -b s_0 chi`, `C1 = (d s_0/2) eta`, and (6.1)
gives `eta' = 2 kappa Z/(d s_0^2)`, i.e. `e = 2`, `eta = alpha Z^2 + beta` with
`alpha = kappa/(d s_0^2)`, `g = 4`, `G_4 = -5b alpha^2`. Then the `Xi` balance
(3.2) at degree `8` reads `-216 ab alpha^5 = 975 ab alpha^5`: false. QED

So the whole `r'=0` sub-section reduces to the window `g = 2e`,
`G_{2e} = -b(1+2e)eta_e^2`, `sigma = 0`, `E1 != 0`, `deg q = deg E1 + 1`, and
`2 deg E1 <= max(e-1,1)`: that is, `deg E1 = 0` with `e >= 1`, or
`1 <= deg E1 <= (e-1)/2` with `e >= 3`.

By T5 the three chamber discussions above may now assume `r' != 0`, so `n >= 1`
and family (iv) is present with exact degree `3e+n-1`.

**Assets handed to the successor.** The `e=0` kill worked because three
independent top-degree relations — from `E3`, from `E1eq`, and from the
combination `E2eq - 6Z*E1eq` — became a homogeneous `3x3` system in the leaders
`(t r_n, q_m, mu s_sigma^2)` with determinant `2(g+Mx) != 0`. The general-`e`
analogue needs the corresponding split of `E2eq`, which I computed and verified
(its `e=0` specialization reproduces `E2d` of Section 5.1 exactly):

```text
E2eq = E2eq|_{G=0} + Delta_2,

E2eq|_{G=0} = 6aZ eta^2(3 eta + 4Z eta') r'
  + 2b[ eta^2 q + 10Z eta eta' q + 4Z^2(eta'^2 + eta eta'')q
        - 6Z eta^2 q' - 4Z^2 eta eta' q' ]
  + 12ab Z eta^2 eta'[ eta eta' - Z eta'^2 + Z eta eta'' ]
  + 2dZ[ 3 eta s s' - 2(2 eta' + Z eta'') s^2 ],

Delta_2 = 6aZ eta^2 eta' G' + 6a eta[ eta eta' - 3Z eta'^2 + Z eta eta'' ] G
  + d[ eta (G^2)' - 4 eta' G^2 ] + 8dZ eta G r' + 4Z(q G' - q' G)
  + (d/b)[ Phi s + 2Z(Phi s' - Phi' s) ],      Phi = sG/eta.
```

The successor task is exactly: form the general-`e` `(E3top)`, `(E1top)`,
`(K1top)` from `Xi`, from (1.1), and from a `Z`-weighted combination of the two
displays above that kills the `I`-analogue; then test the resulting `3x3`
determinant chamber by chamber. If it is nonzero off a finite set of `(e,g)`,
cell `(3,2)` closes. That determinant is a desk computation, not a CAS run.

## 7. Typed conclusion

```text
OPEN[A2-CELL-32].

PROVED (new, live section G != 0, over C, a b kappa != 0, eta != 0):
  T1  O2 <=> [ eta | sG  and  C1 = (3a/2b)((Z eta)'s + sG/(2b eta)) ].
  T2  E3 <=> Z^2 Xi = (3a/b)(Z eta^2 G^2)'/eta, with Xi as displayed;
      hence deg Xi = e+2g-2 with pinned leader, ord Xi = epsilon+2nu-2,
      and epsilon + 2 nu >= 2.
  T3  EMPTY[G != 0, s = 0].
  T4  EMPTY[G != 0, deg eta = 0].
  T5  EMPTY[G != 0, r' = 0] except the single Chamber II wall window
      g=2e, G_{2e} = -b(1+2e)eta_e^2, sigma=0, E1 != 0,
      2 deg E1 <= max(e-1,1).

NOT PROVED:
  no global termination in (deg eta, deg s, deg G) on G != 0, s != 0, e >= 1.
  OBSTRUCTION[A-DEGREE-TWO] is therefore NOT completed; the horn's
  explicit-pullback programme does not advance a layer on this report.

NO WITNESS: no counterexample pair was constructed or approached.
```

The charged spec's live-cell residue `OPEN[ETA-S-DEGREE-TERMINATION,G!=0]` is
narrowed, not removed: three of its sections (`s=0`, `e=0`, and `r'=0` up to
one wall window) are gone. What changed is that the live section is now
**one-parameter rigid in `C1`** (T1) and carries **two independent scalar laws**
on `Xi` (T2), and that two of its four sections — `s=0` and `e=0` — are closed
by pure degree termination. The `e=0` proof is the template: the spiral does not
come from a single equation forcing `deg F, deg G` upward, but from the fact
that three different equations pin the *same three leading coefficients* and the
resulting homogeneous `3x3` system is nonsingular for every admissible
`(g, Mx)`. That is a termination contradiction of exactly the kind the charge
asked for, obtained at `e=0`; Section 6 states precisely what must be computed to
attempt it at `e >= 1`.

Nothing here uses a residue normal form, a companion curve, a boundary datum, a
cover series, a flag, or an exit price. No promotion is requested beyond T1–T5,
each of which is self-contained above. Every degree and order statement is
accompanied by its leader or trailing coefficient, and every place where a leader
could vanish is branched explicitly (Sections 4, 5.2, 6); no nominal degree is
reported as exact.

<!-- BODY-END -->
