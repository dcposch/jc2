# Hostile review: D25 triangular certificate (sol-ideas-0821 items 1–2 + 9.S2)

Reviewer: Grok 4.6 (hostile referee, verdict tier). Date: 2026-08-21.
Repo: `/Users/dc/code/math/jc72108`. No git. No file changes except this
review.

Targets:

- `xmodel/sol-ideas-0821.md` items 1–2 (pivot certificate + carrier /
  point claims).
- `SHEET6-DIRECTIONB.md` §9.S2 (independent mechanical replay).
- `cases/d25_certificate_replay.json` (the replay that CONFIRMED it).

Claim under review: at modular scope (p = 105337 and 105673;
emission-fidelity caveat inherited from section 9), every parked D25
fiber system is 16 disjoint copies of \(\mathbb A^{14}\) over
\(\mathbb F_p\) (2 lift pivots with minor unit\(\cdot uW_1^2 uW_2^2\)
+ 8 Laurent-unit base pivots, DAG well-founded, hcore/hlin
ideal-membership from raw rows), hence NONEMPTY of dimension 14; union
= 576 copies; explicit witnesses vanish 34/34 per fiber; Jacobian
ranks 14/18; the pre-registered ECO-D25 prediction is refuted.

Method: independent `python3` parser and exact \(\mathbb F_p\) sparse
arithmetic on the raw emitted `cases/d25fam_p{105337,105673}*.ms`
(74 files; paren-free msolve format). Own unit-linear greedy DAG, own
Cramer left kernel, own Jacobian, own selector specialization. No
Singular, no msolve, no reuse of Sol transcript code, no reuse of the
replay agent’s code. Local sha256 of all 74 files matched the replay
JSON (0 mismatches); box01 was not re-sshed. No other repo file
modified.

**VERDICT: CONFIRMED.** The emitted modular schemes are 16 disjoint
copies of \(\mathbb A^{14}_{\mathbb F_p}\) on every one of the 72
parked fibers, dimension 14, NONEMPTY; the two selector unions are
576 copies of \(\mathbb A^{14}\). ECO-D25 is refuted at both
registered primes by the lock table’s own “NONEMPTY, dimension 14”
row. Attack (2) (hidden relations among the 14 residual variables)
fails: after 10 unit-linear pivots the only remaining equations are
two separable quartics in \((W_1,W_2)\). Attack (3) (Laurent-unit
pivots secretly saturating a vanishing \(uW\)) fails: the inverse
rows \(W_i uW_i-1\) are among the 34 emitted generators, so \(W,uW\)
are units on the entire affine scheme. §9.S2 states modular +
emission-fidelity + chart scope honestly. Residual nits below do not
flip the identification or the ECO-D25 refutation.

The load-bearing sentence is `SHEET6-DIRECTIONB.md:2402-2408`: at the
registered modular scope, D25 is NONEMPTY of dimension 14 with 16/576
\(\mathbb A^{14}\) components per parked fiber/union, both primes.
That sentence survives.

---

## Attack (1) — recompute pivot unit-ness and the 16-component count from the raw `.ms`

**CONFIRMED, 72/72 parked fibers, both primes.**

### Shape and hashes

Parked files: 28 variables, 34 rows, 6096 terms. Unions: 32 variables,
38 rows, 6104 terms. Inverse rows are file rows 24, 25:
`1*W_i*uW_i+(p-1)`. Residual block is file rows 29–33, each affine of
degree 1 in the six lifts \(\{x_{33},x_{38},x_{16},x_{19},x_{24},x_{27}\}\)
and of rank 4 as a 5-row polynomial matrix (unique constant syzygy).
sha256 of all 74 local files matches `d25_certificate_replay.json`.

### Lift minor

The \(R_1,R_2\) minor in \((x_{33},x_{38})\) is a single Laurent
monomial at every fiber:

\[
\Delta = s\cdot uW_1^2 uW_2^2,
\]

with \(s\neq 0\). On `a00pp` the scalars are exactly the claimed
75772 (p = 105337) and 9899 (p = 105673). Across all 72 fibers the
monomial is uniformly \(uW_1^2 uW_2^2\); the scalar takes three
nonzero values per prime (105337: \(\{75772,58759,76143\}\)). Each is
a Laurent unit on the chart. The identity

\[
R_2+6R_3+30R_4+144R_5=0
\]

holds as a polynomial identity on all 72 fibers (unique up to scale:
residual row-rank 4). The three-dimensional left kernel of the
constant \(5\times 2\) matrix of \((x_{33},x_{38})\) coefficients,
applied to the five residuals, produces three lift-free compatibility
rows of rank 2 (the syzygy direction is in the kernel and kills the
inhomogeneous part). So lift rank is exactly 2 and the other four
lifts lie in the span of \((x_{33},x_{38})\) over the base ring.

### Unit-linear DAG

Independent greedy elimination, refusing only \(\{W_1,W_2,uW_1,uW_2\}\)
as pivot variables, finds exactly 10 unit-linear \(x\)-pivots on every
fiber (72/72), every leading coefficient a nonzero scalar times a
Laurent monomial in \(\{W_1,W_2,uW_1,uW_2\}\), substitution acyclic
by construction. Forbidding the four claimed free lifts forces the
Sol-style sequence on `a00pp` (both primes)

\[
x_{70},x_{53},x_{58},x_{33},x_{38},x_{55},x_{71},x_{52},x_{47},x_{54}
\]

with units of the form \(1\), \(s\cdot uW_i\), \(s\cdot uW_i^2\),
\(s\cdot W_i^2\). The eight base pivots are the claimed set
\(\{x_{71},x_{55},x_{70},x_{53},x_{58},x_{52},x_{47},x_{54}\}\). The
fourteen unsolved \(x\)-variables are exactly Sol’s

\[
T\cup\{x_{16},x_{19},x_{24},x_{27}\},
\quad
T=(x_{57},x_{59},x_{60},x_{62},x_{63},x_{65},x_{66},x_{68},x_{72},x_{73}).
\]

Unrestricted greedy on `a00pp` pivots \(x_{19},x_{27}\) instead of
\(x_{33},x_{38}\). That is a different trivialization of the same
rank-2 lift block, not a hidden cut: the remaining equations are still
\(W\)-only, and fourteen \(x\)-variables remain absent from them.

### Terminal \(6\times 3\) and 16 components

After the 10 pivots, exactly six nonzero rows remain, all trinomials
in \((W_1^4,W_2^4,1)\). On `a00pp` they are coefficient-exact for the
matrices printed in `sol-ideas-0821.md`, rank 2, RREF

\[
\begin{pmatrix}1&0&47664\\0&1&52125\end{pmatrix}
\pmod{105337},
\qquad
\begin{pmatrix}1&0&61274\\0&1&13635\end{pmatrix}
\pmod{105673},
\]

hence \((W_1^4,W_2^4)=(57673,53212)\) and \((44399,92038)\). Both
constants are nonzero fourth powers (\(c^{(p-1)/4}=1\)); \(p\equiv 1
\pmod 8\), so each has exactly four fourth roots in \(\mathbb F_p\).
16 components. Recomputed on all 72 fibers: always rank 2, always
nonzero fourth powers, always 16. There are 9 distinct \((c_1,c_2)\)
pairs per prime (the `a00**` quartet shares one pair, as 9.S2 says);
that is a fiber invariant, not a failure of “16 copies per fiber.”

The two quartics are separable (\(4W_i^3\neq 0\) at every root:
\(p\neq 2\), \(W_i\neq 0\)). Distinct \((W_1,W_2)\) give disjoint
closed subschemes of the ambient affine space. Each component is the
graph of ten polynomial functions of the fourteen free \(x\)-variables
over a single \(W\)-point, hence isomorphic to \(\mathbb A^{14}\) as
an \(\mathbb F_p\)-scheme.

---

## Attack (2) — is the residual system after the 10 pivots genuinely free? Is hcore/hlin membership complete?

**CONFIRMED. No hidden relations among the 14 remaining variables.
hcore/hlin lie in the original (not merely localized) ideal.**

### Residual freedom

The remainder test is the one that can actually kill \(\mathbb A^{14}\).
After substituting the 10 unit-linear solves and reducing
\(W_i uW_i=1\), the 34 source rows become:

- 28 zeros, and
- 6 trinomials in \((W_1^4,W_2^4,1)\) of rank 2,

with **no** remaining support on \(T\) or on the four free lifts, on
every one of the 72 fibers. A polynomial relation among the 14 would
have to appear here. It does not. The 14 coordinates are algebraically
independent in the quotient; the \(W\)-fiber is the finite étale
algebra \(\mathbb F_p[W_1^{\pm1},W_2^{\pm1}]/(W_1^4-c_1,W_2^4-c_2)\).

Both inclusions of the identification close on the chart:

- *no overcut:* the 10 pivot equations are (after unit scaling)
  constant-linear combinations of emitted rows, or emitted rows
  themselves;
- *no undercut:* every emitted row reduces to zero modulo the
  triangular generators.

So \(V_{25,\ell}\) equals the triangular scheme, not merely contains
a 14-dimensional constructible piece of it.

### hcore / hlin membership

Sol’s printed sparse rows (5 terms and 3 terms) were checked as
elements of the \(\mathbb F_p\)-span of the three raw Cramer
compatibility rows \(k\cdot(R_1,\ldots,R_5)\), \(k\) running over a
basis of the left kernel of the constant \(5\times 2\) lift matrix.
Membership holds at both primes, with explicit combination
coefficients (105337: hcore \((75623,62104,0)\), hlin
\((43233,43233,0)\); 105673: \((4463,22315,0)\) and
\((83358,83358,0)\)). Those Cramer rows are *constant*-linear
combinations of residuals, hence lie in the ideal generated by the
34 emitted rows **before** any localization and without the stored
D23 Gröbner basis. 9.S2’s weaker “chart-localized” language is
conservative, not a hole. The raw-compat matrix has rank 2 (the third
direction is the residual syzygy). Using hcore/hlin as pivot sources
is equivalent to using residual rows 30–31 after the lift solve, which
is what the independent greedy DAG actually does.

---

## Attack (3) — saturation / chart: do the Laurent-unit pivots invert quantities that vanish on the honest scheme?

**CONFIRMED that they do not. The inverse rows are in the input.**

File rows 24 and 25 are \(W_i uW_i-1=0\). Every point of the emitted
affine scheme has \(W_i,uW_i\in\mathbb F_p^\times\). Consequently:

- \(\Delta = s\cdot uW_1^2 uW_2^2\) is a unit on \(V\), not only on a
  Zariski-open chart someone might forget to impose;
- every recorded pivot coefficient (scalar, \(uW_i\), \(uW_i^2\),
  \(W_i^2\)) is a unit on \(V\);
- dividing by a pivot unit is an automorphism of \(\mathcal O_V\),
  not a saturation that could discard a component with \(uW=0\).

There is no component with \(uW=0\): it would contradict row 24/25.
Dropping those two rows would indeed make the rank of \(\Delta\)
collapse at \(uW=0\), and §9 / 9.S2’s chart pin \(W_1 W_2\neq 0\)
with the inverse rows present is the correct warning. It is not a
caveat *inside* the emitted object. This is the same saturation
pattern already confirmed for det23 in `xmodel/grok-det23-review.md`
claim (2).

---

## Attack (4) — dimension bookkeeping 10+4 versus D23 (11 in 22 variables)

**CONSISTENT. ECO-D25’s number 13 is refuted independently of
re-proving D23 dimension 11.**

Parked ambient: 28 variables = 22 D23-base + 6 lifts. The triangular
count is

\[
28 - 10\text{ (unit-linear \(x\)-graphs)} - 2\text{ (inverses)} - 0_{\mathrm{Krull}}\text{ (two separable quartics)}
= 14.
\]

Equivalently: 10 free base coordinates \(T\) plus 4 free lifts.
The two quartics cut the \(W\)-line to 16 rational points and add no
Krull dimension.

D23 dimension 11 in 22 variables is the atlas LT-staircase fact
(`det23.max_indep_set` length 11, recorded uniformly; not re-GBed
here). The D25 free base \(T\) is not the D23 independent set: D23’s
11 is \(\{x_{55},x_{58},x_{59},x_{60},x_{62},x_{63},x_{65},x_{66},x_{68},x_{71},x_{73}\}\);
D25’s 10 is \(T\). Intersection 8, D23-only \(\{x_{55},x_{58},x_{71}\}\)
(exactly three of the D25 base pivots), D25-only \(\{x_{57},x_{72}\}\).
That is \(11-3+2=10\), a height-one cut plus a coordinate change, not
a height-two cut.

ECO-D25 (`xmodel/sol-codim2.md`, locked 2026-08-21T03:04:29Z, before
any D25 dimension existed) pre-registered full-lane dimension 13, i.e.
projected \(11\to 9\) plus 4 free lifts. The lock table says
explicitly that “NONEMPTY, dimension 14” means projected dimension 10
and **REFUTED**. The observed 14 does that. The refutation of the
headline number 13 does not wait on a fresh D23 Gröbner basis.

Item 2 (carrier): after the same DAG,

\[
\bar q=(24129\,Z+100248)\bigl[(x_{59}-x_{66})+8603\,x_{72}(x_{57}-x_{65})\bigr]
\]

at p = 105337 with \(Z=W_2^2 uW_1^2\), and the analogous identity with
\((6523\,Z+44573)\) at p = 105673. Coefficient-exact against Sol’s
printed forms; the linear factors’ norms are the claimed 23212 and
2824; the \(x_{59}\) coefficient is nonzero on all 16 branches. So
\(q=0\) is a genuine Cartier divisor on every component, \(\dim
H=10\), \(\dim H+(q)=9\), and ECO-D25-CARRIER’s pair \((9,\le 8)\) is
refuted by \(+1\) each. Qualitative carrier (every component meets
\(D(q)\)) holds.

---

## Attack (5) — does 9.S2 state modular + emission-fidelity + chart scope honestly?

**YES.**

The scope box at `SHEET6-DIRECTIONB.md:2332-2336` is the correct one:
modular only, both registered split primes, residue-A / fixed-\(r\) /
B-frozen / no-log / `PIN42` / \(W_1 W_2\neq 0\) chart; emission
fidelity inherited (the objects are the emitted `.ms` rows, not a
re-derivation from jets). It does not claim characteristic zero, a
formal germ, a Keller pair, other charts, or the third prime. Item 5
of `sol-ideas-0821.md` remains labelled CONJECTURE and is not used.
The 48-hour union GB lanes are correctly declared moot as verdict
lanes.

The inherited emission-fidelity caveat is real and load-bearing for
any promotion past “the emitted modular systems,” and 9.S2 does not
launder it. Section 9’s own header already scoped the family object
the same way. This review attacks the *emitted* triangular
certificate; it does not re-run `d25_assemble.py` against the jets
bank.

---

## Witnesses, Jacobians, union, controls

| check | 105337 | 105673 |
|---|---|---|
| `a00pp` all-\(x\)-zero witness \((W_1,W_2,uW_1,uW_2)\) | (31931, 9457, 64754, 22756), 34/34 | (8021, 20111, 13662, 64399), 34/34 |
| derived all-\(x\)-zero witness, 36 parked fibers | 34/34 at 36/36 | 34/34 at 36/36 |
| union at Sol’s selector + same \(W\) | 38/38 | 38/38 |
| Jacobian of the *unreduced* 34 (resp. 38) rows at that point | 14 in 28 | 14 in 28; union 18 in 32 |
| selector \(\mathbb F_p\)-points | \(3\times 3\times 2\times 2=36\) | 36 |
| union specialized at each atlas fiber vs parked file | 36/36, scale 1 on all 1224 rows | 36/36, scale 1 on all 1224 rows |
| union components | \(36\times 16=576\) | 576 |
| seed-20260821 3-coordinate perturbations of `a00pp` witness | 6–12 rows survive (never 0 fail-to-vanish) | 6–12 |
| 3 fully random points | 0/34 vanish | 0/34 |

Jacobian pitfall, recorded so it is not re-litigated: reducing
\(W_i uW_i=1\) *before* differentiating deletes the inverse rows and
drops the rank by 2 (12/16). The honest Jacobian is of the emitted
polynomials. Rank 14 (parked) / 18 (union) then matches embedding
codimension of a smooth 14-dimensional (resp. still 14-dimensional,
plus 4 independent selector equations) subscheme at the witness.
Together with the graph presentation this is smoothness of the whole
scheme, not a one-point curiosity.

---

## ECO-D25

Pre-registration (`xmodel/sol-codim2.md:688-700`): observed
NONEMPTY dimension 14 \(\Rightarrow\) projected quotient dimension 10
\(\Rightarrow\) **REFUTED**. Found that, uniformly, both primes, all
36 fibers, both unions. The mechanism pieces that the lock said would
*not* be refuted by a mere \(+1\) — NONEMPTY, within-prime
equivariant uniformity, cross-prime agreement, the residual syzygy
\(R_2+6R_3+30R_4+144R_5=0\), lift rank 2, full residual rank 4, \(q\)
a genuine divisor meeting every component — all held.

---

## Nits (non-load-bearing)

1. Sol’s printed \(14\times 14\) minors \(\det=9870\) and \(39560\)
   were not recovered among the natural 14-column complements tried
   (the 10 pivoted \(x\)’s plus four \(W/uW\)). Rank 14 of that
   \(34\times 14\) block is independently confirmed; some minor is
   nonzero. The specific determinants are not needed for smoothness
   or for ECO-D25.
2. Pivot *order* is not unique. Sol’s writeup solves \(x_{33},x_{38}\)
   from \(R_1,R_2\) and \(x_{71},x_{55}\) from printed hcore/hlin;
   unrestricted greedy prefers \(x_{19},x_{27}\) and residual rows
   30–31. Same free 14-set (up to trading the rank-2 lift pair), same
   terminal \(6\times 3\).
3. Box01 byte-identity of the 74 `.ms` files was not re-checked by
   ssh; local copies match the replay JSON hashes. The mathematical
   object reviewed is the local emission.
4. D23 dimension 11 is inherited from the atlas LT-staircase / prior
   reviews, not re-proved. The D25 dimension-14 count and the
   refutation of ECO-D25’s 13 do not depend on it.

---

## What this does not say

Nothing here is a characteristic-zero D25 statement, a formal-germ
statement, a Hensel certificate, or a statement on any other chart.
Emission fidelity of `d25_assemble.py` versus the jets bank is the
inherited section-9 caveat and is not discharged. Sol item 5 (replay
the ten pivots over the selector/radical number field) remains the
bridge, and remains CONJECTURE.
