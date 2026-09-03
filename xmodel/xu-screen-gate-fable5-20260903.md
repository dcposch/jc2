# Hostile gate (page images): the Xu IM >= Im skeleton screen — `XU-SCREEN-GATE-FABLE5-20260903`

**Verdict:** **`CONFIRMED (scoped)`** — promotable as
`C_FULL_TREE_POLYNOMIAL_ODE ∧ XU`, where `XU` = Xu Corollary 5.3
(Theorem 4.7(ii) + Theorem 5.1) for a Jacobian pair monic in `y`, generic `xi`.
The 29 kills are theorems about skeletons **under the operative full-tree
model**, not from Xu alone (Section 4 shows two of the hand-checked kills
vanish without the (12)/(13), Prop 5.6 and ODE-nondegeneracy constraints).
**Basis:** `9bd00a472a692aa43a5c3151f0ad8d02de3f1e53`.  No ledger edits, no
`jc2-lean`, no ideation files, no in-progress lane reports touched.
FALLACY-v2 in force: survival is never attainment.

## 0. Custody

MEASURED: the eight frozen inputs in `/tmp/jc2-lane.AQwgL6/inputs` were
verified from `xmodel/xu-screen-gate-fable5-20260903.run.v2` by generating the
manifest with `awk` over the `charged_input_<i>_basename/_sha256` lines and
running `sha256sum -c`: 8/8 `OK`, no retyped digits.

SOURCE-READ artifacts (pdftoppm, 200 dpi, all 14 pages) in
`box/xuscreen-gate-20260903/xu-pages/xu-p-NN.png`; layout text
`box/xuscreen-gate-20260903/xu-layout.txt`.  Pages named by content:
p.1 definitions (pi-root, split, final); p.2 Lemma 2.1, Prop 3.3;
p.4 Theorem 3.4, Lemma 4.1, Lemma 4.2, Definition 4.3, Lemma 4.4(i);
p.5 Lemma 4.4(ii), Cor 4.5, Definition 4.6, Theorem 4.7; p.6 proof of 4.7,
Cor 4.8; p.7 IM definition and Theorem 5.1; p.8 Cor 5.2, Im definition,
Cor 5.3, case (75,50); p.9 case (84,56), Section 7 start; p.10 Section 7.3,
Prop 7.3; p.11 proof of 7.3, Cor 7.5; p.12 proof of 7.5, Section 8;
p.13 (99,66) data and split cases.

Drivers and logs: `box/xuscreen-gate-20260903/{xu_screen_replay.py,
hand_check.py, hand_trees.py, identity_random.py, *.log, results.json}`.
`xu_screen_replay.py` is the charged driver with one edit: the frozen-input
path.

## 1. Source read against the charged transcription

SOURCE-READ (p.1): a pi-root is `sigma = sum_{j<delta} a_j t^j + pi t^delta`
with `f(sigma) = f_sigma(pi) t^lambda + ...`, `deg f_sigma > 0`; split iff
`f_sigma` has more than one root; final iff `f_sigma` has no multiple roots
and `deg > 1`.  Matches the charged report.

SOURCE-READ (p.4, Theorem 3.4): `I(f_xi, f_y) = -sum_sigma (e(f_sigma)-1)
lambda_sigma` over all splitting pi-roots of `f_xi`, `f` monic in `y`, no
Jacobian condition (p.2 says Section 3 does not need it).  Transcribed
correctly.  DERIVED: the screen never uses Theorem 3.4; `xu_screen.py`
computes only `IM` and the `Im` floor.

SOURCE-READ (p.4, Definition 4.3): major iff `ord g(alpha) < 0`, minor iff
`ord g(alpha) = 0`; two points at infinity with leading form
`(y-a_1x)^u (y-a_2x)^v`, `u < v`: all roots `a_1 t^-1 + ...` of `f_xi` are
minor and form the principal minor roots.  Lemma 4.4: major related final
root has `delta < 1`, minor has `delta > 1`.  Matches.

SOURCE-READ (p.5, Definition 4.6 and Theorem 4.7): `D_sigma^h = {alpha :
h(alpha)=0, ord(sigma-alpha)=delta_sigma}`, `P_m` / `P_M` = final minor /
final major pi-roots of `f_xi`.  Theorem 4.7, hypothesis "Let (f,g) be a
Jacobian pair" (and p.4 line "From now on, we suppose that (f,g) is a
Jacobian pair"):
(i) `I(f_xi,f_y) <= deg_y f - 1 + sum_{P_m} (|D_sigma^{f_xi}|-1)(delta_sigma-1)`;
(ii) `I(f_xi,g) >= 1 + sum_{P_m} (delta_sigma-1)`;
(iii) no final minor roots gives `I(f,f_y) = deg_y f - 1`, `I(f,g) = 1`.
Direction and hypotheses exactly as transcribed and as used.

SOURCE-READ (p.7, Theorem 5.1; p.8, Cor 5.3): `IM(f,g) = -sum_{P_M}
|D_sigma^f| lambda_sigma^g = (deg_y g)/(deg_y f + deg_y g) sum_{P_M}
|D_sigma^f|(1-delta_sigma)`; Theorem 5.1: `I(f_xi,g) = IM(f,g)` for a
Jacobian pair, citing Moh Prop 4.6 for `-lambda^g_sigma =
n(1-delta_sigma)/(n-M_1) = n(1-delta_sigma)/(m+n)` (Xu: `deg_y f = m`,
`deg_y g = n`, so the skeleton's `(n,m)` is `(deg g, deg f)`).
`Im(f,g) = 1 + sum_{P_m}(delta_sigma-1)`; **Cor 5.3: `IM >= Im`, "Let (f,g)
be a Jacobian pair"**.  This is the displayed relation the screen uses;
answer to (b): `IM >= Im` is Cor 5.3 = Thm 4.7(ii) (lower bound on
`I(f_xi,g)`) chained with Thm 5.1 (exact value of `I(f_xi,g)`); both
Jacobian-only; the relation between `I(f_xi,g)` and `I(f_xi,f_y)` enters
only inside the proof of 4.7 via `I(f_xi,f_y g) = I(f_xi,f_y) + I(f_xi,g)`
and `I(f_y,g_y) = 0`.

SOURCE-READ (pp.8-9, Section 6): printed numbers `(75,50)` split (i):
`Im = 4`, `IM = 8` ("do not work"); split (ii): `Im = 1+(4-1)+10(6/5-1) = 6`,
`IM = 5*4*1/5 = 4` (ruled out); `(84,56; M_2=64, V_2=2)`: `Im = 1 + 7(9/7-1)
+ (3-1) = 5`, `IM = 4*7*3/21 = 4` (ruled out); `(84,56; M_2=72, V_2=5)`:
`Im = 1+(2-1)+(3-1) = 4`, `IM = 4*10*3/12 = 10` (not ruled out).  Matches
the charged calibration table.

SOURCE-READ (pp.10-11): Section 7.3 hypotheses (Jacobian pair, monic in `y`,
`f` with two points at infinity, effective index `s > 2`, `T_0 = g`,
`T_1 = f`, `deg T_i = -mu_i`, `d_i = gcd(-mu_0..-mu_{i-1})`, principal minor
multiplicity `m u_s/d_s`, `u_s < v_s = d_s - u_s`) and the multiplicity list
`(-mu_0)u_s/d_s, ..., (-mu_{s-1})u_s/d_s, (-mu_s-2)u_s/d_s + 1`; Prop 7.3
(order-1 pi-root: all `T_{i,sigma_1}` powers of one linear polynomial);
Cor 7.5 (`u_s > 1`, `delta_sigma < (v_s+1)/(u_s+1)` forbids a split into
`u_s` different roots).  Matches.  DERIVED: for `(99,66)` the skeleton
`M_2 = 77 = M_1 + 66*3 - 55`, `M_3 = 97 = M_2 + 55*3 - 145` reproduces Xu's
`-mu_2 = 55`, `-mu_3 = 145` through his Section 7.1 recursion, so the
skeleton's `M_i` are Xu's M-sequence and `d_{i+1} = gcd(d_i, M_i)`.

Answer to (a): the phrase "not split before order 1" appears only in Xu's
introduction as Moh's result; Theorem 4.7 does not hypothesise it, and the
screen does not use it.  Generic `xi` is used for `f_xi` squarefree,
`g(alpha) != 0` at roots of `f_xi`, and `f_xi(beta) != 0` at roots of `f_y`
(p.3, proof of 3.3(iv)); the screen's tree is that of `f_xi`, and all floors
below depend only on the `lambda < 0` (xi-independent) levels.

## 2. Are the floors theorems?  A distance-only rederivation

DERIVED (gate, from Xu p.4 Lemma 4.1 and p.6): let `alpha_1..alpha_m` be the
roots of `f_xi` and `S(alpha) := -ord f_y(alpha) = -sum_{j != i}
ord(alpha-alpha_j)`, a function of the ultrametric root tree only.  Lemma
4.1 at `alpha` (`f(alpha) = xi` constant) gives `f_y(alpha) * d/dt g(alpha)
= J t^-2`, so: major `alpha`: `ord g(alpha) = S(alpha) - 1`; minor `alpha`:
the first non-constant exponent of `g(alpha)` is `S(alpha) - 1`.  Xu p.6
("By Proposition 3.3, ord f_y(alpha) = -delta") is exactly `delta_sigma =
S(alpha)` for the related final minor root; I re-derived its input
`lambda^f_sigma = 0` (Lemma 4.4(ii), "Now lambda^f = 0 = lambda^g") from the
chain-rule identity `d(f(sigma),g(sigma))/d(t,pi) = -J t^{delta-2}`: for
`lambda^f != 0` its leading term `lambda^f f_sigma(pi) g'_sigma(pi)
t^{lambda^f-1}` is a nonconstant polynomial in `pi` and cannot equal `-J`.
Xu's (4.4) step `ord g_y(beta) >= -delta_sigma` follows from Prop 3.3(i)
applied to `g` at `sigma` (`g_y(sigma) = g'_sigma(pi) t^{-delta}`).  Hence:

```text
IM = I(f_xi,g) = sum_{major alpha} (1 - S(alpha))                    (exact)
every final minor root:  delta_sigma = S(alpha) for alpha in D_sigma  (exact)
```

DERIVED (c): a minor child at level `j` with `N` roots and outside sum
`S_out` (sum of `-ord` to roots outside the child) satisfies, for each of
its roots, `delta_final = S_out - sum_inside >= S_out - (N-1) delta_final`,
because a final `sigma` has no `f_xi`-root beyond distance `delta_sigma`.
So `delta_final >= S_out/N` for every final minor root in the child, with
equality iff the child splits in one stage, and the child holds at least one
final minor root.  MEASURED: `S_out/N` equals the driver's floor `delta_j +
(d_j/(n-M_j))(1-delta_j)/v` on all 934 (row, level, `v <= lo`) instances of
the selected paths of the 1420 operative rows, and on 126,363 random-path
instances (`identity_random.log`), so it is an algebraic identity of Def
5.1(3), and the floor is a theorem given `lambda^f_sigma = 0`; it is not
literally stated in Xu (he prints only the instances `9/7` and `2`) and does
not rest on Moh's "not split before order 1".  Also `v <= lo` iff
`S_out/N >= 1`, consistent with Lemma 4.4.  The driver's per-orbit factor
`A_j` and per-zero factor `1` are the conjugate-disc counts; correct.

MEASURED: the driver's leaf term `|D^f_sigma| (n/(n+m))(1-delta_1)` equals
the distance value `N_1 (1 - S(alpha))` on all 1420 selected paths and on
16,898 random paths (0 mismatches), so Moh Prop 4.6 as cited by Xu is an
identity of Def 5.1(3) and needed no separate Moh page read.  DERIVED: a
multi-stage bottom split only raises `S(alpha)` (lowers `IM`), so the
single-stage leaf value is an upper bound; fail-closed.

DERIVED (principal side): the same inequality applied to the `N_p =
u_s m/d_s` principal minor roots (outside sum `V_s m/d_s`, all at distance
`-1`) gives `delta_final >= V_s/u_s` for every final principal minor root,
hence contribution `>= V_s/u_s - 1` for **all** `u_s >= 1`.  For `u_s = 1`
this is the driver's `V_s - 1` (Xu's examples assert equality with one final
root).  For `u_s > 1` the driver's floor `0` is fail-closed but not sharp:
Section 7.3 / Cor 7.5 alone give no numeric floor (they bound where and how
the principal disc may split), but the distance argument does.  MEASURED
(post-processing `results.json`, not a promoted rerun): the floor
`V_s/u_s - 1` would kill 5 more rows / 4 more groups at `D <= 200`:
`(168,112;154,161,166;V_s=5;u_s=2)`, `(180,144;162,168,178;4;2)`,
`(192,128;160,184,190;5;3)`, `(198,132;154,187,196;7;4)`; `(99,66)` still
survives (`16 >= 8/3`).  Typed `DERIVED`, not consumed here.

Singleton edge: Xu's "final" requires `deg f_sigma > 1`; a minor child with a
single root would fall outside `P_m`.  MEASURED: no operative row has
`m/d_2 = 1`, so no census child is a singleton; and the (4.3)/(4.4) argument
extends to singletons with `|D^{f_y}| = 0`, which only raises `Im`.

## 3. Fail-closed policy (d)

DERIVED: no monotonicity is needed.  The driver enumerates the finite set of
full trees embedding the row under the operative model and takes `IM_max`
over all of them and `Im_min` over all of them (children optimised
independently, sum of maxima = maximum of sums).  If an actual Jacobian pair
realises the row, its tree `T*` is in that set, so `IM(T*) <= IM_max` and
`Im(T*) >= Im_min`; `IM_max < Im_min` then contradicts Cor 5.3.  A
non-maximal embedding being the actual one cannot rescue a killed row and
says nothing about a surviving one (FALLACY-v2).  The only load-bearing
assumptions are (i) `T*` lies in the enumerated set, i.e. the operative
model (radii from Def 5.1(3) on every path, one major child per node, at
most `Q/A` orbits, (12)/(13) at the bottom, Prop 5.6, ODE nondegeneracy),
and (ii) Cor 5.3 itself.  Hence the scope `C_FULL_TREE_POLYNOMIAL_ODE ∧ XU`.

## 4. Replay and hand recomputation

MEASURED (`replay.log`, 48 s): controls 6/6 Moh rows operative; Xu
calibration 3/3 exact; 1420 rows / 686 groups; killed rows 43, killed groups
29, touched groups 37, killed groups at `D <= 120` = 4; every per-row
`(IM_max, Im_min, xu_ok)` identical to the charged `results.json`; strata,
Moh-six status and calibration payloads identical.  Killed `u_s > 1`
groups: 7, as listed in the charged report.

MEASURED (`hand_trees.log`): an independent enumerator (no `XuBounder`
import; `IM` from `sum(1-S(alpha))`, `Im` floor from `S_out/N`) gives, with
the operative constraints (`strict=True`) and without them (`strict=False`):

```text
row                                     strict IM_max  tree_min  Im_min  kill
(84,56; 64,82; V=(2,3); u_s=1)          yes   4        2         5       yes   [Xu 4<5]
                                        no    152/17   0         3       no
(144,108; 126,135,142; V=(3,7,6); u_s=3) yes  18/5     4         5       yes
                                        no    387/55   3         4       no
(64,48; 52,62; V=(3,3))                 yes   9        0         3       no
(99,66; 77,97; V=(8,8); u_s=3)          yes   16       0         1       no   [sharp floor: 8/3]
(84,56; 72,82; V=(5,3))                 yes   10       1         4       no   [Xu 10>=4]
(75,50; 55,73; V=(2,4))                 yes   8        0         4       no   [Xu (i) 8>=4; (ii) 4<6]
```

Hand values agree with the driver in every strict line.  The `strict=False`
lines show that both hand-checked kills need the operative constraints
(e.g. for `(84,56;64)` the zero-major completion `b = 7` is what the
bottom (12)/(13) and Prop 5.6 rules remove); Xu's own printed exclusion of
`(84,56;64;2)` is split-specific (`[2,1]`, `A = 7`) and coincides with the
driver's kill only because the operative model leaves that split alone.

## 5. Verdict, typed

CONFIRMED (scoped): transcription of Theorems 3.4 / 4.7 / 5.1, Cor 5.3,
Section 7.3, Prop 7.3, Cor 7.5 is correct; the comparison uses Cor 5.3 in
the right direction under its stated Jacobian hypothesis; the minor floor is
a theorem (gate-derived from Lemma 4.1 and `lambda^f_sigma = 0`, numerically
identical to the driver's formula); the leaf `IM` term is an identity of
Def 5.1(3); the max/min policy is fail-closed; the replay reproduces
43 rows / 29 groups exactly; four target rows recompute by hand.  Promote as
the necessary screen `C_FULL_TREE_POLYNOMIAL_ODE ∧ XU` with scope: Jacobian
pair, `f,g` monic in `y`, two points at infinity as in the skeleton, generic
`xi`, `XU` = arXiv:1604.07683v4 (a preprint; its Cor 5.3 was re-derived here
from Lemma 4.1 and the chain rule, but that rederivation is a gate note, not
a promoted proof).  A screen is necessary, never attainment: the 657
untouched groups, `(99,66)`, and the K=16 ray entries are not certified.

OPEN[principal-us-gt-1-floor]: bounded quantity: principal contribution
floor `0` in the promoted driver.  Cheapest sharpening: replace it by
`V_s/u_s - 1` (Section 2 derivation), rerun `xu_screen.py`, expect +5 rows /
+4 groups at `D <= 200`; requires its own gate of the distance argument.

OPEN[minor-disc-exact-Im] and OPEN[attainment-correlation] stand as in the
charged report; the same-tree optimisation of `IM - Im` is the cheapest
next test and would only strengthen kills.

No new exit-price assertion is made; no `charge_basis` line.

<!-- BODY-END -->
