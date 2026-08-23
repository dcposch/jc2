# The $H_{29}$ depth dichotomy

**Date:** 2026-08-21  
**Scope:** residue A, $B$-frozen, no-log, `PIN42`, $W_1W_2\ne0$, on the named modular charts.  
**Promoted inputs:** the corrected 30-by-30 Euler/Ore operator of
`xmodel/sol-round6.md` §1 and the filtered differential Newton theorem of
`xmodel/sol-newton-lemma.md`.  
**Purpose:** decide what the universal $H_{29}$ binding pair says as the
depth ladder is extended, and specify the first honest computation that can
distinguish flat from growing loss.

## Executive ruling

The current record proves a permanent lower bound, not an exact loss:

\[
                         \boxed{\ell(L_s^+)\ge 37}.
\]

For every fixed completed corrected operator carrying the certified binding
pair, the target $t^{36}e_{29}$ can never be repaired by adding deeper rows
or higher causal input columns. Thus the floor cannot drop. Deeper windows can
leave the finite-window floor at 37 or expose a larger obstruction; the
present operator structure does not decide between those alternatives.

In particular, the two reported values at D23 and D25 are not two depth
measurements. Both were computed with the same band-≤40,
$174\times170$ matrix in `cases/eplus_certify.py`. The D25 driver changed the
point and the Newton threshold, but called the same operator-window routine.
The first unmeasured $H_{29}$ coefficient is $H_{29}u^1$, at global level
42, exactly where the omitted x-side begins.

The cheapest genuine discriminator is therefore **D43**, whose rows have
global level $<43$. It includes level 42 and, under the unproved corrected
30-stream closure, has the nominal shape $184\times180$. D45 is a useful
immediate regression, but it adds Row 44 and no further $H_{29}$ coefficient;
its corresponding nominal shape is $194\times190$.

The conclusions are:

| question | ruling |
|---|---|
| Can extending a correctly compiled causal operator break the level-36 pair and lower the floor? | **No.** Projection proves persistence. |
| Is the exact all-depth loss proved to equal 37? | **No.** That requires an all-depth causal right section of loss 37. |
| Does the level-36 pair force analogous pairs at levels $42,48,\ldots$? | **No current theorem.** Euler/Ore coefficients change with the coefficient index, and level 42 also introduces the x-side. |
| Did D23 versus D25 measure flatness in depth? | **No.** Both used `RMAX = 40`. |
| Can the finite pivot compiler plausibly reach D75? | **CONJECTURE (engineering): yes, pointwise.** It does not by itself prove the all-depth section or the universal bridge/filter gates. |
| Would a growing floor kill formal existence? | Only under **CONJECTURE FORMAL-REGULARITY-30**. Unconditionally it rules out finite-loss germs, not singular formal germs. |

There is also a quantifier correction. The prompt adopts a universal
residue-A survivor-locus premise. The banked repository artifact itself is
weaker: 8.S9 covers 36 named D23 completions, and 9.S3 covers 360 named D25
completions. `SHEET6-DIRECTIONB.md` §§8.S9 and 9.S3 explicitly say that the
floor is completion-dependent and that sampling does not prove a locus-wide
claim. Accordingly:

> **CONJECTURE LOCUS-UNIVERSAL-H29.** On every relevant D23/D25 survivor and
> every legal completion in the claimed residue-A scope, the same projected
> target $t^{36}e_{29}$ is outside the corrected derivative image.

All locus-wide statements below consume that strengthened premise. The
pointwise persistence theorem does not need it.

The artifact chain is internally consistent: 8.S7 constructs and replays the
corrected low Euler window; 8.S9 applies the promoted literal-$n=0$ loss
definition and upgrades the same target to the bound 37; 9.S3 reruns that gate
on the D25 cells; and `cases/d25_eplus.json` records
`ell_lb_certified_distribution = {"37": 360}` while keeping
`e_plus_certified_all_points = null`. The last field is load-bearing: 37 is a
certified floor, not a certified right-section loss.

## 1. Objects and three different meanings of “the floor”

Put $u=t^6$. The corrected source and target are

\[
 X=\bigoplus_{q=1}^{30}t^{r_q}k[[u]],\qquad
 Y^+=\bigoplus_{a=0}^{29}t^{s_a}k[[u]]e_a,
 \qquad s_{29}=36,
\]

with the shifts and stream order fixed in
`xmodel/sol-newton-lemma.md` (1.0)--(1.4). At a legal full completion $s$,
the corrected derivative is the causal Euler/Ore operator

\[
 L_s^+=D\mathcal H_s:X\longrightarrow Y^+.
\]

Its actual delayed loss is the all-depth invariant

\[
 \ell(L)=\min\{e\ge0:F^{n+e}Y^+\subseteq L(F^nX)
                         \text{ for every }n\ge0\},                 \tag{1.1}
\]

with value $\infty$ when no such $e$ exists. For a fixed $L$, this is
not a function of the residual depth D.

Three quantities must not be conflated:

1. $\ell(L_s^+)$: the exact all-depth loss at one completed point.
2. $\underline\ell_B(L_s^+)$: the strongest lower bound witnessed in the
   finite projection through global band $B$. The current artifact gives
   $\underline\ell_{40}=37$.
3. For a nonempty depth-D survivor class $\mathcal C_D$ of legal full
   completions,
   \[
        \lambda(D)=\inf_{s\in\mathcal C_D}\ell(L_s^+).              \tag{1.2}
   \]
   This is the genuine survivor-locus loss floor. It has not been computed by
   the current samples.

If the survivor/completion classes are defined compatibly, then
$\mathcal C_{D'}\subseteq\mathcal C_D$ for $D'>D$, so $\lambda(D)$ is
nondecreasing whenever the classes are nonempty. This elementary nesting
argument is another reason a genuine locus floor cannot fall. It does not
upgrade sampled named completions to $\mathcal C_D$.

## 2. Persistence theorem: later rows cannot break the pair

### Proposition 2.1 (heredity of a causal finite obstruction)

Let $L:X\to Y^+$ be a causal filtered linear map. Let
$q_B:Y^+\to Y^+/F^{B+1}Y^+$ be projection through global band $B$, and let
$L_B$ be the induced finite map. If a target $y\in Y^+$ of level at most
$B$ obeys

\[
                       q_B(y)\notin\operatorname{im}L_B,             \tag{2.1}
\]

then:

1. $y\notin L(X)$;
2. $q_{B'}(y)\notin\operatorname{im}L_{B'}$ for every $B'\ge B$; and
3. if $y\in F^eY^+$, then the loss inclusion (1.1) fails at $n=0$ for
   that $e$.

#### Proof

Causality gives $q_BL(F^{B+1}X)=0$, so $L_B$ is well defined. If
$y=Lx$, then projecting would put $q_B(y)$ in $\operatorname{im}L_B$,
contrary to (2.1). Likewise, membership in any deeper finite image would
project to forbidden membership at band $B$. Finally, (1.1) at $n=0$
requires every element of $F^eY^+$, including $y$, to lie in $L(X)$.
$\square$

Apply the proposition with

\[
                  B=40,\qquad y_0=t^{36}e_{29}.                      \tag{2.2}
\]

The exact augmented-rank certificate of `xmodel/sol-round6.md` §1.2 and
`xmodel/sol-newton-lemma.md` §8 says that $q_{40}(y_0)$ is outside the
image. Since $y_0\in F^eY^+$ for every $e\le36$, every such $e$ fails at
$n=0$. Hence

\[
                            \ell(L_s^+)\ge37.                         \tag{2.3}
\]

This proves the precise depth behavior of the existing pair:

- adding output rows cannot turn a missing old target into an image target;
- new source columns of level $>40$ project to zero and cannot repair it;
- the $t^{42+}$ x-side cannot alter the already certified band-≤40
  projection; and
- newly discovered surplus output streams can only add obligations.

The only ways an apparent drop can occur are outside the proposition: one
changes to a different completed point whose low operator does not carry the
pair, or discovers that the old source registry omitted an input direction of
level at most 40. The prompt's universal-pair premise excludes the first.
Corrected source-generation and `CYCLIC-30`/surplus-`BRIDGE-30` must exclude
the second.

Thus the analytical trichotomy requested in the question collapses to a
dichotomy:

\[
       \boxed{\text{drop impossible; exact flatness or reinforcement remain.}}
\]

### Corollary 2.2 (what “universal floor” would mean)

Assume **CONJECTURE LOCUS-UNIVERSAL-H29** and compatible survivor classes.
Then every nonempty $\mathcal C_D$ past the certified stage satisfies

\[
                         \lambda(D)\ge37,
\]

and $\lambda(D)$ is nondecreasing. Equality $\lambda(D)=37$ still needs
an upper bound: at least one loss-37 operator in each class for an infimum
statement, or a uniform loss-37 section for a pointwise locus statement.
The binding pair supplies neither.

## 3. Why the operator does not yet choose flat or growth

### 3.1 D23 and D25 used the same window

`cases/eplus_certify.py` fixes

```text
RMAX = 40
window shape = 174 outputs x 170 inputs
```

and `gate_param30(E, p, D)` uses `D` only to compute the threshold
$\lfloor(D-1)/2\rfloor$. `cases/d25_eplus.py` reconstructs a D25 point and
then calls that same gate. It does not append the $H_{29}u^1$ row.

Consequently, the two distributions `{37: ...}` mean:

- the same low obstruction survived a broad change of sampled point and the
  D25 frontier completion; and
- no sampled D25 point acquired a section small enough for D25.

They do **not** mean $\ell(23)=\ell(25)=37$, do not give an upper bound 37,
and do not estimate a depth derivative.

### 3.2 The level-36 cokernel relation does not shift automatically

In Ore normal form the entries have the structure

\[
 L_{aq}=\sum_{m\ge0}u^m(A_{aqm}+B_{aqm}\Theta),
 \qquad \Theta u=u(\Theta+1),                               \tag{3.1}
\]

as recorded in `xmodel/sol-round5.md` §1.3. On an input coefficient $u^j$,
the diagonal factor is $A_{aqm}+jB_{aqm}$. Equivalently,

\[
 L(uZ)=u\sum_{m\ge0}u^m\bigl((A_m+B_m)+B_m\Theta\bigr)Z,   \tag{3.2}
\]

not $uL(Z)$. A left-cokernel relation at coefficient index $j=0$ is
therefore not automatically a relation at $j=1$. At $j=1$, the matrix
coefficients change, prior coefficient columns can feed forward, and the
normalized x-side begins.

This gives the exact current ruling:

> **CONJECTURE FLAT-H29.** After the level-36 transient, the corrected
> all-depth operator has a causal right section of loss 37, so no deeper
> target raises the floor.

> **CONJECTURE SHIFTED-H29-BINDING.** The missing target extends to a proved
> sequence of cokernel targets $y_j=t^{36+6j}e_{29}$, or to another
> cofinal obstruction sequence of comparable level.

Neither conjecture follows from (3.1). The first new coefficient is the
decisive one:

\[
                       y_1=t^{42}e_{29}.                            \tag{3.3}
\]

If every $y_j$ in a depth window were certified missing, then for $D\ge37$
the window would give

\[
 f(D)=37+6\left\lfloor\frac{D-37}{6}\right\rfloor.          \tag{3.4}
\]

Indeed, the largest included $H_{29}$ level is
$36+6\lfloor(D-37)/6\rfloor$, and the $n=0$ loss bound is one larger.
Here $f(D)\ge D-5$, so $2f(D)+1>D$ throughout this range. For a fixed
all-depth operator, missing all $y_j$ would in fact give $\ell(L)=\infty$.
Equation (3.4) is a conditional consequence, not a current certificate.

## 4. Cheapest discriminator: compile D43, then emit D45 as a regression

Depth means that selected output levels satisfy `level < D`. Since (3.3) has
level 42, D43 is minimal; D42 does not contain it. Conditional on the current
30 source shifts and 30 selected target shifts remaining complete after the
x-side is compiled, the shifted-coordinate counts are

\[
\begin{aligned}
N_Y(D)&=\sum_a\max\!\left(0,
 \left\lfloor\frac{D-1-s_a}{6}\right\rfloor+1\right),\\
N_X(D)&=\sum_q\max\!\left(0,
 \left\lfloor\frac{D-1-r_q}{6}\right\rfloor+1\right).
\end{aligned}                                                   \tag{4.1}
\]

They give:

| depth | band cap | selected target coordinates | registered source coordinates | $H_{29}$ coefficients present | provisional maximum y-side tail level |
|---:|---:|---:|---:|---|---:|
| 43 | 42 | 184 | 180 | $u^0,u^1$ at 36, 42 | 74 |
| 45 | 44 | 194 | 190 | $u^0,u^1$ at 36, 42 | 76 |
| 75 | 74 | 344 | 340 | $u^0,\ldots,u^6$ at 36 through 72 | 106 |

The dimensions in the middle columns are exact arithmetic for that conditional
30-stream model. The last column extrapolates the first-occurrence law in
`xmodel/sol-algkill.md` §3: ordinary tails occur at Row $k+27$, and the six
even tails at Row $k+32$. That law is proved only for even $12\le k<42$;
the cited source explicitly forbids extrapolating it through the unbuilt
x-side. Thus 75, 77, and 107 are provisional exclusive y-side caps, not proved
caps for the full post-41 compiler.

### 4.1 Exact commission for the compiler agent

The compiler is not allowed to obtain D43 by passing `--depth 43` to
`cases/eplus_certify.py`; that would still use `RMAX = 40`. It must build a
new post-41 source model and satisfy the following contract.

#### A. Locked scope and inputs

Use this pilot tuple:

```text
depth                 43
band_max              42
provisional_y_cap      75
actual_source_cap      FROM_XSIDE_CONSUMPTION_MANIFEST
prime                 105337
fiber                 a00pp
cell                   one named D25 fourth-root cell
base scheme            promoted D25 triangular A^14 presentation
completion_scope       adjoin all formerly unspecified completion coordinates
```

Then replay at $p=105673$. This commission prolongs the D25 $A^{14}$ cell,
not a frozen all-depth D25 zero completion. The chosen D43 point must agree on
every coordinate represented by the D25 cell, while formerly unspecified
completion coordinates are adjoined and solved. They may change the old
band-≤40 derivative: the current evaluator already lets relative-level
21/23 completion data (absolute levels 53/55) feed such gradient entries.
Thus a D25 finite point is not a frozen full operator. A failure to prolong
one cell is not family emptiness.

Before using the 36-to-1 fiber transport of `xmodel/sol-pcc-orbits.md` §6,
bank **CONJECTURE FUTURE-EMISSION-FIDELITY** at the new rows: weight registry,
row-character covariance, every pin and chart denominator, and both ideal
inclusions for every Schur/pivot replacement. The finite-depth equivariance
theorem transports a faithful presentation; it does not certify a new
compiler.

#### B. Regression before extension

The generalized builder must first reproduce the D25 prefix exactly:

1. the Row-24 90-entry symbol digest
   `ab5ee038b118ba6d0b6303c6b2b55b110dc9872c203e1c6b2d60044458e69d29`;
2. its nine selected eta components and rank-four Schur block;
3. the two registered D25 emitted shapes and hashes;
4. every pristine D25 row after reconstruction; and
5. at the separately named banked D25 zero-completion regression points, the
   restriction of the derivative to bands ≤40, byte-for-byte equal to the
   banked $174\times170$ operator.

Any mismatch is a compiler failure, not evidence about depth behavior.

#### C. Build the real x-side

Rows through 41 are the banked pure-y range. Row 42 is the first range in
which the normalized x-side factors contribute. Implement the actual full
products, schematically

\[
             \Phi_{\rm full}=X_f(t)\Phi_y,\qquad
             \Gamma_{\rm full}=X_g(t)\Gamma_y,                \tag{4.2}
\]

from the LR2/polynomial coefficient data, and differentiate those formulas by
two independent paths. `SHEET6-R1.md` §16.5 is only a future-build
specification; it is not an implementation that may be cited as this gate.

Evaluation of (4.2) is not enough. The same section identifies the LR2/R2
x-side h-Newton budget as a prerequisite. The compiler must therefore:

1. construct the legal x-side source scheme through the actual consumption
   cap, including the lead pin, gauges, dead stretch, and every new x-side
   variable;
2. emit the full finite-range R2/h-Newton budget equations and merge them with
   the y-side survivor equations before any rank-chart decision;
3. include every new variable and relation in the Fitting/Schur census; and
4. replay every R2 row exactly at the final point.

> **CONJECTURE X-SIDE-DERIVATION.** The LR2 data uniquely derives every x-side
> value consumed here and the R2 equations add no independent survivor
> condition. The compiler may omit R2 rows only after proving this statement
> by explicit two-sided identities; it may not infer it from a numerical
> assignment.

The compiler must classify every coefficient consumed through band 42 as:

- held-fixed radical/chart data;
- a function of one of the 30 registered source streams; or
- a genuinely new tangent direction.

> **CONJECTURE X-SIDE-30.** The level-42 x-side introduces no independent
> source direction and no pristine output stream outside the corrected
> 30-by-30 model that is not covered by the surplus bridge.

> **CONJECTURE POST41-FIRST-OCCURRENCE.** After the x-side is included, the
> ten-variable first-occurrence law and the provisional `D + 32` y-tail cap
> continue through the requested depth, with no additional base-completion
> coefficient outside the emitted consumption manifest.

> **CONJECTURE POST41-GRADING.** In the full x-side-corrected pristine system,
> every post-41 odd row vanishes identically, or is discharged by an explicit
> surplus-bridge identity. The pure-y grading proof alone does not establish
> this.

If the third class is nonempty, or a new independent output appears, stop and
rederive the operator. Do not freeze the direction, zero-fill it, or report a
30-by-30 loss.

Although the first x-side elementary-symmetric coefficient occurs at level
42, its product with later y coefficients contributes at every later band.
The manifest must therefore record the consumed coefficient range rather than
assuming that “one x-side term” means “one affected row.”

#### C0. Cheapest operator-only smoke test

Before solving any new nonlinear row, keep one banked D25 zero completion
fixed, add the real level-42 x-side, and extend only its derivative window to
the nominal $184\times180$ shape. Testing $y_1$ there is cheaper than
constructing a D43 survivor and immediately discriminates pointwise between
the first shifted obstruction and coverage. It does **not** measure the D43
survivor-locus floor: that completion need not satisfy Rows 26--42. Report it
as `D25_COMPLETION_BAND42`, never as a third-depth survivor result.

#### D. Compile the D43 survivor scheme

Starting from the D25 cell, append exactly the even pristine row blocks

```text
26, 28, 30, 32, 34, 36, 38, 40, 42
```

and assert that the intervening odd rows only through Row 41 vanish by the
proved pure-y grading law. D43 contains no post-x-side odd row. Retain all
pristine eta components, including any component
$a\ge30$, as an audited surplus sidecar. Do not assume `CYCLIC-30` merely
because the old band-41 regression passed.

Under the provisional append-only 30-stream census, these nine rungs introduce
90 first-occurrence tail coordinates and 89 selected scalar equations: Row 30
has nine selected components and the other eight rungs have ten. The resulting
raw hybrid estimate is 118 variables/123 rows when appended to the D25
28-variable/34-row presentation, before completion coordinates outside that
census, LR2/R2 variables and rows, x-side-independent variables, surplus
rows, or rank-chart splits.
These are conjectural acceptance diagnostics conditional on `CYCLIC-30` (or
the surplus bridge), **CONJECTURE X-SIDE-30**, and
**CONJECTURE POST41-FIRST-OCCURRENCE**; a mismatch must enlarge the model.

At each rung $k$:

1. census every first-occurrence tail by family, residue, absolute level, and
   weight;
2. emit the pristine affine frontier $F_k=A_ky_k+b_k$ over the current
   quotient;
3. compute all ranks by Fitting ideals/minors, not by assuming the D25
   rank-four pattern persists;
4. split every rank chart whose pivot is not a unit on the whole current
   chart;
5. pivot only on field units for a named point or named Laurent/chart units
   for a family certificate;
6. retain RREFs, pivot-unit proofs, inverse formulas, left-kernel compatibility
   rows, and both ideal inclusions;
7. substitute through a straight-line reconstruction DAG, never through
   recursively expanded polynomials; and
8. replay every pristine row and every saturation/inverse row after reverse
   reconstruction.

The output is either a compatible point on a named rank chart or a certified
EMPTY result for that chart. Locus-wide EMPTY requires exhausting all cells
and rank charts. Locus-wide loss requires symbolic stratification of all
survivors and all completion parameters.

#### E. Compatible point and residual certificate

A NONEMPTY artifact must contain:

- the exact map `s43 -> s25`, with equality on every represented D25 cell
  coordinate and a separate list of newly adjoined completion coordinates;
- every registered y-side source coefficient through at least absolute level
  74, plus every further coefficient named by the x-side consumption manifest;
- the x-side values and their provenance;
- radical, chart, pin, selector, and cell identifiers;
- the reconstruction DAG and every pivot unit;
- exact zero evaluation of all 184 selected pristine coefficients and all
  chart/pin rows;
- exact zero evaluation of every retained surplus pristine coefficient/row;
- exact zero evaluation of every emitted LR2/R2 x-side budget row; and
- a coefficient-consumption manifest proving that unspecified higher values
  cannot affect this finite residual or derivative window.

Use a deterministic finite-support completion only after the full formula has
been evaluated at it. “Missing from the builder” is not the value zero.

#### F. Corrected D43 derivative

Differentiate at the same point/completion used by the residual certificate.
Under the conditional 30-stream closure, select every output coordinate of
global level at most 42 and every registered input coordinate of global level
at most 42. The nominal result is

\[
                         M_{43}\in k^{184\times180}.            \tag{4.3}
\]

Hard gates are:

1. the source/output census either proves the nominal shape or stops to
   rederive a larger operator;
2. x-side contributions vanish below their proved first level;
3. direct symbolic differentiation equals an independent dual-number or
   automatic-differentiation path;
4. every nonzero entry obeys global-level causality; and
5. the old $y_0=t^{36}e_{29}$ nonmembership is recomputed and certified at
   this actual D43 completion.

Do not demand byte equality between this low projection and a banked D25
zero-completion operator. Newly activated completion coefficients can change
band-≤40 derivative entries even though the represented D25 cell coordinates
agree. Byte equality belongs only to the separate regression in part B.

#### G. Dual cokernel certificate and literal loss scan

For every target that realizes the scanner maximum, emit an exact sparse left
cokernel witness, not only two ranks. For (3.3), normalize it as

\[
                \lambda^TM_{43}=0,\qquad \lambda^Ty_1=1.       \tag{4.4}
\]

The certificate record should contain at least:

```json
{
  "n_eval": 0,
  "target": ["H29", 1],
  "target_level": 42,
  "eligible_column_rule": "global level >= n_eval",
  "lambda_sparse": "exact indexed coefficients",
  "lambda_times_matrix": "zero",
  "lambda_at_target": 1,
  "implied_loss_floor": 43
}
```

Retain an analogous normalized witness for $H_{29}u^0$. Run every relevant
$n$ in the band-42 projection according to (1.1), yielding only a
finite-window lower bound; record the maximizing target itself and bank hashes
of the ordered row/column registries and matrix.

The exact verdict language is:

| D43 result | certified conclusion |
|---|---|
| $y_1$ is outside the image | At this named completion, $\ell(L_s^+)\ge43$; the $H_{29}$ floor grew at its first opportunity. |
| $y_1$ is covered, but another level-42 target is missing | The floor grew to at least 43, but not by the proposed shifted-$H_{29}$ mechanism. |
| every new target is covered and the maximum remains $y_0$ | No growth is seen through band 42; only $\ell\ge37$ is proved. This is not $\ell=37$. |
| the named D25 cell has no D43 prolongation | That cell/rank chart dies. It says nothing about other cells until they are exhausted. |
| every scoped D43 chart is certified EMPTY | Formal existence in that exact scoped tower is killed at finite depth; no loss argument is needed. |

The pilot should run at $p=105337$, then replay at $p=105673$. Negative
controls must target recorded incidences: perturb a point coordinate having a
named nonzero coefficient in a replay row, an x-side coefficient having a
named nonzero incidence in $M_{43}$, and a matrix entry hit nontrivially by a
stored dual vector. Require the corresponding residual, differentiation, or
dual-identity check to fail. An arbitrary free coordinate need not do so.

Suggested new interfaces, naming proposed artifacts rather than existing
files, are:

```text
python3 cases/depth_point_compile.py --depth 43 --prime 105337 \
  --fiber a00pp --cell 0 --out cases/d43_point_p105337.json

python3 cases/depth_point_replay.py cases/d43_point_p105337.json \
  --all-pristine --negative-controls

python3 cases/eplus_deep.py --depth 43 --band-max 42 \
  --point cases/d43_point_p105337.json --emit-dual \
  --out cases/d43_eplus_p105337.json
```

#### H. D45 follow-on

Once D43 works, D45 is nearly free under the same conjectural census: emit and
audit **both Rows 43 and 44**, raise the provisional y-side cap from 75 to 77,
and form the nominal $194\times190$ selected derivative. Row 43 may be
suppressed only after **CONJECTURE POST41-GRADING** is proved at that range.
Conditional on that vanishing, the append-only estimate adds ten tails and
ten selected equations, giving a provisional raw hybrid size of 128
variables/133 rows. The actual cap and size come from the x-side manifest.
D45 tests whether the new rows kill the chosen D43 branch or create a
different obstruction, but it does not expose $H_{29}u^2$; that target is at
level 48 and first appears at D49.

## 5. Flat branch: the exact D75 germ-certification plan

“Flat” must mean more than seeing 37 again in a finite matrix. At one proposed
live completion $s$, the branch must prove both

\[
 \ell(L_s^+)\ge37\quad\text{and}\quad
 F^{n+37}Y^+\subseteq L_s^+(F^nX)\quad(n\ge0).              \tag{5.1}
\]

The first half is already supplied by the binding pair. The second is an
all-depth right-section theorem. Together they prove the exact value
$\ell(L_s^+)=37$.

D75 is the first depth-only Newton threshold because

\[
                              2\cdot37+1=75.                 \tag{5.2}
\]

### 5.1 What must be compiled

#### Finite-depth geometry

1. Starting from a promoted D25 $A^{14}$ cell, compile the pure-y even rows
   26--40 and replay the proved odd-row identities through 41. Then emit and
   audit **every** full x-side row 42--74, including odd rows, with all surplus
   eta components retained. Suppress a post-41 odd row only after proving
   **CONJECTURE POST41-GRADING** (or the precise needed finite-range instance).
2. Provisionally extend the y-side registry through absolute level 106
   (`y_side_cap_exclusive = 107`): under the extrapolated law, Row 74 first
   sees ordinary tails at 101 and the six even tails at 106. The x-side
   consumption manifest must prove or enlarge this cap.
3. Extend the legal LR2/R2 x-side source scheme and h-Newton budget through
   the actual consumption cap, merging and replaying every new relation as in
   §4.C.
4. Use the sequential Fitting/Schur/Laurent-pivot protocol of §4, retaining all
   rank charts and a reversible DAG.
5. Produce a genuine compatible depth-75 point and prove
   $\mathcal H(s)\in F^{75}Y^+$ by pristine replay. Equivalently, its
   actual residual order $\nu$ must satisfy $\nu\ge75$.
6. Name a legal full completion used for both residual and derivative. A
   finite-support completion is acceptable if every future source value is
   explicitly set and the actual all-depth formulas, including x-side
   normalization, are evaluated at that completion.

Under the provisional append-only 30-stream grading, D25-to-D75 adds 25 even
rungs, 250 first-occurrence tail coordinates, and 249 selected equations. The
corresponding raw hybrid estimate is 278 variables/283 rows when appended to
the D25 28-variable/34-row presentation, before additional completion
coordinates, LR2/R2 variables and rows, extra x-side directions, surplus rows,
or rank-chart duplication.
This estimate is conditional on `CYCLIC-30`/the surplus bridge,
**CONJECTURE X-SIDE-30**, **CONJECTURE POST41-FIRST-OCCURRENCE**, and the
vanishing/discharge of every post-41 odd row under
**CONJECTURE POST41-GRADING**.

#### Finite derivative audit

Conditional on the same 30-stream closure, compile the exact same-completion
selected derivative through band 74:

\[
                         M_{75}\in k^{344\times340}.          \tag{5.3}
\]

Replay every lower projection, both differentiation paths, causality, and all
dual lower-bound witnesses. This matrix is a necessary regression and a good
discovery object. It is not an all-depth PARAM certificate.

#### All-depth application gates

The final certificate must additionally prove:

1. **CONJECTURE CYCLIC-30**, or the surplus part of
   **CONJECTURE BRIDGE-30**, as a universal all-depth identity on the Newton
   ball;
2. the universal two-sided levelwise pristine/selected identities of
   **CONJECTURE BRIDGE-30**, including the emitted pivot presentation;
3. **CONJECTURE FILTER-30** for the actual normalized x-side and every chart
   inverse, with nonlinear filtration loss $\sigma=0$; and
4. **CONJECTURE PARAM-30** at the named completion: an exact causal map
   \[
       S:F^{37}Y^+\longrightarrow X,\qquad L_s^+S=I,
       \qquad S(F^{n+37}Y^+)\subseteq F^nX                 \tag{5.4}
   \]
   for every $n\ge0$.

For a machine proof, (5.4) must be represented by an exact Ore identity or a
finite-state recurrence. It must contain:

- a proved initial transient;
- recurrence state and solve rules for arbitrary coefficient index $j$;
- a maximum global delay of 37;
- boundary identities between transient and recurrence;
- complete characteristic-$p$ resonance closure; and
- an exact replay of $L_s^+S=I$, not a long finite rank profile.

A compact resonance certificate may use polynomial pivot covers together
with a Bézout identity modulo $j^p-j$, thereby proving coverage of every
residue class in $j$. This is only a proposed certificate format; whether
the present operator admits such a cover is part of **CONJECTURE PARAM-30**.
The example $\Theta+1$ in `xmodel/sol-newton-lemma.md` (4.5) shows why a
finite D75 matrix cannot substitute for this step.

Finally verify the sharp arithmetic gate

\[
                             \nu-2e\ge1.                     \tag{5.5}
\]

At the boundary $(\nu,e)=(75,37)$, it is exactly $75-74=1$.

### 5.2 What the completed certificate would prove

By `xmodel/sol-newton-lemma.md` Theorem 6.1, the certificate would prove one
allowed formal solution on the named residue-A chart over the same modular
coefficient field. With $D=75,e=37$, the produced solution lies in

\[
                             s+F^{38}X.                       \tag{5.6}
\]

It therefore agrees with the supplied point only below depth 38, not through
the full D75 jet.

It would **not** prove:

- that every D75 point or every $A^{14}$ cell lifts;
- a formal solution on another chart, with unfrozen $B$, or without the
  named pins;
- a characteristic-zero lift;
- convergence or algebraicity of the formal series; or
- a polynomial Keller pair or a Jacobian-conjecture counterexample.

### 5.3 Can the pivot-certificate method reach D75?

Everything in this subsection that estimates runtime, memory, or tractability
is **CONJECTURE (engineering)**.

Conditional on `CYCLIC-30`/the surplus bridge,
**CONJECTURE X-SIDE-30**, **CONJECTURE X-SIDE-DERIVATION** (or a comparably
small explicit R2 scheme), and no new surplus directions, the finite answer is
plausibly yes. The provisional $344\times340$ matrix has 116,960 dense slots,
so modular elimination and dual-witness extraction are a seconds-to-minutes
task. The nonlinear prolongation has only 25 new affine frontiers if the
post-41 first-occurrence structure persists. The existing D25 certificate
demonstrates that a reversible pivot DAG can be tiny even when a monolithic
Gröbner presentation is not.

> **CONJECTURE (engineering estimate).** After a correct x-side model exists,
> a one-cell D43 compiler is hours-scale, and a one-representative pointwise
> D75 prolongation is hours to a few days, with a certificate measured in tens
> of megabytes rather than an expanded all-family Gröbner object. Rank-chart
> proliferation is the principal variance. A naively expanded 36-fiber D75
> compiler should not be attempted first.

This estimate covers a finite point and its finite derivative. The pivot
method does not automatically produce `CYCLIC-30`, `BRIDGE-30`, `FILTER-30`,
or the all-depth Ore section. Those are research theorems, and `PARAM-30` may
be harder than reaching D75 geometrically. The immediate blocker is the
unimplemented x-side, not matrix size.

## 6. Growth branch and the exact boundary of a kill theorem

### 6.1 What a growing universal floor proves unconditionally

Fix one coefficient field $k$. Let $\mathcal Z_\infty(k)$ be the allowed
formal zeros of the pristine scoped residue-A system over $k$. For each
ladder depth $D$, let $\mathcal C_D(k)$ contain every legal all-depth
completion over $k$ of every depth-D survivor in that same scope. Assume:

1. a certified locus/all-completion floor
   \[
       \ell(L_s^+)\ge f(D)\qquad(s\in\mathcal C_D(k));        \tag{6.1}
   \]
2. $2f(D)+1>D$ on an unbounded cofinal depth ladder; and
3. every $z\in\mathcal Z_\infty(k)$, viewed as its own full completion,
   belongs to $\mathcal C_D(k)$ through its D-jet for every ladder depth.

The third item is the root-to-selected-system half of the universal
`CYCLIC-30`/`BRIDGE-30` scope, not a consequence of sampling. The conclusions
below are over this fixed $k$. To kill roots over $\overline{\mathbf F}_p$ or
arbitrary coefficient-field extensions, (6.1) and the scope/bridge statements
must remain valid after every relevant base extension.

### Theorem 6.1 (growth forces formal singularity)

Under assumptions 1--3, every allowed formal zero has infinite delayed loss:

\[
                  z\in\mathcal Z_\infty(k)
                  \quad\Longrightarrow\quad
                  \ell(L_z^+)=\infty.                         \tag{6.2}
\]

#### Proof

Suppose instead that $e=\ell(L_z^+)<\infty$. Choose a ladder depth
$D\ge2e+1$. Since the exact completion $z$ belongs to $\mathcal C_D(k)$,

\[
                         e\ge f(D).                            \tag{6.3}
\]

But $2f(D)+1>D\ge2e+1$, so $f(D)>e$, contradicting (6.3).
$\square$

Thus a growing universal floor proves:

- no finite-loss, linearly regular formal germ exists in the scoped tower;
- no finite-loss Newton certificate exists when a root's truncation is
  completed by that exact root, and no completion can certify using only the
  guaranteed depth $D$; and
- if formal roots exist, all of them lie on an infinitely singular track.

The inequality at one advertised depth does not exclude a different
completion whose actual residual order is $\nu\gg D$, because the sharp gate
is $\nu>2e$. Such a point must be tested at its actual deeper residual depth
against the corresponding universal floor. The theorem does not yet prove
$\mathcal Z_\infty(k)=\varnothing$.

Pointwise **CONJECTURE SHIFTED-H29-BINDING** makes the loss infinite only for
the fixed operator on which all targets are missed. To obtain (6.1), add the
locus quantifier:

> **CONJECTURE LOCUS-SHIFTED-H29.** For every $D$, every
> $s\in\mathcal C_D(k)$, and every $j\ge1$ with $36+6j<D$, the target
> $t^{36+6j}e_{29}$ is outside the image of $L_s^+$.

Together with **CONJECTURE LOCUS-UNIVERSAL-H29**, this supplies the concrete
$f(D)$ in (3.4). At any fixed formal root it also directly makes the
derivative loss infinite. This remains compatible with a singular root.

### 6.2 Conditional KILL THEOREM

The missing converse-side statement must be isolated rather than attributed
to Newton:

> **CONJECTURE FORMAL-REGULARITY-30.** Every allowed formal zero $z$ of the
> scoped pristine residue-A system has finite delayed derivative loss
> $\ell(L_z^+)<\infty$.

This is stronger than necessary. The weakest sufficient converse is:

> **CONJECTURE EXISTENCE-REGULARITY-30.** If
> $\mathcal Z_\infty(k)\ne\varnothing$, then it contains at least one
> finite-loss root.

### Theorem 6.2 (conditional H29 kill)

Assume the three hypotheses of Theorem 6.1 and
**CONJECTURE FORMAL-REGULARITY-30**. Then

\[
                              \mathcal Z_\infty(k)=\varnothing. \tag{6.4}
\]

#### Proof

Theorem 6.1 says every member of $\mathcal Z_\infty(k)$ has infinite loss;
formal regularity says every member has finite loss. Hence there is no
member. $\square$

The identical conclusion follows if **CONJECTURE FORMAL-REGULARITY-30** is
replaced by the weaker **CONJECTURE EXISTENCE-REGULARITY-30**: a nonempty
root set would contain one finite-loss root, contradicting Theorem 6.1.

No uniform upper bound on the losses is needed. Pointwise finiteness is
enough, because the cofinal ladder can be chosen beyond $2e+1$ separately
for each hypothetical root.

This regularity hypothesis is a genuine gap and is false for general
filtered Euler equations. In characteristic $p$,

\[
                         \mathcal H(x)=(\Theta+1)x             \tag{6.5}
\]

has the exact formal root $x=0$, while its derivative misses
$u^{p-1},u^{2p-1},\ldots$ and has infinite loss. This is the promoted
lemma's own resonance example in `xmodel/sol-newton-lemma.md` (4.5). In every
characteristic, $\mathcal H(x)=x^2$ has the exact root zero and zero
derivative, again with infinite loss. Neither existence, Noetherianity,
smoothness of the finite D25 cells, nor `PARAM-30` at one advertised point
proves **CONJECTURE FORMAL-REGULARITY-30**.

The unconditional kill remains a finite exhaustive, scheme-theoretic
inconsistency: the depth-D ideal is the unit ideal, equivalently the scoped
scheme is empty after the allowed coefficient-field extensions. Mere absence
of $k$-rational points over a non-algebraically-closed $k$ is not this claim.
`xmodel/sol-algkill.md` Proposition 3.3 explains the algebraic boundary: if
the all-orders ideal contains 1, a finite subsystem already contains 1;
asymptotic codimension or loss growth alone is not emptiness.

### 6.3 In what sense a true finite-loss root's truncation would certify

There is a rigorous mathematical statement, but it is not automatically an
effective compiler statement.

Let $z$ be a true formal root with finite loss $e=\ell(L_z^+)$. Lemma 2.1 of
`xmodel/sol-newton-lemma.md` supplies an abstract causal section of delay
$e$. Take $D=2e+1$, take the D-jet $z_D$, and use $z$ itself as the
named legal full completion. Then:

- the residual order is $\nu=\infty$;
- the exact derivative is $L_z^+$;
- the section has loss $e$; and
- $D\ge2e+1$ holds with equality.

Assuming the universal `CYCLIC-30`, `BRIDGE-30`, and `FILTER-30` identities,
Theorem 6.1 of the promoted Newton document applies. Therefore the exact
root-completed depth-$2e+1$ truncation satisfies the abstract Newton
hypotheses. Calling this a finite “certificate” would be too strong.

It is circular and non-effective as a machine artifact. Lemma 2.1 constructs
the section by infinitely many degreewise choices; the exact certificate
contract requires a finite Ore identity or finite-state recurrence.

> **CONJECTURE EFFECTIVE-PARAM-30.** Every finite-loss formal residue-A root
> in scope admits a finitely representable section certificate of the required
> Ore/recurrence form.

This conjecture is unnecessary for the logical conditional kill, but is
needed for the existence of a finite section artifact. Even it does not
promise discovery from a finite jet.

> **CONJECTURE EFFECTIVE-SEARCH-30.** A finite-loss root has a finitely
> representable legal completion and there is a terminating extraction/search
> procedure producing that completion and its `PARAM-30` artifact from finite
> residue-A data.

There is a second issue if a compiler uses a canonical or zero completion
$s_D$ rather than the exact root $z$. The following perturbation lemma is
the required bridge.

### Lemma 6.3 (stability of a delayed section under a deep derivative change)

Suppose $L_z$ has a loss-$e$ section $S$, $s_D-z\in F^qX$ with $q>e$,
and, for $K=L_{s_D}-L_z$,

\[
                         K(F^nX)\subseteq F^{n+q}Y^+
                         \quad(n\ge0).                       \tag{6.6}
\]

Then $L_{s_D}$ has a right section with loss at most $e$.

#### Proof

On $F^eY^+$, the operator $KS$ raises target filtration by $q-e>0$.
Therefore

\[
                    B=(I+KS)^{-1}=\sum_{j\ge0}(-KS)^j         \tag{6.7}
\]

converges and preserves every $F^{n+e}Y^+$. Set $S_D=SB$. Since

\[
                 L_{s_D}S=(L_z+K)S=I+KS,
\]

we have $L_{s_D}S_D=I$, and the same delay estimate follows from those for
$S$ and $B$. $\square$

> **CONJECTURE TRUNCATION-STABILITY-30.** For every finite-loss residue-A root
> $z$, and every sufficiently large $D$, the compiler produces a canonical
> completion $s_D$ of the exact D-jet $z_D$ such that
> $s_D-z\in F^DX$ and (6.6) holds with $q=D$.

`FILTER-30` should be the source of the derivative estimate, but the x-side
restricted-series audit and the exact source-depth identification are not
promoted. Under the conjecture, filtration-Lipschitzness of $\mathcal H$ and
$\mathcal H(z)=0$ also give $\mathcal H(s_D)\in F^DY^+$. Lemma 6.3 then
retains loss at most $e$; for $D\ge2e+1$, the universal application gates give
the abstract Newton hypotheses at $s_D$. This still starts from the unknown
root's abstract section; a finite artifact additionally needs
**CONJECTURE EFFECTIVE-PARAM-30**, and discovery from finite data needs
**CONJECTURE EFFECTIVE-SEARCH-30**. If the compiler proves only
$s_D-z\in F^qX$, it also needs $q\ge D$ and the corresponding
filtration-Lipschitz residual estimate. Until these statements are proved,
only the exact-root-completion argument above is rigorous.

## 7. Campaign decision rule

The next action is not another run of the band-40 scanner. It is the D43
compiler of §4.

1. If $H_{29}u^1$ has a dual cokernel witness at a compatible D43 survivor,
   the floor grows pointwise to at least 43. Repeat at D49 to test
   $H_{29}u^2$, and seek an all-index Ore/cokernel recurrence before making
   a growth theorem.
2. If $H_{29}u^1$ is covered and no other new target is missed, record only
   “flat through level 42.” Pursue the all-depth loss-37 section and the D75
   point in parallel; neither finite observation proves exact flatness.
3. If the scoped D43 scheme is exhaustively EMPTY, bank the finite-depth kill
   and stop the loss campaign for that scope.
4. If a cofinal growing floor is eventually proved, report Theorem 6.1
   unconditionally and Theorem 6.2 only with
   **CONJECTURE FORMAL-REGULARITY-30** visibly attached.

The decisive distinction is therefore not “37 at D23 versus 37 at D25.” It
is whether the corrected post-41 operator supplies a preimage or a new dual
cokernel witness for $t^{42}e_{29}$, with the real x-side present.
