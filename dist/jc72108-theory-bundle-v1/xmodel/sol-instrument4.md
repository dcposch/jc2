# Instrument round 4: decide D23 in the D21 quotient

**Date:** 2026-08-18  
**Scope:** the B-frozen, no-log residue-A D23 window, first at the banked
finite radical fiber and `p=105337`, then across the finite chart cover and
the other primes. A modular result remains a screen until it receives the
appropriate characteristic-zero certificate or lift.

## Decision

**The single best move is an exact Row_22 restriction in the D21 quotient,
combining (c) with the good part of (b).** Do not parameterize the entire
397-element D21 basis, and do not substitute all 22 pivots into the ten
pristine Row_22 rows. Instead:

1. use the exact rank-four deep-tail block to replace the ten Row_22 rows by
   six compatibility rows;
2. replay the 22 pivot definitions into only those six rows, reducing in the
   D21 coordinate ring after every stage;
3. prove that, on the D21 locus, the remaining auxiliary dependence factors
   through only

   \[
   d_1=x17-x32,\qquad d_2=x25-x37;
   \]

4. make the rank-complete fixed-`W` decision object consisting of the D21
   core plus those six affine equations in `d1,d2`; and
5. as an optimization, eliminate `d1,d2` on rank-two charts to obtain four
   obstruction functions `R1,...,R4` on the 13-dimensional D21 base and
   cover the determinantal rank-drop boundary.

The canonical solve is therefore

\[
I_{21}+\langle B(z)d+q(z)\rangle
\]

in 18 fixed-`W` core variables plus `d1,d2`: an expected **20-variable,
30-equation** polynomial system that automatically includes every rank
stratum. The faster rank-two-chart solve is

\[
I_{21}+\langle R_1,R_2,R_3,R_4\rangle.
\]

Add the four obstructions incrementally, one at a time.

This is the real fiber-first reduction, not a new 87-variable F4 attack. The
two-direction cancellation and four-obstruction count are discovery results,
not yet global theorems: the symbolic quotient and provenance gates below
are load-bearing. Keeping `d1,d2` avoids making a rank assumption; the
four-obstruction version is smaller but needs rank-chart coverage.

The robust fallback is already measured exactly. First rank-project Row_22,
then fix a `W`-root branch, and eliminate all 22 pivots in a good order. At
`p=105337`, every one of the 16 `W`-branches gives the same

> **25 variables / 30 equations / 12,251 terms / degree at most 9**

object. Run that if the quotient proof fails or the `Ri` expressions swell.

Keep the running 48-hour lane alive as a shadow lottery and telemetry source,
but do not wait for it and do not launch copies of the same 87-variable
presentation.

## 1. What the new data actually says

The D21 result is decisive about presentation quality. The fixed-radical
CORE2 fiber solves in 11 seconds at each of the three primes, with a
397-element basis and a 13-dimensional, rational-point-rich locus. See
[SHEET6-DIRECTIONB §7.S4](../SHEET6-DIRECTIONB.md) and the
[campaign log](../notes.md). The D23 hybrid, by contrast, timed out in all
three 12-hour lanes and the two main lanes sat near 121 GB for roughly their
last five hours. That does not show that D23 is intrinsically hard. It shows
that adding the pristine quadratic Row_22 block destroys the favorable D21
presentation.

The 12/12 filter result is useful localization, not an emptiness argument.
Each D21 point was tested after setting the 28 D21-free old directions to
zero and to two random draws, and then solving only for the ten new deep
tails. Therefore the banked statement is exactly 36 inconsistent point/draw
tests. It did not originally quantify existentially over those 28 directions.

An exact all-12 quotient replay now gives the right local mechanism. At every
banked D21 point, the deep matrix has rank four. After solving the 22 pivots
and projecting that deep block, exact reduction by the specialized pivot
ideal makes all six compatibility rows degree one in the 28 auxiliaries and
leaves support only in `d1,d2`. At every point the resulting 6-by-2
coefficient matrix has rank two while the augmented matrix has rank three.
Thus **all 12 D21 base points are excluded for every assignment of all 28
auxiliaries**, not merely for the three sampled draws. The six free deep
kernel coordinates cannot repair a failed compatibility.

The fixed-point shape census shows why the restriction is cheap:

| fixed D21 base point | variables | equations | terms | degree |
|---|---:|---:|---:|---:|
| 22 pivots + 10 pristine Row_22 rows | 60 | 32 | 2,412 | at most 3 |
| 22 pivots + 6 deep compatibilities | 50 | 28 | 1,723 | at most 3 |
| after exact pivot-ideal reduction | `d1,d2` effective | 6 | affine | 1 |

Globally, however, this predicts four equations on the D21 base; it does not
predict emptiness. If four independent conditions survive on a 13-fold, a
random base point should almost always die even when the D23 projection is
still positive-dimensional. The all-12 replay remains a discovery audit
until its points, reduction script, and provenance are banked under G0.

### The missing variables in the literal “13-parameter” proposal

The proposed 87-to-13 count conflates the compressed D21 base with the full
source fiber seen by D23. The relevant headers give:

| object | header variables | role |
|---|---:|---|
| D21 CORE2 finite fiber | 22 | 18 `x`-coordinates plus `W1,W2,uW1,uW2` |
| D23 finite fiber | **82** | not the documented 80 |
| difference | 60 | 22 pivots + 28 old free directions + 10 deep directions |

The 28 old free directions are

~~~text
x16,...,x41, x48, x69.
~~~

They are unconstrained at D21 but re-enter the pristine D23 reconstruction.
Thus the full preimage over the 13-dimensional compressed base has 28 more
free directions before Row_22 is imposed. The D23 header discrepancy was
already noticed in [sol-char0-plan §1.2](sol-char0-plan.md); it must be fixed
in the legend before a fiber certificate is promoted.

This is why a global rational parametrization of the 397-element basis is not
the first move. The listed 13 coordinates are a maximal independent set for
the initial ideal, not a promise of one small denominator-free chart. The
naive localization already has more than 100,000 standard monomials. A
rational parametrization would introduce denominator loci that must then be
covered for an EMPTY result.

## 2. The algebraic reduction

### 2.1 Ten deep equations become six compatibilities

Let `y=(x74,...,x83)^T`. The ten pristine Row_22 equations have the
form

\[
F_{22}(z,y)=A(z)y+b(z).
\]

The deep coefficient matrix has rank four. Its variable dependence factors
as

\[
A=C\,\operatorname{diag}(u_1,\ldots,u_{10}),
\]

where `C` is constant on the chosen radical factor and each `ui` is a
product of chart units among `Ai,Wi,HWi`. This is the structural
reduction identified in [sol-char0-plan §2](sol-char0-plan.md). Construct an
exact left kernel `L` of dimension six and form

\[
c=L b.
\]

Four transformed Row_22 equations solve four deep coordinates; the other six
deep coordinates remain free. The six rows `c=0` are the complete
compatibility condition. Crucially, form `Lb` **before** any pivot
substitution. Full substitution into all ten rows is the rejected
4,971,007-term, degree-32 presentation.

The rank-four statement must be certified rather than inferred from point
evaluations. Over the exact coefficient field, exhibit invertible matrices
`U,V` with

\[
UCV=\operatorname{diag}(I_4,0_6),
\]

verify the inverses, and record why every column factor is a unit on the
chart. Once this passes, no hidden deep-rank chamber exists on that chart.

### 2.2 The measured partial-elimination sweet spot

At `p=105337`, split the pole-scale roots, project ten Row_22 rows to six,
and eliminate pivots in this order:

1. the three cheap low pivots `x42,x44,x49`;
2. the 16 high pivots; and
3. the remaining low pivots `x43,x45,x50`.

The six compatibility rows shrink rather than grow:

| stage | terms in six rows |
|---|---:|
| before pivot elimination | 25,554 |
| after three cheap lows | 16,134 |
| after the 16 highs | 10,500 |
| after all 22 pivots | **7,054** |

All 16 `W`-branches have identical counts. The six final row sizes are
`1176,1176,1176,1176,1176,1174`, and their degree is at most nine. Their
support is exactly the 18 D21 `x`-variables together with

~~~text
x16, x17, x24, x25, x32, x37, x69.
~~~

The other 21 reactivated directions cancel. Adding the fixed-`W` D21 core
(24 rows, 5,197 terms, degree at most eight) gives the measured
25-variable/30-equation fallback above. This is the answer to the “partial
elimination sweet spot?” part of option (b): project first, then eliminate all
pivots into only the six projected rows.

### 2.3 Quotient again: seven auxiliaries become two differences

The fallback is small enough to solve directly, but it still carries
on-locus redundancy. Reduce its six compatibility rows by the D21 ideal. The
fixed-point experiments show that the coefficients of `x16,x24,x69` vanish
in the quotient, while `x17,x32` and `x25,x37` occur as opposite pairs.
The expected quotient form is

\[
c(z,d)=B(z)
\begin{pmatrix}d_1\\d_2\end{pmatrix}+q(z),
\qquad B\in\operatorname{Mat}_{6\times2}(k[z]).
\]

The safest solver object retains `d1,d2` and all six affine rows. It is only
two variables larger than the projected D21 base and automatically includes
every coefficient-rank stratum. On a rank-two chart, an optional faster form
solves two rows for `d1,d2` and substitutes into the other four. Equivalently,
take a left cokernel of `B`. This produces four core-only obstructions
`R1,...,R4`. Retain a straight-line provenance DAG rather than expanding
rational substitutions unnecessarily.

The rank boundary matters. If a chosen 2-by-2 minor `Delta` is not a
unit on the D21 locus, an EMPTY result after saturating by `Delta` covers
only the generic rank-two chart. The loci `rank(B)<=1` and,
if present, `rank(B)=0` require their own compatibility
conditions. Chamber the determinantal minors, not the 13 independent
coordinates blindly.

## 3. Gates for the single best move

### G0 — freeze a replayable object

Before promoting a solver result:

- reconcile the 82-variable D23 fiber header with the 80-variable prose;
- bank the D23 emitter, the currently transient `/tmp/fiber_filter2.py`, the
  12 points, all random seeds, the 22-pivot reconstruction log, and raw-row
  labels;
- verify that every reduced row reconstructs the ten pristine Row_22 rows and
  ultimately the original source rows; and
- hash the canonical generator order, variable order, radical fiber, prime,
  and `W`-branch.

At present [fastelim.py](../cases/fastelim.py) defines `run_core2`, but its
main driver does not emit the banked CORE2/D23 artifacts. The filter is also
recorded in [SHEET6-DIRECTIONB §7.S4](../SHEET6-DIRECTIONB.md) as a `/tmp`
harness “to be promoted.” A terminal claim should not depend on transient
state.

### G1 — certify the deep Schur step

- Factor `A=C diag(ui)` exactly on the stated chart.
- Prove `rank(C)=4`, verify `LA=0`, and verify the invertible
  row/column transformations.
- Record polynomial unit identities for `Ai,Wi,HWi`, not merely numeric
  nonvanishing.
- Reconstruct all ten pristine Row_22 equations from four solved deep
  coordinates plus the six compatibilities.

Failure of this gate means retain all ten deep equations; it does not justify
assuming constant rank.

### G2 — prove the two-direction quotient globally

For one fixed `W`-branch at `p=105337`:

- construct `c=Lb` before pivot substitution;
- replay all 22 pivot relations into only `c`, reducing and unit-normalizing
  after each stage;
- reduce coefficients by a fresh certified D21 basis; and
- prove in the quotient, not just at sample points, that all pure and mixed
  auxiliary second differences vanish and that the only nonzero first
  differences factor through `d1,d2`.

The 397-element basis is excellent for normal forms and discovery. Do not
mistake it for a finite vector-space basis or for provenance to the original
rows.

### G3 — emit the rank-complete object; optimize with covered charts

- Form `B(z)` and `q(z)` exactly.
- Determine the generic rank on every D21 component.
- First emit and solve the six affine rows with `d1,d2` retained. This is the
  rank-complete control and needs no determinantal saturation.
- On a rank-two chart, select a nonzero 2-by-2 minor `Delta`, derive
  four cleared-denominator cokernel rows, and verify

  \[
  R_1=\cdots=R_4=0
  \quad\Longleftrightarrow\quad
  \exists(d_1,d_2):B d+q=0
  \]

  after saturation by `Delta`.
- Replay all 12 known excluded points: `B` must have rank two and `[B|q]`
  rank three at each.
- Either prove `Delta` is a unit modulo `I21`, or solve every
  determinantal rank-drop stratum. No generic-chart `[1]` is a global EMPTY
  verdict.

### G4 — census before solving

Emit all three targets from the same canonical source:

1. the preferred rank-complete D21 core plus `d1,d2` and six affine rows;
2. the rank-two-chart D21 core plus four `Ri`; and
3. the measured 25-variable/30-equation fallback.

Register term count, support, actual total degree, row round-trip, and random
evaluation equivalence. If the four-obstruction artifact exceeds roughly
100,000 expanded terms or degree 16, or loses sparse provenance, do not feed
it blindly to F4. Use the rank-complete six-row object instead. If quotient
normal forms themselves swell, use the 12,251-term fallback or keep the `Ri`
as an arithmetic DAG/sparse interpolation target. The purpose of this gate
is to avoid recreating the 4.97-million-term failure under a new name.

### G5 — one-branch pilot, then exhaustive cover

Pilot one `W`-root branch of the representative radical fiber at
`p=105337`, with a 30–60 minute telemetry cap. Start with the rank-complete
20-variable affine object; race the four-obstruction chart if G3 has already
certified it. Promote the presentation if it returns a terminal result or
shows at least a threefold improvement at the same degree/pair frontier over
the hybrid. Otherwise switch immediately to the 25-variable fallback and an
algorithmically different engine.

For a modular witness, one `W`-branch and one radical fiber suffice. For an
EMPTY statement, cover every `W`-root, every determinantal rank chart, and
every radical factor not removed by a proved symmetry, then repeat at another
prime. The current fixed radical fiber is only the `A1,A2,+,+`
representative; the existing finite cover has 36 radical fibers.

### G6 — reconstruct before interpreting the verdict

For a proper basis or extracted point:

1. choose `d1,d2` satisfying the six affine rows and choose the remaining
   free auxiliary directions;
2. reconstruct all 22 pivots;
3. solve four deep directions and choose the six-dimensional deep kernel;
4. verify all 72 emitted fiber rows, then the unspecialized 77-row hybrid and
   the raw source rows; and
5. verify every saturation guard.

Only then compute the banked live diagnostic `e`. For `[1]`, record exactly
which `W`, radical, rank, and prime charts the result covers.

## 4. Pole-scale splitting

“Pole scales pinned” means that `W1^4` and `W2^4` are pinned, not that a
single value of each `Wi` has been selected. At `p=105337`, the D21 basis
gives

\[
W_1^4=57673,\qquad W_2^4=53212,
\]

with roots

~~~text
W1: 31931, 43162, 62175, 73406
W2:  9457, 21687, 83650, 95880.
~~~

Thus there are 16 branches. Explicit root substitution is preferable for the
reduced modular systems: it removes `W1,W2,uW1,uW2`, scalarizes many
coefficients, and produces independent lanes. One selected root pair is a
valid witness search; it is not an EMPTY cover. If `W` remains symbolic,
append the complete verified low-degree pin ideal from the D21 basis rather
than relying on the two quartics as a solver presentation.

## 5. Ranked options

| rank | move | judgment and gate |
|---:|---|---|
| **1** | **Added move: exact D21-quotient Row_22 restriction** | The best synthesis of (b) and (c): ten deep rows become six affine rows in only `d1,d2`. Solve the rank-complete 20-variable form first; the 18-variable/four-obstruction chart is its covered optimization. Requires G0–G4. |
| **2** | **(b), corrected: 25-variable compatibility presentation** | Exact, measured, and uniform across all 16 `W`-roots. This is the immediate fallback/control, not merely a speculative presentation. |
| **3** | **(a) running 48-hour extension** | Let the existing lane run concurrently while it completes F4 rounds; treat it as telemetry and a sunk-cost lottery. Do not make it the critical path or clone it. |
| **4** | **(d) a different engine, on the reduced target** | Compare msolve with an incremental basis workflow and Singular `slimgb`; use Magma/FGb only if already available. A new engine on the raw 87-variable hybrid is likely to rediscover the same matrix cliff. |
| **5** | **(c) literal global parametrization / blind 13-direction chambering** | Not first. The 13-set is a Noether-normalization set, not a small global rational chart; denominator-zero components make EMPTY coverage harder. Use it only if the four-obstruction ideal itself needs triangular decomposition. |
| **6** | **(e) rent iron** | Last. The observed 121 GB plateau on a roughly 991 GB host was not a memory ceiling. Rent only after the reduced object defeats two algorithms and telemetry predicts a genuine capacity wall. |

### Engine gate

The primary comparison should use the same hashed reduced artifact and the
same mathematical chart. Recomputing the D21 basis costs only seconds, so it
is reasonable to reduce the `Ri` with the 397-element basis and then add
them incrementally where the engine supports it. The rank-complete default is
the original 24 fixed-`W` D21 rows plus six affine rows in two added
variables; the covered chart alternative is 24 plus four obstructions.
Compare exact msolve configurations first, then a capped Singular `slimgb`
run for genuinely different behavior.
Require a terminal result or a measured improvement in frontier time/RSS
within 30–60 minutes. Any probabilistic result must be exact-reconfirmed.

### What the extension telemetry means

During this review the verbose extension trace was progressing, but was
already rebuilding the degree-seven matrix cliff: multi-million-row/column
sparse matrices, 83–86% zero reductions, a growing pair backlog, and only
about one to two effective cores during parts of preprocessing. Early RSS was
only in the low tens of GB. That pattern argues against “more RAM” as the next
instrument and against assuming four threads buy fourfold speed.

Leave the lane running while complete F4 rounds continue and the pair
frontier moves. A reasonable stop gate is about six hours with no completed
verbose round together with flat frontier/low CPU; otherwise let the existing
48-hour cap stand. Its outcome can only help, but the quotient reduction
should start now.

## 6. Verdict semantics

### NONEMPTY

A proper modular ideal on one fully specified branch is D23 survival over the
algebraic closure of that finite field. Promote it to a candidate only after
the G6 reconstruction. If an explicit point is available, compute the
Jacobian-minor valuation on the **original series-valued map**, not on the
scalar `.ms` coefficient Jacobian.

Operationally, retain the banked D23 gate `e<=11`. There is, however, a
proof-perimeter issue that should be closed before calling it an unconditional
formal-germ theorem. [DEPTH-STAB §2](../DEPTH-STAB.md) invokes a Tougeron/
Greenberg bridge, while [depthstab_check.py](../cases/depthstab_check.py)
demonstrates that bridge only on a one-variable toy. The emitted `.ms`
systems contain scalar coefficient equations and no `t`, so a t-adic minor
valuation is not obtained from their ordinary Jacobian alone. A promotion
gate should specify the square unknown-function block in the original
series-valued equations and prove that every surplus equation lies in its
completed local ideal, as the analogous requirement is stated in
[sol-lateral.md](sol-lateral.md). Until that bridge is checked, `e<=11` is
a conditional live certificate rather than a self-contained one.

### EMPTY

An empty finite truncation really does kill a formal germ at the same
coefficient-field/scope: every formal germ would truncate to a D23 point.
That kill direction does not need a stabilization theorem. But the levels of
claim remain separate:

- `[1]` on one rank/`W`/radical chart kills only that chart;
- exhaustive `[1]` at two or more primes is strong modular screening, not a
  characteristic-zero proof; and
- the characteristic-zero conclusion needs an exact certificate for the
  canonical saturated chart, with provenance back to the pristine rows.

The closure of projected images and the actual constructible image should
also not be conflated when using depth-stabilization language. None of these
cautions weakens the direct finite-truncation kill.

## 7. Immediate execution order

1. **Bank/replay:** satisfy G0 and freeze one representative p105337 branch.
2. **Project:** certify the rank-four deep block and emit the six `Lb` rows.
3. **Quotient:** replay the pivots, reduce by D21, prove the
   `d1,d2`-only statement, and emit the rank-complete six-row artifact.
4. **Optimize:** derive `R1,...,R4`, split any rank-drop boundary, and census
   the 20-variable, four-obstruction, and 25-variable targets.
5. **Pilot:** run the best of the honest artifacts for 30–60 minutes;
   race msolve against one algorithmically different capped lane only after
   the artifact is frozen.
6. **Expand coverage:** a witness stops the modular search and triggers full
   reconstruction; an EMPTY pilot triggers all 16 `W`-roots, all required
   radical/rank charts, and another prime.
7. **Promote:** for survival, apply G6 and the audited live-lift gate; for
   death, build the characteristic-zero certificate. Keep the current
   extension as a background hedge throughout.

## Bottom line

The D23 decision is not waiting for a bigger machine. The ten Row_22 rows
contain a rank-four deep solve and, after the D21 quotient, apparently only
six affine equations in two effective auxiliary differences—equivalently
four generic core obstructions. Prove that structure and solve the
rank-complete 20-variable object; use the four-obstruction charts when they
are certified. If the final quotient algebra is awkward, the already
measured 25-variable compatibility system is small, uniform across the
`W`-branches, and ready to replace the 87-variable hybrid. That is the
shortest path to an honest D23 verdict.
