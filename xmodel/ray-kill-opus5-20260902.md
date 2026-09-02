# RAY-KILL — deciding the last wall of the A2 horn

Lane: `RAY-KILL`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation + exact symbolic Laurent-coefficient algebra and one exact
Groebner decision (sympy 1.14.0 over `Q`, integer/rational only). No AWS, no
msolve, no `jc2-lean`, no literature fetched, no canonical ledger touched.
Drivers in `/tmp/raykill`, not installed in `box/`.

No `charge_basis` line: this report asserts no new exit price.

## 0. Custody, hashes, method

The three charged frozen copies were hashed with `shasum -a 256` **before any
was read**; all three match the charge exactly:

```text
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  horn-flagship-opus5-20260902.md
424e2f5ddec7189efa90c4259b19394ccee75e3eec4842ed1879544cb8fd7fd2  horn-flagship-review-grok46-20260902.md
d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b  cell-32-termination-opus5-20260901.md
```

Below: **HF** = the flagship, **HR** = its grok-4.6 hostile review, **C32** =
CELL-32-TERMINATION. No charged file was edited; no repository file other than
this report was written.

**Method.** Every polynomial is carried as a truncated Laurent series at
`Z = infinity`, `f = f_D Z^D + f_{D-1} Z^{D-1} + f_{D-2} Z^{D-2}`, the single
division `Phi = sG/eta` being a series inversion of the *actual* truncated
`eta`; coefficient extraction is exact rational arithmetic. Sec 3.7 is an exact
Groebner basis over `Q`, grevlex, with an explicit saturation variable. C32's
`T1`-`T5` remain UNREVIEWED producer input, consumed at their typing exactly as
HF and HR consume them.

## 1. Verdict, up front

```text
(1) THE RAY DOES NOT CLOSE.  It is cut, hard, at its boundary, and it is
    tightened everywhere else.  One order deeper than THEOREM HORN-A2:

    RAY-1  (structure).  The four order-(top-1) conditions are the explicit
      4x5 linear system (N3),(N1),(N4),(N2) of Sec 3.3, HOMOGENEOUS in the
      second coefficients except for one term rho carried by EQ3; rho != 0
      exactly on the boundary slice U = 3e.
    RAY-DEP  (PROVED).  n*(N1) + (n-2)*(N3) - (N4) = -(n-2)*rho identically.
      The four conditions have rank <= 3 and are solvable iff (n-2)*rho = 0.
    RAY-EDGE (PROVED e>=2, CAS e=1).  The whole boundary slice U = 3e is
      EMPTY.  For e >= 2 this is the rank obstruction with
      rho = -P(-(2e+1)) b^2 eta_e^4/((4e-2)s_s^2) != 0, P being HF's own
      Chamber-II polynomial.  The one degenerate cell n = 2, (e,U) = (1,3),
      is killed in Sec 3.7 by an exact Groebner decision (unit ideal).
    RAY-2  (deg E1 drops again).  On the surviving cells the next order
      forces  E1_{2e-1} = 0,  i.e.  deg E1 <= 2e - 2.

(2) EXACT RESIDUAL.  OPEN[A2-CELL-32-E1WALL] narrows to
       U >= 3e+2 ,  deg E1 <= 2e-2 ,  plus the second-order pins
       eta_{e-1}/eta_e = s_{s-1}/s_s - r_{n-1}/(2 r_n),
       q_{m-1}/q_m    = s_{s-1}/s_s + r_{n-1}/(2 r_n),
       G_{2e-1}       = -4 e b eta_e eta_{e-1},
    a 2-dimensional residual per cell.  Order (top-2) adds NOTHING there
    (10 cells, e <= 5): the order-by-order ladder does not terminate, and
    termination is a per-cell finiteness question.

(3) FINITENESS.  Per cell (e,U) the system is finite and massively
    overdetermined (equations - unknowns grows like 5U/2), hence decidable;
    (1,3) is decided here.  Per e it is NOT finite: U ranges over 3e+2,
    3e+4, ... unbounded, and the charged record bounds U nowhere.  New
    OPEN[A2-U-BOUND].  Job spec in Sec 4.

(4) LEDGER.  A ray kill would close ZERO (B3) windows.  The charge's premise
    "(B3)'s A2 route at the affected windows" is not supported by HF Sec 5,
    which states that the A2 and (B3) instruments act on different objects
    and do not compose.  What a ray kill closes is OPEN[A2-CELL-32] and one
    layer of OBSTRUCTION[A-DEGREE-TWO].  Sec 6 gives both ledgers.
```

## 2. Controls: the wall algebra replayed from scratch

Nothing below is consumed on trust; five control layers, all exact, all run
before any new claim was formed.

**(C1) C32's `e=0` identities.** HF's four controls (HF Sec 4.2) rebuilt here
from C32 Sec 5.1's own `I, E3d, E1d, E2d`, with `eta = eta_0` constant and
`s,q,r,G` arbitrary symbolic functions:

```text
   Xi  - 4I                              |_{e=0}  =  0
   EQ1 - 2*E1d                           |_{e=0}  =  0
   EQ2 -   E2d                           |_{e=0}  =  0
   EQ3 - 2*eta_0*(2Z^2 I - t (Z G^2)')   |_{e=0}  =  0
```

Four identities, four exact zeros — validating *my* transcription of `Xi`,
`(1.1)`, C32 Sec 6's `E2eq|_{G=0}`/`Delta_2` and `T2`, independently of HF's,
against the same C32 anchor.

**(C2) The general-`c` Chamber II rows.** With `c := G_{2e}/(b eta_e^2)` and
`x = a eta_e^3 r_n n`, `y = b eta_e^2 q_m`, `w = a eta_e s_sigma^2/b`, HF Sec 4.3's
three rows were recomputed at eight cells. Ratio to HF: `1` for EQ1 and EQ2, a
uniform `eta_e` for EQ3 (row normalisation). No monomial outside `{R,Q,S^2}`
occurred in any top coefficient — the rows really are linear in `(x,y,w)`.

**(C3) The determinant, the wall, the ray.**

```text
  det(EQ3,EQ1,EQ2) in Chamber II  =  36 n (c+2e)(c+2e+1) * eta_e   (ratio 1)
  Wall B rows      = [12,-8n,3n], [-3,0,3n/4], [6,2-4e-8n,3e+9n/2-3/2]
  rank 2, kernel   = (n/4, 3/4, 1)
  all four tops (EQ3,EQ1,EQ2 and the quadratic EQ4) vanish on the ray
```

verified at twelve cells `1 <= e <= 5`: HORN-A2 reproduced exactly, a third
independent replay after HR Sec 7.2.

**(C4) Sub-configurations on Wall B — supplied here, not in HF.** HF displays
the pair/single analysis at `c = -2e` but not at Wall B. There the `2x2` minors
of rows `(EQ3, EQ1)` are `{r,q}: -24n`, `{r,s}: 18n`, `{q,s}: -6n^2`, and the
EQ3 entries `12, -8n, 3n` are individually nonzero for `n >= 1`. So every pair
and every single configuration forces `x = y = w = 0` against `r_n != 0`:
**only the full simultaneous-top regime survives Wall B**, as HORN-A2 asserts.
The gap in its displayed argument is closed here.

**(C5) Which normalisations are legal.** Two scalings were verified exactly on
all five equations (`EQ1, EQ2, EQ3, EQ4, E0`) with `eta, s, q, r, G, p` treated
as arbitrary functions:

```text
 (S1)  a -> alp*a, b -> bet*b, s -> bet*s, q -> alp*q, r -> bet*r, G -> bet*G,
       p' -> alp*p', kappa -> alp*bet*kappa .        (all five residuals: 0)
 (S2)  eta -> mu*eta, s -> mu^2 s, q -> mu^3 q, r -> mu^2 r, G -> mu^2 G,
       p' -> mu^3 p', kappa -> mu^5 kappa .          (all five residuals: 0)
```

`(S1)` licenses `a = b = 1`; `(S2)` licenses `eta_e = 1`. A third, tempting
normalisation is **illegal**: there is no `Z -> lambda Z` symmetry. Writing
`W(M) = (#derivatives) - (power of Z)` for a monomial, covariance would need
each equation isobaric; but `EQ1` forces `W(kappa) = 2` (from `2 kappa Z`
against `6 D1 r'`) while `EQ4` forces `W(kappa) = 1` (from `kappa E1` against
`2 s C1 r'`). **Incompatible.** `s_sigma` may therefore NOT be normalised, and
the cell computations of Sec 3.7 and Sec 4 do not normalise it. (An earlier run
of this pass did; it was discarded.)

## 3. Task (1): one order deeper, on the wall itself

### 3.1 The wall in closed form

Wall B is `G_{2e} = -b(1+2e) eta_e^2`, equivalently `deg E1 <= 2e-1` for
`E1 = (b Z eta^2)' + G`. Treating `E1` rather than `G` as the free object makes
the whole live system collapse. With `psi = (Z eta)'`, `chi = eta + 2Z eta'`,
`phi = eta + 3Z eta'`, `d = 3a/2b` and `Theta := s E1/eta`:

```text
   G   = E1 - b(Z eta^2)'                                          (definition)
   D1  = -a eta^3 / 2 + d eta E1            [ since phi - (3/2)chi = -eta/2 ]
   Phi = s G/eta = -b s chi + Theta
   C1  = (d/2) ( s eta + Theta/b )          [ since psi - chi/2 = eta/2 ]
   T1's divisibility  eta | sG   <==>   eta | s E1 .
```

Two consequences. First, `deg D1 = 3e` with leader `-a eta_e^3/2` and
`deg C1 = e+sigma` with leader `d eta_e s_sigma/2`: both survive Wall B, so no
further branch hides there. Second, in these variables

```text
 EQ1 = -3a eta^3 r' + d s(s'eta - s eta')                     [E1-free, top]
       + 6d eta E1 r' - 4q'E1 + 2q E1' + (d/b)(2 Theta s' - s Theta')
       + 2 kappa Z ,
 EQ4 =  d s^2 eta r' + q s s' - q' s^2                        [E1-free, top]
       + (d/b) s Theta r' - 2 q E1 r' + kappa E1 ,
```

so **every** term of `EQ1` and of `EQ4` carries `r'`, `q` or `s`: neither
equation has a pure `eta/G` family. `EQ3` and `EQ2` do, at `u = 3e-1`.

### 3.2 The grading, and where the boundary is

With `m = U`, `n = U-e`, `2 sigma = U+e` (so `U ≡ e mod 2`, hence `n` even,
`n >= 2e`), every family of `EQ3` sits at degree `(3e+1)+u`, of `EQ1` at
`(2e-1)+u`, of `EQ2` at `2e+u`, with `u_r = u_q = u_s = U` and
`u_eta = u_G = u_T = 3e-1` in Chamber II. Because `U - 3e` is always even, the
`eta/G/target` families sit at

```text
   top - (U - 3e + 1) ,      an ODD offset:  top-1, top-3, top-5, ...
```

They therefore hit `top-1` **exactly when `U = 3e`**, and never hit `top-2`.
That single arithmetic fact organises everything below: the boundary slice
`U = 3e` is inhomogeneous at the next order, every other cell is homogeneous.

Each order-`(top-k)` coefficient is linear in the `k`-th coefficients of
`eta,s,q,r,G`, so at `k = 1` the only possible inhomogeneous term comes from a
family whose own top sits at `top-1`. On Wall B the `E1`-carrying families of
`EQ1` and `EQ4` do sit there, but contribute linearly in `E1_{2e-1}`, itself
linear in the second coefficients. Hence:

> **STRUCTURE.** For `U >= 3e+2` the order-`(top-1)` system is linear and
> **homogeneous**; it cannot be contradictory. For `U = 3e` it is
> inhomogeneous, and that is the only place a contradiction can live at this
> order.

This answers the charge's first disjunct with a reason rather than with a
failed search: away from the boundary slice, no next-order contradiction
exists, for structural reasons.

### 3.3 THEOREM RAY-1: the four next-order conditions

Put, on the ray,

```text
  alpha = eta_{e-1}/eta_e ,  beta = s_{sigma-1}/s_sigma ,  gamma = q_{m-1}/q_m ,
  delta = r_{n-1}/r_n ,      epshat = G_{2e-1}/(b eta_e^2) .
```

> **THEOREM RAY-1.** On Wall B in the simultaneous-top regime `U >= 3e`, the
> order-`(top-1)` coefficient conditions of `EQ3, EQ1, EQ2, EQ4` are exactly
>
> ```text
>  (N3)  beta - gamma + delta/2                                        = rho
>  (N1)  alpha - beta + delta/2                                        = 0
>  (N4)  n*alpha - 2*beta - (n-2)*gamma + (n-1)*delta                  = 0
>  (N2)  (2n-2e-3)alpha - 2(3n+2e-4)beta + (4n+2e-5)gamma
>                                     - (n-1)delta - epshat            = 0
> ```
> with
> ```text
>    rho = 0                                                if U >= 3e+2,
>    rho = (32e^3+32e^2+6e+1) b^2 eta_e^4 / ((4e-2) s_sigma^2)   if U = 3e.
> ```
> The normalising factors are `EQ3 = 6(n-1)(a/b) eta_e^2 s_sigma^2 * (N3)`,
> `EQ1 = -(3/2)(n-1)(a/b) eta_e s_sigma^2 * (N1)`,
> `EQ4 = (3a/8b^2)(s_sigma^4/eta_e) * (N4)`.

`(N1)`, `(N3)`, `(N4)` are **derived by hand** in the closed form of Sec 3.1
(the derivations are reproduced in Sec 3.4-3.5 in compressed form) and then
checked against the CAS at ten cells with the displayed normalising factors:
exact agreement, `rho` sign included. `(N2)` is **measured**: its closed form
was interpolated from the CAS and verified, together with `(N1),(N3),(N4)` and
`rho`, at all 50 cells `1 <= e <= 10`, `U in {3e, 3e+2, ..., 3e+8}`, with zero
mismatches. A wider 72-cell sweep (`1 <= e <= 12`, `U in {3e, ..., 3e+10}`)
confirms at every cell: `rank = 3`, kernel contained in `{E1_{2e-1} = 0}`,
`rho` as displayed, and consistency exactly when `U >= 3e+2`.

Two structural facts fall out of the hand derivations and deserve display,
because they are what makes the system rank-deficient.

* In `EQ1` the `E1_{2e-1}` contributions from `6d eta E1 r'`, `-4q'E1+2qE1'`
  and `(d/b)(2 Theta s' - s Theta')` sum, on the ray, to a multiple of
  `3(n + e - U) = 0`. **They cancel identically.**
* In `EQ4` the two `E1_{2e-1}` contributions, from `(d/b) s Theta r'` and from
  `-2 q E1 r'`, are exact negatives on the ray. **They cancel identically.**

So `epshat` occurs in `(N2)` only: the wall's own deviation is invisible to
three of the four conditions.

### 3.4 THEOREM RAY-DEP and the kill of the boundary slice

> **THEOREM RAY-DEP.** Identically in `(alpha,beta,gamma,delta,rho,n)`,
> ```text
>      n*(N1) + (n-2)*(N3) - (N4)  =  -(n-2)*rho .
> ```
> *Proof.* The `beta`-coefficient is `-n + (n-2) + 2 = 0`; the `gamma`
> coefficient is `-(n-2) + (n-2) = 0`; the `delta` coefficient is
> `n/2 + (n-2)/2 - (n-1) = 0`; `alpha` cancels between `n*(N1)` and `-(N4)`.
> The only survivor is `-(n-2) rho`. QED

> **THEOREM RAY-EDGE.** The boundary slice `U = 3e` of the E1-wall is EMPTY.
>
> *Proof for `e >= 2`.* At `U = 3e` one has `n = 2e >= 4`, so `n - 2 != 0`, and
> `rho != 0` because `32e^3+32e^2+6e+1 > 0` for `e >= 1`. By RAY-DEP the four
> next-order conditions are inconsistent. QED
>
> The remaining cell is `n = 2`. Since `n = U - e` and `U >= 3e` force
> `n >= 2e`, `n = 2` happens **only** at `(e,U) = (1,3)`, which is killed in
> Sec 3.7. QED

The obstruction `rho` is not a new quantity. Let
`P(c) := 4e^2(2e-1) + 4ce(2e-1) - c^2(6e+1)` be HF's own Chamber II
coincidence polynomial (HF Sec 4.4, `U < 3e-1` branch). Then

```text
   P(-(2e+1)) = -(32e^3 + 32e^2 + 6e + 1) ,
   rho        = -P(-(2e+1)) * b^2 eta_e^4 / ((4e-2) s_sigma^2) .
```

HR Sec 7.5 records `P(-(2e+1)) != 0` as the reason Wall B and the `U < 3e-1`
wall are different walls. **The same nonvanishing now kills the boundary slice
of Wall B itself**: the coincident `eta/G/target` families, which at `U = 3e`
sit one order below the top, contribute `P` at Wall B, and there is no
remaining freedom to absorb it.

*Derivation sketch for `(N3)`.* At `top-1`, `EQ3`'s `r,q,s` families give,
after the ray substitution and division by `a s_sigma^2 eta_e^2/b`, the columns
`alpha: 12n - 6(3n+1) + 6(n+1) = 0`, `beta: 6(n-1)`, `gamma: -6(n-1)`,
`delta: 3(n-1)`; so `EQ3|_{top-1} = 6(n-1)(a/b) eta_e^2 s_sigma^2 (beta - gamma
+ delta/2)` plus, when `U = 3e`, the coincident-family term
`3ab eta_e^6 P(-(2e+1))`. The vanishing `alpha` column is the source of the
rank drop.

### 3.5 THEOREM RAY-2: the wall tightens

> **THEOREM RAY-2.** On every surviving cell the next order forces
> ```text
>       E1_{2e-1} = 0 ,   i.e.   deg E1 <= 2e - 2 .
> ```
> *Proof.* `(N1)` and `(N3)` with `rho = 0` give `alpha = beta - delta/2` and
> `gamma = beta + delta/2`. Substituting into `(N2)`:
> the `beta` column is `(2n-2e-3) - 2(3n+2e-4) + (4n+2e-5) = -4e`, and the
> `delta` column is `-(2n-2e-3)/2 + (4n+2e-5)/2 - (n-1) = 2e`, so
> `epshat = -4e beta + 2e delta = -4e(beta - delta/2) = -4e alpha`. Since
> `E1_{2e-1} = b eta_e^2 (4e alpha + epshat)`, it vanishes. QED

At `e = 1` this says `deg E1 <= 0`: on the surviving `e = 1` cells `E1` is a
**constant**. (`RAY-2` inherits `(N2)`'s MEASURED typing; `(N1)`,`(N3)` are
hand-derived.)

### 3.6 The exact residual, and order `top-2`

For `U >= 3e+2` the next-order solution set is 2-dimensional, parametrised by
`(beta, delta)`:

```text
   eta_{e-1}/eta_e = beta - delta/2 ,      s_{sigma-1}/s_sigma = beta ,
   q_{m-1}/q_m     = beta + delta/2 ,      r_{n-1}/r_n         = delta ,
   G_{2e-1}        = -4 e b eta_e eta_{e-1} ,
```

i.e. `eta_{e-1}/eta_e + q_{m-1}/q_m = 2 s_{sigma-1}/s_sigma` and
`q_{m-1}/q_m - eta_{e-1}/eta_e = r_{n-1}/r_n`.

**Order `top-2`.** By Sec 3.2 no `eta/G/target` family reaches `top-2`, so the
order-`(top-2)` system is four conditions on the five third coefficients
`(eta_{e-2}, s_{sigma-2}, q_{m-2}, r_{n-2}, G_{2e-2})` with an inhomogeneity
quadratic in `(beta,delta)`. Computed with the next-order solution substituted:

```text
   U >= 3e+2  (10 cells, e <= 5): rank 3, and the augmented matrix has rank 3
                                  too, for ALL (beta,delta).
                                  ==> NO new condition.  Residual grows.
   (e,U) = (1,3):                 rank 2, cokernel of dimension 2, giving the
                                  single condition  426 eta_1^6 a b (2 beta - delta) = 0,
                                  i.e.  delta = 2 beta,  i.e.  alpha = 0,
                                  i.e.  eta = eta_1 Z .   (426 = 6 * 71 and
                                  71 = 32e^3+32e^2+6e+1 at e = 1.)
```

So the order-by-order ladder does **not** terminate on the surviving cells: four
conditions against five new unknowns per order, with the fifth unknown running
out only when a polynomial's coefficients are exhausted. Any further kill must
be a per-cell finiteness argument, not a further leading-order pass. That is
Task (2).

### 3.7 The degenerate cell `(e,U) = (1,3)`: EMPTY, exactly

`(1,3)` is the unique cell where `n = 2` and RAY-DEP is vacuous, and it is
small enough to decide outright: `e=1, sigma=2, m=3, n=2, g=2`, `deg Phi = 3`,
`deg p' = 2`; 22 unknowns after the legal normalisations `a = b = 1` (S1) and
`eta_e = 1` (S2), including `kappa` and one saturation variable. Generators:
the coefficientwise vanishing of

```text
   EQ1, EQ2, EQ3, EQ4 ,      T1 as  eta*Phi - s*G = 0  (Phi a new polynomial),
   E0  as  2(q r' - p' s) - kappa = 0 ,
   saturation  s_sigma * q_m * r_n * kappa * tt - 1 = 0 .
```

37 generators. Ideal component extracted as the sympy `GroebnerBasis` over
`Q[22 vars]`, grevlex.

```text
   RESULT.  The Groebner basis is [1].   The cell (1,3) is EMPTY.        2.2 s
   With the wall G_2 = -3 eta_1^2 NOT imposed (23 unknowns):  also [1].  13.2 s
```

The second run matters: `(1,3)` is empty independently of the wall derivation,
so this cell does not rest on HORN-A2 at all.

**Controls on the decision** (FALLACY-v2 `sat()` clause).

* *Ring and component.* Generators and basis both in `Q[a0,S0..S2,Q0..Q3,
  R0..R2,G0,G1,F0..F3,P0..P2,kappa,tt]`; the saturation is by the explicit
  variable `tt`, not by a `sat()` wrapper, so no ideal/list confusion can arise.
* *Negative control (planted solution).* The **identical** pipeline — same 37
  generators, same 22 variables, same call — run on the shifted family
  `g_i - g_i(pt)` for a random rational point `pt` with
  `s_sigma q_m r_n kappa != 0` and `tt = 1/(s_sigma q_m r_n kappa)`. The point
  was verified to be a zero of every shifted generator, and the basis is
  **not** `[1]`. So `[1]` is not an artifact of the pipeline.
* *Dropped-equation probe.* Removing `EQ1` still gives `[1]` (140 s): the kill
  does not hinge on one equation. Probes removing more than one equation did
  not terminate in budget and are reported as not run.
* *Engine.* Single engine (sympy 1.14.0). Per the charge's certainty
  discipline, `(1,3) EMPTY` is **not promotion-grade** until a second engine
  confirms it; it is in the Sec 4 job spec as item 0.

Combining Sec 3.4 and Sec 3.7: **the boundary slice `U = 3e` of the E1-wall is
EMPTY at every `e >= 1`**, with the `e >= 2` part PROVED and the `e = 1` part
single-engine CAS.

## 4. Task (2): is the residual finite, and can qqideal decide it?

**Per cell: yes, grossly overdetermined.** With `a = b = eta_e = 1` the cell
`(e,U)` has

```text
  unknowns  =  e + (sigma+1) + (m+1) + (n+1) + 2e + (sigma+e+1) + 3n/2 + 2
  equations =  (U+2e) + (U+2e+1) + (3e+U+2) + (2U+e) + (sigma+e+1) + (2U-e)
```

from `EQ1, EQ2, EQ3, EQ4`, `T1` and `E0` respectively (the `+2` is `kappa` and
the saturation variable). Measured sizes:

```text
   (e,U)   g  sigma  m   n    unknowns  equations  excess
   (1, 3)  2    2    3   2       22        37        15
   (1, 5)  2    3    5   4       31        52        21
   (1, 9)  2    5    9   8       49        82        33
   (2, 8)  4    5    8   6       47        84        37
   (3,11)  6    7   11   8       63       116        53
   (4,12)  8    8   12   8       70       133        63
   (5,15) 10   10   15  10       86       165        79
```

The excess grows like `5U/2 + 5e`, so on a naive dimension count every cell is
expected empty — an expectation, not a theorem, which is the point of the job
below.

**Per `e`: no.** The surviving `U` are `3e+2, 3e+4, ...` without bound, and
nothing in HF, HR or C32 bounds `U` in terms of `e`. This is the single
highest-value successor for the horn lane:

```text
OPEN[A2-U-BOUND].  Bound U (equivalently deg q, deg r, deg s) in terms of e on
the E1-wall.  Without it, no finite computation decides even one value of e.
```

### 4.1 Job spec `A2-E1WALL-CELLS` (for the coordinator; msolve + qqideal)

```text
NAME        A2-E1WALL-CELLS
GOAL        decide EMPTY / NONEMPTY for the residual cells of
            OPEN[A2-CELL-32-E1WALL] after RAY-EDGE and RAY-2.
RING        Q[x_1..x_V], grevlex, characteristic 0 for the decisive run.
GENERATORS  For a cell (e,U), U ≡ e (mod 2), U >= 3e+2: g=2e, m=U, n=U-e,
            sigma=(U+e)/2;  a = b = 1 by (S1);  eta = Z^e + sum_{i<e} A_i Z^i
            with A_e = 1 by (S2);  s,q,r,Phi,p' generic of degrees
            sigma, m, n, sigma+e, 3n/2-1;  G generic of degree g with
            G_g = -(1+2e) (wall, HORN-A2);  kappa free.
            Generators = all Z-coefficients of
              EQ1, EQ2, EQ3, EQ4        (displays: C32 (1.1); C32 Sec 6
                                         E2eq|_{G=0} + Delta_2; C32 T2
                                         eta Z^2 Xi - (3a/b)(Z eta^2 G^2)';
                                         C32 (2.2))
              eta*Phi - s*G             (T1)
              2(q r' - p' s) - kappa    (E0)
            plus the saturation  S_sigma * Q_m * R_n * kappa * tt - 1.
OPTIONAL    (accelerator; each is PROVED above, so adding them does not change
             the variety of the residual)
              4 R_n - S_sigma^2 ,            4 Q_m - 3 S_sigma^2 ,
              G_{g-1} + 4 e A_{e-1} ,                                 (RAY-2)
              2 S_sigma R_n A_{e-1} - (2 S_{sigma-1} R_n - S_sigma R_{n-1}),
              2 S_sigma R_n Q_{m-1} - Q_m (2 S_{sigma-1} R_n + S_sigma R_{n-1}).
DECISION    is 1 in the saturated ideal?
CELLS       item 0 (promotion gate):  (1,3)  [claimed EMPTY here, one engine]
            item 1: e=1, U=5,7,9,11,13    item 2: e=2, U=8,10,12
            item 3: e=3, U=11,13          item 4: e=4, U=14
ENGINES     msolve 0.10.1 over a large prime as the fast screen; qqideal over Q
            for the decisive answer.  A mod-p unit ideal is EVIDENCE only:
            1 in I mod p does not imply 1 in I over Q at a single prime.
            Promotion of any EMPTY requires the Q-computation plus a second
            engine, per the charge's certainty discipline.
DO NOT      normalise S_sigma (no Z-scaling symmetry; Sec 2 (C5)).
            omit the saturation (the unsaturated ideal has spurious components
            with r' = 0 or q = 0 that T5 and (C4) already exclude).
EXPECTED    if the pattern of Sec 3.7 persists, EMPTY at every cell run; that
            would be strong evidence for a uniform kill and would name the
            shape of the missing uniform argument.  It would NOT close the ray:
            see OPEN[A2-U-BOUND].
```

What the job cannot do: even if every listed cell returns EMPTY the ray
survives, `U` being unbounded. The outcome reads "the residual is empty on the
computed window", never "the ray is empty".

**Feasibility note.** Only `(1,3)` was decided inside this pass's budget.
The next cell up, `(1,5)` (31 unknowns, 52 generators), did not terminate in
~50 minutes under sympy, either plain or with the accelerator generators, so
the later cells were never reached. That is a statement about sympy's
Buchberger, not about the cells: `(1,5)` is well inside msolve's range.
Items 1-4 are for msolve/qqideal, not for a CAS.

### 4.2 The two unconsumed levers, named

HF Sec 4 typed `(O0, O1)` as the next lever. This pass consumed `E0` in full
(as a generator, not only through `(2.2)`) — new, and it confirms HF's
observation that `(2.2)` under-uses `O0`. But:

```text
   O1 is NOT in the charged record at all.  C32 quotes it only through its
   s = 0 specialisation (O1 collapses to -8 p' E2 = 0) and its e = 0 form.
   O0 is in the charged record only through (2.2) and its e = 0 form.
```

A fifth and sixth independent equation therefore exist and are unavailable
here. Every cell computation above uses **four of six** residual equations plus
`E0` and `T1`: an EMPTY answer is conclusive, a NONEMPTY answer is not. That
asymmetry governs how the job's output may be read.

## 5. Task (3): composition with the reviewed scope boundaries

The three boundaries the charge names all belong to HF Sec 2-3, the `(B3)`
group-theoretic half. **This pass consumes none of them.**

* **`SCOPE[B3-QH]`** (cusp quasi-homogeneous; charged, not banked; HR items
  (d)/(e) make it load-bearing for B3-PUSHOFF and the local CENTRAL-RANK). The
  A2 wall is about an explicit pullback normal form `(eta,s,p,C1,q,r,G)` at one
  cell of the horn's `A`-degree-2 census: no cusp, no local group, no Puiseux
  pair enters. `SCOPE[B3-QH]` is neither used nor weakened, and none of RAY-1,
  RAY-DEP, RAY-EDGE, RAY-2 may be quoted at a `(B3)` cusp.
* **The `Z(G) = 1` GAP** (HR Sec 4.1: only hypothesis-absence of global
  CENTRAL-RANK is proved, not centre-triviality). Nothing here touches
  `G = pi_1(C^2 \ A_F)`; no centre, global or local, is consumed.
* **The third-class caveat** (HR Sec 4: "global-abelian or local" is not an
  exhaustive partition — B3-PUSHOFF's first sentence, B3-COMPONENT and B3-N4
  are covering geometry of `E`). No transfer of any kind occurs here: no
  `iota`, no cover, no monodromy. The only transfers used are C32's `T1, T2,
  T5` and the four `e = 0` identities, each verified per-theorem in Sec 2.

The composition is therefore **null in the safe direction**: this pass is
orthogonal to the `(B3)` theorem set and crosses no scope boundary. The price
of that safety is Sec 6.

## 6. Task (4): the per-window ledger

The charge asks which `(B3)` windows would close on a ray kill. The answer,
from HF Sec 5 itself, is **none** — and I record the disagreement with the
charge's premise plainly, then give both ledgers.

HF Sec 5, first sentence: "`(1)`-`(2)` and `(3)` are **different instruments on
different objects** ... They do not compose into a kill, and I do not claim
one." HR Sec 10 promotes HORN-A2 and separately declines to promote any EMPTY
window in `N` for `(B3)`. There is no route in the charged record from the A2
wall to a `(B3)` window; the charge's phrase "(B3)'s A2 route at the affected
windows" names an object the record does not contain.

**Ledger A — what actually moves (the horn's `A`-degree-2 census).**

```text
 BEFORE (HF):  OPEN[A2-CELL-32-E1WALL]: g = 2e, deg E1 <= 2e-1, r' != 0,
               U >= 3e, leaders on the ray; plus T5's disjoint leftover
               window (r'=0, sigma=0, E1 != 0, 2 deg E1 <= max(e-1,1)).
 AFTER (here):
   U < 3e-1, U = 3e-1  EMPTY.  [HF, unchanged]
   U = 3e              EMPTY.  [RAY-EDGE; e >= 2 PROVED, (1,3) CAS and
                                independent of the wall]
   U >= 3e+2           SURVIVES, with deg E1 <= 2e-2 (RAY-2) and the
                       second-order pins of Sec 3.6; 2-dimensional per cell,
                       and order (top-2) adds nothing.
   T5 leftover         UNCHANGED (r' = 0 there; RAY-1/RAY-2 do not apply).

 OBSTRUCTION[A-DEGREE-TWO]: still NOT completed.  The explicit-pullback
 programme advances by the boundary slice and by one coefficient of E1; it
 does not advance a layer.
```

**Ledger B — the `(B3)` windows, unchanged, with the reason.**

```text
 N <= 3    EMPTY.                                                    [MI]
 N = 4     (0),(A),(B1),(B2) EMPTY;  (B3) SURVIVES.                  [unchanged]
 5..7      (A) EMPTY;  (B2) beta >= 2;  (B3) open.                    [unchanged]
 N = 8     (A) NONEMPTY (HT's 192-cell residual);  (B3) open.         [unchanged]
 8..10     as above.                                                  [unchanged]
 11..16    (B2) beta >= 1;  (B3) open.                                [unchanged]
 N >= 17   the above, plus (B1) with data solving MI (5.4).           [unchanged]

 REASON:  a ray kill is a statement about (eta,s,p,C1,q,r,G) in C[Z] at one
 census cell; it contains no N, no rho, no cusp, no cover.  Even total closure
 of the horn's live section leaves every row above as HF left it.  The (B3)
 successors remain HF's: OPEN[DEG-AF-VS-N] (highest value), OPEN[B3-J1-KILL],
 OPEN[B3-INFINITY-RANK], OPEN[B3-QH].
```

## 7. FALLACY-v2 audit

* **Flag/place/series.** No flag, place or cover series occurs; HF Sec 6's four
  groups are untouched. The only separation that matters is strict-below versus
  at-level in the `Z`-grading, made explicit in Sec 3.2: the `eta/G/target`
  families sit at `top - (U-3e+1)`, an odd offset, so their at-level appearance
  is confined to `U = 3e`.
* **Per-ray / exit-set charge.** No exit price asserted; no `charge_basis` line.
  "Ray" here is C32/HF's one-dimensional leader ray, not a valuation ray.
* **Carrier/attainment.** RAY-1, RAY-2 and the Sec 3.6 residual are
  `REPRESENTATIVE` necessary conditions on a hypothetical surviving pair; no
  cell is claimed realised, no witness constructed. `EMPTY` means emptiness of
  a coefficient variety, not non-existence of a Keller map.
* **Floor/attainment.** `deg E1 <= 2e-2` is stated as an inequality; the case
  `E1 = 0` is inside it and is not separately excluded here.
* **Pole/interior.** No pole identity used.
* **`sat()` wrapping.** Saturation is by an explicit variable `tt`, never a
  `sat()` call, so no bare-ideal/list confusion is possible; ring declared in
  Sec 3.7; the planted-solution control on the identical pipeline returns a
  non-unit basis while the true system returns `[1]`.
* **Raw remainder degree / vanished leaders.** Every branch on a vanishing
  leader is explicit: Wall B itself; the pair/single sub-configurations (C4);
  `deg E1 = 2e-1` versus `deg E1 <= 2e-2`, which are treated uniformly because
  `E1_{2e-1}` enters linearly and is then proved zero; `n != 1` (n is even);
  `n = 2` isolated and handled separately; `rho != 0` proved by positivity.
  The one division performed, `Phi = sG/eta`, is a series inversion of the
  actual truncated `eta`, not of a nominal leader.
* **Variable/ring map.** Laurent map, generator order and coefficient field
  declared in Sec 0, validated by the four `e = 0` identities before use;
  Groebner ring, order and variable list declared in Sec 3.7.
* **Prime label/derivative.** Every prime is `d/dZ`, per C32's convention; no
  prime is a label. `E1, E2, D1, D2, C1, C2` are C32's polynomial names and
  `EQ1..EQ4` the equations, kept distinct throughout.
* **Merge-free / M-descent, target/arrival index.** Not in play.
* **Not filled by cap or analogy.** The `Z`-scaling normalisation was tried,
  found illegal, and discarded with its obstruction displayed (C5) rather than
  assumed away; the run that used it was thrown out. `(N2)` is typed MEASURED,
  not claimed derived. The charge's premise in Task (4) is contradicted with
  its source quoted, not silently reinterpreted. Where the ray survives I say
  so.

## 8. Typed verdict block

```text
LANE              RAY-KILL
SCOPE             C32's corrected 7/7 live-section system over C, a b kappa != 0,
                  eta != 0, G != 0, s != 0, e >= 1; Chamber II E1-wall
                  (HORN-A2), simultaneous-top regime U >= 3e.
                  No (B3) object, no cusp, no cover, no transfer.

PROVED HERE       RAY-1 (N1),(N3),(N4)  the three hand-derived next-order rows,
                                        with their normalising factors, and the
                                        identical cancellation of E1_{2e-1} in
                                        EQ1 and in EQ4.
                  RAY-DEP               n(N1) + (n-2)(N3) - (N4) = -(n-2) rho.
                  RAY-EDGE (e >= 2)     U = 3e is EMPTY, via
                                        rho = -P(-(2e+1))b^2 eta_e^4/((4e-2)s^2)
                                        and 32e^3+32e^2+6e+1 > 0.
                  (C4)                  on Wall B every pair/single
                                        sub-configuration dies; only the full
                                        simultaneous-top regime survives.
                                        (Gap in HF's display, closed.)
                  (C5)                  the (a,b)- and mu-scalings are exact
                                        symmetries; there is NO Z-scaling
                                        symmetry (EQ1 and EQ4 force
                                        incompatible weights on kappa).
                  All PROVED-HERE, UNREVIEWED.

MEASURED          closed forms of (N2) and rho, and (N1),(N3),(N4) again:
                    50 cells, 1<=e<=10, U in {3e,...,3e+8}, zero mismatches;
                    a 72-cell sweep (e<=12) confirms rank 3, ker inside
                    {E1_{2e-1}=0}, rho, and consistency iff U >= 3e+2.
                  RAY-2 (deg E1 <= 2e-2): proved FROM the measured (N2).
                  order (top-2) adds no condition when U >= 3e+2 (10 cells,
                    e <= 5).
                  the four e=0 identities: all exactly 0.  Chamber II det,
                    Wall B rows/kernel, EQ4 top on the ray: ratio 1 to HF.

CAS-DECIDED       cell (1,3) EMPTY: unit ideal, 37 generators, 22 unknowns,
                  grevlex over Q, 2.2 s; also EMPTY with the wall not imposed
                  (23 unknowns, 13.2 s).  Planted-solution control on the
                  identical pipeline: non-unit.  SINGLE ENGINE (sympy 1.14.0)
                  -- NOT promotion-grade; item 0 of A2-E1WALL-CELLS.

CONSUMED          C32: T1, T2 (Xi), (1.1), Sec 6 E2eq|_{G=0}/Delta_2, (2.2),
                    E0, T5 -- at their typing, re-validated at e=0 before use.
                  HF: HORN-A2 (wall + ray), the Chamber II rows, P(c) -- at
                    HR's CONFIRMED typing.  HR's GAPs (Z(G)=1, the
                    non-partition) respected, not consumed.

NOT CLAIMED       closure of the ray;  of OPEN[A2-CELL-32];  completion of
                  OBSTRUCTION[A-DEGREE-TWO];  any EMPTY window in N for (B3);
                  any statement about a (B3) cusp, about Z(G), or about any
                  transfer;  realisability of any surviving cell;
                  promotion-grade emptiness of (1,3).

OPENS RAISED      OPEN[A2-U-BOUND]      bound U in terms of e on the E1-wall;
                                        without it no finite computation
                                        decides one value of e.  Highest-value
                                        successor for the horn lane.
                  OPEN[A2-E1WALL-RESIDUAL]  U >= 3e+2, deg E1 <= 2e-2,
                                        r' != 0, second-order pins of Sec 3.6.
                                        Replaces OPEN[A2-CELL-32-E1WALL].
                  OPEN[A2-O0-O1]        O1 absent from the charged record, O0
                                        present only through (2.2): two of six
                                        residual equations are unavailable.

DEVIATIONS        (1) The charge's Task (4) premise -- that a ray kill closes
                      (B3) windows -- is contradicted, HF Sec 5 quoted.  Both
                      ledgers supplied anyway.
                  (2) The pass went two orders deep, not one, then decided one
                      cell exactly; the extra depth is what isolates (1,3) and
                      shows the ladder does not terminate.
                  (3) A Z-scaling normalisation used in an early run was found
                      illegal and that run discarded; the obstruction is
                      displayed in (C5), not suppressed.
                  (4) Drivers left in /tmp/raykill, not installed in box/.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `35935`.
- Body SHA-256:
  `95d6d7200d7337ec528350976bc942b87eca0b9cfde4a461d399b67b1d1be259`.
- Frozen basis: `966a65f2c79d225aba4aeef1f89548cb9f24a007`.
