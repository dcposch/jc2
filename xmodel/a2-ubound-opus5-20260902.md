# A2-U-BOUND — the one-cusp horn's missing finisher

Lane: `A2-U-BOUND`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation plus exact symbolic algebra (sympy 1.14.0 over `Q`, rational
arithmetic only) and two exact Groebner decisions. No AWS, no msolve, no
`jc2-lean`, no literature fetched, no canonical ledger touched. Drivers in
`/tmp/ubound`, not installed in `box/`.

No `charge_basis` line: this report asserts no new exit price.

## 0. Custody, hashes, method

The six charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all six match the charge exactly:

```text
3d08b8996227e292d76e0ba3901cfad16099f347f97129d27b6bf5b3bc253f0a  ray-kill-opus5-20260902.md
df5612152d60496bb81311ee9183d3c580759a2549d6ea8945a487d284976fcf  ray-kill-review-gpt55-20260902.md
4116a4e2fbd89a7c041f7eaea48d5199709f3f457ebcbf5397770391e8bd0c66  n2-derive-gpt55-20260902.md
86caf003268ddc40143daa68d439079dbd82d1dac41e1da93f33a661d52f96ac  cell-32-spec-sol56-20260901.md
d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b  cell-32-termination-opus5-20260901.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  horn-flagship-opus5-20260902.md
```

Abbreviations below: **SPEC** = `cell-32-spec-sol56`, **C32** =
`cell-32-termination`, **HF** = `horn-flagship`, **RAY** = `ray-kill`,
**REV** = `ray-kill-review-gpt55`, **N2D** = `n2-derive-gpt55`. No charged file
was edited; no repository file other than this report was written.

**Method and its one deviation from the charge.** The charge asked me to consume
C32 T1-T5, HORN-A2 and RAY-1/DEP/EDGE/2 *at their reviewed typings*. Before
using them I ran the one control none of the six reports had run: I rebuilt the
seven residual equations `O0,O1,O2,E0,E1eq,E2eq,E3eq` **from SPEC's own
`Even`/`Odd` displays** (SPEC:57-66) rather than from SPEC's list of the seven.
That control fails. One of the seven displayed equations is wrong, and it is
load-bearing for HORN-A2 and for `N2`. Everything below is therefore computed on
the corrected system, and Section 2 is a P0 report, not a lane result.

Every polynomial identity below was verified either symbolically over
`Q(a,b,kappa,c)` with `sympy` functions of `Z`, or as an exact truncated Laurent
tail at `Z = infinity` with symbolic coefficients (a small exact class in
`/tmp/ubound/tail.py`; degree bookkeeping is explicit, division is a genuine
series inversion of the actual truncated `eta`, never of a nominal leader).

## 1. Verdict, up front

```text
(1) P0 IN THE CHARGED BASIS.  SPEC's displayed equation `E2` (SPEC:100-104)
    is NOT [A^2]Even.  It is missing the term  -2 q E1.  Four independent
    controls confirm this (Sec 2).  The error propagates verbatim into C32
    Sec 6 (`E2eq|_{G=0} + Delta_2`), hence into HF's `EQ2` row, hence into
    HORN-A2, `N2`, RAY-2, and every box01 cell run.

(2) BLAST RADIUS, measured not guessed.
      HORN-A2's Chamber II determinant  36 n (c+2e)(c+2e+1)  becomes
      IDENTICALLY ZERO on the corrected system, in Chamber II AND in the
      Chamber I / III simultaneous-top branches.  The E1-wall is therefore NOT
      derived: the corrected top-order system is degenerate for EVERY c, with
      the same kernel ray (n/4, 3/4, 1), on which all of EQ1..EQ4 and the new
      O1 vanish identically.  RAY-1's `N2` loses its `epshat` column, so RAY-2
      (deg E1 <= 2e-2) is REFUTED and the residual is 3- not 2-dimensional.
      RAY-DEP and RAY-EDGE(e>=2) are UNAFFECTED (N1,N3,N4 only).

(3) OPEN[A2-O0-O1] RESOLVED.  O0 is NOT missing: given E0 and s != 0, O0 is
      EQUIVALENT to (2.2)=EQ4 (Sec 4.1).  Only O1 was absent; it is transcribed
      here, verified against [A^1]Odd, put on the wall in p'-free form, and
      shown to be INERT at leading order (Sec 4.2).

(4) THE FINISHER.  Change variables to the deviations from the ray,
        X := 4b eta^2 r - s^2 ,      Y := 4b^2 eta q - 3a s^2 .
    THEOREM DEV-FREE (proved).  In (eta,s,G,X,Y) the equations EQ1, EQ2, EQ3
    are EXACTLY s-free, and with N(W) := eta W' - 2W eta' = eta^3 (W/eta^2)',
        EQ1 :  8Z b^2 kappa eta^2 + 3a(3E1 - b eta^2) N(X) - 4 E1 N(Y) + 2 V Y = 0.
    RAY-1's whole 2-dimensional residual is exactly deg X, deg Y <= 2 sigma - 2.
    THEOREM A2-DEV-BOUND (proved).  For c != -2e,  deg X, deg Y <= 4e - 1,
    UNIFORMLY IN U -- the first U-free finiteness statement in the horn lane.
    THEOREM A2-EQ4-HOM (proved).  The EQ4 row is homogeneous at every level, so
    at k = max(deg X, deg Y) the EQ1 and EQ4 rows must be PROPORTIONAL: one
    relation R(e, c, sigma, k) = 0 with k in {0,...,4e-1}.

(5) THE EXACT ANSWER TO THE CHARGE.  R is linear in sigma, so for each fixed
    (e, c) it determines sigma from k; as k ranges over at most 4e values,
    U IS BOUNDED for each fixed c.  What is NOT bounded is c.  The structural
    reason no unconditional U-bound follows is exact, and it is not a gap in the
    search: it is the P0.  HORN-A2 pinned c; the corrected system does not.  So

        OPEN[A2-U-BOUND]  reduces to  OPEN[A2-WALL-REDERIVE] : pin c.

(6) EVIDENCE.  Cell (1,3) is EMPTY on the corrected system with the wall
    imposed, with and without O1 (sympy/Q, unit ideal).  The wall-free variant
    -- the one that made RAY's (1,3) independent of HORN-A2 -- did NOT
    terminate in 1500 s and is NOT re-established.  Single engine.
```

## 2. The P0: SPEC's `E2` display is missing `-2 q E1`

### 2.1 The control

SPEC Sec 1 defines (SPEC:57-66), with `H = A + A^2 Z`, `chi_S = 2 + 4AZ`,
`J(X,Y) = X_A Y_Z - X_Z Y_A`, `WA(X,Y) = X_A Y - X Y_A`,
`WZ(X,Y) = X_Z Y - X Y_Z`,

```text
Even = 2A^2(P_A S0 - Q (R0)_A) + 4H(J(P,S0)+J(Q,R0)) + chi_S(Q (R0)_Z - P_Z S0),
Odd  = 2A^2 WA(Q,S0) + 4J(P,R0) + 4H J(Q,S0) - chi_S WZ(Q,S0),
```

and asserts that the seven residual equations are `[A^0..2]Odd = 0`,
`[A^0]Even = kappa`, `[A^1..3]Even = 0`. I built `Even`, `Odd` from those
displays with `P = p + A C1 + A^2 C2`, `Q = q + A D1 + A^2 D2`,
`R0 = r + A E1 + A^2 E2`, `S0 = s`, all functions of `Z` alone, and subtracted
SPEC's seven displayed equations. Verbatim result:

```text
O0   residual: 0        E0   residual: 0
O1   residual: 0        E1eq residual: 0
O2   residual: 0        E3eq residual: 0
E2eq residual: 2*(-2*Z*b*eta*eta' - b*eta^2 - G)*q      =  -2 q E1
[A^3]Odd  = 0           [A^5]Even = 0
```

Six of seven reproduce exactly. The seventh is off by exactly `-2 q E1`:

```text
                 [A^2]Even  =  (SPEC's E2 display)  -  2 q E1 .
```

### 2.2 Four independent confirmations

1. **The `[A^4]Even` display.** SPEC Sec 2.1 quotes the *review-corrected*
   `[A^4]Even` (SPEC:132-135), the identity that eliminates `D1`. With
   `D1, E1, C2` free my `Even` reproduces it with residual `0`. Its first two
   terms `-2 D2 E1 - 4 D1 E2` come from the *same block*
   `2A^2(P_A S0 - Q (R0)_A)` whose `[A^2]` part is `2(C1 s - q E1)`: SPEC kept
   the `q`-half of that block at `A^4` and dropped it at `A^2`.
2. **`[A^5]Even = 0` and `[A^3]Odd = 0`** hold identically after the `C2` and
   `D1/E1` parametrisations, exactly as SPEC asserts.
3. **SPEC's own positive control** (SPEC Sec 4: `kappa = 2`, `f = Z`,
   `g = U sum_n L_n A^n`, `L_0 = -1`, `L_n = -(2nZ/(2n+1))L_{n-1}`, asserting
   `Odd = 0`, `Even = 2 - 4(J+1)Z L_J A^{J+1}`). Feeding `P = Z`, `Q = 0`,
   `R0 = 0`, `S0 = sum L_n A^n` into my `Even`/`Odd` gives `Odd = 0` and
   `Even - target = 0` at `J = 1,2,3,4`. This is an *external* validation: it
   uses no part of the `(3,2)` parametrisation.
4. **The downstream copy.** C32 Sec 6's `E2eq|_{G=0} + Delta_2` (C32:631-642)
   — the formula RAY's driver and N2D both use — satisfies
   `C32 display - SPEC's E2 display = 0`. C32 transcribed SPEC faithfully and
   inherited the error rather than introducing or correcting one.

Throughout the rest of this report `EQ2` means the **corrected** `[A^2]Even`,
i.e. C32's display **plus** `-2 q E1`; `EQ2old` names the charged one.

### 2.3 Blast radius, measured

Chamber II, simultaneous-top regime (`m = U`, `n = U-e`, `2sigma = U+e`),
`c := G_{2e}/(b eta_e^2)`, HF's coordinates `x = a eta_e^3 r_n n`,
`y = b eta_e^2 q_m`, `w = a eta_e s_sigma^2/b`. Fitting the top rows over 42
cells `1<=e<=7`:

| row | entry `x` | entry `y` | entry `w` |
|---|---|---|---|
| `EQ3` | `12` | `-8n` | `3n` |
| `EQ1` | `3(3c+6e+2)` | `-4n(c+2e+1)` | `3n(c+2e+2)/4` |
| `EQ2old` | `6(2c+4e+3)` | `2(2ce-2cn+4e^2-4en-6n+1)` | `-3(2ce-c+4e^2-2e-3n)/2` |
| `EQ2` | `6(2c+4e+3)` | `EQ2old_y - 2(c+2e+1)` | same as `EQ2old` |

The correction is exactly `-2(c+2e+1)` in the `y` column; it vanishes **on
Wall B**, which is why HF Sec 4.4's Wall-B row `[6, 2-4e-8n, 3e+9n/2-3/2]` is
unchanged. Off the wall it is not zero, and

```text
   det(EQ3, EQ1, EQ2old) = 36 A n (c+2e)(c+2e+1)      [HF, reproduced]
   det(EQ3, EQ1, EQ2   ) = 0                           IDENTICALLY
```

for all `c, e, n`. The same collapse holds in the Chamber I and Chamber III
simultaneous-top branches: at `(e,g,U) = (2,2,8)` HF's determinant is
`25920 A^7 a^2` and the corrected one is `0`; at `(e,g,U) = (2,6,10)` HF's is
`2880 A^3 C^2 a^2/b^2` and the corrected one is `0`.

The corrected nullspace is one-dimensional and **independent of `c`**:

```text
   (x, y, w) = (n/4, 3/4, 1) * w      for every c ,
```

and on it the quadratic tops of `EQ4` and of the new `O1` vanish identically as
well (verified at `(1,3),(1,5),(2,8),(2,10),(3,11),(4,14)`: all five tops are
exactly `0`). So on the corrected system there is no leading-order wall at all
in Chamber II; the whole `c`-line survives the top order.

**Consequences for the charged record.**

```text
 HORN-A2         The wall clause ("off that wall the section is EMPTY") is NOT
                 SUPPORTED: the Chamber II determinant vanishes for every c.
                 The RAY-1 leaders r_n, q_m SURVIVE and are now valid for every
                 c, not only on the wall.
 RAY-1 / N2      N2 loses its epshat column.  On Wall B, E1_{2e-1} enters EQ2
                 only through the corrected term -2qE1, whose normalised
                 contribution is exactly +h = 4e alpha + epshat, cancelling
                 N2D's E1-family contribution -h.  Corrected row:
                   (N2c) (2n+2e-3)alpha - 2(3n+2e-4)beta + (4n+2e-5)gamma
                          - (n-1) delta = 0 ,   NO epshat term,
                 and substituting N1, N3 (rho=0) into N2c gives 0 identically
                 (beta column (2n+2e-3)-2(3n+2e-4)+(4n+2e-5) = 0; delta column
                 -(2n+2e-3)/2+(4n+2e-5)/2-(n-1) = 0).
 RAY-2           REFUTED as stated: epshat is unconstrained at order (top-1),
                 the residual is 3-dimensional in (beta, delta, epshat), and
                 deg E1 <= 2e-1 is all that survives.
 RAY-DEP         UNAFFECTED (identity in N1,N3,N4 only).
 RAY-EDGE e>=2   UNAFFECTED: REV Sec 3 and N2D Sec 6 both record that the edge
                 proof consumes only N1,N3,N4, from EQ3,EQ1,EQ4.
 box01 cells     The wall generator G_g = -(1+2e) is no longer derived, and
                 EQ2 was wrong.  All of (1,3), (1,5), (1,7) must be RE-RUN.
```

## 3. Conventions

C32's, verbatim. `C[Z]`, every prime is `d/dZ`, `deg 0 = -infinity`,
`a b kappa != 0`, `eta != 0`, and `c5 = 0` by C32's shear on the live section.
`e = deg eta`, `sigma = deg s`, `g = deg G`, `m = deg q`, `n = deg r`;
`d = 3a/(2b)`; `E2 = bZ eta^2`, `D2 = aZ eta^3`, `C2 = dZ eta s`,
`E1 = E2' + G`, `D1 = D2' + d eta G`, `Phi = sG/eta`,
`C1 = d[(Z eta)' s + Phi/(2b)]` (C32 T1). I write

```text
   N(W) := eta W' - 2 W eta'  =  eta^3 (W/eta^2)'          (verified identity)
   V    := 2Zb eta^2 eta'' - 2Zb eta eta'^2 + 2b eta^2 eta' - 2G eta' + eta G'
   W1   := E1 - b eta^2 = 2Zb eta eta' + G .
```

`deg V = 3e - 2` for generic `(eta,G)` in Chamber II — the nominal `3e-1`
leader cancels between `2Zb(eta^2 eta'' - eta eta'^2)` and `2b eta^2 eta'`, and
the `G` part is `eta^3 (G/eta^2)'`. Verified with generic tails at
`e = 1,2,3,4`: actual degrees `1,4,7,10`.

## 4. Task (L1): the two "missing" equations

### 4.1 `O0` is not missing

SPEC's `O0` is `4(C1 r' - p' E1) + 2(q s' - q' s) = 0`. Multiply by `s` and use
`E0` in the form `p' s = q r' - kappa/2`:

```text
   s * O0  =  4 r'(s C1 - q E1) + 2 kappa E1 + 2 s(q s' - q' s)
           =  2 * [ 2(sC1 - qE1) r' + kappa E1 + q s s' - q' s^2 ]
           =  2 * EQ4 .
```

Since `s != 0` on the live section (C32 T3), `O0` and `EQ4` are **equivalent
modulo `E0`**. RAY Sec 4.2's "O0 is in the charged record only through (2.2)"
understates the situation: (2.2) *is* `O0`, once `E0` is a generator — and RAY
did use `E0` as a generator. So RAY's cell systems used **five of six**
p'-free residual equations, not four of six, and the only genuinely absent one
was `O1`.

### 4.2 `O1`, transcribed and put on the wall

```text
 O1 :  8(C2 r' - p' E2) + 4(C1 E1' - C1' E1) + 6 D1 s' - 2 D1' s
       + 4Z(q s' - q' s) = 0 .
```

This is verified to be `[A^1]Odd` exactly (Sec 2.1). Multiplying by `s` and
eliminating `p'` through `E0` gives the p'-free generator

```text
 O1s := 8 s C2 r' - 8 E2 (q r' - kappa/2) + 4 s(C1 E1' - C1' E1)
        + 6 D1 s s' - 2 D1' s^2 + 4Z s(q s' - q' s)  =  0 .            (O1s)
```

**Is `O1` independent?** At the top order it is not: writing `O1s` in HF's
`(x,y,w)` coordinates on the wall gives the quadratic form
`12 xw - 8 xy - 2n yw` (up to `1/(a A^3)`), which vanishes identically on the
ray `(n/4, 3/4, 1)` — as does `EQ4`'s quadratic `(3(c+2e+2)/2) xw
- 2(c+2e+1) xy - (n/2) yw`. So `O1` adds **nothing** at leading order in
Chamber II, at any `c`. It is not a consequence of the others as a polynomial
identity (Sec 6 shows its deviation row is a genuine fifth row at
degree `k + 2sigma - 1`), but it is strictly weaker than `EQ3` in the descent
because its inhomogeneity reaches to degree `5e + 2sigma - 1`, one full
`e`-block higher than `EQ3`'s. **The charge's hope that `O0` and `O1` turn
"four on five" into "six on five" is not realised**: the correct statement is
that the order-by-order ladder is the wrong bookkeeping (Sec 5).

Also recorded, because it is where the descent's inhomogeneity comes from:

```text
   Psi_5 := O1s|_{X=Y=0}  has degree 5e + 2sigma - 1 with leader
            6a b^2 eta_e^5 s_sigma^2 (e - sigma)(c + 2e)^2 .
```

## 5. THEOREM DEV-FREE: the deviation variables, and why the ladder was the
wrong bookkeeping

### 5.1 The universal ray is the shadow of the `kappa = 0` family

The corrected leading-order kernel `(x,y,w) = (n/4, 3/4, 1)` is `c`-independent:
`r_n = s_sigma^2/(4b eta_e^2)`, `q_m = 3a s_sigma^2/(4b^2 eta_e)`. Lead (L3) asks
whether `q` and `r` are `s^2/eta`-type expressions. They are, and the reason is
sharp: substituting the *exact* ansatz `s = eta u`, `q = 3a eta u^2/(4b^2)`,
`r = u^2/(4b)` (which makes `T1` automatic) into the corrected system gives

```text
   EQ1  =  2 Z kappa ,          EQ4  =  kappa E1 ,
   EQ2, EQ3, O1s  =  explicit expressions in (eta, G) alone (EQ2, EQ3) resp.
                     (eta, s, G) with a  4Z b^3 kappa eta^4  term (O1s).
```

**Every `(eta, s, G)`-dependence of `EQ1` cancels identically on the ray.** The
ray is exactly the leading order of the `kappa = 0` solution family, and `kappa`
is the whole obstruction. That is the structural statement the order-by-order
ladder could not see.

### 5.2 The deviations

Put

```text
   X := 4b eta^2 r - s^2 ,        Y := 4b^2 eta q - 3a s^2 ,
```

equivalently `r = (s^2+X)/(4b eta^2)`, `q = (3a s^2+Y)/(4b^2 eta)`. In the
simultaneous-top regime `deg(4b eta^2 r) = deg(4b^2 eta q) = deg s^2 = 2 sigma`,
and the ray is exactly the vanishing of the degree-`2sigma` coefficients of `X`
and `Y`.

> **RAY-1 restated.** RAY's entire order-`(top-1)` residual — the pins
> `eta_{e-1}/eta_e = beta - delta/2`, `s_{sigma-1}/s_sigma = beta`,
> `q_{m-1}/q_m = beta + delta/2`, `r_{n-1}/r_n = delta` — is precisely
> ```text
>       deg X <= 2 sigma - 2   and   deg Y <= 2 sigma - 2 .
> ```
> *Proof.* `[Z^{2sigma-1}]X = s_sigma^2(2 alpha + delta - 2 beta)` and
> `[Z^{2sigma-1}]Y = 3a s_sigma^2(alpha + gamma - 2 beta)`, using
> `4b eta_e^2 r_n = s_sigma^2` and `4b^2 eta_e q_m = 3a s_sigma^2`. Both vanish
> exactly on RAY's two-parameter solution. QED

So the "four conditions on five new coefficients per order" bookkeeping is an
artefact of the coordinates: in `(eta, s, G, X, Y)` the free objects at each
order are only `X` and `Y`, and the number of *conditions* is five.

### 5.3 THEOREM DEV-FREE

Write `N(W) := eta W' - 2W eta' = eta^3 (W/eta^2)'` (verified identity) and

```text
   V := 2Zb eta^2 eta'' - 2Zb eta eta'^2 + 2b eta^2 eta' - 2G eta' + eta G' .
```

> **THEOREM DEV-FREE.** In the variables `(eta, s, G, X, Y)` the equations
> `EQ1 = [A^1]Even mod E0`, `EQ2 = [A^2]Even` (corrected) and
> `EQ3 = [A^3]Even` (C32 `T2`) contain **no `s` at all**. Explicitly
>
> ```text
>  4b^2 eta^2 * EQ1 = 8Z b^2 kappa eta^2
>                     + 3a(3E1 - b eta^2) N(X)  -  4 E1 N(Y)  +  2 V Y .   (D1)
> ```
>
> `EQ3` and `EQ2` are likewise `s`-free; the `(X,Y)`-part of `Xi` is
> `(1/b)[3a N(X) - 2 N(Y)]`, so
>
> ```text
>  (b/eta) * EQ3 = b Z^2 Xi_0 - 3a (Z eta^2 G^2)'/eta + Z^2[3a N(X) - 2 N(Y)]
>  Xi_0 = 12ab eta^3 eta'(eta'+2Z eta'') + 12a eta[(eta eta''-eta'^2)G+eta eta'G'] .
> ```

*Proof of `s`-freeness of `EQ3`.* With `r_0 = s^2/(4b eta^2)` and
`q_0 = 3a s^2/(4b^2 eta)`, the three `s`-carrying families of `Xi` are
`4d s(eta s' - eta' s)`, `12a eta^3 r_0' = (3a/b) N(s^2) = (6a/b) s(eta s'-s eta')`
and `8b eta(q_0 eta' - q_0' eta) = -(6a/b) N(s^2) = -(12a/b) s(eta s'-s eta')`.
Since `4d = 6a/b`, they sum to `(6a/b - 12a/b + 6a/b) s(eta s'-s eta') = 0`. QED

*`EQ1`.* `(D1)` was verified symbolically: `4b^2 eta^2 EQ1 - (D1)` is exactly
`0` over `Q(a,b,kappa)` with `eta, s, G, X, Y` arbitrary functions
(`3E1 - b eta^2 = 2b eta^2 + 6Zb eta eta' + 3G`). `s`-freeness of all three is
the machine's verdict on the expanded numerators.

`EQ4` and `O1s` are **not** `s`-free: `EQ4 = kappa E1 + Lambda_4 + Q_4` with

```text
   8b^3 eta^4 * Q_4  =  - N(X) * E1 * Y ,                                (D2)
   8b^3 eta^4 * Lambda_4 = s * [ 3ab eta^3 s X' - 6ab eta^2 s eta' X
        - 2b eta^3 s Y' + 4b eta^2 s eta' Y - 4Zb eta^2 eta' s' Y
        + 4Zb eta s eta'^2 Y - 2G eta s' Y + 2G s eta' Y ] .
```

Both are exact. `O1s|_{X=Y=0}` is the `Psi_5` of Sec 4.2.

## 6. THEOREM A2-DEV-BOUND: a uniform, U-free bound

Fix `xi := deg X`, `ups := deg Y`, `k := max(xi, ups)`, and let
`c := G_g/(b eta_e^2)` in Chamber II. All degrees and leaders below were
computed with **generic** truncated tails (symbolic sub-leading coefficients),
not by monomial substitution, so no vanished leader is hidden.

### 6.1 The two rows and the two inhomogeneities

```text
  deg Lambda_1 = max(2e,g) + e + k - 1 ,
     leader (Chamber II) = (k-2e) b eta_e^3 [ 3a(3c+6e+2) X_k - 4(c+2e+1) Y_k ] ;
  deg Psi_1    = 2e + 1  exactly  (the term 8Z b^2 kappa eta^2, kappa != 0).

  deg Lambda_3 = e + k + 1 ,
     leader = (k-2e) eta_e [ 3a X_k - 2 Y_k ]      (no c, no chamber) ;
  deg Psi_3    = 5e             (Chambers II and III)
             or  e + 2g          (Chamber I),
     leader   = 3a b^2 eta_e^5 P(c)                (Chamber II),
                12a b^2 eta_e^5 e^2 (2e-1)          (Chamber III),
                -3a eta_e G_g^2 (1+2e+2g)           (Chamber I),
     P(c) := 4e^2(2e-1) + 4ce(2e-1) - c^2(6e+1)     [HF Sec 4.4, reproduced].
```

Both `Lambda` leaders were checked ratio-`1` against the displayed closed forms
at twelve `(e,k)` pairs, `1<=e<=3`; the three `Psi_3` leaders ratio-`1` at
fourteen `(e,g)` pairs. `deg V = 3e-2` (generic) was checked at `e=1..4`, which
is what puts `2VY` strictly below `4E1 N(Y)`.

### 6.2 The descent

The `Lambda_1` and `Lambda_3` rows are *homogeneous* (their inhomogeneity is
strictly lower) exactly when

```text
   EQ1 :  max(2e,g) + e + k - 1 > 2e+1        <=>   k >= 3 - e   (all chambers)
   EQ3 :  e + k + 1 > 5e                      <=>   k >= 4e      (Ch. II, III)
          e + k + 1 > e + 2g                  <=>   k >= 2g      (Ch. I)
```

and their `2x2` determinant is

```text
   Chamber II (g = 2e) :  -6a (k-2e)^2 (c + 2e)
   Chamber III (g < 2e) :  -6a e (k-2e)^2
   Chamber I  (g > 2e) :  -6a (k-2e)^2 G_g
```

(the Chamber III/I entries use `lead(E1) = b(1+2e)eta_e^2` resp. `G_g` and
`lead(3E1-b eta^2) = b(6e+2) eta_e^2` resp. `3G_g`). Hence:

> **THEOREM A2-DEV-BOUND.** On the live section (`G != 0`, `s != 0`, `e >= 1`,
> `a b kappa != 0`), in the simultaneous-top regime,
>
> ```text
>   Chamber III (g < 2e) :   deg X <= 4e-1 ,  deg Y <= 4e-1 .   Unconditional.
>   Chamber II  (g = 2e) :   deg X <= 4e-1 ,  deg Y <= 4e-1 ,   provided c != -2e.
>   Chamber I   (g > 2e) :   deg X <= 2g-1 ,  deg Y <= 2g-1 .   Unconditional.
> ```
>
> *Proof.* For `k >= 4e` (resp. `2g`) both rows are homogeneous and, since
> `k >= 4e > 2e` (resp. `k >= 2g > 2e`), the factor `(k-2e)` is nonzero; the
> determinant is then nonzero under the stated proviso, so `X_k = Y_k = 0`.
> Descend. `k >= 3-e` holds throughout since `k >= 4e >= 4`. QED

This is the first statement in the horn lane that bounds anything **uniformly in
`U`**. It is the exact answer to the charge's "prove a bound"; what it bounds is
not `U` itself but the deviation from the ray, and Sec 7 converts that.

Two remarks. If `P(c) = 0` the bound only improves (`deg Psi_3` drops). The
proviso `c != -2e` is not an artefact: there the `EQ1` row is exactly
`2(k-2e) b eta_e^3 [3a X_k - 2 Y_k]`, proportional to the `EQ3` row, and the
descent stalls. HF Sec 4.4's first bullet kills `c = -2e` without using `EQ2`,
but by a *top-order* argument in `(x,y,w)`, and the corrected top-order system
is degenerate for every `c` — so I record `c = -2e` as an open sub-branch rather
than importing that verdict.

## 7. THEOREM A2-U-BOUND: what actually bounds `U`, and what does not

### 7.1 `EQ4`'s row is homogeneous at every level

From `(D2)` and the `Lambda_4` display,

```text
   deg Psi_4 = deg(kappa E1) = 2e ,
   deg Q_4   = xi + ups - e - 1 ,
   deg Lambda_4 = k + 2 sigma - e - 1     (verified generically, 18 cells).
```

In the regime `U >= 3e`, i.e. `2 sigma = U + e >= 4e`, and with `k <= 4e-1`:

```text
   Lambda_4 > Q_4  <=>  k + 2 sigma > xi + ups ;   xi+ups <= 2k and 2 sigma >= 4e > k. OK
   Lambda_4 > Psi_4 <=> k + 2 sigma > 3e + 1 ;     2 sigma >= 4e > 3e+1 for e >= 2,
                                                    and for e = 1 whenever U >= 5.
```

> **THEOREM A2-EQ4-HOM.** In the simultaneous-top regime the `EQ4` deviation row
> is homogeneous at every level `k >= 0`. Its exact form (normalised by
> `s_sigma^2/(8 eta_e b^2)`) is
> ```text
>    [ 3a(k-2e) ,  -2( (sigma-e) c + k + 2e(sigma-e-1) ) ] .
> ```

This row was *derived* from the closed form of `Lambda_4` and then checked at 36
`(e,sigma,k)` triples, `1<=e<=3`: exact agreement including the `sigma`-columns.

### 7.2 The dichotomy

Let `k = max(xi, ups)` and assume `c != -2e` and `c != -(2e+1)`. The `EQ1` row
is homogeneous throughout because `k >= 3-e` fails only for `k <= 2-e`, i.e.
`k <= 1` at `e = 1` and never for `e >= 3`; those finitely many small-`k`
configurations are inside branch (B)'s bound `k <= 2e` and are not used below.

* **`ups > xi` is impossible.** Only `Y_ups` survives; `EQ1`'s `Y`-entry forces
  `(ups-2e)(c+2e+1) = 0`, so `ups = 2e`; then `EQ4`'s `Y`-entry is
  `-2(sigma-e)(c+2e)`, nonzero because `sigma > e` and `c != -2e`. Contradiction.
* **`xi > ups` forces `xi = 2e`.** Only `X_xi` survives, and each of the `EQ1`,
  `EQ3`, `EQ4` `X`-entries carries the factor `(xi - 2e)`.
* **`xi = ups = k`.** The `EQ1`/`EQ4` determinant is

  ```text
     det(EQ1,EQ4) = -6a (k-2e) * R ,
     R := (c+2e)[(3c+6e+2) sigma + k] - e(3c+6e+2)(c+2e+2) + 4e(c+2e+1)
  ```

  (verified: `det + 6a(k-2e)R = 0` identically). So `k = 2e` or `R = 0`.

> **THEOREM A2-U-BOUND.** Live section, Chamber II, `U >= 3e`,
> `c not in {-2e, -(2e+1)}`. Then exactly one of
>
> ```text
>  (A)  xi = ups = k <= 4e-1  and  R(e,c,sigma,k) = 0 ;
>  (B)  xi = 2e ,  ups < 2e   (the N-degenerate branch).
> ```
>
> In branch (A), if `3c+6e+2 != 0` then `R = 0` reads
> ```text
>    sigma = [ e((3c+6e+2)(c+2e+2) - 4(c+2e+1))/(c+2e)  -  k ] / (3c+6e+2) ,
> ```
> so for each fixed `(e,c)` the integer `k in {0,...,4e-1}` determines `sigma`,
> hence `U = 2 sigma - e`: **`U` takes at most `4e` values.**
> If `3c+6e+2 = 0` — exactly HF's **Wall A**, `c = -(2/3)(1+3e)` — then
> `R = 2(2e-k)/3` and `det(EQ1,EQ4) = 4a(k-2e)^2 != 0` for `k != 2e`, so branch
> (A) is **empty** and only branch (B) survives.

So `U` **is** bounded, for every fixed `c` outside three explicit values, and the
bound is explicit and small (`4e` cells). This is a genuine `U`-bound, and it is
the finisher the charge asked for — but it is conditional on `c`, and the reason
is not a gap in my search:

```text
   HORN-A2 pinned c to the single value -(2e+1).  The P0 of Sec 2 removes that
   pin: on the corrected system the top-order determinant vanishes identically
   and the ray is the same for every c.  With c free, the wall R = 0 moves with
   sigma, and no finite computation covers all c.
```

That is the **exact structural reason** (charge lead (L5)) why no unconditional
bound exists *on the present record*. It is not a counterexample, and it is not
an obstruction in principle: it is a hole the P0 opened.

### 7.3 The named gap: branch (B)

Branch (B) is `deg X = 2e`, `deg Y < 2e`. There every leading row of
`EQ1, EQ2, EQ3, EQ4` and `O1s` carries the factor `(k - 2e)` in its `X`-column
and is therefore vacuous, while the `Y`-column is evaluated at `Y_{2e} = 0`.
This is exactly the degeneracy of `N(W) = eta^3 (W/eta^2)'`: its leader
`eta_e W_k (k - 2e)` vanishes precisely at `k = 2e`, i.e. when `W/eta^2` has no
top-order derivative. The leading-order method is blind there by construction.

```text
   OPEN[A2-N-DEGENERATE].  Decide the branch  deg X = 2e,  deg Y <= 2e-1
   of the corrected system.  The next order (the degree-(2e-1) coefficients)
   is the natural attack: at that order the inhomogeneity from level 2e is
   quadratic in the pins, exactly as in RAY Sec 3.6, but now with FIVE rows.
```

### 7.4 What (L2), the order side at `Z = 0`, gives

C32 Sec 1's degree/order duality transports every statement above verbatim with
`e -> epsilon = ord eta`, `g -> ord G`, `k -> ord X`, and every "`>`" reversed.
`ord Psi_1 = 2 epsilon + 1` exactly (from `8Zb^2 kappa eta^2`) against
`ord Lambda_1 = 3 epsilon + ord X - 1`, so the *same* determinant
`-6a(ord - 2 epsilon)^2 (c_0 + 2 epsilon)` governs an ascending ladder bounded
below by `2 epsilon + 1`. Combined with Sec 6 this squeezes `X` and `Y` into the
window `2 epsilon + 1 <= ord <= deg <= 4e - 1`; if `eta` is a monomial
(`epsilon = e`) the window is empty at `e = 1`, forcing `X = Y = 0` and hence
`kappa = 0` by `(D1)`.

I did **not** run the order side to the degree side's standard (the `Psi`
orders were not computed with generic tails), so this is typed **SKETCH, NOT
PROVED** and no cell is claimed on it. RAY Sec 3.6 records that at `(1,3)` the
order-`(top-2)` condition forces `eta = eta_1 Z`; whether `eta` is monomial in
general is **not** decided here.

## 8. Cell evidence, controls, and the global count (L4)

### 8.1 Cell `(1,3)` on the corrected system

The RAY driver was rebuilt with the corrected `EQ2` and with `O1s` added as a
sixth generator family (`/tmp/ubound/cellc.py`). Ring
`Q[A0,S0..S2,Q0..Q3,R0..R2,G0,G1,F0..F3,P0..P2,kappa,tt]`, grevlex, `a = b = 1`
by RAY's `(S1)`, `eta_e = 1` by `(S2)`, `s_sigma` **not** normalised (RAY `(C5)`;
there is no `Z`-scaling symmetry), saturation by the explicit variable `tt`.

```text
  OLD  EQ2, no O1  (RAY's system) : 22 vars, 37 gens, basis = [1], 2.1 s
  CORR EQ2, no O1                 : 22 vars, 37 gens, basis = [1], 0.6 s
  CORR EQ2, +  O1                 : 22 vars, 45 gens, basis = [1], 1.1 s
  OLD  EQ2, +  O1                 : 22 vars, 45 gens, basis = [1], 2.4 s
```

All four runs impose the wall `G_2 = -3`. Since replacing `EQ2old` by `EQ2`
changes the ideal in neither direction, this is a genuine re-decision of the
wall-imposed cell, not a transfer.

**The no-wall variant did not terminate.** RAY's no-wall run (`EQ2old`, 23
unknowns) took 13.2 s. With the corrected `EQ2` the same variant did **not**
finish in 550 s under sympy without `O1s`, nor in 1500 s with `O1s`. So

```text
  (1,3) EMPTY  is re-established here ONLY under the imposed wall G_2 = -3,
  which the corrected system no longer derives.  The no-wall decision that RAY
  reported is NOT re-established, and it was computed on the wrong EQ2.
  (1,3) therefore returns to the box01 queue alongside (1,5) and (1,7).
```

That non-termination is itself weak evidence that the corrected no-wall ideal is
not the unit ideal in an easy way — it is consistent with the `c`-line surviving
the top order (Sec 2.3) — but it is a statement about sympy's Buchberger, not
about the cell, and it is reported as such.

**Controls.** RAY's planted-solution negative control was not re-run (its
pipeline is unchanged; REV Sec 4 reproduces it: planted ideal non-unit, true
ideal unit). The controls run here are the four of Sec 2.2. `(1,3)` remains
**single-engine sympy** and **not promotion-grade**, as RAY typed it.

### 8.2 The global count, corrected (charge lead (L4))

RAY Sec 4's excess count is unchanged in order of magnitude by the P0. But the
count is not what closes anything. The elimination lead (L4) asks for is exactly
Sec 5: eliminating `q`, `r` and `p'` leaves **five equations in
`(eta, s, G, X, Y, kappa)`, three of them `s`-free** — a *triangular* system,
`EQ1/EQ2/EQ3` on `(eta, G, X, Y, kappa)` and `EQ4/O1s` carrying all the
`s`-dependence. Consequently the decisive computation is no longer per-cell in
`(e,U)` but per-`e` in `(eta, G, X, Y)` with `deg X, deg Y <= 4e-1` — a box whose
size depends on `e` **only**, a much smaller campaign than `A2-E1WALL-CELLS`.

```text
JOB  A2-DEVBOX (successor to A2-E1WALL-CELLS)
GOAL decide the s-free subsystem EQ1, EQ2, EQ3 for fixed e: eta generic of
     degree e (eta_e = 1), G generic of degree 2e with G_{2e} = c b eta_e^2,
     c free, X and Y generic of degree 4e-1, kappa free, a = b = 1 by (S1).
GENS every Z-coefficient of (D1), of (b/eta)EQ3 and of 2b^2 eta^2 EQ2, plus the
     saturation  kappa * (c+2e) * tt - 1.
SIZE e=1: 14 unknowns;  e=2: 22.  Tiny compared with A2-E1WALL-CELLS.
READ EMPTY(e) closes every U at that e except branch (B) and c in {-2e,-(2e+1)}.
     NONEMPTY(e) returns the (eta,G,X,Y,c,kappa) locus, which then feeds EQ4
     and O1s to decide sigma.
DO NOT impose the E1-wall: it is not derived on the corrected system.
```

I did not run `A2-DEVBOX`; the `s`-free reduction was reached late in this pass.
It is the single highest-value successor.

## 9. Ledger

**Ledger A — the horn's `A`-degree-2 census, corrected.**

```text
 BEFORE (RAY):  U < 3e-1, U = 3e-1, U = 3e all EMPTY;  U >= 3e+2 survives on
                Wall B with deg E1 <= 2e-2 and a 2-dimensional residual.
 AFTER (here):
   The E1-wall itself      NOT DERIVED.  The corrected Chamber II determinant is
                           identically zero; the whole c-line survives the top
                           order, in every chamber.
   U < 3e-1, U = 3e-1      HF's lone-family / pair-minor arguments there do not
                           use EQ2, but the simultaneous-top sub-branches used
                           the 3x3 determinant.  MUST BE RE-RUN.
   U = 3e (RAY-EDGE)       UNAFFECTED for e >= 2 (N1,N3,N4 only).
   RAY-2 (deg E1 <= 2e-2)  REFUTED; the residual is 3-dimensional.
   NEW, uniform            deg X, deg Y <= 4e-1 (c != -2e), U-free.
   NEW, per-c              U takes at most 4e explicit values for each fixed
                           (e,c) with c not in {-2e, -(2e+1), -(2/3)(1+3e)},
                           branch (B) excepted.
 OBSTRUCTION[A-DEGREE-TWO]: still NOT completed.  The lane moves from "an
 unbounded family of finite cells" to "a bounded box per e, plus two named
 degenerate branches", at the cost of un-deriving the wall.
```

**Ledger B — the `(B3)` windows: unchanged, and untouched here.** Nothing in
this pass touches `N`, `rho`, a cusp, a cover, `Z(G)`, `SCOPE[B3-QH]`, or any
transfer; every `(B3)` row stands as HF left it (HF Sec 5: "different
instruments on different objects ... They do not compose into a kill").

**What the coordinator must re-run.** In priority order:

```text
 P0-1  Re-issue SPEC's equation list with E2 corrected to include -2 q E1, and
       C32 Sec 6's `E2eq|_{G=0}+Delta_2` likewise (add -2qE1; the correction is
       not absorbed by either summand).
 P0-2  box01: cells (1,3), (1,5), (1,7) were run against EQ2old with the wall
       imposed.  RE-RUN all three with corrected EQ2, with O1s, and WITHOUT the
       wall (c free).  sympy does not reach the no-wall (1,3); msolve will.
 P0-3  Re-decide HF Chambers I and III simultaneous-top branches, and the
       Chamber II sub-branches c = -2e and U = 3e-1, on the corrected rows.
       Sec 6 already supplies unconditional deviation bounds there.
 P0-4  Re-type RAY-2 as REFUTED and the RAY residual as 3-dimensional.
       RAY-1's N1, N3, N4, RAY-DEP and RAY-EDGE(e>=2) stand.
```

## 10. FALLACY-v2 audit

* **Flag/place/series.** No flag, place or cover series occurs. The only
  separation is strict-below versus at-level in the `Z`-grading, made explicit
  every time: each `Lambda_j` is compared with its own `Psi_j` by an inequality
  between two *computed* degrees, never a nominal one.
* **Per-ray / exit-set charge.** No exit price; no `charge_basis` line. "Ray"
  is C32/HF's leader ray, not a valuation ray.
* **Carrier / attainment.** A2-DEV-BOUND and A2-U-BOUND are `REPRESENTATIVE`
  necessary conditions on a hypothetical surviving pair; no cell is claimed
  realised and no witness was constructed. `EMPTY` for `(1,3)` means emptiness
  of a coefficient variety.
* **Floor / attainment.** `deg X <= 4e-1` is an inequality; the case
  `X = Y = 0` is inside it and is separately excluded, by `(D1)` giving
  `kappa = 0`. `U <= 4e values` is a finiteness statement, not an exact value.
* **Pole / interior.** No pole identity used.
* **`sat()` wrapping.** Saturation is by an explicit variable `tt`; no `sat()`
  call, so no bare-ideal/list confusion. Ring, order and variable list declared
  in Sec 8.1. Unit ideal tested by the returned basis being `[1]`.
* **Raw remainder degree / vanished leaders.** Every leader that can vanish is
  branched: `(k-2e)` (three times; it is exactly branch (B)); `c+2e` (descent
  proviso); `c+2e+1` (Wall B); `3c+6e+2` (Wall A); `P(c)` (only improves the
  bound); `sigma-e`; `xi` versus `ups`. `deg V` was computed generically
  because its nominal leader cancels. `deg Psi_3` was recomputed after my own
  first transcription dropped a factor of `eta`; the corrected computation
  reproduces HF's `P(c)` exactly, which is the control that caught it. All
  divisions are exact series inversions or are cleared by the stated
  `eta`-power, never pointwise inversions at a root of `eta`.
* **Variable / ring map.** The Laurent-tail class, its degree convention,
  derivative and inversion are declared in `/tmp/ubound/tail.py` and were
  smoke-tested (`x.d()`, `x*x.inv() = 1`) before use; the Groebner ring, order
  and variable list are in Sec 8.1.
* **Prime label / derivative.** Every prime is `d/dZ`, per C32. `E1, E2, D1,
  D2, C1, C2` are polynomial names; `EQ1..EQ4, O0, O1, O1s, O2, E0` are
  equations; `X, Y, N, V, W1, R, P(c)` are named once each. `W1` is *not*
  HF's `w`.
* **Merge-free / M-descent, target/arrival index.** Not in play.
* **Not filled by cap or analogy.** The `EQ4` row was first *fitted* and the fit
  was wrong; it is now *derived* from the closed form `(D2)` and then checked
  at 36 triples. Branch (B) is reported as an open branch, not closed by
  analogy with branch (A). The order-side ladder (L2) is typed SKETCH and no
  cell is claimed on it. HF's `c = -2e` verdict is *not* imported, because its
  argument runs in the corrected-degenerate top-order system.

## 11. Typed verdict block

```text
LANE              A2-U-BOUND
SCOPE             C32's live section over C: a b kappa != 0, eta != 0, G != 0,
                  s != 0, e >= 1, r' != 0 (C32 T5), c5 = 0 (C32 shear), in the
                  simultaneous-top regime U >= 3e.  No (B3) object, no cusp, no
                  cover, no transfer, no Z(G).

P0 RAISED         SPEC:100-104's equation E2 omits the term  -2 q E1;
                  [A^2]Even = (SPEC's E2) - 2 q E1.  Confirmed by (i) rebuilding
                  all seven equations from SPEC's own Even/Odd (six exact, one
                  off by -2qE1), (ii) the review-corrected [A^4]Even display
                  reproducing exactly from the same block, (iii) SPEC's own
                  positive control at J=1..4, (iv) C32 Sec 6 reproducing SPEC's
                  E2 exactly, hence inheriting it.  BLAST RADIUS: HORN-A2's
                  Chamber II determinant -> 0 identically in all chambers; the
                  E1-wall is not derived; N2 loses its epshat column; RAY-2
                  REFUTED; box01 cells (1,3),(1,5),(1,7) must be re-run.
                  RAY-DEP, RAY-EDGE(e>=2), C32 T1-T5 and HF's non-EQ2
                  arguments are unaffected.

PROVED HERE       O0-IDENT      O0 <=> EQ4 modulo E0, on s != 0; only O1 was
                                absent.  O1 transcribed, verified = [A^1]Odd,
                                p'-free form (O1s) given; its top vanishes on
                                the ray at every c, so it is leading-order inert.
                  DEV-FREE      In X = 4b eta^2 r - s^2, Y = 4b^2 eta q - 3a s^2,
                                EQ1, EQ2, EQ3 are exactly s-free; closed forms
                                (D1) for EQ1 and (D2) for EQ4's quadratic part.
                                RAY-1's whole residual is deg X, deg Y <= 2sigma-2.
                  RAY-SHADOW    The ray is the leading order of the kappa = 0
                                family: on r = s^2/(4b eta^2),
                                q = 3a s^2/(4b^2 eta) one has EQ1 = 2Z kappa and
                                EQ4 = kappa E1 exactly.
                  A2-DEV-BOUND  deg X, deg Y <= 4e-1 (Ch. II with c != -2e;
                                Ch. III unconditional), <= 2g-1 (Ch. I).
                                UNIFORM IN U.  Determinant -6a(k-2e)^2(c+2e).
                  A2-EQ4-HOM    The EQ4 row is homogeneous at every level; its
                                exact form is displayed.
                  A2-U-BOUND    Dichotomy (A)/(B) of Sec 7.2.  On (A), for each
                                fixed (e,c) outside three explicit values U
                                takes at most 4e values, given explicitly; on
                                Wall A branch (A) is empty.
                  All PROVED-HERE, UNREVIEWED.

VERIFIED          Even/Odd vs SPEC's positive control, J = 1..4; all seven
                  residual equations vs Even/Odd; [A^4]Even, [A^5]Even = 0,
                  [A^3]Odd = 0; Chamber II rows and determinants, 42 cells,
                  e <= 7; the ray annihilates all five tops, 6 cells, every c;
                  Lambda_1, Lambda_3 leaders ratio 1 at 12 (e,k) pairs and
                  Psi_3 ratio 1 at 14 (e,g) pairs, all with generic tails;
                  deg V = 3e-2 at e = 1..4; Q_4 closed form exact; Lambda_4
                  degree at 18 cells and the EQ4 row at 36 triples;
                  det(EQ1,EQ4) + 6a(k-2e)R = 0 identically.

CAS-DECIDED       (1,3) EMPTY on the corrected system WITH THE WALL IMPOSED,
                  with and without O1s.  SINGLE ENGINE (sympy 1.14.0), NOT
                  promotion-grade.  The no-wall variant did not terminate in
                  1500 s, so RAY's wall-free (1,3) kill is NOT re-established.

CONSUMED          C32: T1, T2 (Xi), (1.1), T3, T5, E0 -- each re-derived or
                    re-verified here before use.  SPEC: Even/Odd, the
                    parametrisation, [A^4]Even.  HF: the Chamber II coordinates
                    and P(c), reproduced not trusted; HORN-A2's wall clause is
                    NOT consumed (P0).  RAY: N1, N3, N4, RAY-DEP,
                    RAY-EDGE(e>=2) at REV's CONFIRMED typing; N2/RAY-2 NOT
                    consumed (P0).  N2D: only as the source of the E1-family
                    bookkeeping the P0 corrects.

NOT CLAIMED       closure of the horn;  of OPEN[A2-CELL-32];  completion of
                  OBSTRUCTION[A-DEGREE-TWO];  any (B3) statement;  emptiness of
                  branch (B) or of c in {-2e, -(2e+1)};  an unconditional
                  U-bound;  promotion-grade emptiness of any cell;  that eta is
                  forced monomial;  any order-side (Z = 0) cell verdict;  the
                  wall-free (1,3) kill.

OPENS RAISED      OPEN[A2-WALL-REDERIVE]   Pin c on the corrected system.  This
                                           is what OPEN[A2-U-BOUND] reduces to.
                                           Highest value: it restores HORN-A2
                                           and, with Sec 7, closes U outright.
                  OPEN[A2-N-DEGENERATE]    Branch (B): deg X = 2e, deg Y < 2e,
                                           invisible to every leading row.
                  OPEN[A2-DEVBOX]          Run the s-free subsystem per e; the
                                           box size depends on e only.
                  OPEN[A2-ORDER-LADDER]    Complete the Z = 0 dual of Sec 6 to
                                           generic-tail standard; if it closes,
                                           X and Y are squeezed from both ends.

OPENS RESOLVED    OPEN[A2-O0-O1]  RESOLVED.  O0 was never missing; O1 is
                                  transcribed here and is leading-order inert.

DEVIATIONS        (1) The charge asked me to consume HORN-A2 and RAY-1/RAY-2 at
                      their reviewed typings.  I ran a transcription control
                      first, it failed, and I could not consume them.  Sec 2 is
                      the evidence; the charge's basis is corrected, not
                      reinterpreted.
                  (2) The charge's expectation that O0 and O1 turn "four
                      conditions on five unknowns" into "six on five" is not
                      what happens.  O0 was already present; O1 is inert at
                      leading order.  What breaks the ladder is the change of
                      variables, not more equations.
                  (3) One intermediate transcription of Psi_3 dropped a factor
                      of eta.  It was caught by the P(c) control and redone;
                      the corrected computation is what Sec 6 reports.  The
                      Lambda rows were never affected.
                  (4) A2-DEVBOX was specified but not run.
                  (5) Drivers left in /tmp/ubound, not installed in box/.
```

<!-- BODY-END -->
