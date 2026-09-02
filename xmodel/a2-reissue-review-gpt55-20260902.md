# A2-REISSUE-REVIEW - hostile computational review

Lane: `A2-REISSUE-REVIEW`. Date: 2026-09-02. Reviewer: GPT-5.5.

No `charge_basis` line: this report asserts no exit-price claim.

## 0. Custody and local method

I first hashed the frozen read-only inputs in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.cQ22za/inputs`.
All five hashes matched the charge exactly:

```text
8fb070799d2666502b2a850a5d347ef59bd332231a40eaa2546b986d82be6baa  a2-dev-projection-sol56-20260902.md
f4945ca9bb57555d8101705d6aee6d167bacac4faf6d8e4d0e8bbe62fd748797  a2-dev-projection-sol56-20260902.py
68c4802f4c4909389eea13bae09c75f744a5c4cbde0a9db76b7237c3b03f20b5  a2-e2-p0-gate-gpt55-20260902.md
86caf003268ddc40143daa68d439079dbd82d1dac41e1da93f33a661d52f96ac  cell-32-spec-sol56-20260901.md
d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b  cell-32-termination-opus5-20260901.md
```

Local tools used: Python 3.14.7, SymPy 1.14.0, `/opt/homebrew/bin/Singular`,
and `/opt/homebrew/bin/msolve` present. `msolveio` is absent from the base
interpreter, so my independent two-engine ideal checks use SymPy and Singular,
not the charged msolve adapter. No canonical ledger was edited. `jc2-lean` was
not inspected.

I abbreviate the charged reissue as `SOL`, the Python generator as `GEN`, the
prior gate as `GATE`, and the two CELL-32 inputs as `SPEC` and `C32`.

## 1. Verdict table

```text
1. Seven source rows and EQ2_even correction:        CONFIRMED.
2. Corrected T2 G' sign from E3:                    CONFIRMED.
3. T1 and O1s/DET-EO derivations:                   CONFIRMED.
4. e=1,2,3 capped deviation unit ideals:            CONFIRMED, scoped.
5. T4 e=0 restoration:                              CONFIRMED.
6. Typed OPENs and retracted-item audit:            CONFIRMED.
Promotion recommendation: PROMOTE SOL with its typed scope only.
```

The important qualifier is item 4: the unit ideals certify emptiness of the
declared capped branch-(A) necessary subsystem. They do not certify an entire
chamber, any uncapped `c=-2e` case, Chamber I, or `e>=4`.

## 2. Charged generator and independent seven-row extraction

I ran the charged generator:

```text
python3 a2-dev-projection-sol56-20260902.py check
```

It returned `status=PASS`, with no failures. Its zero checks included the seven
source residual diffs, whole `Odd`/`Even`, the forbidden higher coefficients
`A3_Odd`, `A4_Even`, `A5_Even`, T1, corrected T2, O1s, DET-EO, the three
deviation clearings, T4 finite ideals, and both controls. Its stale-source
canary was

```text
actual_EQ2_even - SPEC_EQ2_even_old
= -4*Z*b*eta*q*eta' - 2*b*eta^2*q - 2*G*q
= -2*q*((b*Z*eta^2)' + G)
= -2*q*E1.
```

I then rebuilt `Even` and `Odd` independently from SPEC's definitions
(`SPEC:51-80`): `P,Q,R0,S0`, `H=A+A^2Z`, `chi=2+4AZ`, and the three operators
`J`, `WA`, `WZ`. I did not import GEN. Direct coefficient extraction gave:

```text
[A^0]Odd  - O0        = 0
[A^1]Odd  - O1        = 0
[A^2]Odd  - O2        = 0
[A^0]Even - kappa - E0 = 0
[A^1]Even - EQ1_even  = 0
[A^2]Even - EQ2_even  = 0
[A^3]Even - EQ3_even  = 0
```

and also

```text
[A^3]Odd = 0,     [A^4]Even = 0,     [A^5]Even = 0.
```

Against SPEC's old displayed `[A^2]Even` row, the independent extraction gives
exactly

```text
[A^2]Even = SPEC_EQ2_even_old - 2*q*E1,
E1 = (b*Z*eta^2)' + G.
```

No other displayed residual row has a discrepancy. This matches GATE's P0
finding (`GATE:43-65`) and SOL's canonical replacement block (`SOL:62-160`).
Item 1 is therefore CONFIRMED.

## 3. T1, T2, O1s, and DET-EO

I used the corrected rows, with `c5=0` only through the live target shear
identified in SOL (`SOL:170-213`) and C32 (`C32:84-97`). No wall equation was
imposed.

For T1, with

```text
d = 3a/(2b),      psi = (Z*eta)',
M(W)  = 2Z*eta*W' - eta*W - 4Z*eta'*W,
M2(W) = 2Z*eta*W' - eta*W - 2Z*eta'*W,
C1 = d*h,         h0 = psi*s,
```

my expansion of corrected `O2` returned

```text
O2 + 6a*eta*M2(h-h0) - (3a/b)*M(sG) = 0
M(sG) - 2b*eta*M2(sG/(2b*eta)) = 0.
```

The top coefficient multipliers for `M` and `M2` are odd, and the rational
kernel check is the same Euler valuation computation used by SOL: for
`W=eta*v`, `M2(W)=eta^2(2Z*v'-v)`, whose lowest Laurent coefficient is
multiplied by `2m-1`. Thus the rational kernel is zero. The unique rational
candidate is polynomial exactly when `eta | sG`, giving the wall-free T1:

```text
eta | sG,
C1 = (3a/(2b))*((Z*eta)'*s + sG/(2b*eta)).
```

For T2 I substituted this T1 expression into the corrected `EQ3_even`. With

```text
Xi = 12ab*eta^3*eta'*(eta'+2Z*eta'')
   + 4d*s*(eta*s'-eta'*s)
   + 8b*eta*(q*eta'-q'*eta)
   + 12a*eta^3*r'
   + 12a*eta*((eta*eta''-(eta')^2)*G + eta*eta'*G')

Kminus = eta*G^2 + 2Z*eta'*G^2 - 2Z*eta*G*G',
```

the exact diff was

```text
EQ3_even - (Z^2*Xi - (3a/b)*Kminus) = 0.
```

The old derivative bracket is

```text
(Z*eta^2*G^2)'/eta
= eta*G^2 + 2Z*eta'*G^2 + 2Z*eta*G*G',
```

so `Kminus - old_bracket = -4Z*eta*G*G'`. Equivalently, the right-hand sides
differ by `12Z*a*eta*G*G'/b`. The monomial regression from GATE also matches:

```text
a=b=1, eta=Z, G=Z^2, s=q=r=0
source EQ3_even        = 27*Z^5
corrected T2 right side = 27*Z^5
old derivative form     =  3*Z^5
```

This confirms the repaired negative sign in the final `G'` term
(`SOL:216-238`, `GATE:108-125`). Item 2 is CONFIRMED.

For the p-prime-free row, my exact identity was

```text
O1s - (s*O1 - 4*E2*E0) = 0.
```

No division by `s` is present; equivalence with `O1` requires a later live
`s!=0` statement. For the determinant checksum I used

```text
W = q*s' - q'*s,
T = -(C1*E1'-C1'*E1)/2 - 3D1*s'/4 + D1'*s/4 - Z*W/2,
DET_EO = (sC1-qE1)T + (W/2)(sC2-qE2) + (kappa/2)(E1C2-C1E2).
```

The exact diff between this expression and the augmented determinant of the
three affine rows in `(r',p')` was zero. Thus `E0=O0=O1=0` implies
`DET_EO=0`, but DET-EO is only a checksum, not an extra generator. Item 3 is
CONFIRMED.

## 4. Independent capped deviation generator

I wrote an independent in-memory generator from the corrected source rows. It
does not import GEN and does not use SOL's pre-displayed `F1,F2,F3`. The script:

1. substitutes T1 and `c5=0`;
2. uses `E0` only to replace `4Z(qr'-p's)` by `2*kappa*Z` in `EQ1_even`;
3. substitutes

```text
r = (s^2+X)/(4b*eta^2),
q = (3a*s^2+Y)/(4b^2*eta);
```

4. clears exactly as

```text
F1 = 4b^2*eta^2*EQ1_even,
F2 = 2b^2*eta^2*EQ2_even,
F3 = b*EQ3_even.
```

As a preflight, all three source-derived `F` rows had denominator `1` and
contained no `s`, `s'`, or `s''`. This reproduces SOL's source-free deviation
claim (`SOL:347-413`) without trusting the charged generator.

For fixed `e>=1`, my ring and ansatz were:

```text
eta = Z^e + sum_{0<=j<e} eta_j*Z^j,
G   = c*Z^(2e) + sum_{0<=j<2e} G_j*Z^j       main stratum,
G   =             sum_{0<=j<2e} G_j*Z^j       c=0 stratum,
X   = sum_{0<=j<4e} X_j*Z^j,
Y   = sum_{0<=j<4e} Y_j*Z^j,
a=b=eta_e=1, c5=0.
```

The declared cap is exactly `deg X, deg Y <= 4e-1`. I used it only where SOL
licenses it: Chamber II with `c!=-2e`, and Chamber III at `c=0`
(`SOL:427-455`). The mathematical coefficient ring in the main stratum was

```text
QQ[eta0..eta(e-1), G0..G(2e-1), X0..X(4e-1),
   Y0..Y(4e-1), kappa, tt, c],
```

with variable order

```text
eta0,...,G0,...,X0,...,Y0,...,kappa,tt,c.
```

The `c=0` stratum removes `c` from the ring and removes the `c*Z^(2e)` term
from `G`. Saturation was by explicit Rabinowitsch equation only:

```text
main:  kappa*c*(c+2e)*tt - 1
c=0:   kappa*tt - 1
```

I did not call a `sat()` wrapper. SymPy used `grevlex` over `QQ`; Singular used
`dp` in the same variable sequence. Since the full ideal is `(1)`, the
elimination ideal `J_e = I_e cap QQ[c]` is also `(1)` in the main stratum.

The two-engine results were:

```text
e  branch  vars  gens  Z-degrees       SymPy           Singular
1  main      14    20  (5, 6, 5)       unit, 0.10s     unit
1  c=0       13    20  (5, 6, 5)       unit, 0.11s     unit
2  main      25    39  (12, 13, 10)    unit, 2.02s     unit
2  c=0       24    39  (12, 13, 10)    unit, 4.84s     unit
3  main      36    58  (19, 20, 15)    unit, 17.24s    unit
3  c=0       35    58  (19, 20, 15)    unit, 56.45s    unit
```

This extends the requested `e=1,2` reproduction to `e=3` as well. It agrees
with SOL's job census and claimed unit ideals (`SOL:461-483`, `SOL:533-544`),
using a different second engine because `msolveio` was not installed here.

The planted negative control was also rebuilt independently from raw
`Even/Odd`, with

```text
a=b=1, eta=s=Z, G=-2Z^2, c5=0, kappa=0,
p=0, C1=3Z^2/2, q=3Z/4, r=1/4.
```

It gave

```text
raw Even = 0, raw Odd = 0,
X = 4*eta^2*r - s^2 = 0,
Y = 4*eta*q - 3*s^2 = 0,
eta^2 | s^2+X, eta | 3s^2+Y.
```

This point is deliberately not in the live ideal: it has `kappa=0` and, for
`e=1`, `c=-2e`. It is a negative control for overbroad promotion and for the
Rabinowitsch guard. The unit ideals certify only that no point survives the
declared capped necessary subsystem after the live open equations are enforced.
They do not construct or exclude arbitrary chamber objects outside that scope.
Item 4 is CONFIRMED with this bounded scope.

## 5. T4 restoration on the corrected e=0 section

I checked the T4 proof in normalized constants `B=tau=1`; the omitted constants
are nonzero scalars, so zero/unit decisions are unchanged. With

```text
G=g, E1=1+g, E2=Z, D1=2/3+g, D2=(2/3)Z,
C1=s*(1+g/2), C2=Zs,
h=s^2/2, q=y+h, r=(x+h)/2, i=x'-2y', kappa=K,
```

direct source extraction gave the exact factorizations:

```text
EQ1_even - (F1 + 2Z*E0) = 0
EQ2_even - 2F2          = 0
EQ3_even - 2F3          = 0
s*O0 mod E0 - 2F4       = 0
```

For the last line I used `s*p' = q*r' - K/2`, which is just `E0=0`
multiplied form and does not divide by `s`. This is the hidden-division point
that needed checking.

The algebraic reductions in SOL (`SOL:606-647`) also exact-diffed:

```text
F1 - [g*x' + 2y*g' + 2(1+g)i + 2KZ] = 0,
F2 - Z*A - [Z(1-g)i + g*g' - 2KZ^2 - g*y] = 0,
F3 - [2Z^2*i - g*(g-2Zg')] = 0.
```

From `F3=0`, `i=g(g-2Zg')/(2Z^2)`, and the displayed `B` equation gives
`g | Z^2` once `K!=0`. The live `G!=0` section leaves two cases:

```text
g=gamma*Z^2:
  i = -3*gamma^2*Z^2/2,
  the Z^1 coefficient of A is -6K, contradiction.

g=gamma*Z:
  i = -gamma^2/2,
  y = gamma/2 + (gamma^2/2 - 2K/gamma)Z,
  x' = 2K/gamma,
  i=x'-2y' gives K=gamma^3/12.
```

Then `delta = gamma - 4K/gamma^2 = 2gamma/3`, and the last row reduces
exactly to SOL's equation

```text
-(gamma^2/2)*(h + Z*(1+delta*Z)*h') - K*delta*Z*(1+gamma*Z) = 0.
```

Writing `s=u0+u1Z+...`, so `h=(u0+u1Z+...)^2/2`, the constant coefficient is
`-gamma^2*u0^2/4`, hence `u0=0`; after that, the `Z^1` coefficient is
`-gamma^4/18`, contradiction.

The finite T4 ideals were unit in both engines:

```text
g=gamma*Z^2:  QQ[gamma,K,tt], <6K, gamma*K*tt-1> = (1)
g=gamma*Z:    QQ[gamma,K,x1,y0,y1,u0,u1,tt], SOL's seven generators = (1)
```

This proof uses the corrected e=0 source equations, not the old determinant
whose corrected top determinant vanished. Item 5 is CONFIRMED.

## 6. OPEN scope and retracted-item audit

SOL's branch ledger is scoped correctly (`SOL:519-553`):

```text
Chamber-II branch (A), c*kappa*(c+2e)!=0:
  EMPTY for e=1,2,3 in the declared capped necessary subsystem.

c=0 / Chamber III:
  EMPTY for e=1,2,3 by separate c-specialized unit ideals.

c=-(2e+1):
  EMPTY only because it is nonzero and not -2e, hence lies in the main
  Rabinowitsch stratum. This is not an old wall argument.

Wall A, 3c+6e+2=0:
  EMPTY only by membership in the main unit stratum for e>=1. The old Wall-A
  determinant is not consumed.

k=2e:
  closed only inside the preceding capped decided scopes; the ideal did not
  divide by k-2e.
```

No new OPEN is raised by this review. The surviving typed OPENs from SOL remain:

```text
OPEN[A2-CMINUS2E]:
  c=-2e. The 4e-1 cap is unlicensed here; there is no bounded quantity to
  promote until a replacement cap is proved. Any run before that is only a
  capped probe.

OPEN[A2-CHAMBER-I]:
  g>2e. Future jobs must be keyed by fixed (e,g) and use the stated cap
  deg X, deg Y <= 2g-1 with kappa*G_g*tt-1.

OPEN[A2-DEVBOX-EGE4]:
  e>=4. Future jobs are fixed-e coefficient ideals preserving the same
  exceptional c-strata and the licensed cap where it applies.

OPEN[A2-K2E]:
  narrowed, not erased. Closed for e<=3 only in the decided capped subsystems,
  still open on c=-2e, Chamber I, and e>=4.
```

The retracted old wall, RAY-2, and old cell certificates are not consumed.
Their only appearances in SOL are as stale-source canaries, rejected parser or
wall artifacts, explicit non-use statements, or handoff warnings
(`SOL:506-514`, `SOL:737-790`). I found no place where a conclusion is
transported from the retired derivative bracket, old Wall-A determinant, old
RAY-2 inequality, or old cell certificates into the corrected proof. Item 6 is
CONFIRMED.

## 7. FALLACY-v2 audit

* Flag/place/series: none identified. This report contains coefficient ideals,
  source-row identities, and synthetic controls only.
* Carrier/attainment and floor/attainment: no `FULL_ACTUAL_EXIT`,
  `ACTUAL_MAP`, cover, or exit-price assertion is made. The unit ideals are
  necessary subsystem emptiness certificates.
* `sat()` wrapping: no saturation wrapper was used. The ideals include explicit
  Rabinowitsch equations in the declared rings.
* Raw remainder degree: vanished leaders are separated by the declared c-strata;
  `c=0` is its own ring, and `c=-2e` is not promoted.
* Variable/ring map: the coefficient field, variables, order, cap, and
  Rabinowitsch rows are stated above. Matching names alone were not used as a
  coercion.
* Prime notation: every prime in the computations is `d/dZ`.
* Merge-free/M-descent and target/arrival index: not invoked.

## 8. Promotion recommendation

Promote the corrected canonical seven-row system, the T1/T2/O1s/DET-EO
derivations, the branch-(A) capped unit-ideal decisions for `e=1,2,3` in the
main and `c=0` strata, and the restored T4 theorem
`EMPTY[G!=0, deg eta=0]`.

Do not promote any whole-chamber emptiness statement. Preserve
`OPEN[A2-CMINUS2E]`, `OPEN[A2-CHAMBER-I]`, `OPEN[A2-DEVBOX-EGE4]`, and the
narrowed `OPEN[A2-K2E]` exactly as typed.

<!-- BODY-END -->
