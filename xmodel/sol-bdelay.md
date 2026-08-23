# Bounded delay at residue A: exact finite-window cadence and the remaining carrier bound

**Date:** 2026-08-23  
**Inputs read in full:** `xmodel/sol-landing2.md`,
`xmodel/sol-belyi.md`, and `SHEET6-DEPTH.md`; the G2/T8--T10 perimeter
of `REDUCTION.md` was checked against the banked D21/D23/D25 records.  
**Computation:** exact arithmetic in the two registered fields, using
`cases/d23_atlas_p105337.json`, `cases/d23_atlas_p105673.json`,
`cases/d25_certificate_replay.json`, and the corresponding emitted
systems. No floating point or cross-prime recognition is used.

## 0. Verdict

**REDUCED-TO-SUBLEMMA, not proved.** The bounded-delay lemma does not
follow from either proposed rigidity mechanism.

1. The depth-closure invariant cannot give the bound. At residue A every
   admissible $l=0$ step fixes $w=2$, and such steps can be iterated
   arbitrarily in the abstract sheet calculus. The proved number $d_0=2$
   is a stabilization depth for the **jump-cell menu**, not a bound on
   segment depth or on an invisible fiber.
2. The exact D-series has a small and prime-stable **row-response cadence**:
   $\operatorname{Row}_{21}=0$, $\operatorname{Row}_{22}$ is active,
   $\operatorname{Row}_{23}=0$, and $\operatorname{Row}_{24}$ is active.
   The observed gap between active obstruction rows is exactly two at both
   primes.
3. That number 2 is **not** an empirical bounded-delay constant. The
   normalized leading tetrahedral cover is unchanged throughout D21--D25,
   while the surviving source remains positive-dimensional. In the
   leading-cover surrogate there are five consecutive coefficient cutoffs
   D21, D22, D23, D24, D25 with the same marked cover, or three successive
   banked odd windows D21, D23, D25. D23 has six invisible deep-tail
   directions before projection; D25 has four free lift coordinates and a
   ten-dimensional base on every one of its sixteen cells per radical
   fiber.
4. The repository still has neither a positive-order marked-jet map from
   these D-schemes nor a defined and computed vertical tower-gauge quotient.
   Consequently the requested number of successive **non-gauge states with
   the same actual marked Hurwitz jet is undefined**, rather than 2, 3, or
   5.
5. Absolute Belyi rigidity only says that the fixed-passport target is one
   point after gauge. It does not make a map to that point quasi-finite.
   The D25 cells give an exact counterexample to that inference.

The minimal sufficient new statement is the **uniform carrier-denominator
lemma** in Section 5. It would bound the only unbounded $l=0$ direction:
if the pole Puiseux denominator is uniformly at most $K$, then the
residue-A segment has at most $\lfloor\log_2 K\rfloor$ characteristic
steps. No present theorem supplies such a $K$, and the fixed tetrahedral
quotient forgets precisely the common-carrier data from which $K$ would
have to come.

There is therefore **no proved numerical depth cap**.

---

## 1. What must be counted

There are three different quantities in play.

1. $d_{\rm sh}$ counts characteristic vertices in an $M=1$ sheet segment.
   This is the depth of `SHEET6-DEPTH.md`.
2. $D$ is a coefficient cutoff. D21 contains rows $0,\ldots,20$, D23
   adjoins rows 21 and 22, and D25 adjoins rows 23 and 24.
3. A marked Hurwitz $q$-jet is supposed to be obtained by cancelling the
   common carriers in $h_1^3/(s_1f^4)$ and extracting four labelled
   factors. Only its order-zero leading value is currently constructed:

   \[
   \beta(u)=\frac{u(u-2/3)^3}{(u^2-u+1/6)^2}.
   \tag{1.1}
   \]

The proposed bounded-delay constant $B$ counts consecutive non-gauge
states in item 1. A gap between active rows in item 2 is not automatically
the same number. To identify them one needs a theorem assigning each sheet
transition its first D-row and proving that every later coefficient not
seen by that row is gauge. No such theorem is banked.

Likewise, constancy of (1.1) is only constancy of the leading cover. An
actual map

\[
 \mathfrak m_D:\mathcal X_D\longrightarrow
 \widehat{\mathcal H}^{(q)}_\beta
 \tag{1.2}
\]

for $q>0$ is not defined in the artifacts. Hence the exact computation
below measures the leading-cover surrogate and the coefficient response,
not the fiber of (1.2).

This distinction is load-bearing: because the fixed-passport target is
the single point $\beta$, the bounded-delay assertion is really a theorem
about the information discarded before reaching that target.

---

## 2. Route 1: $w$ proves that its own fibers can have arbitrary delay

For a chain edge with child pattern $(\nu,n\nu+1)$, put

\[
 \Delta=(n-1)\nu+1,
 \qquad
 w' = w\frac{n}{\Delta}.
 \tag{2.1}
\]

At residue A,

\[
 (\rho,\nu,\bar\kappa)=(1,2,5),\qquad w_0=2,
 \qquad W(2)=\{2\}.
 \tag{2.2}
\]

A resonant step would have $n\ge2$, $\Delta\ge3$, and
$\Delta\mid\operatorname{num}(w)=2$, which is impossible. Thus every
reachable step is in the $n=1$, or $l=0$, direction and (2.1) becomes

\[
 w'=w=2.
 \tag{2.3}
\]

This is not merely failure to find a decreasing invariant. The proof of
the depth-closure lemma supplies self-reproducing continuations. From a
state $(w,\nu,1)=(2,\nu,1)$, every chosen $\nu'\ge2$ has

\[
 n_e=2(\nu\nu'-1)\in\mathbf N^*,
 \qquad \bar\kappa'=2(\nu'+1)\in\mathbf Z,
 \tag{2.4}
\]

so another $l=0$ state is admissible. Induction produces arbitrarily long
abstract chains, all with $w=2$, the same merged-child datum, and the same
first-jump menu.

Therefore the proposed implication

\[
 \text{unchanged Hurwitz jet for long enough}
 \Longrightarrow \text{$w$ changes}
 \tag{2.5}
\]

is false in the $w$-state model: $w$ is forced **not** to change. The
number $d_0=2$ at residue A says that every menu item is already represented
by shallow depth. It does not say that deeper characteristic vertices are
gauge or nonexistent.

The one genuine depth inequality in `SHEET6-DEPTH.md` is instead

\[
 \prod_{j=1}^{d_{\rm sh}}\nu_j\le\kappa_i,
 \qquad \nu_j\ge2,
 \qquad
 d_{\rm sh}\le\lfloor\log_2\kappa_i\rfloor,
 \tag{2.6}
\]

where $\kappa_i$ is the Puiseux denominator of the actual pole branch. For
a fixed polynomial pair this is finite, but neither topological degree nor
$w=2$ bounds $\kappa_i$. Equation (2.6) isolates the scalar datum that a
new polynomial-origin or carrier theorem must control.

---

## 3. Route 2: exact D21--D25 delay at both primes

### 3.1 The marked leading point

The exact reductions of the four normalized marks are

\[
 (r,b,a,c)=
 \left(0,\frac23,
 \frac12+\frac{\sqrt3}{6},
 \frac12-\frac{\sqrt3}{6}\right).
\]

The replay gives:

| $p$ | $\sqrt3$ | $(r,b,a,c)$ in $\mathbf F_p$ | $(E_3,E_2)$ | $\operatorname{rank}J_H$ |
|---:|---:|---:|---:|---:|
| 105337 | 795 | $(0,35113,133,105205)$ | $(0,0)$ | 2 |
| 105673 | 14686 | $(0,35225,90509,15165)$ | $(0,0)$ | 2 |

In both rows $(\sqrt3)^2=3$, the two affine gauge vectors have rank two,
and they equal the kernel of $J_H$. Thus the gauge-quotiented tangent is
zero at both primes. Every B-frozen normalized leading quotient in the
banked chain is this same point.

This certifies only the order-zero marked cover. It does not construct the
positive transverse jet required in (1.2).

### 3.2 D21 to D23

The exact band statement is

\[
 \operatorname{Row}_{21}=0,
 \qquad \operatorname{Row}_{22}\ne0.
 \tag{3.1}
\]

The ten Row-22 equations are affine in ten new deep tails. Their coefficient
matrix factors as $A=C\operatorname{diag}(u_j)$, with every $u_j$ a Laurent
unit and

\[
 \operatorname{rank}C=4.
 \tag{3.2}
\]

Thus a compatible projected base has a six-dimensional affine family of
deep-tail solutions. The six Schur compatibility rows reduce further to a
rank-two condition on the D21 base. At every one of the 36 radical fibers,
and at each prime, the exact Groebner/staircase dimensions are

\[
 \dim X_{21,\omega}=13,
 \qquad
 \dim\operatorname{im}(X_{23,\omega}\to X_{21,\omega})=11.
 \tag{3.3}
\]

All 36/36 projected D23 loci are nonempty at both primes. The recorded
Schur ranks are constant:

\[
 \operatorname{rank}C_{10}=4,
 \quad \operatorname{rank}C_{\rm lift}=2,
 \quad \operatorname{rank}({\rm NF})=5,
 \quad \dim\ker({\rm NF})=1.
 \tag{3.4}
\]

So Row 22 is a genuine nontrivial source condition, but it neither kills
the source nor changes the leading marked cover.

### 3.3 D23 to D25

The next two bands have the identical parity pattern:

\[
 \operatorname{Row}_{23}=0,
 \qquad \operatorname{Row}_{24}\ne0.
 \tag{3.5}
\]

The Row-24 frontier matrix is $9\times10$, has rank four at both primes,
and produces five Schur residuals. On every radical fiber its exact
triangular certificate has

\[
 \begin{aligned}
  &\dim(\text{admissible D23 base})=10,
  &&\text{one less than the D23 projected dimension }11,\\
  &\dim(\text{free D25 lift})=4,
  &&\dim X_{25,\omega,j}=10+4=14,\\
  &j=1,\ldots,16.
 \end{aligned}
 \tag{3.6}
\]

The sixteen branches come from two independent nonzero fourth-root choices.
Exact replay gives 36 fibers times 16 cells at each prime, all isomorphic
to $\mathbb A^{14}$. All 34/34 defining rows reduce to zero through the
Laurent-unit pivot DAG at all 72 prime/fiber pairs.

The four free lift variables are

\[
 (x16,x19,x24,x27),
 \tag{3.7}
\]

and the ten free projected-base variables are

\[
 (x57,x59,x60,x62,x63,x65,x66,x68,x72,x73).
 \tag{3.8}
\]

Every level-$48+$ variable and the six Row-22 deep-kernel variables cancel
from the five final D25 residuals. This cancellation is exactly the sort of
invisibility that a bounded-delay theorem would have to end; it is not
evidence that those variables are gauge.

### 3.4 Compatibility of the three banked windows

The D25 constructor checks that its bands through 22 agree identically
with the frozen D23 rows. The banked D23 witness regression gives 1566 zero
row evaluations per prime. Conversely, the D25 certificate supplies an
all-$x$-zero point on every radical fiber after choosing the indicated
fourth roots of $W_1^4,W_2^4$; its D23 and D21 truncations satisfy the
corresponding lower systems.

Hence there are exact compatible modular chains

\[
 x_{25}\longmapsto x_{23}\longmapsto x_{21}
 \tag{3.9}
\]

at both registered primes. The chain is not an artifact of comparing
unrelated nonempty varieties.

### 3.5 What empirical $B$ is—and is not

The exact measurements are:

| quantity | $p=105337$ | $p=105673$ | meaning |
|---|---:|---:|---|
| zero row before next active row | 1 | 1 | Rows 21 and 23 |
| gap between active rows | 2 | 2 | Row 22 to Row 24 |
| successive banked windows with fixed leading $\beta$ | 3 | 3 | D21, D23, D25 |
| consecutive coefficient cutoffs with fixed leading $\beta$ | 5 | 5 | D21 through D25 |
| D23 deep-tail kernel before projection | 6 | 6 | rank 4 in ten tails |
| D25 free lift dimension per cell | 4 | 4 | after the implemented pins |

Thus

\[
 \boxed{B_{\rm row}=2}
 \tag{3.10}
\]

is an exact and stable **response cadence** on this window. It is a useful
engineering prediction for the next bands.

It is not a valid value of the bounded-delay $B$. If “jet” is replaced by
the leading cover and “non-gauge” by “survives the implemented
normalizations,” the observed run is already three banked states, or five
individual D-cutoffs. Under those surrogate conventions one obtains only
the lower bounds $B\ge3$ or $B\ge5$, respectively—not an upper bound.
Because the actual positive-order jet map and vertical gauge quotient are
undefined, even these are explicitly **surrogate lower bounds**, not a
formal refutation of a proposed BMRQ value.

> **CONJECTURE (two-row response).** The alternating zero/active parity
> continues in the graph-preserving residue-A D-series, so every genuinely
> new coefficient first enters some equation within two rows.

Even this conjecture would not prove bounded delay. A new row can solve a
coefficient uniquely, leave a positive-dimensional kernel, or impose a
condition on the old base while the normalized residual quotient remains
constant. D23 and D25 exhibit all three phenomena.

---

## 4. Route 3: Belyi rigidity does not make continuations finite

Let $\mathcal H_\beta$ be the marked fixed-passport Hurwitz scheme after
source gauge. At every good characteristic in scope,

\[
 \mathcal H_\beta=\{\beta\},
 \qquad T_\beta\mathcal H_\beta=0.
 \tag{4.1}
\]

The one absolute Nielsen orbit proves (4.1). It contains no statement about
the fiber of a source map. For every scheme $Y$, the constant map
$Y\to\{\beta\}$ is compatible with (4.1); it is finite only when $Y$ is
finite.

Here this is not hypothetical. On every D25 cell the naive leading-cover
map is

\[
 \mathbb A^{14}\longrightarrow\{\beta\}.
 \tag{4.2}
\]

It has fourteen-dimensional tangent kernel at both primes. Before the D23
projection, the Row-22 common-power layer also has a six-dimensional tail
kernel. These directions describe common carriers and upstream tower data,
not deformations of the four branch marks.

One can enrich the Hurwitz object by retaining the cancelled divisor,
labelled carrier jets, the B-side, and graph data. Such an enriched target
might receive a faithful tower map, but classical tetrahedral rigidity no
longer says that this enriched target is finite. Finiteness would then be
the new theorem, not a consequence of the Nielsen orbit.

Therefore Belyi rigidity reduces the problem to controlling the fiber over
one point; it supplies no control of that fiber.

---

## 5. Minimal sublemma

The $w$-calculus already bounds the number of resonant changes. At residue A
there are none. The only remaining source of arbitrary sheet depth is the
self-reproducing $l=0$ carrier chain, and (2.6) bounds its length once the
pole denominator is bounded. This gives the following scalar target.

> **CONJECTURE UCD (uniform carrier-denominator bound).** There is an
> explicit integer $K$, independent of the coefficient cutoff and of the
> chosen compatible continuation, such that every polynomial-origin,
> graph-preserving residue-A tower carrying the normalized tetrahedral
> quotient (1.1) has pole Puiseux denominator
>
> \[
>  \kappa_i\le K.
>  \tag{5.1}
> \]
>
> A sufficient carrier-side reading is that the common carrier removed
> before forming $h_1^3/(s_1f^4)$ cannot acquire an unbounded sequence of
> new characteristic denominator factors while the normalized quotient
> stays tetrahedral.

UCD is sufficient for bounded delay on the residue-A $M=1$ segment:

\[
 \prod_j\nu_j\le\kappa_i\le K,
 \qquad \nu_j\ge2
 \quad\Longrightarrow\quad
 d_{\rm sh}\le\lfloor\log_2 K\rfloor,
 \quad\text{so one may take }B=\lfloor\log_2 K\rfloor.
 \tag{5.2}
\]

This implication is exact. It uses the characteristic-vertex theorem of
`SHEET6-DEPTH.md`, not a heuristic identification of D-rows with sheet
levels.

What remains unproved is (5.1). The Belyi map sees the quotient after the
carrier has been cancelled, so its degree four does not bound the carrier's
Puiseux denominator. The D21--D25 computation confirms that substantial
carrier-tail freedom survives while the quotient is fixed. Topological
degree also does not bound $\kappa_i$, as the depth theorem explicitly
notes.

An equivalent artifact-facing formulation is:

> **CONJECTURE UGD (uniform graph delay).** After the tower gauge is defined,
> there are $D_0,B$ such that no graph-preserving compatible truncation
> chain over residue A contains $B+1$ consecutive genuinely new sheet
> states whose normalized residual quotient has the same marked
> fixed-passport jet.

UCD implies the residue-A $M=1$ case of UGD by (5.2). UGD is the direct
scheme-level statement needed by `sol-landing2`; UCD is the smaller
arithmetic lemma suggested by the tower's own depth theorem.

To test UGD computationally, the next artifact must retain rather than
eliminate:

1. the six Row-22 kernel tails and every later first-occurrence coordinate;
2. all rung reconstruction graph equations;
3. an explicit vertical gauge action; and
4. the labelled factorization of $h_1^3/(s_1f^4)$ to positive order.

Only then can one count consecutive non-gauge states in a fiber of a marked
jet. The current D25 quotient and the later compatibility-only D43 ideal do
not have these semantics.

---

## 6. Final disposition

The three requested attacks have definite outcomes:

\[
\begin{array}{c|c}
\text{attack}&\text{verdict}\\ \hline
w\text{-invariant}&\text{obstructed: }l=0\text{ fixes }w=2\text{ indefinitely}\\
\text{banked D21--D25 chain}&B_{\rm row}=2\text{ at both primes; actual }B\text{ undefined}\\
\text{Belyi rigidity}&\text{obstructed: one target point gives no fiber finiteness}
\end{array}
\]

The strongest exact empirical statement is

\[
 \boxed{
 \begin{gathered}
  \operatorname{Row}_{21}=\operatorname{Row}_{23}=0,
  \qquad
  \operatorname{Row}_{22},\operatorname{Row}_{24}\ne0,\\
  \dim D21=13,\quad \dim D23_{\rm proj}=11,\quad
  D25=16\times\mathbb A^{14}\ \text{ per fiber},\\
  \text{and the normalized leading marked cover is }\beta
  \text{ throughout, at both primes.}
 \end{gathered}}
\]

This is strong evidence for a two-row **equation-response** law and strong
counterevidence to identifying that law with bounded marked-jet delay. The
named gap is **CONJECTURE UCD**, or equivalently the graph-level UGD after
the missing gauge and marked-jet structures are built.

**Final verdict: REDUCED-TO-SUBLEMMA. No bounded-delay constant and no
numerical depth cap are proved.**
