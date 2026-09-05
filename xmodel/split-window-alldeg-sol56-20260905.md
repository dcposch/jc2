# The all-degree finite split-window theorem

**Lane:** `split-window-alldeg-sol56-20260905`  
**Date:** 2026-09-05  
**Verdict:** **THEOREM (necessary finite screen, all degrees); ES not eliminated in general**

## 0. Verdict first

There is an all-degree theorem, but its honest conclusion is a finite necessary
list, not realization and not a split-chart kill.

For every *realized* Moh/Xu principal-minor datum with `u_s>=2`, effective
`s>2`, and first separation `rho<v_s/u_s`, the decorated pair
`(rho,lambda)` belongs to an explicitly finite set computed from the skeleton.
Here `lambda` is the multiplicity partition of the monic degree-`u_s` face
polynomial.  The set is obtained by:

1. enumerating reduced `rho=P/Q` with
   `1<rho<v_s/u_s` and `Q<=u_s`;
2. enumerating every partition `lambda |- u_s` with at least two parts;
3. imposing the exact Puiseux-Galois covariance `(G)`; and
4. imposing the exact local-exponent feasibility condition `(L)` coming from
   the split-face Jacobian ODE.

The charged `(99,66)` result is reproduced exactly: on S1, S2, S3, S4 and S7,
`66` raw pairs become `54` killed and `12` survivors.  S8 separately gives
`12 -> 2`.  One correction is essential for all degrees: the charged claim
that `(L)` is independent of `W=(-mu_s-2)/d_s` is true on those `(99,66)` rows
but false in general.  The nonnegativity condition on the cancelled local
exponent retains `W`.  The repaired tool catches `29` otherwise missed leaves
on `28` rows of the frozen census.

On the hash-frozen printed-conditions census with `Kmin=2`, `full=True`, and
`n<=200`, the run finds

```text
all arithmetic rows                         24,063
rows with u_s >= 2                           6,209
raw (rho,partition) slots                    78,575
G-admissible slots                           22,434
G-admissible after direct Xu 7.5 filter      10,434
survivors of the joint G+L screen              4,898
rows with an empty raw window                 2,422
rows with no G+L survivor                     3,758
```

Thus `OPEN[SPLIT-WINDOW-CLASSIFICATION]` is closed as a finite necessary
classification.  The `4,898` survivors are upper-bound carriers, not realized
splits; no universal source-to-joint-chart map is supplied.

## 1. Custody and source scope

The receipt was parsed with `awk`, pairing each charged digest and basename;
`sha256sum -c` returned `OK` for all six frozen inputs.  The replay files are
`box/split-window-20260905/frozen-inputs.sha256` and
`frozen-inputs.check.log`; no digest was retyped.

There are two scopes which must not be merged.

- The theorem below is degree-free: it applies to any actual datum satisfying
  the stated Moh/Xu hypotheses.
- `moh_skeleton_full.py` implements Moh's printed bounded-search conditions
  `(1)-(13)` beyond their published `n<=100` context.  Its `n<=200` output is a
  frozen arithmetic census, not a proof that all degree-`<=200` Keller data are
  covered.  The charged first-separation report already types this as
  `OPEN[CENSUS-COVERAGE-ALL-DEGREE]`.

### 1.1 The two radii

Moh's Proposition 5.4 on printed p.183 concerns the smallest disc containing
all roots of `g T_1^psi`.  Minimality forces that *global* radius to `-1`.
Lemma 5.3 on pp.185--186 then gives

\[
 M_s=n-2,\qquad d_s>v_s>d_s/2,
\]

and, with `u_s=d_s-v_s`, Moh's p.194 leading form

\[
 g_n(x,y)=\bigl[(y-ax)^{v_s}(y-bx)^{u_s}\bigr]^{n/d_s},
 \qquad a\ne b.
\]

This gives two projective points, not two physical places.

The radius screened here is instead
`rho=delta^*_{s-1}`, the minimum pairwise contact inside the terminal minor
disc.  Moh Proposition 6.1, pp.190--193, proves only `rho>=1`; p.193 explicitly
says that the proposition does not specify the radius beyond that estimate.
At a terminal minor probe `sigma`, his order formula is

\[
 \operatorname{ord}g(\sigma)=\frac n{d_s}(u_s\rho-v_s).
 \tag{1.1}
\]

Therefore the detector side is strictly `rho<v_s/u_s`.  Equality has order
zero and belongs to the Proposition 6.3 descent side; it is not an early split.
See the frozen [Moh PDF](../refs/moh1983_jram340_configurations_of_roots.pdf),
printed pp.183--194, and the charged radius derivation
`prop63-radius-gate-opus5-20260905.md:113-178`.

### 1.2 Exactly what Xu supplies

Xu Section 7.3 assumes an actual characteristic-zero Jacobian pair, monicity
in `y`, the two-point configuration, effective `s>2`, and its
quasi-approximate-root data.  A bare integer skeleton does not assert these
hypotheses.  Xu's `f` is the two-point polynomial; when comparing with the
orientation above, map it explicitly to Moh's `g` and swap the degree letters.

Proposition 7.3, printed pp.10--11, proves that the order-one principal-minor
face is a power of one linear polynomial.  Hence a genuine first split has
`rho>1`.  Corollary 7.5, statement p.11 and proof p.12, says only

\[
 \rho<\frac{v_s+1}{u_s+1}
 \quad\Longrightarrow\quad
 \text{no split into all }u_s\text{ distinct roots}.
 \tag{1.2}
\]

The inequality is strict.  It neither covers equality nor a partial partition
with `2<=length(lambda)<u_s`, and it says nothing about the upper strip
`(v_s+1)/(u_s+1)<=rho<v_s/u_s`.  Xu's own Section 8 illustrates both seams:
at `(u_s,v_s)=(3,8)`, the partial `[2,1]` face at `rho=2` is not excluded by
Corollary 7.5, while the `[1,1,1]` face at `rho=5/2` lies above its cutoff.
See [Xu, arXiv:1604.07683v4, Section 7](https://arxiv.org/abs/1604.07683).

Neither these pages nor Moh pp.183--194 proves the general denominator bound.
Xu Section 8 calls `den(rho)<=3` a tool for `(99,66)` without proving its
all-degree form.  Finiteness below is therefore a new lemma, not a citation.

## 2. Finite-window theorem

Write `u=u_s`, `v=v_s`.  Recover the terminal characteristic exponent from a
Moh skeleton by

\[
 \mu_1=M_1=-m,\qquad
 \mu_i=\frac{d_{i-1}}{d_i}\mu_{i-1}+M_i-M_{i-1},
 \qquad
 W=\frac{-\mu_s-2}{d_s}\in\mathbb Z_{\ge0}.
 \tag{2.1}
\]

For a realized datum, integrality of `W` is part of the terminal
quasi-approximate-root multiplicity statement.  The implementation recomputes
the gcd chain and (2.1) and fails closed if either integrality or nonnegativity
fails.

**Theorem 2.1 (all-degree finite split screen).**  Let a Moh datum arise from an
actual normalized characteristic-zero Keller pair in Xu Section 7.3's setting,
with `u>=2`.  If its terminal minor cluster first separates at
`rho<v/u`, then:

1. `rho=P/Q` in lowest terms belongs to

   \[
   \mathcal R(u,v)=
   \left\{\frac PQ:\ 1\le Q\le u,\ (P,Q)=1,\ Q<P,\ uP<vQ\right\};
   \tag{2.2}
   \]

2. its monic degree-`u` face polynomial has a partition
   `lambda=(lambda_1,...,lambda_r) |- u`, with `r>=2`;
3. the pair `(rho,lambda)` satisfies the Galois condition `(G)` of Section 3;
4. there is a monic terminal face satisfying the coefficient ODE `(F)` and the
   local condition `(L)` of Section 4; and
5. if `lambda=(1^u)`, then `rho>=(v+1)/(u+1)` by Xu Corollary 7.5.

Consequently every actual ES datum maps to the finite output of
`screen_skeleton`, and every output labelled `KILLED` is impossible for that
datum.

The polynomial `P` here is the degree-`u` common face normalization.  If Moh's
first common factor is written with degree `r|u`, raise it to the required
power.  The parts of `lambda` sum to `u`; the physical multiplicities in the
`g`-face are `(n/d_s)lambda_i`.  A face root is an at-level coefficient class,
not automatically a final place, a cover series, or a charged flag.

### Proof of the rational window and finiteness

Moh's contact theorem and (1.1) give `1<=rho<v/u`; Xu Proposition 7.3 excludes
separation at `rho=1`, yielding the strict lower endpoint in (2.2).

Choose one common Puiseux field `k((t^(1/N)))` containing the terminal minor
roots.  Since the principal cluster is Galois-stable and every member has the
same truncation below its first separation, that truncation is fixed by the
Puiseux Galois group.  If `rho=P/Q` is reduced, a generator sends a coefficient
at `t^rho` to

\[
 z\longmapsto\omega z,\qquad
 \omega=\zeta_N^{N\rho},\qquad \operatorname{ord}(\omega)=Q.
 \tag{2.3}
\]

The set of first-separation centres is stable.  For `Q>1`, every nonzero centre
has an orbit of exactly `Q` centres and only zero may be fixed; for `Q=1` the
bound is trivial.  A genuine split has a nonzero centre, so `Q<=r<=u`.

For each `1<=Q<=u`, strict `P/Q<v/u` is equivalent to
`P<=floor((Qv-1)/u)`.  Hence

\[
 N(u,v)=\sum_{Q=1}^{u}
 \sum_{P=Q+1}^{\lfloor(Qv-1)/u\rfloor}[(P,Q)=1]
 \tag{2.4}
\]

is finite.  Before any partition filter, the exact number of typed pairs is

\[
 N(u,v)\bigl(\operatorname{Part}(u)-1\bigr),
 \tag{2.5}
\]

where the one-part partition `[u]` is removed.

There is also a closed count after `(G)`.  Let `A_Q(u)` be the number of
Galois-admissible genuine partitions.  Then

\[
 A_1(u)=\operatorname{Part}(u)-1,\qquad
 A_Q(u)=\sum_{j=0}^{\lfloor u/Q\rfloor}\operatorname{Part}(j)-1
 \quad(Q>1).
 \tag{2.6}
\]

Indeed, a partition of `j` records multiplicities on the nonzero `Q`-orbits,
which consume `Qj` degrees; the remaining `u-Qj` degrees form the optional
fixed root.  The `j=0` term is `[u]`, hence the subtraction.  The full-distinct
partition is Galois-admissible exactly when `u mod Q` is `0` or `1`.  Thus the
exact `(G)+Xu` window size is

\[
 \sum_{P/Q\in\mathcal R(u,v)}
 \left(A_Q(u)-
 [u\bmod Q\in\{0,1\}]\,[(u+1)P<(v+1)Q]\right).
 \tag{2.7}
\]

The final `(G)+(L)` size is the same finite sum with the explicit feasibility
indicator `(L)`.  It depends on `(u,v,W)`, hence on the skeleton.  This proves
the theorem's finiteness assertion.  ∎

## 3. Necessary condition (G), including the group action

Let

\[
 P(z)=\sum_{i=0}^{u}p_i z^i,\qquad p_u=1,
\]

and let `omega` be (2.3).  Monicity removes the scalar ambiguity.  In the
canonical coordinate whose origin is the Galois-fixed common truncation, define

\[
 (g_\omega\cdot P)(z)=\omega^{-u}P(\omega z).
\]

Galois stability is the explicit polynomial system

\[
 \boxed{P(\omega z)=\omega^uP(z)},\qquad
 \boxed{(\omega^i-\omega^u)p_i=0\quad(0\le i<u)}.
 \tag{G}
\]

Equivalently, `p_i=0` unless `i congruent u (mod Q)`, or

\[
 P(z)=z^e H(z^Q),\qquad H(0)\ne0.
 \tag{3.1}
\]

For `Q>1`, nonzero roots occur in `Q`-tuples with equal multiplicity, with one
optional root at zero.  Thus every multiplicity frequency is `0 mod Q`, except
one may be `1 mod Q`.  For `Q=1` the condition is vacuous.

An affine face normalization must conjugate the group element.  Put the new
coordinate `w=h(z)=alpha*z+beta`, `alpha!=0`, and
`P_tilde(w)=alpha^u P((w-beta)/alpha)`.  The acting element is

\[
 \gamma_h=h\circ(\omega\cdot)\circ h^{-1},\qquad
 \boxed{\gamma_h(w)=\omega w+(1-\omega)\beta},
 \tag{3.2}
\]

and the fixed monic equation is
`P_tilde(gamma_h(w))=omega^u P_tilde(w)`.  It is not legitimate to translate the face and
continue using `z->omega z`.  The partition criterion is conjugacy-invariant,
so its kill certificates do not depend on the chosen affine coordinate.
This affine change is a reparametrization of the `pi`-face; it is not asserted
to be a polynomial automorphism of the original `(x,y)` source.

## 4. The face equation and necessary condition (L)

Fix `rho` in (2.2) and put

\[
 X=u\rho-v<0,\qquad a=WX-1+\rho,\qquad D=Wu+1.
 \tag{4.1}
\]

Let `R(z)=sum_{j=0}^D r_j z^j`, `r_D=1`, be the monic `T_s` face.  Xu's
Section 7.3 multiplicity formula gives `D=Wu+1`, as does its Section 8
calculation (`D=40` there).  The larger degree printed inside the proof of
Corollary 7.5 is inconsistent with those passages and is not silently used.
The letter `R` also avoids collision with denominator `Q`.

### 4.1 Exact coefficient system

Let `E=n/d_s`.  At the face, after nonzero scalar normalizations,

\[
 g(\sigma)=P(z)^E t^{EX}+\cdots,\qquad
 T_s(\sigma)=R(z)t^a+\cdots,
\]

while `(T_s)_f` has `P`-exponent `W+E`.  Taking the leading coefficient in
Xu's Jacobian identity (7.1) and dividing by `E P^(E-1)` gives

\[
 \boxed{aRP'-XPR'=(v-u)P^{W+1}.}
 \tag{F}
\]

The top coefficient is consistent because

\[
 au-XD=v-u.
\]

Conversely, this identity forces the normalized leading coefficient of `R` to
one.  In the same new coordinate `w=alpha*z+beta`, use

\[
 \widetilde P(w)=\alpha^uP((w-\beta)/\alpha),\qquad
 \widetilde R(w)=\alpha^DR((w-\beta)/\alpha);
\]

all three terms in `(F)` scale by `alpha^((W+1)u)`, so the monic ODE is
coordinate-consistent.

In the declared ring

\[
 A=k(\omega)[p_0,\ldots,p_{u-1},r_0,\ldots,r_{D-1}],
 \quad p_u=r_D=1,
\]

`(F)` is the finite set `F_l=0`, `0<=l<=(W+1)u`, where

\[
 F_\ell=
 \sum_{i+j=\ell+1}(ai-Xj)p_i r_j
 -(v-u)\!\sum_{i_0+\cdots+i_W=\ell}
 p_{i_0}\cdots p_{i_W}.
 \tag{4.2}
\]

Clear the positive denominators of `a` and `X` to obtain literal polynomial
equations over the coefficient field.

### 4.2 Local proof

At a distinct root `c_i` of `P`, write

\[
 P=(z-c_i)^{\lambda_i}U_i,\qquad
 R=(z-c_i)^{\nu_i}V_i,
 \quad U_i(c_i)V_i(c_i)\ne0.
\]

The coefficient of the lowest possible term on the left of `(F)` is
`(a lambda_i-X nu_i)U_i(c_i)V_i(c_i)`.  If it cancels, then

\[
 \nu_i=k\lambda_i,\qquad k=\frac aX,
 \qquad k\lambda_i\in\mathbb Z_{\ge0}.
 \tag{L-low}
\]

If it does not cancel, matching its order
`lambda_i+nu_i-1` with `lambda_i(W+1)` on the right gives

\[
 \nu_i=W\lambda_i+1.
 \tag{L-high}
\]

These are exact alternatives, not lower bounds.  Since `deg R=D`,
`sum_i nu_i<=Wu+1`.  Put

\[
 t=W-k=\frac{\rho-1}{v-u\rho}>0.
 \tag{4.3}
\]

For a low set `L` and high complement `H`, the degree inequality becomes

\[
 \boxed{|H|\le t\sum_{i\in L}\lambda_i+1.}
 \tag{4.4}
\]

An eligible root moved from high to low improves the degree budget by
`t lambda_i+1>0`.  Therefore it is enough, and exact for this necessary test,
to put every eligible root low.  Define

\[
 L_{\max}=\{i:(W-t)\lambda_i\in\mathbb Z_{\ge0}\}.
\]

Then the implemented condition is

\[
 \boxed{|\{1,\ldots,r\}\setminus L_{\max}|
 \le t\sum_{i\in L_{\max}}\lambda_i+1.}
 \tag{L}
\]

This is equivalent to existence of a low/high assignment.  Since `r>=2`, an
all-high assignment exceeds `D`; at least one low root is necessary.  In
particular `k>=0`, giving the useful sharper cutoff

\[
 \rho\le\frac{Wv+1}{Wu+1}.
 \tag{4.5}
\]

For a literal root-parameter chart, impose
`P=prod_i(z-c_i)^(lambda_i)`, invert
`prod_{i<j}(c_i-c_j)`, and for a chosen allowed `nu_i` impose

\[
 R^{(j)}(c_i)=0\ (0\le j<\nu_i),\qquad R^{(\nu_i)}(c_i)\ne0.
 \tag{4.6}
\]

The inequalities in (4.6) become ordinary polynomial equations through one
Rabinowitsch inverse of the product of the displayed nonzero factors.  This
declares the ring and does not use `sat()`.

### 4.3 The all-degree repair to 17(iiiiii)

The charged argument observed that integrality of `k lambda` is equivalent to
integrality of `t lambda`, and that `W` cancels from (4.4).  It omitted
`k lambda>=0`.  Thus independence of `W` holds only when `t<=W`.

A concrete frozen-census counterexample is

```text
(n,m; M_2,M_3; V_2,V_3) = (114,76; 57,112; 3,15)
d=(114,38,19,1), (u,v,W)=(4,15,7)
rho=11/3, t=8, lambda=[1,1,1,1].
```

`(G)` passes: one fixed root plus one 3-orbit.  But `k=-1`, so every proposed
low multiplicity is negative and `(L)` kills.  Rows with the same `(u,v)` and
`W=11,31` retain that leaf.  The correction affects `29` G-admissible slots on
`28` frozen rows.  It does not change any `(99,66)` verdict.

## 5. Implementation and controls

The reusable standard-library implementation is
`box/lib/split_window.py`.  Its public route is

```text
Moh skeleton
  -> validated (M,d,V), recomputed mu_s and W
  -> exact radius_window(u,v)
  -> every genuine partition of u
  -> G certificate + Xu flag + L certificate
  -> survivors and killed candidates
```

A `(G)` kill records every fixed-root choice and the residual frequencies
modulo `Q`.  An `(L)` kill records the optimal assignment, `minimum(sum nu_i)`,
`deg R`, and the failed inequality.  A survivor is named
`SURVIVES_NECESSARY_SCREEN`, never `SOLVABLE` or `ACTUAL_EXIT`.

`test_split_window.py` checks window endpoints, partition-number counts, the
closed Galois count (2.6), conjugated normalization, the negative-`k`
regression, and all six `u_s>=2` `(99,66)` rows.  Five tests pass.

The `(99,66)` calibration is exact:

| cohort | raw | killed `(G) or (L)` | survivors |
|---|---:|---:|---:|
| charged open S1/S2/S3/S4/S7 | 66 | 54 | 12 |
| banked S8 external control | 12 | 10 | 2 |

The twelve open-row survivors are exactly the charged list: S1 has
`4:[1,1]`; S2/S3/S7 each have
`3/2:[2,2],[2,1,1]` and `5/3:[1,1,1,1]`; S4 has
`2:[2,1]` and `5/2:[1,1,1]`.

## 6. Frozen `n<=200` census run

The driver imports only the hash-matched frozen
`/tmp/jc2-lane.D5nDdq/inputs/moh_skeleton_full.py`, enumerates
`census(n,Kmin=2,full=True)` for `4<=n<=200`, and caches identical screens by
`(u,v,W)`.  There are `132` `(u,v)` types and `2,240` `(u,v,W)` profiles among
the `6,209` rows.  Counts below are expanded back over individual source rows.

| `u_s` | rows | raw pairs | after G | after G+Xu | killed G/L | survivors |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 4,459 | 7,285 | 7,285 | 2,306 | 6,010 | 1,275 |
| 3 | 1,117 | 8,862 | 5,240 | 2,080 | 7,457 | 1,405 |
| 4 | 312 | 7,516 | 3,039 | 1,514 | 6,810 | 706 |
| 5 | 199 | 11,454 | 2,917 | 1,650 | 10,701 | 753 |
| 6 | 37 | 3,140 | 661 | 433 | 3,036 | 104 |
| 7 | 43 | 9,828 | 1,372 | 963 | 9,498 | 330 |
| 8 | 17 | 6,321 | 667 | 499 | 6,209 | 112 |
| 9 | 14 | 8,410 | 623 | 477 | 8,309 | 101 |
| 10 | 3 | 3,239 | 206 | 167 | 3,204 | 35 |
| 11 | 4 | 5,500 | 209 | 166 | 5,470 | 30 |
| 12 | 3 | 5,320 | 189 | 159 | 5,277 | 43 |
| 13 | 1 | 1,700 | 26 | 20 | 1,696 | 4 |
| **total** | **6,209** | **78,575** | **22,434** | **10,434** | **73,677** | **4,898** |

Kill attribution, counting each raw pair once, is `G only=6,668`,
`L only=17,536`, and `G+L=49,473`.  The per-row survivor-count histogram is

```text
0:3758  1:1482  2:416  3:287  4:108  5:9  6:86  7:3  8:6  9:17
10:9  11:3  12:3  13:1  14:12  15:1  17:1  18:5  21:1  25:1
```

Every row count and survivor list is in `census-rows.jsonl`.
`killed-certificates.jsonl` holds profile-deduplicated kill certificates.

### 6.1 Uniformity verdict

There is a uniform **rule**, namely `(2.2)+(G)+(L)`, and it depends only on
`(u_s,v_s,W)`.  There is no uniform “always maximal-contact” survivor shape.
Across the row-expanded output there are `148` distinct surviving partition
shapes and survivor block counts range from `2` through `11`; both
full-distinct and partial partitions occur.

The set is usually independent of `W` after `(u,v)` is fixed, but not always.
Exactly three of the 132 `(u,v)` families in this census show genuine
`W`-sensitivity:

| `(u,v)` | smaller `W` result | larger `W` result |
|---|---|---|
| `(3,17)` | `W=5`: 3 leaves | `W=17,19,25,31,45,49`: same 3 plus `11/2:[1^3]` |
| `(4,15)` | `W=7`: 3 leaves | `W=11,31`: same 3 plus `11/3:[1^4]` |
| `(7,23)` | `W=7`: 14 leaves | `W=11`: same 14 plus `13/4:[3,1,1,1,1]` |

This is why `(u,v)` alone is not an all-degree screen key.

## 7. The 296 atlas complements

As an auxiliary crosswalk, the driver read the existing historical atlas
inventory `box/recvatlas-20260905/cohort/inventory.json` (SHA-256
`972f8d295af4e53f1c95db1dbe81d35ea8984988f18d291b9356320942177a9f`).
All `296/296` source row keys match the frozen census; none is missing.

```text
atlas complementary source rows                 296
raw finite pair slots                            776
G-admissible slots                               453
G-admissible after direct Xu filter              167
G+L survivors                                    104
rows whose split complement is now empty         226
rows retaining at least one split leaf            70
survivor-count histogram       0:226, 1:52, 2:9, 3:4, 4:4, 6:1
```

The correct map is one-to-many:

```text
atlas source ID
  -> its unchanged decorated Moh skeleton
  -> profile (u_s,v_s,W)
  -> zero or more surviving (rho,lambda) ES leaves.
```

The `226` empty lists prove that no early split can realize those source
records, subject to the theorem's actual-datum hypotheses; their complementary
radius branch is consequently the only remaining route.  The other `70`
records expand to `104` finite necessary leaves.  The crosswalk is
`atlas-296-map.jsonl`.

This does **not** assign those 104 leaves to joint charts.  The atlas's `296`
number counts source-level complementary slots, not realized splits; one
source may emit several typed leaves and many emit none.  A future adapter must
preserve source ID and `(rho,lambda)`, build an explicit source ring to joint
ring homomorphism, and pull every proposed kill certificate back.  Coarse
receiver-key equality is insufficient.

## 8. Exact remaining obligations

The result is therefore:

- **PROVED-HERE, ALL DEGREE:** every realized early principal-minor split lies
  in the finite set returned by the theorem and tool.
- **PROVED-HERE:** `(G)` including its conjugated group action, the denominator
  bound, the closed window counts, the normalized coefficient ODE, and `(L)`
  with the repaired nonnegative-exponent gate.
- **MECHANICAL:** the frozen `n<=200` run, every per-row list and kill
  certificate, exact `(99,66)` replay, and the `296/296` atlas crosswalk.
- **OPEN[SPLIT-FACE-ATTAINMENT]:** passing `(G)+(L)` does not prove a face
  solution exists, much less a Keller pair.
- **OPEN[SPLIT-TO-JOINT-MAP]:** no universal necessary joint-chart map or
  certificate pullback is given for the surviving leaves.
- **OPEN[SPLIT-LEAF-KILLS]:** the `4,898` row-expanded survivors (or `104` on
  the historical atlas cohort) remain explicit algebraic obligations unless
  killed elsewhere.
- **OPEN[CENSUS-COVERAGE-ALL-DEGREE]:** applying Moh's bounded-search list
  above degree 100 remains an arithmetic experiment, not source coverage.

So the requested ES obligation is reduced to an explicit finite list per row
(`THEOREM + tool`), but it is not globally discharged.

## 9. Reproduction and artifacts

```bash
box/split-window-20260905/verify_frozen_inputs.sh
python3 box/split-window-20260905/test_split_window.py
python3 box/split-window-20260905/run_census.py \
  > box/split-window-20260905/run-census.log
```

Artifact map:

```text
box/lib/split_window.py
    reusable theorem-level enumeration and certificates
box/split-window-20260905/
    verify_frozen_inputs.sh       receipt-derived custody replay
    frozen-inputs.sha256          generated manifest
    frozen-inputs.check.log       6/6 OK
    test_split_window.py          five exact controls
    run_census.py                 n<=200 and atlas drivers
    summary.json                  aggregate counts and controls
    census-rows.jsonl             all 6,209 per-row survivor counts/lists
    profiles.jsonl                2,240 deduplicated (u,v,W) screens
    killed-certificates.jsonl     exact G/L kill certificates
    atlas-296-map.jsonl           source-ID-preserving crosswalk
    run-census.log                complete summary replay
```

No ledger, `jc2-lean`, or `ideation-*` file was edited.

## 10. FALLACY-v2 audit

- **Flag/place/series:** the global p.183 radius, the terminal minor contact
  `rho`, a face centre, a Puiseux series, and a final place remain distinct.
  Strict-below is separate from equality and later parting.
- **Carrier/attainment:** every survivor is typed
  `SURVIVES_NECESSARY_SCREEN`; no representative or lower bound is promoted to
  an actual split.
- **Group/ring map:** `(G)` states the generator and its conjugate after an
  affine face normalization.  The face gauge is not called a source
  automorphism.  The ODE coefficient ring and generator order are declared.
- **Floor/attainment:** Moh's `rho>=1` becomes `rho>1` only through Xu
  Proposition 7.3 under its stated hypotheses.  Xu's strict cutoff is not
  extended to equality or partial partitions.
- **Raw remainder degree:** `R` is explicitly the monic terminal `T_s` face;
  vanished leading coefficients branch into `(L-low)` and `(L-high)` and the
  zero/negative case is handled.
- **`sat()` wrapping:** none is used.  The optional root chart uses a declared
  Rabinowitsch inverse.
- **Target/arrival index:** ancestor `u_s=d_s-v_s` is never identified with a
  descended arrival index.
- **Per-ray/exit-set charge:** no exit-price assertion is made, so no
  `charge_basis` declaration is emitted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24356`.
- Body SHA-256:
  `278ee0c279e77220df6f9845d93e2a28d19ef076f7c92256234481d115030143`.
- Frozen basis: `c551228927d8693614b68b8f9685b5c6ce3778d5`.
