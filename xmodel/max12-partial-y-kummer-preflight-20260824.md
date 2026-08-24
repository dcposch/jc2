# Exact maximum-12 partial-`y` Kummer preflight: `(8,12)` and `(9,12)`

**Status: `PRODUCER-INTERNAL, SOURCE-HONEST, FROZEN FOR DIFFERENT-MODEL REVIEW`.**

**Verdict.**  Starting only from the reviewed shear/UFD history, the two
primitive maximum-12 residues have the following exact first routing:

```text
(8,12):  residual exactly when 4|H; Kummer orders 4,2,1;
(9,12):  residual exactly when 3|H; Kummer orders 3,1.
```

For every nontrivial Kummer order, including the intermediate quadratic
order in `(8,12)`, the first depression mismatch is forced to zero.  On the
trivial class it is not weight-forced.  Both original `y=0` Taylor
boundaries remain charged in every branch.

There are two different cost comparisons, and they must not be conflated.
The raw depressed constant-W gate is exactly smaller for `(8,12)` (18
variables and 17 positive-degree rows, versus 19 and 18), and it retains the
already familiar `2:3` signature.  The full Kummer branch tree is simpler
for `(9,12)` (two leaves instead of three).  Before high-row integration,
there is no honest exact ordering of the cost of *closing the whole cell*.

This report derives no high-row Faber system, classifies no constant-W
component, proves neither residue empty, and makes no Jacobian-conjecture
claim.  It is independent of the maximum-11 composition review.

## 1. Consumed theorem input

Only these two immutable history artifacts are consumed:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/as109-partial-y-history-stop-20260824.md` | `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe` | shear/UFD theorem and residual criterion |
| `xmodel/as109-partial-y-history-review-grok-20260824.md` | `f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd` | different-model confirmation |

The later `(6,9)` reduction and trajectory artifacts are used only in
Section 6 to label reusable *methods*.  None of their exclusions is an
input here.

## 2. Common `(dr,ds)` umbrella

Let the actual `y`-degrees be

```text
m=dr,  n=ds,  gcd(r,s)=1,
```

and write the leading coefficients, after harmless nonzero target scalings,
as

```text
a_m=h^r,       b_n=h^s.
```

The reviewed large-source-shear theorem closes a row whenever
`gcd(H,d)` is one or two, where `H=deg h`.  No stronger history theorem is
silently assumed below.

Adjoin `u` with `u^d=h`, so `a_m=u^m`, `b_n=u^n`, and define

```text
A = a_(m-1)/u^(m-1),       B = b_(n-1)/u^(n-1).
```

The coefficient of `y^(m+n-2)` in the original Jacobian is

```text
(n-1)(u^m)'u^(n-1)B + n(u^(m-1)A)'u^n
-m u^m(u^(n-1)B)' -(m-1)u^(m-1)A(u^n)'

= u^(m+n-1)(nA'-mB')
= d u^(d(r+s)-1)(sA-rB)'.                         (2.1)
```

All logarithmic derivatives of `u` cancel.  Hence the exact first constant
is

```text
delta = sA-rB in k.                                  (2.2)
```

Put

```text
z = uy + A/m.
```

Then the `z^(m-1)` coefficient of the first coordinate vanishes, and the
`z^(n-1)` coefficient of the second is

```text
B-(n/m)A = -delta/r.                                 (2.3)
```

Thus `delta` is simultaneously the integrated next row and the first
depression mismatch.

### Kummer-order split, including proper divisors of `d`

Work after a harmless scalar extension containing the needed roots of
unity.  Let the class of `h` in `k(x)^*/k(x)^{*d}` have order `e|d`.
The minimal root extension has degree `e`.  If `e>1`, its generator sends
`u` to `zeta u`.  Since `e|m,n`,

```text
wt(A)=-(m-1)=1 mod e,       wt(B)=-(n-1)=1 mod e.
```

But `delta` in (2.2) belongs to the fixed field and also has weight one.
Therefore

```text
e>1  =>  delta=0.                                    (2.4)
```

This argument applies unchanged to the order-two class inside `d=4`; it
does not pretend that this branch has the later mod-four constant filter.
If `e=1`, divisor valuations and Gauss give `h=c q^d` with `q in k[x]`
(after absorbing the constant), so `u=q` is polynomial.  There is then no
nontrivial character and `delta` is weight-unforced.

### Boundary provenance

Write the depressed coordinates as

```text
f(z)=P(x,(z-A/m)/u),       g(z)=Q(x,(z-A/m)/u).
```

Because `y=0` is exactly `z=A/m`, every original polynomial coefficient is
still imposed through

```text
u^ell/ell! * partial_z^ell f(A/m) = [y^ell]P in k[x],
u^ell/ell! * partial_z^ell g(A/m) = [y^ell]Q in k[x]. (2.5)
```

These hold for `0<=ell<=m` and `0<=ell<=n`, respectively.  Thus neither
coordinate boundary may be discarded after passing to the root extension.

## 3. Exact cell routing

| Cell | `(d,r,s)` | History residue | Leading powers | Root and Kummer orders | `delta`; second mismatch |
|---|---:|---|---|---|---|
| `(8,12)` | `(4,2,3)` | `gcd(H,4)=4`, equivalently `4|H` | `a_8=h^2`, `b_12=h^3` | `u^4=h`; orders `4,2,1` | `3A-2B`; `-delta/2` |
| `(9,12)` | `(3,3,4)` | `gcd(H,3)=3`, equivalently `3|H` | `a_9=h^3`, `b_12=h^4` | `u^3=h`; orders `3,1` | `4A-3B`; `-delta/3` |

For `(8,12)`, the exact next row after removing `u^19` is
`12A'-8B'=4(3A-2B)'`; the depression is `z=uy+A/8`.
For `(9,12)`, after removing `u^20` it is
`12A'-9B'=3(4A-3B)'`; the depression is `z=uy+A/9`.

The possible later target constants of a term `c_j z^j` have weight `-j`.
This is only a character filter, not an assertion that integration actually
produces or preserves every listed constant:

| Cell / class order | Minimal extension | `delta` | Potential weight-zero indices `0<=j<=10` |
|---|---:|---|---|
| `(8,12)`, `e=4` | 4 | zero | `0,4,8` |
| `(8,12)`, `e=2` | 2 | zero | `0,2,4,6,8,10` |
| `(8,12)`, `e=1` | 1 | unforced | all indices |
| `(9,12)`, `e=3` | 3 | zero | `0,3,6,9` |
| `(9,12)`, `e=1` | 1 | unforced | all indices |

Exact divisor controls at the smallest residual degrees are:

```text
d=4, order 4: h=x(x-1)(x-2)(x-3), residues 1,1,1,1,-4;
d=4, order 2: h=x^2(x-1)^2,       residues 2,2,-4;
d=4, order 1: h=x^4,               residues 4,-4;
d=3, order 3: h=x(x-1)(x-2),       residues 1,1,1,-3;
d=3, order 1: h=x^3,               residues 3,-3.
```

In particular, the order-two leaf is a genuine minimal quadratic extension,
not a degenerate notation for the quartic or polynomial leaf.

## 4. Portable binary gate and exact raw width

The new cells have not yet been proved to land on a complete Faber system.
Conditionally on the usual constant binary-Jacobian landing, however, its
algebraic gate and raw width are exact.  For monic depressed univariate cores
`f,g` of degrees `dr,ds`, let their binary homogenizations be `F,G`.
Euler's identity gives, at `t=1`,

```text
J_(t,z)(F,G) = d W,
W = r f g_z - s f_z g.                               (4.1)
```

The zero-W locus has an exact common-power description.  Indeed `W=0`
implies `(f^s/g^r)'=0`; monicity and UFD, with `gcd(r,s)=1`, give

```text
f=K^r,       g=K^s,       K monic depressed, deg K=d. (4.2)
```

Conversely (4.2) makes `W=0`.  With `D=f^s-g^r`, the useful route identity
is

```text
f D' - s f'D = -W g^(r-1).                           (4.3)
```

Thus the two cells share one umbrella but not one signature:

```text
(8,12): W=2 f g_z-3 f_z g;  common locus (K^2,K^3), deg K=4;
(9,12): W=3 f g_z-4 f_z g;  common locus (K^3,K^4), deg K=3.
```

After monicity and the two depressions, the constant-W coefficient gates
have the following exact first sizes.  The tangent ranks are computed over
`Q` at the squarefree point `K=z^d+z+1`; they are a local singularity check,
not a global component classification.

| Cell | Depressed variables | Positive-degree W rows | Tangent rank | Kernel | Common-K tangent parameters |
|---|---:|---:|---:|---:|---:|
| `(8,12)` | 18 | 17 | 11 | 7 | 3 |
| `(9,12)` | 19 | 18 | 11 | 8 | 2 |

Both gates are highly singular along their common-power loci: the displayed
kernels are larger than the common-K tangent spaces.  The exact raw gate is
therefore smaller for `(8,12)`.  Separately, `(9,12)` has the smaller branch
tree because there is no proper nontrivial Kummer divisor.  These facts do
not prove that one complete cell closure will be cheaper than the other.

## 5. Reuse and type failure of `(6,9)` machinery

Genuinely reusable without importing a conclusion:

1. the leading UFD and source-shear route;
2. root-extension normalization, the next-row cancellation, depression,
   mismatch character, and all charged Taylor boundaries;
3. Euler reduction to a binary Wronskian, the common-power/UFD lemma, and
   the route identity (4.3);
4. target affine gauges at the abstract level; and
5. valuation, genus, and rational-trajectory methods *after* the new exact
   curves and denominators have been derived.

The `(8,12)` leaf has the same exponent signature `2:3`, so the organization
of a Faber calculation is the closest analogue.  The core degree is four,
however, and the order-two branch has only parity weights; neither change is
cosmetic.

The following are type-specific and cannot be imported: the exact `(6,9)`
Faber coefficients and five Laurent potentials, its Kuranishi quadrics,
the lower-Pfaffian two-sheet decomposition, exceptional polynomials, DS
resultants, finite-pole exponent table, and trajectory reconstruction.
For `(9,12)`, even the Wronskian signature changes from `2:3` to `3:4`.

## 6. Cheapest falsifiers and recommended bounded successors

1. **Smallest raw gate:** derive only the first integrated/high-row Faber
   block for the full-order `(8,12)` leaf.  Reuse the `2:3` organization but
   recompute every coefficient.  Stop if the nonzero constant row survives
   the transverse cokernel.
2. **Mandatory adversarial control for `(8,12)`:** use
   `h=x^2(x-1)^2`.  The replay certifies a quadratic root extension and
   `delta=0`, while all even target weights remain allowed.  Integrate only
   to the first nonlinear compatibility.  Any argument using mod-four
   vanishing on this leaf is falsified immediately.
3. **Clean branch-tree control for `(9,12)`:** compare
   `h=x(x-1)(x-2)` (order three, formal `delta` must die) with `h=x^3`
   (polynomial core, a nonzero formal mismatch must remain legal), then
   derive the first `3:4` high-row block.

The cheapest experiment separating the two allocations is therefore two
small symbolic triangular integrations, one for the order-four `2:3` leaf
and one for the order-three `3:4` leaf, terminated at the first nonlinear
compatibility.  No generic coefficient rectangle is justified by this
preflight.

## 7. Replay and scope

Run:

```sh
python3 cases/max12_partial_y_preflight_20260824/replay.py
```

The pure-stdlib replay pins both theorem inputs, enumerates the residual
`H` classes, checks (2.1), verifies all five example Kummer orders from
divisor residues, audits the character filters and boundary formulas,
verifies the common-power Wronskians and (4.3) on exact polynomials, and
computes the two rational tangent ranks.  It performs no high-row
coefficient search.

Its terminal scope is:

```text
full_high_row_integration=NOT_DONE
constant_W_components=NOT_CLASSIFIED
either_frontier_empty=false
JC2=NOT_CLAIMED
```
