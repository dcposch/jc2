# K16 ray theorem (T): Newton/Lemma 2.1 audit and the `t=2` coefficient attack

**Lane:** `k16-ray-T-newton-sol56-v3-20260903`  
**Date:** 2026-09-03  
**Verdict:** **PROVED at `t=2` only — SATURATED-EMPTY.** The Newton polygon and
Lemma 2.1 support are compatible for every `t>=1`; they do not prove uniform theorem
(T). A source-corrected, two-disc approximate-root necessary chart for `t=2` has
30 unknowns and 37 equations; three safe target gauges reduce it to 27 unknowns,
and its exact `c!=0` saturation has reduced basis `[1]`.  
**Scope:** no ledger edit; no `jc2-lean`; no uncharged ideation file read; new drivers
only in `box/k16T-drivers-20260903/`.

Claim labels in this report are literal: **SOURCE-READ** means the frozen Moh PDF page
was rendered/read; **DERIVED** is a mathematical consequence displayed here;
**MEASURED** is a reproducible program result; **PROVED-HERE** is a checked exact
calculation or proof in this lane. `OPEN[...]` is not filled by analogy.

## 0. Custody and fail-closed gate

**MEASURED.** I read the lane receipt
`xmodel/k16-ray-T-newton-sol56-v3-20260903.run.v2` and mechanically formed the
`sha256sum -c` input with `awk`, pairing each
`charged_input_<i>_sha256` with `charged_input_<i>_basename` under
`/tmp/jc2-lane.9i8ktP/inputs/`. All **11/11** checks returned `OK`. No hash was
retyped. The stop-on-content-mismatch gate did not fire.

**SOURCE-READ.** The frozen PDF has 74 PDF pages; printed journal page `N` is PDF page
`N-139`. Pages rendered or directly read here were printed pp.149, 151, 173-181 and
205-212. In particular, the formulas suppressed by OCR on pp.149, 151, 179 and
207-211 were checked against page images.

## 1. What Lemma 2.1 actually pins

### 1.1 Constant Jacobian: Moh's statement

**SOURCE-READ (Moh p.151).** Let `f(x,y),g(x,y) in k[x,y]` be monic in `y`, of
`y`-degrees `m,n`. Moh chooses a formal root parameter by

```text
g(x,y) = eta^(-n),
f(x,y) = eta^(-m) + sum_{i>-m} f_i(x) eta^i.
```

Then `J_{x,y}(f,g)=c in k*` if and only if

```text
ord_eta( sum_i f_i(x)eta^i - sum_i f_i(0)eta^i ) = n-1,
deg_x f_{n-1}(x) = 1.
```

The proof gives the equivalent coefficient statement

```text
f_i'(x)=0  for every i<n-1,
f_{n-1}'(x) is a nonzero constant.
```

It uses

```text
J_{x,y}(f,g)
 = n (sum_i f_i'(x) eta^i) (eta^(-n+1) + higher eta terms).
```

Immediately afterward Moh notes that `f_{n-1} != 0` and
`gcd(n,n-1)=1` give `M_i<=n-1`, then explicitly says that the values of the
`M_i` are poorly understood. This is an upper terminal bound, not a theorem that
identifies `M_2`.

### 1.2 Monomial Jacobian `c gamma`

**DERIVED / PROVED-HERE.** Repeat the displayed chain-rule proof with `x=gamma` and
`J(f,g)=c gamma^k`. Coefficient comparison gives

```text
f_i(gamma) in k                       (i<n-1),
f_{n-1}'(gamma) = nonzero_scalar*gamma^k,
f_{n-1}(gamma) = nonzero_scalar*gamma^(k+1) + constant.
```

For this ray `k=1`, so `deg_gamma f_{n-1}=2`. Swapping the ordered pair and using a
*different* formal parameter `tilde_eta` with `f=tilde_eta^(-m)` gives separately

```text
g_j(gamma) in k                       (j<m-1),
deg_gamma g_{m-1}=2.
```

In the requested degree notation this specializes precisely to

```text
Q=eta^(-(8t+4)):
  P=eta^(-(12t+4))+sum p_j(gamma)eta^j,
  p_j in k for j<8t+3,       deg_gamma p_(8t+3)=2;

P=tilde_eta^(-(12t+4)):
  Q=tilde_eta^(-(8t+4))+sum q_j(gamma)tilde_eta^j,
  q_j in k for j<12t+3,      deg_gamma q_(12t+3)=2.
```

At either anchor the coefficient is a nonzero scalar times `gamma^2`, plus an
arbitrary constant.

**PROVED-HERE (scope correction).** These are Laurent coefficients in the formal root
parameter of the *other polynomial*. Lemma 2.1 does not say that the ordinary
coefficients of `pi^j` in `P(gamma,pi)` or `Q(gamma,pi)` are constant, and the two
reciprocal conclusions do not live in one common Laurent parameter. Calling the
quadratic term the “unique gamma-dependent coefficient” is also too strong: the
lemma constrains all indices below the anchor and the anchor itself, but says nothing
about later indices. This parameter/ring distinction is essential below.

### 1.3 Negative 4-tuple control

**PROVED-HERE.** Take the pair, monic in `pi`,

```text
(f,g)=(pi, pi-gamma^2/2).
```

Then `J_{gamma,pi}(f,g)=gamma`. With `g=eta^(-1)`, one has
`f=eta^(-1)+gamma^2/2`; hence `n=1`, the Lemma-2.1 monomial analogue has its
anchor at `n-1=0`, and `deg_gamma f_0=2`. Thus the lemma shape **passes**. The
reciprocal parameter `f=tilde_eta^(-1)` gives
`g=tilde_eta^(-1)-gamma^2/2`, so the swapped anchor also has degree `2`. The
pair has neither degrees
`(12t+4,8t+4)` nor `d_2=4`, `M_2=n-3`, `V_2=3`, so the K16 4-tuple classifier
**fails**. Driver output records exactly this separation; the control is not inserted
into the fixed-degree ideal.

## 2. Appendix II, read without promoting its controls

### 2.1 What Moh prints for `(16,12;13;3;X)`

**SOURCE-READ (pp.207-209).** Proposition 6.3/6.4 descent gives the first table row

```text
n=16, m=12, M_2=13, V_2=3, delta_2=-1, delta_1=1/4, Jacobian=X.
```

Moh starts with 244 coefficients. He chooses two coherent `pi`-roots, one in the
major disc and one in the minor disc, and Theorem 1.2 writes

```text
P = h^4 + alpha_1 h^3 + alpha_2 h^2 + alpha_3 h + alpha_4,
Q = h^3 + beta_2 h + beta_3,
deg_pi alpha_i, deg_pi beta_i <= 3.
```

The order inequalities yield

```text
h = pi^3(pi-gamma)+b1*pi^3+b2*pi^2+b3*pi+b4
  = pi*A+b4 = pi^2*B+b3*pi+b4,
```

and short `A,B,pi-gamma` expressions for the `alpha_i,beta_i`; Moh reports a
reduction to 17 coefficients. Target translations and the Laurent expansion of `P`
in `Q^{-1/12}` reduce this further to 10.

**SOURCE-READ (important limit).** Moh does **not** display the final 10 equations,
an elimination, or a certificate for this row. The explicit case split on pp.210-211
is the different row `(15,10;11;3;X^2)`. The closing sentence asserts that all other
cases can be computed similarly. Therefore “Moh hand-kills the `(16,12)` row” is
source-supported only at the level of his conclusion plus the 244-to-17-to-10
reduction, not as a printed auditable certificate.

### 2.2 Independent positive control in this lane

**PROVED-HERE / MEASURED.** `moh1612_control.py` uses the p.208 chart but gives the
apparently repeated `c_5` coefficients of `A` and `B` in `alpha_3` independent
parameters. This is a slightly larger chart, hence a safer emptiness test. With the
top-line coefficient normalized to `-1`, it has 18 polynomial parameters, the
Jacobian scalar `c`, and 23 exact `h`-adic coefficient equations for
`J(Q,P)=c gamma`. In

```text
R = Q[b1,b2,b3,b4,u1,...,u14,c,T],  degree-reverse-lexicographic order,
I = <23 coefficient equations, T*c-1>,
```

Singular 4.3.2 returns

```text
basis size 1
G[1]=1
MOH1612_SATURATED_EMPTY
```

in under one second. This is the required `t=1` positive control. It is a new exact
certificate on the enlarged p.208 chart, not a claim that Moh printed this basis.

## 3. Symbolic characteristic and Newton data for every ray member

Fix the ray parameter `t>=1` (not the local uniformizer) and put

```text
n=12t+4,  m=8t+4,  M_1=-m,  M_2=n-3=12t+1,  V_2=3,  k_jac=1.
```

### 3.1 Gcd chain, tuple level, and the Lemma anchor

**PROVED-HERE.** Euclid gives

```text
d_2=gcd(n,m)=4,
d_3=gcd(4,M_2)=gcd(4,12t+1)=1,
e=n/4=3t+1,  d=m/4=2t+1.
```

In Moh's `eta=P^{-1/n}` expansion of `Q`, `M_2` is the first exponent whose nonzero
coefficient breaks divisibility by `d_2=4`. The requested datum is realized at the
support level by a nonzero *constant* coefficient at

```text
M_2=n-3 < n-1.
```

Lemma 2.1 permits that constant and places the forced quadratic coefficient two
indices later, at `n-1`. Equivalently, in the reciprocal
`tilde_eta=Q^{-1/m}` expansion of `P`, the exponent dictionary gives

```text
N=M_2-(n-m)=m-3=8t+1,
```

again a permitted nonzero constant, followed two indices later by the quadratic
anchor at `m-1`.

**PROVED-HERE.** Consequently the proposed Lemma/Newton contradiction does not occur:

```text
(n-1)-M_2 = 2,
(m-1)-N   = 2.
```

The datum is compatible for all `t`, including `t=1`; compatibility is not
attainment.

### 3.2 `V_2`, top face, and Puiseux separations

**SOURCE-READ + DERIVED.** Definition 5.1/Proposition 5.3 requires for the sole
`D_2 -> D_1` extension

```text
V_3*d_2/d_3 >= V_2 > d_2/(n-M_2),  V_3=d_3=1,
4 >= 3 > 4/3.
```

Thus `V_2=3` is allowed, not forced by Lemma 2.1. Definition 5.1(1) gives the
major-disc root counts

```text
P: (n/d_2)V_2 = 9t+3,     complement n/4 = 3t+1,
Q: (m/d_2)V_2 = 6t+3,     complement m/4 = 2t+1.
```

After a linear normalization the common top approximate root is

```text
h_top=pi^3(pi-a*gamma),  a!=0,
P_top=h_top^(3t+1)=pi^(9t+3)(pi-a*gamma)^(3t+1),
Q_top=h_top^(2t+1)=pi^(6t+3)(pi-a*gamma)^(2t+1).
```

**DERIVED.** In `(gamma exponent, pi exponent)` coordinates the forced top segments
have endpoints

```text
NP(P): (0,12t+4) -- (3t+1,9t+3),
NP(Q): (0, 8t+4) -- (2t+1,6t+3).
```

Both have ordinary edge slope `-1`. The two tangent directions are `pi=0` and
`pi=a gamma`; their cross-disc logarithmic separation is `delta_2'=-1`. The next
major-disc separation `delta_1'` is computed in §4. These segments and separations
do not specify every lower Newton face.

## 4. Definition 5.1, Phi, Proposition 5.3, and descended (8)-(13)

### 4.1 Radius calculation

**SOURCE-READ (Moh p.179).** For a major tower, Definition 5.1(3) says

```text
delta_i^51 = 1
 - (n-M_i) prod_{j=i+1}^s [V_j(n-M_j)-d_j]
   / ((n-M_s-1) prod_{j=i+1}^s [V_j(n-M_{j-1})-d_j]).
```

For `s'=2`, the ray data give

```text
delta_2^51 = -1/2,
delta_1^51 = t/[2(3t+1)].
```

**DERIVED using the banked Phi rule.** Since `k_jac=1`, conversion to geometric
`ord_{gamma^{-1}}` radii multiplies by `k_jac+1=2`:

```text
(delta_2',delta_1')=(-1, t/(3t+1)).
```

**MEASURED.** `k16_symbolic.py` declares `t` as a positive integral Sympy symbol and
simplifies the displayed identities before making any numerical specialization. Its
control substitutions include

```text
t=1: (-1,1/4),
t=2: (-1,2/7).
```

**SOURCE-READ / DERIVED.** Proposition 5.3 is used nontrivially once: it extends the
base disc `D_2` to `D_1` using the multiplicity `V_2=3` and the displayed window.
There are no intermediate `r>=3` sibling-extension stages when `s'=2`.

### 4.2 Conditions (8)-(13)

**DERIVED.** With geometric radii, the lcm of the reduced denominators above
`delta_1'` is `1`, so condition (8) gives

```text
A_1=denominator(delta_1')=3t+1=e.
```

Conditions (9)-(11) have an empty intermediate index range. The bottom alternative
(12) holds identically:

```text
A_1 | (n/d_2)V_2       because 3e,
A_1 | (m/d_2)V_2 - 1   because 3(2t+1)-1=2e.
```

Alternative (13) fails for every `t>=1` because its two numbers are `2e+1` and
`3e-1`. Thus the descended (8)-(13) were explicitly evaluated and used as a
**compatibility check**; they give no obstruction. Phi was used both here (to obtain
`A_1`) and in the `t=2` order truncation below.

## 5. The `t=2` approximate-root truncation

### 5.1 The source-correct order bound

Set `(n,m;M_2,V_2)=(28,20;25,3)` and `delta_1'=2/7`.

**SOURCE-READ (Moh p.149, Theorem 1.2).** If a coherent complete system has accuracy
`lambda` and `h` is its quasi-approximate root of exponent `r`, the coefficient at
`h`-deficit `i` has order at every coherent root at least `(lambda/r)i`.

**DERIVED.** For `P`, the two coherent-root multiplicities are `(21,7)`, so

```text
lambda_P = 21*(2/7)+7*(-1) = -1,
lambda_P/7 = -1/7.
```

For `Q`, they are `(15,5)`, so

```text
lambda_Q = 15*(2/7)+5*(-1) = -5/7,
lambda_Q/5 = -1/7.
```

Hence both coefficient families obey `ord C_i >= -i/7`. Using
`-i*delta_1'=-2i/7` would be a weaker necessary superset; it is not the source's
sharp Theorem-1.2 truncation. At `t=1` the two values coincide, which explains why
this distinction is easy to miss.

### 5.2 A 30-variable necessary chart

Normalize the nonzero top-line coefficient and define

```text
z=pi-gamma,
B=pi*z+b1*pi+b2,
A=pi*B+b3,
h=pi*A+b4=pi^4-gamma*pi^3+b1*pi^3+b2*pi^2+b3*pi+b4.
```

**PROVED-HERE.** The `V_2=3` face has `a!=0`; the invertible linear scaling
`gamma -> a*gamma` sets `a=1` and only rescales the free nonzero Jacobian constant.
Thus the top leading-coefficient localization loses no target point. The remaining
nonvanishing condition `c!=0` is saturated explicitly below.

**DERIVED / PROVED-HERE.** Intersecting the order bound at the major and minor
coherent roots gives the following coefficient spaces:

At the major root,
`ord(1,A,B,z,gamma)=(0,-3/7,-5/7,-1,-1)`; at the normalized minor root,
`1,z` have nonnegative order and `A,B` have positive order. Comparing these values
with `-i/7` gives the table without dividing by any parameter-dependent leader.

| deficit `i` | basis | dimension |
|---:|---|---:|
| 1 | `1` | 1 |
| 2 | `1` | 1 |
| 3 | `1,A` | 2 |
| 4 | `1,A` | 2 |
| 5 | `1,A,B` | 3 |
| 6 | `1,A,B` | 3 |
| 7 | `1,gamma,A,B,z` | 5 |

Write

```text
P=h^7 + sum_{i=1}^7 alpha_i h^(7-i),
Q=h^5 + sum_{i=2}^5 beta_i h^(5-i).
```

The missing `h^4` term of `Q` is the Tschirnhausen/approximate-root normalization.
The table gives `17` alpha parameters and `1+2+2+3=8` beta parameters. With four
`b_i` and the Jacobian scalar `c`, this necessary-chart upper-bound count is

```text
4 + 17 + 8 + 1 = 30 unknowns.
```

This is the requested rigorous upper bound after the order conditions: adding every
Lemma/tower Laurent condition can only lower it. The exact post-Lemma moduli count is
`OPEN[DESCENT-ANCHOR]`, because those Laurent coefficients have not yet been mapped
into this polynomial chart. The empty necessary superset below makes that missing
count irrelevant for the `t=2` nonexistence proof.

**PROVED-HERE (safe gauges).** First subtract the scalar part of `beta_5` from `Q`.
Next, since `alpha_2` is a scalar, replace `P` by `P-alpha_2 Q`; the induced changes
`alpha_4-alpha_2 beta_2`, ..., `alpha_7-alpha_2 beta_5` remain in their displayed
filtration spaces. Finally subtract the scalar part of the new `alpha_7` from `P`.
This invertible triangular target change has determinant one, preserves `J(Q,P)`,
monicity, degrees and the two-disc filtration, and reduces the solver chart to

```text
26 polynomial parameters + c = 27 unknowns.
```

In the reciprocal Laurent expansion, the `P-alpha_2 Q` change starts at exponent
`-m=-20`, divisible by `4`, so it cannot manufacture an earlier non-`4`-divisible
anchor term. The two constant shifts are invisible to the infinity characteristic
data.

**DERIVED (uniform count).** For general ray parameter `t`, Theorem 1.2 gives the
common bound `ord C_i>=-i/(3t+1)`. The both-disc dimensions are `1` through `i=t`,
`2` through `2t`, `3` through `3t`, and `5` at `i=3t+1`. Hence the ungauged
coefficient count including `c` is `9t+12`. This is linear growth, not a uniform
obstruction.

### 5.3 Exact Jacobian equations

**PROVED-HERE.** For terms `a h^r,b h^s`, the driver uses the identity

```text
J(a h^r,b h^s)
 = h^(r+s)J(a,b)
 + h^(r+s-1)[s b J(a,h)+r a J(h,b)].
```

It sums all pairs, then Euclidean-divides each coefficient by the monic polynomial
`h` in `pi`, carrying the quotient to the next `h`-power. No leading coefficient is
divided out and no zero-leader branch is discarded. For the gauged 27-variable
chart, equating the four remainder coordinates to `c gamma` gives, **MEASURED**:

```text
37 scalar equations at h-levels 0..9,
parameter degrees: 1:1, 2:6, 3:16, 4:14,
6395 bytes of generator text.
```

The driver uses `J(Q,P)=c gamma`; the requested convention `J(P,Q)=c gamma` differs
only by replacing the unrestricted nonzero scalar `c` with `-c`.

The declared Singular ring is over `Q`. For the decisive gauged run, generator order
is exactly the 26 surviving chart parameters, `c`, then the Rabinowitsch variable
`T`, with degree-reverse-lexicographic monomial order. The main ideal is

```text
I=<37 coefficient equations, T*c-1>.
```

The top-line coefficient is already normalized to `-1`; `T*c-1` selects the required
nonzero-Jacobian component. The still-untranslated tuple-level Laurent coefficient is
discussed next; it is not the Lemma anchor and is not silently called `c`.

## 6. Saturation, controls, and bounded result

### 6.1 Wrapper and semantic controls

**MEASURED.** Before the main standard basis, the generated Singular program runs in
the identical declared ring:

```text
EMPTY wrapper:    <c, T*c-1>       -> reduce(1,G)=0       PASS
NONEMPTY wrapper: <c-1, T*c-1>     -> reduce(1,G)!=0      PASS
```

The independent actual-pair control `(pi,pi-gamma^2/2)` is monic in `pi`, passes both
reciprocal monomial Lemma shapes, and fails the 4-tuple, as §1.3 requires. The Moh
`t=1` enlarged-chart
control returns `[1]`, as §2.2 requires. Thus neither an always-empty wrapper nor an
over-broad tuple classifier can explain the main result.

### 6.2 Main `t=2` certificate

**MEASURED / PROVED-HERE.** Singular 4.3.2, one core, exact rational arithmetic,
completed the gauged main ideal with

```text
chart unknowns (including c)     27
Rabinowitsch variables            1
Jacobian coefficient generators 37
total ideal generators           38
reduced standard-basis size       1
reduced basis                  G[1]=1
wall time                      37.33 s
maximum resident set           40060 KiB
process exit status                0
```

The complete generated Singular program is 7,315 bytes with SHA-256

```text
6234d5ffa0a4f278eed2940062abedac749cf63c7d8326e0dad927401227414d
```

and the 37 equation expressions occupy 6,395 bytes before wrapper/program syntax.
Thus the certificate is the one-polynomial, one-term reduced basis `[1]`; its
reproducible input size is 38 generators / 7,315 bytes. The captured result and
resource line are in `box/k16T-drivers-20260903/t2_sat_certificate.txt`.

**PROVED-HERE.** Every target pair belongs, after the safe coordinate/target
normalizations, to this Theorem-1.2 order chart. The chart deliberately omits the
extra tuple-level Laurent bridge equations and is therefore a superset. Unit ideal for
this superset's `c!=0` component implies unit ideal for the requested
`(28,20;M_2=25,V_2=3;J=c gamma)` component. Hence theorem (T) is proved at `t=2`.
The identity `1 in I` is over `Q`; scalar extension preserves that identity over
every characteristic-zero coefficient field used by Moh.

**MEASURED (non-result retained for audit).** Before the three target gauges, the
30-unknown version did not finish within 600 seconds (about 104 MiB observed RSS).
That timeout is not used in the proof. An earlier deliberately weak 54-variable
radius-bound superset likewise timed out at 120 seconds; source-reading Theorem 1.2
corrected its bound before any promotion. The decisive result is only the sharp,
gauged 27-unknown run above.

## 7. `OPEN[DESCENT-ANCHOR]`: exactly where it bites

**PROVED-HERE (arithmetic check).** The denominator in Definition 5.1 is

```text
n-M_2-1 = (12t+4)-(12t+1)-1 = 2 != 0.
```

Thus the Phi calculation is nonsingular. But the same equality places `M_2` two
Laurent indices *before* Lemma 2.1's quadratic anchor. Nonzero denominator does not
identify those coefficients.

For `t=2`, in `tilde_eta=Q^{-1/20}`,

```text
P=tilde_eta^(-28)+sum_j p_j(gamma)tilde_eta^j,
N=17.
```

Under the reciprocal exponent dictionary, realization of the exact 4-tuple would
require all earlier non-`4`-divisible `p_j` to vanish and the **tuple-level**
coefficient `p_17` to lie in `k*`; separately, Lemma 2.1 gives `p_j in k` for
`j<19` and `deg_gamma p_19=2`. Thus `p_17` is not the Lemma anchor: that anchor is
`p_19` in this reciprocal parameter (and is at index `27` in the opposite
parameterization). Between indices `-27` and `16` there are 33 earlier
nonmultiples of `4`. Turning the asserted tuple-level condition on `p_17` and those
33 vanishings into polynomials in the 30-variable necessary chart requires the
explicit truncated Laurent ring map. That bridge is not supplied by Lemma 2.1 and
has not been proved here.

**Logical effect.** The order-filtered chart is a necessary **superset**. Its `c!=0`
saturation is empty, so `t=2` is empty a fortiori and the tuple-level bridge is
unnecessary for that proof. `OPEN[DESCENT-ANCHOR]` therefore does **not** bite on the
empty branch. It
would bite on every nonempty/surviving branch and on any attempted representative:
no such solution could be promoted until the 33 vanishings and `p_17!=0` were
checked. It also remains open for a uniform-in-`t` coefficient proof.

## 8. Typed verdict and OPEN accounting

The promotions are limited exactly as follows:

- **PROVED-HERE:** Lemma/Newton support compatibility for all `t`; Phi radii; the
  `(8)-(13)` evaluation; the `t=1` enlarged-chart `SATURATED-EMPTY` control; and
  `SATURATED-EMPTY` for the complete necessary order chart at `t=2`.
- **VERDICT:** **PROVED at `t=2` only (`SATURATED-EMPTY`, reduced basis `[1]`, 38
  input generators, 7,315 input bytes).**
- **NOT PROVED:** theorem (T) for all `t`; existence/nonexistence for `t>=3`; any
  lift back to a Keller pair. The `t=1` result is a control, not a uniform induction.
- **OPEN[DESCENT-ANCHOR].** Bounded quantity at `t=2`: 33 pre-tuple-level
  nonmultiple vanishings plus one nonzero tuple-level `p_17`, conditional on the
  reciprocal exponent dictionary; the post-Lemma chart has at most 30 variables
  before, and at most 27 after, the safe gauges. Obtain the Laurent data through index
  17 (relative order 45; continue to 19 to audit the distinct Lemma anchor). Cheapest test:
  put `xi=h^{-1/4}`, solve
  `h(gamma,Y(xi))=xi^{-4}` by its constant-pivot-4 recurrence, form
  `B_Q=xi^20 Q(gamma,Y)=1+O(xi^8)`, set
  `tilde_eta=xi B_Q^{-1/20}`, revert that unit series, and expand
  `xi^28 P(gamma,Y)` through relative order 45. Under that dictionary, `p_17` is
  the order-45 coefficient. Verify the map by recomposition and add a separate
  Rabinowitsch variable for `p_17`; never divide by a parameter-dependent pivot.
- **OPEN[T-UNIFORM-COEFFICIENT].** Bounded at fixed `t` by `9t+12` ungauged unknowns.
  Cheapest next test after `t=2`: exploit the three safe target gauges and the
  banded `h`-adic identity before attempting a generic-`t` recurrence.

**FALLACY-v2 audit.** No screen is called attainment. The formal Newton/characteristic
compatibility is not a polynomial pair. The actual monomial-Jacobian control is not
promoted into the 4-tuple. Saturation is by an explicit Rabinowitsch generator in a
declared ring and has empty/nonempty wrapper controls. Monic `h`-division handles zero
remainders and needs no vanished-leader branch. Prime marks on descended data are
labels. No exit-price assertion is made, so no `charge_basis` line is due.

## 9. Reproduction

```bash
python3 box/k16T-drivers-20260903/k16_symbolic.py
python3 box/k16T-drivers-20260903/moh1612_control.py
python3 box/k16T-drivers-20260903/moh1612_control.py --emit-singular | Singular -q
python3 box/k16T-drivers-20260903/t2_order_system.py
python3 box/k16T-drivers-20260903/t2_order_system.py --gauged
python3 box/k16T-drivers-20260903/t2_order_system.py --gauged --emit-singular | Singular -q
```

**MEASURED.** The main saturation command is bounded externally in the recorded run by
`timeout 600s`; it completed before the bound.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23318`.
- Body SHA-256:
  `86504cd4be357bba7f1b7d7724c391e5d724e65ba64f35c4650b33f10fa3e674`.
- Frozen basis: `79c0cd4de1d680f4d2e36d3c447b911e5b5a0db1`.
