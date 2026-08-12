# Bounded Hermite--Padé algebraization test for residue A

Date: 2026-08-12.  Engine: `cases/sol_algebraization.py`.  Arithmetic:
exact finite-field arithmetic only (`python-flint`; no floating point).

## Executive verdict

The requested numeric pilot was completed, but the pre-registered
**uniform-locus verdict does not trigger**.

For an explicitly documented completion of the pinned residue-A prefixes,
the requested monomial-evaluation matrix has full column rank at both good
primes:

| prime | matrix | rank | nullity | exact certificate |
|---:|---:|---:|---:|---|
| 105337 | 16,443 x 5,461 | 5,461 | 0 | deg minimal recurrence 5,461; det(M^T D M)=30,914 |
| 105673 | 16,443 x 5,461 | 5,461 | 0 | deg minimal recurrence 5,461; det(M^T D M)=68,016 |

This proves that **that fixed formal completion is not algebraizable with the
prescribed support**.  It does **not** prove uniform full rank on the
saturated residue-A locus, because `SHEET6-TEMPLATE.md` does not define such
a depth-5,481 locus: it pins the pole generators only through slot 37, the
B-side only through slot 12, and leaves all subsequent tails unconstructed.
Those missing coefficients are precisely where an exceptional algebraizable
completion could live.  Two point ranks cannot exclude it.

Accordingly:

- uniform full rank at both primes: **not established**;
- a one-dimensional kernel reconstructing `f`: **not found** in the fixed
  pilot (nullity is zero);
- template-wide verdict: **INCONCLUSIVE / specification-blocked**;
- banked exact result: **full-rank obstruction for the stated completion**.

## 1. Matrix design

### 1.1 Newton support and depth

The branch count and `SHEET6-TEMPLATE.md` lines 61--64 give

\[
  \deg_x(f-a)=42,\qquad \deg_y(f-a)=126,\qquad \deg(f-a)=168.
\]

The same file explicitly counts the rectangular Ansatz as `127*43=5461`
(lines 325--330).  Thus

\[
 \Delta_f\cap\mathbf Z^2
 =\{(i,j):0\le i\le42,\ 0\le j\le126\},
 \qquad C=43\cdot127=5461,
\]

and the requested truncation is

\[
 N=C+20=5481.
\]

Columns are ordered lexicographically by

\[
 \operatorname{col}(i,j)=127i+j.
\]

### 1.2 Orbit generators supplied by the genome

Put `T=x^(-1/42)` and translate `c0` to zero.  The translation is an
invertible triangular change among the monomial columns and hence preserves
rank.  With the campaign gauges `A=1`, `sigma=6`, the two pole generators
have the pinned form

\[
\begin{aligned}
Y_1={}&T^{12}+u_{18}T^{18}+u_{24}T^{24}+u_{30}T^{30}
 +\alpha_1T^{32}+v_{1,34}T^{34}+v_{1,36}T^{36}+w_1T^{37}
 +\sum_{m\ge38}p_{1,m}T^m,\\
Y_2={}&T^{12}+u_{18}T^{18}+u_{24}T^{24}+u_{30}T^{30}
 +\alpha_2T^{32}+v_{2,34}T^{34}+v_{2,36}T^{36}+w_2T^{37}
 +\sum_{m\ge38}p_{2,m}T^m,
\end{aligned}
\]

where

\[
 \alpha_1^3=3+\sqrt3,\qquad \alpha_2^3=3-\sqrt3.
\]

The seven displayed `u/v` coefficients are exactly the free dead-stretch
coefficients on the grids in section 1c.  All intervening off-grid prefix
coefficients vanish.  Section 1d pins 42 B-side series in total but neither
their post-prefix tree nor their orbit partition.  The one-orbit model used
here writes

\[
 Y_B=\beta T^{12}+\sum_{m\ge13}b_mT^m,
 \qquad \beta^7=3/2.
\]

Taking this as one transitive 42-orbit is an explicit additional choice,
also made (with a caveat) by the R1 engine.

For a primitive 42nd root `zeta`, the conjugates are

\[
 Y_{r,k}(T)=Y_r(\zeta^kT),\qquad 0\le k<42.
\]

### 1.3 Evaluation matrix

For

\[
 F(x,y)=\sum_{i=0}^{42}\sum_{j=0}^{126}c_{ij}x^iy^j,
\]

multiply the substituted relation by `T^1764`, where `1764=42*42`.
For representative `r` in `{P1,P2,B}` and `0<=n<5481`, define

\[
 M_{(r,n),(i,j)}
  =[T^n]\,T^{1764-42i}Y_r(T)^j
  =[T^{n-1764+42i}]Y_r(T)^j .
\]

A coefficient with negative index is zero.  This gives

\[
  M\in\mathbf F_p^{16443\times5461}.
\]

The full 126-series matrix is rank-equivalent to this compressed matrix.
Indeed, at the `k`th conjugate,

\[
 M_{(r,k,n),*}=\zeta^{kn}M_{(r,0,n),*},
\]

because every shift `1764-42i` is divisible by 42.  Thus conjugate rows at
fixed `n` are nonzero scalar multiples, not independent equations.

The `j=0` block is an implementation guard:

\[
 M_{(r,1764-42i),(i,0)}=1\quad(0\le i\le42).
\]

All these rows are inside `0<=n<5481`.  A trial that mistakenly dropped
orders `0..19` manufactured a nullity-one boundary kernel; restoring the
specified half-open window removed it.  This caught the most likely shift
error before the banked runs.

### 1.4 Pre-registered interpretation

For a genuinely defined saturated jet locus `V(I_sat,N)`:

- rank 5,461 everywhere at both primes would obstruct algebraization;
- rank 5,460 would give one projective relation, to normalize and verify as
  a candidate `f`;
- smaller rank would require increasing depth and factoring degeneracies.

Algebraically, the uniform assertion is emptiness of the rank-drop locus,
equivalently

\[
  1\in I_{\mathrm{sat},N}+I_{5461}(M),
\]

where `I_5461(M)` is the ideal of maximal minors.  Nonvanishing at two
sampled points is not this unit-ideal certificate.

## 2. Genome audit and exact choices

### 2.1 What is pinned and what is missing

The pole prefixes above end at `T^37`.  Every `p_i,m` for `m>=38` is
unconstructed.  The B-side is pinned only at `T^12`; its subsequent tails
and even its one-orbit versus split-orbit realization are unconstructed.
`SHEET6-TEMPLATE.md` lines 332--336 itself lists `B-side/x-side tail data`
among the remaining unknowns, and lines 283--291 say the sub-pattern tails
remain part of R1.

The requested matrix needs coefficients as deep as `T^5480`.  The cited
genome therefore does not determine a numerical matrix or a finite ideal
defining the phrase “saturated residue-A locus.”  Existing R1 objects reach
only limited coefficient bands (not slot 5,480), so they do not repair this
gap.

### 2.2 E5 erratum used in the pilot

There is an internal factor-of-three error in the template.  Lines 231--237
give

\[
 \lambda_i=9S_Mc_i^4(a_i-a_j)^2
\]

and the unsolved transport equation

\[
 9H_Mc_i^5(a_1-a_2)^2(a_i-b)
 =-\frac34\lambda_i^3w_i^4.
\]

Solving these exact displayed equations gives

\[
 w_i^4=-\frac{4H_M(a_i-b)}
 {243S_M^3(a_1-a_2)^4a_i^2c_i}.
\]

Line 239 instead prints `-(4/3)/243`, smaller by a factor of three.  The
engine derives E5 from the unsolved equation, so its cleared row has
coefficient 243, not 729.  This also avoids importing the same typo from
some older R1 saturation code.  The ratio determining `w1^4/w2^4` is
unchanged because the common factor cancels.

### 2.3 Fixed completion used for the main pilot

The main two-prime pilot chooses:

- `c0=0`, `A=1`, `sigma=6`, `s0=1`;
- all seven dead-stretch coefficients zero;
- `Y_P1=T^12+alpha1*T^32+w1*T^37`;
- `Y_P2=T^12+alpha2*T^32+T^37` (`w2=1`);
- `Y_B=beta*T^12+T^56+T^57`;
- every other coefficient through order 5,480 zero.

The B choice represents one degree-42 B place with contact sum
`4*56/42+57/42=281/42`, hence `S_B=281` and `e_B=282-S_B=1`; it is
compatible with the classical ledger but is still an added completion.

Both primes are `1 mod 84`, avoid `2*3*5*7`, split every required radical,
and satisfy the corrected E5 equations with all saturated quantities
nonzero:

| p | sqrt3 | alpha1 | alpha2 | beta | w1 | w2 | H_M | H_F | s1 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 105337 | 795 | 50630 | 10114 | 24069 | 7210 | 1 | 58944 | 91149 | 64146 |
| 105673 | 14686 | 38664 | 46664 | 48619 | 4018 | 1 | 41561 | 95504 | 88107 |

Here `H_F=2^8 H_M/7^16` and `s1=H_F^3` in the chosen gauge.

For an independent dense implementation check, the engine also supplies a
second, hash-tail completion at primes 29401 and 80557.  It gives rank
5,461 at both primes in about 49 seconds per prime.  Prime 80557 is good for
this f-only matrix but does not split `sqrt(3/2)`, so it is not advertised as
a full f/g radical-ring prime.

## 3. Exact computation and certificates

### 3.1 Sparse black-box matrix

The engine applies `M` without storing 89,795,223 dense entries.  For a
column vector, it evaluates

\[
 \sum_{j=0}^{126}A_j(T)Y_r(T)^j
\]

by Horner multiplication modulo `T^5481`, where `A_j` contains the 43
coefficients at shifts `1764-42i`.  The transpose uses reversed-polynomial
correlations.  A separately generated dot-product identity

\[
 \langle Mx,v\rangle=\langle x,M^Tv\rangle
\]

passed at both primes (values 38,015 and 90,060).

Matrix census for the sparse completion:

| p | nonzeros | density | zero rows | nonzero rows P1/P2/B | max/median row nnz |
|---:|---:|---:|---:|---:|---:|
| 105337 | 11,600,099 | 0.129183921 | 232 | 5415/5415/5381 | 2826/395 |
| 105673 | 11,600,015 | 0.129182986 | 232 | 5415/5415/5381 | 2826/395 |

The small nonzero-count difference is caused by modular cancellations.

### 3.2 Rank certificate

For a deterministic nonzero diagonal `D`, form the square black-box Gram
operator

\[
 B=M^TDM\in\mathbf F_p^{5461\times5461}.
\]

The script uses seed `0x72108+p`, forms 10,922 exact Krylov scalars
`u^T B^k v`, and applies Berlekamp--Massey.  Results:

| p | BM degree | recurrence constant | failures | det(B) | wall |
|---:|---:|---:|---:|---:|---:|
| 105337 | 5461 | 74423 | 0 | 30914 | 824.7 s |
| 105673 | 5461 | 37657 | 0 | 68016 | 824.5 s |

The scalar minimal polynomial divides the minimal polynomial of `B`, which
divides its characteristic polynomial; all have degree at most 5,461.  A
scalar recurrence of degree exactly 5,461 therefore equals the
characteristic polynomial.  Its nonzero constant is, up to the displayed
odd-degree sign, `det(B)`.  Hence `B` is invertible.  Since
`ker(M)` is contained in `ker(M^TDM)`, `M` has full column rank.  Random
projection can miss degree (a false negative), but it cannot manufacture a
degree larger than the exact minimal polynomial, so these are one-sided
exact full-rank certificates.

Authentication hashes (little-endian uint64 packing):

| p | Krylov sequence SHA-256 | recurrence SHA-256 |
|---:|---|---|
| 105337 | `875154551d96eab0dd70230e3755be8ec7d388e377c2852041bca82bd0cac924` | `59b9aaa0986dcb5b8bc8dccb0963d67178632ea296b0af6f1eca47bbb0b1027e` |
| 105673 | `232f01707dfed4ba0acc0520c7a22b9ea192eaa1b10b7c6b935df3011871e552` | `461c4f25287fa248db9870b04bd07337e26b5abcfd02eeceba98ac874f02c242` |

An independent orbit-norm/Toeplitz guard on the same completion produced
an 8,841 x 43 tail matrix of rank 43 at both primes.  The selected minor
uses rows `(j=0,q^43),...,(j=0,q^85)` and has determinants 28,166 and
41,225.  The first forbidden norm tail is `(j=0,q^46)`, values 6,803 and
41,298.  This checks the obstruction through a different algebraic
factorization.

## 4. Interpretation against the pre-registration

The literal table said “uniform full rank at both primes = template dies.”
The experiment has full rank at both primes but **not the word uniform**.
A sampled full-rank point shows that full rank is a nonempty Zariski-open
condition on any component containing that point.  Algebraization, however,
is existential and would occupy the complementary determinantal closed
locus.  Samples cannot prove that locus empty.

Thus it would be mathematically invalid to promote the fixed-completion
certificate to “residue A dies.”  Conversely, no kernel exists for this
completion, so there is no `f` to reconstruct and no Jacobian-linear solve
for `g` to start.

The decisive next object is not another sample.  One must first construct a
finite depth-5,481 saturated jet ideal carrying all pole and B tails (and all
B orbit partitions), then prove the maximal-minor ideal is a unit after
saturation, or find a point of its rank-drop locus.  Until that object
exists, the bounded Hermite--Padé avenue has delivered a strong generic/
fixed-completion obstruction but not a template-wide decision.

## 5. Reproduction

Fast bank authentication and all metadata:

```text
cd /Users/dc/code/math/jc72108
python3 cases/sol_algebraization.py --mode bank
python3 cases/sol_algebraization.py --mode bank --json
```

Regenerate both exact Wiedemann certificates (about 14 minutes per prime on
the development machine):

```text
python3 cases/sol_algebraization.py --mode wiedemann --prime 105337
python3 cases/sol_algebraization.py --mode wiedemann --prime 105673
```

Run the independent dense hash-tail completion (about 49 seconds per prime,
roughly 1.3 GB peak RSS):

```text
python3 cases/sol_algebraization.py --mode rank --prime 29401
python3 cases/sol_algebraization.py --mode rank --prime 80557
```

The `validate` mode checks the latter points, corrected E5 rows, exact roots,
and prime conditions without doing the rank computation.
