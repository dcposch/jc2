# RAY-KILL-REVIEW - hostile gate of RAY-1/RAY-DEP/RAY-EDGE/RAY-2

Lane: `RAY-KILL-REVIEW`.  Reviewer: GPT-5.  Date: 2026-09-02.

## 0. Custody and Scope

Before reading the inputs or running algebra I verified the two frozen copies
specified in the charge:

```text
3d08b8996227e292d76e0ba3901cfad16099f347f97129d27b6bf5b3bc253f0a  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.epUu4p/inputs/ray-kill-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.epUu4p/inputs/horn-flagship-opus5-20260902.md
```

Both matched exactly.  I abbreviate these frozen files as `RAY` and `HF`.

One source issue matters.  The frozen `RAY` prose gives the Groebner generator
list and the closed Wall-B form of `EQ1` and `EQ4`, but it does not print the
full `EQ2` formula.  The workspace copy of
`xmodel/cell-32-termination-opus5-20260901.md` has SHA-256
`d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b`,
matching the C32 hash recorded in the charged lane run receipt, and displays
`E2eq|_{G=0}+Delta_2`.  I used that local C32 copy, plus the `/tmp/raykill`
driver left by the charged run, for the executable Groebner replay.  That is
valid as a rerun of the lane's available transcription, but the two-file frozen
packet alone is not self-contained for `EQ2`.

No web search was used.  No exit price is asserted here, so no `charge_basis`
line is present.

## 1. Verdicts

```text
RAY-1       GAP.
            The displayed 4x5 row system matches every executable replay I ran,
            and N1/N3/N4 replay exactly.  But RAY itself types N2 as MEASURED,
            interpolated from CAS checks rather than derived in prose
            (RAY:233-241).  As a theorem-level proof of the full 4x5 system,
            that is still a gap.

RAY-DEP     CONFIRMED.
            The dependency is an exact polynomial identity.  All coefficient
            residuals are zero.

RAY-EDGE    CONFIRMED for e >= 2.
            P(-(2e+1)) has no root for e >= 2, and the RAY-DEP obstruction
            gives inconsistency when n=2e >= 4.  The e=1 boundary cell is
            confirmed as a single-engine sympy Groebner decision, but remains
            only single-engine.

RAY-2       GAP as an unconditional promoted theorem; CONFIRMED conditional on
            the displayed N2 row.
            The substitution algebra and E1 coefficient cancellation are exact.
            The only weakness is inherited from RAY-1/N2.

2D residual CONFIRMED as a formal consequence of the displayed next-order
            system.  The denominators used in the pins are sourced from degree
            leaders and the HORN-A2 ray.

Per-cell    CONFIRMED as a finite polynomial decision problem with more
finite/     equations than unknowns.  NOT confirmed as a theorem that each
overdet.    residual variety is finite or empty.

U-bound     CONFIRMED OPEN.
            Nothing in RAY or HF bounds U for fixed e; the surviving cells are
            U = 3e+2, 3e+4, ... .

Ledger      CONFIRMED on the B3 correction.
            HF section 5 says the A2 and B3 instruments are different objects
            and do not compose.  A ray kill closes no B3 degree windows.
            The extra phrase "one OBSTRUCTION[A-DEGREE-TWO] layer" is not
            sharply sourced in the frozen text; see section 6 below.

Controls    CONFIRMED for the two spot-checks run here: C3 and C5.
```

## 2. RAY-DEP Replay

I used the row convention in `RAY:214-231`:

```text
N3 = beta - gamma + delta/2 - rho
N1 = alpha - beta + delta/2
N4 = n alpha - 2 beta - (n-2) gamma + (n-1) delta
N2 = (2n-2e-3)alpha - 2(3n+2e-4)beta
     + (4n+2e-5)gamma - (n-1)delta - epshat
```

The claimed dependency is

```text
n*N1 + (n-2)*N3 - N4 = -(n-2)*rho.
```

Sympy 1.14.0 over `QQ[n,e,alpha,beta,gamma,delta,rho,epshat]` returned:

```text
RAY_DEP_identity_residual = 0
coefficients:
  alpha: 0
  beta:  0
  gamma: 0
  delta: 0
  rho:   0
constant: 0
```

Coefficient-by-coefficient, before simplification:

```text
alpha:  n - n = 0
beta:  -n + (n-2) + 2 = 0
gamma: -(n-2) + (n-2) = 0
delta:  n/2 + (n-2)/2 - (n-1) = 0
rho:   -(n-2) + (n-2) = 0       after moving the RHS to the left
```

This confirms `RAY:257-264` exactly.  Since the identity uses only `N1,N3,N4`,
the dependency and the e>=2 edge obstruction do not depend on the measured
status of `N2`.

The homogeneous coefficient matrix of the four displayed rows, in unknowns
`alpha,beta,gamma,delta,epshat`, has symbolic rank 3:

```text
rank = 3
all five 4x4 minors = 0
3x3 minor using rows N1,N3,N2 and columns alpha,gamma,epshat = 1
```

Thus the displayed rows have exactly the advertised rank behavior away from
inhomogeneous inconsistency.

## 3. RAY-EDGE and the Chamber-II Polynomial

`RAY:276-282` identifies the boundary inhomogeneity with HF's chamber-II
polynomial

```text
P(c) = 4e^2(2e-1) + 4ce(2e-1) - c^2(6e+1)
rho = -P(-(2e+1)) * b^2 eta_e^4 / ((4e-2) s_sigma^2).
```

The same `P(c)` is printed in `HF:539-551`.  Exact substitution gives

```text
P(-(2e+1)) = -32e^3 - 32e^2 - 6e - 1.
```

Let

```text
Q(e) = 32e^3 + 32e^2 + 6e + 1 = -P(-(2e+1)).
```

Sympy over `QQ[e]` reports:

```text
factor_QQ(Q)        = 32e^3 + 32e^2 + 6e + 1
discriminant(Q)     = -38912
count_roots(2, oo)  = 0
count_roots(R)      = 1
real root interval  = (-759248/928877, -1299323/1589614)
Q(2)                = 397
Q'(e)               = 2(48e^2 + 32e + 3)
```

The isolated real root is negative, approximately `-0.8174`; the other two
roots are non-real.  In particular `Q(e) != 0` for every integer `e >= 2`.
Also `Q'(e) > 0` for every `e >= 0`, so the simpler monotonic proof from
`Q(2)=397` is valid after the exact root check.

For `U=3e`, `n=U-e=2e`.  If `e >= 2`, then `n-2 != 0`.  RAY-DEP then forces

```text
0 = n*N1 + (n-2)*N3 - N4 = -(n-2)*rho,
```

but `rho != 0` because `a,b,eta_e,s_sigma` are nonzero on the live ray and
`Q(e) != 0`.  Hence the boundary slice is inconsistent for `e >= 2`.

Verdict: `RAY-EDGE e>=2` is confirmed.  This proof does not consume `N2`.

## 4. Degenerate Cell (e,U)=(1,3)

The charged report states that the remaining `n=2` case is the single cell
`(e,U)=(1,3)` and is decided by an exact sympy Groebner basis
(`RAY:352-390`).  I reran the cell.

Engine and ring:

```text
engine:  python3, sympy 1.14.0
field:   QQ
order:   grevlex
cell:    e=1, U=3, g=2, m=3, n=2, sigma=2
vars:    A0,S0,S1,S2,Q0,Q1,Q2,Q3,R0,R1,R2,G0,G1,
         F0,F1,F2,F3,P0,P1,P2,kappa,tt
count:   22 variables, 37 generators
```

The generators are coefficientwise vanishing of

```text
EQ1, EQ2, EQ3, EQ4,
T1: eta*Phi - s*G,
E0: 2(q*r' - p'*s) - kappa,
saturation: S2*Q3*R2*kappa*tt - 1.
```

with `a=b=1`, `eta=Z+A0`, and Wall B imposed as `G=-3Z^2+G1 Z+G0`.

The rerun output was:

```text
basis_len = 1
basis     = ['1']
unit      = True
time      = 2.236 s
```

I also reran the no-wall variant:

```text
wall not imposed: 23 variables, 37 generators
basis_len = 1
basis     = ['1']
unit      = True
time      = 13.275 s
```

The planted-solution negative control in the same pipeline returned:

```text
planted control: 37 generators, 22 vars, planted point verified a zero
PLANTED ideal is unit? False
TRUE    ideal is unit? True
```

So the operational Groebner claim is confirmed: the available sympy
transcription returns the unit ideal.

Transcription check:

* `EQ1` in the driver is C32 `(1.1)`, matching `C32:99-105`.
* `EQ3` is `eta Z^2 Xi - (3a/b)(Z eta^2 G^2)'`, matching `C32:241-255`.
* `EQ4` is C32 `(2.2)` from `O0+E0`, matching `C32:586-590`.
* `T1` is implemented as `eta*Phi-s*G=0`, avoiding division by `eta`; this
  matches `C32:177-203`.
* `EQ2` in the driver matches the C32 displayed `E2eq|_{G=0}+Delta_2`
  formula at `C32:631-642`.

Against `RAY:146-157`, the closed Wall-B identities also check:

```text
E1 = b eta chi + G
G  = E1 - b eta chi
D1 = a eta^2 phi + d eta G
   = a eta^2(phi - 3chi/2) + d eta E1
   = -a eta^3/2 + d eta E1

C1 = d(psi s + Phi/(2b)),  Phi=sG/eta
   = d(psi s + sE1/(2b eta) - s chi/2)
   = (d/2)(s eta + Theta/b),  Theta=sE1/eta.
```

The only caveat is archival: `EQ2` is not fully printed in the two frozen
inputs.  It is printed in the local C32 report whose hash matches the charged
lane receipt, but a future standalone replay should freeze that file or embed
the full driver.

Verdict: `(1,3) EMPTY` is confirmed as a sympy/QQ Groebner decision.  It is not
multi-engine promotion-grade by itself.

## 5. RAY-2 and the Pins

For survivors `U >= 3e+2`, the displayed system has `rho=0`.  Solving only
`N1=N3=0` gives

```text
alpha = beta - delta/2
gamma = beta + delta/2
```

Substitution into `N4` gives zero identically.  Substitution into `N2` gives

```text
N2 = -4e*beta + 2e*delta - epshat.
```

Thus `N2=0` is equivalent to

```text
epshat = 2e(-2 beta + delta) = -4e(beta - delta/2) = -4e alpha.
```

Finally,

```text
E1_{2e-1} = b eta_e^2 (4e alpha + epshat) = 0.
```

The sympy replay returned:

```text
N1_after_pins = 0
N3_after_pins = 0
N4_after_pins = 0
N2_after_N1_N3 = -4*beta*e + 2*delta*e - epshat
epshat_solution = [2*e*(-2*beta + delta)]
E1_coeff_after_N2 = 0
```

No division by `e` is used.  The scope has `e>=1`, but even that is not needed
for this algebraic cancellation.

The second-order pins in `RAY:318-328` are therefore the same solution written
back in coefficient language:

```text
eta_{e-1}/eta_e = s_{sigma-1}/s_sigma - r_{n-1}/(2 r_n)
q_{m-1}/q_m     = s_{sigma-1}/s_sigma + r_{n-1}/(2 r_n)
G_{2e-1}        = -4e b eta_e eta_{e-1}.
```

Nonzero denominators are sourced as follows.

```text
eta_e != 0       by e = deg eta.
s_sigma != 0     by sigma = deg s, and HF live section has s != 0.
a,b,kappa != 0   by HF live section (HF:559-560).
r_n != 0         either by n = deg r in the simultaneous-top regime, or from
                 the HORN-A2 ray r_n = s_sigma^2/(4b eta_e^2) (HF:565-569).
q_m != 0         from q_m = 3a s_sigma^2/(4b^2 eta_e) (HF:568).
```

The derivation does not divide by `epshat`, by `E1_{2e-1}`, or by the
inhomogeneity `rho`.

Verdict: the RAY-2 algebra and the pins are confirmed conditional on the
displayed `N2` row.  Since `RAY` itself says `N2` is measured rather than
derived (`RAY:233-241`), I do not promote RAY-2 as an unconditional theorem.

## 6. Residual, Per-Cell Finiteness, and U

The rank calculation above gives a two-dimensional affine solution set for the
next-order variables in the normalized system: five unknowns, rank three, and
free parameters `(beta,delta)`.  This confirms the displayed residual
parametrization in `RAY:318-328`, subject to the same `N2` typing caveat.

For the finite-cell claim, `RAY:399-455` specifies a finite polynomial system
for every fixed `(e,U)`: generic polynomials of fixed degrees, coefficientwise
vanishing of `EQ1..EQ4,T1,E0`, and one explicit saturation variable.  I built
several of these systems using the lane builder before stopping the large
expansion.  The counts matched the charged pattern; examples:

```text
(e,U)=(1, 3): vars=22  eqs=37
(e,U)=(1, 5): vars=30/31 depending on whether the illegal S-normalization is
              suppressed; the charged no-S-normalization count is 31, eqs=52
(e,U)=(2, 8): vars=46/47 with the same convention; charged count 47, eqs=84
(e,U)=(4,12): vars=70, eqs=133
```

The "grossly overdetermined" statement is only an equation-count statement.
It is not a proof that the algebraic set is zero-dimensional, finite as a set
of points, or empty.  `RAY:423-425` correctly calls emptiness a naive dimension
expectation, not a theorem.

For fixed `e`, the surviving cells remain

```text
U = 3e+2, 3e+4, 3e+6, ...
```

I found no bound on `U` in `RAY` or `HF`, and `RAY:427-433` explicitly records
this as `OPEN[A2-U-BOUND]`.  Therefore no finite cell campaign closes even one
fixed `e` without a new argument bounding `U`.

Verdict: finite per-cell decision problem confirmed; global closure remains
open.

## 7. Ledger Against HF Section 5

HF section 5 is explicit:

```text
"(1)-(2) and (3) are different instruments on different objects..."
"They do not compose into a kill, and I do not claim one."
```

This is at `HF:586-589`.  The per-window ledger then keeps `(B3)` open in the
relevant rows (`HF:591-604`).  So the charged premise that a ray kill would
close `(B3)` windows is wrong.

What a full ray kill would close:

```text
1. The horn/A2 residual it actually addresses: at least
   OPEN[A2-CELL-32-E1WALL] as restated by RAY.

2. If "full ray kill" is defined broadly enough to include the T5 r'=0
   leftover and every residual subcase of the A-degree-two horn census, then it
   would close OPEN[A2-CELL-32].

3. It would advance the explicit-pullback part of
   OBSTRUCTION[A-DEGREE-TWO].  Whether that is exactly "one layer" is not
   sharply defined in HF section 5 or in RAY section 6.
```

What it would not close:

```text
1. No (B3) N-window: not N=4, not 5..7, not 8..10, not 11..16, not N>=17.
2. No H2 all-degree branch.
3. No B3 cusp quasi-homogeneity gap.
4. No global center or CENTRAL-RANK issue.
5. No monodromy/cusp/cover assertion, because the A2 variables
   (eta,s,p,C1,q,r,G) are not a B3 profile.
```

There is an internal wording tension in `RAY`: the up-front summary says a ray
kill closes `OPEN[A2-CELL-32]` plus one obstruction layer (`RAY:69-73`), while
the detailed ledger says the present pass leaves the T5 leftover unchanged and
does not complete `OBSTRUCTION[A-DEGREE-TWO]` (`RAY:548-565`).  I read this as
"a hypothetical full kill of all A2 residuals would move the horn ledger, not
the B3 ledger."  The B3 correction is confirmed; the exact "one layer" phrasing
needs a coordinator definition before it can be promoted.

## 8. Control Spot-Checks

I spot-verified two of RAY section 2's five controls.

### C3: Chamber-II Determinant, Wall B, and Pair Minors

Using the chamber-II rows printed in `HF:471-507`, with `g=2e`,
`m=U`, `n=U-e`, and `sigma=(U+e)/2`, sympy gives

```text
det_general = -36*(-U + e)*(c + 2e)*(c + 2e + 1)
det - 36*(U-e)*(c+2e)*(c+2e+1) = 0.
```

On Wall B, `c=-(2e+1)` and `U=n+e`, the rows are exactly

```text
[12, -8n, 3n]
[-3, 0, 3n/4]
[6, -4e-8n+2, 3e+9n/2-3/2]
```

Multiplication by the claimed ray `(n/4, 3/4, 1)` gives

```text
wall_times_ray = [0, 0, 0]
rank_wall_generic = 2
```

The two-row pair minors for `EQ3,EQ1` are

```text
{r,q}: -24n
{r,s}:  18n
{q,s}:  -6n^2
```

matching `RAY:105-118`.  This control is confirmed.

### C5: Legal Scalings

I reran `/tmp/raykill/t14_scaling.py`.  For the `(a,b)` scaling

```text
a -> alp*a, b -> bet*b, s -> bet*s, q -> alp*q,
r -> bet*r, G -> bet*G, p' -> alp*p', kappa -> alp*bet*kappa
```

the residuals were exactly

```text
EQ1: 0
EQ2: 0
EQ3: 0
EQ4: 0
E0:  0
```

For the `mu` scaling, the only p'-weight that makes all five residuals vanish
is the one printed in RAY:

```text
eta -> mu eta, s -> mu^2 s, q -> mu^3 q, r -> mu^2 r,
G -> mu^2 G, p' -> mu^3 p', kappa -> mu^5 kappa

EQ1: 0
EQ2: 0
EQ3: 0
EQ4: 0
E0:  0
```

The same script shows the nearby wrong choices fail in `E0`:

```text
p'-weight mu^4: E0 residual = 2*mu^5*(1-mu)*p'(Z)*s(Z)
p'-weight mu^5: E0 residual = 2*mu^5*(1-mu^2)*p'(Z)*s(Z)
```

This confirms that `a=b=1` and `eta_e=1` are licensed, while normalizing
`s_sigma` is not licensed by these scalings.  RAY's warning against `Z`
normalization is therefore consistent with the executable scaling residuals.

## 9. Typed Close

```text
CONFIRMED:
  RAY-DEP exactly.
  RAY-EDGE for e>=2 exactly.
  P(-(2e+1)) nonvanishing on e>=2 by exact root isolation.
  (e,U)=(1,3) unit ideal under sympy/QQ/grevlex, basis [1].
  RAY-2 algebra and second-order pins conditional on displayed N2.
  Two-dimensional residual conditional on displayed next-order system.
  Per-cell finite polynomial decision problem and overdetermined counts.
  OPEN[A2-U-BOUND].
  Ledger correction: no B3 window closes from an A2 ray kill.
  Control layers C3 and C5.

GAP:
  RAY-1 as a fully proved theorem, because N2 is explicitly MEASURED in RAY.
  RAY-2 as an unconditional promoted theorem, because it consumes N2.
  Frozen-packet reproducibility of the Groebner transcription, because full
  EQ2 is not printed in the two frozen inputs.
  The phrase "one OBSTRUCTION[A-DEGREE-TWO] layer" without a precise layer
  definition; the B3 non-composition part is still confirmed.

REFUTED:
  None of the replayed algebraic identities.  The only refuted premise is the
  external charge premise that an A2 ray kill closes B3 windows.
```

Bottom line: the charged report contains a real and exact boundary kill.  It
does not contain a promotion-grade proof of the full next-order 4x5 theorem,
because the `N2` row is measured rather than derived.  The ledger correction
against `(B3)` is correct: a full A2 ray kill is not a B3 window kill.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16871`.
- Body SHA-256:
  `1e5bdd0de85c6aa451b0ed73a2b0e91d936954a91f0d25135ea2b0f06e8e1bc2`.
- Frozen basis: `a81e44a51fc72b9b5fa5ecfb1f6cb8bee9e6d606`.
