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

Both are unconditional degree-termination proofs on the review-corrected 7/7
system, over `C`, with `a b kappa != 0` and `eta != 0`. They rest on two new
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
Live-section closures obtained: EMPTY[G!=0, s=0] and EMPTY[G!=0, deg eta=0].
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

## 4. THEOREM T3 — the section `s=0` is empty

## 5. THEOREM T4 — the section `e=0` is empty

## 6. Residual: exact surviving windows for `e>=1`

## 7. Typed conclusion
