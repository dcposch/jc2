# TD6-TWO-CHART-NEXT-ROW — exact rational obstruction

Date: 2026-08-24  
Charged clean basis: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`  
Status: **PROVISIONAL PRODUCER / Q-EMPTY / STOP**

## Verdict

For the exact numerical SP-2/r9-M2 chart-pattern specialization frozen in
`td6-two-chart-first-band-20260824.md`, the next x-side Jacobian row is
impossible over `Q`.  In fact, throughout the complete 94-dimensional affine
space that passed the first-band gate,

\[
  [s^{-1}t^{13}]J(f,g)=-{18858\over3125}\ne0.       \tag{1}
\]

This single coefficient is an exact `Q-EMPTY` certificate.  The requested
opposite-side next row was also compiled and audited, but is not needed for
emptiness.

The scope is deliberately narrow.  Equation (1) kills this one frozen choice
of common centering, F1 orbit values, dead stretch, and pole parameter.  It
does **not** kill SP-2, any of the eight td=6 terminal classes, or JC2.  It is
not a theorem that these numerical moduli are forced.

## 1. Exact hypotheses

Let

\[
 f=\sum_{i=0}^{15}\sum_{j=0}^{60}a_{ij}x^iy^j,
 \qquad
 g=\sum_{i=0}^{25}\sum_{j=0}^{100}b_{ij}x^iy^j
 \quad(a_{ij},b_{ij}\in\mathbb Q).
\]

Use precisely the frozen charts and targets:

1. centered x side
   \[
     y=s^{-1},\qquad x=s+s^2+s^3+t s^4,
   \]
   with `f,g` holomorphic at `s=0`, boundary values
   `[s^0]f=t^15`, `[s^0]g=t+t^25`, and first condition
   `[s^-2]J=0`;
2. F1 side `x=q^-5`, `y=eta q`, with no terms below `q^-15,q^-25`
   and leading patterns `P^3,P^5`, where
   \[
     P(\eta)=(\eta^5-1)^2(\eta^5-2)
              \left(\eta^5-{28\over25}\right);
   \]
3. r9 side
   \[
     x=r^{-25},\qquad y=r^5+\zeta r^{17},
   \]
   with no terms below `r^-3,r^-5` and leading patterns
   \[
   \begin{aligned}
     p(\zeta)&=27\zeta^6-3\zeta,\\
     q_0(\zeta)&=243\zeta^{10}-45\zeta^5+{5\over3}.
   \end{aligned}
   \]

These are exactly the hypotheses of the previous first-band replay, whose
same global coefficients passed `[r^0]J=1`.  No additional band or hidden
normalization is introduced here.

### The exact scoped theorem

**Theorem.** Every pair `(f,g)` over `Q` satisfying the three finite transport
conditions above and `[s^-2]J=0` satisfies (1).  Consequently no such pair can
also satisfy `[s^-1]J=0`; therefore the paired system consisting of both
`[s^-1]J=0` and `[r^1](J-1)=0` is empty over `Q`.

The proof is the exact affine parameterization and one-coefficient identity
below.

## 2. Complete affine parameterization

The compiler reconstructs all `6547` frozen first-band affine rows over `Q`.
Sparse Gaussian elimination has

\[
  \operatorname{rank}=3508\quad\hbox{in }3602\hbox{ variables},
  \qquad \dim=94.
\]

It orders the 94 nonpivot global coefficients as `u_0,...,u_93`, expresses
every `a_ij,b_ij` affinely in them, and replays every one of the 6547 original
rows coefficientwise in all parameters.  The nonpivot coordinates occur as
an identity block, so the map is both exhaustive and injective.  Setting all
`u_i=0` recovers the deterministic witness from the first-band report.

Canonical affine-parameterization SHA-256:

`bfef113f3c4d1ea4ad323b7fd262955bcddf081cad8025c632f9033519015783`.

## 3. Why the nominal quadratic row becomes linear—and contradictory

Write the centered expansions

\[
\begin{aligned}
 F(s,t)&=p(t)+s f_1(t)+s^2f_2(t)+O(s^3),\\
 G(s,t)&=q(t)+s g_1(t)+s^2g_2(t)+O(s^3),
\end{aligned}
\]

where `p=t^15` and `q=t+t^25`.  Since
`dx wedge dy=s^2 ds wedge dt`, the already-imposed first row is the constant
term of `F_sG_t-F_tG_s`; the next row is

\[
 [s^{-1}]J=
 f_1g_1'-f_1'g_1+2f_2q'-2p'g_2.       \tag{2}
\]

A priori (2) is quadratic in the 94 affine parameters.  Exact substitution
shows that the complete first-band system has already frozen

\[
 f_1=-{384\over25}t^{14},
 \qquad
 g_1=-{128\over125}-{128\over5}t^{24},
 \qquad
 [t^{13}]f_2={66927\over625}.          \tag{3}
\]

Thus every quadratic parameter monomial in (2) vanishes identically.  At
degree `t^13`, the terms `f_1g_1'` and `p'g_2` cannot contribute by degree,
and (2)--(3) give

\[
\begin{aligned}
 [t^{13}s^{-1}]J
 &= -14\left(-{384\over25}\right)
             \left(-{128\over125}\right)
    +2\left({66927\over625}\right)\\
 &= -{18858\over3125},
\end{aligned}
\]

proving (1).  The compiled parameter polynomial for this row contains only
that constant and has zero coefficient on every `u_i`.

As an independent check, the replay reconstructs the parameter-zero global
polynomials, differentiates them directly in `Q[x,y]`, substitutes the chart,
and recovers exactly the same full `[s^-1]J` band and coefficient (1).

## 4. Row, degree, and tangent audit

The compiler keeps every possible coefficient slot, including identities:

| next condition | scalar slots | nonzero parameter rows | parameter degree | quadratic monomials | tangent rank at `u=0` |
|---|---:|---:|---:|---:|---:|
| x `[s^-1]J=0` (`t^0,...,t^39`) | 40 | 37 | 1 | 0 | 36 |
| pole `[r^1](J-1)=0` (`zeta^0,...,zeta^13`) | 14 | 2 (degrees 3, 8) | 1 | 0 | 2 |
| combined | 54 | 39 | 1 | 0 | 38 |

The “tangent rank” is the exact rank over `Q` of the derivative of the two
next-row residual maps at the frozen witness `u=0`.  Because the rows collapse
to affine-linear form, it is constant on parameter space.  The constant
contradiction (1) has zero derivative, explaining why the x affine-row count
is 37 while its tangent rank is only 36.  Tangent rank alone would not detect
the emptiness.

At the pole, write

\[
 F=r^{-3}p+r^{-2}p_1+\cdots,
 \qquad G=r^{-5}q_0+r^{-4}q_1+\cdots.
\]

The local wedge row is

\[
 -3p q_1'-2p_1q_0'+4p'q_1+5p_1'q_0.
\]

The compiler divides this by the exact chart determinant coefficient `-25`
to encode the actual `[r^1](J-1)` row.  Independent global differentiation
replays its two nonzero coefficient rows exactly.

The canonical serialization of all 40+14 parameter equations has SHA-256

`b466000b5b4cb73c4dfad1c6ef58706b88369d8faa29520e5b5105191802147b`.

The certificate payload
`[s^-1*t^13]J=-18858/3125;parameter_coefficients=0` has SHA-256

`cb96cef005c2b2455841e455149580514482974b4ea49bb470109777b58e3efc`.

No good-prime probes were run: an exact characteristic-zero certificate is
strictly stronger and made preflight unnecessary.

## 5. Smallest remaining implication

The next global question is no longer another coefficient row for these
fixed numbers; this specialization is dead.  The smallest missing implication
is whether a corresponding obstruction persists when the **licensed common
centering and F1/r9 moduli are retained symbolically**, or whether some
source-typed parameter choice makes the obstruction vanish and permits the
next paired rows.  In particular, the ledger licenses common centering but
does not force `(1,1,1)`, and it does not force the orbit values
`(1,2,28/25)` or `A=1/9`.

A valid successor must therefore vary those moduli inside the same fixed
rectangles and preserve the actual F1-to-r9 transport relation.  Repeating
more bands at the now-empty numerical point would add no information.

## 6. Reproducibility and scope

Run:

```text
python3 cases/td6_two_chart_next_row_20260824/replay.py
```

The replay imports the byte-frozen first-band compiler only after checking its
hash, constructs the complete affine family, compiles both requested next
rows, verifies (1) symbolically, and independently differentiates the global
parameter-zero witness.

| artifact | SHA-256 |
|---|---|
| next-row replay | `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8` |
| canonical replay stdout | `6826250937a7467d04c75d914a452160cb994d4592586285414831caf54805df` |
| imported first-band replay | `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735` |
| first-band report | `cb373892233bddaf1b8fbf7722335ca43ee366b337151c3b244d2604d8168bf2` |
| first-band freeze manifest | `995a0ba55a20b9aa59626654614fe54a5f8beb95742a5376ddf006eef3fe3d49` |

**JC2 scope:** no terminal class is killed, no counterexample is constructed,
and the plane Jacobian conjecture is neither proved nor disproved.  The result
is an exact finite-order obstruction for one licensed but non-forced
two-chart specialization.  No canonical campaign file was edited, no degree
bound was widened, no extra band was imposed, and no AWS work was launched.
