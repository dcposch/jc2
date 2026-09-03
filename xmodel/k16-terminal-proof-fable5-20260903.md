# K=16 ray, terminal statement (8.1): closed indexed form, uniform b3-axis lemma, characteristic-zero kills at t=5,6,7, split-index checks

**Lane:** `k16-terminal-proof-fable5-20260903`  
**Date:** 2026-09-03.  Drivers and artifacts: `box/k16terminal-fable5-20260903/`.

## Verdict

**PARTIAL.  Theorem (T) on the ray is not proved for all `t` here.**  What is
new and typed:

- **PROVED-HERE, all `t>=2`:** a closed *indexed* form of the terminal family
  `T_(t,k)` (section 2), a uniform grading/support theorem (2.3), and the
  **b3-axis lemma** (section 3): on the line `b4=q_2,0=...=q_(t-1),0=0` the
  family collapses to `T_(t,2t-1)=alpha_t b3^2`, `T_(t,t-2)=beta_t b3^3`,
  `T_(t,0)=-c`, all other rows zero, with displayed `alpha_t,beta_t` in
  `Q(t)[d]/(3d^2-t-1)` whose norms are nonzero for every integer `t>=3` and
  vanish exactly at `t=2` (the factor `t-2`).  This is the structural reason
  for the banked `t=2` exception to RESIDUAL-ZERO.
- **PROVED-HERE, fixed `t`:** characteristic-zero certificates of (8.1),
  hence of (T) through the banked reduction chain, at `t=5` and `t=6`
  (previously `INCONCLUSIVE_TIMEOUT` / modular only) and at `t=7`; `t=2,3,4`
  re-certified.  The instrument is new (section 5.1): because the family
  `T_(t,1),...,T_(t,2t-1)` is weighted homogeneous, its zero locus is a
  *projective* family over the valuation ring of a good prime, so an empty
  fibre modulo the prime forces an empty generic fibre (properness).  A
  modular `dim=0` of the homogeneous ideal is therefore a characteristic-zero
  certificate that the cone is `{0}`; the exact number-field runs at `t=3,4`
  and the exact `t=2` fibres are independent controls, and the `t=2`,
  `y=1/5` fibre is the negative control (cone of dimension one, exactly and
  modulo `32003`).
- **Split index `t=11`** (`t=3*2^2-1`, both rational fibres `y=7/23,5/23`):
  spine replayed on both fibres; cone test `JPLUS` mod 32003: fibre `7/23` not finished, fibre `5/23` not finished; RESIDUAL-ZERO cone `RESZ` (rows at `b4=0`, ring without `b4`): fibre `7/23` not finished, fibre `5/23` not finished (INCONCLUSIVE_TIMEOUT where not finished).
- **Not obtained:** a `t`-uniform certificate for TOP-TAIL-UNIT or for
  RESIDUAL-ZERO off the b3-axis.  Section 4 shows why the obstruction is
  genuine: every coefficient carrying `b4` or a `q_j,0` has denominator
  divisible by Sol's pivot norms `F_C(t,j)`, `F_Q(t,j)` (irreducible in
  `(t,j)`), so it is a `t`-indexed sequence, not a polynomial in `t`.  The exact
  residual statement and its (now cheap) test are in section 8.

No exit-price assertion is made; no `charge_basis` line is due.

## 1. Custody

The receipt `xmodel/k16-terminal-proof-fable5-20260903.run.v2` was parsed with
`awk`; the paired `charged_input_<i>_sha256` / `_basename` fields generated
`/tmp/k16terminal_manifest.txt` and `sha256sum -c` returned `OK` for all
**19/19** frozen inputs.  No digest was retyped.  Only the frozen inputs were
used as mathematical sources; no ledger, `jc2-lean`, `ideation-*`, or
in-progress lane report was read or edited.  New files are confined to
`box/k16terminal-fable5-20260903/` and this report.

Notation as in the charged Sol report: `q=2t+1`, `e=3t+1`,
`H_t=12q^2y^2-12q(t+1)y+(t+1)(3t+2)`, `A_t=Q[y]/(H_t)`, `d=2qy-(t+1)`
(`3d^2=t+1` in `A_t`), `g1=e/q`, `g2=e(d+q)/(2q^2)`,
`g=g3=et(3d+2t+2)/(6q^3)`, `c=-yg`.

## 2. The closed indexed form of `T_(t,k)` (task 1)

### 2.1 The `w`-picture

Put `w=1/h` and `theta=w d/dw`.  Every polynomial in the charged h-chart is
`h^a f(w)` with `f` a polynomial in `w` whose `w^j` coefficient has weight `j`
in the second grading `wt(h)=1`, `wt(pi)=-t`, `wt(y)=wt(g)=0`, i.e.
`wt(b4)=1`, `wt(q_j,0)=j`, `wt(C_j)=j`, `wt(b3)=t+1`, `wt(b2)=2t+1`,
`wt(b1)=3t+1`, `wt(T(0))=t`.  The charged data are

```text
U = h^q u(w),        u = 1 + sum_(j=2)^(2t) q_j w^j          (gauge: no w, no w^q)
C = h^(t-1) c(w),    c = 1 + sum_(j=1)^(t-1) C_j w^j,        R = LC, L = h(1-b4 w)
T = h^t tau(w),      tau = g2 + sum_(j=1)^t T_j w^j          (T_t = T(0))
S = h^(2t) sigma(w), sigma = g1 + sum_(j=1)^(2t) S_j w^j
V' = h^(3t) v(w),    v = e + sum_(j=1)^(3t) v_j w^j
utilde = (q-theta)u,
kappa = (1-b4 w)^2 c - y b3 w^(t+1)                        (= Q1/h^(t+1))
psi   = (1-b4 w) sigma - b3 w^(t+1) tau - g b2 w^(2t+1)    (= P1/h^(2t+1))
phi   = (1-b4 w) tau - g b3 w^(t+1)                        (= P2/h^(t+1)).
```

The five Jacobian identities (2.3) of the charged report become polynomial
identities in `w` whose `w^j` coefficient is the weight-`j` band:

```text
(D3)  2y (t-theta) tau = g [ (3t+2-3 theta) c - 3 b4 w (t-1-theta) c ]
(D2)  y [ (4t+1-2theta) sigma - 2 b4 w (2t-theta) sigma ]
        = 3g utilde + (1-b4w) c tau - (1-b4w)^2 c (t-theta)tau
          + 2(1-b4w) tau (t-theta)[(1-b4w)c]
          + g b3 w^(t+1) [ c + (5/2)(t-theta)((1-b4w)c) ]
(D1)  2y (1-b4 w) v = y g b1 w^(3t+1) - kappa (2t+1-theta)psi
                       + psi (t+1-theta)kappa + 2 utilde phi
(D0)  Delta(w) := kappa v - utilde psi = y g w^(4t+1)
(gauge) [w^t] v = 0.                                                   (2.1)
```

Coefficientwise, (D3) and (D2) are the charged Euler recurrences (5.6)-(5.7b):

```text
T_j = g[(3t+2-3j) C_j - 3 b4 (t-j) C_(j-1)] / (2y(t-j)),      1<=j<=t-1,
S_j = { [w^j] RHS(D2) + 2y b4 (2t-j+1) S_(j-1) } / (y(4t+1-2j)), 1<=j<=2t.   (2.2)
```

(D1) is solved by `b1` (its `w^(3t+1)` coefficient, pivot `yg`) and then
defines `v` (pivot `2y`); the gauge solves `T_t` (pivot `q/y`); the
`w^1,...,w^(2t+1)` coefficients of `Delta` are the charged pivots
`C_1..C_(t-1), q_t..q_(2t), b2` with diagonals `p_C(t,j)`, `p_Q(t,j)`, `p_b2`
of (5.10)/(5.13)/(5.15); the `w^0` coefficient vanishes by (5.7a).  Then

```text
T_(t,k) = -[w^(4t+1-k)] sigma_t(Delta) + yg [k=0],   0<=k<=2t-1.          (2.3)
```

This is the requested closed form: a finite, division-free-until-the-listed-
pivots recurrence indexed by `(t,k)`, with every division by one of
`2y`, `y(t-j)`, `y(4t+1-2j)`, `yg`, `q/y`, `p_C(t,j)`, `p_Q(t,j)`, `p_b2`.
Its sign convention is the charged one (`T_(t,k)=[X^k]E_t`, `E_t=-(D0-yg)`).

### 2.2 Verification (t=2..7)

`laurent_spine.py` emits a Singular replay of (2.1)-(2.3) over `A_t`
(`minpoly=H_t` when `H_t` is irreducible; one run per rational fibre when it
splits).  Every step asserts the identities it uses (the `T` and `S`
recurrences, the three leading-coefficient identities (5.7a), divisibility by
`s`, the gauge, each pivot's affinity with a scalar nonzero coefficient, and
the vanishing of every band `>=2t` after the pivots).  Controls:

- the `t=2` rows on both fibres reproduce the banked `terminal_laurent_t2.json`
  exactly (sign `-E_t`): e.g. the `b3^2` coefficient of band 3 is `-28/625`
  at `y=2/5` and `0` at `y=1/5`, the `b3 b4^3` coefficient is `-77/80` at
  `y=1/5`;
- `pivot_control.py`: for `t=3,...,7` every one of the `2t+1` high pivot
  coefficients equals `p_C(t,j)`, `p_Q(t,j)`, `p_b2` exactly (ratio `1` in
  `A_t`), and the `b1`, `T(0)` pivots equal `yg`, `q/y`; printed
  `PIVOT_CONTROL_t{3..7}=PASS`;
- `ringmap_control.py`: at `t=3` the tests of section 5 repeated with `y` an
  ordinary variable and `H_t` an ideal generator over `Q` give the same
  dimensions, radical power and `b4` power (`vdim` 132 / 18).

Wall times of the exact replay (number field, `/usr/bin/time`): `t=3`
0.1 s, `t=4` 0.7 s, `t=5` 3.0 s, `t=6` 6.5 s, `t=7` 35 s, `t=8` 3 min 49 s
(max RSS 62 MB); the `t=7` rows occupy 4.6 MB, the `t=8` rows 10.7 MB.  The
modular replay at `t=11` takes 4 min 33 s per fibre.

### 2.3 Uniform support theorem (PROVED-HERE)

For `1<=k<=2t-1`, `T_(t,k)` is weighted homogeneous of weight `4t+1-k` in
`(b3,b4,q_2,0..q_(t-1),0)` (charged (6.3)); `T_(t,0)=-c+T^hom_(t,0)` with
`T^hom` of weight `4t+1`.  Consequently

```text
deg_(b3) T_(t,k) <= floor((4t+1-k)/(t+1)) ;  in particular
  deg_(b3) T_(t,k) <= 2 for k >= t (top tail), <= 3 always;
  b3^2 occurs in T_(t,k) only for k <= 2t-1, with cofactor of weight 2t-1-k;
  b3^3 occurs only for k <= t-2, with cofactor of weight t-2-k;
deg_(b4) T_(t,k) = 4t+1-k  (the pure b4 power is present, section 4).          (2.4)
```

Measured term counts (exact): `t=3`: 17,16,12,12,9,9 (bands 0..5);
`t=4`: 62,54,47,40,34,29,24,20; `t=5`: 191,171,145,128,105,92,75,64,51,44.
At `b4=0` every row is nonzero for `t=4,5` (the `t=3` vanishing of bands 2,4
is weight parity: all residual weights are even there).

## 3. The b3-axis lemma (PROVED-HERE, all `t>=2`)

On the axis `b4=q_2,0=...=q_(t-1),0=0` the grading forces every pivot to
vanish except `q_(t+1),0 = rho_t b3`, and forces
`T=g2 h^t`, `S=g1 h^(2t)+sigma_t b3 h^(t-1)`,
`V=h^e+nu_1 b3 h^(2t)+nu_2 b3^2 h^(t-1)`, `b1=b2=T(0)=0`.  Solving (2.1) on
the axis (`b3_axis_closed_form.py`, exact in `Q(t)[d]/(3d^2-t-1)`):

```text
rho_t   = -(6dt-3d+9t^2+2t-1)/(6t(3t-1)),
sigma_t = t(2t-d)(3t+1)/(2q^2(3t-1)),
nu_1    = -(3t+1)(3d+4t+1)/(12tq),
nu_2    = t(t-2)(3t+1)(6dt+d-3t-1)/(12(t-1)q^2(3t-1)(3t+2)),
```

the band-`3t` pivot on the axis equals `p_Q(t,t+1)` exactly (control), and

```text
T_(t,2t-1)|axis = alpha_t b3^2,   T_(t,t-2)|axis = beta_t b3^3  (t>=3),
T_(t,0)|axis = -c,  all other rows 0;

alpha_t = -t(3t+1)(27dt^3-30dt^2+dt-2d+6t^3+13t^2-3t+2)
          / (12 q^2 (3t-1)^2 (3t+2)),
beta_t  = t(t-2)(3t+1)(6dt-t-1) / (72 q^3 (3t-1)).                        (3.1)
```

Norms (`N(a+bd)=a^2-b^2(t+1)/3`, equivalently `Res_y(H_t,.)` up to the
nonzero factor `4q^2` of (1.1)):

```text
N(num alpha_t) = -(1/3) t^2 (t-2) (3t-1)^2 (3t+1)^2 (3t+2) (27t^3+17t^2+t+2),
N(num beta_t)  = -t^2 (t-2)^2 (t+1) (3t-1) (3t+1)^2 (4t+1).                (3.2)
```

Positive-integer roots: exactly `t=2` for both (the cubic `27t^3+17t^2+t+2`
is positive for `t>0`).  Hence:

- for every `t>=3`, `alpha_t` and `beta_t` are units of `A_t` (on split
  indices too), so the b3-axis meets `V(T_(t,1),...,T_(t,2t-1))` only at the
  origin, and `b3 in sqrt( <T_(t,1..2t-1)> + (b4,q_2,0,...,q_(t-1),0) )`;
- at `t=2`, `alpha_2=-14(d+1)/625`, `beta_2=0`: on the fibre `d=-1`
  (`y=1/5`) every positive-band row vanishes on the b3-axis and `T^hom_(2,0)`
  vanishes there too, so the b4=0 chart is still killed by `-c`.  This is the
  banked exceptional behaviour, now derived rather than observed.

Checks: `ALPHA_CHECK=0`, `BETA_CHECK=0` against the exact rows for
`t=2,3,4,5` (`structure_rows.py`); the specializations are
`alpha_3=-5(115d+68)/17248`, `beta_3=5(9d-2)/16464`,
`alpha_4=-13(625d+291)/205821`, `beta_4=13(24d-5)/72171`.

Geometrically the axis points are the "z-type" pairs `J(Q,P)=-cz`, and a
nonzero point of `V(T_(t,1..2t-1))` with `T^hom_(t,0)!=0` rescales to a
solution of (8.1); so (8.1) holds iff `T^hom_(t,0)` vanishes on the cone
`V(T_(t,1),...,T_(t,2t-1))`, and the natural sufficient statement is that
this cone is `{0}` (section 5).

## 4. Why nothing else has a polynomial-in-`t` closed form

Every coefficient of `T_(t,k)` multiplying a monomial that contains `b4` or
some `q_j,0` is obtained from the pivots `C_1,...,b2`, whose inverses carry
the norms `F_C(t,j)`, `F_Q(t,j)` of (5.11)/(5.14).  The exact b4-axis
coefficient of the first pivot `C_1 = gamma_(t,1) b4` has denominator equal
to the odd part of `F_C(t,1)`:

| `t` | `F_C(t,1)` | denominator of `gamma_(t,1)` |
|---:|---|---:|
| 3 | `2^4 5^2 59` | 295 |
| 4 | `2^3 3 5^2 113` | 565 |
| 5 | `2^3 3 73 89` | 6497 |
| 6 | `2^4 7 17 163` | 2771 |
| 7 | `2^5 3 5813` | 5813 |

This is a theorem, not an observation.  **Near-axis uniformity
(PROVED-HERE).**  Fix `W>=0`.  For `t>W` the coefficient in `T_(t,k)` of any
monomial `b3^a m` with `m` a monomial of weight `W` in `(b4,q_2,0,...)` is an
element of `Q(t)[d]` whose denominator divides `prod_(j<=W) F_C(t,j)` times
the listed rational diagonals: by the grading, only the pivots of weight
`<=W` (namely `C_1,...,C_W`) and the axis data of section 3 can enter, and
each is a fixed finite recurrence step in `Q(t)[d]`.  The first instance
(`weight1_closed_form.py`, weight-1 linearization of (2.1)) is

```text
C_1 |_(b4-axis) = gamma_(t,1) b4,
gamma_(t,1) = (-12dt^2+6dt+72t^3+22t^2-3t+2) / (48t^3+20t^2-t+2),
F_C(t,1) = 4(t+1)(48t^3+20t^2-t+2),                                     (4.1)
```

and the same linearization returns the band-`4t` diagonal equal to
`p_C(t,1)` (ratio `1`), an independent re-derivation of (5.10) at `j=1`.
Formula (4.1) reproduces the table above exactly at `t=3,...,7`.

Deeper pivots and every pure-`b4` row coefficient (`ROW_B4AXIS` in
`ax_t*.out`; 60-digit numerators at `t=3`, 100-digit at `t=4`) accumulate
products of these norms.  Since `F_C(t,j)` is an irreducible quartic in
`(t,j)` and the number of pivots is `2t+1`, the b4-axis values `tau_(t,k)` are
a `t`-indexed sequence whose denominators grow with `t`; they are not
elements of `Q(t)[d]` (the offset `4t+1-k` of the pure `b4` power grows with
`t`, so the uniformity statement above does not reach them).  The same holds on the `q_2,0`-axis (denominators
1201 at `t=3`, 1669 at `t=4` from `F_C(t,2)`).  The correct uniform statement
is therefore the recurrence (2.1)-(2.3) with the specialization denominator

```text
D_spine(t) = 60 (2t+1)^5 * prod_(j=1)^(t-1) F_C(t,j) * prod_(j=t)^(2t) F_Q(t,j)
             * prod_j (t-j)(4t-2j+1) * (t+1)(3t+2) * 12q^2(t+1)(4t+1),
```

which has no positive-integer root (every factor is positive on its index
range; `F_C(t,t-n)`, `F_Q(t,q-n)` are the manifestly positive forms (5.11),
(5.14)).  A generic-`t` unit certificate for (8.1) would in addition need a
`t`-uniform description of the *rows*, which does not exist in this sense;
this is the FALLACY-v2 reason a fixed-size certificate cannot be interpolated
from `t<=7`.

## 5. Exact fixed-`t` results (task 5, and new kills)

For each `t` the weighted ring is `A_t[b3,b4,q_2,0..q_(t-1),0]` with
`wp(t+1,1,2,...,t-1)`.  Tests (`analyze_rows.py`):

```text
JPLUS: dim <T_1..T_(2t-1)>            (0  =>  V = {0}  =>  (8.1))
T0HOM: least N with (T^hom_0)^N in J_+ (radical membership; the exact criterion)
RESZ : dim <T_1..T_(2t-1), b4>         (0  <=> RESIDUAL-ZERO)
TOPT : least N with b4^N in <T_t..T_(2t-1)>  (exists <=> TOP-TAIL-UNIT)
```

### 5.1 Promotion lemma (PROVED-HERE)

Let `R` be a discrete valuation ring with fraction field `K` and residue field
`kappa`, and `J` an ideal of `R[x_1,...,x_n]` generated by polynomials that
are homogeneous for positive integer weights.  If the affine cone
`V(J kappa[x])` is `{0}` over `kappabar`, then `V(J K[x])` is `{0}` over
`Kbar`.  Proof: `X=Proj(R[x]/J)` is a closed subscheme of a weighted
projective space over `Spec R`, hence proper over `Spec R`; its image is
closed.  The special fibre is `Proj(kappa[x]/J)`, empty exactly when the
cone modulo the maximal ideal is `{0}`; so the image misses the closed point,
and the only closed subset of `Spec R` missing the closed point is empty.
Hence `X` is empty and the generic fibre `Proj(K[x]/J)` is empty, i.e. the
cone over `K` is `{0}`.

Application.  Fix `t`, a prime `p` not dividing `12q^2` with a root `r` of
`H_t` modulo `p`, and the prime `P=(p, y-r)` of `Z[y]/(H_t)`.  The rows
`T_(t,k)` computed in `A_t` have coefficients `a+by` with `a,b` rational;
Singular's evaluation of these at `y=r` in `GF(p)` fails loudly on a
denominator divisible by `p` (`divzero_test.sing`: `? div. by 0` and
`? error occurred`), and no such marker occurs in any modular `.out/.err`
file used here (scanned for `div. by 0`, `div by 0`, `error occurred`).  Thus the rows lie in `R[x]` for the localisation `R` at
`P`, whose fraction field is `A_t` (a field for non-split `t`; for split `t`
each rational fibre is treated with `R=Z_(p)`), and the modular `JPLUS
dim=0` on one root is a characteristic-zero proof that
`V(T_(t,1),...,T_(t,2t-1))={0}`, hence of (8.1) and of (T) at that `t`.  This
is the *safe* direction: an inhomogeneous unit ideal modulo `p` proves
nothing (FALLACY-v2), but emptiness of a proper family is an open condition
on the base.  Negative control: at `t=2`, `y=1/5`, the cone has dimension one
exactly (the b3-axis) and dimension one modulo `32003`; the lemma's
contrapositive (nonempty generic fibre forces nonempty special fibre) is
satisfied.

### 5.2 Results

| `t` | fibre / field | JPLUS dim (time) | T0HOM power | RESZ dim | TOPT `b4^N` | charts `b4=0` / `b4=1` | typing |
|---:|---|---|---:|---:|---:|---|---|
| 2 | `y=1/5` (`d=-1`) | 1 (b3-axis) | 1 | 1 | 7 | UNIT / UNIT | exact, PROVED-HERE |
| 2 | `y=2/5` (`d=1`) | 0 | 1 | 0 | 10 | UNIT / UNIT | exact, PROVED-HERE |
| 3 | `Q(sqrt3)` | 0 (0.1 s) | 2 | 0 | 21 | UNIT / UNIT | exact, PROVED-HERE |
| 4 | `Q(sqrt15)` | 0 (22 s) | 2 | 0 | 36 (mod 32029) | UNIT / (banked) | exact dim, PROVED-HERE |
| 5 | `Q(sqrt2)` | 0 (mod 32009, both roots; exact `std` still running at deadline) | 2 | 0 | 55 (mod) | UNIT (mod) / – | PROVED-HERE via 5.1 |
| 6 | `Q(sqrt21)` | 0 (mod 32003, root 27617; 13 s) | 2 | 0 | 78 (mod) | UNIT (mod) / – | PROVED-HERE via 5.1 |
| 7 | `Q(sqrt6)` | 0 (mod 32059, root 4425; 1207 s) | 2 | 0 | – | – / – | PROVED-HERE via 5.1 |
| 8 | `Q(sqrt3)` | not finished (mod 32003, root 11288; host load ~55) | – | – | – | – | INCONCLUSIVE_TIMEOUT; exact rows and `PIVOT_CONTROL` exist |

Exact runs use `minpoly=H_t` (irreducible for `t=3..7` since `3(t+1)` is
not a square) or the two rational fibres at `t=2`; the `t=3` ring-map control
agrees; the `t=4` exact run (22 s) and the modular `t=4` runs (both roots)
agree, which is the positive control of 5.1.  Each `dim=0` line, exact or
promoted by 5.1, is a characteristic-zero certificate that
`V(T_(t,1),...,T_(t,2t-1))={0}`, hence of (8.1) at that `t`, hence — through
the banked, uniformly proved reduction (constant spine, normalizer lemma,
second affine spine) — of theorem (T) at that `t`.  **New:** `t=5` and `t=6`
are now characteristic-zero kills (the banked `t=5` `b4=1` chart had timed
out after 3600 s; the homogeneous test plus 5.1 replaces the inhomogeneous
chart).  At `t=7` the exact rows (4.6 MB) were produced and controlled (`PIVOT_CONTROL_t7=PASS`), but the exact homogeneous `std` was still running at the lane deadline on a host with load average about 60; that run is typed `INCONCLUSIVE_TIMEOUT` and is not a verdict.

The lead ideals show a stable pattern (MEASURED, not promoted):

```text
lead <T_1..T_(2t-1)>  contains  b3^2,  b3 b4^(t+2),  b4^(2t+4),  q_j,0^(t+7-j) (2<=j<=t-1)
    (t=2: b3^2,b3b4^4,b4^8; t=3: +q_2^8; t=4: +q_2^9,q_3^8; t=5: +q_2^10,q_3^9,q_4^8),
lead <T_1..T_(2t-1), b4>  contains  b3^2  (this is alpha_t, section 3).
```

The `b3^2` entry is the proved lemma; the others depend on b4-carrying
coefficients and are finite observations.

## 6. Split indices (task 5)

- `t=2` (`s=1`): both fibres exact, above.  On `y=1/5` the cone is the
  b3-axis (`dim 1`) and `T^hom_(2,0) in J_+` (power 1): (8.1) holds although
  RESIDUAL-ZERO fails, exactly as banked.
- `t=11` (`s=2`, `H_11 = 12(23y-7)(23y-5)`): `laurent_spine.py 11 --fibre
  7/23|5/23 --modp 32003` replays the spine in `GF(32003)` on each fibre:
  all spine assertions pass (`SPINE_OK t=11`), all `2t+1=23` high pivots
  and the `b1`, `T(0)` pivots are nonzero scalars, no `div. by 0` occurs
  (4 min, 9.3 MB of rows per fibre).  This is the requested numerical check
  of the whole proof spine at a split index in the product algebra: each
  factor is handled separately and no zero divisor is inverted.
  Cone tests on the modular rows: `JPLUS` mod 32003: fibre `7/23` not finished, fibre `5/23` not finished; RESIDUAL-ZERO cone `RESZ` (rows at `b4=0`, ring without `b4`): fibre `7/23` not finished, fibre `5/23` not finished.  Unfinished tests are typed `INCONCLUSIVE_TIMEOUT`, never a verdict.
  A characteristic-zero replay on both rational fibres was started and then
  stopped to respect the four-core budget on a host at load average 60; by
  section 5.1 it is not needed for the certificate (the fibres are rational,
  `R=Z_(p)`).

Modular cone tests (`modular_from_exact.py`, exact rows reduced with `y` a
root of `H_t` modulo a splitting prime; `JPLUS`/`RESZ` `dim 0` are
certificates by 5.1, `TOPT` powers and charts are MEASURED-MODULAR only): `t=4` mod 32029 (roots 25378, 31563), `t=5` mod 32009 (roots 1821, 15639),
`t=6` mod 32003 (roots 27617, 31466): on every root `JPLUS`, `RESZ`, `TOPT`
all have `dim 0`, `T0HOM` power 2, `b4=0` chart UNIT, `b4` powers
36 (`t=4`), 55 (`t=5`), 78 (`t=6`); lead ideals identical on the two roots.
Larger `t` (one root each, exact rows for `t=7,8`, modular spine for `t=9`): `t=7` mod 32059, root 4425: `JPLUS dim=0` (1207 s), `RESZ dim=0`; `t=8` mod 32003, root 11288: not finished (INCONCLUSIVE_TIMEOUT); `t=9` mod 32003, root 14748: not finished (INCONCLUSIVE_TIMEOUT).

## 7. TOP-TAIL-UNIT and RESIDUAL-ZERO: structure proved, certificate not

**Top tail.**  By (2.4) every top-tail row is quadratic in `b3`,
`T_(t,k)=A_k b3^2+B_k b3+C_k` with `A_k,B_k,C_k` of weights
`2t-1-k, 3t-k, 4t+1-k` in `(b4,q)`, and `A_(2t-1)=alpha_t` is a unit for
`t>=3` (section 3).  Hence `A_t[b4,q][b3]/(T_(t,2t-1))` is free of rank two
and TOP-TAIL-UNIT is equivalent to the statement that the images of
`T_(t,t),...,T_(t,2t-2)` at `b4=1` generate the unit ideal of that rank-two
algebra, i.e. that the `t-1` resultants `Res_(b3)(T_(t,2t-1),T_(t,k))|_(b4=1)`
and the `2x2` minors of the linear parts have no common zero in
`(q_2,0,...,q_(t-1),0)`.  This removes `b3` uniformly; the remaining
statement is a system in `t-2` variables whose coefficients are the
b4-carrying sequences of section 4.  The requested "which auxiliary each row
introduces with a unit leading coefficient" structure does **not** exist in
the charged coordinates: `T_(t,k)` at `b4=1` is not affine in any residual
variable (already at `t=2,y=2/5` the two top rows are two genuine quadratics
in `b3`), so the top tail is killed by resultants, not by a triangular affine
chain.  Exact `TOPT` powers: `b4^7,b4^10` (`t=2`), `b4^21` (`t=3`); modular
`b4^36` (`t=4`), `b4^55` (`t=5`).  The reduction is verified exactly at
`t=3` (`resultant_reduction.py`): the two resultants
`Res_(b3)(T_5,T_4)|_(b4=1)`, `Res_(b3)(T_5,T_3)|_(b4=1)` generate the unit
ideal of `A_3[q_2,0]`, and the `b4=0` resultants generate `(q_2,0^10)`, so
both lemmas are univariate statements there.  The `t=4` instance was started and not completed within the budget.

**Residual zero.**  Same reduction at `b4=0`: `b3` is integral of degree two
over `A_t[q]` modulo `T_(t,2t-1)|_(b4=0)` (unit `alpha_t`, `t>=3`), so
RESIDUAL-ZERO is equivalent to `V(Res_(b3)(T_(t,2t-1),T_(t,k))|_(b4=0),
k=1..2t-2) = {0}` in weighted `(q_2,0..q_(t-1),0)`-space.  On the b3-axis it is
proved (section 3); in general it is certified for `t=3..6` (exactly at
`t=3,4`, by 5.1 at `t=5,6`) , and by 5.1 at `t=7`, but the axis values carry the pivot
norms (section 4) and no uniform nonvanishing statement was obtained.

Neither lemma is therefore promoted beyond the finite exact range.

## 8. Exact residual statement and cheapest test

Remaining statement (implies (8.1), hence (T) on the ray):

```text
(V0)  V( T_(t,1), ..., T_(t,2t-1) ) = {0}  in  Abar^t  for every t>=3
      (both roots of H_t; equivalently dim_(A_t) A_t[b3,b4,q]/<T_1..T_(2t-1)> < infinity).
```

(8.1) itself is the weaker `T^hom_(t,0) in sqrt<T_(t,1),...,T_(t,2t-1)>`,
which is what holds at `t=2,y=1/5` where (V0) fails.  Proved strata of (V0):
the b3-axis for all `t>=3`.  Exact range of (V0): `t=3..6` (and `t=2` on
`y=2/5`).  Cheapest test at a new `t`: 

```text
python3 laurent_spine.py t --out t{t}_rows.txt > t{t}.sing; Singular -q t{t}.sing
python3 analyze_rows.py t t{t}_rows.txt > an.sing; Singular -q an.sing   # JPLUS dim
```

(seconds for the spine; the homogeneous `std` is the only cost).  By the
promotion lemma 5.1 the modular replica is not a screen but a proof:

```text
python3 laurent_spine.py t --fibre r --modp p --out rows.txt > s.sing   # r a root of H_t mod p
Singular -q s.sing;  python3 analyze_rows.py t rows.txt --fibre r --modp p > an.sing; Singular -q an.sing
```

(`queue_modular_t.sh t1 t2 ...` automates prime/root selection).  A printed
`JPLUS t=.. dim=0` proves (V0), hence (8.1) and (T), at that `t`; a nonzero
dimension is a non-result (the lemma has one direction only).  This is the
cheapest exact test known for the ray: the whole chain at `t=11` costs
minutes.
The cheapest *uniform* target consistent with section 4 is a recurrence
proof that the `t-1` resultants of section 7 have a unit-coefficient pure
power of `q_(t-1),0`; the lead-ideal pattern `q_j,0^(t+7-j)` of section 5 is
the finite evidence.

## 9. FALLACY-v2 audit and denominators

- `A_t` is treated as a rank-two algebra: exact runs use `minpoly` only when
  `H_t` is irreducible over `Q` (checked: `3(t+1)` not a square), split
  indices run per rational factor; no zero divisor is inverted (the only
  zero-divisor candidates met, `alpha_2`, `beta_2`, are recorded, not inverted).
- Every inversion in the spine is one of the listed diagonals; all were
  asserted nonzero in the field at run time and match the charged closed
  forms (`PIVOT_CONTROL` PASS), whose norms are (5.11), (5.14), (5.15).
- The uniform lemma of section 3 is a formula proof in `Q(t)[d]` with the
  displayed norms and explicit positive-integer root set `{2}`; it was
  specialised to `t=2,3,4,5` and matched the exact objects.
- Modular results are promoted only through the proper-family lemma 5.1,
  which applies to the weighted-homogeneous cone statement (V0) and never to
  an inhomogeneous chart; its hypotheses (good prime, no denominator
  divisible by `p`, root of `H_t` mod `p`, positive weights) are checked per
  run, and its one-directional nature is respected (a modular nonzero
  dimension proves nothing).  The `t=2`, `y=1/5` fibre is the negative
  control; the exact `t=3,4` runs are the positive controls.
- Ring maps: the analysis ring keeps the charged generator names and order
  `(b3,b4,q_2,0,...)`; the sign convention `T=[X^k]E_t` is fixed by the
  banked `t=2` record.  `dim` is read in the declared weighted ring; the
  radical-membership test is by explicit powers, not by `sat()`.
- No fixed-size certificate was interpolated from finite `t` (section 4).

## 10. Reproduction and artifacts

```text
cd box/k16terminal-fable5-20260903
python3 b3_axis_closed_form.py                         # (3.1),(3.2), pivot control on the axis
python3 laurent_spine.py 3 --out t3_rows.txt > t3.sing && Singular -q t3.sing
python3 pivot_control.py 3 t3_rows.txt                 # PIVOT_CONTROL_t3=PASS
python3 analyze_rows.py 3 t3_rows.txt --b4one > an_t3.sing && Singular -q an_t3.sing
python3 structure_rows.py 3 t3_rows.txt > st.sing && Singular -q st.sing   # ALPHA/BETA_CHECK
python3 laurent_spine.py 2 --fibre 1/5 --out t2_f15_rows.txt > t2.sing && Singular -q t2.sing
python3 laurent_spine.py 11 --fibre 7/23 --modp 32003 --out r.txt > t11.sing && Singular -q t11.sing
```

Files: `t{2..7}_rows.txt` (exact rows, pivots, `b1`, `T(0)`),
`an_t*.out` (tests), `st_t*.out`, `ax_t*.out` (axis data),
`t11_f{723,523}_p32003_rows.txt` (modular rows), `an_t*_p*_r*.out`
(modular controls), `SHA256SUMS.final` (manifest, checked with
`sha256sum -c` from inside the directory).  Final manifest: files=179 sha256=bf52bb244be97975d406a22390f6343cd7d1d32dfa80d39d718ac8bfb3ac5311.

<!-- BODY-END -->
