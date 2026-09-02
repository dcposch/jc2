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

The final code-generation status is

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

## 4. Implementation and solver contract

### 4.1 Fraction builder and fail-closed coefficient extraction

`box/a2_cells_jobs.py` contains a small sparse polynomial layer with two
levels: `MPoly` is a multivariate polynomial over `Fraction` in the declared
coefficient variables, and `ZPoly` is a polynomial in `Z` with `MPoly`
coefficients. Addition, multiplication, nonnegative powers, and `d/dZ` are
implemented directly. Thus `build_cell(e,U)` neither imports nor shells out to
sympy, qqideal, msolveio, or msolve.

Each of `EQ1` through `E0` is first built as one `ZPoly`. The extractor is
given the source-derived top degree, requires the actual top degree to match,
and requires every slot down to degree zero to be a nonzero coefficient
polynomial. It then records those coefficients in descending `Z` degree. This
matters for the count check: a missing term cannot be hidden by a CAS silently
dropping an identically zero generator. `CellSystem.block_counts` retains the
six family counts plus `SAT`; optional pins are a separate `ACCEL` block.

The public cell object carries

```text
(e,U,g,m,n,sigma), phi_degree, pprime_degree,
wall_value, wall_sign, accelerators,
variables, blocks, generators, unknown_count, generator_count.
```

Generator strings are expanded unique-monomial sums with rational
coefficients, no parentheses, and variables only from the fixed declared
tuple. This is the input language accepted by both v0.1.0 packages. The
qqideal map is deferred to `build_qqideal`: it constructs
`Ring(*variables, characteristic=...)`, constructs `Ideal(generators,ring=R)`,
then asserts the exact ring-name order, generator count, and the ring of every
image. Because the Rabinowitsch row is already present, this function offers no
`opens=` parameter and never calls `Ideal.saturate`.

### 4.2 Why the runner calls msolveio directly

In qqideal 0.1.0, `Ideal.verdict(timeout=...)` and
`ideal_verdict(...,timeout=...)` do not accept an msolve executable. The charge
requires msolve 0.10.1 to be pinned by the `binary=` parameter. The runner
therefore uses qqideal for the canonical ring/ideal construction and
`Ideal.to_msolve()`, then calls the published msolveio 0.1.0 primitive directly:

```text
run_groebner(source,
  gb=1 for F_p, gb=2 for Q,
  timeout=..., threads=...,
  binary=resolved_absolute_path,
  allow_unknown_version=False)
```

Before any job, it requires package versions exactly `0.1.0`, resolves an
executable file, runs `msolve --version`, requires the exact string `0.10.1`,
and passes that absolute path to every call. msolveio itself accepts the wider
0.10.x parser family, so the additional exact comparison is necessary to
satisfy the charge.

For every successful call the runner checks all of the following before typing
a verdict:

```text
RunResult.input_sha256 == sha256(the exact emitted UTF-8 input),
RunResult.msolve_version == 0.10.1,
echoed characteristic == requested characteristic,
echoed variable tuple == declared tuple, including order,
leading_only == True exactly on the mod-p gb=1 screen,
monomial order == graded reverse lexicographical,
every returned basis entry re-coerces into the declared qqideal ring.
```

The parser's `unit_ideal` field, not an output substring, supplies EMPTY versus
NONEMPTY. `MsolveTimeout` becomes `Kind.TIMEOUT`; a solver, parser, version, or
map failure becomes `Kind.ERROR`. These are typed non-answers and are never
collapsed into EMPTY. Generator-construction and preflight failures are also
fail-closed: when a gate was requested they print `ORACLE-P0` and return 2
rather than escaping the promotion protocol as an untyped exception.

### 4.3 Field and certainty typing

The default screen field is `F_65521`; 65521 is prime and does not divide the
displayed power-of-two denominators. The CLI validates any replacement `--prime`.
An Fp result is `Certainty.PROVEN` only for that finite field and every such row
is labeled `EVIDENCE-only`. It never short-circuits the following Q-form call,
including when it is EMPTY, NONEMPTY, TIMEOUT, or ERROR. This implements the
warning that a unit ideal at one prime does not imply a unit ideal over Q
(RAY:466-470).

For characteristic zero, msolve 0.10.1's `-g 2` returns a lifted proper basis,
so Q-form NONEMPTY is `Certainty.PROVEN`. On a unit ideal, however, msolve
returns after its internal modular computation even though the emitted input
and output header have characteristic zero. qqideal 0.1.0 therefore types that
answer `EMPTY/MODULAR`. The runner preserves this label. For item 0 it follows
the charged gate's stated comparison: Q-form `Kind.EMPTY` is independent
second-engine agreement with the existing sympy/QQ `[1]`; Q-form NONEMPTY,
TIMEOUT, or ERROR prints an `ORACLE-P0` banner and exits 2. It does not call the
MODULAR label PROVEN.

Items 1--4 run only after that gate. Their Q-form TIMEOUT/ERROR rows remain
OPEN non-answers, the campaign continues to later cells, and the final process
status is 1. Answered EMPTY/NONEMPTY rows remain in the table. Every row prints
the full input and, when available, output SHA-256, field role, Kind,
Certainty, version, wall time, variable/generator counts, and accelerator
state.

### 4.4 Optional accelerators are quarantined

With `accelerators=True`, the builder appends exactly the five polynomials at
RAY:456-461 and adds no variables. The default is false, so no decisive hash or
as-run result below consumes them. They are also rejected at `U=3e`: the
item-0 boundary has the nonzero inhomogeneity `rho` (RAY:214-228), whereas the
displayed residual pins are for `U>=3e+2`. The runner consequently leaves item
0 unaccelerated even when its CLI flag is present.

There is a provenance reason for keeping this quarantine visible. RAY calls
the optional rows proved, but it also types the N2 row as measured
(RAY:233-241). REVIEW confirms the pins only conditional on N2 and explicitly
declines to promote RAY-2 unconditionally (REVIEW:340-342, 528-530). The charge
still asks that the rows be encoded, so they are available as the named
experimental variant; this codegen report does not upgrade their theorem
status.

## 5. Required self-checks

The following is the verbatim output of
`python3 box/a2_cells_run.py --self-check`. That code path returns before
importing qqideal/msolveio or probing for an msolve binary.

```text
A2-E1WALL-CELLS preflight: Fraction-only self-checks
=== A2-E1WALL-CELLS self-checks (Fraction only; no msolve) ===
[i] charged unknown/generator counts
  (1,3) vars/gens=22/37 expected=22/37: PASS
  (1,5) vars/gens=31/52 expected=31/52: PASS
  (1,9) vars/gens=49/82 expected=49/82: PASS
  (2,8) vars/gens=47/84 expected=47/84: PASS
  (3,11) vars/gens=63/116 expected=63/116: PASS
  (4,12) vars/gens=70/133 expected=70/133: PASS
  (5,15) vars/gens=86/165 expected=86/165: PASS
CHECK(i) COUNTS: PASS
[ii] deliberately broken wall G_g=+(1+2e)
  nonzero generator-slot differences: 22
  top T1 good-broken: 6*S2
  expected witness:   6*S2
CHECK(ii) BROKEN-WALL-DIFF: PASS
[iii] saturation variable occurrence and exact row
  tt-bearing rows: [('SAT', 0)]
  SAT: S2*Q3*R2*kappa*tt-1
CHECK(iii) SATURATION-EXACTLY-ONCE: PASS
[policy] accelerators default off; S_sigma remains a variable
  base/accelerated generators=52/57; variables=31
  S_sigma name retained: S3
CHECK(policy): PASS
SELF-CHECKS OVERALL: PASS
```

Check (ii) is coefficient-level, not merely a different serialized hash. For
general `e`, the top T1 coefficient is
`F_(sigma+e)+(1+2e)S_sigma` on the charged wall and
`F_(sigma+e)-(1+2e)S_sigma` on the broken wall. Their exact difference is
`2(1+2e)S_sigma`, specializing to the printed `6*S2` at `(1,3)`.

As an additional transcription audit, every variable position and every
generator slot was compared as a sympy polynomial against the surviving
charged driver at `(1,3)`, `(1,5)`, and `(2,8)`. There were zero differences
across respectively 37, 52, and 84 generators. This corroboration is not used
as a mathematical source; the frozen displays and charged review remain the
source cited in Section 3.

## 6. Complete generated window and canonical input hashes

All twelve base cells were constructed and mapped through actual qqideal
0.1.0 over both `F_65521` and Q. `Ideal.to_msolve()` accepted every generator,
and the ring/order/count assertions passed. The following full hashes are of
those canonical emitted inputs; accelerators are off.

| item `(e,U)` | variables/equations | `F_65521` input SHA-256 | Q input SHA-256 |
|---|---:|---|---|
| item 0 `(1,3)` | 22/37 | `a2add80d4eee13db1733254f3b1d44b70866211bc2317a2834d9bdb9a5b01297` | `35f9f437d889b30617f38dc93fdd6c2ca41db4576406d519877e175627a3e1e4` |
| item 1 `(1,5)` | 31/52 | `6208336023d6519ece4593ddd14b7feacf887fe4b715ee38a14ef41f6e338284` | `6424ebcb8c40b91cd75f08c661b85bedc36b07b3b7a839a4f5b5dcb38e7ee855` |
| item 1 `(1,7)` | 40/67 | `42d8a984a5f5f2c55fcafd4dce0a74166aed715c59a2516f0453316bea1e2ccc` | `d77c3286ff6c7b497608fdbf55619d5cce200d15d6413e0ef58b8a077d3e00f1` |
| item 1 `(1,9)` | 49/82 | `b95ea016ee9ad2d6554cf82d7a8132f6e17e43183ccd3ff4bfa99b89e5c98112` | `31c07958a32e844263928146eaa1b24c9be03dcbd5f8da0b15198b56a2e50d43` |
| item 1 `(1,11)` | 58/97 | `1fef2e162b4c3316adc7371957f021a670844125e07c18f01082ed5e3bf5a945` | `4d7653f4c03a52b9edf3045bce195851287216bf126b4bc7f5259d9316731ced` |
| item 1 `(1,13)` | 67/112 | `9747583a94c082ccf62c83fa3d3e4dbd824d7434b489b47bb92389a545f11984` | `353b3734ba26d81975ab956317e46c1b934a0913958737ad8b20c627895ad3ca` |
| item 2 `(2,8)` | 47/84 | `c4ac45aff4698ce428332fd285e7765c6dbf7c76f06da28e37e8b76d358f5969` | `73d7b12ade5883bc775682f1d48a5638f2a02a01e6fa337fe6f8fa7d7b774c85` |
| item 2 `(2,12)` | 65/114 | `441e818b224f3d6d994e4ed126f513b8fb77d26d0591ac0b043863b2f3888574` | `809f1e3e7f4e6b5628c7a97123060390ca216c748444b14417ea0f5e2b0333bf` |
| item 3 `(3,11)` | 63/116 | `d085881a19adf5a26cd8a02f7e2cee57b4eebc7311e41d45422d137c81489869` | `75b290b5b127bbccca8c8c33d03010c78dce5802407dc8a83c974b890d503f18` |
| item 3 `(3,13)` | 72/131 | `0ab6cb2b0e155308c7a462fc0d2f0c60c11c1a35e87557ff5951db1fc5a79804` | `77e21cd0577a9236e35c7fbcd8f042faab2801ff9c34e08a6a6b472710c46e09` |
| item 4 `(4,14)` | 79/148 | `97f9b131d95abc4cff4d97954da22ba99e751ae83cb812643979798f07cb171b` | `04def30878b159b6864d7a5f4704a432f515211bef679a8037818af05ea81f6d` |

The table also verifies the runner list against RAY:463-465: parity skips the
intermediate integers in the two displayed ranges. The largest Q input is
204,566 bytes; code generation and canonical mapping of all 24 field/cell
inputs took about four seconds on the local test host, without invoking
msolve.

## 7. End-to-end runs performed in this lane

The runtime integration used qqideal 0.1.0, msolveio 0.1.0, and the explicit
binary `/opt/homebrew/Cellar/msolve/0.10.1/bin/msolve`. Times below are solver
wall times and can vary; hashes and typed outcomes are the custody data.

The mandatory item-0 gate returned:

| phase | typed result | input SHA-256 | output SHA-256 | wall |
|---|---|---|---|---:|
| `F_65521`, `gb=1` | `EMPTY/PROVEN`, EVIDENCE only | `a2add80d4eee13db1733254f3b1d44b70866211bc2317a2834d9bdb9a5b01297` | `491175047890e0216694bfc10599679ce144a830f574646f0bf99ec0e2ae5b15` | 0.006 s |
| Q-form, `gb=2` | `EMPTY/MODULAR`, decisive gate Kind | `35f9f437d889b30617f38dc93fdd6c2ca41db4576406d519877e175627a3e1e4` | `9eeac1f2da70f18e692e8545d0be6dd025fa2aa8e40c48c09c3cc38bef09e8eb` | 0.005 s |

Thus the requested second engine agrees with the charged sympy decision at
RAY:352-393 and REVIEW:184-273. The operational gate is passed. The certainty
qualification above remains binding.

The next cell `(1,5)` also completed in both phases during integration:

| phase | typed result | input SHA-256 | output SHA-256 | wall |
|---|---|---|---|---:|
| `F_65521`, `gb=1` | `EMPTY/PROVEN`, EVIDENCE only | `6208336023d6519ece4593ddd14b7feacf887fe4b715ee38a14ef41f6e338284` | `aad2a147942167d66ab6cdeef752e5d009398d5bc8dfb31fca996221fbf8222a` | 0.081 s |
| Q-form, `gb=2` | `EMPTY/MODULAR` | `6424ebcb8c40b91cd75f08c661b85bedc36b07b3b7a839a4f5b5dcb38e7ee855` | `41887e0f6c88e13dc28b28e66627c1e348c8439a137abf88333ad1eb554c1b64` | 0.080 s |

In a bounded exploratory continuation, both phases of `(1,7)` reached their
120-second limits and were typed TIMEOUT with the input hashes in Section 6;
the later exploratory cells were not run in this report. This is not a verdict
on `(1,7)`. The delivered campaign runner continues after such later-cell
non-answers, includes them in its final table, and returns status 1.

The P0 branch was also exercised with an intentionally microscopic item-0
timeout. Both calls were typed TIMEOUT, the runner printed the loud
`ORACLE-P0` block, refused items 1--4, and exited exactly 2. This is a control
of failure typing, not mathematical evidence.

## 8. Scope guardrails and final mathematical reading

No cv flag, physical place, or cover series is introduced here. No per-ray
exit price is charged. No carrier statement or attainment statement is made.
No pole identity, raw-remainder claim, or prime-label reinterpretation is
used. The derivative map, coefficient-ring map, field, generator order, and
image checks are explicit above.

The saturation is a single displayed polynomial in the declared ring. There
is no `sat()` return object to confuse with an ideal, and the `tt` occurrence
check proves that no second Rabinowitsch variable is hidden in the input.
`S_sigma`, `Q_m`, `R_n`, and `kappa` remain variables and are forced nonzero on
the encoded graph; none is replaced by 1.

The subsystem has an asymmetric interpretation. RAY:493-506 explains that O1
and the full O0 are unavailable in the charged record: this job has four of six
residual equations, plus E0 and T1. EMPTY for this displayed subsystem is a
conclusive kill of that cell. NONEMPTY would only show that the displayed
subsystem has a point; it would not be a witness to the omitted equations or a
full live pair. The runner reports `NONEMPTY` without upgrading it.

Finally, even a completed all-EMPTY table is only a finite window. It neither
bounds U nor closes `OPEN[A2-E1WALL-RESIDUAL]`; RAY:427-433 and 480-482 are
preserved literally. The executed results here establish the item-0 engine
agreement and an EMPTY answer at `(1,5)` under the stated certainty labels.
They do not establish a uniform kill.

## 9. Reproducibility seal

Final validation was performed after the fail-closed and output-ring-map
hardening. `py_compile` passed for both deliverables; the Fraction-only suite
passed; all twelve cells mapped through qqideal 0.1.0 over both `F_65521` and
Q with the 24 hashes in Section 6; and `git diff --check` reported no errors.
The pinned end-to-end item-0 rerun again returned `EMPTY/PROVEN` for the
finite-field evidence screen and `EMPTY/MODULAR` for the decisive Q-form gate,
with exactly the hashes in Section 7. Planted construction and preflight
failures each produced `ORACLE-P0`, refused downstream cells, and returned 2.

The final executable artifact hashes are

```text
99f4afb6a4cbd596bf3e4c925a69cbc6ffa6a046d61214e41248bd1866ad2895  box/a2_cells_jobs.py
c0133c34715160835e8a4b42042556a3f8fd011928714349db3f75689cf3ba44  box/a2_cells_run.py
```

The report does not embed its own SHA-256 because that would be
self-referential; its completed external hash belongs in the lane handoff.
The optional accelerator variant remains available but was off for every
decisive result and every canonical hash recorded here.

```text
A2-E1WALL-CELLS-CODEGEN: SEALED.
Promotion gate (1,3): EMPTY/MODULAR, PASSED.
Mathematical residual: OPEN[A2-E1WALL-RESIDUAL].
Finite-window limitation: OPEN[A2-U-BOUND].
```
