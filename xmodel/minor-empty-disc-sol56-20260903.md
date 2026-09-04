# MINOR-EMPTY and the discriminant of the principal-minor leader

Lane: `minor-empty-disc-sol56-20260903`
Date: 2026-09-04 UTC
Frozen basis: `158179af4a89e193c843f823bdea21396af1920c`

## 0. Verdict

```text
OPEN[UNIVERSAL-MINOR-EMPTY-DISCRIMINANT]
REFUTED[VANDERMONDE/DISCRIMINANT-INVERTIBILITY ALONE IMPLIES INCONSISTENCY]
CONFIRMED[FIXED-STRATUM LOCALIZATION CRITERION]
CONFIRMED[3/3 SAME PRINCIPAL OPEN; 1/3 NONTRIVIAL DISC-COLLAPSE]
EXACT-OBSTRUCTION[NO UNIFORM AUGMENTED-RANK / SCHUR-COMPATIBILITY THEOREM]
```

The requested universal theorem is **not proved by the frozen sources or
certificates**, and the proposed route has a definite reversal in its first
linear-algebra step.  The discriminant is the square of a Vandermonde
determinant.  On the distinct-root locus its nonvanishing normally makes the
packet-evaluation block invertible, hence makes its equations solvable.  It
does not make them inconsistent.  Inconsistency requires an additional
inhomogeneous row whose Schur complement is nonzero after that interpolation.
Moh, Xu, and the ladder calculation do not supply such a row uniformly.

The exact result of the 3/3 comparison is narrower:

1. In each charged branch the declared genuine-split localization defines the
   same principal open as
   `R = disc(p_red)`.
2. At `(99,66), delta=2` and `(99,66), delta=5/2`, the audited
   certificate-boundary ideal is already the unit ideal before localization.  The terminal constants
   `6264` and `64` are branch-specific pole/Jacobian Schur residues, not values
   of the discriminant or of a resultant.
3. Only at `D=108, delta=3` does the audited post-major common-`h3`
   incidence ideal nontrivially contain the discriminant.  There the rows force
   a quadratic with two declared roots to become a square, so `[1,1]` coarsens
   to `[2]`.

There is no full-chart counterexample in the inputs, so the universal
MINOR-EMPTY statement is not refuted.  What is refuted is the assertion that it
follows from the shared leader, Moh Theorem 1.2, and the discriminant/resultant
of packet evaluation.  The exact missing theorem is a global, fixed-partition
incidence/Jacobian Fitting statement

```text
disc(p_red) in radical(I_joint)
```

for every fully specified admissible datum.  None of the charged artifacts
constructs or proves that statement outside the three special charts.

## 1. Custody, scope, and computations

The receipt
`xmodel/minor-empty-disc-sol56-20260903.run.v2` was read first.  An `awk`
program joined each indexed `charged_input_<i>_sha256` field to the matching
`charged_input_<i>_basename` under the receipt's `lane_inputs_dir`; that stream
was passed directly to `sha256sum -c`.  All **12/12** frozen inputs returned
`OK`.  No digest was manually transcribed into the check and no content
mismatch occurred.

The source and evidentiary basis of the report is the twelve frozen inputs.
The two source PDFs were read at the printed pages cited below.  Supplementary
desk replays used exact arithmetic over `QQ`; their mathematical dependencies
outside the frozen directory are disclosed here:

- the frozen standalone `d108_certificate.py` completed in about one second
  and returned the ten-row pre-pivot localized certificate with identity `1`;
- the frozen `filtered_obstruction.py` completed and reproduced all three
  reported exact ranks and kernels;
- a short SymPy calculation, written only to standard output, verified the two
  parameter-uniform face ODE identities in Section 4;
- the frozen `delta2_certificate.py` is not relocatable as a standalone frozen
  file: its `ROOT=Path(__file__).parents[2]` resolves to `/tmp`, and its default
  stage/run dependencies are not among this lane's frozen inputs.  A
  byte-identical workspace twin reads the prior-lane receipt
  `xmodel/two-place-obstruction-core-sol56-20260903.run.v2`, an explicitly
  supplied `box/g9966band-20260903/runs/delta2/stage4.json`, and
  `box/g9966indep-20260903/{indep_engine.py,ring.py}`.  The driver checks the
  stage JSON against the prior receipt; the current frozen lane does not
  authenticate the two imported modules.  This supplementary replay reproduces
  terminal normal form `6264` and the eight-row identity, but the report's
  evidence for that certificate remains the frozen charged reports.  This is a
  replay-boundary limitation, not silently treated as a self-contained frozen
  replay;
- no `delta=5/2` certificate driver is among this lane's three frozen scripts;
  the separate stage-8 value `64` is audited from the two frozen charged
  reports, not claimed as a new independent replay here;
- similarly, the frozen `moh_skeleton_full.py` lacks its sibling
  `moh_skeleton_N.py` in the frozen directory.  Its byte-identical workspace
  twin passes the controls, while its own Control 4 records 658 survivors of
  printed conditions (1)--(13), versus six printed table rows.  It therefore
  supplies no missing completeness or incidence theorem.

No ledger, `jc2-lean`, `ideation-*`, or in-progress lane report was edited.
The only workspace write is this report.  No exit price is asserted.

## 2. The type-correct statement

### 2.1 Partition convention

Fix a multiplicity vector

```text
lambda = (m_1,...,m_r),       m_i >= 1,       sum_i m_i = u_s,
```

and distinct packet centres `c_1,...,c_r`.  Then

```text
p(pi)     = product_i (pi-c_i)^(m_i),
p_red(pi) = product_i (pi-c_i).
```

A genuine split means `r >= 2`, equivalently the multiplicity partition is not
the one-part partition `[u_s]`.  The phrase in the task
`partition != [1,1,...]` is not equivalent: read literally, it excludes the
fully simple splits `[1,1]` and `[1,1,1]` used in two flagship branches while
still allowing the unsplit partition `[u_s]`.  This report uses the source
definition: at least two distinct roots.

There is a second small but important point.  Since `p_red` is squarefree by
definition, its discriminant is nonzero after one has specialized to actual
distinct roots over Xu's coefficient field.  Even for an unsplit power,
`p_red` is linear and its conventional discriminant is `1`.  Thus the genuine
condition is

```text
deg(p_red) = r >= 2       and       disc(p_red) != 0,
```

not discriminant nonvanishing alone.  This is why `u_s=1` must be excluded
explicitly.

### 2.2 The fixed-stratum root ring

An ideal-membership assertion needs a parameter ring, not a single specialized
field point.  Work first on the ordered-root cover of a fixed multiplicity
stratum, with coefficient/tower/jet parameters collectively denoted `theta`:

```text
A_lambda = k[theta,c_1,...,c_r] / (the fixed chart relations),
R_lambda = disc(p_red)
         = product_{i<j}(c_i-c_j)^2                 (p_red monic).
```

The expression is symmetric and can subsequently descend through the relevant
root-permutation action.  This stratumwise construction matters: taking the
squarefree part by a gcd is not a polynomial operation on one coefficient
space across loci where multiplicities jump.  One must either use the root
cover above or a coefficient/subresultant chart with the appropriate
subresultants inverted.

Let `I_lambda` be the ideal generated by all *proved necessary* rows in that
same ring before the genuine-split localization.  The genuine part of the
necessary chart is, with `V_A` and `D_A` denoting subsets of
`Spec(A_lambda)`,

```text
X_lambda^gen = V_A(I_lambda) intersect D_A(R_lambda).
```

### 2.3 Fixed-stratum localization theorem

**Theorem 2.1 (exact algebraic criterion).**  For any commutative ring
`A_lambda`, ideal `I_lambda`, and element `R_lambda`, the following are
equivalent:

1. `V_A(I_lambda) intersect D_A(R_lambda)` is empty in `Spec(A_lambda)`;
2. `I_lambda A_lambda[R_lambda^(-1)] = A_lambda[R_lambda^(-1)]`;
3. `R_lambda` belongs to `radical(I_lambda)`;
4. `R_lambda^N` belongs to `I_lambda` for some integer `N >= 0`.

*Proof.*  The first and third statements are the standard
`V_A(I) subset V_A(R)` equivalence.  If `R^N` is in `I`, it becomes a unit after
localization, proving the second statement.  Conversely, writing `1` as a
finite combination of localized generators and clearing denominators gives a
power of `R` in `I`.  The case `N=0` is exactly `I=(1)`.  QED.

This is the rigorous content behind a discriminant kill.  Exact membership
`R in I` is the stronger kill-order-one case, not the general criterion.
Likewise, “the chart dies iff `R` is a unit” is not the right formulation:
`R` is a unit in `A[R^(-1)]` by construction, whether or not the localized
ideal is proper.  At an individual genuine field-valued datum, `R` is already
a nonzero scalar.  The nontrivial assertion is `R in radical(I)` in the
unlocalized family ring.

Consequently, **if** the missing assertion
`R_lambda in radical(I_lambda)` were proved for every admissible genuine split
datum, then MINOR-EMPTY would indeed be unconditional on the genuine split
stratum: `R_lambda != 0` is part of that stratum.  The automatic nonvanishing
does not prove the radical containment.

## 3. What Moh and Xu actually provide

### 3.1 Packets and multiplicities

Xu defines a split `pi`-root by the leading polynomial `f_sigma(pi)` having
more than one distinct root (Xu, p.1).  Moh Proposition 1.2 (p.147) factors that
leader as a nonzero scalar times a product `(pi-a_i)`, with repetitions counted
root by root.  Hence the distinct `a_i` label child packets and their repetition
counts give a multiplicity vector.  This supports the packet interpretation;
neither statement introduces a joint coefficient-incidence ideal.

### 3.2 Proposition 7.3 is the order-one nonsplitting result

Xu Proposition 7.3 (pp.10--11) concerns the **order-one** principal-minor
`pi`-root `sigma_1`.  Its proof first writes the leading coefficients of
`T_0,...,T_{s-1}` as powers of one degree-`u_s` polynomial `p(pi)` and writes
the `T_s` leader as a power of `p` times `(pi-a)`.  The conclusion is

```text
p(pi) = (pi-a)^(u_s).
```

Thus the proposition proves one common **linear-power** leader and no split at
order one.  It is not a theorem assigning an arbitrary later split leader to
all packets.

### 3.3 Corollary 7.5 treats only the full simple split

Xu Corollary 7.5 (pp.11--12) says that, when `u_s>1`, a principal-minor root at
order

```text
delta < (v_s+1)/(u_s+1)
```

cannot split into `u_s` different roots.  Inside its contradiction proof Xu
writes

```text
p(pi) = product_{i=1}^{u_s}(pi-c_i),       c_i != c_j,
```

and uses the fact that this `p` has no multiple roots in the divisibility
iteration.  Therefore the `p` in that proof is already squarefree and its only
partition is `[1,...,1]`.  Corollary 7.5 does not state the common-leader or
incidence theorem needed for arbitrary partial partitions such as `[2,1]`.

The frozen PDF also has a display inconsistency in this proof: the `T_s` and
`deg q` line uses `(-mu_s+n-2)/d_s`, while Section 7.3's multiplicity list and
Section 8's `deg q=40` use `(-mu_s-2)/d_s`.  The later charged derivations use
the self-consistent Section 7.3/8 exponent.  This does not change Corollary
7.5's stated conclusion, but it makes an unsourced symbolic generalization of
the display unsafe.

### 3.4 “Theorem 1.2” is Moh's inequality, not packet independence

Xu has no Theorem 1.2 in this role.  The cited result is Moh Theorem 1.2,
p.149.  Given an already verified coherent complete system
`{sigma_1,...,sigma_s}` with common accuracy `lambda`, a divisor `d` of all
multiplicities, and a `d`-th quasi-approximate root `h`, write

```text
f = h^d + sum_{j=1}^d h_j h^(d-j),       deg_y(h_j) < deg_y(h).
```

The conclusion is only

```text
ord h_j(sigma_i) >= j*lambda/d            for every i,j.
```

The theorem supplies a common lower bound at each member of a coherent
complete system.  It supplies no equality, no algebraic independence of
packet coordinates, no row-rank assertion, and no inconsistency.  Coherence
and completeness are hypotheses from Moh Definition 1.4 (p.148); after a
leader splits, its children must first be extended to appropriate `pi`-roots
and those hypotheses checked.  There is no universal verification in Xu.
Moh's p.208 application checks a particular two-centre coherent complete
system before invoking the theorem.

This also fixes the FALLACY-v2 floor/attainment issue: Theorem 1.2 licenses
strictly-below vanishing rows.  It does not license setting at-boundary terms
equal to a chosen face unless a separate leading-form theorem fixes that face.

### 3.5 Equation (7.1) is a leading ODE

Xu equation (7.1), p.12, is the leading Jacobian relation obtained from
`J(T_s,g) = (T_s)_f J(f,g)` after substituting one `pi`-root; the minus sign in
Xu's `(t,pi)` display comes from the coordinate Jacobian
`det(partial(x,y)/partial(t,pi))=-t^(delta-2)`.  It relates the
leader polynomials `p,q` and their `pi`-derivatives.  Sections 7--8 do not turn
it into a global two-point coefficient chart, a resultant condition, or a
Fitting ideal.  In fact, Section 8 supplies nondegenerate solutions, as the
next section makes explicit.

## 4. Source-level countermodels to the proposed discriminant step

These are countermodels to the claimed deduction from the sourced local
leader/order/ODE system.  They are **not** polynomial Keller pairs and do not
refute a future theorem using additional global coefficient compatibility.

### 4.1 The `D=108, delta=3` face works for every quadratic

The charged source derivation reduces the face equation to

```text
p q' - 23 p' q = 5 p^26,      deg p=2,      deg q=51.
```

Let

```text
p(pi) = pi^2 + b*pi - c,
u(pi) = integral(5*p(pi)^2 d pi) + e_0,
q(pi) = p(pi)^23 u(pi).
```

Then, identically,

```text
p q' - 23 p' q = p^24 u' = 5 p^26.
```

The antiderivative is a polynomial of degree five; explicitly it may be taken
as

```text
u = pi^5 + (5b/2)pi^4 + (5/3)(b^2-2c)pi^3
    -5bc*pi^2 + 5c^2*pi + e_0.
```

The desk CAS returned residual `0`, `deg u=5`, and
`disc(p)=b^2+4c`.  Setting `b=0,c=1` gives a source-level solution with
discriminant `4`.  Therefore the face ODE and shared leader do not contain the
discriminant in the radical of their relation ideal.  The later `D=108`
contradiction comes from the additional global common-`h3` incidence cut, not
from Xu's ODE.

### 4.2 Xu's `(99,66)` survivors also have nonzero discriminant

At `delta=2`, Xu Section 8 exhibits the exact identity (8.2) for

```text
p(pi) = pi^2(pi+3a),       partition [2,1],       a != 0.
```

Here

```text
p_red = pi(pi+3a),       disc(p_red)=9a^2 != 0.
```

This partial split lies outside Corollary 7.5's all-three-distinct hypothesis.

At `delta=5/2`, the leading equation reduces to

```text
q_1' + 2p^3 = 0,       p=pi(pi^2-c).
```

For every `p`, take `q_1=-2 integral(p^3 d pi)+e_0`.  Exact CAS gave residual
`0`, `deg q_1=10`, and

```text
disc(p)=4c^3.
```

Choosing `c=1` again gives a nondegenerate sourced solution.  Xu explicitly
labels this possibility open; its order `5/2` is above the Corollary 7.5
threshold `9/4`.

Thus all three flagship face data are compatible with distinct roots at the
source-leading level.  Any death must use genuinely new global shared-
coefficient information.

### 4.3 Why the resultant argument points the other way

Evaluation of a polynomial of degree `<r` at distinct points
`c_1,...,c_r` has coefficient matrix

```text
V = (c_i^j)_{i,j},       det(V)=product_{i<j}(c_j-c_i).
```

For derivative conditions one gets a confluent Vandermonde.  Its determinant
is again a product of root differences to positive powers; its square contains
the discriminant.  Localizing at `R` therefore makes this pivot block
invertible.  Given `Vx=b`, invertibility gives a unique `x`, for every `b`.

To obtain a contradiction one needs more rows.  In block form, after ordering
interpolation variables first,

```text
              x     y
pivot rows    A     B
test rows     C     D
```

with `det(A)` invertible on `D(R)`, elimination leaves the Schur object

```text
S = D - C A^(-1) B.
```

The discriminant controls whether `A` may be inverted.  Emptiness requires the
entries of `S` (and any affine/localization column) to generate `1`.  No
Vandermonde identity makes `S` nonzero.  The missing universal theorem is
precisely a rank-augmentation or Schur-compatibility theorem for this lower
block.

## 5. The three charged charts, exactly

Let `I` denote the unlocalized ideal at the certificate boundary actually
audited.  The common observation and the actual obstruction are:

| branch | `p(pi)` and partition | `R=disc(p_red)` | declared open | proved obstruction |
|---|---|---|---|---|
| `(99,66), delta=2` | `zeta^2(zeta+3rho)`, `[2,1]` | `9rho^2` | `rho != 0` | `I=(1)` before localization; terminal `6264` |
| `(99,66), delta=5/2` | `pi(pi^2-c)`, `[1,1,1]` | `4c^3` | `c != 0` | `I=(1)` before localization; terminal `64` |
| `D=108, delta=3` | `pi^2+b*pi-c`, `[1,1]` | `b^2+4c` | `R != 0` (`c != 0` after gauge) | `R in I_inc`; raw incidence chart proper |

### 5.1 `D=108`: the one literal discriminant collapse

In the translation gauge `p=pi^2-c`, the seven rational incidence pivots leave

```text
r60 = -jet2^2,
r70 =  2*jet1^2*jet2,
r71 = -2*jet2,
r80 = -c-jet1^4+9*jet1*jet2^2,
r81 =  2*jet1^2.
```

Already before localization,

```text
c = -(9/2)jet1*jet2*r71 -(1/2)jet1^2*r81 - r80.
```

Hence `disc(pi^2-c)=4c` belongs to the incidence ideal.  With
`L=Zc*c-1`, the readable localized identity is

```text
1 = -(9/2)jet1*jet2*Zc*r71
    -(1/2)jet1^2*Zc*r81 - Zc*r80 - L.
```

The frozen standalone replay verifies an inclusion-minimal reduced support
using `r80,r81,L`, and after back-substitution a ten-row raw support.  The raw
incidence ideal is not the unit ideal (`RAW_DIM=1` in the charged Singular
control); localization is essential.

In the ungauged nine-coordinate variant the two relevant residual equations
can be written

```text
r81 = b+2*jet1^2,       r80 = -c-jet1^4.
```

They give the explicit identity

```text
b^2+4c = (b-2*jet1^2)r81 - 4r80.
```

Thus `p=(pi-jet1^2)^2` modulo incidence and `[1,1]` collapses to `[2]`.
This is exact ideal membership, not merely a radical calculation.

It is also demonstrably special.  The negative control deletes the `-c` term
from the local-power-eight incidence row.  Then all retained `Hc` and jet
variables zero with `c=Zc=1` give a common zero of the perturbed support and
the localization row.  The inhomogeneous `-c` contribution from this exact
top form, weight cut, and truncation is what kills the chart.

### 5.2 `(99,66), delta=2`: `6264` is a pole/Jacobian residue

The exact certificate slice has one fixed-face incidence row, four pole rows,
three Jacobian rows, and no localization row.  After the charged rational
pivots the killing Jacobian row reduces to

```text
6264 = (-8)*(-783),       783 = e*A*(K-ell) = 27*(33-4).
```

Here `-8` is an affine pole-row offset and `29=33-4` is a band-index
complement.  Neither involves the root separation `rho`.  The charged integral
basis actually has 118 nonzero constant residual rows; `6264` is the first and
their gcd in that basis.  Row rescaling or a different pivot order changes such
a numerical representative.

Therefore the unlocalized ideal over `QQ[...,rho]` is already `(1)`.  It
contains `9rho^2` only in the vacuous sense that a unit ideal contains every
element.  No incidence calculation in this certificate forces `rho=0`.

### 5.3 `(99,66), delta=5/2`: `64` is a later Schur normal form

At the audited post-outer-`D_2`, common-`h3` quotient boundary, a 43-square
`B1` block consists of eight outer-`D_1` rows and 35 Jacobian rows.  Its pivot
determinant is a nonzero rational unit.  Reducing the pole row against this
block gives terminal scalar `64`; the support-minimal certificate retains that
pole row and six Jacobian rows.  The multipliers may depend polynomially on the
branch variable `c` (one displayed multiplier contains `-6525c`), but no
coefficient has a `c` denominator and the localization row `Zc*c-1` does not
occur.

Thus this unlocalized quotient ideal is also `(1)`.  The number `64` is an
exact normal form after 66 cumulative pivots, but the charged work supplies no
formula identifying it with `4c^3`.  Since one is constant and the other has
positive `c`-degree, they are not associates in the unlocalized polynomial
ring.

### 5.4 Same open is not the same element or mechanism

The exact common statement is

```text
D(9rho^2) = D(rho),       A[(9rho^2)^(-1)] = A[rho^(-1)],
D(4c^3)   = D(c),         A[(4c^3)^(-1)]   = A[c^(-1)].
```

But `9rho^2` is not a polynomial-ring unit multiple of `rho`, and `4c^3` is
not a polynomial-ring unit multiple of `c`.  After localization, of course,
every one of these elements is a unit and any two units are unit multiples of
one another.  Calling `6264` or `64` a “unit multiple of the discriminant” only
in that localized sense is tautological and has no invariant content.

The 3/3 fit is therefore a 3/3 match of **principal opens**, while the first
obstruction page and the certificate mechanism vary:

```text
D=108                  common-h3 incidence page; R in I;
(99,66), delta=2       fixed-face + pole/Jacobian page; 1 in I;
(99,66), delta=5/2     pole Schur page after 43 pivots; 1 in I.
```

## 6. What the ladder law does and does not prove

For a chart with

```text
F = K2^e + ...,
G = K2^f + B_j K2^(f-j) + ...,
in(K2)=y^A(y-x)^B,       K=A+B,
```

the lowest relevant `y`-index is

```text
k0 = A(e+f-j)-1.
```

The top-form computation derives the `B_j`-block contribution at the lowest
row,

```text
c_J(ell,k0) = +/- e*A*(jK-ell)
```

multiplying one alternating, or `x`-pure, functional on the `B_j` face.  For
the charged `(99,66)` support and pivot order, the reduced rows obey

```text
c_J(ell,k) = +/-[e*A*(jK-ell)-n(k-k0)],
```

and the dossier derives the 66 displayed coefficients after using that
branch's support cuts.  This explains the `783` factor in `6264`.

It does not give a universal kill, for four independent reasons.

1. The coefficient vanishes at `ell=jK`, and higher rows have their own
   resonances.  The ladder has a hard stop rather than a guaranteed unit.
2. The functional is available only when the relevant Tschirnhaus face has a
   nonzero `x`-pure coefficient.  In the `(16,12)` control that face is
   `y^2`-divisible and the predicted row is identically zero.
3. A Jacobian row setting a functional to zero is consistent.  The
   `(99,66),delta=2` contradiction occurs only because a branch-specific pole
   row sets the *same* functional to a nonzero affine value `-1`, producing the
   extra factor `8`.  No source theorem produces such a matching affine row for
   every datum.
4. The clean low-band formula requires all other tower blocks to begin later
   than the obstruction.  That is proved in the two charged `(99,66)` charts,
   where no live `A2,A3,B2,T2,T3` variable enters the certificate, but not for
   arbitrary skeletons.

The exact first-point operator from the frozen filtered calculation makes the
rank issue visible.  Assume

```text
d_3 divides d_2,       u_3+v_3=d_3,       gcd(u_3,v_3)=1,
0<=n<=d_2.
```

With

```text
H(w)=w^(u_3)(w-1)^(v_3),
A0=H^(d_2/d_3),       N=3d_2,
L_n(B)=N*A0*B'-(N-3n)*A0'*B,
```

solving the first-order equation gives

```text
ker L_n = 0                                      if d_3 does not divide n,
ker L_n = k*H^(d_2/d_3-n/d_3)                   if d_3 divides n.
```

The frozen script checks three instances of that analytic formula.  It gives
ranks `34/34` at `(99,66), n=4`, `33/34` at
`(99,66), n=11`, and `36/37` at `D=108, n=9`.  Thus even this symbolic
Jacobian block is not uniformly invertible.

Without the charged coprimality hypothesis, and still in the displayed range
`0<=n<=d_2`, solving `L_n(B)=0` gives more generally

```text
B = C*H^((d_2-n)/d_3),       C in k.
```

For `H=product_i(w-c_i)^(a_i)`, this is polynomial precisely when
`d_3` divides every `a_i(d_2-n)`.  A desk check with
`d_2=d_3=4`, `H=w^2(w-1)^2`, and `n=2` has the nonzero kernel generator
`w(w-1)`, even though `4` does not divide `2`.  The exponents here are the
first-point top-form multiplicities, not the later shared-leader `p(pi)`
partition.  This is a block-level counterexample to extending the coprime
kernel rule blindly; it is not asserted to be a complete admissible Moh
skeleton or a Keller pair.

The ladder and `L_n` formula are therefore valuable screens and pivot formulas,
but neither supplies the missing augmented-rank theorem.

## 7. The exact obstruction to MINOR-EMPTY

For a universal proof one must fix a complete datum

```text
(Moh skeleton, major tower, split order, multiplicity stratum,
 branch series, face normalization, centre/gauge parameters)
```

and construct its actual joint ideal `I_lambda`.  Then one must establish all
of the following uniformly.

### O1. A sourced common global coefficient chart

Moh Proposition 1.2 identifies roots of a local leader, Xu Proposition 7.3
handles the order-one linear power, and Corollary 7.5 handles a full simple
split in one contradiction proof.  None states that every later, partially
split datum has the same globally defined tower leader with the coefficient
incidence map used by the engines.  The special `(99,66)` and `D=108` maps were
compiled case by case.

### O2. A stratumwise polynomial presentation

`p_red`, the row generators, the root-permutation action, and the localization
must live in one declared ring.  A formula using `gcd(p,p')` across partition
boundaries is not such a presentation.  This is a typing prerequisite for even
stating `R in radical(I)`.

### O3. An invertible pivot block after localizing at `R`

A (possibly confluent) Vandermonde calculation may prove this part.  It would
show that packet equations are independent on the genuine locus.  Kernel and
resonance phenomena in Section 6 show that the required block and hypotheses
must be specified; the discriminant alone need not control every Jacobian
block.

### O4. A nonzero augmented Schur row

This is the decisive missing claim.  After the pivot block is inverted, one
must prove that the remaining incidence/pole/Jacobian rows generate `1`, or,
before localization, that they generate a power of `R`.  The affine right-hand
side depends on the split partition, physical branch series, face
normalization, jets, and low-tower coefficients.  The charged obstruction-core
report expressly records that the final Schur scalar is not determined by
`(d_s,u_s,V_s,delta,weights)` alone.

### O5. General low-band closure and certificate lift

The current small certificates work because other approximate-root blocks have
not entered by the killing page.  No uniform support-onset theorem guarantees
that for all data.  The `(99,66),delta=2` `C2/C3` inverse ledger, the
`delta=5/2` pre-`D_2`/pre-major lift, and the `D=108` pre-major row lift are
explicitly open at their earlier coordinate boundaries.  Exact certificates
at the declared quotients remain valid, but they cannot be promoted to an
arbitrary universal presentation by analogy.

### O6. Chart coverage and normalizations

The `(99,66)` necessity dossier has two chart-coverage gaps relevant even after
the split datum is fixed: simultaneous zeroing of the major and minor constant
centres is not supplied by the one available translation, and compatibility of
the `D_1` recentring scale with every other row family is unproved.  Its broader
degree statement also has census and split-exhaustiveness gaps.  The `D=108`
classification labels the global lift open, although the later gate establishes
the necessity of its post-major common-`h3` slice.

These are not six vague requests for “more computation.”  O4 is the exact
mathematical obstruction: nonzero discriminant proves that interpolation can
be performed, while MINOR-EMPTY needs a uniform theorem that the **augmented**
system is incompatible.  O1--O3 and O5--O6 are the hypotheses needed to make
that Schur statement a theorem about every required chart.

The smallest derived leading-ODE subsystem where the proposed mechanism breaks
is already the surviving `D=108,delta=3` face of Section 4.1: arbitrary squarefree
quadratic `p` solves the leader ODE.  The extra seven-coordinate global
incidence cut then kills that special chart.  Among the three frozen checked
flagship matrices, `D=108,n=9` has an exact one-dimensional kernel.  Neither is
a surviving full Keller chart, so no counterexample to universal MINOR-EMPTY
is claimed.

## 8. What can be stated as a theorem now

**MINOR-EMPTY, fixed-datum conditional form.**  Let `k` be algebraically closed
of characteristic zero.  Fix a fully sourced principal-minor split datum with
`u_s>=2`, a multiplicity vector `lambda` of length at least two, a common
coefficient chart `A_lambda`, its proved necessary ideal `I_lambda`, and

```text
R_lambda = disc(product_i(pi-c_i)).
```

If `R_lambda in radical(I_lambda)`—equivalently if some power of `R_lambda`
lies in `I_lambda`—then the genuine split chart
`V_A(I_lambda) intersect D_A(R_lambda)` is empty.

This theorem is unconditional algebra once its hypothesis is checked.  The
three charged computations instantiate it with kill orders

```text
(99,66), delta=2       N=0, because 1 in I;
(99,66), delta=5/2     N=0, because 1 in I;
D=108, delta=3         N=1, because R in I_inc.
```

They do not prove the hypothesis for every datum.  A suitable theorem-sized
next target is therefore:

> **Fixed-partition augmented-rank lemma (missing).**  For every admissible
> principal-minor datum and every multiplicity vector of length at least two,
> construct the sourced global joint presentation over the ordered-root cover.
> Prove over `A_lambda[R_lambda^(-1)]` that the appropriate augmented
> maximal-minor/Fitting ideal is the unit ideal; equivalently, prove directly
> that the residual Schur ideal is `(1)`.  Generic or fiberwise rank alone is
> not sufficient over the parameter ring.

Clearing the Vandermonde denominators would then give a power of
`disc(p_red)` in the unlocalized ideal and prove the desired MINOR-EMPTY
statement.  Merely computing the Vandermonde determinant proves only the pivot
half and is insufficient.

## 9. Frozen evidence map

The following map gives the exact frozen provenance for the nontrivial inputs
to the verdict.  Line numbers refer to the frozen Markdown/Python copies under
the receipt's `lane_inputs_dir`; PDF references are printed page numbers.

| assertion used here | frozen provenance |
|---|---|
| split definition; packet factors | Xu pp.1--2; Moh Proposition 1.2, p.147 |
| order-one common linear power | Xu Proposition 7.3, pp.10--11 |
| full-simple-split exclusion and (7.1) | Xu Corollary 7.5, pp.11--12 |
| `(99,66)` face survivors | Xu Section 8, pp.12--13 |
| coherent system and order inequalities | Moh Definition 1.4, p.148; Theorem 1.2, p.149 |
| three discriminants and localization opens | `minor-residue-formula-opus5-20260903.md:158-195` |
| `6264` ladder/pole calculation | same file, lines 93--143 and 314--345 |
| `64` status and scope | same file, lines 145--156; `two-place-obstruction-core-sol56-20260903.md:572-590` |
| three certificate boundaries and page rule | `two-place-obstruction-core-sol56-20260903.md:6-52,542-663` |
| `D=108` residuals and localized certificate | same file, lines 430--534; `d108_certificate.py:185-367` |
| `(99,66)` chart necessity and ladder pivots | `g9966-chart-necessity-opus5-20260903.md:476-700` |
| `(99,66)` remaining coverage gaps | same file, lines 821--854 |
| `D=108` common-leader source audit and controls | `g108-delta3-kill-gate-gpt55-20260903.md:140-210,258-276` |
| first-point operator, Schur identity, ranks | `filtered_obstruction.py:24-106`; `two-place-obstruction-core-sol56-20260903.md:597-663` |
| `u_s=1` control | `minor-residue-formula-opus5-20260903.md:197-285` |

The charged `g108-minor-classification-opus5-20260903.md:137-220`
supplies the derived `D=108` face ODE and split tree; its lines 385--399 retain
the global-lift qualifications.  `FALLACY-v2.md:1-36` supplies the reasoning
guardrails audited below.

## 10. Controls and FALLACY-v2 audit

### `u_s=1`

The `(16,12)` chart is the Proposition 6.3 descent of `(64,48)` and has
`u_s=1`.  Its leader is linear and has no genuine split stratum; under the usual
convention its squarefree discriminant is `1`.  Its separate localized chart
is empty with kill order two, but the `(99,66)` `x`-pure ladder functional
vanishes there.  This is neither confirmation nor refutation of a theorem
whose hypotheses require at least two packets.

The tame affine control

```text
F=a*x+y,       G=(a-1)*x+y,       J(F,G)=1
```

survives, as it must.  It is outside the `s=3` two-point tower, so a
principal-minor `u_s` split datum is not applicable and the proposed
discriminant machinery is not applied to it.

### Guardrails

- **Flag/place/series:** the major tower, the physical principal-minor place,
  the cover coordinate, the split order, the pole filtration, and the
  Jacobian homogeneous filtration are not identified.
- **Floor/attainment:** Moh Theorem 1.2 is used only for lower bounds and
  strictly-below vanishings.  No at-level face is inferred without a separate
  source.
- **Carrier/attainment:** source-level ODE solutions are explicitly not Keller
  witnesses or full actual exits.
- **Pole/interior:** pole rows are used only in the two declared `(99,66)`
  branch charts; no universal pole row is invented.
- **Localization:** no `sat()` is used.  The exact criterion is stated with
  `A[R^(-1)]`, and the `D=108` certificate uses the Rabinowitsch row
  `Zc*c-1` with raw/empty/perturbation controls.
- **Raw remainder:** `6264` and `64` are typed as normal forms at their declared
  quotient boundaries, not invariant residue values.  The zero
  `minor_n8_pi2` row is checked by the standalone `D=108` script.
- **Variable/ring map:** `p_red` is defined on a fixed root stratum, and equality
  of principal opens is not called association in the unlocalized polynomial
  ring.
- **Prime/derivative:** every prime in the ODE and `L_n` formulas means
  differentiation in the displayed variable; `p_red` never denotes a
  derivative.
- **Fit/proof:** the 3/3 localization match is reported as such.  The one
  discriminant membership, two unit certificates, source-level ODE identities,
  and matrix kernels are kept distinct.
- **Exit charge:** no exit-price assertion is made, so no `charge_basis` line is
  emitted.

## 11. Final status

The answer to the final question is two-part:

1. **Yes:** once a fixed multiplicity stratum is genuinely split, its distinct
   packet centres make `disc(p_red) != 0` automatically.  Thus a proved
   universal radical-containment theorem would make MINOR-EMPTY unconditional
   on that stratum.
2. **No theorem is presently available:** genuineness is an open condition,
   not an equation in the necessary ideal.  Moh's order inequalities and Xu's
   leader ODE allow nonzero-discriminant faces; Vandermonde invertibility solves
   the packet interpolation block.  What is missing is the additional,
   uniformly incompatible Schur row.

Accordingly the flagship promotion must remain

```text
OPEN[UNIVERSAL-MINOR-EMPTY-DISCRIMINANT].
```

The exact safe replacement is Theorem 2.1 plus the three typed branch
certificates above.  Promoting the 3/3 match to a universal theorem would be the
FALLACY-v2 3/3-fit error the lane was designed to avoid.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `35434`.
- Body SHA-256:
  `23a60bd280cfcd7c211ee3fb03f97762f4f697b2174c94da4ba3fbe1d645eb0e`.
- Frozen basis: `158179af4a89e193c843f823bdea21396af1920c`.
