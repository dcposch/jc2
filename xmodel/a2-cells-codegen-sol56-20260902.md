# A2-CELLS-CODEGEN: executable `A2-E1WALL-CELLS` transcription

Lane: `A2-CELLS-CODEGEN`. Date: 2026-09-02. Generator target:
`qqideal==0.1.0`, `msolveio==0.1.0`, and msolve 0.10.1 selected by the
`binary=` argument of `msolveio.run_groebner`.

## 0. Custody, scope, and typed status

Before reading the mathematical content I hashed the three frozen input copies.
The observed SHA-256 values were

```text
3d08b8996227e292d76e0ba3901cfad16099f347f97129d27b6bf5b3bc253f0a  ray-kill-opus5-20260902.md
d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b  cell-32-termination-opus5-20260901.md
df5612152d60496bb81311ee9183d3c580759a2549d6ea8945a487d284976fcf  ray-kill-review-gpt55-20260902.md
```

All three match the charge exactly. I abbreviate the frozen copies as `RAY`,
`C32`, and `REVIEW`. The repository copies are not substituted for these
inputs. The implementation files are `box/a2_cells_jobs.py` and
`box/a2_cells_run.py`.

This is a code-generation and decision-job lane. It does not assert an exit
price, attainment, a flag count, or closure of the unbounded ray. Accordingly
there is no `charge_basis` declaration. Even an EMPTY verdict at every listed
cell leaves `OPEN[A2-U-BOUND]`, because the cells for fixed `e` continue with
unbounded `U` (RAY:427-433), and RAY itself limits the correct reading to
“empty on the computed window” (RAY:480-482).

The code-generation status at completion is intended to be

```text
A2-E1WALL-CELLS-CODEGEN: SEALED.
Mathematical residual: OPEN[A2-E1WALL-RESIDUAL].
Item 0 is a mandatory second-engine gate; a NONEMPTY or non-answer over the
characteristic-zero input is ORACLE-P0 and terminates the runner with exit 2.
```

## 1. Transcription choices and the two source errata

### 1.1 The `(2.2)` label collision is resolved by the charged review

There are two nearby uses of “(2.2)” in the source chain. C32:198-203 labels

```text
C1 = d*psi*s + (d/(2b))*Phi,       Phi = sG/eta
```

as its displayed `(2.2)`. This is the substitution used in all four residual
equations; it is not a fifth residual equation. Later C32 says that the
charged spec's `(2.2)`, re-derived from `O0+E0`, is

```text
2(s*C1-q*E1)r' + kappa*E1 + q*s*s' - q'*s^2 = 0
```

(C32:583-590). That latter polynomial is `EQ4`. REVIEW explicitly resolves
the job transcription the same way: `EQ4` is the `O0+E0` identity at
C32:586-590, while T1 is separately encoded without division as
`eta*Phi-s*G` (REVIEW:243-251). The decisive builder therefore constructs
`C1` with the first display and takes coefficients of the second display as
`EQ4`. No unresolved formula variant remains.

A literal alternative in which the C32:202 assignment itself were treated as
`EQ4` would be identically zero after the mandated `C1` substitution, would
lose the quadratic `EQ4` family described by RAY:108 and RAY:167-169, and
would not reproduce the charged 37-generator gate. It is recorded as a
rejected label-reading, not silently encoded as an extra decisive system.

### 1.2 The symbolic count line drops T1 slots and the saturation row

RAY:405-410 prints a symbolic equation-count sum and then gives the measured
table at RAY:412-420. The literal T1 display is `eta*Phi-s*G` (RAY:448-455),
with `deg eta=e`, `deg Phi=sigma+e`, `deg s=sigma`, and `deg G=2e`.
Consequently T1 has degree `sigma+2e` and contributes
`sigma+2e+1` coefficient generators, not `sigma+e+1`. The explicit
Rabinowitsch generator contributes one further equation. Thus the actual block
counts are

```text
EQ1  U+2e             EQ2  U+2e+1
EQ3  3e+U+2           EQ4  2U+e
T1   sigma+2e+1       E0   2U-e
SAT  1
```

These sum to `(15U+19e)/2+5`, reproduce `(1,3): 37`, `(1,5): 52`,
`(1,9): 82`, `(2,8): 84`, `(3,11): 116`, `(4,12): 133`, and
`(5,15): 165`, and agree with the direct nonzero coefficient expansion. The
unknown count is `(9U+5e)/2+6`, matching the same table. The resulting excess
is `3U+7e-1`; therefore RAY:423's informal asymptotic phrase is also not the
arithmetic of its own table. These are count-prose errata only. No displayed
mathematical generator is altered or truncated.

## 2. Ring, variables, normalizations, and wall

For every accepted `(e,U)`, the builder checks `e>=1`, `U>=3e`, and
`U congruent to e (mod 2)`, then sets exactly as in RAY:443-447

```text
g=2e,        m=U,        n=U-e,        sigma=(U+e)/2,
a=b=1,       d=3/2,      A_e=1,        G_g=-(1+2e).
```

It declares the grevlex coefficient ring over `Q` in this fixed order:

```text
A0,...,A(e-1),
S0,...,S(sigma), Q0,...,Q(m), R0,...,R(n),
G0,...,G(g-1), F0,...,F(sigma+e),
P0,...,P(3n/2-1), kappa, tt.
```

Here `F_i` are coefficients of `Phi`, not coefficients of the live deviation
`F=D1-D2'`; the latter has already been eliminated as `d*eta*G` by C32:64-68.
`P_i` are coefficients of the polynomial denoted `p'`; the prime is genuine
`d/dZ`, as C32 fixes at lines 58-60. Names are mapped to polynomials explicitly:

```text
eta = Z^e + sum_(i<e) A_i Z^i
s   = sum_(i=0)^sigma S_i Z^i
q   = sum_(i=0)^m Q_i Z^i
r   = sum_(i=0)^n R_i Z^i
G   = -(1+2e)Z^(2e) + sum_(i<2e) G_i Z^i
Phi = sum_(i=0)^(sigma+e) F_i Z^i
p'  = sum_(i=0)^(3n/2-1) P_i Z^i.
```

The two legal normalizations are supported by the two coefficient scalings in
RAY:126-133. In contrast, RAY:133-140 proves there is no `Z`-scaling symmetry,
and RAY:471 repeats the resulting DO-NOT. `S_sigma` therefore remains a ring
variable and appears in the explicit open generator. The implementation has no
option to normalize it.

The wall sign is negative in every decisive build. A non-decisive
`wall_sign=+1` construction exists solely for required self-check (ii); it
changes `G_g` to `+(1+2e)` and is never reachable through the runner's solve
path. This separates a negative control from the charged ideal.

## 3. Coefficient-level derivation correspondence

All primes in the following table mean `d/dZ`. Every row is expanded in the
univariate variable `Z`; each nonzero coefficient becomes one generator of the
coefficient ring. No raw functional equation is handed to msolve.

| Block | Polynomial expanded coefficientwise | Charged source |
|---|---|---|
| definitions | `psi=eta+Z eta'`, `chi=eta+2Z eta'`, `phi=eta+3Z eta'`; `E1=eta*chi+G`, `D1=eta^2*phi+(3/2)eta*G`; `C1=(3/2)(psi*s+Phi/2)` | C32:64-74 gives `d=3a/(2b)` and the definitions; C32:198-203 gives the `Phi` form of `C1`; `a=b=1` is RAY:443-447. |
| `EQ1` | `6D1*r' - 4q'*E1 + 2q*E1' + 4C1*s' - 2C1'*s + 2*kappa*Z` | C32 equation (1.1), lines 99-105. The `2*kappa*Z` replacement uses E0 exactly, not a new normalization. |
| `EQ2` | `E2eq|_(G=0)+Delta_2`, transcribed term-for-term in §3.1 below | C32:631-643. |
| `EQ3` | `eta*Z^2*Xi - 3*(Z*eta^2*G^2)'` | C32 T2 at lines 241-255, after `a=b=1`. |
| `EQ4` | `2(s*C1-q*E1)r' + kappa*E1 + q*s*s' - q'*s^2` | C32:583-590 and the explicit resolution REVIEW:243-251. |
| `T1` | `eta*Phi-s*G` | C32:177-203 proves `eta | sG`; RAY:448-455 mandates the division-free coefficient encoding. |
| `E0` | `2(q*r'-p'*s)-kappa` | C32:99-104 and RAY:453-455. |
| saturation | `S_sigma*Q_m*R_n*kappa*tt-1` | RAY:455 and the DO-NOT at RAY:471-473. This is already an explicit Rabinowitsch equation; no `sat()` wrapper is applied. |

### 3.1 Exact `EQ2` transcript

With `d=3/2`, the implementation uses

```text
E2G0 = 6Z eta^2(3eta+4Zeta')r'
      +2[eta^2 q+10Z eta eta' q+4Z^2(eta'^2+eta eta'')q
          -6Z eta^2 q'-4Z^2 eta eta' q']
      +12Z eta^2 eta'[eta eta'-Z eta'^2+Z eta eta'']
      +2dZ[3eta s s'-2(2eta'+Zeta'')s^2],

Delta2 = 6Z eta^2 eta' G'
        +6eta[eta eta'-3Z eta'^2+Z eta eta'']G
        +d[eta(G^2)'-4eta'G^2]
        +8dZ eta G r' +4Z(qG'-q'G)
        +d[Phi*s+2Z(Phi*s'-Phi'*s)],

EQ2 = E2G0+Delta2.
```

This is C32:631-643 with only the licensed `a=b=1` substitution. In
particular, the final `Phi` group is retained, `Delta2` is not replaced by a
degree leader, and no term is divided by `eta`.

### 3.2 Exact `Xi` transcript

The five T2 families are encoded as

```text
Xi = 12 eta^3 eta'(eta'+2Zeta'')
   +  4d s(eta s'-eta' s)
   +  8 eta(q eta'-q' eta)
   + 12 eta^3 r'
   + 12 eta[(eta eta''-eta'^2)G+eta eta'G'].
```

These are C32:249-255, in the displayed order. The builder then forms the
polynomial identity version `eta*Z^2*Xi-3*(Z*eta^2*G^2)'`; it never encodes
the divided form `Z^2 Xi=3(... )'/eta`. This is the safe ring map required by
T2 at C32:241-247.

