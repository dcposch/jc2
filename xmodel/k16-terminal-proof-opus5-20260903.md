# The K=16 terminal statement (8.1): the weighted cone, the extended grading,
# and a proved b3-axis theorem for every `t`

Third independent attack on the last statement of the K=16 ray,

```text
<T_(t,0),...,T_(t,2t-1)> = [1]  in  A_t[b3,b4,q_2,0,...,q_(t-1),0]   (8.1)
```

by a route disjoint from band-index induction: the weighted cone structure of
the terminal family, the extension of the (6.3) grading to the whole second
affine spine, and the exact collapse of that spine on coordinate sub-charts.

## Verdict

```text
(T) on the ray for all t>=1 : NOT PROVED here.  Typed OPEN, with four
                              promotions and one strictly sharper criterion.

PROVED-HERE-1  Lemma CONE.  With I_(t,+)=<T_(t,1),...,T_(t,2t-1)> and
               T_(t,0)=c+tau_t (c=-yg a unit, tau_t weighted homogeneous of
               weight 4t+1),
                   (8.1)  <=>  tau_t in sqrt(I_(t,+))
               on every geometric point of Spec A_t; and
                   dim I_(t,+) = 0  =>  (8.1).
               Band zero leaves the search; the test becomes homogeneous.

PROVED-HERE-2  The (6.3) grading extends to all 6t+2 spine variables:
               wt(h)=wt(b4)=1, wt(C_j)=wt(q_(j,0))=j, wt(T(0))=t,
               wt(b_i)=(4-i)t+1.  The 2t+1 eliminated variables carry the
               distinct weights 1,...,2t+1, matched to bands 4t,...,2t.

PROVED-HERE-3  Sub-chart collapse principle, and the b3-axis theorem: on
               S={b4=0, q_(2,0)=...=q_(t-1,0)=0} the whole spine collapses to
               one scalar, and for every t>=2
                   T_(t,k)|_S = 0 for k not in {0,t-2,2t-1},  T_(t,0)|_S = c,
                   T_(t,2t-1)|_S = alpha_t b3^2,  T_(t,t-2)|_S = phi_t b3^3,
               with closed alpha_t, phi_t and their exact norms.  Both are
               units of A_t for every t>=3.

PROVED-HERE-4  The t=2 anomaly is the single factor (t-2), shared by alpha_t
               and phi_t; it degenerates on exactly one fibre (d=-1, y=1/5).
               There W is nonempty yet (8.1) holds, so RESIDUAL-ZERO is
               sufficient but NOT necessary.  Lemma CONE supplies the correct
               necessary and sufficient replacement.

Route (1) generating functions : CLOSED-STRUCTURE, NOT-HYPERGEOMETRIC (Sec. 6).
Route (2) q-affine top tail    : the charged hypothesis is FALSE (Sec. 7);
                                 what survives is deg_(b3) <= 2, proved.
```

`FALLACY-v2` applies throughout.  No exit-price assertion is made here, so no
`charge_basis` line is declared.  No ledger, `jc2-lean`, `ideation-*` or
in-progress lane report was read or written.

## 0. Custody

The 20 charged inputs were verified mechanically: the manifest was generated
from `xmodel/k16-terminal-proof-opus5-20260903.run.v2` with

```text
awk -F= '/^lane_inputs_dir=/{dir=$2}
 /^charged_input_[0-9]+_sha256=/{split($1,a,"_"); sha[a[3]]=$2}
 /^charged_input_[0-9]+_basename=/{split($1,a,"_"); base[a[3]]=$2}
 END{for(i=1;i<=20;i++) printf "%s  %s/%s\n", sha[i], dir, base[i]}' ... \
 | sha256sum -c
```

and all 20 lines report `OK`.  Drivers and artifacts are in
`box/k16terminal-opus-20260903/`.  All exact terminal records used are the
charged `box/k16spine-20260903/terminal_laurent_t{2,3,4,5}.json` plus chart
records built here from the charged `terminal_laurent_model.py`.

Typing of the algebra.  `A_t = Q[y]/(H_t)`, `H_t = 12q^2y^2-12q(t+1)y+(t+1)(3t+2)`,
`q=2t+1`, `e=3t+1`.  Put `d = 2qy-(t+1)`; then `3d^2 = t+1` in `A_t`, so
`A_t = Q[d]/(3d^2-(t+1))`.  `H_t` is reducible over `Q` exactly when
`t = 3s^2-1`; among `2<=t<=8` only `t=2` splits, and there every statement below
is made separately on the two rational fibres `y=1/5` (`d=-1`) and `y=2/5`
(`d=+1`).  For `3<=t<=8`, `A_t` is a quadratic field and the Singular runs carry
`minpoly = H_t/lc(H_t)`.  Nothing is divided by a zero divisor: every inverted
scalar is displayed with its norm `N(Ad+B) = B^2 - A^2(t+1)/3`, a rational
associate of `Res_y(H_t, .)`.

## 1. Lemma CONE: (8.1) is a statement about a weighted cone

Recall (6.3): with `wt(b4)=1`, `wt(q_(i,0))=i`, `wt(b3)=t+1`, each `T_(t,k)` for
`1<=k<2t` is weighted homogeneous of weight `4t+1-k`, and

```text
T_(t,0) = c + tau_t,   c = -y g,   tau_t weighted homogeneous of weight 4t+1.
```

`a1_homog.py` re-verifies this band by band on the charged records and prints
`GRADING_t = PASS` for `t=2,3,4`; it also prints the weight-0 part of band
zero and confirms it equals `c` exactly (for instance `28/625-7y/25` at `t=2`,
which is `-yg` reduced mod `H_2`).

**Lemma CONE.** Let `K` be an algebraically closed field and `A_t -> K` a ring
map (a geometric point of `Spec A_t`; there are exactly two).  Write
`I_(t,+) = <T_(t,1),...,T_(t,2t-1)>`, `Z_+ = V(I_(t,+)) subset A^t_K` in the
coordinates `(b4,q_(2,0),...,q_(t-1,0),b3)`, and `Z = V(T_(t,0),...,T_(t,2t-1))`.
Then

```text
Z = empty   <=>   tau_t vanishes identically on Z_+   <=>  tau_t in sqrt(I_(t,+)).
```

*Proof.* The `G_m`-action `lam.(b4,q_i,b3) = (lam b4, lam^i q_i, lam^(t+1) b3)`
preserves `Z_+`, because every generator is weighted homogeneous of positive
weight.  If `tau_t` vanishes on `Z_+`, then `T_(t,0) = c` on `Z_+` and `c` is a
unit of `A_t`, hence nonzero in `K`; so `Z = empty`.  Conversely let `x in Z_+`
with `tau_t(x) != 0`.  Since `K` is algebraically closed choose `lam` with
`lam^(4t+1) = -c/tau_t(x)`.  Then `lam.x in Z_+` and

```text
T_(t,0)(lam.x) = c + lam^(4t+1) tau_t(x) = c - c = 0,
```

so `lam.x in Z`.  The last equivalence is the Nullstellensatz over `K`. `[]`

**Corollary C1.** `Z_+ = {0}`  =>  `(8.1)`, because `tau_t` has positive weight
so `tau_t(0)=0`.  Since `I_(t,+)` is homogeneous, `Z_+` is a cone through the
origin, hence

```text
Z_+ = {0}   <=>   dim I_(t,+) = 0.                                   (1.1)
```

**Corollary C2.** The producer's split is exactly the chart-wise verification
of `Z_+={0}`: `RESIDUAL-ZERO` is `Z_+ cap {b4=0} = {0}` and `TOP-TAIL-UNIT`
implies `Z_+ cap {b4!=0} = empty`.  Lemma CONE shows this is sufficient but not
necessary, and Section 5 exhibits a live failure of necessity at `t=2`.

Two practical consequences, both used below.

* Band zero, the row with the largest support and the only inhomogeneous one,
  is removed from the search.  Only its weight-0 part `c`, already a banked
  unit, is used.
* The remaining test is *homogeneous*.  A weighted-degree `std` plus `dim` is
  substantially cheaper than the inhomogeneous unit test on the `b4=1` chart
  that the charged report recorded as `INCONCLUSIVE_TIMEOUT` at `t=5`.

## 2. The grading on the whole second spine

The (6.3) grading is the restriction of a grading of the entire post-spine
Laurent chart.  Assign

```text
wt(h) = wt(s) = wt(b4) = 1,
wt(C_j)     = j        (1<=j<=t-1),
wt(q_(j,0)) = j        (2<=j<=2t),
wt(T(0))    = t,
wt(b_i)     = (4-i)t+1  (i=1,2,3,4),  i.e. 3t+1, 2t+1, t+1, 1,
wt(y) = wt(g) = wt(g1) = wt(g2) = wt(c) = 0.                       (2.1)
```

Then, by direct inspection of (2.2)-(2.4) of the charged spine report,
`U`, `Q1 = LR-yb3`, `Q2 = yL` are homogeneous with `wt(1/pi)=t` making `Q`
homogeneous of weight `q`; `P0,P1,P2,P3` make `P` homogeneous of weight `e`;
`D0,...,D4` are homogeneous; `E_t` of (6.1) is homogeneous of weight `4t+1`;
and band `k` of `E_t` has weight `4t+1-k`.  This is uniform in `t` and uses no
fixed-`t` data.

Mechanical confirmation.  `a4_weights.py` reads the charged records and checks
that every solved right-hand side (both auxiliary pivots and all `2t+1` high
pivots) is weighted homogeneous of exactly the weight of the variable it
solves, and that the eliminated variables carry the weights `1,2,...,2t+1` in
bijection with the bands `4t,4t-1,...,2t`.  It prints `WEIGHTS_t = PASS` for
`t=2,3,4`.

This is a different grading from the intrinsic one of the banked
`17(xx)` Section 1 (`wt(gamma)=wt(pi)=1`, `wt(b_i)=i`, `wt(h)=4`); the two live
on different rings (the `alpha/beta` chart there, the post-spine Laurent chart
here) and no uniqueness claim is made for either.  On the `b_i` alone the two
are related by `(2.1) = -t*(intrinsic) + (4t+1)*(number of b-factors)`.

Immediate corollaries, all uniform in `t`:

```text
deg_(b3) T_(t,k) <= floor((4t+1-k)/(t+1)) <= 3,  and <= 2 for k >= t-1;
[b3^2] T_(t,2t-1) has weight 0, i.e. is a scalar of A_t;
[b3^2] T_(t,2t-1-r) has weight r.                                   (2.2)
```

Observed degrees agree exactly: `deg_(b3) T_(t,k) = 3` for `k<=t-2` and `= 2`
for `k>=t-1` at `t=2,3,4` (`b3_toptail.py`, `a1_homog.py`).

## 3. The sub-chart collapse principle

**Proposition SUBCHART.** Let `R` be a subset of the residual variables and let
`S` be the coordinate sub-chart on which the residual variables outside `R` are
set to `0`.  Let `Sem(R)` be the numerical semigroup generated by the weights of
`R`.  Then on `S` every eliminated variable whose weight lies outside `Sem(R)`
restricts to `0`, and the others restrict to `A_t`-combinations of the monomials
in `R` of the given weight.

*Proof.* By Section 2 the solved value of each eliminated variable is weighted
homogeneous, in the residual variables, of that variable's weight.  Setting the
complementary variables to zero deletes every monomial that involves them; what
remains is spanned by monomials in `R` of that weight, and there are none when
the weight is outside `Sem(R)`. `[]`

The bound is sharp and, when the weight admits a unique monomial, the solved
value is forced to be one `A_t`-scalar times that monomial.  `c4_subchart_check.py`
controls this on a *second* sub-chart, `R = {q_(t-1,0), b3}`: it restricts all
`2t+1` high pivots of the charged records and checks the surviving support
against the semigroup prediction, printing `SUBCHART2_t = PASS` at `t=4` and
`t=5`.  Both index collisions are exercised there: `b2` (weight `2t+1`) survives
at `t=4` because `2t+1 = 3(t-1)` exactly then, and vanishes at `t=5`, both as
predicted.  (The `b1` and `T(0)` right-hand sides are recorded before the high
substitutions, so they are still functions of not-yet-eliminated variables;
their grading is checked by `a4_weights.py` instead.)

This is where the present route separates from band-index induction: it does
not iterate over bands at all.  It chooses a sub-chart in which the triangular
solve degenerates, and then the whole spine is available in closed form.

## 4. The b3-axis theorem

Take `R = {b3}`, `wt(b3)=t+1`, so `S = {b4=0, q_(2,0)=...=q_(t-1,0)=0}` and
`Sem(R) = (t+1)Z_(>=0)`.  The eliminated weights are `1,...,t-1` (the `C_j`),
`t,...,2t` (the `q_(j,0)`), `2t+1` (`b2`), together with `t` (`T(0)`) and `3t+1`
(`b1`).  In `[1,2t+1]` the only multiple of `t+1` is `t+1`; and for `t>=2`
neither `t` nor `3t+1` is a multiple of `t+1`.  Hence on `S`

```text
C_j = 0 (all j),  T(0)=0,  b1 = b2 = 0,  q_(j,0)=0 for j != t+1,
q_(t+1,0) = lam * b3   for a single scalar lam in A_t.               (4.1)
```

So on `S` the entire `5t+2`-step spine collapses to one linear equation.
Writing it out (`c1_b3axis.py`, all arithmetic in `Q(t)[d]/(3d^2-(t+1))`):

```text
C = h^(t-1),   R = A = h^t,   U = h^q + lam*b3*h^t,
B  = g2 h^t,                         g2 = g(3t+2)/(2ty),
D  = g1 h^(2t) + delta h^(t-1),      delta = g(6t*lam*b3+(5t+2)b3)/(2y(2t-1)),
Y  = g1 h^q + eta h^t,               eta = delta - g2 b3,
Z  = g2 h^(t+1) - g b3,
X' = e h^(3t) + Bc h^(2t-1) + Cc h^(t-2),
Bc = (eta + q y g1 b3 - 2 q g b3 + 2 t g2 lam b3)/(2y),
Cc = t b3 (y*eta - 2 lam b3 g)/(2y).                                 (4.2)
```

Then `Phi = Q1 X' - U' Y + c` has only the bands `4t+1, 3t, 2t-1, t-2, 0`:

```text
band 4t+1 = e - q g1 = 0                    identically, by 2q g2 - t g1 = 2ey;
band 3t   = Bc - y b3 e - q eta - t lam b3 g1 = 0   determines lam;
band 2t-1, band t-2  are terminal;  band 0 = c.                      (4.3)
```

The three leading-coefficient identities (5.7a) are re-derived and printed as
identically zero by the same script, which also verifies `H_t <-> 3d^2=t+1`.

Solving band `3t`:

```text
lam = (3d - 6dt - 9t^2 - 2t + 1) / (6t(3t-1)).                       (4.4)
```

Substituting into (4.3) gives the two surviving terminal rows, in closed form
for every `t >= 2`:

```text
T_(t,2t-1)|_S = alpha_t * b3^2,
alpha_t = t(3t+1) * [ (27t^3-30t^2+t-2) d + (6t^3+13t^2-3t+2) ]
          / ( 12 q^2 (3t-1)^2 (3t+2) ),                              (4.5)

T_(t,t-2)|_S = phi_t * b3^3,
phi_t   = - t (t-2) (3t+1) * ( 6t d - (t+1) )
          / ( 72 q^3 (3t-1) ),                                       (4.6)

T_(t,0)|_S = c,     T_(t,k)|_S = 0  for k not in {0, t-2, 2t-1}.     (4.7)
```

Norms (the decision rule (1.1) of the charged spine report):

```text
N( 6t d - (t+1) )                     = -(t+1)(3t-1)(4t+1),
N( (27t^3-30t^2+t-2) d + (6t^3+13t^2-3t+2) )
      = -(t-2)(3t-1)^2(3t+2)(27t^3+17t^2+t+2)/3.                     (4.8)
```

The first has no root at any integer `t>=1`.  The second has the single
positive integer root `t=2` (the cubic `27t^3+17t^2+t+2` is positive for
`t>=1`).  The rational prefactor of `phi_t` vanishes exactly at `t=0,2`; that of
`alpha_t` only at `t=0`.  Therefore:

**Theorem B3-AXIS.** For every `t>=3`, both `alpha_t` and `phi_t` are units of
`A_t`, and `Z_+ cap S = {0}`.  Equivalently

```text
b3 in sqrt( I_(t,+) + (b4, q_(2,0),...,q_(t-1,0)) )   for every t>=3,
```

certified by band `t-2` alone (or by band `2t-1` alone).  For `t=2`, `phi_2=0`
and `alpha_2` is a rational multiple of `d+1`, whose norm is `0`; it vanishes on
exactly the fibre `d=-1`, i.e. `y=1/5`.

Formula control.  `c2_verify.py` restricts every available exact record to `S`
and compares band by band against (4.5)-(4.7).  It prints
`SUBCHART_FORMULA_CONTROL = PASS` on ten records: the charged
`terminal_laurent_t{2,3,4,5}.json` and the chart records
`chart_t{2,3,4,5,6,7}_b4_0.json` built here.  The formulas were *derived*, not
interpolated; the ten records are an independent check of the derivation, and
they include `t=6,7`, beyond any fixed-`t` datum used anywhere in the campaign.

Chart control.  `a5_control.py` checks that the `b4`-specialised model runs
reproduce the `b4`-specialisation of the charged full records band by band, and
prints `CHART_CONTROL = PASS` for `t=2,3,4` on both charts.

## 5. The `t=2` base case, and why RESIDUAL-ZERO is not necessary

By (4.7) with `t=2` (so `t-2 = 0` and `2t-1 = 3`), on `S = {b4=0}` -- which at
`t=2` is the whole `b4=0` chart, since there are no `q_(i,0)` --

```text
T_(2,1)|_(b4=0) = T_(2,2)|_(b4=0) = 0,   T_(2,3)|_(b4=0) = alpha_2 b3^2,
T_(2,0)|_(b4=0) = c + phi_2 b3^3 = c.                                 (5.1)
```

On the fibre `y=1/5` we have `alpha_2 = 0`, so *every* positive band vanishes on
`{b4=0}` and `Z_+` contains the whole `b3`-axis.  The homogeneous dimension test
confirms this independently:

```text
dimtest_t2_branch0 : DIM=1,  lead(G) = b4^6, b4^4 b3, b4^2 b3^2
dimtest_t2_branch1 : DIM=0,  lead(G) = b4^6, b4^4 b3, b4^2 b3^2, b3^3
```

so `Z_+` is one-dimensional on `y=1/5`.  Nevertheless `(8.1)` holds there, and
Lemma CONE says exactly why: `phi_2 = 0` forces `deg_(b3) T_(2,0) <= 2`, and
every weight-9 monomial in `b4` (weight 1) and `b3` (weight 3) of `b3`-degree at
most `2` is divisible by `b4^3`.  Hence `tau_2 = b4^3 * (...)`, so `tau_2`
vanishes on `{b4=0}` and lies in `sqrt(I_(2,+))`.  `c3_t2_cone.py` prints
`tau_2 | b4=0 : 0` and confirms mechanically, on both fibres,

```text
t=2 branch0 RABINOWITSCH_tau_in_radical = 1    t=2 branch0 y=1/5 UNIT_IDEAL_8.1 = 1
t=2 branch1 RABINOWITSCH_tau_in_radical = 1    t=2 branch1 y=2/5 UNIT_IDEAL_8.1 = 1
```

The Rabinowitsch test is `1 in <I_(2,+), 1 - z*tau_2>` in `Q[z,b4,b3]`; no
`sat()` wrapper is used anywhere in this report, so the corresponding
`FALLACY-v2` hazard does not arise.  Positive control: the same script's direct
`std` of the *full* four-row ideal returns `[1]` on both fibres, reproducing the
banked `t=2` product-algebra base case.

This makes the `t=2` behaviour a derived consequence of one closed formula, the
factor `(t-2)` shared by (4.5) and (4.6), rather than a sampled exception.  It
also settles a structural question the charged report left open: the two-lemma
split (8.2) is *strictly stronger* than (8.1), and any induction that tries to
prove `RESIDUAL-ZERO` for all `t>=2` is proving something false.

## 6. Route (1): generating functions and the Euler structure

The requested question -- is `sigma_t(E_t)` an `X`-truncation of a product or
composition of a few fixed power series with coefficients hypergeometric in
`(t,k)`? -- has a definite two-part answer.

**Closed, `t`-independent operator description (yes).**  In the variable
`s = X - b4`, with `C` monic of degree `t-1` and `U` monic of degree `q`:

```text
B  = T(0) + (g/2y) ( 3 s C + 2 Int_0^s C ),                          (6.1)
D  = Euler^(-1)(rhs_D),   [s^m] D = [s^m] rhs_D / (y(2m+1)),
     equivalently, with s = w^2,  D(w^2) = (1/(y w)) Int_0^w rhs_D(v^2) dv,
X' = ( y g b1 - Q1 Y' + Q1' Y + 2 U' Z ) / (2 y s),                  (6.2)
Phi = Q1 X' - U' Y + c,
T_(t,k) = [h^k] Phi(h - b4) = (1/k!) (d/ds)^k Phi |_(s=-b4).          (6.3)
```

(6.1) is (5.6) integrated; the closed integral form of the Euler inverse (5.7b)
is a half-integration.  The operator list -- multiply, differentiate, integrate,
half-integrate, divide once by `s` -- is fixed; `t` enters only through the two
degrees `2t+1`, `t-1`, the four scalars `y,g,g1,g2 in A_t`, and the elimination
of the top `2t+1` bands.  (6.3) is worth isolating on its own: the terminal
family is the `2t`-jet of `Phi` at `s = -b4`, so `(T)` says that `D0 + c` cannot
vanish to order `2t` at `h=0`.

**Hypergeometric coefficients (no).**  The obstruction is not the Euler
structure but the band elimination.  Its diagonals `p_C(t,j)`, `p_Q(t,j)`,
`p_b2` of (5.10), (5.13), (5.15) are rational in `(t,j)`, but the *solved
values* are the full triangular product of those steps, and no fixed-length
product or composition of series reproduces them.  Section 4 is the positive
control for this diagnosis rather than a refutation of it: on the one sub-chart
where the triangular solve degenerates to a single equation, the answer is
immediately an explicit rational function of `(t,d)`, namely (4.4)-(4.6).  This
is why a Wronskian or resultant of two fixed series is not available as posed;
the uniform objects that do exist are the weighted initial forms, and
Section 4 is the first of them.

Typed: `GF-OPERATORS-CLOSED / COEFFICIENTS-NOT-HYPERGEOMETRIC`.  No claim is
made that some other presentation is impossible; this is a negative result
about the presentation reached through `sigma_t`.

## 7. Route (2): the `b4=1` top tail

The charged parenthetical -- do the `q_(j,0)` enter the top-tail rows affinely?
-- is answered in the negative, exactly.  From `a1_homog.py`:

```text
t=4, top tail k=4..7:  deg_(q_2,0) = 6,6,5,5   deg_(q_3,0) = 4,4,3,3
t=3, top tail k=3..5:  deg_(q_2,0) = 5,4,4
```

so no affine elimination of the `q_(j,0)` from the top tail exists, and the
proposed reduction of `TOP-TAIL-UNIT` to polynomials in `b3` alone is not
available in that form.  What is available, and is proved by (2.2):

```text
every top-tail row is quadratic in b3;
[b3^2] T_(t,2t-1) is the scalar alpha_t of (4.5), a unit for t>=3;
[b3^2] T_(t,2t-1-r) is weighted homogeneous of weight r in (b4,q).   (7.1)
```

So on `b4=1` the top tail is `t` quadratics in `b3` over `A_t[q_2,...,q_(t-1)]`,
the topmost with a scalar unit leading coefficient for `t>=3`.  Eliminating
`b3` by a pairwise resultant is therefore legitimate for `t>=3`, but it leaves
`t-1` resultants in `t-2` variables and no uniform recursion in `t` was
obtained.  `TOP-TAIL-UNIT` is re-verified exactly here at `t=2` (both fibres),
`t=3` and `t=4` (`toptail_*.out`, `UNIT=1`, `DIM=-1`), matching the banked
record.

## 8. New exact evidence

All tests below are the *homogeneous* ones licensed by (1.1).  Ring, generator
order and coefficient field are declared in each emitted `.sing` file; the
variable order is `(b4, q_(2,0),...,q_(t-1,0), b3)` with weights
`wp(1,2,...,t-1,t+1)`.

```text
full cone,  dim I_(t,+)  (EXACT unless marked):
  t=2 y=1/5 : DIM=1, 3 basis elements   (negative control -- see Sec. 5)
  t=2 y=2/5 : DIM=0, 4 basis elements
  t=3       : DIM=0, 20  => (8.1) at t=3 by Corollary C1
  t=4       : DIM=0, 81  => (8.1) at t=4 by Corollary C1
  t=5       : exact run INCOMPLETE at seal (typed INCONCLUSIVE_TIMEOUT, never
              NONUNIT);  modulo 1009 on the quadratic extension of F_1009:
              DIM=0, 340 basis elements.  Modular only; not promoted.

b4=0 cone,  dim I_(t,+)|_(b4=0)   (RESIDUAL-ZERO in cone form; EXACT unless marked):
  t=3 : DIM=0,   4 basis elements, lead ideal contains b3^3
  t=4 : DIM=0,  17 basis elements, lead ideal contains b3^4
  t=5 : DIM=0,  54 basis elements   <-- EXACT, new; charged record has t=5
  t=6 : DIM=0, 185 basis elements   <-- EXACT, new; charged record has t=6
                                        only modulo 1009 (which reproduces
                                        DIM=0 with the same 185 here)
  t=7 : exact run INCOMPLETE at seal (INCONCLUSIVE_TIMEOUT)
```

So `RESIDUAL-ZERO` now holds in characteristic zero at `t=3,4,5,6`, two indices
beyond the charged exact record, and `(8.1)` itself is certified outright by
Corollary C1 at `t=2,3,4` (exact) and `t=5` (modulo 1009 only).

The `b4=0` chart records at `t=6,7` are new exact objects, built with the
charged `terminal_laurent_model.py` specialised at `b4=0` before construction.
That specialisation is legitimate because every spine pivot coefficient is a
weight-0 scalar of `A_t`, hence unchanged by it; it is controlled against the
charged full records at `t=2,3,4` (`CHART_CONTROL = PASS`).  A modular fallback
at `t=7` was attempted and *failed cleanly*: `H_7` is reducible modulo `1009`,
so Singular rejects the minpoly.  The correct handling is to branch to the two
roots mod `1009`; that was not run here and no modular `t=7` claim is made.

The lead-ideal pattern `b3^t` reported in the charged (7.1) is confirmed at
`t=3,4` in characteristic zero here, and Theorem B3-AXIS explains its source:
band `t-2` contributes `phi_t b3^3` with `phi_t` a unit, and the remaining
powers come from the mixed bands.

## 9. Denominators and the FALLACY-v2 audit

Every division performed in Section 4 is displayed.  The list, with all integer
roots:

```text
2y, y(4t+1), y(2t-1)      Euler and B diagonals; y is inverted with
                          Res_y(H_t,y) = (t+1)(3t+2) != 0 (banked (5.7c));
2t, 2(2t-1)               integration and eta;
6t(3t-1)                  the lam solve (4.4);
12 q^2 (3t-1)^2 (3t+2)    alpha_t;
72 q^3 (3t-1)             phi_t.
```

Integer roots of `t, 2t-1, 4t+1, 3t-1, 3t+2, q=2t+1`: `0, 1/2, -1/4, 1/3, -2/3,
-1/2`.  None is a positive integer, so no denominator in Section 4 has a
positive integer specialisation.  The inverted scalars of `A_t` are `y` and `g`
only, both with the banked nonzero norms; `g ~ 3d+2(t+1)`,
`Res_y(H_t,g) = 12q^2(t+1)(4t+1)`.

The factor `(t-2)` is a *numerator* factor of `phi_t` and of `N(alpha_t)`; it is
never inverted.  Consequently `t=2` is not a denominator exception but a genuine
degeneration of the sub-chart, handled directly in Section 5.  No
`D_terminal(t)` is declared and no generic terminal certificate was obtained;
inventing one from `t<=7` samples would be the forbidden generic-specialisation
fallacy.

Named `FALLACY-v2` items touched:

* **`sat()` wrapping.**  Not used.  Radical membership is tested by an explicit
  Rabinowitsch ideal in a declared ring, with the positive control of the direct
  unit test and the negative control of the `DIM=1` fibre.
* **Raw remainder degree.**  All normal forms are taken in the declared
  quotient `A_t = Q[y]/(H_t)`, with the split index `t=2` branched to its two
  rational fibres and never treated as a field.
* **Variable/ring map.**  Every emitted job declares its ring, generator order,
  weight vector and coefficient field; the `sympy -> Singular` map is by literal
  generator name after denominator clearing to primitive integral coefficients,
  and the map is controlled by `a5_control.py` and `c2_verify.py` re-reading the
  charged records.
* **Prime label/derivative.**  `'` denotes `d/ds = d/dh` throughout, as in the
  charged Section 2; no label is intended.
* **Floor/attainment.**  Theorem B3-AXIS is an exact identity on `S`, not a
  bound.  Corollary C1 is a sufficient condition, and Lemma CONE states the
  necessary and sufficient one; the two are kept distinct.

## 10. Verdict, sharpest partial statement, cheapest test

`(T)` on the K=16 normalised ray is **not proved for all `t`** here, and the
present route did not close it.  What is added:

1. `(8.1) <=> tau_t in sqrt(I_(t,+))` on every geometric point of `Spec A_t`,
   with `dim I_(t,+) = 0` sufficient.  This deletes band zero from the search,
   makes the decision problem homogeneous, and replaces the charged two-lemma
   split by a criterion that is also necessary.
2. The grading (2.1) on the whole spine, with the eliminated variables carrying
   the distinct weights `1,...,2t+1`, and its corollary `deg_(b3) T_(t,k) <= 3`
   with `<= 2` on the whole top tail.
3. Proposition SUBCHART, and Theorem B3-AXIS: for all `t>=2` the exact closed
   restriction (4.5)-(4.7), giving `b3 in sqrt(I_(t,+) + (b4,q))` for every
   `t>=3` with the explicit unit `phi_t`, and the exceptional index `t=2` read
   off a single factor.
4. `RESIDUAL-ZERO` is proved false at `t=2` *as a consequence of the same
   formula*, so it is not a candidate for an all-`t` induction; Lemma CONE
   supplies what should be proved instead.
5. Exact characteristic-zero evidence at `t=5` (and `t=6,7` on the `b4=0` cone),
   beyond the charged modular records.

**Sharpest partial statement.**  For every `t>=3` the `b3`-direction of the
terminal cone is uniformly killed by a proved unit; `(8.1)` is equivalent to
`tau_t in sqrt(I_(t,+))`; and the outstanding content is exactly the
`q`-directions of the `b4=0` cone,

```text
q_(j,0) in sqrt( I_(t,+) + (b4) )   for 2<=j<=t-1, uniformly in t.   (10.1)
```

**Cheapest test of (8.1) at a fixed `t`.**  One weighted-homogeneous `std` of
`I_(t,+)` in `A_t[b4,q_(2,0),...,q_(t-1,0),b3]` with `wp(1,2,...,t-1,t+1)`
followed by `dim`.  A single homogeneous computation replaces the producer's
two-chart pair, and `dim = 0` certifies `(8.1)` outright by Corollary C1.  The
mandatory negative control is the `t=2`, `y=1/5` fibre, where `dim = 1` and
`(8.1)` nevertheless holds by the `tau` criterion.  If `dim > 0`, do not report
failure: fall back to the Rabinowitsch test `1 in <I_(t,+), 1-z tau_t>`.

**Cheapest next step towards (10.1).**  Apply Proposition SUBCHART to
`R = {q_(t-1,0), b3}`, weights `t-1` and `t+1`.  Writing `w = n t + m` with
`n = a+b`, `m = b-a`, `|m| <= n`, `n = m mod 2`, the semigroup meets `[1,2t+1]`
in exactly `{t-1, t+1, 2t-2, 2t}` once `t >= 5`.  Hence for `t >= 6` the only
surviving eliminated variables are, each a single `A_t`-scalar times a single
monomial,

```text
C_(t-1)     = c1 * q_(t-1,0),        q_(t+1,0)  = c2 * b3,
q_(2t-2,0)  = c3 * q_(t-1,0)^2,      q_(2t,0)   = c4 * q_(t-1,0)*b3,
b1          = c5 * q_(t-1,0)*b3^2                                    (10.2)
```

(`b1` survives because `3t+1 = (t-1)+2(t+1)`; `T(0)` never does, and `b2` does
not once `t >= 5`).  Five scalars, one linear solve: a bounded closed-form
computation of exactly the type carried out in Section 4, which would give the
`q_(t-1,0)` direction for all `t >= 6`.  The exceptional small indices must be
branched and are already exact: `2t-2 = t+1` at `t=3`; `b2 = c*q_(t-1,0)^3`
survives at `t=4` (`2t+1 = 3(t-1)`); and `b1` acquires the extra monomial
`q_(t-1,0)^4` at `t=5` (`3t+1 = 4(t-1)`).  All three collisions are confirmed on
the charged records by `c4_subchart_check.py`.

**Typed status.**

```text
(8.1) all t                     : OPEN
Lemma CONE                      : PROVED-HERE (all t)
grading (2.1) on the spine      : PROVED-HERE (all t); mechanically checked t=2,3,4
Proposition SUBCHART            : PROVED-HERE (all t)
Theorem B3-AXIS (4.5)-(4.8)     : PROVED-HERE (all t>=2); checked on 10 records
t=2 base case                   : PROVED-HERE, derived (not sampled)
RESIDUAL-ZERO as an all-t lemma : DISPROVED at t=2
(8.1) at t=2 (both fibres)      : EXACT [1] (reproduced)
(8.1) at t=3,4                  : EXACT, via dim I_(t,+) = 0
(8.1) at t=5                    : see the status line in Sec. 8 / repro
route (1) hypergeometric        : NEGATIVE, with the Sec. 4 positive control
route (2) q-affine top tail      : DISPROVED
```

## 11. Reproduction

From `box/k16terminal-opus-20260903/`:

```text
python3 a1_homog.py 2 3 4          # GRADING_t = PASS, band weights and degrees
python3 a4_weights.py 2 3 4        # WEIGHTS_t = PASS on the charged records
python3 a2_b4zero.py 2 3 4         # b4=0 support, incl. the t=2,3 vanishing bands
python3 a3_extremes.py 2 3 4 5     # extreme coefficients with their resultants
python3 c1_b3axis.py               # derives (4.4)-(4.8); prints the (5.7a) checks
python3 c2_verify.py 2 3 4 5 6 7   # SUBCHART_FORMULA_CONTROL = PASS (10 records)
python3 c4_subchart_check.py 4 5   # SUBCHART2_t = PASS, second sub-chart
python3 tf_chart_model.py T --b4 0 # exact b4=0 chart record at t=T
python3 a5_control.py 2 3 4        # CHART_CONTROL = PASS
python3 b1_emit_dim.py 2 3 4 5     # emits the homogeneous cone dim jobs
python3 b2_emit_b4zero.py 3 4 5 6 7
python3 b3_toptail.py 2 3 4        # emits TOP-TAIL-UNIT jobs, prints deg_b3
python3 c3_t2_cone.py              # emits the t=2 Rabinowitsch + unit jobs
Singular -q <job>.sing             # for each emitted job
```

`tf_chart_model.py` is the charged `terminal_laurent_model.py` with a single
added `--b4` specialisation switch and the terminal-band assertion relaxed to
admit identically zero bands; the diff is confined to those two points and the
output path.  `tf_load.py` is the shared reader for the charged records.

Status of the long-running exact jobs at seal time is recorded in
`box/k16terminal-opus-20260903/RUN_STATUS.txt`, written after all producer
processes were stopped; any job still incomplete there is typed
`INCONCLUSIVE_TIMEOUT` and is never read as `NONUNIT`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30316`.
- Body SHA-256:
  `96e924b90cb4289336917c5857281c3d2030f79fb3c2d6b9df5556325af104ad`.
- Frozen basis: `88d6c6a9bf3fa9e4060bb56ee0dbdc27ea2e7baa`.
