# Closed high-`E_t` pivot forms (5.9)–(5.15), derived in `(t, j)`

Date: 2026-09-03.  Lane: `k16-pivot-forms-grok46-20260903`.
Charged spine: `xmodel/k16-middle-spine-sol56-20260903.md`.
Charged gate: `xmodel/k16-spine-gate-opus5-20260903.md`.

## Verdict

**(5.9)–(5.15) DERIVED.**  The identities

```text
b_j  = g_3 (3t+2-3j) / (2 y (t-j)),
d_j  = (g_2 (t+1-2j) + b_j (t+1+j)) / (y (4t-2j+1)),
n_j  = -g_1 (t+j) + (j-t) d_j + 2 q b_j,
dq_j = 3 g_3 (q-j) / (y (4t-2j+1)),
nq_j = (j-t) dq_j + 2 (q-j) g_2,
p_b2 = g_3 d / (2 y),
```

are the first-order responses, in the function field `Q(t,j,y,g_1,g_2,g_3,q)`,
of the homogeneous-origin jet of `-E_t` to a weight-`j` perturbation.  Their
differences with the forms asserted in charged `laurent_pivot_formulas.py` are
identically zero.  Reducing in `A_t = Q(t,j)[d]/(3d^2-(t+1))` recovers the
closed linear classes `(5.9)–(5.15)` identically.  Combined with the Opus
gate's confirmation of the reconstruction block, the weight argument, and the
norm certificates, the **second affine spine is a theorem for every integer
`t>=2`**, and the reduction **`(T) <=> (8.1)` is PROMOTED**.  Statement
`(8.1)` itself — that the terminal ideal is `[1]` for every such `t` — remains
`OPEN` as a uniform claim.

No new exit-price is asserted, so no `charge_basis` line is due.

## 0. Frozen inputs

The receipt's `charged_input_i_sha256` / `_basename` fields generated
`box/k16pivot-20260903/inputs.sha256` by `awk`; `sha256sum -c` returned `OK`
for all 13 charged files.  No hash was retyped into the check command.  All
new drivers live in `box/k16pivot-20260903/`.  No ledger was edited.

Throughout, a prime is `d/ds` (equivalently `d/dX` at the origin `b4=0`).
The algebra generator is `d = 2 q y - (t+1)`, never inverted unless its
resultant against `H_t` is a nonzero polynomial with no positive-integer root
on the declared range.  Records store `-E_t`; the displayed `(5.10)`, `(5.13)`,
`(5.15)` are coefficients of `R_s := -E_t`.

## 1. Fixed-`t` rebuild (`t=2,3`)

`terminal_laurent_model.build` was re-run with output redirected into this
lane's box.  Against the charged JSON, `H_t`, `d`, the normalizer
`(g_1,g_2,g_3,c)`, every high-pivot coefficient and resultant, both unit
pivots `b1` and `B0`, every terminal band, and the residual variable lists
`[b3,b4]` / `[b3,b4,q2_0]` agree exactly in `A_t` (`compare_rebuild.py`:
`REBUILD_COMPARE_PASS`).  This is the recurrence the symbolic jet linearizes.

Spine order, as recorded: bands `4t,...,2t` of `R_s` eliminate
`C_1,...,C_(t-1)`, `q_t,...,q_(2t)`, `b2` in increasing weight `j=1,...,2t+1`.

## 2. Symbolic perturbation

Driver: `box/k16pivot-20260903/derive_pivot_forms.py`.  Two-jet series
`c_0 s^m + eps c_1 s^{m'}` with exponents in `Z[t,j]`.  Background at the
homogeneous origin is the charged `(6.5)`, with named normalizers `g_2,g_1,e`
as leading coefficients of `T,S,X'`.  The gate confirmed that each new
elimination variable occupies its own weight, so the affine pivot coefficient
has weight zero, lies in `A_t`, and equals this linearization — the
calculation below is therefore the exact nonlinear diagonal, not a tangent
heuristic.

**C-family, `1<=j<=t-1`.**  Perturb `C` by `eps s^{t-1-j}`.  Identity
`(5.6)` / `(5.7b)` gives `T' = (g_3/(2y))(5C+3s C')`; bandwise integration
produces `b_j = [s^{t-j}]_eps T`.  The Euler right-hand side
`3 g_3 U' + A B - s A B' + 2 s A' B` (at `b3=0`) and
`[s^m] S = [s^m] rhs / (y(2m+1))` produce `d_j = [s^{2t-j}]_eps S`.  The `D1`
numerator `-V Y' + V' Y + 2 U' Z`, divided by `s` and by `2y`, produces
`n_j = [s^{3t+1-j}]_eps numer`.  Then

```text
[s^{4t+1-j}] R_s = e + n_j/(2y) - q d_j.
```

All three of `b_j,d_j,n_j` match the asserted rational functions identically
(the `n_j` identity holds with `q` a free name, and also after `q=2t+1`).
The unperturbed band `[s^{4t+1}] R_s = e - q g_1` vanishes on `g_1=e/q`.

**Q-family, `t<=j<=2t`.**  Perturb `U` by `eps s^{q-j}`.  `C` and `T` are
unperturbed, so the only first-order Euler source is `3 g_3 U'`, giving
`dq_j`.  The same numerator and `R_s` reading give `nq_j` and

```text
[s^{4t+1-j}] R_s = nq_j/(2y) - (q-j) g_1 - q dq_j.
```

Both `dq_j` and `nq_j` match the asserted forms identically.

**`b2`, weight `j=2t+1`.**  Perturb `Y` by `-g_3 eps`.  The `s^{2t}` band of
`R_s` is `g_3 (2 q y - (t+1))/(2y) = g_3 d/(2y)`.

**Boundaries.**  `j=0` is not an unknown (the leading coefficient of `C` is
the monic `1`).  At `j=t` the C-family denominator `t-j` vanishes and
`s^{t-1-t}=s^{-1}` is not a polynomial term of `C`; this index is the first
Q-variable `q_t`.  At `j=2t`, `q-j=1` and `4t-2j+1=1`.  At `j=2t+1` the
unknown is `b2`, not a coefficient of `C` or `U`.

## 3. Reduction to `(5.9)–(5.15)`

Substitute `q=2t+1`, `e=3t+1`, `y=(d+t+1)/(2q)` and the charged expressions
for `g_1,g_2,g_3` in `d`.  Remainders modulo `3d^2-(t+1)` invert a denominator
only after the remainder, and only if `Res_d(denom, 3d^2-(t+1))` is not the
zero polynomial.  The three `(5.7a)` identities hold in `A_t`, and the
`(5.7b)` leading term of `T` equals `g_2`.  Then

```text
p_C(t,j) = 3t(3t+1) L_C / ((t+1)(3t+2)^3 (4t-2j+1)),
p_Q(t,j) = -3t(3t+1)(q-j) L_Q / ((t+1) q (3t+2)^2 (4t-2j+1)),
p_b2     = g_3 d/(2y)  ~  L_2 = 3q d+(t+1),
```

with `L_C, L_Q` exactly `(5.9)` and `(5.12)`.  The positivity certificates
`(5.11)` and `(5.14)` reproduce.  The factor `t-j` cancels in `p_C`, so the
C-pivot closed form does not inherit that intermediate pole.

## 4. Specialisation

Charged nonlinear records exist for `t=2,3,4,5` (32 high-pivot coefficients).
Every specialised derived coefficient equals the recorded element of `A_t`
exactly (leading-coefficient ratio `1`, not a proper associate):

```text
t=2: 5/5   t=3: 7/7   t=4: 9/9   t=5: 11/11.
```

There is **no** charged `terminal_laurent_t6.json`.  The `t=6` specialisation
of the closed forms is well-defined in `A_6` and every one of the 13
resultants is a nonzero rational (a corollary of the positivity certificates,
not an independent nonlinear record).

## 5. Denominators (FALLACY-v2)

Every division in the jet is by an element of the coefficient field, or by a
linear form in `d` whose resultant against `H_t` is recorded below.  No
nonzero zero-divisor of `A_t` is inverted, including on the split ray
`t=3s^2-1` (the section-5.1 order never schedules `d+s`).

| denominator | integer roots in `t` | integer roots in `j` | status on the spine range |
|---|---|---|---|
| `2` | none | none | unit |
| `y` | `H_t(0)=(t+1)(3t+2)`: `t=-1` | — | unit for `t>=1` |
| `t` | `{0}` | — | `t>=2` |
| `t-j` | `t=j` (parametric) | `j=t` | excluded: C-range is `1<=j<=t-1` |
| `q=2t+1` | `t=-1/2` (not integer) | — | unit |
| `3t+1` | `t=-1/3` (not integer) | — | unit |
| `t+1` | `{-1}` | — | unit for `t>=1` |
| `3t+2` | `t=-2/3` (not integer) | — | unit |
| `4t-2j+1` | `t=(2j-1)/4` never integer (`2j-1` odd) | `j=2t+1/2` never integer | unit on all integer `(t,j)` |
| `q-j` | — | `j=2t+1` | excluded: Q-range is `t<=j<=2t` |
| `2m+1` at `m=2t` | `t=-1/4` | — | unit |
| `m+1` at `m=t-1` | `{0}` | — | `t>=2` |
| `(5.10)` | `t=-1` from `t+1`; others not integer | `j=2t+1/2` never | positive on `1<=j<=t-1`, `t>=2` |
| `(5.13)` | `t=-1`; `t=-1/2` from `q` | `j=2t+1/2` never | positive on `t<=j<=2t`, `t>=2` |
| `(5.15)` reduced | none integer (`6 q^2 (3t+2)`) | — | unit for `t>=1` |

Norms, consumed from the gate and re-checked: `Res_y(H_t,L_C)=-4q^2(3t+2)^3 F_C`
with `F_C(t,t-n)` the all-nonnegative quartic of constant term `32`;
`Res_y(H_t,L_Q)=-4q^2(t+1)(3t+2)^2 F_Q` with `F_Q(t,q-n)>=12` on
`1<=n<=t+1`; `Res_y(H_t,L_2)=-12 q^2 (t+1)(3t+2)(4t+1)`, integer `t`-root
`{-1}`.  Exhaustive scan `t<=40` finds no zero of either indexed family in
range.  Reconstruction diagonals `2 m y` and `(2m+1)y` are units by the `y`
row.

`sat()` wrapping, raw-remainder degree, variable/ring map, and prime-versus-
derivative are not re-opened: this lane inverts only after a remainder in the
declared quotient, and a prime is `d/ds`.  Finite `t<=5` records are tests of
the specialised identities, not a substitute for the `(t,j)` derivation.

## 6. Scope of the promotion

**THEOREM, `t>=2`:** the Laurent/Euler proof order of charged §5.1 consists of
`5t+2` unit affine substitutions (reconstruction `(5.6)–(5.7b)`, the two
divisibility/gauge pivots, and the `2t+1` high-`E_t` eliminations whose
diagonals are now derived).  Each is an isomorphism of the quotient ring.

**PROMOTED:** the gate's logical chain that `(T)` on the ray is equivalent to
`(8.1)` in `A_t[b3,b4,q_(2,0),...,q_(t-1,0)]`.  The residual variable list
`(4.2)` is what remains after those `2t+1` eliminations; it no longer inherits
a derivation gap.

**OPEN, unchanged:** `(8.1)` as a statement for every `t>=2`.  Exact unit
ideals at `t=1,2,3,4` and the modular `t=5,6` checks are finite tests, not an
induction.  The `t=1` fibre does not instantiate this spine and remains the
banked exact base case.  The charged `t=5, b4=1` timeout remains
`INCONCLUSIVE_TIMEOUT`.

The charged driver's `LAURENT_PIVOT_FORMULAS_PASS` was a consistency check
between an asserted linearization and a closed form.  That assertion is now
replaced by the jet calculation above.

## 7. Reproduction

```text
awk -F= '...' xmodel/k16-pivot-forms-grok46-20260903.run.v2 \
  > box/k16pivot-20260903/inputs.sha256
sha256sum -c box/k16pivot-20260903/inputs.sha256          # 13/13 OK
python3 box/k16pivot-20260903/terminal_laurent_model.py 2 3
python3 box/k16pivot-20260903/compare_rebuild.py          # PASS
python3 box/k16pivot-20260903/derive_pivot_forms.py       # ALL_PASS
```

The last prints the derived `b_j,d_j,n_j,dq_j,nq_j,p_b2`, the identically-zero
differences, the `A_t` reductions matching `(5.9)–(5.15)`, the denominator
root lists, the 32 exact specialisations, and the typed `t=6` gap.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9872`.
- Body SHA-256:
  `9e4b20438912e6efc3aca44697e6ec84794f387efcad79ff0660ae5ff174dfcb`.
- Frozen basis: `c3a3ae3b10d920018ed7797331e6473a626319d3`.
